
# Pystats results

- fork: brandtbucher
- ref: shrink-method-caches
- commit hash: 4b64c3e
- commit date: 2023-02-08T04:50:24-08:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 17,034,172,220 | 15.2% | 15.2% |  |
| LOAD_FAST__LOAD_FAST | 5,747,531,163 | 5.1% | 20.3% |  |
| RESUME | 4,825,742,631 | 4.3% | 24.6% |  |
| STORE_FAST__LOAD_FAST | 4,341,313,224 | 3.9% | 28.5% |  |
| POP_JUMP_IF_FALSE | 4,113,275,537 | 3.7% | 32.1% |  |
| LOAD_GLOBAL_BUILTIN | 4,038,871,338 | 3.6% | 35.7% | 0.0% |
| LOAD_CONST | 3,983,268,985 | 3.5% | 39.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 3,525,817,048 | 3.1% | 42.4% | 5.2% |
| RETURN_VALUE | 2,795,587,733 | 2.5% | 44.9% |  |
| LOAD_GLOBAL_MODULE | 2,551,395,559 | 2.3% | 47.2% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,482,072,038 | 2.2% | 49.4% | 3.8% |
| JUMP_BACKWARD | 2,358,161,849 | 2.1% | 51.5% |  |
| POP_TOP | 2,220,439,204 | 2.0% | 53.5% |  |
| LOAD_FAST__LOAD_CONST | 2,047,807,990 | 1.8% | 55.3% |  |
| STORE_FAST__STORE_FAST | 2,009,735,516 | 1.8% | 57.1% |  |
| STORE_FAST | 2,009,169,694 | 1.8% | 58.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,716,099,454 | 1.5% | 60.4% | 8.8% |
| INTERPRETER_EXIT | 1,640,412,047 | 1.5% | 61.8% |  |
| LOAD_ATTR_SLOT | 1,408,856,144 | 1.3% | 63.1% | 6.2% |
| COMPARE_AND_BRANCH_INT | 1,347,450,760 | 1.2% | 64.3% | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,343,912,573 | 1.2% | 65.5% | 4.3% |
| LOAD_ATTR | 1,339,865,404 | 1.2% | 66.7% |  |
| RETURN_CONST | 1,337,666,170 | 1.2% | 67.9% |  |
| FOR_ITER_LIST | 1,248,166,423 | 1.1% | 69.0% | 5.3% |
| BINARY_OP_ADD_INT | 1,213,399,843 | 1.1% | 70.1% | 0.0% |
| POP_JUMP_IF_TRUE | 1,173,950,814 | 1.0% | 71.1% |  |
| BINARY_SUBSCR | 1,117,258,919 | 1.0% | 72.1% |  |
| STORE_ATTR_SLOT | 1,050,600,313 | 0.9% | 73.1% | 10.8% |
| LOAD_CONST__LOAD_FAST | 989,974,398 | 0.9% | 73.9% |  |
| CALL_NO_KW_BUILTIN_FAST | 982,698,216 | 0.9% | 74.8% | 0.0% |
| CALL | 959,043,267 | 0.9% | 75.7% |  |
| LOAD_DEREF | 914,438,611 | 0.8% | 76.5% |  |
| BINARY_SUBSCR_LIST_INT | 903,334,360 | 0.8% | 77.3% | 0.4% |
| PUSH_NULL | 882,292,564 | 0.8% | 78.1% |  |
| BINARY_OP | 858,686,332 | 0.8% | 78.8% |  |
| CALL_NO_KW_BUILTIN_O | 852,510,468 | 0.8% | 79.6% | 0.3% |
| SWAP | 840,105,323 | 0.7% | 80.3% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,610,537 | 0.7% | 81.1% | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 811,753,875 | 0.7% | 81.8% | 7.8% |
| COPY | 811,664,597 | 0.7% | 82.5% |  |
| CONTAINS_OP | 740,105,930 | 0.7% | 83.2% |  |
| CALL_NO_KW_ISINSTANCE | 710,527,079 | 0.6% | 83.8% |  |
| YIELD_VALUE | 686,200,323 | 0.6% | 84.4% |  |
| IS_OP | 664,689,856 | 0.6% | 85.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 616,926,519 | 0.5% | 85.6% |  |
| BUILD_TUPLE | 599,321,530 | 0.5% | 86.1% |  |
| GET_ITER | 548,466,619 | 0.5% | 86.6% |  |
| NOP | 505,270,805 | 0.5% | 87.0% |  |
| POP_JUMP_IF_NOT_NONE | 468,444,339 | 0.4% | 87.5% |  |
| BINARY_OP_SUBTRACT_INT | 466,164,535 | 0.4% | 87.9% | 0.1% |
| FOR_ITER_RANGE | 464,108,323 | 0.4% | 88.3% | 0.0% |
| JUMP_FORWARD | 446,662,179 | 0.4% | 88.7% |  |
| UNPACK_SEQUENCE_TUPLE | 427,162,775 | 0.4% | 89.1% | 0.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 407,635,217 | 0.4% | 89.4% | 8.1% |
| CALL_NO_KW_TYPE_1 | 393,391,756 | 0.4% | 89.8% |  |
| BINARY_OP_ADD_FLOAT | 390,013,599 | 0.3% | 90.1% | 1.6% |
| BINARY_SUBSCR_DICT | 381,147,741 | 0.3% | 90.5% | 0.0% |
| FOR_ITER | 379,227,674 | 0.3% | 90.8% |  |
| LOAD_ATTR_MODULE | 361,659,607 | 0.3% | 91.1% | 0.0% |
| POP_JUMP_IF_NONE | 345,009,213 | 0.3% | 91.4% |  |
| STORE_SUBSCR | 332,546,841 | 0.3% | 91.7% |  |
| LOAD_ATTR_WITH_HINT | 325,056,261 | 0.3% | 92.0% | 2.4% |
| SEND | 319,386,400 | 0.3% | 92.3% |  |
| CALL_NO_KW_LEN | 318,886,351 | 0.3% | 92.6% |  |
| STORE_SUBSCR_LIST_INT | 317,829,585 | 0.3% | 92.9% | 0.0% |
| BUILD_LIST | 306,148,209 | 0.3% | 93.1% |  |
| FOR_ITER_TUPLE | 297,398,639 | 0.3% | 93.4% | 22.3% |
| COPY_FREE_VARS | 271,680,043 | 0.2% | 93.6% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,774,899 | 0.2% | 93.9% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 267,696,438 | 0.2% | 94.1% | 3.2% |
| EXTENDED_ARG | 258,174,494 | 0.2% | 94.4% |  |
| CALL_NO_KW_LIST_APPEND | 256,198,033 | 0.2% | 94.6% | 0.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 238,531,296 | 0.2% | 94.8% | 8.7% |
| BINARY_SUBSCR_TUPLE_INT | 232,083,585 | 0.2% | 95.0% | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 230,556,025 | 0.2% | 95.2% | 12.7% |
| RETURN_GENERATOR | 221,040,570 | 0.2% | 95.4% |  |
| CALL_BUILTIN_CLASS | 219,344,678 | 0.2% | 95.6% | 0.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 216,956,077 | 0.2% | 95.8% | 0.2% |
| COMPARE_OP | 196,209,152 | 0.2% | 96.0% |  |
| KW_NAMES | 188,619,768 | 0.2% | 96.1% |  |
| STORE_SUBSCR_DICT | 186,430,696 | 0.2% | 96.3% |  |
| BINARY_SLICE | 163,371,307 | 0.1% | 96.5% |  |
| BUILD_SLICE | 158,520,480 | 0.1% | 96.6% |  |
| CALL_PY_WITH_DEFAULTS | 153,306,336 | 0.1% | 96.7% | 3.4% |
| BINARY_SUBSCR_GETITEM | 148,412,544 | 0.1% | 96.9% | 0.6% |
| JUMP_IF_FALSE_OR_POP | 147,838,743 | 0.1% | 97.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 144,463,688 | 0.1% | 97.1% | 0.1% |
| COMPARE_AND_BRANCH | 143,089,120 | 0.1% | 97.2% |  |
| CALL_INTRINSIC_1 | 142,912,976 | 0.1% | 97.4% |  |
| UNPACK_SEQUENCE_LIST | 140,459,329 | 0.1% | 97.5% | 0.9% |
| DELETE_SUBSCR | 131,997,656 | 0.1% | 97.6% |  |
| FOR_ITER_GEN | 128,324,931 | 0.1% | 97.7% | 0.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 125,850,056 | 0.1% | 97.8% |  |
| MAKE_FUNCTION | 122,938,796 | 0.1% | 98.0% |  |
| UNARY_NEGATIVE | 121,639,581 | 0.1% | 98.1% |  |
| MAKE_CELL | 121,014,821 | 0.1% | 98.2% |  |
| LIST_APPEND | 117,916,545 | 0.1% | 98.3% |  |
| STORE_SLICE | 117,635,220 | 0.1% | 98.4% |  |
| LOAD_ATTR_CLASS | 113,617,007 | 0.1% | 98.5% | 1.5% |
| FORMAT_VALUE | 111,055,620 | 0.1% | 98.6% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| CALL_FUNCTION_EX | 96,388,048 | 0.1% | 98.8% |  |
| LOAD_CLOSURE | 94,741,579 | 0.1% | 98.8% |  |
| COMPARE_AND_BRANCH_STR | 90,571,388 | 0.1% | 98.9% | 0.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 86,537,899 | 0.1% | 99.0% | 0.0% |
| GET_AWAITABLE | 83,837,120 | 0.1% | 99.1% |  |
| BUILD_MAP | 82,004,810 | 0.1% | 99.1% |  |
| STORE_DEREF | 66,506,580 | 0.1% | 99.2% |  |
| LOAD_ATTR_PROPERTY | 65,618,494 | 0.1% | 99.3% | 13.9% |
| BINARY_OP_ADD_UNICODE | 62,695,000 | 0.1% | 99.3% |  |
| COMPARE_AND_BRANCH_FLOAT | 62,016,806 | 0.1% | 99.4% | 0.0% |
| STORE_ATTR | 57,324,651 | 0.1% | 99.4% |  |
| BUILD_STRING | 56,411,220 | 0.1% | 99.5% |  |
| CALL_NO_KW_STR_1 | 55,976,262 | 0.0% | 99.5% |  |
| JUMP_IF_TRUE_OR_POP | 54,856,636 | 0.0% | 99.6% |  |
| STORE_ATTR_WITH_HINT | 50,302,445 | 0.0% | 99.6% | 2.0% |
| LIST_EXTEND | 49,441,054 | 0.0% | 99.7% |  |
| UNARY_NOT | 46,511,732 | 0.0% | 99.7% |  |
| END_FOR | 38,658,990 | 0.0% | 99.7% |  |
| MAP_ADD | 37,775,458 | 0.0% | 99.8% |  |
| DICT_MERGE | 31,383,142 | 0.0% | 99.8% |  |
| CALL_NO_KW_TUPLE_1 | 26,012,500 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 24,271,213 | 0.0% | 99.8% | 7.2% |
| PUSH_EXC_INFO | 17,759,019 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,759,019 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 17,358,300 | 0.0% | 99.9% |  |
| LOAD_GLOBAL | 14,618,691 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,867,175 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 9,562,464 | 0.0% | 99.9% |  |
| IMPORT_FROM | 9,557,909 | 0.0% | 99.9% |  |
| LOAD_NAME | 9,003,000 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,615,151 | 0.0% | 99.9% |  |
| IMPORT_NAME | 8,342,124 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 7,373,750 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 5,601,926 | 0.0% | 100.0% |  |
| BEFORE_WITH | 4,056,868 | 0.0% | 100.0% |  |
| SET_ADD | 3,114,300 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,871,580 | 0.0% | 100.0% |  |
| RERAISE | 2,589,480 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 2,253,398 | 0.0% | 100.0% |  |
| BUILD_SET | 1,520,266 | 0.0% | 100.0% |  |
| DELETE_FAST | 1,347,480 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 401,993 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 36,000 | 0.0% | 100.0% |  |
| SET_UPDATE | 16,680 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| STORE_NAME | 5,220 | 0.0% | 100.0% |  |
| LOAD_CLASSDEREF | 2,580 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 240 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,804,352,819 | 2.5% | 2.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,320,703,152 | 2.1% | 4.6% |
| CALL_PY_EXACT_ARGS RESUME | 2,232,714,013 | 2.0% | 6.6% |
| RESUME LOAD_FAST | 1,925,883,997 | 1.7% | 8.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 1,812,281,334 | 1.6% | 9.9% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,113,190,902 | 1.0% | 10.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,099,388,742 | 1.0% | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,020,310,135 | 0.9% | 12.8% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 977,007,535 | 0.9% | 13.6% |
| JUMP_BACKWARD FOR_ITER_LIST | 918,748,777 | 0.8% | 14.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 889,891,093 | 0.8% | 15.2% |
| RESUME LOAD_GLOBAL_BUILTIN | 883,951,863 | 0.8% | 16.0% |
| STORE_FAST__STORE_FAST STORE_FAST__STORE_FAST | 822,937,620 | 0.7% | 16.8% |
| STORE_FAST__LOAD_FAST LOAD_FAST | 770,079,852 | 0.7% | 17.4% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 760,850,602 | 0.7% | 18.1% |
| POP_TOP JUMP_BACKWARD | 738,694,480 | 0.7% | 18.8% |
| LOAD_FAST__LOAD_FAST CALL_PY_EXACT_ARGS | 663,925,490 | 0.6% | 19.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 657,775,993 | 0.6% | 20.0% |
| LOAD_FAST__LOAD_FAST LOAD_FAST__LOAD_FAST | 643,273,240 | 0.6% | 20.5% |
| LOAD_FAST RETURN_VALUE | 641,338,399 | 0.6% | 21.1% |
| POP_TOP LOAD_FAST | 621,570,097 | 0.6% | 21.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST__LOAD_FAST | 612,113,127 | 0.5% | 22.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 611,308,551 | 0.5% | 22.7% |
| YIELD_VALUE INTERPRETER_EXIT | 596,688,102 | 0.5% | 23.3% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST__STORE_FAST | 586,841,960 | 0.5% | 23.8% |
| IS_OP POP_JUMP_IF_FALSE | 577,208,265 | 0.5% | 24.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 571,199,784 | 0.5% | 24.8% |
| CALL_NO_KW_ISINSTANCE POP_JUMP_IF_FALSE | 556,101,887 | 0.5% | 25.3% |
| RESUME POP_TOP | 552,962,961 | 0.5% | 25.8% |
| COMPARE_AND_BRANCH_INT LOAD_FAST | 552,265,904 | 0.5% | 26.3% |
| RETURN_CONST POP_TOP | 547,699,176 | 0.5% | 26.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 546,448,155 | 0.5% | 27.3% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_FALSE | 543,299,751 | 0.5% | 27.8% |
| LOAD_FAST POP_JUMP_IF_TRUE | 540,530,310 | 0.5% | 28.2% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 525,378,399 | 0.5% | 28.7% |
| RETURN_CONST INTERPRETER_EXIT | 525,363,713 | 0.5% | 29.2% |
| RETURN_VALUE INTERPRETER_EXIT | 503,999,252 | 0.4% | 29.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 503,237,835 | 0.4% | 30.1% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_SLOT | 502,486,525 | 0.4% | 30.5% |
| LOAD_FAST LOAD_ATTR | 485,930,296 | 0.4% | 31.0% |
| FOR_ITER_LIST STORE_FAST__LOAD_FAST | 484,732,438 | 0.4% | 31.4% |
| POP_JUMP_IF_TRUE LOAD_FAST | 482,901,967 | 0.4% | 31.8% |
| PUSH_NULL LOAD_FAST__LOAD_FAST | 480,221,317 | 0.4% | 32.2% |
| CALL_NO_KW_BUILTIN_FAST POP_JUMP_IF_FALSE | 472,883,749 | 0.4% | 32.7% |
| LOAD_DEREF LOAD_FAST | 472,217,636 | 0.4% | 33.1% |
| LOAD_CONST LOAD_CONST | 458,880,644 | 0.4% | 33.5% |
| STORE_FAST__LOAD_FAST LOAD_CONST | 455,549,994 | 0.4% | 33.9% |
| STORE_FAST__STORE_FAST LOAD_FAST | 445,218,527 | 0.4% | 34.3% |
| RETURN_VALUE RETURN_VALUE | 438,918,179 | 0.4% | 34.7% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 435,765,640 | 0.4% | 35.1% |
| JUMP_BACKWARD FOR_ITER_RANGE | 429,290,292 | 0.4% | 35.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 426,340,975 | 0.4% | 35.8% |
| LOAD_FAST BINARY_SUBSCR | 420,561,126 | 0.4% | 36.2% |
| BINARY_SUBSCR LOAD_FAST | 413,628,750 | 0.4% | 36.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 402,222,283 | 0.4% | 36.9% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST__STORE_FAST | 391,869,089 | 0.3% | 37.3% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 389,714,958 | 0.3% | 37.6% |
| STORE_FAST__LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 389,252,857 | 0.3% | 38.0% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 388,769,615 | 0.3% | 38.3% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 386,831,391 | 0.3% | 38.7% |
| LOAD_FAST__LOAD_FAST LOAD_CONST | 381,507,445 | 0.3% | 39.0% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 367,535,482 | 0.3% | 39.3% |
| STORE_FAST__LOAD_FAST POP_JUMP_IF_FALSE | 366,854,685 | 0.3% | 39.7% |
| LOAD_FAST__LOAD_FAST LOAD_FAST | 364,546,512 | 0.3% | 40.0% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 363,615,000 | 0.3% | 40.3% |
| LOAD_FAST__LOAD_CONST BINARY_OP_ADD_INT | 360,354,120 | 0.3% | 40.6% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 356,486,880 | 0.3% | 41.0% |
| LOAD_CONST COMPARE_AND_BRANCH_INT | 342,511,572 | 0.3% | 41.3% |
| STORE_FAST__LOAD_FAST LOAD_GLOBAL_MODULE | 340,327,823 | 0.3% | 41.6% |
| BUILD_TUPLE RETURN_VALUE | 337,650,531 | 0.3% | 41.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 336,574,536 | 0.3% | 42.2% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 321,894,292 | 0.3% | 42.5% |
| LOAD_ATTR_SLOT LOAD_FAST | 320,966,999 | 0.3% | 42.7% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 319,417,627 | 0.3% | 43.0% |
| RETURN_VALUE STORE_FAST__LOAD_FAST | 314,364,512 | 0.3% | 43.3% |
| LOAD_CONST STORE_FAST | 314,339,492 | 0.3% | 43.6% |
| POP_JUMP_IF_FALSE LOAD_FAST__LOAD_FAST | 313,760,796 | 0.3% | 43.9% |
| RESUME LOAD_FAST__LOAD_FAST | 313,232,292 | 0.3% | 44.1% |
| STORE_FAST__LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 308,898,664 | 0.3% | 44.4% |
| LOAD_FAST POP_JUMP_IF_FALSE | 306,170,194 | 0.3% | 44.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST__LOAD_CONST | 304,009,822 | 0.3% | 45.0% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 302,844,033 | 0.3% | 45.2% |
| LOAD_FAST__LOAD_CONST LOAD_CONST | 292,555,858 | 0.3% | 45.5% |
| CALL STORE_FAST__LOAD_FAST | 291,836,626 | 0.3% | 45.8% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 290,713,216 | 0.3% | 46.0% |
| STORE_FAST PUSH_NULL | 287,346,309 | 0.3% | 46.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST STORE_FAST__LOAD_FAST | 286,214,576 | 0.3% | 46.5% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 284,043,300 | 0.3% | 46.8% |
| LOAD_ATTR LOAD_FAST | 283,776,953 | 0.3% | 47.0% |
| LOAD_CONST__LOAD_FAST STORE_ATTR_SLOT | 282,953,589 | 0.3% | 47.3% |
| LOAD_FAST BINARY_OP_ADD_INT | 281,326,925 | 0.3% | 47.5% |
| STORE_ATTR_SLOT LOAD_FAST__LOAD_FAST | 281,273,627 | 0.3% | 47.8% |
| RESUME LOAD_GLOBAL_MODULE | 280,745,661 | 0.3% | 48.0% |
| JUMP_BACKWARD FOR_ITER | 273,153,211 | 0.2% | 48.3% |
| COPY COPY | 270,086,400 | 0.2% | 48.5% |
| SWAP SWAP | 270,086,400 | 0.2% | 48.8% |
| LOAD_GLOBAL_MODULE CONTAINS_OP | 266,981,980 | 0.2% | 49.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 266,616,023 | 0.2% | 49.2% |
| NOP LOAD_FAST | 266,031,815 | 0.2% | 49.5% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 265,735,344 | 0.2% | 49.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### <252>

