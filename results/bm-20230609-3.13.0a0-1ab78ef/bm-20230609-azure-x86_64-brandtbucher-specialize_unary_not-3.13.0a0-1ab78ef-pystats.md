
# Pystats results

- fork: brandtbucher
- ref: specialize-unary-not
- commit hash: 1ab78ef
- commit date: 2023-06-09T13:15:40-07:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 17,883,670,947 | 13.1% | 13.1% |  |
| LOAD_FAST__LOAD_FAST | 7,526,385,379 | 5.5% | 18.7% |  |
| STORE_FAST__LOAD_FAST | 5,775,422,225 | 4.2% | 22.9% |  |
| POP_JUMP_IF_TRUE | 5,618,215,231 | 4.1% | 27.0% |  |
| RESUME | 5,082,713,498 | 3.7% | 30.8% |  |
| LOAD_CONST | 4,685,213,895 | 3.4% | 34.2% |  |
| POP_JUMP_IF_FALSE | 4,085,253,240 | 3.0% | 37.2% |  |
| LOAD_GLOBAL_BUILTIN | 4,052,064,921 | 3.0% | 40.2% | 0.0% |
| LOAD_FAST__LOAD_CONST | 3,709,357,826 | 2.7% | 42.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 3,697,235,897 | 2.7% | 45.6% | 6.3% |
| JUMP_BACKWARD | 3,209,143,789 | 2.4% | 48.0% |  |
| UNARY_NOT_BOOL | 3,165,820,141 | 2.3% | 50.3% | 0.0% |
| STORE_FAST | 3,115,142,587 | 2.3% | 52.6% |  |
| RETURN_VALUE | 2,873,235,016 | 2.1% | 54.7% |  |
| CALL_PY_EXACT_ARGS | 2,788,063,911 | 2.0% | 56.8% | 3.2% |
| LOAD_GLOBAL_MODULE | 2,766,879,914 | 2.0% | 58.8% | 0.0% |
| BINARY_SUBSCR | 2,343,160,519 | 1.7% | 60.5% |  |
| POP_TOP | 2,327,882,778 | 1.7% | 62.3% |  |
| BINARY_OP_ADD_INT | 2,201,683,542 | 1.6% | 63.9% | 0.0% |
| STORE_FAST__STORE_FAST | 2,002,329,532 | 1.5% | 65.3% |  |
| CONTAINS_OP | 1,974,424,073 | 1.5% | 66.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,801,760,982 | 1.3% | 68.1% | 9.3% |
| COMPARE_OP_STR | 1,585,988,318 | 1.2% | 69.3% | 0.0% |
| NOP | 1,476,540,368 | 1.1% | 70.4% |  |
| COMPARE_OP_INT | 1,401,964,064 | 1.0% | 71.4% | 0.1% |
| RETURN_CONST | 1,321,268,871 | 1.0% | 72.4% |  |
| LOAD_ATTR_SLOT | 1,316,805,512 | 1.0% | 73.3% | 4.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,302,831,883 | 1.0% | 74.3% | 3.5% |
| INTERPRETER_EXIT | 1,269,482,560 | 0.9% | 75.2% |  |
| FOR_ITER_LIST | 1,234,355,015 | 0.9% | 76.1% | 5.3% |
| LOAD_ATTR | 1,199,983,963 | 0.9% | 77.0% |  |
| COPY | 1,052,215,830 | 0.8% | 77.8% |  |
| STORE_ATTR_SLOT | 1,049,600,660 | 0.8% | 78.6% | 10.7% |
| LOAD_CONST__LOAD_FAST | 1,020,338,110 | 0.7% | 79.3% |  |
| CALL | 940,450,273 | 0.7% | 80.0% |  |
| CALL_NO_KW_BUILTIN_FAST | 927,701,584 | 0.7% | 80.7% | 0.0% |
| SWAP | 907,489,224 | 0.7% | 81.3% |  |
| BINARY_SUBSCR_LIST_INT | 883,651,728 | 0.6% | 82.0% | 0.4% |
| YIELD_VALUE | 880,842,036 | 0.6% | 82.6% |  |
| BINARY_OP | 828,330,764 | 0.6% | 83.3% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,599,486 | 0.6% | 83.9% | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 812,760,343 | 0.6% | 84.5% | 9.2% |
| LOAD_DEREF | 810,421,107 | 0.6% | 85.1% |  |
| CALL_NO_KW_ISINSTANCE | 781,800,252 | 0.6% | 85.6% |  |
| CALL_NO_KW_BUILTIN_O | 778,637,117 | 0.6% | 86.2% | 0.1% |
| PUSH_NULL | 745,775,946 | 0.5% | 86.8% |  |
| BUILD_TUPLE | 666,240,566 | 0.5% | 87.2% |  |
| BINARY_SUBSCR_DICT | 613,618,267 | 0.5% | 87.7% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 598,577,844 | 0.4% | 88.1% |  |
| GET_ITER | 580,503,527 | 0.4% | 88.6% |  |
| SEND_GEN | 490,119,932 | 0.4% | 88.9% |  |
| FOR_ITER_RANGE | 477,545,646 | 0.4% | 89.3% | 0.0% |
| BINARY_OP_SUBTRACT_INT | 469,333,316 | 0.3% | 89.6% | 0.1% |
| IS_OP | 432,848,069 | 0.3% | 89.9% |  |
| UNPACK_SEQUENCE_TUPLE | 419,524,327 | 0.3% | 90.2% | 0.3% |
| POP_JUMP_IF_NOT_NONE | 418,959,406 | 0.3% | 90.5% |  |
| FOR_ITER_TUPLE | 416,523,242 | 0.3% | 90.9% | 15.7% |
| JUMP_FORWARD | 412,411,235 | 0.3% | 91.2% |  |
| UNARY_NOT_NONE | 408,164,771 | 0.3% | 91.5% | 13.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 391,010,135 | 0.3% | 91.7% | 1.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 390,536,056 | 0.3% | 92.0% |  |
| BINARY_OP_ADD_FLOAT | 390,152,672 | 0.3% | 92.3% | 1.6% |
| UNARY_NOT | 366,964,742 | 0.3% | 92.6% |  |
| LOAD_ATTR_WITH_HINT | 338,178,054 | 0.2% | 92.8% | 2.7% |
| CALL_NO_KW_TYPE_1 | 327,635,548 | 0.2% | 93.1% |  |
| CALL_NO_KW_LEN | 322,568,643 | 0.2% | 93.3% |  |
| LOAD_ATTR_MODULE | 322,235,663 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR | 315,796,981 | 0.2% | 93.8% |  |
| STORE_SUBSCR_LIST_INT | 302,122,860 | 0.2% | 94.0% | 0.0% |
| EXTENDED_ARG | 299,502,660 | 0.2% | 94.2% |  |
| BUILD_LIST | 291,336,947 | 0.2% | 94.4% |  |
| POP_JUMP_IF_NONE | 289,666,958 | 0.2% | 94.7% |  |
| FOR_ITER | 281,659,617 | 0.2% | 94.9% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,664,263 | 0.2% | 95.1% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 265,876,856 | 0.2% | 95.3% | 3.2% |
| RETURN_GENERATOR | 250,364,372 | 0.2% | 95.4% |  |
| COPY_FREE_VARS | 249,536,641 | 0.2% | 95.6% |  |
| BINARY_SLICE | 243,550,410 | 0.2% | 95.8% |  |
| CALL_NO_KW_LIST_APPEND | 238,091,872 | 0.2% | 96.0% | 0.0% |
| UNARY_NOT_INT | 226,284,260 | 0.2% | 96.1% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 225,106,102 | 0.2% | 96.3% | 7.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 211,150,773 | 0.2% | 96.5% | 0.0% |
| END_SEND | 205,874,588 | 0.2% | 96.6% |  |
| STORE_SUBSCR_DICT | 192,434,572 | 0.1% | 96.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 186,611,280 | 0.1% | 96.9% |  |
| KW_NAMES | 168,472,256 | 0.1% | 97.0% |  |
| BUILD_SLICE | 158,173,976 | 0.1% | 97.1% |  |
| CALL_PY_WITH_DEFAULTS | 150,370,000 | 0.1% | 97.2% | 3.5% |
| CALL_INTRINSIC_1 | 147,721,737 | 0.1% | 97.4% |  |
| BINARY_SUBSCR_GETITEM | 146,525,152 | 0.1% | 97.5% | 0.0% |
| LIST_APPEND | 146,034,728 | 0.1% | 97.6% |  |
| UNPACK_SEQUENCE_LIST | 140,238,520 | 0.1% | 97.7% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,029,210 | 0.1% | 97.8% | 19.2% |
| COMPARE_OP | 134,970,339 | 0.1% | 97.9% |  |
| DELETE_SUBSCR | 126,942,352 | 0.1% | 98.0% |  |
| UNARY_NEGATIVE | 121,209,060 | 0.1% | 98.1% |  |
| LOAD_ATTR_CLASS | 120,575,511 | 0.1% | 98.1% | 1.1% |
| CALL_BUILTIN_CLASS | 119,096,485 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,634,500 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 117,169,972 | 0.1% | 98.4% |  |
| FORMAT_VALUE | 114,281,160 | 0.1% | 98.5% |  |
| SEND | 112,328,352 | 0.1% | 98.6% |  |
| UNARY_NOT_LIST | 110,493,248 | 0.1% | 98.6% | 1.2% |
| LOAD_CLOSURE | 109,629,532 | 0.1% | 98.7% |  |
| COMPARE_OP_FLOAT | 109,603,932 | 0.1% | 98.8% | 0.0% |
| FOR_ITER_GEN | 102,608,940 | 0.1% | 98.9% | 0.0% |
| GET_ANEXT | 100,136,760 | 0.1% | 99.0% |  |
| MAKE_FUNCTION | 93,651,920 | 0.1% | 99.0% |  |
| GET_AWAITABLE | 84,577,928 | 0.1% | 99.1% |  |
| MAKE_CELL | 83,112,599 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,764,714 | 0.1% | 99.2% | 0.0% |
| CALL_FUNCTION_EX | 73,787,503 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_UNICODE | 67,845,340 | 0.0% | 99.3% |  |
| UNARY_NOT_STR | 66,635,180 | 0.0% | 99.4% | 3.0% |
| STORE_DEREF | 65,095,920 | 0.0% | 99.4% |  |
| BUILD_STRING | 57,369,180 | 0.0% | 99.4% |  |
| END_FOR | 56,941,860 | 0.0% | 99.5% |  |
| STORE_ATTR_WITH_HINT | 52,984,378 | 0.0% | 99.5% | 5.9% |
| STORE_ATTR | 52,783,603 | 0.0% | 99.6% |  |
| BUILD_MAP | 51,794,895 | 0.0% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 50,397,637 | 0.0% | 99.6% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 48,913,208 | 0.0% | 99.7% | 0.0% |
| LIST_EXTEND | 47,759,779 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 44,803,782 | 0.0% | 99.7% | 12.1% |
| MAP_ADD | 40,747,620 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,417,900 | 0.0% | 99.8% |  |
| GET_YIELD_FROM_ITER | 27,169,140 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 22,737,614 | 0.0% | 99.8% | 7.7% |
| CALL_NO_KW_TUPLE_1 | 21,686,956 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 17,133,426 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,133,426 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,765,857 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,583,879 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,871,779 | 0.0% | 99.9% |  |
| DICT_MERGE | 9,344,080 | 0.0% | 99.9% |  |
| RERAISE | 8,742,901 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,512,434 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,359,895 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 6,993,593 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,921,920 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 3,745,380 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,411,180 | 0.0% | 100.0% |  |
| BEFORE_WITH | 3,335,595 | 0.0% | 100.0% |  |
| SET_ADD | 3,100,800 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,270,460 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,848,240 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,530,300 | 0.0% | 100.0% |  |
| BUILD_SET | 1,466,520 | 0.0% | 100.0% |  |
| DELETE_FAST | 370,876 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 207,060 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 25,740 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,439 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,419 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 4,080 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,140 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,926,428,431 | 2.2% | 2.2% |
| CALL_PY_EXACT_ARGS RESUME | 2,482,052,951 | 1.8% | 4.0% |
| UNARY_NOT_BOOL POP_JUMP_IF_TRUE | 2,302,227,973 | 1.7% | 5.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,289,690,865 | 1.7% | 7.3% |
| RESUME LOAD_FAST | 1,919,766,787 | 1.4% | 8.8% |
| CONTAINS_OP POP_JUMP_IF_TRUE | 1,863,792,785 | 1.4% | 10.1% |
| POP_JUMP_IF_TRUE LOAD_FAST | 1,863,432,678 | 1.4% | 11.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,546,058,941 | 1.1% | 12.6% |
| LOAD_FAST__LOAD_CONST BINARY_OP_ADD_INT | 1,355,449,320 | 1.0% | 13.6% |
| STORE_FAST__LOAD_FAST LOAD_CONST | 1,262,049,667 | 0.9% | 14.6% |
| STORE_FAST__LOAD_FAST LOAD_FAST | 1,209,313,748 | 0.9% | 15.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,172,645,771 | 0.9% | 16.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,141,601,166 | 0.8% | 17.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 1,116,659,135 | 0.8% | 18.0% |
| LOAD_FAST__LOAD_FAST BINARY_SUBSCR | 1,089,220,800 | 0.8% | 18.8% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,075,251,141 | 0.8% | 19.6% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,033,124,355 | 0.8% | 20.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,027,279,564 | 0.8% | 21.1% |
| NOP LOAD_FAST__LOAD_FAST | 1,017,905,432 | 0.7% | 21.8% |
| BINARY_SUBSCR STORE_FAST__LOAD_FAST | 946,403,800 | 0.7% | 22.5% |
| STORE_FAST JUMP_BACKWARD | 930,118,883 | 0.7% | 23.2% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_BUILTIN | 929,271,909 | 0.7% | 23.9% |
| POP_JUMP_IF_FALSE LOAD_FAST__LOAD_CONST | 921,738,808 | 0.7% | 24.6% |
| POP_JUMP_IF_TRUE LOAD_FAST__LOAD_CONST | 919,867,632 | 0.7% | 25.2% |
| JUMP_BACKWARD FOR_ITER_LIST | 916,355,974 | 0.7% | 25.9% |
| POP_JUMP_IF_FALSE LOAD_FAST__LOAD_FAST | 912,865,273 | 0.7% | 26.6% |
| LOAD_CONST COMPARE_OP_STR | 847,100,392 | 0.6% | 27.2% |
| RESUME LOAD_GLOBAL_BUILTIN | 828,262,489 | 0.6% | 27.8% |
| STORE_FAST__STORE_FAST STORE_FAST__STORE_FAST | 821,885,300 | 0.6% | 28.4% |
| LOAD_FAST__LOAD_FAST CONTAINS_OP | 810,834,780 | 0.6% | 29.0% |
| POP_TOP LOAD_FAST | 805,616,800 | 0.6% | 29.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 804,806,084 | 0.6% | 30.2% |
| LOAD_FAST__LOAD_FAST CALL_PY_EXACT_ARGS | 792,646,439 | 0.6% | 30.8% |
| BINARY_OP_ADD_INT STORE_FAST | 784,748,096 | 0.6% | 31.4% |
| CALL_NO_KW_ISINSTANCE UNARY_NOT_BOOL | 768,979,454 | 0.6% | 31.9% |
| BINARY_SUBSCR LOAD_FAST | 756,842,460 | 0.6% | 32.5% |
| LOAD_FAST RETURN_VALUE | 736,497,406 | 0.5% | 33.0% |
| UNARY_NOT_BOOL POP_JUMP_IF_FALSE | 728,169,396 | 0.5% | 33.6% |
| JUMP_BACKWARD NOP | 717,864,209 | 0.5% | 34.1% |
| LOAD_FAST__LOAD_CONST COMPARE_OP_STR | 713,505,860 | 0.5% | 34.6% |
| LOAD_FAST BINARY_SUBSCR | 704,419,260 | 0.5% | 35.1% |
| POP_TOP JUMP_BACKWARD | 652,462,454 | 0.5% | 35.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST__LOAD_FAST | 626,194,141 | 0.5% | 36.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 626,002,425 | 0.5% | 36.5% |
| LOAD_FAST__LOAD_FAST LOAD_FAST__LOAD_FAST | 624,755,794 | 0.5% | 37.0% |
| LOAD_FAST CONTAINS_OP | 620,462,040 | 0.5% | 37.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 596,308,132 | 0.4% | 37.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST__STORE_FAST | 575,812,464 | 0.4% | 38.3% |
| LOAD_FAST UNARY_NOT_BOOL | 549,009,574 | 0.4% | 38.7% |
| RETURN_CONST POP_TOP | 546,259,972 | 0.4% | 39.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 534,865,474 | 0.4% | 39.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 534,551,816 | 0.4% | 39.9% |
| LOAD_FAST LOAD_ATTR | 532,307,551 | 0.4% | 40.3% |
| LOAD_DEREF LOAD_FAST | 532,009,928 | 0.4% | 40.7% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 518,622,914 | 0.4% | 41.1% |
| FOR_ITER_LIST STORE_FAST__LOAD_FAST | 499,184,157 | 0.4% | 41.4% |
| RESUME POP_TOP | 483,928,820 | 0.4% | 41.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 478,701,433 | 0.4% | 42.1% |
| CALL_NO_KW_BUILTIN_FAST UNARY_NOT_BOOL | 477,098,622 | 0.4% | 42.5% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_SLOT | 475,977,614 | 0.3% | 42.8% |
| BINARY_OP_ADD_INT STORE_FAST__LOAD_FAST | 473,720,340 | 0.3% | 43.2% |
| RETURN_CONST INTERPRETER_EXIT | 472,107,036 | 0.3% | 43.5% |
| RETURN_VALUE RETURN_VALUE | 471,083,933 | 0.3% | 43.9% |
| LOAD_GLOBAL_MODULE LOAD_FAST__LOAD_FAST | 465,585,491 | 0.3% | 44.2% |
| LOAD_FAST__LOAD_FAST LOAD_FAST | 462,089,132 | 0.3% | 44.6% |
| LOAD_CONST LOAD_CONST | 452,403,703 | 0.3% | 44.9% |
| YIELD_VALUE INTERPRETER_EXIT | 450,639,616 | 0.3% | 45.2% |
| STORE_FAST__STORE_FAST LOAD_FAST | 440,623,536 | 0.3% | 45.5% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,640 | 0.3% | 45.9% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 432,557,055 | 0.3% | 46.2% |
| PUSH_NULL LOAD_FAST__LOAD_FAST | 431,925,985 | 0.3% | 46.5% |
| JUMP_BACKWARD FOR_ITER_RANGE | 425,401,576 | 0.3% | 46.8% |
| STORE_FAST__LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 423,068,321 | 0.3% | 47.1% |
| LOAD_ATTR_INSTANCE_VALUE UNARY_NOT_BOOL | 414,542,916 | 0.3% | 47.4% |
| STORE_FAST LOAD_GLOBAL_MODULE | 411,801,012 | 0.3% | 47.7% |
| LOAD_CONST BINARY_OP_ADD_INT | 411,463,259 | 0.3% | 48.0% |
| BUILD_TUPLE RETURN_VALUE | 405,101,760 | 0.3% | 48.3% |
| LOAD_FAST__LOAD_FAST LOAD_CONST | 394,524,928 | 0.3% | 48.6% |
| RESUME JUMP_BACKWARD_NO_INTERRUPT | 390,536,056 | 0.3% | 48.9% |
| SEND_GEN RESUME | 384,535,580 | 0.3% | 49.2% |
| YIELD_VALUE YIELD_VALUE | 384,535,580 | 0.3% | 49.5% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 384,535,580 | 0.3% | 49.7% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 383,696,845 | 0.3% | 50.0% |
| POP_JUMP_IF_TRUE LOAD_FAST__LOAD_FAST | 382,461,468 | 0.3% | 50.3% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 377,602,117 | 0.3% | 50.6% |
| IS_OP POP_JUMP_IF_TRUE | 366,135,361 | 0.3% | 50.9% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST__STORE_FAST | 365,320,240 | 0.3% | 51.1% |
| LOAD_CONST COMPARE_OP_INT | 360,831,466 | 0.3% | 51.4% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 357,611,880 | 0.3% | 51.7% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,708,557 | 0.3% | 51.9% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 334,179,947 | 0.2% | 52.2% |
| RESUME NOP | 332,680,266 | 0.2% | 52.4% |
| RETURN_VALUE STORE_FAST__LOAD_FAST | 328,402,425 | 0.2% | 52.6% |
| RESUME LOAD_GLOBAL_MODULE | 325,450,257 | 0.2% | 52.9% |
| UNARY_NOT_NONE POP_JUMP_IF_TRUE | 325,336,474 | 0.2% | 53.1% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 324,000,348 | 0.2% | 53.4% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 320,456,025 | 0.2% | 53.6% |
| RETURN_VALUE INTERPRETER_EXIT | 316,646,328 | 0.2% | 53.8% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 315,011,862 | 0.2% | 54.1% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 314,791,388 | 0.2% | 54.3% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 120 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,952,480 | 58.5% |
| LOAD_ATTR_INSTANCE_VALUE | 973,086 | 29.2% |
| CALL | 303,651 | 9.1% |
| LOAD_GLOBAL_MODULE | 68,758 | 2.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,900 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,912,624 | 87.3% |
| STORE_FAST__LOAD_FAST | 345,231 | 10.3% |
| STORE_FAST | 76,300 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 209,249,620 | 25.3% |
| LOAD_FAST | 125,112,533 | 15.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.7% |
| LOAD_FAST__LOAD_FAST | 66,097,720 | 8.0% |
| LOAD_ATTR_INSTANCE_VALUE | 44,171,820 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 128,040,020 | 15.5% |
| STORE_FAST__LOAD_FAST | 113,098,175 | 13.7% |
| LOAD_FAST__LOAD_FAST | 106,844,406 | 12.9% |
| RETURN_VALUE | 69,475,980 | 8.4% |
| LOAD_CONST | 68,589,420 | 8.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,043,300 | 72.8% |
| LOAD_FAST | 65,042,770 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 90,420,050 | 23.2% |
| LOAD_FAST | 45,573,500 | 11.7% |
| LOAD_FAST__LOAD_FAST | 41,370,060 | 10.6% |
| RETURN_VALUE | 31,350,960 | 8.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 1,355,449,320 | 61.6% |
| LOAD_CONST | 411,463,259 | 18.7% |
| LOAD_FAST | 281,181,076 | 12.8% |
| LOAD_FAST__LOAD_FAST | 47,334,360 | 2.1% |
| END_SEND | 29,134,080 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 784,748,096 | 35.6% |
| STORE_FAST__LOAD_FAST | 473,720,340 | 21.5% |
| LOAD_CONST | 132,088,680 | 6.0% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,055,140 | 4.4% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,833,340 | 46.9% |
| BINARY_SLICE | 15,579,000 | 23.0% |
| LOAD_CONST | 12,143,600 | 17.9% |
| LOAD_ATTR | 2,105,320 | 3.1% |
| BUILD_STRING | 2,011,200 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.4% |
| BUILD_TUPLE | 15,457,800 | 22.8% |
| LOAD_FAST | 15,452,520 | 22.8% |
| LOAD_CONST | 8,422,380 | 12.4% |
| RETURN_VALUE | 3,047,100 | 4.5% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 2,305,260 | 38.9% |
| BINARY_SLICE | 1,580,580 | 26.7% |
| RETURN_VALUE | 680,220 | 11.5% |
| BINARY_OP_ADD_UNICODE | 365,020 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,515,160 | 59.4% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,480 | 8.6% |
| LOAD_FAST__LOAD_CONST | 216,660 | 3.7% |
| LOAD_CONST__LOAD_FAST | 60,360 | 1.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 357,611,880 | 43.2% |
| LOAD_FAST__LOAD_FAST | 240,558,420 | 29.1% |
| LOAD_ATTR_INSTANCE_VALUE | 118,763,280 | 14.4% |
| BINARY_SUBSCR | 67,701,000 | 8.2% |
| CALL_BUILTIN_CLASS | 12,782,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 284,043,300 | 34.3% |
| YIELD_VALUE | 210,931,680 | 25.5% |
| BINARY_OP_SUBTRACT_FLOAT | 109,285,680 | 13.2% |
| LOAD_FAST__LOAD_FAST | 96,886,480 | 11.7% |
| LOAD_FAST | 50,101,980 | 6.1% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 96,055,140 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,996 | 19.3% |
| LOAD_FAST__LOAD_FAST | 41,778,900 | 15.7% |
| BINARY_OP | 27,332,740 | 10.3% |
| LOAD_FAST | 27,011,320 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,941,460 | 22.9% |
| LOAD_FAST | 46,425,420 | 17.5% |
| STORE_FAST | 31,320,480 | 11.8% |
| STORE_FAST__LOAD_FAST | 30,843,240 | 11.6% |
| LOAD_FAST__LOAD_FAST | 28,244,880 | 10.6% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.5% |
| LOAD_FAST | 99,719,340 | 37.0% |
| LOAD_ATTR_INSTANCE_VALUE | 28,661,940 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 96,299,197 | 35.7% |
| LOAD_FAST__LOAD_FAST | 73,322,880 | 27.2% |
| SWAP | 55,701,000 | 20.7% |
| LOAD_FAST | 28,349,160 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 205,747,310 | 43.8% |
| LOAD_FAST__LOAD_CONST | 153,616,612 | 32.7% |
| LOAD_FAST | 76,530,680 | 16.3% |
| LOAD_FAST__LOAD_FAST | 20,323,034 | 4.3% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,675,400 | 20.0% |
| STORE_FAST__LOAD_FAST | 72,308,434 | 15.4% |
| SWAP | 68,452,210 | 14.6% |
| RETURN_VALUE | 39,931,800 | 8.5% |
| BINARY_OP | 37,165,200 | 7.9% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 133,483,008 | 54.8% |
| LOAD_FAST | 46,398,900 | 19.1% |
| BINARY_OP_ADD_INT | 35,909,760 | 14.7% |
| LOAD_FAST__LOAD_FAST | 17,152,320 | 7.0% |
| LOAD_FAST__LOAD_CONST | 3,341,446 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 35,333,326 | 14.5% |
| GET_ITER | 33,131,560 | 13.6% |
| CALL_PY_EXACT_ARGS | 25,417,320 | 10.4% |
| BUILD_TUPLE | 24,334,200 | 10.0% |
| LOAD_DEREF | 18,985,680 | 7.8% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 1,089,220,800 | 46.5% |
| LOAD_FAST | 704,419,260 | 30.1% |
| COPY | 109,564,100 | 4.7% |
| BUILD_SLICE | 104,833,920 | 4.5% |
| BINARY_OP_ADD_INT | 89,539,800 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 946,403,800 | 40.4% |
| LOAD_FAST | 756,842,460 | 32.3% |
| LOAD_FAST__LOAD_FAST | 128,268,480 | 5.5% |
| LOAD_FAST__LOAD_CONST | 103,941,420 | 4.4% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 202,300,635 | 33.0% |
| LOAD_FAST__LOAD_CONST | 161,988,960 | 26.4% |
| LOAD_FAST__LOAD_FAST | 131,855,220 | 21.5% |
| LOAD_CONST | 43,786,360 | 7.1% |
| BINARY_SUBSCR | 41,253,400 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 152,197,440 | 24.8% |
| RETURN_VALUE | 104,528,628 | 17.0% |
| STORE_FAST | 79,547,072 | 13.0% |
| CONTAINS_OP | 77,768,700 | 12.7% |
| LOAD_FAST | 49,128,480 | 8.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 48,461,732 | 33.1% |
| LOAD_FAST__LOAD_CONST | 37,507,300 | 25.6% |
| BUILD_TUPLE | 28,812,000 | 19.7% |
| LOAD_FAST | 23,095,860 | 15.8% |
| LOAD_CONST | 4,109,540 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,815,092 | 99.5% |
| MAKE_CELL | 705,600 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,280 | 0.0% |
| CONTAINS_OP | 1,020 | 0.0% |
| LOAD_FAST | 300 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 315,011,862 | 35.6% |
| COPY | 157,633,380 | 17.8% |
| LOAD_CONST | 146,070,608 | 16.5% |
| LOAD_FAST__LOAD_FAST | 114,424,500 | 12.9% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 230,234,215 | 26.1% |
| LOAD_CONST | 192,235,260 | 21.8% |
| LOAD_FAST__LOAD_FAST | 97,229,460 | 11.0% |
| RETURN_VALUE | 90,397,980 | 10.3% |
| LOAD_FAST | 48,951,000 | 5.6% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 117,782,140 | 63.1% |
| LOAD_FAST | 39,803,100 | 21.3% |
| LOAD_CONST | 29,022,380 | 15.6% |
| LOAD_FAST__LOAD_FAST | 3,360 | 0.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,700 | 38.6% |
| LOAD_CONST | 24,655,900 | 13.2% |
| LOAD_FAST | 21,756,180 | 11.7% |
| YIELD_VALUE | 19,353,600 | 10.4% |
| STORE_FAST__LOAD_FAST | 7,579,120 | 4.1% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,719,040 | 99.3% |
| LOAD_FAST__LOAD_CONST | 26,340 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,839,300 | 49.1% |
| LOAD_FAST__LOAD_FAST | 1,704,180 | 45.5% |
| LOAD_FAST__LOAD_CONST | 91,320 | 2.4% |
| STORE_FAST__LOAD_FAST | 48,540 | 1.3% |
| DICT_MERGE | 16,320 | 0.4% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 115,360,342 | 39.6% |
| LOAD_ATTR_SLOT | 37,318,997 | 12.8% |
| SWAP | 31,893,189 | 10.9% |
| LOAD_FAST | 22,113,890 | 7.6% |
| RESUME | 17,316,820 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 94,977,297 | 32.6% |
| LOAD_FAST | 80,708,228 | 27.7% |
| STORE_FAST | 32,887,513 | 11.3% |
| SWAP | 31,893,249 | 10.9% |
| CALL | 9,670,700 | 3.3% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,349,060 | 16.1% |
| RESUME | 6,495,395 | 12.5% |
| SWAP | 5,489,700 | 10.6% |
| POP_JUMP_IF_TRUE | 3,663,000 | 7.1% |
| POP_JUMP_IF_NOT_NONE | 3,543,600 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,342,271 | 31.6% |
| STORE_FAST__LOAD_FAST | 10,324,500 | 19.9% |
| STORE_FAST | 9,949,224 | 19.2% |
| SWAP | 5,489,700 | 10.6% |
| CALL_FUNCTION_EX | 3,354,540 | 6.5% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| LOAD_CONST | 82,320 | 5.6% |
| LOAD_FAST | 45,000 | 3.1% |
| LOAD_GLOBAL_MODULE | 9,960 | 0.7% |
| STORE_FAST__LOAD_FAST | 7,920 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| STORE_FAST__LOAD_FAST | 48,240 | 3.3% |
| LOAD_GLOBAL_BUILTIN | 36,600 | 2.5% |
| CALL_PY_EXACT_ARGS | 34,080 | 2.3% |
| CONTAINS_OP | 9,600 | 0.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,374,360 | 99.5% |
| LOAD_CONST__LOAD_FAST | 674,276 | 0.4% |
| LOAD_FAST | 69,840 | 0.0% |
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
| FORMAT_VALUE | 50,666,640 | 88.3% |
| LOAD_CONST | 6,702,540 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 64.0% |
| CALL | 12,295,080 | 21.4% |
| STORE_FAST | 2,922,000 | 5.1% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.5% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 166,749,573 | 25.0% |
| LOAD_FAST__LOAD_FAST | 141,694,386 | 21.3% |
| LOAD_FAST | 98,971,241 | 14.9% |
| LOAD_CLOSURE | 79,459,466 | 11.9% |
| CALL | 37,728,900 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 405,101,760 | 60.8% |
| LOAD_CONST | 81,810,140 | 12.3% |
| CALL_NO_KW_ISINSTANCE | 33,206,720 | 5.0% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.3% |
| LIST_APPEND | 26,458,320 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 235,488,279 | 25.0% |
| KW_NAMES | 142,851,096 | 15.2% |
| LOAD_FAST__LOAD_FAST | 98,178,245 | 10.4% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,700 | 7.7% |
| LOAD_GLOBAL_MODULE | 55,564,383 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 293,494,982 | 31.2% |
| RESUME | 202,714,727 | 21.6% |
| RETURN_VALUE | 88,091,412 | 9.4% |
| POP_TOP | 43,600,231 | 4.6% |
| LOAD_GLOBAL_MODULE | 38,965,428 | 4.1% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,581,690 | 30.8% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.3% |
| LOAD_FAST__LOAD_FAST | 21,191,050 | 15.4% |
| LOAD_CONST | 12,001,960 | 8.7% |
| LOAD_FAST__LOAD_CONST | 11,519,700 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,450,379 | 78.6% |
| COPY_FREE_VARS | 26,846,101 | 19.4% |
| POP_TOP | 2,060,300 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,130 | 0.3% |
| MAKE_CELL | 171,620 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,564,864 | 27.3% |
| CALL_NO_KW_LEN | 23,148,461 | 19.4% |
| LOAD_GLOBAL_BUILTIN | 9,122,140 | 7.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,231,400 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 61,413,630 | 51.6% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.7% |
| STORE_FAST__LOAD_FAST | 9,170,540 | 7.7% |
| LOAD_FAST | 9,140,700 | 7.7% |
| CALL_BUILTIN_CLASS | 4,071,001 | 3.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,040 | 43.0% |
| KW_NAMES | 24,569,680 | 32.0% |
| LOAD_FAST | 13,265,660 | 17.3% |
| LOAD_FAST__LOAD_FAST | 2,692,180 | 3.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,011,320 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 40.8% |
| STORE_FAST | 23,980,760 | 31.2% |
| POP_TOP | 11,160,113 | 14.5% |
| RETURN_VALUE | 5,460,241 | 7.1% |
| STORE_FAST__LOAD_FAST | 3,855,720 | 5.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 41,803,817 | 56.7% |
| LOAD_FAST | 9,715,746 | 13.2% |
| DICT_MERGE | 9,344,080 | 12.7% |
| LOAD_FAST__LOAD_FAST | 5,883,880 | 8.0% |
| BUILD_MAP | 3,354,540 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 44,952,837 | 60.9% |
| STORE_FAST__LOAD_FAST | 7,649,220 | 10.4% |
| RETURN_VALUE | 6,016,286 | 8.2% |
| MAKE_CELL | 4,707,040 | 6.4% |
| LOAD_FAST__LOAD_FAST | 3,815,580 | 5.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 88,136,760 | 62.3% |
| LIST_EXTEND | 47,196,297 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 63.7% |
| CALL_FUNCTION_EX | 41,803,817 | 28.3% |
| RERAISE | 6,377,160 | 4.3% |
| LOAD_CONST__LOAD_FAST | 3,322,320 | 2.2% |
| BUILD_MAP | 2,008,660 | 1.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,916,892 | 39.2% |
| LOAD_CONST | 8,589,320 | 37.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,063,100 | 17.9% |
| LOAD_FAST__LOAD_FAST | 740,602 | 3.3% |
| LOAD_ATTR | 258,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 30.5% |
| STORE_FAST | 4,122,340 | 18.1% |
| STORE_FAST__LOAD_FAST | 2,929,222 | 12.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,435,680 | 10.7% |
| BINARY_OP | 2,010,960 | 8.8% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,640 | 46.8% |
| LOAD_CONST | 275,337,180 | 29.7% |
| LOAD_FAST__LOAD_FAST | 71,748,020 | 7.7% |
| LOAD_FAST__LOAD_CONST | 62,784,382 | 6.8% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_BOOL | 477,098,622 | 51.4% |
| STORE_FAST | 216,352,154 | 23.3% |
| STORE_FAST__LOAD_FAST | 93,889,500 | 10.1% |
| POP_TOP | 47,606,396 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 377,602,117 | 48.5% |
| LOAD_FAST__LOAD_FAST | 176,689,100 | 22.7% |
| LOAD_FAST__LOAD_CONST | 55,886,880 | 7.2% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,708,557 | 43.9% |
| LOAD_CONST | 171,752,506 | 22.1% |
| STORE_FAST__LOAD_FAST | 157,750,520 | 20.3% |
| RETURN_VALUE | 29,119,142 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 334,179,947 | 42.7% |
| LOAD_GLOBAL_BUILTIN | 320,456,025 | 41.0% |
| LOAD_FAST__LOAD_FAST | 61,327,020 | 7.8% |
| BUILD_TUPLE | 33,206,720 | 4.2% |
| LOAD_ATTR_MODULE | 21,885,180 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_BOOL | 768,979,454 | 98.4% |
| COPY | 5,946,000 | 0.8% |
| RETURN_VALUE | 2,214,338 | 0.3% |
| POP_TOP | 1,996,800 | 0.3% |
| STORE_FAST__LOAD_FAST | 1,367,220 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,250,105 | 63.3% |
| LOAD_ATTR_INSTANCE_VALUE | 42,406,416 | 13.1% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.2% |
| LOAD_DEREF | 20,446,300 | 6.3% |
| LOAD_ATTR_SLOT | 8,331,340 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 125,640,018 | 38.9% |
| LOAD_FAST | 43,771,140 | 13.6% |
| STORE_FAST__LOAD_FAST | 35,106,858 | 10.9% |
| COMPARE_OP_INT | 32,499,860 | 10.1% |
| CALL_BUILTIN_CLASS | 23,148,461 | 7.2% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,098,956 | 73.1% |
| BINARY_SUBSCR | 20,171,040 | 8.5% |
| BINARY_SLICE | 18,506,220 | 7.8% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 4,572,240 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,681,952 | 37.7% |
| LOAD_FAST__LOAD_FAST | 29,968,920 | 12.6% |
| EXTENDED_ARG | 27,821,580 | 11.7% |
| LOAD_FAST | 25,904,540 | 10.9% |
| RETURN_CONST | 20,553,780 | 8.6% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,049,292 | 44.5% |
| LOAD_CONST | 80,788,520 | 20.7% |
| LOAD_FAST__LOAD_FAST | 56,250,720 | 14.4% |
| LOAD_ATTR_METHOD_NO_DICT | 50,243,780 | 12.8% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 260,805,350 | 66.7% |
| STORE_FAST | 40,124,740 | 10.3% |
| LIST_APPEND | 28,850,040 | 7.4% |
| RETURN_VALUE | 11,996,484 | 3.1% |
| LOAD_FAST | 10,523,940 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 143,891,503 | 63.9% |
| LOAD_ATTR | 71,923,116 | 32.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,410,777 | 3.3% |
| LOAD_FAST__LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 301,166 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_BOOL | 59,436,016 | 26.4% |
| STORE_FAST__LOAD_FAST | 51,918,437 | 23.1% |
| GET_ITER | 31,836,780 | 14.1% |
| STORE_FAST | 20,002,188 | 8.9% |
| LOAD_GLOBAL_MODULE | 18,632,220 | 8.3% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,585,251 | 78.9% |
| CALL | 19,486,434 | 9.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.3% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.5% |
| LOAD_ATTR | 3,038,880 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 101,256,933 | 48.0% |
| BINARY_OP | 72,002,140 | 34.1% |
| RETURN_VALUE | 17,284,260 | 8.2% |
| STORE_FAST | 6,522,540 | 3.1% |
| LOAD_FAST | 5,101,920 | 2.4% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,381,580 | 91.9% |
| RETURN_VALUE | 1,727,580 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,800 | 3.3% |
| BINARY_SUBSCR_TUPLE_INT | 30,420 | 0.1% |
| CALL | 25,580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,460 | 33.9% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 29.0% |
| STORE_FAST__LOAD_FAST | 5,588,100 | 14.9% |
| RETURN_VALUE | 3,244,980 | 8.7% |
| BUILD_LIST | 1,966,480 | 5.3% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,490,800 | 66.8% |
| RETURN_GENERATOR | 5,394,160 | 24.9% |
| LOAD_ATTR_SLOT | 1,098,636 | 5.1% |
| CALL | 412,220 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,240 | 65.9% |
| BUILD_TUPLE | 2,891,796 | 13.3% |
| YIELD_VALUE | 2,419,200 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 571,920 | 2.6% |
| STORE_FAST__LOAD_FAST | 452,340 | 2.1% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 324,000,348 | 98.9% |
| LOAD_CONST | 3,615,800 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 239,978,100 | 73.2% |
| STORE_FAST | 45,880,584 | 14.0% |
| LOAD_GLOBAL_MODULE | 13,598,440 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 9,387,180 | 2.9% |
| LOAD_FAST | 7,639,740 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 804,806,084 | 28.9% |
| LOAD_FAST__LOAD_FAST | 792,646,439 | 28.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 432,557,055 | 15.5% |
| LOAD_GLOBAL_MODULE | 159,665,676 | 5.7% |
| LOAD_ATTR_METHOD_NO_DICT | 109,896,674 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,482,052,951 | 89.0% |
| RETURN_GENERATOR | 140,523,912 | 5.0% |
| COPY_FREE_VARS | 124,045,050 | 4.4% |
| MAKE_CELL | 24,891,113 | 0.9% |
| INSTRUMENTED_RESUME | 14,577,840 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 84,858,651 | 56.4% |
| LOAD_ATTR_METHOD_NO_DICT | 12,061,720 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,609,495 | 7.7% |
| LOAD_ATTR | 11,184,040 | 7.4% |
| LOAD_SUPER_ATTR_METHOD | 5,951,040 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,340,059 | 96.7% |
| RETURN_GENERATOR | 3,297,720 | 2.2% |
| MAKE_CELL | 1,008,240 | 0.7% |
| COPY_FREE_VARS | 611,141 | 0.4% |
| CALL_PY_EXACT_ARGS | 87,660 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,682,300 | 93.5% |
| LOAD_GLOBAL_MODULE | 689,760 | 4.1% |
| BUILD_TUPLE | 356,040 | 2.1% |
| LOAD_ATTR_MODULE | 37,756 | 0.2% |
| LOAD_GLOBAL | 1 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,765,857 | 100.0% |


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
| LOAD_FAST | 41,846,920 | 31.0% |
| LOAD_CONST | 37,770,602 | 28.0% |
| LOAD_ATTR | 15,173,613 | 11.2% |
| LOAD_ATTR_SLOT | 13,693,605 | 10.1% |
| LOAD_GLOBAL_MODULE | 8,707,211 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 69,295,743 | 51.3% |
| POP_JUMP_IF_TRUE | 38,838,508 | 28.8% |
| COPY | 18,630,990 | 13.8% |
| RETURN_VALUE | 7,091,533 | 5.3% |
| EXTENDED_ARG | 771,840 | 0.6% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 65,980,840 | 60.2% |
| BINARY_SUBSCR | 23,382,660 | 21.3% |
| LOAD_FAST | 6,297,813 | 5.7% |
| LOAD_CONST | 6,004,560 | 5.5% |
| LOAD_GLOBAL_MODULE | 3,631,939 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 47,981,020 | 43.8% |
| POP_JUMP_IF_TRUE | 32,445,300 | 29.6% |
| POP_JUMP_IF_FALSE | 29,177,252 | 26.6% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360,831,466 | 25.7% |
| LOAD_FAST__LOAD_CONST | 253,027,873 | 18.0% |
| LOAD_FAST | 178,298,128 | 12.7% |
| LOAD_ATTR_INSTANCE_VALUE | 173,086,246 | 12.3% |
| COPY | 102,794,040 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,172,645,771 | 83.6% |
| POP_JUMP_IF_TRUE | 120,646,107 | 8.6% |
| RETURN_VALUE | 59,342,143 | 4.2% |
| EXTENDED_ARG | 16,635,060 | 1.2% |
| LOAD_FAST | 15,024,000 | 1.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 847,100,392 | 53.4% |
| LOAD_FAST__LOAD_CONST | 713,505,860 | 45.0% |
| LOAD_FAST | 8,569,064 | 0.5% |
| LOAD_GLOBAL_MODULE | 4,650,155 | 0.3% |
| RETURN_VALUE | 4,023,840 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,546,058,941 | 97.5% |
| POP_JUMP_IF_TRUE | 26,990,869 | 1.7% |
| COPY | 6,083,868 | 0.4% |
| RETURN_VALUE | 4,337,060 | 0.3% |
| EXTENDED_ARG | 1,145,940 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 810,834,780 | 41.1% |
| LOAD_FAST | 620,462,040 | 31.4% |
| LOAD_GLOBAL_MODULE | 301,342,680 | 15.3% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_CONST__LOAD_FAST | 66,104,160 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,863,792,785 | 94.4% |
| POP_JUMP_IF_FALSE | 59,687,088 | 3.0% |
| RETURN_VALUE | 25,006,920 | 1.3% |
| COPY | 20,881,380 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,776,280 | 25.4% |
| LOAD_FAST | 236,011,506 | 22.4% |
| SWAP | 105,748,980 | 10.1% |
| LOAD_FAST__LOAD_FAST | 88,896,900 | 8.4% |
| LOAD_FAST__LOAD_CONST | 78,332,100 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,776,280 | 25.4% |
| UNARY_NOT_BOOL | 232,816,634 | 22.1% |
| BINARY_SUBSCR_LIST_INT | 157,633,380 | 15.0% |
| BINARY_SUBSCR | 109,564,100 | 10.4% |
| COMPARE_OP_INT | 102,794,040 | 9.8% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 124,045,050 | 77.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,846,101 | 16.7% |
| CALL | 8,744,572 | 5.5% |
| CALL_PY_WITH_DEFAULTS | 611,141 | 0.4% |
| LOAD_ATTR_PROPERTY | 157,200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 176,119,981 | 70.6% |
| RETURN_GENERATOR | 73,398,180 | 29.4% |
| MAKE_CELL | 18,480 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,512,434 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,648,636 | 78.1% |
| NOP | 1,713,800 | 20.1% |
| RETURN_CONST | 149,518 | 1.8% |
| LOAD_GLOBAL_MODULE | 480 | 0.0% |


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
| CALL | 81,000 | 21.8% |
| STORE_ATTR_INSTANCE_VALUE | 18,000 | 4.9% |
| POP_EXCEPT | 18,000 | 4.9% |
| NOP | 18,000 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 151,020 | 40.7% |
| RETURN_VALUE | 138,600 | 37.4% |
| RETURN_CONST | 36,000 | 9.7% |
| LOAD_FAST | 20,956 | 5.7% |
| JUMP_BACKWARD | 9,540 | 2.6% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 72,991,500 | 57.5% |
| BUILD_SLICE | 53,340,056 | 42.0% |
| LOAD_FAST | 295,498 | 0.2% |
| LOAD_FAST__LOAD_CONST | 277,500 | 0.2% |
| CALL | 19,918 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 54,070,500 | 42.6% |
| LOAD_FAST | 26,986,436 | 21.3% |
| LOAD_FAST__LOAD_FAST | 26,382,660 | 20.8% |
| LOAD_CONST | 18,040,078 | 14.2% |
| JUMP_BACKWARD | 1,038,960 | 0.8% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,025,020 | 96.6% |
| LOAD_ATTR_INSTANCE_VALUE | 150,600 | 1.6% |
| LOAD_DEREF | 75,760 | 0.8% |
| RETURN_VALUE | 50,880 | 0.5% |
| BUILD_CONST_KEY_MAP | 16,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,344,080 | 100.0% |


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
| RETURN_CONST | 56,941,860 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 37,036,080 | 65.0% |
| LOAD_FAST | 19,006,800 | 33.4% |
| RETURN_CONST | 790,080 | 1.4% |
| LOAD_FAST__LOAD_FAST | 93,840 | 0.2% |
| LOAD_CONST__LOAD_FAST | 5,280 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,299,236 | 48.7% |
| RETURN_VALUE | 68,993,656 | 33.5% |
| RETURN_CONST | 36,581,696 | 17.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 88,752,956 | 43.1% |
| POP_TOP | 48,145,132 | 23.4% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 14.2% |
| BINARY_OP_ADD_INT | 29,134,080 | 14.2% |
| STORE_FAST | 6,081,240 | 3.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_BOOL | 81,549,080 | 27.2% |
| JUMP_BACKWARD | 45,498,780 | 15.2% |
| LOAD_FAST | 34,637,660 | 11.6% |
| CALL_NO_KW_LIST_APPEND | 27,821,580 | 9.3% |
| IS_OP | 18,001,680 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 104,876,800 | 35.0% |
| JUMP_BACKWARD | 58,818,900 | 19.6% |
| FOR_ITER_LIST | 45,404,440 | 15.2% |
| POP_JUMP_IF_NONE | 36,518,860 | 12.2% |
| POP_JUMP_IF_FALSE | 19,416,960 | 6.5% |


