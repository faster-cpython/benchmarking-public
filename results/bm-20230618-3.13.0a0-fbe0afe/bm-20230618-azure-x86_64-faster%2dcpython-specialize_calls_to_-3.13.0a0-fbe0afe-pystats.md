
# Pystats results

- fork: faster-cpython
- ref: specialize-calls-to-python-classes
- commit hash: fbe0afe
- commit date: 2023-06-18T10:27:33+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 27,028,557,596 | 19.2% | 19.2% |  |
| STORE_FAST | 9,675,328,565 | 6.9% | 26.1% |  |
| LOAD_CONST | 9,381,617,255 | 6.7% | 32.7% |  |
| POP_JUMP_IF_FALSE | 8,193,919,267 | 5.8% | 38.5% |  |
| LOAD_FAST_LOAD_FAST | 8,050,349,328 | 5.7% | 44.3% |  |
| RESUME | 4,856,870,910 | 3.4% | 47.7% |  |
| LOAD_GLOBAL_BUILTIN | 4,041,878,587 | 2.9% | 50.6% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,591,071,324 | 2.6% | 53.1% | 5.8% |
| JUMP_BACKWARD | 3,191,305,194 | 2.3% | 55.4% |  |
| RETURN_VALUE | 2,916,506,414 | 2.1% | 57.5% |  |
| CALL_PY_EXACT_ARGS | 2,758,681,386 | 2.0% | 59.4% | 3.1% |
| LOAD_GLOBAL_MODULE | 2,754,030,618 | 2.0% | 61.4% | 0.0% |
| BINARY_SUBSCR | 2,343,207,298 | 1.7% | 63.1% |  |
| POP_TOP | 2,279,433,177 | 1.6% | 64.7% |  |
| BINARY_OP_ADD_INT | 2,198,081,644 | 1.6% | 66.2% | 0.0% |
| CONTAINS_OP | 1,974,801,925 | 1.4% | 67.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,775,828,644 | 1.3% | 68.9% | 8.7% |
| COMPARE_OP_STR | 1,586,135,953 | 1.1% | 70.0% | 0.0% |
| STORE_FAST_STORE_FAST | 1,528,571,240 | 1.1% | 71.1% |  |
| NOP | 1,479,995,523 | 1.1% | 72.2% |  |
| POP_JUMP_IF_TRUE | 1,441,566,603 | 1.0% | 73.2% |  |
| COMPARE_OP_INT | 1,393,649,801 | 1.0% | 74.2% | 0.1% |
| LOAD_ATTR_SLOT | 1,317,811,076 | 0.9% | 75.1% | 4.3% |
| RETURN_CONST | 1,307,503,327 | 0.9% | 76.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,305,334,854 | 0.9% | 77.0% | 3.5% |
| FOR_ITER_LIST | 1,235,972,497 | 0.9% | 77.8% | 5.3% |
| LOAD_ATTR | 1,202,746,235 | 0.9% | 78.7% |  |
| INTERPRETER_EXIT | 1,191,851,334 | 0.8% | 79.5% |  |
| STORE_ATTR_SLOT | 1,050,946,892 | 0.7% | 80.3% | 10.6% |
| COPY | 1,030,005,717 | 0.7% | 81.0% |  |
| CALL_NO_KW_BUILTIN_FAST | 928,199,252 | 0.7% | 81.7% | 0.0% |
| SWAP | 904,826,142 | 0.6% | 82.3% |  |
| BINARY_SUBSCR_LIST_INT | 879,289,520 | 0.6% | 82.9% | 0.4% |
| CALL | 874,205,218 | 0.6% | 83.6% |  |
| BINARY_OP | 829,010,298 | 0.6% | 84.2% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,611,296 | 0.6% | 84.7% | 0.8% |
| LOAD_DEREF | 807,127,990 | 0.6% | 85.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 787,387,934 | 0.6% | 85.9% | 8.8% |
| CALL_NO_KW_BUILTIN_O | 781,866,356 | 0.6% | 86.4% | 0.1% |
| CALL_NO_KW_ISINSTANCE | 777,967,312 | 0.6% | 87.0% |  |
| PUSH_NULL | 746,951,882 | 0.5% | 87.5% |  |
| YIELD_VALUE | 692,366,292 | 0.5% | 88.0% |  |
| BUILD_TUPLE | 666,857,190 | 0.5% | 88.5% |  |
| BINARY_SUBSCR_DICT | 613,545,029 | 0.4% | 88.9% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 598,988,640 | 0.4% | 89.3% |  |
| GET_ITER | 580,758,385 | 0.4% | 89.8% |  |
| FOR_ITER_RANGE | 477,118,400 | 0.3% | 90.1% | 0.0% |
| BINARY_OP_SUBTRACT_INT | 468,262,525 | 0.3% | 90.4% | 0.1% |
| IS_OP | 434,350,002 | 0.3% | 90.7% |  |
| UNPACK_SEQUENCE_TUPLE | 419,572,324 | 0.3% | 91.0% | 0.3% |
| FOR_ITER_TUPLE | 416,433,676 | 0.3% | 91.3% | 15.7% |
| JUMP_FORWARD | 408,712,656 | 0.3% | 91.6% |  |
| POP_JUMP_IF_NOT_NONE | 408,613,967 | 0.3% | 91.9% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 392,943,951 | 0.3% | 92.2% | 1.7% |
| BINARY_OP_ADD_FLOAT | 390,243,312 | 0.3% | 92.5% | 1.6% |
| LOAD_ATTR_WITH_HINT | 337,941,390 | 0.2% | 92.7% | 2.6% |
| CALL_NO_KW_TYPE_1 | 327,370,780 | 0.2% | 92.9% |  |
| LOAD_ATTR_MODULE | 326,443,236 | 0.2% | 93.2% | 0.0% |
| CALL_NO_KW_LEN | 318,781,946 | 0.2% | 93.4% |  |
| STORE_SUBSCR | 315,798,654 | 0.2% | 93.6% |  |
| SEND_GEN | 301,845,848 | 0.2% | 93.8% |  |
| STORE_SUBSCR_LIST_INT | 301,564,020 | 0.2% | 94.0% | 0.0% |
| BUILD_LIST | 291,876,796 | 0.2% | 94.3% |  |
| POP_JUMP_IF_NONE | 282,497,225 | 0.2% | 94.5% |  |
| FOR_ITER | 281,692,152 | 0.2% | 94.7% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,755,059 | 0.2% | 94.8% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 265,876,856 | 0.2% | 95.0% | 3.2% |
| EXTENDED_ARG | 263,869,120 | 0.2% | 95.2% |  |
| COPY_FREE_VARS | 246,246,091 | 0.2% | 95.4% |  |
| BINARY_SLICE | 243,551,600 | 0.2% | 95.6% |  |
| CALL_NO_KW_LIST_APPEND | 238,176,982 | 0.2% | 95.7% | 0.0% |
| RETURN_GENERATOR | 238,121,312 | 0.2% | 95.9% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 225,397,087 | 0.2% | 96.1% | 7.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,261,852 | 0.2% | 96.2% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 211,253,771 | 0.2% | 96.4% | 0.0% |
| END_SEND | 193,874,708 | 0.1% | 96.5% |  |
| STORE_SUBSCR_DICT | 192,889,906 | 0.1% | 96.6% |  |
| BINARY_SUBSCR_TUPLE_INT | 186,614,160 | 0.1% | 96.8% |  |
| KW_NAMES | 168,570,595 | 0.1% | 96.9% |  |
| BUILD_SLICE | 158,173,976 | 0.1% | 97.0% |  |
| CALL_PY_WITH_DEFAULTS | 151,191,162 | 0.1% | 97.1% | 3.5% |
| CALL_INTRINSIC_1 | 147,720,880 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,525,147 | 0.1% | 97.3% | 0.0% |
| LIST_APPEND | 146,316,256 | 0.1% | 97.4% |  |
| UNPACK_SEQUENCE_LIST | 140,238,520 | 0.1% | 97.5% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,071,695 | 0.1% | 97.6% | 19.2% |
| COMPARE_OP | 135,145,526 | 0.1% | 97.7% |  |
| STORE_FAST_LOAD_FAST | 132,738,000 | 0.1% | 97.8% |  |
| DELETE_SUBSCR | 126,944,758 | 0.1% | 97.9% |  |
| UNARY_NEGATIVE | 121,209,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 120,578,224 | 0.1% | 98.1% | 1.1% |
| CALL_BUILTIN_CLASS | 119,370,310 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,634,500 | 0.1% | 98.2% |  |
| FORMAT_SIMPLE | 116,927,880 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 113,854,481 | 0.1% | 98.4% |  |
| SEND | 112,328,352 | 0.1% | 98.5% |  |
| LOAD_CLOSURE | 109,631,368 | 0.1% | 98.6% |  |
| COMPARE_OP_FLOAT | 109,606,206 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,731,420 | 0.1% | 98.7% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.8% |  |
| MAKE_FUNCTION | 93,654,313 | 0.1% | 98.9% |  |
| FOR_ITER_GEN | 90,139,500 | 0.1% | 98.9% | 0.0% |
| GET_AWAITABLE | 84,577,928 | 0.1% | 99.0% |  |
| MAKE_CELL | 83,115,956 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 82,577,425 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,792,940 | 0.1% | 99.2% | 0.0% |
| CALL_FUNCTION_EX | 73,865,420 | 0.1% | 99.2% |  |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,583,344 | 0.0% | 99.3% | 2.5% |
| BINARY_OP_ADD_UNICODE | 67,846,300 | 0.0% | 99.3% |  |
| EXIT_INIT_CHECK | 66,872,724 | 0.0% | 99.3% |  |
| STORE_DEREF | 65,100,060 | 0.0% | 99.4% |  |
| BUILD_STRING | 58,694,340 | 0.0% | 99.4% |  |
| END_FOR | 56,697,960 | 0.0% | 99.5% |  |
| STORE_ATTR_WITH_HINT | 52,984,262 | 0.0% | 99.5% | 5.9% |
| STORE_ATTR | 52,788,614 | 0.0% | 99.6% |  |
| BUILD_MAP | 51,981,692 | 0.0% | 99.6% |  |
| UNARY_NOT | 50,993,549 | 0.0% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 50,668,930 | 0.0% | 99.7% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 49,037,756 | 0.0% | 99.7% | 0.0% |
| LIST_EXTEND | 47,939,148 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 46,509,306 | 0.0% | 99.8% | 11.8% |
| MAP_ADD | 40,747,620 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,417,840 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 22,738,142 | 0.0% | 99.8% | 7.7% |
| CALL_NO_KW_TUPLE_1 | 21,711,140 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 17,143,984 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,143,984 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,775,971 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,169,260 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 12,501,773 | 0.0% | 99.9% |  |
| DICT_MERGE | 9,346,240 | 0.0% | 99.9% |  |
| RERAISE | 8,743,620 | 0.0% | 100.0% |  |
| DELETE_ATTR | 8,516,043 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,361,122 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,107,439 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,922,640 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 3,745,380 | 0.0% | 100.0% |  |
| BEFORE_WITH | 3,569,633 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,411,420 | 0.0% | 100.0% |  |
| SET_ADD | 3,100,800 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,296,260 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,850,880 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,532,940 | 0.0% | 100.0% |  |
| BUILD_SET | 1,466,520 | 0.0% | 100.0% |  |
| DELETE_FAST | 370,475 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 207,020 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,990 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,430 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,410 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 4,320 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,160 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,180 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| SET_UPDATE | 360 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 240 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 120 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 4,950,508,249 | 3.5% | 3.5% |
| STORE_FAST LOAD_FAST | 4,326,081,198 | 3.1% | 6.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,309,272,534 | 3.1% | 9.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,060,514,652 | 2.2% | 11.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,566,762,946 | 1.8% | 13.6% |
| CALL_PY_EXACT_ARGS RESUME | 2,456,908,688 | 1.7% | 15.4% |
| RESUME LOAD_FAST | 2,020,155,041 | 1.4% | 16.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,866,996,229 | 1.3% | 18.1% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,763,868,366 | 1.3% | 19.4% |
| LOAD_CONST COMPARE_OP_STR | 1,560,613,776 | 1.1% | 20.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,546,202,334 | 1.1% | 21.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,528,755,641 | 1.1% | 22.7% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 1,436,488,100 | 1.0% | 23.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,320,658,101 | 0.9% | 24.7% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,469,036 | 0.9% | 25.5% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,203,727,666 | 0.9% | 26.4% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,180,820,184 | 0.8% | 27.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,164,327,716 | 0.8% | 28.1% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,090,023,419 | 0.8% | 28.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,037,806,695 | 0.7% | 29.6% |
| LOAD_CONST LOAD_FAST | 1,022,611,831 | 0.7% | 30.3% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,041,440 | 0.7% | 31.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 971,100,006 | 0.7% | 31.7% |
| BINARY_SUBSCR STORE_FAST | 970,638,117 | 0.7% | 32.4% |
| NOP LOAD_FAST_LOAD_FAST | 956,612,067 | 0.7% | 33.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 955,042,684 | 0.7% | 33.7% |
| LOAD_FAST LOAD_FAST | 925,020,900 | 0.7% | 34.4% |
| JUMP_BACKWARD FOR_ITER_LIST | 922,952,537 | 0.7% | 35.1% |
| STORE_FAST JUMP_BACKWARD | 918,359,804 | 0.7% | 35.7% |
| BINARY_SUBSCR LOAD_FAST | 878,904,840 | 0.6% | 36.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 858,660,376 | 0.6% | 36.9% |
| RESUME LOAD_GLOBAL_BUILTIN | 825,765,522 | 0.6% | 37.5% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,096,820 | 0.6% | 38.1% |
| POP_TOP LOAD_FAST | 801,842,092 | 0.6% | 38.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 777,688,879 | 0.6% | 39.2% |
| LOAD_FAST RETURN_VALUE | 755,176,577 | 0.5% | 39.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 752,255,998 | 0.5% | 40.3% |
| LOAD_FAST POP_JUMP_IF_TRUE | 735,426,695 | 0.5% | 40.8% |
| LOAD_CONST LOAD_CONST | 734,071,478 | 0.5% | 41.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 722,673,564 | 0.5% | 41.9% |
| JUMP_BACKWARD NOP | 717,887,966 | 0.5% | 42.4% |
| LOAD_FAST LOAD_ATTR | 709,993,110 | 0.5% | 42.9% |
| STORE_FAST STORE_FAST | 709,955,358 | 0.5% | 43.4% |
| LOAD_FAST POP_JUMP_IF_FALSE | 671,217,254 | 0.5% | 43.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 656,765,766 | 0.5% | 44.3% |
| POP_TOP JUMP_BACKWARD | 653,588,819 | 0.5% | 44.8% |
| CALL_NO_KW_ISINSTANCE POP_JUMP_IF_FALSE | 645,946,364 | 0.5% | 45.2% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 637,415,728 | 0.5% | 45.7% |
| LOAD_CONST COMPARE_OP_INT | 608,828,089 | 0.4% | 46.1% |
| RETURN_VALUE STORE_FAST | 600,167,897 | 0.4% | 46.6% |
| FOR_ITER_LIST STORE_FAST | 585,447,897 | 0.4% | 47.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 565,611,994 | 0.4% | 47.4% |
| RETURN_CONST POP_TOP | 544,108,517 | 0.4% | 47.8% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_FALSE | 541,710,766 | 0.4% | 48.1% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,014,840 | 0.4% | 48.5% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 536,882,006 | 0.4% | 48.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 532,907,487 | 0.4% | 49.3% |
| LOAD_DEREF LOAD_FAST | 529,357,362 | 0.4% | 49.7% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 517,439,611 | 0.4% | 50.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 510,410,284 | 0.4% | 50.4% |
| LOAD_FAST CONTAINS_OP | 508,360,080 | 0.4% | 50.7% |
| RETURN_VALUE RETURN_VALUE | 503,937,112 | 0.4% | 51.1% |
| LOAD_FAST STORE_ATTR_SLOT | 497,613,081 | 0.4% | 51.5% |
| RESUME POP_TOP | 471,727,280 | 0.3% | 51.8% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 464,340,637 | 0.3% | 52.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 463,364,295 | 0.3% | 52.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 457,081,672 | 0.3% | 52.8% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 453,016,101 | 0.3% | 53.1% |
| YIELD_VALUE INTERPRETER_EXIT | 450,663,616 | 0.3% | 53.4% |
| STORE_FAST_STORE_FAST LOAD_FAST | 447,248,369 | 0.3% | 53.7% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 443,213,081 | 0.3% | 54.1% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 432,605,953 | 0.3% | 54.7% |
| PUSH_NULL LOAD_FAST | 429,407,448 | 0.3% | 55.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 425,028,487 | 0.3% | 55.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 416,610,166 | 0.3% | 55.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 412,375,363 | 0.3% | 55.9% |
| RETURN_CONST INTERPRETER_EXIT | 405,799,602 | 0.3% | 56.2% |
| BUILD_TUPLE RETURN_VALUE | 405,102,480 | 0.3% | 56.4% |
| LOAD_CONST STORE_FAST | 400,017,207 | 0.3% | 56.7% |
| FOR_ITER_RANGE STORE_FAST | 393,613,832 | 0.3% | 57.0% |
| IS_OP POP_JUMP_IF_FALSE | 385,735,202 | 0.3% | 57.3% |
| CALL_NO_KW_BUILTIN_FAST POP_JUMP_IF_FALSE | 371,852,708 | 0.3% | 57.5% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 362,173,820 | 0.3% | 57.8% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 358,216,577 | 0.3% | 58.1% |
| LOAD_FAST BINARY_SUBSCR | 357,175,920 | 0.3% | 58.3% |
| NOP LOAD_FAST | 350,228,962 | 0.2% | 58.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 348,936,668 | 0.2% | 58.8% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,708,546 | 0.2% | 59.0% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 338,306,588 | 0.2% | 59.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 336,549,732 | 0.2% | 59.5% |
| RESUME NOP | 334,548,946 | 0.2% | 59.8% |
| STORE_FAST LOAD_DEREF | 333,047,509 | 0.2% | 60.0% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 330,232,649 | 0.2% | 60.2% |
| RESUME LOAD_GLOBAL_MODULE | 323,756,098 | 0.2% | 60.5% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 323,735,600 | 0.2% | 60.7% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 320,906,023 | 0.2% | 60.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 320,411,244 | 0.2% | 61.1% |
| RETURN_VALUE INTERPRETER_EXIT | 317,298,536 | 0.2% | 61.4% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 314,363,580 | 0.2% | 61.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 120 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,405,572 | 67.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,024,260 | 28.7% |
| LOAD_GLOBAL_MODULE | 70,921 | 2.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,900 | 1.0% |
| CALL | 31,980 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,965,241 | 83.1% |
| STORE_FAST | 602,952 | 16.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 223,310,950 | 26.9% |
| LOAD_FAST | 185,143,493 | 22.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.7% |
| LOAD_FAST_LOAD_FAST | 47,329,420 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,171,820 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 163,924,140 | 19.8% |
| LOAD_FAST | 136,763,500 | 16.5% |
| LOAD_FAST_LOAD_FAST | 106,675,143 | 12.9% |
| RETURN_VALUE | 69,476,700 | 8.4% |
| LOAD_CONST | 68,118,840 | 8.2% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,043,300 | 72.8% |
| LOAD_FAST | 65,133,318 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 115,846,912 | 29.7% |
| LOAD_FAST | 59,481,900 | 15.2% |
| RETURN_VALUE | 31,350,960 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,763,868,366 | 80.2% |
| LOAD_FAST | 234,195,815 | 10.7% |
| LOAD_FAST_LOAD_FAST | 94,378,620 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,469,036 | 57.3% |
| LOAD_CONST | 131,530,200 | 6.0% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,055,140 | 4.4% |
| BINARY_SUBSCR | 89,539,800 | 4.1% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,035,180 | 47.2% |
| BINARY_SLICE | 15,579,000 | 23.0% |
| LOAD_CONST | 13,011,920 | 19.2% |
| LOAD_ATTR | 2,105,320 | 3.1% |
| BUILD_STRING | 2,011,200 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,139,520 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.4% |
| BUILD_TUPLE | 15,457,800 | 22.8% |
| LOAD_CONST | 8,423,340 | 12.4% |
| RETURN_VALUE | 3,047,100 | 4.5% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,590,560 | 43.7% |
| BINARY_SLICE | 1,580,580 | 26.7% |
| RETURN_VALUE | 680,220 | 11.5% |
| BINARY_OP_ADD_UNICODE | 365,020 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,731,820 | 63.0% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,480 | 8.6% |
| LOAD_CONST | 60,360 | 1.0% |
| LOAD_FAST_LOAD_FAST | 24,300 | 0.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,014,840 | 65.1% |
| LOAD_ATTR_INSTANCE_VALUE | 118,763,280 | 14.4% |
| BINARY_SUBSCR | 67,701,000 | 8.2% |
| LOAD_FAST_LOAD_FAST | 59,227,020 | 7.2% |
| CALL_BUILTIN_CLASS | 12,782,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 284,043,300 | 34.3% |
| YIELD_VALUE | 210,931,680 | 25.5% |
| LOAD_FAST | 111,266,580 | 13.4% |
| BINARY_OP_SUBTRACT_FLOAT | 109,285,680 | 13.2% |
| STORE_FAST | 36,069,060 | 4.4% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 96,055,140 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,996 | 19.3% |
| LOAD_FAST_LOAD_FAST | 44,782,000 | 16.8% |
| LOAD_FAST | 38,770,580 | 14.6% |
| BINARY_OP | 27,332,740 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,163,720 | 23.4% |
| LOAD_CONST | 61,631,700 | 23.2% |
| LOAD_FAST | 47,053,140 | 17.7% |
| LOAD_FAST_LOAD_FAST | 28,244,880 | 10.6% |
| BINARY_OP_ADD_INT | 23,999,760 | 9.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.5% |
| LOAD_FAST | 69,478,900 | 25.8% |
| LOAD_FAST_LOAD_FAST | 36,089,040 | 13.4% |
| LOAD_ATTR_INSTANCE_VALUE | 28,661,940 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,391,743 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.2% |
| SWAP | 55,701,000 | 20.6% |
| LOAD_FAST | 28,349,160 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 358,216,577 | 76.5% |
| LOAD_FAST | 66,874,540 | 14.3% |
| LOAD_FAST_LOAD_FAST | 30,055,488 | 6.4% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.1% |
| CALL_NO_KW_LEN | 2,724,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,675,400 | 20.0% |
| STORE_FAST | 84,169,325 | 18.0% |
| SWAP | 67,852,580 | 14.5% |
| RETURN_VALUE | 39,931,800 | 8.5% |
| BINARY_OP | 37,165,200 | 7.9% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 136,824,444 | 56.2% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.4% |
| BINARY_OP_ADD_INT | 35,910,960 | 14.7% |
| LOAD_FAST | 24,778,136 | 10.2% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,132,683 | 21.8% |
| GET_ITER | 33,131,560 | 13.6% |
| CALL_PY_EXACT_ARGS | 25,418,520 | 10.4% |
| BUILD_TUPLE | 24,334,200 | 10.0% |
| LOAD_DEREF | 18,985,680 | 7.8% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,436,488,100 | 61.3% |
| LOAD_FAST | 357,175,920 | 15.2% |
| LOAD_CONST | 139,424,777 | 6.0% |
| COPY | 109,564,100 | 4.7% |
| BUILD_SLICE | 104,833,920 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 970,638,117 | 41.4% |
| LOAD_FAST | 878,904,840 | 37.5% |
| LOAD_FAST_LOAD_FAST | 110,147,520 | 4.7% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |
| BINARY_SUBSCR | 48,584,661 | 2.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 205,776,760 | 33.5% |
| LOAD_FAST | 202,372,182 | 33.0% |
| LOAD_FAST_LOAD_FAST | 131,706,060 | 21.5% |
| BINARY_SUBSCR | 41,253,420 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 231,744,567 | 37.8% |
| RETURN_VALUE | 104,454,097 | 17.0% |
| CONTAINS_OP | 77,768,700 | 12.7% |
| LOAD_FAST | 59,365,320 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 41,379,720 | 6.7% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 68,480,547 | 46.7% |
| LOAD_CONST | 41,616,840 | 28.4% |
| BUILD_TUPLE | 28,812,000 | 19.7% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,020 | 2.3% |
| LOAD_FAST | 3,077,040 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,815,007 | 99.5% |
| MAKE_CELL | 705,600 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,420 | 0.0% |
| CONTAINS_OP | 1,020 | 0.0% |
| LOAD_FAST | 300 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 272,981,600 | 31.0% |
| LOAD_CONST | 180,391,372 | 20.5% |
| COPY | 157,633,380 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,082,508 | 17.5% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,492,342 | 26.8% |
| LOAD_CONST | 192,235,800 | 21.9% |
| LOAD_FAST | 140,235,780 | 16.0% |
| RETURN_VALUE | 90,397,860 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 146,807,400 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.3% |
| LOAD_FAST_LOAD_FAST | 3,360 | 0.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,660 | 38.6% |
| LOAD_CONST | 24,655,900 | 13.2% |
| LOAD_FAST | 24,038,880 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.4% |
| STORE_FAST | 8,164,120 | 4.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,745,380 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,930,620 | 51.5% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 45.5% |
| STORE_FAST | 55,200 | 1.5% |
| DICT_MERGE | 16,320 | 0.4% |
| LOAD_DEREF | 15,600 | 0.4% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 115,895,934 | 39.7% |
| LOAD_ATTR_SLOT | 37,318,140 | 12.8% |
| SWAP | 32,074,132 | 11.0% |
| LOAD_FAST | 25,052,258 | 8.6% |
| RESUME | 17,316,940 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 128,044,232 | 43.9% |
| LOAD_FAST | 83,267,612 | 28.5% |
| SWAP | 32,074,192 | 11.0% |
| CALL | 9,652,180 | 3.3% |
| RETURN_VALUE | 8,829,960 | 3.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,350,200 | 16.1% |
| RESUME | 6,654,352 | 12.8% |
| SWAP | 5,489,700 | 10.6% |
| LOAD_FAST | 5,420,640 | 10.4% |
| POP_JUMP_IF_FALSE | 3,888,600 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,252,940 | 39.0% |
| LOAD_FAST | 16,525,852 | 31.8% |
| SWAP | 5,489,700 | 10.6% |
| CALL_FUNCTION_EX | 3,354,540 | 6.5% |
| LOAD_CONST | 2,915,940 | 5.6% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| LOAD_CONST | 82,320 | 5.6% |
| LOAD_FAST | 52,920 | 3.6% |
| LOAD_GLOBAL_MODULE | 9,960 | 0.7% |
| LOAD_ATTR_MODULE | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| STORE_FAST | 48,240 | 3.3% |
| LOAD_GLOBAL_BUILTIN | 36,600 | 2.5% |
| CALL_PY_EXACT_ARGS | 34,080 | 2.3% |
| CONTAINS_OP | 9,600 | 0.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,374,420 | 99.5% |
| LOAD_FAST | 744,116 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,920 | 66.3% |
| DELETE_SUBSCR | 53,340,056 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 51,991,080 | 88.6% |
| LOAD_CONST | 6,703,260 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.5% |
| CALL | 12,295,080 | 20.9% |
| STORE_FAST | 4,596,420 | 7.8% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 167,388,536 | 25.1% |
| LOAD_FAST_LOAD_FAST | 125,015,043 | 18.7% |
| LOAD_FAST | 119,219,209 | 17.9% |
| LOAD_CLOSURE | 79,459,304 | 11.9% |
| CALL | 37,728,900 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 405,102,480 | 60.7% |
| LOAD_CONST | 81,838,513 | 12.3% |
| CALL_NO_KW_ISINSTANCE | 33,206,720 | 5.0% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.3% |
| LIST_APPEND | 26,458,320 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 254,177,059 | 29.1% |
| KW_NAMES | 142,949,435 | 16.4% |
| LOAD_FAST_LOAD_FAST | 97,111,997 | 11.1% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,660 | 8.2% |
| LOAD_GLOBAL_MODULE | 46,275,225 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 308,175,356 | 35.3% |
| RESUME | 202,931,795 | 23.2% |
| RETURN_VALUE | 46,790,890 | 5.4% |
| POP_TOP | 43,333,020 | 5.0% |
| LOAD_GLOBAL_MODULE | 38,964,956 | 4.5% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,746,168 | 31.0% |
| LOAD_CONST | 23,522,380 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.3% |
| LOAD_FAST_LOAD_FAST | 21,208,226 | 15.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,363,216 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,493,399 | 78.6% |
| COPY_FREE_VARS | 26,845,932 | 19.4% |
| POP_TOP | 2,060,540 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,244 | 0.3% |
| MAKE_CELL | 171,620 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,906,419 | 27.6% |
| CALL_NO_KW_LEN | 23,238,334 | 19.5% |
| LOAD_GLOBAL_BUILTIN | 9,122,140 | 7.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,231,400 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 61,505,213 | 51.5% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.7% |
| STORE_FAST | 11,950,320 | 10.0% |
| LOAD_FAST | 9,360,960 | 7.8% |
| CALL_BUILTIN_CLASS | 4,160,874 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,040 | 43.0% |
| KW_NAMES | 24,569,680 | 32.0% |
| LOAD_FAST | 13,267,940 | 17.3% |
| LOAD_FAST_LOAD_FAST | 2,692,180 | 3.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,011,320 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 40.8% |
| STORE_FAST | 27,836,360 | 36.2% |
| POP_TOP | 11,163,272 | 14.5% |
| RETURN_VALUE | 5,484,948 | 7.1% |
| LOAD_CONST | 322,140 | 0.4% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 41,802,960 | 56.6% |
| LOAD_FAST | 9,792,360 | 13.3% |
| DICT_MERGE | 9,346,240 | 12.7% |
| LOAD_FAST_LOAD_FAST | 5,883,880 | 8.0% |
| BUILD_MAP | 3,354,540 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 44,978,020 | 60.9% |
| STORE_FAST | 8,097,060 | 11.0% |
| RETURN_VALUE | 6,067,820 | 8.2% |
| MAKE_CELL | 4,707,040 | 6.4% |
| LOAD_FAST_LOAD_FAST | 3,815,580 | 5.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 62.3% |
| LIST_EXTEND | 47,195,440 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 63.7% |
| CALL_FUNCTION_EX | 41,802,960 | 28.3% |
| RERAISE | 6,377,160 | 4.3% |
| LOAD_CONST | 3,370,680 | 2.3% |
| BUILD_MAP | 2,008,660 | 1.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,916,888 | 39.2% |
| LOAD_CONST | 8,589,560 | 37.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,063,100 | 17.9% |
| LOAD_FAST_LOAD_FAST | 740,654 | 3.3% |
| LOAD_ATTR | 258,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,051,614 | 31.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 30.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,435,680 | 10.7% |
| BINARY_OP | 2,010,960 | 8.8% |
| RETURN_VALUE | 1,418,500 | 6.2% |


