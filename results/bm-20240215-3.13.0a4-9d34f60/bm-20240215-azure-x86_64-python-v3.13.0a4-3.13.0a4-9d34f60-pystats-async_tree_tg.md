
# Pystats results

- benchmark: async_tree_tg
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 422,574,080 | 20.7% | 20.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 141,854,020 | 6.9% | 27.6% |  |
| POP_JUMP_IF_FALSE | 112,731,800 | 5.5% | 33.1% |  |
| RESUME_CHECK | 103,028,260 | 5.0% | 38.2% | 0.0% |
| POP_TOP | 85,855,060 | 4.2% | 42.4% |  |
| LOAD_FAST_LOAD_FAST | 85,850,760 | 4.2% | 46.6% |  |
| TO_BOOL_BOOL | 77,638,660 | 3.8% | 50.4% |  |
| LOAD_CONST | 75,411,540 | 3.7% | 54.1% |  |
| STORE_FAST | 72,433,520 | 3.5% | 57.6% |  |
| STORE_ATTR_SLOT | 67,931,820 | 3.3% | 60.9% |  |
| LOAD_ATTR_SLOT | 67,931,320 | 3.3% | 64.3% |  |
| RETURN_CONST | 56,740,460 | 2.8% | 67.0% |  |
| CALL_PY_EXACT_ARGS | 52,265,020 | 2.6% | 69.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 51,516,740 | 2.5% | 72.1% |  |
| LOAD_ATTR_METHOD_NO_DICT | 47,031,840 | 2.3% | 74.4% |  |
| RETURN_VALUE | 45,542,780 | 2.2% | 76.6% |  |
| INTERPRETER_EXIT | 44,790,500 | 2.2% | 78.8% |  |
| LOAD_ATTR | 38,093,360 | 1.9% | 80.7% |  |
| CALL | 33,612,180 | 1.6% | 82.4% |  |
| PUSH_NULL | 31,356,900 | 1.5% | 83.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 27,620,140 | 1.4% | 85.2% | 0.0% |
| POP_JUMP_IF_NOT_NONE | 25,383,160 | 1.2% | 86.5% |  |
| TO_BOOL_NONE | 23,887,700 | 1.2% | 87.6% |  |
| LOAD_GLOBAL_MODULE | 22,401,960 | 1.1% | 88.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 19,409,520 | 0.9% | 89.7% | 0.0% |
| LOAD_ATTR_MODULE | 17,172,940 | 0.8% | 90.5% |  |
| FOR_ITER_RANGE | 14,931,320 | 0.7% | 91.3% |  |
| JUMP_BACKWARD | 14,184,840 | 0.7% | 92.0% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.7% | 92.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 11,946,640 | 0.6% | 93.2% |  |
| TO_BOOL | 11,204,980 | 0.5% | 93.7% |  |
| NOP | 10,454,000 | 0.5% | 94.3% |  |
| BUILD_LIST | 10,452,720 | 0.5% | 94.8% |  |
| POP_JUMP_IF_TRUE | 9,708,340 | 0.5% | 95.2% |  |
| CALL_FUNCTION_EX | 9,704,640 | 0.5% | 95.7% |  |
| RETURN_GENERATOR | 9,704,560 | 0.5% | 96.2% |  |
| CALL_KW | 9,704,480 | 0.5% | 96.7% |  |
| CALL_INTRINSIC_1 | 9,704,400 | 0.5% | 97.1% |  |
| LIST_EXTEND | 9,704,400 | 0.5% | 97.6% |  |
| SEND_GEN | 5,972,140 | 0.3% | 97.9% |  |
| END_SEND | 5,972,080 | 0.3% | 98.2% |  |
| GET_AWAITABLE | 5,972,080 | 0.3% | 98.5% |  |
| TO_BOOL_LIST | 5,228,660 | 0.3% | 98.8% |  |
| JUMP_FORWARD | 4,482,660 | 0.2% | 99.0% |  |
| COMPARE_OP_INT | 4,482,600 | 0.2% | 99.2% |  |
| BINARY_OP_SUBTRACT_INT | 4,478,920 | 0.2% | 99.4% |  |
| LOAD_GLOBAL_BUILTIN | 1,502,160 | 0.1% | 99.5% | 0.0% |
| CALL_BUILTIN_CLASS | 1,495,220 | 0.1% | 99.6% |  |
| SEND | 1,493,720 | 0.1% | 99.6% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,493,120 | 0.1% | 99.7% |  |
| YIELD_VALUE | 1,493,120 | 0.1% | 99.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 760,860 | 0.0% | 99.8% | 100.0% |
| GET_ITER | 751,540 | 0.0% | 99.9% |  |
| BEFORE_ASYNC_WITH | 746,480 | 0.0% | 99.9% |  |
| EXIT_INIT_CHECK | 746,460 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 746,460 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 746,460 | 0.0% | 100.0% |  |
| CALL_LEN | 4,740 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,900 | 0.0% | 100.0% |  |
| STORE_ATTR | 3,540 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 3,220 | 0.0% | 100.0% |  |
| COPY | 2,340 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 1,960 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,780 | 0.0% | 100.0% |  |
| RESUME | 1,720 | 0.0% | 100.0% | 1,533.7% |
| BINARY_OP_ADD_FLOAT | 1,580 | 0.0% | 100.0% |  |
| LOAD_DEREF | 1,220 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 1,060 | 0.0% | 100.0% |  |
| BINARY_OP | 800 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 640 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 620 | 0.0% | 100.0% |  |
| CALL_ISINSTANCE | 520 | 0.0% | 100.0% |  |
| COMPARE_OP | 500 | 0.0% | 100.0% |  |
| FOR_ITER | 440 | 0.0% | 100.0% |  |
| BUILD_MAP | 400 | 0.0% | 100.0% |  |
| IS_OP | 400 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 380 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 380 | 0.0% | 100.0% |  |
| SWAP | 340 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 240 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 240 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 240 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 200 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| CONTAINS_OP | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 120 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| MAKE_CELL | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 60 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_INT | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 60 | 0.0% | 100.0% |  |
| BEFORE_WITH | 40 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 40 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 40 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 137,372,920 | 6.7% | 6.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 87,342,460 | 4.3% | 11.0% |
| RESUME_CHECK LOAD_FAST | 76,148,020 | 3.7% | 14.7% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 72,412,620 | 3.5% | 18.3% |
| LOAD_FAST LOAD_ATTR_SLOT | 67,930,960 | 3.3% | 21.6% |
| STORE_FAST LOAD_FAST | 57,492,440 | 2.8% | 24.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 48,523,400 | 2.4% | 26.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 44,053,000 | 2.2% | 28.9% |
| CACHE RESUME_CHECK | 38,818,140 | 1.9% | 30.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 38,817,760 | 1.9% | 32.7% |
| POP_TOP LOAD_FAST | 38,074,360 | 1.9% | 34.6% |
| LOAD_CONST LOAD_FAST | 37,327,780 | 1.8% | 36.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 37,326,500 | 1.8% | 38.2% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 36,583,640 | 1.8% | 40.0% |
| LOAD_FAST RETURN_VALUE | 29,115,620 | 1.4% | 41.5% |
| LOAD_FAST STORE_ATTR_SLOT | 29,113,800 | 1.4% | 42.9% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 29,113,380 | 1.4% | 44.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 28,370,760 | 1.4% | 45.7% |
| RETURN_CONST INTERPRETER_EXIT | 27,621,000 | 1.4% | 47.1% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 27,620,120 | 1.4% | 48.4% |
| LOAD_FAST LOAD_ATTR | 26,880,620 | 1.3% | 49.7% |
| RETURN_CONST POP_TOP | 23,893,800 | 1.2% | 50.9% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 23,887,700 | 1.2% | 52.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 23,141,220 | 1.1% | 53.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 23,140,960 | 1.1% | 54.3% |
| STORE_ATTR_SLOT LOAD_CONST | 19,409,120 | 0.9% | 55.3% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 19,408,720 | 0.9% | 56.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 18,664,400 | 0.9% | 57.1% |
| CALL STORE_FAST | 18,662,980 | 0.9% | 58.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 17,172,260 | 0.8% | 58.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 17,172,000 | 0.8% | 59.7% |
| POP_JUMP_IF_FALSE RETURN_CONST | 14,930,460 | 0.7% | 60.5% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 14,930,340 | 0.7% | 61.2% |
| RETURN_VALUE INTERPRETER_EXIT | 14,930,060 | 0.7% | 61.9% |
| RETURN_VALUE STORE_FAST | 14,185,600 | 0.7% | 62.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,183,760 | 0.7% | 63.3% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,183,600 | 0.7% | 64.0% |
| POP_TOP JUMP_BACKWARD | 14,183,280 | 0.7% | 64.7% |
| JUMP_BACKWARD FOR_ITER_RANGE | 14,183,240 | 0.7% | 65.4% |
| FOR_ITER_RANGE STORE_FAST | 14,183,240 | 0.7% | 66.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 14,183,240 | 0.7% | 66.8% |
| POP_TOP RETURN_CONST | 13,438,040 | 0.7% | 67.4% |
| POP_JUMP_IF_NONE LOAD_FAST | 12,690,400 | 0.6% | 68.1% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 11,945,020 | 0.6% | 68.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 11,199,120 | 0.5% | 69.2% |
| PUSH_NULL LOAD_FAST | 11,198,080 | 0.5% | 69.7% |
| LOAD_CONST STORE_FAST | 10,458,960 | 0.5% | 70.3% |
| NOP LOAD_FAST | 10,453,440 | 0.5% | 70.8% |
| POP_TOP LOAD_CONST | 10,453,220 | 0.5% | 71.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 10,452,980 | 0.5% | 71.8% |
| BUILD_LIST LOAD_FAST | 10,451,120 | 0.5% | 72.3% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 9,708,640 | 0.5% | 72.8% |
| POP_JUMP_IF_FALSE LOAD_CONST | 9,708,000 | 0.5% | 73.2% |
| LOAD_FAST LOAD_CONST | 9,706,500 | 0.5% | 73.7% |
| STORE_FAST RETURN_CONST | 9,706,000 | 0.5% | 74.2% |
| LOAD_ATTR PUSH_NULL | 9,705,180 | 0.5% | 74.7% |
| RESUME_CHECK NOP | 9,705,020 | 0.5% | 75.1% |
| RETURN_VALUE TO_BOOL_BOOL | 9,704,960 | 0.5% | 75.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 9,704,880 | 0.5% | 76.1% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,800 | 0.5% | 76.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 9,704,720 | 0.5% | 77.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,704,660 | 0.5% | 77.5% |
| STORE_ATTR_SLOT LOAD_FAST | 9,704,660 | 0.5% | 78.0% |
| STORE_ATTR_SLOT RETURN_CONST | 9,704,660 | 0.5% | 78.5% |
| CALL_FUNCTION_EX POP_TOP | 9,704,560 | 0.5% | 78.9% |
| LOAD_FAST_LOAD_FAST CALL | 9,704,560 | 0.5% | 79.4% |
| LOAD_CONST CALL_KW | 9,704,480 | 0.5% | 79.9% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 9,704,480 | 0.5% | 80.4% |
| LOAD_ATTR_SLOT LOAD_ATTR | 9,704,480 | 0.5% | 80.8% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 0.5% | 81.3% |
| POP_TOP RESUME_CHECK | 9,704,440 | 0.5% | 81.8% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 9,704,400 | 0.5% | 82.3% |
| LIST_EXTEND CALL_INTRINSIC_1 | 9,704,400 | 0.5% | 82.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 9,704,400 | 0.5% | 83.2% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 9,704,400 | 0.5% | 83.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 9,704,380 | 0.5% | 84.2% |
| LOAD_ATTR_SLOT BUILD_LIST | 9,704,380 | 0.5% | 84.6% |
| LOAD_ATTR_SLOT LIST_EXTEND | 9,704,380 | 0.5% | 85.1% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,240 | 0.5% | 85.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 9,704,200 | 0.5% | 86.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 8,961,820 | 0.4% | 86.5% |
| LOAD_ATTR CALL | 8,959,540 | 0.4% | 86.9% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,957,920 | 0.4% | 87.4% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,211,840 | 0.4% | 87.8% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,211,380 | 0.4% | 88.2% |
| TO_BOOL POP_JUMP_IF_FALSE | 6,719,280 | 0.3% | 88.5% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 6,718,340 | 0.3% | 88.8% |
| GET_AWAITABLE LOAD_CONST | 5,972,080 | 0.3% | 89.1% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 5,228,660 | 0.3% | 89.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 5,228,580 | 0.3% | 89.7% |
| PUSH_NULL CALL | 5,228,380 | 0.3% | 89.9% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 5,227,220 | 0.3% | 90.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 5,227,160 | 0.3% | 90.4% |
| CALL POP_TOP | 5,226,120 | 0.3% | 90.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 5,226,060 | 0.3% | 90.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 5,225,980 | 0.3% | 91.2% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 5,225,760 | 0.3% | 91.4% |
| END_SEND POP_TOP | 5,225,600 | 0.3% | 91.7% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 5,225,580 | 0.3% | 92.0% |
| SEND_GEN POP_TOP | 5,225,500 | 0.3% | 92.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 38,818,140 | 86.7% |
| POP_TOP | 4,478,960 | 10.0% |
| RETURN_GENERATOR | 1,492,960 | 3.3% |
| RESUME | 260 | 0.0% |
| COPY_FREE_VARS | 180 | 0.0% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 746,460 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 746,480 | 100.0% |


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
| RETURN_CONST | 4,479,120 | 75.0% |
| RETURN_VALUE | 746,480 | 12.5% |
| SEND | 746,480 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,225,600 | 87.5% |
| STORE_FAST | 746,480 | 12.5% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 746,460 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 746,460 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 748,100 | 99.5% |
| LOAD_FAST | 3,220 | 0.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 160 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 748,040 | 99.5% |
| FOR_ITER_LIST | 3,160 | 0.4% |
| FOR_ITER | 320 | 0.0% |
| FOR_ITER_TUPLE | 20 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 27,621,000 | 61.7% |
| RETURN_VALUE | 14,930,060 | 33.3% |
| RETURN_GENERATOR | 1,492,960 | 3.3% |
| YIELD_VALUE | 746,480 | 1.7% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 240 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,705,020 | 92.8% |
| STORE_ATTR_INSTANCE_VALUE | 746,460 | 7.1% |
| STORE_FAST | 1,760 | 0.0% |
| POP_TOP | 400 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,453,440 | 100.0% |
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
| CALL_METHOD_DESCRIPTOR_O | 27,620,120 | 32.2% |
| RETURN_CONST | 23,893,800 | 27.8% |
| CALL_FUNCTION_EX | 9,704,560 | 11.3% |
| CALL | 5,226,120 | 6.1% |
| END_SEND | 5,225,600 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,074,360 | 44.3% |
| JUMP_BACKWARD | 14,183,280 | 16.5% |
| RETURN_CONST | 13,438,040 | 15.7% |
| LOAD_CONST | 10,453,220 | 12.2% |
| RESUME_CHECK | 9,704,440 | 11.3% |


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
| LOAD_ATTR_MODULE | 17,172,260 | 54.8% |
| LOAD_ATTR | 9,705,180 | 31.0% |
| LOAD_FAST | 4,479,380 | 14.3% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,183,600 | 45.2% |
| LOAD_FAST | 11,198,080 | 35.7% |
| CALL | 5,228,380 | 16.7% |
| CALL_ALLOC_AND_ENTER_INIT | 746,440 | 2.4% |
| LOAD_CONST | 240 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 8,211,380 | 84.6% |
| CACHE | 1,492,960 | 15.4% |
| CALL | 80 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 4,478,920 | 46.2% |
| GET_AWAITABLE | 3,732,640 | 38.5% |
| INTERPRETER_EXIT | 1,492,960 | 15.4% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,115,620 | 63.9% |
| LOAD_ATTR_INSTANCE_VALUE | 14,930,340 | 32.8% |
| CALL_KW | 746,480 | 1.6% |
| EXIT_INIT_CHECK | 746,460 | 1.6% |
| CALL | 1,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 14,930,060 | 32.8% |
| STORE_FAST | 14,185,600 | 31.1% |
| TO_BOOL_BOOL | 9,704,960 | 21.3% |
| POP_TOP | 4,479,120 | 9.8% |
| LOAD_FAST | 748,080 | 1.6% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 40 | 66.7% |
| LOAD_FAST | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 33.3% |
| LOAD_FAST | 20 | 33.3% |
| STORE_SUBSCR_DICT | 20 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 11,199,120 | 99.9% |
| TO_BOOL | 3,800 | 0.0% |
| LOAD_ATTR | 600 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |
| COPY | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,719,280 | 60.0% |
| POP_JUMP_IF_TRUE | 4,480,720 | 40.0% |
| TO_BOOL | 3,800 | 0.0% |
| TO_BOOL_BOOL | 840 | 0.0% |
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
| LOAD_GLOBAL_MODULE | 180 | 22.5% |
| UNARY_INVERT | 160 | 20.0% |
| BINARY_OP | 120 | 15.0% |
| LOAD_CONST | 120 | 15.0% |
| POP_JUMP_IF_FALSE | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 25.0% |
| COPY | 160 | 20.0% |
| BINARY_OP | 120 | 15.0% |
| UNARY_INVERT | 80 | 10.0% |
| TO_BOOL | 40 | 5.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,704,380 | 92.8% |
| STORE_ATTR_INSTANCE_VALUE | 746,680 | 7.1% |
| STORE_FAST | 1,600 | 0.0% |
| STORE_ATTR | 40 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,451,120 | 100.0% |
| STORE_FAST | 1,600 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 140 | 35.0% |
| POP_TOP | 80 | 20.0% |
| BUILD_TUPLE | 80 | 20.0% |
| RESUME_CHECK | 60 | 15.0% |
| STORE_ATTR | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 37.5% |
| CALL | 80 | 12.5% |
| LOAD_CONST | 80 | 12.5% |
| LOAD_FAST_LOAD_FAST | 80 | 12.5% |
| LOAD_GLOBAL_MODULE | 80 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 37.5% |
| CALL | 160 | 25.0% |
| RETURN_VALUE | 80 | 12.5% |
| BUILD_MAP | 80 | 12.5% |
| CALL_ISINSTANCE | 40 | 6.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,704,560 | 28.9% |
| LOAD_ATTR | 8,959,540 | 26.7% |
| PUSH_NULL | 5,228,380 | 15.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,100 | 13.3% |
| RETURN_GENERATOR | 4,478,920 | 13.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,662,980 | 55.5% |
| POP_TOP | 5,226,120 | 15.5% |
| RESUME_CHECK | 4,479,460 | 13.3% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,080 | 13.3% |
| LOAD_FAST | 747,200 | 2.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 9,704,400 | 100.0% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,704,560 | 100.0% |
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
| LOAD_CONST | 9,704,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 46.2% |
| RESUME_CHECK | 4,478,940 | 46.2% |
| RETURN_VALUE | 746,480 | 7.7% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220 | 44.0% |
| CALL_BUILTIN_CLASS | 140 | 28.0% |
| COMPARE_OP | 40 | 8.0% |
| RETURN_VALUE | 20 | 4.0% |
| CALL | 20 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 320 | 64.0% |
| COMPARE_OP_INT | 120 | 24.0% |
| COMPARE_OP | 40 | 8.0% |
| COPY | 20 | 4.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 60 | 37.5% |
| LOAD_GLOBAL_MODULE | 60 | 37.5% |
| LOAD_ATTR | 20 | 12.5% |
| LOAD_GLOBAL | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 160 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,580 | 67.5% |
| BINARY_OP | 160 | 6.8% |
| LOAD_FAST | 160 | 6.8% |
| CALL_BUILTIN_FAST | 140 | 6.0% |
| UNARY_NOT | 80 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 1,640 | 70.1% |
| TO_BOOL | 240 | 10.3% |
| TO_BOOL_BOOL | 200 | 8.5% |
| POP_EXCEPT | 80 | 3.4% |
| LOAD_ATTR | 80 | 3.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 640 | 60.4% |
| CACHE | 180 | 17.0% |
| CALL | 160 | 15.1% |
| CALL_FUNCTION_EX | 80 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 700 | 66.0% |
| RESUME | 200 | 18.9% |
| RETURN_GENERATOR | 80 | 7.5% |
| MAKE_CELL | 80 | 7.5% |


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
| GET_ITER | 320 | 72.7% |
| FOR_ITER | 80 | 18.2% |
| JUMP_BACKWARD | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 27.3% |
| LOAD_FAST | 100 | 22.7% |
| FOR_ITER | 80 | 18.2% |
| FOR_ITER_LIST | 60 | 13.6% |
| STORE_FAST | 40 | 9.1% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 3,732,640 | 62.5% |
| BEFORE_ASYNC_WITH | 746,480 | 12.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 746,460 | 12.5% |
| LOAD_ATTR_INSTANCE_VALUE | 746,460 | 12.5% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,972,080 | 100.0% |


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
| LOAD_CONST | 400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 400 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 14,183,280 | 100.0% |
| POP_JUMP_IF_FALSE | 1,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 14,183,240 | 100.0% |
| LOAD_FAST | 1,540 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| FOR_ITER_TUPLE | 20 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,493,040 | 100.0% |
| RESUME | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 746,600 | 50.0% |
| SEND | 746,520 | 50.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,482,480 | 100.0% |
| POP_TOP | 100 | 0.0% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,040 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 1,560 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


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
| LOAD_FAST | 26,880,620 | 70.6% |
| LOAD_ATTR_SLOT | 9,704,480 | 25.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,493,520 | 3.9% |
| LOAD_ATTR | 12,320 | 0.0% |
| LOAD_GLOBAL_MODULE | 820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 9,705,180 | 25.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,240 | 25.5% |
| CALL | 8,959,540 | 23.5% |
| LOAD_FAST | 4,479,920 | 11.8% |
| TO_BOOL_NONE | 4,478,920 | 11.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 19,409,120 | 25.7% |
| POP_TOP | 10,453,220 | 13.9% |
| POP_JUMP_IF_FALSE | 9,708,000 | 12.9% |
| LOAD_FAST | 9,706,500 | 12.9% |
| LOAD_FAST_LOAD_FAST | 8,957,920 | 11.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,327,780 | 49.5% |
| STORE_FAST | 10,458,960 | 13.9% |
| CALL_KW | 9,704,480 | 12.9% |
| SEND_GEN | 5,225,440 | 6.9% |
| COMPARE_OP_INT | 4,480,920 | 5.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 620 | 50.8% |
| LOAD_GLOBAL | 200 | 16.4% |
| STORE_FAST | 160 | 13.1% |
| NOP | 80 | 6.6% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 820 | 67.2% |
| LOAD_CONST | 160 | 13.1% |
| PUSH_NULL | 80 | 6.6% |
| POP_JUMP_IF_NOT_NONE | 80 | 6.6% |
| STORE_FAST | 80 | 6.6% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 87,342,460 | 20.7% |
| RESUME_CHECK | 76,148,020 | 18.0% |
| STORE_FAST | 57,492,440 | 13.6% |
| POP_TOP | 38,074,360 | 9.0% |
| LOAD_CONST | 37,327,780 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 137,372,920 | 32.5% |
| LOAD_ATTR_SLOT | 67,930,960 | 16.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,583,640 | 8.7% |
| RETURN_VALUE | 29,115,620 | 6.9% |
| STORE_ATTR_SLOT | 29,113,800 | 6.9% |


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
| STORE_ATTR_SLOT | 29,113,380 | 33.9% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 16.5% |
| PUSH_NULL | 14,183,600 | 16.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 14,183,240 | 16.5% |
| POP_JUMP_IF_NOT_NONE | 9,704,400 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 38,817,760 | 45.2% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 16.5% |
| LOAD_FAST | 9,704,880 | 11.3% |
| CALL | 9,704,560 | 11.3% |
| LOAD_CONST | 8,957,920 | 10.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 500 | 12.8% |
| RESUME_CHECK | 480 | 12.3% |
| POP_TOP | 460 | 11.8% |
| LOAD_FAST | 380 | 9.7% |
| STORE_FAST | 320 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,280 | 32.8% |
| LOAD_ATTR | 800 | 20.5% |
| LOAD_GLOBAL_BUILTIN | 600 | 15.4% |
| LOAD_FAST | 320 | 8.2% |
| CALL | 260 | 6.7% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 380 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 180 | 47.4% |
| CALL | 120 | 31.6% |
| LOAD_FAST | 60 | 15.8% |
| LOAD_FAST_LOAD_FAST | 20 | 5.3% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 72,412,620 | 64.2% |
| TO_BOOL_NONE | 23,887,700 | 21.2% |
| TO_BOOL | 6,719,280 | 6.0% |
| TO_BOOL_LIST | 5,228,660 | 4.6% |
| COMPARE_OP_INT | 4,482,600 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,342,460 | 77.5% |
| RETURN_CONST | 14,930,460 | 13.2% |
| LOAD_CONST | 9,708,000 | 8.6% |
| LOAD_GLOBAL_MODULE | 746,640 | 0.7% |
| LOAD_GLOBAL_BUILTIN | 1,580 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,211,840 | 61.1% |
| LOAD_ATTR_INSTANCE_VALUE | 5,225,580 | 38.9% |
| CALL | 160 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,690,400 | 94.4% |
| LOAD_CONST | 746,480 | 5.6% |
| RETURN_CONST | 480 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,664,400 | 73.5% |
| LOAD_ATTR_INSTANCE_VALUE | 6,718,340 | 26.5% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,704,400 | 38.2% |
| LOAD_FAST | 5,227,220 | 20.6% |
| LOAD_GLOBAL_MODULE | 5,225,760 | 20.6% |
| RETURN_CONST | 4,478,880 | 17.6% |
| LOAD_CONST | 746,500 | 2.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,225,980 | 53.8% |
| TO_BOOL | 4,480,720 | 46.2% |
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
| POP_JUMP_IF_FALSE | 14,930,460 | 26.3% |
| POP_TOP | 13,438,040 | 23.7% |
| STORE_FAST | 9,706,000 | 17.1% |
| STORE_ATTR_SLOT | 9,704,660 | 17.1% |
| POP_JUMP_IF_NOT_NONE | 4,478,880 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 27,621,000 | 48.7% |
| POP_TOP | 23,893,800 | 42.1% |
| END_SEND | 4,479,120 | 7.9% |
| EXIT_INIT_CHECK | 746,460 | 1.3% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,640 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 746,520 | 50.0% |
| SEND | 560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 746,480 | 50.0% |
| YIELD_VALUE | 746,480 | 50.0% |
| SEND | 560 | 0.0% |
| POP_TOP | 100 | 0.0% |
| SEND_GEN | 100 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,740 | 77.4% |
| LOAD_FAST_LOAD_FAST | 300 | 8.5% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 7.9% |
| STORE_ATTR | 100 | 2.8% |
| SWAP | 80 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,280 | 36.2% |
| LOAD_FAST | 580 | 16.4% |
| LOAD_CONST | 500 | 14.1% |
| RETURN_CONST | 500 | 14.1% |
| STORE_ATTR_SLOT | 260 | 7.3% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 18,662,980 | 25.8% |
| RETURN_VALUE | 14,185,600 | 19.6% |
| FOR_ITER_RANGE | 14,183,240 | 19.6% |
| LOAD_CONST | 10,458,960 | 14.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,380 | 13.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,492,440 | 79.4% |
| RETURN_CONST | 9,706,000 | 13.4% |
| JUMP_FORWARD | 4,482,480 | 6.2% |
| LOAD_GLOBAL_BUILTIN | 748,060 | 1.0% |
| NOP | 1,760 | 0.0% |


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
| LOAD_ATTR | 80 | 23.5% |
| LOAD_FAST | 80 | 23.5% |
| BINARY_OP_ADD_INT | 60 | 17.6% |
| BINARY_OP_SUBTRACT_INT | 60 | 17.6% |
| BINARY_OP | 40 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 100 | 29.4% |
| STORE_ATTR | 80 | 23.5% |
| STORE_FAST | 80 | 23.5% |
| STORE_ATTR_INSTANCE_VALUE | 80 | 23.5% |


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
| YIELD_VALUE | 746,640 | 50.0% |
| SEND | 746,480 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 746,640 | 50.0% |
| INTERPRETER_EXIT | 746,480 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,060 | 61.6% |
| CACHE | 260 | 15.1% |
| COPY_FREE_VARS | 200 | 11.6% |
| POP_TOP | 120 | 7.0% |
| SEND_GEN | 40 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 800 | 46.5% |
| LOAD_GLOBAL | 500 | 29.1% |
| LOAD_CONST | 140 | 8.1% |
| NOP | 100 | 5.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 80 | 4.7% |


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
| LOAD_CONST | 40 | 66.7% |
| BINARY_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 60 | 100.0% |


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
| PUSH_NULL | 746,440 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 746,460 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,440 | 98.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 1.9% |
| PUSH_NULL | 40 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 746,460 | 98.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 1.9% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 746,660 | 49.9% |
| LOAD_GLOBAL_MODULE | 746,440 | 49.9% |
| LOAD_FAST | 1,740 | 0.1% |
| CALL | 180 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 748,100 | 50.0% |
| LOAD_FAST | 746,700 | 49.9% |
| COMPARE_OP | 140 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 180 | 75.0% |
| CALL | 40 | 16.7% |
| LOAD_FAST_LOAD_FAST | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 140 | 58.3% |
| TO_BOOL_BOOL | 80 | 33.3% |
| TO_BOOL | 20 | 8.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 746,440 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,460 | 100.0% |


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
| LOAD_ATTR_METHOD_NO_DICT | 9,704,800 | 50.0% |
| LOAD_ATTR | 9,704,240 | 50.0% |
| CALL | 360 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,704,380 | 50.0% |
| TO_BOOL_BOOL | 9,704,200 | 50.0% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |
| CALL | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,140,960 | 83.8% |
| CALL | 4,479,080 | 16.2% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 27,620,120 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 28,370,760 | 54.3% |
| LOAD_FAST | 9,708,640 | 18.6% |
| LOAD_ATTR_METHOD_NO_DICT | 9,704,480 | 18.6% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 8.6% |
| CALL | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 44,053,000 | 84.3% |
| RETURN_GENERATOR | 8,211,380 | 15.7% |
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
| LOAD_FAST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 66.7% |
| LOAD_GLOBAL | 20 | 33.3% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,480,920 | 100.0% |
| LOAD_GLOBAL_MODULE | 1,560 | 0.0% |
| COMPARE_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,482,600 | 100.0% |


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
| GET_ITER | 3,160 | 98.1% |
| FOR_ITER | 60 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,640 | 50.9% |
| LOAD_FAST | 1,580 | 49.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 14,183,240 | 95.0% |
| GET_ITER | 748,040 | 5.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,183,240 | 95.0% |
| LOAD_CONST | 748,080 | 5.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 50.0% |
| JUMP_BACKWARD | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| STORE_FAST | 20 | 50.0% |


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
| LOAD_FAST | 137,372,920 | 96.8% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 3.2% |
| LOAD_ATTR | 1,780 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 48,523,400 | 34.2% |
| LOAD_ATTR_METHOD_NO_DICT | 37,326,500 | 26.3% |
| RETURN_VALUE | 14,930,340 | 10.5% |
| TO_BOOL | 11,199,120 | 7.9% |
| POP_JUMP_IF_NOT_NONE | 6,718,340 | 4.7% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 37,326,500 | 79.4% |
| LOAD_FAST | 9,704,720 | 20.6% |
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
| LOAD_FAST | 36,583,640 | 71.0% |
| LOAD_ATTR_SLOT | 9,704,480 | 18.8% |
| LOAD_ATTR_INSTANCE_VALUE | 5,227,160 | 10.1% |
| LOAD_ATTR | 1,100 | 0.0% |
| RETURN_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 28,370,760 | 55.1% |
| LOAD_FAST_LOAD_FAST | 14,183,240 | 27.5% |
| LOAD_FAST | 8,961,820 | 17.4% |
| CALL | 620 | 0.0% |
| LOAD_CONST | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 17,172,000 | 100.0% |
| LOAD_ATTR | 820 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 17,172,260 | 100.0% |
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
| LOAD_FAST | 67,930,960 | 100.0% |
| LOAD_ATTR | 280 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 19,408,720 | 28.6% |
| LOAD_ATTR | 9,704,480 | 14.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 14.3% |
| TO_BOOL_BOOL | 9,704,400 | 14.3% |
| BUILD_LIST | 9,704,380 | 14.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 748,060 | 49.8% |
| STORE_ATTR_INSTANCE_VALUE | 746,580 | 49.7% |
| RESUME_CHECK | 2,640 | 0.2% |
| POP_JUMP_IF_FALSE | 1,580 | 0.1% |
| JUMP_FORWARD | 1,560 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 746,660 | 49.7% |
| LOAD_GLOBAL_MODULE | 746,480 | 49.7% |
| LOAD_FAST | 7,620 | 0.5% |
| LOAD_DEREF | 620 | 0.0% |
| CALL_ISINSTANCE | 380 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,452,980 | 46.7% |
| POP_JUMP_IF_NOT_NONE | 5,225,760 | 23.3% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 20.0% |
| STORE_ATTR_INSTANCE_VALUE | 746,800 | 3.3% |
| POP_JUMP_IF_FALSE | 746,640 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 17,172,000 | 76.7% |
| LOAD_FAST_LOAD_FAST | 4,479,200 | 20.0% |
| CALL_BUILTIN_CLASS | 746,440 | 3.3% |
| COMPARE_OP_INT | 1,560 | 0.0% |
| LOAD_ATTR | 820 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 71.0% |
| LOAD_SUPER_ATTR | 180 | 29.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260 | 41.9% |
| CALL_PY_EXACT_ARGS | 200 | 32.3% |
| CALL | 100 | 16.1% |
| LOAD_FAST_LOAD_FAST | 60 | 9.7% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 44,053,000 | 42.8% |
| CACHE | 38,818,140 | 37.7% |
| POP_TOP | 9,704,440 | 9.4% |
| CALL | 4,479,460 | 4.3% |
| CALL_KW | 4,478,940 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 76,148,020 | 73.9% |
| LOAD_GLOBAL_MODULE | 10,452,980 | 10.1% |
| NOP | 9,705,020 | 9.4% |
| RETURN_CONST | 3,732,460 | 3.6% |
| LOAD_CONST | 1,493,380 | 1.4% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,225,440 | 87.5% |
| JUMP_BACKWARD_NO_INTERRUPT | 746,600 | 12.5% |
| SEND | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,225,500 | 87.5% |
| RESUME_CHECK | 746,600 | 12.5% |
| RESUME | 40 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,945,020 | 100.0% |
| STORE_ATTR | 1,280 | 0.0% |
| LOAD_FAST_LOAD_FAST | 260 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,226,060 | 43.7% |
| LOAD_FAST | 2,986,600 | 25.0% |
| RETURN_CONST | 747,120 | 6.3% |
| LOAD_GLOBAL_MODULE | 746,800 | 6.3% |
| BUILD_LIST | 746,680 | 6.3% |


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
| LOAD_ATTR | 40 | 66.7% |
| STORE_SUBSCR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 48,523,400 | 62.5% |
| RETURN_VALUE | 9,704,960 | 12.5% |
| LOAD_ATTR_SLOT | 9,704,400 | 12.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,704,200 | 12.5% |
| TO_BOOL | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 72,412,620 | 93.3% |
| POP_JUMP_IF_TRUE | 5,225,980 | 6.7% |
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
| LOAD_ATTR_INSTANCE_VALUE | 5,228,580 | 100.0% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,228,660 | 100.0% |


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
|     deferred | 580 | 0.0% |
|          hit | 4,480,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 45.5% |
| Failure | 120 | 54.5% |

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
|     deferred | 34,345,900 | 25.1% |
|          hit | 102,290,600 | 74.8% |
|         miss | 761,180 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,960 | 61.8% |
| Failure | 10,500 | 38.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 3,000 | 28.6% |
| no dict | 2,580 | 24.6% |
| code complex parameters | 1,340 | 12.8% |
| class no vectorcall | 1,340 | 12.8% |
| other | 1,280 | 12.2% |
| cfunc noargs | 660 | 6.3% |
| class mutable | 80 | 0.8% |
| metaclass | 60 | 0.6% |
| wrong number arguments | 40 | 0.4% |
| cfunc varargs | 40 | 0.4% |
| operator wrapper | 40 | 0.4% |
| cmethod | 20 | 0.2% |
| cfunc varargs keywords | 20 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 4,482,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 75.0% |
| Failure | 40 | 25.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bool | 40 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 14,934,580 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 55.6% |
| Failure | 80 | 44.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 80 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 38,077,300 | 10.5% |
|          hit | 325,507,060 | 89.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,560 | 28.4% |
| Failure | 11,500 | 71.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 6,000 | 52.2% |
| method | 3,980 | 34.6% |
| class attr descriptor | 1,280 | 11.1% |
| not managed dict | 140 | 1.2% |
| metaclass attribute | 60 | 0.5% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,100 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 23,904,040 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,880 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 20.0% |
|          hit | 620 | 62.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
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
|     deferred | 1,493,060 | 20.0% |
|          hit | 5,972,140 | 80.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 15.2% |
| Failure | 560 | 84.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 560 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,900 | 0.0% |
|          hit | 79,878,460 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,540 | 93.9% |
| Failure | 100 | 6.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 80 | 80.0% |
| overriding descriptor | 20 | 20.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 33.3% |
|          hit | 60 | 50.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,200,040 | 9.5% |
|          hit | 106,756,980 | 90.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,140 | 23.1% |
| Failure | 3,800 | 76.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 3,700 | 97.4% |
| sequence | 100 | 2.6% |


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
| Basic | 1,025,837,500 | 50.2% |
| Not specialized | 245,675,000 | 12.0% |
| Specialized hits | 771,210,020 | 37.7% |
| Specialized misses | 787,640 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 38,077,300 | 44.7% |
| CALL | 34,345,900 | 40.3% |
| TO_BOOL | 11,200,040 | 13.2% |
| SEND | 1,493,060 | 1.8% |
| LOAD_GLOBAL | 2,100 | 0.0% |
| STORE_ATTR | 1,900 | 0.0% |
| BINARY_OP | 580 | 0.0% |
| COMPARE_OP | 340 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 760,800 | 93.5% |
| RESUME | 26,380 | 3.2% |
| RESUME_CHECK | 26,380 | 3.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 260 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_ASYNC_WITH | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 44,790,500 | 39.7% |
| Calls to Python functions inlined | 67,944,040 | 60.3% |
| Calls via PyEval_EvalFrame (total) | 44,790,500 | 39.7% |
| Calls via PyEval_EvalFrame (vector) | 39,565,060 | 35.1% |
| Calls via PyEval_EvalFrame (generator) | 5,225,440 | 4.6% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 39,565,060 | 35.1% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 4.0% |
| Calls via PyEval_EvalFrame (method) | 19,408,800 | 17.2% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 53,758,460 | 47.7% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 50,789,220 | 35.0% |
| Frees to freelist | 50,957,180 |  |
| Allocations | 94,277,347 | 65.0% |
| Allocations to 512 bytes | 93,472,320 | 64.4% |
| Allocations to 4 kbytes | 804,920 | 0.6% |
| Allocations over 4 kbytes | 107 | 0.0% |
| Frees | 94,234,418 |  |
| New values | 440 |  |
| Interpreter increfs | 1,063,868,680 | 79.4% |
| Interpreter decrefs | 1,121,146,020 | 76.4% |
| Increfs | 276,218,602 | 20.6% |
| Decrefs | 346,495,087 | 23.6% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 57,501,341 |  |
| Method cache misses | 3,779 |  |
| Method cache collisions | 3,584 |  |
| Method cache dunder hits | 11,198,864 |  |
| Method cache dunder misses | 396 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 51,280 | 2,040 | 274,480,120 |
| 1 | 4,660 | 0 | 296,829,880 |
| 2 | 400 | 0 | 849,086,280 |


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
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
