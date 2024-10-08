
# Pystats results

- benchmark: async_tree
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 349,431,640 | 18.1% | 18.1% |  |
| POP_JUMP_IF_FALSE | 109,003,400 | 5.6% | 23.7% |  |
| RESUME_CHECK | 100,790,620 | 5.2% | 28.9% | 0.0% |
| LOAD_FAST_LOAD_FAST | 92,569,640 | 4.8% | 33.7% |  |
| LOAD_CONST | 85,862,540 | 4.4% | 38.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 76,167,660 | 3.9% | 42.0% |  |
| STORE_FAST | 73,184,000 | 3.8% | 45.8% |  |
| POP_TOP | 70,925,500 | 3.7% | 49.5% |  |
| STORE_ATTR_SLOT | 67,931,820 | 3.5% | 53.0% |  |
| TO_BOOL_BOOL | 66,445,220 | 3.4% | 56.4% |  |
| RETURN_CONST | 60,472,860 | 3.1% | 59.6% |  |
| CALL_PY_EXACT_ARGS | 51,520,260 | 2.7% | 62.2% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 51,516,760 | 2.7% | 64.9% |  |
| RETURN_VALUE | 49,275,200 | 2.5% | 67.4% |  |
| INTERPRETER_EXIT | 44,044,000 | 2.3% | 69.7% |  |
| LOAD_DEREF | 40,311,140 | 2.1% | 71.8% |  |
| CALL | 38,839,080 | 2.0% | 73.8% |  |
| LOAD_GLOBAL_MODULE | 36,585,340 | 1.9% | 75.7% |  |
| LOAD_ATTR_SLOT | 33,600,120 | 1.7% | 77.4% |  |
| PUSH_NULL | 30,612,140 | 1.6% | 79.0% |  |
| LOAD_ATTR | 29,134,820 | 1.5% | 80.5% |  |
| POP_JUMP_IF_NOT_NONE | 28,369,080 | 1.5% | 82.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 27,626,800 | 1.4% | 83.4% |  |
| LOAD_ATTR_MODULE | 25,384,240 | 1.3% | 84.7% |  |
| TO_BOOL_NONE | 23,887,700 | 1.2% | 86.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,751,120 | 1.0% | 86.9% | 24.3% |
| CALL_METHOD_DESCRIPTOR_O | 18,662,420 | 1.0% | 87.9% | 0.0% |
| ENTER_EXECUTOR | 18,661,220 | 1.0% | 88.8% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.7% | 89.5% |  |
| STORE_DEREF | 12,690,160 | 0.7% | 90.2% |  |
| LOAD_GLOBAL_BUILTIN | 10,459,920 | 0.5% | 90.7% | 0.0% |
| CALL_FUNCTION_EX | 10,451,120 | 0.5% | 91.3% |  |
| CALL_KW | 10,450,960 | 0.5% | 91.8% |  |
| POP_JUMP_IF_TRUE | 9,708,340 | 0.5% | 92.3% |  |
| COMPARE_OP_INT | 8,961,460 | 0.5% | 92.8% |  |
| BINARY_OP_ADD_INT | 8,957,780 | 0.5% | 93.2% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.5% | 93.7% |  |
| RETURN_GENERATOR | 8,211,600 | 0.4% | 94.1% |  |
| TO_BOOL | 5,230,980 | 0.3% | 94.4% |  |
| NOP | 5,230,360 | 0.3% | 94.7% |  |
| STORE_ATTR | 5,229,960 | 0.3% | 94.9% |  |
| FOR_ITER_RANGE | 5,228,800 | 0.3% | 95.2% |  |
| COPY_FREE_VARS | 5,226,420 | 0.3% | 95.5% |  |
| CONTAINS_OP | 5,225,800 | 0.3% | 95.8% |  |
| JUMP_FORWARD | 4,482,660 | 0.2% | 96.0% |  |
| TO_BOOL_LIST | 4,482,200 | 0.2% | 96.2% |  |
| JUMP_BACKWARD | 4,481,440 | 0.2% | 96.4% |  |
| COPY | 4,481,220 | 0.2% | 96.7% |  |
| IS_OP | 4,479,280 | 0.2% | 96.9% |  |
| END_SEND | 4,479,120 | 0.2% | 97.1% |  |
| GET_AWAITABLE | 4,479,120 | 0.2% | 97.4% |  |
| CALL_BUILTIN_FAST | 4,479,120 | 0.2% | 97.6% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 97.8% |  |
| BINARY_OP_SUBTRACT_INT | 4,478,920 | 0.2% | 98.1% |  |
| STORE_SUBSCR_DICT | 4,478,920 | 0.2% | 98.3% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 98.5% |  |
| SEND_GEN | 3,732,740 | 0.2% | 98.7% |  |
| MAKE_CELL | 3,732,480 | 0.2% | 98.9% |  |
| GET_ITER | 2,990,980 | 0.2% | 99.1% |  |
| BUILD_LIST | 2,989,640 | 0.2% | 99.2% |  |
| FOR_ITER_LIST | 2,242,900 | 0.1% | 99.3% |  |
| SWAP | 2,239,780 | 0.1% | 99.5% |  |
| SEND | 1,493,640 | 0.1% | 99.5% |  |
| FOR_ITER_TUPLE | 1,493,260 | 0.1% | 99.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.7% |  |
| CALL_BUILTIN_CLASS | 748,760 | 0.0% | 99.7% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_METHOD | 747,080 | 0.0% | 99.8% |  |
| BUILD_MAP | 746,880 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.8% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 746,640 | 0.0% | 99.9% |  |
| YIELD_VALUE | 746,640 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| CALL_LEN | 4,740 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,940 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 1,960 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 1,880 | 0.0% | 100.0% |  |
| LIST_EXTEND | 1,880 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,780 | 0.0% | 100.0% |  |
| RESUME | 1,640 | 0.0% | 100.0% | 2,514.6% |
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
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 70,940,560 | 3.7% | 3.7% |
| RESUME_CHECK LOAD_FAST | 67,936,760 | 3.5% | 7.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 57,486,760 | 3.0% | 10.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 55,994,020 | 2.9% | 13.0% |
| STORE_FAST LOAD_FAST | 52,270,800 | 2.7% | 15.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 43,308,240 | 2.2% | 18.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 38,817,760 | 2.0% | 20.0% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 36,583,680 | 1.9% | 21.9% |
| LOAD_CONST LOAD_FAST | 34,341,860 | 1.8% | 23.6% |
| CACHE RESUME_CHECK | 34,339,280 | 1.8% | 25.4% |
| LOAD_FAST LOAD_ATTR_SLOT | 33,599,760 | 1.7% | 27.2% |
| LOAD_FAST LOAD_ATTR | 29,119,700 | 1.5% | 28.7% |
| LOAD_FAST STORE_ATTR_SLOT | 29,113,800 | 1.5% | 30.2% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 29,113,380 | 1.5% | 31.7% |
| RETURN_CONST INTERPRETER_EXIT | 28,367,460 | 1.5% | 33.1% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 27,624,320 | 1.4% | 34.6% |
| LOAD_ATTR_MODULE PUSH_NULL | 25,383,560 | 1.3% | 35.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 25,383,320 | 1.3% | 37.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 24,637,920 | 1.3% | 38.5% |
| RETURN_CONST POP_TOP | 23,893,800 | 1.2% | 39.7% |
| POP_TOP LOAD_FAST | 23,891,240 | 1.2% | 40.9% |
| LOAD_FAST RETURN_VALUE | 23,890,260 | 1.2% | 42.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,889,760 | 1.2% | 43.4% |
| CALL STORE_FAST | 23,888,360 | 1.2% | 44.6% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 23,887,700 | 1.2% | 45.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 23,141,220 | 1.2% | 47.1% |
| POP_JUMP_IF_FALSE RETURN_CONST | 22,395,260 | 1.2% | 48.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 19,412,840 | 1.0% | 49.2% |
| STORE_ATTR_SLOT LOAD_CONST | 19,409,120 | 1.0% | 50.2% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 19,408,720 | 1.0% | 51.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 18,666,300 | 1.0% | 52.2% |
| POP_JUMP_IF_FALSE LOAD_CONST | 18,665,760 | 1.0% | 53.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 18,662,400 | 1.0% | 54.1% |
| LOAD_CONST STORE_FAST | 14,937,840 | 0.8% | 54.9% |
| RETURN_VALUE STORE_FAST | 14,932,080 | 0.8% | 55.7% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 14,930,340 | 0.8% | 56.4% |
| RETURN_VALUE INTERPRETER_EXIT | 14,930,060 | 0.8% | 57.2% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 14,185,420 | 0.7% | 57.9% |
| POP_TOP RETURN_CONST | 14,184,520 | 0.7% | 58.7% |
| RETURN_VALUE TO_BOOL_BOOL | 14,183,840 | 0.7% | 59.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,183,760 | 0.7% | 60.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,183,760 | 0.7% | 60.9% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,183,600 | 0.7% | 61.6% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 14,183,360 | 0.7% | 62.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 14,183,320 | 0.7% | 63.1% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,183,280 | 0.7% | 63.8% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,436,800 | 0.7% | 64.5% |
| LOAD_FAST LOAD_CONST | 10,452,980 | 0.5% | 65.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 9,708,300 | 0.5% | 65.5% |
| PUSH_NULL LOAD_FAST | 9,706,840 | 0.5% | 66.0% |
| POP_TOP LOAD_CONST | 9,706,740 | 0.5% | 66.5% |
| LOAD_FAST CALL | 9,706,160 | 0.5% | 67.0% |
| STORE_FAST RETURN_CONST | 9,706,000 | 0.5% | 67.5% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,704,660 | 0.5% | 68.0% |
| STORE_ATTR_SLOT LOAD_FAST | 9,704,660 | 0.5% | 68.5% |
| STORE_ATTR_SLOT RETURN_CONST | 9,704,660 | 0.5% | 69.0% |
| CALL_FUNCTION_EX POP_TOP | 9,704,560 | 0.5% | 69.6% |
| LOAD_FAST_LOAD_FAST CALL | 9,704,560 | 0.5% | 70.1% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 0.5% | 70.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 9,704,380 | 0.5% | 71.1% |
| POP_TOP ENTER_EXECUTOR | 9,704,060 | 0.5% | 71.6% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 9,702,520 | 0.5% | 72.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 8,965,380 | 0.5% | 72.5% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 8,961,460 | 0.5% | 73.0% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 8,960,400 | 0.5% | 73.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 8,958,400 | 0.5% | 73.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.5% | 74.4% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.5% | 74.8% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.5% | 75.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,957,720 | 0.5% | 75.8% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.5% | 76.2% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.5% | 76.7% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 8,957,080 | 0.5% | 77.2% |
| POP_TOP RESUME_CHECK | 8,211,520 | 0.4% | 77.6% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,211,380 | 0.4% | 78.0% |
| LOAD_CONST CALL_KW | 6,718,840 | 0.3% | 78.3% |
| PUSH_NULL CALL | 5,974,820 | 0.3% | 78.7% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 5,972,200 | 0.3% | 79.0% |
| NOP LOAD_FAST | 5,229,800 | 0.3% | 79.2% |
| LOAD_ATTR CALL | 5,227,440 | 0.3% | 79.5% |
| CALL POP_TOP | 5,226,120 | 0.3% | 79.8% |
| COPY_FREE_VARS RESUME_CHECK | 5,226,020 | 0.3% | 80.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 5,225,940 | 0.3% | 80.3% |
| LOAD_FAST PUSH_NULL | 5,225,860 | 0.3% | 80.6% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 5,225,800 | 0.3% | 80.9% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 5,225,800 | 0.3% | 81.1% |
| CACHE COPY_FREE_VARS | 5,225,540 | 0.3% | 81.4% |
| POP_JUMP_IF_FALSE LOAD_DEREF | 5,225,360 | 0.3% | 81.7% |
| LOAD_DEREF LOAD_ATTR_METHOD_WITH_VALUES | 5,225,280 | 0.3% | 81.9% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 4,482,200 | 0.2% | 82.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 4,482,140 | 0.2% | 82.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 4,481,040 | 0.2% | 82.6% |
| LOAD_FAST STORE_ATTR | 4,481,020 | 0.2% | 82.9% |
| LOAD_CONST COMPARE_OP_INT | 4,480,920 | 0.2% | 83.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 4,480,780 | 0.2% | 83.3% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 4,480,740 | 0.2% | 83.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 4,480,720 | 0.2% | 83.8% |
| FOR_ITER_RANGE STORE_FAST | 4,480,720 | 0.2% | 84.0% |
| LOAD_ATTR LOAD_FAST | 4,479,920 | 0.2% | 84.2% |
| TO_BOOL POP_JUMP_IF_FALSE | 4,479,800 | 0.2% | 84.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 34,339,280 | 78.0% |
| COPY_FREE_VARS | 5,225,540 | 11.9% |
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
| RETURN_CONST | 28,367,460 | 64.4% |
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
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 71.4% |
| RESUME_CHECK | 748,980 | 14.3% |
| STORE_FAST | 748,240 | 14.3% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,229,800 | 100.0% |
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
| ENTER_EXECUTOR | 9,704,060 | 13.7% |
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
| LOAD_ATTR_MODULE | 25,383,560 | 82.9% |
| LOAD_FAST | 5,225,860 | 17.1% |
| LOAD_ATTR | 2,640 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,183,600 | 46.3% |
| LOAD_FAST | 9,706,840 | 31.7% |
| CALL | 5,974,820 | 19.5% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 2.4% |
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
| STORE_FAST | 14,932,080 | 30.3% |
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
| STORE_FAST | 748,080 | 25.0% |
| POP_JUMP_IF_FALSE | 746,480 | 25.0% |
| STORE_DEREF | 746,480 | 25.0% |
| SWAP | 746,480 | 25.0% |
| LOAD_ATTR_SLOT | 1,860 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,494,560 | 50.0% |
| STORE_DEREF | 746,480 | 25.0% |
| SWAP | 746,480 | 25.0% |
| LOAD_FAST | 2,120 | 0.1% |


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
| LOAD_FAST | 9,706,160 | 25.0% |
| LOAD_FAST_LOAD_FAST | 9,704,560 | 25.0% |
| PUSH_NULL | 5,974,820 | 15.4% |
| LOAD_ATTR | 5,227,440 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,080 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,888,360 | 61.5% |
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
| ENTER_EXECUTOR | 9,702,520 | 92.8% |
| STORE_FAST | 746,480 | 7.1% |
| CALL_INTRINSIC_1 | 1,880 | 0.0% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

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
| LIST_EXTEND | 1,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,880 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,718,840 | 64.3% |
| ENTER_EXECUTOR | 3,732,120 | 35.7% |

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
| LOAD_GLOBAL_MODULE | 4,478,940 | 85.7% |
| LOAD_FAST_LOAD_FAST | 746,760 | 14.3% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,225,800 | 100.0% |


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
| CACHE | 5,225,540 | 100.0% |
| CALL_PY_EXACT_ARGS | 640 | 0.0% |
| CALL | 160 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,704,060 | 52.0% |
| CALL_LIST_APPEND | 8,957,080 | 48.0% |
| JUMP_BACKWARD | 60 | 0.0% |
| POP_JUMP_IF_FALSE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,702,520 | 52.0% |
| CALL | 3,732,120 | 20.0% |
| CALL_KW | 3,732,120 | 20.0% |
| FOR_ITER_TUPLE | 746,460 | 4.0% |
| FOR_ITER_LIST | 746,440 | 4.0% |


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
| LIST_APPEND | 4,478,880 | 99.9% |
| POP_JUMP_IF_FALSE | 1,540 | 0.0% |
| CALL_LIST_APPEND | 640 | 0.0% |
| POP_TOP | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 4,479,160 | 99.9% |
| LOAD_FAST | 1,540 | 0.0% |
| FOR_ITER_LIST | 300 | 0.0% |
| FOR_ITER_TUPLE | 300 | 0.0% |
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
| LOAD_FAST | 2,160 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,560 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


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
| LOAD_ATTR_SLOT | 1,860 | 98.9% |
| LOAD_ATTR | 20 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,880 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,119,700 | 99.9% |
| LOAD_ATTR | 10,100 | 0.0% |
| LOAD_ATTR_SLOT | 1,960 | 0.0% |
| LOAD_GLOBAL_MODULE | 800 | 0.0% |
| LOAD_GLOBAL | 780 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,183,360 | 48.7% |
| CALL | 5,227,440 | 17.9% |
| LOAD_FAST | 4,479,920 | 15.4% |
| TO_BOOL_NONE | 4,478,920 | 15.4% |
| STORE_FAST | 746,640 | 2.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 19,409,120 | 22.6% |
| POP_JUMP_IF_FALSE | 18,665,760 | 21.7% |
| LOAD_FAST | 10,452,980 | 12.2% |
| POP_TOP | 9,706,740 | 11.3% |
| LOAD_DEREF | 8,957,920 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,341,860 | 40.0% |
| STORE_FAST | 14,937,840 | 17.4% |
| BINARY_OP_ADD_INT | 8,957,720 | 10.4% |
| CALL_KW | 6,718,840 | 7.8% |
| COMPARE_OP_INT | 4,480,920 | 5.2% |


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
| RESUME_CHECK | 67,936,760 | 19.4% |
| POP_JUMP_IF_FALSE | 55,994,020 | 16.0% |
| STORE_FAST | 52,270,800 | 15.0% |
| LOAD_CONST | 34,341,860 | 9.8% |
| POP_TOP | 23,891,240 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 70,940,560 | 20.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,583,680 | 10.5% |
| LOAD_ATTR_SLOT | 33,599,760 | 9.6% |
| LOAD_ATTR | 29,119,700 | 8.3% |
| STORE_ATTR_SLOT | 29,113,800 | 8.3% |


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
| STORE_ATTR_SLOT | 29,113,380 | 31.5% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 15.3% |
| PUSH_NULL | 14,183,600 | 15.3% |
| POP_JUMP_IF_NOT_NONE | 13,436,800 | 14.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,704,380 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 38,817,760 | 41.9% |
| LOAD_FAST | 14,183,760 | 15.3% |
| LOAD_FAST_LOAD_FAST | 14,183,760 | 15.3% |
| CALL | 9,704,560 | 10.5% |
| LOAD_CONST | 5,225,800 | 5.6% |


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
| TO_BOOL_BOOL | 57,486,760 | 52.7% |
| TO_BOOL_NONE | 23,887,700 | 21.9% |
| COMPARE_OP_INT | 8,961,460 | 8.2% |
| CONTAINS_OP | 5,225,800 | 4.8% |
| TO_BOOL_LIST | 4,482,200 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,994,020 | 51.4% |
| RETURN_CONST | 22,395,260 | 20.5% |
| LOAD_CONST | 18,665,760 | 17.1% |
| LOAD_DEREF | 5,225,360 | 4.8% |
| RETURN_VALUE | 4,479,040 | 4.1% |


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
| INTERPRETER_EXIT | 28,367,460 | 46.9% |
| POP_TOP | 23,893,800 | 39.5% |
| TO_BOOL_BOOL | 4,478,920 | 7.4% |
| END_SEND | 3,732,640 | 6.2% |
| TO_BOOL | 40 | 0.0% |


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
| CALL | 23,888,360 | 32.6% |
| LOAD_CONST | 14,937,840 | 20.4% |
| RETURN_VALUE | 14,932,080 | 20.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,480,720 | 6.1% |
| FOR_ITER_RANGE | 4,480,720 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,270,800 | 71.4% |
| RETURN_CONST | 9,706,000 | 13.3% |
| LOAD_GLOBAL_MODULE | 4,479,080 | 6.1% |
| LOAD_FAST_LOAD_FAST | 1,493,560 | 2.0% |
| LOAD_CONST | 1,493,040 | 2.0% |


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
| ENTER_EXECUTOR | 8,957,080 | 100.0% |
| JUMP_BACKWARD | 640 | 0.0% |


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
| LOAD_ATTR | 14,183,360 | 75.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 23.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,280 | 0.0% |
| CALL | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 14,183,320 | 75.6% |
| STORE_FAST | 4,480,720 | 23.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.5% |
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
| LOAD_ATTR_METHOD_WITH_VALUES | 27,624,320 | 53.6% |
| LOAD_FAST | 19,412,840 | 37.7% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 8.7% |
| LOAD_ATTR_METHOD_NO_DICT | 1,960 | 0.0% |
| CALL | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 43,308,240 | 84.1% |
| RETURN_GENERATOR | 8,211,380 | 15.9% |
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
| GET_ITER | 1,496,060 | 66.7% |
| ENTER_EXECUTOR | 746,440 | 33.3% |
| JUMP_BACKWARD | 300 | 0.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 1,492,940 | 66.6% |
| STORE_FAST | 746,740 | 33.3% |
| RETURN_CONST | 1,640 | 0.1% |
| LOAD_FAST | 1,580 | 0.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,479,160 | 85.7% |
| SWAP | 746,460 | 14.3% |
| GET_ITER | 1,580 | 0.0% |
| ENTER_EXECUTOR | 1,560 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,480,720 | 85.7% |
| SWAP | 746,480 | 14.3% |
| LOAD_CONST | 1,600 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 746,480 | 50.0% |
| ENTER_EXECUTOR | 746,460 | 50.0% |
| JUMP_BACKWARD | 300 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,760 | 50.0% |
| LOAD_GLOBAL_MODULE | 746,440 | 50.0% |
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
| LOAD_FAST | 70,940,560 | 93.1% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 5.9% |
| LOAD_DEREF | 746,440 | 1.0% |
| LOAD_ATTR | 1,340 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 24,637,920 | 32.3% |
| LOAD_ATTR_METHOD_NO_DICT | 18,666,300 | 24.5% |
| RETURN_VALUE | 14,930,340 | 19.6% |
| TO_BOOL_LIST | 4,482,140 | 5.9% |
| TO_BOOL | 4,480,780 | 5.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 18,666,300 | 67.6% |
| LOAD_FAST | 4,481,040 | 16.2% |
| LOAD_DEREF | 4,478,840 | 16.2% |
| LOAD_ATTR | 540 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,141,220 | 83.8% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 16.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,280 | 0.0% |
| CALL_PY_EXACT_ARGS | 1,960 | 0.0% |
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
| LOAD_FAST | 33,599,760 | 100.0% |
| LOAD_ATTR | 280 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 19,408,720 | 57.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,704,480 | 28.9% |
| LOAD_CONST | 4,479,160 | 13.3% |
| LOAD_ATTR | 1,960 | 0.0% |
| TO_BOOL_BOOL | 1,880 | 0.0% |


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
| RESUME_CHECK | 14,185,420 | 38.8% |
| POP_JUMP_IF_NOT_NONE | 5,972,200 | 16.3% |
| STORE_FAST | 4,479,080 | 12.2% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 12.2% |
| CALL_TYPE_1 | 4,478,920 | 12.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 25,383,320 | 69.4% |
| LOAD_FAST_LOAD_FAST | 5,225,940 | 14.3% |
| CONTAINS_OP | 4,478,940 | 12.2% |
| LOAD_DEREF | 746,460 | 2.0% |
| CALL_BUILTIN_CLASS | 746,440 | 2.0% |


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
| CALL_PY_EXACT_ARGS | 43,308,240 | 43.0% |
| CACHE | 34,339,280 | 34.1% |
| POP_TOP | 8,211,520 | 8.1% |
| COPY_FREE_VARS | 5,226,020 | 5.2% |
| CALL | 4,479,500 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,936,760 | 67.4% |
| LOAD_GLOBAL_MODULE | 14,185,420 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 8,960,400 | 8.9% |
| LOAD_DEREF | 4,478,920 | 4.4% |
| RETURN_CONST | 3,732,460 | 3.7% |


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
| LOAD_ATTR_INSTANCE_VALUE | 24,637,920 | 37.1% |
| RETURN_VALUE | 14,183,840 | 21.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,183,320 | 21.3% |
| COPY | 4,479,080 | 6.7% |
| RETURN_CONST | 4,478,920 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 57,486,760 | 86.5% |
| POP_JUMP_IF_TRUE | 8,958,400 | 13.5% |
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
|     deferred | 43,303,620 | 25.5% |
|          hit | 126,178,000 | 74.4% |
|         miss | 4,565,360 | 2.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 88,700 | 88.0% |
| Failure | 12,120 | 12.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 4,280 | 35.3% |
| no dict | 2,580 | 21.3% |
| class no vectorcall | 1,340 | 11.1% |
| code complex parameters | 1,320 | 10.9% |
| other | 1,280 | 10.6% |
| cfunc noargs | 660 | 5.4% |
| cmethod | 380 | 3.1% |
| class mutable | 80 | 0.7% |
| metaclass | 60 | 0.5% |
| wrong number arguments | 40 | 0.3% |
| cfunc varargs | 40 | 0.3% |
| operator wrapper | 40 | 0.3% |
| cfunc varargs keywords | 20 | 0.2% |


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
|          hit | 8,964,960 | 100.0% |

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
|     deferred | 29,121,340 | 9.1% |
|          hit | 291,915,940 | 90.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,080 | 30.3% |
| Failure | 9,400 | 69.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 7,280 | 77.4% |
| class attr descriptor | 1,280 | 13.6% |
| method | 600 | 6.4% |
| not managed dict | 140 | 1.5% |
| metaclass attribute | 60 | 0.6% |
| class attr simple | 40 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,120 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 47,045,180 | 100.0% |
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
| Basic | 1,021,384,980 | 52.8% |
| Not specialized | 240,453,580 | 12.4% |
| Specialized hits | 668,953,700 | 34.6% |
| Specialized misses | 4,606,680 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 43,303,620 | 51.3% |
| LOAD_ATTR | 29,121,340 | 34.5% |
| TO_BOOL | 5,228,140 | 6.2% |
| STORE_ATTR | 5,226,960 | 6.2% |
| SEND | 1,493,020 | 1.8% |
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
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 98.2% |
| RESUME | 41,240 | 0.9% |
| RESUME_CHECK | 41,240 | 0.9% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| END_SEND | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 44,044,000 | 37.1% |
| Calls to Python functions inlined | 74,662,380 | 62.9% |
| Calls via PyEval_EvalFrame (total) | 44,044,000 | 37.1% |
| Calls via PyEval_EvalFrame (vector) | 38,818,560 | 32.7% |
| Calls via PyEval_EvalFrame (generator) | 5,225,440 | 4.4% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 38,818,560 | 32.7% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 746,560 | 0.6% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.8% |
| Calls via PyEval_EvalFrame (method) | 19,408,800 | 16.4% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 109,748,140 | 92.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 58,343,760 | 37.2% |
| Frees to freelist | 58,597,880 |  |
| Allocations | 98,662,166 | 62.8% |
| Allocations to 512 bytes | 98,603,600 | 62.8% |
| Allocations to 4 kbytes | 58,460 | 0.0% |
| Allocations over 4 kbytes | 106 | 0.0% |
| Frees | 100,808,069 |  |
| New values | 420 |  |
| Interpreter increfs | 1,002,682,960 | 67.6% |
| Interpreter decrefs | 1,078,098,060 | 66.5% |
| Increfs | 481,505,013 | 32.4% |
| Decrefs | 543,333,234 | 33.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 82,745,289 |  |
| Method cache misses | 884,651 |  |
| Method cache collisions | 880,715 |  |
| Method cache dunder hits | 10,452,374 |  |
| Method cache dunder misses | 366 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 49,260 | 2,040 | 257,811,600 |
| 1 | 4,480 | 0 | 278,829,520 |
| 2 | 380 | 0 | 752,907,000 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 2,400 |  |
| Traces created | 2,400 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 2,300 | 95.8% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 2,380 | 99.2% |
| <= 64 | 0 | 0.0% |
| <= 128 | 20 | 0.8% |


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
| <= 16 | 20 | 0.8% |
| <= 32 | 20 | 0.8% |
| <= 64 | 20 | 0.8% |


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
| CALL | 20 |
| CALL_FUNCTION_EX | 20 |
| CALL_KW | 20 |


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