</details>

### CALL_NO_KW_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_NO_KW_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 20,210,840 | 29.5% |
| LOAD_GLOBAL_MODULE | 9,490,512 | 13.8% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.1% |
| RETURN_CONST | 7,864,740 | 11.5% |
| BINARY_OP_ADD_FLOAT | 5,100,000 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,174,492 | 95.0% |
| COPY_FREE_VARS | 1,697,992 | 2.5% |
| LOAD_FAST | 1,660,840 | 2.4% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 32,220 | 0.0% |
| STORE_FAST | 13,960 | 0.0% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,160 | 46.8% |
| LOAD_CONST | 338,306,588 | 36.4% |
| LOAD_FAST_LOAD_FAST | 71,767,860 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,659,160 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 371,852,708 | 40.1% |
| STORE_FAST | 310,343,708 | 33.4% |
| EXTENDED_ARG | 72,007,560 | 7.8% |
| POP_TOP | 47,607,996 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 536,882,006 | 68.7% |
| LOAD_CONST | 55,890,060 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,626,040 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,708,546 | 43.7% |
| LOAD_CONST | 171,752,796 | 22.0% |
| STORE_FAST | 163,891,569 | 21.0% |
| RETURN_VALUE | 29,118,946 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 330,232,649 | 42.4% |
| LOAD_GLOBAL_BUILTIN | 320,906,023 | 41.2% |
| LOAD_FAST_LOAD_FAST | 61,327,020 | 7.9% |
| BUILD_TUPLE | 33,206,720 | 4.3% |
| LOAD_ATTR_MODULE | 21,885,180 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 645,946,364 | 83.0% |
| POP_JUMP_IF_TRUE | 104,095,964 | 13.4% |
| UNARY_NOT | 7,956,060 | 1.0% |
| EXTENDED_ARG | 7,144,080 | 0.9% |
| COPY | 5,946,000 | 0.8% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200,462,059 | 62.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,415,647 | 13.3% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.3% |
| LOAD_DEREF | 20,446,300 | 6.4% |
| LOAD_ATTR_SLOT | 8,331,340 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 122,162,623 | 38.3% |
| LOAD_FAST | 43,784,160 | 13.7% |
| STORE_FAST | 38,003,926 | 11.9% |
| COMPARE_OP_INT | 32,501,580 | 10.2% |
| CALL_BUILTIN_CLASS | 23,238,334 | 7.3% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,098,692 | 73.1% |
| BINARY_SUBSCR | 20,171,040 | 8.5% |
| BINARY_SLICE | 18,506,220 | 7.8% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 4,894,440 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,857,542 | 37.7% |
| LOAD_FAST | 72,260,300 | 30.3% |
| EXTENDED_ARG | 27,730,920 | 11.6% |
| RETURN_CONST | 20,553,780 | 8.6% |
| LOAD_CONST | 11,303,760 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 176,804,361 | 45.0% |
| LOAD_CONST | 83,042,300 | 21.1% |
| LOAD_FAST_LOAD_FAST | 56,250,240 | 14.3% |
| LOAD_ATTR_METHOD_NO_DICT | 50,243,780 | 12.8% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 302,434,322 | 77.0% |
| LIST_APPEND | 28,850,040 | 7.3% |
| RETURN_VALUE | 11,974,980 | 3.0% |
| LOAD_FAST | 11,021,400 | 2.8% |
| POP_TOP | 9,001,729 | 2.3% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 144,156,363 | 64.0% |
| LOAD_ATTR | 71,924,076 | 31.9% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,435,949 | 3.3% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 301,159 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 71,943,761 | 31.9% |
| POP_JUMP_IF_FALSE | 58,433,400 | 25.9% |
| GET_ITER | 31,836,780 | 14.1% |
| LOAD_GLOBAL_MODULE | 18,632,220 | 8.3% |
| LOAD_FAST | 12,470,700 | 5.5% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,682,443 | 78.9% |
| CALL | 19,487,687 | 9.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.3% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.5% |
| LOAD_ATTR | 3,038,880 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 101,355,311 | 48.0% |
| BINARY_OP | 72,002,140 | 34.1% |
| RETURN_VALUE | 17,285,700 | 8.2% |
| STORE_FAST | 6,937,860 | 3.3% |
| LOAD_FAST | 5,872,740 | 2.8% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,381,500 | 91.9% |
| RETURN_VALUE | 1,727,580 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,800 | 3.3% |
| BINARY_SUBSCR_TUPLE_INT | 30,420 | 0.1% |
| CALL | 25,600 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.9% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 29.0% |
| STORE_FAST | 5,602,140 | 15.0% |
| RETURN_VALUE | 3,244,980 | 8.7% |
| BUILD_LIST | 1,966,480 | 5.3% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,490,760 | 66.7% |
| RETURN_GENERATOR | 5,394,160 | 24.8% |
| LOAD_ATTR_SLOT | 1,098,640 | 5.1% |
| CALL | 436,440 | 2.0% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 65.8% |
| BUILD_TUPLE | 2,891,800 | 13.3% |
| YIELD_VALUE | 2,419,200 | 11.1% |
| STORE_FAST | 641,280 | 3.0% |
| LOAD_GLOBAL_BUILTIN | 571,920 | 2.6% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 323,735,600 | 98.9% |
| LOAD_CONST | 3,615,800 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,836,160 | 87.3% |
| LOAD_GLOBAL_MODULE | 13,598,440 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 9,387,180 | 2.9% |
| LOAD_FAST | 7,472,280 | 2.3% |
| CALL_PY_EXACT_ARGS | 4,477,440 | 1.4% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 955,042,684 | 34.6% |
| LOAD_FAST_LOAD_FAST | 637,415,728 | 23.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 416,610,166 | 15.1% |
| LOAD_GLOBAL_MODULE | 159,068,296 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 109,897,500 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,456,908,688 | 89.1% |
| RETURN_GENERATOR | 140,282,172 | 5.1% |
| COPY_FREE_VARS | 120,097,607 | 4.4% |
| MAKE_CELL | 24,891,932 | 0.9% |
| INSTRUMENTED_RESUME | 14,577,840 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,707,898 | 58.0% |
| LOAD_ATTR_METHOD_NO_DICT | 12,061,720 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,845,321 | 7.8% |
| LOAD_ATTR | 11,184,040 | 7.4% |
| LOAD_SUPER_ATTR_METHOD | 5,951,040 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,717,193 | 96.4% |
| RETURN_GENERATOR | 3,297,720 | 2.2% |
| COPY_FREE_VARS | 1,061,269 | 0.7% |
| MAKE_CELL | 1,008,240 | 0.7% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,692,816 | 93.5% |
| LOAD_GLOBAL_MODULE | 689,760 | 4.1% |
| BUILD_TUPLE | 356,040 | 2.1% |
| LOAD_ATTR_MODULE | 37,355 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,775,971 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 240 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 43,331,040 | 32.1% |
| LOAD_FAST_LOAD_FAST | 32,019,060 | 23.7% |
| LOAD_ATTR | 15,173,607 | 11.2% |
| LOAD_ATTR_SLOT | 13,691,312 | 10.1% |
| LOAD_FAST | 10,752,460 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 69,488,011 | 51.4% |
| POP_JUMP_IF_TRUE | 38,838,504 | 28.7% |
| COPY | 18,630,884 | 13.8% |
| RETURN_VALUE | 7,089,328 | 5.2% |
| EXTENDED_ARG | 756,720 | 0.6% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 65,983,169 | 60.2% |
| BINARY_SUBSCR | 23,382,660 | 21.3% |
| LOAD_CONST | 6,004,560 | 5.5% |
| LOAD_FAST | 6,000,854 | 5.5% |
| LOAD_GLOBAL_MODULE | 3,631,843 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 47,983,349 | 43.8% |
| POP_JUMP_IF_TRUE | 32,445,300 | 29.6% |
| POP_JUMP_IF_FALSE | 29,177,197 | 26.6% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 608,828,089 | 43.7% |
| LOAD_ATTR_INSTANCE_VALUE | 171,816,659 | 12.3% |
| LOAD_FAST | 121,565,420 | 8.7% |
| LOAD_FAST_LOAD_FAST | 118,693,601 | 8.5% |
| COPY | 102,794,040 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,164,327,716 | 83.5% |
| POP_JUMP_IF_TRUE | 120,647,262 | 8.7% |
| RETURN_VALUE | 59,343,329 | 4.3% |
| EXTENDED_ARG | 16,635,600 | 1.2% |
| LOAD_FAST | 15,024,000 | 1.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,560,613,776 | 98.4% |
| LOAD_FAST | 8,529,312 | 0.5% |
| LOAD_GLOBAL_MODULE | 4,789,013 | 0.3% |
| RETURN_VALUE | 4,023,840 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,546,202,334 | 97.5% |
| POP_JUMP_IF_TRUE | 26,991,324 | 1.7% |
| COPY | 6,085,404 | 0.4% |
| RETURN_VALUE | 4,337,871 | 0.3% |
| EXTENDED_ARG | 1,145,940 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,041,440 | 50.1% |
| LOAD_FAST | 508,360,080 | 25.7% |
| LOAD_GLOBAL_MODULE | 301,342,680 | 15.3% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,292,842 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,866,996,229 | 94.5% |
| POP_JUMP_IF_TRUE | 59,611,776 | 3.0% |
| RETURN_VALUE | 25,006,920 | 1.3% |
| COPY | 20,881,380 | 1.1% |
| STORE_FAST | 1,481,820 | 0.1% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,367,300 | 48.6% |
| LOAD_FAST_LOAD_FAST | 36,024,720 | 34.7% |
| LOAD_ATTR | 11,580,660 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,731,420 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,776,280 | 26.0% |
| LOAD_FAST | 226,658,615 | 22.0% |
| LOAD_FAST_LOAD_FAST | 120,895,740 | 11.7% |
| SWAP | 105,748,980 | 10.3% |
| LOAD_CONST | 95,089,500 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,776,280 | 26.0% |
| POP_JUMP_IF_FALSE | 165,003,170 | 16.0% |
| BINARY_SUBSCR_LIST_INT | 157,633,380 | 15.3% |
| BINARY_SUBSCR | 109,564,100 | 10.6% |
| COMPARE_OP_INT | 102,794,040 | 10.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 120,097,607 | 75.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,845,932 | 16.9% |
| CALL | 8,744,807 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,697,992 | 1.1% |
| CALL_PY_WITH_DEFAULTS | 1,061,269 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 172,829,431 | 70.2% |
| RETURN_GENERATOR | 73,398,180 | 29.8% |
| MAKE_CELL | 18,480 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,516,043 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,651,042 | 78.1% |
| NOP | 1,713,800 | 20.1% |
| RETURN_CONST | 150,241 | 1.8% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |


