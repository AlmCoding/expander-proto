/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.7 */

#ifndef PB_CTRL_PROTO_CTRL_PB_H_INCLUDED
#define PB_CTRL_PROTO_CTRL_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Struct definitions */
typedef struct _ctrl_proto_CtrlMsg {
    uint32_t sequence_number;
    bool system_reset;
} ctrl_proto_CtrlMsg;


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define ctrl_proto_CtrlMsg_init_default          {0, 0}
#define ctrl_proto_CtrlMsg_init_zero             {0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define ctrl_proto_CtrlMsg_sequence_number_tag   1
#define ctrl_proto_CtrlMsg_system_reset_tag      2

/* Struct field encoding specification for nanopb */
#define ctrl_proto_CtrlMsg_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   sequence_number,   1) \
X(a, STATIC,   SINGULAR, BOOL,     system_reset,      2)
#define ctrl_proto_CtrlMsg_CALLBACK NULL
#define ctrl_proto_CtrlMsg_DEFAULT NULL

extern const pb_msgdesc_t ctrl_proto_CtrlMsg_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define ctrl_proto_CtrlMsg_fields &ctrl_proto_CtrlMsg_msg

/* Maximum encoded size of messages (where known) */
#define ctrl_proto_CtrlMsg_size                  8

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
