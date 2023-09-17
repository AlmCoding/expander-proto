/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.7 */

#ifndef PB_UART_PROTO_UART_PB_H_INCLUDED
#define PB_UART_PROTO_UART_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
typedef enum _uart_proto_UartId {
    uart_proto_UartId_UART0 = 0,
    uart_proto_UartId_UART1 = 1
} uart_proto_UartId;

/* Struct definitions */
typedef struct _uart_proto_UartConfig {
    uint32_t baud_rate;
} uart_proto_UartConfig;

typedef PB_BYTES_ARRAY_T(256) uart_proto_UartData_tx_data_t;
typedef struct _uart_proto_UartData {
    uart_proto_UartData_tx_data_t tx_data;
} uart_proto_UartData;

typedef PB_BYTES_ARRAY_T(256) uart_proto_UartStatus_rx_data_t;
typedef struct _uart_proto_UartStatus {
    bool rx_overflow;
    bool tx_overflow;
    bool tx_complete;
    uint32_t tx_space;
    uint32_t rx_space;
    uart_proto_UartStatus_rx_data_t rx_data;
} uart_proto_UartStatus;

typedef struct _uart_proto_UartMsg {
    uart_proto_UartId uart_id;
    uint32_t sequence_number;
    pb_size_t which_msg;
    union {
        uart_proto_UartConfig cfg;
        uart_proto_UartData data;
        uart_proto_UartStatus status;
    } msg;
} uart_proto_UartMsg;


#ifdef __cplusplus
extern "C" {
#endif

/* Helper constants for enums */
#define _uart_proto_UartId_MIN uart_proto_UartId_UART0
#define _uart_proto_UartId_MAX uart_proto_UartId_UART1
#define _uart_proto_UartId_ARRAYSIZE ((uart_proto_UartId)(uart_proto_UartId_UART1+1))




#define uart_proto_UartMsg_uart_id_ENUMTYPE uart_proto_UartId


/* Initializer values for message structs */
#define uart_proto_UartConfig_init_default       {0}
#define uart_proto_UartData_init_default         {{0, {0}}}
#define uart_proto_UartStatus_init_default       {0, 0, 0, 0, 0, {0, {0}}}
#define uart_proto_UartMsg_init_default          {_uart_proto_UartId_MIN, 0, 0, {uart_proto_UartConfig_init_default}}
#define uart_proto_UartConfig_init_zero          {0}
#define uart_proto_UartData_init_zero            {{0, {0}}}
#define uart_proto_UartStatus_init_zero          {0, 0, 0, 0, 0, {0, {0}}}
#define uart_proto_UartMsg_init_zero             {_uart_proto_UartId_MIN, 0, 0, {uart_proto_UartConfig_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define uart_proto_UartConfig_baud_rate_tag      1
#define uart_proto_UartData_tx_data_tag          1
#define uart_proto_UartStatus_rx_overflow_tag    1
#define uart_proto_UartStatus_tx_overflow_tag    2
#define uart_proto_UartStatus_tx_complete_tag    3
#define uart_proto_UartStatus_tx_space_tag       4
#define uart_proto_UartStatus_rx_space_tag       5
#define uart_proto_UartStatus_rx_data_tag        6
#define uart_proto_UartMsg_uart_id_tag           1
#define uart_proto_UartMsg_sequence_number_tag   2
#define uart_proto_UartMsg_cfg_tag               3
#define uart_proto_UartMsg_data_tag              4
#define uart_proto_UartMsg_status_tag            5

/* Struct field encoding specification for nanopb */
#define uart_proto_UartConfig_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   baud_rate,         1)
#define uart_proto_UartConfig_CALLBACK NULL
#define uart_proto_UartConfig_DEFAULT NULL

#define uart_proto_UartData_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BYTES,    tx_data,           1)
#define uart_proto_UartData_CALLBACK NULL
#define uart_proto_UartData_DEFAULT NULL

#define uart_proto_UartStatus_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BOOL,     rx_overflow,       1) \
X(a, STATIC,   SINGULAR, BOOL,     tx_overflow,       2) \
X(a, STATIC,   SINGULAR, BOOL,     tx_complete,       3) \
X(a, STATIC,   SINGULAR, UINT32,   tx_space,          4) \
X(a, STATIC,   SINGULAR, UINT32,   rx_space,          5) \
X(a, STATIC,   SINGULAR, BYTES,    rx_data,           6)
#define uart_proto_UartStatus_CALLBACK NULL
#define uart_proto_UartStatus_DEFAULT NULL

#define uart_proto_UartMsg_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    uart_id,           1) \
X(a, STATIC,   SINGULAR, UINT32,   sequence_number,   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,cfg,msg.cfg),   3) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,data,msg.data),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,status,msg.status),   5)
#define uart_proto_UartMsg_CALLBACK NULL
#define uart_proto_UartMsg_DEFAULT NULL
#define uart_proto_UartMsg_msg_cfg_MSGTYPE uart_proto_UartConfig
#define uart_proto_UartMsg_msg_data_MSGTYPE uart_proto_UartData
#define uart_proto_UartMsg_msg_status_MSGTYPE uart_proto_UartStatus

extern const pb_msgdesc_t uart_proto_UartConfig_msg;
extern const pb_msgdesc_t uart_proto_UartData_msg;
extern const pb_msgdesc_t uart_proto_UartStatus_msg;
extern const pb_msgdesc_t uart_proto_UartMsg_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define uart_proto_UartConfig_fields &uart_proto_UartConfig_msg
#define uart_proto_UartData_fields &uart_proto_UartData_msg
#define uart_proto_UartStatus_fields &uart_proto_UartStatus_msg
#define uart_proto_UartMsg_fields &uart_proto_UartMsg_msg

/* Maximum encoded size of messages (where known) */
#define uart_proto_UartConfig_size               6
#define uart_proto_UartData_size                 259
#define uart_proto_UartMsg_size                  288
#define uart_proto_UartStatus_size               277

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
