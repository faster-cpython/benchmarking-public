
# Pystats results

- benchmark: raytrace
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 809,356,160 | 22.4% | 22.4% |  |
| LOAD_ATTR_INSTANCE_VALUE | 523,157,000 | 14.5% | 36.9% | 0.1% |
| RESUME_CHECK | 229,362,800 | 6.4% | 43.3% | 0.0% |
| LOAD_FAST_LOAD_FAST | 196,303,120 | 5.4% | 48.7% |  |
| RETURN_VALUE | 189,277,120 | 5.2% | 54.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 172,145,380 | 4.8% | 58.7% | 5.4% |
| CALL_PY_EXACT_ARGS | 159,434,400 | 4.4% | 63.2% | 2.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 156,935,740 | 4.3% | 67.5% | 2.5% |
| STORE_ATTR_INSTANCE_VALUE | 128,143,400 | 3.6% | 71.1% | 0.0% |
| STORE_FAST | 92,493,760 | 2.6% | 73.6% |  |
| BINARY_OP_ADD_FLOAT | 92,345,380 | 2.6% | 76.2% | 8.8% |
| RETURN_CONST | 84,603,600 | 2.3% | 78.5% |  |
| BINARY_OP | 72,879,720 | 2.0% | 80.6% |  |
| BINARY_OP_SUBTRACT_FLOAT | 67,918,880 | 1.9% | 82.4% | 29.7% |
| LOAD_CONST | 65,711,920 | 1.8% | 84.3% |  |
| LOAD_GLOBAL_MODULE | 59,268,400 | 1.6% | 85.9% | 0.0% |
| EXIT_INIT_CHECK | 44,517,200 | 1.2% | 87.1% |  |
| CALL_ALLOC_AND_ENTER_INIT | 44,517,200 | 1.2% | 88.4% |  |
| POP_JUMP_IF_FALSE | 43,041,040 | 1.2% | 89.6% |  |
| POP_TOP | 42,787,820 | 1.2% | 90.7% |  |
| FOR_ITER_LIST | 31,952,860 | 0.9% | 91.6% |  |
| JUMP_BACKWARD | 29,412,560 | 0.8% | 92.4% |  |
| INTERPRETER_EXIT | 25,483,520 | 0.7% | 93.2% |  |
| TO_BOOL_BOOL | 24,682,420 | 0.7% | 93.8% |  |
| BINARY_OP_MULTIPLY_INT | 18,928,260 | 0.5% | 94.4% | 60.7% |
| POP_JUMP_IF_NOT_NONE | 17,617,840 | 0.5% | 94.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 17,473,440 | 0.5% | 95.3% |  |
| STORE_FAST_STORE_FAST | 16,823,280 | 0.5% | 95.8% |  |
| COMPARE_OP | 16,460,520 | 0.5% | 96.3% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 16,396,600 | 0.5% | 96.7% |  |
| BUILD_TUPLE | 11,050,720 | 0.3% | 97.0% |  |
| CALL_BUILTIN_O | 10,271,320 | 0.3% | 97.3% |  |
| PUSH_NULL | 10,146,320 | 0.3% | 97.6% |  |
| LIST_APPEND | 9,769,600 | 0.3% | 97.9% |  |
| LOAD_GLOBAL_BUILTIN | 9,485,900 | 0.3% | 98.1% |  |
| LOAD_ATTR_MODULE | 9,346,000 | 0.3% | 98.4% |  |
| BINARY_OP_SUBTRACT_INT | 6,505,540 | 0.2% | 98.6% | 7.2% |
| CALL | 5,233,360 | 0.1% | 98.7% |  |
| BINARY_OP_ADD_INT | 5,040,340 | 0.1% | 98.8% | 0.0% |
| POP_JUMP_IF_TRUE | 4,291,440 | 0.1% | 99.0% |  |
| GET_ITER | 4,157,280 | 0.1% | 99.1% |  |
| UNARY_NEGATIVE | 3,533,840 | 0.1% | 99.2% |  |
| CALL_BUILTIN_CLASS | 3,333,780 | 0.1% | 99.3% |  |
| STORE_SUBSCR | 3,201,520 | 0.1% | 99.4% |  |
| COMPARE_OP_FLOAT | 2,619,220 | 0.1% | 99.4% |  |
| BUILD_LIST | 2,448,160 | 0.1% | 99.5% |  |
| LOAD_FAST_AND_CLEAR | 2,442,400 | 0.1% | 99.6% |  |
| SWAP | 2,442,400 | 0.1% | 99.6% |  |
| TO_BOOL | 2,040,960 | 0.1% | 99.7% |  |
| NOP | 2,015,840 | 0.1% | 99.7% |  |
| FOR_ITER_RANGE | 1,616,780 | 0.0% | 99.8% |  |
| COMPARE_OP_INT | 1,226,620 | 0.0% | 99.8% |  |
| LOAD_ATTR | 1,115,280 | 0.0% | 99.9% |  |
| LOAD_ATTR_METHOD_NO_DICT | 821,600 | 0.0% | 99.9% |  |
| CALL_LIST_APPEND | 819,620 | 0.0% | 99.9% |  |
| CALL_FUNCTION_EX | 800,240 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 800,080 | 0.0% | 99.9% |  |
| LIST_EXTEND | 800,080 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NONE | 451,120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 426,620 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 308,540 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 2,520 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,980 | 0.0% | 100.0% |  |
| STORE_ATTR | 1,060 | 0.0% | 100.0% |  |
| RESUME | 720 | 0.0% | 100.0% | 2.8% |
| CALL_KW | 560 | 0.0% | 100.0% |  |
| FOR_ITER | 400 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 320 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 240 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| BUILD_MAP | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| TO_BOOL_NONE | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 485,378,200 | 13.5% | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 232,436,680 | 6.4% | 19.9% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 159,361,580 | 4.4% | 24.3% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_FLOAT | 157,546,120 | 4.4% | 28.7% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 141,587,880 | 3.9% | 32.6% |
| RESUME_CHECK LOAD_FAST | 138,480,140 | 3.8% | 36.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 117,843,980 | 3.3% | 39.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 83,054,320 | 2.3% | 42.0% |
| STORE_FAST LOAD_FAST | 82,739,920 | 2.3% | 44.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 73,326,680 | 2.0% | 46.3% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 70,109,240 | 1.9% | 48.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 54,772,240 | 1.5% | 49.8% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST | 51,536,660 | 1.4% | 51.2% |
| BINARY_OP_ADD_FLOAT LOAD_FAST | 46,980,640 | 1.3% | 52.5% |
| RETURN_VALUE RETURN_VALUE | 45,571,120 | 1.3% | 53.8% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 45,312,780 | 1.3% | 55.0% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 44,634,960 | 1.2% | 56.3% |
| EXIT_INIT_CHECK RETURN_VALUE | 44,517,200 | 1.2% | 57.5% |
| RETURN_CONST EXIT_INIT_CHECK | 44,517,200 | 1.2% | 58.8% |
| CALL_ALLOC_AND_ENTER_INIT RESUME_CHECK | 44,517,200 | 1.2% | 60.0% |
| LOAD_FAST RETURN_VALUE | 43,718,240 | 1.2% | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP | 43,352,260 | 1.2% | 62.4% |
| RETURN_VALUE POP_TOP | 41,952,240 | 1.2% | 63.6% |
| POP_TOP LOAD_FAST | 40,790,080 | 1.1% | 64.7% |
| BINARY_OP_ADD_FLOAT RETURN_VALUE | 40,682,960 | 1.1% | 65.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 40,449,640 | 1.1% | 66.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 37,762,840 | 1.0% | 68.0% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_SUBTRACT_FLOAT | 36,709,640 | 1.0% | 69.0% |
| BINARY_OP_SUBTRACT_FLOAT LOAD_FAST | 36,284,440 | 1.0% | 70.0% |
| LOAD_FAST LOAD_CONST | 33,586,400 | 0.9% | 70.9% |
| JUMP_BACKWARD FOR_ITER_LIST | 27,803,900 | 0.8% | 71.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 26,704,240 | 0.7% | 72.5% |
| BINARY_OP CALL_ALLOC_AND_ENTER_INIT | 26,509,880 | 0.7% | 73.2% |
| CACHE RESUME_CHECK | 25,483,300 | 0.7% | 73.9% |
| RETURN_VALUE STORE_FAST | 25,351,180 | 0.7% | 74.6% |
| RETURN_VALUE INTERPRETER_EXIT | 24,682,480 | 0.7% | 75.3% |
| RETURN_CONST TO_BOOL_BOOL | 24,682,360 | 0.7% | 76.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 24,682,320 | 0.7% | 76.6% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_LOAD_FAST | 23,940,720 | 0.7% | 77.3% |
| RESUME_CHECK RETURN_CONST | 23,829,160 | 0.7% | 78.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 23,829,160 | 0.7% | 78.6% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 20,770,480 | 0.6% | 79.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 20,313,000 | 0.6% | 79.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 17,617,840 | 0.5% | 80.3% |
| LOAD_CONST BINARY_SUBSCR_TUPLE_INT | 17,473,280 | 0.5% | 80.7% |
| LOAD_CONST COMPARE_OP | 16,455,400 | 0.5% | 81.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS | 16,396,600 | 0.5% | 81.7% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 16,396,600 | 0.5% | 82.1% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 16,396,560 | 0.5% | 82.6% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_INT | 15,712,820 | 0.4% | 83.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 15,636,500 | 0.4% | 83.4% |
| BINARY_OP STORE_FAST | 14,736,120 | 0.4% | 83.8% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_SUBTRACT_FLOAT | 14,356,880 | 0.4% | 84.2% |
| RETURN_VALUE LOAD_FAST_LOAD_FAST | 14,356,560 | 0.4% | 84.6% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 14,356,520 | 0.4% | 85.0% |
| BINARY_OP_SUBTRACT_FLOAT STORE_FAST | 14,316,580 | 0.4% | 85.4% |
| BINARY_OP_SUBTRACT_FLOAT BINARY_OP_SUBTRACT_FLOAT | 14,316,500 | 0.4% | 85.8% |
| POP_JUMP_IF_FALSE RETURN_CONST | 13,807,280 | 0.4% | 86.2% |
| POP_JUMP_IF_NOT_NONE JUMP_BACKWARD | 13,801,840 | 0.4% | 86.6% |
| FOR_ITER_LIST STORE_FAST | 12,662,900 | 0.4% | 86.9% |
| LOAD_CONST LOAD_FAST | 12,368,080 | 0.3% | 87.3% |
| BINARY_OP LOAD_FAST | 12,160,200 | 0.3% | 87.6% |
| BINARY_OP_MULTIPLY_FLOAT CALL_ALLOC_AND_ENTER_INIT | 11,970,360 | 0.3% | 88.0% |
| BINARY_OP_MULTIPLY_INT BINARY_OP_ADD_FLOAT | 11,249,600 | 0.3% | 88.3% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 10,622,800 | 0.3% | 88.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 10,298,800 | 0.3% | 88.8% |
| RETURN_VALUE LOAD_FAST | 9,774,300 | 0.3% | 89.1% |
| LOAD_FAST BUILD_TUPLE | 9,769,680 | 0.3% | 89.4% |
| BUILD_TUPLE LIST_APPEND | 9,769,600 | 0.3% | 89.7% |
| LIST_APPEND JUMP_BACKWARD | 9,769,600 | 0.3% | 89.9% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 9,769,600 | 0.3% | 90.2% |
| BINARY_SUBSCR_TUPLE_INT STORE_FAST | 9,769,580 | 0.3% | 90.5% |
| RETURN_VALUE BINARY_OP | 9,644,240 | 0.3% | 90.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_CONST | 9,526,120 | 0.3% | 91.0% |
| PUSH_NULL LOAD_FAST | 9,346,000 | 0.3% | 91.3% |
| LOAD_ATTR_MODULE PUSH_NULL | 9,345,940 | 0.3% | 91.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 9,345,840 | 0.3% | 91.8% |
| BINARY_OP CALL_PY_EXACT_ARGS | 9,099,440 | 0.3% | 92.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 9,076,280 | 0.3% | 92.3% |
| CALL_BUILTIN_O RETURN_VALUE | 8,790,940 | 0.2% | 92.5% |
| RETURN_VALUE CALL_BUILTIN_O | 8,790,920 | 0.2% | 92.8% |
| LOAD_FAST BINARY_OP | 8,639,900 | 0.2% | 93.0% |
| RETURN_CONST LOAD_FAST | 8,275,840 | 0.2% | 93.2% |
| RETURN_VALUE CALL_PY_EXACT_ARGS | 7,480,360 | 0.2% | 93.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 6,627,680 | 0.2% | 93.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 6,627,040 | 0.2% | 93.8% |
| STORE_FAST_STORE_FAST LOAD_FAST | 6,627,040 | 0.2% | 94.0% |
| RETURN_CONST STORE_FAST | 6,326,000 | 0.2% | 94.2% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_ADD_FLOAT | 5,300,080 | 0.1% | 94.3% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 5,226,560 | 0.1% | 94.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 4,949,000 | 0.1% | 94.6% |
| LOAD_CONST LOAD_GLOBAL_BUILTIN | 4,799,760 | 0.1% | 94.7% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST | 4,396,240 | 0.1% | 94.9% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 4,066,100 | 0.1% | 95.0% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 3,864,240 | 0.1% | 95.1% |
| BINARY_SUBSCR_TUPLE_INT LOAD_FAST_LOAD_FAST | 3,839,700 | 0.1% | 95.2% |
| BINARY_SUBSCR_TUPLE_INT BINARY_OP | 3,785,880 | 0.1% | 95.3% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_SUBTRACT_INT | 3,675,500 | 0.1% | 95.4% |
| LOAD_CONST BINARY_OP_ADD_INT | 3,621,040 | 0.1% | 95.5% |
| BINARY_OP_SUBTRACT_INT CALL_ALLOC_AND_ENTER_INIT | 3,545,160 | 0.1% | 95.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 25,483,300 | 100.0% |
| RESUME | 220 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 160 | 50.0% |
| BINARY_OP | 60 | 18.8% |
| LOAD_FAST_LOAD_FAST | 60 | 18.8% |
| COMPARE_OP | 20 | 6.2% |
| STORE_FAST | 20 | 6.2% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 44,517,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 44,517,200 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,501,060 | 60.2% |
| LOAD_FAST | 1,221,280 | 29.4% |
| RETURN_VALUE | 426,640 | 10.3% |
| CALL_BUILTIN_CLASS | 8,160 | 0.2% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 2,927,680 | 70.4% |
| LOAD_FAST_AND_CLEAR | 1,221,200 | 29.4% |
| FOR_ITER_RANGE | 8,160 | 0.2% |
| FOR_ITER | 160 | 0.0% |
| EXTENDED_ARG | 80 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 24,682,480 | 96.9% |
| RETURN_CONST | 801,040 | 3.1% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,221,200 | 60.6% |
| POP_JUMP_IF_NOT_NONE | 794,560 | 39.4% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,015,760 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 41,952,240 | 98.0% |
| CALL_FUNCTION_EX | 800,000 | 1.9% |
| POP_JUMP_IF_TRUE | 34,400 | 0.1% |
| RETURN_CONST | 1,040 | 0.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,790,080 | 95.3% |
| LOAD_GLOBAL_MODULE | 853,360 | 2.0% |
| JUMP_BACKWARD | 800,500 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 308,560 | 0.7% |
| RETURN_CONST | 34,440 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 9,345,940 | 92.1% |
| LOAD_ATTR | 800,220 | 7.9% |
| LOAD_DEREF | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,346,000 | 92.1% |
| LOAD_FAST_LOAD_FAST | 800,000 | 7.9% |
| CALL | 240 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 45,571,120 | 24.1% |
| EXIT_INIT_CHECK | 44,517,200 | 23.5% |
| LOAD_FAST | 43,718,240 | 23.1% |
| BINARY_OP_ADD_FLOAT | 40,682,960 | 21.5% |
| CALL_BUILTIN_O | 8,790,940 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 45,571,120 | 24.1% |
| POP_TOP | 41,952,240 | 22.2% |
| STORE_FAST | 25,351,180 | 13.4% |
| INTERPRETER_EXIT | 24,682,480 | 13.0% |
| LOAD_FAST_LOAD_FAST | 14,356,560 | 7.6% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,399,940 | 75.0% |
| LOAD_FAST | 800,000 | 25.0% |
| STORE_SUBSCR | 1,520 | 0.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,599,920 | 50.0% |
| JUMP_BACKWARD | 800,000 | 25.0% |
| RETURN_CONST | 800,000 | 25.0% |
| STORE_SUBSCR | 1,520 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,040,120 | 100.0% |
| TO_BOOL | 680 | 0.0% |
| RETURN_CONST | 120 | 0.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,040,160 | 100.0% |
| TO_BOOL | 680 | 0.0% |
| TO_BOOL_BOOL | 60 | 0.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,040,080 | 57.7% |
| LOAD_GLOBAL_MODULE | 1,493,740 | 42.3% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 2,040,080 | 57.7% |
| COMPARE_OP_FLOAT | 1,493,720 | 42.3% |
| COMPARE_OP | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 43,352,260 | 59.5% |
| RETURN_VALUE | 9,644,240 | 13.2% |
| LOAD_FAST | 8,639,900 | 11.9% |
| BINARY_SUBSCR_TUPLE_INT | 3,785,880 | 5.2% |
| LOAD_FAST_LOAD_FAST | 2,449,520 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ALLOC_AND_ENTER_INIT | 26,509,880 | 36.4% |
| STORE_FAST | 14,736,120 | 20.2% |
| LOAD_FAST | 12,160,200 | 16.7% |
| CALL_PY_EXACT_ARGS | 9,099,440 | 12.5% |
| BINARY_OP_ADD_FLOAT | 4,066,100 | 5.6% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,221,200 | 49.9% |
| LOAD_FAST_LOAD_FAST | 800,000 | 32.7% |
| RESUME_CHECK | 426,680 | 17.4% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,221,200 | 49.9% |
| LOAD_FAST | 800,160 | 32.7% |
| STORE_FAST | 426,640 | 17.4% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,769,680 | 88.4% |
| BINARY_OP_ADD_FLOAT | 1,271,860 | 11.5% |
| BINARY_OP | 8,060 | 0.1% |
| LOAD_FAST_LOAD_FAST | 640 | 0.0% |
| LOAD_CONST | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 9,769,600 | 88.4% |
| RETURN_VALUE | 1,279,920 | 11.6% |
| CALL_LIST_APPEND | 600 | 0.0% |
| LOAD_CONST | 480 | 0.0% |
| BUILD_MAP | 80 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,402,860 | 45.9% |
| CALL_BUILTIN_CLASS | 2,399,940 | 45.9% |
| LOAD_FAST | 427,520 | 8.2% |
| BINARY_OP | 620 | 0.0% |
| LOAD_CONST | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,402,860 | 45.9% |
| LOAD_FAST | 2,400,280 | 45.9% |
| STORE_FAST | 426,860 | 8.2% |
| CALL_PY_EXACT_ARGS | 960 | 0.0% |
| RESUME_CHECK | 520 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 800,080 | 100.0% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 800,000 | 100.0% |
| RESUME_CHECK | 140 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 800,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 800,080 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 480 | 85.7% |
| CALL | 80 | 14.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,455,400 | 100.0% |
| COMPARE_OP | 5,000 | 0.0% |
| UNARY_NEGATIVE | 40 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 15,636,500 | 95.0% |
| POP_JUMP_IF_TRUE | 818,940 | 5.0% |
| COMPARE_OP | 5,000 | 0.0% |
| COMPARE_OP_FLOAT | 60 | 0.0% |
| COMPARE_OP_INT | 20 | 0.0% |


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

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 33.3% |
| POP_TOP | 80 | 33.3% |
| JUMP_BACKWARD | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 120 | 50.0% |
| JUMP_BACKWARD | 80 | 33.3% |
| FOR_ITER | 40 | 16.7% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 180 | 45.0% |
| GET_ITER | 160 | 40.0% |
| EXTENDED_ARG | 40 | 10.0% |
| SWAP | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 40.0% |
| FOR_ITER_LIST | 100 | 25.0% |
| FOR_ITER_RANGE | 100 | 25.0% |
| UNPACK_SEQUENCE | 40 | 10.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 13,801,840 | 46.9% |
| LIST_APPEND | 9,769,600 | 33.2% |
| POP_JUMP_IF_TRUE | 2,257,600 | 7.7% |
| STORE_FAST | 1,156,080 | 3.9% |
| CALL_LIST_APPEND | 818,860 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 27,803,900 | 94.5% |
| FOR_ITER_RANGE | 1,608,400 | 5.5% |
| FOR_ITER | 180 | 0.0% |
| EXTENDED_ARG | 80 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 9,769,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 9,769,600 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 800,000 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 800,080 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 804,560 | 72.1% |
| LOAD_GLOBAL_MODULE | 308,940 | 27.7% |
| LOAD_ATTR | 840 | 0.1% |
| LOAD_FAST_LOAD_FAST | 360 | 0.0% |
| LOAD_GLOBAL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 800,220 | 71.8% |
| BINARY_OP | 309,020 | 27.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,680 | 0.2% |
| LOAD_FAST | 1,060 | 0.1% |
| LOAD_ATTR | 840 | 0.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,586,400 | 51.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 9,526,120 | 14.5% |
| LOAD_GLOBAL_BUILTIN | 5,226,560 | 8.0% |
| LOAD_ATTR_INSTANCE_VALUE | 4,949,000 | 7.5% |
| LOAD_FAST_LOAD_FAST | 3,864,240 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 17,473,280 | 26.6% |
| COMPARE_OP | 16,455,400 | 25.0% |
| LOAD_FAST | 12,368,080 | 18.8% |
| LOAD_GLOBAL_BUILTIN | 4,799,760 | 7.3% |
| BINARY_OP_ADD_INT | 3,621,040 | 5.5% |


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
| LOAD_ATTR_INSTANCE_VALUE | 232,436,680 | 28.7% |
| RESUME_CHECK | 138,480,140 | 17.1% |
| STORE_FAST | 82,739,920 | 10.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 54,772,240 | 6.8% |
| BINARY_OP_MULTIPLY_FLOAT | 51,536,660 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 485,378,200 | 60.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 141,587,880 | 17.5% |
| RETURN_VALUE | 43,718,240 | 5.4% |
| CALL_PY_EXACT_ARGS | 40,449,640 | 5.0% |
| LOAD_CONST | 33,586,400 | 4.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,221,200 | 50.0% |
| LOAD_FAST_AND_CLEAR | 1,221,200 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 1,221,200 | 50.0% |
| SWAP | 1,221,200 | 50.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 73,326,680 | 37.4% |
| RESUME_CHECK | 44,634,960 | 22.7% |
| BINARY_OP_MULTIPLY_FLOAT | 23,940,720 | 12.2% |
| LOAD_GLOBAL_MODULE | 20,313,000 | 10.3% |
| RETURN_VALUE | 14,356,560 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 117,843,980 | 60.0% |
| LOAD_ATTR_INSTANCE_VALUE | 37,762,840 | 19.2% |
| BINARY_OP_MULTIPLY_FLOAT | 14,356,520 | 7.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,622,800 | 5.4% |
| LOAD_FAST | 6,627,040 | 3.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 19.0% |
| LOAD_CONST | 240 | 9.5% |
| POP_TOP | 160 | 6.3% |
| LOAD_ATTR | 160 | 6.3% |
| LOAD_FAST | 160 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 840 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 420 | 16.7% |
| LOAD_FAST | 340 | 13.5% |
| LOAD_CONST | 320 | 12.7% |
| LOAD_ATTR | 260 | 10.3% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 23,829,160 | 55.4% |
| COMPARE_OP | 15,636,500 | 36.3% |
| TO_BOOL | 2,040,160 | 4.7% |
| COMPARE_OP_INT | 1,226,620 | 2.8% |
| TO_BOOL_INT | 308,540 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 24,682,320 | 57.3% |
| RETURN_CONST | 13,807,280 | 32.1% |
| LOAD_CONST | 2,466,720 | 5.7% |
| NOP | 1,221,200 | 2.8% |
| LOAD_FAST | 863,360 | 2.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 451,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 426,640 | 94.6% |
| LOAD_FAST_LOAD_FAST | 24,480 | 5.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,617,840 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 13,801,840 | 78.3% |
| LOAD_FAST | 3,021,440 | 17.1% |
| NOP | 794,560 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 2,619,220 | 61.0% |
| TO_BOOL_BOOL | 853,260 | 19.9% |
| COMPARE_OP | 818,940 | 19.1% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,257,600 | 52.6% |
| LOAD_FAST | 1,274,160 | 29.7% |
| LOAD_FAST_LOAD_FAST | 725,280 | 16.9% |
| POP_TOP | 34,400 | 0.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 45,312,780 | 53.6% |
| RESUME_CHECK | 23,829,160 | 28.2% |
| POP_JUMP_IF_FALSE | 13,807,280 | 16.3% |
| FOR_ITER_LIST | 818,880 | 1.0% |
| STORE_SUBSCR | 800,000 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXIT_INIT_CHECK | 44,517,200 | 52.6% |
| TO_BOOL_BOOL | 24,682,360 | 29.2% |
| LOAD_FAST | 8,275,840 | 9.8% |
| STORE_FAST | 6,326,000 | 7.5% |
| INTERPRETER_EXIT | 801,040 | 0.9% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 720 | 67.9% |
| LOAD_FAST_LOAD_FAST | 340 | 32.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 560 | 52.8% |
| RETURN_CONST | 180 | 17.0% |
| LOAD_FAST | 120 | 11.3% |
| LOAD_CONST | 60 | 5.7% |
| LOAD_GLOBAL | 60 | 5.7% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 25,351,180 | 27.4% |
| BINARY_OP | 14,736,120 | 15.9% |
| BINARY_OP_SUBTRACT_FLOAT | 14,316,580 | 15.5% |
| FOR_ITER_LIST | 12,662,900 | 13.7% |
| BINARY_SUBSCR_TUPLE_INT | 9,769,580 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 82,739,920 | 89.5% |
| LOAD_GLOBAL_MODULE | 2,874,520 | 3.1% |
| STORE_FAST | 2,442,400 | 2.6% |
| LOAD_FAST_LOAD_FAST | 1,245,680 | 1.3% |
| LOAD_CONST | 1,226,720 | 1.3% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 16,396,600 | 97.5% |
| UNPACK_SEQUENCE_TUPLE | 426,620 | 2.5% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,769,600 | 58.1% |
| LOAD_FAST | 6,627,040 | 39.4% |
| STORE_FAST | 426,640 | 2.5% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 1,221,200 | 50.0% |
| LOAD_FAST_AND_CLEAR | 1,221,200 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 1,221,200 | 50.0% |
| FOR_ITER_LIST | 1,221,180 | 50.0% |
| FOR_ITER | 20 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |
| FOR_ITER_LIST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 40 | 33.3% |
| UNPACK_SEQUENCE_TUPLE | 20 | 16.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 400 | 55.6% |
| CACHE | 220 | 30.6% |
| CALL_PY_EXACT_ARGS | 60 | 8.3% |
| CALL_FUNCTION_EX | 20 | 2.8% |
| COPY_FREE_VARS | 20 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 420 | 58.3% |
| LOAD_GLOBAL | 100 | 13.9% |
| LOAD_FAST_LOAD_FAST | 80 | 11.1% |
| BUILD_LIST | 40 | 5.6% |
| RETURN_CONST | 40 | 5.6% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 70,109,240 | 75.9% |
| BINARY_OP_MULTIPLY_INT | 11,249,600 | 12.2% |
| LOAD_ATTR_INSTANCE_VALUE | 5,300,080 | 5.7% |
| BINARY_OP | 4,066,100 | 4.4% |
| LOAD_CONST | 925,560 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,980,640 | 50.9% |
| RETURN_VALUE | 40,682,960 | 44.1% |
| CALL_ALLOC_AND_ENTER_INIT | 1,636,760 | 1.8% |
| BUILD_TUPLE | 1,271,860 | 1.4% |
| CALL_BUILTIN_CLASS | 925,560 | 1.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,621,040 | 71.8% |
| LOAD_FAST | 799,960 | 15.9% |
| CALL_BUILTIN_CLASS | 617,040 | 12.2% |
| BINARY_OP_MULTIPLY_INT | 2,140 | 0.0% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR | 2,399,940 | 47.6% |
| LOAD_FAST | 1,222,240 | 24.2% |
| LOAD_CONST | 1,108,520 | 22.0% |
| LOAD_GLOBAL_BUILTIN | 308,520 | 6.1% |
| RETURN_VALUE | 1,060 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 157,546,120 | 91.5% |
| LOAD_FAST_LOAD_FAST | 14,356,520 | 8.3% |
| BINARY_OP_MULTIPLY_INT | 149,580 | 0.1% |
| BINARY_SUBSCR_TUPLE_INT | 53,820 | 0.0% |
| BINARY_OP | 25,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 70,109,240 | 40.7% |
| LOAD_FAST | 51,536,660 | 29.9% |
| LOAD_FAST_LOAD_FAST | 23,940,720 | 13.9% |
| BINARY_OP_SUBTRACT_FLOAT | 14,356,880 | 8.3% |
| CALL_ALLOC_AND_ENTER_INIT | 11,970,360 | 7.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 15,712,820 | 83.0% |
| LOAD_CONST | 2,998,620 | 15.8% |
| BINARY_OP | 182,820 | 1.0% |
| BINARY_OP_MULTIPLY_FLOAT | 33,920 | 0.2% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 11,249,600 | 59.4% |
| LOAD_FAST | 4,396,240 | 23.2% |
| CALL_BUILTIN_CLASS | 1,398,760 | 7.4% |
| LOAD_CONST | 800,040 | 4.2% |
| STORE_FAST | 799,980 | 4.2% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 36,709,640 | 54.0% |
| BINARY_OP_MULTIPLY_FLOAT | 14,356,880 | 21.1% |
| BINARY_OP_SUBTRACT_FLOAT | 14,316,500 | 21.1% |
| LOAD_FAST | 1,599,960 | 2.4% |
| CALL_BUILTIN_O | 554,680 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,284,440 | 53.4% |
| STORE_FAST | 14,316,580 | 21.1% |
| BINARY_OP_SUBTRACT_FLOAT | 14,316,500 | 21.1% |
| CALL_PY_EXACT_ARGS | 1,599,920 | 2.4% |
| RETURN_VALUE | 554,700 | 0.8% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,675,500 | 56.5% |
| LOAD_CONST | 2,021,160 | 31.1% |
| LOAD_FAST | 799,960 | 12.3% |
| BINARY_OP | 8,200 | 0.1% |
| BINARY_OP_SUBTRACT_FLOAT | 720 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ALLOC_AND_ENTER_INIT | 3,545,160 | 54.5% |
| LOAD_FAST | 2,151,420 | 33.1% |
| LOAD_CONST | 799,980 | 12.3% |
| BINARY_OP | 8,260 | 0.1% |
| BINARY_OP_SUBTRACT_FLOAT | 700 | 0.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,473,280 | 100.0% |
| BINARY_SUBSCR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,769,580 | 55.9% |
| LOAD_FAST_LOAD_FAST | 3,839,700 | 22.0% |
| BINARY_OP | 3,785,880 | 21.7% |
| BINARY_OP_MULTIPLY_FLOAT | 53,820 | 0.3% |
| COMPARE_OP_FLOAT | 24,440 | 0.1% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 26,509,880 | 59.5% |
| BINARY_OP_MULTIPLY_FLOAT | 11,970,360 | 26.9% |
| BINARY_OP_SUBTRACT_INT | 3,545,160 | 8.0% |
| BINARY_OP_ADD_FLOAT | 1,636,760 | 3.7% |
| RETURN_VALUE | 426,600 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 44,517,200 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 1,398,760 | 42.0% |
| BINARY_OP | 1,001,160 | 30.0% |
| BINARY_OP_ADD_FLOAT | 925,560 | 27.8% |
| LOAD_ATTR_INSTANCE_VALUE | 8,000 | 0.2% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,399,940 | 72.0% |
| BINARY_OP_ADD_INT | 617,040 | 18.5% |
| LOAD_GLOBAL_BUILTIN | 308,520 | 9.3% |
| GET_ITER | 8,160 | 0.2% |
| STORE_FAST | 60 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,790,920 | 85.6% |
| LOAD_ATTR_INSTANCE_VALUE | 925,560 | 9.0% |
| LOAD_FAST | 554,720 | 5.4% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,790,940 | 85.6% |
| LOAD_CONST | 925,620 | 9.0% |
| BINARY_OP_SUBTRACT_FLOAT | 554,680 | 5.4% |
| STORE_FAST | 60 | 0.0% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 818,960 | 99.9% |
| BUILD_TUPLE | 600 | 0.1% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 818,860 | 99.9% |
| RETURN_CONST | 760 | 0.1% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,880 | 94.9% |
| CALL | 100 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,980 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 83,054,320 | 52.1% |
| LOAD_FAST | 40,449,640 | 25.4% |
| LOAD_ATTR_INSTANCE_VALUE | 16,396,600 | 10.3% |
| BINARY_OP | 9,099,440 | 5.7% |
| RETURN_VALUE | 7,480,360 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 159,361,580 | 100.0% |
| CALL_PY_EXACT_ARGS | 72,760 | 0.0% |
| RESUME | 60 | 0.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 1,493,720 | 57.0% |
| LOAD_GLOBAL_MODULE | 1,101,000 | 42.0% |
| BINARY_SUBSCR_TUPLE_INT | 24,440 | 0.9% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,619,220 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,226,600 | 100.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,226,620 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 27,803,900 | 87.0% |
| GET_ITER | 2,927,680 | 9.2% |
| SWAP | 1,221,180 | 3.8% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 16,396,560 | 51.3% |
| STORE_FAST | 12,662,900 | 39.6% |
| LOAD_FAST | 1,647,840 | 5.2% |
| RETURN_CONST | 818,880 | 2.6% |
| LOAD_GLOBAL_BUILTIN | 426,600 | 1.3% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,608,400 | 99.5% |
| GET_ITER | 8,160 | 0.5% |
| EXTENDED_ARG | 120 | 0.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,608,460 | 99.5% |
| JUMP_BACKWARD | 8,000 | 0.5% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| RETURN_CONST | 80 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 485,378,200 | 92.8% |
| LOAD_FAST_LOAD_FAST | 37,762,840 | 7.2% |
| LOAD_ATTR_INSTANCE_VALUE | 14,280 | 0.0% |
| LOAD_ATTR | 1,680 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 232,436,680 | 44.4% |
| BINARY_OP_MULTIPLY_FLOAT | 157,546,120 | 30.1% |
| BINARY_OP | 43,352,260 | 8.3% |
| BINARY_OP_SUBTRACT_FLOAT | 36,709,640 | 7.0% |
| CALL_PY_EXACT_ARGS | 16,396,600 | 3.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 820,720 | 99.9% |
| LOAD_ATTR_INSTANCE_VALUE | 720 | 0.1% |
| LOAD_ATTR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 819,000 | 99.7% |
| LOAD_CONST | 1,980 | 0.2% |
| LOAD_FAST_LOAD_FAST | 620 | 0.1% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 141,587,880 | 90.2% |
| LOAD_FAST_LOAD_FAST | 10,622,800 | 6.8% |
| LOAD_ATTR_INSTANCE_VALUE | 2,893,280 | 1.8% |
| BINARY_OP | 936,880 | 0.6% |
| RETURN_VALUE | 818,920 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 83,054,320 | 52.9% |
| LOAD_FAST | 54,772,240 | 34.9% |
| LOAD_CONST | 9,526,120 | 6.1% |
| LOAD_GLOBAL_MODULE | 6,627,680 | 4.2% |
| LOAD_FAST_LOAD_FAST | 2,879,840 | 1.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,345,840 | 100.0% |
| LOAD_ATTR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 9,345,940 | 100.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,799,760 | 50.6% |
| STORE_SUBSCR | 1,599,920 | 16.9% |
| LOAD_GLOBAL_BUILTIN | 925,560 | 9.8% |
| STORE_FAST | 807,960 | 8.5% |
| FOR_ITER_LIST | 426,600 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,226,560 | 55.1% |
| LOAD_FAST | 3,333,660 | 35.1% |
| LOAD_GLOBAL_BUILTIN | 925,560 | 9.8% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,682,320 | 41.6% |
| RESUME_CHECK | 20,770,480 | 35.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,627,680 | 11.2% |
| LOAD_FAST | 3,457,920 | 5.8% |
| STORE_FAST | 2,874,520 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,704,240 | 45.1% |
| LOAD_FAST_LOAD_FAST | 20,313,000 | 34.3% |
| LOAD_ATTR_MODULE | 9,345,840 | 15.8% |
| UNARY_NEGATIVE | 1,493,740 | 2.5% |
| COMPARE_OP_FLOAT | 1,101,000 | 1.9% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 159,361,580 | 69.5% |
| CALL_ALLOC_AND_ENTER_INIT | 44,517,200 | 19.4% |
| CACHE | 25,483,300 | 11.1% |
| CALL | 520 | 0.0% |
| CALL_FUNCTION_EX | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,480,140 | 60.4% |
| LOAD_FAST_LOAD_FAST | 44,634,960 | 19.5% |
| RETURN_CONST | 23,829,160 | 10.4% |
| LOAD_GLOBAL_MODULE | 20,770,480 | 9.1% |
| LOAD_CONST | 1,221,180 | 0.5% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 117,843,980 | 92.0% |
| LOAD_FAST | 10,298,800 | 8.0% |
| STORE_ATTR | 560 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 73,326,680 | 57.2% |
| RETURN_CONST | 45,312,780 | 35.4% |
| LOAD_FAST | 9,076,280 | 7.1% |
| RETURN_VALUE | 426,620 | 0.3% |
| LOAD_CONST | 740 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 24,682,360 | 100.0% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 23,829,160 | 96.5% |
| POP_JUMP_IF_TRUE | 853,260 | 3.5% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 308,520 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 308,540 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| TO_BOOL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 426,600 | 100.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 426,620 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 16,396,560 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 16,396,600 | 100.0% |


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
|     deferred | 70,784,940 | 16.2% |
|          hit | 313,387,080 | 71.9% |
|         miss | 49,496,700 | 11.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 934,840 | 44.6% |
| Failure | 1,159,940 | 55.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 771,820 | 66.5% |
| multiply different types | 219,060 | 18.9% |
| add different types | 157,880 | 13.6% |
| subtract other | 6,680 | 0.6% |
| true divide float | 2,360 | 0.2% |
| true divide different types | 1,120 | 0.1% |
| add other | 760 | 0.1% |
| remainder | 260 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 160 | 0.0% |
|          hit | 17,473,440 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,156,100 | 2.3% |
|          hit | 214,521,120 | 95.9% |
|         miss | 3,857,180 | 1.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 74,580 | 96.5% |
| Failure | 2,680 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc varargs keywords | 2,580 | 96.3% |
| cfunc noargs | 60 | 2.2% |
| class no vectorcall | 20 | 0.7% |
| init not simple | 20 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,455,440 | 81.0% |
|          hit | 3,845,840 | 18.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 1.6% |
| Failure | 5,000 | 98.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 5,000 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 0.0% |
|          hit | 33,569,640 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,022,300 | 0.1% |
|          hit | 685,520,020 | 99.2% |
|         miss | 4,740,320 | 0.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 92,260 | 99.2% |
| Failure | 720 | 0.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 380 | 52.8% |
| mutable class | 320 | 44.4% |
| metaclass attribute | 20 | 2.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,220 | 0.0% |
|          hit | 68,752,180 | 100.0% |
|         miss | 2,120 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,300 | 100.0% |
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
|     deferred | 440 | 0.0% |
|          hit | 128,140,500 | 100.0% |
|         miss | 2,900 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,200,000 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 0 | 0.0% |
| Failure | 1,520 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 1,520 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,040,180 | 7.5% |
|          hit | 24,991,020 | 92.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 12.8% |
| Failure | 680 | 87.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float | 680 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 16,823,220 | 100.0% |

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
| Basic | 1,647,179,020 | 45.7% |
| Not specialized | 166,337,220 | 4.6% |
| Specialized hits | 1,736,386,840 | 48.1% |
| Specialized misses | 58,099,240 | 1.6% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 70,784,940 | 71.7% |
| COMPARE_OP | 16,455,440 | 16.7% |
| CALL | 5,156,100 | 5.2% |
| STORE_SUBSCR | 3,200,000 | 3.2% |
| TO_BOOL | 2,040,180 | 2.1% |
| LOAD_ATTR | 1,022,300 | 1.0% |
| LOAD_GLOBAL | 1,220 | 0.0% |
| STORE_ATTR | 440 | 0.0% |
| FOR_ITER | 200 | 0.0% |
| BINARY_SUBSCR | 160 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 20,189,880 | 34.8% |
| BINARY_OP_MULTIPLY_INT | 11,484,580 | 19.8% |
| BINARY_OP_MULTIPLY_FLOAT | 9,253,780 | 15.9% |
| BINARY_OP_ADD_FLOAT | 8,097,820 | 13.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,983,320 | 6.9% |
| CALL_PY_EXACT_ARGS | 3,857,180 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 757,000 | 1.3% |
| BINARY_OP_SUBTRACT_INT | 468,520 | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 2,900 | 0.0% |
| BINARY_OP_ADD_INT | 2,120 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 25,483,520 | 11.1% |
| Calls to Python functions inlined | 203,880,000 | 88.9% |
| Calls via PyEval_EvalFrame (total) | 25,483,520 | 11.1% |
| Calls via PyEval_EvalFrame (vector) | 25,483,520 | 11.1% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 25,483,520 | 11.1% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 24,682,480 | 10.8% |
| Calls via PyEval_EvalFrame (function ex) | 240 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 244,611,620 | 106.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 307,926,220 | 73.1% |
| Frees to freelist | 307,929,520 |  |
| Allocations | 113,548,060 | 26.9% |
| Allocations to 512 bytes | 113,547,900 | 26.9% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 115,189,264 |  |
| New values | 1,040 |  |
| Interpreter increfs | 2,340,547,040 | 96.2% |
| Interpreter decrefs | 2,554,252,960 | 90.9% |
| Increfs | 92,902,489 | 3.8% |
| Decrefs | 254,556,885 | 9.1% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 6,167,252 |  |
| Method cache misses | 1,168 |  |
| Method cache collisions | 910 |  |
| Method cache dunder hits | 24,683,877 |  |
| Method cache dunder misses | 243 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 2,100 | 140,840 |
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
