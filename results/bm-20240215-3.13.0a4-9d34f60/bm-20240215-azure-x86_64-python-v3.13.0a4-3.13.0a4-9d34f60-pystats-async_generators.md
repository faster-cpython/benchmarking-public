
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
| LOAD_FAST | 287,358,540 | 11.6% | 11.6% |  |
| LOAD_CONST | 182,252,400 | 7.3% | 18.9% |  |
| RESUME_CHECK | 181,849,320 | 7.3% | 26.2% | 0.0% |
| STORE_FAST | 158,024,300 | 6.4% | 32.6% |  |
| POP_TOP | 157,780,180 | 6.4% | 39.0% |  |
| INTERPRETER_EXIT | 157,610,020 | 6.4% | 45.3% |  |
| SEND | 133,548,900 | 5.4% | 50.7% |  |
| GET_ANEXT | 133,515,680 | 5.4% | 56.1% |  |
| JUMP_BACKWARD | 125,695,140 | 5.1% | 61.1% |  |
| CALL_INTRINSIC_1 | 125,521,280 | 5.1% | 66.2% |  |
| YIELD_VALUE | 125,521,100 | 5.1% | 71.3% |  |
| END_SEND | 125,515,760 | 5.1% | 76.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 88,278,780 | 3.6% | 79.9% | 0.0% |
| POP_JUMP_IF_FALSE | 56,429,320 | 2.3% | 82.2% |  |
| LOAD_FAST_LOAD_FAST | 48,259,960 | 1.9% | 84.1% |  |
| RETURN_CONST | 48,153,000 | 1.9% | 86.0% |  |
| LOAD_GLOBAL_MODULE | 32,415,200 | 1.3% | 87.3% | 0.2% |
| CALL_PY_EXACT_ARGS | 24,144,620 | 1.0% | 88.3% | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 24,119,980 | 1.0% | 89.3% | 0.1% |
| LOAD_GLOBAL_BUILTIN | 16,265,700 | 0.7% | 89.9% | 0.3% |
| CALL | 16,195,980 | 0.7% | 90.6% |  |
| RETURN_VALUE | 16,190,980 | 0.7% | 91.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 16,152,760 | 0.7% | 91.9% |  |
| CALL_LEN | 16,064,280 | 0.6% | 92.5% |  |
| COMPARE_OP_INT | 16,057,720 | 0.6% | 93.2% | 0.0% |
| BINARY_SLICE | 16,034,200 | 0.6% | 93.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 16,033,920 | 0.6% | 94.5% | 0.0% |
| TO_BOOL_BOOL | 8,226,980 | 0.3% | 94.8% | 0.0% |
| PUSH_NULL | 8,156,840 | 0.3% | 95.1% |  |
| TO_BOOL_NONE | 8,080,840 | 0.3% | 95.5% | 45.2% |
| TO_BOOL_ALWAYS_TRUE | 8,069,900 | 0.3% | 95.8% | 45.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,057,400 | 0.3% | 96.1% | 0.0% |
| BINARY_OP_ADD_INT | 8,044,060 | 0.3% | 96.4% |  |
| BINARY_OP | 8,041,500 | 0.3% | 96.8% |  |
| POP_JUMP_IF_NONE | 8,033,800 | 0.3% | 97.1% |  |
| TO_BOOL | 8,015,820 | 0.3% | 97.4% |  |
| BINARY_SUBSCR | 8,012,820 | 0.3% | 97.7% |  |
| TO_BOOL_LIST | 8,009,540 | 0.3% | 98.1% | 0.0% |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,540 | 0.3% | 98.4% | 0.0% |
| EXIT_INIT_CHECK | 8,009,440 | 0.3% | 98.7% |  |
| RETURN_GENERATOR | 8,003,520 | 0.3% | 99.0% |  |
| END_ASYNC_FOR | 8,000,000 | 0.3% | 99.4% |  |
| GET_AITER | 8,000,000 | 0.3% | 99.7% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 5,248,700 | 0.2% | 99.9% |  |
| POP_JUMP_IF_TRUE | 170,080 | 0.0% | 99.9% |  |
| LOAD_ATTR_MODULE | 123,820 | 0.0% | 99.9% | 7.5% |
| NOP | 122,680 | 0.0% | 99.9% |  |
| LOAD_ATTR | 110,420 | 0.0% | 99.9% |  |
| CONTAINS_OP | 101,580 | 0.0% | 99.9% |  |
| STORE_NAME | 90,980 | 0.0% | 99.9% |  |
| LOAD_NAME | 89,340 | 0.0% | 99.9% |  |
| POP_JUMP_IF_NOT_NONE | 81,320 | 0.0% | 99.9% |  |
| COMPARE_OP_STR | 80,540 | 0.0% | 99.9% | 0.3% |
| FOR_ITER | 74,580 | 0.0% | 99.9% |  |
| COPY | 72,700 | 0.0% | 99.9% |  |
| FOR_ITER_TUPLE | 64,340 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 60,120 | 0.0% | 99.9% |  |
| EXTENDED_ARG | 59,780 | 0.0% | 99.9% |  |
| CALL_BUILTIN_FAST | 56,920 | 0.0% | 99.9% | 1.2% |
| SWAP | 55,200 | 0.0% | 99.9% |  |
| STORE_FAST_STORE_FAST | 52,500 | 0.0% | 99.9% |  |
| IS_OP | 52,140 | 0.0% | 99.9% |  |
| LOAD_DEREF | 52,020 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 50,560 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 50,220 | 0.0% | 100.0% | 1.4% |
| BUILD_TUPLE | 46,500 | 0.0% | 100.0% |  |
| CALL_ISINSTANCE | 42,280 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 42,080 | 0.0% | 100.0% | 7.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 42,060 | 0.0% | 100.0% | 16.3% |
| GET_ITER | 41,280 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 40,800 | 0.0% | 100.0% |  |
| BUILD_LIST | 39,480 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 36,560 | 0.0% | 100.0% | 0.7% |
| COPY_FREE_VARS | 35,340 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 35,200 | 0.0% | 100.0% |  |
| LIST_APPEND | 33,760 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 32,300 | 0.0% | 100.0% | 5.8% |
| TO_BOOL_STR | 30,680 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 30,380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 30,020 | 0.0% | 100.0% |  |
| STORE_ATTR | 29,800 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 28,600 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 28,320 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 24,980 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 24,580 | 0.0% | 100.0% | 4.2% |
| LOAD_ATTR_SLOT | 24,540 | 0.0% | 100.0% | 1.4% |
| FOR_ITER_RANGE | 23,840 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 22,680 | 0.0% | 100.0% |  |
| FORMAT_SIMPLE | 22,000 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 21,260 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 19,080 | 0.0% | 100.0% |  |
| BUILD_STRING | 18,120 | 0.0% | 100.0% |  |
| BEFORE_WITH | 18,100 | 0.0% | 100.0% |  |
| COMPARE_OP | 17,680 | 0.0% | 100.0% |  |
| BUILD_MAP | 17,640 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 17,500 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 15,280 | 0.0% | 100.0% | 14.5% |
| CALL_KW | 14,220 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 14,200 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 13,780 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 12,560 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 11,160 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 10,700 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 10,360 | 0.0% | 100.0% |  |
| MAP_ADD | 9,780 | 0.0% | 100.0% |  |
| RESUME | 9,200 | 0.0% | 100.0% | 123.9% |
| STORE_SUBSCR_LIST_INT | 8,180 | 0.0% | 100.0% |  |
| MAKE_CELL | 8,120 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 8,040 | 0.0% | 100.0% | 1.5% |
| CHECK_EXC_MATCH | 7,980 | 0.0% | 100.0% |  |
| POP_EXCEPT | 7,980 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 7,980 | 0.0% | 100.0% |  |
| IMPORT_NAME | 7,200 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 7,060 | 0.0% | 100.0% |  |
| DICT_MERGE | 6,540 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 6,340 | 0.0% | 100.0% |  |
| LIST_EXTEND | 5,840 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 5,800 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 5,580 | 0.0% | 100.0% | 7.9% |
| BUILD_CONST_KEY_MAP | 5,420 | 0.0% | 100.0% |  |
| IMPORT_FROM | 4,920 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 4,700 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 4,220 | 0.0% | 100.0% |  |
| STORE_DEREF | 4,040 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 3,780 | 0.0% | 100.0% |  |
| CALL_STR_1 | 3,300 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 3,060 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 3,000 | 0.0% | 100.0% |  |
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
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 660 | 0.0% | 100.0% | 3.0% |
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
| STORE_FAST LOAD_FAST | 141,741,880 | 5.7% | 5.7% |
| CACHE RESUME_CHECK | 141,572,440 | 5.7% | 11.4% |
| LOAD_CONST SEND | 133,515,720 | 5.4% | 16.8% |
| GET_ANEXT LOAD_CONST | 133,515,680 | 5.4% | 22.2% |
| RESUME_CHECK POP_TOP | 125,520,720 | 5.1% | 27.2% |
| YIELD_VALUE INTERPRETER_EXIT | 125,520,680 | 5.1% | 32.3% |
| END_SEND STORE_FAST | 125,515,680 | 5.1% | 37.3% |
| CALL_INTRINSIC_1 YIELD_VALUE | 125,515,680 | 5.1% | 42.4% |
| JUMP_BACKWARD GET_ANEXT | 125,515,680 | 5.1% | 47.5% |
| SEND END_SEND | 125,515,680 | 5.1% | 52.5% |
| POP_TOP JUMP_BACKWARD | 117,532,740 | 4.7% | 57.3% |
| LOAD_FAST CALL_INTRINSIC_1 | 117,515,680 | 4.7% | 62.0% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 80,260,380 | 3.2% | 65.2% |
| POP_JUMP_IF_FALSE LOAD_FAST | 42,967,260 | 1.7% | 67.0% |
| LOAD_FAST LOAD_CONST | 32,244,900 | 1.3% | 68.3% |
| RESUME_CHECK LOAD_FAST | 32,132,900 | 1.3% | 69.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 24,137,700 | 1.0% | 70.5% |
| RETURN_CONST INTERPRETER_EXIT | 24,063,900 | 1.0% | 71.5% |
| POP_TOP RETURN_CONST | 24,056,820 | 1.0% | 72.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 24,053,440 | 1.0% | 73.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 16,147,980 | 0.7% | 74.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 16,058,320 | 0.6% | 74.7% |
| LOAD_FAST CALL_LEN | 16,042,360 | 0.6% | 75.4% |
| LOAD_CONST COMPARE_OP_INT | 16,037,000 | 0.6% | 76.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 16,036,700 | 0.6% | 76.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 16,032,660 | 0.6% | 77.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 16,024,660 | 0.6% | 78.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 16,024,240 | 0.6% | 78.6% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 16,010,620 | 0.6% | 79.2% |
| CALL_LEN STORE_FAST | 16,005,300 | 0.6% | 79.9% |
| BINARY_SLICE CALL_PY_EXACT_ARGS | 16,002,980 | 0.6% | 80.5% |
| POP_JUMP_IF_FALSE RETURN_CONST | 13,268,380 | 0.5% | 81.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,122,980 | 0.3% | 81.4% |
| LOAD_FAST PUSH_NULL | 8,089,960 | 0.3% | 81.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 8,089,900 | 0.3% | 82.1% |
| POP_TOP LOAD_FAST | 8,087,780 | 0.3% | 82.4% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 8,069,700 | 0.3% | 82.7% |
| LOAD_CONST LOAD_FAST | 8,060,920 | 0.3% | 83.0% |
| RETURN_CONST POP_TOP | 8,057,820 | 0.3% | 83.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 8,055,480 | 0.3% | 83.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 8,044,600 | 0.3% | 84.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,041,600 | 0.3% | 84.3% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 8,034,960 | 0.3% | 84.6% |
| CALL STORE_FAST | 8,026,240 | 0.3% | 85.0% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 8,024,660 | 0.3% | 85.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 8,024,060 | 0.3% | 85.6% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,019,560 | 0.3% | 85.9% |
| LOAD_CONST BINARY_SLICE | 8,019,380 | 0.3% | 86.3% |
| LOAD_CONST BINARY_OP | 8,016,620 | 0.3% | 86.6% |
| POP_JUMP_IF_NONE LOAD_FAST | 8,016,420 | 0.3% | 86.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 8,015,520 | 0.3% | 87.2% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 8,014,900 | 0.3% | 87.6% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 8,010,860 | 0.3% | 87.9% |
| RETURN_VALUE RETURN_VALUE | 8,010,500 | 0.3% | 88.2% |
| EXIT_INIT_CHECK RETURN_VALUE | 8,009,440 | 0.3% | 88.5% |
| RETURN_CONST EXIT_INIT_CHECK | 8,009,440 | 0.3% | 88.8% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 8,009,440 | 0.3% | 89.2% |
| PUSH_NULL CALL | 8,009,380 | 0.3% | 89.5% |
| TO_BOOL POP_JUMP_IF_FALSE | 8,008,620 | 0.3% | 89.8% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 8,007,020 | 0.3% | 90.1% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 8,006,960 | 0.3% | 90.5% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,006,660 | 0.3% | 90.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 8,005,280 | 0.3% | 91.1% |
| BINARY_OP STORE_FAST | 8,004,800 | 0.3% | 91.4% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 8,004,620 | 0.3% | 91.8% |
| LOAD_FAST BINARY_SLICE | 8,004,580 | 0.3% | 92.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 8,004,280 | 0.3% | 92.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 8,004,240 | 0.3% | 92.7% |
| CACHE POP_TOP | 8,003,380 | 0.3% | 93.0% |
| POP_TOP RESUME_CHECK | 8,003,340 | 0.3% | 93.4% |
| STORE_FAST JUMP_BACKWARD | 8,002,480 | 0.3% | 93.7% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 8,002,480 | 0.3% | 94.0% |
| BINARY_OP_ADD_INT LOAD_CONST | 8,001,980 | 0.3% | 94.3% |
| LOAD_ATTR_INSTANCE_VALUE CALL | 8,001,660 | 0.3% | 94.7% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 8,001,040 | 0.3% | 95.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_ALWAYS_TRUE | 8,001,020 | 0.3% | 95.3% |
| CALL CALL_METHOD_DESCRIPTOR_O | 8,000,340 | 0.3% | 95.6% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 8,000,040 | 0.3% | 95.9% |
| CACHE RETURN_GENERATOR | 8,000,000 | 0.3% | 96.3% |
| GET_AITER GET_ANEXT | 8,000,000 | 0.3% | 96.6% |
| RETURN_GENERATOR INTERPRETER_EXIT | 8,000,000 | 0.3% | 96.9% |
| SEND END_ASYNC_FOR | 8,000,000 | 0.3% | 97.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_INTRINSIC_1 | 7,999,980 | 0.3% | 97.6% |
| BINARY_SUBSCR LOAD_GLOBAL_MODULE | 7,999,960 | 0.3% | 97.9% |
| LOAD_ATTR_INSTANCE_VALUE GET_AITER | 7,999,880 | 0.3% | 98.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_NONE | 7,998,960 | 0.3% | 98.5% |
| JUMP_BACKWARD_NO_INTERRUPT LOAD_FAST | 5,248,680 | 0.2% | 98.7% |
| RETURN_VALUE LOAD_FAST_LOAD_FAST | 5,242,880 | 0.2% | 98.9% |
| RETURN_CONST CALL_ALLOC_AND_ENTER_INIT | 5,242,840 | 0.2% | 99.2% |
| END_ASYNC_FOR JUMP_BACKWARD_NO_INTERRUPT | 5,242,800 | 0.2% | 99.4% |
| END_ASYNC_FOR RETURN_CONST | 2,757,200 | 0.1% | 99.5% |
| RETURN_CONST LOAD_FAST_LOAD_FAST | 2,757,200 | 0.1% | 99.6% |
| RETURN_VALUE CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 0.1% | 99.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 108,660 | 0.0% | 99.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 100,500 | 0.0% | 99.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 99,300 | 0.0% | 99.7% |
| LOAD_CONST LOAD_CONST | 97,860 | 0.0% | 99.7% |
| LOAD_FAST LOAD_FAST | 84,240 | 0.0% | 99.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 83,520 | 0.0% | 99.7% |
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
| LOAD_CONST | 8,019,380 | 50.0% |
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
| LOAD_CONST | 7,380 | 0.1% |
| BINARY_SUBSCR | 2,300 | 0.0% |
| BUILD_SLICE | 1,540 | 0.0% |
| LOAD_FAST | 980 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,999,960 | 99.8% |
| SWAP | 4,700 | 0.1% |
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
| CONVERT_VALUE | 10,360 | 47.1% |
| LOAD_FAST | 6,500 | 29.5% |
| LOAD_ATTR | 3,120 | 14.2% |
| STORE_FAST_LOAD_FAST | 1,540 | 7.0% |
| LOAD_ATTR_MODULE | 360 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,840 | 81.1% |
| BUILD_STRING | 4,120 | 18.7% |
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
| LOAD_FAST | 23,820 | 57.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,300 | 10.4% |
| LOAD_GLOBAL_MODULE | 2,000 | 4.8% |
| BUILD_TUPLE | 1,620 | 3.9% |
| BINARY_SUBSCR | 1,320 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 10,480 | 25.4% |
| FOR_ITER_TUPLE | 8,700 | 21.1% |
| FOR_ITER_LIST | 8,560 | 20.7% |
| EXTENDED_ARG | 5,540 | 13.4% |
| CALL_PY_EXACT_ARGS | 3,140 | 7.6% |


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
| STORE_FAST | 47,500 | 38.7% |
| POP_TOP | 15,980 | 13.0% |
| STORE_FAST_STORE_FAST | 9,640 | 7.9% |
| POP_JUMP_IF_FALSE | 9,180 | 7.5% |
| NOP | 8,360 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 70,160 | 57.2% |
| LOAD_GLOBAL_MODULE | 25,300 | 20.6% |
| LOAD_CONST | 9,860 | 8.0% |
| NOP | 8,360 | 6.8% |
| LOAD_FAST_LOAD_FAST | 4,160 | 3.4% |


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
| CALL_METHOD_DESCRIPTOR_O | 16,010,620 | 10.1% |
| RETURN_CONST | 8,057,820 | 5.1% |
| CACHE | 8,003,380 | 5.1% |
| CALL | 54,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 117,532,740 | 74.5% |
| RETURN_CONST | 24,056,820 | 15.2% |
| LOAD_FAST | 8,087,780 | 5.1% |
| RESUME_CHECK | 8,003,340 | 5.1% |
| LOAD_GLOBAL_BUILTIN | 17,820 | 0.0% |


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
| LOAD_FAST | 8,089,960 | 99.2% |
| LOAD_ATTR_MODULE | 37,360 | 0.5% |
| LOAD_NAME | 6,740 | 0.1% |
| LOAD_ATTR | 4,960 | 0.1% |
| LOAD_DEREF | 4,940 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 8,009,380 | 98.2% |
| LOAD_FAST | 81,820 | 1.0% |
| LOAD_CONST | 18,800 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 18,740 | 0.2% |
| LOAD_FAST_LOAD_FAST | 13,420 | 0.2% |


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
| LOAD_FAST | 54,880 | 0.3% |
| CALL | 19,760 | 0.1% |
| POP_JUMP_IF_FALSE | 14,120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,010,500 | 49.5% |
| LOAD_FAST_LOAD_FAST | 5,242,880 | 32.4% |
| CALL_ALLOC_AND_ENTER_INIT | 2,757,120 | 17.0% |
| STORE_FAST | 53,640 | 0.3% |
| TO_BOOL_BOOL | 42,220 | 0.3% |


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
| STORE_SUBSCR | 500 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,780 | 72.2% |
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
| LOAD_FAST | 4,240 | 0.1% |
| TO_BOOL | 2,320 | 0.0% |
| CALL | 1,340 | 0.0% |
| LOAD_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,008,620 | 99.9% |
| TO_BOOL | 2,320 | 0.0% |
| POP_JUMP_IF_TRUE | 2,200 | 0.0% |
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
| BINARY_OP | 3,740 | 0.0% |
| LOAD_FAST_LOAD_FAST | 2,300 | 0.0% |
| LOAD_FAST | 1,380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,004,800 | 99.5% |
| TO_BOOL_INT | 11,860 | 0.1% |
| STORE_SUBSCR | 10,340 | 0.1% |
| BINARY_OP | 3,740 | 0.0% |
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
| SWAP | 10,260 | 26.0% |
| LOAD_ATTR_INSTANCE_VALUE | 4,800 | 12.2% |
| STORE_ATTR_INSTANCE_VALUE | 4,120 | 10.4% |
| LOAD_FAST | 4,040 | 10.2% |
| RESUME_CHECK | 3,880 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,300 | 26.1% |
| SWAP | 10,260 | 26.0% |
| STORE_FAST | 9,820 | 24.9% |
| COMPARE_OP | 4,800 | 12.2% |
| CALL_METHOD_DESCRIPTOR_O | 2,060 | 5.2% |


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
| LOAD_CONST | 14,000 | 77.3% |
| FORMAT_SIMPLE | 4,120 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,400 | 29.8% |
| LIST_APPEND | 5,360 | 29.6% |
| LOAD_FAST | 3,420 | 18.9% |
| YIELD_VALUE | 1,540 | 8.5% |
| CALL_BUILTIN_O | 1,540 | 8.5% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,500 | 41.9% |
| LOAD_FAST_LOAD_FAST | 5,080 | 10.9% |
| LOAD_GLOBAL_MODULE | 3,820 | 8.2% |
| CALL_BUILTIN_O | 2,940 | 6.3% |
| BUILD_TUPLE | 2,140 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,620 | 22.8% |
| STORE_FAST | 6,620 | 14.2% |
| RETURN_VALUE | 6,080 | 13.1% |
| LOAD_FAST | 3,600 | 7.7% |
| CONTAINS_OP | 2,840 | 6.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 8,009,380 | 49.5% |
| LOAD_ATTR_INSTANCE_VALUE | 8,001,660 | 49.4% |
| LOAD_CONST | 48,840 | 0.3% |
| LOAD_FAST | 32,100 | 0.2% |
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
| CALL_INTRINSIC_1 | 3,860 | 30.7% |
| LOAD_FAST | 1,560 | 12.4% |
| STORE_FAST | 480 | 3.8% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.5% |

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
| LOAD_CONST | 23,260 | 22.9% |
| LOAD_GLOBAL_MODULE | 22,940 | 22.6% |
| LOAD_FAST | 22,440 | 22.1% |
| LOAD_FAST_LOAD_FAST | 18,960 | 18.7% |
| LOAD_ATTR | 4,040 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 78,000 | 76.8% |
| POP_JUMP_IF_TRUE | 12,940 | 12.7% |
| EXTENDED_ARG | 5,740 | 5.7% |
| STORE_FAST | 4,040 | 4.0% |
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
| COMPARE_OP_STR | 10,820 | 14.9% |
| COMPARE_OP_INT | 9,700 | 13.3% |
| SWAP | 9,360 | 12.9% |
| CALL | 9,160 | 12.6% |
| CALL_BUILTIN_FAST | 8,360 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 49,020 | 67.4% |
| COMPARE_OP_STR | 9,360 | 12.9% |
| TO_BOOL_STR | 5,240 | 7.2% |
| STORE_FAST_STORE_FAST | 2,120 | 2.9% |
| LOAD_FAST | 1,440 | 2.0% |


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
| FOR_ITER | 60 | 20.0% |
| POP_TOP | 20 | 6.7% |

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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,140 | 22.0% |
| POP_TOP | 7,860 | 13.1% |
| JUMP_FORWARD | 6,040 | 10.1% |
| CONTAINS_OP | 5,740 | 9.6% |
| GET_ITER | 5,540 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,900 | 28.3% |
| POP_JUMP_IF_FALSE | 13,160 | 22.0% |
| FOR_ITER_LIST | 9,420 | 15.8% |
| FOR_ITER | 9,260 | 15.5% |
| JUMP_FORWARD | 6,160 | 10.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 57,540 | 77.2% |
| EXTENDED_ARG | 9,260 | 12.4% |
| GET_ITER | 3,100 | 4.2% |
| LOAD_FAST | 2,140 | 2.9% |
| FOR_ITER | 2,120 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 34,000 | 45.6% |
| STORE_FAST | 29,040 | 38.9% |
| RETURN_CONST | 4,420 | 5.9% |
| FOR_ITER | 2,120 | 2.8% |
| STORE_NAME | 1,040 | 1.4% |


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
| LOAD_GLOBAL_MODULE | 43,500 | 83.4% |
| LOAD_GLOBAL_BUILTIN | 5,880 | 11.3% |
| LOAD_FAST | 1,540 | 3.0% |
| LOAD_CONST | 880 | 1.7% |
| LOAD_GLOBAL | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 45,740 | 87.7% |
| POP_JUMP_IF_TRUE | 5,360 | 10.3% |
| RETURN_VALUE | 400 | 0.8% |
| COPY | 300 | 0.6% |
| STORE_FAST | 180 | 0.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 117,532,740 | 93.5% |
| STORE_FAST | 8,002,480 | 6.4% |
| POP_JUMP_IF_TRUE | 46,620 | 0.0% |
| LIST_APPEND | 33,760 | 0.0% |
| EXTENDED_ARG | 16,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 125,515,680 | 99.9% |
| FOR_ITER | 57,540 | 0.0% |
| FOR_ITER_TUPLE | 44,620 | 0.0% |
| FOR_ITER_LIST | 22,340 | 0.0% |
| FOR_ITER_RANGE | 22,000 | 0.0% |


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
| EXTENDED_ARG | 6,040 | 17.2% |
| LOAD_GLOBAL_BUILTIN | 5,700 | 16.2% |
| LOAD_FAST_LOAD_FAST | 2,400 | 6.8% |
| COPY | 1,640 | 4.7% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 20,400 | 60.4% |
| BUILD_STRING | 5,360 | 15.9% |
| LOAD_FAST | 2,960 | 8.8% |
| CALL_BUILTIN_CLASS | 2,560 | 7.6% |
| BUILD_TUPLE | 2,060 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 33,760 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,720 | 80.8% |
| LOAD_CONST | 620 | 10.6% |
| LOAD_ATTR | 180 | 3.1% |
| LOAD_ATTR_SLOT | 140 | 2.4% |
| CALL_KW | 80 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 5,040 | 86.3% |
| STORE_NAME | 240 | 4.1% |
| LOAD_FAST | 160 | 2.7% |
| BUILD_LIST | 140 | 2.4% |
| LOAD_CONST | 140 | 2.4% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,500 | 64.8% |
| LOAD_FAST_LOAD_FAST | 10,060 | 9.1% |
| LOAD_NAME | 6,560 | 5.9% |
| LOAD_ATTR | 5,240 | 4.7% |
| LOAD_GLOBAL_BUILTIN | 4,960 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,940 | 17.2% |
| LOAD_ATTR_METHOD_NO_DICT | 17,080 | 15.5% |
| LOAD_FAST | 14,100 | 12.8% |
| CALL | 12,140 | 11.0% |
| LOAD_ATTR | 5,240 | 4.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 133,515,680 | 73.3% |
| LOAD_FAST | 32,244,900 | 17.7% |
| LOAD_FAST_LOAD_FAST | 8,006,660 | 4.4% |
| BINARY_OP_ADD_INT | 8,001,980 | 4.4% |
| LOAD_CONST | 97,860 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 133,515,720 | 73.3% |
| COMPARE_OP_INT | 16,037,000 | 8.8% |
| LOAD_FAST | 8,060,920 | 4.4% |
| BINARY_OP_ADD_INT | 8,041,600 | 4.4% |
| BINARY_SLICE | 8,019,380 | 4.4% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 28,980 | 55.7% |
| POP_JUMP_IF_FALSE | 6,660 | 12.8% |
| RESUME_CHECK | 3,760 | 7.2% |
| STORE_FAST | 3,620 | 7.0% |
| BINARY_SLICE | 2,000 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,940 | 57.6% |
| PUSH_NULL | 4,940 | 9.5% |
| LOAD_CONST | 3,600 | 6.9% |
| TO_BOOL_BOOL | 3,040 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 2,220 | 4.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 141,741,880 | 49.3% |
| POP_JUMP_IF_FALSE | 42,967,260 | 15.0% |
| RESUME_CHECK | 32,132,900 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 16,147,980 | 5.6% |
| LOAD_GLOBAL_MODULE | 8,089,900 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 117,515,680 | 40.9% |
| LOAD_ATTR_INSTANCE_VALUE | 80,260,380 | 27.9% |
| LOAD_CONST | 32,244,900 | 11.2% |
| CALL_LEN | 16,042,360 | 5.6% |
| PUSH_NULL | 8,089,960 | 2.8% |


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
| STORE_ATTR_INSTANCE_VALUE | 16,032,660 | 33.2% |
| LOAD_GLOBAL_MODULE | 16,024,240 | 33.2% |
| RESUME_CHECK | 8,024,660 | 16.6% |
| RETURN_VALUE | 5,242,880 | 10.9% |
| RETURN_CONST | 2,757,200 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 24,053,440 | 49.8% |
| LOAD_ATTR_INSTANCE_VALUE | 8,014,900 | 16.6% |
| LOAD_CONST | 8,006,660 | 16.6% |
| BINARY_SUBSCR | 8,000,040 | 16.6% |
| LOAD_FAST | 44,700 | 0.1% |


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
| STORE_FAST | 21,000 | 23.5% |
| LOAD_NAME | 20,100 | 22.5% |
| STORE_NAME | 18,900 | 21.2% |
| LOAD_CONST | 7,220 | 8.1% |
| RESUME | 4,220 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 20,720 | 23.2% |
| LOAD_NAME | 20,100 | 22.5% |
| LOAD_CONST | 10,100 | 11.3% |
| PUSH_NULL | 6,740 | 7.5% |
| LOAD_ATTR | 6,560 | 7.3% |


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
| COMPARE_OP_INT | 16,036,700 | 28.4% |
| TO_BOOL_BOOL | 8,122,980 | 14.4% |
| TO_BOOL_NONE | 8,010,860 | 14.2% |
| TO_BOOL | 8,008,620 | 14.2% |
| TO_BOOL_LIST | 8,006,960 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,967,260 | 76.1% |
| RETURN_CONST | 13,268,380 | 23.5% |
| LOAD_GLOBAL_MODULE | 37,740 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 34,060 | 0.1% |
| POP_TOP | 25,700 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,019,560 | 99.8% |
| LOAD_ATTR_INSTANCE_VALUE | 7,780 | 0.1% |
| LOAD_GLOBAL_MODULE | 3,020 | 0.0% |
| LOAD_ATTR_MODULE | 2,060 | 0.0% |
| RETURN_VALUE | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,016,420 | 99.8% |
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
| LOAD_FAST | 58,100 | 71.4% |
| LOAD_ATTR_INSTANCE_VALUE | 8,060 | 9.9% |
| CALL_BUILTIN_FAST | 7,080 | 8.7% |
| LOAD_FAST_CHECK | 4,740 | 5.8% |
| LOAD_GLOBAL_MODULE | 2,760 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,820 | 57.6% |
| LOAD_GLOBAL_MODULE | 12,760 | 15.7% |
| JUMP_BACKWARD | 9,140 | 11.2% |
| NOP | 4,000 | 4.9% |
| LOAD_CONST | 2,400 | 3.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 100,500 | 59.1% |
| TO_BOOL_STR | 25,980 | 15.3% |
| CONTAINS_OP | 12,940 | 7.6% |
| COMPARE_OP_INT | 8,120 | 4.8% |
| TO_BOOL_INT | 7,240 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,420 | 35.5% |
| JUMP_BACKWARD | 46,620 | 27.4% |
| LOAD_GLOBAL_BUILTIN | 17,880 | 10.5% |
| LOAD_GLOBAL_MODULE | 15,560 | 9.1% |
| POP_TOP | 9,580 | 5.6% |


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
| POP_JUMP_IF_FALSE | 13,268,380 | 27.6% |
| STORE_ATTR_INSTANCE_VALUE | 8,034,960 | 16.7% |
| END_ASYNC_FOR | 2,757,200 | 5.7% |
| RESUME_CHECK | 7,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 24,063,900 | 50.0% |
| POP_TOP | 8,057,820 | 16.7% |
| EXIT_INIT_CHECK | 8,009,440 | 16.6% |
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
| LOAD_FAST | 18,560 | 62.3% |
| LOAD_FAST_LOAD_FAST | 7,740 | 26.0% |
| STORE_ATTR | 1,960 | 6.6% |
| SWAP | 580 | 1.9% |
| LOAD_NAME | 380 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,120 | 40.7% |
| RETURN_CONST | 3,400 | 11.4% |
| LOAD_CONST | 2,620 | 8.8% |
| LOAD_FAST_LOAD_FAST | 2,360 | 7.9% |
| STORE_ATTR | 1,960 | 6.6% |


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
| END_SEND | 125,515,680 | 79.4% |
| CALL_LEN | 16,005,300 | 10.1% |
| CALL | 8,026,240 | 5.1% |
| BINARY_OP | 8,004,800 | 5.1% |
| LOAD_ATTR_INSTANCE_VALUE | 59,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 141,741,880 | 89.7% |
| LOAD_GLOBAL_MODULE | 8,044,600 | 5.1% |
| JUMP_BACKWARD | 8,002,480 | 5.1% |
| NOP | 47,500 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 46,960 | 0.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 22,780 | 79.7% |
| FOR_ITER_LIST | 3,020 | 10.6% |
| CALL_LEN | 2,720 | 9.5% |
| FOR_ITER | 60 | 0.2% |
| COPY | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 20,400 | 71.3% |
| PUSH_NULL | 2,720 | 9.5% |
| LOAD_FAST | 2,120 | 7.4% |
| FORMAT_SIMPLE | 1,540 | 5.4% |
| LOAD_CONST | 1,340 | 4.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 47,700 | 90.9% |
| UNPACK_SEQUENCE_TUPLE | 2,380 | 4.5% |
| COPY | 2,120 | 4.0% |
| UNPACK_SEQUENCE | 180 | 0.3% |
| STORE_FAST_STORE_FAST | 120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,040 | 59.1% |
| NOP | 9,640 | 18.4% |
| LOAD_FAST_LOAD_FAST | 5,060 | 9.6% |
| STORE_FAST | 2,260 | 4.3% |
| LOAD_GLOBAL_MODULE | 1,700 | 3.2% |


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
| MAKE_FUNCTION | 26,000 | 28.6% |
| LOAD_CONST | 15,420 | 16.9% |
| SET_FUNCTION_ATTRIBUTE | 8,040 | 8.8% |
| CALL | 7,780 | 8.6% |
| LOAD_NAME | 5,680 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,800 | 54.7% |
| LOAD_NAME | 18,900 | 20.8% |
| STORE_NAME | 4,640 | 5.1% |
| RETURN_CONST | 4,040 | 4.4% |
| LOAD_BUILD_CLASS | 3,640 | 4.0% |


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
| BUILD_STRING | 1,540 | 0.0% |
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
| LOAD_FAST_LOAD_FAST | 13,400 | 63.0% |
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
| LOAD_FAST | 24,300 | 85.8% |
| LOAD_CONST | 2,000 | 7.1% |
| LOAD_FAST_LOAD_FAST | 1,020 | 3.6% |
| LOAD_DEREF | 460 | 1.6% |
| BUILD_TUPLE | 240 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,100 | 39.2% |
| PUSH_EXC_INFO | 6,260 | 22.1% |
| STORE_FAST | 4,440 | 15.7% |
| PUSH_NULL | 2,960 | 10.5% |
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
| PUSH_NULL | 18,740 | 44.6% |
| LOAD_CONST | 11,860 | 28.2% |
| LOAD_FAST | 7,020 | 16.7% |
| LOAD_FAST_LOAD_FAST | 2,140 | 5.1% |
| BUILD_TUPLE | 2,040 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 37,180 | 88.4% |
| POP_TOP | 4,660 | 11.1% |
| COPY_FREE_VARS | 100 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 80 | 0.2% |
| CALL_PY_EXACT_ARGS | 40 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,600 | 23.3% |
| LOAD_GLOBAL_BUILTIN | 1,720 | 15.4% |
| CALL_LEN | 1,340 | 12.0% |
| LOAD_FAST | 1,160 | 10.4% |
| BINARY_SUBSCR_DICT | 1,000 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,280 | 29.4% |
| LIST_APPEND | 2,560 | 22.9% |
| LOAD_CONST | 1,480 | 13.3% |
| GET_ITER | 900 | 8.1% |
| RETURN_VALUE | 740 | 6.6% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 25,880 | 45.5% |
| LOAD_FAST | 13,340 | 23.4% |
| LOAD_FAST_LOAD_FAST | 8,900 | 15.6% |
| LOAD_ATTR_SLOT | 3,700 | 6.5% |
| LOAD_GLOBAL_MODULE | 3,280 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 14,460 | 25.4% |
| STORE_FAST | 10,760 | 18.9% |
| TO_BOOL_BOOL | 9,160 | 16.1% |
| COPY | 8,360 | 14.7% |
| POP_JUMP_IF_NOT_NONE | 7,080 | 12.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,440 | 70.0% |
| LOAD_GLOBAL_MODULE | 4,240 | 10.1% |
| LOAD_CONST | 3,300 | 7.8% |
| RETURN_GENERATOR | 2,000 | 4.8% |
| LOAD_FAST_LOAD_FAST | 1,200 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 20,720 | 49.2% |
| STORE_FAST | 7,360 | 17.5% |
| RETURN_VALUE | 7,180 | 17.1% |
| BUILD_TUPLE | 2,120 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 2,120 | 5.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,520 | 45.0% |
| LOAD_GLOBAL_MODULE | 4,480 | 13.9% |
| LOAD_CONST | 3,500 | 10.8% |
| BINARY_SUBSCR_TUPLE_INT | 3,080 | 9.5% |
| BUILD_STRING | 1,540 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,240 | 68.9% |
| BUILD_TUPLE | 2,940 | 9.1% |
| STORE_FAST | 2,900 | 9.0% |
| TO_BOOL_BOOL | 2,700 | 8.4% |
| TO_BOOL_INT | 1,220 | 3.8% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 27,060 | 64.0% |
| LOAD_GLOBAL_MODULE | 10,980 | 26.0% |
| BUILD_TUPLE | 1,800 | 4.3% |
| LOAD_NAME | 1,500 | 3.5% |
| CALL | 440 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 41,060 | 97.1% |
| RETURN_VALUE | 480 | 1.1% |
| TO_BOOL | 440 | 1.0% |
| LOAD_FAST | 240 | 0.6% |
| YIELD_VALUE | 60 | 0.1% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,042,360 | 99.9% |
| LOAD_ATTR_INSTANCE_VALUE | 15,140 | 0.1% |
| POP_JUMP_IF_TRUE | 3,180 | 0.0% |
| LOAD_NAME | 1,360 | 0.0% |
| LOAD_ATTR | 1,060 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,005,300 | 99.6% |
| LOAD_CONST | 24,700 | 0.2% |
| LOAD_FAST | 12,540 | 0.1% |
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
| BUILD_TUPLE | 2,600 | 11.5% |
| LOAD_FAST_CHECK | 620 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 7,460 | 32.9% |
| RETURN_CONST | 6,640 | 29.3% |
| LOAD_FAST | 3,800 | 16.8% |
| JUMP_BACKWARD | 2,240 | 9.9% |
| LOAD_GLOBAL_BUILTIN | 940 | 4.1% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 22,840 | 45.5% |
| LOAD_FAST | 10,960 | 21.8% |
| BUILD_MAP | 5,960 | 11.9% |
| LOAD_ATTR_METHOD_NO_DICT | 4,660 | 9.3% |
| LOAD_CONST | 1,600 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 20,400 | 40.6% |
| STORE_FAST | 18,420 | 36.7% |
| POP_TOP | 8,280 | 16.5% |
| LOAD_FAST | 1,220 | 2.4% |
| SWAP | 1,000 | 2.0% |


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
| LOAD_ATTR_METHOD_NO_DICT | 4,780 | 85.7% |
| CALL | 380 | 6.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 180 | 3.2% |
| LOAD_ATTR | 120 | 2.2% |
| LOAD_FAST | 120 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,000 | 35.8% |
| GET_ITER | 960 | 17.2% |
| BUILD_TUPLE | 700 | 12.5% |
| BINARY_OP | 400 | 7.2% |
| POP_TOP | 380 | 6.8% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,004,620 | 49.9% |
| CALL | 8,000,340 | 49.9% |
| STORE_FAST | 9,200 | 0.1% |
| LOAD_CONST | 8,740 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 3,700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 16,010,620 | 99.9% |
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
| LOAD_FAST | 8,069,700 | 33.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,460 | 0.2% |
| LOAD_FAST_LOAD_FAST | 10,620 | 0.0% |
| CALL | 5,780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 24,137,700 | 100.0% |
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
| LOAD_FAST | 3,380 | 71.9% |
| LOAD_GLOBAL_MODULE | 1,020 | 21.7% |
| LOAD_CONST | 200 | 4.3% |
| CALL | 80 | 1.7% |
| LOAD_ATTR_MODULE | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,480 | 52.8% |
| PUSH_NULL | 1,040 | 22.1% |
| LOAD_FAST_LOAD_FAST | 480 | 10.2% |
| LOAD_FAST | 460 | 9.8% |
| BUILD_TUPLE | 100 | 2.1% |


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
| LOAD_CONST | 16,037,000 | 99.9% |
| LOAD_FAST | 16,180 | 0.1% |
| CALL_LEN | 2,140 | 0.0% |
| BINARY_OP | 1,000 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,036,700 | 99.9% |
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
| POP_JUMP_IF_FALSE | 62,940 | 78.1% |
| COPY | 10,820 | 13.4% |
| EXTENDED_ARG | 3,960 | 4.9% |
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
| JUMP_BACKWARD | 22,340 | 54.8% |
| EXTENDED_ARG | 9,420 | 23.1% |
| GET_ITER | 8,560 | 21.0% |
| LOAD_FAST | 240 | 0.6% |
| FOR_ITER | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 15,900 | 39.0% |
| STORE_FAST | 14,180 | 34.8% |
| STORE_FAST_LOAD_FAST | 3,020 | 7.4% |
| LOAD_GLOBAL_BUILTIN | 2,420 | 5.9% |
| LOAD_FAST | 2,160 | 5.3% |


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
| JUMP_BACKWARD | 44,620 | 69.4% |
| SWAP | 9,660 | 15.0% |
| GET_ITER | 8,700 | 13.5% |
| LOAD_FAST | 980 | 1.5% |
| FOR_ITER | 380 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 22,780 | 35.4% |
| STORE_FAST | 20,480 | 31.8% |
| SWAP | 9,700 | 15.1% |
| LOAD_FAST | 4,180 | 6.5% |
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
| LOAD_FAST | 80,260,380 | 90.9% |
| LOAD_FAST_LOAD_FAST | 8,014,900 | 9.1% |
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
| LOAD_ATTR_INSTANCE_VALUE | 16,024,660 | 99.2% |
| LOAD_FAST | 83,520 | 0.5% |
| LOAD_ATTR | 17,080 | 0.1% |
| LOAD_GLOBAL_MODULE | 13,880 | 0.1% |
| LOAD_CONST | 4,340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,055,480 | 49.9% |
| LOAD_GLOBAL_MODULE | 8,024,060 | 49.7% |
| LOAD_CONST | 55,740 | 0.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,780 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 4,660 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,005,280 | 99.4% |
| LOAD_FAST | 45,360 | 0.6% |
| LOAD_GLOBAL_MODULE | 3,700 | 0.0% |
| LOAD_ATTR | 1,120 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,015,520 | 99.5% |
| CALL_PY_EXACT_ARGS | 36,460 | 0.5% |
| LOAD_FAST_LOAD_FAST | 2,940 | 0.0% |
| LOAD_CONST | 1,260 | 0.0% |
| CALL | 620 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 99,300 | 80.2% |
| LOAD_NAME | 20,720 | 16.7% |
| LOAD_FAST | 2,720 | 2.2% |
| LOAD_ATTR | 1,040 | 0.8% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 37,360 | 30.2% |
| CALL | 29,020 | 23.4% |
| LOAD_FAST | 13,860 | 11.2% |
| LOAD_ATTR_SLOT | 12,200 | 9.9% |
| LOAD_CONST | 8,960 | 7.2% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 600 | 90.9% |
| LOAD_FAST | 40 | 6.1% |
| LOAD_ATTR | 20 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 600 | 90.9% |
| LOAD_FAST | 60 | 9.1% |


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
| LOAD_ATTR_MODULE | 12,200 | 49.7% |
| LOAD_FAST | 9,720 | 39.6% |
| RETURN_VALUE | 1,700 | 6.9% |
| LOAD_ATTR | 360 | 1.5% |
| CALL_BUILTIN_FAST | 300 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,040 | 49.1% |
| LOAD_CONST | 4,500 | 18.3% |
| CALL_BUILTIN_FAST | 3,700 | 15.1% |
| STORE_FAST | 1,700 | 6.9% |
| LOAD_FAST_LOAD_FAST | 520 | 2.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,058,320 | 98.7% |
| STORE_FAST | 46,960 | 0.3% |
| POP_JUMP_IF_FALSE | 34,060 | 0.2% |
| LOAD_FAST | 28,720 | 0.2% |
| POP_JUMP_IF_TRUE | 17,880 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,147,980 | 99.3% |
| LOAD_DEREF | 28,980 | 0.2% |
| CALL_ISINSTANCE | 27,060 | 0.2% |
| LOAD_FAST_LOAD_FAST | 19,460 | 0.1% |
| CHECK_EXC_MATCH | 7,920 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,044,600 | 24.8% |
| LOAD_ATTR_METHOD_NO_DICT | 8,024,060 | 24.8% |
| LOAD_GLOBAL_MODULE | 8,007,020 | 24.7% |
| BINARY_SUBSCR | 7,999,960 | 24.7% |
| LOAD_FAST | 108,660 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,024,240 | 49.4% |
| LOAD_FAST | 8,089,900 | 25.0% |
| LOAD_GLOBAL_MODULE | 8,007,020 | 24.7% |
| LOAD_ATTR_MODULE | 99,300 | 0.3% |
| IS_OP | 43,500 | 0.1% |


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
| CALL_PY_EXACT_ARGS | 24,137,700 | 13.3% |
| CALL_ALLOC_AND_ENTER_INIT | 8,009,440 | 4.4% |
| POP_TOP | 8,003,340 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 37,180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 125,520,720 | 69.0% |
| LOAD_FAST | 32,132,900 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 16,058,320 | 8.8% |
| LOAD_FAST_LOAD_FAST | 8,024,660 | 4.4% |
| LOAD_GLOBAL_MODULE | 78,760 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 24,053,440 | 99.7% |
| LOAD_FAST | 64,800 | 0.3% |
| STORE_ATTR | 1,240 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 240 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,032,660 | 66.5% |
| RETURN_CONST | 8,034,960 | 33.3% |
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
| LOAD_FAST | 15,540 | 51.2% |
| LOAD_CONST | 5,640 | 18.6% |
| LOAD_FAST_LOAD_FAST | 3,040 | 10.0% |
| LOAD_ATTR_INSTANCE_VALUE | 2,440 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,000 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,280 | 27.3% |
| LOAD_FAST | 6,300 | 20.7% |
| LOAD_GLOBAL_MODULE | 3,240 | 10.7% |
| JUMP_FORWARD | 3,040 | 10.0% |
| LOAD_NAME | 1,440 | 4.7% |


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
| COPY | 49,020 | 0.6% |
| RETURN_VALUE | 42,220 | 0.5% |
| CALL_ISINSTANCE | 41,060 | 0.5% |
| LOAD_FAST | 27,980 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,122,980 | 98.7% |
| POP_JUMP_IF_TRUE | 100,500 | 1.2% |
| EXTENDED_ARG | 3,420 | 0.0% |
| UNARY_NOT | 60 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,860 | 48.3% |
| LOAD_FAST | 6,160 | 25.1% |
| CALL_LEN | 3,700 | 15.1% |
| COPY | 1,240 | 5.0% |
| CALL_BUILTIN_O | 1,220 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 15,760 | 64.1% |
| POP_JUMP_IF_TRUE | 7,240 | 29.5% |
| UNARY_NOT | 1,560 | 6.3% |
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
| LOAD_ATTR_INSTANCE_VALUE | 7,998,960 | 99.0% |
| TO_BOOL_ALWAYS_TRUE | 68,860 | 0.9% |
| LOAD_FAST | 11,780 | 0.1% |
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
| STORE_FAST_LOAD_FAST | 20,400 | 66.5% |
| COPY | 5,240 | 17.1% |
| LOAD_FAST | 4,900 | 16.0% |
| TO_BOOL | 60 | 0.2% |
| LOAD_GLOBAL_MODULE | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 25,980 | 84.7% |
| POP_JUMP_IF_FALSE | 4,700 | 15.3% |


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
| FOR_ITER | 34,000 | 56.6% |
| FOR_ITER_LIST | 15,900 | 26.4% |
| RETURN_VALUE | 9,220 | 15.3% |
| UNPACK_SEQUENCE | 280 | 0.5% |
| LOAD_CONST | 260 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 47,700 | 79.3% |
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
|     deferred | 8,037,320 | 49.8% |
|          hit | 8,083,280 | 50.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 500 | 12.0% |
| Failure | 3,680 | 88.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 2,340 | 63.6% |
| and int | 640 | 17.4% |
| or | 300 | 8.2% |
| add other | 180 | 4.9% |
| power | 80 | 2.2% |
| add different types | 60 | 1.6% |
| multiply different types | 60 | 1.6% |
| and different types | 20 | 0.5% |


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
|     deferred | 8,012,640 | 98.6% |
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
|     deferred | 71,880 | 35.2% |
|          hit | 129,460 | 63.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 580 | 21.5% |
| Failure | 2,120 | 78.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict values | 840 | 39.6% |
| dict items | 700 | 33.0% |
| set | 180 | 8.5% |
| itertools | 180 | 8.5% |
| map | 120 | 5.7% |
| seq iter | 40 | 1.9% |
| dict keys | 20 | 0.9% |
| enumerate | 20 | 0.9% |
| zip | 20 | 0.9% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 115,020 | 0.1% |
|        deopt | 360 | 0.0% |
|          hit | 112,630,100 | 99.9% |
|         miss | 14,600 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,180 | 61.8% |
| Failure | 3,820 | 38.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 2,480 | 64.9% |
| method | 460 | 12.0% |
| not managed dict | 340 | 8.9% |
| module attr not found | 140 | 3.7% |
| has managed dict | 120 | 3.1% |
| class method obj | 60 | 1.6% |
| class attr descriptor | 60 | 1.6% |
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
|     deferred | 126,660 | 0.3% |
|        deopt | 2,620 | 0.0% |
|          hit | 48,560,460 | 99.7% |
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
|     deferred | 38,820 | 0.2% |
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
|     deferred | 18,340 | 31.8% |
|          hit | 38,560 | 66.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 32.4% |
| Failure | 500 | 67.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 460 | 92.0% |
| py simple | 40 | 8.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,179,740 | 37.5% |
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
| Basic | 1,738,123,720 | 70.0% |
| Not specialized | 254,830,980 | 10.3% |
| Specialized hits | 481,421,140 | 19.4% |
| Specialized misses | 7,495,880 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| SEND | 133,515,700 | 73.6% |
| CALL | 16,208,680 | 8.9% |
| TO_BOOL | 15,179,740 | 8.4% |
| BINARY_OP | 8,037,320 | 4.4% |
| BINARY_SUBSCR | 8,012,640 | 4.4% |
| LOAD_GLOBAL | 126,660 | 0.1% |
| LOAD_ATTR | 115,020 | 0.1% |
| FOR_ITER | 71,880 | 0.0% |
| STORE_ATTR | 38,820 | 0.0% |
| STORE_SUBSCR | 18,340 | 0.0% |


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
| Frames pushed | 40,204,960 | 21.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 259,435,520 | 52.3% |
| Frees to freelist | 259,432,260 |  |
| Allocations | 236,282,480 | 47.7% |
| Allocations to 512 bytes | 236,241,960 | 47.7% |
| Allocations to 4 kbytes | 37,600 | 0.0% |
| Allocations over 4 kbytes | 2,920 | 0.0% |
| Frees | 235,699,285 |  |
| New values | 10,380 |  |
| Interpreter increfs | 1,008,950,520 | 58.7% |
| Interpreter decrefs | 1,463,456,440 | 62.1% |
| Increfs | 710,398,502 | 41.3% |
| Decrefs | 891,926,995 | 37.9% |
| Materialize dict (on request) | 140 | 1.3% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 80 | 0.8% |
| Method cache hits | 177,226 |  |
| Method cache misses | 57,374 |  |
| Method cache collisions | 64,636 |  |
| Method cache dunder hits | 8,317,028 |  |
| Method cache dunder misses | 22,212 |  |


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
| func modification | 80 |
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