</details>

### DELETE_DEREF

<details>
<summary> Successors and predecessors for DELETE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR | 1,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_FAST | 1,200 | 100.0% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 222,720 | 60.1% |
| CALL | 81,000 | 21.9% |
| POP_EXCEPT | 18,000 | 4.9% |
| STORE_ATTR_INSTANCE_VALUE | 18,000 | 4.9% |
| NOP | 18,000 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 151,020 | 40.8% |
| RETURN_VALUE | 138,600 | 37.4% |
| RETURN_CONST | 36,000 | 9.7% |
| LOAD_FAST | 20,555 | 5.5% |
| JUMP_BACKWARD | 9,540 | 2.6% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,994,140 | 57.5% |
| BUILD_SLICE | 53,340,056 | 42.0% |
| LOAD_FAST | 293,581 | 0.2% |
| LOAD_CONST | 286,740 | 0.2% |
| CALL | 20,641 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,232,176 | 84.5% |
| LOAD_CONST | 18,102,781 | 14.3% |
| JUMP_BACKWARD | 1,038,960 | 0.8% |
| RETURN_CONST | 347,041 | 0.3% |
| LOAD_FAST_LOAD_FAST | 208,140 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,025,740 | 96.6% |
| LOAD_ATTR_INSTANCE_VALUE | 152,040 | 1.6% |
| LOAD_DEREF | 75,760 | 0.8% |
| RETURN_VALUE | 50,880 | 0.5% |
| BUILD_CONST_KEY_MAP | 16,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,346,240 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 13,140 | 100.0% |


