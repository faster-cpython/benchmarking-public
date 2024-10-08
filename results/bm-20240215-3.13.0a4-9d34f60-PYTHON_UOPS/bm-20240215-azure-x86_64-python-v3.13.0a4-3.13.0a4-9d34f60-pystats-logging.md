
# Pystats results

- benchmark: logging
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 545,515,460 | 22.5% | 22.5% |  |
| POP_JUMP_IF_FALSE | 168,755,860 | 7.0% | 29.4% |  |
| RESUME_CHECK | 156,468,280 | 6.5% | 35.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 154,858,780 | 6.4% | 42.3% | 1.1% |
| TO_BOOL_BOOL | 140,083,340 | 5.8% | 48.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 130,580,340 | 5.4% | 53.4% |  |
| LOAD_GLOBAL_MODULE | 111,413,820 | 4.6% | 58.0% | 0.0% |
| CALL_PY_EXACT_ARGS | 96,666,000 | 4.0% | 62.0% |  |
| RETURN_VALUE | 92,571,520 | 3.8% | 65.8% |  |
| POP_TOP | 75,367,540 | 3.1% | 68.9% |  |
| CALL | 72,122,900 | 3.0% | 71.9% |  |
| LOAD_CONST | 65,536,980 | 2.7% | 74.6% |  |
| RETURN_CONST | 65,536,240 | 2.7% | 77.3% |  |
| STORE_FAST | 64,721,180 | 2.7% | 80.0% |  |
| NOP | 62,259,440 | 2.6% | 82.6% |  |
| BINARY_SUBSCR_DICT | 55,705,540 | 2.3% | 84.8% |  |
| LOAD_FAST_LOAD_FAST | 46,613,120 | 1.9% | 86.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 36,043,920 | 1.5% | 88.3% |  |
| LOAD_ATTR_MODULE | 29,493,020 | 1.2% | 89.5% |  |
| LOAD_GLOBAL_BUILTIN | 19,660,940 | 0.8% | 90.3% | 0.0% |
| PUSH_NULL | 16,385,840 | 0.7% | 91.0% |  |
| TO_BOOL_NONE | 14,745,240 | 0.6% | 91.6% |  |
| COMPARE_OP_INT | 13,926,600 | 0.6% | 92.1% |  |
| POP_JUMP_IF_TRUE | 13,108,160 | 0.5% | 92.7% |  |
| LOAD_ATTR | 11,484,500 | 0.5% | 93.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 11,468,680 | 0.5% | 93.6% |  |
| ENTER_EXECUTOR | 10,319,680 | 0.4% | 94.1% |  |
| BINARY_OP | 9,016,320 | 0.4% | 94.4% |  |
| CALL_ISINSTANCE | 7,372,660 | 0.3% | 94.7% |  |
| JUMP_FORWARD | 6,553,660 | 0.3% | 95.0% |  |
| BINARY_SLICE | 6,553,600 | 0.3% | 95.3% |  |
| FOR_ITER_LIST | 6,553,520 | 0.3% | 95.5% |  |
| BINARY_OP_ADD_INT | 6,553,480 | 0.3% | 95.8% |  |
| TO_BOOL_ALWAYS_TRUE | 6,553,440 | 0.3% | 96.1% |  |
| CALL_BUILTIN_FAST | 5,734,440 | 0.2% | 96.3% |  |
| COPY | 4,915,900 | 0.2% | 96.5% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,915,800 | 0.2% | 96.7% |  |
| LOAD_ATTR_SLOT | 4,915,720 | 0.2% | 96.9% |  |
| GET_ITER | 4,915,440 | 0.2% | 97.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,915,440 | 0.2% | 97.3% |  |
| BUILD_TUPLE | 4,915,200 | 0.2% | 97.5% |  |
| POP_JUMP_IF_NONE | 4,915,200 | 0.2% | 97.7% |  |
| INTERPRETER_EXIT | 4,096,460 | 0.2% | 97.9% |  |
| TO_BOOL | 3,281,280 | 0.1% | 98.0% |  |
| POP_JUMP_IF_NOT_NONE | 3,277,440 | 0.1% | 98.2% |  |
| COMPARE_OP_STR | 3,277,360 | 0.1% | 98.3% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 3,277,260 | 0.1% | 98.4% |  |
| CALL_BUILTIN_CLASS | 3,276,900 | 0.1% | 98.6% |  |
| BEFORE_WITH | 3,276,860 | 0.1% | 98.7% |  |
| STORE_FAST_STORE_FAST | 3,276,800 | 0.1% | 98.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,276,720 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 2,457,540 | 0.1% | 99.1% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,670,020 | 0.1% | 99.2% | 100.0% |
| CALL_FUNCTION_EX | 1,638,880 | 0.1% | 99.2% |  |
| BINARY_OP_SUBTRACT_FLOAT | 1,638,540 | 0.1% | 99.3% |  |
| BUILD_MAP | 1,638,400 | 0.1% | 99.4% |  |
| CONTAINS_OP | 1,638,400 | 0.1% | 99.4% |  |
| DICT_MERGE | 1,638,400 | 0.1% | 99.5% |  |
| BINARY_OP_ADD_UNICODE | 1,638,360 | 0.1% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 1,638,360 | 0.1% | 99.6% |  |
| CALL_METHOD_DESCRIPTOR_O | 1,638,360 | 0.1% | 99.7% |  |
| CALL_STR_1 | 1,638,360 | 0.1% | 99.8% |  |
| LOAD_ATTR_PROPERTY | 1,638,360 | 0.1% | 99.8% |  |
| TO_BOOL_STR | 1,638,360 | 0.1% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 1,638,360 | 0.1% | 100.0% |  |
| CALL_LEN | 819,360 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,400 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 2,380 | 0.0% | 100.0% |  |
| STORE_ATTR | 1,760 | 0.0% | 100.0% |  |
| RESUME | 1,400 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 1,380 | 0.0% | 100.0% |  |
| COMPARE_OP | 1,000 | 0.0% | 100.0% |  |
| LOAD_DEREF | 720 | 0.0% | 100.0% |  |
| FOR_ITER | 280 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 240 | 0.0% | 100.0% |  |
| BUILD_LIST | 240 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 240 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 240 | 0.0% | 100.0% |  |
| LIST_EXTEND | 240 | 0.0% | 100.0% |  |
| IS_OP | 180 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 120 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 80 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 60 | 0.0% | 100.0% |  |
| POP_EXCEPT | 60 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 60 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 60 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 60 | 0.0% | 100.0% |  |
| SWAP | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 154,007,200 | 6.3% | 6.3% |
| RESUME_CHECK LOAD_FAST | 131,071,720 | 5.4% | 11.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 130,252,180 | 5.4% | 17.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 127,302,360 | 5.2% | 22.4% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 96,666,000 | 4.0% | 26.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 67,583,920 | 2.8% | 29.1% |
| RETURN_CONST POP_TOP | 60,621,040 | 2.5% | 31.6% |
| RETURN_VALUE TO_BOOL_BOOL | 58,982,440 | 2.4% | 34.1% |
| NOP LOAD_FAST | 58,982,400 | 2.4% | 36.5% |
| POP_JUMP_IF_FALSE RETURN_CONST | 57,344,000 | 2.4% | 38.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 57,343,860 | 2.4% | 41.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 57,343,720 | 2.4% | 43.6% |
| POP_JUMP_IF_FALSE NOP | 55,705,600 | 2.3% | 45.9% |
| BINARY_SUBSCR_DICT RETURN_VALUE | 55,705,540 | 2.3% | 48.2% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 55,705,400 | 2.3% | 50.5% |
| POP_TOP LOAD_FAST | 55,214,380 | 2.3% | 52.8% |
| LOAD_FAST CALL | 54,479,480 | 2.2% | 55.0% |
| CALL RESUME_CHECK | 54,067,300 | 2.2% | 57.2% |
| LOAD_FAST BINARY_SUBSCR_DICT | 54,067,080 | 2.2% | 59.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 54,067,080 | 2.2% | 61.7% |
| STORE_FAST LOAD_FAST | 40,143,740 | 1.7% | 63.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 33,587,560 | 1.4% | 64.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 26,213,920 | 1.1% | 65.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 23,757,400 | 1.0% | 66.8% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 19,659,840 | 0.8% | 67.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 16,383,200 | 0.7% | 68.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 15,565,740 | 0.6% | 68.9% |
| LOAD_FAST LOAD_CONST | 15,565,280 | 0.6% | 69.6% |
| LOAD_ATTR_MODULE PUSH_NULL | 14,746,500 | 0.6% | 70.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 14,745,640 | 0.6% | 70.8% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 14,745,240 | 0.6% | 71.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 13,106,880 | 0.5% | 71.9% |
| LOAD_FAST LOAD_ATTR | 11,476,120 | 0.5% | 72.4% |
| RETURN_VALUE STORE_FAST | 11,469,440 | 0.5% | 72.9% |
| LOAD_FAST RETURN_VALUE | 11,469,040 | 0.5% | 73.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 10,649,880 | 0.4% | 73.8% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 9,831,160 | 0.4% | 74.2% |
| LOAD_CONST LOAD_FAST | 9,830,400 | 0.4% | 74.6% |
| LOAD_CONST STORE_FAST | 9,830,400 | 0.4% | 75.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 9,829,920 | 0.4% | 75.4% |
| LOAD_CONST COMPARE_OP_INT | 9,011,200 | 0.4% | 75.8% |
| POP_TOP RETURN_CONST | 8,192,240 | 0.3% | 76.1% |
| RETURN_VALUE RETURN_VALUE | 8,192,240 | 0.3% | 76.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 8,192,000 | 0.3% | 76.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 8,191,840 | 0.3% | 77.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 7,372,520 | 0.3% | 77.4% |
| POP_TOP ENTER_EXECUTOR | 7,043,420 | 0.3% | 77.7% |
| LOAD_FAST STORE_FAST | 6,554,300 | 0.3% | 78.0% |
| CALL STORE_FAST | 6,554,140 | 0.3% | 78.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 6,554,120 | 0.3% | 78.5% |
| POP_JUMP_IF_TRUE LOAD_FAST | 6,553,920 | 0.3% | 78.8% |
| LOAD_CONST LOAD_CONST | 6,553,720 | 0.3% | 79.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 6,553,600 | 0.3% | 79.3% |
| RETURN_VALUE LOAD_FAST | 6,553,560 | 0.3% | 79.6% |
| LOAD_CONST BINARY_OP_ADD_INT | 6,553,320 | 0.3% | 79.9% |
| LOAD_FAST TO_BOOL_NONE | 6,553,280 | 0.3% | 80.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 6,553,280 | 0.3% | 80.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_NONE | 6,553,280 | 0.3% | 80.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 6,553,280 | 0.3% | 81.0% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 6,553,280 | 0.3% | 81.2% |
| LOAD_ATTR_MODULE LOAD_ATTR_MODULE | 5,734,760 | 0.2% | 81.5% |
| ENTER_EXECUTOR CALL | 5,405,520 | 0.2% | 81.7% |
| PUSH_NULL LOAD_FAST | 4,916,320 | 0.2% | 81.9% |
| PUSH_NULL CALL | 4,916,000 | 0.2% | 82.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 4,915,940 | 0.2% | 82.3% |
| LOAD_ATTR STORE_FAST | 4,915,880 | 0.2% | 82.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 4,915,780 | 0.2% | 82.7% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,915,720 | 0.2% | 82.9% |
| LOAD_ATTR_MODULE LOAD_FAST | 4,915,720 | 0.2% | 83.1% |
| LOAD_CONST BINARY_OP | 4,915,640 | 0.2% | 83.3% |
| POP_TOP LOAD_CONST | 4,915,200 | 0.2% | 83.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 4,915,200 | 0.2% | 83.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 4,915,200 | 0.2% | 83.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 4,915,200 | 0.2% | 84.1% |
| STORE_FAST LOAD_CONST | 4,915,200 | 0.2% | 84.3% |
| FOR_ITER_LIST LOAD_FAST | 4,915,160 | 0.2% | 84.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 4,915,140 | 0.2% | 84.7% |
| BINARY_OP_ADD_INT STORE_FAST | 4,915,120 | 0.2% | 84.9% |
| LOAD_ATTR_INSTANCE_VALUE GET_ITER | 4,915,120 | 0.2% | 85.1% |
| RESUME_CHECK NOP | 4,915,120 | 0.2% | 85.3% |
| GET_ITER FOR_ITER_LIST | 4,915,080 | 0.2% | 85.5% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 4,915,080 | 0.2% | 85.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 4,915,080 | 0.2% | 86.0% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 4,915,080 | 0.2% | 86.2% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 4,915,040 | 0.2% | 86.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 4,915,000 | 0.2% | 86.6% |
| LOAD_CONST CALL_BUILTIN_FAST | 4,914,960 | 0.2% | 86.8% |
| LOAD_FAST TO_BOOL_ALWAYS_TRUE | 4,914,960 | 0.2% | 87.0% |
| CACHE RESUME_CHECK | 4,096,260 | 0.2% | 87.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 4,096,080 | 0.2% | 87.3% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 4,096,060 | 0.2% | 87.5% |
| TO_BOOL POP_JUMP_IF_FALSE | 3,278,060 | 0.1% | 87.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 3,277,440 | 0.1% | 87.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 3,277,440 | 0.1% | 87.9% |
| LOAD_CONST CALL | 3,277,380 | 0.1% | 88.0% |
| CALL POP_TOP | 3,277,300 | 0.1% | 88.1% |
| COPY TO_BOOL_BOOL | 3,277,280 | 0.1% | 88.3% |
| CALL LOAD_FAST | 3,277,080 | 0.1% | 88.4% |
| CALL LOAD_CONST | 3,276,880 | 0.1% | 88.6% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 3,276,880 | 0.1% | 88.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,276,800 | 50.0% |
| LOAD_FAST | 1,638,400 | 25.0% |
| BINARY_OP_ADD_INT | 1,638,360 | 25.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,638,400 | 25.0% |
| BUILD_TUPLE | 1,638,400 | 25.0% |
| LOAD_FAST | 1,638,400 | 25.0% |
| LOAD_FAST_LOAD_FAST | 1,638,400 | 25.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,096,260 | 100.0% |
| RESUME | 200 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,276,720 | 100.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,276,860 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 50.0% |
| LOAD_FAST | 120 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 60 | 25.0% |
| BINARY_SUBSCR_DICT | 60 | 25.0% |
| BINARY_SUBSCR_TUPLE_INT | 60 | 25.0% |
| LOAD_FAST | 40 | 16.7% |
| LOAD_GLOBAL | 20 | 8.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,915,120 | 100.0% |
| LOAD_FAST | 240 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,915,080 | 100.0% |
| FOR_ITER | 180 | 0.0% |
| FOR_ITER_RANGE | 180 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,276,800 | 80.0% |
| RETURN_VALUE | 819,660 | 20.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 55,705,600 | 89.5% |
| RESUME_CHECK | 4,915,120 | 7.9% |
| STORE_ATTR_INSTANCE_VALUE | 1,638,360 | 2.6% |
| POP_TOP | 240 | 0.0% |
| RESUME | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,982,400 | 94.7% |
| LOAD_GLOBAL_MODULE | 3,276,720 | 5.3% |
| LOAD_DEREF | 240 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60,621,040 | 80.4% |
| CALL | 3,277,300 | 4.3% |
| BEFORE_WITH | 3,276,860 | 4.3% |
| RETURN_VALUE | 1,638,400 | 2.2% |
| CALL_FUNCTION_EX | 1,638,400 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,214,380 | 73.3% |
| RETURN_CONST | 8,192,240 | 10.9% |
| ENTER_EXECUTOR | 7,043,420 | 9.3% |
| LOAD_CONST | 4,915,200 | 6.5% |
| JUMP_BACKWARD | 1,700 | 0.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 60 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 14,746,500 | 90.0% |
| LOAD_ATTR | 1,638,860 | 10.0% |
| LOAD_DEREF | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,916,320 | 30.0% |
| CALL | 4,916,000 | 30.0% |
| LOAD_CONST | 1,638,400 | 10.0% |
| LOAD_FAST_LOAD_FAST | 1,638,400 | 10.0% |
| CALL_PY_EXACT_ARGS | 1,638,320 | 10.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 55,705,540 | 60.2% |
| LOAD_FAST | 11,469,040 | 12.4% |
| RETURN_VALUE | 8,192,240 | 8.8% |
| BUILD_TUPLE | 3,276,800 | 3.5% |
| CALL_BUILTIN_FAST | 2,457,720 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 58,982,440 | 63.7% |
| STORE_FAST | 11,469,440 | 12.4% |
| RETURN_VALUE | 8,192,240 | 8.8% |
| LOAD_FAST | 6,553,560 | 7.1% |
| POP_TOP | 1,638,400 | 1.8% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,639,100 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,700 | 49.9% |
| TO_BOOL | 1,600 | 0.0% |
| LOAD_ATTR | 520 | 0.0% |
| RETURN_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,278,060 | 99.9% |
| TO_BOOL | 1,600 | 0.0% |
| TO_BOOL_BOOL | 820 | 0.0% |
| TO_BOOL_NONE | 360 | 0.0% |
| POP_JUMP_IF_TRUE | 240 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,915,640 | 54.5% |
| LOAD_FAST | 1,638,520 | 18.2% |
| CALL_BUILTIN_CLASS | 1,638,360 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 819,180 | 9.1% |
| BINARY_OP | 4,400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,276,800 | 36.3% |
| LOAD_CONST | 1,638,440 | 18.2% |
| RETURN_VALUE | 1,638,400 | 18.2% |
| CALL_BUILTIN_CLASS | 1,638,320 | 18.2% |
| STORE_FAST | 819,380 | 9.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 240 | 100.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,638,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,400 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 1,638,400 | 33.3% |
| LOAD_FAST | 1,638,400 | 33.3% |
| LOAD_FAST_LOAD_FAST | 1,638,400 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,276,800 | 66.7% |
| BUILD_MAP | 1,638,400 | 33.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,479,480 | 75.5% |
| ENTER_EXECUTOR | 5,405,520 | 7.5% |
| PUSH_NULL | 4,916,000 | 6.8% |
| LOAD_CONST | 3,277,380 | 4.5% |
| LOAD_GLOBAL_MODULE | 1,638,580 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 54,067,300 | 75.0% |
| STORE_FAST | 6,554,140 | 9.1% |
| POP_TOP | 3,277,300 | 4.5% |
| LOAD_FAST | 3,277,080 | 4.5% |
| LOAD_CONST | 3,276,880 | 4.5% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 1,638,400 | 100.0% |
| CALL_INTRINSIC_1 | 240 | 0.0% |
| LOAD_FAST | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,638,400 | 100.0% |
| COPY_FREE_VARS | 240 | 0.0% |
| RESUME_CHECK | 180 | 0.0% |
| RESUME | 60 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 240 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 400 | 40.0% |
| LOAD_FAST_LOAD_FAST | 160 | 16.0% |
| LOAD_FAST | 140 | 14.0% |
| RETURN_VALUE | 60 | 6.0% |
| BINARY_OP | 40 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 380 | 38.0% |
| COMPARE_OP_INT | 360 | 36.0% |
| COPY | 100 | 10.0% |
| COMPARE_OP_STR | 80 | 8.0% |
| RETURN_VALUE | 40 | 4.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,638,400 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 1,639,000 | 33.3% |
| CONTAINS_OP | 1,638,400 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,360 | 33.3% |
| COMPARE_OP | 100 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,277,280 | 66.7% |
| STORE_FAST | 1,638,400 | 33.3% |
| TO_BOOL | 160 | 0.0% |
| STORE_FAST_LOAD_FAST | 60 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 180 | 75.0% |
| RESUME | 60 | 25.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,638,400 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,043,420 | 68.3% |
| POP_JUMP_IF_FALSE | 3,276,120 | 31.7% |
| JUMP_BACKWARD | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 5,405,520 | 52.4% |
| POP_TOP | 1,638,080 | 15.9% |
| POP_JUMP_IF_FALSE | 1,638,080 | 15.9% |
| FOR_ITER_LIST | 1,637,760 | 15.9% |
| FOR_ITER_RANGE | 240 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 180 | 64.3% |
| JUMP_BACKWARD | 100 | 35.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 35.7% |
| FOR_ITER_LIST | 80 | 28.6% |
| FOR_ITER_RANGE | 60 | 21.4% |
| LOAD_FAST | 40 | 14.3% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 180 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,700 | 71.4% |
| POP_JUMP_IF_FALSE | 680 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 900 | 37.8% |
| LOAD_FAST | 640 | 26.9% |
| FOR_ITER_LIST | 600 | 25.2% |
| ENTER_EXECUTOR | 140 | 5.9% |
| FOR_ITER | 100 | 4.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 3,276,720 | 50.0% |
| STORE_FAST | 1,638,400 | 25.0% |
| STORE_FAST_STORE_FAST | 1,638,400 | 25.0% |
| STORE_ATTR | 80 | 0.0% |
| POP_TOP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,276,800 | 50.0% |
| LOAD_CONST | 1,638,400 | 25.0% |
| LOAD_GLOBAL_MODULE | 1,638,320 | 25.0% |
| LOAD_GLOBAL | 80 | 0.0% |
| LOAD_FAST_CHECK | 60 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 240 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,476,120 | 99.9% |
| LOAD_ATTR | 6,120 | 0.1% |
| LOAD_GLOBAL_MODULE | 760 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |
| LOAD_ATTR_MODULE | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,915,880 | 42.8% |
| LOAD_FAST | 1,639,940 | 14.3% |
| LOAD_ATTR_SLOT | 1,639,080 | 14.3% |
| PUSH_NULL | 1,638,860 | 14.3% |
| TO_BOOL_BOOL | 1,638,320 | 14.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,565,280 | 23.8% |
| LOAD_CONST | 6,553,720 | 10.0% |
| POP_TOP | 4,915,200 | 7.5% |
| LOAD_FAST_LOAD_FAST | 4,915,200 | 7.5% |
| STORE_FAST | 4,915,200 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,830,400 | 15.0% |
| STORE_FAST | 9,830,400 | 15.0% |
| COMPARE_OP_INT | 9,011,200 | 13.7% |
| LOAD_CONST | 6,553,720 | 10.0% |
| BINARY_OP_ADD_INT | 6,553,320 | 10.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 240 | 33.3% |
| BUILD_LIST | 240 | 33.3% |
| RESUME_CHECK | 180 | 25.0% |
| RESUME | 60 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 480 | 66.7% |
| LIST_EXTEND | 240 | 33.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 131,071,720 | 24.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 67,583,920 | 12.4% |
| NOP | 58,982,400 | 10.8% |
| LOAD_ATTR_INSTANCE_VALUE | 57,343,860 | 10.5% |
| POP_TOP | 55,214,380 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 154,007,200 | 28.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 127,302,360 | 23.3% |
| CALL | 54,479,480 | 10.0% |
| BINARY_SUBSCR_DICT | 54,067,080 | 9.9% |
| CALL_PY_EXACT_ARGS | 26,213,920 | 4.8% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 60 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 13,106,880 | 28.1% |
| LOAD_FAST_LOAD_FAST | 8,192,000 | 17.6% |
| STORE_FAST | 6,553,600 | 14.1% |
| LOAD_GLOBAL_MODULE | 4,096,080 | 8.8% |
| POP_JUMP_IF_FALSE | 4,096,060 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 16,383,200 | 35.1% |
| LOAD_FAST_LOAD_FAST | 8,192,000 | 17.6% |
| LOAD_CONST | 4,915,200 | 10.5% |
| LOAD_FAST | 4,915,200 | 10.5% |
| CALL_PY_EXACT_ARGS | 3,276,640 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 840 | 19.1% |
| POP_JUMP_IF_FALSE | 560 | 12.7% |
| RESUME_CHECK | 440 | 10.0% |
| LOAD_FAST | 400 | 9.1% |
| RESUME | 400 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,660 | 37.7% |
| LOAD_ATTR | 720 | 16.4% |
| LOAD_FAST | 580 | 13.2% |
| LOAD_GLOBAL_BUILTIN | 520 | 11.8% |
| CALL | 220 | 5.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 130,252,180 | 77.2% |
| TO_BOOL_NONE | 14,745,240 | 8.7% |
| COMPARE_OP_INT | 10,649,880 | 6.3% |
| TO_BOOL_ALWAYS_TRUE | 4,915,080 | 2.9% |
| TO_BOOL | 3,278,060 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 57,344,000 | 34.0% |
| NOP | 55,705,600 | 33.0% |
| LOAD_FAST | 33,587,560 | 19.9% |
| LOAD_GLOBAL_MODULE | 6,553,280 | 3.9% |
| LOAD_GLOBAL_BUILTIN | 4,915,140 | 2.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,915,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,276,800 | 66.7% |
| LOAD_GLOBAL_MODULE | 1,638,320 | 33.3% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,277,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,277,440 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 9,831,160 | 75.0% |
| COMPARE_OP_INT | 1,638,360 | 12.5% |
| TO_BOOL_ALWAYS_TRUE | 1,638,360 | 12.5% |
| TO_BOOL | 240 | 0.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,553,920 | 50.0% |
| LOAD_CONST | 3,276,800 | 25.0% |
| RETURN_VALUE | 1,638,720 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 1,638,320 | 12.5% |
| POP_TOP | 320 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 57,344,000 | 87.5% |
| POP_TOP | 8,192,240 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 60,621,040 | 92.5% |
| INTERPRETER_EXIT | 3,276,800 | 5.0% |
| STORE_FAST | 1,638,400 | 2.5% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 960 | 54.5% |
| LOAD_FAST_LOAD_FAST | 800 | 45.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 880 | 50.0% |
| LOAD_FAST_LOAD_FAST | 320 | 18.2% |
| LOAD_GLOBAL | 280 | 15.9% |
| LOAD_FAST | 120 | 6.8% |
| JUMP_FORWARD | 80 | 4.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 11,469,440 | 17.7% |
| LOAD_CONST | 9,830,400 | 15.2% |
| LOAD_FAST | 6,554,300 | 10.1% |
| CALL | 6,554,140 | 10.1% |
| LOAD_ATTR | 4,915,880 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,143,740 | 62.0% |
| LOAD_GLOBAL_MODULE | 6,554,120 | 10.1% |
| LOAD_FAST_LOAD_FAST | 6,553,600 | 10.1% |
| LOAD_CONST | 4,915,200 | 7.6% |
| LOAD_GLOBAL_BUILTIN | 3,276,880 | 5.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 60 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,638,400 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 1,638,360 | 50.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 1,638,400 | 50.0% |
| STORE_FAST_STORE_FAST | 1,638,400 | 50.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_CHECK | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 60 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 40 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 40 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,080 | 77.1% |
| CACHE | 200 | 14.3% |
| CALL_FUNCTION_EX | 60 | 4.3% |
| COPY_FREE_VARS | 60 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 820 | 58.6% |
| LOAD_GLOBAL | 400 | 28.6% |
| NOP | 80 | 5.7% |
| LOAD_DEREF | 60 | 4.3% |
| LOAD_CONST | 40 | 2.9% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,553,320 | 100.0% |
| BINARY_OP | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,915,120 | 75.0% |
| BINARY_SLICE | 1,638,360 | 25.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,638,320 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 1,638,320 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 66.7% |
| BINARY_OP | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 80 | 66.7% |
| COMPARE_OP | 40 | 33.3% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,638,320 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,638,360 | 100.0% |
| STORE_FAST | 180 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,638,320 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,638,360 | 100.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,067,080 | 97.1% |
| CALL | 1,638,400 | 2.9% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 55,705,540 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,457,480 | 100.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,360 | 66.7% |
| LOAD_GLOBAL_MODULE | 819,160 | 33.3% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,440 | 50.0% |
| BINARY_OP | 1,638,320 | 50.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,638,360 | 50.0% |
| LOAD_CONST | 1,638,360 | 50.0% |
| STORE_FAST | 180 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,914,960 | 85.7% |
| LOAD_FAST_LOAD_FAST | 819,340 | 14.3% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,276,640 | 57.1% |
| RETURN_VALUE | 2,457,720 | 42.9% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,915,720 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,276,760 | 66.7% |
| RETURN_VALUE | 1,639,040 | 33.3% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,276,720 | 44.4% |
| LOAD_GLOBAL_MODULE | 3,276,640 | 44.4% |
| LOAD_ATTR_MODULE | 819,160 | 11.1% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 7,372,520 | 100.0% |
| TO_BOOL | 140 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 819,240 | 100.0% |
| CALL | 80 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 819,240 | 100.0% |
| LOAD_FAST | 120 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,276,760 | 66.7% |
| LOAD_FAST | 1,638,320 | 33.3% |
| CALL | 240 | 0.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,915,080 | 100.0% |
| POP_TOP | 360 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 80 | 66.7% |
| CALL | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_LAZY_DICT | 1,638,440 | 98.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 31,480 | 1.9% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,638,360 | 98.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 31,480 | 1.9% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| CALL_LEN | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 1,638,320 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,638,360 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 55,705,400 | 57.6% |
| LOAD_FAST | 26,213,920 | 27.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,553,280 | 6.8% |
| LOAD_FAST_LOAD_FAST | 3,276,640 | 3.4% |
| LOAD_ATTR_SLOT | 1,638,960 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 96,666,000 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,638,360 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,011,200 | 64.7% |
| LOAD_FAST_LOAD_FAST | 3,276,640 | 23.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 11.8% |
| COMPARE_OP | 360 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,649,880 | 76.5% |
| RETURN_VALUE | 1,638,360 | 11.8% |
| POP_JUMP_IF_TRUE | 1,638,360 | 11.8% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,638,960 | 50.0% |
| LOAD_FAST | 1,638,320 | 50.0% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,639,000 | 50.0% |
| POP_JUMP_IF_FALSE | 1,638,360 | 50.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 4,915,080 | 75.0% |
| ENTER_EXECUTOR | 1,637,760 | 25.0% |
| JUMP_BACKWARD | 600 | 0.0% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,915,160 | 75.0% |
| STORE_FAST | 1,638,360 | 25.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 900 | 65.2% |
| ENTER_EXECUTOR | 240 | 17.4% |
| GET_ITER | 180 | 13.0% |
| FOR_ITER | 60 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,140 | 82.6% |
| LOAD_GLOBAL | 120 | 8.7% |
| LOAD_GLOBAL_MODULE | 120 | 8.7% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 154,007,200 | 99.5% |
| LOAD_FAST_LOAD_FAST | 819,160 | 0.5% |
| LOAD_ATTR_INSTANCE_VALUE | 31,200 | 0.0% |
| LOAD_ATTR | 1,220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,343,860 | 37.0% |
| TO_BOOL_BOOL | 57,343,720 | 37.0% |
| TO_BOOL_NONE | 6,553,280 | 4.2% |
| GET_ITER | 4,915,120 | 3.2% |
| BEFORE_WITH | 3,276,720 | 2.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,680 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 50.0% |
| LOAD_ATTR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,638,440 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,638,360 | 50.0% |
| LOAD_CONST | 180 | 0.0% |
| CALL | 160 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 120 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,915,000 | 42.9% |
| LOAD_ATTR_MODULE | 3,276,640 | 28.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 14.3% |
| LOAD_GLOBAL_MODULE | 1,638,320 | 14.3% |
| LOAD_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,191,840 | 71.4% |
| LOAD_CONST | 3,276,720 | 28.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 80 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 127,302,360 | 97.5% |
| LOAD_ATTR_INSTANCE_VALUE | 3,276,640 | 2.5% |
| LOAD_ATTR | 1,340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,583,920 | 51.8% |
| LOAD_GLOBAL_MODULE | 54,067,080 | 41.4% |
| CALL_PY_EXACT_ARGS | 6,553,280 | 5.0% |
| LOAD_FAST_LOAD_FAST | 2,375,840 | 1.8% |
| CALL | 160 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 23,757,400 | 80.6% |
| LOAD_ATTR_MODULE | 5,734,760 | 19.4% |
| LOAD_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 14,746,500 | 50.0% |
| LOAD_ATTR_MODULE | 5,734,760 | 19.4% |
| LOAD_FAST | 4,915,720 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 3,276,640 | 11.1% |
| CALL_ISINSTANCE | 819,160 | 2.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,638,320 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,638,320 | 50.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,638,360 | 50.0% |
| BINARY_OP_ADD_UNICODE | 1,638,320 | 50.0% |
| BINARY_OP | 40 | 0.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,638,320 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,638,360 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,276,640 | 66.7% |
| LOAD_ATTR | 1,639,080 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,276,720 | 66.7% |
| CALL_PY_EXACT_ARGS | 1,638,960 | 33.3% |
| CALL | 40 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,915,140 | 25.0% |
| LOAD_FAST | 4,915,040 | 25.0% |
| STORE_FAST | 3,276,880 | 16.7% |
| RESUME_CHECK | 3,276,720 | 16.7% |
| POP_JUMP_IF_TRUE | 1,638,320 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,745,640 | 75.0% |
| CALL_ISINSTANCE | 3,276,720 | 16.7% |
| LOAD_GLOBAL_MODULE | 1,638,320 | 8.3% |
| RETURN_VALUE | 180 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 54,067,080 | 48.5% |
| RESUME_CHECK | 15,565,740 | 14.0% |
| STORE_ATTR_INSTANCE_VALUE | 9,829,920 | 8.8% |
| STORE_FAST | 6,554,120 | 5.9% |
| POP_JUMP_IF_FALSE | 6,553,280 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 55,705,400 | 50.0% |
| LOAD_ATTR_MODULE | 23,757,400 | 21.3% |
| TO_BOOL_BOOL | 6,553,280 | 5.9% |
| LOAD_FAST | 4,915,940 | 4.4% |
| LOAD_FAST_LOAD_FAST | 4,096,080 | 3.7% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 96,666,000 | 61.8% |
| CALL | 54,067,300 | 34.6% |
| CACHE | 4,096,260 | 2.6% |
| LOAD_ATTR_PROPERTY | 1,638,360 | 1.0% |
| CALL_FUNCTION_EX | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 131,071,720 | 83.8% |
| LOAD_GLOBAL_MODULE | 15,565,740 | 9.9% |
| NOP | 4,915,120 | 3.1% |
| LOAD_GLOBAL_BUILTIN | 3,276,720 | 2.1% |
| LOAD_CONST | 1,638,360 | 1.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,659,840 | 54.5% |
| LOAD_FAST_LOAD_FAST | 16,383,200 | 45.5% |
| STORE_ATTR | 880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,106,880 | 36.4% |
| LOAD_GLOBAL_MODULE | 9,829,920 | 27.3% |
| LOAD_FAST | 4,915,080 | 13.6% |
| JUMP_FORWARD | 3,276,720 | 9.1% |
| NOP | 1,638,360 | 4.5% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,914,960 | 75.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 25.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,915,080 | 75.0% |
| POP_JUMP_IF_TRUE | 1,638,360 | 25.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 58,982,440 | 42.1% |
| LOAD_ATTR_INSTANCE_VALUE | 57,343,720 | 40.9% |
| CALL_ISINSTANCE | 7,372,520 | 5.3% |
| LOAD_GLOBAL_MODULE | 6,553,280 | 4.7% |
| COPY | 3,277,280 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 130,252,180 | 93.0% |
| POP_JUMP_IF_TRUE | 9,831,160 | 7.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,553,280 | 44.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,553,280 | 44.4% |
| STORE_FAST | 1,638,320 | 11.1% |
| TO_BOOL | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,745,240 | 100.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,638,320 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,638,360 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,638,320 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,638,360 | 100.0% |


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
|     deferred | 9,011,540 | 44.0% |
|          hit | 11,468,860 | 56.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 7.9% |
| Failure | 4,400 | 92.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 1,600 | 36.4% |
| remainder | 1,200 | 27.3% |
| add different types | 800 | 18.2% |
| subtract different types | 800 | 18.2% |


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
|     deferred | 120 | 0.0% |
|          hit | 58,163,080 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 73,730,920 | 35.0% |
|          hit | 136,806,100 | 65.0% |
|         miss | 1,669,840 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 33,680 | 54.5% |
| Failure | 28,140 | 45.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 19,200 | 68.2% |
| cfunc noargs | 3,340 | 11.9% |
| meth descr varargs | 3,200 | 11.4% |
| cfunc varargs | 1,600 | 5.7% |
| init not simple | 800 | 2.8% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 560 | 0.0% |
|          hit | 22,118,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 140 | 0.0% |
|          hit | 6,554,900 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,097,420 | 3.5% |
|          hit | 356,365,080 | 96.4% |
|         miss | 1,653,960 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 35,440 | 86.4% |
| Failure | 5,600 | 13.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 3,200 | 57.1% |
| method | 800 | 14.3% |
| shadowed | 800 | 14.3% |
| class attr descriptor | 800 | 14.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,580 | 0.0% |
|          hit | 131,074,400 | 100.0% |
|         miss | 360 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,180 | 100.0% |
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
|     deferred | 880 | 0.0% |
|          hit | 36,043,920 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 880 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,278,300 | 1.9% |
|          hit | 167,934,620 | 98.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,380 | 46.3% |
| Failure | 1,600 | 53.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 1,600 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 1,638,360 | 100.0% |

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
| Basic | 1,083,337,400 | 44.7% |
| Not specialized | 292,523,080 | 12.1% |
| Specialized hits | 1,046,468,680 | 43.1% |
| Specialized misses | 3,324,160 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 73,730,920 | 74.4% |
| LOAD_ATTR | 13,097,420 | 13.2% |
| BINARY_OP | 9,011,540 | 9.1% |
| TO_BOOL | 3,278,300 | 3.3% |
| LOAD_GLOBAL | 2,580 | 0.0% |
| STORE_ATTR | 880 | 0.0% |
| COMPARE_OP | 560 | 0.0% |
| FOR_ITER | 140 | 0.0% |
| BINARY_SUBSCR | 120 | 0.0% |
| STORE_SUBSCR | 60 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,669,840 | 50.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,653,960 | 49.8% |
| LOAD_GLOBAL_BUILTIN | 180 | 0.0% |
| LOAD_GLOBAL_MODULE | 180 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| NOP | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 4,096,460 | 2.5% |
| Calls to Python functions inlined | 158,925,540 | 97.5% |
| Calls via PyEval_EvalFrame (total) | 4,096,460 | 2.5% |
| Calls via PyEval_EvalFrame (vector) | 4,096,460 | 2.5% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 4,096,460 | 2.5% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 480 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 100 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 4,915,420 | 3.0% |
| Frames pushed | 163,022,000 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 86,017,340 | 63.6% |
| Frees to freelist | 86,017,280 |  |
| Allocations | 49,171,753 | 36.4% |
| Allocations to 512 bytes | 49,171,513 | 36.4% |
| Allocations to 4 kbytes | 80 | 0.0% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 49,170,957 |  |
| New values | 1,638,400 |  |
| Interpreter increfs | 1,007,406,500 | 85.9% |
| Interpreter decrefs | 1,160,085,453 | 88.5% |
| Increfs | 165,381,022 | 14.1% |
| Decrefs | 151,166,498 | 11.5% |
| Materialize dict (on request) | 1,638,400 | 100.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 1,638,360 | 100.0% |
| Method cache hits | 24,603,431 |  |
| Method cache misses | 3,009 |  |
| Method cache collisions | 2,649 |  |
| Method cache dunder hits | 14,747,592 |  |
| Method cache dunder misses | 648 |  |


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
| Optimization attempts | 140 |  |
| Traces created | 140 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 40 | 28.6% |
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
| <= 32 | 60 | 42.9% |
| <= 64 | 0 | 0.0% |
| <= 128 | 80 | 57.1% |


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
| <= 16 | 60 | 42.9% |
| <= 32 | 0 | 0.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 80 | 57.1% |


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
| CALL | 100 |


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
| Number of data files | 60 |


</details>

---
Stats gathered on: 2024-09-10