</details>

### FORMAT_VALUE

<details>
<summary> Successors and predecessors for FORMAT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 50,269,440 | 44.0% |
| LOAD_FAST__LOAD_FAST | 36,024,720 | 31.5% |
| LOAD_ATTR | 13,008,960 | 11.4% |
| LOAD_FAST | 5,719,740 | 5.0% |
| RETURN_VALUE | 2,459,160 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 51,035,580 | 44.7% |
| BUILD_STRING | 50,666,640 | 44.3% |
| LOAD_CONST | 6,725,100 | 5.9% |
| LOAD_FAST | 5,845,020 | 5.1% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 206,640,687 | 73.4% |
| GET_ITER | 49,591,081 | 17.6% |
| EXTENDED_ARG | 16,515,680 | 5.9% |
| SWAP | 5,812,740 | 2.1% |
| LOAD_FAST | 3,009,020 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 147,898,980 | 52.5% |
| STORE_FAST__LOAD_FAST | 56,673,220 | 20.1% |
| STORE_FAST | 20,077,318 | 7.1% |
| LOAD_FAST | 17,496,241 | 6.2% |
| RETURN_CONST | 14,192,109 | 5.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,954,400 | 55.5% |
| JUMP_BACKWARD | 45,290,700 | 44.1% |
| EXTENDED_ARG | 321,360 | 0.3% |
| LOAD_FAST | 42,120 | 0.0% |
| SWAP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 57,005,100 | 55.6% |
| RESUME | 45,603,600 | 44.4% |
| STORE_FAST__LOAD_FAST | 120 | 0.0% |
| RETURN_CONST | 120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 916,355,974 | 74.2% |
| GET_ITER | 186,524,629 | 15.1% |
| LOAD_FAST | 59,095,840 | 4.8% |
| EXTENDED_ARG | 45,404,440 | 3.7% |
| SWAP | 25,731,389 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 499,184,157 | 40.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,183,712 | 25.5% |
| STORE_FAST | 160,025,892 | 13.0% |
| RETURN_CONST | 103,269,754 | 8.4% |
| LOAD_FAST | 57,748,091 | 4.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 425,401,576 | 89.1% |
| GET_ITER | 25,514,610 | 5.3% |
| LOAD_FAST | 21,531,120 | 4.5% |
| SWAP | 4,261,260 | 0.9% |
| EXTENDED_ARG | 836,040 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 296,061,136 | 62.0% |
| STORE_FAST | 132,193,187 | 27.7% |
| RETURN_CONST | 23,855,580 | 5.0% |
| JUMP_BACKWARD | 9,669,540 | 2.0% |
| LOAD_FAST | 3,289,241 | 0.7% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 290,433,498 | 69.7% |
| GET_ITER | 120,733,158 | 29.0% |
| SWAP | 2,897,440 | 0.7% |
| FOR_ITER_LIST | 1,236,557 | 0.3% |
| LOAD_FAST | 1,120,800 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 242,996,400 | 58.3% |
| STORE_FAST | 46,725,180 | 11.2% |
| LOAD_FAST__LOAD_FAST | 41,688,480 | 10.0% |
| LOAD_FAST | 39,925,172 | 9.6% |
| LOAD_FAST__LOAD_CONST | 21,393,480 | 5.1% |


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
| STORE_FAST__LOAD_FAST | 138,283,364 | 23.8% |
| LOAD_ATTR_INSTANCE_VALUE | 77,343,937 | 13.3% |
| LOAD_FAST | 71,848,060 | 12.4% |
| CALL_BUILTIN_CLASS | 61,413,630 | 10.6% |
| RETURN_VALUE | 49,965,360 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 186,524,629 | 32.1% |
| FOR_ITER_TUPLE | 120,733,158 | 20.8% |
| CALL_PY_EXACT_ARGS | 84,798,720 | 14.6% |
| FOR_ITER_GEN | 56,954,400 | 9.8% |
| FOR_ITER | 49,591,081 | 8.5% |


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
| IMPORT_NAME | 1,397,760 | 75.6% |
| STORE_FAST | 450,480 | 24.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,848,240 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,530,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,397,760 | 91.3% |
| STORE_FAST__LOAD_FAST | 129,840 | 8.5% |
| STORE_FAST | 2,100 | 0.1% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,359 | 51.7% |
| GET_ITER | 4,020 | 47.6% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,419 | 52.4% |
| NOP | 3,060 | 36.3% |
| INSTRUMENTED_RETURN_CONST | 240 | 2.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 240 | 2.8% |
| LOAD_CONST | 240 | 2.8% |


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,060 | 41.2% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,060 | 41.2% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 819 | 11.0% |
| LIST_APPEND | 300 | 4.0% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 120 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,359 | 58.8% |
| LOAD_FAST | 3,060 | 41.2% |


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
| COMPARE_OP_INT | 14,567,100 | 99.9% |
| COMPARE_OP_STR | 7,020 | 0.0% |
| UNARY_NOT_BOOL | 5,319 | 0.0% |
| UNARY_NOT | 3,060 | 0.0% |
| UNARY_NOT_STR | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,291,980 | 50.0% |
| LOAD_GLOBAL | 7,290,600 | 50.0% |
| INSTRUMENTED_JUMP_BACKWARD | 819 | 0.0% |
| INSTRUMENTED_RETURN_VALUE | 480 | 0.0% |


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
| UNARY_NOT_BOOL | 13,920 | 54.1% |
| UNARY_NOT_STR | 6,600 | 25.6% |
| EXTENDED_ARG | 3,300 | 12.8% |
| UNARY_NOT_NONE | 780 | 3.0% |
| UNARY_NOT | 480 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,960 | 73.7% |
| INSTRUMENTED_RETURN_CONST | 4,740 | 18.4% |
| LOAD_GLOBAL | 1,020 | 4.0% |
| POP_TOP | 420 | 1.6% |
| LOAD_CONST | 240 | 0.9% |


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
| INSTRUMENTED_POP_JUMP_IF_TRUE | 4,740 | 87.8% |
| POP_TOP | 300 | 5.6% |
| INSTRUMENTED_FOR_ITER | 240 | 4.4% |
| STORE_GLOBAL | 60 | 1.1% |
| CALL_NO_KW_LIST_APPEND | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,800 | 88.9% |
| UNARY_NOT_BOOL | 400 | 7.4% |
| POP_TOP | 180 | 3.3% |
| UNARY_NOT | 20 | 0.4% |


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
| UNARY_NOT_BOOL | 1,200 | 0.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 472,107,036 | 37.2% |
| YIELD_VALUE | 450,639,616 | 35.5% |
| RETURN_VALUE | 316,646,328 | 24.9% |
| RETURN_GENERATOR | 30,089,340 | 2.4% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,104,040 | 49.9% |
| LOAD_GLOBAL_MODULE | 78,736,347 | 18.2% |
| LOAD_FAST | 63,227,640 | 14.6% |
| LOAD_FAST__LOAD_FAST | 50,633,760 | 11.7% |
| LOAD_GLOBAL_BUILTIN | 11,509,560 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 366,135,361 | 84.6% |
| POP_JUMP_IF_FALSE | 38,166,408 | 8.8% |
| EXTENDED_ARG | 18,001,680 | 4.2% |
| RETURN_VALUE | 3,140,700 | 0.7% |
| COPY | 2,903,520 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 930,118,883 | 29.0% |
| POP_TOP | 652,462,454 | 20.3% |
| POP_JUMP_IF_TRUE | 518,622,914 | 16.2% |
| POP_JUMP_IF_FALSE | 383,696,845 | 12.0% |
| LIST_APPEND | 145,926,908 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 916,355,974 | 28.6% |
| NOP | 717,864,209 | 22.4% |
| FOR_ITER_RANGE | 425,401,576 | 13.3% |
| FOR_ITER_TUPLE | 290,433,498 | 9.1% |
| FOR_ITER | 206,640,687 | 6.4% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 390,536,056 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 384,535,580 | 98.5% |
| SEND | 6,000,476 | 1.5% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 172,024,982 | 41.7% |
| POP_JUMP_IF_FALSE | 97,309,387 | 23.6% |
| POP_TOP | 56,832,569 | 13.8% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.4% |
| POP_JUMP_IF_NONE | 10,513,680 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 158,542,048 | 38.4% |
| LOAD_FAST__LOAD_FAST | 77,362,132 | 18.8% |
| LOAD_CONST__LOAD_FAST | 36,254,040 | 8.8% |
| LOAD_GLOBAL_MODULE | 26,455,882 | 6.4% |
| LOAD_GLOBAL_BUILTIN | 25,564,696 | 6.2% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 42,893,633 | 25.5% |
| LOAD_CONST | 34,616,447 | 20.5% |
| LOAD_FAST | 29,808,916 | 17.7% |
| LOAD_GLOBAL_MODULE | 18,000,780 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,341,020 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 142,851,096 | 84.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,569,680 | 14.6% |
| CALL_BUILTIN_CLASS | 1,051,480 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,850,040 | 19.8% |
| BUILD_TUPLE | 26,458,320 | 18.1% |
| BINARY_OP | 20,606,280 | 14.1% |
| LOAD_FAST | 18,168,840 | 12.4% |
| RETURN_VALUE | 14,843,380 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 145,926,908 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 37,120,517 | 77.7% |
| LOAD_FAST | 10,038,981 | 21.0% |
| LOAD_CONST | 366,720 | 0.8% |
| RETURN_VALUE | 114,881 | 0.2% |
| LOAD_DEREF | 77,460 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 47,196,297 | 98.8% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.4% |
| STORE_FAST | 172,560 | 0.4% |
| LOAD_FAST | 107,981 | 0.2% |
| STORE_FAST__LOAD_FAST | 88,721 | 0.2% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 532,307,551 | 44.4% |
| LOAD_GLOBAL_BUILTIN | 221,928,804 | 18.5% |
| STORE_FAST__LOAD_FAST | 160,189,849 | 13.3% |
| LOAD_GLOBAL_MODULE | 94,750,122 | 7.9% |
| LOAD_ATTR_SLOT | 80,022,237 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,352,563 | 18.6% |
| IS_OP | 216,104,040 | 18.0% |
| STORE_FAST__LOAD_FAST | 118,485,214 | 9.9% |
| LOAD_FAST__LOAD_FAST | 94,228,802 | 7.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 71,923,116 | 6.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,323,987 | 96.5% |
| LOAD_FAST | 1,812,980 | 1.5% |
| LOAD_GLOBAL_BUILTIN | 1,789,824 | 1.5% |
| LOAD_ATTR_MODULE | 358,500 | 0.3% |
| STORE_FAST__LOAD_FAST | 170,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,700,000 | 49.5% |
| LOAD_FAST | 21,919,557 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,784,900 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.4% |
| LOAD_FAST__LOAD_FAST | 2,458,644 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,926,428,431 | 79.2% |
| STORE_FAST__LOAD_FAST | 311,181,670 | 8.4% |
| LOAD_FAST__LOAD_FAST | 247,325,734 | 6.7% |
| COPY | 72,036,285 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 50,757,496 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,027,279,564 | 27.8% |
| UNARY_NOT_BOOL | 414,542,916 | 11.2% |
| STORE_FAST__LOAD_FAST | 222,288,640 | 6.0% |
| LOAD_ATTR_METHOD_NO_DICT | 181,658,456 | 4.9% |
| RETURN_VALUE | 177,937,673 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 30,424,860 | 62.2% |
| STORE_FAST__LOAD_FAST | 11,951,660 | 24.4% |
| LOAD_FAST | 6,406,181 | 13.1% |
| LOAD_CONST__LOAD_FAST | 130,067 | 0.3% |
| LOAD_ATTR | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,235,214 | 72.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,410,777 | 15.2% |
| LOAD_CONST | 4,823,940 | 9.9% |
| LOAD_FAST__LOAD_FAST | 1,228,800 | 2.5% |
| CALL | 119,437 | 0.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 478,701,433 | 36.7% |
| STORE_FAST__LOAD_FAST | 300,932,186 | 23.1% |
| LOAD_ATTR_INSTANCE_VALUE | 181,658,456 | 13.9% |
| LOAD_FAST__LOAD_CONST | 54,094,680 | 4.2% |
| LOAD_GLOBAL_MODULE | 52,835,475 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 626,002,425 | 48.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 143,891,503 | 11.0% |
| LOAD_FAST__LOAD_FAST | 128,642,181 | 9.9% |
| LOAD_CONST | 118,744,847 | 9.1% |
| CALL_PY_EXACT_ARGS | 109,896,674 | 8.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,141,601,166 | 63.4% |
| STORE_FAST__LOAD_FAST | 423,068,321 | 23.5% |
| LOAD_ATTR_INSTANCE_VALUE | 61,490,202 | 3.4% |
| LOAD_ATTR | 45,742,077 | 2.5% |
| LOAD_ATTR_SLOT | 44,399,813 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 626,194,141 | 34.8% |
| LOAD_FAST | 596,308,132 | 33.1% |
| CALL_PY_EXACT_ARGS | 432,557,055 | 24.0% |
| LOAD_GLOBAL_MODULE | 49,469,424 | 2.7% |
| LOAD_CONST__LOAD_FAST | 30,941,880 | 1.7% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 306,832,765 | 95.2% |
| LOAD_ATTR_MODULE | 11,591,920 | 3.6% |
| LOAD_ATTR | 1,339,738 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.4% |
| LOAD_FAST__LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 99,677,595 | 30.9% |
| LOAD_FAST | 98,054,872 | 30.4% |
| CALL | 25,893,302 | 8.0% |
| CALL_NO_KW_ISINSTANCE | 21,885,180 | 6.8% |
| LOAD_GLOBAL_BUILTIN | 15,320,020 | 4.8% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,775,349 | 62.0% |
| STORE_FAST__LOAD_FAST | 9,220,906 | 20.6% |
| LOAD_ATTR_SLOT | 5,106,800 | 11.4% |
| RETURN_VALUE | 1,251,000 | 2.8% |
| LOAD_ATTR_INSTANCE_VALUE | 931,920 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 39,206,779 | 87.5% |
| UNARY_NOT_NONE | 3,117,900 | 7.0% |
| RETURN_VALUE | 827,543 | 1.8% |
| LOAD_FAST | 538,780 | 1.2% |
| LOAD_ATTR_WITH_HINT | 383,760 | 0.9% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,033,124,355 | 78.5% |
| STORE_FAST__LOAD_FAST | 161,286,800 | 12.2% |
| LOAD_ATTR_SLOT | 40,634,171 | 3.1% |
| COPY | 40,131,480 | 3.0% |
| LOAD_CONST__LOAD_FAST | 13,777,780 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 303,479,481 | 23.0% |
| UNARY_NOT_NONE | 85,862,458 | 6.5% |
| LOAD_ATTR | 80,022,237 | 6.1% |
| UNARY_NOT_BOOL | 66,914,825 | 5.1% |
| COMPARE_OP_FLOAT | 65,980,840 | 5.0% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 197,353,462 | 58.4% |
| STORE_FAST__LOAD_FAST | 73,035,280 | 21.6% |
| LOAD_ATTR_WITH_HINT | 22,491,140 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 22,337,272 | 6.6% |
| COPY | 12,982,380 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,524,240 | 23.2% |
| STORE_FAST__LOAD_FAST | 42,208,320 | 12.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,665,378 | 10.8% |
| COMPARE_OP_INT | 35,140,620 | 10.4% |
| LOAD_CONST | 27,884,640 | 8.2% |


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
| LOAD_CLOSURE | 30,170,066 | 27.5% |
| STORE_FAST | 19,018,320 | 17.3% |
| POP_JUMP_IF_FALSE | 2,240,040 | 2.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,697,940 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 79,459,466 | 72.5% |
| LOAD_CLOSURE | 30,170,066 | 27.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 1,262,049,667 | 26.9% |
| LOAD_CONST | 452,403,703 | 9.7% |
| LOAD_FAST__LOAD_FAST | 394,524,928 | 8.4% |
| LOAD_FAST__LOAD_CONST | 275,324,700 | 5.9% |
| BINARY_SUBSCR_LIST_INT | 192,235,260 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 847,100,392 | 18.1% |
| LOAD_CONST | 452,403,703 | 9.7% |
| BINARY_OP_ADD_INT | 411,463,259 | 8.8% |
| COMPARE_OP_INT | 360,831,466 | 7.7% |
| STORE_FAST | 300,724,761 | 6.4% |


