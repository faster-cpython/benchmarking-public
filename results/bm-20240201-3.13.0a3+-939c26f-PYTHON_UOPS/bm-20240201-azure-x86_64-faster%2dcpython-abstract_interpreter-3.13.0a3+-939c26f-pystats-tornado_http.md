
# Pystats results

- benchmark: tornado_http
- fork: faster-cpython
- ref: abstract-interpreter-generator
- commit hash: 939c26f
- commit date: 2024-02-01T15:28:16+00:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 74,226,711 | 20.7% | 20.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 25,228,632 | 7.0% | 27.8% | 0.1% |
| RESUME_CHECK | 19,629,895 | 5.5% | 33.3% | 0.0% |
| LOAD_CONST | 16,010,577 | 4.5% | 37.7% |  |
| POP_JUMP_IF_FALSE | 14,037,886 | 3.9% | 41.6% |  |
| RETURN_VALUE | 11,658,557 | 3.3% | 44.9% |  |
| CALL_PY_EXACT_ARGS | 10,900,046 | 3.0% | 47.9% | 0.6% |
| STORE_FAST | 10,743,373 | 3.0% | 50.9% |  |
| LOAD_GLOBAL_MODULE | 10,554,969 | 2.9% | 53.9% | 0.0% |
| POP_TOP | 10,179,918 | 2.8% | 56.7% |  |
| LOAD_FAST_LOAD_FAST | 10,131,433 | 2.8% | 59.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,867,593 | 2.5% | 62.0% | 0.9% |
| TO_BOOL_BOOL | 8,745,624 | 2.4% | 64.5% | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 8,132,010 | 2.3% | 66.8% | 0.1% |
| RETURN_CONST | 7,905,104 | 2.2% | 69.0% |  |
| LOAD_GLOBAL_BUILTIN | 6,960,027 | 1.9% | 70.9% | 0.1% |
| CALL | 5,928,736 | 1.7% | 72.6% |  |
| INTERPRETER_EXIT | 5,736,099 | 1.6% | 74.2% |  |
| LOAD_ATTR | 5,583,637 | 1.6% | 75.7% |  |
| POP_JUMP_IF_NONE | 5,416,852 | 1.5% | 77.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 4,317,694 | 1.2% | 78.4% | 0.8% |
| POP_JUMP_IF_TRUE | 4,075,584 | 1.1% | 79.6% |  |
| STORE_ATTR_SLOT | 3,608,413 | 1.0% | 80.6% | 19.1% |
| COMPARE_OP_INT | 3,395,706 | 0.9% | 81.5% | 0.0% |
| PUSH_NULL | 3,228,321 | 0.9% | 82.4% |  |
| LOAD_ATTR_MODULE | 3,088,885 | 0.9% | 83.3% | 0.0% |
| NOP | 2,977,982 | 0.8% | 84.1% |  |
| LOAD_ATTR_SLOT | 2,761,517 | 0.8% | 84.9% | 10.7% |
| COPY | 2,411,523 | 0.7% | 85.6% |  |
| LOAD_DEREF | 2,095,095 | 0.6% | 86.2% |  |
| CALL_ISINSTANCE | 2,083,846 | 0.6% | 86.7% |  |
| CALL_BUILTIN_FAST | 1,654,780 | 0.5% | 87.2% |  |
| POP_JUMP_IF_NOT_NONE | 1,650,276 | 0.5% | 87.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,506,083 | 0.4% | 88.1% | 8.3% |
| TO_BOOL_NONE | 1,491,855 | 0.4% | 88.5% | 1.5% |
| SWAP | 1,468,699 | 0.4% | 88.9% |  |
| ENTER_EXECUTOR | 1,355,234 | 0.4% | 89.3% |  |
| BUILD_TUPLE | 1,300,179 | 0.4% | 89.7% |  |
| TO_BOOL | 1,272,418 | 0.4% | 90.0% |  |
| BINARY_OP | 1,109,539 | 0.3% | 90.3% |  |
| BINARY_OP_ADD_INT | 1,090,049 | 0.3% | 90.6% |  |
| CALL_FUNCTION_EX | 1,086,671 | 0.3% | 90.9% |  |
| CALL_LEN | 994,767 | 0.3% | 91.2% |  |
| CALL_METHOD_DESCRIPTOR_O | 989,175 | 0.3% | 91.5% | 3.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 958,343 | 0.3% | 91.8% |  |
| STORE_FAST_STORE_FAST | 887,207 | 0.2% | 92.0% |  |
| BUILD_LIST | 886,004 | 0.2% | 92.2% |  |
| BINARY_SUBSCR_DICT | 880,538 | 0.2% | 92.5% |  |
| BINARY_OP_SUBTRACT_INT | 844,267 | 0.2% | 92.7% |  |
| CONTAINS_OP | 799,440 | 0.2% | 93.0% |  |
| BUILD_MAP | 793,640 | 0.2% | 93.2% |  |
| TO_BOOL_INT | 782,399 | 0.2% | 93.4% | 0.8% |
| COPY_FREE_VARS | 782,060 | 0.2% | 93.6% |  |
| LOAD_ATTR_WITH_HINT | 764,637 | 0.2% | 93.8% | 2.1% |
| JUMP_FORWARD | 748,108 | 0.2% | 94.0% |  |
| LOAD_ATTR_CLASS | 733,220 | 0.2% | 94.2% | 0.1% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 711,852 | 0.2% | 94.4% |  |
| GET_ITER | 704,626 | 0.2% | 94.6% |  |
| CALL_PY_WITH_DEFAULTS | 646,929 | 0.2% | 94.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 646,107 | 0.2% | 95.0% |  |
| YIELD_VALUE | 577,520 | 0.2% | 95.2% |  |
| FOR_ITER_LIST | 573,312 | 0.2% | 95.3% |  |
| IS_OP | 568,820 | 0.2% | 95.5% |  |
| STORE_SUBSCR_DICT | 565,080 | 0.2% | 95.6% |  |
| BINARY_SLICE | 554,160 | 0.2% | 95.8% |  |
| DICT_MERGE | 480,760 | 0.1% | 95.9% |  |
| CALL_KW | 469,209 | 0.1% | 96.1% |  |
| PUSH_EXC_INFO | 459,340 | 0.1% | 96.2% |  |
| POP_EXCEPT | 459,220 | 0.1% | 96.3% |  |
| GET_AWAITABLE | 456,000 | 0.1% | 96.4% |  |
| CHECK_EXC_MATCH | 449,433 | 0.1% | 96.6% |  |
| END_SEND | 444,000 | 0.1% | 96.7% |  |
| BINARY_SUBSCR_GETITEM | 420,540 | 0.1% | 96.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 384,180 | 0.1% | 96.9% | 3.1% |
| MAKE_CELL | 363,859 | 0.1% | 97.0% |  |
| MAKE_FUNCTION | 359,953 | 0.1% | 97.1% |  |
| COMPARE_OP_FLOAT | 354,253 | 0.1% | 97.2% | 0.0% |
| BINARY_SUBSCR | 342,700 | 0.1% | 97.3% |  |
| SEND | 338,220 | 0.1% | 97.4% |  |
| RETURN_GENERATOR | 337,000 | 0.1% | 97.5% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 327,071 | 0.1% | 97.6% | 0.1% |
| EXIT_INIT_CHECK | 324,640 | 0.1% | 97.7% |  |
| CALL_ALLOC_AND_ENTER_INIT | 324,640 | 0.1% | 97.8% |  |
| LIST_EXTEND | 313,532 | 0.1% | 97.9% |  |
| CALL_INTRINSIC_1 | 301,512 | 0.1% | 97.9% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 293,920 | 0.1% | 98.0% | 46.5% |
| TO_BOOL_STR | 289,500 | 0.1% | 98.1% | 2.0% |
| STORE_ATTR | 289,200 | 0.1% | 98.2% |  |
| SEND_GEN | 287,800 | 0.1% | 98.3% |  |
| COMPARE_OP_STR | 277,940 | 0.1% | 98.3% | 0.0% |
| FOR_ITER_GEN | 275,940 | 0.1% | 98.4% |  |
| CALL_LIST_APPEND | 258,744 | 0.1% | 98.5% |  |
| CALL_BUILTIN_CLASS | 246,270 | 0.1% | 98.6% |  |
| BEFORE_WITH | 240,029 | 0.1% | 98.6% |  |
| JUMP_BACKWARD | 230,660 | 0.1% | 98.7% |  |
| BINARY_SUBSCR_TUPLE_INT | 229,280 | 0.1% | 98.8% |  |
| BINARY_OP_ADD_UNICODE | 228,560 | 0.1% | 98.8% |  |
| STORE_SUBSCR | 219,120 | 0.1% | 98.9% |  |
| DELETE_FAST | 214,469 | 0.1% | 98.9% |  |
| SET_FUNCTION_ATTRIBUTE | 207,084 | 0.1% | 99.0% |  |
| STORE_FAST_LOAD_FAST | 206,440 | 0.1% | 99.1% |  |
| CALL_TYPE_1 | 205,260 | 0.1% | 99.1% |  |
| FOR_ITER | 202,152 | 0.1% | 99.2% |  |
| LOAD_SUPER_ATTR_METHOD | 194,280 | 0.1% | 99.2% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 190,429 | 0.1% | 99.3% |  |
| COMPARE_OP | 177,004 | 0.0% | 99.3% |  |
| EXTENDED_ARG | 145,900 | 0.0% | 99.4% |  |
| TO_BOOL_LIST | 145,287 | 0.0% | 99.4% | 0.1% |
| STORE_DEREF | 121,560 | 0.0% | 99.4% |  |
| BINARY_OP_ADD_FLOAT | 121,312 | 0.0% | 99.5% |  |
| LOAD_ATTR_PROPERTY | 120,560 | 0.0% | 99.5% |  |
| DELETE_SUBSCR | 120,440 | 0.0% | 99.5% |  |
| LOAD_SUPER_ATTR_ATTR | 119,980 | 0.0% | 99.6% |  |
| UNPACK_SEQUENCE_LIST | 119,960 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_STR_INT | 108,700 | 0.0% | 99.6% | 0.1% |
| FOR_ITER_TUPLE | 100,520 | 0.0% | 99.7% |  |
| BINARY_OP_SUBTRACT_FLOAT | 84,956 | 0.0% | 99.7% |  |
| UNPACK_SEQUENCE_TUPLE | 84,280 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_LIST_INT | 74,805 | 0.0% | 99.7% | 0.1% |
| LOAD_FAST_AND_CLEAR | 73,440 | 0.0% | 99.8% |  |
| BUILD_SLICE | 72,060 | 0.0% | 99.8% |  |
| RERAISE | 72,020 | 0.0% | 99.8% |  |
| FORMAT_SIMPLE | 60,400 | 0.0% | 99.8% |  |
| CONVERT_VALUE | 60,320 | 0.0% | 99.8% |  |
| UNARY_INVERT | 60,180 | 0.0% | 99.9% |  |
| END_FOR | 59,980 | 0.0% | 99.9% |  |
| STORE_ATTR_WITH_HINT | 59,019 | 0.0% | 99.9% | 9.0% |
| FOR_ITER_RANGE | 57,642 | 0.0% | 99.9% |  |
| CALL_BUILTIN_O | 56,263 | 0.0% | 99.9% |  |
| TO_BOOL_ALWAYS_TRUE | 48,240 | 0.0% | 99.9% | 0.1% |
| LOAD_FAST_CHECK | 40,131 | 0.0% | 99.9% |  |
| LOAD_GLOBAL | 28,720 | 0.0% | 99.9% |  |
| RAISE_VARARGS | 24,420 | 0.0% | 100.0% |  |
| BUILD_STRING | 24,240 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 23,960 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 13,960 | 0.0% | 100.0% |  |
| LIST_APPEND | 13,120 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 12,240 | 0.0% | 100.0% |  |
| UNARY_NOT | 12,140 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 12,080 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 12,025 | 0.0% | 100.0% |  |
| BUILD_SET | 12,020 | 0.0% | 100.0% |  |
| RESUME | 9,300 | 0.0% | 100.0% | 9.3% |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 21,842,112 | 6.1% | 6.1% |
| RESUME_CHECK LOAD_FAST | 11,423,647 | 3.2% | 9.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 10,221,060 | 2.9% | 12.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,248,797 | 2.0% | 14.2% |
| STORE_FAST LOAD_FAST | 6,715,617 | 1.9% | 16.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 6,383,229 | 1.8% | 17.8% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 6,011,619 | 1.7% | 19.5% |
| CACHE RESUME_CHECK | 5,386,817 | 1.5% | 21.0% |
| RETURN_CONST POP_TOP | 5,225,398 | 1.5% | 22.5% |
| LOAD_CONST LOAD_FAST | 5,162,967 | 1.4% | 23.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,145,154 | 1.4% | 25.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 4,942,874 | 1.4% | 26.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 4,479,679 | 1.3% | 28.0% |
| POP_JUMP_IF_NONE LOAD_FAST | 4,474,781 | 1.2% | 29.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 4,116,224 | 1.1% | 30.4% |
| POP_TOP LOAD_FAST | 3,984,607 | 1.1% | 31.5% |
| RETURN_VALUE INTERPRETER_EXIT | 3,745,795 | 1.0% | 32.5% |
| LOAD_FAST LOAD_ATTR | 3,592,345 | 1.0% | 33.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 3,344,509 | 0.9% | 34.5% |
| LOAD_FAST LOAD_CONST | 3,329,133 | 0.9% | 35.4% |
| LOAD_FAST RETURN_VALUE | 3,170,134 | 0.9% | 36.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,073,745 | 0.9% | 37.1% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 3,035,561 | 0.8% | 38.0% |
| POP_TOP RETURN_CONST | 3,012,091 | 0.8% | 38.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,852,512 | 0.8% | 39.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 2,819,709 | 0.8% | 40.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,790,436 | 0.8% | 41.2% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 2,703,031 | 0.8% | 42.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 2,663,006 | 0.7% | 42.7% |
| LOAD_FAST LOAD_ATTR_SLOT | 2,602,324 | 0.7% | 43.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 2,256,545 | 0.6% | 44.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 2,247,933 | 0.6% | 44.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,230,475 | 0.6% | 45.3% |
| RETURN_VALUE STORE_FAST | 2,207,843 | 0.6% | 45.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,189,012 | 0.6% | 46.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,138,787 | 0.6% | 47.1% |
| LOAD_FAST POP_JUMP_IF_NONE | 2,044,672 | 0.6% | 47.7% |
| LOAD_FAST CALL | 2,006,386 | 0.6% | 48.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 1,993,522 | 0.6% | 48.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,992,600 | 0.6% | 49.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,966,828 | 0.5% | 49.9% |
| RETURN_VALUE TO_BOOL_BOOL | 1,899,071 | 0.5% | 50.5% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,878,526 | 0.5% | 51.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,876,866 | 0.5% | 51.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 1,825,373 | 0.5% | 52.0% |
| CALL STORE_FAST | 1,803,676 | 0.5% | 52.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 1,798,384 | 0.5% | 53.0% |
| LOAD_FAST STORE_ATTR_SLOT | 1,796,754 | 0.5% | 53.5% |
| RETURN_CONST INTERPRETER_EXIT | 1,712,664 | 0.5% | 54.0% |
| LOAD_CONST COMPARE_OP_INT | 1,710,423 | 0.5% | 54.5% |
| NOP LOAD_FAST | 1,682,112 | 0.5% | 54.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,680,262 | 0.5% | 55.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 1,679,189 | 0.5% | 55.9% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,563,420 | 0.4% | 56.3% |
| PUSH_NULL LOAD_FAST | 1,366,504 | 0.4% | 56.7% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 1,304,433 | 0.4% | 57.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 1,287,582 | 0.4% | 57.4% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,274,671 | 0.4% | 57.8% |
| LOAD_CONST STORE_FAST | 1,220,154 | 0.3% | 58.1% |
| RESUME_CHECK NOP | 1,203,182 | 0.3% | 58.5% |
| LOAD_ATTR LOAD_FAST | 1,172,585 | 0.3% | 58.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,164,196 | 0.3% | 59.1% |
| LOAD_FAST COPY | 1,130,196 | 0.3% | 59.4% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 1,129,586 | 0.3% | 59.7% |
| LOAD_CONST LOAD_CONST | 1,100,038 | 0.3% | 60.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,093,580 | 0.3% | 60.4% |
| TO_BOOL POP_JUMP_IF_FALSE | 1,061,849 | 0.3% | 60.7% |
| POP_JUMP_IF_FALSE LOAD_CONST | 1,061,660 | 0.3% | 61.0% |
| STORE_ATTR_SLOT LOAD_CONST | 1,048,122 | 0.3% | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,043,920 | 0.3% | 61.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 1,035,076 | 0.3% | 61.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,007,465 | 0.3% | 62.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 997,280 | 0.3% | 62.4% |
| CALL POP_TOP | 984,542 | 0.3% | 62.7% |
| RETURN_VALUE RETURN_VALUE | 973,720 | 0.3% | 62.9% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 950,451 | 0.3% | 63.2% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 947,851 | 0.3% | 63.5% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 937,196 | 0.3% | 63.7% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 937,196 | 0.3% | 64.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 927,531 | 0.3% | 64.2% |
| POP_TOP LOAD_CONST | 922,363 | 0.3% | 64.5% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 900,980 | 0.3% | 64.8% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 894,462 | 0.2% | 65.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 878,729 | 0.2% | 65.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 875,966 | 0.2% | 65.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 856,785 | 0.2% | 65.7% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 856,262 | 0.2% | 66.0% |
| LOAD_FAST CALL_BUILTIN_FAST | 837,640 | 0.2% | 66.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 815,744 | 0.2% | 66.4% |
| CALL_BUILTIN_FAST STORE_FAST | 814,460 | 0.2% | 66.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 813,313 | 0.2% | 66.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 797,440 | 0.2% | 67.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_INSTANCE_VALUE | 791,180 | 0.2% | 67.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 785,958 | 0.2% | 67.6% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 763,677 | 0.2% | 67.8% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 760,772 | 0.2% | 68.0% |
| PUSH_NULL CALL | 736,137 | 0.2% | 68.2% |
| CALL LOAD_FAST | 736,031 | 0.2% | 68.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 734,671 | 0.2% | 68.6% |
| COPY_FREE_VARS RESUME_CHECK | 732,500 | 0.2% | 68.8% |


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
| RESUME_CHECK | 5,386,817 | 93.7% |
| COPY_FREE_VARS | 238,462 | 4.1% |
| POP_TOP | 97,060 | 1.7% |
| MAKE_CELL | 12,360 | 0.2% |
| RETURN_GENERATOR | 12,000 | 0.2% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 118,569 | 49.4% |
| RETURN_VALUE | 108,100 | 45.0% |
| LOAD_GLOBAL_MODULE | 12,540 | 5.2% |
| CALL | 380 | 0.2% |
| LOAD_ATTR | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 239,949 | 100.0% |
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
| LOAD_CONST | 338,020 | 98.6% |
| BINARY_SUBSCR | 2,940 | 0.9% |
| BUILD_TUPLE | 640 | 0.2% |
| LOAD_FAST | 420 | 0.1% |
| LOAD_NAME | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 180,200 | 52.6% |
| LOAD_FAST | 60,140 | 17.5% |
| CONVERT_VALUE | 24,000 | 7.0% |
| LOAD_CONST | 12,960 | 3.8% |
| BINARY_SUBSCR_LIST_INT | 12,300 | 3.6% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 390,724 | 86.9% |
| BUILD_TUPLE | 24,080 | 5.4% |
| LOAD_ATTR_MODULE | 22,349 | 5.0% |
| LOAD_GLOBAL_MODULE | 11,980 | 2.7% |
| LOAD_GLOBAL | 260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 449,433 | 100.0% |


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
| LOAD_FAST | 240,656 | 34.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 144,140 | 20.5% |
| LOAD_ATTR_INSTANCE_VALUE | 96,580 | 13.7% |
| LOAD_ATTR | 72,140 | 10.2% |
| BINARY_SLICE | 36,240 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 319,425 | 45.3% |
| FOR_ITER | 148,431 | 21.1% |
| FOR_ITER_TUPLE | 73,020 | 10.4% |
| CALL_PY_EXACT_ARGS | 72,720 | 10.3% |
| LOAD_FAST_AND_CLEAR | 49,440 | 7.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,745,795 | 65.3% |
| RETURN_CONST | 1,712,664 | 29.9% |
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
| LOAD_CONST | 359,953 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 155,253 | 43.1% |
| CALL | 120,080 | 33.4% |
| LOAD_FAST | 48,400 | 13.4% |
| CALL_PY_EXACT_ARGS | 23,920 | 6.6% |
| STORE_DEREF | 12,000 | 3.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,203,182 | 40.4% |
| POP_JUMP_IF_FALSE | 521,987 | 17.5% |
| STORE_FAST | 382,856 | 12.9% |
| STORE_ATTR_INSTANCE_VALUE | 306,622 | 10.3% |
| POP_JUMP_IF_TRUE | 196,922 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,682,112 | 56.5% |
| LOAD_GLOBAL_MODULE | 547,046 | 18.4% |
| LOAD_FAST_LOAD_FAST | 300,220 | 10.1% |
| LOAD_DEREF | 134,638 | 4.5% |
| LOAD_GLOBAL_BUILTIN | 120,140 | 4.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 256,271 | 55.8% |
| SWAP | 132,240 | 28.8% |
| COPY | 36,020 | 7.8% |
| STORE_ATTR_INSTANCE_VALUE | 12,120 | 2.6% |
| STORE_SUBSCR_DICT | 12,000 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 218,213 | 47.5% |
| RETURN_VALUE | 132,240 | 28.8% |
| RERAISE | 36,020 | 7.8% |
| DELETE_FAST | 24,000 | 5.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 22,429 | 4.9% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,225,398 | 51.3% |
| CALL | 984,542 | 9.7% |
| CALL_METHOD_DESCRIPTOR_O | 815,744 | 8.0% |
| POP_JUMP_IF_FALSE | 610,672 | 6.0% |
| CALL_FUNCTION_EX | 500,062 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,984,607 | 39.1% |
| RETURN_CONST | 3,012,091 | 29.6% |
| LOAD_CONST | 922,363 | 9.1% |
| ENTER_EXECUTOR | 705,036 | 6.9% |
| RESUME_CHECK | 336,620 | 3.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 348,440 | 75.9% |
| CALL | 36,502 | 7.9% |
| RERAISE | 36,020 | 7.8% |
| CALL_METHOD_DESCRIPTOR_O | 12,105 | 2.6% |
| RAISE_VARARGS | 12,000 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 400,491 | 87.2% |
| LOAD_GLOBAL_MODULE | 46,229 | 10.1% |
| LOAD_FAST | 12,000 | 2.6% |
| LOAD_GLOBAL | 620 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,680,262 | 52.0% |
| LOAD_ATTR | 674,641 | 20.9% |
| LOAD_FAST | 474,718 | 14.7% |
| LOAD_DEREF | 204,500 | 6.3% |
| RETURN_VALUE | 132,080 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,366,504 | 42.3% |
| CALL | 736,137 | 22.8% |
| LOAD_FAST_LOAD_FAST | 713,269 | 22.1% |
| LOAD_GLOBAL_MODULE | 108,380 | 3.4% |
| LOAD_CONST | 96,100 | 3.0% |


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
| LOAD_FAST | 3,170,134 | 27.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,703,031 | 23.2% |
| RETURN_VALUE | 973,720 | 8.4% |
| CALL | 626,326 | 5.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 622,560 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 3,745,795 | 32.1% |
| STORE_FAST | 2,207,843 | 18.9% |
| TO_BOOL_BOOL | 1,899,071 | 16.3% |
| RETURN_VALUE | 973,720 | 8.4% |
| LOAD_FAST | 603,752 | 5.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 108,580 | 49.6% |
| LOAD_CONST | 96,180 | 43.9% |
| LOAD_FAST_LOAD_FAST | 12,220 | 5.6% |
| STORE_SUBSCR | 1,740 | 0.8% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 108,240 | 49.4% |
| LOAD_FAST | 48,240 | 22.0% |
| LOAD_CONST | 24,060 | 11.0% |
| LOAD_DEREF | 24,000 | 11.0% |
| ENTER_EXECUTOR | 11,880 | 5.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 567,086 | 44.6% |
| LOAD_ATTR_INSTANCE_VALUE | 520,532 | 40.9% |
| LOAD_ATTR | 122,800 | 9.7% |
| COPY | 36,800 | 2.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 12,380 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,061,849 | 83.5% |
| POP_JUMP_IF_TRUE | 197,067 | 15.5% |
| TO_BOOL | 5,900 | 0.5% |
| TO_BOOL_BOOL | 5,200 | 0.4% |
| TO_BOOL_NONE | 1,082 | 0.1% |


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
| LOAD_GLOBAL_MODULE | 188,526 | 17.0% |
| LOAD_CONST | 168,985 | 15.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 155,880 | 14.0% |
| LOAD_FAST | 107,657 | 9.7% |
| LOAD_ATTR_CLASS | 96,080 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 291,014 | 26.2% |
| STORE_FAST | 201,831 | 18.2% |
| COPY | 135,415 | 12.2% |
| LOAD_FAST | 96,640 | 8.7% |
| RETURN_VALUE | 96,120 | 8.7% |


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
| LOAD_FAST | 382,940 | 43.2% |
| STORE_FAST | 111,272 | 12.6% |
| LOAD_FAST_LOAD_FAST | 107,540 | 12.1% |
| RESUME_CHECK | 72,940 | 8.2% |
| SWAP | 49,440 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 662,332 | 74.8% |
| STORE_FAST | 136,932 | 15.5% |
| SWAP | 49,440 | 5.6% |
| LOAD_CONST | 24,120 | 2.7% |
| CALL_BUILTIN_CLASS | 11,960 | 1.3% |


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
| LOAD_FAST | 512,862 | 39.4% |
| LOAD_FAST_LOAD_FAST | 300,780 | 23.1% |
| LOAD_GLOBAL_BUILTIN | 156,660 | 12.0% |
| LOAD_GLOBAL_MODULE | 99,540 | 7.7% |
| LOAD_ATTR_MODULE | 71,940 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 191,840 | 14.8% |
| RETURN_VALUE | 180,760 | 13.9% |
| CALL_ISINSTANCE | 157,200 | 12.1% |
| LOAD_CONST | 154,873 | 11.9% |
| CONTAINS_OP | 121,400 | 9.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,006,386 | 33.8% |
| PUSH_NULL | 736,137 | 12.4% |
| LOAD_GLOBAL_MODULE | 571,613 | 9.6% |
| LOAD_CONST | 468,373 | 7.9% |
| LOAD_FAST_LOAD_FAST | 439,871 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,803,676 | 30.4% |
| POP_TOP | 984,542 | 16.6% |
| LOAD_FAST | 736,031 | 12.4% |
| RETURN_VALUE | 626,326 | 10.6% |
| BINARY_SUBSCR_DICT | 420,140 | 7.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 480,760 | 44.2% |
| ENTER_EXECUTOR | 364,270 | 33.5% |
| LOAD_FAST | 106,709 | 9.8% |
| CALL_INTRINSIC_1 | 75,652 | 7.0% |
| BUILD_MAP | 59,200 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 500,062 | 46.0% |
| RETURN_VALUE | 227,429 | 20.9% |
| RESUME_CHECK | 132,220 | 12.2% |
| STORE_FAST | 119,360 | 11.0% |
| CALL | 83,300 | 7.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 289,512 | 96.0% |
| RERAISE | 12,000 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 154,660 | 51.3% |
| CALL_FUNCTION_EX | 75,652 | 25.1% |
| LOAD_CONST | 59,200 | 19.6% |
| RERAISE | 12,000 | 4.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 409,529 | 87.3% |
| ENTER_EXECUTOR | 59,680 | 12.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 265,420 | 56.6% |
| STORE_FAST | 106,509 | 22.7% |
| COPY_FREE_VARS | 24,000 | 5.1% |
| RETURN_VALUE | 12,440 | 2.7% |
| LOAD_FAST | 12,180 | 2.6% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 112,536 | 63.6% |
| LOAD_ATTR | 24,440 | 13.8% |
| LOAD_ATTR_INSTANCE_VALUE | 12,340 | 7.0% |
| LOAD_FAST_LOAD_FAST | 12,000 | 6.8% |
| LOAD_ATTR_CLASS | 12,000 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 112,521 | 63.6% |
| POP_JUMP_IF_TRUE | 60,580 | 34.2% |
| COMPARE_OP | 1,763 | 1.0% |
| COMPARE_OP_INT | 1,440 | 0.8% |
| COMPARE_OP_STR | 460 | 0.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 204,420 | 25.6% |
| LOAD_CONST | 145,280 | 18.2% |
| BUILD_TUPLE | 121,400 | 15.2% |
| LOAD_FAST | 109,280 | 13.7% |
| LOAD_FAST_LOAD_FAST | 108,720 | 13.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 605,580 | 75.8% |
| COPY | 120,040 | 15.0% |
| POP_JUMP_IF_TRUE | 25,300 | 3.2% |
| SWAP | 24,000 | 3.0% |
| STORE_FAST | 12,080 | 1.5% |


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
| LOAD_FAST | 1,130,196 | 46.9% |
| LOAD_CONST | 252,200 | 10.5% |
| STORE_ATTR_INSTANCE_VALUE | 227,980 | 9.5% |
| BINARY_OP | 135,415 | 5.6% |
| CONTAINS_OP | 120,040 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 937,196 | 38.9% |
| LOAD_FAST | 456,000 | 18.9% |
| TO_BOOL_BOOL | 326,140 | 13.5% |
| TO_BOOL_NONE | 190,721 | 7.9% |
| TO_BOOL_INT | 163,126 | 6.8% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 288,531 | 36.9% |
| CACHE | 238,462 | 30.5% |
| CALL | 120,900 | 15.5% |
| LOAD_ATTR_PROPERTY | 83,920 | 10.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 25,907 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 732,500 | 93.7% |
| RETURN_GENERATOR | 24,600 | 3.1% |
| MAKE_CELL | 24,100 | 3.1% |
| RESUME | 860 | 0.1% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 108,000 | 50.4% |
| NOP | 24,000 | 11.2% |
| POP_EXCEPT | 24,000 | 11.2% |
| STORE_ATTR_INSTANCE_VALUE | 23,980 | 11.2% |
| POP_TOP | 22,389 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 108,000 | 50.4% |
| RETURN_CONST | 48,000 | 22.4% |
| LOAD_FAST | 34,389 | 16.0% |
| LOAD_CONST | 12,080 | 5.6% |
| ENTER_EXECUTOR | 11,660 | 5.4% |


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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 705,036 | 52.0% |
| POP_JUMP_IF_TRUE | 210,030 | 15.5% |
| FOR_ITER_LIST | 107,660 | 7.9% |
| CALL_LIST_APPEND | 100,422 | 7.4% |
| STORE_ATTR_INSTANCE_VALUE | 83,660 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 364,270 | 26.9% |
| FOR_ITER_LIST | 233,768 | 17.2% |
| CALL | 225,886 | 16.7% |
| RESUME_CHECK | 129,353 | 9.5% |
| YIELD_VALUE | 95,400 | 7.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 119,920 | 82.2% |
| COMPARE_OP_STR | 12,180 | 8.3% |
| STORE_ATTR_INSTANCE_VALUE | 11,980 | 8.2% |
| POP_JUMP_IF_TRUE | 340 | 0.2% |
| GET_ITER | 320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 108,000 | 74.0% |
| POP_JUMP_IF_FALSE | 24,520 | 16.8% |
| JUMP_FORWARD | 12,340 | 8.5% |
| JUMP_BACKWARD | 440 | 0.3% |
| FOR_ITER_LIST | 360 | 0.2% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 148,431 | 73.4% |
| SWAP | 24,460 | 12.1% |
| LOAD_FAST | 24,200 | 12.0% |
| JUMP_BACKWARD | 2,641 | 1.3% |
| FOR_ITER | 2,180 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 108,531 | 53.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 24,360 | 12.1% |
| LOAD_FAST | 24,340 | 12.0% |
| SWAP | 24,080 | 11.9% |
| STORE_FAST | 16,601 | 8.2% |


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
| LOAD_GLOBAL_MODULE | 314,880 | 55.4% |
| LOAD_FAST | 108,560 | 19.1% |
| LOAD_CONST | 108,160 | 19.0% |
| LOAD_DEREF | 24,000 | 4.2% |
| LOAD_FAST_LOAD_FAST | 12,360 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 460,360 | 80.9% |
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
| POP_TOP | 219,340 | 95.1% |
| POP_JUMP_IF_TRUE | 3,040 | 1.3% |
| POP_JUMP_IF_FALSE | 2,140 | 0.9% |
| CALL_LIST_APPEND | 1,840 | 0.8% |
| LIST_APPEND | 960 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 215,960 | 93.6% |
| FOR_ITER_LIST | 6,459 | 2.8% |
| FOR_ITER | 2,641 | 1.1% |
| LOAD_FAST | 1,820 | 0.8% |
| FOR_ITER_RANGE | 1,260 | 0.5% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 167,760 | 88.1% |
| POP_EXCEPT | 22,429 | 11.8% |
| RESUME | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 108,000 | 56.7% |
| SEND | 60,000 | 31.5% |
| LOAD_FAST | 22,429 | 11.8% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 441,025 | 59.0% |
| POP_TOP | 132,420 | 17.7% |
| STORE_ATTR_INSTANCE_VALUE | 48,380 | 6.5% |
| POP_JUMP_IF_FALSE | 29,063 | 3.9% |
| POP_JUMP_IF_TRUE | 24,400 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 486,498 | 65.0% |
| LOAD_CONST | 86,311 | 11.5% |
| LOAD_FAST_LOAD_FAST | 60,420 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 41,979 | 5.6% |
| LOAD_GLOBAL_MODULE | 36,000 | 4.8% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 12,040 | 91.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 500 | 3.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 320 | 2.4% |
| LOAD_FAST | 240 | 1.8% |
| CALL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,160 | 92.7% |
| JUMP_BACKWARD | 960 | 7.3% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 262,020 | 83.6% |
| LOAD_CONST | 24,020 | 7.7% |
| LOAD_ATTR_SLOT | 15,292 | 4.9% |
| LOAD_ATTR_INSTANCE_VALUE | 11,980 | 3.8% |
| LOAD_DEREF | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 289,512 | 92.3% |
| LOAD_FAST | 24,000 | 7.7% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,592,345 | 64.3% |
| LOAD_ATTR_INSTANCE_VALUE | 878,729 | 15.7% |
| LOAD_ATTR_WITH_HINT | 335,900 | 6.0% |
| LOAD_GLOBAL_MODULE | 303,620 | 5.4% |
| LOAD_DEREF | 152,042 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,172,585 | 21.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 894,462 | 16.0% |
| PUSH_NULL | 674,641 | 12.1% |
| LOAD_CONST | 483,080 | 8.7% |
| CALL_PY_EXACT_ARGS | 321,815 | 5.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,329,133 | 20.8% |
| STORE_ATTR_INSTANCE_VALUE | 1,679,189 | 10.5% |
| LOAD_CONST | 1,100,038 | 6.9% |
| POP_JUMP_IF_FALSE | 1,061,660 | 6.6% |
| STORE_ATTR_SLOT | 1,048,122 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,162,967 | 32.2% |
| COMPARE_OP_INT | 1,710,423 | 10.7% |
| STORE_FAST | 1,220,154 | 7.6% |
| LOAD_CONST | 1,100,038 | 6.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 634,620 | 4.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 401,531 | 19.2% |
| RESUME_CHECK | 207,571 | 9.9% |
| POP_JUMP_IF_FALSE | 171,591 | 8.2% |
| POP_JUMP_IF_TRUE | 144,340 | 6.9% |
| NOP | 134,638 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 506,920 | 24.2% |
| LOAD_ATTR_INSTANCE_VALUE | 368,853 | 17.6% |
| PUSH_NULL | 204,500 | 9.8% |
| STORE_ATTR_INSTANCE_VALUE | 155,680 | 7.4% |
| LOAD_ATTR | 152,042 | 7.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,423,647 | 15.4% |
| POP_JUMP_IF_FALSE | 7,248,797 | 9.8% |
| STORE_FAST | 6,715,617 | 9.0% |
| LOAD_CONST | 5,162,967 | 7.0% |
| LOAD_GLOBAL_BUILTIN | 5,145,154 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 21,842,112 | 29.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,011,619 | 8.1% |
| STORE_ATTR_INSTANCE_VALUE | 4,942,874 | 6.7% |
| LOAD_ATTR | 3,592,345 | 4.8% |
| CALL_PY_EXACT_ARGS | 3,344,509 | 4.5% |


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
| LOAD_ATTR_METHOD_NO_DICT | 15,571 | 38.8% |
| POP_JUMP_IF_FALSE | 12,000 | 29.9% |
| STORE_FAST | 12,000 | 29.9% |
| POP_TOP | 320 | 0.8% |
| JUMP_FORWARD | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 15,471 | 38.6% |
| LOAD_ATTR | 12,000 | 29.9% |
| LOAD_CONST | 12,000 | 29.9% |
| POP_JUMP_IF_NOT_NONE | 440 | 1.1% |
| LOAD_FAST | 80 | 0.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,304,433 | 12.9% |
| LOAD_GLOBAL_MODULE | 1,093,580 | 10.8% |
| STORE_ATTR_INSTANCE_VALUE | 997,280 | 9.8% |
| STORE_FAST | 950,451 | 9.4% |
| POP_JUMP_IF_FALSE | 900,980 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,992,600 | 19.7% |
| STORE_ATTR_SLOT | 1,798,384 | 17.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,274,671 | 12.6% |
| LOAD_FAST | 875,966 | 8.6% |
| LOAD_FAST_LOAD_FAST | 734,671 | 7.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,560 | 12.4% |
| POP_JUMP_IF_FALSE | 3,460 | 12.0% |
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
| MAKE_CELL | 187,662 | 51.6% |
| CALL_PY_EXACT_ARGS | 115,197 | 31.7% |
| COPY_FREE_VARS | 24,100 | 6.6% |
| CACHE | 12,360 | 3.4% |
| CALL | 12,320 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 187,662 | 51.6% |
| RESUME_CHECK | 163,677 | 45.0% |
| RETURN_GENERATOR | 12,000 | 3.3% |
| RESUME | 520 | 0.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,383,229 | 45.5% |
| COMPARE_OP_INT | 2,663,006 | 19.0% |
| TO_BOOL_NONE | 1,287,582 | 9.2% |
| TO_BOOL | 1,061,849 | 7.6% |
| CONTAINS_OP | 605,580 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,248,797 | 51.6% |
| RETURN_CONST | 1,563,420 | 11.1% |
| LOAD_CONST | 1,061,660 | 7.6% |
| LOAD_GLOBAL_MODULE | 1,007,465 | 7.2% |
| LOAD_FAST_LOAD_FAST | 900,980 | 6.4% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,035,561 | 56.0% |
| LOAD_FAST | 2,044,672 | 37.7% |
| LOAD_ATTR | 132,960 | 2.5% |
| LOAD_DEREF | 132,080 | 2.4% |
| LOAD_ATTR_WITH_HINT | 34,959 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,474,781 | 82.6% |
| RETURN_CONST | 279,751 | 5.2% |
| LOAD_GLOBAL_MODULE | 276,580 | 5.1% |
| LOAD_FAST_LOAD_FAST | 144,440 | 2.7% |
| NOP | 132,300 | 2.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,035,076 | 62.7% |
| LOAD_ATTR_INSTANCE_VALUE | 456,040 | 27.6% |
| LOAD_ATTR | 108,980 | 6.6% |
| LOAD_GLOBAL_MODULE | 12,600 | 0.8% |
| CALL | 12,020 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 573,954 | 34.8% |
| LOAD_FAST_LOAD_FAST | 435,551 | 26.4% |
| LOAD_GLOBAL_MODULE | 337,931 | 20.5% |
| LOAD_CONST | 132,200 | 8.0% |
| LOAD_DEREF | 84,280 | 5.1% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,230,475 | 54.7% |
| COMPARE_OP_INT | 708,520 | 17.4% |
| TO_BOOL_INT | 251,789 | 6.2% |
| TO_BOOL_STR | 240,700 | 5.9% |
| TO_BOOL_NONE | 203,853 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,993,522 | 48.9% |
| LOAD_GLOBAL_BUILTIN | 449,420 | 11.0% |
| LOAD_CONST | 233,998 | 5.7% |
| LOAD_FAST_LOAD_FAST | 228,460 | 5.6% |
| POP_TOP | 216,280 | 5.3% |


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
| POP_TOP | 3,012,091 | 38.1% |
| POP_JUMP_IF_FALSE | 1,563,420 | 19.8% |
| STORE_ATTR_INSTANCE_VALUE | 760,772 | 9.6% |
| STORE_ATTR_SLOT | 613,331 | 7.8% |
| STORE_FAST | 394,614 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,225,398 | 66.1% |
| INTERPRETER_EXIT | 1,712,664 | 21.7% |
| EXIT_INIT_CHECK | 324,640 | 4.1% |
| STORE_FAST | 170,311 | 2.2% |
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
| MAKE_FUNCTION | 155,253 | 75.0% |
| SET_FUNCTION_ATTRIBUTE | 51,831 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 65,522 | 31.6% |
| SET_FUNCTION_ATTRIBUTE | 51,831 | 25.0% |
| CALL | 39,571 | 19.1% |
| LOAD_FAST | 24,320 | 11.7% |
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
| RETURN_VALUE | 2,207,843 | 20.6% |
| CALL | 1,803,676 | 16.8% |
| LOAD_CONST | 1,220,154 | 11.4% |
| CALL_BUILTIN_FAST | 814,460 | 7.6% |
| LOAD_ATTR_INSTANCE_VALUE | 713,632 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,715,617 | 62.5% |
| LOAD_FAST_LOAD_FAST | 950,451 | 8.8% |
| LOAD_CONST | 587,869 | 5.5% |
| LOAD_GLOBAL_BUILTIN | 476,028 | 4.4% |
| JUMP_FORWARD | 441,025 | 4.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 107,980 | 52.3% |
| COPY | 84,060 | 40.7% |
| STORE_ATTR | 12,000 | 5.8% |
| FOR_ITER_LIST | 940 | 0.5% |
| FOR_ITER_TUPLE | 500 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 108,560 | 52.6% |
| STORE_ATTR_INSTANCE_VALUE | 83,920 | 40.7% |
| STORE_ATTR | 12,080 | 5.9% |
| TO_BOOL_LIST | 540 | 0.3% |
| TO_BOOL_STR | 500 | 0.2% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 633,707 | 71.4% |
| UNPACK_SEQUENCE_LIST | 119,960 | 13.5% |
| UNPACK_SEQUENCE_TUPLE | 72,300 | 8.1% |
| COPY | 24,200 | 2.7% |
| STORE_FAST_STORE_FAST | 24,160 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 453,387 | 51.1% |
| LOAD_GLOBAL_MODULE | 131,880 | 14.9% |
| STORE_FAST | 96,460 | 10.9% |
| LOAD_FAST_LOAD_FAST | 84,660 | 9.5% |
| LOAD_GLOBAL_BUILTIN | 84,180 | 9.5% |


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
| BINARY_OP_ADD_INT | 573,449 | 39.0% |
| BINARY_OP_SUBTRACT_INT | 340,027 | 23.2% |
| LOAD_FAST | 264,520 | 18.0% |
| LOAD_ATTR | 58,223 | 4.0% |
| BUILD_LIST | 49,440 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 937,196 | 63.8% |
| POP_EXCEPT | 132,240 | 9.0% |
| COPY | 108,300 | 7.4% |
| STORE_FAST | 95,003 | 6.5% |
| LOAD_CONST | 72,280 | 4.9% |


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
| YIELD_VALUE | 108,000 | 18.7% |
| BINARY_OP_ADD_UNICODE | 107,980 | 18.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 107,980 | 18.7% |
| ENTER_EXECUTOR | 95,400 | 16.5% |
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
| CACHE | 2,000 | 21.5% |
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
| LOAD_ATTR_INSTANCE_VALUE | 14,992 | 12.4% |
| LOAD_ATTR | 11,960 | 9.9% |
| BINARY_OP | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,160 | 58.7% |
| LOAD_GLOBAL_MODULE | 35,080 | 28.9% |
| STORE_FAST | 15,012 | 12.4% |
| LOAD_GLOBAL | 60 | 0.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 682,109 | 62.6% |
| LOAD_FAST_LOAD_FAST | 263,840 | 24.2% |
| CALL_LEN | 83,960 | 7.7% |
| LOAD_CONST | 59,760 | 5.5% |
| BINARY_OP | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 573,449 | 52.6% |
| BINARY_SLICE | 311,940 | 28.6% |
| RETURN_VALUE | 71,980 | 6.6% |
| CALL_PY_EXACT_ARGS | 71,960 | 6.6% |
| STORE_FAST | 60,280 | 5.5% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 119,920 | 52.5% |
| RETURN_VALUE | 107,960 | 47.2% |
| LOAD_FAST_LOAD_FAST | 300 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.1% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 107,980 | 47.2% |
| LOAD_GLOBAL_MODULE | 107,960 | 47.2% |
| STORE_FAST | 12,220 | 5.3% |
| LOAD_FAST | 240 | 0.1% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 11,960 | 99.5% |
| BINARY_OP | 40 | 0.3% |
| LOAD_CONST | 25 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,980 | 99.6% |
| CALL_BUILTIN_O | 25 | 0.2% |
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
| RETURN_VALUE | 59,185 | 69.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,960 | 14.1% |
| LOAD_ATTR_WITH_HINT | 11,960 | 14.1% |
| CALL | 1,691 | 2.0% |
| BINARY_OP | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 59,160 | 69.6% |
| RETURN_VALUE | 11,980 | 14.1% |
| LOAD_FAST | 11,980 | 14.1% |
| STORE_FAST | 1,756 | 2.1% |
| LOAD_DEREF | 60 | 0.1% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 563,920 | 66.8% |
| LOAD_ATTR_INSTANCE_VALUE | 95,920 | 11.4% |
| BINARY_OP_SUBTRACT_INT | 83,960 | 9.9% |
| CALL_LEN | 60,080 | 7.1% |
| LOAD_CONST | 40,107 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 340,027 | 40.3% |
| STORE_FAST | 324,000 | 38.4% |
| LOAD_FAST | 84,040 | 10.0% |
| BINARY_OP_SUBTRACT_INT | 83,960 | 9.9% |
| BINARY_SUBSCR_LIST_INT | 11,960 | 1.4% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 420,140 | 47.7% |
| LOAD_FAST | 350,378 | 39.8% |
| BUILD_TUPLE | 48,080 | 5.5% |
| RETURN_VALUE | 23,980 | 2.7% |
| LOAD_FAST_LOAD_FAST | 12,240 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 432,040 | 49.1% |
| PUSH_EXC_INFO | 348,440 | 39.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 37,998 | 4.3% |
| STORE_FAST | 24,340 | 2.8% |
| LOAD_FAST_LOAD_FAST | 12,200 | 1.4% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 300,000 | 71.3% |
| LOAD_FAST | 120,100 | 28.6% |
| LOAD_CONST | 240 | 0.1% |
| ENTER_EXECUTOR | 160 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 420,520 | 100.0% |
| RESUME | 20 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,965 | 66.8% |
| BINARY_SUBSCR | 12,300 | 16.4% |
| BINARY_OP_SUBTRACT_INT | 11,960 | 16.0% |
| LOAD_FAST | 580 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,240 | 32.4% |
| LOAD_ATTR_SLOT | 20,195 | 27.0% |
| STORE_FAST | 14,852 | 19.9% |
| LOAD_CONST | 11,980 | 16.0% |
| TO_BOOL_BOOL | 2,318 | 3.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,420 | 99.7% |
| LOAD_FAST | 160 | 0.1% |
| BINARY_SUBSCR | 60 | 0.1% |
| ENTER_EXECUTOR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 108,040 | 99.4% |
| LOAD_CONST | 340 | 0.3% |
| STORE_FAST | 120 | 0.1% |
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
| LOAD_ATTR_INSTANCE_VALUE | 84,040 | 25.9% |
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
| LOAD_FAST | 85,056 | 28.9% |
| LOAD_FAST_LOAD_FAST | 48,620 | 16.5% |
| BINARY_SLICE | 23,960 | 8.2% |
| CALL_BUILTIN_CLASS | 23,960 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 157,086 | 53.4% |
| POP_TOP | 108,260 | 36.8% |
| COPY_FREE_VARS | 25,907 | 8.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,060 | 0.7% |
| CALL_PY_EXACT_ARGS | 467 | 0.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,960 | 29.2% |
| LOAD_FAST | 39,252 | 15.9% |
| CALL | 36,480 | 14.8% |
| LOAD_ATTR_INSTANCE_VALUE | 36,160 | 14.7% |
| LOAD_GLOBAL_MODULE | 13,998 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,500 | 39.2% |
| LOAD_FAST | 36,200 | 14.7% |
| RETURN_VALUE | 35,980 | 14.6% |
| GET_ITER | 29,150 | 11.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,960 | 9.7% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 837,640 | 50.6% |
| LOAD_FAST_LOAD_FAST | 455,120 | 27.5% |
| LOAD_CONST | 289,540 | 17.5% |
| LOAD_GLOBAL_MODULE | 35,920 | 2.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,960 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 814,460 | 49.6% |
| RETURN_VALUE | 454,780 | 27.7% |
| TO_BOOL_BOOL | 132,780 | 8.1% |
| COPY | 107,980 | 6.6% |
| POP_TOP | 59,500 | 3.6% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 191,920 | 58.7% |
| BINARY_OP_SUBTRACT_FLOAT | 59,160 | 18.1% |
| LOAD_ATTR | 38,231 | 11.7% |
| BINARY_OP | 23,960 | 7.3% |
| LOAD_FAST | 12,700 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 144,660 | 44.2% |
| LOAD_FAST | 83,160 | 25.4% |
| LOAD_CONST | 59,980 | 18.3% |
| COPY | 23,160 | 7.1% |
| POP_TOP | 15,151 | 4.6% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 49,040 | 87.2% |
| LOAD_ATTR_INSTANCE_VALUE | 5,818 | 10.3% |
| BUILD_TUPLE | 360 | 0.6% |
| CALL | 220 | 0.4% |
| BINARY_SUBSCR_TUPLE_INT | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 23,920 | 42.5% |
| STORE_FAST | 17,818 | 31.7% |
| BINARY_SUBSCR_DICT | 11,960 | 21.3% |
| POP_TOP | 1,640 | 2.9% |
| RETURN_VALUE | 440 | 0.8% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,129,586 | 54.2% |
| LOAD_GLOBAL_BUILTIN | 437,120 | 21.0% |
| LOAD_ATTR_MODULE | 298,800 | 14.3% |
| BUILD_TUPLE | 157,200 | 7.5% |
| LOAD_ATTR | 59,960 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,878,526 | 90.1% |
| RETURN_VALUE | 144,240 | 6.9% |
| COPY | 35,980 | 1.7% |
| STORE_FAST | 24,060 | 1.2% |
| TO_BOOL | 980 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 649,740 | 65.3% |
| LOAD_ATTR_INSTANCE_VALUE | 320,087 | 32.2% |
| LOAD_GLOBAL_MODULE | 12,080 | 1.2% |
| BINARY_SUBSCR | 12,060 | 1.2% |
| CALL | 640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 296,195 | 29.8% |
| LOAD_FAST | 226,320 | 22.8% |
| LOAD_CONST | 97,380 | 9.8% |
| BINARY_OP_ADD_INT | 83,960 | 8.4% |
| BINARY_OP_SUBTRACT_INT | 60,080 | 6.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,319 | 53.5% |
| BUILD_TUPLE | 65,835 | 25.4% |
| ENTER_EXECUTOR | 29,950 | 11.6% |
| RETURN_VALUE | 24,040 | 9.3% |
| CALL | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120,260 | 46.5% |
| ENTER_EXECUTOR | 100,422 | 38.8% |
| LOAD_FAST | 24,120 | 9.3% |
| NOP | 12,022 | 4.6% |
| JUMP_BACKWARD | 1,840 | 0.7% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 634,620 | 66.2% |
| LOAD_ATTR_METHOD_NO_DICT | 204,040 | 21.3% |
| LOAD_FAST_LOAD_FAST | 72,200 | 7.5% |
| RETURN_VALUE | 24,040 | 2.5% |
| LOAD_FAST | 21,963 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 622,560 | 65.0% |
| CALL_PY_EXACT_ARGS | 108,040 | 11.3% |
| STORE_FAST | 94,383 | 9.8% |
| LOAD_CONST | 71,980 | 7.5% |
| LOAD_FAST | 24,060 | 2.5% |


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
| LOAD_FAST_LOAD_FAST | 14,992 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 267,592 | 37.6% |
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
| LOAD_ATTR | 894,462 | 59.4% |
| LOAD_ATTR_METHOD_NO_DICT | 572,021 | 38.0% |
| LOAD_FAST | 24,040 | 1.6% |
| LOAD_ATTR_METHOD_LAZY_DICT | 11,960 | 0.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 927,531 | 61.6% |
| POP_TOP | 146,251 | 9.7% |
| GET_ITER | 144,140 | 9.6% |
| LOAD_FAST | 72,200 | 4.8% |
| STORE_FAST | 66,723 | 4.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 562,984 | 56.9% |
| BUILD_TUPLE | 191,840 | 19.4% |
| LOAD_ATTR_INSTANCE_VALUE | 84,120 | 8.5% |
| LOAD_CONST | 48,400 | 4.9% |
| CALL | 36,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 815,744 | 82.5% |
| STORE_FAST | 99,486 | 10.1% |
| LOAD_CONST | 24,300 | 2.5% |
| UNPACK_SEQUENCE_TUPLE | 24,080 | 2.4% |
| PUSH_EXC_INFO | 12,105 | 1.2% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 4,479,679 | 41.1% |
| LOAD_FAST | 3,344,509 | 30.7% |
| LOAD_FAST_LOAD_FAST | 660,778 | 6.1% |
| LOAD_CONST | 576,140 | 5.3% |
| LOAD_ATTR | 321,815 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,221,060 | 93.8% |
| COPY_FREE_VARS | 288,531 | 2.6% |
| RETURN_GENERATOR | 264,140 | 2.4% |
| MAKE_CELL | 115,197 | 1.1% |
| TO_BOOL_BOOL | 9,774 | 0.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,100 | 31.5% |
| LOAD_CONST | 143,680 | 22.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 130,189 | 20.1% |
| PUSH_NULL | 72,040 | 11.1% |
| LOAD_ATTR | 35,920 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 634,889 | 98.1% |
| RETURN_GENERATOR | 11,980 | 1.9% |
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
| LOAD_ATTR_SLOT | 330,535 | 93.3% |
| LOAD_FAST | 14,672 | 4.1% |
| LOAD_GLOBAL_MODULE | 8,906 | 2.5% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 330,555 | 93.3% |
| POP_JUMP_IF_FALSE | 23,698 | 6.7% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,710,423 | 50.4% |
| LOAD_ATTR_INSTANCE_VALUE | 947,851 | 27.9% |
| LOAD_ATTR_CLASS | 383,960 | 11.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 119,920 | 3.5% |
| COPY | 108,180 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,663,006 | 78.4% |
| POP_JUMP_IF_TRUE | 708,520 | 20.9% |
| COPY | 24,000 | 0.7% |
| RETURN_VALUE | 100 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 229,200 | 82.5% |
| LOAD_GLOBAL_MODULE | 47,840 | 17.2% |
| COMPARE_OP | 460 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 340 | 0.1% |
| LOAD_FAST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 217,800 | 78.4% |
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
| GET_ITER | 319,425 | 55.7% |
| ENTER_EXECUTOR | 233,768 | 40.8% |
| SWAP | 12,460 | 2.2% |
| JUMP_BACKWARD | 6,459 | 1.1% |
| FOR_ITER | 780 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 195,252 | 34.1% |
| STORE_FAST | 148,320 | 25.9% |
| ENTER_EXECUTOR | 107,660 | 18.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 32,106 | 5.6% |
| RETURN_CONST | 27,314 | 4.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 29,150 | 50.6% |
| ENTER_EXECUTOR | 27,072 | 47.0% |
| JUMP_BACKWARD | 1,260 | 2.2% |
| FOR_ITER | 100 | 0.2% |
| SWAP | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 30,070 | 52.2% |
| LOAD_CONST | 15,032 | 26.1% |
| RETURN_CONST | 12,000 | 20.8% |
| STORE_FAST_LOAD_FAST | 380 | 0.7% |
| LOAD_FAST | 80 | 0.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 73,020 | 72.6% |
| ENTER_EXECUTOR | 13,840 | 13.8% |
| SWAP | 12,460 | 12.4% |
| LOAD_FAST | 700 | 0.7% |
| JUMP_BACKWARD | 420 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,220 | 59.9% |
| STORE_FAST | 13,740 | 13.7% |
| SWAP | 12,480 | 12.4% |
| LOAD_CONST | 12,000 | 11.9% |
| RETURN_CONST | 700 | 0.7% |


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
| LOAD_FAST | 21,842,112 | 86.6% |
| LOAD_FAST_LOAD_FAST | 1,274,671 | 5.1% |
| COPY | 937,196 | 3.7% |
| LOAD_ATTR_INSTANCE_VALUE | 791,180 | 3.1% |
| LOAD_DEREF | 368,853 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,116,224 | 16.3% |
| POP_JUMP_IF_NONE | 3,035,561 | 12.0% |
| RETURN_VALUE | 2,703,031 | 10.7% |
| LOAD_ATTR_METHOD_NO_DICT | 2,256,545 | 8.9% |
| TO_BOOL_BOOL | 2,247,933 | 8.9% |


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
| LOAD_ATTR_INSTANCE_VALUE | 2,256,545 | 52.3% |
| LOAD_FAST | 1,164,196 | 27.0% |
| BINARY_SLICE | 251,960 | 5.8% |
| LOAD_CONST | 132,180 | 3.1% |
| STORE_FAST_LOAD_FAST | 108,560 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,876,866 | 43.5% |
| LOAD_CONST | 813,313 | 18.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 572,021 | 13.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 227,960 | 5.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 204,040 | 4.7% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,011,619 | 67.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,825,373 | 20.6% |
| LOAD_ATTR_SLOT | 589,111 | 6.6% |
| LOAD_DEREF | 123,151 | 1.4% |
| LOAD_FAST_LOAD_FAST | 107,160 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,479,679 | 50.5% |
| LOAD_FAST | 2,852,512 | 32.2% |
| LOAD_FAST_LOAD_FAST | 675,311 | 7.6% |
| LOAD_CONST | 431,980 | 4.9% |
| LOAD_GLOBAL_BUILTIN | 143,180 | 1.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,073,745 | 99.5% |
| LOAD_ATTR_MODULE | 11,960 | 0.4% |
| LOAD_ATTR | 2,940 | 0.1% |
| LOAD_FAST | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,680,262 | 54.4% |
| LOAD_ATTR_CLASS | 455,800 | 14.8% |
| CALL_ISINSTANCE | 298,800 | 9.7% |
| LOAD_GLOBAL_MODULE | 143,800 | 4.7% |
| LOAD_ATTR | 132,240 | 4.3% |


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
| LOAD_FAST | 2,602,324 | 94.2% |
| BINARY_SUBSCR_TUPLE_INT | 120,040 | 4.3% |
| BINARY_SUBSCR_LIST_INT | 20,195 | 0.7% |
| LOAD_DEREF | 11,960 | 0.4% |
| LOAD_ATTR_SLOT | 5,538 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 856,262 | 31.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 589,111 | 21.3% |
| LOAD_FAST | 345,872 | 12.5% |
| COMPARE_OP_FLOAT | 330,535 | 12.0% |
| TO_BOOL_BOOL | 310,783 | 11.3% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 763,677 | 99.9% |
| LOAD_ATTR | 660 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 335,900 | 43.9% |
| LOAD_CONST | 95,960 | 12.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,759 | 10.8% |
| LOAD_ATTR_METHOD_NO_DICT | 59,960 | 7.8% |
| RETURN_VALUE | 35,980 | 4.7% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,790,436 | 40.1% |
| LOAD_FAST | 797,440 | 11.5% |
| POP_JUMP_IF_FALSE | 640,593 | 9.2% |
| STORE_FAST | 476,028 | 6.8% |
| POP_JUMP_IF_TRUE | 449,420 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,145,154 | 73.9% |
| CALL_ISINSTANCE | 437,120 | 6.3% |
| LOAD_DEREF | 401,531 | 5.8% |
| CHECK_EXC_MATCH | 390,724 | 5.6% |
| BUILD_TUPLE | 156,660 | 2.3% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,189,012 | 20.7% |
| RESUME_CHECK | 1,966,828 | 18.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,043,920 | 9.9% |
| POP_JUMP_IF_FALSE | 1,007,465 | 9.5% |
| STORE_ATTR_INSTANCE_VALUE | 785,958 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 3,073,745 | 29.1% |
| LOAD_FAST | 2,138,787 | 20.3% |
| CALL_ISINSTANCE | 1,129,586 | 10.7% |
| LOAD_FAST_LOAD_FAST | 1,093,580 | 10.4% |
| CALL | 571,613 | 5.4% |


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
| CALL_PY_EXACT_ARGS | 10,221,060 | 52.1% |
| CACHE | 5,386,817 | 27.4% |
| COPY_FREE_VARS | 732,500 | 3.7% |
| CALL_PY_WITH_DEFAULTS | 634,889 | 3.2% |
| BINARY_SUBSCR_GETITEM | 420,520 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,423,647 | 58.2% |
| LOAD_GLOBAL_BUILTIN | 2,790,436 | 14.2% |
| LOAD_GLOBAL_MODULE | 1,966,828 | 10.0% |
| NOP | 1,203,182 | 6.1% |
| LOAD_CONST | 652,191 | 3.3% |


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
| LOAD_FAST | 4,942,874 | 60.8% |
| LOAD_FAST_LOAD_FAST | 1,992,600 | 24.5% |
| SWAP | 937,196 | 11.5% |
| LOAD_DEREF | 155,680 | 1.9% |
| STORE_FAST_LOAD_FAST | 83,920 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,819,709 | 34.7% |
| LOAD_CONST | 1,679,189 | 20.6% |
| LOAD_FAST_LOAD_FAST | 997,280 | 12.3% |
| LOAD_GLOBAL_MODULE | 785,958 | 9.7% |
| RETURN_CONST | 760,772 | 9.4% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,798,384 | 49.8% |
| LOAD_FAST | 1,796,754 | 49.8% |
| STORE_ATTR_SLOT | 12,915 | 0.4% |
| STORE_ATTR | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,304,433 | 36.1% |
| LOAD_CONST | 1,048,122 | 29.0% |
| LOAD_FAST | 619,149 | 17.2% |
| RETURN_CONST | 613,331 | 17.0% |
| STORE_ATTR_SLOT | 12,915 | 0.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,879 | 79.4% |
| LOAD_FAST_LOAD_FAST | 11,960 | 20.3% |
| STORE_ATTR_INSTANCE_VALUE | 100 | 0.2% |
| STORE_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,920 | 81.2% |
| RETURN_CONST | 10,999 | 18.6% |
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
| ENTER_EXECUTOR | 60 | 25.0% |
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
| LOAD_ATTR_INSTANCE_VALUE | 2,247,933 | 25.7% |
| RETURN_VALUE | 1,899,071 | 21.7% |
| CALL_ISINSTANCE | 1,878,526 | 21.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 927,531 | 10.6% |
| LOAD_FAST | 390,222 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,383,229 | 73.0% |
| POP_JUMP_IF_TRUE | 2,230,475 | 25.5% |
| EXTENDED_ARG | 119,920 | 1.4% |
| UNARY_NOT | 11,980 | 0.1% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 315,299 | 40.3% |
| BINARY_OP | 291,014 | 37.2% |
| COPY | 163,126 | 20.8% |
| LOAD_ATTR | 11,960 | 1.5% |
| TO_BOOL | 600 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 530,438 | 67.8% |
| POP_JUMP_IF_TRUE | 251,789 | 32.2% |
| TO_BOOL_NONE | 112 | 0.0% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 143,807 | 99.0% |
| LOAD_FAST | 720 | 0.5% |
| STORE_FAST_LOAD_FAST | 540 | 0.4% |
| TO_BOOL | 200 | 0.1% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 144,287 | 99.3% |
| POP_JUMP_IF_TRUE | 940 | 0.6% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 856,262 | 57.4% |
| LOAD_FAST | 262,438 | 17.6% |
| COPY | 190,721 | 12.8% |
| LOAD_ATTR | 83,800 | 5.6% |
| LOAD_ATTR_INSTANCE_VALUE | 72,040 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,287,582 | 86.3% |
| POP_JUMP_IF_TRUE | 203,853 | 13.7% |
| TO_BOOL | 200 | 0.0% |
| TO_BOOL_STR | 120 | 0.0% |
| TO_BOOL_INT | 100 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 229,060 | 79.1% |
| COPY | 36,180 | 12.5% |
| LOAD_ATTR | 11,960 | 4.1% |
| CALL_BUILTIN_FAST | 5,740 | 2.0% |
| ENTER_EXECUTOR | 5,640 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 240,700 | 83.1% |
| POP_JUMP_IF_FALSE | 48,700 | 16.8% |
| TO_BOOL_NONE | 100 | 0.0% |


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
| BINARY_SUBSCR | 180,200 | 27.9% |
| RETURN_VALUE | 156,480 | 24.2% |
| YIELD_VALUE | 107,960 | 16.7% |
| STORE_FAST | 58,043 | 9.0% |
| BINARY_SUBSCR_DICT | 37,998 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 633,707 | 98.1% |
| LOAD_FAST | 12,040 | 1.9% |
| STORE_FAST | 340 | 0.1% |
| STORE_DEREF | 20 | 0.0% |


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
|     deferred | 1,100,741 | 31.4% |
|          hit | 2,393,349 | 68.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 960 | 10.9% |
| Failure | 7,838 | 89.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,496 | 44.6% |
| add other | 1,420 | 18.1% |
| or | 1,260 | 16.1% |
| remainder | 880 | 11.2% |
| add different types | 441 | 5.6% |
| floor divide | 180 | 2.3% |
| true divide other | 140 | 1.8% |
| multiply different types | 21 | 0.3% |


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
|     deferred | 339,100 | 16.5% |
|          hit | 1,713,743 | 83.3% |
|         miss | 120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,000 | 26.9% |
| Failure | 2,720 | 73.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 2,400 | 88.2% |
| other | 160 | 5.9% |
| out of range | 160 | 5.9% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,244,185 | 22.1% |
|          hit | 21,972,879 | 77.7% |
|         miss | 368,558 | 1.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,688 | 42.7% |
| Failure | 30,421 | 57.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 6,377 | 21.0% |
| class no vectorcall | 5,500 | 18.1% |
| meth descr method fastcall keywords | 3,860 | 12.7% |
| cfunc noargs | 3,257 | 10.7% |
| meth descr varargs | 3,025 | 9.9% |
| other | 1,757 | 5.8% |
| class mutable | 1,460 | 4.8% |
| meth descr varargs keywords | 1,185 | 3.9% |
| cfunc varargs keywords | 1,120 | 3.7% |
| no dict | 820 | 2.7% |
| init not simple | 680 | 2.2% |
| cfunc varargs | 520 | 1.7% |
| operator wrapper | 500 | 1.6% |
| wrong number arguments | 180 | 0.6% |
| cmethod | 160 | 0.5% |
| init not python | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 173,486 | 4.1% |
|          hit | 4,027,694 | 95.8% |
|         miss | 205 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,960 | 52.6% |
| Failure | 1,763 | 47.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 480 | 27.2% |
| bytes | 360 | 20.4% |
| other | 340 | 19.3% |
| tuple | 180 | 10.2% |
| big int | 160 | 9.1% |
| float long | 143 | 8.1% |
| baseobject | 60 | 3.4% |
| bool | 40 | 2.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 198,952 | 16.4% |
|          hit | 1,007,414 | 83.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,020 | 31.9% |
| Failure | 2,180 | 68.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 1,300 | 59.6% |
| set | 220 | 10.1% |
| dict keys | 200 | 9.2% |
| other | 180 | 8.3% |
| bytes | 120 | 5.5% |
| ascii string | 120 | 5.5% |
| enumerate | 40 | 1.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,971,373 | 11.5% |
|          hit | 45,828,120 | 88.3% |
|         miss | 462,818 | 0.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 37,553 | 50.0% |
| Failure | 37,529 | 50.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 8,180 | 21.8% |
| method | 8,079 | 21.5% |
| not managed dict | 7,104 | 18.9% |
| not in keys | 6,880 | 18.3% |
| shadowed | 1,786 | 4.8% |
| module attr not found | 1,600 | 4.3% |
| non overriding descriptor | 1,220 | 3.3% |
| metaclass attribute | 920 | 2.5% |
| class attr descriptor | 540 | 1.4% |
| class method obj | 460 | 1.2% |
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
|     deferred | 20,840 | 0.1% |
|        deopt | 980 | 0.0% |
|          hit | 17,508,656 | 99.8% |
|         miss | 6,340 | 0.0% |

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
|     deferred | 966,351 | 8.0% |
|          hit | 11,096,916 | 91.8% |
|         miss | 702,526 | 5.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 21,175 | 83.4% |
| Failure | 4,200 | 16.6% |

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
|     deferred | 217,000 | 27.7% |
|          hit | 565,320 | 72.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 17.9% |
| Failure | 1,740 | 82.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 1,420 | 81.6% |
| dict subclass no override | 320 | 18.4% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,293,177 | 10.1% |
|          hit | 11,468,112 | 89.8% |
|         miss | 34,793 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,934 | 56.5% |
| Failure | 6,100 | 43.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 1,900 | 31.1% |
| bytes | 1,136 | 18.6% |
| float | 960 | 15.7% |
| dict | 620 | 10.2% |
| mapping | 524 | 8.6% |
| bytearray | 420 | 6.9% |
| tuple | 360 | 5.9% |
| set | 180 | 3.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,920 | 1.5% |
|          hit | 850,347 | 98.4% |

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
| Basic | 176,776,041 | 49.4% |
| Not specialized | 41,241,044 | 11.5% |
| Specialized hits | 138,481,990 | 38.7% |
| Specialized misses | 1,576,227 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 6,244,185 | 37.0% |
| LOAD_ATTR | 5,971,373 | 35.4% |
| TO_BOOL | 1,293,177 | 7.7% |
| BINARY_OP | 1,100,741 | 6.5% |
| STORE_ATTR | 966,351 | 5.7% |
| BINARY_SUBSCR | 339,100 | 2.0% |
| SEND | 336,200 | 2.0% |
| STORE_SUBSCR | 217,000 | 1.3% |
| FOR_ITER | 198,952 | 1.2% |
| COMPARE_OP | 173,486 | 1.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 690,905 | 43.8% |
| LOAD_ATTR_SLOT | 296,086 | 18.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 136,610 | 8.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 124,818 | 7.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,422 | 5.2% |
| CALL_PY_EXACT_ARGS | 70,050 | 4.4% |
| CALL_METHOD_DESCRIPTOR_O | 36,840 | 2.3% |
| LOAD_ATTR_METHOD_NO_DICT | 36,187 | 2.3% |
| TO_BOOL_NONE | 22,317 | 1.4% |
| LOAD_ATTR_INSTANCE_VALUE | 19,483 | 1.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 5,748,699 | 29.0% |
| Calls to Python functions inlined | 14,098,083 | 71.0% |
| Calls via PyEval_EvalFrame (total) | 5,748,699 | 29.0% |
| Calls via PyEval_EvalFrame (vector) | 5,398,119 | 27.2% |
| Calls via PyEval_EvalFrame (generator) | 350,580 | 1.8% |
| Calls via PyEval_EvalFrame (legacy) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 5,397,819 | 27.2% |
| Calls via PyEval_EvalFrame (build class) | 220 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,093,075 | 5.5% |
| Calls via PyEval_EvalFrame (function ex) | 132,520 | 0.7% |
| Calls via PyEval_EvalFrame (api) | 206,300 | 1.0% |
| Calls via PyEval_EvalFrame (method) | 915,711 | 4.6% |
| Frame objects created | 751,949 | 3.8% |
| Frames pushed | 13,458,752 | 67.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 11,559,199 | 40.1% |
| Frees to freelist | 11,612,893 |  |
| Allocations | 17,276,380 | 59.9% |
| Allocations to 512 bytes | 16,952,284 | 58.8% |
| Allocations to 4 kbytes | 90,931 | 0.3% |
| Allocations over 4 kbytes | 233,165 | 0.8% |
| Frees | 17,534,955 |  |
| New values | 158,420 |  |
| Interpreter increfs | 187,023,411 | 77.6% |
| Interpreter decrefs | 202,641,098 | 75.6% |
| Increfs | 54,026,509 | 22.4% |
| Decrefs | 65,455,377 | 24.4% |
| Materialize dict (on request) | 200 | 0.1% |
| Materialize dict (new key) | 24,000 | 15.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 140 | 0.1% |
| Method cache hits | 10,442,338 |  |
| Method cache misses | 255,961 |  |
| Method cache collisions | 268,027 |  |
| Method cache dunder hits | 6,895,319 |  |
| Method cache dunder misses | 17,586 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 1,104 | 1,920 | 12,297,842 |
| 1 | 104 | 22 | 3,644,904 |
| 2 | 1 | 33 | 306,240 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 1,080 |  |
| Traces created | 720 | 66.7% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 360 | 33.3% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 1 | 0.1% |
| Traces executed | 1,355,234 |  |
| Uops executed | 50,399,958 | 37.19 |

