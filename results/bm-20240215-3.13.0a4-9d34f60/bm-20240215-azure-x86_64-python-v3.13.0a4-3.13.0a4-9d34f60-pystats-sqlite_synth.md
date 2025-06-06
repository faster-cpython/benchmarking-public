
# Pystats results

- benchmark: sqlite_synth
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 52,431,040 | 17.2% | 17.2% |  |
| STORE_FAST | 15,729,760 | 5.2% | 22.4% |  |
| COPY | 15,728,640 | 5.2% | 27.6% |  |
| SWAP | 15,728,640 | 5.2% | 32.8% |  |
| LOAD_GLOBAL_BUILTIN | 10,487,120 | 3.4% | 36.2% |  |
| LOAD_CONST | 10,486,960 | 3.4% | 39.7% |  |
| JUMP_BACKWARD | 10,486,320 | 3.4% | 43.1% |  |
| LOAD_GLOBAL_MODULE | 10,486,320 | 3.4% | 46.6% |  |
| PUSH_NULL | 10,486,240 | 3.4% | 50.0% |  |
| POP_JUMP_IF_FALSE | 10,486,240 | 3.4% | 53.4% |  |
| LOAD_ATTR_MODULE | 10,485,960 | 3.4% | 56.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 10,485,840 | 3.4% | 60.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 10,485,840 | 3.4% | 63.8% |  |
| BINARY_OP_ADD_INT | 10,485,720 | 3.4% | 67.2% |  |
| CALL_BUILTIN_O | 10,485,720 | 3.4% | 70.7% |  |
| COMPARE_OP_FLOAT | 10,485,720 | 3.4% | 74.1% |  |
| FOR_ITER | 5,244,480 | 1.7% | 75.9% |  |
| POP_TOP | 5,244,000 | 1.7% | 77.6% |  |
| LOAD_FAST_LOAD_FAST | 5,243,840 | 1.7% | 79.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,243,420 | 1.7% | 81.0% |  |
| RESUME_CHECK | 5,243,340 | 1.7% | 82.8% |  |
| INTERPRETER_EXIT | 5,243,200 | 1.7% | 84.5% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 5,243,100 | 1.7% | 86.2% |  |
| BUILD_LIST | 5,242,960 | 1.7% | 87.9% |  |
| RETURN_CONST | 5,242,960 | 1.7% | 89.7% |  |
| FOR_ITER_RANGE | 5,242,940 | 1.7% | 91.4% |  |
| POP_JUMP_IF_NONE | 5,242,880 | 1.7% | 93.1% |  |
| STORE_FAST_STORE_FAST | 5,242,880 | 1.7% | 94.8% |  |
| CALL_LEN | 5,242,860 | 1.7% | 96.5% |  |
| CALL_STR_1 | 5,242,860 | 1.7% | 98.3% |  |
| UNPACK_SEQUENCE_TUPLE | 5,242,860 | 1.7% | 100.0% |  |
| CALL | 1,260 | 0.0% | 100.0% |  |
| LOAD_ATTR | 860 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 800 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 720 | 0.0% | 100.0% |  |
| NOP | 560 | 0.0% | 100.0% |  |
| LOAD_DEREF | 560 | 0.0% | 100.0% |  |
| RETURN_VALUE | 480 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 480 | 0.0% | 100.0% |  |
| STORE_ATTR | 360 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 320 | 0.0% | 100.0% |  |
| GET_ITER | 320 | 0.0% | 100.0% |  |
| POP_EXCEPT | 320 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 320 | 0.0% | 100.0% |  |
| BINARY_OP | 220 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 160 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 160 | 0.0% | 100.0% |  |
| MAKE_CELL | 160 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 160 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 120 | 0.0% | 100.0% |  |
| RESUME | 100 | 0.0% | 100.0% |  |
| BUILD_MAP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COMPARE_OP | 80 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| CALL_ISINSTANCE | 80 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 80 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 80 | 0.0% | 100.0% |  |
| TO_BOOL_BOOL | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 40 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| PUSH_NULL LOAD_FAST | 10,485,920 | 3.4% | 3.4% |
| LOAD_ATTR_MODULE PUSH_NULL | 10,485,900 | 3.4% | 6.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 10,485,840 | 3.4% | 10.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 10,485,840 | 3.4% | 13.8% |
| LOAD_FAST COPY | 10,485,760 | 3.4% | 17.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 10,485,720 | 3.4% | 20.7% |
| BINARY_OP_ADD_INT SWAP | 10,485,720 | 3.4% | 24.1% |
| COMPARE_OP_FLOAT POP_JUMP_IF_FALSE | 10,485,720 | 3.4% | 27.6% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 10,485,680 | 3.4% | 31.0% |
| LOAD_FAST CALL_BUILTIN_O | 10,485,680 | 3.4% | 34.5% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 10,485,680 | 3.4% | 37.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 5,243,220 | 1.7% | 39.7% |
| STORE_FAST LOAD_FAST | 5,243,200 | 1.7% | 41.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 5,243,160 | 1.7% | 43.1% |
| POP_TOP JUMP_BACKWARD | 5,243,120 | 1.7% | 44.8% |
| RESUME_CHECK LOAD_FAST | 5,243,000 | 1.7% | 46.5% |
| CACHE RESUME_CHECK | 5,242,980 | 1.7% | 48.3% |
| CALL_METHOD_DESCRIPTOR_FAST POP_TOP | 5,242,980 | 1.7% | 50.0% |
| RETURN_CONST INTERPRETER_EXIT | 5,242,960 | 1.7% | 51.7% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 5,242,920 | 1.7% | 53.4% |
| JUMP_BACKWARD FOR_ITER | 5,242,900 | 1.7% | 55.2% |
| LOAD_CONST LOAD_FAST_LOAD_FAST | 5,242,880 | 1.7% | 56.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 5,242,880 | 1.7% | 58.6% |
| LOAD_FAST SWAP | 5,242,880 | 1.7% | 60.3% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 5,242,880 | 1.7% | 62.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 5,242,880 | 1.7% | 63.8% |
| POP_JUMP_IF_NONE LOAD_FAST | 5,242,880 | 1.7% | 65.5% |
| STORE_FAST_STORE_FAST STORE_FAST | 5,242,880 | 1.7% | 67.2% |
| SWAP COPY | 5,242,880 | 1.7% | 69.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_BUILTIN | 5,242,880 | 1.7% | 70.7% |
| JUMP_BACKWARD FOR_ITER_RANGE | 5,242,860 | 1.7% | 72.4% |
| CALL_BUILTIN_O LOAD_FAST | 5,242,860 | 1.7% | 74.1% |
| CALL_BUILTIN_O STORE_FAST | 5,242,860 | 1.7% | 75.9% |
| CALL_STR_1 BUILD_LIST | 5,242,860 | 1.7% | 77.6% |
| FOR_ITER_RANGE STORE_FAST | 5,242,860 | 1.7% | 79.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 5,242,860 | 1.7% | 81.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 5,242,860 | 1.7% | 82.8% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 5,242,860 | 1.7% | 84.5% |
| BUILD_LIST CALL_METHOD_DESCRIPTOR_FAST | 5,242,840 | 1.7% | 86.2% |
| COPY COMPARE_OP_FLOAT | 5,242,840 | 1.7% | 87.9% |
| FOR_ITER UNPACK_SEQUENCE_TUPLE | 5,242,840 | 1.7% | 89.6% |
| LOAD_CONST BINARY_OP_ADD_INT | 5,242,840 | 1.7% | 91.4% |
| LOAD_FAST CALL_LEN | 5,242,840 | 1.7% | 93.1% |
| LOAD_FAST CALL_STR_1 | 5,242,840 | 1.7% | 94.8% |
| LOAD_FAST COMPARE_OP_FLOAT | 5,242,840 | 1.7% | 96.5% |
| LOAD_FAST_LOAD_FAST LOAD_GLOBAL_BUILTIN | 5,242,840 | 1.7% | 98.3% |
| CALL_LEN BINARY_OP_ADD_INT | 5,242,840 | 1.7% | 100.0% |
| FOR_ITER FOR_ITER | 1,480 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 800 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 560 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 560 | 0.0% | 100.0% |
| FOR_ITER_TUPLE STORE_FAST | 560 | 0.0% | 100.0% |
| NOP LOAD_GLOBAL_BUILTIN | 480 | 0.0% | 100.0% |
| STORE_FAST NOP | 480 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 440 | 0.0% | 100.0% |
| CALL POP_TOP | 400 | 0.0% | 100.0% |
| CHECK_EXC_MATCH POP_JUMP_IF_FALSE | 320 | 0.0% | 100.0% |
| POP_EXCEPT JUMP_BACKWARD | 320 | 0.0% | 100.0% |
| POP_TOP POP_EXCEPT | 320 | 0.0% | 100.0% |
| POP_TOP LOAD_FAST | 320 | 0.0% | 100.0% |
| PUSH_EXC_INFO LOAD_GLOBAL_BUILTIN | 320 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE POP_TOP | 320 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST PUSH_EXC_INFO | 320 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN CHECK_EXC_MATCH | 320 | 0.0% | 100.0% |
| PUSH_NULL CALL | 240 | 0.0% | 100.0% |
| RETURN_VALUE INTERPRETER_EXIT | 240 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 240 | 0.0% | 100.0% |
| CALL STORE_FAST | 220 | 0.0% | 100.0% |
| LOAD_CONST CALL | 200 | 0.0% | 100.0% |
| LOAD_FAST CALL | 200 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 180 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_METHOD_NO_DICT | 180 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 180 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_TUPLE | 160 | 0.0% | 100.0% |
| MAKE_FUNCTION SET_FUNCTION_ATTRIBUTE | 160 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 160 | 0.0% | 100.0% |
| BUILD_TUPLE LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_CONST MAKE_FUNCTION | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_FAST GET_ITER | 160 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 160 | 0.0% | 100.0% |
| LOAD_FAST BUILD_TUPLE | 160 | 0.0% | 100.0% |
| LOAD_FAST LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_FAST STORE_ATTR | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_FAST | 160 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 160 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST POP_TOP | 160 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST STORE_FAST | 160 | 0.0% | 100.0% |
| CALL CALL | 140 | 0.0% | 100.0% |
| COPY_FREE_VARS RESUME_CHECK | 140 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 140 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE CALL | 140 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 120 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,242,980 | 100.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| MAKE_CELL | 80 | 0.0% |
| RESUME | 60 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 20 | 50.0% |
| BINARY_SUBSCR_TUPLE_INT | 20 | 50.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 320 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 50.0% |
| CALL_BUILTIN_CLASS | 60 | 18.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 60 | 18.8% |
| CALL | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 160 | 50.0% |
| FOR_ITER | 100 | 31.2% |
| FOR_ITER_RANGE | 60 | 18.8% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,242,960 | 100.0% |
| RETURN_VALUE | 240 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 160 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 85.7% |
| POP_TOP | 80 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 480 | 85.7% |
| LOAD_DEREF | 80 | 14.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 320 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 5,242,980 | 100.0% |
| CALL | 400 | 0.0% |
| POP_JUMP_IF_FALSE | 320 | 0.0% |
| CALL_BUILTIN_FAST | 160 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,243,120 | 100.0% |
| POP_EXCEPT | 320 | 0.0% |
| LOAD_FAST | 320 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 320 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 10,485,900 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |
| LOAD_DEREF | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,485,920 | 100.0% |
| CALL | 240 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 160 | 33.3% |
| LOAD_FAST | 160 | 33.3% |
| BINARY_OP | 100 | 20.8% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 240 | 50.0% |
| RETURN_VALUE | 160 | 33.3% |
| LOAD_GLOBAL | 40 | 8.3% |
| LOAD_GLOBAL_MODULE | 40 | 8.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 60 | 27.3% |
| CALL | 40 | 18.2% |
| LOAD_CONST | 40 | 18.2% |
| LOAD_FAST | 40 | 18.2% |
| BINARY_OP | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 100 | 45.5% |
| SWAP | 40 | 18.2% |
| BINARY_OP_ADD_INT | 40 | 18.2% |
| BINARY_OP | 20 | 9.1% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 9.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_STR_1 | 5,242,860 | 100.0% |
| LOAD_FAST | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 5,242,840 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 80 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 240 | 19.0% |
| LOAD_CONST | 200 | 15.9% |
| LOAD_FAST | 200 | 15.9% |
| CALL | 140 | 11.1% |
| LOAD_GLOBAL_MODULE | 140 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 400 | 31.7% |
| STORE_FAST | 220 | 17.5% |
| CALL | 140 | 11.1% |
| LOAD_FAST | 100 | 7.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 100 | 7.9% |


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
| COPY | 40 | 50.0% |
| LOAD_FAST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 50.0% |
| COMPARE_OP_FLOAT | 40 | 50.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,485,760 | 66.7% |
| SWAP | 5,242,880 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 10,485,680 | 66.7% |
| COMPARE_OP_FLOAT | 5,242,840 | 33.3% |
| LOAD_ATTR | 80 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 80 | 50.0% |
| CALL_FUNCTION_EX | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 140 | 87.5% |
| RESUME | 20 | 12.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,242,900 | 100.0% |
| FOR_ITER | 1,480 | 0.0% |
| GET_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 5,242,840 | 100.0% |
| FOR_ITER | 1,480 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |
| STORE_FAST | 20 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,243,120 | 50.0% |
| POP_JUMP_IF_FALSE | 5,242,880 | 50.0% |
| POP_EXCEPT | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 5,242,900 | 50.0% |
| FOR_ITER_RANGE | 5,242,860 | 50.0% |
| FOR_ITER_TUPLE | 560 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


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
| LOAD_FAST | 440 | 51.2% |
| LOAD_GLOBAL_MODULE | 180 | 20.9% |
| LOAD_GLOBAL | 140 | 16.3% |
| COPY | 80 | 9.3% |
| LOAD_ATTR | 20 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 180 | 20.9% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 20.9% |
| LOAD_CONST | 160 | 18.6% |
| LOAD_ATTR_MODULE | 120 | 14.0% |
| CALL | 80 | 9.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,243,220 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 5,242,860 | 50.0% |
| BUILD_TUPLE | 160 | 0.0% |
| LOAD_ATTR | 160 | 0.0% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,242,880 | 50.0% |
| BINARY_OP_ADD_INT | 5,242,840 | 50.0% |
| CALL | 200 | 0.0% |
| MAKE_FUNCTION | 160 | 0.0% |
| LOAD_CONST | 160 | 0.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 14.3% |
| BUILD_LIST | 80 | 14.3% |
| LOAD_DEREF | 80 | 14.3% |
| LOAD_FAST | 80 | 14.3% |
| POP_JUMP_IF_FALSE | 80 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 160 | 28.6% |
| LIST_EXTEND | 80 | 14.3% |
| LOAD_CONST | 80 | 14.3% |
| LOAD_DEREF | 80 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 80 | 14.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 10,485,920 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 10,485,840 | 20.0% |
| STORE_FAST | 5,243,200 | 10.0% |
| RESUME_CHECK | 5,243,000 | 10.0% |
| POP_JUMP_IF_FALSE | 5,242,880 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 10,485,760 | 20.0% |
| CALL_BUILTIN_O | 10,485,680 | 20.0% |
| LOAD_ATTR_METHOD_NO_DICT | 5,243,160 | 10.0% |
| POP_JUMP_IF_NONE | 5,242,880 | 10.0% |
| SWAP | 5,242,880 | 10.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,242,880 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 800 | 0.0% |
| FOR_ITER_TUPLE | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 5,242,840 | 100.0% |
| CALL_BUILTIN_FAST | 560 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| BUILD_MAP | 80 | 0.0% |
| STORE_ATTR | 80 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 25.0% |
| POP_TOP | 80 | 16.7% |
| LOAD_CONST | 80 | 16.7% |
| RETURN_VALUE | 40 | 8.3% |
| LOAD_ATTR | 40 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160 | 33.3% |
| LOAD_ATTR | 140 | 29.2% |
| LOAD_FAST | 80 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 80 | 16.7% |
| CALL | 20 | 4.2% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 80 | 50.0% |
| MAKE_CELL | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 80 | 50.0% |
| RESUME_CHECK | 80 | 50.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 10,485,720 | 100.0% |
| CHECK_EXC_MATCH | 320 | 0.0% |
| COMPARE_OP_INT | 80 | 0.0% |
| TO_BOOL_BOOL | 80 | 0.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,242,880 | 50.0% |
| LOAD_FAST | 5,242,880 | 50.0% |
| POP_TOP | 320 | 0.0% |
| JUMP_FORWARD | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,242,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,242,880 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 5,242,920 | 100.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 5,242,960 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 44.4% |
| LOAD_FAST_LOAD_FAST | 80 | 22.2% |
| SWAP | 80 | 22.2% |
| STORE_ATTR | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100 | 27.8% |
| LOAD_GLOBAL_MODULE | 80 | 22.2% |
| STORE_ATTR_INSTANCE_VALUE | 80 | 22.2% |
| RETURN_CONST | 40 | 11.1% |
| STORE_ATTR | 40 | 11.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 5,242,880 | 33.3% |
| CALL_BUILTIN_O | 5,242,860 | 33.3% |
| FOR_ITER_RANGE | 5,242,860 | 33.3% |
| FOR_ITER_TUPLE | 560 | 0.0% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,485,720 | 66.7% |
| LOAD_FAST | 5,243,200 | 33.3% |
| NOP | 480 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 240 | 0.0% |
| LOAD_GLOBAL | 120 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 5,242,860 | 100.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,242,880 | 100.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 10,485,720 | 66.7% |
| LOAD_FAST | 5,242,880 | 33.3% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 10,485,680 | 66.7% |
| COPY | 5,242,880 | 33.3% |
| STORE_ATTR | 80 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 20 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 20 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 60 | 60.0% |
| CALL_FUNCTION_EX | 20 | 20.0% |
| COPY_FREE_VARS | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| LOAD_CONST | 20 | 20.0% |
| LOAD_DEREF | 20 | 20.0% |
| LOAD_GLOBAL | 20 | 20.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,242,840 | 50.0% |
| CALL_LEN | 5,242,840 | 50.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,485,720 | 100.0% |


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

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| BINARY_SUBSCR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 50.0% |
| BINARY_OP | 60 | 50.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 560 | 70.0% |
| LOAD_FAST | 160 | 20.0% |
| BUILD_MAP | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 320 | 40.0% |
| POP_TOP | 160 | 20.0% |
| STORE_FAST | 160 | 20.0% |
| CALL | 80 | 10.0% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 10.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,485,680 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,242,860 | 50.0% |
| STORE_FAST | 5,242,860 | 50.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 80 | 100.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,242,840 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 5,242,840 | 100.0% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 5,242,840 | 100.0% |
| LOAD_CONST | 160 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,242,980 | 100.0% |
| GET_ITER | 60 | 0.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 80 | 66.7% |
| CALL | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 50.0% |
| LOAD_CONST | 60 | 50.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,242,840 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 5,242,860 | 100.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,242,840 | 50.0% |
| LOAD_FAST | 5,242,840 | 50.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,485,720 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,242,860 | 100.0% |
| GET_ITER | 60 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,242,860 | 100.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 560 | 77.8% |
| GET_ITER | 160 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 560 | 77.8% |
| LOAD_FAST | 80 | 11.1% |
| LOAD_FAST_LOAD_FAST | 80 | 11.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 10,485,680 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 5,242,880 | 50.0% |
| LOAD_CONST | 5,242,860 | 50.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| CALL_BUILTIN_CLASS | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,243,160 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |
| CALL_BUILTIN_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,243,220 | 100.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 80 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,485,840 | 100.0% |
| LOAD_ATTR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 10,485,900 | 100.0% |
| CALL | 60 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,242,880 | 50.0% |
| LOAD_FAST_LOAD_FAST | 5,242,840 | 50.0% |
| NOP | 480 | 0.0% |
| PUSH_EXC_INFO | 320 | 0.0% |
| STORE_FAST | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,485,840 | 100.0% |
| LOAD_FAST_LOAD_FAST | 800 | 0.0% |
| CHECK_EXC_MATCH | 320 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| CALL_ISINSTANCE | 80 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,485,720 | 100.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| RESUME_CHECK | 120 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 10,485,840 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |
| CALL | 140 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 5,242,980 | 100.0% |
| COPY_FREE_VARS | 140 | 0.0% |
| MAKE_CELL | 80 | 0.0% |
| CALL_PY_WITH_DEFAULTS | 80 | 0.0% |
| CALL_FUNCTION_EX | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,243,000 | 100.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_DEREF | 60 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,485,680 | 100.0% |
| LOAD_FAST | 80 | 0.0% |
| STORE_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,242,920 | 50.0% |
| LOAD_FAST | 5,242,860 | 50.0% |
| LOAD_CONST | 60 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 5,242,840 | 100.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 5,242,860 | 100.0% |


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
|     deferred | 140 | 0.0% |
|          hit | 10,485,780 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 75.0% |
| Failure | 20 | 25.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| true divide different types | 20 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

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
|     deferred | 840 | 0.0% |
|          hit | 26,215,800 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 66.7% |
| Failure | 140 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 42.9% |
| meth descr method fastcall keywords | 40 | 28.6% |
| meth descr varargs keywords | 20 | 14.3% |
| class no vectorcall | 20 | 14.3% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 10,485,800 | 100.0% |

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
|     deferred | 5,242,980 | 50.0% |
|          hit | 5,243,660 | 50.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 1.3% |
| Failure | 1,480 | 98.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,480 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 460 | 0.0% |
|          hit | 26,215,220 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 95.0% |
| Failure | 20 | 5.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| module attr not found | 20 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 20,973,440 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 10,485,840 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 66.7% |
| Failure | 40 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 40 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|          hit | 80 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 5,242,860 | 100.0% |

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
| Basic | 162,541,700 | 53.4% |
| Not specialized | 20,976,940 | 6.9% |
| Specialized hits | 120,591,880 | 39.7% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| FOR_ITER | 5,242,980 | 100.0% |
| CALL | 840 | 0.0% |
| LOAD_ATTR | 460 | 0.0% |
| LOAD_GLOBAL | 240 | 0.0% |
| STORE_ATTR | 240 | 0.0% |
| BINARY_OP | 140 | 0.0% |
| COMPARE_OP | 40 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |


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
| Calls to PyEval_EvalDefault | 5,243,200 | 100.0% |
| Calls to Python functions inlined | 240 | 0.0% |
| Calls via PyEval_EvalFrame (total) | 5,243,200 | 100.0% |
| Calls via PyEval_EvalFrame (vector) | 5,243,200 | 100.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 5,243,200 | 100.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 80 | 0.0% |
| Frame objects created | 80 | 0.0% |
| Frames pushed | 80 | 0.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 78,672,560 | 51.8% |
| Frees to freelist | 78,673,240 |  |
| Allocations | 73,292,180 | 48.2% |
| Allocations to 512 bytes | 73,292,180 | 48.2% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 78,564,010 |  |
| New values | 80 |  |
| Interpreter increfs | 162,402,400 | 63.2% |
| Interpreter decrefs | 193,831,800 | 48.0% |
| Increfs | 94,390,755 | 36.8% |
| Decrefs | 209,688,447 | 52.0% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 5,244,308 |  |
| Method cache misses | 272 |  |
| Method cache collisions | 329 |  |
| Method cache dunder hits | 799 |  |
| Method cache dunder misses | 181 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 134,080 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


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
| Low confidence | 0 |  |
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
