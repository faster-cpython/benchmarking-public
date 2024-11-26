
# Pystats results

- benchmark: mypy2
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 1,508,381,658 | 20.7% | 20.7% |  |
| RESUME_CHECK | 357,705,952 | 4.9% | 25.6% | 0.0% |
| LOAD_CONST | 356,150,421 | 4.9% | 30.4% |  |
| LOAD_GLOBAL_MODULE | 314,376,100 | 4.3% | 34.8% | 0.0% |
| STORE_ATTR_SLOT | 311,137,969 | 4.3% | 39.0% | 21.7% |
| LOAD_FAST_LOAD_FAST | 289,438,226 | 4.0% | 43.0% |  |
| LOAD_GLOBAL_BUILTIN | 280,667,657 | 3.8% | 46.8% | 0.0% |
| POP_JUMP_IF_FALSE | 279,198,601 | 3.8% | 50.7% |  |
| LOAD_ATTR_SLOT | 259,041,372 | 3.5% | 54.2% | 1.7% |
| STORE_FAST | 254,655,188 | 3.5% | 57.7% |  |
| CALL_PY_EXACT_ARGS | 226,006,096 | 3.1% | 60.8% | 10.2% |
| TO_BOOL_BOOL | 213,283,727 | 2.9% | 63.7% | 0.0% |
| RETURN_VALUE | 204,595,827 | 2.8% | 66.5% |  |
| RETURN_CONST | 154,793,056 | 2.1% | 68.6% |  |
| CALL_ISINSTANCE | 141,769,767 | 1.9% | 70.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 134,569,622 | 1.8% | 72.4% | 21.8% |
| POP_TOP | 114,181,841 | 1.6% | 74.0% |  |
| POP_JUMP_IF_TRUE | 113,910,288 | 1.6% | 75.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 79,687,559 | 1.1% | 76.6% | 2.7% |
| LOAD_DEREF | 66,784,632 | 0.9% | 77.6% |  |
| FOR_ITER_LIST | 65,901,455 | 0.9% | 78.5% | 1.7% |
| INTERPRETER_EXIT | 64,184,452 | 0.9% | 79.3% |  |
| GET_ITER | 62,261,703 | 0.9% | 80.2% |  |
| LOAD_ATTR | 61,429,005 | 0.8% | 81.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 59,426,337 | 0.8% | 81.8% | 12.9% |
| BINARY_SUBSCR_DICT | 58,418,898 | 0.8% | 82.6% |  |
| ENTER_EXECUTOR | 51,887,323 | 0.7% | 83.4% |  |
| POP_JUMP_IF_NOT_NONE | 49,463,047 | 0.7% | 84.0% |  |
| COPY_FREE_VARS | 48,322,395 | 0.7% | 84.7% |  |
| CONTAINS_OP | 48,153,510 | 0.7% | 85.4% |  |
| SWAP | 44,723,524 | 0.6% | 86.0% |  |
| LOAD_SUPER_ATTR_METHOD | 44,076,769 | 0.6% | 86.6% |  |
| BUILD_LIST | 42,546,593 | 0.6% | 87.2% |  |
| STORE_ATTR_INSTANCE_VALUE | 41,570,547 | 0.6% | 87.7% | 2.1% |
| POP_JUMP_IF_NONE | 40,932,069 | 0.6% | 88.3% |  |
| CALL_KW | 39,196,755 | 0.5% | 88.8% |  |
| CALL | 35,041,010 | 0.5% | 89.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 33,507,348 | 0.5% | 89.8% | 8.9% |
| IS_OP | 29,521,741 | 0.4% | 90.2% |  |
| NOP | 28,412,473 | 0.4% | 90.6% |  |
| JUMP_FORWARD | 26,477,605 | 0.4% | 90.9% |  |
| COPY | 26,411,868 | 0.4% | 91.3% |  |
| COMPARE_OP_STR | 23,671,672 | 0.3% | 91.6% | 0.3% |
| TO_BOOL_LIST | 23,241,826 | 0.3% | 91.9% | 0.7% |
| COMPARE_OP | 21,967,034 | 0.3% | 92.2% |  |
| BINARY_SUBSCR | 21,190,865 | 0.3% | 92.5% |  |
| CALL_BUILTIN_CLASS | 21,089,401 | 0.3% | 92.8% |  |
| COMPARE_OP_INT | 19,702,507 | 0.3% | 93.1% | 2.3% |
| CALL_LEN | 18,477,802 | 0.3% | 93.3% |  |
| PUSH_NULL | 18,394,104 | 0.3% | 93.6% |  |
| MAKE_CELL | 17,475,233 | 0.2% | 93.8% |  |
| LOAD_ATTR_WITH_HINT | 17,181,577 | 0.2% | 94.1% | 2.2% |
| TO_BOOL_NONE | 16,824,946 | 0.2% | 94.3% | 8.5% |
| CALL_LIST_APPEND | 16,633,758 | 0.2% | 94.5% |  |
| BUILD_TUPLE | 16,519,507 | 0.2% | 94.7% |  |
| MAP_ADD | 15,635,199 | 0.2% | 95.0% |  |
| FOR_ITER_TUPLE | 15,505,137 | 0.2% | 95.2% | 6.8% |
| TO_BOOL_ALWAYS_TRUE | 15,003,588 | 0.2% | 95.4% | 13.4% |
| LOAD_ATTR_PROPERTY | 14,845,109 | 0.2% | 95.6% | 6.9% |
| STORE_FAST_STORE_FAST | 14,683,343 | 0.2% | 95.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,519,620 | 0.2% | 96.0% | 28.7% |
| LOAD_FAST_AND_CLEAR | 14,174,549 | 0.2% | 96.2% |  |
| EXTENDED_ARG | 14,047,108 | 0.2% | 96.4% |  |
| LOAD_ATTR_MODULE | 13,666,639 | 0.2% | 96.6% | 0.0% |
| UNARY_NOT | 13,444,526 | 0.2% | 96.7% |  |
| LIST_APPEND | 12,848,468 | 0.2% | 96.9% |  |
| FOR_ITER | 12,493,782 | 0.2% | 97.1% |  |
| CALL_PY_WITH_DEFAULTS | 10,801,875 | 0.1% | 97.2% | 2.2% |
| TO_BOOL | 10,584,828 | 0.1% | 97.4% |  |
| CALL_TUPLE_1 | 10,397,741 | 0.1% | 97.5% |  |
| BINARY_SUBSCR_LIST_INT | 9,715,674 | 0.1% | 97.7% | 0.0% |
| JUMP_BACKWARD | 8,862,398 | 0.1% | 97.8% |  |
| CALL_BUILTIN_O | 8,328,912 | 0.1% | 97.9% | 9.1% |
| LOAD_ATTR_CLASS | 7,733,097 | 0.1% | 98.0% | 1.7% |
| UNPACK_SEQUENCE_LIST | 7,192,870 | 0.1% | 98.1% |  |
| STORE_ATTR | 6,710,724 | 0.1% | 98.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,609,421 | 0.1% | 98.3% |  |
| CALL_BUILTIN_FAST | 6,577,560 | 0.1% | 98.4% | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 6,056,615 | 0.1% | 98.4% | 0.0% |
| YIELD_VALUE | 6,024,055 | 0.1% | 98.5% |  |
| DELETE_ATTR | 6,013,389 | 0.1% | 98.6% |  |
| BUILD_MAP | 5,889,035 | 0.1% | 98.7% |  |
| CALL_TYPE_1 | 5,665,591 | 0.1% | 98.8% |  |
| FOR_ITER_RANGE | 4,904,831 | 0.1% | 98.8% |  |
| TO_BOOL_STR | 4,675,540 | 0.1% | 98.9% | 4.1% |
| MAKE_FUNCTION | 4,432,560 | 0.1% | 99.0% |  |
| CALL_FUNCTION_EX | 4,198,995 | 0.1% | 99.0% |  |
| RETURN_GENERATOR | 4,141,468 | 0.1% | 99.1% |  |
| STORE_FAST_LOAD_FAST | 4,004,639 | 0.1% | 99.1% |  |
| BINARY_OP_ADD_INT | 3,803,402 | 0.1% | 99.2% | 0.5% |
| BINARY_SLICE | 3,053,827 | 0.0% | 99.2% |  |
| BINARY_OP_ADD_UNICODE | 2,931,668 | 0.0% | 99.3% |  |
| SET_FUNCTION_ATTRIBUTE | 2,720,434 | 0.0% | 99.3% |  |
| STORE_SUBSCR_DICT | 2,492,787 | 0.0% | 99.3% |  |
| STORE_DEREF | 2,481,088 | 0.0% | 99.4% |  |
| BINARY_OP | 2,471,201 | 0.0% | 99.4% |  |
| CALL_ALLOC_AND_ENTER_INIT | 2,319,474 | 0.0% | 99.4% | 0.2% |
| EXIT_INIT_CHECK | 2,314,692 | 0.0% | 99.5% |  |
| CHECK_EXC_MATCH | 2,208,892 | 0.0% | 99.5% |  |
| POP_EXCEPT | 2,208,892 | 0.0% | 99.5% |  |
| PUSH_EXC_INFO | 2,208,892 | 0.0% | 99.6% |  |
| DICT_MERGE | 2,095,903 | 0.0% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 1,970,273 | 0.0% | 99.6% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,969,581 | 0.0% | 99.6% | 0.0% |
| STORE_SUBSCR | 1,923,615 | 0.0% | 99.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,579,734 | 0.0% | 99.7% | 11.0% |
| LOAD_FAST_CHECK | 1,490,934 | 0.0% | 99.7% |  |
| BEFORE_WITH | 1,474,024 | 0.0% | 99.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,447,287 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_GETITEM | 1,401,691 | 0.0% | 99.8% | 0.0% |
| IMPORT_FROM | 1,260,509 | 0.0% | 99.8% |  |
| FORMAT_SIMPLE | 1,229,519 | 0.0% | 99.8% |  |
| UNPACK_SEQUENCE_TUPLE | 1,052,880 | 0.0% | 99.8% |  |
| IMPORT_NAME | 1,032,258 | 0.0% | 99.8% |  |
| TO_BOOL_INT | 1,006,013 | 0.0% | 99.8% | 4.3% |
| BUILD_SET | 993,325 | 0.0% | 99.9% |  |
| UNARY_NEGATIVE | 977,224 | 0.0% | 99.9% |  |
| STORE_ATTR_WITH_HINT | 927,130 | 0.0% | 99.9% | 2.7% |
| BINARY_SUBSCR_TUPLE_INT | 882,560 | 0.0% | 99.9% | 0.0% |
| BUILD_STRING | 755,970 | 0.0% | 99.9% |  |
| SET_ADD | 726,738 | 0.0% | 99.9% |  |
| FOR_ITER_GEN | 688,357 | 0.0% | 99.9% |  |
| CALL_STR_1 | 610,639 | 0.0% | 99.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 546,970 | 0.0% | 99.9% | 1.9% |
| LOAD_SUPER_ATTR_ATTR | 541,511 | 0.0% | 99.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 534,795 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 509,481 | 0.0% | 100.0% | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 290,457 | 0.0% | 100.0% |  |
| RERAISE | 274,263 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 246,215 | 0.0% | 100.0% |  |
| SEND_GEN | 245,260 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 224,486 | 0.0% | 100.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 202,612 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 172,343 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 146,918 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 143,289 | 0.0% | 100.0% | 13.6% |
| DELETE_FAST | 102,124 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 98,950 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 80,253 | 0.0% | 100.0% |  |
| LIST_EXTEND | 77,678 | 0.0% | 100.0% |  |
| END_SEND | 50,355 | 0.0% | 100.0% |  |
| GET_YIELD_FROM_ITER | 50,355 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 44,113 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 43,602 | 0.0% | 100.0% |  |
| RESUME | 41,330 | 0.0% | 100.0% | 0.1% |
| CONVERT_VALUE | 34,046 | 0.0% | 100.0% |  |
| END_FOR | 27,299 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 16,440 | 0.0% | 100.0% |  |
| BUILD_SLICE | 9,399 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 4,859 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 3,468 | 0.0% | 100.0% |  |
| STORE_NAME | 2,456 | 0.0% | 100.0% |  |
| LOAD_NAME | 2,287 | 0.0% | 100.0% |  |
| UNARY_INVERT | 920 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 908 | 0.0% | 100.0% |  |
| DICT_UPDATE | 800 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 760 | 0.0% | 100.0% |  |
| STORE_SLICE | 555 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 523 | 0.0% | 100.0% |  |
| UNPACK_EX | 486 | 0.0% | 100.0% |  |
| SET_UPDATE | 308 | 0.0% | 100.0% |  |
| SEND | 120 | 0.0% | 100.0% |  |
| SETUP_ANNOTATIONS | 84 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 46 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_SLOT | 228,592,275 | 3.1% | 3.1% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 196,073,583 | 2.7% | 5.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 195,711,860 | 2.7% | 8.5% |
| LOAD_FAST STORE_ATTR_SLOT | 182,562,786 | 2.5% | 11.0% |
| RESUME_CHECK LOAD_FAST | 157,072,160 | 2.2% | 13.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 144,128,880 | 2.0% | 15.1% |
| LOAD_CONST LOAD_FAST | 142,959,317 | 2.0% | 17.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 139,269,109 | 1.9% | 19.0% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 138,520,624 | 1.9% | 20.9% |
| POP_JUMP_IF_FALSE LOAD_FAST | 129,779,428 | 1.8% | 22.7% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 126,804,581 | 1.7% | 24.4% |
| STORE_FAST LOAD_FAST | 125,424,558 | 1.7% | 26.1% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 120,296,078 | 1.6% | 27.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 97,995,489 | 1.3% | 29.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 86,527,028 | 1.2% | 30.3% |
| STORE_ATTR_SLOT LOAD_CONST | 85,947,139 | 1.2% | 31.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 84,538,052 | 1.2% | 32.6% |
| LOAD_FAST LOAD_CONST | 79,217,769 | 1.1% | 33.7% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 71,978,497 | 1.0% | 34.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 68,273,496 | 0.9% | 35.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 64,087,561 | 0.9% | 36.5% |
| STORE_ATTR_SLOT RETURN_CONST | 61,637,187 | 0.8% | 37.4% |
| LOAD_FAST RETURN_VALUE | 60,736,815 | 0.8% | 38.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 59,854,405 | 0.8% | 39.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 59,454,080 | 0.8% | 39.8% |
| STORE_ATTR_SLOT LOAD_FAST | 56,003,317 | 0.8% | 40.6% |
| RETURN_CONST POP_TOP | 54,483,196 | 0.7% | 41.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 52,675,692 | 0.7% | 42.1% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 52,663,174 | 0.7% | 42.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 50,391,278 | 0.7% | 43.5% |
| LOAD_CONST BINARY_SUBSCR_DICT | 50,240,772 | 0.7% | 44.2% |
| POP_TOP LOAD_FAST | 48,591,764 | 0.7% | 44.8% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 48,371,870 | 0.7% | 45.5% |
| COPY_FREE_VARS RESUME_CHECK | 47,811,082 | 0.7% | 46.2% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 47,199,082 | 0.6% | 46.8% |
| RETURN_VALUE STORE_FAST | 46,520,276 | 0.6% | 47.4% |
| LOAD_DEREF LOAD_FAST | 45,132,257 | 0.6% | 48.1% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 44,074,352 | 0.6% | 48.7% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 43,282,848 | 0.6% | 49.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 41,272,623 | 0.6% | 49.8% |
| LOAD_FAST LOAD_ATTR | 40,774,389 | 0.6% | 50.4% |
| RETURN_VALUE RETURN_VALUE | 40,774,174 | 0.6% | 50.9% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 40,603,641 | 0.6% | 51.5% |
| LOAD_FAST LOAD_FAST | 40,388,814 | 0.6% | 52.0% |
| LOAD_CONST CALL_KW | 38,340,134 | 0.5% | 52.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 38,144,869 | 0.5% | 53.1% |
| CACHE RESUME_CHECK | 37,843,962 | 0.5% | 53.6% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 37,328,207 | 0.5% | 54.1% |
| LOAD_SUPER_ATTR_METHOD LOAD_FAST_LOAD_FAST | 36,632,755 | 0.5% | 54.6% |
| RESUME_CHECK RETURN_CONST | 34,608,807 | 0.5% | 55.1% |
| RETURN_CONST INTERPRETER_EXIT | 33,314,195 | 0.5% | 55.6% |
| LOAD_ATTR_SLOT LOAD_FAST | 31,713,585 | 0.4% | 56.0% |
| RETURN_CONST LOAD_FAST | 31,492,766 | 0.4% | 56.4% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 31,135,597 | 0.4% | 56.9% |
| STORE_FAST LOAD_GLOBAL_MODULE | 29,903,460 | 0.4% | 57.3% |
| FOR_ITER_LIST STORE_FAST | 29,615,758 | 0.4% | 57.7% |
| LOAD_ATTR LOAD_FAST | 27,875,990 | 0.4% | 58.0% |
| LOAD_CONST LOAD_CONST | 27,534,514 | 0.4% | 58.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 27,426,946 | 0.4% | 58.8% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 26,186,044 | 0.4% | 59.2% |
| RETURN_VALUE LOAD_FAST | 25,866,755 | 0.4% | 59.5% |
| RETURN_VALUE INTERPRETER_EXIT | 25,655,509 | 0.4% | 59.9% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 24,392,129 | 0.3% | 60.2% |
| LOAD_ATTR_SLOT GET_ITER | 24,354,758 | 0.3% | 60.5% |
| LOAD_FAST CONTAINS_OP | 23,800,919 | 0.3% | 60.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 23,696,877 | 0.3% | 61.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 23,505,189 | 0.3% | 61.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 23,154,134 | 0.3% | 61.8% |
| GET_ITER FOR_ITER_LIST | 23,107,631 | 0.3% | 62.1% |
| LOAD_ATTR_SLOT STORE_FAST | 22,949,322 | 0.3% | 62.5% |
| CACHE COPY_FREE_VARS | 22,250,568 | 0.3% | 62.8% |
| CALL_KW RESUME_CHECK | 22,210,600 | 0.3% | 63.1% |
| ENTER_EXECUTOR FOR_ITER_LIST | 22,130,102 | 0.3% | 63.4% |
| RETURN_CONST RETURN_VALUE | 21,917,808 | 0.3% | 63.7% |
| LOAD_GLOBAL_MODULE IS_OP | 21,603,930 | 0.3% | 64.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 21,175,267 | 0.3% | 64.3% |
| LOAD_FAST POP_JUMP_IF_NONE | 20,129,632 | 0.3% | 64.5% |
| COPY TO_BOOL_BOOL | 20,112,137 | 0.3% | 64.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 20,013,462 | 0.3% | 65.1% |
| IS_OP POP_JUMP_IF_FALSE | 19,910,184 | 0.3% | 65.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 19,670,528 | 0.3% | 65.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 19,642,343 | 0.3% | 65.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 19,630,003 | 0.3% | 66.2% |
| LOAD_ATTR_SLOT RETURN_VALUE | 19,344,808 | 0.3% | 66.4% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_BUILTIN | 19,012,170 | 0.3% | 66.7% |
| POP_TOP LOAD_FAST_LOAD_FAST | 18,046,752 | 0.2% | 66.9% |
| LOAD_ATTR_SLOT LOAD_ATTR_SLOT | 17,949,098 | 0.2% | 67.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 17,708,858 | 0.2% | 67.4% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 17,702,571 | 0.2% | 67.7% |
| LOAD_FAST TO_BOOL_BOOL | 17,608,080 | 0.2% | 67.9% |
| RETURN_VALUE POP_TOP | 17,547,882 | 0.2% | 68.1% |
| LOAD_FAST TO_BOOL_LIST | 17,402,843 | 0.2% | 68.4% |
| TO_BOOL_LIST POP_JUMP_IF_TRUE | 17,377,962 | 0.2% | 68.6% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 17,368,531 | 0.2% | 68.9% |
| LOAD_CONST COMPARE_OP_STR | 17,188,088 | 0.2% | 69.1% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 17,008,629 | 0.2% | 69.3% |
| BUILD_LIST STORE_FAST | 16,677,119 | 0.2% | 69.6% |
| NOP LOAD_FAST | 16,465,482 | 0.2% | 69.8% |
| STORE_ATTR_SLOT LOAD_GLOBAL_BUILTIN | 16,184,493 | 0.2% | 70.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 15,717,788 | 0.2% | 70.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,340,967 | 76.7% |
| BINARY_OP_SUBTRACT_INT | 445,059 | 14.6% |
| LOAD_FAST | 197,860 | 6.5% |
| BINARY_OP_ADD_INT | 52,642 | 1.7% |
| LOAD_ATTR_SLOT | 12,243 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,224,843 | 40.1% |
| CALL_PY_EXACT_ARGS | 446,248 | 14.6% |
| STORE_FAST | 368,203 | 12.1% |
| GET_ITER | 350,895 | 11.5% |
| BUILD_TUPLE | 152,276 | 5.0% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 555 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 555 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 37,843,962 | 58.9% |
| COPY_FREE_VARS | 22,250,568 | 34.7% |
| POP_TOP | 4,042,477 | 6.3% |
| RETURN_GENERATOR | 46,716 | 0.1% |
| PUSH_EXC_INFO | 21,439 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,431,999 | 97.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,113 | 1.6% |
| CALL | 17,684 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 126 | 0.0% |
| JUMP_FORWARD | 82 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,321,090 | 89.6% |
| STORE_FAST | 152,934 | 10.4% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 166,373 | 57.3% |
| RETURN_VALUE | 98,638 | 34.0% |
| BUILD_STRING | 22,367 | 7.7% |
| LOAD_FAST_LOAD_FAST | 2,280 | 0.8% |
| BINARY_SUBSCR_STR_INT | 400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 263,452 | 90.7% |
| LOAD_FAST | 23,865 | 8.2% |
| JUMP_FORWARD | 2,029 | 0.7% |
| JUMP_BACKWARD | 651 | 0.2% |
| LOAD_FAST_LOAD_FAST | 460 | 0.2% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,762,660 | 50.8% |
| LOAD_FAST_LOAD_FAST | 7,516,122 | 35.5% |
| LOAD_FAST | 1,890,689 | 8.9% |
| LOAD_GLOBAL_MODULE | 623,338 | 2.9% |
| COPY | 163,652 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,649,093 | 40.8% |
| CONTAINS_OP | 2,525,771 | 11.9% |
| LOAD_CONST | 2,451,611 | 11.6% |
| LOAD_FAST | 1,666,191 | 7.9% |
| RETURN_VALUE | 1,541,331 | 7.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,199,684 | 99.6% |
| BUILD_TUPLE | 8,423 | 0.4% |
| LOAD_GLOBAL_MODULE | 423 | 0.0% |
| LOAD_GLOBAL | 362 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,208,892 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,133 | 54.7% |
| LOAD_FAST | 8,922 | 20.2% |
| BUILD_SLICE | 8,638 | 19.6% |
| LOAD_FAST_LOAD_FAST | 2,420 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 32,744 | 74.2% |
| LOAD_DEREF | 8,638 | 19.6% |
| JUMP_BACKWARD | 1,216 | 2.8% |
| RETURN_CONST | 972 | 2.2% |
| LOAD_FAST | 320 | 0.7% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 27,299 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 27,299 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 50,355 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 50,355 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,314,692 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,314,692 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 796,855 | 64.8% |
| RETURN_VALUE | 214,570 | 17.5% |
| BINARY_SUBSCR_TUPLE_INT | 149,308 | 12.1% |
| CONVERT_VALUE | 34,046 | 2.8% |
| LOAD_ATTR_SLOT | 20,826 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 719,643 | 58.5% |
| BUILD_STRING | 509,856 | 41.5% |
| LOAD_FAST | 20 | 0.0% |


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 600 | 78.9% |
| LOAD_CONST | 160 | 21.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 24,354,758 | 39.1% |
| LOAD_FAST | 15,041,889 | 24.2% |
| CALL_BUILTIN_CLASS | 9,996,895 | 16.1% |
| BINARY_SUBSCR_DICT | 6,203,361 | 10.0% |
| CALL | 1,409,826 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 23,107,631 | 37.1% |
| LOAD_FAST_AND_CLEAR | 13,508,899 | 21.7% |
| FOR_ITER_TUPLE | 9,567,778 | 15.4% |
| FOR_ITER | 7,747,205 | 12.4% |
| FOR_ITER_RANGE | 3,078,048 | 4.9% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 50,355 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 50,355 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 33,314,195 | 51.9% |
| RETURN_VALUE | 25,655,509 | 40.0% |
| YIELD_VALUE | 5,168,032 | 8.1% |
| RETURN_GENERATOR | 46,716 | 0.1% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 23 | 50.0% |
| POP_TOP | 20 | 43.5% |
| STORE_SUBSCR | 3 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 46 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,432,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,279,028 | 51.4% |
| SET_FUNCTION_ATTRIBUTE | 2,114,370 | 47.7% |
| LOAD_CONST | 25,150 | 0.6% |
| LOAD_GLOBAL_MODULE | 7,386 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 3,674 | 0.1% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,568,604 | 30.2% |
| POP_JUMP_IF_TRUE | 7,002,534 | 24.6% |
| POP_JUMP_IF_FALSE | 4,692,123 | 16.5% |
| RESUME_CHECK | 3,419,340 | 12.0% |
| POP_JUMP_IF_NOT_NONE | 1,446,599 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,465,482 | 58.0% |
| LOAD_CONST | 7,389,949 | 26.0% |
| LOAD_GLOBAL_BUILTIN | 2,646,342 | 9.3% |
| LOAD_GLOBAL_MODULE | 1,555,762 | 5.5% |
| LOAD_FAST_LOAD_FAST | 292,087 | 1.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,437,552 | 65.1% |
| SWAP | 633,961 | 28.7% |
| COPY | 129,581 | 5.9% |
| STORE_FAST | 7,006 | 0.3% |
| POP_JUMP_IF_FALSE | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,437,116 | 65.1% |
| RETURN_VALUE | 633,961 | 28.7% |
| RERAISE | 129,581 | 5.9% |
| JUMP_BACKWARD_NO_INTERRUPT | 7,326 | 0.3% |
| EXTENDED_ARG | 321 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 54,483,196 | 47.7% |
| RETURN_VALUE | 17,547,882 | 15.4% |
| POP_JUMP_IF_FALSE | 10,848,152 | 9.5% |
| POP_JUMP_IF_TRUE | 9,021,369 | 7.9% |
| RESUME_CHECK | 4,367,875 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,591,764 | 42.6% |
| LOAD_FAST_LOAD_FAST | 18,046,752 | 15.8% |
| RETURN_CONST | 12,107,454 | 10.6% |
| ENTER_EXECUTOR | 10,838,898 | 9.5% |
| LOAD_CONST | 4,579,166 | 4.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 1,271,890 | 57.6% |
| LOAD_ATTR_SLOT | 631,903 | 28.6% |
| RERAISE | 107,982 | 4.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 89,628 | 4.1% |
| RAISE_VARARGS | 64,113 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,207,744 | 99.9% |
| LOAD_GLOBAL | 785 | 0.0% |
| LOAD_GLOBAL_MODULE | 363 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,024,749 | 49.1% |
| LOAD_ATTR | 4,462,005 | 24.3% |
| LOAD_ATTR_MODULE | 2,965,904 | 16.1% |
| BINARY_SUBSCR_DICT | 775,408 | 4.2% |
| LOAD_SUPER_ATTR_ATTR | 538,631 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,846,756 | 80.7% |
| LOAD_FAST_LOAD_FAST | 2,944,565 | 16.0% |
| CALL | 286,698 | 1.6% |
| LOAD_CONST | 146,200 | 0.8% |
| LOAD_GLOBAL_BUILTIN | 94,011 | 0.5% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,313,820 | 55.9% |
| CALL_FUNCTION_EX | 1,269,530 | 30.7% |
| COPY_FREE_VARS | 508,193 | 12.3% |
| CACHE | 46,716 | 1.1% |
| MAKE_CELL | 1,282 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 2,474,402 | 59.7% |
| LOAD_FAST | 1,293,148 | 31.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 213,583 | 5.2% |
| GET_YIELD_FROM_ITER | 50,355 | 1.2% |
| INTERPRETER_EXIT | 46,716 | 1.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,736,815 | 29.7% |
| RETURN_VALUE | 40,774,174 | 19.9% |
| RETURN_CONST | 21,917,808 | 10.7% |
| LOAD_ATTR_SLOT | 19,344,808 | 9.5% |
| CALL | 7,730,119 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 46,520,276 | 22.7% |
| RETURN_VALUE | 40,774,174 | 19.9% |
| LOAD_FAST | 25,866,755 | 12.6% |
| INTERPRETER_EXIT | 25,655,509 | 12.5% |
| POP_TOP | 17,547,882 | 8.6% |


