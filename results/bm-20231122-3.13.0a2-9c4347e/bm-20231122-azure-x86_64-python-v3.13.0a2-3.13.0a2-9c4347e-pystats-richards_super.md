
# Pystats results

- benchmark: richards_super
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 381,100,640 | 21.5% | 21.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 161,655,260 | 9.1% | 30.6% | 38.7% |
| TO_BOOL_BOOL | 137,415,860 | 7.7% | 38.3% |  |
| POP_JUMP_IF_FALSE | 104,074,240 | 5.9% | 44.2% |  |
| CALL_PY_EXACT_ARGS | 87,665,460 | 4.9% | 49.1% | 8.0% |
| RESUME_CHECK | 87,537,720 | 4.9% | 54.0% | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 77,723,800 | 4.4% | 58.4% | 49.0% |
| RETURN_VALUE | 77,010,280 | 4.3% | 62.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 70,270,340 | 4.0% | 66.7% | 22.3% |
| STORE_FAST | 66,786,160 | 3.8% | 70.5% |  |
| LOAD_GLOBAL_MODULE | 59,453,480 | 3.3% | 73.8% |  |
| COPY | 59,438,320 | 3.3% | 77.2% |  |
| LOAD_CONST | 55,963,760 | 3.2% | 80.3% |  |
| POP_TOP | 53,524,080 | 3.0% | 83.3% |  |
| LOAD_FAST_LOAD_FAST | 41,521,760 | 2.3% | 85.7% |  |
| POP_JUMP_IF_NOT_NONE | 30,754,880 | 1.7% | 87.4% |  |
| POP_JUMP_IF_TRUE | 27,586,400 | 1.6% | 89.0% |  |
| POP_JUMP_IF_NONE | 22,455,200 | 1.3% | 90.2% |  |
| LOAD_GLOBAL_BUILTIN | 21,053,720 | 1.2% | 91.4% |  |
| UNARY_NOT | 19,888,560 | 1.1% | 92.5% |  |
| JUMP_BACKWARD | 18,549,440 | 1.0% | 93.6% |  |
| COMPARE_OP_INT | 14,132,820 | 0.8% | 94.4% |  |
| JUMP_FORWARD | 10,812,160 | 0.6% | 95.0% |  |
| RETURN_CONST | 10,531,840 | 0.6% | 95.6% |  |
| LOAD_DEREF | 10,527,520 | 0.6% | 96.2% |  |
| COPY_FREE_VARS | 10,527,440 | 0.6% | 96.8% |  |
| LOAD_SUPER_ATTR_METHOD | 10,527,200 | 0.6% | 97.4% |  |
| CALL_ISINSTANCE | 10,526,320 | 0.6% | 97.9% |  |
| BINARY_OP_ADD_INT | 9,673,340 | 0.5% | 98.5% |  |
| SWAP | 9,097,280 | 0.5% | 99.0% |  |
| BINARY_SUBSCR_LIST_INT | 6,807,160 | 0.4% | 99.4% |  |
| BINARY_OP | 4,001,820 | 0.2% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 3,089,240 | 0.2% | 99.8% |  |
| FOR_ITER_RANGE | 1,862,100 | 0.1% | 99.9% |  |
| STORE_SUBSCR_LIST_INT | 1,490,200 | 0.1% | 100.0% |  |
| GET_ITER | 372,560 | 0.0% | 100.0% |  |
| STORE_ATTR | 4,880 | 0.0% | 100.0% |  |
| LOAD_ATTR | 3,680 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,680 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 3,640 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 3,640 | 0.0% | 100.0% |  |
| CALL | 3,540 | 0.0% | 100.0% |  |
| BUILD_LIST | 1,280 | 0.0% | 100.0% |  |
| RESUME | 760 | 0.0% | 100.0% | 2.6% |
| INTERPRETER_EXIT | 680 | 0.0% | 100.0% |  |
| TO_BOOL | 600 | 0.0% | 100.0% |  |
| PUSH_NULL | 480 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 480 | 0.0% | 100.0% |  |
| COMPARE_OP | 440 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 320 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 200 | 0.0% | 100.0% |  |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 80 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 135,528,360 | 7.6% | 7.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 89,941,040 | 5.1% | 12.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 77,006,820 | 4.3% | 17.0% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 77,004,440 | 4.3% | 21.4% |
| RESUME_CHECK LOAD_FAST | 59,540,660 | 3.4% | 24.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 51,598,400 | 2.9% | 27.6% |
| COPY TO_BOOL_BOOL | 50,340,880 | 2.8% | 30.5% |
| POP_TOP LOAD_FAST | 49,429,440 | 2.8% | 33.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 47,043,040 | 2.6% | 35.9% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 44,128,800 | 2.5% | 38.4% |
| STORE_FAST LOAD_FAST | 44,032,960 | 2.5% | 40.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 41,762,620 | 2.4% | 43.2% |
| LOAD_ATTR_INSTANCE_VALUE COPY | 34,172,420 | 1.9% | 45.1% |
| LOAD_CONST LOAD_FAST | 29,192,800 | 1.6% | 46.8% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 29,073,640 | 1.6% | 48.4% |
| RETURN_VALUE TO_BOOL_BOOL | 27,586,320 | 1.6% | 50.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 27,586,300 | 1.6% | 51.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 25,419,040 | 1.4% | 53.0% |
| RETURN_VALUE RETURN_VALUE | 24,772,160 | 1.4% | 54.4% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 24,749,900 | 1.4% | 55.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,315,520 | 1.3% | 57.1% |
| LOAD_FAST POP_JUMP_IF_NONE | 22,455,200 | 1.3% | 58.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 21,558,820 | 1.2% | 59.5% |
| LOAD_FAST RETURN_VALUE | 21,297,360 | 1.2% | 60.7% |
| POP_JUMP_IF_FALSE POP_TOP | 19,888,560 | 1.1% | 61.9% |
| TO_BOOL_BOOL UNARY_NOT | 19,888,520 | 1.1% | 63.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 19,888,480 | 1.1% | 64.1% |
| LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS | 17,463,800 | 1.0% | 65.1% |
| POP_JUMP_IF_NONE JUMP_BACKWARD | 17,059,840 | 1.0% | 66.1% |
| JUMP_BACKWARD LOAD_GLOBAL_MODULE | 17,059,820 | 1.0% | 67.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 16,746,520 | 0.9% | 68.0% |
| UNARY_NOT COPY | 16,168,560 | 0.9% | 68.9% |
| POP_JUMP_IF_TRUE POP_TOP | 16,168,560 | 0.9% | 69.8% |
| RETURN_VALUE STORE_FAST | 15,846,720 | 0.9% | 70.7% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 15,387,440 | 0.9% | 71.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 14,585,220 | 0.8% | 72.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 14,245,720 | 0.8% | 73.2% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 14,245,680 | 0.8% | 74.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 14,132,820 | 0.8% | 74.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 14,116,900 | 0.8% | 75.6% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 13,778,720 | 0.8% | 76.3% |
| POP_JUMP_IF_FALSE RETURN_VALUE | 13,392,480 | 0.8% | 77.1% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 12,933,060 | 0.7% | 77.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 12,330,840 | 0.7% | 78.5% |
| LOAD_FAST STORE_FAST | 12,201,120 | 0.7% | 79.2% |
| RESUME_CHECK LOAD_CONST | 10,660,440 | 0.6% | 79.8% |
| JUMP_FORWARD LOAD_FAST | 10,625,920 | 0.6% | 80.4% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 10,530,200 | 0.6% | 81.0% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 10,527,640 | 0.6% | 81.6% |
| RETURN_CONST POP_TOP | 10,527,520 | 0.6% | 82.2% |
| LOAD_DEREF LOAD_FAST | 10,527,360 | 0.6% | 82.8% |
| COPY_FREE_VARS RESUME_CHECK | 10,527,260 | 0.6% | 83.4% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 10,527,200 | 0.6% | 84.0% |
| LOAD_SUPER_ATTR_METHOD LOAD_FAST_LOAD_FAST | 10,527,060 | 0.6% | 84.5% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 10,527,040 | 0.6% | 85.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 10,526,520 | 0.6% | 85.7% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 10,526,380 | 0.6% | 86.3% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 10,526,360 | 0.6% | 86.9% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_BUILTIN | 10,526,240 | 0.6% | 87.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 10,526,240 | 0.6% | 88.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 10,526,240 | 0.6% | 88.7% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 10,526,240 | 0.6% | 89.3% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 9,097,080 | 0.5% | 89.8% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 9,097,080 | 0.5% | 90.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,184,000 | 0.5% | 90.8% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 7,439,320 | 0.4% | 91.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 7,179,920 | 0.4% | 91.6% |
| RETURN_VALUE POP_TOP | 6,939,080 | 0.4% | 92.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 6,863,520 | 0.4% | 92.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 6,807,840 | 0.4% | 92.8% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 6,807,120 | 0.4% | 93.1% |
| LOAD_CONST STORE_FAST | 6,806,560 | 0.4% | 93.5% |
| STORE_FAST JUMP_FORWARD | 6,719,840 | 0.4% | 93.9% |
| BINARY_OP_ADD_INT SWAP | 6,696,100 | 0.4% | 94.3% |
| LOAD_GLOBAL_MODULE COMPARE_OP_INT | 5,482,120 | 0.3% | 94.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_INSTANCE_VALUE | 5,321,360 | 0.3% | 94.9% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 5,319,180 | 0.3% | 95.2% |
| LOAD_GLOBAL_MODULE COPY | 5,206,840 | 0.3% | 95.5% |
| LOAD_CONST COMPARE_OP_INT | 4,689,280 | 0.3% | 95.7% |
| POP_TOP JUMP_FORWARD | 4,092,320 | 0.2% | 96.0% |
| LOAD_CONST BINARY_OP | 3,998,640 | 0.2% | 96.2% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 3,961,200 | 0.2% | 96.4% |
| LOAD_FAST COPY | 3,890,400 | 0.2% | 96.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 3,848,800 | 0.2% | 96.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 3,774,720 | 0.2% | 97.1% |
| STORE_FAST LOAD_GLOBAL_MODULE | 3,720,400 | 0.2% | 97.3% |
| UNARY_NOT RETURN_VALUE | 3,720,000 | 0.2% | 97.5% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 3,089,200 | 0.2% | 97.7% |
| BINARY_OP LOAD_CONST | 2,398,580 | 0.1% | 97.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 2,232,560 | 0.1% | 97.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,916,820 | 0.1% | 98.0% |
| RETURN_VALUE LOAD_FAST | 1,863,200 | 0.1% | 98.1% |
| POP_JUMP_IF_NONE LOAD_FAST_LOAD_FAST | 1,620,320 | 0.1% | 98.2% |
| STORE_FAST LOAD_CONST | 1,600,000 | 0.1% | 98.3% |
| BINARY_OP_SUBTRACT_INT SWAP | 1,599,980 | 0.1% | 98.4% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 1,599,880 | 0.1% | 98.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 1,599,760 | 0.1% | 98.6% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 1,490,160 | 0.1% | 98.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,490,100 | 0.1% | 98.8% |
| FOR_ITER_RANGE STORE_FAST | 1,489,540 | 0.1% | 98.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 420 | 61.8% |
| RESUME | 140 | 20.6% |
| COPY_FREE_VARS | 120 | 17.6% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 40 | 50.0% |
| LOAD_FAST | 20 | 25.0% |
| STORE_FAST | 20 | 25.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,640 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 372,300 | 99.9% |
| CALL_BUILTIN_CLASS | 140 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 372,360 | 99.9% |
| EXTENDED_ARG | 160 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 680 | 100.0% |


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
| POP_JUMP_IF_FALSE | 19,888,560 | 37.2% |
| POP_JUMP_IF_TRUE | 16,168,560 | 30.2% |
| RETURN_CONST | 10,527,520 | 19.7% |
| RETURN_VALUE | 6,939,080 | 13.0% |
| CALL | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 49,429,440 | 92.3% |
| JUMP_FORWARD | 4,092,320 | 7.6% |
| RETURN_CONST | 960 | 0.0% |
| LOAD_GLOBAL_MODULE | 720 | 0.0% |
| LOAD_GLOBAL | 240 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320 | 66.7% |
| LOAD_DEREF | 80 | 16.7% |
| LOAD_ATTR_MODULE | 60 | 12.5% |
| LOAD_ATTR | 20 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 400 | 83.3% |
| LOAD_FAST | 80 | 16.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 24,772,160 | 32.2% |
| LOAD_FAST | 21,297,360 | 27.7% |
| POP_JUMP_IF_FALSE | 13,392,480 | 17.4% |
| LOAD_ATTR_INSTANCE_VALUE | 12,933,060 | 16.8% |
| UNARY_NOT | 3,720,000 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 27,586,320 | 35.8% |
| RETURN_VALUE | 24,772,160 | 32.2% |
| STORE_FAST | 15,846,720 | 20.6% |
| POP_TOP | 6,939,080 | 9.0% |
| LOAD_FAST | 1,863,200 | 2.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 40 | 50.0% |
| JUMP_BACKWARD | 20 | 25.0% |
| LOAD_CONST | 20 | 25.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 160 | 26.7% |
| RETURN_VALUE | 80 | 13.3% |
| CALL | 80 | 13.3% |
| CALL_ISINSTANCE | 80 | 13.3% |
| LOAD_GLOBAL | 60 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 300 | 50.0% |
| POP_JUMP_IF_FALSE | 160 | 26.7% |
| POP_JUMP_IF_TRUE | 100 | 16.7% |
| UNARY_NOT | 40 | 6.7% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 19,888,520 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 16,168,560 | 81.3% |
| RETURN_VALUE | 3,720,000 | 18.7% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,998,640 | 99.9% |
| BINARY_OP | 1,820 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,260 | 0.0% |
| LOAD_FAST | 40 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,398,580 | 59.9% |
| SWAP | 801,200 | 20.0% |
| LOAD_FAST | 800,040 | 20.0% |
| BINARY_OP | 1,820 | 0.0% |
| BINARY_OP_ADD_INT | 100 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,240 | 96.9% |
| LOAD_GLOBAL | 40 | 3.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 540 | 15.3% |
| LOAD_GLOBAL_MODULE | 540 | 15.3% |
| LOAD_ATTR | 500 | 14.1% |
| LOAD_FAST | 480 | 13.6% |
| PUSH_NULL | 400 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 880 | 24.9% |
| CALL_ALLOC_AND_ENTER_INIT | 520 | 14.7% |
| RESUME | 440 | 12.4% |
| RESUME_CHECK | 420 | 11.9% |
| POP_TOP | 360 | 10.2% |


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
| LOAD_CONST | 240 | 54.5% |
| LOAD_GLOBAL | 60 | 13.6% |
| LOAD_GLOBAL_MODULE | 60 | 13.6% |
| LOAD_ATTR | 40 | 9.1% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220 | 50.0% |
| COMPARE_OP_INT | 220 | 50.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 34,172,420 | 57.5% |
| UNARY_NOT | 16,168,560 | 27.2% |
| LOAD_GLOBAL_MODULE | 5,206,840 | 8.8% |
| LOAD_FAST | 3,890,400 | 6.5% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 50,340,880 | 84.7% |
| LOAD_ATTR_INSTANCE_VALUE | 9,097,080 | 15.3% |
| LOAD_ATTR | 200 | 0.0% |
| TO_BOOL | 160 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,526,380 | 100.0% |
| CALL_ALLOC_AND_ENTER_INIT | 840 | 0.0% |
| CACHE | 120 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,527,260 | 100.0% |
| RESUME | 180 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 160 | 33.3% |
| JUMP_BACKWARD | 160 | 33.3% |
| POP_JUMP_IF_FALSE | 160 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 280 | 58.3% |
| JUMP_BACKWARD | 160 | 33.3% |
| FOR_ITER | 40 | 8.3% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40 | 33.3% |
| EXTENDED_ARG | 40 | 33.3% |
| JUMP_BACKWARD | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 50.0% |
| FOR_ITER_RANGE | 60 | 50.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 17,059,840 | 92.0% |
| STORE_SUBSCR_LIST_INT | 1,489,260 | 8.0% |
| POP_TOP | 160 | 0.0% |
| EXTENDED_ARG | 160 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 17,059,820 | 92.0% |
| FOR_ITER_RANGE | 1,489,400 | 8.0% |
| EXTENDED_ARG | 160 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,719,840 | 62.2% |
| POP_TOP | 4,092,320 | 37.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,625,920 | 98.3% |
| LOAD_FAST_LOAD_FAST | 186,240 | 1.7% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 78.3% |
| COPY | 200 | 5.4% |
| LOAD_GLOBAL | 160 | 4.3% |
| LOAD_GLOBAL_MODULE | 160 | 4.3% |
| RETURN_VALUE | 120 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,100 | 29.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 700 | 19.0% |
| CALL | 500 | 13.6% |
| LOAD_FAST | 440 | 12.0% |
| LOAD_CONST | 220 | 6.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 15,387,440 | 27.5% |
| LOAD_ATTR_INSTANCE_VALUE | 14,585,220 | 26.1% |
| RESUME_CHECK | 10,660,440 | 19.0% |
| POP_JUMP_IF_FALSE | 6,863,520 | 12.3% |
| BINARY_OP | 2,398,580 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,192,800 | 52.2% |
| BINARY_OP_ADD_INT | 8,184,000 | 14.6% |
| STORE_FAST | 6,806,560 | 12.2% |
| COMPARE_OP_INT | 4,689,280 | 8.4% |
| BINARY_OP | 3,998,640 | 7.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 10,527,200 | 100.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| NOP | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,527,360 | 100.0% |
| PUSH_NULL | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 59,540,660 | 15.6% |
| POP_JUMP_IF_FALSE | 51,598,400 | 13.5% |
| POP_TOP | 49,429,440 | 13.0% |
| STORE_FAST | 44,032,960 | 11.6% |
| STORE_ATTR_INSTANCE_VALUE | 41,762,620 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 135,528,360 | 35.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 77,004,440 | 20.2% |
| STORE_ATTR_INSTANCE_VALUE | 44,128,800 | 11.6% |
| POP_JUMP_IF_NOT_NONE | 23,315,520 | 6.1% |
| POP_JUMP_IF_NONE | 22,455,200 | 5.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 14,245,720 | 34.3% |
| RESUME_CHECK | 10,527,640 | 25.4% |
| LOAD_SUPER_ATTR_METHOD | 10,527,060 | 25.4% |
| POP_JUMP_IF_NOT_NONE | 3,848,800 | 9.3% |
| POP_JUMP_IF_NONE | 1,620,320 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 16,746,520 | 40.3% |
| CALL_PY_EXACT_ARGS | 14,245,680 | 34.3% |
| LOAD_ATTR_INSTANCE_VALUE | 10,526,360 | 25.4% |
| STORE_ATTR | 1,320 | 0.0% |
| LOAD_FAST | 800 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 17.4% |
| STORE_FAST | 560 | 15.2% |
| RETURN_VALUE | 280 | 7.6% |
| LOAD_CONST | 280 | 7.6% |
| POP_TOP | 240 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,560 | 42.4% |
| CALL | 540 | 14.7% |
| LOAD_GLOBAL_BUILTIN | 280 | 7.6% |
| LOAD_FAST | 260 | 7.1% |
| LOAD_GLOBAL | 240 | 6.5% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 160 | 50.0% |
| LOAD_FAST_LOAD_FAST | 140 | 43.8% |
| LOAD_FAST | 20 | 6.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 89,941,040 | 86.4% |
| COMPARE_OP_INT | 14,132,820 | 13.6% |
| COMPARE_OP | 220 | 0.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,598,400 | 49.6% |
| POP_TOP | 19,888,560 | 19.1% |
| RETURN_VALUE | 13,392,480 | 12.9% |
| LOAD_GLOBAL_MODULE | 12,330,840 | 11.8% |
| LOAD_CONST | 6,863,520 | 6.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,455,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,059,840 | 76.0% |
| LOAD_FAST | 3,774,720 | 16.8% |
| LOAD_FAST_LOAD_FAST | 1,620,320 | 7.2% |
| RETURN_CONST | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,315,520 | 75.8% |
| LOAD_ATTR_INSTANCE_VALUE | 7,439,320 | 24.2% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,419,040 | 82.7% |
| LOAD_FAST_LOAD_FAST | 3,848,800 | 12.5% |
| LOAD_CONST | 1,487,040 | 4.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 27,586,300 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 16,168,560 | 58.6% |
| LOAD_GLOBAL_BUILTIN | 10,526,240 | 38.2% |
| RETURN_VALUE | 891,440 | 3.2% |
| LOAD_GLOBAL | 160 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 10,530,200 | 100.0% |
| POP_TOP | 960 | 0.0% |
| STORE_ATTR | 360 | 0.0% |
| POP_JUMP_IF_NONE | 160 | 0.0% |
| FOR_ITER_RANGE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,527,520 | 100.0% |
| EXIT_INIT_CHECK | 3,640 | 0.0% |
| INTERPRETER_EXIT | 680 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 59.0% |
| LOAD_FAST_LOAD_FAST | 1,320 | 27.0% |
| STORE_ATTR | 360 | 7.4% |
| SWAP | 200 | 4.1% |
| LOAD_GLOBAL | 60 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,380 | 28.3% |
| STORE_ATTR_INSTANCE_VALUE | 1,360 | 27.9% |
| LOAD_FAST_LOAD_FAST | 940 | 19.3% |
| LOAD_CONST | 400 | 8.2% |
| RETURN_CONST | 360 | 7.4% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 24,749,900 | 37.1% |
| RETURN_VALUE | 15,846,720 | 23.7% |
| LOAD_FAST | 12,201,120 | 18.3% |
| LOAD_CONST | 6,806,560 | 10.2% |
| BINARY_SUBSCR_LIST_INT | 5,319,180 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,032,960 | 65.9% |
| LOAD_GLOBAL_BUILTIN | 10,526,240 | 15.8% |
| JUMP_FORWARD | 6,719,840 | 10.1% |
| LOAD_GLOBAL_MODULE | 3,720,400 | 5.6% |
| LOAD_CONST | 1,600,000 | 2.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,696,100 | 73.6% |
| BINARY_OP_SUBTRACT_INT | 1,599,980 | 17.6% |
| BINARY_OP | 801,200 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 9,097,080 | 100.0% |
| STORE_ATTR | 200 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 440 | 57.9% |
| COPY_FREE_VARS | 180 | 23.7% |
| CACHE | 140 | 18.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 39.5% |
| LOAD_GLOBAL | 220 | 28.9% |
| LOAD_CONST | 200 | 26.3% |
| LOAD_FAST_LOAD_FAST | 40 | 5.3% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,184,000 | 84.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,489,240 | 15.4% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 6,696,100 | 69.2% |
| LOAD_CONST | 1,489,260 | 15.4% |
| LOAD_FAST | 1,487,980 | 15.4% |


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
| LOAD_CONST | 3,089,200 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,599,980 | 51.8% |
| LOAD_FAST | 1,489,260 | 48.2% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,807,120 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,319,180 | 78.1% |
| LOAD_FAST | 1,487,980 | 21.9% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,400 | 65.9% |
| RETURN_VALUE | 720 | 19.8% |
| CALL | 520 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,800 | 76.9% |
| COPY_FREE_VARS | 840 | 23.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 80.0% |
| CALL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 140 | 70.0% |
| STORE_FAST | 60 | 30.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,526,240 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 10,526,240 | 100.0% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 47,043,040 | 53.7% |
| LOAD_ATTR_INSTANCE_VALUE | 17,463,800 | 19.9% |
| LOAD_FAST_LOAD_FAST | 14,245,680 | 16.3% |
| LOAD_FAST | 7,179,920 | 8.2% |
| LOAD_GLOBAL_MODULE | 1,599,880 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 77,006,820 | 87.8% |
| COPY_FREE_VARS | 10,526,380 | 12.0% |
| CALL_PY_EXACT_ARGS | 132,260 | 0.2% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,482,120 | 38.8% |
| LOAD_CONST | 4,689,280 | 33.2% |
| LOAD_ATTR_INSTANCE_VALUE | 3,961,200 | 28.0% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,132,820 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,489,400 | 80.0% |
| GET_ITER | 372,360 | 20.0% |
| EXTENDED_ARG | 280 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,489,540 | 80.0% |
| LOAD_FAST | 372,400 | 20.0% |
| RETURN_CONST | 160 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 135,528,360 | 83.8% |
| LOAD_FAST_LOAD_FAST | 10,526,360 | 6.5% |
| COPY | 9,097,080 | 5.6% |
| LOAD_GLOBAL_MODULE | 5,321,360 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,181,000 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 34,172,420 | 21.1% |
| STORE_FAST | 24,749,900 | 15.3% |
| LOAD_FAST | 21,558,820 | 13.3% |
| TO_BOOL_BOOL | 19,888,480 | 12.3% |
| CALL_PY_EXACT_ARGS | 17,463,800 | 10.8% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 77,004,440 | 99.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 717,940 | 0.9% |
| RETURN_VALUE | 720 | 0.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 47,043,040 | 60.5% |
| LOAD_FAST_LOAD_FAST | 14,245,720 | 18.3% |
| LOAD_FAST | 14,116,900 | 18.2% |
| LOAD_GLOBAL_MODULE | 1,599,760 | 2.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 717,940 | 0.9% |


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

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 10,526,240 | 50.0% |
| STORE_FAST | 10,526,240 | 50.0% |
| RESUME_CHECK | 920 | 0.0% |
| LOAD_GLOBAL | 280 | 0.0% |
| POP_JUMP_IF_FALSE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 10,527,200 | 50.0% |
| LOAD_FAST | 10,526,520 | 50.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,059,820 | 28.7% |
| LOAD_FAST | 13,778,720 | 23.2% |
| POP_JUMP_IF_FALSE | 12,330,840 | 20.7% |
| RESUME_CHECK | 6,807,840 | 11.5% |
| STORE_FAST | 3,720,400 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 29,073,640 | 48.9% |
| CALL_ISINSTANCE | 10,526,240 | 17.7% |
| COMPARE_OP_INT | 5,482,120 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 5,321,360 | 9.0% |
| COPY | 5,206,840 | 8.8% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,527,040 | 100.0% |
| LOAD_SUPER_ATTR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,527,060 | 100.0% |
| LOAD_FAST | 140 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 77,006,820 | 88.0% |
| COPY_FREE_VARS | 10,527,260 | 12.0% |
| CALL_ALLOC_AND_ENTER_INIT | 2,800 | 0.0% |
| CACHE | 420 | 0.0% |
| CALL | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,540,660 | 68.0% |
| LOAD_CONST | 10,660,440 | 12.2% |
| LOAD_FAST_LOAD_FAST | 10,527,640 | 12.0% |
| LOAD_GLOBAL_MODULE | 6,807,840 | 7.8% |
| LOAD_GLOBAL_BUILTIN | 920 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,128,800 | 62.8% |
| LOAD_FAST_LOAD_FAST | 16,746,520 | 23.8% |
| SWAP | 9,097,080 | 12.9% |
| STORE_ATTR_INSTANCE_VALUE | 295,420 | 0.4% |
| STORE_ATTR | 1,360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,762,620 | 59.4% |
| LOAD_CONST | 15,387,440 | 21.9% |
| RETURN_CONST | 10,530,200 | 15.0% |
| LOAD_GLOBAL_MODULE | 1,916,820 | 2.7% |
| LOAD_FAST_LOAD_FAST | 377,780 | 0.5% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,490,160 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,489,260 | 99.9% |
| LOAD_CONST | 940 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 50,340,880 | 36.6% |
| LOAD_GLOBAL_MODULE | 29,073,640 | 21.2% |
| RETURN_VALUE | 27,586,320 | 20.1% |
| LOAD_ATTR_INSTANCE_VALUE | 19,888,480 | 14.5% |
| CALL_ISINSTANCE | 10,526,240 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 89,941,040 | 65.5% |
| POP_JUMP_IF_TRUE | 27,586,300 | 20.1% |
| UNARY_NOT | 19,888,520 | 14.5% |


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
|     deferred | 3,999,840 | 23.9% |
|          hit | 12,762,640 | 76.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 8.1% |
| Failure | 1,820 | 91.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 760 | 41.8% |
| and int | 580 | 31.9% |
| xor | 380 | 20.9% |
| multiply different types | 100 | 5.5% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 6,807,160 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,190,901,980 | 375,700,649,042,406.1% |
|          hit | 91,185,380 | 92.9% |
|         miss | 7,010,240 | 7.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 133,780 | 99.9% |
| Failure | 100 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 60.0% |
| other | 40 | 40.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 220 | 0.0% |
|          hit | 14,132,820 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 1,862,100 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,189,135,220 | 154,119,171,888,158.2% |
|          hit | 138,723,340 | 58.0% |
|         miss | 100,655,840 | 42.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,900,780 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,840 | 0.0% |
|          hit | 80,507,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,840 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 160 | 0.0% |
|          hit | 10,527,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 100.0% |
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
|     deferred | 368,934,881,474,190,740,060 | 524,985,736,756,413.9% |
|          hit | 54,602,220 | 77.7% |
|         miss | 15,668,120 | 22.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 296,780 | 99.9% |
| Failure | 360 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not in keys | 360 | 100.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 1,490,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 300 | 0.0% |
|          hit | 137,415,860 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 825,659,280 | 46.5% |
| Not specialized | 188,889,960 | 10.6% |
| Specialized hits | 637,553,820 | 35.9% |
| Specialized misses | 123,334,220 | 6.9% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 368,934,881,474,190,901,980 | 33.3% |
| STORE_ATTR | 368,934,881,474,190,740,060 | 33.3% |
| LOAD_ATTR | 368,934,881,474,189,135,220 | 33.3% |
| BINARY_OP | 3,999,840 | 0.0% |
| LOAD_GLOBAL | 1,840 | 0.0% |
| TO_BOOL | 300 | 0.0% |
| COMPARE_OP | 220 | 0.0% |
| LOAD_SUPER_ATTR | 160 | 0.0% |
| FOR_ITER | 60 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 62,601,460 | 50.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 38,054,380 | 30.9% |
| STORE_ATTR_INSTANCE_VALUE | 15,668,120 | 12.7% |
| CALL_PY_EXACT_ARGS | 7,010,240 | 5.7% |
| RESUME | 20 | 0.0% |
| RESUME_CHECK | 20 | 0.0% |
| CACHE | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 680 | 0.0% |
| Calls to Python functions inlined | 87,537,800 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 680 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 680 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 680 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 80,662,500 | 92.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 2,620 | 0.0% |
| Frees to freelist | 2,300 |  |
| Allocations | 9,450,800 | 100.0% |
| Allocations to 512 bytes | 9,450,800 | 100.0% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 9,445,152 |  |
| New values | 520 |  |
| Interpreter increfs | 661,835,300 | 86.0% |
| Interpreter decrefs | 734,888,080 | 94.4% |
| Increfs | 107,433,600 | 14.0% |
| Decrefs | 43,822,137 | 5.6% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 113,410,702 |  |
| Method cache misses | 2,921,778 |  |
| Method cache collisions | 2,920,904 |  |
| Method cache dunder hits | 840 |  |
| Method cache dunder misses | 200 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 144,640 |
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