<details>
<summary> Successors and predecessors for <252> </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 99,358,740 | 69.1% |
| STORE_FAST__LOAD_FAST | 44,469,720 | 30.9% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 60 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,998,280 | 49.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,476,234 | 36.4% |
| CALL | 474,531 | 11.7% |
| LOAD_GLOBAL_MODULE | 70,923 | 1.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,900 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,463,117 | 85.4% |
| STORE_FAST__LOAD_FAST | 499,391 | 12.3% |
| STORE_FAST | 92,920 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 215,138,585 | 25.1% |
| LOAD_FAST | 111,661,232 | 13.0% |
| LOAD_FAST__LOAD_FAST | 76,130,123 | 8.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.4% |
| RETURN_VALUE | 49,381,751 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 131,547,939 | 15.3% |
| LOAD_FAST | 107,880,089 | 12.6% |
| LOAD_FAST__LOAD_FAST | 106,838,713 | 12.4% |
| RETURN_VALUE | 81,130,834 | 9.4% |
| LOAD_CONST | 66,842,751 | 7.8% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,043,300 | 72.8% |
| LOAD_FAST | 65,119,952 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 90,497,712 | 23.2% |
| LOAD_FAST | 45,573,260 | 11.7% |
| LOAD_FAST__LOAD_FAST | 41,370,060 | 10.6% |
| RETURN_VALUE | 31,350,960 | 8.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 426,340,975 | 35.1% |
| LOAD_FAST__LOAD_CONST | 360,354,120 | 29.7% |
| LOAD_FAST | 281,326,925 | 23.2% |
| LOAD_FAST__LOAD_FAST | 47,607,661 | 3.9% |
| SEND | 29,134,080 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 237,571,462 | 19.6% |
| LOAD_CONST | 129,229,120 | 10.7% |
| STORE_SLICE | 103,909,740 | 8.6% |
| BINARY_OP_MULTIPLY_INT | 96,055,140 | 7.9% |
| BINARY_SUBSCR | 88,165,020 | 7.3% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,779,800 | 53.9% |
| LOAD_CONST | 12,177,380 | 19.4% |
| CALL_NO_KW_STR_1 | 4,820,800 | 7.7% |
| LOAD_ATTR | 2,417,980 | 3.9% |
| BUILD_STRING | 2,011,200 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,301,100 | 26.0% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 25.4% |
| LOAD_CONST | 8,836,380 | 14.1% |
| STORE_FAST | 6,334,200 | 10.1% |
| RETURN_VALUE | 3,795,900 | 6.1% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 751,440 | 26.2% |
| RETURN_VALUE | 680,220 | 23.7% |
| BINARY_OP_ADD_UNICODE | 411,820 | 14.3% |
| LOAD_ATTR_SLOT | 358,800 | 12.5% |
| LOAD_FAST | 284,640 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,982,580 | 69.0% |
| JUMP_BACKWARD | 545,500 | 19.0% |
| LOAD_FAST__LOAD_CONST | 216,660 | 7.5% |
| LOAD_CONST__LOAD_FAST | 60,360 | 2.1% |
| LOAD_FAST__LOAD_FAST | 52,320 | 1.8% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 363,615,000 | 43.9% |
| LOAD_FAST__LOAD_FAST | 234,480,420 | 28.3% |
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
| BINARY_OP_ADD_INT | 96,055,140 | 35.9% |
| LOAD_ATTR_INSTANCE_VALUE | 50,990,580 | 19.0% |
| LOAD_FAST__LOAD_FAST | 44,483,020 | 16.6% |
| BINARY_OP | 27,332,780 | 10.2% |
| LOAD_FAST | 23,886,050 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 83,455,620 | 31.2% |
| LOAD_FAST | 46,484,940 | 17.4% |
| STORE_FAST | 31,324,860 | 11.7% |
| STORE_FAST__LOAD_FAST | 30,966,770 | 11.6% |
| LOAD_FAST__LOAD_FAST | 28,380,780 | 10.6% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.5% |
| LOAD_FAST | 99,736,020 | 37.0% |
| LOAD_ATTR_INSTANCE_VALUE | 28,661,940 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 96,370,102 | 35.7% |
| LOAD_FAST__LOAD_FAST | 73,322,880 | 27.2% |
| SWAP | 55,701,000 | 20.6% |
| LOAD_FAST | 28,349,160 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 207,805,290 | 44.6% |
| LOAD_FAST__LOAD_CONST | 145,266,656 | 31.2% |
| LOAD_FAST | 73,380,188 | 15.7% |
| LOAD_FAST__LOAD_FAST | 22,611,092 | 4.9% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 79,108,360 | 17.0% |
| STORE_FAST__LOAD_FAST | 78,548,513 | 16.8% |
| SWAP | 68,066,499 | 14.6% |
| RETURN_VALUE | 41,308,860 | 8.9% |
| BINARY_OP | 37,397,095 | 8.0% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,986,314 | 58.1% |
| BINARY_OP_ADD_INT | 34,710,900 | 21.2% |
| LOAD_FAST | 24,403,080 | 14.9% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.7% |
| LOAD_ATTR | 2,053,260 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 33,807,413 | 20.7% |
| CALL_PY_EXACT_ARGS | 24,750,840 | 15.2% |
| CALL_NO_KW_LIST_APPEND | 19,300,980 | 11.8% |
| STORE_FAST | 18,194,040 | 11.1% |
| BINARY_OP | 15,381,780 | 9.4% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 420,561,126 | 37.6% |
| LOAD_FAST__LOAD_FAST | 204,886,959 | 18.3% |
| COPY | 109,568,220 | 9.8% |
| BUILD_SLICE | 105,403,380 | 9.4% |
| BINARY_OP_ADD_INT | 88,165,020 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 413,628,750 | 37.0% |
| LOAD_FAST__LOAD_FAST | 128,271,240 | 11.5% |
| LOAD_FAST__LOAD_CONST | 103,941,420 | 9.3% |
| STORE_FAST__LOAD_FAST | 94,509,760 | 8.5% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 6.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,252,367 | 53.6% |
| LOAD_FAST__LOAD_CONST | 76,425,600 | 20.1% |
| BINARY_SUBSCR | 36,829,920 | 9.7% |
| LOAD_CONST | 21,272,080 | 5.6% |
| LOAD_FAST__LOAD_FAST | 16,570,956 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 104,995,385 | 27.5% |
| LOAD_FAST | 50,290,486 | 13.2% |
| LOAD_ATTR_METHOD_NO_DICT | 40,690,500 | 10.7% |
| STORE_FAST | 40,105,317 | 10.5% |
| STORE_FAST__LOAD_FAST | 39,012,777 | 10.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 72,509,506 | 48.9% |
| LOAD_FAST__LOAD_CONST | 37,526,540 | 25.3% |
| BUILD_TUPLE | 28,812,000 | 19.4% |
| LOAD_CONST | 4,150,458 | 2.8% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,020 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 146,819,546 | 98.9% |
| MAKE_CELL | 716,638 | 0.5% |
| POP_JUMP_IF_FALSE | 160,340 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 155,800 | 0.1% |
| GET_ITER | 143,520 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 302,844,033 | 33.5% |
| COPY | 158,997,820 | 17.6% |
| LOAD_CONST | 147,876,765 | 16.4% |
| LOAD_FAST__LOAD_FAST | 141,620,611 | 15.7% |
| BINARY_OP | 48,349,920 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 226,596,596 | 25.1% |
| LOAD_CONST | 193,145,340 | 21.4% |
| LOAD_FAST__LOAD_FAST | 104,247,733 | 11.6% |
| RETURN_VALUE | 90,771,314 | 10.1% |
| LOAD_FAST | 39,390,120 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 135,604,737 | 58.4% |
| LOAD_CONST | 56,612,264 | 24.4% |
| LOAD_FAST | 39,862,524 | 17.2% |
| LOAD_FAST__LOAD_FAST | 3,540 | 0.0% |
| BINARY_SUBSCR | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,123,680 | 31.1% |
| LOAD_GLOBAL_MODULE | 30,081,740 | 13.0% |
| LOAD_CONST | 24,661,538 | 10.6% |
| LOAD_FAST | 21,994,799 | 9.5% |
| YIELD_VALUE | 19,355,040 | 8.3% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,192,500 | 97.5% |
| LOAD_FAST__LOAD_CONST | 181,250 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,976,560 | 53.9% |
| LOAD_FAST | 2,590,860 | 35.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 383,280 | 5.2% |
| STORE_FAST__LOAD_FAST | 252,410 | 3.4% |
| LOAD_FAST__LOAD_CONST | 91,320 | 1.2% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 117,193,851 | 38.3% |
| RESUME | 46,651,013 | 15.2% |
| LOAD_ATTR_SLOT | 36,559,155 | 11.9% |
| LOAD_FAST | 25,219,852 | 8.2% |
| LOAD_CONST | 11,615,520 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,894,403 | 37.5% |
| STORE_FAST__LOAD_FAST | 99,911,647 | 32.6% |
| STORE_FAST | 34,462,683 | 11.3% |
| CALL | 11,208,780 | 3.7% |
| RETURN_VALUE | 8,900,059 | 2.9% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,540,502 | 22.6% |
| RESUME | 14,386,557 | 17.5% |
| BUILD_TUPLE | 11,167,965 | 13.6% |
| STORE_FAST | 9,212,760 | 11.2% |
| POP_JUMP_IF_NOT_NONE | 3,608,462 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,865,472 | 58.4% |
| STORE_FAST__LOAD_FAST | 12,283,202 | 15.0% |
| STORE_FAST | 9,144,280 | 11.2% |
| CALL_NO_KW_BUILTIN_FAST | 4,338,720 | 5.3% |
| CALL_FUNCTION_EX | 3,905,520 | 4.8% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 1,334,100 | 87.8% |
| LOAD_CONST | 82,320 | 5.4% |
| LOAD_FAST | 68,926 | 4.5% |
| CALL_BUILTIN_CLASS | 16,320 | 1.1% |
| LOAD_GLOBAL_MODULE | 9,960 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,334,100 | 87.8% |
| STORE_FAST__LOAD_FAST | 48,240 | 3.2% |
| LOAD_GLOBAL_BUILTIN | 36,600 | 2.4% |
| CALL_PY_EXACT_ARGS | 34,080 | 2.2% |
| LOAD_CONST | 24,600 | 1.6% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,962,780 | 99.6% |
| LOAD_CONST__LOAD_FAST | 433,800 | 0.3% |
| LOAD_FAST | 69,840 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| LOAD_FAST__LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 105,403,380 | 66.5% |
| DELETE_SUBSCR | 53,117,100 | 33.5% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_VALUE | 49,705,680 | 88.1% |
| LOAD_CONST | 6,705,540 | 11.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 65.0% |
| CALL | 12,312,840 | 21.8% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.6% |
| STORE_FAST | 1,597,740 | 2.8% |
| CALL_NO_KW_LIST_APPEND | 1,398,840 | 2.5% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 164,950,042 | 27.5% |
| LOAD_FAST__LOAD_FAST | 140,606,754 | 23.5% |
| LOAD_FAST | 88,820,701 | 14.8% |
| LOAD_CLOSURE | 78,802,557 | 13.1% |
| CALL | 37,769,878 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,650,531 | 56.3% |
| LOAD_CONST | 81,193,371 | 13.5% |
| YIELD_VALUE | 32,442,540 | 5.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.8% |
| LIST_APPEND | 23,272,548 | 3.9% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,822,471 | 22.3% |
| KW_NAMES | 162,975,108 | 17.0% |
| LOAD_FAST__LOAD_FAST | 103,663,765 | 10.8% |
| BINARY_SUBSCR_TUPLE_INT | 72,123,680 | 7.5% |
| LOAD_GLOBAL_MODULE | 55,468,125 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 291,836,626 | 30.4% |
| RESUME | 186,952,857 | 19.5% |
| RETURN_VALUE | 107,872,619 | 11.2% |
| POP_TOP | 50,609,149 | 5.3% |
| LOAD_GLOBAL_MODULE | 39,244,056 | 4.1% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 77,585,432 | 33.7% |
| LOAD_FAST | 60,989,320 | 26.5% |
| LOAD_FAST__LOAD_CONST | 27,076,500 | 11.7% |
| LOAD_CONST | 16,715,000 | 7.2% |
| LOAD_ATTR_INSTANCE_VALUE | 8,945,080 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 188,772,494 | 81.9% |
| COPY_FREE_VARS | 37,754,556 | 16.4% |
| POP_TOP | 2,094,280 | 0.9% |
| MAKE_CELL | 1,383,181 | 0.6% |
| CALL_PY_EXACT_ARGS | 510,234 | 0.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 83,634,599 | 38.1% |
| LOAD_FAST | 70,124,051 | 32.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,456,797 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 6,278,462 | 2.9% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 111,879,777 | 51.0% |
| GET_ITER | 45,920,134 | 20.9% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 5.8% |
| STORE_FAST__LOAD_FAST | 10,242,422 | 4.7% |
| LOAD_FAST | 9,283,920 | 4.2% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,032,100 | 38.2% |
| KW_NAMES | 24,469,840 | 28.3% |
| LOAD_FAST | 19,452,932 | 22.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 5,653,562 | 6.5% |
| LOAD_FAST__LOAD_FAST | 2,692,640 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 36.2% |
| STORE_FAST | 22,181,120 | 25.6% |
| RETURN_VALUE | 13,310,328 | 15.4% |
| POP_TOP | 11,058,883 | 12.8% |
| STORE_FAST__LOAD_FAST | 3,945,372 | 4.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,219,780 | 44.8% |
| DICT_MERGE | 31,383,142 | 32.6% |
| LOAD_FAST | 7,945,546 | 8.2% |
| LOAD_FAST__LOAD_FAST | 5,886,220 | 6.1% |
| BUILD_MAP | 3,905,520 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 45,803,872 | 47.5% |
| STORE_FAST__LOAD_FAST | 21,254,900 | 22.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,720,080 | 8.0% |
| RETURN_VALUE | 7,369,191 | 7.6% |
| LOAD_FAST__LOAD_FAST | 4,982,640 | 5.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 88,136,760 | 61.7% |
| LIST_EXTEND | 48,723,296 | 34.1% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 65.9% |
| CALL_FUNCTION_EX | 43,219,780 | 30.2% |
| LOAD_CONST__LOAD_FAST | 3,322,080 | 2.3% |
| BUILD_MAP | 2,119,936 | 1.5% |
| LOAD_CONST | 48,360 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,725,660 | 40.1% |
| LOAD_FAST | 6,759,186 | 27.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,481,520 | 18.5% |
| LOAD_DEREF | 2,241,760 | 9.2% |
| LOAD_FAST__LOAD_FAST | 635,947 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 28.6% |
| STORE_FAST | 4,415,080 | 18.2% |
| STORE_FAST__LOAD_FAST | 2,899,567 | 11.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,436,000 | 10.0% |
| BINARY_OP | 2,151,720 | 8.9% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 435,765,640 | 44.3% |
| LOAD_CONST | 290,713,216 | 29.6% |
| LOAD_FAST__LOAD_FAST | 83,905,552 | 8.5% |
| LOAD_FAST__LOAD_CONST | 69,914,351 | 7.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,470,460 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 472,883,749 | 48.1% |
| STORE_FAST | 222,602,540 | 22.7% |
| STORE_FAST__LOAD_FAST | 107,878,818 | 11.0% |
| POP_TOP | 47,644,049 | 4.8% |
| CALL_NO_KW_BUILTIN_FAST | 37,470,460 | 3.8% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 388,769,615 | 45.6% |
| LOAD_FAST__LOAD_FAST | 193,964,118 | 22.8% |
| LOAD_FAST__LOAD_CONST | 85,647,840 | 10.0% |
| RETURN_VALUE | 54,163,500 | 6.4% |
| BUILD_STRING | 36,694,920 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 386,831,391 | 45.4% |
| LOAD_CONST | 172,184,457 | 20.2% |
| STORE_FAST__LOAD_FAST | 169,602,644 | 19.9% |
| RETURN_VALUE | 32,411,164 | 3.8% |
| POP_JUMP_IF_TRUE | 19,474,111 | 2.3% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 367,535,482 | 51.7% |
| LOAD_GLOBAL_BUILTIN | 222,863,939 | 31.4% |
| LOAD_FAST__LOAD_FAST | 61,917,691 | 8.7% |
| LOAD_ATTR_MODULE | 27,920,400 | 3.9% |
| BUILD_TUPLE | 14,677,807 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 556,101,887 | 78.3% |
| POP_JUMP_IF_TRUE | 121,437,148 | 17.1% |
| UNARY_NOT | 8,059,540 | 1.1% |
| JUMP_IF_FALSE_OR_POP | 7,347,420 | 1.0% |
| YIELD_VALUE | 7,318,371 | 1.0% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 221,892,653 | 69.6% |
| LOAD_ATTR_INSTANCE_VALUE | 43,235,039 | 13.6% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.3% |
| LOAD_ATTR_SLOT | 8,353,520 | 2.6% |
| LOAD_FAST__LOAD_FAST | 3,233,220 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 130,863,506 | 41.0% |
| LOAD_FAST | 38,888,400 | 12.2% |
| STORE_FAST__LOAD_FAST | 34,972,344 | 11.0% |
| COMPARE_AND_BRANCH_INT | 30,070,222 | 9.4% |
| RETURN_VALUE | 16,745,508 | 5.3% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 181,980,908 | 71.0% |
| BINARY_SUBSCR | 20,171,040 | 7.9% |
| BINARY_SLICE | 19,300,980 | 7.5% |
| RETURN_VALUE | 8,211,500 | 3.2% |
| BINARY_OP | 5,899,840 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 102,851,847 | 40.1% |
| LOAD_FAST__LOAD_FAST | 30,945,600 | 12.1% |
| EXTENDED_ARG | 29,348,688 | 11.5% |
| LOAD_FAST | 28,008,809 | 10.9% |
| RETURN_CONST | 20,589,960 | 8.0% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 159,162,960 | 39.0% |
| LOAD_CONST | 93,393,581 | 22.9% |
| LOAD_FAST__LOAD_FAST | 56,557,800 | 13.9% |
| LOAD_ATTR_METHOD_NO_DICT | 49,732,680 | 12.2% |
| LOAD_GLOBAL_MODULE | 16,437,420 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 286,214,576 | 70.2% |
| STORE_FAST | 42,434,858 | 10.4% |
| LOAD_FAST | 22,629,119 | 5.6% |
| RETURN_VALUE | 10,298,580 | 2.5% |
| POP_TOP | 9,766,356 | 2.4% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 165,992,088 | 69.6% |
| LOAD_ATTR_METHOD_LAZY_DICT | 53,193,872 | 22.3% |
| LOAD_ATTR | 17,339,157 | 7.3% |
| LOAD_FAST__LOAD_FAST | 1,558,920 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 392,739 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 51,746,412 | 21.7% |
| POP_JUMP_IF_FALSE | 44,998,812 | 18.9% |
| GET_ITER | 43,108,206 | 18.1% |
| STORE_FAST | 27,145,969 | 11.4% |
| LOAD_GLOBAL_MODULE | 18,682,140 | 7.8% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,513,821 | 76.8% |
| CALL | 19,488,267 | 9.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.2% |
| LOAD_GLOBAL_MODULE | 6,146,340 | 2.8% |
| RETURN_VALUE | 3,658,089 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 103,216,379 | 47.6% |
| BINARY_OP | 72,002,140 | 33.2% |
| RETURN_VALUE | 17,462,220 | 8.0% |
| STORE_FAST | 6,524,940 | 3.0% |
| LOAD_FAST | 5,318,760 | 2.5% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,407,142 | 79.3% |
| RETURN_VALUE | 6,551,140 | 11.7% |
| LOAD_FAST__LOAD_FAST | 2,400,000 | 4.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,800 | 2.2% |
| BINARY_SUBSCR_LIST_INT | 1,211,520 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 10,852,320 | 19.4% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 19.4% |
| STORE_FAST__LOAD_FAST | 9,079,680 | 16.2% |
| YIELD_VALUE | 7,682,400 | 13.7% |
| BINARY_OP_ADD_UNICODE | 4,820,800 | 8.6% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,250,090 | 58.6% |
| RETURN_GENERATOR | 5,396,980 | 20.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,465,666 | 13.3% |
| LOAD_ATTR_SLOT | 1,098,692 | 4.2% |
| CALL | 436,580 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,315,160 | 55.0% |
| BINARY_OP | 3,468,346 | 13.3% |
| BUILD_TUPLE | 2,902,412 | 11.2% |
| YIELD_VALUE | 2,419,200 | 9.3% |
| STORE_FAST__LOAD_FAST | 645,120 | 2.5% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 389,714,958 | 99.1% |
| LOAD_CONST | 3,657,358 | 0.9% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 249,581,595 | 63.4% |
| STORE_FAST | 44,101,110 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 41,897,344 | 10.7% |
| IS_OP | 25,804,058 | 6.6% |
| LOAD_GLOBAL_MODULE | 13,606,680 | 3.5% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 760,850,602 | 30.7% |
| LOAD_FAST__LOAD_FAST | 663,925,490 | 26.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 402,222,283 | 16.2% |
| LOAD_ATTR_METHOD_NO_DICT | 124,732,842 | 5.0% |
| GET_ITER | 113,271,150 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,232,714,013 | 90.0% |
| RETURN_GENERATOR | 126,797,214 | 5.1% |
| COPY_FREE_VARS | 93,989,492 | 3.8% |
| MAKE_CELL | 26,452,975 | 1.1% |
| CALL_PY_EXACT_ARGS | 1,170,042 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,111,637 | 58.1% |
| LOAD_ATTR_METHOD_NO_DICT | 13,652,121 | 8.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,558,057 | 8.2% |
| LOAD_ATTR | 7,297,160 | 4.8% |
| LOAD_FAST__LOAD_FAST | 4,821,599 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 143,120,675 | 93.4% |
| COPY_FREE_VARS | 4,954,328 | 3.2% |
| RETURN_GENERATOR | 3,419,820 | 2.2% |
| MAKE_CELL | 1,705,373 | 1.1% |
| CALL_PY_EXACT_ARGS | 87,800 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 16,291,566 | 93.9% |
| BUILD_TUPLE | 518,236 | 3.0% |
| LOAD_GLOBAL_MODULE | 496,658 | 2.9% |
| LOAD_ATTR_MODULE | 50,640 | 0.3% |
| LOAD_FAST | 1,200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 17,358,180 | 100.0% |
| EXTENDED_ARG | 120 | 0.0% |


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

