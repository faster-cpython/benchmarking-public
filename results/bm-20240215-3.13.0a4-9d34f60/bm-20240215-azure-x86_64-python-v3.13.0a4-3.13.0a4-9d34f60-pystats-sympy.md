
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
| LOAD_FAST | 977,239,139 | 16.4% | 16.4% |  |
| STORE_FAST | 359,073,889 | 6.0% | 22.4% |  |
| POP_JUMP_IF_FALSE | 272,442,469 | 4.6% | 27.0% |  |
| RESUME_CHECK | 258,292,257 | 4.3% | 31.3% |  |
| LOAD_FAST_LOAD_FAST | 254,310,091 | 4.3% | 35.6% |  |
| LOAD_GLOBAL_BUILTIN | 233,855,378 | 3.9% | 39.5% | 0.0% |
| LOAD_CONST | 191,442,158 | 3.2% | 42.8% |  |
| RETURN_VALUE | 177,416,971 | 3.0% | 45.7% |  |
| TO_BOOL_BOOL | 172,719,233 | 2.9% | 48.6% | 0.1% |
| JUMP_BACKWARD | 156,747,719 | 2.6% | 51.3% |  |
| LOAD_GLOBAL_MODULE | 145,741,586 | 2.4% | 53.7% | 0.0% |
| INTERPRETER_EXIT | 127,598,411 | 2.1% | 55.9% |  |
| LOAD_ATTR | 121,704,469 | 2.0% | 57.9% |  |
| STORE_FAST_STORE_FAST | 106,113,763 | 1.8% | 59.7% |  |
| FOR_ITER | 104,250,807 | 1.8% | 61.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 104,161,235 | 1.7% | 63.2% |  |
| POP_JUMP_IF_TRUE | 100,078,691 | 1.7% | 64.9% |  |
| LOAD_ATTR_SLOT | 96,035,234 | 1.6% | 66.5% | 38.1% |
| LOAD_ATTR_METHOD_NO_DICT | 91,719,505 | 1.5% | 68.0% | 10.1% |
| LOAD_DEREF | 69,030,462 | 1.2% | 69.2% |  |
| CALL_PY_EXACT_ARGS | 68,196,541 | 1.1% | 70.3% | 11.5% |
| CALL_ISINSTANCE | 67,458,795 | 1.1% | 71.4% |  |
| FOR_ITER_LIST | 62,860,918 | 1.1% | 72.5% | 1.2% |
| POP_TOP | 61,988,041 | 1.0% | 73.5% |  |
| PUSH_NULL | 60,716,050 | 1.0% | 74.6% |  |
| GET_ITER | 60,070,262 | 1.0% | 75.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 58,863,526 | 1.0% | 76.6% | 28.9% |
| RETURN_CONST | 57,324,483 | 1.0% | 77.5% |  |
| BUILD_TUPLE | 57,006,381 | 1.0% | 78.5% |  |
| CONTAINS_OP | 52,227,497 | 0.9% | 79.4% |  |
| COMPARE_OP_INT | 51,179,107 | 0.9% | 80.2% | 1.1% |
| IS_OP | 47,986,795 | 0.8% | 81.0% |  |
| POP_JUMP_IF_NOT_NONE | 46,925,463 | 0.8% | 81.8% |  |
| SWAP | 45,313,666 | 0.8% | 82.6% |  |
| CALL_BUILTIN_FAST | 43,496,831 | 0.7% | 83.3% |  |
| CALL_BUILTIN_O | 39,889,248 | 0.7% | 84.0% | 6.7% |
| COMPARE_OP | 38,614,118 | 0.6% | 84.6% |  |
| BINARY_OP | 35,325,073 | 0.6% | 85.2% |  |
| FOR_ITER_TUPLE | 34,823,225 | 0.6% | 85.8% | 2.3% |
| NOP | 33,954,271 | 0.6% | 86.4% |  |
| BUILD_MAP | 33,796,727 | 0.6% | 86.9% |  |
| COPY_FREE_VARS | 31,801,736 | 0.5% | 87.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 31,285,480 | 0.5% | 88.0% | 0.4% |
| BINARY_SUBSCR_LIST_INT | 30,211,015 | 0.5% | 88.5% | 0.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 29,538,989 | 0.5% | 89.0% | 21.9% |
| CALL_LEN | 28,098,849 | 0.5% | 89.5% |  |
| CALL_FUNCTION_EX | 28,012,956 | 0.5% | 89.9% |  |
| LOAD_ATTR_PROPERTY | 28,006,799 | 0.5% | 90.4% | 14.7% |
| CALL | 25,350,421 | 0.4% | 90.8% |  |
| BINARY_SUBSCR | 24,215,073 | 0.4% | 91.2% |  |
| CALL_LIST_APPEND | 24,015,284 | 0.4% | 91.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,522,945 | 0.4% | 92.0% | 0.2% |
| DICT_MERGE | 23,272,258 | 0.4% | 92.4% |  |
| YIELD_VALUE | 23,250,559 | 0.4% | 92.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 23,187,701 | 0.4% | 93.2% | 63.1% |
| BUILD_LIST | 21,625,689 | 0.4% | 93.6% |  |
| EXTENDED_ARG | 21,416,872 | 0.4% | 93.9% |  |
| STORE_SUBSCR_LIST_INT | 20,342,153 | 0.3% | 94.3% |  |
| TO_BOOL_INT | 19,693,259 | 0.3% | 94.6% | 0.1% |
| LOAD_FAST_AND_CLEAR | 16,788,613 | 0.3% | 94.9% |  |
| CALL_TYPE_1 | 16,713,086 | 0.3% | 95.2% |  |
| COMPARE_OP_STR | 14,564,743 | 0.2% | 95.4% |  |
| RETURN_GENERATOR | 14,349,249 | 0.2% | 95.7% |  |
| MAKE_FUNCTION | 14,304,509 | 0.2% | 95.9% |  |
| BINARY_OP_ADD_INT | 12,977,818 | 0.2% | 96.1% |  |
| TO_BOOL | 12,924,987 | 0.2% | 96.3% |  |
| POP_JUMP_IF_NONE | 12,555,159 | 0.2% | 96.5% |  |
| FOR_ITER_RANGE | 12,132,066 | 0.2% | 96.7% |  |
| CALL_KW | 10,673,060 | 0.2% | 96.9% |  |
| SET_FUNCTION_ATTRIBUTE | 10,430,117 | 0.2% | 97.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 9,176,941 | 0.2% | 97.2% | 0.0% |
| CALL_BUILTIN_CLASS | 9,148,406 | 0.2% | 97.4% |  |
| STORE_ATTR_SLOT | 9,059,350 | 0.2% | 97.6% | 24.5% |
| BINARY_SUBSCR_TUPLE_INT | 8,996,150 | 0.2% | 97.7% | 0.1% |
| IMPORT_FROM | 8,954,222 | 0.2% | 97.9% |  |
| STORE_DEREF | 8,695,408 | 0.1% | 98.0% |  |
| MAP_ADD | 7,867,003 | 0.1% | 98.1% |  |
| IMPORT_NAME | 7,759,131 | 0.1% | 98.3% |  |
| LIST_APPEND | 6,188,368 | 0.1% | 98.4% |  |
| MAKE_CELL | 6,049,456 | 0.1% | 98.5% |  |
| JUMP_FORWARD | 5,989,539 | 0.1% | 98.6% |  |
| CALL_TUPLE_1 | 5,851,735 | 0.1% | 98.7% | 0.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,735,270 | 0.1% | 98.8% | 0.1% |
| STORE_FAST_LOAD_FAST | 5,345,751 | 0.1% | 98.9% |  |
| UNARY_NOT | 5,307,528 | 0.1% | 98.9% |  |
| COPY | 4,908,522 | 0.1% | 99.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 4,647,668 | 0.1% | 99.1% | 0.2% |
| CALL_PY_WITH_DEFAULTS | 4,597,648 | 0.1% | 99.2% | 0.7% |
| STORE_SUBSCR | 3,428,657 | 0.1% | 99.2% |  |
| STORE_ATTR_INSTANCE_VALUE | 3,358,893 | 0.1% | 99.3% | 0.0% |
| BINARY_SUBSCR_DICT | 3,348,676 | 0.1% | 99.4% |  |
| BINARY_OP_MULTIPLY_INT | 2,771,425 | 0.0% | 99.4% | 0.0% |
| TO_BOOL_NONE | 2,709,038 | 0.0% | 99.4% | 8.4% |
| BINARY_OP_SUBTRACT_INT | 2,486,023 | 0.0% | 99.5% |  |
| TO_BOOL_LIST | 2,302,247 | 0.0% | 99.5% | 0.5% |
| STORE_SUBSCR_DICT | 2,283,382 | 0.0% | 99.6% |  |
| LOAD_SUPER_ATTR_METHOD | 1,814,127 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,644,956 | 0.0% | 99.6% | 20.5% |
| UNPACK_SEQUENCE_TUPLE | 1,630,393 | 0.0% | 99.6% |  |
| LOAD_FAST_CHECK | 1,578,342 | 0.0% | 99.7% |  |
| LIST_EXTEND | 1,349,173 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 1,349,133 | 0.0% | 99.7% |  |
| DELETE_FAST | 1,302,220 | 0.0% | 99.7% |  |
| LOAD_ATTR_MODULE | 1,271,350 | 0.0% | 99.8% | 0.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,980 | 0.0% | 99.8% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,121,215 | 0.0% | 99.8% |  |
| SEND_GEN | 1,029,836 | 0.0% | 99.8% | 3.0% |
| CHECK_EXC_MATCH | 906,726 | 0.0% | 99.8% |  |
| POP_EXCEPT | 906,726 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 906,726 | 0.0% | 99.9% |  |
| UNARY_NEGATIVE | 613,339 | 0.0% | 99.9% |  |
| STORE_ATTR | 591,395 | 0.0% | 99.9% |  |
| BINARY_SLICE | 569,049 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 563,580 | 0.0% | 99.9% |  |
| COMPARE_OP_FLOAT | 543,647 | 0.0% | 99.9% | 0.3% |
| GET_YIELD_FROM_ITER | 540,416 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 519,760 | 0.0% | 99.9% |  |
| END_SEND | 519,360 | 0.0% | 99.9% |  |
| SEND | 442,840 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 284,520 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 284,480 | 0.0% | 100.0% |  |
| CALL_STR_1 | 233,240 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 228,374 | 0.0% | 100.0% | 36.3% |
| FOR_ITER_GEN | 191,368 | 0.0% | 100.0% | 0.2% |
| LOAD_ATTR_CLASS | 187,600 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 181,850 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_LIST | 180,068 | 0.0% | 100.0% |  |
| LOAD_NAME | 178,820 | 0.0% | 100.0% |  |
| STORE_NAME | 167,980 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 159,246 | 0.0% | 100.0% | 0.0% |
| BUILD_STRING | 141,900 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 129,250 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 119,090 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 95,920 | 0.0% | 100.0% | 0.2% |
| EXIT_INIT_CHECK | 95,600 | 0.0% | 100.0% |  |
| BUILD_SET | 50,426 | 0.0% | 100.0% |  |
| RESUME | 47,566 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 39,759 | 0.0% | 100.0% |  |
| BEFORE_WITH | 37,420 | 0.0% | 100.0% |  |
| END_FOR | 22,523 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 19,500 | 0.0% | 100.0% |  |
| SET_ADD | 19,280 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 5,980 | 0.0% | 100.0% |  |
| BUILD_SLICE | 4,008 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 3,100 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 2,660 | 0.0% | 100.0% |  |
| STORE_SLICE | 2,160 | 0.0% | 100.0% |  |
| RERAISE | 2,080 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,040 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,204 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 480 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 300 | 0.0% | 100.0% | 20.0% |
| DELETE_NAME | 120 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 60 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |
| DICT_UPDATE | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST | 196,230,653 | 3.3% | 3.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 162,956,827 | 2.7% | 6.0% |
| RESUME_CHECK LOAD_FAST | 115,572,942 | 1.9% | 8.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 113,688,069 | 1.9% | 9.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 111,606,481 | 1.9% | 11.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 99,388,010 | 1.7% | 13.4% |
| CACHE RESUME_CHECK | 99,362,607 | 1.7% | 15.1% |
| LOAD_FAST LOAD_ATTR_SLOT | 95,201,873 | 1.6% | 16.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 79,150,603 | 1.3% | 18.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 78,852,593 | 1.3% | 19.3% |
| RETURN_VALUE INTERPRETER_EXIT | 72,902,828 | 1.2% | 20.6% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 71,491,557 | 1.2% | 21.8% |
| LOAD_FAST LOAD_CONST | 69,885,090 | 1.2% | 22.9% |
| JUMP_BACKWARD FOR_ITER | 68,846,941 | 1.2% | 24.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 62,582,205 | 1.1% | 25.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 59,844,091 | 1.0% | 26.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 58,000,778 | 1.0% | 27.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 57,025,410 | 1.0% | 28.1% |
| LOAD_FAST LOAD_ATTR | 55,274,501 | 0.9% | 29.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 54,507,047 | 0.9% | 29.9% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 54,472,446 | 0.9% | 30.8% |
| LOAD_FAST RETURN_VALUE | 53,597,004 | 0.9% | 31.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 51,067,944 | 0.9% | 32.6% |
| PUSH_NULL LOAD_FAST | 46,546,836 | 0.8% | 33.4% |
| JUMP_BACKWARD FOR_ITER_LIST | 46,542,629 | 0.8% | 34.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 45,485,915 | 0.8% | 34.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT TO_BOOL_BOOL | 44,302,285 | 0.7% | 35.7% |
| FOR_ITER_LIST STORE_FAST | 43,132,740 | 0.7% | 36.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 42,210,968 | 0.7% | 37.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 41,993,365 | 0.7% | 37.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 41,290,269 | 0.7% | 38.5% |
| LOAD_CONST LOAD_CONST | 40,444,126 | 0.7% | 39.2% |
| RETURN_VALUE STORE_FAST | 38,558,098 | 0.6% | 39.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 38,054,916 | 0.6% | 40.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 37,717,711 | 0.6% | 41.1% |
| LOAD_ATTR STORE_FAST | 36,818,612 | 0.6% | 41.7% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 35,899,402 | 0.6% | 42.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 35,576,124 | 0.6% | 42.9% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 34,145,171 | 0.6% | 43.5% |
| LOAD_ATTR_SLOT RETURN_VALUE | 33,432,749 | 0.6% | 44.0% |
| RETURN_CONST INTERPRETER_EXIT | 32,283,305 | 0.5% | 44.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 31,861,750 | 0.5% | 45.1% |
| IS_OP POP_JUMP_IF_FALSE | 30,056,283 | 0.5% | 45.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 29,776,713 | 0.5% | 46.1% |
| POP_JUMP_IF_FALSE RETURN_CONST | 29,384,791 | 0.5% | 46.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 28,997,810 | 0.5% | 47.1% |
| LOAD_FAST PUSH_NULL | 28,426,428 | 0.5% | 47.6% |
| LOAD_FAST CALL_LEN | 27,057,561 | 0.5% | 48.0% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 27,007,153 | 0.5% | 48.5% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 26,484,027 | 0.4% | 48.9% |
| CONTAINS_OP POP_JUMP_IF_TRUE | 26,192,485 | 0.4% | 49.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 26,024,852 | 0.4% | 49.8% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 25,639,298 | 0.4% | 50.2% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 24,783,764 | 0.4% | 50.7% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 24,532,829 | 0.4% | 51.1% |
| POP_TOP JUMP_BACKWARD | 24,341,986 | 0.4% | 51.5% |
| LOAD_CONST CALL_BUILTIN_FAST | 24,272,173 | 0.4% | 51.9% |
| BINARY_OP STORE_FAST | 24,216,556 | 0.4% | 52.3% |
| FOR_ITER_TUPLE STORE_FAST | 23,957,318 | 0.4% | 52.7% |
| DICT_MERGE CALL_FUNCTION_EX | 23,272,258 | 0.4% | 53.1% |
| BUILD_MAP LOAD_FAST | 23,183,067 | 0.4% | 53.5% |
| LOAD_FAST DICT_MERGE | 23,143,352 | 0.4% | 53.9% |
| LOAD_DEREF LOAD_ATTR_METHOD_WITH_VALUES | 22,532,845 | 0.4% | 54.2% |
| LOAD_ATTR_SLOT STORE_FAST | 22,510,395 | 0.4% | 54.6% |
| YIELD_VALUE INTERPRETER_EXIT | 22,404,538 | 0.4% | 55.0% |
| STORE_FAST_STORE_FAST LOAD_DEREF | 22,363,782 | 0.4% | 55.4% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 22,270,503 | 0.4% | 55.8% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_BUILTIN | 22,035,221 | 0.4% | 56.1% |
| COPY_FREE_VARS RESUME_CHECK | 21,815,899 | 0.4% | 56.5% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 21,656,967 | 0.4% | 56.9% |
| LOAD_FAST GET_ITER | 21,641,725 | 0.4% | 57.2% |
| LOAD_FAST TO_BOOL_BOOL | 21,619,302 | 0.4% | 57.6% |
| POP_JUMP_IF_NOT_NONE JUMP_BACKWARD | 21,412,175 | 0.4% | 57.9% |
| RESUME_CHECK NOP | 21,364,165 | 0.4% | 58.3% |
| BUILD_TUPLE RETURN_VALUE | 21,221,339 | 0.4% | 58.7% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 21,088,732 | 0.4% | 59.0% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 21,016,241 | 0.4% | 59.4% |
| LOAD_CONST COMPARE_OP_INT | 20,986,375 | 0.4% | 59.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 20,512,263 | 0.3% | 60.1% |
| COMPARE_OP POP_JUMP_IF_FALSE | 20,133,398 | 0.3% | 60.4% |
| LOAD_ATTR CONTAINS_OP | 20,047,561 | 0.3% | 60.7% |
| GET_ITER FOR_ITER | 20,018,940 | 0.3% | 61.1% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 20,004,187 | 0.3% | 61.4% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 19,466,541 | 0.3% | 61.7% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 19,055,189 | 0.3% | 62.0% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 18,850,860 | 0.3% | 62.4% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 18,813,038 | 0.3% | 62.7% |
| LOAD_FAST TO_BOOL_INT | 18,366,681 | 0.3% | 63.0% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 18,333,566 | 0.3% | 63.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 18,254,977 | 0.3% | 63.6% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 18,103,288 | 0.3% | 63.9% |
| LOAD_FAST CALL_BUILTIN_O | 17,818,737 | 0.3% | 64.2% |
| CALL_LIST_APPEND JUMP_BACKWARD | 17,342,505 | 0.3% | 64.5% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 17,273,551 | 0.3% | 64.8% |
| LOAD_ATTR IS_OP | 17,248,597 | 0.3% | 65.1% |
| LOAD_FAST BUILD_TUPLE | 17,199,930 | 0.3% | 65.4% |
| LOAD_FAST CALL_TYPE_1 | 16,590,175 | 0.3% | 65.6% |
| LOAD_FAST CALL_LIST_APPEND | 16,418,890 | 0.3% | 65.9% |
| LOAD_ATTR LOAD_FAST | 16,038,970 | 0.3% | 66.2% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 16,027,782 | 0.3% | 66.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 535,689 | 94.1% |
| LOAD_FAST | 26,720 | 4.7% |
| BINARY_OP_ADD_INT | 6,320 | 1.1% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 319,620 | 56.2% |
| RETURN_VALUE | 93,840 | 16.5% |
| GET_ITER | 54,720 | 9.6% |
| BINARY_OP | 39,120 | 6.9% |
| STORE_FAST | 18,960 | 3.3% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,160 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,362,607 | 77.7% |
| POP_TOP | 13,900,259 | 10.9% |
| COPY_FREE_VARS | 13,004,196 | 10.2% |
| MAKE_CELL | 1,509,140 | 1.2% |
| RESUME | 18,059 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 14,265,456 | 58.9% |
| LOAD_DEREF | 6,404,584 | 26.4% |
| BUILD_TUPLE | 1,844,124 | 7.6% |
| LOAD_FAST | 1,313,083 | 5.4% |
| RETURN_VALUE | 152,428 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 7,046,740 | 29.1% |
| LOAD_FAST | 6,942,444 | 28.7% |
| RETURN_VALUE | 6,066,493 | 25.1% |
| GET_ITER | 922,102 | 3.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 922,062 | 3.8% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 667,836 | 73.7% |
| BUILD_TUPLE | 157,240 | 17.3% |
| LOAD_GLOBAL_MODULE | 79,310 | 8.7% |
| LOAD_FAST | 1,600 | 0.2% |
| LOAD_GLOBAL | 740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 906,566 | 100.0% |
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
| JUMP_BACKWARD | 1,200 | 38.7% |
| LOAD_FAST | 60 | 1.9% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 22,523 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,523 | 100.0% |


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
| CONVERT_VALUE | 284,480 | 100.0% |
| LOAD_FAST | 20 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 141,720 | 49.8% |
| LOAD_CONST | 108,280 | 38.1% |
| LOAD_FAST | 34,520 | 12.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,641,725 | 36.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,456,984 | 24.1% |
| CALL | 10,953,541 | 18.2% |
| RETURN_VALUE | 4,116,587 | 6.9% |
| CALL_BUILTIN_O | 2,591,122 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 20,018,940 | 33.3% |
| CALL_PY_EXACT_ARGS | 13,020,285 | 21.7% |
| FOR_ITER_TUPLE | 9,973,489 | 16.6% |
| LOAD_FAST_AND_CLEAR | 9,198,496 | 15.3% |
| FOR_ITER_LIST | 4,573,695 | 7.6% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 347,016 | 64.2% |
| BINARY_SUBSCR | 185,800 | 34.4% |
| RETURN_VALUE | 7,520 | 1.4% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540,416 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 72,902,828 | 57.1% |
| RETURN_CONST | 32,283,305 | 25.3% |
| YIELD_VALUE | 22,404,538 | 17.6% |
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
| LOAD_CONST | 14,304,509 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 10,428,577 | 72.9% |
| LOAD_GLOBAL_BUILTIN | 2,651,182 | 18.5% |
| STORE_FAST | 669,668 | 4.7% |
| LOAD_FAST | 459,286 | 3.2% |
| STORE_NAME | 33,580 | 0.2% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,364,165 | 62.9% |
| POP_JUMP_IF_TRUE | 4,184,047 | 12.3% |
| STORE_FAST | 3,935,150 | 11.6% |
| POP_JUMP_IF_FALSE | 1,913,383 | 5.6% |
| POP_TOP | 1,391,923 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,286,056 | 36.2% |
| LOAD_DEREF | 10,423,965 | 30.7% |
| LOAD_GLOBAL_MODULE | 6,494,871 | 19.1% |
| LOAD_CONST | 2,608,142 | 7.7% |
| LOAD_GLOBAL_BUILTIN | 1,215,617 | 3.6% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 414,851 | 45.8% |
| POP_TOP | 358,475 | 39.5% |
| STORE_FAST | 130,960 | 14.4% |
| COPY | 1,920 | 0.2% |
| STORE_SUBSCR_DICT | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 414,851 | 45.8% |
| EXTENDED_ARG | 201,310 | 22.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 159,225 | 17.6% |
| LOAD_FAST | 83,020 | 9.2% |
| RETURN_CONST | 45,040 | 5.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 15,271,099 | 24.6% |
| CACHE | 13,900,259 | 22.4% |
| RETURN_CONST | 9,464,400 | 15.3% |
| STORE_FAST | 5,839,023 | 9.4% |
| SWAP | 5,778,577 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 24,341,986 | 39.3% |
| RESUME_CHECK | 14,343,689 | 23.1% |
| LOAD_FAST | 7,272,516 | 11.7% |
| RETURN_VALUE | 5,302,377 | 8.6% |
| LOAD_CONST | 2,640,798 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 374,785 | 41.3% |
| BINARY_SUBSCR_DICT | 233,871 | 25.8% |
| RAISE_VARARGS | 115,270 | 12.7% |
| LOAD_ATTR | 95,500 | 10.5% |
| CALL_BUILTIN_CLASS | 38,500 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 788,496 | 87.0% |
| LOAD_GLOBAL_MODULE | 114,790 | 12.7% |
| LOAD_GLOBAL | 1,840 | 0.2% |
| LOAD_FAST | 1,600 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,426,428 | 46.8% |
| LOAD_ATTR | 14,956,602 | 24.6% |
| LOAD_DEREF | 11,928,958 | 19.6% |
| CALL_BUILTIN_FAST | 2,129,900 | 3.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,980 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,546,836 | 76.7% |
| LOAD_FAST_LOAD_FAST | 12,228,921 | 20.1% |
| LOAD_CONST | 1,723,720 | 2.8% |
| LOAD_DEREF | 128,568 | 0.2% |
| CALL | 35,600 | 0.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 9,905,151 | 69.0% |
| CALL_PY_EXACT_ARGS | 4,261,358 | 29.7% |
| CALL_PY_WITH_DEFAULTS | 163,640 | 1.1% |
| CALL_KW | 8,000 | 0.1% |
| CACHE | 7,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 10,209,752 | 71.2% |
| STORE_FAST | 2,660,379 | 18.5% |
| LOAD_FAST | 792,028 | 5.5% |
| GET_YIELD_FROM_ITER | 347,016 | 2.4% |
| CALL_BUILTIN_CLASS | 160,600 | 1.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,597,004 | 30.2% |
| LOAD_ATTR_SLOT | 33,432,749 | 18.8% |
| BUILD_TUPLE | 21,221,339 | 12.0% |
| RETURN_VALUE | 15,183,337 | 8.6% |
| CALL_BUILTIN_O | 11,433,059 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 72,902,828 | 41.1% |
| STORE_FAST | 38,558,098 | 21.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 19,466,541 | 11.0% |
| RETURN_VALUE | 15,183,337 | 8.6% |
| LOAD_FAST | 5,453,580 | 3.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,303,489 | 96.3% |
| BINARY_SUBSCR | 93,200 | 2.7% |
| LOAD_FAST_LOAD_FAST | 18,960 | 0.6% |
| SWAP | 5,960 | 0.2% |
| STORE_SUBSCR | 3,640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,290,409 | 96.0% |
| JUMP_BACKWARD | 116,380 | 3.4% |
| JUMP_FORWARD | 9,840 | 0.3% |
| STORE_SUBSCR | 3,640 | 0.1% |
| LOAD_FAST | 2,623 | 0.1% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 10,287,220 | 79.6% |
| LOAD_FAST | 2,207,926 | 17.1% |
| LOAD_GLOBAL_MODULE | 118,930 | 0.9% |
| LOAD_ATTR | 117,981 | 0.9% |
| RETURN_VALUE | 27,310 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,253,017 | 94.8% |
| POP_JUMP_IF_TRUE | 509,997 | 3.9% |
| UNARY_NOT | 84,101 | 0.7% |
| TO_BOOL_BOOL | 41,195 | 0.3% |
| TO_BOOL | 21,472 | 0.2% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 188,542 | 30.7% |
| LOAD_ATTR_SLOT | 117,470 | 19.2% |
| LOAD_ATTR | 107,040 | 17.5% |
| RETURN_VALUE | 106,160 | 17.3% |
| LOAD_FAST_LOAD_FAST | 50,678 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 131,967 | 21.5% |
| CALL_LIST_APPEND | 119,120 | 19.4% |
| LOAD_GLOBAL_MODULE | 106,842 | 17.4% |
| IS_OP | 106,160 | 17.3% |
| STORE_FAST | 58,058 | 9.5% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 3,442,685 | 64.9% |
| TO_BOOL_BOOL | 1,118,709 | 21.1% |
| TO_BOOL_LIST | 661,868 | 12.5% |
| TO_BOOL | 84,101 | 1.6% |
| TO_BOOL_INT | 165 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,529,452 | 66.5% |
| STORE_FAST | 882,746 | 16.6% |
| BUILD_MAP | 734,720 | 13.8% |
| COPY | 86,866 | 1.6% |
| LOAD_CONST | 68,084 | 1.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,766,511 | 33.3% |
| COMPARE_OP_INT | 6,308,780 | 17.9% |
| COMPARE_OP | 6,162,400 | 17.4% |
| CALL_TUPLE_1 | 4,707,369 | 13.3% |
| LOAD_FAST | 2,678,436 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,216,556 | 68.6% |
| RETURN_VALUE | 5,771,267 | 16.3% |
| BUILD_TUPLE | 1,556,880 | 4.4% |
| CALL_BUILTIN_O | 1,095,133 | 3.1% |
| LOAD_FAST | 857,871 | 2.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 129,250 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 126,470 | 97.8% |
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
| SWAP | 4,464,227 | 20.6% |
| POP_JUMP_IF_TRUE | 4,083,244 | 18.9% |
| STORE_FAST | 3,817,131 | 17.7% |
| LOAD_FAST | 2,312,058 | 10.7% |
| BINARY_SUBSCR_TUPLE_INT | 1,557,600 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,718,081 | 54.2% |
| SWAP | 4,464,227 | 20.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,294,388 | 10.6% |
| LOAD_FAST | 1,414,433 | 6.5% |
| BUILD_LIST | 748,353 | 3.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,167,552 | 36.0% |
| BUILD_TUPLE | 10,998,565 | 32.5% |
| SWAP | 4,716,269 | 14.0% |
| LOAD_CONST | 1,656,800 | 4.9% |
| RESUME_CHECK | 1,285,960 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,183,067 | 68.6% |
| SWAP | 4,716,269 | 14.0% |
| STORE_FAST | 3,331,875 | 9.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,561,360 | 4.6% |
| CALL_FUNCTION_EX | 734,880 | 2.2% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,346 | 64.1% |
| SWAP | 18,000 | 35.7% |
| BINARY_OP | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 32,346 | 64.1% |
| SWAP | 18,000 | 35.7% |
| STORE_FAST | 80 | 0.2% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,008 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_GETITEM | 3,840 | 95.8% |
| BINARY_SUBSCR | 168 | 4.2% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 141,720 | 99.9% |
| LOAD_CONST | 180 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 106,160 | 74.8% |
| LOAD_CONST | 16,000 | 11.3% |
| LOAD_FAST | 16,000 | 11.3% |
| LIST_APPEND | 3,420 | 2.4% |
| CALL | 300 | 0.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 25,639,298 | 45.0% |
| LOAD_FAST | 17,199,930 | 30.2% |
| LOAD_ATTR_SLOT | 5,042,334 | 8.8% |
| LOAD_ATTR | 3,034,625 | 5.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,484,120 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 21,221,339 | 37.2% |
| BUILD_MAP | 10,998,565 | 19.3% |
| LOAD_CONST | 10,451,523 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 4,707,169 | 8.3% |
| CALL_LIST_APPEND | 3,231,440 | 5.7% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,640,523 | 38.0% |
| LOAD_FAST | 7,185,351 | 28.3% |
| LOAD_ATTR | 3,067,163 | 12.1% |
| BINARY_OP_MULTIPLY_INT | 2,291,864 | 9.0% |
| LOAD_GLOBAL_BUILTIN | 1,572,931 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,953,541 | 43.2% |
| STORE_FAST | 5,657,944 | 22.3% |
| RETURN_VALUE | 4,394,705 | 17.3% |
| RESUME_CHECK | 1,060,865 | 4.2% |
| CALL_LIST_APPEND | 693,134 | 2.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 23,272,258 | 83.1% |
| LOAD_FAST | 2,317,522 | 8.3% |
| CALL_INTRINSIC_1 | 1,256,797 | 4.5% |
| BUILD_MAP | 734,880 | 2.6% |
| BINARY_OP | 201,680 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,600,701 | 45.0% |
| RESUME_CHECK | 11,673,526 | 41.7% |
| LOAD_FAST_LOAD_FAST | 1,561,000 | 5.6% |
| BUILD_TUPLE | 638,860 | 2.3% |
| SWAP | 480,160 | 1.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 1,347,913 | 99.9% |
| IMPORT_NAME | 1,060 | 0.1% |
| LIST_APPEND | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,256,797 | 93.2% |
| BUILD_MAP | 91,276 | 6.8% |
| POP_TOP | 1,060 | 0.1% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,673,060 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,493,087 | 88.9% |
| POP_TOP | 698,039 | 6.5% |
| COPY_FREE_VARS | 261,140 | 2.4% |
| RETURN_VALUE | 84,811 | 0.8% |
| STORE_FAST | 35,740 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 21,088,732 | 54.6% |
| LOAD_FAST | 8,338,426 | 21.6% |
| CALL_TYPE_1 | 5,882,665 | 15.2% |
| LOAD_GLOBAL_MODULE | 1,179,160 | 3.1% |
| LOAD_CONST | 950,558 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,133,398 | 52.1% |
| BINARY_OP | 6,162,400 | 16.0% |
| LOAD_FAST_LOAD_FAST | 6,162,320 | 16.0% |
| UNARY_NOT | 3,442,685 | 8.9% |
| POP_JUMP_IF_TRUE | 2,321,171 | 6.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 24,783,764 | 47.5% |
| LOAD_ATTR | 20,047,561 | 38.4% |
| LOAD_GLOBAL_MODULE | 5,290,120 | 10.1% |
| LOAD_DEREF | 1,536,480 | 2.9% |
| LOAD_CONST | 174,996 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 26,192,485 | 50.2% |
| POP_JUMP_IF_FALSE | 26,024,852 | 49.8% |
| STORE_FAST | 4,560 | 0.0% |
| EXTENDED_ARG | 4,480 | 0.0% |
| RETURN_VALUE | 960 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 170,080 | 59.8% |
| LOAD_FAST | 111,500 | 39.2% |
| STORE_FAST_LOAD_FAST | 2,520 | 0.9% |
| LOAD_GLOBAL_MODULE | 300 | 0.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 284,480 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,237,532 | 25.2% |
| COPY | 1,214,400 | 24.7% |
| LOAD_FAST_LOAD_FAST | 872,880 | 17.8% |
| CALL_ISINSTANCE | 525,020 | 10.7% |
| LOAD_CONST | 236,782 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,340,145 | 27.3% |
| COPY | 1,214,400 | 24.7% |
| BINARY_SUBSCR_LIST_INT | 1,208,120 | 24.6% |
| LOAD_ATTR_INSTANCE_VALUE | 956,400 | 19.5% |
| STORE_FAST_STORE_FAST | 55,582 | 1.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,004,196 | 40.9% |
| CALL_PY_EXACT_ARGS | 11,888,241 | 37.4% |
| LOAD_ATTR_PROPERTY | 5,061,251 | 15.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,202,666 | 3.8% |
| CALL_KW | 261,140 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,815,899 | 68.6% |
| RETURN_GENERATOR | 9,905,151 | 31.1% |
| MAKE_CELL | 78,500 | 0.2% |
| RESUME | 2,186 | 0.0% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,285,120 | 98.7% |
| POP_JUMP_IF_NONE | 15,920 | 1.2% |
| FOR_ITER_LIST | 880 | 0.1% |
| STORE_FAST | 160 | 0.0% |
| POP_TOP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 643,240 | 49.4% |
| BUILD_LIST | 642,560 | 49.3% |
| LOAD_FAST | 16,060 | 1.2% |
| LOAD_GLOBAL | 200 | 0.0% |
| RERAISE | 160 | 0.0% |


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 80 | 66.7% |
| POP_TOP | 20 | 16.7% |
| FOR_ITER | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_NAME | 80 | 66.7% |
| RETURN_CONST | 20 | 16.7% |
| BUILD_LIST | 20 | 16.7% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,143,352 | 99.4% |
| LOAD_DEREF | 128,906 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 23,272,258 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,678,893 | 26.5% |
| TO_BOOL_BOOL | 5,485,716 | 25.6% |
| CALL_LIST_APPEND | 4,571,168 | 21.3% |
| GET_ITER | 2,378,138 | 11.1% |
| COMPARE_OP_INT | 1,719,902 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,031,112 | 32.8% |
| JUMP_BACKWARD | 5,759,253 | 26.9% |
| FOR_ITER_LIST | 5,660,705 | 26.4% |
| FOR_ITER_TUPLE | 1,740,040 | 8.1% |
| FOR_ITER_RANGE | 642,400 | 3.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 68,846,941 | 66.0% |
| GET_ITER | 20,018,940 | 19.2% |
| SWAP | 7,638,701 | 7.3% |
| LOAD_FAST | 7,635,263 | 7.3% |
| FOR_ITER | 79,816 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 71,491,557 | 68.6% |
| STORE_FAST | 8,361,197 | 8.0% |
| SWAP | 7,602,929 | 7.3% |
| LOAD_FAST | 4,704,178 | 4.5% |
| RETURN_CONST | 4,697,715 | 4.5% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 7,757,611 | 86.6% |
| STORE_FAST | 982,369 | 11.0% |
| STORE_DEREF | 185,702 | 2.1% |
| STORE_NAME | 26,000 | 0.3% |
| EXTENDED_ARG | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,821,179 | 76.2% |
| STORE_DEREF | 2,092,443 | 23.4% |
| STORE_NAME | 38,060 | 0.4% |
| EXTENDED_ARG | 2,540 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,759,111 | 100.0% |
| EXTENDED_ARG | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 7,757,611 | 100.0% |
| CALL_INTRINSIC_1 | 1,060 | 0.0% |
| STORE_NAME | 440 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 17,248,597 | 35.9% |
| LOAD_FAST | 13,002,007 | 27.1% |
| LOAD_CONST | 10,976,172 | 22.9% |
| LOAD_FAST_LOAD_FAST | 5,893,574 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 539,795 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 30,056,283 | 62.6% |
| YIELD_VALUE | 12,986,667 | 27.1% |
| POP_JUMP_IF_TRUE | 4,906,541 | 10.2% |
| EXTENDED_ARG | 20,300 | 0.0% |
| STORE_FAST | 8,960 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 42,210,968 | 26.9% |
| POP_TOP | 24,341,986 | 15.5% |
| POP_JUMP_IF_NOT_NONE | 21,412,175 | 13.7% |
| CALL_LIST_APPEND | 17,342,505 | 11.1% |
| POP_JUMP_IF_FALSE | 14,897,713 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 68,846,941 | 43.9% |
| FOR_ITER_LIST | 46,542,629 | 29.7% |
| FOR_ITER_TUPLE | 22,270,503 | 14.2% |
| FOR_ITER_RANGE | 10,610,441 | 6.8% |
| EXTENDED_ARG | 5,678,893 | 3.6% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 928,400 | 82.8% |
| POP_EXCEPT | 159,225 | 14.2% |
| EXTENDED_ARG | 33,430 | 3.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 661,220 | 59.0% |
| SEND | 267,340 | 23.8% |
| LOAD_GLOBAL_BUILTIN | 120,110 | 10.7% |
| NOP | 35,535 | 3.2% |
| LOAD_FAST_LOAD_FAST | 17,960 | 1.6% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,278,220 | 71.4% |
| POP_TOP | 734,226 | 12.3% |
| STORE_FAST_STORE_FAST | 240,720 | 4.0% |
| CALL_LIST_APPEND | 191,818 | 3.2% |
| LOAD_FAST | 146,870 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,007,390 | 66.9% |
| BUILD_MAP | 721,820 | 12.1% |
| LOAD_GLOBAL_BUILTIN | 470,043 | 7.8% |
| LOAD_FAST_LOAD_FAST | 441,650 | 7.4% |
| STORE_FAST | 118,970 | 2.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,004,160 | 48.5% |
| BUILD_TUPLE | 1,568,828 | 25.4% |
| RETURN_VALUE | 511,481 | 8.3% |
| BINARY_SUBSCR | 489,428 | 7.9% |
| BINARY_SUBSCR_LIST_INT | 396,080 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,183,408 | 99.9% |
| LOAD_NAME | 4,800 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,347,033 | 99.8% |
| LOAD_CONST | 1,260 | 0.1% |
| LOAD_DEREF | 640 | 0.0% |
| LOAD_ATTR_SLOT | 200 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,347,913 | 99.9% |
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
| LOAD_GLOBAL_MODULE | 57,025,410 | 46.9% |
| LOAD_FAST | 55,274,501 | 45.4% |
| CALL_TYPE_1 | 4,209,322 | 3.5% |
| LOAD_ATTR_SLOT | 2,297,048 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 1,904,973 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 36,818,612 | 30.3% |
| CONTAINS_OP | 20,047,561 | 16.5% |
| IS_OP | 17,248,597 | 14.2% |
| LOAD_FAST | 16,038,970 | 13.2% |
| PUSH_NULL | 14,956,602 | 12.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 69,885,090 | 36.5% |
| LOAD_CONST | 40,444,126 | 21.1% |
| RESUME_CHECK | 15,734,421 | 8.2% |
| BUILD_TUPLE | 10,451,523 | 5.5% |
| RETURN_CONST | 9,526,680 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,444,126 | 21.1% |
| CALL_BUILTIN_FAST | 24,272,173 | 12.7% |
| COMPARE_OP_INT | 20,986,375 | 11.0% |
| STORE_FAST | 14,708,483 | 7.7% |
| MAKE_FUNCTION | 14,304,509 | 7.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 22,363,782 | 32.4% |
| NOP | 10,423,965 | 15.1% |
| LOAD_FAST | 7,794,211 | 11.3% |
| LOAD_ATTR_SLOT | 6,404,584 | 9.3% |
| POP_JUMP_IF_FALSE | 4,653,463 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 22,532,845 | 32.6% |
| PUSH_NULL | 11,928,958 | 17.3% |
| LOAD_FAST | 9,406,582 | 13.6% |
| CALL_ISINSTANCE | 7,549,303 | 10.9% |
| BINARY_SUBSCR | 6,404,584 | 9.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 196,230,653 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 162,956,827 | 16.7% |
| RESUME_CHECK | 115,572,942 | 11.8% |
| POP_JUMP_IF_FALSE | 113,688,069 | 11.6% |
| PUSH_NULL | 46,546,836 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 95,201,873 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 79,150,603 | 8.1% |
| LOAD_GLOBAL_MODULE | 78,852,593 | 8.1% |
| LOAD_CONST | 69,885,090 | 7.2% |
| LOAD_ATTR | 55,274,501 | 5.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,198,496 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,590,037 | 45.2% |
| MAKE_CELL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,198,416 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,590,037 | 45.2% |
| MAKE_CELL | 160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,557,060 | 98.7% |
| LOAD_FAST | 9,760 | 0.6% |
| POP_TOP | 7,360 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 2,980 | 0.2% |
| POP_JUMP_IF_FALSE | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 1,556,980 | 98.6% |
| COMPARE_OP_INT | 7,680 | 0.5% |
| POP_JUMP_IF_NOT_NONE | 7,360 | 0.5% |
| LOAD_FAST | 3,860 | 0.2% |
| CALL_BUILTIN_CLASS | 1,360 | 0.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,582,205 | 24.6% |
| POP_JUMP_IF_FALSE | 34,145,171 | 13.4% |
| LOAD_GLOBAL_BUILTIN | 28,997,810 | 11.4% |
| RESUME_CHECK | 20,004,187 | 7.9% |
| STORE_FAST_STORE_FAST | 15,653,121 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 27,007,153 | 10.6% |
| BUILD_TUPLE | 25,639,298 | 10.1% |
| CONTAINS_OP | 24,783,764 | 9.7% |
| COMPARE_OP | 21,088,732 | 8.3% |
| STORE_SUBSCR_LIST_INT | 18,850,860 | 7.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,227 | 19.4% |
| LOAD_FAST | 34,209 | 18.8% |
| STORE_FAST | 26,929 | 14.8% |
| RESUME_CHECK | 10,934 | 6.0% |
| RESUME | 10,783 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 50,540 | 27.8% |
| LOAD_GLOBAL_BUILTIN | 41,262 | 22.7% |
| LOAD_FAST | 39,596 | 21.8% |
| LOAD_ATTR | 14,080 | 7.7% |
| CALL | 9,831 | 5.4% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 46,040 | 25.7% |
| LOAD_NAME | 43,340 | 24.2% |
| POP_JUMP_IF_FALSE | 35,940 | 20.1% |
| JUMP_BACKWARD | 17,980 | 10.1% |
| CALL | 7,360 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 43,340 | 24.2% |
| CONTAINS_OP | 35,920 | 20.1% |
| PUSH_NULL | 22,600 | 12.6% |
| LOAD_CONST | 19,560 | 10.9% |
| LOAD_ATTR_METHOD_NO_DICT | 18,340 | 10.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,084 | 90.0% |
| LOAD_DEREF | 120 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 500 | 41.5% |
| CALL | 324 | 26.9% |
| LOAD_FAST | 180 | 15.0% |
| PUSH_NULL | 100 | 8.3% |
| LOAD_SUPER_ATTR_ATTR | 100 | 8.3% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,274,806 | 37.6% |
| CACHE | 1,509,140 | 24.9% |
| CALL_PY_EXACT_ARGS | 772,716 | 12.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 654,434 | 10.8% |
| CALL | 523,697 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,771,090 | 62.3% |
| MAKE_CELL | 2,274,806 | 37.6% |
| RESUME | 3,000 | 0.0% |
| RETURN_GENERATOR | 400 | 0.0% |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 7,853,843 | 99.8% |
| LOAD_FAST | 4,160 | 0.1% |
| RETURN_VALUE | 3,620 | 0.0% |
| CALL | 1,920 | 0.0% |
| STORE_FAST | 1,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,866,663 | 100.0% |
| LOAD_CONST | 320 | 0.0% |
| LOAD_NAME | 20 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 111,606,481 | 41.0% |
| COMPARE_OP_INT | 35,576,124 | 13.1% |
| IS_OP | 30,056,283 | 11.0% |
| CONTAINS_OP | 26,024,852 | 9.6% |
| COMPARE_OP | 20,133,398 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,688,069 | 41.7% |
| LOAD_GLOBAL_BUILTIN | 58,000,778 | 21.3% |
| LOAD_FAST_LOAD_FAST | 34,145,171 | 12.5% |
| RETURN_CONST | 29,384,791 | 10.8% |
| JUMP_BACKWARD | 14,897,713 | 5.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 7,046,740 | 56.1% |
| LOAD_FAST | 4,397,250 | 35.0% |
| LOAD_DEREF | 1,088,847 | 8.7% |
| LOAD_ATTR_INSTANCE_VALUE | 8,380 | 0.1% |
| EXTENDED_ARG | 6,802 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 7,053,891 | 56.2% |
| LOAD_FAST | 2,615,815 | 20.8% |
| LOAD_CONST | 1,111,425 | 8.9% |
| LOAD_GLOBAL_BUILTIN | 957,313 | 7.6% |
| NOP | 601,588 | 4.8% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,485,915 | 96.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,225,008 | 2.6% |
| EXTENDED_ARG | 179,780 | 0.4% |
| CALL_BUILTIN_FAST | 11,040 | 0.0% |
| LOAD_DEREF | 8,920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 21,412,175 | 45.6% |
| LOAD_FAST | 12,237,180 | 26.1% |
| LOAD_FAST_LOAD_FAST | 9,890,765 | 21.1% |
| LOAD_GLOBAL_MODULE | 1,880,247 | 4.0% |
| LOAD_GLOBAL_BUILTIN | 1,385,645 | 3.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 54,507,047 | 54.5% |
| CONTAINS_OP | 26,192,485 | 26.2% |
| TO_BOOL_INT | 9,135,808 | 9.1% |
| IS_OP | 4,906,541 | 4.9% |
| COMPARE_OP | 2,321,171 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 42,210,968 | 42.2% |
| LOAD_FAST | 38,054,916 | 38.0% |
| LOAD_GLOBAL_BUILTIN | 5,309,933 | 5.3% |
| NOP | 4,184,047 | 4.2% |
| BUILD_LIST | 4,083,244 | 4.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 118,930 | 99.9% |
| CALL_KW | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 115,270 | 98.4% |
| COPY | 1,760 | 1.5% |
| LOAD_CONST | 160 | 0.1% |


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

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 29,384,791 | 51.3% |
| RESUME_CHECK | 10,045,386 | 17.5% |
| FOR_ITER_LIST | 5,671,868 | 9.9% |
| FOR_ITER | 4,697,715 | 8.2% |
| STORE_SUBSCR | 3,290,409 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 32,283,305 | 56.3% |
| LOAD_CONST | 9,526,680 | 16.6% |
| POP_TOP | 9,464,400 | 16.5% |
| TO_BOOL_BOOL | 3,461,748 | 6.0% |
| STORE_FAST | 1,541,185 | 2.7% |


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
| LOAD_FAST | 17,200 | 89.2% |
| RETURN_VALUE | 2,040 | 10.6% |
| BINARY_SUBSCR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 19,280 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 10,428,577 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 1,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,832,375 | 94.3% |
| STORE_FAST | 307,032 | 2.9% |
| STORE_DEREF | 113,234 | 1.1% |
| LOAD_CONST | 52,360 | 0.5% |
| LOAD_GLOBAL_MODULE | 42,976 | 0.4% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 486,866 | 82.3% |
| LOAD_FAST | 98,460 | 16.6% |
| STORE_ATTR | 3,906 | 0.7% |
| SWAP | 2,151 | 0.4% |
| LOAD_DEREF | 12 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 289,676 | 49.0% |
| LOAD_FAST_LOAD_FAST | 116,270 | 19.7% |
| LOAD_FAST | 89,977 | 15.2% |
| LOAD_GLOBAL_BUILTIN | 74,060 | 12.5% |
| STORE_ATTR_INSTANCE_VALUE | 3,960 | 0.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 4,491,620 | 51.7% |
| IMPORT_FROM | 2,092,443 | 24.1% |
| LOAD_ATTR | 1,558,844 | 17.9% |
| STORE_FAST | 240,860 | 2.8% |
| SET_FUNCTION_ATTRIBUTE | 113,234 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,491,580 | 51.7% |
| POP_TOP | 1,906,741 | 21.9% |
| LOAD_DEREF | 1,298,346 | 14.9% |
| LOAD_GLOBAL_MODULE | 481,480 | 5.5% |
| IMPORT_FROM | 185,702 | 2.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 43,132,740 | 12.0% |
| RETURN_VALUE | 38,558,098 | 10.7% |
| LOAD_ATTR | 36,818,612 | 10.3% |
| BINARY_OP | 24,216,556 | 6.7% |
| FOR_ITER_TUPLE | 23,957,318 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 196,230,653 | 54.6% |
| LOAD_FAST_LOAD_FAST | 62,582,205 | 17.4% |
| LOAD_GLOBAL_BUILTIN | 37,717,711 | 10.5% |
| LOAD_GLOBAL_MODULE | 18,254,977 | 5.1% |
| STORE_FAST | 9,344,840 | 2.6% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,156,260 | 77.7% |
| FOR_ITER_TUPLE | 596,531 | 11.2% |
| FOR_ITER_RANGE | 500,000 | 9.4% |
| FOR_ITER | 92,960 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,303,754 | 80.5% |
| LOAD_ATTR_PROPERTY | 318,744 | 6.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 238,680 | 4.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 157,680 | 2.9% |
| LOAD_DEREF | 107,360 | 2.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 99,388,010 | 93.7% |
| RETURN_VALUE | 3,248,261 | 3.1% |
| UNPACK_SEQUENCE_TUPLE | 1,435,778 | 1.4% |
| STORE_FAST_STORE_FAST | 771,044 | 0.7% |
| BUILD_LIST | 413,120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,993,365 | 39.6% |
| LOAD_DEREF | 22,363,782 | 21.1% |
| LOAD_GLOBAL_BUILTIN | 22,035,221 | 20.8% |
| LOAD_FAST_LOAD_FAST | 15,653,121 | 14.8% |
| LOAD_GLOBAL_MODULE | 1,958,340 | 1.8% |


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

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 38,060 | 22.7% |
| MAKE_FUNCTION | 33,580 | 20.0% |
| STORE_NAME | 21,720 | 12.9% |
| CALL | 21,600 | 12.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 18,940 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,660 | 29.0% |
| LOAD_NAME | 46,040 | 27.4% |
| IMPORT_FROM | 26,000 | 15.5% |
| STORE_NAME | 21,720 | 12.9% |
| POP_TOP | 12,080 | 7.2% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 9,396,959 | 20.7% |
| LOAD_FAST_AND_CLEAR | 9,198,416 | 20.3% |
| FOR_ITER | 7,602,929 | 16.8% |
| BUILD_MAP | 4,716,269 | 10.4% |
| LOAD_FAST | 4,641,397 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,397,179 | 20.7% |
| STORE_FAST | 7,931,156 | 17.5% |
| FOR_ITER | 7,638,701 | 16.9% |
| POP_TOP | 5,778,577 | 12.8% |
| BUILD_MAP | 4,716,269 | 10.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,452 | 26.3% |
| FOR_ITER | 6,803 | 17.1% |
| CALL_BUILTIN_CLASS | 6,340 | 15.9% |
| LOAD_FAST | 3,970 | 10.0% |
| CALL_BUILTIN_FAST | 3,260 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 18,673 | 47.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,429 | 23.7% |
| STORE_FAST | 8,122 | 20.4% |
| UNPACK_SEQUENCE_TUPLE | 1,139 | 2.9% |
| UNPACK_SEQUENCE | 916 | 2.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 12,986,667 | 55.9% |
| CALL_ISINSTANCE | 6,945,827 | 29.9% |
| LOAD_FAST | 1,146,864 | 4.9% |
| YIELD_VALUE | 677,496 | 2.9% |
| RETURN_VALUE | 423,461 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 22,404,538 | 96.4% |
| YIELD_VALUE | 677,496 | 2.9% |
| STORE_FAST | 162,885 | 0.7% |
| UNPACK_SEQUENCE | 3,120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,520 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 18,059 | 38.0% |
| CALL | 11,109 | 23.4% |
| CALL_PY_EXACT_ARGS | 6,103 | 12.8% |
| POP_TOP | 3,960 | 8.3% |
| MAKE_CELL | 3,000 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,694 | 37.2% |
| LOAD_GLOBAL | 10,783 | 22.7% |
| LOAD_CONST | 8,763 | 18.4% |
| LOAD_NAME | 3,700 | 7.8% |
| POP_TOP | 3,360 | 7.1% |


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

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,827,352 | 91.1% |
| LOAD_FAST_LOAD_FAST | 573,568 | 4.4% |
| BINARY_SUBSCR_DICT | 422,960 | 3.3% |
| CALL_BUILTIN_CLASS | 81,090 | 0.6% |
| LOAD_FAST | 43,682 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 9,394,923 | 72.4% |
| STORE_FAST | 1,576,111 | 12.1% |
| SWAP | 1,085,051 | 8.4% |
| LOAD_CONST | 268,886 | 2.1% |
| LOAD_FAST | 201,363 | 1.6% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 480,720 | 85.3% |
| CALL_METHOD_DESCRIPTOR_O | 39,600 | 7.0% |
| LOAD_FAST | 21,480 | 3.8% |
| LOAD_FAST_LOAD_FAST | 13,440 | 2.4% |
| BINARY_SUBSCR_LIST_INT | 3,680 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 503,960 | 89.4% |
| RETURN_VALUE | 41,840 | 7.4% |
| CALL | 6,760 | 1.2% |
| LOAD_FAST | 6,720 | 1.2% |
| CALL_BUILTIN_FAST | 3,120 | 0.6% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,668,670 | 60.2% |
| LOAD_ATTR_SLOT | 723,516 | 26.1% |
| LOAD_FAST_LOAD_FAST | 283,402 | 10.2% |
| LOAD_FAST | 94,285 | 3.4% |
| BINARY_OP | 1,445 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,291,864 | 82.7% |
| LOAD_FAST_LOAD_FAST | 181,166 | 6.5% |
| STORE_FAST | 175,495 | 6.3% |
| LOAD_FAST | 90,186 | 3.3% |
| LOAD_GLOBAL_MODULE | 25,175 | 0.9% |


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
| LOAD_CONST | 1,568,869 | 63.1% |
| LOAD_FAST_LOAD_FAST | 606,649 | 24.4% |
| BINARY_SUBSCR_LIST_INT | 181,120 | 7.3% |
| LOAD_FAST | 123,228 | 5.0% |
| BINARY_OP | 2,184 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,082,420 | 43.5% |
| STORE_FAST | 709,813 | 28.6% |
| BINARY_OP | 311,556 | 12.5% |
| COMPARE_OP_INT | 184,120 | 7.4% |
| BINARY_SUBSCR_LIST_INT | 54,440 | 2.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,215,057 | 36.3% |
| LOAD_FAST_LOAD_FAST | 925,741 | 27.6% |
| LOAD_CONST | 642,800 | 19.2% |
| CALL_TUPLE_1 | 443,840 | 13.3% |
| RETURN_VALUE | 114,552 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 884,366 | 26.4% |
| RETURN_VALUE | 809,080 | 24.2% |
| BINARY_OP_ADD_INT | 422,960 | 12.6% |
| PUSH_NULL | 376,980 | 11.3% |
| SWAP | 318,100 | 9.5% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80,480 | 50.5% |
| BINARY_OP_ADD_INT | 59,680 | 37.5% |
| LOAD_CONST | 14,546 | 9.1% |
| BUILD_SLICE | 3,840 | 2.4% |
| BINARY_SUBSCR | 700 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 159,240 | 100.0% |
| RETURN_VALUE | 3 | 0.0% |
| LOAD_CONST | 3 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 27,007,153 | 89.4% |
| COPY | 1,208,120 | 4.0% |
| LOAD_CONST | 1,026,705 | 3.4% |
| LOAD_FAST | 570,274 | 1.9% |
| CALL_BUILTIN_CLASS | 282,223 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,459,659 | 31.3% |
| SWAP | 9,396,959 | 31.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,550,175 | 25.0% |
| LOAD_CONST | 1,208,580 | 4.0% |
| STORE_FAST | 517,143 | 1.7% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 18,880 | 96.8% |
| LOAD_FAST | 600 | 3.1% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 18,880 | 96.8% |
| LIST_APPEND | 620 | 3.2% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,729,563 | 97.0% |
| LOAD_FAST | 263,311 | 2.9% |
| BINARY_SUBSCR | 2,736 | 0.0% |
| LOAD_FAST_LOAD_FAST | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,738,616 | 52.7% |
| CALL_LIST_APPEND | 1,762,920 | 19.6% |
| BUILD_LIST | 1,557,600 | 17.3% |
| LOAD_FAST | 322,100 | 3.6% |
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
| LOAD_FAST | 13,333,799 | 56.7% |
| BINARY_OP_ADD_INT | 9,394,923 | 39.9% |
| LOAD_FAST_LOAD_FAST | 480,449 | 2.0% |
| LOAD_ATTR | 152,040 | 0.6% |
| LOAD_DEREF | 83,580 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,656,967 | 92.1% |
| COPY_FREE_VARS | 1,202,666 | 5.1% |
| MAKE_CELL | 654,434 | 2.8% |
| POP_TOP | 7,360 | 0.0% |
| CALL_PY_EXACT_ARGS | 718 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,821,402 | 30.8% |
| CALL_BUILTIN_CLASS | 1,959,412 | 21.4% |
| LOAD_GLOBAL_BUILTIN | 921,381 | 10.1% |
| LOAD_CONST | 710,920 | 7.8% |
| CALL_LEN | 611,123 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,419,435 | 37.4% |
| CALL_BUILTIN_CLASS | 1,959,412 | 21.4% |
| GET_ITER | 1,868,874 | 20.4% |
| BINARY_SUBSCR_LIST_INT | 282,223 | 3.1% |
| LOAD_FAST_LOAD_FAST | 243,269 | 2.7% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,272,173 | 55.8% |
| LOAD_FAST_LOAD_FAST | 17,273,551 | 39.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,337,294 | 3.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 1.1% |
| LOAD_FAST | 64,266 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 18,103,288 | 41.8% |
| STORE_FAST | 11,046,827 | 25.5% |
| TO_BOOL | 10,287,220 | 23.8% |
| PUSH_NULL | 2,129,900 | 4.9% |
| RETURN_VALUE | 1,500,172 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,891,169 | 85.3% |
| LOAD_FAST | 260,029 | 4.5% |
| CALL_BUILTIN_CLASS | 237,740 | 4.1% |
| BINARY_OP | 148,230 | 2.6% |
| LOAD_CONST | 124,290 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_TUPLE_1 | 4,707,169 | 82.1% |
| STORE_FAST | 315,417 | 5.5% |
| GET_ITER | 173,780 | 3.0% |
| RETURN_VALUE | 158,090 | 2.8% |
| LOAD_CONST | 128,550 | 2.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,818,737 | 44.7% |
| RETURN_GENERATOR | 10,209,752 | 25.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 5,612,356 | 14.1% |
| LOAD_ATTR_SLOT | 4,880,248 | 12.2% |
| BINARY_OP | 1,095,133 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,697,494 | 39.4% |
| RETURN_VALUE | 11,433,059 | 28.7% |
| TO_BOOL_BOOL | 9,911,726 | 24.8% |
| GET_ITER | 2,591,122 | 6.5% |
| LOAD_FAST | 50,620 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 35,899,402 | 53.2% |
| LOAD_GLOBAL_BUILTIN | 19,055,189 | 28.2% |
| LOAD_DEREF | 7,549,303 | 11.2% |
| LOAD_FAST_LOAD_FAST | 2,883,742 | 4.3% |
| LOAD_FAST | 1,621,128 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 59,844,091 | 88.7% |
| YIELD_VALUE | 6,945,827 | 10.3% |
| COPY | 525,020 | 0.8% |
| RETURN_VALUE | 127,535 | 0.2% |
| TO_BOOL | 9,664 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,057,561 | 96.3% |
| LOAD_GLOBAL_MODULE | 553,240 | 2.0% |
| BINARY_SUBSCR | 185,800 | 0.7% |
| RETURN_VALUE | 95,093 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 93,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 10,271,295 | 36.6% |
| LOAD_GLOBAL_BUILTIN | 9,677,000 | 34.4% |
| LOAD_CONST | 7,191,143 | 25.6% |
| CALL_BUILTIN_CLASS | 611,123 | 2.2% |
| STORE_FAST | 84,420 | 0.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,418,890 | 68.4% |
| BUILD_TUPLE | 3,231,440 | 13.5% |
| BINARY_SUBSCR_TUPLE_INT | 1,762,920 | 7.3% |
| LOAD_FAST_CHECK | 1,556,980 | 6.5% |
| CALL | 693,134 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,342,505 | 72.2% |
| EXTENDED_ARG | 4,571,168 | 19.0% |
| LOAD_FAST | 1,681,753 | 7.0% |
| LOAD_FAST_LOAD_FAST | 207,500 | 0.9% |
| JUMP_FORWARD | 191,818 | 0.8% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,352,261 | 66.2% |
| LOAD_CONST | 2,390,170 | 10.3% |
| BUILD_LIST | 2,294,388 | 9.9% |
| BUILD_MAP | 1,561,360 | 6.7% |
| BINARY_SUBSCR | 922,062 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,034,747 | 56.2% |
| STORE_FAST | 3,454,118 | 14.9% |
| LOAD_ATTR_METHOD_NO_DICT | 3,116,160 | 13.4% |
| POP_TOP | 1,833,585 | 7.9% |
| GET_ITER | 737,588 | 3.2% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,840 | 47.5% |
| LOAD_CONST | 2,220 | 37.1% |
| LOAD_FAST | 800 | 13.4% |
| CALL | 120 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,160 | 36.1% |
| STORE_FAST | 1,860 | 31.1% |
| GET_ITER | 880 | 14.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 680 | 11.4% |
| LOAD_ATTR_METHOD_NO_DICT | 220 | 3.7% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 24,532,829 | 83.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,807,729 | 16.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,791 | 0.4% |
| LOAD_ATTR | 72,820 | 0.2% |
| CALL | 3,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 14,456,984 | 48.9% |
| STORE_FAST | 9,689,483 | 32.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,891,169 | 16.6% |
| CALL_BUILTIN_CLASS | 169,811 | 0.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,791 | 0.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,853,920 | 61.4% |
| LOAD_CONST | 1,226,508 | 26.4% |
| LOAD_FAST | 353,960 | 7.6% |
| RETURN_VALUE | 97,600 | 2.1% |
| BUILD_LIST | 44,300 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,235,540 | 69.6% |
| LOAD_CONST | 1,224,508 | 26.3% |
| TO_BOOL_NONE | 104,000 | 2.2% |
| BINARY_OP_ADD_UNICODE | 39,600 | 0.9% |
| STORE_FAST | 25,520 | 0.5% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 21,016,241 | 30.8% |
| LOAD_FAST | 15,749,806 | 23.1% |
| LOAD_FAST_LOAD_FAST | 13,821,089 | 20.3% |
| GET_ITER | 13,020,285 | 19.1% |
| LOAD_SUPER_ATTR_METHOD | 1,539,381 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 51,067,944 | 74.9% |
| COPY_FREE_VARS | 11,888,241 | 17.4% |
| RETURN_GENERATOR | 4,261,358 | 6.2% |
| MAKE_CELL | 772,716 | 1.1% |
| CALL_PY_EXACT_ARGS | 144,892 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,105,004 | 45.8% |
| LOAD_FAST | 1,865,774 | 40.6% |
| RETURN_VALUE | 192,550 | 4.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 157,740 | 3.4% |
| LOAD_CONST | 80,430 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,379,651 | 95.3% |
| RETURN_GENERATOR | 163,640 | 3.6% |
| MAKE_CELL | 53,735 | 1.2% |
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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,707,169 | 80.4% |
| LOAD_FAST | 1,017,562 | 17.4% |
| STORE_FAST | 105,752 | 1.8% |
| RETURN_VALUE | 7,920 | 0.1% |
| LOAD_DEREF | 4,132 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 4,707,369 | 80.4% |
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
| LOAD_FAST | 16,590,175 | 99.3% |
| LOAD_CONST | 119,990 | 0.7% |
| LOAD_GLOBAL_MODULE | 1,840 | 0.0% |
| CALL | 1,081 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,423,791 | 38.4% |
| COMPARE_OP | 5,882,665 | 35.2% |
| LOAD_ATTR | 4,209,322 | 25.2% |
| IS_OP | 64,250 | 0.4% |
| BUILD_TUPLE | 55,800 | 0.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 493,450 | 90.8% |
| CALL_BUILTIN_CLASS | 25,400 | 4.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 21,817 | 4.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,840 | 0.3% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 542,047 | 99.7% |
| RETURN_VALUE | 1,580 | 0.3% |
| COMPARE_OP | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,986,375 | 41.0% |
| LOAD_FAST_LOAD_FAST | 18,333,566 | 35.8% |
| CALL_LEN | 10,271,295 | 20.1% |
| LOAD_FAST | 1,029,108 | 2.0% |
| LOAD_ATTR_SLOT | 225,490 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,576,124 | 69.5% |
| BINARY_OP | 6,308,780 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 4,738,660 | 9.3% |
| EXTENDED_ARG | 1,719,902 | 3.4% |
| LOAD_FAST_LOAD_FAST | 1,570,040 | 3.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,030,880 | 68.9% |
| LOAD_CONST | 4,335,572 | 29.8% |
| LOAD_GLOBAL_MODULE | 192,391 | 1.3% |
| LOAD_ATTR | 3,160 | 0.0% |
| LOAD_FAST | 2,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,480,603 | 99.4% |
| YIELD_VALUE | 79,760 | 0.5% |
| POP_JUMP_IF_TRUE | 3,520 | 0.0% |
| EXTENDED_ARG | 860 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 100,574 | 52.6% |
| GET_ITER | 90,694 | 47.4% |
| FOR_ITER | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,654 | 52.1% |
| POP_TOP | 90,534 | 47.3% |
| RESUME | 860 | 0.4% |
| STORE_FAST | 320 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 46,542,629 | 74.0% |
| EXTENDED_ARG | 5,660,705 | 9.0% |
| LOAD_FAST | 4,843,731 | 7.7% |
| GET_ITER | 4,573,695 | 7.3% |
| SWAP | 1,221,442 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,132,740 | 68.6% |
| RETURN_CONST | 5,671,868 | 9.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,710,451 | 7.5% |
| STORE_FAST_LOAD_FAST | 4,156,260 | 6.6% |
| LOAD_FAST | 4,094,062 | 6.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,610,441 | 87.5% |
| GET_ITER | 809,585 | 6.7% |
| EXTENDED_ARG | 642,400 | 5.3% |
| SWAP | 38,880 | 0.3% |
| LOAD_FAST | 29,360 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,761,181 | 88.7% |
| RETURN_CONST | 630,343 | 5.2% |
| STORE_FAST_LOAD_FAST | 500,000 | 4.1% |
| LOAD_FAST | 195,180 | 1.6% |
| SWAP | 38,520 | 0.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,270,503 | 64.0% |
| GET_ITER | 9,973,489 | 28.6% |
| EXTENDED_ARG | 1,740,040 | 5.0% |
| LOAD_FAST | 518,871 | 1.5% |
| SWAP | 299,473 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,957,318 | 68.8% |
| LOAD_FAST | 7,494,828 | 21.5% |
| RETURN_CONST | 789,080 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 710,592 | 2.0% |
| LOAD_GLOBAL_MODULE | 602,506 | 1.7% |


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
| LOAD_FAST | 5,501,590 | 60.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,694 | 11.6% |
| LOAD_DEREF | 1,058,154 | 11.5% |
| COPY | 956,400 | 10.4% |
| LOAD_GLOBAL_MODULE | 571,623 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,578,008 | 17.2% |
| CALL_BUILTIN_FAST | 1,337,294 | 14.6% |
| POP_JUMP_IF_NOT_NONE | 1,225,008 | 13.3% |
| STORE_FAST | 1,075,854 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,694 | 11.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,150,603 | 86.3% |
| RETURN_VALUE | 4,635,629 | 5.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,116,160 | 3.4% |
| LOAD_GLOBAL_MODULE | 1,983,553 | 2.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,578,008 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,861,750 | 34.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,532,829 | 26.7% |
| CALL_PY_EXACT_ARGS | 21,016,241 | 22.9% |
| LOAD_CONST | 4,054,832 | 4.4% |
| LOAD_DEREF | 3,320,104 | 3.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 22,532,845 | 72.0% |
| LOAD_ATTR_SLOT | 4,711,809 | 15.1% |
| LOAD_FAST | 3,706,419 | 11.8% |
| STORE_FAST_LOAD_FAST | 157,680 | 0.5% |
| LOAD_ATTR | 147,515 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,298,890 | 48.9% |
| LOAD_FAST_LOAD_FAST | 10,850,746 | 34.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,807,729 | 15.4% |
| CALL_PY_EXACT_ARGS | 313,535 | 1.0% |
| LOAD_CONST | 6,682 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,260,767 | 99.2% |
| LOAD_FAST | 5,540 | 0.4% |
| LOAD_ATTR_MODULE | 2,640 | 0.2% |
| LOAD_ATTR | 1,403 | 0.1% |
| LOAD_FAST_LOAD_FAST | 1,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,044,000 | 82.1% |
| CALL_PY_EXACT_ARGS | 80,590 | 6.3% |
| CALL | 57,380 | 4.5% |
| LOAD_FAST | 26,100 | 2.1% |
| LOAD_ATTR_SLOT | 15,920 | 1.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,472,446 | 92.5% |
| LOAD_DEREF | 3,109,100 | 5.3% |
| BINARY_SUBSCR_LIST_INT | 342,120 | 0.6% |
| STORE_FAST_LOAD_FAST | 238,680 | 0.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 236,946 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 44,302,285 | 75.3% |
| CALL_BUILTIN_O | 5,612,356 | 9.5% |
| BUILD_TUPLE | 2,484,120 | 4.2% |
| LOAD_FAST | 1,920,932 | 3.3% |
| BINARY_OP_MULTIPLY_INT | 1,668,670 | 2.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,001,393 | 60.9% |
| LOAD_FAST_LOAD_FAST | 478,940 | 29.1% |
| LOAD_DEREF | 144,340 | 8.8% |
| LOAD_ATTR | 12,020 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,897 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 478,200 | 29.1% |
| TO_BOOL_STR | 478,200 | 29.1% |
| TO_BOOL_BOOL | 409,375 | 24.9% |
| LOAD_CONST | 106,520 | 6.5% |
| CALL_LEN | 73,480 | 4.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,484,027 | 94.6% |
| RETURN_VALUE | 642,568 | 2.3% |
| STORE_FAST_LOAD_FAST | 318,744 | 1.1% |
| LOAD_DEREF | 217,206 | 0.8% |
| LOAD_FAST_LOAD_FAST | 168,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,813,038 | 67.2% |
| COPY_FREE_VARS | 5,061,251 | 18.1% |
| GET_ITER | 1,920,578 | 6.9% |
| TO_BOOL_BOOL | 729,198 | 2.6% |
| STORE_FAST | 506,129 | 1.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,201,873 | 99.1% |
| LOAD_ATTR_SLOT | 613,674 | 0.6% |
| LOAD_FAST_LOAD_FAST | 88,054 | 0.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 72,523 | 0.1% |
| STORE_FAST_LOAD_FAST | 21,598 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,432,749 | 34.8% |
| STORE_FAST | 22,510,395 | 23.4% |
| LOAD_DEREF | 6,404,584 | 6.7% |
| LOAD_FAST | 5,219,934 | 5.4% |
| LOAD_CONST | 5,210,174 | 5.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 58,000,778 | 24.8% |
| RESUME_CHECK | 41,290,269 | 17.7% |
| STORE_FAST | 37,717,711 | 16.1% |
| STORE_FAST_STORE_FAST | 22,035,221 | 9.4% |
| LOAD_FAST | 20,512,263 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,956,827 | 69.7% |
| LOAD_FAST_LOAD_FAST | 28,997,810 | 12.4% |
| CALL_ISINSTANCE | 19,055,189 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 9,010,252 | 3.9% |
| LOAD_DEREF | 3,365,421 | 1.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,852,593 | 54.1% |
| STORE_FAST | 18,254,977 | 12.5% |
| RESUME_CHECK | 16,027,782 | 11.0% |
| POP_JUMP_IF_FALSE | 9,667,099 | 6.6% |
| NOP | 6,494,871 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 57,025,410 | 39.1% |
| CALL_ISINSTANCE | 35,899,402 | 24.6% |
| LOAD_FAST | 29,776,713 | 20.4% |
| CONTAINS_OP | 5,290,120 | 3.6% |
| LOAD_FAST_LOAD_FAST | 3,332,877 | 2.3% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,104,580 | 93.5% |
| LOAD_DEREF | 77,300 | 6.5% |
| LOAD_SUPER_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,181,980 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,813,627 | 100.0% |
| LOAD_SUPER_ATTR | 500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,539,381 | 84.9% |
| LOAD_GLOBAL_MODULE | 172,246 | 9.5% |
| LOAD_FAST | 84,580 | 4.7% |
| LOAD_FAST_LOAD_FAST | 17,560 | 1.0% |
| CALL | 360 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 99,362,607 | 38.5% |
| CALL_PY_EXACT_ARGS | 51,067,944 | 19.8% |
| COPY_FREE_VARS | 21,815,899 | 8.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 21,656,967 | 8.4% |
| LOAD_ATTR_PROPERTY | 18,813,038 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 115,572,942 | 44.7% |
| LOAD_GLOBAL_BUILTIN | 41,290,269 | 16.0% |
| NOP | 21,364,165 | 8.3% |
| LOAD_FAST_LOAD_FAST | 20,004,187 | 7.7% |
| LOAD_GLOBAL_MODULE | 16,027,782 | 6.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 661,220 | 64.2% |
| LOAD_CONST | 367,996 | 35.7% |
| SEND | 620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 646,240 | 62.8% |
| POP_TOP | 352,936 | 34.3% |
| YIELD_VALUE | 15,060 | 1.5% |
| END_SEND | 15,020 | 1.5% |
| SEND | 580 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,103,802 | 62.6% |
| SWAP | 956,400 | 28.5% |
| LOAD_FAST_LOAD_FAST | 259,600 | 7.7% |
| LOAD_ATTR_SLOT | 35,131 | 1.0% |
| STORE_ATTR | 3,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,210,719 | 36.0% |
| RETURN_CONST | 887,408 | 26.4% |
| NOP | 480,100 | 14.3% |
| RETURN_VALUE | 478,260 | 14.2% |
| LOAD_FAST_LOAD_FAST | 122,720 | 3.7% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,731,999 | 52.2% |
| LOAD_FAST | 4,284,476 | 47.3% |
| STORE_ATTR_SLOT | 41,775 | 0.5% |
| STORE_ATTR | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,672,779 | 51.6% |
| LOAD_FAST_LOAD_FAST | 2,255,935 | 24.9% |
| LOAD_CONST | 1,890,546 | 20.9% |
| LOAD_GLOBAL_MODULE | 136,855 | 1.5% |
| RETURN_CONST | 45,660 | 0.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,574,091 | 68.9% |
| LOAD_FAST | 397,958 | 17.4% |
| CALL_TUPLE_1 | 181,360 | 7.9% |
| RETURN_VALUE | 82,840 | 3.6% |
| LOAD_CONST | 39,331 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,660,511 | 72.7% |
| EXTENDED_ARG | 226,738 | 9.9% |
| LOAD_FAST_LOAD_FAST | 184,960 | 8.1% |
| LOAD_FAST | 165,801 | 7.3% |
| LOAD_GLOBAL_MODULE | 38,951 | 1.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,850,860 | 92.7% |
| SWAP | 1,208,120 | 5.9% |
| BINARY_SUBSCR_DICT | 112,800 | 0.6% |
| LOAD_FAST | 99,413 | 0.5% |
| BINARY_OP_SUBTRACT_INT | 49,280 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,115,474 | 49.7% |
| LOAD_FAST_LOAD_FAST | 10,022,019 | 49.3% |
| LOAD_CONST | 160,200 | 0.8% |
| LOAD_FAST | 21,140 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 21,060 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,332 | 98.7% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| STORE_FAST_LOAD_FAST | 1,240 | 0.5% |
| TO_BOOL | 382 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 217,404 | 95.2% |
| POP_JUMP_IF_FALSE | 9,502 | 4.2% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| TO_BOOL | 48 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 59,844,091 | 34.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 44,302,285 | 25.6% |
| LOAD_FAST | 21,619,302 | 12.5% |
| CALL_BUILTIN_FAST | 18,103,288 | 10.5% |
| CALL_BUILTIN_O | 9,911,726 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 111,606,481 | 64.6% |
| POP_JUMP_IF_TRUE | 54,507,047 | 31.6% |
| EXTENDED_ARG | 5,485,716 | 3.2% |
| UNARY_NOT | 1,118,709 | 0.6% |
| TO_BOOL_NONE | 1,280 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,366,681 | 93.3% |
| BINARY_OP | 732,332 | 3.7% |
| BINARY_SUBSCR_LIST_INT | 485,260 | 2.5% |
| BINARY_SUBSCR_TUPLE_INT | 63,307 | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 24,846 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,556,820 | 53.6% |
| POP_JUMP_IF_TRUE | 9,135,808 | 46.4% |
| TO_BOOL_NONE | 440 | 0.0% |
| UNARY_NOT | 165 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,234,287 | 97.0% |
| COPY | 39,560 | 1.7% |
| LOAD_DEREF | 10,895 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 8,780 | 0.4% |
| STORE_FAST | 6,240 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 833,968 | 36.2% |
| POP_JUMP_IF_TRUE | 784,691 | 34.1% |
| UNARY_NOT | 661,868 | 28.7% |
| EXTENDED_ARG | 21,480 | 0.9% |
| TO_BOOL_NONE | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,841,630 | 68.0% |
| RETURN_VALUE | 389,261 | 14.4% |
| LOAD_ATTR_PROPERTY | 293,354 | 10.8% |
| CALL_METHOD_DESCRIPTOR_O | 104,000 | 3.8% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 41,976 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,944,316 | 71.8% |
| POP_JUMP_IF_TRUE | 745,642 | 27.5% |
| EXTENDED_ARG | 15,420 | 0.6% |
| TO_BOOL_BOOL | 1,680 | 0.1% |
| TO_BOOL | 1,500 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 92.0% |
| STORE_FAST_LOAD_FAST | 26,080 | 5.0% |
| LOAD_FAST | 13,080 | 2.5% |
| COPY | 2,120 | 0.4% |
| LOAD_GLOBAL_MODULE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 487,380 | 93.8% |
| POP_JUMP_IF_TRUE | 32,380 | 6.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120,308 | 66.8% |
| RETURN_VALUE | 49,120 | 27.3% |
| CALL_BUILTIN_CLASS | 2,600 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 1,880 | 1.0% |
| FOR_ITER_LIST | 1,880 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 114,940 | 63.8% |
| STORE_FAST_STORE_FAST | 65,128 | 36.2% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 884,420 | 54.2% |
| RETURN_VALUE | 660,894 | 40.5% |
| STORE_FAST | 79,520 | 4.9% |
| CALL_METHOD_DESCRIPTOR_O | 3,680 | 0.2% |
| UNPACK_SEQUENCE | 1,139 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,435,778 | 88.1% |
| STORE_FAST | 154,695 | 9.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 39,760 | 2.4% |
| STORE_DEREF | 120 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 71,491,557 | 68.6% |
| RETURN_VALUE | 19,466,541 | 18.7% |
| BINARY_SUBSCR_LIST_INT | 7,550,175 | 7.2% |
| FOR_ITER_LIST | 4,710,451 | 4.5% |
| FOR_ITER_TUPLE | 710,592 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 99,388,010 | 95.4% |
| STORE_DEREF | 4,491,620 | 4.3% |
| STORE_FAST | 257,705 | 0.2% |
| STORE_NAME | 18,940 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,680 | 0.0% |


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


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 35,267,090 | 65.2% |
|          hit | 18,801,606 | 34.7% |
|         miss | 120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,770 | 11.7% |
| Failure | 51,333 | 88.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 9,463 | 18.4% |
| multiply different types | 7,463 | 14.5% |
| subtract other | 6,800 | 13.2% |
| and int | 4,143 | 8.1% |
| rshift | 3,824 | 7.4% |
| or | 3,700 | 7.2% |
| power | 2,861 | 5.6% |
| true divide different types | 2,523 | 4.9% |
| multiply other | 2,360 | 4.6% |
| remainder | 2,313 | 4.5% |
| add different types | 1,939 | 3.8% |
| floor divide | 1,272 | 2.5% |
| subtract different types | 1,185 | 2.3% |
| xor | 583 | 1.1% |
| and other | 376 | 0.7% |
| true divide other | 300 | 0.6% |
| lshift | 225 | 0.4% |
| true divide float | 3 | 0.0% |


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
|     deferred | 24,234,616 | 36.2% |
|          hit | 42,689,028 | 63.8% |
|         miss | 45,559 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,356 | 32.1% |
| Failure | 17,660 | 67.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 12,237 | 69.3% |
| out of range | 3,640 | 20.6% |
| buffer int | 1,760 | 10.0% |
| array int | 20 | 0.1% |
| tuple slice | 3 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 56,285,149 | 12.7% |
|        deopt | 31,040 | 0.0% |
|          hit | 386,268,874 | 87.1% |
|         miss | 31,680,667 | 7.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 679,311 | 91.1% |
| Failure | 66,628 | 8.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass | 25,648 | 38.5% |
| code complex parameters | 14,052 | 21.1% |
| class no vectorcall | 9,220 | 13.8% |
| class mutable | 3,100 | 4.7% |
| other | 3,040 | 4.6% |
| wrong number arguments | 2,520 | 3.8% |
| cfunc noargs | 2,400 | 3.6% |
| bound method | 2,168 | 3.3% |
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
|     deferred | 39,100,271 | 37.3% |
|          hit | 65,711,510 | 62.6% |
|         miss | 575,987 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20,475 | 22.8% |
| Failure | 69,359 | 77.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 18,491 | 26.7% |
| other | 15,270 | 22.0% |
| different types | 12,239 | 17.6% |
| tuple | 10,054 | 14.5% |
| string | 9,960 | 14.4% |
| bool | 2,145 | 3.1% |
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
|     deferred | 105,660,083 | 49.3% |
|          hit | 108,460,160 | 50.6% |
|         miss | 1,547,417 | 0.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 41,065 | 29.7% |
| Failure | 97,076 | 70.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 68,817 | 70.9% |
| set | 9,110 | 9.4% |
| zip | 7,600 | 7.8% |
| enumerate | 4,229 | 4.4% |
| other | 2,720 | 2.8% |
| itertools | 1,940 | 2.0% |
| dict keys | 1,640 | 1.7% |
| reversed list | 860 | 0.9% |
| dict values | 80 | 0.1% |
| ascii string | 80 | 0.1% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 187,633,565 | 42.7% |
|        deopt | 20 | 0.0% |
|          hit | 250,751,976 | 57.0% |
|         miss | 67,439,415 | 15.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,350,195 | 89.4% |
| Failure | 160,124 | 10.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 60,835 | 38.0% |
| mutable class | 58,767 | 36.7% |
| method | 10,464 | 6.5% |
| has managed dict | 8,780 | 5.5% |
| overridden | 8,671 | 5.4% |
| shadowed | 5,300 | 3.3% |
| class method obj | 3,900 | 2.4% |
| builtin class method | 1,320 | 0.8% |
| not managed dict | 1,107 | 0.7% |
| non object slot | 560 | 0.3% |
| not in keys | 300 | 0.2% |
| non overriding descriptor | 60 | 0.0% |
| module attr not found | 60 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 110,308 | 0.0% |
|          hit | 379,576,544 | 99.9% |
|         miss | 20,420 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 91,962 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 604 | 0.0% |
|          hit | 2,996,107 | 100.0% |

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
|          hit | 999,176 | 67.8% |
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
|     deferred | 2,762,227 | 21.2% |
|          hit | 10,196,670 | 78.4% |
|         miss | 2,221,573 | 17.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 46,835 | 92.3% |
| Failure | 3,906 | 7.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 1,960 | 50.2% |
| not managed dict | 1,446 | 37.0% |
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
|     deferred | 3,422,295 | 13.1% |
|          hit | 22,625,535 | 86.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,722 | 42.8% |
| Failure | 3,640 | 57.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict subclass no override | 3,640 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,282,097 | 6.3% |
|          hit | 197,731,833 | 93.7% |
|         miss | 440,078 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 59,928 | 72.2% |
| Failure | 23,040 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 10,784 | 46.8% |
| number | 3,518 | 15.3% |
| mapping | 3,300 | 14.3% |
| dict | 2,340 | 10.2% |
| other | 1,627 | 7.1% |
| set | 1,431 | 6.2% |
| float | 40 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 27,595 | 0.0% |
|          hit | 105,971,696 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 11,388 | 93.6% |
| Failure | 776 | 6.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 716 | 92.3% |
| iterator | 60 | 7.7% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 3,225,031,561 | 54.1% |
| Not specialized | 799,643,644 | 13.4% |
| Specialized hits | 1,827,557,567 | 30.7% |
| Specialized misses | 104,001,896 | 1.7% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 187,633,565 | 40.1% |
| FOR_ITER | 105,660,083 | 22.6% |
| CALL | 56,285,149 | 12.0% |
| COMPARE_OP | 39,100,271 | 8.4% |
| BINARY_OP | 35,267,090 | 7.5% |
| BINARY_SUBSCR | 24,234,616 | 5.2% |
| TO_BOOL | 13,282,097 | 2.8% |
| STORE_SUBSCR | 3,422,295 | 0.7% |
| STORE_ATTR | 2,762,227 | 0.6% |
| SEND | 469,800 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 36,606,329 | 35.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 17,008,041 | 16.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 14,622,980 | 14.1% |
| LOAD_ATTR_METHOD_NO_DICT | 9,218,708 | 8.9% |
| CALL_PY_EXACT_ARGS | 7,821,242 | 7.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,479,480 | 6.2% |
| LOAD_ATTR_PROPERTY | 4,124,930 | 4.0% |
| CALL_BUILTIN_O | 2,661,168 | 2.6% |
| STORE_ATTR_SLOT | 2,220,593 | 2.1% |
| FOR_ITER_TUPLE | 784,437 | 0.8% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 127,802,001 | 46.9% |
| Calls to Python functions inlined | 144,887,071 | 53.1% |
| Calls via PyEval_EvalFrame (total) | 127,802,001 | 46.9% |
| Calls via PyEval_EvalFrame (vector) | 98,455,677 | 36.1% |
| Calls via PyEval_EvalFrame (generator) | 29,346,324 | 10.8% |
| Calls via PyEval_EvalFrame (legacy) | 4,640 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 98,448,377 | 36.1% |
| Calls via PyEval_EvalFrame (build class) | 2,660 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 23,668,323 | 8.7% |
| Calls via PyEval_EvalFrame (function ex) | 11,825,000 | 4.3% |
| Calls via PyEval_EvalFrame (api) | 53,328,443 | 19.6% |
| Calls via PyEval_EvalFrame (method) | 6,960 | 0.0% |
| Frame objects created | 1,287,392 | 0.5% |
| Frames pushed | 112,647,504 | 41.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 362,928,040 | 54.3% |
| Frees to freelist | 363,171,064 |  |
| Allocations | 305,118,507 | 45.7% |
| Allocations to 512 bytes | 304,054,799 | 45.5% |
| Allocations to 4 kbytes | 1,039,248 | 0.2% |
| Allocations over 4 kbytes | 24,460 | 0.0% |
| Frees | 312,804,442 |  |
| New values | 1,057,445 |  |
| Interpreter increfs | 2,570,558,119 | 64.2% |
| Interpreter decrefs | 2,996,277,125 | 65.4% |
| Increfs | 1,431,010,926 | 35.8% |
| Decrefs | 1,585,096,777 | 34.6% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 60 | 0.0% |
| Method cache hits | 243,204,423 |  |
| Method cache misses | 4,305,656 |  |
| Method cache collisions | 6,936,874 |  |
| Method cache dunder hits | 346,099,059 |  |
| Method cache dunder misses | 2,631,752 |  |


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
| Optimization attempts | 0 |  |
| Traces created | 0 |  |
| Trace stack overflow | 0 |  |
| Trace stack underflow | 0 |  |
| Trace too long | 0 |  |
| Trace too short | 0 |  |
| Inner loop found | 0 |  |
| Recursive call | 0 |  |
| Low confidence | 0 |  |
| Traces executed | 0 |  |
| Uops executed | 0 |  |

### Trace length histogram

<details>
<summary> trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 |  |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 |  |


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
| watched dict modification | 0 |
| watched globals modification | 0 |


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
