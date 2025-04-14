
# Pystats results

- benchmark: logging
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 580,816,180 | 22.6% | 22.6% |  |
| POP_JUMP_IF_FALSE | 168,755,860 | 6.6% | 29.2% |  |
| RESUME_CHECK | 163,020,600 | 6.3% | 35.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 154,858,780 | 6.0% | 41.6% | 1.1% |
| TO_BOOL_BOOL | 144,997,580 | 5.6% | 47.2% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 135,985,860 | 5.3% | 52.5% |  |
| LOAD_GLOBAL_MODULE | 124,518,460 | 4.9% | 57.4% | 0.0% |
| CALL_PY_EXACT_ARGS | 103,218,320 | 4.0% | 61.4% |  |
| RETURN_VALUE | 97,485,760 | 3.8% | 65.2% |  |
| STORE_FAST | 79,955,180 | 3.1% | 68.3% |  |
| POP_TOP | 75,367,540 | 2.9% | 71.2% |  |
| CALL | 72,122,900 | 2.8% | 74.0% |  |
| LOAD_CONST | 67,175,060 | 2.6% | 76.7% |  |
| RETURN_CONST | 65,536,240 | 2.6% | 79.2% |  |
| NOP | 62,259,440 | 2.4% | 81.6% |  |
| BINARY_SUBSCR_DICT | 55,705,540 | 2.2% | 83.8% |  |
| LOAD_FAST_LOAD_FAST | 46,694,640 | 1.8% | 85.6% |  |
| LOAD_ATTR_MODULE | 39,321,500 | 1.5% | 87.2% |  |
| STORE_ATTR_INSTANCE_VALUE | 36,043,920 | 1.4% | 88.6% |  |
| PUSH_NULL | 19,662,000 | 0.8% | 89.3% |  |
| LOAD_GLOBAL_BUILTIN | 19,660,940 | 0.8% | 90.1% | 0.0% |
| LOAD_ATTR | 18,038,420 | 0.7% | 90.8% |  |
| POP_JUMP_IF_TRUE | 18,022,400 | 0.7% | 91.5% |  |
| COMPARE_OP_INT | 15,564,680 | 0.6% | 92.1% |  |
| TO_BOOL_NONE | 14,745,240 | 0.6% | 92.7% |  |
| LOAD_ATTR_METHOD_NO_DICT | 11,468,680 | 0.4% | 93.1% |  |
| JUMP_BACKWARD | 10,321,920 | 0.4% | 93.5% |  |
| BINARY_OP | 9,016,320 | 0.4% | 93.9% |  |
| COPY | 8,192,060 | 0.3% | 94.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 8,191,960 | 0.3% | 94.5% |  |
| LOAD_ATTR_SLOT | 8,191,880 | 0.3% | 94.8% |  |
| CALL_ISINSTANCE | 7,372,660 | 0.3% | 95.1% |  |
| JUMP_FORWARD | 6,553,660 | 0.3% | 95.4% |  |
| BINARY_SLICE | 6,553,600 | 0.3% | 95.6% |  |
| POP_JUMP_IF_NOT_NONE | 6,553,600 | 0.3% | 95.9% |  |
| COMPARE_OP_STR | 6,553,520 | 0.3% | 96.1% |  |
| FOR_ITER_LIST | 6,553,520 | 0.3% | 96.4% |  |
| BINARY_OP_ADD_INT | 6,553,480 | 0.3% | 96.7% |  |
| TO_BOOL_ALWAYS_TRUE | 6,553,440 | 0.3% | 96.9% |  |
| CALL_BUILTIN_FAST | 5,734,440 | 0.2% | 97.1% |  |
| FOR_ITER_RANGE | 5,406,900 | 0.2% | 97.3% |  |
| GET_ITER | 4,915,440 | 0.2% | 97.5% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,915,440 | 0.2% | 97.7% |  |
| POP_JUMP_IF_NONE | 4,915,200 | 0.2% | 97.9% |  |
| BUILD_TUPLE | 4,915,200 | 0.2% | 98.1% |  |
| INTERPRETER_EXIT | 4,096,460 | 0.2% | 98.3% |  |
| TO_BOOL | 3,281,280 | 0.1% | 98.4% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 3,277,260 | 0.1% | 98.5% |  |
| CALL_BUILTIN_CLASS | 3,276,900 | 0.1% | 98.7% |  |
| BEFORE_WITH | 3,276,860 | 0.1% | 98.8% |  |
| STORE_FAST_STORE_FAST | 3,276,800 | 0.1% | 98.9% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,276,720 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 2,457,540 | 0.1% | 99.1% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,670,020 | 0.1% | 99.2% | 100.0% |
| CALL_FUNCTION_EX | 1,638,880 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_FLOAT | 1,638,540 | 0.1% | 99.3% |  |
| BUILD_MAP | 1,638,400 | 0.1% | 99.4% |  |
| CONTAINS_OP | 1,638,400 | 0.1% | 99.5% |  |
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
| STORE_ATTR | 1,760 | 0.0% | 100.0% |  |
| RESUME | 1,400 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 154,007,200 | 6.0% | 6.0% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 132,707,880 | 5.2% | 11.2% |
| RESUME_CHECK LOAD_FAST | 131,071,720 | 5.1% | 16.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 130,252,180 | 5.1% | 21.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 103,218,320 | 4.0% | 25.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 72,907,920 | 2.8% | 28.2% |
| RETURN_CONST POP_TOP | 60,621,040 | 2.4% | 30.6% |
| RETURN_VALUE TO_BOOL_BOOL | 60,620,520 | 2.4% | 32.9% |
| LOAD_FAST CALL | 59,803,480 | 2.3% | 35.3% |
| NOP LOAD_FAST | 58,982,400 | 2.3% | 37.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 57,344,000 | 2.2% | 39.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 57,343,860 | 2.2% | 42.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 57,343,720 | 2.2% | 44.3% |
| POP_JUMP_IF_FALSE NOP | 55,705,600 | 2.2% | 46.4% |
| BINARY_SUBSCR_DICT RETURN_VALUE | 55,705,540 | 2.2% | 48.6% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 55,705,400 | 2.2% | 50.8% |
| POP_TOP LOAD_FAST | 55,214,380 | 2.2% | 52.9% |
| CALL RESUME_CHECK | 54,067,300 | 2.1% | 55.0% |
| LOAD_FAST BINARY_SUBSCR_DICT | 54,067,080 | 2.1% | 57.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 54,067,080 | 2.1% | 59.2% |
| STORE_FAST LOAD_FAST | 52,101,580 | 2.0% | 61.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 33,587,560 | 1.3% | 62.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 30,309,720 | 1.2% | 63.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 29,490,080 | 1.1% | 64.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 22,118,060 | 0.9% | 65.8% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 19,659,840 | 0.8% | 66.5% |
| LOAD_FAST LOAD_ATTR | 18,028,440 | 0.7% | 67.2% |
| LOAD_ATTR_MODULE PUSH_NULL | 18,022,660 | 0.7% | 67.9% |
| LOAD_FAST LOAD_CONST | 17,203,360 | 0.7% | 68.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 16,383,200 | 0.6% | 69.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 14,745,640 | 0.6% | 69.8% |
| RETURN_VALUE STORE_FAST | 14,745,600 | 0.6% | 70.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 14,745,400 | 0.6% | 71.0% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 14,745,240 | 0.6% | 71.5% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 13,106,880 | 0.5% | 72.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 12,287,960 | 0.5% | 72.5% |
| LOAD_FAST RETURN_VALUE | 11,469,040 | 0.4% | 73.0% |
| LOAD_CONST COMPARE_OP_INT | 10,649,280 | 0.4% | 73.4% |
| LOAD_FAST STORE_FAST | 9,830,460 | 0.4% | 73.8% |
| LOAD_CONST LOAD_FAST | 9,830,400 | 0.4% | 74.2% |
| LOAD_CONST STORE_FAST | 9,830,400 | 0.4% | 74.5% |
| STORE_FAST LOAD_GLOBAL_MODULE | 9,830,280 | 0.4% | 74.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 9,829,920 | 0.4% | 75.3% |
| LOAD_ATTR_MODULE LOAD_ATTR_MODULE | 9,010,920 | 0.4% | 75.7% |
| PUSH_NULL LOAD_FAST | 8,192,480 | 0.3% | 76.0% |
| POP_TOP RETURN_CONST | 8,192,240 | 0.3% | 76.3% |
| RETURN_VALUE RETURN_VALUE | 8,192,240 | 0.3% | 76.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 8,192,100 | 0.3% | 76.9% |
| LOAD_ATTR STORE_FAST | 8,192,040 | 0.3% | 77.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 8,192,000 | 0.3% | 77.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 8,192,000 | 0.3% | 77.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 8,191,940 | 0.3% | 78.2% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 8,191,880 | 0.3% | 78.5% |
| LOAD_ATTR_MODULE LOAD_FAST | 8,191,880 | 0.3% | 78.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 8,191,840 | 0.3% | 79.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 7,372,520 | 0.3% | 79.5% |
| POP_TOP JUMP_BACKWARD | 7,045,120 | 0.3% | 79.7% |
| CALL STORE_FAST | 6,554,140 | 0.3% | 80.0% |
| LOAD_CONST LOAD_CONST | 6,553,720 | 0.3% | 80.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 6,553,600 | 0.3% | 80.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 6,553,600 | 0.3% | 80.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 6,553,600 | 0.3% | 81.0% |
| RETURN_VALUE LOAD_FAST | 6,553,560 | 0.3% | 81.3% |
| COPY TO_BOOL_BOOL | 6,553,440 | 0.3% | 81.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 6,553,320 | 0.3% | 81.8% |
| LOAD_FAST TO_BOOL_NONE | 6,553,280 | 0.3% | 82.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 6,553,280 | 0.3% | 82.3% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_NONE | 6,553,280 | 0.3% | 82.5% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 6,553,280 | 0.3% | 82.8% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 6,553,280 | 0.3% | 83.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 5,406,660 | 0.2% | 83.3% |
| FOR_ITER_RANGE STORE_FAST | 5,406,660 | 0.2% | 83.5% |
| PUSH_NULL CALL | 4,916,000 | 0.2% | 83.7% |
| LOAD_CONST BINARY_OP | 4,915,640 | 0.2% | 83.8% |
| LOAD_ATTR LOAD_ATTR_SLOT | 4,915,240 | 0.2% | 84.0% |
| POP_TOP LOAD_CONST | 4,915,200 | 0.2% | 84.2% |
| LOAD_FAST POP_JUMP_IF_NONE | 4,915,200 | 0.2% | 84.4% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 4,915,200 | 0.2% | 84.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 4,915,200 | 0.2% | 84.8% |
| STORE_FAST LOAD_CONST | 4,915,200 | 0.2% | 85.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS RETURN_VALUE | 4,915,200 | 0.2% | 85.2% |
| COMPARE_OP_STR COPY | 4,915,160 | 0.2% | 85.4% |
| FOR_ITER_LIST LOAD_FAST | 4,915,160 | 0.2% | 85.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 4,915,140 | 0.2% | 85.8% |
| LOAD_ATTR_INSTANCE_VALUE GET_ITER | 4,915,120 | 0.2% | 86.0% |
| LOAD_GLOBAL_MODULE COMPARE_OP_STR | 4,915,120 | 0.2% | 86.1% |
| RESUME_CHECK NOP | 4,915,120 | 0.2% | 86.3% |
| BINARY_OP_ADD_INT STORE_FAST | 4,915,120 | 0.2% | 86.5% |
| LOAD_ATTR_SLOT CALL_PY_EXACT_ARGS | 4,915,120 | 0.2% | 86.7% |
| GET_ITER FOR_ITER_LIST | 4,915,080 | 0.2% | 86.9% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 4,915,080 | 0.2% | 87.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 4,915,080 | 0.2% | 87.3% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 4,915,080 | 0.2% | 87.5% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 4,915,040 | 0.2% | 87.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 4,915,000 | 0.2% | 87.9% |
| LOAD_CONST CALL_BUILTIN_FAST | 4,914,960 | 0.2% | 88.1% |
| LOAD_FAST TO_BOOL_ALWAYS_TRUE | 4,914,960 | 0.2% | 88.3% |
| CACHE RESUME_CHECK | 4,096,260 | 0.2% | 88.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 4,096,080 | 0.2% | 88.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 4,096,060 | 0.2% | 88.7% |


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
| JUMP_BACKWARD | 7,045,120 | 9.3% |
| LOAD_CONST | 4,915,200 | 6.5% |
| NOP | 240 | 0.0% |


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
| LOAD_ATTR_MODULE | 18,022,660 | 91.7% |
| LOAD_ATTR | 1,638,860 | 8.3% |
| LOAD_DEREF | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,192,480 | 41.7% |
| CALL | 4,916,000 | 25.0% |
| LOAD_CONST | 1,638,400 | 8.3% |
| LOAD_FAST_LOAD_FAST | 1,638,400 | 8.3% |
| CALL_PY_EXACT_ARGS | 1,638,320 | 8.3% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 55,705,540 | 57.1% |
| LOAD_FAST | 11,469,040 | 11.8% |
| RETURN_VALUE | 8,192,240 | 8.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,915,200 | 5.0% |
| POP_JUMP_IF_TRUE | 3,276,800 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 60,620,520 | 62.2% |
| STORE_FAST | 14,745,600 | 15.1% |
| RETURN_VALUE | 8,192,240 | 8.4% |
| LOAD_FAST | 6,553,560 | 6.7% |
| POP_TOP | 1,638,400 | 1.7% |


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

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,803,480 | 82.9% |
| PUSH_NULL | 4,916,000 | 6.8% |
| LOAD_CONST | 3,277,380 | 4.5% |
| LOAD_GLOBAL_MODULE | 1,638,580 | 2.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,638,360 | 2.3% |

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

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 4,915,160 | 60.0% |
| CONTAINS_OP | 1,638,400 | 20.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,360 | 20.0% |
| COMPARE_OP | 100 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,553,440 | 80.0% |
| STORE_FAST | 1,638,400 | 20.0% |
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

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,045,120 | 68.3% |
| POP_JUMP_IF_FALSE | 3,276,800 | 31.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 5,406,660 | 52.4% |
| LOAD_FAST | 3,276,800 | 31.7% |
| FOR_ITER_LIST | 1,638,360 | 15.9% |
| FOR_ITER | 100 | 0.0% |


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
| LOAD_FAST | 18,028,440 | 99.9% |
| LOAD_ATTR | 7,720 | 0.0% |
| LOAD_GLOBAL_MODULE | 760 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |
| LOAD_ATTR_MODULE | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,192,040 | 45.4% |
| LOAD_ATTR_SLOT | 4,915,240 | 27.2% |
| LOAD_FAST | 1,639,940 | 9.1% |
| PUSH_NULL | 1,638,860 | 9.1% |
| TO_BOOL_BOOL | 1,638,320 | 9.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,203,360 | 25.6% |
| LOAD_CONST | 6,553,720 | 9.8% |
| POP_TOP | 4,915,200 | 7.3% |
| LOAD_FAST_LOAD_FAST | 4,915,200 | 7.3% |
| STORE_FAST | 4,915,200 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 10,649,280 | 15.9% |
| LOAD_FAST | 9,830,400 | 14.6% |
| STORE_FAST | 9,830,400 | 14.6% |
| LOAD_CONST | 6,553,720 | 9.8% |
| BINARY_OP_ADD_INT | 6,553,320 | 9.8% |


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
| RESUME_CHECK | 131,071,720 | 22.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 72,907,920 | 12.6% |
| NOP | 58,982,400 | 10.2% |
| LOAD_ATTR_INSTANCE_VALUE | 57,343,860 | 9.9% |
| POP_TOP | 55,214,380 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 154,007,200 | 26.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 132,707,880 | 22.8% |
| CALL | 59,803,480 | 10.3% |
| BINARY_SUBSCR_DICT | 54,067,080 | 9.3% |
| CALL_PY_EXACT_ARGS | 29,490,080 | 5.1% |


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
| LOAD_FAST_LOAD_FAST | 8,192,000 | 17.5% |
| STORE_FAST | 6,553,600 | 14.0% |
| LOAD_GLOBAL_MODULE | 4,096,080 | 8.8% |
| POP_JUMP_IF_FALSE | 4,096,060 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 16,383,200 | 35.1% |
| LOAD_FAST_LOAD_FAST | 8,192,000 | 17.5% |
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
| COMPARE_OP_INT | 12,287,960 | 7.3% |
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
| LOAD_FAST | 6,553,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,553,600 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 14,745,400 | 81.8% |
| COMPARE_OP_INT | 1,638,360 | 9.1% |
| TO_BOOL_ALWAYS_TRUE | 1,638,360 | 9.1% |
| TO_BOOL | 240 | 0.0% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,192,000 | 45.5% |
| RETURN_VALUE | 3,276,800 | 18.2% |
| LOAD_CONST | 3,276,800 | 18.2% |
| POP_TOP | 1,638,400 | 9.1% |
| LOAD_GLOBAL_BUILTIN | 1,638,320 | 9.1% |


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
| RETURN_VALUE | 14,745,600 | 18.4% |
| LOAD_FAST | 9,830,460 | 12.3% |
| LOAD_CONST | 9,830,400 | 12.3% |
| LOAD_ATTR | 8,192,040 | 10.2% |
| CALL | 6,554,140 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,101,580 | 65.2% |
| LOAD_GLOBAL_MODULE | 9,830,280 | 12.3% |
| LOAD_FAST_LOAD_FAST | 6,553,600 | 8.2% |
| LOAD_CONST | 4,915,200 | 6.1% |
| LOAD_GLOBAL_BUILTIN | 3,276,880 | 4.1% |


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
| CALL_LEN | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 55,705,400 | 54.0% |
| LOAD_FAST | 29,490,080 | 28.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,553,280 | 6.3% |
| LOAD_ATTR_SLOT | 4,915,120 | 4.8% |
| LOAD_FAST_LOAD_FAST | 3,276,640 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 103,218,320 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,649,280 | 68.4% |
| LOAD_FAST_LOAD_FAST | 3,276,640 | 21.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,638,320 | 10.5% |
| COMPARE_OP | 360 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,287,960 | 78.9% |
| RETURN_VALUE | 1,638,360 | 10.5% |
| POP_JUMP_IF_TRUE | 1,638,360 | 10.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,406,660 | 100.0% |
| GET_ITER | 180 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,406,660 | 100.0% |
| LOAD_GLOBAL | 120 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |


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

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 132,707,880 | 97.6% |
| LOAD_ATTR_INSTANCE_VALUE | 3,276,640 | 2.4% |
| LOAD_ATTR | 1,340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,907,920 | 53.6% |
| LOAD_GLOBAL_MODULE | 54,067,080 | 39.8% |
| CALL_PY_EXACT_ARGS | 6,553,280 | 4.8% |
| LOAD_FAST_LOAD_FAST | 2,457,360 | 1.8% |
| CALL | 160 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 30,309,720 | 77.1% |
| LOAD_ATTR_MODULE | 9,010,920 | 22.9% |
| LOAD_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 18,022,660 | 45.8% |
| LOAD_ATTR_MODULE | 9,010,920 | 22.9% |
| LOAD_FAST | 8,191,880 | 20.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,276,640 | 8.3% |
| CALL_ISINSTANCE | 819,160 | 2.1% |


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
| LOAD_ATTR_METHOD_WITH_VALUES | 54,067,080 | 43.4% |
| RESUME_CHECK | 22,118,060 | 17.8% |
| STORE_FAST | 9,830,280 | 7.9% |
| STORE_ATTR_INSTANCE_VALUE | 9,829,920 | 7.9% |
| LOAD_FAST | 8,191,940 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 55,705,400 | 44.7% |
| LOAD_ATTR_MODULE | 30,309,720 | 24.3% |
| LOAD_FAST | 8,192,100 | 6.6% |
| TO_BOOL_BOOL | 6,553,280 | 5.3% |
| COMPARE_OP_STR | 4,915,120 | 3.9% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 103,218,320 | 63.3% |
| CALL | 54,067,300 | 33.2% |
| CACHE | 4,096,260 | 2.5% |
| LOAD_ATTR_PROPERTY | 1,638,360 | 1.0% |
| CALL_FUNCTION_EX | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 131,071,720 | 80.4% |
| LOAD_GLOBAL_MODULE | 22,118,060 | 13.6% |
| NOP | 4,915,120 | 3.0% |
| LOAD_GLOBAL_BUILTIN | 3,276,720 | 2.0% |
| LOAD_CONST | 1,638,360 | 1.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60,620,520 | 41.8% |
| LOAD_ATTR_INSTANCE_VALUE | 57,343,720 | 39.5% |
| CALL_ISINSTANCE | 7,372,520 | 5.1% |
| COPY | 6,553,440 | 4.5% |
| LOAD_GLOBAL_MODULE | 6,553,280 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 130,252,180 | 89.8% |
| POP_JUMP_IF_TRUE | 14,745,400 | 10.2% |


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
| LOAD_FAST | 8,191,880 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,915,200 | 60.0% |
| STORE_FAST | 3,276,760 | 40.0% |


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

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,915,120 | 75.0% |
| LOAD_FAST | 1,638,320 | 25.0% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,915,160 | 75.0% |
| POP_JUMP_IF_FALSE | 1,638,360 | 25.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 4,915,080 | 75.0% |
| JUMP_BACKWARD | 1,638,360 | 25.0% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,915,160 | 75.0% |
| STORE_FAST | 1,638,360 | 25.0% |


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
| LOAD_ATTR | 4,915,240 | 60.0% |
| LOAD_FAST | 3,276,640 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,915,120 | 60.0% |
| LOAD_FAST | 3,276,720 | 40.0% |
| CALL | 40 | 0.0% |


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
|     deferred | 72,061,080 | 34.2% |
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
|          hit | 11,960,420 | 100.0% |

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
|     deferred | 17,995,780 | 4.8% |
|          hit | 356,365,080 | 94.8% |
|         miss | 1,653,960 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 35,440 | 83.1% |
| Failure | 7,200 | 16.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 4,800 | 66.7% |
| method | 800 | 11.1% |
| shadowed | 800 | 11.1% |
| class attr descriptor | 800 | 11.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,220 | 0.0% |
|          hit | 144,179,040 | 100.0% |
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
| Basic | 1,147,058,140 | 44.7% |
| Not specialized | 307,267,400 | 12.0% |
| Specialized hits | 1,109,698,280 | 43.2% |
| Specialized misses | 3,324,160 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 72,061,080 | 70.4% |
| LOAD_ATTR | 17,995,780 | 17.6% |
| BINARY_OP | 9,011,540 | 8.8% |
| TO_BOOL | 3,278,300 | 3.2% |
| LOAD_GLOBAL | 2,220 | 0.0% |
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
| Frames pushed | 104,856,680 | 64.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 86,017,340 | 63.6% |
| Frees to freelist | 86,017,280 |  |
| Allocations | 49,150,794 | 36.4% |
| Allocations to 512 bytes | 49,150,634 | 36.4% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 49,150,178 |  |
| New values | 1,638,400 |  |
| Interpreter increfs | 1,069,079,620 | 92.0% |
| Interpreter decrefs | 1,197,679,834 | 92.1% |
| Increfs | 93,388,027 | 8.0% |
| Decrefs | 103,231,478 | 7.9% |
| Materialize dict (on request) | 1,638,400 | 100.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 1,638,360 | 100.0% |
| Method cache hits | 24,604,908 |  |
| Method cache misses | 3,132 |  |
| Method cache collisions | 2,712 |  |
| Method cache dunder hits | 14,747,591 |  |
| Method cache dunder misses | 649 |  |


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
| Number of data files | 60 |


</details>

---
Stats gathered on: 2024-09-10
