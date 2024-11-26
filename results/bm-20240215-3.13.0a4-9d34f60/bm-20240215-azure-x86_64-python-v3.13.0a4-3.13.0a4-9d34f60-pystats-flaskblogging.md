
# Pystats results

- benchmark: flaskblogging
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 10,700,871 | 19.0% | 19.0% |  |
| LOAD_CONST | 3,308,100 | 5.9% | 24.9% |  |
| STORE_FAST | 2,623,580 | 4.7% | 29.6% |  |
| RESUME_CHECK | 2,578,206 | 4.6% | 34.2% |  |
| POP_JUMP_IF_FALSE | 2,053,466 | 3.7% | 37.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,808,460 | 3.2% | 41.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,807,600 | 3.2% | 44.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,696,773 | 3.0% | 47.3% | 0.2% |
| LOAD_GLOBAL_MODULE | 1,632,920 | 2.9% | 50.2% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,513,500 | 2.7% | 52.9% | 0.1% |
| RETURN_VALUE | 1,508,206 | 2.7% | 55.6% |  |
| POP_TOP | 1,358,446 | 2.4% | 58.0% |  |
| POP_JUMP_IF_TRUE | 1,261,140 | 2.2% | 60.2% |  |
| TO_BOOL_BOOL | 1,167,446 | 2.1% | 62.3% |  |
| CALL_PY_EXACT_ARGS | 1,047,960 | 1.9% | 64.2% | 0.3% |
| STORE_ATTR_INSTANCE_VALUE | 1,000,120 | 1.8% | 66.0% | 0.3% |
| CALL | 914,513 | 1.6% | 67.6% |  |
| RETURN_CONST | 899,600 | 1.6% | 69.2% |  |
| JUMP_BACKWARD | 825,720 | 1.5% | 70.7% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 771,100 | 1.4% | 72.0% | 0.7% |
| LOAD_ATTR | 752,098 | 1.3% | 73.4% |  |
| INTERPRETER_EXIT | 735,546 | 1.3% | 74.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 589,286 | 1.0% | 75.7% | 5.1% |
| STORE_FAST_STORE_FAST | 556,020 | 1.0% | 76.7% |  |
| CALL_ISINSTANCE | 426,680 | 0.8% | 77.5% |  |
| GET_ITER | 410,300 | 0.7% | 78.2% |  |
| FOR_ITER_LIST | 403,740 | 0.7% | 78.9% | 3.1% |
| COMPARE_OP_INT | 352,820 | 0.6% | 79.6% |  |
| BUILD_TUPLE | 338,260 | 0.6% | 80.2% |  |
| CONTAINS_OP | 336,060 | 0.6% | 80.8% |  |
| NOP | 331,253 | 0.6% | 81.4% |  |
| TO_BOOL_STR | 326,900 | 0.6% | 81.9% | 6.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 304,220 | 0.5% | 82.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 294,320 | 0.5% | 83.0% |  |
| PUSH_NULL | 292,820 | 0.5% | 83.5% |  |
| POP_JUMP_IF_NOT_NONE | 287,540 | 0.5% | 84.0% |  |
| TO_BOOL_NONE | 272,360 | 0.5% | 84.5% | 8.9% |
| FOR_ITER_TUPLE | 267,020 | 0.5% | 85.0% |  |
| SWAP | 264,480 | 0.5% | 85.5% |  |
| COPY | 258,720 | 0.5% | 85.9% |  |
| COMPARE_OP_STR | 250,560 | 0.4% | 86.4% | 1.0% |
| CALL_PY_WITH_DEFAULTS | 244,820 | 0.4% | 86.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 243,040 | 0.4% | 87.2% | 2.1% |
| FOR_ITER | 237,500 | 0.4% | 87.7% |  |
| JUMP_FORWARD | 217,740 | 0.4% | 88.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 204,780 | 0.4% | 88.4% | 3.8% |
| CALL_BUILTIN_FAST | 202,620 | 0.4% | 88.8% |  |
| TO_BOOL | 201,100 | 0.4% | 89.1% |  |
| STORE_ATTR | 196,640 | 0.3% | 89.5% |  |
| CALL_LEN | 194,180 | 0.3% | 89.8% |  |
| BUILD_LIST | 192,620 | 0.3% | 90.2% |  |
| FOR_ITER_GEN | 190,240 | 0.3% | 90.5% | 12.8% |
| LOAD_ATTR_MODULE | 185,100 | 0.3% | 90.8% | 0.0% |
| POP_JUMP_IF_NONE | 182,060 | 0.3% | 91.2% |  |
| YIELD_VALUE | 174,120 | 0.3% | 91.5% |  |
| CALL_KW | 171,800 | 0.3% | 91.8% |  |
| CALL_FUNCTION_EX | 171,760 | 0.3% | 92.1% |  |
| LOAD_DEREF | 164,280 | 0.3% | 92.4% |  |
| BUILD_MAP | 163,920 | 0.3% | 92.7% |  |
| BINARY_SLICE | 159,180 | 0.3% | 93.0% |  |
| UNPACK_SEQUENCE_TUPLE | 153,360 | 0.3% | 93.2% |  |
| CALL_BUILTIN_CLASS | 150,640 | 0.3% | 93.5% |  |
| COPY_FREE_VARS | 148,680 | 0.3% | 93.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 138,220 | 0.2% | 94.0% |  |
| BINARY_OP_ADD_INT | 127,840 | 0.2% | 94.2% |  |
| BINARY_OP | 127,820 | 0.2% | 94.5% |  |
| EXTENDED_ARG | 122,900 | 0.2% | 94.7% |  |
| COMPARE_OP | 117,840 | 0.2% | 94.9% |  |
| STORE_SUBSCR | 114,260 | 0.2% | 95.1% |  |
| IS_OP | 110,860 | 0.2% | 95.3% |  |
| CALL_LIST_APPEND | 110,060 | 0.2% | 95.5% |  |
| BINARY_OP_ADD_UNICODE | 105,160 | 0.2% | 95.7% |  |
| FOR_ITER_RANGE | 104,960 | 0.2% | 95.9% |  |
| BINARY_SUBSCR_DICT | 102,920 | 0.2% | 96.0% | 5.1% |
| BINARY_SUBSCR_GETITEM | 96,820 | 0.2% | 96.2% | 7.1% |
| RETURN_GENERATOR | 94,760 | 0.2% | 96.4% |  |
| STORE_SUBSCR_DICT | 94,600 | 0.2% | 96.5% |  |
| TO_BOOL_ALWAYS_TRUE | 93,740 | 0.2% | 96.7% | 6.8% |
| LOAD_ATTR_METHOD_LAZY_DICT | 87,180 | 0.2% | 96.9% | 8.3% |
| BEFORE_WITH | 82,120 | 0.1% | 97.0% |  |
| CALL_BUILTIN_O | 81,860 | 0.1% | 97.2% |  |
| POP_EXCEPT | 79,440 | 0.1% | 97.3% |  |
| PUSH_EXC_INFO | 79,440 | 0.1% | 97.4% |  |
| LOAD_ATTR_PROPERTY | 79,020 | 0.1% | 97.6% |  |
| LOAD_ATTR_SLOT | 77,000 | 0.1% | 97.7% |  |
| DICT_MERGE | 76,880 | 0.1% | 97.9% |  |
| CHECK_EXC_MATCH | 74,320 | 0.1% | 98.0% |  |
| BINARY_SUBSCR | 66,100 | 0.1% | 98.1% |  |
| MAKE_FUNCTION | 59,240 | 0.1% | 98.2% |  |
| LOAD_FAST_AND_CLEAR | 59,100 | 0.1% | 98.3% |  |
| TO_BOOL_INT | 58,780 | 0.1% | 98.4% |  |
| BINARY_SUBSCR_LIST_INT | 51,120 | 0.1% | 98.5% |  |
| LOAD_SUPER_ATTR_METHOD | 51,020 | 0.1% | 98.6% |  |
| TO_BOOL_LIST | 50,980 | 0.1% | 98.7% |  |
| END_FOR | 48,560 | 0.1% | 98.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 41,160 | 0.1% | 98.9% | 19.1% |
| STORE_ATTR_SLOT | 40,800 | 0.1% | 98.9% |  |
| EXIT_INIT_CHECK | 35,680 | 0.1% | 99.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 35,680 | 0.1% | 99.1% |  |
| UNPACK_SEQUENCE | 30,020 | 0.1% | 99.1% |  |
| RERAISE | 28,160 | 0.1% | 99.2% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 27,940 | 0.0% | 99.2% |  |
| FORMAT_SIMPLE | 25,600 | 0.0% | 99.3% |  |
| DELETE_ATTR | 23,040 | 0.0% | 99.3% |  |
| RAISE_VARARGS | 23,040 | 0.0% | 99.3% |  |
| LOAD_GLOBAL | 21,580 | 0.0% | 99.4% |  |
| LIST_APPEND | 20,960 | 0.0% | 99.4% |  |
| BUILD_CONST_KEY_MAP | 20,520 | 0.0% | 99.5% |  |
| BINARY_OP_SUBTRACT_INT | 17,820 | 0.0% | 99.5% |  |
| STORE_FAST_LOAD_FAST | 15,860 | 0.0% | 99.5% |  |
| LOAD_FAST_CHECK | 15,480 | 0.0% | 99.5% |  |
| BUILD_STRING | 15,360 | 0.0% | 99.6% |  |
| CALL_STR_1 | 15,360 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 12,900 | 0.0% | 99.6% | 97.7% |
| CALL_INTRINSIC_1 | 12,900 | 0.0% | 99.6% |  |
| LIST_EXTEND | 12,900 | 0.0% | 99.7% |  |
| MAKE_CELL | 12,840 | 0.0% | 99.7% |  |
| CONVERT_VALUE | 12,800 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_ATTR | 12,780 | 0.0% | 99.7% |  |
| STORE_SUBSCR_LIST_INT | 12,780 | 0.0% | 99.8% |  |
| UNPACK_SEQUENCE_LIST | 12,760 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 10,540 | 0.0% | 99.8% | 0.6% |
| BINARY_SUBSCR_STR_INT | 10,260 | 0.0% | 99.8% |  |
| CALL_TYPE_1 | 10,240 | 0.0% | 99.8% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 10,160 | 0.0% | 99.8% |  |
| IMPORT_FROM | 7,680 | 0.0% | 99.9% |  |
| MAP_ADD | 7,680 | 0.0% | 99.9% |  |
| RESUME | 6,440 | 0.0% | 99.9% |  |
| IMPORT_NAME | 5,180 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 5,160 | 0.0% | 99.9% |  |
| UNARY_NOT | 5,120 | 0.0% | 99.9% |  |
| WITH_EXCEPT_START | 5,120 | 0.0% | 99.9% |  |
| BUILD_SET | 5,120 | 0.0% | 99.9% |  |
| LOAD_ATTR_CLASS | 5,100 | 0.0% | 99.9% |  |
| SEND_GEN | 5,100 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 5,080 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 2,660 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 2,580 | 0.0% | 100.0% |  |
| END_SEND | 2,560 | 0.0% | 100.0% |  |
| GET_YIELD_FROM_ITER | 2,560 | 0.0% | 100.0% |  |
| BUILD_SLICE | 2,560 | 0.0% | 100.0% |  |
| SET_ADD | 2,560 | 0.0% | 100.0% |  |
| SET_UPDATE | 2,560 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% | 100.0% | 2.4% |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| STORE_NAME | 500 | 0.0% | 100.0% |  |
| LOAD_NAME | 100 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| SEND | 40 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,665,780 | 3.0% | 3.0% |
| STORE_FAST LOAD_FAST | 1,515,280 | 2.7% | 5.7% |
| RESUME_CHECK LOAD_FAST | 1,334,526 | 2.4% | 8.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,093,700 | 1.9% | 10.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 1,065,773 | 1.9% | 11.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 968,480 | 1.7% | 13.6% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 896,560 | 1.6% | 15.2% |
| LOAD_FAST LOAD_CONST | 879,700 | 1.6% | 16.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 804,626 | 1.4% | 18.2% |
| CACHE RESUME_CHECK | 637,926 | 1.1% | 19.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 578,240 | 1.0% | 20.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 562,200 | 1.0% | 21.4% |
| LOAD_FAST LOAD_ATTR | 553,818 | 1.0% | 22.3% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 516,740 | 0.9% | 23.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 512,740 | 0.9% | 24.2% |
| LOAD_CONST LOAD_FAST | 459,040 | 0.8% | 25.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 426,400 | 0.8% | 25.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 416,440 | 0.7% | 26.5% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 405,620 | 0.7% | 27.2% |
| RETURN_CONST POP_TOP | 402,280 | 0.7% | 27.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 401,820 | 0.7% | 28.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 401,653 | 0.7% | 29.4% |
| POP_TOP LOAD_FAST | 376,506 | 0.7% | 30.0% |
| RETURN_VALUE INTERPRETER_EXIT | 373,426 | 0.7% | 30.7% |
| LOAD_CONST LOAD_CONST | 369,680 | 0.7% | 31.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 363,560 | 0.6% | 32.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 355,180 | 0.6% | 32.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 351,500 | 0.6% | 33.3% |
| RETURN_VALUE STORE_FAST | 348,700 | 0.6% | 33.9% |
| LOAD_FAST RETURN_VALUE | 343,500 | 0.6% | 34.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 329,400 | 0.6% | 35.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 315,080 | 0.6% | 35.6% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 314,200 | 0.6% | 36.2% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 312,080 | 0.6% | 36.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 295,900 | 0.5% | 37.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 289,420 | 0.5% | 37.8% |
| RETURN_CONST INTERPRETER_EXIT | 287,480 | 0.5% | 38.3% |
| LOAD_FAST TO_BOOL_STR | 281,880 | 0.5% | 38.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 281,560 | 0.5% | 39.3% |
| LOAD_FAST TO_BOOL_BOOL | 275,180 | 0.5% | 39.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 268,820 | 0.5% | 40.3% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 259,040 | 0.5% | 40.7% |
| STORE_FAST_STORE_FAST LOAD_FAST | 258,760 | 0.5% | 41.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 258,100 | 0.5% | 41.7% |
| POP_TOP JUMP_BACKWARD | 256,120 | 0.5% | 42.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 247,780 | 0.4% | 42.6% |
| JUMP_BACKWARD FOR_ITER_LIST | 242,600 | 0.4% | 43.0% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 242,540 | 0.4% | 43.4% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 242,280 | 0.4% | 43.9% |
| LOAD_FAST LOAD_FAST | 240,780 | 0.4% | 44.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 237,460 | 0.4% | 44.7% |
| LOAD_CONST CALL | 237,080 | 0.4% | 45.1% |
| LOAD_CONST COMPARE_OP_INT | 236,980 | 0.4% | 45.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 232,120 | 0.4% | 46.0% |
| LOAD_FAST CALL | 232,013 | 0.4% | 46.4% |
| STORE_FAST LOAD_GLOBAL_MODULE | 219,000 | 0.4% | 46.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 218,060 | 0.4% | 47.2% |
| POP_TOP RETURN_CONST | 217,980 | 0.4% | 47.5% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 214,260 | 0.4% | 47.9% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 205,240 | 0.4% | 48.3% |
| FOR_ITER_TUPLE STORE_FAST | 204,800 | 0.4% | 48.7% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 202,940 | 0.4% | 49.0% |
| PUSH_NULL LOAD_FAST | 200,100 | 0.4% | 49.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 200,040 | 0.4% | 49.7% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 197,260 | 0.4% | 50.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 196,120 | 0.3% | 50.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 194,880 | 0.3% | 50.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 194,840 | 0.3% | 51.1% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 181,040 | 0.3% | 51.4% |
| NOP LOAD_FAST | 176,933 | 0.3% | 51.8% |
| CALL STORE_FAST | 173,320 | 0.3% | 52.1% |
| LOAD_CONST CALL_KW | 171,800 | 0.3% | 52.4% |
| RESUME_CHECK POP_TOP | 171,320 | 0.3% | 52.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 171,260 | 0.3% | 53.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 165,440 | 0.3% | 53.3% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 165,380 | 0.3% | 53.6% |
| POP_JUMP_IF_FALSE LOAD_CONST | 164,100 | 0.3% | 53.9% |
| RETURN_VALUE RETURN_VALUE | 161,360 | 0.3% | 54.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 160,500 | 0.3% | 54.4% |
| STORE_FAST_STORE_FAST STORE_FAST | 158,800 | 0.3% | 54.7% |
| LOAD_CONST STORE_FAST | 151,500 | 0.3% | 55.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 150,360 | 0.3% | 55.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS LOAD_FAST | 148,300 | 0.3% | 55.5% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 147,980 | 0.3% | 55.8% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 147,800 | 0.3% | 56.0% |
| LOAD_FAST POP_JUMP_IF_NONE | 146,080 | 0.3% | 56.3% |
| LOAD_FAST COPY | 145,920 | 0.3% | 56.6% |
| COPY_FREE_VARS RESUME_CHECK | 145,760 | 0.3% | 56.8% |
| LOAD_FAST TO_BOOL_NONE | 141,280 | 0.3% | 57.1% |
| CALL RETURN_VALUE | 138,773 | 0.2% | 57.3% |
| LOAD_FAST CONTAINS_OP | 138,640 | 0.2% | 57.6% |
| RETURN_VALUE LOAD_FAST | 138,220 | 0.2% | 57.8% |
| LOAD_ATTR LOAD_FAST | 136,640 | 0.2% | 58.1% |
| RESUME_CHECK NOP | 135,540 | 0.2% | 58.3% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 132,900 | 0.2% | 58.5% |
| JUMP_FORWARD LOAD_FAST | 130,580 | 0.2% | 58.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 130,200 | 0.2% | 59.0% |
| JUMP_BACKWARD FOR_ITER_GEN | 127,560 | 0.2% | 59.2% |
| LOAD_FAST TO_BOOL | 125,520 | 0.2% | 59.4% |
| GET_ITER FOR_ITER_LIST | 124,720 | 0.2% | 59.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,780 | 53.3% |
| BINARY_OP_ADD_INT | 61,420 | 38.6% |
| LOAD_FAST | 12,960 | 8.1% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 71,720 | 45.1% |
| GET_ITER | 41,040 | 25.8% |
| CALL_METHOD_DESCRIPTOR_O | 22,960 | 14.4% |
| LOAD_ATTR_METHOD_NO_DICT | 10,120 | 6.4% |
| LOAD_CONST | 5,160 | 3.2% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 637,926 | 86.2% |
| POP_TOP | 41,320 | 5.6% |
| COPY_FREE_VARS | 38,460 | 5.2% |
| RETURN_GENERATOR | 20,480 | 2.8% |
| RESUME | 1,800 | 0.2% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 71,600 | 87.2% |
| RETURN_VALUE | 10,260 | 12.5% |
| LOAD_ATTR | 120 | 0.1% |
| CALL | 100 | 0.1% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 79,540 | 96.9% |
| STORE_FAST | 2,580 | 3.1% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,040 | 49.6% |
| BUILD_STRING | 2,520 | 24.8% |
| LOAD_FAST_LOAD_FAST | 2,520 | 24.8% |
| BINARY_OP | 80 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,620 | 75.0% |
| LOAD_FAST_LOAD_FAST | 2,540 | 25.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 46,080 | 69.7% |
| LOAD_CONST | 13,680 | 20.7% |
| BINARY_SUBSCR | 3,400 | 5.1% |
| BUILD_TUPLE | 2,560 | 3.9% |
| LOAD_FAST | 260 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,660 | 73.6% |
| CALL_LEN | 5,080 | 7.7% |
| BINARY_SUBSCR | 3,400 | 5.1% |
| PUSH_EXC_INFO | 2,600 | 3.9% |
| LOAD_FAST | 2,560 | 3.9% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 63,980 | 86.1% |
| BUILD_TUPLE | 7,680 | 10.3% |
| LOAD_ATTR_MODULE | 2,540 | 3.4% |
| LOAD_GLOBAL | 100 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 74,320 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 2,560 | 99.2% |
| LOAD_FAST | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 99.2% |
| LOAD_GLOBAL_MODULE | 20 | 0.8% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 48,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 48,560 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,560 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 35,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 35,680 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 12,800 | 50.0% |
| LOAD_FAST | 10,240 | 40.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 9.9% |
| LOAD_GLOBAL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 15,360 | 60.0% |
| LOAD_CONST | 10,240 | 40.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 123,260 | 30.0% |
| CALL_BUILTIN_CLASS | 63,880 | 15.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 57,660 | 14.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,100 | 12.5% |
| BINARY_SLICE | 41,040 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 124,720 | 30.4% |
| FOR_ITER | 84,800 | 20.7% |
| LOAD_FAST_AND_CLEAR | 48,860 | 11.9% |
| FOR_ITER_TUPLE | 46,100 | 11.2% |
| FOR_ITER_GEN | 41,800 | 10.2% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 373,426 | 50.8% |
| RETURN_CONST | 287,480 | 39.1% |
| YIELD_VALUE | 54,160 | 7.4% |
| RETURN_GENERATOR | 20,480 | 2.8% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,640 | 82.1% |
| SET_FUNCTION_ATTRIBUTE | 2,660 | 4.5% |
| LOAD_CONST | 2,620 | 4.4% |
| STORE_FAST | 2,560 | 4.3% |
| LOAD_GLOBAL_MODULE | 2,520 | 4.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 135,540 | 40.9% |
| STORE_FAST | 41,180 | 12.4% |
| POP_JUMP_IF_FALSE | 38,513 | 11.6% |
| POP_JUMP_IF_TRUE | 33,280 | 10.0% |
| POP_TOP | 23,260 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 176,933 | 53.4% |
| LOAD_FAST_LOAD_FAST | 46,120 | 13.9% |
| LOAD_GLOBAL_MODULE | 43,580 | 13.2% |
| LOAD_GLOBAL_BUILTIN | 38,000 | 11.5% |
| NOP | 12,820 | 3.9% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 28,180 | 35.5% |
| SWAP | 23,060 | 29.0% |
| COPY | 23,040 | 29.0% |
| STORE_FAST | 2,600 | 3.3% |
| POP_JUMP_IF_FALSE | 2,560 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 28,160 | 35.4% |
| RETURN_VALUE | 23,060 | 29.0% |
| RERAISE | 23,040 | 29.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,600 | 3.3% |
| LOAD_FAST | 2,580 | 3.2% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 402,280 | 29.6% |
| RESUME_CHECK | 171,320 | 12.6% |
| CALL | 114,060 | 8.4% |
| POP_JUMP_IF_FALSE | 87,120 | 6.4% |
| BEFORE_WITH | 79,540 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 376,506 | 27.7% |
| JUMP_BACKWARD | 256,120 | 18.9% |
| RETURN_CONST | 217,980 | 16.0% |
| LOAD_CONST | 115,300 | 8.5% |
| RESUME_CHECK | 91,880 | 6.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 27,560 | 34.7% |
| RERAISE | 21,780 | 27.4% |
| CALL_BUILTIN_FAST | 7,660 | 9.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,120 | 6.4% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 5,080 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 71,500 | 90.0% |
| WITH_EXCEPT_START | 5,120 | 6.4% |
| LOAD_GLOBAL_MODULE | 2,520 | 3.2% |
| LOAD_GLOBAL | 300 | 0.4% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 113,240 | 38.7% |
| LOAD_ATTR_MODULE | 79,280 | 27.1% |
| LOAD_FAST | 77,000 | 26.3% |
| LOAD_SUPER_ATTR_ATTR | 12,780 | 4.4% |
| BINARY_SUBSCR_DICT | 5,120 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200,100 | 68.3% |
| CALL | 36,200 | 12.4% |
| LOAD_FAST_LOAD_FAST | 18,060 | 6.2% |
| LOAD_CONST | 18,020 | 6.2% |
| LOAD_GLOBAL_MODULE | 15,240 | 5.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 58,720 | 62.0% |
| CACHE | 20,480 | 21.6% |
| CALL_FUNCTION_EX | 7,680 | 8.1% |
| COPY_FREE_VARS | 2,600 | 2.7% |
| CALL_KW | 2,560 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 28,160 | 29.7% |
| INTERPRETER_EXIT | 20,480 | 21.6% |
| CALL_BUILTIN_O | 12,760 | 13.5% |
| STORE_FAST | 10,240 | 10.8% |
| LOAD_FAST | 7,680 | 8.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 343,500 | 22.8% |
| RETURN_VALUE | 161,360 | 10.7% |
| CALL | 138,773 | 9.2% |
| CALL_FUNCTION_EX | 84,520 | 5.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 84,400 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 373,426 | 24.8% |
| STORE_FAST | 348,700 | 23.1% |
| RETURN_VALUE | 161,360 | 10.7% |
| LOAD_FAST | 138,220 | 9.2% |
| BUILD_TUPLE | 51,180 | 3.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 51,200 | 44.8% |
| LOAD_FAST | 30,800 | 27.0% |
| LOAD_FAST_LOAD_FAST | 20,560 | 18.0% |
| RETURN_VALUE | 10,240 | 9.0% |
| STORE_SUBSCR | 1,100 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 51,260 | 44.9% |
| RETURN_CONST | 51,200 | 44.8% |
| LOAD_FAST | 5,200 | 4.6% |
| LOAD_CONST | 2,640 | 2.3% |
| LOAD_GLOBAL_BUILTIN | 2,520 | 2.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,520 | 62.4% |
| LOAD_ATTR_INSTANCE_VALUE | 33,700 | 16.8% |
| COPY | 16,480 | 8.2% |
| LOAD_ATTR | 6,740 | 3.4% |
| LOAD_FAST_CHECK | 5,160 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 109,100 | 54.3% |
| POP_JUMP_IF_TRUE | 81,560 | 40.6% |
| TO_BOOL | 3,700 | 1.8% |
| TO_BOOL_BOOL | 3,620 | 1.8% |
| TO_BOOL_NONE | 1,240 | 0.6% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,080 | 99.2% |
| TO_BOOL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,560 | 50.0% |
| STORE_FAST | 2,560 | 50.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 5,040 | 98.4% |
| TO_BOOL | 80 | 1.6% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 61,560 | 48.2% |
| BUILD_TUPLE | 35,880 | 28.1% |
| LOAD_FAST | 15,700 | 12.3% |
| LOAD_CONST | 13,460 | 10.5% |
| BINARY_OP | 840 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 74,460 | 58.3% |
| RETURN_VALUE | 35,900 | 28.1% |
| LOAD_FAST | 12,920 | 10.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,520 | 2.0% |
| BINARY_OP | 840 | 0.7% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,800 | 62.4% |
| RETURN_VALUE | 2,580 | 12.6% |
| STORE_FAST | 2,580 | 12.6% |
| CALL | 2,560 | 12.5% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,620 | 20.0% |
| RESUME_CHECK | 25,480 | 13.2% |
| LOAD_FAST | 23,140 | 12.0% |
| LOAD_CONST | 23,060 | 12.0% |
| STORE_ATTR_INSTANCE_VALUE | 20,420 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 76,940 | 39.9% |
| SWAP | 38,620 | 20.0% |
| LOAD_FAST | 35,920 | 18.6% |
| CALL_PY_EXACT_ARGS | 12,680 | 6.6% |
| MAP_ADD | 7,680 | 4.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,760 | 18.8% |
| POP_TOP | 30,720 | 18.7% |
| STORE_ATTR_INSTANCE_VALUE | 30,600 | 18.7% |
| BUILD_TUPLE | 28,160 | 17.2% |
| POP_JUMP_IF_NOT_NONE | 10,240 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,820 | 71.9% |
| STORE_FAST | 23,040 | 14.1% |
| SWAP | 7,680 | 4.7% |
| JUMP_FORWARD | 5,120 | 3.1% |
| CALL_PY_WITH_DEFAULTS | 5,040 | 3.1% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,560 | 50.0% |
| CALL_BUILTIN_CLASS | 2,540 | 49.6% |
| CALL | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 50.0% |
| SWAP | 2,560 | 50.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 2,560 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 15,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 5,120 | 33.3% |
| RETURN_VALUE | 2,560 | 16.7% |
| CALL | 2,560 | 16.7% |
| STORE_FAST | 2,560 | 16.7% |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,520 | 16.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 107,640 | 31.8% |
| LOAD_FAST | 66,640 | 19.7% |
| RETURN_VALUE | 51,180 | 15.1% |
| LOAD_GLOBAL_BUILTIN | 40,800 | 12.1% |
| LOAD_GLOBAL_MODULE | 38,420 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 56,480 | 16.7% |
| LOAD_FAST | 56,320 | 16.6% |
| CALL | 41,420 | 12.2% |
| YIELD_VALUE | 40,960 | 12.1% |
| BINARY_OP | 35,880 | 10.6% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 237,080 | 25.9% |
| LOAD_FAST | 232,013 | 25.4% |
| LOAD_FAST_LOAD_FAST | 80,660 | 8.8% |
| LOAD_GLOBAL_MODULE | 77,420 | 8.5% |
| LOAD_ATTR_METHOD_NO_DICT | 70,660 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 173,320 | 19.0% |
| RETURN_VALUE | 138,773 | 15.2% |
| TO_BOOL_BOOL | 122,320 | 13.4% |
| POP_TOP | 114,060 | 12.5% |
| RESUME_CHECK | 81,460 | 8.9% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 76,880 | 44.8% |
| LOAD_FAST | 71,760 | 41.8% |
| CALL_INTRINSIC_1 | 12,880 | 7.5% |
| RETURN_VALUE | 10,240 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 84,520 | 49.2% |
| POP_TOP | 40,960 | 23.8% |
| RESUME_CHECK | 17,920 | 10.4% |
| STORE_FAST | 12,820 | 7.5% |
| RETURN_GENERATOR | 7,680 | 4.5% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 12,900 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 12,880 | 99.8% |
| BUILD_MAP | 20 | 0.2% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 171,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 97,020 | 56.5% |
| RETURN_VALUE | 28,180 | 16.4% |
| STORE_FAST | 17,960 | 10.5% |
| LOAD_FAST | 12,800 | 7.5% |
| POP_TOP | 5,120 | 3.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,340 | 60.5% |
| LOAD_FAST | 23,280 | 19.8% |
| LOAD_GLOBAL_MODULE | 10,360 | 8.8% |
| LOAD_FAST_LOAD_FAST | 5,240 | 4.4% |
| BUILD_LIST | 2,600 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 97,580 | 82.8% |
| POP_JUMP_IF_FALSE | 16,720 | 14.2% |
| COMPARE_OP | 1,720 | 1.5% |
| COMPARE_OP_INT | 1,160 | 1.0% |
| COMPARE_OP_STR | 520 | 0.4% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,640 | 41.3% |
| LOAD_FAST_LOAD_FAST | 99,880 | 29.7% |
| LOAD_GLOBAL_MODULE | 43,580 | 13.0% |
| LOAD_CONST | 33,280 | 9.9% |
| LOAD_ATTR_MODULE | 10,260 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 194,840 | 58.0% |
| POP_JUMP_IF_TRUE | 102,800 | 30.6% |
| STORE_FAST | 15,380 | 4.6% |
| EXTENDED_ARG | 10,240 | 3.0% |
| COPY | 5,120 | 1.5% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 80.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,540 | 19.8% |
| LOAD_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 12,800 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 145,920 | 56.4% |
| RAISE_VARARGS | 17,920 | 6.9% |
| CALL_ISINSTANCE | 12,780 | 4.9% |
| LOAD_CONST | 10,280 | 4.0% |
| RETURN_VALUE | 10,240 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 58,300 | 22.5% |
| LOAD_ATTR_INSTANCE_VALUE | 43,320 | 16.7% |
| TO_BOOL_STR | 30,560 | 11.8% |
| TO_BOOL_BOOL | 30,480 | 11.8% |
| POP_EXCEPT | 23,040 | 8.9% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 86,900 | 58.4% |
| CACHE | 38,460 | 25.9% |
| CALL | 20,680 | 13.9% |
| CALL_KW | 2,560 | 1.7% |
| CALL_FUNCTION_EX | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 145,760 | 98.0% |
| RETURN_GENERATOR | 2,600 | 1.7% |
| RESUME | 320 | 0.2% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,360 | 66.7% |
| NOP | 7,680 | 33.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,740 | 93.3% |
| BUILD_MAP | 2,560 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,540 | 3.3% |
| CALL | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 76,880 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 30,680 | 25.0% |
| POP_JUMP_IF_TRUE | 28,160 | 22.9% |
| TO_BOOL_STR | 10,540 | 8.6% |
| CONTAINS_OP | 10,240 | 8.3% |
| JUMP_BACKWARD | 10,240 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 61,440 | 50.0% |
| JUMP_FORWARD | 30,720 | 25.0% |
| FOR_ITER | 12,880 | 10.5% |
| JUMP_BACKWARD | 10,240 | 8.3% |
| FOR_ITER_LIST | 5,040 | 4.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,100 | 47.2% |
| GET_ITER | 84,800 | 35.7% |
| LOAD_FAST | 18,080 | 7.6% |
| EXTENDED_ARG | 12,880 | 5.4% |
| SWAP | 5,500 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 80,020 | 33.7% |
| RETURN_CONST | 53,880 | 22.7% |
| STORE_FAST | 47,360 | 19.9% |
| LOAD_FAST | 31,040 | 13.1% |
| LOAD_CONST | 12,860 | 5.4% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 5,120 | 66.7% |
| STORE_FAST | 2,560 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,680 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 5,120 | 98.8% |
| STORE_NAME | 40 | 0.8% |
| STORE_FAST | 20 | 0.4% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,640 | 43.9% |
| LOAD_GLOBAL_MODULE | 36,440 | 32.9% |
| LOAD_FAST_LOAD_FAST | 20,480 | 18.5% |
| LOAD_FAST | 5,140 | 4.6% |
| LOAD_GLOBAL | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 75,000 | 67.7% |
| RETURN_VALUE | 15,360 | 13.9% |
| COPY | 10,240 | 9.2% |
| POP_JUMP_IF_TRUE | 7,700 | 6.9% |
| STORE_FAST | 2,560 | 2.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 259,040 | 31.4% |
| POP_TOP | 256,120 | 31.0% |
| STORE_SUBSCR_DICT | 74,180 | 9.0% |
| STORE_FAST | 61,680 | 7.5% |
| STORE_SUBSCR | 51,260 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 242,600 | 29.4% |
| FOR_ITER_TUPLE | 205,240 | 24.9% |
| FOR_ITER_GEN | 127,560 | 15.4% |
| FOR_ITER | 112,100 | 13.6% |
| FOR_ITER_RANGE | 89,540 | 10.8% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 2,600 | 50.4% |
| RESUME_CHECK | 2,540 | 49.2% |
| RESUME | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 49.6% |
| SEND_GEN | 2,540 | 49.2% |
| LOAD_FAST | 40 | 0.8% |
| SEND | 20 | 0.4% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 41,020 | 18.8% |
| POP_JUMP_IF_FALSE | 38,400 | 17.6% |
| EXTENDED_ARG | 30,720 | 14.1% |
| LOAD_CONST | 20,480 | 9.4% |
| STORE_SUBSCR_LIST_INT | 12,780 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,580 | 60.0% |
| STORE_FAST | 40,960 | 18.8% |
| LOAD_GLOBAL_MODULE | 27,920 | 12.8% |
| LOAD_CONST | 7,680 | 3.5% |
| BUILD_MAP | 5,120 | 2.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,240 | 48.9% |
| BUILD_TUPLE | 10,240 | 48.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 480 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20,960 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,820 | 99.4% |
| LOAD_DEREF | 80 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 12,900 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 553,818 | 73.6% |
| LOAD_ATTR_INSTANCE_VALUE | 75,600 | 10.1% |
| LOAD_ATTR | 49,760 | 6.6% |
| LOAD_GLOBAL_MODULE | 29,400 | 3.9% |
| RETURN_VALUE | 13,000 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 136,640 | 18.2% |
| PUSH_NULL | 113,240 | 15.1% |
| LOAD_CONST | 53,740 | 7.1% |
| LOAD_ATTR | 49,760 | 6.6% |
| STORE_FAST | 49,180 | 6.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 879,700 | 26.6% |
| LOAD_ATTR_METHOD_NO_DICT | 426,400 | 12.9% |
| LOAD_CONST | 369,680 | 11.2% |
| STORE_ATTR_INSTANCE_VALUE | 165,440 | 5.0% |
| POP_JUMP_IF_FALSE | 164,100 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 459,040 | 13.9% |
| LOAD_CONST | 369,680 | 11.2% |
| CALL | 237,080 | 7.2% |
| COMPARE_OP_INT | 236,980 | 7.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 181,040 | 5.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 68,880 | 41.9% |
| LOAD_ATTR_METHOD_NO_DICT | 58,880 | 35.8% |
| LOAD_GLOBAL_MODULE | 15,320 | 9.3% |
| STORE_FAST | 5,160 | 3.1% |
| NOP | 2,640 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,080 | 39.0% |
| LOAD_CONST | 61,480 | 37.4% |
| LOAD_ATTR_INSTANCE_VALUE | 12,600 | 7.7% |
| LOAD_FAST_LOAD_FAST | 7,680 | 4.7% |
| BINARY_SUBSCR_DICT | 5,120 | 3.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,515,280 | 14.2% |
| RESUME_CHECK | 1,334,526 | 12.5% |
| POP_JUMP_IF_FALSE | 1,065,773 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 968,480 | 9.1% |
| POP_JUMP_IF_TRUE | 512,740 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,665,780 | 15.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,093,700 | 10.2% |
| LOAD_CONST | 879,700 | 8.2% |
| STORE_ATTR_INSTANCE_VALUE | 578,240 | 5.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 562,200 | 5.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 48,860 | 82.7% |
| LOAD_FAST_AND_CLEAR | 10,240 | 17.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 48,860 | 82.7% |
| LOAD_FAST_AND_CLEAR | 10,240 | 17.3% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,760 | 50.1% |
| LOAD_GLOBAL_BUILTIN | 5,080 | 32.8% |
| LOAD_FAST_LOAD_FAST | 2,560 | 16.5% |
| LOAD_GLOBAL | 40 | 0.3% |
| JUMP_FORWARD | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 5,160 | 33.3% |
| BUILD_TUPLE | 2,560 | 16.5% |
| LOAD_ATTR | 2,560 | 16.5% |
| CALL_BUILTIN_CLASS | 2,520 | 16.3% |
| TO_BOOL_BOOL | 2,520 | 16.3% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 315,080 | 17.4% |
| LOAD_GLOBAL_MODULE | 289,420 | 16.0% |
| STORE_ATTR_INSTANCE_VALUE | 247,780 | 13.7% |
| LOAD_FAST_LOAD_FAST | 197,260 | 10.9% |
| RESUME_CHECK | 122,660 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 363,560 | 20.1% |
| LOAD_FAST_LOAD_FAST | 197,260 | 10.9% |
| LOAD_FAST | 194,880 | 10.8% |
| CALL_PY_EXACT_ARGS | 114,380 | 6.3% |
| BUILD_TUPLE | 107,640 | 6.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980 | 13.8% |
| STORE_FAST | 2,880 | 13.3% |
| POP_JUMP_IF_FALSE | 2,420 | 11.2% |
| RESUME_CHECK | 2,000 | 9.3% |
| RESUME | 1,920 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,740 | 31.2% |
| LOAD_FAST | 4,380 | 20.3% |
| LOAD_GLOBAL_BUILTIN | 4,200 | 19.5% |
| LOAD_ATTR | 1,580 | 7.3% |
| CALL | 1,460 | 6.8% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 60 | 60.0% |
| LOAD_CONST | 20 | 20.0% |
| STORE_NAME | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 60 | 60.0% |
| CALL | 20 | 20.0% |
| LOAD_CONST | 20 | 20.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 260 | 50.0% |
| CALL | 140 | 26.9% |
| LOAD_FAST | 40 | 7.7% |
| LOAD_FAST_LOAD_FAST | 40 | 7.7% |
| PUSH_NULL | 20 | 3.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 5,120 | 39.9% |
| CALL_PY_EXACT_ARGS | 2,580 | 20.1% |
| CALL_KW | 2,560 | 19.9% |
| CALL_PY_WITH_DEFAULTS | 2,540 | 19.8% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 5,120 | 39.9% |
| RESUME_CHECK | 5,120 | 39.9% |
| RETURN_GENERATOR | 2,560 | 19.9% |
| RESUME | 40 | 0.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 7,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,680 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 804,626 | 39.2% |
| COMPARE_OP_INT | 258,100 | 12.6% |
| CONTAINS_OP | 194,840 | 9.5% |
| TO_BOOL_NONE | 160,500 | 7.8% |
| TO_BOOL_STR | 113,080 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,065,773 | 51.9% |
| RETURN_CONST | 200,040 | 9.7% |
| LOAD_GLOBAL_MODULE | 165,380 | 8.1% |
| LOAD_CONST | 164,100 | 8.0% |
| LOAD_GLOBAL_BUILTIN | 130,200 | 6.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 146,080 | 80.2% |
| LOAD_ATTR_INSTANCE_VALUE | 17,860 | 9.8% |
| LOAD_ATTR | 12,940 | 7.1% |
| LOAD_DEREF | 2,560 | 1.4% |
| CALL_BUILTIN_FAST | 2,540 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,840 | 52.1% |
| LOAD_GLOBAL_BUILTIN | 20,260 | 11.1% |
| LOAD_CONST | 17,940 | 9.9% |
| LOAD_FAST_LOAD_FAST | 15,360 | 8.4% |
| JUMP_BACKWARD | 10,240 | 5.6% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 218,060 | 75.8% |
| LOAD_ATTR_INSTANCE_VALUE | 23,020 | 8.0% |
| LOAD_ATTR | 15,520 | 5.4% |
| LOAD_GLOBAL_MODULE | 15,400 | 5.4% |
| RETURN_VALUE | 7,640 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,020 | 39.3% |
| LOAD_GLOBAL_MODULE | 58,700 | 20.4% |
| LOAD_GLOBAL_BUILTIN | 43,280 | 15.1% |
| LOAD_FAST_LOAD_FAST | 25,600 | 8.9% |
| NOP | 12,860 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 355,180 | 28.2% |
| TO_BOOL_STR | 202,940 | 16.1% |
| COMPARE_OP_STR | 120,220 | 9.5% |
| TO_BOOL_NONE | 106,680 | 8.5% |
| CONTAINS_OP | 102,800 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 512,740 | 40.7% |
| JUMP_BACKWARD | 259,040 | 20.5% |
| LOAD_GLOBAL_BUILTIN | 86,820 | 6.9% |
| LOAD_CONST | 81,960 | 6.5% |
| POP_TOP | 76,820 | 6.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,920 | 77.8% |
| LOAD_GLOBAL_BUILTIN | 2,540 | 11.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 11.0% |
| LOAD_GLOBAL | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 17,920 | 87.5% |
| PUSH_EXC_INFO | 2,560 | 12.5% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 23,040 | 81.8% |
| POP_JUMP_IF_TRUE | 5,120 | 18.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 21,780 | 81.0% |
| COPY | 5,120 | 19.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 217,980 | 24.2% |
| POP_JUMP_IF_FALSE | 200,040 | 22.2% |
| STORE_ATTR_INSTANCE_VALUE | 147,980 | 16.4% |
| FOR_ITER | 53,880 | 6.0% |
| CALL_LIST_APPEND | 53,720 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 402,280 | 44.7% |
| INTERPRETER_EXIT | 287,480 | 32.0% |
| TO_BOOL_BOOL | 94,500 | 10.5% |
| END_FOR | 48,560 | 5.4% |
| EXIT_INIT_CHECK | 35,680 | 4.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 20 | 50.0% |
| LOAD_CONST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 20 | 50.0% |
| SEND_GEN | 20 | 50.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 2,540 | 99.2% |
| CALL | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,560 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,660 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,580 | 97.0% |
| STORE_NAME | 40 | 1.5% |
| LOAD_GLOBAL_MODULE | 40 | 1.5% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 2,560 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 118,700 | 60.4% |
| LOAD_FAST_LOAD_FAST | 59,380 | 30.2% |
| SWAP | 7,960 | 4.0% |
| STORE_ATTR | 7,900 | 4.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,720 | 27.8% |
| LOAD_CONST | 42,020 | 21.4% |
| RETURN_CONST | 28,780 | 14.6% |
| LOAD_FAST_LOAD_FAST | 26,440 | 13.4% |
| LOAD_GLOBAL_MODULE | 22,680 | 11.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 348,700 | 13.3% |
| FOR_ITER_TUPLE | 204,800 | 7.8% |
| CALL | 173,320 | 6.6% |
| STORE_FAST_STORE_FAST | 158,800 | 6.1% |
| LOAD_CONST | 151,500 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,515,280 | 57.8% |
| LOAD_FAST_LOAD_FAST | 315,080 | 12.0% |
| LOAD_GLOBAL_BUILTIN | 232,120 | 8.8% |
| LOAD_GLOBAL_MODULE | 219,000 | 8.3% |
| LOAD_CONST | 77,140 | 2.9% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 10,200 | 64.3% |
| FOR_ITER | 5,160 | 32.5% |
| FOR_ITER_TUPLE | 480 | 3.0% |
| COPY | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 7,680 | 48.4% |
| LOAD_ATTR_METHOD_NO_DICT | 7,620 | 48.0% |
| TO_BOOL_STR | 480 | 3.0% |
| LOAD_ATTR | 80 | 0.5% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 281,560 | 50.6% |
| UNPACK_SEQUENCE_TUPLE | 132,900 | 23.9% |
| STORE_FAST_STORE_FAST | 64,000 | 11.5% |
| UNPACK_SEQUENCE | 28,880 | 5.2% |
| POP_TOP | 20,480 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 258,760 | 46.5% |
| STORE_FAST | 158,800 | 28.6% |
| STORE_FAST_STORE_FAST | 64,000 | 11.5% |
| LOAD_FAST_LOAD_FAST | 43,520 | 7.8% |
| LOAD_GLOBAL_BUILTIN | 12,760 | 2.3% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 180 | 36.0% |
| LOAD_CONST | 100 | 20.0% |
| CALL | 60 | 12.0% |
| LOAD_NAME | 60 | 12.0% |
| IMPORT_NAME | 40 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 72.0% |
| LOAD_BUILD_CLASS | 60 | 12.0% |
| RETURN_CONST | 60 | 12.0% |
| LOAD_NAME | 20 | 4.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,280 | 28.1% |
| LOAD_FAST_AND_CLEAR | 48,860 | 18.5% |
| BINARY_OP_ADD_INT | 43,400 | 16.4% |
| BUILD_LIST | 38,620 | 14.6% |
| FOR_ITER_LIST | 20,480 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 43,320 | 16.4% |
| BUILD_LIST | 38,620 | 14.6% |
| LOAD_CONST | 30,760 | 11.6% |
| FOR_ITER_LIST | 25,480 | 9.6% |
| POP_EXCEPT | 23,060 | 8.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,800 | 85.9% |
| RETURN_VALUE | 2,920 | 9.7% |
| FOR_ITER | 300 | 1.0% |
| UNPACK_SEQUENCE | 300 | 1.0% |
| CALL | 280 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 28,880 | 96.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 420 | 1.4% |
| UNPACK_SEQUENCE_TUPLE | 320 | 1.1% |
| UNPACK_SEQUENCE | 300 | 1.0% |
| UNPACK_SEQUENCE_LIST | 40 | 0.1% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,760 | 30.9% |
| BUILD_TUPLE | 40,960 | 23.5% |
| RETURN_VALUE | 30,720 | 17.6% |
| COMPARE_OP_STR | 12,780 | 7.3% |
| BINARY_SUBSCR_LIST_INT | 10,220 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 97,120 | 55.8% |
| INTERPRETER_EXIT | 54,160 | 31.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20,240 | 11.6% |
| YIELD_VALUE | 2,560 | 1.5% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,280 | 50.9% |
| CACHE | 1,800 | 28.0% |
| CALL_KW | 480 | 7.5% |
| POP_TOP | 320 | 5.0% |
| COPY_FREE_VARS | 320 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,180 | 49.4% |
| LOAD_GLOBAL | 1,920 | 29.8% |
| LOAD_CONST | 300 | 4.7% |
| LOAD_FAST_LOAD_FAST | 300 | 4.7% |
| POP_TOP | 240 | 3.7% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 2,520 | 99.2% |
| BINARY_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 114,920 | 89.9% |
| CALL_LEN | 7,600 | 5.9% |
| LOAD_FAST_LOAD_FAST | 5,080 | 4.0% |
| BINARY_OP | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 61,420 | 48.0% |
| SWAP | 43,400 | 33.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 15,280 | 12.0% |
| STORE_FAST | 5,100 | 4.0% |
| LOAD_CONST | 2,600 | 2.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,800 | 60.7% |
| CALL_METHOD_DESCRIPTOR_O | 10,200 | 9.7% |
| RETURN_VALUE | 10,160 | 9.7% |
| LOAD_CONST | 10,160 | 9.7% |
| BINARY_SLICE | 5,120 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,040 | 39.0% |
| RETURN_VALUE | 20,460 | 19.5% |
| STORE_FAST | 20,460 | 19.5% |
| STORE_SUBSCR_DICT | 12,760 | 12.1% |
| COPY | 5,120 | 4.9% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,040 | 99.2% |
| BINARY_OP | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 50.0% |
| BINARY_OP_ADD_FLOAT | 2,520 | 49.6% |
| BINARY_OP | 20 | 0.4% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,080 | 28.5% |
| LOAD_FAST_LOAD_FAST | 5,080 | 28.5% |
| CALL_LEN | 5,040 | 28.3% |
| LOAD_CONST | 2,520 | 14.1% |
| BINARY_OP | 100 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 12,720 | 71.4% |
| STORE_FAST | 5,100 | 28.6% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 28,160 | 27.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20,440 | 19.9% |
| LOAD_CONST | 20,200 | 19.6% |
| LOAD_FAST | 17,860 | 17.4% |
| LOAD_FAST_LOAD_FAST | 10,780 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 33,260 | 32.5% |
| PUSH_EXC_INFO | 27,560 | 26.9% |
| LOAD_ATTR_METHOD_NO_DICT | 12,600 | 12.3% |
| LOAD_FAST_LOAD_FAST | 10,780 | 10.5% |
| RETURN_VALUE | 10,220 | 10.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 50,620 | 52.3% |
| LOAD_FAST | 40,920 | 42.3% |
| LOAD_CONST | 5,120 | 5.3% |
| BINARY_SUBSCR_DICT | 100 | 0.1% |
| BINARY_SUBSCR_GETITEM | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 89,980 | 92.9% |
| LOAD_FAST_LOAD_FAST | 4,640 | 4.8% |
| PUSH_EXC_INFO | 1,880 | 1.9% |
| RETURN_VALUE | 200 | 0.2% |
| BINARY_SUBSCR_DICT | 80 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 38,240 | 74.8% |
| LOAD_FAST_LOAD_FAST | 12,760 | 25.0% |
| BINARY_SUBSCR | 120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 12,780 | 25.0% |
| LOAD_ATTR_METHOD_NO_DICT | 12,720 | 24.9% |
| YIELD_VALUE | 10,220 | 20.0% |
| RETURN_VALUE | 7,660 | 15.0% |
| TO_BOOL_STR | 7,640 | 14.9% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,200 | 99.4% |
| BINARY_SUBSCR | 60 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,220 | 99.6% |
| LOAD_ATTR | 40 | 0.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 117,640 | 85.1% |
| LOAD_FAST | 20,440 | 14.8% |
| BINARY_SUBSCR | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,620 | 35.2% |
| STORE_FAST | 40,980 | 29.6% |
| LOAD_GLOBAL_BUILTIN | 35,840 | 25.9% |
| LOAD_ATTR_METHOD_NO_DICT | 10,200 | 7.4% |
| JUMP_FORWARD | 2,540 | 1.8% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,160 | 28.5% |
| LOAD_GLOBAL_MODULE | 10,080 | 28.3% |
| LOAD_ATTR_INSTANCE_VALUE | 7,560 | 21.2% |
| LOAD_ATTR | 5,080 | 14.2% |
| PUSH_NULL | 2,520 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 35,680 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 38,280 | 93.0% |
| LOAD_FAST | 2,640 | 6.4% |
| CALL | 120 | 0.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 33,300 | 80.9% |
| POP_TOP | 7,720 | 18.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.3% |
| CALL_PY_EXACT_ARGS | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,120 | 40.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 25,440 | 16.9% |
| LOAD_ATTR_INSTANCE_VALUE | 20,360 | 13.5% |
| CALL_LEN | 12,720 | 8.4% |
| CALL | 8,180 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,880 | 42.4% |
| STORE_FAST | 38,280 | 25.4% |
| RETURN_VALUE | 20,440 | 13.6% |
| LOAD_FAST | 15,320 | 10.2% |
| COPY | 7,640 | 5.1% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 104,340 | 51.5% |
| LOAD_FAST_LOAD_FAST | 72,280 | 35.7% |
| LOAD_ATTR_INSTANCE_VALUE | 20,360 | 10.0% |
| BUILD_MAP | 2,520 | 1.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,520 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 83,940 | 41.4% |
| RETURN_VALUE | 82,520 | 40.7% |
| STORE_FAST | 12,780 | 6.3% |
| PUSH_EXC_INFO | 7,660 | 3.8% |
| LOAD_FAST | 5,080 | 2.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,400 | 98.7% |
| LOAD_CONST | 60 | 0.6% |
| RETURN_GENERATOR | 40 | 0.4% |
| CALL | 20 | 0.2% |
| CALL_STR_1 | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,260 | 49.9% |
| PUSH_EXC_INFO | 5,120 | 48.6% |
| RETURN_VALUE | 140 | 1.3% |
| BEFORE_WITH | 20 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,940 | 78.1% |
| RETURN_GENERATOR | 12,760 | 15.6% |
| BUILD_TUPLE | 2,560 | 3.1% |
| BUILD_LIST | 2,520 | 3.1% |
| CALL | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 63,960 | 78.1% |
| TO_BOOL_BOOL | 15,280 | 18.7% |
| RETURN_VALUE | 2,560 | 3.1% |
| TO_BOOL | 40 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 242,540 | 56.8% |
| LOAD_GLOBAL_MODULE | 122,220 | 28.6% |
| BUILD_TUPLE | 33,020 | 7.7% |
| LOAD_ATTR_MODULE | 22,800 | 5.3% |
| LOAD_ATTR | 5,040 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 351,500 | 82.4% |
| STORE_FAST | 35,860 | 8.4% |
| LOAD_FAST | 20,460 | 4.8% |
| COPY | 12,780 | 3.0% |
| RETURN_VALUE | 5,100 | 1.2% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 109,440 | 56.4% |
| LOAD_ATTR_INSTANCE_VALUE | 66,500 | 34.2% |
| LOAD_ATTR | 10,080 | 5.2% |
| BINARY_SUBSCR | 5,080 | 2.6% |
| LOAD_ATTR_SLOT | 2,520 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,500 | 34.2% |
| LOAD_CONST | 35,840 | 18.5% |
| LOAD_GLOBAL_MODULE | 28,040 | 14.4% |
| CALL_BUILTIN_CLASS | 12,720 | 6.6% |
| LOAD_FAST | 10,160 | 5.2% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,040 | 88.2% |
| BUILD_TUPLE | 12,720 | 11.6% |
| CALL | 260 | 0.2% |
| LOAD_CONST | 20 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 53,720 | 48.8% |
| JUMP_BACKWARD | 35,780 | 32.5% |
| LOAD_GLOBAL_BUILTIN | 12,760 | 11.6% |
| LOAD_FAST | 5,140 | 4.7% |
| LOAD_FAST_LOAD_FAST | 2,540 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 101,560 | 41.8% |
| LOAD_ATTR_METHOD_NO_DICT | 63,660 | 26.2% |
| LOAD_FAST | 30,500 | 12.5% |
| BINARY_OP_ADD_INT | 15,280 | 6.3% |
| LOAD_FAST_LOAD_FAST | 10,200 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 61,280 | 25.2% |
| POP_TOP | 58,680 | 24.1% |
| RETURN_VALUE | 38,320 | 15.8% |
| LOAD_FAST | 28,100 | 11.6% |
| BUILD_TUPLE | 20,440 | 8.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 181,040 | 59.5% |
| LOAD_ATTR_METHOD_NO_DICT | 114,920 | 37.8% |
| LOAD_FAST | 5,040 | 1.7% |
| LOAD_FAST_LOAD_FAST | 2,520 | 0.8% |
| CALL | 700 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 84,400 | 27.7% |
| LOAD_FAST | 61,420 | 20.2% |
| STORE_FAST | 58,840 | 19.3% |
| POP_TOP | 30,660 | 10.1% |
| GET_ITER | 15,300 | 5.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 516,740 | 87.7% |
| LOAD_ATTR_METHOD_LAZY_DICT | 42,660 | 7.2% |
| LOAD_ATTR | 17,786 | 3.0% |
| LOAD_FAST | 5,060 | 0.9% |
| LOAD_SUPER_ATTR_METHOD | 5,040 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 148,300 | 25.2% |
| STORE_FAST | 115,380 | 19.6% |
| GET_ITER | 57,660 | 9.8% |
| STORE_SUBSCR | 51,200 | 8.7% |
| BINARY_SUBSCR | 46,080 | 7.8% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,320 | 41.2% |
| LOAD_FAST | 76,240 | 37.2% |
| BINARY_SLICE | 22,960 | 11.2% |
| STORE_FAST | 10,420 | 5.1% |
| LOAD_ATTR_INSTANCE_VALUE | 5,060 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 99,600 | 48.6% |
| POP_TOP | 30,560 | 14.9% |
| RETURN_VALUE | 28,300 | 13.8% |
| STORE_FAST | 15,360 | 7.5% |
| LOAD_CONST | 12,860 | 6.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 401,820 | 38.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 268,820 | 25.7% |
| LOAD_FAST_LOAD_FAST | 114,380 | 10.9% |
| LOAD_ATTR | 42,960 | 4.1% |
| GET_ITER | 40,740 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 896,560 | 85.6% |
| COPY_FREE_VARS | 86,900 | 8.3% |
| RETURN_GENERATOR | 58,720 | 5.6% |
| MAKE_CELL | 2,580 | 0.2% |
| STORE_FAST | 2,080 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,480 | 25.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 58,760 | 24.0% |
| LOAD_FAST | 45,680 | 18.7% |
| LOAD_ATTR_INSTANCE_VALUE | 32,840 | 13.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 15,240 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 242,280 | 99.0% |
| MAKE_CELL | 2,540 | 1.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,780 | 83.2% |
| RETURN_VALUE | 2,520 | 16.4% |
| CALL | 60 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 12,720 | 82.8% |
| STORE_FAST | 2,580 | 16.8% |
| LOAD_ATTR | 40 | 0.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 0.1% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,200 | 99.6% |
| CALL | 20 | 0.2% |
| LOAD_GLOBAL_MODULE | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120 | 50.0% |
| CALL_PY_EXACT_ARGS | 5,080 | 49.6% |
| PUSH_NULL | 20 | 0.2% |
| CALL | 20 | 0.2% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 236,980 | 67.2% |
| LOAD_GLOBAL_MODULE | 33,120 | 9.4% |
| LOAD_ATTR_INSTANCE_VALUE | 30,600 | 8.7% |
| CALL | 10,200 | 2.9% |
| COPY | 10,120 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 258,100 | 73.2% |
| POP_JUMP_IF_TRUE | 53,780 | 15.2% |
| EXTENDED_ARG | 30,680 | 8.7% |
| STORE_FAST | 10,240 | 2.9% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 109,500 | 43.7% |
| LOAD_FAST | 107,460 | 42.9% |
| LOAD_GLOBAL_MODULE | 33,080 | 13.2% |
| COMPARE_OP | 520 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 120,220 | 48.0% |
| POP_JUMP_IF_FALSE | 112,440 | 44.9% |
| YIELD_VALUE | 12,780 | 5.1% |
| EXTENDED_ARG | 5,080 | 2.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 127,560 | 67.1% |
| GET_ITER | 41,800 | 22.0% |
| SWAP | 17,660 | 9.3% |
| LOAD_FAST | 2,540 | 1.3% |
| FOR_ITER | 680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 117,580 | 61.8% |
| POP_TOP | 48,320 | 25.4% |
| STORE_FAST | 15,120 | 7.9% |
| JUMP_FORWARD | 8,720 | 4.6% |
| FOR_ITER | 440 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 242,600 | 60.1% |
| GET_ITER | 124,720 | 30.9% |
| SWAP | 25,480 | 6.3% |
| LOAD_FAST | 5,060 | 1.3% |
| EXTENDED_ARG | 5,040 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 147,800 | 36.6% |
| STORE_FAST | 105,000 | 26.0% |
| LOAD_FAST | 63,740 | 15.8% |
| RETURN_CONST | 33,220 | 8.2% |
| SWAP | 20,480 | 5.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,540 | 85.3% |
| GET_ITER | 15,340 | 14.6% |
| FOR_ITER | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 89,540 | 85.3% |
| LOAD_FAST | 10,320 | 9.8% |
| LOAD_CONST | 5,100 | 4.9% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 205,240 | 76.9% |
| GET_ITER | 46,100 | 17.3% |
| LOAD_FAST | 15,320 | 5.7% |
| SWAP | 220 | 0.1% |
| FOR_ITER | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 204,800 | 76.7% |
| LOAD_FAST | 46,120 | 17.3% |
| RETURN_CONST | 15,380 | 5.8% |
| STORE_FAST_LOAD_FAST | 480 | 0.2% |
| SWAP | 220 | 0.1% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,060 | 99.2% |
| LOAD_ATTR | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 50.2% |
| GET_ITER | 2,540 | 49.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,665,780 | 92.1% |
| LOAD_FAST_LOAD_FAST | 58,320 | 3.2% |
| COPY | 43,320 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 22,840 | 1.3% |
| LOAD_DEREF | 12,600 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 314,200 | 17.4% |
| LOAD_ATTR_METHOD_NO_DICT | 295,900 | 16.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 150,360 | 8.3% |
| LOAD_CONST | 109,720 | 6.1% |
| STORE_FAST | 94,580 | 5.2% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 58,200 | 66.8% |
| LOAD_FAST | 28,420 | 32.6% |
| LOAD_ATTR | 460 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 60 | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 42,660 | 48.9% |
| LOAD_CONST | 15,240 | 17.5% |
| LOAD_FAST | 12,720 | 14.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 10,080 | 11.6% |
| LOAD_GLOBAL_MODULE | 6,060 | 7.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,093,700 | 64.5% |
| LOAD_ATTR_INSTANCE_VALUE | 295,900 | 17.4% |
| LOAD_GLOBAL_MODULE | 86,700 | 5.1% |
| LOAD_CONST | 68,720 | 4.1% |
| LOAD_FAST_LOAD_FAST | 20,400 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 516,740 | 30.5% |
| LOAD_CONST | 426,400 | 25.1% |
| LOAD_FAST | 401,653 | 23.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 114,920 | 6.8% |
| CALL | 70,660 | 4.2% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 562,200 | 72.9% |
| LOAD_ATTR_INSTANCE_VALUE | 150,360 | 19.5% |
| LOAD_ATTR | 38,260 | 5.0% |
| LOAD_ATTR_MODULE | 12,600 | 1.6% |
| LOAD_GLOBAL_MODULE | 5,060 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 268,820 | 34.9% |
| LOAD_FAST | 196,120 | 25.4% |
| LOAD_CONST | 122,400 | 15.9% |
| LOAD_FAST_LOAD_FAST | 102,080 | 13.2% |
| CALL_PY_WITH_DEFAULTS | 58,760 | 7.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 171,260 | 92.5% |
| LOAD_ATTR_MODULE | 12,680 | 6.9% |
| LOAD_ATTR | 1,140 | 0.6% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 79,280 | 42.8% |
| CALL_ISINSTANCE | 22,800 | 12.3% |
| LOAD_FAST | 15,460 | 8.4% |
| LOAD_ATTR_MODULE | 12,680 | 6.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,600 | 6.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,080 | 78.1% |
| LOAD_FAST_LOAD_FAST | 2,520 | 19.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 200 | 1.6% |
| LOAD_ATTR | 100 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,040 | 39.1% |
| LOAD_FAST | 2,540 | 19.7% |
| CALL_BUILTIN_FAST | 2,520 | 19.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,520 | 19.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 200 | 1.6% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,160 | 72.2% |
| LOAD_FAST_LOAD_FAST | 7,560 | 27.1% |
| LOAD_ATTR | 220 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,700 | 45.5% |
| LOAD_FAST | 5,080 | 18.2% |
| PUSH_NULL | 2,540 | 9.1% |
| CONVERT_VALUE | 2,540 | 9.1% |
| COMPARE_OP_INT | 2,520 | 9.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 73,560 | 93.1% |
| RETURN_VALUE | 2,520 | 3.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,520 | 3.2% |
| LOAD_ATTR | 420 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 79,020 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40,920 | 53.1% |
| LOAD_FAST | 30,500 | 39.6% |
| COPY | 5,040 | 6.5% |
| LOAD_ATTR_MODULE | 280 | 0.4% |
| LOAD_ATTR | 220 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,200 | 53.5% |
| LOAD_CONST | 12,820 | 16.6% |
| GET_ITER | 10,220 | 13.3% |
| PUSH_NULL | 2,540 | 3.3% |
| BUILD_MAP | 2,540 | 3.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 405,620 | 26.8% |
| STORE_FAST | 232,120 | 15.3% |
| LOAD_FAST | 214,260 | 14.2% |
| POP_JUMP_IF_FALSE | 130,200 | 8.6% |
| POP_JUMP_IF_TRUE | 86,820 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 968,480 | 64.0% |
| CALL_ISINSTANCE | 242,540 | 16.0% |
| LOAD_DEREF | 68,880 | 4.6% |
| CHECK_EXC_MATCH | 63,980 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 45,700 | 3.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 329,400 | 20.2% |
| RESUME_CHECK | 312,080 | 19.1% |
| STORE_FAST | 219,000 | 13.4% |
| POP_JUMP_IF_FALSE | 165,380 | 10.1% |
| STORE_ATTR_INSTANCE_VALUE | 91,220 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 416,440 | 25.5% |
| LOAD_FAST_LOAD_FAST | 289,420 | 17.7% |
| LOAD_ATTR_MODULE | 171,260 | 10.5% |
| CALL_ISINSTANCE | 122,220 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 86,700 | 5.3% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,760 | 99.8% |
| LOAD_SUPER_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 12,780 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,760 | 99.5% |
| LOAD_SUPER_ATTR | 260 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 12,860 | 25.2% |
| CALL_PY_EXACT_ARGS | 12,680 | 24.9% |
| LOAD_FAST_LOAD_FAST | 10,240 | 20.1% |
| LOAD_FAST | 10,200 | 20.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 5,040 | 9.9% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 896,560 | 34.8% |
| CACHE | 637,926 | 24.7% |
| CALL_PY_WITH_DEFAULTS | 242,280 | 9.4% |
| COPY_FREE_VARS | 145,760 | 5.7% |
| FOR_ITER_GEN | 117,580 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,334,526 | 51.8% |
| LOAD_GLOBAL_BUILTIN | 405,620 | 15.7% |
| LOAD_GLOBAL_MODULE | 312,080 | 12.1% |
| POP_TOP | 171,320 | 6.6% |
| NOP | 135,540 | 5.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 2,540 | 49.8% |
| LOAD_CONST | 2,540 | 49.8% |
| SEND | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,540 | 49.8% |
| RESUME_CHECK | 2,540 | 49.8% |
| RESUME | 20 | 0.4% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 578,240 | 57.8% |
| LOAD_FAST_LOAD_FAST | 363,560 | 36.4% |
| SWAP | 43,320 | 4.3% |
| LOAD_ATTR_INSTANCE_VALUE | 7,600 | 0.8% |
| STORE_ATTR | 4,840 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 247,780 | 24.8% |
| LOAD_FAST | 237,460 | 23.7% |
| LOAD_CONST | 165,440 | 16.5% |
| RETURN_CONST | 147,980 | 14.8% |
| LOAD_GLOBAL_MODULE | 91,220 | 9.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,260 | 49.7% |
| LOAD_FAST_LOAD_FAST | 15,260 | 37.4% |
| SWAP | 5,040 | 12.4% |
| STORE_ATTR | 240 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 12,780 | 31.3% |
| LOAD_FAST | 12,760 | 31.3% |
| LOAD_FAST_LOAD_FAST | 7,620 | 18.7% |
| LOAD_CONST | 5,100 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 2,520 | 6.2% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 58,840 | 62.2% |
| LOAD_CONST | 17,640 | 18.6% |
| BINARY_OP_ADD_UNICODE | 12,760 | 13.5% |
| LOAD_FAST | 2,560 | 2.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,520 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 74,180 | 78.4% |
| LOAD_FAST | 10,180 | 10.8% |
| LOAD_CONST | 7,620 | 8.1% |
| LOAD_FAST_LOAD_FAST | 2,540 | 2.7% |
| NOP | 40 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,760 | 99.8% |
| STORE_SUBSCR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 12,780 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 53,900 | 57.5% |
| LOAD_ATTR | 22,420 | 23.9% |
| LOAD_FAST | 17,020 | 18.2% |
| TO_BOOL | 300 | 0.3% |
| TO_BOOL_NONE | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 73,900 | 78.8% |
| POP_JUMP_IF_FALSE | 19,720 | 21.0% |
| TO_BOOL_NONE | 120 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 351,500 | 30.1% |
| LOAD_FAST | 275,180 | 23.6% |
| CALL | 122,320 | 10.5% |
| RETURN_CONST | 94,500 | 8.1% |
| LOAD_ATTR_INSTANCE_VALUE | 89,140 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 804,626 | 68.9% |
| POP_JUMP_IF_TRUE | 355,180 | 30.4% |
| UNARY_NOT | 5,080 | 0.4% |
| EXTENDED_ARG | 2,560 | 0.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 30,680 | 52.2% |
| LOAD_FAST | 10,120 | 17.2% |
| LOAD_ATTR | 7,600 | 12.9% |
| COPY | 5,040 | 8.6% |
| CALL_LEN | 2,540 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 38,340 | 65.2% |
| POP_JUMP_IF_FALSE | 20,440 | 34.8% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,620 | 79.7% |
| LOAD_ATTR_INSTANCE_VALUE | 10,100 | 19.8% |
| TO_BOOL | 260 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 33,100 | 64.9% |
| POP_JUMP_IF_TRUE | 17,880 | 35.1% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 141,280 | 51.9% |
| COPY | 58,300 | 21.4% |
| LOAD_ATTR_INSTANCE_VALUE | 25,240 | 9.3% |
| CALL | 25,180 | 9.2% |
| LOAD_ATTR | 13,100 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 160,500 | 58.9% |
| POP_JUMP_IF_TRUE | 106,680 | 39.2% |
| EXTENDED_ARG | 4,780 | 1.8% |
| TO_BOOL_STR | 300 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 100 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 281,880 | 86.2% |
| COPY | 30,560 | 9.3% |
| BINARY_SUBSCR_LIST_INT | 7,640 | 2.3% |
| STORE_FAST | 5,040 | 1.5% |
| TO_BOOL | 1,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 202,940 | 62.1% |
| POP_JUMP_IF_FALSE | 113,080 | 34.6% |
| EXTENDED_ARG | 10,540 | 3.2% |
| TO_BOOL_NONE | 340 | 0.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 12,720 | 99.7% |
| UNPACK_SEQUENCE | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 12,760 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 99,600 | 64.9% |
| RETURN_VALUE | 38,240 | 24.9% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 7,640 | 5.0% |
| LOAD_FAST | 5,040 | 3.3% |
| LOAD_CONST | 2,520 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 132,900 | 86.7% |
| POP_TOP | 20,460 | 13.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 147,800 | 50.2% |
| FOR_ITER | 80,020 | 27.2% |
| LOAD_FAST | 22,920 | 7.8% |
| YIELD_VALUE | 20,240 | 6.9% |
| CALL | 10,200 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 281,560 | 95.7% |
| STORE_FAST | 10,220 | 3.5% |
| LOAD_FAST | 2,540 | 0.9% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 126,340 | 31.9% |
|          hit | 268,540 | 67.7% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 720 | 46.8% |
| Failure | 820 | 53.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 620 | 75.6% |
| add different types | 200 | 24.4% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 76,560 | 16.4% |
|          hit | 387,200 | 83.2% |
|         miss | 12,140 | 2.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 840 | 50.0% |
| Failure | 840 | 50.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 400 | 47.6% |
| code complex parameters | 240 | 28.6% |
| other | 200 | 23.8% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 937,819 | 19.3% |
|          hit | 3,892,220 | 80.1% |
|         miss | 54,246 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 13,500 | 43.6% |
| Failure | 17,440 | 56.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 2,820 | 16.2% |
| meth descr varargs | 2,820 | 16.2% |
| class no vectorcall | 2,000 | 11.5% |
| meth descr method fastcall keywords | 1,960 | 11.2% |
| metaclass | 1,720 | 9.9% |
| cfunc noargs | 1,160 | 6.7% |
| meth descr varargs keywords | 1,140 | 6.5% |
| cfunc varargs keywords | 840 | 4.8% |
| operator wrapper | 640 | 3.7% |
| other | 420 | 2.4% |
| wrong number arguments | 400 | 2.3% |
| cfunc varargs | 380 | 2.2% |
| cmethod | 320 | 1.8% |
| class mutable | 320 | 1.8% |
| no dict | 240 | 1.4% |
| method wrapper | 140 | 0.8% |
| str | 120 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 116,960 | 16.2% |
|          hit | 600,860 | 83.3% |
|         miss | 2,560 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,680 | 48.8% |
| Failure | 1,760 | 51.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 880 | 50.0% |
| big int | 260 | 14.8% |
| bytes | 200 | 11.4% |
| bool | 180 | 10.2% |
| list | 120 | 6.8% |
| set | 120 | 6.8% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 268,260 | 22.3% |
|          hit | 929,320 | 77.2% |
|         miss | 36,640 | 3.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,740 | 29.6% |
| Failure | 4,140 | 70.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,540 | 37.2% |
| dict keys | 1,160 | 28.0% |
| dict items | 420 | 10.1% |
| enumerate | 340 | 8.2% |
| dict values | 300 | 7.2% |
| reversed list | 160 | 3.9% |
| set | 140 | 3.4% |
| ascii string | 80 | 1.9% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 743,518 | 13.5% |
|          hit | 4,721,333 | 85.8% |
|         miss | 29,240 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,020 | 42.4% |
| Failure | 21,800 | 57.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 16,600 | 76.1% |
| method | 1,740 | 8.0% |
| class attr descriptor | 720 | 3.3% |
| metaclass attribute | 680 | 3.1% |
| module attr not found | 620 | 2.8% |
| class method obj | 600 | 2.8% |
| class attr simple | 360 | 1.7% |
| non overriding descriptor | 240 | 1.1% |
| mutable class | 240 | 1.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,700 | 0.4% |
|        deopt | 800 | 0.0% |
|          hit | 3,144,340 | 99.3% |
|         miss | 2,080 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,960 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.4% |
|          hit | 63,800 | 99.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.4% |
|          hit | 5,100 | 99.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 186,720 | 15.1% |
|          hit | 1,037,820 | 83.9% |
|         miss | 3,100 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,120 | 39.3% |
| Failure | 7,900 | 60.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 6,980 | 88.4% |
| class attr simple | 420 | 5.3% |
| property | 360 | 4.6% |
| overridden | 120 | 1.5% |
| no dict | 20 | 0.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 112,900 | 50.9% |
|          hit | 107,380 | 48.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 19.1% |
| Failure | 1,100 | 80.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 640 | 58.2% |
| other | 460 | 41.8% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 241,720 | 11.1% |
|          hit | 1,918,386 | 88.4% |
|         miss | 51,820 | 2.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,500 | 67.0% |
| Failure | 3,700 | 33.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 1,480 | 40.0% |
| dict | 860 | 23.2% |
| sequence | 620 | 16.8% |
| set | 240 | 6.5% |
| tuple | 240 | 6.5% |
| other | 140 | 3.8% |
| mapping | 120 | 3.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 28,940 | 5.9% |
|          hit | 460,440 | 93.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 72.2% |
| Failure | 300 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 300 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 29,189,462 | 52.0% |
| Not specialized | 6,723,417 | 12.0% |
| Specialized hits | 20,081,625 | 35.7% |
| Specialized misses | 191,886 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 937,819 | 32.9% |
| LOAD_ATTR | 743,518 | 26.1% |
| FOR_ITER | 268,260 | 9.4% |
| TO_BOOL | 241,720 | 8.5% |
| STORE_ATTR | 186,720 | 6.5% |
| BINARY_OP | 126,340 | 4.4% |
| COMPARE_OP | 116,960 | 4.1% |
| STORE_SUBSCR | 112,900 | 4.0% |
| BINARY_SUBSCR | 76,560 | 2.7% |
| UNPACK_SEQUENCE | 28,940 | 1.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 30,166 | 15.7% |
| FOR_ITER_GEN | 24,280 | 12.7% |
| TO_BOOL_NONE | 24,160 | 12.6% |
| TO_BOOL_STR | 21,300 | 11.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 12,600 | 6.6% |
| FOR_ITER_LIST | 12,360 | 6.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 7,880 | 4.1% |
| CALL_METHOD_DESCRIPTOR_O | 7,760 | 4.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,220 | 3.8% |
| BINARY_SUBSCR_GETITEM | 6,840 | 3.6% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 739,986 | 27.6% |
| Calls to Python functions inlined | 1,939,420 | 72.4% |
| Calls via PyEval_EvalFrame (total) | 739,986 | 27.6% |
| Calls via PyEval_EvalFrame (vector) | 644,746 | 24.1% |
| Calls via PyEval_EvalFrame (generator) | 95,240 | 3.6% |
| Calls via PyEval_EvalFrame (legacy) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 644,666 | 24.1% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 114,820 | 4.3% |
| Calls via PyEval_EvalFrame (function ex) | 25,780 | 1.0% |
| Calls via PyEval_EvalFrame (api) | 67,120 | 2.5% |
| Calls via PyEval_EvalFrame (method) | 23,026 | 0.9% |
| Frame objects created | 97,360 | 3.6% |
| Frames pushed | 1,563,200 | 58.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 2,219,213 | 36.8% |
| Frees to freelist | 2,220,253 |  |
| Allocations | 3,807,686 | 63.2% |
| Allocations to 512 bytes | 3,776,666 | 62.7% |
| Allocations to 4 kbytes | 28,420 | 0.5% |
| Allocations over 4 kbytes | 2,600 | 0.0% |
| Frees | 4,001,678 |  |
| New values | 95,100 |  |
| Interpreter increfs | 24,551,135 | 73.8% |
| Interpreter decrefs | 28,421,754 | 73.7% |
| Increfs | 8,704,257 | 26.2% |
| Decrefs | 10,157,748 | 26.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 20 | 0.0% |
| Method cache hits | 1,320,422 |  |
| Method cache misses | 51,741 |  |
| Method cache collisions | 72,654 |  |
| Method cache dunder hits | 1,003,437 |  |
| Method cache dunder misses | 23,763 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 0 |  |
| Traces created | 0 |  |
| Trace stack overflow | 0 |  |
| Trace stack underflow | 0 |  |
| Trace too long | 0 |  |
| Trace too short | 0 |  |
| Inner loop found | 0 |  |
| Recursive call | 0 |  |
| Low confidence | 0 |  |
| Traces executed | 0 |  |
| Uops executed | 0 |  |

### Trace length histogram

<details>
<summary> trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 |  |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 |  |


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 |  |


</details>

### Uop execution stats

<details>
<summary> uop execution stats </summary>


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>


</details>


</details>

## Rare events

<details>
<summary> Counts of rare/unlikely events </summary>

|Event | Count | 
|---|---:|
| set class | 0 |
| set bases | 0 |
| set eval frame func | 0 |
| builtin dict | 0 |
| func modification | 0 |
| watched dict modification | 0 |
| watched globals modification | 0 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
