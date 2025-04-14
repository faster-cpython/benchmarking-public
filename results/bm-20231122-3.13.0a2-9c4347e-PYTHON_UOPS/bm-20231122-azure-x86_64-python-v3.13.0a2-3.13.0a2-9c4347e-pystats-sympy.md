
# Pystats results

- benchmark: sympy
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 976,648,062 | 16.4% | 16.4% |  |
| STORE_FAST | 358,998,486 | 6.0% | 22.4% |  |
| POP_JUMP_IF_FALSE | 291,821,688 | 4.9% | 27.3% |  |
| RESUME_CHECK | 258,035,111 | 4.3% | 31.7% |  |
| LOAD_FAST_LOAD_FAST | 254,015,743 | 4.3% | 36.0% |  |
| LOAD_GLOBAL_BUILTIN | 233,830,574 | 3.9% | 39.9% | 0.0% |
| LOAD_CONST | 191,414,273 | 3.2% | 43.1% |  |
| RETURN_VALUE | 177,399,999 | 3.0% | 46.1% |  |
| TO_BOOL_BOOL | 172,701,950 | 2.9% | 49.0% | 0.1% |
| JUMP_BACKWARD | 156,666,742 | 2.6% | 51.6% |  |
| LOAD_GLOBAL_MODULE | 145,736,673 | 2.4% | 54.1% | 0.0% |
| INTERPRETER_EXIT | 127,408,188 | 2.1% | 56.2% |  |
| LOAD_ATTR | 121,711,051 | 2.0% | 58.2% |  |
| STORE_FAST_STORE_FAST | 105,852,861 | 1.8% | 60.0% |  |
| FOR_ITER | 103,972,069 | 1.7% | 61.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 103,899,929 | 1.7% | 63.5% |  |
| LOAD_ATTR_SLOT | 96,029,928 | 1.6% | 65.1% | 38.1% |
| LOAD_ATTR_METHOD_NO_DICT | 91,686,148 | 1.5% | 66.7% | 10.1% |
| POP_JUMP_IF_TRUE | 80,547,567 | 1.4% | 68.0% |  |
| LOAD_DEREF | 68,791,142 | 1.2% | 69.2% |  |
| CALL_PY_EXACT_ARGS | 68,120,647 | 1.1% | 70.3% | 11.5% |
| CALL_ISINSTANCE | 67,455,978 | 1.1% | 71.5% |  |
| FOR_ITER_LIST | 62,863,126 | 1.1% | 72.5% | 1.2% |
| POP_TOP | 61,719,547 | 1.0% | 73.6% |  |
| PUSH_NULL | 60,691,443 | 1.0% | 74.6% |  |
| GET_ITER | 60,049,799 | 1.0% | 75.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 58,856,811 | 1.0% | 76.6% | 28.9% |
| RETURN_CONST | 57,268,127 | 1.0% | 77.5% |  |
| BUILD_TUPLE | 56,982,173 | 1.0% | 78.5% |  |
| CONTAINS_OP | 52,163,645 | 0.9% | 79.4% |  |
| COMPARE_OP_INT | 51,165,700 | 0.9% | 80.2% | 1.1% |
| IS_OP | 47,802,716 | 0.8% | 81.0% |  |
| SWAP | 45,303,473 | 0.8% | 81.8% |  |
| CALL_BUILTIN_FAST | 43,494,544 | 0.7% | 82.5% |  |
| POP_JUMP_IF_NONE | 41,250,346 | 0.7% | 83.2% |  |
| CALL_BUILTIN_O | 39,863,330 | 0.7% | 83.9% | 6.7% |
| COMPARE_OP | 38,558,750 | 0.6% | 84.5% |  |
| BINARY_OP | 35,325,669 | 0.6% | 85.1% |  |
| FOR_ITER_TUPLE | 34,819,672 | 0.6% | 85.7% | 2.3% |
| BUILD_MAP | 33,796,119 | 0.6% | 86.3% |  |
| NOP | 33,470,024 | 0.6% | 86.8% |  |
| COPY_FREE_VARS | 31,787,274 | 0.5% | 87.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 31,050,333 | 0.5% | 87.9% | 0.4% |
| BINARY_SUBSCR_LIST_INT | 30,184,308 | 0.5% | 88.4% | 0.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 29,530,802 | 0.5% | 88.9% | 21.9% |
| CALL_LEN | 28,097,232 | 0.5% | 89.4% |  |
| CALL_FUNCTION_EX | 28,011,869 | 0.5% | 89.8% |  |
| LOAD_ATTR_PROPERTY | 28,004,251 | 0.5% | 90.3% | 14.7% |
| CALL | 26,849,296 | 0.5% | 90.8% |  |
| BINARY_SUBSCR | 24,095,676 | 0.4% | 91.2% |  |
| CALL_LIST_APPEND | 24,015,446 | 0.4% | 91.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,514,824 | 0.4% | 92.0% | 0.2% |
| DICT_MERGE | 23,271,983 | 0.4% | 92.4% |  |
| YIELD_VALUE | 23,066,855 | 0.4% | 92.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 22,070,559 | 0.4% | 93.1% | 65.4% |
| BUILD_LIST | 21,624,739 | 0.4% | 93.5% |  |
| EXTENDED_ARG | 21,423,188 | 0.4% | 93.8% |  |
| STORE_SUBSCR_LIST_INT | 20,326,813 | 0.3% | 94.2% |  |
| TO_BOOL_INT | 19,694,702 | 0.3% | 94.5% | 0.1% |
| POP_JUMP_IF_NOT_NONE | 18,156,267 | 0.3% | 94.8% |  |
| LOAD_FAST_AND_CLEAR | 16,787,537 | 0.3% | 95.1% |  |
| CALL_TYPE_1 | 16,711,679 | 0.3% | 95.4% |  |
| COMPARE_OP_STR | 14,564,591 | 0.2% | 95.6% |  |
| RETURN_GENERATOR | 14,336,773 | 0.2% | 95.9% |  |
| MAKE_FUNCTION | 14,292,042 | 0.2% | 96.1% |  |
| BINARY_OP_ADD_INT | 12,970,696 | 0.2% | 96.3% |  |
| TO_BOOL | 12,924,789 | 0.2% | 96.5% |  |
| FOR_ITER_RANGE | 12,123,885 | 0.2% | 96.8% |  |
| CALL_KW | 10,672,348 | 0.2% | 96.9% |  |
| SET_FUNCTION_ATTRIBUTE | 10,418,108 | 0.2% | 97.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 9,175,739 | 0.2% | 97.3% | 0.0% |
| CALL_BUILTIN_CLASS | 9,146,734 | 0.2% | 97.4% |  |
| STORE_ATTR_SLOT | 9,059,031 | 0.2% | 97.6% | 24.5% |
| BINARY_SUBSCR_TUPLE_INT | 8,995,555 | 0.2% | 97.7% | 0.1% |
| IMPORT_FROM | 8,953,552 | 0.2% | 97.9% |  |
| STORE_DEREF | 8,694,902 | 0.1% | 98.0% |  |
| MAP_ADD | 7,865,707 | 0.1% | 98.1% |  |
| IMPORT_NAME | 7,758,646 | 0.1% | 98.3% |  |
| LIST_APPEND | 6,187,687 | 0.1% | 98.4% |  |
| MAKE_CELL | 6,048,386 | 0.1% | 98.5% |  |
| JUMP_FORWARD | 5,902,424 | 0.1% | 98.6% |  |
| CALL_TUPLE_1 | 5,851,436 | 0.1% | 98.7% | 0.0% |
| STORE_FAST_LOAD_FAST | 5,344,793 | 0.1% | 98.8% |  |
| UNARY_NOT | 5,307,389 | 0.1% | 98.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,171,575 | 0.1% | 98.9% | 0.1% |
| COPY | 4,908,229 | 0.1% | 99.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 4,647,578 | 0.1% | 99.1% | 0.2% |
| CALL_PY_WITH_DEFAULTS | 4,597,574 | 0.1% | 99.2% | 0.7% |
| STORE_SUBSCR | 3,428,065 | 0.1% | 99.2% |  |
| STORE_ATTR_INSTANCE_VALUE | 3,358,541 | 0.1% | 99.3% | 0.0% |
| BINARY_SUBSCR_DICT | 3,348,254 | 0.1% | 99.4% |  |
| BINARY_OP_MULTIPLY_INT | 2,771,489 | 0.0% | 99.4% | 0.0% |
| TO_BOOL_NONE | 2,707,927 | 0.0% | 99.4% | 8.4% |
| BINARY_OP_SUBTRACT_INT | 2,486,465 | 0.0% | 99.5% |  |
| TO_BOOL_LIST | 2,302,169 | 0.0% | 99.5% | 0.5% |
| STORE_SUBSCR_DICT | 2,283,374 | 0.0% | 99.6% |  |
| LOAD_SUPER_ATTR_METHOD | 1,814,122 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,647,574 | 0.0% | 99.6% | 20.6% |
| UNPACK_SEQUENCE_TUPLE | 1,630,785 | 0.0% | 99.7% |  |
| LOAD_FAST_CHECK | 1,578,319 | 0.0% | 99.7% |  |
| LIST_EXTEND | 1,348,893 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 1,348,853 | 0.0% | 99.7% |  |
| DELETE_FAST | 1,302,220 | 0.0% | 99.7% |  |
| LOAD_ATTR_MODULE | 1,271,598 | 0.0% | 99.8% | 0.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,848 | 0.0% | 99.8% |  |
| SEND_GEN | 1,029,740 | 0.0% | 99.8% | 3.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 928,560 | 0.0% | 99.8% |  |
| CHECK_EXC_MATCH | 906,024 | 0.0% | 99.8% |  |
| POP_EXCEPT | 906,024 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 906,024 | 0.0% | 99.9% |  |
| UNARY_NEGATIVE | 613,158 | 0.0% | 99.9% |  |
| STORE_ATTR | 591,283 | 0.0% | 99.9% |  |
| BINARY_SLICE | 568,946 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 563,580 | 0.0% | 99.9% |  |
| COMPARE_OP_FLOAT | 543,573 | 0.0% | 99.9% | 0.3% |
| GET_YIELD_FROM_ITER | 540,320 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 519,760 | 0.0% | 99.9% |  |
| END_SEND | 519,360 | 0.0% | 99.9% |  |
| SEND | 442,840 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 284,520 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 284,480 | 0.0% | 100.0% |  |
| CALL_STR_1 | 233,240 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 228,460 | 0.0% | 100.0% | 36.3% |
| FOR_ITER_GEN | 191,208 | 0.0% | 100.0% | 0.2% |
| LOAD_ATTR_CLASS | 187,600 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 181,811 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_LIST | 180,052 | 0.0% | 100.0% |  |
| LOAD_NAME | 178,820 | 0.0% | 100.0% |  |
| STORE_NAME | 167,980 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 159,240 | 0.0% | 100.0% | 0.0% |
| BUILD_STRING | 141,900 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 129,301 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 119,038 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 95,920 | 0.0% | 100.0% | 0.2% |
| EXIT_INIT_CHECK | 95,600 | 0.0% | 100.0% |  |
| BUILD_SET | 50,253 | 0.0% | 100.0% |  |
| RESUME | 47,564 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 39,643 | 0.0% | 100.0% |  |
| BEFORE_WITH | 37,420 | 0.0% | 100.0% |  |
| END_FOR | 22,507 | 0.0% | 100.0% |  |
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
| STORE_FAST LOAD_FAST | 196,202,666 | 3.3% | 3.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 162,937,836 | 2.7% | 6.0% |
| RESUME_CHECK LOAD_FAST | 115,548,335 | 1.9% | 8.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 113,710,993 | 1.9% | 9.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 111,640,595 | 1.9% | 11.8% |
| CACHE RESUME_CHECK | 99,186,466 | 1.7% | 13.4% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 99,126,782 | 1.7% | 15.1% |
| LOAD_FAST LOAD_ATTR_SLOT | 95,196,531 | 1.6% | 16.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 79,135,103 | 1.3% | 18.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 78,851,505 | 1.3% | 19.4% |
| RETURN_VALUE INTERPRETER_EXIT | 72,897,579 | 1.2% | 20.6% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 71,232,970 | 1.2% | 21.8% |
| LOAD_FAST LOAD_CONST | 69,874,990 | 1.2% | 22.9% |
| JUMP_BACKWARD FOR_ITER | 68,588,606 | 1.2% | 24.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 62,539,746 | 1.1% | 25.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 59,841,461 | 1.0% | 26.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 57,999,739 | 1.0% | 27.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 57,024,374 | 1.0% | 28.1% |
| LOAD_FAST LOAD_ATTR | 55,265,410 | 0.9% | 29.0% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 54,467,943 | 0.9% | 29.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 54,455,607 | 0.9% | 30.8% |
| LOAD_FAST RETURN_VALUE | 53,587,460 | 0.9% | 31.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 51,008,736 | 0.9% | 32.6% |
| JUMP_BACKWARD FOR_ITER_LIST | 46,543,233 | 0.8% | 33.4% |
| PUSH_NULL LOAD_FAST | 46,522,511 | 0.8% | 34.2% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 45,412,322 | 0.8% | 34.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT TO_BOOL_BOOL | 44,300,805 | 0.7% | 35.7% |
| FOR_ITER_LIST STORE_FAST | 43,123,895 | 0.7% | 36.4% |
| STORE_FAST_STORE_FAST LOAD_FAST | 41,979,900 | 0.7% | 37.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 41,287,385 | 0.7% | 37.8% |
| LOAD_CONST LOAD_CONST | 40,441,633 | 0.7% | 38.5% |
| RETURN_VALUE STORE_FAST | 38,550,703 | 0.6% | 39.1% |
| POP_JUMP_IF_TRUE LOAD_FAST | 38,015,324 | 0.6% | 39.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 37,716,082 | 0.6% | 40.4% |
| LOAD_ATTR STORE_FAST | 36,810,358 | 0.6% | 41.0% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 35,897,553 | 0.6% | 41.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 35,523,327 | 0.6% | 42.2% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 34,387,291 | 0.6% | 42.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 34,094,570 | 0.6% | 43.4% |
| LOAD_ATTR_SLOT RETURN_VALUE | 33,431,216 | 0.6% | 43.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 33,145,361 | 0.6% | 44.5% |
| RETURN_CONST INTERPRETER_EXIT | 32,281,795 | 0.5% | 45.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 31,844,480 | 0.5% | 45.6% |
| IS_OP POP_JUMP_IF_FALSE | 30,047,270 | 0.5% | 46.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 29,774,772 | 0.5% | 46.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 29,331,468 | 0.5% | 47.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 28,996,857 | 0.5% | 47.6% |
| LOAD_FAST PUSH_NULL | 28,402,865 | 0.5% | 48.0% |
| LOAD_FAST CALL_LEN | 27,056,087 | 0.5% | 48.5% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 26,980,339 | 0.5% | 48.9% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 26,481,076 | 0.4% | 49.4% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 25,639,424 | 0.4% | 49.8% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 24,720,227 | 0.4% | 50.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 24,524,903 | 0.4% | 50.6% |
| LOAD_CONST CALL_BUILTIN_FAST | 24,270,760 | 0.4% | 51.0% |
| BINARY_OP STORE_FAST | 24,216,741 | 0.4% | 51.5% |
| POP_TOP JUMP_BACKWARD | 24,111,868 | 0.4% | 51.9% |
| FOR_ITER_TUPLE STORE_FAST | 23,956,122 | 0.4% | 52.3% |
| DICT_MERGE CALL_FUNCTION_EX | 23,271,983 | 0.4% | 52.7% |
| BUILD_MAP LOAD_FAST | 23,182,782 | 0.4% | 53.0% |
| LOAD_FAST DICT_MERGE | 23,143,083 | 0.4% | 53.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 22,700,490 | 0.4% | 53.8% |
| LOAD_ATTR_SLOT STORE_FAST | 22,509,317 | 0.4% | 54.2% |
| LOAD_DEREF LOAD_ATTR_METHOD_WITH_VALUES | 22,297,414 | 0.4% | 54.6% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 22,268,260 | 0.4% | 54.9% |
| YIELD_VALUE INTERPRETER_EXIT | 22,221,074 | 0.4% | 55.3% |
| STORE_FAST_STORE_FAST LOAD_DEREF | 22,128,669 | 0.4% | 55.7% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_BUILTIN | 22,022,759 | 0.4% | 56.1% |
| COPY_FREE_VARS RESUME_CHECK | 21,813,248 | 0.4% | 56.4% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 21,649,219 | 0.4% | 56.8% |
| LOAD_FAST GET_ITER | 21,629,155 | 0.4% | 57.2% |
| LOAD_FAST TO_BOOL_BOOL | 21,618,755 | 0.4% | 57.5% |
| RESUME_CHECK NOP | 21,361,760 | 0.4% | 57.9% |
| BUILD_TUPLE RETURN_VALUE | 21,221,440 | 0.4% | 58.2% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 21,088,269 | 0.4% | 58.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 21,014,242 | 0.4% | 58.9% |
| LOAD_CONST COMPARE_OP_INT | 20,988,448 | 0.4% | 59.3% |
| POP_JUMP_IF_NONE JUMP_BACKWARD | 20,920,744 | 0.4% | 59.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 20,511,871 | 0.3% | 60.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 20,120,657 | 0.3% | 60.3% |
| LOAD_ATTR CONTAINS_OP | 20,047,172 | 0.3% | 60.7% |
| GET_ITER FOR_ITER | 20,010,747 | 0.3% | 61.0% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 19,950,557 | 0.3% | 61.3% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 19,466,404 | 0.3% | 61.7% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 19,054,887 | 0.3% | 62.0% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 18,835,523 | 0.3% | 62.3% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 18,812,026 | 0.3% | 62.6% |
| LOAD_FAST TO_BOOL_INT | 18,367,636 | 0.3% | 62.9% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 18,318,288 | 0.3% | 63.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 18,254,110 | 0.3% | 63.5% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 18,102,932 | 0.3% | 63.8% |
| LOAD_FAST CALL_BUILTIN_O | 17,805,254 | 0.3% | 64.1% |
| CALL_LIST_APPEND JUMP_BACKWARD | 17,342,715 | 0.3% | 64.4% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 17,273,105 | 0.3% | 64.7% |
| LOAD_ATTR IS_OP | 17,248,136 | 0.3% | 65.0% |
| LOAD_FAST BUILD_TUPLE | 17,176,347 | 0.3% | 65.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 16,716,809 | 0.3% | 65.6% |
| LOAD_FAST CALL_TYPE_1 | 16,588,820 | 0.3% | 65.9% |
| LOAD_FAST CALL_LIST_APPEND | 16,419,081 | 0.3% | 66.1% |
| LOAD_ATTR LOAD_FAST | 16,056,175 | 0.3% | 66.4% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 535,586 | 94.1% |
| LOAD_FAST | 26,720 | 4.7% |
| BINARY_OP_ADD_INT | 6,320 | 1.1% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 319,541 | 56.2% |
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
| RESUME_CHECK | 99,186,466 | 77.7% |
| POP_TOP | 13,887,950 | 10.9% |
| COPY_FREE_VARS | 13,002,549 | 10.2% |
| MAKE_CELL | 1,509,008 | 1.2% |
| RESUME | 18,053 | 0.0% |


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

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,159,749 | 58.8% |
| LOAD_DEREF | 6,402,802 | 26.6% |
| BUILD_TUPLE | 1,832,690 | 7.6% |
| LOAD_FAST | 1,312,605 | 5.4% |
| RETURN_VALUE | 152,428 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 6,993,861 | 29.0% |
| LOAD_FAST | 6,889,665 | 28.6% |
| RETURN_VALUE | 6,064,989 | 25.2% |
| CALL | 917,091 | 3.8% |
| GET_ITER | 916,385 | 3.8% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 667,290 | 73.7% |
| BUILD_TUPLE | 157,136 | 17.3% |
| LOAD_GLOBAL_MODULE | 79,258 | 8.7% |
| LOAD_FAST | 1,600 | 0.2% |
| LOAD_GLOBAL | 740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 905,864 | 100.0% |
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
| RETURN_CONST | 22,507 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,507 | 100.0% |


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
| LOAD_FAST | 21,629,155 | 36.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,456,719 | 24.1% |
| CALL | 10,953,192 | 18.2% |
| RETURN_VALUE | 4,116,056 | 6.9% |
| CALL_BUILTIN_O | 2,591,084 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 20,010,747 | 33.3% |
| CALL_PY_EXACT_ARGS | 13,008,077 | 21.7% |
| FOR_ITER_TUPLE | 9,973,191 | 16.6% |
| LOAD_FAST_AND_CLEAR | 9,197,701 | 15.3% |
| FOR_ITER_LIST | 4,575,366 | 7.6% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 346,920 | 64.2% |
| BINARY_SUBSCR | 185,800 | 34.4% |
| RETURN_VALUE | 7,520 | 1.4% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540,320 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 72,897,579 | 57.2% |
| RETURN_CONST | 32,281,795 | 25.3% |
| YIELD_VALUE | 22,221,074 | 17.4% |
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
| LOAD_CONST | 14,292,042 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 10,416,568 | 72.9% |
| LOAD_GLOBAL_BUILTIN | 2,651,040 | 18.5% |
| STORE_FAST | 669,659 | 4.7% |
| LOAD_FAST | 459,037 | 3.2% |
| STORE_NAME | 33,580 | 0.2% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,361,760 | 63.8% |
| POP_JUMP_IF_TRUE | 4,183,602 | 12.5% |
| STORE_FAST | 3,934,880 | 11.8% |
| POP_JUMP_IF_FALSE | 1,913,577 | 5.7% |
| POP_TOP | 1,391,455 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,285,681 | 36.7% |
| LOAD_DEREF | 10,423,785 | 31.1% |
| LOAD_GLOBAL_MODULE | 6,492,436 | 19.4% |
| LOAD_CONST | 2,608,104 | 7.8% |
| LOAD_FAST_LOAD_FAST | 912,242 | 2.7% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 414,573 | 45.8% |
| POP_TOP | 358,031 | 39.5% |
| STORE_FAST | 130,960 | 14.5% |
| COPY | 1,920 | 0.2% |
| STORE_SUBSCR_DICT | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 414,573 | 45.8% |
| EXTENDED_ARG | 201,050 | 22.2% |
| JUMP_BACKWARD | 159,381 | 17.6% |
| LOAD_FAST | 83,020 | 9.2% |
| RETURN_CONST | 45,040 | 5.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 15,099,745 | 24.5% |
| CACHE | 13,887,950 | 22.5% |
| RETURN_CONST | 9,410,042 | 15.2% |
| STORE_FAST | 5,838,592 | 9.5% |
| SWAP | 5,778,555 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 24,111,868 | 39.1% |
| RESUME_CHECK | 14,331,213 | 23.2% |
| LOAD_FAST | 7,246,971 | 11.7% |
| RETURN_VALUE | 5,302,355 | 8.6% |
| LOAD_CONST | 2,640,498 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 374,501 | 41.3% |
| BINARY_SUBSCR_DICT | 233,609 | 25.8% |
| RAISE_VARARGS | 115,218 | 12.7% |
| LOAD_ATTR | 95,500 | 10.5% |
| CALL_BUILTIN_CLASS | 38,396 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 787,846 | 87.0% |
| LOAD_GLOBAL_MODULE | 114,738 | 12.7% |
| LOAD_GLOBAL | 1,840 | 0.2% |
| LOAD_FAST | 1,600 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,402,865 | 46.8% |
| LOAD_ATTR | 14,955,975 | 24.6% |
| LOAD_DEREF | 11,928,399 | 19.7% |
| CALL_BUILTIN_FAST | 2,129,900 | 3.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,848 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,522,511 | 76.7% |
| LOAD_FAST_LOAD_FAST | 12,228,848 | 20.1% |
| LOAD_CONST | 1,723,720 | 2.8% |
| LOAD_DEREF | 128,568 | 0.2% |
| CALL | 35,600 | 0.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 9,893,340 | 69.0% |
| CALL_PY_EXACT_ARGS | 4,260,693 | 29.7% |
| CALL_PY_WITH_DEFAULTS | 163,640 | 1.1% |
| CALL_KW | 8,000 | 0.1% |
| CACHE | 7,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 10,197,743 | 71.1% |
| STORE_FAST | 2,660,251 | 18.6% |
| LOAD_FAST | 791,856 | 5.5% |
| GET_YIELD_FROM_ITER | 346,920 | 2.4% |
| CALL_BUILTIN_CLASS | 160,600 | 1.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,587,460 | 30.2% |
| LOAD_ATTR_SLOT | 33,431,216 | 18.8% |
| BUILD_TUPLE | 21,221,440 | 12.0% |
| RETURN_VALUE | 15,182,662 | 8.6% |
| CALL_BUILTIN_O | 11,432,311 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 72,897,579 | 41.1% |
| STORE_FAST | 38,550,703 | 21.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 19,466,404 | 11.0% |
| RETURN_VALUE | 15,182,662 | 8.6% |
| LOAD_FAST | 5,453,419 | 3.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,302,897 | 96.3% |
| BINARY_SUBSCR | 93,200 | 2.7% |
| LOAD_FAST_LOAD_FAST | 18,960 | 0.6% |
| SWAP | 5,960 | 0.2% |
| STORE_SUBSCR | 3,640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,289,817 | 96.0% |
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
| LOAD_FAST | 2,207,738 | 17.1% |
| LOAD_GLOBAL_MODULE | 118,981 | 0.9% |
| LOAD_ATTR | 117,975 | 0.9% |
| RETURN_VALUE | 27,290 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,253,034 | 94.8% |
| POP_JUMP_IF_TRUE | 509,737 | 3.9% |
| UNARY_NOT | 84,152 | 0.7% |
| TO_BOOL_BOOL | 41,183 | 0.3% |
| TO_BOOL | 21,456 | 0.2% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 188,428 | 30.7% |
| LOAD_ATTR_SLOT | 117,476 | 19.2% |
| LOAD_ATTR | 107,040 | 17.5% |
| RETURN_VALUE | 106,160 | 17.3% |
| LOAD_FAST_LOAD_FAST | 50,656 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 131,954 | 21.5% |
| CALL_LIST_APPEND | 119,120 | 19.4% |
| LOAD_GLOBAL_MODULE | 106,842 | 17.4% |
| IS_OP | 106,160 | 17.3% |
| STORE_FAST | 58,052 | 9.5% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 3,442,580 | 64.9% |
| TO_BOOL_BOOL | 1,118,640 | 21.1% |
| TO_BOOL_LIST | 661,852 | 12.5% |
| TO_BOOL | 84,152 | 1.6% |
| TO_BOOL_INT | 165 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,529,340 | 66.5% |
| STORE_FAST | 882,714 | 16.6% |
| BUILD_MAP | 734,720 | 13.8% |
| COPY | 86,917 | 1.6% |
| LOAD_CONST | 68,038 | 1.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,766,655 | 33.3% |
| COMPARE_OP_INT | 6,308,780 | 17.9% |
| COMPARE_OP | 6,162,400 | 17.4% |
| CALL_TUPLE_1 | 4,707,117 | 13.3% |
| LOAD_FAST | 2,678,435 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,216,741 | 68.6% |
| RETURN_VALUE | 5,771,006 | 16.3% |
| BUILD_TUPLE | 1,556,880 | 4.4% |
| CALL_BUILTIN_O | 1,095,103 | 3.1% |
| LOAD_FAST | 857,855 | 2.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 129,301 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 126,521 | 97.8% |
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
| SWAP | 4,463,684 | 20.6% |
| POP_JUMP_IF_TRUE | 4,083,244 | 18.9% |
| STORE_FAST | 3,817,053 | 17.7% |
| LOAD_FAST | 2,311,726 | 10.7% |
| BINARY_SUBSCR_TUPLE_INT | 1,557,600 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,718,015 | 54.2% |
| SWAP | 4,463,684 | 20.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,294,372 | 10.6% |
| LOAD_FAST | 1,414,153 | 6.5% |
| BUILD_LIST | 748,350 | 3.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,167,334 | 36.0% |
| BUILD_TUPLE | 10,998,540 | 32.5% |
| SWAP | 4,716,017 | 14.0% |
| LOAD_CONST | 1,656,800 | 4.9% |
| RESUME_CHECK | 1,285,960 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,182,782 | 68.6% |
| SWAP | 4,716,017 | 14.0% |
| STORE_FAST | 3,331,862 | 9.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,561,360 | 4.6% |
| CALL_FUNCTION_EX | 734,880 | 2.2% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,173 | 64.0% |
| SWAP | 18,000 | 35.8% |
| BINARY_OP | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 32,173 | 64.0% |
| SWAP | 18,000 | 35.8% |
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
| LOAD_FAST_LOAD_FAST | 25,639,424 | 45.0% |
| LOAD_FAST | 17,176,347 | 30.1% |
| LOAD_ATTR_SLOT | 5,042,022 | 8.8% |
| LOAD_ATTR | 3,034,561 | 5.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,484,120 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 21,221,440 | 37.2% |
| BUILD_MAP | 10,998,540 | 19.3% |
| LOAD_CONST | 10,439,508 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 4,706,917 | 8.3% |
| CALL_LIST_APPEND | 3,231,440 | 5.7% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,643,119 | 35.9% |
| LOAD_FAST | 7,320,236 | 27.3% |
| LOAD_ATTR | 3,067,122 | 11.4% |
| BINARY_OP_MULTIPLY_INT | 2,291,864 | 8.5% |
| LOAD_GLOBAL_BUILTIN | 1,572,909 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,953,192 | 40.8% |
| STORE_FAST | 5,844,427 | 21.8% |
| RETURN_VALUE | 4,521,774 | 16.8% |
| POP_TOP | 1,139,971 | 4.2% |
| RESUME_CHECK | 1,064,658 | 4.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 23,271,983 | 83.1% |
| LOAD_FAST | 2,317,388 | 8.3% |
| CALL_INTRINSIC_1 | 1,256,575 | 4.5% |
| BUILD_MAP | 734,880 | 2.6% |
| BINARY_OP | 201,680 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,600,469 | 45.0% |
| RESUME_CHECK | 11,673,273 | 41.7% |
| LOAD_FAST_LOAD_FAST | 1,561,000 | 5.6% |
| BUILD_TUPLE | 638,781 | 2.3% |
| SWAP | 480,160 | 1.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 1,347,633 | 99.9% |
| IMPORT_NAME | 1,060 | 0.1% |
| LIST_APPEND | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,256,575 | 93.2% |
| BUILD_MAP | 91,218 | 6.8% |
| POP_TOP | 1,060 | 0.1% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,672,348 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,492,381 | 88.9% |
| POP_TOP | 698,026 | 6.5% |
| COPY_FREE_VARS | 261,140 | 2.4% |
| RETURN_VALUE | 84,815 | 0.8% |
| STORE_FAST | 35,740 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 21,088,269 | 54.7% |
| LOAD_FAST | 8,285,406 | 21.5% |
| CALL_TYPE_1 | 5,882,177 | 15.3% |
| LOAD_GLOBAL_MODULE | 1,179,749 | 3.1% |
| LOAD_CONST | 948,664 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,120,657 | 52.2% |
| BINARY_OP | 6,162,400 | 16.0% |
| LOAD_FAST_LOAD_FAST | 6,162,320 | 16.0% |
| UNARY_NOT | 3,442,580 | 8.9% |
| POP_JUMP_IF_TRUE | 2,278,778 | 5.9% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 24,720,227 | 47.4% |
| LOAD_ATTR | 20,047,172 | 38.4% |
| LOAD_GLOBAL_MODULE | 5,290,222 | 10.1% |
| LOAD_DEREF | 1,536,480 | 2.9% |
| LOAD_CONST | 174,997 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 45,412,322 | 87.1% |
| POP_JUMP_IF_TRUE | 6,741,163 | 12.9% |
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
| LOAD_FAST | 1,237,516 | 25.2% |
| COPY | 1,214,400 | 24.7% |
| LOAD_FAST_LOAD_FAST | 872,880 | 17.8% |
| CALL_ISINSTANCE | 525,020 | 10.7% |
| LOAD_CONST | 236,733 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,339,983 | 27.3% |
| COPY | 1,214,400 | 24.7% |
| BINARY_SUBSCR_LIST_INT | 1,208,120 | 24.6% |
| LOAD_ATTR_INSTANCE_VALUE | 956,400 | 19.5% |
| STORE_FAST_STORE_FAST | 55,533 | 1.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,002,549 | 40.9% |
| CALL_PY_EXACT_ARGS | 11,876,062 | 37.4% |
| LOAD_ATTR_PROPERTY | 5,060,870 | 15.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,202,434 | 3.8% |
| CALL_KW | 261,140 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,813,248 | 68.6% |
| RETURN_GENERATOR | 9,893,340 | 31.1% |
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
| LOAD_FAST | 23,143,083 | 99.4% |
| LOAD_DEREF | 128,900 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 23,271,983 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,678,812 | 26.5% |
| TO_BOOL_BOOL | 5,485,828 | 25.6% |
| CALL_LIST_APPEND | 4,571,139 | 21.3% |
| GET_ITER | 2,378,070 | 11.1% |
| COMPARE_OP_INT | 1,719,879 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,038,369 | 32.9% |
| JUMP_BACKWARD | 5,792,342 | 27.0% |
| FOR_ITER_LIST | 5,660,666 | 26.4% |
| FOR_ITER_TUPLE | 1,740,040 | 8.1% |
| FOR_ITER_RANGE | 642,400 | 3.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 68,588,606 | 66.0% |
| GET_ITER | 20,010,747 | 19.2% |
| SWAP | 7,638,449 | 7.3% |
| LOAD_FAST | 7,623,667 | 7.3% |
| FOR_ITER | 79,583 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 71,232,970 | 68.5% |
| STORE_FAST | 8,349,505 | 8.0% |
| SWAP | 7,602,677 | 7.3% |
| LOAD_FAST | 4,698,535 | 4.5% |
| RETURN_CONST | 4,697,797 | 4.5% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 7,757,126 | 86.6% |
| STORE_FAST | 982,207 | 11.0% |
| STORE_DEREF | 185,679 | 2.1% |
| STORE_NAME | 26,000 | 0.3% |
| EXTENDED_ARG | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,820,589 | 76.2% |
| STORE_DEREF | 2,092,363 | 23.4% |
| STORE_NAME | 38,060 | 0.4% |
| EXTENDED_ARG | 2,540 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,758,626 | 100.0% |
| EXTENDED_ARG | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 7,757,126 | 100.0% |
| CALL_INTRINSIC_1 | 1,060 | 0.0% |
| STORE_NAME | 440 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 17,248,136 | 36.1% |
| LOAD_FAST | 12,819,806 | 26.8% |
| LOAD_CONST | 10,974,918 | 23.0% |
| LOAD_FAST_LOAD_FAST | 5,893,466 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 539,788 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 30,047,270 | 62.9% |
| YIELD_VALUE | 12,804,466 | 26.8% |
| POP_JUMP_IF_TRUE | 4,906,796 | 10.3% |
| EXTENDED_ARG | 27,180 | 0.1% |
| STORE_FAST | 8,960 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 34,387,291 | 21.9% |
| POP_TOP | 24,111,868 | 15.4% |
| POP_JUMP_IF_TRUE | 22,700,490 | 14.5% |
| POP_JUMP_IF_NONE | 20,920,744 | 13.4% |
| CALL_LIST_APPEND | 17,342,715 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 68,588,606 | 43.8% |
| FOR_ITER_LIST | 46,543,233 | 29.7% |
| FOR_ITER_TUPLE | 22,268,260 | 14.2% |
| FOR_ITER_RANGE | 10,602,761 | 6.8% |
| EXTENDED_ARG | 5,678,812 | 3.6% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 928,400 | 100.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 661,220 | 71.2% |
| SEND | 267,340 | 28.8% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,278,454 | 72.5% |
| POP_TOP | 734,240 | 12.4% |
| STORE_FAST_STORE_FAST | 240,720 | 4.1% |
| CALL_LIST_APPEND | 191,862 | 3.3% |
| LOAD_FAST | 146,921 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,005,690 | 67.9% |
| BUILD_MAP | 642,560 | 10.9% |
| LOAD_GLOBAL_BUILTIN | 470,020 | 8.0% |
| LOAD_FAST_LOAD_FAST | 437,227 | 7.4% |
| STORE_FAST | 119,021 | 2.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,003,984 | 48.5% |
| BUILD_TUPLE | 1,568,799 | 25.4% |
| RETURN_VALUE | 511,241 | 8.3% |
| BINARY_SUBSCR | 489,428 | 7.9% |
| BINARY_SUBSCR_LIST_INT | 396,080 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,182,727 | 99.9% |
| LOAD_NAME | 4,800 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,346,753 | 99.8% |
| LOAD_CONST | 1,260 | 0.1% |
| LOAD_DEREF | 640 | 0.0% |
| LOAD_ATTR_SLOT | 200 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,347,633 | 99.9% |
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
| LOAD_GLOBAL_MODULE | 57,024,374 | 46.9% |
| LOAD_FAST | 55,265,410 | 45.4% |
| CALL_TYPE_1 | 4,209,112 | 3.5% |
| LOAD_ATTR_SLOT | 2,297,032 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 1,904,819 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 36,810,358 | 30.2% |
| CONTAINS_OP | 20,047,172 | 16.5% |
| IS_OP | 17,248,136 | 14.2% |
| LOAD_FAST | 16,056,175 | 13.2% |
| PUSH_NULL | 14,955,975 | 12.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 69,874,990 | 36.5% |
| LOAD_CONST | 40,441,633 | 21.1% |
| RESUME_CHECK | 15,733,861 | 8.2% |
| BUILD_TUPLE | 10,439,508 | 5.5% |
| RETURN_CONST | 9,526,680 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,441,633 | 21.1% |
| CALL_BUILTIN_FAST | 24,270,760 | 12.7% |
| COMPARE_OP_INT | 20,988,448 | 11.0% |
| STORE_FAST | 14,708,272 | 7.7% |
| MAKE_FUNCTION | 14,292,042 | 7.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 22,128,669 | 32.2% |
| NOP | 10,423,785 | 15.2% |
| LOAD_FAST | 7,793,968 | 11.3% |
| LOAD_ATTR_SLOT | 6,402,802 | 9.3% |
| POP_JUMP_IF_FALSE | 4,653,352 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 22,297,414 | 32.4% |
| PUSH_NULL | 11,928,399 | 17.3% |
| LOAD_FAST | 9,405,879 | 13.7% |
| CALL_ISINSTANCE | 7,549,083 | 11.0% |
| BINARY_SUBSCR | 6,402,802 | 9.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 196,202,666 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 162,937,836 | 16.7% |
| RESUME_CHECK | 115,548,335 | 11.8% |
| POP_JUMP_IF_FALSE | 113,710,993 | 11.6% |
| PUSH_NULL | 46,522,511 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 95,196,531 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 79,135,103 | 8.1% |
| LOAD_GLOBAL_MODULE | 78,851,505 | 8.1% |
| LOAD_CONST | 69,874,990 | 7.2% |
| LOAD_ATTR | 55,265,410 | 5.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,197,701 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,589,756 | 45.2% |
| MAKE_CELL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,197,621 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,589,756 | 45.2% |
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
| STORE_FAST | 62,539,746 | 24.6% |
| POP_JUMP_IF_FALSE | 34,094,570 | 13.4% |
| LOAD_GLOBAL_BUILTIN | 28,996,857 | 11.4% |
| RESUME_CHECK | 19,950,557 | 7.9% |
| STORE_FAST_STORE_FAST | 15,652,918 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 26,980,339 | 10.6% |
| BUILD_TUPLE | 25,639,424 | 10.1% |
| CONTAINS_OP | 24,720,227 | 9.7% |
| COMPARE_OP | 21,088,269 | 8.3% |
| STORE_SUBSCR_LIST_INT | 18,835,523 | 7.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,251 | 19.4% |
| LOAD_FAST | 34,209 | 18.8% |
| STORE_FAST | 26,929 | 14.8% |
| RESUME_CHECK | 10,928 | 6.0% |
| RESUME | 10,777 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 50,534 | 27.8% |
| LOAD_GLOBAL_BUILTIN | 41,250 | 22.7% |
| LOAD_FAST | 39,593 | 21.8% |
| LOAD_ATTR | 14,074 | 7.7% |
| CALL | 9,825 | 5.4% |


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
| MAKE_CELL | 2,274,343 | 37.6% |
| CACHE | 1,509,008 | 24.9% |
| CALL_PY_EXACT_ARGS | 772,483 | 12.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 654,292 | 10.8% |
| CALL | 523,656 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,770,483 | 62.3% |
| MAKE_CELL | 2,274,343 | 37.6% |
| RESUME | 3,000 | 0.0% |
| RETURN_GENERATOR | 400 | 0.0% |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 7,852,547 | 99.8% |
| LOAD_FAST | 4,160 | 0.1% |
| RETURN_VALUE | 3,620 | 0.0% |
| CALL | 1,920 | 0.0% |
| STORE_FAST | 1,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,865,367 | 100.0% |
| LOAD_CONST | 320 | 0.0% |
| LOAD_NAME | 20 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 111,640,595 | 38.3% |
| CONTAINS_OP | 45,412,322 | 15.6% |
| COMPARE_OP_INT | 35,523,327 | 12.2% |
| IS_OP | 30,047,270 | 10.3% |
| COMPARE_OP | 20,120,657 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,710,993 | 39.0% |
| LOAD_GLOBAL_BUILTIN | 57,999,739 | 19.9% |
| JUMP_BACKWARD | 34,387,291 | 11.8% |
| LOAD_FAST_LOAD_FAST | 34,094,570 | 11.7% |
| RETURN_CONST | 29,331,468 | 10.1% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,145,361 | 80.4% |
| BINARY_SUBSCR | 6,993,861 | 17.0% |
| LOAD_DEREF | 1,088,825 | 2.6% |
| LOAD_ATTR_INSTANCE_VALUE | 8,380 | 0.0% |
| EXTENDED_ARG | 6,779 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20,920,744 | 50.7% |
| LOAD_FAST_LOAD_FAST | 14,853,406 | 36.0% |
| LOAD_FAST | 2,615,587 | 6.3% |
| LOAD_GLOBAL_BUILTIN | 1,437,622 | 3.5% |
| LOAD_CONST | 1,111,391 | 2.7% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,716,809 | 92.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,224,918 | 6.7% |
| EXTENDED_ARG | 179,780 | 1.0% |
| CALL_BUILTIN_FAST | 11,040 | 0.1% |
| LOAD_DEREF | 8,920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,236,647 | 67.4% |
| LOAD_FAST_LOAD_FAST | 2,031,153 | 11.2% |
| LOAD_GLOBAL_MODULE | 1,880,083 | 10.4% |
| LOAD_GLOBAL_BUILTIN | 1,385,674 | 7.6% |
| JUMP_BACKWARD | 503,314 | 2.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 54,455,607 | 67.6% |
| TO_BOOL_INT | 9,136,899 | 11.3% |
| CONTAINS_OP | 6,741,163 | 8.4% |
| IS_OP | 4,906,796 | 6.1% |
| COMPARE_OP | 2,278,778 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,015,324 | 47.2% |
| JUMP_BACKWARD | 22,700,490 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 5,308,493 | 6.6% |
| NOP | 4,183,602 | 5.2% |
| BUILD_LIST | 4,083,244 | 5.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 118,878 | 99.9% |
| CALL_KW | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 115,218 | 98.4% |
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
| POP_JUMP_IF_FALSE | 29,331,468 | 51.2% |
| RESUME_CHECK | 10,044,615 | 17.5% |
| FOR_ITER_LIST | 5,671,308 | 9.9% |
| FOR_ITER | 4,697,797 | 8.2% |
| STORE_SUBSCR | 3,289,817 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 32,281,795 | 56.4% |
| LOAD_CONST | 9,526,680 | 16.6% |
| POP_TOP | 9,410,042 | 16.4% |
| TO_BOOL_BOOL | 3,461,946 | 6.0% |
| STORE_FAST | 1,540,960 | 2.7% |


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
| MAKE_FUNCTION | 10,416,568 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 1,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,820,660 | 94.3% |
| STORE_FAST | 306,982 | 2.9% |
| STORE_DEREF | 113,182 | 1.1% |
| LOAD_CONST | 52,360 | 0.5% |
| LOAD_GLOBAL_MODULE | 42,880 | 0.4% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 486,750 | 82.3% |
| LOAD_FAST | 98,460 | 16.7% |
| STORE_ATTR | 3,906 | 0.7% |
| SWAP | 2,155 | 0.4% |
| LOAD_DEREF | 12 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 289,612 | 49.0% |
| LOAD_FAST_LOAD_FAST | 116,218 | 19.7% |
| LOAD_FAST | 89,981 | 15.2% |
| LOAD_GLOBAL_BUILTIN | 74,060 | 12.5% |
| STORE_ATTR_INSTANCE_VALUE | 3,960 | 0.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 4,491,620 | 51.7% |
| IMPORT_FROM | 2,092,363 | 24.1% |
| LOAD_ATTR | 1,558,804 | 17.9% |
| STORE_FAST | 240,860 | 2.8% |
| SET_FUNCTION_ATTRIBUTE | 113,182 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,491,580 | 51.7% |
| POP_TOP | 1,906,684 | 21.9% |
| LOAD_DEREF | 1,298,283 | 14.9% |
| LOAD_GLOBAL_MODULE | 481,480 | 5.5% |
| IMPORT_FROM | 185,679 | 2.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 43,123,895 | 12.0% |
| RETURN_VALUE | 38,550,703 | 10.7% |
| LOAD_ATTR | 36,810,358 | 10.3% |
| BINARY_OP | 24,216,741 | 6.7% |
| FOR_ITER_TUPLE | 23,956,122 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 196,202,666 | 54.7% |
| LOAD_FAST_LOAD_FAST | 62,539,746 | 17.4% |
| LOAD_GLOBAL_BUILTIN | 37,716,082 | 10.5% |
| LOAD_GLOBAL_MODULE | 18,254,110 | 5.1% |
| STORE_FAST | 9,344,402 | 2.6% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,156,210 | 77.8% |
| FOR_ITER_TUPLE | 595,623 | 11.1% |
| FOR_ITER_RANGE | 500,000 | 9.4% |
| FOR_ITER | 92,960 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,303,710 | 80.5% |
| LOAD_ATTR_PROPERTY | 319,456 | 6.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 236,807 | 4.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 157,680 | 3.0% |
| LOAD_DEREF | 107,360 | 2.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 99,126,782 | 93.6% |
| RETURN_VALUE | 3,248,045 | 3.1% |
| UNPACK_SEQUENCE_TUPLE | 1,436,119 | 1.4% |
| STORE_FAST_STORE_FAST | 771,401 | 0.7% |
| BUILD_LIST | 413,120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,979,900 | 39.7% |
| LOAD_DEREF | 22,128,669 | 20.9% |
| LOAD_GLOBAL_BUILTIN | 22,022,759 | 20.8% |
| LOAD_FAST_LOAD_FAST | 15,652,918 | 14.8% |
| LOAD_GLOBAL_MODULE | 1,958,340 | 1.9% |


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
| BINARY_SUBSCR_LIST_INT | 9,389,302 | 20.7% |
| LOAD_FAST_AND_CLEAR | 9,197,621 | 20.3% |
| FOR_ITER | 7,602,677 | 16.8% |
| BUILD_MAP | 4,716,017 | 10.4% |
| LOAD_FAST | 4,641,375 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,389,522 | 20.7% |
| STORE_FAST | 7,930,506 | 17.5% |
| FOR_ITER | 7,638,449 | 16.9% |
| POP_TOP | 5,778,555 | 12.8% |
| BUILD_MAP | 4,716,017 | 10.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,452 | 26.4% |
| FOR_ITER | 6,803 | 17.2% |
| CALL_BUILTIN_CLASS | 6,340 | 16.0% |
| LOAD_FAST | 3,941 | 9.9% |
| CALL_BUILTIN_FAST | 3,260 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 18,673 | 47.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,429 | 23.8% |
| STORE_FAST | 8,009 | 20.2% |
| UNPACK_SEQUENCE_TUPLE | 1,139 | 2.9% |
| UNPACK_SEQUENCE | 913 | 2.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 12,804,466 | 55.5% |
| CALL_ISINSTANCE | 6,945,701 | 30.1% |
| LOAD_FAST | 1,146,596 | 5.0% |
| YIELD_VALUE | 677,400 | 2.9% |
| RETURN_VALUE | 423,186 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 22,221,074 | 96.3% |
| YIELD_VALUE | 677,400 | 2.9% |
| STORE_FAST | 162,741 | 0.7% |
| UNPACK_SEQUENCE | 3,120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,520 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 18,053 | 38.0% |
| CALL | 11,103 | 23.3% |
| CALL_PY_EXACT_ARGS | 6,110 | 12.8% |
| POP_TOP | 3,960 | 8.3% |
| MAKE_CELL | 3,000 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,698 | 37.2% |
| LOAD_GLOBAL | 10,777 | 22.7% |
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
| LOAD_CONST | 11,819,889 | 91.1% |
| LOAD_FAST_LOAD_FAST | 573,895 | 4.4% |
| BINARY_SUBSCR_DICT | 422,960 | 3.3% |
| CALL_BUILTIN_CLASS | 81,141 | 0.6% |
| LOAD_FAST | 43,682 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 9,387,214 | 72.4% |
| STORE_FAST | 1,576,479 | 12.2% |
| SWAP | 1,085,055 | 8.4% |
| LOAD_CONST | 268,988 | 2.1% |
| LOAD_FAST | 201,465 | 1.6% |


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
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,668,682 | 60.2% |
| LOAD_ATTR_SLOT | 723,517 | 26.1% |
| LOAD_FAST_LOAD_FAST | 283,453 | 10.2% |
| LOAD_FAST | 94,285 | 3.4% |
| BINARY_OP | 1,445 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,291,864 | 82.7% |
| LOAD_FAST_LOAD_FAST | 181,166 | 6.5% |
| STORE_FAST | 175,546 | 6.3% |
| LOAD_FAST | 90,186 | 3.3% |
| LOAD_GLOBAL_MODULE | 25,188 | 0.9% |


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
| LOAD_CONST | 1,569,015 | 63.1% |
| LOAD_FAST_LOAD_FAST | 606,941 | 24.4% |
| BINARY_SUBSCR_LIST_INT | 181,120 | 7.3% |
| LOAD_FAST | 123,235 | 5.0% |
| BINARY_OP | 2,184 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,082,420 | 43.5% |
| STORE_FAST | 710,159 | 28.6% |
| BINARY_OP | 311,648 | 12.5% |
| COMPARE_OP_INT | 184,120 | 7.4% |
| BINARY_SUBSCR_LIST_INT | 54,440 | 2.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,215,088 | 36.3% |
| LOAD_FAST_LOAD_FAST | 925,237 | 27.6% |
| LOAD_CONST | 642,800 | 19.2% |
| CALL_TUPLE_1 | 443,840 | 13.3% |
| RETURN_VALUE | 114,456 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 884,065 | 26.4% |
| RETURN_VALUE | 809,182 | 24.2% |
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
| LOAD_CONST | 14,540 | 9.1% |
| BUILD_SLICE | 3,840 | 2.4% |
| BINARY_SUBSCR | 700 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 159,236 | 100.0% |
| RETURN_VALUE | 2 | 0.0% |
| LOAD_CONST | 2 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 26,980,339 | 89.4% |
| COPY | 1,208,120 | 4.0% |
| LOAD_CONST | 1,026,634 | 3.4% |
| LOAD_FAST | 570,317 | 1.9% |
| CALL_BUILTIN_CLASS | 282,358 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,452,002 | 31.3% |
| SWAP | 9,389,302 | 31.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,538,675 | 25.0% |
| LOAD_CONST | 1,208,580 | 4.0% |
| STORE_FAST | 517,278 | 1.7% |


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
| LOAD_CONST | 8,728,929 | 97.0% |
| LOAD_FAST | 263,350 | 2.9% |
| BINARY_SUBSCR | 2,736 | 0.0% |
| LOAD_FAST_LOAD_FAST | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,738,172 | 52.7% |
| CALL_LIST_APPEND | 1,762,920 | 19.6% |
| BUILD_LIST | 1,557,600 | 17.3% |
| LOAD_FAST | 322,021 | 3.6% |
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
| LOAD_FAST | 13,333,585 | 56.7% |
| BINARY_OP_ADD_INT | 9,387,214 | 39.9% |
| LOAD_FAST_LOAD_FAST | 480,346 | 2.0% |
| LOAD_ATTR | 152,040 | 0.6% |
| LOAD_DEREF | 83,580 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,649,219 | 92.1% |
| COPY_FREE_VARS | 1,202,434 | 5.1% |
| MAKE_CELL | 654,292 | 2.8% |
| POP_TOP | 7,360 | 0.0% |
| CALL_PY_EXACT_ARGS | 719 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,821,437 | 30.8% |
| CALL_BUILTIN_CLASS | 1,958,889 | 21.4% |
| LOAD_GLOBAL_BUILTIN | 921,044 | 10.1% |
| LOAD_CONST | 710,920 | 7.8% |
| CALL_LEN | 610,645 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,419,032 | 37.4% |
| CALL_BUILTIN_CLASS | 1,958,889 | 21.4% |
| GET_ITER | 1,868,296 | 20.4% |
| CALL | 284,323 | 3.1% |
| BINARY_SUBSCR_LIST_INT | 282,358 | 3.1% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,270,760 | 55.8% |
| LOAD_FAST_LOAD_FAST | 17,273,105 | 39.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,337,014 | 3.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 1.1% |
| LOAD_FAST | 64,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 18,102,932 | 41.8% |
| STORE_FAST | 11,045,638 | 25.5% |
| TO_BOOL | 10,287,220 | 23.8% |
| PUSH_NULL | 2,129,900 | 4.9% |
| RETURN_VALUE | 1,499,723 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,880,637 | 94.4% |
| LOAD_FAST | 135,097 | 2.6% |
| BINARY_OP | 119,081 | 2.3% |
| RETURN_GENERATOR | 27,800 | 0.5% |
| LOAD_CONST | 5,580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_TUPLE_1 | 4,706,917 | 91.0% |
| GET_ITER | 173,780 | 3.4% |
| STORE_FAST | 127,997 | 2.5% |
| CALL_BUILTIN_CLASS | 119,081 | 2.3% |
| RETURN_VALUE | 34,520 | 0.7% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,805,254 | 44.7% |
| RETURN_GENERATOR | 10,197,743 | 25.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 5,611,882 | 14.1% |
| LOAD_ATTR_SLOT | 4,880,546 | 12.2% |
| BINARY_OP | 1,095,103 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,684,026 | 39.3% |
| RETURN_VALUE | 11,432,311 | 28.7% |
| TO_BOOL_BOOL | 9,900,062 | 24.8% |
| GET_ITER | 2,591,084 | 6.5% |
| LOAD_FAST | 50,620 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 35,897,553 | 53.2% |
| LOAD_GLOBAL_BUILTIN | 19,054,887 | 28.2% |
| LOAD_DEREF | 7,549,083 | 11.2% |
| LOAD_FAST_LOAD_FAST | 2,883,493 | 4.3% |
| LOAD_FAST | 1,621,032 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 59,841,461 | 88.7% |
| YIELD_VALUE | 6,945,701 | 10.3% |
| COPY | 525,020 | 0.8% |
| RETURN_VALUE | 127,509 | 0.2% |
| TO_BOOL | 9,664 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,056,087 | 96.3% |
| LOAD_GLOBAL_MODULE | 553,240 | 2.0% |
| BINARY_SUBSCR | 185,800 | 0.7% |
| RETURN_VALUE | 94,980 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 93,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 10,271,095 | 36.6% |
| LOAD_GLOBAL_BUILTIN | 9,676,816 | 34.4% |
| LOAD_CONST | 7,190,417 | 25.6% |
| CALL_BUILTIN_CLASS | 610,645 | 2.2% |
| STORE_FAST | 84,420 | 0.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,419,081 | 68.4% |
| BUILD_TUPLE | 3,231,440 | 13.5% |
| BINARY_SUBSCR_TUPLE_INT | 1,762,920 | 7.3% |
| LOAD_FAST_CHECK | 1,556,980 | 6.5% |
| CALL | 693,105 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,342,715 | 72.2% |
| EXTENDED_ARG | 4,571,139 | 19.0% |
| LOAD_FAST | 1,681,750 | 7.0% |
| LOAD_FAST_LOAD_FAST | 207,500 | 0.9% |
| JUMP_FORWARD | 191,862 | 0.8% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,165,097 | 68.7% |
| LOAD_CONST | 2,390,066 | 10.8% |
| BUILD_LIST | 2,294,372 | 10.4% |
| BUILD_MAP | 1,561,360 | 7.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 272,258 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,852,546 | 58.2% |
| STORE_FAST | 3,452,873 | 15.6% |
| LOAD_ATTR_METHOD_NO_DICT | 3,116,160 | 14.1% |
| POP_TOP | 908,781 | 4.1% |
| GET_ITER | 737,572 | 3.3% |


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
| LOAD_ATTR_METHOD_NO_DICT | 24,524,903 | 83.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,807,474 | 16.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,785 | 0.4% |
| LOAD_ATTR | 72,820 | 0.2% |
| CALL | 3,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 14,456,719 | 49.0% |
| STORE_FAST | 9,681,811 | 32.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,880,637 | 16.5% |
| CALL_BUILTIN_CLASS | 169,815 | 0.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,785 | 0.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,853,920 | 61.4% |
| LOAD_CONST | 1,226,418 | 26.4% |
| LOAD_FAST | 353,960 | 7.6% |
| RETURN_VALUE | 97,600 | 2.1% |
| BUILD_LIST | 44,300 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,235,540 | 69.6% |
| LOAD_CONST | 1,224,418 | 26.3% |
| TO_BOOL_NONE | 104,000 | 2.2% |
| BINARY_OP_ADD_UNICODE | 39,600 | 0.9% |
| STORE_FAST | 25,520 | 0.5% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 21,014,242 | 30.8% |
| LOAD_FAST | 15,740,607 | 23.1% |
| LOAD_FAST_LOAD_FAST | 13,767,682 | 20.2% |
| GET_ITER | 13,008,077 | 19.1% |
| LOAD_SUPER_ATTR_METHOD | 1,539,388 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 51,008,736 | 74.9% |
| COPY_FREE_VARS | 11,876,062 | 17.4% |
| RETURN_GENERATOR | 4,260,693 | 6.3% |
| MAKE_CELL | 772,483 | 1.1% |
| CALL_PY_EXACT_ARGS | 144,902 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,104,925 | 45.8% |
| LOAD_FAST | 1,865,608 | 40.6% |
| RETURN_VALUE | 192,601 | 4.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 157,842 | 3.4% |
| LOAD_CONST | 80,481 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,379,603 | 95.3% |
| RETURN_GENERATOR | 163,640 | 3.6% |
| MAKE_CELL | 53,709 | 1.2% |
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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,706,917 | 80.4% |
| LOAD_FAST | 1,017,539 | 17.4% |
| STORE_FAST | 105,740 | 1.8% |
| RETURN_VALUE | 7,920 | 0.1% |
| LOAD_DEREF | 4,120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 4,707,117 | 80.4% |
| BINARY_SUBSCR_DICT | 443,840 | 7.6% |
| STORE_FAST | 353,180 | 6.0% |
| STORE_SUBSCR_DICT | 181,360 | 3.1% |
| RETURN_VALUE | 56,520 | 1.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,588,820 | 99.3% |
| LOAD_CONST | 119,938 | 0.7% |
| LOAD_GLOBAL_MODULE | 1,840 | 0.0% |
| CALL | 1,081 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,423,284 | 38.4% |
| COMPARE_OP | 5,882,177 | 35.2% |
| LOAD_ATTR | 4,209,112 | 25.2% |
| IS_OP | 64,198 | 0.4% |
| BUILD_TUPLE | 55,800 | 0.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 493,785 | 90.8% |
| CALL_BUILTIN_CLASS | 25,400 | 4.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 21,408 | 3.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,840 | 0.3% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 541,973 | 99.7% |
| RETURN_VALUE | 1,580 | 0.3% |
| COMPARE_OP | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,988,448 | 41.0% |
| LOAD_FAST_LOAD_FAST | 18,318,288 | 35.8% |
| CALL_LEN | 10,271,095 | 20.1% |
| LOAD_FAST | 1,029,121 | 2.0% |
| LOAD_ATTR_SLOT | 225,194 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,523,327 | 69.4% |
| BINARY_OP | 6,308,780 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 4,738,660 | 9.3% |
| EXTENDED_ARG | 1,719,879 | 3.4% |
| LOAD_FAST_LOAD_FAST | 1,570,040 | 3.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,030,880 | 68.9% |
| LOAD_CONST | 4,335,283 | 29.8% |
| LOAD_GLOBAL_MODULE | 192,528 | 1.3% |
| LOAD_ATTR | 3,160 | 0.0% |
| LOAD_FAST | 2,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,480,519 | 99.4% |
| YIELD_VALUE | 79,552 | 0.5% |
| POP_JUMP_IF_TRUE | 3,520 | 0.0% |
| EXTENDED_ARG | 1,000 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 100,485 | 52.6% |
| GET_ITER | 90,623 | 47.4% |
| FOR_ITER | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,565 | 52.1% |
| POP_TOP | 90,463 | 47.3% |
| RESUME | 860 | 0.4% |
| STORE_FAST | 320 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 46,543,233 | 74.0% |
| EXTENDED_ARG | 5,660,666 | 9.0% |
| LOAD_FAST | 4,843,623 | 7.7% |
| GET_ITER | 4,575,366 | 7.3% |
| SWAP | 1,221,391 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,123,895 | 68.6% |
| RETURN_CONST | 5,671,308 | 9.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,719,902 | 7.5% |
| STORE_FAST_LOAD_FAST | 4,156,210 | 6.6% |
| LOAD_FAST | 4,093,925 | 6.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,602,761 | 87.5% |
| GET_ITER | 809,084 | 6.7% |
| EXTENDED_ARG | 642,400 | 5.3% |
| SWAP | 38,880 | 0.3% |
| LOAD_FAST | 29,360 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,753,501 | 88.7% |
| RETURN_CONST | 629,865 | 5.2% |
| STORE_FAST_LOAD_FAST | 500,000 | 4.1% |
| LOAD_FAST | 195,180 | 1.6% |
| SWAP | 38,520 | 0.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,268,260 | 64.0% |
| GET_ITER | 9,973,191 | 28.6% |
| EXTENDED_ARG | 1,740,040 | 5.0% |
| LOAD_FAST | 518,367 | 1.5% |
| SWAP | 298,981 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,956,122 | 68.8% |
| LOAD_FAST | 7,494,563 | 21.5% |
| RETURN_CONST | 788,798 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 710,008 | 2.0% |
| LOAD_GLOBAL_MODULE | 602,500 | 1.7% |


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
| LOAD_FAST | 5,501,022 | 60.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,616 | 11.6% |
| LOAD_DEREF | 1,058,076 | 11.5% |
| COPY | 956,400 | 10.4% |
| LOAD_GLOBAL_MODULE | 571,145 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,560,358 | 17.0% |
| CALL_BUILTIN_FAST | 1,337,014 | 14.6% |
| POP_JUMP_IF_NOT_NONE | 1,224,918 | 13.3% |
| STORE_FAST | 1,075,776 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,616 | 11.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,135,103 | 86.3% |
| RETURN_VALUE | 4,635,473 | 5.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,116,160 | 3.4% |
| LOAD_GLOBAL_MODULE | 1,983,465 | 2.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,560,358 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,844,480 | 34.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,524,903 | 26.7% |
| CALL_PY_EXACT_ARGS | 21,014,242 | 22.9% |
| LOAD_CONST | 4,054,656 | 4.4% |
| LOAD_DEREF | 3,320,058 | 3.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 22,297,414 | 71.8% |
| LOAD_ATTR_SLOT | 4,711,557 | 15.2% |
| LOAD_FAST | 3,706,965 | 11.9% |
| STORE_FAST_LOAD_FAST | 157,680 | 0.5% |
| LOAD_ATTR | 147,499 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,115,637 | 48.7% |
| LOAD_FAST_LOAD_FAST | 10,797,536 | 34.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,807,474 | 15.5% |
| CALL_PY_EXACT_ARGS | 314,918 | 1.0% |
| LOAD_CONST | 6,851 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,261,015 | 99.2% |
| LOAD_FAST | 5,540 | 0.4% |
| LOAD_ATTR_MODULE | 2,640 | 0.2% |
| LOAD_ATTR | 1,403 | 0.1% |
| LOAD_FAST_LOAD_FAST | 1,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,044,197 | 82.1% |
| CALL_PY_EXACT_ARGS | 80,641 | 6.3% |
| CALL | 57,380 | 4.5% |
| LOAD_FAST | 26,100 | 2.1% |
| LOAD_ATTR_SLOT | 15,920 | 1.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,467,943 | 92.5% |
| LOAD_DEREF | 3,109,100 | 5.3% |
| BINARY_SUBSCR_LIST_INT | 342,120 | 0.6% |
| STORE_FAST_LOAD_FAST | 236,807 | 0.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 236,792 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 44,300,805 | 75.3% |
| CALL_BUILTIN_O | 5,611,882 | 9.5% |
| BUILD_TUPLE | 2,484,120 | 4.2% |
| LOAD_FAST | 1,920,865 | 3.3% |
| BINARY_OP_MULTIPLY_INT | 1,668,682 | 2.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,003,730 | 60.9% |
| LOAD_FAST_LOAD_FAST | 478,940 | 29.1% |
| LOAD_DEREF | 144,340 | 8.8% |
| LOAD_ATTR | 12,020 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,933 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 478,200 | 29.0% |
| TO_BOOL_STR | 478,200 | 29.0% |
| TO_BOOL_BOOL | 409,863 | 24.9% |
| LOAD_CONST | 106,520 | 6.5% |
| CALL_LEN | 73,480 | 4.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,481,076 | 94.6% |
| RETURN_VALUE | 642,369 | 2.3% |
| STORE_FAST_LOAD_FAST | 319,456 | 1.1% |
| LOAD_DEREF | 217,200 | 0.8% |
| LOAD_FAST_LOAD_FAST | 168,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,812,026 | 67.2% |
| COPY_FREE_VARS | 5,060,870 | 18.1% |
| GET_ITER | 1,920,350 | 6.9% |
| TO_BOOL_BOOL | 728,888 | 2.6% |
| STORE_FAST | 505,361 | 1.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,196,531 | 99.1% |
| LOAD_ATTR_SLOT | 613,588 | 0.6% |
| LOAD_FAST_LOAD_FAST | 88,058 | 0.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 72,529 | 0.1% |
| STORE_FAST_LOAD_FAST | 21,704 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,431,216 | 34.8% |
| STORE_FAST | 22,509,317 | 23.4% |
| LOAD_DEREF | 6,402,802 | 6.7% |
| LOAD_FAST | 5,219,850 | 5.4% |
| LOAD_CONST | 5,209,839 | 5.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 57,999,739 | 24.8% |
| RESUME_CHECK | 41,287,385 | 17.7% |
| STORE_FAST | 37,716,082 | 16.1% |
| STORE_FAST_STORE_FAST | 22,022,759 | 9.4% |
| LOAD_FAST | 20,511,871 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,937,836 | 69.7% |
| LOAD_FAST_LOAD_FAST | 28,996,857 | 12.4% |
| CALL_ISINSTANCE | 19,054,887 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 9,008,871 | 3.9% |
| LOAD_DEREF | 3,364,828 | 1.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,851,505 | 54.1% |
| STORE_FAST | 18,254,110 | 12.5% |
| RESUME_CHECK | 16,027,094 | 11.0% |
| POP_JUMP_IF_FALSE | 9,686,175 | 6.6% |
| NOP | 6,492,436 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 57,024,374 | 39.1% |
| CALL_ISINSTANCE | 35,897,553 | 24.6% |
| LOAD_FAST | 29,774,772 | 20.4% |
| CONTAINS_OP | 5,290,222 | 3.6% |
| LOAD_FAST_LOAD_FAST | 3,332,712 | 2.3% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,104,448 | 93.5% |
| LOAD_DEREF | 77,300 | 6.5% |
| LOAD_SUPER_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,181,848 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,813,622 | 100.0% |
| LOAD_SUPER_ATTR | 500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,539,388 | 84.9% |
| LOAD_GLOBAL_MODULE | 172,234 | 9.5% |
| LOAD_FAST | 84,580 | 4.7% |
| LOAD_FAST_LOAD_FAST | 17,560 | 1.0% |
| CALL | 360 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 99,186,466 | 38.4% |
| CALL_PY_EXACT_ARGS | 51,008,736 | 19.8% |
| COPY_FREE_VARS | 21,813,248 | 8.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 21,649,219 | 8.4% |
| LOAD_ATTR_PROPERTY | 18,812,026 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 115,548,335 | 44.8% |
| LOAD_GLOBAL_BUILTIN | 41,287,385 | 16.0% |
| NOP | 21,361,760 | 8.3% |
| LOAD_FAST_LOAD_FAST | 19,950,557 | 7.7% |
| LOAD_GLOBAL_MODULE | 16,027,094 | 6.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 661,220 | 64.2% |
| LOAD_CONST | 367,900 | 35.7% |
| SEND | 620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 646,240 | 62.8% |
| POP_TOP | 352,840 | 34.3% |
| YIELD_VALUE | 15,060 | 1.5% |
| END_SEND | 15,020 | 1.5% |
| SEND | 580 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,103,446 | 62.6% |
| SWAP | 956,400 | 28.5% |
| LOAD_FAST_LOAD_FAST | 259,600 | 7.7% |
| LOAD_ATTR_SLOT | 35,135 | 1.0% |
| STORE_ATTR | 3,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,210,551 | 36.0% |
| RETURN_CONST | 887,236 | 26.4% |
| NOP | 480,100 | 14.3% |
| RETURN_VALUE | 478,260 | 14.2% |
| LOAD_FAST_LOAD_FAST | 122,720 | 3.7% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,731,831 | 52.2% |
| LOAD_FAST | 4,284,334 | 47.3% |
| STORE_ATTR_SLOT | 41,766 | 0.5% |
| STORE_ATTR | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,672,611 | 51.6% |
| LOAD_FAST_LOAD_FAST | 2,255,925 | 24.9% |
| LOAD_CONST | 1,890,430 | 20.9% |
| LOAD_GLOBAL_MODULE | 136,839 | 1.5% |
| RETURN_CONST | 45,660 | 0.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,574,095 | 68.9% |
| LOAD_FAST | 397,942 | 17.4% |
| CALL_TUPLE_1 | 181,360 | 7.9% |
| RETURN_VALUE | 82,840 | 3.6% |
| LOAD_CONST | 39,335 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,660,515 | 72.7% |
| EXTENDED_ARG | 226,722 | 9.9% |
| LOAD_FAST_LOAD_FAST | 184,960 | 8.1% |
| LOAD_FAST | 165,801 | 7.3% |
| LOAD_GLOBAL_MODULE | 38,955 | 1.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,835,523 | 92.7% |
| SWAP | 1,208,120 | 5.9% |
| BINARY_SUBSCR_DICT | 112,800 | 0.6% |
| LOAD_FAST | 99,410 | 0.5% |
| BINARY_OP_SUBTRACT_INT | 49,280 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,107,791 | 49.7% |
| LOAD_FAST_LOAD_FAST | 10,014,362 | 49.3% |
| LOAD_CONST | 160,200 | 0.8% |
| LOAD_FAST | 21,140 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 21,060 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,414 | 98.7% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| STORE_FAST_LOAD_FAST | 1,240 | 0.5% |
| TO_BOOL | 386 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 217,404 | 95.2% |
| POP_JUMP_IF_FALSE | 9,587 | 4.2% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| TO_BOOL | 49 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 59,841,461 | 34.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 44,300,805 | 25.7% |
| LOAD_FAST | 21,618,755 | 12.5% |
| CALL_BUILTIN_FAST | 18,102,932 | 10.5% |
| CALL_BUILTIN_O | 9,900,062 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 111,640,595 | 64.6% |
| POP_JUMP_IF_TRUE | 54,455,607 | 31.5% |
| EXTENDED_ARG | 5,485,828 | 3.2% |
| UNARY_NOT | 1,118,640 | 0.6% |
| TO_BOOL_NONE | 1,280 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,367,636 | 93.3% |
| BINARY_OP | 732,762 | 3.7% |
| BINARY_SUBSCR_LIST_INT | 485,260 | 2.5% |
| BINARY_SUBSCR_TUPLE_INT | 63,352 | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 24,859 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,557,172 | 53.6% |
| POP_JUMP_IF_TRUE | 9,136,899 | 46.4% |
| TO_BOOL_NONE | 440 | 0.0% |
| UNARY_NOT | 165 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,234,235 | 97.0% |
| COPY | 39,560 | 1.7% |
| LOAD_DEREF | 10,869 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 8,780 | 0.4% |
| STORE_FAST | 6,240 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 834,143 | 36.2% |
| POP_JUMP_IF_TRUE | 784,454 | 34.1% |
| UNARY_NOT | 661,852 | 28.7% |
| EXTENDED_ARG | 21,480 | 0.9% |
| TO_BOOL_NONE | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,841,292 | 68.0% |
| RETURN_VALUE | 389,090 | 14.4% |
| LOAD_ATTR_PROPERTY | 292,802 | 10.8% |
| CALL_METHOD_DESCRIPTOR_O | 104,000 | 3.8% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 41,928 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,943,396 | 71.8% |
| POP_JUMP_IF_TRUE | 745,451 | 27.5% |
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
| POP_JUMP_IF_FALSE | 513,460 | 98.8% |
| POP_JUMP_IF_TRUE | 6,300 | 1.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120,292 | 66.8% |
| RETURN_VALUE | 49,120 | 27.3% |
| CALL_BUILTIN_CLASS | 2,600 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 1,880 | 1.0% |
| FOR_ITER_LIST | 1,880 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 114,940 | 63.8% |
| STORE_FAST_STORE_FAST | 65,112 | 36.2% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 884,828 | 54.3% |
| RETURN_VALUE | 660,878 | 40.5% |
| STORE_FAST | 79,520 | 4.9% |
| CALL_METHOD_DESCRIPTOR_O | 3,680 | 0.2% |
| UNPACK_SEQUENCE | 1,139 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,436,119 | 88.1% |
| STORE_FAST | 154,746 | 9.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 39,760 | 2.4% |
| STORE_DEREF | 120 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 71,232,970 | 68.6% |
| RETURN_VALUE | 19,466,404 | 18.7% |
| BINARY_SUBSCR_LIST_INT | 7,538,675 | 7.3% |
| FOR_ITER_LIST | 4,719,902 | 4.5% |
| FOR_ITER_TUPLE | 710,008 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 99,126,782 | 95.4% |
| STORE_DEREF | 4,491,620 | 4.3% |
| STORE_FAST | 257,627 | 0.2% |
| STORE_NAME | 18,940 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,680 | 0.0% |


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
|     deferred | 35,267,575 | 65.2% |
|          hit | 18,794,990 | 34.7% |
|         miss | 120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,770 | 11.7% |
| Failure | 51,324 | 88.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 9,458 | 18.4% |
| multiply different types | 7,463 | 14.5% |
| subtract other | 6,800 | 13.2% |
| and int | 4,141 | 8.1% |
| rshift | 3,824 | 7.5% |
| or | 3,700 | 7.2% |
| power | 2,861 | 5.6% |
| true divide different types | 2,523 | 4.9% |
| multiply other | 2,360 | 4.6% |
| remainder | 2,314 | 4.5% |
| add different types | 1,938 | 3.8% |
| floor divide | 1,272 | 2.5% |
| subtract different types | 1,186 | 2.3% |
| xor | 583 | 1.1% |
| and other | 373 | 0.7% |
| true divide other | 300 | 0.6% |
| lshift | 225 | 0.4% |
| true divide float | 3 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> specialization stats for BINARY_OP_INPLACE_ADD_UNICODE family </summary>


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
|     deferred | 24,069,705 | 36.0% |
|          hit | 42,661,317 | 63.9% |
|         miss | 45,540 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,356 | 32.2% |
| Failure | 17,615 | 67.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 12,192 | 69.2% |
| out of range | 3,640 | 20.7% |
| buffer int | 1,760 | 10.0% |
| array int | 20 | 0.1% |
| tuple slice | 3 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 26,132,867 | 5.9% |
|        deopt | 31,040 | 0.0% |
|          hit | 384,641,385 | 86.8% |
|         miss | 31,490,977 | 7.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 674,610 | 90.3% |
| Failure | 72,859 | 9.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class mutable | 28,603 | 39.3% |
| code complex parameters | 14,050 | 19.3% |
| class no vectorcall | 9,220 | 12.7% |
| cfunc varargs keywords | 6,384 | 8.8% |
| other | 3,040 | 4.2% |
| wrong number arguments | 2,520 | 3.5% |
| cfunc noargs | 2,400 | 3.3% |
| bound method | 2,168 | 3.0% |
| meth descr varargs | 1,914 | 2.6% |
| no dict | 1,120 | 1.5% |
| meth descr varargs keywords | 640 | 0.9% |
| operator wrapper | 380 | 0.5% |
| cfunc varargs | 240 | 0.3% |
| meth descr method fastcall keywords | 180 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 38,468,908 | 36.7% |
|          hit | 65,696,986 | 62.7% |
|         miss | 576,878 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20,487 | 22.8% |
| Failure | 69,355 | 77.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 18,531 | 26.7% |
| other | 15,215 | 21.9% |
| different types | 12,282 | 17.7% |
| tuple | 10,042 | 14.5% |
| string | 9,960 | 14.4% |
| bool | 2,126 | 3.1% |
| float long | 340 | 0.5% |
| baseobject | 280 | 0.4% |
| set | 279 | 0.4% |
| list | 220 | 0.3% |
| long float | 80 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 103,834,065 | 48.5% |
|          hit | 108,444,420 | 50.7% |
|         miss | 1,553,471 | 0.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 41,180 | 29.8% |
| Failure | 96,824 | 70.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 68,631 | 70.9% |
| set | 9,045 | 9.3% |
| zip | 7,600 | 7.8% |
| enumerate | 4,228 | 4.4% |
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
|     deferred | 120,200,991 | 27.3% |
|        deopt | 20 | 0.0% |
|          hit | 250,481,634 | 57.0% |
|         miss | 67,428,348 | 15.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,349,981 | 89.4% |
| Failure | 160,099 | 10.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 60,829 | 38.0% |
| mutable class | 58,758 | 36.7% |
| method | 10,459 | 6.5% |
| has managed dict | 8,780 | 5.5% |
| overridden | 8,666 | 5.4% |
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
|     deferred | 89,867 | 0.0% |
|          hit | 379,546,827 | 99.9% |
|         miss | 20,420 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 91,944 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 604 | 0.0% |
|          hit | 2,995,970 | 100.0% |

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
|     deferred | 439,140 | 29.8% |
|          hit | 999,080 | 67.8% |
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
|     deferred | 540,551 | 4.2% |
|          hit | 10,196,722 | 78.4% |
|         miss | 2,220,850 | 17.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 46,826 | 92.3% |
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
|     deferred | 3,421,703 | 13.1% |
|          hit | 22,610,187 | 86.8% |

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
|     deferred | 12,841,846 | 6.1% |
|          hit | 197,715,435 | 93.7% |
|         miss | 439,533 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 59,918 | 72.2% |
| Failure | 23,025 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 10,778 | 46.8% |
| number | 3,512 | 15.3% |
| mapping | 3,300 | 14.3% |
| dict | 2,340 | 10.2% |
| other | 1,633 | 7.1% |
| set | 1,422 | 6.2% |
| float | 40 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 27,482 | 0.0% |
|          hit | 105,710,766 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 11,388 | 93.6% |
| Failure | 773 | 6.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 713 | 92.2% |
| iterator | 60 | 7.8% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 3,221,595,419 | 54.1% |
| Not specialized | 800,471,160 | 13.5% |
| Specialized hits | 1,825,021,506 | 30.7% |
| Specialized misses | 103,806,797 | 1.7% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 120,200,991 | 32.9% |
| FOR_ITER | 103,834,065 | 28.4% |
| COMPARE_OP | 38,468,908 | 10.5% |
| BINARY_OP | 35,267,575 | 9.7% |
| CALL | 26,132,867 | 7.2% |
| BINARY_SUBSCR | 24,069,705 | 6.6% |
| TO_BOOL | 12,841,846 | 3.5% |
| STORE_SUBSCR | 3,421,703 | 0.9% |
| STORE_ATTR | 540,551 | 0.1% |
| SEND | 439,140 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 36,601,634 | 35.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 17,001,915 | 16.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 14,437,025 | 13.9% |
| LOAD_ATTR_METHOD_NO_DICT | 9,216,688 | 8.9% |
| CALL_PY_EXACT_ARGS | 7,817,222 | 7.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,479,222 | 6.2% |
| LOAD_ATTR_PROPERTY | 4,123,775 | 4.0% |
| CALL_BUILTIN_O | 2,661,130 | 2.6% |
| STORE_ATTR_SLOT | 2,219,870 | 2.1% |
| FOR_ITER_TUPLE | 783,760 | 0.8% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 127,611,766 | 46.8% |
| Calls to Python functions inlined | 144,807,682 | 53.2% |
| Calls via PyEval_EvalFrame (total) | 127,611,766 | 46.8% |
| Calls via PyEval_EvalFrame (vector) | 98,449,016 | 36.1% |
| Calls via PyEval_EvalFrame (generator) | 29,162,750 | 10.7% |
| Calls via PyEval_EvalFrame (legacy) | 4,640 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 98,441,716 | 36.1% |
| Calls via PyEval_EvalFrame (build class) | 2,660 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 23,667,145 | 8.7% |
| Calls via PyEval_EvalFrame (function ex) | 11,824,718 | 4.3% |
| Calls via PyEval_EvalFrame (api) | 53,323,678 | 19.6% |
| Calls via PyEval_EvalFrame (method) | 6,960 | 0.0% |
| Frame objects created | 1,286,802 | 0.5% |
| Frames pushed | 112,565,457 | 41.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 363,407,392 | 54.3% |
| Frees to freelist | 363,650,268 |  |
| Allocations | 305,554,336 | 45.7% |
| Allocations to 512 bytes | 304,497,480 | 45.5% |
| Allocations to 4 kbytes | 1,032,396 | 0.2% |
| Allocations over 4 kbytes | 24,460 | 0.0% |
| Frees | 313,239,499 |  |
| New values | 1,057,183 |  |
| Interpreter increfs | 2,568,795,044 | 64.2% |
| Interpreter decrefs | 2,994,207,104 | 65.4% |
| Increfs | 1,430,311,539 | 35.8% |
| Decrefs | 1,585,630,259 | 34.6% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 60 | 0.0% |
| Method cache hits | 242,964,396 |  |
| Method cache misses | 4,543,451 |  |
| Method cache collisions | 5,834,412 |  |
| Method cache dunder hits | 347,251,074 |  |
| Method cache dunder misses | 1,291,451 |  |


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

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 80 |


</details>

---
Stats gathered on: 2024-09-10