### COMPARE_AND_BRANCH

<details>
<summary> Successors and predecessors for COMPARE_AND_BRANCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 53,901,447 | 37.7% |
| LOAD_FAST | 50,384,322 | 35.2% |
| LOAD_ATTR | 8,879,407 | 6.2% |
| LOAD_FAST__LOAD_CONST | 6,212,248 | 4.3% |
| LOAD_GLOBAL_MODULE | 4,708,012 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,726,062 | 25.7% |
| JUMP_BACKWARD | 29,984,133 | 21.0% |
| RETURN_CONST | 25,018,409 | 17.5% |
| LOAD_FAST__LOAD_FAST | 19,525,860 | 13.6% |
| LOAD_GLOBAL_MODULE | 10,663,174 | 7.5% |


</details>

### COMPARE_AND_BRANCH_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_AND_BRANCH_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 23,382,660 | 37.7% |
| LOAD_ATTR_SLOT | 17,999,820 | 29.0% |
| LOAD_FAST | 6,292,967 | 10.1% |
| LOAD_CONST | 6,004,560 | 9.7% |
| LOAD_GLOBAL_MODULE | 3,632,090 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 29,182,500 | 47.1% |
| LOAD_FAST | 21,277,139 | 34.3% |
| LOAD_GLOBAL_MODULE | 6,026,760 | 9.7% |
| LOAD_FAST__LOAD_CONST | 4,722,780 | 7.6% |
| PUSH_NULL | 381,329 | 0.6% |


