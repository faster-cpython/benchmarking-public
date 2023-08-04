
# Pystats results

- fork: faster-cpython
- ref: gc-scan-roots
- commit hash: 3994224
- commit date: 2023-08-04T12:00:47+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 27,779,066,244 | 18.7% | 18.7% |  |
| STORE_FAST | 9,837,506,705 | 6.6% | 25.3% |  |
| LOAD_CONST | 9,593,222,310 | 6.5% | 31.8% |  |
| POP_JUMP_IF_FALSE | 8,437,408,280 | 5.7% | 37.4% |  |
| LOAD_FAST_LOAD_FAST | 8,167,173,090 | 5.5% | 42.9% |  |
| RESUME | 4,989,306,711 | 3.4% | 46.3% |  |
| LOAD_GLOBAL_BUILTIN | 4,135,824,554 | 2.8% | 49.1% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,793,919,006 | 2.6% | 51.6% | 6.1% |
| TO_BOOL_BOOL | 3,237,223,368 | 2.2% | 53.8% | 0.0% |
| JUMP_BACKWARD | 3,212,829,736 | 2.2% | 56.0% |  |
| RETURN_VALUE | 3,011,528,943 | 2.0% | 58.0% |  |
| LOAD_GLOBAL_MODULE | 2,891,024,058 | 1.9% | 59.9% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,835,826,619 | 1.9% | 61.8% | 3.2% |
| POP_TOP | 2,358,843,909 | 1.6% | 63.4% |  |
| BINARY_SUBSCR | 2,351,572,945 | 1.6% | 65.0% |  |
| BINARY_OP_ADD_INT | 2,226,181,771 | 1.5% | 66.5% | 0.0% |
| CONTAINS_OP | 1,983,045,576 | 1.3% | 67.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,860,167,184 | 1.3% | 69.1% | 9.1% |
| COMPARE_OP_STR | 1,590,668,332 | 1.1% | 70.2% | 0.0% |
| STORE_FAST_STORE_FAST | 1,542,757,263 | 1.0% | 71.2% |  |
| COMPARE_OP_INT | 1,507,520,790 | 1.0% | 72.2% | 0.1% |
| NOP | 1,497,420,459 | 1.0% | 73.2% |  |
| POP_JUMP_IF_TRUE | 1,467,389,973 | 1.0% | 74.2% |  |
| LOAD_ATTR_SLOT | 1,345,012,322 | 0.9% | 75.1% | 4.3% |
| RETURN_CONST | 1,344,201,402 | 0.9% | 76.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,335,706,921 | 0.9% | 76.9% | 3.4% |
| FOR_ITER_LIST | 1,239,661,653 | 0.8% | 77.7% | 5.3% |
| INTERPRETER_EXIT | 1,210,104,490 | 0.8% | 78.6% |  |
| COPY | 1,078,787,996 | 0.7% | 79.3% |  |
| LOAD_ATTR | 1,072,305,283 | 0.7% | 80.0% |  |
| STORE_ATTR_SLOT | 1,062,919,380 | 0.7% | 80.7% | 10.6% |
| SWAP | 934,727,521 | 0.6% | 81.3% |  |
| CALL_NO_KW_BUILTIN_FAST | 933,468,766 | 0.6% | 82.0% | 0.0% |
| CALL | 894,469,605 | 0.6% | 82.6% |  |
| BINARY_SUBSCR_LIST_INT | 880,835,888 | 0.6% | 83.2% | 0.4% |
| LOAD_DEREF | 844,285,874 | 0.6% | 83.7% |  |
| BINARY_OP | 842,347,216 | 0.6% | 84.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 834,762,435 | 0.6% | 84.9% | 9.0% |
| BINARY_OP_MULTIPLY_FLOAT | 827,760,442 | 0.6% | 85.4% | 0.8% |
| CALL_NO_KW_ISINSTANCE | 814,199,148 | 0.5% | 86.0% |  |
| PUSH_NULL | 786,701,324 | 0.5% | 86.5% |  |
| CALL_NO_KW_BUILTIN_O | 785,536,634 | 0.5% | 87.0% | 0.1% |
| YIELD_VALUE | 693,473,776 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 692,931,463 | 0.5% | 88.0% |  |
| BINARY_SUBSCR_DICT | 622,336,347 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 605,548,174 | 0.4% | 88.8% |  |
| GET_ITER | 594,214,210 | 0.4% | 89.2% |  |
| BINARY_OP_SUBTRACT_INT | 500,871,892 | 0.3% | 89.5% | 0.1% |
| FOR_ITER_RANGE | 482,698,503 | 0.3% | 89.8% | 0.0% |
| IS_OP | 444,311,067 | 0.3% | 90.1% |  |
| POP_JUMP_IF_NOT_NONE | 431,349,643 | 0.3% | 90.4% |  |
| UNPACK_SEQUENCE_TUPLE | 425,326,361 | 0.3% | 90.7% | 0.3% |
| JUMP_FORWARD | 423,260,290 | 0.3% | 91.0% |  |
| FOR_ITER_TUPLE | 422,585,207 | 0.3% | 91.3% | 15.5% |
| BINARY_OP_ADD_FLOAT | 391,150,183 | 0.3% | 91.6% | 1.6% |
| TO_BOOL_NONE | 376,302,768 | 0.3% | 91.8% | 10.9% |
| LOAD_ATTR_WITH_HINT | 354,377,836 | 0.2% | 92.0% | 2.5% |
| CALL_NO_KW_LEN | 345,739,528 | 0.2% | 92.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 340,457,906 | 0.2% | 92.5% | 2.0% |
| LOAD_ATTR_MODULE | 339,735,066 | 0.2% | 92.7% | 0.0% |
| CALL_NO_KW_TYPE_1 | 335,994,286 | 0.2% | 93.0% |  |
| STORE_SUBSCR | 316,199,659 | 0.2% | 93.2% |  |
| EXTENDED_ARG | 308,251,812 | 0.2% | 93.4% |  |
| SEND_GEN | 302,363,210 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR_LIST_INT | 302,192,312 | 0.2% | 93.8% | 0.0% |
| BUILD_LIST | 301,099,456 | 0.2% | 94.0% |  |
| POP_JUMP_IF_NONE | 298,698,224 | 0.2% | 94.2% |  |
| FOR_ITER | 293,180,556 | 0.2% | 94.4% |  |
| BINARY_OP_SUBTRACT_FLOAT | 270,382,924 | 0.2% | 94.6% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 266,391,249 | 0.2% | 94.8% | 3.2% |
| COPY_FREE_VARS | 253,300,604 | 0.2% | 94.9% |  |
| BINARY_SLICE | 248,170,566 | 0.2% | 95.1% |  |
| CALL_NO_KW_LIST_APPEND | 239,607,195 | 0.2% | 95.2% | 0.0% |
| RETURN_GENERATOR | 238,823,831 | 0.2% | 95.4% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 233,391,070 | 0.2% | 95.6% | 6.9% |
| TO_BOOL_INT | 228,373,348 | 0.2% | 95.7% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 228,038,603 | 0.2% | 95.9% | 0.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,746,851 | 0.1% | 96.0% |  |
| TO_BOOL | 204,965,355 | 0.1% | 96.2% |  |
| STORE_SUBSCR_DICT | 198,971,145 | 0.1% | 96.3% |  |
| END_SEND | 194,307,541 | 0.1% | 96.4% |  |
| BINARY_SUBSCR_TUPLE_INT | 188,459,658 | 0.1% | 96.5% | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 178,900,376 | 0.1% | 96.7% | 21.3% |
| KW_NAMES | 172,957,050 | 0.1% | 96.8% |  |
| CALL_PY_WITH_DEFAULTS | 171,283,997 | 0.1% | 96.9% | 3.1% |
| BUILD_SLICE | 158,211,395 | 0.1% | 97.0% |  |
| CALL_INTRINSIC_1 | 154,034,154 | 0.1% | 97.1% |  |
| LIST_APPEND | 146,919,590 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,424,398 | 0.1% | 97.3% | 0.0% |
| COMPARE_OP | 145,537,884 | 0.1% | 97.4% |  |
| UNPACK_SEQUENCE_LIST | 140,234,020 | 0.1% | 97.5% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,653,800 | 0.1% | 97.6% | 19.1% |
| STORE_FAST_LOAD_FAST | 133,486,517 | 0.1% | 97.7% |  |
| DELETE_SUBSCR | 127,970,479 | 0.1% | 97.8% |  |
| CALL_BUILTIN_CLASS | 126,629,678 | 0.1% | 97.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 124,439,915 | 0.1% | 97.9% | 32.6% |
| UNARY_NEGATIVE | 121,275,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 121,008,339 | 0.1% | 98.1% | 1.1% |
| LOAD_SUPER_ATTR_METHOD | 118,361,814 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,671,352 | 0.1% | 98.3% |  |
| FORMAT_SIMPLE | 117,345,214 | 0.1% | 98.3% |  |
| SEND | 112,730,357 | 0.1% | 98.4% |  |
| TO_BOOL_LIST | 111,951,552 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 111,063,229 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,739,102 | 0.1% | 98.6% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 94,839,290 | 0.1% | 98.8% |  |
| MAKE_CELL | 92,652,021 | 0.1% | 98.8% |  |
| FOR_ITER_GEN | 90,214,926 | 0.1% | 98.9% | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 87,702,692 | 0.1% | 98.9% | 2.0% |
| GET_AWAITABLE | 85,009,883 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 83,745,401 | 0.1% | 99.1% |  |
| CALL_FUNCTION_EX | 83,029,688 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,377,237 | 0.1% | 99.2% | 0.0% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,837,245 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 68,048,025 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 67,240,998 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 67,125,785 | 0.0% | 99.4% |  |
| STORE_DEREF | 65,760,139 | 0.0% | 99.4% |  |
| BUILD_MAP | 63,934,760 | 0.0% | 99.4% |  |
| BUILD_STRING | 59,066,154 | 0.0% | 99.5% |  |
| UNARY_NOT | 58,461,261 | 0.0% | 99.5% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 56,934,640 | 0.0% | 99.6% | 0.0% |
| END_FOR | 56,701,025 | 0.0% | 99.6% |  |
| LIST_EXTEND | 54,338,060 | 0.0% | 99.6% |  |
| STORE_ATTR_WITH_HINT | 54,053,479 | 0.0% | 99.7% | 5.8% |
| STORE_ATTR | 53,543,116 | 0.0% | 99.7% |  |
| LOAD_FAST_AND_CLEAR | 52,326,033 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 48,589,852 | 0.0% | 99.8% | 11.3% |
| MAP_ADD | 41,400,808 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,648,269 | 0.0% | 99.8% |  |
| CALL_NO_KW_TUPLE_1 | 22,405,308 | 0.0% | 99.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 22,351,920 | 0.0% | 99.9% | 0.0% |
| PUSH_EXC_INFO | 17,043,852 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,043,847 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,576,281 | 0.0% | 99.9% |  |
| DICT_MERGE | 16,231,552 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,170,582 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,462,890 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,524,212 | 0.0% | 100.0% |  |
| RERAISE | 8,497,614 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,376,769 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,306,297 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,700 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,924,442 | 0.0% | 100.0% |  |
| BEFORE_WITH | 5,252,336 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 4,632,658 | 0.0% | 100.0% |  |
| SET_ADD | 3,234,120 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 2,897,243 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,298,840 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,989,900 | 0.0% | 100.0% |  |
| BUILD_SET | 1,918,507 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,671,480 | 0.0% | 100.0% |  |
| DELETE_FAST | 622,710 | 0.0% | 100.0% |  |
| UNPACK_EX | 286,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 216,638 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 138,123 | 0.0% | 100.0% |  |
| SET_UPDATE | 66,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 51,372 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,987 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,427 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,407 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,220 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,540 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 792 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 5,017,094,087 | 3.4% | 3.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,443,349,771 | 3.0% | 6.4% |
| STORE_FAST LOAD_FAST | 4,424,547,769 | 3.0% | 9.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,221,502,051 | 2.2% | 11.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,666,329,357 | 1.8% | 13.3% |
| CALL_PY_EXACT_ARGS RESUME | 2,521,816,262 | 1.7% | 15.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,359,044,505 | 1.6% | 16.6% |
| RESUME LOAD_FAST | 2,087,436,893 | 1.4% | 18.0% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,870,240,520 | 1.3% | 19.2% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,774,699,448 | 1.2% | 20.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,595,167,152 | 1.1% | 21.5% |
| LOAD_CONST COMPARE_OP_STR | 1,563,963,920 | 1.1% | 22.6% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,550,235,069 | 1.0% | 23.6% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 1,436,494,402 | 1.0% | 24.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,332,352,082 | 0.9% | 25.5% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,270,866,165 | 0.9% | 26.3% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,763,458 | 0.8% | 27.2% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,229,227,381 | 0.8% | 28.0% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,183,236,419 | 0.8% | 28.8% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,097,579,924 | 0.7% | 29.5% |
| LOAD_CONST LOAD_FAST | 1,062,052,958 | 0.7% | 30.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,061,541,514 | 0.7% | 31.0% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,415,720 | 0.7% | 31.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 980,817,812 | 0.7% | 32.3% |
| BINARY_SUBSCR STORE_FAST | 977,845,482 | 0.7% | 32.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 972,355,579 | 0.7% | 33.6% |
| NOP LOAD_FAST_LOAD_FAST | 959,961,356 | 0.6% | 34.2% |
| LOAD_FAST LOAD_FAST | 939,308,318 | 0.6% | 34.9% |
| JUMP_BACKWARD FOR_ITER_LIST | 924,212,373 | 0.6% | 35.5% |
| STORE_FAST JUMP_BACKWARD | 918,432,425 | 0.6% | 36.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 904,990,344 | 0.6% | 36.7% |
| BINARY_SUBSCR LOAD_FAST | 879,036,848 | 0.6% | 37.3% |
| POP_TOP LOAD_FAST | 851,162,133 | 0.6% | 37.9% |
| RESUME LOAD_GLOBAL_BUILTIN | 844,809,895 | 0.6% | 38.5% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,163,842 | 0.5% | 39.0% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 801,059,204 | 0.5% | 39.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 798,057,985 | 0.5% | 40.1% |
| LOAD_FAST RETURN_VALUE | 781,930,623 | 0.5% | 40.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 768,728,565 | 0.5% | 41.1% |
| LOAD_CONST LOAD_CONST | 744,407,188 | 0.5% | 41.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 738,458,244 | 0.5% | 42.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 735,435,202 | 0.5% | 42.6% |
| JUMP_BACKWARD NOP | 718,029,658 | 0.5% | 43.1% |
| LOAD_FAST TO_BOOL_BOOL | 715,260,391 | 0.5% | 43.6% |
| STORE_FAST STORE_FAST | 711,196,126 | 0.5% | 44.1% |
| LOAD_CONST COMPARE_OP_INT | 672,715,841 | 0.5% | 44.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 665,056,886 | 0.4% | 45.0% |
| POP_TOP JUMP_BACKWARD | 657,977,823 | 0.4% | 45.4% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 644,133,011 | 0.4% | 45.8% |
| RETURN_VALUE STORE_FAST | 624,265,104 | 0.4% | 46.3% |
| LOAD_FAST LOAD_ATTR | 592,743,777 | 0.4% | 46.7% |
| FOR_ITER_LIST STORE_FAST | 587,187,520 | 0.4% | 47.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 573,783,207 | 0.4% | 47.4% |
| RETURN_CONST POP_TOP | 573,634,975 | 0.4% | 47.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 540,592,628 | 0.4% | 48.2% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 539,786,848 | 0.4% | 48.5% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,153,020 | 0.4% | 48.9% |
| LOAD_DEREF LOAD_FAST | 535,034,536 | 0.4% | 49.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 519,356,889 | 0.3% | 49.6% |
| RETURN_VALUE RETURN_VALUE | 518,784,875 | 0.3% | 50.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 515,578,570 | 0.3% | 50.3% |
| LOAD_FAST CONTAINS_OP | 510,851,662 | 0.3% | 50.7% |
| LOAD_FAST STORE_ATTR_SLOT | 504,065,079 | 0.3% | 51.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 480,013,131 | 0.3% | 51.3% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,713,140 | 0.3% | 51.6% |
| RESUME POP_TOP | 472,273,965 | 0.3% | 52.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 465,340,438 | 0.3% | 52.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 459,649,224 | 0.3% | 52.6% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 458,552,062 | 0.3% | 52.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 452,913,816 | 0.3% | 53.2% |
| YIELD_VALUE INTERPRETER_EXIT | 451,458,842 | 0.3% | 53.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 449,995,088 | 0.3% | 53.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 446,658,315 | 0.3% | 54.1% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 444,398,875 | 0.3% | 54.4% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.7% |
| PUSH_NULL LOAD_FAST | 433,935,019 | 0.3% | 55.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 433,474,985 | 0.3% | 55.3% |
| JUMP_BACKWARD FOR_ITER_RANGE | 428,698,614 | 0.3% | 55.6% |
| LOAD_CONST STORE_FAST | 422,817,526 | 0.3% | 55.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 421,883,964 | 0.3% | 56.1% |
| BUILD_TUPLE RETURN_VALUE | 413,113,306 | 0.3% | 56.4% |
| RETURN_CONST INTERPRETER_EXIT | 410,748,122 | 0.3% | 56.7% |
| FOR_ITER_RANGE STORE_FAST | 397,287,848 | 0.3% | 57.0% |
| IS_OP POP_JUMP_IF_FALSE | 375,967,109 | 0.3% | 57.2% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 375,884,523 | 0.3% | 57.5% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 368,147,865 | 0.2% | 57.7% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 366,745,317 | 0.2% | 58.0% |
| NOP LOAD_FAST | 358,684,317 | 0.2% | 58.2% |
| LOAD_FAST BINARY_SUBSCR | 357,874,763 | 0.2% | 58.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 355,170,539 | 0.2% | 58.7% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 346,525,380 | 0.2% | 58.9% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,716,573 | 0.2% | 59.1% |
| STORE_FAST LOAD_DEREF | 341,240,442 | 0.2% | 59.4% |
| RESUME LOAD_GLOBAL_MODULE | 339,273,617 | 0.2% | 59.6% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 339,157,867 | 0.2% | 59.8% |
| RESUME NOP | 337,463,102 | 0.2% | 60.1% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 332,978,444 | 0.2% | 60.3% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 332,292,744 | 0.2% | 60.5% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 331,892,473 | 0.2% | 60.7% |
| RETURN_VALUE INTERPRETER_EXIT | 329,721,066 | 0.2% | 60.9% |


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
| RETURN_VALUE | 2,428,929 | 46.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,273,446 | 43.3% |
| LOAD_GLOBAL_MODULE | 210,141 | 4.0% |
| LOAD_ATTR_WITH_HINT | 132,620 | 2.5% |
| LOAD_FAST | 132,060 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,628,727 | 88.1% |
| STORE_FAST | 622,169 | 11.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 249,142,380 | 29.6% |
| LOAD_FAST | 170,130,584 | 20.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.5% |
| LOAD_FAST_LOAD_FAST | 47,866,507 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,907 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 153,778,736 | 18.3% |
| LOAD_FAST | 134,704,677 | 16.0% |
| LOAD_FAST_LOAD_FAST | 106,872,583 | 12.7% |
| LOAD_CONST | 91,364,831 | 10.8% |
| RETURN_VALUE | 69,617,582 | 8.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,109,360 | 72.6% |
| LOAD_FAST | 65,394,989 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,256,824 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,612,524 | 29.8% |
| STORE_FAST | 116,105,635 | 29.7% |
| LOAD_FAST | 59,770,704 | 15.3% |
| RETURN_VALUE | 31,351,200 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,774,699,448 | 79.7% |
| LOAD_FAST | 244,323,015 | 11.0% |
| LOAD_FAST_LOAD_FAST | 94,838,268 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,763,458 | 56.5% |
| LOAD_CONST | 132,769,476 | 6.0% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,091,992 | 4.3% |
| SWAP | 90,613,231 | 4.1% |


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
| LOAD_FAST | 16,173,541 | 23.8% |
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
| LOAD_FAST | 3,731,941 | 63.0% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,840 | 8.6% |
| LOAD_CONST | 60,360 | 1.0% |
| LOAD_FAST_LOAD_FAST | 24,301 | 0.4% |


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
| BINARY_OP_ADD_INT | 96,091,992 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,999 | 19.2% |
| LOAD_FAST_LOAD_FAST | 44,913,199 | 16.9% |
| LOAD_FAST | 38,771,060 | 14.6% |
| BINARY_OP | 27,332,907 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,212,232 | 23.4% |
| LOAD_CONST | 61,633,100 | 23.1% |
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
| LOAD_FAST | 69,610,868 | 25.7% |
| LOAD_FAST_LOAD_FAST | 36,420,278 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 28,678,206 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,605,549 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.1% |
| SWAP | 55,832,924 | 20.6% |
| LOAD_FAST | 28,365,842 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 366,745,317 | 73.2% |
| LOAD_FAST | 78,850,673 | 15.7% |
| LOAD_FAST_LOAD_FAST | 30,056,046 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 21,634,306 | 4.3% |
| CALL_NO_KW_LEN | 2,724,600 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,030,206 | 19.2% |
| CALL_PY_EXACT_ARGS | 94,404,100 | 18.8% |
| SWAP | 69,253,513 | 13.8% |
| RETURN_VALUE | 40,191,098 | 8.0% |
| BINARY_OP | 37,297,299 | 7.4% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 137,122,839 | 55.3% |
| BINARY_OP_ADD_INT | 40,077,520 | 16.1% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.1% |
| LOAD_FAST | 24,931,487 | 10.0% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 57,269,089 | 23.1% |
| GET_ITER | 33,199,240 | 13.4% |
| CALL_PY_EXACT_ARGS | 25,430,496 | 10.2% |
| BUILD_TUPLE | 24,334,502 | 9.8% |
| LOAD_DEREF | 18,985,680 | 7.7% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,436,494,402 | 61.1% |
| LOAD_FAST | 357,874,763 | 15.2% |
| LOAD_CONST | 139,739,619 | 5.9% |
| COPY | 109,830,440 | 4.7% |
| BUILD_SLICE | 104,833,980 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 977,845,482 | 41.6% |
| LOAD_FAST | 879,036,848 | 37.4% |
| LOAD_FAST_LOAD_FAST | 110,207,520 | 4.7% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |
| BINARY_SUBSCR | 48,587,981 | 2.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,822,200 | 33.2% |
| LOAD_FAST | 205,313,713 | 33.0% |
| LOAD_FAST_LOAD_FAST | 135,440,518 | 21.8% |
| BINARY_SUBSCR | 41,253,853 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,009,448 | 38.1% |
| RETURN_VALUE | 104,203,354 | 16.7% |
| CONTAINS_OP | 77,768,700 | 12.5% |
| LOAD_FAST | 60,027,798 | 9.6% |
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
| LOAD_FAST | 3,529,618 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,060 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,516,138 | 99.4% |
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
| LOAD_FAST | 273,182,684 | 31.0% |
| LOAD_CONST | 180,971,985 | 20.5% |
| COPY | 157,633,500 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,824,054 | 17.6% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,340,632 | 26.8% |
| LOAD_CONST | 192,236,280 | 21.9% |
| LOAD_FAST | 141,519,064 | 16.1% |
| RETURN_VALUE | 90,406,908 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 148,324,058 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.1% |
| LOAD_FAST_LOAD_FAST | 329,628 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 2,529 | 0.0% |
| BINARY_SUBSCR | 343 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,900 | 38.3% |
| LOAD_CONST | 24,654,420 | 13.1% |
| LOAD_FAST | 24,246,832 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.3% |
| STORE_FAST | 8,763,755 | 4.7% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,632,658 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,034,612 | 43.9% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 36.8% |
| STORE_FAST | 383,091 | 8.3% |
| RETURN_VALUE | 144,407 | 3.1% |
| CALL_NO_KW_LIST_APPEND | 132,780 | 2.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,262,466 | 38.6% |
| LOAD_ATTR_SLOT | 38,396,136 | 12.8% |
| SWAP | 32,353,460 | 10.7% |
| LOAD_FAST | 26,266,186 | 8.7% |
| RESUME | 18,138,532 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 129,102,129 | 42.9% |
| LOAD_FAST | 89,938,085 | 29.9% |
| SWAP | 32,389,352 | 10.8% |
| CALL | 9,652,840 | 3.2% |
| RETURN_VALUE | 9,311,715 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,290,238 | 16.1% |
| RESUME | 6,821,345 | 10.7% |
| LOAD_FAST | 6,700,275 | 10.5% |
| CALL_INTRINSIC_1 | 6,520,609 | 10.2% |
| SWAP | 6,077,760 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,056,542 | 37.6% |
| LOAD_FAST | 23,243,917 | 36.4% |
| SWAP | 6,077,760 | 9.5% |
| CALL_FUNCTION_EX | 3,407,654 | 5.3% |
| LOAD_CONST | 2,982,596 | 4.7% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| LOAD_CONST | 142,320 | 7.4% |
| LOAD_GLOBAL_MODULE | 142,207 | 7.4% |
| LOAD_ATTR | 66,000 | 3.4% |
| LOAD_FAST | 52,920 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| CONTAINS_OP | 141,847 | 7.4% |
| LOAD_CONST | 74,280 | 3.9% |
| BINARY_OP | 68,400 | 3.6% |
| STORE_FAST | 48,240 | 2.5% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,375,104 | 99.5% |
| LOAD_FAST | 780,851 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,980 | 66.3% |
| DELETE_SUBSCR | 53,377,415 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 52,318,600 | 88.6% |
| LOAD_CONST | 6,747,554 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.1% |
| CALL | 12,296,988 | 20.8% |
| STORE_FAST | 4,749,962 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,950,474 | 29.9% |
| LOAD_CONST | 167,604,087 | 24.2% |
| LOAD_FAST_LOAD_FAST | 126,885,016 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 40,166,586 | 5.8% |
| CALL | 38,800,658 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 413,113,306 | 59.6% |
| LOAD_CONST | 82,949,297 | 12.0% |
| CALL_NO_KW_ISINSTANCE | 40,155,257 | 5.8% |
| STORE_FAST | 30,270,204 | 4.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 256,841,083 | 28.7% |
| KW_NAMES | 149,665,372 | 16.7% |
| LOAD_FAST_LOAD_FAST | 99,270,993 | 11.1% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,900 | 8.1% |
| LOAD_GLOBAL_MODULE | 49,105,912 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 305,180,169 | 34.1% |
| RESUME | 211,845,403 | 23.7% |
| RETURN_VALUE | 51,180,676 | 5.7% |
| POP_TOP | 47,330,432 | 5.3% |
| LOAD_GLOBAL_MODULE | 39,308,027 | 4.4% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,870,819 | 30.9% |
| LOAD_CONST | 23,537,060 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.2% |
| LOAD_FAST_LOAD_FAST | 21,626,356 | 15.6% |
| LOAD_ATTR_INSTANCE_VALUE | 6,372,281 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,993,889 | 78.6% |
| COPY_FREE_VARS | 26,910,062 | 19.4% |
| POP_TOP | 2,068,100 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,538 | 0.3% |
| MAKE_CELL | 172,407 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,477,816 | 28.8% |
| CALL_NO_KW_LEN | 23,254,130 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 10,773,042 | 8.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 9,078,776 | 7.2% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,640,802 | 50.3% |
| STORE_FAST | 13,560,273 | 10.7% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.1% |
| LOAD_FAST | 10,268,977 | 8.1% |
| CALL_BUILTIN_CLASS | 4,235,830 | 3.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,880 | 43.2% |
| KW_NAMES | 22,239,878 | 29.1% |
| LOAD_FAST | 13,403,952 | 17.5% |
| LOAD_FAST_LOAD_FAST | 2,766,388 | 3.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,137,420 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,880 | 41.0% |
| STORE_FAST | 27,917,688 | 36.6% |
| POP_TOP | 8,839,629 | 11.6% |
| RETURN_VALUE | 5,704,143 | 7.5% |
| BINARY_OP_ADD_INT | 931,385 | 1.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,151,647 | 52.0% |
| DICT_MERGE | 16,231,552 | 19.5% |
| LOAD_FAST | 10,562,463 | 12.7% |
| LOAD_FAST_LOAD_FAST | 5,883,400 | 7.1% |
| BUILD_MAP | 3,407,654 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,277,150 | 56.9% |
| STORE_FAST | 8,426,979 | 10.1% |
| RESUME | 7,482,487 | 9.0% |
| RETURN_VALUE | 6,926,523 | 8.3% |
| MAKE_CELL | 4,744,312 | 5.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 59.7% |
| LIST_EXTEND | 53,504,770 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.1% |
| RERAISE | 42,144 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 61.1% |
| CALL_FUNCTION_EX | 43,151,647 | 28.0% |
| BUILD_MAP | 6,520,609 | 4.2% |
| RERAISE | 6,381,104 | 4.1% |
| LOAD_CONST | 3,819,374 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,944,166 | 72.9% |
| LOAD_FAST | 10,476,422 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,512,508 | 8.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,177,290 | 4.8% |
| LOAD_FAST_LOAD_FAST | 1,041,742 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 70,523,155 | 80.4% |
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
| LOAD_GLOBAL_MODULE | 9,509,430 | 13.8% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.0% |
| RETURN_CONST | 7,864,740 | 11.4% |
| BINARY_OP_ADD_FLOAT | 5,101,500 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,410,380 | 95.0% |
| COPY_FREE_VARS | 1,715,285 | 2.5% |
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
| LOAD_CONST | 339,157,867 | 36.3% |
| LOAD_FAST_LOAD_FAST | 72,302,392 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,233,120 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,713,140 | 51.2% |
| STORE_FAST | 310,648,492 | 33.3% |
| POP_TOP | 47,791,704 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 22,195,223 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,786,848 | 68.7% |
| LOAD_CONST | 55,891,718 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,646,995 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,716,573 | 43.5% |
| LOAD_CONST | 171,776,466 | 21.9% |
| STORE_FAST | 166,549,949 | 21.2% |
| RETURN_VALUE | 29,452,394 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,260 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 346,525,380 | 42.6% |
| LOAD_GLOBAL_BUILTIN | 331,892,473 | 40.8% |
| LOAD_FAST_LOAD_FAST | 61,752,886 | 7.6% |
| BUILD_TUPLE | 40,155,257 | 4.9% |
| LOAD_ATTR_MODULE | 22,114,580 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 801,059,204 | 98.4% |
| COPY | 6,062,052 | 0.7% |
| RETURN_VALUE | 2,415,426 | 0.3% |
| POP_TOP | 1,996,800 | 0.2% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 214,117,197 | 61.9% |
| LOAD_ATTR_INSTANCE_VALUE | 55,114,917 | 15.9% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 8.5% |
| LOAD_DEREF | 20,449,960 | 5.9% |
| LOAD_ATTR_SLOT | 8,655,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,800,331 | 35.8% |
| LOAD_FAST | 55,702,342 | 16.1% |
| STORE_FAST | 44,229,929 | 12.8% |
| COMPARE_OP_INT | 32,613,567 | 9.4% |
| CALL_BUILTIN_CLASS | 23,254,130 | 6.7% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,300,171 | 72.7% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 18,543,072 | 7.7% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 5,805,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 90,825,182 | 37.9% |
| LOAD_FAST | 72,490,162 | 30.3% |
| EXTENDED_ARG | 27,822,060 | 11.6% |
| RETURN_CONST | 20,554,860 | 8.6% |
| LOAD_CONST | 11,304,024 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,411,538 | 52.4% |
| LOAD_FAST_LOAD_FAST | 56,755,997 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 50,383,451 | 14.8% |
| LOAD_CONST | 27,325,290 | 8.0% |
| LOAD_ATTR_SLOT | 8,567,760 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 249,379,859 | 73.2% |
| LIST_APPEND | 28,917,240 | 8.5% |
| RETURN_VALUE | 11,797,277 | 3.5% |
| LOAD_FAST | 10,857,720 | 3.2% |
| POP_TOP | 9,173,261 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 151,135,258 | 64.8% |
| LOAD_ATTR | 72,898,510 | 31.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,472,864 | 3.2% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 302,622 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 73,504,981 | 31.5% |
| TO_BOOL_BOOL | 60,226,957 | 25.8% |
| GET_ITER | 33,735,960 | 14.5% |
| LOAD_GLOBAL_MODULE | 18,632,700 | 8.0% |
| LOAD_FAST | 12,556,165 | 5.4% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,468,876 | 76.9% |
| CALL | 19,599,012 | 8.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.0% |
| CALL_NO_KW_BUILTIN_FAST | 6,013,960 | 2.6% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 111,506,224 | 48.9% |
| BINARY_OP | 72,002,140 | 31.6% |
| RETURN_VALUE | 23,761,890 | 10.4% |
| STORE_FAST | 6,977,370 | 3.1% |
| LOAD_FAST | 5,874,061 | 2.6% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,382,665 | 91.3% |
| RETURN_VALUE | 1,727,780 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,230,542 | 3.3% |
| LOAD_ATTR | 95,179 | 0.3% |
| CALL_NO_KW_TUPLE_1 | 66,000 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.7% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 28.8% |
| STORE_FAST | 5,604,307 | 14.9% |
| RETURN_VALUE | 3,244,983 | 8.6% |
| BUILD_LIST | 1,966,480 | 5.2% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,919,652 | 66.6% |
| RETURN_GENERATOR | 5,526,160 | 24.7% |
| LOAD_ATTR_SLOT | 1,098,656 | 4.9% |
| CALL | 436,440 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 63.8% |
| BUILD_TUPLE | 2,891,816 | 12.9% |
| YIELD_VALUE | 2,419,200 | 10.8% |
| RETURN_VALUE | 1,003,692 | 4.5% |
| STORE_FAST | 642,060 | 2.9% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 332,292,744 | 98.9% |
| LOAD_CONST | 3,615,840 | 1.1% |
| BINARY_SUBSCR_TUPLE_INT | 66,000 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,418,460 | 85.5% |
| LOAD_GLOBAL_MODULE | 13,779,532 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 12,241,634 | 3.6% |
| CALL_PY_EXACT_ARGS | 8,083,958 | 2.4% |
| LOAD_FAST | 7,606,680 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 972,355,579 | 34.3% |
| LOAD_FAST_LOAD_FAST | 644,133,011 | 22.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 446,658,315 | 15.8% |
| LOAD_GLOBAL_MODULE | 166,093,833 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 111,389,558 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,521,816,262 | 88.9% |
| RETURN_GENERATOR | 140,431,731 | 5.0% |
| COPY_FREE_VARS | 125,500,956 | 4.4% |
| MAKE_CELL | 31,460,831 | 1.1% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,974,916 | 55.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,267,523 | 7.2% |
| LOAD_ATTR_METHOD_NO_DICT | 12,068,800 | 7.0% |
| LOAD_ATTR | 11,205,994 | 6.5% |
| LOAD_CONST | 8,918,107 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 165,108,723 | 96.4% |
| RETURN_GENERATOR | 3,374,277 | 2.0% |
| MAKE_CELL | 1,593,282 | 0.9% |
| COPY_FREE_VARS | 1,100,915 | 0.6% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,417,172 | 93.0% |
| LOAD_GLOBAL_MODULE | 690,024 | 4.2% |
| BUILD_TUPLE | 359,940 | 2.2% |
| LOAD_ATTR_MODULE | 109,113 | 0.7% |
| LOAD_GLOBAL | 27 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,576,281 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 408 | 51.5% |
| CALL_INTRINSIC_1 | 240 | 30.3% |
| JUMP_BACKWARD | 144 | 18.2% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 46,495,579 | 31.9% |
| LOAD_FAST_LOAD_FAST | 32,739,520 | 22.5% |
| LOAD_ATTR | 15,308,312 | 10.5% |
| LOAD_ATTR_SLOT | 13,758,174 | 9.5% |
| LOAD_FAST | 10,889,700 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 78,706,418 | 54.1% |
| POP_JUMP_IF_TRUE | 38,840,662 | 26.7% |
| COPY | 18,630,830 | 12.8% |
| RETURN_VALUE | 7,090,312 | 4.9% |
| EXTENDED_ARG | 1,918,366 | 1.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 66,490,381 | 59.9% |
| BINARY_SUBSCR | 23,382,660 | 21.1% |
| LOAD_CONST | 6,328,676 | 5.7% |
| LOAD_FAST | 6,311,972 | 5.7% |
| LOAD_GLOBAL_MODULE | 3,631,912 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,490,561 | 43.7% |
| POP_JUMP_IF_TRUE | 32,446,020 | 29.2% |
| POP_JUMP_IF_FALSE | 30,125,888 | 27.1% |
| COMPARE_OP | 380 | 0.0% |
| EXTENDED_ARG | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 672,715,841 | 44.6% |
| LOAD_ATTR_INSTANCE_VALUE | 173,864,106 | 11.5% |
| LOAD_FAST | 121,639,270 | 8.1% |
| LOAD_FAST_LOAD_FAST | 120,556,004 | 8.0% |
| COPY | 109,002,712 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,270,866,165 | 84.3% |
| POP_JUMP_IF_TRUE | 122,124,100 | 8.1% |
| RETURN_VALUE | 59,381,586 | 3.9% |
| EXTENDED_ARG | 22,449,448 | 1.5% |
| LOAD_FAST | 15,024,000 | 1.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,563,963,920 | 98.3% |
| LOAD_FAST | 8,980,206 | 0.6% |
| LOAD_GLOBAL_MODULE | 5,067,278 | 0.3% |
| RETURN_VALUE | 4,023,960 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,550,235,069 | 97.5% |
| POP_JUMP_IF_TRUE | 27,393,495 | 1.7% |
| COPY | 6,090,366 | 0.4% |
| RETURN_VALUE | 4,403,502 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,415,720 | 49.9% |
| LOAD_FAST | 510,851,662 | 25.8% |
| LOAD_GLOBAL_MODULE | 301,873,338 | 15.2% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 44,370,386 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,870,240,520 | 94.3% |
| POP_JUMP_IF_TRUE | 60,477,180 | 3.0% |
| RETURN_VALUE | 25,865,640 | 1.3% |
| COPY | 21,273,122 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,368,504 | 48.6% |
| LOAD_FAST_LOAD_FAST | 36,024,720 | 34.7% |
| LOAD_ATTR | 11,580,662 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,739,102 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,856,793 | 24.9% |
| LOAD_FAST | 238,922,031 | 22.1% |
| LOAD_FAST_LOAD_FAST | 120,961,740 | 11.2% |
| SWAP | 112,622,859 | 10.4% |
| LOAD_CONST | 95,330,137 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,856,793 | 24.9% |
| TO_BOOL_BOOL | 234,249,595 | 21.7% |
| BINARY_SUBSCR_LIST_INT | 157,633,500 | 14.6% |
| BINARY_SUBSCR | 109,830,440 | 10.2% |
| COMPARE_OP_INT | 109,002,712 | 10.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 125,500,956 | 76.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,910,062 | 16.3% |
| CALL | 9,063,403 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,715,285 | 1.0% |
| CALL_PY_WITH_DEFAULTS | 1,100,915 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 179,675,094 | 70.9% |
| RETURN_GENERATOR | 73,605,650 | 29.1% |
| MAKE_CELL | 19,860 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,523,972 | 100.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,654,648 | 78.1% |
| NOP | 1,715,420 | 20.1% |
| RETURN_CONST | 151,258 | 1.8% |
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
| STORE_FAST | 223,764 | 35.9% |
| CALL | 155,043 | 24.9% |
| POP_TOP | 77,820 | 12.5% |
| NOP | 55,056 | 8.8% |
| STORE_ATTR_INSTANCE_VALUE | 54,951 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 212,643 | 34.1% |
| RERAISE | 151,224 | 24.3% |
| RETURN_CONST | 109,932 | 17.7% |
| JUMP_FORWARD | 66,240 | 10.6% |
| LOAD_FAST | 57,524 | 9.2% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,193,292 | 57.2% |
| BUILD_SLICE | 53,377,415 | 41.7% |
| LOAD_FAST | 1,016,308 | 0.8% |
| LOAD_CONST | 286,740 | 0.2% |
| LOAD_ATTR_SLOT | 66,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,533,639 | 84.1% |
| LOAD_CONST | 18,169,149 | 14.2% |
| JUMP_BACKWARD | 1,105,140 | 0.9% |
| RETURN_CONST | 540,747 | 0.4% |
| LOAD_FAST_LOAD_FAST | 274,584 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,444,149 | 95.1% |
| RETURN_VALUE | 376,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 218,707 | 1.3% |
| LOAD_DEREF | 112,619 | 0.7% |
| LOAD_GLOBAL_MODULE | 36,852 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,231,552 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 36,852 | 71.7% |
| LOAD_FAST | 13,140 | 25.6% |
| BUILD_MAP | 540 | 1.1% |
| RETURN_VALUE | 480 | 0.9% |
| MAP_ADD | 180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,392 | 72.8% |
| DICT_MERGE | 13,140 | 25.6% |
| STORE_FAST | 540 | 1.1% |
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
| RETURN_CONST | 56,701,025 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,101,421 | 33.7% |
| RETURN_CONST | 789,604 | 1.4% |
| LOAD_CONST | 5,940 | 0.0% |
| NOP | 4,980 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,454,850 | 51.7% |
| RETURN_VALUE | 69,220,966 | 35.6% |
| RETURN_CONST | 24,631,461 | 12.7% |
| JUMP_BACKWARD | 144 | 0.0% |
| SEND_GEN | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,092,379 | 48.9% |
| POP_TOP | 36,245,608 | 18.7% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,940 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 67,125,785 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,125,785 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 88,770,394 | 28.8% |
| LOAD_FAST | 42,655,580 | 13.8% |
| JUMP_BACKWARD | 40,665,662 | 13.2% |
| CALL_NO_KW_LIST_APPEND | 27,822,060 | 9.0% |
| COMPARE_OP_INT | 22,449,448 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 138,159,141 | 44.8% |
| JUMP_BACKWARD | 54,300,459 | 17.6% |
| FOR_ITER_LIST | 38,691,700 | 12.6% |
| POP_JUMP_IF_NONE | 36,519,160 | 11.8% |
| FOR_ITER | 16,516,644 | 5.4% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,739,102 | 88.4% |
| LOAD_FAST | 9,752,310 | 8.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,423,980 | 1.2% |
| RETURN_VALUE | 1,042,740 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,138,082 | 50.4% |
| BUILD_STRING | 52,318,600 | 44.6% |
| LOAD_FAST | 5,879,712 | 5.0% |
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
| JUMP_BACKWARD | 212,791,800 | 72.6% |
| GET_ITER | 53,883,760 | 18.4% |
| EXTENDED_ARG | 16,516,644 | 5.6% |
| SWAP | 6,717,705 | 2.3% |
| LOAD_FAST | 3,174,012 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 151,762,124 | 51.8% |
| STORE_FAST | 76,737,901 | 26.2% |
| LOAD_FAST | 19,227,003 | 6.6% |
| RETURN_CONST | 15,910,174 | 5.4% |
| PUSH_NULL | 7,956,120 | 2.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,713,322 | 62.9% |
| JUMP_BACKWARD | 33,136,681 | 36.7% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,240 | 0.0% |
| SWAP | 1,300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,764,923 | 62.9% |
| RESUME | 33,449,463 | 37.1% |
| RETURN_CONST | 300 | 0.0% |
| STORE_FAST | 240 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 924,212,373 | 74.6% |
| GET_ITER | 190,448,157 | 15.4% |
| LOAD_FAST | 59,098,400 | 4.8% |
| EXTENDED_ARG | 38,691,700 | 3.1% |
| SWAP | 25,968,135 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 587,187,520 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,621,398 | 25.4% |
| RETURN_CONST | 103,913,580 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,513,880 | 6.5% |
| LOAD_FAST | 59,133,979 | 4.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 428,698,614 | 88.8% |
| GET_ITER | 27,376,549 | 5.7% |
| LOAD_FAST | 21,531,300 | 4.5% |
| SWAP | 4,261,440 | 0.9% |
| EXTENDED_ARG | 829,500 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 397,287,848 | 82.3% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.3% |
| RETURN_CONST | 24,277,692 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,444,229 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 292,047,453 | 69.1% |
| GET_ITER | 124,941,798 | 29.6% |
| SWAP | 2,996,680 | 0.7% |
| LOAD_FAST | 1,261,050 | 0.3% |
| FOR_ITER_LIST | 1,236,398 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 290,654,925 | 68.8% |
| LOAD_FAST | 61,886,886 | 14.6% |
| LOAD_FAST_LOAD_FAST | 43,821,240 | 10.4% |
| RETURN_CONST | 12,361,266 | 2.9% |
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
| RETURN_GENERATOR | 78,584,969 | 92.4% |
| LOAD_FAST | 3,323,640 | 3.9% |
| RETURN_VALUE | 2,594,515 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 489,659 | 0.6% |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,009,883 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,778,684 | 36.0% |
| LOAD_ATTR_INSTANCE_VALUE | 78,053,209 | 13.1% |
| CALL_BUILTIN_CLASS | 63,640,802 | 10.7% |
| RETURN_VALUE | 50,004,072 | 8.4% |
| LOAD_ATTR_SLOT | 38,736,000 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 190,448,157 | 32.1% |
| FOR_ITER_TUPLE | 124,941,798 | 21.0% |
| CALL_PY_EXACT_ARGS | 85,106,682 | 14.3% |
| FOR_ITER_GEN | 56,713,322 | 9.5% |
| FOR_ITER | 53,883,760 | 9.1% |


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
| IMPORT_NAME | 1,538,760 | 77.3% |
| STORE_FAST | 451,140 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,989,780 | 100.0% |
| PUSH_EXC_INFO | 120 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,671,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,538,760 | 92.1% |
| STORE_FAST | 132,120 | 7.9% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,347 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,407 | 52.3% |
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
| INSTRUMENTED_POP_JUMP_IF_TRUE | 867 | 11.7% |
| LIST_APPEND | 300 | 4.1% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,347 | 58.7% |
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
| TO_BOOL_BOOL | 5,307 | 53.1% |
| TO_BOOL | 3,060 | 30.6% |
| TO_BOOL_STR | 960 | 9.6% |
| TO_BOOL_NONE | 300 | 3.0% |
| COMPARE_OP_STR | 240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.7% |
| LOAD_GLOBAL | 4,020 | 40.3% |
| INSTRUMENTED_JUMP_BACKWARD | 867 | 8.7% |
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
| YIELD_VALUE | 451,458,842 | 37.3% |
| RETURN_CONST | 410,748,122 | 33.9% |
| RETURN_VALUE | 329,721,066 | 27.2% |
| RETURN_GENERATOR | 18,176,220 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,239,560 | 48.7% |
| LOAD_FAST_LOAD_FAST | 111,730,858 | 25.1% |
| LOAD_GLOBAL_MODULE | 81,531,477 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 15,924,414 | 3.6% |
| LOAD_CONST | 8,668,875 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 375,967,109 | 84.6% |
| POP_JUMP_IF_TRUE | 39,091,972 | 8.8% |
| EXTENDED_ARG | 18,199,680 | 4.1% |
| RETURN_VALUE | 3,377,313 | 0.8% |
| COPY | 3,175,067 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,432,425 | 28.6% |
| POP_TOP | 657,977,823 | 20.5% |
| POP_JUMP_IF_TRUE | 465,340,438 | 14.5% |
| POP_JUMP_IF_FALSE | 444,398,875 | 13.8% |
| LIST_APPEND | 146,811,764 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 924,212,373 | 28.8% |
| NOP | 718,029,658 | 22.3% |
| FOR_ITER_RANGE | 428,698,614 | 13.3% |
| FOR_ITER_TUPLE | 292,047,453 | 9.1% |
| LOAD_FAST | 280,759,099 | 8.7% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,746,851 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,501,279 | 97.1% |
| SEND | 6,245,572 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 174,401,972 | 41.2% |
| POP_JUMP_IF_FALSE | 100,899,226 | 23.8% |
| POP_TOP | 57,661,834 | 13.6% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| EXTENDED_ARG | 14,628,748 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 168,023,918 | 39.7% |
| LOAD_FAST_LOAD_FAST | 82,446,981 | 19.5% |
| LOAD_CONST | 37,404,635 | 8.8% |
| LOAD_GLOBAL_MODULE | 28,035,225 | 6.6% |
| LOAD_GLOBAL_BUILTIN | 25,952,030 | 6.1% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,205,079 | 23.8% |
| LOAD_CONST | 38,153,240 | 22.1% |
| LOAD_FAST_LOAD_FAST | 35,523,950 | 20.5% |
| LOAD_GLOBAL_MODULE | 18,005,396 | 10.4% |
| LOAD_ATTR_INSTANCE_VALUE | 11,379,396 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 149,665,372 | 86.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 22,239,878 | 12.9% |
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
| LOAD_FAST | 18,295,865 | 12.5% |
| RETURN_VALUE | 15,151,772 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,811,764 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |
| CALL | 6 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 38,197,656 | 70.3% |
| LOAD_FAST | 15,440,921 | 28.4% |
| LOAD_CONST | 366,720 | 0.7% |
| RETURN_VALUE | 212,690 | 0.4% |
| LOAD_DEREF | 77,527 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 53,504,770 | 98.5% |
| STORE_FAST | 432,794 | 0.8% |
| LOAD_FAST | 224,036 | 0.4% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 592,743,777 | 55.3% |
| LOAD_GLOBAL_BUILTIN | 221,923,460 | 20.7% |
| LOAD_GLOBAL_MODULE | 95,612,068 | 8.9% |
| LOAD_ATTR_SLOT | 81,100,341 | 7.6% |
| LOAD_FAST_LOAD_FAST | 26,581,461 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 219,350,691 | 20.5% |
| IS_OP | 216,239,560 | 20.2% |
| STORE_FAST | 170,152,712 | 15.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 72,898,510 | 6.8% |
| LOAD_FAST_LOAD_FAST | 60,675,601 | 5.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,574,315 | 96.3% |
| LOAD_GLOBAL_BUILTIN | 1,785,480 | 1.5% |
| LOAD_FAST | 1,408,580 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 543,084 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,810,796 | 49.4% |
| LOAD_FAST | 21,988,406 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,858,688 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,920 | 2.3% |
| TO_BOOL_BOOL | 2,450,640 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,221,502,051 | 84.9% |
| LOAD_FAST_LOAD_FAST | 332,978,444 | 8.8% |
| COPY | 80,659,335 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,838,763 | 1.3% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,061,541,514 | 28.0% |
| TO_BOOL_BOOL | 433,474,985 | 11.4% |
| STORE_FAST | 287,953,887 | 7.6% |
| LOAD_ATTR_METHOD_NO_DICT | 190,060,182 | 5.0% |
| RETURN_VALUE | 181,689,619 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40,723,026 | 71.5% |
| LOAD_FAST | 16,211,172 | 28.5% |
| LOAD_ATTR | 402 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,574,980 | 69.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,472,864 | 13.1% |
| LOAD_GLOBAL_MODULE | 5,902,240 | 10.4% |
| LOAD_CONST | 2,491,800 | 4.4% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 768,728,565 | 57.6% |
| LOAD_ATTR_INSTANCE_VALUE | 190,060,182 | 14.2% |
| LOAD_CONST | 90,385,215 | 6.8% |
| LOAD_GLOBAL_MODULE | 52,878,567 | 4.0% |
| LOAD_ATTR_SLOT | 48,976,840 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 665,056,886 | 49.8% |
| LOAD_CONST | 155,816,869 | 11.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 151,135,258 | 11.3% |
| LOAD_FAST_LOAD_FAST | 111,686,484 | 8.4% |
| CALL_PY_EXACT_ARGS | 111,389,558 | 8.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,595,167,152 | 85.8% |
| LOAD_ATTR_INSTANCE_VALUE | 63,483,231 | 3.4% |
| LOAD_ATTR | 45,749,270 | 2.5% |
| LOAD_ATTR_SLOT | 45,627,318 | 2.5% |
| LOAD_ATTR_WITH_HINT | 37,390,779 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 798,057,985 | 42.9% |
| LOAD_FAST_LOAD_FAST | 480,013,131 | 25.8% |
| CALL_PY_EXACT_ARGS | 446,658,315 | 24.0% |
| LOAD_GLOBAL_MODULE | 56,045,493 | 3.0% |
| LOAD_CONST | 53,011,399 | 2.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 324,225,347 | 95.4% |
| LOAD_ATTR_MODULE | 11,618,950 | 3.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,324,680 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,933,254 | 33.5% |
| LOAD_FAST_LOAD_FAST | 101,058,839 | 29.7% |
| CALL | 27,534,968 | 8.1% |
| CALL_NO_KW_ISINSTANCE | 22,114,580 | 6.5% |
| LOAD_CONST | 15,918,387 | 4.7% |


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
| LOAD_FAST | 111,853,235 | 89.9% |
| LOAD_FAST_LOAD_FAST | 10,763,360 | 8.6% |
| LOAD_ATTR_INSTANCE_VALUE | 867,760 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 757,860 | 0.6% |
| STORE_FAST_LOAD_FAST | 181,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,634,397 | 24.6% |
| LOAD_FAST_LOAD_FAST | 27,613,920 | 22.2% |
| LOAD_GLOBAL_BUILTIN | 15,217,140 | 12.2% |
| LOAD_ATTR_METHOD_NO_DICT | 10,309,640 | 8.3% |
| BINARY_OP | 6,989,681 | 5.6% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,580,281 | 83.5% |
| LOAD_ATTR_SLOT | 5,106,843 | 10.5% |
| RETURN_VALUE | 1,327,489 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,064,920 | 2.2% |
| LOAD_FAST_LOAD_FAST | 125,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 42,948,653 | 88.4% |
| TO_BOOL_NONE | 3,107,760 | 6.4% |
| RETURN_VALUE | 831,776 | 1.7% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,227,381 | 91.4% |
| LOAD_ATTR_SLOT | 40,651,806 | 3.0% |
| COPY | 40,401,404 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,278,679 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,014,358 | 22.8% |
| TO_BOOL_NONE | 88,078,700 | 6.5% |
| LOAD_ATTR | 81,100,341 | 6.0% |
| TO_BOOL_BOOL | 68,847,342 | 5.1% |
| COMPARE_OP_FLOAT | 66,490,381 | 4.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 281,510,267 | 79.4% |
| LOAD_ATTR_INSTANCE_VALUE | 22,667,983 | 6.4% |
| LOAD_ATTR_WITH_HINT | 22,490,654 | 6.3% |
| COPY | 14,038,523 | 4.0% |
| LOAD_FAST_LOAD_FAST | 8,682,045 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,596,024 | 24.2% |
| STORE_FAST | 43,356,660 | 12.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 37,390,779 | 10.6% |
| COMPARE_OP_INT | 35,280,755 | 10.0% |
| LOAD_CONST | 29,603,800 | 8.4% |


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
| LOAD_FAST | 5,017,094,087 | 52.3% |
| LOAD_CONST | 744,407,188 | 7.8% |
| LOAD_FAST_LOAD_FAST | 458,552,062 | 4.8% |
| STORE_FAST | 293,205,793 | 3.1% |
| POP_JUMP_IF_FALSE | 277,139,628 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,774,699,448 | 18.5% |
| COMPARE_OP_STR | 1,563,963,920 | 16.3% |
| LOAD_FAST | 1,062,052,958 | 11.1% |
| LOAD_CONST | 744,407,188 | 7.8% |
| COMPARE_OP_INT | 672,715,841 | 7.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 341,240,442 | 40.4% |
| LOAD_GLOBAL_BUILTIN | 111,441,672 | 13.2% |
| PUSH_NULL | 38,332,121 | 4.5% |
| POP_JUMP_IF_FALSE | 32,319,177 | 3.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 535,034,536 | 63.4% |
| LOAD_CONST | 69,818,750 | 8.3% |
| LOAD_FAST_LOAD_FAST | 29,849,022 | 3.5% |
| LOAD_DEREF | 24,558,733 | 2.9% |
| CALL_NO_KW_LEN | 20,449,960 | 2.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,443,349,771 | 16.0% |
| STORE_FAST | 4,424,547,769 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 2,666,329,357 | 9.6% |
| RESUME | 2,087,436,893 | 7.5% |
| LOAD_CONST | 1,062,052,958 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,017,094,087 | 18.1% |
| LOAD_ATTR_INSTANCE_VALUE | 3,221,502,051 | 11.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,595,167,152 | 5.7% |
| LOAD_ATTR_SLOT | 1,229,227,381 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,097,579,924 | 4.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 39,945,320 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,380,713 | 23.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 39,937,160 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,380,713 | 23.7% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,682,680 | 50.4% |
| POP_TOP | 2,058,366 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 421,860 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 339,090 | 4.6% |
| STORE_FAST | 308,760 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 49.0% |
| POP_JUMP_IF_NOT_NONE | 1,511,040 | 20.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 5.9% |
| LOAD_FAST | 383,640 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 334,890 | 4.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,332,352,082 | 16.3% |
| POP_JUMP_IF_FALSE | 1,183,236,419 | 14.5% |
| NOP | 959,961,356 | 11.8% |
| LOAD_FAST_LOAD_FAST | 519,356,889 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 480,013,131 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,436,494,402 | 17.6% |
| CONTAINS_OP | 989,415,720 | 12.1% |
| LOAD_FAST | 738,458,244 | 9.0% |
| CALL_PY_EXACT_ARGS | 644,133,011 | 7.9% |
| LOAD_FAST_LOAD_FAST | 519,356,889 | 6.4% |


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
| STORE_FAST | 20,032 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 8,264 | 0.1% |
| NOP | 4,595 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,644 | 98.9% |
| LOAD_GLOBAL_MODULE | 41,864 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 15,893 | 0.2% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,609 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,097,579,924 | 26.5% |
| POP_JUMP_IF_FALSE | 980,817,812 | 23.7% |
| RESUME | 844,809,895 | 20.4% |
| STORE_FAST | 540,592,628 | 13.1% |
| POP_JUMP_IF_TRUE | 102,095,618 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,666,329,357 | 64.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.5% |
| CALL_NO_KW_ISINSTANCE | 331,892,473 | 8.0% |
| LOAD_ATTR | 221,923,460 | 5.4% |
| LOAD_FAST_LOAD_FAST | 113,563,234 | 2.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 904,990,344 | 31.3% |
| STORE_FAST | 421,883,964 | 14.6% |
| RESUME | 339,273,617 | 11.7% |
| POP_JUMP_IF_FALSE | 277,622,887 | 9.6% |
| LOAD_FAST_LOAD_FAST | 125,773,394 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 459,649,224 | 15.9% |
| LOAD_FAST | 449,995,088 | 15.6% |
| CALL_NO_KW_ISINSTANCE | 346,525,380 | 12.0% |
| LOAD_ATTR_MODULE | 324,225,347 | 11.2% |
| CONTAINS_OP | 301,873,338 | 10.4% |


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
| LOAD_FAST | 118,351,314 | 100.0% |
| LOAD_DEREF | 9,080 | 0.0% |
| LOAD_SUPER_ATTR | 1,420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 66,679,861 | 56.3% |
| LOAD_FAST | 37,260,552 | 31.5% |
| CALL_PY_EXACT_ARGS | 6,419,377 | 5.4% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.0% |
| CALL | 1,200,040 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,467,443 | 53.6% |
| CALL_PY_EXACT_ARGS | 31,460,831 | 34.1% |
| CALL_FUNCTION_EX | 4,744,312 | 5.1% |
| CALL | 4,138,926 | 4.5% |
| CALL_PY_WITH_DEFAULTS | 1,593,282 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,467,443 | 53.4% |
| RESUME | 42,520,767 | 45.9% |
| RETURN_GENERATOR | 655,651 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,839,290 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 82,636,757 | 87.1% |
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
| LOAD_FAST | 6,188,714 | 14.9% |
| JUMP_FORWARD | 4,782,840 | 11.6% |
| STORE_FAST | 4,549,800 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,597,580 | 49.8% |
| JUMP_BACKWARD | 19,591,408 | 47.3% |
| CALL_FUNCTION_EX | 1,211,460 | 2.9% |
| DICT_UPDATE | 180 | 0.0% |
| BUILD_MAP | 120 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 718,029,658 | 48.0% |
| RESUME | 337,463,102 | 22.5% |
| STORE_FAST | 159,013,444 | 10.6% |
| POP_JUMP_IF_FALSE | 80,734,318 | 5.4% |
| NOP | 52,969,646 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 959,961,356 | 64.1% |
| LOAD_FAST | 358,684,317 | 24.0% |
| NOP | 52,969,646 | 3.5% |
| PUSH_NULL | 43,635,533 | 2.9% |
| LOAD_GLOBAL_BUILTIN | 34,268,091 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,939,194 | 58.3% |
| STORE_SUBSCR_DICT | 3,085,491 | 18.1% |
| SWAP | 1,973,639 | 11.6% |
| COPY | 1,285,298 | 7.5% |
| STORE_FAST | 546,780 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,500,638 | 55.7% |
| RETURN_VALUE | 1,913,944 | 11.2% |
| JUMP_FORWARD | 1,715,820 | 10.1% |
| POP_TOP | 1,384,994 | 8.1% |
| RERAISE | 1,285,298 | 7.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,359,044,505 | 28.0% |
| CONTAINS_OP | 1,870,240,520 | 22.2% |
| COMPARE_OP_STR | 1,550,235,069 | 18.4% |
| COMPARE_OP_INT | 1,270,866,165 | 15.1% |
| IS_OP | 375,967,109 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,443,349,771 | 52.7% |
| LOAD_FAST_LOAD_FAST | 1,183,236,419 | 14.0% |
| LOAD_GLOBAL_BUILTIN | 980,817,812 | 11.6% |
| JUMP_BACKWARD | 444,398,875 | 5.3% |
| LOAD_GLOBAL_MODULE | 277,622,887 | 3.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 203,451,331 | 68.1% |
| EXTENDED_ARG | 36,519,160 | 12.2% |
| LOAD_ATTR_SLOT | 25,425,420 | 8.5% |
| LOAD_DEREF | 13,781,941 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,404,913 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 132,174,562 | 44.3% |
| PUSH_NULL | 53,765,467 | 18.0% |
| LOAD_DEREF | 28,707,212 | 9.6% |
| JUMP_BACKWARD | 26,808,810 | 9.0% |
| RETURN_CONST | 15,884,706 | 5.3% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 355,170,539 | 82.3% |
| LOAD_ATTR_INSTANCE_VALUE | 30,455,003 | 7.1% |
| LOAD_ATTR | 14,170,936 | 3.3% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.1% |
| EXTENDED_ARG | 7,255,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 157,939,525 | 36.6% |
| LOAD_GLOBAL_BUILTIN | 96,627,572 | 22.4% |
| LOAD_FAST_LOAD_FAST | 60,380,069 | 14.0% |
| LOAD_GLOBAL_MODULE | 36,033,596 | 8.4% |
| PUSH_NULL | 18,680,814 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 735,435,202 | 50.1% |
| TO_BOOL | 132,365,301 | 9.0% |
| COMPARE_OP_INT | 122,124,100 | 8.3% |
| TO_BOOL_ALWAYS_TRUE | 82,915,618 | 5.7% |
| TO_BOOL_NONE | 77,693,504 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 573,783,207 | 39.1% |
| JUMP_BACKWARD | 465,340,438 | 31.7% |
| LOAD_GLOBAL_BUILTIN | 102,095,618 | 7.0% |
| POP_TOP | 72,472,847 | 4.9% |
| LOAD_CONST | 68,425,270 | 4.7% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 573,634,975 | 25.3% |
| RESUME | 472,273,965 | 20.8% |
| CALL_NO_KW_BUILTIN_O | 341,716,573 | 15.0% |
| POP_JUMP_IF_FALSE | 169,430,574 | 7.5% |
| RETURN_VALUE | 123,834,708 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 851,162,133 | 36.1% |
| JUMP_BACKWARD | 657,977,823 | 27.9% |
| RESUME | 238,823,831 | 10.1% |
| RETURN_CONST | 184,081,891 | 7.8% |
| LOAD_FAST_LOAD_FAST | 99,544,144 | 4.2% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,215,582 | 30.7% |
| LOAD_ATTR | 3,246,421 | 19.1% |
| RAISE_VARARGS | 2,298,203 | 13.5% |
| CALL_NO_KW_BUILTIN_FAST | 1,785,260 | 10.5% |
| RERAISE | 1,115,630 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,414,626 | 90.4% |
| LOAD_GLOBAL_MODULE | 1,103,235 | 6.5% |
| LOAD_FAST | 387,186 | 2.3% |
| WITH_EXCEPT_START | 138,123 | 0.8% |
| LOAD_GLOBAL | 617 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 274,220,684 | 34.9% |
| POP_JUMP_IF_FALSE | 114,547,281 | 14.6% |
| POP_TOP | 70,762,430 | 9.0% |
| POP_JUMP_IF_NONE | 53,765,467 | 6.8% |
| NOP | 43,635,533 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 433,935,019 | 55.2% |
| LOAD_FAST_LOAD_FAST | 310,633,850 | 39.5% |
| LOAD_DEREF | 38,332,121 | 4.9% |
| LOAD_GLOBAL_BUILTIN | 3,416,040 | 0.4% |
| PUSH_NULL | 272,934 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,494,536 | 51.6% |
| LOAD_ATTR_MODULE | 583,740 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 18.8% |
| LOAD_FAST | 151,164 | 5.2% |
| RETURN_VALUE | 55,440 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,298,203 | 79.4% |
| COPY | 445,440 | 15.4% |
| LOAD_CONST | 151,224 | 5.2% |
| CALL_INTRINSIC_1 | 36 | 0.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,381,104 | 75.1% |
| POP_EXCEPT | 1,285,298 | 15.1% |
| POP_TOP | 386,940 | 4.6% |
| POP_JUMP_IF_FALSE | 155,640 | 1.8% |
| DELETE_FAST | 151,224 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,115,630 | 56.1% |
| COPY | 831,212 | 41.8% |
| CALL_INTRINSIC_1 | 42,144 | 2.1% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,521,816,262 | 63.5% |
| POP_TOP | 238,823,831 | 6.0% |
| CALL | 211,845,403 | 5.3% |
| SEND_GEN | 208,501,225 | 5.2% |
| COPY_FREE_VARS | 179,675,094 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,087,436,893 | 41.8% |
| LOAD_GLOBAL_BUILTIN | 844,809,895 | 16.9% |
| POP_TOP | 472,273,965 | 9.5% |
| LOAD_GLOBAL_MODULE | 339,273,617 | 6.8% |
| NOP | 337,463,102 | 6.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 267,543,589 | 19.9% |
| STORE_ATTR_SLOT | 246,971,411 | 18.4% |
| POP_TOP | 184,081,891 | 13.7% |
| STORE_ATTR_INSTANCE_VALUE | 178,469,978 | 13.3% |
| RESUME | 122,771,702 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 573,634,975 | 42.7% |
| INTERPRETER_EXIT | 410,748,122 | 30.6% |
| EXIT_INIT_CHECK | 67,125,785 | 5.0% |
| TO_BOOL_BOOL | 56,811,082 | 4.2% |
| END_FOR | 56,701,025 | 4.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,431,731 | 63.6% |
| COPY_FREE_VARS | 73,605,650 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,374,277 | 1.5% |
| CALL_FUNCTION_EX | 1,715,660 | 0.8% |
| CALL | 873,198 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,584,969 | 32.9% |
| GET_ITER | 37,670,522 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,880 | 13.8% |
| STORE_FAST | 19,530,120 | 8.2% |
| INTERPRETER_EXIT | 18,176,220 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 781,930,623 | 26.0% |
| RETURN_VALUE | 518,784,875 | 17.2% |
| BUILD_TUPLE | 413,113,306 | 13.7% |
| LOAD_ATTR_INSTANCE_VALUE | 181,689,619 | 6.0% |
| BINARY_SUBSCR_DICT | 104,203,354 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 624,265,104 | 20.7% |
| RETURN_VALUE | 518,784,875 | 17.2% |
| INTERPRETER_EXIT | 329,721,066 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 264,500,662 | 8.8% |
| TO_BOOL_BOOL | 261,873,944 | 8.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,455,900 | 94.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,245,572 | 5.5% |
| SEND | 28,885 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,454,850 | 89.1% |
| YIELD_VALUE | 6,246,010 | 5.5% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,885 | 0.0% |
| SEND_GEN | 606 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,501,279 | 69.0% |
| LOAD_CONST | 93,861,325 | 31.0% |
| SEND | 606 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,501,225 | 69.0% |
| POP_TOP | 93,861,805 | 31.0% |
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
| MAKE_FUNCTION | 82,636,757 | 98.7% |
| SET_FUNCTION_ATTRIBUTE | 1,108,644 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,219,650 | 64.7% |
| LOAD_GLOBAL_BUILTIN | 18,989,340 | 22.7% |
| STORE_FAST | 5,794,634 | 6.9% |
| CALL_PY_EXACT_ARGS | 2,062,872 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 1,108,644 | 1.3% |


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
| LOAD_FAST | 31,580,653 | 59.0% |
| LOAD_FAST_LOAD_FAST | 15,244,558 | 28.5% |
| CALL | 5,419,260 | 10.1% |
| SWAP | 946,685 | 1.8% |
| LOAD_GLOBAL_MODULE | 199,140 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,910,486 | 29.7% |
| LOAD_DEREF | 13,447,060 | 25.1% |
| RETURN_CONST | 8,606,030 | 16.1% |
| JUMP_BACKWARD | 5,554,200 | 10.4% |
| LOAD_FAST_LOAD_FAST | 4,743,837 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 375,884,523 | 45.0% |
| LOAD_FAST_LOAD_FAST | 303,079,750 | 36.3% |
| SWAP | 80,659,335 | 9.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.2% |
| RETURN_VALUE | 20,943,360 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 310,789,070 | 37.2% |
| RETURN_CONST | 178,469,978 | 21.4% |
| LOAD_FAST_LOAD_FAST | 167,820,827 | 20.1% |
| LOAD_CONST | 73,319,511 | 8.8% |
| NOP | 51,795,988 | 6.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 515,578,570 | 48.5% |
| LOAD_FAST | 504,065,079 | 47.4% |
| SWAP | 40,401,404 | 3.8% |
| STORE_ATTR_SLOT | 2,127,230 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 279,501,107 | 26.3% |
| LOAD_FAST | 253,874,743 | 23.9% |
| RETURN_CONST | 246,971,411 | 23.2% |
| LOAD_CONST | 220,183,600 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 25,391,400 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,039,041 | 50.0% |
| SWAP | 14,038,523 | 26.0% |
| LOAD_FAST_LOAD_FAST | 12,443,823 | 23.0% |
| LOAD_DEREF | 242,500 | 0.4% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,962,848 | 62.8% |
| RETURN_CONST | 6,694,842 | 12.4% |
| JUMP_BACKWARD | 5,313,540 | 9.8% |
| LOAD_CONST | 3,924,016 | 7.3% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.3% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,874,000 | 40.9% |
| STORE_FAST | 19,047,660 | 29.0% |
| LOAD_CONST | 6,838,765 | 10.4% |
| LOAD_FAST | 2,917,140 | 4.4% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,460 | 28.9% |
| LOAD_DEREF | 13,769,735 | 20.9% |
| LOAD_FAST_LOAD_FAST | 13,437,000 | 20.4% |
| LOAD_FAST | 9,631,399 | 14.6% |
| LOAD_CONST | 4,834,675 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,763,458 | 12.8% |
| BINARY_SUBSCR | 977,845,482 | 9.9% |
| STORE_FAST | 711,196,126 | 7.2% |
| RETURN_VALUE | 624,265,104 | 6.3% |
| FOR_ITER_LIST | 587,187,520 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,424,547,769 | 45.0% |
| LOAD_FAST_LOAD_FAST | 1,332,352,082 | 13.5% |
| JUMP_BACKWARD | 918,432,425 | 9.3% |
| STORE_FAST | 711,196,126 | 7.2% |
| LOAD_GLOBAL_BUILTIN | 540,592,628 | 5.5% |


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
| FOR_ITER | 2,965,745 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,780 | 22.2% |
| LOAD_FAST | 24,358,500 | 18.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,555,720 | 15.4% |
| STORE_ATTR_INSTANCE_VALUE | 9,297,252 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,842 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 368,147,865 | 23.9% |
| UNPACK_SEQUENCE_TUPLE | 140,575,268 | 9.1% |
| UNPACK_SEQUENCE_LIST | 134,205,000 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,842 | 52.8% |
| LOAD_FAST | 452,913,816 | 29.4% |
| LOAD_FAST_LOAD_FAST | 86,523,220 | 5.6% |
| STORE_FAST | 75,477,186 | 4.9% |
| LOAD_GLOBAL_MODULE | 46,178,824 | 3.0% |


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
| LOAD_CONST | 13,495,572 | 11.5% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,615,052 | 91.5% |
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
| SWAP | 109,838,320 | 34.7% |
| LOAD_FAST | 64,774,564 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 17.9% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.1% |
| LOAD_CONST | 27,783,040 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.4% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 32.9% |
| RETURN_CONST | 33,885,785 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,003,020 | 8.5% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 95,460,714 | 48.0% |
| LOAD_FAST | 63,111,804 | 31.7% |
| CALL_NO_KW_BUILTIN_O | 13,999,260 | 7.0% |
| RETURN_VALUE | 7,992,040 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,054,145 | 36.7% |
| LOAD_FAST | 66,078,744 | 33.2% |
| JUMP_BACKWARD | 31,629,374 | 15.9% |
| RETURN_CONST | 12,893,885 | 6.5% |
| LOAD_GLOBAL_MODULE | 7,343,166 | 3.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,500 | 52.2% |
| LOAD_FAST | 57,439,700 | 19.0% |
| LOAD_CONST | 26,911,812 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,062,300 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,905,360 | 38.0% |
| JUMP_BACKWARD | 110,636,710 | 36.6% |
| LOAD_FAST_LOAD_FAST | 71,548,270 | 23.7% |
| RETURN_CONST | 4,469,760 | 1.5% |
| LOAD_CONST | 231,120 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,856,793 | 28.8% |
| BINARY_OP_ADD_FLOAT | 116,612,524 | 12.5% |
| LOAD_FAST | 105,298,980 | 11.3% |
| BINARY_OP_ADD_INT | 90,613,231 | 9.7% |
| BINARY_OP_SUBTRACT_INT | 69,253,513 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,856,793 | 28.8% |
| STORE_SUBSCR_LIST_INT | 157,633,500 | 16.9% |
| COPY | 112,622,859 | 12.0% |
| STORE_SUBSCR | 109,838,320 | 11.8% |
| STORE_ATTR_INSTANCE_VALUE | 80,659,335 | 8.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,776,541 | 80.9% |
| LOAD_ATTR_INSTANCE_VALUE | 23,951,203 | 11.7% |
| LOAD_ATTR | 7,358,476 | 3.6% |
| LOAD_ATTR_SLOT | 3,352,620 | 1.6% |
| COPY | 2,330,965 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 132,365,301 | 64.6% |
| POP_JUMP_IF_FALSE | 71,871,818 | 35.1% |
| TO_BOOL | 235,800 | 0.1% |
| UNARY_NOT | 220,621 | 0.1% |
| TO_BOOL_NONE | 125,709 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,565,228 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,746,352 | 33.4% |
| LOAD_ATTR_SLOT | 17,761,080 | 9.9% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 7,172,935 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 94,344,231 | 52.7% |
| POP_JUMP_IF_TRUE | 82,915,618 | 46.3% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,846 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,501 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 801,059,204 | 24.7% |
| LOAD_FAST | 715,260,391 | 22.1% |
| CALL_NO_KW_BUILTIN_FAST | 477,713,140 | 14.8% |
| LOAD_ATTR_INSTANCE_VALUE | 433,474,985 | 13.4% |
| RETURN_VALUE | 261,873,944 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,359,044,505 | 72.9% |
| POP_JUMP_IF_TRUE | 735,435,202 | 22.7% |
| EXTENDED_ARG | 88,770,394 | 2.7% |
| UNARY_NOT | 53,930,780 | 1.7% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 173,554,841 | 76.0% |
| CALL_NO_KW_BUILTIN_O | 12,836,580 | 5.6% |
| COPY | 12,731,284 | 5.6% |
| BINARY_OP | 9,150,731 | 4.0% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,530,184 | 88.2% |
| POP_JUMP_IF_TRUE | 25,625,283 | 11.2% |
| UNARY_NOT | 1,035,600 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,876,773 | 66.9% |
| LOAD_ATTR_INSTANCE_VALUE | 27,748,423 | 24.8% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,712,180 | 1.5% |
| COPY | 814,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,666,574 | 55.1% |
| POP_JUMP_IF_FALSE | 46,715,857 | 41.7% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,761 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,518,798 | 45.0% |
| LOAD_ATTR_SLOT | 88,078,700 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 53,032,667 | 14.1% |
| LOAD_ATTR | 21,871,032 | 5.8% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 296,852,358 | 78.9% |
| POP_JUMP_IF_TRUE | 77,693,504 | 20.6% |
| EXTENDED_ARG | 967,320 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,933 | 0.2% |
| TO_BOOL | 123,673 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,966,054 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,407,740 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,340 | 5.8% |
| COPY | 2,682,160 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 36,172,736 | 53.8% |
| POP_JUMP_IF_TRUE | 30,414,562 | 45.2% |
| UNARY_NOT | 600,240 | 0.9% |
| TO_BOOL_NONE | 36,180 | 0.1% |
| EXTENDED_ARG | 8,280 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,621,307 | 92.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 397,706 | 3.5% |
| LOAD_ATTR_MODULE | 311,577 | 2.7% |
| LOAD_FAST | 122,040 | 1.1% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,462,890 | 100.0% |


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
| TO_BOOL_BOOL | 53,930,780 | 92.3% |
| TO_BOOL_LIST | 2,640,720 | 4.5% |
| TO_BOOL_INT | 1,035,600 | 1.8% |
| TO_BOOL_STR | 600,240 | 1.0% |
| TO_BOOL | 220,621 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 29,526,900 | 50.5% |
| RETURN_VALUE | 16,583,539 | 28.4% |
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
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,941 | 31.4% |
| COPY | 19,920 | 9.2% |
| FOR_ITER_LIST | 10,560 | 4.9% |
| CALL_BUILTIN_CLASS | 10,080 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,282 | 62.0% |
| STORE_FAST | 79,687 | 36.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,729 | 0.8% |
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
| RETURN_VALUE | 264,500,662 | 62.2% |
| LOAD_FAST | 103,134,100 | 24.2% |
| BINARY_SUBSCR_DICT | 15,509,726 | 3.6% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260,433,953 | 61.2% |
| STORE_FAST_STORE_FAST | 140,575,268 | 33.1% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.6% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,621,398 | 52.0% |
| FOR_ITER | 151,762,124 | 25.1% |
| RETURN_VALUE | 84,701,610 | 14.0% |
| LOAD_FAST | 35,337,180 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 368,147,865 | 60.8% |
| STORE_FAST | 215,215,609 | 35.5% |
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
| TO_BOOL_NONE | 137,323 | 99.4% |
| TO_BOOL_BOOL | 780 | 0.6% |
| TO_BOOL | 20 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.4% |
| YIELD_VALUE | 208,501,573 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,259 | 4.5% |
| LOAD_CONST | 26,890,884 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 451,458,842 | 65.1% |
| YIELD_VALUE | 208,501,573 | 30.1% |
| STORE_FAST | 24,773,582 | 3.6% |
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
| specialization.deferred |    204567672 | 4.6% |
| specialization.deopt |      1599014 | 0.0% |
|          hit |   4115212266 | 93.4% |
|         miss |     84780144 | 1.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,613,124 | 80.8% |
| Failure | 383,573 | 19.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.4% |
| other | 125,983 | 32.8% |
| tuple | 75,020 | 19.6% |
| dict | 16,816 | 4.4% |
| bytes | 10,778 | 2.8% |
| set | 7,220 | 1.9% |
| sequence | 6,040 | 1.6% |
| mapping | 4,596 | 1.2% |
| float | 980 | 0.3% |
| bytearray | 320 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2350979110 | 56.1% |
| specialization.deopt |        65098 | 0.0% |
|          hit |   1834604905 | 43.8% |
|         miss |      3451386 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 67,152 | 10.2% |
| Failure | 591,781 | 89.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 305,140 | 51.6% |
| array int | 112,980 | 19.1% |
| other | 77,501 | 13.1% |
| out of range | 40,460 | 6.8% |
| buffer int | 25,740 | 4.3% |
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
| specialization.deferred |    316114150 | 38.7% |
| specialization.deopt |           40 | 0.0% |
|          hit |    501161237 | 61.3% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,750 | 2.0% |
| Failure | 83,799 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.5% |
| dict subclass no override | 17,961 | 21.4% |
| py simple | 13,818 | 16.5% |
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
| specialization.deferred |       213969 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1168560855 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,289 | 99.1% |
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
| specialization.deferred |    293082853 | 11.6% |
| specialization.deopt |      2480429 | 0.1% |
|          hit |   2103696844 | 83.2% |
|         miss |    131463445 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,497 | 96.3% |
| Failure | 96,635 | 3.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,020 | 23.8% |
| dict items | 20,427 | 21.1% |
| seq iter | 15,120 | 15.6% |
| set | 13,187 | 13.6% |
| other | 7,660 | 7.9% |
| dict values | 3,820 | 4.0% |
| reversed list | 3,641 | 3.8% |
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
| specialization.deferred |     53481968 | 2.7% |
| specialization.deopt |      3602124 | 0.2% |
|          hit |   1760805021 | 87.8% |
|         miss |    190930273 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,624,532 | 98.9% |
| Failure | 38,740 | 1.1% |

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
| not managed dict | 380 | 1.0% |
| method | 300 | 0.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1070777372 | 10.2% |
| specialization.deopt |     10551215 | 0.1% |
|          hit |   8842872000 | 84.4% |
|         miss |    559371001 | 5.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,622,663 | 87.9% |
| Failure | 1,456,463 | 12.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 1,154,631 | 79.3% |
| metaclass attribute | 101,977 | 7.0% |
| method | 60,722 | 4.2% |
| not managed dict | 59,483 | 4.1% |
| shadowed | 40,608 | 2.8% |
| non object slot | 7,712 | 0.5% |
| class method obj | 7,261 | 0.5% |
| class attr descriptor | 6,286 | 0.4% |
| overridden | 5,220 | 0.4% |
| non overriding descriptor | 4,476 | 0.3% |
| mutable class | 2,861 | 0.2% |
| not in keys | 1,740 | 0.1% |
| class attr simple | 1,686 | 0.1% |
| module attr not found | 1,340 | 0.1% |
| builtin class method | 440 | 0.0% |
| property | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    145420168 | 4.3% |
| specialization.deopt |        26276 | 0.0% |
|          hit |   3207858439 | 95.6% |
|         miss |      1393912 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 30,294 | 21.0% |
| Failure | 113,698 | 79.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 51,400 | 45.2% |
| different types | 23,814 | 20.9% |
| baseobject | 13,260 | 11.7% |
| float long | 9,289 | 8.2% |
| set | 6,620 | 5.8% |
| other | 3,000 | 2.6% |
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
| specialization.deferred |      7322472 | 0.1% |
| specialization.deopt |          435 | 0.0% |
|          hit |   7026823849 | 99.9% |
|         miss |        24763 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 54,732 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    841232295 | 15.6% |
| specialization.deopt |       712840 | 0.0% |
|          hit |   4518927960 | 83.7% |
|         miss |     37782968 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,923 | 39.2% |
| Failure | 1,110,838 | 60.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,020 | 52.1% |
| multiply different types | 171,562 | 15.4% |
| add different types | 151,879 | 13.7% |
| floor divide | 32,920 | 3.0% |
| and int | 32,278 | 2.9% |
| remainder | 32,024 | 2.9% |
| add other | 27,100 | 2.4% |
| lshift | 18,760 | 1.7% |
| rshift | 16,632 | 1.5% |
| true divide different types | 14,867 | 1.3% |
| xor | 10,500 | 0.9% |
| true divide float | 6,785 | 0.6% |
| subtract other | 5,520 | 0.5% |
| or | 4,105 | 0.4% |
| power | 3,703 | 0.3% |
| true divide other | 1,203 | 0.1% |
| multiply other | 1,060 | 0.1% |
| and other | 860 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112700866 | 27.2% |
|          hit |    302363030 | 72.8% |
|         miss |          180 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 606 | 2.1% |
| Failure | 28,885 | 97.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 84.6% |
| other | 4,365 | 15.1% |
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
|          hit |    120660654 | 100.0% |

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
| specialization.deferred |    894028308 | 10.1% |
| specialization.deopt |      2800408 | 0.0% |
|          hit |   7809761860 | 88.2% |
|         miss |    148544943 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,847,620 | 87.8% |
| Failure | 394,085 | 12.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 66,310 | 16.8% |
| kwnames | 56,140 | 14.2% |
| code complex parameters | 54,198 | 13.8% |
| no dict | 51,380 | 13.0% |
| class no vectorcall | 29,456 | 7.5% |
| cfunc varargs keywords | 24,884 | 6.3% |
| cfunc noargs | 22,546 | 5.7% |
| meth descr varargs | 22,420 | 5.7% |
| other | 11,458 | 2.9% |
| init not python | 10,420 | 2.6% |
| class mutable | 8,761 | 2.2% |
| init not simple | 8,421 | 2.1% |
| meth descr varargs keywords | 7,329 | 1.9% |
| wrong number arguments | 4,460 | 1.1% |
| cmethod | 3,600 | 0.9% |
| bound method | 3,366 | 0.9% |
| cfunc varargs | 3,091 | 0.8% |
| method wrapper | 2,480 | 0.6% |
| operator wrapper | 2,365 | 0.6% |
| str | 1,000 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 94,449,299,596 | 63.5% |
| Not specialized | 11,033,411,512 | 7.4% |
| Specialized | 43,176,800,098 | 29.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,350,979,110 | 37.4% |
| LOAD_ATTR | 1,070,777,372 | 17.0% |
| CALL | 894,028,308 | 14.2% |
| BINARY_OP | 841,232,295 | 13.4% |
| STORE_SUBSCR | 316,114,150 | 5.0% |
| FOR_ITER | 293,082,853 | 4.7% |
| TO_BOOL | 204,567,672 | 3.3% |
| COMPARE_OP | 145,420,168 | 2.3% |
| SEND | 112,700,866 | 1.8% |
| STORE_ATTR | 53,481,968 | 0.9% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 231,305,258 | 19.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 168,428,670 | 14.5% |
| STORE_ATTR_SLOT | 112,736,766 | 9.7% |
| CALL_PY_EXACT_ARGS | 89,440,882 | 7.7% |
| STORE_ATTR_INSTANCE_VALUE | 75,036,259 | 6.5% |
| FOR_ITER_LIST | 65,827,891 | 5.7% |
| FOR_ITER_TUPLE | 65,584,134 | 5.7% |
| LOAD_ATTR_SLOT | 57,456,039 | 5.0% |
| LOAD_ATTR_METHOD_NO_DICT | 45,687,660 | 3.9% |
| TO_BOOL_NONE | 41,154,892 | 3.5% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,218,676,339 | 23.2% |
| Calls to Python functions inlined | 4,030,436,091 | 76.8% |
| Calls via PyEval_EvalFrame (total) | 1,218,676,339 | 23.2% |
| Calls via PyEval_EvalFrame (vector) | 678,956,154 | 12.9% |
| Calls via PyEval_EvalFrame (generator) | 539,720,185 | 10.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 678,951,054 | 12.9% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 191,539,250 | 3.6% |
| Calls via PyEval_EvalFrame (function ex) | 13,952,944 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 115,841,552 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 94,976,474 | 1.8% |
| Frames pushed | 4,383,940,668 | 83.5% |
| Frame objects created | 59,292,384 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,172,097,865 | 35.4% |
| Frees to freelist | 4,176,254,358 |  |
| Allocations | 7,619,568,067 | 64.6% |
| Allocations to 512 bytes | 7,537,834,992 | 63.9% |
| Allocations to 4 kbytes | 66,549,412 | 0.6% |
| Allocations over 4 kbytes | 15,183,663 | 0.1% |
| Frees | 7,862,288,545 |  |
| New values | 57,541,459 |  |
| Interpreter increfs | 56,471,846,260 | 76.6% |
| Interpreter decrefs | 65,534,098,566 | 77.2% |
| Increfs | 17,286,278,982 | 23.4% |
| Decrefs | 19,383,986,926 | 22.8% |
| Materialize dict (on request) | 3,685,802 | 6.4% |
| Materialize dict (new key) | 58,140 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,912,970,032 |  |
| Method cache misses | 70,515,499 |  |
| Method cache collisions | 74,994,020 |  |
| Method cache dunder hits | 2,211,756,666 |  |
| Method cache dunder misses | 4,519,377 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 350,234 | 34,411,686 | 3,608,183,622 |
| 1 | 31,106 | 51,220,070 | 2,680,590,521 |
| 2 | 14,224 | 42,608,639 | 9,952,642,884 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,278 |


</details>

---
Stats gathered on: 2023-08-04
