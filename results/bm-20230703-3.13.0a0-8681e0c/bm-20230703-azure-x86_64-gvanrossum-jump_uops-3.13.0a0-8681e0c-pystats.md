
# Pystats results

- fork: gvanrossum
- ref: jump-uops
- commit hash: 8681e0c
- commit date: 2023-07-03T18:28:09-07:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 27,187,804,461 | 18.6% | 18.6% |  |
| STORE_FAST | 9,687,803,866 | 6.6% | 25.2% |  |
| LOAD_CONST | 9,393,704,448 | 6.4% | 31.7% |  |
| POP_JUMP_IF_FALSE | 8,218,275,048 | 5.6% | 37.3% |  |
| LOAD_FAST_LOAD_FAST | 8,050,739,646 | 5.5% | 42.8% |  |
| RESUME | 5,057,625,116 | 3.5% | 46.2% |  |
| LOAD_GLOBAL_BUILTIN | 4,042,158,170 | 2.8% | 49.0% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,639,333,720 | 2.5% | 51.5% | 5.7% |
| JUMP_BACKWARD | 3,203,389,094 | 2.2% | 53.7% |  |
| TO_BOOL_BOOL | 3,118,959,326 | 2.1% | 55.8% | 0.0% |
| RETURN_VALUE | 2,916,939,603 | 2.0% | 57.8% |  |
| CALL_PY_EXACT_ARGS | 2,759,036,055 | 1.9% | 59.7% | 3.1% |
| LOAD_GLOBAL_MODULE | 2,754,840,377 | 1.9% | 61.6% | 0.0% |
| BINARY_SUBSCR | 2,343,204,632 | 1.6% | 63.2% |  |
| POP_TOP | 2,315,562,357 | 1.6% | 64.8% |  |
| BINARY_OP_ADD_INT | 2,198,079,414 | 1.5% | 66.3% | 0.0% |
| CONTAINS_OP | 1,974,909,456 | 1.4% | 67.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,776,022,490 | 1.2% | 68.9% | 8.7% |
| COMPARE_OP_STR | 1,586,136,871 | 1.1% | 69.9% | 0.0% |
| STORE_FAST_STORE_FAST | 1,528,586,205 | 1.0% | 71.0% |  |
| NOP | 1,480,173,099 | 1.0% | 72.0% |  |
| POP_JUMP_IF_TRUE | 1,441,721,568 | 1.0% | 73.0% |  |
| COMPARE_OP_INT | 1,393,652,770 | 1.0% | 73.9% | 0.1% |
| RETURN_CONST | 1,319,629,260 | 0.9% | 74.8% |  |
| LOAD_ATTR_SLOT | 1,317,811,267 | 0.9% | 75.7% | 4.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,305,311,322 | 0.9% | 76.6% | 3.5% |
| FOR_ITER_LIST | 1,235,998,006 | 0.8% | 77.5% | 5.3% |
| INTERPRETER_EXIT | 1,203,856,802 | 0.8% | 78.3% |  |
| LOAD_ATTR | 1,203,030,671 | 0.8% | 79.1% |  |
| STORE_ATTR_SLOT | 1,050,947,461 | 0.7% | 79.8% | 10.6% |
| COPY | 1,030,005,554 | 0.7% | 80.6% |  |
| CALL_NO_KW_BUILTIN_FAST | 928,218,743 | 0.6% | 81.2% | 0.0% |
| SWAP | 904,871,384 | 0.6% | 81.8% |  |
| YIELD_VALUE | 880,585,236 | 0.6% | 82.4% |  |
| BINARY_SUBSCR_LIST_INT | 879,300,915 | 0.6% | 83.0% | 0.4% |
| CALL | 874,484,428 | 0.6% | 83.6% |  |
| BINARY_OP | 829,179,327 | 0.6% | 84.2% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,611,302 | 0.6% | 84.7% | 0.8% |
| LOAD_DEREF | 807,170,603 | 0.6% | 85.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 787,444,840 | 0.5% | 85.8% | 8.8% |
| CALL_NO_KW_BUILTIN_O | 781,866,088 | 0.5% | 86.4% | 0.1% |
| CALL_NO_KW_ISINSTANCE | 777,992,360 | 0.5% | 86.9% |  |
| PUSH_NULL | 746,968,482 | 0.5% | 87.4% |  |
| BUILD_TUPLE | 666,889,178 | 0.5% | 87.9% |  |
| BINARY_SUBSCR_DICT | 613,551,040 | 0.4% | 88.3% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 599,009,005 | 0.4% | 88.7% |  |
| GET_ITER | 580,810,926 | 0.4% | 89.1% |  |
| SEND_GEN | 490,118,435 | 0.3% | 89.4% |  |
| FOR_ITER_RANGE | 477,136,350 | 0.3% | 89.8% | 0.0% |
| BINARY_OP_SUBTRACT_INT | 468,262,549 | 0.3% | 90.1% | 0.1% |
| IS_OP | 434,488,236 | 0.3% | 90.4% |  |
| UNPACK_SEQUENCE_TUPLE | 419,571,747 | 0.3% | 90.7% | 0.3% |
| FOR_ITER_TUPLE | 416,507,621 | 0.3% | 90.9% | 15.7% |
| JUMP_FORWARD | 408,753,135 | 0.3% | 91.2% |  |
| POP_JUMP_IF_NOT_NONE | 408,683,320 | 0.3% | 91.5% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 392,996,393 | 0.3% | 91.8% | 1.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 390,534,556 | 0.3% | 92.0% |  |
| BINARY_OP_ADD_FLOAT | 390,249,154 | 0.3% | 92.3% | 1.6% |
| TO_BOOL_NONE | 385,003,449 | 0.3% | 92.6% | 12.1% |
| LOAD_ATTR_WITH_HINT | 337,925,543 | 0.2% | 92.8% | 2.6% |
| CALL_NO_KW_TYPE_1 | 327,453,724 | 0.2% | 93.0% |  |
| LOAD_ATTR_MODULE | 326,480,992 | 0.2% | 93.3% | 0.0% |
| CALL_NO_KW_LEN | 318,787,621 | 0.2% | 93.5% |  |
| STORE_SUBSCR | 315,798,618 | 0.2% | 93.7% |  |
| STORE_SUBSCR_LIST_INT | 301,564,020 | 0.2% | 93.9% | 0.0% |
| BUILD_LIST | 291,906,741 | 0.2% | 94.1% |  |
| EXTENDED_ARG | 288,289,080 | 0.2% | 94.3% |  |
| POP_JUMP_IF_NONE | 282,531,843 | 0.2% | 94.5% |  |
| FOR_ITER | 281,705,473 | 0.2% | 94.7% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,760,753 | 0.2% | 94.9% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 265,876,859 | 0.2% | 95.0% | 3.2% |
| RETURN_GENERATOR | 250,121,318 | 0.2% | 95.2% |  |
| COPY_FREE_VARS | 246,287,374 | 0.2% | 95.4% |  |
| BINARY_SLICE | 243,545,752 | 0.2% | 95.5% |  |
| CALL_NO_KW_LIST_APPEND | 238,181,075 | 0.2% | 95.7% | 0.0% |
| TO_BOOL_INT | 228,268,143 | 0.2% | 95.9% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 225,407,497 | 0.2% | 96.0% | 7.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 211,249,703 | 0.1% | 96.2% | 0.0% |
| END_SEND | 205,874,597 | 0.1% | 96.3% |  |
| TO_BOOL | 198,422,765 | 0.1% | 96.4% |  |
| STORE_SUBSCR_DICT | 192,917,476 | 0.1% | 96.6% |  |
| TO_BOOL_ALWAYS_TRUE | 190,360,327 | 0.1% | 96.7% | 22.9% |
| BINARY_SUBSCR_TUPLE_INT | 186,609,780 | 0.1% | 96.8% |  |
| KW_NAMES | 168,575,513 | 0.1% | 96.9% |  |
| BUILD_SLICE | 158,173,979 | 0.1% | 97.1% |  |
| CALL_PY_WITH_DEFAULTS | 151,256,155 | 0.1% | 97.2% | 3.5% |
| CALL_INTRINSIC_1 | 147,718,453 | 0.1% | 97.3% |  |
| BINARY_SUBSCR_GETITEM | 146,525,147 | 0.1% | 97.4% | 0.0% |
| LIST_APPEND | 146,333,777 | 0.1% | 97.5% |  |
| UNPACK_SEQUENCE_LIST | 140,233,120 | 0.1% | 97.6% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,071,472 | 0.1% | 97.6% | 19.2% |
| COMPARE_OP | 135,188,721 | 0.1% | 97.7% |  |
| STORE_FAST_LOAD_FAST | 132,738,000 | 0.1% | 97.8% |  |
| DELETE_SUBSCR | 126,944,749 | 0.1% | 97.9% |  |
| UNARY_NEGATIVE | 121,209,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 120,596,679 | 0.1% | 98.1% | 1.1% |
| CALL_BUILTIN_CLASS | 119,386,699 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,634,500 | 0.1% | 98.2% |  |
| FORMAT_SIMPLE | 116,927,880 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 113,895,396 | 0.1% | 98.4% |  |
| SEND | 112,328,358 | 0.1% | 98.5% |  |
| TO_BOOL_LIST | 110,689,154 | 0.1% | 98.6% | 1.2% |
| COMPARE_OP_FLOAT | 109,604,978 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,731,420 | 0.1% | 98.7% |  |
| FOR_ITER_GEN | 102,139,620 | 0.1% | 98.8% | 0.0% |
| GET_ANEXT | 100,136,760 | 0.1% | 98.8% |  |
| MAKE_FUNCTION | 93,654,484 | 0.1% | 98.9% |  |
| GET_AWAITABLE | 84,577,937 | 0.1% | 99.0% |  |
| MAKE_CELL | 83,116,454 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 82,577,762 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,790,938 | 0.1% | 99.1% | 0.0% |
| CALL_FUNCTION_EX | 73,863,177 | 0.1% | 99.2% |  |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,606,484 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 67,842,040 | 0.0% | 99.3% |  |
| EXIT_INIT_CHECK | 66,895,864 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 66,629,460 | 0.0% | 99.4% | 3.0% |
| STORE_DEREF | 65,100,060 | 0.0% | 99.4% |  |
| BUILD_STRING | 58,694,340 | 0.0% | 99.5% |  |
| END_FOR | 56,698,080 | 0.0% | 99.5% |  |
| STORE_ATTR_WITH_HINT | 52,984,261 | 0.0% | 99.5% | 5.9% |
| STORE_ATTR | 52,788,619 | 0.0% | 99.6% |  |
| BUILD_MAP | 52,010,944 | 0.0% | 99.6% |  |
| UNARY_NOT | 50,999,459 | 0.0% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 50,685,620 | 0.0% | 99.7% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 49,037,848 | 0.0% | 99.7% | 0.0% |
| LIST_EXTEND | 47,948,417 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 46,531,023 | 0.0% | 99.8% | 11.8% |
| MAP_ADD | 40,747,620 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,417,840 | 0.0% | 99.8% |  |
| GET_YIELD_FROM_ITER | 27,169,140 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 22,732,712 | 0.0% | 99.9% | 7.7% |
| CALL_NO_KW_TUPLE_1 | 21,711,096 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 17,144,609 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,144,609 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,776,632 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 12,542,918 | 0.0% | 99.9% |  |
| DICT_MERGE | 9,346,240 | 0.0% | 99.9% |  |
| RERAISE | 8,743,620 | 0.0% | 100.0% |  |
| DELETE_ATTR | 8,516,025 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,360,878 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,113,304 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,922,580 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 3,745,380 | 0.0% | 100.0% |  |
| BEFORE_WITH | 3,581,231 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,411,420 | 0.0% | 100.0% |  |
| SET_ADD | 3,100,800 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,296,260 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,850,880 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,532,940 | 0.0% | 100.0% |  |
| BUILD_SET | 1,466,520 | 0.0% | 100.0% |  |
| DELETE_FAST | 370,643 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 207,020 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,996 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,436 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,416 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_CONST | 4,950,572,083 | 3.4% | 3.4% |
| STORE_FAST LOAD_FAST | 4,345,281,000 | 3.0% | 6.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,326,051,017 | 3.0% | 9.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,108,736,535 | 2.1% | 11.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,620,708,425 | 1.8% | 13.2% |
| CALL_PY_EXACT_ARGS RESUME | 2,457,262,561 | 1.7% | 14.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,272,783,365 | 1.6% | 16.5% |
| RESUME LOAD_FAST | 2,032,366,448 | 1.4% | 17.9% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,864,289,496 | 1.3% | 19.1% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,763,865,962 | 1.2% | 20.3% |
| LOAD_CONST COMPARE_OP_STR | 1,560,613,768 | 1.1% | 21.4% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,546,177,162 | 1.1% | 22.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,528,908,541 | 1.0% | 23.5% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 1,436,485,400 | 1.0% | 24.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,320,668,936 | 0.9% | 25.4% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,467,839 | 0.9% | 26.3% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,203,728,196 | 0.8% | 27.1% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,180,876,581 | 0.8% | 27.9% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,164,331,876 | 0.8% | 28.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,090,049,857 | 0.7% | 29.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,037,852,320 | 0.7% | 30.2% |
| LOAD_CONST LOAD_FAST | 1,022,648,899 | 0.7% | 30.9% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,041,440 | 0.7% | 31.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 971,100,053 | 0.7% | 32.2% |
| BINARY_SUBSCR STORE_FAST | 970,638,202 | 0.7% | 32.9% |
| NOP LOAD_FAST_LOAD_FAST | 956,612,067 | 0.7% | 33.5% |
| LOAD_FAST LOAD_FAST | 955,763,848 | 0.7% | 34.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 955,183,312 | 0.7% | 34.8% |
| STORE_FAST JUMP_BACKWARD | 930,359,161 | 0.6% | 35.5% |
| JUMP_BACKWARD FOR_ITER_LIST | 922,228,525 | 0.6% | 36.1% |
| BINARY_SUBSCR LOAD_FAST | 878,904,840 | 0.6% | 36.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 858,853,505 | 0.6% | 37.3% |
| RESUME LOAD_GLOBAL_BUILTIN | 825,833,626 | 0.6% | 37.8% |
| POP_TOP LOAD_FAST | 821,799,184 | 0.6% | 38.4% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,096,820 | 0.6% | 39.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 779,468,500 | 0.5% | 39.5% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 765,171,566 | 0.5% | 40.0% |
| LOAD_FAST RETURN_VALUE | 755,310,379 | 0.5% | 40.5% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 752,193,503 | 0.5% | 41.0% |
| LOAD_CONST LOAD_CONST | 734,093,160 | 0.5% | 41.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 722,763,268 | 0.5% | 42.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 718,083,426 | 0.5% | 42.5% |
| JUMP_BACKWARD NOP | 717,888,007 | 0.5% | 43.0% |
| LOAD_FAST TO_BOOL_BOOL | 714,449,593 | 0.5% | 43.5% |
| LOAD_FAST LOAD_ATTR | 710,151,240 | 0.5% | 44.0% |
| STORE_FAST STORE_FAST | 709,959,129 | 0.5% | 44.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 656,892,489 | 0.4% | 44.9% |
| POP_TOP JUMP_BACKWARD | 652,950,708 | 0.4% | 45.4% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 637,454,275 | 0.4% | 45.8% |
| LOAD_CONST COMPARE_OP_INT | 608,823,811 | 0.4% | 46.2% |
| RETURN_VALUE STORE_FAST | 600,293,445 | 0.4% | 46.6% |
| FOR_ITER_LIST STORE_FAST | 585,427,969 | 0.4% | 47.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 567,856,227 | 0.4% | 47.4% |
| RETURN_CONST POP_TOP | 544,207,875 | 0.4% | 47.8% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,014,840 | 0.4% | 48.2% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 536,882,009 | 0.4% | 48.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 532,982,947 | 0.4% | 48.9% |
| LOAD_DEREF LOAD_FAST | 529,407,277 | 0.4% | 49.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 517,474,823 | 0.4% | 49.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 510,410,960 | 0.3% | 50.0% |
| LOAD_FAST CONTAINS_OP | 508,359,240 | 0.3% | 50.3% |
| RETURN_VALUE RETURN_VALUE | 503,981,746 | 0.3% | 50.7% |
| LOAD_FAST STORE_ATTR_SLOT | 497,613,593 | 0.3% | 51.0% |
| RESUME POP_TOP | 483,673,520 | 0.3% | 51.3% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,293,184 | 0.3% | 51.7% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 464,330,151 | 0.3% | 52.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 463,364,464 | 0.3% | 52.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 457,182,114 | 0.3% | 52.6% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 453,011,870 | 0.3% | 52.9% |
| YIELD_VALUE INTERPRETER_EXIT | 450,609,859 | 0.3% | 53.2% |
| STORE_FAST_STORE_FAST LOAD_FAST | 447,250,788 | 0.3% | 53.5% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 442,900,529 | 0.3% | 53.8% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 432,799,740 | 0.3% | 54.4% |
| PUSH_NULL LOAD_FAST | 429,405,534 | 0.3% | 54.7% |
| JUMP_BACKWARD FOR_ITER_RANGE | 425,040,583 | 0.3% | 55.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 416,710,018 | 0.3% | 55.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 412,449,777 | 0.3% | 55.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 406,842,151 | 0.3% | 55.9% |
| RETURN_CONST INTERPRETER_EXIT | 405,808,909 | 0.3% | 56.1% |
| BUILD_TUPLE RETURN_VALUE | 405,100,800 | 0.3% | 56.4% |
| LOAD_CONST STORE_FAST | 400,063,822 | 0.3% | 56.7% |
| FOR_ITER_RANGE STORE_FAST | 393,625,964 | 0.3% | 57.0% |
| RESUME JUMP_BACKWARD_NO_INTERRUPT | 390,534,556 | 0.3% | 57.2% |
| YIELD_VALUE YIELD_VALUE | 384,534,077 | 0.3% | 57.5% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 384,534,077 | 0.3% | 57.8% |
| SEND_GEN RESUME | 384,534,077 | 0.3% | 58.0% |
| IS_OP POP_JUMP_IF_FALSE | 367,788,812 | 0.3% | 58.3% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 362,194,185 | 0.2% | 58.5% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 358,216,555 | 0.2% | 58.8% |
| LOAD_FAST BINARY_SUBSCR | 357,175,920 | 0.2% | 59.0% |
| NOP LOAD_FAST | 350,311,005 | 0.2% | 59.2% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 348,982,691 | 0.2% | 59.5% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,708,549 | 0.2% | 59.7% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 338,318,284 | 0.2% | 60.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 336,560,273 | 0.2% | 60.2% |
| RESUME NOP | 334,584,591 | 0.2% | 60.4% |
| STORE_FAST LOAD_DEREF | 333,047,877 | 0.2% | 60.6% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 330,231,562 | 0.2% | 60.9% |
| RESUME LOAD_GLOBAL_MODULE | 323,932,080 | 0.2% | 61.1% |


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
| RETURN_VALUE | 2,417,292 | 67.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,024,444 | 28.6% |
| LOAD_GLOBAL_MODULE | 70,915 | 2.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,600 | 1.0% |
| CALL | 31,980 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,965,419 | 82.8% |
| STORE_FAST | 614,372 | 17.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 223,310,944 | 26.9% |
| LOAD_FAST | 185,142,425 | 22.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.7% |
| LOAD_FAST_LOAD_FAST | 47,329,420 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,171,820 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 163,958,247 | 19.8% |
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
| LOAD_FAST | 65,139,190 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 115,852,754 | 29.7% |
| LOAD_FAST | 59,481,900 | 15.2% |
| RETURN_VALUE | 31,350,960 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,763,865,962 | 80.2% |
| LOAD_FAST | 234,195,983 | 10.7% |
| LOAD_FAST_LOAD_FAST | 94,378,620 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,467,839 | 57.3% |
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
| LOAD_FAST | 32,034,040 | 47.2% |
| BINARY_SLICE | 15,579,000 | 23.0% |
| LOAD_CONST | 13,011,920 | 19.2% |
| LOAD_ATTR | 2,105,320 | 3.1% |
| BUILD_STRING | 2,011,200 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,139,520 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.5% |
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
| BINARY_OP_ADD_UNICODE | 364,960 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,731,820 | 63.0% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,420 | 8.6% |
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
| LOAD_ATTR_INSTANCE_VALUE | 51,230,999 | 19.3% |
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
| STORE_FAST | 96,397,431 | 35.7% |
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
| LOAD_CONST | 358,216,555 | 76.5% |
| LOAD_FAST | 66,874,540 | 14.3% |
| LOAD_FAST_LOAD_FAST | 30,055,534 | 6.4% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.1% |
| CALL_NO_KW_LEN | 2,724,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,675,400 | 20.0% |
| STORE_FAST | 84,169,456 | 18.0% |
| SWAP | 67,852,473 | 14.5% |
| RETURN_VALUE | 39,931,800 | 8.5% |
| BINARY_OP | 37,165,200 | 7.9% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 136,821,893 | 56.2% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.4% |
| BINARY_OP_ADD_INT | 35,909,760 | 14.7% |
| LOAD_FAST | 24,776,039 | 10.2% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,132,683 | 21.8% |
| GET_ITER | 33,131,560 | 13.6% |
| CALL_PY_EXACT_ARGS | 25,418,520 | 10.4% |
| BUILD_TUPLE | 24,332,520 | 10.0% |
| LOAD_DEREF | 18,985,680 | 7.8% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,436,485,400 | 61.3% |
| LOAD_FAST | 357,175,920 | 15.2% |
| LOAD_CONST | 139,424,854 | 6.0% |
| COPY | 109,564,100 | 4.7% |
| BUILD_SLICE | 104,833,920 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 970,638,202 | 41.4% |
| LOAD_FAST | 878,904,840 | 37.5% |
| LOAD_FAST_LOAD_FAST | 110,147,520 | 4.7% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |
| BINARY_SUBSCR | 48,584,618 | 2.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 205,776,760 | 33.5% |
| LOAD_FAST | 202,378,193 | 33.0% |
| LOAD_FAST_LOAD_FAST | 131,706,060 | 21.5% |
| BINARY_SUBSCR | 41,253,420 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 231,744,567 | 37.8% |
| RETURN_VALUE | 104,460,072 | 17.0% |
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
| LOAD_CONST | 180,391,071 | 20.5% |
| COPY | 157,633,380 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,094,204 | 17.5% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,504,002 | 26.8% |
| LOAD_CONST | 192,235,800 | 21.9% |
| LOAD_FAST | 140,235,840 | 16.0% |
| RETURN_VALUE | 90,397,860 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 146,803,020 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.3% |
| LOAD_FAST_LOAD_FAST | 3,360 | 0.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,660 | 38.6% |
| LOAD_CONST | 24,655,900 | 13.2% |
| LOAD_FAST | 24,038,880 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.4% |
| STORE_FAST | 8,162,440 | 4.4% |


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
| STORE_FAST | 115,895,664 | 39.7% |
| LOAD_ATTR_SLOT | 37,318,413 | 12.8% |
| SWAP | 32,085,851 | 11.0% |
| LOAD_FAST | 25,052,910 | 8.6% |
| RESUME | 17,316,940 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 128,055,445 | 43.9% |
| LOAD_FAST | 83,276,905 | 28.5% |
| SWAP | 32,085,911 | 11.0% |
| CALL | 9,652,180 | 3.3% |
| RETURN_VALUE | 8,829,960 | 3.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,350,200 | 16.1% |
| RESUME | 6,684,504 | 12.9% |
| SWAP | 5,488,800 | 10.6% |
| LOAD_FAST | 5,420,640 | 10.4% |
| POP_JUMP_IF_FALSE | 3,888,600 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,271,372 | 39.0% |
| LOAD_FAST | 16,537,572 | 31.8% |
| SWAP | 5,488,800 | 10.6% |
| CALL_FUNCTION_EX | 3,354,540 | 6.4% |
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
| LOAD_FAST | 744,119 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,920 | 66.3% |
| DELETE_SUBSCR | 53,340,059 | 33.7% |


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
| LOAD_FAST | 198,707,740 | 29.8% |
| LOAD_CONST | 167,388,702 | 25.1% |
| LOAD_FAST_LOAD_FAST | 125,013,843 | 18.7% |
| CALL | 37,728,900 | 5.7% |
| LOAD_GLOBAL_BUILTIN | 28,322,860 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 405,100,800 | 60.7% |
| LOAD_CONST | 81,838,684 | 12.3% |
| CALL_NO_KW_ISINSTANCE | 33,206,480 | 5.0% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.3% |
| LIST_APPEND | 26,458,320 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 254,289,402 | 29.1% |
| KW_NAMES | 142,954,873 | 16.3% |
| LOAD_FAST_LOAD_FAST | 97,141,291 | 11.1% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,660 | 8.2% |
| LOAD_GLOBAL_MODULE | 46,274,856 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 308,233,307 | 35.2% |
| RESUME | 202,943,743 | 23.2% |
| RETURN_VALUE | 46,902,900 | 5.4% |
| POP_TOP | 43,344,700 | 5.0% |
| LOAD_GLOBAL_MODULE | 38,964,962 | 4.5% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,746,073 | 31.0% |
| LOAD_CONST | 23,522,380 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.3% |
| LOAD_FAST_LOAD_FAST | 21,208,091 | 15.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,363,219 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,493,161 | 78.6% |
| COPY_FREE_VARS | 26,845,942 | 19.4% |
| POP_TOP | 2,060,540 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,249 | 0.3% |
| MAKE_CELL | 171,620 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,912,161 | 27.6% |
| CALL_NO_KW_LEN | 23,244,182 | 19.5% |
| LOAD_GLOBAL_BUILTIN | 9,121,860 | 7.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,231,400 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 61,510,707 | 51.5% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.7% |
| STORE_FAST | 11,949,720 | 10.0% |
| LOAD_FAST | 9,360,960 | 7.8% |
| CALL_BUILTIN_CLASS | 4,166,722 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,040 | 43.0% |
| KW_NAMES | 24,569,440 | 32.0% |
| LOAD_FAST | 13,265,960 | 17.3% |
| LOAD_FAST_LOAD_FAST | 2,692,180 | 3.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,011,320 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 40.8% |
| STORE_FAST | 27,834,440 | 36.2% |
| POP_TOP | 11,163,198 | 14.5% |
| RETURN_VALUE | 5,485,000 | 7.1% |
| LOAD_CONST | 322,140 | 0.4% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 41,800,533 | 56.6% |
| LOAD_FAST | 9,792,544 | 13.3% |
| DICT_MERGE | 9,346,240 | 12.7% |
| LOAD_FAST_LOAD_FAST | 5,883,880 | 8.0% |
| BUILD_MAP | 3,354,540 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 44,978,293 | 60.9% |
| STORE_FAST | 8,094,360 | 11.0% |
| RETURN_VALUE | 6,068,004 | 8.2% |
| MAKE_CELL | 4,707,040 | 6.4% |
| LOAD_FAST_LOAD_FAST | 3,815,580 | 5.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 62.3% |
| LIST_EXTEND | 47,193,013 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 63.7% |
| CALL_FUNCTION_EX | 41,800,533 | 28.3% |
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
| LOAD_CONST | 8,584,160 | 37.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,063,100 | 17.9% |
| LOAD_FAST_LOAD_FAST | 740,624 | 3.3% |
| LOAD_ATTR | 258,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,051,584 | 31.0% |
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
| LOAD_GLOBAL_MODULE | 9,502,232 | 13.9% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.1% |
| RETURN_CONST | 7,864,740 | 11.5% |
| BINARY_OP_ADD_FLOAT | 5,100,000 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,185,912 | 95.0% |
| COPY_FREE_VARS | 1,709,712 | 2.5% |
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
| LOAD_CONST | 338,318,284 | 36.4% |
| LOAD_FAST_LOAD_FAST | 71,766,500 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,668,612 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,293,184 | 51.4% |
| STORE_FAST | 310,343,514 | 33.4% |
| POP_TOP | 47,606,907 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 21,993,660 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 536,882,009 | 68.7% |
| LOAD_CONST | 55,890,060 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,626,040 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,708,549 | 43.7% |
| LOAD_CONST | 171,752,802 | 22.0% |
| STORE_FAST | 163,891,301 | 21.0% |
| RETURN_VALUE | 29,118,932 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 330,231,562 | 42.4% |
| LOAD_GLOBAL_BUILTIN | 320,932,698 | 41.3% |
| LOAD_FAST_LOAD_FAST | 61,327,020 | 7.9% |
| BUILD_TUPLE | 33,206,480 | 4.3% |
| LOAD_ATTR_MODULE | 21,884,900 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 765,171,566 | 98.4% |
| COPY | 5,946,000 | 0.8% |
| RETURN_VALUE | 2,214,354 | 0.3% |
| POP_TOP | 1,996,800 | 0.3% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200,467,982 | 62.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,415,399 | 13.3% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.3% |
| LOAD_DEREF | 20,446,300 | 6.4% |
| LOAD_ATTR_SLOT | 8,331,340 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 122,162,593 | 38.3% |
| LOAD_FAST | 43,784,160 | 13.7% |
| STORE_FAST | 38,003,780 | 11.9% |
| COMPARE_OP_INT | 32,501,580 | 10.2% |
| CALL_BUILTIN_CLASS | 23,244,182 | 7.3% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,096,830 | 73.1% |
| BINARY_SUBSCR | 20,171,040 | 8.5% |
| BINARY_SLICE | 18,506,220 | 7.8% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 4,894,440 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,770,975 | 37.7% |
| LOAD_FAST | 72,260,300 | 30.3% |
| EXTENDED_ARG | 27,821,580 | 11.7% |
| RETURN_CONST | 20,553,780 | 8.6% |
| LOAD_CONST | 11,303,760 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 176,845,276 | 45.0% |
| LOAD_CONST | 83,042,300 | 21.1% |
| LOAD_FAST_LOAD_FAST | 56,250,240 | 14.3% |
| LOAD_ATTR_METHOD_NO_DICT | 50,238,380 | 12.8% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 302,444,117 | 77.0% |
| LIST_APPEND | 28,850,040 | 7.3% |
| RETURN_VALUE | 11,993,412 | 3.1% |
| LOAD_FAST | 11,021,400 | 2.8% |
| POP_TOP | 9,030,924 | 2.3% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 144,166,771 | 64.0% |
| LOAD_ATTR | 71,924,079 | 31.9% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,435,988 | 3.3% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 301,159 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 71,944,063 | 31.9% |
| TO_BOOL_BOOL | 59,436,739 | 26.4% |
| GET_ITER | 31,836,120 | 14.1% |
| LOAD_GLOBAL_MODULE | 18,632,220 | 8.3% |
| LOAD_FAST | 12,470,700 | 5.5% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,679,023 | 78.9% |
| CALL | 19,487,650 | 9.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.3% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.5% |
| LOAD_ATTR | 3,038,880 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 101,351,843 | 48.0% |
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
| STORE_FAST | 5,602,200 | 15.0% |
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
| LOAD_ATTR_SLOT | 1,098,596 | 5.1% |
| CALL | 436,440 | 2.0% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 65.8% |
| BUILD_TUPLE | 2,891,756 | 13.3% |
| YIELD_VALUE | 2,419,200 | 11.1% |
| STORE_FAST | 641,280 | 3.0% |
| LOAD_GLOBAL_BUILTIN | 571,920 | 2.6% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 323,818,544 | 98.9% |
| LOAD_CONST | 3,615,800 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,854,592 | 87.3% |
| LOAD_GLOBAL_MODULE | 13,598,440 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 9,387,180 | 2.9% |
| LOAD_FAST | 7,472,280 | 2.3% |
| CALL_PY_EXACT_ARGS | 4,541,952 | 1.4% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 955,183,312 | 34.6% |
| LOAD_FAST_LOAD_FAST | 637,454,275 | 23.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 416,710,018 | 15.1% |
| LOAD_GLOBAL_MODULE | 159,068,299 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 109,897,193 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,457,262,561 | 89.1% |
| RETURN_GENERATOR | 140,282,178 | 5.1% |
| COPY_FREE_VARS | 120,097,633 | 4.4% |
| MAKE_CELL | 24,892,098 | 0.9% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,731,961 | 58.0% |
| LOAD_ATTR_METHOD_NO_DICT | 12,061,720 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,856,987 | 7.8% |
| LOAD_ATTR | 11,184,040 | 7.4% |
| LOAD_SUPER_ATTR_METHOD | 5,951,040 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,752,991 | 96.4% |
| RETURN_GENERATOR | 3,297,720 | 2.2% |
| COPY_FREE_VARS | 1,090,464 | 0.7% |
| MAKE_CELL | 1,008,240 | 0.7% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,693,069 | 93.5% |
| LOAD_GLOBAL_MODULE | 689,760 | 4.1% |
| BUILD_TUPLE | 356,280 | 2.1% |
| LOAD_ATTR_MODULE | 37,523 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,776,632 | 100.0% |


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
| LOAD_CONST | 43,375,794 | 32.1% |
| LOAD_FAST_LOAD_FAST | 32,019,060 | 23.7% |
| LOAD_ATTR | 15,173,607 | 11.2% |
| LOAD_ATTR_SLOT | 13,692,962 | 10.1% |
| LOAD_FAST | 10,752,440 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 69,515,797 | 51.4% |
| POP_JUMP_IF_TRUE | 38,838,506 | 28.7% |
| COPY | 18,631,078 | 13.8% |
| RETURN_VALUE | 7,090,662 | 5.2% |
| EXTENDED_ARG | 771,840 | 0.6% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 65,981,978 | 60.2% |
| BINARY_SUBSCR | 23,382,660 | 21.3% |
| LOAD_CONST | 6,004,560 | 5.5% |
| LOAD_FAST | 6,000,818 | 5.5% |
| LOAD_GLOBAL_MODULE | 3,631,842 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 47,982,158 | 43.8% |
| POP_JUMP_IF_TRUE | 32,445,300 | 29.6% |
| POP_JUMP_IF_FALSE | 29,177,160 | 26.6% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 608,823,811 | 43.7% |
| LOAD_ATTR_INSTANCE_VALUE | 171,828,245 | 12.3% |
| LOAD_FAST | 121,565,140 | 8.7% |
| LOAD_FAST_LOAD_FAST | 118,690,750 | 8.5% |
| COPY | 102,794,040 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,164,331,876 | 83.5% |
| POP_JUMP_IF_TRUE | 120,647,256 | 8.7% |
| RETURN_VALUE | 59,342,510 | 4.3% |
| EXTENDED_ARG | 16,635,600 | 1.2% |
| LOAD_FAST | 15,024,000 | 1.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,560,613,768 | 98.4% |
| LOAD_FAST | 8,528,016 | 0.5% |
| LOAD_GLOBAL_MODULE | 4,794,862 | 0.3% |
| RETURN_VALUE | 4,023,840 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,546,177,162 | 97.5% |
| POP_JUMP_IF_TRUE | 26,991,231 | 1.7% |
| COPY | 6,085,092 | 0.4% |
| RETURN_VALUE | 4,337,486 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,041,440 | 50.1% |
| LOAD_FAST | 508,359,240 | 25.7% |
| LOAD_GLOBAL_MODULE | 301,342,680 | 15.3% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,322,036 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,864,289,496 | 94.4% |
| POP_JUMP_IF_TRUE | 59,676,420 | 3.0% |
| RETURN_VALUE | 25,006,260 | 1.3% |
| COPY | 20,881,380 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


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
| LOAD_FAST | 226,658,676 | 22.0% |
| LOAD_FAST_LOAD_FAST | 120,895,740 | 11.7% |
| SWAP | 105,748,980 | 10.3% |
| LOAD_CONST | 95,089,500 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,776,280 | 26.0% |
| TO_BOOL_BOOL | 213,938,602 | 20.8% |
| BINARY_SUBSCR_LIST_INT | 157,633,380 | 15.3% |
| BINARY_SUBSCR | 109,564,100 | 10.6% |
| COMPARE_OP_INT | 102,794,040 | 10.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 120,097,633 | 75.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,845,942 | 16.9% |
| CALL | 8,744,807 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,709,712 | 1.1% |
| CALL_PY_WITH_DEFAULTS | 1,090,464 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 172,870,714 | 70.2% |
| RETURN_GENERATOR | 73,398,180 | 29.8% |
| MAKE_CELL | 18,480 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,516,025 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,651,030 | 78.1% |
| NOP | 1,713,800 | 20.1% |
| RETURN_CONST | 150,235 | 1.8% |
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
| RERAISE | 151,020 | 40.7% |
| RETURN_VALUE | 138,600 | 37.4% |
| RETURN_CONST | 36,000 | 9.7% |
| LOAD_FAST | 20,723 | 5.6% |
| JUMP_BACKWARD | 9,540 | 2.6% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,994,140 | 57.5% |
| BUILD_SLICE | 53,340,059 | 42.0% |
| LOAD_FAST | 293,575 | 0.2% |
| LOAD_CONST | 286,740 | 0.2% |
| CALL | 20,635 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,232,179 | 84.5% |
| LOAD_CONST | 18,102,775 | 14.3% |
| JUMP_BACKWARD | 1,038,960 | 0.8% |
| RETURN_CONST | 347,035 | 0.3% |
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
| RETURN_CONST | 56,698,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,420 | 64.9% |
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
| SEND | 100,299,239 | 48.7% |
| RETURN_VALUE | 68,993,659 | 33.5% |
| RETURN_CONST | 36,581,699 | 17.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 94,834,199 | 46.1% |
| POP_TOP | 48,145,138 | 23.4% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 14.2% |
| BINARY_OP_ADD_INT | 29,134,080 | 14.2% |
| LOAD_FAST | 3,215,880 | 1.6% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 66,895,864 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,895,864 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 81,581,000 | 28.3% |
| LOAD_FAST | 42,587,000 | 14.8% |
| JUMP_BACKWARD | 40,664,220 | 14.1% |
| CALL_NO_KW_LIST_APPEND | 27,821,580 | 9.7% |
| IS_OP | 18,001,680 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 123,737,320 | 42.9% |
| JUMP_BACKWARD | 53,986,020 | 18.7% |
| FOR_ITER_LIST | 38,689,360 | 13.4% |
| POP_JUMP_IF_NONE | 36,518,860 | 12.7% |
| FOR_ITER | 16,516,640 | 5.7% |


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
| JUMP_BACKWARD | 206,688,137 | 73.4% |
| GET_ITER | 49,587,892 | 17.6% |
| EXTENDED_ARG | 16,516,640 | 5.9% |
| SWAP | 5,813,460 | 2.1% |
| LOAD_FAST | 3,009,260 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 147,920,760 | 52.5% |
| STORE_FAST | 74,841,313 | 26.6% |
| LOAD_FAST | 17,495,989 | 6.2% |
| RETURN_CONST | 14,191,787 | 5.0% |
| PUSH_NULL | 7,954,800 | 2.8% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,710,620 | 55.5% |
| JUMP_BACKWARD | 45,065,160 | 44.1% |
| EXTENDED_ARG | 321,360 | 0.3% |
| LOAD_FAST | 42,120 | 0.0% |
| SWAP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,761,320 | 55.6% |
| RESUME | 45,378,060 | 44.4% |
| STORE_FAST | 120 | 0.0% |
| RETURN_CONST | 120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 922,228,525 | 74.6% |
| GET_ITER | 188,818,410 | 15.3% |
| LOAD_FAST | 59,095,840 | 4.8% |
| EXTENDED_ARG | 38,689,360 | 3.1% |
| SWAP | 25,923,331 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 585,427,969 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,375,530 | 25.4% |
| RETURN_CONST | 103,261,812 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,495,100 | 6.5% |
| LOAD_FAST | 58,162,293 | 4.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 425,040,583 | 89.1% |
| GET_ITER | 25,472,487 | 5.3% |
| LOAD_FAST | 21,531,120 | 4.5% |
| SWAP | 4,261,260 | 0.9% |
| EXTENDED_ARG | 829,860 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 393,625,964 | 82.5% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.4% |
| RETURN_CONST | 23,855,760 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,301,542 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 290,422,505 | 69.7% |
| GET_ITER | 120,729,126 | 29.0% |
| SWAP | 2,896,540 | 0.7% |
| FOR_ITER_LIST | 1,236,371 | 0.3% |
| LOAD_FAST | 1,121,280 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,544,035 | 68.6% |
| LOAD_FAST | 61,318,546 | 14.7% |
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
| RETURN_GENERATOR | 78,331,698 | 92.6% |
| LOAD_FAST | 3,309,180 | 3.9% |
| RETURN_VALUE | 2,446,800 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 489,659 | 0.6% |
| CALL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,577,937 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 210,285,890 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 77,368,229 | 13.3% |
| CALL_BUILTIN_CLASS | 61,510,707 | 10.6% |
| RETURN_VALUE | 49,965,300 | 8.6% |
| RETURN_GENERATOR | 37,669,200 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 188,818,410 | 32.5% |
| FOR_ITER_TUPLE | 120,729,126 | 20.8% |
| CALL_PY_EXACT_ARGS | 84,799,440 | 14.6% |
| FOR_ITER_GEN | 56,710,620 | 9.8% |
| FOR_ITER | 49,587,892 | 8.5% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 24,000,300 | 88.3% |
| RETURN_GENERATOR | 3,161,760 | 11.6% |
| LOAD_FAST | 7,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 27,169,140 | 100.0% |


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
| INSTRUMENTED_JUMP_BACKWARD | 4,356 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,416 | 52.3% |
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
| INSTRUMENTED_POP_JUMP_IF_TRUE | 876 | 11.8% |
| LIST_APPEND | 300 | 4.0% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,356 | 58.7% |
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
| TO_BOOL_BOOL | 13,920 | 0.1% |
| COMPARE_OP_STR | 7,020 | 0.0% |
| TO_BOOL_STR | 6,600 | 0.0% |
| EXTENDED_ARG | 3,300 | 0.0% |

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
| TO_BOOL_BOOL | 5,316 | 53.2% |
| TO_BOOL | 3,060 | 30.6% |
| TO_BOOL_STR | 960 | 9.6% |
| TO_BOOL_NONE | 300 | 3.0% |
| COMPARE_OP_STR | 240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.6% |
| LOAD_GLOBAL | 4,020 | 40.2% |
| INSTRUMENTED_JUMP_BACKWARD | 876 | 8.8% |
| INSTRUMENTED_RETURN_VALUE | 480 | 4.8% |
| LOAD_FAST_LOAD_FAST | 180 | 1.8% |