</details>

### SETUP_ANNOTATIONS

<details>
<summary> Successors and predecessors for SETUP_ANNOTATIONS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 43 | 51.2% |
| STORE_NAME | 41 | 48.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 43 | 51.2% |
| LOAD_NAME | 41 | 48.8% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,507,160 | 78.4% |
| LOAD_FAST | 194,680 | 10.1% |
| SWAP | 163,652 | 8.5% |
| LOAD_CONST | 44,767 | 2.3% |
| LOAD_ATTR_SLOT | 8,879 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,506,818 | 78.3% |
| LOAD_CONST | 191,803 | 10.0% |
| LOAD_FAST | 135,023 | 7.0% |
| RETURN_CONST | 85,112 | 4.4% |
| STORE_SUBSCR | 1,810 | 0.1% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 4,778,267 | 45.1% |
| LOAD_FAST | 3,578,115 | 33.8% |
| LOAD_ATTR_SLOT | 1,486,275 | 14.0% |
| COPY | 557,351 | 5.3% |
| LOAD_ATTR_WITH_HINT | 37,495 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,719,387 | 82.4% |
| POP_JUMP_IF_TRUE | 1,586,236 | 15.0% |
| UNARY_NOT | 166,394 | 1.6% |
| TO_BOOL_BOOL | 49,276 | 0.5% |
| TO_BOOL | 29,196 | 0.3% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 700 | 76.1% |
| LOAD_FAST | 220 | 23.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 920 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 506,796 | 51.9% |
| CALL_LEN | 445,199 | 45.6% |
| LOAD_GLOBAL_MODULE | 11,891 | 1.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 8,618 | 0.9% |
| LOAD_ATTR_INSTANCE_VALUE | 4,469 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 445,079 | 45.5% |
| COMPARE_OP_INT | 445,039 | 45.5% |
| CALL_PY_EXACT_ARGS | 45,167 | 4.6% |
| RETURN_VALUE | 13,278 | 1.4% |
| BUILD_TUPLE | 11,911 | 1.2% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 11,668,046 | 86.8% |
| TO_BOOL_LIST | 1,328,485 | 9.9% |
| TO_BOOL_STR | 195,538 | 1.5% |
| TO_BOOL | 166,394 | 1.2% |
| TO_BOOL_INT | 73,215 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,801,939 | 50.6% |
| RETURN_VALUE | 4,880,805 | 36.3% |
| COPY | 1,362,895 | 10.1% |
| LOAD_FAST | 255,507 | 1.9% |
| STORE_FAST | 87,376 | 0.6% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,383,995 | 56.0% |
| LOAD_FAST | 242,554 | 9.8% |
| BUILD_LIST | 204,438 | 8.3% |
| STORE_FAST | 177,181 | 7.2% |
| LOAD_ATTR | 100,964 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 996,506 | 40.3% |
| STORE_FAST | 640,633 | 25.9% |
| CALL_PY_EXACT_ARGS | 269,953 | 10.9% |
| GET_ITER | 115,980 | 4.7% |
| LOAD_CONST | 71,743 | 2.9% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 43,602 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 25,010 | 57.4% |
| STORE_FAST | 17,488 | 40.1% |
| DICT_UPDATE | 800 | 1.8% |
| LOAD_CONST | 160 | 0.4% |
| LOAD_FAST | 144 | 0.3% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 12,254,412 | 28.8% |
| STORE_FAST | 9,385,327 | 22.1% |
| LOAD_GLOBAL_MODULE | 5,506,825 | 12.9% |
| RESUME_CHECK | 4,623,541 | 10.9% |
| STORE_ATTR_SLOT | 2,110,783 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,677,119 | 39.2% |
| SWAP | 12,254,412 | 28.8% |
| CALL | 5,699,937 | 13.4% |
| LOAD_FAST | 4,132,360 | 9.7% |
| LOAD_GLOBAL_BUILTIN | 1,330,278 | 3.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,218,681 | 37.7% |
| LOAD_CONST | 887,799 | 15.1% |
| STORE_ATTR_INSTANCE_VALUE | 517,582 | 8.8% |
| RESUME_CHECK | 482,987 | 8.2% |
| POP_JUMP_IF_FALSE | 437,746 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,437,358 | 58.4% |
| LOAD_CONST | 852,786 | 14.5% |
| STORE_FAST | 750,857 | 12.8% |
| SWAP | 341,731 | 5.8% |
| RETURN_VALUE | 163,043 | 2.8% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 912,756 | 91.9% |
| LOAD_CONST | 62,538 | 6.3% |
| LOAD_FAST | 17,723 | 1.8% |
| POP_JUMP_IF_FALSE | 304 | 0.0% |
| STORE_SUBSCR | 4 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 912,756 | 91.9% |
| STORE_FAST | 38,754 | 3.9% |
| CALL_PY_EXACT_ARGS | 23,578 | 2.4% |
| BINARY_OP | 9,108 | 0.9% |
| LOAD_CONST | 9,083 | 0.9% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,398 | 100.0% |
| LOAD_FAST | 1 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 8,638 | 91.9% |
| BINARY_SUBSCR | 761 | 8.1% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 509,856 | 67.4% |
| LOAD_CONST | 246,114 | 32.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 247,088 | 32.7% |
| RETURN_VALUE | 194,190 | 25.7% |
| LOAD_FAST | 90,261 | 11.9% |
| CALL | 48,361 | 6.4% |
| CALL_PY_EXACT_ARGS | 46,755 | 6.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,833,708 | 35.3% |
| LOAD_GLOBAL_MODULE | 2,799,638 | 16.9% |
| LOAD_ATTR_SLOT | 2,668,178 | 16.2% |
| LOAD_FAST_LOAD_FAST | 2,241,714 | 13.6% |
| LOAD_ATTR | 718,652 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,287,261 | 26.0% |
| CALL_BUILTIN_O | 2,970,737 | 18.0% |
| CALL_ISINSTANCE | 2,438,725 | 14.8% |
| LOAD_CONST | 2,115,170 | 12.8% |
| LOAD_FAST | 1,862,301 | 11.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,113,359 | 17.4% |
| BUILD_LIST | 5,699,937 | 16.3% |
| LOAD_FAST_LOAD_FAST | 4,851,499 | 13.8% |
| ENTER_EXECUTOR | 3,363,532 | 9.6% |
| LOAD_ATTR_SLOT | 2,432,051 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,699,958 | 39.1% |
| RETURN_VALUE | 7,730,119 | 22.1% |
| LIST_APPEND | 3,496,081 | 10.0% |
| RESUME_CHECK | 2,390,874 | 6.8% |
| TO_BOOL_BOOL | 1,890,410 | 5.4% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 2,095,903 | 49.9% |
| LOAD_FAST | 1,022,919 | 24.4% |
| MAP_ADD | 851,779 | 20.3% |
| LOAD_ATTR | 139,996 | 3.3% |
| CALL_INTRINSIC_1 | 74,728 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,099,070 | 50.0% |
| RETURN_GENERATOR | 1,269,530 | 30.2% |
| POP_TOP | 541,391 | 12.9% |
| STORE_FAST | 187,038 | 4.5% |
| RESUME_CHECK | 72,425 | 1.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 77,511 | 78.3% |
| RERAISE | 21,439 | 21.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 74,728 | 75.5% |
| RERAISE | 21,439 | 21.7% |
| BUILD_MAP | 2,783 | 2.8% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 38,340,134 | 97.8% |
| ENTER_EXECUTOR | 856,621 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 22,210,600 | 56.7% |
| UNPACK_SEQUENCE_LIST | 7,057,243 | 18.0% |
| RETURN_VALUE | 2,826,839 | 7.2% |
| MAKE_CELL | 2,554,672 | 6.5% |
| CALL_PY_EXACT_ARGS | 1,977,429 | 5.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,543,263 | 43.4% |
| LOAD_GLOBAL_MODULE | 4,458,760 | 20.3% |
| LOAD_CONST | 3,977,684 | 18.1% |
| LOAD_ATTR_MODULE | 1,394,996 | 6.4% |
| LOAD_FAST | 1,134,201 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 8,842,652 | 40.3% |
| POP_JUMP_IF_FALSE | 6,830,855 | 31.1% |
| RETURN_VALUE | 4,370,942 | 19.9% |
| POP_JUMP_IF_TRUE | 1,321,863 | 6.0% |
| EXTENDED_ARG | 440,735 | 2.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,800,919 | 49.4% |
| LOAD_FAST_LOAD_FAST | 8,703,482 | 18.1% |
| LOAD_ATTR_INSTANCE_VALUE | 4,090,489 | 8.5% |
| LOAD_ATTR_SLOT | 2,566,906 | 5.3% |
| BINARY_SUBSCR | 2,525,771 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40,603,641 | 84.3% |
| POP_JUMP_IF_TRUE | 5,617,944 | 11.7% |
| RETURN_VALUE | 1,510,616 | 3.1% |
| EXTENDED_ARG | 225,921 | 0.5% |
| COPY | 112,202 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,663 | 98.9% |
| RETURN_CONST | 320 | 0.9% |
| LOAD_GLOBAL_MODULE | 63 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 34,046 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 8,842,652 | 33.5% |
| LOAD_FAST | 3,197,414 | 12.1% |
| CALL_ISINSTANCE | 2,159,212 | 8.2% |
| SWAP | 1,842,972 | 7.0% |
| COMPARE_OP_STR | 1,594,643 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 20,112,137 | 76.1% |
| COMPARE_OP_INT | 1,840,244 | 7.0% |
| TO_BOOL_NONE | 926,182 | 3.5% |
| TO_BOOL_STR | 760,647 | 2.9% |
| TO_BOOL | 557,351 | 2.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 24,392,129 | 50.5% |
| CACHE | 22,250,568 | 46.0% |
| CALL | 1,078,537 | 2.2% |
| CALL_ALLOC_AND_ENTER_INIT | 242,993 | 0.5% |
| CALL_KW | 225,292 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 47,811,082 | 98.9% |
| RETURN_GENERATOR | 508,193 | 1.1% |
| RESUME | 3,116 | 0.0% |
| MAKE_CELL | 4 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,013,389 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,650,411 | 77.3% |
| NOP | 1,269,530 | 21.1% |
| RETURN_CONST | 93,448 | 1.6% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 102,124 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 101,804 | 99.7% |
| JUMP_BACKWARD | 320 | 0.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,095,903 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 2,095,903 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 15,091,354 | 29.1% |
| LIST_APPEND | 12,550,646 | 24.2% |
| POP_TOP | 10,838,898 | 20.9% |
| CALL_LIST_APPEND | 5,197,273 | 10.0% |
| POP_JUMP_IF_FALSE | 1,457,411 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 22,130,102 | 42.7% |
| FOR_ITER_TUPLE | 4,204,231 | 8.1% |
| CALL | 3,363,532 | 6.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,889,283 | 5.6% |
| LOAD_ATTR_PROPERTY | 2,740,426 | 5.3% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 4,810,749 | 34.2% |
| GET_ITER | 2,455,575 | 17.5% |
| JUMP_BACKWARD | 817,003 | 5.8% |
| ENTER_EXECUTOR | 738,641 | 5.3% |
| LOAD_ATTR_SLOT | 643,689 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,199,591 | 51.3% |
| FOR_ITER | 2,204,946 | 15.7% |
| FOR_ITER_LIST | 1,649,534 | 11.7% |
| POP_JUMP_IF_NONE | 1,293,423 | 9.2% |
| JUMP_FORWARD | 646,763 | 4.6% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 7,747,205 | 62.0% |
| EXTENDED_ARG | 2,204,946 | 17.6% |
| JUMP_BACKWARD | 2,086,914 | 16.7% |
| SWAP | 379,063 | 3.0% |
| LOAD_FAST | 42,633 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 4,797,812 | 38.4% |
| RETURN_CONST | 2,348,987 | 18.8% |
| STORE_FAST | 2,117,162 | 16.9% |
| LOAD_FAST | 1,797,997 | 14.4% |
| LOAD_GLOBAL_BUILTIN | 471,175 | 3.8% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 949,104 | 75.3% |
| STORE_FAST | 310,467 | 24.6% |
| STORE_NAME | 938 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,259,105 | 99.9% |
| STORE_NAME | 1,404 | 0.1% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,020,745 | 98.9% |
| ENTER_EXECUTOR | 11,513 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 949,104 | 91.9% |
| STORE_FAST | 82,952 | 8.0% |
| STORE_DEREF | 160 | 0.0% |
| STORE_NAME | 42 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 21,603,930 | 73.2% |
| LOAD_CONST | 3,884,477 | 13.2% |
| LOAD_FAST | 3,478,830 | 11.8% |
| LOAD_FAST_LOAD_FAST | 445,099 | 1.5% |
| LOAD_ATTR | 48,650 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 19,910,184 | 67.4% |
| POP_JUMP_IF_TRUE | 5,755,872 | 19.5% |
| RETURN_VALUE | 2,255,165 | 7.6% |
| LOAD_FAST | 834,320 | 2.8% |
| COPY | 454,720 | 1.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,555,464 | 51.4% |
| STORE_SUBSCR | 1,506,818 | 17.0% |
| POP_JUMP_IF_TRUE | 890,682 | 10.1% |
| EXTENDED_ARG | 528,054 | 6.0% |
| FOR_ITER_LIST | 331,019 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,957,623 | 55.9% |
| FOR_ITER | 2,086,914 | 23.5% |
| EXTENDED_ARG | 817,003 | 9.2% |
| FOR_ITER_GEN | 639,619 | 7.2% |
| FOR_ITER_TUPLE | 277,965 | 3.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 194,905 | 96.2% |
| POP_EXCEPT | 7,326 | 3.6% |
| EXTENDED_ARG | 321 | 0.2% |
| RESUME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 194,925 | 96.2% |
| LOAD_FAST | 5,086 | 2.5% |
| NOP | 2,240 | 1.1% |
| LOAD_FAST_LOAD_FAST | 160 | 0.1% |
| LOAD_GLOBAL_MODULE | 121 | 0.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 6,965,313 | 26.3% |
| LOAD_ATTR_SLOT | 6,787,540 | 25.6% |
| STORE_ATTR_SLOT | 4,463,328 | 16.9% |
| LOAD_FAST | 3,480,877 | 13.1% |
| STORE_FAST | 1,927,690 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,276,937 | 53.9% |
| STORE_FAST | 7,299,514 | 27.6% |
| MAP_ADD | 3,306,772 | 12.5% |
| LOAD_CONST | 539,828 | 2.0% |
| LOAD_GLOBAL_MODULE | 534,090 | 2.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,662,711 | 59.6% |
| CALL | 3,496,081 | 27.2% |
| LOAD_FAST | 803,300 | 6.3% |
| BINARY_SUBSCR_LIST_INT | 175,664 | 1.4% |
| LOAD_ATTR_SLOT | 174,692 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,550,646 | 97.7% |
| JUMP_BACKWARD | 297,822 | 2.3% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,190 | 81.3% |
| RETURN_VALUE | 9,556 | 12.3% |
| BINARY_SLICE | 4,525 | 5.8% |
| LOAD_CONST | 163 | 0.2% |
| STORE_FAST | 162 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 77,511 | 99.8% |
| LOAD_CONST | 162 | 0.2% |
| LOAD_FAST | 2 | 0.0% |
| LOAD_GLOBAL | 2 | 0.0% |
| LOAD_GLOBAL_MODULE | 1 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,774,389 | 66.4% |
| LOAD_GLOBAL_MODULE | 15,717,788 | 25.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,359,465 | 2.2% |
| LOAD_FAST_LOAD_FAST | 1,070,516 | 1.7% |
| CALL_TYPE_1 | 813,952 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,875,990 | 45.4% |
| LOAD_FAST_LOAD_FAST | 5,741,479 | 9.3% |
| TO_BOOL | 4,778,267 | 7.8% |
| PUSH_NULL | 4,462,005 | 7.3% |
| CALL_PY_EXACT_ARGS | 3,763,785 | 6.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 85,947,139 | 24.1% |
| LOAD_FAST | 79,217,769 | 22.2% |
| LOAD_CONST | 27,534,514 | 7.7% |
| MAP_ADD | 14,493,043 | 4.1% |
| LOAD_ATTR_INSTANCE_VALUE | 14,173,933 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 142,959,317 | 40.1% |
| BINARY_SUBSCR_DICT | 50,240,772 | 14.1% |
| CALL_KW | 38,340,134 | 10.8% |
| LOAD_CONST | 27,534,514 | 7.7% |
| COMPARE_OP_STR | 17,188,088 | 4.8% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 47,199,082 | 70.7% |
| LOAD_DEREF | 6,819,072 | 10.2% |
| LOAD_FAST | 2,862,791 | 4.3% |
| LOAD_GLOBAL_MODULE | 2,641,920 | 4.0% |
| POP_JUMP_IF_FALSE | 1,361,259 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,132,257 | 67.6% |
| LOAD_DEREF | 6,819,072 | 10.2% |
| LOAD_ATTR_SLOT | 4,041,018 | 6.1% |
| LOAD_CONST | 2,250,909 | 3.4% |
| LOAD_FAST_LOAD_FAST | 1,911,219 | 2.9% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 195,711,860 | 13.0% |
| RESUME_CHECK | 157,072,160 | 10.4% |
| LOAD_CONST | 142,959,317 | 9.5% |
| POP_JUMP_IF_FALSE | 129,779,428 | 8.6% |
| STORE_FAST | 125,424,558 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 228,592,275 | 15.2% |
| STORE_ATTR_SLOT | 182,562,786 | 12.1% |
| LOAD_GLOBAL_MODULE | 139,269,109 | 9.2% |
| LOAD_ATTR_METHOD_NO_DICT | 97,995,489 | 6.5% |
| CALL_PY_EXACT_ARGS | 84,538,052 | 5.6% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 13,508,899 | 95.3% |
| LOAD_FAST_AND_CLEAR | 665,650 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 13,502,949 | 95.3% |
| LOAD_FAST_AND_CLEAR | 665,650 | 4.7% |
| MAKE_CELL | 5,950 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,120,981 | 75.2% |
| POP_JUMP_IF_FALSE | 168,267 | 11.3% |
| LOAD_GLOBAL_BUILTIN | 150,588 | 10.1% |
| POP_JUMP_IF_TRUE | 15,458 | 1.0% |
| LOAD_FAST_CHECK | 11,058 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 1,043,933 | 70.0% |
| LOAD_ATTR_SLOT | 103,583 | 6.9% |
| EXTENDED_ARG | 91,168 | 6.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 79,278 | 5.3% |
| TO_BOOL_BOOL | 57,539 | 3.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 71,978,497 | 24.9% |
| LOAD_SUPER_ATTR_METHOD | 36,632,755 | 12.7% |
| RESUME_CHECK | 31,135,597 | 10.8% |
| LOAD_GLOBAL_MODULE | 23,505,189 | 8.1% |
| STORE_FAST | 21,175,267 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 126,804,581 | 43.8% |
| CALL_PY_EXACT_ARGS | 52,663,174 | 18.2% |
| STORE_ATTR_INSTANCE_VALUE | 23,154,134 | 8.0% |
| LOAD_FAST | 20,013,462 | 6.9% |
| CONTAINS_OP | 8,703,482 | 3.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,205 | 18.8% |
| POP_JUMP_IF_FALSE | 45,286 | 18.4% |
| STORE_FAST | 38,673 | 15.7% |
| RESUME_CHECK | 12,563 | 5.1% |
| RESUME | 12,483 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 76,355 | 31.0% |
| LOAD_FAST | 53,430 | 21.7% |
| LOAD_GLOBAL_BUILTIN | 46,662 | 19.0% |
| CALL | 27,155 | 11.0% |
| LOAD_ATTR | 11,719 | 4.8% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,187 | 51.9% |
| LOAD_NAME | 634 | 27.7% |
| STORE_NAME | 217 | 9.5% |
| STORE_SUBSCR | 101 | 4.4% |
| RESUME | 46 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 658 | 28.8% |
| LOAD_NAME | 634 | 27.7% |
| BUILD_TUPLE | 399 | 17.4% |
| BINARY_SUBSCR | 327 | 14.3% |
| GET_ITER | 80 | 3.5% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,859 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 2,417 | 49.7% |
| CALL | 1,052 | 21.7% |
| LOAD_FAST | 687 | 14.1% |
| LOAD_FAST_LOAD_FAST | 422 | 8.7% |
| LOAD_GLOBAL | 181 | 3.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 11,497,470 | 65.8% |
| CALL_PY_EXACT_ARGS | 2,599,976 | 14.9% |
| CALL_KW | 2,554,672 | 14.6% |
| BINARY_SUBSCR_GETITEM | 470,336 | 2.7% |
| CALL_PY_WITH_DEFAULTS | 317,625 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 11,497,470 | 65.8% |
| RESUME_CHECK | 5,968,879 | 34.2% |
| SWAP | 5,950 | 0.0% |
| RESUME | 1,652 | 0.0% |
| RETURN_GENERATOR | 1,282 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 11,180,803 | 71.5% |
| JUMP_FORWARD | 3,306,772 | 21.1% |
| CALL_BUILTIN_CLASS | 853,657 | 5.5% |
| LOAD_FAST | 134,245 | 0.9% |
| RETURN_VALUE | 85,497 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 14,493,043 | 92.7% |
| CALL_FUNCTION_EX | 851,779 | 5.4% |
| ENTER_EXECUTOR | 285,255 | 1.8% |
| JUMP_BACKWARD | 4,322 | 0.0% |
| LOAD_FAST | 800 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 144,128,880 | 51.6% |
| CONTAINS_OP | 40,603,641 | 14.5% |
| IS_OP | 19,910,184 | 7.1% |
| TO_BOOL_ALWAYS_TRUE | 12,921,967 | 4.6% |
| TO_BOOL_NONE | 11,955,584 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 129,779,428 | 46.5% |
| LOAD_GLOBAL_BUILTIN | 68,273,496 | 24.5% |
| LOAD_GLOBAL_MODULE | 23,696,877 | 8.5% |
| LOAD_FAST_LOAD_FAST | 14,356,354 | 5.1% |
| POP_TOP | 10,848,152 | 3.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,129,632 | 49.2% |
| LOAD_ATTR_SLOT | 15,531,402 | 37.9% |
| LOAD_ATTR | 1,872,927 | 4.6% |
| EXTENDED_ARG | 1,293,423 | 3.2% |
| BINARY_SUBSCR_DICT | 1,039,661 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,630,003 | 48.0% |
| RETURN_CONST | 7,999,961 | 19.5% |
| JUMP_FORWARD | 6,965,313 | 17.0% |
| LOAD_CONST | 2,341,972 | 5.7% |
| LOAD_GLOBAL_BUILTIN | 1,738,070 | 4.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 43,282,848 | 87.5% |
| LOAD_ATTR_SLOT | 2,594,527 | 5.2% |
| BINARY_SUBSCR_DICT | 1,962,874 | 4.0% |
| LOAD_FAST_CHECK | 1,043,933 | 2.1% |
| BINARY_SUBSCR | 159,706 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 19,012,170 | 38.4% |
| LOAD_FAST | 10,436,837 | 21.1% |
| LOAD_CONST | 6,945,575 | 14.0% |
| LOAD_FAST_LOAD_FAST | 5,590,446 | 11.3% |
| RETURN_CONST | 2,442,644 | 4.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 52,675,692 | 46.2% |
| TO_BOOL_LIST | 17,377,962 | 15.3% |
| COMPARE_OP_STR | 15,231,662 | 13.4% |
| COMPARE_OP_INT | 6,040,510 | 5.3% |
| IS_OP | 5,755,872 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,391,278 | 44.2% |
| ENTER_EXECUTOR | 15,091,354 | 13.2% |
| LOAD_GLOBAL_MODULE | 12,640,469 | 11.1% |
| POP_TOP | 9,021,369 | 7.9% |
| NOP | 7,002,534 | 6.1% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 101,804 | 59.1% |
| RETURN_VALUE | 38,192 | 22.2% |
| CALL | 25,849 | 15.0% |
| LOAD_CONST | 6,080 | 3.5% |
| POP_TOP | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 101,804 | 59.1% |
| PUSH_EXC_INFO | 64,113 | 37.2% |
| COPY | 6,338 | 3.7% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 129,581 | 47.2% |
| DELETE_FAST | 101,804 | 37.1% |
| CALL_INTRINSIC_1 | 21,439 | 7.8% |
| POP_JUMP_IF_FALSE | 21,439 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 123,243 | 48.8% |
| PUSH_EXC_INFO | 107,982 | 42.7% |
| CALL_INTRINSIC_1 | 21,439 | 8.5% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 61,637,187 | 39.8% |
| RESUME_CHECK | 34,608,807 | 22.4% |
| POP_TOP | 12,107,454 | 7.8% |
| POP_JUMP_IF_FALSE | 9,499,597 | 6.1% |
| POP_JUMP_IF_NONE | 7,999,961 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 54,483,196 | 35.2% |
| INTERPRETER_EXIT | 33,314,195 | 21.5% |
| LOAD_FAST | 31,492,766 | 20.3% |
| RETURN_VALUE | 21,917,808 | 14.2% |
| TO_BOOL_BOOL | 6,097,823 | 3.9% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 66.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 50.0% |
| SEND_GEN | 60 | 50.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 665,424 | 91.6% |
| LOAD_ATTR_INSTANCE_VALUE | 32,556 | 4.5% |
| STORE_FAST_LOAD_FAST | 20,614 | 2.8% |
| LOAD_FAST | 3,836 | 0.5% |
| RETURN_VALUE | 3,288 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 719,139 | 99.0% |
| JUMP_BACKWARD | 7,599 | 1.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,114,370 | 77.7% |
| SET_FUNCTION_ATTRIBUTE | 606,064 | 22.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 910,461 | 33.5% |
| SET_FUNCTION_ATTRIBUTE | 606,064 | 22.3% |
| STORE_FAST | 531,130 | 19.5% |
| LOAD_FAST | 244,754 | 9.0% |
| STORE_DEREF | 220,264 | 8.1% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 308 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 304 | 98.7% |
| STORE_NAME | 4 | 1.3% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,450,502 | 81.2% |
| LOAD_FAST | 1,170,620 | 17.4% |
| SWAP | 60,980 | 0.9% |
| STORE_ATTR | 20,839 | 0.3% |
| LOAD_ATTR_SLOT | 5,041 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,723,191 | 40.6% |
| RETURN_CONST | 2,257,255 | 33.6% |
| LOAD_FAST | 1,342,831 | 20.0% |
| LOAD_CONST | 145,935 | 2.2% |
| LOAD_GLOBAL_MODULE | 137,439 | 2.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,044,022 | 82.4% |
| SET_FUNCTION_ATTRIBUTE | 220,264 | 8.9% |
| RETURN_VALUE | 83,202 | 3.4% |
| LOAD_ATTR_SLOT | 52,702 | 2.1% |
| FOR_ITER_LIST | 22,863 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,539,957 | 62.1% |
| LOAD_FAST | 592,694 | 23.9% |
| LOAD_GLOBAL_BUILTIN | 139,224 | 5.6% |
| LOAD_CONST | 97,183 | 3.9% |
| LOAD_DEREF | 91,531 | 3.7% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 46,520,276 | 18.3% |
| FOR_ITER_LIST | 29,615,758 | 11.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 26,186,044 | 10.3% |
| LOAD_ATTR_SLOT | 22,949,322 | 9.0% |
| BUILD_LIST | 16,677,119 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,424,558 | 49.3% |
| LOAD_GLOBAL_BUILTIN | 37,328,207 | 14.7% |
| LOAD_GLOBAL_MODULE | 29,903,460 | 11.7% |
| LOAD_FAST_LOAD_FAST | 21,175,267 | 8.3% |
| LOAD_CONST | 9,737,714 | 3.8% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 2,811,605 | 70.2% |
| FOR_ITER_TUPLE | 925,324 | 23.1% |
| FOR_ITER_RANGE | 174,875 | 4.4% |
| FOR_ITER | 91,740 | 2.3% |
| CALL_LEN | 1,020 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,552,315 | 38.8% |
| LOAD_CONST | 895,759 | 22.4% |
| LOAD_ATTR_INSTANCE_VALUE | 670,608 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 308,794 | 7.7% |
| LOAD_FAST | 222,322 | 5.6% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_LIST | 7,189,963 | 49.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,124,859 | 41.7% |
| UNPACK_SEQUENCE_TUPLE | 886,770 | 6.0% |
| COPY | 318,193 | 2.2% |
| BINARY_SUBSCR_LIST_INT | 51,193 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,390,679 | 77.6% |
| LOAD_FAST_LOAD_FAST | 1,193,938 | 8.1% |
| STORE_FAST | 961,628 | 6.5% |
| LOAD_GLOBAL_BUILTIN | 690,247 | 4.7% |
| LOAD_GLOBAL_MODULE | 184,397 | 1.3% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,404 | 57.2% |
| SET_FUNCTION_ATTRIBUTE | 608 | 24.8% |
| LOAD_CONST | 138 | 5.6% |
| CALL | 88 | 3.6% |
| BUILD_STRING | 60 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 938 | 38.2% |
| LOAD_CONST | 676 | 27.5% |
| POP_TOP | 466 | 19.0% |
| LOAD_NAME | 217 | 8.8% |
| RETURN_CONST | 68 | 2.8% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 13,502,949 | 30.2% |
| BUILD_LIST | 12,254,412 | 27.4% |
| FOR_ITER_LIST | 9,005,885 | 20.1% |
| LOAD_FAST | 2,603,938 | 5.8% |
| CALL_LEN | 1,836,322 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 12,254,412 | 27.4% |
| FOR_ITER_LIST | 11,329,591 | 25.3% |
| STORE_FAST | 10,868,432 | 24.3% |
| COPY | 1,842,972 | 4.1% |
| POP_TOP | 1,830,446 | 4.1% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 486 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 486 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 50,489 | 62.9% |
| COPY | 13,286 | 16.6% |
| FOR_ITER_LIST | 4,624 | 5.8% |
| FOR_ITER | 4,606 | 5.7% |
| RETURN_VALUE | 3,711 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 54,912 | 68.4% |
| STORE_FAST_STORE_FAST | 19,140 | 23.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,167 | 5.2% |
| UNPACK_SEQUENCE_TUPLE | 988 | 1.2% |
| UNPACK_SEQUENCE | 743 | 0.9% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,296,770 | 21.5% |
| LOAD_CONST | 1,057,308 | 17.6% |
| ENTER_EXECUTOR | 951,205 | 15.8% |
| LOAD_FAST | 575,178 | 9.5% |
| CALL_ISINSTANCE | 421,529 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 5,168,032 | 85.8% |
| STORE_FAST | 449,243 | 7.5% |
| UNPACK_SEQUENCE_TUPLE | 211,755 | 3.5% |
| YIELD_VALUE | 194,965 | 3.2% |
| UNPACK_SEQUENCE | 60 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20,048 | 48.5% |
| CALL_PY_EXACT_ARGS | 5,617 | 13.6% |
| CACHE | 5,549 | 13.4% |
| COPY_FREE_VARS | 3,116 | 7.5% |
| POP_TOP | 2,447 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,579 | 47.4% |
| LOAD_GLOBAL | 12,483 | 30.2% |
| LOAD_FAST_LOAD_FAST | 2,068 | 5.0% |
| LOAD_CONST | 1,964 | 4.8% |
| POP_TOP | 1,851 | 4.5% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 118,433 | 82.7% |
| ENTER_EXECUTOR | 24,477 | 17.1% |
| BINARY_OP_ADD_INT | 379 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 142,930 | 99.7% |
| BINARY_OP_ADD_INT | 359 | 0.3% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,125,643 | 55.9% |
| CALL_LEN | 776,362 | 20.4% |
| CALL_METHOD_DESCRIPTOR_O | 734,533 | 19.3% |
| LOAD_FAST_LOAD_FAST | 80,325 | 2.1% |
| LOAD_FAST | 79,408 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,620,356 | 42.6% |
| LOAD_FAST | 993,536 | 26.1% |
| SWAP | 526,226 | 13.8% |
| LOAD_FAST_LOAD_FAST | 307,782 | 8.1% |
| LOAD_CONST | 116,250 | 3.1% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,073,125 | 36.6% |
| LOAD_FAST | 575,711 | 19.6% |
| LOAD_FAST_LOAD_FAST | 492,263 | 16.8% |
| CALL_METHOD_DESCRIPTOR_O | 492,250 | 16.8% |
| LOAD_ATTR | 207,168 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 837,243 | 28.6% |
| RETURN_VALUE | 721,487 | 24.6% |
| SET_ADD | 665,424 | 22.7% |
| STORE_FAST | 383,584 | 13.1% |
| BINARY_OP_INPLACE_ADD_UNICODE | 166,373 | 5.7% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 888 | 97.8% |
| BINARY_OP | 20 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 888 | 97.8% |
| CALL | 20 | 2.2% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,788 | 80.4% |
| BINARY_SUBSCR_TUPLE_INT | 640 | 18.5% |
| LOAD_FAST | 34 | 1.0% |
| BINARY_OP | 6 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,240 | 64.6% |
| BINARY_OP_ADD_INT | 672 | 19.4% |
| SWAP | 190 | 5.5% |
| LOAD_CONST | 180 | 5.2% |
| CALL_BUILTIN_O | 180 | 5.2% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 90,132 | 61.3% |
| LOAD_FAST_LOAD_FAST | 56,286 | 38.3% |
| BINARY_OP | 380 | 0.3% |
| LOAD_ATTR_WITH_HINT | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 118,355 | 80.6% |
| LOAD_FAST_LOAD_FAST | 28,083 | 19.1% |
| LOAD_GLOBAL_BUILTIN | 240 | 0.2% |
| LOAD_FAST | 140 | 0.1% |
| BINARY_OP | 60 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,843,427 | 93.6% |
| LOAD_FAST | 62,758 | 3.2% |
| CALL_LEN | 55,894 | 2.8% |
| LOAD_FAST_LOAD_FAST | 3,874 | 0.2% |
| LOAD_ATTR_SLOT | 2,072 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 968,791 | 49.2% |
| BINARY_SLICE | 445,059 | 22.6% |
| SWAP | 170,319 | 8.6% |
| STORE_FAST | 144,967 | 7.4% |
| BINARY_SUBSCR_LIST_INT | 142,394 | 7.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 50,240,772 | 86.0% |
| LOAD_FAST | 4,420,013 | 7.6% |
| BINARY_SUBSCR_DICT | 1,508,028 | 2.6% |
| BINARY_SUBSCR_LIST_INT | 954,508 | 1.6% |
| LOAD_DEREF | 786,017 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,859,095 | 18.6% |
| STORE_FAST | 9,921,064 | 17.0% |
| LOAD_CONST | 9,890,654 | 16.9% |
| GET_ITER | 6,203,361 | 10.6% |
| CALL_PY_EXACT_ARGS | 4,730,476 | 8.1% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 767,185 | 54.7% |
| ENTER_EXECUTOR | 424,620 | 30.3% |
| LOAD_FAST_LOAD_FAST | 202,525 | 14.4% |
| LOAD_CONST | 6,880 | 0.5% |
| LOAD_FAST | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 931,023 | 66.4% |
| MAKE_CELL | 470,336 | 33.6% |
| LOAD_ATTR_SLOT | 332 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,450,298 | 45.8% |
| LOAD_FAST | 2,782,339 | 28.6% |
| LOAD_FAST_LOAD_FAST | 2,288,576 | 23.6% |
| BINARY_OP_SUBTRACT_INT | 142,394 | 1.5% |
| BINARY_OP_ADD_INT | 24,698 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,428,221 | 14.7% |
| LOAD_FAST | 1,304,351 | 13.4% |
| LOAD_GLOBAL_MODULE | 1,243,120 | 12.8% |
| BINARY_SUBSCR_DICT | 954,508 | 9.8% |
| CALL_PY_EXACT_ARGS | 757,556 | 7.8% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 417,553 | 82.0% |
| BINARY_OP_ADD_INT | 59,570 | 11.7% |
| BINARY_OP_SUBTRACT_INT | 18,408 | 3.6% |
| LOAD_FAST_LOAD_FAST | 11,790 | 2.3% |
| LOAD_FAST | 1,700 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 361,479 | 71.0% |
| LOAD_FAST | 70,100 | 13.8% |
| CALL_BUILTIN_O | 33,916 | 6.7% |
| LOAD_FAST_LOAD_FAST | 16,928 | 3.3% |
| COMPARE_OP_STR | 16,888 | 3.3% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 878,560 | 99.5% |
| LOAD_FAST_LOAD_FAST | 2,531 | 0.3% |
| BINARY_SUBSCR | 1,466 | 0.2% |
| ENTER_EXECUTOR | 3 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 170,106 | 19.3% |
| FORMAT_SIMPLE | 149,308 | 16.9% |
| LOAD_FAST_LOAD_FAST | 105,487 | 12.0% |
| STORE_FAST | 105,189 | 11.9% |
| CALL | 78,432 | 8.9% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 949,007 | 40.9% |
| LOAD_FAST_LOAD_FAST | 446,717 | 19.3% |
| LOAD_GLOBAL_MODULE | 356,318 | 15.4% |
| CALL | 224,823 | 9.7% |
| RETURN_VALUE | 188,669 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,071,487 | 89.3% |
| COPY_FREE_VARS | 242,993 | 10.5% |
| CALL_PY_EXACT_ARGS | 3,423 | 0.1% |
| STORE_FAST | 1,317 | 0.1% |
| MAKE_CELL | 212 | 0.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,073,860 | 62.5% |
| BINARY_SUBSCR_DICT | 3,205,953 | 22.1% |
| LOAD_CONST | 1,482,633 | 10.2% |
| ENTER_EXECUTOR | 464,879 | 3.2% |
| RETURN_VALUE | 140,068 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,992,916 | 89.5% |
| POP_TOP | 1,447,347 | 10.0% |
| CALL_PY_EXACT_ARGS | 50,709 | 0.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 27,232 | 0.2% |
| RESUME | 988 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,105,192 | 28.9% |
| LOAD_GLOBAL_BUILTIN | 3,832,610 | 18.2% |
| LOAD_ATTR_SLOT | 2,389,778 | 11.3% |
| LOAD_ATTR_CLASS | 1,992,158 | 9.4% |
| CALL_LEN | 1,590,644 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,996,895 | 47.4% |
| LOAD_FAST | 5,509,852 | 26.1% |
| STORE_FAST | 2,018,919 | 9.6% |
| RETURN_VALUE | 1,320,502 | 6.3% |
| MAP_ADD | 853,657 | 4.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,136,302 | 47.7% |
| LOAD_ATTR_INSTANCE_VALUE | 2,587,020 | 39.3% |
| LOAD_FAST_LOAD_FAST | 651,083 | 9.9% |
| LOAD_FAST | 101,799 | 1.5% |
| LOAD_GLOBAL_BUILTIN | 46,087 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,611,986 | 24.5% |
| RETURN_VALUE | 1,291,410 | 19.6% |
| PUSH_EXC_INFO | 1,271,890 | 19.3% |
| POP_TOP | 815,866 | 12.4% |
| TO_BOOL_BOOL | 749,503 | 11.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,627,663 | 82.6% |
| RETURN_GENERATOR | 213,583 | 10.8% |
| CALL_BUILTIN_CLASS | 78,520 | 4.0% |
| RETURN_VALUE | 24,313 | 1.2% |
| LOAD_CONST | 13,500 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,339,937 | 68.0% |
| COPY | 173,345 | 8.8% |
| LOAD_CONST | 158,983 | 8.1% |
| RETURN_VALUE | 93,373 | 4.7% |
| PUSH_EXC_INFO | 89,628 | 4.6% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 2,970,737 | 35.7% |
| RETURN_GENERATOR | 2,474,402 | 29.7% |
| LOAD_FAST | 1,183,668 | 14.2% |
| LOAD_GLOBAL_MODULE | 623,910 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 337,401 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,660,877 | 44.0% |
| LOAD_FAST | 2,568,591 | 30.8% |
| TO_BOOL_BOOL | 894,470 | 10.7% |
| CALL_PY_EXACT_ARGS | 520,761 | 6.3% |
| STORE_FAST | 240,500 | 2.9% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120,296,078 | 84.9% |
| LOAD_GLOBAL_BUILTIN | 17,368,531 | 12.3% |
| BUILD_TUPLE | 2,438,725 | 1.7% |
| LOAD_ATTR | 998,943 | 0.7% |
| LOAD_ATTR_MODULE | 494,926 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 138,520,624 | 97.7% |
| COPY | 2,159,212 | 1.5% |
| YIELD_VALUE | 421,529 | 0.3% |
| RETURN_VALUE | 393,671 | 0.3% |
| STORE_FAST | 211,579 | 0.1% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,444,252 | 56.5% |
| LOAD_ATTR_SLOT | 5,837,951 | 31.6% |
| LOAD_ATTR_INSTANCE_VALUE | 983,024 | 5.3% |
| LOAD_DEREF | 950,323 | 5.1% |
| LOAD_ATTR | 110,360 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,032,639 | 27.2% |
| COMPARE_OP_INT | 3,049,208 | 16.5% |
| LOAD_GLOBAL_BUILTIN | 2,376,049 | 12.9% |
| SWAP | 1,836,322 | 9.9% |
| CALL_BUILTIN_CLASS | 1,590,644 | 8.6% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,558,251 | 75.5% |
| RETURN_VALUE | 1,433,392 | 8.6% |
| ENTER_EXECUTOR | 999,821 | 6.0% |
| LOAD_CONST | 320,604 | 1.9% |
| BUILD_TUPLE | 296,966 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,864,498 | 53.3% |
| ENTER_EXECUTOR | 5,197,273 | 31.2% |
| NOP | 1,287,793 | 7.7% |
| LOAD_CONST | 371,586 | 2.2% |
| LOAD_GLOBAL_BUILTIN | 258,684 | 1.6% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,708,858 | 52.9% |
| LOAD_ATTR_METHOD_NO_DICT | 10,277,610 | 30.7% |
| LOAD_CONST | 1,416,907 | 4.2% |
| RETURN_VALUE | 1,202,926 | 3.6% |
| ENTER_EXECUTOR | 992,161 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 26,186,044 | 78.2% |
| POP_TOP | 4,099,657 | 12.2% |
| LOAD_FAST | 1,349,671 | 4.0% |
| CALL_PY_EXACT_ARGS | 456,980 | 1.4% |
| LOAD_ATTR_METHOD_NO_DICT | 322,476 | 1.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,287,726 | 89.0% |
| LOAD_FAST | 93,704 | 6.5% |
| LOAD_ATTR_MODULE | 51,436 | 3.6% |
| LOAD_ATTR_METHOD_NO_DICT | 13,713 | 0.9% |
| CALL | 688 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,102,048 | 76.1% |
| LOAD_CONST | 128,883 | 8.9% |
| GET_ITER | 94,266 | 6.5% |
| CONTAINS_OP | 51,456 | 3.6% |
| RETURN_VALUE | 46,691 | 3.2% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,546,496 | 97.9% |
| ENTER_EXECUTOR | 25,506 | 1.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,231 | 0.2% |
| LOAD_ATTR | 2,832 | 0.2% |
| CALL | 1,549 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 895,086 | 56.7% |
| LOAD_FAST | 291,812 | 18.5% |
| POP_TOP | 179,652 | 11.4% |
| CALL_BUILTIN_CLASS | 120,580 | 7.6% |
| LOAD_ATTR_METHOD_NO_DICT | 49,852 | 3.2% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,306,331 | 54.6% |
| LOAD_FAST | 1,919,894 | 31.7% |
| RETURN_VALUE | 330,817 | 5.5% |
| BUILD_TUPLE | 124,997 | 2.1% |
| LOAD_ATTR_SLOT | 120,678 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,585,796 | 42.7% |
| POP_TOP | 2,112,738 | 34.9% |
| BINARY_OP_ADD_INT | 734,533 | 12.1% |
| BINARY_OP_ADD_UNICODE | 492,250 | 8.1% |
| STORE_FAST | 87,429 | 1.4% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 84,538,052 | 37.4% |
| LOAD_FAST_LOAD_FAST | 52,663,174 | 23.3% |
| LOAD_ATTR_METHOD_NO_DICT | 38,144,869 | 16.9% |
| LOAD_ATTR_SLOT | 7,794,079 | 3.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,058,629 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 196,073,583 | 86.8% |
| COPY_FREE_VARS | 24,392,129 | 10.8% |
| MAKE_CELL | 2,599,976 | 1.2% |
| RETURN_GENERATOR | 2,313,820 | 1.0% |
| CALL_PY_EXACT_ARGS | 371,703 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 4,039,549 | 37.4% |
| LOAD_FAST | 3,559,374 | 33.0% |
| LOAD_FAST_LOAD_FAST | 961,563 | 8.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 606,251 | 5.6% |
| LOAD_ATTR_SLOT | 333,555 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,346,622 | 95.8% |
| MAKE_CELL | 317,625 | 2.9% |
| COPY_FREE_VARS | 132,626 | 1.2% |
| CALL_PY_EXACT_ARGS | 4,261 | 0.0% |
| RETURN_GENERATOR | 676 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 610,399 | 100.0% |
| UNARY_NOT | 120 | 0.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 491,775 | 80.5% |
| CALL_BUILTIN_O | 93,733 | 15.3% |
| STORE_FAST | 17,162 | 2.8% |
| CALL | 7,766 | 1.3% |
| BUILD_TUPLE | 140 | 0.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,598,996 | 92.3% |
| LOAD_ATTR_SLOT | 764,806 | 7.4% |
| RETURN_VALUE | 11,773 | 0.1% |
| RETURN_GENERATOR | 11,272 | 0.1% |
| LOAD_FAST_CHECK | 9,787 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,675,548 | 93.1% |
| LOAD_GLOBAL_BUILTIN | 396,106 | 3.8% |
| BUILD_TUPLE | 279,433 | 2.7% |
| CALL_PY_EXACT_ARGS | 17,017 | 0.2% |
| RETURN_VALUE | 14,559 | 0.1% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,665,019 | 100.0% |
| LOAD_CONST | 309 | 0.0% |
| CALL | 200 | 0.0% |
| LOAD_GLOBAL_MODULE | 63 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,453,447 | 61.0% |
| LOAD_ATTR | 813,952 | 14.4% |
| STORE_FAST | 804,863 | 14.2% |
| PUSH_NULL | 445,122 | 7.9% |
| LOAD_GLOBAL_MODULE | 61,244 | 1.1% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 440 | 84.1% |
| LOAD_ATTR_INSTANCE_VALUE | 63 | 12.0% |
| COMPARE_OP | 20 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 460 | 88.0% |
| POP_JUMP_IF_FALSE | 63 | 12.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,903,272 | 40.1% |
| CALL_LEN | 3,049,208 | 15.5% |
| LOAD_GLOBAL_MODULE | 1,871,807 | 9.5% |
| LOAD_ATTR_CLASS | 1,854,072 | 9.4% |
| COPY | 1,840,244 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 11,360,753 | 57.7% |
| POP_JUMP_IF_TRUE | 6,040,510 | 30.7% |
| COPY | 1,077,191 | 5.5% |
| RETURN_VALUE | 688,397 | 3.5% |
| EXTENDED_ARG | 328,229 | 1.7% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,188,088 | 72.6% |
| LOAD_FAST | 4,761,049 | 20.1% |
| RETURN_VALUE | 479,180 | 2.0% |
| LOAD_ATTR_MODULE | 328,990 | 1.4% |
| LOAD_ATTR | 233,906 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 15,231,662 | 64.3% |
| POP_JUMP_IF_FALSE | 5,729,066 | 24.2% |
| COPY | 1,594,643 | 6.7% |
| RETURN_VALUE | 641,343 | 2.7% |
| EXTENDED_ARG | 425,189 | 1.8% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 639,619 | 92.9% |
| GET_ITER | 48,590 | 7.1% |
| FOR_ITER | 102 | 0.0% |
| LOAD_FAST | 46 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 639,639 | 92.9% |
| POP_TOP | 48,636 | 7.1% |
| RESUME | 82 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 23,107,631 | 35.1% |
| ENTER_EXECUTOR | 22,130,102 | 33.6% |
| SWAP | 11,329,591 | 17.2% |
| JUMP_BACKWARD | 4,957,623 | 7.5% |
| LOAD_FAST | 2,695,526 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 29,615,758 | 44.9% |
| LOAD_FAST | 13,879,062 | 21.1% |
| SWAP | 9,005,885 | 13.7% |
| RETURN_CONST | 7,578,395 | 11.5% |
| STORE_FAST_LOAD_FAST | 2,811,605 | 4.3% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,078,048 | 62.8% |
| ENTER_EXECUTOR | 1,230,103 | 25.1% |
| SWAP | 410,573 | 8.4% |
| EXTENDED_ARG | 120,972 | 2.5% |
| JUMP_BACKWARD | 64,470 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,500,677 | 30.6% |
| RETURN_CONST | 1,422,333 | 29.0% |
| LOAD_FAST | 1,160,439 | 23.7% |
| LOAD_GLOBAL_MODULE | 435,860 | 8.9% |
| STORE_FAST_LOAD_FAST | 174,875 | 3.6% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 9,567,778 | 61.7% |
| ENTER_EXECUTOR | 4,204,231 | 27.1% |
| SWAP | 1,389,672 | 9.0% |
| JUMP_BACKWARD | 277,965 | 1.8% |
| EXTENDED_ARG | 35,046 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,830,626 | 57.0% |
| STORE_FAST | 3,371,684 | 21.7% |
| SWAP | 1,380,001 | 8.9% |
| STORE_FAST_LOAD_FAST | 925,324 | 6.0% |
| LOAD_FAST_LOAD_FAST | 539,601 | 3.5% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,903,990 | 89.3% |
| LOAD_FAST | 771,931 | 10.0% |
| COPY | 32,099 | 0.4% |
| ENTER_EXECUTOR | 19,740 | 0.3% |
| LOAD_ATTR_CLASS | 2,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 1,992,158 | 25.8% |
| COMPARE_OP_INT | 1,854,072 | 24.0% |
| LOAD_ATTR_METHOD_NO_DICT | 1,416,899 | 18.3% |
| CALL | 1,357,606 | 17.6% |
| LOAD_ATTR_MODULE | 771,931 | 10.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,087,561 | 80.4% |
| LOAD_FAST_LOAD_FAST | 6,561,361 | 8.2% |
| LOAD_ATTR_INSTANCE_VALUE | 3,021,556 | 3.8% |
| LOAD_GLOBAL_MODULE | 2,187,083 | 2.7% |
| LOAD_DEREF | 941,514 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,716,245 | 18.5% |
| LOAD_CONST | 14,173,933 | 17.8% |
| LOAD_ATTR_METHOD_NO_DICT | 7,426,034 | 9.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,943,577 | 8.7% |
| CONTAINS_OP | 4,090,489 | 5.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,400 | 99.8% |
| LOAD_ATTR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,300 | 99.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 120 | 0.7% |
| CALL | 20 | 0.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,995,489 | 72.8% |
| LOAD_ATTR_SLOT | 13,766,100 | 10.2% |
| LOAD_ATTR_INSTANCE_VALUE | 7,426,034 | 5.5% |
| LOAD_GLOBAL_MODULE | 4,982,018 | 3.7% |
| ENTER_EXECUTOR | 2,889,283 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,854,405 | 44.5% |
| CALL_PY_EXACT_ARGS | 38,144,869 | 28.3% |
| LOAD_CONST | 12,507,181 | 9.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 10,277,610 | 7.6% |
| LOAD_GLOBAL_MODULE | 9,648,423 | 7.2% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,371,870 | 81.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,943,577 | 11.7% |
| LOAD_DEREF | 1,305,451 | 2.2% |
| LOAD_ATTR_WITH_HINT | 775,400 | 1.3% |
| LOAD_FAST_LOAD_FAST | 682,112 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,272,623 | 69.5% |
| LOAD_FAST_LOAD_FAST | 8,304,228 | 14.0% |
| CALL_PY_EXACT_ARGS | 6,058,629 | 10.2% |
| LOAD_CONST | 1,415,011 | 2.4% |
| LOAD_DEREF | 1,123,920 | 1.9% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,151,647 | 67.0% |
| LOAD_ATTR_MODULE | 2,983,485 | 21.8% |
| LOAD_ATTR_CLASS | 771,931 | 5.6% |
| LOAD_FAST_LOAD_FAST | 638,814 | 4.7% |
| LOAD_FAST | 107,985 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,983,485 | 21.8% |
| PUSH_NULL | 2,965,904 | 21.7% |
| LOAD_FAST | 2,132,913 | 15.6% |
| COMPARE_OP | 1,394,996 | 10.2% |
| LOAD_GLOBAL_MODULE | 803,895 | 5.9% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 534,715 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 491,775 | 92.0% |
| LOAD_FAST | 21,601 | 4.0% |
| IS_OP | 21,419 | 4.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 358,324 | 65.5% |
| LOAD_FAST | 184,105 | 33.7% |
| LOAD_FAST_LOAD_FAST | 1,777 | 0.3% |
| BINARY_SUBSCR_DICT | 931 | 0.2% |
| ENTER_EXECUTOR | 855 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 359,364 | 65.7% |
| CALL_LEN | 69,691 | 12.7% |
| LOAD_FAST | 48,430 | 8.9% |
| RETURN_VALUE | 45,448 | 8.3% |
| POP_JUMP_IF_NONE | 19,061 | 3.5% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,076,994 | 54.4% |
| LOAD_ATTR_SLOT | 3,570,671 | 24.1% |
| ENTER_EXECUTOR | 2,740,426 | 18.5% |
| LOAD_ATTR_INSTANCE_VALUE | 268,000 | 1.8% |
| LOAD_FAST_LOAD_FAST | 46,922 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 13,827,536 | 93.1% |
| RETURN_VALUE | 594,646 | 4.0% |
| STORE_FAST | 138,469 | 0.9% |
| LOAD_FAST | 136,330 | 0.9% |
| LOAD_CONST | 59,528 | 0.4% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 228,592,275 | 88.2% |
| LOAD_ATTR_SLOT | 17,949,098 | 6.9% |
| LOAD_DEREF | 4,041,018 | 1.6% |
| LOAD_FAST_LOAD_FAST | 3,468,696 | 1.3% |
| STORE_FAST_LOAD_FAST | 1,552,315 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,713,585 | 12.2% |
| GET_ITER | 24,354,758 | 9.4% |
| STORE_FAST | 22,949,322 | 8.9% |
| RETURN_VALUE | 19,344,808 | 7.5% |
| LOAD_ATTR_SLOT | 17,949,098 | 6.9% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,956,019 | 57.9% |
| LOAD_FAST_LOAD_FAST | 3,606,890 | 21.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,289,479 | 19.1% |
| LOAD_ATTR_WITH_HINT | 270,355 | 1.6% |
| ENTER_EXECUTOR | 41,038 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,411,876 | 31.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,086,074 | 12.1% |
| TO_BOOL_BOOL | 1,910,892 | 11.1% |
| COPY | 1,476,678 | 8.6% |
| LOAD_FAST | 1,390,903 | 8.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 86,527,028 | 30.8% |
| POP_JUMP_IF_FALSE | 68,273,496 | 24.3% |
| STORE_FAST | 37,328,207 | 13.3% |
| LOAD_FAST | 19,642,343 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 19,012,170 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 195,711,860 | 69.7% |
| LOAD_DEREF | 47,199,082 | 16.8% |
| CALL_ISINSTANCE | 17,368,531 | 6.2% |
| CALL_BUILTIN_CLASS | 3,832,610 | 1.4% |
| LOAD_CONST | 3,396,552 | 1.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,269,109 | 44.3% |
| STORE_FAST | 29,903,460 | 9.5% |
| RESUME_CHECK | 27,426,946 | 8.7% |
| POP_JUMP_IF_FALSE | 23,696,877 | 7.5% |
| LOAD_GLOBAL_MODULE | 17,008,629 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 120,296,078 | 38.3% |
| LOAD_FAST | 59,454,080 | 18.9% |
| LOAD_FAST_LOAD_FAST | 23,505,189 | 7.5% |
| IS_OP | 21,603,930 | 6.9% |
| LOAD_GLOBAL_MODULE | 17,008,629 | 5.4% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 541,451 | 100.0% |
| LOAD_SUPER_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 538,631 | 99.5% |
| STORE_FAST | 2,880 | 0.5% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,074,352 | 100.0% |
| LOAD_SUPER_ATTR | 2,417 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 36,632,755 | 83.1% |
| CALL_PY_WITH_DEFAULTS | 4,039,549 | 9.2% |
| CALL_PY_EXACT_ARGS | 1,647,966 | 3.7% |
| LOAD_FAST | 1,135,376 | 2.6% |
| LOAD_GLOBAL_MODULE | 384,362 | 0.9% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 196,073,583 | 54.8% |
| COPY_FREE_VARS | 47,811,082 | 13.4% |
| CACHE | 37,843,962 | 10.6% |
| CALL_KW | 22,210,600 | 6.2% |
| LOAD_ATTR_PROPERTY | 13,827,536 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 157,072,160 | 43.9% |
| LOAD_GLOBAL_BUILTIN | 86,527,028 | 24.2% |
| RETURN_CONST | 34,608,807 | 9.7% |
| LOAD_FAST_LOAD_FAST | 31,135,597 | 8.7% |
| LOAD_GLOBAL_MODULE | 27,426,946 | 7.7% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 194,925 | 79.5% |
| LOAD_CONST | 50,275 | 20.5% |
| SEND | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 194,925 | 79.5% |
| POP_TOP | 50,295 | 20.5% |
| RESUME | 40 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 23,154,134 | 55.7% |
| LOAD_FAST | 17,702,571 | 42.6% |
| SWAP | 447,609 | 1.1% |
| BINARY_SUBSCR | 239,985 | 0.6% |
| STORE_ATTR_INSTANCE_VALUE | 16,253 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 19,670,528 | 47.3% |
| LOAD_FAST | 7,154,120 | 17.2% |
| RETURN_CONST | 6,733,885 | 16.2% |
| LOAD_GLOBAL_BUILTIN | 2,831,502 | 6.8% |
| LOAD_GLOBAL_MODULE | 1,929,039 | 4.6% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 182,562,786 | 58.7% |
| LOAD_FAST_LOAD_FAST | 126,804,581 | 40.8% |
| STORE_ATTR_SLOT | 1,271,721 | 0.4% |
| LOAD_ATTR_SLOT | 476,175 | 0.2% |
| STORE_ATTR | 12,794 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 85,947,139 | 27.6% |
| LOAD_FAST_LOAD_FAST | 71,978,497 | 23.1% |
| RETURN_CONST | 61,637,187 | 19.8% |
| LOAD_FAST | 56,003,317 | 18.0% |
| LOAD_GLOBAL_BUILTIN | 16,184,493 | 5.2% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 523,886 | 56.5% |
| LOAD_FAST_LOAD_FAST | 400,492 | 43.2% |
| SWAP | 1,614 | 0.2% |
| STORE_ATTR | 597 | 0.1% |
| STORE_ATTR_WITH_HINT | 301 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 291,220 | 31.4% |
| LOAD_GLOBAL_MODULE | 249,500 | 26.9% |
| RETURN_CONST | 199,525 | 21.5% |
| LOAD_FAST | 142,132 | 15.3% |
| LOAD_GLOBAL_BUILTIN | 43,516 | 4.7% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,871,529 | 75.1% |
| LOAD_FAST_LOAD_FAST | 191,975 | 7.7% |
| LOAD_ATTR_SLOT | 187,831 | 7.5% |
| SWAP | 166,508 | 6.7% |
| LOAD_CONST | 22,878 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,297,447 | 52.0% |
| ENTER_EXECUTOR | 582,495 | 23.4% |
| LOAD_FAST | 487,605 | 19.6% |
| LOAD_GLOBAL_BUILTIN | 44,542 | 1.8% |
| LOAD_DEREF | 31,618 | 1.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 223,600 | 99.6% |
| LOAD_FAST | 804 | 0.4% |
| STORE_SUBSCR | 82 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 222,338 | 99.0% |
| ENTER_EXECUTOR | 846 | 0.4% |
| LOAD_FAST | 684 | 0.3% |
| RETURN_CONST | 320 | 0.1% |
| EXTENDED_ARG | 298 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,092,746 | 73.9% |
| LOAD_ATTR_SLOT | 2,961,820 | 19.7% |
| LOAD_ATTR_INSTANCE_VALUE | 294,526 | 2.0% |
| ENTER_EXECUTOR | 247,031 | 1.6% |
| LOAD_ATTR | 120,584 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,921,967 | 86.1% |
| POP_JUMP_IF_TRUE | 1,531,132 | 10.2% |
| EXTENDED_ARG | 513,146 | 3.4% |
| TO_BOOL_NONE | 19,034 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 16,833 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 138,520,624 | 64.9% |
| COPY | 20,112,137 | 9.4% |
| LOAD_FAST | 17,608,080 | 8.3% |
| RETURN_VALUE | 13,419,081 | 6.3% |
| LOAD_ATTR_SLOT | 6,291,005 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 144,128,880 | 67.6% |
| POP_JUMP_IF_TRUE | 52,675,692 | 24.7% |
| UNARY_NOT | 11,668,046 | 5.5% |
| EXTENDED_ARG | 4,810,749 | 2.3% |
| TO_BOOL_STR | 333 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 622,159 | 61.8% |
| LOAD_ATTR_INSTANCE_VALUE | 199,998 | 19.9% |
| RETURN_VALUE | 76,126 | 7.6% |
| LOAD_ATTR_SLOT | 72,815 | 7.2% |
| BINARY_OP | 28,403 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 717,322 | 71.3% |
| POP_JUMP_IF_TRUE | 214,651 | 21.3% |
| UNARY_NOT | 73,215 | 7.3% |
| TO_BOOL_STR | 662 | 0.1% |
| TO_BOOL_BOOL | 163 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,402,843 | 74.9% |
| LOAD_ATTR_SLOT | 3,451,772 | 14.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,350,410 | 5.8% |
| COPY | 486,765 | 2.1% |
| BINARY_SUBSCR_LIST_INT | 201,918 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 17,377,962 | 74.8% |
| POP_JUMP_IF_FALSE | 4,116,372 | 17.7% |
| UNARY_NOT | 1,328,485 | 5.7% |
| EXTENDED_ARG | 415,925 | 1.8% |
| TO_BOOL | 2,215 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,586,992 | 62.9% |
| LOAD_ATTR_SLOT | 4,223,953 | 25.1% |
| COPY | 926,182 | 5.5% |
| LOAD_ATTR_INSTANCE_VALUE | 325,410 | 1.9% |
| LOAD_ATTR_MODULE | 266,665 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 11,955,584 | 71.1% |
| POP_JUMP_IF_TRUE | 4,449,081 | 26.4% |
| EXTENDED_ARG | 381,172 | 2.3% |
| TO_BOOL_ALWAYS_TRUE | 19,398 | 0.1% |
| UNARY_NOT | 12,848 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,378,060 | 72.2% |
| COPY | 760,647 | 16.3% |
| LOAD_ATTR_SLOT | 237,304 | 5.1% |
| LOAD_ATTR_INSTANCE_VALUE | 186,312 | 4.0% |
| STORE_FAST_LOAD_FAST | 94,350 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,729,080 | 58.4% |
| POP_JUMP_IF_TRUE | 1,747,333 | 37.4% |
| UNARY_NOT | 195,538 | 4.2% |
| TO_BOOL_NONE | 2,558 | 0.1% |
| TO_BOOL_INT | 803 | 0.0% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_KW | 7,057,243 | 98.1% |
| RETURN_VALUE | 118,538 | 1.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 8,160 | 0.1% |
| LOAD_FAST | 7,967 | 0.1% |
| LOAD_ATTR_SLOT | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 7,189,963 | 100.0% |
| STORE_FAST | 2,907 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 401,037 | 38.1% |
| YIELD_VALUE | 211,755 | 20.1% |
| STORE_FAST | 151,430 | 14.4% |
| FOR_ITER | 122,857 | 11.7% |
| FOR_ITER_LIST | 83,994 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 886,770 | 84.2% |
| LOAD_FAST | 93,412 | 8.9% |
| STORE_FAST | 72,657 | 6.9% |
| STORE_DEREF | 41 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 4,797,812 | 72.6% |
| RETURN_VALUE | 763,652 | 11.6% |
| FOR_ITER_LIST | 533,812 | 8.1% |
| RETURN_CONST | 169,609 | 2.6% |
| STORE_FAST | 152,894 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 6,124,859 | 92.7% |
| STORE_FAST | 466,434 | 7.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 18,037 | 0.3% |
| STORE_FAST_LOAD_FAST | 71 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_CONST_KEY_MAP | 800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 800 | 100.0% |


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
|     deferred | 2,492,712 | 15.8% |
|          hit | 13,309,915 | 84.1% |
|         miss | 39,525 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,864 | 32.6% |
| Failure | 12,150 | 67.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 5,670 | 46.7% |
| multiply different types | 2,969 | 24.4% |
| or | 1,057 | 8.7% |
| remainder | 861 | 7.1% |
| subtract other | 774 | 6.4% |
| and int | 340 | 2.8% |
| and different types | 159 | 1.3% |
| subtract different types | 140 | 1.2% |
| true divide different types | 120 | 1.0% |
| and other | 40 | 0.3% |
| add different types | 20 | 0.2% |


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
|     deferred | 21,157,589 | 20.0% |
|          hit | 84,653,336 | 80.0% |
|         miss | 1,284 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 12,401 | 35.9% |
| Failure | 22,159 | 64.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 13,541 | 61.1% |
| other | 4,719 | 21.3% |
| code complex parameters | 3,636 | 16.4% |
| buffer int | 203 | 0.9% |
| tuple slice | 60 | 0.3% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 65,531,178 | 10.9% |
|          hit | 536,425,750 | 89.0% |
|         miss | 31,285,538 | 5.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 704,443 | 88.6% |
| Failure | 90,927 | 11.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| no dict | 32,016 | 35.2% |
| code complex parameters | 23,461 | 25.8% |
| meth descr varargs | 7,898 | 8.7% |
| class no vectorcall | 7,778 | 8.6% |
| cfunc noargs | 4,539 | 5.0% |
| class mutable | 3,160 | 3.5% |
| cfunc varargs keywords | 2,174 | 2.4% |
| metaclass | 2,146 | 2.4% |
| meth descr varargs keywords | 1,314 | 1.4% |
| wrong number arguments | 1,154 | 1.3% |
| init not simple | 1,118 | 1.2% |
| meth descr method fastcall keywords | 1,035 | 1.1% |
| bound method | 942 | 1.0% |
| other | 799 | 0.9% |
| init not python | 486 | 0.5% |
| cfunc varargs | 447 | 0.5% |
| cmethod | 360 | 0.4% |
| operator wrapper | 100 | 0.1% |
| out of versions | 60 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 22,416,948 | 30.7% |
|          hit | 50,481,096 | 69.2% |
|         miss | 527,717 | 0.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 23,083 | 29.7% |
| Failure | 54,720 | 70.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 28,537 | 52.2% |
| baseobject | 10,841 | 19.8% |
| other | 4,952 | 9.0% |
| different types | 3,680 | 6.7% |
| tuple | 2,256 | 4.1% |
| bool | 2,118 | 3.9% |
| list | 1,813 | 3.3% |
| set | 283 | 0.5% |
| string | 240 | 0.4% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 14,557,469 | 14.6% |
|          hit | 84,854,194 | 85.3% |
|         miss | 2,145,586 | 2.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 52,888 | 64.6% |
| Failure | 29,011 | 35.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 7,210 | 24.9% |
| zip | 5,734 | 19.8% |
| set | 5,589 | 19.3% |
| dict items | 3,971 | 13.7% |
| reversed list | 3,085 | 10.6% |
| dict keys | 1,759 | 6.1% |
| dict values | 870 | 3.0% |
| itertools | 571 | 2.0% |
| map | 140 | 0.5% |
| other | 80 | 0.3% |
| callable | 2 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 105,368,520 | 15.6% |
|        deopt | 989 | 0.0% |
|          hit | 568,813,659 | 84.2% |
|         miss | 45,112,441 | 6.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,007,545 | 85.9% |
| Failure | 165,381 | 14.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 78,697 | 47.6% |
| not managed dict | 32,659 | 19.7% |
| shadowed | 21,817 | 13.2% |
| class method obj | 6,505 | 3.9% |
| non overriding descriptor | 6,276 | 3.8% |
| metaclass attribute | 6,020 | 3.6% |
| method | 4,770 | 2.9% |
| class attr simple | 3,618 | 2.2% |
| module attr not found | 2,562 | 1.5% |
| out of versions | 1,919 | 1.2% |
| builtin class method | 317 | 0.2% |
| class attr descriptor | 120 | 0.1% |
| mutable class | 101 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 128,030 | 0.0% |
|        deopt | 862 | 0.0% |
|          hit | 595,038,845 | 100.0% |
|         miss | 4,912 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 123,097 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,382 | 0.0% |
|          hit | 44,618,280 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,477 | 100.0% |
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
|     deferred | 60 | 0.0% |
|          hit | 245,260 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 73,708,715 | 20.4% |
|          hit | 285,600,003 | 79.2% |
|         miss | 68,330,407 | 18.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,311,481 | 98.4% |
| Failure | 20,935 | 1.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 14,259 | 68.1% |
| not in dict | 4,745 | 22.7% |
| not in keys | 721 | 3.4% |
| overridden | 612 | 2.9% |
| out of versions | 596 | 2.8% |
| not managed dict | 2 | 0.0% |


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
|     deferred | 1,920,280 | 39.2% |
|          hit | 2,970,364 | 60.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,525 | 45.7% |
| Failure | 1,810 | 54.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict subclass no override | 1,222 | 67.5% |
| out of range | 588 | 32.5% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 14,273,429 | 4.8% |
|          hit | 285,120,533 | 95.2% |
|         miss | 3,857,593 | 1.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 132,702 | 78.5% |
| Failure | 36,290 | 21.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 17,639 | 48.6% |
| tuple | 10,379 | 28.6% |
| dict | 3,930 | 10.8% |
| set | 1,804 | 5.0% |
| other | 1,306 | 3.6% |
| mapping | 1,232 | 3.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 74,093 | 0.4% |
|          hit | 18,689,353 | 99.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,437 | 88.3% |
| Failure | 723 | 11.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 542 | 75.0% |
| iterator | 181 | 25.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 3,669,285,277 | 50.3% |
| Not specialized | 660,701,898 | 9.1% |
| Specialized hits | 2,817,153,440 | 38.6% |
| Specialized misses | 151,305,026 | 2.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 105,368,520 | 32.8% |
| STORE_ATTR | 73,708,715 | 22.9% |
| CALL | 65,531,178 | 20.4% |
| COMPARE_OP | 22,416,948 | 7.0% |
| BINARY_SUBSCR | 21,157,589 | 6.6% |
| FOR_ITER | 14,557,469 | 4.5% |
| TO_BOOL | 14,273,429 | 4.4% |
| BINARY_OP | 2,492,712 | 0.8% |
| STORE_SUBSCR | 1,920,280 | 0.6% |
| LOAD_GLOBAL | 128,030 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 67,421,878 | 44.6% |
| LOAD_ATTR_METHOD_NO_DICT | 29,320,281 | 19.4% |
| CALL_PY_EXACT_ARGS | 22,964,248 | 15.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 7,677,871 | 5.1% |
| LOAD_ATTR_SLOT | 4,411,326 | 2.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,164,490 | 2.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,987,977 | 2.0% |
| LOAD_ATTR_INSTANCE_VALUE | 2,163,395 | 1.4% |
| TO_BOOL_ALWAYS_TRUE | 2,013,875 | 1.3% |
| TO_BOOL_NONE | 1,426,651 | 0.9% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 64,210,879 | 17.4% |
| Calls to Python functions inlined | 304,481,051 | 82.6% |
| Calls via PyEval_EvalFrame (total) | 64,210,879 | 17.4% |
| Calls via PyEval_EvalFrame (vector) | 56,416,958 | 15.3% |
| Calls via PyEval_EvalFrame (generator) | 7,793,921 | 2.1% |
| Calls via PyEval_EvalFrame (legacy) | 104 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 56,416,808 | 15.3% |
| Calls via PyEval_EvalFrame (build class) | 46 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 7,175,981 | 1.9% |
| Calls via PyEval_EvalFrame (function ex) | 1,368,748 | 0.4% |
| Calls via PyEval_EvalFrame (api) | 12,470,983 | 3.4% |
| Calls via PyEval_EvalFrame (method) | 102 | 0.0% |
| Frame objects created | 2,520,693 | 0.7% |
| Frames pushed | 362,279,024 | 98.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 160,497,593 | 28.9% |
| Frees to freelist | 160,543,979 |  |
| Allocations | 395,064,850 | 71.1% |
| Allocations to 512 bytes | 394,513,354 | 71.0% |
| Allocations to 4 kbytes | 384,909 | 0.1% |
| Allocations over 4 kbytes | 166,587 | 0.0% |
| Frees | 389,865,862 |  |
| New values | 5,939,802 |  |
| Interpreter increfs | 3,595,035,602 | 70.3% |
| Interpreter decrefs | 4,014,495,279 | 72.3% |
| Increfs | 1,518,760,364 | 29.7% |
| Decrefs | 1,538,534,687 | 27.7% |
| Materialize dict (on request) | 345 | 0.0% |
| Materialize dict (new key) | 1,815 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 220 | 0.0% |
| Method cache hits | 214,737,598 |  |
| Method cache misses | 9,398,610 |  |
| Method cache collisions | 5,556,737 |  |
| Method cache dunder hits | 184,691,770 |  |
| Method cache dunder misses | 2,874,350 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 180 | 230,767 | 431,689,752 |
| 1 | 20 | 10,527,177 | 223,180,540 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 29,884 |  |
| Traces created | 28,699 | 96.0% |
| Trace stack overflow | 160 | 0.5% |
| Trace stack underflow | 79 | 0.3% |
| Trace too long | 1 | 0.0% |
| Trace too short | 1,185 | 4.0% |
| Inner loop found | 592 | 2.0% |
| Recursive call | 1,547 | 5.2% |
| Low confidence | 495 | 1.7% |
| Traces executed | 0 |  |
| Uops executed | 0 |  |