</details>

### COMPARE_AND_BRANCH_INT

<details>
<summary> Successors and predecessors for COMPARE_AND_BRANCH_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 342,511,572 | 25.4% |
| LOAD_FAST__LOAD_CONST | 262,905,968 | 19.5% |
| LOAD_FAST | 178,445,447 | 13.2% |
| LOAD_ATTR_INSTANCE_VALUE | 168,140,479 | 12.5% |
| COPY | 102,867,180 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 552,265,904 | 41.0% |
| LOAD_FAST__LOAD_FAST | 178,875,599 | 13.3% |
| LOAD_FAST__LOAD_CONST | 156,786,996 | 11.6% |
| JUMP_BACKWARD | 115,805,974 | 8.6% |
| JUMP_FORWARD | 96,327,120 | 7.1% |


</details>

### COMPARE_AND_BRANCH_STR

<details>
<summary> Successors and predecessors for COMPARE_AND_BRANCH_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 35,704,860 | 39.4% |
| LOAD_FAST__LOAD_CONST | 27,924,372 | 30.8% |
| LOAD_FAST | 16,736,284 | 18.5% |
| LOAD_ATTR_INSTANCE_VALUE | 2,498,700 | 2.8% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,445,500 | 24.8% |
| LOAD_FAST__LOAD_CONST | 18,212,040 | 20.1% |
| LOAD_GLOBAL_MODULE | 16,681,572 | 18.4% |
| JUMP_BACKWARD | 9,115,983 | 10.1% |
| LOAD_GLOBAL_BUILTIN | 9,108,852 | 10.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 89,899,774 | 45.8% |
| LOAD_CONST | 36,330,691 | 18.5% |
| LOAD_FAST__LOAD_FAST | 19,163,518 | 9.8% |
| LOAD_FAST | 12,476,716 | 6.4% |
| CALL_NO_KW_LEN | 10,420,980 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 119,068,526 | 60.7% |
| EXTENDED_ARG | 18,807,590 | 9.6% |
| JUMP_IF_FALSE_OR_POP | 12,062,021 | 6.1% |
| LOAD_FAST | 10,600,320 | 5.4% |
| BINARY_OP | 9,899,520 | 5.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 266,981,980 | 36.1% |
| LOAD_FAST__LOAD_FAST | 148,996,293 | 20.1% |
| LOAD_FAST | 142,001,932 | 19.2% |
| LOAD_CONST__LOAD_FAST | 66,590,160 | 9.0% |
| LOAD_ATTR_INSTANCE_VALUE | 43,002,604 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 657,775,993 | 88.9% |
| POP_JUMP_IF_TRUE | 68,230,957 | 9.2% |
| RETURN_VALUE | 5,895,720 | 0.8% |
| EXTENDED_ARG | 3,834,660 | 0.5% |
| JUMP_IF_FALSE_OR_POP | 1,460,640 | 0.2% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 270,086,400 | 33.3% |
| LOAD_FAST | 134,302,839 | 16.5% |
| SWAP | 128,776,500 | 15.9% |
| LOAD_FAST__LOAD_FAST | 101,528,340 | 12.5% |
| LOAD_FAST__LOAD_CONST | 78,469,140 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 270,086,400 | 33.3% |
| BINARY_SUBSCR_LIST_INT | 158,997,820 | 19.6% |
| BINARY_SUBSCR | 109,568,220 | 13.5% |
| COMPARE_AND_BRANCH_INT | 102,867,180 | 12.7% |
| LOAD_ATTR_INSTANCE_VALUE | 66,090,550 | 8.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,989,492 | 62.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 37,754,556 | 25.0% |
| CALL | 10,250,296 | 6.8% |
| CALL_PY_WITH_DEFAULTS | 4,954,328 | 3.3% |
| LOAD_ATTR_PROPERTY | 3,939,026 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 209,900,128 | 77.3% |
| RETURN_GENERATOR | 61,661,636 | 22.7% |
| MAKE_CELL | 118,279 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,615,091 | 100.0% |
| LOAD_DEREF | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,717,074 | 78.0% |
| NOP | 1,746,820 | 20.3% |
| RETURN_CONST | 150,237 | 1.7% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |
| LOAD_CONST | 60 | 0.0% |


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
| FOR_ITER | 958,080 | 71.1% |
| STORE_FAST | 222,840 | 16.5% |
| CALL | 81,000 | 6.0% |
| POP_EXCEPT | 18,000 | 1.3% |
| STORE_ATTR_INSTANCE_VALUE | 18,000 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 483,540 | 35.9% |
| BUILD_LIST | 479,040 | 35.6% |
| RERAISE | 151,140 | 11.2% |
| RETURN_VALUE | 138,600 | 10.3% |
| RETURN_CONST | 36,000 | 2.7% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 72,992,280 | 55.3% |
| BUILD_SLICE | 53,117,100 | 40.2% |
| LOAD_FAST__LOAD_CONST | 5,558,460 | 4.2% |
| LOAD_FAST | 296,339 | 0.2% |
| CALL | 20,637 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 54,070,500 | 41.0% |
| LOAD_FAST | 26,757,000 | 20.3% |
| LOAD_FAST__LOAD_FAST | 26,382,660 | 20.0% |
| LOAD_CONST | 18,042,359 | 13.7% |
| JUMP_FORWARD | 5,280,960 | 4.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,886,182 | 98.4% |
| LOAD_DEREF | 236,378 | 0.8% |
| LOAD_ATTR_INSTANCE_VALUE | 167,882 | 0.5% |
| RETURN_VALUE | 50,880 | 0.2% |
| BUILD_CONST_KEY_MAP | 16,320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 31,383,142 | 100.0% |


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
| JUMP_BACKWARD | 3,932,100 | 65.5% |
| RETURN_CONST | 2,067,900 | 34.5% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 38,658,990 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 37,036,860 | 95.8% |
| RETURN_CONST | 920,100 | 2.4% |
| LOAD_FAST | 414,690 | 1.1% |
| LOAD_FAST__LOAD_FAST | 93,840 | 0.2% |
| RETURN_VALUE | 80,040 | 0.2% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| <252> | 99,358,740 | 27.8% |
| JUMP_BACKWARD | 75,951,188 | 21.2% |
| LOAD_FAST | 35,153,820 | 9.8% |
| STORE_FAST__LOAD_FAST | 32,913,420 | 9.2% |
| CALL_NO_KW_LIST_APPEND | 29,348,688 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 57,630,249 | 22.3% |
| FOR_ITER_LIST | 49,984,220 | 19.4% |
| POP_JUMP_IF_NONE | 37,259,810 | 14.4% |
| POP_JUMP_IF_FALSE | 32,440,597 | 12.6% |
| POP_JUMP_IF_NOT_NONE | 30,172,920 | 11.7% |


</details>

### FORMAT_VALUE

