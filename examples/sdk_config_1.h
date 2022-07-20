#ifndef SDK_CONFIG_H
#define SDK_CONFIG_H

#ifdef USE_APP_CONFIG
#    include "app_config.h"
#endif
// <h> Board Support

//==========================================================
// <q> BSP_BTN_BLE_ENABLED  - bsp_btn_ble - Button Control for BLE

#ifndef BSP_BTN_BLE_ENABLED
#    define BSP_BTN_BLE_ENABLED 1
#endif

// </h>
//==========================================================

// <h> nRF_BLE

//==========================================================
// <q> BLE_ADVERTISING_ENABLED  - ble_advertising - Advertising module

#ifndef BLE_ADVERTISING_ENABLED
#    define BLE_ADVERTISING_ENABLED 1
#endif

// <e> BLE_DTM_ENABLED - ble_dtm - Module for testing RF/PHY using DTM commands
//==========================================================
#ifndef BLE_DTM_ENABLED
#    define BLE_DTM_ENABLED 0
#endif

// <o> NRF_RADIO_ANTENNA_COUNT
#ifndef NRF_RADIO_ANTENNA_COUNT
#    define NRF_RADIO_ANTENNA_COUNT 12
#endif

// <o> DTM_RADIO_IRQ_PRIORITY - RADIO interrupt priority
#ifndef DTM_RADIO_IRQ_PRIORITY
#    define DTM_RADIO_IRQ_PRIORITY 2
#endif

// <o> DTM_TIMER_IRQ_PRIORITY - DTM timer interrupt priority
#ifndef DTM_TIMER_IRQ_PRIORITY
#    define DTM_TIMER_IRQ_PRIORITY 3
#endif

// <o> DTM_ANOMALY_172_TIMER_IRQ_PRIORITY - DTM anomaly 172 timer interrupt priority
#ifndef DTM_ANOMALY_172_TIMER_IRQ_PRIORITY
#    define DTM_ANOMALY_172_TIMER_IRQ_PRIORITY 2
#endif

#endif // SDK_CONFIG_H
