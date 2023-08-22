
# Pystats results

- fork: faster-cpython
- ref: incremental-gc
- commit hash: 97f762a
- commit date: 2023-08-12T23:12:50+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 27,634,511,116 | 18.7% | 18.7% |  |
| STORE_FAST | 9,812,072,767 | 6.6% | 25.3% |  |
| LOAD_CONST | 9,572,088,900 | 6.5% | 31.8% |  |
| POP_JUMP_IF_FALSE | 8,398,046,543 | 5.7% | 37.4% |  |
| LOAD_FAST_LOAD_FAST | 8,151,299,091 | 5.5% | 43.0% |  |
| RESUME | 4,956,013,594 | 3.3% | 46.3% |  |
| LOAD_GLOBAL_BUILTIN | 4,127,754,078 | 2.8% | 49.1% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,733,016,351 | 2.5% | 51.6% | 5.6% |
| JUMP_BACKWARD | 3,205,763,014 | 2.2% | 53.8% |  |
| TO_BOOL_BOOL | 3,185,593,600 | 2.2% | 55.9% | 0.0% |
| RETURN_VALUE | 2,982,306,261 | 2.0% | 58.0% |  |
| LOAD_GLOBAL_MODULE | 2,868,372,101 | 1.9% | 59.9% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,802,690,663 | 1.9% | 61.8% | 3.1% |
| BINARY_SUBSCR | 2,351,573,212 | 1.6% | 63.4% |  |
| POP_TOP | 2,338,521,962 | 1.6% | 65.0% |  |
| BINARY_OP_ADD_INT | 2,222,549,709 | 1.5% | 66.5% | 0.0% |
| CONTAINS_OP | 1,983,012,969 | 1.3% | 67.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,830,822,415 | 1.2% | 69.0% | 8.4% |
| COMPARE_OP_STR | 1,590,661,541 | 1.1% | 70.1% | 0.0% |
| STORE_FAST_STORE_FAST | 1,542,732,183 | 1.0% | 71.1% |  |
| COMPARE_OP_INT | 1,502,163,370 | 1.0% | 72.2% | 0.1% |
| NOP | 1,497,262,653 | 1.0% | 73.2% |  |
| POP_JUMP_IF_TRUE | 1,457,000,962 | 1.0% | 74.2% |  |
| LOAD_ATTR_SLOT | 1,345,022,501 | 0.9% | 75.1% | 4.3% |
| RETURN_CONST | 1,340,103,188 | 0.9% | 76.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,335,610,142 | 0.9% | 76.9% | 3.4% |
| FOR_ITER_LIST | 1,239,569,306 | 0.8% | 77.7% | 5.3% |
| INTERPRETER_EXIT | 1,210,025,576 | 0.8% | 78.5% |  |
| LOAD_ATTR | 1,072,049,106 | 0.7% | 79.3% |  |
| STORE_ATTR_SLOT | 1,062,933,829 | 0.7% | 80.0% | 10.6% |
| COPY | 1,056,406,780 | 0.7% | 80.7% |  |
| CALL_NO_KW_BUILTIN_FAST | 933,436,283 | 0.6% | 81.3% | 0.0% |
| SWAP | 931,247,763 | 0.6% | 81.9% |  |
| CALL | 894,321,881 | 0.6% | 82.6% |  |
| BINARY_SUBSCR_LIST_INT | 878,269,273 | 0.6% | 83.1% | 0.4% |
| BINARY_OP | 840,655,118 | 0.6% | 83.7% |  |
| LOAD_DEREF | 840,284,752 | 0.6% | 84.3% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,759,755 | 0.6% | 84.8% | 0.8% |
| CALL_NO_KW_ISINSTANCE | 810,216,098 | 0.5% | 85.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 808,352,952 | 0.5% | 85.9% | 8.6% |
| PUSH_NULL | 786,692,651 | 0.5% | 86.5% |  |
| CALL_NO_KW_BUILTIN_O | 785,532,000 | 0.5% | 87.0% | 0.1% |
| YIELD_VALUE | 693,472,908 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 692,889,807 | 0.5% | 87.9% |  |
| BINARY_SUBSCR_DICT | 622,311,324 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 605,523,596 | 0.4% | 88.8% |  |
| GET_ITER | 594,031,564 | 0.4% | 89.2% |  |
| BINARY_OP_SUBTRACT_INT | 499,708,959 | 0.3% | 89.5% | 0.1% |
| FOR_ITER_RANGE | 481,981,956 | 0.3% | 89.8% | 0.0% |
| IS_OP | 444,304,104 | 0.3% | 90.1% |  |
| UNPACK_SEQUENCE_TUPLE | 425,326,477 | 0.3% | 90.4% | 0.3% |
| FOR_ITER_TUPLE | 422,579,630 | 0.3% | 90.7% | 15.5% |
| POP_JUMP_IF_NOT_NONE | 419,728,091 | 0.3% | 91.0% |  |
| JUMP_FORWARD | 419,193,140 | 0.3% | 91.3% |  |
| BINARY_OP_ADD_FLOAT | 391,145,497 | 0.3% | 91.5% | 1.6% |
| TO_BOOL_NONE | 376,305,918 | 0.3% | 91.8% | 10.9% |
| LOAD_ATTR_WITH_HINT | 354,376,715 | 0.2% | 92.0% | 2.5% |
| CALL_NO_KW_LEN | 345,740,239 | 0.2% | 92.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 340,387,308 | 0.2% | 92.5% | 2.0% |
| LOAD_ATTR_MODULE | 339,683,099 | 0.2% | 92.7% | 0.0% |
| CALL_NO_KW_TYPE_1 | 335,992,470 | 0.2% | 92.9% |  |
| STORE_SUBSCR | 316,199,506 | 0.2% | 93.2% |  |
| EXTENDED_ARG | 308,252,860 | 0.2% | 93.4% |  |
| SEND_GEN | 302,363,233 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR_LIST_INT | 301,630,227 | 0.2% | 93.8% | 0.0% |
| BUILD_LIST | 301,062,100 | 0.2% | 94.0% |  |
| FOR_ITER | 293,150,155 | 0.2% | 94.2% |  |
| POP_JUMP_IF_NONE | 290,237,255 | 0.2% | 94.4% |  |
| BINARY_OP_SUBTRACT_FLOAT | 270,375,814 | 0.2% | 94.6% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 266,389,950 | 0.2% | 94.7% | 3.2% |
| COPY_FREE_VARS | 249,308,300 | 0.2% | 94.9% |  |
| BINARY_SLICE | 248,171,096 | 0.2% | 95.1% |  |
| CALL_NO_KW_LIST_APPEND | 239,601,350 | 0.2% | 95.2% | 0.0% |
| RETURN_GENERATOR | 238,824,705 | 0.2% | 95.4% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 233,380,564 | 0.2% | 95.6% | 6.9% |
| TO_BOOL_INT | 228,200,677 | 0.2% | 95.7% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 228,035,403 | 0.2% | 95.9% | 0.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,745,874 | 0.1% | 96.0% |  |
| TO_BOOL | 204,962,670 | 0.1% | 96.1% |  |
| STORE_SUBSCR_DICT | 198,930,960 | 0.1% | 96.3% |  |
| END_SEND | 194,308,829 | 0.1% | 96.4% |  |
| BINARY_SUBSCR_TUPLE_INT | 188,460,022 | 0.1% | 96.5% | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 178,900,709 | 0.1% | 96.7% | 21.3% |
| KW_NAMES | 172,945,011 | 0.1% | 96.8% |  |
| CALL_PY_WITH_DEFAULTS | 171,233,071 | 0.1% | 96.9% | 3.1% |
| BUILD_SLICE | 158,211,587 | 0.1% | 97.0% |  |
| CALL_INTRINSIC_1 | 154,034,541 | 0.1% | 97.1% |  |
| LIST_APPEND | 146,898,752 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,425,089 | 0.1% | 97.3% | 0.0% |
| COMPARE_OP | 145,533,964 | 0.1% | 97.4% |  |
| UNPACK_SEQUENCE_LIST | 140,233,880 | 0.1% | 97.5% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,652,137 | 0.1% | 97.6% | 19.1% |
| STORE_FAST_LOAD_FAST | 133,486,694 | 0.1% | 97.7% |  |
| DELETE_SUBSCR | 127,970,609 | 0.1% | 97.8% |  |
| CALL_BUILTIN_CLASS | 126,611,017 | 0.1% | 97.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 124,394,175 | 0.1% | 97.9% | 32.6% |
| UNARY_NEGATIVE | 121,275,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 121,010,089 | 0.1% | 98.1% | 1.1% |
| STORE_SLICE | 117,671,497 | 0.1% | 98.2% |  |
| FORMAT_SIMPLE | 117,345,605 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 114,367,798 | 0.1% | 98.3% |  |
| SEND | 112,730,656 | 0.1% | 98.4% |  |
| TO_BOOL_LIST | 111,941,195 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 111,060,902 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,738,812 | 0.1% | 98.6% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 94,841,299 | 0.1% | 98.8% |  |
| MAKE_CELL | 92,651,054 | 0.1% | 98.8% |  |
| FOR_ITER_GEN | 90,214,972 | 0.1% | 98.9% | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 87,704,621 | 0.1% | 98.9% | 2.0% |
| GET_AWAITABLE | 85,011,188 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 83,748,047 | 0.1% | 99.1% |  |
| CALL_FUNCTION_EX | 83,031,761 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,377,099 | 0.1% | 99.2% | 0.0% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,808,866 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 68,048,020 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 67,240,937 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 67,097,406 | 0.0% | 99.4% |  |
| STORE_DEREF | 65,761,437 | 0.0% | 99.4% |  |
| BUILD_MAP | 63,920,503 | 0.0% | 99.4% |  |
| BUILD_STRING | 59,066,533 | 0.0% | 99.5% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 56,935,136 | 0.0% | 99.5% | 0.0% |
| END_FOR | 56,701,034 | 0.0% | 99.6% |  |
| LIST_EXTEND | 54,325,482 | 0.0% | 99.6% |  |
| STORE_ATTR_WITH_HINT | 54,053,434 | 0.0% | 99.6% | 5.8% |
| STORE_ATTR | 53,544,183 | 0.0% | 99.7% |  |
| LOAD_FAST_AND_CLEAR | 52,305,949 | 0.0% | 99.7% |  |
| UNARY_NOT | 50,995,608 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 48,563,311 | 0.0% | 99.8% | 11.3% |
| MAP_ADD | 41,400,840 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,642,183 | 0.0% | 99.8% |  |
| CALL_NO_KW_TUPLE_1 | 22,405,429 | 0.0% | 99.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 22,351,800 | 0.0% | 99.9% | 0.0% |
| PUSH_EXC_INFO | 17,044,839 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,044,836 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,577,232 | 0.0% | 99.9% |  |
| DICT_MERGE | 16,230,689 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,170,580 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,416,351 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,524,248 | 0.0% | 100.0% |  |
| RERAISE | 8,497,221 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,377,568 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,298,675 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,700 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,924,440 | 0.0% | 100.0% |  |
| BEFORE_WITH | 5,238,799 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 4,632,806 | 0.0% | 100.0% |  |
| SET_ADD | 3,234,120 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 2,897,245 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,298,840 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,989,894 | 0.0% | 100.0% |  |
| BUILD_SET | 1,918,506 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,671,474 | 0.0% | 100.0% |  |
| DELETE_FAST | 623,760 | 0.0% | 100.0% |  |
| UNPACK_EX | 286,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 216,640 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 138,125 | 0.0% | 100.0% |  |
| SET_UPDATE | 66,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 51,517 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,993 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,433 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,413 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,220 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,580 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 837 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 5,016,456,885 | 3.4% | 3.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,423,887,748 | 3.0% | 6.4% |
| STORE_FAST LOAD_FAST | 4,407,789,953 | 3.0% | 9.4% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,170,438,074 | 2.1% | 11.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,662,298,741 | 1.8% | 13.3% |
| CALL_PY_EXACT_ARGS RESUME | 2,492,675,824 | 1.7% | 15.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,325,238,823 | 1.6% | 16.6% |
| RESUME LOAD_FAST | 2,064,849,539 | 1.4% | 18.0% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,870,207,665 | 1.3% | 19.2% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,771,624,342 | 1.2% | 20.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,566,130,391 | 1.1% | 21.5% |
| LOAD_CONST COMPARE_OP_STR | 1,563,963,594 | 1.1% | 22.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,550,228,013 | 1.0% | 23.6% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 1,436,494,400 | 1.0% | 24.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,332,262,896 | 0.9% | 25.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,265,507,416 | 0.9% | 26.3% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,763,702 | 0.9% | 27.2% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,229,236,566 | 0.8% | 28.0% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,183,197,861 | 0.8% | 28.8% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,097,548,458 | 0.7% | 29.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,053,415,163 | 0.7% | 30.2% |
| LOAD_CONST LOAD_FAST | 1,051,102,108 | 0.7% | 30.9% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,415,720 | 0.7% | 31.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 980,819,358 | 0.7% | 32.3% |
| BINARY_SUBSCR STORE_FAST | 977,845,748 | 0.7% | 32.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 969,533,677 | 0.7% | 33.6% |
| NOP LOAD_FAST_LOAD_FAST | 959,959,585 | 0.6% | 34.2% |
| LOAD_FAST LOAD_FAST | 939,304,823 | 0.6% | 34.9% |
| JUMP_BACKWARD FOR_ITER_LIST | 924,155,046 | 0.6% | 35.5% |
| STORE_FAST JUMP_BACKWARD | 918,432,356 | 0.6% | 36.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 899,688,131 | 0.6% | 36.7% |
| BINARY_SUBSCR LOAD_FAST | 879,036,850 | 0.6% | 37.3% |
| RESUME LOAD_GLOBAL_BUILTIN | 844,727,012 | 0.6% | 37.9% |
| POP_TOP LOAD_FAST | 832,485,905 | 0.6% | 38.5% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,163,560 | 0.6% | 39.0% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 797,075,854 | 0.5% | 39.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 792,685,653 | 0.5% | 40.1% |
| LOAD_FAST RETURN_VALUE | 773,811,772 | 0.5% | 40.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 768,715,647 | 0.5% | 41.1% |
| LOAD_CONST LOAD_CONST | 744,381,158 | 0.5% | 41.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 738,371,208 | 0.5% | 42.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 725,076,449 | 0.5% | 42.6% |
| JUMP_BACKWARD NOP | 718,029,615 | 0.5% | 43.1% |
| LOAD_FAST TO_BOOL_BOOL | 715,260,566 | 0.5% | 43.6% |
| STORE_FAST STORE_FAST | 711,189,610 | 0.5% | 44.1% |
| LOAD_CONST COMPARE_OP_INT | 670,912,674 | 0.5% | 44.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 664,982,570 | 0.4% | 45.0% |
| POP_TOP JUMP_BACKWARD | 657,945,721 | 0.4% | 45.4% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 638,784,324 | 0.4% | 45.8% |
| RETURN_VALUE STORE_FAST | 618,259,847 | 0.4% | 46.3% |
| LOAD_FAST LOAD_ATTR | 592,530,064 | 0.4% | 46.7% |
| FOR_ITER_LIST STORE_FAST | 587,143,262 | 0.4% | 47.1% |
| POP_JUMP_IF_TRUE LOAD_FAST | 573,785,381 | 0.4% | 47.4% |
| RETURN_CONST POP_TOP | 569,578,492 | 0.4% | 47.8% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 539,786,865 | 0.4% | 48.2% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,153,020 | 0.4% | 48.6% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 536,619,613 | 0.4% | 48.9% |
| LOAD_DEREF LOAD_FAST | 531,041,308 | 0.4% | 49.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 519,318,114 | 0.4% | 49.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 515,586,137 | 0.3% | 50.0% |
| LOAD_FAST CONTAINS_OP | 510,851,315 | 0.3% | 50.3% |
| RETURN_VALUE RETURN_VALUE | 509,441,684 | 0.3% | 50.7% |
| LOAD_FAST STORE_ATTR_SLOT | 504,072,010 | 0.3% | 51.0% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,699,651 | 0.3% | 51.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 474,672,952 | 0.3% | 51.7% |
| RESUME POP_TOP | 472,273,823 | 0.3% | 52.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 465,310,055 | 0.3% | 52.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 459,576,326 | 0.3% | 52.6% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 458,551,963 | 0.3% | 52.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 452,908,493 | 0.3% | 53.2% |
| YIELD_VALUE INTERPRETER_EXIT | 451,458,887 | 0.3% | 53.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 449,377,333 | 0.3% | 53.8% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 444,392,169 | 0.3% | 54.1% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.4% |
| PUSH_NULL LOAD_FAST | 433,937,967 | 0.3% | 54.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 428,907,444 | 0.3% | 55.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 428,126,672 | 0.3% | 55.3% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 425,979,144 | 0.3% | 55.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 420,491,015 | 0.3% | 55.9% |
| LOAD_CONST STORE_FAST | 420,257,845 | 0.3% | 56.1% |
| BUILD_TUPLE RETURN_VALUE | 413,113,751 | 0.3% | 56.4% |
| RETURN_CONST INTERPRETER_EXIT | 410,732,684 | 0.3% | 56.7% |
| FOR_ITER_RANGE STORE_FAST | 396,715,978 | 0.3% | 57.0% |
| IS_OP POP_JUMP_IF_FALSE | 375,960,552 | 0.3% | 57.2% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 368,123,276 | 0.2% | 57.5% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 365,584,591 | 0.2% | 57.7% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 359,286,813 | 0.2% | 58.0% |
| NOP LOAD_FAST | 358,588,506 | 0.2% | 58.2% |
| LOAD_FAST BINARY_SUBSCR | 357,874,618 | 0.2% | 58.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 346,404,897 | 0.2% | 58.7% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 342,572,117 | 0.2% | 58.9% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,715,832 | 0.2% | 59.1% |
| STORE_FAST LOAD_DEREF | 341,240,889 | 0.2% | 59.4% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 339,144,414 | 0.2% | 59.6% |
| RESUME NOP | 337,434,454 | 0.2% | 59.8% |
| RESUME LOAD_GLOBAL_MODULE | 336,656,407 | 0.2% | 60.1% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 332,290,930 | 0.2% | 60.3% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 331,860,871 | 0.2% | 60.5% |
| RETURN_VALUE INTERPRETER_EXIT | 329,657,531 | 0.2% | 60.7% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 328,985,525 | 0.2% | 61.0% |


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
| RETURN_VALUE | 2,415,325 | 46.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,273,728 | 43.4% |
| LOAD_GLOBAL_MODULE | 210,134 | 4.0% |
| LOAD_ATTR_WITH_HINT | 132,420 | 2.5% |
| LOAD_FAST | 132,060 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,628,808 | 88.4% |
| STORE_FAST | 608,551 | 11.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 247,643,215 | 29.5% |
| LOAD_FAST | 170,130,527 | 20.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.6% |
| LOAD_FAST_LOAD_FAST | 47,865,881 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,910 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 153,738,150 | 18.3% |
| LOAD_FAST | 134,404,817 | 16.0% |
| LOAD_FAST_LOAD_FAST | 106,872,480 | 12.7% |
| LOAD_CONST | 90,465,868 | 10.8% |
| RETURN_VALUE | 69,617,576 | 8.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,109,360 | 72.6% |
| LOAD_FAST | 65,388,462 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,256,842 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,612,542 | 29.8% |
| STORE_FAST | 116,100,631 | 29.7% |
| LOAD_FAST | 59,771,004 | 15.3% |
| RETURN_VALUE | 31,351,200 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,771,624,342 | 79.7% |
| LOAD_FAST | 244,325,012 | 11.0% |
| LOAD_FAST_LOAD_FAST | 94,838,479 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,763,702 | 56.6% |
| LOAD_CONST | 132,210,856 | 5.9% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,092,137 | 4.3% |
| BINARY_SUBSCR | 89,539,800 | 4.0% |


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
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,233,480 | 1.8% |

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
| LOAD_FAST | 3,731,940 | 63.0% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,840 | 8.6% |
| LOAD_CONST | 60,360 | 1.0% |
| LOAD_FAST_LOAD_FAST | 24,300 | 0.4% |


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
| BINARY_OP_ADD_INT | 96,092,137 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,998 | 19.2% |
| LOAD_FAST_LOAD_FAST | 44,913,098 | 16.9% |
| LOAD_FAST | 38,771,060 | 14.6% |
| BINARY_OP | 27,332,895 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,212,341 | 23.4% |
| LOAD_CONST | 61,632,913 | 23.1% |
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
| LOAD_FAST | 69,610,864 | 25.7% |
| LOAD_FAST_LOAD_FAST | 36,420,236 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 28,678,232 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,598,616 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.1% |
| SWAP | 55,832,922 | 20.7% |
| LOAD_FAST | 28,365,798 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 365,584,591 | 73.2% |
| LOAD_FAST | 78,848,225 | 15.8% |
| LOAD_FAST_LOAD_FAST | 30,056,126 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 21,634,479 | 4.3% |
| CALL_NO_KW_LEN | 2,724,600 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,030,606 | 19.2% |
| CALL_PY_EXACT_ARGS | 94,404,100 | 18.9% |
| SWAP | 68,653,066 | 13.7% |
| RETURN_VALUE | 40,190,960 | 8.0% |
| BINARY_OP | 37,297,198 | 7.5% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 137,122,490 | 55.3% |
| BINARY_OP_ADD_INT | 40,077,824 | 16.1% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.1% |
| LOAD_FAST | 24,932,062 | 10.0% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 57,269,248 | 23.1% |
| GET_ITER | 33,199,100 | 13.4% |
| CALL_PY_EXACT_ARGS | 25,430,562 | 10.2% |
| BUILD_TUPLE | 24,334,500 | 9.8% |
| LOAD_DEREF | 18,985,680 | 7.7% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,436,494,400 | 61.1% |
| LOAD_FAST | 357,874,618 | 15.2% |
| LOAD_CONST | 139,740,029 | 5.9% |
| COPY | 109,830,240 | 4.7% |
| BUILD_SLICE | 104,833,980 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 977,845,748 | 41.6% |
| LOAD_FAST | 879,036,850 | 37.4% |
| LOAD_FAST_LOAD_FAST | 110,207,520 | 4.7% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |
| BINARY_SUBSCR | 48,587,981 | 2.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,811,146 | 33.2% |
| LOAD_FAST | 205,307,561 | 33.0% |
| LOAD_FAST_LOAD_FAST | 135,438,749 | 21.8% |
| BINARY_SUBSCR | 41,253,840 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,001,231 | 38.1% |
| RETURN_VALUE | 104,203,695 | 16.7% |
| CONTAINS_OP | 77,768,700 | 12.5% |
| LOAD_FAST | 60,021,665 | 9.6% |
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
| LOAD_FAST | 3,530,309 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,060 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,516,829 | 99.4% |
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
| LOAD_FAST | 270,630,032 | 30.8% |
| LOAD_CONST | 180,974,746 | 20.6% |
| COPY | 157,633,500 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,808,935 | 17.6% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 233,334,370 | 26.6% |
| LOAD_CONST | 192,236,280 | 21.9% |
| LOAD_FAST | 140,961,239 | 16.1% |
| RETURN_VALUE | 90,406,836 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 148,324,479 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.1% |
| LOAD_FAST_LOAD_FAST | 329,577 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 2,526 | 0.0% |
| BINARY_SUBSCR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,900 | 38.3% |
| LOAD_CONST | 24,654,420 | 13.1% |
| LOAD_FAST | 24,246,777 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.3% |
| STORE_FAST | 8,763,770 | 4.7% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,632,806 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,034,757 | 43.9% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 36.8% |
| STORE_FAST | 383,025 | 8.3% |
| RETURN_VALUE | 144,336 | 3.1% |
| CALL_NO_KW_LIST_APPEND | 132,780 | 2.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,264,407 | 38.6% |
| LOAD_ATTR_SLOT | 38,398,061 | 12.8% |
| SWAP | 32,340,063 | 10.7% |
| LOAD_FAST | 26,259,932 | 8.7% |
| RESUME | 18,138,677 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 129,090,949 | 42.9% |
| LOAD_FAST | 89,925,360 | 29.9% |
| SWAP | 32,376,096 | 10.8% |
| CALL | 9,652,840 | 3.2% |
| RETURN_VALUE | 9,311,866 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,290,236 | 16.1% |
| RESUME | 6,807,930 | 10.7% |
| LOAD_FAST | 6,700,836 | 10.5% |
| CALL_INTRINSIC_1 | 6,518,817 | 10.2% |
| SWAP | 6,077,760 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,056,533 | 37.6% |
| LOAD_FAST | 23,229,284 | 36.3% |
| SWAP | 6,077,760 | 9.5% |
| CALL_FUNCTION_EX | 3,407,815 | 5.3% |
| LOAD_CONST | 2,982,591 | 4.7% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| LOAD_CONST | 142,320 | 7.4% |
| LOAD_GLOBAL_MODULE | 142,206 | 7.4% |
| LOAD_ATTR | 66,000 | 3.4% |
| LOAD_FAST | 52,920 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| CONTAINS_OP | 141,846 | 7.4% |
| LOAD_CONST | 74,280 | 3.9% |
| BINARY_OP | 68,400 | 3.6% |
| STORE_FAST | 48,240 | 2.5% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,375,152 | 99.5% |
| LOAD_FAST | 780,995 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,980 | 66.3% |
| DELETE_SUBSCR | 53,377,607 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 52,318,980 | 88.6% |
| LOAD_CONST | 6,747,553 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.1% |
| CALL | 12,296,999 | 20.8% |
| STORE_FAST | 4,750,184 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,919,836 | 29.9% |
| LOAD_CONST | 167,604,908 | 24.2% |
| LOAD_FAST_LOAD_FAST | 126,884,743 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 40,167,299 | 5.8% |
| CALL | 38,800,735 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 413,113,751 | 59.6% |
| LOAD_CONST | 82,951,019 | 12.0% |
| CALL_NO_KW_ISINSTANCE | 40,155,939 | 5.8% |
| STORE_FAST | 30,270,377 | 4.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 256,840,603 | 28.7% |
| KW_NAMES | 149,653,475 | 16.7% |
| LOAD_FAST_LOAD_FAST | 99,239,547 | 11.1% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,900 | 8.1% |
| LOAD_GLOBAL_MODULE | 49,106,341 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 305,129,498 | 34.1% |
| RESUME | 211,832,104 | 23.7% |
| RETURN_VALUE | 51,148,599 | 5.7% |
| POP_TOP | 47,310,722 | 5.3% |
| LOAD_GLOBAL_MODULE | 39,306,609 | 4.4% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,871,060 | 30.9% |
| LOAD_CONST | 23,537,074 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.2% |
| LOAD_FAST_LOAD_FAST | 21,625,934 | 15.6% |
| LOAD_ATTR_INSTANCE_VALUE | 6,372,297 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,992,123 | 78.6% |
| COPY_FREE_VARS | 26,910,158 | 19.4% |
| POP_TOP | 2,068,114 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,544 | 0.3% |
| MAKE_CELL | 172,402 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,472,549 | 28.8% |
| CALL_NO_KW_LEN | 23,247,403 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 10,772,871 | 8.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 9,078,500 | 7.2% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,636,081 | 50.3% |
| STORE_FAST | 13,560,170 | 10.7% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.1% |
| LOAD_FAST | 10,269,411 | 8.1% |
| CALL_BUILTIN_CLASS | 4,229,103 | 3.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,880 | 43.2% |
| KW_NAMES | 22,239,736 | 29.1% |
| LOAD_FAST | 13,404,074 | 17.5% |
| LOAD_FAST_LOAD_FAST | 2,766,726 | 3.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,137,420 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,880 | 41.0% |
| STORE_FAST | 27,917,948 | 36.6% |
| POP_TOP | 8,840,117 | 11.6% |
| RETURN_VALUE | 5,704,006 | 7.5% |
| BINARY_OP_ADD_INT | 930,900 | 1.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,153,861 | 52.0% |
| DICT_MERGE | 16,230,689 | 19.5% |
| LOAD_FAST | 10,562,879 | 12.7% |
| LOAD_FAST_LOAD_FAST | 5,883,400 | 7.1% |
| BUILD_MAP | 3,407,815 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,279,218 | 56.9% |
| STORE_FAST | 8,427,426 | 10.1% |
| RESUME | 7,481,060 | 9.0% |
| RETURN_VALUE | 6,927,247 | 8.3% |
| MAKE_CELL | 4,744,457 | 5.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 59.7% |
| LIST_EXTEND | 53,505,353 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.1% |
| RERAISE | 42,039 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 61.1% |
| CALL_FUNCTION_EX | 43,153,861 | 28.0% |
| BUILD_MAP | 6,518,817 | 4.2% |
| RERAISE | 6,380,908 | 4.1% |
| LOAD_CONST | 3,819,535 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,944,083 | 72.9% |
| LOAD_FAST | 10,476,562 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,512,540 | 8.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,177,293 | 4.8% |
| LOAD_FAST_LOAD_FAST | 1,043,428 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 70,524,940 | 80.4% |
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
| LOAD_GLOBAL_MODULE | 9,494,413 | 13.8% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.0% |
| RETURN_CONST | 7,864,740 | 11.4% |
| BINARY_OP_ADD_FLOAT | 5,101,500 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,395,776 | 95.0% |
| COPY_FREE_VARS | 1,701,510 | 2.5% |
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
| LOAD_CONST | 339,144,414 | 36.3% |
| LOAD_FAST_LOAD_FAST | 72,296,433 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,219,603 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,699,651 | 51.2% |
| STORE_FAST | 310,642,043 | 33.3% |
| POP_TOP | 47,791,853 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 22,195,596 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,786,865 | 68.7% |
| LOAD_CONST | 55,891,716 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,644,325 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,715,832 | 43.5% |
| LOAD_CONST | 171,775,857 | 21.9% |
| STORE_FAST | 166,546,899 | 21.2% |
| RETURN_VALUE | 29,452,318 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,260 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 342,572,117 | 42.3% |
| LOAD_GLOBAL_BUILTIN | 331,860,871 | 41.0% |
| LOAD_FAST_LOAD_FAST | 61,753,438 | 7.6% |
| BUILD_TUPLE | 40,155,939 | 5.0% |
| LOAD_ATTR_MODULE | 22,115,024 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 797,075,854 | 98.4% |
| COPY | 6,062,177 | 0.7% |
| RETURN_VALUE | 2,415,607 | 0.3% |
| POP_TOP | 1,996,800 | 0.2% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 214,111,964 | 61.9% |
| LOAD_ATTR_INSTANCE_VALUE | 55,120,627 | 15.9% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 8.5% |
| LOAD_DEREF | 20,449,960 | 5.9% |
| LOAD_ATTR_SLOT | 8,655,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,800,384 | 35.8% |
| LOAD_FAST | 55,702,950 | 16.1% |
| STORE_FAST | 44,233,242 | 12.8% |
| COMPARE_OP_INT | 32,613,692 | 9.4% |
| CALL_BUILTIN_CLASS | 23,247,403 | 6.7% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,300,585 | 72.7% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 18,543,217 | 7.7% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 5,805,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 90,819,084 | 37.9% |
| LOAD_FAST | 72,490,401 | 30.3% |
| EXTENDED_ARG | 27,822,060 | 11.6% |
| RETURN_CONST | 20,554,860 | 8.6% |
| LOAD_CONST | 11,304,039 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,341,365 | 52.4% |
| LOAD_FAST_LOAD_FAST | 56,756,330 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 50,383,385 | 14.8% |
| LOAD_CONST | 27,324,965 | 8.0% |
| LOAD_ATTR_SLOT | 8,567,760 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 249,366,113 | 73.3% |
| LIST_APPEND | 28,917,240 | 8.5% |
| RETURN_VALUE | 11,797,610 | 3.5% |
| LOAD_FAST | 10,857,720 | 3.2% |
| POP_TOP | 9,139,748 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 151,122,309 | 64.8% |
| LOAD_ATTR | 72,900,582 | 31.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,473,061 | 3.2% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 302,632 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 73,505,290 | 31.5% |
| TO_BOOL_BOOL | 60,228,791 | 25.8% |
| GET_ITER | 33,735,960 | 14.5% |
| LOAD_GLOBAL_MODULE | 18,632,700 | 8.0% |
| LOAD_FAST | 12,556,454 | 5.4% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,471,010 | 76.9% |
| CALL | 19,599,082 | 8.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.0% |
| CALL_NO_KW_BUILTIN_FAST | 6,014,137 | 2.6% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 111,508,498 | 48.9% |
| BINARY_OP | 72,002,140 | 31.6% |
| RETURN_VALUE | 23,756,118 | 10.4% |
| STORE_FAST | 6,977,504 | 3.1% |
| LOAD_FAST | 5,874,060 | 2.6% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,382,663 | 91.3% |
| RETURN_VALUE | 1,727,780 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,230,540 | 3.3% |
| LOAD_ATTR | 89,100 | 0.2% |
| CALL_NO_KW_TUPLE_1 | 66,000 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.7% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 28.8% |
| STORE_FAST | 5,604,303 | 14.9% |
| RETURN_VALUE | 3,244,980 | 8.6% |
| BUILD_LIST | 1,966,480 | 5.2% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,919,797 | 66.6% |
| RETURN_GENERATOR | 5,526,160 | 24.7% |
| LOAD_ATTR_SLOT | 1,098,632 | 4.9% |
| CALL | 436,440 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 63.8% |
| BUILD_TUPLE | 2,891,792 | 12.9% |
| YIELD_VALUE | 2,419,200 | 10.8% |
| RETURN_VALUE | 1,003,837 | 4.5% |
| STORE_FAST | 642,060 | 2.9% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 332,290,930 | 98.9% |
| LOAD_CONST | 3,615,840 | 1.1% |
| BINARY_SUBSCR_TUPLE_INT | 66,000 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,418,260 | 85.5% |
| LOAD_GLOBAL_MODULE | 13,779,657 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 12,241,650 | 3.6% |
| CALL_PY_EXACT_ARGS | 8,082,189 | 2.4% |
| LOAD_FAST | 7,606,680 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 969,533,677 | 34.6% |
| LOAD_FAST_LOAD_FAST | 638,784,324 | 22.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 428,907,444 | 15.3% |
| LOAD_GLOBAL_MODULE | 165,494,061 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 111,391,983 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,492,675,824 | 88.9% |
| RETURN_GENERATOR | 140,432,166 | 5.0% |
| COPY_FREE_VARS | 121,553,538 | 4.3% |
| MAKE_CELL | 31,461,819 | 1.1% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,969,250 | 55.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,255,230 | 7.2% |
| LOAD_ATTR_METHOD_NO_DICT | 12,068,800 | 7.0% |
| LOAD_ATTR | 11,206,124 | 6.5% |
| LOAD_CONST | 8,918,513 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 165,090,622 | 96.4% |
| RETURN_GENERATOR | 3,374,706 | 2.0% |
| MAKE_CELL | 1,593,330 | 0.9% |
| COPY_FREE_VARS | 1,067,463 | 0.6% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,417,652 | 93.0% |
| LOAD_GLOBAL_MODULE | 690,039 | 4.2% |
| BUILD_TUPLE | 359,940 | 2.2% |
| LOAD_ATTR_MODULE | 109,568 | 0.7% |
| LOAD_GLOBAL | 30 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,577,232 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 438 | 52.3% |
| CALL_INTRINSIC_1 | 240 | 28.7% |
| JUMP_BACKWARD | 159 | 19.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 46,492,501 | 31.9% |
| LOAD_FAST_LOAD_FAST | 32,739,500 | 22.5% |
| LOAD_ATTR | 15,308,322 | 10.5% |
| LOAD_ATTR_SLOT | 13,757,980 | 9.5% |
| LOAD_FAST | 10,889,700 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 78,702,884 | 54.1% |
| POP_JUMP_IF_TRUE | 38,840,703 | 26.7% |
| COPY | 18,630,898 | 12.8% |
| RETURN_VALUE | 7,089,996 | 4.9% |
| EXTENDED_ARG | 1,918,719 | 1.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 66,486,598 | 59.9% |
| BINARY_SUBSCR | 23,382,660 | 21.1% |
| LOAD_CONST | 6,328,743 | 5.7% |
| LOAD_FAST | 6,313,834 | 5.7% |
| LOAD_GLOBAL_MODULE | 3,631,951 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,486,778 | 43.7% |
| POP_JUMP_IF_TRUE | 32,445,960 | 29.2% |
| POP_JUMP_IF_FALSE | 30,127,424 | 27.1% |
| COMPARE_OP | 380 | 0.0% |
| EXTENDED_ARG | 340 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 670,912,674 | 44.7% |
| LOAD_ATTR_INSTANCE_VALUE | 172,366,483 | 11.5% |
| LOAD_FAST | 121,639,236 | 8.1% |
| LOAD_FAST_LOAD_FAST | 120,552,686 | 8.0% |
| COPY | 109,001,674 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,265,507,416 | 84.2% |
| POP_JUMP_IF_TRUE | 122,125,341 | 8.1% |
| RETURN_VALUE | 59,381,804 | 4.0% |
| EXTENDED_ARG | 22,449,480 | 1.5% |
| LOAD_FAST | 15,024,000 | 1.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,563,963,594 | 98.3% |
| LOAD_FAST | 8,980,332 | 0.6% |
| LOAD_GLOBAL_MODULE | 5,060,552 | 0.3% |
| RETURN_VALUE | 4,023,960 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,550,228,013 | 97.5% |
| POP_JUMP_IF_TRUE | 27,393,551 | 1.7% |
| COPY | 6,090,420 | 0.4% |
| RETURN_VALUE | 4,403,657 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,415,720 | 49.9% |
| LOAD_FAST | 510,851,315 | 25.8% |
| LOAD_GLOBAL_MODULE | 301,873,345 | 15.2% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 44,337,659 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,870,207,665 | 94.3% |
| POP_JUMP_IF_TRUE | 60,477,432 | 3.0% |
| RETURN_VALUE | 25,865,640 | 1.3% |
| COPY | 21,273,120 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,368,500 | 48.6% |
| LOAD_FAST_LOAD_FAST | 36,024,720 | 34.7% |
| LOAD_ATTR | 11,580,660 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,738,812 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,850,166 | 25.4% |
| LOAD_FAST | 237,464,485 | 22.5% |
| LOAD_FAST_LOAD_FAST | 120,961,740 | 11.5% |
| SWAP | 112,621,732 | 10.7% |
| LOAD_CONST | 95,324,000 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,850,166 | 25.4% |
| TO_BOOL_BOOL | 215,369,716 | 20.4% |
| BINARY_SUBSCR_LIST_INT | 157,633,500 | 14.9% |
| BINARY_SUBSCR | 109,830,240 | 10.4% |
| COMPARE_OP_INT | 109,001,674 | 10.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 121,553,538 | 75.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,910,158 | 16.7% |
| CALL | 9,063,674 | 5.6% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,701,510 | 1.1% |
| CALL_PY_WITH_DEFAULTS | 1,067,463 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 175,683,208 | 70.5% |
| RETURN_GENERATOR | 73,605,232 | 29.5% |
| MAKE_CELL | 19,860 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,524,008 | 100.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,654,672 | 78.1% |
| NOP | 1,715,434 | 20.1% |
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
| STORE_FAST | 223,779 | 35.9% |
| CALL | 155,337 | 24.9% |
| POP_TOP | 78,092 | 12.5% |
| NOP | 55,216 | 8.9% |
| STORE_ATTR_INSTANCE_VALUE | 55,100 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 212,937 | 34.1% |
| RERAISE | 151,239 | 24.2% |
| RETURN_CONST | 110,252 | 17.7% |
| JUMP_FORWARD | 66,240 | 10.6% |
| LOAD_FAST | 57,946 | 9.3% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,193,436 | 57.2% |
| BUILD_SLICE | 53,377,607 | 41.7% |
| LOAD_FAST | 1,016,104 | 0.8% |
| LOAD_CONST | 286,740 | 0.2% |
| LOAD_ATTR_SLOT | 66,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,533,679 | 84.1% |
| LOAD_CONST | 18,169,145 | 14.2% |
| JUMP_BACKWARD | 1,105,140 | 0.9% |
| RETURN_CONST | 540,793 | 0.4% |
| LOAD_FAST_LOAD_FAST | 274,632 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,443,060 | 95.1% |
| RETURN_VALUE | 376,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 218,706 | 1.3% |
| LOAD_DEREF | 112,763 | 0.7% |
| LOAD_GLOBAL_MODULE | 36,997 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,230,689 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 36,997 | 71.8% |
| LOAD_FAST | 13,140 | 25.5% |
| BUILD_MAP | 540 | 1.0% |
| RETURN_VALUE | 480 | 0.9% |
| MAP_ADD | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,537 | 72.9% |
| DICT_MERGE | 13,140 | 25.5% |
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
| RETURN_CONST | 56,701,034 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,101,420 | 33.7% |
| RETURN_CONST | 789,600 | 1.4% |
| LOAD_CONST | 5,940 | 0.0% |
| NOP | 4,980 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,455,138 | 51.7% |
| RETURN_VALUE | 69,221,684 | 35.6% |
| RETURN_CONST | 24,631,728 | 12.7% |
| JUMP_BACKWARD | 159 | 0.0% |
| SEND_GEN | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,093,103 | 48.9% |
| POP_TOP | 36,246,174 | 18.7% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,940 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 67,097,406 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,097,406 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 88,770,707 | 28.8% |
| LOAD_FAST | 42,655,580 | 13.8% |
| JUMP_BACKWARD | 40,665,600 | 13.2% |
| CALL_NO_KW_LIST_APPEND | 27,822,060 | 9.0% |
| COMPARE_OP_INT | 22,449,480 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 138,159,920 | 44.8% |
| JUMP_BACKWARD | 54,300,832 | 17.6% |
| FOR_ITER_LIST | 38,691,700 | 12.6% |
| POP_JUMP_IF_NONE | 36,519,160 | 11.8% |
| FOR_ITER | 16,516,640 | 5.4% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,738,812 | 88.4% |
| LOAD_FAST | 9,752,769 | 8.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,423,980 | 1.2% |
| RETURN_VALUE | 1,042,740 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,137,948 | 50.4% |
| BUILD_STRING | 52,318,980 | 44.6% |
| LOAD_FAST | 5,879,857 | 5.0% |
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
| JUMP_BACKWARD | 212,761,233 | 72.6% |
| GET_ITER | 53,883,771 | 18.4% |
| EXTENDED_ARG | 16,516,640 | 5.6% |
| SWAP | 6,717,703 | 2.3% |
| LOAD_FAST | 3,174,157 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 151,762,728 | 51.8% |
| STORE_FAST | 76,706,678 | 26.2% |
| LOAD_FAST | 19,227,122 | 6.6% |
| RETURN_CONST | 15,910,117 | 5.4% |
| PUSH_NULL | 7,956,120 | 2.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,713,320 | 62.9% |
| JUMP_BACKWARD | 33,136,718 | 36.7% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,240 | 0.0% |
| SWAP | 1,314 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,764,934 | 62.9% |
| RESUME | 33,449,498 | 37.1% |
| RETURN_CONST | 300 | 0.0% |
| STORE_FAST | 240 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 924,155,046 | 74.6% |
| GET_ITER | 190,426,525 | 15.4% |
| LOAD_FAST | 59,098,400 | 4.8% |
| EXTENDED_ARG | 38,691,700 | 3.1% |
| SWAP | 25,954,726 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 587,143,262 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,608,474 | 25.4% |
| RETURN_CONST | 103,915,416 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,513,880 | 6.5% |
| LOAD_FAST | 59,110,495 | 4.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 428,126,672 | 88.8% |
| GET_ITER | 27,232,064 | 5.7% |
| LOAD_FAST | 21,531,300 | 4.5% |
| SWAP | 4,261,440 | 0.9% |
| EXTENDED_ARG | 829,380 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 396,715,978 | 82.3% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.3% |
| RETURN_CONST | 24,277,777 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,297,696 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 292,045,142 | 69.1% |
| GET_ITER | 124,938,992 | 29.6% |
| SWAP | 2,996,680 | 0.7% |
| LOAD_FAST | 1,260,632 | 0.3% |
| FOR_ITER_LIST | 1,236,439 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 290,650,813 | 68.8% |
| LOAD_FAST | 61,885,522 | 14.6% |
| LOAD_FAST_LOAD_FAST | 43,821,240 | 10.4% |
| RETURN_CONST | 12,360,924 | 2.9% |
| STORE_FAST_LOAD_FAST | 5,123,040 | 1.2% |


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
| RETURN_GENERATOR | 78,585,971 | 92.4% |
| LOAD_FAST | 3,323,640 | 3.9% |
| RETURN_VALUE | 2,594,819 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 489,658 | 0.6% |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,011,188 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,741,965 | 36.0% |
| LOAD_ATTR_INSTANCE_VALUE | 78,053,184 | 13.1% |
| CALL_BUILTIN_CLASS | 63,636,081 | 10.7% |
| RETURN_VALUE | 50,004,231 | 8.4% |
| LOAD_ATTR_SLOT | 38,736,054 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 190,426,525 | 32.1% |
| FOR_ITER_TUPLE | 124,938,992 | 21.0% |
| CALL_PY_EXACT_ARGS | 85,106,409 | 14.3% |
| FOR_ITER_GEN | 56,713,320 | 9.5% |
| FOR_ITER | 53,883,771 | 9.1% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 12,000,420 | 79.1% |
| RETURN_GENERATOR | 3,161,760 | 20.8% |
| LOAD_FAST | 7,080 | 0.0% |
| LOAD_ATTR_SLOT | 1,320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,170,580 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 1,538,754 | 77.3% |
| STORE_FAST | 451,140 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,989,774 | 100.0% |
| PUSH_EXC_INFO | 120 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,671,474 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,538,754 | 92.1% |
| STORE_FAST | 132,120 | 7.9% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,353 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,413 | 52.3% |
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
| INSTRUMENTED_POP_JUMP_IF_TRUE | 873 | 11.8% |
| LIST_APPEND | 300 | 4.0% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,353 | 58.7% |
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
| TO_BOOL_BOOL | 5,313 | 53.2% |
| TO_BOOL | 3,060 | 30.6% |
| TO_BOOL_STR | 960 | 9.6% |
| TO_BOOL_NONE | 300 | 3.0% |
| COMPARE_OP_STR | 240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.6% |
| LOAD_GLOBAL | 4,020 | 40.2% |
| INSTRUMENTED_JUMP_BACKWARD | 873 | 8.7% |
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
| YIELD_VALUE | 451,458,887 | 37.3% |
| RETURN_CONST | 410,732,684 | 33.9% |
| RETURN_VALUE | 329,657,531 | 27.2% |
| RETURN_GENERATOR | 18,176,234 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,239,460 | 48.7% |
| LOAD_FAST_LOAD_FAST | 111,729,089 | 25.1% |
| LOAD_GLOBAL_MODULE | 81,532,511 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 15,924,230 | 3.6% |
| LOAD_CONST | 8,662,851 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 375,960,552 | 84.6% |
| POP_JUMP_IF_TRUE | 39,091,917 | 8.8% |
| EXTENDED_ARG | 18,199,680 | 4.1% |
| RETURN_VALUE | 3,377,395 | 0.8% |
| COPY | 3,174,640 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,432,356 | 28.6% |
| POP_TOP | 657,945,721 | 20.5% |
| POP_JUMP_IF_TRUE | 465,310,055 | 14.5% |
| POP_JUMP_IF_FALSE | 444,392,169 | 13.9% |
| LIST_APPEND | 146,790,923 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 924,155,046 | 28.8% |
| NOP | 718,029,615 | 22.4% |
| FOR_ITER_RANGE | 428,126,672 | 13.4% |
| FOR_ITER_TUPLE | 292,045,142 | 9.1% |
| LOAD_FAST | 280,753,634 | 8.8% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,745,874 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,500,302 | 97.1% |
| SEND | 6,245,572 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 171,866,864 | 41.0% |
| POP_JUMP_IF_FALSE | 100,900,398 | 24.1% |
| POP_TOP | 56,127,989 | 13.4% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| EXTENDED_ARG | 14,628,780 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 164,028,507 | 39.1% |
| LOAD_FAST_LOAD_FAST | 82,377,099 | 19.7% |
| LOAD_CONST | 37,404,815 | 8.9% |
| LOAD_GLOBAL_MODULE | 28,035,056 | 6.7% |
| LOAD_GLOBAL_BUILTIN | 25,956,179 | 6.2% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,205,066 | 23.8% |
| LOAD_CONST | 38,153,718 | 22.1% |
| LOAD_FAST_LOAD_FAST | 35,511,202 | 20.5% |
| LOAD_GLOBAL_MODULE | 18,005,252 | 10.4% |
| LOAD_ATTR_INSTANCE_VALUE | 11,379,556 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 149,653,475 | 86.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 22,239,736 | 12.9% |
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
| LOAD_FAST | 18,295,907 | 12.5% |
| RETURN_VALUE | 15,138,559 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,790,923 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |
| CALL | 9 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 38,199,581 | 70.3% |
| LOAD_FAST | 15,433,143 | 28.4% |
| LOAD_CONST | 366,720 | 0.7% |
| RETURN_VALUE | 205,963 | 0.4% |
| LOAD_DEREF | 77,526 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 53,505,353 | 98.5% |
| STORE_FAST | 426,357 | 0.8% |
| LOAD_FAST | 217,312 | 0.4% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 592,530,064 | 55.3% |
| LOAD_GLOBAL_BUILTIN | 221,923,460 | 20.7% |
| LOAD_GLOBAL_MODULE | 95,605,741 | 8.9% |
| LOAD_ATTR_SLOT | 81,102,280 | 7.6% |
| LOAD_FAST_LOAD_FAST | 26,581,235 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 219,261,480 | 20.5% |
| IS_OP | 216,239,460 | 20.2% |
| STORE_FAST | 170,130,800 | 15.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 72,900,582 | 6.8% |
| LOAD_FAST_LOAD_FAST | 60,668,956 | 5.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,575,225 | 96.3% |
| LOAD_GLOBAL_BUILTIN | 1,785,580 | 1.5% |
| LOAD_FAST | 1,408,580 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 543,824 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,811,231 | 49.4% |
| LOAD_FAST | 21,988,579 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,858,993 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,920 | 2.3% |
| LOAD_FAST_LOAD_FAST | 2,450,700 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,170,438,074 | 84.9% |
| LOAD_FAST_LOAD_FAST | 328,985,525 | 8.8% |
| COPY | 77,249,123 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,396,209 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,053,415,163 | 28.2% |
| TO_BOOL_BOOL | 425,979,144 | 11.4% |
| STORE_FAST | 278,665,993 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 189,983,544 | 5.1% |
| RETURN_VALUE | 176,805,132 | 4.7% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40,723,364 | 71.5% |
| LOAD_FAST | 16,211,332 | 28.5% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,575,076 | 69.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,473,061 | 13.1% |
| LOAD_GLOBAL_MODULE | 5,902,417 | 10.4% |
| LOAD_CONST | 2,491,800 | 4.4% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 768,715,647 | 57.6% |
| LOAD_ATTR_INSTANCE_VALUE | 189,983,544 | 14.2% |
| LOAD_CONST | 90,379,296 | 6.8% |
| LOAD_GLOBAL_MODULE | 52,878,410 | 4.0% |
| LOAD_ATTR_SLOT | 48,976,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 664,982,570 | 49.8% |
| LOAD_CONST | 155,809,501 | 11.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 151,122,309 | 11.3% |
| LOAD_FAST_LOAD_FAST | 111,681,978 | 8.4% |
| CALL_PY_EXACT_ARGS | 111,391,983 | 8.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,566,130,391 | 85.5% |
| LOAD_ATTR_INSTANCE_VALUE | 63,474,590 | 3.5% |
| LOAD_ATTR | 45,749,349 | 2.5% |
| LOAD_ATTR_SLOT | 45,629,594 | 2.5% |
| LOAD_ATTR_WITH_HINT | 37,390,573 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 792,685,653 | 43.3% |
| LOAD_FAST_LOAD_FAST | 474,672,952 | 25.9% |
| CALL_PY_EXACT_ARGS | 428,907,444 | 23.4% |
| LOAD_GLOBAL_MODULE | 55,446,147 | 3.0% |
| LOAD_CONST | 53,011,467 | 2.9% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 324,173,430 | 95.4% |
| LOAD_ATTR_MODULE | 11,618,940 | 3.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,324,680 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,919,393 | 33.5% |
| LOAD_FAST_LOAD_FAST | 101,061,511 | 29.8% |
| CALL | 27,523,170 | 8.1% |
| CALL_NO_KW_ISINSTANCE | 22,115,024 | 6.5% |
| LOAD_CONST | 15,919,142 | 4.7% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,484,760 | 73.8% |
| LOAD_FAST_LOAD_FAST | 5,866,920 | 26.2% |
| LOAD_ATTR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,387,760 | 37.5% |
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
| LOAD_FAST | 111,820,021 | 89.9% |
| LOAD_FAST_LOAD_FAST | 10,750,129 | 8.6% |
| LOAD_ATTR_INSTANCE_VALUE | 868,485 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 757,860 | 0.6% |
| STORE_FAST_LOAD_FAST | 181,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,601,084 | 24.6% |
| LOAD_FAST_LOAD_FAST | 27,613,920 | 22.2% |
| LOAD_GLOBAL_BUILTIN | 15,217,140 | 12.2% |
| LOAD_ATTR_METHOD_NO_DICT | 10,309,640 | 8.3% |
| BINARY_OP | 6,990,093 | 5.6% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,553,757 | 83.5% |
| LOAD_ATTR_SLOT | 5,106,841 | 10.5% |
| RETURN_VALUE | 1,327,483 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,064,880 | 2.2% |
| LOAD_FAST_LOAD_FAST | 125,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 42,922,210 | 88.4% |
| TO_BOOL_NONE | 3,107,760 | 6.4% |
| RETURN_VALUE | 831,680 | 1.7% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,236,566 | 91.4% |
| LOAD_ATTR_SLOT | 40,651,881 | 3.0% |
| COPY | 40,401,402 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,278,674 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,012,508 | 22.8% |
| TO_BOOL_NONE | 88,082,271 | 6.5% |
| LOAD_ATTR | 81,102,280 | 6.0% |
| TO_BOOL_BOOL | 68,852,344 | 5.1% |
| COMPARE_OP_FLOAT | 66,486,598 | 4.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 281,509,778 | 79.4% |
| LOAD_ATTR_INSTANCE_VALUE | 22,667,586 | 6.4% |
| LOAD_ATTR_WITH_HINT | 22,490,592 | 6.3% |
| COPY | 14,038,524 | 4.0% |
| LOAD_FAST_LOAD_FAST | 8,682,059 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,595,344 | 24.2% |
| STORE_FAST | 43,356,660 | 12.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 37,390,573 | 10.6% |
| COMPARE_OP_INT | 35,280,990 | 10.0% |
| LOAD_CONST | 29,603,520 | 8.4% |


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
| LOAD_FAST | 5,016,456,885 | 52.4% |
| LOAD_CONST | 744,381,158 | 7.8% |
| LOAD_FAST_LOAD_FAST | 458,551,963 | 4.8% |
| STORE_FAST | 292,604,779 | 3.1% |
| POP_JUMP_IF_FALSE | 274,564,498 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,771,624,342 | 18.5% |
| COMPARE_OP_STR | 1,563,963,594 | 16.3% |
| LOAD_FAST | 1,051,102,108 | 11.0% |
| LOAD_CONST | 744,381,158 | 7.8% |
| COMPARE_OP_INT | 670,912,674 | 7.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 341,240,889 | 40.6% |
| LOAD_GLOBAL_BUILTIN | 107,448,457 | 12.8% |
| PUSH_NULL | 38,331,717 | 4.6% |
| POP_JUMP_IF_FALSE | 32,319,622 | 3.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 531,041,308 | 63.2% |
| LOAD_CONST | 69,819,321 | 8.3% |
| LOAD_FAST_LOAD_FAST | 29,843,294 | 3.6% |
| LOAD_DEREF | 24,559,774 | 2.9% |
| CALL_NO_KW_LEN | 20,449,960 | 2.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,423,887,748 | 16.0% |
| STORE_FAST | 4,407,789,953 | 16.0% |
| LOAD_GLOBAL_BUILTIN | 2,662,298,741 | 9.6% |
| RESUME | 2,064,849,539 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,053,415,163 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,016,456,885 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 3,170,438,074 | 11.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,566,130,391 | 5.7% |
| LOAD_ATTR_SLOT | 1,229,236,566 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,097,548,458 | 4.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 39,931,923 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,374,026 | 23.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 39,923,763 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,374,026 | 23.7% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,682,680 | 50.5% |
| POP_TOP | 2,058,305 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 421,860 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 339,225 | 4.6% |
| STORE_FAST | 308,760 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 49.0% |
| POP_JUMP_IF_NOT_NONE | 1,511,040 | 20.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 5.9% |
| LOAD_FAST | 383,640 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 335,025 | 4.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,332,262,896 | 16.3% |
| POP_JUMP_IF_FALSE | 1,183,197,861 | 14.5% |
| NOP | 959,959,585 | 11.8% |
| LOAD_FAST_LOAD_FAST | 519,318,114 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 474,672,952 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,436,494,400 | 17.6% |
| CONTAINS_OP | 989,415,720 | 12.1% |
| LOAD_FAST | 738,371,208 | 9.1% |
| CALL_PY_EXACT_ARGS | 638,784,324 | 7.8% |
| LOAD_FAST_LOAD_FAST | 519,318,114 | 6.4% |


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
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 98.8% |
| STORE_FAST | 20,188 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 8,308 | 0.1% |
| NOP | 4,607 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,599 | 98.9% |
| LOAD_GLOBAL_MODULE | 42,855 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 15,823 | 0.2% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,603 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,097,548,458 | 26.6% |
| POP_JUMP_IF_FALSE | 980,819,358 | 23.8% |
| RESUME | 844,727,012 | 20.5% |
| STORE_FAST | 536,619,613 | 13.0% |
| POP_JUMP_IF_TRUE | 98,145,385 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,662,298,741 | 64.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.5% |
| CALL_NO_KW_ISINSTANCE | 331,860,871 | 8.0% |
| LOAD_ATTR | 221,923,460 | 5.4% |
| LOAD_FAST_LOAD_FAST | 113,563,744 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 899,688,131 | 31.4% |
| STORE_FAST | 420,491,015 | 14.7% |
| RESUME | 336,656,407 | 11.7% |
| POP_JUMP_IF_FALSE | 272,960,804 | 9.5% |
| LOAD_FAST_LOAD_FAST | 125,773,889 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 459,576,326 | 16.0% |
| LOAD_FAST | 449,377,333 | 15.7% |
| CALL_NO_KW_ISINSTANCE | 342,572,117 | 11.9% |
| LOAD_ATTR_MODULE | 324,173,430 | 11.3% |
| CONTAINS_OP | 301,873,345 | 10.5% |


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
| LOAD_FAST | 1,460 | 92.4% |
| EXTENDED_ARG | 60 | 3.8% |
| LOAD_DEREF | 60 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,460 | 92.4% |
| LOAD_SUPER_ATTR_ATTR | 120 | 7.6% |


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
| LOAD_FAST | 2,218,380 | 96.5% |
| LOAD_GLOBAL_MODULE | 65,560 | 2.9% |
| LOAD_FAST_LOAD_FAST | 10,200 | 0.4% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_CONST | 240 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,357,258 | 100.0% |
| LOAD_DEREF | 9,080 | 0.0% |
| LOAD_SUPER_ATTR | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,699,015 | 54.8% |
| LOAD_FAST | 37,260,637 | 32.6% |
| CALL_PY_EXACT_ARGS | 6,406,107 | 5.6% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.2% |
| CALL | 1,200,040 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,471,041 | 53.6% |
| CALL_PY_EXACT_ARGS | 31,461,819 | 34.1% |
| CALL_FUNCTION_EX | 4,744,457 | 5.1% |
| CALL | 4,133,185 | 4.5% |
| CALL_PY_WITH_DEFAULTS | 1,593,330 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,471,041 | 53.4% |
| RESUME | 42,515,933 | 45.9% |
| RETURN_GENERATOR | 655,920 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,841,299 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 82,638,479 | 87.1% |
| LOAD_FAST | 8,773,080 | 9.3% |
| LOAD_GLOBAL_MODULE | 2,504,360 | 2.6% |
| PUSH_NULL | 289,380 | 0.3% |
| KW_NAMES | 255,360 | 0.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,896,280 | 38.4% |
| RETURN_VALUE | 6,380,580 | 15.4% |
| LOAD_FAST | 6,188,730 | 14.9% |
| JUMP_FORWARD | 4,782,840 | 11.6% |
| STORE_FAST | 4,549,800 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,597,580 | 49.8% |
| JUMP_BACKWARD | 19,591,440 | 47.3% |
| CALL_FUNCTION_EX | 1,211,460 | 2.9% |
| DICT_UPDATE | 180 | 0.0% |
| BUILD_MAP | 120 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 718,029,615 | 48.0% |
| RESUME | 337,434,454 | 22.5% |
| STORE_FAST | 158,947,484 | 10.6% |
| POP_JUMP_IF_FALSE | 80,714,860 | 5.4% |
| NOP | 52,970,376 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 959,959,585 | 64.1% |
| LOAD_FAST | 358,588,506 | 23.9% |
| NOP | 52,970,376 | 3.5% |
| PUSH_NULL | 43,637,447 | 2.9% |
| LOAD_GLOBAL_BUILTIN | 34,248,460 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,940,070 | 58.3% |
| STORE_SUBSCR_DICT | 3,085,425 | 18.1% |
| SWAP | 1,973,496 | 11.6% |
| COPY | 1,285,201 | 7.5% |
| STORE_FAST | 547,196 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,501,070 | 55.7% |
| RETURN_VALUE | 1,913,807 | 11.2% |
| JUMP_FORWARD | 1,715,820 | 10.1% |
| POP_TOP | 1,385,126 | 8.1% |
| RERAISE | 1,285,201 | 7.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,325,238,823 | 27.7% |
| CONTAINS_OP | 1,870,207,665 | 22.3% |
| COMPARE_OP_STR | 1,550,228,013 | 18.5% |
| COMPARE_OP_INT | 1,265,507,416 | 15.1% |
| IS_OP | 375,960,552 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,423,887,748 | 52.7% |
| LOAD_FAST_LOAD_FAST | 1,183,197,861 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 980,819,358 | 11.7% |
| JUMP_BACKWARD | 444,392,169 | 5.3% |
| LOAD_CONST | 274,564,498 | 3.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 194,987,062 | 67.2% |
| EXTENDED_ARG | 36,519,160 | 12.6% |
| LOAD_ATTR_SLOT | 25,425,420 | 8.8% |
| LOAD_DEREF | 13,782,341 | 4.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,407,799 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,750,075 | 45.0% |
| PUSH_NULL | 53,765,463 | 18.5% |
| LOAD_DEREF | 28,701,623 | 9.9% |
| JUMP_BACKWARD | 20,410,122 | 7.0% |
| RETURN_CONST | 15,885,434 | 5.5% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 346,404,897 | 82.5% |
| LOAD_ATTR_INSTANCE_VALUE | 27,639,437 | 6.6% |
| LOAD_ATTR | 14,144,191 | 3.4% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.1% |
| EXTENDED_ARG | 7,255,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 148,389,758 | 35.4% |
| LOAD_GLOBAL_BUILTIN | 96,627,731 | 23.0% |
| LOAD_FAST_LOAD_FAST | 58,938,657 | 14.0% |
| LOAD_GLOBAL_MODULE | 36,033,947 | 8.6% |
| PUSH_NULL | 18,681,152 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 725,076,449 | 49.8% |
| TO_BOOL | 132,361,036 | 9.1% |
| COMPARE_OP_INT | 122,125,341 | 8.4% |
| TO_BOOL_ALWAYS_TRUE | 82,915,713 | 5.7% |
| TO_BOOL_NONE | 77,693,798 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 573,785,381 | 39.4% |
| JUMP_BACKWARD | 465,310,055 | 31.9% |
| LOAD_GLOBAL_BUILTIN | 98,145,385 | 6.7% |
| LOAD_CONST | 68,427,717 | 4.7% |
| POP_TOP | 66,409,329 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 569,578,492 | 25.3% |
| RESUME | 472,273,823 | 21.0% |
| CALL_NO_KW_BUILTIN_O | 341,715,832 | 15.2% |
| POP_JUMP_IF_FALSE | 161,932,950 | 7.2% |
| RETURN_VALUE | 121,192,650 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 832,485,905 | 35.6% |
| JUMP_BACKWARD | 657,945,721 | 28.1% |
| RESUME | 238,824,705 | 10.2% |
| RETURN_CONST | 184,065,007 | 7.9% |
| LOAD_FAST_LOAD_FAST | 99,543,805 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,215,808 | 30.7% |
| LOAD_ATTR | 3,246,420 | 19.1% |
| RAISE_VARARGS | 2,298,205 | 13.5% |
| CALL_NO_KW_BUILTIN_FAST | 1,785,274 | 10.5% |
| RERAISE | 1,115,623 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,415,132 | 90.4% |
| LOAD_GLOBAL_MODULE | 1,103,712 | 6.5% |
| LOAD_FAST | 387,189 | 2.3% |
| WITH_EXCEPT_START | 138,125 | 0.8% |
| LOAD_GLOBAL | 613 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 274,214,974 | 34.9% |
| POP_JUMP_IF_FALSE | 114,548,372 | 14.6% |
| POP_TOP | 70,762,487 | 9.0% |
| POP_JUMP_IF_NONE | 53,765,463 | 6.8% |
| NOP | 43,637,447 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 433,937,967 | 55.2% |
| LOAD_FAST_LOAD_FAST | 310,622,232 | 39.5% |
| LOAD_DEREF | 38,331,717 | 4.9% |
| LOAD_GLOBAL_BUILTIN | 3,416,040 | 0.4% |
| PUSH_NULL | 273,335 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,494,521 | 51.6% |
| LOAD_ATTR_MODULE | 583,740 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 18.8% |
| LOAD_FAST | 151,179 | 5.2% |
| RETURN_VALUE | 55,440 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,298,205 | 79.4% |
| COPY | 445,440 | 15.4% |
| LOAD_CONST | 151,239 | 5.2% |
| CALL_INTRINSIC_1 | 21 | 0.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,380,908 | 75.1% |
| POP_EXCEPT | 1,285,201 | 15.1% |
| POP_TOP | 386,940 | 4.6% |
| POP_JUMP_IF_FALSE | 155,520 | 1.8% |
| DELETE_FAST | 151,239 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,115,623 | 56.1% |
| COPY | 831,112 | 41.8% |
| CALL_INTRINSIC_1 | 42,039 | 2.1% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,492,675,824 | 63.3% |
| POP_TOP | 238,824,705 | 6.1% |
| CALL | 211,832,104 | 5.4% |
| SEND_GEN | 208,500,245 | 5.3% |
| COPY_FREE_VARS | 175,683,208 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,064,849,539 | 41.7% |
| LOAD_GLOBAL_BUILTIN | 844,727,012 | 17.0% |
| POP_TOP | 472,273,823 | 9.5% |
| NOP | 337,434,454 | 6.8% |
| LOAD_GLOBAL_MODULE | 336,656,407 | 6.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 267,494,960 | 20.0% |
| STORE_ATTR_SLOT | 246,973,722 | 18.4% |
| POP_TOP | 184,065,007 | 13.7% |
| STORE_ATTR_INSTANCE_VALUE | 174,468,053 | 13.0% |
| RESUME | 122,771,700 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 569,578,492 | 42.5% |
| INTERPRETER_EXIT | 410,732,684 | 30.6% |
| EXIT_INIT_CHECK | 67,097,406 | 5.0% |
| TO_BOOL_BOOL | 56,811,847 | 4.2% |
| END_FOR | 56,701,034 | 4.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,432,166 | 63.6% |
| COPY_FREE_VARS | 73,605,232 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,374,706 | 1.5% |
| CALL_FUNCTION_EX | 1,715,674 | 0.8% |
| CALL | 873,337 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,585,971 | 32.9% |
| GET_ITER | 37,670,520 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,880 | 13.8% |
| STORE_FAST | 19,530,120 | 8.2% |
| INTERPRETER_EXIT | 18,176,234 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 773,811,772 | 25.9% |
| RETURN_VALUE | 509,441,684 | 17.1% |
| BUILD_TUPLE | 413,113,751 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 176,805,132 | 5.9% |
| BINARY_SUBSCR_DICT | 104,203,695 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 618,259,847 | 20.7% |
| RETURN_VALUE | 509,441,684 | 17.1% |
| INTERPRETER_EXIT | 329,657,531 | 11.1% |
| UNPACK_SEQUENCE_TUPLE | 264,500,837 | 8.9% |
| TO_BOOL_BOOL | 251,512,584 | 8.4% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,456,200 | 94.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,245,572 | 5.5% |
| SEND | 28,884 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,455,138 | 89.1% |
| YIELD_VALUE | 6,246,028 | 5.5% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,884 | 0.0% |
| SEND_GEN | 603 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,500,302 | 69.0% |
| LOAD_CONST | 93,862,328 | 31.0% |
| SEND | 603 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,500,245 | 69.0% |
| POP_TOP | 93,862,808 | 31.0% |
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
| MAKE_FUNCTION | 82,638,479 | 98.7% |
| SET_FUNCTION_ATTRIBUTE | 1,109,568 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,219,232 | 64.7% |
| LOAD_GLOBAL_BUILTIN | 18,989,340 | 22.7% |
| STORE_FAST | 5,795,581 | 6.9% |
| CALL_PY_EXACT_ARGS | 2,063,017 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 1,109,568 | 1.3% |


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
| LOAD_FAST | 31,581,206 | 59.0% |
| LOAD_FAST_LOAD_FAST | 15,245,033 | 28.5% |
| CALL | 5,419,260 | 10.1% |
| SWAP | 946,682 | 1.8% |
| LOAD_GLOBAL_MODULE | 199,180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,910,817 | 29.7% |
| LOAD_DEREF | 13,447,060 | 25.1% |
| RETURN_CONST | 8,606,156 | 16.1% |
| JUMP_BACKWARD | 5,554,200 | 10.4% |
| LOAD_FAST_LOAD_FAST | 4,744,229 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 359,286,813 | 44.4% |
| LOAD_FAST_LOAD_FAST | 296,788,825 | 36.7% |
| SWAP | 77,249,123 | 9.6% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.4% |
| RETURN_VALUE | 20,943,360 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 295,130,428 | 36.5% |
| RETURN_CONST | 174,468,053 | 21.6% |
| LOAD_FAST_LOAD_FAST | 167,680,857 | 20.7% |
| LOAD_CONST | 67,550,811 | 8.4% |
| NOP | 51,797,134 | 6.4% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 515,586,137 | 48.5% |
| LOAD_FAST | 504,072,010 | 47.4% |
| SWAP | 40,401,402 | 3.8% |
| STORE_ATTR_SLOT | 2,127,184 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 279,506,651 | 26.3% |
| LOAD_FAST | 253,876,344 | 23.9% |
| RETURN_CONST | 246,973,722 | 23.2% |
| LOAD_CONST | 220,187,745 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 25,391,400 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,039,039 | 50.0% |
| SWAP | 14,038,524 | 26.0% |
| LOAD_FAST_LOAD_FAST | 12,443,829 | 23.0% |
| LOAD_DEREF | 242,460 | 0.4% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,962,831 | 62.8% |
| RETURN_CONST | 6,694,841 | 12.4% |
| JUMP_BACKWARD | 5,313,540 | 9.8% |
| LOAD_CONST | 3,923,998 | 7.3% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.3% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,874,000 | 40.9% |
| STORE_FAST | 19,047,660 | 29.0% |
| LOAD_CONST | 6,838,848 | 10.4% |
| LOAD_FAST | 2,917,140 | 4.4% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,460 | 28.9% |
| LOAD_DEREF | 13,769,864 | 20.9% |
| LOAD_FAST_LOAD_FAST | 13,437,000 | 20.4% |
| LOAD_FAST | 9,631,683 | 14.6% |
| LOAD_CONST | 4,834,987 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,763,702 | 12.8% |
| BINARY_SUBSCR | 977,845,748 | 10.0% |
| STORE_FAST | 711,189,610 | 7.2% |
| RETURN_VALUE | 618,259,847 | 6.3% |
| FOR_ITER_LIST | 587,143,262 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,407,789,953 | 44.9% |
| LOAD_FAST_LOAD_FAST | 1,332,262,896 | 13.6% |
| JUMP_BACKWARD | 918,432,356 | 9.4% |
| STORE_FAST | 711,189,610 | 7.2% |
| LOAD_GLOBAL_BUILTIN | 536,619,613 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,513,880 | 60.3% |
| FOR_ITER_RANGE | 35,405,280 | 26.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,140 | 6.9% |
| FOR_ITER_TUPLE | 5,123,040 | 3.8% |
| FOR_ITER | 2,965,743 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,780 | 22.2% |
| LOAD_FAST | 24,358,500 | 18.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,555,720 | 15.4% |
| STORE_ATTR_INSTANCE_VALUE | 9,297,393 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,560 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 368,123,276 | 23.9% |
| UNPACK_SEQUENCE_TUPLE | 140,575,262 | 9.1% |
| UNPACK_SEQUENCE_LIST | 134,204,860 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,560 | 52.8% |
| LOAD_FAST | 452,908,493 | 29.4% |
| LOAD_FAST_LOAD_FAST | 86,509,868 | 5.6% |
| STORE_FAST | 75,477,042 | 4.9% |
| LOAD_GLOBAL_MODULE | 46,179,114 | 3.0% |


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
| LOAD_CONST | 13,495,717 | 11.5% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,615,197 | 91.5% |
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
| SWAP | 109,838,120 | 34.7% |
| LOAD_FAST | 64,774,561 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 17.9% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.1% |
| LOAD_CONST | 27,783,040 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.4% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 32.9% |
| RETURN_CONST | 33,885,783 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,003,020 | 8.5% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 95,460,730 | 48.0% |
| LOAD_FAST | 63,111,369 | 31.7% |
| CALL_NO_KW_BUILTIN_O | 13,999,260 | 7.0% |
| RETURN_VALUE | 7,992,040 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,054,143 | 36.7% |
| LOAD_FAST | 66,038,961 | 33.2% |
| JUMP_BACKWARD | 31,629,390 | 15.9% |
| RETURN_CONST | 12,893,538 | 6.5% |
| LOAD_GLOBAL_MODULE | 7,343,163 | 3.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,500 | 52.3% |
| LOAD_FAST | 56,880,860 | 18.9% |
| LOAD_CONST | 26,911,957 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,058,910 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,905,360 | 38.1% |
| JUMP_BACKWARD | 110,076,370 | 36.5% |
| LOAD_FAST_LOAD_FAST | 71,546,740 | 23.7% |
| RETURN_CONST | 4,469,760 | 1.5% |
| LOAD_CONST | 230,760 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,850,166 | 28.9% |
| BINARY_OP_ADD_FLOAT | 116,612,542 | 12.5% |
| LOAD_FAST | 105,289,368 | 11.3% |
| BINARY_OP_ADD_INT | 88,097,096 | 9.5% |
| BINARY_OP_SUBTRACT_INT | 68,653,066 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,850,166 | 28.9% |
| STORE_SUBSCR_LIST_INT | 157,633,500 | 16.9% |
| COPY | 112,621,732 | 12.1% |
| STORE_SUBSCR | 109,838,120 | 11.8% |
| STORE_ATTR_INSTANCE_VALUE | 77,249,123 | 8.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,771,648 | 80.9% |
| LOAD_ATTR_INSTANCE_VALUE | 23,952,916 | 11.7% |
| LOAD_ATTR | 7,358,299 | 3.6% |
| LOAD_ATTR_SLOT | 3,352,620 | 1.6% |
| COPY | 2,331,394 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 132,361,036 | 64.6% |
| POP_JUMP_IF_FALSE | 71,873,396 | 35.1% |
| TO_BOOL | 235,796 | 0.1% |
| UNARY_NOT | 220,620 | 0.1% |
| TO_BOOL_NONE | 125,693 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,565,608 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,746,340 | 33.4% |
| LOAD_ATTR_SLOT | 17,761,080 | 9.9% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 7,172,907 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 94,344,467 | 52.7% |
| POP_JUMP_IF_TRUE | 82,915,713 | 46.3% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,846 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,503 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 797,075,854 | 25.0% |
| LOAD_FAST | 715,260,566 | 22.5% |
| CALL_NO_KW_BUILTIN_FAST | 477,699,651 | 15.0% |
| LOAD_ATTR_INSTANCE_VALUE | 425,979,144 | 13.4% |
| RETURN_VALUE | 251,512,584 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,325,238,823 | 73.0% |
| POP_JUMP_IF_TRUE | 725,076,449 | 22.8% |
| EXTENDED_ARG | 88,770,707 | 2.8% |
| UNARY_NOT | 46,465,128 | 1.5% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 173,514,676 | 76.0% |
| CALL_NO_KW_BUILTIN_O | 12,836,580 | 5.6% |
| COPY | 12,653,528 | 5.5% |
| BINARY_OP | 9,119,194 | 4.0% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,385,530 | 88.2% |
| POP_JUMP_IF_TRUE | 25,597,261 | 11.2% |
| UNARY_NOT | 1,035,600 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,863,468 | 66.9% |
| LOAD_ATTR_INSTANCE_VALUE | 27,751,322 | 24.8% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,712,180 | 1.5% |
| COPY | 814,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,666,753 | 55.1% |
| POP_JUMP_IF_FALSE | 46,705,322 | 41.7% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,760 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,518,234 | 45.0% |
| LOAD_ATTR_SLOT | 88,082,271 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 53,032,666 | 14.1% |
| LOAD_ATTR | 21,871,157 | 5.8% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 296,855,222 | 78.9% |
| POP_JUMP_IF_TRUE | 77,693,798 | 20.6% |
| EXTENDED_ARG | 967,320 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,931 | 0.2% |
| TO_BOOL | 123,667 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,965,997 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,407,740 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,340 | 5.8% |
| COPY | 2,682,160 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 36,172,677 | 53.8% |
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
| BINARY_OP | 10,588,000 | 92.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 384,332 | 3.4% |
| LOAD_ATTR_MODULE | 311,719 | 2.7% |
| LOAD_FAST | 122,040 | 1.1% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,416,351 | 100.0% |


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
| TO_BOOL_BOOL | 46,465,128 | 91.1% |
| TO_BOOL_LIST | 2,640,720 | 5.2% |
| TO_BOOL_INT | 1,035,600 | 2.0% |
| TO_BOOL_STR | 600,240 | 1.2% |
| TO_BOOL | 220,620 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 23,463,060 | 46.0% |
| RETURN_VALUE | 15,181,728 | 29.8% |
| KW_NAMES | 10,514,640 | 20.6% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.5% |
| LOAD_FAST | 555,240 | 1.1% |


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
| STORE_FAST_STORE_FAST | 134,280 | 62.0% |
| STORE_FAST | 79,690 | 36.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,730 | 0.8% |
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
| STORE_FAST | 6,001,600 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 799,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,204,860 | 95.7% |
| STORE_FAST | 6,004,980 | 4.3% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 264,500,837 | 62.2% |
| LOAD_FAST | 103,134,100 | 24.2% |
| BINARY_SUBSCR_DICT | 15,509,545 | 3.6% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260,434,075 | 61.2% |
| STORE_FAST_STORE_FAST | 140,575,262 | 33.1% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.6% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,608,474 | 52.0% |
| FOR_ITER | 151,762,728 | 25.1% |
| RETURN_VALUE | 84,701,839 | 14.0% |
| LOAD_FAST | 35,337,180 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 368,123,276 | 60.8% |
| STORE_FAST | 215,215,620 | 35.5% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST_LOAD_FAST | 9,187,140 | 1.5% |
| LOAD_FAST | 906,540 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 138,125 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 137,332 | 99.4% |
| TO_BOOL_BOOL | 780 | 0.6% |
| TO_BOOL | 13 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.4% |
| YIELD_VALUE | 208,500,623 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,298 | 4.5% |
| LOAD_CONST | 26,891,183 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 451,458,887 | 65.1% |
| YIELD_VALUE | 208,500,623 | 30.1% |
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
| specialization.deferred |    204565074 | 4.7% |
| specialization.deopt |      1599013 | 0.0% |
|          hit |   4063403074 | 93.3% |
|         miss |     84779962 | 1.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,613,046 | 80.8% |
| Failure | 383,563 | 19.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.4% |
| other | 125,980 | 32.8% |
| tuple | 75,020 | 19.6% |
| dict | 16,814 | 4.4% |
| bytes | 10,789 | 2.8% |
| set | 7,220 | 1.9% |
| sequence | 6,018 | 1.6% |
| mapping | 4,602 | 1.2% |
| float | 980 | 0.3% |
| bytearray | 320 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2350979393 | 56.1% |
| specialization.deopt |        65092 | 0.0% |
|          hit |   1832014589 | 43.8% |
|         miss |      3451119 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 67,130 | 10.2% |
| Failure | 591,781 | 89.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 305,140 | 51.6% |
| array int | 112,980 | 19.1% |
| other | 77,500 | 13.1% |
| out of range | 40,462 | 6.8% |
| buffer int | 25,739 | 4.3% |
| list slice | 25,520 | 4.3% |
| sequence int | 2,920 | 0.5% |
| code complex parameters | 1,420 | 0.2% |
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
| specialization.deferred |    316114000 | 38.7% |
| specialization.deopt |           40 | 0.0% |
|          hit |    500558967 | 61.3% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,749 | 2.0% |
| Failure | 83,797 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.5% |
| dict subclass no override | 17,960 | 21.4% |
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
| specialization.deferred |       213970 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1168536253 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,290 | 99.1% |
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
| specialization.deferred |    293052445 | 11.6% |
| specialization.deopt |      2480414 | 0.1% |
|          hit |   2102883130 | 83.2% |
|         miss |    131462734 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,473 | 96.3% |
| Failure | 96,651 | 3.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,020 | 23.8% |
| dict items | 20,434 | 21.1% |
| seq iter | 15,120 | 15.6% |
| set | 13,199 | 13.7% |
| other | 7,660 | 7.9% |
| dict values | 3,820 | 4.0% |
| reversed list | 3,640 | 3.8% |
| zip | 3,400 | 3.5% |
| ascii string | 2,680 | 2.8% |
| dict keys | 2,060 | 2.1% |
| itertools | 820 | 0.8% |
| map | 600 | 0.6% |
| callable | 120 | 0.1% |
| bytes | 78 | 0.1% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     53482809 | 2.7% |
| specialization.deopt |      3491310 | 0.2% |
|          hit |   1740288100 | 87.9% |
|         miss |    185052115 | 9.4% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,513,942 | 98.9% |
| Failure | 38,742 | 1.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,280 | 44.6% |
| not in dict | 10,940 | 28.2% |
| overriding descriptor | 5,020 | 13.0% |
| property | 1,220 | 3.1% |
| not in keys | 960 | 2.5% |
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
| specialization.deferred |   1070521508 | 10.3% |
| specialization.deopt |      9839275 | 0.1% |
|          hit |   8790151970 | 84.7% |
|         miss |    521633764 | 5.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,910,416 | 87.2% |
| Failure | 1,456,457 | 12.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 1,154,659 | 79.3% |
| metaclass attribute | 101,995 | 7.0% |
| method | 60,692 | 4.2% |
| not managed dict | 59,470 | 4.1% |
| shadowed | 40,589 | 2.8% |
| non object slot | 7,724 | 0.5% |
| class method obj | 7,260 | 0.5% |
| class attr descriptor | 6,280 | 0.4% |
| overridden | 5,220 | 0.4% |
| non overriding descriptor | 4,484 | 0.3% |
| mutable class | 2,860 | 0.2% |
| not in keys | 1,740 | 0.1% |
| class attr simple | 1,684 | 0.1% |
| module attr not found | 1,340 | 0.1% |
| builtin class method | 440 | 0.0% |
| property | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    145416780 | 4.3% |
| specialization.deopt |        26192 | 0.0% |
|          hit |   3202496458 | 95.6% |
|         miss |      1389355 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 30,122 | 21.0% |
| Failure | 113,254 | 79.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 50,981 | 45.0% |
| different types | 23,801 | 21.0% |
| baseobject | 13,278 | 11.7% |
| float long | 9,282 | 8.2% |
| set | 6,620 | 5.8% |
| other | 3,000 | 2.6% |
| bool | 2,352 | 2.1% |
| tuple | 1,680 | 1.5% |
| list | 1,020 | 0.9% |
| bytes | 800 | 0.7% |
| long float | 300 | 0.3% |
| string | 140 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322350 | 0.1% |
| specialization.deopt |          431 | 0.0% |
|          hit |   6996100720 | 99.9% |
|         miss |        25459 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 55,649 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    839540705 | 15.6% |
| specialization.deopt |       712840 | 0.0% |
|          hit |   4514119181 | 83.7% |
|         miss |     37782963 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,849 | 39.2% |
| Failure | 1,110,404 | 60.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,020 | 52.1% |
| multiply different types | 171,552 | 15.4% |
| add different types | 151,880 | 13.7% |
| floor divide | 32,760 | 3.0% |
| and int | 32,120 | 2.9% |
| remainder | 32,025 | 2.9% |
| add other | 27,100 | 2.4% |
| lshift | 18,760 | 1.7% |
| rshift | 16,633 | 1.5% |
| true divide different types | 14,863 | 1.3% |
| xor | 10,420 | 0.9% |
| true divide float | 6,779 | 0.6% |
| subtract other | 5,520 | 0.5% |
| or | 4,090 | 0.4% |
| power | 3,701 | 0.3% |
| true divide other | 1,201 | 0.1% |
| multiply other | 1,060 | 0.1% |
| and other | 860 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112701169 | 27.2% |
|          hit |    302363053 | 72.8% |
|         miss |          180 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 603 | 2.0% |
| Failure | 28,884 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 84.6% |
| other | 4,364 | 15.1% |
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
|          hit |    116666638 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,580 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    893880146 | 10.1% |
| specialization.deopt |      2750822 | 0.0% |
|          hit |   7775037705 | 88.2% |
|         miss |    145916135 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,798,533 | 87.7% |
| Failure | 394,024 | 12.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 66,333 | 16.8% |
| kwnames | 56,140 | 14.2% |
| code complex parameters | 54,190 | 13.8% |
| no dict | 51,380 | 13.0% |
| class no vectorcall | 29,440 | 7.5% |
| cfunc varargs keywords | 24,879 | 6.3% |
| cfunc noargs | 22,492 | 5.7% |
| meth descr varargs | 22,438 | 5.7% |
| other | 11,458 | 2.9% |
| init not python | 10,420 | 2.6% |
| class mutable | 8,742 | 2.2% |
| init not simple | 8,420 | 2.1% |
| meth descr varargs keywords | 7,329 | 1.9% |
| wrong number arguments | 4,460 | 1.1% |
| cmethod | 3,600 | 0.9% |
| bound method | 3,366 | 0.9% |
| cfunc varargs | 3,091 | 0.8% |
| method wrapper | 2,480 | 0.6% |
| operator wrapper | 2,366 | 0.6% |
| str | 1,000 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 94,039,413,353 | 63.5% |
| Not specialized | 10,977,965,552 | 7.4% |
| Specialized | 42,968,112,799 | 29.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,350,979,393 | 37.4% |
| LOAD_ATTR | 1,070,521,508 | 17.0% |
| CALL | 893,880,146 | 14.2% |
| BINARY_OP | 839,540,705 | 13.4% |
| STORE_SUBSCR | 316,114,000 | 5.0% |
| FOR_ITER | 293,052,445 | 4.7% |
| TO_BOOL | 204,565,074 | 3.3% |
| COMPARE_OP | 145,416,780 | 2.3% |
| SEND | 112,701,169 | 1.8% |
| STORE_ATTR | 53,482,809 | 0.9% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 207,834,823 | 18.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 154,163,573 | 13.8% |
| STORE_ATTR_SLOT | 112,732,738 | 10.1% |
| CALL_PY_EXACT_ARGS | 86,811,241 | 7.8% |
| STORE_ATTR_INSTANCE_VALUE | 69,162,141 | 6.2% |
| FOR_ITER_LIST | 65,829,476 | 5.9% |
| FOR_ITER_TUPLE | 65,581,838 | 5.9% |
| LOAD_ATTR_SLOT | 57,457,803 | 5.2% |
| LOAD_ATTR_METHOD_NO_DICT | 45,686,665 | 4.1% |
| TO_BOOL_NONE | 41,154,702 | 3.7% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,218,597,244 | 23.4% |
| Calls to Python functions inlined | 3,997,222,933 | 76.6% |
| Calls via PyEval_EvalFrame (total) | 1,218,597,244 | 23.4% |
| Calls via PyEval_EvalFrame (vector) | 678,877,239 | 13.0% |
| Calls via PyEval_EvalFrame (generator) | 539,720,005 | 10.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 678,872,139 | 13.0% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 191,532,805 | 3.7% |
| Calls via PyEval_EvalFrame (function ex) | 13,951,673 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 115,827,378 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 94,979,238 | 1.8% |
| Frames pushed | 4,350,620,150 | 83.4% |
| Frame objects created | 59,291,081 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,171,583,134 | 35.4% |
| Frees to freelist | 4,171,718,133 |  |
| Allocations | 7,615,753,603 | 64.6% |
| Allocations to 512 bytes | 7,534,020,528 | 63.9% |
| Allocations to 4 kbytes | 66,549,925 | 0.6% |
| Allocations over 4 kbytes | 15,183,150 | 0.1% |
| Frees | 7,755,259,812 |  |
| New values | 57,541,697 |  |
| Interpreter increfs | 56,220,409,583 | 76.5% |
| Interpreter decrefs | 65,254,941,362 | 77.3% |
| Increfs | 17,239,518,905 | 23.5% |
| Decrefs | 19,205,621,231 | 22.7% |
| Materialize dict (on request) | 3,685,800 | 6.4% |
| Materialize dict (new key) | 58,140 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,872,432,259 |  |
| Method cache misses | 67,150,468 |  |
| Method cache collisions | 70,984,544 |  |
| Method cache dunder hits | 2,212,274,312 |  |
| Method cache dunder misses | 3,874,272 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects queued | Objects collected | Object visits | 
|---:|---:|---:|---:|---:|
| 0 | 138,041 | 402,045,513 | 49,058,769 | 3,640,465,440 |
| 1 | 138,041 | 321,119,706 | 15,225,547 | 3,247,231,150 |
| 2 | 11,520 | 0 | 8,064,000 | 5,268,449,440 |
| 3 | 0 | 0 | 0 | 0 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,278 |


</details>

---
Stats gathered on: 2023-08-22
