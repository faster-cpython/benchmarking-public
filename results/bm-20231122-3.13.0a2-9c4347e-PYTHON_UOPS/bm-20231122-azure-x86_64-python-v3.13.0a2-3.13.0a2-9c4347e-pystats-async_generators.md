
# Pystats results

- benchmark: async_generators
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 287,397,060 | 11.6% | 11.6% |  |
| LOAD_CONST | 182,260,180 | 7.3% | 18.9% |  |
| RESUME_CHECK | 181,859,100 | 7.3% | 26.2% | 0.0% |
| STORE_FAST | 158,024,920 | 6.4% | 32.6% |  |
| POP_TOP | 157,784,620 | 6.3% | 38.9% |  |
| INTERPRETER_EXIT | 157,616,100 | 6.3% | 45.3% |  |
| JUMP_BACKWARD | 133,700,660 | 5.4% | 50.7% |  |
| SEND | 133,548,900 | 5.4% | 56.0% |  |
| GET_ANEXT | 133,515,680 | 5.4% | 61.4% |  |
| YIELD_VALUE | 125,521,580 | 5.1% | 66.5% |  |
| CALL_INTRINSIC_1 | 125,521,280 | 5.1% | 71.5% |  |
| END_SEND | 125,515,760 | 5.1% | 76.6% |  |
| LOAD_ATTR_INSTANCE_VALUE | 88,279,260 | 3.6% | 80.1% | 0.0% |
| POP_JUMP_IF_FALSE | 56,463,520 | 2.3% | 82.4% |  |
| LOAD_FAST_LOAD_FAST | 48,273,100 | 1.9% | 84.3% |  |
| RETURN_CONST | 48,159,420 | 1.9% | 86.3% |  |
| LOAD_GLOBAL_MODULE | 32,424,420 | 1.3% | 87.6% | 0.2% |
| CALL_PY_EXACT_ARGS | 24,149,020 | 1.0% | 88.5% | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 24,141,680 | 1.0% | 89.5% | 0.1% |
| LOAD_GLOBAL_BUILTIN | 16,276,960 | 0.7% | 90.2% | 0.3% |
| CALL | 16,209,000 | 0.7% | 90.8% |  |
| RETURN_VALUE | 16,193,940 | 0.7% | 91.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 16,143,540 | 0.6% | 92.1% |  |
| CALL_LEN | 16,064,500 | 0.6% | 92.8% |  |
| COMPARE_OP_INT | 16,057,880 | 0.6% | 93.4% | 0.0% |
| BINARY_SLICE | 16,034,140 | 0.6% | 94.1% |  |
| CALL_METHOD_DESCRIPTOR_O | 16,033,860 | 0.6% | 94.7% | 0.0% |
| TO_BOOL_BOOL | 8,227,660 | 0.3% | 95.0% | 0.0% |
| PUSH_NULL | 8,156,620 | 0.3% | 95.4% |  |
| TO_BOOL_NONE | 8,083,940 | 0.3% | 95.7% | 45.2% |
| TO_BOOL_ALWAYS_TRUE | 8,069,900 | 0.3% | 96.0% | 45.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,060,500 | 0.3% | 96.3% | 0.0% |
| BINARY_OP_ADD_INT | 8,044,060 | 0.3% | 96.7% |  |
| BINARY_OP | 8,042,140 | 0.3% | 97.0% |  |
| POP_JUMP_IF_NONE | 8,034,180 | 0.3% | 97.3% |  |
| TO_BOOL | 8,015,860 | 0.3% | 97.6% |  |
| BINARY_SUBSCR | 8,013,020 | 0.3% | 98.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,660 | 0.3% | 98.3% | 0.0% |
| EXIT_INIT_CHECK | 8,009,560 | 0.3% | 98.6% |  |
| TO_BOOL_LIST | 8,009,540 | 0.3% | 98.9% | 0.0% |
| RETURN_GENERATOR | 8,003,940 | 0.3% | 99.2% |  |
| END_ASYNC_FOR | 8,000,000 | 0.3% | 99.6% |  |
| GET_AITER | 8,000,000 | 0.3% | 99.9% |  |
| POP_JUMP_IF_TRUE | 140,020 | 0.0% | 99.9% |  |
| LOAD_ATTR_MODULE | 123,720 | 0.0% | 99.9% | 7.5% |
| LOAD_ATTR | 116,420 | 0.0% | 99.9% |  |
| NOP | 116,160 | 0.0% | 99.9% |  |
| CONTAINS_OP | 98,080 | 0.0% | 99.9% |  |
| STORE_NAME | 90,100 | 0.0% | 99.9% |  |
| LOAD_NAME | 89,340 | 0.0% | 99.9% |  |
| POP_JUMP_IF_NOT_NONE | 81,620 | 0.0% | 99.9% |  |
| COMPARE_OP_STR | 80,540 | 0.0% | 99.9% | 0.3% |
| COPY | 76,400 | 0.0% | 99.9% |  |
| FOR_ITER | 71,000 | 0.0% | 99.9% |  |
| FOR_ITER_TUPLE | 64,640 | 0.0% | 99.9% |  |
| EXTENDED_ARG | 60,380 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 59,980 | 0.0% | 99.9% |  |
| CALL_BUILTIN_FAST | 59,680 | 0.0% | 99.9% | 1.2% |
| IS_OP | 56,580 | 0.0% | 99.9% |  |
| SWAP | 55,200 | 0.0% | 99.9% |  |
| LOAD_DEREF | 54,300 | 0.0% | 99.9% |  |
| STORE_FAST_STORE_FAST | 52,360 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 50,480 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 48,520 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 47,240 | 0.0% | 100.0% | 1.5% |
| FOR_ITER_LIST | 44,460 | 0.0% | 100.0% | 6.7% |
| CALL_ISINSTANCE | 43,200 | 0.0% | 100.0% |  |
| GET_ITER | 41,680 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 41,000 | 0.0% | 100.0% | 16.7% |
| BUILD_LIST | 39,660 | 0.0% | 100.0% |  |
| STORE_ATTR | 36,820 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 36,600 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 36,560 | 0.0% | 100.0% | 0.7% |
| LIST_APPEND | 33,720 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,640 | 0.0% | 100.0% | 9.1% |
| CALL_BUILTIN_O | 33,440 | 0.0% | 100.0% | 5.4% |
| STORE_SUBSCR_DICT | 31,480 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 31,120 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 30,680 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 30,020 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 28,540 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 28,500 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 25,820 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 24,600 | 0.0% | 100.0% | 1.1% |
| TO_BOOL_INT | 24,240 | 0.0% | 100.0% | 2.7% |
| FOR_ITER_RANGE | 23,840 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 22,740 | 0.0% | 100.0% |  |
| FORMAT_SIMPLE | 21,920 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 21,300 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 19,060 | 0.0% | 100.0% |  |
| BEFORE_WITH | 18,100 | 0.0% | 100.0% |  |
| BUILD_STRING | 18,040 | 0.0% | 100.0% |  |
| COMPARE_OP | 17,760 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 17,680 | 0.0% | 100.0% |  |
| BUILD_MAP | 17,380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 15,260 | 0.0% | 100.0% | 14.4% |
| LOAD_GLOBAL | 14,800 | 0.0% | 100.0% |  |
| CALL_KW | 14,640 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 14,220 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 13,780 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 12,740 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 10,700 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 10,360 | 0.0% | 100.0% |  |
| MAP_ADD | 9,780 | 0.0% | 100.0% |  |
| RESUME | 9,280 | 0.0% | 100.0% | 123.1% |
| MAKE_CELL | 8,320 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 8,180 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 8,040 | 0.0% | 100.0% | 0.7% |
| CHECK_EXC_MATCH | 7,980 | 0.0% | 100.0% |  |
| POP_EXCEPT | 7,980 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 7,980 | 0.0% | 100.0% |  |
| IMPORT_NAME | 7,140 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 7,060 | 0.0% | 100.0% |  |
| DICT_MERGE | 6,720 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 6,340 | 0.0% | 100.0% |  |
| LIST_EXTEND | 5,820 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 5,820 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 5,800 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 5,520 | 0.0% | 100.0% | 8.0% |
| BUILD_CONST_KEY_MAP | 5,420 | 0.0% | 100.0% |  |
| IMPORT_FROM | 4,900 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 4,140 | 0.0% | 100.0% |  |
| STORE_DEREF | 4,140 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 3,780 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 3,760 | 0.0% | 100.0% | 0.5% |
| CALL_TUPLE_1 | 3,420 | 0.0% | 100.0% |  |
| CALL_STR_1 | 3,300 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 2,960 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,180 | 0.0% | 100.0% |  |
| RERAISE | 2,000 | 0.0% | 100.0% |  |
| UNARY_NOT | 1,900 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 1,800 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 1,700 | 0.0% | 100.0% | 3.5% |
| BUILD_SLICE | 1,540 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 1,360 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 1,220 | 0.0% | 100.0% |  |
| BUILD_SET | 1,100 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,060 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 740 | 0.0% | 100.0% |  |
| UNARY_INVERT | 720 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 620 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 540 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 540 | 0.0% | 100.0% |  |
| FOR_ITER_GEN | 480 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 400 | 0.0% | 100.0% |  |
| DELETE_NAME | 300 | 0.0% | 100.0% |  |
| DICT_UPDATE | 300 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 240 | 0.0% | 100.0% |  |
| STORE_SLICE | 160 | 0.0% | 100.0% |  |
| DELETE_FAST | 140 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 140 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 100 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 100 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_2 | 80 | 0.0% | 100.0% |  |
| GET_AWAITABLE | 80 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 80 | 0.0% | 100.0% |  |
| SET_UPDATE | 80 | 0.0% | 100.0% |  |
| END_FOR | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| SEND_GEN | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST | 141,742,520 | 5.7% | 5.7% |
| CACHE RESUME_CHECK | 141,577,220 | 5.7% | 11.4% |
| LOAD_CONST SEND | 133,515,720 | 5.4% | 16.8% |
| GET_ANEXT LOAD_CONST | 133,515,680 | 5.4% | 22.1% |
| YIELD_VALUE INTERPRETER_EXIT | 125,521,160 | 5.1% | 27.2% |
| RESUME_CHECK POP_TOP | 125,521,160 | 5.1% | 32.3% |
| END_SEND STORE_FAST | 125,515,680 | 5.1% | 37.3% |
| CALL_INTRINSIC_1 YIELD_VALUE | 125,515,680 | 5.1% | 42.4% |
| JUMP_BACKWARD GET_ANEXT | 125,515,680 | 5.1% | 47.4% |
| SEND END_SEND | 125,515,680 | 5.1% | 52.5% |
| POP_TOP JUMP_BACKWARD | 117,532,820 | 4.7% | 57.2% |
| LOAD_FAST CALL_INTRINSIC_1 | 117,515,680 | 4.7% | 61.9% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 80,260,780 | 3.2% | 65.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 42,992,520 | 1.7% | 66.9% |
| LOAD_FAST LOAD_CONST | 32,248,620 | 1.3% | 68.2% |
| RESUME_CHECK LOAD_FAST | 32,134,740 | 1.3% | 69.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 24,141,720 | 1.0% | 70.4% |
| RETURN_CONST INTERPRETER_EXIT | 24,068,060 | 1.0% | 71.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 24,065,840 | 1.0% | 72.4% |
| POP_TOP RETURN_CONST | 24,057,480 | 1.0% | 73.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 16,153,920 | 0.7% | 74.0% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 16,059,100 | 0.6% | 74.6% |
| LOAD_FAST CALL_LEN | 16,042,560 | 0.6% | 75.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 16,038,860 | 0.6% | 75.9% |
| LOAD_CONST COMPARE_OP_INT | 16,037,060 | 0.6% | 76.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 16,036,860 | 0.6% | 77.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 16,024,600 | 0.6% | 77.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 16,017,260 | 0.6% | 78.5% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 16,010,560 | 0.6% | 79.2% |
| CALL_LEN STORE_FAST | 16,005,340 | 0.6% | 79.8% |
| BINARY_SLICE CALL_PY_EXACT_ARGS | 16,002,980 | 0.6% | 80.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 13,268,420 | 0.5% | 81.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,137,020 | 0.3% | 81.3% |
| POP_TOP LOAD_FAST | 8,090,960 | 0.3% | 81.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 8,090,900 | 0.3% | 82.0% |
| LOAD_FAST PUSH_NULL | 8,089,780 | 0.3% | 82.3% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 8,070,460 | 0.3% | 82.6% |
| LOAD_CONST LOAD_FAST | 8,061,140 | 0.3% | 82.9% |
| RETURN_CONST POP_TOP | 8,059,960 | 0.3% | 83.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 8,045,100 | 0.3% | 83.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 8,045,100 | 0.3% | 83.9% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,041,600 | 0.3% | 84.2% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 8,041,160 | 0.3% | 84.6% |
| CALL STORE_FAST | 8,032,460 | 0.3% | 84.9% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 8,029,920 | 0.3% | 85.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 8,024,060 | 0.3% | 85.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,019,540 | 0.3% | 85.8% |
| LOAD_CONST BINARY_SLICE | 8,019,320 | 0.3% | 86.2% |
| POP_JUMP_IF_NONE LOAD_FAST | 8,016,800 | 0.3% | 86.5% |
| LOAD_CONST BINARY_OP | 8,016,620 | 0.3% | 86.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 8,015,520 | 0.3% | 87.1% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 8,014,900 | 0.3% | 87.5% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 8,010,740 | 0.3% | 87.8% |
| RETURN_VALUE RETURN_VALUE | 8,010,600 | 0.3% | 88.1% |
| EXIT_INIT_CHECK RETURN_VALUE | 8,009,560 | 0.3% | 88.4% |
| RETURN_CONST EXIT_INIT_CHECK | 8,009,560 | 0.3% | 88.7% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 8,009,500 | 0.3% | 89.1% |
| PUSH_NULL CALL | 8,009,340 | 0.3% | 89.4% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 8,009,040 | 0.3% | 89.7% |
| TO_BOOL POP_JUMP_IF_FALSE | 8,008,560 | 0.3% | 90.0% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 8,006,960 | 0.3% | 90.4% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,006,540 | 0.3% | 90.7% |
| BINARY_OP STORE_FAST | 8,005,300 | 0.3% | 91.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 8,005,280 | 0.3% | 91.3% |
| LOAD_FAST BINARY_SLICE | 8,004,580 | 0.3% | 91.6% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 8,004,560 | 0.3% | 92.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 8,004,280 | 0.3% | 92.3% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 8,004,240 | 0.3% | 92.6% |
| CACHE POP_TOP | 8,003,800 | 0.3% | 92.9% |
| POP_TOP RESUME_CHECK | 8,003,700 | 0.3% | 93.3% |
| STORE_FAST JUMP_BACKWARD | 8,002,480 | 0.3% | 93.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 8,002,480 | 0.3% | 93.9% |
| BINARY_OP_ADD_INT LOAD_CONST | 8,001,980 | 0.3% | 94.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL | 8,001,680 | 0.3% | 94.5% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 8,001,040 | 0.3% | 94.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_ALWAYS_TRUE | 8,001,020 | 0.3% | 95.2% |
| CALL CALL_METHOD_DESCRIPTOR_O | 8,000,340 | 0.3% | 95.5% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 8,000,040 | 0.3% | 95.8% |
| CACHE RETURN_GENERATOR | 8,000,000 | 0.3% | 96.2% |
| GET_AITER GET_ANEXT | 8,000,000 | 0.3% | 96.5% |
| RETURN_GENERATOR INTERPRETER_EXIT | 8,000,000 | 0.3% | 96.8% |
| SEND END_ASYNC_FOR | 8,000,000 | 0.3% | 97.1% |
| LOAD_ATTR_INSTANCE_VALUE CALL_INTRINSIC_1 | 7,999,980 | 0.3% | 97.4% |
| BINARY_SUBSCR LOAD_GLOBAL_MODULE | 7,999,960 | 0.3% | 97.8% |
| END_ASYNC_FOR JUMP_BACKWARD | 7,999,920 | 0.3% | 98.1% |
| LOAD_ATTR_INSTANCE_VALUE GET_AITER | 7,999,880 | 0.3% | 98.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_NONE | 7,998,960 | 0.3% | 98.7% |
| JUMP_BACKWARD LOAD_FAST | 5,260,320 | 0.2% | 98.9% |
| RETURN_VALUE LOAD_FAST_LOAD_FAST | 5,242,880 | 0.2% | 99.2% |
| RETURN_CONST CALL_ALLOC_AND_ENTER_INIT | 5,242,840 | 0.2% | 99.4% |
| RETURN_CONST LOAD_FAST_LOAD_FAST | 2,757,200 | 0.1% | 99.5% |
| RETURN_VALUE CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 0.1% | 99.6% |
| JUMP_BACKWARD RETURN_CONST | 2,757,120 | 0.1% | 99.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 110,920 | 0.0% | 99.7% |
| LOAD_CONST LOAD_CONST | 100,700 | 0.0% | 99.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 99,200 | 0.0% | 99.7% |
| LOAD_FAST LOAD_FAST | 89,560 | 0.0% | 99.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 87,140 | 0.0% | 99.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 84,740 | 0.0% | 99.7% |
| PUSH_NULL LOAD_FAST | 81,820 | 0.0% | 99.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,019,320 | 50.0% |
| LOAD_FAST | 8,004,580 | 49.9% |
| BINARY_OP_ADD_INT | 10,220 | 0.1% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 16,002,980 | 99.8% |
| STORE_FAST | 13,940 | 0.1% |
| LOAD_FAST | 4,680 | 0.0% |
| SWAP | 4,680 | 0.0% |
| LOAD_CONST | 2,560 | 0.0% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 120 | 75.0% |
| LOAD_CONST | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 120 | 75.0% |
| LOAD_FAST | 40 | 25.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 141,577,220 | 89.8% |
| POP_TOP | 8,003,800 | 5.1% |
| RETURN_GENERATOR | 8,000,000 | 5.1% |
| COPY_FREE_VARS | 30,880 | 0.0% |
| RESUME | 5,320 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 7,400 | 40.9% |
| RETURN_VALUE | 4,920 | 27.2% |
| CALL | 4,660 | 25.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,000 | 5.5% |
| LOAD_GLOBAL | 100 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 17,100 | 94.5% |
| STORE_FAST | 1,000 | 5.5% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 1,640 | 75.2% |
| LOAD_FAST_LOAD_FAST | 500 | 22.9% |
| RETURN_VALUE | 20 | 0.9% |
| BINARY_OP | 20 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,680 | 77.1% |
| JUMP_BACKWARD | 500 | 22.9% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,000,040 | 99.8% |
| LOAD_CONST | 7,400 | 0.1% |
| BINARY_SUBSCR | 2,340 | 0.0% |
| BUILD_SLICE | 1,540 | 0.0% |
| LOAD_FAST | 980 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,999,960 | 99.8% |
| SWAP | 4,700 | 0.1% |
| BINARY_SUBSCR | 2,340 | 0.0% |
| GET_ITER | 1,320 | 0.0% |
| LOAD_CONST | 1,320 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 7,920 | 99.2% |
| LOAD_GLOBAL | 40 | 0.5% |
| LOAD_NAME | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,980 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,220 | 100.0% |


