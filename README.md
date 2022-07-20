# nrf_sdk_sdkconfig_diff

This is a script I made to compare **sdk_config.h** files in the [NRF5 SDK](https://www.nordicsemi.com/Products/Development-software/nrf5-sdk).

This script will only print the differences, all the similar defines will be ignored.

# Install

1. Clone this repository
2. **pip install -r requirements.txt**
3. run the script

# Usage

```
$ USAGE: ./compare_sdkconfig.py sdk_config1 sdk_config2 [...]
```

# Examples

With 2 files:

```
$ ./compare_sdkconfig.py examples/sdk_config_1.h examples/sdk_config_2.h
╒════════════════════════════════════╤═══════════════════╤═══════════════════╕
│ Define                             │   examples/sdk_co │ examples/sdk_co   │
│                                    │          nfig_1.h │ nfig_2.h          │
╞════════════════════════════════════╪═══════════════════╪═══════════════════╡
│ NRF_RADIO_ANTENNA_COUNT            │                12 │ 3                 │
├────────────────────────────────────┼───────────────────┼───────────────────┤
│ DTM_ANOMALY_172_TIMER_IRQ_PRIORITY │                 2 │ None              │
╘════════════════════════════════════╧═══════════════════╧═══════════════════╛
```

With 3 files:
```
$ ./compare_sdkconfig.py examples/sdk_config_1.h examples/sdk_config_2.h examples/sdk_config_3.h
╒════════════════════════════════════╤═══════════════════╤═══════════════════╤═══════════════════╕
│ Define                             │   examples/sdk_co │ examples/sdk_co   │ examples/sdk_co   │
│                                    │          nfig_1.h │ nfig_2.h          │ nfig_3.h          │
╞════════════════════════════════════╪═══════════════════╪═══════════════════╪═══════════════════╡
│ BSP_BTN_BLE_ENABLED                │                 1 │ 1                 │ 0                 │
├────────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ BLE_ADVERTISING_ENABLED            │                 1 │ 1                 │ 23                │
├────────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ NRF_RADIO_ANTENNA_COUNT            │                12 │ 3                 │ 6                 │
├────────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ DTM_TIMER_IRQ_PRIORITY             │                 3 │ 3                 │ None              │
├────────────────────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ DTM_ANOMALY_172_TIMER_IRQ_PRIORITY │                 2 │ None              │ 2                 │
╘════════════════════════════════════╧═══════════════════╧═══════════════════╧═══════════════════╛
```

**None** is for when a define doesn't exists in the file.

# License

See [LICENSE](./LICENSE)