</details>

### END_ASYNC_FOR

<details>
<summary> Successors and predecessors for END_ASYNC_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 6,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,999,940 | 100.0% |
| RETURN_CONST | 60 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 56,697,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,100,880 | 33.7% |
| RETURN_CONST | 789,480 | 1.4% |
| LOAD_CONST | 5,280 | 0.0% |
| NOP | 4,980 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,299,236 | 51.7% |
| RETURN_VALUE | 68,993,656 | 35.6% |
| RETURN_CONST | 24,581,816 | 12.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 94,834,196 | 48.9% |
| POP_TOP | 36,145,252 | 18.6% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,880 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 66,872,724 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,872,724 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_FAST | 72,007,560 | 27.3% |
| LOAD_FAST | 44,058,880 | 16.7% |
| JUMP_BACKWARD | 39,530,880 | 15.0% |
| CALL_NO_KW_LIST_APPEND | 27,730,920 | 10.5% |
| COMPARE_OP_INT | 16,635,600 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 102,545,760 | 38.9% |
| JUMP_BACKWARD | 52,276,080 | 19.8% |
| FOR_ITER_LIST | 37,843,240 | 14.3% |
| POP_JUMP_IF_NONE | 36,425,260 | 13.8% |
| FOR_ITER | 16,059,920 | 6.1% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,731,420 | 88.7% |
| LOAD_FAST | 9,631,020 | 8.2% |
| LOAD_ATTR | 1,428,300 | 1.2% |
| RETURN_VALUE | 1,042,680 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,086,200 | 50.5% |
| BUILD_STRING | 51,991,080 | 44.5% |
| LOAD_FAST | 5,841,780 | 5.0% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,920 | 88.9% |
| LOAD_CONST | 240 | 11.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 207,090,386 | 73.5% |
| GET_ITER | 49,628,873 | 17.6% |
| EXTENDED_ARG | 16,059,920 | 5.7% |
| SWAP | 5,813,460 | 2.1% |
| LOAD_FAST | 3,009,260 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 147,923,220 | 52.5% |
| STORE_FAST | 74,823,875 | 26.6% |
| LOAD_FAST | 17,496,238 | 6.2% |
| RETURN_CONST | 14,192,346 | 5.0% |
| PUSH_NULL | 7,954,800 | 2.8% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,710,500 | 62.9% |
| JUMP_BACKWARD | 33,065,160 | 36.7% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,120 | 0.0% |
| SWAP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,761,200 | 63.0% |
| RESUME | 33,378,060 | 37.0% |
| STORE_FAST | 120 | 0.0% |
| RETURN_CONST | 120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 922,952,537 | 74.7% |
| GET_ITER | 188,926,736 | 15.3% |
| LOAD_FAST | 59,095,840 | 4.8% |
| EXTENDED_ARG | 37,843,240 | 3.1% |
| SWAP | 25,911,612 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 585,447,897 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,363,580 | 25.4% |
| RETURN_CONST | 103,265,010 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,495,100 | 6.5% |
| LOAD_FAST | 58,136,940 | 4.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 425,028,487 | 89.1% |
| GET_ITER | 25,466,633 | 5.3% |
| LOAD_FAST | 21,531,120 | 4.5% |
| SWAP | 4,261,260 | 0.9% |
| EXTENDED_ARG | 829,860 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 393,613,832 | 82.5% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.4% |
| RETURN_CONST | 23,855,760 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,295,694 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 290,363,129 | 69.7% |
| GET_ITER | 120,713,571 | 29.0% |
| SWAP | 2,897,440 | 0.7% |
| FOR_ITER_LIST | 1,236,430 | 0.3% |
| LOAD_FAST | 1,121,280 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,485,480 | 68.6% |
| LOAD_FAST | 61,321,500 | 14.7% |
| LOAD_FAST_LOAD_FAST | 43,820,520 | 10.5% |
| RETURN_CONST | 12,222,960 | 2.9% |
| STORE_FAST_LOAD_FAST | 5,055,840 | 1.2% |


</details>

### GET_AITER

<details>
<summary> Successors and predecessors for GET_AITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,999,940 | 100.0% |
| RETURN_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 6,000,000 | 100.0% |


</details>

### GET_ANEXT

