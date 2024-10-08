
# Pystats results

- benchmark: pickle_list
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 4,560 | 17.8% | 17.8% |  |
| PUSH_NULL | 4,400 | 17.1% | 34.9% |  |
| POP_TOP | 4,080 | 15.9% | 50.8% |  |
| LOAD_FAST_LOAD_FAST | 4,000 | 15.6% | 66.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,800 | 14.8% | 81.2% |  |
| STORE_FAST | 800 | 3.1% | 84.3% |  |
| CALL | 740 | 2.9% | 87.2% |  |
| FOR_ITER_RANGE | 460 | 1.8% | 89.0% |  |
| JUMP_BACKWARD | 340 | 1.3% | 90.3% |  |
| LOAD_DEREF | 240 | 0.9% | 91.3% |  |
| LOAD_ATTR_MODULE | 240 | 0.9% | 92.2% |  |
| LOAD_GLOBAL_MODULE | 240 | 0.9% | 93.1% |  |
| LOAD_ATTR | 200 | 0.8% | 93.9% |  |
| LOAD_GLOBAL | 200 | 0.8% | 94.7% |  |
| RETURN_VALUE | 160 | 0.6% | 95.3% |  |
| CALL_FUNCTION_EX | 160 | 0.6% | 95.9% |  |
| RESUME_CHECK | 120 | 0.5% | 96.4% |  |
| GET_ITER | 80 | 0.3% | 96.7% |  |
| NOP | 80 | 0.3% | 97.0% |  |
| BUILD_LIST | 80 | 0.3% | 97.3% |  |
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
| PUSH_NULL LOAD_FAST_LOAD_FAST | 4,000 | 15.6% | 15.6% |
| LOAD_FAST PUSH_NULL | 4,000 | 15.6% | 31.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 3,800 | 14.8% | 46.0% |
| POP_TOP LOAD_FAST | 3,600 | 14.0% | 60.0% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,600 | 14.0% | 74.0% |
| STORE_FAST LOAD_FAST | 640 | 2.5% | 76.5% |
| LOAD_FAST_LOAD_FAST CALL | 400 | 1.6% | 78.1% |
| FOR_ITER_RANGE STORE_FAST | 380 | 1.5% | 79.6% |
| POP_TOP JUMP_BACKWARD | 340 | 1.3% | 80.9% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 1.2% | 82.1% |
| CALL POP_TOP | 280 | 1.1% | 83.2% |
| PUSH_NULL CALL | 240 | 0.9% | 84.1% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 200 | 0.8% | 84.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.7% | 85.6% |
| PUSH_NULL LOAD_FAST | 160 | 0.6% | 86.2% |
| LOAD_DEREF PUSH_NULL | 160 | 0.6% | 86.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.5% | 87.3% |
| CALL STORE_FAST | 100 | 0.4% | 87.7% |
| NOP LOAD_DEREF | 80 | 0.3% | 88.0% |
| POP_TOP NOP | 80 | 0.3% | 88.3% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.3% | 88.6% |
| BUILD_LIST LOAD_DEREF | 80 | 0.3% | 88.9% |
| CALL LOAD_FAST | 80 | 0.3% | 89.2% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.3% | 89.6% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.3% | 89.9% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.3% | 90.2% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.3% | 90.5% |
| LOAD_ATTR LOAD_ATTR_MODULE | 80 | 0.3% | 90.8% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.3% | 91.1% |
| LOAD_FAST GET_ITER | 80 | 0.3% | 91.4% |
| LOAD_FAST BUILD_LIST | 80 | 0.3% | 91.7% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.3% | 92.0% |
| LOAD_FAST LOAD_ATTR | 80 | 0.3% | 92.4% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 80 | 0.3% | 92.7% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.3% | 93.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 80 | 0.3% | 93.3% |
| GET_ITER FOR_ITER_RANGE | 60 | 0.2% | 93.5% |
| POP_TOP ENTER_EXECUTOR | 60 | 0.2% | 93.8% |
| CALL CALL | 60 | 0.2% | 94.0% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.2% | 94.2% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.2% | 94.5% |
| LOAD_ATTR PUSH_NULL | 60 | 0.2% | 94.7% |
| LOAD_GLOBAL LOAD_ATTR | 60 | 0.2% | 94.9% |
| BINARY_OP_SUBTRACT_FLOAT RETURN_VALUE | 60 | 0.2% | 95.2% |
| CALL_BUILTIN_CLASS STORE_FAST | 60 | 0.2% | 95.4% |
| LOAD_ATTR_MODULE STORE_FAST | 60 | 0.2% | 95.6% |
| LOAD_ATTR_WITH_HINT STORE_FAST | 60 | 0.2% | 95.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 60 | 0.2% | 96.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 60 | 0.2% | 96.3% |
| LOAD_GLOBAL_MODULE STORE_FAST | 60 | 0.2% | 96.6% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.2% | 96.8% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.2% | 97.0% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.2% | 97.1% |
| LOAD_ATTR STORE_FAST | 40 | 0.2% | 97.3% |
| LOAD_FAST BINARY_OP | 40 | 0.2% | 97.4% |
| LOAD_FAST CALL | 40 | 0.2% | 97.6% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 40 | 0.2% | 97.7% |
| LOAD_FAST CALL_BUILTIN_CLASS | 40 | 0.2% | 97.9% |
| LOAD_FAST LOAD_ATTR_MODULE | 40 | 0.2% | 98.1% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 40 | 0.2% | 98.2% |
| FOR_ITER_RANGE LOAD_GLOBAL | 40 | 0.2% | 98.4% |
| FOR_ITER_RANGE LOAD_GLOBAL_MODULE | 40 | 0.2% | 98.5% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 40 | 0.2% | 98.7% |
| GET_ITER FOR_ITER | 20 | 0.1% | 98.8% |
| BINARY_OP RETURN_VALUE | 20 | 0.1% | 98.8% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.1% | 98.9% |
| CALL CALL_BUILTIN_CLASS | 20 | 0.1% | 99.0% |
| CALL_FUNCTION_EX RESUME | 20 | 0.1% | 99.1% |
| COPY_FREE_VARS RESUME | 20 | 0.1% | 99.1% |
| FOR_ITER STORE_FAST | 20 | 0.1% | 99.2% |
| FOR_ITER FOR_ITER_RANGE | 20 | 0.1% | 99.3% |
| JUMP_BACKWARD ENTER_EXECUTOR | 20 | 0.1% | 99.4% |
| JUMP_BACKWARD FOR_ITER | 20 | 0.1% | 99.5% |
| LOAD_ATTR LOAD_ATTR_WITH_HINT | 20 | 0.1% | 99.5% |
| LOAD_GLOBAL LOAD_FAST | 20 | 0.1% | 99.6% |
| LOAD_GLOBAL STORE_FAST | 20 | 0.1% | 99.7% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 20 | 0.1% | 99.8% |
| RESUME LOAD_DEREF | 20 | 0.1% | 99.8% |
| RESUME LOAD_GLOBAL | 20 | 0.1% | 99.9% |
| RESUME_CHECK LOAD_GLOBAL | 20 | 0.1% | 100.0% |


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
| LOAD_FAST | 4,000 | 90.9% |
| LOAD_ATTR_MODULE | 180 | 4.1% |
| LOAD_DEREF | 160 | 3.6% |
| LOAD_ATTR | 60 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,000 | 90.9% |
| CALL | 240 | 5.5% |
| LOAD_FAST | 160 | 3.6% |


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
| LOAD_FAST_LOAD_FAST | 400 | 54.1% |
| PUSH_NULL | 240 | 32.4% |
| CALL | 60 | 8.1% |
| LOAD_FAST | 40 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 280 | 37.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 200 | 27.0% |
| STORE_FAST | 100 | 13.5% |
| LOAD_FAST | 80 | 10.8% |
| CALL | 60 | 8.1% |


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
| POP_TOP | 3,600 | 78.9% |
| STORE_FAST | 640 | 14.0% |
| PUSH_NULL | 160 | 3.5% |
| CALL | 80 | 1.8% |
| LOAD_GLOBAL_BUILTIN | 60 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,000 | 87.7% |
| GET_ITER | 80 | 1.8% |
| BUILD_LIST | 80 | 1.8% |
| CALL_FUNCTION_EX | 80 | 1.8% |
| LOAD_ATTR | 80 | 1.8% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 3,600 | 90.0% |
| CALL | 400 | 10.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 40.0% |
| RETURN_VALUE | 40 | 20.0% |
| FOR_ITER_RANGE | 40 | 20.0% |
| RESUME | 20 | 10.0% |
| RESUME_CHECK | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 40.0% |
| LOAD_ATTR | 60 | 30.0% |
| LOAD_FAST | 20 | 10.0% |
| STORE_FAST | 20 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 10.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 380 | 47.5% |
| CALL | 100 | 12.5% |
| CALL_BUILTIN_CLASS | 60 | 7.5% |
| LOAD_ATTR_MODULE | 60 | 7.5% |
| LOAD_ATTR_WITH_HINT | 60 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 80.0% |
| LOAD_GLOBAL | 80 | 10.0% |
| LOAD_GLOBAL_MODULE | 80 | 10.0% |


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
| LOAD_FAST_LOAD_FAST | 3,600 | 94.7% |
| CALL | 200 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,800 | 100.0% |


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
| LOAD_GLOBAL | 80 | 33.3% |
| STORE_FAST | 80 | 33.3% |
| RETURN_VALUE | 40 | 16.7% |
| FOR_ITER_RANGE | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 120 | 50.0% |
| LOAD_ATTR | 60 | 25.0% |
| STORE_FAST | 60 | 25.0% |


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
|     deferred | 460 | 0.0% |
|          hit | 1,638,260 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 78.6% |
| Failure | 60 | 21.4% |

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
| Basic | 19,340 | 75.4% |
| Not specialized | 1,220 | 4.8% |
| Specialized hits | 5,100 | 19.9% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 460 | 65.7% |
| LOAD_ATTR | 100 | 14.3% |
| LOAD_GLOBAL | 100 | 14.3% |
| BINARY_OP | 20 | 2.9% |
| FOR_ITER | 20 | 2.9% |
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
| Allocations from freelist | 320 | 0.0% |
| Frees to freelist | 260 |  |
| Allocations | 11,612,440 | 100.0% |
| Allocations to 512 bytes | 6,697,220 | 57.7% |
| Allocations to 4 kbytes | 3,276,820 | 28.2% |
| Allocations over 4 kbytes | 1,638,400 | 14.1% |
| Frees | 11,612,402 |  |
| New values | 0 |  |
| Interpreter increfs | 10,160 | 0.0% |
| Interpreter decrefs | 14,660 | 0.0% |
| Increfs | 108,127,201 | 100.0% |
| Decrefs | 113,181,684 | 100.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 3,276,857 |  |
| Method cache misses | 63 |  |
| Method cache collisions | 55 |  |
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