</details>

### LOAD_CONST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_CONST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 216,250,756 | 21.2% |
| POP_JUMP_IF_TRUE | 170,365,497 | 16.7% |
| RESUME | 149,545,260 | 14.7% |
| STORE_FAST | 111,610,964 | 10.9% |
| STORE_ATTR_INSTANCE_VALUE | 70,468,217 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 283,151,503 | 27.8% |
| LOAD_FAST | 202,072,139 | 19.8% |
| STORE_ATTR_INSTANCE_VALUE | 120,911,870 | 11.9% |
| SWAP | 78,966,600 | 7.7% |
| CONTAINS_OP | 66,104,160 | 6.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 229,975,980 | 28.4% |
| STORE_FAST | 122,116,793 | 15.1% |
| LOAD_GLOBAL_BUILTIN | 109,919,905 | 13.6% |
| PUSH_NULL | 37,562,576 | 4.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,640 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 532,009,928 | 65.6% |
| LOAD_CONST | 67,722,287 | 8.4% |
| LOAD_FAST__LOAD_FAST | 29,856,212 | 3.7% |
| LOAD_DEREF | 23,803,733 | 2.9% |
| CALL_NO_KW_LEN | 20,446,300 | 2.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,289,690,865 | 12.8% |
| RESUME | 1,919,766,787 | 10.7% |
| POP_JUMP_IF_TRUE | 1,863,432,678 | 10.4% |
| STORE_FAST__LOAD_FAST | 1,209,313,748 | 6.8% |
| POP_JUMP_IF_FALSE | 1,116,659,135 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,926,428,431 | 16.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,141,601,166 | 6.4% |
| LOAD_GLOBAL_BUILTIN | 1,075,251,141 | 6.0% |
| LOAD_ATTR_SLOT | 1,033,124,355 | 5.8% |
| CALL_PY_EXACT_ARGS | 804,806,084 | 4.5% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 38,703,249 | 76.8% |
| LOAD_FAST_AND_CLEAR | 11,694,388 | 23.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,695,089 | 76.8% |
| LOAD_FAST_AND_CLEAR | 11,694,388 | 23.2% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 3,609,960 | 51.6% |
| POP_TOP | 2,028,060 | 29.0% |
| LOAD_GLOBAL_BUILTIN | 421,740 | 6.0% |
| STORE_FAST | 308,040 | 4.4% |
| LOAD_ATTR_METHOD_NO_DICT | 298,440 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 51.2% |
| POP_JUMP_IF_NOT_NONE | 1,506,240 | 21.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 408,000 | 5.8% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 294,360 | 4.2% |
| LOAD_FAST | 243,960 | 3.5% |