<details>
<summary> Successors and predecessors for FORMAT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 51,072,060 | 46.0% |
| LOAD_FAST__LOAD_FAST | 36,024,720 | 32.4% |
| LOAD_ATTR | 13,027,440 | 11.7% |
| LOAD_FAST | 3,107,820 | 2.8% |
| RETURN_VALUE | 2,535,719 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 51,397,560 | 46.3% |
| BUILD_STRING | 49,705,680 | 44.8% |
| LOAD_CONST | 6,745,380 | 6.1% |
| LOAD_FAST | 3,198,180 | 2.9% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 273,153,211 | 72.0% |
| GET_ITER | 70,009,282 | 18.5% |
| LOAD_FAST | 21,406,714 | 5.6% |
| EXTENDED_ARG | 14,489,696 | 3.8% |
| FOR_ITER | 144,398 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 202,805,821 | 53.5% |
| STORE_FAST__LOAD_FAST | 69,728,854 | 18.4% |
| STORE_FAST | 24,304,676 | 6.4% |
| LOAD_FAST | 20,190,832 | 5.3% |
| RETURN_CONST | 19,600,791 | 5.2% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 63,733,800 | 49.7% |
| GET_ITER | 38,319,471 | 29.9% |
| EXTENDED_ARG | 26,083,460 | 20.3% |
| LOAD_FAST | 185,320 | 0.1% |
| FOR_ITER | 2,860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 89,384,100 | 69.7% |
| POP_TOP | 38,787,111 | 30.2% |
| STORE_FAST__LOAD_FAST | 63,160 | 0.0% |
| JUMP_FORWARD | 55,200 | 0.0% |
| RETURN_VALUE | 30,520 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 918,748,777 | 73.6% |
| GET_ITER | 197,918,711 | 15.9% |
| LOAD_FAST | 80,258,418 | 6.4% |
| EXTENDED_ARG | 49,984,220 | 4.0% |
| FOR_ITER_TUPLE | 1,244,486 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 484,732,438 | 38.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 319,417,627 | 25.6% |
| STORE_FAST | 171,950,863 | 13.8% |
| RETURN_CONST | 107,253,990 | 8.6% |
| LOAD_FAST | 68,321,269 | 5.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 429,290,292 | 92.5% |
| GET_ITER | 25,531,151 | 5.5% |
| LOAD_FAST | 6,810,360 | 1.5% |
| EXTENDED_ARG | 2,475,480 | 0.5% |
| FOR_ITER_LIST | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 161,028,878 | 34.7% |
| LOAD_FAST | 81,927,340 | 17.7% |
| LOAD_DEREF | 64,789,749 | 14.0% |
| LOAD_CONST__LOAD_FAST | 55,903,320 | 12.0% |
| PUSH_NULL | 29,574,433 | 6.4% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 205,203,840 | 69.0% |
| GET_ITER | 84,963,166 | 28.6% |
| LOAD_FAST | 4,611,478 | 1.6% |
| EXTENDED_ARG | 1,370,880 | 0.5% |
| FOR_ITER_LIST | 1,237,852 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 149,934,647 | 50.4% |
| STORE_FAST | 55,879,772 | 18.8% |
| LOAD_FAST__LOAD_FAST | 40,052,360 | 13.5% |
| LOAD_FAST | 27,486,191 | 9.2% |
| RETURN_CONST | 12,812,480 | 4.3% |


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
| RETURN_GENERATOR | 77,837,900 | 92.8% |
| LOAD_FAST | 3,303,060 | 3.9% |
| CALL_FUNCTION_EX | 2,239,620 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 249,240 | 0.3% |
| RETURN_VALUE | 207,120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 83,837,120 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 100,528,397 | 18.3% |
| LOAD_FAST | 80,844,704 | 14.7% |
| LOAD_ATTR_INSTANCE_VALUE | 79,795,491 | 14.5% |
| RETURN_VALUE | 56,990,326 | 10.4% |
| CALL_BUILTIN_CLASS | 45,920,134 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 197,918,711 | 36.1% |
| CALL_PY_EXACT_ARGS | 113,271,150 | 20.7% |
| FOR_ITER_TUPLE | 84,963,166 | 15.5% |
| FOR_ITER | 70,009,282 | 12.8% |
| FOR_ITER_GEN | 38,319,471 | 7.0% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 6,000,480 | 62.8% |
| RETURN_GENERATOR | 3,389,724 | 35.4% |
| BINARY_SUBSCR | 132,060 | 1.4% |
| LOAD_ATTR_SLOT | 33,120 | 0.3% |
| LOAD_FAST | 7,080 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,562,464 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 8,315,244 | 87.0% |
| STORE_FAST | 1,106,235 | 11.6% |
| STORE_DEREF | 136,430 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,000,804 | 83.7% |
| STORE_DEREF | 1,557,105 | 16.3% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,342,124 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 8,315,244 | 99.7% |
| STORE_FAST__LOAD_FAST | 24,240 | 0.3% |
| STORE_FAST | 2,040 | 0.0% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 596,688,102 | 36.4% |
| RETURN_CONST | 525,363,713 | 32.0% |
| RETURN_VALUE | 503,999,252 | 30.7% |
| RETURN_GENERATOR | 14,360,980 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 228,958,388 | 34.4% |
| LOAD_GLOBAL_MODULE | 177,156,719 | 26.7% |
| LOAD_FAST | 79,123,514 | 11.9% |
| LOAD_FAST__LOAD_FAST | 63,246,510 | 9.5% |
| LOAD_GLOBAL_BUILTIN | 44,298,264 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 577,208,265 | 86.8% |
| POP_JUMP_IF_TRUE | 57,615,472 | 8.7% |
| STORE_FAST__LOAD_FAST | 12,173,460 | 1.8% |
| YIELD_VALUE | 9,984,899 | 1.5% |
| RETURN_VALUE | 3,210,360 | 0.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 738,694,480 | 31.3% |
| POP_JUMP_IF_TRUE | 356,486,880 | 15.1% |
| POP_JUMP_IF_FALSE | 184,080,222 | 7.8% |
| STORE_FAST | 178,424,044 | 7.6% |
| LIST_APPEND | 117,809,025 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 918,748,777 | 39.0% |
| FOR_ITER_RANGE | 429,290,292 | 18.2% |
| FOR_ITER | 273,153,211 | 11.6% |
| FOR_ITER_TUPLE | 205,203,840 | 8.7% |
| LOAD_FAST__LOAD_FAST | 107,852,520 | 4.6% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 125,850,056 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 125,850,056 | 100.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 151,480,207 | 33.9% |
| COMPARE_AND_BRANCH_INT | 96,327,120 | 21.6% |
| POP_TOP | 58,401,480 | 13.1% |
| POP_JUMP_IF_FALSE | 25,037,260 | 5.6% |
| JUMP_FORWARD | 23,968,740 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 156,326,240 | 35.0% |
| LOAD_FAST__LOAD_FAST | 78,609,599 | 17.6% |
| LOAD_CONST__LOAD_FAST | 36,260,640 | 8.1% |
| LOAD_FAST__LOAD_CONST | 29,456,850 | 6.6% |
| LOAD_GLOBAL_BUILTIN | 25,642,852 | 5.7% |


</details>

### JUMP_IF_FALSE_OR_POP

<details>
<summary> Successors and predecessors for JUMP_IF_FALSE_OR_POP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 77,685,880 | 52.5% |
| UNARY_NOT | 15,265,190 | 10.3% |
| LOAD_ATTR_INSTANCE_VALUE | 14,784,532 | 10.0% |
| CALL_NO_KW_BUILTIN_FAST | 13,519,860 | 9.1% |
| COMPARE_OP | 12,062,021 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 104,821,343 | 70.9% |
| RETURN_VALUE | 34,115,860 | 23.1% |
| LOAD_GLOBAL_BUILTIN | 3,574,840 | 2.4% |
| STORE_FAST__LOAD_FAST | 1,601,700 | 1.1% |
| LOAD_GLOBAL_MODULE | 1,580,500 | 1.1% |


</details>

### JUMP_IF_TRUE_OR_POP

<details>
<summary> Successors and predecessors for JUMP_IF_TRUE_OR_POP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 13,843,922 | 25.2% |
| LOAD_FAST | 12,236,831 | 22.3% |
| COMPARE_OP | 9,473,572 | 17.3% |
| LOAD_ATTR | 7,388,292 | 13.5% |
| RETURN_CONST | 2,773,792 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,197,617 | 62.3% |
| RETURN_VALUE | 8,594,640 | 15.7% |
| STORE_FAST__LOAD_FAST | 3,738,919 | 6.8% |
| LOAD_CONST__LOAD_FAST | 1,410,120 | 2.6% |
| LOAD_GLOBAL_BUILTIN | 1,238,760 | 2.3% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 43,013,745 | 22.8% |
| LOAD_CONST | 42,797,067 | 22.7% |
| LOAD_FAST | 29,770,520 | 15.8% |
| LOAD_GLOBAL_MODULE | 18,506,380 | 9.8% |
| LOAD_ATTR_INSTANCE_VALUE | 15,392,220 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 162,975,108 | 86.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,469,840 | 13.0% |
| CALL_BUILTIN_CLASS | 1,174,820 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 23,272,548 | 19.7% |
| RETURN_VALUE | 22,168,457 | 18.8% |
| BINARY_OP | 20,608,680 | 17.5% |
| LOAD_FAST | 15,913,324 | 13.5% |
| RETURN_GENERATOR | 13,436,700 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 117,809,025 | 99.9% |
| LOAD_DEREF | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 36,359,655 | 73.5% |
| LOAD_FAST | 12,403,260 | 25.1% |
| LOAD_CONST | 367,320 | 0.7% |
| RETURN_VALUE | 210,919 | 0.4% |
| LOAD_DEREF | 78,000 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 48,723,296 | 98.5% |
| STORE_FAST | 172,680 | 0.3% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| LOAD_FAST | 165,619 | 0.3% |
| STORE_FAST__LOAD_FAST | 165,319 | 0.3% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 485,930,296 | 36.3% |
| LOAD_GLOBAL_BUILTIN | 221,414,717 | 16.5% |
| STORE_FAST__LOAD_FAST | 159,443,522 | 11.9% |
| CALL_BUILTIN_CLASS | 111,879,777 | 8.4% |
| LOAD_GLOBAL_MODULE | 101,730,934 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 283,776,953 | 21.2% |
| IS_OP | 228,958,388 | 17.1% |
| STORE_FAST__LOAD_FAST | 144,942,832 | 10.8% |
| LOAD_FAST__LOAD_FAST | 142,704,960 | 10.7% |
| POP_JUMP_IF_FALSE | 61,864,375 | 4.6% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 93,305,626 | 82.1% |
| LOAD_GLOBAL_BUILTIN | 15,500,160 | 13.6% |
| LOAD_FAST | 2,579,140 | 2.3% |
| LOAD_ATTR_MODULE | 1,894,500 | 1.7% |
| STORE_FAST__LOAD_FAST | 179,500 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_AND_BRANCH_INT | 56,413,440 | 49.7% |
| LOAD_FAST | 23,496,156 | 20.7% |
| LOAD_FAST__LOAD_FAST | 16,266,900 | 14.3% |
| COMPARE_OP | 3,286,560 | 2.9% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.5% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,804,352,819 | 79.5% |
| STORE_FAST__LOAD_FAST | 242,567,849 | 6.9% |
| LOAD_FAST__LOAD_FAST | 234,838,779 | 6.7% |
| COPY | 66,090,550 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 59,332,158 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,020,310,135 | 28.9% |
| POP_JUMP_IF_FALSE | 543,299,751 | 15.4% |
| LOAD_ATTR_METHOD_NO_DICT | 181,086,332 | 5.1% |
| RETURN_VALUE | 171,593,132 | 4.9% |
| STORE_FAST__LOAD_FAST | 170,939,234 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,785,458 | 60.1% |
| LOAD_ATTR_INSTANCE_VALUE | 36,685,880 | 25.4% |
| STORE_FAST__LOAD_FAST | 20,720,240 | 14.3% |
| LOAD_CONST__LOAD_FAST | 155,606 | 0.1% |
| LOAD_DEREF | 74,483 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,330,952 | 39.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 53,193,872 | 36.8% |
| CALL | 27,028,100 | 18.7% |
| LOAD_CONST | 5,260,020 | 3.6% |
| LOAD_FAST__LOAD_FAST | 1,305,960 | 0.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 503,237,835 | 37.4% |
| STORE_FAST__LOAD_FAST | 308,898,664 | 23.0% |
| LOAD_ATTR_INSTANCE_VALUE | 181,086,332 | 13.5% |
| LOAD_GLOBAL_MODULE | 55,128,989 | 4.1% |
| LOAD_FAST__LOAD_CONST | 54,128,280 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 611,308,551 | 45.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 165,992,088 | 12.4% |
| LOAD_CONST | 135,335,976 | 10.1% |
| LOAD_FAST__LOAD_FAST | 129,465,184 | 9.6% |
| CALL_PY_EXACT_ARGS | 124,732,842 | 9.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,099,388,742 | 64.1% |
| STORE_FAST__LOAD_FAST | 389,252,857 | 22.7% |
| LOAD_ATTR_INSTANCE_VALUE | 70,819,185 | 4.1% |
| LOAD_ATTR_SLOT | 45,766,735 | 2.7% |
| LOAD_DEREF | 32,439,098 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 612,113,127 | 35.7% |
| LOAD_FAST | 546,448,155 | 31.8% |
| CALL_PY_EXACT_ARGS | 402,222,283 | 23.4% |
| LOAD_GLOBAL_MODULE | 48,509,352 | 2.8% |
| LOAD_CONST__LOAD_FAST | 31,056,120 | 1.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 336,574,536 | 93.1% |
| LOAD_ATTR_MODULE | 11,695,000 | 3.2% |
| LOAD_ATTR | 6,904,551 | 1.9% |
| LOAD_FAST | 3,267,180 | 0.9% |
| LOAD_ATTR_CLASS | 1,887,220 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,010,364 | 34.6% |
| LOAD_FAST__LOAD_FAST | 100,547,658 | 27.8% |
| CALL | 30,480,141 | 8.4% |
| CALL_NO_KW_ISINSTANCE | 27,920,400 | 7.7% |
| LOAD_GLOBAL_BUILTIN | 12,459,760 | 3.4% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,129,476 | 62.7% |
| STORE_FAST__LOAD_FAST | 14,311,748 | 21.8% |
| LOAD_ATTR_SLOT | 5,110,975 | 7.8% |
| RETURN_VALUE | 1,738,224 | 2.6% |
| LOAD_DEREF | 1,222,618 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 51,194,453 | 78.0% |
| POP_JUMP_IF_FALSE | 4,163,339 | 6.3% |
| COPY_FREE_VARS | 3,939,026 | 6.0% |
| GET_ITER | 1,452,235 | 2.2% |
| MAKE_CELL | 1,340,676 | 2.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,113,190,902 | 79.0% |
| STORE_FAST__LOAD_FAST | 168,196,245 | 11.9% |
| LOAD_ATTR_SLOT | 41,112,308 | 2.9% |
| COPY | 40,164,120 | 2.9% |
| LOAD_DEREF | 16,015,380 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,966,999 | 22.8% |
| POP_JUMP_IF_FALSE | 150,709,622 | 10.7% |
| COMPARE_OP | 89,899,774 | 6.4% |
| LOAD_ATTR | 85,206,786 | 6.0% |
| STORE_FAST__LOAD_FAST | 58,615,046 | 4.2% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 186,560,160 | 57.4% |
| STORE_FAST__LOAD_FAST | 72,981,880 | 22.5% |
| LOAD_ATTR_WITH_HINT | 22,464,780 | 6.9% |
| LOAD_ATTR_INSTANCE_VALUE | 22,337,200 | 6.9% |
| COPY | 12,970,260 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,478,660 | 24.1% |
| STORE_FAST__LOAD_FAST | 42,224,640 | 13.0% |
| COMPARE_AND_BRANCH_INT | 33,680,160 | 10.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 32,090,540 | 9.9% |
| LOAD_CONST | 27,880,560 | 8.6% |


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

