
# Pystats results

- benchmark: gc_collect
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 55,834,320 | 18.5% | 18.5% |  |
| STORE_ATTR_INSTANCE_VALUE | 43,007,920 | 14.3% | 32.8% |  |
| STORE_FAST | 22,038,400 | 7.3% | 40.1% |  |
| LOAD_FAST_LOAD_FAST | 22,021,520 | 7.3% | 47.4% |  |
| LOAD_CONST | 22,021,200 | 7.3% | 54.7% |  |
| RESUME_CHECK | 22,016,440 | 7.3% | 62.0% | 0.0% |
| RETURN_CONST | 22,016,000 | 7.3% | 69.2% |  |
| POP_TOP | 11,264,500 | 3.7% | 73.0% |  |
| CALL_PY_EXACT_ARGS | 11,264,320 | 3.7% | 76.7% |  |
| RETURN_VALUE | 10,757,240 | 3.6% | 80.3% |  |
| ENTER_EXECUTOR | 10,756,160 | 3.6% | 83.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 10,751,980 | 3.6% | 87.4% |  |
| EXIT_INIT_CHECK | 10,751,960 | 3.6% | 91.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 10,751,960 | 3.6% | 94.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,751,960 | 3.6% | 98.1% |  |
| LOAD_GLOBAL_MODULE | 1,041,100 | 0.3% | 98.4% |  |
| FOR_ITER_RANGE | 1,030,580 | 0.3% | 98.8% |  |
| POP_JUMP_IF_FALSE | 517,120 | 0.2% | 99.0% |  |
| COMPARE_OP_INT | 517,080 | 0.2% | 99.1% |  |
| GET_ITER | 512,480 | 0.2% | 99.3% |  |
| CALL_BUILTIN_CLASS | 512,420 | 0.2% | 99.5% |  |
| LOAD_GLOBAL_BUILTIN | 512,420 | 0.2% | 99.6% |  |
| CALL_LIST_APPEND | 511,980 | 0.2% | 99.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 511,980 | 0.2% | 100.0% |  |
| PUSH_NULL | 16,000 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 15,740 | 0.0% | 100.0% |  |
| CALL | 11,100 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,480 | 0.0% | 100.0% |  |
| DELETE_FAST | 5,120 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NOT_NONE | 5,120 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 5,100 | 0.0% | 100.0% | 1.2% |
| BINARY_OP_ADD_INT | 5,100 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 5,100 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 5,100 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,020 | 0.0% | 100.0% |  |
| BUILD_LIST | 480 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 480 | 0.0% | 100.0% |  |
| LOAD_ATTR | 360 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| BINARY_OP | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| STORE_ATTR | 160 | 0.0% | 100.0% |  |
| RESUME | 120 | 0.0% | 100.0% | 8,533.3% |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COMPARE_OP | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_CONST LOAD_FAST | 21,504,000 | 7.1% | 7.1% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 21,503,960 | 7.1% | 14.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 21,503,920 | 7.1% | 21.4% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,264,320 | 3.7% | 25.1% |
| RETURN_CONST POP_TOP | 11,264,000 | 3.7% | 28.8% |
| STORE_FAST LOAD_FAST | 10,762,240 | 3.6% | 32.4% |
| RETURN_VALUE STORE_FAST | 10,757,080 | 3.6% | 36.0% |
| RESUME_CHECK LOAD_CONST | 10,752,040 | 3.6% | 39.5% |
| LOAD_FAST STORE_FAST | 10,752,000 | 3.6% | 43.1% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 10,751,980 | 3.6% | 46.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 10,751,980 | 3.6% | 50.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 10,751,980 | 3.6% | 53.8% |
| EXIT_INIT_CHECK RETURN_VALUE | 10,751,960 | 3.6% | 57.4% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 10,751,960 | 3.6% | 60.9% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 10,751,960 | 3.6% | 64.5% |
| RETURN_CONST EXIT_INIT_CHECK | 10,751,960 | 3.6% | 68.0% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 10,751,960 | 3.6% | 71.6% |
| LOAD_ATTR_INSTANCE_VALUE STORE_ATTR_INSTANCE_VALUE | 10,751,960 | 3.6% | 75.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 10,751,960 | 3.6% | 78.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 10,751,920 | 3.6% | 82.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 10,751,920 | 3.6% | 85.9% |
| POP_TOP LOAD_FAST | 10,240,000 | 3.4% | 89.3% |
| STORE_FAST ENTER_EXECUTOR | 10,239,660 | 3.4% | 92.6% |
| ENTER_EXECUTOR CALL_ALLOC_AND_ENTER_INIT | 10,238,960 | 3.4% | 96.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 518,400 | 0.2% | 96.2% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 517,200 | 0.2% | 96.4% |
| FOR_ITER_RANGE LOAD_FAST | 517,200 | 0.2% | 96.6% |
| LOAD_FAST LOAD_CONST | 517,120 | 0.2% | 96.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 517,080 | 0.2% | 96.9% |
| FOR_ITER_RANGE STORE_FAST | 513,380 | 0.2% | 97.1% |
| LOAD_GLOBAL_MODULE CALL_ALLOC_AND_ENTER_INIT | 512,960 | 0.2% | 97.2% |
| GET_ITER FOR_ITER_RANGE | 512,420 | 0.2% | 97.4% |
| CALL_BUILTIN_CLASS GET_ITER | 512,420 | 0.2% | 97.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 512,420 | 0.2% | 97.7% |
| LOAD_FAST CALL_BUILTIN_CLASS | 512,360 | 0.2% | 97.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 512,360 | 0.2% | 98.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 512,360 | 0.2% | 98.3% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 512,320 | 0.2% | 98.4% |
| POP_TOP RETURN_CONST | 512,000 | 0.2% | 98.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 512,000 | 0.2% | 98.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 511,980 | 0.2% | 98.9% |
| RESUME_CHECK LOAD_FAST | 511,980 | 0.2% | 99.1% |
| LOAD_CONST COMPARE_OP_INT | 511,960 | 0.2% | 99.3% |
| LOAD_FAST CALL_LIST_APPEND | 511,960 | 0.2% | 99.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 511,960 | 0.2% | 99.6% |
| CALL_LIST_APPEND LOAD_GLOBAL_MODULE | 511,960 | 0.2% | 99.8% |
| POP_TOP ENTER_EXECUTOR | 511,660 | 0.2% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 15,740 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 15,640 | 0.0% | 100.0% |
| PUSH_NULL CALL | 10,400 | 0.0% | 100.0% |
| PUSH_NULL CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,440 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 5,200 | 0.0% | 100.0% |
| CALL STORE_FAST | 5,180 | 0.0% | 100.0% |
| CALL LOAD_FAST | 5,120 | 0.0% | 100.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 5,120 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 5,120 | 0.0% | 100.0% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 5,120 | 0.0% | 100.0% |
| STORE_FAST DELETE_FAST | 5,120 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 5,100 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 5,100 | 0.0% | 100.0% |
| DELETE_FAST LOAD_GLOBAL_MODULE | 5,080 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 5,080 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 5,080 | 0.0% | 100.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 5,080 | 0.0% | 100.0% |
| BINARY_OP_ADD_INT BINARY_OP_MULTIPLY_INT | 5,080 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_INT COMPARE_OP_INT | 5,080 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_FLOAT BINARY_OP_ADD_FLOAT | 5,080 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 4,780 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 900 | 0.0% | 100.0% |
| BUILD_LIST STORE_FAST | 400 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS POP_TOP | 380 | 0.0% | 100.0% |
| RESUME_CHECK BUILD_LIST | 380 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL_MODULE | 360 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| STORE_FAST JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| CALL CALL | 300 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 280 | 0.0% | 100.0% |
| LOAD_FAST CALL | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 180 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| CALL POP_TOP | 120 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 120 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 100 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_MODULE | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 100 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 100.0% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 100.0% |
| CALL CALL_PY_EXACT_ARGS | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |
| LOAD_CONST STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 100.0% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 20 | 50.0% |
| RESUME_CHECK | 20 | 50.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 10,751,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,751,960 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 512,420 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 512,420 | 100.0% |
| FOR_ITER | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 40 | 100.0% |


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
| RETURN_CONST | 11,264,000 | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 380 | 0.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240,000 | 90.9% |
| RETURN_CONST | 512,000 | 4.5% |
| ENTER_EXECUTOR | 511,660 | 4.5% |
| LOAD_GLOBAL_MODULE | 360 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 15,740 | 98.4% |
| LOAD_DEREF | 160 | 1.0% |
| LOAD_ATTR | 100 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 10,400 | 65.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,440 | 34.0% |
| LOAD_FAST | 160 | 1.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXIT_INIT_CHECK | 10,751,960 | 100.0% |
| LOAD_FAST | 5,200 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,757,080 | 100.0% |
| RETURN_VALUE | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 40 | 25.0% |
| LOAD_CONST | 40 | 25.0% |
| LOAD_FAST | 40 | 25.0% |
| BINARY_OP_ADD_INT | 20 | 12.5% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 40 | 25.0% |
| COMPARE_OP | 20 | 12.5% |
| STORE_FAST | 20 | 12.5% |
| BINARY_OP_ADD_FLOAT | 20 | 12.5% |
| BINARY_OP_ADD_INT | 20 | 12.5% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 380 | 79.2% |
| LOAD_FAST | 80 | 16.7% |
| RESUME | 20 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 400 | 83.3% |
| LOAD_DEREF | 80 | 16.7% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 10,400 | 93.7% |
| CALL | 300 | 2.7% |
| LOAD_FAST | 240 | 2.2% |
| LOAD_FAST_LOAD_FAST | 80 | 0.7% |
| LOAD_GLOBAL | 40 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,180 | 46.7% |
| LOAD_FAST | 5,120 | 46.1% |
| CALL | 300 | 2.7% |
| POP_TOP | 120 | 1.1% |
| CALL_PY_EXACT_ARGS | 80 | 0.7% |


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
| LOAD_CONST | 40 | 50.0% |
| BINARY_OP | 20 | 25.0% |
| BINARY_OP_MULTIPLY_INT | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 50.0% |
| COMPARE_OP_INT | 40 | 50.0% |


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

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,080 | 99.2% |
| LOAD_GLOBAL | 40 | 0.8% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,239,660 | 95.2% |
| POP_TOP | 511,660 | 4.8% |
| POP_JUMP_IF_FALSE | 4,780 | 0.0% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ALLOC_AND_ENTER_INIT | 10,238,960 | 95.2% |
| FOR_ITER_RANGE | 517,200 | 4.8% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 50.0% |
| JUMP_BACKWARD | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 50.0% |
| FOR_ITER_RANGE | 60 | 50.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 33.3% |
| POP_JUMP_IF_FALSE | 340 | 33.3% |
| STORE_FAST | 340 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 900 | 88.2% |
| ENTER_EXECUTOR | 60 | 5.9% |
| FOR_ITER | 60 | 5.9% |


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
| LOAD_FAST | 120 | 33.3% |
| LOAD_GLOBAL | 100 | 27.8% |
| LOAD_GLOBAL_MODULE | 100 | 27.8% |
| LOAD_FAST_LOAD_FAST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 100 | 27.8% |
| LOAD_ATTR_MODULE | 100 | 27.8% |
| LOAD_FAST | 60 | 16.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 11.1% |
| STORE_ATTR | 20 | 5.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,752,040 | 48.8% |
| STORE_ATTR_INSTANCE_VALUE | 10,751,980 | 48.8% |
| LOAD_FAST | 517,120 | 2.3% |
| RESUME | 40 | 0.0% |
| STORE_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,504,000 | 97.7% |
| COMPARE_OP_INT | 511,960 | 2.3% |
| BINARY_OP_ADD_INT | 5,080 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| BINARY_OP | 40 | 0.0% |


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
| LOAD_CONST | 21,504,000 | 38.5% |
| STORE_FAST | 10,762,240 | 19.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,751,960 | 19.3% |
| POP_TOP | 10,240,000 | 18.3% |
| FOR_ITER_RANGE | 517,200 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 21,503,920 | 38.5% |
| STORE_FAST | 10,752,000 | 19.3% |
| CALL_PY_EXACT_ARGS | 10,751,920 | 19.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,751,920 | 19.3% |
| LOAD_CONST | 517,120 | 0.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,751,980 | 48.8% |
| STORE_ATTR_INSTANCE_VALUE | 10,751,980 | 48.8% |
| LOAD_GLOBAL_MODULE | 512,360 | 2.3% |
| POP_JUMP_IF_NOT_NONE | 5,120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 10,751,960 | 48.8% |
| STORE_ATTR_INSTANCE_VALUE | 10,751,960 | 48.8% |
| CALL_PY_EXACT_ARGS | 512,320 | 2.3% |
| LOAD_FAST | 5,120 | 0.0% |
| CALL | 80 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 280 | 58.3% |
| POP_TOP | 60 | 12.5% |
| RETURN_VALUE | 40 | 8.3% |
| DELETE_FAST | 40 | 8.3% |
| LOAD_FAST | 40 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 180 | 37.5% |
| LOAD_ATTR | 100 | 20.8% |
| LOAD_FAST | 60 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 60 | 12.5% |
| CALL | 40 | 8.3% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 517,080 | 100.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 512,000 | 99.0% |
| ENTER_EXECUTOR | 4,780 | 0.9% |
| JUMP_BACKWARD | 340 | 0.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,120 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 21,503,960 | 97.7% |
| POP_TOP | 512,000 | 2.3% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,264,000 | 51.2% |
| EXIT_INIT_CHECK | 10,751,960 | 48.8% |
| INTERPRETER_EXIT | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| LOAD_FAST_LOAD_FAST | 40 | 25.0% |
| LOAD_ATTR | 20 | 12.5% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 80 | 50.0% |
| RETURN_CONST | 40 | 25.0% |
| LOAD_CONST | 20 | 12.5% |
| LOAD_FAST_LOAD_FAST | 20 | 12.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,757,080 | 48.8% |
| LOAD_FAST | 10,752,000 | 48.8% |
| FOR_ITER_RANGE | 513,380 | 2.3% |
| CALL | 5,180 | 0.0% |
| BINARY_OP_ADD_FLOAT | 5,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,762,240 | 48.8% |
| ENTER_EXECUTOR | 10,239,660 | 46.5% |
| LOAD_GLOBAL_MODULE | 518,400 | 2.4% |
| LOAD_GLOBAL_BUILTIN | 512,360 | 2.3% |
| DELETE_FAST | 5,120 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 60 | 50.0% |
| CACHE | 20 | 16.7% |
| CALL_FUNCTION_EX | 20 | 16.7% |
| COPY_FREE_VARS | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 33.3% |
| BUILD_LIST | 20 | 16.7% |
| LOAD_DEREF | 20 | 16.7% |
| LOAD_FAST | 20 | 16.7% |
| LOAD_FAST_LOAD_FAST | 20 | 16.7% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,100 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 5,080 | 99.6% |
| COMPARE_OP | 20 | 0.4% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 10,238,960 | 95.2% |
| LOAD_GLOBAL_MODULE | 512,960 | 4.8% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,751,960 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 512,360 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 512,420 | 100.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 5,440 | 99.3% |
| CALL | 40 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,100 | 93.1% |
| POP_TOP | 380 | 6.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 511,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 511,960 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,751,920 | 95.5% |
| LOAD_FAST_LOAD_FAST | 512,320 | 4.5% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,264,320 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 511,960 | 99.0% |
| BINARY_OP_MULTIPLY_INT | 5,080 | 1.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 517,080 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 517,200 | 50.2% |
| GET_ITER | 512,420 | 49.7% |
| JUMP_BACKWARD | 900 | 0.1% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 517,200 | 50.2% |
| STORE_FAST | 513,380 | 49.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,751,960 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 10,751,960 | 100.0% |
| STORE_ATTR | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 511,960 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 511,980 | 100.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,751,920 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,751,960 | 100.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 15,640 | 99.4% |
| LOAD_ATTR | 100 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 15,740 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 512,360 | 100.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 512,420 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 518,400 | 49.8% |
| CALL_LIST_APPEND | 511,960 | 49.2% |
| DELETE_FAST | 5,080 | 0.5% |
| LOAD_FAST | 5,080 | 0.5% |
| POP_TOP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ALLOC_AND_ENTER_INIT | 512,960 | 49.3% |
| LOAD_FAST_LOAD_FAST | 512,360 | 49.2% |
| LOAD_ATTR_MODULE | 15,640 | 1.5% |
| LOAD_ATTR | 100 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,264,320 | 51.2% |
| CALL_ALLOC_AND_ENTER_INIT | 10,751,960 | 48.8% |
| CALL_FUNCTION_EX | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |
| CACHE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,752,040 | 48.8% |
| LOAD_FAST_LOAD_FAST | 10,751,980 | 48.8% |
| LOAD_FAST | 511,980 | 2.3% |
| BUILD_LIST | 380 | 0.0% |
| LOAD_DEREF | 60 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,503,920 | 50.0% |
| LOAD_FAST_LOAD_FAST | 10,751,960 | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE | 10,751,960 | 25.0% |
| STORE_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 21,503,960 | 50.0% |
| LOAD_CONST | 10,751,980 | 25.0% |
| LOAD_FAST_LOAD_FAST | 10,751,980 | 25.0% |


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
|     deferred | 140 | 0.7% |
|          hit | 20,340 | 98.9% |
|         miss | 60 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,560 | 0.0% |
|          hit | 23,060,320 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 44.4% |
| Failure | 300 | 55.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 300 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 517,080 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 1,030,580 | 100.0% |

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
|     deferred | 180 | 0.0% |
|          hit | 22,036,380 | 100.0% |

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
|     deferred | 240 | 0.0% |
|          hit | 1,553,520 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 43,007,920 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 187,997,280 | 62.3% |
| Not specialized | 534,700 | 0.2% |
| Specialized hits | 113,213,460 | 37.5% |
| Specialized misses | 10,300 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 10,560 | 93.5% |
| LOAD_GLOBAL | 240 | 2.1% |
| LOAD_ATTR | 180 | 1.6% |
| BINARY_OP | 140 | 1.2% |
| STORE_ATTR | 80 | 0.7% |
| FOR_ITER | 60 | 0.5% |
| COMPARE_OP | 40 | 0.4% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| CACHE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| RESUME | 10,240 | 49.9% |
| RESUME_CHECK | 10,240 | 49.9% |
| BINARY_OP_ADD_FLOAT | 60 | 0.3% |
| CACHE | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
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
| Calls to PyEval_EvalDefault | 40 | 0.0% |
| Calls to Python functions inlined | 22,021,240 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 40 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 40 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 40 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 32,773,240 | 148.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 60 | 0.0% |
| Frees to freelist | 16,180 |  |
| Allocations | 22,605,300 | 100.0% |
| Allocations to 512 bytes | 22,605,280 | 100.0% |
| Allocations to 4 kbytes | 20 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 22,619,366 |  |
| New values | 40 |  |
| Interpreter increfs | 175,679,820 | 84.9% |
| Interpreter decrefs | 175,719,920 | 80.3% |
| Increfs | 31,251,260 | 15.1% |
| Decrefs | 43,070,068 | 19.7% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 337 |  |
| Method cache misses | 83 |  |
| Method cache collisions | 64 |  |
| Method cache dunder hits | 60 |  |
| Method cache dunder misses | 20 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 10,240 | 0 | 43,345,920 |
| 1 | 0 | 0 | 0 |
| 2 | 10,240 | 10,753,920 | 1,245,058,160 |


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
| <= 16 | 40 | 66.7% |
| <= 32 | 0 | 0.0% |
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
| <= 16 | 40 | 66.7% |
| <= 32 | 0 | 0.0% |
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
| CALL_ALLOC_AND_ENTER_INIT | 60 |


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