</details>

### LOAD_FAST__LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 921,738,808 | 24.8% |
| POP_JUMP_IF_TRUE | 919,867,632 | 24.8% |
| LOAD_GLOBAL_BUILTIN | 278,721,162 | 7.5% |
| JUMP_BACKWARD | 206,228,040 | 5.6% |
| LOAD_GLOBAL_MODULE | 158,738,640 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,355,449,320 | 36.5% |
| COMPARE_OP_STR | 713,505,860 | 19.2% |
| LOAD_CONST | 275,324,700 | 7.4% |
| COMPARE_OP_INT | 253,027,873 | 6.8% |
| BINARY_SUBSCR_DICT | 161,988,960 | 4.4% |


</details>

### LOAD_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 1,017,905,432 | 13.5% |
| POP_JUMP_IF_FALSE | 912,865,273 | 12.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 626,194,141 | 8.3% |
| LOAD_FAST__LOAD_FAST | 624,755,794 | 8.3% |
| LOAD_GLOBAL_MODULE | 465,585,491 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,089,220,800 | 14.5% |
| CONTAINS_OP | 810,834,780 | 10.8% |
| CALL_PY_EXACT_ARGS | 792,646,439 | 10.5% |
| LOAD_FAST__LOAD_FAST | 624,755,794 | 8.3% |
| STORE_ATTR_SLOT | 475,977,614 | 6.3% |


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
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,290,600 | 99.1% |
| STORE_FAST | 18,451 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 6,700 | 0.1% |
| NOP | 4,161 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,302,185 | 99.2% |
| LOAD_GLOBAL_MODULE | 29,453 | 0.4% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 11,798 | 0.2% |
| LOAD_ATTR | 1,810 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,075,251,141 | 26.5% |
| POP_JUMP_IF_TRUE | 929,271,909 | 22.9% |
| RESUME | 828,262,489 | 20.4% |
| STORE_FAST | 534,551,816 | 13.2% |
| POP_JUMP_IF_FALSE | 141,048,591 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,289,690,865 | 56.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,640 | 10.7% |
| CALL_NO_KW_ISINSTANCE | 320,456,025 | 7.9% |
| LOAD_FAST__LOAD_CONST | 278,721,162 | 6.9% |
| LOAD_ATTR | 221,928,804 | 5.5% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 534,865,474 | 19.3% |
| STORE_FAST | 411,801,012 | 14.9% |
| RESUME | 325,450,257 | 11.8% |
| STORE_FAST__LOAD_FAST | 303,659,518 | 11.0% |
| POP_JUMP_IF_TRUE | 188,440,755 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 465,585,491 | 16.8% |
| CALL_NO_KW_ISINSTANCE | 334,179,947 | 12.1% |
| LOAD_ATTR_MODULE | 306,832,765 | 11.1% |
| CONTAINS_OP | 301,342,680 | 10.9% |
| LOAD_FAST | 264,402,906 | 9.6% |


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
| LOAD_FAST | 1,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,120 | 98.2% |
| LOAD_SUPER_ATTR_ATTR | 20 | 1.8% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,270,320 | 100.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,191,740 | 96.5% |
| LOAD_GLOBAL_MODULE | 64,080 | 2.8% |
| LOAD_FAST__LOAD_FAST | 10,200 | 0.4% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,159,852 | 100.0% |
| LOAD_DEREF | 9,000 | 0.0% |
| LOAD_SUPER_ATTR | 1,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 66,087,401 | 56.4% |
| LOAD_FAST | 36,798,600 | 31.4% |
| CALL_PY_EXACT_ARGS | 6,184,271 | 5.3% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.1% |
| CALL | 1,199,700 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,662,766 | 57.4% |
| CALL_PY_EXACT_ARGS | 24,891,113 | 30.0% |
| CALL_FUNCTION_EX | 4,707,040 | 5.7% |
| CALL | 3,797,580 | 4.6% |
| CALL_PY_WITH_DEFAULTS | 1,008,240 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,662,766 | 57.3% |
| RESUME | 34,860,813 | 41.9% |
| RETURN_GENERATOR | 580,860 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 93,642,680 | 100.0% |
| LOAD_FAST__LOAD_CONST | 9,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,302,820 | 64.4% |
| LOAD_GLOBAL_BUILTIN | 18,994,680 | 20.3% |
| STORE_FAST | 2,954,527 | 3.2% |
| LOAD_GLOBAL_MODULE | 2,838,440 | 3.0% |
| STORE_FAST__LOAD_FAST | 2,503,180 | 2.7% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,836,160 | 38.9% |
| RETURN_VALUE | 6,246,240 | 15.3% |
| LOAD_FAST | 5,888,640 | 14.5% |
| JUMP_FORWARD | 4,782,720 | 11.7% |
| STORE_FAST | 4,423,680 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 20,584,800 | 50.5% |
| JUMP_BACKWARD | 18,945,480 | 46.5% |
| CALL_FUNCTION_EX | 1,211,400 | 3.0% |
| LOAD_CONST | 5,940 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 717,864,209 | 48.6% |
| RESUME | 332,680,266 | 22.5% |
| STORE_FAST | 145,470,393 | 9.9% |
| POP_JUMP_IF_TRUE | 75,260,362 | 5.1% |
| NOP | 52,748,911 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 1,017,905,432 | 68.9% |
| LOAD_FAST | 274,926,147 | 18.6% |
| NOP | 52,748,911 | 3.6% |
| PUSH_NULL | 41,322,754 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 33,600,465 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,776,278 | 57.1% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.9% |
| SWAP | 1,967,760 | 11.5% |
| COPY | 1,668,841 | 9.7% |
| STORE_FAST | 442,456 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,153,911 | 53.4% |
| RETURN_VALUE | 1,910,160 | 11.1% |
| JUMP_FORWARD | 1,715,820 | 10.0% |
| RERAISE | 1,668,841 | 9.7% |
| POP_TOP | 1,384,127 | 8.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 1,546,058,941 | 37.8% |
| COMPARE_OP_INT | 1,172,645,771 | 28.7% |
| UNARY_NOT_BOOL | 728,169,396 | 17.8% |
| UNARY_NOT | 209,499,190 | 5.1% |
| UNARY_NOT_NONE | 80,575,316 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,116,659,135 | 27.3% |
| LOAD_FAST__LOAD_CONST | 921,738,808 | 22.6% |
| LOAD_FAST__LOAD_FAST | 912,865,273 | 22.3% |
| JUMP_BACKWARD | 383,696,845 | 9.4% |
| LOAD_GLOBAL_BUILTIN | 141,048,591 | 3.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 151,340,494 | 52.2% |
| LOAD_FAST | 46,756,090 | 16.1% |
| EXTENDED_ARG | 36,518,860 | 12.6% |
| LOAD_ATTR_SLOT | 25,233,420 | 8.7% |
| LOAD_DEREF | 13,535,820 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 91,810,502 | 31.7% |
| PUSH_NULL | 52,474,740 | 18.1% |
| LOAD_FAST__LOAD_CONST | 36,582,396 | 12.6% |
| LOAD_DEREF | 27,393,360 | 9.5% |
| JUMP_BACKWARD | 26,688,668 | 9.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,889,305 | 53.4% |
| STORE_FAST__LOAD_FAST | 130,062,202 | 31.0% |
| LOAD_ATTR_INSTANCE_VALUE | 29,306,595 | 7.0% |
| LOAD_ATTR | 17,293,882 | 4.1% |
| EXTENDED_ARG | 7,189,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 145,467,227 | 34.7% |
| LOAD_GLOBAL_BUILTIN | 96,121,780 | 22.9% |
| LOAD_FAST__LOAD_FAST | 59,534,109 | 14.2% |
| LOAD_GLOBAL_MODULE | 35,093,052 | 8.4% |
| NOP | 18,177,436 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_BOOL | 2,302,227,973 | 41.0% |
| CONTAINS_OP | 1,863,792,785 | 33.2% |
| IS_OP | 366,135,361 | 6.5% |
| UNARY_NOT_NONE | 325,336,474 | 5.8% |
| UNARY_NOT_INT | 201,164,792 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,863,432,678 | 33.2% |
| LOAD_GLOBAL_BUILTIN | 929,271,909 | 16.5% |
| LOAD_FAST__LOAD_CONST | 919,867,632 | 16.4% |
| JUMP_BACKWARD | 518,622,914 | 9.2% |
| LOAD_FAST__LOAD_FAST | 382,461,468 | 6.8% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 546,259,972 | 24.4% |
| RESUME | 483,928,820 | 21.6% |
| CALL_NO_KW_BUILTIN_O | 341,708,557 | 15.3% |
| POP_JUMP_IF_TRUE | 132,857,359 | 5.9% |
| RETURN_VALUE | 114,719,053 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 805,616,800 | 34.6% |
| JUMP_BACKWARD | 652,462,454 | 28.0% |
| RESUME | 250,364,372 | 10.8% |
| RETURN_CONST | 179,623,556 | 7.7% |
| LOAD_FAST__LOAD_FAST | 124,578,491 | 5.4% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,320,500 | 31.1% |
| LOAD_ATTR | 3,255,660 | 19.0% |
| RAISE_VARARGS | 2,296,860 | 13.4% |
| CALL_NO_KW_BUILTIN_FAST | 1,783,220 | 10.4% |
| RERAISE | 1,632,360 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,710,449 | 91.7% |
| LOAD_GLOBAL_MODULE | 1,031,236 | 6.0% |
| LOAD_FAST | 386,940 | 2.3% |
| WITH_EXCEPT_START | 4,080 | 0.0% |
| LOAD_GLOBAL | 721 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 269,570,392 | 36.1% |
| POP_TOP | 70,133,836 | 9.4% |
| POP_JUMP_IF_TRUE | 67,263,076 | 9.0% |
| POP_JUMP_IF_FALSE | 53,966,555 | 7.2% |
| POP_JUMP_IF_NONE | 52,474,740 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 431,925,985 | 57.9% |
| LOAD_FAST | 150,129,225 | 20.1% |
| LOAD_FAST__LOAD_CONST | 122,537,940 | 16.4% |
| LOAD_DEREF | 37,562,576 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 3,415,920 | 0.5% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,491,540 | 43.7% |
| LOAD_ATTR_MODULE | 583,740 | 17.1% |
| LOAD_CONST | 543,960 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 15.9% |
| LOAD_FAST | 150,960 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,296,860 | 67.3% |
| COPY | 963,300 | 28.2% |
| LOAD_CONST | 151,020 | 4.4% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,377,160 | 72.9% |
| POP_EXCEPT | 1,668,841 | 19.1% |
| POP_TOP | 386,940 | 4.4% |
| POP_JUMP_IF_FALSE | 158,940 | 1.8% |
| DELETE_FAST | 151,020 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,632,360 | 68.9% |
| COPY | 696,901 | 29.4% |
| CALL_INTRINSIC_1 | 41,160 | 1.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,482,052,951 | 61.8% |
| SEND_GEN | 384,535,580 | 9.6% |
| POP_TOP | 250,364,372 | 6.2% |
| CALL | 202,714,727 | 5.0% |
| COPY_FREE_VARS | 176,119,981 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,919,766,787 | 37.8% |
| LOAD_GLOBAL_BUILTIN | 828,262,489 | 16.3% |
| POP_TOP | 483,928,820 | 9.5% |
| JUMP_BACKWARD_NO_INTERRUPT | 390,536,056 | 7.7% |
| NOP | 332,680,266 | 6.5% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 245,133,361 | 18.6% |
| POP_JUMP_IF_TRUE | 208,299,234 | 15.8% |
| POP_TOP | 179,623,556 | 13.6% |
| STORE_ATTR_INSTANCE_VALUE | 176,858,095 | 13.4% |
| RESUME | 122,694,660 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 546,259,972 | 41.3% |
| INTERPRETER_EXIT | 472,107,036 | 35.7% |
| END_FOR | 56,941,860 | 4.3% |
| UNARY_NOT_BOOL | 56,316,354 | 4.3% |
| LOAD_FAST | 52,435,800 | 4.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,523,912 | 63.8% |
| COPY_FREE_VARS | 73,398,180 | 33.3% |
| CALL_PY_WITH_DEFAULTS | 3,297,720 | 1.5% |
| CALL_FUNCTION_EX | 1,713,800 | 0.8% |
| CALL | 768,780 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,331,692 | 31.3% |
| GET_ITER | 37,913,520 | 15.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,040 | 13.2% |
| INTERPRETER_EXIT | 30,089,340 | 12.0% |
| STORE_FAST__LOAD_FAST | 19,048,620 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 736,497,406 | 25.6% |
| RETURN_VALUE | 471,083,933 | 16.4% |
| BUILD_TUPLE | 405,101,760 | 14.1% |
| LOAD_ATTR_INSTANCE_VALUE | 177,937,673 | 6.2% |
| BINARY_SUBSCR_DICT | 104,528,628 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 471,083,933 | 16.4% |
| STORE_FAST__LOAD_FAST | 328,402,425 | 11.4% |
| INTERPRETER_EXIT | 316,646,328 | 11.0% |
| STORE_FAST | 260,344,229 | 9.1% |
| UNPACK_SEQUENCE_TUPLE | 258,461,780 | 9.0% |


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
| JUMP_BACKWARD_NO_INTERRUPT | 384,535,580 | 78.5% |
| LOAD_CONST | 105,584,092 | 21.5% |
| SEND | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 384,535,580 | 78.5% |
| POP_TOP | 105,584,352 | 21.5% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 4.0% |
| STORE_FAST__LOAD_FAST | 48,000 | 1.5% |
| LOAD_FAST | 19,440 | 0.6% |
| BINARY_SUBSCR_LIST_INT | 17,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,100,800 | 100.0% |


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
| LOAD_FAST | 17,651,580 | 33.4% |
| LOAD_CONST__LOAD_FAST | 14,610,802 | 27.7% |
| LOAD_FAST__LOAD_FAST | 14,016,260 | 26.6% |
| CALL | 5,419,260 | 10.3% |
| SWAP | 946,541 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,478,330 | 29.3% |
| LOAD_DEREF | 13,446,120 | 25.5% |
| RETURN_CONST | 8,603,120 | 16.3% |
| JUMP_BACKWARD | 5,554,200 | 10.5% |
| LOAD_FAST__LOAD_FAST | 4,693,240 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 314,791,388 | 38.7% |
| LOAD_FAST | 229,645,429 | 28.3% |
| LOAD_CONST__LOAD_FAST | 120,911,870 | 14.9% |
| SWAP | 72,036,285 | 8.9% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 283,108,602 | 34.8% |
| RETURN_CONST | 176,858,095 | 21.8% |
| LOAD_FAST__LOAD_FAST | 165,530,480 | 20.4% |
| LOAD_CONST__LOAD_FAST | 70,468,217 | 8.7% |
| NOP | 51,296,969 | 6.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 475,977,614 | 45.3% |
| LOAD_CONST__LOAD_FAST | 283,151,503 | 27.0% |
| LOAD_FAST | 243,921,554 | 23.2% |
| SWAP | 40,131,480 | 3.8% |
| STORE_FAST__LOAD_FAST | 3,626,160 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 280,306,565 | 26.7% |
| RETURN_CONST | 245,133,361 | 23.4% |
| LOAD_FAST | 241,760,473 | 23.0% |
| LOAD_CONST__LOAD_FAST | 216,250,756 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 24,862,340 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,238,080 | 40.1% |
| SWAP | 12,982,380 | 24.5% |
| LOAD_FAST__LOAD_FAST | 11,671,620 | 22.0% |
| LOAD_CONST__LOAD_FAST | 6,562,554 | 12.4% |
| LOAD_DEREF | 240,940 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,376,280 | 63.0% |
| RETURN_CONST | 6,693,698 | 12.6% |
| JUMP_BACKWARD | 5,313,540 | 10.0% |
| LOAD_CONST__LOAD_FAST | 3,665,460 | 6.9% |
| LOAD_FAST__LOAD_FAST | 2,308,020 | 4.4% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,873,520 | 41.3% |
| STORE_FAST | 19,045,080 | 29.3% |
| LOAD_CONST | 6,734,880 | 10.3% |
| YIELD_VALUE | 2,419,200 | 3.7% |
| CALL | 2,261,700 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,280 | 29.2% |
| LOAD_DEREF | 13,725,300 | 21.1% |
| LOAD_FAST__LOAD_FAST | 13,436,760 | 20.6% |
| LOAD_FAST | 9,422,220 | 14.5% |
| LOAD_CONST | 4,658,340 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 784,748,096 | 25.2% |
| LOAD_CONST | 300,724,761 | 9.7% |
| RETURN_VALUE | 260,344,229 | 8.4% |
| STORE_FAST__STORE_FAST | 218,029,080 | 7.0% |
| CALL_NO_KW_BUILTIN_FAST | 216,352,154 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 930,118,883 | 29.9% |
| LOAD_GLOBAL_BUILTIN | 534,551,816 | 17.2% |
| LOAD_GLOBAL_MODULE | 411,801,012 | 13.2% |
| PUSH_NULL | 269,570,392 | 8.7% |
| JUMP_FORWARD | 172,024,982 | 5.5% |


