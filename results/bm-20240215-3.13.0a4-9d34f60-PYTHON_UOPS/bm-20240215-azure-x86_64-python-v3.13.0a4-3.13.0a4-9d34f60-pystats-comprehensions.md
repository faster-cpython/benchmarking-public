
# Pystats results

- benchmark: comprehensions
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 110,111,460 | 13.3% | 13.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 81,922,700 | 9.9% | 23.1% |  |
| ENTER_EXECUTOR | 57,019,200 | 6.9% | 30.0% |  |
| FOR_ITER_LIST | 42,604,360 | 5.1% | 35.1% |  |
| RESUME_CHECK | 33,426,920 | 4.0% | 39.1% |  |
| STORE_FAST | 31,466,560 | 3.8% | 42.9% |  |
| POP_JUMP_IF_TRUE | 30,802,100 | 3.7% | 46.6% |  |
| CALL_PY_EXACT_ARGS | 24,904,540 | 3.0% | 49.6% |  |
| LOAD_FAST_LOAD_FAST | 24,265,600 | 2.9% | 52.5% |  |
| BINARY_SUBSCR_DICT | 24,248,820 | 2.9% | 55.5% |  |
| LOAD_GLOBAL_BUILTIN | 24,248,440 | 2.9% | 58.4% |  |
| POP_TOP | 21,628,360 | 2.6% | 61.0% |  |
| RETURN_VALUE | 20,974,300 | 2.5% | 63.5% |  |
| LIST_APPEND | 20,973,660 | 2.5% | 66.0% |  |
| SWAP | 20,318,400 | 2.4% | 68.5% |  |
| INTERPRETER_EXIT | 19,661,100 | 2.4% | 70.8% |  |
| TO_BOOL_ALWAYS_TRUE | 19,144,060 | 2.3% | 73.2% | 38.5% |
| YIELD_VALUE | 19,005,920 | 2.3% | 75.4% |  |
| GET_ITER | 15,731,520 | 1.9% | 77.3% |  |
| STORE_FAST_LOAD_FAST | 14,421,320 | 1.7% | 79.1% |  |
| LOAD_CONST | 13,113,840 | 1.6% | 80.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,107,780 | 1.6% | 82.2% |  |
| MAP_ADD | 12,452,160 | 1.5% | 83.7% |  |
| CALL_LEN | 12,451,860 | 1.5% | 85.2% |  |
| COMPARE_OP_INT | 12,451,860 | 1.5% | 86.7% |  |
| TO_BOOL_NONE | 11,935,960 | 1.4% | 88.2% | 61.7% |
| JUMP_BACKWARD | 11,801,280 | 1.4% | 89.6% |  |
| MAKE_FUNCTION | 11,796,720 | 1.4% | 91.0% |  |
| RETURN_GENERATOR | 11,796,720 | 1.4% | 92.4% |  |
| BUILD_TUPLE | 11,796,720 | 1.4% | 93.8% |  |
| CALL_BUILTIN_O | 11,796,460 | 1.4% | 95.3% |  |
| POP_JUMP_IF_FALSE | 9,831,460 | 1.2% | 96.4% |  |
| TO_BOOL_BOOL | 9,176,060 | 1.1% | 97.5% |  |
| LOAD_FAST_AND_CLEAR | 4,588,640 | 0.6% | 98.1% |  |
| BUILD_LIST | 3,278,080 | 0.4% | 98.5% |  |
| STORE_ATTR_INSTANCE_VALUE | 1,977,420 | 0.2% | 98.7% |  |
| RETURN_CONST | 1,968,240 | 0.2% | 99.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,313,140 | 0.2% | 99.1% |  |
| BUILD_MAP | 1,310,720 | 0.2% | 99.3% |  |
| LOAD_GLOBAL_MODULE | 658,720 | 0.1% | 99.4% |  |
| LOAD_ATTR | 657,760 | 0.1% | 99.4% |  |
| EXIT_INIT_CHECK | 657,240 | 0.1% | 99.5% |  |
| CALL_ALLOC_AND_ENTER_INIT | 657,240 | 0.1% | 99.6% |  |
| BINARY_SUBSCR | 657,040 | 0.1% | 99.7% |  |
| COMPARE_OP | 656,480 | 0.1% | 99.8% |  |
| COPY | 656,000 | 0.1% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 655,900 | 0.1% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,340 | 0.1% | 100.0% |  |
| FOR_ITER_TUPLE | 2,840 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_INT | 2,680 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 1,900 | 0.0% | 100.0% |  |
| CALL | 940 | 0.0% | 100.0% |  |
| BUILD_SLICE | 800 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 760 | 0.0% | 100.0% |  |
| LOAD_DEREF | 720 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 57,673,020 | 6.9% | 6.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 23,592,880 | 2.8% | 9.8% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_SUBSCR_DICT | 23,592,880 | 2.8% | 12.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 19,005,520 | 2.3% | 14.9% |
| YIELD_VALUE INTERPRETER_EXIT | 19,005,460 | 2.3% | 17.2% |
| LOAD_ATTR_INSTANCE_VALUE YIELD_VALUE | 19,005,420 | 2.3% | 19.5% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 19,005,060 | 2.3% | 21.8% |
| STORE_FAST LOAD_FAST | 15,731,760 | 1.9% | 23.7% |
| FOR_ITER_LIST STORE_FAST | 15,075,700 | 1.8% | 25.5% |
| ENTER_EXECUTOR FOR_ITER_LIST | 15,075,160 | 1.8% | 27.3% |
| LOAD_FAST GET_ITER | 15,073,360 | 1.8% | 29.1% |
| FOR_ITER_LIST STORE_FAST_LOAD_FAST | 14,421,220 | 1.7% | 30.8% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 14,418,440 | 1.7% | 32.6% |
| RESUME_CHECK LOAD_FAST | 13,108,260 | 1.6% | 34.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 13,107,840 | 1.6% | 35.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 13,107,780 | 1.6% | 37.3% |
| SWAP STORE_FAST | 12,451,840 | 1.5% | 38.8% |
| FOR_ITER_LIST SWAP | 12,451,840 | 1.5% | 40.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 12,451,760 | 1.5% | 41.8% |
| MAP_ADD ENTER_EXECUTOR | 12,451,480 | 1.5% | 43.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 11,799,220 | 1.4% | 44.7% |
| LIST_APPEND JUMP_BACKWARD | 11,797,840 | 1.4% | 46.2% |
| TO_BOOL_NONE POP_JUMP_IF_TRUE | 11,796,940 | 1.4% | 47.6% |
| LOAD_CONST MAKE_FUNCTION | 11,796,720 | 1.4% | 49.0% |
| POP_TOP RESUME_CHECK | 11,796,700 | 1.4% | 50.4% |
| LOAD_FAST FOR_ITER_LIST | 11,796,700 | 1.4% | 51.8% |
| GET_ITER CALL_PY_EXACT_ARGS | 11,796,680 | 1.4% | 53.3% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 11,796,520 | 1.4% | 54.7% |
| CACHE POP_TOP | 11,796,500 | 1.4% | 56.1% |
| MAKE_FUNCTION LOAD_FAST | 11,796,480 | 1.4% | 57.5% |
| BUILD_TUPLE LIST_APPEND | 11,796,480 | 1.4% | 58.9% |
| STORE_FAST MAP_ADD | 11,796,480 | 1.4% | 60.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 11,796,480 | 1.4% | 61.8% |
| CALL_BUILTIN_O RETURN_VALUE | 11,796,460 | 1.4% | 63.2% |
| CALL_LEN LOAD_FAST | 11,796,460 | 1.4% | 64.6% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 11,796,460 | 1.4% | 66.0% |
| COMPARE_OP_INT LOAD_FAST | 11,796,460 | 1.4% | 67.5% |
| LOAD_ATTR_INSTANCE_VALUE BUILD_TUPLE | 11,796,460 | 1.4% | 68.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 11,796,460 | 1.4% | 70.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 11,796,460 | 1.4% | 71.7% |
| RETURN_GENERATOR CALL_BUILTIN_O | 11,796,440 | 1.4% | 73.1% |
| RETURN_VALUE LOAD_GLOBAL_BUILTIN | 11,796,440 | 1.4% | 74.6% |
| BINARY_SUBSCR_DICT CALL_LEN | 11,796,440 | 1.4% | 76.0% |
| BINARY_SUBSCR_DICT CALL_PY_EXACT_ARGS | 11,796,440 | 1.4% | 77.4% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 11,796,440 | 1.4% | 78.8% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 11,796,240 | 1.4% | 80.2% |
| ENTER_EXECUTOR TO_BOOL_ALWAYS_TRUE | 11,637,380 | 1.4% | 81.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 9,176,060 | 1.1% | 82.7% |
| LIST_APPEND ENTER_EXECUTOR | 9,175,820 | 1.1% | 83.8% |
| RETURN_VALUE TO_BOOL_BOOL | 8,520,060 | 1.0% | 84.9% |
| RESUME_CHECK POP_TOP | 7,864,780 | 0.9% | 85.8% |
| LOAD_FAST LIST_APPEND | 7,864,640 | 0.9% | 86.8% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,864,640 | 0.9% | 87.7% |
| POP_TOP ENTER_EXECUTOR | 7,864,460 | 0.9% | 88.7% |
| CACHE RESUME_CHECK | 7,864,300 | 0.9% | 89.6% |
| ENTER_EXECUTOR RETURN_VALUE | 7,864,100 | 0.9% | 90.5% |
| STORE_FAST_LOAD_FAST TO_BOOL_ALWAYS_TRUE | 7,367,660 | 0.9% | 91.4% |
| ENTER_EXECUTOR TO_BOOL_NONE | 7,367,540 | 0.9% | 92.3% |
| STORE_FAST_LOAD_FAST TO_BOOL_NONE | 4,429,400 | 0.5% | 92.9% |
| GET_ITER LOAD_FAST_AND_CLEAR | 3,933,280 | 0.5% | 93.3% |
| LOAD_FAST_AND_CLEAR SWAP | 3,933,280 | 0.5% | 93.8% |
| SWAP FOR_ITER_LIST | 3,933,120 | 0.5% | 94.3% |
| STORE_FAST STORE_FAST | 3,278,720 | 0.4% | 94.7% |
| BUILD_LIST SWAP | 2,622,560 | 0.3% | 95.0% |
| SWAP BUILD_LIST | 2,622,560 | 0.3% | 95.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 1,311,320 | 0.2% | 95.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 1,311,280 | 0.2% | 95.6% |
| POP_TOP LOAD_FAST | 1,311,160 | 0.2% | 95.8% |
| BUILD_MAP SWAP | 1,310,720 | 0.2% | 95.9% |
| SWAP BUILD_MAP | 1,310,720 | 0.2% | 96.1% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,310,640 | 0.2% | 96.2% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 1,310,320 | 0.2% | 96.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 666,600 | 0.1% | 96.5% |
| LOAD_FAST LOAD_CONST | 659,200 | 0.1% | 96.6% |
| EXIT_INIT_CHECK RETURN_VALUE | 657,240 | 0.1% | 96.6% |
| RETURN_CONST EXIT_INIT_CHECK | 657,240 | 0.1% | 96.7% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 657,240 | 0.1% | 96.8% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 657,240 | 0.1% | 96.9% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 657,240 | 0.1% | 97.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 657,200 | 0.1% | 97.0% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 656,540 | 0.1% | 97.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 656,040 | 0.1% | 97.2% |
| LOAD_ATTR COMPARE_OP | 656,020 | 0.1% | 97.3% |
| COMPARE_OP COPY | 656,000 | 0.1% | 97.4% |
| COPY TO_BOOL_BOOL | 655,960 | 0.1% | 97.4% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 655,960 | 0.1% | 97.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 655,960 | 0.1% | 97.6% |
| CALL_METHOD_DESCRIPTOR_FAST LIST_APPEND | 655,900 | 0.1% | 97.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 655,900 | 0.1% | 97.7% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 655,880 | 0.1% | 97.8% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 655,880 | 0.1% | 97.9% |
| POP_JUMP_IF_FALSE POP_TOP | 655,780 | 0.1% | 98.0% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 655,760 | 0.1% | 98.1% |
| BINARY_SUBSCR BINARY_SUBSCR_DICT | 655,700 | 0.1% | 98.1% |
| LOAD_CONST BINARY_SUBSCR | 655,680 | 0.1% | 98.2% |
| LOAD_FAST MAP_ADD | 655,680 | 0.1% | 98.3% |
| STORE_FAST_LOAD_FAST LOAD_FAST | 655,680 | 0.1% | 98.4% |
| BINARY_SUBSCR_DICT LIST_APPEND | 655,660 | 0.1% | 98.5% |
| LOAD_ATTR_INSTANCE_VALUE GET_ITER | 655,660 | 0.1% | 98.5% |
| FOR_ITER_LIST RETURN_CONST | 655,600 | 0.1% | 98.6% |


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
| LOAD_CONST | 655,680 | 99.8% |
| BUILD_SLICE | 800 | 0.1% |
| BINARY_SUBSCR | 480 | 0.1% |
| LOAD_ATTR | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 655,700 | 99.8% |
| GET_ITER | 800 | 0.1% |
| BINARY_SUBSCR | 480 | 0.1% |
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
| POP_TOP | 240 | 100.0% |


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
| LOAD_FAST | 15,073,360 | 95.8% |
| LOAD_ATTR_INSTANCE_VALUE | 655,660 | 4.2% |
| LOAD_CONST | 1,120 | 0.0% |
| BINARY_SUBSCR | 800 | 0.0% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,796,680 | 75.0% |
| LOAD_FAST_AND_CLEAR | 3,933,280 | 25.0% |
| FOR_ITER_TUPLE | 1,080 | 0.0% |
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
| CACHE | 11,796,500 | 54.5% |
| RESUME_CHECK | 7,864,780 | 36.4% |
| POP_JUMP_IF_FALSE | 655,780 | 3.0% |
| RETURN_CONST | 655,360 | 3.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,340 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,796,700 | 54.5% |
| ENTER_EXECUTOR | 7,864,460 | 36.4% |
| LOAD_FAST | 1,311,160 | 6.1% |
| RETURN_CONST | 655,360 | 3.0% |
| JUMP_BACKWARD | 580 | 0.0% |


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
| CALL_BUILTIN_O | 11,796,460 | 56.2% |
| ENTER_EXECUTOR | 7,864,100 | 37.5% |
| EXIT_INIT_CHECK | 657,240 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 655,760 | 3.1% |
| RETURN_GENERATOR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 11,796,440 | 56.2% |
| TO_BOOL_BOOL | 8,520,060 | 40.6% |
| STORE_FAST | 655,420 | 3.1% |
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
| SWAP | 2,622,560 | 80.0% |
| STORE_ATTR_INSTANCE_VALUE | 655,340 | 20.0% |
| LOAD_FAST | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| STORE_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,622,560 | 80.0% |
| LOAD_FAST | 655,360 | 20.0% |
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
| BINARY_OP_ADD_INT | 780 | 97.5% |
| BINARY_OP | 20 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 800 | 100.0% |


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
| LOAD_ATTR | 656,020 | 99.9% |
| COMPARE_OP | 360 | 0.1% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 656,000 | 99.9% |
| COMPARE_OP | 360 | 0.1% |
| COMPARE_OP_INT | 60 | 0.0% |
| LOAD_FAST | 20 | 0.0% |
| POP_JUMP_IF_FALSE | 20 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 656,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 655,960 | 100.0% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 14,418,440 | 25.3% |
| MAP_ADD | 12,451,480 | 21.8% |
| POP_JUMP_IF_TRUE | 11,796,240 | 20.7% |
| LIST_APPEND | 9,175,820 | 16.1% |
| POP_TOP | 7,864,460 | 13.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 15,075,160 | 26.4% |
| ENTER_EXECUTOR | 14,418,440 | 25.3% |
| TO_BOOL_ALWAYS_TRUE | 11,637,380 | 20.4% |
| RETURN_VALUE | 7,864,100 | 13.8% |
| TO_BOOL_NONE | 7,367,540 | 12.9% |


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
| LIST_APPEND | 11,797,840 | 100.0% |
| FOR_ITER_TUPLE | 820 | 0.0% |
| MAP_ADD | 680 | 0.0% |
| POP_TOP | 580 | 0.0% |
| POP_JUMP_IF_FALSE | 500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 11,799,220 | 100.0% |
| FOR_ITER_TUPLE | 600 | 0.0% |
| FOR_ITER_RANGE | 520 | 0.0% |
| FOR_ITER_GEN | 460 | 0.0% |
| ENTER_EXECUTOR | 240 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 11,796,480 | 56.2% |
| LOAD_FAST | 7,864,640 | 37.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 655,900 | 3.1% |
| BINARY_SUBSCR_DICT | 655,660 | 3.1% |
| LOAD_ATTR_INSTANCE_VALUE | 920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 11,797,840 | 56.3% |
| ENTER_EXECUTOR | 9,175,820 | 43.7% |


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
| LOAD_GLOBAL_MODULE | 656,040 | 99.7% |
| LOAD_FAST | 520 | 0.1% |
| LOAD_DEREF | 480 | 0.1% |
| LOAD_ATTR | 400 | 0.1% |
| STORE_FAST_LOAD_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 656,020 | 99.7% |
| LOAD_ATTR | 400 | 0.1% |
| LOAD_FAST | 360 | 0.1% |
| GET_ITER | 260 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 11,796,520 | 90.0% |
| LOAD_FAST | 659,200 | 5.0% |
| CALL_LEN | 655,400 | 5.0% |
| STORE_FAST | 1,120 | 0.0% |
| LOAD_CONST | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 11,796,720 | 90.0% |
| BINARY_SUBSCR | 655,680 | 5.0% |
| COMPARE_OP_INT | 655,360 | 5.0% |
| BINARY_OP_ADD_INT | 2,640 | 0.0% |
| LOAD_FAST | 1,200 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 240 | 33.3% |
| STORE_FAST | 240 | 33.3% |
| NOP | 80 | 11.1% |
| BUILD_LIST | 80 | 11.1% |
| RESUME_CHECK | 60 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 480 | 66.7% |
| PUSH_NULL | 160 | 22.2% |
| LIST_EXTEND | 80 | 11.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 19,005,520 | 17.3% |
| STORE_FAST | 15,731,760 | 14.3% |
| RESUME_CHECK | 13,108,260 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 13,107,780 | 11.9% |
| MAKE_FUNCTION | 11,796,480 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 57,673,020 | 52.4% |
| GET_ITER | 15,073,360 | 13.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,451,760 | 11.3% |
| FOR_ITER_LIST | 11,796,700 | 10.7% |
| LIST_APPEND | 7,864,640 | 7.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,933,280 | 85.7% |
| LOAD_FAST_AND_CLEAR | 655,360 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,933,280 | 85.7% |
| LOAD_FAST_AND_CLEAR | 655,360 | 14.3% |


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
| STORE_FAST | 11,796,480 | 94.7% |
| LOAD_FAST | 655,680 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,451,480 | 100.0% |
| JUMP_BACKWARD | 680 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 9,176,060 | 93.3% |
| COMPARE_OP_INT | 655,340 | 6.7% |
| TO_BOOL | 40 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,864,640 | 80.0% |
| ENTER_EXECUTOR | 1,310,320 | 13.3% |
| POP_TOP | 655,780 | 6.7% |
| JUMP_BACKWARD | 500 | 0.0% |
| RETURN_VALUE | 220 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 19,005,060 | 61.7% |
| TO_BOOL_NONE | 11,796,940 | 38.3% |
| COMPARE_OP_INT | 60 | 0.0% |
| TO_BOOL | 20 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,005,520 | 61.7% |
| ENTER_EXECUTOR | 11,796,240 | 38.3% |
| JUMP_BACKWARD | 340 | 0.0% |


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
| FOR_ITER_LIST | 15,075,700 | 47.9% |
| SWAP | 12,451,840 | 39.6% |
| STORE_FAST | 3,278,720 | 10.4% |
| RETURN_VALUE | 655,420 | 2.1% |
| BINARY_OP_ADD_INT | 1,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,731,760 | 50.0% |
| MAP_ADD | 11,796,480 | 37.5% |
| STORE_FAST | 3,278,720 | 10.4% |
| LOAD_GLOBAL_BUILTIN | 655,360 | 2.1% |
| ENTER_EXECUTOR | 1,580 | 0.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 14,421,220 | 100.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 7,367,660 | 51.1% |
| TO_BOOL_NONE | 4,429,400 | 30.7% |
| LOAD_ATTR_INSTANCE_VALUE | 656,540 | 4.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 655,960 | 4.5% |
| LOAD_ATTR_METHOD_NO_DICT | 655,880 | 4.5% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 12,451,840 | 61.3% |
| LOAD_FAST_AND_CLEAR | 3,933,280 | 19.4% |
| BUILD_LIST | 2,622,560 | 12.9% |
| BUILD_MAP | 1,310,720 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 12,451,840 | 61.3% |
| FOR_ITER_LIST | 3,933,120 | 19.4% |
| BUILD_LIST | 2,622,560 | 12.9% |
| BUILD_MAP | 1,310,720 | 6.5% |
| FOR_ITER | 160 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 19,005,420 | 100.0% |
| ENTER_EXECUTOR | 240 | 0.0% |
| BINARY_SUBSCR_DICT | 240 | 0.0% |
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
| LOAD_CONST | 2,640 | 98.5% |
| BINARY_OP | 40 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,900 | 70.9% |
| BUILD_SLICE | 780 | 29.1% |


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
| LOAD_ATTR_INSTANCE_VALUE | 23,592,880 | 97.3% |
| BINARY_SUBSCR | 655,700 | 2.7% |
| LOAD_FAST | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 11,796,440 | 48.6% |
| CALL_PY_EXACT_ARGS | 11,796,440 | 48.6% |
| LIST_APPEND | 655,660 | 2.7% |
| YIELD_VALUE | 240 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 654,960 | 99.7% |
| LOAD_FAST_LOAD_FAST | 1,880 | 0.3% |
| LOAD_FAST | 360 | 0.1% |
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
| LOAD_FAST | 655,880 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 655,900 | 100.0% |


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
| GET_ITER | 11,796,680 | 47.4% |
| BINARY_SUBSCR_DICT | 11,796,440 | 47.4% |
| LOAD_FAST | 1,311,280 | 5.3% |
| CALL | 100 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 13,107,840 | 52.6% |
| RETURN_GENERATOR | 11,796,460 | 47.4% |
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
| ENTER_EXECUTOR | 15,075,160 | 35.4% |
| JUMP_BACKWARD | 11,799,220 | 27.7% |
| LOAD_FAST | 11,796,700 | 27.7% |
| SWAP | 3,933,120 | 9.2% |
| FOR_ITER | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,075,700 | 35.4% |
| STORE_FAST_LOAD_FAST | 14,421,220 | 33.8% |
| SWAP | 12,451,840 | 29.2% |
| RETURN_CONST | 655,600 | 1.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 520 | 68.4% |
| GET_ITER | 120 | 15.8% |
| ENTER_EXECUTOR | 80 | 10.5% |
| FOR_ITER | 40 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 78.9% |
| LOAD_GLOBAL | 80 | 10.5% |
| LOAD_GLOBAL_BUILTIN | 40 | 5.3% |
| LOAD_GLOBAL_MODULE | 40 | 5.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,120 | 39.4% |
| GET_ITER | 1,080 | 38.0% |
| JUMP_BACKWARD | 600 | 21.1% |
| FOR_ITER | 40 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,400 | 49.3% |
| JUMP_BACKWARD | 820 | 28.9% |
| ENTER_EXECUTOR | 620 | 21.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,673,020 | 70.4% |
| LOAD_FAST_LOAD_FAST | 23,592,880 | 28.8% |
| STORE_FAST_LOAD_FAST | 656,540 | 0.8% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 23,592,880 | 28.8% |
| YIELD_VALUE | 19,005,420 | 23.2% |
| LOAD_FAST | 13,107,780 | 16.0% |
| BUILD_TUPLE | 11,796,460 | 14.4% |
| COMPARE_OP_INT | 11,796,440 | 14.4% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 657,200 | 50.0% |
| STORE_FAST_LOAD_FAST | 655,880 | 49.9% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 655,900 | 49.9% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 655,320 | 49.9% |
| LOAD_GLOBAL_MODULE | 1,880 | 0.1% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,451,760 | 95.0% |
| STORE_FAST_LOAD_FAST | 655,960 | 5.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,796,460 | 90.0% |
| LOAD_FAST | 1,311,320 | 10.0% |


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
| LOAD_ATTR_INSTANCE_VALUE | 655,960 | 99.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,880 | 0.3% |
| STORE_FAST | 640 | 0.1% |
| LOAD_GLOBAL | 160 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 656,040 | 99.6% |
| LOAD_FAST_LOAD_FAST | 1,900 | 0.3% |
| LOAD_CONST | 380 | 0.1% |
| GET_ITER | 220 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 13,107,840 | 39.2% |
| POP_TOP | 11,796,700 | 35.3% |
| CACHE | 7,864,300 | 23.5% |
| CALL_ALLOC_AND_ENTER_INIT | 657,240 | 2.0% |
| FOR_ITER_GEN | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,108,260 | 39.2% |
| LOAD_GLOBAL_BUILTIN | 11,796,480 | 35.3% |
| POP_TOP | 7,864,780 | 23.5% |
| LOAD_FAST_LOAD_FAST | 657,240 | 2.0% |
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
| ENTER_EXECUTOR | 11,637,380 | 60.8% |
| STORE_FAST_LOAD_FAST | 7,367,660 | 38.5% |
| TO_BOOL_NONE | 139,020 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 19,005,060 | 99.3% |
| TO_BOOL_NONE | 139,000 | 0.7% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,520,060 | 92.9% |
| COPY | 655,960 | 7.1% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,176,060 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 7,367,540 | 61.7% |
| STORE_FAST_LOAD_FAST | 4,429,400 | 37.1% |
| TO_BOOL_ALWAYS_TRUE | 139,000 | 1.2% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 11,796,940 | 98.8% |
| TO_BOOL_ALWAYS_TRUE | 139,020 | 1.2% |


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
|     deferred | 656,540 | 1.8% |
|          hit | 35,389,860 | 98.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 12.0% |
| Failure | 440 | 88.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 360 | 81.8% |
| list slice | 80 | 18.2% |


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
|     deferred | 656,060 | 5.0% |
|          hit | 12,451,860 | 95.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 14.3% |
| Failure | 360 | 85.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 360 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 42,608,660 | 100.0% |

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
|     deferred | 656,920 | 0.3% |
|          hit | 237,252,520 | 99.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 52.4% |
| Failure | 400 | 47.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 400 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 280 | 0.0% |
|          hit | 24,907,160 | 100.0% |

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
|     deferred | 14,457,760 | 21.8% |
|          hit | 51,733,600 | 77.8% |
|         miss | 14,735,720 | 22.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 278,080 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 460,797,320 | 55.5% |
| Not specialized | 42,607,460 | 5.1% |
| Specialized hits | 312,611,100 | 37.6% |
| Specialized misses | 14,735,720 | 1.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL | 14,457,760 | 88.0% |
| LOAD_ATTR | 656,920 | 4.0% |
| BINARY_SUBSCR | 656,540 | 4.0% |
| COMPARE_OP | 656,060 | 4.0% |
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
| TO_BOOL_NONE | 7,368,060 | 50.0% |
| TO_BOOL_ALWAYS_TRUE | 7,367,660 | 50.0% |
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
| Frames pushed | 41,292,200 | 68.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 27,528,720 | 32.8% |
| Frees to freelist | 27,529,580 |  |
| Allocations | 56,352,080 | 67.2% |
| Allocations to 512 bytes | 55,041,260 | 65.6% |
| Allocations to 4 kbytes | 1,310,820 | 1.6% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 70,115,382 |  |
| New values | 40 |  |
| Interpreter increfs | 323,146,740 | 34.5% |
| Interpreter decrefs | 500,755,720 | 49.3% |
| Increfs | 613,457,865 | 65.5% |
| Decrefs | 515,139,909 | 50.7% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 31,459,591 |  |
| Method cache misses | 309 |  |
| Method cache collisions | 317 |  |
| Method cache dunder hits | 260 |  |
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
| Optimization attempts | 6,100 |  |
| Traces created | 6,080 | 99.7% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 20 | 0.3% |
| Inner loop found | 60 | 1.0% |
| Recursive call | 0 | 0.0% |
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
| <= 16 | 40 | 0.7% |
| <= 32 | 100 | 1.6% |
| <= 64 | 100 | 1.6% |
| <= 128 | 5,840 | 96.1% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 20 | 0.3% |
| <= 16 | 120 | 2.0% |
| <= 32 | 0 | 0.0% |
| <= 64 | 100 | 1.6% |


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
| YIELD_VALUE | 20 |
| CALL_ALLOC_AND_ENTER_INIT | 20 |
| FOR_ITER_GEN | 20 |


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
