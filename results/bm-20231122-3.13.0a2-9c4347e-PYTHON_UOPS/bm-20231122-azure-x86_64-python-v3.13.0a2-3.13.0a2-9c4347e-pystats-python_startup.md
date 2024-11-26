
# Pystats results

- benchmark: python_startup
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 67,860 | 21.5% | 21.5% |  |
| LOAD_CONST | 20,260 | 6.4% | 28.0% |  |
| STORE_FAST | 16,360 | 5.2% | 33.1% |  |
| POP_JUMP_IF_FALSE | 14,100 | 4.5% | 37.6% |  |
| LOAD_GLOBAL_MODULE | 12,040 | 3.8% | 41.4% |  |
| RESUME_CHECK | 9,740 | 3.1% | 44.5% |  |
| LOAD_GLOBAL_BUILTIN | 9,120 | 2.9% | 47.4% | 7.2% |
| LOAD_FAST_LOAD_FAST | 8,200 | 2.6% | 50.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 7,880 | 2.5% | 52.5% |  |
| CALL | 7,420 | 2.4% | 54.9% |  |
| LOAD_ATTR_MODULE | 7,300 | 2.3% | 57.2% |  |
| POP_TOP | 7,280 | 2.3% | 59.5% |  |
| STORE_ATTR_INSTANCE_VALUE | 6,740 | 2.1% | 61.6% |  |
| PUSH_NULL | 6,160 | 2.0% | 63.6% |  |
| RETURN_VALUE | 5,960 | 1.9% | 65.5% |  |
| TO_BOOL_BOOL | 5,720 | 1.8% | 67.3% |  |
| LOAD_ATTR | 5,360 | 1.7% | 69.0% |  |
| POP_JUMP_IF_NOT_NONE | 4,620 | 1.5% | 70.5% |  |
| RETURN_CONST | 4,620 | 1.5% | 71.9% |  |
| NOP | 3,960 | 1.3% | 73.2% |  |
| COMPARE_OP_INT | 3,800 | 1.2% | 74.4% |  |
| INTERPRETER_EXIT | 3,600 | 1.1% | 75.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 3,360 | 1.1% | 76.6% | 13.1% |
| LOAD_DEREF | 3,300 | 1.0% | 77.7% |  |
| CALL_PY_EXACT_ARGS | 3,300 | 1.0% | 78.7% |  |
| TO_BOOL | 3,100 | 1.0% | 79.7% |  |
| LOAD_GLOBAL | 3,100 | 1.0% | 80.7% |  |
| CALL_BUILTIN_FAST | 2,700 | 0.9% | 81.5% |  |
| POP_JUMP_IF_TRUE | 2,460 | 0.8% | 82.3% |  |
| POP_JUMP_IF_NONE | 2,420 | 0.8% | 83.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,400 | 0.8% | 83.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,280 | 0.7% | 84.6% |  |
| STORE_ATTR | 2,060 | 0.7% | 85.2% |  |
| BUILD_TUPLE | 1,980 | 0.6% | 85.8% |  |
| CALL_ISINSTANCE | 1,880 | 0.6% | 86.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,820 | 0.6% | 87.0% |  |
| STORE_FAST_STORE_FAST | 1,760 | 0.6% | 87.6% |  |
| BINARY_OP | 1,720 | 0.5% | 88.1% |  |
| BUILD_LIST | 1,320 | 0.4% | 88.5% |  |
| CALL_FUNCTION_EX | 1,320 | 0.4% | 89.0% |  |
| DELETE_ATTR | 1,320 | 0.4% | 89.4% |  |
| JUMP_FORWARD | 1,320 | 0.4% | 89.8% |  |
| CALL_BUILTIN_CLASS | 1,220 | 0.4% | 90.2% |  |
| BINARY_SLICE | 1,100 | 0.3% | 90.5% |  |
| COPY | 1,100 | 0.3% | 90.9% |  |
| MAKE_CELL | 1,100 | 0.3% | 91.2% |  |
| TO_BOOL_STR | 1,080 | 0.3% | 91.6% | 20.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,060 | 0.3% | 91.9% |  |
| COMPARE_OP | 1,020 | 0.3% | 92.2% |  |
| TO_BOOL_NONE | 1,000 | 0.3% | 92.6% |  |
| BEFORE_WITH | 880 | 0.3% | 92.8% |  |
| BUILD_MAP | 880 | 0.3% | 93.1% |  |
| CALL_KW | 880 | 0.3% | 93.4% |  |
| COPY_FREE_VARS | 880 | 0.3% | 93.7% |  |
| DICT_MERGE | 880 | 0.3% | 93.9% |  |
| CALL_LEN | 860 | 0.3% | 94.2% |  |
| CALL_METHOD_DESCRIPTOR_O | 800 | 0.3% | 94.5% |  |
| CALL_PY_WITH_DEFAULTS | 800 | 0.3% | 94.7% |  |
| TO_BOOL_INT | 800 | 0.3% | 95.0% |  |
| GET_ITER | 700 | 0.2% | 95.2% |  |
| SWAP | 680 | 0.2% | 95.4% |  |
| COMPARE_OP_STR | 660 | 0.2% | 95.6% | 33.3% |
| EXTENDED_ARG | 660 | 0.2% | 95.8% |  |
| STORE_DEREF | 660 | 0.2% | 96.0% |  |
| RESUME | 660 | 0.2% | 96.3% |  |
| BINARY_OP_ADD_INT | 660 | 0.2% | 96.5% |  |
| EXIT_INIT_CHECK | 620 | 0.2% | 96.7% |  |
| CALL_ALLOC_AND_ENTER_INIT | 620 | 0.2% | 96.9% |  |
| BINARY_SUBSCR_LIST_INT | 600 | 0.2% | 97.0% |  |
| FOR_ITER | 520 | 0.2% | 97.2% |  |
| CHECK_EXC_MATCH | 440 | 0.1% | 97.4% |  |
| MAKE_FUNCTION | 440 | 0.1% | 97.5% |  |
| POP_EXCEPT | 440 | 0.1% | 97.6% |  |
| PUSH_EXC_INFO | 440 | 0.1% | 97.8% |  |
| RETURN_GENERATOR | 440 | 0.1% | 97.9% |  |
| SET_FUNCTION_ATTRIBUTE | 440 | 0.1% | 98.1% |  |
| YIELD_VALUE | 440 | 0.1% | 98.2% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 400 | 0.1% | 98.3% | 100.0% |
| BINARY_SUBSCR_TUPLE_INT | 400 | 0.1% | 98.4% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 400 | 0.1% | 98.6% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 400 | 0.1% | 98.7% |  |
| FOR_ITER_LIST | 400 | 0.1% | 98.8% |  |
| LOAD_ATTR_SLOT | 400 | 0.1% | 99.0% |  |
| UNPACK_SEQUENCE | 360 | 0.1% | 99.1% |  |
| JUMP_BACKWARD | 260 | 0.1% | 99.1% |  |
| IS_OP | 240 | 0.1% | 99.2% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 220 | 0.1% | 99.3% |  |
| CALL_INTRINSIC_1 | 220 | 0.1% | 99.4% |  |
| LIST_EXTEND | 220 | 0.1% | 99.4% |  |
| BINARY_OP_ADD_UNICODE | 220 | 0.1% | 99.5% |  |
| BINARY_SUBSCR | 200 | 0.1% | 99.6% |  |
| CALL_STR_1 | 200 | 0.1% | 99.6% |  |
| CALL_TUPLE_1 | 200 | 0.1% | 99.7% |  |
| CALL_TYPE_1 | 200 | 0.1% | 99.8% |  |
| STORE_SUBSCR_DICT | 200 | 0.1% | 99.8% |  |
| TO_BOOL_ALWAYS_TRUE | 200 | 0.1% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 200 | 0.1% | 99.9% |  |
| FOR_ITER_TUPLE | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |
| CONTAINS_OP | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_FAST | 7,920 | 2.5% | 2.5% |
| STORE_FAST LOAD_FAST | 7,740 | 2.5% | 5.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,480 | 2.4% | 7.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,780 | 2.2% | 9.5% |
| LOAD_FAST LOAD_CONST | 6,400 | 2.0% | 11.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 5,960 | 1.9% | 13.4% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 5,820 | 1.8% | 15.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 5,600 | 1.8% | 17.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 4,320 | 1.4% | 18.4% |
| LOAD_ATTR_MODULE PUSH_NULL | 4,080 | 1.3% | 19.7% |
| PUSH_NULL LOAD_FAST | 3,960 | 1.3% | 21.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,800 | 1.2% | 22.2% |
| RESUME_CHECK LOAD_FAST | 3,700 | 1.2% | 23.3% |
| LOAD_CONST LOAD_FAST | 3,520 | 1.1% | 24.5% |
| LOAD_CONST LOAD_CONST | 3,080 | 1.0% | 25.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 2,960 | 0.9% | 26.4% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 2,900 | 0.9% | 27.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,860 | 0.9% | 28.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 2,860 | 0.9% | 29.1% |
| CACHE RESUME_CHECK | 2,700 | 0.9% | 30.0% |
| LOAD_CONST COMPARE_OP_INT | 2,700 | 0.9% | 30.8% |
| LOAD_FAST LOAD_ATTR | 2,680 | 0.9% | 31.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,680 | 0.9% | 32.5% |
| POP_TOP LOAD_FAST | 2,640 | 0.8% | 33.4% |
| LOAD_CONST STORE_FAST | 2,640 | 0.8% | 34.2% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 2,480 | 0.8% | 35.0% |
| LOAD_FAST CALL | 2,380 | 0.8% | 35.7% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,160 | 0.7% | 36.4% |
| LOAD_FAST RETURN_VALUE | 1,980 | 0.6% | 37.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 1,980 | 0.6% | 37.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 1,980 | 0.6% | 38.3% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,960 | 0.6% | 38.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,960 | 0.6% | 39.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,960 | 0.6% | 40.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 1,800 | 0.6% | 40.7% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,780 | 0.6% | 41.3% |
| NOP LOAD_FAST | 1,760 | 0.6% | 41.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 1,760 | 0.6% | 42.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,680 | 0.5% | 43.0% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,620 | 0.5% | 43.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 1,600 | 0.5% | 44.0% |
| RETURN_VALUE INTERPRETER_EXIT | 1,580 | 0.5% | 44.5% |
| RETURN_CONST INTERPRETER_EXIT | 1,580 | 0.5% | 45.0% |
| TO_BOOL POP_JUMP_IF_FALSE | 1,560 | 0.5% | 45.5% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 1,420 | 0.5% | 45.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,400 | 0.4% | 46.4% |
| PUSH_NULL CALL | 1,360 | 0.4% | 46.8% |
| LOAD_FAST DELETE_ATTR | 1,320 | 0.4% | 47.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 1,320 | 0.4% | 47.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,320 | 0.4% | 48.1% |
| POP_JUMP_IF_NONE LOAD_FAST | 1,320 | 0.4% | 48.5% |
| RETURN_CONST POP_TOP | 1,320 | 0.4% | 48.9% |
| STORE_FAST STORE_FAST | 1,320 | 0.4% | 49.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,240 | 0.4% | 49.7% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,240 | 0.4% | 50.1% |
| LOAD_FAST STORE_ATTR | 1,220 | 0.4% | 50.5% |
| POP_TOP RETURN_CONST | 1,100 | 0.3% | 50.8% |
| LOAD_FAST PUSH_NULL | 1,100 | 0.3% | 51.2% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 1,100 | 0.3% | 51.5% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,100 | 0.3% | 51.9% |
| STORE_FAST LOAD_CONST | 1,100 | 0.3% | 52.2% |
| LOAD_FAST TO_BOOL | 1,080 | 0.3% | 52.6% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,080 | 0.3% | 52.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,080 | 0.3% | 53.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 1,080 | 0.3% | 53.6% |
| TO_BOOL_STR POP_JUMP_IF_FALSE | 1,080 | 0.3% | 54.0% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 1,060 | 0.3% | 54.3% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 1,040 | 0.3% | 54.6% |
| LOAD_CONST CALL | 1,000 | 0.3% | 54.9% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 1,000 | 0.3% | 55.3% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 960 | 0.3% | 55.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 900 | 0.3% | 55.8% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 900 | 0.3% | 56.1% |
| DELETE_ATTR LOAD_FAST | 880 | 0.3% | 56.4% |
| DICT_MERGE CALL_FUNCTION_EX | 880 | 0.3% | 56.7% |
| LOAD_CONST CALL_KW | 880 | 0.3% | 57.0% |
| LOAD_FAST COPY | 880 | 0.3% | 57.2% |
| LOAD_FAST TO_BOOL_STR | 880 | 0.3% | 57.5% |
| POP_JUMP_IF_NONE LOAD_CONST | 880 | 0.3% | 57.8% |
| RETURN_CONST STORE_FAST | 880 | 0.3% | 58.1% |
| STORE_FAST NOP | 880 | 0.3% | 58.4% |
| CALL POP_TOP | 840 | 0.3% | 58.6% |
| LOAD_FAST CALL_LEN | 840 | 0.3% | 58.9% |
| COPY_FREE_VARS RESUME_CHECK | 820 | 0.3% | 59.2% |
| CALL_BUILTIN_FAST STORE_FAST | 820 | 0.3% | 59.4% |
| LOAD_ATTR_MODULE LOAD_FAST | 820 | 0.3% | 59.7% |
| NOP LOAD_GLOBAL_BUILTIN | 800 | 0.3% | 59.9% |
| CALL_BUILTIN_CLASS STORE_FAST | 800 | 0.3% | 60.2% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 800 | 0.3% | 60.4% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_FAST | 800 | 0.3% | 60.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 800 | 0.3% | 60.9% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 800 | 0.3% | 61.2% |
| LOAD_CONST CALL_BUILTIN_FAST | 760 | 0.2% | 61.4% |
| LOAD_FAST CALL_BUILTIN_CLASS | 760 | 0.2% | 61.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 760 | 0.2% | 61.9% |
| CALL LOAD_FAST | 740 | 0.2% | 62.2% |
| LOAD_FAST TO_BOOL_BOOL | 720 | 0.2% | 62.4% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 720 | 0.2% | 62.6% |
| LOAD_ATTR_MODULE LOAD_ATTR_MODULE | 720 | 0.2% | 62.8% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 720 | 0.2% | 63.1% |


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
| RESUME_CHECK | 2,700 | 75.0% |
| POP_TOP | 440 | 12.2% |
| RESUME | 240 | 6.7% |
| MAKE_CELL | 220 | 6.1% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 640 | 72.7% |
| LOAD_ATTR_INSTANCE_VALUE | 200 | 22.7% |
| CALL | 20 | 2.3% |
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
| JUMP_BACKWARD | 220 | 100.0% |


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

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 620 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 620 | 100.0% |


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
| RETURN_VALUE | 1,580 | 43.9% |
| RETURN_CONST | 1,580 | 43.9% |
| YIELD_VALUE | 440 | 12.2% |


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
| STORE_FAST | 880 | 22.2% |
| DELETE_ATTR | 440 | 11.1% |
| POP_JUMP_IF_NOT_NONE | 440 | 11.1% |
| RESUME_CHECK | 400 | 10.1% |
| FOR_ITER | 240 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,760 | 44.4% |
| LOAD_GLOBAL_BUILTIN | 800 | 20.2% |
| LOAD_GLOBAL_MODULE | 540 | 13.6% |
| NOP | 220 | 5.6% |
| LOAD_CONST | 220 | 5.6% |


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
| LOAD_ATTR_MODULE | 4,080 | 66.2% |
| LOAD_FAST | 1,100 | 17.9% |
| LOAD_ATTR | 540 | 8.8% |
| LOAD_DEREF | 440 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,960 | 64.3% |
| CALL | 1,360 | 22.1% |
| LOAD_DEREF | 440 | 7.1% |
| LOAD_CONST | 220 | 3.6% |
| CALL_ALLOC_AND_ENTER_INIT | 180 | 2.9% |


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
| LOAD_FAST | 1,980 | 33.2% |
| RETURN_VALUE | 660 | 11.1% |
| BUILD_TUPLE | 660 | 11.1% |
| CALL_BUILTIN_FAST | 640 | 10.7% |
| EXIT_INIT_CHECK | 620 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,580 | 26.5% |
| POP_TOP | 660 | 11.1% |
| RETURN_VALUE | 660 | 11.1% |
| STORE_FAST | 660 | 11.1% |
| BEFORE_WITH | 640 | 10.7% |


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
| LOAD_FAST | 1,080 | 34.8% |
| LOAD_ATTR_INSTANCE_VALUE | 560 | 18.1% |
| LOAD_ATTR | 280 | 9.0% |
| RETURN_VALUE | 260 | 8.4% |
| TO_BOOL | 240 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,560 | 50.3% |
| TO_BOOL_BOOL | 440 | 14.2% |
| POP_JUMP_IF_TRUE | 420 | 13.5% |
| TO_BOOL | 240 | 7.7% |
| EXTENDED_ARG | 220 | 7.1% |


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
| LOAD_FAST | 2,380 | 32.1% |
| PUSH_NULL | 1,360 | 18.3% |
| LOAD_CONST | 1,000 | 13.5% |
| CALL | 680 | 9.2% |
| LOAD_FAST_LOAD_FAST | 300 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 840 | 11.3% |
| LOAD_FAST | 740 | 10.0% |
| LOAD_CONST | 700 | 9.4% |
| CALL | 680 | 9.2% |
| RESUME_CHECK | 500 | 6.7% |


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
| GET_ITER | 300 | 57.7% |
| JUMP_BACKWARD | 220 | 42.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 240 | 46.2% |
| STORE_FAST | 220 | 42.3% |
| FOR_ITER_LIST | 40 | 7.7% |
| RETURN_CONST | 20 | 3.8% |


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
| BINARY_OP_INPLACE_ADD_UNICODE | 220 | 84.6% |
| POP_JUMP_IF_TRUE | 40 | 15.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 220 | 84.6% |
| FOR_ITER_TUPLE | 40 | 15.4% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 660 | 50.0% |
| POP_TOP | 220 | 16.7% |
| POP_JUMP_IF_FALSE | 220 | 16.7% |
| POP_JUMP_IF_NOT_NONE | 220 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 50.0% |
| NOP | 220 | 16.7% |
| LOAD_CONST | 220 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 180 | 13.6% |
| LOAD_GLOBAL | 40 | 3.0% |


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
| LOAD_FAST | 2,680 | 50.0% |
| LOAD_GLOBAL_MODULE | 760 | 14.2% |
| LOAD_GLOBAL | 540 | 10.1% |
| LOAD_ATTR | 460 | 8.6% |
| LOAD_ATTR_INSTANCE_VALUE | 460 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 700 | 13.1% |
| LOAD_ATTR_MODULE | 620 | 11.6% |
| PUSH_NULL | 540 | 10.1% |
| LOAD_FAST_LOAD_FAST | 540 | 10.1% |
| LOAD_ATTR | 460 | 8.6% |


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
| PUSH_NULL | 440 | 13.3% |
| POP_JUMP_IF_FALSE | 440 | 13.3% |
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
| POP_JUMP_IF_FALSE | 7,480 | 11.0% |
| LOAD_GLOBAL_BUILTIN | 5,600 | 8.3% |
| PUSH_NULL | 3,960 | 5.8% |

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
| STORE_FAST | 560 | 18.1% |
| LOAD_FAST | 500 | 16.1% |
| POP_JUMP_IF_FALSE | 380 | 12.3% |
| RESUME | 220 | 7.1% |
| RESUME_CHECK | 220 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 960 | 31.0% |
| LOAD_GLOBAL_BUILTIN | 560 | 18.1% |
| LOAD_ATTR | 540 | 17.4% |
| LOAD_FAST | 440 | 14.2% |
| CALL | 180 | 5.8% |


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
| TO_BOOL_BOOL | 4,320 | 30.6% |
| COMPARE_OP_INT | 3,800 | 27.0% |
| TO_BOOL | 1,560 | 11.1% |
| TO_BOOL_STR | 1,080 | 7.7% |
| TO_BOOL_INT | 800 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,480 | 53.0% |
| LOAD_FAST_LOAD_FAST | 1,320 | 9.4% |
| RETURN_CONST | 1,100 | 7.8% |
| LOAD_GLOBAL_MODULE | 1,080 | 7.7% |
| LOAD_CONST | 660 | 4.7% |


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
| TO_BOOL_BOOL | 1,400 | 56.9% |
| TO_BOOL_NONE | 600 | 24.4% |
| TO_BOOL | 420 | 17.1% |
| CONTAINS_OP | 40 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 660 | 26.8% |
| LOAD_FAST | 660 | 26.8% |
| LOAD_GLOBAL_MODULE | 360 | 14.6% |
| NOP | 220 | 8.9% |
| LOAD_DEREF | 220 | 8.9% |


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
| INTERPRETER_EXIT | 1,580 | 34.2% |
| POP_TOP | 1,320 | 28.6% |
| STORE_FAST | 880 | 19.0% |
| EXIT_INIT_CHECK | 620 | 13.4% |
| TO_BOOL_NONE | 180 | 3.9% |


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

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 400 | 64.5% |
| PUSH_NULL | 180 | 29.0% |
| CALL | 40 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 620 | 100.0% |


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
| LOAD_FAST | 1,960 | 86.0% |
| CALL_BUILTIN_CLASS | 180 | 7.9% |
| CALL | 140 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,080 | 47.4% |
| POP_TOP | 400 | 17.5% |
| LOAD_FAST | 400 | 17.5% |
| CALL_TUPLE_1 | 180 | 7.9% |
| TO_BOOL_BOOL | 180 | 7.9% |


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
| RESUME_CHECK | 2,960 | 24.6% |
| STORE_FAST | 2,680 | 22.3% |
| LOAD_FAST | 1,080 | 9.0% |
| POP_JUMP_IF_FALSE | 1,080 | 9.0% |
| LOAD_GLOBAL | 960 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 5,960 | 49.5% |
| LOAD_FAST | 1,680 | 14.0% |
| TO_BOOL_BOOL | 900 | 7.5% |
| LOAD_ATTR | 760 | 6.3% |
| CALL_PY_EXACT_ARGS | 540 | 4.5% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,900 | 29.8% |
| CACHE | 2,700 | 27.7% |
| COPY_FREE_VARS | 820 | 8.4% |
| CALL_PY_WITH_DEFAULTS | 800 | 8.2% |
| CALL_ALLOC_AND_ENTER_INIT | 620 | 6.4% |

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
| CALL_ISINSTANCE | 1,780 | 31.1% |
| LOAD_ATTR_INSTANCE_VALUE | 900 | 15.7% |
| LOAD_GLOBAL_MODULE | 900 | 15.7% |
| LOAD_FAST | 720 | 12.6% |
| TO_BOOL | 440 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,320 | 75.5% |
| POP_JUMP_IF_TRUE | 1,400 | 24.5% |


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

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> specialization stats for BINARY_OP_INPLACE_ADD_UNICODE family </summary>


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
|     deferred | 5,600 | 22.6% |
|          hit | 16,920 | 68.4% |
|         miss | 400 | 1.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,180 | 64.8% |
| Failure | 640 | 35.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 240 | 37.5% |
| code complex parameters | 200 | 31.2% |
| class no vectorcall | 80 | 12.5% |
| cfunc varargs | 40 | 6.2% |
| cfunc varargs keywords | 40 | 6.2% |
| meth descr varargs | 40 | 6.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 600 | 10.9% |
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
|     deferred | 480 | 48.0% |
|          hit | 480 | 48.0% |

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
|     deferred | 3,360 | 12.6% |
|          hit | 20,900 | 78.3% |
|         miss | 440 | 1.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,760 | 88.0% |
| Failure | 240 | 12.0% |

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
|     deferred | 1,580 | 6.5% |
|          hit | 20,500 | 84.5% |
|         miss | 660 | 2.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,520 | 100.0% |
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
|     deferred | 2,200 | 18.5% |
|          hit | 8,580 | 72.1% |
|         miss | 220 | 1.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 660 | 73.3% |
| Failure | 240 | 26.7% |

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
| Basic | 171,220 | 54.3% |
| Not specialized | 49,820 | 15.8% |
| Specialized hits | 92,200 | 29.3% |
| Specialized misses | 1,940 | 0.6% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 5,600 | 32.8% |
| LOAD_ATTR | 3,360 | 19.7% |
| TO_BOOL | 2,200 | 12.9% |
| LOAD_GLOBAL | 1,580 | 9.3% |
| BINARY_OP | 1,540 | 9.0% |
| STORE_ATTR | 1,400 | 8.2% |
| COMPARE_OP | 600 | 3.5% |
| FOR_ITER | 480 | 2.8% |
| UNPACK_SEQUENCE | 180 | 1.1% |
| BINARY_SUBSCR | 100 | 0.6% |


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
| CHECK_EXC_MATCH | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 3,600 | 33.2% |
| Calls to Python functions inlined | 7,240 | 66.8% |
| Calls via PyEval_EvalFrame (total) | 3,600 | 33.2% |
| Calls via PyEval_EvalFrame (vector) | 2,720 | 25.1% |
| Calls via PyEval_EvalFrame (generator) | 880 | 8.1% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,720 | 25.1% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 880 | 8.1% |
| Calls via PyEval_EvalFrame (api) | 440 | 4.1% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 440 | 4.1% |
| Frames pushed | 5,340 | 49.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 15,120 | 36.9% |
| Frees to freelist | 15,260 |  |
| Allocations | 25,860 | 63.1% |
| Allocations to 512 bytes | 24,980 | 61.0% |
| Allocations to 4 kbytes | 220 | 0.5% |
| Allocations over 4 kbytes | 660 | 1.6% |
| Frees | 25,461 |  |
| New values | 480 |  |
| Interpreter increfs | 113,020 | 66.1% |
| Interpreter decrefs | 133,200 | 64.8% |
| Increfs | 57,891 | 33.9% |
| Decrefs | 72,265 | 35.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 15,725 |  |
| Method cache misses | 1,455 |  |
| Method cache collisions | 1,772 |  |
| Method cache dunder hits | 5,979 |  |
| Method cache dunder misses | 781 |  |


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