</details>

### STORE_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 946,403,800 | 16.4% |
| FOR_ITER_LIST | 499,184,157 | 8.6% |
| BINARY_OP_ADD_INT | 473,720,340 | 8.2% |
| RETURN_VALUE | 328,402,425 | 5.7% |
| FOR_ITER_RANGE | 296,061,136 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,262,049,667 | 21.9% |
| LOAD_FAST | 1,209,313,748 | 20.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 423,068,321 | 7.3% |
| LOAD_ATTR_INSTANCE_VALUE | 311,181,670 | 5.4% |
| LOAD_GLOBAL_MODULE | 303,659,518 | 5.3% |


</details>

### STORE_FAST__STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 821,885,300 | 41.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 575,812,464 | 28.8% |
| UNPACK_SEQUENCE_TUPLE | 365,320,240 | 18.2% |
| UNPACK_SEQUENCE_LIST | 140,214,420 | 7.0% |
| LOAD_ATTR_SLOT | 45,908,040 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 821,885,300 | 41.0% |
| LOAD_FAST | 440,623,536 | 22.0% |
| LOAD_DEREF | 229,975,980 | 11.5% |
| STORE_FAST | 218,029,080 | 10.9% |
| STORE_FAST__LOAD_FAST | 87,285,540 | 4.4% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,147,600 | 99.9% |
| CALL | 3,840 | 0.1% |
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
| MAKE_FUNCTION | 240 | 5.0% |

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
| LOAD_FAST__LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 103,875,000 | 88.3% |
| RETURN_CONST | 5,855,760 | 5.0% |
| LOAD_FAST__LOAD_FAST | 4,157,040 | 3.5% |
| LOAD_FAST | 3,703,320 | 3.1% |
| JUMP_BACKWARD | 39,840 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 109,571,980 | 34.7% |
| LOAD_FAST | 85,443,401 | 27.1% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.2% |
| LOAD_FAST__LOAD_FAST | 36,010,260 | 11.4% |
| LOAD_FAST__LOAD_CONST | 25,985,560 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.5% |
| LOAD_FAST__LOAD_FAST | 104,114,220 | 33.0% |
| RETURN_CONST | 33,817,800 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,002,980 | 8.6% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 134,170,988 | 69.7% |
| LOAD_FAST__LOAD_FAST | 20,330,520 | 10.6% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.3% |
| RETURN_VALUE | 7,992,040 | 4.2% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,025,080 | 37.4% |
| LOAD_FAST | 63,769,732 | 33.1% |
| JUMP_BACKWARD | 28,272,900 | 14.7% |
| RETURN_CONST | 12,747,120 | 6.6% |
| LOAD_GLOBAL_MODULE | 7,339,980 | 3.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,380 | 52.2% |
| LOAD_FAST__LOAD_FAST | 69,943,740 | 23.2% |
| LOAD_FAST__LOAD_CONST | 26,244,000 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |
| BINARY_OP_SUBTRACT_INT | 15,939,000 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 110,622,960 | 36.6% |
| LOAD_FAST__LOAD_FAST | 97,710,840 | 32.3% |
| LOAD_FAST__LOAD_CONST | 87,681,480 | 29.0% |
| RETURN_CONST | 4,469,160 | 1.5% |
| LOAD_FAST | 1,049,300 | 0.3% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.5% |
| BINARY_OP_ADD_FLOAT | 116,255,040 | 12.8% |
| BINARY_OP_ADD_INT | 80,910,906 | 8.9% |
| LOAD_CONST__LOAD_FAST | 78,966,600 | 8.7% |
| BINARY_OP_SUBTRACT_INT | 68,452,210 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.5% |
| STORE_SUBSCR_LIST_INT | 157,633,380 | 17.4% |
| STORE_SUBSCR | 109,571,980 | 12.1% |
| COPY | 105,748,980 | 11.7% |
| STORE_ATTR_INSTANCE_VALUE | 72,036,285 | 7.9% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,094,201 | 85.0% |
| LOAD_ATTR_MODULE | 1,444,222 | 12.2% |
| LOAD_ATTR | 201,056 | 1.7% |
| LOAD_FAST | 132,300 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,871,779 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 110,837,640 | 91.4% |
| LOAD_GLOBAL_MODULE | 3,058,560 | 2.5% |
| LOAD_FAST | 2,803,800 | 2.3% |
| LOAD_CONST__LOAD_FAST | 2,222,160 | 1.8% |
| BINARY_SUBSCR_TUPLE_INT | 1,205,640 | 1.0% |

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
| LOAD_FAST | 160,893,936 | 43.8% |
| STORE_FAST__LOAD_FAST | 87,069,307 | 23.7% |
| LOAD_ATTR_INSTANCE_VALUE | 77,838,758 | 21.2% |
| LOAD_ATTR_SLOT | 19,349,940 | 5.3% |
| COPY | 9,403,009 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 209,499,190 | 57.1% |
| POP_JUMP_IF_TRUE | 154,468,714 | 42.1% |
| UNARY_NOT | 1,116,438 | 0.3% |
| UNARY_NOT_NONE | 948,464 | 0.3% |
| EXTENDED_ARG | 653,540 | 0.2% |


