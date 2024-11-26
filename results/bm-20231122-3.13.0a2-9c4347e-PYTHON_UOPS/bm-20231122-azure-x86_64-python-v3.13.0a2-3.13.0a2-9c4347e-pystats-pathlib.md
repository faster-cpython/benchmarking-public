
# Pystats results

- benchmark: pathlib
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 131,991,060 | 21.1% | 21.1% |  |
| RESUME_CHECK | 43,716,720 | 7.0% | 28.1% | 0.0% |
| STORE_FAST | 34,768,280 | 5.6% | 33.7% |  |
| RETURN_VALUE | 33,629,260 | 5.4% | 39.0% |  |
| LOAD_GLOBAL_BUILTIN | 26,911,640 | 4.3% | 43.3% |  |
| INTERPRETER_EXIT | 20,332,920 | 3.3% | 46.6% |  |
| NOP | 20,174,160 | 3.2% | 49.8% |  |
| STORE_ATTR_SLOT | 20,166,680 | 3.2% | 53.0% |  |
| LOAD_ATTR_SLOT | 19,373,240 | 3.1% | 56.1% | 0.0% |
| POP_JUMP_IF_FALSE | 16,036,220 | 2.6% | 58.7% |  |
| PUSH_NULL | 16,014,780 | 2.6% | 61.3% |  |
| LOAD_GLOBAL_MODULE | 13,463,720 | 2.2% | 63.4% |  |
| LOAD_FAST_LOAD_FAST | 13,459,300 | 2.2% | 65.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 13,454,620 | 2.2% | 67.7% |  |
| CALL | 12,658,580 | 2.0% | 69.7% |  |
| JUMP_BACKWARD | 12,005,760 | 1.9% | 71.7% |  |
| LOAD_ATTR_MODULE | 10,097,580 | 1.6% | 73.3% |  |
| POP_TOP | 10,091,820 | 1.6% | 74.9% |  |
| LOAD_ATTR_PROPERTY | 10,085,280 | 1.6% | 76.5% |  |
| FORMAT_SIMPLE | 10,080,140 | 1.6% | 78.1% |  |
| TO_BOOL_BOOL | 9,289,300 | 1.5% | 79.6% |  |
| LOAD_CONST | 6,765,680 | 1.1% | 80.7% |  |
| RETURN_CONST | 6,728,160 | 1.1% | 81.7% |  |
| CALL_STR_1 | 6,725,300 | 1.1% | 82.8% |  |
| CALL_ISINSTANCE | 6,725,020 | 1.1% | 83.9% |  |
| BUILD_LIST | 6,724,560 | 1.1% | 85.0% |  |
| CALL_FUNCTION_EX | 6,722,800 | 1.1% | 86.0% |  |
| FOR_ITER_TUPLE | 6,722,700 | 1.1% | 87.1% |  |
| LOAD_DEREF | 6,084,240 | 1.0% | 88.1% |  |
| POP_JUMP_IF_TRUE | 5,930,940 | 0.9% | 89.0% |  |
| FOR_ITER_LIST | 5,448,760 | 0.9% | 89.9% | 0.0% |
| CALL_PY_EXACT_ARGS | 3,370,820 | 0.5% | 90.5% |  |
| GET_ITER | 3,369,840 | 0.5% | 91.0% |  |
| LOAD_ATTR | 3,367,900 | 0.5% | 91.5% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,365,340 | 0.5% | 92.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 3,365,020 | 0.5% | 92.6% |  |
| IS_OP | 3,364,440 | 0.5% | 93.1% |  |
| TO_BOOL | 3,363,640 | 0.5% | 93.7% |  |
| JUMP_FORWARD | 3,363,480 | 0.5% | 94.2% |  |
| COPY_FREE_VARS | 3,362,800 | 0.5% | 94.8% |  |
| CALL_KW | 3,362,580 | 0.5% | 95.3% |  |
| BINARY_OP | 3,362,480 | 0.5% | 95.8% |  |
| CALL_LIST_APPEND | 3,361,600 | 0.5% | 96.4% |  |
| TO_BOOL_LIST | 3,361,500 | 0.5% | 96.9% | 0.0% |
| CALL_TYPE_1 | 3,361,360 | 0.5% | 97.4% |  |
| LOAD_SUPER_ATTR_ATTR | 3,361,340 | 0.5% | 98.0% |  |
| BUILD_STRING | 3,360,120 | 0.5% | 98.5% |  |
| YIELD_VALUE | 3,360,000 | 0.5% | 99.1% |  |
| FOR_ITER_GEN | 3,202,480 | 0.5% | 99.6% |  |
| TO_BOOL_NONE | 1,931,300 | 0.3% | 99.9% | 24.6% |
| TO_BOOL_ALWAYS_TRUE | 648,080 | 0.1% | 100.0% | 73.1% |
| COMPARE_OP_STR | 9,580 | 0.0% | 100.0% | 0.4% |
| CALL_LEN | 7,600 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 6,980 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 6,900 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 6,000 | 0.0% | 100.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 4,800 | 0.0% | 100.0% |  |
| SWAP | 4,160 | 0.0% | 100.0% |  |
| CONTAINS_OP | 4,100 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 4,080 | 0.0% | 100.0% |  |
| MAKE_CELL | 3,920 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 3,800 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 3,640 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 3,620 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 3,360 | 0.0% | 100.0% | 2.4% |
| POP_JUMP_IF_NOT_NONE | 3,260 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 3,100 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 2,800 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 2,760 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 2,640 | 0.0% | 100.0% |  |
| END_FOR | 2,560 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 2,540 | 0.0% | 100.0% | 0.8% |
| LOAD_GLOBAL | 2,340 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_INT | 2,340 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,140 | 0.0% | 100.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 1,880 | 0.0% | 100.0% |  |
| COPY | 1,840 | 0.0% | 100.0% |  |
| BINARY_SLICE | 1,600 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 1,520 | 0.0% | 100.0% |  |
| POP_EXCEPT | 1,520 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 1,520 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 1,520 | 0.0% | 100.0% |  |
| LIST_APPEND | 1,440 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 1,360 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 1,360 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 1,360 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,340 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 1,300 | 0.0% | 100.0% |  |
| BEFORE_WITH | 1,280 | 0.0% | 100.0% |  |
| STORE_DEREF | 1,280 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 1,180 | 0.0% | 100.0% | 3.4% |
| COMPARE_OP | 1,120 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 1,000 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 920 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 900 | 0.0% | 100.0% | 4.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 860 | 0.0% | 100.0% |  |
| RESUME | 660 | 0.0% | 100.0% | 6.1% |
| FOR_ITER | 580 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 580 | 0.0% | 100.0% |  |
| STORE_ATTR | 400 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 400 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 380 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NONE | 280 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 160 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 120 | 0.0% | 100.0% |  |
| UNARY_NOT | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 120 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 120 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 120 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 100 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 100 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 80 | 0.0% | 100.0% |  |
| BUILD_MAP | 80 | 0.0% | 100.0% |  |
| BUILD_SLICE | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| UNARY_INVERT | 40 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 40 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 40 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_SLOT | 19,371,780 | 3.1% | 3.1% |
| STORE_FAST LOAD_FAST | 18,582,920 | 3.0% | 6.1% |
| CACHE RESUME_CHECK | 16,971,260 | 2.7% | 8.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 16,823,280 | 2.7% | 11.5% |
| NOP LOAD_FAST | 16,811,300 | 2.7% | 14.2% |
| RESUME_CHECK NOP | 16,810,480 | 2.7% | 16.8% |
| LOAD_ATTR_SLOT RETURN_VALUE | 16,807,800 | 2.7% | 19.5% |
| RETURN_VALUE INTERPRETER_EXIT | 13,449,920 | 2.2% | 21.7% |
| LOAD_FAST STORE_ATTR_SLOT | 13,441,240 | 2.1% | 23.8% |
| PUSH_NULL LOAD_FAST | 12,647,920 | 2.0% | 25.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 10,733,720 | 1.7% | 27.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 10,086,840 | 1.6% | 29.2% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 10,086,400 | 1.6% | 30.8% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 10,085,280 | 1.6% | 32.4% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 10,085,000 | 1.6% | 34.0% |
| STORE_ATTR_SLOT LOAD_FAST | 10,080,000 | 1.6% | 35.6% |
| LOAD_FAST CALL | 9,286,500 | 1.5% | 37.1% |
| RESUME_CHECK LOAD_FAST | 6,732,280 | 1.1% | 38.2% |
| LOAD_ATTR_MODULE PUSH_NULL | 6,729,680 | 1.1% | 39.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 6,729,480 | 1.1% | 40.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 6,728,160 | 1.1% | 41.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 6,726,260 | 1.1% | 42.5% |
| LOAD_FAST CALL_STR_1 | 6,725,240 | 1.1% | 43.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 6,725,240 | 1.1% | 44.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 6,724,820 | 1.1% | 45.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 6,724,020 | 1.1% | 46.8% |
| CALL RESUME_CHECK | 6,723,880 | 1.1% | 47.9% |
| RETURN_CONST INTERPRETER_EXIT | 6,722,920 | 1.1% | 48.9% |
| LOAD_FAST CALL_FUNCTION_EX | 6,722,720 | 1.1% | 50.0% |
| RETURN_VALUE STORE_FAST | 6,721,940 | 1.1% | 51.1% |
| POP_TOP JUMP_BACKWARD | 6,720,160 | 1.1% | 52.2% |
| RETURN_VALUE LOAD_FAST | 6,720,140 | 1.1% | 53.2% |
| LOAD_FAST FORMAT_SIMPLE | 6,720,120 | 1.1% | 54.3% |
| FORMAT_SIMPLE LOAD_FAST | 6,720,020 | 1.1% | 55.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 5,940,820 | 0.9% | 56.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 5,927,700 | 0.9% | 57.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 5,442,640 | 0.9% | 58.2% |
| FOR_ITER_LIST STORE_FAST | 5,442,560 | 0.9% | 59.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 4,007,300 | 0.6% | 59.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 3,367,260 | 0.5% | 60.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 3,365,660 | 0.5% | 60.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 3,365,360 | 0.5% | 61.3% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 3,364,920 | 0.5% | 61.8% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,363,900 | 0.5% | 62.4% |
| CALL_STR_1 RETURN_VALUE | 3,363,900 | 0.5% | 62.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT LOAD_ATTR_MODULE | 3,363,680 | 0.5% | 63.4% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 3,363,420 | 0.5% | 64.0% |
| LOAD_ATTR LOAD_FAST | 3,363,180 | 0.5% | 64.5% |
| LOAD_CONST LOAD_FAST | 3,363,080 | 0.5% | 65.1% |
| LOAD_GLOBAL_MODULE IS_OP | 3,363,080 | 0.5% | 65.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 3,362,940 | 0.5% | 66.1% |
| LOAD_FAST GET_ITER | 3,362,920 | 0.5% | 66.7% |
| IS_OP POP_JUMP_IF_FALSE | 3,362,900 | 0.5% | 67.2% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 3,362,880 | 0.5% | 67.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 3,362,680 | 0.5% | 68.3% |
| STORE_ATTR_SLOT RETURN_CONST | 3,362,680 | 0.5% | 68.8% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 3,362,660 | 0.5% | 69.4% |
| NOP LOAD_GLOBAL_MODULE | 3,362,600 | 0.5% | 69.9% |
| LOAD_CONST CALL_KW | 3,362,580 | 0.5% | 70.4% |
| TO_BOOL POP_JUMP_IF_FALSE | 3,361,940 | 0.5% | 71.0% |
| LOAD_FAST RETURN_VALUE | 3,361,940 | 0.5% | 71.5% |
| LOAD_FAST TO_BOOL | 3,361,920 | 0.5% | 72.0% |
| BUILD_LIST STORE_FAST | 3,361,740 | 0.5% | 72.6% |
| JUMP_FORWARD LOAD_FAST | 3,361,580 | 0.5% | 73.1% |
| STORE_FAST JUMP_FORWARD | 3,361,540 | 0.5% | 73.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 3,361,540 | 0.5% | 74.2% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 3,361,520 | 0.5% | 74.7% |
| LOAD_FAST CALL_LIST_APPEND | 3,361,520 | 0.5% | 75.3% |
| POP_TOP RETURN_CONST | 3,361,500 | 0.5% | 75.8% |
| CALL RETURN_VALUE | 3,361,480 | 0.5% | 76.3% |
| POP_JUMP_IF_FALSE NOP | 3,361,480 | 0.5% | 76.9% |
| RESUME_CHECK BUILD_LIST | 3,361,460 | 0.5% | 77.4% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 3,361,440 | 0.5% | 78.0% |
| COPY_FREE_VARS RESUME_CHECK | 3,361,400 | 0.5% | 78.5% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 3,361,400 | 0.5% | 79.0% |
| CACHE COPY_FREE_VARS | 3,361,360 | 0.5% | 79.6% |
| CALL_FUNCTION_EX POP_TOP | 3,361,360 | 0.5% | 80.1% |
| LOAD_DEREF LOAD_FAST | 3,361,360 | 0.5% | 80.6% |
| FOR_ITER_TUPLE LOAD_FAST_LOAD_FAST | 3,361,360 | 0.5% | 81.2% |
| LOAD_GLOBAL_BUILTIN LOAD_ATTR | 3,361,360 | 0.5% | 81.7% |
| GET_ITER FOR_ITER_TUPLE | 3,361,340 | 0.5% | 82.3% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 3,361,340 | 0.5% | 82.8% |
| LOAD_FAST CALL_TYPE_1 | 3,361,340 | 0.5% | 83.3% |
| CALL_LIST_APPEND JUMP_BACKWARD | 3,361,340 | 0.5% | 83.9% |
| FOR_ITER_TUPLE STORE_FAST | 3,361,340 | 0.5% | 84.4% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 3,361,340 | 0.5% | 84.9% |
| LOAD_SUPER_ATTR_ATTR PUSH_NULL | 3,361,340 | 0.5% | 85.5% |
| STORE_ATTR_SLOT LOAD_CONST | 3,361,340 | 0.5% | 86.0% |
| LOAD_FAST LOAD_SUPER_ATTR_ATTR | 3,361,320 | 0.5% | 86.6% |
| CALL_FUNCTION_EX RETURN_VALUE | 3,361,280 | 0.5% | 87.1% |
| CALL_KW RETURN_VALUE | 3,361,280 | 0.5% | 87.6% |
| CALL_TYPE_1 PUSH_NULL | 3,361,260 | 0.5% | 88.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL | 3,361,260 | 0.5% | 88.7% |
| RETURN_VALUE POP_TOP | 3,360,240 | 0.5% | 89.2% |
| LOAD_FAST TO_BOOL_LIST | 3,360,200 | 0.5% | 89.8% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 3,360,140 | 0.5% | 90.3% |
| BINARY_OP LOAD_FAST | 3,360,100 | 0.5% | 90.8% |
| BUILD_STRING STORE_FAST | 3,360,080 | 0.5% | 91.4% |
| FORMAT_SIMPLE BUILD_STRING | 3,360,020 | 0.5% | 91.9% |
| RETURN_VALUE YIELD_VALUE | 3,360,000 | 0.5% | 92.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,440 | 90.0% |
| BUILD_TUPLE | 80 | 5.0% |
| STORE_FAST | 80 | 5.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,971,260 | 83.5% |
| COPY_FREE_VARS | 3,361,360 | 16.5% |
| RESUME | 220 | 0.0% |
| POP_TOP | 160 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,280 | 100.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,680 | 86.5% |
| BINARY_SUBSCR | 200 | 6.5% |
| BUILD_SLICE | 80 | 2.6% |
| LOAD_FAST_LOAD_FAST | 80 | 2.6% |
| LOAD_FAST | 60 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,280 | 41.3% |
| LOAD_FAST | 1,280 | 41.3% |
| BINARY_SUBSCR | 200 | 6.5% |
| GET_ITER | 80 | 2.6% |
| STORE_FAST | 80 | 2.6% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,480 | 97.4% |
| LOAD_GLOBAL | 40 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,520 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,920 | 75.0% |
| JUMP_BACKWARD | 640 | 25.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 120 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,720,120 | 66.7% |
| LOAD_ATTR_MODULE | 3,359,980 | 33.3% |
| LOAD_ATTR | 20 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,720,020 | 66.7% |
| BUILD_STRING | 3,360,020 | 33.3% |
| LOAD_CONST | 100 | 0.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,362,920 | 99.8% |
| RETURN_VALUE | 2,560 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,340 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,340 | 0.0% |
| LOAD_FAST_CHECK | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 3,361,340 | 99.7% |
| FOR_ITER_LIST | 2,620 | 0.1% |
| FOR_ITER_GEN | 2,480 | 0.1% |
| LOAD_FAST_AND_CLEAR | 1,360 | 0.0% |
| CALL_PY_EXACT_ARGS | 1,320 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 13,449,920 | 66.1% |
| RETURN_CONST | 6,722,920 | 33.1% |
| YIELD_VALUE | 160,080 | 0.8% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 1,360 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,810,480 | 83.3% |
| POP_JUMP_IF_FALSE | 3,361,480 | 16.7% |
| STORE_FAST | 2,020 | 0.0% |
| RESUME | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,811,300 | 83.3% |
| LOAD_GLOBAL_MODULE | 3,362,600 | 16.7% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,440 | 94.7% |
| POP_TOP | 40 | 2.6% |
| STORE_ATTR_INSTANCE_VALUE | 40 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,440 | 94.7% |
| JUMP_FORWARD | 40 | 2.6% |
| RETURN_CONST | 40 | 2.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 3,361,360 | 33.3% |
| RETURN_VALUE | 3,360,240 | 33.3% |
| RESUME_CHECK | 3,359,960 | 33.3% |
| FOR_ITER_GEN | 2,480 | 0.0% |
| RETURN_CONST | 2,200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,720,160 | 66.6% |
| RETURN_CONST | 3,361,500 | 33.3% |
| LOAD_FAST | 5,420 | 0.1% |
| RESUME_CHECK | 2,600 | 0.0% |
| LOAD_FAST_CHECK | 1,280 | 0.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,400 | 92.1% |
| LOAD_ATTR | 40 | 2.6% |
| BINARY_SUBSCR_DICT | 40 | 2.6% |
| BINARY_SUBSCR_STR_INT | 40 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,440 | 94.7% |
| LOAD_GLOBAL | 80 | 5.3% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 6,729,680 | 42.0% |
| LOAD_SUPER_ATTR_ATTR | 3,361,340 | 21.0% |
| CALL_TYPE_1 | 3,361,260 | 21.0% |
| LOAD_FAST | 2,561,900 | 16.0% |
| LOAD_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,647,920 | 79.0% |
| LOAD_FAST_LOAD_FAST | 3,361,520 | 21.0% |
| LOAD_CONST | 1,600 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,420 | 0.0% |
| LOAD_DEREF | 1,360 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,360 | 51.5% |
| CALL_PY_EXACT_ARGS | 1,260 | 47.7% |
| CALL | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,360 | 51.5% |
| STORE_FAST | 1,280 | 48.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 16,807,800 | 50.0% |
| CALL_STR_1 | 3,363,900 | 10.0% |
| LOAD_FAST | 3,361,940 | 10.0% |
| CALL | 3,361,480 | 10.0% |
| CALL_FUNCTION_EX | 3,361,280 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 13,449,920 | 40.0% |
| STORE_FAST | 6,721,940 | 20.0% |
| LOAD_FAST | 6,720,140 | 20.0% |
| POP_TOP | 3,360,240 | 10.0% |
| YIELD_VALUE | 3,360,000 | 10.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 50.0% |
| LOAD_FAST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 40 | 50.0% |
| RETURN_CONST | 40 | 50.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,920 | 99.9% |
| TO_BOOL | 1,040 | 0.0% |
| CALL | 160 | 0.0% |
| BINARY_OP | 120 | 0.0% |
| RETURN_VALUE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,361,940 | 99.9% |
| TO_BOOL | 1,040 | 0.0% |
| POP_JUMP_IF_TRUE | 220 | 0.0% |
| TO_BOOL_BOOL | 180 | 0.0% |
| TO_BOOL_STR | 160 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 40 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 80 | 66.7% |
| TO_BOOL_LIST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 66.7% |
| CALL_PY_EXACT_ARGS | 40 | 33.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 3,360,000 | 99.9% |
| BINARY_OP | 1,060 | 0.0% |
| LOAD_GLOBAL_MODULE | 780 | 0.0% |
| LOAD_FAST_LOAD_FAST | 180 | 0.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,360,100 | 99.9% |
| BINARY_OP | 1,060 | 0.0% |
| TO_BOOL_INT | 660 | 0.0% |
| STORE_FAST | 260 | 0.0% |
| TO_BOOL | 120 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,361,460 | 50.0% |
| LOAD_FAST_LOAD_FAST | 3,360,000 | 50.0% |
| LOAD_FAST | 1,360 | 0.0% |
| SWAP | 1,360 | 0.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,361,740 | 50.0% |
| BINARY_OP | 3,360,000 | 50.0% |
| SWAP | 1,360 | 0.0% |
| JUMP_FORWARD | 1,280 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 80 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 3,360,020 | 100.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,360,080 | 100.0% |
| RETURN_VALUE | 20 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,080 | 68.0% |
| LOAD_ATTR_MODULE | 1,260 | 21.0% |
| CALL | 120 | 2.0% |
| CALL_BUILTIN_O | 120 | 2.0% |
| LOAD_FAST_LOAD_FAST | 100 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,820 | 47.0% |
| LOAD_CONST | 1,360 | 22.7% |
| CONTAINS_OP | 1,280 | 21.3% |
| LOAD_FAST | 160 | 2.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 100 | 1.7% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,286,500 | 73.4% |
| LOAD_ATTR_METHOD_NO_DICT | 3,361,260 | 26.6% |
| CALL | 5,480 | 0.0% |
| LOAD_CONST | 2,580 | 0.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,723,880 | 53.1% |
| RETURN_VALUE | 3,361,480 | 26.6% |
| TO_BOOL_NONE | 1,920,840 | 15.2% |
| TO_BOOL_ALWAYS_TRUE | 639,120 | 5.0% |
| CALL | 5,480 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,722,720 | 100.0% |
| CALL_INTRINSIC_1 | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,361,360 | 50.0% |
| RETURN_VALUE | 3,361,280 | 50.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


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

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,362,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,361,280 | 100.0% |
| RESUME_CHECK | 1,280 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 660 | 58.9% |
| LOAD_GLOBAL_MODULE | 140 | 12.5% |
| LOAD_FAST_LOAD_FAST | 100 | 8.9% |
| LOAD_FAST | 80 | 7.1% |
| CALL | 60 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 520 | 46.4% |
| COMPARE_OP_STR | 220 | 19.6% |
| COMPARE_OP_INT | 140 | 12.5% |
| POP_JUMP_IF_TRUE | 120 | 10.7% |
| EXTENDED_ARG | 80 | 7.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,300 | 31.7% |
| BUILD_TUPLE | 1,280 | 31.2% |
| LOAD_GLOBAL_MODULE | 740 | 18.0% |
| LOAD_FAST_LOAD_FAST | 440 | 10.7% |
| LOAD_CONST | 320 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,700 | 90.2% |
| EXTENDED_ARG | 360 | 8.8% |
| RETURN_VALUE | 20 | 0.5% |
| POP_JUMP_IF_TRUE | 20 | 0.5% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 1,300 | 70.7% |
| LOAD_ATTR_INSTANCE_VALUE | 180 | 9.8% |
| LOAD_CONST | 120 | 6.5% |
| RETURN_VALUE | 80 | 4.3% |
| UNARY_NOT | 80 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,340 | 72.8% |
| TO_BOOL_STR | 220 | 12.0% |
| STORE_FAST_STORE_FAST | 120 | 6.5% |
| TO_BOOL | 80 | 4.3% |
| TO_BOOL_INT | 80 | 4.3% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 3,361,360 | 100.0% |
| CALL_PY_EXACT_ARGS | 1,340 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,361,400 | 100.0% |
| RETURN_GENERATOR | 1,360 | 0.0% |
| RESUME | 40 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,260 | 34.6% |
| JUMP_BACKWARD | 480 | 13.2% |
| CONTAINS_OP | 360 | 9.9% |
| POP_TOP | 280 | 7.7% |
| GET_ITER | 240 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,960 | 53.8% |
| FOR_ITER_LIST | 720 | 19.8% |
| JUMP_BACKWARD | 600 | 16.5% |
| JUMP_FORWARD | 360 | 9.9% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 280 | 48.3% |
| JUMP_BACKWARD | 240 | 41.4% |
| FOR_ITER | 20 | 3.4% |
| LOAD_FAST | 20 | 3.4% |
| SWAP | 20 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 34.5% |
| FOR_ITER_LIST | 100 | 17.2% |
| FOR_ITER_GEN | 80 | 13.8% |
| LOAD_FAST | 40 | 6.9% |
| LOAD_GLOBAL_MODULE | 40 | 6.9% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,363,080 | 100.0% |
| LOAD_CONST | 1,300 | 0.0% |
| LOAD_FAST | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,362,900 | 100.0% |
| COPY | 1,300 | 0.0% |
| POP_JUMP_IF_TRUE | 240 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,720,160 | 56.0% |
| CALL_LIST_APPEND | 3,361,340 | 28.0% |
| POP_JUMP_IF_TRUE | 1,920,200 | 16.0% |
| LIST_APPEND | 1,440 | 0.0% |
| FOR_ITER_LIST | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,442,640 | 45.3% |
| FOR_ITER_TUPLE | 3,361,340 | 28.0% |
| FOR_ITER_GEN | 3,199,920 | 26.7% |
| FOR_ITER_RANGE | 820 | 0.0% |
| EXTENDED_ARG | 480 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,361,540 | 99.9% |
| BUILD_LIST | 1,280 | 0.0% |
| EXTENDED_ARG | 360 | 0.0% |
| POP_TOP | 120 | 0.0% |
| POP_JUMP_IF_TRUE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,580 | 99.9% |
| CALL_BUILTIN_FAST | 1,240 | 0.0% |
| EXTENDED_ARG | 240 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 1,420 | 98.6% |
| CALL | 20 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,440 | 100.0% |


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
| LOAD_GLOBAL_BUILTIN | 3,361,360 | 99.8% |
| LOAD_FAST | 4,200 | 0.1% |
| LOAD_ATTR | 1,340 | 0.0% |
| LOAD_GLOBAL | 400 | 0.0% |
| LOAD_GLOBAL_MODULE | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,363,180 | 99.9% |
| LOAD_ATTR | 1,340 | 0.0% |
| STORE_FAST | 800 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 480 | 0.0% |
| LOAD_ATTR_MODULE | 420 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,361,440 | 49.7% |
| STORE_ATTR_SLOT | 3,361,340 | 49.7% |
| LOAD_FAST | 18,300 | 0.3% |
| STORE_FAST | 6,060 | 0.1% |
| LOAD_CONST | 4,340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,363,080 | 49.7% |
| CALL_KW | 3,362,580 | 49.7% |
| COMPARE_OP_STR | 7,720 | 0.1% |
| STORE_FAST | 7,340 | 0.1% |
| LOAD_CONST | 4,340 | 0.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,361,340 | 55.2% |
| STORE_FAST | 2,720,000 | 44.7% |
| PUSH_NULL | 1,360 | 0.0% |
| LOAD_FAST | 1,280 | 0.0% |
| NOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,360 | 55.2% |
| LOAD_ATTR_METHOD_NO_DICT | 2,719,960 | 44.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,320 | 0.0% |
| CALL_PY_EXACT_ARGS | 1,240 | 0.0% |
| PUSH_NULL | 160 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,582,920 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 16,823,280 | 12.7% |
| NOP | 16,811,300 | 12.7% |
| PUSH_NULL | 12,647,920 | 9.6% |
| LOAD_ATTR_METHOD_NO_DICT | 10,086,840 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 19,371,780 | 14.7% |
| STORE_ATTR_SLOT | 13,441,240 | 10.2% |
| LOAD_ATTR_METHOD_NO_DICT | 10,733,720 | 8.1% |
| LOAD_ATTR_PROPERTY | 10,085,000 | 7.6% |
| CALL | 9,286,500 | 7.0% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,360 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,280 | 98.5% |
| POP_JUMP_IF_NOT_NONE | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,280 | 98.5% |
| TO_BOOL_BOOL | 20 | 1.5% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,362,880 | 25.0% |
| STORE_ATTR_SLOT | 3,362,660 | 25.0% |
| PUSH_NULL | 3,361,520 | 25.0% |
| FOR_ITER_TUPLE | 3,361,360 | 25.0% |
| LOAD_GLOBAL_MODULE | 3,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 6,725,240 | 50.0% |
| LOAD_CONST | 3,361,440 | 25.0% |
| BUILD_LIST | 3,360,000 | 25.0% |
| LOAD_FAST | 6,880 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 1,240 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 500 | 21.4% |
| LOAD_FAST | 420 | 17.9% |
| POP_JUMP_IF_FALSE | 240 | 10.3% |
| RESUME | 180 | 7.7% |
| RESUME_CHECK | 180 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 23.1% |
| LOAD_GLOBAL_BUILTIN | 520 | 22.2% |
| LOAD_GLOBAL_MODULE | 460 | 19.7% |
| LOAD_ATTR | 400 | 17.1% |
| CALL | 100 | 4.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 20 | 50.0% |
| LOAD_SUPER_ATTR_ATTR | 20 | 50.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,560 | 65.3% |
| MAKE_CELL | 1,280 | 32.7% |
| CALL | 80 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,600 | 66.3% |
| MAKE_CELL | 1,280 | 32.7% |
| RESUME | 40 | 1.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,927,700 | 37.0% |
| IS_OP | 3,362,900 | 21.0% |
| TO_BOOL | 3,361,940 | 21.0% |
| TO_BOOL_LIST | 3,360,140 | 21.0% |
| COMPARE_OP_STR | 7,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,724,020 | 41.9% |
| LOAD_FAST | 5,940,820 | 37.0% |
| NOP | 3,361,480 | 21.0% |
| LOAD_FAST_LOAD_FAST | 3,000 | 0.0% |
| LOAD_CONST | 2,720 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 200 | 71.4% |
| LOAD_FAST | 80 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 57.1% |
| LOAD_CONST | 120 | 42.9% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,260 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,280 | 39.3% |
| LOAD_GLOBAL_MODULE | 1,280 | 39.3% |
| LOAD_FAST | 420 | 12.9% |
| BUILD_LIST | 80 | 2.5% |
| LOAD_GLOBAL_BUILTIN | 60 | 1.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,361,540 | 56.7% |
| TO_BOOL_NONE | 1,920,840 | 32.4% |
| TO_BOOL_ALWAYS_TRUE | 639,140 | 10.8% |
| TO_BOOL_STR | 5,660 | 0.1% |
| COMPARE_OP_STR | 1,480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,007,300 | 67.6% |
| JUMP_BACKWARD | 1,920,200 | 32.4% |
| LOAD_GLOBAL_MODULE | 1,460 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,280 | 0.0% |
| CALL_LEN | 180 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 3,362,680 | 50.0% |
| POP_TOP | 3,361,500 | 50.0% |
| FOR_ITER_LIST | 2,760 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 580 | 0.0% |
| POP_JUMP_IF_FALSE | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 6,722,920 | 99.9% |
| END_FOR | 2,560 | 0.0% |
| POP_TOP | 2,200 | 0.0% |
| TO_BOOL_BOOL | 260 | 0.0% |
| EXIT_INIT_CHECK | 120 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 1,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,320 | 97.1% |
| LOAD_GLOBAL | 40 | 2.9% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 50.0% |
| LOAD_FAST_LOAD_FAST | 200 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 200 | 50.0% |
| LOAD_FAST | 80 | 20.0% |
| LOAD_FAST_LOAD_FAST | 60 | 15.0% |
| RETURN_CONST | 40 | 10.0% |
| LOAD_CONST | 20 | 5.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,240 | 96.9% |
| LOAD_GLOBAL | 40 | 3.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 6,721,940 | 19.3% |
| FOR_ITER_LIST | 5,442,560 | 15.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,362,680 | 9.7% |
| BUILD_LIST | 3,361,740 | 9.7% |
| FOR_ITER_TUPLE | 3,361,340 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,582,920 | 53.4% |
| LOAD_GLOBAL_BUILTIN | 6,728,160 | 19.4% |
| LOAD_FAST_LOAD_FAST | 3,362,880 | 9.7% |
| JUMP_FORWARD | 3,361,540 | 9.7% |
| LOAD_DEREF | 2,720,000 | 7.8% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,420 | 93.4% |
| CALL_LEN | 80 | 5.3% |
| FOR_ITER | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 1,400 | 92.1% |
| PUSH_NULL | 80 | 5.3% |
| TO_BOOL | 40 | 2.6% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 2,720 | 75.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 700 | 19.3% |
| COPY | 120 | 3.3% |
| UNPACK_SEQUENCE | 60 | 1.7% |
| CALL | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,760 | 76.2% |
| LOAD_FAST | 520 | 14.4% |
| LOAD_FAST_LOAD_FAST | 340 | 9.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,400 | 33.7% |
| BUILD_LIST | 1,360 | 32.7% |
| LOAD_FAST_AND_CLEAR | 1,360 | 32.7% |
| LOAD_ATTR | 40 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 1,440 | 34.6% |
| BUILD_LIST | 1,360 | 32.7% |
| FOR_ITER_LIST | 1,340 | 32.2% |
| FOR_ITER | 20 | 0.5% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 66.7% |
| FOR_ITER | 20 | 16.7% |
| LOAD_FAST | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 40 | 33.3% |
| STORE_FAST | 20 | 16.7% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,360,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,199,920 | 95.2% |
| INTERPRETER_EXIT | 160,080 | 4.8% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 260 | 39.4% |
| CACHE | 220 | 33.3% |
| POP_TOP | 40 | 6.1% |
| COPY_FREE_VARS | 40 | 6.1% |
| MAKE_CELL | 40 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 42.4% |
| LOAD_GLOBAL | 180 | 27.3% |
| NOP | 100 | 15.2% |
| POP_TOP | 40 | 6.1% |
| BUILD_LIST | 40 | 6.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,160 | 92.3% |
| LOAD_FAST_LOAD_FAST | 80 | 3.4% |
| BINARY_OP_MULTIPLY_INT | 60 | 2.6% |
| BINARY_OP | 40 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,780 | 76.1% |
| LOAD_FAST | 500 | 21.4% |
| CALL_PY_EXACT_ARGS | 40 | 1.7% |
| CALL_BUILTIN_O | 20 | 0.9% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 40 | 33.3% |
| LOAD_FAST_LOAD_FAST | 40 | 33.3% |
| CALL_METHOD_DESCRIPTOR_O | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 50.0% |
| LOAD_FAST | 60 | 50.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 60 | 60.0% |
| LOAD_CONST | 40 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 60 | 60.0% |
| LOAD_CONST | 20 | 20.0% |
| CALL_BUILTIN_O | 20 | 20.0% |


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
| CALL_LEN | 180 | 45.0% |
| LOAD_CONST | 140 | 35.0% |
| LOAD_FAST | 80 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 180 | 45.0% |
| LOAD_FAST_LOAD_FAST | 80 | 20.0% |
| STORE_FAST | 60 | 15.0% |
| LOAD_CONST | 40 | 10.0% |
| LOAD_FAST | 40 | 10.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 60 | 50.0% |
| BUILD_TUPLE | 40 | 33.3% |
| LOAD_FAST | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60 | 50.0% |
| PUSH_EXC_INFO | 40 | 33.3% |
| RETURN_VALUE | 20 | 16.7% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 52.6% |
| LOAD_CONST | 180 | 47.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 380 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,440 | 42.9% |
| LOAD_FAST_LOAD_FAST | 1,240 | 36.9% |
| LOAD_FAST | 620 | 18.5% |
| BINARY_SUBSCR | 60 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,600 | 79.3% |
| RETURN_VALUE | 620 | 18.9% |
| LOAD_CONST | 40 | 1.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20 | 0.6% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 60.0% |
| LOAD_CONST | 300 | 33.3% |
| LOAD_FAST_LOAD_FAST | 40 | 4.4% |
| BINARY_SUBSCR | 20 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 53.3% |
| LOAD_CONST | 260 | 28.9% |
| BINARY_OP_INPLACE_ADD_UNICODE | 80 | 8.9% |
| PUSH_EXC_INFO | 40 | 4.4% |
| CALL_BUILTIN_O | 40 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 560 | 96.6% |
| BINARY_SUBSCR | 20 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 200 | 34.5% |
| CALL_BUILTIN_O | 140 | 24.1% |
| BINARY_OP_MULTIPLY_INT | 60 | 10.3% |
| LOAD_FAST | 40 | 6.9% |
| CALL_PY_EXACT_ARGS | 40 | 6.9% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |
| LOAD_GLOBAL_MODULE | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 120 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,400 | 65.4% |
| PUSH_NULL | 300 | 14.0% |
| LOAD_CONST | 240 | 11.2% |
| BUILD_TUPLE | 100 | 4.7% |
| CALL | 60 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,140 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,280 | 46.4% |
| LOAD_FAST | 1,280 | 46.4% |
| CALL_LEN | 100 | 3.6% |
| CALL | 80 | 2.9% |
| CALL_BUILTIN_FAST | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,640 | 95.7% |
| LOAD_CONST | 80 | 2.9% |
| GET_ITER | 20 | 0.7% |
| RETURN_VALUE | 20 | 0.7% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 1,240 | 48.8% |
| LOAD_FAST_LOAD_FAST | 1,240 | 48.8% |
| CALL | 40 | 1.6% |
| LOAD_FAST | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,260 | 49.6% |
| STORE_FAST | 1,260 | 49.6% |
| CALL_BUILTIN_CLASS | 20 | 0.8% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,363,900 | 100.0% |
| LOAD_DEREF | 1,320 | 0.0% |
| CALL | 80 | 0.0% |
| CALL_TUPLE_1 | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,362,680 | 99.9% |
| GET_ITER | 1,340 | 0.0% |
| RETURN_VALUE | 1,320 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_STR_1 | 1,400 | 36.8% |
| LOAD_ATTR_SLOT | 1,240 | 32.6% |
| LOAD_FAST | 580 | 15.3% |
| BINARY_SUBSCR_TUPLE_INT | 140 | 3.7% |
| RETURN_VALUE | 100 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 1,420 | 37.4% |
| RETURN_VALUE | 1,260 | 33.2% |
| POP_TOP | 1,000 | 26.3% |
| BUILD_TUPLE | 120 | 3.2% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,363,420 | 50.0% |
| LOAD_GLOBAL_MODULE | 3,361,400 | 50.0% |
| BUILD_TUPLE | 80 | 0.0% |
| CALL | 80 | 0.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,724,820 | 100.0% |
| RETURN_VALUE | 80 | 0.0% |
| TO_BOOL | 80 | 0.0% |
| LOAD_FAST | 40 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,900 | 90.8% |
| LOAD_ATTR_INSTANCE_VALUE | 320 | 4.2% |
| POP_JUMP_IF_TRUE | 180 | 2.4% |
| CALL | 120 | 1.6% |
| LOAD_GLOBAL_MODULE | 80 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 3,720 | 48.9% |
| LOAD_CONST | 2,860 | 37.6% |
| RETURN_VALUE | 320 | 4.2% |
| BINARY_OP_SUBTRACT_INT | 180 | 2.4% |
| LOAD_GLOBAL_MODULE | 120 | 1.6% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,520 | 100.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |
| CALL | 20 | 0.0% |
| LOAD_CONST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,361,340 | 100.0% |
| RETURN_CONST | 200 | 0.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 60.0% |
| LOAD_CONST | 40 | 20.0% |
| LOAD_FAST_LOAD_FAST | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,320 | 98.5% |
| CALL | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,340 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 37.5% |
| CALL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |
| RETURN_VALUE | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 37.5% |
| POP_TOP | 40 | 25.0% |
| BINARY_OP_ADD_UNICODE | 40 | 25.0% |
| BINARY_OP | 20 | 12.5% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,362,940 | 99.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,800 | 0.1% |
| GET_ITER | 1,320 | 0.0% |
| LOAD_DEREF | 1,240 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,365,660 | 99.8% |
| MAKE_CELL | 2,560 | 0.1% |
| COPY_FREE_VARS | 1,340 | 0.0% |
| RETURN_GENERATOR | 1,260 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 50.0% |
| LOAD_FAST_LOAD_FAST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,725,240 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,363,900 | 50.0% |
| STORE_FAST | 3,359,980 | 50.0% |
| CALL_BUILTIN_O | 1,400 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,340 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 3,361,260 | 100.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 3,720 | 53.9% |
| LOAD_CONST | 2,860 | 41.4% |
| COMPARE_OP | 140 | 2.0% |
| LOAD_GLOBAL_MODULE | 140 | 2.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,320 | 62.6% |
| EXTENDED_ARG | 1,260 | 18.3% |
| STORE_FAST | 1,260 | 18.3% |
| POP_JUMP_IF_TRUE | 60 | 0.9% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,720 | 80.6% |
| LOAD_FAST | 1,360 | 14.2% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 2.9% |
| COMPARE_OP | 220 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,900 | 82.5% |
| POP_JUMP_IF_TRUE | 1,480 | 15.4% |
| EXTENDED_ARG | 200 | 2.1% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,199,920 | 99.9% |
| GET_ITER | 2,480 | 0.1% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,199,980 | 99.9% |
| POP_TOP | 2,480 | 0.1% |
| RESUME | 20 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,442,640 | 99.9% |
| GET_ITER | 2,620 | 0.0% |
| LOAD_FAST | 1,340 | 0.0% |
| SWAP | 1,340 | 0.0% |
| EXTENDED_ARG | 720 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,442,560 | 99.9% |
| RETURN_CONST | 2,760 | 0.1% |
| STORE_FAST_LOAD_FAST | 1,420 | 0.0% |
| JUMP_BACKWARD | 1,280 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 520 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 820 | 82.0% |
| GET_ITER | 160 | 16.0% |
| FOR_ITER | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 820 | 82.0% |
| LOAD_FAST | 100 | 10.0% |
| LOAD_GLOBAL | 40 | 4.0% |
| LOAD_GLOBAL_MODULE | 40 | 4.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,361,340 | 50.0% |
| JUMP_BACKWARD | 3,361,340 | 50.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,361,360 | 50.0% |
| STORE_FAST | 3,361,340 | 50.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,000 | 98.0% |
| LOAD_ATTR | 80 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 4,000 | 98.0% |
| LOAD_ATTR | 80 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,120 | 85.8% |
| LOAD_FAST_LOAD_FAST | 480 | 10.0% |
| LOAD_ATTR_INSTANCE_VALUE | 200 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,400 | 29.2% |
| STORE_FAST | 1,160 | 24.2% |
| CALL_LEN | 320 | 6.7% |
| COMPARE_OP_STR | 280 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 220 | 4.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,733,720 | 79.8% |
| LOAD_DEREF | 2,719,960 | 20.2% |
| LOAD_ATTR | 480 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 220 | 0.0% |
| LOAD_GLOBAL_MODULE | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,086,840 | 75.0% |
| CALL | 3,361,260 | 25.0% |
| CALL_PY_EXACT_ARGS | 3,800 | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,300 | 0.0% |
| LOAD_CONST | 1,260 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 780 | 90.7% |
| BINARY_SUBSCR | 40 | 4.7% |
| BINARY_SUBSCR_TUPLE_INT | 40 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 780 | 90.7% |
| LOAD_CONST | 40 | 4.7% |
| LOAD_FAST | 40 | 4.7% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,729,480 | 66.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 3,363,680 | 33.3% |
| LOAD_ATTR_CLASS | 4,000 | 0.0% |
| LOAD_ATTR | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 6,729,680 | 66.6% |
| FORMAT_SIMPLE | 3,359,980 | 33.3% |
| STORE_FAST | 3,940 | 0.0% |
| LOAD_FAST | 2,600 | 0.0% |
| BUILD_TUPLE | 1,260 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,364,920 | 100.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 3,363,680 | 100.0% |
| CALL | 1,260 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| LOAD_FAST_LOAD_FAST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 20 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 50.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,085,000 | 100.0% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,085,280 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,371,780 | 100.0% |
| RETURN_VALUE | 1,240 | 0.0% |
| LOAD_ATTR | 180 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |
| LOAD_ATTR_SLOT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 16,807,800 | 86.8% |
| STORE_FAST | 2,561,320 | 13.2% |
| PUSH_EXC_INFO | 1,400 | 0.0% |
| SWAP | 1,400 | 0.0% |
| CALL_BUILTIN_O | 1,240 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,086,400 | 37.5% |
| STORE_FAST | 6,728,160 | 25.0% |
| POP_JUMP_IF_FALSE | 6,724,020 | 25.0% |
| LOAD_FAST | 3,367,260 | 12.5% |
| PUSH_EXC_INFO | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,823,280 | 62.5% |
| CALL_ISINSTANCE | 3,363,420 | 12.5% |
| LOAD_ATTR | 3,361,360 | 12.5% |
| LOAD_DEREF | 3,361,340 | 12.5% |
| CHECK_EXC_MATCH | 1,480 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,726,260 | 50.0% |
| RESUME_CHECK | 3,365,360 | 25.0% |
| NOP | 3,362,600 | 25.0% |
| STORE_FAST | 2,000 | 0.0% |
| POP_JUMP_IF_TRUE | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 6,729,480 | 50.0% |
| IS_OP | 3,363,080 | 25.0% |
| CALL_ISINSTANCE | 3,361,400 | 25.0% |
| LOAD_FAST | 3,180 | 0.0% |
| LOAD_FAST_LOAD_FAST | 3,040 | 0.0% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,320 | 100.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 3,361,340 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 16,971,260 | 38.8% |
| LOAD_ATTR_PROPERTY | 10,085,280 | 23.1% |
| CALL | 6,723,880 | 15.4% |
| CALL_PY_EXACT_ARGS | 3,365,660 | 7.7% |
| COPY_FREE_VARS | 3,361,400 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 16,810,480 | 38.5% |
| LOAD_GLOBAL_BUILTIN | 10,086,400 | 23.1% |
| LOAD_FAST | 6,732,280 | 15.4% |
| LOAD_GLOBAL_MODULE | 3,365,360 | 7.7% |
| BUILD_LIST | 3,361,460 | 7.7% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,020 | 54.3% |
| LOAD_FAST_LOAD_FAST | 820 | 43.6% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 580 | 30.9% |
| LOAD_FAST_LOAD_FAST | 500 | 26.6% |
| LOAD_FAST | 360 | 19.1% |
| LOAD_CONST | 280 | 14.9% |
| BUILD_MAP | 80 | 4.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,441,240 | 66.7% |
| LOAD_FAST_LOAD_FAST | 6,725,240 | 33.3% |
| STORE_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,080,000 | 50.0% |
| RETURN_CONST | 3,362,680 | 16.7% |
| LOAD_FAST_LOAD_FAST | 3,362,660 | 16.7% |
| LOAD_CONST | 3,361,340 | 16.7% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 50.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 80.0% |
| LOAD_FAST | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60 | 60.0% |
| EXTENDED_ARG | 20 | 20.0% |
| LOAD_FAST | 20 | 20.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 639,120 | 98.6% |
| TO_BOOL_NONE | 8,960 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 639,140 | 98.6% |
| TO_BOOL_NONE | 8,940 | 1.4% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 6,724,820 | 72.4% |
| LOAD_FAST | 2,560,040 | 27.6% |
| RETURN_VALUE | 1,360 | 0.0% |
| COPY | 1,340 | 0.0% |
| CALL | 1,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,927,700 | 63.8% |
| POP_JUMP_IF_TRUE | 3,361,540 | 36.2% |
| EXTENDED_ARG | 60 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 660 | 55.9% |
| LOAD_FAST | 420 | 35.6% |
| COPY | 80 | 6.8% |
| TO_BOOL | 20 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 800 | 67.8% |
| POP_JUMP_IF_TRUE | 300 | 25.4% |
| UNARY_NOT | 80 | 6.8% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,360,200 | 100.0% |
| RETURN_VALUE | 1,240 | 0.0% |
| TO_BOOL | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,360,140 | 100.0% |
| POP_JUMP_IF_TRUE | 1,320 | 0.0% |
| UNARY_NOT | 40 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,920,840 | 99.5% |
| TO_BOOL_ALWAYS_TRUE | 8,940 | 0.5% |
| LOAD_FAST | 1,480 | 0.1% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,920,840 | 99.5% |
| TO_BOOL_ALWAYS_TRUE | 8,960 | 0.5% |
| POP_JUMP_IF_FALSE | 1,500 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,720 | 39.0% |
| RETURN_VALUE | 2,480 | 35.5% |
| STORE_FAST_LOAD_FAST | 1,400 | 20.1% |
| COPY | 220 | 3.2% |
| TO_BOOL | 160 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,660 | 81.1% |
| POP_JUMP_IF_FALSE | 1,320 | 18.9% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,680 | 95.7% |
| LOAD_FAST | 60 | 2.1% |
| UNPACK_SEQUENCE | 40 | 1.4% |
| BINARY_SUBSCR_TUPLE_INT | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,720 | 97.1% |
| STORE_FAST | 80 | 2.9% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 520 | 56.5% |
| RETURN_VALUE | 360 | 39.1% |
| LOAD_CONST | 20 | 2.2% |
| BINARY_SUBSCR_LIST_INT | 20 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 700 | 76.1% |
| STORE_FAST | 220 | 23.9% |


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
|     deferred | 3,361,320 | 99.9% |
|          hit | 3,100 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 8.6% |
| Failure | 1,060 | 91.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 1,020 | 96.2% |
| and int | 20 | 1.9% |
| multiply different types | 20 | 1.9% |


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
|     deferred | 2,800 | 33.2% |
|          hit | 5,220 | 61.8% |
|         miss | 120 | 1.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 33.3% |
| Failure | 200 | 66.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 200 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,652,220 | 32.0% |
|          hit | 26,932,380 | 68.0% |
|         miss | 20 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 920 | 14.5% |
| Failure | 5,440 | 85.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 3,120 | 57.4% |
| cfunc varargs keywords | 1,020 | 18.8% |
| cmethod | 820 | 15.1% |
| other | 200 | 3.7% |
| cfunc varargs | 100 | 1.8% |
| meth descr varargs | 100 | 1.8% |
| cfunc noargs | 60 | 1.1% |
| class mutable | 20 | 0.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 760 | 4.3% |
|          hit | 16,440 | 93.4% |
|         miss | 40 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 360 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 15,374,700 | 100.0% |
|         miss | 240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 91.7% |
| Failure | 20 | 8.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 20 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,365,260 | 5.6% |
|          hit | 56,384,100 | 94.4% |
|         miss | 1,420 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,480 | 56.1% |
| Failure | 1,160 | 43.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 1,040 | 89.7% |
| class method obj | 120 | 10.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,360 | 0.0% |
|          hit | 40,375,360 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 980 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 3,361,340 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
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
|     deferred | 200 | 0.0% |
|          hit | 20,168,560 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 30.8% |
|          hit | 180 | 69.2% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,344,260 | 18.0% |
|          hit | 14,289,340 | 76.8% |
|         miss | 949,000 | 5.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 18,340 | 94.6% |
| Failure | 1,040 | 5.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 1,040 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 2.1% |
|          hit | 3,720 | 96.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 359,165,380 | 57.4% |
| Not specialized | 44,732,760 | 7.2% |
| Specialized hits | 220,628,900 | 35.3% |
| Specialized misses | 950,880 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 12,652,220 | 55.7% |
| LOAD_ATTR | 3,365,260 | 14.8% |
| BINARY_OP | 3,361,320 | 14.8% |
| TO_BOOL | 3,344,260 | 14.7% |
| BINARY_SUBSCR | 2,800 | 0.0% |
| LOAD_GLOBAL | 1,360 | 0.0% |
| COMPARE_OP | 760 | 0.0% |
| FOR_ITER | 340 | 0.0% |
| STORE_ATTR | 200 | 0.0% |
| STORE_SUBSCR | 80 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL_NONE | 474,920 | 49.9% |
| TO_BOOL_ALWAYS_TRUE | 474,000 | 49.8% |
| LOAD_ATTR_SLOT | 1,420 | 0.1% |
| FOR_ITER_LIST | 240 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 80 | 0.0% |
| RESUME | 40 | 0.0% |
| BINARY_SUBSCR_STR_INT | 40 | 0.0% |
| COMPARE_OP_STR | 40 | 0.0% |
| RESUME_CHECK | 40 | 0.0% |
| TO_BOOL_INT | 40 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 20,333,000 | 46.5% |
| Calls to Python functions inlined | 23,387,020 | 53.5% |
| Calls via PyEval_EvalFrame (total) | 20,333,000 | 46.5% |
| Calls via PyEval_EvalFrame (vector) | 20,172,840 | 46.1% |
| Calls via PyEval_EvalFrame (generator) | 160,160 | 0.4% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 20,172,840 | 46.1% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 6,724,460 | 15.4% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 240 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 1,680 | 0.0% |
| Frames pushed | 13,458,940 | 30.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 43,399,280 | 28.8% |
| Frees to freelist | 43,400,520 |  |
| Allocations | 107,268,360 | 71.2% |
| Allocations to 512 bytes | 107,268,320 | 71.2% |
| Allocations to 4 kbytes | 40 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 116,559,602 |  |
| New values | 80 |  |
| Interpreter increfs | 335,166,240 | 78.7% |
| Interpreter decrefs | 359,225,860 | 63.6% |
| Increfs | 90,499,000 | 21.3% |
| Decrefs | 205,267,663 | 36.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 9,190 |  |
| Method cache misses | 790 |  |
| Method cache collisions | 725 |  |
| Method cache dunder hits | 30,263,572 |  |
| Method cache dunder misses | 188 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 620 | 1,920 | 3,503,120 |
| 1 | 40 | 0 | 1,152,000 |
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
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
