
# Pystats results

- benchmark: richards
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 741,180,480 | 22.5% | 22.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 323,334,640 | 9.8% | 32.3% | 38.7% |
| TO_BOOL_BOOL | 274,862,740 | 8.3% | 40.6% |  |
| POP_JUMP_IF_FALSE | 208,167,600 | 6.3% | 46.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 155,455,760 | 4.7% | 51.6% | 48.9% |
| CALL_PY_EXACT_ARGS | 154,286,660 | 4.7% | 56.3% | 9.1% |
| RESUME_CHECK | 154,031,020 | 4.7% | 61.0% | 0.0% |
| RETURN_VALUE | 154,028,680 | 4.7% | 65.7% |  |
| STORE_FAST | 133,579,600 | 4.1% | 69.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 119,225,200 | 3.6% | 73.3% | 14.5% |
| LOAD_GLOBAL_MODULE | 118,917,880 | 3.6% | 76.9% |  |
| COPY | 118,888,160 | 3.6% | 80.5% |  |
| LOAD_CONST | 111,925,520 | 3.4% | 83.9% |  |
| POP_TOP | 86,002,960 | 2.6% | 86.5% |  |
| POP_JUMP_IF_NOT_NONE | 61,509,760 | 1.9% | 88.4% |  |
| POP_JUMP_IF_TRUE | 55,180,480 | 1.7% | 90.1% |  |
| POP_JUMP_IF_NONE | 44,918,080 | 1.4% | 91.4% |  |
| LOAD_FAST_LOAD_FAST | 40,939,840 | 1.2% | 92.7% |  |
| UNARY_NOT | 39,780,960 | 1.2% | 93.9% |  |
| JUMP_BACKWARD | 37,106,560 | 1.1% | 95.0% |  |
| COMPARE_OP_INT | 28,265,780 | 0.9% | 95.9% |  |
| JUMP_FORWARD | 21,632,000 | 0.7% | 96.5% |  |
| LOAD_GLOBAL_BUILTIN | 21,053,080 | 0.6% | 97.2% |  |
| CALL_ISINSTANCE | 21,052,720 | 0.6% | 97.8% |  |
| BINARY_OP_ADD_INT | 19,346,780 | 0.6% | 98.4% |  |
| SWAP | 18,194,560 | 0.6% | 98.9% |  |
| BINARY_SUBSCR_LIST_INT | 13,614,360 | 0.4% | 99.3% |  |
| BINARY_OP | 8,002,520 | 0.2% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 6,178,520 | 0.2% | 99.8% |  |
| FOR_ITER_RANGE | 3,724,180 | 0.1% | 99.9% |  |
| STORE_SUBSCR_LIST_INT | 2,980,440 | 0.1% | 100.0% |  |
| GET_ITER | 745,040 | 0.0% | 100.0% |  |
| RETURN_CONST | 10,880 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 7,800 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 7,800 | 0.0% | 100.0% |  |
| LOAD_ATTR | 5,880 | 0.0% | 100.0% |  |
| STORE_ATTR | 4,560 | 0.0% | 100.0% |  |
| CALL | 3,560 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,520 | 0.0% | 100.0% |  |
| BUILD_LIST | 2,560 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 960 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 840 | 0.0% | 100.0% |  |
| RESUME | 740 | 0.0% | 100.0% | 2.7% |
| PUSH_NULL | 640 | 0.0% | 100.0% |  |
| TO_BOOL | 600 | 0.0% | 100.0% |  |
| COMPARE_OP | 440 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 360 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| FOR_ITER | 120 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 80 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 271,081,480 | 8.2% | 8.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 179,901,440 | 5.5% | 13.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 154,022,180 | 4.7% | 18.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 154,017,720 | 4.7% | 23.0% |
| RESUME_CHECK LOAD_FAST | 119,089,300 | 3.6% | 26.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 103,212,160 | 3.1% | 29.8% |
| COPY TO_BOOL_BOOL | 100,693,440 | 3.1% | 32.8% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 94,094,560 | 2.9% | 35.7% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 88,258,800 | 2.7% | 38.3% |
| STORE_FAST LOAD_FAST | 88,065,600 | 2.7% | 41.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 83,526,620 | 2.5% | 43.5% |
| POP_TOP LOAD_FAST | 77,813,760 | 2.4% | 45.9% |
| LOAD_ATTR_INSTANCE_VALUE COPY | 68,352,580 | 2.1% | 48.0% |
| LOAD_CONST LOAD_FAST | 58,383,680 | 1.8% | 49.7% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 58,155,080 | 1.8% | 51.5% |
| RETURN_VALUE TO_BOOL_BOOL | 55,180,400 | 1.7% | 53.2% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 55,180,380 | 1.7% | 54.8% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 50,838,080 | 1.5% | 56.4% |
| RETURN_VALUE RETURN_VALUE | 49,544,320 | 1.5% | 57.9% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 49,507,660 | 1.5% | 59.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 46,631,040 | 1.4% | 60.8% |
| LOAD_FAST POP_JUMP_IF_NONE | 44,918,080 | 1.4% | 62.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 43,117,860 | 1.3% | 63.5% |
| LOAD_FAST RETURN_VALUE | 42,594,640 | 1.3% | 64.8% |
| POP_JUMP_IF_FALSE POP_TOP | 39,780,960 | 1.2% | 66.0% |
| TO_BOOL_BOOL UNARY_NOT | 39,780,920 | 1.2% | 67.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 39,780,880 | 1.2% | 68.4% |
| LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS | 34,927,800 | 1.1% | 69.4% |
| POP_JUMP_IF_NONE JUMP_BACKWARD | 34,127,360 | 1.0% | 70.5% |
| JUMP_BACKWARD LOAD_GLOBAL_MODULE | 34,127,340 | 1.0% | 71.5% |
| UNARY_NOT COPY | 32,340,960 | 1.0% | 72.5% |
| POP_JUMP_IF_TRUE POP_TOP | 32,340,960 | 1.0% | 73.5% |
| RETURN_VALUE STORE_FAST | 31,693,600 | 1.0% | 74.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 30,775,280 | 0.9% | 75.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 29,170,660 | 0.9% | 76.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 28,491,480 | 0.9% | 77.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 28,265,780 | 0.9% | 78.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 28,234,020 | 0.9% | 78.8% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 27,558,080 | 0.8% | 79.7% |
| POP_JUMP_IF_FALSE RETURN_VALUE | 26,784,960 | 0.8% | 80.5% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 25,870,100 | 0.8% | 81.3% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 24,661,880 | 0.7% | 82.0% |
| LOAD_FAST STORE_FAST | 24,402,240 | 0.7% | 82.8% |
| RESUME_CHECK LOAD_CONST | 21,321,080 | 0.6% | 83.4% |
| JUMP_FORWARD LOAD_FAST | 21,259,520 | 0.6% | 84.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 21,053,080 | 0.6% | 84.7% |
| POP_JUMP_IF_TRUE LOAD_FAST | 21,052,800 | 0.6% | 85.3% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 21,052,760 | 0.6% | 86.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 21,052,640 | 0.6% | 86.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 21,052,640 | 0.6% | 87.2% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 21,052,640 | 0.6% | 87.9% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 18,194,360 | 0.6% | 88.4% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 18,194,360 | 0.6% | 89.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 16,368,160 | 0.5% | 89.5% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 14,878,680 | 0.5% | 89.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 14,358,760 | 0.4% | 90.4% |
| RETURN_VALUE POP_TOP | 13,878,280 | 0.4% | 90.8% |
| POP_JUMP_IF_FALSE LOAD_CONST | 13,727,040 | 0.4% | 91.2% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 13,617,600 | 0.4% | 91.6% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 13,614,320 | 0.4% | 92.0% |
| LOAD_CONST STORE_FAST | 13,613,120 | 0.4% | 92.4% |
| STORE_FAST JUMP_FORWARD | 13,447,360 | 0.4% | 92.8% |
| BINARY_OP_ADD_INT SWAP | 13,392,260 | 0.4% | 93.2% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 12,441,600 | 0.4% | 93.6% |
| LOAD_GLOBAL_MODULE COMPARE_OP_INT | 10,964,360 | 0.3% | 94.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_INSTANCE_VALUE | 10,642,960 | 0.3% | 94.3% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 10,638,380 | 0.3% | 94.6% |
| LOAD_GLOBAL_MODULE COPY | 10,413,720 | 0.3% | 94.9% |
| LOAD_CONST COMPARE_OP_INT | 9,378,720 | 0.3% | 95.2% |
| POP_TOP JUMP_FORWARD | 8,184,640 | 0.2% | 95.5% |
| LOAD_CONST BINARY_OP | 7,997,040 | 0.2% | 95.7% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 7,922,480 | 0.2% | 95.9% |
| LOAD_FAST COPY | 7,780,800 | 0.2% | 96.2% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 7,697,600 | 0.2% | 96.4% |
| POP_JUMP_IF_NONE LOAD_FAST | 7,549,440 | 0.2% | 96.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 7,441,200 | 0.2% | 96.9% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 7,440,440 | 0.2% | 97.1% |
| UNARY_NOT RETURN_VALUE | 7,440,000 | 0.2% | 97.3% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 6,178,480 | 0.2% | 97.5% |
| BINARY_OP LOAD_CONST | 4,797,140 | 0.1% | 97.6% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 4,465,200 | 0.1% | 97.8% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 3,833,780 | 0.1% | 97.9% |
| RETURN_VALUE LOAD_FAST | 3,726,400 | 0.1% | 98.0% |
| POP_JUMP_IF_NONE LOAD_FAST_LOAD_FAST | 3,240,640 | 0.1% | 98.1% |
| STORE_FAST LOAD_CONST | 3,200,000 | 0.1% | 98.2% |
| BINARY_OP_SUBTRACT_INT SWAP | 3,199,980 | 0.1% | 98.3% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 3,199,880 | 0.1% | 98.4% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 3,199,600 | 0.1% | 98.5% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 2,980,400 | 0.1% | 98.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,980,340 | 0.1% | 98.7% |
| FOR_ITER_RANGE STORE_FAST | 2,979,140 | 0.1% | 98.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 2,978,840 | 0.1% | 98.9% |
| BINARY_OP_ADD_INT LOAD_CONST | 2,978,540 | 0.1% | 98.9% |
| BINARY_OP_SUBTRACT_INT LOAD_FAST | 2,978,540 | 0.1% | 99.0% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 2,978,540 | 0.1% | 99.1% |
| LOAD_ATTR_INSTANCE_VALUE BINARY_OP_ADD_INT | 2,978,520 | 0.1% | 99.2% |
| LOAD_FAST LOAD_CONST | 2,976,400 | 0.1% | 99.3% |
| BINARY_OP_ADD_INT LOAD_FAST | 2,975,980 | 0.1% | 99.4% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 2,975,980 | 0.1% | 99.5% |
| POP_JUMP_IF_NOT_NONE LOAD_CONST | 2,974,080 | 0.1% | 99.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 620 | 73.8% |
| RESUME | 220 | 26.2% |


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
| RETURN_CONST | 7,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,800 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 744,620 | 99.9% |
| CALL_BUILTIN_CLASS | 300 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 744,680 | 100.0% |
| EXTENDED_ARG | 320 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 840 | 100.0% |


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
| POP_JUMP_IF_FALSE | 39,780,960 | 46.3% |
| POP_JUMP_IF_TRUE | 32,340,960 | 37.6% |
| RETURN_VALUE | 13,878,280 | 16.1% |
| RETURN_CONST | 2,240 | 0.0% |
| CALL | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 77,813,760 | 90.5% |
| JUMP_FORWARD | 8,184,640 | 9.5% |
| RETURN_CONST | 1,920 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,680 | 0.0% |
| JUMP_BACKWARD | 320 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 75.0% |
| LOAD_DEREF | 80 | 12.5% |
| LOAD_ATTR_MODULE | 60 | 9.4% |
| LOAD_ATTR | 20 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 560 | 87.5% |
| LOAD_FAST | 80 | 12.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 49,544,320 | 32.2% |
| LOAD_FAST | 42,594,640 | 27.7% |
| POP_JUMP_IF_FALSE | 26,784,960 | 17.4% |
| LOAD_ATTR_INSTANCE_VALUE | 25,870,100 | 16.8% |
| UNARY_NOT | 7,440,000 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 55,180,400 | 35.8% |
| RETURN_VALUE | 49,544,320 | 32.2% |
| STORE_FAST | 31,693,600 | 20.6% |
| POP_TOP | 13,878,280 | 9.0% |
| LOAD_FAST | 3,726,400 | 2.4% |


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
| RETURN_CONST | 20 | 25.0% |


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
| TO_BOOL_BOOL | 39,780,920 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 32,340,960 | 81.3% |
| RETURN_VALUE | 7,440,000 | 18.7% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,997,040 | 99.9% |
| BINARY_OP | 2,840 | 0.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 0.0% |
| LOAD_FAST | 40 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,797,140 | 59.9% |
| SWAP | 1,602,320 | 20.0% |
| LOAD_FAST | 1,600,040 | 20.0% |
| BINARY_OP | 2,840 | 0.0% |
| BINARY_OP_ADD_INT | 100 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,520 | 98.4% |
| LOAD_GLOBAL | 40 | 1.6% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 15.7% |
| LOAD_GLOBAL | 540 | 15.2% |
| LOAD_GLOBAL_MODULE | 540 | 15.2% |
| LOAD_ATTR | 500 | 14.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 400 | 11.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 800 | 22.5% |
| POP_TOP | 520 | 14.6% |
| CALL_ALLOC_AND_ENTER_INIT | 520 | 14.6% |
| RESUME | 440 | 12.4% |
| RESUME_CHECK | 360 | 10.1% |


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
| LOAD_ATTR_INSTANCE_VALUE | 68,352,580 | 57.5% |
| UNARY_NOT | 32,340,960 | 27.2% |
| LOAD_GLOBAL_MODULE | 10,413,720 | 8.8% |
| LOAD_FAST | 7,780,800 | 6.5% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 100,693,440 | 84.7% |
| LOAD_ATTR_INSTANCE_VALUE | 18,194,360 | 15.3% |
| LOAD_ATTR | 200 | 0.0% |
| TO_BOOL | 160 | 0.0% |


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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 320 | 33.3% |
| JUMP_BACKWARD | 320 | 33.3% |
| POP_JUMP_IF_FALSE | 320 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 600 | 62.5% |
| JUMP_BACKWARD | 320 | 33.3% |
| FOR_ITER | 40 | 4.2% |


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
| POP_JUMP_IF_NONE | 34,127,360 | 92.0% |
| STORE_SUBSCR_LIST_INT | 2,978,540 | 8.0% |
| POP_TOP | 320 | 0.0% |
| EXTENDED_ARG | 320 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 34,127,340 | 92.0% |
| FOR_ITER_RANGE | 2,978,840 | 8.0% |
| EXTENDED_ARG | 320 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,447,360 | 62.2% |
| POP_TOP | 8,184,640 | 37.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,259,520 | 98.3% |
| LOAD_FAST_LOAD_FAST | 372,480 | 1.7% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 49.0% |
| LOAD_GLOBAL_MODULE | 2,000 | 34.0% |
| LOAD_ATTR | 280 | 4.8% |
| LOAD_GLOBAL | 240 | 4.1% |
| COPY | 200 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,960 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,100 | 18.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 700 | 11.9% |
| CALL | 500 | 8.5% |
| LOAD_FAST | 440 | 7.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 30,775,280 | 27.5% |
| LOAD_ATTR_INSTANCE_VALUE | 29,170,660 | 26.1% |
| RESUME_CHECK | 21,321,080 | 19.0% |
| POP_JUMP_IF_FALSE | 13,727,040 | 12.3% |
| BINARY_OP | 4,797,140 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,383,680 | 52.2% |
| BINARY_OP_ADD_INT | 16,368,160 | 14.6% |
| STORE_FAST | 13,613,120 | 12.2% |
| COMPARE_OP_INT | 9,378,720 | 8.4% |
| BINARY_OP | 7,997,040 | 7.1% |


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
| RESUME_CHECK | 119,089,300 | 16.1% |
| POP_JUMP_IF_FALSE | 103,212,160 | 13.9% |
| STORE_FAST | 88,065,600 | 11.9% |
| STORE_ATTR_INSTANCE_VALUE | 83,526,620 | 11.3% |
| POP_TOP | 77,813,760 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 271,081,480 | 36.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 154,017,720 | 20.8% |
| STORE_ATTR_INSTANCE_VALUE | 88,258,800 | 11.9% |
| POP_JUMP_IF_NOT_NONE | 46,631,040 | 6.3% |
| POP_JUMP_IF_NONE | 44,918,080 | 6.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 28,491,480 | 69.6% |
| POP_JUMP_IF_NOT_NONE | 7,697,600 | 18.8% |
| POP_JUMP_IF_NONE | 3,240,640 | 7.9% |
| STORE_ATTR_INSTANCE_VALUE | 756,500 | 1.8% |
| JUMP_FORWARD | 372,480 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 21,052,760 | 51.4% |
| STORE_ATTR_INSTANCE_VALUE | 12,441,600 | 30.4% |
| CALL_PY_EXACT_ARGS | 7,440,440 | 18.2% |
| LOAD_FAST_LOAD_FAST | 3,200 | 0.0% |
| STORE_ATTR | 1,280 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 18.2% |
| STORE_FAST | 560 | 15.9% |
| RETURN_VALUE | 280 | 8.0% |
| LOAD_CONST | 280 | 8.0% |
| POP_TOP | 240 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,640 | 46.6% |
| CALL | 540 | 15.3% |
| LOAD_FAST | 260 | 7.4% |
| LOAD_ATTR | 240 | 6.8% |
| LOAD_GLOBAL | 240 | 6.8% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 179,901,440 | 86.4% |
| COMPARE_OP_INT | 28,265,780 | 13.6% |
| COMPARE_OP | 220 | 0.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 103,212,160 | 49.6% |
| POP_TOP | 39,780,960 | 19.1% |
| RETURN_VALUE | 26,784,960 | 12.9% |
| LOAD_GLOBAL_MODULE | 24,661,880 | 11.8% |
| LOAD_CONST | 13,727,040 | 6.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,918,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 34,127,360 | 76.0% |
| LOAD_FAST | 7,549,440 | 16.8% |
| LOAD_FAST_LOAD_FAST | 3,240,640 | 7.2% |
| RETURN_CONST | 320 | 0.0% |
| LOAD_GLOBAL_MODULE | 300 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,631,040 | 75.8% |
| LOAD_ATTR_INSTANCE_VALUE | 14,878,680 | 24.2% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,838,080 | 82.7% |
| LOAD_FAST_LOAD_FAST | 7,697,600 | 12.5% |
| LOAD_CONST | 2,974,080 | 4.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 55,180,380 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 32,340,960 | 58.6% |
| LOAD_FAST | 21,052,800 | 38.2% |
| RETURN_VALUE | 1,786,720 | 3.2% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 6,280 | 57.7% |
| POP_TOP | 1,920 | 17.6% |
| STORE_SUBSCR_LIST_INT | 1,900 | 17.5% |
| POP_JUMP_IF_NONE | 320 | 2.9% |
| FOR_ITER_RANGE | 320 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXIT_INIT_CHECK | 7,800 | 71.7% |
| POP_TOP | 2,240 | 20.6% |
| INTERPRETER_EXIT | 840 | 7.7% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,640 | 57.9% |
| LOAD_FAST_LOAD_FAST | 1,280 | 28.1% |
| STORE_ATTR | 320 | 7.0% |
| SWAP | 200 | 4.4% |
| LOAD_GLOBAL | 60 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,380 | 30.3% |
| STORE_ATTR_INSTANCE_VALUE | 1,320 | 28.9% |
| LOAD_FAST_LOAD_FAST | 940 | 20.6% |
| LOAD_CONST | 400 | 8.8% |
| STORE_ATTR | 320 | 7.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 49,507,660 | 37.1% |
| RETURN_VALUE | 31,693,600 | 23.7% |
| LOAD_FAST | 24,402,240 | 18.3% |
| LOAD_CONST | 13,613,120 | 10.2% |
| BINARY_SUBSCR_LIST_INT | 10,638,380 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,065,600 | 65.9% |
| LOAD_GLOBAL_BUILTIN | 21,052,640 | 15.8% |
| JUMP_FORWARD | 13,447,360 | 10.1% |
| LOAD_GLOBAL_MODULE | 7,441,200 | 5.6% |
| LOAD_CONST | 3,200,000 | 2.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 13,392,260 | 73.6% |
| BINARY_OP_SUBTRACT_INT | 3,199,980 | 17.6% |
| BINARY_OP | 1,602,320 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 18,194,360 | 100.0% |
| STORE_ATTR | 200 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 440 | 59.5% |
| CACHE | 220 | 29.7% |
| CALL_PY_EXACT_ARGS | 60 | 8.1% |
| COPY_FREE_VARS | 20 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 40.5% |
| LOAD_GLOBAL | 220 | 29.7% |
| LOAD_CONST | 200 | 27.0% |
| LOAD_FAST_LOAD_FAST | 20 | 2.7% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,368,160 | 84.6% |
| LOAD_ATTR_INSTANCE_VALUE | 2,978,520 | 15.4% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 13,392,260 | 69.2% |
| LOAD_CONST | 2,978,540 | 15.4% |
| LOAD_FAST | 2,975,980 | 15.4% |


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
| LOAD_CONST | 6,178,480 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,199,980 | 51.8% |
| LOAD_FAST | 2,978,540 | 48.2% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,614,320 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,638,380 | 78.1% |
| LOAD_FAST | 2,975,980 | 21.9% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,600 | 71.8% |
| RETURN_VALUE | 1,680 | 21.5% |
| CALL | 520 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,800 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320 | 88.9% |
| CALL | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 300 | 83.3% |
| STORE_FAST | 60 | 16.7% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 21,052,640 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 21,052,640 | 100.0% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 94,094,560 | 61.0% |
| LOAD_ATTR_INSTANCE_VALUE | 34,927,800 | 22.6% |
| LOAD_FAST | 14,358,760 | 9.3% |
| LOAD_FAST_LOAD_FAST | 7,440,440 | 4.8% |
| LOAD_GLOBAL_MODULE | 3,199,880 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 154,022,180 | 99.8% |
| CALL_PY_EXACT_ARGS | 264,420 | 0.2% |
| RESUME | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,964,360 | 38.8% |
| LOAD_CONST | 9,378,720 | 33.2% |
| LOAD_ATTR_INSTANCE_VALUE | 7,922,480 | 28.0% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 28,265,780 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,978,840 | 80.0% |
| GET_ITER | 744,680 | 20.0% |
| EXTENDED_ARG | 600 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,979,140 | 80.0% |
| LOAD_FAST | 744,720 | 20.0% |
| RETURN_CONST | 320 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 271,081,480 | 83.8% |
| LOAD_FAST_LOAD_FAST | 21,052,760 | 6.5% |
| COPY | 18,194,360 | 5.6% |
| LOAD_GLOBAL_MODULE | 10,642,960 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,361,980 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 68,352,580 | 21.1% |
| STORE_FAST | 49,507,660 | 15.3% |
| LOAD_FAST | 43,117,860 | 13.3% |
| TO_BOOL_BOOL | 39,780,880 | 12.3% |
| CALL_PY_EXACT_ARGS | 34,927,800 | 10.8% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 154,017,720 | 99.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,435,660 | 0.9% |
| RETURN_VALUE | 1,680 | 0.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 94,094,560 | 60.5% |
| LOAD_FAST_LOAD_FAST | 28,491,480 | 18.3% |
| LOAD_FAST | 28,234,020 | 18.2% |
| LOAD_GLOBAL_MODULE | 3,199,600 | 2.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,435,660 | 0.9% |


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
| STORE_FAST | 21,052,640 | 100.0% |
| RESUME_CHECK | 280 | 0.0% |
| LOAD_GLOBAL | 120 | 0.0% |
| POP_JUMP_IF_FALSE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,053,080 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 34,127,340 | 28.7% |
| LOAD_FAST | 27,558,080 | 23.2% |
| POP_JUMP_IF_FALSE | 24,661,880 | 20.7% |
| RESUME_CHECK | 13,617,600 | 11.5% |
| STORE_FAST | 7,441,200 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 58,155,080 | 48.9% |
| CALL_ISINSTANCE | 21,052,640 | 17.7% |
| COMPARE_OP_INT | 10,964,360 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 10,642,960 | 8.9% |
| COPY | 10,413,720 | 8.8% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 154,022,180 | 100.0% |
| CALL_ALLOC_AND_ENTER_INIT | 7,800 | 0.0% |
| CACHE | 620 | 0.0% |
| CALL | 360 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 119,089,300 | 77.3% |
| LOAD_CONST | 21,321,080 | 13.8% |
| LOAD_GLOBAL_MODULE | 13,617,600 | 8.8% |
| LOAD_FAST_LOAD_FAST | 2,540 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 280 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,258,800 | 74.0% |
| SWAP | 18,194,360 | 15.3% |
| LOAD_FAST_LOAD_FAST | 12,441,600 | 10.4% |
| STORE_ATTR_INSTANCE_VALUE | 326,680 | 0.3% |
| LOAD_GLOBAL_MODULE | 2,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,526,620 | 70.1% |
| LOAD_CONST | 30,775,280 | 25.8% |
| LOAD_GLOBAL_MODULE | 3,833,780 | 3.2% |
| LOAD_FAST_LOAD_FAST | 756,500 | 0.6% |
| STORE_ATTR_INSTANCE_VALUE | 326,680 | 0.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980,400 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,978,540 | 99.9% |
| RETURN_CONST | 1,900 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 100,693,440 | 36.6% |
| LOAD_GLOBAL_MODULE | 58,155,080 | 21.2% |
| RETURN_VALUE | 55,180,400 | 20.1% |
| LOAD_ATTR_INSTANCE_VALUE | 39,780,880 | 14.5% |
| CALL_ISINSTANCE | 21,052,640 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 179,901,440 | 65.5% |
| POP_JUMP_IF_TRUE | 55,180,380 | 20.1% |
| UNARY_NOT | 39,780,920 | 14.5% |


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
|     deferred | 7,999,520 | 23.9% |
|          hit | 25,525,360 | 76.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 5.3% |
| Failure | 2,840 | 94.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 1,160 | 40.8% |
| and int | 980 | 34.5% |
| xor | 580 | 20.4% |
| multiply different types | 120 | 4.2% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 13,614,360 | 100.0% |

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
|     deferred | 368,934,881,474,190,769,900 | 210,397,814,142,135.8% |
|          hit | 161,332,820 | 92.0% |
|         miss | 14,014,720 | 8.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 265,860 | 100.0% |
| Failure | 120 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 60 | 50.0% |
| cfunc noargs | 60 | 50.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 220 | 0.0% |
|          hit | 28,265,780 | 100.0% |

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
|          hit | 3,724,180 | 100.0% |

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
|     deferred | 368,934,881,474,187,238,440 | 77,054,648,170,743.8% |
|          hit | 277,506,040 | 58.0% |
|         miss | 201,284,480 | 42.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,799,480 | 100.0% |
| Failure | 280 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 280 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,760 | 0.0% |
|          hit | 139,970,960 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,760 | 100.0% |
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
|     deferred | 368,934,881,474,190,708,560 | 309,431,874,621,059.9% |
|          hit | 101,905,780 | 85.5% |
|         miss | 17,319,420 | 14.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 328,000 | 99.9% |
| Failure | 320 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not in keys | 320 | 100.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 2,980,440 | 100.0% |

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
|          hit | 274,862,740 | 100.0% |

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
| Basic | 1,504,029,180 | 45.6% |
| Not specialized | 377,797,280 | 11.5% |
| Specialized hits | 1,183,719,460 | 35.9% |
| Specialized misses | 232,618,640 | 7.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 368,934,881,474,190,769,900 | 33.3% |
| STORE_ATTR | 368,934,881,474,190,708,560 | 33.3% |
| LOAD_ATTR | 368,934,881,474,187,238,440 | 33.3% |
| BINARY_OP | 7,999,520 | 0.0% |
| LOAD_GLOBAL | 1,760 | 0.0% |
| TO_BOOL | 300 | 0.0% |
| COMPARE_OP | 220 | 0.0% |
| FOR_ITER | 60 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 125,191,680 | 53.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 76,092,800 | 32.7% |
| STORE_ATTR_INSTANCE_VALUE | 17,319,420 | 7.4% |
| CALL_PY_EXACT_ARGS | 14,014,720 | 6.0% |
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
| Calls to PyEval_EvalDefault | 840 | 0.0% |
| Calls to Python functions inlined | 154,030,920 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 840 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 840 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 840 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 140,287,540 | 91.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 3,900 | 0.0% |
| Frees to freelist | 3,580 |  |
| Allocations | 18,901,520 | 100.0% |
| Allocations to 512 bytes | 18,901,520 | 100.0% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 18,886,755 |  |
| New values | 520 |  |
| Interpreter increfs | 1,182,549,840 | 89.9% |
| Interpreter decrefs | 1,307,605,520 | 98.1% |
| Increfs | 132,137,943 | 10.1% |
| Decrefs | 25,959,260 | 1.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 213,956,557 |  |
| Method cache misses | 4,655,543 |  |
| Method cache collisions | 4,654,766 |  |
| Method cache dunder hits | 4,935 |  |
| Method cache dunder misses | 225 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 144,400 |
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
