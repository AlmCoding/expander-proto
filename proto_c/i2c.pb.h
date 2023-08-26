/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.7 */

#ifndef PB_I2C_PROTO_I2C_PB_H_INCLUDED
#define PB_I2C_PROTO_I2C_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
typedef enum _i2c_proto_I2cId {
    i2c_proto_I2cId_I2C0 = 0,
    i2c_proto_I2cId_I2C1 = 1
} i2c_proto_I2cId;

/* Struct definitions */
typedef struct _i2c_proto_I2cConfig {
    uint32_t clock_rate;
} i2c_proto_I2cConfig;

typedef PB_BYTES_ARRAY_T(256) i2c_proto_I2cMasterData_data_t;
typedef struct _i2c_proto_I2cMasterData {
    uint32_t request_id;
    uint32_t slave_addr;
    i2c_proto_I2cMasterData_data_t data;
    uint32_t read_size;
} i2c_proto_I2cMasterData;

typedef PB_BYTES_ARRAY_T(8) i2c_proto_I2cSlaveData_pattern_t;
typedef PB_BYTES_ARRAY_T(256) i2c_proto_I2cSlaveData_data_t;
typedef struct _i2c_proto_I2cSlaveData {
    uint32_t request_id;
    i2c_proto_I2cSlaveData_pattern_t pattern;
    i2c_proto_I2cSlaveData_data_t data;
} i2c_proto_I2cSlaveData;

typedef struct _i2c_proto_I2cStatus {
    uint32_t master_queue_space;
    uint32_t master_buffer_space;
    bool master_overflow;
    uint32_t slave_dict_space;
    uint32_t slave_buffer_space;
    bool slave_overflow;
} i2c_proto_I2cStatus;

typedef struct _i2c_proto_I2cMsg {
    i2c_proto_I2cId i2c_id;
    uint32_t sequence_number;
    pb_size_t which_msg;
    union {
        i2c_proto_I2cConfig cfg;
        i2c_proto_I2cMasterData master;
        i2c_proto_I2cSlaveData slave;
        i2c_proto_I2cStatus status;
    } msg;
} i2c_proto_I2cMsg;


