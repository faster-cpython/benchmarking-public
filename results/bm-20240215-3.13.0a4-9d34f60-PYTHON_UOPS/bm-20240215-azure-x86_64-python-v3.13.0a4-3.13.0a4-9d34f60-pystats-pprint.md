
# Pystats results

- benchmark: pprint
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 3,904,027,280 | 19.2% | 19.2% |  |
| STORE_FAST | 1,824,010,800 | 9.0% | 28.2% |  |
| LOAD_GLOBAL_BUILTIN | 1,680,009,460 | 8.3% | 36.4% |  |
| LOAD_CONST | 1,328,007,760 | 6.5% | 43.0% |  |
| POP_JUMP_IF_FALSE | 1,224,008,080 | 6.0% | 49.0% |  |
| TO_BOOL_BOOL | 1,056,004,800 | 5.2% | 54.2% |  |
| LOAD_FAST_LOAD_FAST | 1,008,008,880 | 5.0% | 59.1% |  |
| CALL_BUILTIN_FAST | 560,003,940 | 2.8% | 61.9% |  |
| RETURN_VALUE | 560,002,000 | 2.8% | 64.7% |  |
| POP_JUMP_IF_TRUE | 552,001,280 | 2.7% | 67.4% |  |
| RESUME_CHECK | 488,004,300 | 2.4% | 69.8% |  |
| CALL_BUILTIN_O | 448,002,040 | 2.2% | 72.0% |  |
| CALL_PY_EXACT_ARGS | 320,004,040 | 1.6% | 73.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 320,003,980 | 1.6% | 75.1% |  |
| LOAD_ATTR | 312,081,480 | 1.5% | 76.7% |  |
| BUILD_TUPLE | 288,000,880 | 1.4% | 78.1% |  |
| LOAD_GLOBAL_MODULE | 280,001,740 | 1.4% | 79.4% |  |
| POP_TOP | 272,002,320 | 1.3% | 80.8% |  |
| CONTAINS_OP | 256,002,320 | 1.3% | 82.0% |  |
| UNPACK_SEQUENCE_TUPLE | 240,000,660 | 1.2% | 83.2% |  |
| IS_OP | 216,000,880 | 1.1% | 84.3% |  |
| ENTER_EXECUTOR | 215,998,720 | 1.1% | 85.4% |  |
| PUSH_NULL | 208,001,760 | 1.0% | 86.4% |  |
| INTERPRETER_EXIT | 168,000,160 | 0.8% | 87.2% |  |
| CALL_TYPE_1 | 160,001,620 | 0.8% | 88.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 152,001,880 | 0.7% | 88.7% |  |
| FOR_ITER_LIST | 136,860,620 | 0.7% | 89.4% | 33.4% |
| LOAD_ATTR_METHOD_NO_DICT | 120,000,640 | 0.6% | 90.0% |  |
| EXTENDED_ARG | 120,000,160 | 0.6% | 90.6% |  |
| RETURN_CONST | 104,000,240 | 0.5% | 91.1% |  |
| CALL_METHOD_DESCRIPTOR_O | 104,000,180 | 0.5% | 91.6% |  |
| FOR_ITER_TUPLE | 96,863,760 | 0.5% | 92.1% | 47.2% |
| CALL | 96,027,540 | 0.5% | 92.6% |  |
| BINARY_OP | 96,025,120 | 0.5% | 93.0% |  |
| BINARY_OP_ADD_INT | 96,000,320 | 0.5% | 93.5% |  |
| DELETE_SUBSCR | 96,000,240 | 0.5% | 94.0% |  |
| GET_ITER | 96,000,160 | 0.5% | 94.5% |  |
| BUILD_LIST | 96,000,160 | 0.5% | 94.9% |  |
| STORE_SUBSCR_DICT | 96,000,140 | 0.5% | 95.4% |  |
| TO_BOOL_NONE | 96,000,080 | 0.5% | 95.9% |  |
| STORE_ATTR_SLOT | 95,999,960 | 0.5% | 96.3% |  |
| BINARY_SUBSCR_TUPLE_INT | 95,999,920 | 0.5% | 96.8% |  |
| COMPARE_OP_INT | 80,000,160 | 0.4% | 97.2% |  |
| TO_BOOL | 72,019,860 | 0.4% | 97.6% |  |
| CALL_LEN | 56,000,020 | 0.3% | 97.8% |  |
| COPY | 48,000,720 | 0.2% | 98.1% |  |
| FORMAT_SIMPLE | 48,000,640 | 0.2% | 98.3% |  |
| CONVERT_VALUE | 48,000,640 | 0.2% | 98.5% |  |
| JUMP_FORWARD | 48,000,240 | 0.2% | 98.8% |  |
| LOAD_ATTR_SLOT | 47,999,920 | 0.2% | 99.0% |  |
| STORE_FAST_STORE_FAST | 32,000,480 | 0.2% | 99.2% |  |
| NOP | 24,000,640 | 0.1% | 99.3% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,000,560 | 0.1% | 99.4% |  |
| BUILD_STRING | 24,000,320 | 0.1% | 99.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 24,000,280 | 0.1% | 99.6% |  |
| TO_BOOL_LIST | 24,000,120 | 0.1% | 99.8% |  |
| CALL_KW | 24,000,000 | 0.1% | 99.9% |  |
| BINARY_OP_SUBTRACT_INT | 16,000,300 | 0.1% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 8,000,160 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 2,560 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,700 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 360 | 0.0% | 100.0% |  |
| RESUME | 340 | 0.0% | 100.0% |  |
| COMPARE_OP | 320 | 0.0% | 100.0% |  |
| LOAD_DEREF | 320 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 240 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 200 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 160 | 0.0% | 100.0% |  |
| FOR_ITER | 160 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 120 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NONE | 80 | 0.0% | 100.0% |  |
| STORE_ATTR | 80 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 80 | 0.0% | 100.0% |  |
| POP_EXCEPT | 80 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 80 | 0.0% | 100.0% |  |
| BUILD_MAP | 80 | 0.0% | 100.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 80 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 60 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 1,040,006,800 | 5.1% | 5.1% |
| STORE_FAST LOAD_FAST | 928,005,520 | 4.6% | 9.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 640,002,240 | 3.1% | 12.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 536,002,680 | 2.6% | 15.5% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 528,003,940 | 2.6% | 18.1% |
| STORE_FAST STORE_FAST | 464,001,440 | 2.3% | 20.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 448,003,200 | 2.2% | 22.5% |
| LOAD_FAST TO_BOOL_BOOL | 440,001,000 | 2.2% | 24.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 432,000,740 | 2.1% | 26.8% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 424,001,680 | 2.1% | 28.9% |
| LOAD_GLOBAL_BUILTIN CALL_BUILTIN_FAST | 424,001,680 | 2.1% | 31.0% |
| LOAD_FAST CALL_BUILTIN_O | 424,001,520 | 2.1% | 33.1% |
| LOAD_FAST LOAD_CONST | 400,002,160 | 2.0% | 35.1% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 320,004,040 | 1.6% | 36.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 320,003,720 | 1.6% | 38.2% |
| LOAD_CONST LOAD_CONST | 304,002,480 | 1.5% | 39.7% |
| BUILD_TUPLE RETURN_VALUE | 288,000,880 | 1.4% | 41.1% |
| POP_TOP LOAD_FAST | 264,001,920 | 1.3% | 42.4% |
| LOAD_CONST STORE_FAST | 264,000,720 | 1.3% | 43.7% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 256,002,320 | 1.3% | 45.0% |
| RETURN_VALUE RETURN_VALUE | 240,000,800 | 1.2% | 46.2% |
| RETURN_VALUE UNPACK_SEQUENCE_TUPLE | 240,000,520 | 1.2% | 47.3% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST | 232,000,600 | 1.1% | 48.5% |
| LOAD_ATTR IS_OP | 216,000,880 | 1.1% | 49.5% |
| LOAD_GLOBAL_BUILTIN LOAD_ATTR | 216,000,720 | 1.1% | 50.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 216,000,560 | 1.1% | 51.7% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 215,998,620 | 1.1% | 52.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 208,003,700 | 1.0% | 53.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 208,002,400 | 1.0% | 54.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 208,002,400 | 1.0% | 55.8% |
| LOAD_FAST PUSH_NULL | 208,001,440 | 1.0% | 56.8% |
| PUSH_NULL LOAD_FAST | 208,001,040 | 1.0% | 57.8% |
| CALL_BUILTIN_O POP_TOP | 208,000,780 | 1.0% | 58.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 192,001,520 | 0.9% | 59.8% |
| IS_OP POP_JUMP_IF_FALSE | 168,000,720 | 0.8% | 60.6% |
| CACHE RESUME_CHECK | 168,000,000 | 0.8% | 61.5% |
| RESUME_CHECK LOAD_FAST | 160,002,140 | 0.8% | 62.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 160,002,040 | 0.8% | 63.0% |
| LOAD_FAST CALL_TYPE_1 | 160,001,560 | 0.8% | 63.8% |
| CALL_TYPE_1 STORE_FAST | 160,001,560 | 0.8% | 64.6% |
| LOAD_GLOBAL_MODULE CONTAINS_OP | 160,001,560 | 0.8% | 65.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 160,001,520 | 0.8% | 66.2% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 152,001,640 | 0.7% | 66.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 144,001,000 | 0.7% | 67.6% |
| LOAD_CONST BUILD_TUPLE | 144,000,720 | 0.7% | 68.4% |
| CALL_BUILTIN_O LOAD_CONST | 144,000,640 | 0.7% | 69.1% |
| CALL_BUILTIN_FAST STORE_FAST | 136,002,060 | 0.7% | 69.7% |
| LOAD_CONST CALL_BUILTIN_FAST | 136,001,520 | 0.7% | 70.4% |
| EXTENDED_ARG POP_JUMP_IF_FALSE | 120,000,160 | 0.6% | 71.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 112,001,440 | 0.6% | 71.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 112,001,280 | 0.6% | 72.1% |
| LOAD_FAST LOAD_FAST_LOAD_FAST | 112,000,320 | 0.6% | 72.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 112,000,280 | 0.6% | 73.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 103,999,960 | 0.5% | 73.7% |
| LOAD_FAST LOAD_ATTR | 96,001,560 | 0.5% | 74.2% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 96,000,720 | 0.5% | 74.6% |
| LOAD_CONST LOAD_FAST_LOAD_FAST | 96,000,640 | 0.5% | 75.1% |
| POP_JUMP_IF_FALSE LOAD_CONST | 96,000,640 | 0.5% | 75.6% |
| CALL_BUILTIN_O STORE_FAST | 96,000,620 | 0.5% | 76.1% |
| STORE_FAST LOAD_CONST | 96,000,320 | 0.5% | 76.5% |
| LOAD_ATTR STORE_FAST | 96,000,280 | 0.5% | 77.0% |
| LOAD_FAST_LOAD_FAST DELETE_SUBSCR | 96,000,240 | 0.5% | 77.5% |
| BINARY_OP LOAD_FAST_LOAD_FAST | 96,000,180 | 0.5% | 78.0% |
| BUILD_LIST STORE_FAST | 96,000,160 | 0.5% | 78.4% |
| LOAD_FAST GET_ITER | 96,000,160 | 0.5% | 78.9% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 96,000,160 | 0.5% | 79.4% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 96,000,160 | 0.5% | 79.8% |
| STORE_FAST BUILD_LIST | 96,000,160 | 0.5% | 80.3% |
| BINARY_OP_ADD_INT STORE_FAST | 96,000,140 | 0.5% | 80.8% |
| LOAD_CONST BINARY_OP_ADD_INT | 96,000,120 | 0.5% | 81.3% |
| TO_BOOL_BOOL EXTENDED_ARG | 96,000,120 | 0.5% | 81.7% |
| CALL_METHOD_DESCRIPTOR_O BINARY_OP | 96,000,080 | 0.5% | 82.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 96,000,080 | 0.5% | 82.7% |
| STORE_SUBSCR_DICT LOAD_CONST | 96,000,080 | 0.5% | 83.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 96,000,080 | 0.5% | 83.6% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_DICT | 96,000,040 | 0.5% | 84.1% |
| LOAD_CONST LOAD_ATTR_METHOD_NO_DICT | 96,000,000 | 0.5% | 84.6% |
| LOAD_FAST TO_BOOL_NONE | 96,000,000 | 0.5% | 85.0% |
| RETURN_CONST INTERPRETER_EXIT | 96,000,000 | 0.5% | 85.5% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 95,999,960 | 0.5% | 86.0% |
| STORE_ATTR_SLOT RETURN_CONST | 95,999,960 | 0.5% | 86.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 95,999,920 | 0.5% | 86.9% |
| BINARY_SUBSCR_TUPLE_INT CALL | 95,999,920 | 0.5% | 87.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 95,999,920 | 0.5% | 87.9% |
| LOAD_CONST BINARY_SUBSCR_TUPLE_INT | 95,999,840 | 0.5% | 88.3% |
| ENTER_EXECUTOR LOAD_GLOBAL_BUILTIN | 79,999,280 | 0.4% | 88.7% |
| ENTER_EXECUTOR FOR_ITER_LIST | 78,085,140 | 0.4% | 89.1% |
| LOAD_FAST TO_BOOL | 72,000,760 | 0.4% | 89.5% |
| TO_BOOL POP_JUMP_IF_TRUE | 72,000,260 | 0.4% | 89.8% |
| DELETE_SUBSCR LOAD_FAST | 72,000,160 | 0.4% | 90.2% |
| RETURN_VALUE INTERPRETER_EXIT | 72,000,160 | 0.4% | 90.5% |
| POP_JUMP_IF_TRUE LOAD_CONST | 72,000,160 | 0.4% | 90.9% |
| FOR_ITER_TUPLE STORE_FAST | 58,172,940 | 0.3% | 91.2% |
| FOR_ITER_LIST LOAD_FAST_LOAD_FAST | 58,171,180 | 0.3% | 91.5% |
| ENTER_EXECUTOR FOR_ITER_TUPLE | 57,914,220 | 0.3% | 91.7% |
| GET_ITER FOR_ITER_LIST | 57,913,000 | 0.3% | 92.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 56,000,200 | 0.3% | 92.3% |
| LOAD_FAST CALL_LEN | 55,999,960 | 0.3% | 92.6% |
| FOR_ITER_LIST STORE_FAST | 53,827,340 | 0.3% | 92.8% |
| POP_JUMP_IF_FALSE POP_TOP | 48,000,720 | 0.2% | 93.1% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 168,000,000 | 100.0% |
| RESUME | 160 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 50.0% |
| BINARY_SUBSCR_TUPLE_INT | 80 | 50.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 96,000,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,000,160 | 75.0% |
| LOAD_CONST | 24,000,000 | 25.0% |
| RETURN_CONST | 80 | 0.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 48,000,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 24,000,320 | 50.0% |
| LOAD_CONST | 24,000,320 | 50.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,000,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 57,913,000 | 60.3% |
| FOR_ITER_TUPLE | 38,087,040 | 39.7% |
| FOR_ITER | 120 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 96,000,000 | 57.1% |
| RETURN_VALUE | 72,000,160 | 42.9% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 23,999,960 | 100.0% |
| STORE_FAST | 480 | 0.0% |
| POP_TOP | 160 | 0.0% |
| RESUME | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,000,000 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 400 | 0.0% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 208,000,780 | 76.5% |
| POP_JUMP_IF_FALSE | 48,000,720 | 17.6% |
| RETURN_CONST | 8,000,240 | 2.9% |
| CALL_METHOD_DESCRIPTOR_O | 8,000,100 | 2.9% |
| CALL | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 264,001,920 | 97.1% |
| RETURN_CONST | 8,000,080 | 2.9% |
| NOP | 160 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 208,001,440 | 100.0% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 208,001,040 | 100.0% |
| CALL | 640 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 288,000,880 | 51.4% |
| RETURN_VALUE | 240,000,800 | 42.9% |
| COMPARE_OP_INT | 23,999,960 | 4.3% |
| LOAD_FAST | 8,000,240 | 1.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 240,000,800 | 42.9% |
| UNPACK_SEQUENCE_TUPLE | 240,000,520 | 42.9% |
| INTERPRETER_EXIT | 72,000,160 | 12.9% |
| STORE_FAST | 8,000,080 | 1.4% |
| UNPACK_SEQUENCE | 280 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 100 | 50.0% |
| LOAD_CONST | 80 | 40.0% |
| LOAD_FAST | 20 | 10.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,000,760 | 100.0% |
| TO_BOOL | 18,340 | 0.0% |
| CALL | 200 | 0.0% |
| CALL_BUILTIN_FAST | 200 | 0.0% |
| COPY | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 72,000,260 | 100.0% |
| TO_BOOL | 18,340 | 0.0% |
| TO_BOOL_BOOL | 640 | 0.0% |
| POP_JUMP_IF_FALSE | 460 | 0.0% |
| TO_BOOL_NONE | 80 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 96,000,080 | 100.0% |
| BINARY_OP | 24,280 | 0.0% |
| LOAD_CONST | 280 | 0.0% |
| LOAD_FAST | 280 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 96,000,180 | 100.0% |
| BINARY_OP | 24,280 | 0.0% |
| STORE_FAST | 220 | 0.0% |
| BINARY_OP_ADD_INT | 160 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 100 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,000,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,000,160 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 24,000,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 24,000,240 | 100.0% |
| CALL | 80 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 144,000,720 | 50.0% |
| LOAD_FAST_LOAD_FAST | 96,000,160 | 33.3% |
| CALL | 48,000,000 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 288,000,880 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 95,999,920 | 100.0% |
| CALL | 24,380 | 0.0% |
| LOAD_FAST | 1,200 | 0.0% |
| PUSH_NULL | 640 | 0.0% |
| LOAD_FAST_LOAD_FAST | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 48,000,000 | 50.0% |
| LOAD_GLOBAL_MODULE | 47,999,920 | 50.0% |
| CALL | 24,380 | 0.0% |
| STORE_FAST | 500 | 0.0% |
| POP_TOP | 480 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 160 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,000,000 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 62.5% |
| LOAD_ATTR | 40 | 12.5% |
| LOAD_FAST | 40 | 12.5% |
| LOAD_ATTR_SLOT | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 160 | 50.0% |
| POP_JUMP_IF_FALSE | 120 | 37.5% |
| RETURN_VALUE | 40 | 12.5% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160,001,560 | 62.5% |
| LOAD_FAST_LOAD_FAST | 96,000,720 | 37.5% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 256,002,320 | 100.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,000,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 48,000,640 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,000,640 | 100.0% |
| BINARY_OP_ADD_INT | 60 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 48,000,480 | 100.0% |
| TO_BOOL | 160 | 0.0% |
| STORE_FAST_STORE_FAST | 80 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 120 | 75.0% |
| RESUME | 40 | 25.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 215,998,620 | 100.0% |
| JUMP_BACKWARD | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 79,999,280 | 37.0% |
| FOR_ITER_LIST | 78,085,140 | 36.2% |
| FOR_ITER_TUPLE | 57,914,220 | 26.8% |
| PUSH_EXC_INFO | 80 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 96,000,120 | 80.0% |
| IS_OP | 24,000,000 | 20.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 120,000,160 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 120 | 75.0% |
| JUMP_BACKWARD | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 25.0% |
| UNPACK_SEQUENCE | 40 | 25.0% |
| FOR_ITER_LIST | 40 | 25.0% |
| FOR_ITER_TUPLE | 40 | 25.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,000,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 168,000,720 | 77.8% |
| POP_JUMP_IF_TRUE | 24,000,160 | 11.1% |
| EXTENDED_ARG | 24,000,000 | 11.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,700 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 640 | 37.6% |
| FOR_ITER_LIST | 600 | 35.3% |
| LOAD_FAST | 320 | 18.8% |
| ENTER_EXECUTOR | 100 | 5.9% |
| FOR_ITER | 40 | 2.4% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 48,000,160 | 100.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 24,000,120 | 50.0% |
| LOAD_FAST | 24,000,000 | 50.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 216,000,720 | 69.2% |
| LOAD_FAST | 96,001,560 | 30.8% |
| LOAD_ATTR | 78,540 | 0.0% |
| LOAD_GLOBAL | 240 | 0.0% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 216,000,880 | 69.2% |
| STORE_FAST | 96,000,280 | 30.8% |
| LOAD_ATTR | 78,540 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 260 | 0.0% |
| LOAD_FAST | 240 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400,002,160 | 30.1% |
| LOAD_CONST | 304,002,480 | 22.9% |
| CALL_BUILTIN_O | 144,000,640 | 10.8% |
| POP_JUMP_IF_FALSE | 96,000,640 | 7.2% |
| STORE_FAST | 96,000,320 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 304,002,480 | 22.9% |
| STORE_FAST | 264,000,720 | 19.9% |
| BUILD_TUPLE | 144,000,720 | 10.8% |
| CALL_BUILTIN_FAST | 136,001,520 | 10.2% |
| LOAD_FAST_LOAD_FAST | 96,000,640 | 7.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 160 | 50.0% |
| STORE_FAST | 160 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 160 | 50.0% |
| STORE_FAST | 160 | 50.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,040,006,800 | 26.6% |
| STORE_FAST | 928,005,520 | 23.8% |
| POP_JUMP_IF_FALSE | 448,003,200 | 11.5% |
| POP_TOP | 264,001,920 | 6.8% |
| POP_JUMP_IF_TRUE | 216,000,560 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 640,002,240 | 16.4% |
| TO_BOOL_BOOL | 440,001,000 | 11.3% |
| CALL_BUILTIN_O | 424,001,520 | 10.9% |
| LOAD_CONST | 400,002,160 | 10.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 320,003,720 | 8.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 208,003,700 | 20.6% |
| LOAD_FAST_LOAD_FAST | 208,002,400 | 20.6% |
| LOAD_FAST | 112,000,320 | 11.1% |
| LOAD_CONST | 96,000,640 | 9.5% |
| BINARY_OP | 96,000,180 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 208,002,400 | 20.6% |
| CALL_PY_EXACT_ARGS | 208,002,400 | 20.6% |
| LOAD_FAST | 112,001,440 | 11.1% |
| CONTAINS_OP | 96,000,720 | 9.5% |
| DELETE_SUBSCR | 96,000,240 | 9.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 800 | 31.2% |
| POP_JUMP_IF_FALSE | 680 | 26.6% |
| STORE_FAST | 160 | 6.2% |
| RESUME | 160 | 6.2% |
| RESUME_CHECK | 160 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,020 | 39.8% |
| LOAD_FAST | 720 | 28.1% |
| LOAD_GLOBAL_MODULE | 260 | 10.2% |
| LOAD_ATTR | 240 | 9.4% |
| CALL | 220 | 8.6% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 528,003,940 | 43.1% |
| CONTAINS_OP | 256,002,320 | 20.9% |
| IS_OP | 168,000,720 | 13.7% |
| EXTENDED_ARG | 120,000,160 | 9.8% |
| TO_BOOL_NONE | 96,000,080 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 536,002,680 | 43.8% |
| LOAD_FAST | 448,003,200 | 36.6% |
| LOAD_CONST | 96,000,640 | 7.8% |
| LOAD_FAST_LOAD_FAST | 96,000,160 | 7.8% |
| POP_TOP | 48,000,720 | 3.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 432,000,740 | 78.3% |
| TO_BOOL | 72,000,260 | 13.0% |
| IS_OP | 24,000,160 | 4.3% |
| TO_BOOL_LIST | 24,000,120 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 216,000,560 | 39.1% |
| ENTER_EXECUTOR | 215,998,620 | 39.1% |
| LOAD_CONST | 72,000,160 | 13.0% |
| LOAD_GLOBAL_BUILTIN | 48,000,040 | 8.7% |
| JUMP_BACKWARD | 1,700 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 95,999,960 | 92.3% |
| POP_TOP | 8,000,080 | 7.7% |
| DELETE_SUBSCR | 80 | 0.0% |
| POP_JUMP_IF_TRUE | 80 | 0.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 96,000,000 | 92.3% |
| POP_TOP | 8,000,240 | 7.7% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 40 | 50.0% |
| STORE_ATTR_SLOT | 40 | 50.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 464,001,440 | 25.4% |
| LOAD_CONST | 264,000,720 | 14.5% |
| UNPACK_SEQUENCE_TUPLE | 232,000,600 | 12.7% |
| CALL_TYPE_1 | 160,001,560 | 8.8% |
| CALL_BUILTIN_FAST | 136,002,060 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 928,005,520 | 50.9% |
| STORE_FAST | 464,001,440 | 25.4% |
| LOAD_GLOBAL_BUILTIN | 192,001,520 | 10.5% |
| LOAD_CONST | 96,000,320 | 5.3% |
| BUILD_LIST | 96,000,160 | 5.3% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 24,000,280 | 75.0% |
| UNPACK_SEQUENCE_TUPLE | 8,000,060 | 25.0% |
| COPY | 80 | 0.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,000,320 | 75.0% |
| STORE_FAST | 8,000,080 | 25.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 280 | 77.8% |
| FOR_ITER | 40 | 11.1% |
| FOR_ITER_LIST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 140 | 38.9% |
| STORE_FAST | 120 | 33.3% |
| STORE_FAST_STORE_FAST | 60 | 16.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 40 | 11.1% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 160 | 47.1% |
| CALL | 140 | 41.2% |
| COPY_FREE_VARS | 40 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 160 | 47.1% |
| LOAD_FAST | 100 | 29.4% |
| NOP | 40 | 11.8% |
| LOAD_FAST_LOAD_FAST | 40 | 11.8% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 96,000,120 | 100.0% |
| BINARY_OP | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,000,140 | 100.0% |
| COPY | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 66.7% |
| BINARY_OP | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 95,999,840 | 100.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 95,999,920 | 100.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 424,001,680 | 75.7% |
| LOAD_CONST | 136,001,520 | 24.3% |
| LOAD_FAST | 440 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 424,001,680 | 75.7% |
| STORE_FAST | 136,002,060 | 24.3% |
| TO_BOOL | 200 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 424,001,520 | 94.6% |
| BUILD_STRING | 24,000,240 | 5.4% |
| CALL | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 208,000,780 | 46.4% |
| LOAD_CONST | 144,000,640 | 32.1% |
| STORE_FAST | 96,000,620 | 21.4% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,999,960 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 47,999,960 | 85.7% |
| LOAD_FAST | 8,000,060 | 14.3% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 24,000,440 | 100.0% |
| CALL | 80 | 0.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 23,999,920 | 100.0% |
| LOAD_FAST | 540 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 103,999,960 | 100.0% |
| CALL | 140 | 0.0% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 96,000,080 | 92.3% |
| POP_TOP | 8,000,100 | 7.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 208,002,400 | 65.0% |
| LOAD_FAST | 112,001,280 | 35.0% |
| CALL | 280 | 0.0% |
| LOAD_CONST | 40 | 0.0% |
| BINARY_OP_ADD_INT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 320,004,040 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160,001,560 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160,001,560 | 100.0% |
| LOAD_ATTR | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,000,040 | 60.0% |
| LOAD_ATTR_SLOT | 23,999,920 | 30.0% |
| LOAD_FAST | 8,000,040 | 10.0% |
| COMPARE_OP | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 56,000,200 | 70.0% |
| RETURN_VALUE | 23,999,960 | 30.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 78,085,140 | 57.1% |
| GET_ITER | 57,913,000 | 42.3% |
| FOR_ITER_TUPLE | 861,840 | 0.6% |
| JUMP_BACKWARD | 600 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 58,171,180 | 42.5% |
| STORE_FAST | 53,827,340 | 39.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 24,000,240 | 17.5% |
| FOR_ITER_TUPLE | 861,820 | 0.6% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 57,914,220 | 59.8% |
| GET_ITER | 38,087,040 | 39.3% |
| FOR_ITER_LIST | 861,820 | 0.9% |
| JUMP_BACKWARD | 640 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 58,172,940 | 60.1% |
| LOAD_FAST_LOAD_FAST | 37,828,980 | 39.1% |
| FOR_ITER_LIST | 861,840 | 0.9% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 152,001,640 | 100.0% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 144,001,000 | 94.7% |
| LOAD_FAST | 8,000,660 | 5.3% |
| TO_BOOL | 100 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| BINARY_OP_ADD_INT | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 96,000,000 | 80.0% |
| LOAD_FAST | 23,999,920 | 20.0% |
| LOAD_FAST_LOAD_FAST | 520 | 0.0% |
| LOAD_ATTR | 160 | 0.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,000,080 | 80.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,000,440 | 20.0% |
| CALL | 60 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,003,720 | 100.0% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 208,003,700 | 65.0% |
| LOAD_FAST | 112,000,280 | 35.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160 | 66.7% |
| LOAD_ATTR | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 120 | 50.0% |
| STORE_FAST | 120 | 50.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,999,840 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,999,960 | 50.0% |
| COMPARE_OP_INT | 23,999,920 | 50.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640,002,240 | 38.1% |
| POP_JUMP_IF_FALSE | 536,002,680 | 31.9% |
| STORE_FAST | 192,001,520 | 11.4% |
| RESUME_CHECK | 160,002,040 | 9.5% |
| ENTER_EXECUTOR | 79,999,280 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,040,006,800 | 61.9% |
| CALL_BUILTIN_FAST | 424,001,680 | 25.2% |
| LOAD_ATTR | 216,000,720 | 12.9% |
| CALL | 200 | 0.0% |
| CHECK_EXC_MATCH | 60 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160,001,520 | 57.1% |
| RESUME_CHECK | 48,000,040 | 17.1% |
| CALL | 47,999,920 | 17.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 23,999,920 | 8.6% |
| LOAD_GLOBAL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 160,001,560 | 57.1% |
| LOAD_FAST | 95,999,920 | 34.3% |
| LOAD_CONST | 23,999,960 | 8.6% |
| LOAD_ATTR_MODULE | 160 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 320,004,040 | 65.6% |
| CACHE | 168,000,000 | 34.4% |
| CALL | 140 | 0.0% |
| COPY_FREE_VARS | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160,002,140 | 32.8% |
| LOAD_GLOBAL_BUILTIN | 160,002,040 | 32.8% |
| LOAD_FAST_LOAD_FAST | 95,999,960 | 19.7% |
| LOAD_GLOBAL_MODULE | 48,000,040 | 9.8% |
| NOP | 23,999,960 | 4.9% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 95,999,920 | 100.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 95,999,960 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 96,000,040 | 100.0% |
| STORE_SUBSCR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 96,000,080 | 100.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440,001,000 | 41.7% |
| CALL_BUILTIN_FAST | 424,001,680 | 40.2% |
| LOAD_ATTR_INSTANCE_VALUE | 144,001,000 | 13.6% |
| COPY | 48,000,480 | 4.5% |
| TO_BOOL | 640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 528,003,940 | 50.0% |
| POP_JUMP_IF_TRUE | 432,000,740 | 40.9% |
| EXTENDED_ARG | 96,000,120 | 9.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,000,080 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 24,000,120 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 96,000,000 | 100.0% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 96,000,080 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 240,000,520 | 100.0% |
| UNPACK_SEQUENCE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 232,000,600 | 96.7% |
| STORE_FAST_STORE_FAST | 8,000,060 | 3.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 24,000,240 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 24,000,280 | 100.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 60 | 75.0% |
| LOAD_GLOBAL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 100.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 80 | 100.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 50.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,000,120 | 100.0% |
| BINARY_OP | 100 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,000,180 | 50.0% |
| LOAD_FAST | 8,000,060 | 50.0% |
| LOAD_CONST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,000,080 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,999,980 | 100.0% |
| LOAD_CONST | 120 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| LOAD_ATTR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 40 | 66.7% |
| LOAD_ATTR | 20 | 33.3% |


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
|     deferred | 96,000,560 | 46.1% |
|          hit | 112,000,800 | 53.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 1.3% |
| Failure | 24,240 | 98.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| remainder | 24,220 | 99.9% |
| multiply different types | 20 | 0.1% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 95,999,920 | 100.0% |

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
|     deferred | 96,001,940 | 3.6% |
|          hit | 2,600,001,340 | 96.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,220 | 4.8% |
| Failure | 24,380 | 95.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| no dict | 24,200 | 99.3% |
| cfunc noargs | 120 | 0.5% |
| other | 40 | 0.2% |
| class no vectorcall | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 160 | 0.0% |
|          hit | 80,000,160 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 89,631,320 | 38.3% |
|          hit | 142,369,480 | 60.9% |
|         miss | 91,354,900 | 39.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,723,740 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 312,002,080 | 22.7% |
|          hit | 1,064,000,880 | 77.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 880 | 1.1% |
| Failure | 78,520 | 98.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 54,280 | 69.1% |
| method | 24,240 | 30.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,280 | 0.0% |
|          hit | 1,960,011,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,280 | 100.0% |
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

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 95,999,960 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 96,000,140 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 72,000,760 | 4.4% |
|          hit | 1,560,000,440 | 95.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 4.0% |
| Failure | 18,340 | 96.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 12,100 | 66.0% |
| dict | 6,240 | 34.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 0.0% |
|          hit | 359,999,900 | 100.0% |

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
| Basic | 11,056,071,480 | 54.4% |
| Not specialized | 2,352,167,280 | 11.6% |
| Specialized hits | 6,830,411,240 | 33.6% |
| Specialized misses | 91,354,900 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 312,002,080 | 46.9% |
| CALL | 96,001,940 | 14.4% |
| BINARY_OP | 96,000,560 | 14.4% |
| FOR_ITER | 89,631,320 | 13.5% |
| TO_BOOL | 72,000,760 | 10.8% |
| LOAD_GLOBAL | 1,280 | 0.0% |
| UNPACK_SEQUENCE | 180 | 0.0% |
| COMPARE_OP | 160 | 0.0% |
| STORE_SUBSCR | 100 | 0.0% |
| BINARY_SUBSCR | 80 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| FOR_ITER_TUPLE | 45,678,260 | 50.0% |
| FOR_ITER_LIST | 45,676,640 | 50.0% |
| CACHE | 0 | 0.0% |
| DELETE_SUBSCR | 0 | 0.0% |
| FORMAT_SIMPLE | 0 | 0.0% |
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
| Calls to PyEval_EvalDefault | 168,000,160 | 20.8% |
| Calls to Python functions inlined | 640,000,640 | 79.2% |
| Calls via PyEval_EvalFrame (total) | 168,000,160 | 20.8% |
| Calls via PyEval_EvalFrame (vector) | 168,000,160 | 20.8% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 168,000,160 | 20.8% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 24,000,000 | 3.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 48,000,000 | 5.9% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 80 | 0.0% |
| Frames pushed | 808,000,800 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 728,000,800 | 38.7% |
| Frees to freelist | 728,000,680 |  |
| Allocations | 1,152,002,260 | 61.3% |
| Allocations to 512 bytes | 1,152,001,920 | 61.3% |
| Allocations to 4 kbytes | 100 | 0.0% |
| Allocations over 4 kbytes | 240 | 0.0% |
| Frees | 1,248,002,284 |  |
| New values | 0 |  |
| Interpreter increfs | 6,152,195,260 | 51.1% |
| Interpreter decrefs | 8,965,389,220 | 64.6% |
| Increfs | 5,879,820,132 | 48.9% |
| Decrefs | 4,906,628,741 | 35.4% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 120,025,906 |  |
| Method cache misses | 334 |  |
| Method cache collisions | 337 |  |
| Method cache dunder hits | 1,320,054,944 |  |
| Method cache dunder misses | 136 |  |


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
| Optimization attempts | 100 |  |
| Traces created | 100 | 100.0% |
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
| <= 128 | 0 | 0.0% |
| <= 256 | 40 | 40.0% |
| <= 512 | 60 | 60.0% |


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
| <= 128 | 40 | 40.0% |
| <= 256 | 60 | 60.0% |


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
| Number of data files | 40 |


</details>

---
Stats gathered on: 2024-09-10