### LOAD_CLASSDEREF

<details>
<summary> Successors and predecessors for LOAD_CLASSDEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CLASSDEREF | 1,200 | 46.5% |
| PUSH_NULL | 1,200 | 46.5% |
| LOAD_NAME | 180 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CLASSDEREF | 1,200 | 46.5% |
| CALL_PY_EXACT_ARGS | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_CLOSURE

<details>
<summary> Successors and predecessors for LOAD_CLOSURE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 61,127,636 | 64.5% |
| LOAD_CLOSURE | 15,939,022 | 16.8% |
| POP_JUMP_IF_TRUE | 3,118,929 | 3.3% |
| LOAD_ATTR_MODULE | 2,239,500 | 2.4% |
| RESUME | 1,952,582 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 78,802,557 | 83.2% |
| LOAD_CLOSURE | 15,939,022 | 16.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 458,880,644 | 11.5% |
| STORE_FAST__LOAD_FAST | 455,549,994 | 11.4% |
| LOAD_FAST__LOAD_FAST | 381,507,445 | 9.6% |
| LOAD_FAST__LOAD_CONST | 292,555,858 | 7.3% |
| BINARY_SUBSCR_LIST_INT | 193,145,340 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 458,880,644 | 11.5% |
| BINARY_OP_ADD_INT | 426,340,975 | 10.7% |
| COMPARE_AND_BRANCH_INT | 342,511,572 | 8.6% |
| STORE_FAST | 314,339,492 | 7.9% |
| CALL_NO_KW_BUILTIN_FAST | 290,713,216 | 7.3% |


</details>

### LOAD_CONST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_CONST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 216,538,887 | 21.9% |
| POP_JUMP_IF_FALSE | 170,382,036 | 17.2% |
| RESUME | 142,133,878 | 14.4% |
| STORE_ATTR_INSTANCE_VALUE | 65,366,021 | 6.6% |
| FOR_ITER_RANGE | 55,903,320 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 282,953,589 | 28.6% |
| LOAD_FAST | 202,427,172 | 20.4% |
| STORE_ATTR_INSTANCE_VALUE | 106,229,195 | 10.7% |
| SWAP | 78,935,460 | 8.0% |
| CONTAINS_OP | 66,590,160 | 6.7% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 228,580,203 | 25.0% |
| STORE_FAST | 96,909,280 | 10.6% |
| FOR_ITER_RANGE | 64,789,749 | 7.1% |
| PUSH_NULL | 56,084,932 | 6.1% |
| LOAD_FAST | 38,804,632 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 472,217,636 | 51.6% |
| LOAD_ATTR | 78,594,902 | 8.6% |
| LOAD_CONST | 61,361,332 | 6.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 32,439,098 | 3.5% |
| LOAD_ATTR_INSTANCE_VALUE | 32,163,849 | 3.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,320,703,152 | 13.6% |
| RESUME | 1,925,883,997 | 11.3% |
| POP_JUMP_IF_FALSE | 1,812,281,334 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,020,310,135 | 6.0% |
| STORE_FAST__LOAD_FAST | 770,079,852 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,804,352,819 | 16.5% |
| LOAD_ATTR_SLOT | 1,113,190,902 | 6.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,099,388,742 | 6.5% |
| LOAD_GLOBAL_BUILTIN | 977,007,535 | 5.7% |
| CALL_PY_EXACT_ARGS | 760,850,602 | 4.5% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,085,900 | 37.2% |
| LOAD_ATTR_METHOD_NO_DICT | 1,231,560 | 22.0% |
| POP_JUMP_IF_NONE | 1,203,206 | 21.5% |
| LOAD_GLOBAL_BUILTIN | 456,660 | 8.2% |
| POP_JUMP_IF_FALSE | 282,720 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 1,506,240 | 26.9% |
| CALL_NO_KW_LIST_APPEND | 1,165,440 | 20.8% |
| LOAD_FAST | 1,042,320 | 18.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 7.7% |
| LOAD_ATTR_METHOD_NO_DICT | 219,620 | 3.9% |


</details>

### LOAD_FAST__LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 304,009,822 | 14.8% |
| PUSH_NULL | 181,067,940 | 8.8% |
| LOAD_GLOBAL_MODULE | 163,214,614 | 8.0% |
| COMPARE_AND_BRANCH_INT | 156,786,996 | 7.7% |
| POP_JUMP_IF_FALSE | 121,266,369 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 360,354,120 | 17.6% |
| LOAD_CONST | 292,555,858 | 14.3% |
| COMPARE_AND_BRANCH_INT | 262,905,968 | 12.8% |
| BINARY_OP_SUBTRACT_INT | 145,266,656 | 7.1% |
| BINARY_SUBSCR_TUPLE_INT | 135,604,737 | 6.6% |


</details>

### LOAD_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 643,273,240 | 11.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 612,113,127 | 10.7% |
| PUSH_NULL | 480,221,317 | 8.4% |
| POP_JUMP_IF_FALSE | 313,760,796 | 5.5% |
| RESUME | 313,232,292 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 663,925,490 | 11.6% |
| LOAD_FAST__LOAD_FAST | 643,273,240 | 11.2% |
| STORE_ATTR_SLOT | 502,486,525 | 8.7% |
| LOAD_CONST | 381,507,445 | 6.6% |
| LOAD_FAST | 364,546,512 | 6.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,284,080 | 49.8% |
| COMPARE_AND_BRANCH | 7,283,705 | 49.8% |
| STORE_FAST | 8,013 | 0.1% |
| RESUME | 7,629 | 0.1% |
| POP_JUMP_IF_FALSE | 3,719 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,567,063 | 99.6% |
| LOAD_GLOBAL_MODULE | 33,911 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 15,301 | 0.1% |
| LOAD_ATTR | 1,881 | 0.0% |
| LOAD_GLOBAL | 175 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 977,007,535 | 24.2% |
| POP_JUMP_IF_FALSE | 889,891,093 | 22.0% |
| RESUME | 883,951,863 | 21.9% |
| STORE_FAST | 525,378,399 | 13.0% |
| POP_JUMP_IF_NOT_NONE | 123,863,490 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,320,703,152 | 57.5% |
| CALL_NO_KW_BUILTIN_FAST | 435,765,640 | 10.8% |
| LOAD_FAST__LOAD_CONST | 304,009,822 | 7.5% |
| CALL_NO_KW_ISINSTANCE | 222,863,939 | 5.5% |
| LOAD_ATTR | 221,414,717 | 5.5% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 571,199,784 | 22.4% |
| STORE_FAST__LOAD_FAST | 340,327,823 | 13.3% |
| RESUME | 280,745,661 | 11.0% |
| STORE_FAST | 261,905,706 | 10.3% |
| POP_JUMP_IF_FALSE | 139,076,149 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 367,535,482 | 14.4% |
| LOAD_ATTR_MODULE | 336,574,536 | 13.2% |
| CONTAINS_OP | 266,981,980 | 10.5% |
| LOAD_FAST | 266,616,023 | 10.4% |
| LOAD_FAST__LOAD_FAST | 237,540,205 | 9.3% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,680,900 | 52.0% |
| LOAD_NAME | 4,320,720 | 48.0% |
| RESUME | 1,320 | 0.0% |
| STORE_NAME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,320,720 | 48.0% |
| LOAD_CONST | 4,320,720 | 48.0% |
| PUSH_NULL | 360,000 | 4.0% |
| STORE_NAME | 1,320 | 0.0% |
| LOAD_CLASSDEREF | 180 | 0.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 67,491,159 | 60.4% |
| CALL_PY_EXACT_ARGS | 26,452,975 | 23.7% |
| CALL | 12,533,600 | 11.2% |
| CALL_PY_WITH_DEFAULTS | 1,705,373 | 1.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,383,181 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 67,491,159 | 55.8% |
| RESUME | 39,503,822 | 32.6% |
| RETURN_GENERATOR | 14,019,840 | 11.6% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 121,902,536 | 99.2% |
| LOAD_FAST__LOAD_CONST | 1,036,260 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,117,621 | 71.7% |
| LOAD_FAST__LOAD_CONST | 11,844,449 | 9.6% |
| LOAD_GLOBAL_BUILTIN | 6,739,336 | 5.5% |
| LOAD_GLOBAL_MODULE | 5,383,846 | 4.4% |
| STORE_FAST | 3,420,976 | 2.8% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,836,160 | 41.9% |
| RETURN_VALUE | 6,247,620 | 16.5% |
| LOAD_FAST__LOAD_FAST | 6,156,598 | 16.3% |
| JUMP_FORWARD | 4,782,720 | 12.7% |
| CALL_BUILTIN_CLASS | 2,461,560 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 20,584,800 | 54.5% |
| JUMP_BACKWARD | 15,973,318 | 42.3% |
| CALL_FUNCTION_EX | 1,211,400 | 3.2% |
| LOAD_CONST | 5,940 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 175,674,210 | 34.8% |
| STORE_FAST | 72,798,202 | 14.4% |
| POP_JUMP_IF_FALSE | 56,152,815 | 11.1% |
| STORE_ATTR_INSTANCE_VALUE | 51,434,123 | 10.2% |
| JUMP_BACKWARD | 40,771,789 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 266,031,815 | 52.7% |
| LOAD_FAST__LOAD_FAST | 73,815,662 | 14.6% |
| PUSH_NULL | 51,345,417 | 10.2% |
| LOAD_GLOBAL_BUILTIN | 33,223,302 | 6.6% |
| LOAD_CONST__LOAD_FAST | 19,662,406 | 3.9% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,548,271 | 48.1% |
| SWAP | 3,544,674 | 20.0% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.3% |
| COPY | 1,817,700 | 10.2% |
| STORE_FAST | 544,080 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,362,581 | 52.7% |
| RETURN_VALUE | 3,487,074 | 19.6% |
| JUMP_FORWARD | 2,235,420 | 12.6% |
| RERAISE | 1,817,700 | 10.2% |
| LOAD_FAST | 342,540 | 1.9% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 657,775,993 | 16.0% |
| IS_OP | 577,208,265 | 14.0% |
| CALL_NO_KW_ISINSTANCE | 556,101,887 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 543,299,751 | 13.2% |
| CALL_NO_KW_BUILTIN_FAST | 472,883,749 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,812,281,334 | 44.1% |
| LOAD_GLOBAL_BUILTIN | 889,891,093 | 21.6% |
| LOAD_FAST__LOAD_FAST | 313,760,796 | 7.6% |
| RETURN_CONST | 197,270,528 | 4.8% |
| JUMP_BACKWARD | 184,080,222 | 4.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 158,616,494 | 46.0% |
| LOAD_FAST | 65,802,756 | 19.1% |
| EXTENDED_ARG | 37,259,810 | 10.8% |
| LOAD_ATTR_SLOT | 25,233,420 | 7.3% |
| LOAD_ATTR | 23,643,920 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 110,932,875 | 32.2% |
| PUSH_NULL | 62,776,313 | 18.2% |
| LOAD_FAST__LOAD_CONST | 36,369,129 | 10.5% |
| JUMP_BACKWARD | 29,137,908 | 8.4% |
| LOAD_DEREF | 27,409,140 | 7.9% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 250,025,313 | 53.4% |
| STORE_FAST__LOAD_FAST | 134,153,977 | 28.6% |
| EXTENDED_ARG | 30,172,920 | 6.4% |
| LOAD_ATTR_INSTANCE_VALUE | 24,768,719 | 5.3% |
| LOAD_ATTR | 17,733,508 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 156,937,844 | 33.5% |
| LOAD_GLOBAL_BUILTIN | 123,863,490 | 26.4% |
| LOAD_FAST__LOAD_FAST | 67,557,064 | 14.4% |
| LOAD_GLOBAL_MODULE | 36,474,907 | 7.8% |
| NOP | 18,375,115 | 3.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540,530,310 | 46.0% |
| STORE_FAST__LOAD_FAST | 179,173,657 | 15.3% |
| CALL_NO_KW_ISINSTANCE | 121,437,148 | 10.3% |
| CONTAINS_OP | 68,230,957 | 5.8% |
| IS_OP | 57,615,472 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 482,901,967 | 41.1% |
| JUMP_BACKWARD | 356,486,880 | 30.4% |
| LOAD_GLOBAL_BUILTIN | 95,795,207 | 8.2% |
| LOAD_CONST | 61,916,094 | 5.3% |
| NOP | 34,776,132 | 3.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 552,962,961 | 27.1% |
| RETURN_CONST | 547,699,176 | 26.9% |
| CALL_NO_KW_BUILTIN_O | 386,831,391 | 19.0% |
| RETURN_VALUE | 109,796,276 | 5.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 103,216,379 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 738,694,480 | 33.3% |
| LOAD_FAST | 621,570,097 | 28.0% |
| RESUME | 221,022,930 | 10.0% |
| RETURN_CONST | 170,497,557 | 7.7% |
| LOAD_FAST__LOAD_FAST | 106,539,069 | 4.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,603,407 | 31.6% |
| LOAD_ATTR | 3,317,322 | 18.7% |
| LOAD_ATTR_SLOT | 2,067,300 | 11.7% |
| CALL_NO_KW_BUILTIN_FAST | 1,822,360 | 10.3% |
| RERAISE | 1,716,000 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 16,454,781 | 92.7% |
| LOAD_GLOBAL_MODULE | 877,878 | 4.9% |
| LOAD_FAST | 388,140 | 2.2% |
| WITH_EXCEPT_START | 36,000 | 0.2% |
| LOAD_CONST | 1,440 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,346,309 | 32.6% |
| POP_JUMP_IF_FALSE | 80,571,159 | 9.1% |
| POP_TOP | 79,748,664 | 9.0% |
| POP_JUMP_IF_NONE | 62,776,313 | 7.1% |
| NOP | 51,345,417 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 480,221,317 | 54.4% |
| LOAD_FAST__LOAD_CONST | 181,067,940 | 20.5% |
| LOAD_FAST | 152,789,285 | 17.3% |
| LOAD_DEREF | 56,084,932 | 6.4% |
| LOAD_GLOBAL_BUILTIN | 5,562,250 | 0.6% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 658,020 | 29.2% |
| LOAD_ATTR_MODULE | 583,740 | 25.9% |
| LOAD_GLOBAL_BUILTIN | 559,560 | 24.8% |
| CALL | 186,098 | 8.3% |
| LOAD_FAST | 152,400 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,078,680 | 48.2% |
| PUSH_EXC_INFO | 1,006,058 | 45.0% |
| LOAD_CONST | 151,140 | 6.8% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 1,817,700 | 70.2% |
| POP_TOP | 386,940 | 14.9% |
| POP_JUMP_IF_FALSE | 154,860 | 6.0% |
| DELETE_FAST | 151,140 | 5.8% |
| CALL_INTRINSIC_1 | 41,400 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,716,000 | 69.0% |
| COPY | 730,380 | 29.4% |
| CALL_INTRINSIC_1 | 41,160 | 1.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,232,714,013 | 63.6% |
| POP_TOP | 221,022,930 | 6.3% |
| COPY_FREE_VARS | 209,900,128 | 6.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 188,772,494 | 5.4% |
| CALL | 186,952,857 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,925,883,997 | 39.9% |
| LOAD_GLOBAL_BUILTIN | 883,951,863 | 18.3% |
| POP_TOP | 552,962,961 | 11.5% |
| LOAD_FAST__LOAD_FAST | 313,232,292 | 6.5% |
| LOAD_GLOBAL_MODULE | 280,745,661 | 5.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 242,975,169 | 18.2% |
| POP_JUMP_IF_FALSE | 197,270,528 | 14.7% |
| STORE_ATTR_INSTANCE_VALUE | 184,880,573 | 13.8% |
| POP_TOP | 170,497,557 | 12.7% |
| RESUME | 129,947,446 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 547,699,176 | 40.9% |
| INTERPRETER_EXIT | 525,363,713 | 39.3% |
| LOAD_FAST | 52,452,120 | 3.9% |
| POP_JUMP_IF_FALSE | 50,858,576 | 3.8% |
| RETURN_VALUE | 49,790,709 | 3.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 126,797,214 | 61.3% |
| COPY_FREE_VARS | 61,661,636 | 29.8% |
| MAKE_CELL | 14,019,840 | 6.8% |
| CALL_PY_WITH_DEFAULTS | 3,419,820 | 1.7% |
| CALL | 789,540 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 77,837,900 | 35.2% |
| GET_ITER | 37,931,880 | 17.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,032,100 | 14.9% |
| CALL | 15,622,820 | 7.1% |
| INTERPRETER_EXIT | 14,360,980 | 6.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,338,399 | 22.9% |
| RETURN_VALUE | 438,918,179 | 15.7% |
| BUILD_TUPLE | 337,650,531 | 12.1% |
| LOAD_ATTR_INSTANCE_VALUE | 171,593,132 | 6.1% |
| COMPARE_OP | 119,068,526 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 503,999,252 | 18.0% |
| RETURN_VALUE | 438,918,179 | 15.7% |
| STORE_FAST__LOAD_FAST | 314,364,512 | 11.2% |
| UNPACK_SEQUENCE_TUPLE | 240,156,909 | 8.6% |
| LOAD_FAST | 213,064,337 | 7.6% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 193,536,344 | 60.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 125,850,056 | 39.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 125,866,100 | 39.4% |
| STORE_FAST__LOAD_FAST | 88,512,240 | 27.7% |
| POP_TOP | 30,022,980 | 9.4% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 9.1% |
| BINARY_OP_ADD_INT | 29,134,080 | 9.1% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 92.5% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 4.0% |
| STORE_FAST__LOAD_FAST | 48,000 | 1.5% |
| LOAD_FAST | 31,380 | 1.0% |
| BINARY_SUBSCR_LIST_INT | 17,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,114,300 | 100.0% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_AND_BRANCH | 16,320 | 97.8% |
| STORE_FAST | 240 | 1.4% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.7% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,317,200 | 32.0% |
| LOAD_CONST__LOAD_FAST | 17,052,085 | 29.7% |
| LOAD_FAST__LOAD_FAST | 14,243,844 | 24.8% |
| CALL | 5,419,260 | 9.5% |
| SWAP | 1,379,066 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,427,101 | 28.7% |
| LOAD_DEREF | 13,449,060 | 23.5% |
| RETURN_CONST | 11,515,226 | 20.1% |
| JUMP_BACKWARD | 5,554,200 | 9.7% |
| LOAD_FAST__LOAD_FAST | 4,982,538 | 8.7% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 321,894,292 | 39.7% |
| LOAD_FAST | 242,518,353 | 29.9% |
| LOAD_CONST__LOAD_FAST | 106,229,195 | 13.1% |
| SWAP | 66,090,550 | 8.1% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 265,735,344 | 32.7% |
| RETURN_CONST | 184,880,573 | 22.8% |
| LOAD_FAST__LOAD_FAST | 173,968,606 | 21.4% |
| LOAD_CONST__LOAD_FAST | 65,366,021 | 8.1% |
| NOP | 51,434,123 | 6.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 502,486,525 | 47.8% |
| LOAD_CONST__LOAD_FAST | 282,953,589 | 26.9% |
| LOAD_FAST | 221,411,544 | 21.1% |
| SWAP | 40,164,120 | 3.8% |
| STORE_ATTR_SLOT | 2,140,335 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 281,273,627 | 26.8% |
| RETURN_CONST | 242,975,169 | 23.1% |
| LOAD_FAST | 241,313,039 | 23.0% |
| LOAD_CONST__LOAD_FAST | 216,538,887 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 24,870,620 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,342,428 | 42.4% |
| SWAP | 12,970,260 | 25.8% |
| LOAD_FAST__LOAD_FAST | 11,671,820 | 23.2% |
| LOAD_CONST__LOAD_FAST | 4,058,300 | 8.1% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,447,437 | 66.5% |
| JUMP_BACKWARD | 5,307,540 | 10.6% |
| RETURN_CONST | 4,207,960 | 8.4% |
| LOAD_CONST__LOAD_FAST | 3,665,340 | 7.3% |
| LOAD_FAST__LOAD_FAST | 2,307,900 | 4.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 27,675,600 | 41.6% |
| LOAD_CONST | 8,746,320 | 13.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,169,040 | 10.8% |
| RETURN_VALUE | 3,731,286 | 5.6% |
| CALL | 3,375,369 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 18,353,961 | 27.6% |
| LOAD_FAST__LOAD_FAST | 13,438,200 | 20.2% |
| LOAD_FAST | 8,760,539 | 13.2% |
| LOAD_CONST | 6,911,340 | 10.4% |
| STORE_FAST__LOAD_FAST | 6,144,600 | 9.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 314,339,492 | 15.6% |
| CALL_NO_KW_BUILTIN_FAST | 222,602,540 | 11.1% |
| STORE_FAST__STORE_FAST | 213,446,340 | 10.6% |
| FOR_ITER_LIST | 171,950,863 | 8.6% |
| RETURN_VALUE | 158,724,944 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 525,378,399 | 26.1% |
| PUSH_NULL | 287,346,309 | 14.3% |
| LOAD_GLOBAL_MODULE | 261,905,706 | 13.0% |
| JUMP_BACKWARD | 178,424,044 | 8.9% |
| LOAD_CONST | 174,405,636 | 8.7% |


