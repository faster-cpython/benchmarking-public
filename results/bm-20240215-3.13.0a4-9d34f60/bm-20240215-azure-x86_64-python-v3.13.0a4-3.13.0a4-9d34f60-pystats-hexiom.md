
# Pystats results

- benchmark: hexiom
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 326,787,360 | 17.1% | 17.1% |  |
| STORE_FAST | 132,124,880 | 6.9% | 24.0% |  |
| LOAD_CONST | 129,022,880 | 6.8% | 30.8% |  |
| BINARY_SUBSCR_LIST_INT | 99,925,140 | 5.2% | 36.0% |  |
| POP_JUMP_IF_FALSE | 95,713,360 | 5.0% | 41.1% |  |
| RESUME_CHECK | 94,503,620 | 5.0% | 46.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 92,846,100 | 4.9% | 50.9% |  |
| JUMP_BACKWARD | 90,566,800 | 4.7% | 55.6% |  |
| COMPARE_OP_INT | 71,327,320 | 3.7% | 59.4% |  |
| FOR_ITER_LIST | 56,770,260 | 3.0% | 62.3% | 0.1% |
| RETURN_VALUE | 52,363,560 | 2.7% | 65.1% |  |
| LOAD_GLOBAL_BUILTIN | 51,702,200 | 2.7% | 67.8% |  |
| LOAD_DEREF | 50,459,120 | 2.6% | 70.4% |  |
| CONTAINS_OP | 48,643,840 | 2.5% | 73.0% |  |
| CALL_PY_EXACT_ARGS | 48,352,460 | 2.5% | 75.5% |  |
| CALL_LEN | 46,942,600 | 2.5% | 78.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 45,952,600 | 2.4% | 80.4% |  |
| TO_BOOL_BOOL | 43,684,640 | 2.3% | 82.7% |  |
| FOR_ITER_RANGE | 41,189,160 | 2.2% | 84.8% | 0.2% |
| POP_TOP | 39,518,060 | 2.1% | 86.9% |  |
| INTERPRETER_EXIT | 38,299,740 | 2.0% | 88.9% |  |
| YIELD_VALUE | 36,383,120 | 1.9% | 90.8% |  |
| LOAD_FAST_LOAD_FAST | 34,147,920 | 1.8% | 92.6% |  |
| POP_JUMP_IF_TRUE | 28,532,480 | 1.5% | 94.1% |  |
| BINARY_OP_ADD_INT | 10,563,260 | 0.6% | 94.7% |  |
| SWAP | 9,578,240 | 0.5% | 95.2% |  |
| LOAD_GLOBAL_MODULE | 9,386,880 | 0.5% | 95.6% |  |
| BINARY_SUBSCR_GETITEM | 9,245,180 | 0.5% | 96.1% |  |
| COPY | 8,791,040 | 0.5% | 96.6% |  |
| JUMP_FORWARD | 8,325,120 | 0.4% | 97.0% |  |
| GET_ITER | 7,410,080 | 0.4% | 97.4% |  |
| RETURN_CONST | 6,071,120 | 0.3% | 97.7% |  |
| STORE_SUBSCR_LIST_INT | 4,634,720 | 0.2% | 98.0% |  |
| BINARY_OP_SUBTRACT_INT | 4,415,740 | 0.2% | 98.2% |  |
| BINARY_SLICE | 3,173,120 | 0.2% | 98.4% |  |
| STORE_FAST_LOAD_FAST | 2,890,640 | 0.2% | 98.5% |  |
| LIST_APPEND | 2,877,440 | 0.2% | 98.7% |  |
| CALL_BUILTIN_CLASS | 2,792,420 | 0.1% | 98.8% |  |
| BUILD_TUPLE | 2,375,680 | 0.1% | 98.9% |  |
| STORE_DEREF | 2,211,840 | 0.1% | 99.1% |  |
| MAKE_FUNCTION | 1,914,960 | 0.1% | 99.2% |  |
| RETURN_GENERATOR | 1,914,960 | 0.1% | 99.3% |  |
| COPY_FREE_VARS | 1,914,960 | 0.1% | 99.4% |  |
| SET_FUNCTION_ATTRIBUTE | 1,914,880 | 0.1% | 99.5% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,914,860 | 0.1% | 99.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,165,300 | 0.1% | 99.6% |  |
| BUILD_LIST | 1,017,680 | 0.1% | 99.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 944,360 | 0.0% | 99.7% |  |
| POP_JUMP_IF_NOT_NONE | 697,600 | 0.0% | 99.8% |  |
| EXTENDED_ARG | 652,800 | 0.0% | 99.8% |  |
| CALL_LIST_APPEND | 597,700 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 558,120 | 0.0% | 99.9% |  |
| EXIT_INIT_CHECK | 313,480 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 313,480 | 0.0% | 99.9% |  |
| MAKE_CELL | 276,480 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 273,880 | 0.0% | 99.9% |  |
| LOAD_ATTR_CLASS | 250,860 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 208,640 | 0.0% | 99.9% |  |
| CALL_PY_WITH_DEFAULTS | 206,000 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 166,480 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 166,420 | 0.0% | 100.0% |  |
| NOP | 133,200 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 131,860 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 48,620 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 48,560 | 0.0% | 100.0% |  |
| CALL_KW | 38,400 | 0.0% | 100.0% |  |
| BINARY_OP | 35,940 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 24,280 | 0.0% | 100.0% |  |
| CALL_STR_1 | 15,320 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 10,140 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 8,160 | 0.0% | 100.0% |  |
| CALL | 7,440 | 0.0% | 100.0% |  |
| LOAD_ATTR | 4,760 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 2,120 | 0.0% | 100.0% |  |
| PUSH_NULL | 1,760 | 0.0% | 100.0% |  |
| COMPARE_OP | 1,560 | 0.0% | 100.0% |  |
| FOR_ITER | 1,560 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 1,500 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,320 | 0.0% | 100.0% |  |
| BUILD_MAP | 1,280 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,260 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 1,260 | 0.0% | 100.0% |  |
| TO_BOOL | 960 | 0.0% | 100.0% |  |
| RESUME | 700 | 0.0% | 100.0% |  |
| STORE_ATTR | 560 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 400 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 83,959,760 | 4.4% | 4.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 79,257,300 | 4.2% | 8.6% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 78,692,800 | 4.1% | 12.7% |
| STORE_FAST LOAD_FAST | 70,811,120 | 3.7% | 16.4% |
| FOR_ITER_LIST STORE_FAST | 51,885,400 | 2.7% | 19.1% |
| JUMP_BACKWARD FOR_ITER_LIST | 51,741,360 | 2.7% | 21.8% |
| LOAD_CONST COMPARE_OP_INT | 51,442,760 | 2.7% | 24.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 48,790,680 | 2.6% | 27.1% |
| CALL_LEN LOAD_CONST | 46,768,540 | 2.5% | 29.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 46,163,660 | 2.4% | 31.9% |
| LOAD_DEREF LOAD_FAST | 44,907,520 | 2.4% | 34.3% |
| LOAD_FAST CONTAINS_OP | 44,907,520 | 2.4% | 36.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 44,551,800 | 2.3% | 39.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 41,590,600 | 2.2% | 41.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 41,473,680 | 2.2% | 43.3% |
| RETURN_VALUE TO_BOOL_BOOL | 40,032,600 | 2.1% | 45.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 39,923,200 | 2.1% | 47.5% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 39,834,520 | 2.1% | 49.6% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 39,382,880 | 2.1% | 51.7% |
| COMPARE_OP_INT RETURN_VALUE | 39,313,900 | 2.1% | 53.7% |
| BINARY_SUBSCR_LIST_INT CALL_LEN | 39,313,880 | 2.1% | 55.8% |
| POP_JUMP_IF_FALSE LOAD_CONST | 39,159,040 | 2.1% | 57.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 38,482,960 | 2.0% | 59.9% |
| POP_TOP JUMP_BACKWARD | 36,516,280 | 1.9% | 61.8% |
| CACHE RESUME_CHECK | 36,384,640 | 1.9% | 63.7% |
| YIELD_VALUE INTERPRETER_EXIT | 36,383,120 | 1.9% | 65.6% |
| RESUME_CHECK POP_TOP | 36,383,080 | 1.9% | 67.5% |
| STORE_FAST LOAD_DEREF | 36,382,720 | 1.9% | 69.4% |
| FOR_ITER_RANGE STORE_FAST | 33,722,880 | 1.8% | 71.2% |
| LOAD_CONST YIELD_VALUE | 28,193,280 | 1.5% | 72.6% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 22,851,780 | 1.2% | 73.8% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 20,794,880 | 1.1% | 74.9% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 17,112,320 | 0.9% | 75.8% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 16,083,000 | 0.8% | 76.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 15,930,420 | 0.8% | 77.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 14,087,760 | 0.7% | 78.2% |
| RESUME_CHECK LOAD_FAST | 13,936,420 | 0.7% | 79.0% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 11,731,000 | 0.6% | 79.6% |
| BINARY_SUBSCR_LIST_INT RETURN_VALUE | 11,310,040 | 0.6% | 80.2% |
| BINARY_OP_ADD_INT STORE_FAST | 10,310,040 | 0.5% | 80.7% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 10,303,560 | 0.5% | 81.3% |
| LOAD_FAST LOAD_CONST | 10,191,360 | 0.5% | 81.8% |
| LOAD_CONST BINARY_OP_ADD_INT | 10,060,040 | 0.5% | 82.3% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 9,932,600 | 0.5% | 82.8% |
| BINARY_SUBSCR_GETITEM RESUME_CHECK | 9,245,180 | 0.5% | 83.3% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_GETITEM | 9,195,040 | 0.5% | 83.8% |
| CONTAINS_OP POP_JUMP_IF_TRUE | 8,574,720 | 0.4% | 84.3% |
| POP_JUMP_IF_FALSE LOAD_DEREF | 8,524,800 | 0.4% | 84.7% |
| JUMP_FORWARD YIELD_VALUE | 8,189,440 | 0.4% | 85.1% |
| LOAD_CONST JUMP_FORWARD | 8,189,440 | 0.4% | 85.6% |
| STORE_FAST JUMP_BACKWARD | 7,806,720 | 0.4% | 86.0% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 7,800,320 | 0.4% | 86.4% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 7,788,160 | 0.4% | 86.8% |
| POP_JUMP_IF_TRUE LOAD_FAST_LOAD_FAST | 7,627,520 | 0.4% | 87.2% |
| LOAD_GLOBAL_MODULE COMPARE_OP_INT | 7,413,360 | 0.4% | 87.6% |
| RETURN_VALUE LOAD_CONST | 7,204,940 | 0.4% | 88.0% |
| LOAD_CONST STORE_FAST | 6,406,400 | 0.3% | 88.3% |
| LOAD_FAST CALL_LEN | 5,763,680 | 0.3% | 88.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 5,692,240 | 0.3% | 88.9% |
| BINARY_SUBSCR_LIST_INT LOAD_GLOBAL_MODULE | 5,642,040 | 0.3% | 89.2% |
| LOAD_DEREF BINARY_SUBSCR_LIST_INT | 5,232,520 | 0.3% | 89.5% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 4,407,880 | 0.2% | 89.7% |
| COPY COPY | 4,395,520 | 0.2% | 89.9% |
| SWAP SWAP | 4,395,520 | 0.2% | 90.2% |
| COPY BINARY_SUBSCR_LIST_INT | 4,395,360 | 0.2% | 90.4% |
| SWAP STORE_SUBSCR_LIST_INT | 4,395,360 | 0.2% | 90.6% |
| BINARY_OP_SUBTRACT_INT SWAP | 4,371,160 | 0.2% | 90.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_DEREF | 4,126,680 | 0.2% | 91.1% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,965,080 | 0.2% | 91.3% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 3,938,440 | 0.2% | 91.5% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 3,850,120 | 0.2% | 91.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 3,714,440 | 0.2% | 91.9% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 3,714,200 | 0.2% | 92.1% |
| BINARY_SUBSCR_LIST_INT CONTAINS_OP | 3,477,740 | 0.2% | 92.2% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 3,380,480 | 0.2% | 92.4% |
| RETURN_CONST TO_BOOL_BOOL | 3,380,360 | 0.2% | 92.6% |
| LOAD_CONST LOAD_CONST | 3,290,880 | 0.2% | 92.8% |
| LOAD_CONST BINARY_SLICE | 3,148,800 | 0.2% | 92.9% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 3,102,680 | 0.2% | 93.1% |
| BINARY_SUBSCR_LIST_INT COPY | 3,097,580 | 0.2% | 93.3% |
| POP_JUMP_IF_FALSE RETURN_CONST | 2,920,960 | 0.2% | 93.4% |
| LIST_APPEND JUMP_BACKWARD | 2,877,440 | 0.2% | 93.6% |
| BINARY_SLICE LIST_APPEND | 2,723,840 | 0.1% | 93.7% |
| FOR_ITER_RANGE STORE_FAST_LOAD_FAST | 2,723,820 | 0.1% | 93.9% |
| STORE_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,723,800 | 0.1% | 94.0% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 2,718,420 | 0.1% | 94.1% |
| STORE_FAST LOAD_CONST | 2,700,880 | 0.1% | 94.3% |
| CALL_BUILTIN_CLASS GET_ITER | 2,645,300 | 0.1% | 94.4% |
| GET_ITER FOR_ITER_RANGE | 2,508,420 | 0.1% | 94.5% |
| GET_ITER FOR_ITER_LIST | 2,500,900 | 0.1% | 94.7% |
| LOAD_FAST GET_ITER | 2,483,280 | 0.1% | 94.8% |
| STORE_DEREF LOAD_FAST | 2,211,840 | 0.1% | 94.9% |
| FOR_ITER_RANGE STORE_DEREF | 2,211,820 | 0.1% | 95.0% |
| LOAD_ATTR_INSTANCE_VALUE GET_ITER | 2,192,580 | 0.1% | 95.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 2,136,320 | 0.1% | 95.3% |
| LOAD_FAST COMPARE_OP_INT | 2,111,920 | 0.1% | 95.4% |
| RETURN_VALUE LOAD_ATTR_INSTANCE_VALUE | 2,088,720 | 0.1% | 95.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,060,360 | 0.1% | 95.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 2,009,320 | 0.1% | 95.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 1,962,040 | 0.1% | 95.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,148,800 | 99.2% |
| BINARY_OP_ADD_INT | 24,280 | 0.8% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 2,723,840 | 85.8% |
| STORE_FAST | 449,280 | 14.2% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 36,384,640 | 95.0% |
| POP_TOP | 1,914,960 | 5.0% |
| RESUME | 140 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 680 | 32.1% |
| LOAD_FAST_LOAD_FAST | 680 | 32.1% |
| LOAD_FAST | 440 | 20.8% |
| COPY | 160 | 7.5% |
| LOAD_DEREF | 120 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 620 | 29.2% |
| LOAD_CONST | 460 | 21.7% |
| BINARY_SUBSCR_GETITEM | 260 | 12.3% |
| CALL | 140 | 6.6% |
| LOAD_GLOBAL | 100 | 4.7% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 313,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 313,480 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 2,645,300 | 35.7% |
| LOAD_FAST | 2,483,280 | 33.5% |
| LOAD_ATTR_INSTANCE_VALUE | 2,192,580 | 29.6% |
| RETURN_VALUE | 62,700 | 0.8% |
| LOAD_GLOBAL_MODULE | 24,300 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 2,508,420 | 33.9% |
| FOR_ITER_LIST | 2,500,900 | 33.7% |
| CALL_PY_EXACT_ARGS | 1,914,880 | 25.8% |
| EXTENDED_ARG | 276,480 | 3.7% |
| LOAD_FAST_AND_CLEAR | 208,640 | 2.8% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 36,383,120 | 95.0% |
| RETURN_CONST | 1,916,360 | 5.0% |
| RETURN_VALUE | 260 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,914,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 1,914,880 | 100.0% |
| LOAD_FAST_CHECK | 80 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 113,920 | 85.5% |
| JUMP_BACKWARD | 19,200 | 14.4% |
| POP_TOP | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 133,040 | 99.9% |
| LOAD_DEREF | 80 | 0.1% |
| LOAD_GLOBAL | 80 | 0.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 36,383,080 | 92.1% |
| CACHE | 1,914,960 | 4.8% |
| CALL_METHOD_DESCRIPTOR_O | 558,060 | 1.4% |
| RETURN_CONST | 460,800 | 1.2% |
| SWAP | 162,560 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,516,280 | 92.4% |
| RESUME_CHECK | 1,914,920 | 4.8% |
| RETURN_CONST | 701,440 | 1.8% |
| RETURN_VALUE | 162,560 | 0.4% |
| LOAD_GLOBAL_MODULE | 145,760 | 0.4% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,500 | 85.2% |
| LOAD_DEREF | 160 | 9.1% |
| LOAD_ATTR | 100 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,600 | 90.9% |
| LOAD_FAST | 160 | 9.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,914,880 | 100.0% |
| CALL_PY_EXACT_ARGS | 60 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,914,840 | 100.0% |
| CALL | 80 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 39,313,900 | 75.1% |
| BINARY_SUBSCR_LIST_INT | 11,310,040 | 21.6% |
| LOAD_FAST | 779,600 | 1.5% |
| EXIT_INIT_CHECK | 313,480 | 0.6% |
| RETURN_VALUE | 208,680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 40,032,600 | 76.5% |
| LOAD_CONST | 7,204,940 | 13.8% |
| LOAD_ATTR_INSTANCE_VALUE | 2,088,720 | 4.0% |
| CALL_LEN | 1,864,920 | 3.6% |
| STORE_FAST | 642,480 | 1.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 160 | 40.0% |
| LOAD_FAST | 120 | 30.0% |
| LOAD_ATTR | 40 | 10.0% |
| LOAD_FAST_LOAD_FAST | 40 | 10.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 160 | 40.0% |
| LOAD_FAST | 80 | 20.0% |
| LOAD_FAST_LOAD_FAST | 60 | 15.0% |
| JUMP_BACKWARD | 40 | 10.0% |
| STORE_SUBSCR_DICT | 40 | 10.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 680 | 70.8% |
| LOAD_FAST | 160 | 16.7% |
| RETURN_CONST | 120 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 480 | 50.0% |
| POP_JUMP_IF_FALSE | 360 | 37.5% |
| POP_JUMP_IF_TRUE | 120 | 12.5% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,000 | 75.1% |
| BINARY_OP_SUBTRACT_INT | 3,840 | 10.7% |
| BUILD_LIST | 2,560 | 7.1% |
| LOAD_CONST | 1,320 | 3.7% |
| BINARY_OP | 780 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 30,900 | 86.0% |
| STORE_FAST | 1,700 | 4.7% |
| LOAD_FAST | 1,340 | 3.7% |
| BINARY_OP | 780 | 2.2% |
| BINARY_OP_ADD_INT | 580 | 1.6% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 483,920 | 47.6% |
| STORE_FAST | 273,920 | 26.9% |
| SWAP | 208,640 | 20.5% |
| LOAD_FAST_LOAD_FAST | 24,320 | 2.4% |
| LOAD_GLOBAL_MODULE | 24,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 547,840 | 53.8% |
| LOAD_FAST | 209,920 | 20.6% |
| SWAP | 208,640 | 20.5% |
| LIST_APPEND | 24,320 | 2.4% |
| CALL_ALLOC_AND_ENTER_INIT | 24,240 | 2.4% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,260 | 98.4% |
| STORE_ATTR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,280 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,914,880 | 80.6% |
| LOAD_FAST_LOAD_FAST | 423,680 | 17.8% |
| LOAD_GLOBAL_MODULE | 37,100 | 1.6% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,914,880 | 80.6% |
| CALL_PY_EXACT_ARGS | 145,880 | 6.1% |
| LIST_APPEND | 121,600 | 5.1% |
| BINARY_SUBSCR_DICT | 107,480 | 4.5% |
| STORE_FAST | 48,640 | 2.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,680 | 22.6% |
| PUSH_NULL | 1,600 | 21.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,440 | 19.4% |
| LOAD_FAST_LOAD_FAST | 440 | 5.9% |
| LOAD_ATTR | 420 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,000 | 40.3% |
| CALL_PY_EXACT_ARGS | 900 | 12.1% |
| CALL_BUILTIN_CLASS | 620 | 8.3% |
| GET_ITER | 500 | 6.7% |
| RESUME | 440 | 5.9% |


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
| LOAD_CONST | 38,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 37,120 | 96.7% |
| RESUME_CHECK | 1,260 | 3.3% |
| RESUME | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 600 | 38.5% |
| LOAD_FAST_LOAD_FAST | 240 | 15.4% |
| LOAD_GLOBAL | 200 | 12.8% |
| LOAD_GLOBAL_MODULE | 200 | 12.8% |
| LOAD_ATTR | 100 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 680 | 43.6% |
| POP_JUMP_IF_FALSE | 520 | 33.3% |
| POP_JUMP_IF_TRUE | 240 | 15.4% |
| COMPARE_OP_STR | 100 | 6.4% |
| RETURN_VALUE | 20 | 1.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,907,520 | 92.3% |
| BINARY_SUBSCR_LIST_INT | 3,477,740 | 7.1% |
| LOAD_ATTR_INSTANCE_VALUE | 145,900 | 0.3% |
| RETURN_VALUE | 112,600 | 0.2% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 39,923,200 | 82.1% |
| POP_JUMP_IF_TRUE | 8,574,720 | 17.6% |
| RETURN_VALUE | 145,920 | 0.3% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,395,520 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 3,097,580 | 35.2% |
| LOAD_FAST_LOAD_FAST | 1,297,920 | 14.8% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,395,520 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 4,395,360 | 50.0% |
| BINARY_SUBSCR | 160 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,914,860 | 100.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 1,914,880 | 100.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 322,560 | 49.4% |
| GET_ITER | 276,480 | 42.4% |
| FOR_ITER_LIST | 53,760 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 547,580 | 83.9% |
| JUMP_BACKWARD | 53,760 | 8.2% |
| FOR_ITER_RANGE | 51,420 | 7.9% |
| FOR_ITER | 40 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 720 | 46.2% |
| GET_ITER | 680 | 43.6% |
| SWAP | 80 | 5.1% |
| EXTENDED_ARG | 40 | 2.6% |
| LOAD_FAST | 40 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 680 | 43.6% |
| FOR_ITER_RANGE | 520 | 33.3% |
| FOR_ITER_LIST | 260 | 16.7% |
| STORE_FAST_LOAD_FAST | 80 | 5.1% |
| STORE_DEREF | 20 | 1.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 36,516,280 | 40.3% |
| POP_JUMP_IF_FALSE | 20,794,880 | 23.0% |
| POP_JUMP_IF_TRUE | 17,112,320 | 18.9% |
| STORE_FAST | 7,806,720 | 8.6% |
| STORE_SUBSCR_LIST_INT | 3,102,680 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 51,741,360 | 57.1% |
| FOR_ITER_RANGE | 38,482,960 | 42.5% |
| EXTENDED_ARG | 322,560 | 0.4% |
| NOP | 19,200 | 0.0% |
| FOR_ITER | 720 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,189,440 | 98.4% |
| STORE_FAST | 113,920 | 1.4% |
| CALL_STR_1 | 15,320 | 0.2% |
| CALL_BUILTIN_CLASS | 5,080 | 0.1% |
| POP_JUMP_IF_FALSE | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 8,189,440 | 98.4% |
| LOAD_FAST | 80,640 | 1.0% |
| LOAD_GLOBAL_BUILTIN | 24,240 | 0.3% |
| STORE_FAST | 20,480 | 0.2% |
| LOAD_FAST_LOAD_FAST | 8,960 | 0.1% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 2,723,840 | 94.7% |
| BUILD_TUPLE | 121,600 | 4.2% |
| BUILD_LIST | 24,320 | 0.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 7,660 | 0.3% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,877,440 | 100.0% |


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
| LOAD_FAST | 3,240 | 68.1% |
| LOAD_FAST_LOAD_FAST | 360 | 7.6% |
| RETURN_VALUE | 240 | 5.0% |
| LOAD_GLOBAL | 200 | 4.2% |
| LOAD_GLOBAL_MODULE | 200 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,260 | 26.5% |
| LOAD_FAST | 820 | 17.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 680 | 14.3% |
| CALL | 420 | 8.8% |
| STORE_FAST | 320 | 6.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 46,768,540 | 36.2% |
| POP_JUMP_IF_FALSE | 39,159,040 | 30.4% |
| BINARY_SUBSCR_LIST_INT | 11,731,000 | 9.1% |
| LOAD_FAST | 10,191,360 | 7.9% |
| RETURN_VALUE | 7,204,940 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 51,442,760 | 39.9% |
| YIELD_VALUE | 28,193,280 | 21.9% |
| BINARY_SUBSCR_LIST_INT | 10,303,560 | 8.0% |
| BINARY_OP_ADD_INT | 10,060,040 | 7.8% |
| JUMP_FORWARD | 8,189,440 | 6.3% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 36,382,720 | 72.1% |
| POP_JUMP_IF_FALSE | 8,524,800 | 16.9% |
| LOAD_ATTR_INSTANCE_VALUE | 4,126,680 | 8.2% |
| LOAD_FAST | 1,127,680 | 2.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 296,940 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,907,520 | 89.0% |
| BINARY_SUBSCR_LIST_INT | 5,232,520 | 10.4% |
| CALL_PY_EXACT_ARGS | 318,640 | 0.6% |
| PUSH_NULL | 160 | 0.0% |
| BINARY_SUBSCR | 120 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 79,257,300 | 24.3% |
| STORE_FAST | 70,811,120 | 21.7% |
| LOAD_GLOBAL_BUILTIN | 48,790,680 | 14.9% |
| LOAD_DEREF | 44,907,520 | 13.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 41,590,600 | 12.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 83,959,760 | 25.7% |
| BINARY_SUBSCR_LIST_INT | 78,692,800 | 24.1% |
| CONTAINS_OP | 44,907,520 | 13.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 44,551,800 | 13.6% |
| CALL_PY_EXACT_ARGS | 41,473,680 | 12.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 208,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 208,640 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 80 | 100.0% |

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
| POP_JUMP_IF_FALSE | 7,800,320 | 22.8% |
| POP_JUMP_IF_TRUE | 7,627,520 | 22.3% |
| STORE_FAST | 5,692,240 | 16.7% |
| RESUME_CHECK | 3,938,440 | 11.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,714,440 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 9,932,600 | 29.1% |
| BINARY_SUBSCR_GETITEM | 9,195,040 | 26.9% |
| LOAD_ATTR_INSTANCE_VALUE | 3,965,080 | 11.6% |
| CALL_PY_EXACT_ARGS | 3,714,200 | 10.9% |
| LOAD_CONST | 3,380,480 | 9.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,340 | 31.6% |
| POP_JUMP_IF_FALSE | 560 | 13.2% |
| LOAD_FAST | 480 | 11.3% |
| POP_TOP | 240 | 5.7% |
| FOR_ITER_RANGE | 240 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,200 | 28.3% |
| LOAD_GLOBAL_BUILTIN | 920 | 21.7% |
| LOAD_FAST | 640 | 15.1% |
| LOAD_FAST_LOAD_FAST | 480 | 11.3% |
| LOAD_CONST | 260 | 6.1% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 273,880 | 99.1% |
| CALL_PY_WITH_DEFAULTS | 2,520 | 0.9% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 276,460 | 100.0% |
| RESUME | 20 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 39,923,200 | 41.7% |
| TO_BOOL_BOOL | 39,834,520 | 41.6% |
| COMPARE_OP_INT | 15,930,420 | 16.6% |
| COMPARE_OP_STR | 24,340 | 0.0% |
| COMPARE_OP | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,159,040 | 40.9% |
| JUMP_BACKWARD | 20,794,880 | 21.7% |
| LOAD_FAST | 14,087,760 | 14.7% |
| LOAD_DEREF | 8,524,800 | 8.9% |
| LOAD_FAST_LOAD_FAST | 7,800,320 | 8.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 697,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 692,480 | 99.3% |
| LOAD_GLOBAL_BUILTIN | 5,040 | 0.7% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 16,083,000 | 56.4% |
| CONTAINS_OP | 8,574,720 | 30.1% |
| TO_BOOL_BOOL | 3,850,120 | 13.5% |
| COMPARE_OP_STR | 24,280 | 0.1% |
| COMPARE_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,112,320 | 60.0% |
| LOAD_FAST_LOAD_FAST | 7,627,520 | 26.7% |
| LOAD_FAST | 2,136,320 | 7.5% |
| LOAD_GLOBAL_BUILTIN | 1,121,240 | 3.9% |
| LOAD_CONST | 460,800 | 1.6% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,920,960 | 48.1% |
| FOR_ITER_LIST | 1,916,240 | 31.6% |
| POP_TOP | 701,440 | 11.6% |
| STORE_ATTR_INSTANCE_VALUE | 313,520 | 5.2% |
| STORE_SUBSCR_LIST_INT | 209,900 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,380,360 | 55.7% |
| INTERPRETER_EXIT | 1,916,360 | 31.6% |
| POP_TOP | 460,800 | 7.6% |
| EXIT_INIT_CHECK | 313,480 | 5.2% |
| TO_BOOL | 120 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 1,914,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,914,880 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 50.0% |
| LOAD_FAST_LOAD_FAST | 280 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 280 | 50.0% |
| LOAD_FAST | 80 | 14.3% |
| RETURN_CONST | 80 | 14.3% |
| LOAD_FAST_LOAD_FAST | 60 | 10.7% |
| LOAD_CONST | 40 | 7.1% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 2,211,820 | 100.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,211,840 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 51,885,400 | 39.3% |
| FOR_ITER_RANGE | 33,722,880 | 25.5% |
| BINARY_SUBSCR_LIST_INT | 22,851,780 | 17.3% |
| BINARY_OP_ADD_INT | 10,310,040 | 7.8% |
| LOAD_CONST | 6,406,400 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 70,811,120 | 53.6% |
| LOAD_DEREF | 36,382,720 | 27.5% |
| JUMP_BACKWARD | 7,806,720 | 5.9% |
| LOAD_GLOBAL_BUILTIN | 7,788,160 | 5.9% |
| LOAD_FAST_LOAD_FAST | 5,692,240 | 4.3% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 2,723,820 | 94.2% |
| FOR_ITER_LIST | 166,740 | 5.8% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,723,800 | 94.2% |
| LOAD_GLOBAL_MODULE | 158,680 | 5.5% |
| LOAD_ATTR_METHOD_NO_DICT | 8,000 | 0.3% |
| LOAD_ATTR | 120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 166,420 | 100.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 142,080 | 85.3% |
| LOAD_GLOBAL_MODULE | 24,320 | 14.6% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 4,395,520 | 45.9% |
| BINARY_OP_SUBTRACT_INT | 4,371,160 | 45.6% |
| BUILD_LIST | 208,640 | 2.2% |
| LOAD_FAST_AND_CLEAR | 208,640 | 2.2% |
| FOR_ITER_RANGE | 144,640 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 4,395,520 | 45.9% |
| STORE_SUBSCR_LIST_INT | 4,395,360 | 45.9% |
| BUILD_LIST | 208,640 | 2.2% |
| STORE_FAST | 207,360 | 2.2% |
| POP_TOP | 162,560 | 1.7% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 33.3% |
| BINARY_SUBSCR | 20 | 16.7% |
| LOAD_ATTR | 20 | 16.7% |
| BINARY_SUBSCR_DICT | 20 | 16.7% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 50.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 28,193,280 | 77.5% |
| JUMP_FORWARD | 8,189,440 | 22.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 380 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 36,383,120 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 440 | 62.9% |
| CACHE | 140 | 20.0% |
| POP_TOP | 40 | 5.7% |
| CALL_FUNCTION_EX | 20 | 2.9% |
| CALL_KW | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 42.9% |
| LOAD_GLOBAL | 180 | 25.7% |
| LOAD_FAST_LOAD_FAST | 120 | 17.1% |
| POP_TOP | 40 | 5.7% |
| LOAD_CONST | 40 | 5.7% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,060,040 | 95.2% |
| LOAD_ATTR_INSTANCE_VALUE | 291,760 | 2.8% |
| CALL_LEN | 174,040 | 1.6% |
| LOAD_FAST_LOAD_FAST | 29,240 | 0.3% |
| BINARY_SUBSCR_LIST_INT | 5,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,310,040 | 97.6% |
| COMPARE_OP_INT | 174,040 | 1.6% |
| BINARY_SLICE | 24,280 | 0.2% |
| SWAP | 24,280 | 0.2% |
| LOAD_CONST | 17,880 | 0.2% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,560 | 74.6% |
| LOAD_FAST | 1,240 | 12.2% |
| BINARY_OP_SUBTRACT_INT | 1,240 | 12.2% |
| BINARY_OP | 100 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,880 | 87.6% |
| LOAD_FAST | 1,260 | 12.4% |


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
| STORE_FAST | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,407,880 | 99.8% |
| LOAD_FAST_LOAD_FAST | 7,600 | 0.2% |
| BINARY_OP | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 4,371,160 | 99.0% |
| STORE_FAST | 17,880 | 0.4% |
| LOAD_CONST | 11,460 | 0.3% |
| CALL_BUILTIN_CLASS | 7,560 | 0.2% |
| BINARY_OP | 3,840 | 0.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 107,480 | 81.5% |
| LOAD_FAST | 24,320 | 18.4% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 107,480 | 81.5% |
| RETURN_VALUE | 24,300 | 18.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 40 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,195,040 | 99.5% |
| LOAD_FAST | 49,880 | 0.5% |
| BINARY_SUBSCR | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,245,180 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,692,800 | 78.8% |
| LOAD_CONST | 10,303,560 | 10.3% |
| LOAD_DEREF | 5,232,520 | 5.2% |
| COPY | 4,395,360 | 4.4% |
| LOAD_FAST_LOAD_FAST | 1,300,280 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 39,313,880 | 39.3% |
| STORE_FAST | 22,851,780 | 22.9% |
| LOAD_CONST | 11,731,000 | 11.7% |
| RETURN_VALUE | 11,310,040 | 11.3% |
| LOAD_GLOBAL_MODULE | 5,642,040 | 5.6% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,480 | 99.8% |
| BINARY_SUBSCR | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,560 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 273,840 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 273,840 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 143,320 | 45.7% |
| LOAD_CONST | 143,320 | 45.7% |
| BUILD_LIST | 24,240 | 7.7% |
| LOAD_FAST | 2,480 | 0.8% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 313,480 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,776,320 | 63.6% |
| LOAD_CONST | 845,920 | 30.3% |
| STORE_FAST | 62,680 | 2.2% |
| CALL_BUILTIN_CLASS | 62,680 | 2.2% |
| LOAD_FAST | 24,000 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,645,300 | 94.7% |
| STORE_FAST | 79,340 | 2.8% |
| CALL_BUILTIN_CLASS | 62,680 | 2.2% |
| JUMP_FORWARD | 5,080 | 0.2% |
| CALL | 20 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 1,914,840 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,914,860 | 100.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 39,313,880 | 83.7% |
| LOAD_FAST | 5,763,680 | 12.3% |
| RETURN_VALUE | 1,864,920 | 4.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 46,768,540 | 99.6% |
| BINARY_OP_ADD_INT | 174,040 | 0.4% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 453,080 | 75.8% |
| LOAD_ATTR_INSTANCE_VALUE | 107,480 | 18.0% |
| BUILD_TUPLE | 37,080 | 6.2% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 560,600 | 93.8% |
| LOAD_FAST | 37,100 | 6.2% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,640 | 93.6% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 5.4% |
| CALL | 80 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 7,660 | 93.9% |
| YIELD_VALUE | 380 | 4.7% |
| STORE_FAST | 120 | 1.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,280 | 97.0% |
| CALL | 40 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,320 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_LAZY_DICT | 1,240 | 98.4% |
| CALL | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,260 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 558,040 | 100.0% |
| RETURN_GENERATOR | 40 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 558,060 | 100.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,473,680 | 85.8% |
| LOAD_FAST_LOAD_FAST | 3,714,200 | 7.7% |
| GET_ITER | 1,914,880 | 4.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 350,520 | 0.7% |
| LOAD_DEREF | 318,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 46,163,660 | 95.5% |
| COPY_FREE_VARS | 1,914,860 | 4.0% |
| MAKE_CELL | 273,880 | 0.6% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 203,440 | 98.8% |
| LOAD_FAST | 2,480 | 1.2% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 203,480 | 98.8% |
| MAKE_CELL | 2,520 | 1.2% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 15,280 | 99.7% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 15,320 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 51,442,760 | 72.1% |
| LOAD_FAST_LOAD_FAST | 9,932,600 | 13.9% |
| LOAD_GLOBAL_MODULE | 7,413,360 | 10.4% |
| LOAD_FAST | 2,111,920 | 3.0% |
| LOAD_ATTR_CLASS | 250,720 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 39,313,900 | 55.1% |
| POP_JUMP_IF_TRUE | 16,083,000 | 22.5% |
| POP_JUMP_IF_FALSE | 15,930,420 | 22.3% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,480 | 99.7% |
| COMPARE_OP | 100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,340 | 50.1% |
| POP_JUMP_IF_TRUE | 24,280 | 49.9% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 51,741,360 | 91.1% |
| GET_ITER | 2,500,900 | 4.4% |
| LOAD_FAST | 1,914,920 | 3.4% |
| EXTENDED_ARG | 547,580 | 1.0% |
| SWAP | 63,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 51,885,400 | 91.4% |
| RETURN_CONST | 1,916,240 | 3.4% |
| LOAD_GLOBAL_BUILTIN | 1,117,320 | 2.0% |
| LOAD_FAST_LOAD_FAST | 949,760 | 1.7% |
| LOAD_FAST | 527,360 | 0.9% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 38,482,960 | 93.4% |
| GET_ITER | 2,508,420 | 6.1% |
| SWAP | 144,600 | 0.4% |
| EXTENDED_ARG | 51,420 | 0.1% |
| FOR_ITER_LIST | 1,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 33,722,880 | 81.9% |
| STORE_FAST_LOAD_FAST | 2,723,820 | 6.6% |
| STORE_DEREF | 2,211,820 | 5.4% |
| JUMP_BACKWARD | 1,694,720 | 4.1% |
| LOAD_FAST | 669,440 | 1.6% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 250,760 | 100.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 250,720 | 99.9% |
| COMPARE_OP | 80 | 0.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,959,760 | 90.4% |
| LOAD_FAST_LOAD_FAST | 3,965,080 | 4.3% |
| STORE_FAST_LOAD_FAST | 2,723,800 | 2.9% |
| RETURN_VALUE | 2,088,720 | 2.2% |
| BINARY_SUBSCR_DICT | 107,480 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,257,300 | 85.4% |
| LOAD_DEREF | 4,126,680 | 4.4% |
| STORE_FAST | 2,718,420 | 2.9% |
| GET_ITER | 2,192,580 | 2.4% |
| CALL_BUILTIN_CLASS | 1,776,320 | 1.9% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 98.4% |
| LOAD_ATTR | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,240 | 98.4% |
| CALL | 20 | 1.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 558,040 | 47.9% |
| LOAD_FAST | 491,480 | 42.2% |
| LOAD_ATTR_INSTANCE_VALUE | 107,480 | 9.2% |
| STORE_FAST_LOAD_FAST | 8,000 | 0.7% |
| LOAD_ATTR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,155,760 | 99.2% |
| LOAD_CONST | 7,720 | 0.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,280 | 0.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 440 | 0.0% |
| CALL | 100 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,551,800 | 97.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,400,120 | 3.0% |
| LOAD_ATTR | 680 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,590,600 | 90.5% |
| LOAD_FAST_LOAD_FAST | 3,714,440 | 8.1% |
| CALL_PY_EXACT_ARGS | 350,520 | 0.8% |
| LOAD_DEREF | 296,940 | 0.6% |
| CALL | 100 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,400 | 93.3% |
| LOAD_ATTR | 100 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,500 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 39,382,880 | 76.2% |
| STORE_FAST | 7,788,160 | 15.1% |
| POP_JUMP_IF_FALSE | 2,009,320 | 3.9% |
| POP_JUMP_IF_TRUE | 1,121,240 | 2.2% |
| FOR_ITER_LIST | 1,117,320 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,790,680 | 94.4% |
| LOAD_FAST_LOAD_FAST | 1,962,040 | 3.8% |
| LOAD_CONST | 886,780 | 1.7% |
| LOAD_GLOBAL_BUILTIN | 62,680 | 0.1% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 5,642,040 | 60.1% |
| LOAD_FAST | 2,060,360 | 21.9% |
| STORE_FAST | 489,860 | 5.2% |
| POP_JUMP_IF_FALSE | 300,520 | 3.2% |
| RESUME_CHECK | 289,160 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 7,413,360 | 79.0% |
| LOAD_FAST_LOAD_FAST | 775,400 | 8.3% |
| LOAD_FAST | 344,200 | 3.7% |
| LOAD_ATTR_CLASS | 250,760 | 2.7% |
| CALL_PY_EXACT_ARGS | 159,920 | 1.7% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 46,163,660 | 48.8% |
| CACHE | 36,384,640 | 38.5% |
| BINARY_SUBSCR_GETITEM | 9,245,180 | 9.8% |
| POP_TOP | 1,914,920 | 2.0% |
| CALL_ALLOC_AND_ENTER_INIT | 313,480 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 39,382,880 | 41.7% |
| POP_TOP | 36,383,080 | 38.5% |
| LOAD_FAST | 13,936,420 | 14.7% |
| LOAD_FAST_LOAD_FAST | 3,938,440 | 4.2% |
| LOAD_CONST | 573,400 | 0.6% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 507,880 | 53.8% |
| LOAD_FAST | 436,200 | 46.2% |
| STORE_ATTR | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 433,840 | 45.9% |
| RETURN_CONST | 313,520 | 33.2% |
| LOAD_FAST_LOAD_FAST | 193,220 | 20.5% |
| LOAD_CONST | 2,520 | 0.3% |
| BUILD_MAP | 1,260 | 0.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,240 | 99.8% |
| STORE_SUBSCR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 24,280 | 100.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 4,395,360 | 94.8% |
| LOAD_FAST | 209,880 | 4.5% |
| LOAD_ATTR_INSTANCE_VALUE | 24,240 | 0.5% |
| LOAD_FAST_LOAD_FAST | 5,080 | 0.1% |
| STORE_SUBSCR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,102,680 | 66.9% |
| LOAD_FAST_LOAD_FAST | 1,273,580 | 27.5% |
| RETURN_CONST | 209,900 | 4.5% |
| LOAD_FAST | 48,560 | 1.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40,032,600 | 91.6% |
| RETURN_CONST | 3,380,360 | 7.7% |
| LOAD_FAST | 271,200 | 0.6% |
| TO_BOOL | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 39,834,520 | 91.2% |
| POP_JUMP_IF_TRUE | 3,850,120 | 8.8% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 142,040 | 85.4% |
| LOAD_ATTR_INSTANCE_VALUE | 24,280 | 14.6% |
| UNPACK_SEQUENCE | 60 | 0.0% |
| BINARY_SUBSCR_DICT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 166,420 | 100.0% |


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
|     deferred | 34,240 | 0.2% |
|          hit | 14,989,200 | 99.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 960 | 56.5% |
| Failure | 740 | 43.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 440 | 59.5% |
| remainder | 300 | 40.5% |


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
|     deferred | 1,060 | 0.0% |
|          hit | 109,624,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,060 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,020 | 0.0% |
|          hit | 101,703,700 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,140 | 88.4% |
| Failure | 280 | 11.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class no vectorcall | 120 | 42.9% |
| wrong number arguments | 100 | 35.7% |
| cfunc noargs | 60 | 21.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 780 | 0.0% |
|          hit | 71,375,940 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 133,420 | 0.1% |
|          hit | 97,824,260 | 99.9% |
|         miss | 135,160 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,300 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,380 | 0.0% |
|          hit | 140,217,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,120 | 0.0% |
|          hit | 61,089,080 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,120 | 100.0% |
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
|     deferred | 280 | 0.0% |
|          hit | 944,360 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 0.0% |
|          hit | 4,659,000 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 43,684,640 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 166,420 | 99.9% |

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
| Basic | 1,039,319,540 | 54.5% |
| Not specialized | 128,176,220 | 6.7% |
| Specialized hits | 740,782,460 | 38.8% |
| Specialized misses | 135,160 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| FOR_ITER | 133,420 | 74.1% |
| BINARY_OP | 34,240 | 19.0% |
| CALL | 5,020 | 2.8% |
| LOAD_ATTR | 2,380 | 1.3% |
| LOAD_GLOBAL | 2,120 | 1.2% |
| BINARY_SUBSCR | 1,060 | 0.6% |
| COMPARE_OP | 780 | 0.4% |
| TO_BOOL | 480 | 0.3% |
| STORE_ATTR | 280 | 0.2% |
| STORE_SUBSCR | 200 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| FOR_ITER_RANGE | 67,840 | 50.2% |
| FOR_ITER_LIST | 67,320 | 49.8% |
| CACHE | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| MAKE_FUNCTION | 0 | 0.0% |
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
| Calls to PyEval_EvalDefault | 38,299,740 | 39.7% |
| Calls to Python functions inlined | 58,119,540 | 60.3% |
| Calls via PyEval_EvalFrame (total) | 38,299,740 | 39.7% |
| Calls via PyEval_EvalFrame (vector) | 1,660 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 38,298,080 | 39.7% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 1,660 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 260 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 58,430,600 | 60.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 5,808,620 | 22.8% |
| Frees to freelist | 5,809,880 |  |
| Allocations | 19,719,660 | 77.2% |
| Allocations to 512 bytes | 19,718,380 | 77.2% |
| Allocations to 4 kbytes | 1,280 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 20,153,085 |  |
| New values | 1,400 |  |
| Interpreter increfs | 602,274,400 | 97.2% |
| Interpreter decrefs | 624,083,020 | 96.8% |
| Increfs | 17,613,968 | 2.8% |
| Decrefs | 20,474,018 | 3.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 72,448 |  |
| Method cache misses | 812 |  |
| Method cache collisions | 612 |  |
| Method cache dunder hits | 144,153 |  |
| Method cache dunder misses | 147 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,980 | 146,680 |
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
