
# Pystats results

- benchmark: richards_super
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 348,289,860 | 21.9% | 21.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 146,778,480 | 9.2% | 31.1% | 34.9% |
| TO_BOOL_BOOL | 101,068,140 | 6.4% | 37.5% |  |
| CALL_PY_EXACT_ARGS | 82,093,240 | 5.2% | 42.6% | 8.5% |
| RESUME_CHECK | 81,965,500 | 5.2% | 47.8% | 0.0% |
| POP_JUMP_IF_FALSE | 81,216,640 | 5.1% | 52.9% |  |
| RETURN_VALUE | 72,657,020 | 4.6% | 57.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 72,039,760 | 4.5% | 62.0% | 44.6% |
| STORE_ATTR_INSTANCE_VALUE | 69,153,620 | 4.3% | 66.4% | 22.7% |
| STORE_FAST | 65,669,440 | 4.1% | 70.5% |  |
| LOAD_CONST | 52,642,240 | 3.3% | 73.8% |  |
| POP_TOP | 48,842,720 | 3.1% | 76.9% |  |
| COPY | 48,068,020 | 3.0% | 79.9% |  |
| LOAD_FAST_LOAD_FAST | 41,521,760 | 2.6% | 82.5% |  |
| LOAD_GLOBAL_MODULE | 41,305,880 | 2.6% | 85.1% |  |
| POP_JUMP_IF_NOT_NONE | 30,754,880 | 1.9% | 87.0% |  |
| POP_JUMP_IF_NONE | 22,455,200 | 1.4% | 88.4% |  |
| POP_JUMP_IF_TRUE | 22,014,180 | 1.4% | 89.8% |  |
| LOAD_GLOBAL_BUILTIN | 21,053,720 | 1.3% | 91.1% |  |
| ENTER_EXECUTOR | 17,460,400 | 1.1% | 92.2% |  |
| UNARY_NOT | 15,207,200 | 1.0% | 93.2% |  |
| COMPARE_OP_INT | 13,016,100 | 0.8% | 94.0% |  |
| JUMP_FORWARD | 10,812,160 | 0.7% | 94.7% |  |
| RETURN_CONST | 10,531,840 | 0.7% | 95.4% |  |
| LOAD_DEREF | 10,527,520 | 0.7% | 96.0% |  |
| COPY_FREE_VARS | 10,527,440 | 0.7% | 96.7% |  |
| LOAD_SUPER_ATTR_METHOD | 10,527,200 | 0.7% | 97.3% |  |
| CALL_ISINSTANCE | 10,526,320 | 0.7% | 98.0% |  |
| SWAP | 7,980,560 | 0.5% | 98.5% |  |
| BINARY_OP_ADD_INT | 7,468,540 | 0.5% | 99.0% |  |
| BINARY_SUBSCR_LIST_INT | 6,807,160 | 0.4% | 99.4% |  |
| BINARY_OP | 4,001,820 | 0.3% | 99.7% |  |
| BINARY_OP_SUBTRACT_INT | 2,001,160 | 0.1% | 99.8% |  |
| NOP | 1,859,120 | 0.1% | 99.9% |  |
| FOR_ITER_RANGE | 745,380 | 0.0% | 99.9% |  |
| STORE_SUBSCR_LIST_INT | 402,120 | 0.0% | 100.0% |  |
| GET_ITER | 372,560 | 0.0% | 100.0% |  |
| STORE_ATTR | 4,880 | 0.0% | 100.0% |  |
| LOAD_ATTR | 3,680 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,680 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 3,640 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 3,640 | 0.0% | 100.0% |  |
| CALL | 3,540 | 0.0% | 100.0% |  |
| BUILD_LIST | 1,280 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,000 | 0.0% | 100.0% |  |
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
| STORE_SUBSCR | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 121,981,900 | 7.7% | 7.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 71,434,600 | 4.5% | 12.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 63,846,900 | 4.0% | 16.2% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 59,944,920 | 3.8% | 19.9% |
| RESUME_CHECK LOAD_FAST | 53,968,440 | 3.4% | 23.3% |
| POP_TOP LOAD_FAST | 44,748,080 | 2.8% | 26.2% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 44,128,800 | 2.8% | 28.9% |
| STORE_FAST LOAD_FAST | 42,916,240 | 2.7% | 31.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 41,470,820 | 2.6% | 34.2% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 40,645,900 | 2.6% | 36.8% |
| COPY TO_BOOL_BOOL | 40,087,300 | 2.5% | 39.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 32,679,840 | 2.1% | 41.4% |
| LOAD_CONST LOAD_FAST | 29,192,800 | 1.8% | 43.2% |
| LOAD_ATTR_INSTANCE_VALUE COPY | 28,600,200 | 1.8% | 45.0% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 25,419,040 | 1.6% | 46.6% |
| RETURN_VALUE RETURN_VALUE | 24,772,160 | 1.6% | 48.2% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 24,749,900 | 1.6% | 49.7% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,315,520 | 1.5% | 51.2% |
| RETURN_VALUE TO_BOOL_BOOL | 23,233,060 | 1.5% | 52.6% |
| LOAD_FAST POP_JUMP_IF_NONE | 22,455,200 | 1.4% | 54.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 22,014,080 | 1.4% | 55.4% |
| LOAD_FAST RETURN_VALUE | 21,297,360 | 1.3% | 56.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 20,470,740 | 1.3% | 58.1% |
| POP_JUMP_IF_FALSE POP_TOP | 19,560,460 | 1.2% | 59.3% |
| LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS | 17,463,800 | 1.1% | 60.4% |
| POP_JUMP_IF_NONE ENTER_EXECUTOR | 17,059,500 | 1.1% | 61.5% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 16,746,520 | 1.1% | 62.5% |
| RETURN_VALUE STORE_FAST | 15,846,720 | 1.0% | 63.5% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 15,387,440 | 1.0% | 64.5% |
| TO_BOOL_BOOL UNARY_NOT | 15,207,160 | 1.0% | 65.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 15,207,120 | 1.0% | 66.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 14,245,720 | 0.9% | 67.3% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 14,245,680 | 0.9% | 68.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 14,116,900 | 0.9% | 69.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 13,778,720 | 0.9% | 69.9% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 13,016,100 | 0.8% | 70.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 12,933,060 | 0.8% | 71.6% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 12,351,780 | 0.8% | 72.3% |
| LOAD_FAST STORE_FAST | 12,201,120 | 0.8% | 73.1% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 12,014,120 | 0.8% | 73.9% |
| ENTER_EXECUTOR LOAD_ATTR_METHOD_WITH_VALUES | 11,487,300 | 0.7% | 74.6% |
| UNARY_NOT COPY | 11,487,200 | 0.7% | 75.3% |
| POP_JUMP_IF_TRUE POP_TOP | 11,487,200 | 0.7% | 76.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 11,242,760 | 0.7% | 76.7% |
| RESUME_CHECK LOAD_CONST | 10,660,440 | 0.7% | 77.4% |
| JUMP_FORWARD LOAD_FAST | 10,625,920 | 0.7% | 78.1% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 10,530,200 | 0.7% | 78.7% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 10,527,640 | 0.7% | 79.4% |
| RETURN_CONST POP_TOP | 10,527,520 | 0.7% | 80.1% |
| LOAD_DEREF LOAD_FAST | 10,527,360 | 0.7% | 80.7% |
| COPY_FREE_VARS RESUME_CHECK | 10,527,260 | 0.7% | 81.4% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 10,527,200 | 0.7% | 82.0% |
| LOAD_SUPER_ATTR_METHOD LOAD_FAST_LOAD_FAST | 10,527,060 | 0.7% | 82.7% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 10,527,040 | 0.7% | 83.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 10,526,520 | 0.7% | 84.0% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 10,526,380 | 0.7% | 84.7% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 10,526,360 | 0.7% | 85.4% |
| POP_JUMP_IF_TRUE LOAD_GLOBAL_BUILTIN | 10,526,240 | 0.7% | 86.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 10,526,240 | 0.7% | 86.7% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 10,526,240 | 0.7% | 87.3% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 10,526,240 | 0.7% | 88.0% |
| POP_JUMP_IF_FALSE RETURN_VALUE | 9,039,220 | 0.6% | 88.6% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 7,980,360 | 0.5% | 89.1% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 7,980,360 | 0.5% | 89.6% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 7,439,320 | 0.5% | 90.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 7,179,920 | 0.5% | 90.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 7,067,280 | 0.4% | 90.9% |
| RETURN_VALUE POP_TOP | 6,939,080 | 0.4% | 91.4% |
| POP_JUMP_IF_FALSE LOAD_CONST | 6,834,880 | 0.4% | 91.8% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 6,807,840 | 0.4% | 92.2% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 6,807,120 | 0.4% | 92.7% |
| LOAD_CONST STORE_FAST | 6,806,560 | 0.4% | 93.1% |
| STORE_FAST JUMP_FORWARD | 6,719,840 | 0.4% | 93.5% |
| BINARY_OP_ADD_INT SWAP | 5,579,380 | 0.4% | 93.9% |
| LOAD_GLOBAL_MODULE COMPARE_OP_INT | 5,482,120 | 0.3% | 94.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_INSTANCE_VALUE | 5,321,360 | 0.3% | 94.5% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 5,319,180 | 0.3% | 94.9% |
| LOAD_GLOBAL_MODULE COPY | 5,206,840 | 0.3% | 95.2% |
| ENTER_EXECUTOR POP_JUMP_IF_FALSE | 4,353,260 | 0.3% | 95.5% |
| POP_TOP JUMP_FORWARD | 4,092,320 | 0.3% | 95.7% |
| LOAD_CONST BINARY_OP | 3,998,640 | 0.3% | 96.0% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 3,961,200 | 0.2% | 96.2% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 3,848,800 | 0.2% | 96.5% |
| POP_JUMP_IF_NONE LOAD_FAST | 3,774,720 | 0.2% | 96.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 3,720,400 | 0.2% | 97.0% |
| UNARY_NOT RETURN_VALUE | 3,720,000 | 0.2% | 97.2% |
| LOAD_CONST COMPARE_OP_INT | 3,572,560 | 0.2% | 97.4% |
| LOAD_FAST COPY | 2,773,680 | 0.2% | 97.6% |
| BINARY_OP LOAD_CONST | 2,398,580 | 0.2% | 97.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 2,232,560 | 0.1% | 97.9% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 2,001,120 | 0.1% | 98.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,916,820 | 0.1% | 98.1% |
| RETURN_VALUE LOAD_FAST | 1,863,200 | 0.1% | 98.2% |
| NOP LOAD_FAST | 1,859,040 | 0.1% | 98.4% |
| POP_JUMP_IF_FALSE NOP | 1,859,040 | 0.1% | 98.5% |
| POP_JUMP_IF_NONE LOAD_FAST_LOAD_FAST | 1,620,320 | 0.1% | 98.6% |
| STORE_FAST LOAD_CONST | 1,600,000 | 0.1% | 98.7% |
| BINARY_OP_SUBTRACT_INT SWAP | 1,599,980 | 0.1% | 98.8% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 1,599,880 | 0.1% | 98.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 1,599,760 | 0.1% | 99.0% |


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
| POP_JUMP_IF_FALSE | 1,859,040 | 100.0% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,859,040 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 19,560,460 | 40.0% |
| POP_JUMP_IF_TRUE | 11,487,200 | 23.5% |
| RETURN_CONST | 10,527,520 | 21.6% |
| RETURN_VALUE | 6,939,080 | 14.2% |
| ENTER_EXECUTOR | 328,100 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,748,080 | 91.6% |
| JUMP_FORWARD | 4,092,320 | 8.4% |
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
| RETURN_VALUE | 24,772,160 | 34.1% |
| LOAD_FAST | 21,297,360 | 29.3% |
| LOAD_ATTR_INSTANCE_VALUE | 12,933,060 | 17.8% |
| POP_JUMP_IF_FALSE | 9,039,220 | 12.4% |
| UNARY_NOT | 3,720,000 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 24,772,160 | 34.1% |
| TO_BOOL_BOOL | 23,233,060 | 32.0% |
| STORE_FAST | 15,846,720 | 21.8% |
| POP_TOP | 6,939,080 | 9.6% |
| LOAD_FAST | 1,863,200 | 2.6% |


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
| TO_BOOL_BOOL | 15,207,160 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 11,487,200 | 75.5% |
| RETURN_VALUE | 3,720,000 | 24.5% |


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
| LOAD_ATTR_INSTANCE_VALUE | 28,600,200 | 59.5% |
| UNARY_NOT | 11,487,200 | 23.9% |
| LOAD_GLOBAL_MODULE | 5,206,840 | 10.8% |
| LOAD_FAST | 2,773,680 | 5.8% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 40,087,300 | 83.4% |
| LOAD_ATTR_INSTANCE_VALUE | 7,980,360 | 16.6% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 17,059,500 | 97.7% |
| STORE_SUBSCR_LIST_INT | 400,860 | 2.3% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 11,487,300 | 65.8% |
| POP_JUMP_IF_FALSE | 4,353,260 | 24.9% |
| RETURN_VALUE | 890,860 | 5.1% |
| FOR_ITER_RANGE | 372,240 | 2.1% |
| POP_TOP | 328,100 | 1.9% |


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
| POP_JUMP_IF_NONE | 340 | 34.0% |
| STORE_SUBSCR_LIST_INT | 320 | 32.0% |
| POP_TOP | 160 | 16.0% |
| EXTENDED_ARG | 160 | 16.0% |
| STORE_SUBSCR | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 440 | 44.0% |
| LOAD_GLOBAL_MODULE | 300 | 30.0% |
| EXTENDED_ARG | 160 | 16.0% |
| ENTER_EXECUTOR | 40 | 4.0% |
| FOR_ITER | 40 | 4.0% |


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
| STORE_ATTR_INSTANCE_VALUE | 15,387,440 | 29.2% |
| LOAD_ATTR_INSTANCE_VALUE | 12,351,780 | 23.5% |
| RESUME_CHECK | 10,660,440 | 20.3% |
| POP_JUMP_IF_FALSE | 6,834,880 | 13.0% |
| BINARY_OP | 2,398,580 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,192,800 | 55.5% |
| BINARY_OP_ADD_INT | 7,067,280 | 13.4% |
| STORE_FAST | 6,806,560 | 12.9% |
| BINARY_OP | 3,998,640 | 7.6% |
| COMPARE_OP_INT | 3,572,560 | 6.8% |


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
| RESUME_CHECK | 53,968,440 | 15.5% |
| POP_TOP | 44,748,080 | 12.8% |
| STORE_FAST | 42,916,240 | 12.3% |
| STORE_ATTR_INSTANCE_VALUE | 40,645,900 | 11.7% |
| POP_JUMP_IF_FALSE | 32,679,840 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 121,981,900 | 35.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 59,944,920 | 17.2% |
| STORE_ATTR_INSTANCE_VALUE | 44,128,800 | 12.7% |
| POP_JUMP_IF_NOT_NONE | 23,315,520 | 6.7% |
| POP_JUMP_IF_NONE | 22,455,200 | 6.4% |


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
| TO_BOOL_BOOL | 63,846,900 | 78.6% |
| COMPARE_OP_INT | 13,016,100 | 16.0% |
| ENTER_EXECUTOR | 4,353,260 | 5.4% |
| COMPARE_OP | 220 | 0.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,679,840 | 40.2% |
| POP_TOP | 19,560,460 | 24.1% |
| LOAD_GLOBAL_MODULE | 11,242,760 | 13.8% |
| RETURN_VALUE | 9,039,220 | 11.1% |
| LOAD_CONST | 6,834,880 | 8.4% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,455,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 17,059,500 | 76.0% |
| LOAD_FAST | 3,774,720 | 16.8% |
| LOAD_FAST_LOAD_FAST | 1,620,320 | 7.2% |
| JUMP_BACKWARD | 340 | 0.0% |
| RETURN_CONST | 160 | 0.0% |


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
| TO_BOOL_BOOL | 22,014,080 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,487,200 | 52.2% |
| LOAD_GLOBAL_BUILTIN | 10,526,240 | 47.8% |
| RETURN_VALUE | 580 | 0.0% |
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
| LOAD_ATTR_INSTANCE_VALUE | 24,749,900 | 37.7% |
| RETURN_VALUE | 15,846,720 | 24.1% |
| LOAD_FAST | 12,201,120 | 18.6% |
| LOAD_CONST | 6,806,560 | 10.4% |
| BINARY_SUBSCR_LIST_INT | 5,319,180 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,916,240 | 65.4% |
| LOAD_GLOBAL_BUILTIN | 10,526,240 | 16.0% |
| JUMP_FORWARD | 6,719,840 | 10.2% |
| LOAD_GLOBAL_MODULE | 3,720,400 | 5.7% |
| LOAD_CONST | 1,600,000 | 2.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 5,579,380 | 69.9% |
| BINARY_OP_SUBTRACT_INT | 1,599,980 | 20.0% |
| BINARY_OP | 801,200 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 7,980,360 | 100.0% |
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
| LOAD_CONST | 7,067,280 | 94.6% |
| LOAD_ATTR_INSTANCE_VALUE | 401,160 | 5.4% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 5,579,380 | 74.7% |
| LOAD_FAST | 1,487,980 | 19.9% |
| LOAD_CONST | 401,180 | 5.4% |


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
| LOAD_CONST | 2,001,120 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,599,980 | 80.0% |
| LOAD_FAST | 401,180 | 20.0% |


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
| LOAD_ATTR_METHOD_WITH_VALUES | 41,470,820 | 50.5% |
| LOAD_ATTR_INSTANCE_VALUE | 17,463,800 | 21.3% |
| LOAD_FAST_LOAD_FAST | 14,245,680 | 17.4% |
| LOAD_FAST | 7,179,920 | 8.7% |
| LOAD_GLOBAL_MODULE | 1,599,880 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 71,434,600 | 87.0% |
| COPY_FREE_VARS | 10,526,380 | 12.8% |
| CALL_PY_EXACT_ARGS | 132,260 | 0.2% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,482,120 | 42.1% |
| LOAD_ATTR_INSTANCE_VALUE | 3,961,200 | 30.4% |
| LOAD_CONST | 3,572,560 | 27.4% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 13,016,100 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 372,360 | 50.0% |
| ENTER_EXECUTOR | 372,240 | 49.9% |
| JUMP_BACKWARD | 440 | 0.1% |
| EXTENDED_ARG | 280 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 372,820 | 50.0% |
| LOAD_FAST | 372,400 | 50.0% |
| RETURN_CONST | 160 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 121,981,900 | 83.1% |
| LOAD_FAST_LOAD_FAST | 10,526,360 | 7.2% |
| COPY | 7,980,360 | 5.4% |
| LOAD_GLOBAL_MODULE | 5,321,360 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 967,400 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 28,600,200 | 19.5% |
| STORE_FAST | 24,749,900 | 16.9% |
| LOAD_FAST | 20,470,740 | 13.9% |
| CALL_PY_EXACT_ARGS | 17,463,800 | 11.9% |
| TO_BOOL_BOOL | 15,207,120 | 10.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 59,944,920 | 83.2% |
| ENTER_EXECUTOR | 11,487,300 | 15.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 606,120 | 0.8% |
| RETURN_VALUE | 720 | 0.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 41,470,820 | 57.6% |
| LOAD_FAST_LOAD_FAST | 14,245,720 | 19.8% |
| LOAD_FAST | 14,116,900 | 19.6% |
| LOAD_GLOBAL_MODULE | 1,599,760 | 2.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 606,120 | 0.8% |


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
| LOAD_FAST | 13,778,720 | 33.4% |
| POP_JUMP_IF_FALSE | 11,242,760 | 27.2% |
| RESUME_CHECK | 6,807,840 | 16.5% |
| STORE_FAST | 3,720,400 | 9.0% |
| LOAD_ATTR_INSTANCE_VALUE | 2,232,560 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 12,014,120 | 29.1% |
| CALL_ISINSTANCE | 10,526,240 | 25.5% |
| COMPARE_OP_INT | 5,482,120 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 5,321,360 | 12.9% |
| COPY | 5,206,840 | 12.6% |


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
| CALL_PY_EXACT_ARGS | 71,434,600 | 87.2% |
| COPY_FREE_VARS | 10,527,260 | 12.8% |
| CALL_ALLOC_AND_ENTER_INIT | 2,800 | 0.0% |
| CACHE | 420 | 0.0% |
| CALL | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,968,440 | 65.8% |
| LOAD_CONST | 10,660,440 | 13.0% |
| LOAD_FAST_LOAD_FAST | 10,527,640 | 12.8% |
| LOAD_GLOBAL_MODULE | 6,807,840 | 8.3% |
| LOAD_GLOBAL_BUILTIN | 920 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,128,800 | 63.8% |
| LOAD_FAST_LOAD_FAST | 16,746,520 | 24.2% |
| SWAP | 7,980,360 | 11.5% |
| STORE_ATTR_INSTANCE_VALUE | 295,420 | 0.4% |
| STORE_ATTR | 1,360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,645,900 | 58.8% |
| LOAD_CONST | 15,387,440 | 22.3% |
| RETURN_CONST | 10,530,200 | 15.2% |
| LOAD_GLOBAL_MODULE | 1,916,820 | 2.8% |
| LOAD_FAST_LOAD_FAST | 377,780 | 0.5% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 402,080 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 400,860 | 99.7% |
| LOAD_CONST | 940 | 0.2% |
| JUMP_BACKWARD | 320 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 40,087,300 | 39.7% |
| RETURN_VALUE | 23,233,060 | 23.0% |
| LOAD_ATTR_INSTANCE_VALUE | 15,207,120 | 15.0% |
| LOAD_GLOBAL_MODULE | 12,014,120 | 11.9% |
| CALL_ISINSTANCE | 10,526,240 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 63,846,900 | 63.2% |
| POP_JUMP_IF_TRUE | 22,014,080 | 21.8% |
| UNARY_NOT | 15,207,160 | 15.0% |


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
|     deferred | 6,879,900 | 7.0% |
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
|          hit | 745,380 | 100.0% |

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
|     deferred | 81,835,940 | 34.2% |
|          hit | 155,646,140 | 65.1% |
|         miss | 83,407,620 | 34.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,575,360 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,840 | 0.0% |
|          hit | 62,359,600 | 100.0% |

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
|     deferred | 15,375,860 | 21.9% |
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
| Basic | 762,978,260 | 48.0% |
| Not specialized | 160,460,140 | 10.1% |
| Specialized hits | 560,870,340 | 35.3% |
| Specialized misses | 106,086,000 | 6.7% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 81,835,940 | 75.7% |
| STORE_ATTR | 15,375,860 | 14.2% |
| CALL | 6,879,900 | 6.4% |
| BINARY_OP | 3,999,840 | 3.7% |
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
| LOAD_ATTR_INSTANCE_VALUE | 51,279,840 | 48.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 32,127,780 | 30.3% |
| STORE_ATTR_INSTANCE_VALUE | 15,668,120 | 14.8% |
| CALL_PY_EXACT_ARGS | 7,010,240 | 6.6% |
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
| Frames pushed | 87,542,120 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 2,620 | 0.0% |
| Frees to freelist | 2,300 |  |
| Allocations | 9,450,840 | 100.0% |
| Allocations to 512 bytes | 9,450,800 | 100.0% |
| Allocations to 4 kbytes | 40 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 9,445,170 |  |
| New values | 520 |  |
| Interpreter increfs | 640,038,540 | 81.0% |
| Interpreter decrefs | 735,480,500 | 92.0% |
| Increfs | 149,731,993 | 19.0% |
| Decrefs | 63,731,365 | 8.0% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 93,121,288 |  |
| Method cache misses | 5,962,972 |  |
| Method cache collisions | 5,962,268 |  |
| Method cache dunder hits | 834 |  |
| Method cache dunder misses | 206 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 145,920 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 40 |  |
| Traces created | 40 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 20 | 50.0% |
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
| <= 64 | 20 | 50.0% |
| <= 128 | 20 | 50.0% |


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
| <= 64 | 40 | 100.0% |


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
