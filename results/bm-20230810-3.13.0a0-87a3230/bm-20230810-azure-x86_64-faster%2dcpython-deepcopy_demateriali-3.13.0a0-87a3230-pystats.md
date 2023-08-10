
# Pystats results

- fork: faster-cpython
- ref: deepcopy-dematerialize
- commit hash: 87a3230
- commit date: 2023-08-10T01:42:21+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 28,091,311,985 | 18.8% | 18.8% |  |
| STORE_FAST | 9,850,116,150 | 6.6% | 25.4% |  |
| LOAD_CONST | 9,593,244,956 | 6.4% | 31.9% |  |
| POP_JUMP_IF_FALSE | 8,445,503,026 | 5.7% | 37.5% |  |
| LOAD_FAST_LOAD_FAST | 8,025,199,048 | 5.4% | 42.9% |  |
| RESUME | 4,989,022,391 | 3.3% | 46.3% |  |
| LOAD_GLOBAL_BUILTIN | 4,135,774,438 | 2.8% | 49.0% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,784,949,162 | 2.5% | 51.6% | 5.7% |
| TO_BOOL_BOOL | 3,237,223,562 | 2.2% | 53.7% | 0.0% |
| JUMP_BACKWARD | 3,212,767,856 | 2.2% | 55.9% |  |
| RETURN_VALUE | 3,011,311,204 | 2.0% | 57.9% |  |
| LOAD_GLOBAL_MODULE | 2,891,235,268 | 1.9% | 59.8% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,836,136,710 | 1.9% | 61.7% | 3.2% |
| POP_TOP | 2,358,663,857 | 1.6% | 63.3% |  |
| BINARY_OP_ADD_INT | 2,226,201,863 | 1.5% | 64.8% | 0.0% |
| CONTAINS_OP | 1,983,036,462 | 1.3% | 66.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,892,123,481 | 1.3% | 67.4% | 8.8% |
| COMPARE_OP_STR | 1,590,659,615 | 1.1% | 68.5% | 0.0% |
| STORE_FAST_STORE_FAST | 1,542,734,118 | 1.0% | 69.5% |  |
| COMPARE_OP_INT | 1,507,418,573 | 1.0% | 70.5% | 0.1% |
| NOP | 1,497,315,627 | 1.0% | 71.5% |  |
| POP_JUMP_IF_TRUE | 1,475,423,207 | 1.0% | 72.5% |  |
| LOAD_ATTR_SLOT | 1,345,108,528 | 0.9% | 73.4% | 4.3% |
| RETURN_CONST | 1,344,094,338 | 0.9% | 74.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,337,589,959 | 0.9% | 75.2% | 3.4% |
| BINARY_SUBSCR_STR_INT | 1,239,946,580 | 0.8% | 76.1% | 0.0% |
| FOR_ITER_LIST | 1,239,543,331 | 0.8% | 76.9% | 5.3% |
| INTERPRETER_EXIT | 1,210,083,937 | 0.8% | 77.7% |  |
| BINARY_SUBSCR | 1,111,328,645 | 0.7% | 78.4% |  |
| PUSH_NULL | 1,082,004,464 | 0.7% | 79.2% |  |
| COPY | 1,078,704,110 | 0.7% | 79.9% |  |
| STORE_ATTR_SLOT | 1,062,993,357 | 0.7% | 80.6% | 10.6% |
| LOAD_ATTR | 1,037,493,817 | 0.7% | 81.3% |  |
| SWAP | 934,681,569 | 0.6% | 81.9% |  |
| CALL_NO_KW_BUILTIN_FAST | 933,434,943 | 0.6% | 82.5% | 0.0% |
| CALL | 894,458,753 | 0.6% | 83.1% |  |
| BINARY_SUBSCR_LIST_INT | 880,816,687 | 0.6% | 83.7% | 0.4% |
| LOAD_DEREF | 844,282,740 | 0.6% | 84.3% |  |
| BINARY_OP | 842,119,438 | 0.6% | 84.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 837,771,402 | 0.6% | 85.4% | 9.0% |
| BINARY_OP_MULTIPLY_FLOAT | 827,759,856 | 0.6% | 86.0% | 0.8% |
| CALL_NO_KW_ISINSTANCE | 814,190,516 | 0.5% | 86.5% |  |
| CALL_NO_KW_BUILTIN_O | 785,535,016 | 0.5% | 87.1% | 0.1% |
| YIELD_VALUE | 693,478,880 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 692,905,502 | 0.5% | 88.0% |  |
| BINARY_SUBSCR_DICT | 622,354,181 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 605,524,702 | 0.4% | 88.8% |  |
| GET_ITER | 594,184,283 | 0.4% | 89.2% |  |
| BINARY_OP_SUBTRACT_INT | 500,868,586 | 0.3% | 89.5% | 0.1% |
| FOR_ITER_RANGE | 482,681,074 | 0.3% | 89.9% | 0.0% |
| IS_OP | 460,629,775 | 0.3% | 90.2% |  |
| POP_JUMP_IF_NOT_NONE | 431,276,765 | 0.3% | 90.5% |  |
| UNPACK_SEQUENCE_TUPLE | 425,327,692 | 0.3% | 90.8% | 0.3% |
| JUMP_FORWARD | 423,252,922 | 0.3% | 91.0% |  |
| FOR_ITER_TUPLE | 422,625,381 | 0.3% | 91.3% | 15.5% |
| BINARY_OP_ADD_FLOAT | 391,145,318 | 0.3% | 91.6% | 1.6% |
| TO_BOOL_NONE | 376,323,214 | 0.3% | 91.8% | 10.9% |
| LOAD_ATTR_WITH_HINT | 347,159,678 | 0.2% | 92.1% | 0.5% |
| CALL_NO_KW_LEN | 345,755,769 | 0.2% | 92.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 340,399,450 | 0.2% | 92.5% | 2.0% |
| LOAD_ATTR_MODULE | 339,706,866 | 0.2% | 92.8% | 0.0% |
| CALL_NO_KW_TYPE_1 | 336,035,161 | 0.2% | 93.0% |  |
| STORE_SUBSCR | 316,199,356 | 0.2% | 93.2% |  |
| EXTENDED_ARG | 308,256,850 | 0.2% | 93.4% |  |
| SEND_GEN | 302,368,132 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR_LIST_INT | 302,185,566 | 0.2% | 93.8% | 0.0% |
| BUILD_LIST | 301,082,939 | 0.2% | 94.0% |  |
| POP_JUMP_IF_NONE | 298,711,136 | 0.2% | 94.2% |  |
| FOR_ITER | 293,186,051 | 0.2% | 94.4% |  |
| BINARY_OP_SUBTRACT_FLOAT | 270,375,608 | 0.2% | 94.6% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 266,392,590 | 0.2% | 94.8% | 3.2% |
| COPY_FREE_VARS | 253,256,843 | 0.2% | 94.9% |  |
| BINARY_SLICE | 248,175,132 | 0.2% | 95.1% |  |
| CALL_NO_KW_LIST_APPEND | 239,600,518 | 0.2% | 95.3% | 0.0% |
| RETURN_GENERATOR | 238,829,188 | 0.2% | 95.4% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 236,932,005 | 0.2% | 95.6% | 6.8% |
| TO_BOOL_INT | 228,200,053 | 0.2% | 95.7% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 228,060,468 | 0.2% | 95.9% | 0.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,748,365 | 0.1% | 96.0% |  |
| TO_BOOL | 204,972,704 | 0.1% | 96.2% |  |
| END_SEND | 194,312,951 | 0.1% | 96.3% |  |
| STORE_SUBSCR_DICT | 192,631,202 | 0.1% | 96.4% |  |
| BINARY_SUBSCR_TUPLE_INT | 188,461,818 | 0.1% | 96.5% | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 178,900,933 | 0.1% | 96.7% | 21.3% |
| KW_NAMES | 172,952,996 | 0.1% | 96.8% |  |
| CALL_PY_WITH_DEFAULTS | 170,762,946 | 0.1% | 96.9% | 2.8% |
| BUILD_SLICE | 158,212,228 | 0.1% | 97.0% |  |
| CALL_INTRINSIC_1 | 154,060,527 | 0.1% | 97.1% |  |
| LIST_APPEND | 146,894,246 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,427,947 | 0.1% | 97.3% | 0.0% |
| COMPARE_OP | 145,601,817 | 0.1% | 97.4% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 143,357,602 | 0.1% | 97.5% | 35.5% |
| UNPACK_SEQUENCE_LIST | 140,234,020 | 0.1% | 97.6% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,651,546 | 0.1% | 97.7% | 19.1% |
| STORE_FAST_LOAD_FAST | 136,652,504 | 0.1% | 97.8% |  |
| DELETE_SUBSCR | 127,971,237 | 0.1% | 97.9% |  |
| CALL_BUILTIN_CLASS | 126,620,119 | 0.1% | 97.9% |  |
| UNARY_NEGATIVE | 121,275,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 121,022,669 | 0.1% | 98.1% | 1.1% |
| LOAD_SUPER_ATTR_METHOD | 118,305,387 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,672,076 | 0.1% | 98.3% |  |
| FORMAT_SIMPLE | 117,348,072 | 0.1% | 98.3% |  |
| SEND | 112,732,377 | 0.1% | 98.4% |  |
| TO_BOOL_LIST | 111,941,267 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 111,077,301 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,739,124 | 0.1% | 98.6% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 94,851,404 | 0.1% | 98.8% |  |
| MAKE_CELL | 92,677,173 | 0.1% | 98.8% |  |
| FOR_ITER_GEN | 90,214,980 | 0.1% | 98.9% | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 87,706,379 | 0.1% | 99.0% | 2.0% |
| GET_AWAITABLE | 85,015,307 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 83,759,644 | 0.1% | 99.1% |  |
| CALL_FUNCTION_EX | 83,062,735 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,385,142 | 0.1% | 99.2% | 0.0% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,803,205 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 68,048,022 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 67,241,012 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 67,091,745 | 0.0% | 99.4% |  |
| STORE_DEREF | 65,767,572 | 0.0% | 99.4% |  |
| BUILD_MAP | 60,414,148 | 0.0% | 99.4% |  |
| BUILD_STRING | 59,068,263 | 0.0% | 99.5% |  |
| UNARY_NOT | 58,452,805 | 0.0% | 99.5% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 56,936,074 | 0.0% | 99.6% | 0.0% |
| END_FOR | 56,701,055 | 0.0% | 99.6% |  |
| LIST_EXTEND | 54,348,989 | 0.0% | 99.6% |  |
| STORE_ATTR | 53,543,190 | 0.0% | 99.7% |  |
| LOAD_FAST_AND_CLEAR | 52,301,226 | 0.0% | 99.7% |  |
| STORE_ATTR_WITH_HINT | 50,965,037 | 0.0% | 99.7% | 0.1% |
| LOAD_ATTR_PROPERTY | 48,558,637 | 0.0% | 99.8% | 11.3% |
| MAP_ADD | 41,400,816 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,648,413 | 0.0% | 99.8% |  |
| CALL_NO_KW_TUPLE_1 | 22,406,040 | 0.0% | 99.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 22,351,920 | 0.0% | 99.9% | 0.0% |
| PUSH_EXC_INFO | 17,049,674 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,049,668 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,582,092 | 0.0% | 99.9% |  |
| DICT_MERGE | 16,251,273 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,170,582 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,404,618 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,524,293 | 0.0% | 100.0% |  |
| RERAISE | 8,497,506 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,376,824 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,298,456 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,700 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,924,440 | 0.0% | 100.0% |  |
| BEFORE_WITH | 5,235,017 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 4,634,064 | 0.0% | 100.0% |  |
| SET_ADD | 3,234,120 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 2,897,543 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,298,840 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,989,931 | 0.0% | 100.0% |  |
| BUILD_SET | 1,918,509 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,671,511 | 0.0% | 100.0% |  |
| DELETE_FAST | 626,414 | 0.0% | 100.0% |  |
| UNPACK_EX | 286,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 216,638 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 138,123 | 0.0% | 100.0% |  |
| SET_UPDATE | 66,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 52,096 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,975 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,415 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,395 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,220 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,540 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 834 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 4,902,349,893 | 3.3% | 3.3% |
| STORE_FAST LOAD_FAST | 4,699,442,655 | 3.2% | 6.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,531,388,077 | 3.0% | 9.5% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,208,337,712 | 2.2% | 11.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,666,337,421 | 1.8% | 13.4% |
| CALL_PY_EXACT_ARGS RESUME | 2,522,112,848 | 1.7% | 15.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,359,039,388 | 1.6% | 16.7% |
| RESUME LOAD_FAST | 2,116,939,926 | 1.4% | 18.1% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,870,209,682 | 1.3% | 19.4% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,774,701,574 | 1.2% | 20.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,606,727,802 | 1.1% | 21.6% |
| LOAD_CONST COMPARE_OP_STR | 1,563,963,599 | 1.0% | 22.7% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,550,226,297 | 1.0% | 23.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,340,310,548 | 0.9% | 24.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,270,757,320 | 0.9% | 25.5% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,765,258 | 0.8% | 26.3% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,230,898,276 | 0.8% | 27.1% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_STR_INT | 1,202,362,860 | 0.8% | 27.9% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,191,156,178 | 0.8% | 28.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,101,488,554 | 0.7% | 29.5% |
| LOAD_CONST LOAD_FAST | 1,063,707,584 | 0.7% | 30.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,061,341,176 | 0.7% | 30.9% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,415,960 | 0.7% | 31.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 982,247,925 | 0.7% | 32.2% |
| NOP LOAD_FAST_LOAD_FAST | 959,973,937 | 0.6% | 32.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 949,403,223 | 0.6% | 33.5% |
| JUMP_BACKWARD FOR_ITER_LIST | 924,139,328 | 0.6% | 34.1% |
| POP_TOP LOAD_FAST | 921,341,063 | 0.6% | 34.7% |
| STORE_FAST JUMP_BACKWARD | 918,433,117 | 0.6% | 35.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 893,404,785 | 0.6% | 36.0% |
| RESUME LOAD_GLOBAL_BUILTIN | 846,739,877 | 0.6% | 36.5% |
| BINARY_SUBSCR_STR_INT STORE_FAST | 841,517,940 | 0.6% | 37.1% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,163,842 | 0.5% | 37.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 809,172,131 | 0.5% | 38.2% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 801,047,711 | 0.5% | 38.7% |
| LOAD_FAST LOAD_FAST | 782,202,609 | 0.5% | 39.2% |
| LOAD_FAST RETURN_VALUE | 781,804,286 | 0.5% | 39.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 770,661,495 | 0.5% | 40.3% |
| LOAD_CONST LOAD_CONST | 744,378,463 | 0.5% | 40.8% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 735,447,593 | 0.5% | 41.3% |
| JUMP_BACKWARD NOP | 718,030,409 | 0.5% | 41.8% |
| LOAD_FAST TO_BOOL_BOOL | 715,266,583 | 0.5% | 42.2% |
| STORE_FAST STORE_FAST | 711,188,363 | 0.5% | 42.7% |
| LOAD_CONST COMPARE_OP_INT | 672,613,891 | 0.5% | 43.2% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 665,894,852 | 0.4% | 43.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 663,870,363 | 0.4% | 44.0% |
| POP_TOP JUMP_BACKWARD | 657,946,443 | 0.4% | 44.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 645,525,724 | 0.4% | 44.9% |
| RETURN_VALUE STORE_FAST | 640,179,350 | 0.4% | 45.4% |
| LOAD_FAST PUSH_NULL | 638,211,063 | 0.4% | 45.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 593,722,210 | 0.4% | 46.2% |
| FOR_ITER_LIST STORE_FAST | 587,112,057 | 0.4% | 46.6% |
| LOAD_FAST LOAD_ATTR | 578,687,198 | 0.4% | 47.0% |
| RETURN_CONST POP_TOP | 573,546,284 | 0.4% | 47.3% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 560,431,818 | 0.4% | 47.7% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 540,586,500 | 0.4% | 48.1% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,153,020 | 0.4% | 48.4% |
| PUSH_NULL LOAD_FAST | 535,081,281 | 0.4% | 48.8% |
| LOAD_DEREF LOAD_FAST | 523,688,548 | 0.4% | 49.2% |
| RETURN_VALUE RETURN_VALUE | 518,742,469 | 0.3% | 49.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 515,616,822 | 0.3% | 49.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 512,657,249 | 0.3% | 50.2% |
| LOAD_FAST CONTAINS_OP | 510,851,722 | 0.3% | 50.5% |
| LOAD_FAST STORE_ATTR_SLOT | 504,100,585 | 0.3% | 50.9% |
| BINARY_SUBSCR LOAD_FAST | 490,867,510 | 0.3% | 51.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 485,769,470 | 0.3% | 51.5% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,696,151 | 0.3% | 51.8% |
| RESUME POP_TOP | 472,276,216 | 0.3% | 52.2% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 471,655,345 | 0.3% | 52.5% |
| STORE_FAST_STORE_FAST LOAD_FAST | 465,936,805 | 0.3% | 52.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 459,615,476 | 0.3% | 53.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 452,848,623 | 0.3% | 53.4% |
| YIELD_VALUE INTERPRETER_EXIT | 451,462,932 | 0.3% | 53.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 450,390,544 | 0.3% | 54.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 448,339,618 | 0.3% | 54.3% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 444,392,088 | 0.3% | 54.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 435,698,503 | 0.3% | 54.9% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 55.2% |
| JUMP_BACKWARD FOR_ITER_RANGE | 428,687,156 | 0.3% | 55.5% |
| LOAD_CONST STORE_FAST | 422,829,907 | 0.3% | 55.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 421,929,977 | 0.3% | 56.0% |
| BUILD_TUPLE RETURN_VALUE | 413,115,517 | 0.3% | 56.3% |
| RETURN_CONST INTERPRETER_EXIT | 410,750,433 | 0.3% | 56.6% |
| NOP LOAD_FAST | 402,246,406 | 0.3% | 56.9% |
| FOR_ITER_RANGE STORE_FAST | 396,964,403 | 0.3% | 57.1% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 388,169,340 | 0.3% | 57.4% |
| IS_OP POP_JUMP_IF_FALSE | 384,295,519 | 0.3% | 57.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 378,146,409 | 0.3% | 57.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 368,124,390 | 0.2% | 58.1% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 366,742,862 | 0.2% | 58.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 355,178,041 | 0.2% | 58.6% |
| LOAD_FAST BINARY_SUBSCR | 352,865,649 | 0.2% | 58.9% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 346,540,111 | 0.2% | 59.1% |
| STORE_FAST LOAD_DEREF | 345,218,531 | 0.2% | 59.3% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,716,527 | 0.2% | 59.6% |
| RESUME LOAD_GLOBAL_MODULE | 339,359,777 | 0.2% | 59.8% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 339,141,968 | 0.2% | 60.0% |
| RESUME NOP | 337,447,157 | 0.2% | 60.2% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 334,850,941 | 0.2% | 60.5% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 332,333,621 | 0.2% | 60.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,500 | 91.9% |
| LOAD_ATTR_WITH_HINT | 360 | 4.4% |
| CALL | 180 | 2.2% |
| LOAD_FAST | 120 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 8,160 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,411,950 | 46.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,273,502 | 43.4% |
| LOAD_GLOBAL_MODULE | 210,141 | 4.0% |
| LOAD_ATTR_WITH_HINT | 132,220 | 2.5% |
| LOAD_FAST | 132,060 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,628,418 | 88.4% |
| STORE_FAST | 605,159 | 11.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 249,145,837 | 29.6% |
| LOAD_FAST | 170,133,914 | 20.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.6% |
| LOAD_FAST_LOAD_FAST | 47,866,033 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,906 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 153,731,046 | 18.3% |
| LOAD_FAST | 138,905,402 | 16.5% |
| LOAD_FAST_LOAD_FAST | 106,872,386 | 12.7% |
| LOAD_CONST | 91,367,251 | 10.8% |
| RETURN_VALUE | 69,617,593 | 8.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,109,360 | 72.6% |
| LOAD_FAST | 65,387,566 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,257,186 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,612,886 | 29.8% |
| STORE_FAST | 116,098,581 | 29.7% |
| LOAD_FAST | 59,772,531 | 15.3% |
| RETURN_VALUE | 31,351,200 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,774,701,574 | 79.7% |
| LOAD_FAST | 244,368,373 | 11.0% |
| LOAD_FAST_LOAD_FAST | 94,802,368 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,765,258 | 56.5% |
| LOAD_CONST | 132,770,672 | 6.0% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,092,716 | 4.3% |
| SWAP | 90,618,932 | 4.1% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,035,480 | 47.1% |
| BINARY_SLICE | 15,579,000 | 22.9% |
| LOAD_CONST | 13,078,200 | 19.2% |
| BUILD_STRING | 2,011,200 | 3.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,233,482 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,173,540 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.4% |
| BUILD_TUPLE | 15,457,800 | 22.7% |
| LOAD_CONST | 8,423,340 | 12.4% |
| RETURN_VALUE | 3,047,640 | 4.5% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,590,560 | 43.7% |
| BINARY_SLICE | 1,580,580 | 26.7% |
| RETURN_VALUE | 680,220 | 11.5% |
| BINARY_OP_ADD_UNICODE | 365,380 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,312,520 | 89.7% |
| JUMP_BACKWARD | 511,840 | 8.6% |
| LOAD_CONST | 60,360 | 1.0% |
| LOAD_FAST_LOAD_FAST | 24,300 | 0.4% |
| LOAD_GLOBAL_MODULE | 10,180 | 0.2% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,153,020 | 65.1% |
| LOAD_ATTR_INSTANCE_VALUE | 118,763,280 | 14.3% |
| BINARY_SUBSCR | 67,701,000 | 8.2% |
| LOAD_FAST_LOAD_FAST | 59,229,880 | 7.2% |
| CALL_BUILTIN_CLASS | 12,782,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 284,109,360 | 34.3% |
| YIELD_VALUE | 210,931,680 | 25.5% |
| LOAD_FAST | 111,266,820 | 13.4% |
| BINARY_OP_SUBTRACT_FLOAT | 109,285,680 | 13.2% |
| STORE_FAST | 36,071,920 | 4.4% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 96,092,716 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,997 | 19.2% |
| LOAD_FAST_LOAD_FAST | 44,913,005 | 16.9% |
| LOAD_FAST | 38,771,060 | 14.6% |
| BINARY_OP | 27,332,904 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,212,956 | 23.4% |
| LOAD_CONST | 61,632,729 | 23.1% |
| LOAD_FAST | 47,053,380 | 17.7% |
| LOAD_FAST_LOAD_FAST | 28,244,880 | 10.6% |
| BINARY_OP_ADD_INT | 23,999,760 | 9.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.4% |
| LOAD_FAST | 69,610,876 | 25.7% |
| LOAD_FAST_LOAD_FAST | 36,420,289 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 28,678,572 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,597,409 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.1% |
| SWAP | 55,832,928 | 20.7% |
| LOAD_FAST | 28,366,215 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 366,742,862 | 73.2% |
| LOAD_FAST | 79,048,939 | 15.8% |
| LOAD_FAST_LOAD_FAST | 29,853,974 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 21,635,350 | 4.3% |
| CALL_NO_KW_LEN | 2,724,600 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,033,524 | 19.2% |
| CALL_PY_EXACT_ARGS | 94,404,100 | 18.8% |
| SWAP | 69,254,725 | 13.8% |
| RETURN_VALUE | 40,192,283 | 8.0% |
| BINARY_OP | 37,297,105 | 7.4% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 137,123,048 | 55.3% |
| BINARY_OP_ADD_INT | 40,078,972 | 16.1% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.1% |
| LOAD_FAST | 24,934,392 | 10.0% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 57,269,825 | 23.1% |
| GET_ITER | 33,199,240 | 13.4% |
| CALL_PY_EXACT_ARGS | 25,430,832 | 10.2% |
| BUILD_TUPLE | 24,334,502 | 9.8% |
| LOAD_DEREF | 18,985,680 | 7.7% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 352,865,649 | 31.8% |
| LOAD_FAST_LOAD_FAST | 234,131,542 | 21.1% |
| LOAD_CONST | 133,676,155 | 12.0% |
| COPY | 109,830,040 | 9.9% |
| BUILD_SLICE | 104,833,980 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 490,867,510 | 44.2% |
| STORE_FAST | 136,329,841 | 12.3% |
| LOAD_FAST_LOAD_FAST | 110,182,080 | 9.9% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 6.1% |
| BINARY_SUBSCR | 48,283,064 | 4.3% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,823,133 | 33.2% |
| LOAD_FAST | 205,174,239 | 33.0% |
| LOAD_FAST_LOAD_FAST | 135,594,628 | 21.8% |
| BINARY_SUBSCR | 41,253,852 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,022,027 | 38.1% |
| RETURN_VALUE | 104,205,779 | 16.7% |
| CONTAINS_OP | 77,768,700 | 12.5% |
| LOAD_FAST | 48,674,908 | 7.8% |
| LOAD_ATTR_METHOD_NO_DICT | 41,442,640 | 6.7% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 67,927,140 | 46.4% |
| LOAD_CONST | 41,616,840 | 28.4% |
| BUILD_TUPLE | 28,812,000 | 19.7% |
| LOAD_FAST | 3,533,167 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,060 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,519,687 | 99.4% |
| MAKE_CELL | 705,600 | 0.5% |
| COPY_FREE_VARS | 198,000 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 2,420 | 0.0% |
| CONTAINS_OP | 1,020 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 273,182,795 | 31.0% |
| LOAD_CONST | 180,976,889 | 20.5% |
| COPY | 157,633,500 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,803,608 | 17.6% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,326,247 | 26.8% |
| LOAD_CONST | 192,236,280 | 21.9% |
| LOAD_FAST | 140,923,542 | 16.0% |
| RETURN_VALUE | 90,406,891 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,202,362,860 | 97.0% |
| BINARY_OP_SUBTRACT_INT | 10,639,800 | 0.9% |
| LOAD_ATTR_SLOT | 10,356,180 | 0.8% |
| LOAD_CONST | 6,067,220 | 0.5% |
| LOAD_FAST | 5,008,740 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 841,517,940 | 67.9% |
| LOAD_FAST | 388,169,340 | 31.3% |
| LOAD_CONST | 5,749,800 | 0.5% |
| RETURN_VALUE | 3,711,600 | 0.3% |
| BINARY_OP_INPLACE_ADD_UNICODE | 216,660 | 0.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 148,326,162 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.1% |
| LOAD_FAST_LOAD_FAST | 329,673 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 2,543 | 0.0% |
| BINARY_SUBSCR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,900 | 38.3% |
| LOAD_CONST | 24,654,420 | 13.1% |
| LOAD_FAST | 24,246,875 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.3% |
| STORE_FAST | 8,763,758 | 4.7% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,634,064 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,035,336 | 43.9% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 36.8% |
| STORE_FAST | 383,073 | 8.3% |
| RETURN_VALUE | 144,386 | 3.1% |
| CALL_NO_KW_LIST_APPEND | 132,780 | 2.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,264,963 | 38.6% |
| LOAD_ATTR_SLOT | 38,405,414 | 12.8% |
| SWAP | 32,337,176 | 10.7% |
| LOAD_FAST | 30,548,714 | 10.1% |
| RESUME | 18,139,256 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 129,089,038 | 42.9% |
| LOAD_FAST | 89,948,647 | 29.9% |
| SWAP | 32,373,787 | 10.8% |
| CALL | 9,652,840 | 3.2% |
| RETURN_VALUE | 9,312,438 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,290,249 | 17.0% |
| LOAD_FAST | 8,877,626 | 14.7% |
| CALL_INTRINSIC_1 | 6,535,297 | 10.8% |
| SWAP | 6,077,760 | 10.1% |
| POP_JUMP_IF_FALSE | 4,143,060 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,245,133 | 38.5% |
| STORE_FAST | 20,532,170 | 34.0% |
| SWAP | 6,077,760 | 10.1% |
| CALL_FUNCTION_EX | 3,408,751 | 5.6% |
| LOAD_CONST | 2,982,593 | 4.9% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| LOAD_CONST | 142,320 | 7.4% |
| LOAD_GLOBAL_MODULE | 142,209 | 7.4% |
| LOAD_ATTR | 66,000 | 3.4% |
| LOAD_FAST | 52,920 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| CONTAINS_OP | 141,849 | 7.4% |
| LOAD_CONST | 74,280 | 3.9% |
| BINARY_OP | 68,400 | 3.6% |
| STORE_FAST | 48,240 | 2.5% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,375,215 | 99.5% |
| LOAD_FAST | 781,573 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,980 | 66.3% |
| DELETE_SUBSCR | 53,378,248 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 52,319,974 | 88.6% |
| LOAD_CONST | 6,748,289 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.1% |
| CALL | 12,297,002 | 20.8% |
| STORE_FAST | 4,750,598 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,414,026 | 29.8% |
| LOAD_CONST | 167,606,957 | 24.2% |
| LOAD_FAST_LOAD_FAST | 127,393,480 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 40,170,504 | 5.8% |
| CALL | 38,801,046 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 413,115,517 | 59.6% |
| LOAD_CONST | 82,959,961 | 12.0% |
| CALL_NO_KW_ISINSTANCE | 40,159,168 | 5.8% |
| STORE_FAST | 30,270,936 | 4.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 241,742,867 | 27.0% |
| KW_NAMES | 149,661,307 | 16.7% |
| LOAD_FAST_LOAD_FAST | 91,122,743 | 10.2% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,900 | 8.1% |
| PUSH_NULL | 50,853,122 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 305,143,885 | 34.1% |
| RESUME | 211,832,440 | 23.7% |
| RETURN_VALUE | 51,178,498 | 5.7% |
| POP_TOP | 47,326,686 | 5.3% |
| LOAD_GLOBAL_MODULE | 39,308,545 | 4.4% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,743,422 | 36.6% |
| LOAD_CONST | 23,537,091 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.2% |
| PUSH_NULL | 11,687,465 | 8.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,373,693 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,991,589 | 78.6% |
| COPY_FREE_VARS | 26,910,046 | 19.4% |
| POP_TOP | 2,068,131 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,541 | 0.3% |
| MAKE_CELL | 172,441 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,150,721 | 28.6% |
| CALL_NO_KW_LEN | 23,245,613 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 10,774,234 | 8.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 9,081,146 | 7.2% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,635,554 | 50.3% |
| STORE_FAST | 13,560,625 | 10.7% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.1% |
| LOAD_FAST | 10,271,148 | 8.1% |
| CALL_BUILTIN_CLASS | 4,227,313 | 3.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,880 | 43.2% |
| KW_NAMES | 22,239,889 | 29.1% |
| LOAD_FAST | 12,867,923 | 16.8% |
| LOAD_FAST_LOAD_FAST | 3,304,827 | 4.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,137,420 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,880 | 41.0% |
| STORE_FAST | 27,919,390 | 36.6% |
| POP_TOP | 8,841,035 | 11.6% |
| RETURN_VALUE | 5,704,153 | 7.5% |
| BINARY_OP_ADD_INT | 936,092 | 1.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,162,376 | 52.0% |
| LOAD_FAST | 16,446,639 | 19.8% |
| DICT_MERGE | 16,251,273 | 19.6% |
| BUILD_MAP | 3,408,751 | 4.1% |
| STORE_FAST | 2,240,100 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,287,153 | 56.9% |
| STORE_FAST | 8,429,518 | 10.1% |
| RESUME | 7,497,894 | 9.0% |
| RETURN_VALUE | 6,929,129 | 8.3% |
| MAKE_CELL | 4,745,036 | 5.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 59.7% |
| LIST_EXTEND | 53,531,284 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.1% |
| RERAISE | 42,158 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 61.1% |
| CALL_FUNCTION_EX | 43,162,376 | 28.0% |
| BUILD_MAP | 6,535,297 | 4.2% |
| RERAISE | 6,380,963 | 4.1% |
| LOAD_CONST | 3,820,471 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,944,210 | 72.9% |
| LOAD_FAST | 10,477,146 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,512,516 | 8.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,178,025 | 4.8% |
| LOAD_FAST_LOAD_FAST | 1,043,197 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 70,525,394 | 80.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 7.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,438,080 | 2.8% |
| RETURN_VALUE | 2,242,720 | 2.6% |
| BINARY_OP | 2,010,960 | 2.3% |