<details>
<summary> Successors and predecessors for GET_ANEXT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 94,136,760 | 94.0% |
| GET_AITER | 6,000,000 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100,136,760 | 100.0% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 78,331,692 | 92.6% |
| LOAD_FAST | 3,309,180 | 3.9% |
| RETURN_VALUE | 2,446,800 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 489,656 | 0.6% |
| CALL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,577,928 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 210,251,170 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 77,368,226 | 13.3% |
| CALL_BUILTIN_CLASS | 61,505,213 | 10.6% |
| RETURN_VALUE | 49,965,600 | 8.6% |
| RETURN_GENERATOR | 37,669,200 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 188,926,736 | 32.5% |
| FOR_ITER_TUPLE | 120,713,571 | 20.8% |
| CALL_PY_EXACT_ARGS | 84,799,440 | 14.6% |
| FOR_ITER_GEN | 56,710,500 | 9.8% |
| FOR_ITER | 49,628,873 | 8.5% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 12,000,420 | 79.1% |
| RETURN_GENERATOR | 3,161,760 | 20.8% |
| LOAD_FAST | 7,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,169,260 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 1,400,400 | 75.7% |
| STORE_FAST | 450,480 | 24.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,850,880 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,532,940 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,400,400 | 91.4% |
| STORE_FAST | 131,940 | 8.6% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,350 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,410 | 52.3% |
| NOP | 3,060 | 36.3% |
| INSTRUMENTED_RETURN_CONST | 240 | 2.8% |
| LOAD_CONST | 240 | 2.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 240 | 2.8% |


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,060 | 41.3% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,060 | 41.3% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 870 | 11.7% |
| LIST_APPEND | 300 | 4.0% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,350 | 58.7% |
| LOAD_FAST | 3,060 | 41.3% |


</details>

### INSTRUMENTED_JUMP_FORWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 240 | 80.0% |
| STORE_FAST | 60 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 80.0% |
| LOAD_GLOBAL | 60 | 20.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 14,567,100 | 99.8% |
| LOAD_FAST | 10,140 | 0.1% |
| CALL | 7,320 | 0.1% |
| COMPARE_OP_STR | 7,020 | 0.0% |
| CALL_NO_KW_ISINSTANCE | 5,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,297,080 | 50.0% |
| LOAD_GLOBAL | 7,287,600 | 49.9% |
| LOAD_FAST_LOAD_FAST | 9,420 | 0.1% |
| INSTRUMENTED_RETURN_CONST | 4,740 | 0.0% |
| LOAD_CONST | 240 | 0.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 100.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,420 | 64.3% |
| CALL | 1,230 | 12.3% |
| INSTRUMENTED_RETURN_VALUE | 720 | 7.2% |
| LOAD_ATTR | 540 | 5.4% |
| COPY | 480 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.6% |
| LOAD_GLOBAL | 4,020 | 40.2% |
| INSTRUMENTED_JUMP_BACKWARD | 870 | 8.7% |
| INSTRUMENTED_RETURN_VALUE | 480 | 4.8% |
| LOAD_FAST_LOAD_FAST | 180 | 1.8% |


</details>

### INSTRUMENTED_RESUME

<details>
<summary> Successors and predecessors for INSTRUMENTED_RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,577,840 | 100.0% |
| CALL | 3,300 | 0.0% |
| RESUME | 1,020 | 0.0% |
| INSTRUMENTED_RESUME | 660 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,569,080 | 99.9% |
| LOAD_GLOBAL | 12,000 | 0.1% |
| RESUME | 960 | 0.0% |
| INSTRUMENTED_RESUME | 660 | 0.0% |
| PUSH_NULL | 240 | 0.0% |


</details>

### INSTRUMENTED_RETURN_CONST

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 4,740 | 87.8% |
| POP_TOP | 300 | 5.6% |
| INSTRUMENTED_FOR_ITER | 240 | 4.4% |
| CALL_NO_KW_LIST_APPEND | 60 | 1.1% |
| STORE_GLOBAL | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,800 | 88.9% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 420 | 7.8% |
| POP_TOP | 180 | 3.3% |


</details>

### INSTRUMENTED_RETURN_VALUE

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,288,320 | 50.0% |
| BINARY_OP_ADD_INT | 7,283,520 | 50.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |
| CALL | 960 | 0.0% |
| BINARY_SLICE | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,283,520 | 50.0% |
| BINARY_OP_ADD_INT | 7,283,520 | 50.0% |
| STORE_FAST | 5,340 | 0.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 720 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 450,663,616 | 37.8% |
| RETURN_CONST | 405,799,602 | 34.0% |
| RETURN_VALUE | 317,298,536 | 26.6% |
| RETURN_GENERATOR | 18,089,340 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,104,040 | 49.8% |
| LOAD_FAST_LOAD_FAST | 108,118,500 | 24.9% |
| LOAD_GLOBAL_MODULE | 80,572,422 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 11,341,740 | 2.6% |
| LOAD_CONST | 8,333,680 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 385,735,202 | 88.8% |
| POP_JUMP_IF_TRUE | 38,069,640 | 8.8% |
| RETURN_VALUE | 3,140,700 | 0.7% |
| COPY | 2,904,060 | 0.7% |
| STORE_FAST | 2,551,540 | 0.6% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,359,804 | 28.8% |
| POP_TOP | 653,588,819 | 20.5% |
| POP_JUMP_IF_TRUE | 464,340,637 | 14.6% |
| POP_JUMP_IF_FALSE | 443,213,081 | 13.9% |
| LIST_APPEND | 146,208,436 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 922,952,537 | 28.9% |
| NOP | 717,887,966 | 22.5% |
| FOR_ITER_RANGE | 425,028,487 | 13.3% |
| FOR_ITER_TUPLE | 290,363,129 | 9.1% |
| LOAD_FAST | 279,831,616 | 8.8% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,261,852 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,261,376 | 97.2% |
| SEND | 6,000,476 | 2.8% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 169,935,403 | 41.6% |
| POP_JUMP_IF_FALSE | 98,745,723 | 24.2% |
| POP_TOP | 55,322,264 | 13.5% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.4% |
| POP_JUMP_IF_NONE | 10,513,680 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 161,160,979 | 39.4% |
| LOAD_FAST_LOAD_FAST | 77,215,500 | 18.9% |
| LOAD_CONST | 37,226,375 | 9.1% |
| LOAD_GLOBAL_MODULE | 26,435,981 | 6.5% |
| JUMP_BACKWARD | 26,010,360 | 6.4% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,412,016 | 25.2% |
| LOAD_CONST | 37,709,518 | 22.4% |
| LOAD_FAST_LOAD_FAST | 30,758,821 | 18.2% |
| LOAD_GLOBAL_MODULE | 18,000,780 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,341,260 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 142,949,435 | 84.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,569,680 | 14.6% |
| CALL_BUILTIN_CLASS | 1,051,480 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,850,040 | 19.7% |
| BUILD_TUPLE | 26,458,320 | 18.1% |
| BINARY_OP | 20,606,280 | 14.1% |
| LOAD_FAST | 18,169,800 | 12.4% |
| RETURN_VALUE | 15,032,698 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,208,436 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 37,119,660 | 77.4% |
| LOAD_FAST | 10,129,334 | 21.1% |
| LOAD_CONST | 366,720 | 0.8% |
| RETURN_VALUE | 204,754 | 0.4% |
| LOAD_DEREF | 77,460 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 47,195,440 | 98.4% |
| STORE_FAST | 351,154 | 0.7% |
| LOAD_FAST | 216,094 | 0.5% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.4% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 709,993,110 | 59.0% |
| LOAD_GLOBAL_BUILTIN | 221,907,180 | 18.5% |
| LOAD_GLOBAL_MODULE | 94,870,987 | 7.9% |
| LOAD_ATTR_SLOT | 80,021,380 | 6.7% |
| LOAD_FAST_LOAD_FAST | 43,833,725 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 246,310,060 | 20.5% |
| IS_OP | 216,104,040 | 18.0% |
| STORE_FAST | 171,736,068 | 14.3% |
| LOAD_FAST_LOAD_FAST | 85,902,634 | 7.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 71,924,076 | 6.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,348,704 | 96.5% |
| LOAD_GLOBAL_BUILTIN | 1,768,320 | 1.5% |
| LOAD_FAST | 1,405,940 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 358,500 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,700,000 | 49.5% |
| LOAD_FAST | 21,946,699 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,784,900 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.4% |
| LOAD_FAST_LOAD_FAST | 2,434,260 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,060,514,652 | 85.2% |
| LOAD_FAST_LOAD_FAST | 320,411,244 | 8.9% |
| COPY | 68,648,781 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 50,314,409 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,037,806,695 | 28.9% |
| POP_JUMP_IF_FALSE | 541,710,766 | 15.1% |
| STORE_FAST | 268,378,588 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 182,654,342 | 5.1% |
| RETURN_VALUE | 173,634,729 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 30,424,860 | 62.0% |
| LOAD_FAST | 18,612,456 | 38.0% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,284,648 | 72.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,435,949 | 15.2% |
| LOAD_CONST | 4,823,940 | 9.8% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.5% |
| CALL | 169,379 | 0.3% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 752,255,998 | 57.6% |
| LOAD_ATTR_INSTANCE_VALUE | 182,654,342 | 14.0% |
| LOAD_CONST | 90,768,160 | 7.0% |
| LOAD_GLOBAL_MODULE | 52,835,960 | 4.0% |
| LOAD_ATTR_SLOT | 47,482,696 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 656,765,766 | 50.3% |
| LOAD_CONST | 146,001,580 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 144,156,363 | 11.0% |
| LOAD_FAST_LOAD_FAST | 109,978,485 | 8.4% |
| CALL_PY_EXACT_ARGS | 109,897,500 | 8.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,528,755,641 | 86.1% |
| LOAD_ATTR_INSTANCE_VALUE | 61,471,626 | 3.5% |
| LOAD_ATTR | 45,745,540 | 2.6% |
| LOAD_ATTR_SLOT | 44,399,361 | 2.5% |
| LOAD_ATTR_WITH_HINT | 36,665,626 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 777,688,879 | 43.8% |
| LOAD_FAST_LOAD_FAST | 463,364,295 | 26.1% |
| CALL_PY_EXACT_ARGS | 416,610,166 | 23.5% |
| LOAD_GLOBAL_MODULE | 48,893,984 | 2.8% |
| LOAD_CONST | 46,533,910 | 2.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 311,040,983 | 95.3% |
| LOAD_ATTR_MODULE | 11,591,900 | 3.6% |
| LOAD_ATTR | 1,339,113 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.4% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 110,005,423 | 33.7% |
| LOAD_FAST_LOAD_FAST | 99,654,711 | 30.5% |
| CALL | 26,144,955 | 8.0% |
| CALL_NO_KW_ISINSTANCE | 21,885,180 | 6.7% |
| LOAD_GLOBAL_BUILTIN | 15,320,080 | 4.7% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,730,816 | 83.3% |
| LOAD_ATTR_SLOT | 5,106,870 | 11.0% |
| RETURN_VALUE | 1,251,720 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 931,920 | 2.0% |
| LOAD_FAST_LOAD_FAST | 125,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 40,868,576 | 87.9% |
| POP_JUMP_IF_FALSE | 3,163,680 | 6.8% |
| RETURN_VALUE | 833,141 | 1.8% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.9% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,203,727,666 | 91.3% |
| LOAD_ATTR_SLOT | 40,633,188 | 3.1% |
| COPY | 40,131,480 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 9,558,240 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 304,788,337 | 23.1% |
| POP_JUMP_IF_FALSE | 147,676,532 | 11.2% |
| LOAD_ATTR | 80,021,380 | 6.1% |
| COMPARE_OP_FLOAT | 65,983,169 | 5.0% |
| STORE_FAST | 58,906,076 | 4.5% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 268,048,298 | 79.3% |
| LOAD_ATTR_WITH_HINT | 22,487,880 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 22,336,752 | 6.6% |
| COPY | 12,982,380 | 3.8% |
| LOAD_FAST_LOAD_FAST | 7,816,760 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 82,481,620 | 24.4% |
| STORE_FAST | 42,837,840 | 12.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,665,626 | 10.8% |
| COMPARE_OP_INT | 35,140,620 | 10.4% |
| LOAD_CONST | 28,138,140 | 8.3% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CLOSURE | 1,320 | 100.0% |


</details>

### LOAD_CLOSURE

