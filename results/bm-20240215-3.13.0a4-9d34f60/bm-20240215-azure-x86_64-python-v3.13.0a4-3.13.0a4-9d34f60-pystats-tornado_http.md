
# Pystats results

- benchmark: tornado_http
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 79,277,688 | 20.7% | 20.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 26,770,065 | 7.0% | 27.7% | 0.1% |
| RESUME_CHECK | 20,143,085 | 5.3% | 33.0% | 0.0% |
| LOAD_CONST | 17,002,404 | 4.4% | 37.4% |  |
| POP_JUMP_IF_FALSE | 15,335,245 | 4.0% | 41.4% |  |
| STORE_FAST | 12,501,135 | 3.3% | 44.7% |  |
| RETURN_VALUE | 11,663,273 | 3.0% | 47.7% |  |
| CALL_PY_EXACT_ARGS | 11,538,800 | 3.0% | 50.7% | 0.6% |
| LOAD_GLOBAL_MODULE | 10,994,771 | 2.9% | 53.6% | 0.0% |
| LOAD_FAST_LOAD_FAST | 10,359,660 | 2.7% | 56.3% |  |
| POP_TOP | 10,278,462 | 2.7% | 59.0% |  |
| TO_BOOL_BOOL | 9,836,539 | 2.6% | 61.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,068,180 | 2.4% | 63.9% | 0.9% |
| STORE_ATTR_INSTANCE_VALUE | 8,212,246 | 2.1% | 66.1% | 0.1% |
| RETURN_CONST | 7,908,894 | 2.1% | 68.1% |  |
| LOAD_GLOBAL_BUILTIN | 7,405,401 | 1.9% | 70.1% | 0.1% |
| LOAD_ATTR | 6,133,129 | 1.6% | 71.7% |  |
| CALL | 5,923,664 | 1.5% | 73.2% |  |
| INTERPRETER_EXIT | 5,742,569 | 1.5% | 74.7% |  |
| POP_JUMP_IF_NONE | 5,493,918 | 1.4% | 76.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,429,459 | 1.4% | 77.6% | 0.7% |
| POP_JUMP_IF_TRUE | 4,447,418 | 1.2% | 78.7% |  |
| LOAD_ATTR_SLOT | 4,326,350 | 1.1% | 79.9% | 6.9% |
| STORE_ATTR_SLOT | 3,653,471 | 1.0% | 80.8% | 19.3% |
| PUSH_NULL | 3,617,555 | 0.9% | 81.8% |  |
| NOP | 3,598,750 | 0.9% | 82.7% |  |
| COMPARE_OP_INT | 3,525,328 | 0.9% | 83.6% | 0.0% |
| LOAD_ATTR_MODULE | 3,142,357 | 0.8% | 84.4% | 0.0% |
| COPY | 2,500,351 | 0.7% | 85.1% |  |
| CALL_ISINSTANCE | 2,229,911 | 0.6% | 85.7% |  |
| LOAD_DEREF | 2,133,050 | 0.6% | 86.2% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,067,137 | 0.5% | 86.8% | 6.0% |
| JUMP_BACKWARD | 1,826,161 | 0.5% | 87.3% |  |
| POP_JUMP_IF_NOT_NONE | 1,705,872 | 0.4% | 87.7% |  |
| CALL_BUILTIN_FAST | 1,703,320 | 0.4% | 88.1% |  |
| SWAP | 1,546,037 | 0.4% | 88.6% |  |
| TO_BOOL_NONE | 1,527,761 | 0.4% | 89.0% | 1.7% |
| BUILD_TUPLE | 1,442,330 | 0.4% | 89.3% |  |
| TO_BOOL | 1,387,981 | 0.4% | 89.7% |  |
| BUILD_LIST | 1,251,000 | 0.3% | 90.0% |  |
| BINARY_OP | 1,203,008 | 0.3% | 90.3% |  |
| STORE_FAST_STORE_FAST | 1,147,196 | 0.3% | 90.6% |  |
| CALL_LEN | 1,101,370 | 0.3% | 90.9% |  |
| BINARY_OP_ADD_INT | 1,091,294 | 0.3% | 91.2% |  |
| CALL_FUNCTION_EX | 1,088,366 | 0.3% | 91.5% |  |
| FOR_ITER_LIST | 1,075,302 | 0.3% | 91.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 1,044,524 | 0.3% | 92.0% | 3.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 989,886 | 0.3% | 92.3% |  |
| TO_BOOL_INT | 948,359 | 0.2% | 92.5% | 0.7% |
| CONTAINS_OP | 907,820 | 0.2% | 92.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 906,136 | 0.2% | 93.0% |  |
| BINARY_SUBSCR_DICT | 904,558 | 0.2% | 93.3% |  |
| BINARY_OP_SUBTRACT_INT | 866,237 | 0.2% | 93.5% |  |
| JUMP_FORWARD | 865,868 | 0.2% | 93.7% |  |
| BUILD_MAP | 793,640 | 0.2% | 93.9% |  |
| GET_ITER | 788,702 | 0.2% | 94.1% |  |
| COPY_FREE_VARS | 782,850 | 0.2% | 94.3% |  |
| LOAD_ATTR_WITH_HINT | 764,634 | 0.2% | 94.5% | 2.1% |
| LOAD_ATTR_CLASS | 733,220 | 0.2% | 94.7% | 0.1% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 711,828 | 0.2% | 94.9% |  |
| LIST_EXTEND | 678,552 | 0.2% | 95.1% |  |
| CALL_INTRINSIC_1 | 666,532 | 0.2% | 95.3% |  |
| CALL_PY_WITH_DEFAULTS | 647,874 | 0.2% | 95.4% |  |
| YIELD_VALUE | 577,520 | 0.2% | 95.6% |  |
| IS_OP | 569,400 | 0.1% | 95.7% |  |
| STORE_SUBSCR_DICT | 565,080 | 0.1% | 95.9% |  |
| BINARY_SLICE | 554,160 | 0.1% | 96.0% |  |
| FOR_ITER_RANGE | 494,058 | 0.1% | 96.1% |  |
| DICT_MERGE | 480,760 | 0.1% | 96.3% |  |
| CALL_KW | 470,154 | 0.1% | 96.4% |  |
| PUSH_EXC_INFO | 460,760 | 0.1% | 96.5% |  |
| POP_EXCEPT | 460,640 | 0.1% | 96.6% |  |
| GET_AWAITABLE | 456,000 | 0.1% | 96.8% |  |
| CHECK_EXC_MATCH | 451,088 | 0.1% | 96.9% |  |
| END_SEND | 444,000 | 0.1% | 97.0% |  |
| BINARY_SUBSCR | 426,420 | 0.1% | 97.1% |  |
| BINARY_SUBSCR_GETITEM | 420,560 | 0.1% | 97.2% | 0.4% |
| MAKE_CELL | 409,218 | 0.1% | 97.3% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 384,180 | 0.1% | 97.4% | 3.1% |
| MAKE_FUNCTION | 359,598 | 0.1% | 97.5% |  |
| FOR_ITER | 357,960 | 0.1% | 97.6% |  |
| COMPARE_OP_FLOAT | 356,794 | 0.1% | 97.7% | 0.0% |
| SEND | 338,220 | 0.1% | 97.8% |  |
| RETURN_GENERATOR | 337,000 | 0.1% | 97.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 327,346 | 0.1% | 98.0% | 0.1% |
| EXIT_INIT_CHECK | 324,640 | 0.1% | 98.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 324,640 | 0.1% | 98.1% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 293,786 | 0.1% | 98.2% | 46.5% |
| TO_BOOL_STR | 290,720 | 0.1% | 98.3% | 3.3% |
| STORE_ATTR | 289,200 | 0.1% | 98.4% |  |
| SEND_GEN | 287,800 | 0.1% | 98.4% |  |
| COMPARE_OP_STR | 278,100 | 0.1% | 98.5% | 0.0% |
| FOR_ITER_GEN | 275,940 | 0.1% | 98.6% |  |
| CALL_LIST_APPEND | 259,823 | 0.1% | 98.6% |  |
| CALL_BUILTIN_CLASS | 246,486 | 0.1% | 98.7% |  |
| STORE_SUBSCR | 242,920 | 0.1% | 98.8% |  |
| BEFORE_WITH | 240,974 | 0.1% | 98.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 229,280 | 0.1% | 98.9% |  |
| BINARY_OP_ADD_UNICODE | 228,800 | 0.1% | 99.0% |  |
| STORE_FAST_LOAD_FAST | 218,840 | 0.1% | 99.0% |  |
| DELETE_FAST | 215,414 | 0.1% | 99.1% |  |
| SET_FUNCTION_ATTRIBUTE | 207,004 | 0.1% | 99.1% |  |
| EXTENDED_ARG | 206,700 | 0.1% | 99.2% |  |
| CALL_TYPE_1 | 205,260 | 0.1% | 99.2% |  |
| LOAD_SUPER_ATTR_METHOD | 194,280 | 0.1% | 99.3% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 191,374 | 0.0% | 99.3% |  |
| COMPARE_OP | 176,058 | 0.0% | 99.4% |  |
| TO_BOOL_LIST | 166,293 | 0.0% | 99.4% | 0.0% |
| FOR_ITER_TUPLE | 150,380 | 0.0% | 99.5% |  |
| STORE_DEREF | 121,600 | 0.0% | 99.5% |  |
| BINARY_OP_ADD_FLOAT | 121,288 | 0.0% | 99.5% |  |
| LOAD_ATTR_PROPERTY | 120,560 | 0.0% | 99.6% |  |
| DELETE_SUBSCR | 120,440 | 0.0% | 99.6% |  |
| LOAD_SUPER_ATTR_ATTR | 119,980 | 0.0% | 99.6% |  |
| UNPACK_SEQUENCE_LIST | 119,960 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_STR_INT | 108,860 | 0.0% | 99.7% | 0.1% |
| BINARY_SUBSCR_LIST_INT | 107,631 | 0.0% | 99.7% | 0.1% |
| LOAD_FAST_CHECK | 96,680 | 0.0% | 99.7% |  |
| UNPACK_SEQUENCE_TUPLE | 84,280 | 0.0% | 99.8% |  |
| BINARY_OP_SUBTRACT_FLOAT | 84,020 | 0.0% | 99.8% |  |
| CALL_BUILTIN_O | 77,297 | 0.0% | 99.8% |  |
| LOAD_FAST_AND_CLEAR | 73,440 | 0.0% | 99.8% |  |
| BUILD_SLICE | 72,060 | 0.0% | 99.8% |  |
| RERAISE | 72,020 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 60,400 | 0.0% | 99.9% |  |
| CONVERT_VALUE | 60,320 | 0.0% | 99.9% |  |
| UNARY_INVERT | 60,180 | 0.0% | 99.9% |  |
| END_FOR | 59,980 | 0.0% | 99.9% |  |
| STORE_ATTR_WITH_HINT | 59,018 | 0.0% | 99.9% | 9.0% |
| TO_BOOL_ALWAYS_TRUE | 48,240 | 0.0% | 99.9% | 0.1% |
| LOAD_GLOBAL | 28,700 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 24,420 | 0.0% | 100.0% |  |
| BUILD_STRING | 24,240 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 23,960 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 13,960 | 0.0% | 100.0% |  |
| LIST_APPEND | 13,780 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 12,240 | 0.0% | 100.0% |  |
| UNARY_NOT | 12,140 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 12,080 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 12,034 | 0.0% | 100.0% |  |
| BUILD_SET | 12,020 | 0.0% | 100.0% |  |
| RESUME | 9,300 | 0.0% | 100.0% | 10.9% |
| LOAD_NAME | 4,500 | 0.0% | 100.0% |  |
| STORE_NAME | 4,480 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 1,440 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,280 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,140 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 880 | 0.0% | 100.0% |  |
| CALL_STR_1 | 360 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 240 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 220 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 100 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 60 | 0.0% | 100.0% |  |
| SET_UPDATE | 20 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 23,277,070 | 6.1% | 6.1% |
| RESUME_CHECK LOAD_FAST | 11,475,162 | 3.0% | 9.1% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 10,813,040 | 2.8% | 11.9% |
| POP_JUMP_IF_FALSE LOAD_FAST | 8,315,100 | 2.2% | 14.1% |
| STORE_FAST LOAD_FAST | 7,949,937 | 2.1% | 16.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 7,370,609 | 1.9% | 18.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 6,139,176 | 1.6% | 19.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,445,263 | 1.4% | 21.1% |
| CACHE RESUME_CHECK | 5,394,197 | 1.4% | 22.5% |
| LOAD_CONST LOAD_FAST | 5,383,170 | 1.4% | 23.9% |
| RETURN_CONST POP_TOP | 5,228,558 | 1.4% | 25.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 5,000,055 | 1.3% | 26.6% |
| POP_JUMP_IF_NONE LOAD_FAST | 4,551,572 | 1.2% | 27.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 4,495,042 | 1.2% | 28.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 4,177,319 | 1.1% | 30.0% |
| LOAD_FAST LOAD_ATTR_SLOT | 4,146,209 | 1.1% | 31.1% |
| POP_TOP LOAD_FAST | 3,983,938 | 1.0% | 32.2% |
| LOAD_FAST LOAD_ATTR | 3,775,090 | 1.0% | 33.2% |
| RETURN_VALUE INTERPRETER_EXIT | 3,750,965 | 1.0% | 34.1% |
| LOAD_FAST LOAD_CONST | 3,460,282 | 0.9% | 35.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 3,456,227 | 0.9% | 35.9% |
| LOAD_FAST RETURN_VALUE | 3,170,800 | 0.8% | 36.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,127,217 | 0.8% | 37.6% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 3,035,562 | 0.8% | 38.4% |
| POP_TOP RETURN_CONST | 3,012,926 | 0.8% | 39.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,916,942 | 0.8% | 39.9% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,841,237 | 0.7% | 40.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 2,820,654 | 0.7% | 41.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 2,792,628 | 0.7% | 42.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 2,762,339 | 0.7% | 42.9% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 2,703,306 | 0.7% | 43.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 2,661,778 | 0.7% | 44.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,337,360 | 0.6% | 44.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,334,030 | 0.6% | 45.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,312,477 | 0.6% | 46.1% |
| RETURN_VALUE STORE_FAST | 2,208,094 | 0.6% | 46.7% |
| NOP LOAD_FAST | 2,176,812 | 0.6% | 47.2% |
| LOAD_FAST POP_JUMP_IF_NONE | 2,121,738 | 0.6% | 47.8% |
| LOAD_FAST CALL | 2,050,820 | 0.5% | 48.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 2,026,278 | 0.5% | 48.8% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 2,024,591 | 0.5% | 49.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,992,740 | 0.5% | 49.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,967,088 | 0.5% | 50.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,926,867 | 0.5% | 50.9% |
| RETURN_VALUE TO_BOOL_BOOL | 1,899,346 | 0.5% | 51.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 1,886,250 | 0.5% | 51.9% |
| LOAD_FAST STORE_ATTR_SLOT | 1,840,438 | 0.5% | 52.4% |
| CALL STORE_FAST | 1,802,444 | 0.5% | 52.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 1,799,484 | 0.5% | 53.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,758,144 | 0.5% | 53.8% |
| PUSH_NULL LOAD_FAST | 1,753,523 | 0.5% | 54.2% |
| LOAD_CONST COMPARE_OP_INT | 1,733,394 | 0.5% | 54.7% |
| RETURN_CONST INTERPRETER_EXIT | 1,713,964 | 0.4% | 55.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,701,831 | 0.4% | 55.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 1,680,134 | 0.4% | 56.0% |
| RESUME_CHECK NOP | 1,613,246 | 0.4% | 56.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,564,640 | 0.4% | 56.8% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,357,406 | 0.4% | 57.2% |
| LOAD_CONST STORE_FAST | 1,333,744 | 0.3% | 57.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 1,305,258 | 0.3% | 57.9% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 1,288,123 | 0.3% | 58.2% |
| LOAD_CONST LOAD_CONST | 1,222,508 | 0.3% | 58.5% |
| LOAD_ATTR LOAD_FAST | 1,202,398 | 0.3% | 58.9% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 1,180,171 | 0.3% | 59.2% |
| LOAD_FAST COPY | 1,153,111 | 0.3% | 59.5% |
| TO_BOOL POP_JUMP_IF_FALSE | 1,146,483 | 0.3% | 59.8% |
| POP_JUMP_IF_FALSE LOAD_CONST | 1,121,945 | 0.3% | 60.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,093,640 | 0.3% | 60.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 1,090,672 | 0.3% | 60.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,057,046 | 0.3% | 60.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,055,214 | 0.3% | 61.2% |
| STORE_ATTR_SLOT LOAD_CONST | 1,048,672 | 0.3% | 61.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,043,920 | 0.3% | 61.7% |
| LOAD_ATTR PUSH_NULL | 1,040,606 | 0.3% | 62.0% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 1,030,586 | 0.3% | 62.3% |
| BUILD_LIST LOAD_FAST | 1,027,352 | 0.3% | 62.5% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 1,020,096 | 0.3% | 62.8% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 1,007,440 | 0.3% | 63.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 997,420 | 0.3% | 63.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 994,076 | 0.3% | 63.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 984,100 | 0.3% | 63.9% |
| CALL POP_TOP | 983,752 | 0.3% | 64.1% |
| RETURN_VALUE RETURN_VALUE | 973,560 | 0.3% | 64.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 971,488 | 0.3% | 64.6% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 960,111 | 0.3% | 64.9% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 960,111 | 0.3% | 65.1% |
| POP_TOP JUMP_BACKWARD | 925,573 | 0.2% | 65.4% |
| POP_TOP LOAD_CONST | 924,034 | 0.2% | 65.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 900,980 | 0.2% | 65.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 893,696 | 0.2% | 66.1% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 892,920 | 0.2% | 66.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 887,332 | 0.2% | 66.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 879,674 | 0.2% | 66.8% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 856,812 | 0.2% | 67.0% |
| LOAD_FAST CALL_BUILTIN_FAST | 838,040 | 0.2% | 67.2% |
| CALL_BUILTIN_FAST STORE_FAST | 814,860 | 0.2% | 67.4% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 814,604 | 0.2% | 67.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 806,983 | 0.2% | 67.8% |
| STORE_FAST LOAD_CONST | 797,063 | 0.2% | 68.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_INSTANCE_VALUE | 791,180 | 0.2% | 68.3% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 311,940 | 56.3% |
| LOAD_CONST | 193,620 | 34.9% |
| LOAD_FAST | 48,540 | 8.8% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 251,960 | 45.5% |
| STORE_FAST | 132,340 | 23.9% |
| CALL_PY_EXACT_ARGS | 60,200 | 10.9% |
| GET_ITER | 36,240 | 6.5% |
| RETURN_VALUE | 24,000 | 4.3% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,394,197 | 93.7% |
| COPY_FREE_VARS | 239,012 | 4.2% |
| POP_TOP | 97,060 | 1.7% |
| MAKE_CELL | 12,360 | 0.2% |
| RETURN_GENERATOR | 12,000 | 0.2% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 119,514 | 49.6% |
| RETURN_VALUE | 108,100 | 44.9% |
| LOAD_GLOBAL_MODULE | 12,540 | 5.2% |
| CALL | 380 | 0.2% |
| LOAD_ATTR | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 240,894 | 100.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 40.0% |
| BINARY_SUBSCR_STR_INT | 40 | 40.0% |
| BINARY_OP | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| LOAD_GLOBAL_MODULE | 40 | 40.0% |
| LOAD_GLOBAL | 20 | 20.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 421,700 | 98.9% |
| BINARY_SUBSCR | 3,000 | 0.7% |
| BUILD_TUPLE | 640 | 0.2% |
| LOAD_FAST | 420 | 0.1% |
| LOAD_NAME | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 263,880 | 61.9% |
| LOAD_FAST | 60,140 | 14.1% |
| CONVERT_VALUE | 24,000 | 5.6% |
| LOAD_CONST | 12,960 | 3.0% |
| BINARY_SUBSCR_LIST_INT | 12,300 | 2.9% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 391,454 | 86.8% |
| BUILD_TUPLE | 24,080 | 5.3% |
| LOAD_ATTR_MODULE | 23,294 | 5.2% |
| LOAD_GLOBAL_MODULE | 11,980 | 2.7% |
| LOAD_GLOBAL | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 451,088 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 72,000 | 59.8% |
| LOAD_FAST | 48,280 | 40.1% |
| LOAD_CONST | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,120 | 59.9% |
| RETURN_CONST | 36,080 | 30.0% |
| LOAD_FAST | 12,000 | 10.0% |
| JUMP_BACKWARD | 160 | 0.1% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 59,980 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 59,980 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 276,000 | 62.2% |
| RETURN_CONST | 132,000 | 29.7% |
| RETURN_VALUE | 36,000 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 288,000 | 64.9% |
| POP_TOP | 144,000 | 32.4% |
| UNPACK_SEQUENCE_TUPLE | 11,960 | 2.7% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 324,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 324,640 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 60,320 | 99.9% |
| LOAD_FAST_LOAD_FAST | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,320 | 99.9% |
| BUILD_STRING | 80 | 0.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 324,516 | 41.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 144,140 | 18.3% |
| LOAD_ATTR_INSTANCE_VALUE | 96,580 | 12.2% |
| LOAD_ATTR | 72,140 | 9.1% |
| BINARY_SLICE | 36,240 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 403,136 | 51.1% |
| FOR_ITER | 148,540 | 18.8% |
| FOR_ITER_TUPLE | 73,020 | 9.3% |
| CALL_PY_EXACT_ARGS | 72,760 | 9.2% |
| LOAD_FAST_AND_CLEAR | 49,440 | 6.3% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,750,965 | 65.3% |
| RETURN_CONST | 1,713,964 | 29.8% |
| YIELD_VALUE | 253,560 | 4.4% |
| RETURN_GENERATOR | 24,080 | 0.4% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 180 | 81.8% |
| POP_TOP | 20 | 9.1% |
| POP_JUMP_IF_FALSE | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 220 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 359,598 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 154,898 | 43.1% |
| CALL | 120,080 | 33.4% |
| LOAD_FAST | 48,400 | 13.5% |
| CALL_PY_EXACT_ARGS | 23,920 | 6.7% |
| STORE_DEREF | 12,000 | 3.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,613,246 | 44.8% |
| POP_JUMP_IF_FALSE | 534,183 | 14.8% |
| STORE_FAST | 498,935 | 13.9% |
| STORE_ATTR_INSTANCE_VALUE | 363,386 | 10.1% |
| POP_JUMP_IF_TRUE | 196,252 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,176,812 | 60.5% |
| LOAD_GLOBAL_MODULE | 591,840 | 16.4% |
| LOAD_FAST_LOAD_FAST | 300,220 | 8.3% |
| LOAD_DEREF | 146,558 | 4.1% |
| NOP | 122,808 | 3.4% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 256,746 | 55.7% |
| SWAP | 132,240 | 28.7% |
| COPY | 36,020 | 7.8% |
| STORE_ATTR_INSTANCE_VALUE | 12,120 | 2.6% |
| STORE_SUBSCR_DICT | 12,000 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 218,448 | 47.4% |
| RETURN_VALUE | 132,240 | 28.7% |
| RERAISE | 36,020 | 7.8% |
| DELETE_FAST | 24,000 | 5.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 23,374 | 5.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,228,558 | 50.9% |
| CALL | 983,752 | 9.6% |
| CALL_METHOD_DESCRIPTOR_O | 814,604 | 7.9% |
| POP_JUMP_IF_FALSE | 623,326 | 6.1% |
| CALL_FUNCTION_EX | 500,812 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,983,938 | 38.8% |
| RETURN_CONST | 3,012,926 | 29.3% |
| JUMP_BACKWARD | 925,573 | 9.0% |
| LOAD_CONST | 924,034 | 9.0% |
| RESUME_CHECK | 336,620 | 3.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 346,980 | 75.3% |
| CALL | 37,682 | 8.2% |
| RERAISE | 36,020 | 7.8% |
| CALL_METHOD_DESCRIPTOR_O | 24,060 | 5.2% |
| RAISE_VARARGS | 12,000 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 400,986 | 87.0% |
| LOAD_GLOBAL_MODULE | 47,174 | 10.2% |
| LOAD_FAST | 12,000 | 2.6% |
| LOAD_GLOBAL | 600 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,701,831 | 47.0% |
| LOAD_ATTR | 1,040,606 | 28.8% |
| LOAD_FAST | 476,418 | 13.2% |
| LOAD_DEREF | 204,500 | 5.7% |
| RETURN_VALUE | 132,080 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,753,523 | 48.5% |
| CALL | 737,342 | 20.4% |
| LOAD_FAST_LOAD_FAST | 713,784 | 19.7% |
| LOAD_GLOBAL_MODULE | 108,380 | 3.0% |
| LOAD_CONST | 96,100 | 2.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 264,140 | 78.4% |
| COPY_FREE_VARS | 24,600 | 7.3% |
| CACHE | 12,000 | 3.6% |
| CALL_KW | 12,000 | 3.6% |
| MAKE_CELL | 12,000 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 84,000 | 24.9% |
| RETURN_VALUE | 60,000 | 17.8% |
| GET_AWAITABLE | 60,000 | 17.8% |
| CALL | 36,080 | 10.7% |
| GET_ITER | 36,000 | 10.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,170,800 | 27.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,703,306 | 23.2% |
| RETURN_VALUE | 973,560 | 8.3% |
| CALL | 627,256 | 5.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 622,560 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 3,750,965 | 32.2% |
| STORE_FAST | 2,208,094 | 18.9% |
| TO_BOOL_BOOL | 1,899,346 | 16.3% |
| RETURN_VALUE | 973,560 | 8.3% |
| LOAD_FAST | 603,728 | 5.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 108,580 | 44.7% |
| LOAD_CONST | 96,180 | 39.6% |
| LOAD_FAST_LOAD_FAST | 36,000 | 14.8% |
| STORE_SUBSCR | 1,760 | 0.7% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 108,240 | 44.6% |
| LOAD_FAST | 48,240 | 19.9% |
| JUMP_BACKWARD | 36,020 | 14.8% |
| LOAD_CONST | 24,060 | 9.9% |
| LOAD_DEREF | 24,000 | 9.9% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 604,188 | 43.5% |
| LOAD_FAST | 598,910 | 43.1% |
| LOAD_ATTR | 122,800 | 8.8% |
| COPY | 36,800 | 2.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 12,380 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,146,483 | 82.6% |
| POP_JUMP_IF_TRUE | 227,914 | 16.4% |
| TO_BOOL | 5,983 | 0.4% |
| TO_BOOL_BOOL | 5,200 | 0.4% |
| TO_BOOL_NONE | 1,081 | 0.1% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 36,040 | 59.9% |
| BINARY_OP | 24,100 | 40.0% |
| LOAD_ATTR | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 60,180 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 11,980 | 98.7% |
| TO_BOOL_INT | 60 | 0.5% |
| TO_BOOL_LIST | 60 | 0.5% |
| TO_BOOL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,000 | 98.8% |
| COPY | 80 | 0.7% |
| CALL_PY_EXACT_ARGS | 60 | 0.5% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 230,998 | 19.2% |
| LOAD_CONST | 168,994 | 14.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 155,880 | 13.0% |
| LOAD_FAST | 106,707 | 8.9% |
| LOAD_ATTR_MODULE | 105,132 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 321,972 | 26.8% |
| STORE_FAST | 211,586 | 17.6% |
| COPY | 177,412 | 14.7% |
| LOAD_FAST | 96,640 | 8.0% |
| RETURN_VALUE | 96,120 | 8.0% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 12,000 | 98.0% |
| RETURN_VALUE | 80 | 0.7% |
| LOAD_FAST | 80 | 0.7% |
| STORE_FAST | 80 | 0.7% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 382,940 | 30.6% |
| LOAD_ATTR_SLOT | 380,312 | 30.4% |
| STORE_FAST | 111,248 | 8.9% |
| LOAD_FAST_LOAD_FAST | 107,540 | 8.6% |
| RESUME_CHECK | 72,940 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,027,352 | 82.1% |
| STORE_FAST | 136,908 | 10.9% |
| SWAP | 49,440 | 4.0% |
| LOAD_CONST | 24,120 | 1.9% |
| CALL_BUILTIN_CLASS | 11,960 | 1.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 277,040 | 34.9% |
| CALL_INTRINSIC_1 | 154,660 | 19.5% |
| RESUME_CHECK | 96,080 | 12.1% |
| STORE_ATTR_INSTANCE_VALUE | 72,420 | 9.1% |
| BUILD_TUPLE | 72,120 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 649,720 | 81.9% |
| CALL_FUNCTION_EX | 59,200 | 7.5% |
| STORE_FAST | 48,380 | 6.1% |
| RETURN_VALUE | 24,000 | 3.0% |
| LOAD_DEREF | 12,020 | 1.5% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,980 | 99.7% |
| LOAD_GLOBAL | 20 | 0.2% |
| STORE_NAME | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 12,000 | 99.8% |
| LOAD_CONST | 20 | 0.2% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 71,980 | 99.9% |
| LOAD_CONST | 60 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 72,000 | 99.9% |
| BINARY_SUBSCR | 60 | 0.1% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,160 | 99.7% |
| FORMAT_SIMPLE | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 12,000 | 49.5% |
| CALL_PY_EXACT_ARGS | 11,960 | 49.3% |
| CALL | 200 | 0.8% |
| STORE_DEREF | 80 | 0.3% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 513,452 | 35.6% |
| LOAD_FAST_LOAD_FAST | 384,540 | 26.7% |
| LOAD_GLOBAL_BUILTIN | 204,400 | 14.2% |
| LOAD_GLOBAL_MODULE | 99,540 | 6.9% |
| LOAD_ATTR_MODULE | 71,940 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 204,940 | 14.2% |
| CALL_METHOD_DESCRIPTOR_O | 191,840 | 13.3% |
| RETURN_VALUE | 180,760 | 12.5% |
| LOAD_CONST | 154,518 | 10.7% |
| CONTAINS_OP | 121,400 | 8.4% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,050,820 | 34.6% |
| PUSH_NULL | 737,342 | 12.4% |
| LOAD_CONST | 590,548 | 10.0% |
| LOAD_GLOBAL_MODULE | 568,778 | 9.6% |
| LOAD_FAST_LOAD_FAST | 440,206 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,802,444 | 30.4% |
| POP_TOP | 983,752 | 16.6% |
| LOAD_FAST | 735,086 | 12.4% |
| RETURN_VALUE | 627,256 | 10.6% |
| BINARY_SUBSCR_DICT | 420,140 | 7.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 480,760 | 44.2% |
| CALL_INTRINSIC_1 | 440,672 | 40.5% |
| LOAD_FAST | 107,654 | 9.9% |
| BUILD_MAP | 59,200 | 5.4% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 500,812 | 46.0% |
| RETURN_VALUE | 228,374 | 21.0% |
| RESUME_CHECK | 132,220 | 12.1% |
| STORE_FAST | 119,360 | 11.0% |
| CALL | 83,300 | 7.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 654,532 | 98.2% |
| RERAISE | 12,000 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 440,672 | 66.1% |
| BUILD_MAP | 154,660 | 23.2% |
| LOAD_CONST | 59,200 | 8.9% |
| RERAISE | 12,000 | 1.8% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 470,154 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 265,420 | 56.5% |
| STORE_FAST | 107,454 | 22.9% |
| COPY_FREE_VARS | 24,000 | 5.1% |
| RETURN_VALUE | 12,440 | 2.6% |
| LOAD_FAST | 12,180 | 2.6% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 111,600 | 63.4% |
| LOAD_ATTR | 24,440 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 12,340 | 7.0% |
| LOAD_FAST_LOAD_FAST | 12,000 | 6.8% |
| LOAD_ATTR_CLASS | 12,000 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 111,594 | 63.4% |
| POP_JUMP_IF_TRUE | 60,580 | 34.4% |
| COMPARE_OP | 1,744 | 1.0% |
| COMPARE_OP_INT | 1,440 | 0.8% |
| COMPARE_OP_STR | 460 | 0.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 217,020 | 23.9% |
| LOAD_ATTR_INSTANCE_VALUE | 204,420 | 22.5% |
| LOAD_CONST | 145,500 | 16.0% |
| BUILD_TUPLE | 121,400 | 13.4% |
| LOAD_FAST_LOAD_FAST | 108,880 | 12.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 606,060 | 66.8% |
| POP_JUMP_IF_TRUE | 133,040 | 14.7% |
| COPY | 120,040 | 13.2% |
| SWAP | 24,000 | 2.6% |
| STORE_FAST | 12,080 | 1.3% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 35,940 | 59.6% |
| BINARY_SUBSCR | 24,000 | 39.8% |
| LOAD_FAST | 240 | 0.4% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |
| LOAD_ATTR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 60,320 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,153,111 | 46.1% |
| LOAD_CONST | 252,200 | 10.1% |
| STORE_ATTR_INSTANCE_VALUE | 227,980 | 9.1% |
| BINARY_OP | 177,412 | 7.1% |
| SWAP | 132,240 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 960,111 | 38.4% |
| LOAD_FAST | 456,000 | 18.2% |
| TO_BOOL_BOOL | 326,140 | 13.0% |
| TO_BOOL_INT | 205,107 | 8.2% |
| TO_BOOL_NONE | 190,713 | 7.6% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 288,640 | 36.9% |
| CACHE | 239,012 | 30.5% |
| CALL | 120,900 | 15.4% |
| LOAD_ATTR_PROPERTY | 83,920 | 10.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,098 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 733,290 | 93.7% |
| RETURN_GENERATOR | 24,600 | 3.1% |
| MAKE_CELL | 24,100 | 3.1% |
| RESUME | 860 | 0.1% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 108,000 | 50.1% |
| NOP | 24,000 | 11.1% |
| POP_EXCEPT | 24,000 | 11.1% |
| STORE_ATTR_INSTANCE_VALUE | 23,980 | 11.1% |
| POP_TOP | 23,334 | 10.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 108,000 | 50.1% |
| RETURN_CONST | 48,000 | 22.3% |
| LOAD_FAST | 35,334 | 16.4% |
| LOAD_CONST | 12,080 | 5.6% |
| JUMP_BACKWARD | 12,000 | 5.6% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 432,640 | 90.0% |
| LOAD_ATTR_INSTANCE_VALUE | 36,040 | 7.5% |
| LOAD_ATTR | 12,080 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 480,760 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 119,920 | 58.0% |
| POP_JUMP_IF_TRUE | 60,060 | 29.1% |
| COMPARE_OP_STR | 12,180 | 5.9% |
| STORE_ATTR_INSTANCE_VALUE | 11,980 | 5.8% |
| JUMP_BACKWARD | 640 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 108,000 | 52.2% |
| JUMP_BACKWARD | 60,720 | 29.4% |
| POP_JUMP_IF_FALSE | 24,680 | 11.9% |
| JUMP_FORWARD | 12,340 | 6.0% |
| FOR_ITER_LIST | 520 | 0.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 157,980 | 44.1% |
| GET_ITER | 148,540 | 41.5% |
| SWAP | 24,460 | 6.8% |
| LOAD_FAST | 24,200 | 6.8% |
| FOR_ITER | 2,340 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 135,399 | 37.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 108,280 | 30.2% |
| STORE_FAST | 49,481 | 13.8% |
| LOAD_FAST | 24,340 | 6.8% |
| SWAP | 24,080 | 6.7% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 276,000 | 60.5% |
| LOAD_FAST | 108,000 | 23.7% |
| RETURN_GENERATOR | 60,000 | 13.2% |
| LOAD_ATTR_INSTANCE_VALUE | 11,980 | 2.6% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 456,000 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 680 | 53.1% |
| IMPORT_NAME | 600 | 46.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 1,140 | 89.1% |
| STORE_FAST | 140 | 10.9% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 600 | 52.6% |
| STORE_NAME | 520 | 45.6% |
| STORE_FAST | 20 | 1.8% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 315,460 | 55.4% |
| LOAD_FAST | 108,560 | 19.1% |
| LOAD_CONST | 108,160 | 19.0% |
| LOAD_DEREF | 24,000 | 4.2% |
| LOAD_FAST_LOAD_FAST | 12,360 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 460,940 | 81.0% |
| RETURN_VALUE | 72,100 | 12.7% |
| POP_JUMP_IF_TRUE | 12,360 | 2.2% |
| COPY | 12,000 | 2.1% |
| STORE_FAST | 12,000 | 2.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 925,573 | 50.7% |
| POP_JUMP_IF_TRUE | 306,466 | 16.8% |
| FOR_ITER_LIST | 108,200 | 5.9% |
| CALL_LIST_APPEND | 103,342 | 5.7% |
| POP_JUMP_IF_FALSE | 85,969 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 658,346 | 36.1% |
| FOR_ITER_RANGE | 464,532 | 25.4% |
| FOR_ITER_GEN | 215,960 | 11.8% |
| FOR_ITER | 157,980 | 8.7% |
| LOAD_FAST | 153,783 | 8.4% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 167,760 | 87.7% |
| POP_EXCEPT | 23,374 | 12.2% |
| RESUME | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 108,000 | 56.4% |
| SEND | 60,000 | 31.4% |
| LOAD_FAST | 23,374 | 12.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 440,014 | 50.8% |
| POP_TOP | 132,480 | 15.3% |
| POP_JUMP_IF_TRUE | 108,080 | 12.5% |
| STORE_ATTR_INSTANCE_VALUE | 48,380 | 5.6% |
| LOAD_CONST | 36,020 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 569,200 | 65.7% |
| LOAD_CONST | 85,366 | 9.9% |
| LOAD_FAST_LOAD_FAST | 60,420 | 7.0% |
| LOAD_GLOBAL_BUILTIN | 41,922 | 4.8% |
| CALL | 36,000 | 4.2% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 12,040 | 87.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,160 | 8.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 320 | 2.3% |
| LOAD_FAST | 240 | 1.7% |
| CALL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,780 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 380,312 | 56.0% |
| LOAD_FAST | 262,020 | 38.6% |
| LOAD_CONST | 24,020 | 3.5% |
| LOAD_ATTR_INSTANCE_VALUE | 11,980 | 1.8% |
| LOAD_DEREF | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 654,532 | 96.5% |
| LOAD_FAST | 24,000 | 3.5% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,775,090 | 61.6% |
| LOAD_ATTR_INSTANCE_VALUE | 879,674 | 14.3% |
| LOAD_ATTR_SLOT | 380,372 | 6.2% |
| LOAD_ATTR_WITH_HINT | 335,900 | 5.5% |
| LOAD_GLOBAL_MODULE | 303,620 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,202,398 | 19.6% |
| PUSH_NULL | 1,040,606 | 17.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,007,440 | 16.4% |
| LOAD_CONST | 483,080 | 7.9% |
| CALL_PY_EXACT_ARGS | 324,045 | 5.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,460,282 | 20.4% |
| STORE_ATTR_INSTANCE_VALUE | 1,680,134 | 9.9% |
| LOAD_CONST | 1,222,508 | 7.2% |
| POP_JUMP_IF_FALSE | 1,121,945 | 6.6% |
| STORE_ATTR_SLOT | 1,048,672 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,383,170 | 31.7% |
| COMPARE_OP_INT | 1,733,394 | 10.2% |
| STORE_FAST | 1,333,744 | 7.8% |
| LOAD_CONST | 1,222,508 | 7.2% |
| CALL_PY_EXACT_ARGS | 659,820 | 3.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 401,806 | 18.8% |
| RESUME_CHECK | 207,846 | 9.7% |
| POP_JUMP_IF_FALSE | 171,866 | 8.1% |
| NOP | 146,558 | 6.9% |
| POP_JUMP_IF_TRUE | 144,340 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 506,920 | 23.8% |
| LOAD_ATTR_INSTANCE_VALUE | 369,678 | 17.3% |
| PUSH_NULL | 204,500 | 9.6% |
| STORE_ATTR_INSTANCE_VALUE | 155,680 | 7.3% |
| LOAD_ATTR | 152,592 | 7.2% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,475,162 | 14.5% |
| POP_JUMP_IF_FALSE | 8,315,100 | 10.5% |
| STORE_FAST | 7,949,937 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 5,445,263 | 6.9% |
| LOAD_CONST | 5,383,170 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 23,277,070 | 29.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,139,176 | 7.7% |
| STORE_ATTR_INSTANCE_VALUE | 5,000,055 | 6.3% |
| LOAD_ATTR_SLOT | 4,146,209 | 5.2% |
| LOAD_ATTR | 3,775,090 | 4.8% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 49,440 | 67.3% |
| LOAD_FAST_AND_CLEAR | 24,000 | 32.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 49,440 | 67.3% |
| LOAD_FAST_AND_CLEAR | 24,000 | 32.7% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 72,060 | 74.5% |
| POP_JUMP_IF_FALSE | 12,000 | 12.4% |
| STORE_FAST | 12,000 | 12.4% |
| POP_TOP | 320 | 0.3% |
| JUMP_FORWARD | 180 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 71,960 | 74.4% |
| LOAD_ATTR | 12,000 | 12.4% |
| LOAD_CONST | 12,000 | 12.4% |
| POP_JUMP_IF_NOT_NONE | 440 | 0.5% |
| LOAD_FAST | 80 | 0.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,305,258 | 12.6% |
| LOAD_GLOBAL_MODULE | 1,093,640 | 10.6% |
| STORE_FAST | 1,057,046 | 10.2% |
| STORE_ATTR_INSTANCE_VALUE | 997,420 | 9.6% |
| POP_JUMP_IF_FALSE | 900,980 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,992,740 | 19.2% |
| STORE_ATTR_SLOT | 1,799,484 | 17.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,357,406 | 13.1% |
| LOAD_FAST | 887,332 | 8.6% |
| LOAD_FAST_LOAD_FAST | 734,946 | 7.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,560 | 12.4% |
| POP_JUMP_IF_FALSE | 3,460 | 12.1% |
| RESUME | 2,480 | 8.6% |
| RESUME_CHECK | 2,420 | 8.4% |
| STORE_FAST | 2,320 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,700 | 33.8% |
| LOAD_GLOBAL_BUILTIN | 4,380 | 15.3% |
| LOAD_ATTR | 4,140 | 14.4% |
| LOAD_FAST | 4,060 | 14.1% |
| CALL | 1,740 | 6.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,620 | 58.2% |
| LOAD_NAME | 1,200 | 26.7% |
| RESUME | 220 | 4.9% |
| STORE_NAME | 180 | 4.0% |
| LOAD_ATTR | 120 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,260 | 28.0% |
| LOAD_NAME | 1,200 | 26.7% |
| LOAD_ATTR | 660 | 14.7% |
| BUILD_TUPLE | 440 | 9.8% |
| BINARY_SUBSCR | 340 | 7.6% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 820 | 93.2% |
| LOAD_DEREF | 60 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 280 | 31.8% |
| LOAD_FAST | 180 | 20.5% |
| CALL | 120 | 13.6% |
| PUSH_NULL | 100 | 11.4% |
| LOAD_SUPER_ATTR_ATTR | 100 | 11.4% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 188,212 | 46.0% |
| CALL_PY_EXACT_ARGS | 160,006 | 39.1% |
| COPY_FREE_VARS | 24,100 | 5.9% |
| CACHE | 12,360 | 3.0% |
| CALL | 12,320 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 208,486 | 50.9% |
| MAKE_CELL | 188,212 | 46.0% |
| RETURN_GENERATOR | 12,000 | 2.9% |
| RESUME | 520 | 0.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 7,370,609 | 48.1% |
| COMPARE_OP_INT | 2,792,628 | 18.2% |
| TO_BOOL_NONE | 1,288,123 | 8.4% |
| TO_BOOL | 1,146,483 | 7.5% |
| CONTAINS_OP | 606,060 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,315,100 | 54.2% |
| RETURN_CONST | 1,564,640 | 10.2% |
| LOAD_CONST | 1,121,945 | 7.3% |
| LOAD_GLOBAL_MODULE | 1,055,214 | 6.9% |
| LOAD_FAST_LOAD_FAST | 900,980 | 5.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,035,562 | 55.3% |
| LOAD_FAST | 2,121,738 | 38.6% |
| LOAD_ATTR | 132,960 | 2.4% |
| LOAD_DEREF | 132,080 | 2.4% |
| LOAD_ATTR_WITH_HINT | 34,958 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,551,572 | 82.8% |
| RETURN_CONST | 280,026 | 5.1% |
| LOAD_GLOBAL_MODULE | 276,580 | 5.0% |
| LOAD_FAST_LOAD_FAST | 144,440 | 2.6% |
| NOP | 132,300 | 2.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,090,672 | 63.9% |
| LOAD_ATTR_INSTANCE_VALUE | 456,040 | 26.7% |
| LOAD_ATTR | 108,980 | 6.4% |
| LOAD_GLOBAL_MODULE | 12,600 | 0.7% |
| CALL | 12,020 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 630,160 | 36.9% |
| LOAD_FAST_LOAD_FAST | 435,826 | 25.5% |
| LOAD_GLOBAL_MODULE | 336,986 | 19.8% |
| LOAD_CONST | 132,200 | 7.7% |
| LOAD_DEREF | 84,280 | 4.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,334,030 | 52.5% |
| COMPARE_OP_INT | 708,520 | 15.9% |
| TO_BOOL_INT | 345,016 | 7.8% |
| TO_BOOL_STR | 241,840 | 5.4% |
| TO_BOOL_NONE | 239,158 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,026,278 | 45.6% |
| LOAD_GLOBAL_BUILTIN | 497,160 | 11.2% |
| JUMP_BACKWARD | 306,466 | 6.9% |
| LOAD_CONST | 290,454 | 6.5% |
| LOAD_FAST_LOAD_FAST | 228,460 | 5.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_KW | 12,020 | 49.2% |
| POP_TOP | 12,000 | 49.1% |
| CALL | 380 | 1.6% |
| LOAD_CONST | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 12,020 | 50.0% |
| PUSH_EXC_INFO | 12,000 | 50.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 36,020 | 50.0% |
| POP_TOP | 12,000 | 16.7% |
| CALL_INTRINSIC_1 | 12,000 | 16.7% |
| POP_JUMP_IF_FALSE | 12,000 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 36,020 | 50.0% |
| COPY | 24,000 | 33.3% |
| CALL_INTRINSIC_1 | 12,000 | 16.7% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,012,926 | 38.1% |
| POP_JUMP_IF_FALSE | 1,564,640 | 19.8% |
| STORE_ATTR_INSTANCE_VALUE | 761,188 | 9.6% |
| STORE_ATTR_SLOT | 613,606 | 7.8% |
| STORE_FAST | 395,340 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,228,558 | 66.1% |
| INTERPRETER_EXIT | 1,713,964 | 21.7% |
| EXIT_INIT_CHECK | 324,640 | 4.1% |
| STORE_FAST | 169,366 | 2.1% |
| TO_BOOL_BOOL | 132,400 | 1.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 276,400 | 81.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 60,000 | 17.7% |
| SEND | 1,820 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 276,000 | 81.6% |
| YIELD_VALUE | 60,000 | 17.7% |
| SEND | 1,820 | 0.5% |
| POP_TOP | 200 | 0.1% |
| SEND_GEN | 200 | 0.1% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 154,898 | 74.8% |
| SET_FUNCTION_ATTRIBUTE | 52,106 | 25.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 64,852 | 31.3% |
| SET_FUNCTION_ATTRIBUTE | 52,106 | 25.2% |
| CALL | 39,846 | 19.2% |
| LOAD_FAST | 24,360 | 11.8% |
| CALL_PY_EXACT_ARGS | 12,040 | 5.8% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 20 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 181,000 | 62.6% |
| LOAD_FAST_LOAD_FAST | 54,500 | 18.8% |
| LOAD_DEREF | 36,480 | 12.6% |
| STORE_FAST_LOAD_FAST | 12,080 | 4.2% |
| STORE_ATTR | 4,200 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 60,460 | 20.9% |
| LOAD_FAST | 51,560 | 17.8% |
| RETURN_CONST | 49,720 | 17.2% |
| LOAD_GLOBAL_BUILTIN | 35,960 | 12.4% |
| JUMP_FORWARD | 24,120 | 8.3% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60,140 | 49.5% |
| LOAD_CONST | 12,300 | 10.1% |
| CALL | 12,040 | 9.9% |
| MAKE_FUNCTION | 12,000 | 9.9% |
| JUMP_FORWARD | 12,000 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,240 | 39.7% |
| LOAD_GLOBAL_MODULE | 36,120 | 29.7% |
| LOAD_FAST | 24,280 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 12,360 | 10.2% |
| LOAD_GLOBAL | 340 | 0.3% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,208,094 | 17.7% |
| CALL | 1,802,444 | 14.4% |
| LOAD_CONST | 1,333,744 | 10.7% |
| CALL_BUILTIN_FAST | 814,860 | 6.5% |
| LOAD_ATTR_INSTANCE_VALUE | 771,762 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,949,937 | 63.6% |
| LOAD_FAST_LOAD_FAST | 1,057,046 | 8.5% |
| LOAD_CONST | 797,063 | 6.4% |
| LOAD_GLOBAL_BUILTIN | 523,668 | 4.2% |
| NOP | 498,935 | 4.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 107,980 | 49.3% |
| COPY | 84,060 | 38.4% |
| STORE_ATTR | 12,000 | 5.5% |
| FOR_ITER_RANGE | 11,980 | 5.5% |
| FOR_ITER_TUPLE | 1,160 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 108,640 | 49.6% |
| STORE_ATTR_INSTANCE_VALUE | 83,920 | 38.3% |
| STORE_ATTR | 12,080 | 5.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,960 | 5.5% |
| TO_BOOL_STR | 1,160 | 0.5% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 893,696 | 77.9% |
| UNPACK_SEQUENCE_LIST | 119,960 | 10.5% |
| UNPACK_SEQUENCE_TUPLE | 72,300 | 6.3% |
| COPY | 24,200 | 2.1% |
| STORE_FAST_STORE_FAST | 24,160 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 629,296 | 54.9% |
| LOAD_FAST_LOAD_FAST | 168,500 | 14.7% |
| LOAD_GLOBAL_MODULE | 131,880 | 11.5% |
| STORE_FAST | 96,460 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 84,180 | 7.3% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 1,640 | 36.6% |
| IMPORT_FROM | 1,140 | 25.4% |
| IMPORT_NAME | 520 | 11.6% |
| LOAD_CONST | 460 | 10.3% |
| CALL | 300 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,500 | 55.8% |
| IMPORT_FROM | 680 | 15.2% |
| POP_TOP | 460 | 10.3% |
| LOAD_BUILD_CLASS | 180 | 4.0% |
| LOAD_NAME | 180 | 4.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 574,394 | 37.2% |
| BINARY_OP_SUBTRACT_INT | 361,997 | 23.4% |
| LOAD_FAST | 264,460 | 17.1% |
| LOAD_ATTR | 88,706 | 5.7% |
| BUILD_LIST | 49,440 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 960,111 | 62.1% |
| POP_EXCEPT | 132,240 | 8.6% |
| COPY | 132,240 | 8.6% |
| STORE_FAST | 125,486 | 8.1% |
| LOAD_CONST | 72,280 | 4.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,080 | 86.5% |
| RETURN_VALUE | 540 | 3.9% |
| CALL | 220 | 1.6% |
| FOR_ITER | 220 | 1.6% |
| BINARY_SUBSCR | 160 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 12,800 | 91.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 660 | 4.7% |
| UNPACK_SEQUENCE_TUPLE | 180 | 1.3% |
| UNPACK_SEQUENCE | 160 | 1.1% |
| LOAD_FAST | 80 | 0.6% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 108,100 | 18.7% |
| YIELD_VALUE | 108,000 | 18.7% |
| BINARY_OP_ADD_UNICODE | 107,980 | 18.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 107,980 | 18.7% |
| RETURN_VALUE | 60,580 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 253,560 | 43.9% |
| YIELD_VALUE | 108,000 | 18.7% |
| STORE_FAST_LOAD_FAST | 107,980 | 18.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 107,960 | 18.7% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 4,780 | 51.4% |
| CACHE | 2,020 | 21.7% |
| COPY_FREE_VARS | 860 | 9.2% |
| MAKE_CELL | 520 | 5.6% |
| POP_TOP | 380 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,020 | 43.2% |
| LOAD_GLOBAL | 2,480 | 26.7% |
| NOP | 600 | 6.5% |
| LOAD_CONST | 540 | 5.8% |
| LOAD_FAST_LOAD_FAST | 460 | 4.9% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,240 | 77.7% |
| LOAD_ATTR_INSTANCE_VALUE | 14,968 | 12.3% |
| LOAD_ATTR | 11,960 | 9.9% |
| BINARY_OP | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,160 | 58.7% |
| LOAD_GLOBAL_MODULE | 35,080 | 28.9% |
| STORE_FAST | 14,988 | 12.4% |
| LOAD_GLOBAL | 60 | 0.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 683,054 | 62.6% |
| LOAD_FAST_LOAD_FAST | 263,840 | 24.2% |
| CALL_LEN | 83,960 | 7.7% |
| LOAD_CONST | 60,060 | 5.5% |
| BINARY_OP | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 574,394 | 52.6% |
| BINARY_SLICE | 311,940 | 28.6% |
| RETURN_VALUE | 71,980 | 6.6% |
| CALL_PY_EXACT_ARGS | 71,960 | 6.6% |
| STORE_FAST | 60,440 | 5.5% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 119,920 | 52.4% |
| RETURN_VALUE | 107,960 | 47.2% |
| LOAD_FAST_LOAD_FAST | 480 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.1% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 107,980 | 47.2% |
| LOAD_GLOBAL_MODULE | 107,960 | 47.2% |
| STORE_FAST | 12,280 | 5.4% |
| CALL | 240 | 0.1% |
| LOAD_FAST | 240 | 0.1% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 11,960 | 99.4% |
| BINARY_OP | 40 | 0.3% |
| LOAD_CONST | 34 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,980 | 99.6% |
| CALL_BUILTIN_O | 34 | 0.3% |
| CALL | 20 | 0.2% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,960 | 99.0% |
| BINARY_SUBSCR_TUPLE_INT | 100 | 0.8% |
| BINARY_OP | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 11,960 | 99.0% |
| BINARY_OP_ADD_INT | 100 | 0.8% |
| COMPARE_OP | 20 | 0.2% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 59,194 | 70.5% |
| LOAD_ATTR_INSTANCE_VALUE | 11,960 | 14.2% |
| LOAD_ATTR_WITH_HINT | 11,960 | 14.2% |
| CALL | 746 | 0.9% |
| BINARY_OP | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 59,160 | 70.4% |
| RETURN_VALUE | 11,980 | 14.3% |
| LOAD_FAST | 11,980 | 14.3% |
| STORE_FAST | 820 | 1.0% |
| LOAD_DEREF | 60 | 0.1% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 563,920 | 65.1% |
| LOAD_ATTR_INSTANCE_VALUE | 95,920 | 11.1% |
| BINARY_OP_SUBTRACT_INT | 83,960 | 9.7% |
| LOAD_CONST | 62,077 | 7.2% |
| CALL_LEN | 60,080 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 361,997 | 41.8% |
| STORE_FAST | 324,000 | 37.4% |
| LOAD_FAST | 84,040 | 9.7% |
| BINARY_OP_SUBTRACT_INT | 83,960 | 9.7% |
| BINARY_SUBSCR_LIST_INT | 11,960 | 1.4% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 420,140 | 46.4% |
| LOAD_FAST | 350,618 | 38.8% |
| BUILD_TUPLE | 48,080 | 5.3% |
| LOAD_FAST_LOAD_FAST | 36,020 | 4.0% |
| RETURN_VALUE | 23,980 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 432,040 | 47.8% |
| PUSH_EXC_INFO | 346,980 | 38.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 38,238 | 4.2% |
| LOAD_FAST_LOAD_FAST | 35,980 | 4.0% |
| STORE_FAST | 24,340 | 2.7% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 300,020 | 71.3% |
| LOAD_FAST | 120,260 | 28.6% |
| LOAD_CONST | 240 | 0.1% |
| BINARY_SUBSCR | 20 | 0.0% |
| BINARY_SUBSCR_GETITEM | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 418,900 | 99.6% |
| PUSH_EXC_INFO | 1,480 | 0.4% |
| RETURN_VALUE | 160 | 0.0% |
| BINARY_SUBSCR_GETITEM | 20 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 82,791 | 76.9% |
| BINARY_SUBSCR | 12,300 | 11.4% |
| BINARY_OP_SUBTRACT_INT | 11,960 | 11.1% |
| LOAD_FAST | 580 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 41,125 | 38.2% |
| LOAD_FAST | 24,240 | 22.5% |
| STORE_FAST | 14,828 | 13.8% |
| TO_BOOL_BOOL | 14,238 | 13.2% |
| LOAD_CONST | 11,980 | 11.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,420 | 99.6% |
| LOAD_FAST | 380 | 0.3% |
| BINARY_SUBSCR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 108,040 | 99.2% |
| LOAD_CONST | 340 | 0.3% |
| STORE_FAST | 280 | 0.3% |
| PUSH_EXC_INFO | 60 | 0.1% |
| LOAD_ATTR | 60 | 0.1% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 229,020 | 99.9% |
| BINARY_SUBSCR | 260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 120,040 | 52.4% |
| LOAD_GLOBAL_MODULE | 24,240 | 10.6% |
| LOAD_GLOBAL_BUILTIN | 24,040 | 10.5% |
| LOAD_FAST | 24,020 | 10.5% |
| STORE_FAST | 12,280 | 5.4% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 132,000 | 40.7% |
| LOAD_ATTR_INSTANCE_VALUE | 95,720 | 29.5% |
| LOAD_FAST_LOAD_FAST | 36,160 | 11.1% |
| LOAD_FAST | 36,140 | 11.1% |
| PUSH_NULL | 11,960 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 324,520 | 100.0% |
| COPY_FREE_VARS | 120 | 0.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,380 | 36.9% |
| LOAD_FAST | 85,133 | 29.0% |
| LOAD_FAST_LOAD_FAST | 48,162 | 16.4% |
| BINARY_SLICE | 23,960 | 8.2% |
| CALL_BUILTIN_CLASS | 23,960 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 156,712 | 53.3% |
| POP_TOP | 108,260 | 36.8% |
| COPY_FREE_VARS | 26,098 | 8.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,080 | 0.7% |
| CALL_PY_EXACT_ARGS | 496 | 0.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,960 | 29.2% |
| LOAD_FAST | 39,228 | 15.9% |
| CALL | 36,480 | 14.8% |
| LOAD_ATTR_INSTANCE_VALUE | 36,160 | 14.7% |
| LOAD_GLOBAL_MODULE | 14,238 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,500 | 39.2% |
| LOAD_FAST | 36,200 | 14.7% |
| RETURN_VALUE | 35,980 | 14.6% |
| GET_ITER | 29,366 | 11.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,960 | 9.7% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 838,040 | 49.2% |
| LOAD_FAST_LOAD_FAST | 455,520 | 26.7% |
| LOAD_CONST | 337,280 | 19.8% |
| LOAD_GLOBAL_MODULE | 35,920 | 2.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,960 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 814,860 | 48.2% |
| RETURN_VALUE | 454,780 | 26.9% |
| TO_BOOL_BOOL | 132,780 | 7.9% |
| COPY | 107,980 | 6.4% |
| POP_TOP | 59,900 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 191,920 | 58.6% |
| BINARY_OP_SUBTRACT_FLOAT | 59,160 | 18.1% |
| LOAD_ATTR | 38,506 | 11.8% |
| BINARY_OP | 23,960 | 7.3% |
| LOAD_FAST | 12,700 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 144,660 | 44.2% |
| LOAD_FAST | 83,160 | 25.4% |
| LOAD_CONST | 59,980 | 18.3% |
| COPY | 23,160 | 7.1% |
| POP_TOP | 15,426 | 4.7% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 49,040 | 63.4% |
| LOAD_ATTR_INSTANCE_VALUE | 26,843 | 34.7% |
| BUILD_TUPLE | 360 | 0.5% |
| CALL | 220 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 180 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 38,843 | 50.3% |
| STORE_SUBSCR_DICT | 23,920 | 30.9% |
| BINARY_SUBSCR_DICT | 11,960 | 15.5% |
| POP_TOP | 1,640 | 2.1% |
| RETURN_VALUE | 440 | 0.6% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,180,171 | 52.9% |
| LOAD_GLOBAL_BUILTIN | 484,860 | 21.7% |
| LOAD_ATTR_MODULE | 298,800 | 13.4% |
| BUILD_TUPLE | 204,940 | 9.2% |
| LOAD_ATTR | 59,960 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,024,591 | 90.8% |
| RETURN_VALUE | 144,240 | 6.5% |
| COPY | 35,980 | 1.6% |
| STORE_FAST | 24,060 | 1.1% |
| TO_BOOL | 980 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 673,680 | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE | 402,750 | 36.6% |
| LOAD_GLOBAL_MODULE | 12,080 | 1.1% |
| BINARY_SUBSCR | 12,060 | 1.1% |
| CALL | 640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 378,882 | 34.4% |
| LOAD_FAST | 226,320 | 20.5% |
| LOAD_CONST | 97,380 | 8.8% |
| BINARY_OP_ADD_INT | 83,960 | 7.6% |
| BINARY_OP_SUBTRACT_INT | 60,080 | 5.5% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 158,657 | 61.1% |
| BUILD_TUPLE | 76,526 | 29.5% |
| RETURN_VALUE | 24,040 | 9.3% |
| CALL | 300 | 0.1% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120,260 | 46.3% |
| JUMP_BACKWARD | 103,342 | 39.8% |
| LOAD_FAST | 24,120 | 9.3% |
| NOP | 12,021 | 4.6% |
| EXTENDED_ARG | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 634,620 | 64.1% |
| LOAD_ATTR_METHOD_NO_DICT | 204,040 | 20.6% |
| LOAD_FAST_LOAD_FAST | 72,200 | 7.3% |
| LOAD_FAST | 52,826 | 5.3% |
| RETURN_VALUE | 24,040 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 622,560 | 62.9% |
| STORE_FAST | 125,146 | 12.6% |
| CALL_PY_EXACT_ARGS | 108,040 | 10.9% |
| LOAD_CONST | 71,980 | 7.3% |
| LOAD_FAST | 24,060 | 2.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 384,520 | 54.0% |
| LOAD_ATTR_METHOD_NO_DICT | 227,960 | 32.0% |
| LOAD_FAST | 59,980 | 8.4% |
| LOAD_ATTR | 24,040 | 3.4% |
| LOAD_FAST_LOAD_FAST | 14,968 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 267,568 | 37.6% |
| UNPACK_SEQUENCE_LIST | 119,920 | 16.8% |
| YIELD_VALUE | 107,980 | 15.2% |
| POP_TOP | 84,100 | 11.8% |
| RETURN_VALUE | 84,000 | 11.8% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,020,096 | 49.3% |
| LOAD_ATTR | 1,007,440 | 48.7% |
| LOAD_FAST | 24,040 | 1.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 11,960 | 0.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,321 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 984,100 | 47.6% |
| STORE_FAST | 488,232 | 23.6% |
| POP_TOP | 228,986 | 11.1% |
| GET_ITER | 144,140 | 7.0% |
| LOAD_FAST | 72,200 | 3.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 561,844 | 53.8% |
| BUILD_TUPLE | 191,840 | 18.4% |
| LOAD_ATTR_INSTANCE_VALUE | 84,120 | 8.1% |
| LOAD_FAST_CHECK | 71,960 | 6.9% |
| LOAD_CONST | 48,400 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 814,604 | 78.0% |
| STORE_FAST | 144,020 | 13.8% |
| LOAD_CONST | 24,300 | 2.3% |
| UNPACK_SEQUENCE_TUPLE | 24,080 | 2.3% |
| PUSH_EXC_INFO | 24,060 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 4,495,042 | 39.0% |
| LOAD_FAST | 3,456,227 | 30.0% |
| LOAD_FAST_LOAD_FAST | 661,476 | 5.7% |
| LOAD_CONST | 659,820 | 5.7% |
| LOAD_ATTR_METHOD_NO_DICT | 513,690 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,813,040 | 93.7% |
| COPY_FREE_VARS | 288,640 | 2.5% |
| RETURN_GENERATOR | 264,140 | 2.3% |
| MAKE_CELL | 160,006 | 1.4% |
| TO_BOOL_BOOL | 11,585 | 0.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,100 | 31.5% |
| LOAD_CONST | 143,680 | 22.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 131,134 | 20.2% |
| PUSH_NULL | 72,040 | 11.1% |
| LOAD_ATTR | 35,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 635,834 | 98.1% |
| RETURN_GENERATOR | 11,980 | 1.8% |
| MAKE_CELL | 60 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 340 | 94.4% |
| CALL | 20 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 280 | 77.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 80 | 22.2% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 700 | 48.6% |
| LOAD_FAST | 540 | 37.5% |
| RETURN_VALUE | 120 | 8.3% |
| LOAD_GLOBAL_MODULE | 80 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 480 | 33.3% |
| LOAD_FAST | 480 | 33.3% |
| STORE_FAST | 340 | 23.6% |
| CALL | 80 | 5.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 4.2% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,940 | 99.8% |
| LOAD_CONST | 200 | 0.1% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 108,300 | 52.8% |
| LOAD_FAST_LOAD_FAST | 48,140 | 23.5% |
| LOAD_GLOBAL_MODULE | 35,960 | 17.5% |
| STORE_FAST | 11,980 | 5.8% |
| LOAD_GLOBAL_BUILTIN | 660 | 0.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 333,105 | 93.4% |
| LOAD_FAST | 14,648 | 4.1% |
| LOAD_GLOBAL_MODULE | 8,901 | 2.5% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 333,125 | 93.4% |
| POP_JUMP_IF_FALSE | 23,669 | 6.6% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,733,394 | 49.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,030,586 | 29.2% |
| LOAD_ATTR_CLASS | 383,960 | 10.9% |
| COPY | 132,120 | 3.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 119,920 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,792,628 | 79.2% |
| POP_JUMP_IF_TRUE | 708,520 | 20.1% |
| COPY | 24,000 | 0.7% |
| RETURN_VALUE | 100 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 229,360 | 82.5% |
| LOAD_GLOBAL_MODULE | 47,840 | 17.2% |
| COMPARE_OP | 460 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 340 | 0.1% |
| LOAD_FAST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 217,960 | 78.4% |
| COPY | 23,960 | 8.6% |
| EXTENDED_ARG | 12,180 | 4.4% |
| POP_JUMP_IF_TRUE | 12,020 | 4.3% |
| RETURN_VALUE | 11,980 | 4.3% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 215,960 | 78.3% |
| LOAD_FAST | 47,960 | 17.4% |
| GET_ITER | 11,960 | 4.3% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 215,960 | 78.3% |
| POP_TOP | 59,940 | 21.7% |
| RESUME | 40 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 658,346 | 61.2% |
| GET_ITER | 403,136 | 37.5% |
| SWAP | 12,460 | 1.2% |
| FOR_ITER | 780 | 0.1% |
| EXTENDED_ARG | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 588,633 | 54.7% |
| LOAD_FAST | 195,228 | 18.2% |
| JUMP_BACKWARD | 108,200 | 10.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 93,772 | 8.7% |
| RETURN_CONST | 27,289 | 2.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 464,532 | 94.0% |
| GET_ITER | 29,366 | 5.9% |
| FOR_ITER | 100 | 0.0% |
| SWAP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 454,910 | 92.1% |
| LOAD_CONST | 15,008 | 3.0% |
| RETURN_CONST | 12,000 | 2.4% |
| STORE_FAST_LOAD_FAST | 11,980 | 2.4% |
| LOAD_FAST | 80 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 73,020 | 48.6% |
| JUMP_BACKWARD | 64,120 | 42.6% |
| SWAP | 12,460 | 8.3% |
| LOAD_FAST | 700 | 0.5% |
| FOR_ITER | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,900 | 41.8% |
| LOAD_FAST | 60,220 | 40.0% |
| SWAP | 12,480 | 8.3% |
| LOAD_CONST | 12,000 | 8.0% |
| STORE_FAST_LOAD_FAST | 1,160 | 0.8% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 455,800 | 62.2% |
| LOAD_GLOBAL_MODULE | 228,420 | 31.2% |
| LOAD_FAST | 48,600 | 6.6% |
| LOAD_ATTR | 400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 383,960 | 52.4% |
| LOAD_FAST | 144,440 | 19.7% |
| BINARY_OP | 96,080 | 13.1% |
| CALL | 48,060 | 6.6% |
| RETURN_VALUE | 24,200 | 3.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,277,070 | 87.0% |
| LOAD_FAST_LOAD_FAST | 1,357,406 | 5.1% |
| COPY | 960,111 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 791,180 | 3.0% |
| LOAD_DEREF | 369,678 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,177,319 | 15.6% |
| POP_JUMP_IF_NONE | 3,035,562 | 11.3% |
| LOAD_ATTR_METHOD_NO_DICT | 2,762,339 | 10.3% |
| RETURN_VALUE | 2,703,306 | 10.1% |
| TO_BOOL_BOOL | 2,661,778 | 9.9% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,920 | 99.8% |
| LOAD_ATTR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,980 | 50.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,960 | 49.9% |
| CALL | 20 | 0.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,762,339 | 50.9% |
| LOAD_FAST | 1,758,144 | 32.4% |
| BINARY_SLICE | 251,960 | 4.6% |
| LOAD_CONST | 132,180 | 2.4% |
| STORE_FAST_LOAD_FAST | 108,640 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,926,867 | 35.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,020,096 | 18.8% |
| LOAD_CONST | 971,488 | 17.9% |
| CALL_PY_EXACT_ARGS | 513,690 | 9.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 227,960 | 4.2% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,139,176 | 67.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,886,250 | 20.8% |
| LOAD_ATTR_SLOT | 589,386 | 6.5% |
| LOAD_DEREF | 123,426 | 1.4% |
| LOAD_FAST_LOAD_FAST | 107,160 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,495,042 | 49.6% |
| LOAD_FAST | 2,916,942 | 32.2% |
| LOAD_FAST_LOAD_FAST | 675,586 | 7.5% |
| LOAD_CONST | 491,660 | 5.4% |
| LOAD_GLOBAL_MODULE | 158,506 | 1.7% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,127,217 | 99.5% |
| LOAD_ATTR_MODULE | 11,960 | 0.4% |
| LOAD_ATTR | 2,940 | 0.1% |
| LOAD_FAST | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,701,831 | 54.2% |
| LOAD_ATTR_CLASS | 455,800 | 14.5% |
| CALL_ISINSTANCE | 298,800 | 9.5% |
| LOAD_GLOBAL_MODULE | 143,800 | 4.6% |
| LOAD_ATTR | 132,240 | 4.2% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 215,720 | 56.2% |
| LOAD_FAST_LOAD_FAST | 84,020 | 21.9% |
| LOAD_FAST | 71,960 | 18.7% |
| LOAD_DEREF | 11,960 | 3.1% |
| LOAD_ATTR | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 155,880 | 40.6% |
| COMPARE_OP_INT | 119,920 | 31.2% |
| LOAD_FAST | 36,060 | 9.4% |
| STORE_FAST | 35,980 | 9.4% |
| CONTAINS_OP | 23,960 | 6.2% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 72,000 | 59.7% |
| LOAD_FAST | 48,260 | 40.0% |
| LOAD_ATTR | 220 | 0.2% |
| RETURN_VALUE | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 83,920 | 69.6% |
| RESUME_CHECK | 36,640 | 30.4% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,146,209 | 95.8% |
| BINARY_SUBSCR_TUPLE_INT | 120,040 | 2.8% |
| BINARY_SUBSCR_LIST_INT | 41,125 | 1.0% |
| LOAD_DEREF | 11,960 | 0.3% |
| LOAD_ATTR_SLOT | 5,556 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 856,812 | 19.8% |
| TO_BOOL_BOOL | 774,588 | 17.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 589,386 | 13.6% |
| LOAD_ATTR | 380,372 | 8.8% |
| BUILD_LIST | 380,312 | 8.8% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 763,671 | 99.9% |
| LOAD_ATTR | 660 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 303 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 335,900 | 43.9% |
| LOAD_CONST | 95,960 | 12.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,758 | 10.8% |
| LOAD_ATTR_METHOD_NO_DICT | 59,960 | 7.8% |
| RETURN_VALUE | 35,980 | 4.7% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,841,237 | 38.4% |
| LOAD_FAST | 892,920 | 12.1% |
| POP_JUMP_IF_FALSE | 688,568 | 9.3% |
| STORE_FAST | 523,668 | 7.1% |
| POP_JUMP_IF_TRUE | 497,160 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,445,263 | 73.5% |
| CALL_ISINSTANCE | 484,860 | 6.5% |
| LOAD_DEREF | 401,806 | 5.4% |
| CHECK_EXC_MATCH | 391,454 | 5.3% |
| BUILD_TUPLE | 204,400 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,312,477 | 21.0% |
| RESUME_CHECK | 1,967,088 | 17.9% |
| POP_JUMP_IF_FALSE | 1,055,214 | 9.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,043,920 | 9.5% |
| STORE_ATTR_INSTANCE_VALUE | 806,983 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 3,127,217 | 28.4% |
| LOAD_FAST | 2,337,360 | 21.3% |
| CALL_ISINSTANCE | 1,180,171 | 10.7% |
| LOAD_FAST_LOAD_FAST | 1,093,640 | 9.9% |
| CALL | 568,778 | 5.2% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 119,880 | 99.9% |
| LOAD_SUPER_ATTR | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 83,920 | 69.9% |
| PUSH_NULL | 36,020 | 30.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 182,040 | 93.7% |
| LOAD_DEREF | 11,960 | 6.2% |
| LOAD_SUPER_ATTR | 280 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 86,000 | 44.3% |
| CALL_PY_EXACT_ARGS | 59,200 | 30.5% |
| LOAD_FAST | 25,080 | 12.9% |
| CALL | 12,020 | 6.2% |
| LOAD_CONST | 11,980 | 6.2% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,813,040 | 53.7% |
| CACHE | 5,394,197 | 26.8% |
| COPY_FREE_VARS | 733,290 | 3.6% |
| CALL_PY_WITH_DEFAULTS | 635,834 | 3.2% |
| BINARY_SUBSCR_GETITEM | 418,900 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,475,162 | 57.0% |
| LOAD_GLOBAL_BUILTIN | 2,841,237 | 14.1% |
| LOAD_GLOBAL_MODULE | 1,967,088 | 9.8% |
| NOP | 1,613,246 | 8.0% |
| LOAD_CONST | 652,466 | 3.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 179,600 | 62.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 108,000 | 37.5% |
| SEND | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 179,800 | 62.5% |
| RESUME_CHECK | 107,820 | 37.5% |
| RESUME | 180 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,000,055 | 60.9% |
| LOAD_FAST_LOAD_FAST | 1,992,740 | 24.3% |
| SWAP | 960,111 | 11.7% |
| LOAD_DEREF | 155,680 | 1.9% |
| STORE_FAST_LOAD_FAST | 83,920 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,820,654 | 34.3% |
| LOAD_CONST | 1,680,134 | 20.5% |
| LOAD_FAST_LOAD_FAST | 997,420 | 12.1% |
| LOAD_GLOBAL_MODULE | 806,983 | 9.8% |
| RETURN_CONST | 761,188 | 9.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,840,438 | 50.4% |
| LOAD_FAST_LOAD_FAST | 1,799,484 | 49.3% |
| STORE_ATTR_SLOT | 13,189 | 0.4% |
| STORE_ATTR | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,305,258 | 35.7% |
| LOAD_CONST | 1,048,672 | 28.7% |
| LOAD_FAST | 640,449 | 17.5% |
| RETURN_CONST | 613,606 | 16.8% |
| JUMP_BACKWARD | 32,297 | 0.9% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,877 | 79.4% |
| LOAD_FAST_LOAD_FAST | 11,960 | 20.3% |
| STORE_ATTR_INSTANCE_VALUE | 101 | 0.2% |
| STORE_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,920 | 81.2% |
| RETURN_CONST | 10,998 | 18.6% |
| STORE_ATTR_INSTANCE_VALUE | 100 | 0.2% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 492,240 | 87.1% |
| LOAD_ATTR | 48,020 | 8.5% |
| CALL_BUILTIN_O | 23,920 | 4.2% |
| STORE_SUBSCR | 340 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 312,260 | 55.3% |
| RETURN_CONST | 216,200 | 38.3% |
| LOAD_GLOBAL_MODULE | 24,200 | 4.3% |
| POP_EXCEPT | 12,000 | 2.1% |
| LOAD_CONST | 140 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 120 | 50.0% |
| LOAD_CONST | 80 | 33.3% |
| STORE_SUBSCR | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 50.0% |
| EXTENDED_ARG | 60 | 25.0% |
| JUMP_FORWARD | 60 | 25.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,160 | 75.0% |
| CALL | 11,960 | 24.8% |
| TO_BOOL | 120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,260 | 50.3% |
| POP_JUMP_IF_TRUE | 23,980 | 49.7% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,661,778 | 27.1% |
| CALL_ISINSTANCE | 2,024,591 | 20.6% |
| RETURN_VALUE | 1,899,346 | 19.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 984,100 | 10.0% |
| LOAD_ATTR_SLOT | 774,588 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,370,609 | 74.9% |
| POP_JUMP_IF_TRUE | 2,334,030 | 23.7% |
| EXTENDED_ARG | 119,920 | 1.2% |
| UNARY_NOT | 11,980 | 0.1% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 408,340 | 43.1% |
| BINARY_OP | 321,972 | 34.0% |
| COPY | 205,107 | 21.6% |
| LOAD_ATTR | 11,960 | 1.3% |
| TO_BOOL | 600 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 603,178 | 63.6% |
| POP_JUMP_IF_TRUE | 345,016 | 36.4% |
| TO_BOOL_NONE | 105 | 0.0% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 164,793 | 99.1% |
| LOAD_FAST | 720 | 0.4% |
| STORE_FAST_LOAD_FAST | 560 | 0.3% |
| TO_BOOL | 200 | 0.1% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 165,273 | 99.4% |
| POP_JUMP_IF_TRUE | 960 | 0.6% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 856,812 | 56.1% |
| LOAD_FAST | 262,430 | 17.2% |
| COPY | 190,713 | 12.5% |
| LOAD_ATTR | 83,800 | 5.5% |
| LOAD_ATTR_INSTANCE_VALUE | 72,040 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,288,123 | 84.3% |
| POP_JUMP_IF_TRUE | 239,158 | 15.7% |
| TO_BOOL | 200 | 0.0% |
| TO_BOOL_STR | 180 | 0.0% |
| TO_BOOL_INT | 100 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 229,060 | 78.8% |
| COPY | 36,180 | 12.4% |
| LOAD_ATTR | 11,960 | 4.1% |
| CALL_BUILTIN_FAST | 11,880 | 4.1% |
| STORE_FAST_LOAD_FAST | 1,160 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 241,840 | 83.2% |
| POP_JUMP_IF_FALSE | 48,700 | 16.8% |
| TO_BOOL_NONE | 180 | 0.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 119,920 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 119,960 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 24,080 | 28.6% |
| LOAD_FAST | 12,080 | 14.3% |
| END_SEND | 11,960 | 14.2% |
| BINARY_SUBSCR_DICT | 11,960 | 14.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,960 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 72,300 | 85.8% |
| LOAD_FAST | 11,980 | 14.2% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 263,880 | 29.1% |
| RETURN_VALUE | 156,480 | 17.3% |
| FOR_ITER | 108,280 | 11.9% |
| YIELD_VALUE | 107,960 | 11.9% |
| FOR_ITER_LIST | 93,772 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 893,696 | 98.6% |
| LOAD_FAST | 12,040 | 1.3% |
| STORE_FAST | 340 | 0.0% |
| STORE_DEREF | 60 | 0.0% |


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
|     deferred | 1,194,137 | 33.0% |
|          hit | 2,415,853 | 66.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 960 | 10.8% |
| Failure | 7,911 | 89.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,585 | 45.3% |
| add other | 1,420 | 17.9% |
| or | 1,265 | 16.0% |
| remainder | 880 | 11.1% |
| add different types | 418 | 5.3% |
| floor divide | 180 | 2.3% |
| true divide other | 140 | 1.8% |
| multiply different types | 23 | 0.3% |


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
|     deferred | 424,420 | 19.3% |
|          hit | 1,769,109 | 80.5% |
|         miss | 1,780 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,000 | 26.5% |
| Failure | 2,780 | 73.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 2,460 | 88.5% |
| other | 160 | 5.8% |
| out of range | 160 | 5.8% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,242,173 | 20.9% |
|          hit | 23,581,033 | 78.9% |
|         miss | 371,346 | 1.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,806 | 43.2% |
| Failure | 30,031 | 56.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 6,340 | 21.1% |
| class no vectorcall | 5,500 | 18.3% |
| meth descr method fastcall keywords | 3,860 | 12.9% |
| cfunc noargs | 3,137 | 10.4% |
| meth descr varargs | 2,852 | 9.5% |
| other | 1,760 | 5.9% |
| class mutable | 1,240 | 4.1% |
| meth descr varargs keywords | 1,122 | 3.7% |
| cfunc varargs keywords | 1,120 | 3.7% |
| metaclass | 880 | 2.9% |
| no dict | 820 | 2.7% |
| cfunc varargs | 520 | 1.7% |
| operator wrapper | 500 | 1.7% |
| wrong number arguments | 180 | 0.6% |
| cmethod | 160 | 0.5% |
| init not python | 20 | 0.1% |
| init not simple | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 172,568 | 4.0% |
|          hit | 4,160,008 | 95.9% |
|         miss | 214 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,960 | 52.9% |
| Failure | 1,744 | 47.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 480 | 27.5% |
| bytes | 360 | 20.6% |
| other | 340 | 19.5% |
| tuple | 180 | 10.3% |
| big int | 160 | 9.2% |
| float long | 124 | 7.1% |
| baseobject | 60 | 3.4% |
| bool | 40 | 2.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 354,600 | 15.1% |
|          hit | 1,995,680 | 84.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,020 | 30.4% |
| Failure | 2,340 | 69.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 1,360 | 58.1% |
| set | 240 | 10.3% |
| dict keys | 240 | 10.3% |
| other | 180 | 7.7% |
| bytes | 160 | 6.8% |
| ascii string | 120 | 5.1% |
| enumerate | 40 | 1.7% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,522,865 | 11.5% |
|          hit | 50,297,927 | 88.4% |
|         miss | 465,098 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 37,601 | 49.9% |
| Failure | 37,761 | 50.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 8,260 | 21.9% |
| method | 8,200 | 21.7% |
| not managed dict | 7,175 | 19.0% |
| not in keys | 6,880 | 18.2% |
| shadowed | 1,726 | 4.6% |
| module attr not found | 1,600 | 4.2% |
| non overriding descriptor | 1,220 | 3.2% |
| metaclass attribute | 920 | 2.4% |
| class attr descriptor | 540 | 1.4% |
| class method obj | 480 | 1.3% |
| non object slot | 380 | 1.0% |
| overridden | 180 | 0.5% |
| builtin class method | 160 | 0.4% |
| mutable class | 40 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20,760 | 0.1% |
|        deopt | 920 | 0.0% |
|          hit | 18,393,892 | 99.8% |
|         miss | 6,280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 14,220 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 500 | 0.2% |
|          hit | 314,260 | 99.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
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
|     deferred | 336,200 | 53.7% |
|          hit | 287,800 | 46.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 9.9% |
| Failure | 1,820 | 90.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,820 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 979,800 | 8.0% |
|          hit | 11,208,485 | 91.8% |
|         miss | 716,250 | 5.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 21,450 | 83.6% |
| Failure | 4,200 | 16.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 1,660 | 39.5% |
| not in keys | 680 | 16.2% |
| method | 480 | 11.4% |
| property | 480 | 11.4% |
| not in dict | 480 | 11.4% |
| not managed dict | 240 | 5.7% |
| overridden | 180 | 4.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240,780 | 29.8% |
|          hit | 565,320 | 69.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 17.8% |
| Failure | 1,760 | 82.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 1,440 | 81.8% |
| dict subclass no override | 320 | 18.2% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,415,445 | 10.0% |
|          hit | 12,776,219 | 89.9% |
|         miss | 41,693 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,046 | 56.5% |
| Failure | 6,183 | 43.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 1,940 | 31.4% |
| bytes | 1,138 | 18.4% |
| float | 960 | 15.5% |
| dict | 620 | 10.0% |
| mapping | 565 | 9.1% |
| bytearray | 420 | 6.8% |
| tuple | 360 | 5.8% |
| set | 180 | 2.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,920 | 1.1% |
|          hit | 1,110,376 | 98.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 880 | 84.6% |
| Failure | 160 | 15.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 160 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 188,366,849 | 49.2% |
| Not specialized | 44,058,713 | 11.5% |
| Specialized hits | 148,836,742 | 38.9% |
| Specialized misses | 1,603,675 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 6,522,865 | 36.4% |
| CALL | 6,242,173 | 34.8% |
| TO_BOOL | 1,415,445 | 7.9% |
| BINARY_OP | 1,194,137 | 6.7% |
| STORE_ATTR | 979,800 | 5.5% |
| BINARY_SUBSCR | 424,420 | 2.4% |
| FOR_ITER | 354,600 | 2.0% |
| SEND | 336,200 | 1.9% |
| STORE_SUBSCR | 240,780 | 1.3% |
| COMPARE_OP | 172,568 | 1.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 704,627 | 43.9% |
| LOAD_ATTR_SLOT | 296,949 | 18.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 136,724 | 8.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 125,059 | 7.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,432 | 5.1% |
| CALL_PY_EXACT_ARGS | 72,483 | 4.5% |
| LOAD_ATTR_METHOD_NO_DICT | 37,588 | 2.3% |
| CALL_METHOD_DESCRIPTOR_O | 36,840 | 2.3% |
| TO_BOOL_NONE | 25,578 | 1.6% |
| LOAD_ATTR_INSTANCE_VALUE | 19,489 | 1.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 5,756,649 | 28.1% |
| Calls to Python functions inlined | 14,732,736 | 71.9% |
| Calls via PyEval_EvalFrame (total) | 5,756,649 | 28.1% |
| Calls via PyEval_EvalFrame (vector) | 5,406,069 | 26.4% |
| Calls via PyEval_EvalFrame (generator) | 350,580 | 1.7% |
| Calls via PyEval_EvalFrame (legacy) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 5,405,769 | 26.4% |
| Calls via PyEval_EvalFrame (build class) | 220 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,097,285 | 5.4% |
| Calls via PyEval_EvalFrame (function ex) | 132,520 | 0.6% |
| Calls via PyEval_EvalFrame (api) | 206,300 | 1.0% |
| Calls via PyEval_EvalFrame (method) | 915,986 | 4.5% |
| Frame objects created | 752,664 | 3.7% |
| Frames pushed | 13,459,993 | 65.7% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 11,581,884 | 40.2% |
| Frees to freelist | 11,635,200 |  |
| Allocations | 17,264,445 | 59.8% |
| Allocations to 512 bytes | 16,940,248 | 58.7% |
| Allocations to 4 kbytes | 90,689 | 0.3% |
| Allocations over 4 kbytes | 233,508 | 0.8% |
| Frees | 17,522,951 |  |
| New values | 158,420 |  |
| Interpreter increfs | 185,751,040 | 77.4% |
| Interpreter decrefs | 201,382,618 | 75.4% |
| Increfs | 54,168,653 | 22.6% |
| Decrefs | 65,594,856 | 24.6% |
| Materialize dict (on request) | 200 | 0.1% |
| Materialize dict (new key) | 24,000 | 15.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 140 | 0.1% |
| Method cache hits | 10,396,367 |  |
| Method cache misses | 318,801 |  |
| Method cache collisions | 345,648 |  |
| Method cache dunder hits | 6,887,891 |  |
| Method cache dunder misses | 32,233 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 915 | 1,920 | 10,114,500 |
| 1 | 86 | 110 | 2,887,922 |
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