</details>

### UNARY_NOT_BOOL

<details>
<summary> Successors and predecessors for UNARY_NOT_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 768,979,454 | 24.3% |
| LOAD_FAST | 549,009,574 | 17.3% |
| CALL_NO_KW_BUILTIN_FAST | 477,098,622 | 15.1% |
| LOAD_ATTR_INSTANCE_VALUE | 414,542,916 | 13.1% |
| RETURN_VALUE | 257,380,531 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,302,227,973 | 72.7% |
| POP_JUMP_IF_FALSE | 728,169,396 | 23.0% |
| EXTENDED_ARG | 81,549,080 | 2.6% |
| COPY | 26,795,460 | 0.8% |
| RETURN_VALUE | 16,098,153 | 0.5% |


</details>

### UNARY_NOT_INT

<details>
<summary> Successors and predecessors for UNARY_NOT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 137,142,280 | 60.6% |
| LOAD_FAST | 38,023,161 | 16.8% |
| CALL_NO_KW_BUILTIN_O | 12,835,620 | 5.7% |
| BINARY_OP | 11,088,495 | 4.9% |
| COPY | 7,503,614 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 201,164,792 | 88.9% |
| POP_JUMP_IF_FALSE | 23,901,798 | 10.6% |
| COPY | 931,380 | 0.4% |
| EXTENDED_ARG | 164,040 | 0.1% |
| RETURN_VALUE | 104,160 | 0.0% |


