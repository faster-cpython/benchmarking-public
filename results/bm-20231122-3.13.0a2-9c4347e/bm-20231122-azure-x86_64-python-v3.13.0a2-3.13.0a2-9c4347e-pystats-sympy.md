
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
| LOAD_FAST | 976,461,008 | 16.4% | 16.4% |  |
| STORE_FAST | 359,063,201 | 6.0% | 22.4% |  |
| POP_JUMP_IF_FALSE | 291,877,927 | 4.9% | 27.4% |  |
| RESUME_CHECK | 257,916,242 | 4.3% | 31.7% |  |
| LOAD_FAST_LOAD_FAST | 254,135,458 | 4.3% | 36.0% |  |
| LOAD_GLOBAL_BUILTIN | 233,849,444 | 3.9% | 39.9% | 0.0% |
| LOAD_CONST | 191,442,821 | 3.2% | 43.1% |  |
| RETURN_VALUE | 177,417,460 | 3.0% | 46.1% |  |
| TO_BOOL_BOOL | 172,716,301 | 2.9% | 49.0% | 0.1% |
| JUMP_BACKWARD | 156,533,579 | 2.6% | 51.6% |  |
| LOAD_GLOBAL_MODULE | 145,745,049 | 2.4% | 54.1% | 0.0% |
| INTERPRETER_EXIT | 127,258,084 | 2.1% | 56.2% |  |
| LOAD_ATTR | 121,721,450 | 2.0% | 58.3% |  |
| STORE_FAST_STORE_FAST | 105,710,241 | 1.8% | 60.0% |  |
| FOR_ITER | 103,821,011 | 1.7% | 61.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 103,756,409 | 1.7% | 63.5% |  |
| LOAD_ATTR_SLOT | 96,028,170 | 1.6% | 65.1% | 38.1% |
| LOAD_ATTR_METHOD_NO_DICT | 91,697,102 | 1.5% | 66.7% | 10.1% |
| POP_JUMP_IF_TRUE | 80,560,417 | 1.4% | 68.0% |  |
| LOAD_DEREF | 68,653,455 | 1.2% | 69.2% |  |
| CALL_PY_EXACT_ARGS | 68,148,125 | 1.1% | 70.3% | 11.5% |
| CALL_ISINSTANCE | 67,458,121 | 1.1% | 71.5% |  |
| FOR_ITER_LIST | 62,870,744 | 1.1% | 72.5% | 1.2% |
| POP_TOP | 61,583,306 | 1.0% | 73.6% |  |
| PUSH_NULL | 60,708,218 | 1.0% | 74.6% |  |
| GET_ITER | 60,060,791 | 1.0% | 75.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 58,867,872 | 1.0% | 76.6% | 28.9% |
| RETURN_CONST | 57,286,786 | 1.0% | 77.5% |  |
| BUILD_TUPLE | 56,992,155 | 1.0% | 78.5% |  |
| CONTAINS_OP | 52,188,795 | 0.9% | 79.4% |  |
| COMPARE_OP_INT | 51,172,241 | 0.9% | 80.2% | 1.1% |
| IS_OP | 47,648,329 | 0.8% | 81.0% |  |
| SWAP | 45,312,067 | 0.8% | 81.8% |  |
| CALL_BUILTIN_FAST | 43,496,501 | 0.7% | 82.5% |  |
| POP_JUMP_IF_NONE | 41,255,968 | 0.7% | 83.2% |  |
| CALL_BUILTIN_O | 39,878,524 | 0.7% | 83.9% | 6.7% |
| COMPARE_OP | 38,576,995 | 0.6% | 84.5% |  |
| BINARY_OP | 35,326,582 | 0.6% | 85.1% |  |
| FOR_ITER_TUPLE | 34,831,860 | 0.6% | 85.7% | 2.3% |
| BUILD_MAP | 33,796,581 | 0.6% | 86.3% |  |
| NOP | 33,473,592 | 0.6% | 86.8% |  |
| COPY_FREE_VARS | 31,797,366 | 0.5% | 87.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 30,909,616 | 0.5% | 87.9% | 0.4% |
| BINARY_SUBSCR_LIST_INT | 30,205,995 | 0.5% | 88.4% | 0.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 29,538,153 | 0.5% | 88.9% | 21.9% |
| CALL_LEN | 28,098,464 | 0.5% | 89.4% |  |
| CALL_FUNCTION_EX | 28,012,799 | 0.5% | 89.9% |  |
| LOAD_ATTR_PROPERTY | 28,007,288 | 0.5% | 90.3% | 14.7% |
| CALL | 26,850,543 | 0.5% | 90.8% |  |
| BINARY_SUBSCR | 24,128,622 | 0.4% | 91.2% |  |
| CALL_LIST_APPEND | 24,016,233 | 0.4% | 91.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 23,522,643 | 0.4% | 92.0% | 0.2% |
| DICT_MERGE | 23,272,271 | 0.4% | 92.4% |  |
| YIELD_VALUE | 22,911,790 | 0.4% | 92.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 21,912,460 | 0.4% | 93.1% | 65.2% |
| BUILD_LIST | 21,625,696 | 0.4% | 93.5% |  |
| EXTENDED_ARG | 21,423,791 | 0.4% | 93.8% |  |
| STORE_SUBSCR_LIST_INT | 20,340,986 | 0.3% | 94.2% |  |
| TO_BOOL_INT | 19,695,732 | 0.3% | 94.5% | 0.1% |
| POP_JUMP_IF_NOT_NONE | 18,158,311 | 0.3% | 94.8% |  |
| LOAD_FAST_AND_CLEAR | 16,788,182 | 0.3% | 95.1% |  |
| CALL_TYPE_1 | 16,712,537 | 0.3% | 95.4% |  |
| COMPARE_OP_STR | 14,565,084 | 0.2% | 95.6% |  |
| RETURN_GENERATOR | 14,344,741 | 0.2% | 95.9% |  |
| MAKE_FUNCTION | 14,300,030 | 0.2% | 96.1% |  |
| BINARY_OP_ADD_INT | 12,978,099 | 0.2% | 96.3% |  |
| TO_BOOL | 12,925,199 | 0.2% | 96.5% |  |
| FOR_ITER_RANGE | 12,131,426 | 0.2% | 96.8% |  |
| CALL_KW | 10,673,104 | 0.2% | 96.9% |  |
| SET_FUNCTION_ATTRIBUTE | 10,425,747 | 0.2% | 97.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 9,176,836 | 0.2% | 97.3% | 0.0% |
| CALL_BUILTIN_CLASS | 9,149,493 | 0.2% | 97.4% |  |
| STORE_ATTR_SLOT | 9,060,156 | 0.2% | 97.6% | 24.5% |
| BINARY_SUBSCR_TUPLE_INT | 8,996,172 | 0.2% | 97.7% | 0.1% |
| IMPORT_FROM | 8,954,749 | 0.2% | 97.9% |  |
| STORE_DEREF | 8,695,177 | 0.1% | 98.0% |  |
| MAP_ADD | 7,866,071 | 0.1% | 98.1% |  |
| IMPORT_NAME | 7,759,597 | 0.1% | 98.3% |  |
| LIST_APPEND | 6,188,198 | 0.1% | 98.4% |  |
| MAKE_CELL | 6,049,033 | 0.1% | 98.5% |  |
| JUMP_FORWARD | 5,902,745 | 0.1% | 98.6% |  |
| CALL_TUPLE_1 | 5,851,558 | 0.1% | 98.7% | 0.0% |
| STORE_FAST_LOAD_FAST | 5,345,598 | 0.1% | 98.8% |  |
| UNARY_NOT | 5,307,607 | 0.1% | 98.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,171,745 | 0.1% | 98.9% | 0.1% |
| COPY | 4,908,507 | 0.1% | 99.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 4,647,616 | 0.1% | 99.1% | 0.2% |
| CALL_PY_WITH_DEFAULTS | 4,598,003 | 0.1% | 99.2% | 0.6% |
| STORE_SUBSCR | 3,428,694 | 0.1% | 99.2% |  |
| STORE_ATTR_INSTANCE_VALUE | 3,358,729 | 0.1% | 99.3% | 0.0% |
| BINARY_SUBSCR_DICT | 3,348,933 | 0.1% | 99.4% |  |
| BINARY_OP_MULTIPLY_INT | 2,771,521 | 0.0% | 99.4% | 0.0% |
| TO_BOOL_NONE | 2,708,996 | 0.0% | 99.4% | 8.4% |
| BINARY_OP_SUBTRACT_INT | 2,486,777 | 0.0% | 99.5% |  |
| TO_BOOL_LIST | 2,302,484 | 0.0% | 99.5% | 0.5% |
| STORE_SUBSCR_DICT | 2,283,397 | 0.0% | 99.6% |  |
| LOAD_SUPER_ATTR_METHOD | 1,814,141 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,646,863 | 0.0% | 99.6% | 20.6% |
| UNPACK_SEQUENCE_TUPLE | 1,631,164 | 0.0% | 99.7% |  |
| LOAD_FAST_CHECK | 1,578,337 | 0.0% | 99.7% |  |
| LIST_EXTEND | 1,349,088 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 1,349,048 | 0.0% | 99.7% |  |
| DELETE_FAST | 1,302,220 | 0.0% | 99.7% |  |
| LOAD_ATTR_MODULE | 1,271,821 | 0.0% | 99.8% | 0.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,964 | 0.0% | 99.8% |  |
| SEND_GEN | 1,029,788 | 0.0% | 99.8% | 3.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 928,560 | 0.0% | 99.8% |  |
| CHECK_EXC_MATCH | 906,324 | 0.0% | 99.8% |  |
| POP_EXCEPT | 906,324 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 906,324 | 0.0% | 99.9% |  |
| UNARY_NEGATIVE | 613,311 | 0.0% | 99.9% |  |
| STORE_ATTR | 591,375 | 0.0% | 99.9% |  |
| BINARY_SLICE | 569,045 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_UNICODE | 563,580 | 0.0% | 99.9% |  |
| COMPARE_OP_FLOAT | 543,654 | 0.0% | 99.9% | 0.3% |
| GET_YIELD_FROM_ITER | 540,368 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 519,760 | 0.0% | 99.9% |  |
| END_SEND | 519,360 | 0.0% | 99.9% |  |
| SEND | 442,840 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 284,520 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 284,480 | 0.0% | 100.0% |  |
| CALL_STR_1 | 233,240 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 228,443 | 0.0% | 100.0% | 36.3% |
| FOR_ITER_GEN | 191,406 | 0.0% | 100.0% | 0.2% |
| LOAD_ATTR_CLASS | 187,600 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 181,800 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_LIST | 180,063 | 0.0% | 100.0% |  |
| LOAD_NAME | 178,820 | 0.0% | 100.0% |  |
| STORE_NAME | 167,980 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 159,238 | 0.0% | 100.0% |  |
| BUILD_STRING | 141,900 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 129,347 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 119,072 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 95,920 | 0.0% | 100.0% | 0.2% |
| EXIT_INIT_CHECK | 95,600 | 0.0% | 100.0% |  |
| BUILD_SET | 50,375 | 0.0% | 100.0% |  |
| RESUME | 47,560 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 39,709 | 0.0% | 100.0% |  |
| BEFORE_WITH | 37,420 | 0.0% | 100.0% |  |
| END_FOR | 22,544 | 0.0% | 100.0% |  |
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
| STORE_FAST LOAD_FAST | 196,232,244 | 3.3% | 3.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 162,951,522 | 2.7% | 6.0% |
| RESUME_CHECK LOAD_FAST | 115,568,674 | 1.9% | 8.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 113,723,714 | 1.9% | 9.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 111,645,385 | 1.9% | 11.8% |
| CACHE RESUME_CHECK | 99,027,216 | 1.7% | 13.4% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 98,983,211 | 1.7% | 15.1% |
| LOAD_FAST LOAD_ATTR_SLOT | 95,194,916 | 1.6% | 16.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 79,145,780 | 1.3% | 18.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 78,854,084 | 1.3% | 19.4% |
| RETURN_VALUE INTERPRETER_EXIT | 72,900,781 | 1.2% | 20.6% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 71,074,712 | 1.2% | 21.8% |
| LOAD_FAST LOAD_CONST | 69,887,286 | 1.2% | 22.9% |
| JUMP_BACKWARD FOR_ITER | 68,431,050 | 1.2% | 24.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 62,569,124 | 1.1% | 25.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 59,843,510 | 1.0% | 26.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 58,001,770 | 1.0% | 27.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 57,025,710 | 1.0% | 28.1% |
| LOAD_FAST LOAD_ATTR | 55,273,693 | 0.9% | 29.0% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 54,477,727 | 0.9% | 29.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 54,464,852 | 0.9% | 30.8% |
| LOAD_FAST RETURN_VALUE | 53,596,955 | 0.9% | 31.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 51,027,110 | 0.9% | 32.6% |
| JUMP_BACKWARD FOR_ITER_LIST | 46,550,715 | 0.8% | 33.4% |
| PUSH_NULL LOAD_FAST | 46,538,881 | 0.8% | 34.2% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 45,435,329 | 0.8% | 34.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT TO_BOOL_BOOL | 44,303,086 | 0.7% | 35.7% |
| FOR_ITER_LIST STORE_FAST | 43,131,622 | 0.7% | 36.4% |
| STORE_FAST_STORE_FAST LOAD_FAST | 41,970,109 | 0.7% | 37.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 41,289,858 | 0.7% | 37.8% |
| LOAD_CONST LOAD_CONST | 40,444,592 | 0.7% | 38.5% |
| RETURN_VALUE STORE_FAST | 38,559,551 | 0.6% | 39.1% |
| POP_JUMP_IF_TRUE LOAD_FAST | 38,017,550 | 0.6% | 39.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 37,717,646 | 0.6% | 40.4% |
| LOAD_ATTR STORE_FAST | 36,817,948 | 0.6% | 41.0% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 35,898,734 | 0.6% | 41.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 35,529,819 | 0.6% | 42.2% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 34,393,990 | 0.6% | 42.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 34,112,302 | 0.6% | 43.4% |
| LOAD_ATTR_SLOT RETURN_VALUE | 33,432,481 | 0.6% | 43.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 33,136,134 | 0.6% | 44.5% |
| RETURN_CONST INTERPRETER_EXIT | 32,283,763 | 0.5% | 45.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 31,845,523 | 0.5% | 45.6% |
| IS_OP POP_JUMP_IF_FALSE | 30,048,840 | 0.5% | 46.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 29,777,229 | 0.5% | 46.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 29,346,650 | 0.5% | 47.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 28,997,668 | 0.5% | 47.6% |
| LOAD_FAST PUSH_NULL | 28,418,035 | 0.5% | 48.0% |
| LOAD_FAST CALL_LEN | 27,057,199 | 0.5% | 48.5% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 27,001,865 | 0.5% | 48.9% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 26,483,976 | 0.4% | 49.4% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 25,639,709 | 0.4% | 49.8% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 24,744,978 | 0.4% | 50.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 24,532,137 | 0.4% | 50.6% |
| LOAD_CONST CALL_BUILTIN_FAST | 24,272,023 | 0.4% | 51.1% |
| BINARY_OP STORE_FAST | 24,216,989 | 0.4% | 51.5% |
| POP_TOP JUMP_BACKWARD | 23,964,448 | 0.4% | 51.9% |
| FOR_ITER_TUPLE STORE_FAST | 23,957,126 | 0.4% | 52.3% |
| DICT_MERGE CALL_FUNCTION_EX | 23,272,271 | 0.4% | 52.7% |
| BUILD_MAP LOAD_FAST | 23,183,088 | 0.4% | 53.0% |
| LOAD_FAST DICT_MERGE | 23,143,373 | 0.4% | 53.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 22,709,169 | 0.4% | 53.8% |
| LOAD_ATTR_SLOT STORE_FAST | 22,510,282 | 0.4% | 54.2% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 22,277,135 | 0.4% | 54.6% |
| LOAD_DEREF LOAD_ATTR_METHOD_WITH_VALUES | 22,156,436 | 0.4% | 54.9% |
| YIELD_VALUE INTERPRETER_EXIT | 22,065,800 | 0.4% | 55.3% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_BUILTIN | 22,030,526 | 0.4% | 55.7% |
| STORE_FAST_STORE_FAST LOAD_DEREF | 21,987,532 | 0.4% | 56.1% |
| COPY_FREE_VARS RESUME_CHECK | 21,815,796 | 0.4% | 56.4% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 21,656,794 | 0.4% | 56.8% |
| LOAD_FAST GET_ITER | 21,637,962 | 0.4% | 57.1% |
| LOAD_FAST TO_BOOL_BOOL | 21,619,608 | 0.4% | 57.5% |
| RESUME_CHECK NOP | 21,364,033 | 0.4% | 57.9% |
| BUILD_TUPLE RETURN_VALUE | 21,221,920 | 0.4% | 58.2% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 21,088,596 | 0.4% | 58.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 21,015,699 | 0.4% | 58.9% |
| LOAD_CONST COMPARE_OP_INT | 20,987,704 | 0.4% | 59.3% |
| POP_JUMP_IF_NONE JUMP_BACKWARD | 20,909,998 | 0.4% | 59.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 20,512,646 | 0.3% | 60.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 20,138,555 | 0.3% | 60.3% |
| LOAD_ATTR CONTAINS_OP | 20,047,462 | 0.3% | 60.7% |
| GET_ITER FOR_ITER | 20,010,270 | 0.3% | 61.0% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 19,966,071 | 0.3% | 61.3% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 19,466,566 | 0.3% | 61.7% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 19,055,433 | 0.3% | 62.0% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 18,849,697 | 0.3% | 62.3% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 18,813,794 | 0.3% | 62.6% |
| LOAD_FAST TO_BOOL_INT | 18,368,442 | 0.3% | 62.9% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 18,325,513 | 0.3% | 63.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 18,255,105 | 0.3% | 63.5% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 18,103,485 | 0.3% | 63.8% |
| LOAD_FAST CALL_BUILTIN_O | 17,812,500 | 0.3% | 64.1% |
| CALL_LIST_APPEND JUMP_BACKWARD | 17,343,472 | 0.3% | 64.4% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 17,273,586 | 0.3% | 64.7% |
| LOAD_ATTR IS_OP | 17,248,423 | 0.3% | 65.0% |
| LOAD_FAST BUILD_TUPLE | 17,185,399 | 0.3% | 65.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 16,718,815 | 0.3% | 65.6% |
| LOAD_FAST CALL_TYPE_1 | 16,589,644 | 0.3% | 65.9% |
| LOAD_FAST CALL_LIST_APPEND | 16,419,852 | 0.3% | 66.1% |
| LOAD_ATTR LOAD_FAST | 16,056,936 | 0.3% | 66.4% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 535,685 | 94.1% |
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
| RESUME_CHECK | 99,027,216 | 77.7% |
| POP_TOP | 13,895,791 | 10.9% |
| COPY_FREE_VARS | 13,003,799 | 10.2% |
| MAKE_CELL | 1,509,065 | 1.2% |
| RESUME | 18,055 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 14,189,303 | 58.8% |
| LOAD_DEREF | 6,404,542 | 26.5% |
| BUILD_TUPLE | 1,833,904 | 7.6% |
| LOAD_FAST | 1,313,032 | 5.4% |
| RETURN_VALUE | 152,428 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 7,008,679 | 29.0% |
| LOAD_FAST | 6,904,391 | 28.6% |
| RETURN_VALUE | 6,066,687 | 25.1% |
| CALL | 917,698 | 3.8% |
| GET_ITER | 916,992 | 3.8% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 667,488 | 73.6% |
| BUILD_TUPLE | 157,204 | 17.3% |
| LOAD_GLOBAL_MODULE | 79,292 | 8.7% |
| LOAD_FAST | 1,600 | 0.2% |
| LOAD_GLOBAL | 740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 906,164 | 100.0% |
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
| RETURN_CONST | 22,544 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,544 | 100.0% |


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
| LOAD_FAST | 21,637,962 | 36.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,456,843 | 24.1% |
| CALL | 10,953,391 | 18.2% |
| RETURN_VALUE | 4,116,838 | 6.9% |
| CALL_BUILTIN_O | 2,591,112 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 20,010,270 | 33.3% |
| CALL_PY_EXACT_ARGS | 13,015,915 | 21.7% |
| FOR_ITER_TUPLE | 9,975,615 | 16.6% |
| LOAD_FAST_AND_CLEAR | 9,198,218 | 15.3% |
| FOR_ITER_LIST | 4,575,487 | 7.6% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 346,968 | 64.2% |
| BINARY_SUBSCR | 185,800 | 34.4% |
| RETURN_VALUE | 7,520 | 1.4% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540,368 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 72,900,781 | 57.3% |
| RETURN_CONST | 32,283,763 | 25.4% |
| YIELD_VALUE | 22,065,800 | 17.3% |
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
| LOAD_CONST | 14,300,030 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 10,424,207 | 72.9% |
| LOAD_GLOBAL_BUILTIN | 2,651,136 | 18.5% |
| STORE_FAST | 669,680 | 4.7% |
| LOAD_FAST | 459,237 | 3.2% |
| STORE_NAME | 33,580 | 0.2% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,364,033 | 63.8% |
| POP_JUMP_IF_TRUE | 4,183,926 | 12.5% |
| STORE_FAST | 3,935,036 | 11.8% |
| POP_JUMP_IF_FALSE | 1,913,693 | 5.7% |
| POP_TOP | 1,392,092 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,287,786 | 36.7% |
| LOAD_DEREF | 10,424,025 | 31.1% |
| LOAD_GLOBAL_MODULE | 6,493,168 | 19.4% |
| LOAD_CONST | 2,608,132 | 7.8% |
| LOAD_FAST_LOAD_FAST | 912,733 | 2.7% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 414,615 | 45.7% |
| POP_TOP | 358,289 | 39.5% |
| STORE_FAST | 130,960 | 14.4% |
| COPY | 1,920 | 0.2% |
| STORE_SUBSCR_DICT | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 414,615 | 45.7% |
| EXTENDED_ARG | 201,220 | 22.2% |
| JUMP_BACKWARD | 159,469 | 17.6% |
| LOAD_FAST | 83,020 | 9.2% |
| RETURN_CONST | 45,040 | 5.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 14,937,671 | 24.3% |
| CACHE | 13,895,791 | 22.6% |
| RETURN_CONST | 9,425,598 | 15.3% |
| STORE_FAST | 5,839,515 | 9.5% |
| SWAP | 5,778,574 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 23,964,448 | 38.9% |
| RESUME_CHECK | 14,339,181 | 23.3% |
| LOAD_FAST | 7,248,333 | 11.8% |
| RETURN_VALUE | 5,302,374 | 8.6% |
| LOAD_CONST | 2,640,846 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 374,549 | 41.3% |
| BINARY_SUBSCR_DICT | 233,759 | 25.8% |
| RAISE_VARARGS | 115,252 | 12.7% |
| LOAD_ATTR | 95,500 | 10.5% |
| CALL_BUILTIN_CLASS | 38,464 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 788,112 | 87.0% |
| LOAD_GLOBAL_MODULE | 114,772 | 12.7% |
| LOAD_GLOBAL | 1,840 | 0.2% |
| LOAD_FAST | 1,600 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,418,035 | 46.8% |
| LOAD_ATTR | 14,956,655 | 24.6% |
| LOAD_DEREF | 11,928,917 | 19.6% |
| CALL_BUILTIN_FAST | 2,129,900 | 3.5% |
| LOAD_SUPER_ATTR_ATTR | 1,181,964 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,538,881 | 76.7% |
| LOAD_FAST_LOAD_FAST | 12,229,103 | 20.1% |
| LOAD_CONST | 1,723,720 | 2.8% |
| LOAD_DEREF | 128,568 | 0.2% |
| CALL | 35,600 | 0.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 9,900,884 | 69.0% |
| CALL_PY_EXACT_ARGS | 4,261,117 | 29.7% |
| CALL_PY_WITH_DEFAULTS | 163,640 | 1.1% |
| CALL_KW | 8,000 | 0.1% |
| CACHE | 7,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 10,205,427 | 71.1% |
| STORE_FAST | 2,660,326 | 18.5% |
| LOAD_FAST | 791,938 | 5.5% |
| GET_YIELD_FROM_ITER | 346,968 | 2.4% |
| CALL_BUILTIN_CLASS | 160,600 | 1.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,596,955 | 30.2% |
| LOAD_ATTR_SLOT | 33,432,481 | 18.8% |
| BUILD_TUPLE | 21,221,920 | 12.0% |
| RETURN_VALUE | 15,184,147 | 8.6% |
| CALL_BUILTIN_O | 11,432,775 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 72,900,781 | 41.1% |
| STORE_FAST | 38,559,551 | 21.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 19,466,566 | 11.0% |
| RETURN_VALUE | 15,184,147 | 8.6% |
| LOAD_FAST | 5,453,745 | 3.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,303,526 | 96.3% |
| BINARY_SUBSCR | 93,200 | 2.7% |
| LOAD_FAST_LOAD_FAST | 18,960 | 0.6% |
| SWAP | 5,960 | 0.2% |
| STORE_SUBSCR | 3,640 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,290,446 | 96.0% |
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
| LOAD_FAST | 2,208,072 | 17.1% |
| LOAD_GLOBAL_MODULE | 119,027 | 0.9% |
| LOAD_ATTR | 117,978 | 0.9% |
| RETURN_VALUE | 27,307 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,253,294 | 94.8% |
| POP_JUMP_IF_TRUE | 509,834 | 3.9% |
| UNARY_NOT | 84,198 | 0.7% |
| TO_BOOL_BOOL | 41,184 | 0.3% |
| TO_BOOL | 21,463 | 0.2% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 188,506 | 30.7% |
| LOAD_ATTR_SLOT | 117,468 | 19.2% |
| LOAD_ATTR | 107,040 | 17.5% |
| RETURN_VALUE | 106,160 | 17.3% |
| LOAD_FAST_LOAD_FAST | 50,691 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 131,982 | 21.5% |
| CALL_LIST_APPEND | 119,120 | 19.4% |
| LOAD_GLOBAL_MODULE | 106,842 | 17.4% |
| IS_OP | 106,160 | 17.3% |
| STORE_FAST | 58,040 | 9.5% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 3,442,663 | 64.9% |
| TO_BOOL_BOOL | 1,118,718 | 21.1% |
| TO_BOOL_LIST | 661,863 | 12.5% |
| TO_BOOL | 84,198 | 1.6% |
| TO_BOOL_INT | 165 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,529,450 | 66.5% |
| STORE_FAST | 882,740 | 16.6% |
| BUILD_MAP | 734,720 | 13.8% |
| COPY | 86,963 | 1.6% |
| LOAD_CONST | 68,074 | 1.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,766,829 | 33.3% |
| COMPARE_OP_INT | 6,308,780 | 17.9% |
| COMPARE_OP | 6,162,400 | 17.4% |
| CALL_TUPLE_1 | 4,707,229 | 13.3% |
| LOAD_FAST | 2,678,515 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,216,989 | 68.6% |
| RETURN_VALUE | 5,771,180 | 16.3% |
| BUILD_TUPLE | 1,556,880 | 4.4% |
| CALL_BUILTIN_O | 1,095,120 | 3.1% |
| LOAD_FAST | 857,866 | 2.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 129,347 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 126,567 | 97.9% |
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
| SWAP | 4,464,089 | 20.6% |
| POP_JUMP_IF_TRUE | 4,083,244 | 18.9% |
| STORE_FAST | 3,817,113 | 17.7% |
| LOAD_FAST | 2,311,962 | 10.7% |
| BINARY_SUBSCR_TUPLE_INT | 1,557,600 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,718,334 | 54.2% |
| SWAP | 4,464,089 | 20.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,294,383 | 10.6% |
| LOAD_FAST | 1,414,348 | 6.5% |
| BUILD_LIST | 748,349 | 3.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,167,587 | 36.0% |
| BUILD_TUPLE | 10,998,560 | 32.5% |
| SWAP | 4,716,129 | 14.0% |
| LOAD_CONST | 1,656,800 | 4.9% |
| RESUME_CHECK | 1,285,960 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,183,088 | 68.6% |
| SWAP | 4,716,129 | 14.0% |
| STORE_FAST | 3,331,874 | 9.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,561,360 | 4.6% |
| CALL_FUNCTION_EX | 734,880 | 2.2% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,295 | 64.1% |
| SWAP | 18,000 | 35.7% |
| BINARY_OP | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 32,295 | 64.1% |
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
| LOAD_FAST_LOAD_FAST | 25,639,709 | 45.0% |
| LOAD_FAST | 17,185,399 | 30.2% |
| LOAD_ATTR_SLOT | 5,042,150 | 8.8% |
| LOAD_ATTR | 3,034,696 | 5.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,484,120 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 21,221,920 | 37.2% |
| BUILD_MAP | 10,998,560 | 19.3% |
| LOAD_CONST | 10,447,145 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 4,707,029 | 8.3% |
| CALL_LIST_APPEND | 3,231,440 | 5.7% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,643,264 | 35.9% |
| LOAD_FAST | 7,320,441 | 27.3% |
| LOAD_ATTR | 3,067,147 | 11.4% |
| BINARY_OP_MULTIPLY_INT | 2,291,864 | 8.5% |
| LOAD_GLOBAL_BUILTIN | 1,572,922 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,953,391 | 40.8% |
| STORE_FAST | 5,844,741 | 21.8% |
| RETURN_VALUE | 4,521,377 | 16.8% |
| POP_TOP | 1,140,578 | 4.2% |
| RESUME_CHECK | 1,064,956 | 4.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 23,272,271 | 83.1% |
| LOAD_FAST | 2,317,502 | 8.3% |
| CALL_INTRINSIC_1 | 1,256,738 | 4.5% |
| BUILD_MAP | 734,880 | 2.6% |
| BINARY_OP | 201,680 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,600,745 | 45.0% |
| RESUME_CHECK | 11,673,454 | 41.7% |
| LOAD_FAST_LOAD_FAST | 1,561,000 | 5.6% |
| BUILD_TUPLE | 638,860 | 2.3% |
| SWAP | 480,160 | 1.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 1,347,828 | 99.9% |
| IMPORT_NAME | 1,060 | 0.1% |
| LIST_APPEND | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,256,738 | 93.2% |
| BUILD_MAP | 91,250 | 6.8% |
| POP_TOP | 1,060 | 0.1% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,673,104 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,493,126 | 88.9% |
| POP_TOP | 698,038 | 6.5% |
| COPY_FREE_VARS | 261,140 | 2.4% |
| RETURN_VALUE | 84,819 | 0.8% |
| STORE_FAST | 35,740 | 0.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 21,088,596 | 54.7% |
| LOAD_FAST | 8,300,238 | 21.5% |
| CALL_TYPE_1 | 5,882,518 | 15.2% |
| LOAD_GLOBAL_MODULE | 1,180,319 | 3.1% |
| LOAD_CONST | 950,811 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,138,555 | 52.2% |
| BINARY_OP | 6,162,400 | 16.0% |
| LOAD_FAST_LOAD_FAST | 6,162,320 | 16.0% |
| UNARY_NOT | 3,442,663 | 8.9% |
| POP_JUMP_IF_TRUE | 2,278,925 | 5.9% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 24,744,978 | 47.4% |
| LOAD_ATTR | 20,047,462 | 38.4% |
| LOAD_GLOBAL_MODULE | 5,290,314 | 10.1% |
| LOAD_DEREF | 1,536,480 | 2.9% |
| LOAD_CONST | 174,998 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 45,435,329 | 87.1% |
| POP_JUMP_IF_TRUE | 6,743,306 | 12.9% |
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
| LOAD_FAST | 1,237,531 | 25.2% |
| COPY | 1,214,400 | 24.7% |
| LOAD_FAST_LOAD_FAST | 872,880 | 17.8% |
| CALL_ISINSTANCE | 525,020 | 10.7% |
| LOAD_CONST | 236,784 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,340,122 | 27.3% |
| COPY | 1,214,400 | 24.7% |
| BINARY_SUBSCR_LIST_INT | 1,208,120 | 24.6% |
| LOAD_ATTR_INSTANCE_VALUE | 956,400 | 19.5% |
| STORE_FAST_STORE_FAST | 55,584 | 1.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 13,003,799 | 40.9% |
| CALL_PY_EXACT_ARGS | 11,883,858 | 37.4% |
| LOAD_ATTR_PROPERTY | 5,061,686 | 15.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,202,646 | 3.8% |
| CALL_KW | 261,140 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,815,796 | 68.6% |
| RETURN_GENERATOR | 9,900,884 | 31.1% |
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
| LOAD_FAST | 23,143,373 | 99.4% |
| LOAD_DEREF | 128,898 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 23,272,271 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,678,869 | 26.5% |
| TO_BOOL_BOOL | 5,486,066 | 25.6% |
| CALL_LIST_APPEND | 4,571,155 | 21.3% |
| GET_ITER | 2,378,115 | 11.1% |
| COMPARE_OP_INT | 1,719,897 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,038,535 | 32.9% |
| JUMP_BACKWARD | 5,792,569 | 27.0% |
| FOR_ITER_LIST | 5,660,702 | 26.4% |
| FOR_ITER_TUPLE | 1,740,040 | 8.1% |
| FOR_ITER_RANGE | 642,400 | 3.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 68,431,050 | 65.9% |
| GET_ITER | 20,010,270 | 19.3% |
| SWAP | 7,638,561 | 7.4% |
| LOAD_FAST | 7,631,085 | 7.4% |
| FOR_ITER | 78,998 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 71,074,712 | 68.5% |
| STORE_FAST | 8,356,971 | 8.0% |
| SWAP | 7,602,789 | 7.3% |
| LOAD_FAST | 4,699,347 | 4.5% |
| RETURN_CONST | 4,698,608 | 4.5% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 7,758,077 | 86.6% |
| STORE_FAST | 982,435 | 11.0% |
| STORE_DEREF | 185,697 | 2.1% |
| STORE_NAME | 26,000 | 0.3% |
| EXTENDED_ARG | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,821,741 | 76.2% |
| STORE_DEREF | 2,092,408 | 23.4% |
| STORE_NAME | 38,060 | 0.4% |
| EXTENDED_ARG | 2,540 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,759,577 | 100.0% |
| EXTENDED_ARG | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 7,758,077 | 100.0% |
| CALL_INTRINSIC_1 | 1,060 | 0.0% |
| STORE_NAME | 440 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 17,248,423 | 36.2% |
| LOAD_FAST | 12,663,795 | 26.6% |
| LOAD_CONST | 10,976,211 | 23.0% |
| LOAD_FAST_LOAD_FAST | 5,893,500 | 12.4% |
| LOAD_GLOBAL_BUILTIN | 539,781 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 30,048,840 | 63.1% |
| YIELD_VALUE | 12,648,455 | 26.5% |
| POP_JUMP_IF_TRUE | 4,906,850 | 10.3% |
| EXTENDED_ARG | 27,180 | 0.1% |
| STORE_FAST | 8,960 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 34,393,990 | 22.0% |
| POP_TOP | 23,964,448 | 15.3% |
| POP_JUMP_IF_TRUE | 22,709,169 | 14.5% |
| POP_JUMP_IF_NONE | 20,909,998 | 13.4% |
| CALL_LIST_APPEND | 17,343,472 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 68,431,050 | 43.7% |
| FOR_ITER_LIST | 46,550,715 | 29.7% |
| FOR_ITER_TUPLE | 22,277,135 | 14.2% |
| FOR_ITER_RANGE | 10,609,857 | 6.8% |
| EXTENDED_ARG | 5,678,869 | 3.6% |


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
| STORE_FAST | 4,278,679 | 72.5% |
| POP_TOP | 734,238 | 12.4% |
| STORE_FAST_STORE_FAST | 240,720 | 4.1% |
| CALL_LIST_APPEND | 191,877 | 3.3% |
| LOAD_FAST | 146,967 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,005,928 | 67.9% |
| BUILD_MAP | 642,560 | 10.9% |
| LOAD_GLOBAL_BUILTIN | 470,038 | 8.0% |
| LOAD_FAST_LOAD_FAST | 437,246 | 7.4% |
| STORE_FAST | 119,067 | 2.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,004,123 | 48.5% |
| BUILD_TUPLE | 1,568,815 | 25.4% |
| RETURN_VALUE | 511,449 | 8.3% |
| BINARY_SUBSCR | 489,428 | 7.9% |
| BINARY_SUBSCR_LIST_INT | 396,080 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,183,238 | 99.9% |
| LOAD_NAME | 4,800 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,346,948 | 99.8% |
| LOAD_CONST | 1,260 | 0.1% |
| LOAD_DEREF | 640 | 0.0% |
| LOAD_ATTR_SLOT | 200 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,347,828 | 99.9% |
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
| LOAD_GLOBAL_MODULE | 57,025,710 | 46.8% |
| LOAD_FAST | 55,273,693 | 45.4% |
| CALL_TYPE_1 | 4,209,238 | 3.5% |
| LOAD_ATTR_SLOT | 2,297,043 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 1,905,091 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 36,817,948 | 30.2% |
| CONTAINS_OP | 20,047,462 | 16.5% |
| IS_OP | 17,248,423 | 14.2% |
| LOAD_FAST | 16,056,936 | 13.2% |
| PUSH_NULL | 14,956,655 | 12.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 69,887,286 | 36.5% |
| LOAD_CONST | 40,444,592 | 21.1% |
| RESUME_CHECK | 15,734,559 | 8.2% |
| BUILD_TUPLE | 10,447,145 | 5.5% |
| RETURN_CONST | 9,526,680 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,444,592 | 21.1% |
| CALL_BUILTIN_FAST | 24,272,023 | 12.7% |
| COMPARE_OP_INT | 20,987,704 | 11.0% |
| STORE_FAST | 14,708,881 | 7.7% |
| MAKE_FUNCTION | 14,300,030 | 7.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 21,987,532 | 32.0% |
| NOP | 10,424,025 | 15.2% |
| LOAD_FAST | 7,794,151 | 11.4% |
| LOAD_ATTR_SLOT | 6,404,542 | 9.3% |
| POP_JUMP_IF_FALSE | 4,653,460 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 22,156,436 | 32.3% |
| PUSH_NULL | 11,928,917 | 17.4% |
| LOAD_FAST | 9,406,200 | 13.7% |
| CALL_ISINSTANCE | 7,549,248 | 11.0% |
| BINARY_SUBSCR | 6,404,542 | 9.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 196,232,244 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 162,951,522 | 16.7% |
| RESUME_CHECK | 115,568,674 | 11.8% |
| POP_JUMP_IF_FALSE | 113,723,714 | 11.6% |
| PUSH_NULL | 46,538,881 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 95,194,916 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 79,145,780 | 8.1% |
| LOAD_GLOBAL_MODULE | 78,854,084 | 8.1% |
| LOAD_CONST | 69,887,286 | 7.2% |
| LOAD_ATTR | 55,273,693 | 5.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,198,218 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,589,884 | 45.2% |
| MAKE_CELL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,198,138 | 54.8% |
| LOAD_FAST_AND_CLEAR | 7,589,884 | 45.2% |
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
| STORE_FAST | 62,569,124 | 24.6% |
| POP_JUMP_IF_FALSE | 34,112,302 | 13.4% |
| LOAD_GLOBAL_BUILTIN | 28,997,668 | 11.4% |
| RESUME_CHECK | 19,966,071 | 7.9% |
| STORE_FAST_STORE_FAST | 15,653,126 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 27,001,865 | 10.6% |
| BUILD_TUPLE | 25,639,709 | 10.1% |
| CONTAINS_OP | 24,744,978 | 9.7% |
| COMPARE_OP | 21,088,596 | 8.3% |
| STORE_SUBSCR_LIST_INT | 18,849,697 | 7.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,249 | 19.4% |
| LOAD_FAST | 34,201 | 18.8% |
| STORE_FAST | 26,929 | 14.8% |
| RESUME_CHECK | 10,928 | 6.0% |
| RESUME | 10,779 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 50,519 | 27.8% |
| LOAD_GLOBAL_BUILTIN | 41,252 | 22.7% |
| LOAD_FAST | 39,589 | 21.8% |
| LOAD_ATTR | 14,076 | 7.7% |
| CALL | 9,827 | 5.4% |


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
| MAKE_CELL | 2,274,597 | 37.6% |
| CACHE | 1,509,065 | 24.9% |
| CALL_PY_EXACT_ARGS | 772,736 | 12.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 654,324 | 10.8% |
| CALL | 523,672 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,770,876 | 62.3% |
| MAKE_CELL | 2,274,597 | 37.6% |
| RESUME | 3,000 | 0.0% |
| RETURN_GENERATOR | 400 | 0.0% |
| LOAD_FAST_AND_CLEAR | 80 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 7,852,911 | 99.8% |
| LOAD_FAST | 4,160 | 0.1% |
| RETURN_VALUE | 3,620 | 0.0% |
| CALL | 1,920 | 0.0% |
| STORE_FAST | 1,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,865,731 | 100.0% |
| LOAD_CONST | 320 | 0.0% |
| LOAD_NAME | 20 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 111,645,385 | 38.3% |
| CONTAINS_OP | 45,435,329 | 15.6% |
| COMPARE_OP_INT | 35,529,819 | 12.2% |
| IS_OP | 30,048,840 | 10.3% |
| COMPARE_OP | 20,138,555 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,723,714 | 39.0% |
| LOAD_GLOBAL_BUILTIN | 58,001,770 | 19.9% |
| JUMP_BACKWARD | 34,393,990 | 11.8% |
| LOAD_FAST_LOAD_FAST | 34,112,302 | 11.7% |
| RETURN_CONST | 29,346,650 | 10.1% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,136,134 | 80.3% |
| BINARY_SUBSCR | 7,008,679 | 17.0% |
| LOAD_DEREF | 1,088,838 | 2.6% |
| LOAD_ATTR_INSTANCE_VALUE | 8,380 | 0.0% |
| EXTENDED_ARG | 6,797 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20,909,998 | 50.7% |
| LOAD_FAST_LOAD_FAST | 14,868,652 | 36.0% |
| LOAD_FAST | 2,616,066 | 6.3% |
| LOAD_GLOBAL_BUILTIN | 1,438,148 | 3.5% |
| LOAD_CONST | 1,111,408 | 2.7% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,718,815 | 92.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,224,956 | 6.7% |
| EXTENDED_ARG | 179,780 | 1.0% |
| CALL_BUILTIN_FAST | 11,040 | 0.1% |
| LOAD_DEREF | 8,920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,237,188 | 67.4% |
| LOAD_FAST_LOAD_FAST | 2,031,876 | 11.2% |
| LOAD_GLOBAL_MODULE | 1,880,324 | 10.4% |
| LOAD_GLOBAL_BUILTIN | 1,385,745 | 7.6% |
| JUMP_BACKWARD | 503,740 | 2.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 54,464,852 | 67.6% |
| TO_BOOL_INT | 9,137,796 | 11.3% |
| CONTAINS_OP | 6,743,306 | 8.4% |
| IS_OP | 4,906,850 | 6.1% |
| COMPARE_OP | 2,278,925 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,017,550 | 47.2% |
| JUMP_BACKWARD | 22,709,169 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 5,308,775 | 6.6% |
| NOP | 4,183,926 | 5.2% |
| BUILD_LIST | 4,083,244 | 5.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 118,912 | 99.9% |
| CALL_KW | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 115,252 | 98.4% |
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
| POP_JUMP_IF_FALSE | 29,346,650 | 51.2% |
| RESUME_CHECK | 10,045,258 | 17.5% |
| FOR_ITER_LIST | 5,671,791 | 9.9% |
| FOR_ITER | 4,698,608 | 8.2% |
| STORE_SUBSCR | 3,290,446 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 32,283,763 | 56.4% |
| LOAD_CONST | 9,526,680 | 16.6% |
| POP_TOP | 9,425,598 | 16.5% |
| TO_BOOL_BOOL | 3,462,735 | 6.0% |
| STORE_FAST | 1,541,170 | 2.7% |


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
| MAKE_FUNCTION | 10,424,207 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 1,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,828,156 | 94.3% |
| STORE_FAST | 306,995 | 2.9% |
| STORE_DEREF | 113,216 | 1.1% |
| LOAD_CONST | 52,360 | 0.5% |
| LOAD_GLOBAL_MODULE | 42,928 | 0.4% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 486,838 | 82.3% |
| LOAD_FAST | 98,460 | 16.6% |
| STORE_ATTR | 3,906 | 0.7% |
| SWAP | 2,159 | 0.4% |
| LOAD_DEREF | 12 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 289,666 | 49.0% |
| LOAD_FAST_LOAD_FAST | 116,252 | 19.7% |
| LOAD_FAST | 89,985 | 15.2% |
| LOAD_GLOBAL_BUILTIN | 74,060 | 12.5% |
| STORE_ATTR_INSTANCE_VALUE | 3,960 | 0.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 4,491,620 | 51.7% |
| IMPORT_FROM | 2,092,408 | 24.1% |
| LOAD_ATTR | 1,558,823 | 17.9% |
| STORE_FAST | 240,860 | 2.8% |
| SET_FUNCTION_ATTRIBUTE | 113,216 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,491,580 | 51.7% |
| POP_TOP | 1,906,711 | 21.9% |
| LOAD_DEREF | 1,298,320 | 14.9% |
| LOAD_GLOBAL_MODULE | 481,480 | 5.5% |
| IMPORT_FROM | 185,697 | 2.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 43,131,622 | 12.0% |
| RETURN_VALUE | 38,559,551 | 10.7% |
| LOAD_ATTR | 36,817,948 | 10.3% |
| BINARY_OP | 24,216,989 | 6.7% |
| FOR_ITER_TUPLE | 23,957,126 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 196,232,244 | 54.7% |
| LOAD_FAST_LOAD_FAST | 62,569,124 | 17.4% |
| LOAD_GLOBAL_BUILTIN | 37,717,646 | 10.5% |
| LOAD_GLOBAL_MODULE | 18,255,105 | 5.1% |
| STORE_FAST | 9,344,867 | 2.6% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,156,234 | 77.8% |
| FOR_ITER_TUPLE | 596,404 | 11.2% |
| FOR_ITER_RANGE | 500,000 | 9.4% |
| FOR_ITER | 92,960 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,303,736 | 80.5% |
| LOAD_ATTR_PROPERTY | 319,218 | 6.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 237,790 | 4.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 157,680 | 2.9% |
| LOAD_DEREF | 107,360 | 2.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 98,983,211 | 93.6% |
| RETURN_VALUE | 3,248,190 | 3.1% |
| UNPACK_SEQUENCE_TUPLE | 1,436,452 | 1.4% |
| STORE_FAST_STORE_FAST | 771,723 | 0.7% |
| BUILD_LIST | 413,120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,970,109 | 39.7% |
| LOAD_GLOBAL_BUILTIN | 22,030,526 | 20.8% |
| LOAD_DEREF | 21,987,532 | 20.8% |
| LOAD_FAST_LOAD_FAST | 15,653,126 | 14.8% |
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
| BINARY_SUBSCR_LIST_INT | 9,396,380 | 20.7% |
| LOAD_FAST_AND_CLEAR | 9,198,138 | 20.3% |
| FOR_ITER | 7,602,789 | 16.8% |
| BUILD_MAP | 4,716,129 | 10.4% |
| LOAD_FAST | 4,641,394 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,396,600 | 20.7% |
| STORE_FAST | 7,930,923 | 17.5% |
| FOR_ITER | 7,638,561 | 16.9% |
| POP_TOP | 5,778,574 | 12.8% |
| BUILD_MAP | 4,716,129 | 10.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,452 | 26.3% |
| FOR_ITER | 6,803 | 17.1% |
| CALL_BUILTIN_CLASS | 6,340 | 16.0% |
| LOAD_FAST | 3,957 | 10.0% |
| CALL_BUILTIN_FAST | 3,260 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 18,673 | 47.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,429 | 23.7% |
| STORE_FAST | 8,074 | 20.3% |
| UNPACK_SEQUENCE_TUPLE | 1,139 | 2.9% |
| UNPACK_SEQUENCE | 914 | 2.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 12,648,455 | 55.2% |
| CALL_ISINSTANCE | 6,945,766 | 30.3% |
| LOAD_FAST | 1,146,726 | 5.0% |
| YIELD_VALUE | 677,448 | 3.0% |
| RETURN_VALUE | 423,377 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 22,065,800 | 96.3% |
| YIELD_VALUE | 677,448 | 3.0% |
| STORE_FAST | 162,902 | 0.7% |
| UNPACK_SEQUENCE | 3,120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,520 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 18,055 | 38.0% |
| CALL | 11,105 | 23.3% |
| CALL_PY_EXACT_ARGS | 6,107 | 12.8% |
| POP_TOP | 3,960 | 8.3% |
| MAKE_CELL | 3,000 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,694 | 37.2% |
| LOAD_GLOBAL | 10,779 | 22.7% |
| LOAD_CONST | 8,762 | 18.4% |
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
| LOAD_CONST | 11,827,069 | 91.1% |
| LOAD_FAST_LOAD_FAST | 574,033 | 4.4% |
| BINARY_SUBSCR_DICT | 422,960 | 3.3% |
| CALL_BUILTIN_CLASS | 81,187 | 0.6% |
| LOAD_FAST | 43,682 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 9,394,344 | 72.4% |
| STORE_FAST | 1,576,581 | 12.1% |
| SWAP | 1,085,059 | 8.4% |
| LOAD_CONST | 269,080 | 2.1% |
| LOAD_FAST | 201,557 | 1.6% |


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
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,668,674 | 60.2% |
| LOAD_ATTR_SLOT | 723,511 | 26.1% |
| LOAD_FAST_LOAD_FAST | 283,499 | 10.2% |
| LOAD_FAST | 94,285 | 3.4% |
| BINARY_OP | 1,445 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,291,864 | 82.7% |
| LOAD_FAST_LOAD_FAST | 181,166 | 6.5% |
| STORE_FAST | 175,592 | 6.3% |
| LOAD_FAST | 90,186 | 3.3% |
| LOAD_GLOBAL_MODULE | 25,174 | 0.9% |


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
| LOAD_CONST | 1,569,121 | 63.1% |
| LOAD_FAST_LOAD_FAST | 607,151 | 24.4% |
| BINARY_SUBSCR_LIST_INT | 181,120 | 7.3% |
| LOAD_FAST | 123,232 | 5.0% |
| BINARY_OP | 2,184 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,082,420 | 43.5% |
| STORE_FAST | 710,438 | 28.6% |
| BINARY_OP | 311,685 | 12.5% |
| COMPARE_OP_INT | 184,120 | 7.4% |
| BINARY_SUBSCR_LIST_INT | 54,440 | 2.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,215,226 | 36.3% |
| LOAD_FAST_LOAD_FAST | 925,732 | 27.6% |
| LOAD_CONST | 642,800 | 19.2% |
| CALL_TUPLE_1 | 443,840 | 13.3% |
| RETURN_VALUE | 114,570 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 884,514 | 26.4% |
| RETURN_VALUE | 809,274 | 24.2% |
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
| LOAD_CONST | 14,538 | 9.1% |
| BUILD_SLICE | 3,840 | 2.4% |
| BINARY_SUBSCR | 700 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 159,238 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 27,001,865 | 89.4% |
| COPY | 1,208,120 | 4.0% |
| LOAD_CONST | 1,026,678 | 3.4% |
| LOAD_FAST | 570,305 | 1.9% |
| CALL_BUILTIN_CLASS | 282,487 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,459,080 | 31.3% |
| SWAP | 9,396,380 | 31.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 7,546,045 | 25.0% |
| LOAD_CONST | 1,208,580 | 4.0% |
| STORE_FAST | 517,407 | 1.7% |


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
| LOAD_CONST | 8,729,566 | 97.0% |
| LOAD_FAST | 263,330 | 2.9% |
| BINARY_SUBSCR | 2,736 | 0.0% |
| LOAD_FAST_LOAD_FAST | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,738,641 | 52.7% |
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
| LOAD_FAST | 13,334,127 | 56.7% |
| BINARY_OP_ADD_INT | 9,394,344 | 39.9% |
| LOAD_FAST_LOAD_FAST | 480,445 | 2.0% |
| LOAD_ATTR | 152,040 | 0.6% |
| LOAD_DEREF | 83,580 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,656,794 | 92.1% |
| COPY_FREE_VARS | 1,202,646 | 5.1% |
| MAKE_CELL | 654,324 | 2.8% |
| POP_TOP | 7,360 | 0.0% |
| CALL_PY_EXACT_ARGS | 719 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,821,942 | 30.8% |
| CALL_BUILTIN_CLASS | 1,959,347 | 21.4% |
| LOAD_GLOBAL_BUILTIN | 921,608 | 10.1% |
| LOAD_CONST | 710,920 | 7.8% |
| CALL_LEN | 611,072 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,419,833 | 37.4% |
| CALL_BUILTIN_CLASS | 1,959,347 | 21.4% |
| GET_ITER | 1,868,795 | 20.4% |
| CALL | 284,415 | 3.1% |
| BINARY_SUBSCR_LIST_INT | 282,487 | 3.1% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,272,023 | 55.8% |
| LOAD_FAST_LOAD_FAST | 17,273,586 | 39.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,337,148 | 3.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 478,200 | 1.1% |
| LOAD_FAST | 64,258 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 18,103,485 | 41.8% |
| STORE_FAST | 11,046,640 | 25.5% |
| TO_BOOL | 10,287,220 | 23.8% |
| PUSH_NULL | 2,129,900 | 4.9% |
| RETURN_VALUE | 1,499,953 | 3.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,880,749 | 94.4% |
| LOAD_FAST | 135,109 | 2.6% |
| BINARY_OP | 119,127 | 2.3% |
| RETURN_GENERATOR | 27,800 | 0.5% |
| LOAD_CONST | 5,580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_TUPLE_1 | 4,707,029 | 91.0% |
| GET_ITER | 173,780 | 3.4% |
| STORE_FAST | 128,009 | 2.5% |
| CALL_BUILTIN_CLASS | 119,127 | 2.3% |
| RETURN_VALUE | 34,520 | 0.7% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,812,500 | 44.7% |
| RETURN_GENERATOR | 10,205,427 | 25.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 5,618,402 | 14.1% |
| LOAD_ATTR_SLOT | 4,874,175 | 12.2% |
| BINARY_OP | 1,095,120 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,691,268 | 39.3% |
| RETURN_VALUE | 11,432,775 | 28.7% |
| TO_BOOL_BOOL | 9,907,520 | 24.8% |
| GET_ITER | 2,591,112 | 6.5% |
| LOAD_FAST | 50,620 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 35,898,734 | 53.2% |
| LOAD_GLOBAL_BUILTIN | 19,055,433 | 28.2% |
| LOAD_DEREF | 7,549,248 | 11.2% |
| LOAD_FAST_LOAD_FAST | 2,883,629 | 4.3% |
| LOAD_FAST | 1,621,080 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 59,843,510 | 88.7% |
| YIELD_VALUE | 6,945,766 | 10.3% |
| COPY | 525,020 | 0.8% |
| RETURN_VALUE | 127,526 | 0.2% |
| TO_BOOL | 9,662 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,057,199 | 96.3% |
| LOAD_GLOBAL_MODULE | 553,240 | 2.0% |
| BINARY_SUBSCR | 185,800 | 0.7% |
| RETURN_VALUE | 95,082 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 93,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 10,271,189 | 36.6% |
| LOAD_GLOBAL_BUILTIN | 9,676,894 | 34.4% |
| LOAD_CONST | 7,191,034 | 25.6% |
| CALL_BUILTIN_CLASS | 611,072 | 2.2% |
| STORE_FAST | 84,420 | 0.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,419,852 | 68.4% |
| BUILD_TUPLE | 3,231,440 | 13.5% |
| BINARY_SUBSCR_TUPLE_INT | 1,762,920 | 7.3% |
| LOAD_FAST_CHECK | 1,556,980 | 6.5% |
| CALL | 693,121 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,343,472 | 72.2% |
| EXTENDED_ARG | 4,571,155 | 19.0% |
| LOAD_FAST | 1,681,749 | 7.0% |
| LOAD_FAST_LOAD_FAST | 207,500 | 0.9% |
| JUMP_FORWARD | 191,877 | 0.8% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,009,547 | 68.5% |
| LOAD_CONST | 2,390,499 | 10.9% |
| BUILD_LIST | 2,294,383 | 10.5% |
| BUILD_MAP | 1,561,360 | 7.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 269,267 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,696,535 | 57.9% |
| STORE_FAST | 3,453,573 | 15.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,116,160 | 14.2% |
| POP_TOP | 908,809 | 4.1% |
| GET_ITER | 737,583 | 3.4% |


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
| LOAD_ATTR_METHOD_NO_DICT | 24,532,137 | 83.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,807,588 | 16.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,788 | 0.4% |
| LOAD_ATTR | 72,820 | 0.2% |
| CALL | 3,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 14,456,843 | 48.9% |
| STORE_FAST | 9,688,915 | 32.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,880,749 | 16.5% |
| CALL_BUILTIN_CLASS | 169,819 | 0.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 121,788 | 0.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,853,920 | 61.4% |
| LOAD_CONST | 1,226,456 | 26.4% |
| LOAD_FAST | 353,960 | 7.6% |
| RETURN_VALUE | 97,600 | 2.1% |
| BUILD_LIST | 44,300 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,235,540 | 69.6% |
| LOAD_CONST | 1,224,456 | 26.3% |
| TO_BOOL_NONE | 104,000 | 2.2% |
| BINARY_OP_ADD_UNICODE | 39,600 | 0.9% |
| STORE_FAST | 25,520 | 0.5% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 21,015,699 | 30.8% |
| LOAD_FAST | 15,742,761 | 23.1% |
| LOAD_FAST_LOAD_FAST | 13,783,786 | 20.2% |
| GET_ITER | 13,015,915 | 19.1% |
| LOAD_SUPER_ATTR_METHOD | 1,539,387 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 51,027,110 | 74.9% |
| COPY_FREE_VARS | 11,883,858 | 17.4% |
| RETURN_GENERATOR | 4,261,117 | 6.3% |
| MAKE_CELL | 772,736 | 1.1% |
| CALL_PY_EXACT_ARGS | 144,888 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,105,004 | 45.8% |
| LOAD_FAST | 1,865,763 | 40.6% |
| RETURN_VALUE | 192,647 | 4.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 157,934 | 3.4% |
| LOAD_CONST | 80,527 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,380,015 | 95.3% |
| RETURN_GENERATOR | 163,640 | 3.6% |
| MAKE_CELL | 53,726 | 1.2% |
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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,707,029 | 80.4% |
| LOAD_FAST | 1,017,557 | 17.4% |
| STORE_FAST | 105,736 | 1.8% |
| RETURN_VALUE | 7,920 | 0.1% |
| LOAD_DEREF | 4,116 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 4,707,229 | 80.4% |
| BINARY_SUBSCR_DICT | 443,840 | 7.6% |
| STORE_FAST | 353,176 | 6.0% |
| STORE_SUBSCR_DICT | 181,360 | 3.1% |
| RETURN_VALUE | 56,520 | 1.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,589,644 | 99.3% |
| LOAD_CONST | 119,972 | 0.7% |
| LOAD_GLOBAL_MODULE | 1,840 | 0.0% |
| CALL | 1,081 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,423,614 | 38.4% |
| COMPARE_OP | 5,882,518 | 35.2% |
| LOAD_ATTR | 4,209,238 | 25.2% |
| IS_OP | 64,232 | 0.4% |
| BUILD_TUPLE | 55,800 | 0.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 493,706 | 90.8% |
| CALL_BUILTIN_CLASS | 25,400 | 4.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 21,568 | 4.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,840 | 0.3% |
| UNARY_NEGATIVE | 320 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 542,054 | 99.7% |
| RETURN_VALUE | 1,580 | 0.3% |
| COMPARE_OP | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,987,704 | 41.0% |
| LOAD_FAST_LOAD_FAST | 18,325,513 | 35.8% |
| CALL_LEN | 10,271,189 | 20.1% |
| LOAD_FAST | 1,029,107 | 2.0% |
| LOAD_ATTR_SLOT | 225,305 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,529,819 | 69.4% |
| BINARY_OP | 6,308,780 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 4,738,660 | 9.3% |
| EXTENDED_ARG | 1,719,897 | 3.4% |
| LOAD_FAST_LOAD_FAST | 1,570,040 | 3.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,030,880 | 68.9% |
| LOAD_CONST | 4,335,757 | 29.8% |
| LOAD_GLOBAL_MODULE | 192,547 | 1.3% |
| LOAD_ATTR | 3,160 | 0.0% |
| LOAD_FAST | 2,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,480,876 | 99.4% |
| YIELD_VALUE | 79,688 | 0.5% |
| POP_JUMP_IF_TRUE | 3,520 | 0.0% |
| EXTENDED_ARG | 1,000 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 100,604 | 52.6% |
| GET_ITER | 90,702 | 47.4% |
| FOR_ITER | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 99,684 | 52.1% |
| POP_TOP | 90,542 | 47.3% |
| RESUME | 860 | 0.4% |
| STORE_FAST | 320 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 46,550,715 | 74.0% |
| EXTENDED_ARG | 5,660,702 | 9.0% |
| LOAD_FAST | 4,843,694 | 7.7% |
| GET_ITER | 4,575,487 | 7.3% |
| SWAP | 1,221,420 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,131,622 | 68.6% |
| RETURN_CONST | 5,671,791 | 9.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,719,671 | 7.5% |
| STORE_FAST_LOAD_FAST | 4,156,234 | 6.6% |
| LOAD_FAST | 4,094,029 | 6.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,609,857 | 87.5% |
| GET_ITER | 809,529 | 6.7% |
| EXTENDED_ARG | 642,400 | 5.3% |
| SWAP | 38,880 | 0.3% |
| LOAD_FAST | 29,360 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,760,597 | 88.7% |
| RETURN_CONST | 630,292 | 5.2% |
| STORE_FAST_LOAD_FAST | 500,000 | 4.1% |
| LOAD_FAST | 195,180 | 1.6% |
| SWAP | 38,520 | 0.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 22,277,135 | 64.0% |
| GET_ITER | 9,975,615 | 28.6% |
| EXTENDED_ARG | 1,740,040 | 5.0% |
| LOAD_FAST | 518,716 | 1.5% |
| SWAP | 299,357 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,957,126 | 68.8% |
| LOAD_FAST | 7,494,876 | 21.5% |
| RETURN_CONST | 788,983 | 2.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 717,399 | 2.1% |
| LOAD_GLOBAL_MODULE | 602,498 | 1.7% |


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
| LOAD_FAST | 5,501,284 | 59.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,820 | 11.6% |
| LOAD_DEREF | 1,058,280 | 11.5% |
| COPY | 956,400 | 10.4% |
| LOAD_GLOBAL_MODULE | 571,572 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,560,396 | 17.0% |
| CALL_BUILTIN_FAST | 1,337,148 | 14.6% |
| POP_JUMP_IF_NOT_NONE | 1,224,956 | 13.3% |
| STORE_FAST | 1,075,980 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,820 | 11.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,145,780 | 86.3% |
| RETURN_VALUE | 4,635,721 | 5.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,116,160 | 3.4% |
| LOAD_GLOBAL_MODULE | 1,983,657 | 2.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,560,396 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,845,523 | 34.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,532,137 | 26.8% |
| CALL_PY_EXACT_ARGS | 21,015,699 | 22.9% |
| LOAD_CONST | 4,055,069 | 4.4% |
| LOAD_DEREF | 3,320,094 | 3.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 22,156,436 | 71.7% |
| LOAD_ATTR_SLOT | 4,711,669 | 15.2% |
| LOAD_FAST | 3,707,102 | 12.0% |
| STORE_FAST_LOAD_FAST | 157,680 | 0.5% |
| LOAD_ATTR | 147,515 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,960,729 | 48.4% |
| LOAD_FAST_LOAD_FAST | 10,812,604 | 35.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,807,588 | 15.6% |
| CALL_PY_EXACT_ARGS | 313,889 | 1.0% |
| LOAD_CONST | 6,902 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,261,240 | 99.2% |
| LOAD_FAST | 5,540 | 0.4% |
| LOAD_ATTR_MODULE | 2,640 | 0.2% |
| LOAD_ATTR | 1,401 | 0.1% |
| LOAD_FAST_LOAD_FAST | 1,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,044,374 | 82.1% |
| CALL_PY_EXACT_ARGS | 80,689 | 6.3% |
| CALL | 57,378 | 4.5% |
| LOAD_FAST | 26,100 | 2.1% |
| LOAD_ATTR_SLOT | 15,920 | 1.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,477,727 | 92.5% |
| LOAD_DEREF | 3,109,100 | 5.3% |
| BINARY_SUBSCR_LIST_INT | 342,120 | 0.6% |
| STORE_FAST_LOAD_FAST | 237,790 | 0.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 237,033 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 44,303,086 | 75.3% |
| CALL_BUILTIN_O | 5,618,402 | 9.5% |
| BUILD_TUPLE | 2,484,120 | 4.2% |
| LOAD_FAST | 1,920,959 | 3.3% |
| BINARY_OP_MULTIPLY_INT | 1,668,674 | 2.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,002,951 | 60.9% |
| LOAD_FAST_LOAD_FAST | 478,940 | 29.1% |
| LOAD_DEREF | 144,340 | 8.8% |
| LOAD_ATTR | 12,020 | 0.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,927 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 478,200 | 29.0% |
| TO_BOOL_STR | 478,200 | 29.0% |
| TO_BOOL_BOOL | 408,891 | 24.8% |
| LOAD_CONST | 106,520 | 6.5% |
| CALL_LEN | 73,480 | 4.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,483,976 | 94.6% |
| RETURN_VALUE | 642,674 | 2.3% |
| STORE_FAST_LOAD_FAST | 319,218 | 1.1% |
| LOAD_DEREF | 217,198 | 0.8% |
| LOAD_FAST_LOAD_FAST | 168,600 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,813,794 | 67.2% |
| COPY_FREE_VARS | 5,061,686 | 18.1% |
| GET_ITER | 1,920,188 | 6.9% |
| TO_BOOL_BOOL | 729,294 | 2.6% |
| STORE_FAST | 505,510 | 1.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,194,916 | 99.1% |
| LOAD_ATTR_SLOT | 613,655 | 0.6% |
| LOAD_FAST_LOAD_FAST | 88,062 | 0.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 72,437 | 0.1% |
| STORE_FAST_LOAD_FAST | 21,590 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,432,481 | 34.8% |
| STORE_FAST | 22,510,282 | 23.4% |
| LOAD_DEREF | 6,404,542 | 6.7% |
| LOAD_FAST | 5,219,830 | 5.4% |
| LOAD_CONST | 5,210,255 | 5.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 58,001,770 | 24.8% |
| RESUME_CHECK | 41,289,858 | 17.7% |
| STORE_FAST | 37,717,646 | 16.1% |
| STORE_FAST_STORE_FAST | 22,030,526 | 9.4% |
| LOAD_FAST | 20,512,646 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,951,522 | 69.7% |
| LOAD_FAST_LOAD_FAST | 28,997,668 | 12.4% |
| CALL_ISINSTANCE | 19,055,433 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 9,009,974 | 3.9% |
| LOAD_DEREF | 3,365,205 | 1.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,854,084 | 54.1% |
| STORE_FAST | 18,255,105 | 12.5% |
| RESUME_CHECK | 16,028,175 | 11.0% |
| POP_JUMP_IF_FALSE | 9,686,945 | 6.6% |
| NOP | 6,493,168 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 57,025,710 | 39.1% |
| CALL_ISINSTANCE | 35,898,734 | 24.6% |
| LOAD_FAST | 29,777,229 | 20.4% |
| CONTAINS_OP | 5,290,314 | 3.6% |
| LOAD_FAST_LOAD_FAST | 3,333,699 | 2.3% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,104,564 | 93.5% |
| LOAD_DEREF | 77,300 | 6.5% |
| LOAD_SUPER_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,181,964 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,813,641 | 100.0% |
| LOAD_SUPER_ATTR | 500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,539,387 | 84.9% |
| LOAD_GLOBAL_MODULE | 172,254 | 9.5% |
| LOAD_FAST | 84,580 | 4.7% |
| LOAD_FAST_LOAD_FAST | 17,560 | 1.0% |
| CALL | 360 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 99,027,216 | 38.4% |
| CALL_PY_EXACT_ARGS | 51,027,110 | 19.8% |
| COPY_FREE_VARS | 21,815,796 | 8.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 21,656,794 | 8.4% |
| LOAD_ATTR_PROPERTY | 18,813,794 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 115,568,674 | 44.8% |
| LOAD_GLOBAL_BUILTIN | 41,289,858 | 16.0% |
| NOP | 21,364,033 | 8.3% |
| LOAD_FAST_LOAD_FAST | 19,966,071 | 7.7% |
| LOAD_GLOBAL_MODULE | 16,028,175 | 6.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 661,220 | 64.2% |
| LOAD_CONST | 367,948 | 35.7% |
| SEND | 620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 646,240 | 62.8% |
| POP_TOP | 352,888 | 34.3% |
| YIELD_VALUE | 15,060 | 1.5% |
| END_SEND | 15,020 | 1.5% |
| SEND | 580 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,103,630 | 62.6% |
| SWAP | 956,400 | 28.5% |
| LOAD_FAST_LOAD_FAST | 259,600 | 7.7% |
| LOAD_ATTR_SLOT | 35,139 | 1.0% |
| STORE_ATTR | 3,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,210,637 | 36.0% |
| RETURN_CONST | 887,318 | 26.4% |
| NOP | 480,100 | 14.3% |
| RETURN_VALUE | 478,260 | 14.2% |
| LOAD_FAST_LOAD_FAST | 122,720 | 3.7% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,732,323 | 52.2% |
| LOAD_FAST | 4,284,964 | 47.3% |
| STORE_ATTR_SLOT | 41,769 | 0.5% |
| STORE_ATTR | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,673,103 | 51.6% |
| LOAD_FAST_LOAD_FAST | 2,256,280 | 24.9% |
| LOAD_CONST | 1,890,689 | 20.9% |
| LOAD_GLOBAL_MODULE | 136,855 | 1.5% |
| RETURN_CONST | 45,660 | 0.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,574,099 | 68.9% |
| LOAD_FAST | 397,957 | 17.4% |
| CALL_TUPLE_1 | 181,360 | 7.9% |
| RETURN_VALUE | 82,840 | 3.6% |
| LOAD_CONST | 39,339 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,660,519 | 72.7% |
| EXTENDED_ARG | 226,737 | 9.9% |
| LOAD_FAST_LOAD_FAST | 184,960 | 8.1% |
| LOAD_FAST | 165,801 | 7.3% |
| LOAD_GLOBAL_MODULE | 38,959 | 1.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,849,697 | 92.7% |
| SWAP | 1,208,120 | 5.9% |
| BINARY_SUBSCR_DICT | 112,800 | 0.6% |
| LOAD_FAST | 99,409 | 0.5% |
| BINARY_OP_SUBTRACT_INT | 49,280 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,114,886 | 49.7% |
| LOAD_FAST_LOAD_FAST | 10,021,440 | 49.3% |
| LOAD_CONST | 160,200 | 0.8% |
| LOAD_FAST | 21,140 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 21,060 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,400 | 98.7% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| STORE_FAST_LOAD_FAST | 1,240 | 0.5% |
| TO_BOOL | 383 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 217,404 | 95.2% |
| POP_JUMP_IF_FALSE | 9,570 | 4.2% |
| TO_BOOL_ALWAYS_TRUE | 1,420 | 0.6% |
| TO_BOOL | 49 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 59,843,510 | 34.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 44,303,086 | 25.7% |
| LOAD_FAST | 21,619,608 | 12.5% |
| CALL_BUILTIN_FAST | 18,103,485 | 10.5% |
| CALL_BUILTIN_O | 9,907,520 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 111,645,385 | 64.6% |
| POP_JUMP_IF_TRUE | 54,464,852 | 31.5% |
| EXTENDED_ARG | 5,486,066 | 3.2% |
| UNARY_NOT | 1,118,718 | 0.6% |
| TO_BOOL_NONE | 1,280 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,368,442 | 93.3% |
| BINARY_OP | 733,018 | 3.7% |
| BINARY_SUBSCR_LIST_INT | 485,260 | 2.5% |
| BINARY_SUBSCR_TUPLE_INT | 63,334 | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 24,845 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,557,305 | 53.6% |
| POP_JUMP_IF_TRUE | 9,137,796 | 46.4% |
| TO_BOOL_NONE | 440 | 0.0% |
| UNARY_NOT | 165 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,234,533 | 97.0% |
| COPY | 39,560 | 1.7% |
| LOAD_DEREF | 10,886 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 8,780 | 0.4% |
| STORE_FAST | 6,240 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 834,377 | 36.2% |
| POP_JUMP_IF_TRUE | 784,524 | 34.1% |
| UNARY_NOT | 661,863 | 28.7% |
| EXTENDED_ARG | 21,480 | 0.9% |
| TO_BOOL_NONE | 240 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,841,695 | 68.0% |
| RETURN_VALUE | 389,086 | 14.4% |
| LOAD_ATTR_PROPERTY | 293,361 | 10.8% |
| CALL_METHOD_DESCRIPTOR_O | 104,000 | 3.8% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 42,037 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,944,364 | 71.8% |
| POP_JUMP_IF_TRUE | 745,549 | 27.5% |
| EXTENDED_ARG | 15,420 | 0.6% |
| TO_BOOL_BOOL | 1,683 | 0.1% |
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
| LOAD_FAST | 120,303 | 66.8% |
| RETURN_VALUE | 49,120 | 27.3% |
| CALL_BUILTIN_CLASS | 2,600 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 1,880 | 1.0% |
| FOR_ITER_LIST | 1,880 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 114,940 | 63.8% |
| STORE_FAST_STORE_FAST | 65,123 | 36.2% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 885,196 | 54.3% |
| RETURN_VALUE | 660,889 | 40.5% |
| STORE_FAST | 79,520 | 4.9% |
| CALL_METHOD_DESCRIPTOR_O | 3,680 | 0.2% |
| UNPACK_SEQUENCE | 1,139 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,436,452 | 88.1% |
| STORE_FAST | 154,792 | 9.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 39,760 | 2.4% |
| STORE_DEREF | 120 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 71,074,712 | 68.5% |
| RETURN_VALUE | 19,466,566 | 18.8% |
| BINARY_SUBSCR_LIST_INT | 7,546,045 | 7.3% |
| FOR_ITER_LIST | 4,719,671 | 4.5% |
| FOR_ITER_TUPLE | 717,399 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 98,983,211 | 95.4% |
| STORE_DEREF | 4,491,620 | 4.3% |
| STORE_FAST | 257,678 | 0.2% |
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
|     deferred | 35,268,481 | 65.2% |
|          hit | 18,802,737 | 34.7% |
|         miss | 120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,770 | 11.7% |
| Failure | 51,331 | 88.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 9,454 | 18.4% |
| multiply different types | 7,463 | 14.5% |
| subtract other | 6,800 | 13.2% |
| and int | 4,146 | 8.1% |
| rshift | 3,826 | 7.5% |
| or | 3,700 | 7.2% |
| power | 2,861 | 5.6% |
| true divide different types | 2,522 | 4.9% |
| multiply other | 2,360 | 4.6% |
| remainder | 2,310 | 4.5% |
| add different types | 1,948 | 3.8% |
| floor divide | 1,272 | 2.5% |
| subtract different types | 1,184 | 2.3% |
| xor | 583 | 1.1% |
| and other | 374 | 0.7% |
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
|     deferred | 24,102,630 | 36.1% |
|          hit | 42,684,286 | 63.8% |
|         miss | 45,552 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,356 | 32.1% |
| Failure | 17,636 | 67.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 12,213 | 69.3% |
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
|     deferred | 26,137,072 | 5.9% |
|        deopt | 31,040 | 0.0% |
|          hit | 384,717,115 | 86.9% |
|         miss | 31,333,304 | 7.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 671,612 | 90.2% |
| Failure | 72,899 | 9.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class mutable | 28,645 | 39.3% |
| code complex parameters | 14,046 | 19.3% |
| class no vectorcall | 9,220 | 12.6% |
| cfunc varargs keywords | 6,384 | 8.8% |
| other | 3,039 | 4.2% |
| wrong number arguments | 2,520 | 3.5% |
| cfunc noargs | 2,400 | 3.3% |
| bound method | 2,168 | 3.0% |
| meth descr varargs | 1,917 | 2.6% |
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
|     deferred | 38,487,189 | 36.7% |
|          hit | 65,705,046 | 62.7% |
|         miss | 575,933 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20,461 | 22.8% |
| Failure | 69,345 | 77.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 18,494 | 26.7% |
| other | 15,220 | 21.9% |
| different types | 12,278 | 17.7% |
| tuple | 10,064 | 14.5% |
| string | 9,960 | 14.4% |
| bool | 2,129 | 3.1% |
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
|     deferred | 103,683,585 | 48.5% |
|          hit | 108,469,877 | 50.7% |
|         miss | 1,555,559 | 0.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 41,223 | 30.0% |
| Failure | 96,203 | 70.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 68,030 | 70.7% |
| set | 9,023 | 9.4% |
| zip | 7,600 | 7.9% |
| enumerate | 4,230 | 4.4% |
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
|     deferred | 120,211,290 | 27.4% |
|        deopt | 20 | 0.0% |
|          hit | 250,357,873 | 57.0% |
|         miss | 67,435,295 | 15.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,350,089 | 89.4% |
| Failure | 160,091 | 10.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 60,816 | 38.0% |
| mutable class | 58,754 | 36.7% |
| method | 10,466 | 6.5% |
| has managed dict | 8,780 | 5.5% |
| overridden | 8,668 | 5.4% |
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
|     deferred | 89,869 | 0.0% |
|          hit | 379,574,073 | 99.9% |
|         miss | 20,420 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 91,931 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 604 | 0.0% |
|          hit | 2,996,105 | 100.0% |

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
|          hit | 999,128 | 67.8% |
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
|     deferred | 540,640 | 4.2% |
|          hit | 10,198,159 | 78.4% |
|         miss | 2,220,726 | 17.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 46,829 | 92.3% |
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
|     deferred | 3,422,332 | 13.1% |
|          hit | 22,624,383 | 86.8% |

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
|     deferred | 12,842,246 | 6.1% |
|          hit | 197,731,641 | 93.7% |
|         miss | 440,075 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 59,921 | 72.2% |
| Failure | 23,032 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 10,781 | 46.8% |
| number | 3,518 | 15.3% |
| mapping | 3,300 | 14.3% |
| dict | 2,340 | 10.2% |
| other | 1,627 | 7.1% |
| set | 1,426 | 6.2% |
| float | 40 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 27,547 | 0.0% |
|          hit | 105,567,636 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 11,388 | 93.6% |
| Failure | 774 | 6.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 714 | 92.2% |
| iterator | 60 | 7.8% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 3,220,768,896 | 54.1% |
| Not specialized | 800,461,892 | 13.5% |
| Specialized hits | 1,824,827,158 | 30.7% |
| Specialized misses | 103,657,644 | 1.7% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 120,211,290 | 32.9% |
| FOR_ITER | 103,683,585 | 28.4% |
| COMPARE_OP | 38,487,189 | 10.5% |
| BINARY_OP | 35,268,481 | 9.7% |
| CALL | 26,137,072 | 7.2% |
| BINARY_SUBSCR | 24,102,630 | 6.6% |
| TO_BOOL | 12,842,246 | 3.5% |
| STORE_SUBSCR | 3,422,332 | 0.9% |
| STORE_ATTR | 540,640 | 0.1% |
| SEND | 439,140 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 36,600,304 | 35.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 17,009,268 | 16.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 14,278,483 | 13.8% |
| LOAD_ATTR_METHOD_NO_DICT | 9,218,195 | 8.9% |
| CALL_PY_EXACT_ARGS | 7,817,971 | 7.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,479,337 | 6.3% |
| LOAD_ATTR_PROPERTY | 4,124,228 | 4.0% |
| CALL_BUILTIN_O | 2,661,160 | 2.6% |
| STORE_ATTR_SLOT | 2,219,746 | 2.1% |
| FOR_ITER_TUPLE | 792,228 | 0.8% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 127,461,666 | 46.8% |
| Calls to Python functions inlined | 144,846,877 | 53.2% |
| Calls via PyEval_EvalFrame (total) | 127,461,666 | 46.8% |
| Calls via PyEval_EvalFrame (vector) | 98,453,268 | 36.2% |
| Calls via PyEval_EvalFrame (generator) | 29,008,398 | 10.7% |
| Calls via PyEval_EvalFrame (legacy) | 4,640 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 98,445,968 | 36.2% |
| Calls via PyEval_EvalFrame (build class) | 2,660 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 23,668,029 | 8.7% |
| Calls via PyEval_EvalFrame (function ex) | 11,824,915 | 4.3% |
| Calls via PyEval_EvalFrame (api) | 53,326,485 | 19.6% |
| Calls via PyEval_EvalFrame (method) | 6,960 | 0.0% |
| Frame objects created | 1,287,023 | 0.5% |
| Frames pushed | 112,603,045 | 41.4% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 363,426,236 | 54.3% |
| Frees to freelist | 363,669,136 |  |
| Allocations | 305,609,602 | 45.7% |
| Allocations to 512 bytes | 304,542,773 | 45.5% |
| Allocations to 4 kbytes | 1,042,369 | 0.2% |
| Allocations over 4 kbytes | 24,460 | 0.0% |
| Frees | 313,295,983 |  |
| New values | 1,057,312 |  |
| Interpreter increfs | 2,568,654,719 | 64.2% |
| Interpreter decrefs | 2,993,954,701 | 65.4% |
| Increfs | 1,430,379,324 | 35.8% |
| Decrefs | 1,585,872,536 | 34.6% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 60 | 0.0% |
| Method cache hits | 242,920,049 |  |
| Method cache misses | 4,608,573 |  |
| Method cache collisions | 6,037,265 |  |
| Method cache dunder hits | 347,179,251 |  |
| Method cache dunder misses | 1,429,223 |  |


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
