
# Pystats results

- benchmark: deltablue
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 327,753,300 | 19.5% | 19.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 245,955,440 | 14.6% | 34.1% | 1.7% |
| RESUME_CHECK | 122,789,880 | 7.3% | 41.4% | 0.0% |
| CALL_PY_EXACT_ARGS | 116,074,920 | 6.9% | 48.3% | 2.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 114,293,640 | 6.8% | 55.1% | 5.7% |
| LOAD_GLOBAL_MODULE | 87,268,040 | 5.2% | 60.3% |  |
| POP_JUMP_IF_FALSE | 85,934,160 | 5.1% | 65.4% |  |
| COMPARE_OP_INT | 80,851,820 | 4.8% | 70.2% |  |
| RETURN_VALUE | 76,423,820 | 4.5% | 74.7% |  |
| LOAD_ATTR_CLASS | 73,806,320 | 4.4% | 79.1% |  |
| STORE_ATTR_INSTANCE_VALUE | 51,788,160 | 3.1% | 82.2% | 3.6% |
| POP_TOP | 50,054,360 | 3.0% | 85.2% |  |
| RETURN_CONST | 49,048,300 | 2.9% | 88.1% |  |
| ENTER_EXECUTOR | 39,826,820 | 2.4% | 90.4% |  |
| STORE_FAST | 23,169,420 | 1.4% | 91.8% |  |
| LOAD_FAST_LOAD_FAST | 15,883,520 | 0.9% | 92.8% |  |
| TO_BOOL_BOOL | 14,168,280 | 0.8% | 93.6% |  |
| LOAD_ATTR | 13,705,420 | 0.8% | 94.4% |  |
| POP_JUMP_IF_TRUE | 8,898,260 | 0.5% | 94.9% |  |
| LOAD_GLOBAL_BUILTIN | 7,871,600 | 0.5% | 95.4% |  |
| FOR_ITER_LIST | 7,728,520 | 0.5% | 95.9% |  |
| BINARY_OP_ADD_INT | 6,163,580 | 0.4% | 96.2% |  |
| CALL_LIST_APPEND | 5,997,860 | 0.4% | 96.6% |  |
| LOAD_CONST | 5,935,120 | 0.4% | 96.9% |  |
| BINARY_OP_MULTIPLY_INT | 5,364,900 | 0.3% | 97.3% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,197,580 | 0.3% | 97.6% |  |
| CALL_LEN | 4,446,600 | 0.3% | 97.8% |  |
| TO_BOOL_INT | 4,446,600 | 0.3% | 98.1% |  |
| CALL | 3,981,820 | 0.2% | 98.3% |  |
| GET_ITER | 3,713,660 | 0.2% | 98.6% |  |
| COPY | 3,655,360 | 0.2% | 98.8% |  |
| COPY_FREE_VARS | 3,402,320 | 0.2% | 99.0% |  |
| LOAD_SUPER_ATTR_METHOD | 3,402,020 | 0.2% | 99.2% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 3,185,780 | 0.2% | 99.4% | 100.0% |
| COMPARE_OP | 3,168,660 | 0.2% | 99.6% |  |
| POP_JUMP_IF_NONE | 2,617,600 | 0.2% | 99.7% |  |
| EXIT_INIT_CHECK | 1,318,140 | 0.1% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 1,318,140 | 0.1% | 99.9% |  |
| SWAP | 796,160 | 0.0% | 99.9% |  |
| BINARY_OP | 349,360 | 0.0% | 99.9% |  |
| UNARY_NOT | 271,360 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 262,400 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 261,380 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 89,540 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 61,320 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 51,200 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 22,980 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 18,020 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 10,400 | 0.0% | 100.0% | 100.0% |
| BUILD_CONST_KEY_MAP | 10,240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 10,220 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 6,040 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 5,120 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,080 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 2,560 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 2,560 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 2,540 | 0.0% | 100.0% |  |
| STORE_ATTR | 2,200 | 0.0% | 100.0% |  |
| TO_BOOL | 1,280 | 0.0% | 100.0% |  |
| RESUME | 1,200 | 0.0% | 100.0% | 296.7% |
| PUSH_NULL | 720 | 0.0% | 100.0% |  |
| FOR_ITER | 520 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 440 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 193,428,860 | 11.5% | 11.5% |
| RESUME_CHECK LOAD_FAST | 116,150,700 | 6.9% | 18.4% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 114,186,820 | 6.8% | 25.2% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 103,665,160 | 6.2% | 31.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 78,112,680 | 4.6% | 36.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 76,527,680 | 4.5% | 40.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_CLASS | 73,806,080 | 4.4% | 44.9% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 73,070,520 | 4.3% | 49.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 71,229,720 | 4.2% | 53.5% |
| LOAD_ATTR_CLASS COMPARE_OP_INT | 71,224,640 | 4.2% | 57.7% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 64,684,180 | 3.8% | 61.6% |
| RETURN_CONST POP_TOP | 45,868,780 | 2.7% | 64.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 45,691,580 | 2.7% | 67.0% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 36,100,580 | 2.1% | 69.2% |
| POP_TOP ENTER_EXECUTOR | 31,196,300 | 1.9% | 71.0% |
| ENTER_EXECUTOR LOAD_ATTR_METHOD_WITH_VALUES | 30,825,760 | 1.8% | 72.8% |
| RETURN_VALUE LOAD_ATTR_INSTANCE_VALUE | 28,510,600 | 1.7% | 74.5% |
| RETURN_VALUE STORE_ATTR_INSTANCE_VALUE | 27,472,520 | 1.6% | 76.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_INSTANCE_VALUE | 22,682,240 | 1.3% | 77.5% |
| STORE_FAST LOAD_FAST | 17,820,220 | 1.1% | 78.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 10,759,920 | 0.6% | 79.2% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 10,477,820 | 0.6% | 79.8% |
| LOAD_ATTR LOAD_FAST | 9,986,100 | 0.6% | 80.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 9,457,520 | 0.6% | 81.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,388,140 | 0.5% | 81.5% |
| RETURN_VALUE TO_BOOL_BOOL | 7,864,740 | 0.5% | 82.0% |
| RETURN_VALUE STORE_FAST | 7,614,260 | 0.5% | 82.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 7,335,340 | 0.4% | 82.8% |
| POP_TOP LOAD_FAST | 7,319,840 | 0.4% | 83.3% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 6,769,840 | 0.4% | 83.7% |
| COMPARE_OP_INT RETURN_VALUE | 6,746,500 | 0.4% | 84.1% |
| LOAD_ATTR_INSTANCE_VALUE STORE_ATTR_INSTANCE_VALUE | 6,503,280 | 0.4% | 84.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 6,502,160 | 0.4% | 84.9% |
| LOAD_FAST LOAD_ATTR | 5,792,880 | 0.3% | 85.2% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 5,508,800 | 0.3% | 85.5% |
| LOAD_FAST CALL_LIST_APPEND | 5,480,560 | 0.3% | 85.9% |
| LOAD_FAST COMPARE_OP_INT | 5,461,400 | 0.3% | 86.2% |
| BINARY_OP_ADD_INT LOAD_FAST | 5,359,180 | 0.3% | 86.5% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST | 5,359,180 | 0.3% | 86.8% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_ADD_INT | 5,359,160 | 0.3% | 87.1% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_MULTIPLY_INT | 5,359,160 | 0.3% | 87.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 5,235,040 | 0.3% | 87.8% |
| CALL_BOUND_METHOD_EXACT_ARGS RESUME_CHECK | 5,197,580 | 0.3% | 88.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 4,456,820 | 0.3% | 88.3% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 4,446,600 | 0.3% | 88.6% |
| LOAD_FAST CALL_LEN | 4,446,480 | 0.3% | 88.9% |
| CALL_LEN TO_BOOL_INT | 4,446,480 | 0.3% | 89.1% |
| RETURN_VALUE LOAD_FAST | 4,156,000 | 0.2% | 89.4% |
| ENTER_EXECUTOR FOR_ITER_LIST | 4,032,340 | 0.2% | 89.6% |
| FOR_ITER_LIST STORE_FAST | 3,693,960 | 0.2% | 89.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 3,692,360 | 0.2% | 90.1% |
| GET_ITER FOR_ITER_LIST | 3,690,420 | 0.2% | 90.3% |
| POP_TOP LOAD_FAST_LOAD_FAST | 3,656,960 | 0.2% | 90.5% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 3,640,080 | 0.2% | 90.7% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BOUND_METHOD_EXACT_ARGS | 3,639,840 | 0.2% | 90.9% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 3,620,220 | 0.2% | 91.1% |
| LOAD_CONST LOAD_FAST | 3,471,360 | 0.2% | 91.3% |
| POP_TOP RETURN_CONST | 3,416,200 | 0.2% | 91.5% |
| COPY_FREE_VARS RESUME_CHECK | 3,402,080 | 0.2% | 91.7% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 3,401,800 | 0.2% | 92.0% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_MODULE | 3,401,800 | 0.2% | 92.2% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 3,160,480 | 0.2% | 92.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,145,840 | 0.2% | 92.5% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 3,131,920 | 0.2% | 92.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 3,127,800 | 0.2% | 92.9% |
| COMPARE_OP POP_JUMP_IF_TRUE | 3,127,600 | 0.2% | 93.1% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 3,127,580 | 0.2% | 93.3% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 3,125,700 | 0.2% | 93.5% |
| FOR_ITER_LIST RETURN_CONST | 2,956,800 | 0.2% | 93.6% |
| LOAD_FAST RETURN_VALUE | 2,878,640 | 0.2% | 93.8% |
| COPY TO_BOOL_BOOL | 2,859,040 | 0.2% | 94.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 2,691,600 | 0.2% | 94.1% |
| LOAD_FAST GET_ITER | 2,621,520 | 0.2% | 94.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 2,608,480 | 0.2% | 94.4% |
| LOAD_FAST POP_JUMP_IF_NONE | 2,607,360 | 0.2% | 94.6% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 2,604,000 | 0.2% | 94.8% |
| POP_TOP LOAD_GLOBAL_BUILTIN | 2,603,360 | 0.2% | 94.9% |
| CALL_LIST_APPEND RETURN_CONST | 2,593,240 | 0.2% | 95.1% |
| LOAD_ATTR_CLASS LOAD_FAST | 2,581,600 | 0.2% | 95.2% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 2,316,740 | 0.1% | 95.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 2,099,200 | 0.1% | 95.5% |
| LOAD_ATTR_INSTANCE_VALUE COPY | 2,086,020 | 0.1% | 95.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 2,058,140 | 0.1% | 95.7% |
| LOAD_GLOBAL_MODULE CALL | 1,885,320 | 0.1% | 95.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 1,872,000 | 0.1% | 95.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_METHOD_WITH_VALUES | 1,854,520 | 0.1% | 96.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 1,828,840 | 0.1% | 96.2% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 1,825,460 | 0.1% | 96.3% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 1,825,180 | 0.1% | 96.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 1,817,360 | 0.1% | 96.5% |
| ENTER_EXECUTOR CALL_METHOD_DESCRIPTOR_FAST | 1,800,000 | 0.1% | 96.6% |
| ENTER_EXECUTOR LOAD_FAST | 1,791,920 | 0.1% | 96.7% |
| CALL STORE_FAST | 1,605,420 | 0.1% | 96.8% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,599,720 | 0.1% | 96.9% |
| RETURN_CONST TO_BOOL_BOOL | 1,594,740 | 0.1% | 97.0% |
| CALL POP_TOP | 1,579,920 | 0.1% | 97.1% |
| LOAD_SUPER_ATTR_METHOD CALL | 1,576,900 | 0.1% | 97.2% |
| POP_TOP LOAD_GLOBAL_MODULE | 1,569,040 | 0.1% | 97.3% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,560,240 | 0.1% | 97.4% |
| LOAD_ATTR LOAD_FAST_LOAD_FAST | 1,557,620 | 0.1% | 97.5% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 258,820 | 99.0% |
| RESUME_CHECK | 2,540 | 1.0% |
| RESUME | 20 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 5,760 | 95.4% |
| BINARY_SUBSCR | 240 | 4.0% |
| LOAD_ATTR | 20 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,680 | 94.0% |
| BINARY_SUBSCR | 240 | 4.0% |
| LOAD_ATTR | 80 | 1.3% |
| RETURN_VALUE | 20 | 0.3% |
| BINARY_SUBSCR_DICT | 20 | 0.3% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,318,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,318,140 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,621,520 | 70.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,069,040 | 28.8% |
| CALL_BUILTIN_CLASS | 22,920 | 0.6% |
| CALL | 120 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 3,690,420 | 99.4% |
| FOR_ITER_RANGE | 22,980 | 0.6% |
| FOR_ITER | 260 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 261,380 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 45,868,780 | 91.6% |
| CALL | 1,579,920 | 3.2% |
| POP_JUMP_IF_FALSE | 1,312,960 | 2.6% |
| RETURN_VALUE | 770,480 | 1.5% |
| POP_JUMP_IF_TRUE | 512,000 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 31,196,300 | 62.3% |
| LOAD_FAST | 7,319,840 | 14.6% |
| LOAD_FAST_LOAD_FAST | 3,656,960 | 7.3% |
| RETURN_CONST | 3,416,200 | 6.8% |
| LOAD_GLOBAL_BUILTIN | 2,603,360 | 5.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 560 | 77.8% |
| LOAD_DEREF | 80 | 11.1% |
| LOAD_ATTR_MODULE | 60 | 8.3% |
| LOAD_ATTR | 20 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 640 | 88.9% |
| LOAD_FAST | 80 | 11.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 64,684,180 | 84.6% |
| COMPARE_OP_INT | 6,746,500 | 8.8% |
| LOAD_FAST | 2,878,640 | 3.8% |
| EXIT_INIT_CHECK | 1,318,140 | 1.7% |
| POP_JUMP_IF_TRUE | 773,120 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 28,510,600 | 37.3% |
| STORE_ATTR_INSTANCE_VALUE | 27,472,520 | 35.9% |
| TO_BOOL_BOOL | 7,864,740 | 10.3% |
| STORE_FAST | 7,614,260 | 10.0% |
| LOAD_FAST | 4,156,000 | 5.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 540 | 42.2% |
| COPY | 160 | 12.5% |
| RETURN_CONST | 140 | 10.9% |
| CALL | 120 | 9.4% |
| CALL_LEN | 120 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 520 | 40.6% |
| POP_JUMP_IF_FALSE | 460 | 35.9% |
| POP_JUMP_IF_TRUE | 160 | 12.5% |
| TO_BOOL_INT | 120 | 9.4% |
| UNARY_NOT | 20 | 1.6% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 271,340 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 271,360 | 100.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 263,720 | 75.5% |
| LOAD_ATTR_INSTANCE_VALUE | 84,520 | 24.2% |
| BINARY_OP | 720 | 0.2% |
| LOAD_CONST | 320 | 0.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 344,380 | 98.6% |
| STORE_FAST | 3,860 | 1.1% |
| BINARY_OP | 720 | 0.2% |
| BINARY_OP_ADD_INT | 100 | 0.0% |
| CALL | 60 | 0.0% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,240 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,885,320 | 47.3% |
| LOAD_SUPER_ATTR_METHOD | 1,576,900 | 39.6% |
| ENTER_EXECUTOR | 506,480 | 12.7% |
| LOAD_FAST | 5,720 | 0.1% |
| CALL | 3,420 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,605,420 | 40.3% |
| POP_TOP | 1,579,920 | 39.7% |
| LOAD_FAST | 788,560 | 19.8% |
| CALL | 3,420 | 0.1% |
| CALL_PY_EXACT_ARGS | 1,520 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,127,580 | 98.7% |
| LOAD_FAST | 20,840 | 0.7% |
| LOAD_ATTR | 15,480 | 0.5% |
| LOAD_CONST | 2,680 | 0.1% |
| COMPARE_OP | 1,880 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 3,127,600 | 98.7% |
| POP_JUMP_IF_FALSE | 28,440 | 0.9% |
| STORE_FAST | 10,240 | 0.3% |
| COMPARE_OP | 1,880 | 0.1% |
| COMPARE_OP_INT | 420 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,086,020 | 57.1% |
| LOAD_FAST | 796,160 | 21.8% |
| COMPARE_OP_INT | 773,100 | 21.1% |
| LOAD_ATTR | 60 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,859,040 | 78.2% |
| LOAD_ATTR_INSTANCE_VALUE | 796,120 | 21.8% |
| TO_BOOL | 160 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,825,180 | 53.6% |
| CALL_ALLOC_AND_ENTER_INIT | 1,318,140 | 38.7% |
| CACHE | 258,820 | 7.6% |
| CALL | 100 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,402,080 | 100.0% |
| RESUME | 240 | 0.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 31,196,300 | 78.3% |
| POP_JUMP_IF_TRUE | 3,620,220 | 9.1% |
| POP_JUMP_IF_FALSE | 2,316,740 | 5.8% |
| CALL_LIST_APPEND | 1,825,460 | 4.6% |
| POP_JUMP_IF_NONE | 508,080 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 30,825,760 | 77.4% |
| FOR_ITER_LIST | 4,032,340 | 10.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,800,000 | 4.5% |
| LOAD_FAST | 1,791,920 | 4.5% |
| CALL | 506,480 | 1.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 260 | 50.0% |
| JUMP_BACKWARD | 260 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 260 | 50.0% |
| FOR_ITER_RANGE | 140 | 26.9% |
| FOR_ITER_LIST | 120 | 23.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,460 | 35.8% |
| POP_JUMP_IF_TRUE | 3,400 | 18.9% |
| POP_TOP | 2,800 | 15.5% |
| CALL_LIST_APPEND | 2,300 | 12.8% |
| STORE_FAST | 1,700 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,080 | 33.7% |
| FOR_ITER_LIST | 5,640 | 31.3% |
| FOR_ITER_RANGE | 4,980 | 27.6% |
| ENTER_EXECUTOR | 1,060 | 5.9% |
| FOR_ITER | 260 | 1.4% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 262,360 | 100.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 256,000 | 97.6% |
| LOAD_GLOBAL_MODULE | 6,400 | 2.4% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,792,880 | 42.3% |
| LOAD_GLOBAL_MODULE | 5,235,040 | 38.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,604,000 | 19.0% |
| LOAD_ATTR_SLOT | 61,320 | 0.4% |
| LOAD_ATTR | 10,940 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,986,100 | 72.9% |
| LOAD_FAST_LOAD_FAST | 1,557,620 | 11.4% |
| LOAD_CONST | 1,336,060 | 9.7% |
| CALL_ALLOC_AND_ENTER_INIT | 783,120 | 5.7% |
| COMPARE_OP | 15,480 | 0.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 2,608,480 | 43.9% |
| LOAD_ATTR | 1,336,060 | 22.5% |
| LOAD_ATTR_INSTANCE_VALUE | 801,220 | 13.5% |
| POP_TOP | 286,720 | 4.8% |
| POP_JUMP_IF_FALSE | 286,720 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,471,360 | 58.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,325,640 | 22.3% |
| BINARY_OP_ADD_INT | 804,320 | 13.6% |
| COMPARE_OP_INT | 261,080 | 4.4% |
| STORE_FAST | 12,800 | 0.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 116,150,700 | 35.4% |
| POP_JUMP_IF_FALSE | 76,527,680 | 23.3% |
| LOAD_ATTR_INSTANCE_VALUE | 45,691,580 | 13.9% |
| STORE_FAST | 17,820,220 | 5.4% |
| LOAD_ATTR | 9,986,100 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 193,428,860 | 59.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 78,112,680 | 23.8% |
| CALL_PY_EXACT_ARGS | 10,759,920 | 3.3% |
| STORE_ATTR_INSTANCE_VALUE | 10,477,820 | 3.2% |
| LOAD_ATTR | 5,792,880 | 1.8% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,520 | 98.4% |
| LOAD_ATTR | 40 | 1.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,656,960 | 23.0% |
| STORE_FAST | 3,160,480 | 19.9% |
| STORE_ATTR_INSTANCE_VALUE | 2,058,140 | 13.0% |
| LOAD_ATTR | 1,557,620 | 9.8% |
| POP_JUMP_IF_TRUE | 1,297,920 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 6,502,160 | 40.9% |
| COMPARE_OP | 3,127,580 | 19.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,560,240 | 9.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,557,560 | 9.8% |
| CALL_PY_EXACT_ARGS | 1,319,560 | 8.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 680 | 16.7% |
| POP_JUMP_IF_FALSE | 560 | 13.7% |
| POP_TOP | 500 | 12.3% |
| RESUME | 380 | 9.3% |
| RESUME_CHECK | 380 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,560 | 38.2% |
| LOAD_ATTR | 760 | 18.6% |
| LOAD_FAST | 660 | 16.2% |
| LOAD_GLOBAL_BUILTIN | 480 | 11.8% |
| CALL | 240 | 5.9% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 220 | 50.0% |
| CALL | 100 | 22.7% |
| LOAD_FAST | 60 | 13.6% |
| LOAD_FAST_LOAD_FAST | 60 | 13.6% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 73,070,520 | 85.0% |
| TO_BOOL_BOOL | 8,388,140 | 9.8% |
| TO_BOOL_INT | 4,446,600 | 5.2% |
| COMPARE_OP | 28,440 | 0.0% |
| TO_BOOL | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 76,527,680 | 89.1% |
| LOAD_GLOBAL_MODULE | 3,127,800 | 3.6% |
| ENTER_EXECUTOR | 2,316,740 | 2.7% |
| RETURN_CONST | 2,099,200 | 2.4% |
| POP_TOP | 1,312,960 | 1.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,607,360 | 99.6% |
| LOAD_ATTR_INSTANCE_VALUE | 10,220 | 0.4% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 783,360 | 29.9% |
| LOAD_FAST_LOAD_FAST | 775,680 | 29.6% |
| ENTER_EXECUTOR | 508,080 | 19.4% |
| LOAD_FAST | 293,120 | 11.2% |
| LOAD_GLOBAL_MODULE | 255,960 | 9.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,508,800 | 61.9% |
| COMPARE_OP | 3,127,600 | 35.1% |
| COMPARE_OP_INT | 261,700 | 2.9% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 3,620,220 | 40.7% |
| LOAD_FAST | 2,691,600 | 30.2% |
| LOAD_FAST_LOAD_FAST | 1,297,920 | 14.6% |
| RETURN_VALUE | 773,120 | 8.7% |
| POP_TOP | 512,000 | 5.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 36,100,580 | 73.6% |
| POP_TOP | 3,416,200 | 7.0% |
| FOR_ITER_LIST | 2,956,800 | 6.0% |
| CALL_LIST_APPEND | 2,593,240 | 5.3% |
| POP_JUMP_IF_FALSE | 2,099,200 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 45,868,780 | 93.5% |
| TO_BOOL_BOOL | 1,594,740 | 3.3% |
| EXIT_INIT_CHECK | 1,318,140 | 2.7% |
| INTERPRETER_EXIT | 261,380 | 0.5% |
| STORE_FAST | 5,120 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,220 | 55.5% |
| LOAD_FAST_LOAD_FAST | 540 | 24.5% |
| RETURN_VALUE | 120 | 5.5% |
| LOAD_ATTR | 120 | 5.5% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,020 | 46.4% |
| RETURN_CONST | 380 | 17.3% |
| LOAD_FAST | 320 | 14.5% |
| LOAD_CONST | 160 | 7.3% |
| LOAD_GLOBAL | 140 | 6.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,614,260 | 32.9% |
| LOAD_ATTR_INSTANCE_VALUE | 6,769,840 | 29.2% |
| FOR_ITER_LIST | 3,693,960 | 15.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,125,700 | 13.5% |
| CALL | 1,605,420 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,820,220 | 76.9% |
| LOAD_FAST_LOAD_FAST | 3,160,480 | 13.6% |
| LOAD_GLOBAL_MODULE | 1,872,000 | 8.1% |
| ENTER_EXECUTOR | 267,100 | 1.2% |
| LOAD_GLOBAL_BUILTIN | 30,520 | 0.1% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 2,540 | 99.2% |
| UNPACK_SEQUENCE | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,560 | 100.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,080 | 99.2% |
| CALL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 50.0% |
| LOAD_GLOBAL_MODULE | 2,520 | 49.2% |
| LOAD_GLOBAL | 40 | 0.8% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 796,140 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 796,120 | 100.0% |
| STORE_ATTR | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 20 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 20 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 740 | 61.7% |
| COPY_FREE_VARS | 240 | 20.0% |
| CALL_PY_EXACT_ARGS | 200 | 16.7% |
| CACHE | 20 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 53.3% |
| LOAD_GLOBAL | 380 | 31.7% |
| RETURN_CONST | 120 | 10.0% |
| LOAD_CONST | 40 | 3.3% |
| LOAD_FAST_LOAD_FAST | 20 | 1.7% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,359,160 | 86.9% |
| LOAD_CONST | 804,320 | 13.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,359,180 | 86.9% |
| SWAP | 796,140 | 12.9% |
| COMPARE_OP_INT | 5,680 | 0.1% |
| CALL_BUILTIN_CLASS | 2,520 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,359,160 | 99.9% |
| LOAD_CONST | 5,680 | 0.1% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,359,180 | 99.9% |
| LOAD_CONST | 5,720 | 0.1% |


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
| LOAD_ATTR_INSTANCE_VALUE | 84,440 | 94.3% |
| LOAD_CONST | 5,040 | 5.6% |
| BINARY_OP | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 84,460 | 94.3% |
| CALL_BUILTIN_CLASS | 5,040 | 5.6% |
| CALL | 40 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 10,200 | 99.8% |
| BINARY_SUBSCR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,220 | 100.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 783,120 | 59.4% |
| LOAD_FAST | 259,760 | 19.7% |
| ENTER_EXECUTOR | 252,160 | 19.1% |
| LOAD_GLOBAL_MODULE | 17,800 | 1.4% |
| LOAD_CONST | 5,040 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,318,140 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,639,840 | 70.0% |
| LOAD_FAST_LOAD_FAST | 1,557,560 | 30.0% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,197,580 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,720 | 55.4% |
| BINARY_OP_SUBTRACT_INT | 5,040 | 21.9% |
| LOAD_FAST | 2,560 | 11.1% |
| BINARY_OP_ADD_INT | 2,520 | 11.0% |
| CALL | 140 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 22,920 | 99.7% |
| STORE_FAST | 60 | 0.3% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,446,480 | 100.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 4,446,480 | 100.0% |
| TO_BOOL | 120 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,480,560 | 91.4% |
| ENTER_EXECUTOR | 500,640 | 8.3% |
| RETURN_VALUE | 16,440 | 0.3% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,593,240 | 43.2% |
| ENTER_EXECUTOR | 1,825,460 | 30.4% |
| LOAD_GLOBAL_BUILTIN | 1,308,080 | 21.8% |
| LOAD_GLOBAL_MODULE | 268,680 | 4.5% |
| JUMP_BACKWARD | 2,300 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,800,000 | 56.5% |
| LOAD_CONST | 1,325,640 | 41.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 60,080 | 1.9% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,125,700 | 98.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 60,080 | 1.9% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,200 | 98.1% |
| CALL_METHOD_DESCRIPTOR_O | 180 | 1.7% |
| CALL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,220 | 98.3% |
| CALL_METHOD_DESCRIPTOR_O | 180 | 1.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 103,665,160 | 89.3% |
| LOAD_FAST | 10,759,920 | 9.3% |
| LOAD_FAST_LOAD_FAST | 1,319,560 | 1.1% |
| LOAD_SUPER_ATTR_METHOD | 255,960 | 0.2% |
| CALL_PY_EXACT_ARGS | 62,720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 114,186,820 | 98.4% |
| COPY_FREE_VARS | 1,825,180 | 1.6% |
| CALL_PY_EXACT_ARGS | 62,720 | 0.1% |
| RESUME | 200 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_CLASS | 71,224,640 | 88.1% |
| LOAD_FAST | 5,461,400 | 6.8% |
| LOAD_ATTR_INSTANCE_VALUE | 3,640,080 | 4.5% |
| LOAD_CONST | 261,080 | 0.3% |
| LOAD_FAST_LOAD_FAST | 258,520 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 73,070,520 | 90.4% |
| RETURN_VALUE | 6,746,500 | 8.3% |
| COPY | 773,100 | 1.0% |
| POP_JUMP_IF_TRUE | 261,700 | 0.3% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,032,340 | 52.2% |
| GET_ITER | 3,690,420 | 47.8% |
| JUMP_BACKWARD | 5,640 | 0.1% |
| FOR_ITER | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,693,960 | 47.8% |
| RETURN_CONST | 2,956,800 | 38.3% |
| LOAD_FAST | 550,400 | 7.1% |
| LOAD_GLOBAL_BUILTIN | 527,320 | 6.8% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 23,100 | 45.1% |
| GET_ITER | 22,980 | 44.9% |
| JUMP_BACKWARD | 4,980 | 9.7% |
| FOR_ITER | 140 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 28,080 | 54.8% |
| LOAD_FAST | 10,320 | 20.2% |
| LOAD_GLOBAL_MODULE | 7,560 | 14.8% |
| RETURN_CONST | 5,120 | 10.0% |
| LOAD_GLOBAL | 120 | 0.2% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 73,806,080 | 100.0% |
| LOAD_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 71,224,640 | 96.5% |
| LOAD_FAST | 2,581,600 | 3.5% |
| COMPARE_OP | 80 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 193,428,860 | 78.6% |
| RETURN_VALUE | 28,510,600 | 11.6% |
| LOAD_ATTR_INSTANCE_VALUE | 22,682,240 | 9.2% |
| COPY | 796,120 | 0.3% |
| LOAD_FAST_LOAD_FAST | 527,240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 71,229,720 | 29.0% |
| RETURN_VALUE | 64,684,180 | 26.3% |
| LOAD_FAST | 45,691,580 | 18.6% |
| LOAD_ATTR_INSTANCE_VALUE | 22,682,240 | 9.2% |
| STORE_FAST | 6,769,840 | 2.8% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,112,680 | 68.3% |
| ENTER_EXECUTOR | 30,825,760 | 27.0% |
| LOAD_GLOBAL_MODULE | 1,854,520 | 1.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,817,360 | 1.6% |
| LOAD_FAST_LOAD_FAST | 1,560,240 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 103,665,160 | 90.7% |
| LOAD_FAST | 9,457,520 | 8.3% |
| LOAD_FAST_LOAD_FAST | 1,048,300 | 0.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 121,820 | 0.1% |
| CALL | 840 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 66.7% |
| LOAD_ATTR | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 50.0% |
| STORE_FAST | 60 | 50.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,200 | 99.8% |
| LOAD_ATTR | 120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 61,320 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,145,840 | 40.0% |
| POP_TOP | 2,603,360 | 33.1% |
| CALL_LIST_APPEND | 1,308,080 | 16.6% |
| FOR_ITER_LIST | 527,320 | 6.7% |
| STORE_ATTR_INSTANCE_VALUE | 255,960 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,456,820 | 56.6% |
| LOAD_GLOBAL_MODULE | 3,401,800 | 43.2% |
| LOAD_CONST | 12,760 | 0.2% |
| LOAD_GLOBAL | 220 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 71,229,720 | 81.6% |
| LOAD_GLOBAL_BUILTIN | 3,401,800 | 3.9% |
| STORE_ATTR_INSTANCE_VALUE | 3,131,920 | 3.6% |
| POP_JUMP_IF_FALSE | 3,127,800 | 3.6% |
| STORE_FAST | 1,872,000 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_CLASS | 73,806,080 | 84.6% |
| LOAD_ATTR | 5,235,040 | 6.0% |
| LOAD_FAST | 3,692,360 | 4.2% |
| CALL | 1,885,320 | 2.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,854,520 | 2.1% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,401,800 | 100.0% |
| LOAD_SUPER_ATTR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,576,900 | 46.4% |
| LOAD_FAST | 1,041,860 | 30.6% |
| LOAD_FAST_LOAD_FAST | 527,300 | 15.5% |
| CALL_PY_EXACT_ARGS | 255,960 | 7.5% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 114,186,820 | 93.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,197,580 | 4.2% |
| COPY_FREE_VARS | 3,402,080 | 2.8% |
| CACHE | 2,540 | 0.0% |
| CALL | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 116,150,700 | 94.6% |
| LOAD_GLOBAL_BUILTIN | 3,145,840 | 2.6% |
| LOAD_GLOBAL_MODULE | 1,599,720 | 1.3% |
| RETURN_CONST | 1,093,300 | 0.9% |
| LOAD_FAST_LOAD_FAST | 774,380 | 0.6% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 27,472,520 | 53.0% |
| LOAD_FAST | 10,477,820 | 20.2% |
| LOAD_ATTR_INSTANCE_VALUE | 6,503,280 | 12.6% |
| LOAD_FAST_LOAD_FAST | 6,502,160 | 12.6% |
| SWAP | 796,120 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 36,100,580 | 69.7% |
| LOAD_FAST | 7,335,340 | 14.2% |
| LOAD_GLOBAL_MODULE | 3,131,920 | 6.0% |
| LOAD_CONST | 2,608,480 | 5.0% |
| LOAD_FAST_LOAD_FAST | 2,058,140 | 4.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,864,740 | 55.5% |
| COPY | 2,859,040 | 20.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,828,840 | 12.9% |
| RETURN_CONST | 1,594,740 | 11.3% |
| LOAD_FAST | 20,400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,388,140 | 59.2% |
| POP_JUMP_IF_TRUE | 5,508,800 | 38.9% |
| UNARY_NOT | 271,340 | 1.9% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 4,446,480 | 100.0% |
| TO_BOOL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,446,600 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,520 | 99.2% |
| UNPACK_SEQUENCE | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,540 | 100.0% |


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
|     deferred | 348,400 | 2.5% |
|          hit | 13,621,600 | 97.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 25.0% |
| Failure | 720 | 75.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| remainder | 500 | 69.4% |
| true divide other | 220 | 30.6% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,780 | 35.5% |
|          hit | 10,220 | 62.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 7.7% |
| Failure | 240 | 92.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 240 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,384,900 | 6.7% |
|          hit | 145,524,360 | 93.3% |
|         miss | 6,532,000 | 4.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 125,500 | 97.3% |
| Failure | 3,420 | 2.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class mutable | 1,920 | 56.1% |
| operator wrapper | 1,060 | 31.0% |
| wrong number arguments | 260 | 7.6% |
| other | 120 | 3.5% |
| cfunc noargs | 60 | 1.8% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,166,360 | 3.5% |
|          hit | 87,805,100 | 96.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 18.3% |
| Failure | 1,880 | 81.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 1,680 | 89.4% |
| float long | 120 | 6.4% |
| different types | 80 | 4.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 7,779,720 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 24,022,280 | 5.0% |
|          hit | 458,068,600 | 95.0% |
|         miss | 10,529,260 | 2.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 202,180 | 95.2% |
| Failure | 10,220 | 4.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 4,180 | 40.9% |
| mutable class | 3,140 | 30.7% |
| class method obj | 2,900 | 28.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,040 | 0.0% |
|          hit | 101,800,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,040 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 220 | 0.0% |
|          hit | 3,402,020 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 100.0% |
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
|     deferred | 1,838,860 | 3.3% |
|          hit | 53,216,500 | 96.6% |
|         miss | 1,872,960 | 3.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 36,260 | 99.9% |
| Failure | 40 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not in keys | 40 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 640 | 0.0% |
|          hit | 22,647,680 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 640 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.8% |
|          hit | 2,540 | 98.4% |

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
| Basic | 601,816,180 | 35.8% |
| Not specialized | 118,669,880 | 7.1% |
| Specialized hits | 943,430,280 | 56.1% |
| Specialized misses | 18,937,780 | 1.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 24,022,280 | 60.4% |
| CALL | 10,384,900 | 26.1% |
| COMPARE_OP | 3,166,360 | 8.0% |
| STORE_ATTR | 1,838,860 | 4.6% |
| BINARY_OP | 348,400 | 0.9% |
| BINARY_SUBSCR | 5,780 | 0.0% |
| LOAD_GLOBAL | 2,040 | 0.0% |
| TO_BOOL | 640 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 220 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 6,464,500 | 34.1% |
| LOAD_ATTR_INSTANCE_VALUE | 4,064,760 | 21.5% |
| CALL_PY_EXACT_ARGS | 3,335,820 | 17.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,185,780 | 16.8% |
| STORE_ATTR_INSTANCE_VALUE | 1,872,960 | 9.9% |
| CALL_METHOD_DESCRIPTOR_O | 10,400 | 0.1% |
| RESUME | 3,560 | 0.0% |
| RESUME_CHECK | 3,560 | 0.0% |
| CACHE | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 261,380 | 0.2% |
| Calls to Python functions inlined | 131,376,460 | 99.8% |
| Calls via PyEval_EvalFrame (total) | 261,380 | 0.2% |
| Calls via PyEval_EvalFrame (vector) | 261,380 | 0.2% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 261,380 | 0.2% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 132,955,980 | 101.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 1,929,960 | 6.6% |
| Frees to freelist | 1,930,240 |  |
| Allocations | 27,357,400 | 93.4% |
| Allocations to 512 bytes | 27,356,640 | 93.4% |
| Allocations to 4 kbytes | 520 | 0.0% |
| Allocations over 4 kbytes | 240 | 0.0% |
| Frees | 29,379,224 |  |
| New values | 258,820 |  |
| Interpreter increfs | 839,814,060 | 80.1% |
| Interpreter decrefs | 948,038,700 | 88.2% |
| Increfs | 208,581,323 | 19.9% |
| Decrefs | 127,338,995 | 11.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 38,769,837 |  |
| Method cache misses | 16,483 |  |
| Method cache collisions | 15,896 |  |
| Method cache dunder hits | 766,620 |  |
| Method cache dunder misses | 200 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 3,040 | 600,560 | 23,402,920 |
| 1 | 260 | 1,457,840 | 17,960,000 |
| 2 | 20 | 102,800 | 3,791,720 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 1,060 |  |
| Traces created | 1,060 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 260 | 24.5% |
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
| <= 16 | 20 | 1.9% |
| <= 32 | 280 | 26.4% |
| <= 64 | 220 | 20.8% |
| <= 128 | 80 | 7.5% |
| <= 256 | 220 | 20.8% |
| <= 512 | 240 | 22.6% |


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
| <= 16 | 280 | 26.4% |
| <= 32 | 60 | 5.7% |
| <= 64 | 220 | 20.8% |
| <= 128 | 40 | 3.8% |
| <= 256 | 220 | 20.8% |
| <= 512 | 240 | 22.6% |


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
| CALL_LIST_APPEND | 240 |
| CALL | 180 |
| CALL_ALLOC_AND_ENTER_INIT | 80 |


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
| watched dict modification | 120 |
| watched globals modification | 120 |


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
