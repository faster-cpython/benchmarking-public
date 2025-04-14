
# Pystats results

- benchmark: gc_traversal
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 40,210,800 | 16.7% | 16.7% |  |
| STORE_FAST | 40,210,480 | 16.7% | 33.4% |  |
| FOR_ITER_RANGE | 40,122,660 | 16.6% | 50.0% |  |
| JUMP_BACKWARD | 40,042,560 | 16.6% | 66.6% |  |
| LOAD_FAST_LOAD_FAST | 39,960,000 | 16.6% | 83.2% |  |
| STORE_SUBSCR_LIST_INT | 39,959,980 | 16.6% | 99.8% |  |
| LOAD_CONST | 82,640 | 0.0% | 99.8% |  |
| BINARY_OP | 80,280 | 0.0% | 99.8% |  |
| GET_ITER | 80,160 | 0.0% | 99.9% |  |
| BUILD_LIST | 80,160 | 0.0% | 99.9% |  |
| CALL_BUILTIN_CLASS | 80,100 | 0.0% | 99.9% |  |
| LOAD_GLOBAL_BUILTIN | 80,100 | 0.0% | 100.0% |  |
| PUSH_NULL | 10,480 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 10,280 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 10,220 | 0.0% | 100.0% |  |
| CALL | 5,700 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,080 | 0.0% | 100.0% |  |
| POP_TOP | 2,640 | 0.0% | 100.0% |  |
| POP_JUMP_IF_FALSE | 2,560 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NOT_NONE | 2,560 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% | 100.0% | 2.4% |
| BINARY_OP_SUBTRACT_FLOAT | 2,540 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 2,540 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 360 | 0.0% | 100.0% |  |
| RETURN_VALUE | 240 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| LOAD_ATTR | 200 | 0.0% | 100.0% |  |
| RESUME_CHECK | 180 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| RESUME | 60 | 0.0% | 100.0% |  |
| CALL_PY_EXACT_ARGS | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |
| COMPARE_OP | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| JUMP_BACKWARD FOR_ITER_RANGE | 40,042,520 | 16.6% | 16.6% |
| FOR_ITER_RANGE STORE_FAST | 40,042,520 | 16.6% | 33.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 39,960,000 | 16.6% | 49.8% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 39,960,000 | 16.6% | 66.4% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 39,959,980 | 16.6% | 83.0% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 39,959,960 | 16.6% | 99.5% |
| FOR_ITER_RANGE LOAD_FAST | 80,140 | 0.0% | 99.6% |
| CALL_BUILTIN_CLASS GET_ITER | 80,100 | 0.0% | 99.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 80,100 | 0.0% | 99.6% |
| GET_ITER FOR_ITER_RANGE | 80,080 | 0.0% | 99.7% |
| LOAD_FAST BINARY_OP | 80,040 | 0.0% | 99.7% |
| LOAD_FAST CALL_BUILTIN_CLASS | 80,040 | 0.0% | 99.7% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 80,040 | 0.0% | 99.8% |
| BINARY_OP STORE_FAST | 80,020 | 0.0% | 99.8% |
| BUILD_LIST LOAD_FAST | 80,000 | 0.0% | 99.8% |
| LOAD_CONST BUILD_LIST | 80,000 | 0.0% | 99.9% |
| LOAD_FAST STORE_FAST | 80,000 | 0.0% | 99.9% |
| STORE_FAST JUMP_BACKWARD | 80,000 | 0.0% | 99.9% |
| STORE_FAST LOAD_CONST | 80,000 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 10,220 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 10,120 | 0.0% | 100.0% |
| PUSH_NULL CALL | 5,280 | 0.0% | 100.0% |
| STORE_FAST LOAD_FAST | 5,120 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 5,080 | 0.0% | 100.0% |
| PUSH_NULL CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,040 | 0.0% | 100.0% |
| CALL STORE_FAST | 2,580 | 0.0% | 100.0% |
| CALL LOAD_FAST | 2,560 | 0.0% | 100.0% |
| LOAD_FAST LOAD_CONST | 2,560 | 0.0% | 100.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,560 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 2,560 | 0.0% | 100.0% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,560 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 2,540 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 2,540 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 2,540 | 0.0% | 100.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 2,540 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL_MODULE | 2,520 | 0.0% | 100.0% |
| LOAD_CONST COMPARE_OP_INT | 2,520 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 2,520 | 0.0% | 100.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,520 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_FLOAT BINARY_OP_ADD_FLOAT | 2,520 | 0.0% | 100.0% |
| CALL CALL | 260 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 220 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |
| CALL POP_TOP | 100 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 100 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_MODULE | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 100 | 0.0% | 100.0% |
| GET_ITER FOR_ITER | 80 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 100.0% |
| RETURN_VALUE STORE_FAST | 80 | 0.0% | 100.0% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 100.0% |
| BUILD_LIST STORE_FAST | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |
| LOAD_CONST STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 100.0% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 80 | 0.0% | 100.0% |
| CALL GET_ITER | 60 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 60 | 0.0% | 100.0% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.0% | 100.0% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.0% | 100.0% |
| FOR_ITER FOR_ITER_RANGE | 60 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 60 | 0.0% | 100.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 60 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 60 | 0.0% | 100.0% |
| RESUME_CHECK BUILD_LIST | 60 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_CONST | 60 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL | 40 | 0.0% | 100.0% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.0% | 100.0% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 0.0% | 100.0% |
| FOR_ITER STORE_FAST | 40 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER | 40 | 0.0% | 100.0% |
| LOAD_CONST COMPARE_OP | 40 | 0.0% | 100.0% |
| LOAD_FAST STORE_SUBSCR | 40 | 0.0% | 100.0% |
| LOAD_FAST LOAD_GLOBAL | 40 | 0.0% | 100.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 40 | 0.0% | 100.0% |
| STORE_SUBSCR JUMP_BACKWARD | 20 | 0.0% | 100.0% |
| STORE_SUBSCR STORE_SUBSCR_LIST_INT | 20 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 20 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% | 100.0% |
| CALL RESUME | 20 | 0.0% | 100.0% |
| CALL CALL_PY_EXACT_ARGS | 20 | 0.0% | 100.0% |
| CALL_FUNCTION_EX RESUME | 20 | 0.0% | 100.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 20 | 0.0% | 100.0% |
| COMPARE_OP COMPARE_OP_INT | 20 | 0.0% | 100.0% |
| COPY_FREE_VARS RESUME | 20 | 0.0% | 100.0% |
| FOR_ITER LOAD_FAST | 20 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 80,100 | 99.9% |
| CALL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 80,080 | 99.9% |
| FOR_ITER | 80 | 0.1% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,540 | 96.2% |
| CALL | 100 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,520 | 95.5% |
| NOP | 80 | 3.0% |
| LOAD_GLOBAL | 40 | 1.5% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 10,220 | 97.5% |
| LOAD_DEREF | 160 | 1.5% |
| LOAD_ATTR | 100 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,280 | 50.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,040 | 48.1% |
| LOAD_FAST | 160 | 1.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 66.7% |
| RETURN_VALUE | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 33.3% |
| STORE_FAST | 80 | 33.3% |
| LOAD_GLOBAL | 40 | 16.7% |
| LOAD_GLOBAL_MODULE | 40 | 16.7% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

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
| LOAD_FAST | 80,040 | 99.7% |
| BINARY_OP | 220 | 0.3% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80,020 | 99.7% |
| BINARY_OP | 220 | 0.3% |
| BINARY_OP_ADD_FLOAT | 20 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80,000 | 99.8% |
| LOAD_FAST | 80 | 0.1% |
| RESUME_CHECK | 60 | 0.1% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,000 | 99.8% |
| LOAD_DEREF | 80 | 0.1% |
| STORE_FAST | 80 | 0.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 5,280 | 92.6% |
| CALL | 260 | 4.6% |
| LOAD_FAST | 160 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,580 | 45.3% |
| LOAD_FAST | 2,560 | 44.9% |
| CALL | 260 | 4.6% |
| POP_TOP | 100 | 1.8% |
| GET_ITER | 60 | 1.1% |


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
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 50.0% |
| COMPARE_OP_INT | 20 | 50.0% |


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
| GET_ITER | 80 | 66.7% |
| JUMP_BACKWARD | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 60 | 50.0% |
| STORE_FAST | 40 | 33.3% |
| LOAD_FAST | 20 | 16.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 39,959,980 | 99.8% |
| STORE_FAST | 80,000 | 0.2% |
| POP_JUMP_IF_FALSE | 2,560 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 40,042,520 | 100.0% |
| FOR_ITER | 40 | 0.0% |


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
| LOAD_GLOBAL | 100 | 50.0% |
| LOAD_GLOBAL_MODULE | 100 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 100 | 50.0% |
| LOAD_ATTR_MODULE | 100 | 50.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80,000 | 96.8% |
| LOAD_FAST | 2,560 | 3.1% |
| RESUME_CHECK | 60 | 0.1% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 80,000 | 96.8% |
| COMPARE_OP_INT | 2,520 | 3.0% |
| STORE_FAST | 80 | 0.1% |
| COMPARE_OP | 40 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 33.3% |
| BUILD_LIST | 80 | 33.3% |
| RESUME_CHECK | 60 | 25.0% |
| RESUME | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 160 | 66.7% |
| LIST_EXTEND | 80 | 33.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 39,960,000 | 99.4% |
| FOR_ITER_RANGE | 80,140 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 80,100 | 0.2% |
| BUILD_LIST | 80,000 | 0.2% |
| STORE_FAST | 5,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 39,959,960 | 99.4% |
| BINARY_OP | 80,040 | 0.2% |
| CALL_BUILTIN_CLASS | 80,040 | 0.2% |
| STORE_FAST | 80,000 | 0.2% |
| LOAD_CONST | 2,560 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 39,960,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,960,000 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 66.7% |
| POP_TOP | 40 | 11.1% |
| RETURN_VALUE | 40 | 11.1% |
| LOAD_FAST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 33.3% |
| LOAD_ATTR | 100 | 27.8% |
| LOAD_FAST | 80 | 22.2% |
| LOAD_GLOBAL_BUILTIN | 60 | 16.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 2,540 | 99.2% |
| COMPARE_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,560 | 100.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 40,042,520 | 99.6% |
| BINARY_OP | 80,020 | 0.2% |
| LOAD_FAST | 80,000 | 0.2% |
| CALL | 2,580 | 0.0% |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 39,960,000 | 99.4% |
| LOAD_GLOBAL_BUILTIN | 80,040 | 0.2% |
| JUMP_BACKWARD | 80,000 | 0.2% |
| LOAD_CONST | 80,000 | 0.2% |
| LOAD_FAST | 5,120 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 33.3% |
| CALL_FUNCTION_EX | 20 | 33.3% |
| COPY_FREE_VARS | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 20 | 33.3% |
| LOAD_CONST | 20 | 33.3% |
| LOAD_DEREF | 20 | 33.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 2,520 | 99.2% |
| BINARY_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,520 | 99.2% |
| BINARY_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 2,520 | 99.2% |
| BINARY_OP | 20 | 0.8% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,040 | 99.9% |
| CALL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80,100 | 100.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 5,040 | 99.2% |
| CALL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,540 | 50.0% |
| STORE_FAST | 2,540 | 50.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,520 | 99.2% |
| COMPARE_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,540 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 40,042,520 | 99.8% |
| GET_ITER | 80,080 | 0.2% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40,042,520 | 99.8% |
| LOAD_FAST | 80,140 | 0.2% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,120 | 99.0% |
| LOAD_ATTR | 100 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 10,220 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80,040 | 99.9% |
| LOAD_GLOBAL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,100 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,080 | 49.4% |
| POP_TOP | 2,520 | 24.5% |
| LOAD_FAST | 2,520 | 24.5% |
| LOAD_GLOBAL | 120 | 1.2% |
| RETURN_VALUE | 40 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 10,120 | 98.4% |
| LOAD_ATTR | 100 | 1.0% |
| LOAD_FAST | 60 | 0.6% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 60 | 33.3% |
| COPY_FREE_VARS | 60 | 33.3% |
| CALL_PY_EXACT_ARGS | 60 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 60 | 33.3% |
| LOAD_CONST | 60 | 33.3% |
| LOAD_DEREF | 60 | 33.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,959,960 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 39,959,980 | 100.0% |


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
|     deferred | 80,040 | 93.8% |
|          hit | 5,020 | 5.9% |
|         miss | 60 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 16.7% |
| Failure | 200 | 83.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 200 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,320 | 5.9% |
|          hit | 85,240 | 93.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 31.6% |
| Failure | 260 | 68.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 260 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.8% |
|          hit | 2,540 | 98.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 40,122,660 | 100.0% |

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
|     deferred | 100 | 1.0% |
|          hit | 10,220 | 98.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 0.2% |
|          hit | 90,380 | 99.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
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

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 39,959,980 | 100.0% |

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
| Basic | 160,680,940 | 66.7% |
| Not specialized | 91,860 | 0.0% |
| Specialized hits | 80,276,220 | 33.3% |
| Specialized misses | 60 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 80,040 | 93.4% |
| CALL | 5,320 | 6.2% |
| LOAD_GLOBAL | 180 | 0.2% |
| LOAD_ATTR | 100 | 0.1% |
| FOR_ITER | 60 | 0.1% |
| STORE_SUBSCR | 20 | 0.0% |
| COMPARE_OP | 20 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 60 | 100.0% |
| GET_ITER | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |
| RETURN_VALUE | 0 | 0.0% |
| BUILD_LIST | 0 | 0.0% |
| CALL_FUNCTION_EX | 0 | 0.0% |
| CALL_INTRINSIC_1 | 0 | 0.0% |
| COPY_FREE_VARS | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 0 | 0.0% |
| Calls to Python functions inlined | 240 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 66.7% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 60 | 25.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 85,840 | 0.4% |
| Frees to freelist | 92,420 |  |
| Allocations | 22,581,580 | 99.6% |
| Allocations to 512 bytes | 22,506,700 | 99.3% |
| Allocations to 4 kbytes | 35,840 | 0.2% |
| Allocations over 4 kbytes | 39,040 | 0.2% |
| Frees | 22,588,982 |  |
| New values | 0 |  |
| Interpreter increfs | 102,197,980 | 99.9% |
| Interpreter decrefs | 84,675,480 | 67.8% |
| Increfs | 120,060 | 0.1% |
| Decrefs | 40,155,662 | 32.2% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 78 |  |
| Method cache misses | 22 |  |
| Method cache collisions | 22 |  |
| Method cache dunder hits | 0 |  |
| Method cache dunder misses | 0 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 100 | 1,920 | 51,552,680 |
| 1 | 0 | 0 | 0 |
| 2 | 5,120 | 0 | 5,709,515,040 |


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
