
# Pystats results

- benchmark: unpickle
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| ENTER_EXECUTOR | 81,500 | 41.9% | 41.9% |  |
| FOR_ITER_TUPLE | 41,560 | 21.3% | 63.2% |  |
| LOAD_FAST | 26,240 | 13.5% | 76.7% |  |
| PUSH_NULL | 13,040 | 6.7% | 83.4% |  |
| POP_TOP | 12,480 | 6.4% | 89.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 12,180 | 6.3% | 96.1% |  |
| STORE_FAST | 1,580 | 0.8% | 96.9% |  |
| CALL | 1,260 | 0.6% | 97.5% |  |
| JUMP_BACKWARD | 680 | 0.3% | 97.9% |  |
| GET_ITER | 480 | 0.2% | 98.1% |  |
| FOR_ITER_RANGE | 460 | 0.2% | 98.3% |  |
| LOAD_ATTR_MODULE | 420 | 0.2% | 98.6% |  |
| LOAD_ATTR | 400 | 0.2% | 98.8% |  |
| LOAD_GLOBAL_MODULE | 360 | 0.2% | 99.0% |  |
| LOAD_GLOBAL | 280 | 0.1% | 99.1% |  |
| LOAD_DEREF | 240 | 0.1% | 99.2% |  |
| LOAD_ATTR_WITH_HINT | 180 | 0.1% | 99.3% |  |
| RETURN_VALUE | 160 | 0.1% | 99.4% |  |
| CALL_FUNCTION_EX | 160 | 0.1% | 99.5% |  |
| RESUME_CHECK | 120 | 0.1% | 99.5% |  |
| NOP | 80 | 0.0% | 99.6% |  |
| BUILD_LIST | 80 | 0.0% | 99.6% |  |
| BUILD_TUPLE | 80 | 0.0% | 99.7% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 99.7% |  |
| COPY_FREE_VARS | 80 | 0.0% | 99.7% |  |
| FOR_ITER | 80 | 0.0% | 99.8% |  |
| LIST_EXTEND | 80 | 0.0% | 99.8% |  |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% | 99.9% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 99.9% |  |
| CALL_BUILTIN_CLASS | 60 | 0.0% | 99.9% |  |
| LOAD_GLOBAL_BUILTIN | 60 | 0.0% | 100.0% |  |
| BINARY_OP | 40 | 0.0% | 100.0% |  |
| RESUME | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| ENTER_EXECUTOR FOR_ITER_TUPLE | 40,860 | 21.0% | 21.0% |
| FOR_ITER_TUPLE ENTER_EXECUTOR | 40,620 | 20.9% | 41.9% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 40,560 | 20.8% | 62.7% |
| PUSH_NULL LOAD_FAST | 12,560 | 6.5% | 69.1% |
| LOAD_FAST PUSH_NULL | 12,400 | 6.4% | 75.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 12,000 | 6.2% | 81.7% |
| POP_TOP LOAD_FAST | 11,780 | 6.1% | 87.7% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 11,600 | 6.0% | 93.7% |
| STORE_FAST LOAD_FAST | 1,340 | 0.7% | 94.4% |
| LOAD_FAST CALL | 840 | 0.4% | 94.8% |
| FOR_ITER_TUPLE STORE_FAST | 600 | 0.3% | 95.1% |
| CALL POP_TOP | 480 | 0.2% | 95.4% |
| LOAD_FAST GET_ITER | 480 | 0.2% | 95.6% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 460 | 0.2% | 95.8% |
| GET_ITER FOR_ITER_TUPLE | 380 | 0.2% | 96.0% |
| FOR_ITER_RANGE STORE_FAST | 380 | 0.2% | 96.2% |
| LOAD_ATTR_MODULE PUSH_NULL | 360 | 0.2% | 96.4% |
| POP_TOP JUMP_BACKWARD | 340 | 0.2% | 96.6% |
| FOR_ITER_TUPLE JUMP_BACKWARD | 340 | 0.2% | 96.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 0.2% | 96.9% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 300 | 0.2% | 97.1% |
| POP_TOP ENTER_EXECUTOR | 280 | 0.1% | 97.2% |
| LOAD_FAST LOAD_ATTR | 280 | 0.1% | 97.4% |
| PUSH_NULL CALL | 240 | 0.1% | 97.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 180 | 0.1% | 97.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 180 | 0.1% | 97.7% |
| CALL STORE_FAST | 160 | 0.1% | 97.8% |
| LOAD_DEREF PUSH_NULL | 160 | 0.1% | 97.8% |
| LOAD_FAST LOAD_ATTR_MODULE | 160 | 0.1% | 97.9% |
| LOAD_ATTR LOAD_ATTR_MODULE | 140 | 0.1% | 98.0% |
| PUSH_NULL LOAD_GLOBAL | 120 | 0.1% | 98.0% |
| PUSH_NULL LOAD_GLOBAL_MODULE | 120 | 0.1% | 98.1% |
| LOAD_ATTR PUSH_NULL | 120 | 0.1% | 98.2% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 120 | 0.1% | 98.2% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 120 | 0.1% | 98.3% |
| LOAD_ATTR_WITH_HINT CALL_BUILTIN_FAST_WITH_KEYWORDS | 120 | 0.1% | 98.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.1% | 98.4% |
| NOP LOAD_DEREF | 80 | 0.0% | 98.5% |
| POP_TOP NOP | 80 | 0.0% | 98.5% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 98.5% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 98.6% |
| BUILD_TUPLE STORE_FAST | 80 | 0.0% | 98.6% |
| CALL LOAD_FAST | 80 | 0.0% | 98.7% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 98.7% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 98.7% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.0% | 98.8% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 98.8% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 98.9% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 98.9% |
| LOAD_FAST BUILD_TUPLE | 80 | 0.0% | 99.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 99.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 80 | 0.0% | 99.0% |
| LOAD_GLOBAL LOAD_FAST | 80 | 0.0% | 99.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 80 | 0.0% | 99.1% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.0% | 99.2% |
| GET_ITER FOR_ITER_RANGE | 60 | 0.0% | 99.2% |
| CALL CALL | 60 | 0.0% | 99.2% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.0% | 99.3% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.0% | 99.3% |
| LOAD_ATTR CALL | 60 | 0.0% | 99.3% |
| LOAD_ATTR LOAD_ATTR_WITH_HINT | 60 | 0.0% | 99.3% |
| LOAD_GLOBAL LOAD_ATTR | 60 | 0.0% | 99.4% |
| BINARY_OP_SUBTRACT_FLOAT RETURN_VALUE | 60 | 0.0% | 99.4% |
| CALL_BUILTIN_CLASS STORE_FAST | 60 | 0.0% | 99.4% |
| LOAD_ATTR_MODULE STORE_FAST | 60 | 0.0% | 99.5% |
| LOAD_ATTR_WITH_HINT CALL | 60 | 0.0% | 99.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 60 | 0.0% | 99.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 60 | 0.0% | 99.6% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.0% | 99.6% |
| RESUME_CHECK LOAD_FAST | 60 | 0.0% | 99.6% |
| GET_ITER FOR_ITER | 40 | 0.0% | 99.6% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.0% | 99.7% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.7% |
| FOR_ITER STORE_FAST | 40 | 0.0% | 99.7% |
| JUMP_BACKWARD ENTER_EXECUTOR | 40 | 0.0% | 99.7% |
| JUMP_BACKWARD FOR_ITER | 40 | 0.0% | 99.7% |
| LOAD_FAST BINARY_OP | 40 | 0.0% | 99.8% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 40 | 0.0% | 99.8% |
| LOAD_FAST CALL_BUILTIN_CLASS | 40 | 0.0% | 99.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 40 | 0.0% | 99.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.8% |
| FOR_ITER_RANGE LOAD_GLOBAL | 40 | 0.0% | 99.9% |
| FOR_ITER_RANGE LOAD_GLOBAL_MODULE | 40 | 0.0% | 99.9% |
| BINARY_OP RETURN_VALUE | 20 | 0.0% | 99.9% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% | 99.9% |
| CALL CALL_BUILTIN_CLASS | 20 | 0.0% | 99.9% |
| CALL_FUNCTION_EX RESUME | 20 | 0.0% | 99.9% |
| COPY_FREE_VARS RESUME | 20 | 0.0% | 99.9% |
| FOR_ITER FOR_ITER_RANGE | 20 | 0.0% | 99.9% |
| FOR_ITER FOR_ITER_TUPLE | 20 | 0.0% | 100.0% |
| LOAD_ATTR STORE_FAST | 20 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 20 | 0.0% | 100.0% |
| RESUME LOAD_DEREF | 20 | 0.0% | 100.0% |
| RESUME LOAD_FAST | 20 | 0.0% | 100.0% |


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
| LOAD_FAST | 12,400 | 95.1% |
| LOAD_ATTR_MODULE | 360 | 2.8% |
| LOAD_DEREF | 160 | 1.2% |
| LOAD_ATTR | 120 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,560 | 96.3% |
| CALL | 240 | 1.8% |
| LOAD_GLOBAL | 120 | 0.9% |
| LOAD_GLOBAL_MODULE | 120 | 0.9% |


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
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 840 | 66.7% |
| PUSH_NULL | 240 | 19.0% |
| CALL | 60 | 4.8% |
| LOAD_ATTR | 60 | 4.8% |
| LOAD_ATTR_WITH_HINT | 60 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 480 | 38.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 460 | 36.5% |
| STORE_FAST | 160 | 12.7% |
| LOAD_FAST | 80 | 6.3% |
| CALL | 60 | 4.8% |


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
| LOAD_FAST | 280 | 70.0% |
| LOAD_GLOBAL | 60 | 15.0% |
| LOAD_GLOBAL_MODULE | 60 | 15.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 140 | 35.0% |
| PUSH_NULL | 120 | 30.0% |
| CALL | 60 | 15.0% |
| LOAD_ATTR_WITH_HINT | 60 | 15.0% |
| STORE_FAST | 20 | 5.0% |


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
| PUSH_NULL | 12,560 | 47.9% |
| POP_TOP | 11,780 | 44.9% |
| STORE_FAST | 1,340 | 5.1% |
| LOAD_GLOBAL_MODULE | 180 | 0.7% |
| CALL | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 12,400 | 47.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 11,600 | 44.2% |
| CALL | 840 | 3.2% |
| GET_ITER | 480 | 1.8% |
| LOAD_ATTR | 280 | 1.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 120 | 42.9% |
| STORE_FAST | 80 | 28.6% |
| RETURN_VALUE | 40 | 14.3% |
| FOR_ITER_RANGE | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 42.9% |
| LOAD_FAST | 80 | 28.6% |
| LOAD_ATTR | 60 | 21.4% |
| LOAD_GLOBAL_BUILTIN | 20 | 7.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 600 | 38.0% |
| FOR_ITER_RANGE | 380 | 24.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 180 | 11.4% |
| CALL | 160 | 10.1% |
| BUILD_TUPLE | 80 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,340 | 84.8% |
| LOAD_FAST_LOAD_FAST | 80 | 5.1% |
| LOAD_GLOBAL | 80 | 5.1% |
| LOAD_GLOBAL_BUILTIN | 40 | 2.5% |
| LOAD_GLOBAL_MODULE | 40 | 2.5% |


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
| LOAD_FAST | 20 | 50.0% |


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
| LOAD_FAST | 11,600 | 95.2% |
| CALL | 460 | 3.8% |
| LOAD_ATTR_WITH_HINT | 120 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 12,000 | 98.5% |
| STORE_FAST | 180 | 1.5% |


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
| LOAD_FAST | 160 | 38.1% |
| LOAD_ATTR | 140 | 33.3% |
| LOAD_GLOBAL_MODULE | 120 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 360 | 85.7% |
| STORE_FAST | 60 | 14.3% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 66.7% |
| LOAD_ATTR | 60 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 120 | 66.7% |
| CALL | 60 | 33.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 66.7% |
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
| PUSH_NULL | 120 | 33.3% |
| LOAD_GLOBAL | 120 | 33.3% |
| RETURN_VALUE | 40 | 11.1% |
| STORE_FAST | 40 | 11.1% |
| FOR_ITER_RANGE | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 50.0% |
| LOAD_ATTR_MODULE | 120 | 33.3% |
| LOAD_ATTR | 60 | 16.7% |


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
| LOAD_FAST | 60 | 50.0% |


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
|     deferred | 720 | 0.0% |
|          hit | 2,457,440 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 88.9% |
| Failure | 60 | 11.1% |

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
|     deferred | 200 | 20.0% |
|          hit | 600 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
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
| Basic | 137,160 | 70.5% |
| Not specialized | 2,060 | 1.1% |
| Specialized hits | 55,460 | 28.5% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 720 | 64.3% |
| LOAD_ATTR | 200 | 17.9% |
| LOAD_GLOBAL | 140 | 12.5% |
| FOR_ITER | 40 | 3.6% |
| BINARY_OP | 20 | 1.8% |
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
| Allocations from freelist | 14,746,400 | 7.0% |
| Frees to freelist | 14,746,340 |  |
| Allocations | 195,033,580 | 93.0% |
| Allocations to 512 bytes | 191,756,100 | 91.4% |
| Allocations to 4 kbytes | 3,277,160 | 1.6% |
| Allocations over 4 kbytes | 320 | 0.0% |
| Frees | 202,404,715 |  |
| New values | 0 |  |
| Interpreter increfs | 110,360 | 0.0% |
| Interpreter decrefs | 205,340 | 0.0% |
| Increfs | 465,517,182 | 100.0% |
| Decrefs | 648,985,040 | 100.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 4,087,834 |  |
| Method cache misses | 828,266 |  |
| Method cache collisions | 828,015 |  |
| Method cache dunder hits | 1,639,009 |  |
| Method cache dunder misses | 111 |  |


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
