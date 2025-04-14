
# Pystats results

- benchmark: comprehensions
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 266,740,720 | 13.9% | 13.9% |  |
| FOR_ITER_LIST | 184,169,120 | 9.6% | 23.5% |  |
| JUMP_BACKWARD | 157,956,320 | 8.2% | 31.8% |  |
| STORE_FAST_LOAD_FAST | 144,845,040 | 7.6% | 39.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 137,635,820 | 7.2% | 46.5% |  |
| LIST_APPEND | 106,178,800 | 5.5% | 52.1% |  |
| LOAD_ATTR_METHOD_NO_DICT | 71,436,100 | 3.7% | 55.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 70,778,860 | 3.7% | 59.5% |  |
| RESUME_CHECK | 48,499,560 | 2.5% | 62.0% |  |
| STORE_FAST | 43,264,000 | 2.3% | 64.3% |  |
| SWAP | 42,602,240 | 2.2% | 66.5% |  |
| CALL_PY_EXACT_ARGS | 39,977,180 | 2.1% | 68.6% |  |
| BINARY_SUBSCR_DICT | 35,389,860 | 1.8% | 70.4% |  |
| POP_JUMP_IF_TRUE | 34,734,160 | 1.8% | 72.2% |  |
| POP_JUMP_IF_FALSE | 32,112,640 | 1.7% | 73.9% |  |
| TO_BOOL_BOOL | 31,457,240 | 1.6% | 75.6% |  |
| POP_TOP | 28,836,660 | 1.5% | 77.1% |  |
| RETURN_VALUE | 28,182,840 | 1.5% | 78.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 28,180,420 | 1.5% | 80.0% |  |
| GET_ITER | 26,873,760 | 1.4% | 81.4% |  |
| LOAD_CONST | 24,913,280 | 1.3% | 82.7% |  |
| LOAD_FAST_LOAD_FAST | 24,265,600 | 1.3% | 84.0% |  |
| LOAD_GLOBAL_BUILTIN | 24,248,440 | 1.3% | 85.2% |  |
| MAP_ADD | 23,592,960 | 1.2% | 86.5% |  |
| INTERPRETER_EXIT | 19,661,100 | 1.0% | 87.5% |  |
| TO_BOOL_ALWAYS_TRUE | 19,169,200 | 1.0% | 88.5% | 45.3% |
| YIELD_VALUE | 19,005,920 | 1.0% | 89.5% |  |
| LOAD_GLOBAL_MODULE | 16,386,320 | 0.9% | 90.3% |  |
| TO_BOOL_NONE | 15,892,520 | 0.8% | 91.2% | 54.6% |
| LOAD_ATTR | 15,734,300 | 0.8% | 92.0% |  |
| COMPARE_OP | 15,732,800 | 0.8% | 92.8% |  |
| LOAD_FAST_AND_CLEAR | 15,730,560 | 0.8% | 93.6% |  |
| COPY | 15,728,640 | 0.8% | 94.5% |  |
| BUILD_LIST | 14,420,000 | 0.8% | 95.2% |  |
| CALL_LEN | 12,451,860 | 0.6% | 95.9% |  |
| COMPARE_OP_INT | 12,451,860 | 0.6% | 96.5% |  |
| BINARY_SUBSCR | 11,801,700 | 0.6% | 97.1% |  |
| MAKE_FUNCTION | 11,796,720 | 0.6% | 97.7% |  |
| RETURN_GENERATOR | 11,796,720 | 0.6% | 98.4% |  |
| BUILD_TUPLE | 11,796,720 | 0.6% | 99.0% |  |
| CALL_BUILTIN_O | 11,796,460 | 0.6% | 99.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 1,977,420 | 0.1% | 99.7% |  |
| RETURN_CONST | 1,968,240 | 0.1% | 99.8% |  |
| BUILD_MAP | 1,310,720 | 0.1% | 99.9% |  |
| EXIT_INIT_CHECK | 657,240 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 657,240 | 0.0% | 99.9% |  |
| FOR_ITER_RANGE | 655,720 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,340 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 4,280 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_INT | 3,800 | 0.0% | 100.0% |  |
| BUILD_SLICE | 1,920 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 1,900 | 0.0% | 100.0% |  |
| LOAD_DEREF | 960 | 0.0% | 100.0% |  |
| CALL | 940 | 0.0% | 100.0% |  |
| FOR_ITER_GEN | 700 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 560 | 0.0% | 100.0% |  |
| FOR_ITER | 520 | 0.0% | 100.0% |  |
| PUSH_NULL | 400 | 0.0% | 100.0% |  |
| STORE_ATTR | 360 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 320 | 0.0% | 100.0% |  |
| END_FOR | 240 | 0.0% | 100.0% |  |
| MAKE_CELL | 240 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 240 | 0.0% | 100.0% |  |
| RESUME | 200 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 180 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| TO_BOOL | 120 | 0.0% | 100.0% |  |
| BINARY_OP | 120 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| JUMP_BACKWARD FOR_ITER_LIST | 157,297,220 | 8.2% | 8.2% |
| FOR_ITER_LIST STORE_FAST_LOAD_FAST | 144,844,940 | 7.6% | 15.8% |
| LIST_APPEND JUMP_BACKWARD | 106,178,800 | 5.5% | 21.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 102,235,800 | 5.3% | 26.6% |
| CALL_METHOD_DESCRIPTOR_FAST LIST_APPEND | 70,778,860 | 3.7% | 30.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 70,778,860 | 3.7% | 34.0% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 70,778,840 | 3.7% | 37.7% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 70,778,840 | 3.7% | 41.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 35,389,380 | 1.8% | 43.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 31,457,240 | 1.6% | 44.9% |
| RESUME_CHECK LOAD_FAST | 28,180,900 | 1.5% | 46.4% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 28,180,480 | 1.5% | 47.9% |
| STORE_FAST LOAD_FAST | 26,873,680 | 1.4% | 49.3% |
| FOR_ITER_LIST STORE_FAST | 26,216,740 | 1.4% | 50.6% |
| MAP_ADD JUMP_BACKWARD | 23,592,960 | 1.2% | 51.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 23,592,880 | 1.2% | 53.1% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_SUBSCR_DICT | 23,592,880 | 1.2% | 54.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 19,005,520 | 1.0% | 55.3% |
| YIELD_VALUE INTERPRETER_EXIT | 19,005,460 | 1.0% | 56.3% |
| LOAD_ATTR_INSTANCE_VALUE YIELD_VALUE | 19,005,420 | 1.0% | 57.3% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 19,005,380 | 1.0% | 58.3% |
| STORE_FAST_LOAD_FAST TO_BOOL_ALWAYS_TRUE | 19,005,360 | 1.0% | 59.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 16,383,960 | 0.9% | 60.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 16,383,920 | 0.9% | 61.0% |
| STORE_FAST_LOAD_FAST TO_BOOL_NONE | 15,728,680 | 0.8% | 61.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 15,728,680 | 0.8% | 62.6% |
| TO_BOOL_NONE POP_JUMP_IF_TRUE | 15,728,680 | 0.8% | 63.4% |
| LOAD_ATTR COMPARE_OP | 15,728,660 | 0.8% | 64.3% |
| COMPARE_OP COPY | 15,728,640 | 0.8% | 65.1% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 15,728,640 | 0.8% | 65.9% |
| RETURN_VALUE TO_BOOL_BOOL | 15,728,600 | 0.8% | 66.7% |
| COPY TO_BOOL_BOOL | 15,728,600 | 0.8% | 67.6% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 15,728,600 | 0.8% | 68.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 15,728,600 | 0.8% | 69.2% |
| GET_ITER LOAD_FAST_AND_CLEAR | 15,075,200 | 0.8% | 70.0% |
| LOAD_FAST_AND_CLEAR SWAP | 15,075,200 | 0.8% | 70.8% |
| SWAP FOR_ITER_LIST | 15,075,040 | 0.8% | 71.6% |
| LOAD_FAST GET_ITER | 15,073,360 | 0.8% | 72.3% |
| BUILD_LIST SWAP | 13,764,480 | 0.7% | 73.1% |
| SWAP BUILD_LIST | 13,764,480 | 0.7% | 73.8% |
| SWAP STORE_FAST | 12,451,840 | 0.6% | 74.4% |
| FOR_ITER_LIST SWAP | 12,451,840 | 0.6% | 75.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 12,451,760 | 0.6% | 75.7% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 11,806,880 | 0.6% | 76.3% |
| LOAD_FAST LOAD_CONST | 11,802,240 | 0.6% | 77.0% |
| LOAD_CONST MAKE_FUNCTION | 11,796,720 | 0.6% | 77.6% |
| POP_TOP RESUME_CHECK | 11,796,700 | 0.6% | 78.2% |
| LOAD_FAST FOR_ITER_LIST | 11,796,700 | 0.6% | 78.8% |
| GET_ITER CALL_PY_EXACT_ARGS | 11,796,680 | 0.6% | 79.4% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 11,796,520 | 0.6% | 80.0% |
| CACHE POP_TOP | 11,796,500 | 0.6% | 80.7% |
| BINARY_SUBSCR BINARY_SUBSCR_DICT | 11,796,500 | 0.6% | 81.3% |
| MAKE_FUNCTION LOAD_FAST | 11,796,480 | 0.6% | 81.9% |
| BUILD_TUPLE LIST_APPEND | 11,796,480 | 0.6% | 82.5% |
| LOAD_CONST BINARY_SUBSCR | 11,796,480 | 0.6% | 83.1% |
| LOAD_FAST LIST_APPEND | 11,796,480 | 0.6% | 83.7% |
| LOAD_FAST MAP_ADD | 11,796,480 | 0.6% | 84.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 11,796,480 | 0.6% | 85.0% |
| STORE_FAST MAP_ADD | 11,796,480 | 0.6% | 85.6% |
| STORE_FAST_LOAD_FAST LOAD_FAST | 11,796,480 | 0.6% | 86.2% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 11,796,480 | 0.6% | 86.8% |
| BINARY_SUBSCR_DICT LIST_APPEND | 11,796,460 | 0.6% | 87.4% |
| CALL_BUILTIN_O RETURN_VALUE | 11,796,460 | 0.6% | 88.0% |
| CALL_LEN LOAD_FAST | 11,796,460 | 0.6% | 88.7% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 11,796,460 | 0.6% | 89.3% |
| COMPARE_OP_INT LOAD_FAST | 11,796,460 | 0.6% | 89.9% |
| LOAD_ATTR_INSTANCE_VALUE GET_ITER | 11,796,460 | 0.6% | 90.5% |
| LOAD_ATTR_INSTANCE_VALUE BUILD_TUPLE | 11,796,460 | 0.6% | 91.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 11,796,460 | 0.6% | 91.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 11,796,460 | 0.6% | 92.3% |
| RETURN_GENERATOR CALL_BUILTIN_O | 11,796,440 | 0.6% | 93.0% |
| RETURN_VALUE LOAD_GLOBAL_BUILTIN | 11,796,440 | 0.6% | 93.6% |
| BINARY_SUBSCR_DICT CALL_LEN | 11,796,440 | 0.6% | 94.2% |
| BINARY_SUBSCR_DICT CALL_PY_EXACT_ARGS | 11,796,440 | 0.6% | 94.8% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 11,796,440 | 0.6% | 95.4% |
| POP_TOP LOAD_FAST | 8,519,700 | 0.4% | 95.9% |
| POP_TOP JUMP_BACKWARD | 7,864,800 | 0.4% | 96.3% |
| RESUME_CHECK POP_TOP | 7,864,780 | 0.4% | 96.7% |
| POP_JUMP_IF_FALSE POP_TOP | 7,864,320 | 0.4% | 97.1% |
| POP_JUMP_IF_FALSE RETURN_VALUE | 7,864,320 | 0.4% | 97.5% |
| CACHE RESUME_CHECK | 7,864,300 | 0.4% | 97.9% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 7,864,300 | 0.4% | 98.3% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 4,587,520 | 0.2% | 98.6% |
| STORE_FAST STORE_FAST | 3,278,720 | 0.2% | 98.7% |
| BUILD_MAP SWAP | 1,310,720 | 0.1% | 98.8% |
| SWAP BUILD_MAP | 1,310,720 | 0.1% | 98.9% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,310,640 | 0.1% | 99.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 666,600 | 0.0% | 99.0% |
| LOAD_CONST LOAD_FAST | 657,280 | 0.0% | 99.0% |
| EXIT_INIT_CHECK RETURN_VALUE | 657,240 | 0.0% | 99.1% |
| RETURN_CONST EXIT_INIT_CHECK | 657,240 | 0.0% | 99.1% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 657,240 | 0.0% | 99.1% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 657,240 | 0.0% | 99.2% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 657,240 | 0.0% | 99.2% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 657,200 | 0.0% | 99.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 655,600 | 0.0% | 99.3% |
| FOR_ITER_LIST RETURN_CONST | 655,600 | 0.0% | 99.3% |
| JUMP_BACKWARD FOR_ITER_RANGE | 655,560 | 0.0% | 99.3% |
| FOR_ITER_RANGE STORE_FAST | 655,560 | 0.0% | 99.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 655,460 | 0.0% | 99.4% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,796,500 | 60.0% |
| RESUME_CHECK | 7,864,300 | 40.0% |
| MAKE_CELL | 240 | 0.0% |
| RESUME | 60 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,796,480 | 100.0% |
| BINARY_SUBSCR | 3,220 | 0.0% |
| BUILD_SLICE | 1,920 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 11,796,500 | 100.0% |
| BINARY_SUBSCR | 3,220 | 0.0% |
| GET_ITER | 1,920 | 0.0% |
| CALL | 40 | 0.0% |
| LIST_APPEND | 20 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 240 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 657,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 657,240 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,073,360 | 56.1% |
| LOAD_ATTR_INSTANCE_VALUE | 11,796,460 | 43.9% |
| BINARY_SUBSCR | 1,920 | 0.0% |
| LOAD_CONST | 1,440 | 0.0% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 15,075,200 | 56.1% |
| CALL_PY_EXACT_ARGS | 11,796,680 | 43.9% |
| FOR_ITER_TUPLE | 1,400 | 0.0% |
| FOR_ITER_GEN | 220 | 0.0% |
| FOR_ITER_RANGE | 120 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 19,005,460 | 96.7% |
| RETURN_CONST | 655,400 | 3.3% |
| RETURN_VALUE | 240 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,796,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,796,480 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 240 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 11,796,500 | 40.9% |
| RESUME_CHECK | 7,864,780 | 27.3% |
| POP_JUMP_IF_FALSE | 7,864,320 | 27.3% |
| RETURN_CONST | 655,360 | 2.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,340 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,796,700 | 40.9% |
| LOAD_FAST | 8,519,700 | 29.5% |
| JUMP_BACKWARD | 7,864,800 | 27.3% |
| RETURN_CONST | 655,360 | 2.3% |
| NOP | 80 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 180 | 45.0% |
| LOAD_DEREF | 160 | 40.0% |
| LOAD_ATTR | 60 | 15.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 240 | 60.0% |
| LOAD_FAST | 160 | 40.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,796,460 | 100.0% |
| COPY_FREE_VARS | 240 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 11,796,440 | 100.0% |
| RETURN_VALUE | 240 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 11,796,460 | 41.9% |
| POP_JUMP_IF_FALSE | 7,864,320 | 27.9% |
| LOAD_ATTR_INSTANCE_VALUE | 7,864,300 | 27.9% |
| EXIT_INIT_CHECK | 657,240 | 2.3% |
| RETURN_GENERATOR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 15,728,600 | 55.8% |
| LOAD_GLOBAL_BUILTIN | 11,796,440 | 41.9% |
| STORE_FAST | 655,420 | 2.3% |
| CALL_LIST_APPEND | 1,880 | 0.0% |
| INTERPRETER_EXIT | 240 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 33.3% |
| COPY | 40 | 33.3% |
| STORE_FAST_LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 33.3% |
| TO_BOOL_BOOL | 40 | 33.3% |
| POP_JUMP_IF_TRUE | 20 | 16.7% |
| TO_BOOL_NONE | 20 | 16.7% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 66.7% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 40 | 33.3% |
| RETURN_VALUE | 20 | 16.7% |
| BUILD_SLICE | 20 | 16.7% |
| STORE_FAST | 20 | 16.7% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 16.7% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 13,764,480 | 95.5% |
| STORE_ATTR_INSTANCE_VALUE | 655,340 | 4.5% |
| LOAD_FAST | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| STORE_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 13,764,480 | 95.5% |
| LOAD_FAST | 655,360 | 4.5% |
| LOAD_DEREF | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,310,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,310,720 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,900 | 99.0% |
| BINARY_OP | 20 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,920 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 11,796,460 | 100.0% |
| LOAD_FAST | 240 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 11,796,480 | 100.0% |
| LOAD_CONST | 240 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 240 | 25.5% |
| LOAD_FAST | 240 | 25.5% |
| CALL | 80 | 8.5% |
| BINARY_SUBSCR | 40 | 4.3% |
| GET_ITER | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 120 | 12.8% |
| STORE_FAST | 120 | 12.8% |
| LOAD_FAST | 100 | 10.6% |
| CALL_PY_EXACT_ARGS | 100 | 10.6% |
| CALL | 80 | 8.5% |


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
| LOAD_ATTR | 15,728,660 | 100.0% |
| COMPARE_OP | 4,040 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 15,728,640 | 100.0% |
| COMPARE_OP | 4,040 | 0.0% |
| COMPARE_OP_INT | 60 | 0.0% |
| LOAD_FAST | 20 | 0.0% |
| POP_JUMP_IF_FALSE | 20 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 15,728,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 15,728,600 | 100.0% |
| TO_BOOL | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 240 | 75.0% |
| CALL_FUNCTION_EX | 80 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 240 | 75.0% |
| RESUME_CHECK | 60 | 18.8% |
| RESUME | 20 | 6.2% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 240 | 46.2% |
| SWAP | 160 | 30.8% |
| GET_ITER | 100 | 19.2% |
| LOAD_FAST | 20 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 30.8% |
| FOR_ITER_LIST | 160 | 30.8% |
| STORE_FAST_LOAD_FAST | 100 | 19.2% |
| FOR_ITER_RANGE | 40 | 7.7% |
| FOR_ITER_TUPLE | 40 | 7.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 106,178,800 | 67.2% |
| MAP_ADD | 23,592,960 | 14.9% |
| POP_JUMP_IF_TRUE | 15,728,640 | 10.0% |
| POP_TOP | 7,864,800 | 5.0% |
| POP_JUMP_IF_FALSE | 4,587,520 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 157,297,220 | 99.6% |
| FOR_ITER_RANGE | 655,560 | 0.4% |
| FOR_ITER_TUPLE | 2,840 | 0.0% |
| FOR_ITER_GEN | 460 | 0.0% |
| FOR_ITER | 240 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 70,778,860 | 66.7% |
| BUILD_TUPLE | 11,796,480 | 11.1% |
| LOAD_FAST | 11,796,480 | 11.1% |
| BINARY_SUBSCR_DICT | 11,796,460 | 11.1% |
| LOAD_ATTR_INSTANCE_VALUE | 10,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 106,178,800 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 15,728,680 | 100.0% |
| LOAD_ATTR | 4,060 | 0.0% |
| LOAD_DEREF | 720 | 0.0% |
| LOAD_FAST | 520 | 0.0% |
| STORE_FAST_LOAD_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 15,728,660 | 100.0% |
| LOAD_ATTR | 4,060 | 0.0% |
| LOAD_FAST | 600 | 0.0% |
| GET_ITER | 260 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,802,240 | 47.4% |
| LOAD_GLOBAL_BUILTIN | 11,796,520 | 47.4% |
| CALL_LEN | 655,400 | 2.6% |
| LOAD_GLOBAL_MODULE | 655,340 | 2.6% |
| LOAD_CONST | 1,920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 11,796,720 | 47.4% |
| BINARY_SUBSCR | 11,796,480 | 47.4% |
| LOAD_FAST | 657,280 | 2.6% |
| COMPARE_OP_INT | 655,360 | 2.6% |
| BINARY_OP_ADD_INT | 3,760 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 50.0% |
| SET_FUNCTION_ATTRIBUTE | 240 | 25.0% |
| NOP | 80 | 8.3% |
| BUILD_LIST | 80 | 8.3% |
| RESUME_CHECK | 60 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 720 | 75.0% |
| PUSH_NULL | 160 | 16.7% |
| LIST_EXTEND | 80 | 8.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 70,778,860 | 26.5% |
| LOAD_ATTR_INSTANCE_VALUE | 35,389,380 | 13.3% |
| RESUME_CHECK | 28,180,900 | 10.6% |
| STORE_FAST | 26,873,680 | 10.1% |
| POP_JUMP_IF_TRUE | 19,005,520 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 102,235,800 | 38.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 70,778,840 | 26.5% |
| CALL_PY_EXACT_ARGS | 16,383,920 | 6.1% |
| GET_ITER | 15,073,360 | 5.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,451,760 | 4.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 15,075,200 | 95.8% |
| LOAD_FAST_AND_CLEAR | 655,360 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 15,075,200 | 95.8% |
| LOAD_FAST_AND_CLEAR | 655,360 | 4.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 11,796,460 | 48.6% |
| LOAD_GLOBAL_BUILTIN | 11,796,460 | 48.6% |
| RESUME_CHECK | 657,240 | 2.7% |
| STORE_ATTR_INSTANCE_VALUE | 9,500 | 0.0% |
| LOAD_FAST_LOAD_FAST | 3,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 23,592,880 | 97.2% |
| STORE_ATTR_INSTANCE_VALUE | 666,600 | 2.7% |
| LOAD_FAST_LOAD_FAST | 3,840 | 0.0% |
| CALL_ALLOC_AND_ENTER_INIT | 1,880 | 0.0% |
| STORE_ATTR | 280 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 42.9% |
| RETURN_VALUE | 80 | 14.3% |
| FOR_ITER_RANGE | 80 | 14.3% |
| LOAD_ATTR | 40 | 7.1% |
| RESUME | 40 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160 | 28.6% |
| LOAD_GLOBAL_BUILTIN | 120 | 21.4% |
| LOAD_ATTR | 80 | 14.3% |
| LOAD_CONST | 60 | 10.7% |
| LOAD_FAST | 60 | 10.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 240 | 100.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,796,480 | 50.0% |
| STORE_FAST | 11,796,480 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 23,592,960 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 31,457,240 | 98.0% |
| COMPARE_OP_INT | 655,340 | 2.0% |
| TO_BOOL | 40 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,796,480 | 36.7% |
| POP_TOP | 7,864,320 | 24.5% |
| RETURN_VALUE | 7,864,320 | 24.5% |
| JUMP_BACKWARD | 4,587,520 | 14.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 19,005,380 | 54.7% |
| TO_BOOL_NONE | 15,728,680 | 45.3% |
| COMPARE_OP_INT | 60 | 0.0% |
| TO_BOOL | 20 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,005,520 | 54.7% |
| JUMP_BACKWARD | 15,728,640 | 45.3% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 657,240 | 33.4% |
| FOR_ITER_LIST | 655,600 | 33.3% |
| POP_TOP | 655,360 | 33.3% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXIT_INIT_CHECK | 657,240 | 33.4% |
| INTERPRETER_EXIT | 655,400 | 33.3% |
| POP_TOP | 655,360 | 33.3% |
| END_FOR | 240 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 240 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 280 | 77.8% |
| LOAD_FAST | 80 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 180 | 50.0% |
| LOAD_FAST_LOAD_FAST | 100 | 27.8% |
| RETURN_CONST | 40 | 11.1% |
| BUILD_LIST | 20 | 5.6% |
| LOAD_FAST | 20 | 5.6% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 26,216,740 | 60.6% |
| SWAP | 12,451,840 | 28.8% |
| STORE_FAST | 3,278,720 | 7.6% |
| FOR_ITER_RANGE | 655,560 | 1.5% |
| RETURN_VALUE | 655,420 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,873,680 | 62.1% |
| MAP_ADD | 11,796,480 | 27.3% |
| STORE_FAST | 3,278,720 | 7.6% |
| LOAD_GLOBAL_MODULE | 655,600 | 1.5% |
| LOAD_GLOBAL_BUILTIN | 655,360 | 1.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 144,844,940 | 100.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 70,778,840 | 48.9% |
| TO_BOOL_ALWAYS_TRUE | 19,005,360 | 13.1% |
| TO_BOOL_NONE | 15,728,680 | 10.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 15,728,600 | 10.9% |
| LOAD_ATTR_INSTANCE_VALUE | 11,806,880 | 8.2% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 15,075,200 | 35.4% |
| BUILD_LIST | 13,764,480 | 32.3% |
| FOR_ITER_LIST | 12,451,840 | 29.2% |
| BUILD_MAP | 1,310,720 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 15,075,040 | 35.4% |
| BUILD_LIST | 13,764,480 | 32.3% |
| STORE_FAST | 12,451,840 | 29.2% |
| BUILD_MAP | 1,310,720 | 3.1% |
| FOR_ITER | 160 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 19,005,420 | 100.0% |
| BINARY_SUBSCR_DICT | 480 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 19,005,460 | 100.0% |
| STORE_FAST | 460 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 40.0% |
| CACHE | 60 | 30.0% |
| POP_TOP | 20 | 10.0% |
| CALL_FUNCTION_EX | 20 | 10.0% |
| COPY_FREE_VARS | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 30.0% |
| LOAD_FAST_LOAD_FAST | 40 | 20.0% |
| LOAD_GLOBAL | 40 | 20.0% |
| POP_TOP | 20 | 10.0% |
| LOAD_CONST | 20 | 10.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,760 | 98.9% |
| BINARY_OP | 40 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 1,900 | 50.0% |
| STORE_FAST | 1,900 | 50.0% |


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

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 23,592,880 | 66.7% |
| BINARY_SUBSCR | 11,796,500 | 33.3% |
| LOAD_FAST | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 11,796,460 | 33.3% |
| CALL_LEN | 11,796,440 | 33.3% |
| CALL_PY_EXACT_ARGS | 11,796,440 | 33.3% |
| YIELD_VALUE | 480 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 655,320 | 99.7% |
| LOAD_FAST_LOAD_FAST | 1,880 | 0.3% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 657,240 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 33.3% |
| LOAD_CONST | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 50.0% |
| STORE_FAST | 60 | 50.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 11,796,440 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 11,796,460 | 100.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 11,796,440 | 94.7% |
| LOAD_ATTR_INSTANCE_VALUE | 655,320 | 5.3% |
| CALL | 60 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,796,460 | 94.7% |
| LOAD_CONST | 655,400 | 5.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,880 | 98.9% |
| CALL | 20 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,900 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 70,778,840 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 70,778,860 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 655,320 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 655,340 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,383,920 | 41.0% |
| GET_ITER | 11,796,680 | 29.5% |
| BINARY_SUBSCR_DICT | 11,796,440 | 29.5% |
| CALL | 100 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 28,180,480 | 70.5% |
| RETURN_GENERATOR | 11,796,460 | 29.5% |
| COPY_FREE_VARS | 240 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 11,796,440 | 94.7% |
| LOAD_CONST | 655,360 | 5.3% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,796,460 | 94.7% |
| POP_JUMP_IF_FALSE | 655,340 | 5.3% |
| POP_JUMP_IF_TRUE | 60 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 460 | 65.7% |
| GET_ITER | 220 | 31.4% |
| FOR_ITER | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 480 | 68.6% |
| POP_TOP | 220 | 31.4% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 157,297,220 | 85.4% |
| SWAP | 15,075,040 | 8.2% |
| LOAD_FAST | 11,796,700 | 6.4% |
| FOR_ITER | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 144,844,940 | 78.6% |
| STORE_FAST | 26,216,740 | 14.2% |
| SWAP | 12,451,840 | 6.8% |
| RETURN_CONST | 655,600 | 0.4% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 655,560 | 100.0% |
| GET_ITER | 120 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 655,560 | 100.0% |
| LOAD_GLOBAL | 80 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,840 | 66.4% |
| GET_ITER | 1,400 | 32.7% |
| FOR_ITER | 40 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,840 | 66.4% |
| JUMP_BACKWARD | 1,440 | 33.6% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 102,235,800 | 74.3% |
| LOAD_FAST_LOAD_FAST | 23,592,880 | 17.1% |
| STORE_FAST_LOAD_FAST | 11,806,880 | 8.6% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,389,380 | 25.7% |
| BINARY_SUBSCR_DICT | 23,592,880 | 17.1% |
| YIELD_VALUE | 19,005,420 | 13.8% |
| LOAD_GLOBAL_MODULE | 15,728,600 | 11.4% |
| GET_ITER | 11,796,460 | 8.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 70,778,840 | 99.1% |
| LOAD_FAST | 657,200 | 0.9% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 70,778,860 | 99.1% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,320 | 0.9% |
| LOAD_GLOBAL_MODULE | 1,880 | 0.0% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 15,728,600 | 55.8% |
| LOAD_FAST | 12,451,760 | 44.2% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,383,960 | 58.1% |
| LOAD_FAST_LOAD_FAST | 11,796,460 | 41.9% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 66.7% |
| LOAD_ATTR | 60 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 180 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,796,480 | 48.6% |
| RETURN_VALUE | 11,796,440 | 48.6% |
| STORE_FAST | 655,360 | 2.7% |
| LOAD_GLOBAL | 120 | 0.0% |
| FOR_ITER_RANGE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,796,520 | 48.6% |
| LOAD_FAST_LOAD_FAST | 11,796,460 | 48.6% |
| LOAD_FAST | 655,460 | 2.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 15,728,600 | 96.0% |
| STORE_FAST | 655,600 | 4.0% |
| LOAD_ATTR_METHOD_NO_DICT | 1,880 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 15,728,680 | 96.0% |
| LOAD_CONST | 655,340 | 4.0% |
| LOAD_FAST_LOAD_FAST | 1,900 | 0.0% |
| GET_ITER | 220 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 28,180,480 | 58.1% |
| POP_TOP | 11,796,700 | 24.3% |
| CACHE | 7,864,300 | 16.2% |
| CALL_ALLOC_AND_ENTER_INIT | 657,240 | 1.4% |
| FOR_ITER_GEN | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,180,900 | 58.1% |
| LOAD_GLOBAL_BUILTIN | 11,796,480 | 24.3% |
| POP_TOP | 7,864,780 | 16.2% |
| LOAD_FAST_LOAD_FAST | 657,240 | 1.4% |
| LOAD_CONST | 60 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,310,640 | 66.3% |
| LOAD_FAST_LOAD_FAST | 666,600 | 33.7% |
| STORE_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 657,240 | 33.2% |
| BUILD_LIST | 655,340 | 33.1% |
| LOAD_FAST | 655,340 | 33.1% |
| LOAD_FAST_LOAD_FAST | 9,500 | 0.5% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 19,005,360 | 99.1% |
| TO_BOOL_NONE | 163,840 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 19,005,380 | 99.1% |
| TO_BOOL_NONE | 163,820 | 0.9% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 15,728,600 | 50.0% |
| COPY | 15,728,600 | 50.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 31,457,240 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 15,728,680 | 99.0% |
| TO_BOOL_ALWAYS_TRUE | 163,820 | 1.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 15,728,680 | 99.0% |
| TO_BOOL_ALWAYS_TRUE | 163,840 | 1.0% |


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
|     deferred | 60 | 1.5% |
|          hit | 3,860 | 97.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,798,460 | 25.0% |
|          hit | 35,389,860 | 75.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 1.9% |
| Failure | 3,180 | 98.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 3,080 | 96.9% |
| list slice | 100 | 3.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 560 | 0.0% |
|          hit | 136,318,960 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 84.2% |
| Failure | 60 | 15.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,728,700 | 55.8% |
|          hit | 12,451,860 | 44.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 1.5% |
| Failure | 4,040 | 98.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 4,040 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 184,829,820 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,729,800 | 6.2% |
|          hit | 237,252,520 | 93.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 9.8% |
| Failure | 4,060 | 90.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 4,060 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 280 | 0.0% |
|          hit | 40,634,760 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


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
|     deferred | 180 | 0.0% |
|          hit | 1,977,420 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,190,704,720 | 554,630,162,464,951.0% |
|          hit | 49,152,000 | 73.9% |
|         miss | 17,366,960 | 26.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 327,720 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,042,129,720 | 54.4% |
| Not specialized | 110,118,220 | 5.7% |
| Specialized hits | 746,510,620 | 39.0% |
| Specialized misses | 17,366,960 | 0.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL | 368,934,881,474,190,704,720 | 100.0% |
| LOAD_ATTR | 15,729,800 | 0.0% |
| COMPARE_OP | 15,728,700 | 0.0% |
| BINARY_SUBSCR | 11,798,460 | 0.0% |
| CALL | 560 | 0.0% |
| LOAD_GLOBAL | 280 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| STORE_ATTR | 180 | 0.0% |
| BINARY_OP | 60 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL_NONE | 8,683,520 | 50.0% |
| TO_BOOL_ALWAYS_TRUE | 8,683,440 | 50.0% |
| CACHE | 0 | 0.0% |
| END_FOR | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| MAKE_FUNCTION | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 19,661,100 | 32.6% |
| Calls to Python functions inlined | 40,635,380 | 67.4% |
| Calls via PyEval_EvalFrame (total) | 19,661,100 | 32.6% |
| Calls via PyEval_EvalFrame (vector) | 280 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 19,660,820 | 32.6% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 280 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 240 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 41,291,660 | 68.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 27,529,140 | 32.8% |
| Frees to freelist | 27,529,580 |  |
| Allocations | 56,351,420 | 67.2% |
| Allocations to 512 bytes | 55,040,700 | 65.6% |
| Allocations to 4 kbytes | 1,310,720 | 1.6% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 70,115,404 |  |
| New values | 40 |  |
| Interpreter increfs | 688,843,480 | 78.3% |
| Interpreter decrefs | 775,342,220 | 80.9% |
| Increfs | 190,729,905 | 21.7% |
| Decrefs | 183,522,211 | 19.1% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 31,459,598 |  |
| Method cache misses | 302 |  |
| Method cache collisions | 275 |  |
| Method cache dunder hits | 276 |  |
| Method cache dunder misses | 44 |  |


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
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
