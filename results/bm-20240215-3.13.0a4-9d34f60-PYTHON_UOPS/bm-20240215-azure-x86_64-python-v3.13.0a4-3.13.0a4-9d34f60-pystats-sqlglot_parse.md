
# Pystats results

- benchmark: sqlglot_parse
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 495,012,760 | 25.0% | 25.0% |  |
| LOAD_ATTR_SLOT | 268,570,580 | 13.6% | 38.6% | 0.9% |
| POP_JUMP_IF_FALSE | 102,752,760 | 5.2% | 43.8% |  |
| STORE_ATTR_SLOT | 88,641,660 | 4.5% | 48.2% | 7.6% |
| RESUME_CHECK | 75,836,160 | 3.8% | 52.1% | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 59,624,620 | 3.0% | 55.1% |  |
| POP_JUMP_IF_TRUE | 46,921,560 | 2.4% | 57.4% |  |
| STORE_FAST | 46,092,240 | 2.3% | 59.8% |  |
| RETURN_CONST | 43,028,480 | 2.2% | 62.0% |  |
| LOAD_CONST | 42,681,840 | 2.2% | 64.1% |  |
| CALL_PY_EXACT_ARGS | 39,973,080 | 2.0% | 66.1% | 2.5% |
| LOAD_GLOBAL_MODULE | 34,048,260 | 1.7% | 67.8% | 0.0% |
| RETURN_VALUE | 33,065,680 | 1.7% | 69.5% |  |
| COMPARE_OP_INT | 32,768,280 | 1.7% | 71.2% |  |
| BINARY_OP_ADD_INT | 32,675,680 | 1.7% | 72.8% |  |
| COPY | 32,051,200 | 1.6% | 74.4% |  |
| SWAP | 29,583,640 | 1.5% | 75.9% |  |
| BINARY_SUBSCR_STR_INT | 28,293,060 | 1.4% | 77.4% |  |
| LOAD_FAST_LOAD_FAST | 27,168,440 | 1.4% | 78.7% |  |
| TO_BOOL_ALWAYS_TRUE | 25,505,740 | 1.3% | 80.0% | 6.3% |
| LOAD_ATTR | 24,968,300 | 1.3% | 81.3% |  |
| ENTER_EXECUTOR | 23,699,100 | 1.2% | 82.5% |  |
| POP_TOP | 23,357,880 | 1.2% | 83.7% |  |
| TO_BOOL_BOOL | 22,876,140 | 1.2% | 84.8% | 2.8% |
| COMPARE_OP | 22,024,280 | 1.1% | 85.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 21,769,780 | 1.1% | 87.0% |  |
| TO_BOOL_NONE | 21,501,040 | 1.1% | 88.1% | 10.6% |
| CALL_PY_WITH_DEFAULTS | 18,708,000 | 0.9% | 89.1% |  |
| BINARY_OP_SUBTRACT_INT | 17,571,700 | 0.9% | 89.9% |  |
| JUMP_FORWARD | 16,957,440 | 0.9% | 90.8% |  |
| LOAD_GLOBAL_BUILTIN | 15,834,580 | 0.8% | 91.6% | 0.0% |
| CONTAINS_OP | 14,275,220 | 0.7% | 92.3% |  |
| TO_BOOL_STR | 13,846,280 | 0.7% | 93.0% | 0.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 12,790,080 | 0.6% | 93.7% |  |
| INTERPRETER_EXIT | 11,120,760 | 0.6% | 94.2% |  |
| TO_BOOL_INT | 8,949,720 | 0.5% | 94.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 6,922,260 | 0.3% | 95.0% | 0.0% |
| CALL_BUILTIN_O | 6,860,800 | 0.3% | 95.4% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,287,480 | 0.3% | 95.7% |  |
| NOP | 6,031,440 | 0.3% | 96.0% |  |
| GET_ITER | 5,079,440 | 0.3% | 96.3% |  |
| FOR_ITER | 4,953,660 | 0.3% | 96.5% |  |
| LOAD_DEREF | 4,935,920 | 0.2% | 96.8% |  |
| BINARY_SUBSCR_LIST_INT | 4,332,020 | 0.2% | 97.0% | 0.7% |
| STORE_FAST_STORE_FAST | 4,262,300 | 0.2% | 97.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,262,220 | 0.2% | 97.4% |  |
| PUSH_NULL | 4,024,960 | 0.2% | 97.6% |  |
| CALL_ISINSTANCE | 3,740,320 | 0.2% | 97.8% |  |
| LOAD_ATTR_PROPERTY | 3,737,500 | 0.2% | 98.0% |  |
| BINARY_SLICE | 3,573,760 | 0.2% | 98.2% |  |
| CALL_LIST_APPEND | 2,979,760 | 0.2% | 98.3% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,913,140 | 0.1% | 98.5% | 83.8% |
| LOAD_ATTR_MODULE | 2,119,460 | 0.1% | 98.6% |  |
| BINARY_SUBSCR_DICT | 1,925,000 | 0.1% | 98.7% |  |
| COMPARE_OP_STR | 1,874,620 | 0.1% | 98.8% |  |
| BUILD_TUPLE | 1,812,760 | 0.1% | 98.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,715,180 | 0.1% | 98.9% | 79.1% |
| CALL_KW | 1,607,680 | 0.1% | 99.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 1,576,920 | 0.1% | 99.1% |  |
| CALL_LEN | 1,576,780 | 0.1% | 99.2% |  |
| CALL | 1,529,040 | 0.1% | 99.3% |  |
| POP_JUMP_IF_NONE | 1,454,080 | 0.1% | 99.3% |  |
| POP_JUMP_IF_NOT_NONE | 1,443,840 | 0.1% | 99.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,413,100 | 0.1% | 99.5% |  |
| BUILD_LIST | 1,382,480 | 0.1% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,337,160 | 0.1% | 99.6% | 71.0% |
| CALL_TYPE_1 | 1,208,280 | 0.1% | 99.7% |  |
| CALL_FUNCTION_EX | 1,013,920 | 0.1% | 99.7% |  |
| DICT_MERGE | 1,013,760 | 0.1% | 99.8% |  |
| BUILD_MAP | 1,003,520 | 0.1% | 99.8% |  |
| MAKE_CELL | 839,680 | 0.0% | 99.9% |  |
| IS_OP | 604,160 | 0.0% | 99.9% |  |
| EXTENDED_ARG | 594,600 | 0.0% | 99.9% |  |
| FOR_ITER_LIST | 215,200 | 0.0% | 99.9% |  |
| STORE_DEREF | 174,080 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 161,640 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 82,000 | 0.0% | 100.0% |  |
| CALL_STR_1 | 71,640 | 0.0% | 100.0% |  |
| UNARY_NOT | 61,440 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 61,440 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 61,440 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 60,880 | 0.0% | 100.0% | 15.7% |
| BUILD_CONST_KEY_MAP | 51,200 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 40,940 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 30,720 | 0.0% | 100.0% |  |
| POP_EXCEPT | 30,720 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 30,720 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 20,480 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 20,480 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 20,460 | 0.0% | 100.0% |  |
| TO_BOOL | 16,880 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 11,280 | 0.0% | 100.0% |  |
| DICT_UPDATE | 10,240 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 10,220 | 0.0% | 100.0% | 0.6% |
| BINARY_OP_SUBTRACT_FLOAT | 10,220 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 10,220 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 6,640 | 0.0% | 100.0% |  |
| RESUME | 2,040 | 0.0% | 100.0% | 206.9% |
| STORE_ATTR | 1,720 | 0.0% | 100.0% |  |
| BINARY_OP | 760 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 460 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 160 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_SLOT | 218,787,440 | 11.1% | 11.1% |
| LOAD_ATTR_SLOT LOAD_FAST | 115,712,220 | 5.8% | 16.9% |
| STORE_ATTR_SLOT LOAD_FAST | 60,743,720 | 3.1% | 20.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 60,550,880 | 3.1% | 23.0% |
| RESUME_CHECK LOAD_FAST | 52,960,320 | 2.7% | 25.7% |
| LOAD_FAST STORE_ATTR_SLOT | 50,462,000 | 2.5% | 28.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 39,462,620 | 2.0% | 30.2% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 35,946,560 | 1.8% | 32.1% |
| POP_JUMP_IF_TRUE LOAD_FAST | 31,048,000 | 1.6% | 33.6% |
| STORE_FAST LOAD_FAST | 30,782,300 | 1.6% | 35.2% |
| LOAD_FAST BINARY_OP_ADD_INT | 29,726,560 | 1.5% | 36.7% |
| LOAD_FAST COPY | 29,071,360 | 1.5% | 38.1% |
| BINARY_OP_ADD_INT SWAP | 29,030,320 | 1.5% | 39.6% |
| COPY LOAD_ATTR_SLOT | 29,030,240 | 1.5% | 41.1% |
| SWAP STORE_ATTR_SLOT | 29,030,240 | 1.5% | 42.5% |
| LOAD_ATTR_SLOT COMPARE_OP_INT | 28,303,240 | 1.4% | 44.0% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 27,187,160 | 1.4% | 45.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 27,074,020 | 1.4% | 46.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 22,803,720 | 1.2% | 47.9% |
| RETURN_CONST POP_TOP | 21,237,760 | 1.1% | 48.9% |
| COMPARE_OP POP_JUMP_IF_FALSE | 20,839,160 | 1.1% | 50.0% |
| LOAD_ATTR_SLOT LOAD_CONST | 20,080,960 | 1.0% | 51.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 19,169,580 | 1.0% | 52.0% |
| POP_JUMP_IF_FALSE RETURN_CONST | 18,728,960 | 0.9% | 52.9% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 18,708,000 | 0.9% | 53.9% |
| STORE_ATTR_SLOT RETURN_CONST | 18,073,480 | 0.9% | 54.8% |
| LOAD_ATTR_SLOT LOAD_ATTR_SLOT | 17,863,080 | 0.9% | 55.7% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 17,662,880 | 0.9% | 56.6% |
| LOAD_ATTR_SLOT TO_BOOL_ALWAYS_TRUE | 17,543,660 | 0.9% | 57.5% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 16,528,860 | 0.8% | 58.3% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 16,277,520 | 0.8% | 59.1% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 16,148,280 | 0.8% | 59.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 14,481,820 | 0.7% | 60.7% |
| RETURN_CONST TO_BOOL_NONE | 13,989,340 | 0.7% | 61.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 13,717,880 | 0.7% | 62.1% |
| COMPARE_OP_INT LOAD_FAST | 13,598,700 | 0.7% | 62.8% |
| BINARY_OP_SUBTRACT_INT BINARY_SUBSCR_STR_INT | 13,598,680 | 0.7% | 63.4% |
| LOAD_ATTR_SLOT BINARY_SUBSCR_STR_INT | 13,588,440 | 0.7% | 64.1% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 13,422,700 | 0.7% | 64.8% |
| POP_TOP LOAD_FAST | 12,482,600 | 0.6% | 65.4% |
| ENTER_EXECUTOR CALL_PY_WITH_DEFAULTS | 12,215,720 | 0.6% | 66.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 12,073,220 | 0.6% | 66.7% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 11,889,000 | 0.6% | 67.3% |
| LOAD_FAST COMPARE_OP | 11,366,480 | 0.6% | 67.8% |
| JUMP_FORWARD LOAD_FAST | 11,335,680 | 0.6% | 68.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 11,295,340 | 0.6% | 69.0% |
| CACHE RESUME_CHECK | 11,120,500 | 0.6% | 69.5% |
| LOAD_ATTR CALL_PY_EXACT_ARGS | 10,769,420 | 0.5% | 70.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 10,616,900 | 0.5% | 70.6% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 10,517,820 | 0.5% | 71.2% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 10,516,560 | 0.5% | 71.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT LOAD_ATTR_METHOD_NO_DICT | 9,860,920 | 0.5% | 72.2% |
| LOAD_ATTR COMPARE_OP | 9,492,920 | 0.5% | 72.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 9,328,160 | 0.5% | 73.1% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 9,164,880 | 0.5% | 73.6% |
| LOAD_ATTR_SLOT CALL_METHOD_DESCRIPTOR_FAST | 9,021,360 | 0.5% | 74.1% |
| LOAD_ATTR_SLOT TO_BOOL_INT | 8,949,680 | 0.5% | 74.5% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 8,946,440 | 0.5% | 75.0% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 8,939,500 | 0.5% | 75.4% |
| LOAD_ATTR_SLOT TO_BOOL_STR | 8,939,480 | 0.5% | 75.9% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 8,867,720 | 0.4% | 76.3% |
| POP_JUMP_IF_FALSE JUMP_FORWARD | 8,581,160 | 0.4% | 76.7% |
| RETURN_VALUE INTERPRETER_EXIT | 8,048,760 | 0.4% | 77.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 8,038,200 | 0.4% | 77.6% |
| LOAD_FAST TO_BOOL_ALWAYS_TRUE | 7,804,900 | 0.4% | 77.9% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 7,688,240 | 0.4% | 78.3% |
| RETURN_VALUE STORE_FAST | 7,669,740 | 0.4% | 78.7% |
| RETURN_VALUE RETURN_VALUE | 7,639,120 | 0.4% | 79.1% |
| LOAD_CONST STORE_FAST | 7,250,000 | 0.4% | 79.5% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,922,240 | 0.3% | 79.8% |
| CALL_BUILTIN_O RETURN_VALUE | 6,860,800 | 0.3% | 80.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_O | 6,860,800 | 0.3% | 80.5% |
| LOAD_CONST LOAD_FAST | 6,656,280 | 0.3% | 80.9% |
| LOAD_FAST TO_BOOL_BOOL | 6,471,740 | 0.3% | 81.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 6,287,280 | 0.3% | 81.5% |
| LOAD_FAST RETURN_VALUE | 5,939,280 | 0.3% | 81.8% |
| LOAD_FAST TO_BOOL_NONE | 5,793,800 | 0.3% | 82.1% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 5,785,740 | 0.3% | 82.4% |
| STORE_FAST LOAD_CONST | 5,570,560 | 0.3% | 82.7% |
| LOAD_FAST CONTAINS_OP | 5,509,120 | 0.3% | 82.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT CONTAINS_OP | 5,498,960 | 0.3% | 83.2% |
| RESUME_CHECK NOP | 5,119,960 | 0.3% | 83.5% |
| GET_ITER FOR_ITER | 4,946,360 | 0.2% | 83.7% |
| LOAD_FAST TO_BOOL_STR | 4,813,120 | 0.2% | 84.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 4,772,260 | 0.2% | 84.2% |
| TO_BOOL_NONE POP_JUMP_IF_TRUE | 4,740,140 | 0.2% | 84.5% |
| LOAD_DEREF LOAD_ATTR_METHOD_NO_DICT | 4,739,200 | 0.2% | 84.7% |
| LOAD_FAST LOAD_CONST | 4,670,000 | 0.2% | 84.9% |
| RETURN_VALUE LOAD_FAST | 4,444,420 | 0.2% | 85.2% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 4,433,800 | 0.2% | 85.4% |
| LOAD_CONST COMPARE_OP_INT | 4,413,760 | 0.2% | 85.6% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 4,341,600 | 0.2% | 85.8% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 4,321,160 | 0.2% | 86.0% |
| NOP LOAD_FAST_LOAD_FAST | 4,300,800 | 0.2% | 86.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 4,300,760 | 0.2% | 86.5% |
| BINARY_SUBSCR_LIST_INT RETURN_VALUE | 4,280,280 | 0.2% | 86.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT CALL_PY_EXACT_ARGS | 4,269,440 | 0.2% | 86.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 4,262,220 | 0.2% | 87.1% |
| LOAD_FAST STORE_FAST | 4,188,480 | 0.2% | 87.3% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 4,168,660 | 0.2% | 87.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 3,573,740 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,573,760 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,120,500 | 100.0% |
| RESUME | 260 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,105,880 | 70.1% |
| ENTER_EXECUTOR | 409,320 | 26.0% |
| LOAD_ATTR_SLOT | 61,680 | 3.9% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,576,920 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,600 | 94.0% |
| BINARY_SUBSCR | 160 | 1.4% |
| LOAD_FAST_LOAD_FAST | 160 | 1.4% |
| LOAD_ATTR | 80 | 0.7% |
| LOAD_FAST | 80 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 10,520 | 93.3% |
| BINARY_SUBSCR | 160 | 1.4% |
| BINARY_SUBSCR_DICT | 120 | 1.1% |
| BINARY_SUBSCR_LIST_INT | 80 | 0.7% |
| RETURN_VALUE | 60 | 0.5% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 30,700 | 99.9% |
| LOAD_GLOBAL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 30,720 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,570,220 | 50.6% |
| LOAD_FAST | 1,515,840 | 29.8% |
| LOAD_ATTR_SLOT | 982,980 | 19.4% |
| CALL_BUILTIN_CLASS | 10,280 | 0.2% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 4,946,360 | 97.4% |
| FOR_ITER_LIST | 133,020 | 2.6% |
| FOR_ITER_RANGE | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,048,760 | 72.4% |
| RETURN_CONST | 3,072,000 | 27.6% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 20,480 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,119,960 | 84.9% |
| POP_JUMP_IF_FALSE | 481,280 | 8.0% |
| STORE_FAST | 430,080 | 7.1% |
| POP_TOP | 80 | 0.0% |
| RESUME | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,300,800 | 71.3% |
| LOAD_FAST | 1,730,560 | 28.7% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 30,720 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 21,237,760 | 90.9% |
| POP_JUMP_IF_TRUE | 1,064,960 | 4.6% |
| SWAP | 553,240 | 2.4% |
| POP_JUMP_IF_FALSE | 481,280 | 2.1% |
| RETURN_VALUE | 20,480 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,482,600 | 53.4% |
| JUMP_FORWARD | 4,126,720 | 17.7% |
| RETURN_CONST | 3,471,360 | 14.9% |
| LOAD_CONST | 1,607,680 | 6.9% |
| RETURN_VALUE | 553,240 | 2.4% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 30,680 | 99.9% |
| LOAD_GLOBAL | 40 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,092,480 | 76.8% |
| LOAD_ATTR_MODULE | 584,020 | 14.5% |
| LOAD_FAST_LOAD_FAST | 204,800 | 5.1% |
| BINARY_SUBSCR_DICT | 71,660 | 1.8% |
| LOAD_ATTR | 51,360 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 1,227,140 | 30.5% |
| CALL_PY_EXACT_ARGS | 1,024,820 | 25.5% |
| LOAD_CONST | 983,040 | 24.4% |
| LOAD_FAST | 583,840 | 14.5% |
| LOAD_FAST_LOAD_FAST | 71,680 | 1.8% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,639,120 | 23.1% |
| CALL_BUILTIN_O | 6,860,800 | 20.7% |
| LOAD_FAST | 5,939,280 | 18.0% |
| BINARY_SUBSCR_LIST_INT | 4,280,280 | 12.9% |
| BINARY_SLICE | 3,573,760 | 10.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 8,048,760 | 24.3% |
| STORE_FAST | 7,669,740 | 23.2% |
| RETURN_VALUE | 7,639,120 | 23.1% |
| LOAD_FAST | 4,444,420 | 13.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,679,560 | 5.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

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
| LOAD_FAST | 11,760 | 69.7% |
| RETURN_CONST | 2,880 | 17.1% |
| COPY | 840 | 5.0% |
| LOAD_ATTR | 380 | 2.3% |
| LOAD_ATTR_SLOT | 300 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,360 | 73.2% |
| TO_BOOL_NONE | 2,020 | 12.0% |
| POP_JUMP_IF_TRUE | 1,000 | 5.9% |
| TO_BOOL_BOOL | 820 | 4.9% |
| TO_BOOL_ALWAYS_TRUE | 180 | 1.1% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 61,420 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 61,440 | 100.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 47.4% |
| LOAD_FAST | 200 | 26.3% |
| LOAD_ATTR | 40 | 5.3% |
| LOAD_FAST_LOAD_FAST | 40 | 5.3% |
| LOAD_ATTR_SLOT | 40 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 160 | 21.1% |
| BINARY_OP_SUBTRACT_INT | 140 | 18.4% |
| STORE_FAST | 120 | 15.8% |
| CALL | 80 | 10.5% |
| SWAP | 80 | 10.5% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 51,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 20,480 | 40.0% |
| LOAD_DEREF | 20,480 | 40.0% |
| LOAD_FAST | 10,240 | 20.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,269,840 | 91.9% |
| STORE_ATTR_SLOT | 71,620 | 5.2% |
| BUILD_LIST | 20,480 | 1.5% |
| RETURN_VALUE | 10,240 | 0.7% |
| ENTER_EXECUTOR | 9,920 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 1,157,120 | 83.7% |
| JUMP_FORWARD | 112,640 | 8.1% |
| LOAD_FAST | 71,680 | 5.2% |
| BUILD_LIST | 20,480 | 1.5% |
| STORE_FAST | 20,480 | 1.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 983,040 | 98.0% |
| BUILD_TUPLE | 10,240 | 1.0% |
| STORE_FAST | 10,240 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 993,280 | 99.0% |
| STORE_FAST | 10,240 | 1.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,689,880 | 93.2% |
| LOAD_GLOBAL_MODULE | 81,900 | 4.5% |
| POP_JUMP_IF_FALSE | 20,480 | 1.1% |
| LOAD_ATTR_MODULE | 20,460 | 1.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,126,400 | 62.1% |
| SWAP | 553,240 | 30.5% |
| CALL_ISINSTANCE | 81,880 | 4.5% |
| LOAD_CONST | 20,480 | 1.1% |
| LOAD_FAST | 20,480 | 1.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,413,260 | 92.4% |
| LOAD_CONST | 61,720 | 4.0% |
| PUSH_NULL | 21,800 | 1.4% |
| LOAD_GLOBAL_MODULE | 10,260 | 0.7% |
| ENTER_EXECUTOR | 9,840 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 1,413,160 | 92.4% |
| TO_BOOL_BOOL | 61,400 | 4.0% |
| STORE_FAST | 20,700 | 1.4% |
| RESUME_CHECK | 13,640 | 0.9% |
| LOAD_FAST | 10,280 | 0.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 1,013,760 | 100.0% |
| CALL_INTRINSIC_1 | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 983,040 | 97.0% |
| RETURN_VALUE | 20,480 | 2.0% |
| LOAD_ATTR_METHOD_NO_DICT | 10,200 | 1.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |


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
| LOAD_CONST | 1,607,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 962,500 | 59.9% |
| RETURN_VALUE | 645,120 | 40.1% |
| RESUME | 60 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,366,480 | 51.6% |
| LOAD_ATTR | 9,492,920 | 43.1% |
| BUILD_LIST | 1,157,120 | 5.3% |
| COMPARE_OP | 7,040 | 0.0% |
| LOAD_CONST | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,839,160 | 94.6% |
| POP_JUMP_IF_TRUE | 1,157,120 | 5.3% |
| STORE_FAST | 20,480 | 0.1% |
| COMPARE_OP | 7,040 | 0.0% |
| COMPARE_OP_INT | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,509,120 | 38.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 5,498,960 | 38.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,853,460 | 13.0% |
| LOAD_FAST_LOAD_FAST | 1,403,200 | 9.8% |
| LOAD_CONST | 10,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 11,295,340 | 79.1% |
| POP_JUMP_IF_TRUE | 1,853,480 | 13.0% |
| STORE_FAST | 1,126,400 | 7.9% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,071,360 | 90.7% |
| RETURN_CONST | 1,607,680 | 5.0% |
| IS_OP | 604,160 | 1.9% |
| CALL_ISINSTANCE | 522,200 | 1.6% |
| RETURN_VALUE | 184,320 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 29,030,240 | 90.6% |
| TO_BOOL_BOOL | 1,576,060 | 4.9% |
| TO_BOOL_NONE | 1,266,240 | 4.0% |
| TO_BOOL_ALWAYS_TRUE | 126,540 | 0.4% |
| TO_BOOL_LIST | 40,920 | 0.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 50,360 | 61.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 31,520 | 38.4% |
| CALL_FUNCTION_EX | 80 | 0.1% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 81,960 | 100.0% |
| RESUME | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 983,040 | 97.0% |
| BUILD_CONST_KEY_MAP | 20,480 | 2.0% |
| DICT_UPDATE | 10,240 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,013,760 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 10,240 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 13,422,700 | 56.6% |
| JUMP_FORWARD | 4,105,900 | 17.3% |
| STORE_ATTR_SLOT | 1,555,200 | 6.6% |
| CALL_LIST_APPEND | 1,402,540 | 5.9% |
| STORE_FAST | 1,125,380 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 12,215,720 | 51.5% |
| LOAD_FAST | 2,037,140 | 8.6% |
| RETURN_CONST | 1,606,040 | 6.8% |
| CALL_LIST_APPEND | 1,392,320 | 5.9% |
| LOAD_CONST | 1,105,600 | 4.7% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 440,380 | 74.1% |
| TO_BOOL_BOOL | 112,500 | 18.9% |
| STORE_FAST | 30,720 | 5.2% |
| TO_BOOL_INT | 10,220 | 1.7% |
| POP_TOP | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 552,960 | 93.0% |
| JUMP_FORWARD | 30,720 | 5.2% |
| POP_JUMP_IF_TRUE | 10,240 | 1.7% |
| JUMP_BACKWARD | 680 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 4,946,360 | 99.9% |
| JUMP_BACKWARD | 5,220 | 0.1% |
| FOR_ITER | 2,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,582,580 | 52.1% |
| STORE_FAST | 2,365,940 | 47.8% |
| FOR_ITER | 2,080 | 0.0% |
| RETURN_CONST | 1,660 | 0.0% |
| LOAD_FAST | 580 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_TYPE_1 | 604,140 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 604,160 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 154,280 | 95.4% |
| POP_JUMP_IF_TRUE | 2,920 | 1.8% |
| STORE_ATTR_SLOT | 1,300 | 0.8% |
| STORE_FAST | 1,020 | 0.6% |
| EXTENDED_ARG | 680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 154,880 | 95.8% |
| FOR_ITER | 5,220 | 3.2% |
| FOR_ITER_LIST | 900 | 0.6% |
| ENTER_EXECUTOR | 340 | 0.2% |
| FOR_ITER_RANGE | 300 | 0.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,581,160 | 50.6% |
| POP_TOP | 4,126,720 | 24.3% |
| STORE_FAST | 1,505,280 | 8.9% |
| RETURN_VALUE | 1,351,660 | 8.0% |
| ENTER_EXECUTOR | 819,160 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,335,680 | 66.8% |
| ENTER_EXECUTOR | 4,105,900 | 24.2% |
| STORE_FAST | 1,464,320 | 8.6% |
| LOAD_DEREF | 30,720 | 0.2% |
| CALL_PY_EXACT_ARGS | 20,460 | 0.1% |


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
| LOAD_GLOBAL_MODULE | 22,803,720 | 91.3% |
| LOAD_FAST | 2,019,000 | 8.1% |
| LOAD_ATTR_MODULE | 92,100 | 0.4% |
| LOAD_ATTR | 26,880 | 0.1% |
| LOAD_DEREF | 22,400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,769,420 | 43.1% |
| COMPARE_OP | 9,492,920 | 38.0% |
| LOAD_FAST | 1,957,800 | 7.8% |
| LOAD_GLOBAL_MODULE | 900,920 | 3.6% |
| CALL_PY_WITH_DEFAULTS | 849,800 | 3.4% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 20,080,960 | 47.0% |
| STORE_FAST | 5,570,560 | 13.1% |
| LOAD_FAST | 4,670,000 | 10.9% |
| POP_JUMP_IF_FALSE | 2,396,440 | 5.6% |
| STORE_ATTR_SLOT | 1,791,900 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 16,148,280 | 37.8% |
| STORE_FAST | 7,250,000 | 17.0% |
| LOAD_FAST | 6,656,280 | 15.6% |
| COMPARE_OP_INT | 4,413,760 | 10.3% |
| BINARY_OP_ADD_INT | 2,948,960 | 6.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,375,680 | 48.1% |
| STORE_FAST | 1,034,240 | 21.0% |
| RESUME_CHECK | 747,480 | 15.1% |
| LOAD_ATTR_METHOD_NO_DICT | 255,940 | 5.2% |
| STORE_DEREF | 174,080 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,739,200 | 96.0% |
| CALL_PY_EXACT_ARGS | 174,000 | 3.5% |
| LOAD_ATTR | 22,400 | 0.5% |
| PUSH_NULL | 160 | 0.0% |
| CALL | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 115,712,220 | 23.4% |
| STORE_ATTR_SLOT | 60,743,720 | 12.3% |
| POP_JUMP_IF_FALSE | 60,550,880 | 12.2% |
| RESUME_CHECK | 52,960,320 | 10.7% |
| POP_JUMP_IF_TRUE | 31,048,000 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 218,787,440 | 44.2% |
| STORE_ATTR_SLOT | 50,462,000 | 10.2% |
| LOAD_ATTR_METHOD_NO_DICT | 35,946,560 | 7.3% |
| BINARY_OP_ADD_INT | 29,726,560 | 6.0% |
| COPY | 29,071,360 | 5.9% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 61,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 61,400 | 99.9% |
| TO_BOOL | 40 | 0.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,772,260 | 17.6% |
| STORE_ATTR_SLOT | 4,433,800 | 16.3% |
| NOP | 4,300,800 | 15.8% |
| POP_JUMP_IF_FALSE | 4,168,660 | 15.3% |
| RESUME_CHECK | 3,184,580 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 8,867,720 | 32.6% |
| BINARY_SUBSCR_LIST_INT | 4,321,160 | 15.9% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,106,140 | 15.1% |
| LOAD_ATTR_SLOT | 1,904,680 | 7.0% |
| LOAD_FAST | 1,484,800 | 5.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 2,140 | 32.2% |
| LOAD_ATTR_METHOD_NO_DICT | 1,860 | 28.0% |
| LOAD_FAST | 560 | 8.4% |
| STORE_FAST | 480 | 7.2% |
| POP_JUMP_IF_FALSE | 400 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,700 | 40.7% |
| LOAD_ATTR | 2,480 | 37.3% |
| LOAD_GLOBAL_BUILTIN | 620 | 9.3% |
| LOAD_FAST | 580 | 8.7% |
| CALL | 80 | 1.2% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 441,260 | 52.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 224,240 | 26.7% |
| MAKE_CELL | 174,080 | 20.7% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 665,520 | 79.3% |
| MAKE_CELL | 174,080 | 20.7% |
| RESUME | 80 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 20,839,160 | 20.3% |
| COMPARE_OP_INT | 19,169,580 | 18.7% |
| TO_BOOL_NONE | 16,277,520 | 15.8% |
| CONTAINS_OP | 11,295,340 | 11.0% |
| TO_BOOL_BOOL | 10,616,900 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,550,880 | 58.9% |
| RETURN_CONST | 18,728,960 | 18.2% |
| JUMP_FORWARD | 8,581,160 | 8.4% |
| LOAD_FAST_LOAD_FAST | 4,168,660 | 4.1% |
| LOAD_CONST | 2,396,440 | 2.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,423,360 | 97.9% |
| LOAD_ATTR_INSTANCE_VALUE | 20,480 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 10,220 | 0.7% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,443,840 | 99.3% |
| LOAD_FAST_LOAD_FAST | 10,240 | 0.7% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,433,600 | 99.3% |
| LOAD_ATTR_SLOT | 10,220 | 0.7% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,443,840 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 16,528,860 | 35.2% |
| TO_BOOL_BOOL | 12,073,220 | 25.7% |
| TO_BOOL_STR | 10,516,560 | 22.4% |
| TO_BOOL_NONE | 4,740,140 | 10.1% |
| CONTAINS_OP | 1,853,480 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,048,000 | 66.2% |
| ENTER_EXECUTOR | 13,422,700 | 28.6% |
| RETURN_CONST | 1,105,920 | 2.4% |
| POP_TOP | 1,064,960 | 2.3% |
| RETURN_VALUE | 133,120 | 0.3% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 18,728,960 | 43.5% |
| STORE_ATTR_SLOT | 18,073,480 | 42.0% |
| POP_TOP | 3,471,360 | 8.1% |
| ENTER_EXECUTOR | 1,606,040 | 3.7% |
| POP_JUMP_IF_TRUE | 1,105,920 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 21,237,760 | 49.4% |
| TO_BOOL_NONE | 13,989,340 | 32.5% |
| INTERPRETER_EXIT | 3,072,000 | 7.1% |
| COPY | 1,607,680 | 3.7% |
| STORE_FAST | 1,085,440 | 2.5% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 20,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 20,440 | 99.8% |
| CALL | 40 | 0.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,040 | 60.5% |
| LOAD_FAST_LOAD_FAST | 520 | 30.2% |
| SWAP | 160 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 860 | 50.0% |
| LOAD_FAST | 280 | 16.3% |
| LOAD_FAST_LOAD_FAST | 180 | 10.5% |
| RETURN_CONST | 120 | 7.0% |
| LOAD_CONST | 100 | 5.8% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 174,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 174,080 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 11,889,000 | 25.8% |
| RETURN_VALUE | 7,669,740 | 16.6% |
| LOAD_CONST | 7,250,000 | 15.7% |
| LOAD_FAST | 4,188,480 | 9.1% |
| FOR_ITER | 2,365,940 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,782,300 | 66.8% |
| LOAD_CONST | 5,570,560 | 12.1% |
| LOAD_FAST_LOAD_FAST | 4,772,260 | 10.4% |
| JUMP_FORWARD | 1,505,280 | 3.3% |
| ENTER_EXECUTOR | 1,125,380 | 2.4% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 4,262,220 | 100.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,653,040 | 62.2% |
| LOAD_GLOBAL_BUILTIN | 1,609,260 | 37.8% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 29,030,320 | 98.1% |
| BUILD_TUPLE | 553,240 | 1.9% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 29,030,240 | 98.1% |
| POP_TOP | 553,240 | 1.9% |
| STORE_ATTR | 160 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| FOR_ITER | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 80 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,440 | 70.6% |
| CACHE | 260 | 12.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 5.9% |
| MAKE_CELL | 80 | 3.9% |
| CALL_KW | 60 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,560 | 76.5% |
| LOAD_GLOBAL | 180 | 8.8% |
| LOAD_DEREF | 120 | 5.9% |
| LOAD_CONST | 80 | 3.9% |
| LOAD_FAST_LOAD_FAST | 60 | 2.9% |


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

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,726,560 | 91.0% |
| LOAD_CONST | 2,948,960 | 9.0% |
| BINARY_OP | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 29,030,320 | 88.8% |
| STORE_FAST | 2,222,020 | 6.8% |
| CALL_PY_EXACT_ARGS | 1,423,320 | 4.4% |
| CALL | 20 | 0.0% |


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

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,148,280 | 91.9% |
| CALL_LEN | 1,413,080 | 8.0% |
| LOAD_ATTR_SLOT | 10,200 | 0.1% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 13,598,680 | 77.4% |
| CALL_PY_EXACT_ARGS | 1,443,720 | 8.2% |
| LOAD_CONST | 1,413,100 | 8.0% |
| LOAD_FAST | 1,105,900 | 6.3% |
| COMPARE_OP_INT | 10,200 | 0.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,105,880 | 57.4% |
| LOAD_ATTR_SLOT | 778,120 | 40.4% |
| LOAD_FAST | 20,440 | 1.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20,440 | 1.1% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,607,640 | 83.5% |
| LOAD_FAST_LOAD_FAST | 204,780 | 10.6% |
| PUSH_NULL | 71,660 | 3.7% |
| RETURN_VALUE | 20,460 | 1.1% |
| CALL_PY_WITH_DEFAULTS | 20,440 | 1.1% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 20,440 | 99.9% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,460 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,321,160 | 99.7% |
| LOAD_CONST | 10,200 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 580 | 0.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,280,280 | 98.8% |
| PUSH_EXC_INFO | 30,720 | 0.7% |
| LOAD_FAST_LOAD_FAST | 10,220 | 0.2% |
| POP_JUMP_IF_NONE | 10,220 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 580 | 0.0% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 13,598,680 | 48.1% |
| LOAD_ATTR_SLOT | 13,588,440 | 48.0% |
| LOAD_FAST | 1,105,880 | 3.9% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,187,160 | 96.1% |
| STORE_FAST | 1,105,900 | 3.9% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,227,140 | 91.8% |
| LOAD_ATTR_SLOT | 71,600 | 5.4% |
| LOAD_FAST | 20,400 | 1.5% |
| CALL_PY_EXACT_ARGS | 17,860 | 1.3% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,063,400 | 79.5% |
| MAKE_CELL | 224,240 | 16.8% |
| COPY_FREE_VARS | 31,520 | 2.4% |
| CALL_PY_EXACT_ARGS | 17,880 | 1.3% |
| RESUME | 120 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 40,920 | 66.6% |
| LOAD_FAST | 10,240 | 16.7% |
| LOAD_ATTR | 10,200 | 16.6% |
| CALL | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40,940 | 66.6% |
| GET_ITER | 10,280 | 16.7% |
| STORE_FAST | 10,220 | 16.6% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,920 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 40,920 | 100.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,413,080 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,413,100 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 6,860,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 6,860,800 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,742,540 | 46.6% |
| LOAD_GLOBAL_BUILTIN | 830,500 | 22.2% |
| LOAD_ATTR_MODULE | 634,680 | 17.0% |
| LOAD_ATTR_SLOT | 450,520 | 12.0% |
| BUILD_TUPLE | 81,880 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,217,960 | 86.0% |
| COPY | 522,200 | 14.0% |
| TO_BOOL | 160 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,556,200 | 98.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 10,200 | 0.6% |
| LOAD_ATTR_SLOT | 10,200 | 0.6% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 1,413,080 | 89.6% |
| STORE_FAST | 81,860 | 5.2% |
| LOAD_CONST | 40,940 | 2.6% |
| COMPARE_OP_INT | 20,400 | 1.3% |
| LOAD_FAST | 10,220 | 0.6% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,413,160 | 47.4% |
| ENTER_EXECUTOR | 1,392,320 | 46.7% |
| LOAD_FAST | 164,080 | 5.5% |
| RETURN_VALUE | 10,200 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,413,100 | 47.4% |
| ENTER_EXECUTOR | 1,402,540 | 47.1% |
| LOAD_FAST | 163,800 | 5.5% |
| JUMP_BACKWARD | 320 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,021,360 | 70.5% |
| LOAD_FAST | 2,037,820 | 15.9% |
| LOAD_ATTR_METHOD_NO_DICT | 819,480 | 6.4% |
| LOAD_ATTR | 819,160 | 6.4% |
| LOAD_CONST | 81,880 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,889,000 | 93.0% |
| CALL_PY_WITH_DEFAULTS | 819,160 | 6.4% |
| RETURN_VALUE | 81,900 | 0.6% |
| CALL | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 6,287,280 | 100.0% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,570,220 | 40.9% |
| TO_BOOL_BOOL | 1,433,480 | 22.8% |
| CALL_PY_EXACT_ARGS | 1,403,160 | 22.3% |
| LOAD_GLOBAL_MODULE | 819,160 | 13.0% |
| BINARY_SUBSCR_DICT | 20,440 | 0.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 10,769,420 | 26.9% |
| LOAD_FAST | 9,328,160 | 23.3% |
| LOAD_ATTR_METHOD_NO_DICT | 7,688,240 | 19.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,269,440 | 10.7% |
| LOAD_ATTR_SLOT | 1,494,960 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 39,462,620 | 98.7% |
| MAKE_CELL | 441,260 | 1.1% |
| COPY_FREE_VARS | 50,360 | 0.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 17,860 | 0.0% |
| CALL | 640 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,215,720 | 65.3% |
| LOAD_ATTR_METHOD_NO_DICT | 3,317,760 | 17.7% |
| LOAD_FAST | 1,474,440 | 7.9% |
| LOAD_ATTR | 849,800 | 4.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 819,160 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,708,000 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,600 | 99.9% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,640 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,208,240 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 604,140 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 604,120 | 50.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 28,303,240 | 86.4% |
| LOAD_CONST | 4,413,760 | 13.5% |
| LOAD_FAST_LOAD_FAST | 20,400 | 0.1% |
| CALL_LEN | 20,400 | 0.1% |
| BINARY_OP_SUBTRACT_INT | 10,200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 19,169,580 | 58.5% |
| LOAD_FAST | 13,598,700 | 41.5% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,464,560 | 78.1% |
| LOAD_FAST | 184,520 | 9.8% |
| LOAD_CONST | 143,480 | 7.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 81,880 | 4.4% |
| COMPARE_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,874,620 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 133,020 | 61.8% |
| ENTER_EXECUTOR | 81,200 | 37.7% |
| JUMP_BACKWARD | 900 | 0.4% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 102,060 | 47.4% |
| STORE_FAST | 82,100 | 38.2% |
| LOAD_FAST | 10,240 | 4.8% |
| LOAD_FAST_LOAD_FAST | 10,240 | 4.8% |
| RETURN_CONST | 10,220 | 4.7% |


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

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,922,240 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 6,860,800 | 99.1% |
| RETURN_VALUE | 20,480 | 0.3% |
| LOAD_FAST | 20,480 | 0.3% |
| POP_JUMP_IF_NONE | 20,480 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,946,560 | 60.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 9,860,920 | 16.5% |
| LOAD_ATTR_SLOT | 5,785,740 | 9.7% |
| LOAD_DEREF | 4,739,200 | 7.9% |
| LOAD_FAST_LOAD_FAST | 1,454,240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,074,020 | 45.4% |
| LOAD_GLOBAL_MODULE | 13,717,880 | 23.0% |
| CALL_PY_EXACT_ARGS | 7,688,240 | 12.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,287,280 | 10.5% |
| CALL_PY_WITH_DEFAULTS | 3,317,760 | 5.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,689,560 | 98.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 25,600 | 1.5% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,607,680 | 93.7% |
| LOAD_CONST | 81,900 | 4.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 25,600 | 1.5% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,118,760 | 100.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 634,680 | 29.9% |
| PUSH_NULL | 584,020 | 27.6% |
| LOAD_FAST | 419,720 | 19.8% |
| LOAD_FAST_LOAD_FAST | 307,000 | 14.5% |
| LOAD_ATTR | 92,100 | 4.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,662,880 | 81.1% |
| LOAD_FAST_LOAD_FAST | 4,106,140 | 18.9% |
| LOAD_ATTR | 760 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 9,860,920 | 45.3% |
| CONTAINS_OP | 5,498,960 | 25.3% |
| CALL_PY_EXACT_ARGS | 4,269,440 | 19.6% |
| STORE_FAST | 1,402,860 | 6.4% |
| LOAD_FAST | 593,860 | 2.7% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,013,520 | 34.8% |
| LOAD_FAST_LOAD_FAST | 962,620 | 33.0% |
| ENTER_EXECUTOR | 890,820 | 30.6% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 46,040 | 1.6% |
| LOAD_ATTR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 1,853,460 | 63.6% |
| LOAD_ATTR_METHOD_NO_DICT | 962,520 | 33.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 46,040 | 1.6% |
| LOAD_FAST | 20,440 | 0.7% |
| PUSH_NULL | 10,220 | 0.4% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,655,520 | 97.8% |
| LOAD_FAST_LOAD_FAST | 81,880 | 2.2% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,737,500 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 218,787,440 | 81.5% |
| COPY | 29,030,240 | 10.8% |
| LOAD_ATTR_SLOT | 17,863,080 | 6.7% |
| LOAD_FAST_LOAD_FAST | 1,904,680 | 0.7% |
| ENTER_EXECUTOR | 982,940 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 115,712,220 | 43.1% |
| COMPARE_OP_INT | 28,303,240 | 10.5% |
| LOAD_CONST | 20,080,960 | 7.5% |
| LOAD_ATTR_SLOT | 17,863,080 | 6.7% |
| TO_BOOL_ALWAYS_TRUE | 17,543,660 | 6.5% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,038,200 | 50.8% |
| LOAD_FAST | 2,243,580 | 14.2% |
| STORE_FAST_STORE_FAST | 1,609,260 | 10.2% |
| STORE_ATTR_SLOT | 1,433,480 | 9.1% |
| POP_JUMP_IF_FALSE | 984,060 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,481,820 | 91.5% |
| CALL_ISINSTANCE | 830,500 | 5.2% |
| LOAD_FAST_LOAD_FAST | 450,540 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 40,980 | 0.3% |
| CHECK_EXC_MATCH | 30,700 | 0.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 13,717,880 | 40.3% |
| LOAD_FAST | 10,517,820 | 30.9% |
| RESUME_CHECK | 4,341,600 | 12.8% |
| POP_JUMP_IF_FALSE | 1,484,920 | 4.4% |
| LOAD_ATTR_SLOT | 1,444,040 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 22,803,720 | 67.0% |
| LOAD_FAST | 4,300,760 | 12.6% |
| LOAD_FAST_LOAD_FAST | 2,816,280 | 8.3% |
| LOAD_ATTR_MODULE | 2,118,760 | 6.2% |
| CALL_ISINSTANCE | 1,742,540 | 5.1% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 39,462,620 | 52.0% |
| CALL_PY_WITH_DEFAULTS | 18,708,000 | 24.7% |
| CACHE | 11,120,500 | 14.7% |
| LOAD_ATTR_PROPERTY | 3,737,500 | 4.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,063,400 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,960,320 | 69.8% |
| LOAD_GLOBAL_BUILTIN | 8,038,200 | 10.6% |
| NOP | 5,119,960 | 6.8% |
| LOAD_GLOBAL_MODULE | 4,341,600 | 5.7% |
| LOAD_FAST_LOAD_FAST | 3,184,580 | 4.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,462,000 | 56.9% |
| SWAP | 29,030,240 | 32.8% |
| LOAD_FAST_LOAD_FAST | 8,867,720 | 10.0% |
| ENTER_EXECUTOR | 153,320 | 0.2% |
| STORE_ATTR_SLOT | 127,520 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,743,720 | 68.5% |
| RETURN_CONST | 18,073,480 | 20.4% |
| LOAD_FAST_LOAD_FAST | 4,433,800 | 5.0% |
| LOAD_CONST | 1,791,900 | 2.0% |
| ENTER_EXECUTOR | 1,555,200 | 1.8% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,200 | 99.8% |
| STORE_SUBSCR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,220 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 17,543,660 | 68.8% |
| LOAD_FAST | 7,804,900 | 30.6% |
| COPY | 126,540 | 0.5% |
| TO_BOOL_NONE | 29,220 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 1,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 16,528,860 | 64.8% |
| POP_JUMP_IF_FALSE | 8,946,440 | 35.1% |
| TO_BOOL_NONE | 29,200 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 1,240 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,164,880 | 40.1% |
| LOAD_FAST | 6,471,740 | 28.3% |
| CALL_ISINSTANCE | 3,217,960 | 14.1% |
| COPY | 1,576,060 | 6.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,433,480 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 12,073,220 | 52.8% |
| POP_JUMP_IF_FALSE | 10,616,900 | 46.4% |
| EXTENDED_ARG | 112,500 | 0.5% |
| UNARY_NOT | 61,420 | 0.3% |
| TO_BOOL_NONE | 12,100 | 0.1% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 8,949,680 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,939,500 | 99.9% |
| EXTENDED_ARG | 10,220 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 40,920 | 67.2% |
| LOAD_FAST | 19,740 | 32.4% |
| TO_BOOL_NONE | 180 | 0.3% |
| TO_BOOL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 40,940 | 67.2% |
| POP_JUMP_IF_FALSE | 19,760 | 32.5% |
| TO_BOOL_NONE | 180 | 0.3% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 13,989,340 | 65.1% |
| LOAD_FAST | 5,793,800 | 26.9% |
| COPY | 1,266,240 | 5.9% |
| LOAD_ATTR_SLOT | 283,900 | 1.3% |
| LOAD_FAST_CHECK | 61,400 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,277,520 | 75.7% |
| POP_JUMP_IF_TRUE | 4,740,140 | 22.0% |
| EXTENDED_ARG | 440,380 | 2.0% |
| TO_BOOL_ALWAYS_TRUE | 29,220 | 0.1% |
| TO_BOOL_BOOL | 12,140 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 8,939,480 | 64.6% |
| LOAD_FAST | 4,813,120 | 34.8% |
| RETURN_VALUE | 81,880 | 0.6% |
| COPY | 10,200 | 0.1% |
| TO_BOOL_NONE | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 10,516,560 | 76.0% |
| POP_JUMP_IF_FALSE | 3,328,260 | 24.0% |
| TO_BOOL_NONE | 1,460 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 2,582,580 | 60.6% |
| RETURN_VALUE | 1,679,560 | 39.4% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 4,262,220 | 100.0% |


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
|     deferred | 440 | 0.0% |
|          hit | 51,844,680 | 100.0% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
| Failure | 0 | 0.0% |


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
|     deferred | 41,560 | 0.1% |
|          hit | 34,539,240 | 99.9% |
|         miss | 31,300 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 860 | 84.3% |
| Failure | 160 | 15.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 160 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,433,380 | 3.1% |
|          hit | 106,415,400 | 96.8% |
|         miss | 1,948,460 | 1.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 42,080 | 95.4% |
| Failure | 2,040 | 4.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bound method | 640 | 31.4% |
| no dict | 540 | 26.5% |
| cfunc noargs | 340 | 16.7% |
| meth descr varargs | 200 | 9.8% |
| code complex parameters | 160 | 7.8% |
| metaclass | 160 | 7.8% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 22,016,780 | 37.2% |
|          hit | 37,191,220 | 62.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 6.1% |
| Failure | 7,040 | 93.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 6,560 | 93.2% |
| different types | 460 | 6.5% |
| list | 20 | 0.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,951,480 | 95.8% |
|          hit | 215,660 | 4.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 4.6% |
| Failure | 2,080 | 95.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 960 | 46.2% |
| ascii string | 540 | 26.0% |
| dict keys | 420 | 20.2% |
| enumerate | 160 | 7.7% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 31,054,880 | 7.1% |
|          hit | 403,223,920 | 92.8% |
|         miss | 6,239,260 | 1.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 126,540 | 82.9% |
| Failure | 26,140 | 17.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 22,540 | 86.2% |
| method | 3,260 | 12.5% |
| mutable class | 340 | 1.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,480 | 0.0% |
|          hit | 49,878,600 | 100.0% |
|         miss | 4,240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,400 | 100.0% |
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
|     deferred | 6,632,440 | 6.8% |
|          hit | 90,872,840 | 93.1% |
|         miss | 6,759,100 | 6.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 128,380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.2% |
|          hit | 10,220 | 99.6% |

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
|     deferred | 4,564,020 | 4.4% |
|          hit | 98,112,460 | 95.5% |
|         miss | 4,637,720 | 4.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 90,420 | 99.8% |
| Failure | 160 | 0.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 160 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 9,512,880 | 100.0% |

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
| Basic | 873,038,660 | 44.1% |
| Not specialized | 209,658,760 | 10.6% |
| Specialized hits | 877,443,760 | 44.3% |
| Specialized misses | 19,624,360 | 1.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 31,054,880 | 42.7% |
| COMPARE_OP | 22,016,780 | 30.3% |
| STORE_ATTR | 6,632,440 | 9.1% |
| FOR_ITER | 4,951,480 | 6.8% |
| TO_BOOL | 4,564,020 | 6.3% |
| CALL | 3,433,380 | 4.7% |
| BINARY_SUBSCR | 41,560 | 0.1% |
| LOAD_GLOBAL | 7,480 | 0.0% |
| BINARY_OP | 440 | 0.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 6,759,100 | 34.4% |
| LOAD_ATTR_SLOT | 2,441,000 | 12.4% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,440,820 | 12.4% |
| TO_BOOL_NONE | 2,289,240 | 11.7% |
| TO_BOOL_ALWAYS_TRUE | 1,616,420 | 8.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,357,340 | 6.9% |
| CALL_PY_EXACT_ARGS | 999,320 | 5.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 949,140 | 4.8% |
| TO_BOOL_BOOL | 645,140 | 3.3% |
| TO_BOOL_STR | 77,380 | 0.4% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 11,120,760 | 14.4% |
| Calls to Python functions inlined | 66,232,360 | 85.6% |
| Calls via PyEval_EvalFrame (total) | 11,120,760 | 14.4% |
| Calls via PyEval_EvalFrame (vector) | 11,120,760 | 14.4% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 11,120,760 | 14.4% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,126,420 | 1.5% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 6,860,900 | 8.9% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 30,720 | 0.0% |
| Frames pushed | 77,353,120 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 15,950,920 | 20.5% |
| Frees to freelist | 15,954,780 |  |
| Allocations | 61,903,280 | 79.5% |
| Allocations to 512 bytes | 61,903,080 | 79.5% |
| Allocations to 4 kbytes | 200 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 61,627,158 |  |
| New values | 1,617,920 |  |
| Interpreter increfs | 972,655,000 | 80.7% |
| Interpreter decrefs | 1,087,849,020 | 85.1% |
| Increfs | 232,307,033 | 19.3% |
| Decrefs | 190,436,714 | 14.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 62,798,339 |  |
| Method cache misses | 889,801 |  |
| Method cache collisions | 973,622 |  |
| Method cache dunder hits | 20,159,877 |  |
| Method cache dunder misses | 84,703 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 4,000 | 1,309,560 | 23,015,960 |
| 1 | 360 | 1,052,940 | 8,869,800 |
| 2 | 20 | 44,280 | 4,268,040 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 740 |  |
| Traces created | 740 | 100.0% |
| Trace stack overflow | 260 | 35.1% |
| Trace stack underflow | 20 | 2.7% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 20 | 2.7% |
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
| <= 16 | 80 | 10.8% |
| <= 32 | 100 | 13.5% |
| <= 64 | 260 | 35.1% |
| <= 128 | 140 | 18.9% |
| <= 256 | 80 | 10.8% |
| <= 512 | 80 | 10.8% |


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
| <= 16 | 60 | 8.1% |
| <= 32 | 240 | 32.4% |
| <= 64 | 40 | 5.4% |


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
| CALL_PY_WITH_DEFAULTS | 60 |
| CALL_LIST_APPEND | 40 |
| BINARY_OP_INPLACE_ADD_UNICODE | 20 |
| CALL | 20 |


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
