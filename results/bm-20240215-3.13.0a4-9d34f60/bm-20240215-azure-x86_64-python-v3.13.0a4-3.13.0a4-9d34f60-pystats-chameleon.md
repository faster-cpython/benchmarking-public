
# Pystats results

- benchmark: chameleon
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 366,174,080 | 21.8% | 21.8% |  |
| LOAD_CONST | 194,599,760 | 11.6% | 33.3% |  |
| STORE_FAST | 168,366,480 | 10.0% | 43.3% |  |
| PUSH_NULL | 100,496,960 | 6.0% | 49.3% |  |
| IS_OP | 91,528,960 | 5.4% | 54.8% |  |
| LOAD_GLOBAL_MODULE | 88,992,880 | 5.3% | 60.1% |  |
| LOAD_GLOBAL_BUILTIN | 87,052,580 | 5.2% | 65.2% |  |
| POP_JUMP_IF_FALSE | 72,330,320 | 4.3% | 69.5% |  |
| POP_TOP | 52,491,600 | 3.1% | 72.6% |  |
| CALL_BUILTIN_O | 52,482,300 | 3.1% | 75.8% |  |
| LOAD_FAST_LOAD_FAST | 37,136,640 | 2.2% | 78.0% |  |
| RESUME_CHECK | 35,219,040 | 2.1% | 80.1% |  |
| RETURN_VALUE | 34,574,160 | 2.1% | 82.1% |  |
| POP_JUMP_IF_TRUE | 26,241,280 | 1.6% | 83.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 20,884,160 | 1.2% | 84.9% | 100.0% |
| LOAD_ATTR_CLASS | 20,487,660 | 1.2% | 86.1% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 20,482,420 | 1.2% | 87.4% |  |
| POP_JUMP_IF_NONE | 19,845,120 | 1.2% | 88.5% |  |
| STORE_SUBSCR | 14,727,240 | 0.9% | 89.4% |  |
| CALL_PY_EXACT_ARGS | 13,442,460 | 0.8% | 90.2% |  |
| COPY_FREE_VARS | 12,801,360 | 0.8% | 91.0% |  |
| POP_JUMP_IF_NOT_NONE | 12,801,280 | 0.8% | 91.7% |  |
| TO_BOOL_BOOL | 12,801,220 | 0.8% | 92.5% |  |
| CALL_TYPE_1 | 12,799,980 | 0.8% | 93.3% |  |
| CALL_STR_1 | 12,799,960 | 0.8% | 94.0% |  |
| CALL | 8,331,720 | 0.5% | 94.5% |  |
| CALL_BUILTIN_FAST | 8,328,760 | 0.5% | 95.0% |  |
| JUMP_FORWARD | 7,682,560 | 0.5% | 95.5% |  |
| FOR_ITER_LIST | 7,681,240 | 0.5% | 95.9% |  |
| NOP | 7,043,920 | 0.4% | 96.3% |  |
| DELETE_SUBSCR | 7,041,280 | 0.4% | 96.8% |  |
| JUMP_BACKWARD | 7,041,280 | 0.4% | 97.2% |  |
| COMPARE_OP_INT | 7,040,020 | 0.4% | 97.6% |  |
| BINARY_OP_SUBTRACT_INT | 7,039,960 | 0.4% | 98.0% |  |
| BINARY_OP | 6,401,960 | 0.4% | 98.4% |  |
| LOAD_DEREF | 6,400,160 | 0.4% | 98.8% |  |
| BINARY_OP_ADD_INT | 6,399,980 | 0.4% | 99.2% |  |
| BINARY_OP_ADD_UNICODE | 6,399,980 | 0.4% | 99.5% |  |
| INTERPRETER_EXIT | 1,287,760 | 0.1% | 99.6% |  |
| STORE_ATTR_SLOT | 1,285,040 | 0.1% | 99.7% |  |
| EXTENDED_ARG | 1,281,280 | 0.1% | 99.8% |  |
| RETURN_CONST | 645,120 | 0.0% | 99.8% |  |
| BUILD_TUPLE | 643,840 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 642,580 | 0.0% | 99.9% |  |
| GET_ITER | 641,360 | 0.0% | 99.9% |  |
| CALL_LEN | 641,260 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 641,240 | 0.0% | 100.0% |  |
| LOAD_ATTR | 14,160 | 0.0% | 100.0% |  |
| BUILD_MAP | 5,120 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 5,040 | 0.0% | 100.0% |  |
| MAKE_CELL | 3,840 | 0.0% | 100.0% |  |
| STORE_DEREF | 3,840 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 2,640 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 2,560 | 0.0% | 100.0% |  |
| DICT_MERGE | 2,560 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 2,560 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 2,520 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,520 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 1,720 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 1,340 | 0.0% | 100.0% |  |
| CALL_KW | 1,280 | 0.0% | 100.0% |  |
| CONTAINS_OP | 1,280 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 1,260 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 1,260 | 0.0% | 100.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,260 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,260 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 1,260 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 1,260 | 0.0% | 100.0% |  |
| RESUME | 240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 200 | 0.0% | 100.0% |  |
| STORE_ATTR | 160 | 0.0% | 100.0% |  |
| TO_BOOL | 120 | 0.0% | 100.0% |  |
| COMPARE_OP | 120 | 0.0% | 100.0% |  |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST | 131,869,760 | 7.8% | 7.8% |
| LOAD_FAST PUSH_NULL | 92,812,960 | 5.5% | 13.4% |
| PUSH_NULL LOAD_CONST | 74,255,360 | 4.4% | 17.8% |
| IS_OP POP_JUMP_IF_FALSE | 59,528,960 | 3.5% | 21.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 59,528,960 | 3.5% | 24.8% |
| CALL_BUILTIN_O POP_TOP | 52,481,020 | 3.1% | 28.0% |
| LOAD_FAST LOAD_CONST | 48,009,040 | 2.9% | 30.8% |
| LOAD_CONST CALL_BUILTIN_O | 39,680,840 | 2.4% | 33.2% |
| LOAD_GLOBAL_BUILTIN IS_OP | 38,399,900 | 2.3% | 35.5% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 38,399,800 | 2.3% | 37.7% |
| LOAD_FAST RETURN_VALUE | 33,287,760 | 2.0% | 39.7% |
| LOAD_CONST LOAD_CONST | 32,001,280 | 1.9% | 41.6% |
| LOAD_GLOBAL_MODULE IS_OP | 27,528,880 | 1.6% | 43.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 27,528,800 | 1.6% | 44.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 27,523,780 | 1.6% | 46.5% |
| STORE_FAST LOAD_CONST | 26,883,840 | 1.6% | 48.1% |
| POP_TOP LOAD_FAST | 26,246,400 | 1.6% | 49.7% |
| LOAD_GLOBAL_MODULE STORE_FAST | 26,244,940 | 1.6% | 51.3% |
| PUSH_NULL LOAD_FAST | 25,600,080 | 1.5% | 52.8% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 20,490,180 | 1.2% | 54.0% |
| LOAD_ATTR_CLASS LOAD_FAST_LOAD_FAST | 20,487,660 | 1.2% | 55.2% |
| LOAD_FAST_LOAD_FAST LOAD_GLOBAL_MODULE | 20,487,640 | 1.2% | 56.4% |
| LOAD_GLOBAL_BUILTIN LOAD_ATTR_CLASS | 20,487,640 | 1.2% | 57.6% |
| LOAD_GLOBAL_MODULE CALL_METHOD_DESCRIPTOR_FAST | 20,487,640 | 1.2% | 58.9% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 20,487,640 | 1.2% | 60.1% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 20,482,420 | 1.2% | 61.3% |
| LOAD_CONST CALL_BOUND_METHOD_EXACT_ARGS | 20,482,280 | 1.2% | 62.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 19,845,120 | 1.2% | 63.7% |
| LOAD_CONST STORE_FAST | 19,843,840 | 1.2% | 64.9% |
| LOAD_FAST LOAD_FAST | 19,843,840 | 1.2% | 66.1% |
| POP_TOP LOAD_GLOBAL_MODULE | 19,842,320 | 1.2% | 67.2% |
| RETURN_VALUE STORE_FAST | 19,202,520 | 1.1% | 68.4% |
| IS_OP POP_JUMP_IF_TRUE | 19,200,000 | 1.1% | 69.5% |
| POP_JUMP_IF_TRUE LOAD_FAST | 19,198,720 | 1.1% | 70.7% |
| LOAD_CONST STORE_SUBSCR | 14,081,320 | 0.8% | 71.5% |
| STORE_SUBSCR LOAD_FAST | 14,081,280 | 0.8% | 72.3% |
| RESUME_CHECK LOAD_FAST | 13,447,540 | 0.8% | 73.1% |
| LOAD_CONST LOAD_GLOBAL_MODULE | 13,442,360 | 0.8% | 73.9% |
| COPY_FREE_VARS RESUME_CHECK | 12,801,300 | 0.8% | 74.7% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 12,801,280 | 0.8% | 75.5% |
| POP_JUMP_IF_NONE LOAD_FAST | 12,801,280 | 0.8% | 76.2% |
| IS_OP STORE_FAST | 12,800,000 | 0.8% | 77.0% |
| LOAD_FAST STORE_FAST | 12,800,000 | 0.8% | 77.7% |
| LOAD_FAST_LOAD_FAST IS_OP | 12,800,000 | 0.8% | 78.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 12,800,000 | 0.8% | 79.3% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 12,800,000 | 0.8% | 80.0% |
| CALL_TYPE_1 STORE_FAST | 12,799,980 | 0.8% | 80.8% |
| LOAD_FAST CALL_TYPE_1 | 12,799,960 | 0.8% | 81.5% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 12,799,960 | 0.8% | 82.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 12,799,960 | 0.8% | 83.1% |
| LOAD_FAST TO_BOOL_BOOL | 12,799,920 | 0.8% | 83.8% |
| LOAD_CONST LOAD_FAST | 7,687,680 | 0.5% | 84.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 7,684,880 | 0.5% | 84.7% |
| CALL_BUILTIN_FAST STORE_FAST | 7,682,480 | 0.5% | 85.2% |
| LOAD_FAST CALL | 7,043,000 | 0.4% | 85.6% |
| DELETE_SUBSCR JUMP_FORWARD | 7,041,280 | 0.4% | 86.0% |
| RETURN_VALUE LOAD_CONST | 7,041,280 | 0.4% | 86.5% |
| JUMP_FORWARD LOAD_FAST | 7,041,280 | 0.4% | 86.9% |
| LOAD_CONST DELETE_SUBSCR | 7,041,280 | 0.4% | 87.3% |
| LOAD_GLOBAL_MODULE CALL_BUILTIN_FAST | 7,041,160 | 0.4% | 87.7% |
| LOAD_CONST COMPARE_OP_INT | 7,039,960 | 0.4% | 88.1% |
| BINARY_OP_SUBTRACT_INT STORE_FAST | 7,039,960 | 0.4% | 88.5% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 7,039,960 | 0.4% | 89.0% |
| FOR_ITER_LIST STORE_FAST | 7,039,960 | 0.4% | 89.4% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 7,039,920 | 0.4% | 89.8% |
| LOAD_CONST CALL_PY_EXACT_ARGS | 7,039,920 | 0.4% | 90.2% |
| LOAD_FAST CALL_BUILTIN_O | 6,401,240 | 0.4% | 90.6% |
| NOP LOAD_DEREF | 6,400,080 | 0.4% | 91.0% |
| LOAD_DEREF PUSH_NULL | 6,400,080 | 0.4% | 91.4% |
| LOAD_FAST BINARY_OP | 6,400,040 | 0.4% | 91.7% |
| CALL LOAD_CONST | 6,400,000 | 0.4% | 92.1% |
| LOAD_CONST IS_OP | 6,400,000 | 0.4% | 92.5% |
| LOAD_FAST IS_OP | 6,400,000 | 0.4% | 92.9% |
| POP_JUMP_IF_NONE NOP | 6,400,000 | 0.4% | 93.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 6,399,980 | 0.4% | 93.6% |
| BINARY_OP_ADD_INT STORE_FAST | 6,399,980 | 0.4% | 94.0% |
| BINARY_OP_ADD_UNICODE STORE_FAST | 6,399,980 | 0.4% | 94.4% |
| CALL_STR_1 STORE_FAST | 6,399,980 | 0.4% | 94.8% |
| RETURN_VALUE CALL_STR_1 | 6,399,960 | 0.4% | 95.2% |
| BINARY_OP CALL_BUILTIN_O | 6,399,960 | 0.4% | 95.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 6,399,960 | 0.4% | 95.9% |
| LOAD_CONST LOAD_GLOBAL_BUILTIN | 6,399,960 | 0.4% | 96.3% |
| LOAD_FAST CALL_STR_1 | 6,399,960 | 0.4% | 96.7% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_BUILTIN | 6,399,960 | 0.4% | 97.1% |
| CALL_STR_1 BINARY_OP_ADD_UNICODE | 6,399,960 | 0.4% | 97.5% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 6,399,960 | 0.4% | 97.8% |
| POP_TOP JUMP_BACKWARD | 5,761,280 | 0.3% | 98.2% |
| CACHE RESUME_CHECK | 1,286,360 | 0.1% | 98.3% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 1,282,480 | 0.1% | 98.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 1,282,480 | 0.1% | 98.4% |
| RETURN_VALUE PUSH_NULL | 1,281,280 | 0.1% | 98.5% |
| RETURN_VALUE INTERPRETER_EXIT | 645,200 | 0.0% | 98.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 645,040 | 0.0% | 98.6% |
| LOAD_FAST CALL_BUILTIN_FAST | 643,720 | 0.0% | 98.6% |
| RETURN_CONST INTERPRETER_EXIT | 642,560 | 0.0% | 98.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 642,520 | 0.0% | 98.7% |
| STORE_ATTR_SLOT RETURN_CONST | 642,520 | 0.0% | 98.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 642,500 | 0.0% | 98.7% |
| CALL STORE_FAST | 641,600 | 0.0% | 98.8% |
| PUSH_NULL CALL | 641,520 | 0.0% | 98.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,286,360 | 99.9% |
| COPY_FREE_VARS | 1,280 | 0.1% |
| RESUME | 120 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_GETITEM | 80 | 40.0% |
| STORE_FAST | 60 | 30.0% |
| STORE_DEREF | 40 | 20.0% |
| BINARY_SUBSCR_DICT | 20 | 10.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,041,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 7,041,280 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 639,980 | 99.8% |
| EXTENDED_ARG | 1,280 | 0.2% |
| FOR_ITER_RANGE | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 645,200 | 50.1% |
| RETURN_CONST | 642,560 | 49.9% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 2,560 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 6,400,000 | 90.9% |
| RESUME_CHECK | 641,260 | 9.1% |
| STORE_FAST | 2,560 | 0.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 6,400,080 | 90.9% |
| LOAD_GLOBAL_BUILTIN | 639,960 | 9.1% |
| LOAD_FAST | 2,560 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,280 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 52,481,020 | 100.0% |
| CALL_BUILTIN_FAST | 6,300 | 0.0% |
| RETURN_CONST | 2,560 | 0.0% |
| CALL | 1,720 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,246,400 | 50.0% |
| LOAD_GLOBAL_MODULE | 19,842,320 | 37.8% |
| JUMP_BACKWARD | 5,761,280 | 11.0% |
| EXTENDED_ARG | 638,720 | 1.2% |
| LOAD_CONST | 1,280 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,812,960 | 92.4% |
| LOAD_DEREF | 6,400,080 | 6.4% |
| RETURN_VALUE | 1,281,280 | 1.3% |
| LOAD_ATTR | 1,300 | 0.0% |
| LOAD_SUPER_ATTR_ATTR | 1,260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 74,255,360 | 73.9% |
| LOAD_FAST | 25,600,080 | 25.5% |
| CALL | 641,520 | 0.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,287,760 | 96.3% |
| BUILD_TUPLE | 641,280 | 1.9% |
| CALL_BUILTIN_FAST | 639,980 | 1.9% |
| CALL_FUNCTION_EX | 2,560 | 0.0% |
| RETURN_VALUE | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 19,202,520 | 55.5% |
| LOAD_CONST | 7,041,280 | 20.4% |
| CALL_STR_1 | 6,399,960 | 18.5% |
| PUSH_NULL | 1,281,280 | 3.7% |
| INTERPRETER_EXIT | 645,200 | 1.9% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 14,081,320 | 95.6% |
| LOAD_FAST_LOAD_FAST | 641,280 | 4.4% |
| STORE_SUBSCR | 4,640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,081,280 | 95.6% |
| LOAD_FAST_LOAD_FAST | 641,280 | 4.4% |
| STORE_SUBSCR | 4,640 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |
| STORE_SUBSCR_DICT | 20 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 66.7% |
| LOAD_ATTR | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 60 | 50.0% |
| POP_JUMP_IF_FALSE | 40 | 33.3% |
| POP_JUMP_IF_TRUE | 20 | 16.7% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,400,040 | 100.0% |
| BINARY_OP | 1,760 | 0.0% |
| LOAD_CONST | 120 | 0.0% |
| CALL | 20 | 0.0% |
| CALL_STR_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 6,399,960 | 100.0% |
| BINARY_OP | 1,760 | 0.0% |
| STORE_FAST | 100 | 0.0% |
| CALL | 40 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 40 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 50.0% |
| STORE_FAST | 1,280 | 25.0% |
| LOAD_GLOBAL_MODULE | 1,260 | 24.6% |
| LOAD_GLOBAL | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 50.0% |
| CALL | 1,280 | 25.0% |
| STORE_FAST | 1,280 | 25.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 641,280 | 99.6% |
| LOAD_FAST | 2,560 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 641,280 | 99.6% |
| LOAD_CONST | 2,560 | 0.4% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,043,000 | 84.5% |
| PUSH_NULL | 641,520 | 7.7% |
| LOAD_FAST_LOAD_FAST | 641,320 | 7.7% |
| CALL | 3,240 | 0.0% |
| BUILD_MAP | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,400,000 | 76.8% |
| STORE_FAST | 641,600 | 7.7% |
| LOAD_FAST_LOAD_FAST | 641,280 | 7.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 641,200 | 7.7% |
| CALL | 3,240 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 2,560 | 97.0% |
| LOAD_FAST | 80 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,560 | 97.0% |
| COPY_FREE_VARS | 80 | 3.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 1,240 | 96.9% |
| CALL | 40 | 3.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 60 | 50.0% |
| POP_JUMP_IF_TRUE | 40 | 33.3% |
| POP_JUMP_IF_FALSE | 20 | 16.7% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,280 | 100.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 12,799,960 | 100.0% |
| CACHE | 1,280 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,801,300 | 100.0% |
| RESUME | 60 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 2,560 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 640,000 | 50.0% |
| POP_TOP | 638,720 | 49.9% |
| GET_ITER | 1,280 | 0.1% |
| POP_JUMP_IF_TRUE | 1,280 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 641,240 | 50.0% |
| JUMP_BACKWARD | 640,000 | 50.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40 | 33.3% |
| EXTENDED_ARG | 40 | 33.3% |
| JUMP_BACKWARD | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 50.0% |
| FOR_ITER_LIST | 40 | 33.3% |
| FOR_ITER_RANGE | 20 | 16.7% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 38,399,900 | 42.0% |
| LOAD_GLOBAL_MODULE | 27,528,880 | 30.1% |
| LOAD_FAST_LOAD_FAST | 12,800,000 | 14.0% |
| LOAD_CONST | 6,400,000 | 7.0% |
| LOAD_FAST | 6,400,000 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 59,528,960 | 65.0% |
| POP_JUMP_IF_TRUE | 19,200,000 | 21.0% |
| STORE_FAST | 12,800,000 | 14.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,761,280 | 81.8% |
| EXTENDED_ARG | 640,000 | 9.1% |
| POP_JUMP_IF_TRUE | 640,000 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 6,399,980 | 90.9% |
| EXTENDED_ARG | 640,000 | 9.1% |
| FOR_ITER_RANGE | 1,260 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 7,041,280 | 91.7% |
| CALL_BUILTIN_CLASS | 641,260 | 8.3% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,041,280 | 91.7% |
| STORE_FAST | 641,280 | 8.3% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,040 | 92.1% |
| LOAD_ATTR | 1,000 | 7.1% |
| LOAD_GLOBAL | 60 | 0.4% |
| LOAD_GLOBAL_MODULE | 40 | 0.3% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,440 | 45.5% |
| LOAD_FAST | 2,560 | 18.1% |
| PUSH_NULL | 1,300 | 9.2% |
| CALL_BUILTIN_CLASS | 1,240 | 8.8% |
| TO_BOOL_BOOL | 1,240 | 8.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 74,255,360 | 38.2% |
| LOAD_FAST | 48,009,040 | 24.7% |
| LOAD_CONST | 32,001,280 | 16.4% |
| STORE_FAST | 26,883,840 | 13.8% |
| RETURN_VALUE | 7,041,280 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 39,680,840 | 20.4% |
| LOAD_CONST | 32,001,280 | 16.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 20,482,280 | 10.5% |
| STORE_FAST | 19,843,840 | 10.2% |
| STORE_SUBSCR | 14,081,320 | 7.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 6,400,080 | 100.0% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 6,400,080 | 100.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 131,869,760 | 36.0% |
| POP_JUMP_IF_FALSE | 59,528,960 | 16.3% |
| LOAD_GLOBAL_BUILTIN | 27,523,780 | 7.5% |
| POP_TOP | 26,246,400 | 7.2% |
| PUSH_NULL | 25,600,080 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 92,812,960 | 25.3% |
| LOAD_CONST | 48,009,040 | 13.1% |
| LOAD_GLOBAL_BUILTIN | 38,399,800 | 10.5% |
| RETURN_VALUE | 33,287,760 | 9.1% |
| LOAD_GLOBAL_MODULE | 27,528,800 | 7.5% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_CLASS | 20,487,660 | 55.2% |
| POP_JUMP_IF_NOT_NONE | 12,800,000 | 34.5% |
| LOAD_GLOBAL_MODULE | 642,520 | 1.7% |
| STORE_SUBSCR | 641,280 | 1.7% |
| CALL | 641,280 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20,487,640 | 55.2% |
| IS_OP | 12,800,000 | 34.5% |
| STORE_ATTR_SLOT | 1,282,480 | 3.5% |
| CALL | 641,320 | 1.7% |
| STORE_SUBSCR | 641,280 | 1.7% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 20.9% |
| STORE_FAST | 320 | 18.6% |
| POP_TOP | 240 | 14.0% |
| LOAD_CONST | 240 | 14.0% |
| POP_JUMP_IF_FALSE | 120 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 560 | 32.6% |
| LOAD_GLOBAL_BUILTIN | 300 | 17.4% |
| LOAD_FAST | 220 | 12.8% |
| IS_OP | 180 | 10.5% |
| STORE_FAST | 180 | 10.5% |


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
| MAKE_CELL | 2,560 | 66.7% |
| CALL_PY_WITH_DEFAULTS | 1,260 | 32.8% |
| CALL | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,560 | 66.7% |
| RESUME_CHECK | 1,260 | 32.8% |
| RESUME | 20 | 0.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 59,528,960 | 82.3% |
| TO_BOOL_BOOL | 12,799,960 | 17.7% |
| CONTAINS_OP | 1,280 | 0.0% |
| COMPARE_OP_INT | 60 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,528,960 | 82.3% |
| LOAD_GLOBAL_BUILTIN | 12,800,000 | 17.7% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.0% |
| LOAD_GLOBAL | 120 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,845,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,801,280 | 64.5% |
| NOP | 6,400,000 | 32.2% |
| LOAD_GLOBAL_BUILTIN | 641,240 | 3.2% |
| LOAD_CONST | 1,280 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,801,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,800,000 | 100.0% |
| LOAD_FAST | 1,280 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 19,200,000 | 73.2% |
| COMPARE_OP_INT | 7,039,960 | 26.8% |
| TO_BOOL_BOOL | 1,260 | 0.0% |
| COMPARE_OP | 40 | 0.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,198,720 | 73.2% |
| LOAD_GLOBAL_BUILTIN | 6,399,960 | 24.4% |
| JUMP_BACKWARD | 640,000 | 2.4% |
| EXTENDED_ARG | 1,280 | 0.0% |
| RETURN_CONST | 1,280 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 642,520 | 99.6% |
| POP_TOP | 1,280 | 0.2% |
| POP_JUMP_IF_TRUE | 1,280 | 0.2% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 642,560 | 99.6% |
| POP_TOP | 2,560 | 0.4% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,560 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| LOAD_FAST_LOAD_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 80 | 50.0% |
| RETURN_CONST | 40 | 25.0% |
| LOAD_FAST | 20 | 12.5% |
| LOAD_FAST_LOAD_FAST | 20 | 12.5% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,520 | 65.6% |
| LOAD_GLOBAL_MODULE | 1,260 | 32.8% |
| BINARY_SUBSCR | 40 | 1.0% |
| LOAD_GLOBAL | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,840 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 26,244,940 | 15.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 20,490,180 | 12.2% |
| LOAD_CONST | 19,843,840 | 11.8% |
| RETURN_VALUE | 19,202,520 | 11.4% |
| IS_OP | 12,800,000 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 131,869,760 | 78.3% |
| LOAD_CONST | 26,883,840 | 16.0% |
| LOAD_GLOBAL_MODULE | 7,684,880 | 4.6% |
| LOAD_GLOBAL_BUILTIN | 1,282,480 | 0.8% |
| STORE_FAST | 641,280 | 0.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 40 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 120 | 50.0% |
| COPY_FREE_VARS | 60 | 25.0% |
| CALL | 40 | 16.7% |
| MAKE_CELL | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 58.3% |
| LOAD_GLOBAL | 60 | 25.0% |
| NOP | 20 | 8.3% |
| LOAD_FAST_LOAD_FAST | 20 | 8.3% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,399,960 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,399,980 | 100.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_STR_1 | 6,399,960 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,399,980 | 100.0% |


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
| LOAD_CONST | 7,039,920 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,039,960 | 100.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 98.4% |
| BINARY_SUBSCR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,260 | 100.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,960 | 98.4% |
| BINARY_SUBSCR | 80 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,040 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,482,280 | 100.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,482,420 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,280 | 99.8% |
| LOAD_ATTR | 1,240 | 0.2% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 641,260 | 99.8% |
| STORE_FAST | 1,320 | 0.2% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,041,160 | 84.5% |
| LOAD_FAST | 643,720 | 7.7% |
| LOAD_FAST_LOAD_FAST | 639,960 | 7.7% |
| CALL_KW | 1,240 | 0.0% |
| LOAD_CONST | 1,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,682,480 | 92.2% |
| RETURN_VALUE | 639,980 | 7.7% |
| POP_TOP | 6,300 | 0.1% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,680,840 | 75.6% |
| LOAD_FAST | 6,401,240 | 12.2% |
| BINARY_OP | 6,399,960 | 12.2% |
| CALL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 52,481,020 | 100.0% |
| RETURN_VALUE | 1,280 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,240 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 641,260 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20,487,640 | 98.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 393,980 | 1.9% |
| LOAD_CONST | 2,480 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,490,180 | 98.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 393,980 | 1.9% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,039,920 | 52.4% |
| LOAD_GLOBAL_MODULE | 6,399,960 | 47.6% |
| LOAD_FAST | 1,240 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,240 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 12,799,960 | 95.2% |
| RESUME_CHECK | 642,500 | 4.8% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 98.4% |
| CALL | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 1,260 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 6,399,960 | 50.0% |
| LOAD_FAST | 6,399,960 | 50.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,399,980 | 50.0% |
| BINARY_OP_ADD_UNICODE | 6,399,960 | 50.0% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,799,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,799,980 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,039,960 | 100.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 7,039,960 | 100.0% |
| POP_JUMP_IF_FALSE | 60 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,399,980 | 83.3% |
| EXTENDED_ARG | 641,240 | 8.3% |
| GET_ITER | 639,980 | 8.3% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,039,960 | 91.7% |
| LOAD_FAST | 641,280 | 8.3% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,260 | 94.0% |
| GET_ITER | 60 | 4.5% |
| FOR_ITER | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,260 | 94.0% |
| LOAD_FAST | 80 | 6.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 20,487,640 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 20,487,660 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 98.4% |
| LOAD_ATTR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,260 | 100.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,480 | 98.4% |
| LOAD_ATTR | 40 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,520 | 100.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 98.4% |
| LOAD_ATTR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,240 | 98.4% |
| CALL | 20 | 1.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 66.7% |
| LOAD_ATTR | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 50.0% |
| STORE_FAST | 60 | 50.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,480 | 98.4% |
| LOAD_ATTR | 40 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,260 | 50.0% |
| CALL_BUILTIN_FAST | 1,240 | 49.2% |
| CALL | 20 | 0.8% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,399,800 | 44.1% |
| RESUME_CHECK | 20,487,640 | 23.5% |
| POP_JUMP_IF_FALSE | 12,800,000 | 14.7% |
| LOAD_CONST | 6,399,960 | 7.4% |
| POP_JUMP_IF_TRUE | 6,399,960 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 38,399,900 | 44.1% |
| LOAD_FAST | 27,523,780 | 31.6% |
| LOAD_ATTR_CLASS | 20,487,640 | 23.5% |
| LOAD_FAST_LOAD_FAST | 639,980 | 0.7% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,528,800 | 30.9% |
| LOAD_FAST_LOAD_FAST | 20,487,640 | 23.0% |
| POP_TOP | 19,842,320 | 22.3% |
| LOAD_CONST | 13,442,360 | 15.1% |
| STORE_FAST | 7,684,880 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 27,528,880 | 30.9% |
| STORE_FAST | 26,244,940 | 29.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 20,487,640 | 23.0% |
| CALL_BUILTIN_FAST | 7,041,160 | 7.9% |
| CALL_PY_EXACT_ARGS | 6,399,960 | 7.2% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 98.4% |
| LOAD_SUPER_ATTR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,260 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 20,482,420 | 58.2% |
| COPY_FREE_VARS | 12,801,300 | 36.3% |
| CACHE | 1,286,360 | 3.7% |
| CALL_PY_EXACT_ARGS | 642,500 | 1.8% |
| BINARY_SUBSCR_GETITEM | 5,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 20,487,640 | 58.2% |
| LOAD_FAST | 13,447,540 | 38.2% |
| NOP | 641,260 | 1.8% |
| LOAD_FAST_LOAD_FAST | 641,260 | 1.8% |
| LOAD_GLOBAL_MODULE | 1,280 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,282,480 | 99.8% |
| LOAD_FAST | 2,480 | 0.2% |
| STORE_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 642,520 | 50.0% |
| LOAD_FAST_LOAD_FAST | 641,260 | 49.9% |
| LOAD_FAST | 1,260 | 0.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 98.4% |
| STORE_SUBSCR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,240 | 98.4% |
| LOAD_GLOBAL | 20 | 1.6% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,799,920 | 100.0% |
| LOAD_ATTR | 1,240 | 0.0% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,799,960 | 100.0% |
| POP_JUMP_IF_TRUE | 1,260 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 641,200 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 641,240 | 100.0% |


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
|     deferred | 6,400,100 | 24.4% |
|          hit | 19,839,980 | 75.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 5.4% |
| Failure | 1,760 | 94.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| remainder | 1,760 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 1.5% |
|          hit | 6,300 | 96.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 28,815,220 | 16.8% |
|          hit | 142,105,920 | 82.9% |
|         miss | 20,881,640 | 12.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 394,900 | 99.2% |
| Failure | 3,240 | 0.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cmethod | 1,760 | 54.3% |
| other | 540 | 16.7% |
| no dict | 440 | 13.6% |
| cfunc noargs | 400 | 12.3% |
| class mutable | 100 | 3.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 7,040,020 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 7,682,580 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,980 | 0.1% |
|          hit | 20,495,340 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 15.3% |
| Failure | 1,000 | 84.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 700 | 70.0% |
| shadowed | 100 | 10.0% |
| class attr simple | 100 | 10.0% |
| class attr descriptor | 100 | 10.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 860 | 0.0% |
|          hit | 176,045,460 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 860 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 1.5% |
|          hit | 1,260 | 96.9% |

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
|     deferred | 80 | 0.0% |
|          hit | 1,285,040 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 14,722,580 | 100.0% |
|          hit | 1,260 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 0.4% |
| Failure | 4,640 | 99.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict subclass no override | 4,300 | 92.7% |
| other | 340 | 7.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 12,801,220 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 641,240 | 100.0% |

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
| Basic | 1,097,904,480 | 65.3% |
| Not specialized | 160,695,640 | 9.6% |
| Specialized hits | 402,682,240 | 23.9% |
| Specialized misses | 20,881,640 | 1.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 28,815,220 | 57.7% |
| STORE_SUBSCR | 14,722,580 | 29.5% |
| BINARY_OP | 6,400,100 | 12.8% |
| LOAD_ATTR | 12,980 | 0.0% |
| LOAD_GLOBAL | 860 | 0.0% |
| BINARY_SUBSCR | 100 | 0.0% |
| STORE_ATTR | 80 | 0.0% |
| TO_BOOL | 60 | 0.0% |
| COMPARE_OP | 60 | 0.0% |
| FOR_ITER | 60 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 20,881,640 | 100.0% |
| CACHE | 0 | 0.0% |
| DELETE_SUBSCR | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| MAKE_FUNCTION | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |
| RETURN_VALUE | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,287,760 | 3.7% |
| Calls to Python functions inlined | 33,931,520 | 96.3% |
| Calls via PyEval_EvalFrame (total) | 1,287,760 | 3.7% |
| Calls via PyEval_EvalFrame (vector) | 1,287,760 | 3.7% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 1,287,760 | 3.7% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 33,931,180 | 96.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 2,593,480 | 4.9% |
| Frees to freelist | 2,593,540 |  |
| Allocations | 50,214,640 | 95.1% |
| Allocations to 512 bytes | 50,212,080 | 95.1% |
| Allocations to 4 kbytes | 1,280 | 0.0% |
| Allocations over 4 kbytes | 1,280 | 0.0% |
| Frees | 50,215,889 |  |
| New values | 0 |  |
| Interpreter increfs | 533,332,260 | 88.2% |
| Interpreter decrefs | 571,439,780 | 88.0% |
| Increfs | 71,165,508 | 11.8% |
| Decrefs | 78,224,541 | 12.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 20 | 20 / 0 !! |
| Method cache hits | 649,731 |  |
| Method cache misses | 369 |  |
| Method cache collisions | 522 |  |
| Method cache dunder hits | 1,930,943 |  |
| Method cache dunder misses | 177 |  |


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
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
