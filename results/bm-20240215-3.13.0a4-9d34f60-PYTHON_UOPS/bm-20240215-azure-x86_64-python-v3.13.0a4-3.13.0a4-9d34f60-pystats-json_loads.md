
# Pystats results

- benchmark: json_loads
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 22,099,180 | 22.4% | 22.4% |  |
| POP_JUMP_IF_NOT_NONE | 7,372,800 | 7.5% | 29.9% |  |
| CALL | 6,171,200 | 6.3% | 36.2% |  |
| LOAD_FAST_LOAD_FAST | 4,915,200 | 5.0% | 41.2% |  |
| RESUME_CHECK | 3,706,860 | 3.8% | 44.9% |  |
| RETURN_VALUE | 3,686,480 | 3.7% | 48.7% |  |
| LOAD_CONST | 3,686,480 | 3.7% | 52.4% |  |
| POP_JUMP_IF_FALSE | 3,686,480 | 3.7% | 56.2% |  |
| LOAD_GLOBAL_BUILTIN | 3,686,400 | 3.7% | 59.9% |  |
| LOAD_ATTR_METHOD_NO_DICT | 3,686,340 | 3.7% | 63.7% |  |
| PUSH_NULL | 3,646,380 | 3.7% | 67.4% |  |
| STORE_FAST_STORE_FAST | 2,457,600 | 2.5% | 69.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 2,457,560 | 2.5% | 72.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,457,560 | 2.5% | 74.9% |  |
| TO_BOOL_BOOL | 2,457,560 | 2.5% | 77.3% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,457,560 | 2.5% | 79.8% |  |
| LOAD_GLOBAL_MODULE | 2,416,560 | 2.5% | 82.3% |  |
| STORE_FAST | 1,250,300 | 1.3% | 83.6% |  |
| POP_TOP | 1,249,360 | 1.3% | 84.8% |  |
| TO_BOOL | 1,229,380 | 1.2% | 86.1% |  |
| NOP | 1,228,880 | 1.2% | 87.3% |  |
| COMPARE_OP_INT | 1,228,840 | 1.2% | 88.6% |  |
| BUILD_TUPLE | 1,228,800 | 1.2% | 89.8% |  |
| CALL_KW | 1,228,800 | 1.2% | 91.1% |  |
| JUMP_FORWARD | 1,228,800 | 1.2% | 92.3% |  |
| POP_JUMP_IF_TRUE | 1,228,800 | 1.2% | 93.6% |  |
| CALL_ISINSTANCE | 1,228,780 | 1.2% | 94.8% |  |
| CALL_LEN | 1,228,780 | 1.2% | 96.1% |  |
| CALL_PY_WITH_DEFAULTS | 1,228,780 | 1.2% | 97.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,780 | 1.2% | 98.6% |  |
| LOAD_ATTR_MODULE | 1,187,780 | 1.2% | 99.8% |  |
| ENTER_EXECUTOR | 81,280 | 0.1% | 99.8% |  |
| EXTENDED_ARG | 41,520 | 0.0% | 99.9% |  |
| FOR_ITER_TUPLE | 41,160 | 0.0% | 99.9% |  |
| GET_ITER | 20,560 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 20,480 | 0.0% | 100.0% |  |
| RETURN_CONST | 20,480 | 0.0% | 100.0% |  |
| LOAD_ATTR | 1,120 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 1,080 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 680 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 460 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| RESUME | 100 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COMPARE_OP | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| FOR_ITER | 80 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 60 | 0.0% | 100.0% |  |
| BINARY_OP | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 7,372,800 | 7.5% | 7.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 7,372,800 | 7.5% | 15.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,457,620 | 2.5% | 17.5% |
| LOAD_CONST CALL | 2,457,600 | 2.5% | 20.0% |
| LOAD_FAST_LOAD_FAST CALL | 2,457,600 | 2.5% | 22.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 2,457,600 | 2.5% | 25.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,457,560 | 2.5% | 27.5% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 2,457,560 | 2.5% | 29.9% |
| CALL LOAD_ATTR_METHOD_NO_DICT | 2,457,520 | 2.5% | 32.4% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 2,457,520 | 2.5% | 34.9% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_FAST | 2,457,520 | 2.5% | 37.4% |
| PUSH_NULL LOAD_FAST | 2,416,940 | 2.5% | 39.9% |
| RESUME_CHECK LOAD_FAST | 1,249,240 | 1.3% | 41.2% |
| STORE_FAST LOAD_FAST | 1,229,520 | 1.2% | 42.4% |
| LOAD_FAST PUSH_NULL | 1,229,360 | 1.2% | 43.7% |
| LOAD_FAST RETURN_VALUE | 1,228,880 | 1.2% | 44.9% |
| LOAD_FAST LOAD_CONST | 1,228,880 | 1.2% | 46.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,228,840 | 1.2% | 47.4% |
| NOP LOAD_FAST | 1,228,800 | 1.2% | 48.6% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 1,228,800 | 1.2% | 49.9% |
| RETURN_VALUE POP_TOP | 1,228,800 | 1.2% | 51.1% |
| RETURN_VALUE RETURN_VALUE | 1,228,800 | 1.2% | 52.4% |
| TO_BOOL POP_JUMP_IF_TRUE | 1,228,800 | 1.2% | 53.6% |
| BUILD_TUPLE RETURN_VALUE | 1,228,800 | 1.2% | 54.9% |
| JUMP_FORWARD LOAD_FAST | 1,228,800 | 1.2% | 56.1% |
| LOAD_CONST CALL_KW | 1,228,800 | 1.2% | 57.4% |
| LOAD_FAST TO_BOOL | 1,228,800 | 1.2% | 58.6% |
| LOAD_FAST_LOAD_FAST PUSH_NULL | 1,228,800 | 1.2% | 59.9% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 1,228,800 | 1.2% | 61.1% |
| POP_JUMP_IF_FALSE JUMP_FORWARD | 1,228,800 | 1.2% | 62.4% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,228,800 | 1.2% | 63.6% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 1,228,800 | 1.2% | 64.9% |
| CALL RESUME_CHECK | 1,228,780 | 1.2% | 66.1% |
| CALL_KW RESUME_CHECK | 1,228,780 | 1.2% | 67.4% |
| CALL_METHOD_DESCRIPTOR_FAST LOAD_CONST | 1,228,780 | 1.2% | 68.6% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 1,228,780 | 1.2% | 69.9% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 1,228,780 | 1.2% | 71.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 1,228,780 | 1.2% | 72.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 1,228,780 | 1.2% | 73.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 1,228,780 | 1.2% | 74.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 1,228,780 | 1.2% | 76.1% |
| RESUME_CHECK NOP | 1,228,780 | 1.2% | 77.3% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 1,228,760 | 1.2% | 78.6% |
| CALL TO_BOOL_BOOL | 1,228,760 | 1.2% | 79.8% |
| CALL UNPACK_SEQUENCE_TWO_TUPLE | 1,228,760 | 1.2% | 81.1% |
| LOAD_FAST CALL_LEN | 1,228,760 | 1.2% | 82.3% |
| LOAD_FAST CALL_PY_WITH_DEFAULTS | 1,228,760 | 1.2% | 83.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,228,760 | 1.2% | 84.8% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,228,760 | 1.2% | 86.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,228,760 | 1.2% | 87.3% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_MODULE | 1,228,760 | 1.2% | 88.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,228,760 | 1.2% | 89.8% |
| CALL_LEN COMPARE_OP_INT | 1,228,760 | 1.2% | 91.1% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 1,228,760 | 1.2% | 92.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_METHOD_WITH_VALUES | 1,228,760 | 1.2% | 93.6% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,228,760 | 1.2% | 94.8% |
| LOAD_FAST CALL | 1,188,180 | 1.2% | 96.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,187,720 | 1.2% | 97.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 1,187,340 | 1.2% | 98.4% |
| POP_TOP LOAD_GLOBAL_MODULE | 1,166,600 | 1.2% | 99.6% |
| POP_TOP ENTER_EXECUTOR | 81,240 | 0.1% | 99.7% |
| ENTER_EXECUTOR CALL | 60,820 | 0.1% | 99.8% |
| EXTENDED_ARG FOR_ITER_TUPLE | 41,140 | 0.0% | 99.8% |
| FOR_ITER_TUPLE STORE_FAST | 20,680 | 0.0% | 99.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 20,660 | 0.0% | 99.8% |
| CALL POP_TOP | 20,560 | 0.0% | 99.9% |
| LOAD_FAST GET_ITER | 20,560 | 0.0% | 99.9% |
| GET_ITER EXTENDED_ARG | 20,480 | 0.0% | 99.9% |
| RETURN_CONST INTERPRETER_EXIT | 20,480 | 0.0% | 99.9% |
| FOR_ITER_TUPLE RETURN_CONST | 20,480 | 0.0% | 99.9% |
| CACHE RESUME_CHECK | 20,460 | 0.0% | 100.0% |
| ENTER_EXECUTOR EXTENDED_ARG | 20,380 | 0.0% | 100.0% |
| CALL CALL | 6,240 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL | 760 | 0.0% | 100.0% |
| PUSH_NULL CALL | 640 | 0.0% | 100.0% |
| TO_BOOL TO_BOOL | 500 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 460 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 460 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 460 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_MODULE | 440 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 420 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 380 | 0.0% | 100.0% |
| POP_TOP EXTENDED_ARG | 340 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| EXTENDED_ARG JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| JUMP_BACKWARD EXTENDED_ARG | 320 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 0.0% | 100.0% |
| CALL STORE_FAST | 120 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 120 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| CALL LOAD_ATTR | 80 | 0.0% | 100.0% |
| CALL LOAD_FAST | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 80 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 80 | 0.0% | 100.0% |
| LOAD_DEREF STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LOAD_FAST LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 80 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,460 | 99.9% |
| RESUME | 20 | 0.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 20,480 | 99.6% |
| FOR_ITER_RANGE | 60 | 0.3% |
| FOR_ITER | 20 | 0.1% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 20,480 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,228,780 | 100.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,800 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,228,800 | 98.4% |
| CALL | 20,560 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,166,600 | 93.4% |
| ENTER_EXECUTOR | 81,240 | 6.5% |
| LOAD_GLOBAL | 760 | 0.1% |
| EXTENDED_ARG | 340 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,360 | 33.7% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 33.7% |
| LOAD_ATTR_MODULE | 1,187,720 | 32.6% |
| LOAD_ATTR | 420 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,416,940 | 66.3% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 33.7% |
| CALL | 640 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,880 | 33.3% |
| RETURN_VALUE | 1,228,800 | 33.3% |
| BUILD_TUPLE | 1,228,800 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,228,800 | 33.3% |
| RETURN_VALUE | 1,228,800 | 33.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,228,760 | 33.3% |
| LOAD_GLOBAL | 40 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,800 | 100.0% |
| TO_BOOL | 500 | 0.0% |
| CALL | 60 | 0.0% |
| CALL_ISINSTANCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,228,800 | 100.0% |
| TO_BOOL | 500 | 0.0% |
| POP_JUMP_IF_FALSE | 40 | 0.0% |
| TO_BOOL_BOOL | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 50.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 50.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,228,800 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,457,600 | 39.8% |
| LOAD_FAST_LOAD_FAST | 2,457,600 | 39.8% |
| LOAD_FAST | 1,188,180 | 19.3% |
| ENTER_EXECUTOR | 60,820 | 1.0% |
| CALL | 6,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,457,520 | 39.8% |
| RESUME_CHECK | 1,228,780 | 19.9% |
| TO_BOOL_BOOL | 1,228,760 | 19.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,228,760 | 19.9% |
| POP_TOP | 20,560 | 0.3% |


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

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,228,780 | 100.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 50.0% |
| CALL | 20 | 25.0% |
| CALL_LEN | 20 | 25.0% |

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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 81,240 | 100.0% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 60,820 | 74.8% |
| EXTENDED_ARG | 20,380 | 25.1% |
| FOR_ITER_RANGE | 80 | 0.1% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20,480 | 49.3% |
| ENTER_EXECUTOR | 20,380 | 49.1% |
| POP_TOP | 340 | 0.8% |
| JUMP_BACKWARD | 320 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 41,140 | 99.1% |
| JUMP_BACKWARD | 340 | 0.8% |
| FOR_ITER | 40 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 40 | 50.0% |
| GET_ITER | 20 | 25.0% |
| JUMP_BACKWARD | 20 | 25.0% |

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
| EXTENDED_ARG | 340 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 320 | 47.1% |
| FOR_ITER_RANGE | 300 | 44.1% |
| ENTER_EXECUTOR | 40 | 5.9% |
| FOR_ITER | 20 | 2.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,800 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 460 | 41.1% |
| LOAD_GLOBAL_MODULE | 460 | 41.1% |
| LOAD_FAST | 120 | 10.7% |
| CALL | 80 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 440 | 39.3% |
| PUSH_NULL | 420 | 37.5% |
| LOAD_ATTR_METHOD_NO_DICT | 60 | 5.4% |
| CALL | 40 | 3.6% |
| LOAD_FAST_LOAD_FAST | 40 | 3.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,880 | 33.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,228,780 | 33.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,228,780 | 33.3% |
| CALL | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,457,600 | 66.7% |
| CALL_KW | 1,228,800 | 33.3% |
| COMPARE_OP | 40 | 0.0% |
| COMPARE_OP_INT | 40 | 0.0% |


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
| POP_JUMP_IF_NOT_NONE | 7,372,800 | 33.4% |
| LOAD_GLOBAL_BUILTIN | 2,457,620 | 11.1% |
| POP_JUMP_IF_FALSE | 2,457,600 | 11.1% |
| PUSH_NULL | 2,416,940 | 10.9% |
| RESUME_CHECK | 1,249,240 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 7,372,800 | 33.4% |
| LOAD_GLOBAL_BUILTIN | 2,457,520 | 11.1% |
| PUSH_NULL | 1,229,360 | 5.6% |
| RETURN_VALUE | 1,228,880 | 5.6% |
| LOAD_CONST | 1,228,880 | 5.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,228,800 | 25.0% |
| STORE_FAST_STORE_FAST | 1,228,800 | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,780 | 25.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,228,780 | 25.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,457,600 | 50.0% |
| PUSH_NULL | 1,228,800 | 25.0% |
| BUILD_TUPLE | 1,228,800 | 25.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 760 | 70.4% |
| LOAD_FAST | 80 | 7.4% |
| RETURN_VALUE | 40 | 3.7% |
| POP_JUMP_IF_FALSE | 40 | 3.7% |
| POP_JUMP_IF_TRUE | 40 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 460 | 42.6% |
| LOAD_GLOBAL_MODULE | 460 | 42.6% |
| LOAD_GLOBAL_BUILTIN | 80 | 7.4% |
| LOAD_FAST | 60 | 5.6% |
| CALL | 20 | 1.9% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,457,560 | 66.7% |
| COMPARE_OP_INT | 1,228,840 | 33.3% |
| TO_BOOL | 40 | 0.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,457,600 | 66.7% |
| JUMP_FORWARD | 1,228,800 | 33.3% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,372,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,372,800 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,228,760 | 100.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 20,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 20,480 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 1,228,780 | 98.3% |
| FOR_ITER_TUPLE | 20,680 | 1.7% |
| FOR_ITER_RANGE | 380 | 0.0% |
| CALL | 120 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,520 | 98.3% |
| LOAD_GLOBAL_MODULE | 20,660 | 1.7% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,457,560 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,800 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 50.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 50.0% |
| CALL | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 40 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 40 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 40.0% |
| CACHE | 20 | 20.0% |
| CALL_KW | 20 | 20.0% |
| COPY_FREE_VARS | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| LOAD_GLOBAL | 40 | 40.0% |
| NOP | 20 | 20.0% |


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

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,228,760 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,228,760 | 100.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,760 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,228,760 | 100.0% |
| COMPARE_OP | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,457,520 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,228,780 | 50.0% |
| STORE_FAST | 1,228,780 | 50.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,760 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,228,780 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,228,760 | 100.0% |
| COMPARE_OP | 40 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,228,840 | 100.0% |


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
| LOAD_FAST | 80 | 17.4% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 41,140 | 100.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,680 | 50.2% |
| RETURN_CONST | 20,480 | 49.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,760 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,228,780 | 100.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,457,520 | 66.7% |
| LOAD_FAST | 1,228,760 | 33.3% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 2,457,520 | 66.7% |
| LOAD_CONST | 1,228,780 | 33.3% |
| CALL | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,760 | 50.0% |
| LOAD_GLOBAL_MODULE | 1,228,760 | 50.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,780 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,228,780 | 50.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,187,340 | 100.0% |
| LOAD_ATTR | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,187,720 | 100.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,457,520 | 66.7% |
| RESUME_CHECK | 1,228,760 | 33.3% |
| LOAD_GLOBAL | 80 | 0.0% |
| POP_JUMP_IF_FALSE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,457,620 | 66.7% |
| CALL_ISINSTANCE | 1,228,760 | 33.3% |
| CALL | 20 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,228,760 | 50.8% |
| POP_TOP | 1,166,600 | 48.3% |
| STORE_FAST | 20,660 | 0.9% |
| LOAD_GLOBAL | 460 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 1,228,760 | 50.8% |
| LOAD_ATTR_MODULE | 1,187,340 | 49.1% |
| LOAD_ATTR | 460 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,228,780 | 33.1% |
| CALL_KW | 1,228,780 | 33.1% |
| CALL_PY_WITH_DEFAULTS | 1,228,780 | 33.1% |
| CACHE | 20,460 | 0.6% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,249,240 | 33.7% |
| NOP | 1,228,780 | 33.1% |
| LOAD_GLOBAL_BUILTIN | 1,228,760 | 33.1% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,228,760 | 50.0% |
| CALL_ISINSTANCE | 1,228,760 | 50.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,457,560 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,228,760 | 50.0% |
| CALL | 1,228,760 | 50.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,457,560 | 100.0% |


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
|     deferred | 6,164,840 | 50.1% |
|          hit | 6,143,960 | 49.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 1.9% |
| Failure | 6,240 | 98.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 4,000 | 64.1% |
| cmethod | 1,000 | 16.0% |
| other | 680 | 10.9% |
| meth descr varargs | 500 | 8.0% |
| cfunc noargs | 60 | 1.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 1,228,840 | 100.0% |

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
|     deferred | 40 | 0.1% |
|          hit | 41,620 | 99.8% |

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
|     deferred | 560 | 0.0% |
|          hit | 8,601,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 560 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 540 | 0.0% |
|          hit | 6,102,960 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 540 | 100.0% |
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

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,228,840 | 33.3% |
|          hit | 2,457,560 | 66.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 7.4% |
| Failure | 500 | 92.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 500 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 2,457,560 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 48,091,680 | 48.8% |
| Not specialized | 19,691,140 | 20.0% |
| Specialized hits | 30,699,880 | 31.2% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 6,164,840 | 83.4% |
| TO_BOOL | 1,228,840 | 16.6% |
| LOAD_ATTR | 560 | 0.0% |
| LOAD_GLOBAL | 540 | 0.0% |
| COMPARE_OP | 40 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |
| BINARY_OP | 20 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |


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
| Calls to PyEval_EvalDefault | 20,480 | 0.6% |
| Calls to Python functions inlined | 3,686,480 | 99.4% |
| Calls via PyEval_EvalFrame (total) | 20,480 | 0.6% |
| Calls via PyEval_EvalFrame (vector) | 20,480 | 0.6% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 20,480 | 0.6% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 3,706,960 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 13,107,360 | 8.5% |
| Frees to freelist | 13,107,300 |  |
| Allocations | 141,332,740 | 91.5% |
| Allocations to 512 bytes | 138,875,140 | 89.9% |
| Allocations to 4 kbytes | 2,457,600 | 1.6% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 145,428,687 |  |
| New values | 0 |  |
| Interpreter increfs | 47,166,620 | 17.2% |
| Interpreter decrefs | 53,044,500 | 12.8% |
| Increfs | 226,303,990 | 82.8% |
| Decrefs | 362,578,099 | 87.2% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 566 |  |
| Method cache misses | 114 |  |
| Method cache collisions | 75 |  |
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
| Optimization attempts | 40 |  |
| Traces created | 40 | 100.0% |
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
| <= 16 | 20 | 50.0% |
| <= 32 | 20 | 50.0% |


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
| <= 16 | 40 | 100.0% |


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
| CALL | 40 |


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
