
# Pystats results

- benchmark: nqueens
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| POP_TOP | 138,195,280 | 12.6% | 12.6% |  |
| RESUME_CHECK | 125,630,500 | 11.5% | 24.1% | 0.0% |
| INTERPRETER_EXIT | 119,179,380 | 10.9% | 35.0% |  |
| ENTER_EXECUTOR | 118,824,280 | 10.9% | 45.9% |  |
| YIELD_VALUE | 112,389,760 | 10.3% | 56.1% |  |
| LOAD_FAST | 79,109,640 | 7.2% | 63.4% |  |
| LOAD_FAST_LOAD_FAST | 32,259,960 | 2.9% | 66.3% |  |
| LOAD_GLOBAL_BUILTIN | 20,031,740 | 1.8% | 68.2% |  |
| LOAD_CONST | 19,696,560 | 1.8% | 70.0% |  |
| STORE_FAST | 19,694,800 | 1.8% | 71.8% |  |
| FOR_ITER_RANGE | 13,580,240 | 1.2% | 73.0% |  |
| LOAD_DEREF | 13,256,640 | 1.2% | 74.2% |  |
| BINARY_SUBSCR_TUPLE_INT | 13,241,520 | 1.2% | 75.4% |  |
| GET_ITER | 13,241,200 | 1.2% | 76.6% |  |
| RETURN_CONST | 13,240,960 | 1.2% | 77.8% |  |
| RETURN_GENERATOR | 13,240,800 | 1.2% | 79.0% |  |
| COPY_FREE_VARS | 13,240,560 | 1.2% | 80.3% |  |
| CALL_PY_EXACT_ARGS | 13,240,540 | 1.2% | 81.5% |  |
| MAKE_FUNCTION | 13,240,480 | 1.2% | 82.7% |  |
| BUILD_TUPLE | 13,240,480 | 1.2% | 83.9% |  |
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 1.2% | 85.1% |  |
| SWAP | 12,903,840 | 1.2% | 86.3% |  |
| BINARY_SUBSCR_LIST_INT | 12,903,600 | 1.2% | 87.5% |  |
| POP_JUMP_IF_FALSE | 12,903,280 | 1.2% | 88.6% |  |
| FOR_ITER_LIST | 12,902,920 | 1.2% | 89.8% |  |
| UNARY_NEGATIVE | 12,902,080 | 1.2% | 91.0% |  |
| CALL_BUILTIN_CLASS | 6,791,060 | 0.6% | 91.6% |  |
| COMPARE_OP_INT | 6,790,080 | 0.6% | 92.2% |  |
| CALL_LEN | 6,789,380 | 0.6% | 92.9% |  |
| JUMP_FORWARD | 6,465,760 | 0.6% | 93.4% |  |
| JUMP_BACKWARD | 6,453,400 | 0.6% | 94.0% |  |
| BINARY_SUBSCR | 6,453,320 | 0.6% | 94.6% |  |
| STORE_SUBSCR | 6,452,920 | 0.6% | 95.2% |  |
| BINARY_OP_ADD_INT | 6,452,900 | 0.6% | 95.8% |  |
| COPY | 6,452,800 | 0.6% | 96.4% |  |
| BINARY_SLICE | 6,452,400 | 0.6% | 97.0% |  |
| STORE_SUBSCR_LIST_INT | 6,452,380 | 0.6% | 97.6% |  |
| STORE_DEREF | 6,451,360 | 0.6% | 98.2% |  |
| FOR_ITER_GEN | 6,451,340 | 0.6% | 98.8% |  |
| CALL_TUPLE_1 | 6,451,300 | 0.6% | 99.3% |  |
| TO_BOOL_INT | 6,451,160 | 0.6% | 99.9% |  |
| BINARY_OP_SUBTRACT_INT | 339,840 | 0.0% | 100.0% |  |
| POP_JUMP_IF_TRUE | 338,080 | 0.0% | 100.0% |  |
| CALL | 1,420 | 0.0% | 100.0% |  |
| BINARY_OP | 1,080 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 840 | 0.0% | 100.0% |  |
| STORE_SLICE | 600 | 0.0% | 100.0% |  |
| PUSH_NULL | 480 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 400 | 0.0% | 100.0% |  |
| MAKE_CELL | 320 | 0.0% | 100.0% |  |
| RESUME | 300 | 0.0% | 100.0% | 20.0% |
| FOR_ITER | 280 | 0.0% | 100.0% |  |
| END_FOR | 160 | 0.0% | 100.0% |  |
| BUILD_SLICE | 160 | 0.0% | 100.0% |  |
| COMPARE_OP | 160 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| RETURN_VALUE | 80 | 0.0% | 100.0% |  |
| TO_BOOL | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| LOAD_ATTR | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| RESUME_CHECK POP_TOP | 112,389,620 | 10.3% | 10.3% |
| CACHE RESUME_CHECK | 105,938,600 | 9.7% | 20.0% |
| YIELD_VALUE INTERPRETER_EXIT | 105,938,580 | 9.7% | 29.6% |
| POP_TOP ENTER_EXECUTOR | 105,922,480 | 9.7% | 39.3% |
| ENTER_EXECUTOR YIELD_VALUE | 92,682,240 | 8.5% | 47.8% |
| STORE_FAST LOAD_DEREF | 13,241,680 | 1.2% | 49.0% |
| LOAD_DEREF LOAD_FAST | 13,241,600 | 1.2% | 50.2% |
| LOAD_FAST BINARY_SUBSCR_TUPLE_INT | 13,241,440 | 1.2% | 51.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 13,241,340 | 1.2% | 52.6% |
| RETURN_CONST INTERPRETER_EXIT | 13,240,800 | 1.2% | 53.8% |
| POP_TOP RESUME_CHECK | 13,240,680 | 1.2% | 55.1% |
| CACHE POP_TOP | 13,240,660 | 1.2% | 56.3% |
| MAKE_FUNCTION SET_FUNCTION_ATTRIBUTE | 13,240,480 | 1.2% | 57.5% |
| BUILD_TUPLE LOAD_CONST | 13,240,480 | 1.2% | 58.7% |
| COPY_FREE_VARS RETURN_GENERATOR | 13,240,480 | 1.2% | 59.9% |
| LOAD_CONST MAKE_FUNCTION | 13,240,480 | 1.2% | 61.1% |
| LOAD_FAST BUILD_TUPLE | 13,240,480 | 1.2% | 62.3% |
| SET_FUNCTION_ATTRIBUTE LOAD_FAST | 13,240,480 | 1.2% | 63.5% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 13,240,400 | 1.2% | 64.7% |
| RESUME_CHECK LOAD_FAST | 13,240,400 | 1.2% | 65.9% |
| GET_ITER CALL_PY_EXACT_ARGS | 13,240,320 | 1.2% | 67.2% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 12,902,760 | 1.2% | 68.3% |
| LOAD_FAST_LOAD_FAST UNARY_NEGATIVE | 12,902,080 | 1.2% | 69.5% |
| FOR_ITER_RANGE STORE_FAST | 6,790,720 | 0.6% | 70.1% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 6,789,880 | 0.6% | 70.8% |
| BINARY_SUBSCR_TUPLE_INT LOAD_FAST | 6,789,800 | 0.6% | 71.4% |
| FOR_ITER_RANGE RETURN_CONST | 6,789,440 | 0.6% | 72.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 6,789,360 | 0.6% | 72.6% |
| LOAD_FAST GET_ITER | 6,789,360 | 0.6% | 73.2% |
| RETURN_GENERATOR CALL_BUILTIN_CLASS | 6,789,320 | 0.6% | 73.9% |
| LOAD_FAST FOR_ITER_RANGE | 6,789,240 | 0.6% | 74.5% |
| CALL_BUILTIN_CLASS CALL_LEN | 6,789,200 | 0.6% | 75.1% |
| LOAD_FAST LOAD_CONST | 6,452,040 | 0.6% | 75.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 6,452,020 | 0.6% | 76.3% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 6,451,840 | 0.6% | 76.9% |
| STORE_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST | 6,451,800 | 0.6% | 77.5% |
| BINARY_SUBSCR_TUPLE_INT YIELD_VALUE | 6,451,720 | 0.6% | 78.1% |
| FOR_ITER_LIST STORE_FAST | 6,451,720 | 0.6% | 78.6% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 6,451,560 | 0.6% | 79.2% |
| BINARY_OP_ADD_INT YIELD_VALUE | 6,451,460 | 0.6% | 79.8% |
| LOAD_FAST BINARY_OP_ADD_INT | 6,451,440 | 0.6% | 80.4% |
| BINARY_SLICE GET_ITER | 6,451,200 | 0.6% | 81.0% |
| LOAD_CONST LOAD_FAST | 6,451,200 | 0.6% | 81.6% |
| LOAD_FAST BINARY_SLICE | 6,451,200 | 0.6% | 82.2% |
| STORE_DEREF LOAD_FAST | 6,451,200 | 0.6% | 82.8% |
| SWAP COPY | 6,451,200 | 0.6% | 83.4% |
| FOR_ITER_LIST RETURN_CONST | 6,451,200 | 0.6% | 83.9% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,451,180 | 0.6% | 84.5% |
| YIELD_VALUE STORE_DEREF | 6,451,180 | 0.6% | 85.1% |
| CALL_LEN SWAP | 6,451,180 | 0.6% | 85.7% |
| COPY COMPARE_OP_INT | 6,451,160 | 0.6% | 86.3% |
| LOAD_FAST FOR_ITER_LIST | 6,451,160 | 0.6% | 86.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 6,451,160 | 0.6% | 87.5% |
| CALL_TUPLE_1 YIELD_VALUE | 6,451,160 | 0.6% | 88.1% |
| FOR_ITER_GEN RESUME_CHECK | 6,451,160 | 0.6% | 88.7% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 6,451,160 | 0.6% | 89.3% |
| RETURN_GENERATOR CALL_TUPLE_1 | 6,451,120 | 0.6% | 89.8% |
| ENTER_EXECUTOR FOR_ITER_LIST | 6,451,120 | 0.6% | 90.4% |
| LOAD_FAST TO_BOOL_INT | 6,451,120 | 0.6% | 91.0% |
| BINARY_SUBSCR LOAD_FAST_LOAD_FAST | 6,451,040 | 0.6% | 91.6% |
| POP_TOP POP_TOP | 6,451,040 | 0.6% | 92.2% |
| POP_TOP JUMP_FORWARD | 6,451,040 | 0.6% | 92.8% |
| UNARY_NEGATIVE BINARY_SUBSCR | 6,451,040 | 0.6% | 93.4% |
| UNARY_NEGATIVE STORE_SUBSCR | 6,451,040 | 0.6% | 94.0% |
| JUMP_FORWARD LOAD_FAST | 6,451,040 | 0.6% | 94.6% |
| SWAP LOAD_FAST_LOAD_FAST | 6,451,040 | 0.6% | 95.2% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 6,451,020 | 0.6% | 95.7% |
| BINARY_SUBSCR_LIST_INT SWAP | 6,451,020 | 0.6% | 96.3% |
| STORE_SUBSCR LOAD_GLOBAL_BUILTIN | 6,451,000 | 0.6% | 96.9% |
| ENTER_EXECUTOR LOAD_FAST_LOAD_FAST | 6,450,840 | 0.6% | 97.5% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 6,450,720 | 0.6% | 98.1% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 6,450,700 | 0.6% | 98.7% |
| POP_TOP JUMP_BACKWARD | 6,129,360 | 0.6% | 99.2% |
| POP_JUMP_IF_FALSE POP_TOP | 6,113,120 | 0.6% | 99.8% |
| BINARY_OP_SUBTRACT_INT YIELD_VALUE | 338,340 | 0.0% | 99.8% |
| LOAD_FAST BINARY_OP_SUBTRACT_INT | 338,320 | 0.0% | 99.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 338,220 | 0.0% | 99.9% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 338,060 | 0.0% | 99.9% |
| CALL_LEN COMPARE_OP_INT | 338,040 | 0.0% | 100.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 323,360 | 0.0% | 100.0% |
| JUMP_FORWARD LOAD_DEREF | 14,720 | 0.0% | 100.0% |
| LOAD_DEREF YIELD_VALUE | 14,720 | 0.0% | 100.0% |
| POP_JUMP_IF_TRUE JUMP_FORWARD | 14,720 | 0.0% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR | 1,800 | 0.0% | 100.0% |
| STORE_SUBSCR STORE_SUBSCR | 1,760 | 0.0% | 100.0% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 1,560 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,360 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 1,200 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 1,040 | 0.0% | 100.0% |
| COPY COPY | 800 | 0.0% | 100.0% |
| LOAD_CONST COMPARE_OP_INT | 800 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST COPY | 800 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 800 | 0.0% | 100.0% |
| SWAP SWAP | 800 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_INT SWAP | 780 | 0.0% | 100.0% |
| COPY BINARY_SUBSCR_LIST_INT | 760 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 760 | 0.0% | 100.0% |
| SWAP STORE_SUBSCR_LIST_INT | 760 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 720 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP_SUBTRACT_INT | 680 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,200 | 100.0% |
| LOAD_CONST | 600 | 0.0% |
| BINARY_OP_ADD_INT | 580 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 6,451,200 | 100.0% |
| BINARY_OP | 600 | 0.0% |
| LOAD_FAST_LOAD_FAST | 600 | 0.0% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 600 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 105,938,600 | 88.9% |
| POP_TOP | 13,240,660 | 11.1% |
| RESUME | 120 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 6,451,040 | 100.0% |
| BINARY_SUBSCR | 1,800 | 0.0% |
| BUILD_SLICE | 160 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,451,040 | 100.0% |
| BINARY_SUBSCR | 1,800 | 0.0% |
| STORE_FAST | 180 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 80 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 80 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 160 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,789,360 | 51.3% |
| BINARY_SLICE | 6,451,200 | 48.7% |
| CALL_BUILTIN_CLASS | 460 | 0.0% |
| RETURN_GENERATOR | 160 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 13,240,320 | 100.0% |
| FOR_ITER_RANGE | 520 | 0.0% |
| CALL | 160 | 0.0% |
| FOR_ITER_GEN | 140 | 0.0% |
| FOR_ITER | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 105,938,580 | 88.9% |
| RETURN_CONST | 13,240,800 | 11.1% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 100.0% |


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
| RESUME_CHECK | 112,389,620 | 81.3% |
| CACHE | 13,240,660 | 9.6% |
| POP_TOP | 6,451,040 | 4.7% |
| POP_JUMP_IF_FALSE | 6,113,120 | 4.4% |
| CALL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 105,922,480 | 76.6% |
| RESUME_CHECK | 13,240,680 | 9.6% |
| POP_TOP | 6,451,040 | 4.7% |
| JUMP_FORWARD | 6,451,040 | 4.7% |
| JUMP_BACKWARD | 6,129,360 | 4.4% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320 | 66.7% |
| LOAD_DEREF | 80 | 16.7% |
| LOAD_ATTR_MODULE | 60 | 12.5% |
| LOAD_ATTR | 20 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 400 | 83.3% |
| LOAD_FAST | 80 | 16.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 13,240,480 | 100.0% |
| MAKE_CELL | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 6,789,320 | 51.3% |
| CALL_TUPLE_1 | 6,451,120 | 48.7% |
| CALL | 200 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 6,451,040 | 100.0% |
| STORE_SUBSCR | 1,760 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| SWAP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,451,000 | 100.0% |
| STORE_SUBSCR | 1,760 | 0.0% |
| STORE_SUBSCR_LIST_INT | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 50.0% |
| TO_BOOL_INT | 40 | 50.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,902,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 6,451,040 | 50.0% |
| STORE_SUBSCR | 6,451,040 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 600 | 55.6% |
| LOAD_CONST | 200 | 18.5% |
| LOAD_FAST | 120 | 11.1% |
| BINARY_OP | 80 | 7.4% |
| LOAD_FAST_LOAD_FAST | 80 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 620 | 57.4% |
| BINARY_OP_ADD_INT | 100 | 9.3% |
| BINARY_OP | 80 | 7.4% |
| BINARY_OP_SUBTRACT_INT | 80 | 7.4% |
| LOAD_CONST | 40 | 3.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 160 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,240,480 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 400 | 28.2% |
| LOAD_FAST | 280 | 19.7% |
| RETURN_GENERATOR | 200 | 14.1% |
| CALL | 200 | 14.1% |
| GET_ITER | 160 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 260 | 18.3% |
| CALL_BUILTIN_CLASS | 220 | 15.5% |
| CALL | 200 | 14.1% |
| STORE_FAST | 160 | 11.3% |
| CALL_PY_EXACT_ARGS | 100 | 7.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 50.0% |
| COPY | 40 | 25.0% |
| CALL | 20 | 12.5% |
| CALL_LEN | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 80 | 50.0% |
| POP_JUMP_IF_FALSE | 60 | 37.5% |
| POP_JUMP_IF_TRUE | 20 | 12.5% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 6,451,200 | 100.0% |
| COPY | 800 | 0.0% |
| LOAD_FAST_LOAD_FAST | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 6,451,160 | 100.0% |
| COPY | 800 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 760 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 13,240,400 | 100.0% |
| CALL | 80 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 13,240,480 | 100.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 105,922,480 | 89.1% |
| ENTER_EXECUTOR | 6,450,720 | 5.4% |
| POP_JUMP_IF_FALSE | 6,450,700 | 5.4% |
| STORE_SUBSCR_LIST_INT | 260 | 0.0% |
| JUMP_BACKWARD | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 92,682,240 | 78.0% |
| FOR_ITER_RANGE | 6,789,360 | 5.7% |
| FOR_ITER_LIST | 6,451,120 | 5.4% |
| LOAD_FAST_LOAD_FAST | 6,450,840 | 5.4% |
| ENTER_EXECUTOR | 6,450,720 | 5.4% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 140 | 50.0% |
| LOAD_FAST | 80 | 28.6% |
| GET_ITER | 60 | 21.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 42.9% |
| FOR_ITER_RANGE | 80 | 28.6% |
| FOR_ITER_LIST | 40 | 14.3% |
| STORE_DEREF | 20 | 7.1% |
| FOR_ITER_GEN | 20 | 7.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,129,360 | 95.0% |
| POP_JUMP_IF_TRUE | 323,360 | 5.0% |
| POP_JUMP_IF_FALSE | 340 | 0.0% |
| STORE_SUBSCR_LIST_INT | 320 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 6,451,180 | 100.0% |
| FOR_ITER_RANGE | 1,040 | 0.0% |
| FOR_ITER_LIST | 600 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 300 | 0.0% |
| FOR_ITER | 140 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,451,040 | 99.8% |
| POP_JUMP_IF_TRUE | 14,720 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,040 | 99.8% |
| LOAD_DEREF | 14,720 | 0.2% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 40 | 50.0% |
| PUSH_NULL | 20 | 25.0% |
| STORE_FAST | 20 | 25.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 13,240,480 | 67.2% |
| LOAD_FAST | 6,452,040 | 32.8% |
| BINARY_SUBSCR_LIST_INT | 1,560 | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,200 | 0.0% |
| BINARY_OP_ADD_INT | 580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 13,240,480 | 67.2% |
| LOAD_FAST | 6,451,200 | 32.8% |
| BINARY_OP_ADD_INT | 1,360 | 0.0% |
| COMPARE_OP_INT | 800 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 760 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,241,680 | 99.9% |
| JUMP_FORWARD | 14,720 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 140 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,241,600 | 99.9% |
| YIELD_VALUE | 14,720 | 0.1% |
| CALL_LEN | 120 | 0.0% |
| PUSH_NULL | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 13,241,600 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 13,241,340 | 16.7% |
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 16.7% |
| RESUME_CHECK | 13,240,400 | 16.7% |
| BINARY_SUBSCR_TUPLE_INT | 6,789,800 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 13,241,440 | 16.7% |
| BUILD_TUPLE | 13,240,480 | 16.7% |
| GET_ITER | 6,789,360 | 8.6% |
| FOR_ITER_RANGE | 6,789,240 | 8.6% |
| LOAD_CONST | 6,452,040 | 8.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,451,840 | 20.0% |
| STORE_SUBSCR_LIST_INT | 6,451,800 | 20.0% |
| BINARY_SUBSCR | 6,451,040 | 20.0% |
| SWAP | 6,451,040 | 20.0% |
| ENTER_EXECUTOR | 6,450,840 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 12,902,760 | 40.0% |
| UNARY_NEGATIVE | 12,902,080 | 40.0% |
| STORE_SUBSCR_LIST_INT | 6,451,560 | 20.0% |
| LOAD_CONST | 1,200 | 0.0% |
| COPY | 800 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 19.0% |
| LOAD_GLOBAL | 120 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 120 | 14.3% |
| POP_JUMP_IF_FALSE | 100 | 11.9% |
| RESUME | 80 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 340 | 40.5% |
| LOAD_FAST | 220 | 26.2% |
| LOAD_GLOBAL | 120 | 14.3% |
| LOAD_GLOBAL_MODULE | 80 | 9.5% |
| LOAD_ATTR | 40 | 4.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140 | 43.8% |
| CALL_PY_WITH_DEFAULTS | 140 | 43.8% |
| CALL | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 320 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 6,452,020 | 50.0% |
| TO_BOOL_INT | 6,451,160 | 50.0% |
| COMPARE_OP | 60 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,450,700 | 50.0% |
| POP_TOP | 6,113,120 | 47.4% |
| LOAD_GLOBAL_BUILTIN | 338,220 | 2.6% |
| LOAD_FAST_LOAD_FAST | 800 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 338,060 | 100.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 323,360 | 95.6% |
| JUMP_FORWARD | 14,720 | 4.4% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 6,789,440 | 51.3% |
| FOR_ITER_LIST | 6,451,200 | 48.7% |
| POP_TOP | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 13,240,800 | 100.0% |
| END_FOR | 160 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,240,480 | 100.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,451,180 | 100.0% |
| CALL_TUPLE_1 | 140 | 0.0% |
| CALL | 20 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,200 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 6,790,720 | 34.5% |
| FOR_ITER_LIST | 6,451,720 | 32.8% |
| BINARY_SUBSCR_LIST_INT | 6,451,020 | 32.8% |
| CALL_BUILTIN_CLASS | 340 | 0.0% |
| BINARY_SUBSCR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 13,241,680 | 67.2% |
| LOAD_FAST_LOAD_FAST | 6,451,840 | 32.8% |
| LOAD_FAST | 640 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 360 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 6,451,180 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 6,451,020 | 50.0% |
| SWAP | 800 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 780 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 6,451,200 | 50.0% |
| LOAD_FAST_LOAD_FAST | 6,451,040 | 50.0% |
| SWAP | 800 | 0.0% |
| STORE_SUBSCR_LIST_INT | 760 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 92,682,240 | 82.5% |
| BINARY_SUBSCR_TUPLE_INT | 6,451,720 | 5.7% |
| BINARY_OP_ADD_INT | 6,451,460 | 5.7% |
| CALL_TUPLE_1 | 6,451,160 | 5.7% |
| BINARY_OP_SUBTRACT_INT | 338,340 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 105,938,580 | 94.3% |
| STORE_DEREF | 6,451,180 | 5.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 120 | 40.0% |
| POP_TOP | 120 | 40.0% |
| FOR_ITER_GEN | 40 | 13.3% |
| COPY_FREE_VARS | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 140 | 46.7% |
| LOAD_FAST | 80 | 26.7% |
| LOAD_GLOBAL | 80 | 26.7% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,440 | 100.0% |
| LOAD_CONST | 1,360 | 0.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,451,460 | 100.0% |
| BINARY_SLICE | 580 | 0.0% |
| LOAD_CONST | 580 | 0.0% |
| LOAD_FAST | 140 | 0.0% |
| CALL_BUILTIN_CLASS | 120 | 0.0% |


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
| LOAD_FAST | 338,320 | 99.6% |
| LOAD_CONST | 760 | 0.2% |
| LOAD_FAST_LOAD_FAST | 680 | 0.2% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 338,340 | 99.6% |
| SWAP | 780 | 0.2% |
| LOAD_FAST_LOAD_FAST | 580 | 0.2% |
| LOAD_CONST | 140 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,902,760 | 100.0% |
| COPY | 760 | 0.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,451,020 | 50.0% |
| SWAP | 6,451,020 | 50.0% |
| LOAD_CONST | 1,560 | 0.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,241,440 | 100.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,789,800 | 51.3% |
| YIELD_VALUE | 6,451,720 | 48.7% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 6,789,320 | 100.0% |
| LOAD_FAST | 720 | 0.0% |
| CALL_BUILTIN_CLASS | 680 | 0.0% |
| CALL | 220 | 0.0% |
| BINARY_OP_ADD_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 6,789,200 | 100.0% |
| CALL_BUILTIN_CLASS | 680 | 0.0% |
| GET_ITER | 460 | 0.0% |
| STORE_FAST | 340 | 0.0% |
| POP_TOP | 140 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 6,789,200 | 100.0% |
| LOAD_DEREF | 120 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 6,451,180 | 95.0% |
| COMPARE_OP_INT | 338,040 | 5.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 13,240,320 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 13,240,400 | 100.0% |
| MAKE_CELL | 140 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| CALL | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 140 | 100.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 6,451,120 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,451,160 | 100.0% |
| STORE_DEREF | 140 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 6,451,160 | 95.0% |
| CALL_LEN | 338,040 | 5.0% |
| LOAD_CONST | 800 | 0.0% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,452,020 | 95.0% |
| POP_JUMP_IF_TRUE | 338,060 | 5.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,451,180 | 100.0% |
| GET_ITER | 140 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,451,160 | 100.0% |
| POP_TOP | 140 | 0.0% |
| RESUME | 40 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,160 | 50.0% |
| ENTER_EXECUTOR | 6,451,120 | 50.0% |
| JUMP_BACKWARD | 600 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,451,720 | 50.0% |
| RETURN_CONST | 6,451,200 | 50.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,789,360 | 50.0% |
| LOAD_FAST | 6,789,240 | 50.0% |
| JUMP_BACKWARD | 1,040 | 0.0% |
| GET_ITER | 520 | 0.0% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,790,720 | 50.0% |
| RETURN_CONST | 6,789,440 | 50.0% |
| LOAD_FAST | 80 | 0.0% |


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

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,789,880 | 33.9% |
| LOAD_FAST | 6,451,160 | 32.2% |
| STORE_SUBSCR | 6,451,000 | 32.2% |
| POP_JUMP_IF_FALSE | 338,220 | 1.7% |
| STORE_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,241,340 | 66.1% |
| LOAD_GLOBAL_BUILTIN | 6,789,880 | 33.9% |
| LOAD_DEREF | 140 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_GLOBAL | 120 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 30.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 30.0% |
| LOAD_GLOBAL | 80 | 20.0% |
| RETURN_VALUE | 40 | 10.0% |
| RESUME_CHECK | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 70.0% |
| LOAD_ATTR_MODULE | 80 | 20.0% |
| LOAD_ATTR | 40 | 10.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 105,938,600 | 84.3% |
| POP_TOP | 13,240,680 | 10.5% |
| FOR_ITER_GEN | 6,451,160 | 5.1% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 112,389,620 | 89.5% |
| LOAD_FAST | 13,240,400 | 10.5% |
| LOAD_GLOBAL_BUILTIN | 360 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,451,560 | 100.0% |
| SWAP | 760 | 0.0% |
| STORE_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,451,800 | 100.0% |
| JUMP_BACKWARD | 320 | 0.0% |
| ENTER_EXECUTOR | 260 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,120 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,451,160 | 100.0% |


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
|     deferred | 800 | 0.0% |
|          hit | 105,105,480 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 71.4% |
| Failure | 80 | 28.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 80 | 100.0% |


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
|     deferred | 6,451,360 | 4.0% |
|          hit | 153,897,760 | 96.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 8.2% |
| Failure | 1,800 | 91.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 1,760 | 97.8% |
| list slice | 40 | 2.2% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 860 | 0.0% |
|          hit | 46,173,860 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 82.1% |
| Failure | 100 | 17.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 60.0% |
| other | 40 | 40.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 24,325,280 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 140 | 0.0% |
|          hit | 32,934,500 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 20.0% |
|          hit | 120 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 420 | 0.0% |
|          hit | 20,032,140 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


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
|     deferred | 6,451,100 | 15.5% |
|          hit | 35,071,940 | 84.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 3.3% |
| Failure | 1,760 | 96.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 1,760 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 6,451,160 | 100.0% |

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
| Basic | 796,922,160 | 72.8% |
| Not specialized | 32,604,700 | 3.0% |
| Specialized hits | 264,501,160 | 24.2% |
| Specialized misses | 60 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 6,451,360 | 50.0% |
| STORE_SUBSCR | 6,451,100 | 50.0% |
| CALL | 860 | 0.0% |
| BINARY_OP | 800 | 0.0% |
| LOAD_GLOBAL | 420 | 0.0% |
| FOR_ITER | 140 | 0.0% |
| COMPARE_OP | 80 | 0.0% |
| TO_BOOL | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| RESUME | 60 | 50.0% |
| RESUME_CHECK | 60 | 50.0% |
| CACHE | 0 | 0.0% |
| END_FOR | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| MAKE_FUNCTION | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 119,179,380 | 85.8% |
| Calls to Python functions inlined | 19,692,220 | 14.2% |
| Calls via PyEval_EvalFrame (total) | 119,179,380 | 85.8% |
| Calls via PyEval_EvalFrame (vector) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 119,179,220 | 85.8% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 13,241,040 | 9.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 52,947,040 | 32.1% |
| Frees to freelist | 52,988,020 |  |
| Allocations | 111,961,220 | 67.9% |
| Allocations to 512 bytes | 105,640,700 | 64.1% |
| Allocations to 4 kbytes | 6,320,520 | 3.8% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 111,923,240 |  |
| New values | 0 |  |
| Interpreter increfs | 263,816,160 | 46.8% |
| Interpreter decrefs | 329,337,660 | 45.2% |
| Increfs | 299,575,720 | 53.2% |
| Decrefs | 399,098,280 | 54.8% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 19 |  |
| Method cache misses | 21 |  |
| Method cache collisions | 42 |  |
| Method cache dunder hits | 12,902,539 |  |
| Method cache dunder misses | 21 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 60 | 1,920 | 133,160 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 3,600 |  |
| Traces created | 120 | 3.3% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 3,480 | 96.7% |
| Inner loop found | 20 | 0.6% |
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
| <= 16 | 40 | 33.3% |
| <= 32 | 40 | 33.3% |
| <= 64 | 0 | 0.0% |
| <= 128 | 40 | 33.3% |


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
| <= 16 | 80 | 66.7% |
| <= 32 | 0 | 0.0% |
| <= 64 | 20 | 16.7% |
| <= 128 | 20 | 16.7% |


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
| FOR_ITER_GEN | 3,480 |
| YIELD_VALUE | 80 |


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
