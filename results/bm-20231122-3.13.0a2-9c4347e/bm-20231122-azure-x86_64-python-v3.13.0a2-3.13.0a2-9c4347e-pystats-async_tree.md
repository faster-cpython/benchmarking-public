
# Pystats results

- benchmark: async_tree
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 424,813,520 | 18.5% | 18.5% |  |
| POP_JUMP_IF_FALSE | 135,872,680 | 5.9% | 24.4% |  |
| RESUME_CHECK | 110,493,140 | 4.8% | 29.2% | 0.0% |
| STORE_FAST | 100,053,280 | 4.4% | 33.5% |  |
| LOAD_FAST_LOAD_FAST | 100,033,880 | 4.4% | 37.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 95,572,700 | 4.2% | 42.0% |  |
| LOAD_CONST | 89,594,660 | 3.9% | 45.9% |  |
| TO_BOOL_BOOL | 89,582,380 | 3.9% | 49.8% |  |
| LOAD_ATTR_SLOT | 72,410,200 | 3.1% | 53.0% |  |
| POP_TOP | 70,925,500 | 3.1% | 56.1% |  |
| STORE_ATTR_SLOT | 67,931,820 | 3.0% | 59.0% |  |
| CALL_PY_EXACT_ARGS | 61,222,780 | 2.7% | 61.7% |  |
| RETURN_CONST | 60,472,860 | 2.6% | 64.3% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 51,516,760 | 2.2% | 66.6% |  |
| RETURN_VALUE | 49,275,320 | 2.1% | 68.7% |  |
| LOAD_ATTR_METHOD_NO_DICT | 47,031,840 | 2.0% | 70.7% |  |
| LOAD_ATTR | 46,305,840 | 2.0% | 72.8% |  |
| INTERPRETER_EXIT | 44,043,880 | 1.9% | 74.7% |  |
| LOAD_GLOBAL_MODULE | 40,317,460 | 1.8% | 76.4% |  |
| PUSH_NULL | 40,314,660 | 1.8% | 78.2% |  |
| LOAD_DEREF | 40,311,140 | 1.8% | 79.9% |  |
| CALL | 38,838,960 | 1.7% | 81.6% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 32,185,760 | 1.4% | 83.0% | 14.2% |
| POP_JUMP_IF_NOT_NONE | 28,369,080 | 1.2% | 84.3% |  |
| LOAD_ATTR_MODULE | 25,384,240 | 1.1% | 85.4% |  |
| TO_BOOL_NONE | 23,887,700 | 1.0% | 86.4% |  |
| JUMP_BACKWARD | 23,142,600 | 1.0% | 87.4% |  |
| CALL_METHOD_DESCRIPTOR_O | 18,662,420 | 0.8% | 88.2% | 0.0% |
| NOP | 14,932,960 | 0.6% | 88.9% |  |
| FOR_ITER_RANGE | 14,931,320 | 0.6% | 89.5% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.6% | 90.1% |  |
| BUILD_LIST | 12,692,160 | 0.6% | 90.6% |  |
| STORE_DEREF | 12,690,160 | 0.6% | 91.2% |  |
| LOAD_GLOBAL_BUILTIN | 10,459,920 | 0.5% | 91.7% | 0.0% |
| CALL_FUNCTION_EX | 10,451,120 | 0.5% | 92.1% |  |
| CALL_KW | 10,450,960 | 0.5% | 92.6% |  |
| POP_JUMP_IF_TRUE | 9,708,340 | 0.4% | 93.0% |  |
| CALL_INTRINSIC_1 | 9,704,400 | 0.4% | 93.4% |  |
| LIST_EXTEND | 9,704,400 | 0.4% | 93.8% |  |
| COMPARE_OP_INT | 8,961,460 | 0.4% | 94.2% |  |
| CONTAINS_OP | 8,957,920 | 0.4% | 94.6% |  |
| BINARY_OP_ADD_INT | 8,957,780 | 0.4% | 95.0% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.4% | 95.4% |  |
| RETURN_GENERATOR | 8,211,600 | 0.4% | 95.7% |  |
| FOR_ITER_LIST | 5,975,020 | 0.3% | 96.0% |  |
| TO_BOOL | 5,230,980 | 0.2% | 96.2% |  |
| STORE_ATTR | 5,229,960 | 0.2% | 96.5% |  |
| COPY_FREE_VARS | 5,226,420 | 0.2% | 96.7% |  |
| FOR_ITER_TUPLE | 5,225,380 | 0.2% | 96.9% |  |
| JUMP_FORWARD | 4,482,660 | 0.2% | 97.1% |  |
| TO_BOOL_LIST | 4,482,200 | 0.2% | 97.3% |  |
| COPY | 4,481,220 | 0.2% | 97.5% |  |
| IS_OP | 4,479,280 | 0.2% | 97.7% |  |
| END_SEND | 4,479,120 | 0.2% | 97.9% |  |
| GET_AWAITABLE | 4,479,120 | 0.2% | 98.1% |  |
| CALL_BUILTIN_FAST | 4,479,120 | 0.2% | 98.3% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 98.5% |  |
| BINARY_OP_SUBTRACT_INT | 4,478,920 | 0.2% | 98.7% |  |
| STORE_SUBSCR_DICT | 4,478,920 | 0.2% | 98.9% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 99.1% |  |
| SEND_GEN | 3,732,740 | 0.2% | 99.2% |  |
| MAKE_CELL | 3,732,480 | 0.2% | 99.4% |  |
| GET_ITER | 2,990,980 | 0.1% | 99.5% |  |
| SWAP | 2,239,780 | 0.1% | 99.6% |  |
| SEND | 1,493,640 | 0.1% | 99.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.7% |  |
| CALL_BUILTIN_CLASS | 748,760 | 0.0% | 99.7% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.8% |  |
| LOAD_SUPER_ATTR_METHOD | 747,080 | 0.0% | 99.8% |  |
| BUILD_MAP | 746,880 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 746,640 | 0.0% | 99.9% |  |
| YIELD_VALUE | 746,640 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| CALL_LEN | 4,740 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,940 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 1,960 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,780 | 0.0% | 100.0% |  |
| RESUME | 1,640 | 0.0% | 100.0% | 2,653.7% |
| BINARY_OP_ADD_FLOAT | 1,580 | 0.0% | 100.0% |  |
| BINARY_OP | 880 | 0.0% | 100.0% |  |
| FOR_ITER | 560 | 0.0% | 100.0% |  |
| COMPARE_OP | 540 | 0.0% | 100.0% |  |
| CALL_ISINSTANCE | 520 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 420 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 380 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 200 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 120 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 120 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 100 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |
| BEFORE_WITH | 40 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 40 | 0.0% | 100.0% |  |
| IMPORT_FROM | 20 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 20 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 20 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 20 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 90,345,600 | 3.9% | 3.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 80,623,920 | 3.5% | 7.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 79,131,180 | 3.4% | 10.9% |
| STORE_FAST LOAD_FAST | 75,407,960 | 3.3% | 14.2% |
| LOAD_FAST LOAD_ATTR_SLOT | 72,409,840 | 3.1% | 17.3% |
| RESUME_CHECK LOAD_FAST | 67,936,760 | 3.0% | 20.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 53,010,760 | 2.3% | 22.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 38,817,760 | 1.7% | 24.3% |
| LOAD_FAST LOAD_ATTR | 36,583,940 | 1.6% | 25.8% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 36,583,680 | 1.6% | 27.4% |
| LOAD_CONST LOAD_FAST | 34,341,860 | 1.5% | 28.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 34,340,440 | 1.5% | 30.4% |
| CACHE RESUME_CHECK | 34,339,220 | 1.5% | 31.9% |
| LOAD_FAST STORE_ATTR_SLOT | 29,113,800 | 1.3% | 33.2% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 29,113,380 | 1.3% | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 28,368,820 | 1.2% | 35.7% |
| RETURN_CONST INTERPRETER_EXIT | 28,367,340 | 1.2% | 36.9% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 27,624,320 | 1.2% | 38.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 25,383,560 | 1.1% | 39.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 25,383,320 | 1.1% | 40.3% |
| RETURN_CONST POP_TOP | 23,893,800 | 1.0% | 41.4% |
| POP_TOP LOAD_FAST | 23,891,240 | 1.0% | 42.4% |
| LOAD_FAST RETURN_VALUE | 23,890,260 | 1.0% | 43.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,889,760 | 1.0% | 44.5% |
| CALL STORE_FAST | 23,888,300 | 1.0% | 45.5% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 23,887,700 | 1.0% | 46.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 23,141,220 | 1.0% | 47.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 22,395,260 | 1.0% | 48.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 19,412,840 | 0.8% | 49.4% |
| PUSH_NULL LOAD_FAST | 19,409,360 | 0.8% | 50.2% |
| STORE_ATTR_SLOT LOAD_CONST | 19,409,120 | 0.8% | 51.1% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 19,408,720 | 0.8% | 51.9% |
| POP_JUMP_IF_FALSE LOAD_CONST | 18,665,760 | 0.8% | 52.7% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 18,662,400 | 0.8% | 53.5% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,480 | 0.8% | 54.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 17,915,440 | 0.8% | 55.1% |
| LOAD_CONST STORE_FAST | 14,937,840 | 0.6% | 55.7% |
| NOP LOAD_FAST | 14,932,400 | 0.6% | 56.4% |
| RETURN_VALUE STORE_FAST | 14,932,140 | 0.6% | 57.0% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 14,930,340 | 0.6% | 57.7% |
| RETURN_VALUE INTERPRETER_EXIT | 14,930,060 | 0.6% | 58.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 14,185,420 | 0.6% | 59.0% |
| POP_TOP RETURN_CONST | 14,184,520 | 0.6% | 59.6% |
| RETURN_VALUE TO_BOOL_BOOL | 14,183,840 | 0.6% | 60.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,183,760 | 0.6% | 60.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,183,760 | 0.6% | 61.4% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,183,600 | 0.6% | 62.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 14,183,560 | 0.6% | 62.7% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,183,280 | 0.6% | 63.3% |
| JUMP_BACKWARD FOR_ITER_RANGE | 14,183,240 | 0.6% | 63.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 14,183,240 | 0.6% | 64.5% |
| FOR_ITER_RANGE STORE_FAST | 14,183,240 | 0.6% | 65.1% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,436,800 | 0.6% | 65.7% |
| LOAD_FAST LOAD_CONST | 10,452,980 | 0.5% | 66.2% |
| RESUME_CHECK NOP | 10,451,500 | 0.5% | 66.6% |
| LOAD_CONST CALL_KW | 10,450,960 | 0.5% | 67.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 9,708,300 | 0.4% | 67.5% |
| POP_TOP LOAD_CONST | 9,706,740 | 0.4% | 67.9% |
| LOAD_FAST CALL | 9,706,120 | 0.4% | 68.3% |
| STORE_FAST RETURN_CONST | 9,706,000 | 0.4% | 68.8% |
| LOAD_ATTR PUSH_NULL | 9,705,160 | 0.4% | 69.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,800 | 0.4% | 69.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,704,660 | 0.4% | 70.0% |
| STORE_ATTR_SLOT LOAD_FAST | 9,704,660 | 0.4% | 70.4% |
| STORE_ATTR_SLOT RETURN_CONST | 9,704,660 | 0.4% | 70.9% |
| BUILD_LIST LOAD_FAST | 9,704,640 | 0.4% | 71.3% |
| CALL_FUNCTION_EX POP_TOP | 9,704,560 | 0.4% | 71.7% |
| LOAD_FAST_LOAD_FAST CALL | 9,704,560 | 0.4% | 72.1% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 9,704,480 | 0.4% | 72.6% |
| LOAD_ATTR_SLOT LOAD_ATTR | 9,704,480 | 0.4% | 73.0% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 0.4% | 73.4% |
| POP_TOP JUMP_BACKWARD | 9,704,440 | 0.4% | 73.8% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 9,704,400 | 0.4% | 74.2% |
| LIST_EXTEND CALL_INTRINSIC_1 | 9,704,400 | 0.4% | 74.7% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 9,704,400 | 0.4% | 75.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 9,704,380 | 0.4% | 75.5% |
| LOAD_ATTR_SLOT BUILD_LIST | 9,704,380 | 0.4% | 75.9% |
| LOAD_ATTR_SLOT LIST_EXTEND | 9,704,380 | 0.4% | 76.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 8,965,380 | 0.4% | 76.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 8,961,460 | 0.4% | 77.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 8,960,400 | 0.4% | 77.5% |
| LOAD_ATTR CALL | 8,959,560 | 0.4% | 77.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 8,958,400 | 0.4% | 78.3% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.4% | 78.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 8,958,060 | 0.4% | 79.1% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 8,957,920 | 0.4% | 79.5% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.4% | 79.9% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,957,920 | 0.4% | 80.3% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.4% | 80.6% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,957,720 | 0.4% | 81.0% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.4% | 81.4% |
| CALL_LIST_APPEND JUMP_BACKWARD | 8,957,720 | 0.4% | 81.8% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.4% | 82.2% |
| POP_TOP RESUME_CHECK | 8,211,520 | 0.4% | 82.6% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,211,380 | 0.4% | 82.9% |
| PUSH_NULL CALL | 5,974,780 | 0.3% | 83.2% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 5,972,200 | 0.3% | 83.4% |
| CALL POP_TOP | 5,226,120 | 0.2% | 83.7% |
| COPY_FREE_VARS RESUME_CHECK | 5,226,020 | 0.2% | 83.9% |
| LOAD_FAST PUSH_NULL | 5,225,860 | 0.2% | 84.1% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 34,339,220 | 78.0% |
| COPY_FREE_VARS | 5,225,480 | 11.9% |
| POP_TOP | 4,478,960 | 10.2% |
| RESUME | 220 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 40 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 20 | 50.0% |
| BINARY_SUBSCR_DICT | 20 | 50.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 160 | 88.9% |
| LOAD_GLOBAL | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 180 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,732,640 | 83.3% |
| SEND | 746,480 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,479,120 | 100.0% |


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

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,496,180 | 50.0% |
| CALL_BUILTIN_CLASS | 748,100 | 25.0% |
| LOAD_DEREF | 746,480 | 25.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 160 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,496,060 | 50.0% |
| LOAD_FAST_AND_CLEAR | 746,480 | 25.0% |
| FOR_ITER_TUPLE | 746,480 | 25.0% |
| FOR_ITER_RANGE | 1,580 | 0.1% |
| FOR_ITER | 380 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 28,367,340 | 64.4% |
| RETURN_VALUE | 14,930,060 | 33.9% |
| YIELD_VALUE | 746,480 | 1.7% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 746,720 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,451,500 | 70.0% |
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 25.0% |
| STORE_FAST | 748,240 | 5.0% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,932,400 | 100.0% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 100 | 55.6% |
| COPY | 80 | 44.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 100 | 55.6% |
| RERAISE | 80 | 44.4% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 23,893,800 | 33.7% |
| CALL_METHOD_DESCRIPTOR_O | 18,662,400 | 26.3% |
| CALL_FUNCTION_EX | 9,704,560 | 13.7% |
| CALL | 5,226,120 | 7.4% |
| END_SEND | 4,479,120 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,891,240 | 33.7% |
| RETURN_CONST | 14,184,520 | 20.0% |
| LOAD_CONST | 9,706,740 | 13.7% |
| JUMP_BACKWARD | 9,704,440 | 13.7% |
| RESUME_CHECK | 8,211,520 | 11.6% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 80 | 44.4% |
| BINARY_SUBSCR_DICT | 80 | 44.4% |
| BINARY_SUBSCR | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 160 | 88.9% |
| LOAD_GLOBAL | 20 | 11.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 25,383,560 | 63.0% |
| LOAD_ATTR | 9,705,160 | 24.1% |
| LOAD_FAST | 5,225,860 | 13.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,409,360 | 48.1% |
| LOAD_FAST_LOAD_FAST | 14,183,600 | 35.2% |
| CALL | 5,974,780 | 14.8% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 1.9% |
| LOAD_CONST | 240 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 8,211,380 | 100.0% |
| CALL | 80 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 4,478,880 | 54.5% |
| GET_AWAITABLE | 3,732,640 | 45.5% |
| CALL | 40 | 0.0% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,890,260 | 48.5% |
| LOAD_ATTR_INSTANCE_VALUE | 14,930,340 | 30.3% |
| RETURN_VALUE | 4,479,360 | 9.1% |
| POP_JUMP_IF_FALSE | 4,479,040 | 9.1% |
| CALL | 748,380 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,932,140 | 30.3% |
| INTERPRETER_EXIT | 14,930,060 | 30.3% |
| TO_BOOL_BOOL | 14,183,840 | 28.8% |
| RETURN_VALUE | 4,479,360 | 9.1% |
| GET_AWAITABLE | 746,480 | 1.5% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 60.0% |
| LOAD_ATTR | 40 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| STORE_SUBSCR_DICT | 40 | 40.0% |
| LOAD_CONST | 20 | 20.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,480,780 | 85.7% |
| LOAD_FAST | 746,640 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |
| LOAD_ATTR | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,479,800 | 85.6% |
| POP_JUMP_IF_TRUE | 748,300 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| TO_BOOL_BOOL | 800 | 0.0% |
| TO_BOOL_INT | 160 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 80 | 50.0% |
| LOAD_ATTR_MODULE | 60 | 37.5% |
| LOAD_ATTR | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 160 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 60 | 37.5% |
| TO_BOOL_INT | 60 | 37.5% |
| TO_BOOL | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 22.7% |
| LOAD_GLOBAL_MODULE | 180 | 20.5% |
| UNARY_INVERT | 160 | 18.2% |
| BINARY_OP | 120 | 13.6% |
| POP_JUMP_IF_FALSE | 80 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 22.7% |
| COPY | 160 | 18.2% |
| BINARY_OP | 120 | 13.6% |
| UNARY_INVERT | 80 | 9.1% |
| BINARY_OP_ADD_INT | 60 | 6.8% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,704,380 | 76.5% |
| STORE_FAST | 748,080 | 5.9% |
| POP_JUMP_IF_FALSE | 746,480 | 5.9% |
| STORE_DEREF | 746,480 | 5.9% |
| SWAP | 746,480 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,704,640 | 76.5% |
| STORE_FAST | 1,494,560 | 11.8% |
| STORE_DEREF | 746,480 | 5.9% |
| SWAP | 746,480 | 5.9% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 99.9% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 99.9% |
| LOAD_FAST | 400 | 0.1% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,720 | 99.9% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,720 | 99.9% |
| CALL | 160 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |
| BUILD_MAP | 80 | 0.0% |
| CALL_ISINSTANCE | 40 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,706,120 | 25.0% |
| LOAD_FAST_LOAD_FAST | 9,704,560 | 25.0% |
| LOAD_ATTR | 8,959,560 | 23.1% |
| PUSH_NULL | 5,974,780 | 15.4% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,080 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,888,300 | 61.5% |
| POP_TOP | 5,226,120 | 13.5% |
| RESUME_CHECK | 4,479,500 | 11.5% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,040 | 11.5% |
| RETURN_VALUE | 748,380 | 1.9% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 9,704,400 | 92.9% |
| STORE_FAST | 746,480 | 7.1% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,704,560 | 92.9% |
| MAKE_CELL | 746,480 | 7.1% |
| COPY_FREE_VARS | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 9,704,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,704,400 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,450,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 42.9% |
| RESUME_CHECK | 4,478,940 | 42.9% |
| POP_TOP | 746,560 | 7.1% |
| STORE_DEREF | 746,480 | 7.1% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220 | 40.7% |
| CALL_BUILTIN_CLASS | 140 | 25.9% |
| COMPARE_OP | 40 | 7.4% |
| LOAD_DEREF | 40 | 7.4% |
| RETURN_VALUE | 20 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 340 | 63.0% |
| COMPARE_OP_INT | 140 | 25.9% |
| COMPARE_OP | 40 | 7.4% |
| COPY | 20 | 3.7% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,478,940 | 50.0% |
| LOAD_FAST_LOAD_FAST | 4,478,880 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,957,920 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 4,479,020 | 100.0% |
| CALL_LEN | 1,580 | 0.0% |
| BINARY_OP | 160 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| UNARY_NOT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 4,479,080 | 100.0% |
| TO_BOOL_INT | 1,640 | 0.0% |
| TO_BOOL | 240 | 0.0% |
| POP_EXCEPT | 80 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 5,225,480 | 100.0% |
| CALL_PY_EXACT_ARGS | 640 | 0.0% |
| CALL | 160 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL_ALLOC_AND_ENTER_INIT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,226,020 | 100.0% |
| RESUME | 240 | 0.0% |
| RETURN_GENERATOR | 80 | 0.0% |
| MAKE_CELL | 80 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 380 | 67.9% |
| FOR_ITER | 80 | 14.3% |
| JUMP_BACKWARD | 80 | 14.3% |
| SWAP | 20 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 21.4% |
| LOAD_FAST | 100 | 17.9% |
| FOR_ITER_LIST | 100 | 17.9% |
| FOR_ITER | 80 | 14.3% |
| STORE_FAST | 80 | 14.3% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 3,732,640 | 83.3% |
| RETURN_VALUE | 746,480 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,479,120 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 80.0% |
| IMPORT_FROM | 20 | 20.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,478,880 | 100.0% |
| LOAD_CONST | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,478,880 | 100.0% |
| RETURN_VALUE | 400 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,704,440 | 41.9% |
| CALL_LIST_APPEND | 8,957,720 | 38.7% |
| LIST_APPEND | 4,478,880 | 19.4% |
| POP_JUMP_IF_FALSE | 1,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 14,183,240 | 61.3% |
| FOR_ITER_TUPLE | 4,478,880 | 19.4% |
| FOR_ITER_LIST | 4,478,860 | 19.4% |
| LOAD_FAST | 1,540 | 0.0% |
| FOR_ITER | 80 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 746,580 | 100.0% |
| RESUME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 746,520 | 100.0% |
| SEND_GEN | 120 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,478,980 | 99.9% |
| STORE_FAST | 3,600 | 0.1% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 99.9% |
| LOAD_FAST | 2,080 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,560 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 4,478,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,478,880 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,704,380 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 9,704,400 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,583,940 | 79.0% |
| LOAD_ATTR_SLOT | 9,704,480 | 21.0% |
| LOAD_ATTR | 14,360 | 0.0% |
| LOAD_GLOBAL_MODULE | 800 | 0.0% |
| LOAD_GLOBAL | 780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,480 | 38.7% |
| PUSH_NULL | 9,705,160 | 21.0% |
| CALL | 8,959,560 | 19.3% |
| LOAD_FAST | 4,479,920 | 9.7% |
| TO_BOOL_NONE | 4,478,920 | 9.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 19,409,120 | 21.7% |
| POP_JUMP_IF_FALSE | 18,665,760 | 20.8% |
| LOAD_FAST | 10,452,980 | 11.7% |
| POP_TOP | 9,706,740 | 10.8% |
| LOAD_DEREF | 8,957,920 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,341,860 | 38.3% |
| STORE_FAST | 14,937,840 | 16.7% |
| CALL_KW | 10,450,960 | 11.7% |
| BINARY_OP_ADD_INT | 8,957,720 | 10.0% |
| COMPARE_OP_INT | 4,480,920 | 5.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 8,957,760 | 22.2% |
| POP_JUMP_IF_FALSE | 5,225,360 | 13.0% |
| RESUME_CHECK | 4,478,920 | 11.1% |
| JUMP_FORWARD | 4,478,880 | 11.1% |
| LOAD_DEREF | 4,478,880 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,957,920 | 22.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,225,280 | 13.0% |
| LOAD_DEREF | 4,478,880 | 11.1% |
| POP_JUMP_IF_NONE | 4,478,880 | 11.1% |
| COMPARE_OP_INT | 4,478,840 | 11.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 79,131,180 | 18.6% |
| STORE_FAST | 75,407,960 | 17.8% |
| RESUME_CHECK | 67,936,760 | 16.0% |
| LOAD_CONST | 34,341,860 | 8.1% |
| POP_TOP | 23,891,240 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 90,345,600 | 21.3% |
| LOAD_ATTR_SLOT | 72,409,840 | 17.0% |
| LOAD_ATTR | 36,583,940 | 8.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,583,680 | 8.6% |
| STORE_ATTR_SLOT | 29,113,800 | 6.9% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 746,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 746,480 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 20 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 29,113,380 | 29.1% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 14.2% |
| PUSH_NULL | 14,183,600 | 14.2% |
| POP_JUMP_IF_NOT_NONE | 13,436,800 | 13.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,704,380 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 38,817,760 | 38.8% |
| LOAD_FAST | 14,183,760 | 14.2% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 14.2% |
| CALL | 9,704,560 | 9.7% |
| LOAD_CONST | 8,957,920 | 9.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 480 | 12.2% |
| POP_TOP | 460 | 11.7% |
| RESUME_CHECK | 460 | 11.7% |
| LOAD_FAST | 380 | 9.6% |
| POP_JUMP_IF_NOT_NONE | 320 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,300 | 33.0% |
| LOAD_ATTR | 780 | 19.8% |
| LOAD_GLOBAL_BUILTIN | 600 | 15.2% |
| LOAD_FAST | 320 | 8.1% |
| CALL | 240 | 6.1% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 420 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 200 | 47.6% |
| CALL | 120 | 28.6% |
| LOAD_FAST | 80 | 19.0% |
| LOAD_FAST_LOAD_FAST | 20 | 4.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,985,920 | 80.0% |
| CALL_FUNCTION_EX | 746,480 | 20.0% |
| COPY_FREE_VARS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,985,920 | 80.0% |
| RESUME_CHECK | 746,520 | 20.0% |
| RESUME | 40 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 80,623,920 | 59.3% |
| TO_BOOL_NONE | 23,887,700 | 17.6% |
| COMPARE_OP_INT | 8,961,460 | 6.6% |
| CONTAINS_OP | 8,957,920 | 6.6% |
| TO_BOOL_LIST | 4,482,200 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,131,180 | 58.2% |
| RETURN_CONST | 22,395,260 | 16.5% |
| LOAD_CONST | 18,665,760 | 13.7% |
| LOAD_GLOBAL_MODULE | 5,225,480 | 3.8% |
| LOAD_DEREF | 5,225,360 | 3.8% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,958,320 | 66.7% |
| LOAD_DEREF | 4,478,880 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 8,957,760 | 66.7% |
| LOAD_FAST | 4,479,120 | 33.3% |
| RETURN_CONST | 480 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,889,760 | 84.2% |
| LOAD_ATTR_INSTANCE_VALUE | 4,478,960 | 15.8% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,436,800 | 47.4% |
| LOAD_GLOBAL_MODULE | 5,972,200 | 21.1% |
| LOAD_FAST | 4,480,740 | 15.8% |
| NOP | 3,732,560 | 13.2% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 2.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 8,958,400 | 92.3% |
| TO_BOOL | 748,300 | 7.7% |
| TO_BOOL_INT | 1,640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,704,660 | 100.0% |
| LOAD_CONST | 1,680 | 0.0% |
| STORE_FAST | 1,600 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 22,395,260 | 37.0% |
| POP_TOP | 14,184,520 | 23.5% |
| STORE_FAST | 9,706,000 | 16.1% |
| STORE_ATTR_SLOT | 9,704,660 | 16.0% |
| RESUME_CHECK | 3,732,460 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 28,367,340 | 46.9% |
| POP_TOP | 23,893,800 | 39.5% |
| TO_BOOL_BOOL | 4,478,920 | 7.4% |
| END_SEND | 3,732,640 | 6.2% |
| EXIT_INIT_CHECK | 120 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,560 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 746,520 | 50.0% |
| SEND | 560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 746,480 | 50.0% |
| YIELD_VALUE | 746,480 | 50.0% |
| SEND | 560 | 0.0% |
| POP_TOP | 60 | 0.0% |
| SEND_GEN | 60 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 746,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,720 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,020 | 85.7% |
| LOAD_FAST_LOAD_FAST | 746,780 | 14.3% |
| STORE_ATTR | 1,760 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 85.6% |
| LOAD_CONST | 746,840 | 14.3% |
| STORE_ATTR | 1,760 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 980 | 0.0% |
| LOAD_FAST | 500 | 0.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 8,957,720 | 70.6% |
| LOAD_CONST | 2,239,440 | 17.6% |
| BUILD_LIST | 746,480 | 5.9% |
| CALL_KW | 746,480 | 5.9% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 35.3% |
| LOAD_FAST_LOAD_FAST | 4,478,880 | 35.3% |
| LOAD_CONST | 1,492,960 | 11.8% |
| LOAD_FAST | 1,492,960 | 11.8% |
| BUILD_LIST | 746,480 | 5.9% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 23,888,300 | 23.9% |
| LOAD_CONST | 14,937,840 | 14.9% |
| RETURN_VALUE | 14,932,140 | 14.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,183,240 | 14.2% |
| FOR_ITER_RANGE | 14,183,240 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 75,407,960 | 75.4% |
| RETURN_CONST | 9,706,000 | 9.7% |
| LOAD_FAST_LOAD_FAST | 5,225,680 | 5.2% |
| LOAD_GLOBAL_MODULE | 4,479,080 | 4.5% |
| LOAD_CONST | 1,493,040 | 1.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 20 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 120 | 75.0% |
| UNPACK_SEQUENCE | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 746,480 | 33.3% |
| LOAD_FAST_AND_CLEAR | 746,480 | 33.3% |
| FOR_ITER_RANGE | 746,480 | 33.3% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,560 | 33.3% |
| BUILD_LIST | 746,480 | 33.3% |
| FOR_ITER_RANGE | 746,460 | 33.3% |
| POP_EXCEPT | 100 | 0.0% |
| STORE_ATTR | 80 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 33.3% |
| CALL | 40 | 33.3% |
| STORE_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 50.0% |
| STORE_FAST_STORE_FAST | 40 | 33.3% |
| LOAD_FAST | 20 | 16.7% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 746,480 | 100.0% |
| YIELD_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 746,480 | 100.0% |
| YIELD_VALUE | 160 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,020 | 62.2% |
| COPY_FREE_VARS | 240 | 14.6% |
| CACHE | 220 | 13.4% |
| POP_TOP | 80 | 4.9% |
| MAKE_CELL | 40 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 780 | 47.6% |
| LOAD_GLOBAL | 480 | 29.3% |
| NOP | 100 | 6.1% |
| LOAD_CONST | 100 | 6.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 60 | 3.7% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,560 | 98.7% |
| BINARY_OP | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,580 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,957,720 | 100.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 8,957,720 | 100.0% |
| SWAP | 60 | 0.0% |


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
| STORE_FAST | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,478,880 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,478,840 | 100.0% |
| SWAP | 60 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 57.1% |
| LOAD_FAST | 40 | 28.6% |
| BINARY_SUBSCR | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 57.1% |
| RETURN_VALUE | 60 | 42.9% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20 | 100.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 40 | 33.3% |
| CALL | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 60 | 50.0% |
| RESUME_CHECK | 60 | 50.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 60 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 746,440 | 99.7% |
| LOAD_FAST | 1,740 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 748,100 | 99.9% |
| LOAD_FAST | 240 | 0.0% |
| COMPARE_OP | 140 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,479,060 | 100.0% |
| CALL | 40 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,479,020 | 100.0% |
| TO_BOOL_BOOL | 80 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 33.3% |
| LOAD_CONST | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 120 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 380 | 73.1% |
| CALL | 60 | 11.5% |
| BUILD_TUPLE | 40 | 7.7% |
| LOAD_GLOBAL_MODULE | 40 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 460 | 88.5% |
| TO_BOOL | 60 | 11.5% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,680 | 98.7% |
| CALL | 60 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,160 | 66.7% |
| COPY | 1,580 | 33.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,957,680 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,957,720 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 120 | 60.0% |
| RETURN_VALUE | 40 | 20.0% |
| CALL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 70.0% |
| STORE_FAST | 60 | 30.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,560 | 87.6% |
| LOAD_CONST | 80 | 4.5% |
| CALL | 60 | 3.4% |
| LOAD_ATTR | 40 | 2.2% |
| LOAD_FAST | 40 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,580 | 88.8% |
| POP_TOP | 120 | 6.7% |
| RETURN_VALUE | 80 | 4.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 17,915,480 | 55.7% |
| LOAD_ATTR_METHOD_NO_DICT | 9,704,800 | 30.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 13.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.3% |
| CALL | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 17,915,440 | 55.7% |
| STORE_FAST | 14,183,240 | 44.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.3% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,183,280 | 76.0% |
| CALL | 4,479,040 | 24.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 18,662,400 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 27,624,320 | 45.1% |
| LOAD_FAST | 19,412,840 | 31.7% |
| LOAD_ATTR_METHOD_NO_DICT | 9,704,480 | 15.9% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 7.3% |
| CALL | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 53,010,760 | 86.6% |
| RETURN_GENERATOR | 8,211,380 | 13.4% |
| COPY_FREE_VARS | 640 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 120 | 31.6% |
| CALL | 100 | 26.3% |
| LOAD_FAST | 80 | 21.1% |
| PUSH_NULL | 40 | 10.5% |
| LOAD_CONST | 40 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 380 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,478,920 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,478,920 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,480,920 | 50.0% |
| LOAD_DEREF | 4,478,840 | 50.0% |
| LOAD_GLOBAL_MODULE | 1,560 | 0.0% |
| COMPARE_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,961,460 | 100.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,478,860 | 75.0% |
| GET_ITER | 1,496,060 | 25.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,860 | 75.0% |
| LOAD_DEREF | 1,492,940 | 25.0% |
| RETURN_CONST | 1,640 | 0.0% |
| LOAD_FAST | 1,580 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 14,183,240 | 95.0% |
| SWAP | 746,460 | 5.0% |
| GET_ITER | 1,580 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,183,240 | 95.0% |
| SWAP | 746,480 | 5.0% |
| LOAD_CONST | 1,600 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,478,880 | 85.7% |
| GET_ITER | 746,480 | 14.3% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,880 | 85.7% |
| LOAD_GLOBAL_MODULE | 746,440 | 14.3% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| LOAD_ATTR | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 90,345,600 | 94.5% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 4.7% |
| LOAD_DEREF | 746,440 | 0.8% |
| LOAD_ATTR | 1,340 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 34,340,440 | 35.9% |
| LOAD_ATTR_METHOD_NO_DICT | 28,368,820 | 29.7% |
| RETURN_VALUE | 14,930,340 | 15.6% |
| TO_BOOL_LIST | 4,482,140 | 4.7% |
| TO_BOOL | 4,480,780 | 4.7% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 28,368,820 | 60.3% |
| LOAD_FAST | 14,183,560 | 30.2% |
| LOAD_DEREF | 4,478,840 | 9.5% |
| LOAD_ATTR | 540 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,141,220 | 49.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,800 | 20.6% |
| CALL_PY_EXACT_ARGS | 9,704,480 | 20.6% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 9.5% |
| LOAD_FAST_LOAD_FAST | 1,720 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,583,680 | 71.0% |
| LOAD_ATTR_SLOT | 9,704,480 | 18.8% |
| LOAD_DEREF | 5,225,280 | 10.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,880 | 0.0% |
| LOAD_ATTR | 1,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 27,624,320 | 53.6% |
| LOAD_FAST | 9,708,300 | 18.8% |
| LOAD_FAST_LOAD_FAST | 9,704,380 | 18.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,478,840 | 8.7% |
| CALL | 620 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 25,383,320 | 100.0% |
| LOAD_ATTR | 800 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 25,383,560 | 100.0% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_ATTR_SLOT | 80 | 0.0% |
| UNARY_INVERT | 60 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| LOAD_ATTR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,409,840 | 100.0% |
| LOAD_ATTR | 280 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 19,408,720 | 26.8% |
| LOAD_ATTR | 9,704,480 | 13.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 13.4% |
| TO_BOOL_BOOL | 9,704,400 | 13.4% |
| BUILD_LIST | 9,704,380 | 13.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,960,400 | 85.7% |
| PUSH_NULL | 746,440 | 7.1% |
| POP_JUMP_IF_NOT_NONE | 746,440 | 7.1% |
| STORE_FAST | 1,620 | 0.0% |
| POP_JUMP_IF_FALSE | 1,580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,965,380 | 85.7% |
| LOAD_DEREF | 747,080 | 7.1% |
| LOAD_GLOBAL_MODULE | 746,480 | 7.1% |
| CALL_ISINSTANCE | 380 | 0.0% |
| CALL_BUILTIN_CLASS | 220 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 14,185,420 | 35.2% |
| POP_JUMP_IF_NOT_NONE | 5,972,200 | 14.8% |
| POP_JUMP_IF_FALSE | 5,225,480 | 13.0% |
| STORE_FAST | 4,479,080 | 11.1% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 25,383,320 | 63.0% |
| LOAD_FAST_LOAD_FAST | 8,958,060 | 22.2% |
| CONTAINS_OP | 4,478,940 | 11.1% |
| LOAD_DEREF | 746,460 | 1.9% |
| CALL_BUILTIN_CLASS | 746,440 | 1.9% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,880 | 100.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,720 | 100.0% |
| CALL_PY_EXACT_ARGS | 200 | 0.0% |
| CALL | 100 | 0.0% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 53,010,760 | 48.0% |
| CACHE | 34,339,220 | 31.1% |
| POP_TOP | 8,211,520 | 7.4% |
| COPY_FREE_VARS | 5,226,020 | 4.7% |
| CALL | 4,479,500 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,936,760 | 61.5% |
| LOAD_GLOBAL_MODULE | 14,185,420 | 12.8% |
| NOP | 10,451,500 | 9.5% |
| LOAD_GLOBAL_BUILTIN | 8,960,400 | 8.1% |
| LOAD_DEREF | 4,478,920 | 4.1% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,732,560 | 100.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 120 | 0.0% |
| SEND | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,732,580 | 100.0% |
| RESUME_CHECK | 140 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 748,420 | 99.8% |
| STORE_ATTR | 980 | 0.1% |
| LOAD_FAST_LOAD_FAST | 260 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 747,120 | 99.7% |
| LOAD_CONST | 840 | 0.1% |
| LOAD_FAST | 760 | 0.1% |
| LOAD_GLOBAL_MODULE | 360 | 0.0% |
| BUILD_LIST | 220 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 38,817,760 | 57.1% |
| LOAD_FAST | 29,113,800 | 42.9% |
| STORE_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 29,113,380 | 42.9% |
| LOAD_CONST | 19,409,120 | 28.6% |
| LOAD_FAST | 9,704,660 | 14.3% |
| RETURN_CONST | 9,704,660 | 14.3% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,478,840 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,478,920 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 34,340,440 | 38.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,440 | 20.0% |
| RETURN_VALUE | 14,183,840 | 15.8% |
| LOAD_ATTR_SLOT | 9,704,400 | 10.8% |
| COPY | 4,479,080 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80,623,920 | 90.0% |
| POP_JUMP_IF_TRUE | 8,958,400 | 10.0% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,640 | 83.7% |
| TO_BOOL | 160 | 8.2% |
| LOAD_FAST | 80 | 4.1% |
| BINARY_OP | 40 | 2.0% |
| LOAD_ATTR_SLOT | 40 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,640 | 83.7% |
| POP_JUMP_IF_FALSE | 260 | 13.3% |
| UNARY_NOT | 60 | 3.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,482,140 | 100.0% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,482,200 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 19,408,720 | 81.2% |
| LOAD_ATTR | 4,478,920 | 18.7% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 23,887,700 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE | 60 | 33.3% |
| RETURN_VALUE | 40 | 22.2% |
| CALL | 40 | 22.2% |
| STORE_FAST | 40 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 120 | 66.7% |
| LOAD_FAST | 60 | 33.3% |


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
|     deferred | 620 | 0.0% |
|          hit | 13,438,340 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 53.8% |
| Failure | 120 | 46.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 80 | 66.7% |
| or | 40 | 33.3% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 7.1% |
|          hit | 240 | 85.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 38,738,140 | 22.8% |
|          hit | 126,178,120 | 74.4% |
|         miss | 4,565,360 | 2.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 88,740 | 88.0% |
| Failure | 12,080 | 12.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 4,280 | 35.4% |
| no dict | 2,580 | 21.4% |
| class no vectorcall | 1,340 | 11.1% |
| code complex parameters | 1,320 | 10.9% |
| other | 1,280 | 10.6% |
| cfunc noargs | 660 | 5.5% |
| cmethod | 380 | 3.1% |
| class mutable | 80 | 0.7% |
| wrong number arguments | 40 | 0.3% |
| cfunc varargs | 40 | 0.3% |
| operator wrapper | 40 | 0.3% |
| cfunc varargs keywords | 20 | 0.2% |
| init not simple | 20 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 360 | 0.0% |
|          hit | 8,961,480 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 77.8% |
| Failure | 40 | 22.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bool | 40 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 320 | 0.0% |
|          hit | 26,131,720 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 66.7% |
| Failure | 80 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 80 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 46,288,100 | 13.7% |
|          hit | 291,915,940 | 86.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,080 | 23.0% |
| Failure | 13,660 | 77.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 9,080 | 66.5% |
| method | 3,060 | 22.4% |
| class attr descriptor | 1,280 | 9.4% |
| not managed dict | 140 | 1.0% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,120 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 50,777,300 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,900 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 220 | 0.0% |
|          hit | 747,080 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
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
|     deferred | 1,493,020 | 28.6% |
|          hit | 3,732,740 | 71.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 9.7% |
| Failure | 560 | 90.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 560 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,226,960 | 7.1% |
|          hit | 68,681,560 | 92.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,240 | 41.3% |
| Failure | 1,760 | 58.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overriding descriptor | 1,300 | 73.9% |
| no dict | 380 | 21.6% |
| overridden | 80 | 4.5% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 4,478,920 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,228,140 | 4.2% |
|          hit | 117,954,240 | 95.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,080 | 38.0% |
| Failure | 1,760 | 62.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 1,280 | 72.7% |
| tuple | 380 | 21.6% |
| sequence | 100 | 5.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 20.0% |
|          hit | 180 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,187,077,360 | 51.6% |
| Not specialized | 284,493,760 | 12.4% |
| Specialized hits | 823,447,420 | 35.8% |
| Specialized misses | 4,608,960 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 46,288,100 | 47.7% |
| CALL | 38,738,140 | 39.9% |
| TO_BOOL | 5,228,140 | 5.4% |
| STORE_ATTR | 5,226,960 | 5.4% |
| SEND | 1,493,020 | 1.5% |
| LOAD_GLOBAL | 2,120 | 0.0% |
| BINARY_OP | 620 | 0.0% |
| COMPARE_OP | 360 | 0.0% |
| FOR_ITER | 320 | 0.0% |
| LOAD_SUPER_ATTR | 220 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 98.1% |
| RESUME | 43,520 | 0.9% |
| RESUME_CHECK | 43,520 | 0.9% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| END_SEND | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 44,043,880 | 37.1% |
| Calls to Python functions inlined | 74,662,500 | 62.9% |
| Calls via PyEval_EvalFrame (total) | 44,043,880 | 37.1% |
| Calls via PyEval_EvalFrame (vector) | 38,818,440 | 32.7% |
| Calls via PyEval_EvalFrame (generator) | 5,225,440 | 4.4% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 38,818,440 | 32.7% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 746,560 | 0.6% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.8% |
| Calls via PyEval_EvalFrame (method) | 19,408,800 | 16.4% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 61,223,540 | 51.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 58,343,480 | 37.2% |
| Frees to freelist | 58,597,160 |  |
| Allocations | 98,662,280 | 62.8% |
| Allocations to 512 bytes | 98,603,740 | 62.8% |
| Allocations to 4 kbytes | 58,440 | 0.0% |
| Allocations over 4 kbytes | 100 | 0.0% |
| Frees | 100,802,840 |  |
| New values | 300 |  |
| Interpreter increfs | 1,152,700,040 | 78.7% |
| Interpreter decrefs | 1,203,258,740 | 75.1% |
| Increfs | 312,794,601 | 21.3% |
| Decrefs | 399,470,850 | 24.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 82,884,063 |  |
| Method cache misses | 750,137 |  |
| Method cache collisions | 745,861 |  |
| Method cache dunder hits | 10,452,249 |  |
| Method cache dunder misses | 431 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 49,240 | 0 | 257,698,600 |
| 1 | 4,480 | 60 | 278,814,520 |
| 2 | 380 | 0 | 754,314,360 |


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
