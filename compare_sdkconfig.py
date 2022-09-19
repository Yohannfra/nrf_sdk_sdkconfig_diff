#!/usr/bin/env python3

import sys
from typing import List, Tuple
import re
from tabulate import tabulate
import textwrap

def get_all_defines(fp: str) -> List[str]:
    with open(fp, 'r') as f:
        all_defines: List[str] = []
        for l in f.readlines():
            if re.match(r"#[ \t]{0,}define", l):
                all_defines.append(l.strip().replace("#    define", "#define"))
        return all_defines


def get_define_key_val(line: str) -> Tuple[str, str]:
    spl = line.split()

    if len(spl) == 2:
        define_key = spl[1]
        define_val = spl[1]
    elif len(spl) >= 3:
        define_key = spl[1]
        define_val = "".join(spl[2:]) if len(spl) > 3 else spl[2]
    else:
        sys.exit(f"Invalid define line: {line}")

    return (define_key, define_val)

def get_define_val(define_list: List[str], to_find: str) -> str:
    for d in define_list:
        (define_key, define_val) = get_define_key_val(d)

        if define_key == to_find:
            return define_val
    return "None"

def wrap(s: str) -> str:
    return "\n".join(textwrap.wrap(s, width=15))

def main(argc: int, argv: List[str]) -> None:
    if argc < 3:
        sys.exit(f"USAGE: {argv[0]} sdk_config1 sdk_config2 ...")

    fs_defines = [get_all_defines(v) for v in argv[1:]]

    differences = []
    for define_list in fs_defines:
        for d in define_list:
            vals = []
            for fs_define in fs_defines:
                vals.append(wrap(get_define_val(fs_define, get_define_key_val(d)[0])))

            if vals.count(vals[0]) != len(vals) and [get_define_key_val(d)[0], *vals] not in differences:
                differences.append([get_define_key_val(d)[0], *vals])

    table = [['Define', *[wrap(a) for a in argv[1:]]], *differences]
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
