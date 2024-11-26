
# Pystats results

- benchmark: asyncio_tcp
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 88,612,957 | 21.3% | 21.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 30,288,647 | 7.3% | 28.6% |  |
| RESUME_CHECK | 21,538,724 | 5.2% | 33.8% | 0.0% |
| STORE_FAST | 19,671,441 | 4.7% | 38.5% |  |
| POP_JUMP_IF_FALSE | 18,122,068 | 4.4% | 42.9% |  |
| CALL_PY_EXACT_ARGS | 15,912,247 | 3.8% | 46.7% |  |
| LOAD_CONST | 14,516,410 | 3.5% | 50.2% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,970,449 | 3.4% | 53.6% |  |
| TO_BOOL_BOOL | 13,174,292 | 3.2% | 56.8% |  |
| POP_TOP | 12,845,410 | 3.1% | 59.8% |  |
| RETURN_VALUE | 12,549,568 | 3.0% | 62.9% |  |
| LOAD_GLOBAL_MODULE | 8,508,723 | 2.0% | 64.9% |  |
| LOAD_FAST_LOAD_FAST | 8,097,597 | 1.9% | 66.9% |  |
| RETURN_CONST | 7,763,421 | 1.9% | 68.7% |  |
| LOAD_GLOBAL_BUILTIN | 7,687,112 | 1.9% | 70.6% | 0.0% |
| POP_JUMP_IF_TRUE | 6,723,752 | 1.6% | 72.2% |  |
| LOAD_ATTR_SLOT | 6,708,025 | 1.6% | 73.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 6,172,255 | 1.5% | 75.3% |  |
| STORE_ATTR_SLOT | 5,612,550 | 1.4% | 76.7% |  |
| LOAD_ATTR | 5,521,804 | 1.3% | 78.0% |  |
| NOP | 4,959,866 | 1.2% | 79.2% |  |
| CALL | 4,373,253 | 1.1% | 80.2% |  |
| BINARY_OP | 4,230,682 | 1.0% | 81.2% |  |
| TO_BOOL_INT | 4,210,415 | 1.0% | 82.3% |  |
| COMPARE_OP_INT | 3,711,533 | 0.9% | 83.2% |  |
| LOAD_ATTR_MODULE | 3,421,651 | 0.8% | 84.0% |  |
| PUSH_NULL | 3,026,937 | 0.7% | 84.7% |  |
| CALL_LEN | 2,952,894 | 0.7% | 85.4% |  |
| COPY | 2,701,666 | 0.7% | 86.1% |  |
| INTERPRETER_EXIT | 2,666,634 | 0.6% | 86.7% |  |
| JUMP_FORWARD | 2,613,976 | 0.6% | 87.3% |  |
| TO_BOOL | 2,436,662 | 0.6% | 87.9% |  |
| POP_JUMP_IF_NOT_NONE | 2,334,832 | 0.6% | 88.5% |  |
| POP_JUMP_IF_NONE | 2,287,647 | 0.6% | 89.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 2,268,620 | 0.5% | 89.6% |  |
| FOR_ITER_LIST | 2,030,490 | 0.5% | 90.1% |  |
| GET_ITER | 1,933,300 | 0.5% | 90.5% |  |
| SEND_GEN | 1,636,500 | 0.4% | 90.9% |  |
| BUILD_LIST | 1,604,500 | 0.4% | 91.3% |  |
| TO_BOOL_LIST | 1,595,520 | 0.4% | 91.7% |  |
| STORE_FAST_STORE_FAST | 1,457,373 | 0.4% | 92.1% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,456,933 | 0.4% | 92.4% |  |
| ENTER_EXECUTOR | 1,411,830 | 0.3% | 92.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,350,443 | 0.3% | 93.1% |  |
| CALL_ISINSTANCE | 1,315,156 | 0.3% | 93.4% |  |
| YIELD_VALUE | 1,307,680 | 0.3% | 93.7% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,307,600 | 0.3% | 94.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,297,738 | 0.3% | 94.3% |  |
| FOR_ITER_RANGE | 1,283,340 | 0.3% | 94.6% |  |
| UNARY_NOT | 1,280,160 | 0.3% | 94.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 1,094,161 | 0.3% | 95.2% | 0.0% |
| BUILD_TUPLE | 1,032,403 | 0.2% | 95.5% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,025,756 | 0.2% | 95.7% | 0.1% |
| CALL_FUNCTION_EX | 1,024,505 | 0.2% | 95.9% |  |
| JUMP_BACKWARD | 1,017,196 | 0.2% | 96.2% |  |
| END_SEND | 987,040 | 0.2% | 96.4% |  |
| GET_AWAITABLE | 987,040 | 0.2% | 96.7% |  |
| CALL_INTRINSIC_1 | 961,780 | 0.2% | 96.9% |  |
| LIST_EXTEND | 961,780 | 0.2% | 97.1% |  |
| LOAD_DEREF | 727,350 | 0.2% | 97.3% |  |
| CALL_BUILTIN_CLASS | 719,203 | 0.2% | 97.5% |  |
| SWAP | 711,063 | 0.2% | 97.6% |  |
| COPY_FREE_VARS | 691,634 | 0.2% | 97.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 664,407 | 0.2% | 98.0% |  |
| TO_BOOL_NONE | 662,360 | 0.2% | 98.1% |  |
| SEND | 659,240 | 0.2% | 98.3% |  |
| RETURN_GENERATOR | 658,640 | 0.2% | 98.5% |  |
| CALL_PY_WITH_DEFAULTS | 657,818 | 0.2% | 98.6% |  |
| UNARY_INVERT | 648,549 | 0.2% | 98.8% |  |
| LOAD_SUPER_ATTR_METHOD | 642,480 | 0.2% | 98.9% |  |
| BINARY_OP_ADD_FLOAT | 641,260 | 0.2% | 99.1% |  |
| CALL_LIST_APPEND | 373,765 | 0.1% | 99.2% |  |
| BINARY_SLICE | 373,705 | 0.1% | 99.3% |  |
| CALL_KW | 346,938 | 0.1% | 99.3% |  |
| STORE_SUBSCR_DICT | 336,638 | 0.1% | 99.4% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 336,098 | 0.1% | 99.5% |  |
| CONTAINS_OP | 321,520 | 0.1% | 99.6% |  |
| LOAD_ATTR_PROPERTY | 321,140 | 0.1% | 99.7% |  |
| BINARY_OP_ADD_INT | 320,600 | 0.1% | 99.7% |  |
| DELETE_SUBSCR | 320,320 | 0.1% | 99.8% |  |
| BUILD_SLICE | 320,320 | 0.1% | 99.9% |  |
| BINARY_OP_MULTIPLY_INT | 320,280 | 0.1% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60,885 | 0.0% | 100.0% |  |
| COMPARE_OP | 19,098 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 16,958 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 9,620 | 0.0% | 100.0% |  |
| FOR_ITER | 9,540 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 8,100 | 0.0% | 100.0% |  |
| STORE_ATTR | 7,500 | 0.0% | 100.0% |  |
| RESUME | 4,340 | 0.0% | 100.0% | 0.5% |
| MAKE_CELL | 1,440 | 0.0% | 100.0% |  |
| IS_OP | 1,360 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 940 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 900 | 0.0% | 100.0% |  |
| STORE_DEREF | 880 | 0.0% | 100.0% |  |
| BUILD_MAP | 800 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 680 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 680 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 680 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 660 | 0.0% | 100.0% |  |
| POP_EXCEPT | 660 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 660 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 560 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 560 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 500 | 0.0% | 100.0% |  |
| BUILD_SET | 400 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 380 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 320 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 320 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 240 | 0.0% | 100.0% | 25.0% |
| DICT_MERGE | 240 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 240 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 200 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 180 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 160 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 80 | 0.0% | 100.0% |  |
| LIST_APPEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 60 | 0.0% | 100.0% |  |
| BEFORE_WITH | 40 | 0.0% | 100.0% |  |
| IMPORT_FROM | 20 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 20 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 20 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 29,289,891 | 7.0% | 7.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 14,917,249 | 3.6% | 10.6% |
| RESUME_CHECK LOAD_FAST | 13,586,146 | 3.3% | 13.9% |
| STORE_FAST LOAD_FAST | 11,887,899 | 2.9% | 16.8% |
| POP_JUMP_IF_FALSE LOAD_FAST | 9,753,478 | 2.3% | 19.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,925,578 | 2.1% | 21.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 7,681,729 | 1.8% | 23.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 7,070,641 | 1.7% | 24.8% |
| LOAD_FAST LOAD_ATTR_SLOT | 6,699,145 | 1.6% | 26.4% |
| RETURN_CONST POP_TOP | 6,389,147 | 1.5% | 28.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 6,269,242 | 1.5% | 29.5% |
| LOAD_CONST LOAD_FAST | 5,883,954 | 1.4% | 30.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 5,834,027 | 1.4% | 32.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 5,618,662 | 1.4% | 33.6% |
| POP_TOP LOAD_FAST | 5,334,673 | 1.3% | 34.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,284,746 | 1.3% | 36.2% |
| LOAD_FAST RETURN_VALUE | 4,593,659 | 1.1% | 37.3% |
| LOAD_FAST LOAD_ATTR | 4,510,108 | 1.1% | 38.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 3,964,921 | 1.0% | 39.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 3,956,294 | 1.0% | 40.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 3,776,685 | 0.9% | 41.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 3,753,418 | 0.9% | 42.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,711,273 | 0.9% | 43.0% |
| LOAD_CONST STORE_FAST | 3,646,999 | 0.9% | 43.9% |
| NOP LOAD_FAST | 3,645,590 | 0.9% | 44.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 3,613,745 | 0.9% | 45.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,419,631 | 0.8% | 46.5% |
| RETURN_VALUE STORE_FAST | 3,303,632 | 0.8% | 47.3% |
| LOAD_FAST LOAD_CONST | 3,279,783 | 0.8% | 48.0% |
| RETURN_VALUE TO_BOOL_BOOL | 3,259,447 | 0.8% | 48.8% |
| LOAD_FAST STORE_ATTR_SLOT | 2,977,334 | 0.7% | 49.5% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,968,694 | 0.7% | 50.3% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 2,867,461 | 0.7% | 50.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,772,233 | 0.7% | 51.6% |
| POP_TOP RETURN_CONST | 2,721,450 | 0.7% | 52.3% |
| CACHE RESUME_CHECK | 2,663,974 | 0.6% | 52.9% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,658,821 | 0.6% | 53.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 2,634,756 | 0.6% | 54.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 2,563,800 | 0.6% | 54.8% |
| TO_BOOL POP_JUMP_IF_TRUE | 2,411,344 | 0.6% | 55.4% |
| POP_JUMP_IF_FALSE LOAD_CONST | 2,310,356 | 0.6% | 55.9% |
| STORE_FAST JUMP_FORWARD | 2,292,356 | 0.6% | 56.5% |
| RESUME_CHECK NOP | 2,292,014 | 0.6% | 57.0% |
| LOAD_CONST COMPARE_OP_INT | 2,284,036 | 0.5% | 57.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,263,420 | 0.5% | 58.1% |
| COPY TO_BOOL_INT | 2,060,086 | 0.5% | 58.6% |
| LOAD_GLOBAL_MODULE BINARY_OP | 2,059,706 | 0.5% | 59.1% |
| CALL STORE_FAST | 2,027,070 | 0.5% | 59.6% |
| LOAD_ATTR_MODULE PUSH_NULL | 2,014,163 | 0.5% | 60.1% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,013,112 | 0.5% | 60.6% |
| POP_TOP LOAD_CONST | 2,002,903 | 0.5% | 61.1% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 1,975,727 | 0.5% | 61.5% |
| JUMP_FORWARD LOAD_FAST | 1,972,036 | 0.5% | 62.0% |
| POP_JUMP_IF_NONE LOAD_FAST | 1,964,527 | 0.5% | 62.5% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 1,962,876 | 0.5% | 63.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,832,109 | 0.4% | 63.4% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 1,777,264 | 0.4% | 63.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST | 1,732,297 | 0.4% | 64.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 1,682,883 | 0.4% | 64.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,675,165 | 0.4% | 65.1% |
| STORE_ATTR_SLOT LOAD_CONST | 1,645,787 | 0.4% | 65.5% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,634,776 | 0.4% | 65.8% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 1,595,340 | 0.4% | 66.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 1,595,220 | 0.4% | 66.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,456,813 | 0.4% | 67.0% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,456,573 | 0.4% | 67.3% |
| BINARY_OP COPY | 1,419,086 | 0.3% | 67.7% |
| LOAD_ATTR LOAD_FAST | 1,370,181 | 0.3% | 68.0% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,369,652 | 0.3% | 68.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,366,581 | 0.3% | 68.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 1,361,303 | 0.3% | 69.0% |
| LOAD_FAST TO_BOOL | 1,359,352 | 0.3% | 69.3% |
| POP_JUMP_IF_FALSE POP_TOP | 1,358,212 | 0.3% | 69.6% |
| STORE_FAST RETURN_CONST | 1,345,145 | 0.3% | 69.9% |
| TO_BOOL_INT POP_JUMP_IF_TRUE | 1,342,894 | 0.3% | 70.3% |
| CALL RETURN_VALUE | 1,336,225 | 0.3% | 70.6% |
| CALL_LEN STORE_FAST | 1,335,496 | 0.3% | 70.9% |
| RETURN_VALUE RETURN_VALUE | 1,314,976 | 0.3% | 71.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,314,896 | 0.3% | 71.5% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 1,314,176 | 0.3% | 71.9% |
| POP_JUMP_IF_TRUE LOAD_CONST | 1,313,509 | 0.3% | 72.2% |
| LOAD_FAST STORE_FAST | 1,313,496 | 0.3% | 72.5% |
| NOP LOAD_GLOBAL_MODULE | 1,313,436 | 0.3% | 72.8% |
| LOAD_FAST POP_JUMP_IF_NONE | 1,308,938 | 0.3% | 73.1% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 1,307,040 | 0.3% | 73.4% |
| RETURN_VALUE INTERPRETER_EXIT | 1,300,760 | 0.3% | 73.8% |
| STORE_FAST NOP | 1,298,938 | 0.3% | 74.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 1,298,920 | 0.3% | 74.4% |
| LOAD_FAST GET_ITER | 1,283,460 | 0.3% | 74.7% |
| GET_ITER FOR_ITER_LIST | 1,283,080 | 0.3% | 75.0% |
| TO_BOOL_BOOL UNARY_NOT | 1,280,020 | 0.3% | 75.3% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 1,094,081 | 0.3% | 75.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 1,069,270 | 0.3% | 75.8% |
| BINARY_OP TO_BOOL_INT | 1,067,130 | 0.3% | 76.1% |
| PUSH_NULL LOAD_FAST | 1,057,841 | 0.3% | 76.3% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 1,048,225 | 0.3% | 76.6% |
| BINARY_OP STORE_FAST | 1,038,152 | 0.2% | 76.8% |
| RETURN_CONST INTERPRETER_EXIT | 1,036,514 | 0.2% | 77.1% |
| CALL_FUNCTION_EX POP_TOP | 1,023,945 | 0.2% | 77.3% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 1,015,145 | 0.2% | 77.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,320 | 85.7% |
| LOAD_CONST | 53,385 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 320,360 | 85.7% |
| CALL_METHOD_DESCRIPTOR_O | 44,956 | 12.0% |
| STORE_FAST | 7,909 | 2.1% |
| LIST_EXTEND | 240 | 0.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 0.1% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,663,974 | 99.9% |
| COPY_FREE_VARS | 1,060 | 0.0% |
| RESUME | 640 | 0.0% |
| POP_TOP | 400 | 0.0% |
| RETURN_GENERATOR | 320 | 0.0% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 80 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 40 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| RETURN_VALUE | 40 | 25.0% |
| LOAD_CONST | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 60 | 37.5% |
| PUSH_EXC_INFO | 40 | 25.0% |
| STORE_FAST | 20 | 12.5% |
| UNPACK_SEQUENCE | 20 | 12.5% |
| BINARY_SUBSCR_LIST_INT | 20 | 12.5% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 460 | 69.7% |
| BUILD_TUPLE | 160 | 24.2% |
| LOAD_GLOBAL | 40 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 660 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 320,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,320 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 336,880 | 34.1% |
| SEND | 328,800 | 33.3% |
| RETURN_VALUE | 321,360 | 32.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 665,840 | 67.5% |
| STORE_FAST | 320,800 | 32.5% |
| UNPACK_SEQUENCE | 120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 120 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 320 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,283,460 | 66.4% |
| CALL_BUILTIN_CLASS | 641,440 | 33.2% |
| LOAD_ATTR_INSTANCE_VALUE | 8,040 | 0.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 160 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,283,080 | 66.4% |
| FOR_ITER_RANGE | 641,380 | 33.2% |
| FOR_ITER | 8,600 | 0.4% |
| EXTENDED_ARG | 80 | 0.0% |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,300,760 | 48.8% |
| RETURN_CONST | 1,036,514 | 38.9% |
| YIELD_VALUE | 328,960 | 12.3% |
| RETURN_GENERATOR | 400 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 560 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,292,014 | 46.2% |
| STORE_FAST | 1,298,938 | 26.2% |
| POP_JUMP_IF_FALSE | 694,905 | 14.0% |
| POP_JUMP_IF_TRUE | 328,709 | 6.6% |
| STORE_ATTR_INSTANCE_VALUE | 320,300 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,645,590 | 73.5% |
| LOAD_GLOBAL_MODULE | 1,313,436 | 26.5% |
| LOAD_GLOBAL_BUILTIN | 320 | 0.0% |
| LOAD_GLOBAL | 280 | 0.0% |
| LOAD_DEREF | 160 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 420 | 63.6% |
| POP_TOP | 160 | 24.2% |
| COPY | 80 | 12.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 420 | 63.6% |
| POP_TOP | 80 | 12.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 80 | 12.1% |
| RERAISE | 80 | 12.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 6,389,147 | 49.7% |
| POP_JUMP_IF_FALSE | 1,358,212 | 10.6% |
| CALL_METHOD_DESCRIPTOR_O | 1,094,081 | 8.5% |
| CALL_FUNCTION_EX | 1,023,945 | 8.0% |
| END_SEND | 665,840 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,334,673 | 41.5% |
| RETURN_CONST | 2,721,450 | 21.2% |
| LOAD_CONST | 2,002,903 | 15.6% |
| ENTER_EXECUTOR | 718,685 | 5.6% |
| LOAD_GLOBAL_MODULE | 702,414 | 5.5% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 380 | 57.6% |
| RERAISE | 80 | 12.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 80 | 12.1% |
| CALL_METHOD_DESCRIPTOR_O | 60 | 9.1% |
| BINARY_SUBSCR | 40 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 520 | 78.8% |
| LOAD_GLOBAL | 140 | 21.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,014,163 | 66.5% |
| LOAD_ATTR | 963,140 | 31.8% |
| LOAD_DEREF | 47,534 | 1.6% |
| LOAD_FAST | 2,100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,057,841 | 34.9% |
| LOAD_FAST_LOAD_FAST | 995,567 | 32.9% |
| CALL | 972,769 | 32.1% |
| LOAD_CONST | 480 | 0.0% |
| CALL_PY_EXACT_ARGS | 160 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 337,260 | 51.2% |
| ENTER_EXECUTOR | 319,920 | 48.6% |
| CALL_KW | 400 | 0.1% |
| CACHE | 320 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 657,840 | 99.9% |
| INTERPRETER_EXIT | 400 | 0.1% |
| STORE_FAST | 160 | 0.0% |
| CALL | 120 | 0.0% |
| LIST_APPEND | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,593,659 | 36.6% |
| LOAD_ATTR_INSTANCE_VALUE | 3,613,745 | 28.8% |
| CALL | 1,336,225 | 10.6% |
| RETURN_VALUE | 1,314,976 | 10.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 656,818 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,303,632 | 26.3% |
| TO_BOOL_BOOL | 3,259,447 | 26.0% |
| RETURN_VALUE | 1,314,976 | 10.5% |
| INTERPRETER_EXIT | 1,300,760 | 10.4% |
| LOAD_FAST | 1,015,065 | 8.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 140 | 28.0% |
| LOAD_CONST | 120 | 24.0% |
| LOAD_ATTR | 100 | 20.0% |
| LOAD_FAST | 100 | 20.0% |
| STORE_SUBSCR | 40 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 180 | 36.0% |
| STORE_SUBSCR_DICT | 140 | 28.0% |
| LOAD_FAST | 60 | 12.0% |
| STORE_SUBSCR | 40 | 8.0% |
| LOAD_CONST | 40 | 8.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,359,352 | 55.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,069,270 | 43.9% |
| TO_BOOL | 2,680 | 0.1% |
| LOAD_ATTR | 2,000 | 0.1% |
| RETURN_VALUE | 1,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,411,344 | 99.0% |
| POP_JUMP_IF_FALSE | 19,458 | 0.8% |
| TO_BOOL | 2,680 | 0.1% |
| TO_BOOL_BOOL | 2,320 | 0.1% |
| TO_BOOL_INT | 400 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 328,189 | 50.6% |
| BINARY_OP | 320,320 | 49.4% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 648,549 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,280,020 | 100.0% |
| TO_BOOL | 80 | 0.0% |
| TO_BOOL_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 640,080 | 50.0% |
| RETURN_VALUE | 640,000 | 50.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,059,706 | 48.7% |
| LOAD_ATTR_MODULE | 754,779 | 17.8% |
| UNARY_INVERT | 648,549 | 15.3% |
| POP_JUMP_IF_FALSE | 381,214 | 9.0% |
| LOAD_ATTR | 373,605 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,419,086 | 33.5% |
| TO_BOOL_INT | 1,067,130 | 25.2% |
| STORE_FAST | 1,038,152 | 24.5% |
| BUILD_TUPLE | 373,465 | 8.8% |
| UNARY_INVERT | 320,320 | 7.6% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 641,440 | 40.0% |
| LOAD_ATTR_SLOT | 641,440 | 40.0% |
| LOAD_FAST_LOAD_FAST | 320,080 | 19.9% |
| LOAD_FAST | 640 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 962,100 | 60.0% |
| STORE_FAST | 641,920 | 40.0% |
| RETURN_VALUE | 240 | 0.0% |
| STORE_DEREF | 160 | 0.0% |
| SWAP | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 240 | 30.0% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 17.5% |
| POP_TOP | 80 | 10.0% |
| LOAD_FAST | 80 | 10.0% |
| POP_JUMP_IF_NOT_NONE | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 70.0% |
| STORE_FAST | 240 | 30.0% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 360 | 90.0% |
| LOAD_ATTR | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 400 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 320,320 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 373,465 | 36.2% |
| LOAD_CONST | 328,149 | 31.8% |
| LOAD_FAST | 321,040 | 31.1% |
| LOAD_FAST_LOAD_FAST | 8,709 | 0.8% |
| LOAD_GLOBAL_BUILTIN | 560 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 373,425 | 36.2% |
| CALL_PY_EXACT_ARGS | 335,978 | 32.5% |
| CALL | 320,600 | 31.1% |
| LOAD_CONST | 560 | 0.1% |
| RETURN_VALUE | 400 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 972,769 | 22.2% |
| LOAD_FAST_LOAD_FAST | 667,258 | 15.3% |
| LOAD_CONST | 658,409 | 15.1% |
| LOAD_ATTR_INSTANCE_VALUE | 649,629 | 14.9% |
| LOAD_ATTR | 324,460 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,027,070 | 46.4% |
| RETURN_VALUE | 1,336,225 | 30.6% |
| POP_TOP | 331,420 | 7.6% |
| RESUME_CHECK | 330,429 | 7.6% |
| LOAD_CONST | 320,440 | 7.3% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 961,780 | 93.9% |
| ENTER_EXECUTOR | 62,245 | 6.1% |
| DICT_MERGE | 240 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,023,945 | 99.9% |
| RESUME_CHECK | 220 | 0.0% |
| GET_AWAITABLE | 160 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| MAKE_CELL | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 961,780 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 961,780 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 346,938 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 328,880 | 94.8% |
| COPY_FREE_VARS | 15,818 | 4.6% |
| STORE_FAST | 800 | 0.2% |
| RESUME_CHECK | 420 | 0.1% |
| RETURN_GENERATOR | 400 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 16,058 | 84.1% |
| LOAD_CONST | 1,020 | 5.3% |
| LOAD_ATTR_MODULE | 940 | 4.9% |
| COMPARE_OP | 540 | 2.8% |
| CALL_BUILTIN_CLASS | 140 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 17,778 | 93.1% |
| COMPARE_OP | 540 | 2.8% |
| COMPARE_OP_INT | 520 | 2.7% |
| POP_JUMP_IF_TRUE | 140 | 0.7% |
| COMPARE_OP_STR | 60 | 0.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,360 | 99.6% |
| BUILD_SET | 400 | 0.1% |
| LOAD_FAST | 240 | 0.1% |
| LOAD_GLOBAL_MODULE | 220 | 0.1% |
| LOAD_ATTR_SLOT | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 321,280 | 99.9% |
| POP_JUMP_IF_TRUE | 240 | 0.1% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,419,086 | 52.5% |
| CALL_LEN | 641,260 | 23.7% |
| UNARY_NOT | 640,080 | 23.7% |
| LOAD_FAST | 480 | 0.0% |
| CALL_BUILTIN_FAST | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 2,060,086 | 76.3% |
| TO_BOOL_BOOL | 640,280 | 23.7% |
| TO_BOOL | 480 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 0.0% |
| LOAD_ATTR | 200 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 657,738 | 95.1% |
| CALL_KW | 15,818 | 2.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 15,798 | 2.3% |
| CACHE | 1,060 | 0.2% |
| LOAD_ATTR_PROPERTY | 580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 690,874 | 99.9% |
| RESUME | 600 | 0.1% |
| RETURN_GENERATOR | 80 | 0.0% |
| MAKE_CELL | 80 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 240 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 718,685 | 50.9% |
| CALL_LIST_APPEND | 373,125 | 26.4% |
| STORE_FAST | 319,900 | 22.7% |
| JUMP_BACKWARD | 100 | 0.0% |
| POP_JUMP_IF_FALSE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 641,160 | 45.4% |
| FOR_ITER_LIST | 373,025 | 26.4% |
| RETURN_GENERATOR | 319,920 | 22.7% |
| CALL_FUNCTION_EX | 62,245 | 4.4% |
| RETURN_CONST | 7,680 | 0.5% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 33.3% |
| POP_TOP | 80 | 33.3% |
| JUMP_BACKWARD | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 160 | 66.7% |
| JUMP_BACKWARD | 80 | 33.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 8,600 | 90.1% |
| JUMP_BACKWARD | 500 | 5.2% |
| FOR_ITER | 260 | 2.7% |
| EXTENDED_ARG | 160 | 1.7% |
| SWAP | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,300 | 87.0% |
| RETURN_CONST | 460 | 4.8% |
| FOR_ITER | 260 | 2.7% |
| FOR_ITER_LIST | 240 | 2.5% |
| LOAD_FAST | 180 | 1.9% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 657,840 | 66.6% |
| LOAD_ATTR_INSTANCE_VALUE | 320,300 | 32.5% |
| LOAD_FAST | 8,240 | 0.8% |
| RETURN_VALUE | 240 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 987,040 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 80.0% |
| IMPORT_FROM | 20 | 20.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 720 | 52.9% |
| LOAD_CONST | 560 | 41.2% |
| LOAD_FAST_LOAD_FAST | 80 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 800 | 58.8% |
| RETURN_VALUE | 400 | 29.4% |
| LOAD_DEREF | 160 | 11.8% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 641,331 | 63.0% |
| POP_JUMP_IF_TRUE | 320,400 | 31.5% |
| POP_TOP | 54,465 | 5.4% |
| CALL_LIST_APPEND | 440 | 0.0% |
| STORE_FAST | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,631 | 63.1% |
| FOR_ITER_LIST | 374,085 | 36.8% |
| FOR_ITER_RANGE | 740 | 0.1% |
| FOR_ITER | 500 | 0.0% |
| ENTER_EXECUTOR | 100 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,307,040 | 100.0% |
| RESUME | 480 | 0.0% |
| POP_EXCEPT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 978,380 | 74.8% |
| SEND | 329,140 | 25.2% |
| LOAD_CONST | 80 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,292,356 | 87.7% |
| POP_TOP | 320,840 | 12.3% |
| STORE_ATTR | 180 | 0.0% |
| POP_JUMP_IF_TRUE | 160 | 0.0% |
| CALL_LIST_APPEND | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,972,036 | 75.4% |
| LOAD_GLOBAL_BUILTIN | 641,480 | 24.5% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 80 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 641,440 | 66.7% |
| LOAD_FAST | 320,080 | 33.3% |
| BINARY_SLICE | 240 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 961,780 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,510,108 | 81.7% |
| LOAD_ATTR_SLOT | 961,880 | 17.4% |
| LOAD_FAST_LOAD_FAST | 32,256 | 0.6% |
| LOAD_ATTR | 9,880 | 0.2% |
| LOAD_GLOBAL_MODULE | 2,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,370,181 | 24.8% |
| PUSH_NULL | 963,140 | 17.4% |
| SWAP | 709,603 | 12.9% |
| LOAD_ATTR_METHOD_NO_DICT | 374,985 | 6.8% |
| BINARY_OP | 373,605 | 6.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,279,783 | 22.6% |
| POP_JUMP_IF_FALSE | 2,310,356 | 15.9% |
| POP_TOP | 2,002,903 | 13.8% |
| STORE_ATTR_SLOT | 1,645,787 | 11.3% |
| POP_JUMP_IF_TRUE | 1,313,509 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,883,954 | 40.5% |
| STORE_FAST | 3,646,999 | 25.1% |
| COMPARE_OP_INT | 2,284,036 | 15.7% |
| CALL | 658,409 | 4.5% |
| SEND_GEN | 657,660 | 4.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 643,160 | 88.4% |
| LOAD_ATTR | 31,676 | 4.4% |
| STORE_FAST | 16,298 | 2.2% |
| RESUME_CHECK | 16,118 | 2.2% |
| CALL_LEN | 15,798 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 659,678 | 90.7% |
| PUSH_NULL | 47,534 | 6.5% |
| COMPARE_OP_INT | 15,818 | 2.2% |
| LOAD_ATTR | 760 | 0.1% |
| LOAD_CONST | 560 | 0.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 13,586,146 | 15.3% |
| STORE_FAST | 11,887,899 | 13.4% |
| POP_JUMP_IF_FALSE | 9,753,478 | 11.0% |
| LOAD_CONST | 5,883,954 | 6.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,618,662 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 29,289,891 | 33.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 7,070,641 | 8.0% |
| LOAD_ATTR_SLOT | 6,699,145 | 7.6% |
| CALL_PY_EXACT_ARGS | 6,269,242 | 7.1% |
| RETURN_VALUE | 4,593,659 | 5.2% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 80 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 20 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,975,727 | 24.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,732,297 | 21.4% |
| PUSH_NULL | 995,567 | 12.3% |
| LOAD_FAST_LOAD_FAST | 652,640 | 8.1% |
| LOAD_GLOBAL_MODULE | 641,860 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 2,634,756 | 32.5% |
| LOAD_FAST | 1,682,883 | 20.8% |
| CALL | 667,258 | 8.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 656,778 | 8.1% |
| LOAD_FAST_LOAD_FAST | 652,640 | 8.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,420 | 14.8% |
| POP_TOP | 940 | 9.8% |
| RESUME | 920 | 9.6% |
| RESUME_CHECK | 900 | 9.4% |
| STORE_FAST | 840 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,080 | 32.0% |
| LOAD_ATTR | 1,900 | 19.8% |
| LOAD_GLOBAL_BUILTIN | 1,660 | 17.3% |
| LOAD_FAST | 800 | 8.3% |
| LOAD_DEREF | 520 | 5.4% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 900 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 400 | 44.4% |
| LOAD_FAST | 200 | 22.2% |
| CALL | 140 | 15.6% |
| LOAD_FAST_LOAD_FAST | 80 | 8.9% |
| LOAD_GLOBAL | 40 | 4.4% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 880 | 61.1% |
| CACHE | 240 | 16.7% |
| CALL_KW | 160 | 11.1% |
| CALL_FUNCTION_EX | 80 | 5.6% |
| COPY_FREE_VARS | 80 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 880 | 61.1% |
| RESUME_CHECK | 260 | 18.1% |
| RETURN_GENERATOR | 240 | 16.7% |
| RESUME | 60 | 4.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 8,925,578 | 49.3% |
| COMPARE_OP_INT | 3,711,273 | 20.5% |
| TO_BOOL_INT | 2,867,461 | 15.8% |
| TO_BOOL_LIST | 1,595,340 | 8.8% |
| TO_BOOL_NONE | 662,360 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,753,478 | 53.8% |
| LOAD_CONST | 2,310,356 | 12.7% |
| RETURN_CONST | 1,369,652 | 7.6% |
| POP_TOP | 1,358,212 | 7.5% |
| LOAD_GLOBAL_BUILTIN | 961,380 | 5.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,308,938 | 57.2% |
| LOAD_ATTR_INSTANCE_VALUE | 977,949 | 42.7% |
| LOAD_ATTR | 440 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,964,527 | 85.9% |
| LOAD_CONST | 320,480 | 14.0% |
| RETURN_CONST | 1,280 | 0.1% |
| LOAD_FAST_LOAD_FAST | 400 | 0.0% |
| LOAD_GLOBAL | 260 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,013,112 | 86.2% |
| LOAD_ATTR_INSTANCE_VALUE | 321,200 | 13.8% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,361,303 | 58.3% |
| LOAD_FAST_LOAD_FAST | 330,240 | 14.1% |
| LOAD_GLOBAL_MODULE | 329,749 | 14.1% |
| LOAD_CONST | 312,180 | 13.4% |
| LOAD_GLOBAL | 400 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,968,694 | 44.2% |
| TO_BOOL | 2,411,344 | 35.9% |
| TO_BOOL_INT | 1,342,894 | 20.0% |
| COMPARE_OP_INT | 260 | 0.0% |
| CONTAINS_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,753,418 | 55.8% |
| LOAD_CONST | 1,313,509 | 19.5% |
| STORE_FAST | 641,280 | 9.5% |
| NOP | 328,709 | 4.9% |
| JUMP_BACKWARD | 320,400 | 4.8% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,721,450 | 35.1% |
| POP_JUMP_IF_FALSE | 1,369,652 | 17.6% |
| STORE_FAST | 1,345,145 | 17.3% |
| STORE_ATTR_SLOT | 987,538 | 12.7% |
| STORE_ATTR_INSTANCE_VALUE | 641,860 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,389,147 | 82.3% |
| INTERPRETER_EXIT | 1,036,514 | 13.4% |
| END_SEND | 336,880 | 4.3% |
| EXIT_INIT_CHECK | 320 | 0.0% |
| RETURN_VALUE | 240 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 329,380 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 329,140 | 49.9% |
| SEND | 720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 328,800 | 49.9% |
| YIELD_VALUE | 328,800 | 49.9% |
| SEND | 720 | 0.1% |
| POP_TOP | 460 | 0.1% |
| SEND_GEN | 460 | 0.1% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 85.7% |
| LOAD_FAST_LOAD_FAST | 80 | 14.3% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,980 | 66.4% |
| LOAD_FAST_LOAD_FAST | 1,540 | 20.5% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 3.7% |
| STORE_ATTR | 260 | 3.5% |
| LOAD_DEREF | 200 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 2,660 | 35.5% |
| LOAD_FAST | 1,200 | 16.0% |
| LOAD_CONST | 1,140 | 15.2% |
| RETURN_CONST | 780 | 10.4% |
| STORE_ATTR_SLOT | 460 | 6.1% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 320 | 36.4% |
| BUILD_LIST | 160 | 18.2% |
| CALL_KW | 160 | 18.2% |
| BINARY_OP_ADD_INT | 120 | 13.6% |
| CALL | 80 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 54.5% |
| LOAD_CONST | 160 | 18.2% |
| BUILD_LIST | 80 | 9.1% |
| LOAD_DEREF | 80 | 9.1% |
| LOAD_FAST_LOAD_FAST | 80 | 9.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,646,999 | 18.5% |
| RETURN_VALUE | 3,303,632 | 16.8% |
| CALL | 2,027,070 | 10.3% |
| CALL_LEN | 1,335,496 | 6.8% |
| LOAD_FAST | 1,313,496 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,887,899 | 60.4% |
| JUMP_FORWARD | 2,292,356 | 11.7% |
| RETURN_CONST | 1,345,145 | 6.8% |
| NOP | 1,298,938 | 6.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 709,443 | 3.6% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 20 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,456,813 | 100.0% |
| UNPACK_SEQUENCE | 260 | 0.0% |
| POP_TOP | 80 | 0.0% |
| COPY | 80 | 0.0% |
| STORE_FAST_STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,456,573 | 99.9% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


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

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 709,603 | 99.8% |
| LOAD_FAST | 400 | 0.1% |
| BINARY_OP_ADD_INT | 260 | 0.0% |
| BUILD_TUPLE | 240 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 709,603 | 99.8% |
| POP_EXCEPT | 420 | 0.1% |
| STORE_ATTR_INSTANCE_VALUE | 280 | 0.0% |
| POP_TOP | 240 | 0.0% |
| STORE_ATTR | 200 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 23.5% |
| END_SEND | 120 | 17.6% |
| RETURN_VALUE | 80 | 11.8% |
| LOAD_FAST | 80 | 11.8% |
| FOR_ITER_LIST | 80 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 280 | 41.2% |
| STORE_FAST_STORE_FAST | 260 | 38.2% |
| UNPACK_SEQUENCE_TUPLE | 60 | 8.8% |
| STORE_FAST | 40 | 5.9% |
| POP_TOP | 20 | 2.9% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 978,720 | 74.8% |
| SEND | 328,800 | 25.1% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 978,720 | 74.8% |
| INTERPRETER_EXIT | 328,960 | 25.2% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,080 | 47.9% |
| CACHE | 640 | 14.7% |
| COPY_FREE_VARS | 600 | 13.8% |
| POP_TOP | 480 | 11.1% |
| SEND_GEN | 400 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,220 | 51.2% |
| LOAD_GLOBAL | 920 | 21.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 480 | 11.1% |
| LOAD_CONST | 240 | 5.5% |
| NOP | 180 | 4.1% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 641,240 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 641,260 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 320,200 | 99.9% |
| LOAD_CONST | 280 | 0.1% |
| BINARY_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 320,220 | 99.9% |
| SWAP | 260 | 0.1% |
| STORE_DEREF | 120 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,200 | 100.0% |
| BINARY_OP | 40 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 320,240 | 100.0% |
| COMPARE_OP | 40 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 7,960 | 98.3% |
| LOAD_CONST | 80 | 1.0% |
| BINARY_OP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,980 | 98.5% |
| SWAP | 120 | 1.5% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 15,858 | 93.5% |
| LOAD_FAST | 1,040 | 6.1% |
| BINARY_SUBSCR | 60 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,798 | 93.2% |
| RETURN_VALUE | 780 | 4.6% |
| PUSH_EXC_INFO | 380 | 2.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| BINARY_SUBSCR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 40 | 66.7% |
| UNPACK_SEQUENCE | 20 | 33.3% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20 | 100.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 160 | 50.0% |
| CALL | 80 | 25.0% |
| LOAD_FAST | 40 | 12.5% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 180 | 56.2% |
| COPY_FREE_VARS | 140 | 43.8% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,280 | 95.3% |
| CALL_BUILTIN_CLASS | 15,778 | 4.7% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 320,300 | 95.3% |
| COPY_FREE_VARS | 15,798 | 4.7% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 657,438 | 91.4% |
| LOAD_ATTR_INSTANCE_VALUE | 61,025 | 8.5% |
| CALL | 280 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 641,440 | 89.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60,865 | 8.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 15,778 | 2.2% |
| STORE_FAST | 500 | 0.1% |
| LOAD_FAST | 240 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 460 | 67.6% |
| LOAD_ATTR_SLOT | 120 | 17.6% |
| CALL | 80 | 11.8% |
| LOAD_FAST_LOAD_FAST | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 280 | 41.2% |
| COPY | 220 | 32.4% |
| POP_TOP | 140 | 20.6% |
| TO_BOOL | 40 | 5.9% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 60,865 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60,885 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 50.0% |
| CALL | 80 | 33.3% |
| LOAD_CONST | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 180 | 75.0% |
| CALL_BUILTIN_CLASS | 40 | 16.7% |
| CALL | 20 | 8.3% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,314,176 | 99.9% |
| BUILD_TUPLE | 400 | 0.0% |
| CALL | 260 | 0.0% |
| LOAD_ATTR_MODULE | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,314,896 | 100.0% |
| TO_BOOL | 260 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,563,800 | 86.8% |
| LOAD_FAST | 388,934 | 13.2% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,335,496 | 45.2% |
| COPY | 641,260 | 21.7% |
| LOAD_CONST | 320,220 | 10.8% |
| BINARY_OP_ADD_INT | 320,200 | 10.8% |
| LOAD_FAST | 319,900 | 10.8% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 373,425 | 99.9% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 373,125 | 99.8% |
| JUMP_BACKWARD | 440 | 0.1% |
| JUMP_FORWARD | 140 | 0.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 656,778 | 48.6% |
| LOAD_FAST | 373,305 | 27.6% |
| RETURN_VALUE | 320,280 | 23.7% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 693,625 | 51.4% |
| RETURN_VALUE | 656,818 | 48.6% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 641,240 | 49.4% |
| LOAD_FAST | 336,058 | 25.9% |
| LOAD_ATTR | 320,280 | 24.7% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 656,398 | 50.6% |
| STORE_FAST | 641,260 | 49.4% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 695,516 | 67.8% |
| LOAD_ATTR | 329,080 | 32.1% |
| CALL | 760 | 0.1% |
| LOAD_FAST | 360 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 694,556 | 67.7% |
| TO_BOOL_BOOL | 329,040 | 32.1% |
| POP_TOP | 620 | 0.1% |
| LOAD_FAST | 460 | 0.0% |
| TO_BOOL | 340 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,048,225 | 95.8% |
| BINARY_SLICE | 44,956 | 4.1% |
| CALL | 720 | 0.1% |
| LOAD_CONST | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,094,081 | 100.0% |
| PUSH_EXC_INFO | 60 | 0.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 7,681,729 | 48.3% |
| LOAD_FAST | 6,269,242 | 39.4% |
| LOAD_ATTR_METHOD_NO_DICT | 969,969 | 6.1% |
| BUILD_TUPLE | 335,978 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 328,149 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 14,917,249 | 93.7% |
| COPY_FREE_VARS | 657,738 | 4.1% |
| RETURN_GENERATOR | 337,260 | 2.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 656,818 | 99.8% |
| LOAD_ATTR_METHOD_NO_DICT | 360 | 0.1% |
| CALL | 240 | 0.0% |
| LOAD_CONST | 240 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 657,698 | 100.0% |
| RETURN_GENERATOR | 120 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 920 | 97.9% |
| CALL | 20 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 720 | 76.6% |
| LOAD_GLOBAL_MODULE | 200 | 21.3% |
| LOAD_GLOBAL | 20 | 2.1% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,284,036 | 61.5% |
| LOAD_GLOBAL_MODULE | 641,240 | 17.3% |
| BINARY_OP_MULTIPLY_INT | 320,240 | 8.6% |
| LOAD_ATTR_INSTANCE_VALUE | 319,880 | 8.6% |
| LOAD_ATTR_SLOT | 60,825 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,711,273 | 100.0% |
| POP_JUMP_IF_TRUE | 260 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 140 | 70.0% |
| COMPARE_OP | 60 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 40.0% |
| COPY | 60 | 30.0% |
| STORE_FAST | 60 | 30.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,283,080 | 63.2% |
| JUMP_BACKWARD | 374,085 | 18.4% |
| ENTER_EXECUTOR | 373,025 | 18.4% |
| FOR_ITER | 240 | 0.0% |
| SWAP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 746,730 | 36.8% |
| RETURN_CONST | 641,460 | 31.6% |
| LOAD_FAST | 641,260 | 31.6% |
| STORE_FAST | 660 | 0.0% |
| LOAD_DEREF | 140 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 641,380 | 50.0% |
| ENTER_EXECUTOR | 641,160 | 50.0% |
| JUMP_BACKWARD | 740 | 0.1% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 641,980 | 50.0% |
| LOAD_CONST | 641,280 | 50.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 44.4% |
| JUMP_BACKWARD | 60 | 33.3% |
| ENTER_EXECUTOR | 20 | 11.1% |
| FOR_ITER | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 44.4% |
| LOAD_GLOBAL | 40 | 22.2% |
| LOAD_GLOBAL_MODULE | 40 | 22.2% |
| LOAD_FAST | 20 | 11.1% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 94.7% |
| LOAD_ATTR | 20 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 380 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,289,891 | 96.7% |
| LOAD_ATTR_INSTANCE_VALUE | 656,658 | 2.2% |
| LOAD_FAST_LOAD_FAST | 336,938 | 1.1% |
| LOAD_ATTR | 4,360 | 0.0% |
| LOAD_DEREF | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,834,027 | 19.3% |
| LOAD_ATTR_METHOD_NO_DICT | 3,964,921 | 13.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,956,294 | 13.1% |
| RETURN_VALUE | 3,613,745 | 11.9% |
| CALL_LEN | 2,563,800 | 8.5% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,964,921 | 64.2% |
| LOAD_FAST | 1,832,109 | 29.7% |
| LOAD_ATTR | 374,985 | 6.1% |
| LOAD_ATTR_SLOT | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,772,233 | 44.9% |
| LOAD_FAST_LOAD_FAST | 1,732,297 | 28.1% |
| CALL_PY_EXACT_ARGS | 969,969 | 15.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 695,516 | 11.3% |
| LOAD_GLOBAL_MODULE | 720 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,070,641 | 50.6% |
| LOAD_ATTR_INSTANCE_VALUE | 3,956,294 | 28.3% |
| LOAD_ATTR_SLOT | 1,962,876 | 14.1% |
| RETURN_VALUE | 656,738 | 4.7% |
| LOAD_FAST_LOAD_FAST | 320,280 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 7,681,729 | 55.0% |
| LOAD_FAST | 5,618,662 | 40.2% |
| LOAD_FAST_LOAD_FAST | 346,798 | 2.5% |
| LOAD_CONST | 320,560 | 2.3% |
| CALL | 1,700 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,419,631 | 99.9% |
| LOAD_ATTR | 1,900 | 0.1% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,014,163 | 58.9% |
| BINARY_OP | 754,779 | 22.1% |
| UNARY_INVERT | 328,189 | 9.6% |
| LOAD_FAST | 320,420 | 9.4% |
| COMPARE_OP | 940 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 664,287 | 100.0% |
| LOAD_ATTR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 336,158 | 50.6% |
| CALL | 320,300 | 48.2% |
| BINARY_OP | 7,949 | 1.2% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,760 | 99.9% |
| LOAD_ATTR | 220 | 0.1% |
| LOAD_DEREF | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 320,560 | 99.8% |
| COPY_FREE_VARS | 580 | 0.2% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,699,145 | 99.9% |
| LOAD_FAST_LOAD_FAST | 7,960 | 0.1% |
| LOAD_ATTR | 840 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 1,962,876 | 29.3% |
| TO_BOOL_BOOL | 1,777,264 | 26.5% |
| LOAD_ATTR | 961,880 | 14.3% |
| TO_BOOL_NONE | 660,560 | 9.8% |
| BUILD_LIST | 641,440 | 9.6% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,658,821 | 34.6% |
| LOAD_FAST | 1,634,776 | 21.3% |
| POP_JUMP_IF_FALSE | 961,380 | 12.5% |
| STORE_FAST | 702,605 | 9.1% |
| JUMP_FORWARD | 641,480 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,284,746 | 68.7% |
| CALL_ISINSTANCE | 1,314,176 | 17.1% |
| LOAD_DEREF | 643,160 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 442,890 | 5.8% |
| BUILD_TUPLE | 560 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,776,685 | 44.4% |
| RESUME_CHECK | 1,675,165 | 19.7% |
| NOP | 1,313,436 | 15.4% |
| POP_TOP | 702,414 | 8.3% |
| POP_JUMP_IF_NOT_NONE | 329,749 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 3,419,631 | 40.2% |
| BINARY_OP | 2,059,706 | 24.2% |
| LOAD_FAST | 1,366,581 | 16.1% |
| LOAD_FAST_LOAD_FAST | 641,860 | 7.5% |
| COMPARE_OP_INT | 641,240 | 7.5% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 94.1% |
| LOAD_SUPER_ATTR | 40 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 640 | 94.1% |
| LOAD_GLOBAL | 40 | 5.9% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 642,080 | 99.9% |
| LOAD_SUPER_ATTR | 400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 321,320 | 50.0% |
| LOAD_FAST_LOAD_FAST | 320,720 | 49.9% |
| CALL_PY_EXACT_ARGS | 320 | 0.0% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,917,249 | 69.3% |
| CACHE | 2,663,974 | 12.4% |
| SEND_GEN | 978,320 | 4.5% |
| COPY_FREE_VARS | 690,874 | 3.2% |
| POP_TOP | 658,160 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,586,146 | 63.1% |
| LOAD_GLOBAL_BUILTIN | 2,658,821 | 12.3% |
| NOP | 2,292,014 | 10.6% |
| LOAD_GLOBAL_MODULE | 1,675,165 | 7.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,307,040 | 6.1% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 978,380 | 59.8% |
| LOAD_CONST | 657,660 | 40.2% |
| SEND | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 978,320 | 59.8% |
| POP_TOP | 657,780 | 40.2% |
| RESUME | 400 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,263,420 | 99.8% |
| STORE_ATTR | 2,660 | 0.1% |
| LOAD_FAST_LOAD_FAST | 1,900 | 0.1% |
| LOAD_DEREF | 360 | 0.0% |
| SWAP | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,298,920 | 57.3% |
| RETURN_CONST | 641,860 | 28.3% |
| NOP | 320,300 | 14.1% |
| LOAD_CONST | 4,160 | 0.2% |
| LOAD_FAST_LOAD_FAST | 780 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,977,334 | 53.0% |
| LOAD_FAST_LOAD_FAST | 2,634,756 | 46.9% |
| STORE_ATTR | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,975,727 | 35.2% |
| LOAD_CONST | 1,645,787 | 29.3% |
| LOAD_FAST | 987,538 | 17.6% |
| RETURN_CONST | 987,538 | 17.6% |
| NOP | 15,960 | 0.3% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 336,058 | 99.8% |
| LOAD_CONST | 280 | 0.1% |
| LOAD_FAST | 160 | 0.0% |
| STORE_SUBSCR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 336,158 | 99.9% |
| NOP | 140 | 0.0% |
| LOAD_CONST | 140 | 0.0% |
| RETURN_CONST | 140 | 0.0% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,834,027 | 44.3% |
| RETURN_VALUE | 3,259,447 | 24.7% |
| LOAD_ATTR_SLOT | 1,777,264 | 13.5% |
| CALL_ISINSTANCE | 1,314,896 | 10.0% |
| COPY | 640,280 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,925,578 | 67.7% |
| POP_JUMP_IF_TRUE | 2,968,694 | 22.5% |
| UNARY_NOT | 1,280,020 | 9.7% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,060,086 | 48.9% |
| BINARY_OP | 1,067,130 | 25.3% |
| LOAD_FAST | 709,254 | 16.8% |
| LOAD_ATTR_INSTANCE_VALUE | 373,505 | 8.9% |
| TO_BOOL | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,867,461 | 68.1% |
| POP_JUMP_IF_TRUE | 1,342,894 | 31.9% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,595,220 | 100.0% |
| TO_BOOL | 180 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,595,340 | 100.0% |
| POP_JUMP_IF_TRUE | 180 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 660,560 | 99.7% |
| LOAD_FAST | 1,240 | 0.2% |
| LOAD_ATTR | 360 | 0.1% |
| TO_BOOL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 662,360 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 44.4% |
| UNPACK_SEQUENCE | 60 | 33.3% |
| BINARY_SUBSCR_LIST_INT | 40 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 33.3% |
| STORE_FAST | 60 | 33.3% |
| STORE_FAST_STORE_FAST | 60 | 33.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 746,730 | 51.3% |
| STORE_FAST | 709,443 | 48.7% |
| UNPACK_SEQUENCE | 280 | 0.0% |
| BINARY_SLICE | 200 | 0.0% |
| END_SEND | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,456,813 | 100.0% |
| LOAD_FAST | 60 | 0.0% |
| STORE_FAST | 60 | 0.0% |


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
|     deferred | 4,226,362 | 76.6% |
|          hit | 1,290,300 | 23.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 6.0% |
| Failure | 4,060 | 94.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 2,900 | 71.4% |
| or | 1,100 | 27.1% |
| floor divide | 40 | 1.0% |
| multiply different types | 20 | 0.5% |


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
|     deferred | 80 | 0.5% |
|          hit | 17,118 | 99.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,362,353 | 13.5% |
|          hit | 27,899,872 | 86.4% |
|         miss | 1,960 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,220 | 48.4% |
| Failure | 6,640 | 51.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class no vectorcall | 1,140 | 17.2% |
| cfunc noargs | 880 | 13.3% |
| code complex parameters | 780 | 11.7% |
| meth descr method fastcall keywords | 780 | 11.7% |
| no dict | 720 | 10.8% |
| meth descr varargs | 700 | 10.5% |
| cfunc varargs keywords | 460 | 6.9% |
| other | 380 | 5.7% |
| class mutable | 380 | 5.7% |
| metaclass | 140 | 2.1% |
| cfunc varargs | 100 | 1.5% |
| operator wrapper | 100 | 1.5% |
| wrong number arguments | 40 | 0.6% |
| cmethod | 40 | 0.6% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 17,978 | 0.5% |
|          hit | 3,711,733 | 99.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 580 | 51.8% |
| Failure | 540 | 48.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 220 | 40.7% |
| tuple | 160 | 29.6% |
| different types | 120 | 22.2% |
| bool | 40 | 7.4% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,960 | 0.3% |
|          hit | 3,314,010 | 99.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 55.2% |
| Failure | 260 | 44.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 140 | 53.8% |
| dict items | 80 | 30.8% |
| set | 40 | 15.4% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,501,884 | 8.1% |
|          hit | 62,425,843 | 91.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 12,080 | 60.6% |
| Failure | 7,840 | 39.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 3,620 | 46.2% |
| method | 1,540 | 19.6% |
| has managed dict | 1,500 | 19.1% |
| shadowed | 640 | 8.2% |
| metaclass attribute | 180 | 2.3% |
| class method obj | 160 | 2.0% |
| non object slot | 80 | 1.0% |
| class attr descriptor | 60 | 0.8% |
| class attr simple | 40 | 0.5% |
| builtin class method | 20 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,960 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 16,195,755 | 99.9% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,740 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 460 | 0.1% |
|          hit | 643,160 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 100.0% |
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
|     deferred | 658,060 | 28.7% |
|          hit | 1,636,500 | 71.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 39.0% |
| Failure | 720 | 61.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 720 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,120 | 0.1% |
|          hit | 7,881,170 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,120 | 92.3% |
| Failure | 260 | 7.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 120 | 46.2% |
| overridden | 80 | 30.8% |
| overriding descriptor | 40 | 15.4% |
| no dict | 20 | 7.7% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 320 | 0.1% |
|          hit | 336,638 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 77.8% |
| Failure | 40 | 22.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 40 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,430,882 | 10.9% |
|          hit | 19,790,057 | 89.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,100 | 53.6% |
| Failure | 2,680 | 46.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 840 | 31.3% |
| sequence | 840 | 31.3% |
| mapping | 280 | 10.4% |
| bytearray | 260 | 9.7% |
| dict | 180 | 6.7% |
| memory view | 140 | 5.2% |
| set | 100 | 3.7% |
| float | 20 | 0.7% |
| tuple | 20 | 0.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 1,457,233 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 202,060,144 | 48.6% |
| Not specialized | 47,111,643 | 11.3% |
| Specialized hits | 166,308,126 | 40.0% |
| Specialized misses | 2,060 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 5,501,884 | 32.0% |
| CALL | 4,362,353 | 25.3% |
| BINARY_OP | 4,226,362 | 24.5% |
| TO_BOOL | 2,430,882 | 14.1% |
| SEND | 658,060 | 3.8% |
| COMPARE_OP | 17,978 | 0.1% |
| FOR_ITER | 8,960 | 0.1% |
| LOAD_GLOBAL | 4,960 | 0.0% |
| STORE_ATTR | 4,120 | 0.0% |
| LOAD_SUPER_ATTR | 460 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,420 | 68.3% |
| CALL_METHOD_DESCRIPTOR_O | 480 | 23.1% |
| LOAD_GLOBAL_BUILTIN | 80 | 3.8% |
| CALL_BUILTIN_O | 60 | 2.9% |
| RESUME | 20 | 1.0% |
| RESUME_CHECK | 20 | 1.0% |
| CACHE | 0 | 0.0% |
| BEFORE_ASYNC_WITH | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 2,666,634 | 12.0% |
| Calls to Python functions inlined | 19,612,515 | 88.0% |
| Calls via PyEval_EvalFrame (total) | 2,666,634 | 12.0% |
| Calls via PyEval_EvalFrame (vector) | 2,337,274 | 10.5% |
| Calls via PyEval_EvalFrame (generator) | 329,360 | 1.5% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,337,274 | 10.5% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 400 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 1,400 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 659,440 | 3.0% |
| Frame objects created | 740 | 0.0% |
| Frames pushed | 20,313,149 | 91.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 9,611,744 | 43.1% |
| Frees to freelist | 9,628,542 |  |
| Allocations | 12,702,192 | 56.9% |
| Allocations to 512 bytes | 12,060,466 | 54.0% |
| Allocations to 4 kbytes | 540 | 0.0% |
| Allocations over 4 kbytes | 641,186 | 2.9% |
| Frees | 13,167,841 |  |
| New values | 820 |  |
| Interpreter increfs | 172,628,655 | 83.3% |
| Interpreter decrefs | 190,045,409 | 83.5% |
| Increfs | 34,565,584 | 16.7% |
| Decrefs | 37,511,767 | 16.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 6,249,847 |  |
| Method cache misses | 8,091 |  |
| Method cache collisions | 7,784 |  |
| Method cache dunder hits | 1,695,250 |  |
| Method cache dunder misses | 1,102 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 1,980 | 161,280 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 980 |  |
| Traces created | 980 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 0 | 0.0% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 480 | 49.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 480 | 49.0% |
| <= 256 | 20 | 2.0% |


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
| <= 16 | 0 | 0.0% |
| <= 32 | 40 | 4.1% |
| <= 64 | 40 | 4.1% |
| <= 128 | 20 | 2.0% |


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
| CALL | 40 |
| RETURN_GENERATOR | 20 |
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
