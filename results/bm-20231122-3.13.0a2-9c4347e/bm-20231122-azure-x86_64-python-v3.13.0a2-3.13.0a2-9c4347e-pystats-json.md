
# Pystats results

- benchmark: json
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 52,299,360 | 22.4% | 22.4% |  |
| POP_JUMP_IF_NOT_NONE | 16,512,000 | 7.1% | 29.4% |  |
| CALL | 13,770,440 | 5.9% | 35.3% |  |
| LOAD_FAST_LOAD_FAST | 11,010,960 | 4.7% | 40.0% |  |
| PUSH_NULL | 8,261,440 | 3.5% | 43.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 8,258,600 | 3.5% | 47.1% |  |
| LOAD_CONST | 8,256,480 | 3.5% | 50.6% |  |
| RESUME_CHECK | 8,256,360 | 3.5% | 54.1% |  |
| RETURN_VALUE | 8,256,320 | 3.5% | 57.6% |  |
| LOAD_GLOBAL_BUILTIN | 8,256,060 | 3.5% | 61.2% |  |
| POP_JUMP_IF_FALSE | 8,256,000 | 3.5% | 64.7% |  |
| STORE_FAST | 5,514,720 | 2.4% | 67.1% |  |
| LOAD_GLOBAL_MODULE | 5,509,360 | 2.4% | 69.4% |  |
| STORE_FAST_STORE_FAST | 5,504,160 | 2.4% | 71.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 5,504,100 | 2.4% | 74.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 5,504,020 | 2.4% | 76.5% |  |
| POP_JUMP_IF_TRUE | 5,504,000 | 2.4% | 78.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,503,960 | 2.4% | 81.2% |  |
| TO_BOOL_BOOL | 5,503,960 | 2.4% | 83.5% |  |
| LOAD_ATTR_MODULE | 2,757,180 | 1.2% | 84.7% |  |
| JUMP_BACKWARD | 2,754,560 | 1.2% | 85.9% |  |
| FOR_ITER_LIST | 2,754,540 | 1.2% | 87.1% |  |
| TO_BOOL | 2,752,980 | 1.2% | 88.2% |  |
| POP_TOP | 2,752,280 | 1.2% | 89.4% |  |
| LOAD_ATTR_INSTANCE_VALUE | 2,752,140 | 1.2% | 90.6% |  |
| NOP | 2,752,080 | 1.2% | 91.8% |  |
| BUILD_TUPLE | 2,752,080 | 1.2% | 92.9% |  |
| CALL_KW | 2,752,000 | 1.2% | 94.1% |  |
| CALL_ISINSTANCE | 2,751,980 | 1.2% | 95.3% |  |
| CALL_LEN | 2,751,980 | 1.2% | 96.5% |  |
| CALL_PY_WITH_DEFAULTS | 2,751,980 | 1.2% | 97.6% |  |
| COMPARE_OP_INT | 2,751,980 | 1.2% | 98.8% |  |
| TO_BOOL_STR | 2,751,980 | 1.2% | 100.0% |  |
| GET_ITER | 2,640 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 2,620 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 2,600 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% | 100.0% | 2.4% |
| BINARY_OP_SUBTRACT_FLOAT | 2,540 | 0.0% | 100.0% |  |
| LOAD_ATTR | 840 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 520 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 240 | 0.0% | 100.0% |  |
| BINARY_OP | 180 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 160 | 0.0% | 100.0% |  |
| BUILD_LIST | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| RETURN_CONST | 160 | 0.0% | 100.0% |  |
| CALL_PY_EXACT_ARGS | 140 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| RESUME | 120 | 0.0% | 100.0% |  |
| BINARY_SLICE | 80 | 0.0% | 100.0% |  |
| BEFORE_WITH | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| FOR_ITER | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 80 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |
| COMPARE_OP | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 16,512,000 | 7.1% | 7.1% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 16,512,000 | 7.1% | 14.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 8,256,000 | 3.5% | 17.6% |
| STORE_FAST LOAD_FAST | 5,509,280 | 2.4% | 20.0% |
| PUSH_NULL LOAD_FAST | 5,504,160 | 2.4% | 22.3% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 5,504,100 | 2.4% | 24.7% |
| LOAD_CONST CALL | 5,504,080 | 2.4% | 27.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,504,020 | 2.4% | 29.4% |
| LOAD_FAST_LOAD_FAST CALL | 5,504,000 | 2.4% | 31.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 5,503,960 | 2.4% | 34.1% |
| CALL LOAD_ATTR_METHOD_NO_DICT | 5,503,920 | 2.4% | 36.5% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 5,503,920 | 2.4% | 38.8% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_MODULE | 5,503,920 | 2.4% | 41.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_FAST | 5,503,920 | 2.4% | 43.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 2,757,180 | 1.2% | 44.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,757,080 | 1.2% | 45.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 2,754,520 | 1.2% | 47.1% |
| LOAD_FAST CALL | 2,752,200 | 1.2% | 48.2% |
| LOAD_FAST RETURN_VALUE | 2,752,160 | 1.2% | 49.4% |
| RETURN_VALUE RETURN_VALUE | 2,752,080 | 1.2% | 50.6% |
| BUILD_TUPLE RETURN_VALUE | 2,752,080 | 1.2% | 51.8% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 2,752,080 | 1.2% | 52.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 2,752,080 | 1.2% | 54.1% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 2,752,080 | 1.2% | 55.3% |
| RESUME_CHECK LOAD_FAST | 2,752,060 | 1.2% | 56.5% |
| LOAD_FAST TO_BOOL | 2,752,040 | 1.2% | 57.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,752,040 | 1.2% | 58.8% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 2,752,040 | 1.2% | 60.0% |
| POP_TOP JUMP_BACKWARD | 2,752,020 | 1.2% | 61.2% |
| TO_BOOL POP_JUMP_IF_TRUE | 2,752,020 | 1.2% | 62.3% |
| NOP LOAD_FAST | 2,752,000 | 1.2% | 63.5% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 2,752,000 | 1.2% | 64.7% |
| RETURN_VALUE POP_TOP | 2,752,000 | 1.2% | 65.9% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 2,752,000 | 1.2% | 67.0% |
| LOAD_CONST CALL_KW | 2,752,000 | 1.2% | 68.2% |
| LOAD_FAST PUSH_NULL | 2,752,000 | 1.2% | 69.4% |
| LOAD_FAST LOAD_CONST | 2,752,000 | 1.2% | 70.6% |
| LOAD_FAST_LOAD_FAST PUSH_NULL | 2,752,000 | 1.2% | 71.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,752,000 | 1.2% | 72.9% |
| CALL RESUME_CHECK | 2,751,980 | 1.2% | 74.1% |
| CALL_KW RESUME_CHECK | 2,751,980 | 1.2% | 75.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 2,751,980 | 1.2% | 76.5% |
| CALL_METHOD_DESCRIPTOR_FAST LOAD_CONST | 2,751,980 | 1.2% | 77.6% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 2,751,980 | 1.2% | 78.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 2,751,980 | 1.2% | 80.0% |
| FOR_ITER_LIST STORE_FAST | 2,751,980 | 1.2% | 81.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 2,751,980 | 1.2% | 82.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 2,751,980 | 1.2% | 83.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,751,980 | 1.2% | 84.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 2,751,980 | 1.2% | 85.9% |
| RESUME_CHECK NOP | 2,751,980 | 1.2% | 87.0% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 2,751,980 | 1.2% | 88.2% |
| CALL TO_BOOL_BOOL | 2,751,960 | 1.2% | 89.4% |
| CALL UNPACK_SEQUENCE_TWO_TUPLE | 2,751,960 | 1.2% | 90.6% |
| LOAD_FAST CALL_LEN | 2,751,960 | 1.2% | 91.7% |
| LOAD_FAST CALL_PY_WITH_DEFAULTS | 2,751,960 | 1.2% | 92.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,751,960 | 1.2% | 94.1% |
| LOAD_FAST TO_BOOL_STR | 2,751,960 | 1.2% | 95.3% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 2,751,960 | 1.2% | 96.4% |
| CALL_LEN COMPARE_OP_INT | 2,751,960 | 1.2% | 97.6% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 2,751,960 | 1.2% | 98.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_METHOD_WITH_VALUES | 2,751,960 | 1.2% | 100.0% |
| PUSH_NULL CALL | 5,280 | 0.0% | 100.0% |
| CALL STORE_FAST | 5,180 | 0.0% | 100.0% |
| CALL CALL | 4,640 | 0.0% | 100.0% |
| LOAD_FAST GET_ITER | 2,560 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 2,560 | 0.0% | 100.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 2,560 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_LIST | 2,540 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 2,540 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 2,540 | 0.0% | 100.0% |
| CALL_LIST_APPEND JUMP_BACKWARD | 2,540 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 2,540 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,540 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 2,520 | 0.0% | 100.0% |
| LOAD_FAST CALL_LIST_APPEND | 2,520 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,520 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_FLOAT BINARY_OP_ADD_FLOAT | 2,520 | 0.0% | 100.0% |
| FOR_ITER_LIST LOAD_GLOBAL_MODULE | 2,520 | 0.0% | 100.0% |
| TO_BOOL TO_BOOL | 860 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 360 | 0.0% | 100.0% |
| CALL POP_TOP | 200 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_FAST_LOAD_FAST | 200 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 200 | 0.0% | 100.0% |
| CACHE RESUME_CHECK | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 160 | 0.0% | 100.0% |
| STORE_FAST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 160 | 0.0% | 100.0% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 160 | 0.0% | 100.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 140 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 120 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |
| BINARY_OP STORE_FAST | 100 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 100 | 0.0% | 100.0% |
| LOAD_ATTR CALL | 100 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 160 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 97.0% |
| CALL_BUILTIN_CLASS | 60 | 2.3% |
| CALL | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 2,540 | 96.2% |
| FOR_ITER_RANGE | 60 | 2.3% |
| FOR_ITER | 40 | 1.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| RETURN_CONST | 80 | 50.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,751,980 | 100.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,000 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,752,000 | 100.0% |
| CALL | 200 | 0.0% |
| RETURN_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,752,020 | 100.0% |
| NOP | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST_CHECK | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,757,180 | 33.4% |
| LOAD_FAST | 2,752,000 | 33.3% |
| LOAD_FAST_LOAD_FAST | 2,752,000 | 33.3% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,504,160 | 66.6% |
| LOAD_FAST_LOAD_FAST | 2,752,000 | 33.3% |
| CALL | 5,280 | 0.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,160 | 33.3% |
| RETURN_VALUE | 2,752,080 | 33.3% |
| BUILD_TUPLE | 2,752,080 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,752,080 | 33.3% |
| POP_TOP | 2,752,000 | 33.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,752,000 | 33.3% |
| INTERPRETER_EXIT | 80 | 0.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,040 | 100.0% |
| TO_BOOL | 860 | 0.0% |
| CALL | 60 | 0.0% |
| CALL_ISINSTANCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,752,020 | 100.0% |
| TO_BOOL | 860 | 0.0% |
| POP_JUMP_IF_FALSE | 40 | 0.0% |
| TO_BOOL_BOOL | 40 | 0.0% |
| TO_BOOL_STR | 20 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 66.7% |
| BINARY_OP | 40 | 22.2% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 55.6% |
| BINARY_OP | 40 | 22.2% |
| BINARY_OP_ADD_FLOAT | 20 | 11.1% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 11.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,752,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,752,080 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,504,080 | 40.0% |
| LOAD_FAST_LOAD_FAST | 5,504,000 | 40.0% |
| LOAD_FAST | 2,752,200 | 20.0% |
| PUSH_NULL | 5,280 | 0.0% |
| CALL | 4,640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,503,920 | 40.0% |
| RESUME_CHECK | 2,751,980 | 20.0% |
| TO_BOOL_BOOL | 2,751,960 | 20.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,751,960 | 20.0% |
| STORE_FAST | 5,180 | 0.0% |


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

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,752,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,751,980 | 100.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 50.0% |
| CALL_LEN | 20 | 50.0% |

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
| FOR_ITER_LIST | 20 | 25.0% |
| FOR_ITER_RANGE | 20 | 25.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,752,020 | 99.9% |
| CALL_LIST_APPEND | 2,540 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 2,751,980 | 99.9% |
| FOR_ITER_RANGE | 2,540 | 0.1% |
| FOR_ITER | 40 | 0.0% |


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
| LOAD_FAST | 360 | 42.9% |
| LOAD_GLOBAL_MODULE | 200 | 23.8% |
| LOAD_GLOBAL | 120 | 14.3% |
| CALL | 80 | 9.5% |
| LOAD_ATTR | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 200 | 23.8% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 14.3% |
| PUSH_NULL | 100 | 11.9% |
| CALL | 100 | 11.9% |
| LOAD_ATTR_MODULE | 100 | 11.9% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,000 | 33.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,751,980 | 33.3% |
| LOAD_ATTR_METHOD_NO_DICT | 2,751,980 | 33.3% |
| LOAD_CONST | 160 | 0.0% |
| STORE_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,504,080 | 66.7% |
| CALL_KW | 2,752,000 | 33.3% |
| LOAD_CONST | 160 | 0.0% |
| BINARY_SLICE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


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
| POP_JUMP_IF_NOT_NONE | 16,512,000 | 31.6% |
| POP_JUMP_IF_FALSE | 8,256,000 | 15.8% |
| STORE_FAST | 5,509,280 | 10.5% |
| PUSH_NULL | 5,504,160 | 10.5% |
| LOAD_GLOBAL_BUILTIN | 5,504,020 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 16,512,000 | 31.6% |
| LOAD_GLOBAL_BUILTIN | 5,503,920 | 10.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,754,520 | 5.3% |
| CALL | 2,752,200 | 5.3% |
| RETURN_VALUE | 2,752,160 | 5.3% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 40 | 50.0% |
| LOAD_ATTR_METHOD_NO_DICT | 40 | 50.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,752,080 | 25.0% |
| PUSH_NULL | 2,752,000 | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE | 2,751,980 | 25.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,751,980 | 25.0% |
| STORE_FAST | 2,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,504,000 | 50.0% |
| BUILD_TUPLE | 2,752,080 | 25.0% |
| PUSH_NULL | 2,752,000 | 25.0% |
| LOAD_FAST | 2,560 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 15.4% |
| POP_JUMP_IF_TRUE | 80 | 15.4% |
| STORE_FAST | 80 | 15.4% |
| RESUME | 60 | 11.5% |
| RESUME_CHECK | 60 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160 | 30.8% |
| LOAD_ATTR | 120 | 23.1% |
| LOAD_GLOBAL_BUILTIN | 100 | 19.2% |
| LOAD_FAST | 80 | 15.4% |
| CALL | 40 | 7.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,503,960 | 66.7% |
| COMPARE_OP_INT | 2,751,980 | 33.3% |
| TO_BOOL | 40 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,256,000 | 100.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,512,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,512,000 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 2,752,020 | 50.0% |
| TO_BOOL_STR | 2,751,980 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,503,920 | 100.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 80 | 50.0% |
| POP_TOP | 80 | 50.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 2,752,040 | 49.9% |
| FOR_ITER_LIST | 2,751,980 | 49.9% |
| CALL | 5,180 | 0.1% |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% |
| FOR_ITER_RANGE | 2,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,509,280 | 99.9% |
| LOAD_FAST_LOAD_FAST | 2,560 | 0.0% |
| LOAD_GLOBAL_MODULE | 2,520 | 0.0% |
| LOAD_CONST | 160 | 0.0% |
| BUILD_LIST | 80 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 5,504,100 | 100.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,080 | 50.0% |
| LOAD_FAST_LOAD_FAST | 2,752,080 | 50.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 66.7% |
| CALL | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 60 | 50.0% |
| CALL_FUNCTION_EX | 20 | 16.7% |
| CALL_KW | 20 | 16.7% |
| COPY_FREE_VARS | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 60 | 50.0% |
| NOP | 20 | 16.7% |
| LOAD_DEREF | 20 | 16.7% |
| LOAD_FAST | 20 | 16.7% |


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
| LOAD_FAST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 100.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 100.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BEFORE_WITH | 60 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,751,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,751,960 | 100.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,751,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 2,751,960 | 100.0% |
| COMPARE_OP | 20 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,520 | 96.9% |
| CALL | 80 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,540 | 97.7% |
| LOAD_FAST_LOAD_FAST | 60 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,503,920 | 100.0% |
| CALL | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,752,040 | 50.0% |
| LOAD_CONST | 2,751,980 | 50.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 57.1% |
| LOAD_FAST | 40 | 28.6% |
| CALL | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 140 | 100.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,751,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,751,980 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 2,751,960 | 100.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,751,980 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,751,980 | 99.9% |
| GET_ITER | 2,540 | 0.1% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,751,980 | 99.9% |
| LOAD_GLOBAL_MODULE | 2,520 | 0.1% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,540 | 96.9% |
| GET_ITER | 60 | 2.3% |
| FOR_ITER | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 96.9% |
| LOAD_FAST | 80 | 3.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,040 | 100.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,751,980 | 100.0% |
| LOAD_FAST | 160 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,503,920 | 66.6% |
| LOAD_FAST | 2,754,520 | 33.4% |
| LOAD_ATTR | 120 | 0.0% |
| LOAD_FAST_CHECK | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 5,503,920 | 66.6% |
| LOAD_CONST | 2,751,980 | 33.3% |
| LOAD_FAST | 2,540 | 0.0% |
| CALL | 60 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,751,960 | 50.0% |
| LOAD_GLOBAL_MODULE | 2,751,960 | 50.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,751,980 | 50.0% |
| LOAD_FAST_LOAD_FAST | 2,751,980 | 50.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,757,080 | 100.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,757,180 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,503,920 | 66.7% |
| RESUME_CHECK | 2,752,000 | 33.3% |
| LOAD_GLOBAL | 100 | 0.0% |
| STORE_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,504,020 | 66.7% |
| CALL_ISINSTANCE | 2,751,960 | 33.3% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,503,920 | 99.9% |
| STORE_FAST | 2,520 | 0.0% |
| FOR_ITER_LIST | 2,520 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| RESUME_CHECK | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,757,080 | 50.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,751,960 | 50.0% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_FAST | 60 | 0.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,751,980 | 33.3% |
| CALL_KW | 2,751,980 | 33.3% |
| CALL_PY_WITH_DEFAULTS | 2,751,980 | 33.3% |
| CACHE | 160 | 0.0% |
| CALL_PY_EXACT_ARGS | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,752,060 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 2,752,000 | 33.3% |
| NOP | 2,751,980 | 33.3% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 66.7% |
| LOAD_FAST_LOAD_FAST | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 160 | 66.7% |
| LOAD_FAST | 80 | 33.3% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,751,960 | 50.0% |
| CALL_ISINSTANCE | 2,751,960 | 50.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,503,960 | 100.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,751,960 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,751,980 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,752,000 | 50.0% |
| CALL | 2,751,960 | 50.0% |
| CALL_BUILTIN_FAST | 80 | 0.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 5,504,100 | 100.0% |


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
|     deferred | 120 | 2.3% |
|          hit | 5,020 | 95.4% |
|         miss | 60 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 66.7% |
| Failure | 20 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 20 | 100.0% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,765,600 | 50.0% |
|          hit | 13,762,960 | 50.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 5.0% |
| Failure | 4,600 | 95.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cmethod | 1,720 | 37.4% |
| other | 860 | 18.7% |
| code complex parameters | 860 | 18.7% |
| meth descr varargs | 860 | 18.7% |
| cfunc noargs | 280 | 6.1% |
| cfunc varargs | 20 | 0.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 2,751,980 | 100.0% |

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
|     deferred | 40 | 0.0% |
|          hit | 2,757,160 | 100.0% |

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
|     deferred | 520 | 0.0% |
|          hit | 19,271,880 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 87.5% |
| Failure | 40 | 12.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 20 | 50.0% |
| class attr simple | 20 | 50.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 13,765,420 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|          hit | 240 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,752,060 | 25.0% |
|          hit | 8,255,940 | 75.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 6.5% |
| Failure | 860 | 93.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 860 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 5,504,100 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 112,870,480 | 48.2% |
| Not specialized | 46,797,280 | 20.0% |
| Specialized hits | 74,331,060 | 31.8% |
| Specialized misses | 60 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 13,765,600 | 83.3% |
| TO_BOOL | 2,752,060 | 16.7% |
| LOAD_ATTR | 520 | 0.0% |
| LOAD_GLOBAL | 260 | 0.0% |
| BINARY_OP | 120 | 0.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| COMPARE_OP | 20 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 60 | 100.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |
| RETURN_VALUE | 0 | 0.0% |
| BUILD_LIST | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 160 | 0.0% |
| Calls to Python functions inlined | 8,256,320 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 2,752,120 | 33.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 24,776,600 | 15.8% |
| Frees to freelist | 24,777,200 |  |
| Allocations | 132,238,740 | 84.2% |
| Allocations to 512 bytes | 132,102,900 | 84.1% |
| Allocations to 4 kbytes | 135,440 | 0.1% |
| Allocations over 4 kbytes | 400 | 0.0% |
| Frees | 137,742,151 |  |
| New values | 80 |  |
| Interpreter increfs | 115,615,900 | 31.1% |
| Interpreter decrefs | 129,387,700 | 25.5% |
| Increfs | 256,126,496 | 68.9% |
| Decrefs | 377,353,491 | 74.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 4,100 |  |
| Method cache misses | 240 |  |
| Method cache collisions | 164 |  |
| Method cache dunder hits | 394 |  |
| Method cache dunder misses | 6 |  |


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
| Optimization attempts | 0 |  |
| Traces created | 0 |  |
| Trace stack overflow | 0 |  |
| Trace stack underflow | 0 |  |
| Trace too long | 0 |  |
| Trace too short | 0 |  |
| Inner loop found | 0 |  |
| Recursive call | 0 |  |
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

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