</details>

### STORE_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 484,732,438 | 11.1% |
| RETURN_VALUE | 314,364,512 | 7.2% |
| CALL | 291,836,626 | 6.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 286,214,576 | 6.5% |
| CALL_NO_KW_TYPE_1 | 249,581,595 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 770,079,852 | 17.7% |
| LOAD_CONST | 455,549,994 | 10.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 389,252,857 | 9.0% |
| POP_JUMP_IF_FALSE | 366,854,685 | 8.5% |
| LOAD_GLOBAL_MODULE | 340,327,823 | 7.8% |


</details>

### STORE_FAST__STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 822,937,620 | 40.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 586,841,960 | 29.2% |
| UNPACK_SEQUENCE_TUPLE | 391,869,089 | 19.5% |
| UNPACK_SEQUENCE_LIST | 140,351,889 | 7.0% |
| LOAD_ATTR_SLOT | 45,908,040 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 822,937,620 | 40.9% |
| LOAD_FAST | 445,218,527 | 22.2% |
| LOAD_DEREF | 228,580,203 | 11.4% |
| STORE_FAST | 213,446,340 | 10.6% |
| STORE_FAST__LOAD_FAST | 112,467,669 | 5.6% |


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
| RETURN_CONST | 180 | 0.0% |
| BUILD_MAP | 60 | 0.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 1,320 | 25.3% |
| LOAD_CONST | 1,320 | 25.3% |
| LOAD_ATTR | 1,200 | 23.0% |
| MAKE_FUNCTION | 660 | 12.6% |
| IMPORT_NAME | 360 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,100 | 40.2% |
| LOAD_CONST | 1,440 | 27.6% |
| PUSH_NULL | 1,380 | 26.4% |
| LOAD_CLOSURE | 120 | 2.3% |
| STORE_NAME | 120 | 2.3% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,909,740 | 88.3% |
| LOAD_CONST | 13,459,080 | 11.4% |
| LOAD_FAST__LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 103,875,000 | 88.3% |
| RETURN_CONST | 5,855,760 | 5.0% |
| LOAD_FAST__LOAD_FAST | 4,157,040 | 3.5% |
| LOAD_FAST | 3,703,320 | 3.1% |
| JUMP_BACKWARD | 40,320 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 109,576,100 | 33.0% |
| LOAD_FAST | 89,285,281 | 26.8% |
| BINARY_OP_ADD_INT | 41,532,300 | 12.5% |
| LOAD_FAST__LOAD_FAST | 36,634,860 | 11.0% |
| LOAD_FAST__LOAD_CONST | 36,065,620 | 10.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,475,280 | 33.8% |
| LOAD_FAST__LOAD_FAST | 104,596,380 | 31.5% |
| RETURN_CONST | 37,815,532 | 11.4% |
| LOAD_GLOBAL_BUILTIN | 27,031,060 | 8.1% |
| LOAD_DEREF | 15,741,300 | 4.7% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 119,747,419 | 64.2% |
| LOAD_FAST__LOAD_FAST | 18,710,277 | 10.0% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.5% |
| LOAD_FAST__LOAD_CONST | 8,221,757 | 4.4% |
| RETURN_VALUE | 8,051,141 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,254,122 | 39.3% |
| LOAD_FAST | 45,292,625 | 24.3% |
| JUMP_BACKWARD | 30,168,417 | 16.2% |
| RETURN_CONST | 17,559,722 | 9.4% |
| LOAD_GLOBAL_MODULE | 7,347,479 | 3.9% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 158,997,820 | 50.0% |
| LOAD_FAST__LOAD_FAST | 53,873,395 | 17.0% |
| LOAD_FAST | 40,428,670 | 12.7% |
| LOAD_FAST__LOAD_CONST | 27,444,000 | 8.6% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 116,881,832 | 36.8% |
| LOAD_FAST__LOAD_FAST | 105,051,913 | 33.1% |
| LOAD_FAST__LOAD_CONST | 87,697,560 | 27.6% |
| RETURN_CONST | 4,685,160 | 1.5% |
| LOAD_FAST | 1,265,480 | 0.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 270,086,400 | 32.1% |
| BINARY_OP_ADD_FLOAT | 116,255,040 | 13.8% |
| LOAD_CONST__LOAD_FAST | 78,935,460 | 9.4% |
| BINARY_OP_ADD_INT | 76,919,273 | 9.2% |
| BINARY_OP_SUBTRACT_INT | 68,066,499 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 270,086,400 | 32.1% |
| STORE_SUBSCR_LIST_INT | 158,997,820 | 18.9% |
| COPY | 128,776,500 | 15.3% |
| STORE_SUBSCR | 109,576,100 | 13.0% |
| STORE_ATTR_INSTANCE_VALUE | 66,090,550 | 7.9% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,477,628 | 88.3% |
| LOAD_ATTR_MODULE | 894,997 | 7.5% |
| LOAD_ATTR | 355,410 | 3.0% |
| LOAD_FAST | 122,040 | 1.0% |
| LOAD_FAST__LOAD_FAST | 17,100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,867,175 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 110,875,678 | 91.2% |
| LOAD_GLOBAL_MODULE | 3,059,150 | 2.5% |
| LOAD_FAST | 2,939,729 | 2.4% |
| LOAD_CONST__LOAD_FAST | 2,197,860 | 1.8% |
| BINARY_SUBSCR_TUPLE_INT | 1,205,640 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 79,368,240 | 65.2% |
| BINARY_SUBSCR_LIST_INT | 26,768,580 | 22.0% |
| CALL_PY_EXACT_ARGS | 3,191,160 | 2.6% |
| STORE_SUBSCR | 2,419,140 | 2.0% |
| BINARY_SUBSCR | 2,419,140 | 2.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 16,889,260 | 36.3% |
| LOAD_FAST | 12,811,554 | 27.5% |
| CALL_NO_KW_ISINSTANCE | 8,059,540 | 17.3% |
| COMPARE_OP | 2,531,429 | 5.4% |
| STORE_FAST__LOAD_FAST | 2,427,609 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 15,883,722 | 34.1% |
| JUMP_IF_FALSE_OR_POP | 15,265,190 | 32.8% |
| KW_NAMES | 10,565,620 | 22.7% |
| JUMP_IF_TRUE_OR_POP | 1,666,800 | 3.6% |
| STORE_FAST | 1,049,900 | 2.3% |


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
| STORE_FAST__LOAD_FAST | 170,968 | 42.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 96,120 | 23.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,940 | 16.9% |
| COPY | 19,920 | 5.0% |
| RETURN_VALUE | 18,660 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 300,943 | 74.9% |
| STORE_FAST | 96,000 | 23.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,880 | 0.7% |
| UNPACK_SEQUENCE | 1,010 | 0.3% |
| UNPACK_SEQUENCE_TUPLE | 700 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,505,729 | 70.1% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,001,080 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 889,800 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 140,351,889 | 99.9% |
| STORE_DEREF | 83,340 | 0.1% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 240,156,909 | 56.2% |
| LOAD_FAST | 103,278,550 | 24.2% |
| YIELD_VALUE | 25,090,720 | 5.9% |
| BINARY_SUBSCR_DICT | 14,268,900 | 3.3% |
| STORE_FAST | 12,341,280 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 391,869,089 | 91.7% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.6% |
| STORE_FAST | 6,003,000 | 1.4% |
| STORE_FAST__LOAD_FAST | 4,943,606 | 1.2% |
| LOAD_FAST | 290,520 | 0.1% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 319,417,627 | 51.8% |
| FOR_ITER | 202,805,821 | 32.9% |
| LOAD_FAST | 36,686,710 | 5.9% |
| RETURN_VALUE | 25,760,848 | 4.2% |
| BINARY_SUBSCR_LIST_INT | 15,010,342 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 586,841,960 | 95.1% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 1.9% |
| STORE_FAST__LOAD_FAST | 9,187,080 | 1.5% |
| STORE_DEREF | 7,169,040 | 1.2% |
| LOAD_FAST | 922,740 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 36,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 36,000 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.7% |
| SEND | 125,866,100 | 18.3% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.7% |
| LOAD_FAST | 40,682,902 | 5.9% |
| STORE_FAST__LOAD_FAST | 33,558,540 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 596,688,102 | 87.0% |
| STORE_FAST__LOAD_FAST | 48,146,681 | 7.0% |
| UNPACK_SEQUENCE_TUPLE | 25,090,720 | 3.7% |
| STORE_FAST | 12,307,740 | 1.8% |
| STORE_DEREF | 2,419,200 | 0.4% |


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
| specialization.deferred |   1116964416 | 40.1% |
| specialization.deopt |        77040 | 0.0% |
|          hit |   1660883418 | 59.7% |
|         miss |      4094812 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 79,138 | 21.3% |
| Failure | 292,405 | 78.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 112,980 | 38.6% |
| other | 86,626 | 29.6% |
| out of range | 25,800 | 8.8% |
| list slice | 25,520 | 8.7% |
| buffer int | 19,600 | 6.7% |
| string int | 17,160 | 5.9% |
| sequence int | 3,119 | 1.1% |
| code complex parameters | 1,340 | 0.5% |
| buffer slice | 180 | 0.1% |
| tuple slice | 60 | 0.0% |
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
| specialization.deferred |    332456856 | 39.7% |
| specialization.deopt |           40 | 0.0% |
|          hit |    504258061 | 60.3% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,065 | 1.2% |
| Failure | 88,960 | 98.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 51.3% |
| dict subclass no override | 22,000 | 24.7% |
| py simple | 14,380 | 16.2% |
| bytearray int | 5,200 | 5.8% |
| out of range | 1,020 | 1.1% |
| other | 680 | 0.8% |
| list slice | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |       397303 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1182000923 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 51,760 | 98.1% |
| Failure | 1,010 | 1.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 730 | 72.3% |
| iterator | 200 | 19.8% |
| other | 80 | 7.9% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    379058082 | 15.1% |
| specialization.deopt |      2508671 | 0.1% |
|          hit |   2005032688 | 79.7% |
|         miss |    132965628 | 5.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,509,492 | 93.7% |
| Failure | 168,771 | 6.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 62,357 | 36.9% |
| enumerate | 24,705 | 14.6% |
| other | 19,500 | 11.6% |
| set | 16,249 | 9.6% |
| seq iter | 15,120 | 9.0% |
| dict keys | 7,180 | 4.3% |
| zip | 7,020 | 4.2% |
| dict values | 5,180 | 3.1% |
| reversed list | 4,540 | 2.7% |
| itertools | 3,000 | 1.8% |
| ascii string | 2,820 | 1.7% |
| range | 500 | 0.3% |
| map | 420 | 0.2% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |
| string | 20 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     57264270 | 2.9% |
| specialization.deopt |      3354015 | 0.2% |
|          hit |   1734887322 | 88.1% |
|         miss |    177769311 | 9.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,370,580 | 98.7% |
| Failure | 43,816 | 1.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,820 | 40.7% |
| not managed dict | 8,390 | 19.1% |
| not in dict | 7,920 | 18.1% |
| overriding descriptor | 5,420 | 12.4% |
| property | 1,060 | 2.4% |
| not in keys | 940 | 2.1% |
| non object slot | 920 | 2.1% |
| overridden | 746 | 1.7% |
| no dict | 360 | 0.8% |
| method | 240 | 0.5% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1338030090 | 12.9% |
| specialization.deopt |      9404845 | 0.1% |
|          hit |   8506162659 | 82.2% |
|         miss |    498937617 | 4.8% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,461,814 | 84.2% |
| Failure | 1,778,345 | 15.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 621,875 | 35.0% |
| class attr simple | 602,027 | 33.9% |
| not managed dict | 287,317 | 16.2% |
| metaclass attribute | 115,034 | 6.5% |
| method | 58,855 | 3.3% |
| overridden | 42,292 | 2.4% |
| mutable class | 20,088 | 1.1% |
| class method obj | 11,903 | 0.7% |
| non object slot | 7,280 | 0.4% |
| non overriding descriptor | 4,008 | 0.2% |
| class attr descriptor | 2,740 | 0.2% |
| shadowed | 2,006 | 0.1% |
| not in keys | 1,680 | 0.1% |
| builtin class method | 840 | 0.0% |
| module attr not found | 400 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    196209152 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     14569479 | 0.2% |
| specialization.deopt |          389 | 0.0% |
|          hit |   6590243392 | 99.8% |
|         miss |        23505 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 49,601 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    857564918 | 19.7% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   3462446571 | 79.4% |
|         miss |     37779860 | 0.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,861 | 39.1% |
| Failure | 1,117,353 | 60.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,325 | 51.8% |
| multiply different types | 173,818 | 15.6% |
| add different types | 152,768 | 13.7% |
| remainder | 33,800 | 3.0% |
| floor divide | 32,640 | 2.9% |
| add other | 26,946 | 2.4% |
| and int | 26,017 | 2.3% |
| lshift | 18,700 | 1.7% |
| rshift | 17,561 | 1.6% |
| true divide different types | 15,300 | 1.4% |
| xor | 10,740 | 1.0% |
| subtract other | 8,320 | 0.7% |
| true divide float | 6,640 | 0.6% |
| or | 5,506 | 0.5% |
| power | 4,480 | 0.4% |
| multiply other | 2,560 | 0.2% |
| true divide other | 1,120 | 0.1% |
| and other | 1,012 | 0.1% |
| and different types | 100 | 0.0% |