</details>

### UNARY_NOT_LIST

<details>
<summary> Successors and predecessors for UNARY_NOT_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,341,500 | 38.3% |
| STORE_FAST__LOAD_FAST | 32,074,091 | 29.0% |
| LOAD_ATTR_INSTANCE_VALUE | 26,967,799 | 24.4% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.6% |
| LOAD_ATTR | 1,779,620 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 61,623,320 | 55.8% |
| POP_JUMP_IF_TRUE | 45,580,148 | 41.3% |
| COPY | 1,597,200 | 1.4% |
| CALL_PY_EXACT_ARGS | 746,880 | 0.7% |
| EXTENDED_ARG | 623,400 | 0.6% |


</details>

### UNARY_NOT_NONE

<details>
<summary> Successors and predecessors for UNARY_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 143,386,256 | 35.1% |
| LOAD_ATTR_SLOT | 85,862,458 | 21.0% |
| LOAD_ATTR_INSTANCE_VALUE | 82,231,000 | 20.1% |
| LOAD_FAST | 37,744,512 | 9.2% |
| LOAD_ATTR | 21,930,580 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 325,336,474 | 79.7% |
| POP_JUMP_IF_FALSE | 80,575,316 | 19.7% |
| EXTENDED_ARG | 1,242,480 | 0.3% |
| UNARY_NOT | 947,101 | 0.2% |
| UNARY_NOT_STR | 36,040 | 0.0% |


