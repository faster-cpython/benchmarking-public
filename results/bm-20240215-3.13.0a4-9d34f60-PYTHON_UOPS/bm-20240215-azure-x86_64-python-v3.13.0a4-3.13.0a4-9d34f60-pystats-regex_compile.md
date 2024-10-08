
# Pystats results

- benchmark: regex_compile
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 224,345,980 | 20.7% | 20.7% |  |
| STORE_FAST | 67,186,360 | 6.2% | 26.9% |  |
| POP_JUMP_IF_FALSE | 62,269,240 | 5.7% | 32.6% |  |
| LOAD_GLOBAL_MODULE | 57,410,900 | 5.3% | 37.9% |  |
| LOAD_CONST | 53,709,520 | 4.9% | 42.8% |  |
| LOAD_GLOBAL_BUILTIN | 42,488,620 | 3.9% | 46.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 39,299,660 | 3.6% | 50.4% |  |
| RESUME_CHECK | 34,979,540 | 3.2% | 53.6% |  |
| PUSH_NULL | 29,442,720 | 2.7% | 56.3% |  |
| POP_TOP | 28,495,880 | 2.6% | 58.9% |  |
| LOAD_FAST_LOAD_FAST | 26,365,020 | 2.4% | 61.3% |  |
| RETURN_VALUE | 22,455,320 | 2.1% | 63.4% |  |
| CALL_BUILTIN_O | 19,259,120 | 1.8% | 65.2% |  |
| ENTER_EXECUTOR | 18,020,080 | 1.7% | 66.9% |  |
| EXTENDED_ARG | 16,423,820 | 1.5% | 68.4% |  |
| TO_BOOL_BOOL | 15,027,120 | 1.4% | 69.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 14,629,200 | 1.3% | 71.1% |  |
| IS_OP | 13,661,080 | 1.3% | 72.4% |  |
| CONTAINS_OP | 13,569,800 | 1.2% | 73.6% |  |
| RETURN_CONST | 13,171,840 | 1.2% | 74.8% |  |
| POP_JUMP_IF_TRUE | 12,348,280 | 1.1% | 76.0% |  |
| CALL_PY_EXACT_ARGS | 11,932,440 | 1.1% | 77.1% |  |
| CALL_LEN | 11,835,360 | 1.1% | 78.1% |  |
| CALL_ISINSTANCE | 11,211,680 | 1.0% | 79.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 11,107,560 | 1.0% | 80.2% |  |
| TO_BOOL_INT | 10,773,800 | 1.0% | 81.2% |  |
| COMPARE_OP_STR | 10,731,100 | 1.0% | 82.2% | 1.5% |
| BINARY_OP_ADD_INT | 10,336,840 | 1.0% | 83.1% |  |
| BINARY_OP | 10,295,420 | 0.9% | 84.1% |  |
| BINARY_SUBSCR_LIST_INT | 10,134,940 | 0.9% | 85.0% | 12.6% |
| STORE_FAST_STORE_FAST | 9,187,020 | 0.8% | 85.9% |  |
| JUMP_FORWARD | 8,892,040 | 0.8% | 86.7% |  |
| INTERPRETER_EXIT | 7,991,280 | 0.7% | 87.4% |  |
| BUILD_TUPLE | 7,981,400 | 0.7% | 88.2% |  |
| LOAD_ATTR | 7,589,520 | 0.7% | 88.9% |  |
| BINARY_SUBSCR_STR_INT | 6,989,320 | 0.6% | 89.5% | 3.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,739,440 | 0.6% | 90.1% |  |
| FOR_ITER_LIST | 6,576,560 | 0.6% | 90.7% | 0.6% |
| NOP | 6,203,920 | 0.6% | 91.3% |  |
| GET_ITER | 5,982,220 | 0.6% | 91.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,911,040 | 0.5% | 92.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,648,920 | 0.5% | 92.9% |  |
| BINARY_SUBSCR_GETITEM | 5,288,720 | 0.5% | 93.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,910,320 | 0.5% | 93.8% |  |
| CALL_LIST_APPEND | 4,252,400 | 0.4% | 94.2% |  |
| FOR_ITER | 4,223,180 | 0.4% | 94.6% |  |
| BUILD_LIST | 4,059,800 | 0.4% | 95.0% |  |
| POP_JUMP_IF_NOT_NONE | 3,862,160 | 0.4% | 95.4% |  |
| BINARY_OP_SUBTRACT_INT | 3,244,800 | 0.3% | 95.7% |  |
| COPY | 3,039,520 | 0.3% | 95.9% |  |
| FOR_ITER_RANGE | 2,807,500 | 0.3% | 96.2% |  |
| COMPARE_OP_INT | 2,576,340 | 0.2% | 96.4% |  |
| POP_JUMP_IF_NONE | 2,497,600 | 0.2% | 96.7% |  |
| BINARY_SUBSCR_TUPLE_INT | 2,481,880 | 0.2% | 96.9% |  |
| TO_BOOL_NONE | 2,361,480 | 0.2% | 97.1% | 4.8% |
| CALL | 2,144,020 | 0.2% | 97.3% |  |
| TO_BOOL_LIST | 1,926,080 | 0.2% | 97.5% | 0.9% |
| JUMP_BACKWARD | 1,827,180 | 0.2% | 97.7% |  |
| STORE_SUBSCR_LIST_INT | 1,748,420 | 0.2% | 97.8% |  |
| BINARY_SUBSCR | 1,570,420 | 0.1% | 98.0% |  |
| CALL_BUILTIN_CLASS | 1,506,460 | 0.1% | 98.1% |  |
| STORE_FAST_LOAD_FAST | 1,445,760 | 0.1% | 98.2% |  |
| UNARY_NOT | 1,403,120 | 0.1% | 98.4% |  |
| TO_BOOL | 1,354,700 | 0.1% | 98.5% |  |
| BUILD_SLICE | 1,274,480 | 0.1% | 98.6% |  |
| STORE_SUBSCR | 1,213,840 | 0.1% | 98.7% |  |
| LOAD_ATTR_MODULE | 1,112,380 | 0.1% | 98.8% |  |
| COMPARE_OP | 991,620 | 0.1% | 98.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 840,800 | 0.1% | 99.0% |  |
| TO_BOOL_STR | 799,520 | 0.1% | 99.1% | 1.0% |
| BINARY_SUBSCR_DICT | 718,580 | 0.1% | 99.1% |  |
| LOAD_ATTR_PROPERTY | 708,480 | 0.1% | 99.2% |  |
| EXIT_INIT_CHECK | 613,040 | 0.1% | 99.2% |  |
| CALL_ALLOC_AND_ENTER_INIT | 613,040 | 0.1% | 99.3% |  |
| CALL_TYPE_1 | 602,800 | 0.1% | 99.4% |  |
| UNPACK_SEQUENCE_TUPLE | 598,720 | 0.1% | 99.4% |  |
| CHECK_EXC_MATCH | 566,480 | 0.1% | 99.5% |  |
| POP_EXCEPT | 566,480 | 0.1% | 99.5% |  |
| PUSH_EXC_INFO | 566,480 | 0.1% | 99.6% |  |
| CALL_PY_WITH_DEFAULTS | 453,200 | 0.0% | 99.6% |  |
| STORE_SUBSCR_DICT | 449,200 | 0.0% | 99.7% |  |
| BUILD_MAP | 448,880 | 0.0% | 99.7% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 447,840 | 0.0% | 99.7% |  |
| LOAD_ATTR_SLOT | 447,840 | 0.0% | 99.8% |  |
| BINARY_OP_MULTIPLY_INT | 445,040 | 0.0% | 99.8% |  |
| BINARY_SLICE | 338,640 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 293,680 | 0.0% | 99.9% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 292,960 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 226,100 | 0.0% | 99.9% |  |
| CALL_TUPLE_1 | 223,920 | 0.0% | 99.9% |  |
| UNARY_INVERT | 162,800 | 0.0% | 100.0% |  |
| SWAP | 107,200 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 79,840 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 52,420 | 0.0% | 100.0% | 100.0% |
| STORE_SLICE | 46,240 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 33,840 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 32,800 | 0.0% | 100.0% |  |
| LIST_APPEND | 32,800 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 32,800 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 14,640 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 3,780 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 540 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| RESUME | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| POP_JUMP_IF_FALSE LOAD_FAST | 53,149,200 | 4.9% | 4.9% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 35,160,560 | 3.2% | 8.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 33,317,160 | 3.1% | 11.2% |
| STORE_FAST LOAD_FAST | 29,465,480 | 2.7% | 13.9% |
| LOAD_FAST PUSH_NULL | 27,100,080 | 2.5% | 16.4% |
| LOAD_FAST LOAD_CONST | 24,201,200 | 2.2% | 18.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 22,530,940 | 2.1% | 20.7% |
| PUSH_NULL LOAD_FAST | 16,151,420 | 1.5% | 22.2% |
| CALL_BUILTIN_O POP_TOP | 15,651,560 | 1.4% | 23.6% |
| POP_TOP LOAD_FAST | 15,124,020 | 1.4% | 25.0% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 14,760,280 | 1.4% | 26.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 13,562,360 | 1.2% | 27.7% |
| LOAD_GLOBAL_MODULE IS_OP | 13,196,680 | 1.2% | 28.9% |
| RESUME_CHECK LOAD_FAST | 13,085,600 | 1.2% | 30.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 12,323,040 | 1.1% | 31.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,932,440 | 1.1% | 32.3% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 10,645,840 | 1.0% | 33.3% |
| LOAD_FAST CALL_BUILTIN_O | 10,596,620 | 1.0% | 34.3% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 10,539,920 | 1.0% | 35.2% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 10,040,160 | 0.9% | 36.2% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 9,974,080 | 0.9% | 37.1% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 9,949,420 | 0.9% | 38.0% |
| IS_OP POP_JUMP_IF_FALSE | 9,938,980 | 0.9% | 38.9% |
| LOAD_CONST BINARY_OP_ADD_INT | 9,722,760 | 0.9% | 39.8% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 9,361,520 | 0.9% | 40.7% |
| CACHE RESUME_CHECK | 9,244,080 | 0.9% | 41.5% |
| LOAD_CONST COMPARE_OP_STR | 8,798,040 | 0.8% | 42.3% |
| LOAD_GLOBAL_MODULE CONTAINS_OP | 8,660,760 | 0.8% | 43.1% |
| LOAD_GLOBAL_MODULE BINARY_OP | 8,594,480 | 0.8% | 43.9% |
| RETURN_CONST POP_TOP | 8,535,480 | 0.8% | 44.7% |
| BINARY_SUBSCR_LIST_INT RETURN_VALUE | 8,423,200 | 0.8% | 45.5% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 7,724,120 | 0.7% | 46.2% |
| LOAD_FAST LOAD_ATTR | 7,534,360 | 0.7% | 46.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 7,437,320 | 0.7% | 47.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 7,338,040 | 0.7% | 48.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 7,214,580 | 0.7% | 48.9% |
| BINARY_OP TO_BOOL_INT | 7,038,640 | 0.6% | 49.6% |
| LOAD_FAST CALL_LEN | 6,895,840 | 0.6% | 50.2% |
| LOAD_ATTR STORE_FAST | 6,860,440 | 0.6% | 50.8% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 6,739,440 | 0.6% | 51.4% |
| BINARY_OP_ADD_INT STORE_FAST | 6,724,320 | 0.6% | 52.1% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 6,672,360 | 0.6% | 52.7% |
| LOAD_CONST STORE_FAST | 6,635,140 | 0.6% | 53.3% |
| RETURN_VALUE INTERPRETER_EXIT | 6,444,320 | 0.6% | 53.9% |
| STORE_FAST LOAD_CONST | 6,441,640 | 0.6% | 54.5% |
| LOAD_GLOBAL_MODULE STORE_FAST | 6,364,160 | 0.6% | 55.1% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 6,103,280 | 0.6% | 55.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 6,087,160 | 0.6% | 56.2% |
| PUSH_NULL LOAD_GLOBAL_MODULE | 5,886,060 | 0.5% | 56.7% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 5,825,360 | 0.5% | 57.3% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 5,820,300 | 0.5% | 57.8% |
| NOP LOAD_FAST | 5,389,440 | 0.5% | 58.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 5,352,580 | 0.5% | 58.8% |
| BINARY_SUBSCR_GETITEM RESUME_CHECK | 5,288,720 | 0.5% | 59.3% |
| ENTER_EXECUTOR EXTENDED_ARG | 5,271,660 | 0.5% | 59.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 5,236,160 | 0.5% | 60.2% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 5,111,160 | 0.5% | 60.7% |
| STORE_FAST NOP | 5,026,120 | 0.5% | 61.2% |
| EXTENDED_ARG JUMP_FORWARD | 4,933,360 | 0.5% | 61.6% |
| STORE_FAST STORE_FAST | 4,756,320 | 0.4% | 62.1% |
| POP_TOP ENTER_EXECUTOR | 4,733,140 | 0.4% | 62.5% |
| STORE_FAST_STORE_FAST LOAD_FAST | 4,679,420 | 0.4% | 62.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 4,645,320 | 0.4% | 63.4% |
| TO_BOOL_INT POP_JUMP_IF_TRUE | 4,541,320 | 0.4% | 63.8% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 4,510,360 | 0.4% | 64.2% |
| JUMP_FORWARD ENTER_EXECUTOR | 4,509,000 | 0.4% | 64.6% |
| EXTENDED_ARG POP_JUMP_IF_FALSE | 4,420,480 | 0.4% | 65.0% |
| LOAD_FAST RETURN_VALUE | 4,419,000 | 0.4% | 65.4% |
| ENTER_EXECUTOR LOAD_FAST | 4,248,860 | 0.4% | 65.8% |
| PUSH_NULL LOAD_CONST | 4,241,360 | 0.4% | 66.2% |
| STORE_FAST ENTER_EXECUTOR | 4,163,780 | 0.4% | 66.6% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 3,935,120 | 0.4% | 67.0% |
| LOAD_GLOBAL_BUILTIN STORE_FAST | 3,914,880 | 0.4% | 67.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 3,862,160 | 0.4% | 67.7% |
| LOAD_CONST BINARY_SUBSCR_STR_INT | 3,856,360 | 0.4% | 68.0% |
| EXTENDED_ARG FOR_ITER | 3,769,680 | 0.3% | 68.4% |
| BINARY_SUBSCR_STR_INT LOAD_CONST | 3,719,720 | 0.3% | 68.7% |
| IS_OP POP_JUMP_IF_TRUE | 3,705,540 | 0.3% | 69.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 3,695,080 | 0.3% | 69.4% |
| CALL_LEN RETURN_VALUE | 3,683,280 | 0.3% | 69.7% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 3,683,280 | 0.3% | 70.1% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST | 3,670,240 | 0.3% | 70.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 3,660,960 | 0.3% | 70.8% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 3,647,720 | 0.3% | 71.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 3,602,000 | 0.3% | 71.4% |
| CALL_LIST_APPEND RETURN_CONST | 3,573,680 | 0.3% | 71.8% |
| LOAD_FAST CALL_LIST_APPEND | 3,565,000 | 0.3% | 72.1% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 3,534,340 | 0.3% | 72.4% |
| LOAD_FAST LOAD_FAST | 3,515,200 | 0.3% | 72.7% |
| BUILD_LIST STORE_FAST | 3,470,040 | 0.3% | 73.1% |
| CONTAINS_OP EXTENDED_ARG | 3,377,680 | 0.3% | 73.4% |
| LOAD_FAST TO_BOOL_INT | 3,369,400 | 0.3% | 73.7% |
| EXTENDED_ARG FOR_ITER_LIST | 3,298,840 | 0.3% | 74.0% |
| POP_TOP EXTENDED_ARG | 3,268,480 | 0.3% | 74.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 3,226,440 | 0.3% | 74.6% |
| BUILD_TUPLE CALL_BOUND_METHOD_EXACT_ARGS | 3,196,280 | 0.3% | 74.9% |
| BINARY_OP_ADD_INT LOAD_FAST | 3,185,720 | 0.3% | 75.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 3,115,220 | 0.3% | 75.5% |
| CALL_BUILTIN_O BUILD_TUPLE | 3,115,160 | 0.3% | 75.7% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 3,103,600 | 0.3% | 76.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 304,800 | 90.0% |
| LOAD_FAST | 32,800 | 9.7% |
| BINARY_OP_ADD_INT | 1,040 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 304,560 | 89.9% |
| LOAD_CONST | 33,840 | 10.0% |
| CALL_BUILTIN_CLASS | 240 | 0.1% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 45,200 | 97.8% |
| LOAD_CONST | 1,040 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 45,200 | 97.8% |
| LOAD_FAST | 1,040 | 2.2% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,244,080 | 100.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 289,520 | 98.8% |
| RETURN_VALUE | 1,340 | 0.5% |
| ENTER_EXECUTOR | 1,040 | 0.4% |
| LOAD_FAST_LOAD_FAST | 1,040 | 0.4% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 291,920 | 99.6% |
| LOAD_GLOBAL_BUILTIN | 1,040 | 0.4% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 1,274,480 | 81.2% |
| LOAD_FAST | 165,200 | 10.5% |
| LOAD_CONST | 130,100 | 8.3% |
| BINARY_SUBSCR | 640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,241,680 | 79.1% |
| CALL_ALLOC_AND_ENTER_INIT | 165,200 | 10.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 130,080 | 8.3% |
| STORE_FAST | 32,800 | 2.1% |
| BINARY_SUBSCR | 640 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 566,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 566,480 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,720 | 72.0% |
| LOAD_CONST | 1,060 | 28.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,720 | 72.0% |
| ENTER_EXECUTOR | 1,020 | 27.0% |
| JUMP_BACKWARD | 40 | 1.1% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 613,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 613,040 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,222,180 | 37.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,908,160 | 31.9% |
| BINARY_SUBSCR | 1,241,680 | 20.8% |
| BINARY_SUBSCR_TUPLE_INT | 235,560 | 3.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 223,920 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 3,035,840 | 50.7% |
| FOR_ITER_RANGE | 1,384,380 | 23.1% |
| FOR_ITER_LIST | 1,072,440 | 17.9% |
| FOR_ITER | 449,160 | 7.5% |
| LOAD_FAST_AND_CLEAR | 32,800 | 0.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 6,444,320 | 80.6% |
| RETURN_CONST | 1,546,960 | 19.4% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,026,120 | 81.0% |
| POP_JUMP_IF_FALSE | 501,600 | 8.1% |
| NOP | 173,260 | 2.8% |
| STORE_FAST_STORE_FAST | 173,120 | 2.8% |
| CALL_LIST_APPEND | 120,960 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,389,440 | 86.9% |
| LOAD_FAST_LOAD_FAST | 289,520 | 4.7% |
| NOP | 173,260 | 2.8% |
| ENTER_EXECUTOR | 120,960 | 1.9% |
| LOAD_CONST | 92,340 | 1.5% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,520 | 60.3% |
| STORE_ATTR_INSTANCE_VALUE | 223,920 | 39.5% |
| STORE_FAST | 1,040 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 341,520 | 60.3% |
| RETURN_CONST | 223,920 | 39.5% |
| ENTER_EXECUTOR | 880 | 0.2% |
| EXTENDED_ARG | 160 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 15,651,560 | 54.9% |
| RETURN_CONST | 8,535,480 | 30.0% |
| RETURN_VALUE | 1,839,320 | 6.5% |
| POP_JUMP_IF_FALSE | 1,083,340 | 3.8% |
| ENTER_EXECUTOR | 773,220 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,124,020 | 53.1% |
| ENTER_EXECUTOR | 4,733,140 | 16.6% |
| EXTENDED_ARG | 3,268,480 | 11.5% |
| LOAD_GLOBAL_MODULE | 1,571,960 | 5.5% |
| RETURN_CONST | 1,562,880 | 5.5% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 304,160 | 53.7% |
| BINARY_SUBSCR_STR_INT | 223,920 | 39.5% |
| BINARY_SUBSCR_DICT | 37,360 | 6.6% |
| STORE_SUBSCR | 1,040 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 566,480 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,100,080 | 92.0% |
| STORE_FAST_LOAD_FAST | 1,445,760 | 4.9% |
| LOAD_ATTR_MODULE | 896,620 | 3.0% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,151,420 | 54.9% |
| LOAD_GLOBAL_MODULE | 5,886,060 | 20.0% |
| LOAD_CONST | 4,241,360 | 14.4% |
| LOAD_FAST_LOAD_FAST | 1,668,400 | 5.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,387,860 | 4.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 8,423,200 | 37.5% |
| LOAD_FAST | 4,419,000 | 19.7% |
| CALL_LEN | 3,683,280 | 16.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,598,240 | 7.1% |
| BINARY_OP_SUBTRACT_INT | 808,400 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 6,444,320 | 28.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,103,280 | 27.2% |
| STORE_FAST | 3,086,720 | 13.7% |
| POP_TOP | 1,839,320 | 8.2% |
| CALL_BUILTIN_O | 1,241,680 | 5.5% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 834,840 | 68.8% |
| LOAD_FAST | 210,400 | 17.3% |
| LOAD_CONST | 165,200 | 13.6% |
| BINARY_OP | 2,640 | 0.2% |
| STORE_SUBSCR | 760 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 797,520 | 65.7% |
| RETURN_CONST | 210,400 | 17.3% |
| EXTENDED_ARG | 165,200 | 13.6% |
| ENTER_EXECUTOR | 35,380 | 2.9% |
| LOAD_FAST | 1,840 | 0.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 844,080 | 62.3% |
| BINARY_OP | 223,920 | 16.5% |
| LOAD_ATTR | 223,920 | 16.5% |
| ENTER_EXECUTOR | 57,080 | 4.2% |
| TO_BOOL | 4,020 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,054,440 | 77.8% |
| POP_JUMP_IF_TRUE | 294,540 | 21.7% |
| TO_BOOL | 4,020 | 0.3% |
| TO_BOOL_NONE | 1,620 | 0.1% |
| TO_BOOL_BOOL | 40 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 162,800 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 32,800 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_LIST | 996,000 | 71.0% |
| TO_BOOL_INT | 407,120 | 29.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 996,000 | 71.0% |
| COPY | 407,120 | 29.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 8,594,480 | 83.5% |
| LOAD_FAST_LOAD_FAST | 731,440 | 7.1% |
| LOAD_FAST | 234,120 | 2.3% |
| RETURN_VALUE | 224,980 | 2.2% |
| LOAD_ATTR_INSTANCE_VALUE | 223,920 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 7,038,640 | 68.4% |
| STORE_FAST | 1,827,040 | 17.7% |
| LOAD_FAST | 387,760 | 3.8% |
| TO_BOOL | 223,920 | 2.2% |
| CALL | 223,920 | 2.2% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 1,333,840 | 32.9% |
| RESUME_CHECK | 833,280 | 20.5% |
| STORE_FAST | 664,000 | 16.4% |
| LOAD_CONST | 554,800 | 13.7% |
| POP_JUMP_IF_FALSE | 288,840 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,470,040 | 85.5% |
| LOAD_FAST | 447,840 | 11.0% |
| LOAD_GLOBAL_BUILTIN | 106,960 | 2.6% |
| SWAP | 32,800 | 0.8% |
| CALL_METHOD_DESCRIPTOR_O | 1,040 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 447,840 | 99.8% |
| STORE_FAST | 1,040 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 447,840 | 99.8% |
| STORE_FAST | 1,040 | 0.2% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,274,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,274,480 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 3,115,160 | 39.0% |
| LOAD_FAST_LOAD_FAST | 1,440,160 | 18.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,431,200 | 17.9% |
| LOAD_FAST | 662,480 | 8.3% |
| BUILD_TUPLE | 495,120 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 3,196,280 | 40.0% |
| LOAD_FAST | 1,596,400 | 20.0% |
| CALL_BUILTIN_O | 806,880 | 10.1% |
| RETURN_VALUE | 564,480 | 7.1% |
| BUILD_TUPLE | 495,120 | 6.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,563,620 | 72.9% |
| BINARY_OP | 223,920 | 10.4% |
| ENTER_EXECUTOR | 179,440 | 8.4% |
| LOAD_CONST | 174,280 | 8.1% |
| CALL | 1,220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,917,300 | 89.4% |
| RETURN_VALUE | 223,920 | 10.4% |
| CALL | 1,220 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,040 | 0.0% |
| POP_TOP | 140 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 80 | 50.0% |
| LOAD_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 50.0% |
| RESUME_CHECK | 60 | 37.5% |
| RESUME | 20 | 12.5% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 670,720 | 67.6% |
| LOAD_FAST | 178,340 | 18.0% |
| LOAD_ATTR_INSTANCE_VALUE | 135,380 | 13.7% |
| COMPARE_OP | 4,020 | 0.4% |
| COMPARE_OP_STR | 3,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 777,060 | 78.4% |
| POP_JUMP_IF_TRUE | 207,360 | 20.9% |
| COMPARE_OP | 4,020 | 0.4% |
| COMPARE_OP_STR | 3,160 | 0.3% |
| COMPARE_OP_INT | 20 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 8,660,760 | 63.8% |
| LOAD_FAST_LOAD_FAST | 3,647,720 | 26.9% |
| LOAD_CONST | 1,260,280 | 9.3% |
| LOAD_FAST | 1,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,040,160 | 74.0% |
| EXTENDED_ARG | 3,377,680 | 24.9% |
| RETURN_VALUE | 141,680 | 1.0% |
| POP_JUMP_IF_TRUE | 10,280 | 0.1% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,431,520 | 47.1% |
| LOAD_ATTR_INSTANCE_VALUE | 808,400 | 26.6% |
| UNARY_NOT | 407,120 | 13.4% |
| LOAD_FAST | 193,040 | 6.4% |
| BINARY_OP | 182,880 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,431,200 | 47.1% |
| TO_BOOL_STR | 798,720 | 26.3% |
| TO_BOOL_BOOL | 423,680 | 13.9% |
| TO_BOOL_INT | 365,760 | 12.0% |
| TO_BOOL_NONE | 9,680 | 0.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,733,140 | 26.3% |
| JUMP_FORWARD | 4,509,000 | 25.0% |
| STORE_FAST | 4,163,780 | 23.1% |
| POP_JUMP_IF_TRUE | 3,534,340 | 19.6% |
| STORE_SUBSCR_LIST_INT | 459,140 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 5,271,660 | 29.3% |
| LOAD_FAST | 4,248,860 | 23.6% |
| BINARY_SUBSCR_GETITEM | 2,998,800 | 16.6% |
| POP_JUMP_IF_FALSE | 1,858,640 | 10.3% |
| FOR_ITER_RANGE | 1,390,240 | 7.7% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,271,660 | 32.1% |
| CONTAINS_OP | 3,377,680 | 20.6% |
| POP_TOP | 3,268,480 | 19.9% |
| GET_ITER | 3,035,840 | 18.5% |
| COMPARE_OP_STR | 778,560 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 4,933,360 | 30.0% |
| POP_JUMP_IF_FALSE | 4,420,480 | 26.9% |
| FOR_ITER | 3,769,680 | 23.0% |
| FOR_ITER_LIST | 3,298,840 | 20.1% |
| JUMP_BACKWARD | 1,460 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 3,769,680 | 89.3% |
| GET_ITER | 449,160 | 10.6% |
| FOR_ITER | 3,340 | 0.1% |
| FOR_ITER_LIST | 760 | 0.0% |
| JUMP_BACKWARD | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,741,760 | 64.9% |
| RETURN_CONST | 1,027,920 | 24.3% |
| LOAD_FAST | 223,920 | 5.3% |
| LOAD_GLOBAL_MODULE | 223,920 | 5.3% |
| FOR_ITER | 3,340 | 0.1% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 13,196,680 | 96.6% |
| LOAD_FAST | 223,920 | 1.6% |
| LOAD_GLOBAL_BUILTIN | 223,920 | 1.6% |
| LOAD_CONST | 16,560 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,938,980 | 72.8% |
| POP_JUMP_IF_TRUE | 3,705,540 | 27.1% |
| COPY | 16,320 | 0.1% |
| RETURN_VALUE | 240 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 912,000 | 49.9% |
| STORE_SUBSCR_LIST_INT | 912,000 | 49.9% |
| EXTENDED_ARG | 1,460 | 0.1% |
| POP_TOP | 800 | 0.0% |
| STORE_SUBSCR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,824,700 | 99.9% |
| EXTENDED_ARG | 840 | 0.0% |
| NOP | 700 | 0.0% |
| ENTER_EXECUTOR | 300 | 0.0% |
| FOR_ITER | 240 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 4,933,360 | 55.5% |
| POP_TOP | 1,094,320 | 12.3% |
| STORE_FAST | 951,920 | 10.7% |
| STORE_SUBSCR | 797,520 | 9.0% |
| POP_JUMP_IF_TRUE | 407,280 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,509,000 | 50.7% |
| LOAD_GLOBAL_BUILTIN | 2,097,280 | 23.6% |
| LOAD_FAST | 1,599,440 | 18.0% |
| LOAD_GLOBAL_MODULE | 381,800 | 4.3% |
| LOAD_FAST_LOAD_FAST | 212,080 | 2.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 32,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 32,800 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 80 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,534,360 | 99.3% |
| LOAD_GLOBAL_BUILTIN | 51,440 | 0.7% |
| LOAD_ATTR | 3,040 | 0.0% |
| LOAD_GLOBAL_MODULE | 520 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,860,440 | 90.4% |
| LOAD_FAST | 275,360 | 3.6% |
| TO_BOOL | 223,920 | 3.0% |
| LOAD_FAST_LOAD_FAST | 223,920 | 3.0% |
| LOAD_ATTR | 3,040 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,201,200 | 45.1% |
| STORE_FAST | 6,441,640 | 12.0% |
| PUSH_NULL | 4,241,360 | 7.9% |
| BINARY_SUBSCR_STR_INT | 3,719,720 | 6.9% |
| LOAD_CONST | 2,858,960 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 9,722,760 | 18.1% |
| COMPARE_OP_STR | 8,798,040 | 16.4% |
| STORE_FAST | 6,635,140 | 12.4% |
| BINARY_SUBSCR_STR_INT | 3,856,360 | 7.2% |
| LOAD_FAST | 3,026,320 | 5.6% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 33.3% |
| BUILD_LIST | 80 | 33.3% |
| RESUME_CHECK | 60 | 25.0% |
| RESUME | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 160 | 66.7% |
| LIST_EXTEND | 80 | 33.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 53,149,200 | 23.7% |
| STORE_FAST | 29,465,480 | 13.1% |
| LOAD_GLOBAL_BUILTIN | 22,530,940 | 10.0% |
| PUSH_NULL | 16,151,420 | 7.2% |
| POP_TOP | 15,124,020 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 35,160,560 | 15.7% |
| LOAD_GLOBAL_MODULE | 33,317,160 | 14.9% |
| PUSH_NULL | 27,100,080 | 12.1% |
| LOAD_CONST | 24,201,200 | 10.8% |
| LOAD_GLOBAL_BUILTIN | 10,645,840 | 4.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 32,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 32,800 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 79,840 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 79,840 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,935,120 | 14.9% |
| LOAD_GLOBAL_MODULE | 3,660,960 | 13.9% |
| STORE_ATTR_INSTANCE_VALUE | 3,226,440 | 12.2% |
| STORE_FAST_STORE_FAST | 3,103,600 | 11.8% |
| LOAD_GLOBAL_BUILTIN | 2,273,680 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 6,672,360 | 25.3% |
| CONTAINS_OP | 3,647,720 | 13.8% |
| LOAD_ATTR_INSTANCE_VALUE | 3,010,400 | 11.4% |
| LOAD_FAST | 2,334,720 | 8.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,824,000 | 6.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 120 | 22.2% |
| RETURN_VALUE | 40 | 7.4% |
| LOAD_FAST | 40 | 7.4% |
| POP_JUMP_IF_FALSE | 40 | 7.4% |
| STORE_FAST | 40 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 300 | 55.6% |
| LOAD_ATTR | 160 | 29.6% |
| LOAD_GLOBAL_BUILTIN | 60 | 11.1% |
| LOAD_FAST | 20 | 3.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 12,323,040 | 19.8% |
| CONTAINS_OP | 10,040,160 | 16.1% |
| COMPARE_OP_STR | 9,949,420 | 16.0% |
| IS_OP | 9,938,980 | 16.0% |
| TO_BOOL_INT | 5,825,360 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,149,200 | 85.4% |
| LOAD_GLOBAL_MODULE | 2,502,640 | 4.0% |
| LOAD_CONST | 1,156,900 | 1.9% |
| POP_TOP | 1,083,340 | 1.7% |
| LOAD_FAST_LOAD_FAST | 1,025,280 | 1.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,822,400 | 73.0% |
| LOAD_FAST | 675,200 | 27.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,431,200 | 57.3% |
| LOAD_FAST | 889,440 | 35.6% |
| ENTER_EXECUTOR | 113,760 | 4.6% |
| LOAD_GLOBAL_BUILTIN | 62,960 | 2.5% |
| RETURN_CONST | 240 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,862,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,610,620 | 41.7% |
| BUILD_LIST | 1,333,840 | 34.5% |
| LOAD_GLOBAL_BUILTIN | 421,360 | 10.9% |
| LOAD_GLOBAL_MODULE | 223,920 | 5.8% |
| LOAD_FAST_LOAD_FAST | 165,200 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 4,541,320 | 36.8% |
| IS_OP | 3,705,540 | 30.0% |
| TO_BOOL_BOOL | 2,439,840 | 19.8% |
| TO_BOOL_STR | 798,720 | 6.5% |
| TO_BOOL_LIST | 338,920 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,087,160 | 49.3% |
| ENTER_EXECUTOR | 3,534,340 | 28.6% |
| CALL_LEN | 799,040 | 6.5% |
| JUMP_FORWARD | 407,280 | 3.3% |
| LOAD_GLOBAL_MODULE | 387,840 | 3.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 4,510,360 | 34.2% |
| CALL_LIST_APPEND | 3,573,680 | 27.1% |
| POP_TOP | 1,562,880 | 11.9% |
| FOR_ITER | 1,027,920 | 7.8% |
| POP_JUMP_IF_FALSE | 982,240 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,535,480 | 64.8% |
| TO_BOOL_BOOL | 2,025,720 | 15.4% |
| INTERPRETER_EXIT | 1,546,960 | 11.7% |
| EXIT_INIT_CHECK | 613,040 | 4.7% |
| STORE_FAST | 450,600 | 3.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 6,860,440 | 10.2% |
| BINARY_OP_ADD_INT | 6,724,320 | 10.0% |
| LOAD_CONST | 6,635,140 | 9.9% |
| LOAD_GLOBAL_MODULE | 6,364,160 | 9.5% |
| LOAD_ATTR_INSTANCE_VALUE | 5,820,300 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,465,480 | 43.9% |
| LOAD_GLOBAL_MODULE | 7,338,040 | 10.9% |
| LOAD_CONST | 6,441,640 | 9.6% |
| LOAD_GLOBAL_BUILTIN | 5,236,160 | 7.8% |
| NOP | 5,026,120 | 7.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,445,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,445,760 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 7,437,320 | 81.0% |
| COPY | 1,431,200 | 15.6% |
| UNPACK_SEQUENCE_TUPLE | 285,760 | 3.1% |
| STORE_FAST_STORE_FAST | 32,720 | 0.4% |
| UNPACK_SEQUENCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,679,420 | 50.9% |
| LOAD_FAST_LOAD_FAST | 3,103,600 | 33.8% |
| LOAD_GLOBAL_BUILTIN | 912,000 | 9.9% |
| STORE_FAST | 253,040 | 2.8% |
| NOP | 173,120 | 1.9% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 32,800 | 30.6% |
| LOAD_FAST_AND_CLEAR | 32,800 | 30.6% |
| FOR_ITER_RANGE | 32,800 | 30.6% |
| BINARY_OP | 8,800 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 32,800 | 30.6% |
| STORE_FAST | 32,800 | 30.6% |
| FOR_ITER_RANGE | 32,800 | 30.6% |
| STORE_ATTR_INSTANCE_VALUE | 8,800 | 8.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 20 | 50.0% |
| FOR_ITER_LIST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 20 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 33.3% |
| CALL_FUNCTION_EX | 20 | 33.3% |
| COPY_FREE_VARS | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 66.7% |
| LOAD_DEREF | 20 | 33.3% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,722,760 | 94.1% |
| LOAD_FAST_LOAD_FAST | 430,240 | 4.2% |
| BINARY_OP_MULTIPLY_INT | 183,840 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,724,320 | 65.1% |
| LOAD_FAST | 3,185,720 | 30.8% |
| CALL_PY_EXACT_ARGS | 183,200 | 1.8% |
| CALL_BUILTIN_O | 130,080 | 1.3% |
| STORE_SLICE | 45,200 | 0.4% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 260,160 | 58.5% |
| BINARY_SUBSCR_TUPLE_INT | 183,840 | 41.3% |
| LOAD_ATTR | 1,040 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 183,840 | 41.3% |
| LOAD_CONST | 130,080 | 29.2% |
| CALL_BUILTIN_O | 130,080 | 29.2% |
| LOAD_GLOBAL_BUILTIN | 1,040 | 0.2% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| BINARY_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,595,360 | 49.2% |
| LOAD_CONST | 841,040 | 25.9% |
| CALL_LEN | 808,400 | 24.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,445,760 | 44.6% |
| RETURN_VALUE | 808,400 | 24.9% |
| LOAD_FAST | 341,520 | 10.5% |
| LOAD_CONST | 292,160 | 9.0% |
| STORE_FAST | 236,080 | 7.3% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 484,500 | 67.4% |
| LOAD_FAST_LOAD_FAST | 196,720 | 27.4% |
| BUILD_TUPLE | 37,360 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 250,500 | 34.9% |
| RETURN_VALUE | 223,920 | 31.2% |
| LOAD_CONST | 189,120 | 26.3% |
| PUSH_EXC_INFO | 37,360 | 5.2% |
| STORE_FAST | 8,800 | 1.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 2,998,800 | 56.7% |
| LOAD_FAST | 1,240,080 | 23.4% |
| LOAD_CONST | 1,049,840 | 19.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,288,720 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,361,520 | 92.4% |
| LOAD_CONST | 486,020 | 4.8% |
| LOAD_FAST_LOAD_FAST | 175,520 | 1.7% |
| BINARY_OP_SUBTRACT_INT | 87,760 | 0.9% |
| BINARY_SUBSCR_LIST_INT | 24,100 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,423,200 | 94.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 116,280 | 1.3% |
| STORE_FAST | 94,720 | 1.1% |
| LOAD_FAST_LOAD_FAST | 87,760 | 1.0% |
| COMPARE_OP_INT | 87,760 | 1.0% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,856,360 | 55.2% |
| LOAD_FAST | 3,031,000 | 43.4% |
| ENTER_EXECUTOR | 97,600 | 1.4% |
| BINARY_SUBSCR_STR_INT | 4,360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,719,720 | 53.2% |
| STORE_FAST | 2,614,760 | 37.4% |
| BINARY_OP_INPLACE_ADD_UNICODE | 289,520 | 4.1% |
| PUSH_EXC_INFO | 223,920 | 3.2% |
| CALL_BUILTIN_O | 137,040 | 2.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,481,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 805,920 | 32.5% |
| CALL_BUILTIN_O | 585,280 | 23.6% |
| GET_ITER | 235,560 | 9.5% |
| LOAD_FAST | 200,400 | 8.1% |
| BINARY_OP_MULTIPLY_INT | 183,840 | 7.4% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,920 | 36.5% |
| LOAD_GLOBAL_MODULE | 223,920 | 36.5% |
| BINARY_SUBSCR | 165,200 | 26.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 613,040 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 3,196,280 | 47.4% |
| LOAD_CONST | 1,879,720 | 27.9% |
| PUSH_NULL | 1,387,860 | 20.6% |
| LOAD_FAST | 275,200 | 4.1% |
| BINARY_SUBSCR_LIST_INT | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,739,440 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,348,640 | 89.5% |
| CALL_BUILTIN_FAST | 51,440 | 3.4% |
| LOAD_CONST | 34,880 | 2.3% |
| BINARY_OP_ADD_INT | 34,880 | 2.3% |
| UNARY_NEGATIVE | 32,800 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,241,680 | 82.4% |
| GET_ITER | 143,120 | 9.5% |
| RETURN_VALUE | 51,440 | 3.4% |
| STORE_FAST | 35,820 | 2.4% |
| LIST_APPEND | 32,800 | 2.2% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,440 | 98.1% |
| CALL_BUILTIN_FAST | 980 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 51,440 | 98.1% |
| CALL_BUILTIN_FAST | 980 | 1.9% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,862,400 | 58.3% |
| LOAD_FAST_LOAD_FAST | 1,824,000 | 37.1% |
| CALL_TUPLE_1 | 223,920 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,824,000 | 37.1% |
| BUILD_TUPLE | 1,431,200 | 29.1% |
| LOAD_GLOBAL_BUILTIN | 1,431,200 | 29.1% |
| RETURN_VALUE | 223,920 | 4.6% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,596,620 | 55.0% |
| LOAD_CONST | 2,361,600 | 12.3% |
| LOAD_GLOBAL_MODULE | 1,999,600 | 10.4% |
| RETURN_VALUE | 1,241,680 | 6.4% |
| CALL_LEN | 1,018,960 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 15,651,560 | 81.3% |
| BUILD_TUPLE | 3,115,160 | 16.2% |
| TO_BOOL_BOOL | 355,680 | 1.8% |
| STORE_FAST | 136,720 | 0.7% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 9,974,080 | 89.0% |
| BUILD_TUPLE | 447,840 | 4.0% |
| LOAD_GLOBAL_MODULE | 341,920 | 3.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 223,920 | 2.0% |
| LOAD_ATTR_SLOT | 223,920 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 10,539,920 | 94.0% |
| RETURN_VALUE | 447,840 | 4.0% |
| LOAD_FAST | 223,920 | 2.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,895,840 | 58.3% |
| LOAD_ATTR_INSTANCE_VALUE | 3,683,280 | 31.1% |
| POP_JUMP_IF_TRUE | 799,040 | 6.8% |
| LOAD_GLOBAL_MODULE | 447,840 | 3.8% |
| LOAD_CONST | 9,360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,683,280 | 31.1% |
| LOAD_FAST | 1,531,600 | 12.9% |
| STORE_FAST_LOAD_FAST | 1,445,760 | 12.2% |
| CALL_BUILTIN_CLASS | 1,348,640 | 11.4% |
| LOAD_CONST | 1,052,240 | 8.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,565,000 | 83.8% |
| BUILD_TUPLE | 307,920 | 7.2% |
| LOAD_GLOBAL_MODULE | 223,920 | 5.3% |
| LOAD_CONST | 130,080 | 3.1% |
| ENTER_EXECUTOR | 25,480 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,573,680 | 84.0% |
| LOAD_FAST | 354,000 | 8.3% |
| ENTER_EXECUTOR | 168,320 | 4.0% |
| NOP | 120,960 | 2.8% |
| LOAD_FAST_LOAD_FAST | 32,800 | 0.8% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 436,160 | 51.9% |
| LOAD_CONST | 341,520 | 40.6% |
| LOAD_FAST_LOAD_FAST | 60,560 | 7.2% |
| BUILD_TUPLE | 2,560 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 838,240 | 99.7% |
| POP_TOP | 2,560 | 0.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 32,800 | 96.9% |
| LOAD_CONST | 1,040 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 32,800 | 96.9% |
| STORE_FAST | 1,040 | 3.1% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 225,680 | 99.8% |
| LOAD_ATTR | 360 | 0.2% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 223,920 | 99.0% |
| POP_TOP | 1,140 | 0.5% |
| RETURN_VALUE | 1,040 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 185,680 | 63.2% |
| RETURN_VALUE | 106,960 | 36.4% |
| BUILD_LIST | 1,040 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 293,680 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 5,111,160 | 42.8% |
| LOAD_FAST | 3,115,220 | 26.1% |
| LOAD_FAST_LOAD_FAST | 1,334,920 | 11.2% |
| UNARY_NOT | 996,000 | 8.3% |
| LOAD_CONST | 406,800 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,932,440 | 100.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 229,280 | 50.6% |
| LOAD_FAST_LOAD_FAST | 223,920 | 49.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 453,200 | 100.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 223,920 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 602,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 378,880 | 62.9% |
| LOAD_FAST | 223,920 | 37.1% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,738,420 | 67.5% |
| LOAD_GLOBAL_MODULE | 577,920 | 22.4% |
| CALL_LEN | 141,360 | 5.5% |
| BINARY_SUBSCR_LIST_INT | 87,760 | 3.4% |
| LOAD_FAST | 29,340 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,574,020 | 99.9% |
| POP_JUMP_IF_TRUE | 2,080 | 0.1% |
| COPY | 240 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,798,040 | 82.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,927,260 | 18.0% |
| COMPARE_OP | 3,160 | 0.0% |
| LOAD_FAST | 2,640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,949,420 | 92.7% |
| EXTENDED_ARG | 778,560 | 7.3% |
| COMPARE_OP | 3,120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 3,298,840 | 50.2% |
| JUMP_BACKWARD | 1,824,700 | 27.7% |
| GET_ITER | 1,072,440 | 16.3% |
| ENTER_EXECUTOR | 379,800 | 5.8% |
| FOR_ITER | 780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,160,400 | 32.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,127,900 | 32.4% |
| LOAD_GLOBAL_BUILTIN | 1,431,200 | 21.8% |
| LOAD_FAST | 298,000 | 4.5% |
| LOAD_FAST_LOAD_FAST | 274,880 | 4.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,390,240 | 49.5% |
| GET_ITER | 1,384,380 | 49.3% |
| SWAP | 32,800 | 1.2% |
| JUMP_BACKWARD | 60 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,390,700 | 49.5% |
| LOAD_FAST | 1,349,680 | 48.1% |
| JUMP_FORWARD | 33,200 | 1.2% |
| SWAP | 32,800 | 1.2% |
| LOAD_GLOBAL_MODULE | 1,080 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 7,600 | 51.9% |
| ENTER_EXECUTOR | 6,840 | 46.7% |
| JUMP_BACKWARD | 200 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,600 | 51.9% |
| LOAD_FAST | 5,920 | 40.4% |
| ENTER_EXECUTOR | 900 | 6.1% |
| JUMP_BACKWARD | 220 | 1.5% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,160,560 | 89.5% |
| LOAD_FAST_LOAD_FAST | 3,010,400 | 7.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,119,840 | 2.8% |
| COPY | 8,800 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,562,360 | 34.5% |
| STORE_FAST | 5,820,300 | 14.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,695,080 | 9.4% |
| CALL_LEN | 3,683,280 | 9.4% |
| COMPARE_OP_STR | 1,927,260 | 4.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,695,080 | 62.5% |
| LOAD_FAST | 1,375,920 | 23.3% |
| LOAD_GLOBAL_MODULE | 838,960 | 14.2% |
| CALL | 1,040 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,645,320 | 78.6% |
| LOAD_GLOBAL_MODULE | 441,840 | 7.5% |
| LOAD_CONST | 423,760 | 7.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 225,680 | 3.8% |
| LOAD_FAST_LOAD_FAST | 174,400 | 3.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,352,580 | 94.8% |
| BINARY_SUBSCR_TUPLE_INT | 165,200 | 2.9% |
| BINARY_SUBSCR | 130,080 | 2.3% |
| LOAD_FAST_LOAD_FAST | 1,040 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 5,111,160 | 90.5% |
| LOAD_FAST | 261,440 | 4.6% |
| LOAD_CONST | 183,920 | 3.3% |
| LOAD_GLOBAL_MODULE | 92,140 | 1.6% |
| LOAD_FAST_LOAD_FAST | 240 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,112,280 | 100.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 896,620 | 80.6% |
| STORE_FAST | 162,720 | 14.6% |
| RETURN_VALUE | 52,000 | 4.7% |
| COMPARE_OP_INT | 1,040 | 0.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,920 | 50.0% |
| LOAD_FAST_LOAD_FAST | 223,920 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 223,920 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 223,920 | 50.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 447,840 | 63.2% |
| LOAD_FAST | 260,160 | 36.7% |
| LOAD_FAST_LOAD_FAST | 480 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 708,480 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,920 | 50.0% |
| LOAD_FAST_LOAD_FAST | 223,920 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 223,920 | 50.0% |
| CALL_ISINSTANCE | 223,920 | 50.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 14,760,280 | 34.7% |
| LOAD_FAST | 10,645,840 | 25.1% |
| STORE_FAST | 5,236,160 | 12.3% |
| JUMP_FORWARD | 2,097,280 | 4.9% |
| LOAD_GLOBAL_BUILTIN | 1,774,320 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,530,940 | 53.0% |
| CALL_ISINSTANCE | 9,974,080 | 23.5% |
| STORE_FAST | 3,914,880 | 9.2% |
| LOAD_FAST_LOAD_FAST | 2,273,680 | 5.4% |
| LOAD_GLOBAL_BUILTIN | 1,774,320 | 4.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,317,160 | 58.0% |
| STORE_FAST | 7,338,040 | 12.8% |
| PUSH_NULL | 5,886,060 | 10.3% |
| POP_JUMP_IF_FALSE | 2,502,640 | 4.4% |
| RESUME_CHECK | 1,917,320 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 13,196,680 | 23.0% |
| CONTAINS_OP | 8,660,760 | 15.1% |
| BINARY_OP | 8,594,480 | 15.0% |
| LOAD_FAST | 7,214,580 | 12.6% |
| STORE_FAST | 6,364,160 | 11.1% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,932,440 | 34.1% |
| CACHE | 9,244,080 | 26.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,739,440 | 19.3% |
| BINARY_SUBSCR_GETITEM | 5,288,720 | 15.1% |
| LOAD_ATTR_PROPERTY | 708,480 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 14,760,280 | 42.2% |
| LOAD_FAST | 13,085,600 | 37.4% |
| LOAD_FAST_LOAD_FAST | 3,935,120 | 11.2% |
| LOAD_GLOBAL_MODULE | 1,917,320 | 5.5% |
| BUILD_LIST | 833,280 | 2.4% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,724,120 | 52.8% |
| LOAD_FAST_LOAD_FAST | 6,672,360 | 45.6% |
| LOAD_ATTR_INSTANCE_VALUE | 223,920 | 1.5% |
| SWAP | 8,800 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 4,510,360 | 30.8% |
| LOAD_FAST | 3,602,000 | 24.6% |
| LOAD_FAST_LOAD_FAST | 3,226,440 | 22.1% |
| LOAD_CONST | 2,394,720 | 16.4% |
| BUILD_MAP | 447,840 | 3.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 449,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,280 | 50.2% |
| LOAD_GLOBAL_BUILTIN | 223,920 | 49.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,533,540 | 87.7% |
| LOAD_FAST | 214,880 | 12.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 912,000 | 52.2% |
| ENTER_EXECUTOR | 459,140 | 26.3% |
| RETURN_CONST | 352,960 | 20.2% |
| LOAD_FAST | 23,920 | 1.4% |
| EXTENDED_ARG | 400 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 10,539,920 | 70.1% |
| RETURN_CONST | 2,025,720 | 13.5% |
| LOAD_FAST | 763,440 | 5.1% |
| RETURN_VALUE | 606,080 | 4.0% |
| COPY | 423,680 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,323,040 | 82.0% |
| POP_JUMP_IF_TRUE | 2,439,840 | 16.2% |
| EXTENDED_ARG | 264,240 | 1.8% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 7,038,640 | 65.3% |
| LOAD_FAST | 3,369,400 | 31.3% |
| COPY | 365,760 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,825,360 | 54.1% |
| POP_JUMP_IF_TRUE | 4,541,320 | 42.2% |
| UNARY_NOT | 407,120 | 3.8% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,809,720 | 94.0% |
| LOAD_ATTR_INSTANCE_VALUE | 116,040 | 6.0% |
| TO_BOOL_NONE | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT | 996,000 | 51.7% |
| POP_JUMP_IF_FALSE | 590,840 | 30.7% |
| POP_JUMP_IF_TRUE | 338,920 | 17.6% |
| TO_BOOL_NONE | 320 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,349,340 | 99.5% |
| COPY | 9,680 | 0.4% |
| TO_BOOL | 1,620 | 0.1% |
| ENTER_EXECUTOR | 360 | 0.0% |
| TO_BOOL_LIST | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,349,680 | 99.5% |
| POP_JUMP_IF_TRUE | 9,680 | 0.4% |
| TO_BOOL | 1,640 | 0.1% |
| TO_BOOL_LIST | 320 | 0.0% |
| TO_BOOL_STR | 160 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 798,720 | 99.9% |
| LOAD_FAST | 600 | 0.1% |
| TO_BOOL_NONE | 160 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 798,720 | 99.9% |
| POP_JUMP_IF_FALSE | 640 | 0.1% |
| TO_BOOL_NONE | 160 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 321,760 | 53.7% |
| RETURN_VALUE | 253,040 | 42.3% |
| BINARY_SUBSCR_TUPLE_INT | 23,920 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 312,960 | 52.3% |
| STORE_FAST_STORE_FAST | 285,760 | 47.7% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 6,103,280 | 54.9% |
| FOR_ITER | 2,741,760 | 24.7% |
| FOR_ITER_LIST | 2,127,900 | 19.2% |
| BINARY_SUBSCR_LIST_INT | 116,280 | 1.0% |
| LOAD_CONST | 18,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 7,437,320 | 67.0% |
| STORE_FAST | 3,670,240 | 33.0% |


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
|     deferred | 10,289,300 | 34.5% |
|          hit | 19,568,860 | 65.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 0.7% |
| Failure | 6,080 | 99.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 4,300 | 70.7% |
| or | 840 | 13.8% |
| add other | 420 | 6.9% |
| multiply different types | 260 | 4.3% |
| add different types | 100 | 1.6% |
| and different types | 100 | 1.6% |
| floor divide | 60 | 1.0% |


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
|     deferred | 3,050,480 | 9.9% |
|          hit | 27,745,920 | 90.0% |
|         miss | 1,509,180 | 4.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 28,480 | 97.8% |
| Failure | 640 | 2.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 340 | 53.1% |
| out of range | 100 | 15.6% |
| list slice | 100 | 15.6% |
| buffer slice | 100 | 15.6% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,193,960 | 2.3% |
|          hit | 93,611,400 | 97.7% |
|         miss | 52,420 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,260 | 50.8% |
| Failure | 1,220 | 49.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| wrong number arguments | 460 | 37.7% |
| class no vectorcall | 340 | 27.9% |
| meth descr varargs | 220 | 18.0% |
| metaclass | 120 | 9.8% |
| cfunc noargs | 60 | 4.9% |
| str | 20 | 1.6% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,147,080 | 6.7% |
|          hit | 16,057,080 | 93.3% |
|         miss | 165,780 | 1.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,180 | 30.8% |
| Failure | 7,140 | 69.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 6,540 | 91.6% |
| other | 260 | 3.6% |
| big int | 200 | 2.8% |
| tuple | 140 | 2.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,258,560 | 31.3% |
|          hit | 9,358,420 | 68.7% |
|         miss | 40,280 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 800 | 16.3% |
| Failure | 4,100 | 83.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| seq iter | 3,880 | 94.6% |
| dict keys | 100 | 2.4% |
| dict items | 100 | 2.4% |
| map | 20 | 0.5% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,586,260 | 9.9% |
|          hit | 68,683,780 | 90.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 6.7% |
| Failure | 3,040 | 93.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 2,420 | 79.6% |
| metaclass attribute | 300 | 9.9% |
| not managed dict | 180 | 5.9% |
| builtin class method | 100 | 3.3% |
| mutable class | 40 | 1.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 0.0% |
|          hit | 99,899,520 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 360 | 100.0% |
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
|          hit | 19,073,120 | 100.0% |


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
|     deferred | 1,213,080 | 27.4% |
|          hit | 3,216,160 | 72.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 0 | 0.0% |
| Failure | 760 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 500 | 65.8% |
| py simple | 160 | 21.1% |
| out of range | 100 | 13.2% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,485,040 | 4.0% |
|          hit | 35,600,380 | 96.0% |
|         miss | 138,660 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,660 | 32.0% |
| Failure | 5,660 | 68.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 4,260 | 75.3% |
| mapping | 500 | 8.8% |
| other | 440 | 7.8% |
| dict | 360 | 6.4% |
| number | 100 | 1.8% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 16,319,500 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 589,349,240 | 54.3% |
| Not specialized | 110,745,460 | 10.2% |
| Specialized hits | 383,596,300 | 35.3% |
| Specialized misses | 1,906,320 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 10,289,300 | 33.0% |
| LOAD_ATTR | 7,586,260 | 24.3% |
| FOR_ITER | 4,258,560 | 13.6% |
| BINARY_SUBSCR | 3,050,480 | 9.8% |
| CALL | 2,193,960 | 7.0% |
| TO_BOOL | 1,485,040 | 4.8% |
| STORE_SUBSCR | 1,213,080 | 3.9% |
| COMPARE_OP | 1,147,080 | 3.7% |
| LOAD_GLOBAL | 180 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 1,276,900 | 67.0% |
| BINARY_SUBSCR_STR_INT | 232,280 | 12.2% |
| COMPARE_OP_STR | 165,780 | 8.7% |
| TO_BOOL_NONE | 113,540 | 6.0% |
| CALL_BUILTIN_FAST | 52,420 | 2.7% |
| FOR_ITER_LIST | 40,280 | 2.1% |
| TO_BOOL_LIST | 16,960 | 0.9% |
| TO_BOOL_STR | 8,160 | 0.4% |
| CACHE | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 9,244,080 | 22.5% |
| Calls to Python functions inlined | 31,809,360 | 77.5% |
| Calls via PyEval_EvalFrame (total) | 9,244,080 | 22.5% |
| Calls via PyEval_EvalFrame (vector) | 9,244,080 | 22.5% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 9,244,080 | 22.5% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 7,649,360 | 18.6% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 3,072,080 | 7.5% |
| Frames pushed | 41,666,480 | 101.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 17,777,240 | 23.4% |
| Frees to freelist | 17,786,240 |  |
| Allocations | 58,262,460 | 76.6% |
| Allocations to 512 bytes | 58,220,320 | 76.6% |
| Allocations to 4 kbytes | 40,060 | 0.1% |
| Allocations over 4 kbytes | 2,080 | 0.0% |
| Frees | 60,955,102 |  |
| New values | 1,333,840 |  |
| Interpreter increfs | 417,681,340 | 62.6% |
| Interpreter decrefs | 460,727,600 | 62.1% |
| Increfs | 249,465,160 | 37.4% |
| Decrefs | 280,598,782 | 37.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 8,207,049 |  |
| Method cache misses | 131 |  |
| Method cache collisions | 177 |  |
| Method cache dunder hits | 20,382,280 |  |
| Method cache dunder misses | 60 |  |


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
| Optimization attempts | 1,300 |  |
| Traces created | 1,300 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 20 | 1.5% |
| Recursive call | 1,000 | 76.9% |
| Low confidence | 0 | 0.0% |
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
| <= 8 | 0 | 0.0% |
| <= 16 | 20 | 1.5% |
| <= 32 | 600 | 46.2% |
| <= 64 | 580 | 44.6% |
| <= 128 | 40 | 3.1% |
| <= 256 | 60 | 4.6% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 0 | 0.0% |
| <= 16 | 80 | 6.2% |
| <= 32 | 80 | 6.2% |
| <= 64 | 40 | 3.1% |
| <= 128 | 60 | 4.6% |
| <= 256 | 40 | 3.1% |


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
| BINARY_SUBSCR_GETITEM | 80 |
| CALL_LIST_APPEND | 60 |


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
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