</details>

### INSTRUMENTED_RESUME

<details>
<summary> Successors and predecessors for INSTRUMENTED_RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,577,900 | 100.0% |
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
| TO_BOOL_BOOL | 400 | 7.4% |
| POP_TOP | 180 | 3.3% |
| TO_BOOL | 20 | 0.4% |


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
| TO_BOOL_BOOL | 1,200 | 0.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 450,609,859 | 37.4% |
| RETURN_CONST | 405,808,909 | 33.7% |
| RETURN_VALUE | 317,348,454 | 26.4% |
| RETURN_GENERATOR | 30,089,340 | 2.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,104,040 | 49.7% |
| LOAD_FAST_LOAD_FAST | 108,118,500 | 24.9% |
| LOAD_GLOBAL_MODULE | 80,710,656 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 11,341,740 | 2.6% |
| LOAD_CONST | 8,333,680 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 367,788,812 | 84.6% |
| POP_JUMP_IF_TRUE | 38,152,584 | 8.8% |
| EXTENDED_ARG | 18,001,680 | 4.1% |
| RETURN_VALUE | 3,140,700 | 0.7% |
| COPY | 2,904,060 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 930,359,161 | 29.0% |
| POP_TOP | 652,950,708 | 20.4% |
| POP_JUMP_IF_TRUE | 464,330,151 | 14.5% |
| POP_JUMP_IF_FALSE | 442,900,529 | 13.8% |
| LIST_APPEND | 146,225,957 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 922,228,525 | 28.8% |
| NOP | 717,888,007 | 22.4% |
| FOR_ITER_RANGE | 425,040,583 | 13.3% |
| FOR_ITER_TUPLE | 290,422,505 | 9.1% |
| LOAD_FAST | 279,836,875 | 8.7% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 390,534,556 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 384,534,077 | 98.5% |
| SEND | 6,000,479 | 1.5% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 169,977,158 | 41.6% |
| POP_JUMP_IF_FALSE | 98,745,526 | 24.2% |
| POP_TOP | 55,321,842 | 13.5% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.4% |
| POP_JUMP_IF_NONE | 10,513,680 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 161,172,589 | 39.4% |
| LOAD_FAST_LOAD_FAST | 77,215,500 | 18.9% |
| LOAD_CONST | 37,226,217 | 9.1% |
| LOAD_GLOBAL_MODULE | 26,454,407 | 6.5% |
| LOAD_GLOBAL_BUILTIN | 25,564,428 | 6.3% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,412,559 | 25.2% |
| LOAD_CONST | 37,709,365 | 22.4% |
| LOAD_FAST_LOAD_FAST | 30,764,429 | 18.2% |
| LOAD_GLOBAL_MODULE | 18,000,780 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,341,260 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 142,954,873 | 84.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,569,440 | 14.6% |
| CALL_BUILTIN_CLASS | 1,051,200 | 0.6% |


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
| RETURN_VALUE | 15,044,348 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,225,957 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 37,119,933 | 77.4% |
| LOAD_FAST | 10,132,482 | 21.1% |
| LOAD_CONST | 366,720 | 0.8% |
| RETURN_VALUE | 210,602 | 0.4% |
| LOAD_DEREF | 77,460 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 47,193,013 | 98.4% |
| STORE_FAST | 357,002 | 0.7% |
| LOAD_FAST | 221,942 | 0.5% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.4% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 710,151,240 | 59.0% |
| LOAD_GLOBAL_BUILTIN | 221,925,612 | 18.4% |
| LOAD_GLOBAL_MODULE | 94,876,457 | 7.9% |
| LOAD_ATTR_SLOT | 80,021,653 | 6.7% |
| LOAD_FAST_LOAD_FAST | 43,939,110 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 246,429,849 | 20.5% |
| IS_OP | 216,104,040 | 18.0% |
| STORE_FAST | 171,736,106 | 14.3% |
| LOAD_FAST_LOAD_FAST | 85,901,162 | 7.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 71,924,079 | 6.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,348,727 | 96.5% |
| LOAD_GLOBAL_BUILTIN | 1,786,752 | 1.5% |
| LOAD_FAST | 1,405,940 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 358,500 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,700,000 | 49.5% |
| LOAD_FAST | 21,946,706 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,784,900 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.4% |
| LOAD_FAST_LOAD_FAST | 2,452,692 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,108,736,535 | 85.4% |
| LOAD_FAST_LOAD_FAST | 320,451,185 | 8.8% |
| COPY | 68,648,838 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 50,314,403 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,037,852,320 | 28.5% |
| TO_BOOL_BOOL | 406,842,151 | 11.2% |
| STORE_FAST | 268,378,659 | 7.4% |
| LOAD_ATTR_METHOD_NO_DICT | 182,707,532 | 5.0% |
| RETURN_VALUE | 173,669,885 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 30,424,860 | 62.0% |
| LOAD_FAST | 18,612,548 | 38.0% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,284,694 | 72.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,435,988 | 15.2% |
| LOAD_CONST | 4,823,940 | 9.8% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.5% |
| CALL | 169,386 | 0.3% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 752,193,503 | 57.6% |
| LOAD_ATTR_INSTANCE_VALUE | 182,707,532 | 14.0% |
| LOAD_CONST | 90,767,560 | 7.0% |
| LOAD_GLOBAL_MODULE | 52,835,960 | 4.0% |
| LOAD_ATTR_SLOT | 47,482,648 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 656,892,489 | 50.3% |
| LOAD_CONST | 145,941,212 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 144,166,771 | 11.0% |
| LOAD_FAST_LOAD_FAST | 109,983,909 | 8.4% |
| CALL_PY_EXACT_ARGS | 109,897,193 | 8.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,528,908,541 | 86.1% |
| LOAD_ATTR_INSTANCE_VALUE | 61,483,557 | 3.5% |
| LOAD_ATTR | 45,745,540 | 2.6% |
| LOAD_ATTR_SLOT | 44,399,530 | 2.5% |
| LOAD_ATTR_WITH_HINT | 36,665,021 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 779,468,500 | 43.9% |
| LOAD_FAST_LOAD_FAST | 463,364,464 | 26.1% |
| CALL_PY_EXACT_ARGS | 416,710,018 | 23.5% |
| LOAD_GLOBAL_MODULE | 48,894,144 | 2.8% |
| LOAD_CONST | 46,533,982 | 2.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 311,080,557 | 95.3% |
| LOAD_ATTR_MODULE | 11,590,180 | 3.6% |
| LOAD_ATTR | 1,339,015 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.4% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 110,011,542 | 33.7% |
| LOAD_FAST_LOAD_FAST | 99,653,200 | 30.5% |
| CALL | 26,156,604 | 8.0% |
| CALL_NO_KW_ISINSTANCE | 21,884,900 | 6.7% |
| LOAD_GLOBAL_BUILTIN | 15,320,040 | 4.7% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,752,555 | 83.3% |
| LOAD_ATTR_SLOT | 5,106,848 | 11.0% |
| RETURN_VALUE | 1,251,720 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 931,920 | 2.0% |
| LOAD_FAST_LOAD_FAST | 125,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 40,891,403 | 87.9% |
| TO_BOOL_NONE | 3,107,760 | 6.7% |
| RETURN_VALUE | 832,052 | 1.8% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.9% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,203,728,196 | 91.3% |
| LOAD_ATTR_SLOT | 40,633,171 | 3.1% |
| COPY | 40,131,480 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 9,558,240 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 305,105,534 | 23.2% |
| TO_BOOL_NONE | 85,430,374 | 6.5% |
| LOAD_ATTR | 80,021,653 | 6.1% |
| TO_BOOL_BOOL | 66,913,420 | 5.1% |
| COMPARE_OP_FLOAT | 65,981,978 | 5.0% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 268,039,794 | 79.3% |
| LOAD_ATTR_WITH_HINT | 22,487,880 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 22,336,749 | 6.6% |
| COPY | 12,982,380 | 3.8% |
| LOAD_FAST_LOAD_FAST | 7,809,620 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 82,481,200 | 24.4% |
| STORE_FAST | 42,837,840 | 12.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,665,021 | 10.9% |
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
| LOAD_FAST | 1,320 | 100.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,950,572,083 | 52.7% |
| LOAD_CONST | 734,093,160 | 7.8% |
| LOAD_FAST_LOAD_FAST | 453,011,870 | 4.8% |
| STORE_FAST | 279,711,453 | 3.0% |
| POP_JUMP_IF_FALSE | 256,773,068 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,763,865,962 | 18.8% |
| COMPARE_OP_STR | 1,560,613,768 | 16.6% |
| LOAD_FAST | 1,022,648,899 | 10.9% |
| LOAD_CONST | 734,093,160 | 7.8% |
| COMPARE_OP_INT | 608,823,811 | 6.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 333,047,877 | 41.3% |
| LOAD_GLOBAL_BUILTIN | 106,670,854 | 13.2% |
| PUSH_NULL | 37,562,081 | 4.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,640 | 3.9% |
| POP_JUMP_IF_NONE | 27,393,360 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,407,277 | 65.6% |
| LOAD_CONST | 69,699,241 | 8.6% |
| LOAD_FAST_LOAD_FAST | 29,692,287 | 3.7% |
| LOAD_DEREF | 23,803,458 | 2.9% |
| CALL_NO_KW_LEN | 20,446,300 | 2.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,345,281,000 | 16.0% |
| POP_JUMP_IF_FALSE | 4,326,051,017 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 2,620,708,425 | 9.6% |
| RESUME | 2,032,366,448 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,037,852,320 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,950,572,083 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 3,108,736,535 | 11.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,528,908,541 | 5.6% |
| LOAD_ATTR_SLOT | 1,203,728,196 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,090,049,857 | 4.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 38,895,011 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,790,609 | 23.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,886,851 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,790,609 | 23.3% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,616,680 | 50.8% |
| POP_TOP | 2,052,780 | 28.9% |
| LOAD_GLOBAL_BUILTIN | 421,740 | 5.9% |
| STORE_FAST | 308,040 | 4.3% |
| LOAD_ATTR_METHOD_NO_DICT | 298,440 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 50.3% |
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
| STORE_FAST | 1,320,668,936 | 16.4% |
| POP_JUMP_IF_FALSE | 1,180,876,581 | 14.7% |
| NOP | 956,612,067 | 11.9% |
| LOAD_FAST_LOAD_FAST | 517,474,823 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 463,364,464 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,436,485,400 | 17.8% |
| CONTAINS_OP | 989,041,440 | 12.3% |
| LOAD_FAST | 722,763,268 | 9.0% |
| CALL_PY_EXACT_ARGS | 637,454,275 | 7.9% |
| LOAD_FAST_LOAD_FAST | 517,474,823 | 6.4% |


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 2,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,200 | 46.5% |
| LOAD_LOCALS | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 99.0% |
| STORE_FAST | 18,352 | 0.2% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 6,720 | 0.1% |
| NOP | 4,140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,584 | 99.2% |
| LOAD_GLOBAL_MODULE | 30,410 | 0.4% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 11,840 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,600 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,090,049,857 | 27.0% |
| POP_JUMP_IF_FALSE | 971,100,053 | 24.0% |
| RESUME | 825,833,626 | 20.4% |
| STORE_FAST | 532,982,947 | 13.2% |
| POP_JUMP_IF_NOT_NONE | 96,121,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,620,708,425 | 64.8% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.8% |
| CALL_NO_KW_ISINSTANCE | 320,932,698 | 7.9% |
| LOAD_ATTR | 221,925,612 | 5.5% |
| LOAD_FAST_LOAD_FAST | 113,013,580 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 858,853,505 | 31.2% |
| STORE_FAST | 412,449,777 | 15.0% |
| RESUME | 323,932,080 | 11.8% |
| POP_JUMP_IF_FALSE | 265,134,360 | 9.6% |
| LOAD_FAST_LOAD_FAST | 113,351,515 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 457,182,114 | 16.6% |
| LOAD_FAST | 432,799,740 | 15.7% |
| CALL_NO_KW_ISINSTANCE | 330,231,562 | 12.0% |
| LOAD_ATTR_MODULE | 311,080,557 | 11.3% |
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
| LOAD_FAST | 113,885,236 | 100.0% |
| LOAD_DEREF | 9,000 | 0.0% |
| LOAD_SUPER_ATTR | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,563,824 | 54.9% |
| LOAD_FAST | 36,953,700 | 32.4% |
| CALL_PY_EXACT_ARGS | 6,376,452 | 5.6% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.2% |
| CALL | 1,199,700 | 1.1% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,665,636 | 57.4% |
| CALL_PY_EXACT_ARGS | 24,892,098 | 30.0% |
| CALL_FUNCTION_EX | 4,707,040 | 5.7% |
| CALL | 3,797,580 | 4.6% |
| CALL_PY_WITH_DEFAULTS | 1,008,240 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,665,636 | 57.3% |
| RESUME | 34,861,798 | 41.9% |
| RETURN_GENERATOR | 580,860 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 93,654,484 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 81,659,224 | 87.2% |
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
| JUMP_BACKWARD | 717,888,007 | 48.5% |
| RESUME | 334,584,591 | 22.6% |
| STORE_FAST | 146,420,851 | 9.9% |
| POP_JUMP_IF_FALSE | 80,966,834 | 5.5% |
| NOP | 52,748,983 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 956,612,067 | 64.6% |
| LOAD_FAST | 350,311,005 | 23.7% |
| NOP | 52,748,983 | 3.6% |
| PUSH_NULL | 41,391,543 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 33,886,008 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,776,244 | 57.0% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.9% |
| SWAP | 1,968,600 | 11.5% |
| COPY | 1,669,320 | 9.7% |
| STORE_FAST | 442,223 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,153,983 | 53.4% |
| RETURN_VALUE | 1,911,000 | 11.1% |
| JUMP_FORWARD | 1,715,820 | 10.0% |
| RERAISE | 1,669,320 | 9.7% |
| POP_TOP | 1,383,961 | 8.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,272,783,365 | 27.7% |
| CONTAINS_OP | 1,864,289,496 | 22.7% |
| COMPARE_OP_STR | 1,546,177,162 | 18.8% |
| COMPARE_OP_INT | 1,164,331,876 | 14.2% |
| IS_OP | 367,788,812 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,326,051,017 | 52.6% |
| LOAD_FAST_LOAD_FAST | 1,180,876,581 | 14.4% |
| LOAD_GLOBAL_BUILTIN | 971,100,053 | 11.8% |
| JUMP_BACKWARD | 442,900,529 | 5.4% |
| LOAD_GLOBAL_MODULE | 265,134,360 | 3.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 191,007,782 | 67.6% |
| EXTENDED_ARG | 36,518,860 | 12.9% |
| LOAD_ATTR_SLOT | 25,233,420 | 8.9% |
| LOAD_DEREF | 13,535,820 | 4.8% |
| LOAD_ATTR_INSTANCE_VALUE | 8,205,380 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 127,082,510 | 45.0% |
| PUSH_NULL | 53,440,680 | 18.9% |
| LOAD_DEREF | 27,393,360 | 9.7% |
| JUMP_BACKWARD | 20,287,165 | 7.2% |
| RETURN_CONST | 15,340,818 | 5.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 336,560,273 | 82.4% |
| LOAD_ATTR_INSTANCE_VALUE | 26,906,470 | 6.6% |
| LOAD_ATTR | 17,728,653 | 4.3% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.2% |
| EXTENDED_ARG | 7,189,900 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 146,152,251 | 35.8% |
| LOAD_GLOBAL_BUILTIN | 96,121,300 | 23.5% |
| LOAD_FAST_LOAD_FAST | 57,939,877 | 14.2% |
| LOAD_GLOBAL_MODULE | 35,096,465 | 8.6% |
| NOP | 18,370,948 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 718,083,426 | 49.8% |
| TO_BOOL | 130,291,345 | 9.0% |
| COMPARE_OP_INT | 120,647,256 | 8.4% |
| TO_BOOL_ALWAYS_TRUE | 82,643,160 | 5.7% |
| TO_BOOL_NONE | 77,264,407 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 567,856,227 | 39.4% |
| JUMP_BACKWARD | 464,330,151 | 32.2% |
| LOAD_GLOBAL_BUILTIN | 95,111,137 | 6.6% |
| LOAD_CONST | 67,478,913 | 4.7% |
| POP_TOP | 65,856,416 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 544,207,875 | 24.4% |
| RESUME | 483,673,520 | 21.7% |
| CALL_NO_KW_BUILTIN_O | 341,708,549 | 15.3% |
| POP_JUMP_IF_FALSE | 159,365,311 | 7.2% |
| RETURN_VALUE | 113,291,833 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 821,799,184 | 35.5% |
| JUMP_BACKWARD | 652,950,708 | 28.2% |
| RESUME | 250,121,318 | 10.8% |
| RETURN_CONST | 179,716,073 | 7.8% |
| LOAD_FAST_LOAD_FAST | 97,708,203 | 4.2% |


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
| LOAD_GLOBAL_BUILTIN | 15,721,626 | 91.7% |
| LOAD_GLOBAL_MODULE | 1,031,003 | 6.0% |
| LOAD_FAST | 386,940 | 2.3% |
| WITH_EXCEPT_START | 4,320 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 269,621,867 | 36.1% |
| POP_JUMP_IF_FALSE | 91,206,246 | 12.2% |
| POP_TOP | 70,137,023 | 9.4% |
| POP_JUMP_IF_NONE | 53,440,680 | 7.2% |
| NOP | 41,391,543 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 429,405,534 | 57.5% |
| LOAD_FAST_LOAD_FAST | 276,380,767 | 37.0% |
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
| CALL_PY_EXACT_ARGS | 2,457,262,561 | 60.6% |
| SEND_GEN | 384,534,077 | 9.5% |
| POP_TOP | 250,121,318 | 6.2% |
| CALL | 202,943,743 | 5.0% |
| COPY_FREE_VARS | 172,870,714 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,032,366,448 | 40.2% |
| LOAD_GLOBAL_BUILTIN | 825,833,626 | 16.3% |
| POP_TOP | 483,673,520 | 9.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 390,534,556 | 7.7% |
| NOP | 334,584,591 | 6.6% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 260,042,184 | 19.7% |
| STORE_ATTR_SLOT | 245,133,503 | 18.6% |
| POP_TOP | 179,716,073 | 13.6% |
| STORE_ATTR_INSTANCE_VALUE | 173,685,764 | 13.2% |
| RESUME | 122,694,660 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 544,207,875 | 41.2% |
| INTERPRETER_EXIT | 405,808,909 | 30.8% |
| EXIT_INIT_CHECK | 66,895,864 | 5.1% |
| END_FOR | 56,698,080 | 4.3% |
| TO_BOOL_BOOL | 56,348,361 | 4.3% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,282,178 | 63.8% |
| COPY_FREE_VARS | 73,398,180 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,297,720 | 1.5% |
| CALL_FUNCTION_EX | 1,713,800 | 0.8% |
| CALL | 768,180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,331,698 | 31.3% |
| GET_ITER | 37,669,200 | 15.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,040 | 13.2% |
| INTERPRETER_EXIT | 30,089,340 | 12.0% |
| STORE_FAST | 19,529,580 | 7.8% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 755,310,379 | 25.9% |
| RETURN_VALUE | 503,981,746 | 17.3% |
| BUILD_TUPLE | 405,100,800 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 173,669,885 | 6.0% |
| BINARY_SUBSCR_DICT | 104,460,072 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600,293,445 | 20.6% |
| RETURN_VALUE | 503,981,746 | 17.3% |
| INTERPRETER_EXIT | 317,348,454 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 258,461,820 | 8.9% |
| TO_BOOL_BOOL | 247,326,753 | 8.5% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,299,739 | 94.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,000,479 | 5.3% |
| SEND | 28,140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,299,239 | 89.3% |
| YIELD_VALUE | 6,000,719 | 5.3% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,140 | 0.0% |
| SEND_GEN | 260 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 384,534,077 | 78.5% |
| LOAD_CONST | 105,584,098 | 21.5% |
| SEND | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 384,534,077 | 78.5% |
| POP_TOP | 105,584,358 | 21.5% |


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
| MAKE_FUNCTION | 81,659,224 | 98.9% |
| SET_FUNCTION_ATTRIBUTE | 918,538 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,014,460 | 65.4% |
| LOAD_GLOBAL_BUILTIN | 18,989,160 | 23.0% |
| STORE_FAST | 5,351,826 | 6.5% |
| CALL_PY_EXACT_ARGS | 2,026,800 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 918,538 | 1.1% |


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
| LOAD_FAST | 31,048,161 | 58.8% |
| LOAD_FAST_LOAD_FAST | 15,234,880 | 28.9% |
| CALL | 5,419,260 | 10.3% |
| SWAP | 946,538 | 1.8% |
| LOAD_ATTR_MODULE | 38,220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,575,968 | 29.5% |
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
| LOAD_FAST | 348,982,691 | 44.3% |
| LOAD_FAST_LOAD_FAST | 294,966,221 | 37.5% |
| SWAP | 68,648,838 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.4% |
| RETURN_VALUE | 20,943,360 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 282,658,694 | 35.9% |
| RETURN_CONST | 173,685,764 | 22.1% |
| LOAD_FAST_LOAD_FAST | 165,266,560 | 21.0% |
| LOAD_CONST | 65,276,180 | 8.3% |
| NOP | 51,296,937 | 6.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 510,410,960 | 48.6% |
| LOAD_FAST | 497,613,593 | 47.3% |
| SWAP | 40,131,480 | 3.8% |
| STORE_ATTR_SLOT | 2,110,988 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 276,224,000 | 26.3% |
| LOAD_FAST | 251,903,548 | 24.0% |
| RETURN_CONST | 245,133,503 | 23.3% |
| LOAD_CONST | 216,371,883 | 20.6% |
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
| LOAD_FAST | 33,616,640 | 63.4% |
| RETURN_CONST | 6,693,701 | 12.6% |
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
| LOAD_FAST | 9,471,160 | 14.5% |
| LOAD_CONST | 4,658,340 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,467,839 | 13.0% |
| BINARY_SUBSCR | 970,638,202 | 10.0% |
| STORE_FAST | 709,959,129 | 7.3% |
| RETURN_VALUE | 600,293,445 | 6.2% |
| FOR_ITER_LIST | 585,427,969 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,345,281,000 | 44.9% |
| LOAD_FAST_LOAD_FAST | 1,320,668,936 | 13.6% |
| JUMP_BACKWARD | 930,359,161 | 9.6% |
| STORE_FAST | 709,959,129 | 7.3% |
| LOAD_GLOBAL_BUILTIN | 532,982,947 | 5.5% |


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
| STORE_ATTR_INSTANCE_VALUE | 9,260,640 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 362,194,185 | 23.7% |
| UNPACK_SEQUENCE_LIST | 134,204,100 | 8.8% |
| UNPACK_SEQUENCE_TUPLE | 132,500,520 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| LOAD_FAST | 447,250,788 | 29.3% |
| LOAD_FAST_LOAD_FAST | 86,432,511 | 5.7% |
| STORE_FAST | 67,404,000 | 4.4% |
| LOAD_GLOBAL_MODULE | 46,036,260 | 3.0% |


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
| LOAD_FAST | 120 | 2.5% |
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
| LOAD_FAST | 64,708,058 | 20.5% |
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
| LOAD_FAST_LOAD_FAST | 92,271,520 | 47.8% |
| LOAD_FAST | 62,231,695 | 32.3% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.3% |
| RETURN_VALUE | 7,992,040 | 4.1% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,920,520 | 37.8% |
| LOAD_FAST | 64,671,616 | 33.5% |
| JUMP_BACKWARD | 28,272,300 | 14.7% |
| RETURN_CONST | 12,749,760 | 6.6% |
| LOAD_GLOBAL_MODULE | 7,340,420 | 3.8% |


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
| JUMP_BACKWARD | 110,064,240 | 36.5% |
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
| LOAD_FAST | 94,732,403 | 10.5% |
| BINARY_OP_ADD_INT | 78,423,615 | 8.7% |
| BINARY_OP_SUBTRACT_INT | 67,852,473 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.6% |
| STORE_SUBSCR_LIST_INT | 157,633,380 | 17.4% |
| STORE_SUBSCR | 109,571,980 | 12.1% |
| COPY | 105,748,980 | 11.7% |
| STORE_ATTR_INSTANCE_VALUE | 68,648,838 | 7.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,698,383 | 82.0% |
| LOAD_ATTR_INSTANCE_VALUE | 23,133,879 | 11.7% |
| LOAD_ATTR | 7,536,128 | 3.8% |
| LOAD_ATTR_SLOT | 2,026,400 | 1.0% |
| COPY | 2,014,840 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 130,291,345 | 65.7% |
| POP_JUMP_IF_FALSE | 67,490,516 | 34.0% |
| TO_BOOL | 230,120 | 0.1% |
| UNARY_NOT | 220,620 | 0.1% |
| TO_BOOL_NONE | 124,924 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,287,775 | 43.8% |
| LOAD_ATTR_INSTANCE_VALUE | 71,719,880 | 37.7% |
| LOAD_ATTR_SLOT | 17,755,080 | 9.3% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.2% |
| COPY | 6,842,256 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 105,973,419 | 55.7% |
| POP_JUMP_IF_TRUE | 82,643,160 | 43.4% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 704,064 | 0.4% |
| TO_BOOL_ALWAYS_TRUE | 116,504 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 765,171,566 | 24.5% |
| LOAD_FAST | 714,449,593 | 22.9% |
| CALL_NO_KW_BUILTIN_FAST | 477,293,184 | 15.3% |
| LOAD_ATTR_INSTANCE_VALUE | 406,842,151 | 13.0% |
| RETURN_VALUE | 247,326,753 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,272,783,365 | 72.9% |
| POP_JUMP_IF_TRUE | 718,083,426 | 23.0% |
| EXTENDED_ARG | 81,581,000 | 2.6% |
| UNARY_NOT | 46,469,039 | 1.5% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,645,281 | 76.9% |
| CALL_NO_KW_BUILTIN_O | 12,835,620 | 5.6% |
| BINARY_OP | 12,594,050 | 5.5% |
| COPY | 7,502,220 | 3.3% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 203,149,903 | 89.0% |
| POP_JUMP_IF_TRUE | 23,900,413 | 10.5% |
| UNARY_NOT | 1,035,540 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,535,612 | 67.3% |
| LOAD_ATTR_INSTANCE_VALUE | 26,971,282 | 24.4% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.6% |
| LOAD_ATTR | 1,779,620 | 1.6% |
| COPY | 814,260 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,623,920 | 55.7% |
| POP_JUMP_IF_FALSE | 45,496,174 | 41.1% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,700 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,199,214 | 43.9% |
| LOAD_ATTR_SLOT | 85,430,374 | 22.2% |
| LOAD_ATTR_INSTANCE_VALUE | 65,218,680 | 16.9% |
| LOAD_ATTR | 21,930,700 | 5.7% |
| RETURN_CONST | 13,912,340 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 305,879,216 | 79.4% |
| POP_JUMP_IF_TRUE | 77,264,407 | 20.1% |
| EXTENDED_ARG | 967,020 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 704,152 | 0.2% |
| TO_BOOL | 123,674 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,564,380 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,424,880 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,220 | 5.8% |
| COPY | 2,668,380 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,708,200 | 53.6% |
| POP_JUMP_IF_TRUE | 30,267,560 | 45.4% |
| UNARY_NOT | 600,240 | 0.9% |
| TO_BOOL_NONE | 36,180 | 0.1% |
| EXTENDED_ARG | 8,280 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,573,524 | 84.3% |
| LOAD_ATTR_MODULE | 1,443,596 | 11.5% |
| LOAD_ATTR | 393,498 | 3.1% |
| LOAD_FAST | 122,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 12,542,918 | 100.0% |


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
| TO_BOOL_BOOL | 46,469,039 | 91.1% |
| TO_BOOL_LIST | 2,640,720 | 5.2% |
| TO_BOOL_INT | 1,035,540 | 2.0% |
| TO_BOOL_STR | 600,240 | 1.2% |
| TO_BOOL | 220,620 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 23,463,000 | 46.0% |
| RETURN_VALUE | 15,186,359 | 29.8% |
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
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 799,560 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,204,100 | 95.7% |
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
| STORE_FAST | 262,754,087 | 62.6% |
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
| FOR_ITER_LIST | 314,375,530 | 52.5% |
| FOR_ITER | 147,920,760 | 24.7% |
| RETURN_VALUE | 84,038,900 | 14.0% |
| LOAD_FAST | 35,322,780 | 5.9% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 362,194,185 | 60.5% |
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
| TO_BOOL_NONE | 4,320 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 384,534,077 | 43.7% |
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 24.0% |
| CALL_INTRINSIC_1 | 94,136,760 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 31,980,360 | 3.6% |
| BINARY_SUBSCR | 30,970,080 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 450,609,859 | 51.2% |
| YIELD_VALUE | 384,534,077 | 43.7% |
| STORE_FAST | 36,701,700 | 4.2% |
| UNPACK_SEQUENCE_TUPLE | 4,808,640 | 0.5% |
| STORE_DEREF | 2,419,200 | 0.3% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    198034621 | 4.6% |
| specialization.deopt |      1805461 | 0.0% |
|          hit |   4004190128 | 93.2% |
|         miss |     95719731 | 2.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,815,711 | 82.8% |
| Failure | 377,894 | 17.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.9% |
| other | 125,880 | 33.3% |
| tuple | 74,420 | 19.7% |
| dict | 14,700 | 3.9% |
| bytes | 10,606 | 2.8% |
| set | 5,820 | 1.5% |
| sequence | 5,455 | 1.4% |
| mapping | 4,273 | 1.1% |
| float | 640 | 0.2% |
| bytearray | 280 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2342614694 | 56.2% |
| specialization.deopt |        60040 | 0.0% |
|          hit |   1822803582 | 43.7% |
|         miss |      3183300 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 61,560 | 9.5% |
| Failure | 588,418 | 90.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 304,920 | 51.8% |
| array int | 112,980 | 19.2% |
| other | 76,520 | 13.0% |
| out of range | 40,400 | 6.9% |
| list slice | 25,500 | 4.3% |
| buffer int | 23,738 | 4.0% |
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
| specialization.deferred |    315714768 | 39.0% |
| specialization.deopt |           40 | 0.0% |
|          hit |    494479276 | 61.0% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 590 | 0.7% |
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
|          hit |   1156266172 | 99.8% |
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
| specialization.deferred |    281614789 | 11.2% |
| specialization.deopt |      2480410 | 0.1% |
|          hit |   2100319564 | 83.6% |
|         miss |    131462033 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,010 | 96.5% |
| Failure | 90,084 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 22,900 | 25.4% |
| dict items | 17,780 | 19.7% |
| seq iter | 15,120 | 16.8% |
| set | 10,904 | 12.1% |
| other | 7,500 | 8.3% |
| reversed list | 3,580 | 4.0% |
| dict values | 3,380 | 3.8% |
| zip | 3,100 | 3.4% |
| ascii string | 2,680 | 3.0% |
| dict keys | 1,780 | 2.0% |
| map | 600 | 0.7% |
| itertools | 600 | 0.7% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     52739169 | 2.7% |
| specialization.deopt |      3475031 | 0.2% |
|          hit |   1707193905 | 87.8% |
|         miss |    184182657 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,489,881 | 99.0% |
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
| specialization.deferred |   1201506742 | 11.9% |
| specialization.deopt |      9043408 | 0.1% |
|          hit |   8439628275 | 83.4% |
|         miss |    479422609 | 4.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,091,388 | 86.0% |
| Failure | 1,475,949 | 14.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 642,940 | 43.6% |
| class attr simple | 581,239 | 39.4% |
| metaclass attribute | 98,884 | 6.7% |
| not managed dict | 67,166 | 4.6% |
| method | 51,269 | 3.5% |
| class method obj | 7,000 | 0.5% |
| non object slot | 6,700 | 0.5% |
| class attr descriptor | 5,740 | 0.4% |
| overridden | 5,260 | 0.4% |
| non overriding descriptor | 4,028 | 0.3% |
| mutable class | 2,320 | 0.2% |
| not in keys | 1,680 | 0.1% |
| module attr not found | 1,160 | 0.1% |
| builtin class method | 360 | 0.0% |
| shadowed | 203 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    135081463 | 4.2% |
| specialization.deopt |        22844 | 0.0% |
|          hit |   3088183198 | 95.8% |
|         miss |      1211421 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 26,059 | 20.0% |
| Failure | 104,043 | 80.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 42,914 | 41.2% |
| different types | 24,145 | 23.2% |
| baseobject | 12,880 | 12.4% |
| float long | 8,846 | 8.5% |
| set | 6,620 | 6.4% |
| other | 2,800 | 2.7% |
| bool | 2,338 | 2.2% |
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
| specialization.deferred |      7322088 | 0.1% |
| specialization.deopt |          266 | 0.0% |
|          hit |   6796980307 | 99.9% |
|         miss |        18240 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 39,056 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    828072694 | 15.6% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   4455825151 | 83.7% |
|         miss |     37779500 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 715,970 | 39.4% |
| Failure | 1,103,463 | 60.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 578,820 | 52.5% |
| multiply different types | 171,368 | 15.5% |
| add different types | 151,662 | 13.7% |
| floor divide | 32,520 | 2.9% |
| remainder | 31,567 | 2.9% |
| add other | 29,080 | 2.6% |
| and int | 25,328 | 2.3% |
| lshift | 18,620 | 1.7% |
| rshift | 16,540 | 1.5% |
| true divide different types | 14,340 | 1.3% |
| xor | 10,420 | 0.9% |
| true divide float | 6,640 | 0.6% |
| subtract other | 5,440 | 0.5% |
| or | 3,678 | 0.3% |
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
| specialization.deferred |    112299958 | 18.6% |
|          hit |    490118435 | 81.4% |

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
|          hit |    116191656 | 100.0% |

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
| specialization.deferred |    874085165 | 10.2% |
| specialization.deopt |      2744674 | 0.0% |
|          hit |   7587532330 | 88.1% |
|         miss |    145572935 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,779,379 | 88.4% |
| Failure | 364,558 | 11.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 65,020 | 17.8% |
| kwnames | 51,112 | 14.0% |
| no dict | 50,420 | 13.8% |
| code complex parameters | 48,625 | 13.3% |
| class no vectorcall | 25,393 | 7.0% |
| cfunc varargs keywords | 23,473 | 6.4% |
| meth descr varargs | 20,908 | 5.7% |
| cfunc noargs | 17,501 | 4.8% |
| init not python | 10,360 | 2.8% |
| other | 10,300 | 2.8% |
| class mutable | 7,937 | 2.2% |
| init not simple | 7,800 | 2.1% |
| meth descr varargs keywords | 7,188 | 2.0% |
| cmethod | 3,540 | 1.0% |
| wrong number arguments | 3,520 | 1.0% |
| bound method | 3,364 | 0.9% |
| cfunc varargs | 2,600 | 0.7% |
| method wrapper | 2,486 | 0.7% |
| operator wrapper | 2,031 | 0.6% |
| str | 980 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 93,037,917,306 | 63.7% |
| Not specialized | 10,999,372,382 | 7.5% |
| Specialized | 42,123,769,369 | 28.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,342,614,694 | 36.9% |
| LOAD_ATTR | 1,201,506,742 | 18.9% |
| CALL | 874,085,165 | 13.8% |
| BINARY_OP | 828,072,694 | 13.0% |
| STORE_SUBSCR | 315,714,768 | 5.0% |
| FOR_ITER | 281,614,789 | 4.4% |
| TO_BOOL | 198,034,621 | 3.1% |
| COMPARE_OP | 135,081,463 | 2.1% |
| SEND | 112,299,958 | 1.8% |
| STORE_ATTR | 52,739,169 | 0.8% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 207,706,290 | 19.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 154,148,926 | 14.3% |
| STORE_ATTR_SLOT | 111,873,315 | 10.3% |
| CALL_PY_EXACT_ARGS | 86,724,031 | 8.0% |
| STORE_ATTR_INSTANCE_VALUE | 69,158,382 | 6.4% |
| FOR_ITER_LIST | 65,828,793 | 6.1% |
| FOR_ITER_TUPLE | 65,582,120 | 6.1% |
| LOAD_ATTR_SLOT | 56,469,837 | 5.2% |
| TO_BOOL_NONE | 46,625,216 | 4.3% |
| LOAD_ATTR_METHOD_NO_DICT | 45,373,216 | 4.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,212,224,407 | 22.7% |
| Calls to Python functions inlined | 4,116,463,947 | 77.3% |
| Calls via PyEval_EvalFrame (total) | 1,212,224,407 | 22.7% |
| Calls via PyEval_EvalFrame (vector) | 673,775,668 | 12.6% |
| Calls via PyEval_EvalFrame (generator) | 538,448,739 | 10.1% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 673,770,568 | 12.6% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 188,903,264 | 3.5% |
| Calls via PyEval_EvalFrame (function ex) | 9,424,660 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 124,649,222 | 2.3% |
| Calls via PyEval_EvalFrame (method) | 93,801,176 | 1.8% |
| Frames pushed | 4,264,877,664 | 80.0% |
| Frame objects created | 58,913,212 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,087,134,650 | 35.2% |
| Frees to freelist | 4,091,021,627 |  |
| Allocations | 7,514,885,713 | 64.8% |
| Allocations to 512 bytes | 7,434,123,702 | 64.1% |
| Allocations to 4 kbytes | 65,741,093 | 0.6% |
| Allocations over 4 kbytes | 15,020,918 | 0.1% |
| Frees | 7,761,512,778 |  |
| New values | 57,249,640 |  |
| Interpreter increfs | 55,199,229,765 | 76.2% |
| Interpreter decrefs | 64,212,676,523 | 77.0% |
| Increfs | 17,219,548,193 | 23.8% |
| Decrefs | 19,199,396,726 | 23.0% |
| Materialize dict (on request) | 3,684,060 | 6.4% |
| Materialize dict (new key) | 57,960 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,964,836,508 |  |
| Method cache misses | 67,316,758 |  |
| Method cache collisions | 72,193,602 |  |
| Method cache dunder hits | 2,166,847,205 |  |
| Method cache dunder misses | 4,916,828 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,265 |


</details>

---
Stats gathered on: 2023-07-04
