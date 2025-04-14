
# Pystats results

- benchmark: async_generators
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 286,877,480 | 12.9% | 12.9% |  |
| RESUME_CHECK | 181,806,720 | 8.2% | 21.0% | 0.0% |
| STORE_FAST | 157,867,320 | 7.1% | 28.1% |  |
| POP_TOP | 157,742,960 | 7.1% | 35.2% |  |
| INTERPRETER_EXIT | 157,610,020 | 7.1% | 42.3% |  |
| SEND | 133,548,900 | 6.0% | 48.3% |  |
| ENTER_EXECUTOR | 125,597,900 | 5.6% | 53.9% |  |
| YIELD_VALUE | 125,521,100 | 5.6% | 59.5% |  |
| CALL_INTRINSIC_1 | 125,519,180 | 5.6% | 65.2% |  |
| END_SEND | 125,515,760 | 5.6% | 70.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 88,213,360 | 4.0% | 74.7% | 0.0% |
| LOAD_CONST | 56,603,660 | 2.5% | 77.3% |  |
| POP_JUMP_IF_FALSE | 56,339,240 | 2.5% | 79.8% |  |
| LOAD_FAST_LOAD_FAST | 48,210,600 | 2.2% | 82.0% |  |
| RETURN_CONST | 48,136,240 | 2.2% | 84.1% |  |
| LOAD_GLOBAL_MODULE | 32,367,220 | 1.5% | 85.6% | 0.2% |
| CALL_PY_EXACT_ARGS | 24,118,580 | 1.1% | 86.7% | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 24,089,300 | 1.1% | 87.8% | 0.1% |
| LOAD_GLOBAL_BUILTIN | 16,235,780 | 0.7% | 88.5% | 0.3% |
| CALL | 16,195,980 | 0.7% | 89.2% |  |
| RETURN_VALUE | 16,170,260 | 0.7% | 89.9% |  |
| LOAD_ATTR_METHOD_NO_DICT | 16,129,280 | 0.7% | 90.7% |  |
| CALL_LEN | 16,053,000 | 0.7% | 91.4% |  |
| COMPARE_OP_INT | 16,049,280 | 0.7% | 92.1% | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 16,031,120 | 0.7% | 92.8% | 0.0% |
| BINARY_SLICE | 16,015,920 | 0.7% | 93.5% |  |
| TO_BOOL_BOOL | 8,177,500 | 0.4% | 93.9% | 0.0% |
| PUSH_NULL | 8,099,580 | 0.4% | 94.3% |  |
| TO_BOOL_NONE | 8,080,840 | 0.4% | 94.6% | 45.2% |
| TO_BOOL_ALWAYS_TRUE | 8,069,900 | 0.4% | 95.0% | 45.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,040,720 | 0.4% | 95.4% | 0.0% |
| BINARY_OP | 8,031,400 | 0.4% | 95.7% |  |
| POP_JUMP_IF_NONE | 8,029,120 | 0.4% | 96.1% |  |
| BINARY_OP_ADD_INT | 8,017,900 | 0.4% | 96.4% |  |
| TO_BOOL | 8,015,620 | 0.4% | 96.8% |  |
| BINARY_SUBSCR | 8,011,840 | 0.4% | 97.2% |  |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,540 | 0.4% | 97.5% | 0.0% |
| EXIT_INIT_CHECK | 8,009,440 | 0.4% | 97.9% |  |
| TO_BOOL_LIST | 8,008,500 | 0.4% | 98.2% | 0.0% |
| RETURN_GENERATOR | 8,003,520 | 0.4% | 98.6% |  |
| GET_ANEXT | 8,000,960 | 0.4% | 98.9% |  |
| END_ASYNC_FOR | 8,000,000 | 0.4% | 99.3% |  |
| GET_AITER | 8,000,000 | 0.4% | 99.7% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 5,248,700 | 0.2% | 99.9% |  |
| POP_JUMP_IF_TRUE | 126,960 | 0.0% | 99.9% |  |
| LOAD_ATTR | 104,440 | 0.0% | 99.9% |  |
| LOAD_ATTR_MODULE | 103,960 | 0.0% | 99.9% | 8.9% |
| NOP | 85,460 | 0.0% | 99.9% |  |
| STORE_NAME | 82,380 | 0.0% | 99.9% |  |
| CONTAINS_OP | 70,000 | 0.0% | 99.9% |  |
| POP_JUMP_IF_NOT_NONE | 64,740 | 0.0% | 99.9% |  |
| COPY | 53,880 | 0.0% | 99.9% |  |
| COMPARE_OP_STR | 50,900 | 0.0% | 99.9% | 0.5% |
| MAKE_FUNCTION | 50,560 | 0.0% | 99.9% |  |
| LOAD_DEREF | 49,260 | 0.0% | 99.9% |  |
| CALL_BUILTIN_FAST | 48,540 | 0.0% | 99.9% | 1.4% |
| LOAD_NAME | 48,480 | 0.0% | 99.9% |  |
| SWAP | 47,440 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 43,360 | 0.0% | 99.9% |  |
| FOR_ITER_TUPLE | 42,720 | 0.0% | 100.0% |  |
| IS_OP | 41,620 | 0.0% | 100.0% |  |
| GET_ITER | 40,760 | 0.0% | 100.0% |  |
| BUILD_LIST | 37,380 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 35,960 | 0.0% | 100.0% | 2.0% |
| CALL_ISINSTANCE | 35,880 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 35,340 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 35,200 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 34,560 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 30,740 | 0.0% | 100.0% | 6.1% |
| JUMP_BACKWARD | 28,780 | 0.0% | 100.0% |  |
| STORE_ATTR | 28,300 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 27,760 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 26,940 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 25,500 | 0.0% | 100.0% | 26.9% |
| LOAD_SUPER_ATTR_METHOD | 24,980 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,260 | 0.0% | 100.0% | 12.6% |
| LOAD_ATTR_SLOT | 24,100 | 0.0% | 100.0% | 1.4% |
| FOR_ITER_LIST | 22,960 | 0.0% | 100.0% | 3.1% |
| CALL_LIST_APPEND | 22,680 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 22,520 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 21,960 | 0.0% | 100.0% | 4.7% |
| STORE_FAST_STORE_FAST | 21,280 | 0.0% | 100.0% |  |
| FOR_ITER | 19,400 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 19,200 | 0.0% | 100.0% |  |
| BEFORE_WITH | 18,100 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 18,040 | 0.0% | 100.0% | 1.3% |
| COMPARE_OP | 17,680 | 0.0% | 100.0% |  |
| BUILD_MAP | 17,640 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 17,500 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 17,380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 15,280 | 0.0% | 100.0% | 14.5% |
| BINARY_OP_ADD_UNICODE | 14,820 | 0.0% | 100.0% |  |
| CALL_KW | 14,220 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 14,200 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 13,960 | 0.0% | 100.0% |  |
| LIST_APPEND | 13,640 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 12,560 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 10,840 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 10,700 | 0.0% | 100.0% |  |
| RESUME | 9,200 | 0.0% | 100.0% | 123.9% |
| FORMAT_SIMPLE | 8,840 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 8,840 | 0.0% | 100.0% |  |
| MAKE_CELL | 8,120 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 8,040 | 0.0% | 100.0% | 1.5% |
| CHECK_EXC_MATCH | 7,980 | 0.0% | 100.0% |  |
| POP_EXCEPT | 7,980 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 7,980 | 0.0% | 100.0% |  |
| MAP_ADD | 7,680 | 0.0% | 100.0% |  |
| IMPORT_NAME | 7,200 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 7,060 | 0.0% | 100.0% |  |
| DICT_MERGE | 6,540 | 0.0% | 100.0% |  |
| BUILD_STRING | 6,460 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 6,340 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 6,100 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 5,800 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 5,420 | 0.0% | 100.0% |  |
| IMPORT_FROM | 4,920 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 4,460 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 4,220 | 0.0% | 100.0% |  |
| STORE_DEREF | 4,040 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 4,020 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,860 | 0.0% | 100.0% | 11.4% |
| UNPACK_SEQUENCE_TUPLE | 3,780 | 0.0% | 100.0% |  |
| LIST_EXTEND | 3,740 | 0.0% | 100.0% |  |
| CALL_STR_1 | 3,300 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 3,160 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 3,060 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 3,000 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 2,680 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,180 | 0.0% | 100.0% |  |
| RERAISE | 2,000 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 1,800 | 0.0% | 100.0% |  |
| BUILD_SLICE | 1,540 | 0.0% | 100.0% |  |
| UNARY_NOT | 1,520 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 1,360 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 1,260 | 0.0% | 100.0% | 4.8% |
| DELETE_SUBSCR | 1,220 | 0.0% | 100.0% |  |
| BUILD_SET | 1,080 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,060 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 740 | 0.0% | 100.0% |  |
| UNARY_INVERT | 720 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 640 | 0.0% | 100.0% | 3.1% |
| UNPACK_SEQUENCE | 580 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 540 | 0.0% | 100.0% |  |
| FOR_ITER_GEN | 480 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 420 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 400 | 0.0% | 100.0% |  |
| DELETE_NAME | 300 | 0.0% | 100.0% |  |
| DICT_UPDATE | 300 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 240 | 0.0% | 100.0% |  |
| STORE_SLICE | 160 | 0.0% | 100.0% |  |
| DELETE_FAST | 160 | 0.0% | 100.0% |  |
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
| STORE_FAST LOAD_FAST | 141,660,640 | 6.4% | 6.4% |
| CACHE RESUME_CHECK | 141,572,440 | 6.4% | 12.7% |
| RESUME_CHECK POP_TOP | 125,520,720 | 5.6% | 18.3% |
| YIELD_VALUE INTERPRETER_EXIT | 125,520,680 | 5.6% | 24.0% |
| END_SEND STORE_FAST | 125,515,680 | 5.6% | 29.6% |
| CALL_INTRINSIC_1 YIELD_VALUE | 125,515,680 | 5.6% | 35.2% |
| SEND END_SEND | 125,515,680 | 5.6% | 40.9% |
| ENTER_EXECUTOR SEND | 125,514,720 | 5.6% | 46.5% |
| POP_TOP ENTER_EXECUTOR | 117,529,460 | 5.3% | 51.8% |
| LOAD_FAST CALL_INTRINSIC_1 | 117,515,680 | 5.3% | 57.0% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 80,195,400 | 3.6% | 60.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 42,910,980 | 1.9% | 62.6% |
| LOAD_FAST LOAD_CONST | 32,157,360 | 1.4% | 64.0% |
| RESUME_CHECK LOAD_FAST | 32,100,100 | 1.4% | 65.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 24,111,660 | 1.1% | 66.5% |
| RETURN_CONST INTERPRETER_EXIT | 24,063,900 | 1.1% | 67.6% |
| POP_TOP RETURN_CONST | 24,056,820 | 1.1% | 68.7% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 24,038,100 | 1.1% | 69.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 16,127,800 | 0.7% | 70.5% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 16,052,880 | 0.7% | 71.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 16,033,640 | 0.7% | 71.9% |
| LOAD_CONST COMPARE_OP_INT | 16,032,280 | 0.7% | 72.7% |
| LOAD_FAST CALL_LEN | 16,032,140 | 0.7% | 73.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 16,024,660 | 0.7% | 74.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 16,020,900 | 0.7% | 74.8% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 16,017,320 | 0.7% | 75.5% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 16,009,020 | 0.7% | 76.3% |
| BINARY_SLICE CALL_PY_EXACT_ARGS | 16,002,980 | 0.7% | 77.0% |
| CALL_LEN STORE_FAST | 16,002,640 | 0.7% | 77.7% |
| POP_JUMP_IF_FALSE RETURN_CONST | 13,267,400 | 0.6% | 78.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,102,840 | 0.4% | 78.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 8,075,640 | 0.4% | 79.0% |
| POP_TOP LOAD_FAST | 8,059,880 | 0.4% | 79.4% |
| LOAD_FAST PUSH_NULL | 8,053,840 | 0.4% | 79.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 8,051,500 | 0.4% | 80.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 8,049,580 | 0.4% | 80.5% |
| LOAD_CONST LOAD_FAST | 8,049,100 | 0.4% | 80.8% |
| RETURN_CONST POP_TOP | 8,042,480 | 0.4% | 81.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 8,040,600 | 0.4% | 81.5% |
| CALL STORE_FAST | 8,026,240 | 0.4% | 81.9% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 8,024,660 | 0.4% | 82.3% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 8,019,620 | 0.4% | 82.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 8,015,520 | 0.4% | 83.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,015,440 | 0.4% | 83.3% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,014,880 | 0.4% | 83.7% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 8,014,460 | 0.4% | 84.1% |
| LOAD_CONST BINARY_SLICE | 8,013,180 | 0.4% | 84.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 8,012,980 | 0.4% | 84.8% |
| POP_JUMP_IF_NONE LOAD_FAST | 8,011,740 | 0.4% | 85.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 8,010,860 | 0.4% | 85.5% |
| RETURN_VALUE RETURN_VALUE | 8,010,500 | 0.4% | 85.9% |
| EXIT_INIT_CHECK RETURN_VALUE | 8,009,440 | 0.4% | 86.2% |
| RETURN_CONST EXIT_INIT_CHECK | 8,009,440 | 0.4% | 86.6% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 8,009,440 | 0.4% | 86.9% |
| PUSH_NULL CALL | 8,009,380 | 0.4% | 87.3% |
| TO_BOOL POP_JUMP_IF_FALSE | 8,008,620 | 0.4% | 87.7% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 8,007,020 | 0.4% | 88.0% |
| LOAD_CONST BINARY_OP | 8,006,860 | 0.4% | 88.4% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,006,260 | 0.4% | 88.7% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 8,005,920 | 0.4% | 89.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 8,005,280 | 0.4% | 89.4% |
| BINARY_OP STORE_FAST | 8,004,800 | 0.4% | 89.8% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 8,004,280 | 0.4% | 90.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 8,004,240 | 0.4% | 90.5% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 8,003,860 | 0.4% | 90.9% |
| CACHE POP_TOP | 8,003,380 | 0.4% | 91.2% |
| POP_TOP RESUME_CHECK | 8,003,340 | 0.4% | 91.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 8,002,480 | 0.4% | 92.0% |
| STORE_FAST ENTER_EXECUTOR | 8,002,400 | 0.4% | 92.3% |
| LOAD_FAST BINARY_SLICE | 8,002,260 | 0.4% | 92.7% |
| BINARY_OP_ADD_INT LOAD_CONST | 8,001,980 | 0.4% | 93.0% |
| LOAD_ATTR_INSTANCE_VALUE CALL | 8,001,660 | 0.4% | 93.4% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 8,001,040 | 0.4% | 93.8% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_ALWAYS_TRUE | 8,001,020 | 0.4% | 94.1% |
| LOAD_CONST SEND | 8,001,000 | 0.4% | 94.5% |
| GET_ANEXT LOAD_CONST | 8,000,960 | 0.4% | 94.8% |
| CALL CALL_METHOD_DESCRIPTOR_O | 8,000,340 | 0.4% | 95.2% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 8,000,040 | 0.4% | 95.6% |
| CACHE RETURN_GENERATOR | 8,000,000 | 0.4% | 95.9% |
| GET_AITER GET_ANEXT | 8,000,000 | 0.4% | 96.3% |
| RETURN_GENERATOR INTERPRETER_EXIT | 8,000,000 | 0.4% | 96.6% |
| SEND END_ASYNC_FOR | 8,000,000 | 0.4% | 97.0% |
| LOAD_ATTR_INSTANCE_VALUE CALL_INTRINSIC_1 | 7,999,980 | 0.4% | 97.3% |
| BINARY_SUBSCR LOAD_GLOBAL_MODULE | 7,999,960 | 0.4% | 97.7% |
| LOAD_ATTR_INSTANCE_VALUE GET_AITER | 7,999,880 | 0.4% | 98.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_NONE | 7,998,960 | 0.4% | 98.4% |
| JUMP_BACKWARD_NO_INTERRUPT LOAD_FAST | 5,248,680 | 0.2% | 98.7% |
| RETURN_VALUE LOAD_FAST_LOAD_FAST | 5,242,880 | 0.2% | 98.9% |
| RETURN_CONST CALL_ALLOC_AND_ENTER_INIT | 5,242,840 | 0.2% | 99.1% |
| END_ASYNC_FOR JUMP_BACKWARD_NO_INTERRUPT | 5,242,800 | 0.2% | 99.4% |
| END_ASYNC_FOR RETURN_CONST | 2,757,200 | 0.1% | 99.5% |
| RETURN_CONST LOAD_FAST_LOAD_FAST | 2,757,200 | 0.1% | 99.6% |
| RETURN_VALUE CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 0.1% | 99.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 96,800 | 0.0% | 99.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 94,740 | 0.0% | 99.7% |
| LOAD_CONST LOAD_CONST | 91,640 | 0.0% | 99.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 77,940 | 0.0% | 99.8% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 71,160 | 0.0% | 99.8% |
| TO_BOOL_ALWAYS_TRUE TO_BOOL_NONE | 68,860 | 0.0% | 99.8% |
| TO_BOOL_NONE TO_BOOL_ALWAYS_TRUE | 68,840 | 0.0% | 99.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,013,180 | 50.0% |
| LOAD_FAST | 8,002,260 | 50.0% |
| BINARY_OP_ADD_INT | 460 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 16,002,980 | 99.9% |
| STORE_FAST | 4,180 | 0.0% |
| BUILD_TUPLE | 2,000 | 0.0% |
| LOAD_DEREF | 2,000 | 0.0% |
| LOAD_FAST | 1,580 | 0.0% |


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
| RESUME_CHECK | 141,572,440 | 89.8% |
| POP_TOP | 8,003,380 | 5.1% |
| RETURN_GENERATOR | 8,000,000 | 5.1% |
| COPY_FREE_VARS | 29,940 | 0.0% |
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
| ENTER_EXECUTOR | 420 | 19.3% |
| LOAD_FAST_LOAD_FAST | 80 | 3.7% |
| RETURN_VALUE | 20 | 0.9% |
| BINARY_OP | 20 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,680 | 77.1% |
| ENTER_EXECUTOR | 500 | 22.9% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,000,040 | 99.9% |
| LOAD_CONST | 6,400 | 0.1% |
| BINARY_SUBSCR | 2,300 | 0.0% |
| BUILD_SLICE | 1,540 | 0.0% |
| LOAD_FAST | 980 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,999,960 | 99.9% |
| SWAP | 3,720 | 0.0% |
| BINARY_SUBSCR | 2,300 | 0.0% |
| GET_ITER | 1,320 | 0.0% |
| LOAD_CONST | 1,260 | 0.0% |


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
| JUMP_BACKWARD_NO_INTERRUPT | 5,242,800 | 65.5% |
| RETURN_CONST | 2,757,200 | 34.5% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 100.0% |


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
| RETURN_CONST | 8,009,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,009,440 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,760 | 42.5% |
| CONVERT_VALUE | 2,680 | 30.3% |
| LOAD_ATTR | 1,620 | 18.3% |
| LOAD_ATTR_MODULE | 360 | 4.1% |
| STORE_FAST_LOAD_FAST | 300 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,420 | 83.9% |
| BUILD_STRING | 1,380 | 15.6% |
| LOAD_FAST | 40 | 0.5% |


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
| GET_AITER | 8,000,000 | 100.0% |
| JUMP_BACKWARD | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,000,960 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,820 | 58.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,940 | 9.7% |
| LOAD_GLOBAL_MODULE | 2,000 | 4.9% |
| BUILD_TUPLE | 1,460 | 3.6% |
| BINARY_SUBSCR | 1,320 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 10,480 | 25.7% |
| FOR_ITER_TUPLE | 8,540 | 21.0% |
| FOR_ITER_LIST | 8,200 | 20.1% |
| EXTENDED_ARG | 5,540 | 13.6% |
| CALL_PY_EXACT_ARGS | 3,140 | 7.7% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 125,520,680 | 79.6% |
| RETURN_CONST | 24,063,900 | 15.3% |
| RETURN_GENERATOR | 8,000,000 | 5.1% |
| RETURN_VALUE | 25,440 | 0.0% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 3,640 | 86.3% |
| POP_TOP | 200 | 4.7% |
| LOAD_NAME | 120 | 2.8% |
| RETURN_VALUE | 100 | 2.4% |
| STORE_ATTR | 60 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,220 | 100.0% |


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
| LOAD_CONST | 50,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 26,000 | 51.4% |
| SET_FUNCTION_ATTRIBUTE | 16,000 | 31.6% |
| LOAD_CONST | 4,340 | 8.6% |
| CALL | 2,120 | 4.2% |
| LOAD_FAST | 620 | 1.2% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 28,620 | 33.5% |
| POP_TOP | 15,980 | 18.7% |
| CALL_LIST_APPEND | 7,460 | 8.7% |
| POP_JUMP_IF_FALSE | 6,600 | 7.7% |
| RESUME_CHECK | 6,560 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 43,600 | 51.0% |
| LOAD_GLOBAL_MODULE | 18,860 | 22.1% |
| LOAD_CONST | 9,860 | 11.5% |
| NOP | 6,340 | 7.4% |
| LOAD_FAST_LOAD_FAST | 4,160 | 4.9% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,960 | 62.2% |
| COPY | 1,040 | 13.0% |
| CALL_LIST_APPEND | 700 | 8.8% |
| POP_TOP | 640 | 8.0% |
| POP_JUMP_IF_FALSE | 240 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 5,540 | 69.4% |
| RERAISE | 1,040 | 13.0% |
| RETURN_CONST | 540 | 6.8% |
| EXTENDED_ARG | 400 | 5.0% |
| JUMP_FORWARD | 240 | 3.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 125,520,720 | 79.6% |
| CALL_METHOD_DESCRIPTOR_O | 16,009,020 | 10.1% |
| RETURN_CONST | 8,042,480 | 5.1% |
| CACHE | 8,003,380 | 5.1% |
| CALL | 54,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 117,529,460 | 74.5% |
| RETURN_CONST | 24,056,820 | 15.3% |
| LOAD_FAST | 8,059,880 | 5.1% |
| RESUME_CHECK | 8,003,340 | 5.1% |
| NOP | 15,980 | 0.0% |


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
| LOAD_FAST | 8,053,840 | 99.4% |
| LOAD_ATTR_MODULE | 18,320 | 0.2% |
| LOAD_ATTR | 4,960 | 0.1% |
| LOAD_DEREF | 4,940 | 0.1% |
| LOAD_NAME | 4,640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 8,009,380 | 98.9% |
| LOAD_FAST | 45,300 | 0.6% |
| LOAD_CONST | 17,560 | 0.2% |
| LOAD_FAST_LOAD_FAST | 11,100 | 0.1% |
| LOAD_GLOBAL_MODULE | 8,080 | 0.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 8,000,000 | 100.0% |
| COPY_FREE_VARS | 2,520 | 0.0% |
| CALL_PY_EXACT_ARGS | 900 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 8,000,000 | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,000 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 480 | 0.0% |
| CALL_TUPLE_1 | 420 | 0.0% |
| CALL | 260 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,010,500 | 49.5% |
| EXIT_INIT_CHECK | 8,009,440 | 49.5% |
| LOAD_FAST | 39,200 | 0.2% |
| CALL | 19,760 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 10,380 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,010,500 | 49.5% |
| LOAD_FAST_LOAD_FAST | 5,242,880 | 32.4% |
| CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 17.1% |
| STORE_FAST | 46,120 | 0.3% |
| TO_BOOL_BOOL | 37,620 | 0.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,760 | 45.2% |
| LOAD_FAST | 1,080 | 17.7% |
| LOAD_CONST | 1,060 | 17.4% |
| BINARY_OP | 580 | 9.5% |
| STORE_SUBSCR | 320 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 1,320 | 21.6% |
| LOAD_FAST | 1,240 | 20.3% |
| RETURN_CONST | 960 | 15.7% |
| EXTENDED_ARG | 840 | 13.8% |
| JUMP_BACKWARD | 820 | 13.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,004,240 | 99.9% |
| LOAD_FAST | 4,040 | 0.1% |
| TO_BOOL | 2,320 | 0.0% |
| CALL | 1,340 | 0.0% |
| LOAD_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,008,620 | 99.9% |
| TO_BOOL | 2,320 | 0.0% |
| POP_JUMP_IF_TRUE | 2,000 | 0.0% |
| TO_BOOL_BOOL | 1,840 | 0.0% |
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
| TO_BOOL_INT | 1,180 | 77.6% |
| TO_BOOL_LIST | 240 | 15.8% |
| TO_BOOL_BOOL | 60 | 3.9% |
| TO_BOOL | 40 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,000 | 65.8% |
| STORE_FAST | 280 | 18.4% |
| CALL_PY_EXACT_ARGS | 240 | 15.8% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,006,860 | 99.7% |
| LOAD_GLOBAL_MODULE | 11,380 | 0.1% |
| BINARY_OP | 3,640 | 0.0% |
| LOAD_FAST_LOAD_FAST | 2,300 | 0.0% |
| LOAD_FAST | 1,380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,004,800 | 99.7% |
| TO_BOOL_INT | 11,620 | 0.1% |
| BINARY_OP | 3,640 | 0.0% |
| LOAD_FAST | 2,060 | 0.0% |
| LOAD_CONST | 1,880 | 0.0% |


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
| SWAP | 10,260 | 27.4% |
| LOAD_ATTR_INSTANCE_VALUE | 4,800 | 12.8% |
| STORE_ATTR_INSTANCE_VALUE | 4,120 | 11.0% |
| RESUME_CHECK | 3,880 | 10.4% |
| LOAD_FAST_LOAD_FAST | 3,160 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,260 | 27.4% |
| STORE_FAST | 9,820 | 26.3% |
| LOAD_FAST | 8,200 | 21.9% |
| COMPARE_OP | 4,800 | 12.8% |
| CALL_METHOD_DESCRIPTOR_O | 2,060 | 5.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,140 | 40.5% |
| LOAD_FAST | 4,040 | 22.9% |
| STORE_FAST | 1,140 | 6.5% |
| CALL_INTRINSIC_1 | 1,000 | 5.7% |
| BUILD_TUPLE | 940 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,800 | 44.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 5,960 | 33.8% |
| STORE_FAST | 780 | 4.4% |
| CALL_BUILTIN_FAST | 600 | 3.4% |
| LOAD_GLOBAL_BUILTIN | 600 | 3.4% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 580 | 53.7% |
| LOAD_CONST | 260 | 24.1% |
| LOAD_GLOBAL_MODULE | 140 | 13.0% |
| PUSH_NULL | 80 | 7.4% |
| LOAD_GLOBAL | 20 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 740 | 68.5% |
| BINARY_OP | 200 | 18.5% |
| LOAD_CONST | 80 | 7.4% |
| STORE_FAST | 60 | 5.6% |


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
| LOAD_CONST | 5,080 | 78.6% |
| FORMAT_SIMPLE | 1,380 | 21.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,740 | 42.4% |
| LOAD_FAST | 1,920 | 29.7% |
| LOAD_CONST | 600 | 9.3% |
| LIST_APPEND | 340 | 5.3% |
| YIELD_VALUE | 300 | 4.6% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,100 | 39.4% |
| LOAD_FAST_LOAD_FAST | 4,860 | 11.2% |
| LOAD_GLOBAL_MODULE | 3,820 | 8.8% |
| CALL_BUILTIN_O | 2,940 | 6.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,120 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,620 | 24.5% |
| RETURN_VALUE | 6,080 | 14.0% |
| STORE_FAST | 4,520 | 10.4% |
| LOAD_FAST | 3,600 | 8.3% |
| CONTAINS_OP | 2,540 | 5.9% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 8,009,380 | 49.5% |
| LOAD_ATTR_INSTANCE_VALUE | 8,001,660 | 49.4% |
| LOAD_CONST | 45,500 | 0.3% |
| LOAD_FAST | 29,380 | 0.2% |
| LOAD_ATTR_MODULE | 29,020 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,026,240 | 49.6% |
| CALL_METHOD_DESCRIPTOR_O | 8,000,340 | 49.4% |
| POP_TOP | 54,120 | 0.3% |
| RESUME_CHECK | 25,320 | 0.2% |
| RETURN_VALUE | 19,760 | 0.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 6,540 | 52.1% |
| ENTER_EXECUTOR | 2,100 | 16.7% |
| CALL_INTRINSIC_1 | 1,760 | 14.0% |
| LOAD_FAST | 1,560 | 12.4% |
| STORE_FAST | 480 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,420 | 35.2% |
| RETURN_VALUE | 3,740 | 29.8% |
| POP_TOP | 1,920 | 15.3% |
| RESUME_CHECK | 1,220 | 9.7% |
| GET_ITER | 480 | 3.8% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,515,680 | 93.6% |
| LOAD_ATTR_INSTANCE_VALUE | 7,999,980 | 6.4% |
| LIST_EXTEND | 2,940 | 0.0% |
| IMPORT_NAME | 420 | 0.0% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 125,515,680 | 100.0% |
| CALL_FUNCTION_EX | 1,760 | 0.0% |
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
| LOAD_CONST | 14,220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,620 | 74.7% |
| STORE_FAST | 1,400 | 9.8% |
| STORE_NAME | 740 | 5.2% |
| RETURN_VALUE | 520 | 3.7% |
| MAKE_CELL | 400 | 2.8% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,600 | 37.3% |
| BUILD_LIST | 4,800 | 27.1% |
| LOAD_GLOBAL_MODULE | 2,700 | 15.3% |
| LOAD_CONST | 1,460 | 8.3% |
| BINARY_OP | 1,000 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,180 | 68.9% |
| POP_JUMP_IF_TRUE | 4,240 | 24.0% |
| COMPARE_OP | 400 | 2.3% |
| COMPARE_OP_INT | 380 | 2.1% |
| COMPARE_OP_STR | 380 | 2.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20,700 | 29.6% |
| LOAD_FAST_LOAD_FAST | 16,720 | 23.9% |
| LOAD_FAST | 10,100 | 14.4% |
| LOAD_CONST | 8,820 | 12.6% |
| LOAD_ATTR | 4,040 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 50,200 | 71.7% |
| POP_JUMP_IF_TRUE | 11,960 | 17.1% |
| EXTENDED_ARG | 4,700 | 6.7% |
| STORE_FAST | 2,280 | 3.3% |
| RETURN_VALUE | 720 | 1.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,540 | 94.8% |
| LOAD_GLOBAL_MODULE | 120 | 4.5% |
| LOAD_GLOBAL | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 2,680 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 9,160 | 17.0% |
| COMPARE_OP_STR | 6,740 | 12.5% |
| CALL_BUILTIN_FAST | 6,520 | 12.1% |
| COMPARE_OP_INT | 5,380 | 10.0% |
| SWAP | 5,280 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 34,720 | 64.4% |
| COMPARE_OP_STR | 5,280 | 9.8% |
| TO_BOOL_STR | 4,800 | 8.9% |
| STORE_FAST_STORE_FAST | 2,120 | 3.9% |
| LOAD_FAST | 1,440 | 2.7% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 29,940 | 84.7% |
| CALL_PY_EXACT_ARGS | 3,460 | 9.8% |
| CALL | 1,520 | 4.3% |
| CALL_FUNCTION_EX | 300 | 0.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 100 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 32,060 | 90.7% |
| RETURN_GENERATOR | 2,520 | 7.1% |
| RESUME | 480 | 1.4% |
| MAKE_CELL | 280 | 0.8% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 140 | 87.5% |
| POP_TOP | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 75.0% |
| LOAD_GLOBAL | 40 | 25.0% |


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 120 | 40.0% |
| STORE_NAME | 100 | 33.3% |
| ENTER_EXECUTOR | 40 | 13.3% |
| POP_TOP | 20 | 6.7% |
| FOR_ITER | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 120 | 40.0% |
| LOAD_NAME | 100 | 33.3% |
| LOAD_BUILD_CLASS | 40 | 13.3% |
| LOAD_CONST | 40 | 13.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,940 | 90.8% |
| CALL | 600 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 6,540 | 100.0% |


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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 117,529,460 | 93.6% |
| STORE_FAST | 8,002,400 | 6.4% |
| POP_JUMP_IF_TRUE | 25,840 | 0.0% |
| LIST_APPEND | 10,880 | 0.0% |
| JUMP_FORWARD | 6,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 125,514,720 | 99.9% |
| CALL_PY_EXACT_ARGS | 14,880 | 0.0% |
| CALL | 14,000 | 0.0% |
| FOR_ITER_TUPLE | 12,840 | 0.0% |
| LOAD_FAST | 9,280 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 5,540 | 16.0% |
| CONTAINS_OP | 4,700 | 13.6% |
| ENTER_EXECUTOR | 4,380 | 12.7% |
| COMPARE_OP_STR | 3,960 | 11.5% |
| TO_BOOL_BOOL | 3,420 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,120 | 35.1% |
| FOR_ITER_LIST | 6,840 | 19.8% |
| JUMP_FORWARD | 6,160 | 17.8% |
| LOAD_CONST | 3,620 | 10.5% |
| FOR_ITER | 3,200 | 9.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,960 | 46.2% |
| EXTENDED_ARG | 3,200 | 16.5% |
| GET_ITER | 3,100 | 16.0% |
| LOAD_FAST | 2,140 | 11.0% |
| FOR_ITER | 1,560 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,760 | 45.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 5,260 | 27.1% |
| FOR_ITER | 1,560 | 8.0% |
| STORE_NAME | 720 | 3.7% |
| RETURN_CONST | 600 | 3.1% |


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
| IMPORT_NAME | 2,980 | 60.6% |
| STORE_NAME | 1,940 | 39.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 4,880 | 99.2% |
| PUSH_EXC_INFO | 20 | 0.4% |
| STORE_FAST | 20 | 0.4% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 3,720 | 51.7% |
| IMPORT_FROM | 2,980 | 41.4% |
| CALL_INTRINSIC_1 | 420 | 5.8% |
| STORE_FAST | 80 | 1.1% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 34,520 | 82.9% |
| LOAD_GLOBAL_BUILTIN | 4,340 | 10.4% |
| LOAD_FAST | 1,540 | 3.7% |
| LOAD_CONST | 880 | 2.1% |
| LOAD_GLOBAL | 180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,380 | 85.0% |
| POP_JUMP_IF_TRUE | 5,200 | 12.5% |
| RETURN_VALUE | 400 | 1.0% |
| COPY | 300 | 0.7% |
| STORE_FAST | 180 | 0.4% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,600 | 19.5% |
| POP_TOP | 4,620 | 16.1% |
| POP_JUMP_IF_FALSE | 3,340 | 11.6% |
| LIST_APPEND | 2,760 | 9.6% |
| STORE_SUBSCR_DICT | 1,960 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 10,320 | 35.9% |
| FOR_ITER | 8,960 | 31.1% |
| FOR_ITER_LIST | 4,340 | 15.1% |
| EXTENDED_ARG | 1,380 | 4.8% |
| FOR_ITER_RANGE | 1,020 | 3.5% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| END_ASYNC_FOR | 5,242,800 | 99.9% |
| POP_EXCEPT | 5,540 | 0.1% |
| EXTENDED_ARG | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,248,680 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,360 | 38.0% |
| EXTENDED_ARG | 6,160 | 17.5% |
| POP_TOP | 3,300 | 9.4% |
| STORE_SUBSCR_DICT | 3,040 | 8.6% |
| LOAD_FAST | 2,000 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,340 | 49.3% |
| ENTER_EXECUTOR | 6,080 | 17.3% |
| LOAD_GLOBAL_BUILTIN | 5,700 | 16.2% |
| LOAD_FAST_LOAD_FAST | 2,400 | 6.8% |
| COPY | 1,640 | 4.7% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 9,360 | 68.6% |
| BUILD_TUPLE | 1,900 | 13.9% |
| LOAD_FAST | 1,380 | 10.1% |
| LOAD_ATTR_INSTANCE_VALUE | 400 | 2.9% |
| BUILD_STRING | 340 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 10,880 | 79.8% |
| JUMP_BACKWARD | 2,760 | 20.2% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,620 | 70.1% |
| LOAD_CONST | 620 | 16.6% |
| LOAD_ATTR | 180 | 4.8% |
| LOAD_ATTR_SLOT | 140 | 3.7% |
| CALL_KW | 80 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 2,940 | 78.6% |
| STORE_NAME | 240 | 6.4% |
| LOAD_FAST | 160 | 4.3% |
| BUILD_LIST | 140 | 3.7% |
| LOAD_CONST | 140 | 3.7% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,940 | 63.1% |
| LOAD_FAST_LOAD_FAST | 10,060 | 9.6% |
| LOAD_NAME | 6,560 | 6.3% |
| LOAD_ATTR | 5,220 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 4,940 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,940 | 18.1% |
| LOAD_ATTR_METHOD_NO_DICT | 13,860 | 13.3% |
| LOAD_FAST | 12,920 | 12.4% |
| CALL | 12,140 | 11.6% |
| LOAD_ATTR | 5,220 | 5.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,157,360 | 56.8% |
| LOAD_FAST_LOAD_FAST | 8,006,260 | 14.1% |
| BINARY_OP_ADD_INT | 8,001,980 | 14.1% |
| GET_ANEXT | 8,000,960 | 14.1% |
| LOAD_CONST | 91,640 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 16,032,280 | 28.3% |
| LOAD_FAST | 8,049,100 | 14.2% |
| BINARY_OP_ADD_INT | 8,015,440 | 14.2% |
| BINARY_SLICE | 8,013,180 | 14.2% |
| BINARY_OP | 8,006,860 | 14.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 28,800 | 58.5% |
| POP_JUMP_IF_FALSE | 4,560 | 9.3% |
| RESUME_CHECK | 3,760 | 7.6% |
| STORE_FAST | 3,260 | 6.6% |
| BINARY_SLICE | 2,000 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,760 | 60.4% |
| PUSH_NULL | 4,940 | 10.0% |
| LOAD_CONST | 3,600 | 7.3% |
| LOAD_ATTR_METHOD_NO_DICT | 2,220 | 4.5% |
| LOAD_ATTR | 1,280 | 2.6% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 141,660,640 | 49.4% |
| POP_JUMP_IF_FALSE | 42,910,980 | 15.0% |
| RESUME_CHECK | 32,100,100 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 16,127,800 | 5.6% |
| LOAD_GLOBAL_MODULE | 8,075,640 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 117,515,680 | 41.0% |
| LOAD_ATTR_INSTANCE_VALUE | 80,195,400 | 28.0% |
| LOAD_CONST | 32,157,360 | 11.2% |
| CALL_LEN | 16,032,140 | 5.6% |
| PUSH_NULL | 8,053,840 | 2.8% |


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
| LOAD_GLOBAL_MODULE | 16,020,900 | 33.2% |
| STORE_ATTR_INSTANCE_VALUE | 16,017,320 | 33.2% |
| RESUME_CHECK | 8,024,660 | 16.6% |
| RETURN_VALUE | 5,242,880 | 10.9% |
| RETURN_CONST | 2,757,200 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 24,038,100 | 49.9% |
| LOAD_ATTR_INSTANCE_VALUE | 8,014,460 | 16.6% |
| LOAD_CONST | 8,006,260 | 16.6% |
| BINARY_SUBSCR | 8,000,040 | 16.6% |
| LOAD_FAST | 29,440 | 0.1% |


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
| LOAD_FAST | 2,320 | 16.3% |
| POP_JUMP_IF_FALSE | 1,960 | 13.8% |
| STORE_FAST | 1,520 | 10.7% |
| RESUME | 1,380 | 9.7% |
| RESUME_CHECK | 1,040 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,700 | 26.1% |
| LOAD_GLOBAL_BUILTIN | 2,840 | 20.0% |
| LOAD_FAST | 2,640 | 18.6% |
| LOAD_ATTR | 1,260 | 8.9% |
| CALL | 840 | 5.9% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 14,020 | 28.9% |
| LOAD_NAME | 8,200 | 16.9% |
| LOAD_CONST | 7,220 | 14.9% |
| RESUME | 4,220 | 8.7% |
| STORE_FAST | 3,640 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,140 | 18.9% |
| LOAD_NAME | 8,200 | 16.9% |
| LOAD_ATTR | 6,560 | 13.5% |
| STORE_NAME | 5,680 | 11.7% |
| PUSH_NULL | 4,640 | 9.6% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 740 | 100.0% |

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
| MAKE_CELL | 3,160 | 38.9% |
| CALL_PY_EXACT_ARGS | 2,140 | 26.4% |
| CACHE | 1,440 | 17.7% |
| CALL | 700 | 8.6% |
| CALL_KW | 400 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,720 | 45.8% |
| MAKE_CELL | 3,160 | 38.9% |
| RESUME | 1,240 | 15.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,080 | 53.1% |
| LOAD_FAST_LOAD_FAST | 1,480 | 19.3% |
| LOAD_NAME | 680 | 8.9% |
| LOAD_FAST | 540 | 7.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 320 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,260 | 42.4% |
| EXTENDED_ARG | 1,560 | 20.3% |
| ENTER_EXECUTOR | 1,340 | 17.4% |
| JUMP_BACKWARD | 1,240 | 16.1% |
| DICT_UPDATE | 220 | 2.9% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 16,033,640 | 28.5% |
| TO_BOOL_BOOL | 8,102,840 | 14.4% |
| TO_BOOL_NONE | 8,010,860 | 14.2% |
| TO_BOOL | 8,008,620 | 14.2% |
| TO_BOOL_LIST | 8,005,920 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,910,980 | 76.2% |
| RETURN_CONST | 13,267,400 | 23.5% |
| LOAD_GLOBAL_MODULE | 32,980 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 31,840 | 0.1% |
| POP_TOP | 21,220 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,014,880 | 99.8% |
| LOAD_ATTR_INSTANCE_VALUE | 7,780 | 0.1% |
| LOAD_GLOBAL_MODULE | 3,020 | 0.0% |
| LOAD_ATTR_MODULE | 2,060 | 0.0% |
| RETURN_VALUE | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,011,740 | 99.8% |
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
| LOAD_FAST | 41,520 | 64.1% |
| LOAD_ATTR_INSTANCE_VALUE | 8,060 | 12.4% |
| CALL_BUILTIN_FAST | 7,080 | 10.9% |
| LOAD_FAST_CHECK | 4,740 | 7.3% |
| LOAD_GLOBAL_MODULE | 2,760 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,560 | 53.4% |
| LOAD_GLOBAL_MODULE | 12,760 | 19.7% |
| NOP | 4,000 | 6.2% |
| ENTER_EXECUTOR | 3,940 | 6.1% |
| LOAD_CONST | 2,400 | 3.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 71,160 | 56.0% |
| TO_BOOL_STR | 14,500 | 11.4% |
| CONTAINS_OP | 11,960 | 9.4% |
| TO_BOOL_INT | 7,240 | 5.7% |
| COMPARE_OP_INT | 7,060 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,520 | 33.5% |
| ENTER_EXECUTOR | 25,840 | 20.4% |
| LOAD_GLOBAL_BUILTIN | 17,540 | 13.8% |
| LOAD_GLOBAL_MODULE | 9,460 | 7.5% |
| POP_TOP | 7,740 | 6.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 280 | 66.7% |
| LOAD_CONST | 80 | 19.0% |
| CALL_KW | 60 | 14.3% |

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
| POP_TOP | 24,056,820 | 50.0% |
| POP_JUMP_IF_FALSE | 13,267,400 | 27.6% |
| STORE_ATTR_INSTANCE_VALUE | 8,019,620 | 16.7% |
| END_ASYNC_FOR | 2,757,200 | 5.7% |
| RESUME_CHECK | 7,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 24,063,900 | 50.0% |
| POP_TOP | 8,042,480 | 16.7% |
| EXIT_INIT_CHECK | 8,009,440 | 16.6% |
| CALL_ALLOC_AND_ENTER_INIT | 5,242,840 | 10.9% |
| LOAD_FAST_LOAD_FAST | 2,757,200 | 5.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 125,514,720 | 94.0% |
| LOAD_CONST | 8,001,000 | 6.0% |
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
| MAKE_FUNCTION | 16,000 | 91.4% |
| SET_FUNCTION_ATTRIBUTE | 1,500 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 8,040 | 45.9% |
| STORE_FAST | 3,420 | 19.5% |
| LOAD_GLOBAL_MODULE | 2,000 | 11.4% |
| CALL | 1,760 | 10.1% |
| SET_FUNCTION_ATTRIBUTE | 1,500 | 8.6% |


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
| LOAD_FAST | 17,060 | 60.3% |
| LOAD_FAST_LOAD_FAST | 7,740 | 27.3% |
| STORE_ATTR | 1,960 | 6.9% |
| SWAP | 580 | 2.0% |
| LOAD_NAME | 380 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,120 | 42.8% |
| RETURN_CONST | 3,400 | 12.0% |
| LOAD_CONST | 2,620 | 9.3% |
| LOAD_FAST_LOAD_FAST | 2,360 | 8.3% |
| STORE_ATTR | 1,960 | 6.9% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 1,200 | 29.7% |
| LOAD_ATTR | 520 | 12.9% |
| CALL_BUILTIN_CLASS | 380 | 9.4% |
| BINARY_OP_ADD_UNICODE | 300 | 7.4% |
| CALL_LEN | 300 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,240 | 30.7% |
| STORE_DEREF | 1,200 | 29.7% |
| LOAD_FAST | 340 | 8.4% |
| LOAD_CONST | 300 | 7.4% |
| LOAD_DEREF | 300 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 125,515,680 | 79.5% |
| CALL_LEN | 16,002,640 | 10.1% |
| CALL | 8,026,240 | 5.1% |
| BINARY_OP | 8,004,800 | 5.1% |
| RETURN_VALUE | 46,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 141,660,640 | 89.7% |
| LOAD_GLOBAL_MODULE | 8,040,600 | 5.1% |
| ENTER_EXECUTOR | 8,002,400 | 5.1% |
| LOAD_GLOBAL_BUILTIN | 33,700 | 0.0% |
| LOAD_CONST | 29,120 | 0.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 10,340 | 74.1% |
| CALL_LEN | 2,720 | 19.5% |
| FOR_ITER_LIST | 820 | 5.9% |
| FOR_ITER | 60 | 0.4% |
| COPY | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 9,360 | 67.0% |
| PUSH_NULL | 2,720 | 19.5% |
| LOAD_FAST | 1,100 | 7.9% |
| FORMAT_SIMPLE | 300 | 2.1% |
| LOAD_DEREF | 180 | 1.3% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 16,480 | 77.4% |
| UNPACK_SEQUENCE_TUPLE | 2,380 | 11.2% |
| COPY | 2,120 | 10.0% |
| UNPACK_SEQUENCE | 180 | 0.8% |
| STORE_FAST_STORE_FAST | 120 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,680 | 50.2% |
| LOAD_FAST_LOAD_FAST | 3,960 | 18.6% |
| NOP | 2,440 | 11.5% |
| STORE_FAST | 2,260 | 10.6% |
| LOAD_GLOBAL_BUILTIN | 620 | 2.9% |


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
| MAKE_FUNCTION | 26,000 | 31.6% |
| LOAD_CONST | 15,420 | 18.7% |
| SET_FUNCTION_ATTRIBUTE | 8,040 | 9.8% |
| CALL | 7,780 | 9.4% |
| LOAD_NAME | 5,680 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,800 | 60.5% |
| LOAD_NAME | 14,020 | 17.0% |
| RETURN_CONST | 4,040 | 4.9% |
| LOAD_BUILD_CLASS | 3,640 | 4.4% |
| POP_TOP | 2,940 | 3.6% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 10,480 | 22.1% |
| BUILD_LIST | 10,260 | 21.6% |
| FOR_ITER_TUPLE | 9,700 | 20.4% |
| POP_JUMP_IF_FALSE | 4,040 | 8.5% |
| BINARY_SUBSCR | 3,720 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,280 | 21.7% |
| BUILD_LIST | 10,260 | 21.6% |
| FOR_ITER_TUPLE | 9,660 | 20.4% |
| POP_TOP | 7,880 | 16.6% |
| COPY | 5,280 | 11.1% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 320 | 55.2% |
| RETURN_VALUE | 100 | 17.2% |
| LOAD_FAST | 80 | 13.8% |
| CALL | 40 | 6.9% |
| STORE_FAST | 40 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 280 | 48.3% |
| STORE_FAST_STORE_FAST | 180 | 31.0% |
| STORE_NAME | 60 | 10.3% |
| STORE_FAST | 40 | 6.9% |
| LOAD_FAST | 20 | 3.4% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 125,515,680 | 100.0% |
| CALL | 2,000 | 0.0% |
| ENTER_EXECUTOR | 1,720 | 0.0% |
| LOAD_FAST | 480 | 0.0% |
| RETURN_VALUE | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 125,520,680 | 100.0% |
| STORE_FAST | 420 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 5,320 | 57.8% |
| CALL | 1,700 | 18.5% |
| MAKE_CELL | 1,240 | 13.5% |
| COPY_FREE_VARS | 480 | 5.2% |
| POP_TOP | 180 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,220 | 45.9% |
| LOAD_CONST | 1,620 | 17.6% |
| LOAD_FAST | 1,400 | 15.2% |
| LOAD_GLOBAL | 1,380 | 15.0% |
| POP_TOP | 160 | 1.7% |


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
| LOAD_CONST | 8,015,440 | 100.0% |
| LOAD_FAST_LOAD_FAST | 1,280 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 1,060 | 0.0% |
| BINARY_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,001,980 | 99.8% |
| LOAD_FAST | 7,120 | 0.1% |
| STORE_FAST | 6,600 | 0.1% |
| CALL_PY_EXACT_ARGS | 680 | 0.0% |
| BINARY_SLICE | 460 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,220 | 55.5% |
| LOAD_CONST | 3,360 | 22.7% |
| BINARY_SUBSCR_LIST_INT | 2,000 | 13.5% |
| CALL_METHOD_DESCRIPTOR_O | 640 | 4.3% |
| BINARY_OP | 260 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,700 | 45.2% |
| STORE_FAST | 2,100 | 14.2% |
| CALL | 1,520 | 10.3% |
| STORE_SUBSCR_DICT | 1,360 | 9.2% |
| BUILD_TUPLE | 800 | 5.4% |


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
| LOAD_CONST | 3,980 | 36.7% |
| LOAD_FAST | 3,640 | 33.6% |
| CALL_LEN | 3,180 | 29.3% |
| BINARY_OP | 40 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,180 | 29.3% |
| LOAD_FAST_LOAD_FAST | 2,720 | 25.1% |
| STORE_FAST | 1,360 | 12.5% |
| LOAD_CONST | 1,140 | 10.5% |
| LOAD_FAST | 1,140 | 10.5% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,360 | 76.9% |
| LOAD_CONST | 2,000 | 11.5% |
| LOAD_FAST_LOAD_FAST | 1,020 | 5.9% |
| LOAD_DEREF | 460 | 2.6% |
| BUILD_TUPLE | 240 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 6,260 | 36.0% |
| STORE_FAST | 3,620 | 20.8% |
| PUSH_NULL | 2,960 | 17.0% |
| LOAD_FAST | 1,340 | 7.7% |
| CALL_BUILTIN_CLASS | 1,000 | 5.8% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,180 | 59.2% |
| LOAD_FAST | 1,400 | 19.8% |
| ENTER_EXECUTOR | 1,380 | 19.5% |
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
| LOAD_FAST | 11,880 | 77.7% |
| LOAD_CONST | 3,240 | 21.2% |
| BINARY_SUBSCR_LIST_INT | 60 | 0.4% |
| BINARY_SUBSCR | 40 | 0.3% |
| LOAD_FAST_LOAD_FAST | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,380 | 79.1% |
| BINARY_OP_ADD_UNICODE | 2,000 | 15.2% |
| STORE_FAST | 340 | 2.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 1.5% |
| LOAD_CONST | 100 | 0.8% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,720 | 59.4% |
| LOAD_FAST | 7,180 | 39.8% |
| ENTER_EXECUTOR | 120 | 0.7% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,220 | 34.5% |
| STORE_FAST | 5,420 | 30.0% |
| LOAD_FAST | 3,700 | 20.5% |
| BINARY_OP_INPLACE_ADD_UNICODE | 1,640 | 9.1% |
| CALL_BUILTIN_O | 800 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 26,820 | 99.6% |
| BINARY_SUBSCR | 120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,420 | 23.8% |
| LOAD_GLOBAL_MODULE | 6,280 | 23.3% |
| RETURN_VALUE | 3,120 | 11.6% |
| CALL_BUILTIN_O | 3,080 | 11.4% |
| LOAD_FAST | 2,620 | 9.7% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,242,840 | 65.5% |
| RETURN_VALUE | 2,757,120 | 34.4% |
| LOAD_FAST_LOAD_FAST | 4,800 | 0.1% |
| LOAD_FAST | 3,680 | 0.0% |
| BINARY_SUBSCR | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,009,440 | 100.0% |
| STORE_FAST | 100 | 0.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,860 | 46.5% |
| LOAD_FAST | 6,200 | 24.3% |
| PUSH_NULL | 3,000 | 11.8% |
| LOAD_FAST_LOAD_FAST | 2,140 | 8.4% |
| BUILD_TUPLE | 2,040 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,620 | 80.9% |
| POP_TOP | 4,660 | 18.3% |
| COPY_FREE_VARS | 100 | 0.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 80 | 0.3% |
| CALL_PY_EXACT_ARGS | 40 | 0.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,720 | 19.5% |
| CALL_LEN | 1,340 | 15.2% |
| LOAD_FAST | 1,160 | 13.1% |
| BINARY_SUBSCR_DICT | 1,000 | 11.3% |
| LOAD_DEREF | 920 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,280 | 37.1% |
| LOAD_CONST | 1,480 | 16.7% |
| GET_ITER | 900 | 10.2% |
| RETURN_VALUE | 740 | 8.4% |
| LOAD_FAST | 660 | 7.5% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 23,100 | 47.6% |
| LOAD_FAST | 10,300 | 21.2% |
| LOAD_FAST_LOAD_FAST | 6,340 | 13.1% |
| LOAD_ATTR_SLOT | 3,700 | 7.6% |
| LOAD_GLOBAL_MODULE | 3,280 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 12,260 | 25.3% |
| TO_BOOL_BOOL | 9,160 | 18.9% |
| STORE_FAST | 7,340 | 15.1% |
| POP_JUMP_IF_NOT_NONE | 7,080 | 14.6% |
| COPY | 6,520 | 13.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,640 | 48.0% |
| LOAD_GLOBAL_MODULE | 4,240 | 17.5% |
| LOAD_CONST | 3,300 | 13.6% |
| RETURN_GENERATOR | 2,000 | 8.2% |
| LOAD_FAST_LOAD_FAST | 1,200 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,360 | 30.3% |
| RETURN_VALUE | 6,740 | 27.8% |
| TO_BOOL_BOOL | 3,360 | 13.8% |
| BUILD_TUPLE | 2,120 | 8.7% |
| LOAD_GLOBAL_BUILTIN | 2,120 | 8.7% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,660 | 41.2% |
| LOAD_GLOBAL_MODULE | 4,480 | 14.6% |
| LOAD_CONST | 3,500 | 11.4% |
| BINARY_SUBSCR_TUPLE_INT | 3,080 | 10.0% |
| ENTER_EXECUTOR | 1,540 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 21,920 | 71.3% |
| BUILD_TUPLE | 2,940 | 9.6% |
| TO_BOOL_BOOL | 2,700 | 8.8% |
| STORE_FAST | 1,660 | 5.4% |
| TO_BOOL_INT | 1,220 | 4.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 24,140 | 67.3% |
| LOAD_GLOBAL_MODULE | 8,520 | 23.7% |
| BUILD_TUPLE | 1,800 | 5.0% |
| LOAD_NAME | 480 | 1.3% |
| CALL | 440 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 34,660 | 96.6% |
| RETURN_VALUE | 480 | 1.3% |
| TO_BOOL | 440 | 1.2% |
| LOAD_FAST | 240 | 0.7% |
| YIELD_VALUE | 60 | 0.2% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,032,140 | 99.9% |
| LOAD_ATTR_INSTANCE_VALUE | 15,140 | 0.1% |
| POP_JUMP_IF_TRUE | 3,180 | 0.0% |
| LOAD_ATTR | 1,060 | 0.0% |
| LOAD_GLOBAL_MODULE | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,002,640 | 99.7% |
| LOAD_CONST | 20,180 | 0.1% |
| LOAD_FAST | 9,500 | 0.1% |
| RETURN_VALUE | 6,100 | 0.0% |
| TO_BOOL_INT | 3,700 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,020 | 48.6% |
| LOAD_CONST | 4,240 | 18.7% |
| LOAD_ATTR_INSTANCE_VALUE | 3,700 | 16.3% |
| BUILD_TUPLE | 2,340 | 10.3% |
| LOAD_FAST_CHECK | 620 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 7,460 | 32.9% |
| RETURN_CONST | 6,640 | 29.3% |
| LOAD_FAST | 3,800 | 16.8% |
| ENTER_EXECUTOR | 1,900 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 940 | 4.1% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,800 | 32.8% |
| LOAD_FAST | 7,740 | 21.5% |
| BUILD_MAP | 5,960 | 16.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,660 | 13.0% |
| LOAD_CONST | 1,600 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,200 | 42.3% |
| LIST_APPEND | 9,360 | 26.0% |
| POP_TOP | 8,280 | 23.0% |
| LOAD_FAST | 1,220 | 3.4% |
| SWAP | 1,000 | 2.8% |


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
| LOAD_ATTR_METHOD_NO_DICT | 3,060 | 79.3% |
| CALL | 380 | 9.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 180 | 4.7% |
| LOAD_ATTR | 120 | 3.1% |
| LOAD_FAST | 120 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 960 | 24.9% |
| BUILD_TUPLE | 540 | 14.0% |
| TO_BOOL_BOOL | 460 | 11.9% |
| BINARY_OP | 400 | 10.4% |
| POP_TOP | 380 | 9.8% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,003,860 | 49.9% |
| CALL | 8,000,340 | 49.9% |
| STORE_FAST | 9,200 | 0.1% |
| LOAD_CONST | 8,300 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 3,700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 16,009,020 | 99.9% |
| RETURN_VALUE | 10,180 | 0.1% |
| LOAD_CONST | 6,220 | 0.0% |
| STORE_FAST | 2,300 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 2,000 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 16,002,980 | 66.4% |
| LOAD_FAST | 8,049,580 | 33.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,220 | 0.1% |
| ENTER_EXECUTOR | 14,880 | 0.1% |
| LOAD_FAST_LOAD_FAST | 7,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 24,111,660 | 100.0% |
| COPY_FREE_VARS | 3,460 | 0.0% |
| MAKE_CELL | 2,140 | 0.0% |
| RETURN_GENERATOR | 900 | 0.0% |
| RESUME | 160 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,660 | 55.3% |
| LOAD_FAST | 820 | 27.3% |
| LOAD_DEREF | 180 | 6.0% |
| CALL | 140 | 4.7% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,000 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 1,200 | 39.2% |
| LOAD_FAST | 840 | 27.5% |
| RETURN_GENERATOR | 420 | 13.7% |
| CALL_BUILTIN_CLASS | 300 | 9.8% |
| CALL | 180 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,200 | 39.2% |
| RETURN_VALUE | 540 | 17.6% |
| LOAD_FAST | 520 | 17.0% |
| STORE_DEREF | 300 | 9.8% |
| STORE_FAST | 260 | 8.5% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,840 | 58.2% |
| LOAD_GLOBAL_MODULE | 1,020 | 32.3% |
| LOAD_CONST | 200 | 6.3% |
| CALL | 80 | 2.5% |
| LOAD_ATTR_MODULE | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,040 | 32.9% |
| LOAD_GLOBAL_BUILTIN | 940 | 29.7% |
| LOAD_FAST_LOAD_FAST | 480 | 15.2% |
| LOAD_FAST | 460 | 14.6% |
| BUILD_TUPLE | 100 | 3.2% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,260 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,260 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,032,280 | 99.9% |
| LOAD_FAST | 13,520 | 0.1% |
| CALL_LEN | 1,080 | 0.0% |
| BINARY_OP | 1,000 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,033,640 | 99.9% |
| POP_JUMP_IF_TRUE | 7,060 | 0.0% |
| COPY | 5,380 | 0.0% |
| RETURN_VALUE | 2,200 | 0.0% |
| STORE_FAST | 1,000 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 36,240 | 71.2% |
| LOAD_ATTR_INSTANCE_VALUE | 7,800 | 15.3% |
| COPY | 5,280 | 10.4% |
| LOAD_FAST | 1,000 | 2.0% |
| COMPARE_OP | 380 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 37,380 | 73.4% |
| COPY | 6,740 | 13.2% |
| EXTENDED_ARG | 3,960 | 7.8% |
| JUMP_FORWARD | 1,640 | 3.2% |
| RETURN_VALUE | 1,160 | 2.3% |


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
| GET_ITER | 8,200 | 35.7% |
| EXTENDED_ARG | 6,840 | 29.8% |
| JUMP_BACKWARD | 4,340 | 18.9% |
| ENTER_EXECUTOR | 3,100 | 13.5% |
| LOAD_FAST | 240 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,180 | 31.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,040 | 30.7% |
| LOAD_GLOBAL_BUILTIN | 2,420 | 10.5% |
| LOAD_FAST | 2,160 | 9.4% |
| BUILD_LIST | 920 | 4.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,600 | 35.9% |
| GET_ITER | 1,540 | 34.5% |
| JUMP_BACKWARD | 1,020 | 22.9% |
| SWAP | 240 | 5.4% |
| FOR_ITER | 60 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,620 | 58.7% |
| LOAD_FAST | 1,340 | 30.0% |
| SWAP | 260 | 5.8% |
| LOAD_CONST | 160 | 3.6% |
| JUMP_FORWARD | 40 | 0.9% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,840 | 30.1% |
| JUMP_BACKWARD | 10,320 | 24.2% |
| SWAP | 9,660 | 22.6% |
| GET_ITER | 8,540 | 20.0% |
| LOAD_FAST | 980 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,140 | 28.4% |
| STORE_FAST_LOAD_FAST | 10,340 | 24.2% |
| SWAP | 9,700 | 22.7% |
| LOAD_FAST | 4,180 | 9.8% |
| JUMP_BACKWARD | 1,140 | 2.7% |


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
| LOAD_FAST | 80,195,400 | 90.9% |
| LOAD_FAST_LOAD_FAST | 8,014,460 | 9.1% |
| LOAD_ATTR | 2,080 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,340 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 16,024,660 | 18.2% |
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
| LOAD_ATTR_INSTANCE_VALUE | 16,024,660 | 99.4% |
| LOAD_FAST | 64,860 | 0.4% |
| LOAD_GLOBAL_MODULE | 13,880 | 0.1% |
| LOAD_ATTR | 13,860 | 0.1% |
| LOAD_ATTR_MODULE | 3,780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,051,500 | 49.9% |
| LOAD_GLOBAL_MODULE | 8,012,980 | 49.7% |
| LOAD_CONST | 50,100 | 0.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 4,660 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,060 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,005,280 | 99.6% |
| LOAD_FAST | 28,680 | 0.4% |
| LOAD_GLOBAL_MODULE | 3,700 | 0.0% |
| LOAD_ATTR | 1,120 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,015,520 | 99.7% |
| CALL_PY_EXACT_ARGS | 20,220 | 0.3% |
| LOAD_FAST_LOAD_FAST | 2,500 | 0.0% |
| LOAD_CONST | 1,260 | 0.0% |
| CALL | 620 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 96,800 | 93.1% |
| LOAD_NAME | 3,360 | 3.2% |
| LOAD_FAST | 2,720 | 2.6% |
| LOAD_ATTR | 1,040 | 1.0% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 29,020 | 27.9% |
| PUSH_NULL | 18,320 | 17.6% |
| LOAD_FAST | 13,040 | 12.5% |
| LOAD_ATTR_SLOT | 12,200 | 11.7% |
| LOAD_CONST | 8,960 | 8.6% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 580 | 90.6% |
| LOAD_FAST | 40 | 6.2% |
| LOAD_ATTR | 20 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 580 | 90.6% |
| LOAD_FAST | 60 | 9.4% |


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
| LOAD_ATTR_MODULE | 12,200 | 50.6% |
| LOAD_FAST | 9,720 | 40.3% |
| RETURN_VALUE | 1,260 | 5.2% |
| LOAD_ATTR | 360 | 1.5% |
| CALL_BUILTIN_FAST | 300 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,040 | 50.0% |
| LOAD_CONST | 4,500 | 18.7% |
| CALL_BUILTIN_FAST | 3,700 | 15.4% |
| STORE_FAST | 1,260 | 5.2% |
| LOAD_FAST_LOAD_FAST | 520 | 2.2% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,052,880 | 98.9% |
| STORE_FAST | 33,700 | 0.2% |
| POP_JUMP_IF_FALSE | 31,840 | 0.2% |
| LOAD_FAST | 25,800 | 0.2% |
| POP_JUMP_IF_TRUE | 17,540 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,127,800 | 99.3% |
| LOAD_DEREF | 28,800 | 0.2% |
| CALL_ISINSTANCE | 24,140 | 0.1% |
| LOAD_FAST_LOAD_FAST | 14,680 | 0.1% |
| CHECK_EXC_MATCH | 7,920 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,040,600 | 24.8% |
| LOAD_ATTR_METHOD_NO_DICT | 8,012,980 | 24.8% |
| LOAD_GLOBAL_MODULE | 8,007,020 | 24.7% |
| BINARY_SUBSCR | 7,999,960 | 24.7% |
| LOAD_FAST | 94,740 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,020,900 | 49.5% |
| LOAD_FAST | 8,075,640 | 25.0% |
| LOAD_GLOBAL_MODULE | 8,007,020 | 24.7% |
| LOAD_ATTR_MODULE | 96,800 | 0.3% |
| IS_OP | 34,520 | 0.1% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,260 | 92.6% |
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
| LOAD_FAST | 24,740 | 99.0% |
| LOAD_SUPER_ATTR | 240 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 22,440 | 89.8% |
| LOAD_FAST | 2,060 | 8.2% |
| CALL | 280 | 1.1% |
| CALL_PY_EXACT_ARGS | 200 | 0.8% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 141,572,440 | 77.9% |
| CALL_PY_EXACT_ARGS | 24,111,660 | 13.3% |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,440 | 4.4% |
| POP_TOP | 8,003,340 | 4.4% |
| COPY_FREE_VARS | 32,060 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 125,520,720 | 69.0% |
| LOAD_FAST | 32,100,100 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 16,052,880 | 8.8% |
| LOAD_FAST_LOAD_FAST | 8,024,660 | 4.4% |
| LOAD_GLOBAL_MODULE | 77,940 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 24,038,100 | 99.8% |
| LOAD_FAST | 49,460 | 0.2% |
| STORE_ATTR | 1,240 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 240 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,017,320 | 66.5% |
| RETURN_CONST | 8,019,620 | 33.3% |
| LOAD_FAST | 31,380 | 0.1% |
| LOAD_CONST | 9,380 | 0.0% |
| BUILD_LIST | 4,120 | 0.0% |


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
| LOAD_FAST | 14,620 | 52.7% |
| LOAD_CONST | 5,640 | 20.3% |
| LOAD_FAST_LOAD_FAST | 3,040 | 11.0% |
| LOAD_ATTR_INSTANCE_VALUE | 2,440 | 8.8% |
| BINARY_OP_ADD_UNICODE | 1,360 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,300 | 22.7% |
| ENTER_EXECUTOR | 4,180 | 15.1% |
| LOAD_GLOBAL_MODULE | 3,240 | 11.7% |
| JUMP_FORWARD | 3,040 | 11.0% |
| JUMP_BACKWARD | 1,960 | 7.1% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,740 | 68.2% |
| LOAD_FAST | 640 | 15.9% |
| LOAD_NAME | 600 | 14.9% |
| STORE_SUBSCR | 40 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,920 | 47.8% |
| JUMP_BACKWARD | 960 | 23.9% |
| RETURN_CONST | 540 | 13.4% |
| LOAD_NAME | 320 | 8.0% |
| EXTENDED_ARG | 160 | 4.0% |


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
| LOAD_ATTR_INSTANCE_VALUE | 8,002,480 | 97.9% |
| RETURN_VALUE | 37,620 | 0.5% |
| COPY | 34,720 | 0.4% |
| CALL_ISINSTANCE | 34,660 | 0.4% |
| LOAD_FAST | 20,640 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,102,840 | 99.1% |
| POP_JUMP_IF_TRUE | 71,160 | 0.9% |
| EXTENDED_ARG | 3,420 | 0.0% |
| UNARY_NOT | 60 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,620 | 52.9% |
| CALL_LEN | 3,700 | 16.8% |
| LOAD_FAST | 3,200 | 14.6% |
| COPY | 1,240 | 5.6% |
| CALL_BUILTIN_O | 1,220 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 13,520 | 61.6% |
| POP_JUMP_IF_TRUE | 7,240 | 33.0% |
| UNARY_NOT | 1,180 | 5.4% |
| TO_BOOL_BOOL | 20 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,004,280 | 99.9% |
| LOAD_FAST | 3,780 | 0.0% |
| LOAD_ATTR | 280 | 0.0% |
| TO_BOOL | 100 | 0.0% |
| LOAD_ATTR_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,005,920 | 100.0% |
| POP_JUMP_IF_TRUE | 2,340 | 0.0% |
| UNARY_NOT | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 7,998,960 | 99.0% |
| TO_BOOL_ALWAYS_TRUE | 68,860 | 0.9% |
| LOAD_FAST | 11,760 | 0.1% |
| COPY | 700 | 0.0% |
| TO_BOOL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,010,860 | 99.1% |
| TO_BOOL_ALWAYS_TRUE | 68,840 | 0.9% |
| POP_JUMP_IF_TRUE | 1,140 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 9,360 | 48.8% |
| LOAD_FAST | 4,900 | 25.5% |
| COPY | 4,800 | 25.0% |
| TO_BOOL | 60 | 0.3% |
| LOAD_GLOBAL_MODULE | 60 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 14,500 | 75.5% |
| POP_JUMP_IF_FALSE | 4,700 | 24.5% |


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
| RETURN_VALUE | 9,220 | 40.9% |
| FOR_ITER_LIST | 7,040 | 31.3% |
| FOR_ITER | 5,260 | 23.4% |
| UNPACK_SEQUENCE | 280 | 1.2% |
| LOAD_CONST | 260 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 16,480 | 73.2% |
| STORE_FAST | 4,980 | 22.1% |
| STORE_NAME | 820 | 3.6% |
| STORE_DEREF | 180 | 0.8% |
| LOAD_FAST | 60 | 0.3% |


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
|     deferred | 8,027,320 | 49.8% |
|          hit | 8,083,280 | 50.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 500 | 12.3% |
| Failure | 3,580 | 87.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 2,240 | 62.6% |
| and int | 640 | 17.9% |
| or | 300 | 8.4% |
| add other | 180 | 5.0% |
| power | 80 | 2.2% |
| add different types | 60 | 1.7% |
| multiply different types | 60 | 1.7% |
| and different types | 20 | 0.6% |


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
|     deferred | 8,011,660 | 98.6% |
|          hit | 114,780 | 1.4% |
|         miss | 2,460 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 360 | 13.6% |
| Failure | 2,280 | 86.4% |

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
|     deferred | 16,208,680 | 20.1% |
|          hit | 64,582,820 | 79.9% |
|         miss | 27,260 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,320 | 43.4% |
| Failure | 8,240 | 56.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class no vectorcall | 2,640 | 32.0% |
| other | 2,280 | 27.7% |
| meth descr varargs | 1,380 | 16.7% |
| cfunc noargs | 440 | 5.3% |
| code complex parameters | 400 | 4.9% |
| method wrapper | 200 | 2.4% |
| cfunc varargs keywords | 160 | 1.9% |
| class mutable | 120 | 1.5% |
| metaclass | 120 | 1.5% |
| wrong number arguments | 100 | 1.2% |
| cfunc varargs | 100 | 1.2% |
| no dict | 60 | 0.7% |
| meth descr method fastcall keywords | 60 | 0.7% |
| operator wrapper | 60 | 0.7% |
| meth descr varargs keywords | 40 | 0.5% |
| init not simple | 40 | 0.5% |
| cmethod | 20 | 0.2% |
| init not python | 20 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,880 | 0.1% |
|          hit | 16,139,600 | 99.9% |
|         miss | 360 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 65.5% |
| Failure | 400 | 34.5% |

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
|     deferred | 17,960 | 20.0% |
|          hit | 69,900 | 77.6% |
|         miss | 720 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 580 | 26.9% |
| Failure | 1,580 | 73.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict values | 500 | 31.6% |
| dict items | 480 | 30.4% |
| set | 180 | 11.4% |
| itertools | 160 | 10.1% |
| seq iter | 140 | 8.9% |
| map | 60 | 3.8% |
| dict keys | 20 | 1.3% |
| enumerate | 20 | 1.3% |
| zip | 20 | 1.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 109,060 | 0.1% |
|        deopt | 360 | 0.0% |
|          hit | 112,630,100 | 99.9% |
|         miss | 14,600 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,180 | 61.9% |
| Failure | 3,800 | 38.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 2,480 | 65.3% |
| method | 460 | 12.1% |
| not managed dict | 340 | 8.9% |
| module attr not found | 140 | 3.7% |
| has managed dict | 120 | 3.2% |
| class attr descriptor | 60 | 1.6% |
| non overriding descriptor | 40 | 1.1% |
| builtin class method | 40 | 1.1% |
| class method obj | 40 | 1.1% |
| class attr simple | 40 | 1.1% |
| overridden | 20 | 0.5% |
| mutable class | 20 | 0.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 126,660 | 0.3% |
|        deopt | 2,620 | 0.0% |
|          hit | 48,482,560 | 99.7% |
|         miss | 120,440 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,980 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 400 | 1.5% |
|          hit | 26,340 | 97.3% |

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
|     deferred | 37,320 | 0.2% |
|          hit | 24,115,280 | 99.8% |
|         miss | 12,740 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,760 | 47.3% |
| Failure | 1,960 | 52.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 1,480 | 75.5% |
| not in keys | 160 | 8.2% |
| overriding descriptor | 140 | 7.1% |
| no dict | 80 | 4.1% |
| not managed dict | 80 | 4.1% |
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
|     deferred | 5,540 | 12.4% |
|          hit | 38,560 | 86.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 42.9% |
| Failure | 320 | 57.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 280 | 87.5% |
| py simple | 40 | 12.5% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,179,540 | 37.5% |
|          hit | 25,135,900 | 62.1% |
|         miss | 7,306,620 | 18.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140,380 | 98.4% |
| Failure | 2,320 | 1.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 2,180 | 94.0% |
| mapping | 60 | 2.6% |
| sequence | 40 | 1.7% |
| number | 20 | 0.9% |
| tuple | 20 | 0.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 300 | 0.5% |
|          hit | 63,900 | 99.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,485,778,160 | 66.7% |
| Not specialized | 254,571,320 | 11.4% |
| Specialized hits | 480,758,220 | 21.6% |
| Specialized misses | 7,496,600 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| SEND | 133,515,700 | 73.7% |
| CALL | 16,208,680 | 8.9% |
| TO_BOOL | 15,179,540 | 8.4% |
| BINARY_OP | 8,027,320 | 4.4% |
| BINARY_SUBSCR | 8,011,660 | 4.4% |
| LOAD_GLOBAL | 126,660 | 0.1% |
| LOAD_ATTR | 109,060 | 0.1% |
| STORE_ATTR | 37,320 | 0.0% |
| FOR_ITER | 17,960 | 0.0% |
| COMPARE_OP | 16,880 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL_NONE | 3,653,780 | 48.7% |
| TO_BOOL_ALWAYS_TRUE | 3,650,500 | 48.6% |
| LOAD_GLOBAL_MODULE | 68,580 | 0.9% |
| LOAD_GLOBAL_BUILTIN | 51,860 | 0.7% |
| STORE_ATTR_INSTANCE_VALUE | 12,620 | 0.2% |
| RESUME | 11,400 | 0.2% |
| RESUME_CHECK | 11,400 | 0.2% |
| CALL_PY_EXACT_ARGS | 9,600 | 0.1% |
| LOAD_ATTR_MODULE | 9,260 | 0.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,860 | 0.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 157,612,520 | 83.0% |
| Calls to Python functions inlined | 32,249,520 | 17.0% |
| Calls via PyEval_EvalFrame (total) | 157,612,520 | 83.0% |
| Calls via PyEval_EvalFrame (vector) | 24,088,680 | 12.7% |
| Calls via PyEval_EvalFrame (generator) | 133,523,840 | 70.3% |
| Calls via PyEval_EvalFrame (legacy) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 24,083,140 | 12.7% |
| Calls via PyEval_EvalFrame (build class) | 4,220 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 28,700 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 1,580 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 16,013,340 | 8.4% |
| Calls via PyEval_EvalFrame (method) | 2,800 | 0.0% |
| Frame objects created | 5,255,120 | 2.8% |
| Frames pushed | 64,347,080 | 33.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 259,435,520 | 52.3% |
| Frees to freelist | 259,432,260 |  |
| Allocations | 236,283,440 | 47.7% |
| Allocations to 512 bytes | 236,242,540 | 47.7% |
| Allocations to 4 kbytes | 37,980 | 0.0% |
| Allocations over 4 kbytes | 2,920 | 0.0% |
| Frees | 235,699,725 |  |
| New values | 10,380 |  |
| Interpreter increfs | 1,133,903,300 | 61.5% |
| Interpreter decrefs | 1,588,454,072 | 64.0% |
| Increfs | 711,046,352 | 38.5% |
| Decrefs | 892,530,280 | 36.0% |
| Materialize dict (on request) | 140 | 1.3% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 80 | 0.8% |
| Method cache hits | 176,766 |  |
| Method cache misses | 57,794 |  |
| Method cache collisions | 65,960 |  |
| Method cache dunder hits | 8,316,687 |  |
| Method cache dunder misses | 22,533 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 10,640 | 3,600 | 60,699,920 |
| 1 | 960 | 0 | 62,093,320 |
| 2 | 80 | 0 | 49,748,440 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 1,280 |  |
| Traces created | 1,280 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 100 | 7.8% |
| Recursive call | 40 | 3.1% |
| Low confidence | 120 | 9.4% |
| Traces executed | 0 |  |
| Uops executed | 0 |  |

### Trace length histogram

<details>
<summary> trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 60 | 4.7% |
| <= 16 | 100 | 7.8% |
| <= 32 | 540 | 42.2% |
| <= 64 | 340 | 26.6% |
| <= 128 | 240 | 18.8% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 80 | 6.2% |
| <= 16 | 120 | 9.4% |
| <= 32 | 440 | 34.4% |
| <= 64 | 320 | 25.0% |


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

|Opcode | Count | 
|---|---:|
| CALL | 120 |
| SEND | 60 |
| CALL_LIST_APPEND | 40 |
| CALL_FUNCTION_EX | 20 |
| YIELD_VALUE | 20 |
| BINARY_SUBSCR_GETITEM | 20 |
| CALL_ALLOC_AND_ENTER_INIT | 20 |


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
| func modification | 80 |
| watched dict modification | 40 |
| watched globals modification | 40 |


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
