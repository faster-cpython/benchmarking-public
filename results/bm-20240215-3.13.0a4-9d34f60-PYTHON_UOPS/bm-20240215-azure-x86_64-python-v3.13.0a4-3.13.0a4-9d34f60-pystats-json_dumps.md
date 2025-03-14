
# Pystats results

- benchmark: json_dumps
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 143,401,500 | 23.1% | 23.1% |  |
| TO_BOOL_BOOL | 51,212,600 | 8.3% | 31.4% |  |
| LOAD_ATTR_INSTANCE_VALUE | 40,970,080 | 6.6% | 38.0% |  |
| POP_JUMP_IF_FALSE | 35,849,040 | 5.8% | 43.8% |  |
| LOAD_GLOBAL_MODULE | 30,729,500 | 5.0% | 48.8% |  |
| LOAD_GLOBAL_BUILTIN | 30,727,620 | 5.0% | 53.7% |  |
| STORE_FAST | 25,609,020 | 4.1% | 57.8% |  |
| LOAD_CONST | 25,606,480 | 4.1% | 62.0% |  |
| POP_JUMP_IF_NOT_NONE | 25,606,400 | 4.1% | 66.1% |  |
| POP_JUMP_IF_TRUE | 20,485,120 | 3.3% | 69.4% |  |
| CALL | 15,370,040 | 2.5% | 71.9% |  |
| RESUME_CHECK | 15,365,100 | 2.5% | 74.4% |  |
| RETURN_VALUE | 15,363,920 | 2.5% | 76.9% |  |
| JUMP_FORWARD | 15,363,840 | 2.5% | 79.3% |  |
| LOAD_ATTR | 10,246,080 | 1.7% | 81.0% |  |
| BUILD_TUPLE | 10,242,560 | 1.7% | 82.6% |  |
| LOAD_FAST_LOAD_FAST | 10,242,560 | 1.7% | 84.3% |  |
| CALL_ISINSTANCE | 10,242,520 | 1.7% | 85.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,242,520 | 1.7% | 87.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 10,242,520 | 1.7% | 89.3% |  |
| ENTER_EXECUTOR | 5,126,720 | 0.8% | 90.1% |  |
| PUSH_NULL | 5,123,820 | 0.8% | 90.9% |  |
| TO_BOOL | 5,123,120 | 0.8% | 91.7% |  |
| POP_TOP | 5,122,640 | 0.8% | 92.6% |  |
| MAKE_FUNCTION | 5,121,280 | 0.8% | 93.4% |  |
| UNARY_NEGATIVE | 5,121,280 | 0.8% | 94.2% |  |
| BUILD_MAP | 5,121,280 | 0.8% | 95.0% |  |
| CALL_KW | 5,121,280 | 0.8% | 95.9% |  |
| POP_JUMP_IF_NONE | 5,121,280 | 0.8% | 96.7% |  |
| SET_FUNCTION_ATTRIBUTE | 5,121,280 | 0.8% | 97.5% |  |
| CALL_METHOD_DESCRIPTOR_O | 5,121,260 | 0.8% | 98.3% |  |
| CALL_PY_EXACT_ARGS | 5,121,260 | 0.8% | 99.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,121,260 | 0.8% | 100.0% |  |
| FOR_ITER_RANGE | 7,380 | 0.0% | 100.0% |  |
| GET_ITER | 2,880 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 2,780 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 1,940 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 1,520 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,500 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 1,280 | 0.0% | 100.0% |  |
| RETURN_CONST | 1,280 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,020 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 640 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| RESUME | 100 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 60 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 60 | 0.0% | 100.0% |  |
| BINARY_OP | 40 | 0.0% | 100.0% |  |
| COMPARE_OP | 40 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 35,848,820 | 5.8% | 5.8% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 35,848,680 | 5.8% | 11.6% |
| LOAD_FAST TO_BOOL_BOOL | 30,727,440 | 5.0% | 16.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 20,485,120 | 3.3% | 19.8% |
| POP_JUMP_IF_FALSE LOAD_FAST | 20,485,120 | 3.3% | 23.1% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 20,485,120 | 3.3% | 26.4% |
| JUMP_FORWARD LOAD_FAST | 15,363,840 | 2.5% | 28.9% |
| STORE_FAST JUMP_FORWARD | 15,363,840 | 2.5% | 31.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 15,363,780 | 2.5% | 33.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 15,363,780 | 2.5% | 36.4% |
| RESUME_CHECK LOAD_FAST | 10,243,780 | 1.7% | 38.0% |
| LOAD_FAST LOAD_CONST | 10,242,640 | 1.7% | 39.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 10,242,580 | 1.7% | 41.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 10,242,560 | 1.7% | 43.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 10,242,520 | 1.7% | 44.6% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES LOAD_FAST | 10,242,520 | 1.7% | 46.3% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 10,242,480 | 1.7% | 47.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 10,242,480 | 1.7% | 49.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 10,242,480 | 1.7% | 51.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 10,242,480 | 1.7% | 52.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 10,242,480 | 1.7% | 54.5% |
| PUSH_NULL LOAD_FAST | 5,123,200 | 0.8% | 55.4% |
| STORE_FAST LOAD_FAST | 5,121,980 | 0.8% | 56.2% |
| POP_TOP ENTER_EXECUTOR | 5,121,880 | 0.8% | 57.0% |
| LOAD_FAST PUSH_NULL | 5,121,820 | 0.8% | 57.8% |
| LOAD_FAST TO_BOOL | 5,121,520 | 0.8% | 58.7% |
| CALL STORE_FAST | 5,121,380 | 0.8% | 59.5% |
| TO_BOOL POP_JUMP_IF_TRUE | 5,121,340 | 0.8% | 60.3% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR | 5,121,320 | 0.8% | 61.2% |
| CALL RETURN_VALUE | 5,121,300 | 0.8% | 62.0% |
| MAKE_FUNCTION SET_FUNCTION_ATTRIBUTE | 5,121,280 | 0.8% | 62.8% |
| RETURN_VALUE POP_TOP | 5,121,280 | 0.8% | 63.6% |
| RETURN_VALUE RETURN_VALUE | 5,121,280 | 0.8% | 64.5% |
| RETURN_VALUE STORE_FAST | 5,121,280 | 0.8% | 65.3% |
| UNARY_NEGATIVE BUILD_TUPLE | 5,121,280 | 0.8% | 66.1% |
| BUILD_MAP STORE_FAST | 5,121,280 | 0.8% | 66.9% |
| BUILD_TUPLE LOAD_CONST | 5,121,280 | 0.8% | 67.8% |
| LOAD_ATTR LOAD_FAST_LOAD_FAST | 5,121,280 | 0.8% | 68.6% |
| LOAD_CONST MAKE_FUNCTION | 5,121,280 | 0.8% | 69.4% |
| LOAD_CONST CALL | 5,121,280 | 0.8% | 70.2% |
| LOAD_CONST CALL_KW | 5,121,280 | 0.8% | 71.1% |
| LOAD_CONST LOAD_CONST | 5,121,280 | 0.8% | 71.9% |
| POP_JUMP_IF_FALSE BUILD_MAP | 5,121,280 | 0.8% | 72.7% |
| POP_JUMP_IF_NONE LOAD_FAST | 5,121,280 | 0.8% | 73.5% |
| POP_JUMP_IF_TRUE LOAD_CONST | 5,121,280 | 0.8% | 74.4% |
| SET_FUNCTION_ATTRIBUTE STORE_FAST | 5,121,280 | 0.8% | 75.2% |
| CALL RESUME_CHECK | 5,121,260 | 0.8% | 76.0% |
| CALL_KW RESUME_CHECK | 5,121,260 | 0.8% | 76.9% |
| CALL_METHOD_DESCRIPTOR_O RETURN_VALUE | 5,121,260 | 0.8% | 77.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 5,121,260 | 0.8% | 78.5% |
| LOAD_ATTR_INSTANCE_VALUE CALL | 5,121,260 | 0.8% | 79.3% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 5,121,260 | 0.8% | 80.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 5,121,260 | 0.8% | 81.0% |
| LOAD_GLOBAL_BUILTIN BUILD_TUPLE | 5,121,260 | 0.8% | 81.8% |
| LOAD_GLOBAL_BUILTIN LOAD_ATTR | 5,121,260 | 0.8% | 82.6% |
| LOAD_GLOBAL_MODULE UNARY_NEGATIVE | 5,121,260 | 0.8% | 83.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 5,121,260 | 0.8% | 84.3% |
| LOAD_GLOBAL_MODULE POP_JUMP_IF_NONE | 5,121,260 | 0.8% | 85.1% |
| LOAD_GLOBAL_MODULE STORE_FAST | 5,121,260 | 0.8% | 85.9% |
| BUILD_TUPLE CALL_ISINSTANCE | 5,121,240 | 0.8% | 86.8% |
| LOAD_ATTR LOAD_GLOBAL_MODULE | 5,121,240 | 0.8% | 87.6% |
| LOAD_CONST LOAD_ATTR_METHOD_NO_DICT | 5,121,240 | 0.8% | 88.4% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 5,121,240 | 0.8% | 89.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,121,240 | 0.8% | 90.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 5,121,240 | 0.8% | 90.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 5,121,240 | 0.8% | 91.7% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 5,121,240 | 0.8% | 92.6% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_MODULE | 5,121,240 | 0.8% | 93.4% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 5,121,240 | 0.8% | 94.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_BUILTIN | 5,121,240 | 0.8% | 95.0% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 5,121,240 | 0.8% | 95.9% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 5,121,240 | 0.8% | 96.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_METHOD_WITH_VALUES | 5,121,240 | 0.8% | 97.5% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 5,121,240 | 0.8% | 98.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 5,121,240 | 0.8% | 99.2% |
| ENTER_EXECUTOR CALL | 5,120,340 | 0.8% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 5,180 | 0.0% | 100.0% |
| FOR_ITER_RANGE ENTER_EXECUTOR | 4,780 | 0.0% | 100.0% |
| CALL CALL | 4,480 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR | 2,880 | 0.0% | 100.0% |
| LOAD_FAST GET_ITER | 2,880 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 2,180 | 0.0% | 100.0% |
| LOAD_FAST CALL | 1,960 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,880 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 1,880 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 1,800 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_RANGE | 1,560 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,520 | 0.0% | 100.0% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,500 | 0.0% | 100.0% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 1,480 | 0.0% | 100.0% |
| TO_BOOL TO_BOOL | 1,440 | 0.0% | 100.0% |
| CALL POP_TOP | 1,360 | 0.0% | 100.0% |
| RETURN_CONST INTERPRETER_EXIT | 1,280 | 0.0% | 100.0% |
| FOR_ITER_LIST RETURN_CONST | 1,280 | 0.0% | 100.0% |
| CACHE RESUME_CHECK | 1,260 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_LIST | 1,260 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_LIST | 1,200 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 680 | 0.0% | 100.0% |
| PUSH_NULL CALL | 620 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 600 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,260 | 98.4% |
| RESUME | 20 | 1.6% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 1,560 | 54.2% |
| FOR_ITER_LIST | 1,260 | 43.8% |
| FOR_ITER | 60 | 2.1% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,280 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,121,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 5,121,280 | 100.0% |


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
| RETURN_VALUE | 5,121,280 | 100.0% |
| CALL | 1,360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,121,880 | 100.0% |
| JUMP_BACKWARD | 680 | 0.0% |
| NOP | 80 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,820 | 100.0% |
| LOAD_ATTR_MODULE | 1,880 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,123,200 | 100.0% |
| CALL | 620 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,121,300 | 33.3% |
| RETURN_VALUE | 5,121,280 | 33.3% |
| CALL_METHOD_DESCRIPTOR_O | 5,121,260 | 33.3% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,121,280 | 33.3% |
| RETURN_VALUE | 5,121,280 | 33.3% |
| STORE_FAST | 5,121,280 | 33.3% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,520 | 100.0% |
| TO_BOOL | 1,440 | 0.0% |
| CALL | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| CALL_ISINSTANCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,121,340 | 100.0% |
| TO_BOOL | 1,440 | 0.0% |
| TO_BOOL_BOOL | 200 | 0.0% |
| POP_JUMP_IF_FALSE | 140 | 0.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,121,260 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 5,121,280 | 100.0% |


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

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,121,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,121,280 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 5,121,280 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 5,121,260 | 50.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,121,280 | 50.0% |
| CALL_ISINSTANCE | 5,121,240 | 50.0% |
| CALL | 40 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,121,280 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 5,121,260 | 33.3% |
| ENTER_EXECUTOR | 5,120,340 | 33.3% |
| CALL | 4,480 | 0.0% |
| LOAD_FAST | 1,960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,121,380 | 33.3% |
| RETURN_VALUE | 5,121,300 | 33.3% |
| RESUME_CHECK | 5,121,260 | 33.3% |
| CALL | 4,480 | 0.0% |
| POP_TOP | 1,360 | 0.0% |


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
| LOAD_CONST | 5,121,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,121,260 | 100.0% |
| RESUME | 20 | 0.0% |


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
| POP_TOP | 5,121,880 | 99.9% |
| FOR_ITER_RANGE | 4,780 | 0.1% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,120,340 | 99.9% |
| FOR_ITER_RANGE | 5,180 | 0.1% |
| FOR_ITER_LIST | 1,200 | 0.0% |


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
| STORE_FAST | 40 | 33.3% |
| FOR_ITER_RANGE | 40 | 33.3% |
| UNPACK_SEQUENCE | 20 | 16.7% |
| FOR_ITER_LIST | 20 | 16.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 680 | 66.7% |
| FOR_ITER_RANGE | 340 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 600 | 58.8% |
| FOR_ITER_LIST | 300 | 29.4% |
| ENTER_EXECUTOR | 60 | 5.9% |
| FOR_ITER | 60 | 5.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,363,840 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,363,840 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,121,320 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 5,121,260 | 50.0% |
| LOAD_ATTR | 2,880 | 0.0% |
| LOAD_FAST | 400 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,121,280 | 50.0% |
| LOAD_GLOBAL_MODULE | 5,121,240 | 50.0% |
| LOAD_ATTR | 2,880 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,640 | 40.0% |
| BUILD_TUPLE | 5,121,280 | 20.0% |
| LOAD_CONST | 5,121,280 | 20.0% |
| POP_JUMP_IF_TRUE | 5,121,280 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 5,121,280 | 20.0% |
| CALL | 5,121,280 | 20.0% |
| CALL_KW | 5,121,280 | 20.0% |
| LOAD_CONST | 5,121,280 | 20.0% |
| LOAD_ATTR_METHOD_NO_DICT | 5,121,240 | 20.0% |


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
| POP_JUMP_IF_FALSE | 20,485,120 | 14.3% |
| POP_JUMP_IF_NOT_NONE | 20,485,120 | 14.3% |
| JUMP_FORWARD | 15,363,840 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 15,363,780 | 10.7% |
| RESUME_CHECK | 10,243,780 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 35,848,680 | 25.0% |
| TO_BOOL_BOOL | 30,727,440 | 21.4% |
| POP_JUMP_IF_NOT_NONE | 20,485,120 | 14.3% |
| LOAD_CONST | 10,242,640 | 7.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 10,242,480 | 7.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 5,121,280 | 50.0% |
| LOAD_GLOBAL_MODULE | 5,121,260 | 50.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 5,121,320 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 5,121,240 | 50.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 120 | 18.8% |
| LOAD_FAST | 80 | 12.5% |
| STORE_FAST | 80 | 12.5% |
| LOAD_ATTR | 60 | 9.4% |
| RETURN_VALUE | 40 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 180 | 28.1% |
| LOAD_GLOBAL_BUILTIN | 140 | 21.9% |
| LOAD_ATTR | 100 | 15.6% |
| LOAD_FAST | 60 | 9.4% |
| LOAD_GLOBAL | 40 | 6.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 35,848,820 | 100.0% |
| TO_BOOL | 140 | 0.0% |
| COMPARE_OP_INT | 60 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,485,120 | 57.1% |
| LOAD_GLOBAL_MODULE | 10,242,480 | 28.6% |
| BUILD_MAP | 5,121,280 | 14.3% |
| LOAD_GLOBAL | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,121,260 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,280 | 100.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,485,120 | 80.0% |
| LOAD_ATTR_INSTANCE_VALUE | 5,121,260 | 20.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,485,120 | 80.0% |
| LOAD_GLOBAL_MODULE | 5,121,240 | 20.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 15,363,780 | 75.0% |
| TO_BOOL | 5,121,340 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,560 | 50.0% |
| LOAD_CONST | 5,121,280 | 25.0% |
| LOAD_GLOBAL_MODULE | 5,121,240 | 25.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,280 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 5,121,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,121,280 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,121,380 | 20.0% |
| RETURN_VALUE | 5,121,280 | 20.0% |
| BUILD_MAP | 5,121,280 | 20.0% |
| SET_FUNCTION_ATTRIBUTE | 5,121,280 | 20.0% |
| LOAD_GLOBAL_MODULE | 5,121,260 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 15,363,840 | 60.0% |
| LOAD_FAST | 5,121,980 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 20.0% |
| LOAD_GLOBAL_MODULE | 1,800 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,500 | 98.7% |
| UNPACK_SEQUENCE | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,520 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 20 | 50.0% |
| FOR_ITER_LIST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 20 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20 | 50.0% |


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
| LOAD_FAST | 60 | 60.0% |
| LOAD_GLOBAL | 40 | 40.0% |


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
| BUILD_TUPLE | 5,121,240 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 50.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 10,242,480 | 100.0% |
| TO_BOOL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,240 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,121,260 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,240 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,121,260 | 100.0% |


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
| GET_ITER | 1,260 | 45.3% |
| ENTER_EXECUTOR | 1,200 | 43.2% |
| JUMP_BACKWARD | 300 | 10.8% |
| FOR_ITER | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,480 | 53.2% |
| RETURN_CONST | 1,280 | 46.0% |
| UNPACK_SEQUENCE | 20 | 0.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,180 | 70.2% |
| GET_ITER | 1,560 | 21.1% |
| JUMP_BACKWARD | 600 | 8.1% |
| FOR_ITER | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,780 | 64.8% |
| STORE_FAST | 2,180 | 29.5% |
| JUMP_BACKWARD | 340 | 4.6% |
| LOAD_FAST | 80 | 1.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,848,680 | 87.5% |
| LOAD_FAST_LOAD_FAST | 5,121,240 | 12.5% |
| LOAD_ATTR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,363,780 | 37.5% |
| TO_BOOL_BOOL | 10,242,480 | 25.0% |
| CALL | 5,121,260 | 12.5% |
| POP_JUMP_IF_NOT_NONE | 5,121,260 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 12.5% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,121,240 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,260 | 100.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,121,240 | 50.0% |
| LOAD_GLOBAL_MODULE | 5,121,240 | 50.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,520 | 100.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,880 | 96.9% |
| LOAD_ATTR | 60 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,880 | 96.9% |
| STORE_FAST | 60 | 3.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,480 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,520 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,480 | 33.3% |
| STORE_FAST | 5,121,240 | 16.7% |
| LOAD_ATTR_INSTANCE_VALUE | 5,121,240 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 16.7% |
| RESUME_CHECK | 5,121,240 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,242,580 | 33.3% |
| BUILD_TUPLE | 5,121,260 | 16.7% |
| LOAD_ATTR | 5,121,260 | 16.7% |
| CALL_ISINSTANCE | 5,121,240 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 16.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,242,480 | 33.3% |
| LOAD_ATTR | 5,121,240 | 16.7% |
| POP_JUMP_IF_NOT_NONE | 5,121,240 | 16.7% |
| POP_JUMP_IF_TRUE | 5,121,240 | 16.7% |
| LOAD_GLOBAL_MODULE | 5,121,240 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 5,121,260 | 16.7% |
| LOAD_FAST_LOAD_FAST | 5,121,260 | 16.7% |
| POP_JUMP_IF_NONE | 5,121,260 | 16.7% |
| STORE_FAST | 5,121,260 | 16.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,121,240 | 16.7% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,121,260 | 33.3% |
| CALL_KW | 5,121,260 | 33.3% |
| CALL_PY_EXACT_ARGS | 5,121,260 | 33.3% |
| CACHE | 1,260 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,243,780 | 66.7% |
| LOAD_GLOBAL_BUILTIN | 5,121,240 | 33.3% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,727,440 | 60.0% |
| CALL_ISINSTANCE | 10,242,480 | 20.0% |
| LOAD_ATTR_INSTANCE_VALUE | 10,242,480 | 20.0% |
| TO_BOOL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,848,820 | 70.0% |
| POP_JUMP_IF_TRUE | 15,363,780 | 30.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,480 | 98.7% |
| UNPACK_SEQUENCE | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,500 | 100.0% |


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
|     deferred | 15,365,460 | 42.9% |
|          hit | 20,485,100 | 57.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 2.2% |
| Failure | 4,480 | 97.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,540 | 34.4% |
| code complex parameters | 1,440 | 32.1% |
| class mutable | 1,440 | 32.1% |
| cfunc noargs | 60 | 1.3% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 20.0% |
|          hit | 60 | 60.0% |

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
|     deferred | 60 | 0.6% |
|          hit | 10,160 | 98.8% |

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
|     deferred | 10,242,880 | 12.5% |
|          hit | 71,697,760 | 87.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 10.0% |
| Failure | 2,880 | 90.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 1,440 | 50.0% |
| metaclass attribute | 1,440 | 50.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 320 | 0.0% |
|          hit | 61,457,120 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


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
|     deferred | 5,121,480 | 9.1% |
|          hit | 51,212,600 | 90.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 12.2% |
| Failure | 1,440 | 87.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 1,440 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.4% |
|          hit | 5,100 | 99.2% |

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
| Basic | 286,817,940 | 46.3% |
| Not specialized | 117,801,960 | 19.0% |
| Specialized hits | 215,110,020 | 34.7% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 15,365,460 | 50.0% |
| LOAD_ATTR | 10,242,880 | 33.3% |
| TO_BOOL | 5,121,480 | 16.7% |
| LOAD_GLOBAL | 320 | 0.0% |
| FOR_ITER | 60 | 0.0% |
| BINARY_OP | 20 | 0.0% |
| COMPARE_OP | 20 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |
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
| Calls to PyEval_EvalDefault | 1,280 | 0.0% |
| Calls to Python functions inlined | 15,363,920 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 1,280 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 1,280 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 1,280 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 15,365,200 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 40,970,400 | 20.4% |
| Frees to freelist | 40,970,340 |  |
| Allocations | 159,668,740 | 79.6% |
| Allocations to 512 bytes | 159,668,740 | 79.6% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 159,668,670 |  |
| New values | 0 |  |
| Interpreter increfs | 209,996,000 | 50.3% |
| Interpreter decrefs | 256,093,160 | 42.0% |
| Increfs | 207,421,549 | 49.7% |
| Decrefs | 353,640,861 | 58.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 5,123,085 |  |
| Method cache misses | 215 |  |
| Method cache collisions | 221 |  |
| Method cache dunder hits | 20,486,516 |  |
| Method cache dunder misses | 44 |  |


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
| <= 16 | 20 | 33.3% |
| <= 32 | 40 | 66.7% |


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
| <= 32 | 20 | 33.3% |


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
| CALL | 60 |


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
