
# Pystats results

- benchmark: richards
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 675,546,980 | 23.1% | 23.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 293,577,680 | 10.0% | 33.1% | 34.9% |
| TO_BOOL_BOOL | 202,156,460 | 6.9% | 40.0% |  |
| POP_JUMP_IF_FALSE | 162,444,080 | 5.5% | 45.6% |  |
| RETURN_VALUE | 145,322,140 | 5.0% | 50.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 144,085,080 | 4.9% | 55.4% | 44.6% |
| CALL_PY_EXACT_ARGS | 143,139,560 | 4.9% | 60.3% | 9.8% |
| RESUME_CHECK | 142,883,920 | 4.9% | 65.2% | 0.0% |
| STORE_FAST | 131,345,920 | 4.5% | 69.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 116,991,520 | 4.0% | 73.7% | 14.8% |
| LOAD_CONST | 105,281,760 | 3.6% | 77.3% |  |
| COPY | 96,144,580 | 3.3% | 80.6% |  |
| LOAD_GLOBAL_MODULE | 82,614,440 | 2.8% | 83.4% |  |
| POP_TOP | 76,640,160 | 2.6% | 86.0% |  |
| POP_JUMP_IF_NOT_NONE | 61,509,760 | 2.1% | 88.1% |  |
| POP_JUMP_IF_NONE | 44,918,080 | 1.5% | 89.6% |  |
| POP_JUMP_IF_TRUE | 44,033,380 | 1.5% | 91.1% |  |
| LOAD_FAST_LOAD_FAST | 40,939,840 | 1.4% | 92.5% |  |
| ENTER_EXECUTOR | 34,928,880 | 1.2% | 93.7% |  |
| UNARY_NOT | 30,418,160 | 1.0% | 94.8% |  |
| COMPARE_OP_INT | 26,032,100 | 0.9% | 95.7% |  |
| JUMP_FORWARD | 21,632,000 | 0.7% | 96.4% |  |
| LOAD_GLOBAL_BUILTIN | 21,053,080 | 0.7% | 97.1% |  |
| CALL_ISINSTANCE | 21,052,720 | 0.7% | 97.8% |  |
| SWAP | 15,960,880 | 0.5% | 98.4% |  |
| BINARY_OP_ADD_INT | 14,936,700 | 0.5% | 98.9% |  |
| BINARY_SUBSCR_LIST_INT | 13,614,360 | 0.5% | 99.4% |  |
| BINARY_OP | 8,002,520 | 0.3% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 4,002,120 | 0.1% | 99.8% |  |
| NOP | 3,718,160 | 0.1% | 99.9% |  |
| FOR_ITER_RANGE | 1,490,500 | 0.1% | 99.9% |  |
| STORE_SUBSCR_LIST_INT | 804,040 | 0.0% | 100.0% |  |
| GET_ITER | 745,040 | 0.0% | 100.0% |  |
| RETURN_CONST | 10,880 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 7,800 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 7,800 | 0.0% | 100.0% |  |
| LOAD_ATTR | 5,880 | 0.0% | 100.0% |  |
| STORE_ATTR | 4,560 | 0.0% | 100.0% |  |
| CALL | 3,560 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,520 | 0.0% | 100.0% |  |
| BUILD_LIST | 2,560 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,320 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 243,985,100 | 8.3% | 8.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 142,875,080 | 4.9% | 13.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 127,705,060 | 4.4% | 17.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 119,890,680 | 4.1% | 21.7% |
| RESUME_CHECK LOAD_FAST | 107,942,200 | 3.7% | 25.4% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 88,258,800 | 3.0% | 28.4% |
| STORE_FAST LOAD_FAST | 85,831,920 | 2.9% | 31.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 82,947,460 | 2.8% | 34.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 81,292,940 | 2.8% | 36.9% |
| COPY TO_BOOL_BOOL | 80,183,540 | 2.7% | 39.6% |
| POP_TOP LOAD_FAST | 68,450,960 | 2.3% | 42.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 65,367,040 | 2.2% | 44.2% |
| LOAD_CONST LOAD_FAST | 58,383,680 | 2.0% | 46.2% |
| LOAD_ATTR_INSTANCE_VALUE COPY | 57,205,480 | 2.0% | 48.2% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 50,838,080 | 1.7% | 49.9% |
| RETURN_VALUE RETURN_VALUE | 49,544,320 | 1.7% | 51.6% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 49,507,660 | 1.7% | 53.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 46,631,040 | 1.6% | 54.9% |
| RETURN_VALUE TO_BOOL_BOOL | 46,473,860 | 1.6% | 56.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 44,918,080 | 1.5% | 58.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 44,033,280 | 1.5% | 59.5% |
| LOAD_FAST RETURN_VALUE | 42,594,640 | 1.5% | 61.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 40,941,460 | 1.4% | 62.4% |
| POP_JUMP_IF_FALSE POP_TOP | 39,124,700 | 1.3% | 63.7% |
| LOAD_ATTR_INSTANCE_VALUE CALL_PY_EXACT_ARGS | 34,927,800 | 1.2% | 64.9% |
| POP_JUMP_IF_NONE ENTER_EXECUTOR | 34,127,020 | 1.2% | 66.1% |
| RETURN_VALUE STORE_FAST | 31,693,600 | 1.1% | 67.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 30,775,280 | 1.1% | 68.2% |
| TO_BOOL_BOOL UNARY_NOT | 30,418,120 | 1.0% | 69.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 30,418,080 | 1.0% | 70.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 28,491,480 | 1.0% | 71.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 28,234,020 | 1.0% | 72.2% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 27,558,080 | 0.9% | 73.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 26,032,100 | 0.9% | 74.0% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 25,870,100 | 0.9% | 74.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_CONST | 24,703,300 | 0.8% | 75.8% |
| LOAD_FAST STORE_FAST | 24,402,240 | 0.8% | 76.6% |
| LOAD_GLOBAL_MODULE TO_BOOL_BOOL | 24,028,040 | 0.8% | 77.4% |
| ENTER_EXECUTOR LOAD_ATTR_METHOD_WITH_VALUES | 22,979,940 | 0.8% | 78.2% |
| UNARY_NOT COPY | 22,978,160 | 0.8% | 79.0% |
| POP_JUMP_IF_TRUE POP_TOP | 22,978,160 | 0.8% | 79.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 22,485,480 | 0.8% | 80.5% |
| RESUME_CHECK LOAD_CONST | 21,321,080 | 0.7% | 81.3% |
| JUMP_FORWARD LOAD_FAST | 21,259,520 | 0.7% | 82.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 21,053,080 | 0.7% | 82.7% |
| POP_JUMP_IF_TRUE LOAD_FAST | 21,052,800 | 0.7% | 83.4% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 21,052,760 | 0.7% | 84.1% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 21,052,640 | 0.7% | 84.9% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 21,052,640 | 0.7% | 85.6% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 21,052,640 | 0.7% | 86.3% |
| POP_JUMP_IF_FALSE RETURN_VALUE | 18,078,420 | 0.6% | 86.9% |
| COPY LOAD_ATTR_INSTANCE_VALUE | 15,960,680 | 0.5% | 87.5% |
| SWAP STORE_ATTR_INSTANCE_VALUE | 15,960,680 | 0.5% | 88.0% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 14,878,680 | 0.5% | 88.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 14,358,760 | 0.5% | 89.0% |
| LOAD_CONST BINARY_OP_ADD_INT | 14,134,480 | 0.5% | 89.5% |
| RETURN_VALUE POP_TOP | 13,878,280 | 0.5% | 90.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 13,669,760 | 0.5% | 90.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 13,617,600 | 0.5% | 90.9% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 13,614,320 | 0.5% | 91.4% |
| LOAD_CONST STORE_FAST | 13,613,120 | 0.5% | 91.8% |
| STORE_FAST JUMP_FORWARD | 13,447,360 | 0.5% | 92.3% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 12,441,600 | 0.4% | 92.7% |
| BINARY_OP_ADD_INT SWAP | 11,158,580 | 0.4% | 93.1% |
| LOAD_GLOBAL_MODULE COMPARE_OP_INT | 10,964,360 | 0.4% | 93.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_INSTANCE_VALUE | 10,642,960 | 0.4% | 93.8% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 10,638,380 | 0.4% | 94.2% |
| LOAD_GLOBAL_MODULE COPY | 10,413,720 | 0.4% | 94.5% |
| ENTER_EXECUTOR POP_JUMP_IF_FALSE | 8,706,540 | 0.3% | 94.8% |
| POP_TOP JUMP_FORWARD | 8,184,640 | 0.3% | 95.1% |
| LOAD_CONST BINARY_OP | 7,997,040 | 0.3% | 95.4% |
| LOAD_ATTR_INSTANCE_VALUE COMPARE_OP_INT | 7,922,480 | 0.3% | 95.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 7,697,600 | 0.3% | 95.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 7,549,440 | 0.3% | 96.2% |
| STORE_FAST LOAD_GLOBAL_MODULE | 7,441,200 | 0.3% | 96.4% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 7,440,440 | 0.3% | 96.7% |
| UNARY_NOT RETURN_VALUE | 7,440,000 | 0.3% | 97.0% |
| LOAD_CONST COMPARE_OP_INT | 7,145,040 | 0.2% | 97.2% |
| LOAD_FAST COPY | 5,547,120 | 0.2% | 97.4% |
| BINARY_OP LOAD_CONST | 4,797,140 | 0.2% | 97.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 4,465,200 | 0.2% | 97.7% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 4,002,080 | 0.1% | 97.8% |
| STORE_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 3,833,780 | 0.1% | 98.0% |
| RETURN_VALUE LOAD_FAST | 3,726,400 | 0.1% | 98.1% |
| NOP LOAD_FAST | 3,718,080 | 0.1% | 98.2% |
| POP_JUMP_IF_FALSE NOP | 3,718,080 | 0.1% | 98.4% |
| POP_JUMP_IF_NONE LOAD_FAST_LOAD_FAST | 3,240,640 | 0.1% | 98.5% |
| STORE_FAST LOAD_CONST | 3,200,000 | 0.1% | 98.6% |
| BINARY_OP_SUBTRACT_INT SWAP | 3,199,980 | 0.1% | 98.7% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 3,199,880 | 0.1% | 98.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_GLOBAL_MODULE | 3,199,600 | 0.1% | 98.9% |
| LOAD_FAST LOAD_CONST | 2,976,400 | 0.1% | 99.0% |
| BINARY_OP_ADD_INT LOAD_FAST | 2,975,980 | 0.1% | 99.1% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 2,975,980 | 0.1% | 99.2% |
| POP_JUMP_IF_NOT_NONE LOAD_CONST | 2,974,080 | 0.1% | 99.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_INSTANCE_VALUE | 1,935,080 | 0.1% | 99.4% |
| ENTER_EXECUTOR RETURN_VALUE | 1,784,300 | 0.1% | 99.4% |
| BINARY_OP SWAP | 1,602,320 | 0.1% | 99.5% |
| BINARY_OP LOAD_FAST | 1,600,040 | 0.1% | 99.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_ATTR_METHOD_WITH_VALUES | 1,212,080 | 0.0% | 99.6% |


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
| POP_JUMP_IF_FALSE | 3,718,080 | 100.0% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,718,080 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 39,124,700 | 51.0% |
| POP_JUMP_IF_TRUE | 22,978,160 | 30.0% |
| RETURN_VALUE | 13,878,280 | 18.1% |
| ENTER_EXECUTOR | 656,260 | 0.9% |
| RETURN_CONST | 2,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 68,450,960 | 89.3% |
| JUMP_FORWARD | 8,184,640 | 10.7% |
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
| RETURN_VALUE | 49,544,320 | 34.1% |
| LOAD_FAST | 42,594,640 | 29.3% |
| LOAD_ATTR_INSTANCE_VALUE | 25,870,100 | 17.8% |
| POP_JUMP_IF_FALSE | 18,078,420 | 12.4% |
| UNARY_NOT | 7,440,000 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 49,544,320 | 34.1% |
| TO_BOOL_BOOL | 46,473,860 | 32.0% |
| STORE_FAST | 31,693,600 | 21.8% |
| POP_TOP | 13,878,280 | 9.6% |
| LOAD_FAST | 3,726,400 | 2.6% |


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
| TO_BOOL_BOOL | 30,418,120 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 22,978,160 | 75.5% |
| RETURN_VALUE | 7,440,000 | 24.5% |


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
| LOAD_ATTR_INSTANCE_VALUE | 57,205,480 | 59.5% |
| UNARY_NOT | 22,978,160 | 23.9% |
| LOAD_GLOBAL_MODULE | 10,413,720 | 10.8% |
| LOAD_FAST | 5,547,120 | 5.8% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 80,183,540 | 83.4% |
| LOAD_ATTR_INSTANCE_VALUE | 15,960,680 | 16.6% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 34,127,020 | 97.7% |
| STORE_SUBSCR_LIST_INT | 801,820 | 2.3% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 22,979,940 | 65.8% |
| POP_JUMP_IF_FALSE | 8,706,540 | 24.9% |
| RETURN_VALUE | 1,784,300 | 5.1% |
| FOR_ITER_RANGE | 744,560 | 2.1% |
| POP_TOP | 656,260 | 1.9% |


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
| POP_JUMP_IF_NONE | 340 | 25.8% |
| POP_TOP | 320 | 24.2% |
| EXTENDED_ARG | 320 | 24.2% |
| STORE_SUBSCR_LIST_INT | 320 | 24.2% |
| STORE_SUBSCR | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 600 | 45.5% |
| EXTENDED_ARG | 320 | 24.2% |
| LOAD_GLOBAL_MODULE | 300 | 22.7% |
| ENTER_EXECUTOR | 40 | 3.0% |
| FOR_ITER | 40 | 3.0% |


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
| STORE_ATTR_INSTANCE_VALUE | 30,775,280 | 29.2% |
| LOAD_ATTR_INSTANCE_VALUE | 24,703,300 | 23.5% |
| RESUME_CHECK | 21,321,080 | 20.3% |
| POP_JUMP_IF_FALSE | 13,669,760 | 13.0% |
| BINARY_OP | 4,797,140 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,383,680 | 55.5% |
| BINARY_OP_ADD_INT | 14,134,480 | 13.4% |
| STORE_FAST | 13,613,120 | 12.9% |
| BINARY_OP | 7,997,040 | 7.6% |
| COMPARE_OP_INT | 7,145,040 | 6.8% |


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
| RESUME_CHECK | 107,942,200 | 16.0% |
| STORE_FAST | 85,831,920 | 12.7% |
| STORE_ATTR_INSTANCE_VALUE | 81,292,940 | 12.0% |
| POP_TOP | 68,450,960 | 10.1% |
| POP_JUMP_IF_FALSE | 65,367,040 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 243,985,100 | 36.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 119,890,680 | 17.7% |
| STORE_ATTR_INSTANCE_VALUE | 88,258,800 | 13.1% |
| POP_JUMP_IF_NOT_NONE | 46,631,040 | 6.9% |
| POP_JUMP_IF_NONE | 44,918,080 | 6.6% |


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
| TO_BOOL_BOOL | 127,705,060 | 78.6% |
| COMPARE_OP_INT | 26,032,100 | 16.0% |
| ENTER_EXECUTOR | 8,706,540 | 5.4% |
| COMPARE_OP | 220 | 0.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,367,040 | 40.2% |
| POP_TOP | 39,124,700 | 24.1% |
| LOAD_GLOBAL_MODULE | 22,485,480 | 13.8% |
| RETURN_VALUE | 18,078,420 | 11.1% |
| LOAD_CONST | 13,669,760 | 8.4% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,918,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 34,127,020 | 76.0% |
| LOAD_FAST | 7,549,440 | 16.8% |
| LOAD_FAST_LOAD_FAST | 3,240,640 | 7.2% |
| JUMP_BACKWARD | 340 | 0.0% |
| RETURN_CONST | 320 | 0.0% |


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
| TO_BOOL_BOOL | 44,033,280 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,978,160 | 52.2% |
| LOAD_FAST | 21,052,800 | 47.8% |
| RETURN_VALUE | 2,420 | 0.0% |


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
| LOAD_ATTR_INSTANCE_VALUE | 49,507,660 | 37.7% |
| RETURN_VALUE | 31,693,600 | 24.1% |
| LOAD_FAST | 24,402,240 | 18.6% |
| LOAD_CONST | 13,613,120 | 10.4% |
| BINARY_SUBSCR_LIST_INT | 10,638,380 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,831,920 | 65.3% |
| LOAD_GLOBAL_BUILTIN | 21,052,640 | 16.0% |
| JUMP_FORWARD | 13,447,360 | 10.2% |
| LOAD_GLOBAL_MODULE | 7,441,200 | 5.7% |
| LOAD_CONST | 3,200,000 | 2.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 11,158,580 | 69.9% |
| BINARY_OP_SUBTRACT_INT | 3,199,980 | 20.0% |
| BINARY_OP | 1,602,320 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 15,960,680 | 100.0% |
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
| LOAD_CONST | 14,134,480 | 94.6% |
| LOAD_ATTR_INSTANCE_VALUE | 802,120 | 5.4% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 11,158,580 | 74.7% |
| LOAD_FAST | 2,975,980 | 19.9% |
| LOAD_CONST | 802,140 | 5.4% |


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
| LOAD_CONST | 4,002,080 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,199,980 | 80.0% |
| LOAD_FAST | 802,140 | 20.0% |


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
| LOAD_ATTR_METHOD_WITH_VALUES | 82,947,460 | 57.9% |
| LOAD_ATTR_INSTANCE_VALUE | 34,927,800 | 24.4% |
| LOAD_FAST | 14,358,760 | 10.0% |
| LOAD_FAST_LOAD_FAST | 7,440,440 | 5.2% |
| LOAD_GLOBAL_MODULE | 3,199,880 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 142,875,080 | 99.8% |
| CALL_PY_EXACT_ARGS | 264,420 | 0.2% |
| RESUME | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,964,360 | 42.1% |
| LOAD_ATTR_INSTANCE_VALUE | 7,922,480 | 30.4% |
| LOAD_CONST | 7,145,040 | 27.4% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 26,032,100 | 100.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 744,680 | 50.0% |
| ENTER_EXECUTOR | 744,560 | 50.0% |
| EXTENDED_ARG | 600 | 0.0% |
| JUMP_BACKWARD | 600 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 745,460 | 50.0% |
| LOAD_FAST | 744,720 | 50.0% |
| RETURN_CONST | 320 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 243,985,100 | 83.1% |
| LOAD_FAST_LOAD_FAST | 21,052,760 | 7.2% |
| COPY | 15,960,680 | 5.4% |
| LOAD_GLOBAL_MODULE | 10,642,960 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,935,080 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 57,205,480 | 19.5% |
| STORE_FAST | 49,507,660 | 16.9% |
| LOAD_FAST | 40,941,460 | 13.9% |
| CALL_PY_EXACT_ARGS | 34,927,800 | 11.9% |
| TO_BOOL_BOOL | 30,418,080 | 10.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 119,890,680 | 83.2% |
| ENTER_EXECUTOR | 22,979,940 | 15.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,212,080 | 0.8% |
| RETURN_VALUE | 1,680 | 0.0% |
| LOAD_ATTR | 700 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 82,947,460 | 57.6% |
| LOAD_FAST_LOAD_FAST | 28,491,480 | 19.8% |
| LOAD_FAST | 28,234,020 | 19.6% |
| LOAD_GLOBAL_MODULE | 3,199,600 | 2.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,212,080 | 0.8% |


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
| LOAD_FAST | 27,558,080 | 33.4% |
| POP_JUMP_IF_FALSE | 22,485,480 | 27.2% |
| RESUME_CHECK | 13,617,600 | 16.5% |
| STORE_FAST | 7,441,200 | 9.0% |
| LOAD_ATTR_INSTANCE_VALUE | 4,465,200 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 24,028,040 | 29.1% |
| CALL_ISINSTANCE | 21,052,640 | 25.5% |
| COMPARE_OP_INT | 10,964,360 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 10,642,960 | 12.9% |
| COPY | 10,413,720 | 12.6% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 142,875,080 | 100.0% |
| CALL_ALLOC_AND_ENTER_INIT | 7,800 | 0.0% |
| CACHE | 620 | 0.0% |
| CALL | 360 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,942,200 | 75.5% |
| LOAD_CONST | 21,321,080 | 14.9% |
| LOAD_GLOBAL_MODULE | 13,617,600 | 9.5% |
| LOAD_FAST_LOAD_FAST | 2,540 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 280 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,258,800 | 75.4% |
| SWAP | 15,960,680 | 13.6% |
| LOAD_FAST_LOAD_FAST | 12,441,600 | 10.6% |
| STORE_ATTR_INSTANCE_VALUE | 326,680 | 0.3% |
| LOAD_GLOBAL_MODULE | 2,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 81,292,940 | 69.5% |
| LOAD_CONST | 30,775,280 | 26.3% |
| LOAD_GLOBAL_MODULE | 3,833,780 | 3.3% |
| LOAD_FAST_LOAD_FAST | 756,500 | 0.6% |
| STORE_ATTR_INSTANCE_VALUE | 326,680 | 0.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 804,000 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 801,820 | 99.7% |
| RETURN_CONST | 1,900 | 0.2% |
| JUMP_BACKWARD | 320 | 0.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 80,183,540 | 39.7% |
| RETURN_VALUE | 46,473,860 | 23.0% |
| LOAD_ATTR_INSTANCE_VALUE | 30,418,080 | 15.0% |
| LOAD_GLOBAL_MODULE | 24,028,040 | 11.9% |
| CALL_ISINSTANCE | 21,052,640 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 127,705,060 | 63.2% |
| POP_JUMP_IF_TRUE | 44,033,280 | 21.8% |
| UNARY_NOT | 30,418,120 | 15.0% |


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
|     deferred | 13,752,300 | 7.8% |
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
|          hit | 1,490,500 | 100.0% |

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
|     deferred | 163,667,200 | 34.2% |
|          hit | 311,329,440 | 65.1% |
|         miss | 166,810,600 | 34.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,149,000 | 100.0% |
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
|          hit | 103,667,520 | 100.0% |

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
|     deferred | 16,995,660 | 14.3% |
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
| Basic | 1,378,650,560 | 47.1% |
| Not specialized | 320,926,660 | 11.0% |
| Specialized hits | 1,030,297,860 | 35.2% |
| Specialized misses | 198,144,760 | 6.8% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 163,667,200 | 80.9% |
| STORE_ATTR | 16,995,660 | 8.4% |
| CALL | 13,752,300 | 6.8% |
| BINARY_OP | 7,999,520 | 4.0% |
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
| LOAD_ATTR_INSTANCE_VALUE | 102,566,920 | 51.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 64,243,680 | 32.4% |
| STORE_ATTR_INSTANCE_VALUE | 17,319,420 | 8.7% |
| CALL_PY_EXACT_ARGS | 14,014,720 | 7.1% |
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
| Frames pushed | 154,039,560 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 3,900 | 0.0% |
| Frees to freelist | 3,580 |  |
| Allocations | 18,901,560 | 100.0% |
| Allocations to 512 bytes | 18,901,520 | 100.0% |
| Allocations to 4 kbytes | 40 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 18,886,763 |  |
| New values | 520 |  |
| Interpreter increfs | 1,138,942,880 | 84.1% |
| Interpreter decrefs | 1,308,794,260 | 95.3% |
| Increfs | 216,011,665 | 15.9% |
| Decrefs | 65,037,294 | 4.7% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 174,144,841 |  |
| Method cache misses | 9,993,379 |  |
| Method cache collisions | 9,992,717 |  |
| Method cache dunder hits | 4,928 |  |
| Method cache dunder misses | 232 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 145,600 |
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