<details>
<summary> Successors and predecessors for LOAD_CLOSURE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 53,797,740 | 49.1% |
| LOAD_CLOSURE | 30,172,064 | 27.5% |
| STORE_FAST | 19,018,320 | 17.3% |
| POP_JUMP_IF_TRUE | 2,239,560 | 2.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,697,940 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 79,459,304 | 72.5% |
| LOAD_CLOSURE | 30,172,064 | 27.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,950,508,249 | 52.8% |
| LOAD_CONST | 734,071,478 | 7.8% |
| LOAD_FAST_LOAD_FAST | 453,016,101 | 4.8% |
| STORE_FAST | 279,687,070 | 3.0% |
| POP_JUMP_IF_FALSE | 256,770,246 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,763,868,366 | 18.8% |
| COMPARE_OP_STR | 1,560,613,776 | 16.6% |
| LOAD_FAST | 1,022,611,831 | 10.9% |
| LOAD_CONST | 734,071,478 | 7.8% |
| COMPARE_OP_INT | 608,828,089 | 6.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 333,047,509 | 41.3% |
| LOAD_GLOBAL_BUILTIN | 106,629,773 | 13.2% |
| PUSH_NULL | 37,562,081 | 4.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,640 | 3.9% |
| POP_JUMP_IF_NONE | 27,393,360 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,357,362 | 65.6% |
| LOAD_CONST | 69,699,205 | 8.6% |
| LOAD_FAST_LOAD_FAST | 29,692,287 | 3.7% |
| LOAD_DEREF | 23,803,292 | 2.9% |
| CALL_NO_KW_LEN | 20,446,300 | 2.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,326,081,198 | 16.0% |
| POP_JUMP_IF_FALSE | 4,309,272,534 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 2,566,762,946 | 9.5% |
| RESUME | 2,020,155,041 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,037,806,695 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,950,508,249 | 18.3% |
| LOAD_ATTR_INSTANCE_VALUE | 3,060,514,652 | 11.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,528,755,641 | 5.7% |
| LOAD_ATTR_SLOT | 1,203,727,666 | 4.5% |
| LOAD_GLOBAL_BUILTIN | 1,090,023,419 | 4.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 38,884,192 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,784,738 | 23.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,876,032 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,784,738 | 23.3% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,616,680 | 50.9% |
| POP_TOP | 2,052,780 | 28.9% |
| LOAD_GLOBAL_BUILTIN | 421,740 | 5.9% |
| STORE_FAST | 308,040 | 4.3% |
| LOAD_ATTR_METHOD_NO_DICT | 298,440 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 50.4% |
| POP_JUMP_IF_NOT_NONE | 1,506,240 | 21.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 6.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 294,360 | 4.1% |
| LOAD_FAST | 250,680 | 3.5% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,320,658,101 | 16.4% |
| POP_JUMP_IF_FALSE | 1,180,820,184 | 14.7% |
| NOP | 956,612,067 | 11.9% |
| LOAD_FAST_LOAD_FAST | 517,439,611 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 463,364,295 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,436,488,100 | 17.8% |
| CONTAINS_OP | 989,041,440 | 12.3% |
| LOAD_FAST | 722,673,564 | 9.0% |
| CALL_PY_EXACT_ARGS | 637,415,728 | 7.9% |
| LOAD_FAST_LOAD_FAST | 517,439,611 | 6.4% |


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 2,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 1,200 | 46.5% |
| CALL_PY_EXACT_ARGS | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 99.0% |
| STORE_FAST | 18,480 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 6,760 | 0.1% |
| NOP | 4,160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,584 | 99.2% |
| LOAD_GLOBAL_MODULE | 30,526 | 0.4% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 11,940 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,600 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,090,023,419 | 27.0% |
| POP_JUMP_IF_FALSE | 971,100,006 | 24.0% |
| RESUME | 825,765,522 | 20.4% |
| STORE_FAST | 532,907,487 | 13.2% |
| POP_JUMP_IF_NOT_NONE | 96,121,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,566,762,946 | 63.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.8% |
| CALL_NO_KW_ISINSTANCE | 320,906,023 | 7.9% |
| LOAD_ATTR | 221,907,180 | 5.5% |
| LOAD_FAST_LOAD_FAST | 113,015,980 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 858,660,376 | 31.2% |
| STORE_FAST | 412,375,363 | 15.0% |
| RESUME | 323,756,098 | 11.8% |
| POP_JUMP_IF_FALSE | 265,105,242 | 9.6% |
| LOAD_FAST_LOAD_FAST | 113,333,083 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 457,081,672 | 16.6% |
| LOAD_FAST | 432,605,953 | 15.7% |
| CALL_NO_KW_ISINSTANCE | 330,232,649 | 12.0% |
| LOAD_ATTR_MODULE | 311,040,983 | 11.3% |
| CONTAINS_OP | 301,342,680 | 10.9% |


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FROM_DICT_OR_DEREF | 1,200 | 46.5% |
| PUSH_NULL | 1,200 | 46.5% |
| LOAD_NAME | 180 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 100.0% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 1,320 | 84.6% |
| PUSH_NULL | 180 | 11.5% |
| STORE_NAME | 60 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 1,320 | 84.6% |
| LOAD_LOCALS | 180 | 11.5% |
| UNPACK_SEQUENCE_TUPLE | 40 | 2.6% |
| UNPACK_SEQUENCE | 20 | 1.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,160 | 98.3% |
| LOAD_SUPER_ATTR_ATTR | 20 | 1.7% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,296,120 | 100.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,217,540 | 96.6% |
| LOAD_GLOBAL_MODULE | 64,080 | 2.8% |
| LOAD_FAST_LOAD_FAST | 10,200 | 0.4% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,844,321 | 100.0% |
| LOAD_DEREF | 9,000 | 0.0% |
| LOAD_SUPER_ATTR | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,534,629 | 54.9% |
| LOAD_FAST | 36,953,700 | 32.5% |
| CALL_PY_EXACT_ARGS | 6,364,732 | 5.6% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.2% |
| CALL | 1,199,700 | 1.1% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,665,304 | 57.4% |
| CALL_PY_EXACT_ARGS | 24,891,932 | 30.0% |
| CALL_FUNCTION_EX | 4,707,040 | 5.7% |
| CALL | 3,797,580 | 4.6% |
| CALL_PY_WITH_DEFAULTS | 1,008,240 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,665,304 | 57.3% |
| RESUME | 34,861,632 | 41.9% |
| RETURN_GENERATOR | 580,860 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 93,654,313 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 81,659,053 | 87.2% |
| LOAD_FAST | 8,709,900 | 9.3% |
| LOAD_GLOBAL_MODULE | 2,504,360 | 2.7% |
| PUSH_NULL | 289,380 | 0.3% |
| KW_NAMES | 255,120 | 0.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,836,160 | 38.9% |
| RETURN_VALUE | 6,314,400 | 15.5% |
| LOAD_FAST | 5,930,640 | 14.6% |
| JUMP_FORWARD | 4,782,720 | 11.7% |
| STORE_FAST | 4,423,680 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,590,740 | 50.5% |
| JUMP_BACKWARD | 18,945,480 | 46.5% |
| CALL_FUNCTION_EX | 1,211,400 | 3.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 717,887,966 | 48.5% |
| RESUME | 334,548,946 | 22.6% |
| STORE_FAST | 146,366,691 | 9.9% |
| POP_JUMP_IF_FALSE | 80,919,866 | 5.5% |
| NOP | 52,748,947 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 956,612,067 | 64.6% |
| LOAD_FAST | 350,228,962 | 23.7% |
| NOP | 52,748,947 | 3.6% |
| PUSH_NULL | 41,372,672 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 33,850,271 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,775,872 | 57.0% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.9% |
| SWAP | 1,968,600 | 11.5% |
| COPY | 1,669,320 | 9.7% |
| STORE_FAST | 442,055 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,153,707 | 53.4% |
| RETURN_VALUE | 1,911,000 | 11.1% |
| JUMP_FORWARD | 1,715,820 | 10.0% |
| RERAISE | 1,669,320 | 9.7% |
| POP_TOP | 1,383,925 | 8.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 1,866,996,229 | 22.8% |
| COMPARE_OP_STR | 1,546,202,334 | 18.9% |
| COMPARE_OP_INT | 1,164,327,716 | 14.2% |
| LOAD_FAST | 671,217,254 | 8.2% |
| CALL_NO_KW_ISINSTANCE | 645,946,364 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,309,272,534 | 52.6% |
| LOAD_FAST_LOAD_FAST | 1,180,820,184 | 14.4% |
| LOAD_GLOBAL_BUILTIN | 971,100,006 | 11.9% |
| JUMP_BACKWARD | 443,213,081 | 5.4% |
| LOAD_GLOBAL_MODULE | 265,105,242 | 3.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 191,066,773 | 67.6% |
| EXTENDED_ARG | 36,425,260 | 12.9% |
| LOAD_ATTR_SLOT | 25,233,420 | 8.9% |
| LOAD_DEREF | 13,535,820 | 4.8% |
| LOAD_ATTR_INSTANCE_VALUE | 8,205,370 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 127,084,065 | 45.0% |
| PUSH_NULL | 53,440,680 | 18.9% |
| LOAD_DEREF | 27,393,360 | 9.7% |
| JUMP_BACKWARD | 20,268,724 | 7.2% |
| RETURN_CONST | 15,340,652 | 5.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 336,549,732 | 82.4% |
| LOAD_ATTR_INSTANCE_VALUE | 26,883,194 | 6.6% |
| LOAD_ATTR | 17,705,213 | 4.3% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.2% |
| EXTENDED_ARG | 7,189,500 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 146,135,555 | 35.8% |
| LOAD_GLOBAL_BUILTIN | 96,121,300 | 23.5% |
| LOAD_FAST_LOAD_FAST | 57,939,708 | 14.2% |
| LOAD_GLOBAL_MODULE | 35,096,631 | 8.6% |
| NOP | 18,359,272 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 735,426,695 | 51.0% |
| COMPARE_OP_INT | 120,647,262 | 8.4% |
| CALL_NO_KW_ISINSTANCE | 104,095,964 | 7.2% |
| COPY | 79,297,352 | 5.5% |
| CONTAINS_OP | 59,611,776 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 565,611,994 | 39.2% |
| JUMP_BACKWARD | 464,340,637 | 32.2% |
| LOAD_GLOBAL_BUILTIN | 95,111,741 | 6.6% |
| LOAD_CONST | 67,478,941 | 4.7% |
| POP_TOP | 65,856,752 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 544,108,517 | 24.8% |
| RESUME | 471,727,280 | 21.5% |
| CALL_NO_KW_BUILTIN_O | 341,708,546 | 15.6% |
| POP_JUMP_IF_FALSE | 159,364,498 | 7.3% |
| RETURN_VALUE | 113,257,083 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 801,842,092 | 35.2% |
| JUMP_BACKWARD | 653,588,819 | 28.7% |
| RESUME | 238,121,312 | 10.4% |
| RETURN_CONST | 175,568,239 | 7.7% |
| LOAD_FAST_LOAD_FAST | 97,708,154 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,320,500 | 31.1% |
| LOAD_ATTR | 3,246,420 | 19.0% |
| RAISE_VARARGS | 2,296,860 | 13.4% |
| CALL_NO_KW_BUILTIN_FAST | 1,783,220 | 10.4% |
| RERAISE | 1,632,600 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,721,169 | 91.7% |
| LOAD_GLOBAL_MODULE | 1,030,835 | 6.0% |
| LOAD_FAST | 386,940 | 2.3% |
| WITH_EXCEPT_START | 4,320 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 269,624,567 | 36.1% |
| POP_JUMP_IF_FALSE | 91,206,332 | 12.2% |
| POP_TOP | 70,136,855 | 9.4% |
| POP_JUMP_IF_NONE | 53,440,680 | 7.2% |
| NOP | 41,372,672 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 429,407,448 | 57.5% |
| LOAD_FAST_LOAD_FAST | 276,362,253 | 37.0% |
| LOAD_DEREF | 37,562,081 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 3,415,800 | 0.5% |
| LOAD_GLOBAL_MODULE | 107,680 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,491,540 | 43.7% |
| LOAD_ATTR_MODULE | 583,740 | 17.1% |
| LOAD_CONST | 544,200 | 16.0% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 15.9% |
| LOAD_FAST | 150,960 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,296,860 | 67.3% |
| COPY | 963,540 | 28.2% |
| LOAD_CONST | 151,020 | 4.4% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,377,160 | 72.9% |
| POP_EXCEPT | 1,669,320 | 19.1% |
| POP_TOP | 386,940 | 4.4% |
| POP_JUMP_IF_FALSE | 154,860 | 1.8% |
| DELETE_FAST | 151,020 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,632,600 | 68.9% |
| COPY | 697,140 | 29.4% |
| CALL_INTRINSIC_1 | 41,160 | 1.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,456,908,688 | 63.7% |
| POP_TOP | 238,121,312 | 6.2% |
| SEND_GEN | 208,261,376 | 5.4% |
| CALL | 202,931,795 | 5.3% |
| COPY_FREE_VARS | 172,829,431 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,020,155,041 | 41.6% |
| LOAD_GLOBAL_BUILTIN | 825,765,522 | 17.0% |
| POP_TOP | 471,727,280 | 9.7% |
| NOP | 334,548,946 | 6.9% |
| LOAD_GLOBAL_MODULE | 323,756,098 | 6.7% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 252,142,761 | 19.3% |
| STORE_ATTR_SLOT | 245,133,334 | 18.7% |
| POP_TOP | 175,568,239 | 13.4% |
| STORE_ATTR_INSTANCE_VALUE | 173,639,314 | 13.3% |
| RESUME | 122,694,660 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 544,108,517 | 41.6% |
| INTERPRETER_EXIT | 405,799,602 | 31.0% |
| EXIT_INIT_CHECK | 66,872,724 | 5.1% |
| END_FOR | 56,697,960 | 4.3% |
| LOAD_FAST | 52,435,800 | 4.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,282,172 | 63.8% |
| COPY_FREE_VARS | 73,398,180 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,297,720 | 1.5% |
| CALL_FUNCTION_EX | 1,713,800 | 0.8% |
| CALL | 768,180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,331,692 | 32.9% |
| GET_ITER | 37,669,200 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,040 | 13.9% |
| STORE_FAST | 19,529,580 | 8.2% |
| INTERPRETER_EXIT | 18,089,340 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 755,176,577 | 25.9% |
| RETURN_VALUE | 503,937,112 | 17.3% |
| BUILD_TUPLE | 405,102,480 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 173,634,729 | 6.0% |
| BINARY_SUBSCR_DICT | 104,454,097 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600,167,897 | 20.6% |
| RETURN_VALUE | 503,937,112 | 17.3% |
| INTERPRETER_EXIT | 317,298,536 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 258,461,820 | 8.9% |
| LOAD_FAST | 236,367,326 | 8.1% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,299,736 | 94.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,000,476 | 5.3% |
| SEND | 28,140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,299,236 | 89.3% |
| YIELD_VALUE | 6,000,716 | 5.3% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,140 | 0.0% |
| SEND_GEN | 260 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,261,376 | 69.0% |
| LOAD_CONST | 93,584,212 | 31.0% |
| SEND | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,261,376 | 69.0% |
| POP_TOP | 93,584,472 | 31.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 4.0% |
| STORE_FAST_LOAD_FAST | 48,000 | 1.5% |
| LOAD_FAST | 19,440 | 0.6% |
| BINARY_SUBSCR_LIST_INT | 17,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,100,800 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 81,659,053 | 98.9% |
| SET_FUNCTION_ATTRIBUTE | 918,372 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,014,460 | 65.4% |
| LOAD_GLOBAL_BUILTIN | 18,989,160 | 23.0% |
| STORE_FAST | 5,351,821 | 6.5% |
| CALL_PY_EXACT_ARGS | 2,026,800 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 918,372 | 1.1% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 66.7% |
| LOAD_GLOBAL_BUILTIN | 120 | 33.3% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,048,160 | 58.8% |
| LOAD_FAST_LOAD_FAST | 15,234,880 | 28.9% |
| CALL | 5,419,260 | 10.3% |
| SWAP | 946,534 | 1.8% |
| LOAD_ATTR_MODULE | 38,220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,575,967 | 29.5% |
| LOAD_DEREF | 13,446,120 | 25.5% |
| RETURN_CONST | 8,603,220 | 16.3% |
| JUMP_BACKWARD | 5,554,200 | 10.5% |
| LOAD_FAST_LOAD_FAST | 4,677,740 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 348,936,668 | 44.3% |
| LOAD_FAST_LOAD_FAST | 294,955,398 | 37.5% |
| SWAP | 68,648,781 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.4% |
| RETURN_VALUE | 20,943,360 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 282,659,724 | 35.9% |
| RETURN_CONST | 173,639,314 | 22.1% |
| LOAD_FAST_LOAD_FAST | 165,266,860 | 21.0% |
| LOAD_CONST | 65,276,017 | 8.3% |
| NOP | 51,296,768 | 6.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 510,410,284 | 48.6% |
| LOAD_FAST | 497,613,081 | 47.3% |
| SWAP | 40,131,480 | 3.8% |
| STORE_ATTR_SLOT | 2,111,607 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 276,223,493 | 26.3% |
| LOAD_FAST | 251,903,642 | 24.0% |
| RETURN_CONST | 245,133,334 | 23.3% |
| LOAD_CONST | 216,371,545 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 24,862,340 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,035,678 | 51.0% |
| SWAP | 12,982,380 | 24.5% |
| LOAD_FAST_LOAD_FAST | 12,436,500 | 23.5% |
| LOAD_DEREF | 240,940 | 0.5% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,376,340 | 63.0% |
| RETURN_CONST | 6,693,702 | 12.6% |
| JUMP_BACKWARD | 5,313,540 | 10.0% |
| LOAD_CONST | 3,923,460 | 7.4% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.4% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,873,520 | 41.3% |
| STORE_FAST | 19,047,000 | 29.3% |
| LOAD_CONST | 6,734,880 | 10.3% |
| LOAD_FAST | 2,916,480 | 4.5% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,280 | 29.2% |
| LOAD_DEREF | 13,726,020 | 21.1% |
| LOAD_FAST_LOAD_FAST | 13,436,760 | 20.6% |
| LOAD_FAST | 9,422,220 | 14.5% |
| LOAD_CONST | 4,658,340 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,469,036 | 13.0% |
| BINARY_SUBSCR | 970,638,117 | 10.0% |
| STORE_FAST | 709,955,358 | 7.3% |
| RETURN_VALUE | 600,167,897 | 6.2% |
| FOR_ITER_LIST | 585,447,897 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,326,081,198 | 44.7% |
| LOAD_FAST_LOAD_FAST | 1,320,658,101 | 13.6% |
| JUMP_BACKWARD | 918,359,804 | 9.5% |
| STORE_FAST | 709,955,358 | 7.3% |
| LOAD_GLOBAL_BUILTIN | 532,907,487 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,495,100 | 60.6% |
| FOR_ITER_RANGE | 35,405,280 | 26.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,080 | 6.9% |
| FOR_ITER_TUPLE | 5,055,840 | 3.8% |
| FOR_ITER | 2,406,120 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,540 | 22.3% |
| LOAD_FAST | 24,358,500 | 18.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,555,520 | 15.5% |
| POP_JUMP_IF_TRUE | 16,249,020 | 12.2% |
| STORE_ATTR_INSTANCE_VALUE | 9,260,640 | 7.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 362,173,820 | 23.7% |
| UNPACK_SEQUENCE_LIST | 134,209,500 | 8.8% |
| UNPACK_SEQUENCE_TUPLE | 132,500,520 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| LOAD_FAST | 447,248,369 | 29.3% |
| LOAD_FAST_LOAD_FAST | 86,424,476 | 5.7% |
| STORE_FAST | 67,404,000 | 4.4% |
| LOAD_GLOBAL_MODULE | 46,037,160 | 3.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,147,600 | 99.9% |
| RETURN_VALUE | 3,900 | 0.1% |
| LOAD_ATTR | 540 | 0.0% |
| LOAD_FAST | 300 | 0.0% |
| BUILD_MAP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,864,260 | 79.1% |
| LOAD_GLOBAL_MODULE | 1,285,980 | 20.9% |
| LOAD_CONST | 1,920 | 0.0% |
| RETURN_CONST | 120 | 0.0% |
| INSTRUMENTED_RETURN_CONST | 60 | 0.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 1,320 | 27.5% |
| LOAD_CONST | 1,320 | 27.5% |
| LOAD_ATTR | 1,200 | 25.0% |
| IMPORT_NAME | 360 | 7.5% |
| CALL_NO_KW_BUILTIN_FAST | 180 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,680 | 35.0% |
| LOAD_CONST | 1,440 | 30.0% |
| PUSH_NULL | 1,380 | 28.7% |
| LOAD_CLOSURE | 120 | 2.5% |
| STORE_NAME | 120 | 2.5% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,909,260 | 88.3% |
| LOAD_CONST | 13,458,840 | 11.4% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,578,320 | 91.5% |
| RETURN_CONST | 5,855,760 | 5.0% |
| LOAD_FAST_LOAD_FAST | 4,157,040 | 3.5% |
| JUMP_BACKWARD | 39,840 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 2,700 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 109,571,980 | 34.7% |
| LOAD_FAST | 64,708,094 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 18.0% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.2% |
| LOAD_CONST | 27,782,080 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.5% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 33.0% |
| RETURN_CONST | 33,819,480 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,002,980 | 8.6% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 92,272,720 | 47.8% |
| LOAD_FAST | 62,232,083 | 32.3% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.3% |
| RETURN_VALUE | 7,992,040 | 4.1% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,920,520 | 37.8% |
| LOAD_FAST | 64,642,546 | 33.5% |
| JUMP_BACKWARD | 28,272,900 | 14.7% |
| RETURN_CONST | 12,749,760 | 6.6% |
| LOAD_GLOBAL_MODULE | 7,340,700 | 3.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,380 | 52.3% |
| LOAD_FAST | 56,880,860 | 18.9% |
| LOAD_CONST | 26,874,440 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,036,360 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,905,300 | 38.1% |
| JUMP_BACKWARD | 110,064,480 | 36.5% |
| LOAD_FAST_LOAD_FAST | 71,536,320 | 23.7% |
| RETURN_CONST | 4,469,160 | 1.5% |
| LOAD_CONST | 230,760 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.6% |
| BINARY_OP_ADD_FLOAT | 116,255,040 | 12.8% |
| LOAD_FAST | 94,726,554 | 10.5% |
| BINARY_OP_ADD_INT | 78,423,448 | 8.7% |
| BINARY_OP_SUBTRACT_INT | 67,852,580 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.6% |
| STORE_SUBSCR_LIST_INT | 157,633,380 | 17.4% |
| STORE_SUBSCR | 109,571,980 | 12.1% |
| COPY | 105,748,980 | 11.7% |
| STORE_ATTR_INSTANCE_VALUE | 68,648,781 | 7.6% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,544,329 | 84.3% |
| LOAD_ATTR_MODULE | 1,443,388 | 11.5% |
| LOAD_ATTR | 381,756 | 3.1% |
| LOAD_FAST | 122,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 12,501,773 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,898,960 | 89.0% |
| LOAD_FAST_LOAD_FAST | 7,964,640 | 6.6% |
| LOAD_GLOBAL_MODULE | 3,058,560 | 2.5% |
| BINARY_SUBSCR_TUPLE_INT | 1,205,640 | 1.0% |
| CALL_NO_KW_LEN | 668,220 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 79,368,120 | 65.5% |
| BINARY_SUBSCR_LIST_INT | 26,768,580 | 22.1% |
| CALL_PY_EXACT_ARGS | 3,191,160 | 2.6% |
| STORE_SUBSCR | 2,419,140 | 2.0% |
| BINARY_SUBSCR | 2,419,140 | 2.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 24,825,790 | 48.7% |
| LOAD_FAST | 14,123,700 | 27.7% |
| CALL_NO_KW_ISINSTANCE | 7,956,060 | 15.6% |
| BINARY_SUBSCR | 1,513,680 | 3.0% |
| RETURN_VALUE | 1,180,819 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 23,463,000 | 46.0% |
| RETURN_VALUE | 15,180,449 | 29.8% |
| KW_NAMES | 10,514,640 | 20.6% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.5% |
| LOAD_FAST | 555,240 | 1.1% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 218,520 | 99.2% |
| CALL_INTRINSIC_1 | 960 | 0.4% |
| FOR_ITER | 720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 220,200 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 96,120 | 46.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,940 | 32.8% |
| COPY | 19,920 | 9.6% |
| FOR_ITER_LIST | 10,560 | 5.1% |
| LOAD_FAST | 9,120 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 126,600 | 61.2% |
| STORE_FAST | 78,240 | 37.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,420 | 0.7% |
| UNPACK_SEQUENCE | 380 | 0.2% |
| UNPACK_SEQUENCE_TUPLE | 360 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,417,940 | 70.2% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,000,900 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 804,960 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,209,500 | 95.7% |
| STORE_FAST | 6,004,980 | 4.3% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 258,461,820 | 61.6% |
| LOAD_FAST | 102,734,520 | 24.5% |
| BINARY_SUBSCR_DICT | 14,268,900 | 3.4% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 262,754,664 | 62.6% |
| STORE_FAST_STORE_FAST | 132,500,520 | 31.6% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.7% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,363,580 | 52.5% |
| FOR_ITER | 147,923,220 | 24.7% |
| RETURN_VALUE | 84,038,900 | 14.0% |
| LOAD_FAST | 35,322,780 | 5.9% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 362,173,820 | 60.5% |
| STORE_FAST | 214,698,100 | 35.8% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST_LOAD_FAST | 9,187,080 | 1.5% |
| LOAD_FAST | 904,800 | 0.2% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 4,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 4,320 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.5% |
| YIELD_VALUE | 208,261,376 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,080 | 4.5% |
| LOAD_CONST | 26,856,640 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 450,663,616 | 65.1% |
| YIELD_VALUE | 208,261,376 | 30.1% |
| STORE_FAST | 24,701,700 | 3.6% |
| UNPACK_SEQUENCE_TUPLE | 4,808,640 | 0.7% |
| STORE_DEREF | 2,419,200 | 0.3% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2342617317 | 56.2% |
| specialization.deopt |        60040 | 0.0% |
|          hit |   1822790556 | 43.7% |
|         miss |      3183300 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 61,560 | 9.5% |
| Failure | 588,461 | 90.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 304,920 | 51.8% |
| array int | 112,980 | 19.2% |
| other | 76,560 | 13.0% |
| out of range | 40,400 | 6.9% |
| list slice | 25,500 | 4.3% |
| buffer int | 23,741 | 4.0% |
| sequence int | 2,920 | 0.5% |
| code complex parameters | 1,340 | 0.2% |
| buffer slice | 40 | 0.0% |
| tuple slice | 40 | 0.0% |
| string slice | 20 | 0.0% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    315714767 | 39.0% |
| specialization.deopt |           40 | 0.0% |
|          hit |    494451706 | 61.0% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 627 | 0.7% |
| Failure | 83,300 | 99.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.8% |
| dict subclass no override | 17,700 | 21.2% |
| py simple | 13,580 | 16.3% |
| bytearray int | 5,200 | 6.2% |
| out of range | 1,020 | 1.2% |
| other | 120 | 0.1% |
| list slice | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |       204840 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1156251784 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 49,880 | 99.2% |
| Failure | 380 | 0.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 180 | 47.4% |
| iterator | 120 | 31.6% |
| other | 80 | 21.1% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    281601279 | 11.3% |
| specialization.deopt |      2480468 | 0.1% |
|          hit |   2088199035 | 83.5% |
|         miss |    131465038 | 5.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,088 | 96.5% |
| Failure | 90,253 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 22,980 | 25.5% |
| dict items | 17,900 | 19.8% |
| seq iter | 15,120 | 16.8% |
| set | 10,833 | 12.0% |
| other | 7,500 | 8.3% |
| reversed list | 3,580 | 4.0% |
| dict values | 3,380 | 3.7% |
| zip | 3,100 | 3.4% |
| ascii string | 2,680 | 3.0% |
| dict keys | 1,760 | 2.0% |
| itertools | 660 | 0.7% |
| map | 600 | 0.7% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     52739167 | 2.7% |
| specialization.deopt |      3475651 | 0.2% |
|          hit |   1707103526 | 87.8% |
|         miss |    184215562 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,490,498 | 99.0% |
| Failure | 34,600 | 1.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,140 | 49.5% |
| not in dict | 8,020 | 23.2% |
| overriding descriptor | 4,940 | 14.3% |
| not in keys | 920 | 2.7% |
| non object slot | 920 | 2.7% |
| no dict | 800 | 2.3% |
| property | 760 | 2.2% |
| overridden | 640 | 1.8% |
| not managed dict | 340 | 1.0% |
| method | 120 | 0.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1201221343 | 11.9% |
| specialization.deopt |      9043492 | 0.1% |
|          hit |   8391129040 | 83.3% |
|         miss |    479426770 | 4.8% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,091,861 | 86.0% |
| Failure | 1,476,523 | 14.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 643,280 | 43.6% |
| class attr simple | 581,375 | 39.4% |
| metaclass attribute | 98,940 | 6.7% |
| not managed dict | 67,146 | 4.5% |
| method | 51,330 | 3.5% |
| class method obj | 7,000 | 0.5% |
| non object slot | 6,700 | 0.5% |
| class attr descriptor | 5,740 | 0.4% |
| overridden | 5,260 | 0.4% |
| non overriding descriptor | 4,028 | 0.3% |
| mutable class | 2,320 | 0.2% |
| not in keys | 1,680 | 0.1% |
| module attr not found | 1,160 | 0.1% |
| builtin class method | 360 | 0.0% |
| shadowed | 204 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    135037027 | 4.2% |
| specialization.deopt |        23218 | 0.0% |
|          hit |   3088160680 | 95.8% |
|         miss |      1231280 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 26,450 | 20.1% |
| Failure | 105,267 | 79.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 44,146 | 41.9% |
| different types | 24,150 | 22.9% |
| baseobject | 12,880 | 12.2% |
| float long | 8,845 | 8.4% |
| set | 6,620 | 6.3% |
| other | 2,800 | 2.7% |
| bool | 2,326 | 2.2% |
| tuple | 1,640 | 1.6% |
| list | 1,020 | 1.0% |
| bytes | 640 | 0.6% |
| string | 140 | 0.1% |
| long float | 60 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322116 | 0.1% |
| specialization.deopt |          291 | 0.0% |
|          hit |   6795889396 | 99.9% |
|         miss |        19809 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 39,297 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    827903702 | 15.6% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   4455820132 | 83.7% |
|         miss |     37779500 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 715,967 | 39.4% |
| Failure | 1,103,429 | 60.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 578,820 | 52.5% |
| multiply different types | 171,367 | 15.5% |
| add different types | 151,662 | 13.7% |
| floor divide | 32,520 | 2.9% |
| remainder | 31,568 | 2.9% |
| add other | 29,080 | 2.6% |
| and int | 25,309 | 2.3% |
| lshift | 18,620 | 1.7% |
| rshift | 16,540 | 1.5% |
| true divide different types | 14,340 | 1.3% |
| xor | 10,420 | 0.9% |
| true divide float | 6,640 | 0.6% |
| subtract other | 5,440 | 0.5% |
| or | 3,663 | 0.3% |
| power | 3,640 | 0.3% |
| multiply other | 1,940 | 0.2% |
| true divide other | 980 | 0.1% |
| and other | 820 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112299952 | 27.1% |
|          hit |    301845848 | 72.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 0.9% |
| Failure | 28,140 | 99.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 86.9% |
| other | 3,660 | 13.0% |
| list | 40 | 0.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> specialization stats for JUMP_BACKWARD family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
|          hit |    116150741 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,180 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    873805192 | 10.2% |
| specialization.deopt |      2744731 | 0.0% |
|          hit |   7586882155 | 88.2% |
|         miss |    145576086 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,779,747 | 88.4% |
| Failure | 365,010 | 11.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 65,200 | 17.9% |
| kwnames | 51,051 | 14.0% |
| no dict | 50,420 | 13.8% |
| code complex parameters | 48,640 | 13.3% |
| class no vectorcall | 25,488 | 7.0% |
| cfunc varargs keywords | 23,464 | 6.4% |
| meth descr varargs | 21,146 | 5.8% |
| cfunc noargs | 17,500 | 4.8% |
| init not python | 10,360 | 2.8% |
| other | 10,276 | 2.8% |
| class mutable | 7,930 | 2.2% |
| init not simple | 7,800 | 2.1% |
| meth descr varargs keywords | 7,197 | 2.0% |
| cmethod | 3,540 | 1.0% |
| wrong number arguments | 3,520 | 1.0% |
| bound method | 3,363 | 0.9% |
| cfunc varargs | 2,660 | 0.7% |
| method wrapper | 2,450 | 0.7% |
| operator wrapper | 2,025 | 0.6% |
| str | 980 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 92,251,472,241 | 65.5% |
| Not specialized | 10,692,430,228 | 7.6% |
| Specialized | 37,868,731,754 | 26.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,342,617,317 | 38.1% |
| LOAD_ATTR | 1,201,221,343 | 19.5% |
| CALL | 873,805,192 | 14.2% |
| BINARY_OP | 827,903,702 | 13.5% |
| STORE_SUBSCR | 315,714,767 | 5.1% |
| FOR_ITER | 281,601,279 | 4.6% |
| COMPARE_OP | 135,037,027 | 2.2% |
| SEND | 112,299,952 | 1.8% |
| STORE_ATTR | 52,739,167 | 0.9% |
| LOAD_GLOBAL | 7,322,116 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 207,706,286 | 21.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 154,144,702 | 15.6% |
| STORE_ATTR_SLOT | 111,906,216 | 11.4% |
| CALL_PY_EXACT_ARGS | 86,727,212 | 8.8% |
| STORE_ATTR_INSTANCE_VALUE | 69,158,384 | 7.0% |
| FOR_ITER_LIST | 65,827,158 | 6.7% |
| FOR_ITER_TUPLE | 65,586,760 | 6.7% |
| LOAD_ATTR_SLOT | 56,469,101 | 5.7% |
| LOAD_ATTR_METHOD_NO_DICT | 45,381,225 | 4.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,514,030 | 2.7% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,200,218,933 | 23.5% |
| Calls to Python functions inlined | 3,915,714,429 | 76.5% |
| Calls via PyEval_EvalFrame (total) | 1,200,218,933 | 23.5% |
| Calls via PyEval_EvalFrame (vector) | 661,716,437 | 12.9% |
| Calls via PyEval_EvalFrame (generator) | 538,502,496 | 10.5% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 661,711,337 | 12.9% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 188,904,757 | 3.7% |
| Calls via PyEval_EvalFrame (function ex) | 9,424,660 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 112,639,084 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 93,801,004 | 1.8% |
| Frames pushed | 4,252,318,482 | 83.1% |
| Frame objects created | 58,912,718 | 1.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,086,660,287 | 35.3% |
| Frees to freelist | 4,090,578,949 |  |
| Allocations | 7,502,739,100 | 64.7% |
| Allocations to 512 bytes | 7,421,974,791 | 64.0% |
| Allocations to 4 kbytes | 65,742,287 | 0.6% |
| Allocations over 4 kbytes | 15,022,022 | 0.1% |
| Frees | 7,743,278,290 |  |
| New values | 57,249,820 |  |
| Interpreter increfs | 55,063,911,945 | 76.2% |
| Interpreter decrefs | 64,064,835,971 | 77.0% |
| Increfs | 17,158,907,784 | 23.8% |
| Decrefs | 19,129,677,962 | 23.0% |
| Materialize dict (on request) | 3,684,060 | 6.4% |
| Materialize dict (new key) | 57,960 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,965,041,423 |  |
| Method cache misses | 66,934,381 |  |
| Method cache collisions | 72,604,033 |  |
| Method cache dunder hits | 2,153,836,790 |  |
| Method cache dunder misses | 5,708,305 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,265 |


</details>

---
Stats gathered on: 2023-06-21
