
# Pystats results

- benchmark: sqlglot_parse
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 552,458,560 | 25.1% | 25.1% |  |
| LOAD_ATTR_SLOT | 287,371,420 | 13.1% | 38.2% | 0.9% |
| POP_JUMP_IF_FALSE | 117,780,480 | 5.4% | 43.6% |  |
| STORE_ATTR_SLOT | 97,633,220 | 4.4% | 48.0% | 7.0% |
| LOAD_ATTR_METHOD_NO_DICT | 79,242,440 | 3.6% | 51.6% |  |
| RESUME_CHECK | 77,351,080 | 3.5% | 55.2% | 0.0% |
| STORE_FAST | 53,934,200 | 2.5% | 57.6% |  |
| POP_JUMP_IF_TRUE | 49,776,640 | 2.3% | 59.9% |  |
| LOAD_CONST | 46,592,080 | 2.1% | 62.0% |  |
| RETURN_CONST | 43,028,480 | 2.0% | 64.0% |  |
| CALL_PY_EXACT_ARGS | 41,488,000 | 1.9% | 65.9% | 2.4% |
| LOAD_GLOBAL_MODULE | 38,346,200 | 1.7% | 67.6% | 0.0% |
| LOAD_FAST_LOAD_FAST | 34,560,000 | 1.6% | 69.2% |  |
| RETURN_VALUE | 34,324,640 | 1.6% | 70.7% |  |
| COMPARE_OP_INT | 34,027,240 | 1.5% | 72.3% |  |
| BINARY_OP_ADD_INT | 32,675,680 | 1.5% | 73.8% |  |
| COPY | 32,051,200 | 1.5% | 75.2% |  |
| SWAP | 30,433,280 | 1.4% | 76.6% |  |
| BINARY_SUBSCR_STR_INT | 28,293,060 | 1.3% | 77.9% |  |
| TO_BOOL_BOOL | 27,675,000 | 1.3% | 79.2% | 2.3% |
| LOAD_ATTR | 26,371,240 | 1.2% | 80.4% |  |
| TO_BOOL_ALWAYS_TRUE | 25,505,740 | 1.2% | 81.5% | 6.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 25,353,480 | 1.2% | 82.7% |  |
| JUMP_BACKWARD | 25,036,800 | 1.1% | 83.8% |  |
| POP_TOP | 24,207,520 | 1.1% | 84.9% |  |
| COMPARE_OP | 23,427,220 | 1.1% | 86.0% |  |
| TO_BOOL_NONE | 21,501,040 | 1.0% | 87.0% | 10.6% |
| LOAD_GLOBAL_BUILTIN | 19,844,640 | 0.9% | 87.9% | 0.0% |
| TO_BOOL_STR | 19,057,800 | 0.9% | 88.7% | 0.4% |
| CONTAINS_OP | 19,046,400 | 0.9% | 89.6% |  |
| CALL_PY_WITH_DEFAULTS | 18,708,000 | 0.9% | 90.5% |  |
| BINARY_OP_SUBTRACT_INT | 17,571,700 | 0.8% | 91.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 17,284,940 | 0.8% | 92.0% |  |
| FOR_ITER | 16,081,860 | 0.7% | 92.8% |  |
| INTERPRETER_EXIT | 11,120,760 | 0.5% | 93.3% |  |
| EXTENDED_ARG | 9,994,240 | 0.5% | 93.7% |  |
| JUMP_FORWARD | 9,840,640 | 0.4% | 94.2% |  |
| STORE_FAST_STORE_FAST | 9,512,960 | 0.4% | 94.6% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,512,880 | 0.4% | 95.0% |  |
| TO_BOOL_INT | 8,949,720 | 0.4% | 95.5% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 7,393,080 | 0.3% | 95.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 6,922,260 | 0.3% | 96.1% | 0.0% |
| CALL_BUILTIN_O | 6,860,800 | 0.3% | 96.4% |  |
| CALL_ISINSTANCE | 6,635,320 | 0.3% | 96.7% |  |
| GET_ITER | 6,185,040 | 0.3% | 97.0% |  |
| NOP | 6,031,440 | 0.3% | 97.3% |  |
| LOAD_DEREF | 4,935,920 | 0.2% | 97.5% |  |
| BINARY_SUBSCR_LIST_INT | 4,332,020 | 0.2% | 97.7% | 0.7% |
| PUSH_NULL | 4,034,800 | 0.2% | 97.9% |  |
| LOAD_ATTR_PROPERTY | 3,737,500 | 0.2% | 98.1% |  |
| BINARY_SLICE | 3,573,760 | 0.2% | 98.2% |  |
| COMPARE_OP_STR | 3,163,980 | 0.1% | 98.4% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,995,020 | 0.1% | 98.5% | 81.5% |
| CALL_LIST_APPEND | 2,979,760 | 0.1% | 98.6% |  |
| CALL | 2,942,660 | 0.1% | 98.8% |  |
| BUILD_TUPLE | 2,662,400 | 0.1% | 98.9% |  |
| LOAD_ATTR_MODULE | 2,129,300 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_DICT | 1,925,000 | 0.1% | 99.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,715,180 | 0.1% | 99.1% | 79.1% |
| CALL_KW | 1,607,680 | 0.1% | 99.2% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 1,576,920 | 0.1% | 99.3% |  |
| CALL_LEN | 1,576,780 | 0.1% | 99.4% |  |
| POP_JUMP_IF_NONE | 1,454,080 | 0.1% | 99.4% |  |
| POP_JUMP_IF_NOT_NONE | 1,443,840 | 0.1% | 99.5% |  |
| BINARY_SUBSCR | 1,403,980 | 0.1% | 99.6% |  |
| BUILD_LIST | 1,382,480 | 0.1% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,337,160 | 0.1% | 99.7% | 71.0% |
| CALL_TYPE_1 | 1,208,280 | 0.1% | 99.7% |  |
| CALL_FUNCTION_EX | 1,013,920 | 0.0% | 99.8% |  |
| DICT_MERGE | 1,013,760 | 0.0% | 99.8% |  |
| BUILD_MAP | 1,003,520 | 0.0% | 99.9% |  |
| MAKE_CELL | 839,680 | 0.0% | 99.9% |  |
| IS_OP | 604,160 | 0.0% | 99.9% |  |
| FOR_ITER_LIST | 368,560 | 0.0% | 100.0% |  |
| STORE_DEREF | 174,080 | 0.0% | 100.0% |  |
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
| FOR_ITER_RANGE | 10,300 | 0.0% | 100.0% |  |
| DICT_UPDATE | 10,240 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 10,220 | 0.0% | 100.0% | 0.6% |
| BINARY_OP_SUBTRACT_FLOAT | 10,220 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 10,220 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 6,640 | 0.0% | 100.0% |  |
| RESUME | 2,040 | 0.0% | 100.0% | 206.9% |
| STORE_ATTR | 1,720 | 0.0% | 100.0% |  |
| BINARY_OP | 760 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_SLOT | 238,158,480 | 10.8% | 10.8% |
| LOAD_ATTR_SLOT LOAD_FAST | 125,111,900 | 5.7% | 16.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 74,045,440 | 3.4% | 19.9% |
| STORE_ATTR_SLOT LOAD_FAST | 69,672,680 | 3.2% | 23.1% |
| LOAD_FAST STORE_ATTR_SLOT | 59,390,960 | 2.7% | 25.8% |
| RESUME_CHECK LOAD_FAST | 54,475,240 | 2.5% | 28.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 48,571,600 | 2.2% | 30.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 40,977,540 | 1.9% | 32.3% |
| STORE_FAST LOAD_FAST | 36,382,760 | 1.7% | 34.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 32,204,800 | 1.5% | 35.5% |
| LOAD_FAST BINARY_OP_ADD_INT | 29,726,560 | 1.4% | 36.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 29,264,600 | 1.3% | 38.1% |
| LOAD_FAST COPY | 29,071,360 | 1.3% | 39.5% |
| BINARY_OP_ADD_INT SWAP | 29,030,320 | 1.3% | 40.8% |
| COPY LOAD_ATTR_SLOT | 29,030,240 | 1.3% | 42.1% |
| SWAP STORE_ATTR_SLOT | 29,030,240 | 1.3% | 43.4% |
| LOAD_ATTR_SLOT COMPARE_OP_INT | 28,303,240 | 1.3% | 44.7% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 27,187,160 | 1.2% | 46.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 24,206,280 | 1.1% | 47.1% |
| COMPARE_OP POP_JUMP_IF_FALSE | 22,241,700 | 1.0% | 48.1% |
| LOAD_ATTR_SLOT LOAD_CONST | 21,882,600 | 1.0% | 49.1% |
| RETURN_CONST POP_TOP | 21,237,760 | 1.0% | 50.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 20,418,320 | 0.9% | 51.0% |
| POP_JUMP_IF_FALSE RETURN_CONST | 18,728,960 | 0.9% | 51.8% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 18,708,000 | 0.9% | 52.7% |
| STORE_ATTR_SLOT RETURN_CONST | 18,073,480 | 0.8% | 53.5% |
| LOAD_ATTR_SLOT LOAD_ATTR_SLOT | 17,866,500 | 0.8% | 54.3% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 17,662,880 | 0.8% | 55.1% |
| LOAD_ATTR_SLOT TO_BOOL_ALWAYS_TRUE | 17,543,660 | 0.8% | 55.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 17,376,820 | 0.8% | 56.7% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 16,528,860 | 0.8% | 57.5% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 16,383,860 | 0.7% | 58.2% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 16,277,520 | 0.7% | 58.9% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 16,148,280 | 0.7% | 59.7% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 15,984,640 | 0.7% | 60.4% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_WITH_DEFAULTS | 15,533,480 | 0.7% | 61.1% |
| JUMP_BACKWARD LOAD_FAST | 14,766,080 | 0.7% | 61.8% |
| RETURN_CONST TO_BOOL_NONE | 13,989,340 | 0.6% | 62.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 13,758,400 | 0.6% | 63.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 13,730,580 | 0.6% | 63.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 13,717,880 | 0.6% | 64.3% |
| COMPARE_OP_INT LOAD_FAST | 13,598,700 | 0.6% | 64.9% |
| BINARY_OP_SUBTRACT_INT BINARY_SUBSCR_STR_INT | 13,598,680 | 0.6% | 65.5% |
| LOAD_ATTR_SLOT BINARY_SUBSCR_STR_INT | 13,588,440 | 0.6% | 66.1% |
| POP_TOP LOAD_FAST | 12,482,600 | 0.6% | 66.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 12,297,760 | 0.6% | 67.3% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 11,622,160 | 0.5% | 67.8% |
| LOAD_FAST COMPARE_OP | 11,366,480 | 0.5% | 68.3% |
| CACHE RESUME_CHECK | 11,120,500 | 0.5% | 68.8% |
| LOAD_ATTR COMPARE_OP | 10,895,480 | 0.5% | 69.3% |
| LOAD_ATTR CALL_PY_EXACT_ARGS | 10,769,420 | 0.5% | 69.8% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 10,280,600 | 0.5% | 70.3% |
| JUMP_BACKWARD FOR_ITER | 10,025,040 | 0.5% | 70.7% |
| LOAD_FAST TO_BOOL_STR | 10,024,640 | 0.5% | 71.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT LOAD_ATTR_METHOD_NO_DICT | 9,860,920 | 0.4% | 71.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 9,737,480 | 0.4% | 72.1% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 9,574,200 | 0.4% | 72.5% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 9,512,880 | 0.4% | 73.0% |
| EXTENDED_ARG JUMP_BACKWARD | 9,400,320 | 0.4% | 73.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT CONTAINS_OP | 9,082,660 | 0.4% | 73.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 9,082,360 | 0.4% | 74.2% |
| LOAD_ATTR_SLOT CALL_METHOD_DESCRIPTOR_FAST | 9,021,360 | 0.4% | 74.6% |
| LOAD_ATTR_SLOT TO_BOOL_INT | 8,949,680 | 0.4% | 75.0% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 8,946,440 | 0.4% | 75.4% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 8,939,500 | 0.4% | 75.8% |
| LOAD_ATTR_SLOT TO_BOOL_STR | 8,939,480 | 0.4% | 76.3% |
| POP_JUMP_IF_TRUE EXTENDED_ARG | 8,929,280 | 0.4% | 76.7% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 8,898,560 | 0.4% | 77.1% |
| RETURN_VALUE INTERPRETER_EXIT | 8,048,760 | 0.4% | 77.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 8,038,200 | 0.4% | 77.8% |
| LOAD_FAST TO_BOOL_BOOL | 7,966,280 | 0.4% | 78.2% |
| LOAD_FAST TO_BOOL_ALWAYS_TRUE | 7,804,900 | 0.4% | 78.5% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 7,689,840 | 0.4% | 78.9% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 7,688,240 | 0.3% | 79.2% |
| RETURN_VALUE STORE_FAST | 7,669,740 | 0.3% | 79.6% |
| RETURN_VALUE RETURN_VALUE | 7,639,120 | 0.3% | 79.9% |
| LOAD_CONST LOAD_FAST | 7,505,920 | 0.3% | 80.3% |
| TO_BOOL_STR POP_JUMP_IF_FALSE | 7,434,180 | 0.3% | 80.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 7,392,880 | 0.3% | 80.9% |
| LOAD_CONST STORE_FAST | 7,250,000 | 0.3% | 81.3% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 6,983,600 | 0.3% | 81.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,922,240 | 0.3% | 81.9% |
| CALL_BUILTIN_O RETURN_VALUE | 6,860,800 | 0.3% | 82.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_O | 6,860,800 | 0.3% | 82.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 6,850,560 | 0.3% | 82.8% |
| STORE_FAST_STORE_FAST LOAD_FAST | 6,277,120 | 0.3% | 83.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 6,112,960 | 0.3% | 83.4% |
| GET_ITER FOR_ITER | 6,051,960 | 0.3% | 83.7% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 6,041,600 | 0.3% | 83.9% |
| LOAD_FAST RETURN_VALUE | 5,939,280 | 0.3% | 84.2% |
| LOAD_FAST LOAD_CONST | 5,928,960 | 0.3% | 84.5% |
| LOAD_FAST TO_BOOL_NONE | 5,793,800 | 0.3% | 84.7% |
| LOAD_CONST COMPARE_OP_INT | 5,672,720 | 0.3% | 85.0% |
| STORE_FAST LOAD_CONST | 5,570,560 | 0.3% | 85.3% |
| LOAD_FAST CONTAINS_OP | 5,509,120 | 0.3% | 85.5% |
| LOAD_FAST STORE_FAST | 5,294,080 | 0.2% | 85.7% |
| RESUME_CHECK NOP | 5,119,960 | 0.2% | 86.0% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_FAST | 4,925,400 | 0.2% | 86.2% |
| RETURN_VALUE LOAD_FAST | 4,853,740 | 0.2% | 86.4% |
| TO_BOOL_NONE POP_JUMP_IF_TRUE | 4,740,140 | 0.2% | 86.6% |


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
| LOAD_ATTR_SLOT | 471,000 | 29.9% |
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
| LOAD_CONST | 1,402,920 | 99.9% |
| BINARY_SUBSCR | 540 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,402,840 | 99.9% |
| BINARY_SUBSCR | 540 | 0.0% |
| BINARY_SUBSCR_DICT | 120 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 80 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |


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
| LOAD_FAST | 2,621,440 | 42.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,570,220 | 41.6% |
| LOAD_ATTR_SLOT | 982,980 | 15.9% |
| CALL_BUILTIN_CLASS | 10,280 | 0.2% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 6,051,960 | 97.8% |
| FOR_ITER_LIST | 133,020 | 2.2% |
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
| RETURN_CONST | 21,237,760 | 87.7% |
| SWAP | 1,402,880 | 5.8% |
| POP_JUMP_IF_TRUE | 1,064,960 | 4.4% |
| POP_JUMP_IF_FALSE | 481,280 | 2.0% |
| RETURN_VALUE | 20,480 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,482,600 | 51.6% |
| JUMP_FORWARD | 4,126,720 | 17.0% |
| RETURN_CONST | 3,471,360 | 14.3% |
| LOAD_CONST | 1,607,680 | 6.6% |
| RETURN_VALUE | 1,402,880 | 5.8% |


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
| LOAD_FAST | 3,092,480 | 76.6% |
| LOAD_ATTR_MODULE | 593,860 | 14.7% |
| LOAD_FAST_LOAD_FAST | 204,800 | 5.1% |
| BINARY_SUBSCR_DICT | 71,660 | 1.8% |
| LOAD_ATTR | 51,360 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 1,227,140 | 30.4% |
| CALL_PY_EXACT_ARGS | 1,024,820 | 25.4% |
| LOAD_CONST | 983,040 | 24.4% |
| LOAD_FAST | 583,840 | 14.5% |
| LOAD_FAST_LOAD_FAST | 71,680 | 1.8% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,639,120 | 22.3% |
| CALL_BUILTIN_O | 6,860,800 | 20.0% |
| LOAD_FAST | 5,939,280 | 17.3% |
| BINARY_SUBSCR_LIST_INT | 4,280,280 | 12.5% |
| BINARY_SLICE | 3,573,760 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 8,048,760 | 23.4% |
| STORE_FAST | 7,669,740 | 22.3% |
| RETURN_VALUE | 7,639,120 | 22.3% |
| LOAD_FAST | 4,853,740 | 14.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,529,200 | 7.4% |


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
| FOR_ITER | 10,240 | 0.7% |

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
| LOAD_FAST | 2,539,520 | 95.4% |
| LOAD_GLOBAL_MODULE | 81,900 | 3.1% |
| POP_JUMP_IF_FALSE | 20,480 | 0.8% |
| LOAD_ATTR_MODULE | 20,460 | 0.8% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,402,880 | 52.7% |
| RETURN_VALUE | 1,126,400 | 42.3% |
| CALL_ISINSTANCE | 81,880 | 3.1% |
| LOAD_CONST | 20,480 | 0.8% |
| LOAD_FAST | 20,480 | 0.8% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,474,800 | 50.1% |
| LOAD_ATTR_SLOT | 1,413,260 | 48.0% |
| PUSH_NULL | 31,640 | 1.1% |
| LOAD_GLOBAL_MODULE | 10,260 | 0.3% |
| LOAD_ATTR | 5,460 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,423,380 | 48.4% |
| CALL_LIST_APPEND | 1,413,160 | 48.0% |
| TO_BOOL_BOOL | 61,400 | 2.1% |
| STORE_FAST | 20,700 | 0.7% |
| RESUME_CHECK | 13,640 | 0.5% |


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
| LOAD_FAST | 11,366,480 | 48.5% |
| LOAD_ATTR | 10,895,480 | 46.5% |
| BUILD_LIST | 1,157,120 | 4.9% |
| COMPARE_OP | 7,420 | 0.0% |
| LOAD_CONST | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 22,241,700 | 94.9% |
| POP_JUMP_IF_TRUE | 1,157,140 | 4.9% |
| STORE_FAST | 20,480 | 0.1% |
| COMPARE_OP | 7,420 | 0.0% |
| COMPARE_OP_INT | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 9,082,660 | 47.7% |
| LOAD_FAST | 5,509,120 | 28.9% |
| LOAD_FAST_LOAD_FAST | 2,508,800 | 13.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,935,340 | 10.2% |
| LOAD_CONST | 10,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 15,984,640 | 83.9% |
| POP_JUMP_IF_TRUE | 1,935,360 | 10.2% |
| STORE_FAST | 1,126,400 | 5.9% |


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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 8,929,280 | 89.3% |
| POP_TOP | 471,040 | 4.7% |
| TO_BOOL_NONE | 440,380 | 4.4% |
| TO_BOOL_BOOL | 112,500 | 1.1% |
| STORE_FAST | 30,720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 9,400,320 | 94.1% |
| POP_JUMP_IF_FALSE | 552,960 | 5.5% |
| JUMP_FORWARD | 30,720 | 0.3% |
| POP_JUMP_IF_TRUE | 10,240 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,025,040 | 62.3% |
| GET_ITER | 6,051,960 | 37.6% |
| FOR_ITER | 4,860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 6,983,600 | 43.4% |
| STORE_FAST | 4,444,240 | 27.6% |
| LOAD_FAST | 1,925,120 | 12.0% |
| RETURN_CONST | 1,607,700 | 10.0% |
| LOAD_CONST | 1,105,920 | 6.9% |


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
| EXTENDED_ARG | 9,400,320 | 37.5% |
| POP_JUMP_IF_TRUE | 6,041,600 | 24.1% |
| JUMP_FORWARD | 4,106,240 | 16.4% |
| STORE_ATTR_SLOT | 1,587,160 | 6.3% |
| CALL_LIST_APPEND | 1,402,860 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,766,080 | 59.0% |
| FOR_ITER | 10,025,040 | 40.0% |
| FOR_ITER_LIST | 235,460 | 0.9% |
| FOR_ITER_RANGE | 10,220 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,126,720 | 41.9% |
| POP_JUMP_IF_FALSE | 2,283,520 | 23.2% |
| STORE_FAST | 1,505,280 | 15.3% |
| RETURN_VALUE | 1,351,660 | 13.7% |
| STORE_ATTR_SLOT | 409,580 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,218,880 | 42.9% |
| JUMP_BACKWARD | 4,106,240 | 41.7% |
| STORE_FAST | 1,464,320 | 14.9% |
| LOAD_DEREF | 30,720 | 0.3% |
| CALL_PY_EXACT_ARGS | 20,460 | 0.2% |


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
| LOAD_GLOBAL_MODULE | 24,206,280 | 91.8% |
| LOAD_FAST | 2,019,000 | 7.7% |
| LOAD_ATTR_MODULE | 92,100 | 0.3% |
| LOAD_ATTR | 27,260 | 0.1% |
| LOAD_DEREF | 22,400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 10,895,480 | 41.3% |
| CALL_PY_EXACT_ARGS | 10,769,420 | 40.8% |
| LOAD_FAST | 1,957,800 | 7.4% |
| LOAD_GLOBAL_MODULE | 900,920 | 3.4% |
| CALL_PY_WITH_DEFAULTS | 849,800 | 3.2% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 21,882,600 | 47.0% |
| LOAD_FAST | 5,928,960 | 12.7% |
| STORE_FAST | 5,570,560 | 12.0% |
| POP_JUMP_IF_FALSE | 3,246,080 | 7.0% |
| STORE_ATTR_SLOT | 1,791,900 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 16,148,280 | 34.7% |
| LOAD_FAST | 7,505,920 | 16.1% |
| STORE_FAST | 7,250,000 | 15.6% |
| COMPARE_OP_INT | 5,672,720 | 12.2% |
| BINARY_OP_ADD_INT | 2,948,960 | 6.3% |


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
| LOAD_ATTR_SLOT | 125,111,900 | 22.6% |
| POP_JUMP_IF_FALSE | 74,045,440 | 13.4% |
| STORE_ATTR_SLOT | 69,672,680 | 12.6% |
| RESUME_CHECK | 54,475,240 | 9.9% |
| STORE_FAST | 36,382,760 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 238,158,480 | 43.1% |
| STORE_ATTR_SLOT | 59,390,960 | 10.8% |
| LOAD_ATTR_METHOD_NO_DICT | 48,571,600 | 8.8% |
| BINARY_OP_ADD_INT | 29,726,560 | 5.4% |
| COPY | 29,071,360 | 5.3% |


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
| POP_JUMP_IF_FALSE | 8,898,560 | 25.7% |
| STORE_FAST | 6,850,560 | 19.8% |
| STORE_ATTR_SLOT | 4,464,460 | 12.9% |
| NOP | 4,300,800 | 12.4% |
| LOAD_GLOBAL_MODULE | 3,921,880 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 9,082,360 | 26.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 7,689,840 | 22.3% |
| BINARY_SUBSCR_LIST_INT | 4,321,160 | 12.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,559,840 | 7.4% |
| CONTAINS_OP | 2,508,800 | 7.3% |


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
| COMPARE_OP | 22,241,700 | 18.9% |
| COMPARE_OP_INT | 20,418,320 | 17.3% |
| TO_BOOL_NONE | 16,277,520 | 13.8% |
| CONTAINS_OP | 15,984,640 | 13.6% |
| TO_BOOL_BOOL | 13,758,400 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,045,440 | 62.9% |
| RETURN_CONST | 18,728,960 | 15.9% |
| LOAD_FAST_LOAD_FAST | 8,898,560 | 7.6% |
| LOAD_CONST | 3,246,080 | 2.8% |
| LOAD_GLOBAL_MODULE | 2,590,520 | 2.2% |


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
| TO_BOOL_ALWAYS_TRUE | 16,528,860 | 33.2% |
| TO_BOOL_BOOL | 13,730,580 | 27.6% |
| TO_BOOL_STR | 11,622,160 | 23.3% |
| TO_BOOL_NONE | 4,740,140 | 9.5% |
| CONTAINS_OP | 1,935,360 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,204,800 | 64.7% |
| EXTENDED_ARG | 8,929,280 | 17.9% |
| JUMP_BACKWARD | 6,041,600 | 12.1% |
| RETURN_CONST | 1,105,920 | 2.2% |
| POP_TOP | 1,064,960 | 2.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 18,728,960 | 43.5% |
| STORE_ATTR_SLOT | 18,073,480 | 42.0% |
| POP_TOP | 3,471,360 | 8.1% |
| FOR_ITER | 1,607,700 | 3.7% |
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
| CALL_METHOD_DESCRIPTOR_FAST | 16,383,860 | 30.4% |
| RETURN_VALUE | 7,669,740 | 14.2% |
| LOAD_CONST | 7,250,000 | 13.4% |
| LOAD_FAST | 5,294,080 | 9.8% |
| FOR_ITER | 4,444,240 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,382,760 | 67.5% |
| LOAD_FAST_LOAD_FAST | 6,850,560 | 12.7% |
| LOAD_CONST | 5,570,560 | 10.3% |
| JUMP_FORWARD | 1,505,280 | 2.8% |
| JUMP_BACKWARD | 1,126,400 | 2.1% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 9,512,880 | 100.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,277,120 | 66.0% |
| LOAD_GLOBAL_BUILTIN | 3,235,840 | 34.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 29,030,320 | 95.4% |
| BUILD_TUPLE | 1,402,880 | 4.6% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 29,030,240 | 95.4% |
| POP_TOP | 1,402,880 | 4.6% |
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
| LOAD_GLOBAL_MODULE | 3,522,480 | 53.1% |
| LOAD_GLOBAL_BUILTIN | 1,945,560 | 29.3% |
| LOAD_ATTR_MODULE | 634,680 | 9.6% |
| LOAD_ATTR_SLOT | 450,520 | 6.8% |
| BUILD_TUPLE | 81,880 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,112,960 | 92.1% |
| COPY | 522,200 | 7.9% |
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
| LOAD_FAST | 1,556,400 | 52.2% |
| CALL | 1,413,160 | 47.4% |
| RETURN_VALUE | 10,200 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,413,100 | 47.4% |
| JUMP_BACKWARD | 1,402,860 | 47.1% |
| LOAD_FAST | 163,800 | 5.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 9,021,360 | 52.2% |
| LOAD_ATTR_METHOD_NO_DICT | 4,925,400 | 28.5% |
| LOAD_FAST | 2,426,760 | 14.0% |
| LOAD_ATTR | 819,160 | 4.7% |
| LOAD_CONST | 81,880 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,383,860 | 94.8% |
| CALL_PY_WITH_DEFAULTS | 819,160 | 4.7% |
| RETURN_VALUE | 81,900 | 0.5% |
| CALL | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 7,392,880 | 100.0% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,570,220 | 34.8% |
| CALL_PY_EXACT_ARGS | 2,508,760 | 33.9% |
| TO_BOOL_BOOL | 1,433,480 | 19.4% |
| LOAD_GLOBAL_MODULE | 819,160 | 11.1% |
| BINARY_SUBSCR_DICT | 20,440 | 0.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 10,769,420 | 26.0% |
| LOAD_FAST | 9,737,480 | 23.5% |
| LOAD_ATTR_METHOD_NO_DICT | 7,688,240 | 18.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,269,440 | 10.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,508,760 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 40,977,540 | 98.8% |
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
| LOAD_ATTR_METHOD_NO_DICT | 15,533,480 | 83.0% |
| LOAD_FAST | 1,474,440 | 7.9% |
| LOAD_ATTR | 849,800 | 4.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 819,160 | 4.4% |
| BINARY_SUBSCR_DICT | 20,440 | 0.1% |

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
| LOAD_ATTR_SLOT | 28,303,240 | 83.2% |
| LOAD_CONST | 5,672,720 | 16.7% |
| LOAD_FAST_LOAD_FAST | 20,400 | 0.1% |
| CALL_LEN | 20,400 | 0.1% |
| BINARY_OP_SUBTRACT_INT | 10,200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,418,320 | 60.0% |
| LOAD_FAST | 13,598,700 | 40.0% |
| POP_JUMP_IF_TRUE | 10,220 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,935,280 | 61.2% |
| LOAD_FAST | 593,840 | 18.8% |
| LOAD_CONST | 552,800 | 17.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 81,880 | 2.6% |
| COMPARE_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,163,980 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 235,460 | 63.9% |
| GET_ITER | 133,020 | 36.1% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,460 | 63.9% |
| JUMP_BACKWARD | 102,400 | 27.8% |
| LOAD_FAST | 10,240 | 2.8% |
| LOAD_FAST_LOAD_FAST | 10,240 | 2.8% |
| RETURN_CONST | 10,220 | 2.8% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,220 | 99.2% |
| GET_ITER | 60 | 0.6% |
| FOR_ITER | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,220 | 99.2% |
| LOAD_FAST | 80 | 0.8% |


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
| LOAD_FAST | 48,571,600 | 61.3% |
| LOAD_ATTR_SLOT | 10,280,600 | 13.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 9,860,920 | 12.4% |
| LOAD_DEREF | 4,739,200 | 6.0% |
| LOAD_FAST_LOAD_FAST | 2,559,840 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,264,600 | 36.9% |
| CALL_PY_WITH_DEFAULTS | 15,533,480 | 19.6% |
| LOAD_GLOBAL_MODULE | 13,717,880 | 17.3% |
| CALL_PY_EXACT_ARGS | 7,688,240 | 9.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 7,392,880 | 9.3% |


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
| LOAD_GLOBAL_MODULE | 2,128,600 | 100.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 634,680 | 29.8% |
| PUSH_NULL | 593,860 | 27.9% |
| LOAD_FAST | 419,720 | 19.7% |
| LOAD_FAST_LOAD_FAST | 307,000 | 14.4% |
| LOAD_ATTR | 92,100 | 4.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,662,880 | 69.7% |
| LOAD_FAST_LOAD_FAST | 7,689,840 | 30.3% |
| LOAD_ATTR | 760 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 9,860,920 | 38.9% |
| CONTAINS_OP | 9,082,660 | 35.8% |
| CALL_PY_EXACT_ARGS | 4,269,440 | 16.8% |
| STORE_FAST | 1,402,860 | 5.5% |
| LOAD_FAST | 593,860 | 2.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,935,320 | 64.6% |
| LOAD_FAST | 1,013,520 | 33.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 46,040 | 1.5% |
| LOAD_ATTR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 1,935,340 | 64.6% |
| LOAD_ATTR_METHOD_NO_DICT | 962,520 | 32.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 46,040 | 1.5% |
| LOAD_FAST | 20,440 | 0.7% |
| PUSH_NULL | 10,220 | 0.3% |


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
| LOAD_FAST | 238,158,480 | 82.9% |
| COPY | 29,030,240 | 10.1% |
| LOAD_ATTR_SLOT | 17,866,500 | 6.2% |
| LOAD_FAST_LOAD_FAST | 2,314,000 | 0.8% |
| LOAD_ATTR | 2,200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,111,900 | 43.5% |
| COMPARE_OP_INT | 28,303,240 | 9.8% |
| LOAD_CONST | 21,882,600 | 7.6% |
| LOAD_ATTR_SLOT | 17,866,500 | 6.2% |
| TO_BOOL_ALWAYS_TRUE | 17,543,660 | 6.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,038,200 | 40.5% |
| LOAD_FAST | 3,358,640 | 16.9% |
| STORE_FAST_STORE_FAST | 3,235,840 | 16.3% |
| POP_JUMP_IF_FALSE | 2,139,960 | 10.8% |
| STORE_ATTR_SLOT | 1,433,480 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,376,820 | 87.6% |
| CALL_ISINSTANCE | 1,945,560 | 9.8% |
| LOAD_FAST_LOAD_FAST | 450,540 | 2.3% |
| LOAD_GLOBAL_BUILTIN | 40,980 | 0.2% |
| CHECK_EXC_MATCH | 30,700 | 0.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 13,717,880 | 35.8% |
| LOAD_FAST | 12,297,760 | 32.1% |
| RESUME_CHECK | 4,341,600 | 11.3% |
| LOAD_ATTR_SLOT | 2,846,600 | 7.4% |
| POP_JUMP_IF_FALSE | 2,590,520 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 24,206,280 | 63.1% |
| LOAD_FAST | 4,300,760 | 11.2% |
| LOAD_FAST_LOAD_FAST | 3,921,880 | 10.2% |
| CALL_ISINSTANCE | 3,522,480 | 9.2% |
| LOAD_ATTR_MODULE | 2,128,600 | 5.6% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 40,977,540 | 53.0% |
| CALL_PY_WITH_DEFAULTS | 18,708,000 | 24.2% |
| CACHE | 11,120,500 | 14.4% |
| LOAD_ATTR_PROPERTY | 3,737,500 | 4.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,063,400 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,475,240 | 70.4% |
| LOAD_GLOBAL_BUILTIN | 8,038,200 | 10.4% |
| NOP | 5,119,960 | 6.6% |
| LOAD_GLOBAL_MODULE | 4,341,600 | 5.6% |
| LOAD_FAST_LOAD_FAST | 3,184,580 | 4.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,390,960 | 60.8% |
| SWAP | 29,030,240 | 29.7% |
| LOAD_FAST_LOAD_FAST | 9,082,360 | 9.3% |
| STORE_ATTR_SLOT | 128,800 | 0.1% |
| STORE_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 69,672,680 | 71.4% |
| RETURN_CONST | 18,073,480 | 18.5% |
| LOAD_FAST_LOAD_FAST | 4,464,460 | 4.6% |
| LOAD_CONST | 1,791,900 | 1.8% |
| JUMP_BACKWARD | 1,587,160 | 1.6% |


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
| LOAD_ATTR_SLOT | 9,574,200 | 34.6% |
| LOAD_FAST | 7,966,280 | 28.8% |
| CALL_ISINSTANCE | 6,112,960 | 22.1% |
| COPY | 1,576,060 | 5.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,433,480 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 13,758,400 | 49.7% |
| POP_JUMP_IF_TRUE | 13,730,580 | 49.6% |
| EXTENDED_ARG | 112,500 | 0.4% |
| UNARY_NOT | 61,420 | 0.2% |
| TO_BOOL_NONE | 12,100 | 0.0% |


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
| LOAD_FAST | 10,024,640 | 52.6% |
| LOAD_ATTR_SLOT | 8,939,480 | 46.9% |
| RETURN_VALUE | 81,880 | 0.4% |
| COPY | 10,200 | 0.1% |
| TO_BOOL_NONE | 1,460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 11,622,160 | 61.0% |
| POP_JUMP_IF_FALSE | 7,434,180 | 39.0% |
| TO_BOOL_NONE | 1,460 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 6,983,600 | 73.4% |
| RETURN_VALUE | 2,529,200 | 26.6% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 9,512,880 | 100.0% |


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
|     deferred | 380 | 0.0% |
|          hit | 51,844,680 | 100.0% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
| Failure | 0 | 0.0% |


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
|     deferred | 1,402,580 | 3.9% |
|          hit | 34,539,240 | 96.0% |
|         miss | 31,300 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 860 | 61.4% |
| Failure | 540 | 38.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 540 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,898,020 | 2.6% |
|          hit | 105,002,300 | 95.5% |
|         miss | 1,948,460 | 1.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 42,060 | 94.2% |
| Failure | 2,580 | 5.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bound method | 640 | 24.8% |
| no dict | 540 | 20.9% |
| cfunc varargs keywords | 540 | 20.9% |
| cfunc noargs | 340 | 13.2% |
| meth descr varargs | 200 | 7.8% |
| code complex parameters | 160 | 6.2% |
| init not python | 160 | 6.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 23,419,340 | 38.6% |
|          hit | 37,191,220 | 61.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 5.8% |
| Failure | 7,420 | 94.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 6,940 | 93.5% |
| different types | 460 | 6.2% |
| list | 20 | 0.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,076,900 | 97.7% |
|          hit | 378,860 | 2.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 2.0% |
| Failure | 4,860 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 2,340 | 48.1% |
| ascii string | 1,080 | 22.2% |
| dict keys | 900 | 18.5% |
| enumerate | 540 | 11.1% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 26,214,760 | 6.0% |
|          hit | 403,045,780 | 92.5% |
|         miss | 6,420,820 | 1.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 129,960 | 83.1% |
| Failure | 26,520 | 16.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 22,920 | 86.4% |
| method | 3,260 | 12.3% |
| mutable class | 340 | 1.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,240 | 0.0% |
|          hit | 58,186,600 | 100.0% |
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
|     deferred | 368,934,881,474,190,904,380 | 377,871,775,692,381.1% |
|          hit | 90,805,640 | 93.0% |
|         miss | 6,827,580 | 7.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 129,660 | 100.0% |
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
|     deferred | 368,934,881,474,190,958,620 | 359,001,105,484,764.2% |
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
| Basic | 968,032,280 | 44.1% |
| Not specialized | 245,858,880 | 11.2% |
| Specialized hits | 963,095,200 | 43.8% |
| Specialized misses | 19,874,400 | 0.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL | 368,934,881,474,190,958,620 | 50.0% |
| STORE_ATTR | 368,934,881,474,190,904,380 | 50.0% |
| LOAD_ATTR | 26,214,760 | 0.0% |
| COMPARE_OP | 23,419,340 | 0.0% |
| FOR_ITER | 16,076,900 | 0.0% |
| CALL | 2,898,020 | 0.0% |
| BINARY_SUBSCR | 1,402,580 | 0.0% |
| LOAD_GLOBAL | 3,240 | 0.0% |
| BINARY_OP | 380 | 0.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 6,827,580 | 34.3% |
| LOAD_ATTR_SLOT | 2,622,520 | 13.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,440,860 | 12.3% |
| TO_BOOL_NONE | 2,289,240 | 11.5% |
| TO_BOOL_ALWAYS_TRUE | 1,616,420 | 8.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,357,340 | 6.8% |
| CALL_PY_EXACT_ARGS | 999,320 | 5.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 949,140 | 4.8% |
| TO_BOOL_BOOL | 645,140 | 3.2% |
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
| Frames pushed | 63,342,660 | 81.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 17,363,400 | 21.5% |
| Frees to freelist | 17,367,900 |  |
| Allocations | 63,316,740 | 78.5% |
| Allocations to 512 bytes | 63,316,740 | 78.5% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 63,055,442 |  |
| New values | 1,617,920 |  |
| Interpreter increfs | 1,049,253,160 | 88.7% |
| Interpreter decrefs | 1,141,648,160 | 90.7% |
| Increfs | 133,507,142 | 11.3% |
| Decrefs | 117,278,542 | 9.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 63,307,928 |  |
| Method cache misses | 630,252 |  |
| Method cache collisions | 741,599 |  |
| Method cache dunder hits | 20,131,984 |  |
| Method cache dunder misses | 112,756 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 4,020 | 1,315,620 | 23,184,360 |
| 1 | 360 | 1,052,880 | 8,757,480 |
| 2 | 20 | 44,280 | 4,298,200 |


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
