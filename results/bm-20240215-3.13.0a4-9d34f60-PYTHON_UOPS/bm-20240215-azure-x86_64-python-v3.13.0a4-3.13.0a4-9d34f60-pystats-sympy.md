
# Pystats results

- benchmark: sympy
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 870,633,645 | 17.1% | 17.1% |  |
| STORE_FAST | 304,033,525 | 6.0% | 23.1% |  |
| RESUME_CHECK | 249,832,980 | 4.9% | 28.0% |  |
| POP_JUMP_IF_FALSE | 245,748,612 | 4.8% | 32.8% |  |
| LOAD_GLOBAL_BUILTIN | 218,042,918 | 4.3% | 37.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 206,530,345 | 4.1% | 41.1% |  |
| LOAD_CONST | 187,051,227 | 3.7% | 44.8% |  |
| RETURN_VALUE | 177,176,997 | 3.5% | 48.3% |  |
| TO_BOOL_BOOL | 161,932,219 | 3.2% | 51.4% | 0.1% |
| INTERPRETER_EXIT | 127,320,622 | 2.5% | 53.9% |  |
| LOAD_GLOBAL_MODULE | 111,276,767 | 2.2% | 56.1% | 0.0% |
| LOAD_ATTR_SLOT | 95,719,635 | 1.9% | 58.0% | 38.1% |
| LOAD_ATTR | 92,051,688 | 1.8% | 59.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 86,909,665 | 1.7% | 61.5% | 10.5% |
| ENTER_EXECUTOR | 81,648,229 | 1.6% | 63.1% |  |
| POP_JUMP_IF_TRUE | 67,816,585 | 1.3% | 64.5% |  |
| POP_TOP | 60,103,833 | 1.2% | 65.6% |  |
| CALL_PY_EXACT_ARGS | 60,014,132 | 1.2% | 66.8% | 13.0% |
| GET_ITER | 57,480,081 | 1.1% | 67.9% |  |
| STORE_FAST_STORE_FAST | 57,091,032 | 1.1% | 69.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 56,748,092 | 1.1% | 70.2% | 27.8% |
| CALL_ISINSTANCE | 56,095,068 | 1.1% | 71.3% |  |
| RETURN_CONST | 54,718,766 | 1.1% | 72.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 54,202,868 | 1.1% | 73.4% |  |
| PUSH_NULL | 51,732,594 | 1.0% | 74.4% |  |
| LOAD_DEREF | 50,510,126 | 1.0% | 75.4% |  |
| BUILD_TUPLE | 49,098,618 | 1.0% | 76.4% |  |
| COMPARE_OP_INT | 48,620,411 | 1.0% | 77.3% | 1.2% |
| IS_OP | 45,396,411 | 0.9% | 78.2% |  |
| SWAP | 43,164,832 | 0.8% | 79.1% |  |
| CALL_BUILTIN_FAST | 42,689,834 | 0.8% | 79.9% |  |
| FOR_ITER | 42,448,598 | 0.8% | 80.8% |  |
| CALL_BUILTIN_O | 37,667,190 | 0.7% | 81.5% | 7.1% |
| COMPARE_OP | 37,652,292 | 0.7% | 82.2% |  |
| BINARY_OP | 34,094,182 | 0.7% | 82.9% |  |
| NOP | 31,986,082 | 0.6% | 83.5% |  |
| COPY_FREE_VARS | 31,645,848 | 0.6% | 84.1% |  |
| BINARY_SUBSCR_LIST_INT | 29,001,645 | 0.6% | 84.7% | 0.0% |
| CALL_LEN | 28,074,109 | 0.6% | 85.3% |  |
| CALL_FUNCTION_EX | 28,012,697 | 0.5% | 85.8% |  |
| LOAD_ATTR_PROPERTY | 27,997,014 | 0.5% | 86.4% | 14.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 27,647,566 | 0.5% | 86.9% | 23.4% |
| BUILD_MAP | 27,159,935 | 0.5% | 87.4% |  |
| CALL | 25,342,554 | 0.5% | 87.9% |  |
| CALL_LIST_APPEND | 24,015,614 | 0.5% | 88.4% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,512,344 | 0.5% | 88.9% | 0.2% |
| YIELD_VALUE | 22,976,304 | 0.5% | 89.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 22,786,966 | 0.4% | 89.8% | 62.9% |
| POP_JUMP_IF_NOT_NONE | 22,607,562 | 0.4% | 90.2% |  |
| FOR_ITER_LIST | 22,440,151 | 0.4% | 90.7% | 0.7% |
| BINARY_SUBSCR | 21,730,813 | 0.4% | 91.1% |  |
| FOR_ITER_TUPLE | 20,778,319 | 0.4% | 91.5% | 1.0% |
| BUILD_LIST | 20,484,929 | 0.4% | 91.9% |  |
| STORE_SUBSCR_LIST_INT | 20,081,447 | 0.4% | 92.3% |  |
| JUMP_BACKWARD | 19,227,245 | 0.4% | 92.7% |  |
| TO_BOOL_INT | 18,503,939 | 0.4% | 93.0% | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 17,790,220 | 0.3% | 93.4% | 0.7% |
| DICT_MERGE | 16,636,314 | 0.3% | 93.7% |  |
| LOAD_FAST_AND_CLEAR | 14,956,980 | 0.3% | 94.0% |  |
| CALL_TYPE_1 | 14,797,531 | 0.3% | 94.3% |  |
| RETURN_GENERATOR | 14,331,245 | 0.3% | 94.6% |  |
| COMPARE_OP_STR | 14,034,024 | 0.3% | 94.8% |  |
| TO_BOOL | 12,906,021 | 0.3% | 95.1% |  |
| BINARY_OP_ADD_INT | 12,599,267 | 0.2% | 95.3% |  |
| MAKE_FUNCTION | 12,424,856 | 0.2% | 95.6% |  |
| EXTENDED_ARG | 11,898,512 | 0.2% | 95.8% |  |
| POP_JUMP_IF_NONE | 11,687,228 | 0.2% | 96.1% |  |
| FOR_ITER_RANGE | 11,076,824 | 0.2% | 96.3% |  |
| CONTAINS_OP | 10,861,875 | 0.2% | 96.5% |  |
| CALL_KW | 10,673,148 | 0.2% | 96.7% |  |
| SET_FUNCTION_ATTRIBUTE | 10,412,294 | 0.2% | 96.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 9,172,184 | 0.2% | 97.1% | 0.0% |
| STORE_ATTR_SLOT | 9,060,323 | 0.2% | 97.3% | 24.5% |
| BINARY_SUBSCR_TUPLE_INT | 8,985,421 | 0.2% | 97.4% | 0.1% |
| IMPORT_FROM | 8,955,167 | 0.2% | 97.6% |  |
| CALL_BUILTIN_CLASS | 8,570,164 | 0.2% | 97.8% |  |
| IMPORT_NAME | 7,759,905 | 0.2% | 97.9% |  |
| STORE_DEREF | 7,737,117 | 0.2% | 98.1% |  |
| MAKE_CELL | 6,049,256 | 0.1% | 98.2% |  |
| CALL_TUPLE_1 | 5,851,387 | 0.1% | 98.3% | 0.0% |
| JUMP_FORWARD | 5,839,625 | 0.1% | 98.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,735,785 | 0.1% | 98.5% | 0.1% |
| UNARY_NOT | 5,273,882 | 0.1% | 98.6% |  |
| MAP_ADD | 4,719,749 | 0.1% | 98.7% |  |
| COPY | 4,618,305 | 0.1% | 98.8% |  |
| CALL_PY_WITH_DEFAULTS | 4,598,144 | 0.1% | 98.9% | 0.7% |
| CALL_METHOD_DESCRIPTOR_O | 4,584,381 | 0.1% | 99.0% | 0.2% |
| STORE_ATTR_INSTANCE_VALUE | 3,358,801 | 0.1% | 99.1% | 0.0% |
| BINARY_SUBSCR_DICT | 3,147,414 | 0.1% | 99.1% |  |
| BINARY_OP_MULTIPLY_INT | 2,757,977 | 0.1% | 99.2% | 0.0% |
| TO_BOOL_NONE | 2,647,218 | 0.1% | 99.2% | 8.6% |
| LIST_APPEND | 2,556,899 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_INT | 2,475,931 | 0.0% | 99.3% |  |
| TO_BOOL_LIST | 2,294,195 | 0.0% | 99.4% | 0.5% |
| STORE_SUBSCR_DICT | 2,276,710 | 0.0% | 99.4% |  |
| LOAD_SUPER_ATTR_METHOD | 1,808,150 | 0.0% | 99.5% |  |
| STORE_FAST_LOAD_FAST | 1,756,926 | 0.0% | 99.5% |  |
| STORE_SUBSCR | 1,653,246 | 0.0% | 99.5% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,650,882 | 0.0% | 99.6% | 20.6% |
| UNPACK_SEQUENCE_TUPLE | 1,592,127 | 0.0% | 99.6% |  |
| LOAD_FAST_CHECK | 1,572,574 | 0.0% | 99.6% |  |
| LIST_EXTEND | 1,349,066 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 1,349,026 | 0.0% | 99.7% |  |
| DELETE_FAST | 1,302,220 | 0.0% | 99.7% |  |
| LOAD_ATTR_MODULE | 1,271,720 | 0.0% | 99.7% | 0.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,913 | 0.0% | 99.8% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,121,104 | 0.0% | 99.8% |  |
| SEND_GEN | 1,029,804 | 0.0% | 99.8% | 3.0% |
| CHECK_EXC_MATCH | 906,313 | 0.0% | 99.8% |  |
| POP_EXCEPT | 906,313 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 906,313 | 0.0% | 99.8% |  |
| STORE_ATTR | 591,379 | 0.0% | 99.9% |  |
| BINARY_SLICE | 563,956 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 551,660 | 0.0% | 99.9% |  |
| COMPARE_OP_FLOAT | 543,602 | 0.0% | 99.9% | 0.3% |
| GET_YIELD_FROM_ITER | 540,384 | 0.0% | 99.9% |  |
| UNARY_NEGATIVE | 533,104 | 0.0% | 99.9% |  |
| END_SEND | 519,360 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 503,100 | 0.0% | 99.9% |  |
| SEND | 442,840 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 282,600 | 0.0% | 99.9% |  |
| CONVERT_VALUE | 282,560 | 0.0% | 100.0% |  |
| CALL_STR_1 | 233,240 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 227,777 | 0.0% | 100.0% | 36.5% |
| FOR_ITER_GEN | 191,294 | 0.0% | 100.0% | 0.2% |
| LOAD_ATTR_CLASS | 187,600 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 182,027 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_LIST | 179,206 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 159,246 | 0.0% | 100.0% | 0.0% |
| BUILD_STRING | 140,940 | 0.0% | 100.0% |  |
| STORE_NAME | 131,280 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 129,373 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 119,074 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 95,920 | 0.0% | 100.0% | 0.2% |
| EXIT_INIT_CHECK | 95,600 | 0.0% | 100.0% |  |
| LOAD_NAME | 71,540 | 0.0% | 100.0% |  |
| BUILD_SET | 50,370 | 0.0% | 100.0% |  |
| RESUME | 47,596 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 39,769 | 0.0% | 100.0% |  |
| BEFORE_WITH | 37,420 | 0.0% | 100.0% |  |
| END_FOR | 22,529 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 19,260 | 0.0% | 100.0% |  |
| SET_ADD | 18,080 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 4,760 | 0.0% | 100.0% |  |
| BUILD_SLICE | 4,014 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 3,100 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 2,660 | 0.0% | 100.0% |  |
| RERAISE | 2,080 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,040 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,207 | 0.0% | 100.0% |  |
| STORE_SLICE | 940 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 480 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 300 | 0.0% | 100.0% | 20.0% |
| DELETE_NAME | 120 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 60 | 0.0% | 100.0% |  |
| DICT_UPDATE | 20 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST | 168,825,574 | 3.3% | 3.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 149,685,315 | 2.9% | 6.3% |
| RESUME_CHECK LOAD_FAST | 115,532,021 | 2.3% | 8.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 107,873,166 | 2.1% | 10.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 107,694,311 | 2.1% | 12.8% |
| CACHE RESUME_CHECK | 99,105,613 | 1.9% | 14.7% |
| LOAD_FAST LOAD_ATTR_SLOT | 94,211,645 | 1.8% | 16.5% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 74,196,339 | 1.5% | 18.0% |
| RETURN_VALUE INTERPRETER_EXIT | 72,899,233 | 1.4% | 19.4% |
| LOAD_FAST LOAD_CONST | 68,842,430 | 1.4% | 20.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 57,223,068 | 1.1% | 21.9% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 53,249,516 | 1.0% | 23.0% |
| LOAD_FAST RETURN_VALUE | 52,928,357 | 1.0% | 24.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 52,519,800 | 1.0% | 25.0% |
| LOAD_FAST LOAD_ATTR | 50,964,793 | 1.0% | 26.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 50,470,565 | 1.0% | 27.0% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 50,403,987 | 1.0% | 28.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 47,874,006 | 0.9% | 28.9% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 47,267,628 | 0.9% | 29.9% |
| PUSH_NULL LOAD_FAST | 44,199,920 | 0.9% | 30.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 43,028,954 | 0.8% | 31.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT TO_BOOL_BOOL | 42,258,136 | 0.8% | 32.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 41,199,854 | 0.8% | 33.2% |
| LOAD_CONST LOAD_CONST | 40,321,075 | 0.8% | 34.0% |
| RETURN_VALUE STORE_FAST | 38,444,544 | 0.8% | 34.8% |
| LOAD_ATTR STORE_FAST | 34,991,961 | 0.7% | 35.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 33,550,990 | 0.7% | 36.1% |
| LOAD_ATTR_SLOT RETURN_VALUE | 33,432,101 | 0.7% | 36.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 33,192,369 | 0.7% | 37.4% |
| POP_JUMP_IF_TRUE LOAD_FAST | 32,715,620 | 0.6% | 38.1% |
| RETURN_CONST INTERPRETER_EXIT | 32,283,254 | 0.6% | 38.7% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 31,738,869 | 0.6% | 39.3% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 30,200,647 | 0.6% | 39.9% |
| IS_OP POP_JUMP_IF_FALSE | 30,004,936 | 0.6% | 40.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 29,853,967 | 0.6% | 41.1% |
| POP_JUMP_IF_FALSE RETURN_CONST | 28,518,253 | 0.6% | 41.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 28,383,426 | 0.6% | 42.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 27,853,342 | 0.5% | 42.8% |
| LOAD_FAST CALL_LEN | 27,045,693 | 0.5% | 43.3% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 26,359,654 | 0.5% | 43.8% |
| LOAD_FAST PUSH_NULL | 26,244,422 | 0.5% | 44.3% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 25,277,881 | 0.5% | 44.8% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 25,063,131 | 0.5% | 45.3% |
| BINARY_OP STORE_FAST | 24,134,621 | 0.5% | 45.8% |
| LOAD_CONST CALL_BUILTIN_FAST | 24,050,815 | 0.5% | 46.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 22,641,509 | 0.4% | 46.7% |
| LOAD_ATTR_SLOT STORE_FAST | 22,510,022 | 0.4% | 47.1% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 22,294,854 | 0.4% | 47.6% |
| YIELD_VALUE INTERPRETER_EXIT | 22,130,395 | 0.4% | 48.0% |
| POP_TOP ENTER_EXECUTOR | 21,997,819 | 0.4% | 48.4% |
| COPY_FREE_VARS RESUME_CHECK | 21,677,776 | 0.4% | 48.9% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 21,652,526 | 0.4% | 49.3% |
| LOAD_FAST TO_BOOL_BOOL | 21,599,188 | 0.4% | 49.7% |
| RESUME_CHECK NOP | 21,363,331 | 0.4% | 50.1% |
| LOAD_FAST GET_ITER | 21,271,275 | 0.4% | 50.5% |
| BUILD_TUPLE RETURN_VALUE | 21,221,040 | 0.4% | 51.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 21,127,713 | 0.4% | 51.4% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 21,085,793 | 0.4% | 51.8% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 21,015,808 | 0.4% | 52.2% |
| LOAD_CONST COMPARE_OP_INT | 20,725,796 | 0.4% | 52.6% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 20,220,508 | 0.4% | 53.0% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 19,740,560 | 0.4% | 53.4% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 19,465,497 | 0.4% | 53.8% |
| COMPARE_OP POP_JUMP_IF_FALSE | 19,268,102 | 0.4% | 54.2% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 18,992,763 | 0.4% | 54.5% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 18,842,414 | 0.4% | 54.9% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 18,812,537 | 0.4% | 55.3% |
| GET_ITER FOR_ITER | 18,761,951 | 0.4% | 55.6% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 18,408,334 | 0.4% | 56.0% |
| LOAD_FAST TO_BOOL_INT | 17,626,924 | 0.3% | 56.3% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 17,392,566 | 0.3% | 56.7% |
| LOAD_FAST BUILD_TUPLE | 16,952,128 | 0.3% | 57.0% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 16,712,752 | 0.3% | 57.3% |
| DICT_MERGE CALL_FUNCTION_EX | 16,636,314 | 0.3% | 57.7% |
| BUILD_MAP LOAD_FAST | 16,611,084 | 0.3% | 58.0% |
| LOAD_FAST DICT_MERGE | 16,571,379 | 0.3% | 58.3% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_BUILTIN | 16,351,111 | 0.3% | 58.6% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 16,148,037 | 0.3% | 59.0% |
| LOAD_ATTR LOAD_FAST | 16,037,861 | 0.3% | 59.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 16,022,336 | 0.3% | 59.6% |
| LOAD_FAST CALL_BUILTIN_O | 15,700,959 | 0.3% | 59.9% |
| RESUME_CHECK LOAD_CONST | 15,611,361 | 0.3% | 60.2% |
| LOAD_FAST CALL_LIST_APPEND | 15,553,304 | 0.3% | 60.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 15,470,237 | 0.3% | 60.8% |
| RETURN_VALUE RETURN_VALUE | 15,184,398 | 0.3% | 61.1% |
| RESUME_CHECK POP_TOP | 15,015,113 | 0.3% | 61.4% |
| LOAD_ATTR IS_OP | 14,931,943 | 0.3% | 61.7% |
| LOAD_FAST CALL_TYPE_1 | 14,728,635 | 0.3% | 62.0% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 14,727,970 | 0.3% | 62.3% |
| POP_TOP RESUME_CHECK | 14,325,685 | 0.3% | 62.6% |
| LOAD_CONST STORE_FAST | 14,264,529 | 0.3% | 62.8% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 13,990,776 | 0.3% | 63.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 13,894,947 | 0.3% | 63.4% |
| CACHE POP_TOP | 13,882,328 | 0.3% | 63.7% |
| CALL_BUILTIN_O STORE_FAST | 13,581,659 | 0.3% | 63.9% |
| LOAD_FAST CALL_BOUND_METHOD_EXACT_ARGS | 13,333,451 | 0.3% | 64.2% |
| GET_ITER CALL_PY_EXACT_ARGS | 13,002,361 | 0.3% | 64.4% |
| CACHE COPY_FREE_VARS | 13,001,378 | 0.3% | 64.7% |
| CALL_METHOD_DESCRIPTOR_FAST LOAD_FAST | 12,757,880 | 0.3% | 65.0% |
| LOAD_FAST IS_OP | 12,728,260 | 0.2% | 65.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 530,596 | 94.1% |
| LOAD_FAST | 26,720 | 4.7% |
| BINARY_OP_ADD_INT | 6,320 | 1.1% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 319,398 | 56.6% |
| RETURN_VALUE | 93,840 | 16.6% |
| GET_ITER | 54,720 | 9.7% |
| BINARY_OP | 39,120 | 6.9% |
| STORE_FAST | 18,960 | 3.4% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 940 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 580 | 61.7% |
| JUMP_BACKWARD | 360 | 38.3% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,105,613 | 77.7% |
| POP_TOP | 13,882,328 | 10.9% |
| COPY_FREE_VARS | 13,001,378 | 10.2% |
| MAKE_CELL | 1,509,098 | 1.2% |
| RESUME | 18,055 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 17,560 | 46.9% |
| RETURN_VALUE | 10,660 | 28.5% |
| CALL | 7,360 | 19.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,840 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 35,580 | 95.1% |
| STORE_FAST | 1,840 | 4.9% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,519,771 | 57.6% |
| LOAD_DEREF | 6,403,860 | 29.5% |
| BUILD_TUPLE | 1,623,934 | 7.5% |
| LOAD_FAST | 780,276 | 3.6% |
| RETURN_VALUE | 152,434 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 6,179,567 | 28.4% |
| RETURN_VALUE | 6,066,007 | 27.9% |
| LOAD_FAST | 6,033,661 | 27.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 907,066 | 4.2% |
| GET_ITER | 716,908 | 3.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 667,471 | 73.6% |
| BUILD_TUPLE | 157,208 | 17.3% |
| LOAD_GLOBAL_MODULE | 79,294 | 8.7% |
| LOAD_FAST | 1,600 | 0.2% |
| LOAD_GLOBAL | 740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 906,153 | 100.0% |
| EXTENDED_ARG | 160 | 0.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,900 | 61.3% |
| LOAD_FAST_LOAD_FAST | 1,200 | 38.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,840 | 59.4% |
| JUMP_BACKWARD | 920 | 29.7% |
| ENTER_EXECUTOR | 280 | 9.0% |
| LOAD_FAST | 60 | 1.9% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 335,800 | 64.7% |
| SEND | 168,540 | 32.5% |
| SEND_GEN | 15,020 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 519,360 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 95,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 95,600 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 282,560 | 100.0% |
| LOAD_FAST | 20 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 140,760 | 49.8% |
| LOAD_CONST | 108,280 | 38.3% |
| LOAD_FAST | 33,560 | 11.9% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,271,275 | 37.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 12,589,362 | 21.9% |
| CALL | 10,953,409 | 19.1% |
| RETURN_VALUE | 4,116,490 | 7.2% |
| CALL_BUILTIN_O | 2,591,106 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 18,761,951 | 32.6% |
| CALL_PY_EXACT_ARGS | 13,002,361 | 22.6% |
| FOR_ITER_TUPLE | 9,980,431 | 17.4% |
| LOAD_FAST_AND_CLEAR | 8,282,571 | 14.4% |
| FOR_ITER_LIST | 4,308,144 | 7.5% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 346,984 | 64.2% |
| BINARY_SUBSCR | 185,800 | 34.4% |
| RETURN_VALUE | 7,520 | 1.4% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540,384 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 72,899,233 | 57.3% |
| RETURN_CONST | 32,283,254 | 25.4% |
| YIELD_VALUE | 22,130,395 | 17.4% |
| RETURN_GENERATOR | 7,740 | 0.0% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 2,220 | 83.5% |
| POP_TOP | 420 | 15.8% |
| STORE_GLOBAL | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,660 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,424,856 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 10,410,754 | 83.8% |
| LOAD_GLOBAL_BUILTIN | 789,474 | 6.4% |
| STORE_FAST | 669,669 | 5.4% |
| LOAD_FAST | 459,179 | 3.7% |
| STORE_NAME | 33,580 | 0.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,363,331 | 66.8% |
| POP_JUMP_IF_TRUE | 4,183,848 | 13.1% |
| STORE_FAST | 1,973,462 | 6.2% |
| POP_JUMP_IF_FALSE | 1,912,924 | 6.0% |
| POP_TOP | 1,392,012 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,284,569 | 38.4% |
| LOAD_DEREF | 10,424,045 | 32.6% |
| LOAD_GLOBAL_MODULE | 6,407,295 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 1,206,656 | 3.8% |
| LOAD_FAST_LOAD_FAST | 899,510 | 2.8% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 414,613 | 45.7% |
| POP_TOP | 358,300 | 39.5% |
| STORE_FAST | 130,960 | 14.4% |
| COPY | 1,920 | 0.2% |
| STORE_SUBSCR_DICT | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 414,613 | 45.7% |
| ENTER_EXECUTOR | 165,696 | 18.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 159,130 | 17.6% |
| LOAD_FAST | 83,020 | 9.2% |
| RETURN_CONST | 45,040 | 5.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 15,015,113 | 25.0% |
| CACHE | 13,882,328 | 23.1% |
| RETURN_CONST | 7,934,355 | 13.2% |
| STORE_FAST | 5,839,811 | 9.7% |
| SWAP | 5,747,107 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 21,997,819 | 36.6% |
| RESUME_CHECK | 14,325,685 | 23.8% |
| LOAD_FAST | 7,271,664 | 12.1% |
| RETURN_VALUE | 5,270,907 | 8.8% |
| LOAD_CONST | 2,640,958 | 4.4% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 374,545 | 41.3% |
| BINARY_SUBSCR_DICT | 169,932 | 18.7% |
| RAISE_VARARGS | 115,254 | 12.7% |
| LOAD_ATTR | 95,500 | 10.5% |
| ENTER_EXECUTOR | 82,748 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 788,099 | 87.0% |
| LOAD_GLOBAL_MODULE | 114,774 | 12.7% |
| LOAD_GLOBAL | 1,840 | 0.2% |
| LOAD_FAST | 1,600 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,244,422 | 50.7% |
| LOAD_DEREF | 11,815,135 | 22.8% |
| LOAD_ATTR | 8,322,738 | 16.1% |
| CALL_BUILTIN_FAST | 2,128,620 | 4.1% |
| LOAD_SUPER_ATTR_ATTR | 1,181,913 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,199,920 | 85.4% |
| LOAD_FAST_LOAD_FAST | 5,593,726 | 10.8% |
| LOAD_CONST | 1,723,680 | 3.3% |
| LOAD_DEREF | 127,454 | 0.2% |
| CALL | 35,600 | 0.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 9,887,382 | 69.0% |
| CALL_PY_EXACT_ARGS | 4,261,123 | 29.7% |
| CALL_PY_WITH_DEFAULTS | 163,640 | 1.1% |
| CALL_KW | 8,000 | 0.1% |
| CACHE | 7,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 10,191,909 | 71.1% |
| STORE_FAST | 2,660,339 | 18.6% |
| LOAD_FAST | 791,980 | 5.5% |
| GET_YIELD_FROM_ITER | 346,984 | 2.4% |
| CALL_BUILTIN_CLASS | 160,600 | 1.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,928,357 | 29.9% |
| LOAD_ATTR_SLOT | 33,432,101 | 18.9% |
| BUILD_TUPLE | 21,221,040 | 12.0% |
| RETURN_VALUE | 15,184,398 | 8.6% |
| CALL_BUILTIN_O | 11,432,780 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 72,899,233 | 41.1% |
| STORE_FAST | 38,444,544 | 21.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 19,465,497 | 11.0% |
| RETURN_VALUE | 15,184,398 | 8.6% |
| LOAD_FAST | 5,438,025 | 3.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,564,665 | 94.6% |
| BINARY_SUBSCR | 56,960 | 3.4% |
| LOAD_FAST_LOAD_FAST | 18,960 | 1.1% |
| SWAP | 5,960 | 0.4% |
| STORE_SUBSCR | 3,287 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,551,785 | 93.9% |
| ENTER_EXECUTOR | 67,100 | 4.1% |
| JUMP_BACKWARD | 12,840 | 0.8% |
| JUMP_FORWARD | 9,840 | 0.6% |
| STORE_SUBSCR | 3,287 | 0.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 10,287,220 | 79.7% |
| LOAD_FAST | 2,207,783 | 17.1% |
| LOAD_GLOBAL_MODULE | 119,053 | 0.9% |
| LOAD_ATTR | 117,985 | 0.9% |
| RETURN_VALUE | 27,297 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,233,830 | 94.8% |
| POP_JUMP_IF_TRUE | 510,136 | 4.0% |
| UNARY_NOT | 84,232 | 0.7% |
| TO_BOOL_BOOL | 41,203 | 0.3% |
| TO_BOOL | 21,377 | 0.2% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 117,478 | 22.0% |
| LOAD_FAST | 109,419 | 20.5% |
| LOAD_ATTR | 107,040 | 20.1% |
| RETURN_VALUE | 106,160 | 19.9% |
| LOAD_FAST_LOAD_FAST | 50,684 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 131,975 | 24.8% |
| LOAD_GLOBAL_MODULE | 106,844 | 20.0% |
| IS_OP | 106,160 | 19.9% |
| STORE_FAST | 58,138 | 10.9% |
| CALL_LIST_APPEND | 39,980 | 7.5% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 3,442,630 | 65.3% |
| TO_BOOL_BOOL | 1,084,985 | 20.6% |
| TO_BOOL_LIST | 661,866 | 12.5% |
| TO_BOOL | 84,232 | 1.6% |
| TO_BOOL_INT | 169 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,529,411 | 66.9% |
| STORE_FAST | 882,736 | 16.7% |
| BUILD_MAP | 734,720 | 13.9% |
| COPY | 87,001 | 1.6% |
| LOAD_CONST | 34,354 | 0.7% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,753,011 | 34.5% |
| COMPARE_OP_INT | 6,277,300 | 18.4% |
| COMPARE_OP | 6,162,400 | 18.1% |
| CALL_TUPLE_1 | 4,707,269 | 13.8% |
| LOAD_FAST | 1,516,623 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,134,621 | 70.8% |
| RETURN_VALUE | 5,648,702 | 16.6% |
| CALL_BUILTIN_O | 1,095,131 | 3.2% |
| LOAD_FAST | 857,898 | 2.5% |
| TO_BOOL_INT | 722,567 | 2.1% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 129,373 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 126,593 | 97.9% |
| RETURN_VALUE | 1,840 | 1.4% |
| LOAD_CONST | 500 | 0.4% |
| LOAD_FAST | 400 | 0.3% |
| DICT_UPDATE | 20 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 4,083,167 | 19.9% |
| STORE_FAST | 3,817,118 | 18.6% |
| SWAP | 3,548,482 | 17.3% |
| LOAD_FAST | 2,131,199 | 10.4% |
| BINARY_SUBSCR_TUPLE_INT | 1,557,600 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,533,422 | 56.3% |
| SWAP | 3,548,482 | 17.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,294,386 | 11.2% |
| LOAD_FAST | 1,374,406 | 6.7% |
| BUILD_LIST | 748,353 | 3.7% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,163,864 | 44.8% |
| SWAP | 4,716,089 | 17.4% |
| BUILD_TUPLE | 4,366,357 | 16.1% |
| LOAD_CONST | 1,656,760 | 6.1% |
| RESUME_CHECK | 1,285,960 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,611,084 | 61.2% |
| SWAP | 4,716,089 | 17.4% |
| STORE_FAST | 3,331,413 | 12.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,561,360 | 5.7% |
| CALL_FUNCTION_EX | 734,880 | 2.7% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,290 | 64.1% |
| SWAP | 18,000 | 35.7% |
| BINARY_OP | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 32,290 | 64.1% |
| SWAP | 18,000 | 35.7% |
| STORE_FAST | 80 | 0.2% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,014 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_GETITEM | 3,840 | 95.7% |
| BINARY_SUBSCR | 174 | 4.3% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 140,760 | 99.9% |
| LOAD_CONST | 180 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 106,160 | 75.3% |
| LOAD_CONST | 16,000 | 11.4% |
| LOAD_FAST | 16,000 | 11.4% |
| LIST_APPEND | 2,460 | 1.7% |
| CALL | 300 | 0.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,992,763 | 38.7% |
| LOAD_FAST | 16,952,128 | 34.5% |
| LOAD_ATTR_SLOT | 5,042,204 | 10.3% |
| LOAD_ATTR | 3,033,711 | 6.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,484,120 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 21,221,040 | 43.2% |
| LOAD_CONST | 10,429,940 | 21.2% |
| LOAD_GLOBAL_BUILTIN | 4,707,069 | 9.6% |
| BUILD_MAP | 4,366,357 | 8.9% |
| CALL_LIST_APPEND | 3,214,240 | 6.5% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,372,499 | 37.0% |
| LOAD_FAST | 7,124,909 | 28.1% |
| BINARY_OP_MULTIPLY_INT | 2,291,867 | 9.0% |
| ENTER_EXECUTOR | 2,272,420 | 9.0% |
| LOAD_GLOBAL_BUILTIN | 1,572,928 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,953,409 | 43.2% |
| STORE_FAST | 5,658,146 | 22.3% |
| RETURN_VALUE | 4,389,005 | 17.3% |
| RESUME_CHECK | 1,058,260 | 4.2% |
| CALL_LIST_APPEND | 693,130 | 2.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 16,636,314 | 59.4% |
| ENTER_EXECUTOR | 7,551,051 | 27.0% |
| LOAD_FAST | 1,403,557 | 5.0% |
| CALL_INTRINSIC_1 | 1,256,706 | 4.5% |
| BUILD_MAP | 734,880 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,600,776 | 45.0% |
| RESUME_CHECK | 11,673,437 | 41.7% |
| LOAD_FAST_LOAD_FAST | 1,561,000 | 5.6% |
| BUILD_TUPLE | 638,818 | 2.3% |
| SWAP | 480,160 | 1.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 1,347,806 | 99.9% |
| IMPORT_NAME | 1,060 | 0.1% |
| LIST_APPEND | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,256,706 | 93.2% |
| BUILD_MAP | 91,260 | 6.8% |
| POP_TOP | 1,060 | 0.1% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,508,774 | 98.5% |
| ENTER_EXECUTOR | 164,374 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,493,168 | 88.9% |
| POP_TOP | 698,040 | 6.5% |
| COPY_FREE_VARS | 261,140 | 2.4% |
| RETURN_VALUE | 84,818 | 0.8% |
| STORE_FAST | 35,740 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 21,085,793 | 56.0% |
| LOAD_FAST | 7,421,639 | 19.7% |
| CALL_TYPE_1 | 5,882,438 | 15.6% |
| LOAD_GLOBAL_MODULE | 1,180,684 | 3.1% |
| LOAD_CONST | 949,786 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 19,268,102 | 51.2% |
| BINARY_OP | 6,162,400 | 16.4% |
| LOAD_FAST_LOAD_FAST | 6,162,320 | 16.4% |
| UNARY_NOT | 3,442,630 | 9.1% |
| POP_JUMP_IF_TRUE | 2,275,294 | 6.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,027,828 | 37.1% |
| LOAD_ATTR | 3,188,626 | 29.4% |
| LOAD_GLOBAL_MODULE | 1,646,086 | 15.2% |
| LOAD_DEREF | 1,478,140 | 13.6% |
| LOAD_CONST | 175,001 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,874,277 | 63.3% |
| POP_JUMP_IF_TRUE | 3,977,438 | 36.6% |
| STORE_FAST | 4,560 | 0.0% |
| EXTENDED_ARG | 4,480 | 0.0% |
| RETURN_VALUE | 960 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 170,080 | 60.2% |
| LOAD_FAST | 110,540 | 39.1% |
| STORE_FAST_LOAD_FAST | 1,560 | 0.6% |
| LOAD_GLOBAL_MODULE | 300 | 0.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 282,560 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,237,534 | 26.8% |
| COPY | 1,074,000 | 23.3% |
| LOAD_FAST_LOAD_FAST | 872,880 | 18.9% |
| CALL_ISINSTANCE | 525,020 | 11.4% |
| LOAD_CONST | 236,753 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,330,781 | 28.8% |
| COPY | 1,074,000 | 23.3% |
| BINARY_SUBSCR_LIST_INT | 1,067,720 | 23.1% |
| LOAD_ATTR_INSTANCE_VALUE | 956,400 | 20.7% |
| STORE_FAST_STORE_FAST | 55,553 | 1.2% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,001,378 | 41.1% |
| CALL_PY_EXACT_ARGS | 11,739,119 | 37.1% |
| LOAD_ATTR_PROPERTY | 5,063,410 | 16.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,196,552 | 3.8% |
| CALL_KW | 261,140 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,677,776 | 68.5% |
| RETURN_GENERATOR | 9,887,382 | 31.2% |
| MAKE_CELL | 78,500 | 0.2% |
| RESUME | 2,190 | 0.0% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,284,800 | 98.7% |
| POP_JUMP_IF_NONE | 15,920 | 1.2% |
| FOR_ITER_LIST | 880 | 0.1% |
| ENTER_EXECUTOR | 320 | 0.0% |
| STORE_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 643,240 | 49.4% |
| BUILD_LIST | 642,560 | 49.3% |
| LOAD_FAST | 16,060 | 1.2% |
| LOAD_GLOBAL | 200 | 0.0% |
| RERAISE | 160 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,571,379 | 99.6% |
| LOAD_DEREF | 64,935 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,636,314 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 21,997,819 | 26.9% |
| CALL_LIST_APPEND | 20,220,508 | 24.8% |
| POP_JUMP_IF_TRUE | 9,162,076 | 11.2% |
| ENTER_EXECUTOR | 8,734,273 | 10.7% |
| POP_JUMP_IF_FALSE | 8,279,560 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 9,199,983 | 11.3% |
| ENTER_EXECUTOR | 8,734,273 | 10.7% |
| FOR_ITER_TUPLE | 8,325,288 | 10.2% |
| CALL_FUNCTION_EX | 7,551,051 | 9.2% |
| SWAP | 6,302,121 | 7.7% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,277,637 | 44.4% |
| GET_ITER | 2,378,120 | 20.0% |
| COMPARE_OP_INT | 1,718,054 | 14.4% |
| ENTER_EXECUTOR | 1,616,629 | 13.6% |
| JUMP_BACKWARD | 265,607 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,815,500 | 57.3% |
| FOR_ITER_LIST | 2,695,202 | 22.7% |
| FOR_ITER_TUPLE | 913,580 | 7.7% |
| FOR_ITER_RANGE | 642,400 | 5.4% |
| JUMP_BACKWARD | 256,087 | 2.2% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 18,761,951 | 44.2% |
| JUMP_BACKWARD | 8,537,086 | 20.1% |
| LOAD_FAST | 7,617,558 | 17.9% |
| SWAP | 6,724,769 | 15.8% |
| ENTER_EXECUTOR | 746,264 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 25,277,881 | 59.5% |
| STORE_FAST | 7,810,548 | 18.4% |
| LOAD_FAST | 3,025,558 | 7.1% |
| ENTER_EXECUTOR | 2,590,066 | 6.1% |
| SWAP | 1,300,708 | 3.1% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 7,758,385 | 86.6% |
| STORE_FAST | 982,548 | 11.0% |
| STORE_DEREF | 185,694 | 2.1% |
| STORE_NAME | 26,000 | 0.3% |
| EXTENDED_ARG | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,822,146 | 76.2% |
| STORE_DEREF | 2,092,421 | 23.4% |
| STORE_NAME | 38,060 | 0.4% |
| EXTENDED_ARG | 2,540 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,759,145 | 100.0% |
| ENTER_EXECUTOR | 740 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 7,758,385 | 100.0% |
| CALL_INTRINSIC_1 | 1,060 | 0.0% |
| STORE_NAME | 440 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 14,931,943 | 32.9% |
| LOAD_FAST | 12,728,260 | 28.0% |
| LOAD_CONST | 10,976,213 | 24.2% |
| LOAD_FAST_LOAD_FAST | 5,893,554 | 13.0% |
| LOAD_GLOBAL_BUILTIN | 539,787 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 30,004,936 | 66.1% |
| YIELD_VALUE | 12,712,920 | 28.0% |
| POP_JUMP_IF_TRUE | 2,641,248 | 5.8% |
| EXTENDED_ARG | 20,300 | 0.0% |
| STORE_FAST | 8,960 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 9,399,700 | 48.9% |
| POP_JUMP_IF_TRUE | 6,999,361 | 36.4% |
| CALL_LIST_APPEND | 1,453,243 | 7.6% |
| POP_TOP | 524,721 | 2.7% |
| EXTENDED_ARG | 256,087 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 9,410,054 | 48.9% |
| FOR_ITER | 8,537,086 | 44.4% |
| FOR_ITER_TUPLE | 731,222 | 3.8% |
| EXTENDED_ARG | 265,607 | 1.4% |
| FOR_ITER_LIST | 166,288 | 0.9% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 928,400 | 82.8% |
| POP_EXCEPT | 159,130 | 14.2% |
| EXTENDED_ARG | 33,414 | 3.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 661,220 | 59.0% |
| SEND | 267,340 | 23.8% |
| LOAD_GLOBAL_BUILTIN | 120,002 | 10.7% |
| NOP | 35,527 | 3.2% |
| LOAD_FAST_LOAD_FAST | 17,960 | 1.6% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,138,419 | 70.9% |
| POP_TOP | 734,226 | 12.6% |
| STORE_FAST_STORE_FAST | 240,720 | 4.1% |
| CALL_LIST_APPEND | 191,810 | 3.3% |
| LOAD_FAST | 137,493 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,007,154 | 68.6% |
| BUILD_MAP | 721,820 | 12.4% |
| LOAD_FAST_LOAD_FAST | 441,752 | 7.6% |
| LOAD_GLOBAL_BUILTIN | 329,636 | 5.6% |
| STORE_FAST | 119,093 | 2.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,144,607 | 44.8% |
| BUILD_TUPLE | 653,920 | 25.6% |
| RETURN_VALUE | 510,709 | 20.0% |
| LOAD_ATTR_PROPERTY | 64,443 | 2.5% |
| BINARY_SUBSCR | 37,834 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 2,424,317 | 94.8% |
| JUMP_BACKWARD | 127,622 | 5.0% |
| LOAD_NAME | 4,800 | 0.2% |
| CALL_INTRINSIC_1 | 160 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,346,926 | 99.8% |
| LOAD_CONST | 1,260 | 0.1% |
| LOAD_DEREF | 640 | 0.0% |
| LOAD_ATTR_SLOT | 200 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,347,806 | 99.9% |
| STORE_DEREF | 880 | 0.1% |
| STORE_NAME | 180 | 0.0% |
| STORE_FAST | 160 | 0.0% |
| EXTENDED_ARG | 40 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,964,793 | 55.4% |
| LOAD_GLOBAL_MODULE | 33,550,990 | 36.4% |
| CALL_TYPE_1 | 2,352,281 | 2.6% |
| LOAD_ATTR_SLOT | 2,297,046 | 2.5% |
| LOAD_GLOBAL_BUILTIN | 1,905,140 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 34,991,961 | 38.0% |
| LOAD_FAST | 16,037,861 | 17.4% |
| IS_OP | 14,931,943 | 16.2% |
| PUSH_NULL | 8,322,738 | 9.0% |
| CONTAINS_OP | 3,188,626 | 3.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 68,842,430 | 36.8% |
| LOAD_CONST | 40,321,075 | 21.6% |
| RESUME_CHECK | 15,611,361 | 8.3% |
| BUILD_TUPLE | 10,429,940 | 5.6% |
| RETURN_CONST | 9,526,680 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,321,075 | 21.6% |
| CALL_BUILTIN_FAST | 24,050,815 | 12.9% |
| COMPARE_OP_INT | 20,725,796 | 11.1% |
| STORE_FAST | 14,264,529 | 7.6% |
| MAKE_FUNCTION | 12,424,856 | 6.6% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 10,424,045 | 20.6% |
| STORE_FAST_STORE_FAST | 9,015,038 | 17.8% |
| LOAD_ATTR_SLOT | 6,403,860 | 12.7% |
| POP_JUMP_IF_FALSE | 4,652,702 | 9.2% |
| LOAD_ATTR_METHOD_NO_DICT | 3,319,048 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 11,815,135 | 23.4% |
| LOAD_FAST | 9,344,611 | 18.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,189,775 | 18.2% |
| BINARY_SUBSCR | 6,403,860 | 12.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 3,109,100 | 6.2% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 168,825,574 | 19.4% |
| LOAD_GLOBAL_BUILTIN | 149,685,315 | 17.2% |
| RESUME_CHECK | 115,532,021 | 13.3% |
| POP_JUMP_IF_FALSE | 107,873,166 | 12.4% |
| PUSH_NULL | 44,199,920 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 94,211,645 | 10.8% |
| LOAD_ATTR_METHOD_NO_DICT | 74,196,339 | 8.5% |
| LOAD_CONST | 68,842,430 | 7.9% |
| RETURN_VALUE | 52,928,357 | 6.1% |
| LOAD_GLOBAL_MODULE | 52,519,800 | 6.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 8,282,571 | 55.4% |
| LOAD_FAST_AND_CLEAR | 6,674,329 | 44.6% |
| MAKE_CELL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 8,282,491 | 55.4% |
| LOAD_FAST_AND_CLEAR | 6,674,329 | 44.6% |
| MAKE_CELL | 160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,557,060 | 99.0% |
| POP_TOP | 7,360 | 0.5% |
| LOAD_FAST | 4,000 | 0.3% |
| LOAD_GLOBAL_BUILTIN | 2,980 | 0.2% |
| POP_JUMP_IF_FALSE | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 1,556,980 | 99.0% |
| POP_JUMP_IF_NOT_NONE | 7,360 | 0.5% |
| LOAD_FAST | 3,860 | 0.2% |
| COMPARE_OP_INT | 1,920 | 0.1% |
| CALL_BUILTIN_CLASS | 1,360 | 0.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 50,470,565 | 24.4% |
| LOAD_GLOBAL_BUILTIN | 27,853,342 | 13.5% |
| POP_JUMP_IF_FALSE | 22,294,854 | 10.8% |
| STORE_FAST_STORE_FAST | 14,727,970 | 7.1% |
| RESUME_CHECK | 12,115,748 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 26,359,654 | 12.8% |
| COMPARE_OP | 21,085,793 | 10.2% |
| BUILD_TUPLE | 18,992,763 | 9.2% |
| STORE_SUBSCR_LIST_INT | 18,842,414 | 9.1% |
| CALL_BUILTIN_FAST | 16,712,752 | 8.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,264 | 19.4% |
| LOAD_FAST | 34,230 | 18.8% |
| STORE_FAST | 26,963 | 14.8% |
| RESUME_CHECK | 10,939 | 6.0% |
| RESUME | 10,795 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 50,594 | 27.8% |
| LOAD_GLOBAL_BUILTIN | 41,270 | 22.7% |
| LOAD_FAST | 39,646 | 21.8% |
| LOAD_ATTR | 14,090 | 7.7% |
| CALL | 9,835 | 5.4% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 27,640 | 38.6% |
| LOAD_NAME | 8,000 | 11.2% |
| CALL | 7,360 | 10.3% |
| LIST_APPEND | 4,800 | 6.7% |
| POP_TOP | 4,740 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 22,500 | 31.5% |
| LOAD_CONST | 19,560 | 27.3% |
| LOAD_NAME | 8,000 | 11.2% |
| CALL | 5,380 | 7.5% |
| EXTENDED_ARG | 3,700 | 5.2% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,087 | 90.1% |
| LOAD_DEREF | 120 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 500 | 41.4% |
| CALL | 327 | 27.1% |
| LOAD_FAST | 180 | 14.9% |
| PUSH_NULL | 100 | 8.3% |
| LOAD_SUPER_ATTR_ATTR | 100 | 8.3% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,274,686 | 37.6% |
| CACHE | 1,509,098 | 24.9% |
| CALL_PY_EXACT_ARGS | 772,744 | 12.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 654,389 | 10.8% |
| CALL | 523,688 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,771,010 | 62.3% |
| MAKE_CELL | 2,274,686 | 37.6% |
| RESUME | 3,000 | 0.0% |
| RETURN_GENERATOR | 400 | 0.0% |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,707,289 | 99.7% |
| LOAD_FAST | 4,160 | 0.1% |
| RETURN_VALUE | 3,620 | 0.1% |
| CALL | 1,920 | 0.0% |
| STORE_FAST | 1,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,714,849 | 99.9% |
| JUMP_BACKWARD | 4,560 | 0.1% |
| LOAD_CONST | 320 | 0.0% |
| LOAD_NAME | 20 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 107,694,311 | 43.8% |
| COMPARE_OP_INT | 33,192,369 | 13.5% |
| IS_OP | 30,004,936 | 12.2% |
| COMPARE_OP | 19,268,102 | 7.8% |
| COMPARE_OP_STR | 13,990,776 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,873,166 | 43.9% |
| LOAD_GLOBAL_BUILTIN | 57,223,068 | 23.3% |
| RETURN_CONST | 28,518,253 | 11.6% |
| LOAD_FAST_LOAD_FAST | 22,294,854 | 9.1% |
| LOAD_GLOBAL_MODULE | 9,654,591 | 3.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 6,179,567 | 52.9% |
| LOAD_FAST | 4,397,866 | 37.6% |
| LOAD_DEREF | 1,088,841 | 9.3% |
| LOAD_ATTR_INSTANCE_VALUE | 8,380 | 0.1% |
| EXTENDED_ARG | 5,434 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,186,675 | 52.9% |
| LOAD_FAST | 2,614,973 | 22.4% |
| LOAD_CONST | 1,111,411 | 9.5% |
| LOAD_GLOBAL_BUILTIN | 957,537 | 8.2% |
| NOP | 601,539 | 5.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,127,713 | 93.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,225,001 | 5.4% |
| EXTENDED_ARG | 179,780 | 0.8% |
| ENTER_EXECUTOR | 40,308 | 0.2% |
| CALL_BUILTIN_FAST | 11,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,235,259 | 54.1% |
| LOAD_FAST_LOAD_FAST | 6,536,133 | 28.9% |
| LOAD_GLOBAL_MODULE | 1,880,456 | 8.3% |
| LOAD_GLOBAL_BUILTIN | 1,385,260 | 6.1% |
| ENTER_EXECUTOR | 443,817 | 2.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 47,874,006 | 70.6% |
| TO_BOOL_INT | 8,152,460 | 12.0% |
| CONTAINS_OP | 3,977,438 | 5.9% |
| IS_OP | 2,641,248 | 3.9% |
| COMPARE_OP | 2,275,294 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,715,620 | 48.2% |
| ENTER_EXECUTOR | 9,162,076 | 13.5% |
| JUMP_BACKWARD | 6,999,361 | 10.3% |
| LOAD_GLOBAL_BUILTIN | 5,244,229 | 7.7% |
| NOP | 4,183,848 | 6.2% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 118,914 | 99.9% |
| CALL_KW | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 115,254 | 98.4% |
| COPY | 1,760 | 1.5% |
| LOAD_CONST | 160 | 0.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 28,518,253 | 52.1% |
| RESUME_CHECK | 10,045,333 | 18.4% |
| FOR_ITER_LIST | 5,671,562 | 10.4% |
| ENTER_EXECUTOR | 4,683,539 | 8.6% |
| STORE_SUBSCR | 1,551,785 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 32,283,254 | 59.0% |
| LOAD_CONST | 9,526,680 | 17.4% |
| POP_TOP | 7,934,355 | 14.5% |
| TO_BOOL_BOOL | 2,386,676 | 4.4% |
| STORE_FAST | 1,541,081 | 2.8% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 267,340 | 60.4% |
| LOAD_CONST | 172,420 | 38.9% |
| SEND | 2,500 | 0.6% |
| SEND_GEN | 580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 257,060 | 58.0% |
| END_SEND | 168,540 | 38.1% |
| RESUME_CHECK | 10,200 | 2.3% |
| POP_TOP | 3,920 | 0.9% |
| SEND | 2,500 | 0.6% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,000 | 88.5% |
| RETURN_VALUE | 2,040 | 11.3% |
| BINARY_SUBSCR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 16,660 | 92.1% |
| JUMP_BACKWARD | 1,420 | 7.9% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 10,410,754 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 1,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,814,638 | 94.3% |
| STORE_FAST | 307,020 | 2.9% |
| STORE_DEREF | 113,221 | 1.1% |
| LOAD_CONST | 52,360 | 0.5% |
| LOAD_GLOBAL_MODULE | 42,944 | 0.4% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 486,831 | 82.3% |
| LOAD_FAST | 98,460 | 16.6% |
| STORE_ATTR | 3,910 | 0.7% |
| SWAP | 2,158 | 0.4% |
| LOAD_DEREF | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 289,657 | 49.0% |
| LOAD_FAST_LOAD_FAST | 116,254 | 19.7% |
| LOAD_FAST | 89,988 | 15.2% |
| LOAD_GLOBAL_BUILTIN | 74,060 | 12.5% |
| STORE_ATTR_INSTANCE_VALUE | 3,960 | 0.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 3,578,200 | 46.2% |
| IMPORT_FROM | 2,092,421 | 27.0% |
| LOAD_ATTR | 1,558,826 | 20.1% |
| STORE_FAST | 240,860 | 3.1% |
| SET_FUNCTION_ATTRIBUTE | 113,221 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,578,160 | 46.2% |
| POP_TOP | 1,906,727 | 24.6% |
| LOAD_DEREF | 1,298,320 | 16.8% |
| LOAD_GLOBAL_MODULE | 481,480 | 6.2% |
| IMPORT_FROM | 185,694 | 2.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 38,444,544 | 12.6% |
| LOAD_ATTR | 34,991,961 | 11.5% |
| BINARY_OP | 24,134,621 | 7.9% |
| LOAD_ATTR_SLOT | 22,510,022 | 7.4% |
| LOAD_CONST | 14,264,529 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 168,825,574 | 55.5% |
| LOAD_FAST_LOAD_FAST | 50,470,565 | 16.6% |
| LOAD_GLOBAL_BUILTIN | 31,738,869 | 10.4% |
| LOAD_GLOBAL_MODULE | 11,260,695 | 3.7% |
| STORE_FAST | 9,342,170 | 3.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,260,934 | 71.8% |
| FOR_ITER_TUPLE | 410,392 | 23.4% |
| FOR_ITER_RANGE | 47,440 | 2.7% |
| FOR_ITER | 38,160 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,178,901 | 67.1% |
| LOAD_ATTR_PROPERTY | 191,687 | 10.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 186,737 | 10.6% |
| LOAD_DEREF | 49,680 | 2.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 46,380 | 2.6% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 50,403,987 | 88.3% |
| RETURN_VALUE | 3,248,152 | 5.7% |
| UNPACK_SEQUENCE_TUPLE | 1,397,385 | 2.4% |
| STORE_FAST_STORE_FAST | 771,929 | 1.4% |
| BUILD_LIST | 413,120 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 16,351,111 | 28.6% |
| LOAD_FAST_LOAD_FAST | 14,727,970 | 25.8% |
| LOAD_FAST | 13,894,947 | 24.3% |
| LOAD_DEREF | 9,015,038 | 15.8% |
| LOAD_GLOBAL_MODULE | 1,036,560 | 1.8% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 38,060 | 29.0% |
| MAKE_FUNCTION | 33,580 | 25.6% |
| CALL | 21,600 | 16.5% |
| LOAD_CONST | 9,120 | 6.9% |
| SET_FUNCTION_ATTRIBUTE | 7,660 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,660 | 37.1% |
| LOAD_NAME | 27,640 | 21.1% |
| IMPORT_FROM | 26,000 | 19.8% |
| POP_TOP | 12,080 | 9.2% |
| RETURN_CONST | 4,860 | 3.7% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 9,392,740 | 21.8% |
| LOAD_FAST_AND_CLEAR | 8,282,491 | 19.2% |
| ENTER_EXECUTOR | 6,302,121 | 14.6% |
| BUILD_MAP | 4,716,089 | 10.9% |
| LOAD_FAST | 4,609,927 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,392,960 | 21.8% |
| STORE_FAST | 7,930,892 | 18.4% |
| FOR_ITER | 6,724,769 | 15.6% |
| POP_TOP | 5,747,107 | 13.3% |
| BUILD_MAP | 4,716,089 | 10.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,474 | 26.3% |
| FOR_ITER | 6,805 | 17.1% |
| CALL_BUILTIN_CLASS | 6,340 | 15.9% |
| LOAD_FAST | 3,977 | 10.0% |
| CALL_BUILTIN_FAST | 3,260 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 18,695 | 47.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,436 | 23.7% |
| STORE_FAST | 8,092 | 20.3% |
| UNPACK_SEQUENCE_TUPLE | 1,152 | 2.9% |
| UNPACK_SEQUENCE | 914 | 2.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 12,712,920 | 55.3% |
| ENTER_EXECUTOR | 4,975,450 | 21.7% |
| CALL_ISINSTANCE | 2,232,688 | 9.7% |
| LOAD_FAST | 1,140,784 | 5.0% |
| YIELD_VALUE | 677,464 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 22,130,395 | 96.3% |
| YIELD_VALUE | 677,464 | 2.9% |
| STORE_FAST | 162,805 | 0.7% |
| UNPACK_SEQUENCE | 3,120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,520 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 18,055 | 37.9% |
| CALL | 11,132 | 23.4% |
| CALL_PY_EXACT_ARGS | 6,107 | 12.8% |
| POP_TOP | 3,960 | 8.3% |
| MAKE_CELL | 3,000 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,708 | 37.2% |
| LOAD_GLOBAL | 10,795 | 22.7% |
| LOAD_CONST | 8,764 | 18.4% |
| LOAD_NAME | 3,700 | 7.8% |
| POP_TOP | 3,360 | 7.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,448,124 | 90.9% |
| LOAD_FAST_LOAD_FAST | 574,094 | 4.6% |
| BINARY_SUBSCR_DICT | 422,960 | 3.4% |
| CALL_BUILTIN_CLASS | 81,213 | 0.6% |
| LOAD_FAST | 43,684 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 9,390,756 | 74.5% |
| STORE_FAST | 1,538,879 | 12.2% |
| SWAP | 944,658 | 7.5% |
| LOAD_CONST | 269,136 | 2.1% |
| LOAD_FAST | 201,626 | 1.6% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 479,440 | 86.9% |
| CALL_METHOD_DESCRIPTOR_O | 39,600 | 7.2% |
| LOAD_FAST | 15,880 | 2.9% |
| LOAD_FAST_LOAD_FAST | 8,400 | 1.5% |
| BINARY_SUBSCR_LIST_INT | 3,680 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 498,440 | 90.4% |
| RETURN_VALUE | 41,840 | 7.6% |
| LOAD_FAST | 6,720 | 1.2% |
| CALL_BUILTIN_FAST | 1,760 | 0.3% |
| CALL | 1,720 | 0.3% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,668,681 | 60.5% |
| LOAD_ATTR_SLOT | 723,514 | 26.2% |
| LOAD_FAST_LOAD_FAST | 269,853 | 9.8% |
| LOAD_FAST | 94,315 | 3.4% |
| BINARY_OP | 1,489 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,291,867 | 83.1% |
| LOAD_FAST_LOAD_FAST | 181,170 | 6.6% |
| STORE_FAST | 175,635 | 6.4% |
| LOAD_FAST | 76,510 | 2.8% |
| LOAD_GLOBAL_MODULE | 25,190 | 0.9% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 83.3% |
| BINARY_OP | 80 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 280 | 58.3% |
| BINARY_OP | 200 | 41.7% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,558,607 | 63.0% |
| LOAD_FAST_LOAD_FAST | 607,358 | 24.5% |
| BINARY_SUBSCR_LIST_INT | 181,120 | 7.3% |
| LOAD_FAST | 122,672 | 5.0% |
| BINARY_OP | 2,201 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,082,420 | 43.7% |
| STORE_FAST | 700,148 | 28.3% |
| BINARY_OP | 311,650 | 12.6% |
| COMPARE_OP_INT | 184,120 | 7.4% |
| BINARY_SUBSCR_LIST_INT | 53,880 | 2.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,129,159 | 35.9% |
| LOAD_FAST_LOAD_FAST | 810,248 | 25.7% |
| LOAD_CONST | 642,800 | 20.4% |
| CALL_TUPLE_1 | 443,840 | 14.1% |
| RETURN_VALUE | 114,345 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 866,157 | 27.5% |
| RETURN_VALUE | 809,326 | 25.7% |
| BINARY_OP_ADD_INT | 422,960 | 13.4% |
| PUSH_NULL | 376,980 | 12.0% |
| SWAP | 318,100 | 10.1% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 59,680 | 37.5% |
| LOAD_FAST_LOAD_FAST | 40,800 | 25.6% |
| ENTER_EXECUTOR | 39,680 | 24.9% |
| LOAD_CONST | 14,546 | 9.1% |
| BUILD_SLICE | 3,840 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 159,244 | 100.0% |
| RETURN_VALUE | 1 | 0.0% |
| LOAD_CONST | 1 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 26,359,654 | 90.9% |
| COPY | 1,067,720 | 3.7% |
| LOAD_CONST | 1,025,966 | 3.5% |
| CALL_BUILTIN_CLASS | 282,682 | 1.0% |
| LOAD_FAST | 204,203 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,401,100 | 32.4% |
| SWAP | 9,392,740 | 32.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,532,494 | 26.0% |
| LOAD_CONST | 1,068,180 | 3.7% |
| RETURN_VALUE | 432,307 | 1.5% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 18,880 | 98.0% |
| LOAD_FAST | 360 | 1.9% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 18,880 | 98.0% |
| LIST_APPEND | 380 | 2.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,718,821 | 97.0% |
| LOAD_FAST | 263,313 | 2.9% |
| BINARY_SUBSCR | 2,747 | 0.0% |
| LOAD_FAST_LOAD_FAST | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,735,369 | 52.7% |
| CALL_LIST_APPEND | 1,762,920 | 19.6% |
| BUILD_LIST | 1,557,600 | 17.3% |
| LOAD_FAST | 321,878 | 3.6% |
| BINARY_OP | 205,240 | 2.3% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 77,660 | 81.0% |
| LOAD_FAST_LOAD_FAST | 16,820 | 17.5% |
| LOAD_GLOBAL_MODULE | 1,000 | 1.0% |
| CALL | 240 | 0.3% |
| PUSH_NULL | 160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 95,740 | 99.8% |
| COPY_FREE_VARS | 180 | 0.2% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,333,451 | 56.7% |
| BINARY_OP_ADD_INT | 9,390,756 | 39.9% |
| LOAD_FAST_LOAD_FAST | 480,396 | 2.0% |
| LOAD_ATTR | 152,040 | 0.6% |
| LOAD_DEREF | 83,580 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,652,526 | 92.1% |
| COPY_FREE_VARS | 1,196,552 | 5.1% |
| MAKE_CELL | 654,389 | 2.8% |
| POP_TOP | 7,360 | 0.0% |
| CALL_PY_EXACT_ARGS | 717 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,796,125 | 32.6% |
| CALL_BUILTIN_CLASS | 1,959,131 | 22.9% |
| LOAD_CONST | 710,920 | 8.3% |
| CALL_LEN | 610,856 | 7.1% |
| BINARY_SUBSCR | 571,356 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,069,787 | 35.8% |
| CALL_BUILTIN_CLASS | 1,959,131 | 22.9% |
| GET_ITER | 1,728,022 | 20.2% |
| BINARY_SUBSCR_LIST_INT | 282,682 | 3.3% |
| LOAD_FAST_LOAD_FAST | 241,335 | 2.8% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,050,815 | 56.3% |
| LOAD_FAST_LOAD_FAST | 16,712,752 | 39.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,337,214 | 3.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 1.1% |
| LOAD_FAST | 40,906 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 17,392,566 | 40.9% |
| STORE_FAST | 10,982,072 | 25.8% |
| TO_BOOL | 10,287,220 | 24.2% |
| PUSH_NULL | 2,128,620 | 5.0% |
| RETURN_VALUE | 1,500,034 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,891,069 | 85.3% |
| LOAD_FAST | 260,143 | 4.5% |
| CALL_BUILTIN_CLASS | 237,986 | 4.1% |
| BINARY_OP | 148,353 | 2.6% |
| LOAD_CONST | 124,413 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_TUPLE_1 | 4,707,069 | 82.1% |
| STORE_FAST | 315,537 | 5.5% |
| GET_ITER | 173,780 | 3.0% |
| RETURN_VALUE | 158,213 | 2.8% |
| LOAD_CONST | 128,673 | 2.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,700,959 | 41.7% |
| RETURN_GENERATOR | 10,191,909 | 27.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 5,613,111 | 14.9% |
| LOAD_ATTR_SLOT | 4,879,431 | 13.0% |
| BINARY_OP | 1,095,131 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,581,659 | 36.1% |
| RETURN_VALUE | 11,432,780 | 30.4% |
| TO_BOOL_BOOL | 9,892,197 | 26.3% |
| GET_ITER | 2,591,106 | 6.9% |
| LOAD_FAST | 50,620 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 30,200,647 | 53.8% |
| LOAD_GLOBAL_BUILTIN | 18,408,334 | 32.8% |
| LOAD_DEREF | 2,859,544 | 5.1% |
| LOAD_FAST_LOAD_FAST | 2,648,574 | 4.7% |
| LOAD_FAST | 1,615,684 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 53,249,516 | 94.9% |
| YIELD_VALUE | 2,232,688 | 4.0% |
| COPY | 525,020 | 0.9% |
| RETURN_VALUE | 71,527 | 0.1% |
| TO_BOOL | 9,664 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,045,693 | 96.3% |
| LOAD_GLOBAL_MODULE | 553,240 | 2.0% |
| BINARY_SUBSCR | 173,720 | 0.6% |
| RETURN_VALUE | 95,032 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 93,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 10,266,520 | 36.6% |
| LOAD_GLOBAL_BUILTIN | 9,672,235 | 34.5% |
| LOAD_CONST | 7,178,018 | 25.6% |
| CALL_BUILTIN_CLASS | 610,856 | 2.2% |
| STORE_FAST | 84,420 | 0.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,553,304 | 64.8% |
| BUILD_TUPLE | 3,214,240 | 13.4% |
| BINARY_SUBSCR_TUPLE_INT | 1,762,920 | 7.3% |
| LOAD_FAST_CHECK | 1,556,980 | 6.5% |
| ENTER_EXECUTOR | 963,240 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 20,220,508 | 84.2% |
| LOAD_FAST | 1,681,753 | 7.0% |
| JUMP_BACKWARD | 1,453,243 | 6.1% |
| EXTENDED_ARG | 240,260 | 1.0% |
| LOAD_FAST_LOAD_FAST | 207,500 | 0.9% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,896,004 | 43.4% |
| ENTER_EXECUTOR | 5,182,966 | 22.7% |
| LOAD_CONST | 2,332,687 | 10.2% |
| BUILD_LIST | 2,294,386 | 10.1% |
| BUILD_MAP | 1,561,360 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,757,880 | 56.0% |
| STORE_FAST | 3,368,302 | 14.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,116,160 | 13.7% |
| POP_TOP | 1,818,419 | 8.0% |
| GET_ITER | 737,586 | 3.2% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,220 | 46.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,620 | 34.0% |
| LOAD_FAST | 800 | 16.8% |
| CALL | 120 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,860 | 39.1% |
| LOAD_FAST_LOAD_FAST | 940 | 19.7% |
| GET_ITER | 880 | 18.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 680 | 14.3% |
| LOAD_ATTR_METHOD_NO_DICT | 220 | 4.6% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 22,641,509 | 81.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,807,628 | 17.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,789 | 0.4% |
| LOAD_ATTR | 72,820 | 0.3% |
| CALL | 3,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 12,589,362 | 45.5% |
| STORE_FAST | 9,683,510 | 35.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,891,069 | 17.7% |
| CALL_BUILTIN_CLASS | 169,738 | 0.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,789 | 0.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,853,920 | 62.3% |
| LOAD_CONST | 1,226,501 | 26.8% |
| LOAD_FAST | 290,680 | 6.3% |
| RETURN_VALUE | 97,600 | 2.1% |
| BUILD_LIST | 44,300 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,234,100 | 70.5% |
| LOAD_CONST | 1,224,501 | 26.7% |
| TO_BOOL_NONE | 42,400 | 0.9% |
| BINARY_OP_ADD_UNICODE | 39,600 | 0.9% |
| STORE_FAST | 25,520 | 0.6% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 21,015,808 | 35.0% |
| LOAD_FAST | 15,470,237 | 25.8% |
| GET_ITER | 13,002,361 | 21.7% |
| LOAD_FAST_LOAD_FAST | 5,927,488 | 9.9% |
| LOAD_SUPER_ATTR_METHOD | 1,539,407 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 43,028,954 | 71.7% |
| COPY_FREE_VARS | 11,739,119 | 19.6% |
| RETURN_GENERATOR | 4,261,123 | 7.1% |
| MAKE_CELL | 772,744 | 1.3% |
| CALL_PY_EXACT_ARGS | 144,902 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,626,555 | 35.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,373,885 | 29.9% |
| ENTER_EXECUTOR | 1,016,613 | 22.1% |
| RETURN_VALUE | 192,673 | 4.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 157,986 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,380,153 | 95.3% |
| RETURN_GENERATOR | 163,640 | 3.6% |
| MAKE_CELL | 53,727 | 1.2% |
| CALL_PY_EXACT_ARGS | 220 | 0.0% |
| CALL_PY_WITH_DEFAULTS | 220 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 145,520 | 62.4% |
| RETURN_VALUE | 73,520 | 31.5% |
| LOAD_FAST | 14,020 | 6.0% |
| CALL | 180 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 219,100 | 93.9% |
| BUILD_TUPLE | 6,860 | 2.9% |
| STORE_FAST | 4,380 | 1.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,840 | 0.8% |
| CALL_BUILTIN_O | 980 | 0.4% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,707,069 | 80.4% |
| LOAD_FAST | 1,017,314 | 17.4% |
| STORE_FAST | 105,752 | 1.8% |
| RETURN_VALUE | 7,920 | 0.1% |
| LOAD_DEREF | 4,132 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 4,707,269 | 80.4% |
| BINARY_SUBSCR_DICT | 443,840 | 7.6% |
| STORE_FAST | 353,192 | 6.0% |
| STORE_SUBSCR_DICT | 181,360 | 3.1% |
| RETURN_VALUE | 56,520 | 1.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,728,635 | 99.5% |
| LOAD_CONST | 65,974 | 0.4% |
| LOAD_GLOBAL_MODULE | 1,840 | 0.0% |
| CALL | 1,082 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,423,555 | 43.4% |
| COMPARE_OP | 5,882,438 | 39.8% |
| LOAD_ATTR | 2,352,281 | 15.9% |
| IS_OP | 64,234 | 0.4% |
| STORE_FAST | 32,977 | 0.2% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 493,683 | 90.8% |
| CALL_BUILTIN_CLASS | 25,400 | 4.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 21,539 | 4.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,840 | 0.3% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 542,002 | 99.7% |
| RETURN_VALUE | 1,580 | 0.3% |
| COMPARE_OP | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,725,796 | 42.6% |
| LOAD_FAST_LOAD_FAST | 16,148,037 | 33.2% |
| CALL_LEN | 10,266,520 | 21.1% |
| LOAD_FAST | 971,239 | 2.0% |
| LOAD_ATTR_SLOT | 225,373 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 33,192,369 | 68.3% |
| BINARY_OP | 6,277,300 | 12.9% |
| LOAD_GLOBAL_BUILTIN | 4,738,660 | 9.7% |
| EXTENDED_ARG | 1,718,054 | 3.5% |
| LOAD_FAST_LOAD_FAST | 1,538,560 | 3.2% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,030,880 | 71.5% |
| LOAD_CONST | 3,806,044 | 27.1% |
| LOAD_GLOBAL_MODULE | 192,480 | 1.4% |
| LOAD_FAST | 2,040 | 0.0% |
| LOAD_ATTR | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 13,990,776 | 99.7% |
| YIELD_VALUE | 40,148 | 0.3% |
| POP_JUMP_IF_TRUE | 2,240 | 0.0% |
| EXTENDED_ARG | 860 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 9,199,983 | 41.0% |
| LOAD_FAST | 4,843,695 | 21.6% |
| GET_ITER | 4,308,144 | 19.2% |
| EXTENDED_ARG | 2,695,202 | 12.0% |
| SWAP | 1,219,674 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,160,840 | 40.8% |
| RETURN_CONST | 5,671,562 | 25.3% |
| LOAD_FAST | 4,094,179 | 18.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,444,651 | 6.4% |
| STORE_FAST_LOAD_FAST | 1,260,934 | 5.6% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 9,410,054 | 85.0% |
| GET_ITER | 668,910 | 6.0% |
| EXTENDED_ARG | 642,400 | 5.8% |
| ENTER_EXECUTOR | 285,820 | 2.6% |
| SWAP | 38,880 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,158,774 | 91.7% |
| RETURN_CONST | 630,076 | 5.7% |
| LOAD_FAST | 195,180 | 1.8% |
| STORE_FAST_LOAD_FAST | 47,440 | 0.4% |
| SWAP | 38,520 | 0.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,980,431 | 48.0% |
| ENTER_EXECUTOR | 8,325,288 | 40.1% |
| EXTENDED_ARG | 913,580 | 4.4% |
| JUMP_BACKWARD | 731,222 | 3.5% |
| LOAD_FAST | 518,688 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,660,570 | 51.3% |
| LOAD_FAST | 7,494,789 | 36.1% |
| RETURN_CONST | 789,025 | 3.8% |
| LOAD_GLOBAL_MODULE | 602,506 | 2.9% |
| STORE_FAST_LOAD_FAST | 410,392 | 2.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 170,180 | 90.7% |
| LOAD_FAST_LOAD_FAST | 16,900 | 9.0% |
| LOAD_GLOBAL_MODULE | 280 | 0.1% |
| LOAD_ATTR | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 146,960 | 78.3% |
| LOAD_FAST | 34,200 | 18.2% |
| STORE_FAST | 6,320 | 3.4% |
| LOAD_ATTR | 120 | 0.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,496,416 | 59.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,061,036 | 11.6% |
| LOAD_DEREF | 1,058,496 | 11.5% |
| COPY | 956,400 | 10.4% |
| LOAD_GLOBAL_MODULE | 571,356 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,578,001 | 17.2% |
| CALL_BUILTIN_FAST | 1,337,214 | 14.6% |
| POP_JUMP_IF_NOT_NONE | 1,225,001 | 13.4% |
| STORE_FAST | 1,076,196 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,061,036 | 11.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,196,339 | 85.4% |
| RETURN_VALUE | 4,635,637 | 5.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,116,160 | 3.6% |
| LOAD_GLOBAL_MODULE | 1,983,777 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,578,001 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,853,967 | 34.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 22,641,509 | 26.1% |
| CALL_PY_EXACT_ARGS | 21,015,808 | 24.2% |
| LOAD_CONST | 4,051,860 | 4.7% |
| LOAD_DEREF | 3,319,048 | 3.8% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 9,189,775 | 51.7% |
| LOAD_ATTR_SLOT | 4,711,169 | 26.5% |
| LOAD_FAST | 3,666,470 | 20.6% |
| LOAD_ATTR | 147,505 | 0.8% |
| STORE_FAST_LOAD_FAST | 46,380 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,804,076 | 55.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,807,628 | 27.0% |
| LOAD_FAST_LOAD_FAST | 2,851,262 | 16.0% |
| CALL_PY_EXACT_ARGS | 313,665 | 1.8% |
| LOAD_CONST | 6,339 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,261,138 | 99.2% |
| LOAD_FAST | 5,540 | 0.4% |
| LOAD_ATTR_MODULE | 2,640 | 0.2% |
| LOAD_ATTR | 1,402 | 0.1% |
| LOAD_FAST_LOAD_FAST | 1,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,044,487 | 82.1% |
| CALL_PY_EXACT_ARGS | 80,716 | 6.3% |
| CALL | 57,377 | 4.5% |
| LOAD_FAST | 25,860 | 2.0% |
| LOAD_ATTR_SLOT | 15,920 | 1.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,267,628 | 83.3% |
| ENTER_EXECUTOR | 5,164,872 | 9.1% |
| LOAD_DEREF | 3,109,100 | 5.5% |
| BINARY_SUBSCR_LIST_INT | 342,120 | 0.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 214,811 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 42,258,136 | 74.5% |
| CALL_BUILTIN_O | 5,613,111 | 9.9% |
| BUILD_TUPLE | 2,484,120 | 4.4% |
| LOAD_FAST | 1,921,403 | 3.4% |
| BINARY_OP_MULTIPLY_INT | 1,668,681 | 2.9% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 995,742 | 60.3% |
| LOAD_FAST_LOAD_FAST | 478,940 | 29.0% |
| LOAD_DEREF | 144,340 | 8.7% |
| LOAD_ATTR | 12,020 | 0.7% |
| ENTER_EXECUTOR | 11,651 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 478,200 | 29.0% |
| TO_BOOL_STR | 478,200 | 29.0% |
| TO_BOOL_BOOL | 413,926 | 25.1% |
| LOAD_CONST | 106,520 | 6.5% |
| CALL_LEN | 73,480 | 4.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,063,131 | 89.5% |
| ENTER_EXECUTOR | 1,564,958 | 5.6% |
| RETURN_VALUE | 642,522 | 2.3% |
| STORE_FAST_LOAD_FAST | 191,687 | 0.7% |
| LOAD_DEREF | 190,726 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,812,537 | 67.2% |
| COPY_FREE_VARS | 5,063,410 | 18.1% |
| GET_ITER | 1,920,306 | 6.9% |
| TO_BOOL_BOOL | 717,600 | 2.6% |
| STORE_FAST | 505,681 | 1.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,211,645 | 98.4% |
| ENTER_EXECUTOR | 687,400 | 0.7% |
| LOAD_ATTR_SLOT | 613,664 | 0.6% |
| LOAD_FAST_LOAD_FAST | 88,063 | 0.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 70,970 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,432,101 | 34.9% |
| STORE_FAST | 22,510,022 | 23.5% |
| LOAD_DEREF | 6,403,860 | 6.7% |
| LOAD_FAST | 5,219,624 | 5.5% |
| LOAD_CONST | 5,210,062 | 5.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 57,223,068 | 26.2% |
| RESUME_CHECK | 41,199,854 | 18.9% |
| STORE_FAST | 31,738,869 | 14.6% |
| LOAD_FAST | 19,740,560 | 9.1% |
| STORE_FAST_STORE_FAST | 16,351,111 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 149,685,315 | 68.6% |
| LOAD_FAST_LOAD_FAST | 27,853,342 | 12.8% |
| CALL_ISINSTANCE | 18,408,334 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 8,864,648 | 4.1% |
| LOAD_DEREF | 3,218,049 | 1.5% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,519,800 | 47.2% |
| RESUME_CHECK | 16,022,336 | 14.4% |
| STORE_FAST | 11,260,695 | 10.1% |
| POP_JUMP_IF_FALSE | 9,654,591 | 8.7% |
| NOP | 6,407,295 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 33,550,990 | 30.2% |
| CALL_ISINSTANCE | 30,200,647 | 27.1% |
| LOAD_FAST | 28,383,426 | 25.5% |
| LOAD_DEREF | 3,261,221 | 2.9% |
| LOAD_FAST_LOAD_FAST | 3,194,002 | 2.9% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,104,513 | 93.5% |
| LOAD_DEREF | 77,300 | 6.5% |
| LOAD_SUPER_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,181,913 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,807,650 | 100.0% |
| LOAD_SUPER_ATTR | 500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,539,407 | 85.1% |
| LOAD_GLOBAL_MODULE | 172,243 | 9.5% |
| LOAD_FAST | 78,580 | 4.3% |
| LOAD_FAST_LOAD_FAST | 17,560 | 1.0% |
| CALL | 360 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 99,105,613 | 39.7% |
| CALL_PY_EXACT_ARGS | 43,028,954 | 17.2% |
| COPY_FREE_VARS | 21,677,776 | 8.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 21,652,526 | 8.7% |
| LOAD_ATTR_PROPERTY | 18,812,537 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 115,532,021 | 46.2% |
| LOAD_GLOBAL_BUILTIN | 41,199,854 | 16.5% |
| NOP | 21,363,331 | 8.6% |
| LOAD_GLOBAL_MODULE | 16,022,336 | 6.4% |
| LOAD_CONST | 15,611,361 | 6.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 661,220 | 64.2% |
| LOAD_CONST | 367,964 | 35.7% |
| SEND | 620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 646,240 | 62.8% |
| POP_TOP | 352,904 | 34.3% |
| YIELD_VALUE | 15,060 | 1.5% |
| END_SEND | 15,020 | 1.5% |
| SEND | 580 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,103,703 | 62.6% |
| SWAP | 956,400 | 28.5% |
| LOAD_FAST_LOAD_FAST | 259,600 | 7.7% |
| LOAD_ATTR_SLOT | 35,138 | 1.0% |
| STORE_ATTR | 3,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,210,678 | 36.0% |
| RETURN_CONST | 887,360 | 26.4% |
| NOP | 480,100 | 14.3% |
| RETURN_VALUE | 478,260 | 14.2% |
| LOAD_FAST_LOAD_FAST | 122,720 | 3.7% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,732,378 | 52.2% |
| LOAD_FAST | 4,285,082 | 47.3% |
| STORE_ATTR_SLOT | 41,763 | 0.5% |
| STORE_ATTR | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,673,158 | 51.6% |
| LOAD_FAST_LOAD_FAST | 2,256,376 | 24.9% |
| LOAD_CONST | 1,890,721 | 20.9% |
| LOAD_GLOBAL_MODULE | 136,845 | 1.5% |
| RETURN_CONST | 45,660 | 0.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,568,598 | 68.9% |
| LOAD_FAST | 396,830 | 17.4% |
| CALL_TUPLE_1 | 181,360 | 8.0% |
| RETURN_VALUE | 82,840 | 3.6% |
| LOAD_CONST | 39,338 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,790,028 | 78.6% |
| LOAD_FAST_LOAD_FAST | 183,280 | 8.1% |
| LOAD_FAST | 164,822 | 7.2% |
| JUMP_BACKWARD | 91,920 | 4.0% |
| LOAD_GLOBAL_MODULE | 38,958 | 1.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,842,414 | 93.8% |
| SWAP | 1,067,720 | 5.3% |
| LOAD_FAST | 98,933 | 0.5% |
| BINARY_OP_SUBTRACT_INT | 49,280 | 0.2% |
| LOAD_CONST | 20,720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,017,800 | 49.9% |
| JUMP_BACKWARD | 9,399,700 | 46.8% |
| ENTER_EXECUTOR | 599,687 | 3.0% |
| LOAD_FAST | 21,140 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 21,060 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 224,345 | 98.5% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| ENTER_EXECUTOR | 860 | 0.4% |
| STORE_FAST_LOAD_FAST | 760 | 0.3% |
| TO_BOOL | 392 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 216,427 | 95.0% |
| POP_JUMP_IF_FALSE | 9,876 | 4.3% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| TO_BOOL | 54 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 53,249,516 | 32.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 42,258,136 | 26.1% |
| LOAD_FAST | 21,599,188 | 13.3% |
| CALL_BUILTIN_FAST | 17,392,566 | 10.7% |
| CALL_BUILTIN_O | 9,892,197 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 107,694,311 | 66.5% |
| POP_JUMP_IF_TRUE | 47,874,006 | 29.6% |
| EXTENDED_ARG | 5,277,637 | 3.3% |
| UNARY_NOT | 1,084,985 | 0.7% |
| TO_BOOL_NONE | 1,280 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,626,924 | 95.3% |
| BINARY_OP | 722,567 | 3.9% |
| BINARY_SUBSCR_TUPLE_INT | 63,311 | 0.3% |
| BINARY_SUBSCR_LIST_INT | 45,280 | 0.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 24,855 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,350,840 | 55.9% |
| POP_JUMP_IF_TRUE | 8,152,460 | 44.1% |
| TO_BOOL_NONE | 440 | 0.0% |
| UNARY_NOT | 169 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,228,019 | 97.1% |
| COPY | 39,560 | 1.7% |
| LOAD_DEREF | 9,107 | 0.4% |
| LOAD_ATTR_INSTANCE_VALUE | 8,780 | 0.4% |
| STORE_FAST | 6,240 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 831,730 | 36.3% |
| POP_JUMP_IF_TRUE | 784,639 | 34.2% |
| UNARY_NOT | 661,866 | 28.8% |
| EXTENDED_ARG | 15,720 | 0.7% |
| TO_BOOL_NONE | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,841,684 | 69.6% |
| RETURN_VALUE | 389,100 | 14.7% |
| LOAD_ATTR_PROPERTY | 293,243 | 11.1% |
| CALL_METHOD_DESCRIPTOR_O | 42,400 | 1.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 41,963 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,938,113 | 73.2% |
| POP_JUMP_IF_TRUE | 690,025 | 26.1% |
| EXTENDED_ARG | 15,420 | 0.6% |
| TO_BOOL_BOOL | 1,680 | 0.1% |
| TO_BOOL | 1,500 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 95.1% |
| LOAD_FAST | 11,300 | 2.2% |
| STORE_FAST_LOAD_FAST | 11,200 | 2.2% |
| COPY | 2,120 | 0.4% |
| LOAD_GLOBAL_MODULE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 487,380 | 96.9% |
| POP_JUMP_IF_TRUE | 15,720 | 3.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120,306 | 67.1% |
| RETURN_VALUE | 49,120 | 27.4% |
| CALL_BUILTIN_CLASS | 2,600 | 1.5% |
| BINARY_SUBSCR_LIST_INT | 1,880 | 1.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 114,940 | 64.1% |
| STORE_FAST_STORE_FAST | 64,266 | 35.9% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 885,419 | 55.6% |
| RETURN_VALUE | 660,896 | 41.5% |
| STORE_FAST | 40,240 | 2.5% |
| CALL_METHOD_DESCRIPTOR_O | 3,680 | 0.2% |
| UNPACK_SEQUENCE | 1,152 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,397,385 | 87.8% |
| STORE_FAST | 154,822 | 9.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 39,760 | 2.5% |
| STORE_DEREF | 120 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 25,277,881 | 46.6% |
| RETURN_VALUE | 19,465,497 | 35.9% |
| BINARY_SUBSCR_LIST_INT | 7,532,494 | 13.9% |
| FOR_ITER_LIST | 1,444,651 | 2.7% |
| FOR_ITER_TUPLE | 278,336 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 50,403,987 | 93.0% |
| STORE_DEREF | 3,578,200 | 6.6% |
| STORE_FAST | 216,441 | 0.4% |
| UNPACK_SEQUENCE_LIST | 1,760 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,320 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 22,529 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,529 | 100.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 100,541 | 52.6% |
| GET_ITER | 90,653 | 47.4% |
| FOR_ITER | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,621 | 52.1% |
| POP_TOP | 90,493 | 47.3% |
| RESUME | 860 | 0.4% |
| STORE_FAST | 320 | 0.2% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,020 | 99.0% |
| BINARY_OP | 20 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,040 | 100.0% |


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 80 | 66.7% |
| POP_TOP | 20 | 16.7% |
| ENTER_EXECUTOR | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 80 | 66.7% |
| BUILD_LIST | 20 | 16.7% |
| RETURN_CONST | 20 | 16.7% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_CONST_KEY_MAP | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 20 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 1,920 | 92.3% |
| DELETE_FAST | 160 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 320 | 66.7% |
| COPY | 160 | 33.3% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| BINARY_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 40 | 66.7% |
| CALL | 20 | 33.3% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_BUILD_CLASS | 20 | 100.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 280 | 93.3% |
| BINARY_OP | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 300 | 100.0% |


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
|     deferred | 34,036,908 | 64.3% |
|          hit | 18,799,595 | 35.5% |
|         miss | 120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,846 | 11.9% |
| Failure | 50,548 | 88.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 9,457 | 18.7% |
| multiply different types | 7,185 | 14.2% |
| subtract other | 6,760 | 13.4% |
| and int | 4,126 | 8.2% |
| rshift | 3,810 | 7.5% |
| or | 3,700 | 7.3% |
| power | 2,875 | 5.7% |
| true divide different types | 2,525 | 5.0% |
| multiply other | 2,260 | 4.5% |
| remainder | 2,072 | 4.1% |
| add different types | 1,822 | 3.6% |
| floor divide | 1,280 | 2.5% |
| subtract different types | 1,183 | 2.3% |
| xor | 585 | 1.2% |
| and other | 374 | 0.7% |
| true divide other | 300 | 0.6% |
| lshift | 229 | 0.5% |
| true divide float | 5 | 0.0% |


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
|     deferred | 21,722,974 | 33.7% |
|          hit | 42,675,696 | 66.2% |
|         miss | 14,924 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,727 | 33.9% |
| Failure | 15,036 | 66.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 11,731 | 78.0% |
| out of range | 1,960 | 13.0% |
| buffer int | 1,320 | 8.8% |
| array int | 20 | 0.1% |
| tuple slice | 5 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 56,008,750 | 12.6% |
|        deopt | 31,040 | 0.0% |
|          hit | 386,063,782 | 87.2% |
|         miss | 31,407,353 | 7.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 674,210 | 91.0% |
| Failure | 66,947 | 9.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass | 25,958 | 38.8% |
| code complex parameters | 14,055 | 21.0% |
| class no vectorcall | 9,220 | 13.8% |
| class mutable | 3,100 | 4.6% |
| other | 3,040 | 4.5% |
| wrong number arguments | 2,520 | 3.8% |
| cfunc noargs | 2,400 | 3.6% |
| bound method | 2,174 | 3.2% |
| cfunc varargs keywords | 1,200 | 1.8% |
| no dict | 1,120 | 1.7% |
| meth descr varargs | 720 | 1.1% |
| meth descr varargs keywords | 640 | 1.0% |
| operator wrapper | 380 | 0.6% |
| cfunc varargs | 240 | 0.4% |
| meth descr method fastcall keywords | 180 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 38,138,799 | 36.7% |
|          hit | 65,631,680 | 63.2% |
|         miss | 575,970 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20,475 | 22.9% |
| Failure | 68,988 | 77.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 18,426 | 26.7% |
| other | 15,225 | 22.1% |
| different types | 12,178 | 17.7% |
| tuple | 10,052 | 14.6% |
| string | 9,960 | 14.4% |
| bool | 1,947 | 2.8% |
| float long | 340 | 0.5% |
| set | 280 | 0.4% |
| baseobject | 280 | 0.4% |
| list | 220 | 0.3% |
| long float | 80 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 42,729,998 | 44.1% |
|          hit | 54,134,865 | 55.8% |
|         miss | 351,723 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 18,527 | 26.3% |
| Failure | 51,796 | 73.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 30,566 | 59.0% |
| set | 6,116 | 11.8% |
| zip | 5,220 | 10.1% |
| enumerate | 3,634 | 7.0% |
| other | 2,000 | 3.9% |
| itertools | 1,840 | 3.6% |
| dict keys | 1,400 | 2.7% |
| reversed list | 860 | 1.7% |
| dict values | 80 | 0.2% |
| ascii string | 80 | 0.2% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 156,580,117 | 38.2% |
|        deopt | 20 | 0.0% |
|          hit | 251,738,369 | 61.4% |
|         miss | 66,003,707 | 16.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,323,116 | 89.7% |
| Failure | 152,162 | 10.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| mutable class | 58,664 | 38.6% |
| metaclass attribute | 53,436 | 35.1% |
| method | 10,381 | 6.8% |
| has managed dict | 8,740 | 5.7% |
| overridden | 8,669 | 5.7% |
| shadowed | 5,300 | 3.5% |
| class method obj | 3,900 | 2.6% |
| builtin class method | 1,320 | 0.9% |
| not managed dict | 772 | 0.5% |
| non object slot | 560 | 0.4% |
| not in keys | 300 | 0.2% |
| non overriding descriptor | 60 | 0.0% |
| module attr not found | 60 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 110,423 | 0.0% |
|          hit | 329,299,265 | 99.9% |
|         miss | 20,420 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 92,024 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 607 | 0.0% |
|          hit | 2,996,063 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 600 | 100.0% |
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
|     deferred | 469,800 | 31.9% |
|          hit | 999,144 | 67.8% |
|         miss | 30,660 | 2.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 16.8% |
| Failure | 3,080 | 83.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| list | 3,080 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,761,604 | 21.2% |
|          hit | 10,198,166 | 78.4% |
|         miss | 2,220,958 | 17.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 46,823 | 92.3% |
| Failure | 3,910 | 7.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 1,960 | 50.1% |
| not managed dict | 1,450 | 37.1% |
| overridden | 240 | 6.1% |
| no dict | 200 | 5.1% |
| not in keys | 60 | 1.5% |


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
|     deferred | 1,647,235 | 6.8% |
|          hit | 22,617,097 | 93.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,724 | 45.3% |
| Failure | 3,287 | 54.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict subclass no override | 3,287 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,263,147 | 6.3% |
|          hit | 197,718,136 | 93.7% |
|         miss | 440,043 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 59,966 | 72.3% |
| Failure | 22,951 | 27.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 10,798 | 47.0% |
| number | 3,509 | 15.3% |
| mapping | 3,300 | 14.4% |
| dict | 2,260 | 9.8% |
| other | 1,618 | 7.0% |
| set | 1,426 | 6.2% |
| float | 40 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 27,587 | 0.0% |
|          hit | 105,533,393 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 11,408 | 93.6% |
| Failure | 774 | 6.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 714 | 92.2% |
| iterator | 60 | 7.8% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 2,775,092,731 | 54.5% |
| Not specialized | 617,561,499 | 12.1% |
| Specialized hits | 1,600,773,057 | 31.4% |
| Specialized misses | 101,065,878 | 2.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 156,580,117 | 42.6% |
| CALL | 56,008,750 | 15.2% |
| FOR_ITER | 42,729,998 | 11.6% |
| COMPARE_OP | 38,138,799 | 10.4% |
| BINARY_OP | 34,036,908 | 9.3% |
| BINARY_SUBSCR | 21,722,974 | 5.9% |
| TO_BOOL | 13,263,147 | 3.6% |
| STORE_ATTR | 2,761,604 | 0.8% |
| STORE_SUBSCR | 1,647,235 | 0.4% |
| SEND | 469,800 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 36,512,467 | 36.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 15,762,253 | 15.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 14,344,049 | 14.2% |
| LOAD_ATTR_METHOD_NO_DICT | 9,131,162 | 9.0% |
| CALL_PY_EXACT_ARGS | 7,826,883 | 7.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,479,378 | 6.4% |
| LOAD_ATTR_PROPERTY | 4,113,487 | 4.1% |
| CALL_BUILTIN_O | 2,661,152 | 2.6% |
| STORE_ATTR_SLOT | 2,219,978 | 2.2% |
| COMPARE_OP_INT | 574,370 | 0.6% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 127,524,212 | 46.8% |
| Calls to Python functions inlined | 144,740,836 | 53.2% |
| Calls via PyEval_EvalFrame (total) | 127,524,212 | 46.8% |
| Calls via PyEval_EvalFrame (vector) | 98,451,772 | 36.2% |
| Calls via PyEval_EvalFrame (generator) | 29,072,440 | 10.7% |
| Calls via PyEval_EvalFrame (legacy) | 4,640 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 98,444,472 | 36.2% |
| Calls via PyEval_EvalFrame (build class) | 2,660 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 23,667,967 | 8.7% |
| Calls via PyEval_EvalFrame (function ex) | 11,824,907 | 4.3% |
| Calls via PyEval_EvalFrame (api) | 53,324,981 | 19.6% |
| Calls via PyEval_EvalFrame (method) | 6,960 | 0.0% |
| Frame objects created | 1,287,023 | 0.5% |
| Frames pushed | 242,084,130 | 88.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 362,862,543 | 54.3% |
| Frees to freelist | 363,105,529 |  |
| Allocations | 305,034,634 | 45.7% |
| Allocations to 512 bytes | 303,969,655 | 45.5% |
| Allocations to 4 kbytes | 1,040,519 | 0.2% |
| Allocations over 4 kbytes | 24,460 | 0.0% |
| Frees | 312,710,059 |  |
| New values | 1,057,373 |  |
| Interpreter increfs | 2,301,887,770 | 56.4% |
| Interpreter decrefs | 2,725,644,568 | 58.5% |
| Increfs | 1,777,134,938 | 43.6% |
| Decrefs | 1,933,025,541 | 41.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 60 | 0.0% |
| Method cache hits | 242,093,550 |  |
| Method cache misses | 3,976,812 |  |
| Method cache collisions | 6,614,185 |  |
| Method cache dunder hits | 345,703,944 |  |
| Method cache dunder misses | 2,637,864 |  |


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
| Optimization attempts | 26,586 |  |
| Traces created | 25,826 | 97.1% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 77 | 0.3% |
| Trace too long | 0 | 0.0% |
| Trace too short | 760 | 2.9% |
| Inner loop found | 280 | 1.1% |
| Recursive call | 420 | 1.6% |
| Low confidence | 91 | 0.3% |
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
| <= 8 | 40 | 0.2% |
| <= 16 | 3,769 | 14.6% |
| <= 32 | 12,495 | 48.4% |
| <= 64 | 7,722 | 29.9% |
| <= 128 | 1,720 | 6.7% |
| <= 256 | 80 | 0.3% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 2,676 | 10.4% |
| <= 16 | 4,350 | 16.8% |
| <= 32 | 2,761 | 10.7% |
| <= 64 | 1,600 | 6.2% |
| <= 128 | 160 | 0.6% |
| <= 256 | 20 | 0.1% |


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
| LOAD_ATTR_PROPERTY | 3,056 |
| YIELD_VALUE | 1,120 |
| CALL | 1,053 |
| FOR_ITER_GEN | 760 |
| CALL_PY_WITH_DEFAULTS | 660 |
| CALL_FUNCTION_EX | 640 |
| CALL_KW | 500 |
| CALL_LIST_APPEND | 480 |
| BINARY_SUBSCR_GETITEM | 240 |
| IMPORT_NAME | 40 |


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
| watched dict modification | 80 |
| watched globals modification | 80 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 80 |


</details>

---
Stats gathered on: 2024-09-10
