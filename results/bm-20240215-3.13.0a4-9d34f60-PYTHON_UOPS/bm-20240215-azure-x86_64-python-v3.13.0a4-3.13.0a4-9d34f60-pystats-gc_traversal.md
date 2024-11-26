
# Pystats results

- benchmark: gc_traversal
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| ENTER_EXECUTOR | 161,740 | 34.1% | 34.1% |  |
| LOAD_FAST | 92,140 | 19.4% | 53.5% |  |
| STORE_FAST | 89,660 | 18.9% | 72.4% |  |
| FOR_ITER_RANGE | 81,440 | 17.2% | 89.5% |  |
| PUSH_NULL | 6,160 | 1.3% | 90.8% |  |
| LOAD_GLOBAL_MODULE | 5,960 | 1.3% | 92.1% |  |
| LOAD_ATTR_MODULE | 5,900 | 1.2% | 93.3% |  |
| CALL | 5,700 | 1.2% | 94.5% |  |
| LOAD_CONST | 3,040 | 0.6% | 95.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,920 | 0.6% | 95.8% |  |
| POP_JUMP_IF_FALSE | 2,560 | 0.5% | 96.3% |  |
| POP_JUMP_IF_NOT_NONE | 2,560 | 0.5% | 96.9% |  |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.5% | 97.4% | 2.4% |
| BINARY_OP_SUBTRACT_FLOAT | 2,540 | 0.5% | 97.9% |  |
| COMPARE_OP_INT | 2,540 | 0.5% | 98.5% |  |
| JUMP_BACKWARD | 1,020 | 0.2% | 98.7% |  |
| GET_ITER | 560 | 0.1% | 98.8% |  |
| BUILD_LIST | 560 | 0.1% | 98.9% |  |
| BINARY_OP | 540 | 0.1% | 99.0% |  |
| LOAD_FAST_LOAD_FAST | 540 | 0.1% | 99.2% |  |
| STORE_SUBSCR_LIST_INT | 520 | 0.1% | 99.3% |  |
| CALL_BUILTIN_CLASS | 500 | 0.1% | 99.4% |  |
| LOAD_GLOBAL_BUILTIN | 500 | 0.1% | 99.5% |  |
| POP_TOP | 480 | 0.1% | 99.6% |  |
| LOAD_GLOBAL | 360 | 0.1% | 99.7% |  |
| RETURN_VALUE | 240 | 0.1% | 99.7% |  |
| LOAD_DEREF | 240 | 0.1% | 99.8% |  |
| LOAD_ATTR | 200 | 0.0% | 99.8% |  |
| RESUME_CHECK | 180 | 0.0% | 99.8% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 99.9% |  |
| FOR_ITER | 120 | 0.0% | 99.9% |  |
| NOP | 80 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 99.9% |  |
| COPY_FREE_VARS | 80 | 0.0% | 99.9% |  |
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
| FOR_ITER_RANGE LOAD_FAST | 80,140 | 16.9% | 16.9% |
| LOAD_FAST STORE_FAST | 80,000 | 16.9% | 33.7% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 79,980 | 16.9% | 50.6% |
| STORE_FAST ENTER_EXECUTOR | 79,660 | 16.8% | 67.4% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 79,600 | 16.8% | 84.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 5,900 | 1.2% | 85.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 5,800 | 1.2% | 86.6% |
| STORE_FAST LOAD_FAST | 5,120 | 1.1% | 87.7% |
| PUSH_NULL CALL | 3,120 | 0.7% | 88.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,920 | 0.6% | 89.0% |
| PUSH_NULL CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,880 | 0.6% | 89.6% |
| CALL STORE_FAST | 2,580 | 0.5% | 90.1% |
| CALL LOAD_FAST | 2,560 | 0.5% | 90.6% |
| LOAD_FAST LOAD_CONST | 2,560 | 0.5% | 91.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,560 | 0.5% | 91.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,560 | 0.5% | 92.3% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 2,540 | 0.5% | 92.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 2,540 | 0.5% | 93.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 2,540 | 0.5% | 93.9% |
| LOAD_CONST COMPARE_OP_INT | 2,520 | 0.5% | 94.4% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 2,520 | 0.5% | 94.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,520 | 0.5% | 95.5% |
| BINARY_OP_SUBTRACT_FLOAT BINARY_OP_ADD_FLOAT | 2,520 | 0.5% | 96.0% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 2,220 | 0.5% | 96.5% |
| ENTER_EXECUTOR CALL | 2,160 | 0.5% | 96.9% |
| FOR_ITER_RANGE STORE_FAST | 1,300 | 0.3% | 97.2% |
| JUMP_BACKWARD FOR_ITER_RANGE | 920 | 0.2% | 97.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 540 | 0.1% | 97.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 540 | 0.1% | 97.6% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 500 | 0.1% | 97.7% |
| CALL_BUILTIN_CLASS GET_ITER | 500 | 0.1% | 97.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 500 | 0.1% | 97.9% |
| GET_ITER FOR_ITER_RANGE | 480 | 0.1% | 98.0% |
| LOAD_FAST BINARY_OP | 440 | 0.1% | 98.1% |
| LOAD_FAST CALL_BUILTIN_CLASS | 440 | 0.1% | 98.2% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 440 | 0.1% | 98.3% |
| BINARY_OP STORE_FAST | 420 | 0.1% | 98.4% |
| BUILD_LIST LOAD_FAST | 400 | 0.1% | 98.5% |
| LOAD_CONST BUILD_LIST | 400 | 0.1% | 98.6% |
| STORE_FAST LOAD_CONST | 400 | 0.1% | 98.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 380 | 0.1% | 98.7% |
| POP_TOP LOAD_GLOBAL_MODULE | 360 | 0.1% | 98.8% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 340 | 0.1% | 98.9% |
| STORE_FAST JUMP_BACKWARD | 340 | 0.1% | 99.0% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 320 | 0.1% | 99.0% |
| CALL CALL | 260 | 0.1% | 99.1% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.1% | 99.1% |
| STORE_SUBSCR_LIST_INT ENTER_EXECUTOR | 200 | 0.0% | 99.2% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 99.2% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 99.2% |
| LOAD_FAST RETURN_VALUE | 160 | 0.0% | 99.3% |
| LOAD_FAST CALL | 160 | 0.0% | 99.3% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 120 | 0.0% | 99.3% |
| CALL POP_TOP | 100 | 0.0% | 99.3% |
| LOAD_ATTR PUSH_NULL | 100 | 0.0% | 99.4% |
| LOAD_ATTR LOAD_ATTR_MODULE | 100 | 0.0% | 99.4% |
| LOAD_GLOBAL LOAD_ATTR | 100 | 0.0% | 99.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 100 | 0.0% | 99.4% |
| GET_ITER FOR_ITER | 80 | 0.0% | 99.4% |
| NOP LOAD_DEREF | 80 | 0.0% | 99.5% |
| POP_TOP NOP | 80 | 0.0% | 99.5% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 99.5% |
| RETURN_VALUE STORE_FAST | 80 | 0.0% | 99.5% |
| BINARY_OP BINARY_OP | 80 | 0.0% | 99.5% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 99.5% |
| BUILD_LIST STORE_FAST | 80 | 0.0% | 99.6% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 99.6% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 99.6% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 99.6% |
| LOAD_CONST STORE_FAST | 80 | 0.0% | 99.6% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 99.7% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 99.7% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 99.7% |
| LOAD_GLOBAL LOAD_FAST | 80 | 0.0% | 99.7% |
| CALL GET_ITER | 60 | 0.0% | 99.7% |
| CALL CALL_BUILTIN_CLASS | 60 | 0.0% | 99.7% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.0% | 99.7% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.0% | 99.8% |
| FOR_ITER FOR_ITER_RANGE | 60 | 0.0% | 99.8% |
| JUMP_BACKWARD ENTER_EXECUTOR | 60 | 0.0% | 99.8% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 60 | 0.0% | 99.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 60 | 0.0% | 99.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 60 | 0.0% | 99.8% |
| RESUME_CHECK BUILD_LIST | 60 | 0.0% | 99.8% |
| RESUME_CHECK LOAD_CONST | 60 | 0.0% | 99.8% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.0% | 99.9% |
| POP_TOP LOAD_GLOBAL | 40 | 0.0% | 99.9% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.0% | 99.9% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.9% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 0.0% | 99.9% |
| FOR_ITER STORE_FAST | 40 | 0.0% | 99.9% |
| JUMP_BACKWARD FOR_ITER | 40 | 0.0% | 99.9% |
| LOAD_CONST COMPARE_OP | 40 | 0.0% | 99.9% |
| LOAD_FAST STORE_SUBSCR | 40 | 0.0% | 99.9% |
| LOAD_FAST LOAD_GLOBAL | 40 | 0.0% | 99.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 40 | 0.0% | 99.9% |
| STORE_SUBSCR JUMP_BACKWARD | 20 | 0.0% | 99.9% |
| STORE_SUBSCR STORE_SUBSCR_LIST_INT | 20 | 0.0% | 99.9% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 20 | 0.0% | 99.9% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 500 | 89.3% |
| CALL | 60 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 480 | 85.7% |
| FOR_ITER | 80 | 14.3% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 380 | 79.2% |
| CALL | 100 | 20.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 360 | 75.0% |
| NOP | 80 | 16.7% |
| LOAD_GLOBAL | 40 | 8.3% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 5,900 | 95.8% |
| LOAD_DEREF | 160 | 2.6% |
| LOAD_ATTR | 100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,120 | 50.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,880 | 46.8% |
| LOAD_FAST | 160 | 2.6% |


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
| LOAD_FAST | 440 | 81.5% |
| BINARY_OP | 80 | 14.8% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 420 | 77.8% |
| BINARY_OP | 80 | 14.8% |
| BINARY_OP_ADD_FLOAT | 20 | 3.7% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 3.7% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 400 | 71.4% |
| LOAD_FAST | 80 | 14.3% |
| RESUME_CHECK | 60 | 10.7% |
| RESUME | 20 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 71.4% |
| LOAD_DEREF | 80 | 14.3% |
| STORE_FAST | 80 | 14.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 3,120 | 54.7% |
| ENTER_EXECUTOR | 2,160 | 37.9% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 79,660 | 49.3% |
| ENTER_EXECUTOR | 79,600 | 49.2% |
| POP_JUMP_IF_FALSE | 2,220 | 1.4% |
| STORE_SUBSCR_LIST_INT | 200 | 0.1% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 79,980 | 49.4% |
| ENTER_EXECUTOR | 79,600 | 49.2% |
| CALL | 2,160 | 1.3% |


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
| POP_JUMP_IF_FALSE | 340 | 33.3% |
| STORE_FAST | 340 | 33.3% |
| STORE_SUBSCR_LIST_INT | 320 | 31.4% |
| STORE_SUBSCR | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 920 | 90.2% |
| ENTER_EXECUTOR | 60 | 5.9% |
| FOR_ITER | 40 | 3.9% |


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
| LOAD_FAST | 2,560 | 84.2% |
| STORE_FAST | 400 | 13.2% |
| RESUME_CHECK | 60 | 2.0% |
| RESUME | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 2,520 | 82.9% |
| BUILD_LIST | 400 | 13.2% |
| STORE_FAST | 80 | 2.6% |
| COMPARE_OP | 40 | 1.3% |


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
| FOR_ITER_RANGE | 80,140 | 87.0% |
| STORE_FAST | 5,120 | 5.6% |
| CALL | 2,560 | 2.8% |
| POP_JUMP_IF_NOT_NONE | 2,560 | 2.8% |
| LOAD_FAST_LOAD_FAST | 540 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80,000 | 86.8% |
| LOAD_CONST | 2,560 | 2.8% |
| POP_JUMP_IF_NOT_NONE | 2,560 | 2.8% |
| BINARY_OP_SUBTRACT_FLOAT | 2,520 | 2.7% |
| LOAD_GLOBAL_MODULE | 2,520 | 2.7% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 100.0% |


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
| ENTER_EXECUTOR | 2,220 | 86.7% |
| JUMP_BACKWARD | 340 | 13.3% |


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
| LOAD_FAST | 80,000 | 89.2% |
| CALL | 2,580 | 2.9% |
| BINARY_OP_ADD_FLOAT | 2,540 | 2.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,540 | 2.8% |
| FOR_ITER_RANGE | 1,300 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 79,660 | 88.8% |
| LOAD_FAST | 5,120 | 5.7% |
| LOAD_GLOBAL_MODULE | 2,920 | 3.3% |
| LOAD_FAST_LOAD_FAST | 540 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 440 | 0.5% |


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
| LOAD_FAST | 440 | 88.0% |
| CALL | 60 | 12.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 500 | 100.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,880 | 98.6% |
| CALL | 40 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 87.0% |
| POP_TOP | 380 | 13.0% |


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
| ENTER_EXECUTOR | 79,980 | 98.2% |
| JUMP_BACKWARD | 920 | 1.1% |
| GET_ITER | 480 | 0.6% |
| FOR_ITER | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,140 | 98.4% |
| STORE_FAST | 1,300 | 1.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,800 | 98.3% |
| LOAD_ATTR | 100 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 5,900 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 440 | 88.0% |
| LOAD_GLOBAL | 60 | 12.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,920 | 49.0% |
| LOAD_FAST | 2,520 | 42.3% |
| POP_TOP | 360 | 6.0% |
| LOAD_GLOBAL | 120 | 2.0% |
| RETURN_VALUE | 40 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 5,800 | 97.3% |
| LOAD_ATTR | 100 | 1.7% |
| LOAD_FAST | 60 | 1.0% |


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
| LOAD_FAST | 500 | 96.2% |
| STORE_SUBSCR | 20 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 320 | 61.5% |
| ENTER_EXECUTOR | 200 | 38.5% |


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
|     deferred | 500 | 8.9% |
|          hit | 5,020 | 89.3% |
|         miss | 60 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 40.0% |
| Failure | 60 | 60.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 60 | 100.0% |


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
|     deferred | 60 | 0.1% |
|          hit | 81,440 | 99.9% |

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
|     deferred | 180 | 2.6% |
|          hit | 6,460 | 94.7% |

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
| Basic | 356,920 | 75.2% |
| Not specialized | 12,120 | 2.6% |
| Specialized hits | 105,540 | 22.2% |
| Specialized misses | 60 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 5,320 | 85.8% |
| BINARY_OP | 500 | 8.1% |
| LOAD_GLOBAL | 180 | 2.9% |
| LOAD_ATTR | 100 | 1.6% |
| FOR_ITER | 60 | 1.0% |
| STORE_SUBSCR | 20 | 0.3% |
| COMPARE_OP | 20 | 0.3% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| BINARY_SUBSCR | 0 | 0.0% |


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
| Frames pushed | 240 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 85,840 | 0.4% |
| Frees to freelist | 92,420 |  |
| Allocations | 22,581,640 | 99.6% |
| Allocations to 512 bytes | 22,506,740 | 99.3% |
| Allocations to 4 kbytes | 35,860 | 0.2% |
| Allocations over 4 kbytes | 39,040 | 0.2% |
| Frees | 22,589,006 |  |
| New values | 0 |  |
| Interpreter increfs | 261,040 | 0.3% |
| Interpreter decrefs | 349,840 | 0.3% |
| Increfs | 102,218,840 | 99.7% |
| Decrefs | 124,643,146 | 99.7% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 74 |  |
| Method cache misses | 26 |  |
| Method cache collisions | 26 |  |
| Method cache dunder hits | 0 |  |
| Method cache dunder misses | 0 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 100 | 1,920 | 51,002,520 |
| 1 | 0 | 0 | 0 |
| 2 | 5,120 | 0 | 5,701,599,840 |


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
| Inner loop found | 20 | 33.3% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 40 | 66.7% |
| <= 64 | 20 | 33.3% |


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
| <= 32 | 20 | 33.3% |
| <= 64 | 20 | 33.3% |


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
