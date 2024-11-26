
# Pystats results

- benchmark: asyncio_websockets
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 3,993,154 | 18.5% | 18.5% |  |
| POP_JUMP_IF_FALSE | 1,138,208 | 5.3% | 23.8% |  |
| LOAD_CONST | 1,135,878 | 5.3% | 29.1% |  |
| RESUME_CHECK | 863,860 | 4.0% | 33.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 816,880 | 3.8% | 36.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 777,016 | 3.6% | 40.5% | 0.1% |
| LOAD_GLOBAL_MODULE | 750,260 | 3.5% | 44.0% | 0.1% |
| STORE_FAST | 736,560 | 3.4% | 47.4% |  |
| LOAD_ATTR | 663,400 | 3.1% | 50.5% |  |
| TO_BOOL_BOOL | 641,220 | 3.0% | 53.4% |  |
| LOAD_GLOBAL_BUILTIN | 616,307 | 2.9% | 56.3% | 0.4% |
| POP_TOP | 565,761 | 2.6% | 58.9% |  |
| RETURN_VALUE | 519,840 | 2.4% | 61.3% |  |
| CALL_PY_EXACT_ARGS | 416,980 | 1.9% | 63.3% | 0.1% |
| RETURN_CONST | 384,180 | 1.8% | 65.0% |  |
| CALL | 359,499 | 1.7% | 66.7% |  |
| LOAD_ATTR_SLOT | 358,640 | 1.7% | 68.4% | 1.4% |
| PUSH_NULL | 289,960 | 1.3% | 69.7% |  |
| LOAD_ATTR_MODULE | 279,720 | 1.3% | 71.0% | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 266,660 | 1.2% | 72.3% | 0.0% |
| POP_JUMP_IF_TRUE | 261,200 | 1.2% | 73.5% |  |
| COMPARE_OP_INT | 245,648 | 1.1% | 74.6% | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 236,281 | 1.1% | 75.7% | 0.4% |
| LOAD_ATTR_WITH_HINT | 229,640 | 1.1% | 76.8% | 3.2% |
| STORE_ATTR | 225,700 | 1.0% | 77.8% |  |
| BINARY_OP | 215,700 | 1.0% | 78.8% |  |
| INTERPRETER_EXIT | 209,720 | 1.0% | 79.8% |  |
| CALL_LEN | 192,688 | 0.9% | 80.7% |  |
| STORE_ATTR_SLOT | 180,220 | 0.8% | 81.5% | 4.7% |
| POP_JUMP_IF_NONE | 165,840 | 0.8% | 82.3% |  |
| RETURN_GENERATOR | 159,800 | 0.7% | 83.0% |  |
| SEND_GEN | 154,200 | 0.7% | 83.8% |  |
| GET_AWAITABLE | 151,360 | 0.7% | 84.5% |  |
| END_SEND | 151,040 | 0.7% | 85.2% |  |
| ENTER_EXECUTOR | 150,620 | 0.7% | 85.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 149,420 | 0.7% | 86.5% | 0.8% |
| CALL_BUILTIN_FAST | 138,760 | 0.6% | 87.2% | 0.0% |
| IS_OP | 131,520 | 0.6% | 87.8% |  |
| POP_JUMP_IF_NOT_NONE | 129,180 | 0.6% | 88.4% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 115,481 | 0.5% | 88.9% | 8.6% |
| JUMP_FORWARD | 106,921 | 0.5% | 89.4% |  |
| NOP | 99,760 | 0.5% | 89.9% |  |
| CALL_KW | 99,400 | 0.5% | 90.4% |  |
| CALL_FUNCTION_EX | 93,740 | 0.4% | 90.8% |  |
| BUILD_TUPLE | 90,600 | 0.4% | 91.2% |  |
| LOAD_DEREF | 88,480 | 0.4% | 91.6% |  |
| TO_BOOL_NONE | 83,880 | 0.4% | 92.0% | 0.1% |
| CONTAINS_OP | 83,400 | 0.4% | 92.4% |  |
| TO_BOOL | 81,280 | 0.4% | 92.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 78,960 | 0.4% | 93.1% | 1.0% |
| BUILD_MAP | 71,460 | 0.3% | 93.5% |  |
| GET_ITER | 70,860 | 0.3% | 93.8% |  |
| BINARY_SLICE | 70,219 | 0.3% | 94.1% |  |
| DICT_MERGE | 67,580 | 0.3% | 94.4% |  |
| TO_BOOL_INT | 61,660 | 0.3% | 94.7% | 0.1% |
| COMPARE_OP | 59,460 | 0.3% | 95.0% |  |
| CALL_TYPE_1 | 59,320 | 0.3% | 95.3% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 51,940 | 0.2% | 95.5% | 19.1% |
| FOR_ITER | 50,020 | 0.2% | 95.8% |  |
| CALL_ISINSTANCE | 44,400 | 0.2% | 96.0% |  |
| STORE_SUBSCR_DICT | 42,700 | 0.2% | 96.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 35,860 | 0.2% | 96.3% | 92.8% |
| DELETE_SUBSCR | 33,919 | 0.2% | 96.5% |  |
| BUILD_SLICE | 33,659 | 0.2% | 96.6% |  |
| FOR_ITER_LIST | 33,540 | 0.2% | 96.8% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 32,460 | 0.2% | 96.9% |  |
| LOAD_GLOBAL | 31,960 | 0.1% | 97.1% |  |
| STORE_FAST_STORE_FAST | 28,100 | 0.1% | 97.2% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 26,020 | 0.1% | 97.3% |  |
| COPY | 24,040 | 0.1% | 97.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 23,560 | 0.1% | 97.6% |  |
| CALL_LIST_APPEND | 23,480 | 0.1% | 97.7% |  |
| STORE_DEREF | 21,720 | 0.1% | 97.8% |  |
| BINARY_OP_ADD_INT | 21,480 | 0.1% | 97.9% |  |
| BUILD_LIST | 20,580 | 0.1% | 98.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 18,960 | 0.1% | 98.1% | 0.2% |
| COPY_FREE_VARS | 18,940 | 0.1% | 98.1% |  |
| EXIT_INIT_CHECK | 18,920 | 0.1% | 98.2% |  |
| EXTENDED_ARG | 18,340 | 0.1% | 98.3% |  |
| LOAD_FAST_CHECK | 16,820 | 0.1% | 98.4% |  |
| TO_BOOL_LIST | 16,140 | 0.1% | 98.5% |  |
| MAP_ADD | 16,040 | 0.1% | 98.5% |  |
| CALL_BUILTIN_CLASS | 15,640 | 0.1% | 98.6% |  |
| JUMP_BACKWARD | 14,280 | 0.1% | 98.7% |  |
| SWAP | 13,980 | 0.1% | 98.7% |  |
| BINARY_SUBSCR_DICT | 13,060 | 0.1% | 98.8% |  |
| YIELD_VALUE | 12,980 | 0.1% | 98.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 11,840 | 0.1% | 98.9% |  |
| CALL_BUILTIN_O | 11,740 | 0.1% | 99.0% | 1.7% |
| LOAD_ATTR_PROPERTY | 11,460 | 0.1% | 99.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 10,620 | 0.0% | 99.1% |  |
| FOR_ITER_RANGE | 10,480 | 0.0% | 99.1% |  |
| RESUME | 10,380 | 0.0% | 99.2% | 0.0% |
| LIST_APPEND | 10,180 | 0.0% | 99.2% |  |
| UNPACK_SEQUENCE_TUPLE | 10,040 | 0.0% | 99.3% |  |
| SEND | 9,400 | 0.0% | 99.3% |  |
| BEFORE_ASYNC_WITH | 9,120 | 0.0% | 99.4% |  |
| UNARY_NOT | 9,000 | 0.0% | 99.4% |  |
| MAKE_CELL | 8,340 | 0.0% | 99.4% |  |
| MAKE_FUNCTION | 6,920 | 0.0% | 99.5% |  |
| COMPARE_OP_FLOAT | 5,700 | 0.0% | 99.5% |  |
| LOAD_SUPER_ATTR_METHOD | 5,440 | 0.0% | 99.5% |  |
| CALL_INTRINSIC_1 | 5,400 | 0.0% | 99.5% |  |
| COMPARE_OP_STR | 5,320 | 0.0% | 99.6% | 4.1% |
| LIST_EXTEND | 5,320 | 0.0% | 99.6% |  |
| FOR_ITER_TUPLE | 5,260 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_LIST_INT | 4,300 | 0.0% | 99.6% |  |
| CALL_PY_WITH_DEFAULTS | 3,940 | 0.0% | 99.7% |  |
| BEFORE_WITH | 3,760 | 0.0% | 99.7% |  |
| BINARY_OP_ADD_FLOAT | 3,740 | 0.0% | 99.7% |  |
| STORE_SUBSCR | 3,720 | 0.0% | 99.7% |  |
| TO_BOOL_STR | 3,560 | 0.0% | 99.7% |  |
| SET_FUNCTION_ATTRIBUTE | 3,460 | 0.0% | 99.7% |  |
| STORE_FAST_LOAD_FAST | 3,300 | 0.0% | 99.8% |  |
| BINARY_OP_SUBTRACT_INT | 3,300 | 0.0% | 99.8% |  |
| STORE_NAME | 3,120 | 0.0% | 99.8% |  |
| CHECK_EXC_MATCH | 3,060 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 3,060 | 0.0% | 99.8% |  |
| POP_EXCEPT | 3,040 | 0.0% | 99.8% |  |
| STORE_ATTR_WITH_HINT | 2,620 | 0.0% | 99.8% | 11.5% |
| TO_BOOL_ALWAYS_TRUE | 2,460 | 0.0% | 99.9% | 6.5% |
| BINARY_SUBSCR | 2,440 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 2,360 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE | 2,100 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 1,960 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 1,700 | 0.0% | 99.9% |  |
| LOAD_NAME | 1,500 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_STR_INT | 1,400 | 0.0% | 99.9% | 11.4% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,340 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR_ATTR | 1,340 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_LIST | 1,140 | 0.0% | 99.9% |  |
| UNARY_INVERT | 1,120 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR | 1,060 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 1,020 | 0.0% | 100.0% |  |
| BUILD_STRING | 940 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 900 | 0.0% | 100.0% |  |
| RERAISE | 880 | 0.0% | 100.0% |  |
| DICT_UPDATE | 760 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 720 | 0.0% | 100.0% | 2.8% |
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
| LOAD_BUILD_CLASS | 280 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 752,016 | 3.5% | 3.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 561,540 | 2.6% | 6.1% |
| LOAD_FAST LOAD_ATTR | 516,800 | 2.4% | 8.5% |
| STORE_FAST LOAD_FAST | 498,240 | 2.3% | 10.8% |
| RESUME_CHECK LOAD_FAST | 467,060 | 2.2% | 13.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 461,940 | 2.1% | 15.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 401,168 | 1.9% | 17.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 353,240 | 1.6% | 18.6% |
| LOAD_FAST LOAD_ATTR_SLOT | 281,520 | 1.3% | 19.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 275,180 | 1.3% | 21.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 242,968 | 1.1% | 22.3% |
| LOAD_FAST LOAD_CONST | 238,980 | 1.1% | 23.4% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 226,920 | 1.1% | 24.5% |
| LOAD_CONST LOAD_FAST | 213,298 | 1.0% | 25.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR | 201,460 | 0.9% | 26.4% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 179,388 | 0.8% | 27.2% |
| RETURN_CONST POP_TOP | 179,360 | 0.8% | 28.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 179,260 | 0.8% | 28.9% |
| POP_TOP LOAD_FAST | 178,040 | 0.8% | 29.7% |
| LOAD_ATTR_MODULE PUSH_NULL | 173,920 | 0.8% | 30.5% |
| LOAD_ATTR LOAD_FAST | 173,320 | 0.8% | 31.3% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 170,380 | 0.8% | 32.1% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 166,440 | 0.8% | 32.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 165,580 | 0.8% | 33.7% |
| CACHE RESUME_CHECK | 164,600 | 0.8% | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 159,140 | 0.7% | 35.2% |
| POP_TOP RESUME_CHECK | 158,280 | 0.7% | 35.9% |
| GET_AWAITABLE LOAD_CONST | 151,360 | 0.7% | 36.6% |
| STORE_ATTR LOAD_FAST_LOAD_FAST | 148,860 | 0.7% | 37.3% |
| POP_JUMP_IF_FALSE LOAD_CONST | 148,380 | 0.7% | 38.0% |
| SEND_GEN POP_TOP | 147,080 | 0.7% | 38.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 146,800 | 0.7% | 39.4% |
| LOAD_CONST SEND_GEN | 146,220 | 0.7% | 40.0% |
| LOAD_ATTR TO_BOOL_BOOL | 145,740 | 0.7% | 40.7% |
| LOAD_FAST RETURN_VALUE | 139,880 | 0.6% | 41.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 139,100 | 0.6% | 42.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 138,980 | 0.6% | 42.7% |
| CALL STORE_FAST | 137,580 | 0.6% | 43.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 137,040 | 0.6% | 43.9% |
| RETURN_GENERATOR GET_AWAITABLE | 130,160 | 0.6% | 44.5% |
| IS_OP POP_JUMP_IF_FALSE | 129,180 | 0.6% | 45.1% |
| LOAD_CONST COMPARE_OP_INT | 125,920 | 0.6% | 45.7% |
| RETURN_VALUE STORE_FAST | 123,240 | 0.6% | 46.3% |
| LOAD_CONST BINARY_OP | 116,960 | 0.5% | 46.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 116,080 | 0.5% | 47.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 113,740 | 0.5% | 47.9% |
| POP_TOP RETURN_CONST | 109,560 | 0.5% | 48.4% |
| RETURN_CONST INTERPRETER_EXIT | 106,420 | 0.5% | 48.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 106,320 | 0.5% | 49.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 106,060 | 0.5% | 49.9% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 105,119 | 0.5% | 50.4% |
| PUSH_NULL LOAD_FAST | 103,860 | 0.5% | 50.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 103,140 | 0.5% | 51.3% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 102,668 | 0.5% | 51.8% |
| RETURN_VALUE RETURN_VALUE | 98,960 | 0.5% | 52.3% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 98,480 | 0.5% | 52.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 96,240 | 0.4% | 53.2% |
| POP_JUMP_IF_NONE LOAD_FAST | 93,160 | 0.4% | 53.6% |
| CALL_LEN LOAD_FAST | 92,388 | 0.4% | 54.0% |
| LOAD_CONST CALL_KW | 91,780 | 0.4% | 54.5% |
| PUSH_NULL LOAD_CONST | 90,980 | 0.4% | 54.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 87,320 | 0.4% | 55.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 81,641 | 0.4% | 55.7% |
| LOAD_FAST STORE_ATTR_SLOT | 80,960 | 0.4% | 56.0% |
| RETURN_VALUE END_SEND | 80,400 | 0.4% | 56.4% |
| LOAD_CONST STORE_FAST | 79,700 | 0.4% | 56.8% |
| RETURN_VALUE TO_BOOL_BOOL | 79,680 | 0.4% | 57.2% |
| END_SEND POP_TOP | 79,440 | 0.4% | 57.5% |
| RETURN_VALUE INTERPRETER_EXIT | 79,200 | 0.4% | 57.9% |
| NOP LOAD_FAST | 76,540 | 0.4% | 58.2% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 75,540 | 0.4% | 58.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 75,340 | 0.3% | 58.9% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 75,300 | 0.3% | 59.3% |
| LOAD_FAST CALL_LEN | 72,720 | 0.3% | 59.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 72,420 | 0.3% | 60.0% |
| LOAD_FAST CALL | 72,140 | 0.3% | 60.3% |
| END_SEND STORE_FAST | 69,920 | 0.3% | 60.6% |
| LOAD_CONST LOAD_CONST | 69,540 | 0.3% | 60.9% |
| RETURN_CONST END_SEND | 68,080 | 0.3% | 61.3% |
| LOAD_FAST COMPARE_OP_INT | 67,880 | 0.3% | 61.6% |
| BUILD_MAP LOAD_FAST | 67,620 | 0.3% | 61.9% |
| DICT_MERGE CALL_FUNCTION_EX | 67,580 | 0.3% | 62.2% |
| CALL_KW RESUME_CHECK | 67,340 | 0.3% | 62.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 67,200 | 0.3% | 62.8% |
| LOAD_GLOBAL_MODULE IS_OP | 66,680 | 0.3% | 63.1% |
| LOAD_FAST DICT_MERGE | 66,300 | 0.3% | 63.4% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_SLOT | 65,060 | 0.3% | 63.7% |
| LOAD_ATTR_SLOT LOAD_GLOBAL_MODULE | 65,000 | 0.3% | 64.0% |
| LOAD_GLOBAL_MODULE CALL_BUILTIN_FAST | 63,920 | 0.3% | 64.3% |
| LOAD_FAST PUSH_NULL | 63,260 | 0.3% | 64.6% |
| LOAD_FAST BUILD_TUPLE | 62,360 | 0.3% | 64.9% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 60,220 | 0.3% | 65.2% |
| CALL_LEN LOAD_CONST | 59,240 | 0.3% | 65.5% |
| LOAD_FAST CALL_TYPE_1 | 59,140 | 0.3% | 65.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 58,120 | 0.3% | 66.0% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 57,560 | 0.3% | 66.3% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 57,280 | 0.3% | 66.6% |
| LOAD_ATTR_WITH_HINT POP_JUMP_IF_NONE | 57,120 | 0.3% | 66.8% |
| JUMP_FORWARD LOAD_FAST | 56,301 | 0.3% | 67.1% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 55,540 | 0.3% | 67.3% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,859 | 46.8% |
| LOAD_CONST | 19,520 | 27.8% |
| BINARY_OP | 16,200 | 23.1% |
| BINARY_OP_ADD_INT | 1,640 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 32,319 | 46.0% |
| STORE_FAST | 18,360 | 26.1% |
| BINARY_OP | 16,240 | 23.1% |
| RETURN_VALUE | 1,360 | 1.9% |
| GET_ITER | 360 | 0.5% |


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
| RESUME_CHECK | 164,600 | 78.3% |
| RETURN_GENERATOR | 18,320 | 8.7% |
| COPY_FREE_VARS | 13,400 | 6.4% |
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
| LOAD_CONST | 1,440 | 59.0% |
| BINARY_SUBSCR | 280 | 11.5% |
| LOAD_FAST | 200 | 8.2% |
| LOAD_GLOBAL_MODULE | 200 | 8.2% |
| LOAD_FAST_LOAD_FAST | 80 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 18.2% |
| BINARY_SUBSCR | 280 | 11.6% |
| STORE_FAST | 280 | 11.6% |
| BINARY_SUBSCR_LIST_INT | 240 | 9.9% |
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
| RETURN_CONST | 18,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 18,920 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,440 | 84.7% |
| LOAD_ATTR | 100 | 5.9% |
| CONVERT_VALUE | 80 | 4.7% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 3.5% |
| LOAD_FAST_LOAD_FAST | 20 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,460 | 85.9% |
| BUILD_STRING | 240 | 14.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 32,600 | 46.0% |
| LOAD_FAST | 22,800 | 32.2% |
| CALL_BUILTIN_CLASS | 12,540 | 17.7% |
| LOAD_ATTR_INSTANCE_VALUE | 820 | 1.2% |
| CALL | 560 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 43,580 | 61.5% |
| FOR_ITER_LIST | 17,460 | 24.6% |
| FOR_ITER_RANGE | 4,100 | 5.8% |
| LOAD_FAST_AND_CLEAR | 2,200 | 3.1% |
| CALL_PY_EXACT_ARGS | 1,540 | 2.2% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 106,420 | 50.7% |
| RETURN_VALUE | 79,200 | 37.8% |
| RETURN_GENERATOR | 18,400 | 8.8% |
| YIELD_VALUE | 5,700 | 2.7% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 240 | 85.7% |
| POP_TOP | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 280 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 3,440 | 49.7% |
| LOAD_FAST | 1,680 | 24.3% |
| STORE_NAME | 1,120 | 16.2% |
| LOAD_CONST | 440 | 6.4% |
| STORE_DEREF | 160 | 2.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 28,680 | 28.7% |
| RESUME_CHECK | 28,640 | 28.7% |
| POP_JUMP_IF_FALSE | 14,680 | 14.7% |
| POP_JUMP_IF_TRUE | 9,520 | 9.5% |
| POP_JUMP_IF_NOT_NONE | 8,760 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 76,540 | 76.7% |
| LOAD_GLOBAL_MODULE | 15,400 | 15.4% |
| LOAD_GLOBAL_BUILTIN | 2,640 | 2.6% |
| LOAD_GLOBAL | 1,420 | 1.4% |
| NOP | 1,260 | 1.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,240 | 40.8% |
| SWAP | 560 | 18.4% |
| STORE_FAST | 420 | 13.8% |
| COPY | 400 | 13.2% |
| STORE_SUBSCR | 240 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 560 | 18.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 540 | 17.8% |
| EXTENDED_ARG | 520 | 17.1% |
| RERAISE | 400 | 13.2% |
| LOAD_FAST | 260 | 8.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 179,360 | 31.7% |
| SEND_GEN | 147,080 | 26.0% |
| END_SEND | 79,440 | 14.0% |
| CALL_METHOD_DESCRIPTOR_O | 75,300 | 13.3% |
| CALL_FUNCTION_EX | 24,800 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,040 | 31.5% |
| RESUME_CHECK | 158,280 | 28.0% |
| RETURN_CONST | 109,560 | 19.4% |
| LOAD_CONST | 42,720 | 7.6% |
| ENTER_EXECUTOR | 32,840 | 5.8% |


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
| LOAD_ATTR_MODULE | 173,920 | 60.0% |
| LOAD_FAST | 63,260 | 21.8% |
| LOAD_ATTR_SLOT | 31,980 | 11.0% |
| LOAD_ATTR | 18,400 | 6.3% |
| LOAD_NAME | 560 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 103,860 | 35.8% |
| LOAD_CONST | 90,980 | 31.4% |
| LOAD_FAST_LOAD_FAST | 60,220 | 20.8% |
| CALL | 31,400 | 10.8% |
| LOAD_DEREF | 800 | 0.3% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 57,560 | 36.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 32,320 | 20.2% |
| ENTER_EXECUTOR | 22,640 | 14.2% |
| CACHE | 18,320 | 11.5% |
| CALL_KW | 17,200 | 10.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 130,160 | 81.5% |
| INTERPRETER_EXIT | 18,400 | 11.5% |
| LIST_APPEND | 8,080 | 5.1% |
| CALL | 1,380 | 0.9% |
| CALL_BUILTIN_O | 600 | 0.4% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,880 | 26.9% |
| RETURN_VALUE | 98,960 | 19.0% |
| LOAD_ATTR_INSTANCE_VALUE | 58,120 | 11.2% |
| CALL | 37,740 | 7.3% |
| CALL_FUNCTION_EX | 34,460 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 123,240 | 23.7% |
| RETURN_VALUE | 98,960 | 19.0% |
| END_SEND | 80,400 | 15.5% |
| TO_BOOL_BOOL | 79,680 | 15.3% |
| INTERPRETER_EXIT | 79,200 | 15.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,580 | 42.5% |
| LOAD_CONST | 920 | 24.7% |
| STORE_SUBSCR | 420 | 11.3% |
| BINARY_OP | 240 | 6.5% |
| LOAD_FAST_LOAD_FAST | 200 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 780 | 21.0% |
| LOAD_FAST | 520 | 14.0% |
| STORE_SUBSCR | 420 | 11.3% |
| JUMP_BACKWARD | 380 | 10.2% |
| RETURN_CONST | 380 | 10.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,060 | 28.4% |
| LOAD_ATTR | 20,760 | 25.5% |
| LOAD_ATTR_INSTANCE_VALUE | 19,940 | 24.5% |
| LOAD_ATTR_SLOT | 8,320 | 10.2% |
| CALL | 1,960 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40,600 | 50.0% |
| POP_JUMP_IF_TRUE | 31,660 | 39.0% |
| TO_BOOL_BOOL | 5,520 | 6.8% |
| TO_BOOL | 1,560 | 1.9% |
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
| LOAD_CONST | 116,960 | 54.2% |
| BINARY_OP | 21,060 | 9.8% |
| LOAD_FAST_LOAD_FAST | 16,380 | 7.6% |
| BINARY_SLICE | 16,240 | 7.5% |
| LOAD_GLOBAL_MODULE | 12,780 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,020 | 24.6% |
| LOAD_FAST | 49,180 | 22.8% |
| TO_BOOL_INT | 43,420 | 20.1% |
| BINARY_OP | 21,060 | 9.8% |
| BINARY_SLICE | 16,200 | 7.5% |


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
| STORE_FAST | 5,060 | 24.6% |
| LOAD_ATTR_SLOT | 3,860 | 18.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,680 | 13.0% |
| SWAP | 2,200 | 10.7% |
| LOAD_FAST | 1,260 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,860 | 33.3% |
| STORE_FAST | 6,500 | 31.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,640 | 12.8% |
| SWAP | 2,200 | 10.7% |
| BUILD_TUPLE | 320 | 1.6% |


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
| LOAD_FAST | 67,620 | 94.6% |
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
| LOAD_CONST | 700 | 74.5% |
| FORMAT_SIMPLE | 240 | 25.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 440 | 46.8% |
| STORE_FAST | 240 | 25.5% |
| LIST_APPEND | 160 | 17.0% |
| CALL | 100 | 10.6% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,360 | 68.8% |
| LOAD_GLOBAL_BUILTIN | 16,500 | 18.2% |
| LOAD_FAST_LOAD_FAST | 4,280 | 4.7% |
| LOAD_GLOBAL_MODULE | 2,060 | 2.3% |
| BINARY_OP | 960 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 32,640 | 36.0% |
| CALL | 17,440 | 19.2% |
| CALL_ISINSTANCE | 16,440 | 18.1% |
| RETURN_VALUE | 11,600 | 12.8% |
| LOAD_CONST | 3,640 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,140 | 20.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,560 | 14.1% |
| LOAD_FAST_LOAD_FAST | 46,540 | 12.9% |
| BINARY_SLICE | 32,319 | 9.0% |
| PUSH_NULL | 31,400 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 137,580 | 38.3% |
| RETURN_VALUE | 37,740 | 10.5% |
| LOAD_CONST | 32,879 | 9.1% |
| LOAD_FAST | 29,220 | 8.1% |
| POP_TOP | 22,740 | 6.3% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 67,580 | 72.1% |
| ENTER_EXECUTOR | 19,400 | 20.7% |
| CALL_INTRINSIC_1 | 4,520 | 4.8% |
| LOAD_FAST | 1,760 | 1.9% |
| BUILD_MAP | 160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 34,460 | 36.8% |
| RESUME_CHECK | 32,480 | 34.6% |
| POP_TOP | 24,800 | 26.5% |
| RETURN_GENERATOR | 640 | 0.7% |
| STORE_FAST | 560 | 0.6% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 5,080 | 94.1% |
| RERAISE | 320 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 4,520 | 83.7% |
| BUILD_MAP | 400 | 7.4% |
| RERAISE | 320 | 5.9% |
| LOAD_CONST | 160 | 3.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 91,780 | 92.3% |
| ENTER_EXECUTOR | 7,620 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 67,340 | 67.8% |
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
| LOAD_FAST | 34,660 | 41.6% |
| LOAD_GLOBAL_MODULE | 26,160 | 31.4% |
| LOAD_ATTR_MODULE | 16,600 | 19.9% |
| BUILD_TUPLE | 2,340 | 2.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,040 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 47,440 | 56.9% |
| POP_JUMP_IF_TRUE | 35,500 | 42.6% |
| SWAP | 320 | 0.4% |
| STORE_FAST | 120 | 0.1% |
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
| CALL_BUILTIN_FAST | 10,440 | 43.4% |
| CALL_LEN | 3,740 | 15.6% |
| BINARY_OP | 3,000 | 12.5% |
| LOAD_FAST | 2,960 | 12.3% |
| SWAP | 1,280 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 11,320 | 47.1% |
| TO_BOOL_INT | 6,800 | 28.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,040 | 8.5% |
| TO_BOOL | 820 | 3.4% |
| COMPARE_OP_INT | 800 | 3.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,400 | 70.7% |
| CALL_PY_EXACT_ARGS | 3,840 | 20.3% |
| LOAD_ATTR_PROPERTY | 800 | 4.2% |
| CALL | 680 | 3.6% |
| CALL_ALLOC_AND_ENTER_INIT | 140 | 0.7% |

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
| LOAD_FAST | 66,300 | 98.1% |
| RETURN_VALUE | 800 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 340 | 0.5% |
| CALL | 80 | 0.1% |
| LOAD_ATTR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 67,580 | 100.0% |


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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 32,840 | 21.8% |
| STORE_SUBSCR_DICT | 32,160 | 21.4% |
| ENTER_EXECUTOR | 31,660 | 21.0% |
| CALL_LIST_APPEND | 16,180 | 10.7% |
| STORE_FAST | 15,660 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,660 | 27.0% |
| ENTER_EXECUTOR | 31,660 | 21.0% |
| RETURN_GENERATOR | 22,640 | 15.0% |
| CALL_FUNCTION_EX | 19,400 | 12.9% |
| FOR_ITER_LIST | 9,260 | 6.1% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 9,480 | 51.7% |
| LOAD_CONST | 5,420 | 29.6% |
| BUILD_MAP | 580 | 3.2% |
| POP_EXCEPT | 520 | 2.8% |
| JUMP_BACKWARD | 400 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,080 | 87.7% |
| JUMP_BACKWARD | 780 | 4.3% |
| FOR_ITER_LIST | 500 | 2.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 320 | 1.7% |
| FOR_ITER | 280 | 1.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 43,580 | 87.1% |
| JUMP_BACKWARD | 3,700 | 7.4% |
| FOR_ITER | 1,180 | 2.4% |
| LOAD_FAST | 920 | 1.8% |
| SWAP | 360 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 44,560 | 89.1% |
| FOR_ITER | 1,180 | 2.4% |
| RETURN_CONST | 1,120 | 2.2% |
| LOAD_FAST | 980 | 2.0% |
| FOR_ITER_LIST | 840 | 1.7% |


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
| LOAD_GLOBAL_MODULE | 66,680 | 50.7% |
| LOAD_FAST | 26,220 | 19.9% |
| LOAD_ATTR_MODULE | 15,960 | 12.1% |
| LOAD_ATTR | 12,120 | 9.2% |
| LOAD_FAST_LOAD_FAST | 8,080 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 129,180 | 98.2% |
| RETURN_VALUE | 1,600 | 1.2% |
| POP_JUMP_IF_TRUE | 660 | 0.5% |
| STORE_FAST | 80 | 0.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,940 | 34.6% |
| LIST_APPEND | 2,380 | 16.7% |
| CALL_LIST_APPEND | 1,220 | 8.5% |
| STORE_FAST | 1,140 | 8.0% |
| POP_JUMP_IF_FALSE | 1,040 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,140 | 29.0% |
| FOR_ITER | 3,700 | 25.9% |
| FOR_ITER_RANGE | 2,460 | 17.2% |
| LOAD_FAST | 1,120 | 7.8% |
| FOR_ITER_TUPLE | 1,060 | 7.4% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,560 | 80.6% |
| RESUME | 1,200 | 11.3% |
| POP_EXCEPT | 540 | 5.1% |
| EXTENDED_ARG | 320 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 6,420 | 60.5% |
| SEND | 3,340 | 31.5% |
| LOAD_FAST | 380 | 3.6% |
| NOP | 160 | 1.5% |
| LOAD_GLOBAL_MODULE | 120 | 1.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,640 | 45.5% |
| STORE_FAST | 34,660 | 32.4% |
| POP_TOP | 17,381 | 16.3% |
| POP_JUMP_IF_FALSE | 4,940 | 4.6% |
| LOAD_FAST | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 56,301 | 52.7% |
| STORE_FAST | 24,400 | 22.8% |
| LOAD_DEREF | 8,320 | 7.8% |
| BINARY_OP | 8,000 | 7.5% |
| LOAD_GLOBAL_BUILTIN | 6,360 | 5.9% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 8,080 | 79.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,120 | 11.0% |
| RETURN_VALUE | 560 | 5.5% |
| BUILD_STRING | 160 | 1.6% |
| BUILD_TUPLE | 80 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 7,800 | 76.6% |
| JUMP_BACKWARD | 2,380 | 23.4% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 3,860 | 72.6% |
| LOAD_FAST | 960 | 18.0% |
| BINARY_SLICE | 240 | 4.5% |
| LOAD_CONST | 240 | 4.5% |
| LOAD_ATTR | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 5,080 | 95.5% |
| LOAD_FAST | 160 | 3.0% |
| LOAD_NAME | 60 | 1.1% |
| STORE_NAME | 20 | 0.4% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 516,800 | 77.9% |
| LOAD_ATTR_WITH_HINT | 34,180 | 5.2% |
| LOAD_GLOBAL_BUILTIN | 32,880 | 5.0% |
| LOAD_GLOBAL_MODULE | 30,920 | 4.7% |
| LOAD_ATTR | 20,800 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 173,320 | 26.1% |
| TO_BOOL_BOOL | 145,740 | 22.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 47,180 | 7.1% |
| LOAD_GLOBAL_MODULE | 42,840 | 6.5% |
| CALL_PY_EXACT_ARGS | 35,060 | 5.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 238,980 | 21.0% |
| GET_AWAITABLE | 151,360 | 13.3% |
| POP_JUMP_IF_FALSE | 148,380 | 13.1% |
| PUSH_NULL | 90,980 | 8.0% |
| LOAD_CONST | 69,540 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,298 | 18.8% |
| SEND_GEN | 146,220 | 12.9% |
| COMPARE_OP_INT | 125,920 | 11.1% |
| BINARY_OP | 116,960 | 10.3% |
| CALL_KW | 91,780 | 8.1% |


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
| POP_JUMP_IF_FALSE | 561,540 | 14.1% |
| STORE_FAST | 498,240 | 12.5% |
| RESUME_CHECK | 467,060 | 11.7% |
| LOAD_GLOBAL_BUILTIN | 401,168 | 10.0% |
| LOAD_CONST | 213,298 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 752,016 | 18.8% |
| LOAD_ATTR | 516,800 | 12.9% |
| LOAD_ATTR_SLOT | 281,520 | 7.1% |
| LOAD_CONST | 238,980 | 6.0% |
| LOAD_ATTR_WITH_HINT | 226,920 | 5.7% |


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
| STORE_ATTR | 148,860 | 18.2% |
| STORE_ATTR_INSTANCE_VALUE | 103,140 | 12.6% |
| LOAD_FAST_LOAD_FAST | 87,320 | 10.7% |
| STORE_ATTR_SLOT | 72,420 | 8.9% |
| PUSH_NULL | 60,220 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR | 201,460 | 24.7% |
| STORE_ATTR_INSTANCE_VALUE | 106,060 | 13.0% |
| STORE_ATTR_SLOT | 98,480 | 12.1% |
| LOAD_FAST_LOAD_FAST | 87,320 | 10.7% |
| LOAD_FAST | 67,200 | 8.2% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,720 | 11.6% |
| LOAD_FAST | 3,520 | 11.0% |
| STORE_FAST | 3,360 | 10.5% |
| RESUME_CHECK | 2,380 | 7.4% |
| RESUME | 2,320 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,420 | 35.7% |
| LOAD_ATTR | 4,860 | 15.2% |
| LOAD_GLOBAL_BUILTIN | 4,740 | 14.8% |
| LOAD_FAST | 4,480 | 14.0% |
| CALL | 1,320 | 4.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 320 | 21.3% |
| STORE_NAME | 300 | 20.0% |
| RESUME | 280 | 18.7% |
| LOAD_CONST | 220 | 14.7% |
| BINARY_OP | 80 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 37.3% |
| LOAD_ATTR | 440 | 29.3% |
| STORE_NAME | 280 | 18.7% |
| CALL | 100 | 6.7% |
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
| MAKE_CELL | 5,480 | 65.7% |
| CALL_PY_EXACT_ARGS | 2,120 | 25.4% |
| CALL | 240 | 2.9% |
| CALL_FUNCTION_EX | 160 | 1.9% |
| CALL_KW | 160 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 5,480 | 65.7% |
| RESUME_CHECK | 1,720 | 20.6% |
| RETURN_GENERATOR | 960 | 11.5% |
| RESUME | 180 | 2.2% |


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
| TO_BOOL_BOOL | 461,940 | 40.6% |
| COMPARE_OP_INT | 242,968 | 21.3% |
| IS_OP | 129,180 | 11.3% |
| TO_BOOL_NONE | 75,540 | 6.6% |
| TO_BOOL_INT | 55,540 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 561,540 | 49.3% |
| LOAD_GLOBAL_BUILTIN | 179,388 | 15.8% |
| LOAD_CONST | 148,380 | 13.0% |
| RETURN_CONST | 113,740 | 10.0% |
| LOAD_GLOBAL_MODULE | 75,340 | 6.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 57,120 | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE | 53,800 | 32.4% |
| LOAD_FAST | 44,480 | 26.8% |
| LOAD_DEREF | 9,120 | 5.5% |
| LOAD_ATTR | 720 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 93,160 | 56.2% |
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
| LOAD_FAST | 116,080 | 89.9% |
| LOAD_ATTR_INSTANCE_VALUE | 10,080 | 7.8% |
| CALL_BUILTIN_FAST | 720 | 0.6% |
| LOAD_GLOBAL_MODULE | 620 | 0.5% |
| LOAD_FAST_CHECK | 480 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,240 | 41.2% |
| LOAD_FAST_LOAD_FAST | 30,160 | 23.3% |
| LOAD_GLOBAL_MODULE | 23,700 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 8,780 | 6.8% |
| NOP | 8,760 | 6.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 170,380 | 65.2% |
| CONTAINS_OP | 35,500 | 13.6% |
| TO_BOOL | 31,660 | 12.1% |
| TO_BOOL_NONE | 8,340 | 3.2% |
| TO_BOOL_INT | 6,040 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,580 | 63.4% |
| LOAD_GLOBAL_MODULE | 42,140 | 16.1% |
| RETURN_CONST | 26,220 | 10.0% |
| NOP | 9,520 | 3.6% |
| LOAD_CONST | 4,300 | 1.6% |


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
| POP_JUMP_IF_FALSE | 113,740 | 29.6% |
| POP_TOP | 109,560 | 28.5% |
| STORE_ATTR | 50,240 | 13.1% |
| STORE_ATTR_SLOT | 27,960 | 7.3% |
| STORE_FAST | 27,200 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 179,360 | 46.7% |
| INTERPRETER_EXIT | 106,420 | 27.7% |
| END_SEND | 68,080 | 17.7% |
| EXIT_INIT_CHECK | 18,920 | 4.9% |
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
| MAKE_FUNCTION | 3,440 | 99.4% |
| SET_FUNCTION_ATTRIBUTE | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,220 | 64.2% |
| STORE_DEREF | 640 | 18.5% |
| LOAD_FAST | 200 | 5.8% |
| STORE_NAME | 200 | 5.8% |
| LOAD_GLOBAL_MODULE | 160 | 4.6% |


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
| CALL | 137,580 | 18.7% |
| RETURN_VALUE | 123,240 | 16.7% |
| LOAD_CONST | 79,700 | 10.8% |
| END_SEND | 69,920 | 9.5% |
| BINARY_OP | 53,020 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 498,240 | 67.6% |
| LOAD_GLOBAL_BUILTIN | 44,000 | 6.0% |
| LOAD_GLOBAL_MODULE | 40,480 | 5.5% |
| JUMP_FORWARD | 34,660 | 4.7% |
| NOP | 28,680 | 3.9% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 1,340 | 40.6% |
| FOR_ITER_TUPLE | 1,120 | 33.9% |
| FOR_ITER_LIST | 260 | 7.9% |
| FOR_ITER | 220 | 6.7% |
| COPY | 160 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,560 | 47.3% |
| TO_BOOL_STR | 1,120 | 33.9% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 5.5% |
| LOAD_ATTR_PROPERTY | 120 | 3.6% |
| STORE_ATTR | 80 | 2.4% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 23,260 | 82.8% |
| UNPACK_SEQUENCE_TUPLE | 1,380 | 4.9% |
| UNPACK_SEQUENCE_LIST | 1,140 | 4.1% |
| UNPACK_SEQUENCE | 900 | 3.2% |
| STORE_FAST_STORE_FAST | 400 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,760 | 81.0% |
| LOAD_GLOBAL_MODULE | 2,000 | 7.1% |
| STORE_FAST | 1,800 | 6.4% |
| LOAD_GLOBAL | 400 | 1.4% |
| STORE_FAST_STORE_FAST | 400 | 1.4% |


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
| MAKE_FUNCTION | 1,120 | 35.9% |
| LOAD_CONST | 540 | 17.3% |
| CALL | 500 | 16.0% |
| LOAD_NAME | 280 | 9.0% |
| IMPORT_NAME | 220 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,680 | 53.8% |
| EXTENDED_ARG | 360 | 11.5% |
| LOAD_NAME | 300 | 9.6% |
| RETURN_CONST | 300 | 9.6% |
| LOAD_BUILD_CLASS | 240 | 7.7% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,200 | 15.7% |
| LOAD_FAST_AND_CLEAR | 2,200 | 15.7% |
| LOAD_FAST | 2,000 | 14.3% |
| LOAD_ATTR | 1,500 | 10.7% |
| BINARY_OP_ADD_INT | 1,340 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,440 | 24.6% |
| BUILD_LIST | 2,200 | 15.7% |
| STORE_ATTR_INSTANCE_VALUE | 2,040 | 14.6% |
| LOAD_CONST | 1,320 | 9.4% |
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
| ENTER_EXECUTOR | 760 | 5.9% |
| RETURN_CONST | 560 | 4.3% |
| BUILD_STRING | 440 | 3.4% |

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
| CALL | 4,240 | 40.8% |
| CACHE | 2,380 | 22.9% |
| POP_TOP | 1,520 | 14.6% |
| SEND_GEN | 920 | 8.9% |
| COPY_FREE_VARS | 700 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,680 | 45.1% |
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
| LOAD_CONST | 18,320 | 85.3% |
| LOAD_FAST_LOAD_FAST | 2,760 | 12.8% |
| BINARY_OP | 280 | 1.3% |
| LOAD_FAST | 120 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 16,120 | 75.0% |
| BINARY_SLICE | 1,640 | 7.6% |
| BUILD_SLICE | 1,340 | 6.2% |
| SWAP | 1,340 | 6.2% |
| CALL_PY_EXACT_ARGS | 320 | 1.5% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,200 | 61.2% |
| LOAD_FAST | 240 | 12.2% |
| BINARY_SUBSCR_LIST_INT | 160 | 8.2% |
| LOAD_CONST | 120 | 6.1% |
| LOAD_GLOBAL_MODULE | 120 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,100 | 56.1% |
| RETURN_VALUE | 300 | 15.3% |
| CALL | 240 | 12.2% |
| STORE_FAST | 160 | 8.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 6.1% |


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
| LOAD_FAST_LOAD_FAST | 1,480 | 44.8% |
| LOAD_CONST | 1,380 | 41.8% |
| BINARY_OP | 200 | 6.1% |
| LOAD_FAST | 200 | 6.1% |
| CALL_LEN | 40 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,560 | 47.3% |
| SWAP | 880 | 26.7% |
| STORE_DEREF | 460 | 13.9% |
| STORE_FAST | 220 | 6.7% |
| RETURN_VALUE | 40 | 1.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,700 | 89.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 520 | 4.0% |
| LOAD_DEREF | 420 | 3.2% |
| LOAD_CONST | 160 | 1.2% |
| BINARY_SUBSCR | 80 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,500 | 80.5% |
| PUSH_EXC_INFO | 980 | 7.5% |
| STORE_FAST | 900 | 6.9% |
| PUSH_NULL | 420 | 3.2% |
| LOAD_FAST | 160 | 1.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 360 | 50.0% |
| BUILD_TUPLE | 120 | 16.7% |
| LOAD_CONST | 120 | 16.7% |
| BINARY_SUBSCR | 100 | 13.9% |
| LOAD_FAST | 20 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 700 | 97.2% |
| PUSH_EXC_INFO | 20 | 2.8% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,000 | 93.0% |
| BINARY_SUBSCR | 240 | 5.6% |
| BINARY_OP_SUBTRACT_INT | 40 | 0.9% |
| LOAD_FAST | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 59.1% |
| LOAD_ATTR_SLOT | 960 | 22.3% |
| RETURN_VALUE | 260 | 6.0% |
| BINARY_OP_ADD_UNICODE | 160 | 3.7% |
| LOAD_FAST | 120 | 2.8% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,000 | 71.4% |
| LOAD_CONST | 200 | 14.3% |
| ENTER_EXECUTOR | 80 | 5.7% |
| LOAD_FAST | 60 | 4.3% |
| BINARY_SUBSCR | 40 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,020 | 72.9% |
| LOAD_CONST | 240 | 17.1% |
| STORE_FAST | 100 | 7.1% |
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
| LOAD_FAST_LOAD_FAST | 8,920 | 47.0% |
| LOAD_ATTR | 8,120 | 42.8% |
| BINARY_OP | 760 | 4.0% |
| CALL | 460 | 2.4% |
| LOAD_FAST | 340 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,780 | 99.1% |
| COPY_FREE_VARS | 140 | 0.7% |
| STORE_FAST | 40 | 0.2% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,520 | 64.5% |
| LOAD_FAST | 9,160 | 17.6% |
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
| LOAD_FAST | 12,960 | 82.9% |
| LOAD_GLOBAL_BUILTIN | 1,020 | 6.5% |
| CALL | 580 | 3.7% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 1.8% |
| LOAD_CONST | 160 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 12,540 | 80.2% |
| STORE_FAST | 1,140 | 7.3% |
| LOAD_GLOBAL_BUILTIN | 480 | 3.1% |
| STORE_FAST_STORE_FAST | 380 | 2.4% |
| LOAD_FAST | 360 | 2.3% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 63,920 | 46.1% |
| LOAD_ATTR_SLOT | 32,580 | 23.5% |
| LOAD_FAST | 25,660 | 18.5% |
| LOAD_CONST | 13,560 | 9.8% |
| LOAD_FAST_LOAD_FAST | 1,880 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,800 | 24.4% |
| LOAD_FAST_LOAD_FAST | 32,480 | 23.4% |
| LOAD_ATTR_METHOD_NO_DICT | 31,960 | 23.0% |
| COPY | 10,440 | 7.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 8,120 | 5.9% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 32,240 | 89.9% |
| LOAD_FAST | 920 | 2.6% |
| PUSH_NULL | 760 | 2.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 620 | 1.7% |
| CALL | 260 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 34,140 | 95.2% |
| RETURN_VALUE | 840 | 2.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 620 | 1.7% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.3% |
| BEFORE_WITH | 80 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,260 | 78.9% |
| LOAD_ATTR_INSTANCE_VALUE | 680 | 5.8% |
| RETURN_GENERATOR | 600 | 5.1% |
| CALL | 460 | 3.9% |
| LOAD_CONST | 240 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,300 | 70.7% |
| TO_BOOL_BOOL | 1,000 | 8.5% |
| STORE_FAST | 700 | 6.0% |
| POP_TOP | 500 | 4.3% |
| LOAD_CONST | 360 | 3.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 16,440 | 37.0% |
| LOAD_GLOBAL_BUILTIN | 13,840 | 31.2% |
| LOAD_GLOBAL_MODULE | 12,320 | 27.7% |
| LOAD_ATTR | 880 | 2.0% |
| CALL | 720 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 43,280 | 97.5% |
| TO_BOOL | 680 | 1.5% |
| RETURN_VALUE | 340 | 0.8% |
| STORE_FAST | 80 | 0.2% |
| LOAD_FAST | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 102,668 | 53.3% |
| LOAD_FAST | 72,720 | 37.7% |
| LOAD_ATTR_WITH_HINT | 16,400 | 8.5% |
| CALL | 740 | 0.4% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,388 | 47.9% |
| LOAD_CONST | 59,240 | 30.7% |
| LOAD_GLOBAL_MODULE | 17,480 | 9.1% |
| STORE_FAST | 16,520 | 8.6% |
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
| ENTER_EXECUTOR | 16,180 | 68.9% |
| LOAD_FAST | 2,600 | 11.1% |
| RETURN_CONST | 2,200 | 9.4% |
| JUMP_BACKWARD | 1,220 | 5.2% |
| LOAD_GLOBAL_MODULE | 640 | 2.7% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,640 | 22.3% |
| LOAD_ATTR_METHOD_NO_DICT | 2,360 | 19.9% |
| LOAD_GLOBAL_MODULE | 1,600 | 13.5% |
| LOAD_CONST | 1,540 | 13.0% |
| LOAD_FAST_LOAD_FAST | 1,240 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,620 | 30.6% |
| RETURN_VALUE | 3,300 | 27.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,040 | 17.2% |
| LIST_APPEND | 1,120 | 9.5% |
| BUILD_TUPLE | 840 | 7.1% |


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
| LOAD_ATTR_METHOD_NO_DICT | 50,081 | 43.4% |
| LOAD_ATTR | 47,180 | 40.9% |
| LOAD_ATTR_METHOD_LAZY_DICT | 8,120 | 7.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,040 | 7.0% |
| CALL | 1,480 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 46,120 | 39.9% |
| GET_ITER | 32,600 | 28.2% |
| STORE_FAST | 20,160 | 17.5% |
| RETURN_VALUE | 8,520 | 7.4% |
| BUILD_LIST | 2,680 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,280 | 72.5% |
| CALL | 9,760 | 12.4% |
| CALL_BUILTIN_FAST | 8,080 | 10.2% |
| LOAD_CONST | 1,980 | 2.5% |
| STORE_FAST | 1,120 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 75,300 | 95.4% |
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
| LOAD_ATTR_METHOD_WITH_VALUES | 166,440 | 39.9% |
| LOAD_FAST | 138,980 | 33.3% |
| LOAD_ATTR | 35,060 | 8.4% |
| LOAD_FAST_LOAD_FAST | 22,760 | 5.5% |
| LOAD_FAST_CHECK | 16,080 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 353,240 | 84.7% |
| RETURN_GENERATOR | 57,560 | 13.8% |
| COPY_FREE_VARS | 3,840 | 0.9% |
| MAKE_CELL | 2,120 | 0.5% |
| TO_BOOL_BOOL | 160 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,700 | 43.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 560 | 14.2% |
| CALL | 500 | 12.7% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 11.2% |
| RETURN_VALUE | 200 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,480 | 88.3% |
| RETURN_GENERATOR | 460 | 11.7% |


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
| RETURN_GENERATOR | 420 | 46.7% |
| LOAD_FAST | 220 | 24.4% |
| LOAD_GLOBAL_MODULE | 160 | 17.8% |
| CALL | 80 | 8.9% |
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
| LOAD_FAST | 59,140 | 99.7% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |
| CALL | 60 | 0.1% |
| LOAD_CONST | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 41,040 | 69.2% |
| LOAD_FAST | 17,960 | 30.3% |
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
| LOAD_CONST | 125,920 | 51.3% |
| LOAD_FAST | 67,880 | 27.6% |
| LOAD_ATTR_INSTANCE_VALUE | 20,468 | 8.3% |
| LOAD_ATTR_WITH_HINT | 8,160 | 3.3% |
| LOAD_FAST_LOAD_FAST | 8,140 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 242,968 | 98.9% |
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
| LOAD_CONST | 3,300 | 62.0% |
| LOAD_GLOBAL_MODULE | 760 | 14.3% |
| COMPARE_OP | 620 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 8.3% |
| LOAD_FAST | 160 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,580 | 86.1% |
| POP_JUMP_IF_TRUE | 420 | 7.9% |
| STORE_FAST | 120 | 2.3% |
| YIELD_VALUE | 120 | 2.3% |
| COPY | 60 | 1.1% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 17,460 | 52.1% |
| ENTER_EXECUTOR | 9,260 | 27.6% |
| JUMP_BACKWARD | 4,140 | 12.3% |
| FOR_ITER | 840 | 2.5% |
| LOAD_FAST | 720 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,960 | 32.7% |
| LOAD_GLOBAL_MODULE | 8,160 | 24.3% |
| RETURN_CONST | 4,980 | 14.8% |
| LOAD_FAST | 4,520 | 13.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 3,140 | 9.4% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 4,100 | 39.1% |
| ENTER_EXECUTOR | 3,700 | 35.3% |
| JUMP_BACKWARD | 2,460 | 23.5% |
| FOR_ITER | 120 | 1.1% |
| SWAP | 100 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,120 | 48.9% |
| LOAD_CONST | 3,760 | 35.9% |
| STORE_FAST_LOAD_FAST | 1,340 | 12.8% |
| SWAP | 120 | 1.1% |
| LOAD_GLOBAL_MODULE | 80 | 0.8% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,380 | 26.2% |
| GET_ITER | 1,160 | 22.1% |
| SWAP | 1,120 | 21.3% |
| JUMP_BACKWARD | 1,060 | 20.2% |
| LOAD_FAST | 400 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,400 | 26.6% |
| STORE_FAST_LOAD_FAST | 1,120 | 21.3% |
| SWAP | 1,120 | 21.3% |
| LOAD_FAST | 680 | 12.9% |
| RETURN_CONST | 440 | 8.4% |


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
| LOAD_FAST | 752,016 | 96.8% |
| LOAD_FAST_LOAD_FAST | 12,540 | 1.6% |
| LOAD_ATTR | 7,800 | 1.0% |
| COPY | 2,040 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,340 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 159,140 | 20.5% |
| CALL_LEN | 102,668 | 13.2% |
| LOAD_ATTR_METHOD_NO_DICT | 81,641 | 10.5% |
| RETURN_VALUE | 58,120 | 7.5% |
| LOAD_GLOBAL_MODULE | 54,080 | 7.0% |


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
| LOAD_ATTR_INSTANCE_VALUE | 81,641 | 34.6% |
| LOAD_FAST | 54,280 | 23.0% |
| CALL_BUILTIN_FAST | 31,960 | 13.5% |
| BINARY_OP | 16,120 | 6.8% |
| LOAD_ATTR_WITH_HINT | 16,040 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,240 | 40.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 50,081 | 21.2% |
| LOAD_GLOBAL_MODULE | 27,020 | 11.4% |
| LOAD_FAST_LOAD_FAST | 19,820 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 16,280 | 6.9% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 179,260 | 67.2% |
| LOAD_ATTR_SLOT | 27,240 | 10.2% |
| LOAD_ATTR_WITH_HINT | 18,440 | 6.9% |
| RETURN_VALUE | 9,520 | 3.6% |
| LOAD_DEREF | 8,640 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 166,440 | 62.4% |
| LOAD_FAST | 53,740 | 20.2% |
| LOAD_FAST_LOAD_FAST | 32,760 | 12.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,040 | 3.0% |
| CALL | 2,660 | 1.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 275,180 | 98.4% |
| LOAD_ATTR | 4,220 | 1.5% |
| LOAD_FAST | 280 | 0.1% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 173,920 | 62.2% |
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
| LOAD_FAST | 281,520 | 78.5% |
| LOAD_FAST_LOAD_FAST | 65,060 | 18.1% |
| LOAD_ATTR_INSTANCE_VALUE | 7,960 | 2.2% |
| LOAD_ATTR_MODULE | 1,560 | 0.4% |
| LOAD_ATTR | 1,300 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 65,000 | 18.1% |
| TO_BOOL_NONE | 46,640 | 13.0% |
| TO_BOOL_BOOL | 42,260 | 11.8% |
| LOAD_FAST | 39,400 | 11.0% |
| CALL_BUILTIN_FAST | 32,580 | 9.1% |


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
| POP_JUMP_IF_FALSE | 179,388 | 29.1% |
| RESUME_CHECK | 146,800 | 23.8% |
| LOAD_GLOBAL_BUILTIN | 105,119 | 17.1% |
| LOAD_FAST | 48,520 | 7.9% |
| STORE_FAST | 44,000 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 401,168 | 65.1% |
| LOAD_GLOBAL_BUILTIN | 105,119 | 17.1% |
| LOAD_ATTR | 32,880 | 5.3% |
| LOAD_FAST_LOAD_FAST | 32,800 | 5.3% |
| BUILD_TUPLE | 16,500 | 2.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 139,100 | 18.5% |
| LOAD_FAST | 106,320 | 14.2% |
| POP_JUMP_IF_FALSE | 75,340 | 10.0% |
| LOAD_ATTR_SLOT | 65,000 | 8.7% |
| LOAD_ATTR_INSTANCE_VALUE | 54,080 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 275,180 | 36.7% |
| LOAD_FAST | 137,040 | 18.3% |
| IS_OP | 66,680 | 8.9% |
| CALL_BUILTIN_FAST | 63,920 | 8.5% |
| COMPARE_OP | 40,680 | 5.4% |


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
| CALL_PY_EXACT_ARGS | 353,240 | 40.9% |
| CACHE | 164,600 | 19.1% |
| POP_TOP | 158,280 | 18.3% |
| CALL_KW | 67,340 | 7.8% |
| CALL_FUNCTION_EX | 32,480 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 467,060 | 54.1% |
| LOAD_GLOBAL_BUILTIN | 146,800 | 17.0% |
| LOAD_GLOBAL_MODULE | 139,100 | 16.1% |
| LOAD_FAST_LOAD_FAST | 51,140 | 5.9% |
| NOP | 28,640 | 3.3% |


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
| LOAD_FAST_LOAD_FAST | 106,060 | 71.0% |
| LOAD_FAST | 35,920 | 24.0% |
| STORE_ATTR | 5,380 | 3.6% |
| SWAP | 2,040 | 1.4% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 103,140 | 69.0% |
| LOAD_FAST | 17,340 | 11.6% |
| RETURN_CONST | 16,080 | 10.8% |
| LOAD_CONST | 6,780 | 4.5% |
| LOAD_GLOBAL_MODULE | 2,380 | 1.6% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 98,480 | 54.6% |
| LOAD_FAST | 80,960 | 44.9% |
| STORE_ATTR | 700 | 0.4% |
| STORE_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,420 | 40.2% |
| LOAD_CONST | 50,840 | 28.2% |
| LOAD_FAST | 28,700 | 15.9% |
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
| ENTER_EXECUTOR | 300 | 11.5% |
| LOAD_GLOBAL_BUILTIN | 200 | 7.6% |
| LOAD_GLOBAL | 40 | 1.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 32,460 | 76.0% |
| LOAD_FAST | 8,720 | 20.4% |
| LOAD_ATTR | 520 | 1.2% |
| STORE_SUBSCR | 280 | 0.7% |
| LOAD_CONST | 280 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 32,160 | 75.3% |
| LOAD_FAST | 8,940 | 20.9% |
| JUMP_BACKWARD | 460 | 1.1% |
| NOP | 280 | 0.7% |
| LOAD_GLOBAL_MODULE | 280 | 0.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 20 | 50.0% |
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
| LOAD_ATTR_INSTANCE_VALUE | 159,140 | 24.8% |
| LOAD_ATTR | 145,740 | 22.7% |
| RETURN_VALUE | 79,680 | 12.4% |
| LOAD_FAST | 51,960 | 8.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 46,120 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 461,940 | 72.0% |
| POP_JUMP_IF_TRUE | 170,380 | 26.6% |
| UNARY_NOT | 8,800 | 1.4% |
| EXTENDED_ARG | 100 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 43,420 | 70.4% |
| LOAD_ATTR_INSTANCE_VALUE | 8,920 | 14.5% |
| COPY | 6,800 | 11.0% |
| LOAD_FAST | 1,580 | 2.6% |
| TO_BOOL | 660 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 55,540 | 90.1% |
| POP_JUMP_IF_TRUE | 6,040 | 9.8% |
| UNARY_NOT | 80 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 14,680 | 91.0% |
| LOAD_FAST | 1,100 | 6.8% |
| TO_BOOL | 360 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 15,400 | 95.4% |
| POP_JUMP_IF_TRUE | 720 | 4.5% |
| UNARY_NOT | 20 | 0.1% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 46,640 | 55.6% |
| LOAD_FAST | 19,440 | 23.2% |
| LOAD_ATTR | 8,920 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 8,240 | 9.8% |
| TO_BOOL | 480 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 75,540 | 90.1% |
| POP_JUMP_IF_TRUE | 8,340 | 9.9% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,760 | 49.4% |
| STORE_FAST_LOAD_FAST | 1,120 | 31.5% |
| COPY | 360 | 10.1% |
| TO_BOOL | 240 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,260 | 63.5% |
| POP_JUMP_IF_FALSE | 1,300 | 36.5% |


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
| RETURN_VALUE | 9,640 | 40.9% |
| CALL_BUILTIN_FAST | 8,120 | 34.5% |
| FOR_ITER_LIST | 3,140 | 13.3% |
| STORE_FAST | 1,360 | 5.8% |
| UNPACK_SEQUENCE | 620 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 23,260 | 98.7% |
| STORE_FAST_LOAD_FAST | 140 | 0.6% |
| STORE_FAST | 100 | 0.4% |
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
|     deferred | 210,240 | 81.0% |
|          hit | 43,940 | 16.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 13.9% |
| Failure | 4,700 | 86.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 1,860 | 39.6% |
| or | 1,060 | 22.6% |
| add other | 600 | 12.8% |
| floor divide | 280 | 6.0% |
| remainder | 280 | 6.0% |
| multiply different types | 220 | 4.7% |
| add different types | 160 | 3.4% |
| xor | 160 | 3.4% |
| lshift | 80 | 1.7% |


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
|     deferred | 1,840 | 5.2% |
|          hit | 33,020 | 92.6% |
|         miss | 180 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 540 | 69.2% |
| Failure | 240 | 30.8% |

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
|     deferred | 385,079 | 20.7% |
|          hit | 1,444,109 | 77.7% |
|         miss | 54,820 | 2.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,920 | 61.3% |
| Failure | 11,320 | 38.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 2,340 | 20.7% |
| code complex parameters | 1,860 | 16.4% |
| class no vectorcall | 1,460 | 12.9% |
| cfunc noargs | 1,180 | 10.4% |
| meth descr varargs | 980 | 8.7% |
| class mutable | 600 | 5.3% |
| metaclass | 560 | 4.9% |
| no dict | 500 | 4.4% |
| cfunc varargs keywords | 380 | 3.4% |
| cfunc varargs | 360 | 3.2% |
| other | 320 | 2.8% |
| meth descr varargs keywords | 320 | 2.8% |
| operator wrapper | 220 | 1.9% |
| wrong number arguments | 120 | 1.1% |
| cmethod | 80 | 0.7% |
| init not simple | 40 | 0.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 55,960 | 17.4% |
|          hit | 261,548 | 81.4% |
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
|     deferred | 47,740 | 48.1% |
|          hit | 49,280 | 49.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,100 | 48.2% |
| Failure | 1,180 | 51.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 480 | 40.7% |
| dict values | 220 | 18.6% |
| dict items | 140 | 11.9% |
| reversed list | 140 | 11.9% |
| bytes | 60 | 5.1% |
| itertools | 40 | 3.4% |
| enumerate | 40 | 3.4% |
| ascii string | 40 | 3.4% |
| other | 20 | 1.7% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 634,580 | 16.3% |
|        deopt | 80 | 0.0% |
|          hit | 3,220,937 | 82.6% |
|         miss | 14,280 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 25,940 | 60.2% |
| Failure | 17,160 | 39.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 5,780 | 33.7% |
| not managed dict | 3,120 | 18.2% |
| shadowed | 3,080 | 17.9% |
| method | 1,720 | 10.0% |
| metaclass attribute | 1,680 | 9.8% |
| module attr not found | 400 | 2.3% |
| builtin class method | 400 | 2.3% |
| class attr descriptor | 320 | 1.9% |
| non object slot | 280 | 1.6% |
| class method obj | 220 | 1.3% |
| mutable class | 80 | 0.5% |
| class attr simple | 80 | 0.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 19,160 | 1.4% |
|        deopt | 160 | 0.0% |
|          hit | 1,363,167 | 97.5% |
|         miss | 3,400 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,200 | 100.0% |
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
|     deferred | 226,000 | 40.5% |
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
|     deferred | 3,020 | 1.7% |
|          hit | 170,240 | 97.9% |

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
|     deferred | 72,640 | 6.6% |
|          hit | 1,022,460 | 92.6% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,360 | 82.5% |
| Failure | 1,560 | 17.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 460 | 29.5% |
| sequence | 380 | 24.4% |
| set | 240 | 15.4% |
| dict | 160 | 10.3% |
| memory view | 140 | 9.0% |
| mapping | 80 | 5.1% |
| tuple | 80 | 5.1% |
| float | 20 | 1.3% |


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
| Basic | 10,671,792 | 49.5% |
| Not specialized | 3,470,426 | 16.1% |
| Specialized hits | 7,326,419 | 34.0% |
| Specialized misses | 83,302 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 634,580 | 38.1% |
| CALL | 385,079 | 23.1% |
| STORE_ATTR | 226,000 | 13.6% |
| BINARY_OP | 210,240 | 12.6% |
| TO_BOOL | 72,640 | 4.4% |
| COMPARE_OP | 55,960 | 3.4% |
| FOR_ITER | 47,740 | 2.9% |
| LOAD_GLOBAL | 19,160 | 1.2% |
| SEND | 6,920 | 0.4% |
| STORE_SUBSCR | 3,020 | 0.2% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,280 | 40.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,940 | 11.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 9,920 | 11.9% |
| STORE_ATTR_SLOT | 8,420 | 10.1% |
| LOAD_ATTR_WITH_HINT | 7,280 | 8.7% |
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
| Calls to PyEval_EvalDefault | 210,280 | 19.8% |
| Calls to Python functions inlined | 849,100 | 80.2% |
| Calls via PyEval_EvalFrame (total) | 210,280 | 19.8% |
| Calls via PyEval_EvalFrame (vector) | 193,420 | 18.3% |
| Calls via PyEval_EvalFrame (generator) | 16,860 | 1.6% |
| Calls via PyEval_EvalFrame (legacy) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 193,060 | 18.2% |
| Calls via PyEval_EvalFrame (build class) | 280 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 5,580 | 0.5% |
| Calls via PyEval_EvalFrame (function ex) | 33,440 | 3.2% |
| Calls via PyEval_EvalFrame (api) | 10,000 | 0.9% |
| Calls via PyEval_EvalFrame (method) | 42,400 | 4.0% |
| Frame objects created | 3,900 | 0.4% |
| Frames pushed | 905,680 | 85.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 776,219 | 32.7% |
| Frees to freelist | 780,319 |  |
| Allocations | 1,598,645 | 67.3% |
| Allocations to 512 bytes | 1,408,336 | 59.3% |
| Allocations to 4 kbytes | 132,514 | 5.6% |
| Allocations over 4 kbytes | 57,795 | 2.4% |
| Frees | 1,537,061 |  |
| New values | 34,900 |  |
| Interpreter increfs | 9,824,017 | 61.1% |
| Interpreter decrefs | 11,557,640 | 63.9% |
| Increfs | 6,266,828 | 38.9% |
| Decrefs | 6,536,239 | 36.1% |
| Materialize dict (on request) | 20 | 0.1% |
| Materialize dict (new key) | 160 | 0.5% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 1,223,603 |  |
| Method cache misses | 36,297 |  |
| Method cache collisions | 41,221 |  |
| Method cache dunder hits | 356,746 |  |
| Method cache dunder misses | 7,454 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 80 | 0 | 606,028 |
| 1 | 20 | 600 | 1,283,120 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 480 |  |
| Traces created | 480 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 20 | 4.2% |
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
| <= 8 | 0 | 0.0% |
| <= 16 | 40 | 8.3% |
| <= 32 | 240 | 50.0% |
| <= 64 | 40 | 8.3% |
| <= 128 | 160 | 33.3% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 0 | 0.0% |
| <= 16 | 80 | 16.7% |
| <= 32 | 220 | 45.8% |
| <= 64 | 140 | 29.2% |
| <= 128 | 40 | 8.3% |


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
| RETURN_GENERATOR | 140 |
| CALL | 60 |
| CALL_KW | 60 |
| YIELD_VALUE | 40 |
| CALL_FUNCTION_EX | 20 |
| CALL_LIST_APPEND | 20 |


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
| watched dict modification | 60 |
| watched globals modification | 60 |


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
