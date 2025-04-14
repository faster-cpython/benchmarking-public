
# Pystats results

- benchmark: asyncio_websockets
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 5,031,514 | 18.6% | 18.6% |  |
| POP_JUMP_IF_FALSE | 1,501,488 | 5.6% | 24.2% |  |
| LOAD_ATTR_SLOT | 1,299,760 | 4.8% | 29.0% | 0.4% |
| LOAD_CONST | 1,175,118 | 4.3% | 33.3% |  |
| LOAD_FAST_LOAD_FAST | 1,099,140 | 4.1% | 37.4% |  |
| LOAD_GLOBAL_MODULE | 1,058,800 | 3.9% | 41.3% | 0.1% |
| STORE_FAST | 988,580 | 3.7% | 44.9% |  |
| RESUME_CHECK | 888,960 | 3.3% | 48.2% | 0.0% |
| TO_BOOL_BOOL | 850,080 | 3.1% | 51.4% |  |
| LOAD_ATTR_INSTANCE_VALUE | 830,776 | 3.1% | 54.4% | 0.1% |
| LOAD_GLOBAL_BUILTIN | 747,387 | 2.8% | 57.2% | 0.4% |
| LOAD_ATTR | 721,420 | 2.7% | 59.9% |  |
| POP_JUMP_IF_TRUE | 580,960 | 2.1% | 62.0% |  |
| POP_TOP | 565,881 | 2.1% | 64.1% |  |
| RETURN_VALUE | 519,740 | 1.9% | 66.0% |  |
| CALL_PY_EXACT_ARGS | 464,640 | 1.7% | 67.8% | 0.1% |
| IS_OP | 418,560 | 1.5% | 69.3% |  |
| RETURN_CONST | 384,340 | 1.4% | 70.7% |  |
| CALL | 359,719 | 1.3% | 72.1% |  |
| PUSH_NULL | 311,080 | 1.2% | 73.2% |  |
| JUMP_BACKWARD | 305,400 | 1.1% | 74.3% |  |
| LOAD_ATTR_MODULE | 280,160 | 1.0% | 75.4% | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 276,341 | 1.0% | 76.4% | 0.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 271,740 | 1.0% | 77.4% | 0.0% |
| CALL_BUILTIN_FAST | 266,260 | 1.0% | 78.4% | 0.0% |
| CONTAINS_OP | 260,720 | 1.0% | 79.3% |  |
| FOR_ITER | 250,860 | 0.9% | 80.3% |  |
| COMPARE_OP_INT | 250,808 | 0.9% | 81.2% | 0.1% |
| LOAD_ATTR_WITH_HINT | 229,640 | 0.8% | 82.1% | 3.2% |
| BINARY_OP | 225,760 | 0.8% | 82.9% |  |
| STORE_ATTR | 225,700 | 0.8% | 83.7% |  |
| INTERPRETER_EXIT | 209,660 | 0.8% | 84.5% |  |
| CALL_LEN | 195,908 | 0.7% | 85.2% |  |
| STORE_ATTR_SLOT | 180,460 | 0.7% | 85.9% | 4.7% |
| STORE_SUBSCR_DICT | 170,200 | 0.6% | 86.5% |  |
| POP_JUMP_IF_NONE | 165,920 | 0.6% | 87.1% |  |
| RETURN_GENERATOR | 159,800 | 0.6% | 87.7% |  |
| SEND_GEN | 154,200 | 0.6% | 88.3% |  |
| GET_AWAITABLE | 151,360 | 0.6% | 88.9% |  |
| END_SEND | 151,040 | 0.6% | 89.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 149,700 | 0.6% | 90.0% | 0.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 142,661 | 0.5% | 90.5% | 7.0% |
| POP_JUMP_IF_NOT_NONE | 131,240 | 0.5% | 91.0% |  |
| NOP | 121,000 | 0.4% | 91.4% |  |
| JUMP_FORWARD | 108,501 | 0.4% | 91.8% |  |
| CALL_KW | 99,320 | 0.4% | 92.2% |  |
| CALL_FUNCTION_EX | 93,760 | 0.3% | 92.5% |  |
| BUILD_TUPLE | 90,580 | 0.3% | 92.9% |  |
| LOAD_DEREF | 88,480 | 0.3% | 93.2% |  |
| TO_BOOL_NONE | 83,440 | 0.3% | 93.5% | 0.1% |
| TO_BOOL | 83,340 | 0.3% | 93.8% |  |
| BINARY_SLICE | 81,539 | 0.3% | 94.1% |  |
| CALL_METHOD_DESCRIPTOR_O | 79,040 | 0.3% | 94.4% | 1.0% |
| BUILD_MAP | 71,480 | 0.3% | 94.7% |  |
| GET_ITER | 70,900 | 0.3% | 94.9% |  |
| DICT_MERGE | 67,600 | 0.2% | 95.2% |  |
| TO_BOOL_INT | 61,740 | 0.2% | 95.4% | 0.1% |
| CALL_TYPE_1 | 59,480 | 0.2% | 95.6% |  |
| COMPARE_OP | 59,460 | 0.2% | 95.9% |  |
| FOR_ITER_RANGE | 56,240 | 0.2% | 96.1% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 51,940 | 0.2% | 96.3% | 19.0% |
| CALL_ISINSTANCE | 44,580 | 0.2% | 96.4% |  |
| FOR_ITER_LIST | 43,020 | 0.2% | 96.6% |  |
| BUILD_LIST | 40,000 | 0.1% | 96.7% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 35,520 | 0.1% | 96.9% | 93.7% |
| DELETE_SUBSCR | 33,919 | 0.1% | 97.0% |  |
| BUILD_SLICE | 33,659 | 0.1% | 97.1% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 32,460 | 0.1% | 97.2% |  |
| LOAD_GLOBAL | 31,900 | 0.1% | 97.3% |  |
| BINARY_OP_ADD_INT | 31,580 | 0.1% | 97.5% |  |
| MAKE_CELL | 31,320 | 0.1% | 97.6% |  |
| STORE_FAST_STORE_FAST | 29,660 | 0.1% | 97.7% |  |
| EXTENDED_ARG | 26,200 | 0.1% | 97.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 26,020 | 0.1% | 97.9% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 25,120 | 0.1% | 98.0% |  |
| CALL_INTRINSIC_1 | 24,820 | 0.1% | 98.1% |  |
| LIST_EXTEND | 24,740 | 0.1% | 98.2% |  |
| COPY | 24,320 | 0.1% | 98.2% |  |
| CALL_LIST_APPEND | 23,480 | 0.1% | 98.3% |  |
| BINARY_SUBSCR_DICT | 23,060 | 0.1% | 98.4% |  |
| STORE_DEREF | 21,720 | 0.1% | 98.5% |  |
| TO_BOOL_LIST | 19,680 | 0.1% | 98.6% |  |
| CALL_ALLOC_AND_ENTER_INIT | 19,080 | 0.1% | 98.6% | 0.2% |
| EXIT_INIT_CHECK | 19,040 | 0.1% | 98.7% |  |
| COPY_FREE_VARS | 18,940 | 0.1% | 98.8% |  |
| CALL_BUILTIN_CLASS | 16,880 | 0.1% | 98.8% |  |
| LOAD_FAST_CHECK | 16,820 | 0.1% | 98.9% |  |
| MAP_ADD | 16,040 | 0.1% | 99.0% |  |
| FOR_ITER_TUPLE | 14,260 | 0.1% | 99.0% |  |
| SWAP | 13,940 | 0.1% | 99.1% |  |
| STORE_SUBSCR | 13,720 | 0.1% | 99.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 13,080 | 0.0% | 99.2% |  |
| YIELD_VALUE | 12,980 | 0.0% | 99.2% |  |
| LIST_APPEND | 12,700 | 0.0% | 99.3% |  |
| CALL_BUILTIN_O | 12,060 | 0.0% | 99.3% | 1.7% |
| LOAD_ATTR_PROPERTY | 11,460 | 0.0% | 99.4% |  |
| STORE_FAST_LOAD_FAST | 11,220 | 0.0% | 99.4% |  |
| RESUME | 10,360 | 0.0% | 99.4% | 0.2% |
| UNPACK_SEQUENCE_TUPLE | 10,040 | 0.0% | 99.5% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 9,760 | 0.0% | 99.5% |  |
| SEND | 9,400 | 0.0% | 99.5% |  |
| BEFORE_ASYNC_WITH | 9,120 | 0.0% | 99.6% |  |
| UNARY_NOT | 9,000 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_LIST_INT | 6,980 | 0.0% | 99.6% |  |
| MAKE_FUNCTION | 6,860 | 0.0% | 99.7% |  |
| COMPARE_OP_FLOAT | 5,700 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_METHOD | 5,440 | 0.0% | 99.7% |  |
| COMPARE_OP_STR | 5,360 | 0.0% | 99.7% | 4.1% |
| TO_BOOL_STR | 4,840 | 0.0% | 99.7% |  |
| BINARY_OP_SUBTRACT_INT | 4,780 | 0.0% | 99.8% |  |
| BEFORE_WITH | 3,760 | 0.0% | 99.8% |  |
| BINARY_OP_ADD_FLOAT | 3,740 | 0.0% | 99.8% |  |
| CALL_PY_WITH_DEFAULTS | 3,640 | 0.0% | 99.8% |  |
| SET_FUNCTION_ATTRIBUTE | 3,420 | 0.0% | 99.8% |  |
| CHECK_EXC_MATCH | 3,060 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 3,060 | 0.0% | 99.8% |  |
| POP_EXCEPT | 3,040 | 0.0% | 99.8% |  |
| STORE_NAME | 3,020 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 2,900 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 2,680 | 0.0% | 99.9% |  |
| STORE_ATTR_WITH_HINT | 2,620 | 0.0% | 99.9% | 11.5% |
| BINARY_SUBSCR | 2,480 | 0.0% | 99.9% |  |
| TO_BOOL_ALWAYS_TRUE | 2,460 | 0.0% | 99.9% | 6.5% |
| LOAD_FAST_AND_CLEAR | 2,360 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE | 2,100 | 0.0% | 99.9% |  |
| BUILD_STRING | 1,540 | 0.0% | 99.9% |  |
| LOAD_NAME | 1,460 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_STR_INT | 1,420 | 0.0% | 99.9% | 11.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,340 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR_ATTR | 1,340 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_LIST | 1,140 | 0.0% | 100.0% |  |
| UNARY_INVERT | 1,120 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,060 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 1,020 | 0.0% | 100.0% | 2.0% |
| BINARY_SUBSCR_TUPLE_INT | 1,020 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 900 | 0.0% | 100.0% |  |
| RERAISE | 880 | 0.0% | 100.0% |  |
| DICT_UPDATE | 760 | 0.0% | 100.0% |  |
| CALL_STR_1 | 720 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 720 | 0.0% | 100.0% |  |
| BUILD_SET | 560 | 0.0% | 100.0% |  |
| IMPORT_NAME | 500 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 500 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 420 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 400 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 360 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 320 | 0.0% | 100.0% |  |
| DELETE_FAST | 320 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 260 | 0.0% | 100.0% |  |
| IMPORT_FROM | 220 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 220 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 200 | 0.0% | 100.0% |  |
| DELETE_ATTR | 180 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 140 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 120 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 80 | 0.0% | 100.0% |  |
| STORE_SLICE | 40 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_SLOT | 964,960 | 3.6% | 3.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 805,536 | 3.0% | 6.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 786,740 | 2.9% | 9.5% |
| STORE_FAST LOAD_FAST | 728,700 | 2.7% | 12.2% |
| LOAD_FAST LOAD_ATTR | 548,020 | 2.0% | 14.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 511,380 | 1.9% | 16.1% |
| RESUME_CHECK LOAD_FAST | 469,240 | 1.7% | 17.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 451,520 | 1.7% | 19.5% |
| IS_OP POP_JUMP_IF_FALSE | 416,300 | 1.5% | 21.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 404,728 | 1.5% | 22.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 378,260 | 1.4% | 23.9% |
| LOAD_GLOBAL_MODULE IS_OP | 353,720 | 1.3% | 25.2% |
| LOAD_ATTR_SLOT LOAD_GLOBAL_MODULE | 351,920 | 1.3% | 26.5% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 329,800 | 1.2% | 27.7% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_SLOT | 320,060 | 1.2% | 28.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 306,948 | 1.1% | 30.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 275,620 | 1.0% | 31.1% |
| LOAD_FAST LOAD_CONST | 261,080 | 1.0% | 32.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 248,128 | 0.9% | 33.0% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 226,920 | 0.8% | 33.8% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 223,840 | 0.8% | 34.6% |
| LOAD_CONST LOAD_FAST | 214,218 | 0.8% | 35.4% |
| JUMP_BACKWARD FOR_ITER | 204,580 | 0.8% | 36.2% |
| FOR_ITER STORE_FAST | 204,540 | 0.8% | 36.9% |
| LOAD_FAST CONTAINS_OP | 204,160 | 0.8% | 37.7% |
| LOAD_FAST_LOAD_FAST STORE_ATTR | 201,460 | 0.7% | 38.4% |
| LOAD_ATTR_SLOT LOAD_FAST | 198,820 | 0.7% | 39.2% |
| CONTAINS_OP POP_JUMP_IF_TRUE | 194,960 | 0.7% | 39.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 182,720 | 0.7% | 40.6% |
| RETURN_CONST POP_TOP | 179,380 | 0.7% | 41.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 178,540 | 0.7% | 41.9% |
| POP_TOP LOAD_FAST | 177,700 | 0.7% | 42.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 174,320 | 0.6% | 43.2% |
| LOAD_ATTR LOAD_FAST | 174,020 | 0.6% | 43.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 169,880 | 0.6% | 44.5% |
| CACHE RESUME_CHECK | 164,620 | 0.6% | 45.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 160,300 | 0.6% | 45.7% |
| STORE_SUBSCR_DICT JUMP_BACKWARD | 160,120 | 0.6% | 46.3% |
| LOAD_ATTR_SLOT CALL_BUILTIN_FAST | 160,080 | 0.6% | 46.8% |
| CALL_BUILTIN_FAST LOAD_FAST_LOAD_FAST | 159,980 | 0.6% | 47.4% |
| LOAD_ATTR_SLOT STORE_SUBSCR_DICT | 159,960 | 0.6% | 48.0% |
| POP_TOP RESUME_CHECK | 158,280 | 0.6% | 48.6% |
| POP_JUMP_IF_FALSE LOAD_CONST | 151,720 | 0.6% | 49.2% |
| GET_AWAITABLE LOAD_CONST | 151,360 | 0.6% | 49.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 150,320 | 0.6% | 50.3% |
| STORE_ATTR LOAD_FAST_LOAD_FAST | 148,860 | 0.6% | 50.8% |
| SEND_GEN POP_TOP | 147,080 | 0.5% | 51.4% |
| LOAD_CONST SEND_GEN | 146,220 | 0.5% | 51.9% |
| LOAD_ATTR TO_BOOL_BOOL | 145,740 | 0.5% | 52.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 141,900 | 0.5% | 53.0% |
| LOAD_FAST RETURN_VALUE | 139,900 | 0.5% | 53.5% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 139,100 | 0.5% | 54.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 138,480 | 0.5% | 54.5% |
| CALL STORE_FAST | 137,740 | 0.5% | 55.0% |
| RETURN_GENERATOR GET_AWAITABLE | 130,160 | 0.5% | 55.5% |
| LOAD_CONST COMPARE_OP_INT | 127,860 | 0.5% | 56.0% |
| LOAD_CONST BINARY_OP | 126,960 | 0.5% | 56.5% |
| PUSH_NULL LOAD_FAST | 123,680 | 0.5% | 56.9% |
| RETURN_VALUE STORE_FAST | 123,000 | 0.5% | 57.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 118,140 | 0.4% | 57.8% |
| POP_JUMP_IF_FALSE RETURN_CONST | 113,580 | 0.4% | 58.2% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 110,040 | 0.4% | 58.6% |
| POP_TOP RETURN_CONST | 109,560 | 0.4% | 59.0% |
| RETURN_CONST INTERPRETER_EXIT | 106,280 | 0.4% | 59.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 106,080 | 0.4% | 59.8% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 105,888 | 0.4% | 60.2% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 105,119 | 0.4% | 60.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 103,160 | 0.4% | 61.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 100,881 | 0.4% | 61.4% |
| LOAD_CONST CALL_KW | 99,320 | 0.4% | 61.7% |
| RETURN_VALUE RETURN_VALUE | 98,960 | 0.4% | 62.1% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 98,480 | 0.4% | 62.5% |
| NOP LOAD_FAST | 96,340 | 0.4% | 62.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 96,060 | 0.4% | 63.2% |
| POP_JUMP_IF_NONE LOAD_FAST | 93,240 | 0.3% | 63.5% |
| CALL_LEN LOAD_FAST | 92,248 | 0.3% | 63.9% |
| PUSH_NULL LOAD_CONST | 90,960 | 0.3% | 64.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 87,320 | 0.3% | 64.5% |
| LOAD_CONST STORE_FAST | 83,760 | 0.3% | 64.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 83,000 | 0.3% | 65.1% |
| LOAD_FAST STORE_ATTR_SLOT | 81,200 | 0.3% | 65.4% |
| RETURN_VALUE END_SEND | 80,400 | 0.3% | 65.7% |
| RETURN_VALUE TO_BOOL_BOOL | 79,680 | 0.3% | 66.0% |
| END_SEND POP_TOP | 79,440 | 0.3% | 66.3% |
| RETURN_VALUE INTERPRETER_EXIT | 79,280 | 0.3% | 66.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 78,520 | 0.3% | 66.9% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 75,380 | 0.3% | 67.2% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 75,100 | 0.3% | 67.5% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 75,100 | 0.3% | 67.7% |
| LOAD_FAST CALL_LEN | 72,720 | 0.3% | 68.0% |
| LOAD_FAST CALL | 72,620 | 0.3% | 68.3% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 72,520 | 0.3% | 68.5% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 72,420 | 0.3% | 68.8% |
| END_SEND STORE_FAST | 69,920 | 0.3% | 69.1% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 69,561 | 0.3% | 69.3% |
| LOAD_CONST LOAD_CONST | 69,520 | 0.3% | 69.6% |
| RETURN_CONST END_SEND | 68,080 | 0.3% | 69.8% |
| LOAD_FAST COMPARE_OP_INT | 67,880 | 0.3% | 70.1% |
| BUILD_MAP LOAD_FAST | 67,640 | 0.3% | 70.3% |
| DICT_MERGE CALL_FUNCTION_EX | 67,600 | 0.2% | 70.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,099 | 41.8% |
| LOAD_CONST | 19,520 | 23.9% |
| BINARY_OP | 16,200 | 19.9% |
| BINARY_OP_ADD_INT | 11,720 | 14.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 32,319 | 39.6% |
| STORE_FAST | 28,440 | 34.9% |
| BINARY_OP | 16,240 | 19.9% |
| RETURN_VALUE | 1,360 | 1.7% |
| LOAD_CONST | 1,300 | 1.6% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 164,620 | 78.3% |
| RETURN_GENERATOR | 18,320 | 8.7% |
| COPY_FREE_VARS | 13,340 | 6.3% |
| POP_TOP | 11,160 | 5.3% |
| RESUME | 2,380 | 1.1% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 8,140 | 89.3% |
| RETURN_VALUE | 800 | 8.8% |
| CALL | 160 | 1.8% |
| LOAD_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 9,120 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,840 | 48.9% |
| LOAD_GLOBAL_MODULE | 760 | 20.2% |
| CALL | 480 | 12.8% |
| RETURN_VALUE | 240 | 6.4% |
| LOAD_ATTR | 240 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,680 | 97.9% |
| STORE_FAST | 80 | 2.1% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_STR_1 | 80 | 66.7% |
| BINARY_OP | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,440 | 58.1% |
| BINARY_SUBSCR | 280 | 11.3% |
| LOAD_FAST | 240 | 9.7% |
| LOAD_GLOBAL_MODULE | 200 | 8.1% |
| LOAD_FAST_LOAD_FAST | 80 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 18.0% |
| BINARY_SUBSCR | 280 | 11.5% |
| STORE_FAST | 280 | 11.5% |
| BINARY_SUBSCR_LIST_INT | 240 | 9.8% |
| BUILD_TUPLE | 160 | 6.6% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,200 | 71.9% |
| BUILD_TUPLE | 320 | 10.5% |
| LOAD_ATTR_MODULE | 280 | 9.2% |
| LOAD_GLOBAL | 220 | 7.2% |
| LOAD_ATTR | 40 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,900 | 94.8% |
| EXTENDED_ARG | 160 | 5.2% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 320 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 33,599 | 99.1% |
| LOAD_FAST | 260 | 0.8% |
| CALL | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,599 | 99.1% |
| LOAD_CONST | 140 | 0.4% |
| LOAD_GLOBAL_MODULE | 120 | 0.4% |
| RETURN_CONST | 60 | 0.2% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80,400 | 53.2% |
| RETURN_CONST | 68,080 | 45.1% |
| SEND | 2,560 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 79,440 | 52.6% |
| STORE_FAST | 69,920 | 46.3% |
| RETURN_VALUE | 880 | 0.6% |
| UNPACK_SEQUENCE | 240 | 0.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 0.1% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 19,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 19,040 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,640 | 91.0% |
| LOAD_ATTR | 100 | 3.4% |
| CONVERT_VALUE | 80 | 2.8% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 2.1% |
| LOAD_FAST_LOAD_FAST | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,660 | 91.7% |
| BUILD_STRING | 240 | 8.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 32,600 | 46.0% |
| LOAD_FAST | 22,840 | 32.2% |
| CALL_BUILTIN_CLASS | 12,540 | 17.7% |
| LOAD_ATTR_INSTANCE_VALUE | 820 | 1.2% |
| CALL | 560 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 43,660 | 61.6% |
| FOR_ITER_LIST | 17,460 | 24.6% |
| FOR_ITER_RANGE | 4,100 | 5.8% |
| LOAD_FAST_AND_CLEAR | 2,200 | 3.1% |
| CALL_PY_EXACT_ARGS | 1,560 | 2.2% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 106,280 | 50.7% |
| RETURN_VALUE | 79,280 | 37.8% |
| RETURN_GENERATOR | 18,400 | 8.8% |
| YIELD_VALUE | 5,700 | 2.7% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 220 | 84.6% |
| POP_TOP | 40 | 15.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 260 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,860 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 3,400 | 49.6% |
| LOAD_FAST | 1,680 | 24.5% |
| STORE_NAME | 1,120 | 16.3% |
| LOAD_CONST | 420 | 6.1% |
| STORE_DEREF | 160 | 2.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 48,040 | 39.7% |
| STORE_FAST | 29,640 | 24.5% |
| POP_JUMP_IF_FALSE | 14,360 | 11.9% |
| POP_JUMP_IF_TRUE | 9,680 | 8.0% |
| POP_JUMP_IF_NOT_NONE | 8,760 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,340 | 79.6% |
| LOAD_GLOBAL_MODULE | 16,720 | 13.8% |
| LOAD_GLOBAL_BUILTIN | 2,640 | 2.2% |
| LOAD_GLOBAL | 1,420 | 1.2% |
| NOP | 1,380 | 1.1% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,560 | 51.3% |
| STORE_FAST | 420 | 13.8% |
| COPY | 400 | 13.2% |
| STORE_SUBSCR | 240 | 7.9% |
| SWAP | 240 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 620 | 20.4% |
| EXTENDED_ARG | 520 | 17.1% |
| RETURN_CONST | 500 | 16.4% |
| RERAISE | 400 | 13.2% |
| LOAD_FAST | 260 | 8.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 179,380 | 31.7% |
| SEND_GEN | 147,080 | 26.0% |
| END_SEND | 79,440 | 14.0% |
| CALL_METHOD_DESCRIPTOR_O | 75,380 | 13.3% |
| CALL_FUNCTION_EX | 24,800 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 177,700 | 31.4% |
| RESUME_CHECK | 158,280 | 28.0% |
| RETURN_CONST | 109,560 | 19.4% |
| LOAD_CONST | 42,720 | 7.5% |
| JUMP_BACKWARD | 37,880 | 6.7% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 980 | 32.0% |
| CALL | 680 | 22.2% |
| LOAD_ATTR | 340 | 11.1% |
| CLEANUP_THROW | 320 | 10.5% |
| CALL_BUILTIN_FAST | 300 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,920 | 62.7% |
| LOAD_GLOBAL | 660 | 21.6% |
| LOAD_GLOBAL_MODULE | 320 | 10.5% |
| LOAD_FAST | 160 | 5.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 174,320 | 56.0% |
| LOAD_FAST | 64,580 | 20.8% |
| LOAD_ATTR | 37,820 | 12.2% |
| LOAD_ATTR_SLOT | 31,980 | 10.3% |
| LOAD_NAME | 560 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 123,680 | 39.8% |
| LOAD_CONST | 90,960 | 29.2% |
| LOAD_FAST_LOAD_FAST | 61,460 | 19.8% |
| CALL | 31,360 | 10.1% |
| LOAD_DEREF | 800 | 0.3% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 72,520 | 45.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 32,320 | 20.2% |
| CACHE | 18,320 | 11.5% |
| CALL_KW | 17,200 | 10.8% |
| CALL | 9,260 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 130,160 | 81.5% |
| INTERPRETER_EXIT | 18,400 | 11.5% |
| LIST_APPEND | 8,080 | 5.1% |
| CALL | 1,520 | 1.0% |
| CALL_BUILTIN_O | 600 | 0.4% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,900 | 26.9% |
| RETURN_VALUE | 98,960 | 19.0% |
| LOAD_ATTR_INSTANCE_VALUE | 58,120 | 11.2% |
| CALL | 37,740 | 7.3% |
| CALL_FUNCTION_EX | 34,460 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 123,000 | 23.7% |
| RETURN_VALUE | 98,960 | 19.0% |
| END_SEND | 80,400 | 15.5% |
| TO_BOOL_BOOL | 79,680 | 15.3% |
| INTERPRETER_EXIT | 79,280 | 15.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,240 | 74.6% |
| LOAD_FAST | 1,580 | 11.5% |
| LOAD_CONST | 920 | 6.7% |
| STORE_SUBSCR | 420 | 3.1% |
| LOAD_FAST_LOAD_FAST | 200 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 11,160 | 81.3% |
| LOAD_FAST | 520 | 3.8% |
| STORE_SUBSCR | 420 | 3.1% |
| RETURN_CONST | 380 | 2.8% |
| LOAD_CONST | 300 | 2.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,980 | 27.6% |
| LOAD_ATTR_INSTANCE_VALUE | 22,060 | 26.5% |
| LOAD_ATTR | 20,760 | 24.9% |
| LOAD_ATTR_SLOT | 8,320 | 10.0% |
| CALL | 1,960 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40,560 | 48.7% |
| POP_JUMP_IF_TRUE | 33,800 | 40.6% |
| TO_BOOL_BOOL | 5,500 | 6.6% |
| TO_BOOL | 1,600 | 1.9% |
| TO_BOOL_INT | 660 | 0.8% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 560 | 50.0% |
| LOAD_ATTR_MODULE | 520 | 46.4% |
| LOAD_ATTR | 40 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,120 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 280 | 77.8% |
| LOAD_ATTR | 40 | 11.1% |
| LOAD_FAST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 160 | 44.4% |
| LOAD_CONST | 160 | 44.4% |
| CALL_BUILTIN_CLASS | 40 | 11.1% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 8,800 | 97.8% |
| TO_BOOL | 100 | 1.1% |
| TO_BOOL_INT | 80 | 0.9% |
| TO_BOOL_LIST | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,160 | 90.7% |
| COPY | 420 | 4.7% |
| RETURN_VALUE | 320 | 3.6% |
| STORE_FAST | 80 | 0.9% |
| CALL_PY_EXACT_ARGS | 20 | 0.2% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 126,960 | 56.2% |
| BINARY_OP | 21,040 | 9.3% |
| LOAD_FAST_LOAD_FAST | 16,380 | 7.3% |
| BINARY_SLICE | 16,240 | 7.2% |
| LOAD_GLOBAL_MODULE | 12,820 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,020 | 23.5% |
| LOAD_FAST | 49,180 | 21.8% |
| TO_BOOL_INT | 43,460 | 19.3% |
| BINARY_OP | 21,040 | 9.3% |
| BINARY_SLICE | 16,200 | 7.2% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 40.0% |
| STORE_FAST | 80 | 40.0% |
| DICT_UPDATE | 20 | 10.0% |
| LOAD_CONST | 20 | 10.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 23,260 | 58.1% |
| STORE_FAST | 5,060 | 12.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,680 | 6.7% |
| SWAP | 2,200 | 5.5% |
| LOAD_FAST | 1,280 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,280 | 65.7% |
| STORE_FAST | 6,500 | 16.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,640 | 6.6% |
| SWAP | 2,200 | 5.5% |
| BUILD_TUPLE | 320 | 0.8% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 32,640 | 45.7% |
| LOAD_CONST | 32,500 | 45.5% |
| LOAD_FAST | 2,220 | 3.1% |
| RESUME_CHECK | 1,280 | 1.8% |
| DICT_UPDATE | 720 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,640 | 94.6% |
| RETURN_VALUE | 800 | 1.1% |
| STORE_FAST | 760 | 1.1% |
| LOAD_GLOBAL_MODULE | 600 | 0.8% |
| EXTENDED_ARG | 580 | 0.8% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 360 | 64.3% |
| LOAD_GLOBAL_MODULE | 140 | 25.0% |
| LOAD_ATTR | 40 | 7.1% |
| LOAD_GLOBAL | 20 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 560 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,239 | 95.8% |
| BINARY_OP_ADD_INT | 1,340 | 4.0% |
| LOAD_CONST | 60 | 0.2% |
| BINARY_OP | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 33,599 | 99.8% |
| BINARY_SUBSCR | 60 | 0.2% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,300 | 84.4% |
| FORMAT_SIMPLE | 240 | 15.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,040 | 67.5% |
| STORE_FAST | 240 | 15.6% |
| LIST_APPEND | 160 | 10.4% |
| CALL | 100 | 6.5% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,340 | 68.8% |
| LOAD_GLOBAL_BUILTIN | 16,500 | 18.2% |
| LOAD_FAST_LOAD_FAST | 4,280 | 4.7% |
| LOAD_GLOBAL_MODULE | 2,060 | 2.3% |
| BINARY_OP | 960 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 32,640 | 36.0% |
| CALL | 17,440 | 19.3% |
| CALL_ISINSTANCE | 16,440 | 18.1% |
| RETURN_VALUE | 11,600 | 12.8% |
| LOAD_CONST | 3,620 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,620 | 20.2% |
| LOAD_ATTR_INSTANCE_VALUE | 50,560 | 14.1% |
| LOAD_FAST_LOAD_FAST | 46,540 | 12.9% |
| LOAD_ATTR | 35,240 | 9.8% |
| BINARY_SLICE | 32,319 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 137,740 | 38.3% |
| RETURN_VALUE | 37,740 | 10.5% |
| LOAD_CONST | 32,879 | 9.1% |
| LOAD_FAST | 29,160 | 8.1% |
| POP_TOP | 22,840 | 6.3% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 67,600 | 72.1% |
| CALL_INTRINSIC_1 | 23,920 | 25.5% |
| LOAD_FAST | 1,760 | 1.9% |
| BUILD_MAP | 160 | 0.2% |
| MAP_ADD | 160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 34,460 | 36.8% |
| RESUME_CHECK | 32,480 | 34.6% |
| POP_TOP | 24,800 | 26.5% |
| RETURN_GENERATOR | 640 | 0.7% |
| STORE_FAST | 580 | 0.6% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 24,500 | 98.7% |
| RERAISE | 320 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 23,920 | 96.4% |
| BUILD_MAP | 420 | 1.7% |
| RERAISE | 320 | 1.3% |
| LOAD_CONST | 160 | 0.6% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 99,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 67,260 | 67.7% |
| RETURN_GENERATOR | 17,200 | 17.3% |
| STORE_FAST | 10,040 | 10.1% |
| RETURN_VALUE | 3,200 | 3.2% |
| LOAD_FAST | 320 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40,680 | 68.4% |
| LOAD_FAST | 8,600 | 14.5% |
| LOAD_CONST | 5,280 | 8.9% |
| COMPARE_OP | 1,700 | 2.9% |
| LOAD_ATTR_MODULE | 900 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 54,680 | 92.0% |
| COMPARE_OP | 1,700 | 2.9% |
| COMPARE_OP_INT | 1,580 | 2.7% |
| POP_JUMP_IF_TRUE | 680 | 1.1% |
| COMPARE_OP_STR | 620 | 1.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,160 | 78.3% |
| LOAD_GLOBAL_MODULE | 26,320 | 10.1% |
| LOAD_ATTR_MODULE | 16,600 | 6.4% |
| LOAD_FAST_LOAD_FAST | 8,340 | 3.2% |
| BUILD_TUPLE | 2,340 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 194,960 | 74.8% |
| POP_JUMP_IF_FALSE | 65,300 | 25.0% |
| SWAP | 320 | 0.1% |
| STORE_FAST | 120 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 80 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 10,440 | 42.9% |
| CALL_LEN | 3,740 | 15.4% |
| LOAD_FAST | 3,200 | 13.2% |
| BINARY_OP | 3,040 | 12.5% |
| SWAP | 1,280 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 11,320 | 46.5% |
| TO_BOOL_INT | 6,840 | 28.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,280 | 9.4% |
| TO_BOOL | 820 | 3.4% |
| COMPARE_OP_INT | 800 | 3.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,340 | 70.4% |
| CALL_PY_EXACT_ARGS | 3,840 | 20.3% |
| LOAD_ATTR_PROPERTY | 800 | 4.2% |
| CALL | 680 | 3.6% |
| CALL_ALLOC_AND_ENTER_INIT | 200 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 17,720 | 93.6% |
| RESUME | 700 | 3.7% |
| RETURN_GENERATOR | 440 | 2.3% |
| MAKE_CELL | 80 | 0.4% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 66.7% |
| RETURN_CONST | 60 | 33.3% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 160 | 50.0% |
| LOAD_FAST | 160 | 50.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 66,320 | 98.1% |
| RETURN_VALUE | 800 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 340 | 0.5% |
| CALL | 80 | 0.1% |
| LOAD_ATTR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 67,600 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 740 | 97.4% |
| BUILD_CONST_KEY_MAP | 20 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 720 | 94.7% |
| EXTENDED_ARG | 20 | 2.6% |
| STORE_NAME | 20 | 2.6% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 9,480 | 36.2% |
| POP_JUMP_IF_NONE | 7,680 | 29.3% |
| LOAD_CONST | 5,420 | 20.7% |
| BUILD_MAP | 580 | 2.2% |
| POP_EXCEPT | 520 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,080 | 61.4% |
| JUMP_BACKWARD | 8,900 | 34.0% |
| FOR_ITER_LIST | 600 | 2.3% |
| POP_JUMP_IF_FALSE | 280 | 1.1% |
| POP_JUMP_IF_NONE | 160 | 0.6% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 204,580 | 81.6% |
| GET_ITER | 43,660 | 17.4% |
| FOR_ITER | 1,260 | 0.5% |
| LOAD_FAST | 920 | 0.4% |
| SWAP | 360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 204,540 | 81.5% |
| LOAD_FAST | 40,680 | 16.2% |
| RETURN_CONST | 1,540 | 0.6% |
| FOR_ITER | 1,260 | 0.5% |
| FOR_ITER_LIST | 840 | 0.3% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 130,160 | 86.0% |
| BEFORE_ASYNC_WITH | 9,120 | 6.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 8,960 | 5.9% |
| RETURN_VALUE | 1,040 | 0.7% |
| LOAD_FAST | 640 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 151,360 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 200 | 90.9% |
| STORE_NAME | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 180 | 81.8% |
| STORE_FAST | 40 | 18.2% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 500 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 220 | 44.0% |
| IMPORT_FROM | 200 | 40.0% |
| STORE_FAST | 80 | 16.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 353,720 | 84.5% |
| LOAD_FAST | 26,220 | 6.3% |
| LOAD_ATTR_MODULE | 15,960 | 3.8% |
| LOAD_ATTR | 12,120 | 2.9% |
| LOAD_FAST_LOAD_FAST | 8,080 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 416,300 | 99.5% |
| RETURN_VALUE | 1,600 | 0.4% |
| POP_JUMP_IF_TRUE | 580 | 0.1% |
| STORE_FAST | 80 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 160,120 | 52.4% |
| POP_TOP | 37,880 | 12.4% |
| POP_JUMP_IF_TRUE | 34,320 | 11.2% |
| CALL_LIST_APPEND | 17,400 | 5.7% |
| STORE_FAST | 16,780 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 204,580 | 67.0% |
| FOR_ITER_RANGE | 51,920 | 17.0% |
| FOR_ITER_LIST | 22,780 | 7.5% |
| LOAD_FAST | 12,960 | 4.2% |
| FOR_ITER_TUPLE | 11,400 | 3.7% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,560 | 87.7% |
| RESUME | 1,200 | 12.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 6,420 | 65.8% |
| SEND | 3,340 | 34.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,640 | 44.8% |
| STORE_FAST | 36,680 | 33.8% |
| POP_TOP | 17,381 | 16.0% |
| POP_JUMP_IF_FALSE | 4,660 | 4.3% |
| LOAD_FAST | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,161 | 53.6% |
| STORE_FAST | 24,400 | 22.5% |
| LOAD_DEREF | 8,240 | 7.6% |
| BINARY_OP | 8,000 | 7.4% |
| LOAD_GLOBAL_BUILTIN | 6,360 | 5.9% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 8,080 | 63.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,400 | 18.9% |
| CALL_BUILTIN_CLASS | 1,280 | 10.1% |
| RETURN_VALUE | 560 | 4.4% |
| BUILD_STRING | 160 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 12,700 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 23,260 | 94.0% |
| LOAD_FAST | 980 | 4.0% |
| BINARY_SLICE | 240 | 1.0% |
| LOAD_CONST | 240 | 1.0% |
| LOAD_ATTR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 24,500 | 99.0% |
| LOAD_FAST | 160 | 0.6% |
| LOAD_NAME | 60 | 0.2% |
| STORE_NAME | 20 | 0.1% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 548,020 | 76.0% |
| LOAD_ATTR_WITH_HINT | 34,180 | 4.7% |
| LOAD_GLOBAL_BUILTIN | 32,880 | 4.6% |
| LOAD_GLOBAL_MODULE | 30,920 | 4.3% |
| LOAD_ATTR_SLOT | 23,900 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,020 | 24.1% |
| TO_BOOL_BOOL | 145,740 | 20.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 54,880 | 7.6% |
| CALL_PY_EXACT_ARGS | 50,340 | 7.0% |
| LOAD_GLOBAL_MODULE | 49,480 | 6.9% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 261,080 | 22.2% |
| POP_JUMP_IF_FALSE | 151,720 | 12.9% |
| GET_AWAITABLE | 151,360 | 12.9% |
| PUSH_NULL | 90,960 | 7.7% |
| LOAD_CONST | 69,520 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 214,218 | 18.2% |
| SEND_GEN | 146,220 | 12.4% |
| COMPARE_OP_INT | 127,860 | 10.9% |
| BINARY_OP | 126,960 | 10.8% |
| CALL_KW | 99,320 | 8.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 17,520 | 19.8% |
| RESUME_CHECK | 10,220 | 11.6% |
| POP_JUMP_IF_FALSE | 9,440 | 10.7% |
| STORE_DEREF | 9,360 | 10.6% |
| LOAD_DEREF | 8,400 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,520 | 19.8% |
| POP_JUMP_IF_NONE | 9,120 | 10.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,640 | 9.8% |
| LOAD_DEREF | 8,400 | 9.5% |
| LOAD_ATTR_METHOD_NO_DICT | 8,200 | 9.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 786,740 | 15.6% |
| STORE_FAST | 728,700 | 14.5% |
| RESUME_CHECK | 469,240 | 9.3% |
| POP_JUMP_IF_TRUE | 451,520 | 9.0% |
| LOAD_GLOBAL_BUILTIN | 404,728 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 964,960 | 19.2% |
| LOAD_ATTR_INSTANCE_VALUE | 805,536 | 16.0% |
| LOAD_ATTR | 548,020 | 10.9% |
| LOAD_CONST | 261,080 | 5.2% |
| LOAD_ATTR_WITH_HINT | 226,920 | 4.5% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,200 | 93.2% |
| LOAD_FAST_AND_CLEAR | 160 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,200 | 93.2% |
| LOAD_FAST_AND_CLEAR | 160 | 6.8% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,120 | 48.3% |
| LOAD_ATTR_INSTANCE_VALUE | 8,060 | 47.9% |
| POP_TOP | 480 | 2.9% |
| JUMP_FORWARD | 80 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 16,080 | 95.6% |
| POP_JUMP_IF_NOT_NONE | 480 | 2.9% |
| CALL | 80 | 0.5% |
| SWAP | 80 | 0.5% |
| LOAD_FAST | 40 | 0.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 160,300 | 14.6% |
| CALL_BUILTIN_FAST | 159,980 | 14.6% |
| STORE_ATTR | 148,860 | 13.5% |
| STORE_ATTR_INSTANCE_VALUE | 103,160 | 9.4% |
| LOAD_FAST_LOAD_FAST | 87,320 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 320,060 | 29.1% |
| STORE_ATTR | 201,460 | 18.3% |
| STORE_ATTR_INSTANCE_VALUE | 106,080 | 9.7% |
| STORE_ATTR_SLOT | 98,480 | 9.0% |
| LOAD_FAST_LOAD_FAST | 87,320 | 7.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,720 | 11.7% |
| LOAD_FAST | 3,500 | 11.0% |
| STORE_FAST | 3,380 | 10.6% |
| RESUME_CHECK | 2,380 | 7.5% |
| RESUME | 2,320 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,420 | 35.8% |
| LOAD_ATTR | 4,880 | 15.3% |
| LOAD_GLOBAL_BUILTIN | 4,660 | 14.6% |
| LOAD_FAST | 4,480 | 14.0% |
| CALL | 1,320 | 4.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 320 | 21.9% |
| STORE_NAME | 300 | 20.5% |
| RESUME | 260 | 17.8% |
| LOAD_CONST | 200 | 13.7% |
| BINARY_OP | 80 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 38.4% |
| LOAD_ATTR | 440 | 30.1% |
| STORE_NAME | 260 | 17.8% |
| CALL | 80 | 5.5% |
| LOAD_NAME | 40 | 2.7% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,060 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 420 | 39.6% |
| LOAD_FAST | 180 | 17.0% |
| CALL | 160 | 15.1% |
| LOAD_FAST_LOAD_FAST | 100 | 9.4% |
| LOAD_SUPER_ATTR_ATTR | 100 | 9.4% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 20,800 | 66.4% |
| CALL_PY_EXACT_ARGS | 9,800 | 31.3% |
| CALL | 220 | 0.7% |
| CALL_FUNCTION_EX | 160 | 0.5% |
| CALL_KW | 160 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 20,800 | 66.4% |
| RETURN_GENERATOR | 8,640 | 27.6% |
| RESUME_CHECK | 1,720 | 5.5% |
| RESUME | 160 | 0.5% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,920 | 80.5% |
| LOAD_FAST | 2,880 | 18.0% |
| LOAD_ATTR_INSTANCE_VALUE | 180 | 1.1% |
| LOAD_ATTR | 60 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 9,480 | 59.1% |
| LOAD_CONST | 5,640 | 35.2% |
| DICT_UPDATE | 740 | 4.6% |
| CALL_FUNCTION_EX | 160 | 1.0% |
| BUILD_MAP | 20 | 0.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 511,380 | 34.1% |
| IS_OP | 416,300 | 27.7% |
| COMPARE_OP_INT | 248,128 | 16.5% |
| TO_BOOL_NONE | 75,100 | 5.0% |
| CONTAINS_OP | 65,300 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 786,740 | 52.4% |
| LOAD_GLOBAL_BUILTIN | 306,948 | 20.4% |
| LOAD_CONST | 151,720 | 10.1% |
| RETURN_CONST | 113,580 | 7.6% |
| LOAD_GLOBAL_MODULE | 83,000 | 5.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 57,120 | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE | 53,800 | 32.4% |
| LOAD_FAST | 44,320 | 26.7% |
| LOAD_DEREF | 9,120 | 5.5% |
| LOAD_ATTR | 800 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 93,240 | 56.2% |
| LOAD_GLOBAL_BUILTIN | 24,700 | 14.9% |
| LOAD_DEREF | 17,520 | 10.6% |
| LOAD_CONST | 10,900 | 6.6% |
| LOAD_FAST_LOAD_FAST | 8,640 | 5.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 118,140 | 90.0% |
| LOAD_ATTR_INSTANCE_VALUE | 10,080 | 7.7% |
| CALL_BUILTIN_FAST | 720 | 0.5% |
| LOAD_GLOBAL_MODULE | 620 | 0.5% |
| LOAD_FAST_CHECK | 480 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,280 | 42.1% |
| LOAD_FAST_LOAD_FAST | 30,160 | 23.0% |
| LOAD_GLOBAL_MODULE | 23,700 | 18.1% |
| LOAD_GLOBAL_BUILTIN | 8,780 | 6.7% |
| NOP | 8,760 | 6.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 329,800 | 56.8% |
| CONTAINS_OP | 194,960 | 33.6% |
| TO_BOOL | 33,800 | 5.8% |
| TO_BOOL_NONE | 8,340 | 1.4% |
| TO_BOOL_INT | 6,040 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 451,520 | 77.7% |
| LOAD_GLOBAL_MODULE | 42,100 | 7.2% |
| JUMP_BACKWARD | 34,320 | 5.9% |
| RETURN_CONST | 26,220 | 4.5% |
| NOP | 9,680 | 1.7% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 260 | 52.0% |
| POP_TOP | 160 | 32.0% |
| LOAD_CONST | 80 | 16.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 240 | 75.0% |
| PUSH_EXC_INFO | 80 | 25.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 400 | 45.5% |
| CALL_INTRINSIC_1 | 320 | 36.4% |
| POP_TOP | 160 | 18.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 320 | 57.1% |
| COPY | 160 | 28.6% |
| PUSH_EXC_INFO | 80 | 14.3% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 113,580 | 29.6% |
| POP_TOP | 109,560 | 28.5% |
| STORE_ATTR | 50,240 | 13.1% |
| STORE_ATTR_SLOT | 27,960 | 7.3% |
| STORE_FAST | 27,200 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 179,380 | 46.7% |
| INTERPRETER_EXIT | 106,280 | 27.7% |
| END_SEND | 68,080 | 17.7% |
| EXIT_INIT_CHECK | 19,040 | 5.0% |
| TO_BOOL_BOOL | 9,320 | 2.4% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,140 | 54.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 3,340 | 35.5% |
| SEND | 920 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 2,800 | 29.8% |
| END_SEND | 2,560 | 27.2% |
| POP_TOP | 1,560 | 16.6% |
| SEND_GEN | 1,560 | 16.6% |
| SEND | 920 | 9.8% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 3,400 | 99.4% |
| SET_FUNCTION_ATTRIBUTE | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,220 | 64.9% |
| STORE_DEREF | 640 | 18.7% |
| LOAD_FAST | 200 | 5.8% |
| STORE_NAME | 180 | 5.3% |
| LOAD_GLOBAL_MODULE | 160 | 4.7% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 201,460 | 89.3% |
| LOAD_FAST | 20,280 | 9.0% |
| STORE_ATTR | 3,160 | 1.4% |
| SWAP | 360 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 148,860 | 66.0% |
| RETURN_CONST | 50,240 | 22.3% |
| LOAD_DEREF | 8,080 | 3.6% |
| STORE_ATTR_INSTANCE_VALUE | 5,380 | 2.4% |
| LOAD_FAST | 3,580 | 1.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 16,120 | 74.2% |
| RETURN_VALUE | 1,760 | 8.1% |
| LOAD_CONST | 1,160 | 5.3% |
| SET_FUNCTION_ATTRIBUTE | 640 | 2.9% |
| BINARY_OP_SUBTRACT_INT | 460 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 9,360 | 43.1% |
| LOAD_FAST_LOAD_FAST | 8,080 | 37.2% |
| LOAD_FAST | 2,800 | 12.9% |
| LOAD_CONST | 880 | 4.1% |
| LOAD_GLOBAL_MODULE | 240 | 1.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 204,540 | 20.7% |
| CALL | 137,740 | 13.9% |
| RETURN_VALUE | 123,000 | 12.4% |
| LOAD_CONST | 83,760 | 8.5% |
| END_SEND | 69,920 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 728,700 | 73.7% |
| LOAD_FAST_LOAD_FAST | 44,120 | 4.5% |
| LOAD_GLOBAL_BUILTIN | 44,020 | 4.5% |
| LOAD_GLOBAL_MODULE | 41,000 | 4.1% |
| JUMP_FORWARD | 36,680 | 3.7% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 7,980 | 71.1% |
| FOR_ITER_TUPLE | 2,400 | 21.4% |
| FOR_ITER_LIST | 260 | 2.3% |
| FOR_ITER | 220 | 2.0% |
| COPY | 160 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 8,200 | 73.1% |
| TO_BOOL_STR | 2,400 | 21.4% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 1.6% |
| LOAD_ATTR_PROPERTY | 120 | 1.1% |
| STORE_ATTR | 80 | 0.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 24,820 | 83.7% |
| UNPACK_SEQUENCE_TUPLE | 1,380 | 4.7% |
| UNPACK_SEQUENCE_LIST | 1,140 | 3.8% |
| UNPACK_SEQUENCE | 900 | 3.0% |
| STORE_FAST_STORE_FAST | 400 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,480 | 79.2% |
| LOAD_GLOBAL_MODULE | 2,000 | 6.7% |
| STORE_FAST | 1,800 | 6.1% |
| NOP | 1,120 | 3.8% |
| LOAD_GLOBAL | 400 | 1.3% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 42.9% |
| CALL | 40 | 28.6% |
| LOAD_CONST | 20 | 14.3% |
| LOAD_FAST | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 28.6% |
| LOAD_GLOBAL_MODULE | 40 | 28.6% |
| LOAD_CONST | 20 | 14.3% |
| LOAD_FAST | 20 | 14.3% |
| LOAD_NAME | 20 | 14.3% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 1,120 | 37.1% |
| LOAD_CONST | 500 | 16.6% |
| CALL | 480 | 15.9% |
| LOAD_NAME | 260 | 8.6% |
| IMPORT_NAME | 220 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,620 | 53.6% |
| EXTENDED_ARG | 360 | 11.9% |
| LOAD_NAME | 300 | 9.9% |
| RETURN_CONST | 280 | 9.3% |
| LOAD_BUILD_CLASS | 220 | 7.3% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,200 | 15.8% |
| LOAD_FAST_AND_CLEAR | 2,200 | 15.8% |
| LOAD_FAST | 1,680 | 12.1% |
| LOAD_ATTR | 1,540 | 11.0% |
| BINARY_OP_ADD_INT | 1,340 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,480 | 25.0% |
| STORE_ATTR_INSTANCE_VALUE | 2,280 | 16.4% |
| BUILD_LIST | 2,200 | 15.8% |
| LOAD_CONST | 1,320 | 9.5% |
| COPY | 1,280 | 9.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 600 | 28.6% |
| CALL | 280 | 13.3% |
| END_SEND | 240 | 11.4% |
| LOAD_FAST | 200 | 9.5% |
| FOR_ITER_LIST | 200 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 900 | 42.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 620 | 29.5% |
| UNPACK_SEQUENCE_TUPLE | 300 | 14.3% |
| STORE_FAST | 120 | 5.7% |
| UNPACK_SEQUENCE_LIST | 60 | 2.9% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 7,280 | 56.1% |
| SEND | 2,800 | 21.6% |
| BUILD_STRING | 1,040 | 8.0% |
| RETURN_CONST | 720 | 5.5% |
| CALL | 320 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 7,280 | 56.1% |
| INTERPRETER_EXIT | 5,700 | 43.9% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 4,240 | 40.9% |
| CACHE | 2,380 | 23.0% |
| POP_TOP | 1,520 | 14.7% |
| SEND_GEN | 920 | 8.9% |
| COPY_FREE_VARS | 700 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,680 | 45.2% |
| LOAD_GLOBAL | 2,320 | 22.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,200 | 11.6% |
| NOP | 560 | 5.4% |
| LOAD_CONST | 520 | 5.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,720 | 99.5% |
| BINARY_OP | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,740 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 28,420 | 90.0% |
| LOAD_FAST_LOAD_FAST | 2,760 | 8.7% |
| BINARY_OP | 280 | 0.9% |
| LOAD_FAST | 120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 16,120 | 51.0% |
| BINARY_SLICE | 11,720 | 37.1% |
| BUILD_SLICE | 1,340 | 4.2% |
| SWAP | 1,340 | 4.2% |
| CALL_PY_EXACT_ARGS | 320 | 1.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,920 | 71.6% |
| LOAD_FAST | 240 | 9.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 6.0% |
| LOAD_CONST | 120 | 4.5% |
| LOAD_GLOBAL_MODULE | 120 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,100 | 41.0% |
| CALL | 960 | 35.8% |
| RETURN_VALUE | 300 | 11.2% |
| STORE_FAST | 160 | 6.0% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 4.5% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 90.9% |
| BINARY_OP | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 200 | 90.9% |
| CALL | 20 | 9.1% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 360 | 85.7% |
| LOAD_ATTR | 40 | 9.5% |
| BINARY_OP | 20 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 360 | 85.7% |
| LOAD_GLOBAL_BUILTIN | 40 | 9.5% |
| COMPARE_OP | 20 | 4.8% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 200 | 50.0% |
| BINARY_OP | 80 | 20.0% |
| LOAD_FAST | 80 | 20.0% |
| CALL | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 340 | 85.0% |
| RETURN_VALUE | 60 | 15.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,620 | 33.9% |
| LOAD_FAST_LOAD_FAST | 1,480 | 31.0% |
| LOAD_FAST | 1,440 | 30.1% |
| BINARY_OP | 200 | 4.2% |
| CALL_LEN | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,800 | 58.6% |
| SWAP | 1,120 | 23.4% |
| STORE_DEREF | 460 | 9.6% |
| STORE_FAST | 220 | 4.6% |
| RETURN_VALUE | 40 | 0.8% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,700 | 94.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 520 | 2.3% |
| LOAD_DEREF | 420 | 1.8% |
| LOAD_CONST | 160 | 0.7% |
| BINARY_SUBSCR | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,500 | 45.6% |
| LOAD_FAST | 10,160 | 44.1% |
| PUSH_EXC_INFO | 980 | 4.3% |
| STORE_FAST | 900 | 3.9% |
| PUSH_NULL | 420 | 1.8% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 360 | 35.3% |
| LOAD_FAST | 300 | 29.4% |
| BINARY_SUBSCR | 120 | 11.8% |
| BUILD_TUPLE | 120 | 11.8% |
| LOAD_CONST | 120 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,000 | 98.0% |
| PUSH_EXC_INFO | 20 | 2.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,680 | 95.7% |
| BINARY_SUBSCR | 240 | 3.4% |
| BINARY_OP_SUBTRACT_INT | 40 | 0.6% |
| LOAD_FAST | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 3,640 | 52.1% |
| STORE_FAST | 2,540 | 36.4% |
| RETURN_VALUE | 260 | 3.7% |
| BINARY_OP_ADD_UNICODE | 160 | 2.3% |
| LOAD_FAST | 120 | 1.7% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,000 | 70.4% |
| LOAD_CONST | 220 | 15.5% |
| LOAD_FAST | 140 | 9.9% |
| BINARY_SUBSCR | 40 | 2.8% |
| BINARY_SUBSCR_STR_INT | 20 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,020 | 71.8% |
| LOAD_CONST | 240 | 16.9% |
| STORE_FAST | 120 | 8.5% |
| PUSH_EXC_INFO | 20 | 1.4% |
| BINARY_SUBSCR_STR_INT | 20 | 1.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 920 | 90.2% |
| BINARY_SUBSCR | 100 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 58.8% |
| RETURN_VALUE | 260 | 25.5% |
| LOAD_GLOBAL_MODULE | 80 | 7.8% |
| LOAD_GLOBAL_BUILTIN | 60 | 5.9% |
| LOAD_GLOBAL | 20 | 2.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,920 | 46.8% |
| LOAD_ATTR | 8,120 | 42.6% |
| BINARY_OP | 760 | 4.0% |
| CALL | 500 | 2.6% |
| LOAD_FAST | 380 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,840 | 98.7% |
| COPY_FREE_VARS | 200 | 1.0% |
| STORE_FAST | 40 | 0.2% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,520 | 64.5% |
| LOAD_FAST | 9,080 | 17.5% |
| RETURN_VALUE | 8,120 | 15.6% |
| LOAD_ATTR_INSTANCE_VALUE | 520 | 1.0% |
| CALL | 300 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 32,320 | 62.2% |
| RESUME_CHECK | 10,020 | 19.3% |
| GET_AWAITABLE | 8,960 | 17.3% |
| POP_TOP | 480 | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 140 | 0.3% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,960 | 76.8% |
| LOAD_CONST | 1,400 | 8.3% |
| LOAD_GLOBAL_BUILTIN | 1,020 | 6.0% |
| CALL | 580 | 3.4% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 12,540 | 74.3% |
| LIST_APPEND | 1,280 | 7.6% |
| STORE_FAST | 1,140 | 6.8% |
| LOAD_GLOBAL_BUILTIN | 480 | 2.8% |
| STORE_FAST_STORE_FAST | 380 | 2.3% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 160,080 | 60.1% |
| LOAD_GLOBAL_MODULE | 63,920 | 24.0% |
| LOAD_FAST | 25,660 | 9.6% |
| LOAD_CONST | 13,560 | 5.1% |
| LOAD_FAST_LOAD_FAST | 1,880 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 159,980 | 60.1% |
| RETURN_VALUE | 33,800 | 12.7% |
| LOAD_ATTR_METHOD_NO_DICT | 31,960 | 12.0% |
| COPY | 10,440 | 3.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 8,120 | 3.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 32,240 | 90.8% |
| LOAD_FAST | 840 | 2.4% |
| PUSH_NULL | 760 | 2.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 620 | 1.7% |
| BUILD_LIST | 240 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 33,840 | 95.3% |
| RETURN_VALUE | 840 | 2.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 620 | 1.7% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.3% |
| BEFORE_WITH | 80 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,340 | 77.4% |
| LOAD_ATTR_INSTANCE_VALUE | 920 | 7.6% |
| RETURN_GENERATOR | 600 | 5.0% |
| CALL | 460 | 3.8% |
| LOAD_CONST | 240 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,300 | 68.8% |
| STORE_FAST | 1,020 | 8.5% |
| TO_BOOL_BOOL | 1,000 | 8.3% |
| POP_TOP | 500 | 4.1% |
| LOAD_CONST | 360 | 3.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 16,440 | 36.9% |
| LOAD_GLOBAL_BUILTIN | 13,880 | 31.1% |
| LOAD_GLOBAL_MODULE | 12,480 | 28.0% |
| LOAD_ATTR | 880 | 2.0% |
| CALL | 700 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 43,480 | 97.5% |
| TO_BOOL | 660 | 1.5% |
| RETURN_VALUE | 340 | 0.8% |
| STORE_FAST | 80 | 0.2% |
| LOAD_FAST | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 105,888 | 54.0% |
| LOAD_FAST | 72,720 | 37.1% |
| LOAD_ATTR_WITH_HINT | 16,400 | 8.4% |
| CALL | 740 | 0.4% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,248 | 47.1% |
| LOAD_CONST | 59,240 | 30.2% |
| STORE_FAST | 19,880 | 10.1% |
| LOAD_GLOBAL_MODULE | 17,480 | 8.9% |
| COPY | 3,740 | 1.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,220 | 81.9% |
| BUILD_TUPLE | 3,400 | 14.5% |
| CALL | 360 | 1.5% |
| LOAD_CONST | 160 | 0.7% |
| CALL_KW | 120 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,400 | 74.1% |
| LOAD_FAST | 2,600 | 11.1% |
| RETURN_CONST | 2,200 | 9.4% |
| LOAD_GLOBAL_MODULE | 640 | 2.7% |
| NOP | 300 | 1.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,880 | 22.0% |
| BUILD_LIST | 2,640 | 20.2% |
| LOAD_ATTR_METHOD_NO_DICT | 2,360 | 18.0% |
| LOAD_CONST | 1,540 | 11.8% |
| LOAD_FAST_LOAD_FAST | 1,240 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,660 | 28.0% |
| RETURN_VALUE | 3,300 | 25.2% |
| LIST_APPEND | 2,400 | 18.3% |
| LOAD_ATTR_METHOD_NO_DICT | 2,040 | 15.6% |
| BUILD_TUPLE | 840 | 6.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 16,120 | 62.0% |
| LOAD_CONST | 3,820 | 14.7% |
| LOAD_FAST_LOAD_FAST | 3,720 | 14.3% |
| LOAD_ATTR | 640 | 2.5% |
| LOAD_FAST | 640 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 16,420 | 63.1% |
| STORE_FAST | 6,440 | 24.8% |
| POP_TOP | 1,580 | 6.1% |
| UNPACK_SEQUENCE_LIST | 1,080 | 4.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 120 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 69,561 | 48.8% |
| LOAD_ATTR | 54,880 | 38.5% |
| LOAD_ATTR_METHOD_LAZY_DICT | 8,120 | 5.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,040 | 5.6% |
| CALL | 1,480 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 53,820 | 37.7% |
| STORE_FAST | 39,640 | 27.8% |
| GET_ITER | 32,600 | 22.9% |
| RETURN_VALUE | 8,520 | 6.0% |
| BUILD_LIST | 2,680 | 1.9% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,340 | 72.5% |
| CALL | 9,780 | 12.4% |
| CALL_BUILTIN_FAST | 8,080 | 10.2% |
| LOAD_CONST | 1,980 | 2.5% |
| STORE_FAST | 1,120 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 75,380 | 95.4% |
| RETURN_VALUE | 1,420 | 1.8% |
| UNPACK_SEQUENCE_TUPLE | 1,080 | 1.4% |
| LOAD_CONST | 840 | 1.1% |
| STORE_FAST | 160 | 0.2% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 169,880 | 36.6% |
| LOAD_FAST | 141,900 | 30.5% |
| LOAD_ATTR | 50,340 | 10.8% |
| LOAD_ATTR_METHOD_NO_DICT | 25,160 | 5.4% |
| LOAD_FAST_LOAD_FAST | 22,760 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 378,260 | 81.4% |
| RETURN_GENERATOR | 72,520 | 15.6% |
| MAKE_CELL | 9,800 | 2.1% |
| COPY_FREE_VARS | 3,840 | 0.8% |
| TO_BOOL_BOOL | 160 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,420 | 39.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 560 | 15.4% |
| CALL | 480 | 13.2% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 12.1% |
| RETURN_VALUE | 200 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,180 | 87.4% |
| RETURN_GENERATOR | 460 | 12.6% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 620 | 86.1% |
| CALL | 100 | 13.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 400 | 55.6% |
| BUILD_TUPLE | 120 | 16.7% |
| BINARY_OP_INPLACE_ADD_UNICODE | 80 | 11.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 80 | 11.1% |
| BINARY_OP | 40 | 5.6% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 440 | 48.9% |
| LOAD_FAST | 240 | 26.7% |
| LOAD_GLOBAL_MODULE | 160 | 17.8% |
| CALL | 40 | 4.4% |
| RETURN_VALUE | 20 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 360 | 40.0% |
| LOAD_FAST | 220 | 24.4% |
| CALL | 160 | 17.8% |
| RETURN_VALUE | 140 | 15.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 2.2% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,300 | 99.7% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |
| CALL | 60 | 0.1% |
| LOAD_CONST | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 41,200 | 69.3% |
| LOAD_FAST | 17,960 | 30.2% |
| PUSH_NULL | 80 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.1% |
| LOAD_FAST_LOAD_FAST | 40 | 0.1% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,520 | 44.2% |
| LOAD_ATTR_SLOT | 2,120 | 37.2% |
| RETURN_VALUE | 760 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 240 | 4.2% |
| COMPARE_OP | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,560 | 62.5% |
| RETURN_VALUE | 2,140 | 37.5% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 127,860 | 51.0% |
| LOAD_FAST | 67,880 | 27.1% |
| LOAD_ATTR_INSTANCE_VALUE | 20,328 | 8.1% |
| LOAD_ATTR_WITH_HINT | 8,160 | 3.3% |
| LOAD_FAST_LOAD_FAST | 8,140 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 248,128 | 98.9% |
| POP_JUMP_IF_TRUE | 2,420 | 1.0% |
| RETURN_VALUE | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| COPY | 60 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,340 | 62.3% |
| LOAD_GLOBAL_MODULE | 760 | 14.2% |
| COMPARE_OP | 620 | 11.6% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 8.2% |
| LOAD_FAST | 160 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,620 | 86.2% |
| POP_JUMP_IF_TRUE | 420 | 7.8% |
| STORE_FAST | 120 | 2.2% |
| YIELD_VALUE | 120 | 2.2% |
| COPY | 60 | 1.1% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,780 | 53.0% |
| GET_ITER | 17,460 | 40.6% |
| FOR_ITER | 840 | 2.0% |
| LOAD_FAST | 720 | 1.7% |
| SWAP | 620 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,940 | 44.0% |
| LOAD_GLOBAL_MODULE | 8,160 | 19.0% |
| RETURN_CONST | 4,980 | 11.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,640 | 10.8% |
| LOAD_FAST | 4,520 | 10.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 51,920 | 92.3% |
| GET_ITER | 4,100 | 7.3% |
| FOR_ITER | 120 | 0.2% |
| SWAP | 100 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 44,240 | 78.7% |
| STORE_FAST_LOAD_FAST | 7,980 | 14.2% |
| LOAD_CONST | 3,760 | 6.7% |
| SWAP | 120 | 0.2% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 11,400 | 79.9% |
| GET_ITER | 1,200 | 8.4% |
| SWAP | 1,120 | 7.9% |
| LOAD_FAST | 400 | 2.8% |
| FOR_ITER | 140 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,120 | 64.0% |
| STORE_FAST_LOAD_FAST | 2,400 | 16.8% |
| SWAP | 1,120 | 7.9% |
| LOAD_FAST | 680 | 4.8% |
| RETURN_CONST | 440 | 3.1% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 77.8% |
| LOAD_ATTR | 80 | 11.1% |
| LOAD_ATTR_MODULE | 80 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 460 | 63.9% |
| STORE_FAST | 140 | 19.4% |
| CALL | 60 | 8.3% |
| COMPARE_OP | 60 | 8.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 805,536 | 97.0% |
| LOAD_FAST_LOAD_FAST | 12,540 | 1.5% |
| LOAD_ATTR | 7,800 | 0.9% |
| COPY | 2,280 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,340 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 178,540 | 21.5% |
| CALL_LEN | 105,888 | 12.7% |
| LOAD_ATTR_METHOD_NO_DICT | 100,881 | 12.1% |
| RETURN_VALUE | 58,120 | 7.0% |
| LOAD_GLOBAL_MODULE | 54,080 | 6.5% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,360 | 99.7% |
| LOAD_ATTR | 100 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,200 | 49.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,120 | 25.0% |
| LOAD_GLOBAL_MODULE | 8,080 | 24.9% |
| LOAD_GLOBAL | 40 | 0.1% |
| CALL | 20 | 0.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 100,881 | 36.5% |
| LOAD_FAST | 75,100 | 27.2% |
| CALL_BUILTIN_FAST | 31,960 | 11.6% |
| BINARY_OP | 16,120 | 5.8% |
| LOAD_ATTR_WITH_HINT | 16,040 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,060 | 34.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 69,561 | 25.2% |
| LOAD_GLOBAL_MODULE | 28,300 | 10.2% |
| CALL_PY_EXACT_ARGS | 25,160 | 9.1% |
| LOAD_FAST_LOAD_FAST | 19,820 | 7.2% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 182,720 | 67.2% |
| LOAD_ATTR_SLOT | 27,240 | 10.0% |
| LOAD_ATTR_WITH_HINT | 18,440 | 6.8% |
| LOAD_ATTR_INSTANCE_VALUE | 10,220 | 3.8% |
| RETURN_VALUE | 9,520 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 169,880 | 62.5% |
| LOAD_FAST | 55,440 | 20.4% |
| LOAD_FAST_LOAD_FAST | 32,700 | 12.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,040 | 3.0% |
| CALL | 2,660 | 1.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 275,620 | 98.4% |
| LOAD_ATTR | 4,220 | 1.5% |
| LOAD_FAST | 280 | 0.1% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 174,320 | 62.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 32,240 | 11.5% |
| CONTAINS_OP | 16,600 | 5.9% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 16,120 | 5.8% |
| IS_OP | 15,960 | 5.7% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,180 | 88.1% |
| LOAD_ATTR | 140 | 10.4% |
| LOAD_FAST_LOAD_FAST | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 47.8% |
| CALL | 560 | 41.8% |
| BINARY_OP | 60 | 4.5% |
| CALL_BUILTIN_CLASS | 40 | 3.0% |
| CALL_ISINSTANCE | 20 | 1.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,340 | 90.2% |
| LOAD_ATTR | 680 | 5.9% |
| LOAD_ATTR_SLOT | 200 | 1.7% |
| STORE_FAST_LOAD_FAST | 120 | 1.0% |
| RETURN_VALUE | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,660 | 93.0% |
| COPY_FREE_VARS | 800 | 7.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 964,960 | 74.2% |
| LOAD_FAST_LOAD_FAST | 320,060 | 24.6% |
| LOAD_ATTR_INSTANCE_VALUE | 7,960 | 0.6% |
| BINARY_SUBSCR_LIST_INT | 3,640 | 0.3% |
| LOAD_ATTR_MODULE | 1,560 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 351,920 | 27.1% |
| TO_BOOL_BOOL | 223,840 | 17.2% |
| LOAD_FAST | 198,820 | 15.3% |
| CALL_BUILTIN_FAST | 160,080 | 12.3% |
| STORE_SUBSCR_DICT | 159,960 | 12.3% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 226,920 | 98.8% |
| LOAD_ATTR | 2,340 | 1.0% |
| LOAD_FAST_LOAD_FAST | 320 | 0.1% |
| LOAD_ATTR_WITH_HINT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 57,120 | 24.9% |
| LOAD_ATTR | 34,180 | 14.9% |
| TO_BOOL_BOOL | 24,920 | 10.9% |
| LOAD_CONST | 24,540 | 10.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 18,440 | 8.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 306,948 | 41.1% |
| RESUME_CHECK | 150,320 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 105,119 | 14.1% |
| LOAD_FAST | 48,560 | 6.5% |
| STORE_FAST | 44,020 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 404,728 | 54.2% |
| LOAD_FAST_LOAD_FAST | 160,300 | 21.4% |
| LOAD_GLOBAL_BUILTIN | 105,119 | 14.1% |
| LOAD_ATTR | 32,880 | 4.4% |
| BUILD_TUPLE | 16,500 | 2.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 351,920 | 33.2% |
| RESUME_CHECK | 139,100 | 13.1% |
| LOAD_FAST | 110,040 | 10.4% |
| POP_JUMP_IF_FALSE | 83,000 | 7.8% |
| LOAD_ATTR_INSTANCE_VALUE | 54,080 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 353,720 | 33.4% |
| LOAD_ATTR_MODULE | 275,620 | 26.0% |
| LOAD_FAST | 138,480 | 13.1% |
| CALL_BUILTIN_FAST | 63,920 | 6.0% |
| LOAD_FAST_LOAD_FAST | 43,620 | 4.1% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 92.5% |
| LOAD_SUPER_ATTR | 100 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 880 | 65.7% |
| PUSH_NULL | 420 | 31.3% |
| LOAD_GLOBAL | 40 | 3.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,020 | 92.3% |
| LOAD_SUPER_ATTR | 420 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,560 | 47.1% |
| LOAD_FAST | 1,500 | 27.6% |
| CALL_PY_EXACT_ARGS | 1,240 | 22.8% |
| CALL | 140 | 2.6% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 378,260 | 42.6% |
| CACHE | 164,620 | 18.5% |
| POP_TOP | 158,280 | 17.8% |
| CALL_KW | 67,260 | 7.6% |
| CALL_FUNCTION_EX | 32,480 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 469,240 | 52.8% |
| LOAD_GLOBAL_BUILTIN | 150,320 | 16.9% |
| LOAD_GLOBAL_MODULE | 139,100 | 15.6% |
| LOAD_FAST_LOAD_FAST | 51,140 | 5.8% |
| NOP | 48,040 | 5.4% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 146,220 | 94.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,420 | 4.2% |
| SEND | 1,560 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 147,080 | 95.4% |
| RESUME_CHECK | 6,200 | 4.0% |
| RESUME | 920 | 0.6% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 106,080 | 70.9% |
| LOAD_FAST | 35,940 | 24.0% |
| STORE_ATTR | 5,380 | 3.6% |
| SWAP | 2,280 | 1.5% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 103,160 | 68.9% |
| LOAD_FAST | 17,340 | 11.6% |
| RETURN_CONST | 16,100 | 10.8% |
| LOAD_CONST | 6,780 | 4.5% |
| LOAD_GLOBAL_MODULE | 2,620 | 1.8% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 98,480 | 54.6% |
| LOAD_FAST | 81,200 | 45.0% |
| STORE_ATTR | 700 | 0.4% |
| STORE_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,420 | 40.1% |
| LOAD_CONST | 50,840 | 28.2% |
| LOAD_FAST | 28,940 | 16.0% |
| RETURN_CONST | 27,960 | 15.5% |
| BUILD_LIST | 300 | 0.2% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,800 | 68.7% |
| LOAD_FAST_LOAD_FAST | 400 | 15.3% |
| STORE_ATTR | 340 | 13.0% |
| STORE_FAST_LOAD_FAST | 80 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,460 | 55.7% |
| NOP | 580 | 22.1% |
| EXTENDED_ARG | 300 | 11.5% |
| LOAD_GLOBAL_BUILTIN | 200 | 7.6% |
| LOAD_GLOBAL | 40 | 1.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 159,960 | 94.0% |
| LOAD_FAST | 8,720 | 5.1% |
| LOAD_ATTR | 520 | 0.3% |
| STORE_SUBSCR | 280 | 0.2% |
| LOAD_CONST | 280 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 160,120 | 94.1% |
| LOAD_FAST | 8,940 | 5.3% |
| NOP | 280 | 0.2% |
| LOAD_GLOBAL_MODULE | 280 | 0.2% |
| LOAD_CONST | 260 | 0.2% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 20 | 50.0% |
| RETURN_CONST | 20 | 50.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,040 | 82.9% |
| LOAD_FAST | 320 | 13.0% |
| TO_BOOL | 100 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,100 | 85.4% |
| POP_JUMP_IF_FALSE | 360 | 14.6% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 223,840 | 26.3% |
| LOAD_ATTR_INSTANCE_VALUE | 178,540 | 21.0% |
| LOAD_ATTR | 145,740 | 17.1% |
| RETURN_VALUE | 79,680 | 9.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 53,820 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 511,380 | 60.2% |
| POP_JUMP_IF_TRUE | 329,800 | 38.8% |
| UNARY_NOT | 8,800 | 1.0% |
| EXTENDED_ARG | 100 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 43,460 | 70.4% |
| LOAD_ATTR_INSTANCE_VALUE | 8,920 | 14.4% |
| COPY | 6,840 | 11.1% |
| LOAD_FAST | 1,580 | 2.6% |
| TO_BOOL | 660 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 55,620 | 90.1% |
| POP_JUMP_IF_TRUE | 6,040 | 9.8% |
| UNARY_NOT | 80 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 18,280 | 92.9% |
| LOAD_FAST | 1,060 | 5.4% |
| TO_BOOL | 340 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 19,000 | 96.5% |
| POP_JUMP_IF_TRUE | 660 | 3.4% |
| UNARY_NOT | 20 | 0.1% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 46,640 | 55.9% |
| LOAD_FAST | 19,040 | 22.8% |
| LOAD_ATTR | 8,920 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 8,240 | 9.9% |
| TO_BOOL | 440 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 75,100 | 90.0% |
| POP_JUMP_IF_TRUE | 8,340 | 10.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,400 | 49.6% |
| LOAD_FAST | 1,760 | 36.4% |
| COPY | 360 | 7.4% |
| TO_BOOL | 240 | 5.0% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,700 | 76.4% |
| POP_JUMP_IF_TRUE | 1,140 | 23.6% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,080 | 94.7% |
| UNPACK_SEQUENCE | 60 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,140 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 8,080 | 80.5% |
| CALL_METHOD_DESCRIPTOR_O | 1,080 | 10.8% |
| LOAD_FAST | 360 | 3.6% |
| UNPACK_SEQUENCE | 300 | 3.0% |
| RETURN_VALUE | 140 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,380 | 83.5% |
| STORE_FAST_STORE_FAST | 1,380 | 13.7% |
| POP_TOP | 280 | 2.8% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 9,640 | 38.4% |
| CALL_BUILTIN_FAST | 8,120 | 32.3% |
| FOR_ITER_LIST | 4,640 | 18.5% |
| STORE_FAST | 1,400 | 5.6% |
| UNPACK_SEQUENCE | 620 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 24,820 | 98.8% |
| STORE_FAST_LOAD_FAST | 140 | 0.6% |
| STORE_FAST | 100 | 0.4% |
| LOAD_FAST | 60 | 0.2% |


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
|     deferred | 220,320 | 81.7% |
|          hit | 43,940 | 16.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 14.0% |
| Failure | 4,680 | 86.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 1,860 | 39.7% |
| or | 1,060 | 22.6% |
| add other | 580 | 12.4% |
| floor divide | 280 | 6.0% |
| remainder | 280 | 6.0% |
| multiply different types | 220 | 4.7% |
| add different types | 160 | 3.4% |
| xor | 160 | 3.4% |
| lshift | 80 | 1.7% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> specialization stats for BINARY_OP_INPLACE_ADD_UNICODE family </summary>


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
|     deferred | 1,680 | 4.7% |
|          hit | 33,320 | 92.6% |
|         miss | 180 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 560 | 70.0% |
| Failure | 240 | 30.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 160 | 66.7% |
| code complex parameters | 60 | 25.0% |
| out of range | 20 | 8.3% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 330,539 | 17.8% |
|          hit | 1,443,409 | 77.7% |
|         miss | 54,840 | 3.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,820 | 61.1% |
| Failure | 11,360 | 38.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 2,340 | 20.6% |
| code complex parameters | 1,880 | 16.5% |
| class no vectorcall | 1,380 | 12.1% |
| cfunc noargs | 1,260 | 11.1% |
| meth descr varargs | 1,020 | 9.0% |
| class mutable | 1,020 | 9.0% |
| no dict | 580 | 5.1% |
| cfunc varargs keywords | 400 | 3.5% |
| cfunc varargs | 360 | 3.2% |
| other | 320 | 2.8% |
| meth descr varargs keywords | 320 | 2.8% |
| operator wrapper | 220 | 1.9% |
| wrong number arguments | 120 | 1.1% |
| cmethod | 80 | 0.7% |
| init not simple | 60 | 0.5% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 55,500 | 17.3% |
|          hit | 261,408 | 81.4% |
|         miss | 460 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,260 | 57.1% |
| Failure | 1,700 | 42.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,000 | 58.8% |
| bool | 180 | 10.6% |
| bytes | 160 | 9.4% |
| different types | 140 | 8.2% |
| float long | 140 | 8.2% |
| big int | 80 | 4.7% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 248,500 | 68.2% |
|          hit | 113,520 | 31.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,100 | 46.6% |
| Failure | 1,260 | 53.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 480 | 38.1% |
| dict values | 280 | 22.2% |
| reversed list | 160 | 12.7% |
| dict items | 140 | 11.1% |
| bytes | 60 | 4.8% |
| itertools | 40 | 3.2% |
| enumerate | 40 | 3.2% |
| ascii string | 40 | 3.2% |
| other | 20 | 1.6% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 677,940 | 17.1% |
|        deopt | 80 | 0.0% |
|          hit | 3,220,117 | 81.4% |
|         miss | 14,280 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 25,900 | 59.5% |
| Failure | 17,660 | 40.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 6,160 | 34.9% |
| not managed dict | 3,120 | 17.7% |
| shadowed | 3,080 | 17.4% |
| method | 1,780 | 10.1% |
| metaclass attribute | 1,740 | 9.9% |
| module attr not found | 400 | 2.3% |
| builtin class method | 400 | 2.3% |
| class attr descriptor | 320 | 1.8% |
| non object slot | 280 | 1.6% |
| class method obj | 220 | 1.2% |
| mutable class | 80 | 0.5% |
| class attr simple | 80 | 0.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,940 | 0.9% |
|        deopt | 160 | 0.0% |
|          hit | 1,802,967 | 98.1% |
|         miss | 3,220 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,120 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 540 | 6.9% |
|          hit | 6,780 | 86.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 520 | 100.0% |
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
|     deferred | 6,920 | 4.2% |
|          hit | 154,200 | 94.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,560 | 62.9% |
| Failure | 920 | 37.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 920 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 216,120 | 38.7% |
|          hit | 322,900 | 57.8% |
|         miss | 9,880 | 1.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,420 | 67.0% |
| Failure | 3,160 | 33.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 960 | 30.4% |
| not in keys | 880 | 27.8% |
| not in dict | 740 | 23.4% |
| overriding descriptor | 200 | 6.3% |
| method | 120 | 3.8% |
| not managed dict | 120 | 3.8% |
| overridden | 80 | 2.5% |
| no dict | 60 | 1.9% |


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,020 | 7.1% |
|          hit | 170,240 | 92.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 40.0% |
| Failure | 420 | 60.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 400 | 95.2% |
| bytearray int | 20 | 4.8% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 74,460 | 6.7% |
|          hit | 1,021,960 | 92.4% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,280 | 82.0% |
| Failure | 1,600 | 18.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 460 | 28.7% |
| sequence | 400 | 25.0% |
| set | 240 | 15.0% |
| dict | 180 | 11.2% |
| memory view | 140 | 8.8% |
| mapping | 80 | 5.0% |
| tuple | 80 | 5.0% |
| float | 20 | 1.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,100 | 2.9% |
|          hit | 36,300 | 94.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 980 | 98.0% |
| Failure | 20 | 2.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 20 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 13,034,712 | 48.2% |
| Not specialized | 4,448,226 | 16.4% |
| Specialized hits | 9,477,520 | 35.0% |
| Specialized misses | 83,161 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 677,940 | 36.4% |
| CALL | 330,539 | 17.7% |
| FOR_ITER | 248,500 | 13.3% |
| BINARY_OP | 220,320 | 11.8% |
| STORE_ATTR | 216,120 | 11.6% |
| TO_BOOL | 74,460 | 4.0% |
| COMPARE_OP | 55,500 | 3.0% |
| LOAD_GLOBAL | 15,940 | 0.9% |
| STORE_SUBSCR | 13,020 | 0.7% |
| SEND | 6,920 | 0.4% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,280 | 40.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,940 | 11.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 9,860 | 11.9% |
| STORE_ATTR_SLOT | 8,420 | 10.1% |
| LOAD_ATTR_WITH_HINT | 7,280 | 8.8% |
| LOAD_ATTR_SLOT | 4,940 | 5.9% |
| LOAD_GLOBAL_BUILTIN | 2,620 | 3.1% |
| STORE_ATTR_INSTANCE_VALUE | 1,160 | 1.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,060 | 1.3% |
| CALL_METHOD_DESCRIPTOR_O | 820 | 1.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 210,240 | 19.8% |
| Calls to Python functions inlined | 849,200 | 80.2% |
| Calls via PyEval_EvalFrame (total) | 210,240 | 19.8% |
| Calls via PyEval_EvalFrame (vector) | 193,380 | 18.3% |
| Calls via PyEval_EvalFrame (generator) | 16,860 | 1.6% |
| Calls via PyEval_EvalFrame (legacy) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 193,040 | 18.2% |
| Calls via PyEval_EvalFrame (build class) | 260 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 5,600 | 0.5% |
| Calls via PyEval_EvalFrame (function ex) | 33,440 | 3.2% |
| Calls via PyEval_EvalFrame (api) | 10,000 | 0.9% |
| Calls via PyEval_EvalFrame (method) | 42,400 | 4.0% |
| Frame objects created | 4,220 | 0.4% |
| Frames pushed | 560,220 | 52.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 776,419 | 32.7% |
| Frees to freelist | 780,579 |  |
| Allocations | 1,598,016 | 67.3% |
| Allocations to 512 bytes | 1,408,010 | 59.3% |
| Allocations to 4 kbytes | 132,208 | 5.6% |
| Allocations over 4 kbytes | 57,798 | 2.4% |
| Frees | 1,537,540 |  |
| New values | 34,780 |  |
| Interpreter increfs | 12,202,839 | 76.6% |
| Interpreter decrefs | 14,018,044 | 78.1% |
| Increfs | 3,731,909 | 23.4% |
| Decrefs | 3,920,573 | 21.9% |
| Materialize dict (on request) | 20 | 0.1% |
| Materialize dict (new key) | 160 | 0.5% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 20 | 0.1% |
| Method cache hits | 1,223,543 |  |
| Method cache misses | 37,437 |  |
| Method cache collisions | 40,847 |  |
| Method cache dunder hits | 357,450 |  |
| Method cache dunder misses | 6,450 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 100 | 540 | 743,956 |
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

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