### Trace length histogram

<details>
<summary> trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 0 | 0.0% |
| <= 16 | 20 | 2.8% |
| <= 32 | 320 | 44.4% |
| <= 64 | 200 | 27.8% |
| <= 128 | 140 | 19.4% |
| <= 256 | 40 | 5.6% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 100 | 13.9% |
| <= 16 | 280 | 38.9% |
| <= 32 | 160 | 22.2% |
| <= 64 | 100 | 13.9% |
| <= 128 | 80 | 11.1% |


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 40 | 0.0% |
| <= 2 | 224,340 | 16.6% |
| <= 4 | 27,072 | 2.0% |
| <= 8 | 26,011 | 1.9% |
| <= 16 | 277,118 | 20.4% |
| <= 32 | 162,634 | 12.0% |
| <= 64 | 92,430 | 6.8% |
| <= 128 | 541,988 | 40.0% |
| <= 256 | 1,834 | 0.1% |
| <= 512 | 1,311 | 0.1% |
| <= 1,024 | 291 | 0.0% |
| <= 2,048 | 165 | 0.0% |


</details>

### Uop execution stats

<details>
<summary> uop execution stats </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| _SET_IP | 6,252,588 | 12.4% | 12.4% |  |
| _CHECK_VALIDITY | 5,875,191 | 11.7% | 24.1% |  |
| LOAD_FAST | 5,497,622 | 10.9% | 35.0% |  |
| _GUARD_TYPE_VERSION | 4,522,888 | 9.0% | 43.9% |  |
| STORE_FAST | 2,286,144 | 4.5% | 48.5% |  |
| _LOAD_ATTR_SLOT | 1,554,334 | 3.1% | 51.6% |  |
| _CHECK_MANAGED_OBJECT_HAS_VALUES | 1,538,898 | 3.1% | 54.6% |  |
| _LOAD_ATTR_INSTANCE_VALUE | 1,538,898 | 3.1% | 57.7% |  |
| _GUARD_IS_FALSE_POP | 1,228,094 | 2.4% | 60.1% | 4.7% |
| _LOAD_ATTR_METHOD_NO_DICT | 1,110,919 | 2.2% | 62.3% |  |
| TO_BOOL_BOOL | 1,086,414 | 2.2% | 64.5% |  |
| _EXIT_TRACE | 917,062 | 1.8% | 66.3% | 100.0% |
| _GUARD_GLOBALS_VERSION | 879,610 | 1.7% | 68.0% | 0.1% |
| _LOAD_CONST_INLINE_BORROW | 757,070 | 1.5% | 69.5% |  |
| _ITER_CHECK_LIST | 734,195 | 1.5% | 71.0% | 0.0% |
| _GUARD_NOT_EXHAUSTED_LIST | 734,155 | 1.5% | 72.4% | 31.9% |
| _CHECK_FUNCTION_EXACT_ARGS | 634,137 | 1.3% | 73.7% |  |
| _CHECK_STACK_SPACE | 634,137 | 1.3% | 75.0% |  |
| _INIT_CALL_PY_EXACT_ARGS | 634,137 | 1.3% | 76.2% |  |
| _PUSH_FRAME | 634,137 | 1.3% | 77.5% |  |
| _SAVE_RETURN_OFFSET | 634,137 | 1.3% | 78.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 561,008 | 1.1% | 79.9% |  |
| _LOAD_ATTR | 547,480 | 1.1% | 80.9% |  |
| RESUME_CHECK | 504,724 | 1.0% | 81.9% |  |
| _ITER_NEXT_LIST | 500,247 | 1.0% | 82.9% |  |
| _GUARD_NOT_EXHAUSTED_RANGE | 462,522 | 0.9% | 83.9% | 5.9% |
| _ITER_CHECK_RANGE | 462,522 | 0.9% | 84.8% |  |
| _GUARD_BUILTINS_VERSION | 442,600 | 0.9% | 85.6% |  |
| _LOAD_GLOBAL_BUILTINS | 442,600 | 0.9% | 86.5% |  |
| _LOAD_GLOBAL_MODULE | 435,750 | 0.9% | 87.4% |  |
| _ITER_NEXT_RANGE | 435,450 | 0.9% | 88.3% |  |
| _GUARD_IS_TRUE_POP | 398,323 | 0.8% | 89.0% | 10.1% |
| PUSH_NULL | 385,852 | 0.8% | 89.8% |  |
| BUILD_LIST | 364,270 | 0.7% | 90.5% |  |
| CALL_INTRINSIC_1 | 364,270 | 0.7% | 91.3% |  |
| LIST_EXTEND | 364,270 | 0.7% | 92.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 258,364 | 0.5% | 92.5% |  |
| _JUMP_TO_TOP | 240,129 | 0.5% | 93.0% |  |
| _LOAD_CONST_INLINE | 229,732 | 0.5% | 93.4% |  |
| _GUARD_DORV_VALUES_INST_ATTR_FROM_DICT | 197,767 | 0.4% | 93.8% |  |
| _GUARD_KEYS_VERSION | 197,767 | 0.4% | 94.2% |  |
| _LOAD_ATTR_METHOD_WITH_VALUES | 197,767 | 0.4% | 94.6% |  |
| POP_TOP | 187,408 | 0.4% | 95.0% |  |
| TO_BOOL_INT | 163,956 | 0.3% | 95.3% |  |
| _FOR_ITER_TIER_TWO | 155,460 | 0.3% | 95.6% | 24.9% |
| CALL_ISINSTANCE | 143,220 | 0.3% | 95.9% |  |
| BUILD_TUPLE | 141,796 | 0.3% | 96.2% |  |
| COMPARE_OP_INT | 131,560 | 0.3% | 96.4% |  |
| _TO_BOOL | 113,968 | 0.2% | 96.7% |  |
| CONTAINS_OP | 108,380 | 0.2% | 96.9% |  |
| CALL_LEN | 107,620 | 0.2% | 97.1% |  |
| _BINARY_OP | 91,487 | 0.2% | 97.3% |  |
| COPY | 86,329 | 0.2% | 97.4% |  |
| GET_ITER | 83,800 | 0.2% | 97.6% |  |
| _BINARY_SUBSCR | 83,680 | 0.2% | 97.8% |  |
| _GUARD_DORV_VALUES | 78,111 | 0.2% | 97.9% |  |
| _STORE_ATTR_INSTANCE_VALUE | 78,111 | 0.2% | 98.1% |  |
| _GUARD_IS_NOT_NONE_POP | 77,541 | 0.2% | 98.2% | 0.1% |
| SWAP | 75,290 | 0.1% | 98.4% |  |
| _GUARD_NOT_EXHAUSTED_TUPLE | 63,700 | 0.1% | 98.5% | 21.7% |
| _ITER_CHECK_TUPLE | 63,700 | 0.1% | 98.6% |  |
| LOAD_FAST_CHECK | 56,489 | 0.1% | 98.7% |  |
| CALL_METHOD_DESCRIPTOR_O | 56,489 | 0.1% | 98.9% |  |
| _CHECK_ATTR_MODULE | 51,350 | 0.1% | 99.0% |  |
| _LOAD_ATTR_MODULE | 51,350 | 0.1% | 99.1% |  |
| _ITER_NEXT_TUPLE | 49,860 | 0.1% | 99.2% |  |
| CALL_BUILTIN_FAST | 48,540 | 0.1% | 99.3% |  |
| TO_BOOL_NONE | 47,740 | 0.1% | 99.4% | 25.0% |
| MAKE_CELL | 44,534 | 0.1% | 99.4% |  |
| _STORE_ATTR_SLOT | 42,859 | 0.1% | 99.5% |  |
| LOAD_DEREF | 35,000 | 0.1% | 99.6% |  |
| BINARY_SUBSCR_LIST_INT | 32,942 | 0.1% | 99.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 30,948 | 0.1% | 99.7% |  |
| BINARY_SUBSCR_DICT | 23,780 | 0.0% | 99.8% |  |
| _STORE_SUBSCR | 23,780 | 0.0% | 99.8% |  |
| _GUARD_NOS_INT | 21,502 | 0.0% | 99.9% |  |
| TO_BOOL_LIST | 21,362 | 0.0% | 99.9% |  |
| CALL_BUILTIN_O | 21,342 | 0.0% | 99.9% |  |
| _BINARY_OP_SUBTRACT_INT | 21,342 | 0.0% | 100.0% |  |
| _GUARD_IS_NONE_POP | 1,411 | 0.0% | 100.0% | 100.0% |
| LIST_APPEND | 660 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 660 | 0.0% | 100.0% |  |
| IS_OP | 580 | 0.0% | 100.0% |  |
| _BINARY_OP_ADD_INT | 300 | 0.0% | 100.0% |  |
| _POP_FRAME | 280 | 0.0% | 100.0% |  |
| _GUARD_BOTH_UNICODE | 240 | 0.0% | 100.0% |  |
| _BINARY_OP_ADD_UNICODE | 240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 220 | 0.0% | 100.0% | 27.3% |
| _CHECK_CALL_BOUND_METHOD_EXACT_ARGS | 220 | 0.0% | 100.0% |  |
| _INIT_CALL_BOUND_METHOD_EXACT_ARGS | 220 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 160 | 0.0% | 100.0% |  |
| _GUARD_BOTH_INT | 140 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 40 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 40 | 0.0% | 100.0% |  |
| STORE_DEREF | 40 | 0.0% | 100.0% |  |


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>

|Opcode | Count | 
|---|---:|
| FOR_ITER_GEN | 360 |
| CALL | 160 |
| CALL_LIST_APPEND | 102 |
| YIELD_VALUE | 60 |
| CALL_FUNCTION_EX | 20 |
| CALL_KW | 20 |
| CALL_ALLOC_AND_ENTER_INIT | 20 |


</details>


</details>

## Rare events

<details>
<summary> Counts of rare/unlikely events </summary>

|Event | Count | 
|---|---:|
| set_class | 0 |
| set_bases | 0 |
| set_eval_frame_func | 0 |
| builtin_dict | 0 |
| func_modification | 0 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-02-01
