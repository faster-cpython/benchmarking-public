
# Pystats results

- benchmark: pickle_dict
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 2,480 | 14.3% | 14.3% |  |
| PUSH_NULL | 2,400 | 13.8% | 28.0% |  |
| POP_TOP | 2,080 | 12.0% | 40.0% |  |
| LOAD_ATTR_MODULE | 2,080 | 12.0% | 52.0% |  |
| LOAD_FAST_LOAD_FAST | 2,000 | 11.5% | 63.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,900 | 10.9% | 74.4% |  |
| STORE_FAST | 720 | 4.1% | 78.5% |  |
| CALL | 540 | 3.1% | 81.6% |  |
| FOR_ITER_RANGE | 460 | 2.6% | 84.3% |  |
| LOAD_ATTR | 360 | 2.1% | 86.3% |  |
| JUMP_BACKWARD | 340 | 2.0% | 88.3% |  |
| LOAD_DEREF | 240 | 1.4% | 89.7% |  |
| LOAD_GLOBAL_MODULE | 240 | 1.4% | 91.0% |  |
| LOAD_GLOBAL | 200 | 1.1% | 92.2% |  |
| RETURN_VALUE | 160 | 0.9% | 93.1% |  |
| CALL_FUNCTION_EX | 160 | 0.9% | 94.0% |  |
| RESUME_CHECK | 120 | 0.7% | 94.7% |  |
| GET_ITER | 80 | 0.5% | 95.2% |  |
| NOP | 80 | 0.5% | 95.6% |  |
| BUILD_LIST | 80 | 0.5% | 96.1% |  |
| CALL_INTRINSIC_1 | 80 | 0.5% | 96.6% |  |
| COPY_FREE_VARS | 80 | 0.5% | 97.0% |  |
| ENTER_EXECUTOR | 80 | 0.5% | 97.5% |  |
| LIST_EXTEND | 80 | 0.5% | 97.9% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.3% | 98.3% |  |
| CALL_BUILTIN_CLASS | 60 | 0.3% | 98.6% |  |
| LOAD_ATTR_WITH_HINT | 60 | 0.3% | 99.0% |  |
| LOAD_GLOBAL_BUILTIN | 60 | 0.3% | 99.3% |  |
| BINARY_OP | 40 | 0.2% | 99.5% |  |
| FOR_ITER | 40 | 0.2% | 99.8% |  |
| RESUME | 40 | 0.2% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_ATTR_MODULE PUSH_NULL | 2,080 | 12.0% | 12.0% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 2,000 | 11.5% | 23.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 1,900 | 10.9% | 34.4% |
| LOAD_FAST LOAD_ATTR_MODULE | 1,800 | 10.3% | 44.7% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,800 | 10.3% | 55.1% |
| POP_TOP LOAD_FAST | 1,600 | 9.2% | 64.3% |
| STORE_FAST LOAD_FAST | 560 | 3.2% | 67.5% |
| FOR_ITER_RANGE STORE_FAST | 380 | 2.2% | 69.7% |
| POP_TOP JUMP_BACKWARD | 340 | 2.0% | 71.6% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 1.7% | 73.3% |
| PUSH_NULL CALL | 240 | 1.4% | 74.7% |
| LOAD_FAST LOAD_ATTR | 240 | 1.4% | 76.1% |
| LOAD_FAST_LOAD_FAST CALL | 200 | 1.1% | 77.2% |
| CALL POP_TOP | 180 | 1.0% | 78.3% |
| PUSH_NULL LOAD_FAST | 160 | 0.9% | 79.2% |
| LOAD_ATTR PUSH_NULL | 160 | 0.9% | 80.1% |
| LOAD_ATTR LOAD_ATTR_MODULE | 160 | 0.9% | 81.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.9% | 82.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.7% | 82.6% |
| CALL STORE_FAST | 100 | 0.6% | 83.2% |
| CALL CALL_BUILTIN_FAST_WITH_KEYWORDS | 100 | 0.6% | 83.8% |
| NOP LOAD_DEREF | 80 | 0.5% | 84.3% |
| POP_TOP NOP | 80 | 0.5% | 84.7% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.5% | 85.2% |
| BUILD_LIST LOAD_DEREF | 80 | 0.5% | 85.6% |
| CALL LOAD_FAST | 80 | 0.5% | 86.1% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.5% | 86.6% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.5% | 87.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.5% | 87.5% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.5% | 87.9% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.5% | 88.4% |
| LOAD_FAST GET_ITER | 80 | 0.5% | 88.9% |
| LOAD_FAST BUILD_LIST | 80 | 0.5% | 89.3% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.5% | 89.8% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 80 | 0.5% | 90.2% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.5% | 90.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 80 | 0.5% | 91.1% |
| GET_ITER FOR_ITER_RANGE | 60 | 0.3% | 91.5% |
| POP_TOP ENTER_EXECUTOR | 60 | 0.3% | 91.8% |
| CALL CALL | 60 | 0.3% | 92.2% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.3% | 92.5% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.3% | 92.9% |
| LOAD_GLOBAL LOAD_ATTR | 60 | 0.3% | 93.2% |
| BINARY_OP_SUBTRACT_FLOAT RETURN_VALUE | 60 | 0.3% | 93.6% |
| CALL_BUILTIN_CLASS STORE_FAST | 60 | 0.3% | 93.9% |
| LOAD_ATTR_WITH_HINT STORE_FAST | 60 | 0.3% | 94.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 60 | 0.3% | 94.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 60 | 0.3% | 94.9% |
| LOAD_GLOBAL_MODULE STORE_FAST | 60 | 0.3% | 95.3% |
| RESUME_CHECK LOAD_DEREF | 60 | 0.3% | 95.6% |
| RETURN_VALUE LOAD_GLOBAL | 40 | 0.2% | 95.9% |
| RETURN_VALUE LOAD_GLOBAL_MODULE | 40 | 0.2% | 96.1% |
| LOAD_FAST BINARY_OP | 40 | 0.2% | 96.3% |
| LOAD_FAST CALL | 40 | 0.2% | 96.6% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 40 | 0.2% | 96.8% |
| LOAD_FAST CALL_BUILTIN_CLASS | 40 | 0.2% | 97.0% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 40 | 0.2% | 97.2% |
| FOR_ITER_RANGE LOAD_GLOBAL | 40 | 0.2% | 97.5% |
| FOR_ITER_RANGE LOAD_GLOBAL_MODULE | 40 | 0.2% | 97.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 40 | 0.2% | 97.9% |
| GET_ITER FOR_ITER | 20 | 0.1% | 98.0% |
| BINARY_OP RETURN_VALUE | 20 | 0.1% | 98.2% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 20 | 0.1% | 98.3% |
| CALL CALL_BUILTIN_CLASS | 20 | 0.1% | 98.4% |
| CALL_FUNCTION_EX RESUME | 20 | 0.1% | 98.5% |
| COPY_FREE_VARS RESUME | 20 | 0.1% | 98.6% |
| FOR_ITER STORE_FAST | 20 | 0.1% | 98.7% |
| FOR_ITER FOR_ITER_RANGE | 20 | 0.1% | 98.9% |
| JUMP_BACKWARD ENTER_EXECUTOR | 20 | 0.1% | 99.0% |
| JUMP_BACKWARD FOR_ITER | 20 | 0.1% | 99.1% |
| LOAD_ATTR STORE_FAST | 20 | 0.1% | 99.2% |
| LOAD_ATTR LOAD_ATTR_WITH_HINT | 20 | 0.1% | 99.3% |
| LOAD_GLOBAL LOAD_FAST | 20 | 0.1% | 99.4% |
| LOAD_GLOBAL STORE_FAST | 20 | 0.1% | 99.5% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 20 | 0.1% | 99.7% |
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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,900 | 91.3% |
| CALL | 180 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,600 | 76.9% |
| JUMP_BACKWARD | 340 | 16.3% |
| NOP | 80 | 3.8% |
| ENTER_EXECUTOR | 60 | 2.9% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,080 | 86.7% |
| LOAD_ATTR | 160 | 6.7% |
| LOAD_DEREF | 160 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,000 | 83.3% |
| CALL | 240 | 10.0% |
| LOAD_FAST | 160 | 6.7% |


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
| PUSH_NULL | 240 | 44.4% |
| LOAD_FAST_LOAD_FAST | 200 | 37.0% |
| CALL | 60 | 11.1% |
| LOAD_FAST | 40 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 180 | 33.3% |
| STORE_FAST | 100 | 18.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 100 | 18.5% |
| LOAD_FAST | 80 | 14.8% |
| CALL | 60 | 11.1% |


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
| LOAD_FAST | 240 | 66.7% |
| LOAD_GLOBAL | 60 | 16.7% |
| LOAD_GLOBAL_MODULE | 60 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 160 | 44.4% |
| LOAD_ATTR_MODULE | 160 | 44.4% |
| STORE_FAST | 20 | 5.6% |
| LOAD_ATTR_WITH_HINT | 20 | 5.6% |


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
| POP_TOP | 1,600 | 64.5% |
| STORE_FAST | 560 | 22.6% |
| PUSH_NULL | 160 | 6.5% |
| CALL | 80 | 3.2% |
| LOAD_GLOBAL_BUILTIN | 60 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,800 | 72.6% |
| LOAD_ATTR | 240 | 9.7% |
| GET_ITER | 80 | 3.2% |
| BUILD_LIST | 80 | 3.2% |
| CALL_FUNCTION_EX | 80 | 3.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,800 | 90.0% |
| CALL | 200 | 10.0% |


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
| FOR_ITER_RANGE | 380 | 52.8% |
| CALL | 100 | 13.9% |
| CALL_BUILTIN_CLASS | 60 | 8.3% |
| LOAD_ATTR_WITH_HINT | 60 | 8.3% |
| LOAD_GLOBAL_MODULE | 60 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 77.8% |
| LOAD_GLOBAL | 80 | 11.1% |
| LOAD_GLOBAL_MODULE | 80 | 11.1% |


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
| LOAD_FAST_LOAD_FAST | 1,800 | 94.7% |
| CALL | 100 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,900 | 100.0% |


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
| LOAD_FAST | 1,800 | 86.5% |
| LOAD_ATTR | 160 | 7.7% |
| LOAD_GLOBAL_MODULE | 120 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,080 | 100.0% |


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
|     deferred | 360 | 0.1% |
|          hit | 409,560 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 66.7% |
| Failure | 60 | 33.3% |

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
|     deferred | 180 | 0.0% |
|          hit | 409,740 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
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
| Basic | 11,180 | 64.3% |
| Not specialized | 1,180 | 6.8% |
| Specialized hits | 5,040 | 29.0% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 360 | 52.9% |
| LOAD_ATTR | 180 | 26.5% |
| LOAD_GLOBAL | 100 | 14.7% |
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
| Allocations | 3,338,520 | 100.0% |
| Allocations to 512 bytes | 1,700,100 | 50.9% |
| Allocations to 4 kbytes | 819,220 | 24.5% |
| Allocations over 4 kbytes | 819,200 | 24.5% |
| Frees | 3,338,482 |  |
| New values | 0 |  |
| Interpreter increfs | 7,920 | 0.0% |
| Interpreter decrefs | 10,500 | 0.0% |
| Increfs | 84,782,162 | 100.0% |
| Decrefs | 86,070,248 | 100.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 819,333 |  |
| Method cache misses | 67 |  |
| Method cache collisions | 58 |  |
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
| <= 64 | 20 | 100.0% |


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
