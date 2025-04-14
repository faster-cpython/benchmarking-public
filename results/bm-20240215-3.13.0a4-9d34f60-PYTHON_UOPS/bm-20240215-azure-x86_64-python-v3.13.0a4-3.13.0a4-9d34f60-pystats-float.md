
# Pystats results

- benchmark: float
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 80,189,140 | 18.5% | 18.5% |  |
| STORE_ATTR_SLOT | 48,052,540 | 11.1% | 29.6% |  |
| BINARY_OP | 32,010,300 | 7.4% | 37.0% |  |
| LOAD_FAST_LOAD_FAST | 32,001,440 | 7.4% | 44.4% |  |
| LOAD_GLOBAL_MODULE | 32,001,140 | 7.4% | 51.8% |  |
| LOAD_CONST | 32,000,720 | 7.4% | 59.2% |  |
| CALL_BUILTIN_O | 32,000,420 | 7.4% | 66.6% |  |
| STORE_FAST | 16,029,420 | 3.7% | 70.3% |  |
| ENTER_EXECUTOR | 16,024,700 | 3.7% | 74.1% |  |
| CALL | 16,004,920 | 3.7% | 77.8% |  |
| COPY | 16,001,440 | 3.7% | 81.5% |  |
| BINARY_OP_MULTIPLY_FLOAT | 16,001,360 | 3.7% | 85.2% |  |
| RESUME_CHECK | 16,001,240 | 3.7% | 88.9% | 0.1% |
| RETURN_CONST | 16,000,480 | 3.7% | 92.6% |  |
| INTERPRETER_EXIT | 16,000,160 | 3.7% | 96.3% |  |
| STORE_SUBSCR_LIST_INT | 15,999,980 | 3.7% | 100.0% |  |
| LOAD_ATTR_SLOT | 107,040 | 0.0% | 100.0% |  |
| POP_JUMP_IF_FALSE | 26,680 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 26,540 | 0.0% | 100.0% |  |
| RETURN_VALUE | 25,580 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 13,320 | 0.0% | 100.0% |  |
| SWAP | 1,440 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 1,240 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,180 | 0.0% | 100.0% |  |
| CALL_PY_EXACT_ARGS | 1,060 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 920 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 920 | 0.0% | 100.0% |  |
| LOAD_ATTR | 840 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 840 | 0.0% | 100.0% |  |
| POP_TOP | 720 | 0.0% | 100.0% |  |
| GET_ITER | 560 | 0.0% | 100.0% |  |
| PUSH_NULL | 480 | 0.0% | 100.0% |  |
| STORE_ATTR | 400 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 360 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 200 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_BUILTIN | 200 | 0.0% | 100.0% |  |
| BINARY_SLICE | 160 | 0.0% | 100.0% |  |
| BUILD_LIST | 160 | 0.0% | 100.0% |  |
| COMPARE_OP | 160 | 0.0% | 100.0% |  |
| FOR_ITER | 160 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 140 | 0.0% | 100.0% |  |
| RESUME | 120 | 0.0% | 100.0% | 18,950.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 60 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 40 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST STORE_ATTR_SLOT | 48,051,020 | 11.1% | 11.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 32,000,560 | 7.4% | 18.5% |
| BINARY_OP LOAD_FAST | 32,000,000 | 7.4% | 25.9% |
| LOAD_CONST BINARY_OP | 32,000,000 | 7.4% | 33.3% |
| LOAD_FAST CALL_BUILTIN_O | 31,999,920 | 7.4% | 40.7% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 16,001,280 | 3.7% | 44.4% |
| STORE_FAST LOAD_GLOBAL_MODULE | 16,000,840 | 3.7% | 48.1% |
| STORE_ATTR_SLOT RETURN_CONST | 16,000,440 | 3.7% | 51.8% |
| CACHE RESUME_CHECK | 16,000,120 | 3.7% | 55.5% |
| CALL LOAD_FAST_LOAD_FAST | 16,000,000 | 3.7% | 59.2% |
| COPY LOAD_FAST | 16,000,000 | 3.7% | 62.9% |
| RETURN_CONST INTERPRETER_EXIT | 16,000,000 | 3.7% | 66.6% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 16,000,000 | 3.7% | 70.3% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_CONST | 15,999,980 | 3.7% | 74.0% |
| CALL_BUILTIN_O COPY | 15,999,980 | 3.7% | 77.7% |
| CALL_BUILTIN_O LOAD_CONST | 15,999,980 | 3.7% | 81.4% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 15,999,980 | 3.7% | 85.1% |
| STORE_ATTR_SLOT STORE_FAST | 15,999,980 | 3.7% | 88.8% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 15,999,960 | 3.7% | 92.5% |
| STORE_SUBSCR_LIST_INT ENTER_EXECUTOR | 15,999,660 | 3.7% | 96.2% |
| ENTER_EXECUTOR CALL | 15,999,520 | 3.7% | 99.9% |
| LOAD_FAST LOAD_ATTR_SLOT | 105,380 | 0.0% | 99.9% |
| LOAD_ATTR_SLOT LOAD_FAST | 65,840 | 0.0% | 99.9% |
| STORE_ATTR_SLOT LOAD_FAST | 52,140 | 0.0% | 99.9% |
| POP_JUMP_IF_FALSE LOAD_FAST | 26,600 | 0.0% | 99.9% |
| COMPARE_OP_FLOAT POP_JUMP_IF_FALSE | 26,540 | 0.0% | 100.0% |
| LOAD_ATTR_SLOT COMPARE_OP_FLOAT | 26,480 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 25,420 | 0.0% | 100.0% |
| RETURN_VALUE STORE_FAST | 25,180 | 0.0% | 100.0% |
| STORE_FAST ENTER_EXECUTOR | 24,840 | 0.0% | 100.0% |
| ENTER_EXECUTOR LOAD_FAST | 24,700 | 0.0% | 100.0% |
| JUMP_FORWARD LOAD_FAST | 13,320 | 0.0% | 100.0% |
| LOAD_ATTR_SLOT JUMP_FORWARD | 13,280 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 8,460 | 0.0% | 100.0% |
| CALL CALL | 4,200 | 0.0% | 100.0% |
| STORE_FAST LOAD_FAST | 3,040 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 1,640 | 0.0% | 100.0% |
| BINARY_OP SWAP | 1,440 | 0.0% | 100.0% |
| LOAD_FAST COPY | 1,440 | 0.0% | 100.0% |
| LOAD_ATTR_SLOT STORE_FAST | 1,380 | 0.0% | 100.0% |
| COPY LOAD_ATTR_SLOT | 1,320 | 0.0% | 100.0% |
| SWAP STORE_ATTR_SLOT | 1,320 | 0.0% | 100.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 1,060 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_FAST | 1,060 | 0.0% | 100.0% |
| FOR_ITER_LIST STORE_FAST | 920 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 880 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 880 | 0.0% | 100.0% |
| LOAD_FAST CALL | 720 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 640 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_LIST | 600 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 600 | 0.0% | 100.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 560 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 500 | 0.0% | 100.0% |
| RETURN_CONST POP_TOP | 480 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT LOAD_FAST_LOAD_FAST | 460 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_LOAD_FAST | 460 | 0.0% | 100.0% |
| CALL_BUILTIN_O STORE_FAST | 460 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 460 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 460 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 440 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT CALL_BUILTIN_O | 440 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 440 | 0.0% | 100.0% |
| PUSH_NULL CALL | 400 | 0.0% | 100.0% |
| LOAD_FAST LOAD_CONST | 400 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_SLOT | 340 | 0.0% | 100.0% |
| STORE_FAST JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_LIST | 320 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 320 | 0.0% | 100.0% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 320 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_LIST | 280 | 0.0% | 100.0% |
| LOAD_FAST STORE_ATTR | 280 | 0.0% | 100.0% |
| CALL POP_TOP | 240 | 0.0% | 100.0% |
| LOAD_FAST GET_ITER | 240 | 0.0% | 100.0% |
| FOR_ITER_RANGE LOAD_FAST | 240 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_RANGE | 200 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_FAST | 200 | 0.0% | 100.0% |
| STORE_ATTR STORE_ATTR_SLOT | 200 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 200 | 0.0% | 100.0% |
| BINARY_OP STORE_FAST | 180 | 0.0% | 100.0% |
| BINARY_SLICE GET_ITER | 160 | 0.0% | 100.0% |
| RETURN_VALUE INTERPRETER_EXIT | 160 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 160 | 0.0% | 100.0% |
| BUILD_LIST LOAD_FAST | 160 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 160 | 0.0% | 100.0% |
| LOAD_CONST BINARY_SLICE | 160 | 0.0% | 100.0% |
| LOAD_CONST BUILD_LIST | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 160 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 160 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 160 | 0.0% | 100.0% |
| FOR_ITER_LIST LOAD_FAST | 160 | 0.0% | 100.0% |
| POP_TOP ENTER_EXECUTOR | 140 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 140 | 0.0% | 100.0% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 140 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS GET_ITER | 140 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_CONST | 140 | 0.0% | 100.0% |
| CALL STORE_FAST | 120 | 0.0% | 100.0% |
| COPY LOAD_ATTR | 120 | 0.0% | 100.0% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 120 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 160 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,000,120 | 100.0% |
| RESUME | 40 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 20 | 50.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 42.9% |
| BINARY_SLICE | 160 | 28.6% |
| CALL_BUILTIN_CLASS | 140 | 25.0% |
| CALL | 20 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 280 | 50.0% |
| FOR_ITER_RANGE | 200 | 35.7% |
| FOR_ITER | 80 | 14.3% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 16,000,000 | 100.0% |
| RETURN_VALUE | 160 | 0.0% |


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
| RETURN_CONST | 480 | 66.7% |
| CALL | 240 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 500 | 69.4% |
| ENTER_EXECUTOR | 140 | 19.4% |
| NOP | 80 | 11.1% |


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

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,420 | 99.4% |
| RETURN_VALUE | 160 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,180 | 98.4% |
| INTERPRETER_EXIT | 160 | 0.6% |
| RETURN_VALUE | 160 | 0.6% |
| LOAD_GLOBAL | 40 | 0.2% |
| LOAD_GLOBAL_MODULE | 40 | 0.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20 | 50.0% |
| STORE_SUBSCR_LIST_INT | 20 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 32,000,000 | 100.0% |
| BINARY_OP | 8,460 | 0.0% |
| LOAD_FAST | 1,640 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,000,000 | 100.0% |
| BINARY_OP | 8,460 | 0.0% |
| SWAP | 1,440 | 0.0% |
| STORE_FAST | 180 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 80 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 15,999,520 | 100.0% |
| CALL | 4,200 | 0.0% |
| LOAD_FAST | 720 | 0.0% |
| PUSH_NULL | 400 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,000,000 | 100.0% |
| CALL | 4,200 | 0.0% |
| POP_TOP | 240 | 0.0% |
| STORE_FAST | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


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
| LOAD_ATTR | 60 | 37.5% |
| LOAD_ATTR_SLOT | 60 | 37.5% |
| LOAD_CONST | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 50.0% |
| COMPARE_OP_FLOAT | 60 | 37.5% |
| COMPARE_OP_INT | 20 | 12.5% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 15,999,980 | 100.0% |
| LOAD_FAST | 1,440 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,000,000 | 100.0% |
| LOAD_ATTR_SLOT | 1,320 | 0.0% |
| LOAD_ATTR | 120 | 0.0% |


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
| STORE_SUBSCR_LIST_INT | 15,999,660 | 99.8% |
| STORE_FAST | 24,840 | 0.2% |
| POP_TOP | 140 | 0.0% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 15,999,520 | 99.8% |
| LOAD_FAST | 24,700 | 0.2% |
| FOR_ITER_LIST | 320 | 0.0% |
| FOR_ITER_RANGE | 160 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 50.0% |
| JUMP_BACKWARD | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 50.0% |
| FOR_ITER_LIST | 40 | 25.0% |
| FOR_ITER_RANGE | 40 | 25.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 500 | 42.4% |
| STORE_FAST | 340 | 28.8% |
| STORE_SUBSCR_LIST_INT | 320 | 27.1% |
| STORE_SUBSCR | 20 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 600 | 50.8% |
| FOR_ITER_RANGE | 440 | 37.3% |
| FOR_ITER | 80 | 6.8% |
| ENTER_EXECUTOR | 60 | 5.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 13,280 | 99.7% |
| LOAD_ATTR | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,320 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 76.2% |
| COPY | 120 | 14.3% |
| LOAD_GLOBAL | 40 | 4.8% |
| LOAD_GLOBAL_MODULE | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 340 | 40.5% |
| LOAD_FAST | 200 | 23.8% |
| STORE_FAST | 80 | 9.5% |
| COMPARE_OP | 60 | 7.1% |
| JUMP_FORWARD | 40 | 4.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 15,999,980 | 50.0% |
| CALL_BUILTIN_O | 15,999,980 | 50.0% |
| LOAD_FAST | 400 | 0.0% |
| LOAD_CONST | 160 | 0.0% |
| RESUME_CHECK | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 32,000,000 | 100.0% |
| BINARY_SLICE | 160 | 0.0% |
| BUILD_LIST | 160 | 0.0% |
| LOAD_CONST | 160 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 32,000,560 | 39.9% |
| BINARY_OP | 32,000,000 | 39.9% |
| COPY | 16,000,000 | 20.0% |
| LOAD_ATTR_SLOT | 65,840 | 0.1% |
| STORE_ATTR_SLOT | 52,140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 48,051,020 | 59.9% |
| CALL_BUILTIN_O | 31,999,920 | 39.9% |
| LOAD_ATTR_SLOT | 105,380 | 0.1% |
| RETURN_VALUE | 25,420 | 0.0% |
| BINARY_OP | 1,640 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 16,000,000 | 50.0% |
| STORE_ATTR_SLOT | 15,999,980 | 50.0% |
| BINARY_OP_ADD_FLOAT | 460 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 460 | 0.0% |
| LOAD_GLOBAL_MODULE | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 16,001,280 | 50.0% |
| STORE_SUBSCR_LIST_INT | 15,999,960 | 50.0% |
| BINARY_OP | 160 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 44.4% |
| RETURN_VALUE | 40 | 11.1% |
| POP_JUMP_IF_FALSE | 40 | 11.1% |
| RESUME | 40 | 11.1% |
| FOR_ITER_LIST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 140 | 38.9% |
| LOAD_FAST | 120 | 33.3% |
| LOAD_ATTR | 40 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 40 | 11.1% |
| LOAD_FAST_LOAD_FAST | 20 | 5.6% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 26,540 | 99.5% |
| COMPARE_OP | 80 | 0.3% |
| COMPARE_OP_INT | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,600 | 99.7% |
| LOAD_GLOBAL | 40 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 16,000,440 | 100.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 16,000,000 | 100.0% |
| POP_TOP | 480 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 70.0% |
| SWAP | 120 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 200 | 50.0% |
| LOAD_FAST | 120 | 30.0% |
| RETURN_CONST | 40 | 10.0% |
| LOAD_FAST_LOAD_FAST | 20 | 5.0% |
| STORE_FAST | 20 | 5.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 15,999,980 | 99.8% |
| RETURN_VALUE | 25,180 | 0.2% |
| LOAD_ATTR_SLOT | 1,380 | 0.0% |
| FOR_ITER_LIST | 920 | 0.0% |
| FOR_ITER_RANGE | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 16,000,840 | 99.8% |
| ENTER_EXECUTOR | 24,840 | 0.2% |
| LOAD_FAST | 3,040 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,320 | 91.7% |
| STORE_ATTR | 120 | 8.3% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 60 | 50.0% |
| CACHE | 40 | 33.3% |
| COPY_FREE_VARS | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 50.0% |
| LOAD_GLOBAL | 40 | 33.3% |
| LOAD_CONST | 20 | 16.7% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 880 | 95.7% |
| BINARY_OP | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 460 | 50.0% |
| CALL_BUILTIN_O | 440 | 47.8% |
| CALL | 20 | 2.2% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 16,001,280 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,999,980 | 100.0% |
| BINARY_OP_ADD_FLOAT | 880 | 0.0% |
| LOAD_FAST_LOAD_FAST | 460 | 0.0% |
| BINARY_OP | 40 | 0.0% |


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

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 85.7% |
| BINARY_SUBSCR | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 140 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 80.0% |
| CALL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 140 | 70.0% |
| STORE_FAST | 60 | 30.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,999,920 | 100.0% |
| BINARY_OP_ADD_FLOAT | 440 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 15,999,980 | 50.0% |
| LOAD_CONST | 15,999,980 | 50.0% |
| STORE_FAST | 460 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 52.8% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 41.5% |
| CALL | 60 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,060 | 100.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 26,480 | 99.8% |
| COMPARE_OP | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 26,540 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| COMPARE_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 600 | 48.4% |
| ENTER_EXECUTOR | 320 | 25.8% |
| GET_ITER | 280 | 22.6% |
| FOR_ITER | 40 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 920 | 74.2% |
| LOAD_FAST | 160 | 12.9% |
| LOAD_GLOBAL_MODULE | 120 | 9.7% |
| LOAD_GLOBAL | 40 | 3.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 440 | 52.4% |
| GET_ITER | 200 | 23.8% |
| ENTER_EXECUTOR | 160 | 19.0% |
| FOR_ITER | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 71.4% |
| LOAD_FAST | 240 | 28.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880 | 95.7% |
| LOAD_ATTR | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 460 | 50.0% |
| CALL_PY_EXACT_ARGS | 440 | 47.8% |
| CALL | 20 | 2.2% |


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

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 105,380 | 98.4% |
| COPY | 1,320 | 1.2% |
| LOAD_ATTR | 340 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,840 | 61.5% |
| COMPARE_OP_FLOAT | 26,480 | 24.7% |
| JUMP_FORWARD | 13,280 | 12.4% |
| STORE_FAST | 1,380 | 1.3% |
| COMPARE_OP | 60 | 0.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 60.0% |
| LOAD_GLOBAL | 40 | 20.0% |
| POP_JUMP_IF_FALSE | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,000,840 | 50.0% |
| RESUME_CHECK | 16,000,000 | 50.0% |
| LOAD_GLOBAL | 140 | 0.0% |
| FOR_ITER_LIST | 120 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,000,560 | 100.0% |
| LOAD_FAST_LOAD_FAST | 460 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 16,000,120 | 100.0% |
| CALL_PY_EXACT_ARGS | 1,060 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 16,000,000 | 100.0% |
| LOAD_FAST | 1,060 | 0.0% |
| LOAD_CONST | 140 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,051,020 | 100.0% |
| SWAP | 1,320 | 0.0% |
| STORE_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 16,000,440 | 33.3% |
| LOAD_FAST_LOAD_FAST | 15,999,980 | 33.3% |
| STORE_FAST | 15,999,980 | 33.3% |
| LOAD_FAST | 52,140 | 0.1% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 15,999,960 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 15,999,660 | 100.0% |
| JUMP_BACKWARD | 320 | 0.0% |


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
|     deferred | 32,001,740 | 25.0% |
|          hit | 95,999,940 | 75.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 1.6% |
| Failure | 8,420 | 98.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 4,140 | 49.2% |
| true divide different types | 4,100 | 48.7% |
| true divide float | 180 | 2.1% |


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
|     deferred | 20 | 11.1% |
|          hit | 140 | 77.8% |

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
|     deferred | 16,000,560 | 16.7% |
|          hit | 80,000,080 | 83.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 3.7% |
| Failure | 4,200 | 96.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| no dict | 4,100 | 97.6% |
| cfunc noargs | 60 | 1.4% |
| other | 40 | 1.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 47,999,520 | 100.0% |

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
|     deferred | 80 | 3.6% |
|          hit | 2,080 | 92.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 420 | 0.0% |
|          hit | 271,998,140 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 0.0% |
|          hit | 32,001,340 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 0.0% |
|          hit | 143,999,320 | 100.0% |

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
|     deferred | 20 | 0.0% |
|          hit | 15,999,980 | 100.0% |

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
| Basic | 224,291,460 | 51.9% |
| Not specialized | 48,044,060 | 11.1% |
| Specialized hits | 160,173,280 | 37.0% |
| Specialized misses | 22,740 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 32,001,740 | 66.7% |
| CALL | 16,000,560 | 33.3% |
| LOAD_ATTR | 420 | 0.0% |
| STORE_ATTR | 200 | 0.0% |
| LOAD_GLOBAL | 180 | 0.0% |
| COMPARE_OP | 80 | 0.0% |
| FOR_ITER | 80 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| RESUME | 22,740 | 50.0% |
| RESUME_CHECK | 22,740 | 50.0% |
| CACHE | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |
| RETURN_VALUE | 0 | 0.0% |
| BUILD_LIST | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 16,000,160 | 33.3% |
| Calls to Python functions inlined | 32,000,080 | 66.7% |
| Calls via PyEval_EvalFrame (total) | 16,000,160 | 33.3% |
| Calls via PyEval_EvalFrame (vector) | 16,000,160 | 33.3% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 16,000,160 | 33.3% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 48,000,240 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 192,013,720 | 70.6% |
| Frees to freelist | 192,016,620 |  |
| Allocations | 79,992,840 | 29.4% |
| Allocations to 512 bytes | 79,992,480 | 29.4% |
| Allocations to 4 kbytes | 40 | 0.0% |
| Allocations over 4 kbytes | 320 | 0.0% |
| Frees | 79,999,705 |  |
| New values | 0 |  |
| Interpreter increfs | 272,165,460 | 21.5% |
| Interpreter decrefs | 512,123,920 | 33.3% |
| Increfs | 991,613,980 | 78.5% |
| Decrefs | 1,023,667,390 | 66.7% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 1,077 |  |
| Method cache misses | 123 |  |
| Method cache collisions | 104 |  |
| Method cache dunder hits | 15,999,980 |  |
| Method cache dunder misses | 20 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20,700 | 1,920 | 140,038,280 |
| 1 | 1,880 | 0 | 152,873,400 |
| 2 | 160 | 0 | 118,249,240 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 60 |  |
| Traces created | 60 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
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
| <= 16 | 20 | 33.3% |
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 20 | 33.3% |
| <= 256 | 20 | 33.3% |


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
| <= 16 | 20 | 33.3% |
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 40 | 66.7% |


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
