
# Pystats results

- benchmark: python_startup
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 67,860 | 21.5% | 21.5% |  |
| LOAD_CONST | 20,260 | 6.4% | 28.0% |  |
| STORE_FAST | 16,360 | 5.2% | 33.2% |  |
| POP_JUMP_IF_FALSE | 14,540 | 4.6% | 37.8% |  |
| LOAD_GLOBAL_MODULE | 12,240 | 3.9% | 41.7% |  |
| RESUME_CHECK | 9,740 | 3.1% | 44.7% |  |
| LOAD_GLOBAL_BUILTIN | 9,120 | 2.9% | 47.6% | 7.2% |
| LOAD_FAST_LOAD_FAST | 8,200 | 2.6% | 50.2% |  |
| CALL | 7,880 | 2.5% | 52.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 7,880 | 2.5% | 55.2% |  |
| LOAD_ATTR_MODULE | 7,300 | 2.3% | 57.6% |  |
| POP_TOP | 7,280 | 2.3% | 59.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 6,740 | 2.1% | 62.0% |  |
| TO_BOOL_BOOL | 5,920 | 1.9% | 63.9% |  |
| PUSH_NULL | 5,720 | 1.8% | 65.7% |  |
| LOAD_ATTR | 5,440 | 1.7% | 67.4% |  |
| RETURN_VALUE | 5,340 | 1.7% | 69.1% |  |
| POP_JUMP_IF_NOT_NONE | 4,620 | 1.5% | 70.6% |  |
| RETURN_CONST | 4,620 | 1.5% | 72.1% |  |
| INTERPRETER_EXIT | 4,220 | 1.3% | 73.4% |  |
| COMPARE_OP_INT | 3,800 | 1.2% | 74.6% |  |
| NOP | 3,740 | 1.2% | 75.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 3,360 | 1.1% | 76.9% | 13.1% |
| LOAD_DEREF | 3,300 | 1.0% | 77.9% |  |
| CALL_PY_EXACT_ARGS | 3,300 | 1.0% | 78.9% |  |
| TO_BOOL | 3,140 | 1.0% | 79.9% |  |
| LOAD_GLOBAL | 3,140 | 1.0% | 80.9% |  |
| CALL_BUILTIN_FAST | 2,700 | 0.9% | 81.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,480 | 0.8% | 82.6% |  |
| POP_JUMP_IF_NONE | 2,420 | 0.8% | 83.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,400 | 0.8% | 84.1% |  |
| POP_JUMP_IF_TRUE | 2,240 | 0.7% | 84.8% |  |
| STORE_ATTR | 2,060 | 0.7% | 85.5% |  |
| BUILD_TUPLE | 1,980 | 0.6% | 86.1% |  |
| CALL_ISINSTANCE | 1,880 | 0.6% | 86.7% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,820 | 0.6% | 87.3% |  |
| STORE_FAST_STORE_FAST | 1,760 | 0.6% | 87.8% |  |
| BINARY_OP | 1,720 | 0.5% | 88.4% |  |
| JUMP_FORWARD | 1,540 | 0.5% | 88.9% |  |
| BUILD_LIST | 1,320 | 0.4% | 89.3% |  |
| CALL_FUNCTION_EX | 1,320 | 0.4% | 89.7% |  |
| DELETE_ATTR | 1,320 | 0.4% | 90.1% |  |
| CALL_BUILTIN_CLASS | 1,220 | 0.4% | 90.5% |  |
| BINARY_SLICE | 1,100 | 0.3% | 90.9% |  |
| COPY | 1,100 | 0.3% | 91.2% |  |
| MAKE_CELL | 1,100 | 0.3% | 91.6% |  |
| TO_BOOL_STR | 1,080 | 0.3% | 91.9% | 20.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,060 | 0.3% | 92.2% |  |
| COMPARE_OP | 1,020 | 0.3% | 92.6% |  |
| TO_BOOL_NONE | 1,000 | 0.3% | 92.9% |  |
| BEFORE_WITH | 880 | 0.3% | 93.2% |  |
| BUILD_MAP | 880 | 0.3% | 93.4% |  |
| CALL_KW | 880 | 0.3% | 93.7% |  |
| COPY_FREE_VARS | 880 | 0.3% | 94.0% |  |
| DICT_MERGE | 880 | 0.3% | 94.3% |  |
| CALL_LEN | 860 | 0.3% | 94.6% |  |
| CALL_METHOD_DESCRIPTOR_O | 800 | 0.3% | 94.8% |  |
| CALL_PY_WITH_DEFAULTS | 800 | 0.3% | 95.1% |  |
| TO_BOOL_INT | 800 | 0.3% | 95.3% |  |
| GET_ITER | 700 | 0.2% | 95.5% |  |
| SWAP | 680 | 0.2% | 95.8% |  |
| COMPARE_OP_STR | 660 | 0.2% | 96.0% | 33.3% |
| EXTENDED_ARG | 660 | 0.2% | 96.2% |  |
| STORE_DEREF | 660 | 0.2% | 96.4% |  |
| RESUME | 660 | 0.2% | 96.6% |  |
| BINARY_OP_ADD_INT | 660 | 0.2% | 96.8% |  |
| BINARY_SUBSCR_LIST_INT | 600 | 0.2% | 97.0% |  |
| CHECK_EXC_MATCH | 440 | 0.1% | 97.1% |  |
| MAKE_FUNCTION | 440 | 0.1% | 97.3% |  |
| POP_EXCEPT | 440 | 0.1% | 97.4% |  |
| PUSH_EXC_INFO | 440 | 0.1% | 97.6% |  |
| RETURN_GENERATOR | 440 | 0.1% | 97.7% |  |
| SET_FUNCTION_ATTRIBUTE | 440 | 0.1% | 97.8% |  |
| YIELD_VALUE | 440 | 0.1% | 98.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 400 | 0.1% | 98.1% | 100.0% |
| BINARY_SUBSCR_TUPLE_INT | 400 | 0.1% | 98.2% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 400 | 0.1% | 98.3% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 400 | 0.1% | 98.5% |  |
| FOR_ITER_LIST | 400 | 0.1% | 98.6% |  |
| LOAD_ATTR_CLASS | 400 | 0.1% | 98.7% |  |
| LOAD_ATTR_SLOT | 400 | 0.1% | 98.9% |  |
| UNPACK_SEQUENCE | 360 | 0.1% | 99.0% |  |
| FOR_ITER | 300 | 0.1% | 99.1% |  |
| IS_OP | 240 | 0.1% | 99.1% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 220 | 0.1% | 99.2% |  |
| CALL_INTRINSIC_1 | 220 | 0.1% | 99.3% |  |
| ENTER_EXECUTOR | 220 | 0.1% | 99.4% |  |
| LIST_EXTEND | 220 | 0.1% | 99.4% |  |
| BINARY_OP_ADD_UNICODE | 220 | 0.1% | 99.5% |  |
| BINARY_SUBSCR | 200 | 0.1% | 99.6% |  |
| CALL_STR_1 | 200 | 0.1% | 99.6% |  |
| CALL_TUPLE_1 | 200 | 0.1% | 99.7% |  |
| CALL_TYPE_1 | 200 | 0.1% | 99.7% |  |
| STORE_SUBSCR_DICT | 200 | 0.1% | 99.8% |  |
| TO_BOOL_ALWAYS_TRUE | 200 | 0.1% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 200 | 0.1% | 99.9% |  |
| FOR_ITER_TUPLE | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |
| CONTAINS_OP | 40 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_FAST | 7,920 | 2.5% | 2.5% |
| STORE_FAST LOAD_FAST | 7,740 | 2.5% | 5.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,260 | 2.3% | 7.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,780 | 2.2% | 9.4% |
| LOAD_FAST LOAD_CONST | 6,400 | 2.0% | 11.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 5,960 | 1.9% | 13.3% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 5,820 | 1.8% | 15.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,600 | 1.8% | 17.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 4,720 | 1.5% | 18.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 4,080 | 1.3% | 19.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,800 | 1.2% | 21.0% |
| RESUME_CHECK LOAD_FAST | 3,700 | 1.2% | 22.1% |
| PUSH_NULL LOAD_FAST | 3,520 | 1.1% | 23.3% |
| LOAD_CONST LOAD_FAST | 3,520 | 1.1% | 24.4% |
| CACHE RESUME_CHECK | 3,320 | 1.1% | 25.4% |
| LOAD_CONST LOAD_CONST | 3,080 | 1.0% | 26.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 2,960 | 0.9% | 27.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 2,900 | 0.9% | 28.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,860 | 0.9% | 29.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 2,860 | 0.9% | 30.1% |
| LOAD_FAST LOAD_ATTR | 2,760 | 0.9% | 31.0% |
| LOAD_CONST COMPARE_OP_INT | 2,700 | 0.9% | 31.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,680 | 0.9% | 32.7% |
| POP_TOP LOAD_FAST | 2,640 | 0.8% | 33.5% |
| LOAD_CONST STORE_FAST | 2,640 | 0.8% | 34.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 2,480 | 0.8% | 35.1% |
| LOAD_FAST CALL | 2,380 | 0.8% | 35.9% |
| RETURN_CONST INTERPRETER_EXIT | 2,200 | 0.7% | 36.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,160 | 0.7% | 37.3% |
| LOAD_FAST RETURN_VALUE | 1,980 | 0.6% | 37.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 1,980 | 0.6% | 38.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 1,980 | 0.6% | 39.2% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,960 | 0.6% | 39.8% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,960 | 0.6% | 40.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,960 | 0.6% | 41.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 1,800 | 0.6% | 41.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,780 | 0.6% | 42.2% |
| NOP LOAD_FAST | 1,760 | 0.6% | 42.7% |
| LOAD_FAST POP_JUMP_IF_NONE | 1,760 | 0.6% | 43.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,680 | 0.5% | 43.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,620 | 0.5% | 44.3% |
| TO_BOOL POP_JUMP_IF_FALSE | 1,600 | 0.5% | 44.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 1,600 | 0.5% | 45.3% |
| RETURN_VALUE INTERPRETER_EXIT | 1,580 | 0.5% | 45.8% |
| PUSH_NULL CALL | 1,540 | 0.5% | 46.3% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 1,420 | 0.5% | 46.8% |
| LOAD_FAST DELETE_ATTR | 1,320 | 0.4% | 47.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 1,320 | 0.4% | 47.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,320 | 0.4% | 48.0% |
| POP_JUMP_IF_NONE LOAD_FAST | 1,320 | 0.4% | 48.5% |
| RETURN_CONST POP_TOP | 1,320 | 0.4% | 48.9% |
| STORE_FAST STORE_FAST | 1,320 | 0.4% | 49.3% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,260 | 0.4% | 49.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,240 | 0.4% | 50.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,240 | 0.4% | 50.5% |
| LOAD_FAST STORE_ATTR | 1,220 | 0.4% | 50.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,200 | 0.4% | 51.2% |
| POP_TOP RETURN_CONST | 1,100 | 0.3% | 51.6% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 1,100 | 0.3% | 51.9% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,100 | 0.3% | 52.3% |
| STORE_FAST LOAD_CONST | 1,100 | 0.3% | 52.6% |
| LOAD_FAST TO_BOOL | 1,080 | 0.3% | 53.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,080 | 0.3% | 53.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 1,080 | 0.3% | 53.7% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 1,080 | 0.3% | 54.0% |
| TO_BOOL_STR POP_JUMP_IF_FALSE | 1,080 | 0.3% | 54.4% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 1,060 | 0.3% | 54.7% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 1,040 | 0.3% | 55.0% |
| LOAD_CONST CALL | 1,000 | 0.3% | 55.3% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 1,000 | 0.3% | 55.7% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 980 | 0.3% | 56.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 900 | 0.3% | 56.3% |
| DELETE_ATTR LOAD_FAST | 880 | 0.3% | 56.5% |
| DICT_MERGE CALL_FUNCTION_EX | 880 | 0.3% | 56.8% |
| JUMP_FORWARD LOAD_FAST | 880 | 0.3% | 57.1% |
| LOAD_CONST CALL_KW | 880 | 0.3% | 57.4% |
| LOAD_FAST COPY | 880 | 0.3% | 57.6% |
| LOAD_FAST TO_BOOL_STR | 880 | 0.3% | 57.9% |
| POP_JUMP_IF_NONE LOAD_CONST | 880 | 0.3% | 58.2% |
| RETURN_CONST STORE_FAST | 880 | 0.3% | 58.5% |
| STORE_FAST NOP | 880 | 0.3% | 58.8% |
| CALL POP_TOP | 840 | 0.3% | 59.0% |
| LOAD_FAST CALL_LEN | 840 | 0.3% | 59.3% |
| COPY_FREE_VARS RESUME_CHECK | 820 | 0.3% | 59.6% |
| CALL_BUILTIN_FAST STORE_FAST | 820 | 0.3% | 59.8% |
| LOAD_ATTR_MODULE LOAD_FAST | 820 | 0.3% | 60.1% |
| NOP LOAD_GLOBAL_BUILTIN | 800 | 0.3% | 60.3% |
| CALL_BUILTIN_CLASS STORE_FAST | 800 | 0.3% | 60.6% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 800 | 0.3% | 60.8% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_FAST | 800 | 0.3% | 61.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 800 | 0.3% | 61.3% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 800 | 0.3% | 61.6% |
| LOAD_CONST CALL_BUILTIN_FAST | 760 | 0.2% | 61.8% |
| LOAD_FAST CALL_BUILTIN_CLASS | 760 | 0.2% | 62.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 760 | 0.2% | 62.3% |
| CALL CALL | 740 | 0.2% | 62.6% |
| CALL RETURN_VALUE | 720 | 0.2% | 62.8% |
| LOAD_FAST TO_BOOL_BOOL | 720 | 0.2% | 63.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 720 | 0.2% | 63.2% |
| LOAD_ATTR_MODULE LOAD_ATTR_MODULE | 720 | 0.2% | 63.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 60.0% |
| LOAD_CONST | 440 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 60.0% |
| GET_ITER | 220 | 20.0% |
| LOAD_FAST | 220 | 20.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,320 | 78.7% |
| POP_TOP | 440 | 10.4% |
| RESUME | 240 | 5.7% |
| MAKE_CELL | 220 | 5.2% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 440 | 50.0% |
| CALL | 220 | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE | 200 | 22.7% |
| LOAD_ATTR | 20 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 440 | 50.0% |
| STORE_FAST | 440 | 50.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 220 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 60 | 30.0% |
| CALL | 40 | 20.0% |
| STORE_FAST | 40 | 20.0% |
| BINARY_SUBSCR_TUPLE_INT | 40 | 20.0% |
| STORE_DEREF | 20 | 10.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 420 | 95.5% |
| LOAD_GLOBAL | 20 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 440 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260 | 37.1% |
| BINARY_SLICE | 220 | 31.4% |
| CALL_BUILTIN_CLASS | 220 | 31.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 360 | 51.4% |
| FOR_ITER | 300 | 42.9% |
| FOR_ITER_TUPLE | 40 | 5.7% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,200 | 52.1% |
| RETURN_VALUE | 1,580 | 37.4% |
| YIELD_VALUE | 440 | 10.4% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 440 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 880 | 23.5% |
| DELETE_ATTR | 440 | 11.8% |
| POP_JUMP_IF_NOT_NONE | 440 | 11.8% |
| RESUME_CHECK | 400 | 10.7% |
| NOP | 220 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,760 | 47.1% |
| LOAD_GLOBAL_BUILTIN | 800 | 21.4% |
| LOAD_GLOBAL_MODULE | 360 | 9.6% |
| NOP | 220 | 5.9% |
| LOAD_CONST | 220 | 5.9% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 440 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,320 | 18.1% |
| CALL | 840 | 11.5% |
| RETURN_VALUE | 660 | 9.1% |
| POP_JUMP_IF_TRUE | 660 | 9.1% |
| CALL_METHOD_DESCRIPTOR_O | 600 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,640 | 36.3% |
| RETURN_CONST | 1,100 | 15.1% |
| LOAD_CONST | 660 | 9.1% |
| LOAD_GLOBAL_MODULE | 540 | 7.4% |
| POP_EXCEPT | 440 | 6.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 420 | 95.5% |
| CALL | 20 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 400 | 90.9% |
| LOAD_GLOBAL | 40 | 9.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 4,080 | 71.3% |
| LOAD_FAST | 660 | 11.5% |
| LOAD_ATTR | 540 | 9.4% |
| LOAD_DEREF | 440 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,520 | 61.5% |
| CALL | 1,540 | 26.9% |
| LOAD_DEREF | 440 | 7.7% |
| LOAD_CONST | 220 | 3.8% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 100.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,980 | 37.1% |
| CALL | 720 | 13.5% |
| BUILD_TUPLE | 660 | 12.4% |
| CALL_BUILTIN_FAST | 640 | 12.0% |
| LOAD_ATTR_INSTANCE_VALUE | 400 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,580 | 29.6% |
| POP_TOP | 660 | 12.4% |
| STORE_FAST | 660 | 12.4% |
| BEFORE_WITH | 440 | 8.2% |
| TO_BOOL | 260 | 4.9% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| STORE_SUBSCR_DICT | 20 | 50.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,080 | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE | 560 | 17.8% |
| LOAD_ATTR | 280 | 8.9% |
| RETURN_VALUE | 260 | 8.3% |
| TO_BOOL | 240 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,600 | 51.0% |
| TO_BOOL_BOOL | 460 | 14.6% |
| POP_JUMP_IF_TRUE | 400 | 12.7% |
| TO_BOOL | 240 | 7.6% |
| EXTENDED_ARG | 220 | 7.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 38.4% |
| CALL_LEN | 660 | 38.4% |
| BUILD_LIST | 220 | 12.8% |
| BINARY_OP | 180 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 38.4% |
| COMPARE_OP_STR | 660 | 38.4% |
| LOAD_FAST | 220 | 12.8% |
| BINARY_OP | 180 | 10.5% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 33.3% |
| STORE_FAST | 220 | 16.7% |
| CALL_STR_1 | 200 | 15.2% |
| LOAD_ATTR_INSTANCE_VALUE | 200 | 15.2% |
| RESUME_CHECK | 200 | 15.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 50.0% |
| BINARY_OP | 220 | 16.7% |
| LOAD_FAST | 220 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 13.6% |
| LOAD_ATTR | 40 | 3.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 50.0% |
| CALL_INTRINSIC_1 | 220 | 25.0% |
| LOAD_DEREF | 220 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 75.0% |
| LOAD_DEREF | 220 | 25.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,100 | 55.6% |
| LOAD_FAST | 440 | 22.2% |
| LOAD_DEREF | 220 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 200 | 10.1% |
| LOAD_GLOBAL | 20 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 660 | 33.3% |
| LOAD_CONST | 440 | 22.2% |
| CALL_METHOD_DESCRIPTOR_O | 360 | 18.2% |
| STORE_FAST | 220 | 11.1% |
| CALL_ISINSTANCE | 180 | 9.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,380 | 30.2% |
| PUSH_NULL | 1,540 | 19.5% |
| LOAD_CONST | 1,000 | 12.7% |
| CALL | 740 | 9.4% |
| LOAD_FAST_LOAD_FAST | 520 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 840 | 10.7% |
| CALL | 740 | 9.4% |
| RETURN_VALUE | 720 | 9.1% |
| LOAD_CONST | 700 | 8.9% |
| LOAD_FAST | 540 | 6.9% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 880 | 66.7% |
| LOAD_FAST | 440 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 440 | 33.3% |
| POP_TOP | 220 | 16.7% |
| COPY_FREE_VARS | 220 | 16.7% |
| MAKE_CELL | 220 | 16.7% |
| LOAD_GLOBAL_MODULE | 180 | 13.6% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 220 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 400 | 45.5% |
| LOAD_FAST | 220 | 25.0% |
| STORE_FAST | 220 | 25.0% |
| RESUME | 40 | 4.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 600 | 58.8% |
| LOAD_FAST_LOAD_FAST | 220 | 21.6% |
| LOAD_GLOBAL | 60 | 5.9% |
| LOAD_GLOBAL_MODULE | 60 | 5.9% |
| COMPARE_OP | 40 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 600 | 58.8% |
| COMPARE_OP_INT | 380 | 37.3% |
| COMPARE_OP | 40 | 3.9% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 40 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880 | 80.0% |
| RETURN_VALUE | 220 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 540 | 49.1% |
| LOAD_FAST | 220 | 20.0% |
| TO_BOOL_BOOL | 180 | 16.4% |
| TO_BOOL | 160 | 14.5% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 460 | 52.3% |
| CALL_FUNCTION_EX | 220 | 25.0% |
| CALL_PY_EXACT_ARGS | 200 | 22.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 820 | 93.2% |
| RESUME | 60 | 6.8% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880 | 66.7% |
| NOP | 440 | 33.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 75.0% |
| LOAD_DEREF | 220 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 880 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 220 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 66.7% |
| TO_BOOL | 220 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220 | 33.3% |
| POP_JUMP_IF_NONE | 220 | 33.3% |
| POP_JUMP_IF_NOT_NONE | 220 | 33.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 220 | 73.3% |
| FOR_ITER_LIST | 40 | 13.3% |
| NOP | 20 | 6.7% |
| RETURN_CONST | 20 | 6.7% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220 | 91.7% |
| LOAD_GLOBAL | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 220 | 91.7% |
| POP_JUMP_IF_FALSE | 20 | 8.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 40 | 100.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 42.9% |
| POP_JUMP_IF_FALSE | 440 | 28.6% |
| POP_TOP | 220 | 14.3% |
| POP_JUMP_IF_NOT_NONE | 220 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880 | 57.1% |
| LOAD_CONST | 220 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 180 | 11.7% |
| LOAD_GLOBAL_MODULE | 180 | 11.7% |
| LOAD_GLOBAL | 80 | 5.2% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 220 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,760 | 50.7% |
| LOAD_GLOBAL_MODULE | 760 | 14.0% |
| LOAD_GLOBAL | 540 | 9.9% |
| LOAD_ATTR | 460 | 8.5% |
| LOAD_ATTR_INSTANCE_VALUE | 460 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 700 | 12.9% |
| LOAD_ATTR_MODULE | 620 | 11.4% |
| PUSH_NULL | 540 | 9.9% |
| LOAD_FAST_LOAD_FAST | 540 | 9.9% |
| LOAD_ATTR | 460 | 8.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,400 | 31.6% |
| LOAD_CONST | 3,080 | 15.2% |
| STORE_ATTR_INSTANCE_VALUE | 1,800 | 8.9% |
| STORE_FAST | 1,100 | 5.4% |
| POP_JUMP_IF_NONE | 880 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,520 | 17.4% |
| LOAD_CONST | 3,080 | 15.2% |
| COMPARE_OP_INT | 2,700 | 13.3% |
| STORE_FAST | 2,640 | 13.0% |
| CALL | 1,000 | 4.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 660 | 20.0% |
| PUSH_NULL | 440 | 13.3% |
| LOAD_GLOBAL_MODULE | 420 | 12.7% |
| LOAD_ATTR_MODULE | 400 | 12.1% |
| NOP | 220 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 660 | 20.0% |
| CALL_PY_EXACT_ARGS | 540 | 16.4% |
| PUSH_NULL | 440 | 13.3% |
| BUILD_MAP | 220 | 6.7% |
| BUILD_TUPLE | 220 | 6.7% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,920 | 11.7% |
| STORE_FAST | 7,740 | 11.4% |
| POP_JUMP_IF_FALSE | 7,260 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 5,600 | 8.3% |
| RESUME_CHECK | 3,700 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,920 | 11.7% |
| LOAD_ATTR_INSTANCE_VALUE | 6,780 | 10.0% |
| LOAD_CONST | 6,400 | 9.4% |
| STORE_ATTR_INSTANCE_VALUE | 5,820 | 8.6% |
| POP_JUMP_IF_NOT_NONE | 2,860 | 4.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,320 | 16.1% |
| POP_JUMP_IF_FALSE | 1,320 | 16.1% |
| LOAD_DEREF | 660 | 8.0% |
| STORE_FAST_STORE_FAST | 660 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 600 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,980 | 24.1% |
| LOAD_FAST_LOAD_FAST | 1,320 | 16.1% |
| BUILD_TUPLE | 1,100 | 13.4% |
| STORE_ATTR | 700 | 8.5% |
| LOAD_GLOBAL_BUILTIN | 660 | 8.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 560 | 17.8% |
| LOAD_FAST | 500 | 15.9% |
| POP_JUMP_IF_FALSE | 420 | 13.4% |
| RESUME | 220 | 7.0% |
| RESUME_CHECK | 220 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 980 | 31.2% |
| LOAD_GLOBAL_BUILTIN | 560 | 17.8% |
| LOAD_ATTR | 540 | 17.2% |
| LOAD_FAST | 440 | 14.0% |
| CALL | 180 | 5.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 440 | 40.0% |
| CACHE | 220 | 20.0% |
| CALL_FUNCTION_EX | 220 | 20.0% |
| CALL_PY_EXACT_ARGS | 200 | 18.2% |
| CALL | 20 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 600 | 54.5% |
| MAKE_CELL | 440 | 40.0% |
| RESUME | 60 | 5.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 4,720 | 32.5% |
| COMPARE_OP_INT | 3,800 | 26.1% |
| TO_BOOL | 1,600 | 11.0% |
| TO_BOOL_STR | 1,080 | 7.4% |
| TO_BOOL_INT | 800 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,260 | 49.9% |
| LOAD_FAST_LOAD_FAST | 1,320 | 9.1% |
| LOAD_GLOBAL_MODULE | 1,260 | 8.7% |
| RETURN_CONST | 1,100 | 7.6% |
| LOAD_CONST | 660 | 4.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,760 | 72.7% |
| LOAD_ATTR_INSTANCE_VALUE | 400 | 16.5% |
| EXTENDED_ARG | 220 | 9.1% |
| LOAD_ATTR | 40 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,320 | 54.5% |
| LOAD_CONST | 880 | 36.4% |
| NOP | 220 | 9.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,860 | 61.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,000 | 21.6% |
| EXTENDED_ARG | 220 | 4.8% |
| LOAD_DEREF | 220 | 4.8% |
| LOAD_GLOBAL_MODULE | 200 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,980 | 42.9% |
| LOAD_GLOBAL_BUILTIN | 540 | 11.7% |
| NOP | 440 | 9.5% |
| LOAD_CONST | 440 | 9.5% |
| LOAD_GLOBAL_MODULE | 360 | 7.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,200 | 53.6% |
| TO_BOOL_NONE | 600 | 26.8% |
| TO_BOOL | 400 | 17.9% |
| CONTAINS_OP | 40 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 660 | 29.5% |
| LOAD_FAST | 660 | 29.5% |
| LOAD_GLOBAL_MODULE | 360 | 16.1% |
| NOP | 220 | 9.8% |
| LOAD_GLOBAL_BUILTIN | 220 | 9.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,100 | 23.8% |
| POP_JUMP_IF_FALSE | 1,100 | 23.8% |
| STORE_ATTR_INSTANCE_VALUE | 1,040 | 22.5% |
| STORE_ATTR | 500 | 10.8% |
| POP_EXCEPT | 440 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 2,200 | 47.6% |
| POP_TOP | 1,320 | 28.6% |
| STORE_FAST | 880 | 19.0% |
| TO_BOOL_NONE | 180 | 3.9% |
| TO_BOOL | 40 | 0.9% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 440 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,220 | 59.2% |
| LOAD_FAST_LOAD_FAST | 700 | 34.0% |
| STORE_ATTR | 140 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 520 | 25.2% |
| RETURN_CONST | 500 | 24.3% |
| LOAD_FAST | 440 | 21.4% |
| LOAD_CONST | 180 | 8.7% |
| LOAD_GLOBAL_MODULE | 180 | 8.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 220 | 33.3% |
| CALL | 220 | 33.3% |
| BINARY_SUBSCR_LIST_INT | 200 | 30.3% |
| BINARY_SUBSCR | 20 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 360 | 54.5% |
| LOAD_FAST | 220 | 33.3% |
| LOAD_GLOBAL | 80 | 12.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,640 | 16.1% |
| STORE_FAST | 1,320 | 8.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,080 | 6.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,060 | 6.5% |
| RETURN_CONST | 880 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,740 | 47.3% |
| LOAD_GLOBAL_MODULE | 2,680 | 16.4% |
| STORE_FAST | 1,320 | 8.1% |
| LOAD_CONST | 1,100 | 6.7% |
| NOP | 880 | 5.4% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,620 | 92.0% |
| UNPACK_SEQUENCE | 140 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 37.5% |
| LOAD_FAST_LOAD_FAST | 660 | 37.5% |
| LOAD_CONST | 440 | 25.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 64.7% |
| RETURN_VALUE | 220 | 32.4% |
| LOAD_GLOBAL | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 64.7% |
| LOAD_CONST | 220 | 32.4% |
| POP_TOP | 20 | 2.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 120 | 33.3% |
| LOAD_CONST | 120 | 33.3% |
| RETURN_VALUE | 80 | 22.2% |
| CALL_BUILTIN_FAST | 20 | 5.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 160 | 44.4% |
| STORE_FAST_STORE_FAST | 140 | 38.9% |
| STORE_FAST | 40 | 11.1% |
| UNPACK_SEQUENCE_TUPLE | 20 | 5.6% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220 | 50.0% |
| LOAD_FAST | 220 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 440 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 240 | 36.4% |
| CALL | 220 | 33.3% |
| COPY_FREE_VARS | 60 | 9.1% |
| MAKE_CELL | 60 | 9.1% |
| POP_TOP | 40 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 45.5% |
| LOAD_GLOBAL | 220 | 33.3% |
| NOP | 40 | 6.1% |
| POP_TOP | 40 | 6.1% |
| BUILD_LIST | 20 | 3.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 660 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 100.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 220 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540 | 90.0% |
| BINARY_SUBSCR | 60 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 360 | 60.0% |
| STORE_DEREF | 200 | 33.3% |
| CALL | 40 | 6.7% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 90.0% |
| BINARY_SUBSCR | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 400 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 90.0% |
| CALL | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 400 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 760 | 62.3% |
| BINARY_SUBSCR_LIST_INT | 360 | 29.5% |
| CALL | 100 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 800 | 65.6% |
| GET_ITER | 220 | 18.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 180 | 14.8% |
| CALL | 20 | 1.6% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 800 | 29.6% |
| LOAD_CONST | 760 | 28.1% |
| LOAD_FAST | 580 | 21.5% |
| LOAD_FAST_LOAD_FAST | 200 | 7.4% |
| CALL | 180 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 820 | 30.4% |
| RETURN_VALUE | 640 | 23.7% |
| PUSH_EXC_INFO | 420 | 15.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 400 | 14.8% |
| POP_TOP | 200 | 7.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,960 | 79.0% |
| LOAD_FAST_LOAD_FAST | 180 | 7.3% |
| CALL_BUILTIN_CLASS | 180 | 7.3% |
| CALL | 160 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,080 | 43.5% |
| LOAD_FAST | 600 | 24.2% |
| POP_TOP | 400 | 16.1% |
| CALL_TUPLE_1 | 180 | 7.3% |
| TO_BOOL_BOOL | 180 | 7.3% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,420 | 75.5% |
| BUILD_TUPLE | 180 | 9.6% |
| LOAD_ATTR_MODULE | 180 | 9.6% |
| CALL | 100 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,780 | 94.7% |
| TO_BOOL | 100 | 5.3% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 840 | 97.7% |
| CALL | 20 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 660 | 76.7% |
| LOAD_CONST | 200 | 23.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 62.3% |
| LOAD_ATTR | 180 | 17.0% |
| LOAD_CONST | 180 | 17.0% |
| CALL | 40 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,060 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 180 | 45.0% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 45.0% |
| CALL | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 200 | 50.0% |
| STORE_FAST | 200 | 50.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 180 | 45.0% |
| LOAD_ATTR_METHOD_NO_DICT | 180 | 45.0% |
| CALL | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 200 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 45.0% |
| UNPACK_SEQUENCE | 20 | 5.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 360 | 45.0% |
| LOAD_CONST | 180 | 22.5% |
| LOAD_FAST | 180 | 22.5% |
| CALL | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 600 | 75.0% |
| LOAD_CONST | 200 | 25.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,600 | 48.5% |
| LOAD_DEREF | 540 | 16.4% |
| LOAD_GLOBAL_MODULE | 540 | 16.4% |
| CALL | 220 | 6.7% |
| LOAD_FAST_LOAD_FAST | 220 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,900 | 87.9% |
| COPY_FREE_VARS | 200 | 6.1% |
| MAKE_CELL | 200 | 6.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 45.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 360 | 45.0% |
| CALL | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 800 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 90.0% |
| CALL | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 200 | 100.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 180 | 90.0% |
| CALL | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 90.0% |
| CALL | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 200 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,700 | 71.1% |
| LOAD_GLOBAL_MODULE | 540 | 14.2% |
| COMPARE_OP | 380 | 10.0% |
| LOAD_ATTR_INSTANCE_VALUE | 180 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,800 | 100.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 660 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 660 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 360 | 90.0% |
| FOR_ITER | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 200 | 50.0% |
| RETURN_CONST | 200 | 50.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40 | 50.0% |
| JUMP_BACKWARD | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 75.0% |
| LOAD_GLOBAL | 20 | 25.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 90.0% |
| LOAD_ATTR | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,780 | 86.0% |
| LOAD_ATTR | 700 | 8.9% |
| LOAD_FAST_LOAD_FAST | 400 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 15.7% |
| POP_JUMP_IF_NOT_NONE | 1,000 | 12.7% |
| TO_BOOL_BOOL | 900 | 11.4% |
| CALL_BUILTIN_FAST | 800 | 10.2% |
| TO_BOOL | 560 | 7.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,480 | 73.8% |
| LOAD_ATTR_INSTANCE_VALUE | 540 | 16.1% |
| BUILD_LIST | 180 | 5.4% |
| LOAD_ATTR | 160 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,960 | 58.3% |
| LOAD_CONST | 400 | 11.9% |
| LOAD_FAST_LOAD_FAST | 400 | 11.9% |
| LOAD_DEREF | 200 | 6.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 180 | 5.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,160 | 90.0% |
| LOAD_ATTR | 240 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 800 | 33.3% |
| LOAD_FAST_LOAD_FAST | 600 | 25.0% |
| CALL_PY_WITH_DEFAULTS | 360 | 15.0% |
| CALL | 240 | 10.0% |
| LOAD_CONST | 200 | 8.3% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,960 | 81.6% |
| LOAD_ATTR_MODULE | 720 | 9.9% |
| LOAD_ATTR | 620 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 4,080 | 55.9% |
| LOAD_FAST | 820 | 11.2% |
| LOAD_ATTR_MODULE | 720 | 9.9% |
| LOAD_DEREF | 400 | 5.5% |
| LOAD_ATTR_SLOT | 360 | 4.9% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 360 | 90.0% |
| LOAD_ATTR | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 360 | 90.0% |
| TO_BOOL | 40 | 10.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,960 | 21.5% |
| RESUME_CHECK | 1,240 | 13.6% |
| NOP | 800 | 8.8% |
| STORE_FAST | 720 | 7.9% |
| LOAD_GLOBAL_BUILTIN | 720 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,600 | 61.4% |
| CALL_ISINSTANCE | 1,420 | 15.6% |
| LOAD_GLOBAL_BUILTIN | 720 | 7.9% |
| CHECK_EXC_MATCH | 420 | 4.6% |
| CALL | 260 | 2.9% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,960 | 24.2% |
| STORE_FAST | 2,680 | 21.9% |
| POP_JUMP_IF_FALSE | 1,260 | 10.3% |
| LOAD_FAST | 1,080 | 8.8% |
| LOAD_GLOBAL | 980 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 5,960 | 48.7% |
| LOAD_FAST | 1,680 | 13.7% |
| TO_BOOL_BOOL | 1,080 | 8.8% |
| LOAD_ATTR | 760 | 6.2% |
| CALL_PY_EXACT_ARGS | 540 | 4.4% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 3,320 | 34.1% |
| CALL_PY_EXACT_ARGS | 2,900 | 29.8% |
| COPY_FREE_VARS | 820 | 8.4% |
| CALL_PY_WITH_DEFAULTS | 800 | 8.2% |
| MAKE_CELL | 600 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,700 | 38.0% |
| LOAD_GLOBAL_MODULE | 2,960 | 30.4% |
| LOAD_GLOBAL_BUILTIN | 1,240 | 12.7% |
| NOP | 400 | 4.1% |
| POP_TOP | 400 | 4.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,820 | 86.4% |
| STORE_ATTR | 520 | 7.7% |
| LOAD_FAST_LOAD_FAST | 400 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,860 | 42.4% |
| LOAD_CONST | 1,800 | 26.7% |
| RETURN_CONST | 1,040 | 15.4% |
| LOAD_FAST_LOAD_FAST | 420 | 6.2% |
| LOAD_GLOBAL_BUILTIN | 400 | 5.9% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 180 | 90.0% |
| STORE_SUBSCR | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 180 | 90.0% |
| TO_BOOL | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 200 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,780 | 30.1% |
| LOAD_GLOBAL_MODULE | 1,080 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 900 | 15.2% |
| LOAD_FAST | 720 | 12.2% |
| TO_BOOL | 460 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,720 | 79.7% |
| POP_JUMP_IF_TRUE | 1,200 | 20.3% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 360 | 45.0% |
| LOAD_FAST | 180 | 22.5% |
| LOAD_ATTR_INSTANCE_VALUE | 180 | 22.5% |
| TO_BOOL | 80 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 800 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 540 | 54.0% |
| RETURN_CONST | 180 | 18.0% |
| LOAD_ATTR_INSTANCE_VALUE | 180 | 18.0% |
| TO_BOOL | 100 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 600 | 60.0% |
| POP_JUMP_IF_FALSE | 400 | 40.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880 | 81.5% |
| RETURN_VALUE | 180 | 16.7% |
| TO_BOOL | 20 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,080 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 180 | 90.0% |
| UNPACK_SEQUENCE | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 540 | 29.7% |
| CALL_BUILTIN_FAST | 400 | 22.0% |
| CALL | 360 | 19.8% |
| RETURN_VALUE | 180 | 9.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 180 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,620 | 89.0% |
| STORE_FAST | 200 | 11.0% |


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
|     deferred | 1,540 | 54.6% |
|          hit | 1,100 | 39.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 0 | 0.0% |
| Failure | 180 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 100 | 55.6% |
| add different types | 40 | 22.2% |
| multiply different types | 40 | 22.2% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 8.3% |
|          hit | 1,000 | 83.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,420 | 25.9% |
|          hit | 16,500 | 66.6% |
|         miss | 400 | 1.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,160 | 62.4% |
| Failure | 700 | 37.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 200 | 28.6% |
| cfunc noargs | 200 | 28.6% |
| class no vectorcall | 120 | 17.1% |
| metaclass | 100 | 14.3% |
| cfunc varargs | 40 | 5.7% |
| meth descr varargs | 40 | 5.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 820 | 15.0% |
|          hit | 4,240 | 77.4% |
|         miss | 220 | 4.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 90.5% |
| Failure | 40 | 9.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 40 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 33.3% |
|          hit | 480 | 61.5% |

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
|     deferred | 3,840 | 14.1% |
|          hit | 21,300 | 78.4% |
|         miss | 440 | 1.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,800 | 88.2% |
| Failure | 240 | 11.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 80 | 33.3% |
| metaclass attribute | 60 | 25.0% |
| shadowed | 40 | 16.7% |
| class attr descriptor | 40 | 16.7% |
| class attr simple | 20 | 8.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,260 | 9.2% |
|          hit | 20,700 | 84.5% |
|         miss | 660 | 2.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,540 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,400 | 15.9% |
|          hit | 6,740 | 76.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 520 | 78.8% |
| Failure | 140 | 21.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 100 | 71.4% |
| not managed dict | 40 | 28.6% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 8.3% |
|          hit | 200 | 83.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,440 | 20.1% |
|          hit | 8,780 | 72.3% |
|         miss | 220 | 1.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 680 | 73.9% |
| Failure | 240 | 26.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 80 | 33.3% |
| sequence | 80 | 33.3% |
| bytearray | 40 | 16.7% |
| tuple | 40 | 16.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 7.6% |
|          hit | 2,020 | 84.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 170,160 | 54.0% |
| Not specialized | 50,220 | 15.9% |
| Specialized hits | 92,800 | 29.4% |
| Specialized misses | 1,940 | 0.6% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 6,420 | 33.3% |
| LOAD_ATTR | 3,840 | 19.9% |
| TO_BOOL | 2,440 | 12.7% |
| LOAD_GLOBAL | 2,260 | 11.7% |
| BINARY_OP | 1,540 | 8.0% |
| STORE_ATTR | 1,400 | 7.3% |
| COMPARE_OP | 820 | 4.3% |
| FOR_ITER | 260 | 1.3% |
| UNPACK_SEQUENCE | 180 | 0.9% |
| BINARY_SUBSCR | 100 | 0.5% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 660 | 34.0% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 22.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 400 | 20.6% |
| COMPARE_OP_STR | 220 | 11.3% |
| TO_BOOL_STR | 220 | 11.3% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 4,220 | 38.9% |
| Calls to Python functions inlined | 6,620 | 61.1% |
| Calls via PyEval_EvalFrame (total) | 4,220 | 38.9% |
| Calls via PyEval_EvalFrame (vector) | 3,340 | 30.8% |
| Calls via PyEval_EvalFrame (generator) | 880 | 8.1% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 3,340 | 30.8% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 880 | 8.1% |
| Calls via PyEval_EvalFrame (api) | 440 | 4.1% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 440 | 4.1% |
| Frames pushed | 9,960 | 91.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 15,320 | 37.4% |
| Frees to freelist | 15,460 |  |
| Allocations | 25,640 | 62.6% |
| Allocations to 512 bytes | 24,760 | 60.4% |
| Allocations to 4 kbytes | 220 | 0.5% |
| Allocations over 4 kbytes | 660 | 1.6% |
| Frees | 25,240 |  |
| New values | 1,100 |  |
| Interpreter increfs | 114,460 | 65.8% |
| Interpreter decrefs | 134,460 | 64.5% |
| Increfs | 59,380 | 34.2% |
| Decrefs | 73,944 | 35.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 15,653 |  |
| Method cache misses | 1,687 |  |
| Method cache collisions | 2,050 |  |
| Method cache dunder hits | 6,377 |  |
| Method cache dunder misses | 963 |  |


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
