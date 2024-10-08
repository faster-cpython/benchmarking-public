
# Pystats results

- benchmark: concurrent_imap
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 102,198,820 | 17.7% | 17.7% |  |
| RESUME_CHECK | 37,549,273 | 6.5% | 24.2% | 0.0% |
| STORE_FAST | 29,842,318 | 5.2% | 29.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 24,724,074 | 4.3% | 33.6% | 0.9% |
| POP_TOP | 24,300,898 | 4.2% | 37.8% |  |
| RETURN_VALUE | 22,297,961 | 3.9% | 41.7% |  |
| POP_JUMP_IF_FALSE | 19,506,761 | 3.4% | 45.0% |  |
| JUMP_BACKWARD | 18,064,855 | 3.1% | 48.2% |  |
| LOAD_GLOBAL_MODULE | 17,293,658 | 3.0% | 51.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 15,906,684 | 2.8% | 53.9% |  |
| LOAD_CONST | 15,595,517 | 2.7% | 56.6% |  |
| CALL_PY_EXACT_ARGS | 12,703,533 | 2.2% | 58.8% | 0.0% |
| INTERPRETER_EXIT | 11,955,972 | 2.1% | 60.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,311,260 | 2.0% | 62.8% | 0.7% |
| CALL | 11,063,372 | 1.9% | 64.7% |  |
| LOAD_ATTR | 10,528,790 | 1.8% | 66.5% |  |
| NOP | 10,122,383 | 1.8% | 68.3% |  |
| FOR_ITER_LIST | 10,079,888 | 1.7% | 70.0% |  |
| RETURN_CONST | 9,413,424 | 1.6% | 71.7% |  |
| LOAD_GLOBAL_BUILTIN | 8,854,785 | 1.5% | 73.2% | 0.0% |
| PUSH_NULL | 7,393,343 | 1.3% | 74.5% |  |
| COPY | 7,308,574 | 1.3% | 75.7% |  |
| BINARY_OP | 7,214,949 | 1.2% | 77.0% |  |
| TO_BOOL_BOOL | 7,102,739 | 1.2% | 78.2% |  |
| YIELD_VALUE | 6,913,660 | 1.2% | 79.4% |  |
| LOAD_ATTR_METHOD_NO_DICT | 6,481,902 | 1.1% | 80.5% |  |
| STORE_FAST_LOAD_FAST | 6,464,820 | 1.1% | 81.7% |  |
| FOR_ITER_GEN | 6,347,440 | 1.1% | 82.7% |  |
| TO_BOOL_INT | 5,332,436 | 0.9% | 83.7% |  |
| POP_JUMP_IF_NOT_NONE | 5,133,007 | 0.9% | 84.6% |  |
| STORE_FAST_STORE_FAST | 4,850,961 | 0.8% | 85.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 4,480,566 | 0.8% | 86.2% | 5.5% |
| BUILD_TUPLE | 4,324,988 | 0.7% | 86.9% |  |
| COMPARE_OP_INT | 3,779,863 | 0.7% | 87.6% | 0.2% |
| LOAD_ATTR_MODULE | 3,657,274 | 0.6% | 88.2% | 0.0% |
| CALL_PY_WITH_DEFAULTS | 2,979,131 | 0.5% | 88.7% |  |
| POP_JUMP_IF_TRUE | 2,762,741 | 0.5% | 89.2% |  |
| SWAP | 2,661,922 | 0.5% | 89.7% |  |
| GET_ITER | 2,421,268 | 0.4% | 90.1% |  |
| CALL_FUNCTION_EX | 2,413,972 | 0.4% | 90.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,163,681 | 0.4% | 90.9% |  |
| CALL_BUILTIN_CLASS | 2,045,534 | 0.4% | 91.2% |  |
| LOAD_DEREF | 1,873,206 | 0.3% | 91.5% |  |
| BEFORE_WITH | 1,864,258 | 0.3% | 91.9% |  |
| CALL_BUILTIN_FAST | 1,858,105 | 0.3% | 92.2% |  |
| COPY_FREE_VARS | 1,823,146 | 0.3% | 92.5% |  |
| CONTAINS_OP | 1,780,300 | 0.3% | 92.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,763,556 | 0.3% | 93.1% |  |
| LOAD_SUPER_ATTR_METHOD | 1,726,826 | 0.3% | 93.4% |  |
| UNARY_INVERT | 1,722,896 | 0.3% | 93.7% |  |
| JUMP_FORWARD | 1,722,174 | 0.3% | 94.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,713,494 | 0.3% | 94.3% | 0.0% |
| BUILD_MAP | 1,684,326 | 0.3% | 94.6% |  |
| TO_BOOL | 1,594,446 | 0.3% | 94.9% |  |
| BUILD_LIST | 1,549,964 | 0.3% | 95.1% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,511,494 | 0.3% | 95.4% |  |
| COMPARE_OP_STR | 1,489,114 | 0.3% | 95.7% |  |
| FOR_ITER | 1,305,260 | 0.2% | 95.9% |  |
| STORE_SUBSCR_DICT | 1,293,608 | 0.2% | 96.1% |  |
| CALL_ISINSTANCE | 1,221,040 | 0.2% | 96.3% |  |
| UNPACK_SEQUENCE_TUPLE | 1,169,544 | 0.2% | 96.5% |  |
| POP_JUMP_IF_NONE | 1,146,834 | 0.2% | 96.7% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,137,984 | 0.2% | 96.9% | 0.0% |
| BINARY_OP_ADD_INT | 1,112,441 | 0.2% | 97.1% |  |
| EXIT_INIT_CHECK | 1,075,632 | 0.2% | 97.3% |  |
| CALL_ALLOC_AND_ENTER_INIT | 1,075,632 | 0.2% | 97.5% |  |
| LOAD_ATTR_PROPERTY | 1,053,901 | 0.2% | 97.7% | 1.2% |
| CALL_METHOD_DESCRIPTOR_O | 969,969 | 0.2% | 97.8% | 0.0% |
| LIST_APPEND | 840,804 | 0.1% | 98.0% |  |
| LOAD_FAST_CHECK | 837,230 | 0.1% | 98.1% |  |
| FOR_ITER_RANGE | 782,724 | 0.1% | 98.3% |  |
| LOAD_FAST_AND_CLEAR | 777,880 | 0.1% | 98.4% |  |
| BINARY_SUBSCR | 637,859 | 0.1% | 98.5% |  |
| CALL_LEN | 633,579 | 0.1% | 98.6% |  |
| COMPARE_OP | 594,930 | 0.1% | 98.7% |  |
| CALL_TUPLE_1 | 583,120 | 0.1% | 98.8% |  |
| DICT_MERGE | 564,260 | 0.1% | 98.9% |  |
| TO_BOOL_LIST | 558,246 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_LIST_INT | 498,008 | 0.1% | 99.1% |  |
| LIST_EXTEND | 487,888 | 0.1% | 99.2% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 409,116 | 0.1% | 99.3% |  |
| CALL_KW | 360,029 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_INT | 331,188 | 0.1% | 99.4% |  |
| CALL_LIST_APPEND | 271,748 | 0.0% | 99.4% |  |
| BINARY_OP_ADD_FLOAT | 260,502 | 0.0% | 99.5% |  |
| UNARY_NOT | 259,736 | 0.0% | 99.5% |  |
| BINARY_OP_SUBTRACT_FLOAT | 243,898 | 0.0% | 99.6% |  |
| TO_BOOL_NONE | 240,417 | 0.0% | 99.6% | 0.1% |
| CALL_BUILTIN_O | 154,400 | 0.0% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 142,392 | 0.0% | 99.6% | 4.5% |
| MAKE_CELL | 137,900 | 0.0% | 99.7% |  |
| STORE_DEREF | 137,660 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_DICT | 114,880 | 0.0% | 99.7% |  |
| BINARY_OP_MULTIPLY_FLOAT | 112,600 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_STR_INT | 112,600 | 0.0% | 99.8% |  |
| STORE_ATTR | 100,864 | 0.0% | 99.8% |  |
| LOAD_ATTR_SLOT | 99,760 | 0.0% | 99.8% |  |
| STORE_ATTR_SLOT | 97,980 | 0.0% | 99.8% |  |
| LOAD_ATTR_CLASS | 91,524 | 0.0% | 99.8% |  |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 0.0% | 99.8% |  |
| DELETE_ATTR | 86,400 | 0.0% | 99.8% |  |
| DELETE_SUBSCR | 78,220 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 63,680 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 55,680 | 0.0% | 99.9% |  |
| POP_EXCEPT | 50,000 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 50,000 | 0.0% | 99.9% |  |
| IS_OP | 46,957 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 44,240 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 43,340 | 0.0% | 99.9% |  |
| BUILD_STRING | 41,600 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 39,160 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 39,040 | 0.0% | 99.9% |  |
| IMPORT_NAME | 33,760 | 0.0% | 100.0% |  |
| IMPORT_FROM | 33,420 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 31,258 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 30,220 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 28,160 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 27,480 | 0.0% | 100.0% |  |
| BINARY_SLICE | 19,820 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 18,900 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 17,844 | 0.0% | 100.0% |  |
| RERAISE | 17,281 | 0.0% | 100.0% |  |
| CALL_STR_1 | 11,900 | 0.0% | 100.0% |  |
| END_FOR | 11,520 | 0.0% | 100.0% |  |
| STORE_NAME | 7,480 | 0.0% | 100.0% |  |
| RESUME | 5,980 | 0.0% | 100.0% | 0.0% |
| RAISE_VARARGS | 5,780 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 5,760 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 3,840 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 2,800 | 0.0% | 100.0% |  |
| LOAD_NAME | 2,200 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 1,440 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 920 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 917 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 280 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 160 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 140 | 0.0% | 100.0% | 14.3% |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 22,341,722 | 3.9% | 3.9% |
| RESUME_CHECK LOAD_FAST | 21,025,430 | 3.6% | 7.5% |
| STORE_FAST LOAD_FAST | 13,045,490 | 2.3% | 9.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 12,656,933 | 2.2% | 11.9% |
| CACHE RESUME_CHECK | 11,842,092 | 2.0% | 14.0% |
| LOAD_FAST RETURN_VALUE | 10,812,404 | 1.9% | 15.9% |
| RETURN_VALUE INTERPRETER_EXIT | 10,479,286 | 1.8% | 17.7% |
| POP_TOP JUMP_BACKWARD | 8,735,486 | 1.5% | 19.2% |
| LOAD_FAST LOAD_ATTR | 8,161,990 | 1.4% | 20.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 8,134,301 | 1.4% | 22.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,984,807 | 1.4% | 23.4% |
| JUMP_BACKWARD FOR_ITER_LIST | 7,984,624 | 1.4% | 24.8% |
| POP_TOP LOAD_FAST | 7,599,067 | 1.3% | 26.1% |
| RESUME_CHECK POP_TOP | 6,913,520 | 1.2% | 27.3% |
| RETURN_CONST POP_TOP | 6,649,724 | 1.1% | 28.4% |
| NOP LOAD_FAST | 6,424,422 | 1.1% | 29.5% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,335,920 | 1.1% | 30.6% |
| YIELD_VALUE STORE_FAST | 6,335,920 | 1.1% | 31.7% |
| FOR_ITER_GEN RESUME_CHECK | 6,335,920 | 1.1% | 32.8% |
| FOR_ITER_LIST STORE_FAST_LOAD_FAST | 5,760,060 | 1.0% | 33.8% |
| STORE_FAST JUMP_BACKWARD | 5,760,000 | 1.0% | 34.8% |
| STORE_FAST_LOAD_FAST YIELD_VALUE | 5,760,000 | 1.0% | 35.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 5,708,827 | 1.0% | 36.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 5,643,433 | 1.0% | 37.8% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 5,332,296 | 0.9% | 38.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,318,887 | 0.9% | 39.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 4,964,938 | 0.9% | 40.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 4,963,377 | 0.9% | 41.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 4,085,573 | 0.7% | 42.0% |
| LOAD_FAST LOAD_CONST | 3,997,093 | 0.7% | 42.7% |
| LOAD_GLOBAL_MODULE BINARY_OP | 3,869,088 | 0.7% | 43.4% |
| STORE_FAST NOP | 3,865,828 | 0.7% | 44.1% |
| LOAD_CONST LOAD_CONST | 3,839,401 | 0.7% | 44.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,776,085 | 0.7% | 45.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 3,740,181 | 0.6% | 46.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 3,708,856 | 0.6% | 46.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,707,746 | 0.6% | 47.3% |
| LOAD_FAST PUSH_NULL | 3,683,628 | 0.6% | 47.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,654,034 | 0.6% | 48.6% |
| LOAD_ATTR LOAD_FAST | 3,546,393 | 0.6% | 49.2% |
| PUSH_NULL LOAD_FAST | 3,494,477 | 0.6% | 49.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 3,458,958 | 0.6% | 50.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 3,179,529 | 0.5% | 50.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 3,158,581 | 0.5% | 51.5% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 3,099,338 | 0.5% | 52.0% |
| BINARY_OP COPY | 2,926,016 | 0.5% | 52.5% |
| COPY TO_BOOL_INT | 2,925,696 | 0.5% | 53.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 2,714,884 | 0.5% | 53.5% |
| CALL STORE_FAST | 2,665,107 | 0.5% | 54.0% |
| COPY STORE_FAST | 2,630,400 | 0.5% | 54.4% |
| STORE_FAST COPY | 2,629,760 | 0.5% | 54.9% |
| LOAD_CONST CALL | 2,615,036 | 0.5% | 55.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,554,415 | 0.4% | 55.8% |
| CALL RETURN_VALUE | 2,506,080 | 0.4% | 56.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,429,094 | 0.4% | 56.6% |
| RETURN_VALUE STORE_FAST | 2,330,365 | 0.4% | 57.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 2,298,622 | 0.4% | 57.4% |
| CALL POP_TOP | 2,263,277 | 0.4% | 57.8% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 2,228,224 | 0.4% | 58.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,187,468 | 0.4% | 58.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 2,156,621 | 0.4% | 59.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 2,080,544 | 0.4% | 59.3% |
| LOAD_CONST COMPARE_OP_INT | 2,071,535 | 0.4% | 59.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,062,546 | 0.4% | 60.0% |
| PUSH_NULL CALL | 2,044,185 | 0.4% | 60.4% |
| RETURN_VALUE RETURN_VALUE | 2,015,159 | 0.3% | 60.7% |
| LOAD_FAST_LOAD_FAST CALL | 1,943,558 | 0.3% | 61.1% |
| POP_TOP RETURN_CONST | 1,931,896 | 0.3% | 61.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 1,920,449 | 0.3% | 61.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,878,105 | 0.3% | 62.1% |
| LOAD_FAST CALL_FUNCTION_EX | 1,849,692 | 0.3% | 62.4% |
| NOP LOAD_GLOBAL_MODULE | 1,829,477 | 0.3% | 62.7% |
| COPY_FREE_VARS RESUME_CHECK | 1,822,486 | 0.3% | 63.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,819,920 | 0.3% | 63.3% |
| LOAD_DEREF LOAD_FAST | 1,816,866 | 0.3% | 63.6% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 1,816,346 | 0.3% | 64.0% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,779,680 | 0.3% | 64.3% |
| LOAD_ATTR_INSTANCE_VALUE CONTAINS_OP | 1,779,021 | 0.3% | 64.6% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 1,776,011 | 0.3% | 64.9% |
| LOAD_FAST BUILD_TUPLE | 1,770,000 | 0.3% | 65.2% |
| POP_TOP LOAD_CONST | 1,761,266 | 0.3% | 65.5% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,757,254 | 0.3% | 65.8% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 1,726,626 | 0.3% | 66.1% |
| UNARY_INVERT BINARY_OP | 1,722,896 | 0.3% | 66.4% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 1,706,806 | 0.3% | 66.7% |
| FOR_ITER_LIST STORE_FAST | 1,704,748 | 0.3% | 67.0% |
| LOAD_CONST LOAD_FAST | 1,696,007 | 0.3% | 67.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,608,056 | 0.3% | 67.5% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,606,774 | 0.3% | 67.8% |
| GET_ITER FOR_ITER_LIST | 1,591,932 | 0.3% | 68.1% |
| POP_TOP NOP | 1,589,572 | 0.3% | 68.4% |
| LOAD_FAST GET_ITER | 1,542,144 | 0.3% | 68.6% |
| LOAD_FAST TO_BOOL | 1,532,906 | 0.3% | 68.9% |
| RETURN_VALUE POP_TOP | 1,529,548 | 0.3% | 69.2% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,511,715 | 0.3% | 69.4% |
| POP_JUMP_IF_FALSE POP_TOP | 1,507,565 | 0.3% | 69.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,479,840 | 0.3% | 69.9% |
| BINARY_OP STORE_FAST | 1,477,428 | 0.3% | 70.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,451,971 | 0.3% | 70.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,450,084 | 0.3% | 70.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 18,520 | 93.4% |
| LOAD_CONST | 980 | 4.9% |
| LOAD_FAST | 280 | 1.4% |
| BINARY_OP | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,900 | 95.4% |
| BUILD_TUPLE | 280 | 1.4% |
| LOAD_DEREF | 280 | 1.4% |
| STORE_FAST | 280 | 1.4% |
| CALL | 80 | 0.4% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,842,092 | 99.0% |
| COPY_FREE_VARS | 109,900 | 0.9% |
| POP_TOP | 7,460 | 0.1% |
| RESUME | 2,280 | 0.0% |
| MAKE_CELL | 20 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,253,732 | 67.3% |
| RETURN_VALUE | 503,946 | 27.0% |
| LOAD_GLOBAL_MODULE | 82,440 | 4.4% |
| LOAD_FAST | 17,280 | 0.9% |
| CALL | 6,360 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,354,652 | 72.7% |
| STORE_FAST | 509,606 | 27.3% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 27,440 | 99.9% |
| BINARY_OP | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 27,480 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 576,080 | 90.3% |
| LOAD_CONST | 60,820 | 9.5% |
| BINARY_SUBSCR | 879 | 0.1% |
| CALL | 40 | 0.0% |
| CALL_BUILTIN_O | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 575,920 | 90.3% |
| STORE_FAST | 60,540 | 9.5% |
| BINARY_SUBSCR | 879 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 39,079 | 88.3% |
| LOAD_ATTR_MODULE | 5,100 | 11.5% |
| LOAD_GLOBAL | 41 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 44,240 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,900 | 48.5% |
| CALL | 27,520 | 35.2% |
| LOAD_ATTR_INSTANCE_VALUE | 12,716 | 16.3% |
| LOAD_ATTR | 84 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,800 | 77.7% |
| RETURN_CONST | 10,240 | 13.1% |
| LOAD_FAST | 7,040 | 9.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.2% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 11,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 5,760 | 50.0% |
| LOAD_FAST | 5,760 | 50.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,075,632 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,075,632 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 28,160 | 50.6% |
| LOAD_FAST | 27,520 | 49.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 41,600 | 74.7% |
| BUILD_STRING | 14,080 | 25.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,542,144 | 63.7% |
| STORE_FAST_LOAD_FAST | 576,000 | 23.8% |
| CALL_BUILTIN_CLASS | 275,584 | 11.4% |
| CALL | 14,340 | 0.6% |
| RETURN_VALUE | 5,760 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,591,932 | 65.7% |
| LOAD_FAST_AND_CLEAR | 517,992 | 21.4% |
| FOR_ITER_RANGE | 268,670 | 11.1% |
| FOR_ITER | 12,114 | 0.5% |
| FOR_ITER_TUPLE | 11,740 | 0.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,479,286 | 87.6% |
| RETURN_CONST | 898,946 | 7.5% |
| YIELD_VALUE | 577,740 | 4.8% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 500 | 89.3% |
| POP_TOP | 60 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 39,040 | 61.3% |
| STORE_FAST | 14,080 | 22.1% |
| LOAD_FAST | 7,040 | 11.1% |
| STORE_NAME | 2,480 | 3.9% |
| LOAD_CONST | 560 | 0.9% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,865,828 | 38.2% |
| POP_TOP | 1,589,572 | 15.7% |
| RESUME_CHECK | 1,404,820 | 13.9% |
| POP_JUMP_IF_FALSE | 1,350,884 | 13.3% |
| JUMP_BACKWARD | 1,088,000 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,424,422 | 63.5% |
| LOAD_GLOBAL_MODULE | 1,829,477 | 18.1% |
| LOAD_GLOBAL_BUILTIN | 743,224 | 7.3% |
| LOAD_FAST_LOAD_FAST | 583,320 | 5.8% |
| LOAD_CONST | 530,020 | 5.2% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 32,979 | 66.0% |
| COPY | 11,521 | 23.0% |
| POP_TOP | 5,200 | 10.4% |
| STORE_FAST | 280 | 0.6% |
| STORE_SUBSCR_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 33,279 | 66.6% |
| RERAISE | 11,521 | 23.0% |
| JUMP_FORWARD | 5,120 | 10.2% |
| RETURN_CONST | 60 | 0.1% |
| LOAD_FAST | 20 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,913,520 | 28.4% |
| RETURN_CONST | 6,649,724 | 27.4% |
| CALL | 2,263,277 | 9.3% |
| RETURN_VALUE | 1,529,548 | 6.3% |
| POP_JUMP_IF_FALSE | 1,507,565 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,735,486 | 35.9% |
| LOAD_FAST | 7,599,067 | 31.3% |
| RETURN_CONST | 1,931,896 | 7.9% |
| LOAD_CONST | 1,761,266 | 7.2% |
| NOP | 1,589,572 | 6.5% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 38,700 | 77.4% |
| RERAISE | 5,760 | 11.5% |
| CALL_KW | 5,120 | 10.2% |
| BINARY_SUBSCR_DICT | 300 | 0.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 39,039 | 78.1% |
| WITH_EXCEPT_START | 5,760 | 11.5% |
| LOAD_GLOBAL_MODULE | 5,080 | 10.2% |
| LOAD_GLOBAL | 121 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,683,628 | 49.8% |
| LOAD_ATTR_MODULE | 2,298,622 | 31.1% |
| LOAD_ATTR | 1,284,373 | 17.4% |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,494,477 | 47.3% |
| CALL | 2,044,185 | 27.6% |
| LOAD_FAST_LOAD_FAST | 1,396,348 | 18.9% |
| LOAD_CONST | 321,001 | 4.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 64,712 | 0.9% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,420 | 97.5% |
| COPY_FREE_VARS | 340 | 1.8% |
| CALL | 140 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,760 | 30.5% |
| LOAD_FAST | 5,760 | 30.5% |
| STORE_FAST | 5,760 | 30.5% |
| CALL_METHOD_DESCRIPTOR_O | 1,300 | 6.9% |
| CALL | 320 | 1.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,812,404 | 48.5% |
| CALL | 2,506,080 | 11.2% |
| RETURN_VALUE | 2,015,159 | 9.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,606,774 | 7.2% |
| CALL_FUNCTION_EX | 1,265,512 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 10,479,286 | 47.0% |
| STORE_FAST | 2,330,365 | 10.5% |
| RETURN_VALUE | 2,015,159 | 9.0% |
| POP_TOP | 1,529,548 | 6.9% |
| LOAD_FAST_LOAD_FAST | 1,203,120 | 5.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 14,080 | 45.0% |
| LOAD_FAST | 10,438 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 5,800 | 18.6% |
| STORE_SUBSCR | 660 | 2.1% |
| LOAD_ATTR | 200 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 19,960 | 63.9% |
| LOAD_GLOBAL_MODULE | 10,200 | 32.6% |
| STORE_SUBSCR | 660 | 2.1% |
| STORE_SUBSCR_DICT | 259 | 0.8% |
| LOAD_GLOBAL | 80 | 0.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,532,906 | 96.1% |
| LOAD_ATTR_INSTANCE_VALUE | 53,500 | 3.4% |
| TO_BOOL | 3,666 | 0.2% |
| LOAD_ATTR | 881 | 0.1% |
| RETURN_VALUE | 773 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 848,589 | 53.2% |
| POP_JUMP_IF_FALSE | 739,148 | 46.4% |
| TO_BOOL | 3,666 | 0.2% |
| TO_BOOL_BOOL | 2,163 | 0.1% |
| TO_BOOL_NONE | 360 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,203,120 | 69.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 519,696 | 30.2% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,722,896 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 259,696 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 259,736 | 100.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 5,680 | 98.6% |
| TO_BOOL | 80 | 1.4% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,869,088 | 53.6% |
| UNARY_INVERT | 1,722,896 | 23.9% |
| POP_JUMP_IF_FALSE | 1,203,120 | 16.7% |
| LOAD_ATTR | 273,988 | 3.8% |
| LOAD_FAST_LOAD_FAST | 84,160 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,926,016 | 40.6% |
| STORE_FAST | 1,477,428 | 20.5% |
| TO_BOOL_INT | 1,203,180 | 16.7% |
| UNARY_INVERT | 1,203,120 | 16.7% |
| BUILD_TUPLE | 259,888 | 3.6% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 50.0% |
| STORE_FAST | 140 | 50.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 517,992 | 33.4% |
| JUMP_FORWARD | 503,706 | 32.5% |
| LOAD_FAST | 260,562 | 16.8% |
| POP_TOP | 243,164 | 15.7% |
| STORE_ATTR_INSTANCE_VALUE | 10,660 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520,946 | 33.6% |
| SWAP | 517,992 | 33.4% |
| STORE_FAST | 505,166 | 32.6% |
| RETURN_VALUE | 5,120 | 0.3% |
| COMPARE_OP | 280 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 576,000 | 34.2% |
| LOAD_FAST | 529,560 | 31.4% |
| RESUME_CHECK | 513,906 | 30.5% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 2.0% |
| POP_JUMP_IF_NOT_NONE | 17,280 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,091,026 | 64.8% |
| BUILD_TUPLE | 576,020 | 34.2% |
| STORE_FAST | 17,280 | 1.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 27,520 | 66.2% |
| FORMAT_SIMPLE | 14,080 | 33.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 27,440 | 66.0% |
| RETURN_VALUE | 14,080 | 33.8% |
| BINARY_OP | 80 | 0.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,770,000 | 40.9% |
| LOAD_FAST_LOAD_FAST | 1,160,320 | 26.8% |
| BUILD_MAP | 576,020 | 13.3% |
| RETURN_VALUE | 512,000 | 11.8% |
| BINARY_OP | 259,888 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,204,680 | 27.9% |
| YIELD_VALUE | 1,152,100 | 26.6% |
| BUILD_MAP | 576,000 | 13.3% |
| STORE_FAST | 512,000 | 11.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 511,960 | 11.8% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,615,036 | 23.6% |
| PUSH_NULL | 2,044,185 | 18.5% |
| LOAD_FAST_LOAD_FAST | 1,943,558 | 17.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,441,920 | 13.0% |
| BUILD_TUPLE | 1,204,680 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,665,107 | 24.1% |
| RETURN_VALUE | 2,506,080 | 22.7% |
| POP_TOP | 2,263,277 | 20.5% |
| LOAD_FAST | 1,085,348 | 9.8% |
| TO_BOOL_BOOL | 731,796 | 6.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,849,692 | 76.6% |
| DICT_MERGE | 564,260 | 23.4% |
| CALL_INTRINSIC_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,265,512 | 52.4% |
| RESUME_CHECK | 535,040 | 22.2% |
| CALL_BUILTIN_CLASS | 511,960 | 21.2% |
| POP_TOP | 95,360 | 4.0% |
| STORE_FAST | 5,760 | 0.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 140 | 87.5% |
| CALL_FUNCTION_EX | 20 | 12.5% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360,029 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 290,444 | 80.7% |
| LOAD_FAST | 28,800 | 8.0% |
| RETURN_VALUE | 21,120 | 5.9% |
| STORE_FAST | 14,220 | 3.9% |
| PUSH_EXC_INFO | 5,120 | 1.4% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 590,198 | 99.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,474 | 0.2% |
| COMPARE_OP | 1,316 | 0.2% |
| LOAD_GLOBAL_MODULE | 380 | 0.1% |
| LOAD_FAST | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 591,633 | 99.4% |
| COMPARE_OP | 1,316 | 0.2% |
| COMPARE_OP_INT | 1,181 | 0.2% |
| COMPARE_OP_STR | 440 | 0.1% |
| POP_JUMP_IF_TRUE | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,779,021 | 99.9% |
| LOAD_ATTR_MODULE | 560 | 0.0% |
| LOAD_FAST | 480 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR | 99 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,779,680 | 100.0% |
| POP_JUMP_IF_TRUE | 480 | 0.0% |
| STORE_FAST | 140 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 14,040 | 49.9% |
| CALL_BUILTIN_FAST | 14,040 | 49.9% |
| BINARY_SUBSCR | 40 | 0.1% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 28,160 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 2,926,016 | 40.0% |
| STORE_FAST | 2,629,760 | 36.0% |
| LOAD_CONST | 1,100,800 | 15.1% |
| LOAD_FAST | 590,100 | 8.1% |
| STORE_ATTR_INSTANCE_VALUE | 21,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 2,925,696 | 40.0% |
| STORE_FAST | 2,630,400 | 36.0% |
| STORE_FAST_STORE_FAST | 1,093,760 | 15.0% |
| LOAD_ATTR_INSTANCE_VALUE | 575,882 | 7.9% |
| LOAD_FAST | 28,160 | 0.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 1,203,120 | 66.0% |
| CALL_ALLOC_AND_ENTER_INIT | 503,666 | 27.6% |
| CACHE | 109,900 | 6.0% |
| CALL | 5,940 | 0.3% |
| CALL_PY_EXACT_ARGS | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,822,486 | 100.0% |
| RETURN_GENERATOR | 340 | 0.0% |
| RESUME | 320 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,600 | 66.7% |
| RETURN_CONST | 27,520 | 31.9% |
| LOAD_GLOBAL_MODULE | 1,240 | 1.4% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,700 | 93.9% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 6.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 564,260 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,271,226 | 97.4% |
| SWAP | 14,160 | 1.1% |
| GET_ITER | 12,114 | 0.9% |
| LOAD_FAST | 6,060 | 0.5% |
| FOR_ITER | 1,700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 688,680 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 581,600 | 44.6% |
| SWAP | 14,080 | 1.1% |
| RETURN_CONST | 11,820 | 0.9% |
| LOAD_GLOBAL_MODULE | 5,680 | 0.4% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 33,080 | 99.0% |
| STORE_NAME | 340 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 32,640 | 97.7% |
| STORE_NAME | 780 | 2.3% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 33,080 | 98.0% |
| STORE_NAME | 680 | 2.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 27,520 | 58.6% |
| LOAD_FAST | 17,420 | 37.1% |
| LOAD_GLOBAL_MODULE | 1,977 | 4.2% |
| LOAD_GLOBAL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 46,817 | 99.7% |
| POP_JUMP_IF_TRUE | 140 | 0.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,735,486 | 48.4% |
| STORE_FAST | 5,760,000 | 31.9% |
| POP_JUMP_IF_NOT_NONE | 999,388 | 5.5% |
| LIST_APPEND | 840,804 | 4.7% |
| STORE_FAST_STORE_FAST | 581,760 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 7,984,624 | 44.2% |
| FOR_ITER_GEN | 6,335,920 | 35.1% |
| FOR_ITER | 1,271,226 | 7.0% |
| NOP | 1,088,000 | 6.0% |
| LOAD_GLOBAL_BUILTIN | 575,960 | 3.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,082,441 | 62.9% |
| POP_TOP | 621,513 | 36.1% |
| STORE_ATTR_INSTANCE_VALUE | 7,020 | 0.4% |
| BINARY_SUBSCR_TUPLE_INT | 5,720 | 0.3% |
| POP_EXCEPT | 5,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,142,029 | 66.3% |
| BUILD_LIST | 503,706 | 29.2% |
| POP_EXCEPT | 32,979 | 1.9% |
| LOAD_GLOBAL_MODULE | 24,820 | 1.4% |
| LOAD_FAST_LOAD_FAST | 7,320 | 0.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 466,256 | 55.5% |
| LOAD_ATTR | 259,908 | 30.9% |
| BINARY_SUBSCR_STR_INT | 112,600 | 13.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,000 | 0.2% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 840,804 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 244,584 | 50.1% |
| RETURN_VALUE | 243,164 | 49.8% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_DEREF | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 243,804 | 50.0% |
| STORE_FAST | 243,164 | 49.8% |
| RETURN_VALUE | 640 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |
| STORE_NAME | 120 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,161,990 | 77.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,819,920 | 17.3% |
| LOAD_GLOBAL_MODULE | 400,084 | 3.8% |
| CALL | 83,860 | 0.8% |
| LOAD_ATTR | 22,879 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,546,393 | 33.7% |
| PUSH_NULL | 1,284,373 | 12.2% |
| STORE_SUBSCR_DICT | 1,203,040 | 11.4% |
| POP_JUMP_IF_NOT_NONE | 1,162,830 | 11.0% |
| STORE_FAST | 748,154 | 7.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,997,093 | 25.6% |
| LOAD_CONST | 3,839,401 | 24.6% |
| POP_TOP | 1,761,266 | 11.3% |
| POP_JUMP_IF_FALSE | 922,539 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 740,903 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,839,401 | 24.6% |
| CALL | 2,615,036 | 16.8% |
| COMPARE_OP_INT | 2,071,535 | 13.3% |
| LOAD_FAST | 1,696,007 | 10.9% |
| COPY | 1,100,800 | 7.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,816,346 | 97.0% |
| POP_JUMP_IF_NOT_NONE | 27,520 | 1.5% |
| STORE_DEREF | 27,520 | 1.5% |
| STORE_FAST | 440 | 0.0% |
| POP_JUMP_IF_FALSE | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,816,866 | 97.0% |
| POP_JUMP_IF_NOT_NONE | 55,040 | 2.9% |
| PUSH_NULL | 460 | 0.0% |
| LOAD_CONST | 280 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 21,025,430 | 20.6% |
| STORE_FAST | 13,045,490 | 12.8% |
| POP_JUMP_IF_FALSE | 7,984,807 | 7.8% |
| POP_TOP | 7,599,067 | 7.4% |
| NOP | 6,424,422 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 22,341,722 | 21.9% |
| RETURN_VALUE | 10,812,404 | 10.6% |
| LOAD_ATTR | 8,161,990 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,134,301 | 8.0% |
| CALL_PY_EXACT_ARGS | 5,318,887 | 5.2% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 517,992 | 66.6% |
| LOAD_FAST_AND_CLEAR | 259,888 | 33.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 517,992 | 66.6% |
| LOAD_FAST_AND_CLEAR | 259,888 | 33.4% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 576,560 | 68.9% |
| POP_JUMP_IF_NONE | 243,818 | 29.1% |
| LOAD_ATTR_CLASS | 16,532 | 2.0% |
| LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 575,920 | 68.8% |
| LOAD_GLOBAL_MODULE | 243,738 | 29.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 16,492 | 2.0% |
| POP_JUMP_IF_NOT_NONE | 560 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,714,884 | 17.1% |
| LOAD_FAST_LOAD_FAST | 2,080,544 | 13.1% |
| POP_JUMP_IF_FALSE | 1,511,715 | 9.5% |
| PUSH_NULL | 1,396,348 | 8.8% |
| LOAD_SUPER_ATTR_METHOD | 1,217,400 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,708,856 | 23.3% |
| LOAD_FAST_LOAD_FAST | 2,080,544 | 13.1% |
| CALL | 1,943,558 | 12.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,757,254 | 11.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,203,040 | 7.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,000 | 11.2% |
| RESUME_CHECK | 1,720 | 9.6% |
| POP_JUMP_IF_FALSE | 1,708 | 9.6% |
| LOAD_FAST | 1,600 | 9.0% |
| RESUME | 1,520 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,820 | 38.2% |
| LOAD_ATTR | 3,321 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 2,740 | 15.4% |
| LOAD_FAST | 2,161 | 12.1% |
| CALL | 740 | 4.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 820 | 37.3% |
| LOAD_CONST | 600 | 27.3% |
| RESUME | 560 | 25.5% |
| PUSH_NULL | 120 | 5.5% |
| POP_TOP | 80 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 640 | 29.1% |
| CALL | 500 | 22.7% |
| LOAD_ATTR | 420 | 19.1% |
| LOAD_CONST | 380 | 17.3% |
| PUSH_NULL | 220 | 10.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 200 | 38.5% |
| PUSH_NULL | 80 | 15.4% |
| LOAD_FAST_LOAD_FAST | 80 | 15.4% |
| LOAD_SUPER_ATTR_ATTR | 80 | 15.4% |
| CALL | 40 | 7.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| CALL_PY_EXACT_ARGS | 27,800 | 20.2% |
| CACHE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| RESUME_CHECK | 27,820 | 20.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 5,332,296 | 27.3% |
| TO_BOOL_BOOL | 4,964,938 | 25.5% |
| COMPARE_OP_INT | 3,776,085 | 19.4% |
| CONTAINS_OP | 1,779,680 | 9.1% |
| COMPARE_OP_STR | 1,450,084 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,984,807 | 40.9% |
| RETURN_CONST | 3,179,529 | 16.3% |
| LOAD_FAST_LOAD_FAST | 1,511,715 | 7.7% |
| POP_TOP | 1,507,565 | 7.7% |
| LOAD_GLOBAL_MODULE | 1,479,840 | 7.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,069,034 | 93.2% |
| LOAD_ATTR_INSTANCE_VALUE | 47,800 | 4.2% |
| LOAD_ATTR | 28,300 | 2.5% |
| RETURN_VALUE | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 297,239 | 25.9% |
| NOP | 281,084 | 24.5% |
| LOAD_FAST | 274,725 | 24.0% |
| LOAD_FAST_CHECK | 243,818 | 21.3% |
| RETURN_CONST | 24,340 | 2.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,429,094 | 47.3% |
| LOAD_ATTR | 1,162,830 | 22.7% |
| LOAD_ATTR_INSTANCE_VALUE | 997,435 | 19.4% |
| RETURN_VALUE | 466,896 | 9.1% |
| LOAD_DEREF | 55,040 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,062,546 | 40.2% |
| RETURN_CONST | 1,164,161 | 22.7% |
| JUMP_BACKWARD | 999,388 | 19.5% |
| NOP | 512,415 | 10.0% |
| LOAD_CONST | 243,444 | 4.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,878,105 | 68.0% |
| TO_BOOL | 848,589 | 30.7% |
| TO_BOOL_NONE | 19,700 | 0.7% |
| COMPARE_OP_STR | 10,950 | 0.4% |
| COMPARE_OP_INT | 3,377 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 957,544 | 34.7% |
| LOAD_FAST_LOAD_FAST | 851,388 | 30.8% |
| RETURN_CONST | 766,114 | 27.7% |
| LOAD_GLOBAL_MODULE | 72,807 | 2.6% |
| RETURN_VALUE | 60,500 | 2.2% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,760 | 99.7% |
| CALL_KW | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,760 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 11,521 | 66.7% |
| POP_JUMP_IF_TRUE | 5,760 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,761 | 50.0% |
| PUSH_EXC_INFO | 5,760 | 50.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,179,529 | 33.8% |
| STORE_ATTR_INSTANCE_VALUE | 2,228,224 | 23.7% |
| POP_TOP | 1,931,896 | 20.5% |
| POP_JUMP_IF_NOT_NONE | 1,164,161 | 12.4% |
| POP_JUMP_IF_TRUE | 766,114 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,649,724 | 70.6% |
| EXIT_INIT_CHECK | 1,075,632 | 11.4% |
| INTERPRETER_EXIT | 898,946 | 9.5% |
| TO_BOOL_BOOL | 689,090 | 7.3% |
| STORE_FAST | 62,340 | 0.7% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 39,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 37,920 | 97.1% |
| STORE_NAME | 780 | 2.0% |
| LOAD_GLOBAL_MODULE | 280 | 0.7% |
| LOAD_FAST | 60 | 0.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,566 | 58.1% |
| LOAD_FAST_LOAD_FAST | 22,040 | 21.9% |
| LOAD_ATTR_INSTANCE_VALUE | 17,280 | 17.1% |
| STORE_ATTR | 2,520 | 2.5% |
| LOAD_ATTR | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 44,840 | 44.5% |
| LOAD_FAST_LOAD_FAST | 14,760 | 14.6% |
| LOAD_FAST | 13,619 | 13.5% |
| LOAD_CONST | 12,644 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 5,680 | 5.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_BUILTIN | 27,520 | 20.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 54,960 | 39.9% |
| LOAD_DEREF | 27,520 | 20.0% |
| LOAD_FAST | 27,520 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 27,480 | 20.0% |
| LOAD_GLOBAL | 120 | 0.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,335,920 | 21.2% |
| CALL | 2,665,107 | 8.9% |
| COPY | 2,630,400 | 8.8% |
| RETURN_VALUE | 2,330,365 | 7.8% |
| FOR_ITER_LIST | 1,704,748 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,045,490 | 43.7% |
| JUMP_BACKWARD | 5,760,000 | 19.3% |
| NOP | 3,865,828 | 13.0% |
| COPY | 2,629,760 | 8.8% |
| LOAD_GLOBAL_BUILTIN | 1,214,402 | 4.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,760,060 | 89.1% |
| FOR_ITER | 688,680 | 10.7% |
| COPY | 14,080 | 0.2% |
| FOR_ITER_TUPLE | 2,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 5,760,000 | 89.1% |
| GET_ITER | 576,000 | 8.9% |
| LOAD_FAST | 112,640 | 1.7% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 0.2% |
| TO_BOOL_STR | 2,000 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,156,621 | 44.5% |
| COPY | 1,093,760 | 22.5% |
| UNPACK_SEQUENCE_TUPLE | 1,088,220 | 22.4% |
| STORE_FAST_STORE_FAST | 512,000 | 10.6% |
| UNPACK_SEQUENCE | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,608,056 | 33.1% |
| STORE_FAST | 1,088,280 | 22.4% |
| LOAD_FAST_LOAD_FAST | 1,044,945 | 21.5% |
| JUMP_BACKWARD | 581,760 | 12.0% |
| STORE_FAST_STORE_FAST | 512,000 | 10.6% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,480 | 33.2% |
| CALL | 1,200 | 16.0% |
| IMPORT_FROM | 780 | 10.4% |
| SET_FUNCTION_ATTRIBUTE | 780 | 10.4% |
| IMPORT_NAME | 680 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,640 | 62.0% |
| LOAD_NAME | 820 | 11.0% |
| RETURN_CONST | 700 | 9.4% |
| LOAD_BUILD_CLASS | 500 | 6.7% |
| POP_TOP | 440 | 5.9% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 575,941 | 21.6% |
| BUILD_LIST | 517,992 | 19.5% |
| LOAD_FAST_AND_CLEAR | 517,992 | 19.5% |
| FOR_ITER_LIST | 503,052 | 18.9% |
| LOAD_FAST | 271,618 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 575,882 | 21.6% |
| LOAD_CONST | 531,506 | 20.0% |
| BUILD_LIST | 517,992 | 19.5% |
| STORE_FAST | 517,992 | 19.5% |
| FOR_ITER_LIST | 502,972 | 18.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 260 | 28.3% |
| FOR_ITER | 240 | 26.1% |
| LOAD_FAST | 120 | 13.0% |
| RETURN_VALUE | 80 | 8.7% |
| LOAD_FAST_CHECK | 80 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 360 | 39.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 37.0% |
| UNPACK_SEQUENCE_TUPLE | 100 | 10.9% |
| LOAD_FAST | 40 | 4.3% |
| STORE_FAST | 40 | 4.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,000 | 83.3% |
| BUILD_TUPLE | 1,152,100 | 16.7% |
| CALL_STR_1 | 1,260 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,335,920 | 91.6% |
| INTERPRETER_EXIT | 577,740 | 8.4% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,820 | 47.2% |
| CACHE | 2,280 | 38.1% |
| COPY_FREE_VARS | 320 | 5.4% |
| CALL_KW | 200 | 3.3% |
| POP_TOP | 140 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 48.2% |
| LOAD_GLOBAL | 1,520 | 25.4% |
| LOAD_NAME | 560 | 9.4% |
| NOP | 280 | 4.7% |
| LOAD_CONST | 240 | 4.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260,462 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260,502 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,093,802 | 98.3% |
| LOAD_FAST_LOAD_FAST | 18,480 | 1.7% |
| BINARY_OP | 159 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 575,941 | 51.8% |
| STORE_FAST | 511,980 | 46.0% |
| BINARY_SLICE | 18,520 | 1.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,680 | 0.5% |
| LOAD_CONST | 280 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 32.3% |
| CALL_METHOD_DESCRIPTOR_O | 1,240 | 32.3% |
| LOAD_FAST_LOAD_FAST | 960 | 25.0% |
| BINARY_SUBSCR_LIST_INT | 280 | 7.3% |
| LOAD_FAST | 80 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,740 | 45.3% |
| LOAD_CONST | 1,260 | 32.8% |
| CALL | 480 | 12.5% |
| STORE_FAST | 360 | 9.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 112,560 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 243,738 | 99.9% |
| BINARY_OP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 243,898 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 264,888 | 80.0% |
| LOAD_CONST | 60,420 | 18.2% |
| CALL_LEN | 5,680 | 1.7% |
| BINARY_OP | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 325,468 | 98.3% |
| CALL_BUILTIN_CLASS | 5,680 | 1.7% |
| CALL | 40 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 99,860 | 86.9% |
| LOAD_CONST | 14,280 | 12.4% |
| LOAD_FAST | 700 | 0.6% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 99,860 | 86.9% |
| CONVERT_VALUE | 14,040 | 12.2% |
| STORE_FAST | 400 | 0.3% |
| PUSH_EXC_INFO | 300 | 0.3% |
| LOAD_FAST | 140 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 486,248 | 97.6% |
| LOAD_CONST | 11,640 | 2.3% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 486,288 | 97.6% |
| LOAD_CONST | 11,440 | 2.3% |
| BINARY_OP_ADD_UNICODE | 280 | 0.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 112,600 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,120 | 99.9% |
| BINARY_SUBSCR | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,020 | 84.3% |
| JUMP_FORWARD | 5,720 | 14.6% |
| STORE_FAST | 420 | 1.1% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 531,106 | 49.4% |
| LOAD_FAST | 510,826 | 47.5% |
| CALL | 33,420 | 3.1% |
| LOAD_FAST_LOAD_FAST | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 571,966 | 53.2% |
| COPY_FREE_VARS | 503,666 | 46.8% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 64,712 | 45.4% |
| LOAD_FAST | 64,240 | 45.1% |
| LOAD_CONST | 7,480 | 5.3% |
| BINARY_OP_ADD_INT | 5,680 | 4.0% |
| CALL | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 135,992 | 95.5% |
| POP_TOP | 6,280 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 736,764 | 36.0% |
| CALL_FUNCTION_EX | 511,960 | 25.0% |
| LOAD_FAST | 278,242 | 13.6% |
| CALL_BUILTIN_CLASS | 243,084 | 11.9% |
| CALL_LEN | 243,084 | 11.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 772,482 | 37.8% |
| STORE_FAST | 737,064 | 36.0% |
| GET_ITER | 275,584 | 13.5% |
| CALL_BUILTIN_CLASS | 243,084 | 11.9% |
| LOAD_FAST | 17,280 | 0.8% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 902,445 | 48.6% |
| LOAD_CONST | 644,208 | 34.7% |
| LOAD_FAST_LOAD_FAST | 173,248 | 9.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 81,284 | 4.4% |
| LOAD_GLOBAL_MODULE | 27,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 634,148 | 34.1% |
| STORE_FAST | 597,116 | 32.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 468,905 | 25.2% |
| UNPACK_SEQUENCE_TUPLE | 81,284 | 4.4% |
| POP_TOP | 14,872 | 0.8% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 519,140 | 45.6% |
| BUILD_TUPLE | 511,960 | 45.0% |
| CALL | 65,012 | 5.7% |
| LOAD_FAST_CHECK | 16,492 | 1.4% |
| LOAD_ATTR | 14,000 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,053,900 | 92.6% |
| RETURN_VALUE | 82,184 | 7.2% |
| LOAD_FAST | 1,260 | 0.1% |
| STORE_FAST | 440 | 0.0% |
| BEFORE_WITH | 140 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 112,560 | 72.9% |
| LOAD_ATTR | 27,440 | 17.8% |
| LOAD_FAST | 14,280 | 9.2% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 112,560 | 72.9% |
| LOAD_FAST | 41,520 | 26.9% |
| STORE_FAST | 140 | 0.1% |
| TO_BOOL_INT | 140 | 0.1% |
| BINARY_SUBSCR | 40 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,220,580 | 100.0% |
| CALL | 180 | 0.0% |
| BUILD_TUPLE | 140 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,220,860 | 100.0% |
| TO_BOOL | 180 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 605,299 | 95.5% |
| LOAD_ATTR_INSTANCE_VALUE | 27,900 | 4.4% |
| CALL | 380 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 344,328 | 54.3% |
| CALL_BUILTIN_CLASS | 243,084 | 38.4% |
| CALL_PY_EXACT_ARGS | 33,160 | 5.2% |
| LOAD_FAST | 5,720 | 0.9% |
| BINARY_OP_SUBTRACT_INT | 5,680 | 0.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 259,808 | 95.6% |
| LOAD_FAST | 11,440 | 4.2% |
| LOAD_CONST | 140 | 0.1% |
| LOAD_FAST_CHECK | 140 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 259,848 | 95.6% |
| LOAD_GLOBAL_MODULE | 11,440 | 4.2% |
| NOP | 280 | 0.1% |
| RETURN_CONST | 140 | 0.1% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,706,806 | 99.6% |
| LOAD_ATTR_INSTANCE_VALUE | 2,589 | 0.2% |
| LOAD_GLOBAL_MODULE | 2,280 | 0.1% |
| LOAD_CONST | 1,240 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,203,400 | 70.2% |
| STORE_FAST | 506,554 | 29.6% |
| LIST_APPEND | 2,000 | 0.1% |
| TO_BOOL_NONE | 1,240 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 37,480 | 86.5% |
| BUILD_TUPLE | 5,680 | 13.1% |
| CALL | 180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 31,860 | 73.5% |
| LOAD_FAST | 11,480 | 26.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,410,698 | 93.3% |
| LOAD_ATTR_METHOD_LAZY_DICT | 97,776 | 6.5% |
| LOAD_ATTR | 2,480 | 0.2% |
| CALL | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 661,586 | 43.8% |
| STORE_FAST | 575,960 | 38.1% |
| LOAD_FAST | 85,060 | 5.6% |
| CALL_BUILTIN_FAST | 81,284 | 5.4% |
| RETURN_VALUE | 51,624 | 3.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 890,530 | 91.8% |
| LOAD_CONST | 33,720 | 3.5% |
| CALL | 29,139 | 3.0% |
| RETURN_VALUE | 14,000 | 1.4% |
| RETURN_GENERATOR | 1,300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 919,809 | 94.8% |
| LOAD_CONST | 33,440 | 3.4% |
| RETURN_VALUE | 14,900 | 1.5% |
| BINARY_OP_ADD_UNICODE | 1,240 | 0.1% |
| STORE_FAST | 280 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 5,708,827 | 44.9% |
| LOAD_FAST | 5,318,887 | 41.9% |
| LOAD_FAST_LOAD_FAST | 833,284 | 6.6% |
| LOAD_SUPER_ATTR_METHOD | 503,626 | 4.0% |
| LOAD_GLOBAL_MODULE | 93,900 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,656,933 | 99.6% |
| MAKE_CELL | 27,800 | 0.2% |
| RETURN_GENERATOR | 18,420 | 0.1% |
| COPY_FREE_VARS | 360 | 0.0% |
| PUSH_EXC_INFO | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 1,235,703 | 41.5% |
| LOAD_ATTR_MODULE | 1,203,040 | 40.4% |
| LOAD_FAST | 342,848 | 11.5% |
| LOAD_CONST | 107,656 | 3.6% |
| BINARY_OP | 83,760 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,776,011 | 59.6% |
| COPY_FREE_VARS | 1,203,120 | 40.4% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,860 | 99.7% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,220 | 85.9% |
| YIELD_VALUE | 1,260 | 10.6% |
| STORE_FAST | 280 | 2.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 140 | 1.2% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 581,740 | 99.8% |
| LOAD_FAST | 1,240 | 0.2% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 581,720 | 99.8% |
| LOAD_FAST | 1,260 | 0.2% |
| CALL | 140 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 86.1% |
| LOAD_GLOBAL_MODULE | 140 | 9.7% |
| CALL | 60 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,260 | 87.5% |
| PUSH_NULL | 140 | 9.7% |
| LOAD_GLOBAL | 40 | 2.8% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 140 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,071,535 | 54.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,087,830 | 28.8% |
| LOAD_FAST | 576,980 | 15.3% |
| LOAD_FAST_LOAD_FAST | 18,480 | 0.5% |
| CALL_BUILTIN_FAST | 14,000 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,776,085 | 99.9% |
| POP_JUMP_IF_TRUE | 3,377 | 0.1% |
| RETURN_VALUE | 160 | 0.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 101 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,422,994 | 95.6% |
| LOAD_CONST | 59,860 | 4.0% |
| LOAD_FAST | 5,820 | 0.4% |
| COMPARE_OP | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,450,084 | 97.4% |
| COPY | 14,040 | 0.9% |
| LOAD_FAST | 14,040 | 0.9% |
| POP_JUMP_IF_TRUE | 10,950 | 0.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,335,920 | 99.8% |
| GET_ITER | 11,440 | 0.2% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,335,920 | 99.8% |
| POP_TOP | 11,440 | 0.2% |
| RESUME | 80 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,984,624 | 79.2% |
| GET_ITER | 1,591,932 | 15.8% |
| SWAP | 502,972 | 5.0% |
| FOR_ITER | 300 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,060 | 57.1% |
| STORE_FAST | 1,704,748 | 16.9% |
| LOAD_FAST | 1,007,412 | 10.0% |
| JUMP_BACKWARD | 576,000 | 5.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 520,176 | 5.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 513,854 | 65.6% |
| GET_ITER | 268,670 | 34.3% |
| FOR_ITER | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 528,520 | 67.5% |
| LOAD_FAST | 243,324 | 31.1% |
| RETURN_CONST | 10,880 | 1.4% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,320 | 54.0% |
| GET_ITER | 11,740 | 38.8% |
| LOAD_FAST | 1,260 | 4.2% |
| SWAP | 860 | 2.8% |
| FOR_ITER | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,260 | 47.2% |
| LOAD_FAST | 10,460 | 34.6% |
| RETURN_CONST | 2,560 | 8.5% |
| STORE_FAST_LOAD_FAST | 2,000 | 6.6% |
| SWAP | 860 | 2.8% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 81,244 | 88.8% |
| LOAD_ATTR_MODULE | 10,200 | 11.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,992 | 81.9% |
| LOAD_FAST_CHECK | 16,532 | 18.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,341,722 | 90.4% |
| LOAD_FAST_LOAD_FAST | 1,757,254 | 7.1% |
| COPY | 575,882 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 23,677 | 0.1% |
| RETURN_VALUE | 14,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,643,433 | 22.8% |
| LOAD_FAST | 3,740,181 | 15.1% |
| TO_BOOL_BOOL | 1,920,449 | 7.8% |
| LOAD_ATTR | 1,819,920 | 7.4% |
| CONTAINS_OP | 1,779,021 | 7.2% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 408,936 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,688 | 39.8% |
| CALL | 148,652 | 36.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 97,776 | 23.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,643,433 | 87.1% |
| LOAD_FAST | 638,291 | 9.8% |
| LOAD_ATTR | 85,278 | 1.3% |
| LOAD_ATTR_SLOT | 83,760 | 1.3% |
| LOAD_CONST | 15,520 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,554,415 | 39.4% |
| CALL | 1,441,920 | 22.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,410,698 | 21.8% |
| LOAD_CONST | 740,903 | 11.4% |
| LOAD_FAST_LOAD_FAST | 302,426 | 4.7% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,134,301 | 71.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,349,895 | 11.9% |
| LOAD_FAST_LOAD_FAST | 1,203,040 | 10.6% |
| BINARY_SUBSCR | 575,920 | 5.1% |
| LOAD_GLOBAL_MODULE | 28,860 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 5,708,827 | 50.5% |
| LOAD_FAST | 3,458,958 | 30.6% |
| CALL_PY_WITH_DEFAULTS | 1,235,703 | 10.9% |
| LOAD_FAST_LOAD_FAST | 678,560 | 6.0% |
| LOAD_CONST | 126,136 | 1.1% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,654,034 | 99.9% |
| LOAD_ATTR | 2,820 | 0.1% |
| LOAD_FAST | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,298,622 | 62.9% |
| CALL_PY_WITH_DEFAULTS | 1,203,040 | 32.9% |
| STORE_DEREF | 55,040 | 1.5% |
| LOAD_CONST | 35,840 | 1.0% |
| LOAD_FAST | 28,800 | 0.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,243,640 | 70.5% |
| LOAD_FAST_LOAD_FAST | 519,616 | 29.5% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,203,080 | 68.2% |
| UNARY_INVERT | 519,696 | 29.5% |
| RETURN_VALUE | 14,040 | 0.8% |
| LOAD_CONST | 14,040 | 0.8% |
| LOAD_FAST_LOAD_FAST | 5,720 | 0.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,024,681 | 97.2% |
| RETURN_VALUE | 27,440 | 2.6% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.1% |
| LOAD_ATTR | 320 | 0.0% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,041,521 | 98.8% |
| TO_BOOL_BOOL | 12,160 | 1.2% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,360 | 98.6% |
| LOAD_ATTR_MODULE | 1,180 | 1.2% |
| RETURN_VALUE | 140 | 0.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 83,760 | 84.0% |
| CALL_BUILTIN_FAST | 14,140 | 14.2% |
| LOAD_FAST | 1,040 | 1.0% |
| LOAD_CONST | 600 | 0.6% |
| STORE_FAST | 140 | 0.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,707,746 | 41.9% |
| LOAD_FAST | 1,247,220 | 14.1% |
| STORE_FAST | 1,214,402 | 13.7% |
| LOAD_GLOBAL_BUILTIN | 998,128 | 11.3% |
| NOP | 743,224 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,085,573 | 46.1% |
| LOAD_DEREF | 1,816,346 | 20.5% |
| CALL_ISINSTANCE | 1,220,580 | 13.8% |
| LOAD_GLOBAL_BUILTIN | 998,128 | 11.3% |
| LOAD_GLOBAL_MODULE | 625,080 | 7.1% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,963,377 | 28.7% |
| RESUME_CHECK | 3,158,581 | 18.3% |
| NOP | 1,829,477 | 10.6% |
| POP_JUMP_IF_FALSE | 1,479,840 | 8.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,451,971 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 3,869,088 | 22.4% |
| LOAD_ATTR_MODULE | 3,654,034 | 21.1% |
| LOAD_FAST_LOAD_FAST | 2,714,884 | 15.7% |
| LOAD_FAST | 2,187,468 | 12.6% |
| COMPARE_OP_STR | 1,422,994 | 8.2% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,440 | 99.9% |
| LOAD_SUPER_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 89,520 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,726,626 | 100.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,217,400 | 70.5% |
| CALL_PY_EXACT_ARGS | 503,626 | 29.2% |
| LOAD_FAST | 5,760 | 0.3% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 12,656,933 | 33.7% |
| CACHE | 11,842,092 | 31.5% |
| FOR_ITER_GEN | 6,335,920 | 16.9% |
| COPY_FREE_VARS | 1,822,486 | 4.9% |
| CALL_PY_WITH_DEFAULTS | 1,776,011 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,025,430 | 56.0% |
| POP_TOP | 6,913,520 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 3,707,746 | 9.9% |
| LOAD_GLOBAL_MODULE | 3,158,581 | 8.4% |
| NOP | 1,404,820 | 3.7% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,099,338 | 69.2% |
| LOAD_FAST_LOAD_FAST | 765,406 | 17.1% |
| SWAP | 575,882 | 12.9% |
| LOAD_ATTR_INSTANCE_VALUE | 17,040 | 0.4% |
| STORE_FAST_LOAD_FAST | 14,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,228,224 | 49.7% |
| LOAD_FAST | 940,601 | 21.0% |
| LOAD_GLOBAL_MODULE | 742,246 | 16.6% |
| LOAD_CONST | 302,856 | 6.8% |
| LOAD_FAST_LOAD_FAST | 129,480 | 2.9% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,760 | 85.5% |
| LOAD_FAST_LOAD_FAST | 14,140 | 14.4% |
| STORE_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,980 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,203,040 | 93.0% |
| LOAD_FAST | 44,189 | 3.4% |
| LOAD_ATTR_INSTANCE_VALUE | 34,680 | 2.7% |
| CALL | 10,200 | 0.8% |
| LOAD_CONST | 1,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,205,688 | 93.2% |
| RETURN_CONST | 32,520 | 2.5% |
| LOAD_GLOBAL_MODULE | 27,720 | 2.1% |
| LOAD_CONST | 27,480 | 2.1% |
| NOP | 140 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,920,449 | 27.0% |
| CALL_ISINSTANCE | 1,220,860 | 17.2% |
| RETURN_VALUE | 894,561 | 12.6% |
| CALL | 731,796 | 10.3% |
| LOAD_FAST | 720,260 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,964,938 | 69.9% |
| POP_JUMP_IF_TRUE | 1,878,105 | 26.4% |
| UNARY_NOT | 259,696 | 3.7% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,925,696 | 54.9% |
| BINARY_OP | 1,203,180 | 22.6% |
| LOAD_FAST | 1,203,040 | 22.6% |
| TO_BOOL | 240 | 0.0% |
| CALL_BUILTIN_O | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,332,296 | 100.0% |
| POP_JUMP_IF_TRUE | 140 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 515,126 | 92.3% |
| LOAD_ATTR_INSTANCE_VALUE | 42,900 | 7.7% |
| TO_BOOL | 200 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 558,086 | 100.0% |
| POP_JUMP_IF_TRUE | 160 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 191,357 | 79.6% |
| LOAD_FAST | 27,900 | 11.6% |
| COPY | 13,880 | 5.8% |
| WITH_EXCEPT_START | 5,680 | 2.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220,717 | 91.8% |
| POP_JUMP_IF_TRUE | 19,700 | 8.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,000 | 71.4% |
| LOAD_FAST | 620 | 22.1% |
| COPY | 160 | 5.7% |
| LOAD_GLOBAL_MODULE | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,600 | 92.9% |
| POP_JUMP_IF_TRUE | 200 | 7.1% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,087,880 | 93.0% |
| CALL_BUILTIN_FAST | 81,284 | 7.0% |
| CALL_METHOD_DESCRIPTOR_O | 280 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,088,220 | 93.0% |
| STORE_FAST | 81,324 | 7.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 581,600 | 26.9% |
| LOAD_FAST_CHECK | 575,920 | 26.6% |
| FOR_ITER_LIST | 520,176 | 24.0% |
| CALL_BUILTIN_FAST | 468,905 | 21.7% |
| CALL | 9,440 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,156,621 | 99.7% |
| LOAD_FAST | 7,000 | 0.3% |
| STORE_DEREF | 60 | 0.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 65.4% |
| COPY | 277 | 30.2% |
| TO_BOOL | 40 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 620 | 67.6% |
| POP_JUMP_IF_FALSE | 297 | 32.4% |


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
|     deferred | 7,207,848 | 77.4% |
|          hit | 2,091,949 | 22.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 599 | 8.4% |
| Failure | 6,502 | 91.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,246 | 49.9% |
| or | 1,737 | 26.7% |
| remainder | 779 | 12.0% |
| add different types | 640 | 9.8% |
| add other | 100 | 1.5% |


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
|     deferred | 636,740 | 45.4% |
|          hit | 764,648 | 54.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 21.4% |
| Failure | 879 | 78.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 879 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,023,804 | 27.4% |
|          hit | 29,186,247 | 72.5% |
|         miss | 7,580 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,302 | 23.5% |
| Failure | 30,266 | 76.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 7,924 | 26.2% |
| cfunc noargs | 6,348 | 21.0% |
| class no vectorcall | 4,000 | 13.2% |
| meth descr varargs keywords | 3,217 | 10.6% |
| class mutable | 1,295 | 4.3% |
| other | 1,180 | 3.9% |
| bound method | 1,127 | 3.7% |
| cfunc varargs | 1,100 | 3.6% |
| cfunc varargs keywords | 935 | 3.1% |
| meth descr method fastcall keywords | 920 | 3.0% |
| operator wrapper | 780 | 2.6% |
| cmethod | 640 | 2.1% |
| wrong number arguments | 480 | 1.6% |
| method wrapper | 280 | 0.9% |
| meth descr varargs | 40 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 591,892 | 10.1% |
|          hit | 5,262,242 | 89.7% |
|         miss | 6,875 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,621 | 53.4% |
| Failure | 1,417 | 46.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 822 | 58.0% |
| big int | 360 | 25.4% |
| different types | 235 | 16.6% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,302,940 | 7.0% |
|          hit | 17,240,272 | 93.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 26.7% |
| Failure | 1,700 | 73.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 520 | 30.6% |
| enumerate | 520 | 30.6% |
| itertools | 400 | 23.5% |
| callable | 260 | 15.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,485,702 | 17.4% |
|          hit | 49,280,643 | 82.0% |
|         miss | 311,724 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,461 | 52.1% |
| Failure | 20,627 | 47.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 4,628 | 22.4% |
| shadowed | 4,292 | 20.8% |
| not managed dict | 3,779 | 18.3% |
| non overriding descriptor | 2,480 | 12.0% |
| has managed dict | 1,120 | 5.4% |
| class attr descriptor | 1,040 | 5.0% |
| metaclass attribute | 960 | 4.7% |
| class method obj | 920 | 4.5% |
| non object slot | 560 | 2.7% |
| class attr simple | 488 | 2.4% |
| mutable class | 280 | 1.4% |
| overridden | 80 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,362 | 0.0% |
|        deopt | 100 | 0.0% |
|          hit | 26,144,019 | 99.9% |
|         miss | 4,424 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,582 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 1,816,346 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 89,364 | 1.9% |
|          hit | 4,333,286 | 92.6% |
|         miss | 245,260 | 5.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,980 | 78.1% |
| Failure | 2,520 | 21.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| property | 1,180 | 46.8% |
| class attr simple | 560 | 22.2% |
| not in keys | 520 | 20.6% |
| no dict | 260 | 10.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 30,339 | 2.3% |
|          hit | 1,293,608 | 97.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 259 | 28.2% |
| Failure | 660 | 71.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 440 | 66.7% |
| other | 220 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,587,777 | 10.7% |
|          hit | 13,237,275 | 89.2% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,003 | 45.0% |
| Failure | 3,666 | 55.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| mapping | 1,087 | 29.7% |
| sequence | 879 | 24.0% |
| set | 740 | 20.2% |
| tuple | 740 | 20.2% |
| other | 220 | 6.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 3,333,225 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 324,678,687 | 56.1% |
| Not specialized | 61,687,655 | 10.7% |
| Specialized hits | 191,369,559 | 33.1% |
| Specialized misses | 576,145 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 11,023,804 | 33.4% |
| LOAD_ATTR | 10,485,702 | 31.8% |
| BINARY_OP | 7,207,848 | 21.9% |
| TO_BOOL | 1,587,777 | 4.8% |
| FOR_ITER | 1,302,940 | 4.0% |
| BINARY_SUBSCR | 636,740 | 1.9% |
| COMPARE_OP | 591,892 | 1.8% |
| STORE_ATTR | 89,364 | 0.3% |
| STORE_SUBSCR | 30,339 | 0.1% |
| LOAD_GLOBAL | 8,362 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 245,260 | 42.6% |
| LOAD_ATTR_INSTANCE_VALUE | 216,194 | 37.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,050 | 14.2% |
| LOAD_ATTR_PROPERTY | 12,380 | 2.1% |
| COMPARE_OP_INT | 6,855 | 1.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,400 | 1.1% |
| LOAD_GLOBAL_MODULE | 4,084 | 0.7% |
| LOAD_ATTR_MODULE | 1,100 | 0.2% |
| CALL_PY_EXACT_ARGS | 580 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 420 | 0.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 11,961,752 | 31.8% |
| Calls to Python functions inlined | 25,612,401 | 68.2% |
| Calls via PyEval_EvalFrame (total) | 11,961,752 | 31.8% |
| Calls via PyEval_EvalFrame (vector) | 11,376,632 | 30.3% |
| Calls via PyEval_EvalFrame (generator) | 585,120 | 1.6% |
| Calls via PyEval_EvalFrame (legacy) | 140 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 11,375,932 | 30.3% |
| Calls via PyEval_EvalFrame (build class) | 560 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 625,920 | 1.7% |
| Calls via PyEval_EvalFrame (function ex) | 535,340 | 1.4% |
| Calls via PyEval_EvalFrame (api) | 641,556 | 1.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 50,115 | 0.1% |
| Frames pushed | 19,010,861 | 50.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 19,445,163 | 41.8% |
| Frees to freelist | 19,457,913 |  |
| Allocations | 27,050,673 | 58.2% |
| Allocations to 512 bytes | 26,765,462 | 57.6% |
| Allocations to 4 kbytes | 117,218 | 0.3% |
| Allocations over 4 kbytes | 167,993 | 0.4% |
| Frees | 28,555,324 |  |
| New values | 88,020 |  |
| Interpreter increfs | 226,547,515 | 76.9% |
| Interpreter decrefs | 248,427,710 | 73.8% |
| Increfs | 68,106,725 | 23.1% |
| Decrefs | 88,007,167 | 26.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 40 | 0.0% |
| Method cache hits | 12,425,239 |  |
| Method cache misses | 40,523 |  |
| Method cache collisions | 75,775 |  |
| Method cache dunder hits | 11,537,634 |  |
| Method cache dunder misses | 39,153 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 600 | 280,224 |
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
| Number of data files | 40 |


</details>

---
Stats gathered on: 2024-09-10