</details>

### COMPARE_AND_BRANCH

<details>
<summary> specialization stats for COMPARE_AND_BRANCH family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    142969523 | 8.7% |
| specialization.deopt |        24204 | 0.0% |
|          hit |   1498753798 | 91.2% |
|         miss |      1285156 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 28,225 | 19.6% |
| Failure | 115,576 | 80.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 51,318 | 44.4% |
| different types | 29,278 | 25.3% |
| float long | 8,905 | 7.7% |
| baseobject | 7,922 | 6.9% |
| set | 6,823 | 5.9% |
| other | 4,040 | 3.5% |
| tuple | 3,434 | 3.0% |
| bool | 1,776 | 1.5% |
| bytes | 940 | 0.8% |
| list | 900 | 0.8% |
| long float | 160 | 0.1% |
| string | 80 | 0.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    958553974 | 10.8% |
| specialization.deopt |      3539328 | 0.0% |
|          hit |   7696103877 | 87.0% |
|         miss |    187699120 | 2.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,584,133 | 89.0% |
| Failure | 444,488 | 11.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| python class | 106,650 | 24.0% |
| meth descr method fastcall keywords | 67,320 | 15.1% |
| kwnames | 57,496 | 12.9% |
| code complex parameters | 50,651 | 11.4% |
| class no vectorcall | 33,726 | 7.6% |
| cfunc varargs keywords | 25,288 | 5.7% |
| class mutable | 24,851 | 5.6% |
| cfunc noargs | 22,820 | 5.1% |
| meth descr varargs | 18,856 | 4.2% |
| other | 9,979 | 2.2% |
| meth descr varargs keywords | 8,142 | 1.8% |
| bound method | 6,809 | 1.5% |
| cmethod | 4,480 | 1.0% |
| cfunc varargs | 3,780 | 0.9% |
| method wrapper | 1,740 | 0.4% |
| str | 1,260 | 0.3% |
| operator wrapper | 640 | 0.1% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 70,942,399,620 | 63.2% |
| Not specialized | 6,722,383,500 | 6.0% |
| Specialized | 34,612,381,156 | 30.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 1,338,030,090 | 24.8% |
| BINARY_SUBSCR | 1,116,964,416 | 20.7% |
| CALL | 958,553,974 | 17.8% |
| BINARY_OP | 857,564,918 | 15.9% |
| FOR_ITER | 379,058,082 | 7.0% |
| STORE_SUBSCR | 332,456,856 | 6.2% |
| COMPARE_OP | 196,209,152 | 3.6% |
| COMPARE_AND_BRANCH | 142,969,523 | 2.7% |
| STORE_ATTR | 57,264,270 | 1.1% |
| LOAD_GLOBAL | 14,569,479 | 0.3% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 184,406,072 | 17.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 151,667,197 | 14.5% |
| STORE_ATTR_SLOT | 113,427,166 | 10.9% |
| CALL_PY_EXACT_ARGS | 94,164,795 | 9.0% |
| LOAD_ATTR_SLOT | 86,896,530 | 8.3% |
| FOR_ITER_LIST | 66,550,862 | 6.4% |
| FOR_ITER_TUPLE | 66,210,166 | 6.3% |
| STORE_ATTR_INSTANCE_VALUE | 63,354,360 | 6.1% |
| LOAD_ATTR_METHOD_NO_DICT | 57,250,397 | 5.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 32,992,523 | 3.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,642,732,517 | 32.5% |
| Calls to Python functions inlined | 3,404,083,084 | 67.5% |
| Calls via PyEval_EvalFrame (total) | 1,642,732,517 | 32.5% |
| Calls via PyEval_EvalFrame (vector) | 871,026,381 | 17.3% |
| Calls via PyEval_EvalFrame (generator) | 771,706,136 | 15.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,964,560 | 0.1% |
| Calls via PyEval_EvalFrame (function vectorcall) | 867,060,501 | 17.2% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 206,981,083 | 4.1% |
| Calls via PyEval_EvalFrame (function ex) | 22,167,058 | 0.4% |
| Calls via PyEval_EvalFrame (api) | 172,365,166 | 3.4% |
| Calls via PyEval_EvalFrame (method) | 60,614,714 | 1.2% |
| Frames pushed | 4,146,954,574 | 82.2% |
| Frame objects created | 46,307,821 | 0.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 5,096,265,619 | 42.9% |
| Frees to freelist | 5,100,112,005 |  |
| Allocations | 6,776,580,442 | 57.1% |
| Allocations to 512 bytes | 6,700,323,799 | 56.4% |
| Allocations to 4 kbytes | 65,797,218 | 0.6% |
| Allocations over 4 kbytes | 10,459,425 | 0.1% |
| Frees | 7,025,768,356 |  |
| New values | 134,862,779 |  |
| Interpreter increfs | 80,761,166,531 | 67.2% |
| Interpreter decrefs | 92,235,117,723 | 70.3% |
| Increfs | 39,493,207,000 | 32.8% |
| Decrefs | 38,992,540,388 | 29.7% |
| Materialize dict (on request) | 3,699,120 | 2.7% |
| Materialize dict (new key) | 58,320 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 2,032,503,049 |  |
| Method cache misses | 98,623,496 |  |
| Method cache collisions | 109,318,251 |  |
| Method cache dunder hits | 2,477,967,940 |  |
| Method cache dunder misses | 10,949,636 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,643 |


</details>

---
Stats gathered on: 2023-02-10
