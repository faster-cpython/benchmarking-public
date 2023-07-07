
# Pystats results

- fork: faster-cpython
- ref: specialize-more-load-attr
- commit hash: 16a2718
- commit date: 2023-07-05T17:16:30+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 28,019,765,324 | 18.7% | 18.7% |  |
| STORE_FAST | 9,863,358,286 | 6.6% | 25.2% |  |
| LOAD_CONST | 9,603,650,077 | 6.4% | 31.6% |  |
| POP_JUMP_IF_FALSE | 8,437,090,139 | 5.6% | 37.3% |  |
| LOAD_FAST_LOAD_FAST | 8,161,628,339 | 5.4% | 42.7% |  |
| RESUME | 4,983,741,276 | 3.3% | 46.0% |  |
| LOAD_GLOBAL_BUILTIN | 4,138,302,978 | 2.8% | 48.8% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,789,205,991 | 2.5% | 51.3% | 6.1% |
| TO_BOOL_BOOL | 3,235,787,967 | 2.2% | 53.5% | 0.0% |
| JUMP_BACKWARD | 3,213,696,745 | 2.1% | 55.6% |  |
| RETURN_VALUE | 3,007,565,793 | 2.0% | 57.6% |  |
| LOAD_GLOBAL_MODULE | 2,888,505,874 | 1.9% | 59.5% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,833,401,451 | 1.9% | 61.4% | 3.2% |
| STORE_FAST_STORE_FAST | 2,525,351,360 | 1.7% | 63.1% |  |
| POP_TOP | 2,356,398,739 | 1.6% | 64.7% |  |
| BINARY_SUBSCR | 2,351,531,919 | 1.6% | 66.2% |  |
| BINARY_OP_ADD_INT | 2,225,621,119 | 1.5% | 67.7% | 0.0% |
| CONTAINS_OP | 1,982,568,842 | 1.3% | 69.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,857,841,980 | 1.2% | 70.3% | 9.1% |
| COMPARE_OP_STR | 1,590,519,987 | 1.1% | 71.3% | 0.0% |
| COMPARE_OP_INT | 1,506,112,477 | 1.0% | 72.3% | 0.1% |
| NOP | 1,497,932,075 | 1.0% | 73.3% |  |
| POP_JUMP_IF_TRUE | 1,466,061,964 | 1.0% | 74.3% |  |
| LOAD_ATTR_SLOT | 1,345,212,416 | 0.9% | 75.2% | 4.3% |
| RETURN_CONST | 1,341,894,574 | 0.9% | 76.1% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,337,515,691 | 0.9% | 77.0% | 3.4% |
| FOR_ITER_LIST | 1,238,014,835 | 0.8% | 77.8% | 5.3% |
| INTERPRETER_EXIT | 1,209,453,708 | 0.8% | 78.6% |  |
| COPY | 1,074,228,161 | 0.7% | 79.3% |  |
| LOAD_ATTR | 1,071,389,079 | 0.7% | 80.0% |  |
| STORE_ATTR_SLOT | 1,063,068,208 | 0.7% | 80.8% | 10.6% |
| CALL_NO_KW_BUILTIN_FAST | 935,181,378 | 0.6% | 81.4% | 0.0% |
| SWAP | 934,010,751 | 0.6% | 82.0% |  |
| CALL | 900,430,451 | 0.6% | 82.6% |  |
| BINARY_SUBSCR_LIST_INT | 883,050,142 | 0.6% | 83.2% | 0.4% |
| BINARY_OP | 857,287,737 | 0.6% | 83.8% |  |
| LOAD_DEREF | 843,766,525 | 0.6% | 84.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 833,885,433 | 0.6% | 84.9% | 9.0% |
| BINARY_OP_MULTIPLY_FLOAT | 827,749,087 | 0.6% | 85.4% | 0.8% |
| CALL_NO_KW_ISINSTANCE | 813,810,813 | 0.5% | 86.0% |  |
| PUSH_NULL | 785,932,094 | 0.5% | 86.5% |  |
| CALL_NO_KW_BUILTIN_O | 785,528,003 | 0.5% | 87.0% | 0.1% |
| YIELD_VALUE | 693,204,315 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 692,363,112 | 0.5% | 87.9% |  |
| BINARY_SUBSCR_DICT | 623,779,294 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 605,148,658 | 0.4% | 88.8% |  |
| GET_ITER | 593,574,162 | 0.4% | 89.2% |  |
| UNPACK_SEQUENCE_TUPLE | 525,985,465 | 0.4% | 89.5% | 0.2% |
| BINARY_OP_SUBTRACT_INT | 500,635,884 | 0.3% | 89.8% | 0.1% |
| FOR_ITER_RANGE | 485,332,917 | 0.3% | 90.2% | 0.0% |
| IS_OP | 444,351,548 | 0.3% | 90.5% |  |
| POP_JUMP_IF_NOT_NONE | 430,196,107 | 0.3% | 90.7% |  |
| FOR_ITER_TUPLE | 422,609,147 | 0.3% | 91.0% | 15.5% |
| JUMP_FORWARD | 422,554,475 | 0.3% | 91.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 397,787,393 | 0.3% | 91.6% | 1.7% |
| BINARY_OP_ADD_FLOAT | 391,064,163 | 0.3% | 91.8% | 1.6% |
| TO_BOOL_NONE | 376,339,808 | 0.3% | 92.1% | 10.9% |
| LOAD_ATTR_WITH_HINT | 354,376,801 | 0.2% | 92.3% | 2.5% |
| CALL_NO_KW_LEN | 345,592,358 | 0.2% | 92.5% |  |
| LOAD_ATTR_MODULE | 340,144,408 | 0.2% | 92.8% | 0.0% |
| CALL_NO_KW_TYPE_1 | 336,013,997 | 0.2% | 93.0% |  |
| STORE_SUBSCR | 316,197,311 | 0.2% | 93.2% |  |
| EXTENDED_ARG | 309,247,043 | 0.2% | 93.4% |  |
| SEND_GEN | 302,379,454 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR_LIST_INT | 302,183,816 | 0.2% | 93.8% | 0.0% |
| BUILD_LIST | 300,607,148 | 0.2% | 94.0% |  |
| POP_JUMP_IF_NONE | 298,481,449 | 0.2% | 94.2% |  |
| FOR_ITER | 293,118,840 | 0.2% | 94.4% |  |
| BINARY_OP_SUBTRACT_FLOAT | 270,292,777 | 0.2% | 94.6% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 266,393,834 | 0.2% | 94.8% | 3.2% |
| COPY_FREE_VARS | 252,661,641 | 0.2% | 94.9% |  |
| BINARY_SLICE | 248,179,517 | 0.2% | 95.1% |  |
| CALL_NO_KW_LIST_APPEND | 239,517,791 | 0.2% | 95.3% | 0.0% |
| RETURN_GENERATOR | 238,835,118 | 0.2% | 95.4% |  |
| UNPACK_SEQUENCE_LIST | 238,538,020 | 0.2% | 95.6% | 0.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 233,149,715 | 0.2% | 95.7% | 6.9% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 227,986,332 | 0.2% | 95.9% | 0.0% |
| TO_BOOL_INT | 227,842,866 | 0.2% | 96.0% | 0.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,756,278 | 0.1% | 96.2% |  |
| TO_BOOL | 204,842,611 | 0.1% | 96.3% |  |
| STORE_SUBSCR_DICT | 198,510,196 | 0.1% | 96.5% |  |
| END_SEND | 194,319,171 | 0.1% | 96.6% |  |
| BINARY_SUBSCR_TUPLE_INT | 188,463,615 | 0.1% | 96.7% | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 178,900,512 | 0.1% | 96.8% | 21.3% |
| KW_NAMES | 175,272,082 | 0.1% | 96.9% |  |
| CALL_PY_WITH_DEFAULTS | 169,797,931 | 0.1% | 97.1% | 3.1% |
| BUILD_SLICE | 158,213,142 | 0.1% | 97.2% |  |
| CALL_INTRINSIC_1 | 154,085,432 | 0.1% | 97.3% |  |
| COMPARE_OP | 147,117,013 | 0.1% | 97.4% |  |
| BINARY_SUBSCR_GETITEM | 147,065,366 | 0.1% | 97.5% | 0.0% |
| LIST_APPEND | 146,630,734 | 0.1% | 97.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,190,927 | 0.1% | 97.7% | 19.2% |
| STORE_FAST_LOAD_FAST | 133,211,218 | 0.1% | 97.7% |  |
| DELETE_SUBSCR | 127,969,367 | 0.1% | 97.8% |  |
| CALL_BUILTIN_CLASS | 126,377,849 | 0.1% | 97.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 123,797,649 | 0.1% | 98.0% | 32.8% |
| UNARY_NEGATIVE | 121,275,060 | 0.1% | 98.1% |  |
| LOAD_ATTR_CLASS | 121,001,835 | 0.1% | 98.2% | 1.1% |
| LOAD_SUPER_ATTR_METHOD | 117,716,308 | 0.1% | 98.2% |  |
| STORE_SLICE | 117,672,986 | 0.1% | 98.3% |  |
| FORMAT_SIMPLE | 117,347,791 | 0.1% | 98.4% |  |
| SEND | 112,735,192 | 0.1% | 98.5% |  |
| TO_BOOL_LIST | 111,775,684 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 111,089,719 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,736,285 | 0.1% | 98.7% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 94,866,152 | 0.1% | 98.8% |  |
| MAKE_CELL | 92,715,401 | 0.1% | 98.9% |  |
| FOR_ITER_GEN | 89,950,536 | 0.1% | 98.9% | 0.0% |
| GET_AWAITABLE | 85,021,530 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 83,779,939 | 0.1% | 99.0% |  |
| CALL_FUNCTION_EX | 83,017,505 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 78,764,042 | 0.1% | 99.2% | 0.0% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,462,207 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 68,047,063 | 0.0% | 99.2% |  |
| TO_BOOL_STR | 67,241,023 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 66,750,747 | 0.0% | 99.3% |  |
| STORE_DEREF | 65,773,776 | 0.0% | 99.4% |  |
| BUILD_MAP | 63,757,559 | 0.0% | 99.4% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 59,214,775 | 0.0% | 99.5% | 0.0% |
| BUILD_STRING | 59,068,486 | 0.0% | 99.5% |  |
| UNARY_NOT | 58,367,590 | 0.0% | 99.5% |  |
| END_FOR | 56,700,607 | 0.0% | 99.6% |  |
| LIST_EXTEND | 54,206,640 | 0.0% | 99.6% |  |
| STORE_ATTR_WITH_HINT | 54,053,860 | 0.0% | 99.6% | 5.8% |
| STORE_ATTR | 53,539,143 | 0.0% | 99.7% |  |
| LOAD_FAST_AND_CLEAR | 52,046,880 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 48,216,580 | 0.0% | 99.7% | 11.4% |
| MAP_ADD | 41,400,838 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,654,252 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 30,832,106 | 0.0% | 99.8% | 5.7% |
| CALL_NO_KW_TUPLE_1 | 22,382,206 | 0.0% | 99.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 22,351,920 | 0.0% | 99.9% | 0.0% |
| PUSH_EXC_INFO | 17,939,421 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,939,414 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 17,472,291 | 0.0% | 99.9% |  |
| DICT_MERGE | 16,263,676 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,170,583 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 12,130,343 | 0.0% | 99.9% |  |
| RERAISE | 9,093,380 | 0.0% | 100.0% |  |
| DELETE_ATTR | 8,520,801 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,377,419 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,190,641 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,700 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,923,720 | 0.0% | 100.0% |  |
| BEFORE_WITH | 5,011,719 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 4,636,272 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,493,975 | 0.0% | 100.0% |  |
| SET_ADD | 3,234,120 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,272,920 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,987,321 | 0.0% | 100.0% |  |
| BUILD_SET | 1,918,507 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,668,901 | 0.0% | 100.0% |  |
| DELETE_FAST | 631,316 | 0.0% | 100.0% |  |
| UNPACK_EX | 286,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 216,637 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 137,883 | 0.0% | 100.0% |  |
| SET_UPDATE | 66,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 53,006 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,993 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,433 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,413 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,220 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,540 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 846 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 5,020,529,246 | 3.3% | 3.3% |
| STORE_FAST LOAD_FAST | 4,451,014,170 | 3.0% | 6.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,444,069,568 | 3.0% | 9.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,217,397,598 | 2.1% | 11.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,667,669,417 | 1.8% | 13.2% |
| CALL_PY_EXACT_ARGS RESUME | 2,519,363,023 | 1.7% | 14.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,357,936,263 | 1.6% | 16.4% |
| RESUME LOAD_FAST | 2,083,823,975 | 1.4% | 17.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,869,763,641 | 1.2% | 19.1% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,774,516,131 | 1.2% | 20.3% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 1,601,595,843 | 1.1% | 21.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,594,115,318 | 1.1% | 22.4% |
| LOAD_CONST COMPARE_OP_STR | 1,563,958,173 | 1.0% | 23.4% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,550,090,511 | 1.0% | 24.5% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 1,436,470,403 | 1.0% | 25.4% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,331,859,110 | 0.9% | 26.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,269,536,761 | 0.8% | 27.1% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,597,637 | 0.8% | 28.0% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,229,420,834 | 0.8% | 28.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,183,163,823 | 0.8% | 29.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,097,138,610 | 0.7% | 30.3% |
| LOAD_CONST LOAD_FAST | 1,064,332,829 | 0.7% | 31.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,062,250,970 | 0.7% | 31.7% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,415,480 | 0.7% | 32.4% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 980,839,800 | 0.7% | 33.1% |
| BINARY_SUBSCR STORE_FAST | 977,836,566 | 0.7% | 33.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 971,879,112 | 0.6% | 34.4% |
| NOP LOAD_FAST_LOAD_FAST | 960,587,189 | 0.6% | 35.0% |
| LOAD_FAST LOAD_FAST | 959,656,224 | 0.6% | 35.6% |
| JUMP_BACKWARD FOR_ITER_LIST | 923,140,895 | 0.6% | 36.2% |
| STORE_FAST JUMP_BACKWARD | 918,193,643 | 0.6% | 36.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 903,961,743 | 0.6% | 37.5% |
| BINARY_SUBSCR LOAD_FAST | 879,036,850 | 0.6% | 38.0% |
| POP_TOP LOAD_FAST | 848,228,339 | 0.6% | 38.6% |
| RESUME LOAD_GLOBAL_BUILTIN | 843,691,664 | 0.6% | 39.2% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 800,664,603 | 0.5% | 39.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 797,632,063 | 0.5% | 40.2% |
| LOAD_FAST RETURN_VALUE | 779,995,820 | 0.5% | 40.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 771,572,043 | 0.5% | 41.3% |
| LOAD_CONST LOAD_CONST | 743,934,866 | 0.5% | 41.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 737,198,857 | 0.5% | 42.3% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 735,198,209 | 0.5% | 42.8% |
| JUMP_BACKWARD NOP | 718,007,432 | 0.5% | 43.2% |
| LOAD_FAST TO_BOOL_BOOL | 715,232,148 | 0.5% | 43.7% |
| STORE_FAST STORE_FAST | 711,104,537 | 0.5% | 44.2% |
| LOAD_CONST COMPARE_OP_INT | 672,021,415 | 0.4% | 44.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 667,912,591 | 0.4% | 45.1% |
| POP_TOP JUMP_BACKWARD | 659,626,407 | 0.4% | 45.5% |
| STORE_FAST_STORE_FAST LOAD_FAST | 648,269,608 | 0.4% | 45.9% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 644,021,127 | 0.4% | 46.4% |
| RETURN_VALUE STORE_FAST | 624,117,738 | 0.4% | 46.8% |
| LOAD_FAST LOAD_ATTR | 592,374,702 | 0.4% | 47.2% |
| FOR_ITER_LIST STORE_FAST | 586,540,207 | 0.4% | 47.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 573,899,411 | 0.4% | 48.0% |
| RETURN_CONST POP_TOP | 571,911,375 | 0.4% | 48.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 542,590,473 | 0.4% | 48.7% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 539,794,839 | 0.4% | 49.1% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,141,500 | 0.4% | 49.4% |
| LOAD_DEREF LOAD_FAST | 534,377,152 | 0.4% | 49.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 518,799,525 | 0.3% | 50.1% |
| RETURN_VALUE RETURN_VALUE | 518,398,433 | 0.3% | 50.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 515,668,236 | 0.3% | 50.8% |
| LOAD_FAST CONTAINS_OP | 510,851,664 | 0.3% | 51.1% |
| LOAD_FAST STORE_ATTR_SLOT | 504,123,180 | 0.3% | 51.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 479,985,335 | 0.3% | 51.8% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,523,999 | 0.3% | 52.1% |
| RESUME POP_TOP | 471,991,894 | 0.3% | 52.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 465,331,339 | 0.3% | 52.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 458,639,967 | 0.3% | 53.1% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 458,555,833 | 0.3% | 53.4% |
| YIELD_VALUE INTERPRETER_EXIT | 451,445,431 | 0.3% | 53.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 449,240,923 | 0.3% | 54.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 445,042,537 | 0.3% | 54.3% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 443,991,262 | 0.3% | 54.5% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.8% |
| PUSH_NULL LOAD_FAST | 433,876,548 | 0.3% | 55.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 432,874,257 | 0.3% | 55.4% |
| JUMP_BACKWARD FOR_ITER_RANGE | 430,929,796 | 0.3% | 55.7% |
| LOAD_CONST STORE_FAST | 424,137,163 | 0.3% | 56.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 421,861,969 | 0.3% | 56.3% |
| BUILD_TUPLE RETURN_VALUE | 413,118,042 | 0.3% | 56.5% |
| RETURN_CONST INTERPRETER_EXIT | 410,565,032 | 0.3% | 56.8% |
| FOR_ITER_RANGE STORE_FAST | 400,009,571 | 0.3% | 57.1% |
| IS_OP POP_JUMP_IF_FALSE | 376,003,957 | 0.3% | 57.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 375,168,742 | 0.2% | 57.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 367,749,053 | 0.2% | 57.8% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 366,580,841 | 0.2% | 58.1% |
| NOP LOAD_FAST | 359,495,413 | 0.2% | 58.3% |
| LOAD_FAST BINARY_SUBSCR | 357,873,985 | 0.2% | 58.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 354,994,186 | 0.2% | 58.8% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 346,557,866 | 0.2% | 59.0% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,716,840 | 0.2% | 59.2% |
| STORE_FAST LOAD_DEREF | 341,250,670 | 0.2% | 59.5% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 338,970,289 | 0.2% | 59.7% |
| RESUME NOP | 338,451,614 | 0.2% | 59.9% |
| RESUME LOAD_GLOBAL_MODULE | 338,302,889 | 0.2% | 60.1% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 332,345,959 | 0.2% | 60.4% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 332,312,457 | 0.2% | 60.6% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 331,447,653 | 0.2% | 60.8% |
| RETURN_VALUE INTERPRETER_EXIT | 329,266,724 | 0.2% | 61.0% |


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
| RETURN_VALUE | 2,242,696 | 44.7% |
| LOAD_ATTR_INSTANCE_VALUE | 2,222,254 | 44.3% |
| LOAD_GLOBAL_MODULE | 207,985 | 4.1% |
| LOAD_FAST | 132,060 | 2.6% |
| LOAD_ATTR_WITH_HINT | 131,820 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,574,644 | 91.3% |
| STORE_FAST | 435,635 | 8.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 251,138,192 | 29.3% |
| LOAD_FAST | 185,748,189 | 21.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.4% |
| LOAD_FAST_LOAD_FAST | 47,840,601 | 5.6% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,904 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 168,441,863 | 19.6% |
| LOAD_FAST | 137,105,835 | 16.0% |
| LOAD_FAST_LOAD_FAST | 106,872,375 | 12.5% |
| LOAD_CONST | 91,370,851 | 10.7% |
| RETURN_VALUE | 69,616,894 | 8.1% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,109,360 | 72.7% |
| LOAD_FAST | 65,303,948 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,257,661 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,613,361 | 29.8% |
| STORE_FAST | 116,014,619 | 29.7% |
| LOAD_FAST | 59,774,863 | 15.3% |
| RETURN_VALUE | 31,351,200 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,774,516,131 | 79.7% |
| LOAD_FAST | 244,342,463 | 11.0% |
| LOAD_FAST_LOAD_FAST | 94,427,212 | 4.2% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,597,637 | 56.6% |
| LOAD_CONST | 132,359,094 | 5.9% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,093,626 | 4.3% |
| SWAP | 90,609,131 | 4.1% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,035,480 | 47.1% |
| BINARY_SLICE | 15,579,000 | 22.9% |
| LOAD_CONST | 13,077,720 | 19.2% |
| BUILD_STRING | 2,011,200 | 3.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,233,483 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,173,060 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.4% |
| BUILD_TUPLE | 15,457,800 | 22.7% |
| LOAD_CONST | 8,422,860 | 12.4% |
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
| LOAD_FAST_LOAD_FAST | 23,580 | 0.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,141,500 | 65.1% |
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
| BINARY_OP_ADD_INT | 96,093,626 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,231,000 | 19.2% |
| LOAD_FAST_LOAD_FAST | 44,912,992 | 16.9% |
| LOAD_FAST | 38,771,060 | 14.6% |
| BINARY_OP | 27,332,905 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,213,863 | 23.4% |
| LOAD_CONST | 61,632,593 | 23.1% |
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
| LOAD_FAST | 69,610,854 | 25.8% |
| LOAD_FAST_LOAD_FAST | 36,420,308 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 28,679,062 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,512,788 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.1% |
| SWAP | 55,832,917 | 20.7% |
| LOAD_FAST | 28,366,709 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 366,580,841 | 73.2% |
| LOAD_FAST | 78,849,644 | 15.7% |
| LOAD_FAST_LOAD_FAST | 29,979,698 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 21,637,088 | 4.3% |
| CALL_NO_KW_LEN | 2,724,360 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,799,668 | 19.1% |
| CALL_PY_EXACT_ARGS | 94,404,100 | 18.9% |
| SWAP | 69,255,777 | 13.8% |
| RETURN_VALUE | 40,192,766 | 8.0% |
| BINARY_OP | 37,297,092 | 7.4% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 137,123,138 | 55.3% |
| BINARY_OP_ADD_INT | 40,079,604 | 16.1% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.1% |
| LOAD_FAST | 24,938,055 | 10.0% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 57,270,759 | 23.1% |
| GET_ITER | 33,199,240 | 13.4% |
| CALL_PY_EXACT_ARGS | 25,429,886 | 10.2% |
| BUILD_TUPLE | 24,334,503 | 9.8% |
| LOAD_DEREF | 18,985,680 | 7.6% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,436,470,403 | 61.1% |
| LOAD_FAST | 357,873,985 | 15.2% |
| LOAD_CONST | 139,734,023 | 5.9% |
| COPY | 109,829,640 | 4.7% |
| BUILD_SLICE | 104,833,980 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 977,836,566 | 41.6% |
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
| LOAD_CONST | 206,829,221 | 33.2% |
| LOAD_FAST | 206,722,666 | 33.1% |
| LOAD_FAST_LOAD_FAST | 135,458,441 | 21.7% |
| BINARY_SUBSCR | 41,253,848 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,034,055 | 38.0% |
| RETURN_VALUE | 105,304,598 | 16.9% |
| CONTAINS_OP | 77,768,700 | 12.5% |
| LOAD_FAST | 60,034,450 | 9.6% |
| LOAD_ATTR_METHOD_NO_DICT | 41,442,640 | 6.6% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 68,559,740 | 46.6% |
| LOAD_CONST | 41,616,840 | 28.3% |
| BUILD_TUPLE | 28,812,000 | 19.6% |
| LOAD_FAST | 3,537,986 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,060 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 146,157,106 | 99.4% |
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
| LOAD_FAST | 275,582,796 | 31.2% |
| LOAD_CONST | 180,981,248 | 20.5% |
| COPY | 157,633,500 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,633,815 | 17.5% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,560,121 | 27.0% |
| LOAD_CONST | 192,235,800 | 21.8% |
| LOAD_FAST | 141,519,799 | 16.1% |
| RETURN_VALUE | 90,407,083 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 148,328,046 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.1% |
| LOAD_FAST_LOAD_FAST | 329,529 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 2,540 | 0.0% |
| BINARY_SUBSCR | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,900 | 38.3% |
| LOAD_CONST | 24,656,020 | 13.1% |
| LOAD_FAST | 24,246,732 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.3% |
| STORE_FAST | 8,762,169 | 4.6% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,636,272 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,036,246 | 43.9% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 36.8% |
| STORE_FAST | 383,265 | 8.3% |
| RETURN_VALUE | 144,580 | 3.1% |
| CALL_NO_KW_LIST_APPEND | 132,780 | 2.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,266,943 | 38.7% |
| LOAD_ATTR_SLOT | 38,418,707 | 12.8% |
| SWAP | 32,167,608 | 10.7% |
| LOAD_FAST | 26,182,373 | 8.7% |
| RESUME | 18,139,926 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 128,923,296 | 42.9% |
| LOAD_FAST | 89,805,429 | 29.9% |
| SWAP | 32,205,128 | 10.7% |
| CALL | 9,652,840 | 3.2% |
| RETURN_VALUE | 9,313,348 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,290,268 | 16.1% |
| LOAD_FAST | 6,707,156 | 10.5% |
| RESUME | 6,634,996 | 10.4% |
| CALL_INTRINSIC_1 | 6,543,194 | 10.3% |
| SWAP | 6,077,760 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,055,852 | 37.7% |
| LOAD_FAST | 23,085,638 | 36.2% |
| SWAP | 6,077,760 | 9.5% |
| CALL_FUNCTION_EX | 3,410,155 | 5.3% |
| LOAD_CONST | 2,982,595 | 4.7% |


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
| LOAD_CONST | 157,375,216 | 99.5% |
| LOAD_FAST | 782,486 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,980 | 66.3% |
| DELETE_SUBSCR | 53,379,162 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 52,319,986 | 88.6% |
| LOAD_CONST | 6,748,500 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.1% |
| CALL | 12,297,008 | 20.8% |
| STORE_FAST | 4,751,135 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,518,120 | 29.8% |
| LOAD_CONST | 167,611,254 | 24.2% |
| LOAD_FAST_LOAD_FAST | 126,835,874 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 40,176,141 | 5.8% |
| CALL | 38,801,703 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 413,118,042 | 59.7% |
| LOAD_CONST | 82,974,810 | 12.0% |
| CALL_NO_KW_ISINSTANCE | 40,164,783 | 5.8% |
| STORE_FAST | 30,271,870 | 4.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 263,404,564 | 29.3% |
| KW_NAMES | 149,580,374 | 16.6% |
| LOAD_FAST_LOAD_FAST | 98,804,705 | 11.0% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,900 | 8.0% |
| LOAD_GLOBAL_MODULE | 49,101,150 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 311,416,297 | 34.6% |
| RESUME | 211,631,798 | 23.5% |
| RETURN_VALUE | 50,661,674 | 5.6% |
| POP_TOP | 47,025,029 | 5.2% |
| LOAD_GLOBAL_MODULE | 39,308,899 | 4.4% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,849,250 | 31.0% |
| LOAD_CONST | 23,536,881 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.3% |
| LOAD_FAST_LOAD_FAST | 21,190,121 | 15.3% |
| LOAD_ATTR_INSTANCE_VALUE | 6,372,622 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,530,999 | 78.5% |
| COPY_FREE_VARS | 26,910,225 | 19.5% |
| POP_TOP | 2,067,921 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,553 | 0.3% |
| MAKE_CELL | 172,456 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,401,126 | 28.8% |
| CALL_NO_KW_LEN | 23,161,323 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 10,774,711 | 8.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 9,082,112 | 7.2% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,552,947 | 50.3% |
| STORE_FAST | 13,561,399 | 10.7% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.1% |
| LOAD_FAST | 10,273,158 | 8.1% |
| CALL_BUILTIN_CLASS | 4,143,023 | 3.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,880 | 41.9% |
| KW_NAMES | 24,639,908 | 31.3% |
| LOAD_FAST | 13,403,329 | 17.0% |
| LOAD_FAST_LOAD_FAST | 2,769,768 | 3.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,137,420 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,880 | 39.7% |
| STORE_FAST | 27,921,232 | 35.4% |
| POP_TOP | 11,239,911 | 14.3% |
| RETURN_VALUE | 5,679,483 | 7.2% |
| BINARY_OP_ADD_INT | 938,417 | 1.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,177,966 | 52.0% |
| DICT_MERGE | 16,263,676 | 19.6% |
| LOAD_FAST | 10,487,222 | 12.6% |
| LOAD_FAST_LOAD_FAST | 5,883,880 | 7.1% |
| BUILD_MAP | 3,410,155 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,275,196 | 56.9% |
| STORE_FAST | 8,432,981 | 10.2% |
| RESUME | 7,506,215 | 9.0% |
| RETURN_VALUE | 6,880,623 | 8.3% |
| MAKE_CELL | 4,746,426 | 5.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 59.7% |
| LIST_EXTEND | 53,556,175 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.1% |
| RERAISE | 42,162 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 61.1% |
| CALL_FUNCTION_EX | 43,177,966 | 28.0% |
| BUILD_MAP | 6,543,194 | 4.2% |
| RERAISE | 6,380,977 | 4.1% |
| LOAD_CONST | 3,821,875 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,154,456 | 29.7% |
| LOAD_CONST | 8,598,493 | 27.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,512,538 | 24.4% |
| LOAD_ATTR_METHOD_NO_DICT | 4,178,954 | 13.6% |
| LOAD_FAST_LOAD_FAST | 920,818 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,805,623 | 48.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 22.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,435,680 | 7.9% |
| BINARY_OP | 2,010,960 | 6.5% |
| RETURN_VALUE | 1,419,280 | 4.6% |


