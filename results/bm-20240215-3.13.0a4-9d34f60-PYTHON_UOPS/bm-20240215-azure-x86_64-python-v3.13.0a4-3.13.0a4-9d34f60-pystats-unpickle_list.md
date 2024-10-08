
# Pystats results

- benchmark: unpickle_list
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 8,640 | 33.3% | 33.3% |  |
| PUSH_NULL | 4,480 | 17.3% | 50.6% |  |
| POP_TOP | 4,080 | 15.7% | 66.3% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,860 | 14.9% | 81.2% |  |
| CALL | 780 | 3.0% | 84.2% |  |
| STORE_FAST | 720 | 2.8% | 87.0% |  |
| FOR_ITER_RANGE | 460 | 1.8% | 88.7% |  |
| JUMP_BACKWARD | 340 | 1.3% | 90.1% |  |
| LOAD_ATTR_MODULE | 300 | 1.2% | 91.2% |  |
| LOAD_ATTR | 240 | 0.9% | 92.1% |  |
| LOAD_DEREF | 240 | 0.9% | 93.1% |  |
| LOAD_GLOBAL_MODULE | 240 | 0.9% | 94.0% |  |
| LOAD_GLOBAL | 200 | 0.8% | 94.8% |  |
| RETURN_VALUE | 160 | 0.6% | 95.4% |  |
| CALL_FUNCTION_EX | 160 | 0.6% | 96.0% |  |
| RESUME_CHECK | 120 | 0.5% | 96.5% |  |
| GET_ITER | 80 | 0.3% | 96.8% |  |
| NOP | 80 | 0.3% | 97.1% |  |
| BUILD_LIST | 80 | 0.3% | 97.4% |  |
| CALL_INTRINSIC_1 | 80 | 0.3% | 97.7% |  |
| COPY_FREE_VARS | 80 | 0.3% | 98.0% |  |
| ENTER_EXECUTOR | 80 | 0.3% | 98.3% |  |
| LIST_EXTEND | 80 | 0.3% | 98.6% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.2% | 98.8% |  |
| CALL_BUILTIN_CLASS | 60 | 0.2% | 99.1% |  |
| LOAD_ATTR_WITH_HINT | 60 | 0.2% | 99.3% |  |
| LOAD_GLOBAL_BUILTIN | 60 | 0.2% | 99.5% |  |
| BINARY_OP | 40 | 0.2% | 99.7% |  |
| FOR_ITER | 40 | 0.2% | 99.8% |  |
| RESUME | 40 | 0.2% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| PUSH_NULL LOAD_FAST | 4,160 | 16.0% | 16.0% |
| LOAD_FAST PUSH_NULL | 4,000 | 15.4% | 31.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 3,800 | 14.6% | 46.1% |
| POP_TOP LOAD_FAST | 3,600 | 13.9% | 60.0% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,600 | 13.9% | 73.9% |
| STORE_FAST LOAD_FAST | 560 | 2.2% | 76.0% |
| LOAD_FAST CALL | 440 | 1.7% | 77.7% |
| FOR_ITER_RANGE STORE_FAST | 380 | 1.5% | 79.2% |
| POP_TOP JUMP_BACKWARD | 340 | 1.3% | 80.5% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 1.2% | 81.6% |
| CALL POP_TOP | 280 | 1.1% | 82.7% |
| PUSH_NULL CALL | 240 | 0.9% | 83.7% |
| LOAD_ATTR_MODULE PUSH_NULL | 240 | 0.9% | 84.6% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 220 | 0.8% | 85.4% |
| LOAD_DEREF PUSH_NULL | 160 | 0.6% | 86.0% |
| CALL STORE_FAST | 120 | 0.5% | 86.5% |
| LOAD_FAST LOAD_ATTR | 120 | 0.5% | 87.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.5% | 87.4% |
| LOAD_ATTR LOAD_ATTR_MODULE | 100 | 0.4% | 87.8% |
| NOP LOAD_DEREF | 80 | 0.3% | 88.1% |
| POP_TOP NOP | 80 | 0.3% | 88.4% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.3% | 88.7% |
| BUILD_LIST LOAD_DEREF | 80 | 0.3% | 89.1% |
| CALL LOAD_FAST | 80 | 0.3% | 89.4% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.3% | 89.7% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.3% | 90.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.3% | 90.3% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.3% | 90.6% |
| LOAD_ATTR PUSH_NULL | 80 | 0.3% | 90.9% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.3% | 91.2% |
| LOAD_FAST GET_ITER | 80 | 0.3% | 91.5% |
| LOAD_FAST BUILD_LIST | 80 | 0.3% | 91.8% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.3% | 92.1% |
| LOAD_FAST LOAD_ATTR_MODULE | 80 | 0.3% | 92.4% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 80 | 0.3% | 92.8% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.3% | 93.1% |
| GET_ITER FOR_ITER_RANGE | 60 | 0.2% | 93.3% |
| POP_TOP ENTER_EXECUTOR | 60 | 0.2% | 93.5% |
| CALL CALL | 60 | 0.2% | 93.8% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.2% | 94.0% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.2% | 94.2% |
| LOAD_GLOBAL LOAD_ATTR | 60 | 0.2% | 94.4% |
| BINARY_OP_SUBTRACT_FLOAT RETURN_VALUE | 60 | 0.2% | 94.7% |
| CALL_BUILTIN_CLASS STORE_FAST | 60 | 0.2% | 94.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 60 | 0.2% | 95.1% |
| LOAD_ATTR_MODULE STORE_FAST | 60 | 0.2% | 95.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 60 | 0.2% | 95.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 60 | 0.2% | 95.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 60 | 0.2% | 96.1% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.2% | 96.3% |
| RESUME_CHECK LOAD_FAST | 60 | 0.2% | 96.5% |
| PUSH_NULL LOAD_GLOBAL | 40 | 0.2% | 96.7% |
| PUSH_NULL LOAD_GLOBAL_MODULE | 40 | 0.2% | 96.8% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.2% | 97.0% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.2% | 97.1% |
| LOAD_FAST BINARY_OP | 40 | 0.2% | 97.3% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 40 | 0.2% | 97.5% |
| LOAD_FAST CALL_BUILTIN_CLASS | 40 | 0.2% | 97.6% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 40 | 0.2% | 97.8% |
| LOAD_GLOBAL LOAD_FAST | 40 | 0.2% | 97.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 40 | 0.2% | 98.1% |
| STORE_FAST LOAD_GLOBAL_MODULE | 40 | 0.2% | 98.2% |
| FOR_ITER_RANGE LOAD_GLOBAL | 40 | 0.2% | 98.4% |
| FOR_ITER_RANGE LOAD_GLOBAL_MODULE | 40 | 0.2% | 98.5% |
| LOAD_ATTR_WITH_HINT CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 0.2% | 98.7% |
| GET_ITER FOR_ITER | 20 | 0.1% | 98.8% |
| BINARY_OP RETURN_VALUE | 20 | 0.1% | 98.8% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.1% | 98.9% |
| CALL CALL_BUILTIN_CLASS | 20 | 0.1% | 99.0% |
| CALL_FUNCTION_EX RESUME | 20 | 0.1% | 99.1% |
| COPY_FREE_VARS RESUME | 20 | 0.1% | 99.2% |
| FOR_ITER STORE_FAST | 20 | 0.1% | 99.2% |
| FOR_ITER FOR_ITER_RANGE | 20 | 0.1% | 99.3% |
| JUMP_BACKWARD ENTER_EXECUTOR | 20 | 0.1% | 99.4% |
| JUMP_BACKWARD FOR_ITER | 20 | 0.1% | 99.5% |
| LOAD_ATTR CALL | 20 | 0.1% | 99.5% |
| LOAD_ATTR STORE_FAST | 20 | 0.1% | 99.6% |
| LOAD_ATTR LOAD_ATTR_WITH_HINT | 20 | 0.1% | 99.7% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 20 | 0.1% | 99.8% |
| RESUME LOAD_DEREF | 20 | 0.1% | 99.8% |
| RESUME LOAD_FAST | 20 | 0.1% | 99.9% |
| LOAD_ATTR_WITH_HINT CALL | 20 | 0.1% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 60 | 75.0% |
| FOR_ITER | 20 | 25.0% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,800 | 93.1% |
| CALL | 280 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,600 | 88.2% |
| JUMP_BACKWARD | 340 | 8.3% |
| NOP | 80 | 2.0% |
| ENTER_EXECUTOR | 60 | 1.5% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,000 | 89.3% |
| LOAD_ATTR_MODULE | 240 | 5.4% |
| LOAD_DEREF | 160 | 3.6% |
| LOAD_ATTR | 80 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,160 | 92.9% |
| CALL | 240 | 5.4% |
| LOAD_GLOBAL | 40 | 0.9% |
| LOAD_GLOBAL_MODULE | 40 | 0.9% |


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

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 56.4% |
| PUSH_NULL | 240 | 30.8% |
| CALL | 60 | 7.7% |
| LOAD_ATTR | 20 | 2.6% |
| LOAD_ATTR_WITH_HINT | 20 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 280 | 35.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 220 | 28.2% |
| STORE_FAST | 120 | 15.4% |
| LOAD_FAST | 80 | 10.3% |
| CALL | 60 | 7.7% |


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
| POP_TOP | 60 | 75.0% |
| JUMP_BACKWARD | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 80 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 50.0% |
| JUMP_BACKWARD | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 50.0% |
| FOR_ITER_RANGE | 20 | 50.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 300 | 88.2% |
| ENTER_EXECUTOR | 20 | 5.9% |
| FOR_ITER | 20 | 5.9% |


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
| LOAD_FAST | 120 | 50.0% |
| LOAD_GLOBAL | 60 | 25.0% |
| LOAD_GLOBAL_MODULE | 60 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 100 | 41.7% |
| PUSH_NULL | 80 | 33.3% |
| CALL | 20 | 8.3% |
| STORE_FAST | 20 | 8.3% |
| LOAD_ATTR_WITH_HINT | 20 | 8.3% |


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
| PUSH_NULL | 4,160 | 48.1% |
| POP_TOP | 3,600 | 41.7% |
| STORE_FAST | 560 | 6.5% |
| CALL | 80 | 0.9% |
| LOAD_GLOBAL_BUILTIN | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,000 | 46.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,600 | 41.7% |
| CALL | 440 | 5.1% |
| LOAD_ATTR | 120 | 1.4% |
| GET_ITER | 80 | 0.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 40.0% |
| PUSH_NULL | 40 | 20.0% |
| RETURN_VALUE | 40 | 20.0% |
| FOR_ITER_RANGE | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 40.0% |
| LOAD_ATTR | 60 | 30.0% |
| LOAD_FAST | 40 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 10.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 380 | 52.8% |
| CALL | 120 | 16.7% |
| CALL_BUILTIN_CLASS | 60 | 8.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 8.3% |
| LOAD_ATTR_MODULE | 60 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 77.8% |
| LOAD_GLOBAL | 80 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 40 | 5.6% |
| LOAD_GLOBAL_MODULE | 40 | 5.6% |


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
| LOAD_FAST | 3,600 | 93.3% |
| CALL | 220 | 5.7% |
| LOAD_ATTR_WITH_HINT | 40 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,800 | 98.4% |
| STORE_FAST | 60 | 1.6% |


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

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 40.0% |
| LOAD_ATTR | 100 | 33.3% |
| LOAD_FAST | 80 | 26.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 240 | 80.0% |
| STORE_FAST | 60 | 20.0% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 66.7% |
| CALL | 20 | 33.3% |


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
| LOAD_GLOBAL | 80 | 33.3% |
| PUSH_NULL | 40 | 16.7% |
| RETURN_VALUE | 40 | 16.7% |
| STORE_FAST | 40 | 16.7% |
| FOR_ITER_RANGE | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 120 | 50.0% |
| LOAD_ATTR | 60 | 25.0% |
| LOAD_FAST | 60 | 25.0% |


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
|     deferred | 480 | 0.0% |
|          hit | 1,638,320 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 80.0% |
| Failure | 60 | 20.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 4.0% |
|          hit | 460 | 92.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 120 | 20.0% |
|          hit | 360 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 20.0% |
|          hit | 300 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 19,420 | 74.9% |
| Not specialized | 1,300 | 5.0% |
| Specialized hits | 5,220 | 20.1% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 480 | 64.9% |
| LOAD_ATTR | 120 | 16.2% |
| LOAD_GLOBAL | 100 | 13.5% |
| BINARY_OP | 20 | 2.7% |
| FOR_ITER | 20 | 2.7% |
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
| Allocations from freelist | 101,581,120 | 61.9% |
| Frees to freelist | 101,581,060 |  |
| Allocations | 62,403,400 | 38.1% |
| Allocations to 512 bytes | 62,403,140 | 38.1% |
| Allocations to 4 kbytes | 180 | 0.0% |
| Allocations over 4 kbytes | 80 | 0.0% |
| Frees | 116,470,566 |  |
| New values | 0 |  |
| Interpreter increfs | 10,300 | 0.0% |
| Interpreter decrefs | 14,900 | 0.0% |
| Increfs | 163,837,984 | 100.0% |
| Decrefs | 270,473,411 | 100.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 1,638,615 |  |
| Method cache misses | 85 |  |
| Method cache collisions | 68 |  |
| Method cache dunder hits | 0 |  |
| Method cache dunder misses | 0 |  |


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
| Optimization attempts | 20 |  |
| Traces created | 20 | 100.0% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 20 | 100.0% |


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
| <= 128 | 20 | 100.0% |


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
