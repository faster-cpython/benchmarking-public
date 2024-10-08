
# Pystats results

- benchmark: pickle
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| ENTER_EXECUTOR | 81,500 | 42.2% | 42.2% |  |
| FOR_ITER_TUPLE | 41,560 | 21.5% | 63.8% |  |
| LOAD_FAST | 13,360 | 6.9% | 70.7% |  |
| PUSH_NULL | 12,800 | 6.6% | 77.3% |  |
| POP_TOP | 12,480 | 6.5% | 83.8% |  |
| LOAD_FAST_LOAD_FAST | 12,400 | 6.4% | 90.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 12,000 | 6.2% | 96.5% |  |
| STORE_FAST | 1,420 | 0.7% | 97.2% |  |
| CALL | 1,140 | 0.6% | 97.8% |  |
| JUMP_BACKWARD | 680 | 0.4% | 98.1% |  |
| GET_ITER | 480 | 0.2% | 98.4% |  |
| FOR_ITER_RANGE | 460 | 0.2% | 98.6% |  |
| LOAD_GLOBAL_MODULE | 360 | 0.2% | 98.8% |  |
| LOAD_GLOBAL | 280 | 0.1% | 99.0% |  |
| LOAD_DEREF | 240 | 0.1% | 99.1% |  |
| LOAD_ATTR_MODULE | 240 | 0.1% | 99.2% |  |
| LOAD_ATTR | 200 | 0.1% | 99.3% |  |
| RETURN_VALUE | 160 | 0.1% | 99.4% |  |
| CALL_FUNCTION_EX | 160 | 0.1% | 99.5% |  |
| RESUME_CHECK | 120 | 0.1% | 99.5% |  |
| NOP | 80 | 0.0% | 99.6% |  |
| BUILD_LIST | 80 | 0.0% | 99.6% |  |
| BUILD_TUPLE | 80 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 99.7% |  |
| COPY_FREE_VARS | 80 | 0.0% | 99.8% |  |
| FOR_ITER | 80 | 0.0% | 99.8% |  |
| LIST_EXTEND | 80 | 0.0% | 99.8% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 99.9% |  |
| CALL_BUILTIN_CLASS | 60 | 0.0% | 99.9% |  |
| LOAD_ATTR_WITH_HINT | 60 | 0.0% | 99.9% |  |
| LOAD_GLOBAL_BUILTIN | 60 | 0.0% | 100.0% |  |
| BINARY_OP | 40 | 0.0% | 100.0% |  |
| RESUME | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| ENTER_EXECUTOR FOR_ITER_TUPLE | 40,860 | 21.2% | 21.2% |
| FOR_ITER_TUPLE ENTER_EXECUTOR | 40,620 | 21.1% | 42.2% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 40,560 | 21.0% | 63.3% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 12,400 | 6.4% | 69.7% |
| LOAD_FAST PUSH_NULL | 12,400 | 6.4% | 76.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 12,000 | 6.2% | 82.3% |
| POP_TOP LOAD_FAST | 11,780 | 6.1% | 88.4% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 11,600 | 6.0% | 94.5% |
| STORE_FAST LOAD_FAST | 1,260 | 0.7% | 95.1% |
| LOAD_FAST_LOAD_FAST CALL | 800 | 0.4% | 95.5% |
| FOR_ITER_TUPLE STORE_FAST | 600 | 0.3% | 95.8% |
| CALL POP_TOP | 480 | 0.2% | 96.1% |
| LOAD_FAST GET_ITER | 480 | 0.2% | 96.3% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 400 | 0.2% | 96.5% |
| GET_ITER FOR_ITER_TUPLE | 380 | 0.2% | 96.7% |
| FOR_ITER_RANGE STORE_FAST | 380 | 0.2% | 96.9% |
| POP_TOP JUMP_BACKWARD | 340 | 0.2% | 97.1% |
| FOR_ITER_TUPLE JUMP_BACKWARD | 340 | 0.2% | 97.3% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 0.2% | 97.4% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 300 | 0.2% | 97.6% |
| POP_TOP ENTER_EXECUTOR | 280 | 0.1% | 97.7% |
| PUSH_NULL CALL | 240 | 0.1% | 97.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.1% | 98.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.1% | 98.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.1% | 98.1% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 120 | 0.1% | 98.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.1% | 98.2% |
| CALL STORE_FAST | 100 | 0.1% | 98.3% |
| NOP LOAD_DEREF | 80 | 0.0% | 98.3% |
| POP_TOP NOP | 80 | 0.0% | 98.4% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 98.4% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 98.5% |
| BUILD_TUPLE STORE_FAST | 80 | 0.0% | 98.5% |
| CALL LOAD_FAST | 80 | 0.0% | 98.5% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 98.6% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 98.6% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.0% | 98.7% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 98.7% |
| LOAD_ATTR LOAD_ATTR_MODULE | 80 | 0.0% | 98.8% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 98.8% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 98.8% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 98.9% |
| LOAD_FAST LOAD_ATTR | 80 | 0.0% | 98.9% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.0% | 99.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 80 | 0.0% | 99.0% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 80 | 0.0% | 99.0% |
| GET_ITER FOR_ITER_RANGE | 60 | 0.0% | 99.1% |
| CALL CALL | 60 | 0.0% | 99.1% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.0% | 99.1% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.0% | 99.2% |
| LOAD_ATTR PUSH_NULL | 60 | 0.0% | 99.2% |
| LOAD_GLOBAL LOAD_ATTR | 60 | 0.0% | 99.2% |
| BINARY_OP_SUBTRACT_FLOAT RETURN_VALUE | 60 | 0.0% | 99.3% |
| CALL_BUILTIN_CLASS STORE_FAST | 60 | 0.0% | 99.3% |
| LOAD_ATTR_MODULE STORE_FAST | 60 | 0.0% | 99.3% |
| LOAD_ATTR_WITH_HINT STORE_FAST | 60 | 0.0% | 99.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 60 | 0.0% | 99.4% |
| LOAD_GLOBAL_MODULE BUILD_TUPLE | 60 | 0.0% | 99.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 60 | 0.0% | 99.5% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.0% | 99.5% |
| GET_ITER FOR_ITER | 40 | 0.0% | 99.5% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.0% | 99.5% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.5% |
| FOR_ITER STORE_FAST | 40 | 0.0% | 99.6% |
| JUMP_BACKWARD ENTER_EXECUTOR | 40 | 0.0% | 99.6% |
| JUMP_BACKWARD FOR_ITER | 40 | 0.0% | 99.6% |
| LOAD_ATTR STORE_FAST | 40 | 0.0% | 99.6% |
| LOAD_FAST BINARY_OP | 40 | 0.0% | 99.6% |
| LOAD_FAST CALL | 40 | 0.0% | 99.7% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 40 | 0.0% | 99.7% |
| LOAD_FAST CALL_BUILTIN_CLASS | 40 | 0.0% | 99.7% |
| LOAD_FAST LOAD_ATTR_MODULE | 40 | 0.0% | 99.7% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 40 | 0.0% | 99.8% |
| LOAD_GLOBAL LOAD_GLOBAL | 40 | 0.0% | 99.8% |
| FOR_ITER_RANGE LOAD_GLOBAL | 40 | 0.0% | 99.8% |
| FOR_ITER_RANGE LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.8% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL | 40 | 0.0% | 99.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 40 | 0.0% | 99.9% |
| BINARY_OP RETURN_VALUE | 20 | 0.0% | 99.9% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% | 99.9% |
| CALL CALL_BUILTIN_CLASS | 20 | 0.0% | 99.9% |
| CALL_FUNCTION_EX RESUME | 20 | 0.0% | 99.9% |
| COPY_FREE_VARS RESUME | 20 | 0.0% | 99.9% |
| FOR_ITER FOR_ITER_RANGE | 20 | 0.0% | 99.9% |
| FOR_ITER FOR_ITER_TUPLE | 20 | 0.0% | 99.9% |
| LOAD_ATTR LOAD_ATTR_WITH_HINT | 20 | 0.0% | 99.9% |
| LOAD_GLOBAL BUILD_TUPLE | 20 | 0.0% | 99.9% |
| LOAD_GLOBAL LOAD_FAST | 20 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 20 | 0.0% | 100.0% |
| RESUME LOAD_DEREF | 20 | 0.0% | 100.0% |
| RESUME LOAD_GLOBAL | 20 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL | 20 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 380 | 79.2% |
| FOR_ITER_RANGE | 60 | 12.5% |
| FOR_ITER | 40 | 8.3% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 12,000 | 96.2% |
| CALL | 480 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,780 | 94.4% |
| JUMP_BACKWARD | 340 | 2.7% |
| ENTER_EXECUTOR | 280 | 2.2% |
| NOP | 80 | 0.6% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,400 | 96.9% |
| LOAD_ATTR_MODULE | 180 | 1.4% |
| LOAD_DEREF | 160 | 1.2% |
| LOAD_ATTR | 60 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,400 | 96.9% |
| CALL | 240 | 1.9% |
| LOAD_FAST | 160 | 1.2% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 37.5% |
| BINARY_OP | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20 | 50.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 50.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 60 | 75.0% |
| LOAD_GLOBAL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 800 | 70.2% |
| PUSH_NULL | 240 | 21.1% |
| CALL | 60 | 5.3% |
| LOAD_FAST | 40 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 480 | 42.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 400 | 35.1% |
| STORE_FAST | 100 | 8.8% |
| LOAD_FAST | 80 | 7.0% |
| CALL | 60 | 5.3% |


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
| FOR_ITER_TUPLE | 40,620 | 49.8% |
| ENTER_EXECUTOR | 40,560 | 49.8% |
| POP_TOP | 280 | 0.3% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 40,860 | 50.1% |
| ENTER_EXECUTOR | 40,560 | 49.8% |
| FOR_ITER_RANGE | 80 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40 | 50.0% |
| JUMP_BACKWARD | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 50.0% |
| FOR_ITER_RANGE | 20 | 25.0% |
| FOR_ITER_TUPLE | 20 | 25.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 50.0% |
| FOR_ITER_TUPLE | 340 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 300 | 44.1% |
| FOR_ITER_TUPLE | 300 | 44.1% |
| ENTER_EXECUTOR | 40 | 5.9% |
| FOR_ITER | 40 | 5.9% |


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
| LOAD_FAST | 80 | 40.0% |
| LOAD_GLOBAL | 60 | 30.0% |
| LOAD_GLOBAL_MODULE | 60 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 80 | 40.0% |
| PUSH_NULL | 60 | 30.0% |
| STORE_FAST | 40 | 20.0% |
| LOAD_ATTR_WITH_HINT | 20 | 10.0% |


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
| POP_TOP | 11,780 | 88.2% |
| STORE_FAST | 1,260 | 9.4% |
| PUSH_NULL | 160 | 1.2% |
| CALL | 80 | 0.6% |
| LOAD_GLOBAL_BUILTIN | 60 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 12,400 | 92.8% |
| GET_ITER | 480 | 3.6% |
| BUILD_LIST | 80 | 0.6% |
| CALL_FUNCTION_EX | 80 | 0.6% |
| LOAD_ATTR | 80 | 0.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 12,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 11,600 | 93.5% |
| CALL | 800 | 6.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 28.6% |
| RETURN_VALUE | 40 | 14.3% |
| LOAD_GLOBAL | 40 | 14.3% |
| FOR_ITER_RANGE | 40 | 14.3% |
| LOAD_GLOBAL_MODULE | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 42.9% |
| LOAD_ATTR | 60 | 21.4% |
| LOAD_GLOBAL | 40 | 14.3% |
| BUILD_TUPLE | 20 | 7.1% |
| LOAD_FAST | 20 | 7.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 600 | 42.3% |
| FOR_ITER_RANGE | 380 | 26.8% |
| CALL | 100 | 7.0% |
| BUILD_TUPLE | 80 | 5.6% |
| CALL_BUILTIN_CLASS | 60 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,260 | 88.7% |
| LOAD_GLOBAL | 80 | 5.6% |
| LOAD_GLOBAL_MODULE | 80 | 5.6% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 20 | 50.0% |
| COPY_FREE_VARS | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 20 | 50.0% |
| LOAD_GLOBAL | 20 | 50.0% |


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

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,600 | 96.7% |
| CALL | 400 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 12,000 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 300 | 65.2% |
| ENTER_EXECUTOR | 80 | 17.4% |
| GET_ITER | 60 | 13.0% |
| FOR_ITER | 20 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 380 | 82.6% |
| LOAD_GLOBAL | 40 | 8.7% |
| LOAD_GLOBAL_MODULE | 40 | 8.7% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 40,860 | 98.3% |
| GET_ITER | 380 | 0.9% |
| JUMP_BACKWARD | 300 | 0.7% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 40,620 | 97.7% |
| STORE_FAST | 600 | 1.4% |
| JUMP_BACKWARD | 340 | 0.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 50.0% |
| LOAD_ATTR | 80 | 33.3% |
| LOAD_FAST | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 180 | 75.0% |
| STORE_FAST | 60 | 25.0% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| LOAD_ATTR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 40 | 66.7% |
| LOAD_GLOBAL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 120 | 33.3% |
| STORE_FAST | 80 | 22.2% |
| LOAD_GLOBAL_MODULE | 80 | 22.2% |
| RETURN_VALUE | 40 | 11.1% |
| FOR_ITER_RANGE | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 120 | 33.3% |
| LOAD_GLOBAL_MODULE | 80 | 22.2% |
| BUILD_TUPLE | 60 | 16.7% |
| LOAD_ATTR | 60 | 16.7% |
| LOAD_GLOBAL | 40 | 11.1% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 60 | 50.0% |
| COPY_FREE_VARS | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 60 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 33.3% |
| LOAD_GLOBAL | 20 | 16.7% |


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
|     deferred | 20 | 20.0% |
|          hit | 60 | 60.0% |

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
|     deferred | 660 | 0.0% |
|          hit | 2,457,260 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 87.5% |
| Failure | 60 | 12.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.1% |
|          hit | 42,020 | 99.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 20.0% |
|          hit | 300 | 60.0% |

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
|     deferred | 140 | 20.0% |
|          hit | 420 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 136,200 | 70.6% |
| Not specialized | 1,740 | 0.9% |
| Specialized hits | 54,980 | 28.5% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 660 | 68.8% |
| LOAD_GLOBAL | 140 | 14.6% |
| LOAD_ATTR | 100 | 10.4% |
| FOR_ITER | 40 | 4.2% |
| BINARY_OP | 20 | 2.1% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| BINARY_SUBSCR | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| NOP | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 0 | 0.0% |
| Calls to Python functions inlined | 160 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 100.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 160 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,096,400 | 15.1% |
| Frees to freelist | 4,096,340 |  |
| Allocations | 22,999,340 | 84.9% |
| Allocations to 512 bytes | 16,445,700 | 60.7% |
| Allocations to 4 kbytes | 3,276,840 | 12.1% |
| Allocations over 4 kbytes | 3,276,800 | 12.1% |
| Frees | 22,998,621 |  |
| New values | 0 |  |
| Interpreter increfs | 109,540 | 0.0% |
| Interpreter decrefs | 204,220 | 0.1% |
| Increfs | 236,969,442 | 100.0% |
| Decrefs | 254,139,266 | 99.9% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 5,693,673 |  |
| Method cache misses | 860,047 |  |
| Method cache collisions | 900,977 |  |
| Method cache dunder hits | 7,331,737 |  |
| Method cache dunder misses | 41,063 |  |


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
| Optimization attempts | 40 |  |
| Traces created | 40 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 20 | 50.0% |
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
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 0 | 0.0% |
| <= 256 | 40 | 100.0% |


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
| <= 16 | 0 | 0.0% |
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 0 | 0.0% |
| <= 256 | 40 | 100.0% |


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
