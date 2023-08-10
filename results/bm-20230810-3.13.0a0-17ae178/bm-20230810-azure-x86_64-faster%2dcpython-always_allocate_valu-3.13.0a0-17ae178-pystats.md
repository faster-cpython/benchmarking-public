
# Pystats results

- fork: faster-cpython
- ref: always-allocate-value-for-managed-dict-objects
- commit hash: 17ae178
- commit date: 2023-08-10T00:43:52+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 27,934,963,283 | 18.8% | 18.8% |  |
| STORE_FAST | 9,808,981,490 | 6.6% | 25.4% |  |
| LOAD_CONST | 9,572,189,729 | 6.4% | 31.9% |  |
| POP_JUMP_IF_FALSE | 8,398,455,007 | 5.7% | 37.5% |  |
| LOAD_FAST_LOAD_FAST | 7,999,949,651 | 5.4% | 42.9% |  |
| RESUME | 4,956,123,792 | 3.3% | 46.3% |  |
| LOAD_GLOBAL_BUILTIN | 4,127,779,890 | 2.8% | 49.0% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,724,244,030 | 2.5% | 51.6% | 5.2% |
| JUMP_BACKWARD | 3,205,766,425 | 2.2% | 53.7% |  |
| TO_BOOL_BOOL | 3,185,632,900 | 2.1% | 55.9% | 0.0% |
| RETURN_VALUE | 2,982,376,449 | 2.0% | 57.9% |  |
| LOAD_GLOBAL_MODULE | 2,868,642,816 | 1.9% | 59.8% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,802,731,270 | 1.9% | 61.7% | 3.1% |
| POP_TOP | 2,338,597,512 | 1.6% | 63.3% |  |
| BINARY_OP_ADD_INT | 2,222,565,576 | 1.5% | 64.8% | 0.0% |
| CONTAINS_OP | 1,982,991,799 | 1.3% | 66.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,862,978,697 | 1.3% | 67.4% | 8.2% |
| COMPARE_OP_STR | 1,590,662,181 | 1.1% | 68.4% | 0.0% |
| STORE_FAST_STORE_FAST | 1,542,738,194 | 1.0% | 69.5% |  |
| COMPARE_OP_INT | 1,502,262,821 | 1.0% | 70.5% | 0.1% |
| NOP | 1,497,305,156 | 1.0% | 71.5% |  |
| POP_JUMP_IF_TRUE | 1,456,976,293 | 1.0% | 72.5% |  |
| LOAD_ATTR_SLOT | 1,345,038,272 | 0.9% | 73.4% | 4.3% |
| RETURN_CONST | 1,340,146,690 | 0.9% | 74.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,334,032,548 | 0.9% | 75.2% | 3.4% |
| BINARY_SUBSCR_STR_INT | 1,239,946,580 | 0.8% | 76.0% | 0.0% |
| FOR_ITER_LIST | 1,239,582,123 | 0.8% | 76.8% | 5.3% |
| INTERPRETER_EXIT | 1,210,065,976 | 0.8% | 77.7% |  |
| BINARY_SUBSCR | 1,111,325,486 | 0.7% | 78.4% |  |
| PUSH_NULL | 1,081,961,485 | 0.7% | 79.1% |  |
| STORE_ATTR_SLOT | 1,062,944,653 | 0.7% | 79.9% | 10.6% |
| COPY | 1,056,439,509 | 0.7% | 80.6% |  |
| LOAD_ATTR | 1,037,513,962 | 0.7% | 81.3% |  |
| CALL_NO_KW_BUILTIN_FAST | 933,442,963 | 0.6% | 81.9% | 0.0% |
| SWAP | 931,285,931 | 0.6% | 82.5% |  |
| CALL | 894,309,573 | 0.6% | 83.1% |  |
| BINARY_SUBSCR_LIST_INT | 878,269,068 | 0.6% | 83.7% | 0.4% |
| BINARY_OP | 840,686,549 | 0.6% | 84.3% |  |
| LOAD_DEREF | 840,327,278 | 0.6% | 84.8% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,760,246 | 0.6% | 85.4% | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 811,407,106 | 0.5% | 86.0% | 8.6% |
| CALL_NO_KW_ISINSTANCE | 810,232,312 | 0.5% | 86.5% |  |
| CALL_NO_KW_BUILTIN_O | 785,535,358 | 0.5% | 87.0% | 0.1% |
| YIELD_VALUE | 693,473,159 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 692,908,805 | 0.5% | 88.0% |  |
| BINARY_SUBSCR_DICT | 622,354,501 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 605,529,017 | 0.4% | 88.8% |  |
| GET_ITER | 594,037,751 | 0.4% | 89.2% |  |
| BINARY_OP_SUBTRACT_INT | 499,709,571 | 0.3% | 89.5% | 0.1% |
| FOR_ITER_RANGE | 481,984,761 | 0.3% | 89.9% | 0.0% |
| IS_OP | 444,607,004 | 0.3% | 90.2% |  |
| UNPACK_SEQUENCE_TUPLE | 425,326,816 | 0.3% | 90.4% | 0.3% |
| FOR_ITER_TUPLE | 422,561,305 | 0.3% | 90.7% | 15.5% |
| POP_JUMP_IF_NOT_NONE | 419,759,540 | 0.3% | 91.0% |  |
| JUMP_FORWARD | 419,179,973 | 0.3% | 91.3% |  |
| BINARY_OP_ADD_FLOAT | 391,145,594 | 0.3% | 91.6% | 1.6% |
| TO_BOOL_NONE | 376,309,829 | 0.3% | 91.8% | 10.9% |
| LOAD_ATTR_WITH_HINT | 347,159,094 | 0.2% | 92.0% | 0.5% |
| CALL_NO_KW_LEN | 345,742,852 | 0.2% | 92.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 340,396,428 | 0.2% | 92.5% | 2.0% |
| LOAD_ATTR_MODULE | 339,700,249 | 0.2% | 92.7% | 0.0% |
| CALL_NO_KW_TYPE_1 | 335,973,007 | 0.2% | 93.0% |  |
| STORE_SUBSCR | 316,199,457 | 0.2% | 93.2% |  |
| EXTENDED_ARG | 308,253,416 | 0.2% | 93.4% |  |
| SEND_GEN | 302,362,248 | 0.2% | 93.6% | 0.0% |
| STORE_SUBSCR_LIST_INT | 301,629,698 | 0.2% | 93.8% | 0.0% |
| BUILD_LIST | 301,078,125 | 0.2% | 94.0% |  |
| FOR_ITER | 293,160,105 | 0.2% | 94.2% |  |
| POP_JUMP_IF_NONE | 290,276,039 | 0.2% | 94.4% |  |
| BINARY_OP_SUBTRACT_FLOAT | 270,377,454 | 0.2% | 94.6% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 266,391,882 | 0.2% | 94.7% | 3.2% |
| COPY_FREE_VARS | 249,318,395 | 0.2% | 94.9% |  |
| BINARY_SLICE | 248,172,044 | 0.2% | 95.1% |  |
| CALL_NO_KW_LIST_APPEND | 239,602,224 | 0.2% | 95.2% | 0.0% |
| RETURN_GENERATOR | 238,826,020 | 0.2% | 95.4% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 233,386,938 | 0.2% | 95.6% | 6.9% |
| TO_BOOL_INT | 228,237,265 | 0.2% | 95.7% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 228,047,855 | 0.2% | 95.9% | 0.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,744,561 | 0.1% | 96.0% |  |
| TO_BOOL | 204,963,711 | 0.1% | 96.1% |  |
| STORE_SUBSCR_DICT | 198,946,640 | 0.1% | 96.3% |  |
| END_SEND | 194,309,540 | 0.1% | 96.4% |  |
| BINARY_SUBSCR_TUPLE_INT | 188,460,501 | 0.1% | 96.5% | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 178,900,523 | 0.1% | 96.7% | 21.3% |
| KW_NAMES | 172,956,015 | 0.1% | 96.8% |  |
| CALL_PY_WITH_DEFAULTS | 171,234,689 | 0.1% | 96.9% | 3.1% |
| BUILD_SLICE | 158,211,677 | 0.1% | 97.0% |  |
| CALL_INTRINSIC_1 | 154,045,294 | 0.1% | 97.1% |  |
| LIST_APPEND | 146,902,535 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,425,604 | 0.1% | 97.3% | 0.0% |
| COMPARE_OP | 145,458,385 | 0.1% | 97.4% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 143,373,180 | 0.1% | 97.5% | 35.5% |
| UNPACK_SEQUENCE_LIST | 140,234,020 | 0.1% | 97.6% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,652,330 | 0.1% | 97.7% | 19.1% |
| STORE_FAST_LOAD_FAST | 136,652,507 | 0.1% | 97.8% |  |
| DELETE_SUBSCR | 127,970,639 | 0.1% | 97.9% |  |
| CALL_BUILTIN_CLASS | 126,618,606 | 0.1% | 97.9% |  |
| UNARY_NEGATIVE | 121,275,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 121,005,079 | 0.1% | 98.1% | 1.1% |
| STORE_SLICE | 117,671,608 | 0.1% | 98.2% |  |
| FORMAT_SIMPLE | 117,346,273 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 114,374,820 | 0.1% | 98.3% |  |
| SEND | 112,731,038 | 0.1% | 98.4% |  |
| TO_BOOL_LIST | 111,941,693 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 111,067,073 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,739,111 | 0.1% | 98.6% |  |
| GET_ANEXT | 100,136,760 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 94,843,674 | 0.1% | 98.8% |  |
| MAKE_CELL | 92,663,765 | 0.1% | 98.8% |  |
| FOR_ITER_GEN | 90,214,950 | 0.1% | 98.9% | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 87,703,795 | 0.1% | 99.0% | 2.0% |
| GET_AWAITABLE | 85,011,887 | 0.1% | 99.0% |  |
| SET_FUNCTION_ATTRIBUTE | 83,750,563 | 0.1% | 99.1% |  |
| CALL_FUNCTION_EX | 83,043,203 | 0.1% | 99.1% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,380,615 | 0.1% | 99.2% | 0.0% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,812,628 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 68,048,023 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 67,240,991 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 67,101,168 | 0.0% | 99.4% |  |
| STORE_DEREF | 65,762,684 | 0.0% | 99.4% |  |
| BUILD_MAP | 63,926,361 | 0.0% | 99.4% |  |
| BUILD_STRING | 59,066,945 | 0.0% | 99.5% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 56,935,268 | 0.0% | 99.5% | 0.0% |
| END_FOR | 56,701,040 | 0.0% | 99.6% |  |
| LIST_EXTEND | 54,338,148 | 0.0% | 99.6% |  |
| STORE_ATTR | 53,544,339 | 0.0% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 52,309,014 | 0.0% | 99.7% |  |
| UNARY_NOT | 50,996,655 | 0.0% | 99.7% |  |
| STORE_ATTR_WITH_HINT | 50,964,945 | 0.0% | 99.7% | 0.1% |
| LOAD_ATTR_PROPERTY | 48,569,647 | 0.0% | 99.8% | 11.3% |
| MAP_ADD | 41,400,812 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,651,362 | 0.0% | 99.8% |  |
| CALL_NO_KW_TUPLE_1 | 22,405,528 | 0.0% | 99.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 22,351,920 | 0.0% | 99.9% | 0.0% |
| PUSH_EXC_INFO | 17,045,685 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,045,677 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,578,152 | 0.0% | 99.9% |  |
| DICT_MERGE | 16,240,224 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,170,583 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,423,003 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,524,251 | 0.0% | 100.0% |  |
| RERAISE | 8,497,622 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,377,935 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 7,300,701 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,700 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,924,440 | 0.0% | 100.0% |  |
| BEFORE_WITH | 5,240,740 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 4,633,578 | 0.0% | 100.0% |  |
| SET_ADD | 3,234,120 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 2,897,242 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,298,840 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,989,914 | 0.0% | 100.0% |  |
| BUILD_SET | 1,918,508 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,671,494 | 0.0% | 100.0% |  |
| DELETE_FAST | 624,101 | 0.0% | 100.0% |  |
| UNPACK_EX | 286,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 216,643 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 138,122 | 0.0% | 100.0% |  |
| SET_UPDATE | 66,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 51,628 | 0.0% | 100.0% |  |
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
| CLEANUP_THROW | 810 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 4,901,789,892 | 3.3% | 3.3% |
| STORE_FAST LOAD_FAST | 4,674,942,499 | 3.1% | 6.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,511,943,295 | 3.0% | 9.5% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,157,431,269 | 2.1% | 11.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,662,318,497 | 1.8% | 13.4% |
| CALL_PY_EXACT_ARGS RESUME | 2,492,712,812 | 1.7% | 15.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,325,268,881 | 1.6% | 16.7% |
| RESUME LOAD_FAST | 2,091,089,259 | 1.4% | 18.1% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,870,207,968 | 1.3% | 19.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,771,634,353 | 1.2% | 20.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,577,858,370 | 1.1% | 21.6% |
| LOAD_CONST COMPARE_OP_STR | 1,563,963,726 | 1.1% | 22.6% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,550,229,127 | 1.0% | 23.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,332,276,589 | 0.9% | 24.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,265,605,196 | 0.9% | 25.4% |
| BINARY_OP_ADD_INT STORE_FAST | 1,258,764,033 | 0.8% | 26.3% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,230,830,657 | 0.8% | 27.1% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_STR_INT | 1,202,362,860 | 0.8% | 27.9% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,183,206,149 | 0.8% | 28.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,101,492,738 | 0.7% | 29.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,053,256,862 | 0.7% | 30.2% |
| LOAD_CONST LOAD_FAST | 1,052,729,818 | 0.7% | 30.9% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,415,960 | 0.7% | 31.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 982,241,381 | 0.7% | 32.2% |
| NOP LOAD_FAST_LOAD_FAST | 959,967,658 | 0.6% | 32.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 946,724,111 | 0.6% | 33.5% |
| JUMP_BACKWARD FOR_ITER_LIST | 924,164,281 | 0.6% | 34.1% |
| STORE_FAST JUMP_BACKWARD | 918,432,595 | 0.6% | 34.7% |
| POP_TOP LOAD_FAST | 902,821,941 | 0.6% | 35.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 888,217,750 | 0.6% | 35.9% |
| RESUME LOAD_GLOBAL_BUILTIN | 846,746,459 | 0.6% | 36.5% |
| BINARY_SUBSCR_STR_INT STORE_FAST | 841,517,940 | 0.6% | 37.1% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,163,843 | 0.5% | 37.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 803,890,334 | 0.5% | 38.2% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 797,091,394 | 0.5% | 38.7% |
| LOAD_FAST LOAD_FAST | 782,191,535 | 0.5% | 39.2% |
| LOAD_FAST RETURN_VALUE | 773,837,622 | 0.5% | 39.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 767,117,309 | 0.5% | 40.3% |
| LOAD_CONST LOAD_CONST | 744,385,935 | 0.5% | 40.8% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 725,084,520 | 0.5% | 41.3% |
| JUMP_BACKWARD NOP | 718,029,939 | 0.5% | 41.7% |
| LOAD_FAST TO_BOOL_BOOL | 715,261,639 | 0.5% | 42.2% |
| STORE_FAST STORE_FAST | 711,190,646 | 0.5% | 42.7% |
| LOAD_CONST COMPARE_OP_INT | 671,005,240 | 0.5% | 43.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 663,868,160 | 0.4% | 43.6% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 660,066,855 | 0.4% | 44.0% |
| POP_TOP JUMP_BACKWARD | 657,953,160 | 0.4% | 44.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 643,890,050 | 0.4% | 44.9% |
| LOAD_FAST PUSH_NULL | 630,231,274 | 0.4% | 45.3% |
| RETURN_VALUE STORE_FAST | 618,271,199 | 0.4% | 45.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 593,708,132 | 0.4% | 46.2% |
| FOR_ITER_LIST STORE_FAST | 587,131,335 | 0.4% | 46.6% |
| LOAD_FAST LOAD_ATTR | 578,754,836 | 0.4% | 47.0% |
| RETURN_CONST POP_TOP | 569,606,923 | 0.4% | 47.3% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 560,432,589 | 0.4% | 47.7% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,153,020 | 0.4% | 48.1% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 536,607,134 | 0.4% | 48.4% |
| PUSH_NULL LOAD_FAST | 535,068,566 | 0.4% | 48.8% |
| LOAD_DEREF LOAD_FAST | 519,755,636 | 0.4% | 49.1% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 515,591,935 | 0.3% | 49.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 512,666,048 | 0.3% | 49.8% |
| LOAD_FAST CONTAINS_OP | 510,851,781 | 0.3% | 50.2% |
| RETURN_VALUE RETURN_VALUE | 509,460,775 | 0.3% | 50.5% |
| LOAD_FAST STORE_ATTR_SLOT | 504,077,578 | 0.3% | 50.9% |
| BINARY_SUBSCR LOAD_FAST | 490,867,513 | 0.3% | 51.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 480,420,914 | 0.3% | 51.5% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,701,598 | 0.3% | 51.8% |
| RESUME POP_TOP | 472,275,107 | 0.3% | 52.2% |
| STORE_FAST_STORE_FAST LOAD_FAST | 465,938,218 | 0.3% | 52.5% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 465,303,685 | 0.3% | 52.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 459,616,968 | 0.3% | 53.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 452,200,588 | 0.3% | 53.4% |
| YIELD_VALUE INTERPRETER_EXIT | 451,460,649 | 0.3% | 53.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 450,389,754 | 0.3% | 54.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 444,393,844 | 0.3% | 54.3% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 54.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 430,701,561 | 0.3% | 54.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 428,229,904 | 0.3% | 55.2% |
| JUMP_BACKWARD FOR_ITER_RANGE | 428,129,786 | 0.3% | 55.5% |
| STORE_FAST LOAD_GLOBAL_MODULE | 420,470,264 | 0.3% | 55.8% |
| LOAD_CONST STORE_FAST | 420,259,370 | 0.3% | 56.0% |
| BUILD_TUPLE RETURN_VALUE | 413,114,075 | 0.3% | 56.3% |
| RETURN_CONST INTERPRETER_EXIT | 410,743,440 | 0.3% | 56.6% |
| NOP LOAD_FAST | 402,241,770 | 0.3% | 56.9% |
| FOR_ITER_RANGE STORE_FAST | 396,406,979 | 0.3% | 57.1% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 388,169,340 | 0.3% | 57.4% |
| IS_OP POP_JUMP_IF_FALSE | 376,290,211 | 0.3% | 57.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 368,128,708 | 0.2% | 57.9% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 365,584,544 | 0.2% | 58.1% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 361,598,116 | 0.2% | 58.4% |
| LOAD_FAST BINARY_SUBSCR | 352,865,838 | 0.2% | 58.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 346,426,284 | 0.2% | 58.9% |
| STORE_FAST LOAD_DEREF | 345,216,825 | 0.2% | 59.1% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 342,580,679 | 0.2% | 59.3% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,716,865 | 0.2% | 59.5% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 339,146,649 | 0.2% | 59.8% |
| RESUME NOP | 337,443,652 | 0.2% | 60.0% |
| RESUME LOAD_GLOBAL_MODULE | 336,737,488 | 0.2% | 60.2% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 332,271,467 | 0.2% | 60.5% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 331,866,824 | 0.2% | 60.7% |


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
| RETURN_VALUE | 2,417,404 | 46.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,273,569 | 43.4% |
| LOAD_GLOBAL_MODULE | 210,143 | 4.0% |
| LOAD_ATTR_WITH_HINT | 132,420 | 2.5% |
| LOAD_FAST | 132,060 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,628,670 | 88.3% |
| STORE_FAST | 610,630 | 11.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 247,644,258 | 29.5% |
| LOAD_FAST | 170,131,564 | 20.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.6% |
| LOAD_FAST_LOAD_FAST | 47,866,475 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,907 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 153,745,196 | 18.3% |
| LOAD_FAST | 138,604,937 | 16.5% |
| LOAD_FAST_LOAD_FAST | 106,872,553 | 12.7% |
| LOAD_CONST | 90,466,239 | 10.8% |
| RETURN_VALUE | 69,617,587 | 8.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,109,360 | 72.6% |
| LOAD_FAST | 65,389,650 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,256,980 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,612,680 | 29.8% |
| STORE_FAST | 116,100,216 | 29.7% |
| LOAD_FAST | 59,771,378 | 15.3% |
| RETURN_VALUE | 31,351,200 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,771,634,353 | 79.7% |
| LOAD_FAST | 244,362,998 | 11.0% |
| LOAD_FAST_LOAD_FAST | 94,801,717 | 4.3% |
| END_SEND | 29,134,080 | 1.3% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,258,764,033 | 56.6% |
| LOAD_CONST | 132,211,606 | 5.9% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,092,248 | 4.3% |
| SWAP | 88,107,432 | 4.0% |


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
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,233,483 | 1.8% |

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
| BINARY_OP_ADD_INT | 96,092,248 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,999 | 19.2% |
| LOAD_FAST_LOAD_FAST | 44,913,171 | 16.9% |
| LOAD_FAST | 38,771,060 | 14.6% |
| BINARY_OP | 27,332,901 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,212,483 | 23.4% |
| LOAD_CONST | 61,632,904 | 23.1% |
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
| LOAD_FAST | 69,610,886 | 25.7% |
| LOAD_FAST_LOAD_FAST | 36,420,281 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 28,678,362 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,599,749 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.1% |
| SWAP | 55,832,933 | 20.6% |
| LOAD_FAST | 28,366,001 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 365,584,544 | 73.2% |
| LOAD_FAST | 79,048,227 | 15.8% |
| LOAD_FAST_LOAD_FAST | 29,855,732 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 21,634,654 | 4.3% |
| CALL_NO_KW_LEN | 2,724,600 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,030,786 | 19.2% |
| CALL_PY_EXACT_ARGS | 94,404,100 | 18.9% |
| SWAP | 68,653,683 | 13.7% |
| RETURN_VALUE | 40,191,705 | 8.0% |
| BINARY_OP | 37,297,271 | 7.5% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 137,122,774 | 55.3% |
| BINARY_OP_ADD_INT | 40,078,035 | 16.1% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.1% |
| LOAD_FAST | 24,932,515 | 10.0% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 57,269,342 | 23.1% |
| GET_ITER | 33,199,240 | 13.4% |
| CALL_PY_EXACT_ARGS | 25,430,649 | 10.2% |
| BUILD_TUPLE | 24,334,503 | 9.8% |
| LOAD_DEREF | 18,985,680 | 7.7% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 352,865,838 | 31.8% |
| LOAD_FAST_LOAD_FAST | 234,131,543 | 21.1% |
| LOAD_CONST | 133,673,084 | 12.0% |
| COPY | 109,830,240 | 9.9% |
| BUILD_SLICE | 104,833,980 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 490,867,513 | 44.2% |
| STORE_FAST | 136,327,727 | 12.3% |
| LOAD_FAST_LOAD_FAST | 110,182,080 | 9.9% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 6.1% |
| BINARY_SUBSCR | 48,283,059 | 4.3% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,825,767 | 33.2% |
| LOAD_FAST | 205,176,522 | 33.0% |
| LOAD_FAST_LOAD_FAST | 135,588,357 | 21.8% |
| BINARY_SUBSCR | 41,253,854 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 237,018,999 | 38.1% |
| RETURN_VALUE | 104,204,105 | 16.7% |
| CONTAINS_OP | 77,768,700 | 12.5% |
| LOAD_FAST | 48,678,073 | 7.8% |
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
| LOAD_FAST | 3,530,824 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,060 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,517,344 | 99.4% |
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
| LOAD_FAST | 270,630,010 | 30.8% |
| LOAD_CONST | 180,973,080 | 20.6% |
| COPY | 157,633,500 | 17.9% |
| LOAD_FAST_LOAD_FAST | 154,810,690 | 17.6% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 233,335,132 | 26.6% |
| LOAD_CONST | 192,236,280 | 21.9% |
| LOAD_FAST | 140,365,324 | 16.0% |
| RETURN_VALUE | 90,407,114 | 10.3% |
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
| LOAD_CONST | 148,324,981 | 78.7% |
| LOAD_FAST | 39,803,100 | 21.1% |
| LOAD_FAST_LOAD_FAST | 329,556 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 2,524 | 0.0% |
| BINARY_SUBSCR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,900 | 38.3% |
| LOAD_CONST | 24,654,420 | 13.1% |
| LOAD_FAST | 24,246,759 | 12.9% |
| YIELD_VALUE | 19,353,600 | 10.3% |
| STORE_FAST | 8,763,756 | 4.7% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,633,578 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,034,868 | 43.9% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 36.8% |
| STORE_FAST | 383,294 | 8.3% |
| RETURN_VALUE | 144,611 | 3.1% |
| CALL_NO_KW_LIST_APPEND | 132,780 | 2.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,263,188 | 38.6% |
| LOAD_ATTR_SLOT | 38,399,412 | 12.8% |
| SWAP | 32,342,195 | 10.7% |
| LOAD_FAST | 30,542,219 | 10.1% |
| RESUME | 18,138,788 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 129,091,835 | 42.9% |
| LOAD_FAST | 89,938,007 | 29.9% |
| SWAP | 32,378,343 | 10.8% |
| CALL | 9,652,840 | 3.2% |
| RETURN_VALUE | 9,311,968 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,290,241 | 16.1% |
| LOAD_FAST | 8,875,519 | 13.9% |
| RESUME | 6,803,665 | 10.6% |
| CALL_INTRINSIC_1 | 6,527,545 | 10.2% |
| SWAP | 6,077,760 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,050,388 | 37.6% |
| LOAD_FAST | 23,240,743 | 36.4% |
| SWAP | 6,077,760 | 9.5% |
| CALL_FUNCTION_EX | 3,408,069 | 5.3% |
| LOAD_CONST | 2,982,597 | 4.7% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| LOAD_CONST | 142,320 | 7.4% |
| LOAD_GLOBAL_MODULE | 142,208 | 7.4% |
| LOAD_ATTR | 66,000 | 3.4% |
| LOAD_FAST | 52,920 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,514,100 | 78.9% |
| CONTAINS_OP | 141,848 | 7.4% |
| LOAD_CONST | 74,280 | 3.9% |
| BINARY_OP | 68,400 | 3.6% |
| STORE_FAST | 48,240 | 2.5% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,375,130 | 99.5% |
| LOAD_FAST | 781,107 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 104,833,980 | 66.3% |
| DELETE_SUBSCR | 53,377,697 | 33.7% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 52,319,130 | 88.6% |
| LOAD_CONST | 6,747,815 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.1% |
| CALL | 12,296,996 | 20.8% |
| STORE_FAST | 4,750,229 | 8.0% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,418,559 | 29.8% |
| LOAD_CONST | 167,605,120 | 24.2% |
| LOAD_FAST_LOAD_FAST | 127,393,455 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 40,167,860 | 5.8% |
| CALL | 38,800,762 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 413,114,075 | 59.6% |
| LOAD_CONST | 82,953,167 | 12.0% |
| CALL_NO_KW_ISINSTANCE | 40,156,528 | 5.8% |
| STORE_FAST | 30,270,466 | 4.4% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 241,647,020 | 27.0% |
| KW_NAMES | 149,664,334 | 16.7% |
| LOAD_FAST_LOAD_FAST | 91,129,450 | 10.2% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,900 | 8.1% |
| PUSH_NULL | 50,852,638 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 305,136,383 | 34.1% |
| RESUME | 211,834,796 | 23.7% |
| RETURN_VALUE | 51,129,748 | 5.7% |
| POP_TOP | 47,321,563 | 5.3% |
| LOAD_GLOBAL_MODULE | 39,308,375 | 4.4% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,743,225 | 36.6% |
| LOAD_CONST | 23,537,074 | 17.0% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.2% |
| PUSH_NULL | 11,687,194 | 8.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,373,612 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,992,402 | 78.6% |
| COPY_FREE_VARS | 26,910,060 | 19.4% |
| POP_TOP | 2,068,114 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,537 | 0.3% |
| MAKE_CELL | 172,417 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,147,604 | 28.5% |
| CALL_NO_KW_LEN | 23,248,348 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 10,773,662 | 8.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 9,079,990 | 7.2% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,635,883 | 50.3% |
| STORE_FAST | 13,560,272 | 10.7% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.1% |
| LOAD_FAST | 10,269,744 | 8.1% |
| CALL_BUILTIN_CLASS | 4,230,048 | 3.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,880 | 43.2% |
| KW_NAMES | 22,239,881 | 29.1% |
| LOAD_FAST | 12,867,355 | 16.8% |
| LOAD_FAST_LOAD_FAST | 3,303,806 | 4.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,137,420 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,880 | 41.0% |
| STORE_FAST | 27,918,244 | 36.6% |
| POP_TOP | 8,840,152 | 11.6% |
| RETURN_VALUE | 5,704,163 | 7.5% |
| BINARY_OP_ADD_INT | 933,742 | 1.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 43,155,436 | 52.0% |
| LOAD_FAST | 16,446,246 | 19.8% |
| DICT_MERGE | 16,240,224 | 19.6% |
| BUILD_MAP | 3,408,069 | 4.1% |
| STORE_FAST | 2,240,100 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,280,683 | 56.9% |
| STORE_FAST | 8,427,908 | 10.1% |
| RESUME | 7,489,740 | 9.0% |
| RETURN_VALUE | 6,927,578 | 8.3% |
| MAKE_CELL | 4,744,568 | 5.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 59.7% |
| LIST_EXTEND | 53,515,910 | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.1% |
| RERAISE | 42,150 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 61.1% |
| CALL_FUNCTION_EX | 43,155,436 | 28.0% |
| BUILD_MAP | 6,527,545 | 4.2% |
| RERAISE | 6,381,104 | 4.1% |
| LOAD_CONST | 3,819,789 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,944,175 | 72.9% |
| LOAD_FAST | 10,476,672 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,512,512 | 8.6% |
| LOAD_ATTR_METHOD_NO_DICT | 4,177,549 | 4.8% |
| LOAD_FAST_LOAD_FAST | 1,042,074 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 70,523,753 | 80.4% |
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
| LOAD_GLOBAL_MODULE | 9,496,295 | 13.8% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.0% |
| RETURN_CONST | 7,864,740 | 11.4% |
| BINARY_OP_ADD_FLOAT | 5,101,500 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 65,397,659 | 95.0% |
| COPY_FREE_VARS | 1,703,389 | 2.5% |
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
| LOAD_CONST | 339,146,649 | 36.3% |
| LOAD_FAST_LOAD_FAST | 72,133,608 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,386,154 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,701,598 | 51.2% |
| STORE_FAST | 310,643,063 | 33.3% |
| POP_TOP | 47,792,132 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 22,196,428 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560,432,589 | 71.3% |
| LOAD_CONST | 55,891,721 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| BINARY_OP_ADD_UNICODE | 15,909,600 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,716,865 | 43.5% |
| LOAD_CONST | 171,776,426 | 21.9% |
| STORE_FAST | 166,547,762 | 21.2% |
| RETURN_VALUE | 29,452,313 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,260 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 342,580,679 | 42.3% |
| LOAD_GLOBAL_BUILTIN | 331,866,824 | 41.0% |
| LOAD_FAST_LOAD_FAST | 62,970,589 | 7.8% |
| BUILD_TUPLE | 40,156,528 | 5.0% |
| LOAD_ATTR_MODULE | 22,115,516 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 797,091,394 | 98.4% |
| COPY | 6,062,308 | 0.7% |
| RETURN_VALUE | 2,416,150 | 0.3% |
| POP_TOP | 1,996,800 | 0.2% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 217,351,123 | 62.9% |
| LOAD_ATTR_INSTANCE_VALUE | 55,066,118 | 15.9% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 8.5% |
| LOAD_DEREF | 20,449,960 | 5.9% |
| LOAD_ATTR_SLOT | 8,655,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,800,551 | 35.8% |
| LOAD_FAST | 55,703,458 | 16.1% |
| STORE_FAST | 43,150,837 | 12.5% |
| COMPARE_OP_INT | 32,614,063 | 9.4% |
| CALL_BUILTIN_CLASS | 23,248,348 | 6.7% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,300,377 | 72.7% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 18,543,328 | 7.7% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 5,805,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 90,819,901 | 37.9% |
| LOAD_FAST | 72,490,468 | 30.3% |
| EXTENDED_ARG | 27,822,060 | 11.6% |
| RETURN_CONST | 20,554,860 | 8.6% |
| LOAD_CONST | 11,304,030 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,355,014 | 52.4% |
| LOAD_FAST_LOAD_FAST | 56,756,530 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 50,383,654 | 14.8% |
| LOAD_CONST | 27,325,086 | 8.0% |
| LOAD_ATTR_SLOT | 8,567,760 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 249,369,279 | 73.3% |
| LIST_APPEND | 28,917,240 | 8.5% |
| RETURN_VALUE | 11,791,666 | 3.5% |
| LOAD_FAST | 10,857,720 | 3.2% |
| POP_TOP | 9,144,367 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 151,127,016 | 64.8% |
| LOAD_ATTR | 59,465,433 | 25.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,436,960 | 5.8% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,473,159 | 3.2% |
| LOAD_FAST | 1,577,820 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 73,506,706 | 31.5% |
| TO_BOOL_BOOL | 60,230,079 | 25.8% |
| GET_ITER | 33,735,960 | 14.5% |
| LOAD_GLOBAL_MODULE | 18,632,700 | 8.0% |
| LOAD_FAST | 12,556,678 | 5.4% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,473,650 | 76.9% |
| CALL | 19,599,263 | 8.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.0% |
| CALL_NO_KW_BUILTIN_FAST | 6,014,220 | 2.6% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 111,511,495 | 48.9% |
| BINARY_OP | 72,002,140 | 31.6% |
| RETURN_VALUE | 23,765,422 | 10.4% |
| STORE_FAST | 6,977,549 | 3.1% |
| LOAD_FAST | 5,876,700 | 2.6% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,382,666 | 91.3% |
| RETURN_VALUE | 1,727,780 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,230,543 | 3.3% |
| LOAD_ATTR | 98,270 | 0.3% |
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
| LOAD_FAST | 14,919,908 | 66.6% |
| RETURN_GENERATOR | 5,526,160 | 24.7% |
| LOAD_ATTR_SLOT | 1,098,620 | 4.9% |
| CALL | 436,440 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,640 | 63.8% |
| BUILD_TUPLE | 2,891,780 | 12.9% |
| YIELD_VALUE | 2,419,200 | 10.8% |
| RETURN_VALUE | 1,003,948 | 4.5% |
| STORE_FAST | 642,060 | 2.9% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 332,271,467 | 98.9% |
| LOAD_CONST | 3,615,840 | 1.1% |
| BINARY_SUBSCR_TUPLE_INT | 66,000 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,412,116 | 85.5% |
| LOAD_GLOBAL_MODULE | 13,779,788 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 12,241,636 | 3.6% |
| CALL_PY_EXACT_ARGS | 8,068,753 | 2.4% |
| LOAD_FAST | 5,614,860 | 1.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 946,724,111 | 33.8% |
| LOAD_FAST_LOAD_FAST | 660,066,855 | 23.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 430,701,561 | 15.4% |
| LOAD_GLOBAL_MODULE | 165,494,239 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 111,393,348 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,492,712,812 | 88.9% |
| RETURN_GENERATOR | 140,432,348 | 5.0% |
| COPY_FREE_VARS | 121,555,881 | 4.3% |
| MAKE_CELL | 31,462,235 | 1.1% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 55,240,496 | 32.3% |
| LOAD_FAST | 42,031,223 | 24.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,256,754 | 7.2% |
| LOAD_ATTR_METHOD_NO_DICT | 12,068,800 | 7.0% |
| LOAD_ATTR | 11,113,740 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 165,087,435 | 96.4% |
| RETURN_GENERATOR | 3,374,890 | 2.0% |
| MAKE_CELL | 1,593,597 | 0.9% |
| COPY_FREE_VARS | 1,072,027 | 0.6% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,418,411 | 93.0% |
| LOAD_GLOBAL_MODULE | 690,030 | 4.2% |
| BUILD_TUPLE | 359,940 | 2.2% |
| LOAD_ATTR_MODULE | 109,737 | 0.7% |
| LOAD_GLOBAL | 28 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,578,152 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 420 | 51.9% |
| CALL_INTRINSIC_1 | 240 | 29.6% |
| JUMP_BACKWARD | 150 | 18.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 46,413,977 | 31.9% |
| LOAD_FAST_LOAD_FAST | 32,739,520 | 22.5% |
| LOAD_ATTR | 15,308,324 | 10.5% |
| LOAD_ATTR_SLOT | 13,757,711 | 9.5% |
| LOAD_FAST | 10,889,700 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 78,624,808 | 54.1% |
| POP_JUMP_IF_TRUE | 38,840,673 | 26.7% |
| COPY | 18,630,248 | 12.8% |
| RETURN_VALUE | 7,090,345 | 4.9% |
| EXTENDED_ARG | 1,918,796 | 1.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 66,492,869 | 59.9% |
| BINARY_SUBSCR | 23,382,660 | 21.1% |
| LOAD_CONST | 6,328,698 | 5.7% |
| LOAD_FAST | 6,312,866 | 5.7% |
| LOAD_GLOBAL_MODULE | 3,631,896 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,493,049 | 43.7% |
| POP_JUMP_IF_TRUE | 32,446,020 | 29.2% |
| POP_JUMP_IF_FALSE | 30,127,244 | 27.1% |
| COMPARE_OP | 380 | 0.0% |
| EXTENDED_ARG | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 671,005,240 | 44.7% |
| LOAD_ATTR_INSTANCE_VALUE | 172,369,401 | 11.5% |
| LOAD_FAST | 121,639,319 | 8.1% |
| LOAD_FAST_LOAD_FAST | 120,555,628 | 8.0% |
| COPY | 109,002,212 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,265,605,196 | 84.2% |
| POP_JUMP_IF_TRUE | 122,126,481 | 8.1% |
| RETURN_VALUE | 59,381,537 | 4.0% |
| EXTENDED_ARG | 22,449,452 | 1.5% |
| LOAD_FAST | 15,024,000 | 1.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,563,963,726 | 98.3% |
| LOAD_FAST | 8,980,217 | 0.6% |
| LOAD_GLOBAL_MODULE | 5,061,522 | 0.3% |
| RETURN_VALUE | 4,023,960 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,470,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,550,229,127 | 97.5% |
| POP_JUMP_IF_TRUE | 27,393,490 | 1.7% |
| COPY | 6,090,357 | 0.4% |
| RETURN_VALUE | 4,403,307 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,415,960 | 49.9% |
| LOAD_FAST | 510,851,781 | 25.8% |
| LOAD_GLOBAL_MODULE | 301,873,792 | 15.2% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 44,342,780 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,870,207,968 | 94.3% |
| POP_JUMP_IF_TRUE | 60,455,952 | 3.0% |
| RETURN_VALUE | 25,865,640 | 1.3% |
| COPY | 21,273,123 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,393,226 | 83.3% |
| LOAD_ATTR | 11,580,663 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 1,385,580 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,739,111 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,859,840 | 25.4% |
| LOAD_FAST | 237,466,247 | 22.5% |
| LOAD_FAST_LOAD_FAST | 120,961,740 | 11.4% |
| SWAP | 112,622,324 | 10.7% |
| LOAD_CONST | 95,333,896 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 268,859,840 | 25.4% |
| TO_BOOL_BOOL | 215,369,765 | 20.4% |
| BINARY_SUBSCR_LIST_INT | 157,633,500 | 14.9% |
| BINARY_SUBSCR | 109,830,240 | 10.4% |
| COMPARE_OP_INT | 109,002,212 | 10.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 121,555,881 | 75.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,910,060 | 16.7% |
| CALL | 9,064,113 | 5.6% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,703,389 | 1.1% |
| CALL_PY_WITH_DEFAULTS | 1,072,027 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 175,692,725 | 70.5% |
| RETURN_GENERATOR | 73,605,810 | 29.5% |
| MAKE_CELL | 19,860 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,524,011 | 100.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,654,674 | 78.1% |
| NOP | 1,715,434 | 20.1% |
| RETURN_CONST | 151,257 | 1.8% |
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
| STORE_FAST | 223,770 | 35.9% |
| CALL | 155,548 | 24.9% |
| POP_TOP | 77,927 | 12.5% |
| NOP | 55,318 | 8.9% |
| STORE_ATTR_INSTANCE_VALUE | 55,200 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 213,148 | 34.2% |
| RERAISE | 151,230 | 24.2% |
| RETURN_CONST | 110,456 | 17.7% |
| JUMP_FORWARD | 66,240 | 10.6% |
| LOAD_FAST | 57,879 | 9.3% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,193,370 | 57.2% |
| BUILD_SLICE | 53,377,697 | 41.7% |
| LOAD_FAST | 1,016,109 | 0.8% |
| LOAD_CONST | 286,740 | 0.2% |
| LOAD_ATTR_SLOT | 66,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,533,747 | 84.1% |
| LOAD_CONST | 18,169,149 | 14.2% |
| JUMP_BACKWARD | 1,105,140 | 0.9% |
| RETURN_CONST | 540,773 | 0.4% |
| LOAD_FAST_LOAD_FAST | 274,610 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,452,306 | 95.1% |
| RETURN_VALUE | 376,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 218,708 | 1.3% |
| LOAD_DEREF | 112,876 | 0.7% |
| LOAD_GLOBAL_MODULE | 37,108 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 16,240,224 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 37,108 | 71.9% |
| LOAD_FAST | 13,140 | 25.5% |
| BUILD_MAP | 540 | 1.0% |
| RETURN_VALUE | 480 | 0.9% |
| MAP_ADD | 180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,648 | 72.9% |
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
| RETURN_CONST | 56,701,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,102,080 | 33.7% |
| RETURN_CONST | 789,606 | 1.4% |
| LOAD_CONST | 5,940 | 0.0% |
| NOP | 4,980 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,455,363 | 51.7% |
| RETURN_VALUE | 69,222,093 | 35.6% |
| RETURN_CONST | 24,631,814 | 12.7% |
| JUMP_BACKWARD | 150 | 0.0% |
| SEND_GEN | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 95,093,659 | 48.9% |
| POP_TOP | 36,246,325 | 18.7% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,940 | 1.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 67,101,168 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,101,168 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 88,770,834 | 28.8% |
| LOAD_FAST | 42,654,620 | 13.8% |
| JUMP_BACKWARD | 40,665,603 | 13.2% |
| CALL_NO_KW_LIST_APPEND | 27,822,060 | 9.0% |
| COMPARE_OP_INT | 22,449,452 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 138,160,224 | 44.8% |
| JUMP_BACKWARD | 54,301,167 | 17.6% |
| FOR_ITER_LIST | 38,691,700 | 12.6% |
| POP_JUMP_IF_NONE | 36,519,160 | 11.8% |
| FOR_ITER | 16,516,646 | 5.4% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,739,111 | 88.4% |
| LOAD_FAST | 9,753,093 | 8.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,423,980 | 1.2% |
| RETURN_VALUE | 1,042,740 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,138,355 | 50.4% |
| BUILD_STRING | 52,319,130 | 44.6% |
| LOAD_FAST | 5,879,968 | 5.0% |
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
| JUMP_BACKWARD | 212,770,608 | 72.6% |
| GET_ITER | 53,884,172 | 18.4% |
| EXTENDED_ARG | 16,516,646 | 5.6% |
| SWAP | 6,717,706 | 2.3% |
| LOAD_FAST | 3,174,268 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 151,763,390 | 51.8% |
| STORE_FAST | 76,715,480 | 26.2% |
| LOAD_FAST | 27,183,274 | 9.3% |
| RETURN_CONST | 15,910,390 | 5.4% |
| SWAP | 6,179,340 | 2.1% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,713,320 | 62.9% |
| JUMP_BACKWARD | 33,136,690 | 36.7% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,240 | 0.0% |
| SWAP | 1,314 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,764,934 | 62.9% |
| RESUME | 33,449,476 | 37.1% |
| RETURN_CONST | 300 | 0.0% |
| STORE_FAST | 240 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 924,164,281 | 74.6% |
| GET_ITER | 190,427,961 | 15.4% |
| LOAD_FAST | 59,098,400 | 4.8% |
| EXTENDED_ARG | 38,691,700 | 3.1% |
| SWAP | 25,956,855 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 587,131,335 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,610,478 | 25.4% |
| RETURN_CONST | 103,914,037 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,533,080 | 6.5% |
| LOAD_FAST | 59,442,196 | 4.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 428,129,786 | 88.8% |
| GET_ITER | 27,231,755 | 5.6% |
| LOAD_FAST | 21,531,300 | 4.5% |
| SWAP | 4,261,440 | 0.9% |
| EXTENDED_ARG | 829,380 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 396,406,979 | 82.2% |
| STORE_FAST_LOAD_FAST | 35,717,280 | 7.4% |
| RETURN_CONST | 24,277,888 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,444,912 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 292,024,420 | 69.1% |
| GET_ITER | 124,940,827 | 29.6% |
| SWAP | 2,996,680 | 0.7% |
| LOAD_FAST | 1,261,210 | 0.3% |
| FOR_ITER_LIST | 1,236,365 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 288,887,181 | 68.4% |
| LOAD_FAST | 61,889,809 | 14.6% |
| LOAD_FAST_LOAD_FAST | 43,821,240 | 10.4% |
| RETURN_CONST | 12,361,426 | 2.9% |
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
| RETURN_GENERATOR | 78,586,454 | 92.4% |
| LOAD_FAST | 3,323,640 | 3.9% |
| RETURN_VALUE | 2,595,034 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 489,659 | 0.6% |
| BEFORE_ASYNC_WITH | 8,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,011,887 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 213,812,201 | 36.0% |
| LOAD_ATTR_INSTANCE_VALUE | 64,977,517 | 10.9% |
| CALL_BUILTIN_CLASS | 63,635,883 | 10.7% |
| RETURN_VALUE | 50,004,342 | 8.4% |
| LOAD_ATTR_SLOT | 38,736,006 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 190,427,961 | 32.1% |
| FOR_ITER_TUPLE | 124,940,827 | 21.0% |
| CALL_PY_EXACT_ARGS | 85,107,098 | 14.3% |
| FOR_ITER_GEN | 56,713,320 | 9.5% |
| FOR_ITER | 53,884,172 | 9.1% |


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
| IMPORT_NAME | 1,538,774 | 77.3% |
| STORE_FAST | 451,140 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,989,794 | 100.0% |
| PUSH_EXC_INFO | 120 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,671,494 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,538,774 | 92.1% |
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
| YIELD_VALUE | 451,460,649 | 37.3% |
| RETURN_CONST | 410,743,440 | 33.9% |
| RETURN_VALUE | 329,685,413 | 27.2% |
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
| LOAD_ATTR | 216,239,526 | 48.6% |
| LOAD_FAST_LOAD_FAST | 111,737,157 | 25.1% |
| LOAD_GLOBAL_MODULE | 81,817,729 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 15,924,216 | 3.6% |
| LOAD_CONST | 8,672,230 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 376,290,211 | 84.6% |
| POP_JUMP_IF_TRUE | 39,064,381 | 8.8% |
| EXTENDED_ARG | 18,199,680 | 4.1% |
| RETURN_VALUE | 3,377,572 | 0.8% |
| COPY | 3,175,231 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 918,432,595 | 28.6% |
| POP_TOP | 657,953,160 | 20.5% |
| POP_JUMP_IF_TRUE | 465,303,685 | 14.5% |
| POP_JUMP_IF_FALSE | 444,393,844 | 13.9% |
| LIST_APPEND | 146,794,709 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 924,164,281 | 28.8% |
| NOP | 718,029,939 | 22.4% |
| FOR_ITER_RANGE | 428,129,786 | 13.4% |
| LOAD_FAST | 308,047,521 | 9.6% |
| FOR_ITER_TUPLE | 292,024,420 | 9.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,744,561 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,498,831 | 97.1% |
| SEND | 6,245,730 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 171,854,381 | 41.0% |
| POP_JUMP_IF_FALSE | 100,899,492 | 24.1% |
| POP_TOP | 56,127,809 | 13.4% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| EXTENDED_ARG | 14,628,752 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,288,388 | 39.7% |
| LOAD_FAST_LOAD_FAST | 82,377,352 | 19.7% |
| LOAD_CONST | 37,405,312 | 8.9% |
| LOAD_GLOBAL_MODULE | 28,028,912 | 6.7% |
| LOAD_GLOBAL_BUILTIN | 25,953,147 | 6.2% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,539,168 | 24.0% |
| LOAD_CONST | 38,153,846 | 22.1% |
| LOAD_FAST_LOAD_FAST | 35,187,439 | 20.3% |
| LOAD_GLOBAL_MODULE | 18,005,402 | 10.4% |
| LOAD_ATTR_INSTANCE_VALUE | 11,379,658 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 149,664,334 | 86.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 22,239,881 | 12.9% |
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
| LOAD_FAST | 18,295,876 | 12.5% |
| RETURN_VALUE | 15,140,460 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,794,709 | 99.9% |
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
| LOAD_ATTR_SLOT | 38,200,932 | 70.3% |
| LOAD_FAST | 15,443,514 | 28.4% |
| LOAD_CONST | 366,720 | 0.7% |
| RETURN_VALUE | 206,908 | 0.4% |
| LOAD_DEREF | 77,528 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 53,515,910 | 98.5% |
| STORE_FAST | 427,524 | 0.8% |
| LOAD_FAST | 218,254 | 0.4% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.3% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 578,754,836 | 55.8% |
| LOAD_GLOBAL_BUILTIN | 221,917,316 | 21.4% |
| LOAD_GLOBAL_MODULE | 95,606,882 | 9.2% |
| LOAD_ATTR_SLOT | 81,103,622 | 7.8% |
| LOAD_FAST_LOAD_FAST | 23,057,353 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 216,239,526 | 20.8% |
| STORE_FAST | 169,609,710 | 16.3% |
| LOAD_FAST | 154,026,890 | 14.8% |
| PUSH_NULL | 69,681,293 | 6.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 59,465,433 | 5.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,575,879 | 96.3% |
| LOAD_GLOBAL_BUILTIN | 1,779,370 | 1.5% |
| LOAD_FAST | 1,408,580 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 544,370 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,811,564 | 49.4% |
| CALL_PY_EXACT_ARGS | 21,859,206 | 18.1% |
| LOAD_FAST | 14,220,659 | 11.8% |
| PUSH_NULL | 8,285,400 | 6.8% |
| CALL_BUILTIN_CLASS | 2,841,920 | 2.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,157,431,269 | 84.8% |
| LOAD_FAST_LOAD_FAST | 330,916,312 | 8.9% |
| COPY | 77,250,653 | 2.1% |
| LOAD_ATTR_INSTANCE_VALUE | 50,253,592 | 1.3% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,053,256,862 | 28.3% |
| TO_BOOL_BOOL | 428,229,904 | 11.5% |
| STORE_FAST | 276,443,467 | 7.4% |
| LOAD_ATTR_METHOD_NO_DICT | 190,003,151 | 5.1% |
| RETURN_VALUE | 176,982,760 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40,723,544 | 71.5% |
| LOAD_FAST | 16,211,284 | 28.5% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,575,038 | 69.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,473,159 | 13.1% |
| LOAD_GLOBAL_MODULE | 5,902,500 | 10.4% |
| LOAD_CONST | 2,491,800 | 4.4% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 767,117,309 | 57.5% |
| LOAD_ATTR_INSTANCE_VALUE | 190,003,151 | 14.2% |
| LOAD_CONST | 90,388,568 | 6.8% |
| LOAD_GLOBAL_MODULE | 52,878,581 | 4.0% |
| LOAD_ATTR_SLOT | 48,976,832 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 663,868,160 | 49.8% |
| LOAD_CONST | 155,817,009 | 11.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 151,127,016 | 11.3% |
| LOAD_FAST_LOAD_FAST | 111,682,121 | 8.4% |
| CALL_PY_EXACT_ARGS | 111,393,348 | 8.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,577,858,370 | 84.7% |
| LOAD_ATTR_INSTANCE_VALUE | 63,481,152 | 3.4% |
| LOAD_ATTR_SLOT | 45,631,315 | 2.4% |
| LOAD_ATTR | 45,436,236 | 2.4% |
| LOAD_ATTR_WITH_HINT | 37,578,857 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 803,890,334 | 43.2% |
| LOAD_FAST_LOAD_FAST | 480,420,914 | 25.8% |
| CALL_PY_EXACT_ARGS | 430,701,561 | 23.1% |
| LOAD_GLOBAL_MODULE | 55,446,412 | 3.0% |
| LOAD_CONST | 53,011,746 | 2.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 324,190,529 | 95.4% |
| LOAD_ATTR_MODULE | 11,618,955 | 3.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,324,680 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 266,356,831 | 78.4% |
| CALL_NO_KW_ISINSTANCE | 22,115,516 | 6.5% |
| LOAD_ATTR_MODULE | 11,618,955 | 3.4% |
| LOAD_FAST | 10,381,529 | 3.1% |
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
| LOAD_FAST | 130,433,371 | 91.0% |
| LOAD_FAST_LOAD_FAST | 10,919,929 | 7.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,061,220 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 759,700 | 0.5% |
| STORE_FAST_LOAD_FAST | 181,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,600,359 | 21.3% |
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
| LOAD_FAST | 40,559,998 | 83.5% |
| LOAD_ATTR_SLOT | 5,106,880 | 10.5% |
| RETURN_VALUE | 1,327,492 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,064,920 | 2.2% |
| LOAD_FAST_LOAD_FAST | 125,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 42,926,527 | 88.4% |
| TO_BOOL_NONE | 3,107,760 | 6.4% |
| RETURN_VALUE | 833,661 | 1.7% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,230,830,657 | 91.5% |
| LOAD_ATTR_SLOT | 40,651,782 | 3.0% |
| COPY | 40,401,413 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 8,700,845 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,016,472 | 22.8% |
| TO_BOOL_NONE | 88,085,075 | 6.5% |
| LOAD_ATTR | 81,103,622 | 6.0% |
| TO_BOOL_BOOL | 68,852,736 | 5.1% |
| COMPARE_OP_FLOAT | 66,492,869 | 4.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 277,226,566 | 79.9% |
| LOAD_ATTR_INSTANCE_VALUE | 22,740,846 | 6.6% |
| LOAD_ATTR_WITH_HINT | 22,281,408 | 6.4% |
| COPY | 14,038,528 | 4.0% |
| LOAD_FAST_LOAD_FAST | 8,451,706 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,380,678 | 24.6% |
| STORE_FAST | 43,154,700 | 12.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 37,578,857 | 10.8% |
| COMPARE_OP_INT | 35,280,942 | 10.2% |
| LOAD_CONST | 29,373,200 | 8.5% |


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
| LOAD_FAST | 4,901,789,892 | 51.2% |
| LOAD_CONST | 744,385,935 | 7.8% |
| LOAD_FAST_LOAD_FAST | 450,389,754 | 4.7% |
| STORE_FAST | 292,609,882 | 3.1% |
| POP_JUMP_IF_FALSE | 274,564,117 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,771,634,353 | 18.5% |
| COMPARE_OP_STR | 1,563,963,726 | 16.3% |
| LOAD_FAST | 1,052,729,818 | 11.0% |
| LOAD_CONST | 744,385,935 | 7.8% |
| COMPARE_OP_INT | 671,005,240 | 7.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 345,216,825 | 41.1% |
| LOAD_GLOBAL_BUILTIN | 107,455,726 | 12.8% |
| POP_JUMP_IF_FALSE | 57,743,084 | 6.9% |
| RESUME | 33,048,539 | 3.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,880 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 519,755,636 | 61.9% |
| LOAD_CONST | 69,819,537 | 8.3% |
| PUSH_NULL | 38,304,351 | 4.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 31,867,105 | 3.8% |
| LOAD_DEREF | 24,558,683 | 2.9% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,674,942,499 | 16.7% |
| POP_JUMP_IF_FALSE | 4,511,943,295 | 16.2% |
| LOAD_GLOBAL_BUILTIN | 2,662,318,497 | 9.5% |
| RESUME | 2,091,089,259 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,053,256,862 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,901,789,892 | 17.5% |
| LOAD_ATTR_INSTANCE_VALUE | 3,157,431,269 | 11.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,577,858,370 | 5.6% |
| LOAD_ATTR_SLOT | 1,230,830,657 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 1,101,492,738 | 3.9% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 39,934,055 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,374,959 | 23.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 39,925,895 | 76.3% |
| LOAD_FAST_AND_CLEAR | 12,374,959 | 23.7% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,682,680 | 50.4% |
| POP_TOP | 2,058,360 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 421,860 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 339,271 | 4.6% |
| STORE_FAST | 308,760 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 49.0% |
| POP_JUMP_IF_NOT_NONE | 1,511,040 | 20.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 5.9% |
| LOAD_FAST | 383,640 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 335,071 | 4.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,332,276,589 | 16.7% |
| POP_JUMP_IF_FALSE | 1,183,206,149 | 14.8% |
| NOP | 959,967,658 | 12.0% |
| LOAD_FAST_LOAD_FAST | 512,666,048 | 6.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 480,420,914 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 1,202,362,860 | 15.0% |
| CONTAINS_OP | 989,415,960 | 12.4% |
| CALL_PY_EXACT_ARGS | 660,066,855 | 8.3% |
| LOAD_FAST | 643,890,050 | 8.0% |
| STORE_ATTR_SLOT | 515,591,935 | 6.4% |


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
| STORE_FAST | 20,223 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 8,395 | 0.1% |
| NOP | 4,589 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,695 | 98.9% |
| LOAD_GLOBAL_MODULE | 42,885 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 15,900 | 0.2% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,618 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,101,492,738 | 26.7% |
| POP_JUMP_IF_FALSE | 982,241,381 | 23.8% |
| RESUME | 846,746,459 | 20.5% |
| STORE_FAST | 536,607,134 | 13.0% |
| POP_JUMP_IF_TRUE | 98,147,477 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,662,318,497 | 64.5% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.5% |
| CALL_NO_KW_ISINSTANCE | 331,866,824 | 8.0% |
| LOAD_ATTR | 221,917,316 | 5.4% |
| LOAD_FAST_LOAD_FAST | 113,564,756 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 888,217,750 | 31.0% |
| STORE_FAST | 420,470,264 | 14.7% |
| RESUME | 336,737,488 | 11.7% |
| POP_JUMP_IF_FALSE | 272,980,142 | 9.5% |
| LOAD_FAST_LOAD_FAST | 113,386,399 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 459,616,968 | 16.0% |
| LOAD_FAST | 452,200,588 | 15.8% |
| CALL_NO_KW_ISINSTANCE | 342,580,679 | 11.9% |
| LOAD_ATTR_MODULE | 324,190,529 | 11.3% |
| CONTAINS_OP | 301,873,792 | 10.5% |


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
| LOAD_FAST | 114,364,280 | 100.0% |
| LOAD_DEREF | 9,080 | 0.0% |
| LOAD_SUPER_ATTR | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,703,944 | 54.8% |
| LOAD_FAST | 37,260,748 | 32.6% |
| CALL_PY_EXACT_ARGS | 6,408,098 | 5.6% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.2% |
| CALL | 1,200,040 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,473,336 | 53.6% |
| CALL_PY_EXACT_ARGS | 31,462,235 | 34.1% |
| CALL_FUNCTION_EX | 4,744,568 | 5.1% |
| CALL | 4,142,792 | 4.5% |
| CALL_PY_WITH_DEFAULTS | 1,593,597 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 49,473,336 | 53.4% |
| RESUME | 42,526,105 | 45.9% |
| RETURN_GENERATOR | 656,164 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 94,843,674 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 82,640,627 | 87.1% |
| LOAD_FAST | 9,062,460 | 9.6% |
| LOAD_GLOBAL_MODULE | 2,504,360 | 2.6% |
| KW_NAMES | 255,360 | 0.3% |
| CALL | 127,951 | 0.1% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,896,280 | 38.4% |
| RETURN_VALUE | 6,380,580 | 15.4% |
| LOAD_FAST | 6,188,716 | 14.9% |
| JUMP_FORWARD | 4,782,840 | 11.6% |
| STORE_FAST | 4,549,800 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,597,580 | 49.8% |
| JUMP_BACKWARD | 19,591,412 | 47.3% |
| CALL_FUNCTION_EX | 1,211,460 | 2.9% |
| DICT_UPDATE | 180 | 0.0% |
| BUILD_MAP | 120 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 718,029,939 | 48.0% |
| RESUME | 337,443,652 | 22.5% |
| STORE_FAST | 158,967,381 | 10.6% |
| POP_JUMP_IF_FALSE | 80,718,660 | 5.4% |
| NOP | 52,970,963 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 959,967,658 | 64.1% |
| LOAD_FAST | 402,241,770 | 26.9% |
| NOP | 52,970,963 | 3.5% |
| LOAD_GLOBAL_BUILTIN | 34,245,423 | 2.3% |
| LOAD_CONST | 22,891,841 | 1.5% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,940,556 | 58.3% |
| STORE_SUBSCR_DICT | 3,085,694 | 18.1% |
| SWAP | 1,973,644 | 11.6% |
| COPY | 1,285,302 | 7.5% |
| STORE_FAST | 547,142 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,501,463 | 55.7% |
| RETURN_VALUE | 1,913,949 | 11.2% |
| JUMP_FORWARD | 1,715,820 | 10.1% |
| POP_TOP | 1,385,013 | 8.1% |
| RERAISE | 1,285,302 | 7.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,325,268,881 | 27.7% |
| CONTAINS_OP | 1,870,207,968 | 22.3% |
| COMPARE_OP_STR | 1,550,229,127 | 18.5% |
| COMPARE_OP_INT | 1,265,605,196 | 15.1% |
| IS_OP | 376,290,211 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,511,943,295 | 53.7% |
| LOAD_FAST_LOAD_FAST | 1,183,206,149 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 982,241,381 | 11.7% |
| JUMP_BACKWARD | 444,393,844 | 5.3% |
| LOAD_CONST | 274,564,117 | 3.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 195,023,208 | 67.2% |
| EXTENDED_ARG | 36,519,160 | 12.6% |
| LOAD_ATTR_SLOT | 25,425,420 | 8.8% |
| LOAD_DEREF | 13,782,636 | 4.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,410,085 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 184,160,236 | 63.4% |
| LOAD_DEREF | 28,710,406 | 9.9% |
| JUMP_BACKWARD | 20,403,953 | 7.0% |
| RETURN_CONST | 15,885,972 | 5.5% |
| LOAD_GLOBAL_BUILTIN | 12,783,234 | 4.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 346,426,284 | 82.5% |
| LOAD_ATTR_INSTANCE_VALUE | 27,648,178 | 6.6% |
| LOAD_ATTR | 14,147,896 | 3.4% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.1% |
| EXTENDED_ARG | 7,255,900 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 167,073,646 | 39.8% |
| LOAD_GLOBAL_BUILTIN | 96,627,842 | 23.0% |
| LOAD_FAST_LOAD_FAST | 58,939,790 | 14.0% |
| LOAD_GLOBAL_MODULE | 36,034,966 | 8.6% |
| NOP | 18,001,720 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 725,084,520 | 49.8% |
| TO_BOOL | 132,361,732 | 9.1% |
| COMPARE_OP_INT | 122,126,481 | 8.4% |
| TO_BOOL_ALWAYS_TRUE | 82,915,559 | 5.7% |
| TO_BOOL_NONE | 77,693,842 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 593,708,132 | 40.7% |
| JUMP_BACKWARD | 465,303,685 | 31.9% |
| LOAD_GLOBAL_BUILTIN | 98,147,477 | 6.7% |
| LOAD_CONST | 68,426,792 | 4.7% |
| POP_TOP | 66,410,431 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 569,606,923 | 25.3% |
| RESUME | 472,275,107 | 21.0% |
| CALL_NO_KW_BUILTIN_O | 341,716,865 | 15.2% |
| POP_JUMP_IF_FALSE | 161,938,763 | 7.2% |
| RETURN_VALUE | 121,198,755 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 902,821,941 | 38.6% |
| JUMP_BACKWARD | 657,953,160 | 28.1% |
| RESUME | 238,826,020 | 10.2% |
| RETURN_CONST | 184,078,203 | 7.9% |
| LOAD_FAST_LOAD_FAST | 99,544,334 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,216,301 | 30.7% |
| LOAD_ATTR | 3,246,421 | 19.1% |
| RAISE_VARARGS | 2,298,202 | 13.5% |
| CALL_NO_KW_BUILTIN_FAST | 1,785,274 | 10.5% |
| RERAISE | 1,115,622 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,415,830 | 90.4% |
| LOAD_GLOBAL_MODULE | 1,103,867 | 6.5% |
| LOAD_FAST | 387,186 | 2.3% |
| WITH_EXCEPT_START | 138,122 | 0.8% |
| LOAD_GLOBAL | 616 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 630,231,274 | 58.2% |
| LOAD_ATTR_MODULE | 266,356,831 | 24.6% |
| LOAD_ATTR | 69,681,293 | 6.4% |
| LOAD_FAST_LOAD_FAST | 47,492,640 | 4.4% |
| LOAD_DEREF | 38,304,351 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 535,068,566 | 49.5% |
| LOAD_FAST_LOAD_FAST | 283,767,872 | 26.2% |
| LOAD_CONST | 138,368,898 | 12.8% |
| CALL | 50,852,638 | 4.7% |
| LOAD_GLOBAL_MODULE | 31,523,796 | 2.9% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,494,530 | 51.6% |
| LOAD_ATTR_MODULE | 583,740 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 18.8% |
| LOAD_FAST | 151,170 | 5.2% |
| RETURN_VALUE | 55,440 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,298,202 | 79.4% |
| COPY | 445,440 | 15.4% |
| LOAD_CONST | 151,230 | 5.2% |
| CALL_INTRINSIC_1 | 30 | 0.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,381,104 | 75.1% |
| POP_EXCEPT | 1,285,302 | 15.1% |
| POP_TOP | 386,940 | 4.6% |
| POP_JUMP_IF_FALSE | 155,640 | 1.8% |
| DELETE_FAST | 151,230 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,115,622 | 56.1% |
| COPY | 831,216 | 41.8% |
| CALL_INTRINSIC_1 | 42,150 | 2.1% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,492,712,812 | 63.3% |
| POP_TOP | 238,826,020 | 6.1% |
| CALL | 211,834,796 | 5.4% |
| SEND_GEN | 208,498,780 | 5.3% |
| COPY_FREE_VARS | 175,692,725 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,091,089,259 | 42.2% |
| LOAD_GLOBAL_BUILTIN | 846,746,459 | 17.1% |
| POP_TOP | 472,275,107 | 9.5% |
| NOP | 337,443,652 | 6.8% |
| LOAD_GLOBAL_MODULE | 336,737,488 | 6.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 267,508,108 | 20.0% |
| STORE_ATTR_SLOT | 246,975,585 | 18.4% |
| POP_TOP | 184,078,203 | 13.7% |
| STORE_ATTR_INSTANCE_VALUE | 176,745,057 | 13.2% |
| RESUME | 122,771,703 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 569,606,923 | 42.5% |
| INTERPRETER_EXIT | 410,743,440 | 30.6% |
| EXIT_INIT_CHECK | 67,101,168 | 5.0% |
| TO_BOOL_BOOL | 56,811,291 | 4.2% |
| END_FOR | 56,701,040 | 4.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,432,348 | 63.6% |
| COPY_FREE_VARS | 73,605,810 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,374,890 | 1.5% |
| CALL_FUNCTION_EX | 1,715,674 | 0.8% |
| CALL | 873,460 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,586,454 | 32.9% |
| GET_ITER | 37,670,523 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,880 | 13.8% |
| STORE_FAST | 19,530,120 | 8.2% |
| INTERPRETER_EXIT | 18,176,234 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 773,837,622 | 25.9% |
| RETURN_VALUE | 509,460,775 | 17.1% |
| BUILD_TUPLE | 413,114,075 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 176,982,760 | 5.9% |
| BINARY_SUBSCR_DICT | 104,204,105 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 618,271,199 | 20.7% |
| RETURN_VALUE | 509,460,775 | 17.1% |
| INTERPRETER_EXIT | 329,685,413 | 11.1% |
| UNPACK_SEQUENCE_TUPLE | 264,500,923 | 8.9% |
| TO_BOOL_BOOL | 251,520,406 | 8.4% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,456,422 | 94.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,245,730 | 5.5% |
| SEND | 28,886 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,455,363 | 89.1% |
| YIELD_VALUE | 6,246,171 | 5.5% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,886 | 0.0% |
| SEND_GEN | 609 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,498,831 | 69.0% |
| LOAD_CONST | 93,862,808 | 31.0% |
| SEND | 609 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,498,780 | 69.0% |
| POP_TOP | 93,863,288 | 31.0% |
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
| MAKE_FUNCTION | 82,640,627 | 98.7% |
| SET_FUNCTION_ATTRIBUTE | 1,109,936 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,219,810 | 64.7% |
| LOAD_GLOBAL_BUILTIN | 18,989,340 | 22.7% |
| STORE_FAST | 5,796,599 | 6.9% |
| CALL_PY_EXACT_ARGS | 2,063,128 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 1,109,936 | 1.3% |


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
| LOAD_FAST | 31,581,337 | 59.0% |
| LOAD_FAST_LOAD_FAST | 15,245,065 | 28.5% |
| CALL | 5,419,260 | 10.1% |
| SWAP | 946,677 | 1.8% |
| LOAD_GLOBAL_MODULE | 199,180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,910,891 | 29.7% |
| LOAD_DEREF | 13,447,060 | 25.1% |
| RETURN_CONST | 8,606,153 | 16.1% |
| JUMP_BACKWARD | 5,554,200 | 10.4% |
| LOAD_FAST_LOAD_FAST | 4,744,244 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 361,598,116 | 44.6% |
| LOAD_FAST_LOAD_FAST | 297,300,351 | 36.6% |
| SWAP | 77,250,653 | 9.5% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.3% |
| RETURN_VALUE | 21,167,460 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300,528,451 | 37.0% |
| RETURN_CONST | 176,745,057 | 21.8% |
| LOAD_FAST_LOAD_FAST | 167,682,881 | 20.7% |
| LOAD_CONST | 67,551,752 | 8.3% |
| NOP | 51,797,785 | 6.4% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 515,591,935 | 48.5% |
| LOAD_FAST | 504,077,578 | 47.4% |
| SWAP | 40,401,413 | 3.8% |
| STORE_ATTR_SLOT | 2,126,634 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 279,510,809 | 26.3% |
| LOAD_FAST | 253,879,056 | 23.9% |
| RETURN_CONST | 246,975,585 | 23.2% |
| LOAD_CONST | 220,190,994 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 25,391,400 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,739,753 | 48.5% |
| SWAP | 14,038,528 | 27.5% |
| LOAD_FAST_LOAD_FAST | 11,937,004 | 23.4% |
| LOAD_DEREF | 242,500 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,113,637 | 66.9% |
| JUMP_BACKWARD | 5,313,540 | 10.4% |
| RETURN_CONST | 4,426,115 | 8.7% |
| LOAD_CONST | 3,924,007 | 7.7% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.5% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,874,000 | 40.9% |
| STORE_FAST | 19,047,660 | 29.0% |
| LOAD_CONST | 6,839,016 | 10.4% |
| LOAD_FAST | 2,917,140 | 4.4% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,460 | 28.9% |
| LOAD_DEREF | 13,769,978 | 20.9% |
| LOAD_FAST_LOAD_FAST | 13,437,000 | 20.4% |
| LOAD_FAST | 9,640,256 | 14.7% |
| LOAD_CONST | 4,835,432 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,258,764,033 | 12.8% |
| BINARY_SUBSCR_STR_INT | 841,517,940 | 8.6% |
| STORE_FAST | 711,190,646 | 7.3% |
| RETURN_VALUE | 618,271,199 | 6.3% |
| FOR_ITER_LIST | 587,131,335 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,674,942,499 | 47.7% |
| LOAD_FAST_LOAD_FAST | 1,332,276,589 | 13.6% |
| JUMP_BACKWARD | 918,432,595 | 9.4% |
| STORE_FAST | 711,190,646 | 7.3% |
| LOAD_GLOBAL_BUILTIN | 536,607,134 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,533,080 | 58.9% |
| FOR_ITER_RANGE | 35,717,280 | 26.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,140 | 6.7% |
| FOR_ITER_TUPLE | 6,874,080 | 5.0% |
| FOR_ITER | 2,965,746 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,780 | 21.6% |
| LOAD_FAST | 24,445,380 | 17.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,928,140 | 15.3% |
| STORE_ATTR_INSTANCE_VALUE | 9,297,508 | 6.8% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.5% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,843 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 368,128,708 | 23.9% |
| UNPACK_SEQUENCE_TUPLE | 140,575,357 | 9.1% |
| UNPACK_SEQUENCE_LIST | 134,205,000 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,163,843 | 52.8% |
| LOAD_FAST | 465,938,218 | 30.2% |
| LOAD_FAST_LOAD_FAST | 86,512,369 | 5.6% |
| STORE_FAST | 75,477,274 | 4.9% |
| LOAD_GLOBAL_MODULE | 46,179,336 | 3.0% |


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
| LOAD_CONST | 13,495,828 | 11.5% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,615,308 | 91.5% |
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
| LOAD_FAST | 64,774,560 | 20.5% |
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
| LOAD_FAST_LOAD_FAST | 95,460,716 | 48.0% |
| LOAD_FAST | 63,112,655 | 31.7% |
| CALL_NO_KW_BUILTIN_O | 13,999,260 | 7.0% |
| RETURN_VALUE | 7,992,040 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 73,054,146 | 36.7% |
| LOAD_FAST | 66,119,031 | 33.2% |
| JUMP_BACKWARD | 31,629,616 | 15.9% |
| RETURN_CONST | 12,894,044 | 6.5% |
| LOAD_GLOBAL_MODULE | 7,343,169 | 3.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,500 | 52.3% |
| LOAD_FAST | 56,880,860 | 18.9% |
| LOAD_CONST | 26,912,068 | 8.9% |
| LOAD_FAST_LOAD_FAST | 24,058,270 | 8.0% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 114,923,300 | 38.1% |
| JUMP_BACKWARD | 110,076,280 | 36.5% |
| LOAD_FAST_LOAD_FAST | 71,546,190 | 23.7% |
| RETURN_CONST | 4,469,760 | 1.5% |
| LOAD_CONST | 230,760 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,859,840 | 28.9% |
| BINARY_OP_ADD_FLOAT | 116,612,680 | 12.5% |
| LOAD_FAST | 105,298,979 | 11.3% |
| BINARY_OP_ADD_INT | 88,107,432 | 9.5% |
| BINARY_OP_SUBTRACT_INT | 68,653,683 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 268,859,840 | 28.9% |
| STORE_SUBSCR_LIST_INT | 157,633,500 | 16.9% |
| COPY | 112,622,324 | 12.1% |
| STORE_SUBSCR | 109,838,120 | 11.8% |
| STORE_ATTR_INSTANCE_VALUE | 77,250,653 | 8.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 165,772,188 | 80.9% |
| LOAD_ATTR_INSTANCE_VALUE | 23,952,666 | 11.7% |
| LOAD_ATTR | 7,358,388 | 3.6% |
| LOAD_ATTR_SLOT | 3,352,621 | 1.6% |
| COPY | 2,331,736 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 132,361,732 | 64.6% |
| POP_JUMP_IF_FALSE | 71,873,653 | 35.1% |
| TO_BOOL | 235,790 | 0.1% |
| UNARY_NOT | 220,623 | 0.1% |
| TO_BOOL_NONE | 125,703 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,565,367 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,746,358 | 33.4% |
| LOAD_ATTR_SLOT | 17,761,080 | 9.9% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 7,172,936 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 94,344,435 | 52.7% |
| POP_JUMP_IF_TRUE | 82,915,559 | 46.3% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,844 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,505 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 797,091,394 | 25.0% |
| LOAD_FAST | 715,261,639 | 22.5% |
| CALL_NO_KW_BUILTIN_FAST | 477,701,598 | 15.0% |
| LOAD_ATTR_INSTANCE_VALUE | 428,229,904 | 13.4% |
| RETURN_VALUE | 251,520,406 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,325,268,881 | 73.0% |
| POP_JUMP_IF_TRUE | 725,084,520 | 22.8% |
| EXTENDED_ARG | 88,770,834 | 2.8% |
| UNARY_NOT | 46,466,172 | 1.5% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 173,527,796 | 76.0% |
| CALL_NO_KW_BUILTIN_O | 12,836,580 | 5.6% |
| COPY | 12,663,668 | 5.5% |
| BINARY_OP | 9,124,997 | 4.0% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,407,504 | 88.2% |
| POP_JUMP_IF_TRUE | 25,611,874 | 11.2% |
| UNARY_NOT | 1,035,600 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,865,303 | 66.9% |
| LOAD_ATTR_INSTANCE_VALUE | 27,749,907 | 24.8% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,712,180 | 1.5% |
| COPY | 814,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,666,782 | 55.1% |
| POP_JUMP_IF_FALSE | 46,705,791 | 41.7% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 902,760 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,518,948 | 45.0% |
| LOAD_ATTR_SLOT | 88,085,075 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 56,724,297 | 15.1% |
| LOAD_ATTR | 21,871,288 | 5.8% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 296,859,082 | 78.9% |
| POP_JUMP_IF_TRUE | 77,693,842 | 20.6% |
| EXTENDED_ARG | 967,320 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,931 | 0.2% |
| TO_BOOL | 123,674 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,966,048 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,407,740 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,340 | 5.8% |
| COPY | 2,682,160 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 36,172,731 | 53.8% |
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
| BINARY_OP | 10,592,675 | 92.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 386,198 | 3.4% |
| LOAD_ATTR_MODULE | 311,830 | 2.7% |
| LOAD_FAST | 122,040 | 1.1% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,423,003 | 100.0% |


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
| TO_BOOL_BOOL | 46,466,172 | 91.1% |
| TO_BOOL_LIST | 2,640,720 | 5.2% |
| TO_BOOL_INT | 1,035,600 | 2.0% |
| TO_BOOL_STR | 600,240 | 1.2% |
| TO_BOOL | 220,623 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 23,463,060 | 46.0% |
| RETURN_VALUE | 15,182,772 | 29.8% |
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
| STORE_FAST_STORE_FAST | 134,286 | 62.0% |
| STORE_FAST | 79,690 | 36.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,727 | 0.8% |
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
| RETURN_VALUE | 264,500,923 | 62.2% |
| LOAD_FAST | 103,134,100 | 24.2% |
| BINARY_SUBSCR_DICT | 15,509,554 | 3.6% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260,434,319 | 61.2% |
| STORE_FAST_STORE_FAST | 140,575,357 | 33.1% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.6% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,610,478 | 52.0% |
| FOR_ITER | 151,763,390 | 25.1% |
| RETURN_VALUE | 84,702,116 | 14.0% |
| LOAD_FAST | 35,337,180 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 368,128,708 | 60.8% |
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
| PUSH_EXC_INFO | 138,122 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 137,324 | 99.4% |
| TO_BOOL_BOOL | 780 | 0.6% |
| TO_BOOL | 18 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.4% |
| YIELD_VALUE | 208,499,140 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,270 | 4.5% |
| LOAD_CONST | 26,891,256 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 451,460,649 | 65.1% |
| YIELD_VALUE | 208,499,140 | 30.1% |
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
| specialization.deferred |    204566077 | 4.7% |
| specialization.deopt |      1599021 | 0.0% |
|          hit |   4063483071 | 93.3% |
|         miss |     84780130 | 1.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,613,091 | 80.8% |
| Failure | 383,564 | 19.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.4% |
| other | 125,980 | 32.8% |
| tuple | 75,020 | 19.6% |
| dict | 16,813 | 4.4% |
| bytes | 10,777 | 2.8% |
| set | 7,220 | 1.9% |
| sequence | 6,039 | 1.6% |
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
| specialization.deferred |   1111036533 | 26.5% |
| specialization.deopt |        68528 | 0.0% |
|          hit |   3071821406 | 73.4% |
|         miss |      3634848 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 70,622 | 19.8% |
| Failure | 286,859 | 80.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 112,980 | 39.4% |
| other | 77,500 | 27.0% |
| out of range | 40,680 | 14.2% |
| buffer int | 25,739 | 9.0% |
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
| specialization.deferred |    316113957 | 38.7% |
| specialization.deopt |           40 | 0.0% |
|          hit |    500574118 | 61.3% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,747 | 2.0% |
| Failure | 83,793 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.5% |
| dict subclass no override | 17,960 | 21.4% |
| py simple | 13,813 | 16.5% |
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
| specialization.deferred |       213976 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1168542153 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,287 | 99.1% |
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
| specialization.deferred |    293062325 | 11.6% |
| specialization.deopt |      2480405 | 0.1% |
|          hit |   2102880908 | 83.2% |
|         miss |    131462231 | 5.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,480 | 96.2% |
| Failure | 96,705 | 3.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,020 | 23.8% |
| dict items | 20,430 | 21.1% |
| seq iter | 15,120 | 15.6% |
| set | 13,252 | 13.7% |
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
| specialization.deferred |     53482916 | 2.7% |
| specialization.deopt |      3437802 | 0.2% |
|          hit |   1743104885 | 88.1% |
|         miss |    182211819 | 9.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,460,485 | 98.9% |
| Failure | 38,740 | 1.1% |

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
| not managed dict | 380 | 1.0% |
| method | 300 | 0.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1036992532 | 10.0% |
| specialization.deopt |      9595758 | 0.1% |
|          hit |   8836665761 | 85.1% |
|         miss |    508722223 | 4.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,667,547 | 95.6% |
| Failure | 449,641 | 4.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 147,826 | 32.9% |
| metaclass attribute | 101,975 | 22.7% |
| method | 60,697 | 13.5% |
| not managed dict | 59,451 | 13.2% |
| shadowed | 40,658 | 9.0% |
| non object slot | 7,714 | 1.7% |
| class method obj | 7,260 | 1.6% |
| class attr descriptor | 6,280 | 1.4% |
| overridden | 5,220 | 1.2% |
| non overriding descriptor | 4,472 | 1.0% |
| mutable class | 2,863 | 0.6% |
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
| specialization.deferred |    145338450 | 4.3% |
| specialization.deopt |        27070 | 0.0% |
|          hit |   3202556349 | 95.6% |
|         miss |      1435726 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 31,116 | 21.2% |
| Failure | 115,889 | 78.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 53,571 | 46.2% |
| different types | 23,826 | 20.6% |
| baseobject | 13,267 | 11.4% |
| float long | 9,288 | 8.0% |
| set | 6,620 | 5.7% |
| other | 3,000 | 2.6% |
| bool | 2,357 | 2.0% |
| tuple | 1,680 | 1.4% |
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
| specialization.deferred |      7322610 | 0.1% |
| specialization.deopt |          462 | 0.0% |
|          hit |   6996394936 | 99.9% |
|         miss |        27770 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 55,787 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    839572105 | 15.6% |
| specialization.deopt |       712840 | 0.0% |
|          hit |   4514139841 | 83.7% |
|         miss |     37782945 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,908 | 39.2% |
| Failure | 1,110,376 | 60.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 579,020 | 52.1% |
| multiply different types | 171,560 | 15.5% |
| add different types | 151,880 | 13.7% |
| floor divide | 32,760 | 3.0% |
| and int | 32,087 | 2.9% |
| remainder | 32,031 | 2.9% |
| add other | 27,100 | 2.4% |
| lshift | 18,760 | 1.7% |
| rshift | 16,631 | 1.5% |
| true divide different types | 14,862 | 1.3% |
| xor | 10,420 | 0.9% |
| true divide float | 6,780 | 0.6% |
| subtract other | 5,520 | 0.5% |
| or | 4,083 | 0.4% |
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
| specialization.deferred |    112701543 | 27.2% |
|          hit |    302362068 | 72.8% |
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
|          hit |    116673660 | 100.0% |

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
| specialization.deferred |    893867650 | 10.1% |
| specialization.deopt |      2750808 | 0.0% |
|          hit |   7775141458 | 88.2% |
|         miss |    145916636 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,798,650 | 87.7% |
| Failure | 394,081 | 12.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 66,299 | 16.8% |
| kwnames | 56,140 | 14.2% |
| code complex parameters | 54,197 | 13.8% |
| no dict | 51,380 | 13.0% |
| class no vectorcall | 29,448 | 7.5% |
| cfunc varargs keywords | 24,892 | 6.3% |
| cfunc noargs | 22,591 | 5.7% |
| meth descr varargs | 22,420 | 5.7% |
| other | 11,456 | 2.9% |
| init not python | 10,420 | 2.6% |
| class mutable | 8,747 | 2.2% |
| init not simple | 8,420 | 2.1% |
| meth descr varargs keywords | 7,327 | 1.9% |
| wrong number arguments | 4,460 | 1.1% |
| cmethod | 3,600 | 0.9% |
| bound method | 3,365 | 0.9% |
| cfunc varargs | 3,090 | 0.8% |
| method wrapper | 2,468 | 0.6% |
| operator wrapper | 2,361 | 0.6% |
| str | 1,000 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 94,485,346,276 | 63.7% |
| Not specialized | 9,687,623,268 | 6.5% |
| Specialized | 44,257,833,280 | 29.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 1,111,036,533 | 22.2% |
| LOAD_ATTR | 1,036,992,532 | 20.7% |
| CALL | 893,867,650 | 17.8% |
| BINARY_OP | 839,572,105 | 16.7% |
| STORE_SUBSCR | 316,113,957 | 6.3% |
| FOR_ITER | 293,062,325 | 5.8% |
| TO_BOOL | 204,566,077 | 4.1% |
| COMPARE_OP | 145,338,450 | 2.9% |
| SEND | 112,701,543 | 2.2% |
| STORE_ATTR | 53,482,916 | 1.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 193,659,665 | 17.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 152,824,881 | 13.9% |
| STORE_ATTR_SLOT | 112,704,554 | 10.3% |
| CALL_PY_EXACT_ARGS | 86,811,675 | 7.9% |
| STORE_ATTR_INSTANCE_VALUE | 69,438,567 | 6.3% |
| FOR_ITER_LIST | 65,829,676 | 6.0% |
| FOR_ITER_TUPLE | 65,581,135 | 6.0% |
| LOAD_ATTR_SLOT | 57,457,589 | 5.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 50,962,803 | 4.6% |
| LOAD_ATTR_METHOD_NO_DICT | 45,158,420 | 4.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,218,637,833 | 23.4% |
| Calls to Python functions inlined | 3,997,294,142 | 76.6% |
| Calls via PyEval_EvalFrame (total) | 1,218,637,833 | 23.4% |
| Calls via PyEval_EvalFrame (vector) | 678,915,141 | 13.0% |
| Calls via PyEval_EvalFrame (generator) | 539,722,692 | 10.3% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 678,910,041 | 13.0% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 191,541,058 | 3.7% |
| Calls via PyEval_EvalFrame (function ex) | 13,960,471 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 115,829,307 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 94,980,963 | 1.8% |
| Frames pushed | 4,350,734,024 | 83.4% |
| Frame objects created | 59,296,960 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,172,066,180 | 35.4% |
| Frees to freelist | 4,176,184,440 |  |
| Allocations | 7,612,228,064 | 64.6% |
| Allocations to 512 bytes | 7,530,494,093 | 63.9% |
| Allocations to 4 kbytes | 66,550,243 | 0.6% |
| Allocations over 4 kbytes | 15,183,728 | 0.1% |
| Frees | 7,878,934,704 |  |
| New values | 57,541,973 |  |
| Interpreter increfs | 56,253,318,418 | 78.0% |
| Interpreter decrefs | 65,256,339,522 | 78.3% |
| Increfs | 15,905,205,059 | 22.0% |
| Decrefs | 18,090,793,795 | 21.7% |
| Materialize dict (on request) | 3,979,283 | 6.9% |
| Materialize dict (new key) | 142,640 | 0.2% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 1,524,463 | 2.6% |
| Method cache hits | 1,817,932,905 |  |
| Method cache misses | 71,547,460 |  |
| Method cache collisions | 75,806,140 |  |
| Method cache dunder hits | 2,210,906,900 |  |
| Method cache dunder misses | 4,299,427 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 345,419 | 34,711,594 | 3,462,919,836 |
| 1 | 30,682 | 65,125,536 | 2,927,476,472 |
| 2 | 14,205 | 40,814,646 | 9,814,047,368 |


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