#ifdef __cplusplus
extern "C" {
#endif

/* Helper constants for enums */
#define _i2c_proto_I2cId_MIN i2c_proto_I2cId_I2C0
#define _i2c_proto_I2cId_MAX i2c_proto_I2cId_I2C1
#define _i2c_proto_I2cId_ARRAYSIZE ((i2c_proto_I2cId)(i2c_proto_I2cId_I2C1+1))





#define i2c_proto_I2cMsg_i2c_id_ENUMTYPE i2c_proto_I2cId


/* Initializer values for message structs */
#define i2c_proto_I2cConfig_init_default         {0}
#define i2c_proto_I2cMasterData_init_default     {0, 0, {0, {0}}, 0}
#define i2c_proto_I2cSlaveData_init_default      {0, {0, {0}}, {0, {0}}}
#define i2c_proto_I2cStatus_init_default         {0, 0, 0, 0, 0, 0}
#define i2c_proto_I2cMsg_init_default            {_i2c_proto_I2cId_MIN, 0, 0, {i2c_proto_I2cConfig_init_default}}
#define i2c_proto_I2cConfig_init_zero            {0}
#define i2c_proto_I2cMasterData_init_zero        {0, 0, {0, {0}}, 0}
#define i2c_proto_I2cSlaveData_init_zero         {0, {0, {0}}, {0, {0}}}
#define i2c_proto_I2cStatus_init_zero            {0, 0, 0, 0, 0, 0}
#define i2c_proto_I2cMsg_init_zero               {_i2c_proto_I2cId_MIN, 0, 0, {i2c_proto_I2cConfig_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define i2c_proto_I2cConfig_clock_rate_tag       2
#define i2c_proto_I2cMasterData_request_id_tag   2
#define i2c_proto_I2cMasterData_slave_addr_tag   3
#define i2c_proto_I2cMasterData_data_tag         4
#define i2c_proto_I2cMasterData_read_size_tag    5
#define i2c_proto_I2cSlaveData_request_id_tag    1
#define i2c_proto_I2cSlaveData_pattern_tag       2
#define i2c_proto_I2cSlaveData_data_tag          3
#define i2c_proto_I2cStatus_master_queue_space_tag 1
#define i2c_proto_I2cStatus_master_buffer_space_tag 2
#define i2c_proto_I2cStatus_master_overflow_tag  3
#define i2c_proto_I2cStatus_slave_dict_space_tag 4
#define i2c_proto_I2cStatus_slave_buffer_space_tag 5
#define i2c_proto_I2cStatus_slave_overflow_tag   6
#define i2c_proto_I2cMsg_i2c_id_tag              1
#define i2c_proto_I2cMsg_sequence_number_tag     2
#define i2c_proto_I2cMsg_cfg_tag                 3
#define i2c_proto_I2cMsg_master_tag              4
#define i2c_proto_I2cMsg_slave_tag               5
#define i2c_proto_I2cMsg_status_tag              6

/* Struct field encoding specification for nanopb */
#define i2c_proto_I2cConfig_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   clock_rate,        2)
#define i2c_proto_I2cConfig_CALLBACK NULL
#define i2c_proto_I2cConfig_DEFAULT NULL

#define i2c_proto_I2cMasterData_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   request_id,        2) \
X(a, STATIC,   SINGULAR, UINT32,   slave_addr,        3) \
X(a, STATIC,   SINGULAR, BYTES,    data,              4) \
X(a, STATIC,   SINGULAR, UINT32,   read_size,         5)
#define i2c_proto_I2cMasterData_CALLBACK NULL
#define i2c_proto_I2cMasterData_DEFAULT NULL

#define i2c_proto_I2cSlaveData_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   request_id,        1) \
X(a, STATIC,   SINGULAR, BYTES,    pattern,           2) \
X(a, STATIC,   SINGULAR, BYTES,    data,              3)
#define i2c_proto_I2cSlaveData_CALLBACK NULL
#define i2c_proto_I2cSlaveData_DEFAULT NULL

#define i2c_proto_I2cStatus_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   master_queue_space,   1) \
X(a, STATIC,   SINGULAR, UINT32,   master_buffer_space,   2) \
X(a, STATIC,   SINGULAR, BOOL,     master_overflow,   3) \
X(a, STATIC,   SINGULAR, UINT32,   slave_dict_space,   4) \
X(a, STATIC,   SINGULAR, UINT32,   slave_buffer_space,   5) \
X(a, STATIC,   SINGULAR, BOOL,     slave_overflow,    6)
#define i2c_proto_I2cStatus_CALLBACK NULL
#define i2c_proto_I2cStatus_DEFAULT NULL

#define i2c_proto_I2cMsg_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    i2c_id,            1) \
X(a, STATIC,   SINGULAR, UINT32,   sequence_number,   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,cfg,msg.cfg),   3) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,master,msg.master),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,slave,msg.slave),   5) \
X(a, STATIC,   ONEOF,    MESSAGE,  (msg,status,msg.status),   6)
#define i2c_proto_I2cMsg_CALLBACK NULL
#define i2c_proto_I2cMsg_DEFAULT NULL
#define i2c_proto_I2cMsg_msg_cfg_MSGTYPE i2c_proto_I2cConfig
#define i2c_proto_I2cMsg_msg_master_MSGTYPE i2c_proto_I2cMasterData
#define i2c_proto_I2cMsg_msg_slave_MSGTYPE i2c_proto_I2cSlaveData
#define i2c_proto_I2cMsg_msg_status_MSGTYPE i2c_proto_I2cStatus

extern const pb_msgdesc_t i2c_proto_I2cConfig_msg;
extern const pb_msgdesc_t i2c_proto_I2cMasterData_msg;
extern const pb_msgdesc_t i2c_proto_I2cSlaveData_msg;
extern const pb_msgdesc_t i2c_proto_I2cStatus_msg;
extern const pb_msgdesc_t i2c_proto_I2cMsg_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define i2c_proto_I2cConfig_fields &i2c_proto_I2cConfig_msg
#define i2c_proto_I2cMasterData_fields &i2c_proto_I2cMasterData_msg
#define i2c_proto_I2cSlaveData_fields &i2c_proto_I2cSlaveData_msg
#define i2c_proto_I2cStatus_fields &i2c_proto_I2cStatus_msg
#define i2c_proto_I2cMsg_fields &i2c_proto_I2cMsg_msg

/* Maximum encoded size of messages (where known) */
#define i2c_proto_I2cConfig_size                 6
#define i2c_proto_I2cMasterData_size             277
#define i2c_proto_I2cMsg_size                    288
#define i2c_proto_I2cSlaveData_size              275
#define i2c_proto_I2cStatus_size                 28

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