</details>

### END_ASYNC_FOR

<details>
<summary> Successors and predecessors for END_ASYNC_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 8,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,999,920 | 100.0% |
| RETURN_CONST | 80 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 125,515,680 | 100.0% |
| RETURN_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 125,515,680 | 100.0% |
| POP_TOP | 80 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 8,009,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,009,560 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 10,360 | 47.3% |
| LOAD_FAST | 6,440 | 29.4% |
| LOAD_ATTR | 3,120 | 14.2% |
| STORE_FAST_LOAD_FAST | 1,480 | 6.8% |
| LOAD_ATTR_MODULE | 360 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,820 | 81.3% |
| BUILD_STRING | 4,060 | 18.5% |
| LOAD_FAST | 40 | 0.2% |


</details>

### GET_AITER

<details>
<summary> Successors and predecessors for GET_AITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 7,999,880 | 100.0% |
| RETURN_VALUE | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 8,000,000 | 100.0% |


</details>

### GET_ANEXT

<details>
<summary> Successors and predecessors for GET_ANEXT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 125,515,680 | 94.0% |
| GET_AITER | 8,000,000 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 133,515,680 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,140 | 57.9% |
| LOAD_ATTR_INSTANCE_VALUE | 4,300 | 10.3% |
| LOAD_GLOBAL_MODULE | 2,000 | 4.8% |
| BUILD_TUPLE | 1,620 | 3.9% |
| BINARY_SUBSCR | 1,320 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 10,480 | 25.1% |
| FOR_ITER_TUPLE | 8,820 | 21.2% |
| FOR_ITER_LIST | 8,560 | 20.5% |
| EXTENDED_ARG | 5,540 | 13.3% |
| CALL_PY_EXACT_ARGS | 3,480 | 8.3% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 125,521,160 | 79.6% |
| RETURN_CONST | 24,068,060 | 15.3% |
| RETURN_GENERATOR | 8,000,000 | 5.1% |
| RETURN_VALUE | 26,880 | 0.0% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 3,540 | 85.5% |
| POP_TOP | 200 | 4.8% |
| LOAD_NAME | 120 | 2.9% |
| RETURN_VALUE | 100 | 2.4% |
| DELETE_NAME | 60 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,140 | 100.0% |


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 60 | 60.0% |
| LOAD_CONST | 40 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FROM_DICT_OR_DEREF | 80 | 80.0% |
| STORE_DEREF | 20 | 20.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 50,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 25,760 | 51.0% |
| SET_FUNCTION_ATTRIBUTE | 16,160 | 32.0% |
| LOAD_CONST | 4,260 | 8.4% |
| CALL | 2,060 | 4.1% |
| LOAD_FAST | 760 | 1.5% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 46,740 | 40.2% |
| POP_TOP | 14,380 | 12.4% |
| STORE_FAST_STORE_FAST | 9,640 | 8.3% |
| NOP | 8,420 | 7.2% |
| POP_JUMP_IF_FALSE | 6,820 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,480 | 56.4% |
| LOAD_GLOBAL_MODULE | 24,260 | 20.9% |
| LOAD_CONST | 9,880 | 8.5% |
| NOP | 8,420 | 7.2% |
| LOAD_FAST_LOAD_FAST | 4,160 | 3.6% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,960 | 62.2% |
| COPY | 1,040 | 13.0% |
| POP_TOP | 640 | 8.0% |
| JUMP_FORWARD | 620 | 7.8% |
| POP_JUMP_IF_FALSE | 240 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,980 | 62.4% |
| RERAISE | 1,040 | 13.0% |
| EXTENDED_ARG | 1,020 | 12.8% |
| RETURN_CONST | 540 | 6.8% |
| JUMP_FORWARD | 240 | 3.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 125,521,160 | 79.6% |
| CALL_METHOD_DESCRIPTOR_O | 16,010,560 | 10.1% |
| RETURN_CONST | 8,059,960 | 5.1% |
| CACHE | 8,003,800 | 5.1% |
| CALL | 54,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 117,532,820 | 74.5% |
| RETURN_CONST | 24,057,480 | 15.2% |
| LOAD_FAST | 8,090,960 | 5.1% |
| RESUME_CHECK | 8,003,700 | 5.1% |
| LOAD_GLOBAL_BUILTIN | 20,640 | 0.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 6,260 | 78.4% |
| RERAISE | 1,040 | 13.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 300 | 3.8% |
| BINARY_SUBSCR_STR_INT | 240 | 3.0% |
| CALL_PY_EXACT_ARGS | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 7,900 | 99.0% |
| LOAD_GLOBAL | 60 | 0.8% |
| LOAD_NAME | 20 | 0.3% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,089,780 | 99.2% |
| LOAD_ATTR_MODULE | 37,260 | 0.5% |
| LOAD_NAME | 6,720 | 0.1% |
| LOAD_ATTR | 4,960 | 0.1% |
| LOAD_DEREF | 4,940 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 8,009,340 | 98.2% |
| LOAD_FAST | 81,820 | 1.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 18,740 | 0.2% |
| LOAD_CONST | 18,640 | 0.2% |
| LOAD_FAST_LOAD_FAST | 13,420 | 0.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 8,000,000 | 100.0% |
| COPY_FREE_VARS | 2,800 | 0.0% |
| CALL_PY_EXACT_ARGS | 1,020 | 0.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 8,000,000 | 100.0% |
| CALL | 2,340 | 0.0% |
| CALL_TUPLE_1 | 620 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 480 | 0.0% |
| CALL_BUILTIN_O | 320 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,010,600 | 49.5% |
| EXIT_INIT_CHECK | 8,009,560 | 49.5% |
| LOAD_FAST | 55,300 | 0.3% |
| CALL | 20,280 | 0.1% |
| POP_JUMP_IF_FALSE | 14,340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,010,600 | 49.5% |
| LOAD_FAST_LOAD_FAST | 5,242,880 | 32.4% |
| CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 17.0% |
| STORE_FAST | 54,020 | 0.3% |
| TO_BOOL_BOOL | 42,940 | 0.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,340 | 54.2% |
| LOAD_FAST_LOAD_FAST | 5,800 | 30.4% |
| LOAD_FAST | 1,080 | 5.7% |
| LOAD_CONST | 1,060 | 5.6% |
| STORE_SUBSCR | 480 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,780 | 72.3% |
| JUMP_FORWARD | 1,320 | 6.9% |
| LOAD_FAST | 1,240 | 6.5% |
| RETURN_CONST | 960 | 5.0% |
| EXTENDED_ARG | 840 | 4.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,004,240 | 99.9% |
| LOAD_FAST | 4,200 | 0.1% |
| TO_BOOL | 2,340 | 0.0% |
| CALL | 1,400 | 0.0% |
| LOAD_ATTR | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,008,560 | 99.9% |
| TO_BOOL | 2,340 | 0.0% |
| POP_JUMP_IF_TRUE | 2,240 | 0.0% |
| TO_BOOL_BOOL | 1,880 | 0.0% |
| TO_BOOL_INT | 340 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 72.2% |
| BINARY_OP | 80 | 11.1% |
| LOAD_ATTR_MODULE | 60 | 8.3% |
| LOAD_FAST_LOAD_FAST | 40 | 5.6% |
| LOAD_ATTR | 20 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 720 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 240 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 1,560 | 82.1% |
| TO_BOOL_LIST | 240 | 12.6% |
| TO_BOOL_BOOL | 60 | 3.2% |
| TO_BOOL | 40 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,380 | 72.6% |
| STORE_FAST | 280 | 14.7% |
| CALL_PY_EXACT_ARGS | 240 | 12.6% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,016,620 | 99.7% |
| LOAD_GLOBAL_MODULE | 11,620 | 0.1% |
| BINARY_OP | 3,880 | 0.0% |
| LOAD_FAST_LOAD_FAST | 2,300 | 0.0% |
| BUILD_TUPLE | 1,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,005,300 | 99.5% |
| TO_BOOL_INT | 11,860 | 0.1% |
| STORE_SUBSCR | 10,340 | 0.1% |
| BINARY_OP | 3,880 | 0.0% |
| LOAD_FAST | 2,060 | 0.0% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,420 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,260 | 41.7% |
| STORE_FAST | 1,600 | 29.5% |
| RETURN_VALUE | 1,000 | 18.5% |
| STORE_NAME | 240 | 4.4% |
| LOAD_FAST | 140 | 2.6% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,260 | 25.9% |
| LOAD_ATTR_INSTANCE_VALUE | 4,800 | 12.1% |
| STORE_ATTR_INSTANCE_VALUE | 4,120 | 10.4% |
| LOAD_FAST | 4,040 | 10.2% |
| RESUME_CHECK | 4,040 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,520 | 26.5% |
| SWAP | 10,260 | 25.9% |
| STORE_FAST | 9,980 | 25.2% |
| COMPARE_OP | 4,800 | 12.1% |
| CALL_METHOD_DESCRIPTOR_O | 2,060 | 5.2% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,140 | 41.1% |
| LOAD_FAST | 4,220 | 24.3% |
| CALL_INTRINSIC_1 | 1,000 | 5.8% |
| BUILD_TUPLE | 940 | 5.4% |
| STORE_FAST | 920 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,580 | 43.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 5,960 | 34.3% |
| STORE_FAST | 780 | 4.5% |
| LOAD_GLOBAL_BUILTIN | 600 | 3.5% |
| CALL_BUILTIN_FAST | 560 | 3.2% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 600 | 54.5% |
| LOAD_CONST | 260 | 23.6% |
| LOAD_GLOBAL_MODULE | 140 | 12.7% |
| PUSH_NULL | 80 | 7.3% |
| LOAD_GLOBAL | 20 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 760 | 69.1% |
| BINARY_OP | 200 | 18.2% |
| LOAD_CONST | 80 | 7.3% |
| STORE_FAST | 60 | 5.5% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,540 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,980 | 77.5% |
| FORMAT_SIMPLE | 4,060 | 22.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,400 | 29.9% |
| LIST_APPEND | 5,360 | 29.7% |
| LOAD_FAST | 3,420 | 19.0% |
| YIELD_VALUE | 1,480 | 8.2% |
| CALL_BUILTIN_O | 1,480 | 8.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,800 | 40.8% |
| LOAD_FAST_LOAD_FAST | 5,100 | 10.5% |
| LOAD_GLOBAL_MODULE | 5,000 | 10.3% |
| CALL_BUILTIN_O | 2,940 | 6.1% |
| CALL | 2,380 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,860 | 22.4% |
| STORE_FAST | 6,920 | 14.3% |
| RETURN_VALUE | 6,080 | 12.5% |
| LOAD_FAST | 3,600 | 7.4% |
| CONTAINS_OP | 3,300 | 6.8% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 8,009,340 | 49.4% |
| LOAD_ATTR_INSTANCE_VALUE | 8,001,680 | 49.4% |
| LOAD_CONST | 50,060 | 0.3% |
| LOAD_FAST | 32,140 | 0.2% |
| LOAD_ATTR_MODULE | 29,020 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,032,460 | 49.6% |
| CALL_METHOD_DESCRIPTOR_O | 8,000,340 | 49.4% |
| POP_TOP | 54,820 | 0.3% |
| RESUME_CHECK | 25,600 | 0.2% |
| RETURN_VALUE | 20,280 | 0.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 6,720 | 52.7% |
| CALL_INTRINSIC_1 | 3,860 | 30.3% |
| LOAD_FAST | 1,560 | 12.2% |
| STORE_FAST | 480 | 3.8% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,420 | 34.7% |
| RETURN_VALUE | 3,920 | 30.8% |
| POP_TOP | 1,920 | 15.1% |
| RESUME_CHECK | 1,220 | 9.6% |
| GET_ITER | 480 | 3.8% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,515,680 | 93.6% |
| LOAD_ATTR_INSTANCE_VALUE | 7,999,980 | 6.4% |
| LIST_EXTEND | 5,040 | 0.0% |
| IMPORT_NAME | 420 | 0.0% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 125,515,680 | 100.0% |
| CALL_FUNCTION_EX | 3,860 | 0.0% |
| BUILD_MAP | 1,000 | 0.0% |
| POP_TOP | 420 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_INTRINSIC_2

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_2 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 60 | 75.0% |
| MAKE_FUNCTION | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 75.0% |
| COPY | 20 | 25.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 14,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,980 | 75.0% |
| STORE_FAST | 1,400 | 9.6% |
| STORE_NAME | 740 | 5.1% |
| RETURN_VALUE | 620 | 4.2% |
| MAKE_CELL | 360 | 2.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,600 | 37.2% |
| BUILD_LIST | 4,800 | 27.0% |
| LOAD_GLOBAL_MODULE | 2,700 | 15.2% |
| LOAD_CONST | 1,540 | 8.7% |
| BINARY_OP | 1,000 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,200 | 68.7% |
| POP_JUMP_IF_TRUE | 4,240 | 23.9% |
| COMPARE_OP | 400 | 2.3% |
| COMPARE_OP_INT | 400 | 2.3% |
| COMPARE_OP_STR | 380 | 2.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 22,940 | 23.4% |
| LOAD_FAST | 22,160 | 22.6% |
| LOAD_CONST | 20,580 | 21.0% |
| LOAD_FAST_LOAD_FAST | 18,900 | 19.3% |
| LOAD_ATTR_MODULE | 3,880 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 77,520 | 79.0% |
| POP_JUMP_IF_TRUE | 12,580 | 12.8% |
| EXTENDED_ARG | 5,740 | 5.9% |
| STORE_FAST | 1,380 | 1.4% |
| RETURN_VALUE | 720 | 0.7% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,220 | 98.6% |
| LOAD_GLOBAL_MODULE | 120 | 1.2% |
| LOAD_GLOBAL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 10,360 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 10,820 | 14.2% |
| CALL | 9,980 | 13.1% |
| COMPARE_OP_INT | 9,700 | 12.7% |
| SWAP | 9,360 | 12.3% |
| CALL_BUILTIN_FAST | 8,360 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 49,840 | 65.2% |
| COMPARE_OP_STR | 9,360 | 12.3% |
| TO_BOOL_STR | 5,240 | 6.9% |
| TO_BOOL_NONE | 3,800 | 5.0% |
| STORE_FAST_STORE_FAST | 2,120 | 2.8% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 30,880 | 84.4% |
| CALL_PY_EXACT_ARGS | 3,680 | 10.1% |
| CALL | 1,560 | 4.3% |
| CALL_FUNCTION_EX | 300 | 0.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 100 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 32,900 | 89.9% |
| RETURN_GENERATOR | 2,800 | 7.7% |
| RESUME | 460 | 1.3% |
| MAKE_CELL | 440 | 1.2% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 120 | 85.7% |
| POP_TOP | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 100 | 71.4% |
| LOAD_GLOBAL | 40 | 28.6% |


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 120 | 40.0% |
| STORE_NAME | 100 | 33.3% |
| FOR_ITER | 60 | 20.0% |
| POP_TOP | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 120 | 40.0% |
| LOAD_NAME | 80 | 26.7% |
| LOAD_BUILD_CLASS | 60 | 20.0% |
| LOAD_CONST | 40 | 13.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,120 | 91.1% |
| CALL | 600 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 6,720 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 220 | 73.3% |
| BUILD_CONST_KEY_MAP | 60 | 20.0% |
| BUILD_MAP | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 160 | 53.3% |
| STORE_NAME | 80 | 26.7% |
| EXTENDED_ARG | 20 | 6.7% |
| LOAD_CONST | 20 | 6.7% |
| LOAD_NAME | 20 | 6.7% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,140 | 21.8% |
| CONTAINS_OP | 5,740 | 9.5% |
| GET_ITER | 5,540 | 9.2% |
| POP_TOP | 5,220 | 8.6% |
| JUMP_FORWARD | 5,200 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,880 | 29.6% |
| POP_JUMP_IF_FALSE | 13,620 | 22.6% |
| FOR_ITER_LIST | 13,160 | 21.8% |
| JUMP_FORWARD | 5,700 | 9.4% |
| FOR_ITER | 5,520 | 9.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 57,400 | 80.8% |
| EXTENDED_ARG | 5,520 | 7.8% |
| GET_ITER | 2,960 | 4.2% |
| LOAD_FAST | 2,360 | 3.3% |
| FOR_ITER | 2,280 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 31,440 | 44.3% |
| STORE_FAST | 29,080 | 41.0% |
| RETURN_CONST | 3,280 | 4.6% |
| FOR_ITER | 2,280 | 3.2% |
| STORE_NAME | 1,040 | 1.5% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 2,980 | 60.8% |
| STORE_NAME | 1,920 | 39.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 4,860 | 99.2% |
| PUSH_EXC_INFO | 20 | 0.4% |
| STORE_FAST | 20 | 0.4% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 3,660 | 51.3% |
| IMPORT_FROM | 2,980 | 41.7% |
| CALL_INTRINSIC_1 | 420 | 5.9% |
| STORE_FAST | 80 | 1.1% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 43,700 | 77.2% |
| LOAD_GLOBAL_BUILTIN | 7,060 | 12.5% |
| LOAD_CONST | 4,000 | 7.1% |
| LOAD_FAST | 1,480 | 2.6% |
| LOAD_GLOBAL | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 46,720 | 82.6% |
| POP_JUMP_IF_TRUE | 5,720 | 10.1% |
| LOAD_FAST | 3,100 | 5.5% |
| RETURN_VALUE | 400 | 0.7% |
| COPY | 300 | 0.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 117,532,820 | 87.9% |
| STORE_FAST | 8,002,480 | 6.0% |
| END_ASYNC_FOR | 7,999,920 | 6.0% |
| LIST_APPEND | 33,720 | 0.0% |
| POP_JUMP_IF_TRUE | 32,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 125,515,680 | 93.9% |
| LOAD_FAST | 5,260,320 | 3.9% |
| RETURN_CONST | 2,757,120 | 2.1% |
| FOR_ITER | 57,400 | 0.0% |
| FOR_ITER_TUPLE | 44,580 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,380 | 43.0% |
| EXTENDED_ARG | 5,700 | 18.3% |
| POP_TOP | 3,300 | 10.6% |
| LOAD_FAST | 2,000 | 6.4% |
| COMPARE_OP_STR | 1,640 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,920 | 44.7% |
| LOAD_GLOBAL_BUILTIN | 5,280 | 17.0% |
| EXTENDED_ARG | 5,200 | 16.7% |
| LOAD_FAST_LOAD_FAST | 2,360 | 7.6% |
| COPY | 1,640 | 5.3% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 20,400 | 60.5% |
| BUILD_STRING | 5,360 | 15.9% |
| LOAD_FAST | 2,920 | 8.7% |
| CALL_BUILTIN_CLASS | 2,560 | 7.6% |
| BUILD_TUPLE | 2,060 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 33,720 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,720 | 81.1% |
| LOAD_CONST | 600 | 10.3% |
| LOAD_ATTR | 180 | 3.1% |
| LOAD_ATTR_SLOT | 140 | 2.4% |
| CALL_KW | 80 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 5,040 | 86.6% |
| STORE_NAME | 240 | 4.1% |
| LOAD_FAST | 160 | 2.7% |
| LOAD_CONST | 140 | 2.4% |
| BUILD_LIST | 120 | 2.1% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,300 | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE | 7,980 | 6.9% |
| LOAD_FAST_LOAD_FAST | 7,880 | 6.8% |
| LOAD_NAME | 6,720 | 5.8% |
| LOAD_ATTR | 5,540 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,460 | 20.2% |
| STORE_FAST | 18,940 | 16.3% |
| LOAD_ATTR_METHOD_NO_DICT | 14,100 | 12.1% |
| CALL | 12,160 | 10.4% |
| LOAD_ATTR | 5,540 | 4.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 133,515,680 | 73.3% |
| LOAD_FAST | 32,248,620 | 17.7% |
| LOAD_FAST_LOAD_FAST | 8,006,540 | 4.4% |
| BINARY_OP_ADD_INT | 8,001,980 | 4.4% |
| LOAD_CONST | 100,700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 133,515,720 | 73.3% |
| COMPARE_OP_INT | 16,037,060 | 8.8% |
| LOAD_FAST | 8,061,140 | 4.4% |
| BINARY_OP_ADD_INT | 8,041,600 | 4.4% |
| BINARY_SLICE | 8,019,320 | 4.4% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 30,100 | 55.4% |
| POP_JUMP_IF_FALSE | 6,640 | 12.2% |
| RESUME_CHECK | 3,760 | 6.9% |
| STORE_FAST | 3,620 | 6.7% |
| BINARY_SLICE | 2,000 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,760 | 56.6% |
| PUSH_NULL | 4,940 | 9.1% |
| LOAD_CONST | 3,740 | 6.9% |
| TO_BOOL_BOOL | 3,040 | 5.6% |
| LOAD_ATTR_METHOD_NO_DICT | 2,220 | 4.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 141,742,520 | 49.3% |
| POP_JUMP_IF_FALSE | 42,992,520 | 15.0% |
| RESUME_CHECK | 32,134,740 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 16,153,920 | 5.6% |
| POP_TOP | 8,090,960 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 117,515,680 | 40.9% |
| LOAD_ATTR_INSTANCE_VALUE | 80,260,780 | 27.9% |
| LOAD_CONST | 32,248,620 | 11.2% |
| CALL_LEN | 16,042,560 | 5.6% |
| PUSH_NULL | 8,089,780 | 2.8% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,480 | 97.9% |
| LOAD_FAST_AND_CLEAR | 220 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,480 | 97.9% |
| LOAD_FAST_AND_CLEAR | 220 | 2.1% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,660 | 73.5% |
| LOAD_ATTR_METHOD_NO_DICT | 800 | 12.6% |
| LOAD_FAST | 620 | 9.8% |
| LOAD_GLOBAL_BUILTIN | 120 | 1.9% |
| POP_JUMP_IF_FALSE | 80 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 4,740 | 74.8% |
| LOAD_FAST | 620 | 9.8% |
| CALL_LIST_APPEND | 620 | 9.8% |
| LOAD_ATTR | 180 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 120 | 1.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 16,038,860 | 33.2% |
| LOAD_GLOBAL_MODULE | 16,024,600 | 33.2% |
| RESUME_CHECK | 8,029,920 | 16.6% |
| RETURN_VALUE | 5,242,880 | 10.9% |
| RETURN_CONST | 2,757,200 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 24,065,840 | 49.9% |
| LOAD_ATTR_INSTANCE_VALUE | 8,014,900 | 16.6% |
| LOAD_CONST | 8,006,540 | 16.6% |
| BINARY_SUBSCR | 8,000,040 | 16.6% |
| LOAD_FAST | 44,860 | 0.1% |


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 40 | 50.0% |
| STORE_NAME | 40 | 50.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,460 | 16.6% |
| POP_JUMP_IF_FALSE | 2,040 | 13.8% |
| STORE_FAST | 1,620 | 10.9% |
| RESUME | 1,440 | 9.7% |
| RESUME_CHECK | 1,120 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,800 | 25.7% |
| LOAD_GLOBAL_BUILTIN | 3,040 | 20.5% |
| LOAD_FAST | 2,780 | 18.8% |
| LOAD_ATTR | 1,280 | 8.6% |
| CALL | 860 | 5.8% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 21,000 | 23.5% |
| LOAD_NAME | 20,080 | 22.5% |
| STORE_NAME | 18,820 | 21.1% |
| LOAD_CONST | 7,240 | 8.1% |
| RESUME | 4,140 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 20,720 | 23.2% |
| LOAD_NAME | 20,080 | 22.5% |
| LOAD_CONST | 10,020 | 11.2% |
| PUSH_NULL | 6,720 | 7.5% |
| LOAD_ATTR | 6,720 | 7.5% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 700 | 94.6% |
| LOAD_DEREF | 40 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 240 | 32.4% |
| CALL | 140 | 18.9% |
| PUSH_NULL | 100 | 13.5% |
| LOAD_FAST_LOAD_FAST | 100 | 13.5% |
| LOAD_SUPER_ATTR_ATTR | 100 | 13.5% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 3,140 | 37.7% |
| CALL_PY_EXACT_ARGS | 2,180 | 26.2% |
| CACHE | 1,500 | 18.0% |
| CALL | 700 | 8.4% |
| COPY_FREE_VARS | 440 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,900 | 46.9% |
| MAKE_CELL | 3,140 | 37.7% |
| RESUME | 1,280 | 15.4% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,080 | 41.7% |
| LOAD_FAST_LOAD_FAST | 1,480 | 15.1% |
| LOAD_FAST | 1,400 | 14.3% |
| BINARY_SUBSCR_TUPLE_INT | 1,340 | 13.7% |
| LOAD_NAME | 680 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,680 | 47.9% |
| LOAD_CONST | 3,260 | 33.3% |
| EXTENDED_ARG | 1,560 | 16.0% |
| DICT_UPDATE | 220 | 2.2% |
| BUILD_MAP | 60 | 0.6% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 16,036,860 | 28.4% |
| TO_BOOL_BOOL | 8,137,020 | 14.4% |
| TO_BOOL_NONE | 8,010,740 | 14.2% |
| TO_BOOL | 8,008,560 | 14.2% |
| TO_BOOL_LIST | 8,006,960 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,992,520 | 76.1% |
| RETURN_CONST | 13,268,420 | 23.5% |
| LOAD_GLOBAL_MODULE | 37,900 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 32,480 | 0.1% |
| JUMP_BACKWARD | 28,360 | 0.1% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,019,540 | 99.8% |
| LOAD_ATTR_INSTANCE_VALUE | 7,780 | 0.1% |
| LOAD_GLOBAL_MODULE | 3,020 | 0.0% |
| LOAD_ATTR_MODULE | 2,060 | 0.0% |
| RETURN_VALUE | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,016,800 | 99.8% |
| LOAD_GLOBAL_MODULE | 6,460 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 5,160 | 0.1% |
| LOAD_CONST | 2,720 | 0.0% |
| NOP | 1,100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,400 | 71.6% |
| LOAD_ATTR_INSTANCE_VALUE | 8,060 | 9.9% |
| CALL_BUILTIN_FAST | 7,080 | 8.7% |
| LOAD_FAST_CHECK | 4,740 | 5.8% |
| LOAD_GLOBAL_MODULE | 2,760 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,220 | 57.9% |
| LOAD_GLOBAL_MODULE | 12,760 | 15.6% |
| JUMP_BACKWARD | 8,800 | 10.8% |
| NOP | 4,000 | 4.9% |
| LOAD_CONST | 2,400 | 2.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 87,140 | 62.2% |
| CONTAINS_OP | 12,580 | 9.0% |
| COMPARE_OP_INT | 8,120 | 5.8% |
| TO_BOOL_INT | 7,680 | 5.5% |
| IS_OP | 5,720 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,440 | 28.2% |
| JUMP_BACKWARD | 32,900 | 23.5% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 13.7% |
| LOAD_GLOBAL_MODULE | 15,500 | 11.1% |
| POP_TOP | 12,620 | 9.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 400 | 74.1% |
| LOAD_CONST | 80 | 14.8% |
| CALL_KW | 60 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 1,040 | 52.0% |
| POP_JUMP_IF_FALSE | 960 | 48.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,040 | 52.0% |
| COPY | 960 | 48.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 24,057,480 | 50.0% |
| POP_JUMP_IF_FALSE | 13,268,420 | 27.6% |
| STORE_ATTR_INSTANCE_VALUE | 8,041,160 | 16.7% |
| JUMP_BACKWARD | 2,757,120 | 5.7% |
| RESUME_CHECK | 7,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 24,068,060 | 50.0% |
| POP_TOP | 8,059,960 | 16.7% |
| EXIT_INIT_CHECK | 8,009,560 | 16.6% |
| CALL_ALLOC_AND_ENTER_INIT | 5,242,840 | 10.9% |
| LOAD_FAST_LOAD_FAST | 2,757,200 | 5.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 133,515,720 | 100.0% |
| SEND | 33,180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 125,515,680 | 94.0% |
| END_ASYNC_FOR | 8,000,000 | 6.0% |
| SEND | 33,180 | 0.0% |
| POP_TOP | 20 | 0.0% |
| SEND_GEN | 20 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 16,160 | 91.4% |
| SET_FUNCTION_ATTRIBUTE | 1,520 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 8,000 | 45.2% |
| STORE_FAST | 3,380 | 19.1% |
| LOAD_GLOBAL_MODULE | 2,000 | 11.3% |
| CALL | 1,740 | 9.8% |
| SET_FUNCTION_ATTRIBUTE | 1,520 | 8.6% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,780 | 67.3% |
| LOAD_FAST_LOAD_FAST | 8,060 | 21.9% |
| STORE_ATTR | 2,100 | 5.7% |
| SWAP | 580 | 1.6% |
| LOAD_DEREF | 380 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,400 | 50.0% |
| RETURN_CONST | 3,520 | 9.6% |
| LOAD_CONST | 2,720 | 7.4% |
| LOAD_FAST_LOAD_FAST | 2,600 | 7.1% |
| STORE_ATTR | 2,100 | 5.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 1,200 | 29.0% |
| LOAD_ATTR | 520 | 12.6% |
| CALL_BUILTIN_CLASS | 380 | 9.2% |
| LOAD_CONST | 300 | 7.2% |
| BINARY_OP_ADD_UNICODE | 300 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,320 | 31.9% |
| STORE_DEREF | 1,200 | 29.0% |
| LOAD_FAST | 340 | 8.2% |
| LOAD_CONST | 300 | 7.2% |
| LOAD_DEREF | 300 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 125,515,680 | 79.4% |
| CALL_LEN | 16,005,340 | 10.1% |
| CALL | 8,032,460 | 5.1% |
| BINARY_OP | 8,005,300 | 5.1% |
| LOAD_ATTR_INSTANCE_VALUE | 59,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 141,742,520 | 89.7% |
| LOAD_GLOBAL_MODULE | 8,045,100 | 5.1% |
| JUMP_BACKWARD | 8,002,480 | 5.1% |
| LOAD_GLOBAL_BUILTIN | 47,280 | 0.0% |
| NOP | 46,740 | 0.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 22,720 | 79.6% |
| FOR_ITER_LIST | 3,020 | 10.6% |
| CALL_LEN | 2,720 | 9.5% |
| FOR_ITER | 60 | 0.2% |
| COPY | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 20,400 | 71.5% |
| PUSH_NULL | 2,720 | 9.5% |
| LOAD_FAST | 2,120 | 7.4% |
| FORMAT_SIMPLE | 1,480 | 5.2% |
| LOAD_CONST | 1,340 | 4.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 47,560 | 90.8% |
| UNPACK_SEQUENCE_TUPLE | 2,380 | 4.5% |
| COPY | 2,120 | 4.0% |
| UNPACK_SEQUENCE | 180 | 0.3% |
| STORE_FAST_STORE_FAST | 120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,920 | 59.1% |
| NOP | 9,640 | 18.4% |
| LOAD_FAST_LOAD_FAST | 5,060 | 9.7% |
| STORE_FAST | 2,260 | 4.3% |
| LOAD_GLOBAL_MODULE | 1,640 | 3.1% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 40.0% |
| LOAD_NAME | 40 | 40.0% |
| CALL | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60 | 60.0% |
| LOAD_BUILD_CLASS | 20 | 20.0% |
| LOAD_NAME | 20 | 20.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 25,760 | 28.6% |
| LOAD_CONST | 15,180 | 16.8% |
| SET_FUNCTION_ATTRIBUTE | 8,000 | 8.9% |
| CALL | 7,640 | 8.5% |
| LOAD_NAME | 5,600 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,180 | 54.6% |
| LOAD_NAME | 18,820 | 20.9% |
| STORE_NAME | 4,640 | 5.1% |
| RETURN_CONST | 3,960 | 4.4% |
| LOAD_BUILD_CLASS | 3,540 | 3.9% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 10,480 | 19.0% |
| BUILD_LIST | 10,260 | 18.6% |
| FOR_ITER_TUPLE | 9,700 | 17.6% |
| POP_JUMP_IF_FALSE | 7,720 | 14.0% |
| BINARY_SUBSCR | 4,700 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,560 | 20.9% |
| STORE_FAST | 10,280 | 18.6% |
| BUILD_LIST | 10,260 | 18.6% |
| FOR_ITER_TUPLE | 9,660 | 17.5% |
| COPY | 9,360 | 17.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 320 | 51.6% |
| LOAD_FAST | 120 | 19.4% |
| RETURN_VALUE | 100 | 16.1% |
| CALL | 40 | 6.5% |
| STORE_FAST | 40 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 320 | 51.6% |
| STORE_FAST_STORE_FAST | 180 | 29.0% |
| STORE_NAME | 60 | 9.7% |
| STORE_FAST | 40 | 6.5% |
| LOAD_FAST | 20 | 3.2% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 125,515,680 | 100.0% |
| CALL | 2,020 | 0.0% |
| BUILD_STRING | 1,480 | 0.0% |
| LOAD_FAST | 680 | 0.0% |
| RETURN_VALUE | 620 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 125,521,160 | 100.0% |
| STORE_FAST | 420 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 5,320 | 57.3% |
| CALL | 1,700 | 18.3% |
| MAKE_CELL | 1,280 | 13.8% |
| COPY_FREE_VARS | 460 | 5.0% |
| POP_TOP | 240 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,140 | 44.6% |
| LOAD_CONST | 1,620 | 17.5% |
| LOAD_FAST | 1,460 | 15.7% |
| LOAD_GLOBAL | 1,440 | 15.5% |
| POP_TOP | 200 | 2.2% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 120 | 85.7% |
| BINARY_OP | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 140 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,041,600 | 100.0% |
| LOAD_FAST_LOAD_FAST | 1,280 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 1,060 | 0.0% |
| BINARY_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,001,980 | 99.5% |
| LOAD_FAST | 22,840 | 0.3% |
| BINARY_SLICE | 10,220 | 0.1% |
| STORE_FAST | 7,280 | 0.1% |
| CALL_PY_EXACT_ARGS | 680 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,400 | 62.9% |
| LOAD_CONST | 4,320 | 20.3% |
| BINARY_SUBSCR_LIST_INT | 2,000 | 9.4% |
| CALL_METHOD_DESCRIPTOR_O | 640 | 3.0% |
| LOAD_FAST | 400 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 6,700 | 31.5% |
| LOAD_FAST | 6,700 | 31.5% |
| STORE_FAST | 2,400 | 11.3% |
| STORE_SUBSCR_DICT | 2,000 | 9.4% |
| BUILD_TUPLE | 960 | 4.5% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 1,060 | 58.9% |
| LOAD_CONST | 720 | 40.0% |
| BINARY_OP | 20 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,060 | 58.9% |
| LOAD_CONST | 360 | 20.0% |
| CALL_BUILTIN_O | 360 | 20.0% |
| LOAD_GLOBAL | 20 | 1.1% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| BINARY_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,540 | 47.5% |
| LOAD_CONST | 4,020 | 29.2% |
| CALL_LEN | 3,180 | 23.1% |
| BINARY_OP | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,840 | 27.9% |
| RETURN_VALUE | 3,180 | 23.1% |
| LOAD_FAST_LOAD_FAST | 2,720 | 19.7% |
| STORE_FAST | 1,360 | 9.9% |
| LOAD_CONST | 1,340 | 9.7% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,300 | 85.3% |
| LOAD_CONST | 2,000 | 7.0% |
| LOAD_FAST_LOAD_FAST | 1,020 | 3.6% |
| LOAD_DEREF | 640 | 2.2% |
| BUILD_TUPLE | 240 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,100 | 38.9% |
| PUSH_EXC_INFO | 6,260 | 22.0% |
| STORE_FAST | 4,500 | 15.8% |
| PUSH_NULL | 3,140 | 11.0% |
| CALL_BUILTIN_CLASS | 1,000 | 3.5% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,280 | 60.6% |
| LOAD_FAST | 2,680 | 38.0% |
| LOAD_FAST_LOAD_FAST | 80 | 1.1% |
| BINARY_SUBSCR | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,060 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,880 | 77.9% |
| LOAD_CONST | 3,240 | 21.2% |
| BINARY_SUBSCR | 40 | 0.3% |
| LOAD_FAST_LOAD_FAST | 40 | 0.3% |
| BINARY_SUBSCR_LIST_INT | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,380 | 79.2% |
| BINARY_OP_ADD_UNICODE | 2,000 | 15.3% |
| STORE_FAST | 340 | 2.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 1.5% |
| LOAD_CONST | 100 | 0.8% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,420 | 64.1% |
| LOAD_CONST | 13,120 | 35.9% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 21,540 | 58.9% |
| LOAD_CONST | 7,640 | 20.9% |
| LOAD_FAST | 4,680 | 12.8% |
| BINARY_OP_INPLACE_ADD_UNICODE | 1,640 | 4.5% |
| CALL_BUILTIN_O | 800 | 2.2% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 29,900 | 99.6% |
| BINARY_SUBSCR | 120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,860 | 22.9% |
| LOAD_GLOBAL_MODULE | 6,280 | 20.9% |
| LOAD_FAST | 3,840 | 12.8% |
| RETURN_VALUE | 3,120 | 10.4% |
| CALL_BUILTIN_O | 3,080 | 10.3% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,242,840 | 65.5% |
| RETURN_VALUE | 2,757,120 | 34.4% |
| LOAD_FAST_LOAD_FAST | 4,800 | 0.1% |
| LOAD_FAST | 3,720 | 0.0% |
| BINARY_SUBSCR | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,009,500 | 100.0% |
| STORE_FAST | 100 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 18,740 | 45.7% |
| LOAD_CONST | 11,860 | 28.9% |
| LOAD_FAST | 7,020 | 17.1% |
| BUILD_TUPLE | 2,040 | 5.0% |
| LOAD_FAST_LOAD_FAST | 1,080 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 36,120 | 88.1% |
| POP_TOP | 4,660 | 11.4% |
| COPY_FREE_VARS | 100 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 80 | 0.2% |
| CALL_PY_EXACT_ARGS | 40 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 3,780 | 26.6% |
| LOAD_CONST | 2,600 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 1,620 | 11.4% |
| CALL_LEN | 1,340 | 9.4% |
| LOAD_FAST | 1,200 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,640 | 25.6% |
| STORE_FAST | 3,320 | 23.3% |
| LIST_APPEND | 2,560 | 18.0% |
| LOAD_CONST | 1,480 | 10.4% |
| GET_ITER | 900 | 6.3% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 29,200 | 48.9% |
| LOAD_FAST | 13,100 | 22.0% |
| LOAD_FAST_LOAD_FAST | 8,620 | 14.4% |
| LOAD_ATTR_SLOT | 3,700 | 6.2% |
| LOAD_GLOBAL_MODULE | 3,280 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 14,220 | 23.8% |
| STORE_FAST | 10,520 | 17.6% |
| TO_BOOL_BOOL | 9,260 | 15.5% |
| COPY | 8,360 | 14.0% |
| POP_JUMP_IF_NOT_NONE | 7,080 | 11.9% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,440 | 84.5% |
| LOAD_CONST | 3,300 | 9.8% |
| CALL_STR_1 | 1,000 | 3.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 320 | 1.0% |
| CALL_TUPLE_1 | 240 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 20,720 | 61.6% |
| RETURN_VALUE | 7,180 | 21.3% |
| STORE_FAST | 3,160 | 9.4% |
| BEFORE_WITH | 1,000 | 3.0% |
| MAP_ADD | 340 | 1.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,460 | 46.2% |
| LOAD_GLOBAL_MODULE | 4,480 | 13.4% |
| LOAD_CONST | 3,500 | 10.5% |
| BINARY_SUBSCR_TUPLE_INT | 3,080 | 9.2% |
| BUILD_STRING | 1,480 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,240 | 66.5% |
| STORE_FAST | 3,720 | 11.1% |
| BUILD_TUPLE | 2,940 | 8.8% |
| TO_BOOL_BOOL | 2,640 | 7.9% |
| TO_BOOL_INT | 1,220 | 3.6% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 26,780 | 62.0% |
| LOAD_GLOBAL_MODULE | 11,760 | 27.2% |
| BUILD_TUPLE | 2,160 | 5.0% |
| LOAD_NAME | 1,500 | 3.5% |
| CALL | 500 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 41,920 | 97.0% |
| TO_BOOL | 500 | 1.2% |
| RETURN_VALUE | 480 | 1.1% |
| LOAD_FAST | 240 | 0.6% |
| YIELD_VALUE | 60 | 0.1% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,042,560 | 99.9% |
| LOAD_ATTR_INSTANCE_VALUE | 15,140 | 0.1% |
| POP_JUMP_IF_TRUE | 3,180 | 0.0% |
| LOAD_NAME | 1,360 | 0.0% |
| LOAD_ATTR | 1,060 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,005,340 | 99.6% |
| LOAD_CONST | 24,800 | 0.2% |
| LOAD_FAST | 12,540 | 0.1% |
| RETURN_VALUE | 6,100 | 0.0% |
| TO_BOOL_INT | 3,700 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,100 | 48.8% |
| LOAD_CONST | 4,240 | 18.6% |
| LOAD_ATTR_INSTANCE_VALUE | 3,700 | 16.3% |
| BUILD_TUPLE | 2,600 | 11.4% |
| LOAD_FAST_CHECK | 620 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 6,640 | 29.2% |
| NOP | 4,320 | 19.0% |
| LOAD_FAST | 3,800 | 16.7% |
| EXTENDED_ARG | 3,540 | 15.6% |
| JUMP_BACKWARD | 2,320 | 10.2% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 22,840 | 48.3% |
| LOAD_FAST | 7,980 | 16.9% |
| BUILD_MAP | 5,960 | 12.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,660 | 9.9% |
| LOAD_CONST | 1,600 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 20,400 | 43.2% |
| STORE_FAST | 18,080 | 38.3% |
| POP_TOP | 5,640 | 11.9% |
| LOAD_FAST | 1,220 | 2.6% |
| SWAP | 1,000 | 2.1% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 300 | 28.3% |
| LOAD_GLOBAL_MODULE | 240 | 22.6% |
| LOAD_ATTR_METHOD_NO_DICT | 220 | 20.8% |
| LOAD_FAST_LOAD_FAST | 120 | 11.3% |
| CALL | 80 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 22.6% |
| STORE_DEREF | 220 | 20.8% |
| LOAD_ATTR_METHOD_NO_DICT | 220 | 20.8% |
| STORE_FAST | 180 | 17.0% |
| POP_TOP | 120 | 11.3% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,720 | 85.5% |
| CALL | 380 | 6.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 180 | 3.3% |
| LOAD_ATTR | 120 | 2.2% |
| LOAD_FAST | 120 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,940 | 35.1% |
| GET_ITER | 960 | 17.4% |
| BUILD_TUPLE | 700 | 12.7% |
| BINARY_OP | 400 | 7.2% |
| POP_TOP | 380 | 6.9% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,004,560 | 49.9% |
| CALL | 8,000,340 | 49.9% |
| STORE_FAST | 9,200 | 0.1% |
| LOAD_CONST | 8,740 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 3,700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 16,010,560 | 99.9% |
| RETURN_VALUE | 10,180 | 0.1% |
| LOAD_CONST | 6,660 | 0.0% |
| STORE_FAST | 2,300 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 2,000 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 16,002,980 | 66.3% |
| LOAD_FAST | 8,070,460 | 33.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,460 | 0.2% |
| LOAD_FAST_LOAD_FAST | 13,740 | 0.1% |
| CALL | 5,800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 24,141,720 | 100.0% |
| COPY_FREE_VARS | 3,680 | 0.0% |
| MAKE_CELL | 2,180 | 0.0% |
| RETURN_GENERATOR | 1,020 | 0.0% |
| RESUME | 160 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,640 | 55.4% |
| LOAD_FAST | 820 | 27.7% |
| LOAD_DEREF | 160 | 5.4% |
| CALL | 140 | 4.7% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,960 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,000 | 60.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,000 | 30.3% |
| CALL_BUILTIN_O | 300 | 9.1% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,200 | 35.1% |
| LOAD_FAST | 960 | 28.1% |
| RETURN_GENERATOR | 620 | 18.1% |
| CALL_BUILTIN_CLASS | 300 | 8.8% |
| CALL | 180 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,200 | 35.1% |
| RETURN_VALUE | 700 | 20.5% |
| LOAD_FAST | 640 | 18.7% |
| STORE_FAST | 340 | 9.9% |
| STORE_DEREF | 300 | 8.8% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,420 | 75.9% |
| LOAD_GLOBAL_MODULE | 1,020 | 17.5% |
| LOAD_CONST | 280 | 4.8% |
| CALL | 80 | 1.4% |
| LOAD_ATTR_MODULE | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,640 | 62.5% |
| PUSH_NULL | 1,040 | 17.9% |
| LOAD_FAST_LOAD_FAST | 480 | 8.2% |
| LOAD_FAST | 440 | 7.6% |
| BUILD_TUPLE | 140 | 2.4% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,700 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,700 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,037,060 | 99.9% |
| LOAD_FAST | 16,180 | 0.1% |
| CALL_LEN | 2,180 | 0.0% |
| BINARY_OP | 1,000 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,036,860 | 99.9% |
| COPY | 9,700 | 0.1% |
| POP_JUMP_IF_TRUE | 8,120 | 0.1% |
| RETURN_VALUE | 2,200 | 0.0% |
| STORE_FAST | 1,000 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 61,320 | 76.1% |
| COPY | 9,360 | 11.6% |
| LOAD_ATTR_INSTANCE_VALUE | 7,800 | 9.7% |
| LOAD_FAST | 1,000 | 1.2% |
| LOAD_FAST_LOAD_FAST | 600 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 62,520 | 77.6% |
| COPY | 10,820 | 13.4% |
| EXTENDED_ARG | 4,380 | 5.4% |
| JUMP_FORWARD | 1,640 | 2.0% |
| RETURN_VALUE | 1,160 | 1.4% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 420 | 87.5% |
| SWAP | 40 | 8.3% |
| FOR_ITER | 20 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 420 | 87.5% |
| POP_TOP | 60 | 12.5% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,220 | 50.0% |
| EXTENDED_ARG | 13,160 | 29.6% |
| GET_ITER | 8,560 | 19.3% |
| LOAD_FAST | 240 | 0.5% |
| FOR_ITER | 160 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 18,280 | 41.1% |
| STORE_FAST | 14,060 | 31.6% |
| STORE_FAST_LOAD_FAST | 3,020 | 6.8% |
| LOAD_GLOBAL_BUILTIN | 2,420 | 5.4% |
| LOAD_FAST | 2,160 | 4.9% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,000 | 92.3% |
| GET_ITER | 1,540 | 6.5% |
| SWAP | 240 | 1.0% |
| FOR_ITER | 60 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 22,000 | 92.3% |
| LOAD_FAST | 1,340 | 5.6% |
| SWAP | 260 | 1.1% |
| LOAD_CONST | 160 | 0.7% |
| JUMP_FORWARD | 40 | 0.2% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 44,580 | 69.0% |
| SWAP | 9,660 | 14.9% |
| GET_ITER | 8,820 | 13.6% |
| LOAD_FAST | 1,180 | 1.8% |
| FOR_ITER | 400 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 22,720 | 35.1% |
| STORE_FAST | 20,500 | 31.7% |
| SWAP | 9,700 | 15.0% |
| LOAD_FAST | 4,080 | 6.3% |
| STORE_NAME | 1,960 | 3.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260 | 65.0% |
| LOAD_ATTR | 140 | 35.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 45.0% |
| LOAD_CONST | 100 | 25.0% |
| GET_ITER | 40 | 10.0% |
| CALL | 20 | 5.0% |
| CONTAINS_OP | 20 | 5.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,260,780 | 90.9% |
| LOAD_FAST_LOAD_FAST | 8,014,900 | 9.1% |
| LOAD_ATTR | 2,160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,340 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 16,017,260 | 18.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,005,280 | 9.1% |
| TO_BOOL_LIST | 8,004,280 | 9.1% |
| TO_BOOL | 8,004,240 | 9.1% |
| TO_BOOL_BOOL | 8,002,480 | 9.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 16,017,260 | 99.2% |
| LOAD_FAST | 84,740 | 0.5% |
| LOAD_ATTR | 14,100 | 0.1% |
| LOAD_GLOBAL_MODULE | 13,860 | 0.1% |
| LOAD_CONST | 4,340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,045,100 | 49.8% |
| LOAD_GLOBAL_MODULE | 8,024,060 | 49.7% |
| LOAD_CONST | 57,000 | 0.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,720 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 4,660 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,005,280 | 99.3% |
| LOAD_FAST | 48,500 | 0.6% |
| LOAD_GLOBAL_MODULE | 3,700 | 0.0% |
| LOAD_ATTR | 1,140 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,015,520 | 99.4% |
| CALL_PY_EXACT_ARGS | 36,460 | 0.5% |
| LOAD_FAST_LOAD_FAST | 6,040 | 0.1% |
| LOAD_CONST | 1,260 | 0.0% |
| CALL | 620 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 99,200 | 80.2% |
| LOAD_NAME | 20,720 | 16.7% |
| LOAD_FAST | 2,720 | 2.2% |
| LOAD_ATTR | 1,040 | 0.8% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 37,260 | 30.1% |
| CALL | 29,020 | 23.5% |
| LOAD_FAST | 13,860 | 11.2% |
| LOAD_ATTR_SLOT | 12,200 | 9.9% |
| LOAD_CONST | 8,960 | 7.2% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,140 | 83.5% |
| LOAD_CONST | 600 | 16.0% |
| LOAD_ATTR | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,160 | 84.0% |
| LOAD_GLOBAL_BUILTIN | 600 | 16.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 51.9% |
| LOAD_FAST_LOAD_FAST | 240 | 44.4% |
| LOAD_ATTR | 20 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 240 | 44.4% |
| LOAD_GLOBAL_BUILTIN | 240 | 44.4% |
| LOAD_FAST | 60 | 11.1% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,300 | 91.4% |
| LOAD_ATTR_INSTANCE_VALUE | 480 | 8.3% |
| LOAD_ATTR | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,800 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 12,200 | 49.6% |
| LOAD_FAST | 9,780 | 39.8% |
| RETURN_VALUE | 1,700 | 6.9% |
| LOAD_ATTR | 360 | 1.5% |
| CALL_BUILTIN_FAST | 300 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,040 | 48.9% |
| LOAD_CONST | 4,500 | 18.3% |
| CALL_BUILTIN_FAST | 3,700 | 15.0% |
| STORE_FAST | 1,700 | 6.9% |
| LOAD_FAST_LOAD_FAST | 600 | 2.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,059,100 | 98.7% |
| STORE_FAST | 47,280 | 0.3% |
| POP_JUMP_IF_FALSE | 32,480 | 0.2% |
| LOAD_FAST | 28,500 | 0.2% |
| POP_TOP | 20,640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,153,920 | 99.2% |
| LOAD_DEREF | 30,100 | 0.2% |
| CALL_ISINSTANCE | 26,780 | 0.2% |
| LOAD_FAST_LOAD_FAST | 18,780 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 10,660 | 0.1% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,045,100 | 24.8% |
| LOAD_ATTR_METHOD_NO_DICT | 8,024,060 | 24.7% |
| LOAD_GLOBAL_MODULE | 8,009,040 | 24.7% |
| BINARY_SUBSCR | 7,999,960 | 24.7% |
| LOAD_FAST | 110,920 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,024,600 | 49.4% |
| LOAD_FAST | 8,090,900 | 25.0% |
| LOAD_GLOBAL_MODULE | 8,009,040 | 24.7% |
| LOAD_ATTR_MODULE | 99,200 | 0.3% |
| IS_OP | 43,700 | 0.1% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,120 | 82.4% |
| LOAD_DEREF | 140 | 10.3% |
| LOAD_SUPER_ATTR | 100 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,360 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,580 | 99.1% |
| LOAD_SUPER_ATTR | 240 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 23,280 | 90.2% |
| LOAD_FAST | 2,060 | 8.0% |
| CALL | 280 | 1.1% |
| CALL_PY_EXACT_ARGS | 200 | 0.8% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 141,577,220 | 77.8% |
| CALL_PY_EXACT_ARGS | 24,141,720 | 13.3% |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,500 | 4.4% |
| POP_TOP | 8,003,700 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 36,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 125,521,160 | 69.0% |
| LOAD_FAST | 32,134,740 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 16,059,100 | 8.8% |
| LOAD_FAST_LOAD_FAST | 8,029,920 | 4.4% |
| LOAD_GLOBAL_MODULE | 79,760 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| SEND | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 100.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 24,065,840 | 99.7% |
| LOAD_FAST | 74,100 | 0.3% |
| STORE_ATTR | 1,240 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 240 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,038,860 | 66.4% |
| RETURN_CONST | 8,041,160 | 33.3% |
| LOAD_FAST | 34,940 | 0.1% |
| LOAD_CONST | 9,380 | 0.0% |
| LOAD_GLOBAL_MODULE | 5,620 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,780 | 59.5% |
| LOAD_FAST | 2,620 | 32.6% |
| STORE_ATTR | 340 | 4.2% |
| LOAD_ATTR_SLOT | 300 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,940 | 73.9% |
| RETURN_CONST | 720 | 9.0% |
| LOAD_FAST_LOAD_FAST | 660 | 8.2% |
| LOAD_CONST | 640 | 8.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 1.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,000 | 54.0% |
| LOAD_CONST | 5,240 | 16.6% |
| LOAD_FAST_LOAD_FAST | 3,100 | 9.8% |
| LOAD_ATTR_INSTANCE_VALUE | 2,440 | 7.8% |
| BINARY_OP_ADD_UNICODE | 2,000 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,580 | 36.8% |
| JUMP_BACKWARD | 8,280 | 26.3% |
| LOAD_GLOBAL_MODULE | 3,220 | 10.2% |
| NOP | 2,400 | 7.6% |
| LOAD_NAME | 1,440 | 4.6% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,320 | 52.8% |
| LOAD_FAST_LOAD_FAST | 2,740 | 33.5% |
| LOAD_FAST | 1,080 | 13.2% |
| STORE_SUBSCR | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,360 | 53.3% |
| EXTENDED_ARG | 1,780 | 21.8% |
| LOAD_NAME | 1,380 | 16.9% |
| RETURN_CONST | 540 | 6.6% |
| LOAD_FAST | 120 | 1.5% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,001,020 | 99.1% |
| TO_BOOL_NONE | 68,840 | 0.9% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,001,040 | 99.1% |
| TO_BOOL_NONE | 68,860 | 0.9% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,002,480 | 97.3% |
| COPY | 49,840 | 0.6% |
| RETURN_VALUE | 42,940 | 0.5% |
| CALL_ISINSTANCE | 41,920 | 0.5% |
| LOAD_FAST | 26,300 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,137,020 | 98.9% |
| POP_JUMP_IF_TRUE | 87,140 | 1.1% |
| EXTENDED_ARG | 3,420 | 0.0% |
| UNARY_NOT | 60 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,860 | 48.9% |
| LOAD_FAST | 5,820 | 24.0% |
| CALL_LEN | 3,700 | 15.3% |
| COPY | 1,240 | 5.1% |
| CALL_BUILTIN_O | 1,220 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,980 | 61.8% |
| POP_JUMP_IF_TRUE | 7,680 | 31.7% |
| UNARY_NOT | 1,560 | 6.4% |
| TO_BOOL_BOOL | 20 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,004,280 | 99.9% |
| LOAD_FAST | 4,820 | 0.1% |
| LOAD_ATTR | 280 | 0.0% |
| TO_BOOL | 100 | 0.0% |
| LOAD_ATTR_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,006,960 | 100.0% |
| POP_JUMP_IF_TRUE | 2,340 | 0.0% |
| UNARY_NOT | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 7,998,960 | 98.9% |
| TO_BOOL_ALWAYS_TRUE | 68,860 | 0.9% |
| LOAD_FAST | 11,780 | 0.1% |
| COPY | 3,800 | 0.0% |
| TO_BOOL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,010,740 | 99.1% |
| TO_BOOL_ALWAYS_TRUE | 68,840 | 0.9% |
| POP_JUMP_IF_TRUE | 4,360 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 20,400 | 66.5% |
| COPY | 5,240 | 17.1% |
| LOAD_FAST | 4,900 | 16.0% |
| TO_BOOL | 60 | 0.2% |
| LOAD_GLOBAL_MODULE | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 25,100 | 81.8% |
| POP_JUMP_IF_TRUE | 5,580 | 18.2% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 2,000 | 52.9% |
| LOAD_FAST | 940 | 24.9% |
| RETURN_VALUE | 420 | 11.1% |
| BUILD_TUPLE | 300 | 7.9% |
| BINARY_SUBSCR_TUPLE_INT | 120 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,380 | 63.0% |
| STORE_FAST | 1,100 | 29.1% |
| STORE_DEREF | 300 | 7.9% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 31,440 | 52.4% |
| FOR_ITER_LIST | 18,280 | 30.5% |
| RETURN_VALUE | 9,220 | 15.4% |
| UNPACK_SEQUENCE | 320 | 0.5% |
| LOAD_CONST | 260 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 47,560 | 79.3% |
| STORE_FAST | 7,640 | 12.7% |
| STORE_NAME | 4,540 | 7.6% |
| STORE_DEREF | 180 | 0.3% |
| LOAD_FAST | 60 | 0.1% |


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
|     deferred | 8,037,820 | 49.8% |
|          hit | 8,083,320 | 50.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 500 | 11.6% |
| Failure | 3,820 | 88.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 2,340 | 61.3% |
| and int | 740 | 19.4% |
| or | 300 | 7.9% |
| add other | 220 | 5.8% |
| power | 80 | 2.1% |
| add different types | 60 | 1.6% |
| multiply different types | 60 | 1.6% |
| and different types | 20 | 0.5% |


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
|     deferred | 8,010,400 | 98.5% |
|          hit | 114,960 | 1.4% |
|         miss | 2,440 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 13.0% |
| Failure | 2,280 | 87.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence int | 2,140 | 93.9% |
| out of range | 80 | 3.5% |
| code complex parameters | 40 | 1.8% |
| other | 20 | 0.9% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,194,140 | 20.0% |
|          hit | 64,583,300 | 79.9% |
|         miss | 27,240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,500 | 43.7% |
| Failure | 8,360 | 56.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class no vectorcall | 2,660 | 31.8% |
| other | 2,280 | 27.3% |
| meth descr varargs | 1,380 | 16.5% |
| code complex parameters | 460 | 5.5% |
| cfunc noargs | 440 | 5.3% |
| cfunc varargs keywords | 240 | 2.9% |
| method wrapper | 200 | 2.4% |
| wrong number arguments | 140 | 1.7% |
| class mutable | 140 | 1.7% |
| cfunc varargs | 100 | 1.2% |
| no dict | 60 | 0.7% |
| meth descr method fastcall keywords | 60 | 0.7% |
| operator wrapper | 60 | 0.7% |
| init not simple | 60 | 0.7% |
| meth descr varargs keywords | 40 | 0.5% |
| cmethod | 20 | 0.2% |
| init not python | 20 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,580 | 0.1% |
|          hit | 16,139,760 | 99.9% |
|         miss | 360 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 66.1% |
| Failure | 400 | 33.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 140 | 35.0% |
| list | 60 | 15.0% |
| other | 40 | 10.0% |
| different types | 40 | 10.0% |
| tuple | 40 | 10.0% |
| bool | 40 | 10.0% |
| set | 20 | 5.0% |
| baseobject | 20 | 5.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 68,020 | 33.3% |
|          hit | 130,420 | 63.8% |
|         miss | 3,000 | 1.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 640 | 21.5% |
| Failure | 2,340 | 78.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict values | 840 | 35.9% |
| dict items | 700 | 29.9% |
| seq iter | 260 | 11.1% |
| set | 180 | 7.7% |
| itertools | 180 | 7.7% |
| map | 120 | 5.1% |
| dict keys | 20 | 0.9% |
| enumerate | 20 | 0.9% |
| zip | 20 | 0.9% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 106,380 | 0.1% |
|        deopt | 360 | 0.0% |
|          hit | 112,627,480 | 99.9% |
|         miss | 14,640 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,280 | 60.4% |
| Failure | 4,120 | 39.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 2,540 | 61.7% |
| method | 460 | 11.2% |
| not managed dict | 340 | 8.3% |
| module attr not found | 200 | 4.9% |
| has managed dict | 160 | 3.9% |
| shadowed | 120 | 2.9% |
| class attr descriptor | 80 | 1.9% |
| class method obj | 60 | 1.5% |
| non overriding descriptor | 40 | 1.0% |
| builtin class method | 40 | 1.0% |
| class attr simple | 40 | 1.0% |
| overridden | 20 | 0.5% |
| mutable class | 20 | 0.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 9,080 | 0.0% |
|        deopt | 2,620 | 0.0% |
|          hit | 48,571,220 | 99.7% |
|         miss | 130,160 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,340 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 400 | 1.4% |
|          hit | 27,180 | 97.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 100.0% |
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
|     deferred | 133,515,700 | 100.0% |
|          hit | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 0.1% |
| Failure | 33,180 | 99.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 33,180 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 32,960 | 0.1% |
|          hit | 24,137,040 | 99.8% |
|         miss | 12,680 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,760 | 45.6% |
| Failure | 2,100 | 54.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 1,560 | 74.3% |
| not in keys | 160 | 7.6% |
| overriding descriptor | 140 | 6.7% |
| no dict | 80 | 3.8% |
| not managed dict | 80 | 3.8% |
| class attr simple | 60 | 2.9% |
| mutable class | 20 | 1.0% |


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
|     deferred | 18,340 | 31.2% |
|          hit | 39,660 | 67.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 33.3% |
| Failure | 480 | 66.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 440 | 91.7% |
| py simple | 40 | 8.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,873,100 | 19.5% |
|          hit | 25,139,600 | 62.1% |
|         miss | 7,306,360 | 18.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140,420 | 98.4% |
| Failure | 2,340 | 1.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 2,180 | 93.2% |
| mapping | 60 | 2.6% |
| sequence | 40 | 1.7% |
| dict | 20 | 0.9% |
| number | 20 | 0.9% |
| tuple | 20 | 0.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 300 | 0.5% |
|          hit | 63,760 | 99.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,740,961,720 | 70.1% |
| Not specialized | 254,861,960 | 10.3% |
| Specialized hits | 481,467,000 | 19.4% |
| Specialized misses | 7,508,300 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| SEND | 133,515,700 | 76.8% |
| CALL | 16,194,140 | 9.3% |
| BINARY_OP | 8,037,820 | 4.6% |
| BINARY_SUBSCR | 8,010,400 | 4.6% |
| TO_BOOL | 7,873,100 | 4.5% |
| LOAD_ATTR | 106,380 | 0.1% |
| FOR_ITER | 68,020 | 0.0% |
| STORE_ATTR | 32,960 | 0.0% |
| STORE_SUBSCR | 18,340 | 0.0% |
| COMPARE_OP | 16,580 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL_NONE | 3,653,900 | 48.6% |
| TO_BOOL_ALWAYS_TRUE | 3,650,500 | 48.5% |
| LOAD_GLOBAL_MODULE | 73,640 | 1.0% |
| LOAD_GLOBAL_BUILTIN | 56,520 | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 12,620 | 0.2% |
| RESUME | 11,420 | 0.2% |
| RESUME_CHECK | 11,420 | 0.2% |
| CALL_PY_EXACT_ARGS | 9,640 | 0.1% |
| LOAD_ATTR_MODULE | 9,260 | 0.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,860 | 0.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 157,618,720 | 83.0% |
| Calls to Python functions inlined | 32,253,600 | 17.0% |
| Calls via PyEval_EvalFrame (total) | 157,618,720 | 83.0% |
| Calls via PyEval_EvalFrame (vector) | 24,093,980 | 12.7% |
| Calls via PyEval_EvalFrame (generator) | 133,524,740 | 70.3% |
| Calls via PyEval_EvalFrame (legacy) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 24,088,520 | 12.7% |
| Calls via PyEval_EvalFrame (build class) | 4,140 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 30,240 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 1,580 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 16,013,620 | 8.4% |
| Calls via PyEval_EvalFrame (method) | 2,800 | 0.0% |
| Frame objects created | 5,255,320 | 2.8% |
| Frames pushed | 40,208,460 | 21.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 259,447,380 | 52.3% |
| Frees to freelist | 259,444,140 |  |
| Allocations | 236,282,292 | 47.7% |
| Allocations to 512 bytes | 236,242,360 | 47.7% |
| Allocations to 4 kbytes | 37,052 | 0.0% |
| Allocations over 4 kbytes | 2,880 | 0.0% |
| Frees | 235,700,487 |  |
| New values | 13,460 |  |
| Interpreter increfs | 1,009,021,380 | 58.7% |
| Interpreter decrefs | 1,463,527,620 | 62.1% |
| Increfs | 710,343,158 | 41.3% |
| Decrefs | 891,888,925 | 37.9% |
| Materialize dict (on request) | 240 | 1.8% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 100 | 0.7% |
| Method cache hits | 181,772 |  |
| Method cache misses | 52,708 |  |
| Method cache collisions | 63,860 |  |
| Method cache dunder hits | 8,332,550 |  |
| Method cache dunder misses | 24,610 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 10,660 | 3,600 | 60,631,080 |
| 1 | 960 | 0 | 62,009,640 |
| 2 | 80 | 0 | 50,041,520 |


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
