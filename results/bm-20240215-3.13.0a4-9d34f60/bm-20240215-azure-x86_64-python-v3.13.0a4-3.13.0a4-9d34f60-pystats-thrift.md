
# Pystats results

- benchmark: thrift
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 91,171,920 | 18.6% | 18.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 43,008,280 | 8.8% | 27.4% |  |
| LOAD_FAST_LOAD_FAST | 29,707,320 | 6.1% | 33.5% |  |
| LOAD_CONST | 28,683,900 | 5.9% | 39.3% |  |
| RESUME_CHECK | 28,673,160 | 5.9% | 45.2% |  |
| LOAD_GLOBAL_MODULE | 21,526,180 | 4.4% | 49.6% | 0.0% |
| RETURN_CONST | 19,456,720 | 4.0% | 53.5% |  |
| STORE_FAST | 18,474,400 | 3.8% | 57.3% |  |
| INTERPRETER_EXIT | 17,408,460 | 3.6% | 60.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 16,384,900 | 3.3% | 64.2% |  |
| LOAD_ATTR_MODULE | 14,357,360 | 2.9% | 67.1% | 0.0% |
| POP_TOP | 12,289,100 | 2.5% | 69.7% |  |
| CALL | 11,291,660 | 2.3% | 72.0% |  |
| PUSH_NULL | 11,285,060 | 2.3% | 74.3% |  |
| CALL_PY_EXACT_ARGS | 11,264,320 | 2.3% | 76.6% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 9,226,700 | 1.9% | 78.4% | 0.0% |
| RETURN_VALUE | 9,216,900 | 1.9% | 80.3% |  |
| POP_JUMP_IF_FALSE | 7,168,640 | 1.5% | 81.8% |  |
| LOAD_ATTR_METHOD_NO_DICT | 6,154,640 | 1.3% | 83.0% |  |
| POP_JUMP_IF_NONE | 6,144,140 | 1.3% | 84.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 6,144,100 | 1.3% | 85.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,144,020 | 1.3% | 86.8% | 0.0% |
| TO_BOOL_BOOL | 5,120,340 | 1.0% | 87.9% |  |
| FOR_ITER_TUPLE | 4,096,060 | 0.8% | 88.7% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 4,095,920 | 0.8% | 89.5% |  |
| JUMP_BACKWARD | 3,082,340 | 0.6% | 90.2% |  |
| BUILD_LIST | 3,072,300 | 0.6% | 90.8% |  |
| BUILD_MAP | 3,072,080 | 0.6% | 91.4% |  |
| CALL_ISINSTANCE | 3,072,000 | 0.6% | 92.0% |  |
| GET_ITER | 2,058,400 | 0.4% | 92.5% |  |
| LOAD_ATTR | 2,050,860 | 0.4% | 92.9% |  |
| NOP | 2,048,660 | 0.4% | 93.3% |  |
| POP_JUMP_IF_TRUE | 2,048,420 | 0.4% | 93.7% |  |
| CALL_FUNCTION_EX | 2,048,240 | 0.4% | 94.1% |  |
| CALL_BUILTIN_FAST | 2,048,200 | 0.4% | 94.6% |  |
| COPY_FREE_VARS | 2,048,140 | 0.4% | 95.0% |  |
| LOAD_ATTR_SLOT | 2,048,100 | 0.4% | 95.4% |  |
| DICT_MERGE | 2,048,080 | 0.4% | 95.8% |  |
| CALL_KW | 2,048,060 | 0.4% | 96.2% |  |
| COMPARE_OP_STR | 2,048,020 | 0.4% | 96.6% |  |
| TO_BOOL_INT | 2,048,020 | 0.4% | 97.1% |  |
| IMPORT_FROM | 2,048,000 | 0.4% | 97.5% |  |
| IMPORT_NAME | 2,048,000 | 0.4% | 97.9% |  |
| LOAD_SUPER_ATTR_ATTR | 2,047,980 | 0.4% | 98.3% |  |
| LOAD_ATTR_CLASS | 2,047,960 | 0.4% | 98.7% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 2,047,960 | 0.4% | 99.1% |  |
| FOR_ITER_RANGE | 1,044,520 | 0.2% | 99.4% |  |
| CALL_METHOD_DESCRIPTOR_O | 1,024,100 | 0.2% | 99.6% | 0.0% |
| JUMP_FORWARD | 1,024,020 | 0.2% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,023,980 | 0.2% | 100.0% |  |
| CALL_LIST_APPEND | 10,340 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 10,280 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 10,220 | 0.0% | 100.0% | 0.6% |
| BINARY_OP_SUBTRACT_FLOAT | 10,220 | 0.0% | 100.0% |  |
| STORE_ATTR | 1,140 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 1,120 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NOT_NONE | 580 | 0.0% | 100.0% |  |
| RESUME | 400 | 0.0% | 100.0% |  |
| LOAD_DEREF | 300 | 0.0% | 100.0% |  |
| BEFORE_WITH | 160 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 140 | 0.0% | 100.0% | 71.4% |
| SWAP | 140 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 140 | 0.0% | 100.0% |  |
| CONTAINS_OP | 120 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 120 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 120 | 0.0% | 100.0% |  |
| TO_BOOL | 100 | 0.0% | 100.0% |  |
| BINARY_OP | 100 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 100 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 100 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 100 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 100 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 80 | 0.0% | 100.0% | 25.0% |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| FOR_ITER | 80 | 0.0% | 100.0% |  |
| IS_OP | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 80 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 0.0% | 100.0% |  |
| TO_BOOL_NONE | 60 | 0.0% | 100.0% | 66.7% |
| EXIT_INIT_CHECK | 60 | 0.0% | 100.0% |  |
| COMPARE_OP | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |
| CALL_LEN | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 60 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 40 | 0.0% | 100.0% |  |
| FORMAT_SIMPLE | 40 | 0.0% | 100.0% |  |
| POP_EXCEPT | 40 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 40 | 0.0% | 100.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 40 | 0.0% | 100.0% |  |
| LIST_APPEND | 40 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 40 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 40 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 40 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 40 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 40 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 20 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 20 | 0.0% | 100.0% |  |
| BUILD_STRING | 20 | 0.0% | 100.0% |  |
| COPY | 20 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 20 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 20 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 20 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 20 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 20 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 22,527,700 | 4.6% | 4.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 20,480,040 | 4.2% | 8.8% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 16,384,620 | 3.3% | 12.1% |
| CACHE RESUME_CHECK | 15,360,260 | 3.1% | 15.3% |
| RETURN_CONST INTERPRETER_EXIT | 14,336,420 | 2.9% | 18.2% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 14,336,040 | 2.9% | 21.1% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,264,320 | 2.3% | 23.4% |
| RESUME_CHECK LOAD_FAST | 11,264,220 | 2.3% | 25.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 10,261,060 | 2.1% | 27.8% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 10,240,060 | 2.1% | 29.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 9,216,160 | 1.9% | 31.8% |
| LOAD_CONST LOAD_CONST | 8,192,460 | 1.7% | 33.5% |
| LOAD_CONST LOAD_FAST | 8,192,300 | 1.7% | 35.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 8,192,060 | 1.7% | 36.8% |
| CALL STORE_FAST | 7,188,660 | 1.5% | 38.3% |
| LOAD_ATTR_MODULE PUSH_NULL | 7,188,480 | 1.5% | 39.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 7,168,480 | 1.5% | 41.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 7,167,980 | 1.5% | 42.7% |
| PUSH_NULL CALL | 6,164,660 | 1.3% | 43.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 6,154,300 | 1.3% | 45.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 6,154,180 | 1.3% | 46.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 6,144,060 | 1.3% | 47.7% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST | 6,143,880 | 1.3% | 48.9% |
| STORE_FAST LOAD_FAST | 5,130,800 | 1.0% | 50.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 5,120,300 | 1.0% | 51.0% |
| RETURN_CONST POP_TOP | 5,120,140 | 1.0% | 52.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,120,100 | 1.0% | 53.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 5,120,080 | 1.0% | 54.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 5,119,960 | 1.0% | 55.2% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 5,119,840 | 1.0% | 56.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 4,106,240 | 0.8% | 57.1% |
| LOAD_FAST RETURN_VALUE | 4,096,320 | 0.8% | 57.9% |
| RETURN_VALUE STORE_FAST | 4,096,280 | 0.8% | 58.8% |
| LOAD_ATTR_MODULE LOAD_FAST | 4,096,180 | 0.8% | 59.6% |
| POP_TOP LOAD_FAST | 4,096,140 | 0.8% | 60.4% |
| LOAD_FAST LOAD_ATTR_MODULE | 4,095,980 | 0.8% | 61.3% |
| CALL_METHOD_DESCRIPTOR_FAST LOAD_FAST | 4,095,980 | 0.8% | 62.1% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 4,095,840 | 0.8% | 63.0% |
| POP_TOP RETURN_CONST | 3,072,340 | 0.6% | 63.6% |
| PUSH_NULL LOAD_FAST | 3,072,300 | 0.6% | 64.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,072,300 | 0.6% | 64.8% |
| POP_JUMP_IF_NONE LOAD_FAST | 3,072,120 | 0.6% | 65.5% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 3,072,100 | 0.6% | 66.1% |
| BUILD_MAP LOAD_FAST | 3,072,080 | 0.6% | 66.7% |
| LOAD_FAST BUILD_MAP | 3,072,080 | 0.6% | 67.3% |
| RETURN_VALUE INTERPRETER_EXIT | 3,072,040 | 0.6% | 68.0% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 3,071,980 | 0.6% | 68.6% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 3,071,960 | 0.6% | 69.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 3,071,900 | 0.6% | 69.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 2,058,420 | 0.4% | 70.3% |
| LOAD_FAST CALL | 2,048,420 | 0.4% | 70.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 2,048,260 | 0.4% | 71.1% |
| POP_TOP NOP | 2,048,240 | 0.4% | 71.5% |
| LOAD_FAST LOAD_CONST | 2,048,240 | 0.4% | 71.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,048,240 | 0.4% | 72.4% |
| LOAD_ATTR PUSH_NULL | 2,048,220 | 0.4% | 72.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 2,048,160 | 0.4% | 73.2% |
| POP_JUMP_IF_FALSE RETURN_CONST | 2,048,120 | 0.4% | 73.6% |
| NOP LOAD_CONST | 2,048,100 | 0.4% | 74.0% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 2,048,100 | 0.4% | 74.5% |
| CALL LOAD_FAST | 2,048,100 | 0.4% | 74.9% |
| COPY_FREE_VARS RESUME_CHECK | 2,048,100 | 0.4% | 75.3% |
| DICT_MERGE CALL_FUNCTION_EX | 2,048,080 | 0.4% | 75.7% |
| LOAD_FAST DICT_MERGE | 2,048,080 | 0.4% | 76.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 2,048,080 | 0.4% | 76.5% |
| CACHE COPY_FREE_VARS | 2,048,060 | 0.4% | 77.0% |
| LOAD_CONST CALL_KW | 2,048,060 | 0.4% | 77.4% |
| LOAD_FAST GET_ITER | 2,048,060 | 0.4% | 77.8% |
| POP_TOP LOAD_FAST_LOAD_FAST | 2,048,040 | 0.4% | 78.2% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 2,048,040 | 0.4% | 78.6% |
| LOAD_FAST POP_JUMP_IF_NONE | 2,048,040 | 0.4% | 79.1% |
| CALL_BUILTIN_FAST TO_BOOL_BOOL | 2,048,040 | 0.4% | 79.5% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 2,048,040 | 0.4% | 79.9% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 2,048,040 | 0.4% | 80.3% |
| LOAD_ATTR_SLOT LOAD_FAST | 2,048,040 | 0.4% | 80.7% |
| LOAD_CONST COMPARE_OP_STR | 2,048,020 | 0.4% | 81.1% |
| LOAD_FAST LOAD_FAST | 2,048,020 | 0.4% | 81.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 2,048,020 | 0.4% | 82.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 2,048,020 | 0.4% | 82.4% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 2,048,020 | 0.4% | 82.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 2,048,020 | 0.4% | 83.2% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 2,048,020 | 0.4% | 83.7% |
| GET_ITER FOR_ITER_TUPLE | 2,048,000 | 0.4% | 84.1% |
| BUILD_LIST CALL | 2,048,000 | 0.4% | 84.5% |
| CALL_FUNCTION_EX POP_TOP | 2,048,000 | 0.4% | 84.9% |
| CALL_KW RETURN_VALUE | 2,048,000 | 0.4% | 85.3% |
| IMPORT_FROM STORE_FAST | 2,048,000 | 0.4% | 85.7% |
| IMPORT_NAME IMPORT_FROM | 2,048,000 | 0.4% | 86.2% |
| LOAD_CONST IMPORT_NAME | 2,048,000 | 0.4% | 86.6% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 2,048,000 | 0.4% | 87.0% |
| STORE_FAST POP_TOP | 2,048,000 | 0.4% | 87.4% |
| FOR_ITER_TUPLE LOAD_FAST | 2,048,000 | 0.4% | 87.8% |
| FOR_ITER_TUPLE STORE_FAST | 2,048,000 | 0.4% | 88.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 2,048,000 | 0.4% | 88.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 2,048,000 | 0.4% | 89.1% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_MODULE | 2,048,000 | 0.4% | 89.5% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 2,048,000 | 0.4% | 89.9% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 2,047,980 | 0.4% | 90.3% |
| LOAD_SUPER_ATTR_ATTR PUSH_NULL | 2,047,980 | 0.4% | 90.8% |
| LOAD_FAST LOAD_SUPER_ATTR_ATTR | 2,047,960 | 0.4% | 91.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 15,360,260 | 88.2% |
| COPY_FREE_VARS | 2,048,060 | 11.8% |
| RESUME | 140 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 50.0% |
| RETURN_VALUE | 40 | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 160 | 100.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| LOAD_ATTR_MODULE | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 20 | 50.0% |
| LOAD_CONST | 20 | 50.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,060 | 99.5% |
| CALL_BUILTIN_CLASS | 10,280 | 0.5% |
| CALL | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 2,048,000 | 99.5% |
| FOR_ITER_RANGE | 10,280 | 0.5% |
| FOR_ITER_LIST | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| LOAD_FAST_AND_CLEAR | 20 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 14,336,420 | 82.4% |
| RETURN_VALUE | 3,072,040 | 17.6% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 20 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,048,240 | 100.0% |
| STORE_FAST | 180 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 40 | 0.0% |
| CALL_LIST_APPEND | 40 | 0.0% |
| RESUME_CHECK | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,048,100 | 100.0% |
| LOAD_FAST | 200 | 0.0% |
| LOAD_GLOBAL_MODULE | 200 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 40 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,120,140 | 41.7% |
| CALL_FUNCTION_EX | 2,048,000 | 16.7% |
| STORE_FAST | 2,048,000 | 16.7% |
| CALL | 1,024,480 | 8.3% |
| RETURN_VALUE | 1,024,060 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,096,140 | 33.3% |
| RETURN_CONST | 3,072,340 | 25.0% |
| NOP | 2,048,240 | 16.7% |
| LOAD_FAST_LOAD_FAST | 2,048,040 | 16.7% |
| JUMP_BACKWARD | 1,024,040 | 8.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 40 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 7,188,480 | 63.7% |
| LOAD_ATTR | 2,048,220 | 18.1% |
| LOAD_SUPER_ATTR_ATTR | 2,047,980 | 18.1% |
| LOAD_DEREF | 180 | 0.0% |
| LOAD_FAST | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 6,164,660 | 54.6% |
| LOAD_FAST | 3,072,300 | 27.2% |
| LOAD_FAST_LOAD_FAST | 2,048,100 | 18.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,096,320 | 44.4% |
| CALL_KW | 2,048,000 | 22.2% |
| RETURN_VALUE | 1,024,120 | 11.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,024,020 | 11.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,023,980 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,096,280 | 44.4% |
| INTERPRETER_EXIT | 3,072,040 | 33.3% |
| RETURN_VALUE | 1,024,120 | 11.1% |
| POP_TOP | 1,024,060 | 11.1% |
| LOAD_FAST | 60 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| CALL | 20 | 20.0% |
| CALL_ISINSTANCE | 20 | 20.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 60.0% |
| TO_BOOL_BOOL | 20 | 20.0% |
| TO_BOOL_INT | 20 | 20.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| BINARY_OP | 20 | 20.0% |
| LOAD_CONST | 20 | 20.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 20 | 20.0% |
| LOAD_FAST | 20 | 20.0% |
| STORE_FAST | 20 | 20.0% |
| BINARY_OP_ADD_FLOAT | 20 | 20.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 20.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,047,960 | 66.7% |
| LOAD_FAST_LOAD_FAST | 1,024,000 | 33.3% |
| LOAD_FAST | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,048,000 | 66.7% |
| LOAD_FAST | 1,024,060 | 33.3% |
| STORE_FAST | 100 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,072,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,072,080 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 80.0% |
| LOAD_FAST | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 80.0% |
| LOAD_CONST | 20 | 20.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 6,164,660 | 54.6% |
| LOAD_FAST | 2,048,420 | 18.1% |
| BUILD_LIST | 2,048,000 | 18.1% |
| LOAD_GLOBAL_MODULE | 1,024,180 | 9.1% |
| CALL | 5,320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,188,660 | 63.7% |
| LOAD_FAST | 2,048,100 | 18.1% |
| POP_TOP | 1,024,480 | 9.1% |
| CALL_PY_EXACT_ARGS | 1,024,200 | 9.1% |
| CALL | 5,320 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 2,048,080 | 100.0% |
| CALL_INTRINSIC_1 | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,048,000 | 100.0% |
| RETURN_VALUE | 80 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


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
| LOAD_CONST | 2,048,060 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,048,000 | 100.0% |
| RESUME_CHECK | 40 | 0.0% |
| STORE_FAST | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 40 | 66.7% |
| LOAD_FAST | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 66.7% |
| POP_JUMP_IF_TRUE | 20 | 33.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 80 | 66.7% |
| LOAD_FAST | 20 | 16.7% |
| LOAD_FAST_LOAD_FAST | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 66.7% |
| POP_JUMP_IF_TRUE | 20 | 16.7% |
| STORE_FAST | 20 | 16.7% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 20 | 100.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 2,048,060 | 100.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,048,100 | 100.0% |
| RESUME | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 2,048,080 | 100.0% |


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
| FOR_ITER_RANGE | 40 | 50.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 2,048,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,048,000 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,048,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 2,048,000 | 100.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 60 | 75.0% |
| LOAD_FAST | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 75.0% |
| POP_JUMP_IF_TRUE | 20 | 25.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,047,980 | 66.4% |
| POP_TOP | 1,024,040 | 33.2% |
| CALL_LIST_APPEND | 10,220 | 0.3% |
| POP_JUMP_IF_NOT_NONE | 60 | 0.0% |
| LIST_APPEND | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 2,048,040 | 66.4% |
| FOR_ITER_RANGE | 1,034,200 | 33.6% |
| FOR_ITER_LIST | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,023,980 | 100.0% |
| STORE_ATTR | 20 | 0.0% |
| STORE_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,024,020 | 100.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 40 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 2,048,260 | 99.9% |
| LOAD_FAST | 1,340 | 0.1% |
| LOAD_ATTR | 800 | 0.0% |
| LOAD_GLOBAL | 300 | 0.0% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,048,220 | 99.9% |
| LOAD_ATTR | 800 | 0.0% |
| LOAD_FAST | 340 | 0.0% |
| LOAD_ATTR_MODULE | 320 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,192,460 | 28.6% |
| STORE_ATTR_INSTANCE_VALUE | 7,167,980 | 25.0% |
| LOAD_ATTR_METHOD_NO_DICT | 6,144,060 | 21.4% |
| LOAD_FAST | 2,048,240 | 7.1% |
| NOP | 2,048,100 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,192,460 | 28.6% |
| LOAD_FAST | 8,192,300 | 28.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 6,143,880 | 21.4% |
| CALL_KW | 2,048,060 | 7.1% |
| COMPARE_OP_STR | 2,048,020 | 7.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 26.7% |
| BUILD_LIST | 80 | 26.7% |
| RESUME_CHECK | 80 | 26.7% |
| LOAD_GLOBAL_BUILTIN | 40 | 13.3% |
| RESUME | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 180 | 60.0% |
| LIST_EXTEND | 80 | 26.7% |
| LOAD_FAST | 40 | 13.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,264,220 | 12.4% |
| LOAD_CONST | 8,192,300 | 9.0% |
| STORE_ATTR_INSTANCE_VALUE | 8,192,060 | 9.0% |
| STORE_FAST | 5,130,800 | 5.6% |
| LOAD_GLOBAL_MODULE | 5,120,300 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 22,527,700 | 24.7% |
| LOAD_ATTR_INSTANCE_VALUE | 16,384,620 | 18.0% |
| LOAD_ATTR_METHOD_NO_DICT | 6,154,300 | 6.8% |
| CALL_PY_EXACT_ARGS | 5,120,100 | 5.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,119,840 | 5.6% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 20 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 66.7% |
| LOAD_FAST | 20 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 80 | 66.7% |
| LOAD_FAST | 20 | 16.7% |
| CALL_LIST_APPEND | 20 | 16.7% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,240,060 | 34.5% |
| STORE_ATTR_INSTANCE_VALUE | 9,216,160 | 31.0% |
| PUSH_NULL | 2,048,100 | 6.9% |
| LOAD_GLOBAL_MODULE | 2,048,080 | 6.9% |
| POP_TOP | 2,048,040 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 20,480,040 | 68.9% |
| CALL_PY_EXACT_ARGS | 3,071,960 | 10.3% |
| LOAD_FAST | 2,058,420 | 6.9% |
| CALL_BUILTIN_FAST | 2,048,000 | 6.9% |
| BUILD_LIST | 1,024,000 | 3.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 400 | 35.7% |
| RESUME | 140 | 12.5% |
| RESUME_CHECK | 140 | 12.5% |
| POP_JUMP_IF_NONE | 120 | 10.7% |
| STORE_ATTR | 60 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 480 | 42.9% |
| LOAD_ATTR | 300 | 26.8% |
| LOAD_FAST | 120 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 80 | 7.1% |
| CALL | 60 | 5.4% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 20 | 50.0% |
| LOAD_SUPER_ATTR_ATTR | 20 | 50.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,072,100 | 42.9% |
| COMPARE_OP_STR | 2,048,020 | 28.6% |
| TO_BOOL_INT | 2,048,000 | 28.6% |
| COMPARE_OP_INT | 100 | 0.0% |
| CONTAINS_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,048,120 | 28.6% |
| LOAD_GLOBAL_BUILTIN | 2,048,020 | 28.6% |
| JUMP_BACKWARD | 2,047,980 | 28.6% |
| LOAD_FAST | 1,024,260 | 14.3% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,040 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,048,040 | 33.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,047,960 | 33.3% |
| LOAD_ATTR | 80 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,072,120 | 50.0% |
| LOAD_GLOBAL_MODULE | 2,047,920 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 1,023,980 | 16.7% |
| LOAD_GLOBAL | 120 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260 | 44.8% |
| CALL_BUILTIN_FAST | 120 | 20.7% |
| LOAD_FAST_CHECK | 80 | 13.8% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 13.8% |
| LOAD_GLOBAL_MODULE | 40 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 62.1% |
| LOAD_GLOBAL_MODULE | 100 | 17.2% |
| JUMP_BACKWARD | 60 | 10.3% |
| NOP | 40 | 6.9% |
| RETURN_CONST | 20 | 3.4% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,048,240 | 100.0% |
| TO_BOOL_STR | 60 | 0.0% |
| COMPARE_OP | 20 | 0.0% |
| CONTAINS_OP | 20 | 0.0% |
| IS_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,160 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |
| LOAD_CONST | 20 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 14,336,040 | 73.7% |
| POP_TOP | 3,072,340 | 15.8% |
| POP_JUMP_IF_FALSE | 2,048,120 | 10.5% |
| STORE_ATTR | 140 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 14,336,420 | 73.7% |
| POP_TOP | 5,120,140 | 26.3% |
| EXIT_INIT_CHECK | 60 | 0.0% |
| STORE_FAST | 60 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 660 | 57.9% |
| LOAD_FAST_LOAD_FAST | 480 | 42.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 540 | 47.4% |
| LOAD_FAST | 140 | 12.3% |
| RETURN_CONST | 140 | 12.3% |
| LOAD_FAST_LOAD_FAST | 120 | 10.5% |
| LOAD_CONST | 100 | 8.8% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 7,188,660 | 38.9% |
| RETURN_VALUE | 4,096,280 | 22.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,048,040 | 11.1% |
| IMPORT_FROM | 2,048,000 | 11.1% |
| FOR_ITER_TUPLE | 2,048,000 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,154,180 | 33.3% |
| LOAD_FAST | 5,130,800 | 27.8% |
| LOAD_GLOBAL_BUILTIN | 4,106,240 | 22.2% |
| POP_TOP | 2,048,000 | 11.1% |
| LOAD_CONST | 1,024,140 | 5.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 40 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 80.0% |
| UNPACK_SEQUENCE | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 80.0% |
| NOP | 20 | 20.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 28.6% |
| LOAD_FAST | 40 | 28.6% |
| BUILD_LIST | 20 | 14.3% |
| LOAD_FAST_AND_CLEAR | 20 | 14.3% |
| FOR_ITER_TUPLE | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60 | 42.9% |
| BUILD_LIST | 20 | 14.3% |
| LOAD_CONST | 20 | 14.3% |
| STORE_FAST | 20 | 14.3% |
| FOR_ITER_TUPLE | 20 | 14.3% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 100.0% |

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
| CALL | 200 | 50.0% |
| CACHE | 140 | 35.0% |
| COPY_FREE_VARS | 40 | 10.0% |
| CALL_FUNCTION_EX | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 35.0% |
| LOAD_GLOBAL | 140 | 35.0% |
| LOAD_FAST_LOAD_FAST | 100 | 25.0% |
| LOAD_DEREF | 20 | 5.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 10,200 | 99.8% |
| BINARY_OP | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,220 | 100.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 50.0% |
| LOAD_FAST | 20 | 50.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,200 | 99.8% |
| BINARY_OP | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 10,200 | 99.8% |
| BINARY_OP | 20 | 0.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 60.0% |
| PUSH_EXC_INFO | 40 | 40.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 75.0% |
| RETURN_VALUE | 20 | 25.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 50.0% |
| LOAD_FAST_LOAD_FAST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| STORE_FAST | 20 | 25.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 57.1% |
| LOAD_FAST | 40 | 28.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 57.1% |
| RESUME_CHECK | 40 | 28.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 20 | 14.3% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,200 | 99.2% |
| CALL | 40 | 0.4% |
| LOAD_FAST | 40 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 10,280 | 100.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,048,000 | 100.0% |
| LOAD_CONST | 160 | 0.0% |
| LOAD_FAST | 20 | 0.0% |
| LOAD_ATTR_SLOT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,048,040 | 100.0% |
| POP_JUMP_IF_NOT_NONE | 120 | 0.0% |
| POP_TOP | 40 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 66.7% |
| STORE_FAST | 20 | 33.3% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 20 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,048,020 | 66.7% |
| LOAD_ATTR_MODULE | 1,023,960 | 33.3% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,071,980 | 100.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| TO_BOOL_INT | 20 | 33.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,200 | 98.6% |
| CALL | 80 | 0.8% |
| LOAD_CONST | 20 | 0.2% |
| LOAD_FAST_CHECK | 20 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,220 | 98.8% |
| LOAD_FAST_LOAD_FAST | 60 | 0.6% |
| NOP | 40 | 0.4% |
| RETURN_CONST | 20 | 0.2% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,143,880 | 100.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |
| CALL | 60 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 40 | 0.0% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,095,980 | 66.7% |
| STORE_FAST | 2,048,040 | 33.3% |
| POP_TOP | 40 | 0.0% |
| LIST_APPEND | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_LAZY_DICT | 1,023,960 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,023,980 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,023,960 | 100.0% |
| LOAD_CONST | 80 | 0.0% |
| CALL | 20 | 0.0% |
| STORE_FAST | 20 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,024,000 | 100.0% |
| LOAD_CONST | 80 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120,100 | 45.5% |
| LOAD_FAST_LOAD_FAST | 3,071,960 | 27.3% |
| CALL | 1,024,200 | 9.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,024,000 | 9.1% |
| LOAD_GLOBAL_MODULE | 1,023,980 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,264,320 | 100.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20 | 100.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 100.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100 | 71.4% |
| LOAD_CONST | 40 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 100 | 71.4% |
| RETURN_VALUE | 20 | 14.3% |
| POP_JUMP_IF_TRUE | 20 | 14.3% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,048,020 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,048,020 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 50.0% |
| JUMP_BACKWARD | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 83.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20 | 16.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,034,200 | 99.0% |
| GET_ITER | 10,280 | 1.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,034,200 | 99.0% |
| LOAD_GLOBAL_MODULE | 10,200 | 1.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,048,040 | 50.0% |
| GET_ITER | 2,048,000 | 50.0% |
| SWAP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,000 | 50.0% |
| STORE_FAST | 2,048,000 | 50.0% |
| STORE_FAST_LOAD_FAST | 40 | 0.0% |
| SWAP | 20 | 0.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,047,920 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,047,960 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,384,620 | 100.0% |
| LOAD_ATTR | 260 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120,080 | 31.2% |
| POP_JUMP_IF_NONE | 2,048,040 | 12.5% |
| LOAD_CONST | 2,048,020 | 12.5% |
| LOAD_FAST_LOAD_FAST | 2,048,000 | 12.5% |
| LOAD_ATTR_METHOD_LAZY_DICT | 2,047,920 | 12.5% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,047,920 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,023,980 | 50.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,023,960 | 50.0% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,154,300 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |
| LOAD_ATTR_MODULE | 60 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,144,060 | 99.8% |
| LOAD_FAST | 10,360 | 0.2% |
| LOAD_GLOBAL_MODULE | 100 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,119,840 | 83.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,024,040 | 16.7% |
| LOAD_ATTR | 120 | 0.0% |
| LOAD_GLOBAL_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,119,960 | 83.3% |
| CALL_PY_EXACT_ARGS | 1,024,000 | 16.7% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,261,060 | 71.5% |
| LOAD_FAST | 4,095,980 | 28.5% |
| LOAD_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 7,188,480 | 50.1% |
| LOAD_FAST | 4,096,180 | 28.5% |
| LOAD_ATTR_CLASS | 2,047,920 | 14.3% |
| CALL_ISINSTANCE | 1,023,960 | 7.1% |
| CALL | 340 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,095,840 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,047,960 | 50.0% |
| POP_JUMP_IF_NONE | 2,047,960 | 50.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,024,000 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,023,960 | 50.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,048,040 | 100.0% |
| LOAD_CONST | 20 | 0.0% |
| STORE_FAST | 20 | 0.0% |
| CALL_BUILTIN_FAST | 20 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,106,240 | 44.5% |
| LOAD_FAST | 2,048,020 | 22.2% |
| POP_JUMP_IF_FALSE | 2,048,020 | 22.2% |
| POP_JUMP_IF_NONE | 1,023,980 | 11.1% |
| POP_JUMP_IF_TRUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,072,300 | 33.3% |
| CALL_ISINSTANCE | 2,048,020 | 22.2% |
| LOAD_FAST_LOAD_FAST | 2,048,000 | 22.2% |
| LOAD_GLOBAL_MODULE | 2,048,000 | 22.2% |
| LOAD_CONST | 10,220 | 0.1% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,168,480 | 33.3% |
| STORE_FAST | 6,154,180 | 28.6% |
| STORE_ATTR_INSTANCE_VALUE | 3,071,900 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 2,048,000 | 9.5% |
| POP_JUMP_IF_NONE | 2,047,920 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 10,261,060 | 47.7% |
| LOAD_FAST | 5,120,300 | 23.8% |
| LOAD_ATTR | 2,048,260 | 9.5% |
| LOAD_FAST_LOAD_FAST | 2,048,080 | 9.5% |
| CALL | 1,024,180 | 4.8% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,047,960 | 100.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,047,980 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 15,360,260 | 53.6% |
| CALL_PY_EXACT_ARGS | 11,264,320 | 39.3% |
| COPY_FREE_VARS | 2,048,100 | 7.1% |
| CALL | 200 | 0.0% |
| CALL_FUNCTION_EX | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,264,220 | 39.3% |
| LOAD_FAST_LOAD_FAST | 10,240,060 | 35.7% |
| LOAD_GLOBAL_MODULE | 7,168,480 | 25.0% |
| LOAD_GLOBAL | 140 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,527,700 | 52.4% |
| LOAD_FAST_LOAD_FAST | 20,480,040 | 47.6% |
| STORE_ATTR | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 14,336,040 | 33.3% |
| LOAD_FAST_LOAD_FAST | 9,216,160 | 21.4% |
| LOAD_FAST | 8,192,060 | 19.0% |
| LOAD_CONST | 7,167,980 | 16.7% |
| LOAD_GLOBAL_MODULE | 3,071,900 | 7.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 50.0% |
| NOP | 20 | 25.0% |
| LOAD_FAST | 20 | 25.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 3,071,980 | 60.0% |
| CALL_BUILTIN_FAST | 2,048,040 | 40.0% |
| LOAD_FAST | 140 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,072,100 | 60.0% |
| POP_JUMP_IF_TRUE | 2,048,240 | 40.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,047,960 | 100.0% |
| TO_BOOL | 20 | 0.0% |
| CALL_BUILTIN_O | 20 | 0.0% |
| CALL_LEN | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,048,000 | 100.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 50.0% |
| POP_JUMP_IF_TRUE | 20 | 50.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 100.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| STORE_FAST_LOAD_FAST | 40 | 40.0% |
| COPY | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 60 | 60.0% |
| POP_JUMP_IF_FALSE | 40 | 40.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 50.0% |
| UNPACK_SEQUENCE | 20 | 25.0% |
| FOR_ITER_LIST | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 80 | 100.0% |


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
|     deferred | 120 | 0.6% |
|          hit | 20,420 | 99.2% |
|         miss | 60 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|          hit | 180 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,286,240 | 31.4% |
|          hit | 24,597,520 | 68.5% |
|         miss | 260 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 7.7% |
| Failure | 5,240 | 92.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| wrong number arguments | 3,100 | 59.2% |
| cfunc varargs | 880 | 16.8% |
| class no vectorcall | 880 | 16.8% |
| cfunc noargs | 360 | 6.9% |
| code complex parameters | 20 | 0.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 2,048,180 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 5,140,700 | 100.0% |

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
|     deferred | 2,049,440 | 3.7% |
|        deopt | 20 | 0.0% |
|          hit | 53,280,640 | 96.3% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,000 | 58.8% |
| Failure | 700 | 41.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 700 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,620 | 0.0% |
|        deopt | 40 | 0.0% |
|          hit | 30,748,760 | 100.0% |
|         miss | 4,120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 2,048,020 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
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
|     deferred | 600 | 0.0% |
|          hit | 43,008,300 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 540 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|          hit | 80 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 7,168,520 | 100.0% |
|         miss | 40 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 16.7% |
|          hit | 80 | 66.7% |

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
| Basic | 264,342,240 | 54.0% |
| Not specialized | 28,706,980 | 5.9% |
| Specialized hits | 196,734,520 | 40.2% |
| Specialized misses | 4,760 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 11,286,240 | 84.6% |
| LOAD_ATTR | 2,049,440 | 15.4% |
| LOAD_GLOBAL | 4,620 | 0.0% |
| STORE_ATTR | 600 | 0.0% |
| BINARY_OP | 120 | 0.0% |
| TO_BOOL | 100 | 0.0% |
| COMPARE_OP | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,140 | 66.0% |
| LOAD_GLOBAL_MODULE | 980 | 20.6% |
| LOAD_ATTR_MODULE | 240 | 5.0% |
| CALL_PY_EXACT_ARGS | 120 | 2.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 100 | 2.1% |
| BINARY_OP_ADD_FLOAT | 60 | 1.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.8% |
| TO_BOOL_NONE | 40 | 0.8% |
| CALL_ALLOC_AND_ENTER_INIT | 20 | 0.4% |
| CALL_METHOD_DESCRIPTOR_O | 20 | 0.4% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 17,408,460 | 60.7% |
| Calls to Python functions inlined | 11,265,100 | 39.3% |
| Calls via PyEval_EvalFrame (total) | 17,408,460 | 60.7% |
| Calls via PyEval_EvalFrame (vector) | 17,408,460 | 60.7% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 17,408,460 | 60.7% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 3,072,060 | 10.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 40 | 0.0% |
| Frames pushed | 11,264,440 | 39.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 46,108,000 | 42.5% |
| Frees to freelist | 46,109,920 |  |
| Allocations | 62,492,340 | 57.5% |
| Allocations to 512 bytes | 62,492,340 | 57.5% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 62,490,126 |  |
| New values | 12,288,200 |  |
| Interpreter increfs | 283,765,180 | 68.9% |
| Interpreter decrefs | 296,097,320 | 61.2% |
| Increfs | 128,008,156 | 31.1% |
| Decrefs | 187,411,055 | 38.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 21,506,521 |  |
| Method cache misses | 1,019 |  |
| Method cache collisions | 940 |  |
| Method cache dunder hits | 20,484,458 |  |
| Method cache dunder misses | 222 |  |


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
