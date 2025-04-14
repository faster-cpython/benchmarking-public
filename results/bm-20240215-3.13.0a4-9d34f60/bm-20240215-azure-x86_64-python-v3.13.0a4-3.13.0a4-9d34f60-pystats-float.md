
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
| LOAD_FAST | 495,999,520 | 25.0% | 25.0% |  |
| LOAD_ATTR_SLOT | 239,998,220 | 12.1% | 37.1% |  |
| STORE_FAST | 144,000,560 | 7.3% | 44.4% |  |
| STORE_ATTR_SLOT | 143,999,320 | 7.3% | 51.6% |  |
| BINARY_OP | 80,020,980 | 4.0% | 55.6% |  |
| LOAD_FAST_LOAD_FAST | 80,000,000 | 4.0% | 59.7% |  |
| LOAD_GLOBAL_MODULE | 64,000,180 | 3.2% | 62.9% |  |
| COPY | 64,000,000 | 3.2% | 66.1% |  |
| BINARY_OP_MULTIPLY_FLOAT | 63,999,920 | 3.2% | 69.4% |  |
| RESUME_CHECK | 48,000,120 | 2.4% | 71.8% | 0.0% |
| JUMP_BACKWARD | 48,000,000 | 2.4% | 74.2% |  |
| SWAP | 48,000,000 | 2.4% | 76.6% |  |
| CALL_BUILTIN_O | 47,999,940 | 2.4% | 79.0% |  |
| POP_JUMP_IF_FALSE | 47,999,600 | 2.4% | 81.5% |  |
| COMPARE_OP_FLOAT | 47,999,460 | 2.4% | 83.9% |  |
| LOAD_CONST | 32,000,720 | 1.6% | 85.5% |  |
| FOR_ITER_LIST | 32,000,120 | 1.6% | 87.1% |  |
| RETURN_CONST | 32,000,000 | 1.6% | 88.7% |  |
| BINARY_OP_ADD_FLOAT | 31,999,960 | 1.6% | 90.3% |  |
| CALL_PY_EXACT_ARGS | 31,999,940 | 1.6% | 91.9% |  |
| LOAD_ATTR_METHOD_NO_DICT | 31,999,800 | 1.6% | 93.5% |  |
| JUMP_FORWARD | 31,986,880 | 1.6% | 95.2% |  |
| CALL | 16,004,920 | 0.8% | 96.0% |  |
| FOR_ITER_RANGE | 16,000,360 | 0.8% | 96.8% |  |
| POP_TOP | 16,000,240 | 0.8% | 97.6% |  |
| RETURN_VALUE | 16,000,240 | 0.8% | 98.4% |  |
| INTERPRETER_EXIT | 16,000,160 | 0.8% | 99.2% |  |
| STORE_SUBSCR_LIST_INT | 15,999,980 | 0.8% | 100.0% |  |
| LOAD_ATTR | 840 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_SLOT | 191,998,000 | 9.7% | 9.7% |
| LOAD_ATTR_SLOT LOAD_FAST | 112,011,980 | 5.6% | 15.3% |
| LOAD_FAST STORE_ATTR_SLOT | 95,999,240 | 4.8% | 20.2% |
| STORE_FAST LOAD_FAST | 80,000,480 | 4.0% | 24.2% |
| STORE_ATTR_SLOT LOAD_FAST | 79,999,400 | 4.0% | 28.2% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 63,999,840 | 3.2% | 31.5% |
| LOAD_FAST BINARY_OP | 48,000,200 | 2.4% | 33.9% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 48,000,080 | 2.4% | 36.3% |
| BINARY_OP SWAP | 48,000,000 | 2.4% | 38.7% |
| LOAD_FAST COPY | 48,000,000 | 2.4% | 41.1% |
| LOAD_ATTR_SLOT STORE_FAST | 47,999,940 | 2.4% | 43.5% |
| COPY LOAD_ATTR_SLOT | 47,999,880 | 2.4% | 46.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 47,999,880 | 2.4% | 48.4% |
| SWAP STORE_ATTR_SLOT | 47,999,880 | 2.4% | 50.8% |
| POP_JUMP_IF_FALSE LOAD_FAST | 47,999,520 | 2.4% | 53.2% |
| COMPARE_OP_FLOAT POP_JUMP_IF_FALSE | 47,999,460 | 2.4% | 55.6% |
| LOAD_ATTR_SLOT COMPARE_OP_FLOAT | 47,999,400 | 2.4% | 58.1% |
| BINARY_OP LOAD_FAST | 32,000,000 | 1.6% | 59.7% |
| LOAD_CONST BINARY_OP | 32,000,000 | 1.6% | 61.3% |
| STORE_ATTR_SLOT RETURN_CONST | 31,999,960 | 1.6% | 62.9% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 31,999,940 | 1.6% | 64.5% |
| RESUME_CHECK LOAD_FAST | 31,999,940 | 1.6% | 66.1% |
| LOAD_FAST CALL_BUILTIN_O | 31,999,920 | 1.6% | 67.7% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 31,999,920 | 1.6% | 69.4% |
| JUMP_BACKWARD FOR_ITER_LIST | 31,999,800 | 1.6% | 71.0% |
| FOR_ITER_LIST STORE_FAST | 31,999,800 | 1.6% | 72.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 31,999,760 | 1.6% | 74.2% |
| JUMP_FORWARD LOAD_FAST | 31,986,880 | 1.6% | 75.8% |
| LOAD_ATTR_SLOT JUMP_FORWARD | 31,986,840 | 1.6% | 77.4% |
| LOAD_FAST CALL | 16,000,240 | 0.8% | 78.2% |
| POP_TOP JUMP_BACKWARD | 16,000,160 | 0.8% | 79.0% |
| CACHE RESUME_CHECK | 16,000,120 | 0.8% | 79.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 16,000,120 | 0.8% | 80.6% |
| FOR_ITER_RANGE STORE_FAST | 16,000,120 | 0.8% | 81.4% |
| LOAD_FAST RETURN_VALUE | 16,000,080 | 0.8% | 82.3% |
| CALL LOAD_FAST_LOAD_FAST | 16,000,000 | 0.8% | 83.1% |
| COPY LOAD_FAST | 16,000,000 | 0.8% | 83.9% |
| RETURN_CONST INTERPRETER_EXIT | 16,000,000 | 0.8% | 84.7% |
| RETURN_CONST POP_TOP | 16,000,000 | 0.8% | 85.5% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 16,000,000 | 0.8% | 86.3% |
| BINARY_OP_ADD_FLOAT LOAD_FAST_LOAD_FAST | 15,999,980 | 0.8% | 87.1% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_CONST | 15,999,980 | 0.8% | 87.9% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_LOAD_FAST | 15,999,980 | 0.8% | 88.7% |
| CALL_BUILTIN_O COPY | 15,999,980 | 0.8% | 89.5% |
| CALL_BUILTIN_O LOAD_CONST | 15,999,980 | 0.8% | 90.3% |
| CALL_BUILTIN_O STORE_FAST | 15,999,980 | 0.8% | 91.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 15,999,980 | 0.8% | 91.9% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 15,999,980 | 0.8% | 92.7% |
| STORE_ATTR_SLOT STORE_FAST | 15,999,980 | 0.8% | 93.5% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 15,999,980 | 0.8% | 94.4% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 15,999,960 | 0.8% | 95.2% |
| BINARY_OP_ADD_FLOAT CALL_BUILTIN_O | 15,999,960 | 0.8% | 96.0% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 15,999,960 | 0.8% | 96.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 15,999,920 | 0.8% | 97.6% |
| RETURN_VALUE STORE_FAST | 15,999,840 | 0.8% | 98.4% |
| STORE_FAST JUMP_BACKWARD | 15,999,840 | 0.8% | 99.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 15,999,820 | 0.8% | 100.0% |
| BINARY_OP BINARY_OP | 20,580 | 0.0% | 100.0% |
| CALL CALL | 4,200 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 640 | 0.0% | 100.0% |
| PUSH_NULL CALL | 400 | 0.0% | 100.0% |
| LOAD_FAST LOAD_CONST | 400 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_SLOT | 340 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 320 | 0.0% | 100.0% |
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
| LOAD_CONST BINARY_SLICE | 160 | 0.0% | 100.0% |
| LOAD_CONST BUILD_LIST | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 160 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 160 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 160 | 0.0% | 100.0% |
| FOR_ITER_LIST LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 140 | 0.0% | 100.0% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 140 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS GET_ITER | 140 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_CONST | 140 | 0.0% | 100.0% |
| CALL STORE_FAST | 120 | 0.0% | 100.0% |
| COPY LOAD_ATTR | 120 | 0.0% | 100.0% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 120 | 0.0% | 100.0% |
| STORE_ATTR LOAD_FAST | 120 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 120 | 0.0% | 100.0% |
| SWAP STORE_ATTR | 120 | 0.0% | 100.0% |
| FOR_ITER_LIST LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |
| GET_ITER FOR_ITER | 80 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |


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
| RETURN_CONST | 16,000,000 | 100.0% |
| CALL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,000,160 | 100.0% |
| NOP | 80 | 0.0% |


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
| LOAD_FAST | 16,000,080 | 100.0% |
| RETURN_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,999,840 | 100.0% |
| INTERPRETER_EXIT | 160 | 0.0% |
| RETURN_VALUE | 160 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


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
| LOAD_FAST | 48,000,200 | 60.0% |
| LOAD_CONST | 32,000,000 | 40.0% |
| BINARY_OP | 20,580 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 48,000,000 | 60.0% |
| LOAD_FAST | 32,000,000 | 40.0% |
| BINARY_OP | 20,580 | 0.0% |
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
| LOAD_FAST | 16,000,240 | 100.0% |
| CALL | 4,200 | 0.0% |
| PUSH_NULL | 400 | 0.0% |
| BINARY_OP | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

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
| LOAD_FAST | 48,000,000 | 75.0% |
| CALL_BUILTIN_O | 15,999,980 | 25.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 47,999,880 | 75.0% |
| LOAD_FAST | 16,000,000 | 25.0% |
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
| POP_TOP | 16,000,160 | 33.3% |
| STORE_SUBSCR_LIST_INT | 15,999,980 | 33.3% |
| STORE_FAST | 15,999,840 | 33.3% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 31,999,800 | 66.7% |
| FOR_ITER_RANGE | 16,000,120 | 33.3% |
| FOR_ITER | 80 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 31,986,840 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,986,880 | 100.0% |


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
| LOAD_ATTR_SLOT | 112,011,980 | 22.6% |
| STORE_FAST | 80,000,480 | 16.1% |
| STORE_ATTR_SLOT | 79,999,400 | 16.1% |
| LOAD_GLOBAL_MODULE | 48,000,080 | 9.7% |
| POP_JUMP_IF_FALSE | 47,999,520 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 191,998,000 | 38.7% |
| STORE_ATTR_SLOT | 95,999,240 | 19.4% |
| BINARY_OP | 48,000,200 | 9.7% |
| COPY | 48,000,000 | 9.7% |
| CALL_BUILTIN_O | 31,999,920 | 6.5% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 16,000,000 | 20.0% |
| BINARY_OP_ADD_FLOAT | 15,999,980 | 20.0% |
| BINARY_OP_MULTIPLY_FLOAT | 15,999,980 | 20.0% |
| LOAD_GLOBAL_MODULE | 15,999,980 | 20.0% |
| STORE_ATTR_SLOT | 15,999,980 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 63,999,840 | 80.0% |
| STORE_SUBSCR_LIST_INT | 15,999,960 | 20.0% |
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
| COMPARE_OP_FLOAT | 47,999,460 | 100.0% |
| COMPARE_OP | 80 | 0.0% |
| COMPARE_OP_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,999,520 | 100.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 31,999,960 | 100.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 16,000,000 | 50.0% |
| POP_TOP | 16,000,000 | 50.0% |


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
| LOAD_ATTR_SLOT | 47,999,940 | 33.3% |
| FOR_ITER_LIST | 31,999,800 | 22.2% |
| FOR_ITER_RANGE | 16,000,120 | 11.1% |
| CALL_BUILTIN_O | 15,999,980 | 11.1% |
| STORE_ATTR_SLOT | 15,999,980 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,000,480 | 55.6% |
| LOAD_GLOBAL_MODULE | 47,999,880 | 33.3% |
| JUMP_BACKWARD | 15,999,840 | 11.1% |
| LOAD_GLOBAL | 160 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 48,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 47,999,880 | 100.0% |
| STORE_ATTR | 120 | 0.0% |


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
| BINARY_OP_MULTIPLY_FLOAT | 31,999,920 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 15,999,980 | 50.0% |
| CALL_BUILTIN_O | 15,999,960 | 50.0% |
| CALL | 20 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 63,999,840 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 31,999,920 | 50.0% |
| LOAD_CONST | 15,999,980 | 25.0% |
| LOAD_FAST_LOAD_FAST | 15,999,980 | 25.0% |
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
| LOAD_FAST | 31,999,920 | 66.7% |
| BINARY_OP_ADD_FLOAT | 15,999,960 | 33.3% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 15,999,980 | 33.3% |
| LOAD_CONST | 15,999,980 | 33.3% |
| STORE_FAST | 15,999,980 | 33.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 15,999,960 | 50.0% |
| LOAD_FAST | 15,999,920 | 50.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 31,999,940 | 100.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 47,999,400 | 100.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 47,999,460 | 100.0% |


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
| JUMP_BACKWARD | 31,999,800 | 100.0% |
| GET_ITER | 280 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 31,999,800 | 100.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,000,120 | 100.0% |
| GET_ITER | 200 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,000,120 | 100.0% |
| LOAD_FAST | 240 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,999,760 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 15,999,960 | 50.0% |
| LOAD_FAST | 15,999,820 | 50.0% |
| CALL | 20 | 0.0% |


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
| LOAD_FAST | 191,998,000 | 80.0% |
| COPY | 47,999,880 | 20.0% |
| LOAD_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 112,011,980 | 46.7% |
| STORE_FAST | 47,999,940 | 20.0% |
| COMPARE_OP_FLOAT | 47,999,400 | 20.0% |
| JUMP_FORWARD | 31,986,840 | 13.3% |
| COMPARE_OP | 60 | 0.0% |


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
| STORE_FAST | 47,999,880 | 75.0% |
| RESUME_CHECK | 16,000,000 | 25.0% |
| LOAD_GLOBAL | 140 | 0.0% |
| FOR_ITER_LIST | 120 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,000,080 | 75.0% |
| LOAD_FAST_LOAD_FAST | 15,999,980 | 25.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 31,999,940 | 66.7% |
| CACHE | 16,000,120 | 33.3% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,999,940 | 66.7% |
| LOAD_GLOBAL_MODULE | 16,000,000 | 33.3% |
| LOAD_CONST | 140 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,999,240 | 66.7% |
| SWAP | 47,999,880 | 33.3% |
| STORE_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,999,400 | 55.6% |
| RETURN_CONST | 31,999,960 | 22.2% |
| LOAD_FAST_LOAD_FAST | 15,999,980 | 11.1% |
| STORE_FAST | 15,999,980 | 11.1% |


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
| JUMP_BACKWARD | 15,999,980 | 100.0% |


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
|     deferred | 80,000,300 | 45.4% |
|          hit | 95,999,940 | 54.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 0.7% |
| Failure | 20,540 | 99.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| true divide float | 12,300 | 59.9% |
| multiply different types | 4,140 | 20.2% |
| true divide different types | 4,100 | 20.0% |


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
|     deferred | 80 | 0.0% |
|          hit | 48,000,480 | 100.0% |

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
|          hit | 64,000,380 | 100.0% |

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
| Basic | 1,023,990,040 | 51.6% |
| Not specialized | 144,027,660 | 7.3% |
| Specialized hits | 815,975,360 | 41.1% |
| Specialized misses | 22,740 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 80,000,300 | 83.3% |
| CALL | 16,000,560 | 16.7% |
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
| Frames pushed | 31,999,940 | 66.7% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 192,013,720 | 70.6% |
| Frees to freelist | 192,016,620 |  |
| Allocations | 79,992,780 | 29.4% |
| Allocations to 512 bytes | 79,992,460 | 29.4% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 320 | 0.0% |
| Frees | 79,999,710 |  |
| New values | 0 |  |
| Interpreter increfs | 1,183,793,040 | 94.9% |
| Interpreter decrefs | 1,343,754,380 | 88.4% |
| Increfs | 63,961,600 | 5.1% |
| Decrefs | 176,012,135 | 11.6% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 1,078 |  |
| Method cache misses | 122 |  |
| Method cache collisions | 106 |  |
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
