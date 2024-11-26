
# Pystats results

- benchmark: concurrent_imap
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 97,589,870 | 17.7% | 17.7% |  |
| RESUME_CHECK | 35,505,989 | 6.4% | 24.1% | 0.0% |
| STORE_FAST | 29,053,534 | 5.3% | 29.4% |  |
| LOAD_ATTR_INSTANCE_VALUE | 24,033,778 | 4.4% | 33.8% | 0.9% |
| POP_TOP | 23,232,317 | 4.2% | 38.0% |  |
| RETURN_VALUE | 20,598,276 | 3.7% | 41.7% |  |
| JUMP_BACKWARD | 18,354,038 | 3.3% | 45.0% |  |
| POP_JUMP_IF_FALSE | 17,252,078 | 3.1% | 48.2% |  |
| LOAD_GLOBAL_MODULE | 16,512,923 | 3.0% | 51.2% | 0.0% |
| LOAD_FAST_LOAD_FAST | 15,764,110 | 2.9% | 54.0% |  |
| LOAD_CONST | 14,772,659 | 2.7% | 56.7% |  |
| INTERPRETER_EXIT | 12,742,992 | 2.3% | 59.0% |  |
| CALL_PY_EXACT_ARGS | 11,590,195 | 2.1% | 61.1% | 0.0% |
| CALL | 11,249,973 | 2.0% | 63.2% |  |
| LOAD_ATTR | 10,058,759 | 1.8% | 65.0% |  |
| FOR_ITER_LIST | 9,859,616 | 1.8% | 66.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,826,242 | 1.8% | 68.5% | 0.8% |
| NOP | 9,777,138 | 1.8% | 70.3% |  |
| LOAD_GLOBAL_BUILTIN | 8,470,972 | 1.5% | 71.9% | 0.0% |
| RETURN_CONST | 8,062,489 | 1.5% | 73.3% |  |
| PUSH_NULL | 7,320,031 | 1.3% | 74.6% |  |
| COPY | 7,132,220 | 1.3% | 75.9% |  |
| YIELD_VALUE | 6,913,660 | 1.3% | 77.2% |  |
| BINARY_OP | 6,788,629 | 1.2% | 78.4% |  |
| STORE_FAST_LOAD_FAST | 6,464,820 | 1.2% | 79.6% |  |
| FOR_ITER_GEN | 6,347,440 | 1.2% | 80.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 6,319,179 | 1.1% | 81.9% |  |
| TO_BOOL_BOOL | 5,840,046 | 1.1% | 83.0% |  |
| TO_BOOL_INT | 5,009,036 | 0.9% | 83.9% |  |
| POP_JUMP_IF_NOT_NONE | 4,955,037 | 0.9% | 84.8% |  |
| STORE_FAST_STORE_FAST | 4,792,191 | 0.9% | 85.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 4,333,784 | 0.8% | 86.4% | 5.7% |
| BUILD_TUPLE | 4,236,807 | 0.8% | 87.2% |  |
| COMPARE_OP_INT | 3,673,739 | 0.7% | 87.9% | 0.2% |
| LOAD_ATTR_MODULE | 3,525,016 | 0.6% | 88.5% | 0.0% |
| POP_JUMP_IF_TRUE | 2,670,541 | 0.5% | 89.0% |  |
| SWAP | 2,544,522 | 0.5% | 89.4% |  |
| CALL_FUNCTION_EX | 2,414,005 | 0.4% | 89.9% |  |
| CALL_PY_WITH_DEFAULTS | 2,357,646 | 0.4% | 90.3% |  |
| GET_ITER | 2,318,526 | 0.4% | 90.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 2,114,580 | 0.4% | 91.1% | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,104,911 | 0.4% | 91.5% |  |
| CALL_BUILTIN_CLASS | 1,957,419 | 0.4% | 91.8% |  |
| BEFORE_WITH | 1,834,937 | 0.3% | 92.2% |  |
| CALL_BUILTIN_FAST | 1,784,687 | 0.3% | 92.5% |  |
| LOAD_DEREF | 1,770,334 | 0.3% | 92.8% |  |
| STORE_SUBSCR_DICT | 1,724,047 | 0.3% | 93.1% |  |
| COPY_FREE_VARS | 1,720,274 | 0.3% | 93.4% |  |
| CONTAINS_OP | 1,706,781 | 0.3% | 93.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,660,713 | 0.3% | 94.1% |  |
| BUILD_MAP | 1,654,973 | 0.3% | 94.4% |  |
| LOAD_SUPER_ATTR_METHOD | 1,623,954 | 0.3% | 94.7% |  |
| UNARY_INVERT | 1,620,053 | 0.3% | 94.9% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,476,880 | 0.3% | 95.2% |  |
| COMPARE_OP_STR | 1,474,414 | 0.3% | 95.5% |  |
| BUILD_LIST | 1,461,909 | 0.3% | 95.7% |  |
| FOR_ITER | 1,305,260 | 0.2% | 96.0% |  |
| UNPACK_SEQUENCE_TUPLE | 1,169,569 | 0.2% | 96.2% |  |
| CALL_ISINSTANCE | 1,147,521 | 0.2% | 96.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,138,429 | 0.2% | 96.6% | 0.0% |
| JUMP_FORWARD | 1,124,635 | 0.2% | 96.8% |  |
| BINARY_OP_ADD_INT | 1,112,421 | 0.2% | 97.0% |  |
| POP_JUMP_IF_NONE | 1,102,864 | 0.2% | 97.2% |  |
| TO_BOOL | 1,073,875 | 0.2% | 97.4% |  |
| LOAD_ATTR_PROPERTY | 995,092 | 0.2% | 97.6% | 1.2% |
| CALL_METHOD_DESCRIPTOR_O | 966,430 | 0.2% | 97.8% | 0.0% |
| LOAD_FAST_CHECK | 822,572 | 0.1% | 97.9% |  |
| LIST_APPEND | 796,698 | 0.1% | 98.1% |  |
| FOR_ITER_RANGE | 738,655 | 0.1% | 98.2% |  |
| LOAD_FAST_AND_CLEAR | 733,869 | 0.1% | 98.3% |  |
| BINARY_SUBSCR | 636,076 | 0.1% | 98.4% |  |
| CALL_LEN | 618,947 | 0.1% | 98.6% |  |
| CALL_TUPLE_1 | 583,120 | 0.1% | 98.7% |  |
| COMPARE_OP | 565,340 | 0.1% | 98.8% |  |
| DICT_MERGE | 564,260 | 0.1% | 98.9% |  |
| TO_BOOL_LIST | 528,893 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_LIST_INT | 468,634 | 0.1% | 99.0% |  |
| LIST_EXTEND | 458,514 | 0.1% | 99.1% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 409,216 | 0.1% | 99.2% |  |
| CALL_KW | 345,237 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_INT | 329,454 | 0.1% | 99.3% |  |
| CALL_LIST_APPEND | 257,086 | 0.0% | 99.4% |  |
| BINARY_OP_ADD_FLOAT | 245,836 | 0.0% | 99.4% |  |
| UNARY_NOT | 245,082 | 0.0% | 99.5% |  |
| TO_BOOL_NONE | 240,424 | 0.0% | 99.5% | 0.1% |
| BINARY_OP_SUBTRACT_FLOAT | 229,207 | 0.0% | 99.5% |  |
| CALL_BUILTIN_O | 154,260 | 0.0% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 142,384 | 0.0% | 99.6% | 4.5% |
| MAKE_CELL | 137,900 | 0.0% | 99.6% |  |
| STORE_DEREF | 137,660 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_DICT | 114,880 | 0.0% | 99.7% |  |
| BINARY_OP_MULTIPLY_FLOAT | 112,600 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_STR_INT | 112,600 | 0.0% | 99.7% |  |
| STORE_ATTR | 100,900 | 0.0% | 99.7% |  |
| LOAD_ATTR_SLOT | 99,760 | 0.0% | 99.7% |  |
| STORE_ATTR_SLOT | 97,980 | 0.0% | 99.8% |  |
| LOAD_ATTR_CLASS | 91,549 | 0.0% | 99.8% |  |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 0.0% | 99.8% |  |
| DELETE_ATTR | 86,397 | 0.0% | 99.8% |  |
| DELETE_SUBSCR | 78,218 | 0.0% | 99.8% |  |
| EXIT_INIT_CHECK | 68,300 | 0.0% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 68,300 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 63,680 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 55,680 | 0.0% | 99.9% |  |
| POP_EXCEPT | 48,216 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 48,216 | 0.0% | 99.9% |  |
| IS_OP | 46,966 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 43,340 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 42,456 | 0.0% | 99.9% |  |
| BUILD_STRING | 41,600 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 39,160 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 39,040 | 0.0% | 99.9% |  |
| IMPORT_NAME | 33,760 | 0.0% | 99.9% |  |
| IMPORT_FROM | 33,420 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 31,476 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 31,298 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 30,220 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 28,160 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 27,480 | 0.0% | 100.0% |  |
| BINARY_SLICE | 19,820 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 18,900 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 17,852 | 0.0% | 100.0% |  |
| RERAISE | 17,280 | 0.0% | 100.0% |  |
| CALL_STR_1 | 11,900 | 0.0% | 100.0% |  |
| END_FOR | 11,520 | 0.0% | 100.0% |  |
| STORE_NAME | 7,480 | 0.0% | 100.0% |  |
| RESUME | 5,980 | 0.0% | 100.0% | 0.1% |
| RAISE_VARARGS | 5,780 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 5,760 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 3,840 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 2,800 | 0.0% | 100.0% |  |
| LOAD_NAME | 2,200 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 1,440 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 926 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 920 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 280 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 160 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 140 | 0.0% | 100.0% | 14.3% |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 21,250,348 | 3.9% | 3.9% |
| RESUME_CHECK LOAD_FAST | 19,452,305 | 3.5% | 7.4% |
| STORE_FAST LOAD_FAST | 12,573,973 | 2.3% | 9.7% |
| CACHE RESUME_CHECK | 12,154,800 | 2.2% | 11.9% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,543,595 | 2.1% | 14.0% |
| LOAD_FAST RETURN_VALUE | 10,518,504 | 1.9% | 15.9% |
| RETURN_VALUE INTERPRETER_EXIT | 10,347,036 | 1.9% | 17.7% |
| POP_TOP JUMP_BACKWARD | 8,661,852 | 1.6% | 19.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 7,852,407 | 1.4% | 20.7% |
| LOAD_FAST LOAD_ATTR | 7,736,220 | 1.4% | 22.1% |
| POP_TOP LOAD_FAST | 7,285,853 | 1.3% | 23.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 7,257,918 | 1.3% | 24.8% |
| RESUME_CHECK POP_TOP | 6,913,520 | 1.3% | 26.0% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,335,920 | 1.1% | 27.2% |
| YIELD_VALUE STORE_FAST | 6,335,920 | 1.1% | 28.3% |
| FOR_ITER_GEN RESUME_CHECK | 6,335,920 | 1.1% | 29.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 6,258,645 | 1.1% | 30.6% |
| NOP LOAD_FAST | 6,226,088 | 1.1% | 31.7% |
| RETURN_CONST POP_TOP | 5,894,260 | 1.1% | 32.8% |
| FOR_ITER_LIST STORE_FAST_LOAD_FAST | 5,760,060 | 1.0% | 33.9% |
| STORE_FAST JUMP_BACKWARD | 5,760,000 | 1.0% | 34.9% |
| STORE_FAST_LOAD_FAST YIELD_VALUE | 5,760,000 | 1.0% | 35.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 5,502,517 | 1.0% | 36.9% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 5,008,896 | 0.9% | 37.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,006,745 | 0.9% | 38.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 4,951,673 | 0.9% | 39.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 4,669,310 | 0.8% | 40.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 4,139,361 | 0.8% | 41.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,909,307 | 0.7% | 42.0% |
| LOAD_FAST LOAD_CONST | 3,859,675 | 0.7% | 42.7% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 3,796,478 | 0.7% | 43.4% |
| LOAD_CONST LOAD_CONST | 3,780,654 | 0.7% | 44.0% |
| STORE_FAST NOP | 3,742,938 | 0.7% | 44.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,669,956 | 0.7% | 45.4% |
| LOAD_FAST PUSH_NULL | 3,669,006 | 0.7% | 46.0% |
| LOAD_GLOBAL_MODULE BINARY_OP | 3,633,869 | 0.7% | 46.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,531,355 | 0.6% | 47.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,521,776 | 0.6% | 48.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 3,517,782 | 0.6% | 48.6% |
| PUSH_NULL LOAD_FAST | 3,450,391 | 0.6% | 49.3% |
| LOAD_ATTR LOAD_FAST | 3,355,091 | 0.6% | 49.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 3,264,409 | 0.6% | 50.5% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 3,011,725 | 0.5% | 51.0% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,981,930 | 0.5% | 51.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,952,192 | 0.5% | 52.1% |
| BINARY_OP COPY | 2,749,654 | 0.5% | 52.6% |
| COPY TO_BOOL_INT | 2,749,334 | 0.5% | 53.1% |
| COPY STORE_FAST | 2,630,400 | 0.5% | 53.5% |
| STORE_FAST COPY | 2,629,760 | 0.5% | 54.0% |
| CALL STORE_FAST | 2,589,591 | 0.5% | 54.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 2,553,159 | 0.5% | 55.0% |
| CALL RETURN_VALUE | 2,432,561 | 0.4% | 55.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,398,086 | 0.4% | 55.8% |
| LOAD_ATTR_MODULE PUSH_NULL | 2,239,894 | 0.4% | 56.2% |
| CALL POP_TOP | 2,228,624 | 0.4% | 56.6% |
| RETURN_VALUE STORE_FAST | 2,212,919 | 0.4% | 57.0% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,158,227 | 0.4% | 57.4% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 2,110,812 | 0.4% | 57.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 2,097,851 | 0.4% | 58.2% |
| LOAD_CONST CALL | 2,079,949 | 0.4% | 58.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,069,930 | 0.4% | 59.0% |
| POP_JUMP_IF_FALSE RETURN_CONST | 2,066,834 | 0.4% | 59.3% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,016,728 | 0.4% | 59.7% |
| PUSH_NULL CALL | 2,014,885 | 0.4% | 60.1% |
| LOAD_CONST COMPARE_OP_INT | 1,996,412 | 0.4% | 60.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 1,992,338 | 0.4% | 60.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,927,512 | 0.3% | 61.1% |
| POP_TOP RETURN_CONST | 1,898,951 | 0.3% | 61.5% |
| RETURN_VALUE RETURN_VALUE | 1,897,564 | 0.3% | 61.8% |
| LOAD_FAST_LOAD_FAST CALL | 1,870,095 | 0.3% | 62.2% |
| LOAD_FAST CALL_FUNCTION_EX | 1,849,725 | 0.3% | 62.5% |
| RETURN_CONST INTERPRETER_EXIT | 1,818,216 | 0.3% | 62.8% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 1,817,702 | 0.3% | 63.2% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,798,526 | 0.3% | 63.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,790,358 | 0.3% | 63.8% |
| POP_TOP LOAD_CONST | 1,730,129 | 0.3% | 64.1% |
| NOP LOAD_GLOBAL_MODULE | 1,726,641 | 0.3% | 64.4% |
| COPY_FREE_VARS RESUME_CHECK | 1,719,614 | 0.3% | 64.7% |
| LOAD_DEREF LOAD_FAST | 1,713,994 | 0.3% | 65.1% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 1,713,474 | 0.3% | 65.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,706,161 | 0.3% | 65.7% |
| LOAD_ATTR_INSTANCE_VALUE CONTAINS_OP | 1,705,482 | 0.3% | 66.0% |
| LOAD_FAST BUILD_TUPLE | 1,696,481 | 0.3% | 66.3% |
| LOAD_CONST LOAD_FAST | 1,666,687 | 0.3% | 66.6% |
| STORE_SUBSCR_DICT LOAD_FAST | 1,636,127 | 0.3% | 66.9% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 1,623,754 | 0.3% | 67.2% |
| UNARY_INVERT BINARY_OP | 1,620,053 | 0.3% | 67.5% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 1,603,934 | 0.3% | 67.8% |
| FOR_ITER_LIST STORE_FAST | 1,601,855 | 0.3% | 68.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,578,732 | 0.3% | 68.3% |
| POP_TOP NOP | 1,534,660 | 0.3% | 68.6% |
| GET_ITER FOR_ITER_LIST | 1,533,226 | 0.3% | 68.9% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,518,530 | 0.3% | 69.2% |
| CALL LOAD_FAST | 1,515,642 | 0.3% | 69.5% |
| LOAD_FAST GET_ITER | 1,454,089 | 0.3% | 69.7% |
| RETURN_VALUE POP_TOP | 1,439,583 | 0.3% | 70.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,437,280 | 0.3% | 70.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL | 1,436,568 | 0.3% | 70.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,435,397 | 0.3% | 70.8% |
| POP_JUMP_IF_FALSE POP_TOP | 1,417,609 | 0.3% | 71.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 18,520 | 93.4% |
| LOAD_CONST | 980 | 4.9% |
| LOAD_FAST | 280 | 1.4% |
| BINARY_OP | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,900 | 95.4% |
| BUILD_TUPLE | 280 | 1.4% |
| LOAD_DEREF | 280 | 1.4% |
| STORE_FAST | 280 | 1.4% |
| CALL | 80 | 0.4% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,154,800 | 95.3% |
| COPY_FREE_VARS | 584,213 | 4.6% |
| POP_TOP | 7,460 | 0.1% |
| RESUME | 2,280 | 0.0% |
| MAKE_CELL | 20 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,253,765 | 68.3% |
| CALL | 480,673 | 26.2% |
| LOAD_GLOBAL_MODULE | 82,439 | 4.5% |
| LOAD_FAST | 17,280 | 0.9% |
| RETURN_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,354,684 | 73.8% |
| STORE_FAST | 480,253 | 26.2% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 27,440 | 99.9% |
| BINARY_OP | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 27,480 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 576,080 | 90.6% |
| LOAD_CONST | 59,036 | 9.3% |
| BINARY_SUBSCR | 880 | 0.1% |
| CALL | 40 | 0.0% |
| CALL_BUILTIN_O | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 575,920 | 90.5% |
| STORE_FAST | 58,756 | 9.2% |
| BINARY_SUBSCR | 880 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 37,296 | 87.8% |
| LOAD_ATTR_MODULE | 5,100 | 12.0% |
| LOAD_GLOBAL | 40 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 42,456 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,899 | 48.5% |
| CALL | 27,519 | 35.2% |
| LOAD_ATTR_INSTANCE_VALUE | 12,718 | 16.3% |
| LOAD_ATTR | 82 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,799 | 77.7% |
| RETURN_CONST | 10,239 | 13.1% |
| LOAD_FAST | 7,040 | 9.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.2% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 11,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,520 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 68,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 68,300 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 28,160 | 50.6% |
| LOAD_FAST | 27,520 | 49.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 41,600 | 74.7% |
| BUILD_STRING | 14,080 | 25.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,454,089 | 62.7% |
| STORE_FAST_LOAD_FAST | 576,000 | 24.8% |
| CALL_BUILTIN_CLASS | 260,897 | 11.3% |
| CALL | 14,340 | 0.6% |
| RETURN_VALUE | 5,760 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,533,226 | 66.1% |
| LOAD_FAST_AND_CLEAR | 488,643 | 21.1% |
| FOR_ITER_RANGE | 253,982 | 11.0% |
| FOR_ITER | 12,115 | 0.5% |
| FOR_ITER_TUPLE | 11,740 | 0.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,347,036 | 81.2% |
| RETURN_CONST | 1,818,216 | 14.3% |
| YIELD_VALUE | 577,740 | 4.5% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 500 | 89.3% |
| POP_TOP | 60 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 39,040 | 61.3% |
| STORE_FAST | 14,080 | 22.1% |
| LOAD_FAST | 7,040 | 11.1% |
| STORE_NAME | 2,480 | 3.9% |
| LOAD_CONST | 560 | 0.9% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,742,938 | 38.3% |
| POP_TOP | 1,534,660 | 15.7% |
| RESUME_CHECK | 1,331,301 | 13.6% |
| POP_JUMP_IF_FALSE | 1,306,808 | 13.4% |
| JUMP_BACKWARD | 1,088,000 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,226,088 | 63.7% |
| LOAD_GLOBAL_MODULE | 1,726,641 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 699,149 | 7.2% |
| LOAD_FAST_LOAD_FAST | 583,320 | 6.0% |
| LOAD_CONST | 530,020 | 5.4% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 31,476 | 65.3% |
| COPY | 11,520 | 23.9% |
| POP_TOP | 5,200 | 10.8% |
| STORE_SUBSCR_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 31,476 | 65.3% |
| RERAISE | 11,520 | 23.9% |
| JUMP_FORWARD | 5,120 | 10.6% |
| RETURN_CONST | 60 | 0.1% |
| JUMP_BACKWARD | 20 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,913,520 | 29.8% |
| RETURN_CONST | 5,894,260 | 25.4% |
| CALL | 2,228,624 | 9.6% |
| RETURN_VALUE | 1,439,583 | 6.2% |
| POP_JUMP_IF_FALSE | 1,417,609 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,661,852 | 37.3% |
| LOAD_FAST | 7,285,853 | 31.4% |
| RETURN_CONST | 1,898,951 | 8.2% |
| LOAD_CONST | 1,730,129 | 7.4% |
| NOP | 1,534,660 | 6.6% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 36,916 | 76.6% |
| RERAISE | 5,760 | 11.9% |
| CALL_KW | 5,120 | 10.6% |
| BINARY_SUBSCR_DICT | 300 | 0.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 37,256 | 77.3% |
| WITH_EXCEPT_START | 5,760 | 11.9% |
| LOAD_GLOBAL_MODULE | 5,080 | 10.5% |
| LOAD_GLOBAL | 120 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,669,006 | 50.1% |
| LOAD_ATTR_MODULE | 2,239,894 | 30.6% |
| LOAD_ATTR | 1,284,411 | 17.5% |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,450,391 | 47.1% |
| CALL | 2,014,885 | 27.5% |
| LOAD_FAST_LOAD_FAST | 1,396,398 | 19.1% |
| LOAD_CONST | 321,033 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 64,704 | 0.9% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,420 | 97.5% |
| COPY_FREE_VARS | 340 | 1.8% |
| CALL | 140 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,760 | 30.5% |
| LOAD_FAST | 5,760 | 30.5% |
| STORE_FAST | 5,760 | 30.5% |
| CALL_METHOD_DESCRIPTOR_O | 1,300 | 6.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 280 | 1.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,518,504 | 51.1% |
| CALL | 2,432,561 | 11.8% |
| RETURN_VALUE | 1,897,564 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,518,530 | 7.4% |
| CALL_FUNCTION_EX | 1,265,545 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 10,347,036 | 50.2% |
| STORE_FAST | 2,212,919 | 10.7% |
| RETURN_VALUE | 1,897,564 | 9.2% |
| POP_TOP | 1,439,583 | 7.0% |
| LOAD_FAST_LOAD_FAST | 1,129,601 | 5.5% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 14,080 | 45.0% |
| LOAD_FAST | 10,478 | 33.5% |
| LOAD_ATTR_INSTANCE_VALUE | 5,800 | 18.5% |
| STORE_SUBSCR | 660 | 2.1% |
| LOAD_ATTR | 200 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 19,960 | 63.8% |
| LOAD_GLOBAL_MODULE | 10,200 | 32.6% |
| STORE_SUBSCR | 660 | 2.1% |
| STORE_SUBSCR_DICT | 279 | 0.9% |
| LOAD_GLOBAL | 80 | 0.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,012,479 | 94.3% |
| LOAD_ATTR_INSTANCE_VALUE | 53,498 | 5.0% |
| TO_BOOL | 3,522 | 0.3% |
| LOAD_ATTR | 886 | 0.1% |
| RETURN_VALUE | 770 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 833,972 | 77.7% |
| POP_JUMP_IF_FALSE | 233,339 | 21.7% |
| TO_BOOL | 3,522 | 0.3% |
| TO_BOOL_BOOL | 2,162 | 0.2% |
| TO_BOOL_NONE | 360 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,129,601 | 69.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 490,372 | 30.3% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,620,053 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 245,042 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 245,082 | 100.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 5,680 | 98.6% |
| TO_BOOL | 80 | 1.4% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,633,869 | 53.5% |
| UNARY_INVERT | 1,620,053 | 23.9% |
| POP_JUMP_IF_FALSE | 1,129,601 | 16.6% |
| LOAD_ATTR | 259,326 | 3.8% |
| LOAD_FAST_LOAD_FAST | 84,160 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,749,654 | 40.5% |
| STORE_FAST | 1,389,247 | 20.5% |
| TO_BOOL_INT | 1,129,661 | 16.6% |
| UNARY_INVERT | 1,129,601 | 16.6% |
| BUILD_TUPLE | 245,226 | 3.6% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 50.0% |
| STORE_FAST | 140 | 50.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 488,643 | 33.4% |
| JUMP_FORWARD | 474,353 | 32.4% |
| LOAD_FAST | 245,896 | 16.8% |
| POP_TOP | 228,477 | 15.6% |
| STORE_ATTR_INSTANCE_VALUE | 10,660 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 491,593 | 33.6% |
| SWAP | 488,643 | 33.4% |
| STORE_FAST | 475,813 | 32.5% |
| RETURN_VALUE | 5,120 | 0.4% |
| COMPARE_OP | 280 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 576,000 | 34.8% |
| LOAD_FAST | 529,560 | 32.0% |
| RESUME_CHECK | 484,553 | 29.3% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 2.1% |
| POP_JUMP_IF_NOT_NONE | 17,280 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,061,673 | 64.2% |
| BUILD_TUPLE | 576,020 | 34.8% |
| STORE_FAST | 17,280 | 1.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 27,520 | 66.2% |
| FORMAT_SIMPLE | 14,080 | 33.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 27,440 | 66.0% |
| RETURN_VALUE | 14,080 | 33.8% |
| BINARY_OP | 80 | 0.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,696,481 | 40.0% |
| LOAD_FAST_LOAD_FAST | 1,160,320 | 27.4% |
| BUILD_MAP | 576,020 | 13.6% |
| RETURN_VALUE | 512,000 | 12.1% |
| BINARY_OP | 245,226 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,152,100 | 27.2% |
| CALL | 1,131,161 | 26.7% |
| BUILD_MAP | 576,000 | 13.6% |
| STORE_FAST | 512,000 | 12.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 511,960 | 12.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,079,949 | 18.5% |
| PUSH_NULL | 2,014,885 | 17.9% |
| LOAD_FAST_LOAD_FAST | 1,870,095 | 16.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,436,568 | 12.8% |
| BUILD_TUPLE | 1,131,161 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,589,591 | 23.0% |
| RETURN_VALUE | 2,432,561 | 21.6% |
| POP_TOP | 2,228,624 | 19.8% |
| LOAD_FAST | 1,515,642 | 13.5% |
| CALL_TUPLE_1 | 581,740 | 5.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,849,725 | 76.6% |
| DICT_MERGE | 564,260 | 23.4% |
| CALL_INTRINSIC_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,265,545 | 52.4% |
| RESUME_CHECK | 535,040 | 22.2% |
| CALL_BUILTIN_CLASS | 511,960 | 21.2% |
| POP_TOP | 95,360 | 4.0% |
| STORE_FAST | 5,760 | 0.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 140 | 87.5% |
| CALL_FUNCTION_EX | 20 | 12.5% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 345,237 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 275,757 | 79.9% |
| LOAD_FAST | 28,800 | 8.3% |
| RETURN_VALUE | 21,120 | 6.1% |
| STORE_FAST | 14,220 | 4.1% |
| PUSH_EXC_INFO | 5,120 | 1.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 560,855 | 99.2% |
| COMPARE_OP | 1,299 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,249 | 0.2% |
| LOAD_GLOBAL_MODULE | 380 | 0.1% |
| LOAD_FAST | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 562,066 | 99.4% |
| COMPARE_OP | 1,299 | 0.2% |
| COMPARE_OP_INT | 1,175 | 0.2% |
| COMPARE_OP_STR | 440 | 0.1% |
| POP_JUMP_IF_TRUE | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,705,482 | 99.9% |
| LOAD_ATTR_MODULE | 560 | 0.0% |
| LOAD_FAST | 480 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR | 119 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,706,161 | 100.0% |
| POP_JUMP_IF_TRUE | 480 | 0.0% |
| STORE_FAST | 140 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 14,040 | 49.9% |
| CALL_BUILTIN_FAST | 14,040 | 49.9% |
| BINARY_SUBSCR | 40 | 0.1% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 28,160 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 2,749,654 | 38.6% |
| STORE_FAST | 2,629,760 | 36.9% |
| LOAD_CONST | 1,100,800 | 15.4% |
| LOAD_FAST | 590,100 | 8.3% |
| STORE_ATTR_INSTANCE_VALUE | 21,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 2,749,334 | 38.5% |
| STORE_FAST | 2,630,400 | 36.9% |
| STORE_FAST_STORE_FAST | 1,093,760 | 15.3% |
| LOAD_ATTR_INSTANCE_VALUE | 575,842 | 8.1% |
| LOAD_FAST | 28,160 | 0.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 1,129,601 | 65.7% |
| CACHE | 584,213 | 34.0% |
| CALL | 5,940 | 0.3% |
| CALL_PY_EXACT_ARGS | 360 | 0.0% |
| CALL_FUNCTION_EX | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,719,614 | 100.0% |
| RETURN_GENERATOR | 340 | 0.0% |
| RESUME | 320 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,397 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,598 | 66.7% |
| RETURN_CONST | 27,519 | 31.9% |
| LOAD_GLOBAL_MODULE | 1,240 | 1.4% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,700 | 93.9% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 6.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 564,260 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,271,225 | 97.4% |
| SWAP | 14,160 | 1.1% |
| GET_ITER | 12,115 | 0.9% |
| LOAD_FAST | 6,060 | 0.5% |
| FOR_ITER | 1,700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 688,680 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 581,600 | 44.6% |
| SWAP | 14,080 | 1.1% |
| RETURN_CONST | 11,820 | 0.9% |
| LOAD_GLOBAL_MODULE | 5,680 | 0.4% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 33,080 | 99.0% |
| STORE_NAME | 340 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 32,640 | 97.7% |
| STORE_NAME | 780 | 2.3% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 33,080 | 98.0% |
| STORE_NAME | 680 | 2.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 27,520 | 58.6% |
| LOAD_FAST | 17,420 | 37.1% |
| LOAD_GLOBAL_MODULE | 1,986 | 4.2% |
| LOAD_GLOBAL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 46,826 | 99.7% |
| POP_JUMP_IF_TRUE | 140 | 0.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,661,852 | 47.2% |
| STORE_FAST | 5,760,000 | 31.4% |
| POP_JUMP_IF_NOT_NONE | 970,014 | 5.3% |
| LIST_APPEND | 796,698 | 4.3% |
| POP_JUMP_IF_FALSE | 734,368 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 7,852,407 | 42.8% |
| FOR_ITER_GEN | 6,335,920 | 34.5% |
| FOR_ITER | 1,271,225 | 6.9% |
| NOP | 1,088,000 | 5.9% |
| LOAD_FAST | 729,693 | 4.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 31,476 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 31,196 | 99.1% |
| LOAD_FAST | 280 | 0.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 988,881 | 87.9% |
| POP_TOP | 117,534 | 10.5% |
| STORE_ATTR_INSTANCE_VALUE | 7,020 | 0.6% |
| BINARY_SUBSCR_TUPLE_INT | 5,720 | 0.5% |
| POP_EXCEPT | 5,120 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 606,823 | 54.0% |
| BUILD_LIST | 474,353 | 42.2% |
| LOAD_GLOBAL_MODULE | 24,819 | 2.2% |
| LOAD_FAST_LOAD_FAST | 7,320 | 0.7% |
| STORE_FAST | 5,760 | 0.5% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 436,812 | 54.8% |
| LOAD_ATTR | 245,246 | 30.8% |
| BINARY_SUBSCR_STR_INT | 112,600 | 14.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,000 | 0.3% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 796,698 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 229,897 | 50.1% |
| RETURN_VALUE | 228,477 | 49.8% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_DEREF | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 229,117 | 50.0% |
| STORE_FAST | 228,477 | 49.8% |
| RETURN_VALUE | 640 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |
| STORE_NAME | 120 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,736,220 | 76.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,790,358 | 17.8% |
| LOAD_GLOBAL_MODULE | 385,397 | 3.8% |
| CALL | 83,860 | 0.8% |
| LOAD_ATTR | 22,782 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,355,091 | 33.4% |
| PUSH_NULL | 1,284,411 | 12.8% |
| STORE_SUBSCR_DICT | 1,129,521 | 11.2% |
| POP_JUMP_IF_NOT_NONE | 1,104,114 | 11.0% |
| STORE_FAST | 718,851 | 7.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,859,675 | 26.1% |
| LOAD_CONST | 3,780,654 | 25.6% |
| POP_TOP | 1,730,129 | 11.7% |
| POP_JUMP_IF_FALSE | 907,882 | 6.1% |
| STORE_FAST | 628,285 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,780,654 | 25.6% |
| CALL | 2,079,949 | 14.1% |
| COMPARE_OP_INT | 1,996,412 | 13.5% |
| LOAD_FAST | 1,666,687 | 11.3% |
| COPY | 1,100,800 | 7.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,713,474 | 96.8% |
| POP_JUMP_IF_NOT_NONE | 27,520 | 1.6% |
| STORE_DEREF | 27,520 | 1.6% |
| STORE_FAST | 440 | 0.0% |
| POP_JUMP_IF_FALSE | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,713,994 | 96.8% |
| POP_JUMP_IF_NOT_NONE | 55,040 | 3.1% |
| PUSH_NULL | 460 | 0.0% |
| LOAD_CONST | 280 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 19,452,305 | 19.9% |
| STORE_FAST | 12,573,973 | 12.9% |
| POP_TOP | 7,285,853 | 7.5% |
| POP_JUMP_IF_FALSE | 6,258,645 | 6.4% |
| NOP | 6,226,088 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 21,250,348 | 21.8% |
| RETURN_VALUE | 10,518,504 | 10.8% |
| LOAD_ATTR | 7,736,220 | 7.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 7,257,918 | 7.4% |
| CALL_PY_EXACT_ARGS | 5,006,745 | 5.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 488,643 | 66.6% |
| LOAD_FAST_AND_CLEAR | 245,226 | 33.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 488,643 | 66.6% |
| LOAD_FAST_AND_CLEAR | 245,226 | 33.4% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 576,560 | 70.1% |
| POP_JUMP_IF_NONE | 229,127 | 27.9% |
| LOAD_ATTR_CLASS | 16,565 | 2.0% |
| LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 575,920 | 70.0% |
| LOAD_GLOBAL_MODULE | 229,047 | 27.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 16,525 | 2.0% |
| POP_JUMP_IF_NOT_NONE | 560 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,553,159 | 16.2% |
| LOAD_FAST_LOAD_FAST | 1,992,338 | 12.6% |
| POP_JUMP_IF_FALSE | 1,927,512 | 12.2% |
| PUSH_NULL | 1,396,398 | 8.9% |
| LOAD_SUPER_ATTR_METHOD | 1,143,881 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,517,782 | 22.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,158,227 | 13.7% |
| LOAD_FAST_LOAD_FAST | 1,992,338 | 12.6% |
| CALL | 1,870,095 | 11.9% |
| BUILD_TUPLE | 1,160,320 | 7.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,000 | 11.2% |
| RESUME_CHECK | 1,720 | 9.6% |
| POP_JUMP_IF_FALSE | 1,713 | 9.6% |
| LOAD_FAST | 1,600 | 9.0% |
| RESUME | 1,520 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,820 | 38.2% |
| LOAD_ATTR | 3,326 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 2,740 | 15.3% |
| LOAD_FAST | 2,166 | 12.1% |
| CALL | 740 | 4.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 820 | 37.3% |
| LOAD_CONST | 600 | 27.3% |
| RESUME | 560 | 25.5% |
| PUSH_NULL | 120 | 5.5% |
| POP_TOP | 80 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 640 | 29.1% |
| CALL | 500 | 22.7% |
| LOAD_ATTR | 420 | 19.1% |
| LOAD_CONST | 380 | 17.3% |
| PUSH_NULL | 220 | 10.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 200 | 38.5% |
| PUSH_NULL | 80 | 15.4% |
| LOAD_FAST_LOAD_FAST | 80 | 15.4% |
| LOAD_SUPER_ATTR_ATTR | 80 | 15.4% |
| CALL | 40 | 7.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| CALL_PY_EXACT_ARGS | 27,800 | 20.2% |
| CACHE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| RESUME_CHECK | 27,820 | 20.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 5,008,896 | 29.0% |
| TO_BOOL_BOOL | 3,796,478 | 22.0% |
| COMPARE_OP_INT | 3,669,956 | 21.3% |
| CONTAINS_OP | 1,706,161 | 9.9% |
| COMPARE_OP_STR | 1,435,397 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,258,645 | 36.3% |
| RETURN_CONST | 2,066,834 | 12.0% |
| LOAD_FAST_LOAD_FAST | 1,927,512 | 11.2% |
| POP_TOP | 1,417,609 | 8.2% |
| LOAD_GLOBAL_MODULE | 1,406,326 | 8.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,025,064 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 47,800 | 4.3% |
| LOAD_ATTR | 28,300 | 2.6% |
| RETURN_VALUE | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 282,582 | 25.6% |
| LOAD_FAST | 274,779 | 24.9% |
| NOP | 266,397 | 24.2% |
| LOAD_FAST_CHECK | 229,127 | 20.8% |
| RETURN_CONST | 24,340 | 2.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,398,086 | 48.4% |
| LOAD_ATTR | 1,104,114 | 22.3% |
| LOAD_ATTR_INSTANCE_VALUE | 938,563 | 18.9% |
| RETURN_VALUE | 437,452 | 8.8% |
| LOAD_DEREF | 55,040 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,016,728 | 40.7% |
| RETURN_CONST | 1,105,468 | 22.3% |
| JUMP_BACKWARD | 970,014 | 19.6% |
| NOP | 483,014 | 9.7% |
| LOAD_CONST | 228,757 | 4.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,798,526 | 67.3% |
| TO_BOOL | 833,972 | 31.2% |
| TO_BOOL_NONE | 19,700 | 0.7% |
| COMPARE_OP_STR | 10,937 | 0.4% |
| COMPARE_OP_INT | 3,386 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 892,653 | 33.4% |
| LOAD_FAST_LOAD_FAST | 836,726 | 31.3% |
| RETURN_CONST | 736,926 | 27.6% |
| LOAD_GLOBAL_MODULE | 71,014 | 2.7% |
| RETURN_VALUE | 58,716 | 2.2% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,760 | 99.7% |
| CALL_KW | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,760 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 11,520 | 66.7% |
| POP_JUMP_IF_TRUE | 5,760 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,760 | 50.0% |
| COPY | 5,760 | 50.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 2,110,812 | 26.2% |
| POP_JUMP_IF_FALSE | 2,066,834 | 25.6% |
| POP_TOP | 1,898,951 | 23.6% |
| POP_JUMP_IF_NOT_NONE | 1,105,468 | 13.7% |
| POP_JUMP_IF_TRUE | 736,926 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,894,260 | 73.1% |
| INTERPRETER_EXIT | 1,818,216 | 22.6% |
| TO_BOOL_BOOL | 183,395 | 2.3% |
| EXIT_INIT_CHECK | 68,300 | 0.8% |
| STORE_FAST | 60,556 | 0.8% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 39,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 37,920 | 97.1% |
| STORE_NAME | 780 | 2.0% |
| LOAD_GLOBAL_MODULE | 280 | 0.7% |
| LOAD_FAST | 60 | 0.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,562 | 58.0% |
| LOAD_FAST_LOAD_FAST | 22,040 | 21.8% |
| LOAD_ATTR_INSTANCE_VALUE | 17,280 | 17.1% |
| STORE_ATTR | 2,520 | 2.5% |
| LOAD_ATTR | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 44,840 | 44.4% |
| LOAD_FAST_LOAD_FAST | 14,760 | 14.6% |
| LOAD_FAST | 13,639 | 13.5% |
| LOAD_CONST | 12,642 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 5,680 | 5.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_BUILTIN | 27,520 | 20.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 54,960 | 39.9% |
| LOAD_DEREF | 27,520 | 20.0% |
| LOAD_FAST | 27,520 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 27,480 | 20.0% |
| LOAD_GLOBAL | 120 | 0.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,335,920 | 21.8% |
| COPY | 2,630,400 | 9.1% |
| CALL | 2,589,591 | 8.9% |
| RETURN_VALUE | 2,212,919 | 7.6% |
| FOR_ITER_LIST | 1,601,855 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,573,973 | 43.3% |
| JUMP_BACKWARD | 5,760,000 | 19.8% |
| NOP | 3,742,938 | 12.9% |
| COPY | 2,629,760 | 9.1% |
| LOAD_GLOBAL_BUILTIN | 1,155,725 | 4.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,760,060 | 89.1% |
| FOR_ITER | 688,680 | 10.7% |
| COPY | 14,080 | 0.2% |
| FOR_ITER_TUPLE | 2,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 5,760,000 | 89.1% |
| GET_ITER | 576,000 | 8.9% |
| LOAD_FAST | 112,640 | 1.7% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 0.2% |
| TO_BOOL_STR | 2,000 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,097,851 | 43.8% |
| COPY | 1,093,760 | 22.8% |
| UNPACK_SEQUENCE_TUPLE | 1,088,220 | 22.7% |
| STORE_FAST_STORE_FAST | 512,000 | 10.7% |
| UNPACK_SEQUENCE | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,578,732 | 32.9% |
| STORE_FAST | 1,088,280 | 22.7% |
| LOAD_FAST_LOAD_FAST | 1,015,499 | 21.2% |
| JUMP_BACKWARD | 581,760 | 12.1% |
| STORE_FAST_STORE_FAST | 512,000 | 10.7% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,480 | 33.2% |
| CALL | 1,200 | 16.0% |
| IMPORT_FROM | 780 | 10.4% |
| SET_FUNCTION_ATTRIBUTE | 780 | 10.4% |
| IMPORT_NAME | 680 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,640 | 62.0% |
| LOAD_NAME | 820 | 11.0% |
| RETURN_CONST | 700 | 9.4% |
| LOAD_BUILD_CLASS | 500 | 6.7% |
| POP_TOP | 440 | 5.9% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 575,921 | 22.6% |
| BUILD_LIST | 488,643 | 19.2% |
| LOAD_FAST_AND_CLEAR | 488,643 | 19.2% |
| FOR_ITER_LIST | 473,703 | 18.6% |
| LOAD_FAST | 256,927 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 575,842 | 22.6% |
| LOAD_CONST | 502,153 | 19.7% |
| BUILD_LIST | 488,643 | 19.2% |
| STORE_FAST | 488,643 | 19.2% |
| FOR_ITER_LIST | 473,623 | 18.6% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 260 | 28.3% |
| FOR_ITER | 240 | 26.1% |
| LOAD_FAST | 120 | 13.0% |
| RETURN_VALUE | 80 | 8.7% |
| LOAD_FAST_CHECK | 80 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 360 | 39.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 37.0% |
| UNPACK_SEQUENCE_TUPLE | 100 | 10.9% |
| LOAD_FAST | 40 | 4.3% |
| STORE_FAST | 40 | 4.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,000 | 83.3% |
| BUILD_TUPLE | 1,152,100 | 16.7% |
| CALL_STR_1 | 1,260 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,335,920 | 91.6% |
| INTERPRETER_EXIT | 577,740 | 8.4% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,820 | 47.2% |
| CACHE | 2,280 | 38.1% |
| COPY_FREE_VARS | 320 | 5.4% |
| CALL_KW | 200 | 3.3% |
| POP_TOP | 140 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 48.2% |
| LOAD_GLOBAL | 1,520 | 25.4% |
| LOAD_NAME | 560 | 9.4% |
| NOP | 280 | 4.7% |
| LOAD_CONST | 240 | 4.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 245,796 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 245,836 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,093,762 | 98.3% |
| LOAD_FAST_LOAD_FAST | 18,480 | 1.7% |
| BINARY_OP | 179 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 575,921 | 51.8% |
| STORE_FAST | 511,980 | 46.0% |
| BINARY_SLICE | 18,520 | 1.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,680 | 0.5% |
| LOAD_CONST | 280 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 32.3% |
| CALL_METHOD_DESCRIPTOR_O | 1,240 | 32.3% |
| LOAD_FAST_LOAD_FAST | 960 | 25.0% |
| BINARY_SUBSCR_LIST_INT | 280 | 7.3% |
| LOAD_FAST | 80 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,740 | 45.3% |
| LOAD_CONST | 1,260 | 32.8% |
| CALL | 480 | 12.5% |
| STORE_FAST | 360 | 9.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 112,560 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 229,047 | 99.9% |
| BINARY_OP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 229,207 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 264,938 | 80.4% |
| LOAD_CONST | 58,636 | 17.8% |
| CALL_LEN | 5,680 | 1.7% |
| BINARY_OP | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 323,734 | 98.3% |
| CALL_BUILTIN_CLASS | 5,680 | 1.7% |
| CALL | 40 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 99,860 | 86.9% |
| LOAD_CONST | 14,280 | 12.4% |
| LOAD_FAST | 700 | 0.6% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 99,860 | 86.9% |
| CONVERT_VALUE | 14,040 | 12.2% |
| STORE_FAST | 400 | 0.3% |
| PUSH_EXC_INFO | 300 | 0.3% |
| LOAD_FAST | 140 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 456,874 | 97.5% |
| LOAD_CONST | 11,640 | 2.5% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 456,914 | 97.5% |
| LOAD_CONST | 11,440 | 2.4% |
| BINARY_OP_ADD_UNICODE | 280 | 0.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 112,600 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,120 | 99.9% |
| BINARY_SUBSCR | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,020 | 84.3% |
| JUMP_FORWARD | 5,720 | 14.6% |
| STORE_FAST | 420 | 1.1% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 33,340 | 48.8% |
| LOAD_GLOBAL_MODULE | 27,480 | 40.2% |
| LOAD_FAST | 7,200 | 10.5% |
| LOAD_FAST_LOAD_FAST | 280 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 68,300 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 64,704 | 45.4% |
| LOAD_FAST | 64,240 | 45.1% |
| LOAD_CONST | 7,480 | 5.3% |
| BINARY_OP_ADD_INT | 5,680 | 4.0% |
| CALL | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 135,984 | 95.5% |
| POP_TOP | 6,280 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 692,689 | 35.4% |
| CALL_FUNCTION_EX | 511,960 | 26.2% |
| LOAD_FAST | 263,576 | 13.5% |
| CALL_BUILTIN_CLASS | 228,397 | 11.7% |
| CALL_LEN | 228,397 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 757,816 | 38.7% |
| STORE_FAST | 692,989 | 35.4% |
| GET_ITER | 260,897 | 13.3% |
| CALL_BUILTIN_CLASS | 228,397 | 11.7% |
| LOAD_FAST | 17,280 | 0.9% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 858,326 | 48.1% |
| LOAD_CONST | 614,834 | 34.5% |
| LOAD_FAST_LOAD_FAST | 173,298 | 9.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 81,309 | 4.6% |
| LOAD_GLOBAL_MODULE | 27,880 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 604,774 | 33.9% |
| STORE_FAST | 582,504 | 32.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 439,459 | 24.6% |
| UNPACK_SEQUENCE_TUPLE | 81,309 | 4.6% |
| POP_TOP | 14,861 | 0.8% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 519,280 | 45.6% |
| BUILD_TUPLE | 511,960 | 45.0% |
| CALL | 65,004 | 5.7% |
| LOAD_FAST_CHECK | 16,525 | 1.5% |
| LOAD_ATTR | 14,000 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,053,900 | 92.6% |
| RETURN_VALUE | 82,209 | 7.2% |
| LOAD_FAST | 1,260 | 0.1% |
| STORE_FAST | 860 | 0.1% |
| BEFORE_WITH | 140 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 112,560 | 73.0% |
| LOAD_ATTR | 27,440 | 17.8% |
| LOAD_FAST | 14,140 | 9.2% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 112,560 | 73.0% |
| LOAD_FAST | 41,520 | 26.9% |
| TO_BOOL_INT | 140 | 0.1% |
| BINARY_SUBSCR | 40 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,147,061 | 100.0% |
| CALL | 180 | 0.0% |
| BUILD_TUPLE | 140 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,147,341 | 100.0% |
| TO_BOOL | 180 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 590,667 | 95.4% |
| LOAD_ATTR_INSTANCE_VALUE | 27,900 | 4.5% |
| CALL | 380 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 344,378 | 55.6% |
| CALL_BUILTIN_CLASS | 228,397 | 36.9% |
| CALL_PY_EXACT_ARGS | 33,160 | 5.4% |
| LOAD_FAST | 5,720 | 0.9% |
| BINARY_OP_SUBTRACT_INT | 5,680 | 0.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 245,146 | 95.4% |
| LOAD_FAST | 11,440 | 4.4% |
| LOAD_CONST | 140 | 0.1% |
| LOAD_FAST_CHECK | 140 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 245,186 | 95.4% |
| LOAD_GLOBAL_MODULE | 11,440 | 4.4% |
| NOP | 280 | 0.1% |
| RETURN_CONST | 140 | 0.1% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,603,934 | 75.9% |
| LOAD_ATTR_INSTANCE_VALUE | 506,527 | 24.0% |
| LOAD_GLOBAL_MODULE | 2,280 | 0.1% |
| LOAD_CONST | 1,240 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,129,881 | 53.4% |
| STORE_FAST | 981,159 | 46.4% |
| LIST_APPEND | 2,000 | 0.1% |
| TO_BOOL_NONE | 1,240 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 37,480 | 86.5% |
| BUILD_TUPLE | 5,680 | 13.1% |
| CALL | 180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 31,860 | 73.5% |
| LOAD_FAST | 11,480 | 26.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,376,026 | 93.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 97,834 | 6.6% |
| LOAD_ATTR | 2,480 | 0.2% |
| CALL | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 628,665 | 42.6% |
| STORE_FAST | 575,960 | 39.0% |
| LOAD_FAST | 85,060 | 5.8% |
| CALL_BUILTIN_FAST | 81,309 | 5.5% |
| RETURN_VALUE | 51,690 | 3.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 886,971 | 91.8% |
| LOAD_CONST | 33,720 | 3.5% |
| CALL | 29,159 | 3.0% |
| RETURN_VALUE | 14,000 | 1.4% |
| RETURN_GENERATOR | 1,300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 916,270 | 94.8% |
| LOAD_CONST | 33,440 | 3.5% |
| RETURN_VALUE | 14,900 | 1.5% |
| BINARY_OP_ADD_UNICODE | 1,240 | 0.1% |
| STORE_FAST | 280 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,006,745 | 43.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,951,673 | 42.7% |
| LOAD_FAST_LOAD_FAST | 818,597 | 7.1% |
| LOAD_SUPER_ATTR_METHOD | 474,273 | 4.1% |
| LOAD_GLOBAL_MODULE | 93,900 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,543,595 | 99.6% |
| MAKE_CELL | 27,800 | 0.2% |
| RETURN_GENERATOR | 18,420 | 0.2% |
| COPY_FREE_VARS | 360 | 0.0% |
| PUSH_EXC_INFO | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,129,521 | 47.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 702,306 | 29.8% |
| LOAD_FAST | 328,186 | 13.9% |
| LOAD_CONST | 107,751 | 4.6% |
| BINARY_OP | 83,760 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,228,045 | 52.1% |
| COPY_FREE_VARS | 1,129,601 | 47.9% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,860 | 99.7% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,220 | 85.9% |
| YIELD_VALUE | 1,260 | 10.6% |
| STORE_FAST | 280 | 2.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 140 | 1.2% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 581,740 | 99.8% |
| LOAD_FAST | 1,240 | 0.2% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 581,720 | 99.8% |
| LOAD_FAST | 1,260 | 0.2% |
| CALL | 140 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 86.1% |
| LOAD_GLOBAL_MODULE | 140 | 9.7% |
| CALL | 60 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,260 | 87.5% |
| PUSH_NULL | 140 | 9.7% |
| LOAD_GLOBAL | 40 | 2.8% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 140 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,996,412 | 54.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,056,826 | 28.8% |
| LOAD_FAST | 576,980 | 15.7% |
| LOAD_FAST_LOAD_FAST | 18,480 | 0.5% |
| CALL_BUILTIN_FAST | 14,000 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,669,956 | 99.9% |
| POP_JUMP_IF_TRUE | 3,386 | 0.1% |
| RETURN_VALUE | 160 | 0.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 97 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,408,294 | 95.5% |
| LOAD_CONST | 59,860 | 4.1% |
| LOAD_FAST | 5,820 | 0.4% |
| COMPARE_OP | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,435,397 | 97.4% |
| COPY | 14,040 | 1.0% |
| LOAD_FAST | 14,040 | 1.0% |
| POP_JUMP_IF_TRUE | 10,937 | 0.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,335,920 | 99.8% |
| GET_ITER | 11,440 | 0.2% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,335,920 | 99.8% |
| POP_TOP | 11,440 | 0.2% |
| RESUME | 80 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,852,407 | 79.6% |
| GET_ITER | 1,533,226 | 15.6% |
| SWAP | 473,623 | 4.8% |
| FOR_ITER | 300 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,060 | 58.4% |
| STORE_FAST | 1,601,855 | 16.2% |
| LOAD_FAST | 948,706 | 9.6% |
| JUMP_BACKWARD | 576,000 | 5.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 490,852 | 5.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 484,473 | 65.6% |
| GET_ITER | 253,982 | 34.4% |
| FOR_ITER | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 499,138 | 67.6% |
| LOAD_FAST | 228,637 | 31.0% |
| RETURN_CONST | 10,880 | 1.5% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,320 | 54.0% |
| GET_ITER | 11,740 | 38.8% |
| LOAD_FAST | 1,260 | 4.2% |
| SWAP | 860 | 2.8% |
| FOR_ITER | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,260 | 47.2% |
| LOAD_FAST | 10,460 | 34.6% |
| RETURN_CONST | 2,560 | 8.5% |
| STORE_FAST_LOAD_FAST | 2,000 | 6.6% |
| SWAP | 860 | 2.8% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 81,269 | 88.8% |
| LOAD_ATTR_MODULE | 10,200 | 11.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,984 | 81.9% |
| LOAD_FAST_CHECK | 16,565 | 18.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,250,348 | 88.4% |
| LOAD_FAST_LOAD_FAST | 2,158,227 | 9.0% |
| COPY | 575,842 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 23,686 | 0.1% |
| RETURN_VALUE | 14,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,502,517 | 22.9% |
| LOAD_FAST | 4,139,361 | 17.2% |
| TO_BOOL_BOOL | 1,817,702 | 7.6% |
| LOAD_ATTR | 1,790,358 | 7.4% |
| CONTAINS_OP | 1,705,482 | 7.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 409,036 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,738 | 39.8% |
| CALL | 148,644 | 36.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 97,834 | 23.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,502,517 | 87.1% |
| LOAD_FAST | 616,444 | 9.8% |
| LOAD_ATTR | 85,318 | 1.4% |
| LOAD_ATTR_SLOT | 83,760 | 1.3% |
| LOAD_CONST | 15,520 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,952,192 | 46.7% |
| CALL | 1,436,568 | 22.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,376,026 | 21.8% |
| LOAD_FAST_LOAD_FAST | 287,820 | 4.6% |
| LOAD_CONST | 235,033 | 3.7% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,257,918 | 73.9% |
| LOAD_FAST_LOAD_FAST | 1,129,521 | 11.5% |
| LOAD_ATTR_INSTANCE_VALUE | 814,781 | 8.3% |
| BINARY_SUBSCR | 575,920 | 5.9% |
| LOAD_GLOBAL_MODULE | 28,860 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,951,673 | 50.4% |
| LOAD_FAST | 3,264,409 | 33.2% |
| CALL_PY_WITH_DEFAULTS | 702,306 | 7.1% |
| LOAD_FAST_LOAD_FAST | 678,560 | 6.9% |
| LOAD_CONST | 126,231 | 1.3% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,521,776 | 99.9% |
| LOAD_ATTR | 2,820 | 0.1% |
| LOAD_FAST | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,239,894 | 63.5% |
| CALL_PY_WITH_DEFAULTS | 1,129,521 | 32.0% |
| STORE_DEREF | 55,040 | 1.6% |
| LOAD_CONST | 35,840 | 1.0% |
| LOAD_FAST | 28,800 | 0.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,170,121 | 70.5% |
| LOAD_FAST_LOAD_FAST | 490,292 | 29.5% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,129,561 | 68.0% |
| UNARY_INVERT | 490,372 | 29.5% |
| RETURN_VALUE | 14,040 | 0.8% |
| LOAD_CONST | 14,040 | 0.8% |
| LOAD_FAST_LOAD_FAST | 5,720 | 0.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 965,872 | 97.1% |
| RETURN_VALUE | 27,440 | 2.8% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.1% |
| LOAD_ATTR | 320 | 0.0% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 982,712 | 98.8% |
| TO_BOOL_BOOL | 12,160 | 1.2% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,360 | 98.6% |
| LOAD_ATTR_MODULE | 1,180 | 1.2% |
| RETURN_VALUE | 140 | 0.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 83,760 | 84.0% |
| CALL_BUILTIN_FAST | 14,140 | 14.2% |
| LOAD_FAST | 1,040 | 1.0% |
| LOAD_CONST | 600 | 0.6% |
| STORE_FAST | 140 | 0.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,531,355 | 41.7% |
| LOAD_FAST | 1,173,701 | 13.9% |
| STORE_FAST | 1,155,725 | 13.6% |
| LOAD_GLOBAL_BUILTIN | 968,754 | 11.4% |
| NOP | 699,149 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,909,307 | 46.1% |
| LOAD_DEREF | 1,713,474 | 20.2% |
| CALL_ISINSTANCE | 1,147,061 | 13.5% |
| LOAD_GLOBAL_BUILTIN | 968,754 | 11.4% |
| LOAD_GLOBAL_MODULE | 625,080 | 7.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,669,310 | 28.3% |
| RESUME_CHECK | 3,011,725 | 18.2% |
| NOP | 1,726,641 | 10.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,437,280 | 8.7% |
| POP_JUMP_IF_FALSE | 1,406,326 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 3,633,869 | 22.0% |
| LOAD_ATTR_MODULE | 3,521,776 | 21.3% |
| LOAD_FAST_LOAD_FAST | 2,553,159 | 15.5% |
| LOAD_FAST | 2,069,930 | 12.5% |
| COMPARE_OP_STR | 1,408,294 | 8.5% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,440 | 99.9% |
| LOAD_SUPER_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 89,520 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,623,754 | 100.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,143,881 | 70.4% |
| CALL_PY_EXACT_ARGS | 474,273 | 29.2% |
| LOAD_FAST | 5,760 | 0.4% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 12,154,800 | 34.2% |
| CALL_PY_EXACT_ARGS | 11,543,595 | 32.5% |
| FOR_ITER_GEN | 6,335,920 | 17.8% |
| COPY_FREE_VARS | 1,719,614 | 4.8% |
| CALL_PY_WITH_DEFAULTS | 1,228,045 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,452,305 | 54.8% |
| POP_TOP | 6,913,520 | 19.5% |
| LOAD_GLOBAL_BUILTIN | 3,531,355 | 9.9% |
| LOAD_GLOBAL_MODULE | 3,011,725 | 8.5% |
| NOP | 1,331,301 | 3.7% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,981,930 | 68.8% |
| LOAD_FAST_LOAD_FAST | 736,053 | 17.0% |
| SWAP | 575,842 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 17,040 | 0.4% |
| STORE_FAST_LOAD_FAST | 14,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,110,812 | 48.7% |
| LOAD_FAST | 940,581 | 21.7% |
| LOAD_GLOBAL_MODULE | 712,893 | 16.4% |
| LOAD_CONST | 302,858 | 7.0% |
| LOAD_FAST_LOAD_FAST | 129,480 | 3.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,760 | 85.5% |
| LOAD_FAST_LOAD_FAST | 14,140 | 14.4% |
| STORE_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,980 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,129,521 | 65.5% |
| LOAD_FAST | 548,127 | 31.8% |
| LOAD_ATTR_INSTANCE_VALUE | 34,680 | 2.0% |
| CALL | 10,200 | 0.6% |
| LOAD_CONST | 1,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,636,127 | 94.9% |
| RETURN_CONST | 32,520 | 1.9% |
| LOAD_GLOBAL_MODULE | 27,720 | 1.6% |
| LOAD_CONST | 27,480 | 1.6% |
| NOP | 140 | 0.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 64.8% |
| COPY | 286 | 30.9% |
| TO_BOOL | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 620 | 67.0% |
| POP_JUMP_IF_FALSE | 306 | 33.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,817,702 | 31.1% |
| CALL_ISINSTANCE | 1,147,341 | 19.6% |
| RETURN_VALUE | 850,627 | 14.6% |
| LOAD_FAST | 718,476 | 12.3% |
| CALL_BUILTIN_FAST | 604,774 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,796,478 | 65.0% |
| POP_JUMP_IF_TRUE | 1,798,526 | 30.8% |
| UNARY_NOT | 245,042 | 4.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,749,334 | 54.9% |
| BINARY_OP | 1,129,661 | 22.6% |
| LOAD_FAST | 1,129,521 | 22.5% |
| TO_BOOL | 240 | 0.0% |
| CALL_BUILTIN_O | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,008,896 | 100.0% |
| POP_JUMP_IF_TRUE | 140 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 485,773 | 91.8% |
| LOAD_ATTR_INSTANCE_VALUE | 42,900 | 8.1% |
| TO_BOOL | 200 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 528,733 | 100.0% |
| POP_JUMP_IF_TRUE | 160 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 191,364 | 79.6% |
| LOAD_FAST | 27,900 | 11.6% |
| COPY | 13,880 | 5.8% |
| WITH_EXCEPT_START | 5,680 | 2.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220,724 | 91.8% |
| POP_JUMP_IF_TRUE | 19,700 | 8.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,000 | 71.4% |
| LOAD_FAST | 620 | 22.1% |
| COPY | 160 | 5.7% |
| LOAD_GLOBAL_MODULE | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,200 | 78.6% |
| POP_JUMP_IF_FALSE | 600 | 21.4% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,087,880 | 93.0% |
| CALL_BUILTIN_FAST | 81,309 | 7.0% |
| CALL_METHOD_DESCRIPTOR_O | 280 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,088,220 | 93.0% |
| STORE_FAST | 81,349 | 7.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 581,600 | 27.6% |
| LOAD_FAST_CHECK | 575,920 | 27.4% |
| FOR_ITER_LIST | 490,852 | 23.3% |
| CALL_BUILTIN_FAST | 439,459 | 20.9% |
| CALL | 9,440 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,097,851 | 99.7% |
| LOAD_FAST | 7,000 | 0.3% |
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
|     deferred | 6,781,633 | 76.6% |
|          hit | 2,060,838 | 23.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 619 | 8.8% |
| Failure | 6,377 | 91.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,168 | 49.7% |
| or | 1,690 | 26.5% |
| remainder | 779 | 12.2% |
| add different types | 640 | 10.0% |
| add other | 100 | 1.6% |


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
|     deferred | 634,956 | 46.3% |
|          hit | 735,274 | 53.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 21.4% |
| Failure | 880 | 78.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 880 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,217,263 | 29.7% |
|          hit | 26,542,968 | 70.2% |
|         miss | 7,580 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,260 | 23.0% |
| Failure | 31,030 | 77.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 7,917 | 25.5% |
| cfunc noargs | 5,829 | 18.8% |
| class no vectorcall | 4,500 | 14.5% |
| meth descr varargs keywords | 3,103 | 10.0% |
| class mutable | 1,274 | 4.1% |
| other | 1,180 | 3.8% |
| bound method | 1,121 | 3.6% |
| metaclass | 1,112 | 3.6% |
| cfunc varargs | 1,100 | 3.5% |
| meth descr method fastcall keywords | 920 | 3.0% |
| cfunc varargs keywords | 914 | 2.9% |
| operator wrapper | 780 | 2.5% |
| cmethod | 640 | 2.1% |
| wrong number arguments | 320 | 1.0% |
| method wrapper | 280 | 0.9% |
| meth descr varargs | 40 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 569,080 | 10.0% |
|          hit | 5,141,542 | 90.0% |
|         miss | 6,751 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,615 | 53.6% |
| Failure | 1,396 | 46.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 814 | 58.3% |
| big int | 360 | 25.8% |
| different types | 222 | 15.9% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,302,940 | 7.1% |
|          hit | 16,975,931 | 92.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 26.7% |
| Failure | 1,700 | 73.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 520 | 30.6% |
| enumerate | 520 | 30.6% |
| itertools | 400 | 23.5% |
| callable | 260 | 15.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,327,324 | 18.1% |
|          hit | 46,648,851 | 81.8% |
|         miss | 311,694 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,635 | 52.5% |
| Failure | 20,494 | 47.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 4,616 | 22.5% |
| shadowed | 4,268 | 20.8% |
| not managed dict | 3,706 | 18.1% |
| non overriding descriptor | 2,468 | 12.0% |
| has managed dict | 1,120 | 5.5% |
| class attr descriptor | 1,040 | 5.1% |
| metaclass attribute | 960 | 4.7% |
| class method obj | 920 | 4.5% |
| non object slot | 560 | 2.7% |
| class attr simple | 476 | 2.3% |
| mutable class | 280 | 1.4% |
| overridden | 80 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 14,474 | 0.1% |
|        deopt | 100 | 0.0% |
|          hit | 24,977,681 | 99.9% |
|         miss | 6,214 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,592 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 1,713,474 | 100.0% |

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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 334,641 | 7.4% |
|          hit | 4,186,504 | 92.4% |
|         miss | 245,260 | 5.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,999 | 78.1% |
| Failure | 2,520 | 21.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| property | 1,180 | 46.8% |
| class attr simple | 560 | 22.2% |
| not in keys | 520 | 20.6% |
| no dict | 260 | 10.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 30,359 | 1.7% |
|          hit | 1,724,047 | 98.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 279 | 29.7% |
| Failure | 660 | 70.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 440 | 66.7% |
| other | 220 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,067,631 | 8.4% |
|          hit | 11,621,845 | 91.5% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,002 | 46.0% |
| Failure | 3,522 | 54.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| mapping | 1,082 | 30.7% |
| sequence | 740 | 21.0% |
| set | 740 | 21.0% |
| tuple | 740 | 21.0% |
| other | 220 | 6.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 3,274,480 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 312,041,378 | 56.6% |
| Not specialized | 57,829,742 | 10.5% |
| Specialized hits | 180,973,437 | 32.8% |
| Specialized misses | 577,782 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 11,217,263 | 34.7% |
| LOAD_ATTR | 10,327,324 | 32.0% |
| BINARY_OP | 6,781,633 | 21.0% |
| FOR_ITER | 1,302,940 | 4.0% |
| TO_BOOL | 1,067,631 | 3.3% |
| BINARY_SUBSCR | 634,956 | 2.0% |
| COMPARE_OP | 569,080 | 1.8% |
| STORE_ATTR | 334,641 | 1.0% |
| STORE_SUBSCR | 30,359 | 0.1% |
| LOAD_GLOBAL | 14,474 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 245,260 | 42.4% |
| LOAD_ATTR_INSTANCE_VALUE | 216,174 | 37.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,040 | 14.2% |
| LOAD_ATTR_PROPERTY | 12,380 | 2.1% |
| COMPARE_OP_INT | 6,731 | 1.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,400 | 1.1% |
| LOAD_GLOBAL_MODULE | 5,874 | 1.0% |
| LOAD_ATTR_MODULE | 1,100 | 0.2% |
| CALL_PY_EXACT_ARGS | 580 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 420 | 0.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 12,748,773 | 35.9% |
| Calls to Python functions inlined | 22,782,096 | 64.1% |
| Calls via PyEval_EvalFrame (total) | 12,748,773 | 35.9% |
| Calls via PyEval_EvalFrame (vector) | 12,163,653 | 34.2% |
| Calls via PyEval_EvalFrame (generator) | 585,120 | 1.6% |
| Calls via PyEval_EvalFrame (legacy) | 140 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 12,162,953 | 34.2% |
| Calls via PyEval_EvalFrame (build class) | 560 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 625,920 | 1.8% |
| Calls via PyEval_EvalFrame (function ex) | 535,340 | 1.5% |
| Calls via PyEval_EvalFrame (api) | 612,110 | 1.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 48,346 | 0.1% |
| Frames pushed | 15,202,557 | 42.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 18,723,774 | 41.3% |
| Frees to freelist | 18,736,411 |  |
| Allocations | 26,595,439 | 58.7% |
| Allocations to 512 bytes | 26,289,453 | 58.0% |
| Allocations to 4 kbytes | 132,849 | 0.3% |
| Allocations over 4 kbytes | 173,137 | 0.4% |
| Frees | 27,988,356 |  |
| New values | 1,036,646 |  |
| Interpreter increfs | 216,972,392 | 76.1% |
| Interpreter decrefs | 238,096,698 | 73.1% |
| Increfs | 68,036,845 | 23.9% |
| Decrefs | 87,579,724 | 26.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 40 | 0.0% |
| Method cache hits | 11,938,275 |  |
| Method cache misses | 50,709 |  |
| Method cache collisions | 69,891 |  |
| Method cache dunder hits | 12,237,834 |  |
| Method cache dunder misses | 22,959 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 720 | 287,852 |
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
| Number of data files | 40 |


</details>

---
Stats gathered on: 2024-09-10