### Trace length histogram

<details>
<summary> trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 20 | 0.1% |
| <= 16 | 1,315 | 4.6% |
| <= 32 | 12,761 | 44.5% |
| <= 64 | 8,405 | 29.3% |
| <= 128 | 4,001 | 13.9% |
| <= 256 | 1,734 | 6.0% |
| <= 512 | 463 | 1.6% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 20 | 0.1% |
| <= 8 | 529 | 1.8% |
| <= 16 | 3,931 | 13.7% |
| <= 32 | 3,486 | 12.1% |
| <= 64 | 2,530 | 8.8% |
| <= 128 | 1,725 | 6.0% |
| <= 256 | 497 | 1.7% |
| <= 512 | 141 | 0.5% |


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

|Opcode | Count | 
|---|---:|
| CALL | 1,795 |
| CALL_LIST_APPEND | 1,223 |
| FOR_ITER_GEN | 1,185 |
| CALL_PY_WITH_DEFAULTS | 833 |
| CALL_KW | 808 |
| LOAD_ATTR_PROPERTY | 799 |
| YIELD_VALUE | 770 |
| CALL_ALLOC_AND_ENTER_INIT | 444 |
| IMPORT_NAME | 20 |
| BINARY_SUBSCR_GETITEM | 20 |
| RETURN_GENERATOR | 19 |


</details>


</details>

## Rare events

<details>
<summary> Counts of rare/unlikely events </summary>

|Event | Count | 
|---|---:|
| set class | 0 |
| set bases | 41 |
| set eval frame func | 0 |
| builtin dict | 0 |
| func modification | 41 |
| watched dict modification | 0 |
| watched globals modification | 0 |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