</details>

### CALL_NO_KW_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_NO_KW_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 20,210,840 | 29.4% |
| LOAD_GLOBAL_MODULE | 9,492,394 | 13.8% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.0% |
| RETURN_CONST | 7,864,740 | 11.4% |
| BINARY_OP_ADD_FLOAT | 5,101,500 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,393,377 | 95.0% |
| COPY_FREE_VARS | 1,698,248 | 2.5% |
| LOAD_FAST | 1,660,840 | 2.4% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 32,220 | 0.0% |
| STORE_FAST | 13,960 | 0.0% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,160 | 46.6% |
| LOAD_CONST | 339,141,968 | 36.3% |
| LOAD_FAST_LOAD_FAST | 72,136,613 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,378,589 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,696,151 | 51.2% |
| STORE_FAST | 310,640,711 | 33.3% |
| POP_TOP | 47,792,828 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 22,198,599 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560,431,818 | 71.3% |
| LOAD_CONST | 55,891,729 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| BINARY_OP_ADD_UNICODE | 15,909,600 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,716,527 | 43.5% |
| LOAD_CONST | 171,776,242 | 21.9% |
| STORE_FAST | 166,546,889 | 21.2% |
| RETURN_VALUE | 29,452,408 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,260 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 346,540,111 | 42.6% |
| LOAD_GLOBAL_BUILTIN | 331,858,865 | 40.8% |
| LOAD_FAST_LOAD_FAST | 62,973,044 | 7.7% |
| BUILD_TUPLE | 40,159,168 | 4.9% |
| LOAD_ATTR_MODULE | 22,117,150 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 801,047,711 | 98.4% |
| COPY | 6,062,776 | 0.7% |
| RETURN_VALUE | 2,417,569 | 0.3% |
| POP_TOP | 1,996,800 | 0.2% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 217,357,307 | 62.9% |
| LOAD_ATTR_INSTANCE_VALUE | 55,072,533 | 15.9% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 8.5% |
| LOAD_DEREF | 20,449,960 | 5.9% |
| LOAD_ATTR_SLOT | 8,655,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,800,417 | 35.8% |
| LOAD_FAST | 55,705,559 | 16.1% |
| STORE_FAST | 43,158,453 | 12.5% |
| COMPARE_OP_INT | 32,614,412 | 9.4% |
| CALL_BUILTIN_CLASS | 23,245,613 | 6.7% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,300,447 | 72.7% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 18,543,796 | 7.7% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 5,805,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 90,817,545 | 37.9% |
| LOAD_FAST | 72,491,106 | 30.3% |
| EXTENDED_ARG | 27,822,060 | 11.6% |
| RETURN_CONST | 20,554,860 | 8.6% |
| LOAD_CONST | 11,304,038 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,345,958 | 52.4% |
| LOAD_FAST_LOAD_FAST | 56,757,554 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 50,383,433 | 14.8% |
| LOAD_CONST | 27,324,906 | 8.0% |
| LOAD_ATTR_SLOT | 8,567,760 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 249,362,945 | 73.3% |
| LIST_APPEND | 28,917,240 | 8.5% |
| RETURN_VALUE | 11,804,978 | 3.5% |
| LOAD_FAST | 10,857,720 | 3.2% |
| POP_TOP | 9,130,602 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 154,664,160 | 65.3% |
| LOAD_ATTR | 59,472,800 | 25.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,437,067 | 5.7% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,473,581 | 3.2% |
| LOAD_FAST | 1,577,820 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 77,042,446 | 32.5% |
| TO_BOOL_BOOL | 60,236,148 | 25.4% |
| GET_ITER | 33,735,960 | 14.2% |
| LOAD_GLOBAL_MODULE | 18,632,700 | 7.9% |
| LOAD_FAST | 12,557,614 | 5.3% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,486,366 | 76.9% |
| CALL | 19,599,728 | 8.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.0% |
| CALL_NO_KW_BUILTIN_FAST | 6,014,692 | 2.6% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 111,525,142 | 48.9% |
| BINARY_OP | 72,002,140 | 31.6% |
| RETURN_VALUE | 23,763,418 | 10.4% |
| STORE_FAST | 6,978,028 | 3.1% |
| LOAD_FAST | 5,876,700 | 2.6% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,382,666 | 91.3% |
| RETURN_VALUE | 1,727,780 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,230,542 | 3.3% |
| LOAD_ATTR | 95,323 | 0.3% |
| CALL_NO_KW_TUPLE_1 | 66,000 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.7% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 28.8% |
| STORE_FAST | 5,604,308 | 14.9% |
| RETURN_VALUE | 3,244,982 | 8.6% |
| BUILD_LIST | 1,966,480 | 5.2% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,920,376 | 66.6% |
| RETURN_GENERATOR | 5,526,160 | 24.7% |
| LOAD_ATTR_SLOT | 1,098,664 | 4.9% |
| CALL | 436,440 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 63.7% |
| BUILD_TUPLE | 2,891,824 | 12.9% |
| YIELD_VALUE | 2,419,200 | 10.8% |
| RETURN_VALUE | 1,004,416 | 4.5% |
| STORE_FAST | 642,060 | 2.9% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 332,333,621 | 98.9% |
| LOAD_CONST | 3,615,840 | 1.1% |
| BINARY_SUBSCR_TUPLE_INT | 66,000 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,424,504 | 85.5% |
| LOAD_GLOBAL_MODULE | 13,780,256 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 12,241,638 | 3.6% |
| CALL_PY_EXACT_ARGS | 8,118,032 | 2.4% |
| LOAD_FAST | 5,614,860 | 1.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 949,403,223 | 33.5% |
| LOAD_FAST_LOAD_FAST | 665,894,852 | 23.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 448,339,618 | 15.8% |
| LOAD_GLOBAL_MODULE | 166,095,059 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 111,400,391 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,522,112,848 | 88.9% |
| RETURN_GENERATOR | 140,433,352 | 5.0% |
| COPY_FREE_VARS | 125,506,566 | 4.4% |
| MAKE_CELL | 31,465,016 | 1.1% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 54,790,544 | 32.1% |
| LOAD_FAST | 42,031,965 | 24.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,253,402 | 7.2% |
| LOAD_ATTR_METHOD_NO_DICT | 12,068,800 | 7.1% |
| LOAD_ATTR | 11,113,740 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 164,634,929 | 96.4% |
| RETURN_GENERATOR | 3,375,896 | 2.0% |
| MAKE_CELL | 1,594,641 | 0.9% |
| COPY_FREE_VARS | 1,058,240 | 0.6% |
| CALL_PY_EXACT_ARGS | 89,140 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,421,469 | 93.0% |
| LOAD_GLOBAL_MODULE | 690,038 | 4.2% |
| BUILD_TUPLE | 359,940 | 2.2% |
| LOAD_ATTR_MODULE | 110,605 | 0.7% |
| LOAD_GLOBAL | 34 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,582,092 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 436 | 52.3% |
| CALL_INTRINSIC_1 | 240 | 28.8% |
| JUMP_BACKWARD | 158 | 18.9% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 46,560,649 | 32.0% |
| LOAD_FAST_LOAD_FAST | 32,739,520 | 22.5% |
| LOAD_ATTR | 15,308,348 | 10.5% |
| LOAD_ATTR_SLOT | 13,758,373 | 9.4% |
| LOAD_FAST | 10,889,700 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 78,772,013 | 54.1% |
| POP_JUMP_IF_TRUE | 38,840,693 | 26.7% |
| COPY | 18,630,840 | 12.8% |
| RETURN_VALUE | 7,090,495 | 4.9% |
| EXTENDED_ARG | 1,919,513 | 1.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 66,500,912 | 59.9% |
| BINARY_SUBSCR | 23,382,660 | 21.1% |
| LOAD_CONST | 6,328,928 | 5.7% |
| LOAD_FAST | 6,314,872 | 5.7% |
| LOAD_GLOBAL_MODULE | 3,631,919 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,501,092 | 43.7% |
| POP_JUMP_IF_TRUE | 32,446,020 | 29.2% |
| POP_JUMP_IF_FALSE | 30,129,429 | 27.1% |
| COMPARE_OP | 380 | 0.0% |
| EXTENDED_ARG | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 672,613,891 | 44.6% |
| LOAD_ATTR_INSTANCE_VALUE | 173,856,102 | 11.5% |
| LOAD_FAST | 121,639,625 | 8.1% |
| LOAD_FAST_LOAD_FAST | 120,555,695 | 8.0% |
| COPY | 109,001,248 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,270,757,320 | 84.3% |
| POP_JUMP_IF_TRUE | 122,131,032 | 8.1% |
| RETURN_VALUE | 59,382,152 | 3.9% |
| EXTENDED_ARG | 22,449,456 | 1.5% |
| LOAD_FAST | 15,024,000 | 1.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,563,963,599 | 98.3% |
| LOAD_FAST | 8,980,413 | 0.6% |
| LOAD_GLOBAL_MODULE | 5,058,761 | 0.3% |
| RETURN_VALUE | 4,023,960 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,550,226,297 | 97.5% |
| POP_JUMP_IF_TRUE | 27,393,581 | 1.7% |
| COPY | 6,090,438 | 0.4% |
| RETURN_VALUE | 4,403,399 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,415,960 | 49.9% |
| LOAD_FAST | 510,851,722 | 25.8% |
| LOAD_GLOBAL_MODULE | 301,874,060 | 15.2% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 44,331,335 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,870,209,682 | 94.3% |
| POP_JUMP_IF_TRUE | 60,498,900 | 3.1% |
| RETURN_VALUE | 25,865,640 | 1.3% |
| COPY | 21,273,122 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,393,224 | 83.3% |
| LOAD_ATTR | 11,580,662 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 1,385,580 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,739,124 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,856,561 | 24.9% |
| LOAD_FAST | 238,931,312 | 22.1% |
| LOAD_FAST_LOAD_FAST | 120,961,740 | 11.2% |
| SWAP | 112,621,215 | 10.4% |
| LOAD_CONST | 95,331,753 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,856,561 | 24.9% |
| TO_BOOL_BOOL | 234,251,051 | 21.7% |
| BINARY_SUBSCR_LIST_INT | 157,633,500 | 14.6% |
| BINARY_SUBSCR | 109,830,040 | 10.2% |
| COMPARE_OP_INT | 109,001,248 | 10.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 125,506,566 | 76.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,910,046 | 16.3% |
| CALL | 9,065,556 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,698,248 | 1.0% |
| CALL_PY_WITH_DEFAULTS | 1,058,240 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 179,631,448 | 70.9% |
| RETURN_GENERATOR | 73,605,535 | 29.1% |
| MAKE_CELL | 19,860 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,524,053 | 100.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,654,702 | 78.1% |
| NOP | 1,715,451 | 20.1% |
| RETURN_CONST | 151,253 | 1.8% |
| PUSH_EXC_INFO | 1,800 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,080 | 0.0% |


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
| STORE_FAST | 223,778 | 35.7% |
| CALL | 156,491 | 25.0% |
| POP_TOP | 77,862 | 12.4% |
| NOP | 55,794 | 8.9% |
| STORE_ATTR_INSTANCE_VALUE | 55,675 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 214,091 | 34.2% |
| RERAISE | 151,238 | 24.1% |
| RETURN_CONST | 111,408 | 17.8% |
| JUMP_FORWARD | 66,240 | 10.6% |
| LOAD_FAST | 58,288 | 9.3% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,193,625 | 57.2% |
| BUILD_SLICE | 53,378,248 | 41.7% |
| LOAD_FAST | 1,015,904 | 0.8% |
| LOAD_CONST | 286,740 | 0.2% |
| LOAD_ATTR_SLOT | 66,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,534,183 | 84.1% |
| LOAD_CONST | 18,169,146 | 14.2% |
| JUMP_BACKWARD | 1,105,140 | 0.9% |
| RETURN_CONST | 540,853 | 0.4% |
| LOAD_FAST_LOAD_FAST | 274,695 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,462,417 | 95.1% |
| RETURN_VALUE | 376,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 218,709 | 1.3% |
| LOAD_DEREF | 113,345 | 0.7% |
| LOAD_GLOBAL_MODULE | 37,576 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,251,273 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 37,576 | 72.1% |
| LOAD_FAST | 13,140 | 25.2% |
| BUILD_MAP | 540 | 1.0% |
| RETURN_VALUE | 480 | 0.9% |
| MAP_ADD | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,116 | 73.2% |
| DICT_MERGE | 13,140 | 25.2% |
| STORE_FAST | 540 | 1.0% |
| LOAD_DEREF | 120 | 0.2% |
| BUILD_MAP | 60 | 0.1% |


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
| RETURN_CONST | 56,701,055 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,102,080 | 33.7% |
| RETURN_CONST | 789,604 | 1.4% |
| LOAD_CONST | 5,940 | 0.0% |
| NOP | 4,980 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,456,298 | 51.7% |
| RETURN_VALUE | 69,224,034 | 35.6% |
| RETURN_CONST | 24,632,341 | 12.7% |
| JUMP_BACKWARD | 158 | 0.0% |
| SEND_GEN | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,095,997 | 48.9% |
| POP_TOP | 36,247,396 | 18.7% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,940 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 67,091,745 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,091,745 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 88,771,783 | 28.8% |
| LOAD_FAST | 42,654,620 | 13.8% |
| JUMP_BACKWARD | 40,665,662 | 13.2% |
| CALL_NO_KW_LIST_APPEND | 27,822,060 | 9.0% |
| COMPARE_OP_INT | 22,449,456 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 138,162,070 | 44.8% |
| JUMP_BACKWARD | 54,302,626 | 17.6% |
| FOR_ITER_LIST | 38,691,700 | 12.6% |
| POP_JUMP_IF_NONE | 36,519,160 | 11.8% |
| FOR_ITER | 16,516,644 | 5.4% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,739,124 | 88.4% |
| LOAD_FAST | 9,754,510 | 8.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,423,980 | 1.2% |
| RETURN_VALUE | 1,042,740 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,138,842 | 50.4% |
| BUILD_STRING | 52,319,974 | 44.6% |
| LOAD_FAST | 5,880,436 | 5.0% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,920 | 86.5% |
| LOAD_CONST | 300 | 13.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 212,795,018 | 72.6% |
| GET_ITER | 53,885,246 | 18.4% |
| EXTENDED_ARG | 16,516,644 | 5.6% |
| SWAP | 6,717,706 | 2.3% |
| LOAD_FAST | 3,174,736 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 151,765,268 | 51.8% |
| STORE_FAST | 76,738,030 | 26.2% |
| LOAD_FAST | 27,183,855 | 9.3% |
| RETURN_CONST | 15,910,874 | 5.4% |
| SWAP | 6,179,340 | 2.1% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,713,320 | 62.9% |
| JUMP_BACKWARD | 33,136,705 | 36.7% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,240 | 0.0% |
| SWAP | 1,331 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,764,951 | 62.9% |
| RESUME | 33,449,489 | 37.1% |
| RETURN_CONST | 300 | 0.0% |
| STORE_FAST | 240 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 924,139,328 | 74.6% |
| GET_ITER | 190,419,192 | 15.4% |
| LOAD_FAST | 59,098,400 | 4.8% |
| EXTENDED_ARG | 38,691,700 | 3.1% |
| SWAP | 25,951,819 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 587,112,057 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,605,804 | 25.4% |
| RETURN_CONST | 103,915,402 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,532,600 | 6.5% |
| LOAD_FAST | 59,432,000 | 4.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 428,687,156 | 88.8% |
| GET_ITER | 27,370,578 | 5.7% |
| LOAD_FAST | 21,531,300 | 4.5% |
| SWAP | 4,261,440 | 0.9% |
| EXTENDED_ARG | 829,500 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 396,964,403 | 82.2% |
| STORE_FAST_LOAD_FAST | 35,717,280 | 7.4% |
| RETURN_CONST | 24,278,416 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,581,682 | 1.2% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 292,068,571 | 69.1% |
| GET_ITER | 124,960,998 | 29.6% |
| SWAP | 2,996,680 | 0.7% |
| LOAD_FAST | 1,260,935 | 0.3% |
| FOR_ITER_LIST | 1,236,392 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 288,937,393 | 68.4% |
| LOAD_FAST | 61,890,960 | 14.6% |
| LOAD_FAST_LOAD_FAST | 43,821,240 | 10.4% |
| RETURN_CONST | 12,361,292 | 2.9% |
| STORE_FAST_LOAD_FAST | 6,874,080 | 1.6% |


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
| RETURN_GENERATOR | 78,588,931 | 92.4% |
| LOAD_FAST | 3,323,640 | 3.9% |
| RETURN_VALUE | 2,595,979 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 489,657 | 0.6% |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,015,307 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,799,867 | 36.0% |
| LOAD_ATTR_INSTANCE_VALUE | 64,977,512 | 10.9% |
| CALL_BUILTIN_CLASS | 63,635,554 | 10.7% |
| RETURN_VALUE | 50,004,827 | 8.4% |
| LOAD_ATTR_SLOT | 38,736,079 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 190,419,192 | 32.0% |
| FOR_ITER_TUPLE | 124,960,998 | 21.0% |
| CALL_PY_EXACT_ARGS | 85,107,291 | 14.3% |
| FOR_ITER_GEN | 56,713,320 | 9.5% |
| FOR_ITER | 53,885,246 | 9.1% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 12,000,420 | 79.1% |
| RETURN_GENERATOR | 3,161,762 | 20.8% |
| LOAD_FAST | 7,080 | 0.0% |
| LOAD_ATTR_SLOT | 1,320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,170,582 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 1,538,791 | 77.3% |
| STORE_FAST | 451,140 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,989,811 | 100.0% |
| PUSH_EXC_INFO | 120 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,671,511 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,538,791 | 92.1% |
| STORE_FAST | 132,120 | 7.9% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,335 | 51.5% |
| GET_ITER | 4,020 | 47.8% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,395 | 52.2% |
| NOP | 3,060 | 36.4% |
| INSTRUMENTED_RETURN_CONST | 240 | 2.9% |
| LOAD_CONST | 240 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 240 | 2.9% |


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,060 | 41.4% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,060 | 41.4% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 855 | 11.6% |
| LIST_APPEND | 300 | 4.1% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,335 | 58.6% |
| LOAD_FAST | 3,060 | 41.4% |


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
| LOAD_FAST | 7,297,260 | 50.0% |
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
| TO_BOOL_BOOL | 5,295 | 53.1% |
| TO_BOOL | 3,060 | 30.7% |
| TO_BOOL_STR | 960 | 9.6% |
| TO_BOOL_NONE | 300 | 3.0% |
| COMPARE_OP_STR | 240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.7% |
| LOAD_GLOBAL | 4,020 | 40.3% |
| INSTRUMENTED_JUMP_BACKWARD | 855 | 8.6% |
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
| LOAD_FAST | 14,569,320 | 99.9% |
| LOAD_GLOBAL | 12,000 | 0.1% |
| RESUME | 960 | 0.0% |
| INSTRUMENTED_RESUME | 660 | 0.0% |
| LOAD_CONST | 180 | 0.0% |


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
| YIELD_VALUE | 451,462,932 | 37.3% |
| RETURN_CONST | 410,750,433 | 33.9% |
| RETURN_VALUE | 329,694,081 | 27.2% |
| RETURN_GENERATOR | 18,176,251 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,239,346 | 46.9% |
| LOAD_FAST_LOAD_FAST | 127,666,228 | 27.7% |
| LOAD_GLOBAL_MODULE | 81,913,653 | 17.8% |
| LOAD_GLOBAL_BUILTIN | 15,924,318 | 3.5% |
| LOAD_CONST | 8,669,619 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 384,295,519 | 83.4% |
| POP_JUMP_IF_TRUE | 47,081,644 | 10.2% |
| EXTENDED_ARG | 18,199,680 | 4.0% |
| RETURN_VALUE | 3,378,043 | 0.7% |
| COPY | 3,174,963 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,433,117 | 28.6% |
| POP_TOP | 657,946,443 | 20.5% |
| POP_JUMP_IF_TRUE | 471,655,345 | 14.7% |
| POP_JUMP_IF_FALSE | 444,392,088 | 13.8% |
| LIST_APPEND | 146,786,419 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 924,139,328 | 28.8% |
| NOP | 718,030,409 | 22.3% |
| FOR_ITER_RANGE | 428,687,156 | 13.3% |
| LOAD_FAST | 308,046,545 | 9.6% |
| FOR_ITER_TUPLE | 292,068,571 | 9.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,748,365 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,502,239 | 97.1% |
| SEND | 6,246,126 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 174,387,086 | 41.2% |
| POP_JUMP_IF_FALSE | 100,900,206 | 23.8% |
| POP_TOP | 57,665,456 | 13.6% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| EXTENDED_ARG | 14,628,756 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 170,279,699 | 40.2% |
| LOAD_FAST_LOAD_FAST | 82,446,973 | 19.5% |
| LOAD_CONST | 37,406,782 | 8.8% |
| LOAD_GLOBAL_MODULE | 28,040,948 | 6.6% |
| LOAD_GLOBAL_BUILTIN | 25,956,245 | 6.1% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,539,172 | 24.0% |
| LOAD_CONST | 38,154,754 | 22.1% |
| LOAD_FAST_LOAD_FAST | 35,182,080 | 20.3% |
| LOAD_GLOBAL_MODULE | 18,005,418 | 10.4% |
| LOAD_ATTR_INSTANCE_VALUE | 11,380,134 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 149,661,307 | 86.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 22,239,889 | 12.9% |
| CALL_BUILTIN_CLASS | 1,051,800 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,917,240 | 19.7% |
| BUILD_TUPLE | 26,458,320 | 18.0% |
| BINARY_OP | 20,606,280 | 14.0% |
| LOAD_FAST | 18,295,892 | 12.5% |
| RETURN_VALUE | 15,134,924 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,786,419 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |
| CALL | 7 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 38,206,934 | 70.3% |
| LOAD_FAST | 15,451,086 | 28.4% |
| LOAD_CONST | 366,720 | 0.7% |
| RETURN_VALUE | 204,173 | 0.4% |
| LOAD_DEREF | 77,529 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 53,531,284 | 98.5% |
| STORE_FAST | 425,725 | 0.8% |
| LOAD_FAST | 215,520 | 0.4% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 578,687,198 | 55.8% |
| LOAD_GLOBAL_BUILTIN | 221,929,604 | 21.4% |
| LOAD_GLOBAL_MODULE | 95,605,000 | 9.2% |
| LOAD_ATTR_SLOT | 81,109,633 | 7.8% |
| LOAD_FAST_LOAD_FAST | 23,100,663 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 216,239,346 | 20.8% |
| STORE_FAST | 169,599,153 | 16.3% |
| LOAD_FAST | 154,006,515 | 14.8% |
| PUSH_NULL | 69,690,008 | 6.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 59,472,800 | 5.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,578,653 | 96.3% |
| LOAD_GLOBAL_BUILTIN | 1,791,838 | 1.5% |
| LOAD_FAST | 1,408,580 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 546,718 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,812,968 | 49.4% |
| CALL_PY_EXACT_ARGS | 21,860,150 | 18.1% |
| LOAD_FAST | 14,221,105 | 11.8% |
| PUSH_NULL | 8,285,400 | 6.8% |
| CALL_BUILTIN_CLASS | 2,841,920 | 2.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,208,337,712 | 84.8% |
| LOAD_FAST_LOAD_FAST | 334,850,941 | 8.8% |
| COPY | 80,667,567 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,697,358 | 1.3% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,061,341,176 | 28.0% |
| TO_BOOL_BOOL | 435,698,503 | 11.5% |
| STORE_FAST | 285,741,269 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 190,019,010 | 5.0% |
| RETURN_VALUE | 181,837,737 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40,724,486 | 71.5% |
| LOAD_FAST | 16,211,148 | 28.5% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,574,972 | 69.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,473,581 | 13.1% |
| LOAD_GLOBAL_MODULE | 5,902,972 | 10.4% |
| LOAD_CONST | 2,491,800 | 4.4% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 770,661,495 | 57.6% |
| LOAD_ATTR_INSTANCE_VALUE | 190,019,010 | 14.2% |
| LOAD_CONST | 90,386,097 | 6.8% |
| LOAD_GLOBAL_MODULE | 52,878,631 | 4.0% |
| LOAD_ATTR_SLOT | 48,976,888 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 663,870,363 | 49.6% |
| LOAD_CONST | 155,821,121 | 11.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 154,664,160 | 11.6% |
| LOAD_FAST_LOAD_FAST | 111,682,363 | 8.3% |
| CALL_PY_EXACT_ARGS | 111,400,391 | 8.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,606,727,802 | 84.9% |
| LOAD_ATTR_INSTANCE_VALUE | 63,489,003 | 3.4% |
| LOAD_ATTR_SLOT | 45,638,768 | 2.4% |
| LOAD_ATTR | 45,436,103 | 2.4% |
| LOAD_ATTR_WITH_HINT | 37,578,978 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 809,172,131 | 42.8% |
| LOAD_FAST_LOAD_FAST | 485,769,470 | 25.7% |
| CALL_PY_EXACT_ARGS | 448,339,618 | 23.7% |
| LOAD_GLOBAL_MODULE | 56,047,996 | 3.0% |
| LOAD_CONST | 53,012,506 | 2.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 324,197,149 | 95.4% |
| LOAD_ATTR_MODULE | 11,618,950 | 3.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,324,680 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 266,370,583 | 78.4% |
| CALL_NO_KW_ISINSTANCE | 22,117,150 | 6.5% |
| LOAD_ATTR_MODULE | 11,618,950 | 3.4% |
| LOAD_FAST | 10,381,993 | 3.1% |
| LOAD_GLOBAL_MODULE | 4,984,900 | 1.5% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,484,880 | 73.8% |
| LOAD_FAST_LOAD_FAST | 5,866,920 | 26.2% |
| LOAD_ATTR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,387,820 | 37.5% |
| CONTAINS_OP | 6,929,880 | 31.0% |
| CALL_PY_EXACT_ARGS | 3,269,240 | 14.6% |
| LOAD_ATTR_MODULE | 1,324,680 | 5.9% |
| STORE_FAST | 1,071,420 | 4.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,420,524 | 91.0% |
| LOAD_FAST_LOAD_FAST | 10,914,858 | 7.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,063,560 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 759,700 | 0.5% |
| STORE_FAST_LOAD_FAST | 181,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,587,045 | 21.3% |
| LOAD_FAST_LOAD_FAST | 27,613,920 | 19.3% |
| GET_ITER | 19,279,760 | 13.4% |
| LOAD_GLOBAL_BUILTIN | 15,384,960 | 10.7% |
| LOAD_ATTR_METHOD_NO_DICT | 10,309,640 | 7.2% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,548,954 | 83.5% |
| LOAD_ATTR_SLOT | 5,106,870 | 10.5% |
| RETURN_VALUE | 1,327,490 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,064,920 | 2.2% |
| LOAD_FAST_LOAD_FAST | 125,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 42,916,007 | 88.4% |
| TO_BOOL_NONE | 3,107,760 | 6.4% |
| RETURN_VALUE | 833,180 | 1.7% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,230,898,276 | 91.5% |
| LOAD_ATTR_SLOT | 40,652,016 | 3.0% |
| COPY | 40,401,408 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 8,700,851 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,027,215 | 22.8% |
| TO_BOOL_NONE | 88,096,915 | 6.5% |
| LOAD_ATTR | 81,109,633 | 6.0% |
| TO_BOOL_BOOL | 68,862,608 | 5.1% |
| COMPARE_OP_FLOAT | 66,500,912 | 4.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 277,226,850 | 79.9% |
| LOAD_ATTR_INSTANCE_VALUE | 22,741,043 | 6.6% |
| LOAD_ATTR_WITH_HINT | 22,281,420 | 6.4% |
| COPY | 14,038,524 | 4.0% |
| LOAD_FAST_LOAD_FAST | 8,451,801 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,380,184 | 24.6% |
| STORE_FAST | 43,154,700 | 12.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 37,578,978 | 10.8% |
| COMPARE_OP_INT | 35,281,246 | 10.2% |
| LOAD_CONST | 29,373,000 | 8.5% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 1,200 | 90.9% |
| RESUME | 120 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,320 | 100.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,902,349,893 | 51.1% |
| LOAD_CONST | 744,378,463 | 7.8% |
| LOAD_FAST_LOAD_FAST | 450,390,544 | 4.7% |
| STORE_FAST | 293,216,325 | 3.1% |
| POP_JUMP_IF_FALSE | 277,144,419 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,774,701,574 | 18.5% |
| COMPARE_OP_STR | 1,563,963,599 | 16.3% |
| LOAD_FAST | 1,063,707,584 | 11.1% |
| LOAD_CONST | 744,378,463 | 7.8% |
| COMPARE_OP_INT | 672,613,891 | 7.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 345,218,531 | 40.9% |
| LOAD_GLOBAL_BUILTIN | 111,388,133 | 13.2% |
| POP_JUMP_IF_FALSE | 57,745,657 | 6.8% |
| RESUME | 33,052,913 | 3.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 523,688,548 | 62.0% |
| LOAD_CONST | 69,820,940 | 8.3% |
| PUSH_NULL | 38,305,546 | 4.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 31,869,402 | 3.8% |
| LOAD_DEREF | 24,561,433 | 2.9% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,699,442,655 | 16.7% |
| POP_JUMP_IF_FALSE | 4,531,388,077 | 16.1% |
| LOAD_GLOBAL_BUILTIN | 2,666,337,421 | 9.5% |
| RESUME | 2,116,939,926 | 7.5% |
| LOAD_CONST | 1,063,707,584 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,902,349,893 | 17.5% |
| LOAD_ATTR_INSTANCE_VALUE | 3,208,337,712 | 11.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,606,727,802 | 5.7% |
| LOAD_ATTR_SLOT | 1,230,898,276 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,101,488,554 | 3.9% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 39,929,036 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,372,190 | 23.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 39,920,876 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,372,190 | 23.7% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,682,680 | 50.5% |
| POP_TOP | 2,058,382 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 421,860 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 339,748 | 4.7% |
| STORE_FAST | 308,760 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 49.0% |
| POP_JUMP_IF_NOT_NONE | 1,511,040 | 20.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 5.9% |
| LOAD_FAST | 383,640 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 335,548 | 4.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,340,310,548 | 16.7% |
| POP_JUMP_IF_FALSE | 1,191,156,178 | 14.8% |
| NOP | 959,973,937 | 12.0% |
| LOAD_FAST_LOAD_FAST | 512,657,249 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 485,769,470 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 1,202,362,860 | 15.0% |
| CONTAINS_OP | 989,415,960 | 12.3% |
| CALL_PY_EXACT_ARGS | 665,894,852 | 8.3% |
| LOAD_FAST | 645,525,724 | 8.0% |
| STORE_ATTR_SLOT | 515,616,822 | 6.4% |


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
| PUSH_NULL | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 98.8% |
| STORE_FAST | 20,043 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 8,288 | 0.1% |
| NOP | 4,594 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,672 | 98.9% |
| LOAD_GLOBAL_MODULE | 41,834 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 15,868 | 0.2% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,614 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,101,488,554 | 26.6% |
| POP_JUMP_IF_FALSE | 982,247,925 | 23.8% |
| RESUME | 846,739,877 | 20.5% |
| STORE_FAST | 540,586,500 | 13.1% |
| POP_JUMP_IF_TRUE | 102,095,950 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,666,337,421 | 64.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.5% |
| CALL_NO_KW_ISINSTANCE | 331,858,865 | 8.0% |
| LOAD_ATTR | 221,929,604 | 5.4% |
| LOAD_FAST_LOAD_FAST | 113,567,236 | 2.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 893,404,785 | 30.9% |
| STORE_FAST | 421,929,977 | 14.6% |
| RESUME | 339,359,777 | 11.7% |
| POP_JUMP_IF_FALSE | 277,598,071 | 9.6% |
| LOAD_FAST_LOAD_FAST | 113,398,694 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 459,615,476 | 15.9% |
| LOAD_FAST | 452,848,623 | 15.7% |
| CALL_NO_KW_ISINSTANCE | 346,540,111 | 12.0% |
| LOAD_ATTR_MODULE | 324,197,149 | 11.2% |
| CONTAINS_OP | 301,874,060 | 10.4% |


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,380 | 53.5% |
| STORE_NAME | 1,200 | 46.5% |

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
| STORE_NAME | 240 | 15.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 1,320 | 84.6% |
| PUSH_NULL | 180 | 11.5% |
| UNPACK_SEQUENCE_TUPLE | 40 | 2.6% |
| UNPACK_SEQUENCE | 20 | 1.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,420 | 92.2% |
| EXTENDED_ARG | 60 | 3.9% |
| LOAD_DEREF | 60 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,420 | 92.2% |
| LOAD_SUPER_ATTR_ATTR | 120 | 7.8% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,298,440 | 100.0% |
| EXTENDED_ARG | 120 | 0.0% |
| LOAD_SUPER_ATTR | 120 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_DEREF | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,228,880 | 97.0% |
| LOAD_GLOBAL_MODULE | 65,520 | 2.9% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 118,294,887 | 100.0% |
| LOAD_DEREF | 9,080 | 0.0% |
| LOAD_SUPER_ATTR | 1,420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 66,639,008 | 56.3% |
| LOAD_FAST | 37,261,277 | 31.5% |
| CALL_PY_EXACT_ARGS | 6,403,064 | 5.4% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.0% |
| CALL | 1,200,040 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,484,116 | 53.6% |
| CALL_PY_EXACT_ARGS | 31,465,016 | 34.1% |
| CALL_FUNCTION_EX | 4,745,036 | 5.1% |
| CALL | 4,141,103 | 4.5% |
| CALL_PY_WITH_DEFAULTS | 1,594,641 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,484,116 | 53.4% |
| RESUME | 42,527,796 | 45.9% |
| RETURN_GENERATOR | 657,101 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,851,404 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 82,647,421 | 87.1% |
| LOAD_FAST | 9,062,460 | 9.6% |
| LOAD_GLOBAL_MODULE | 2,504,360 | 2.6% |
| KW_NAMES | 255,360 | 0.3% |
| CALL | 128,418 | 0.1% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,896,280 | 38.4% |
| RETURN_VALUE | 6,380,580 | 15.4% |
| LOAD_FAST | 6,188,718 | 14.9% |
| JUMP_FORWARD | 4,782,840 | 11.6% |
| STORE_FAST | 4,549,800 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,597,580 | 49.8% |
| JUMP_BACKWARD | 19,591,416 | 47.3% |
| CALL_FUNCTION_EX | 1,211,460 | 2.9% |
| DICT_UPDATE | 180 | 0.0% |
| BUILD_MAP | 120 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 718,030,409 | 48.0% |
| RESUME | 337,447,157 | 22.5% |
| STORE_FAST | 158,985,202 | 10.6% |
| POP_JUMP_IF_FALSE | 80,712,906 | 5.4% |
| NOP | 52,973,290 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 959,973,937 | 64.1% |
| LOAD_FAST | 402,246,406 | 26.9% |
| NOP | 52,973,290 | 3.5% |
| LOAD_GLOBAL_BUILTIN | 34,250,406 | 2.3% |
| LOAD_CONST | 22,895,231 | 1.5% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,943,177 | 58.3% |
| STORE_SUBSCR_DICT | 3,085,473 | 18.1% |
| SWAP | 1,973,411 | 11.6% |
| COPY | 1,285,315 | 7.5% |
| STORE_FAST | 547,538 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,503,142 | 55.7% |
| RETURN_VALUE | 1,913,724 | 11.2% |
| JUMP_FORWARD | 1,715,820 | 10.1% |
| POP_TOP | 1,385,007 | 8.1% |
| RERAISE | 1,285,315 | 7.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,359,039,388 | 27.9% |
| CONTAINS_OP | 1,870,209,682 | 22.1% |
| COMPARE_OP_STR | 1,550,226,297 | 18.4% |
| COMPARE_OP_INT | 1,270,757,320 | 15.0% |
| IS_OP | 384,295,519 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,531,388,077 | 53.7% |
| LOAD_FAST_LOAD_FAST | 1,191,156,178 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 982,247,925 | 11.6% |
| JUMP_BACKWARD | 444,392,088 | 5.3% |
| LOAD_GLOBAL_MODULE | 277,598,071 | 3.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 203,447,341 | 68.1% |
| EXTENDED_ARG | 36,519,160 | 12.2% |
| LOAD_ATTR_SLOT | 25,425,420 | 8.5% |
| LOAD_DEREF | 13,784,044 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,419,539 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 185,583,308 | 62.1% |
| LOAD_DEREF | 28,708,061 | 9.6% |
| JUMP_BACKWARD | 26,814,927 | 9.0% |
| RETURN_CONST | 15,888,446 | 5.3% |
| LOAD_GLOBAL_BUILTIN | 12,784,363 | 4.3% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 355,178,041 | 82.4% |
| LOAD_ATTR_INSTANCE_VALUE | 30,430,251 | 7.1% |
| LOAD_ATTR | 14,136,830 | 3.3% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.1% |
| EXTENDED_ARG | 7,255,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 176,606,203 | 40.9% |
| LOAD_GLOBAL_BUILTIN | 96,628,327 | 22.4% |
| LOAD_FAST_LOAD_FAST | 60,388,654 | 14.0% |
| LOAD_GLOBAL_MODULE | 36,037,857 | 8.4% |
| NOP | 17,996,998 | 4.2% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 735,447,593 | 49.8% |
| TO_BOOL | 132,363,467 | 9.0% |
| COMPARE_OP_INT | 122,131,032 | 8.3% |
| TO_BOOL_ALWAYS_TRUE | 82,915,595 | 5.6% |
| TO_BOOL_NONE | 77,694,819 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 593,722,210 | 40.2% |
| JUMP_BACKWARD | 471,655,345 | 32.0% |
| LOAD_GLOBAL_BUILTIN | 102,095,950 | 6.9% |
| POP_TOP | 72,476,448 | 4.9% |
| LOAD_CONST | 68,430,886 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 573,546,284 | 25.3% |
| RESUME | 472,276,216 | 20.8% |
| CALL_NO_KW_BUILTIN_O | 341,716,527 | 15.1% |
| POP_JUMP_IF_FALSE | 169,386,493 | 7.5% |
| RETURN_VALUE | 123,788,165 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 921,341,063 | 39.1% |
| JUMP_BACKWARD | 657,946,443 | 27.9% |
| RESUME | 238,829,188 | 10.1% |
| RETURN_CONST | 184,093,166 | 7.8% |
| LOAD_FAST_LOAD_FAST | 99,544,114 | 4.2% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,217,014 | 30.7% |
| LOAD_ATTR | 3,246,420 | 19.1% |
| RAISE_VARARGS | 2,298,503 | 13.5% |
| CALL_NO_KW_BUILTIN_FAST | 1,785,291 | 10.5% |
| RERAISE | 1,115,619 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,418,926 | 90.4% |
| LOAD_GLOBAL_MODULE | 1,104,743 | 6.5% |
| LOAD_FAST | 387,187 | 2.3% |
| WITH_EXCEPT_START | 138,123 | 0.8% |
| LOAD_GLOBAL | 628 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 638,211,063 | 59.0% |
| LOAD_ATTR_MODULE | 266,370,583 | 24.6% |
| LOAD_ATTR | 69,690,008 | 6.4% |
| LOAD_FAST_LOAD_FAST | 39,531,240 | 3.7% |
| LOAD_DEREF | 38,305,546 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 535,081,281 | 49.5% |
| LOAD_FAST_LOAD_FAST | 283,789,828 | 26.2% |
| LOAD_CONST | 138,370,821 | 12.8% |
| CALL | 50,853,122 | 4.7% |
| LOAD_GLOBAL_MODULE | 31,525,671 | 2.9% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,494,822 | 51.6% |
| LOAD_ATTR_MODULE | 583,740 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 18.7% |
| LOAD_FAST | 151,178 | 5.2% |
| RETURN_VALUE | 55,440 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,298,503 | 79.4% |
| COPY | 445,440 | 15.4% |
| LOAD_CONST | 151,238 | 5.2% |
| CALL_INTRINSIC_1 | 22 | 0.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,380,963 | 75.1% |
| POP_EXCEPT | 1,285,315 | 15.1% |
| POP_TOP | 386,940 | 4.6% |
| POP_JUMP_IF_FALSE | 155,640 | 1.8% |
| DELETE_FAST | 151,238 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,115,619 | 56.1% |
| COPY | 831,228 | 41.8% |
| CALL_INTRINSIC_1 | 42,158 | 2.1% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,522,112,848 | 63.5% |
| POP_TOP | 238,829,188 | 6.0% |
| CALL | 211,832,440 | 5.3% |
| SEND_GEN | 208,502,187 | 5.2% |
| COPY_FREE_VARS | 179,631,448 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,116,939,926 | 42.4% |
| LOAD_GLOBAL_BUILTIN | 846,739,877 | 17.0% |
| POP_TOP | 472,276,216 | 9.5% |
| LOAD_GLOBAL_MODULE | 339,359,777 | 6.8% |
| NOP | 337,447,157 | 6.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 267,503,674 | 19.9% |
| STORE_ATTR_SLOT | 246,983,266 | 18.4% |
| POP_TOP | 184,093,166 | 13.7% |
| STORE_ATTR_INSTANCE_VALUE | 180,674,965 | 13.4% |
| RESUME | 122,771,702 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 573,546,284 | 42.7% |
| INTERPRETER_EXIT | 410,750,433 | 30.6% |
| EXIT_INIT_CHECK | 67,091,745 | 5.0% |
| TO_BOOL_BOOL | 56,815,673 | 4.2% |
| END_FOR | 56,701,055 | 4.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,433,352 | 63.6% |
| COPY_FREE_VARS | 73,605,535 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,375,896 | 1.5% |
| CALL_FUNCTION_EX | 1,715,691 | 0.8% |
| CALL | 873,924 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,588,931 | 32.9% |
| GET_ITER | 37,670,522 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,880 | 13.8% |
| STORE_FAST | 19,530,120 | 8.2% |
| INTERPRETER_EXIT | 18,176,251 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 781,804,286 | 26.0% |
| RETURN_VALUE | 518,742,469 | 17.2% |
| BUILD_TUPLE | 413,115,517 | 13.7% |
| LOAD_ATTR_INSTANCE_VALUE | 181,837,737 | 6.0% |
| BINARY_SUBSCR_DICT | 104,205,779 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 640,179,350 | 21.3% |
| RETURN_VALUE | 518,742,469 | 17.2% |
| INTERPRETER_EXIT | 329,694,081 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 264,501,394 | 8.8% |
| TO_BOOL_BOOL | 261,875,709 | 8.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,457,364 | 94.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,246,126 | 5.5% |
| SEND | 28,887 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,456,298 | 89.1% |
| YIELD_VALUE | 6,246,576 | 5.5% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,887 | 0.0% |
| SEND_GEN | 608 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,502,239 | 69.0% |
| LOAD_CONST | 93,865,285 | 31.0% |
| SEND | 608 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,502,187 | 69.0% |
| POP_TOP | 93,865,765 | 31.0% |
| END_SEND | 120 | 0.0% |
| YIELD_VALUE | 60 | 0.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 89.0% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 3.9% |
| STORE_FAST_LOAD_FAST | 108,000 | 3.3% |
| RETURN_VALUE | 69,060 | 2.1% |
| LOAD_FAST | 25,440 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,234,120 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 82,647,421 | 98.7% |
| SET_FUNCTION_ATTRIBUTE | 1,112,223 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,219,535 | 64.7% |
| LOAD_GLOBAL_BUILTIN | 18,989,340 | 22.7% |
| STORE_FAST | 5,800,424 | 6.9% |
| CALL_PY_EXACT_ARGS | 2,063,596 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 1,112,223 | 1.3% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 66,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 66,000 | 99.5% |
| STORE_FAST | 240 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,580,680 | 59.0% |
| LOAD_FAST_LOAD_FAST | 15,244,607 | 28.5% |
| CALL | 5,419,260 | 10.1% |
| SWAP | 946,681 | 1.8% |
| LOAD_GLOBAL_MODULE | 199,140 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,910,506 | 29.7% |
| LOAD_DEREF | 13,447,060 | 25.1% |
| RETURN_CONST | 8,606,077 | 16.1% |
| JUMP_BACKWARD | 5,554,200 | 10.4% |
| LOAD_FAST_LOAD_FAST | 4,743,842 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 378,146,409 | 45.1% |
| LOAD_FAST_LOAD_FAST | 303,587,056 | 36.2% |
| SWAP | 80,667,567 | 9.6% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.2% |
| RETURN_VALUE | 21,167,460 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 316,200,875 | 37.7% |
| RETURN_CONST | 180,674,965 | 21.6% |
| LOAD_FAST_LOAD_FAST | 167,833,513 | 20.0% |
| LOAD_CONST | 73,326,816 | 8.8% |
| NOP | 51,801,583 | 6.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 515,616,822 | 48.5% |
| LOAD_FAST | 504,100,585 | 47.4% |
| SWAP | 40,401,408 | 3.8% |
| STORE_ATTR_SLOT | 2,127,445 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 279,528,950 | 26.3% |
| LOAD_FAST | 253,887,681 | 23.9% |
| RETURN_CONST | 246,983,266 | 23.2% |
| LOAD_CONST | 220,204,705 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 25,391,400 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,739,759 | 48.5% |
| SWAP | 14,038,524 | 27.5% |
| LOAD_FAST_LOAD_FAST | 11,937,095 | 23.4% |
| LOAD_DEREF | 242,500 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,113,723 | 66.9% |
| JUMP_BACKWARD | 5,313,540 | 10.4% |
| RETURN_CONST | 4,426,120 | 8.7% |
| LOAD_CONST | 3,924,012 | 7.7% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.5% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,874,000 | 40.9% |
| STORE_FAST | 19,047,660 | 29.0% |
| LOAD_CONST | 6,839,507 | 10.4% |
| LOAD_FAST | 2,917,140 | 4.4% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,460 | 28.9% |
| LOAD_DEREF | 13,770,449 | 20.9% |
| LOAD_FAST_LOAD_FAST | 13,437,000 | 20.4% |
| LOAD_FAST | 9,641,351 | 14.7% |
| LOAD_CONST | 4,836,881 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,765,258 | 12.8% |
| BINARY_SUBSCR_STR_INT | 841,517,940 | 8.5% |
| STORE_FAST | 711,188,363 | 7.2% |
| RETURN_VALUE | 640,179,350 | 6.5% |
| FOR_ITER_LIST | 587,112,057 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,699,442,655 | 47.7% |
| LOAD_FAST_LOAD_FAST | 1,340,310,548 | 13.6% |
| JUMP_BACKWARD | 918,433,117 | 9.3% |
| STORE_FAST | 711,188,363 | 7.2% |
| LOAD_GLOBAL_BUILTIN | 540,586,500 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,532,600 | 58.9% |
| FOR_ITER_RANGE | 35,717,280 | 26.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,140 | 6.7% |
| FOR_ITER_TUPLE | 6,874,080 | 5.0% |
| FOR_ITER | 2,965,746 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,780 | 21.6% |
| LOAD_FAST | 24,445,380 | 17.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,928,140 | 15.3% |
| STORE_ATTR_INSTANCE_VALUE | 9,297,971 | 6.8% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.5% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,842 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 368,124,390 | 23.9% |
| UNPACK_SEQUENCE_TUPLE | 140,575,580 | 9.1% |
| UNPACK_SEQUENCE_LIST | 134,205,000 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,842 | 52.8% |
| LOAD_FAST | 465,936,805 | 30.2% |
| LOAD_FAST_LOAD_FAST | 86,508,081 | 5.6% |
| STORE_FAST | 75,477,498 | 4.9% |
| LOAD_GLOBAL_MODULE | 46,180,272 | 3.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,147,720 | 99.9% |
| RETURN_VALUE | 3,900 | 0.1% |
| LOAD_ATTR | 540 | 0.0% |
| LOAD_FAST | 360 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,864,320 | 79.1% |
| LOAD_GLOBAL_MODULE | 1,286,100 | 20.9% |
| LOAD_CONST | 2,040 | 0.0% |
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
| LOAD_LOCALS | 1,200 | 25.0% |
| LOAD_NAME | 240 | 5.0% |
| LOAD_FAST | 120 | 2.5% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,909,260 | 88.3% |
| LOAD_CONST | 13,496,296 | 11.5% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,615,776 | 91.5% |
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
| SWAP | 109,837,920 | 34.7% |
| LOAD_FAST | 64,774,559 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 17.9% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.1% |
| LOAD_CONST | 27,783,040 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.4% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 32.9% |
| RETURN_CONST | 33,885,786 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,003,020 | 8.5% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 95,460,718 | 49.6% |
| LOAD_FAST | 64,774,923 | 33.6% |
| CALL_NO_KW_BUILTIN_O | 13,999,260 | 7.3% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 2.0% |
| CALL_NO_KW_LEN | 3,782,400 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,054,146 | 37.9% |
| LOAD_FAST | 66,101,546 | 34.3% |
| JUMP_BACKWARD | 25,332,018 | 13.2% |
| RETURN_CONST | 12,893,911 | 6.7% |
| LOAD_GLOBAL_MODULE | 7,343,168 | 3.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,500 | 52.2% |
| LOAD_FAST | 57,439,700 | 19.0% |
| LOAD_CONST | 26,912,536 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,054,830 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,923,300 | 38.0% |
| JUMP_BACKWARD | 110,633,010 | 36.6% |
| LOAD_FAST_LOAD_FAST | 71,544,500 | 23.7% |
| RETURN_CONST | 4,469,760 | 1.5% |
| LOAD_CONST | 231,120 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,856,561 | 28.8% |
| BINARY_OP_ADD_FLOAT | 116,612,886 | 12.5% |
| LOAD_FAST | 105,301,187 | 11.3% |
| BINARY_OP_ADD_INT | 90,618,932 | 9.7% |
| BINARY_OP_SUBTRACT_INT | 69,254,725 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,856,561 | 28.8% |
| STORE_SUBSCR_LIST_INT | 157,633,500 | 16.9% |
| COPY | 112,621,215 | 12.0% |
| STORE_SUBSCR | 109,837,920 | 11.8% |
| STORE_ATTR_INSTANCE_VALUE | 80,667,567 | 8.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,775,616 | 80.9% |
| LOAD_ATTR_INSTANCE_VALUE | 23,955,969 | 11.7% |
| LOAD_ATTR | 7,358,316 | 3.6% |
| LOAD_ATTR_SLOT | 3,352,621 | 1.6% |
| COPY | 2,333,138 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 132,363,467 | 64.6% |
| POP_JUMP_IF_FALSE | 71,880,721 | 35.1% |
| TO_BOOL | 235,793 | 0.1% |
| UNARY_NOT | 220,622 | 0.1% |
| TO_BOOL_NONE | 125,702 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,565,771 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,746,352 | 33.4% |
| LOAD_ATTR_SLOT | 17,761,080 | 9.9% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 7,172,951 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 94,344,812 | 52.7% |
| POP_JUMP_IF_TRUE | 82,915,595 | 46.3% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,845 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,501 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 801,047,711 | 24.7% |
| LOAD_FAST | 715,266,583 | 22.1% |
| CALL_NO_KW_BUILTIN_FAST | 477,696,151 | 14.8% |
| LOAD_ATTR_INSTANCE_VALUE | 435,698,503 | 13.5% |
| RETURN_VALUE | 261,875,709 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,359,039,388 | 72.9% |
| POP_JUMP_IF_TRUE | 735,447,593 | 22.7% |
| EXTENDED_ARG | 88,771,783 | 2.7% |
| UNARY_NOT | 53,922,323 | 1.7% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 173,517,218 | 76.0% |
| CALL_NO_KW_BUILTIN_O | 12,836,580 | 5.6% |
| COPY | 12,633,973 | 5.5% |
| BINARY_OP | 9,116,763 | 4.0% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,354,634 | 88.2% |
| POP_JUMP_IF_TRUE | 25,627,531 | 11.2% |
| UNARY_NOT | 1,035,600 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,859,989 | 66.9% |
| LOAD_ATTR_INSTANCE_VALUE | 27,754,587 | 24.8% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,712,180 | 1.5% |
| COPY | 814,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,667,338 | 55.1% |
| POP_JUMP_IF_FALSE | 46,704,809 | 41.7% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,760 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,519,535 | 45.0% |
| LOAD_ATTR_SLOT | 88,096,915 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 56,724,295 | 15.1% |
| LOAD_ATTR | 21,871,756 | 5.8% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 296,871,488 | 78.9% |
| POP_JUMP_IF_TRUE | 77,694,819 | 20.6% |
| EXTENDED_ARG | 967,320 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,934 | 0.2% |
| TO_BOOL | 123,673 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,966,070 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,407,740 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,340 | 5.8% |
| COPY | 2,682,160 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 36,172,752 | 53.8% |
| POP_JUMP_IF_TRUE | 30,414,560 | 45.2% |
| UNARY_NOT | 600,240 | 0.9% |
| TO_BOOL_NONE | 36,180 | 0.1% |
| EXTENDED_ARG | 8,280 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,579,357 | 92.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 380,660 | 3.3% |
| LOAD_ATTR_MODULE | 312,301 | 2.7% |
| LOAD_FAST | 122,040 | 1.1% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,404,618 | 100.0% |


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
| LOAD_CONST | 79,368,120 | 65.4% |
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
| TO_BOOL_BOOL | 53,922,323 | 92.2% |
| TO_BOOL_LIST | 2,640,720 | 4.5% |
| TO_BOOL_INT | 1,035,600 | 1.8% |
| TO_BOOL_STR | 600,240 | 1.0% |
| TO_BOOL | 220,622 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 29,526,902 | 50.5% |
| RETURN_VALUE | 16,575,081 | 28.4% |
| KW_NAMES | 10,514,640 | 18.0% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.3% |
| LOAD_FAST | 555,240 | 0.9% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 218,520 | 76.4% |
| LOAD_FAST | 66,000 | 23.1% |
| CALL_INTRINSIC_1 | 960 | 0.3% |
| FOR_ITER | 720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 286,200 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 96,120 | 44.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,940 | 31.4% |
| COPY | 19,920 | 9.2% |
| FOR_ITER_LIST | 10,560 | 4.9% |
| CALL_BUILTIN_CLASS | 10,080 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,284 | 62.0% |
| STORE_FAST | 79,688 | 36.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,726 | 0.8% |
| UNPACK_SEQUENCE | 460 | 0.2% |
| UNPACK_SEQUENCE_TUPLE | 440 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,417,940 | 70.2% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,001,740 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 799,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,205,000 | 95.7% |
| STORE_FAST | 6,004,980 | 4.3% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 264,501,394 | 62.2% |
| LOAD_FAST | 103,134,100 | 24.2% |
| BINARY_SUBSCR_DICT | 15,509,306 | 3.6% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260,434,972 | 61.2% |
| STORE_FAST_STORE_FAST | 140,575,580 | 33.1% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.6% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,605,804 | 52.0% |
| FOR_ITER | 151,765,268 | 25.1% |
| RETURN_VALUE | 84,703,074 | 14.0% |
| LOAD_FAST | 35,337,180 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 368,124,390 | 60.8% |
| STORE_FAST | 215,215,612 | 35.5% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST_LOAD_FAST | 9,187,140 | 1.5% |
| LOAD_FAST | 906,540 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 138,123 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 137,325 | 99.4% |
| TO_BOOL_BOOL | 780 | 0.6% |
| TO_BOOL | 18 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.4% |
| YIELD_VALUE | 208,502,563 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,285 | 4.5% |
| LOAD_CONST | 26,891,811 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 451,462,932 | 65.1% |
| YIELD_VALUE | 208,502,563 | 30.1% |
| STORE_FAST | 24,773,580 | 3.6% |
| UNPACK_SEQUENCE_TUPLE | 4,808,640 | 0.7% |
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
| specialization.deferred |    204575062 | 4.6% |
| specialization.deopt |      1599021 | 0.0% |
|          hit |   4115049895 | 93.4% |
|         miss |     84780146 | 1.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,613,097 | 80.8% |
| Failure | 383,566 | 19.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.4% |
| other | 125,980 | 32.8% |
| tuple | 75,020 | 19.6% |
| dict | 16,814 | 4.4% |
| bytes | 10,779 | 2.8% |
| set | 7,220 | 1.9% |
| sequence | 6,038 | 1.6% |
| mapping | 4,595 | 1.2% |
| float | 980 | 0.3% |
| bytearray | 320 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1111039688 | 26.5% |
| specialization.deopt |        68566 | 0.0% |
|          hit |   3074370468 | 73.4% |
|         miss |      3636745 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 70,659 | 19.8% |
| Failure | 286,864 | 80.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 112,980 | 39.4% |
| other | 77,502 | 27.0% |
| out of range | 40,682 | 14.2% |
| buffer int | 25,740 | 9.0% |
| list slice | 25,520 | 8.9% |
| sequence int | 2,920 | 1.0% |
| code complex parameters | 1,420 | 0.5% |
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
| specialization.deferred |    316113851 | 39.0% |
| specialization.deopt |           40 | 0.0% |
|          hit |    494814548 | 61.0% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,747 | 2.0% |
| Failure | 83,798 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.5% |
| dict subclass no override | 17,961 | 21.4% |
| py simple | 13,817 | 16.5% |
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
| specialization.deferred |       213972 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1168538714 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,286 | 99.1% |
| Failure | 460 | 0.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| iterator | 200 | 43.5% |
| sequence | 180 | 39.1% |
| other | 80 | 17.4% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    293088283 | 11.6% |
| specialization.deopt |      2480406 | 0.1% |
|          hit |   2103602479 | 83.2% |
|         miss |    131462287 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,473 | 96.2% |
| Failure | 96,701 | 3.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,020 | 23.8% |
| dict items | 20,431 | 21.1% |
| seq iter | 15,120 | 15.6% |
| set | 13,248 | 13.7% |
| other | 7,660 | 7.9% |
| dict values | 3,820 | 4.0% |
| reversed list | 3,642 | 3.8% |
| zip | 3,400 | 3.5% |
| ascii string | 2,680 | 2.8% |
| dict keys | 2,060 | 2.1% |
| itertools | 820 | 0.8% |
| map | 600 | 0.6% |
| callable | 120 | 0.1% |
| bytes | 80 | 0.1% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     53482055 | 2.7% |
| specialization.deopt |      3549368 | 0.2% |
|          hit |   1763601662 | 87.9% |
|         miss |    188128134 | 9.4% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,571,761 | 98.9% |
| Failure | 38,742 | 1.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,280 | 44.6% |
| not in dict | 10,740 | 27.7% |
| overriding descriptor | 5,020 | 13.0% |
| property | 1,220 | 3.1% |
| not in keys | 1,160 | 3.0% |
| non object slot | 920 | 2.4% |
| overridden | 860 | 2.2% |
| no dict | 860 | 2.2% |
| not managed dict | 382 | 1.0% |
| method | 300 | 0.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1036972453 | 9.9% |
| specialization.deopt |     10308034 | 0.1% |
|          hit |   8892387714 | 84.9% |
|         miss |    546476862 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,379,650 | 95.8% |
| Failure | 449,748 | 4.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 147,851 | 32.9% |
| metaclass attribute | 102,016 | 22.7% |
| method | 60,700 | 13.5% |
| not managed dict | 59,468 | 13.2% |
| shadowed | 40,650 | 9.0% |
| non object slot | 7,736 | 1.7% |
| class method obj | 7,260 | 1.6% |
| class attr descriptor | 6,280 | 1.4% |
| overridden | 5,220 | 1.2% |
| non overriding descriptor | 4,480 | 1.0% |
| mutable class | 2,862 | 0.6% |
| not in keys | 1,740 | 0.4% |
| class attr simple | 1,685 | 0.4% |
| module attr not found | 1,340 | 0.3% |
| builtin class method | 440 | 0.1% |
| property | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    145487134 | 4.3% |
| specialization.deopt |        25428 | 0.0% |
|          hit |   3207807007 | 95.6% |
|         miss |      1348482 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 29,429 | 21.0% |
| Failure | 110,682 | 79.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 48,348 | 43.7% |
| different types | 23,830 | 21.5% |
| baseobject | 13,277 | 12.0% |
| float long | 9,292 | 8.4% |
| set | 6,620 | 6.0% |
| other | 3,000 | 2.7% |
| bool | 2,355 | 2.1% |
| tuple | 1,680 | 1.5% |
| list | 1,020 | 0.9% |
| bytes | 800 | 0.7% |
| long float | 320 | 0.3% |
| string | 140 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322582 | 0.1% |
| specialization.deopt |          451 | 0.0% |
|          hit |   7026984297 | 99.9% |
|         miss |        25409 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 54,693 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    841004606 | 15.6% |
| specialization.deopt |       712840 | 0.0% |
|          hit |   4518933337 | 83.7% |
|         miss |     37782946 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,917 | 39.2% |
| Failure | 1,110,755 | 60.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,020 | 52.1% |
| multiply different types | 171,555 | 15.4% |
| add different types | 151,885 | 13.7% |
| floor divide | 32,920 | 3.0% |
| and int | 32,231 | 2.9% |
| remainder | 32,028 | 2.9% |
| add other | 27,100 | 2.4% |
| lshift | 18,760 | 1.7% |
| rshift | 16,637 | 1.5% |
| true divide different types | 14,860 | 1.3% |
| xor | 10,500 | 0.9% |
| true divide float | 6,780 | 0.6% |
| subtract other | 5,520 | 0.5% |
| or | 4,075 | 0.4% |
| power | 3,702 | 0.3% |
| true divide other | 1,202 | 0.1% |
| multiply other | 1,060 | 0.1% |
| and other | 860 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112702882 | 27.2% |
|          hit |    302367952 | 72.8% |
|         miss |          180 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 608 | 2.1% |
| Failure | 28,887 | 97.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 84.6% |
| other | 4,367 | 15.1% |
| dict keys | 40 | 0.1% |
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
|          hit |    120604227 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,540 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    894017459 | 10.1% |
| specialization.deopt |      2794510 | 0.0% |
|          hit |   7813337732 | 88.2% |
|         miss |    148233160 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,841,648 | 87.8% |
| Failure | 394,156 | 12.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 66,303 | 16.8% |
| kwnames | 56,144 | 14.2% |
| code complex parameters | 54,196 | 13.7% |
| no dict | 51,380 | 13.0% |
| class no vectorcall | 29,468 | 7.5% |
| cfunc varargs keywords | 24,892 | 6.3% |
| cfunc noargs | 22,584 | 5.7% |
| meth descr varargs | 22,427 | 5.7% |
| other | 11,466 | 2.9% |
| init not python | 10,420 | 2.6% |
| class mutable | 8,739 | 2.2% |
| init not simple | 8,420 | 2.1% |
| meth descr varargs keywords | 7,338 | 1.9% |
| wrong number arguments | 4,460 | 1.1% |
| cmethod | 3,600 | 0.9% |
| bound method | 3,367 | 0.9% |
| cfunc varargs | 3,096 | 0.8% |
| method wrapper | 2,492 | 0.6% |
| operator wrapper | 2,364 | 0.6% |
| str | 1,000 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 94,958,362,273 | 63.7% |
| Not specialized | 9,742,270,485 | 6.5% |
| Specialized | 44,465,893,486 | 29.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 1,111,039,688 | 22.1% |
| LOAD_ATTR | 1,036,972,453 | 20.7% |
| CALL | 894,017,459 | 17.8% |
| BINARY_OP | 841,004,606 | 16.8% |
| STORE_SUBSCR | 316,113,851 | 6.3% |
| FOR_ITER | 293,088,283 | 5.8% |
| TO_BOOL | 204,575,062 | 4.1% |
| COMPARE_OP | 145,487,134 | 2.9% |
| SEND | 112,702,882 | 2.2% |
| STORE_ATTR | 53,482,055 | 1.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 217,130,557 | 19.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 167,089,328 | 14.6% |
| STORE_ATTR_SLOT | 112,746,716 | 9.9% |
| CALL_PY_EXACT_ARGS | 89,523,665 | 7.8% |
| STORE_ATTR_INSTANCE_VALUE | 75,312,681 | 6.6% |
| FOR_ITER_LIST | 65,828,487 | 5.8% |
| FOR_ITER_TUPLE | 65,582,380 | 5.7% |
| LOAD_ATTR_SLOT | 57,466,381 | 5.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 50,962,802 | 4.5% |
| LOAD_ATTR_METHOD_NO_DICT | 45,168,272 | 3.9% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,218,655,664 | 23.2% |
| Calls to Python functions inlined | 4,030,178,423 | 76.8% |
| Calls via PyEval_EvalFrame (total) | 1,218,655,664 | 23.2% |
| Calls via PyEval_EvalFrame (vector) | 678,929,996 | 12.9% |
| Calls via PyEval_EvalFrame (generator) | 539,725,668 | 10.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 678,924,896 | 12.9% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 191,551,249 | 3.6% |
| Calls via PyEval_EvalFrame (function ex) | 13,969,119 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 115,825,241 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 94,989,360 | 1.8% |
| Frames pushed | 4,383,617,824 | 83.5% |
| Frame objects created | 59,301,984 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,166,344,681 | 35.3% |
| Frees to freelist | 4,170,463,239 |  |
| Allocations | 7,621,333,244 | 64.7% |
| Allocations to 512 bytes | 7,539,597,882 | 64.0% |
| Allocations to 4 kbytes | 66,551,050 | 0.6% |
| Allocations over 4 kbytes | 15,184,312 | 0.1% |
| Frees | 7,887,990,390 |  |
| New values | 57,542,936 |  |
| Interpreter increfs | 56,509,142,190 | 78.0% |
| Interpreter decrefs | 65,540,193,292 | 78.4% |
| Increfs | 15,944,402,978 | 22.0% |
| Decrefs | 18,105,778,012 | 21.6% |
| Materialize dict (on request) | 3,979,282 | 6.9% |
| Materialize dict (new key) | 142,640 | 0.2% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 1,524,462 | 2.6% |
| Method cache hits | 1,865,067,834 |  |
| Method cache misses | 68,004,682 |  |
| Method cache collisions | 73,105,843 |  |
| Method cache dunder hits | 2,210,151,534 |  |
| Method cache dunder misses | 5,141,551 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 345,461 | 34,722,278 | 3,464,100,346 |
| 1 | 30,682 | 65,127,585 | 2,927,545,172 |
| 2 | 14,202 | 40,814,674 | 9,811,975,217 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,278 |


</details>

---
Stats gathered on: 2023-08-10