</details>

### UNARY_NOT_STR

<details>
<summary> Successors and predecessors for UNARY_NOT_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,536,820 | 44.3% |
| STORE_FAST__LOAD_FAST | 15,320,440 | 23.0% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,424,880 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,220 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 35,711,400 | 53.6% |
| POP_JUMP_IF_FALSE | 30,270,200 | 45.4% |
| STORE_FAST | 316,800 | 0.5% |
| RETURN_VALUE | 282,360 | 0.4% |
| UNARY_NOT_NONE | 36,060 | 0.1% |


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
| STORE_FAST__STORE_FAST | 220,200 | 100.0% |


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
| LOAD_FAST | 9,080 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 204,840 | 98.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,420 | 0.7% |
| UNPACK_SEQUENCE_TUPLE | 400 | 0.2% |
| UNPACK_SEQUENCE | 380 | 0.2% |
| UNPACK_SEQUENCE_LIST | 20 | 0.0% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,172,180 | 70.0% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,000,900 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 804,960 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 140,214,420 | 100.0% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 258,461,780 | 61.6% |
| LOAD_FAST | 102,455,620 | 24.4% |
| BINARY_SUBSCR_DICT | 14,268,900 | 3.4% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 365,320,240 | 87.1% |
| STORE_FAST | 24,993,240 | 6.0% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.7% |
| STORE_FAST__LOAD_FAST | 4,893,827 | 1.2% |
| LOAD_FAST | 290,520 | 0.1% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,183,712 | 52.5% |
| FOR_ITER | 147,898,980 | 24.7% |
| RETURN_VALUE | 84,038,180 | 14.0% |
| LOAD_FAST | 35,129,100 | 5.9% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 575,812,464 | 96.2% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST__LOAD_FAST | 9,187,080 | 1.5% |
| LOAD_FAST | 904,080 | 0.2% |
| STORE_FAST | 649,380 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 4,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT_NONE | 4,080 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 384,535,580 | 43.7% |
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 23.9% |
| CALL_INTRINSIC_1 | 94,136,760 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 31,980,360 | 3.6% |
| BINARY_SUBSCR | 30,970,080 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 450,639,616 | 51.2% |
| YIELD_VALUE | 384,535,580 | 43.7% |
| STORE_FAST | 28,777,860 | 3.3% |
| STORE_FAST__LOAD_FAST | 8,241,960 | 0.9% |
| UNPACK_SEQUENCE_TUPLE | 4,809,360 | 0.5% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### UNARY_NOT

<details>
<summary> specialization stats for UNARY_NOT family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    364867824 | 8.4% |
| specialization.deopt |      1102731 | 0.0% |
|          hit |   3918918426 | 90.2% |
|         miss |     58479174 | 1.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,112,890 | 34.8% |
| Failure | 2,086,759 | 65.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| heap type | 1,854,351 | 88.9% |
| other | 125,860 | 6.0% |
| tuple | 74,420 | 3.6% |
| dict | 14,700 | 0.7% |
| bytes | 10,608 | 0.5% |
| set | 5,820 | 0.3% |
| float | 640 | 0.0% |
| bytearray | 280 | 0.0% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2342570545 | 56.1% |
| specialization.deopt |        60040 | 0.0% |
|          hit |   1827223187 | 43.8% |
|         miss |      3183240 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 61,518 | 9.5% |
| Failure | 588,496 | 90.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 304,920 | 51.8% |
| array int | 112,980 | 19.2% |
| other | 76,560 | 13.0% |
| out of range | 40,440 | 6.9% |
| list slice | 25,500 | 4.3% |
| buffer int | 23,736 | 4.0% |
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
| specialization.deferred |    315713090 | 39.0% |
| specialization.deopt |           40 | 0.0% |
|          hit |    494555212 | 61.0% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 631 | 0.8% |
| Failure | 83,300 | 99.2% |

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
|          hit |   1155792991 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 49,920 | 99.2% |
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
| specialization.deferred |    281568588 | 11.2% |
| specialization.deopt |      2480769 | 0.1% |
|          hit |   2099551880 | 83.6% |
|         miss |    131480963 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,389 | 96.5% |
| Failure | 90,409 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 22,980 | 25.4% |
| dict items | 17,900 | 19.8% |
| seq iter | 15,120 | 16.7% |
| set | 10,909 | 12.1% |
| other | 7,540 | 8.3% |
| reversed list | 3,620 | 4.0% |
| dict values | 3,380 | 3.7% |
| zip | 3,100 | 3.4% |
| ascii string | 2,660 | 2.9% |
| dict keys | 1,760 | 1.9% |
| itertools | 660 | 0.7% |
| map | 600 | 0.7% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |
| string | 20 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     52734292 | 2.7% |
| specialization.deopt |      3586913 | 0.2% |
|          hit |   1725232309 | 87.7% |
|         miss |    190113072 | 9.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,601,504 | 99.0% |
| Failure | 34,720 | 1.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,180 | 49.5% |
| not in dict | 8,020 | 23.1% |
| overriding descriptor | 4,940 | 14.2% |
| not in keys | 1,000 | 2.9% |
| non object slot | 920 | 2.6% |
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
| specialization.deferred |   1198461903 | 11.8% |
| specialization.deopt |      9760923 | 0.1% |
|          hit |   8475892044 | 83.2% |
|         miss |    517448448 | 5.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,809,150 | 86.9% |
| Failure | 1,473,833 | 13.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 641,000 | 43.5% |
| class attr simple | 582,034 | 39.5% |
| metaclass attribute | 98,848 | 6.7% |
| not managed dict | 66,213 | 4.5% |
| method | 51,295 | 3.5% |
| class method obj | 7,020 | 0.5% |
| non object slot | 6,700 | 0.5% |
| class attr descriptor | 5,740 | 0.4% |
| overridden | 5,240 | 0.4% |
| non overriding descriptor | 4,024 | 0.3% |
| mutable class | 2,320 | 0.2% |
| not in keys | 1,680 | 0.1% |
| module attr not found | 1,160 | 0.1% |
| builtin class method | 360 | 0.0% |
| shadowed | 199 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    134862194 | 4.2% |
| specialization.deopt |        22899 | 0.0% |
|          hit |   3096342096 | 95.8% |
|         miss |      1214218 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 25,975 | 19.8% |
| Failure | 105,069 | 80.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 43,830 | 41.7% |
| different types | 24,264 | 23.1% |
| baseobject | 12,880 | 12.3% |
| float long | 8,834 | 8.4% |
| set | 6,620 | 6.3% |
| other | 2,800 | 2.7% |
| bool | 2,341 | 2.2% |
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
| specialization.deferred |      7322104 | 0.1% |
| specialization.deopt |          287 | 0.0% |
|          hit |   6818925116 | 99.9% |
|         miss |        19719 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 38,078 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    827224174 | 15.5% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   4460297895 | 83.7% |
|         miss |     37779500 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 715,967 | 39.4% |
| Failure | 1,103,423 | 60.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 578,820 | 52.5% |
| multiply different types | 171,357 | 15.5% |
| add different types | 151,661 | 13.7% |
| floor divide | 32,680 | 3.0% |
| remainder | 31,550 | 2.9% |
| add other | 29,140 | 2.6% |
| and int | 25,215 | 2.3% |
| lshift | 18,620 | 1.7% |
| rshift | 16,540 | 1.5% |
| true divide different types | 14,340 | 1.3% |
| xor | 10,500 | 1.0% |
| true divide float | 6,640 | 0.6% |
| subtract other | 5,440 | 0.5% |
| power | 3,640 | 0.3% |
| or | 3,440 | 0.3% |
| multiply other | 1,940 | 0.2% |
| true divide other | 980 | 0.1% |
| and other | 820 | 0.1% |
| and different types | 100 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112299952 | 18.6% |
|          hit |    490119932 | 81.4% |

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
|          hit |    119440432 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,140 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    940026719 | 10.9% |
| specialization.deopt |      2762079 | 0.0% |
|          hit |   7547278942 | 87.4% |
|         miss |    146490308 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,795,108 | 87.7% |
| Failure | 390,525 | 12.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| python class | 98,984 | 25.3% |
| meth descr method fastcall keywords | 65,200 | 16.7% |
| kwnames | 50,132 | 12.8% |
| code complex parameters | 48,714 | 12.5% |
| class no vectorcall | 25,477 | 6.5% |
| cfunc varargs keywords | 23,334 | 6.0% |
| meth descr varargs | 21,149 | 5.4% |
| cfunc noargs | 17,260 | 4.4% |
| other | 10,248 | 2.6% |
| class mutable | 7,860 | 2.0% |
| meth descr varargs keywords | 7,143 | 1.8% |
| cmethod | 3,540 | 0.9% |
| bound method | 3,420 | 0.9% |
| cfunc varargs | 2,580 | 0.7% |
| method wrapper | 2,472 | 0.6% |
| operator wrapper | 2,032 | 0.5% |
| str | 980 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 82,733,910,930 | 60.8% |
| Not specialized | 11,243,084,509 | 8.3% |
| Specialized | 42,093,670,028 | 30.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,342,570,545 | 35.6% |
| LOAD_ATTR | 1,198,461,903 | 18.2% |
| CALL | 940,026,719 | 14.3% |
| BINARY_OP | 827,224,174 | 12.6% |
| UNARY_NOT | 364,867,824 | 5.5% |
| STORE_SUBSCR | 315,713,090 | 4.8% |
| FOR_ITER | 281,568,588 | 4.3% |
| COMPARE_OP | 134,862,194 | 2.1% |
| SEND | 112,299,952 | 1.7% |
| STORE_ATTR | 52,734,292 | 0.8% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 231,278,853 | 21.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 168,368,227 | 15.5% |
| STORE_ATTR_SLOT | 111,918,460 | 10.3% |
| CALL_PY_EXACT_ARGS | 89,348,841 | 8.2% |
| STORE_ATTR_INSTANCE_VALUE | 75,043,649 | 6.9% |
| FOR_ITER_LIST | 65,838,353 | 6.0% |
| FOR_ITER_TUPLE | 65,591,490 | 6.0% |
| LOAD_ATTR_SLOT | 56,519,788 | 5.2% |
| UNARY_NOT_NONE | 52,940,635 | 4.9% |
| LOAD_ATTR_METHOD_NO_DICT | 45,376,928 | 4.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,277,849,922 | 23.9% |
| Calls to Python functions inlined | 4,076,169,088 | 76.1% |
| Calls via PyEval_EvalFrame (total) | 1,277,849,922 | 23.9% |
| Calls via PyEval_EvalFrame (vector) | 739,372,146 | 13.8% |
| Calls via PyEval_EvalFrame (generator) | 538,477,776 | 10.1% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 739,367,046 | 13.8% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 189,045,074 | 3.5% |
| Calls via PyEval_EvalFrame (function ex) | 9,423,700 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 124,423,728 | 2.3% |
| Calls via PyEval_EvalFrame (method) | 93,801,445 | 1.8% |
| Frames pushed | 4,222,812,602 | 78.9% |
| Frame objects created | 58,901,954 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,140,087,631 | 35.5% |
| Frees to freelist | 4,143,997,004 |  |
| Allocations | 7,512,477,011 | 64.5% |
| Allocations to 512 bytes | 7,431,789,592 | 63.8% |
| Allocations to 4 kbytes | 65,716,324 | 0.6% |
| Allocations over 4 kbytes | 14,971,095 | 0.1% |
| Frees | 7,758,563,728 |  |
| New values | 123,755,022 |  |
| Interpreter increfs | 55,528,684,450 | 76.0% |
| Interpreter decrefs | 64,648,129,037 | 76.9% |
| Increfs | 17,491,570,031 | 24.0% |
| Decrefs | 19,417,111,243 | 23.1% |
| Materialize dict (on request) | 3,684,060 | 3.0% |
| Materialize dict (new key) | 58,440 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 2,004,533,766 |  |
| Method cache misses | 67,859,939 |  |
| Method cache collisions | 74,209,116 |  |
| Method cache dunder hits | 2,230,730,773 |  |
| Method cache dunder misses | 6,390,167 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,265 |


</details>

---
Stats gathered on: 2023-06-09