</details>

### CALL_NO_KW_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_NO_KW_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 20,210,840 | 29.5% |
| LOAD_GLOBAL_MODULE | 9,322,362 | 13.6% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.1% |
| RETURN_CONST | 7,864,740 | 11.5% |
| BINARY_OP_ADD_FLOAT | 5,101,500 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,221,691 | 95.3% |
| LOAD_FAST | 1,660,840 | 2.4% |
| COPY_FREE_VARS | 1,528,936 | 2.2% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 32,220 | 0.0% |
| STORE_FAST | 13,960 | 0.0% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,160 | 46.5% |
| LOAD_CONST | 338,970,289 | 36.2% |
| LOAD_FAST_LOAD_FAST | 72,114,663 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 28,347,780 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,523,999 | 51.1% |
| STORE_FAST | 310,350,745 | 33.2% |
| POP_TOP | 47,792,332 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 22,203,127 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,794,839 | 68.7% |
| LOAD_CONST | 55,891,748 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,639,261 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,716,840 | 43.5% |
| LOAD_CONST | 171,777,468 | 21.9% |
| STORE_FAST | 166,547,779 | 21.2% |
| RETURN_VALUE | 29,452,501 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 346,557,866 | 42.6% |
| LOAD_GLOBAL_BUILTIN | 331,447,653 | 40.7% |
| LOAD_FAST_LOAD_FAST | 61,759,914 | 7.6% |
| BUILD_TUPLE | 40,164,783 | 4.9% |
| LOAD_ATTR_MODULE | 22,120,397 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 800,664,603 | 98.4% |
| COPY | 6,063,686 | 0.7% |
| RETURN_VALUE | 2,420,064 | 0.3% |
| POP_TOP | 1,996,800 | 0.2% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,952,774 | 61.9% |
| LOAD_ATTR_INSTANCE_VALUE | 55,131,473 | 16.0% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 8.6% |
| LOAD_DEREF | 20,449,960 | 5.9% |
| LOAD_ATTR_SLOT | 8,655,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 124,720,196 | 36.1% |
| LOAD_FAST | 55,709,786 | 16.1% |
| STORE_FAST | 44,149,848 | 12.8% |
| COMPARE_OP_INT | 32,615,527 | 9.4% |
| CALL_BUILTIN_CLASS | 23,161,323 | 6.7% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,300,232 | 72.8% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 18,544,706 | 7.7% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 5,805,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 90,734,387 | 37.9% |
| LOAD_FAST | 72,492,018 | 30.3% |
| EXTENDED_ARG | 27,822,060 | 11.6% |
| RETURN_CONST | 20,554,860 | 8.6% |
| LOAD_CONST | 11,304,042 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,415,417 | 44.9% |
| LOAD_CONST | 85,069,997 | 21.4% |
| LOAD_FAST_LOAD_FAST | 56,250,676 | 14.1% |
| LOAD_ATTR_METHOD_NO_DICT | 50,383,625 | 12.7% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 306,660,280 | 77.1% |
| LIST_APPEND | 28,917,240 | 7.3% |
| RETURN_VALUE | 11,991,496 | 3.0% |
| LOAD_FAST | 11,161,140 | 2.8% |
| POP_TOP | 8,709,827 | 2.2% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 150,891,418 | 64.7% |
| LOAD_ATTR | 72,924,570 | 31.3% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,449,293 | 3.2% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 302,686 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 73,501,978 | 31.5% |
| TO_BOOL_BOOL | 60,248,089 | 25.8% |
| GET_ITER | 33,735,960 | 14.5% |
| LOAD_GLOBAL_MODULE | 18,632,700 | 8.0% |
| LOAD_FAST | 12,533,275 | 5.4% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,405,593 | 76.9% |
| CALL | 19,599,448 | 8.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.0% |
| CALL_NO_KW_BUILTIN_FAST | 6,015,624 | 2.6% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 111,445,021 | 48.9% |
| BINARY_OP | 72,002,140 | 31.6% |
| RETURN_VALUE | 23,770,406 | 10.4% |
| STORE_FAST | 6,979,208 | 3.1% |
| LOAD_FAST | 5,874,060 | 2.6% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,382,186 | 91.3% |
| RETURN_VALUE | 1,727,780 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,230,543 | 3.3% |
| LOAD_ATTR | 101,640 | 0.3% |
| CALL_NO_KW_TUPLE_1 | 66,000 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.7% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 28.8% |
| STORE_FAST | 5,604,309 | 14.9% |
| RETURN_VALUE | 3,244,983 | 8.6% |
| BUILD_LIST | 1,966,480 | 5.2% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,920,806 | 66.7% |
| RETURN_GENERATOR | 5,526,160 | 24.7% |
| LOAD_ATTR_SLOT | 1,098,640 | 4.9% |
| CALL | 412,200 | 1.8% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,160 | 63.8% |
| BUILD_TUPLE | 2,891,800 | 12.9% |
| YIELD_VALUE | 2,419,200 | 10.8% |
| RETURN_VALUE | 1,005,326 | 4.5% |
| STORE_FAST | 617,820 | 2.8% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 332,312,457 | 98.9% |
| LOAD_CONST | 3,615,840 | 1.1% |
| BINARY_SUBSCR_TUPLE_INT | 66,000 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,418,540 | 85.5% |
| LOAD_GLOBAL_MODULE | 13,781,166 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 12,241,649 | 3.6% |
| CALL_PY_EXACT_ARGS | 8,101,881 | 2.4% |
| LOAD_FAST | 7,607,160 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 971,879,112 | 34.3% |
| LOAD_FAST_LOAD_FAST | 644,021,127 | 22.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 445,042,537 | 15.7% |
| LOAD_GLOBAL_MODULE | 166,093,792 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 111,415,682 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,519,363,023 | 88.9% |
| RETURN_GENERATOR | 140,433,925 | 5.0% |
| COPY_FREE_VARS | 125,515,383 | 4.4% |
| MAKE_CELL | 31,470,994 | 1.1% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,236,348 | 55.5% |
| LOAD_ATTR_METHOD_NO_DICT | 12,068,800 | 7.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,029,104 | 7.1% |
| LOAD_ATTR | 11,207,626 | 6.6% |
| LOAD_CONST | 8,896,371 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 164,081,357 | 96.6% |
| RETURN_GENERATOR | 3,377,638 | 2.0% |
| MAKE_CELL | 1,596,180 | 0.9% |
| COPY_FREE_VARS | 636,016 | 0.4% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 16,309,483 | 93.3% |
| LOAD_GLOBAL_MODULE | 690,042 | 3.9% |
| BUILD_TUPLE | 359,940 | 2.1% |
| LOAD_ATTR_MODULE | 112,788 | 0.6% |
| LOAD_GLOBAL | 32 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 17,472,291 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 444 | 52.5% |
| CALL_INTRINSIC_1 | 240 | 28.4% |
| JUMP_BACKWARD | 162 | 19.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,724,115 | 33.1% |
| LOAD_FAST_LOAD_FAST | 32,085,580 | 21.8% |
| LOAD_ATTR | 15,308,376 | 10.4% |
| LOAD_ATTR_SLOT | 13,761,151 | 9.4% |
| LOAD_FAST | 10,889,700 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80,281,160 | 54.6% |
| POP_JUMP_IF_TRUE | 38,840,701 | 26.4% |
| COPY | 18,631,626 | 12.7% |
| RETURN_VALUE | 7,092,499 | 4.8% |
| EXTENDED_ARG | 1,920,549 | 1.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 66,510,546 | 59.9% |
| BINARY_SUBSCR | 23,382,660 | 21.0% |
| LOAD_CONST | 6,328,960 | 5.7% |
| LOAD_FAST | 6,317,800 | 5.7% |
| LOAD_GLOBAL_MODULE | 3,631,972 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,510,726 | 43.7% |
| POP_JUMP_IF_TRUE | 32,446,020 | 29.2% |
| POP_JUMP_IF_FALSE | 30,132,213 | 27.1% |
| EXTENDED_ARG | 360 | 0.0% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 672,021,415 | 44.6% |
| LOAD_ATTR_INSTANCE_VALUE | 173,661,394 | 11.5% |
| LOAD_FAST | 121,616,382 | 8.1% |
| LOAD_FAST_LOAD_FAST | 120,050,326 | 8.0% |
| COPY | 109,003,081 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,269,536,761 | 84.3% |
| POP_JUMP_IF_TRUE | 122,045,023 | 8.1% |
| RETURN_VALUE | 59,382,120 | 3.9% |
| EXTENDED_ARG | 22,449,478 | 1.5% |
| LOAD_FAST | 15,024,000 | 1.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,563,958,173 | 98.3% |
| LOAD_FAST | 8,980,143 | 0.6% |
| LOAD_GLOBAL_MODULE | 4,925,480 | 0.3% |
| RETURN_VALUE | 4,023,960 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,550,090,511 | 97.5% |
| POP_JUMP_IF_TRUE | 27,393,285 | 1.7% |
| COPY | 6,088,977 | 0.4% |
| RETURN_VALUE | 4,402,754 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,415,480 | 49.9% |
| LOAD_FAST | 510,851,664 | 25.8% |
| LOAD_GLOBAL_MODULE | 301,875,173 | 15.2% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 43,889,656 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,869,763,641 | 94.3% |
| POP_JUMP_IF_TRUE | 60,477,324 | 3.1% |
| RETURN_VALUE | 25,865,640 | 1.3% |
| COPY | 21,273,123 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,368,506 | 48.6% |
| LOAD_FAST_LOAD_FAST | 36,024,720 | 34.7% |
| LOAD_ATTR | 11,580,663 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,736,285 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,862,827 | 25.0% |
| LOAD_FAST | 238,917,654 | 22.2% |
| LOAD_FAST_LOAD_FAST | 120,961,740 | 11.3% |
| SWAP | 112,622,356 | 10.5% |
| LOAD_CONST | 95,315,279 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,862,827 | 25.0% |
| TO_BOOL_BOOL | 234,252,478 | 21.8% |
| BINARY_SUBSCR_LIST_INT | 157,633,500 | 14.7% |
| BINARY_SUBSCR | 109,829,640 | 10.2% |
| COMPARE_OP_INT | 109,003,081 | 10.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 125,515,383 | 76.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,910,225 | 16.4% |
| CALL | 9,068,389 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,528,936 | 0.9% |
| CALL_PY_WITH_DEFAULTS | 636,016 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 179,035,398 | 70.9% |
| RETURN_GENERATOR | 73,606,383 | 29.1% |
| MAKE_CELL | 19,860 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,520,561 | 100.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,652,374 | 78.1% |
| NOP | 1,715,481 | 20.1% |
| RETURN_CONST | 150,539 | 1.8% |
| PUSH_EXC_INFO | 1,800 | 0.0% |
| LOAD_GLOBAL_MODULE | 600 | 0.0% |


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
| STORE_FAST | 223,782 | 35.4% |
| CALL | 158,302 | 25.1% |
| POP_TOP | 78,220 | 12.4% |
| NOP | 56,708 | 9.0% |
| STORE_ATTR_INSTANCE_VALUE | 56,576 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 215,902 | 34.2% |
| RERAISE | 151,242 | 24.0% |
| RETURN_CONST | 113,236 | 17.9% |
| JUMP_FORWARD | 66,240 | 10.5% |
| LOAD_FAST | 59,549 | 9.4% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,193,628 | 57.2% |
| BUILD_SLICE | 53,379,162 | 41.7% |
| LOAD_FAST | 1,014,791 | 0.8% |
| LOAD_CONST | 286,740 | 0.2% |
| LOAD_ATTR_SLOT | 66,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,533,978 | 84.1% |
| LOAD_CONST | 18,167,472 | 14.2% |
| JUMP_BACKWARD | 1,105,140 | 0.9% |
| RETURN_CONST | 540,861 | 0.4% |
| LOAD_FAST_LOAD_FAST | 274,696 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,474,444 | 95.1% |
| RETURN_VALUE | 376,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 217,267 | 1.3% |
| LOAD_DEREF | 114,253 | 0.7% |
| LOAD_GLOBAL_MODULE | 38,486 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,263,676 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 38,486 | 72.6% |
| LOAD_FAST | 13,140 | 24.8% |
| BUILD_MAP | 540 | 1.0% |
| RETURN_VALUE | 480 | 0.9% |
| MAP_ADD | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,026 | 73.6% |
| DICT_MERGE | 13,140 | 24.8% |
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
| RETURN_CONST | 56,700,607 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,101,180 | 33.7% |
| RETURN_CONST | 789,606 | 1.4% |
| LOAD_CONST | 5,940 | 0.0% |
| NOP | 4,740 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,458,119 | 51.7% |
| RETURN_VALUE | 69,227,597 | 35.6% |
| RETURN_CONST | 24,633,173 | 12.7% |
| JUMP_BACKWARD | 162 | 0.0% |
| SEND_GEN | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,100,550 | 48.9% |
| POP_TOP | 36,249,067 | 18.7% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,940 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 66,750,747 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,750,747 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 88,773,895 | 28.7% |
| LOAD_FAST | 42,655,580 | 13.8% |
| JUMP_BACKWARD | 41,157,663 | 13.3% |
| CALL_NO_KW_LIST_APPEND | 27,822,060 | 9.0% |
| COMPARE_OP_INT | 22,449,478 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 138,165,239 | 44.7% |
| JUMP_BACKWARD | 54,797,355 | 17.7% |
| FOR_ITER_LIST | 38,691,700 | 12.5% |
| POP_JUMP_IF_NONE | 36,519,160 | 11.8% |
| FOR_ITER | 16,516,646 | 5.3% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,736,285 | 88.4% |
| LOAD_FAST | 9,756,531 | 8.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,423,980 | 1.2% |
| RETURN_VALUE | 1,042,740 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,137,639 | 50.4% |
| BUILD_STRING | 52,319,986 | 44.6% |
| LOAD_FAST | 5,881,346 | 5.0% |
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
| JUMP_BACKWARD | 212,727,054 | 72.6% |
| GET_ITER | 53,886,819 | 18.4% |
| EXTENDED_ARG | 16,516,646 | 5.6% |
| SWAP | 6,716,266 | 2.3% |
| LOAD_FAST | 3,175,406 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 151,744,214 | 51.8% |
| STORE_FAST | 76,726,572 | 26.2% |
| LOAD_FAST | 19,228,535 | 6.6% |
| RETURN_CONST | 15,911,716 | 5.4% |
| PUSH_NULL | 7,956,120 | 2.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,712,840 | 63.0% |
| JUMP_BACKWARD | 32,872,709 | 36.5% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,240 | 0.0% |
| SWAP | 1,361 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,764,501 | 63.1% |
| RESUME | 33,185,495 | 36.9% |
| RETURN_CONST | 300 | 0.0% |
| STORE_FAST | 240 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 923,140,895 | 74.6% |
| GET_ITER | 190,057,315 | 15.4% |
| LOAD_FAST | 59,098,400 | 4.8% |
| EXTENDED_ARG | 38,691,700 | 3.1% |
| SWAP | 25,783,661 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 586,540,207 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,438,950 | 25.4% |
| RETURN_CONST | 103,915,976 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,273,880 | 6.5% |
| LOAD_FAST | 58,765,130 | 4.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 430,929,796 | 88.8% |
| GET_ITER | 27,287,781 | 5.6% |
| LOAD_FAST | 21,531,300 | 4.4% |
| SWAP | 4,261,440 | 0.9% |
| EXTENDED_ARG | 1,321,500 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 400,009,571 | 82.4% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.3% |
| RETURN_CONST | 24,279,086 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,351,396 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 292,049,931 | 69.1% |
| GET_ITER | 124,962,990 | 29.6% |
| SWAP | 2,996,680 | 0.7% |
| LOAD_FAST | 1,261,300 | 0.3% |
| FOR_ITER_LIST | 1,236,405 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 290,675,133 | 68.8% |
| LOAD_FAST | 61,888,972 | 14.6% |
| LOAD_FAST_LOAD_FAST | 43,821,240 | 10.4% |
| RETURN_CONST | 12,361,163 | 2.9% |
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
| RETURN_GENERATOR | 78,593,329 | 92.4% |
| LOAD_FAST | 3,323,640 | 3.9% |
| RETURN_VALUE | 2,597,801 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 489,660 | 0.6% |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,021,530 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,231,341 | 35.9% |
| LOAD_ATTR_INSTANCE_VALUE | 78,052,926 | 13.1% |
| CALL_BUILTIN_CLASS | 63,552,947 | 10.7% |
| RETURN_VALUE | 50,005,527 | 8.4% |
| LOAD_ATTR_SLOT | 38,736,093 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 190,057,315 | 32.0% |
| FOR_ITER_TUPLE | 124,962,990 | 21.1% |
| CALL_PY_EXACT_ARGS | 85,108,326 | 14.3% |
| FOR_ITER_GEN | 56,712,840 | 9.6% |
| FOR_ITER | 53,886,819 | 9.1% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 12,000,420 | 79.1% |
| RETURN_GENERATOR | 3,161,763 | 20.8% |
| LOAD_FAST | 7,080 | 0.0% |
| LOAD_ATTR_SLOT | 1,320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,170,583 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 1,536,181 | 77.3% |
| STORE_FAST | 451,140 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,987,201 | 100.0% |
| PUSH_EXC_INFO | 120 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,668,901 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,536,181 | 92.0% |
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
| YIELD_VALUE | 451,445,431 | 37.3% |
| RETURN_CONST | 410,565,032 | 33.9% |
| RETURN_VALUE | 329,266,724 | 27.2% |
| RETURN_GENERATOR | 18,176,281 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,239,322 | 48.7% |
| LOAD_FAST_LOAD_FAST | 111,749,741 | 25.1% |
| LOAD_GLOBAL_MODULE | 81,544,538 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 15,924,029 | 3.6% |
| LOAD_CONST | 8,677,355 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 376,003,957 | 84.6% |
| POP_JUMP_IF_TRUE | 39,093,207 | 8.8% |
| EXTENDED_ARG | 18,199,680 | 4.1% |
| RETURN_VALUE | 3,378,947 | 0.8% |
| COPY | 3,175,348 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,193,643 | 28.6% |
| POP_TOP | 659,626,407 | 20.5% |
| POP_JUMP_IF_TRUE | 465,331,339 | 14.5% |
| POP_JUMP_IF_FALSE | 443,991,262 | 13.8% |
| LIST_APPEND | 146,522,907 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 923,140,895 | 28.7% |
| NOP | 718,007,432 | 22.3% |
| FOR_ITER_RANGE | 430,929,796 | 13.4% |
| FOR_ITER_TUPLE | 292,049,931 | 9.1% |
| LOAD_FAST | 280,672,707 | 8.7% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,756,278 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,509,162 | 97.1% |
| SEND | 6,247,116 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 173,707,143 | 41.1% |
| POP_JUMP_IF_FALSE | 100,900,958 | 23.9% |
| POP_TOP | 57,643,469 | 13.6% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| EXTENDED_ARG | 14,628,778 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 167,828,536 | 39.7% |
| LOAD_FAST_LOAD_FAST | 82,128,227 | 19.4% |
| LOAD_CONST | 37,409,166 | 8.9% |
| LOAD_GLOBAL_MODULE | 28,033,017 | 6.6% |
| LOAD_GLOBAL_BUILTIN | 25,958,964 | 6.1% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 43,603,671 | 24.9% |
| LOAD_CONST | 38,153,120 | 21.8% |
| LOAD_FAST_LOAD_FAST | 35,439,129 | 20.2% |
| LOAD_GLOBAL_MODULE | 18,005,456 | 10.3% |
| LOAD_ATTR_INSTANCE_VALUE | 11,380,808 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 149,580,374 | 85.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,639,908 | 14.1% |
| CALL_BUILTIN_CLASS | 1,051,800 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,917,240 | 19.7% |
| BUILD_TUPLE | 26,458,320 | 18.0% |
| BINARY_OP | 20,606,280 | 14.1% |
| LOAD_FAST | 18,295,896 | 12.5% |
| RETURN_VALUE | 14,967,706 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,522,907 | 99.9% |
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
| LOAD_ATTR_SLOT | 38,220,227 | 70.5% |
| LOAD_FAST | 15,379,736 | 28.4% |
| LOAD_CONST | 366,720 | 0.7% |
| RETURN_VALUE | 119,883 | 0.2% |
| LOAD_DEREF | 77,527 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 53,556,175 | 98.8% |
| STORE_FAST | 343,255 | 0.6% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| LOAD_FAST | 130,990 | 0.2% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 592,374,702 | 55.3% |
| LOAD_GLOBAL_BUILTIN | 221,923,460 | 20.7% |
| LOAD_GLOBAL_MODULE | 95,491,754 | 8.9% |
| LOAD_ATTR_SLOT | 81,122,929 | 7.6% |
| LOAD_FAST_LOAD_FAST | 26,553,852 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220,463,067 | 20.6% |
| IS_OP | 216,239,322 | 20.2% |
| STORE_FAST | 169,714,931 | 15.8% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 72,924,570 | 6.8% |
| LOAD_FAST_LOAD_FAST | 60,585,768 | 5.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,559,385 | 96.3% |
| LOAD_GLOBAL_BUILTIN | 1,785,718 | 1.5% |
| LOAD_FAST | 1,408,580 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 551,272 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,815,698 | 49.4% |
| LOAD_FAST | 21,965,777 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,861,974 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,920 | 2.3% |
| LOAD_FAST_LOAD_FAST | 2,450,838 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,217,397,598 | 84.9% |
| LOAD_FAST_LOAD_FAST | 332,345,959 | 8.8% |
| COPY | 80,653,936 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,840,109 | 1.3% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,062,250,970 | 28.0% |
| TO_BOOL_BOOL | 432,874,257 | 11.4% |
| STORE_FAST | 287,051,359 | 7.6% |
| LOAD_ATTR_METHOD_NO_DICT | 188,473,158 | 5.0% |
| RETURN_VALUE | 181,199,044 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40,726,339 | 68.8% |
| LOAD_FAST | 18,487,996 | 31.2% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,525,527 | 66.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,449,293 | 12.6% |
| LOAD_GLOBAL_MODULE | 5,903,904 | 10.0% |
| LOAD_CONST | 4,892,760 | 8.3% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 771,572,043 | 57.7% |
| LOAD_ATTR_INSTANCE_VALUE | 188,473,158 | 14.1% |
| LOAD_CONST | 90,987,780 | 6.8% |
| LOAD_GLOBAL_MODULE | 52,878,159 | 4.0% |
| LOAD_ATTR_SLOT | 48,951,192 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 667,912,591 | 49.9% |
| LOAD_CONST | 155,782,794 | 11.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 150,891,418 | 11.3% |
| CALL_PY_EXACT_ARGS | 111,415,682 | 8.3% |
| LOAD_FAST_LOAD_FAST | 110,969,886 | 8.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,594,115,318 | 85.8% |
| LOAD_ATTR_INSTANCE_VALUE | 63,291,984 | 3.4% |
| LOAD_ATTR | 45,749,081 | 2.5% |
| LOAD_ATTR_SLOT | 45,654,356 | 2.5% |
| LOAD_ATTR_WITH_HINT | 37,390,219 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 797,632,063 | 42.9% |
| LOAD_FAST_LOAD_FAST | 479,985,335 | 25.8% |
| CALL_PY_EXACT_ARGS | 445,042,537 | 24.0% |
| LOAD_GLOBAL_MODULE | 56,026,979 | 3.0% |
| LOAD_CONST | 52,987,569 | 2.9% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 324,634,675 | 95.4% |
| LOAD_ATTR_MODULE | 11,618,955 | 3.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,324,680 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,760,953 | 33.4% |
| LOAD_FAST_LOAD_FAST | 101,064,184 | 29.7% |
| CALL | 27,282,239 | 8.0% |
| CALL_NO_KW_ISINSTANCE | 22,120,397 | 6.5% |
| LOAD_CONST | 15,863,922 | 4.7% |


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
| LOAD_FAST | 110,586,689 | 89.3% |
| LOAD_FAST_LOAD_FAST | 11,379,470 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 875,930 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 757,860 | 0.6% |
| STORE_FAST_LOAD_FAST | 181,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,394,000 | 23.7% |
| LOAD_FAST_LOAD_FAST | 27,613,680 | 22.3% |
| LOAD_GLOBAL_BUILTIN | 15,217,140 | 12.3% |
| LOAD_ATTR_METHOD_NO_DICT | 10,309,640 | 8.3% |
| BINARY_OP | 7,771,235 | 6.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,208,060 | 83.4% |
| LOAD_ATTR_SLOT | 5,106,861 | 10.6% |
| RETURN_VALUE | 1,326,772 | 2.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,064,920 | 2.2% |
| LOAD_FAST_LOAD_FAST | 125,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 42,574,379 | 88.3% |
| TO_BOOL_NONE | 3,107,760 | 6.4% |
| RETURN_VALUE | 832,759 | 1.7% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,420,834 | 91.4% |
| LOAD_ATTR_SLOT | 40,652,364 | 3.0% |
| COPY | 40,401,397 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,278,678 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,041,203 | 22.8% |
| TO_BOOL_NONE | 88,122,207 | 6.6% |
| LOAD_ATTR | 81,122,929 | 6.0% |
| TO_BOOL_BOOL | 68,883,596 | 5.1% |
| COMPARE_OP_FLOAT | 66,510,546 | 4.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 281,509,612 | 79.4% |
| LOAD_ATTR_INSTANCE_VALUE | 22,667,192 | 6.4% |
| LOAD_ATTR_WITH_HINT | 22,490,682 | 6.3% |
| COPY | 14,038,522 | 4.0% |
| LOAD_FAST_LOAD_FAST | 8,682,439 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,593,482 | 24.2% |
| STORE_FAST | 43,356,660 | 12.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 37,390,219 | 10.6% |
| COMPARE_OP_INT | 35,281,432 | 10.0% |
| LOAD_CONST | 29,603,000 | 8.4% |


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
| LOAD_FAST | 5,020,529,246 | 52.3% |
| LOAD_CONST | 743,934,866 | 7.7% |
| LOAD_FAST_LOAD_FAST | 458,555,833 | 4.8% |
| STORE_FAST | 293,956,425 | 3.1% |
| POP_JUMP_IF_FALSE | 277,083,103 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,774,516,131 | 18.5% |
| COMPARE_OP_STR | 1,563,958,173 | 16.3% |
| LOAD_FAST | 1,064,332,829 | 11.1% |
| LOAD_CONST | 743,934,866 | 7.7% |
| COMPARE_OP_INT | 672,021,415 | 7.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 341,250,670 | 40.4% |
| LOAD_GLOBAL_BUILTIN | 110,777,434 | 13.1% |
| PUSH_NULL | 38,338,089 | 4.5% |
| POP_JUMP_IF_FALSE | 32,330,237 | 3.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 534,377,152 | 63.3% |
| LOAD_CONST | 69,824,360 | 8.3% |
| LOAD_FAST_LOAD_FAST | 29,855,169 | 3.5% |
| LOAD_DEREF | 24,569,145 | 2.9% |
| CALL_NO_KW_LEN | 20,449,960 | 2.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,451,014,170 | 15.9% |
| POP_JUMP_IF_FALSE | 4,444,069,568 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 2,667,669,417 | 9.5% |
| RESUME | 2,083,823,975 | 7.4% |
| LOAD_CONST | 1,064,332,829 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,020,529,246 | 17.9% |
| LOAD_ATTR_INSTANCE_VALUE | 3,217,397,598 | 11.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,594,115,318 | 5.7% |
| LOAD_ATTR_SLOT | 1,229,420,834 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,097,138,610 | 3.9% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 39,759,468 | 76.4% |
| LOAD_FAST_AND_CLEAR | 12,287,412 | 23.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 39,751,308 | 76.4% |
| LOAD_FAST_AND_CLEAR | 12,287,412 | 23.6% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,682,680 | 51.2% |
| POP_TOP | 2,034,391 | 28.3% |
| LOAD_GLOBAL_BUILTIN | 421,860 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 340,928 | 4.7% |
| STORE_FAST | 308,760 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 49.8% |
| POP_JUMP_IF_NOT_NONE | 1,511,040 | 21.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 408,000 | 5.7% |
| LOAD_FAST | 383,640 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 336,728 | 4.7% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,331,859,110 | 16.3% |
| POP_JUMP_IF_FALSE | 1,183,163,823 | 14.5% |
| NOP | 960,587,189 | 11.8% |
| LOAD_FAST_LOAD_FAST | 518,799,525 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 479,985,335 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,436,470,403 | 17.6% |
| CONTAINS_OP | 989,415,480 | 12.1% |
| LOAD_FAST | 737,198,857 | 9.0% |
| CALL_PY_EXACT_ARGS | 644,021,127 | 7.9% |
| LOAD_FAST_LOAD_FAST | 518,799,525 | 6.4% |


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
| STORE_FAST | 20,041 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 8,274 | 0.1% |
| NOP | 4,597 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,695 | 98.9% |
| LOAD_GLOBAL_MODULE | 41,839 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 16,407 | 0.2% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,618 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,097,138,610 | 26.5% |
| POP_JUMP_IF_FALSE | 980,839,800 | 23.7% |
| RESUME | 843,691,664 | 20.4% |
| STORE_FAST | 542,590,473 | 13.1% |
| POP_JUMP_IF_TRUE | 102,097,806 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,667,669,417 | 64.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.5% |
| CALL_NO_KW_ISINSTANCE | 331,447,653 | 8.0% |
| LOAD_ATTR | 221,923,460 | 5.4% |
| LOAD_FAST_LOAD_FAST | 113,572,040 | 2.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 903,961,743 | 31.3% |
| STORE_FAST | 421,861,969 | 14.6% |
| RESUME | 338,302,889 | 11.7% |
| POP_JUMP_IF_FALSE | 279,569,113 | 9.7% |
| LOAD_FAST_LOAD_FAST | 125,777,905 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 458,639,967 | 15.9% |
| LOAD_FAST | 449,240,923 | 15.6% |
| CALL_NO_KW_ISINSTANCE | 346,557,866 | 12.0% |
| LOAD_ATTR_MODULE | 324,634,675 | 11.2% |
| CONTAINS_OP | 301,875,173 | 10.5% |


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
| LOAD_FAST | 2,272,520 | 100.0% |
| EXTENDED_ARG | 120 | 0.0% |
| LOAD_SUPER_ATTR | 120 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_DEREF | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,192,460 | 96.5% |
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
| LOAD_FAST | 117,705,808 | 100.0% |
| LOAD_DEREF | 9,080 | 0.0% |
| LOAD_SUPER_ATTR | 1,420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 66,217,657 | 56.3% |
| LOAD_FAST | 37,261,946 | 31.7% |
| CALL_PY_EXACT_ARGS | 6,234,663 | 5.3% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.1% |
| CALL | 1,200,040 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,504,357 | 53.6% |
| CALL_PY_EXACT_ARGS | 31,470,994 | 34.1% |
| CALL_FUNCTION_EX | 4,746,426 | 5.1% |
| CALL | 4,150,168 | 4.5% |
| CALL_PY_WITH_DEFAULTS | 1,596,180 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,504,357 | 53.4% |
| RESUME | 42,543,965 | 45.9% |
| RETURN_GENERATOR | 658,919 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,866,152 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 82,662,510 | 87.1% |
| LOAD_FAST | 8,772,360 | 9.2% |
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
| LOAD_FAST | 6,188,729 | 14.9% |
| JUMP_FORWARD | 4,782,840 | 11.6% |
| STORE_FAST | 4,549,800 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,597,580 | 49.8% |
| JUMP_BACKWARD | 19,591,438 | 47.3% |
| CALL_FUNCTION_EX | 1,211,460 | 2.9% |
| DICT_UPDATE | 180 | 0.0% |
| BUILD_MAP | 120 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 718,007,432 | 47.9% |
| RESUME | 338,451,614 | 22.6% |
| STORE_FAST | 157,789,728 | 10.5% |
| POP_JUMP_IF_FALSE | 81,516,620 | 5.4% |
| NOP | 52,977,800 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 960,587,189 | 64.1% |
| LOAD_FAST | 359,495,413 | 24.0% |
| NOP | 52,977,800 | 3.5% |
| PUSH_NULL | 43,592,731 | 2.9% |
| LOAD_GLOBAL_BUILTIN | 33,993,436 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,246,567 | 57.1% |
| STORE_SUBSCR_DICT | 3,085,665 | 17.2% |
| SWAP | 1,973,671 | 11.0% |
| COPY | 1,881,411 | 10.5% |
| STORE_FAST | 548,807 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,506,518 | 53.0% |
| RETURN_VALUE | 1,913,981 | 10.7% |
| RERAISE | 1,881,411 | 10.5% |
| JUMP_FORWARD | 1,715,820 | 9.6% |
| POP_TOP | 1,385,215 | 7.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,357,936,263 | 27.9% |
| CONTAINS_OP | 1,869,763,641 | 22.2% |
| COMPARE_OP_STR | 1,550,090,511 | 18.4% |
| COMPARE_OP_INT | 1,269,536,761 | 15.0% |
| IS_OP | 376,003,957 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,444,069,568 | 52.7% |
| LOAD_FAST_LOAD_FAST | 1,183,163,823 | 14.0% |
| LOAD_GLOBAL_BUILTIN | 980,839,800 | 11.6% |
| JUMP_BACKWARD | 443,991,262 | 5.3% |
| LOAD_GLOBAL_MODULE | 279,569,113 | 3.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 203,201,376 | 68.1% |
| EXTENDED_ARG | 36,519,160 | 12.2% |
| LOAD_ATTR_SLOT | 25,425,420 | 8.5% |
| LOAD_DEREF | 13,787,041 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,436,082 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 132,202,962 | 44.3% |
| PUSH_NULL | 53,765,229 | 18.0% |
| LOAD_DEREF | 28,714,940 | 9.6% |
| JUMP_BACKWARD | 26,808,523 | 9.0% |
| RETURN_CONST | 15,892,380 | 5.3% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 354,994,186 | 82.5% |
| LOAD_ATTR_INSTANCE_VALUE | 30,088,592 | 7.0% |
| LOAD_ATTR | 13,747,787 | 3.2% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.1% |
| EXTENDED_ARG | 7,255,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 156,997,744 | 36.5% |
| LOAD_GLOBAL_BUILTIN | 96,629,747 | 22.5% |
| LOAD_FAST_LOAD_FAST | 60,398,346 | 14.0% |
| LOAD_GLOBAL_MODULE | 36,040,381 | 8.4% |
| PUSH_NULL | 18,684,979 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 735,198,209 | 50.1% |
| TO_BOOL | 132,262,725 | 9.0% |
| COMPARE_OP_INT | 122,045,023 | 8.3% |
| TO_BOOL_ALWAYS_TRUE | 82,915,501 | 5.7% |
| TO_BOOL_NONE | 77,694,136 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 573,899,411 | 39.1% |
| JUMP_BACKWARD | 465,331,339 | 31.7% |
| LOAD_GLOBAL_BUILTIN | 102,097,806 | 7.0% |
| POP_TOP | 72,478,211 | 4.9% |
| LOAD_CONST | 68,438,532 | 4.7% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 571,911,375 | 25.2% |
| RESUME | 471,991,894 | 20.8% |
| CALL_NO_KW_BUILTIN_O | 341,716,840 | 15.1% |
| POP_JUMP_IF_FALSE | 168,207,608 | 7.4% |
| RETURN_VALUE | 123,272,583 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 848,228,339 | 36.0% |
| JUMP_BACKWARD | 659,626,407 | 28.0% |
| RESUME | 238,835,118 | 10.1% |
| RETURN_CONST | 183,809,735 | 7.8% |
| LOAD_FAST_LOAD_FAST | 99,494,350 | 4.2% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,517,314 | 30.9% |
| LOAD_ATTR | 3,246,420 | 18.2% |
| RAISE_VARARGS | 2,298,603 | 12.9% |
| CALL_NO_KW_BUILTIN_FAST | 1,785,321 | 10.0% |
| RERAISE | 1,711,947 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 16,306,370 | 90.9% |
| LOAD_GLOBAL_MODULE | 1,106,929 | 6.2% |
| LOAD_FAST | 387,187 | 2.2% |
| WITH_EXCEPT_START | 137,883 | 0.8% |
| LOAD_GLOBAL | 985 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 273,790,293 | 34.8% |
| POP_JUMP_IF_FALSE | 114,515,450 | 14.6% |
| POP_TOP | 70,761,353 | 9.0% |
| POP_JUMP_IF_NONE | 53,765,229 | 6.8% |
| NOP | 43,592,731 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 433,876,548 | 55.2% |
| LOAD_FAST_LOAD_FAST | 309,912,023 | 39.4% |
| LOAD_DEREF | 38,338,089 | 4.9% |
| LOAD_GLOBAL_BUILTIN | 3,416,040 | 0.4% |
| PUSH_NULL | 278,034 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,494,918 | 42.8% |
| LOAD_CONST | 622,432 | 17.8% |
| LOAD_ATTR_MODULE | 583,740 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 15.5% |
| LOAD_FAST | 151,182 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,298,603 | 65.8% |
| COPY | 1,041,772 | 29.8% |
| LOAD_CONST | 151,242 | 4.3% |
| CALL_INTRINSIC_1 | 18 | 0.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,380,977 | 70.2% |
| POP_EXCEPT | 1,881,411 | 20.7% |
| POP_TOP | 386,940 | 4.3% |
| POP_JUMP_IF_FALSE | 155,640 | 1.7% |
| DELETE_FAST | 151,242 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,711,947 | 66.2% |
| COPY | 830,992 | 32.1% |
| CALL_INTRINSIC_1 | 42,162 | 1.6% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,519,363,023 | 63.5% |
| POP_TOP | 238,835,118 | 6.0% |
| CALL | 211,631,798 | 5.3% |
| SEND_GEN | 208,509,111 | 5.3% |
| COPY_FREE_VARS | 179,035,398 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,083,823,975 | 41.8% |
| LOAD_GLOBAL_BUILTIN | 843,691,664 | 16.9% |
| POP_TOP | 471,991,894 | 9.5% |
| NOP | 338,451,614 | 6.8% |
| LOAD_GLOBAL_MODULE | 338,302,889 | 6.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 266,840,194 | 19.9% |
| STORE_ATTR_SLOT | 246,999,377 | 18.4% |
| POP_TOP | 183,809,735 | 13.7% |
| STORE_ATTR_INSTANCE_VALUE | 177,726,540 | 13.2% |
| RESUME | 122,771,703 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 571,911,375 | 42.6% |
| INTERPRETER_EXIT | 410,565,032 | 30.6% |
| EXIT_INIT_CHECK | 66,750,747 | 5.0% |
| TO_BOOL_BOOL | 56,781,618 | 4.2% |
| END_FOR | 56,700,607 | 4.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,433,925 | 63.6% |
| COPY_FREE_VARS | 73,606,383 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,377,638 | 1.5% |
| CALL_FUNCTION_EX | 1,715,721 | 0.8% |
| CALL | 874,838 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,593,329 | 32.9% |
| GET_ITER | 37,670,523 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,880 | 13.8% |
| STORE_FAST | 19,530,360 | 8.2% |
| INTERPRETER_EXIT | 18,176,281 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 779,995,820 | 25.9% |
| RETURN_VALUE | 518,398,433 | 17.2% |
| BUILD_TUPLE | 413,118,042 | 13.7% |
| LOAD_ATTR_INSTANCE_VALUE | 181,199,044 | 6.0% |
| BINARY_SUBSCR_DICT | 105,304,598 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 624,117,738 | 20.8% |
| RETURN_VALUE | 518,398,433 | 17.2% |
| INTERPRETER_EXIT | 329,266,724 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 264,502,327 | 8.8% |
| TO_BOOL_BOOL | 261,652,347 | 8.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,459,190 | 94.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,247,116 | 5.5% |
| SEND | 28,886 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,458,119 | 89.1% |
| YIELD_VALUE | 6,247,569 | 5.5% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,886 | 0.0% |
| SEND_GEN | 609 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,509,162 | 69.0% |
| LOAD_CONST | 93,869,683 | 31.0% |
| SEND | 609 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,509,111 | 69.0% |
| POP_TOP | 93,870,163 | 31.0% |
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
| MAKE_FUNCTION | 82,662,510 | 98.7% |
| SET_FUNCTION_ATTRIBUTE | 1,117,429 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,220,380 | 64.7% |
| LOAD_GLOBAL_BUILTIN | 18,989,340 | 22.7% |
| STORE_FAST | 5,807,345 | 6.9% |
| CALL_PY_EXACT_ARGS | 2,064,506 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 1,117,429 | 1.3% |


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
| LOAD_FAST | 31,579,016 | 59.0% |
| LOAD_FAST_LOAD_FAST | 15,242,960 | 28.5% |
| CALL | 5,419,260 | 10.1% |
| SWAP | 946,687 | 1.8% |
| LOAD_GLOBAL_MODULE | 199,140 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,910,045 | 29.7% |
| LOAD_DEREF | 13,447,060 | 25.1% |
| RETURN_CONST | 8,606,112 | 16.1% |
| JUMP_BACKWARD | 5,554,200 | 10.4% |
| LOAD_FAST_LOAD_FAST | 4,742,404 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 375,168,742 | 45.0% |
| LOAD_FAST_LOAD_FAST | 302,921,011 | 36.3% |
| SWAP | 80,653,936 | 9.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.2% |
| RETURN_VALUE | 20,943,360 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 310,783,085 | 37.3% |
| RETURN_CONST | 177,726,540 | 21.3% |
| LOAD_FAST_LOAD_FAST | 167,843,586 | 20.1% |
| LOAD_CONST | 73,328,727 | 8.8% |
| NOP | 51,809,271 | 6.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 515,668,236 | 48.5% |
| LOAD_FAST | 504,123,180 | 47.4% |
| SWAP | 40,401,397 | 3.8% |
| STORE_ATTR_SLOT | 2,128,296 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 279,567,515 | 26.3% |
| LOAD_FAST | 253,877,306 | 23.9% |
| RETURN_CONST | 246,999,377 | 23.2% |
| LOAD_CONST | 220,233,641 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 25,391,400 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,039,058 | 50.0% |
| SWAP | 14,038,522 | 26.0% |
| LOAD_FAST_LOAD_FAST | 12,444,198 | 23.0% |
| LOAD_DEREF | 242,500 | 0.4% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,963,215 | 62.8% |
| RETURN_CONST | 6,694,862 | 12.4% |
| JUMP_BACKWARD | 5,313,540 | 9.8% |
| LOAD_CONST | 3,924,023 | 7.3% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.3% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,874,000 | 40.9% |
| STORE_FAST | 19,047,660 | 29.0% |
| LOAD_CONST | 6,840,424 | 10.4% |
| LOAD_FAST | 2,917,140 | 4.4% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,460 | 28.9% |
| LOAD_DEREF | 13,770,848 | 20.9% |
| LOAD_FAST_LOAD_FAST | 13,437,000 | 20.4% |
| LOAD_FAST | 9,634,592 | 14.6% |
| LOAD_CONST | 4,839,627 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,597,637 | 12.8% |
| BINARY_SUBSCR | 977,836,566 | 9.9% |
| STORE_FAST | 711,104,537 | 7.2% |
| RETURN_VALUE | 624,117,738 | 6.3% |
| FOR_ITER_LIST | 586,540,207 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,451,014,170 | 45.1% |
| LOAD_FAST_LOAD_FAST | 1,331,859,110 | 13.5% |
| JUMP_BACKWARD | 918,193,643 | 9.3% |
| STORE_FAST | 711,104,537 | 7.2% |
| LOAD_GLOBAL_BUILTIN | 542,590,473 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,273,880 | 60.3% |
| FOR_ITER_RANGE | 35,405,280 | 26.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,140 | 6.9% |
| FOR_ITER_TUPLE | 5,123,040 | 3.8% |
| FOR_ITER | 2,930,226 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,780 | 22.2% |
| LOAD_FAST | 24,358,500 | 18.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,555,720 | 15.4% |
| STORE_ATTR_INSTANCE_VALUE | 9,297,440 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,601,595,843 | 63.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 367,749,053 | 14.6% |
| UNPACK_SEQUENCE_TUPLE | 238,856,387 | 9.5% |
| UNPACK_SEQUENCE_LIST | 232,509,000 | 9.2% |
| LOAD_ATTR_SLOT | 45,908,040 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,601,595,843 | 63.4% |
| LOAD_FAST | 648,269,608 | 25.7% |
| LOAD_FAST_LOAD_FAST | 86,315,745 | 3.4% |
| STORE_FAST | 75,454,304 | 3.0% |
| LOAD_GLOBAL_MODULE | 46,180,412 | 1.8% |


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
| LOAD_CONST | 13,497,206 | 11.5% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,616,686 | 91.5% |
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
| SWAP | 109,837,520 | 34.7% |
| LOAD_FAST | 64,774,566 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 17.9% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.1% |
| LOAD_CONST | 27,783,040 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.4% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 32.9% |
| RETURN_CONST | 33,884,106 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,003,020 | 8.5% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 95,460,729 | 48.1% |
| LOAD_FAST | 63,108,380 | 31.8% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.1% |
| RETURN_VALUE | 7,992,040 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,053,426 | 36.8% |
| LOAD_FAST | 65,621,546 | 33.1% |
| JUMP_BACKWARD | 31,629,149 | 15.9% |
| RETURN_CONST | 12,891,621 | 6.5% |
| LOAD_GLOBAL_MODULE | 7,342,449 | 3.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,500 | 52.2% |
| LOAD_FAST | 57,439,700 | 19.0% |
| LOAD_CONST | 26,913,446 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,052,170 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,905,360 | 38.0% |
| JUMP_BACKWARD | 110,631,650 | 36.6% |
| LOAD_FAST_LOAD_FAST | 71,543,200 | 23.7% |
| RETURN_CONST | 4,469,760 | 1.5% |
| LOAD_CONST | 231,120 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,862,827 | 28.8% |
| BINARY_OP_ADD_FLOAT | 116,613,361 | 12.5% |
| LOAD_FAST | 105,222,695 | 11.3% |
| BINARY_OP_ADD_INT | 90,609,131 | 9.7% |
| BINARY_OP_SUBTRACT_INT | 69,255,777 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,862,827 | 28.8% |
| STORE_SUBSCR_LIST_INT | 157,633,500 | 16.9% |
| COPY | 112,622,356 | 12.1% |
| STORE_SUBSCR | 109,837,520 | 11.8% |
| STORE_ATTR_INSTANCE_VALUE | 80,653,936 | 8.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,638,066 | 80.9% |
| LOAD_ATTR_INSTANCE_VALUE | 23,958,423 | 11.7% |
| LOAD_ATTR | 7,358,874 | 3.6% |
| LOAD_ATTR_SLOT | 3,352,621 | 1.6% |
| COPY | 2,335,675 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 132,262,725 | 64.6% |
| POP_JUMP_IF_FALSE | 71,851,107 | 35.1% |
| TO_BOOL | 235,794 | 0.1% |
| UNARY_NOT | 220,623 | 0.1% |
| TO_BOOL_NONE | 125,695 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,565,779 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,746,358 | 33.4% |
| LOAD_ATTR_SLOT | 17,761,080 | 9.9% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 7,172,753 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 94,344,484 | 52.7% |
| POP_JUMP_IF_TRUE | 82,915,501 | 46.3% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,849 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,498 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 800,664,603 | 24.7% |
| LOAD_FAST | 715,232,148 | 22.1% |
| CALL_NO_KW_BUILTIN_FAST | 477,523,999 | 14.8% |
| LOAD_ATTR_INSTANCE_VALUE | 432,874,257 | 13.4% |
| RETURN_VALUE | 261,652,347 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,357,936,263 | 72.9% |
| POP_JUMP_IF_TRUE | 735,198,209 | 22.7% |
| EXTENDED_ARG | 88,773,895 | 2.7% |
| UNARY_NOT | 53,837,107 | 1.7% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,501,669 | 77.0% |
| CALL_NO_KW_BUILTIN_O | 12,836,580 | 5.6% |
| BINARY_OP | 11,804,958 | 5.2% |
| COPY | 7,608,039 | 3.3% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,912,926 | 88.6% |
| POP_JUMP_IF_TRUE | 24,712,050 | 10.8% |
| UNARY_NOT | 1,035,600 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,690,229 | 66.8% |
| LOAD_ATTR_INSTANCE_VALUE | 27,758,488 | 24.8% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,712,180 | 1.5% |
| COPY | 814,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,668,518 | 55.2% |
| POP_JUMP_IF_FALSE | 46,538,046 | 41.6% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,760 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,519,734 | 45.0% |
| LOAD_ATTR_SLOT | 88,122,207 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 53,032,667 | 14.1% |
| LOAD_ATTR | 21,872,666 | 5.8% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 296,888,777 | 78.9% |
| POP_JUMP_IF_TRUE | 77,694,136 | 20.6% |
| EXTENDED_ARG | 967,320 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,933 | 0.2% |
| TO_BOOL | 123,662 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,966,080 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,407,740 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,340 | 5.8% |
| COPY | 2,682,160 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 36,172,763 | 53.8% |
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
| BINARY_OP | 10,158,042 | 83.7% |
| LOAD_ATTR_MODULE | 1,628,897 | 13.4% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 211,104 | 1.7% |
| LOAD_FAST | 122,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 12,130,343 | 100.0% |


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
| TO_BOOL_BOOL | 53,837,107 | 92.2% |
| TO_BOOL_LIST | 2,640,720 | 4.5% |
| TO_BOOL_INT | 1,035,600 | 1.8% |
| TO_BOOL_STR | 600,240 | 1.0% |
| TO_BOOL | 220,623 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 29,526,900 | 50.6% |
| RETURN_VALUE | 16,489,867 | 28.3% |
| KW_NAMES | 10,514,640 | 18.0% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.3% |
| LOAD_FAST | 555,240 | 1.0% |


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
| STORE_FAST_STORE_FAST | 134,286 | 62.0% |
| STORE_FAST | 79,687 | 36.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,724 | 0.8% |
| UNPACK_SEQUENCE | 460 | 0.2% |
| UNPACK_SEQUENCE_TUPLE | 440 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 196,721,940 | 82.5% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 10.1% |
| CALL | 10,636,560 | 4.5% |
| STORE_FAST | 6,001,740 | 2.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 799,600 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 232,509,000 | 97.5% |
| STORE_FAST | 6,004,980 | 2.5% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 264,502,327 | 50.3% |
| LOAD_FAST | 201,414,100 | 38.3% |
| BINARY_SUBSCR_DICT | 15,509,180 | 2.9% |
| STORE_FAST | 12,281,520 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 262,811,938 | 50.0% |
| STORE_FAST_STORE_FAST | 238,856,387 | 45.4% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 4.6% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,438,950 | 52.0% |
| FOR_ITER | 151,744,214 | 25.1% |
| RETURN_VALUE | 84,704,183 | 14.0% |
| LOAD_FAST | 35,337,180 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 367,749,053 | 60.8% |
| STORE_FAST | 215,215,625 | 35.6% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST_LOAD_FAST | 9,187,140 | 1.5% |
| LOAD_FAST | 905,820 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 137,883 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 137,083 | 99.4% |
| TO_BOOL_BOOL | 780 | 0.6% |
| TO_BOOL | 20 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.4% |
| YIELD_VALUE | 208,509,495 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,289 | 4.5% |
| LOAD_CONST | 26,892,673 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 451,445,431 | 65.1% |
| YIELD_VALUE | 208,509,495 | 30.1% |
| STORE_FAST | 24,509,580 | 3.5% |
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
| specialization.deferred |    204444977 | 4.6% |
| specialization.deopt |      1599012 | 0.0% |
|          hit |   4113108168 | 93.4% |
|         miss |     84779692 | 1.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,613,090 | 80.8% |
| Failure | 383,556 | 19.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.4% |
| other | 125,980 | 32.8% |
| tuple | 75,063 | 19.6% |
| dict | 16,834 | 4.4% |
| bytes | 10,746 | 2.8% |
| set | 7,180 | 1.9% |
| sequence | 6,041 | 1.6% |
| mapping | 4,592 | 1.2% |
| float | 980 | 0.3% |
| bytearray | 320 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2350938030 | 56.1% |
| specialization.deopt |        65120 | 0.0% |
|          hit |   1838905766 | 43.8% |
|         miss |      3452651 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 67,228 | 10.2% |
| Failure | 591,781 | 89.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 305,140 | 51.6% |
| array int | 112,980 | 19.1% |
| other | 77,500 | 13.1% |
| out of range | 40,460 | 6.8% |
| buffer int | 25,741 | 4.3% |
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
| specialization.deferred |    316111798 | 38.7% |
| specialization.deopt |           40 | 0.0% |
|          hit |    500691792 | 61.3% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,750 | 2.0% |
| Failure | 83,803 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.5% |
| dict subclass no override | 17,960 | 21.4% |
| py simple | 13,823 | 16.5% |
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
| specialization.deferred |       213973 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1367124443 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,284 | 99.1% |
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
| specialization.deferred |    293021120 | 11.6% |
| specialization.deopt |      2480425 | 0.1% |
|          hit |   2104443968 | 83.2% |
|         miss |    131463467 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,496 | 96.3% |
| Failure | 96,649 | 3.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,020 | 23.8% |
| dict items | 20,431 | 21.1% |
| seq iter | 15,120 | 15.6% |
| set | 13,195 | 13.7% |
| other | 7,660 | 7.9% |
| dict values | 3,820 | 4.0% |
| reversed list | 3,643 | 3.8% |
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
| specialization.deferred |     53478030 | 2.7% |
| specialization.deopt |      3603180 | 0.2% |
|          hit |   1760020480 | 87.8% |
|         miss |    190987021 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,625,573 | 98.9% |
| Failure | 38,720 | 1.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,260 | 44.6% |
| not in dict | 10,940 | 28.3% |
| overriding descriptor | 5,020 | 13.0% |
| property | 1,220 | 3.2% |
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
| specialization.deferred |   1069861302 | 10.2% |
| specialization.deopt |     10551806 | 0.1% |
|          hit |   8839476158 | 84.4% |
|         miss |    559403888 | 5.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,623,246 | 87.9% |
| Failure | 1,456,337 | 12.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 1,154,635 | 79.3% |
| metaclass attribute | 102,068 | 7.0% |
| method | 60,578 | 4.2% |
| not managed dict | 59,121 | 4.1% |
| shadowed | 40,355 | 2.8% |
| non object slot | 7,734 | 0.5% |
| class method obj | 7,260 | 0.5% |
| class attr descriptor | 6,280 | 0.4% |
| overridden | 5,780 | 0.4% |
| non overriding descriptor | 4,476 | 0.3% |
| mutable class | 2,863 | 0.2% |
| not in keys | 1,740 | 0.1% |
| class attr simple | 1,647 | 0.1% |
| module attr not found | 1,340 | 0.1% |
| builtin class method | 440 | 0.0% |
| property | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    147000115 | 4.4% |
| specialization.deopt |        25981 | 0.0% |
|          hit |   3206344375 | 95.6% |
|         miss |      1377808 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 29,996 | 21.0% |
| Failure | 112,883 | 79.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 50,187 | 44.5% |
| different types | 24,372 | 21.6% |
| baseobject | 13,269 | 11.8% |
| float long | 9,290 | 8.2% |
| set | 6,620 | 5.9% |
| other | 3,000 | 2.7% |
| bool | 2,365 | 2.1% |
| tuple | 1,680 | 1.5% |
| list | 1,020 | 0.9% |
| bytes | 640 | 0.6% |
| long float | 300 | 0.3% |
| string | 140 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322633 | 0.1% |
| specialization.deopt |          425 | 0.0% |
|          hit |   7026784995 | 99.9% |
|         miss |        23857 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 55,211 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    856168646 | 15.8% |
| specialization.deopt |       712840 | 0.0% |
|          hit |   4517944657 | 83.5% |
|         miss |     37782990 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,917 | 39.1% |
| Failure | 1,115,014 | 60.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,020 | 51.9% |
| multiply different types | 172,165 | 15.4% |
| add different types | 151,881 | 13.6% |
| floor divide | 32,820 | 2.9% |
| and int | 32,517 | 2.9% |
| remainder | 32,011 | 2.9% |
| add other | 29,440 | 2.6% |
| lshift | 18,760 | 1.7% |
| rshift | 16,642 | 1.5% |
| true divide different types | 14,861 | 1.3% |
| xor | 10,500 | 0.9% |
| true divide float | 6,779 | 0.6% |
| subtract other | 5,520 | 0.5% |
| or | 4,316 | 0.4% |
| power | 3,711 | 0.3% |
| multiply other | 1,940 | 0.2% |
| true divide other | 1,211 | 0.1% |
| and other | 860 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112705697 | 27.2% |
|          hit |    302379274 | 72.8% |
|         miss |          180 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 609 | 2.1% |
| Failure | 28,886 | 97.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 84.6% |
| other | 4,366 | 15.1% |
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
|          hit |    119989228 | 100.0% |

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
| specialization.deferred |    899987089 | 10.2% |
| specialization.deopt |      2800510 | 0.0% |
|          hit |   7807927378 | 88.2% |
|         miss |    148549330 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,847,475 | 87.8% |
| Failure | 396,397 | 12.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 66,306 | 16.7% |
| kwnames | 56,118 | 14.2% |
| code complex parameters | 54,138 | 13.7% |
| no dict | 51,380 | 13.0% |
| class no vectorcall | 29,952 | 7.6% |
| cfunc varargs keywords | 25,257 | 6.4% |
| meth descr varargs | 22,424 | 5.7% |
| cfunc noargs | 22,377 | 5.6% |
| other | 11,417 | 2.9% |
| init not python | 10,420 | 2.6% |
| meth descr varargs keywords | 8,739 | 2.2% |
| class mutable | 8,632 | 2.2% |
| init not simple | 8,400 | 2.1% |
| wrong number arguments | 4,420 | 1.1% |
| cfunc varargs | 3,629 | 0.9% |
| cmethod | 3,600 | 0.9% |
| bound method | 3,362 | 0.8% |
| method wrapper | 2,460 | 0.6% |
| operator wrapper | 2,366 | 0.6% |
| str | 1,000 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 95,681,716,310 | 63.7% |
| Not specialized | 11,055,704,944 | 7.4% |
| Specialized | 43,369,094,725 | 28.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,350,938,030 | 37.2% |
| LOAD_ATTR | 1,069,861,302 | 17.0% |
| CALL | 899,987,089 | 14.3% |
| BINARY_OP | 856,168,646 | 13.6% |
| STORE_SUBSCR | 316,111,798 | 5.0% |
| FOR_ITER | 293,021,120 | 4.6% |
| TO_BOOL | 204,444,977 | 3.2% |
| COMPARE_OP | 147,000,115 | 2.3% |
| SEND | 112,705,697 | 1.8% |
| STORE_ATTR | 53,478,030 | 0.8% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 231,303,504 | 19.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 168,432,875 | 14.5% |
| STORE_ATTR_SLOT | 112,793,299 | 9.7% |
| CALL_PY_EXACT_ARGS | 89,441,572 | 7.7% |
| STORE_ATTR_INSTANCE_VALUE | 75,036,268 | 6.5% |
| FOR_ITER_LIST | 65,826,856 | 5.7% |
| FOR_ITER_TUPLE | 65,585,191 | 5.7% |
| LOAD_ATTR_SLOT | 57,485,412 | 5.0% |
| LOAD_ATTR_METHOD_NO_DICT | 45,684,821 | 3.9% |
| TO_BOOL_NONE | 41,154,552 | 3.5% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,218,025,207 | 23.2% |
| Calls to Python functions inlined | 4,025,534,630 | 76.8% |
| Calls via PyEval_EvalFrame (total) | 1,218,025,207 | 23.2% |
| Calls via PyEval_EvalFrame (vector) | 678,315,053 | 12.9% |
| Calls via PyEval_EvalFrame (generator) | 539,710,154 | 10.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 678,309,953 | 12.9% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 191,536,550 | 3.7% |
| Calls via PyEval_EvalFrame (function ex) | 13,978,877 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 115,648,323 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 95,006,947 | 1.8% |
| Frames pushed | 4,378,271,211 | 83.5% |
| Frame objects created | 60,199,817 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,181,222,507 | 35.3% |
| Frees to freelist | 4,185,374,704 |  |
| Allocations | 7,661,700,350 | 64.7% |
| Allocations to 512 bytes | 7,580,037,929 | 64.0% |
| Allocations to 4 kbytes | 66,528,879 | 0.6% |
| Allocations over 4 kbytes | 15,133,542 | 0.1% |
| Frees | 7,903,840,661 |  |
| New values | 57,539,007 |  |
| Interpreter increfs | 56,701,303,138 | 76.5% |
| Interpreter decrefs | 65,787,486,661 | 77.1% |
| Increfs | 17,401,242,218 | 23.5% |
| Decrefs | 19,525,067,163 | 22.9% |
| Materialize dict (on request) | 3,685,803 | 6.4% |
| Materialize dict (new key) | 58,140 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,913,853,801 |  |
| Method cache misses | 72,872,515 |  |
| Method cache collisions | 77,956,045 |  |
| Method cache dunder hits | 2,209,207,334 |  |
| Method cache dunder misses | 5,123,384 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,285 |


</details>

---
Stats gathered on: 2023-07-07
