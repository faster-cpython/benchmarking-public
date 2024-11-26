
# Pystats results

- benchmark: spectral_norm
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 1,473,940 | 13.7% | 13.7% |  |
| BINARY_OP_ADD_INT | 1,052,700 | 9.8% | 23.4% |  |
| LOAD_CONST | 1,052,400 | 9.8% | 33.2% |  |
| BINARY_OP | 837,860 | 7.8% | 40.9% |  |
| ENTER_EXECUTOR | 832,240 | 7.7% | 48.6% |  |
| LOAD_FAST_LOAD_FAST | 635,580 | 5.9% | 54.5% |  |
| STORE_FAST | 632,860 | 5.9% | 60.4% |  |
| RETURN_VALUE | 631,520 | 5.9% | 66.2% |  |
| RESUME_CHECK | 424,460 | 3.9% | 70.2% |  |
| CALL_PY_EXACT_ARGS | 424,360 | 3.9% | 74.1% | 0.9% |
| STORE_FAST_STORE_FAST | 420,960 | 3.9% | 78.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 420,780 | 3.9% | 81.9% |  |
| LIST_APPEND | 416,000 | 3.9% | 85.8% |  |
| LOAD_GLOBAL_BUILTIN | 218,340 | 2.0% | 87.8% |  |
| LOAD_GLOBAL_MODULE | 216,540 | 2.0% | 89.8% |  |
| CALL_BUILTIN_CLASS | 215,520 | 2.0% | 91.8% |  |
| GET_ITER | 212,940 | 2.0% | 93.7% |  |
| FOR_ITER | 211,480 | 2.0% | 95.7% |  |
| BINARY_OP_MULTIPLY_INT | 210,540 | 2.0% | 97.7% |  |
| BINARY_OP_MULTIPLY_FLOAT | 210,160 | 1.9% | 99.6% | 0.0% |
| SWAP | 8,760 | 0.1% | 99.7% |  |
| FOR_ITER_RANGE | 6,860 | 0.1% | 99.8% |  |
| BINARY_OP_ADD_FLOAT | 3,520 | 0.0% | 99.8% | 63.6% |
| PUSH_NULL | 3,500 | 0.0% | 99.8% |  |
| BUILD_TUPLE | 3,100 | 0.0% | 99.8% |  |
| STORE_FAST_LOAD_FAST | 3,100 | 0.0% | 99.9% |  |
| BUILD_LIST | 2,940 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 2,780 | 0.0% | 99.9% |  |
| CALL_LEN | 2,760 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 1,780 | 0.0% | 100.0% |  |
| CALL | 960 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 800 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 200 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 180 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| RESUME | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| POP_TOP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| CALL_PY_EXACT_ARGS RESUME_CHECK | 424,280 | 3.9% | 3.9% |
| BINARY_OP_ADD_INT LOAD_CONST | 421,080 | 3.9% | 7.8% |
| LOAD_CONST BINARY_OP_ADD_INT | 421,040 | 3.9% | 11.7% |
| LOAD_FAST_LOAD_FAST BINARY_OP_ADD_INT | 421,040 | 3.9% | 15.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 420,780 | 3.9% | 19.5% |
| STORE_FAST ENTER_EXECUTOR | 416,480 | 3.9% | 23.4% |
| RETURN_VALUE LIST_APPEND | 416,000 | 3.9% | 27.2% |
| ENTER_EXECUTOR LOAD_FAST | 416,000 | 3.9% | 31.1% |
| LOAD_FAST RETURN_VALUE | 416,000 | 3.9% | 35.0% |
| LIST_APPEND ENTER_EXECUTOR | 415,660 | 3.9% | 38.8% |
| BINARY_OP STORE_FAST | 414,040 | 3.8% | 42.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 212,760 | 2.0% | 44.6% |
| CALL_BUILTIN_CLASS GET_ITER | 212,700 | 2.0% | 46.6% |
| LOAD_FAST CALL_BUILTIN_CLASS | 212,620 | 2.0% | 48.6% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 210,840 | 2.0% | 50.5% |
| LOAD_CONST BINARY_OP | 210,640 | 2.0% | 52.5% |
| BINARY_OP RETURN_VALUE | 210,580 | 2.0% | 54.4% |
| RETURN_VALUE LOAD_FAST | 210,560 | 2.0% | 56.4% |
| BINARY_OP LOAD_FAST | 210,560 | 2.0% | 58.3% |
| LOAD_CONST LOAD_FAST_LOAD_FAST | 210,560 | 2.0% | 60.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 210,560 | 2.0% | 62.2% |
| BINARY_OP_ADD_INT BINARY_OP | 210,560 | 2.0% | 64.2% |
| BINARY_OP_ADD_INT LOAD_FAST_LOAD_FAST | 210,540 | 2.0% | 66.1% |
| BINARY_OP_MULTIPLY_INT LOAD_CONST | 210,540 | 2.0% | 68.1% |
| RESUME_CHECK LOAD_CONST | 210,540 | 2.0% | 70.0% |
| LOAD_FAST BINARY_OP_ADD_INT | 210,520 | 2.0% | 72.0% |
| BINARY_OP_ADD_INT BINARY_OP_MULTIPLY_INT | 210,520 | 2.0% | 73.9% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 210,520 | 2.0% | 75.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 210,480 | 2.0% | 77.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 210,480 | 2.0% | 79.8% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 210,080 | 1.9% | 81.7% |
| GET_ITER FOR_ITER | 210,040 | 1.9% | 83.7% |
| LOAD_CONST STORE_FAST | 209,920 | 1.9% | 85.6% |
| STORE_FAST_STORE_FAST LOAD_CONST | 209,920 | 1.9% | 87.5% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 209,880 | 1.9% | 89.5% |
| RESUME_CHECK LOAD_FAST | 209,880 | 1.9% | 91.4% |
| LOAD_FAST UNPACK_SEQUENCE_TWO_TUPLE | 209,840 | 1.9% | 93.4% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP | 208,080 | 1.9% | 95.3% |
| ENTER_EXECUTOR CALL_PY_EXACT_ARGS | 206,820 | 1.9% | 97.2% |
| ENTER_EXECUTOR BINARY_OP | 205,340 | 1.9% | 99.1% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 5,480 | 0.1% | 99.2% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 3,480 | 0.0% | 99.2% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 3,420 | 0.0% | 99.2% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 3,260 | 0.0% | 99.3% |
| STORE_FAST RETURN_VALUE | 3,200 | 0.0% | 99.3% |
| SWAP STORE_FAST | 3,200 | 0.0% | 99.3% |
| FOR_ITER_RANGE SWAP | 3,200 | 0.0% | 99.4% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 3,100 | 0.0% | 99.4% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 3,100 | 0.0% | 99.4% |
| STORE_FAST_LOAD_FAST PUSH_NULL | 3,100 | 0.0% | 99.4% |
| FOR_ITER_RANGE STORE_FAST_LOAD_FAST | 3,080 | 0.0% | 99.5% |
| BUILD_TUPLE CALL_PY_EXACT_ARGS | 3,060 | 0.0% | 99.5% |
| GET_ITER LOAD_FAST_AND_CLEAR | 2,780 | 0.0% | 99.5% |
| BUILD_LIST SWAP | 2,780 | 0.0% | 99.6% |
| LOAD_FAST_AND_CLEAR SWAP | 2,780 | 0.0% | 99.6% |
| SWAP BUILD_LIST | 2,780 | 0.0% | 99.6% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,780 | 0.0% | 99.6% |
| SWAP FOR_ITER_RANGE | 2,760 | 0.0% | 99.7% |
| CALL_BUILTIN_CLASS CALL_LEN | 2,740 | 0.0% | 99.7% |
| CALL_LEN CALL_BUILTIN_CLASS | 2,740 | 0.0% | 99.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,300 | 0.0% | 99.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 2,240 | 0.0% | 99.7% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 2,080 | 0.0% | 99.8% |
| RETURN_VALUE RETURN_VALUE | 1,680 | 0.0% | 99.8% |
| BINARY_OP BINARY_OP | 1,680 | 0.0% | 99.8% |
| RETURN_VALUE STORE_FAST | 1,600 | 0.0% | 99.8% |
| RETURN_VALUE CALL_PY_EXACT_ARGS | 1,560 | 0.0% | 99.8% |
| LOAD_FAST BINARY_OP | 1,360 | 0.0% | 99.8% |
| STORE_FAST JUMP_BACKWARD | 1,360 | 0.0% | 99.9% |
| STORE_FAST LOAD_GLOBAL_MODULE | 1,140 | 0.0% | 99.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,140 | 0.0% | 99.9% |
| JUMP_BACKWARD FOR_ITER | 1,020 | 0.0% | 99.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 800 | 0.0% | 99.9% |
| ENTER_EXECUTOR BINARY_OP_ADD_FLOAT | 740 | 0.0% | 99.9% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 700 | 0.0% | 99.9% |
| JUMP_BACKWARD FOR_ITER_RANGE | 660 | 0.0% | 99.9% |
| FOR_ITER_RANGE STORE_FAST | 420 | 0.0% | 99.9% |
| FOR_ITER FOR_ITER | 400 | 0.0% | 99.9% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 400 | 0.0% | 99.9% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 400 | 0.0% | 99.9% |
| LIST_APPEND JUMP_BACKWARD | 340 | 0.0% | 99.9% |
| LOAD_FAST CALL | 280 | 0.0% | 99.9% |
| PUSH_NULL CALL | 240 | 0.0% | 99.9% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 240 | 0.0% | 99.9% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.0% | 99.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.0% | 99.9% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 99.9% |
| CALL GET_ITER | 160 | 0.0% | 99.9% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 99.9% |
| LOAD_GLOBAL LOAD_FAST | 160 | 0.0% | 99.9% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 160 | 0.0% | 99.9% |
| CALL CALL_PY_EXACT_ARGS | 140 | 0.0% | 99.9% |
| GET_ITER FOR_ITER_RANGE | 120 | 0.0% | 100.0% |
| CALL CALL | 120 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| FOR_ITER UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_INT | 100 | 0.0% | 100.0% |
| CALL STORE_FAST | 100 | 0.0% | 100.0% |
| JUMP_BACKWARD ENTER_EXECUTOR | 100 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 212,700 | 99.9% |
| CALL | 160 | 0.1% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 210,040 | 98.6% |
| LOAD_FAST_AND_CLEAR | 2,780 | 1.3% |
| FOR_ITER_RANGE | 120 | 0.1% |


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
| CALL | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 80 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 3,100 | 88.6% |
| LOAD_ATTR_MODULE | 180 | 5.1% |
| LOAD_DEREF | 160 | 4.6% |
| LOAD_ATTR | 60 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,100 | 88.6% |
| CALL | 240 | 6.9% |
| LOAD_FAST | 160 | 4.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 416,000 | 65.9% |
| BINARY_OP | 210,580 | 33.3% |
| STORE_FAST | 3,200 | 0.5% |
| RETURN_VALUE | 1,680 | 0.3% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 416,000 | 65.9% |
| LOAD_FAST | 210,560 | 33.3% |
| RETURN_VALUE | 1,680 | 0.3% |
| STORE_FAST | 1,600 | 0.3% |
| CALL_PY_EXACT_ARGS | 1,560 | 0.2% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 210,640 | 25.1% |
| BINARY_OP_ADD_INT | 210,560 | 25.1% |
| BINARY_OP_MULTIPLY_FLOAT | 208,080 | 24.8% |
| ENTER_EXECUTOR | 205,340 | 24.5% |
| BINARY_OP | 1,680 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 414,040 | 49.4% |
| RETURN_VALUE | 210,580 | 25.1% |
| LOAD_FAST | 210,560 | 25.1% |
| BINARY_OP | 1,680 | 0.2% |
| BINARY_OP_ADD_FLOAT | 700 | 0.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,780 | 94.6% |
| LOAD_CONST | 80 | 2.7% |
| LOAD_FAST | 80 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,780 | 94.6% |
| LOAD_DEREF | 80 | 2.7% |
| LOAD_GLOBAL | 40 | 1.4% |
| LOAD_GLOBAL_MODULE | 40 | 1.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,060 | 98.7% |
| CALL | 40 | 1.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 29.2% |
| PUSH_NULL | 240 | 25.0% |
| CALL | 120 | 12.5% |
| LOAD_FAST_CHECK | 80 | 8.3% |
| LOAD_FAST_LOAD_FAST | 80 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 160 | 16.7% |
| CALL_PY_EXACT_ARGS | 140 | 14.6% |
| CALL | 120 | 12.5% |
| CALL_BUILTIN_CLASS | 120 | 12.5% |
| STORE_FAST | 100 | 10.4% |


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

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 80 | 100.0% |


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
| STORE_FAST | 416,480 | 50.0% |
| LIST_APPEND | 415,660 | 49.9% |
| JUMP_BACKWARD | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 416,000 | 50.0% |
| CALL_PY_EXACT_ARGS | 206,820 | 24.9% |
| BINARY_OP | 205,340 | 24.7% |
| FOR_ITER_RANGE | 3,260 | 0.4% |
| BINARY_OP_ADD_FLOAT | 740 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 210,040 | 99.3% |
| JUMP_BACKWARD | 1,020 | 0.5% |
| FOR_ITER | 400 | 0.2% |
| SWAP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 210,840 | 99.7% |
| FOR_ITER | 400 | 0.2% |
| UNPACK_SEQUENCE | 120 | 0.1% |
| FOR_ITER_RANGE | 60 | 0.0% |
| STORE_FAST | 40 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,360 | 76.4% |
| LIST_APPEND | 340 | 19.1% |
| ENTER_EXECUTOR | 80 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,020 | 57.3% |
| FOR_ITER_RANGE | 660 | 37.1% |
| ENTER_EXECUTOR | 100 | 5.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 416,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 415,660 | 99.9% |
| JUMP_BACKWARD | 340 | 0.1% |


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
| LOAD_GLOBAL | 60 | 50.0% |
| LOAD_GLOBAL_MODULE | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 50.0% |
| LOAD_ATTR_MODULE | 60 | 50.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 421,080 | 40.0% |
| BINARY_OP_MULTIPLY_INT | 210,540 | 20.0% |
| RESUME_CHECK | 210,540 | 20.0% |
| STORE_FAST_STORE_FAST | 209,920 | 19.9% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 421,040 | 40.0% |
| BINARY_OP | 210,640 | 20.0% |
| LOAD_FAST_LOAD_FAST | 210,560 | 20.0% |
| STORE_FAST | 209,920 | 19.9% |
| BUILD_LIST | 80 | 0.0% |


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
| ENTER_EXECUTOR | 416,000 | 28.2% |
| LOAD_GLOBAL_BUILTIN | 212,760 | 14.4% |
| RETURN_VALUE | 210,560 | 14.3% |
| BINARY_OP | 210,560 | 14.3% |
| STORE_FAST_STORE_FAST | 210,560 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 416,000 | 28.2% |
| CALL_BUILTIN_CLASS | 212,620 | 14.4% |
| BINARY_OP_ADD_INT | 210,520 | 14.3% |
| LOAD_GLOBAL_MODULE | 210,480 | 14.3% |
| BINARY_OP_MULTIPLY_FLOAT | 210,080 | 14.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,780 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,780 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 210,560 | 33.1% |
| BINARY_OP_ADD_INT | 210,540 | 33.1% |
| LOAD_GLOBAL_MODULE | 210,520 | 33.1% |
| PUSH_NULL | 3,100 | 0.5% |
| STORE_FAST | 400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 421,040 | 66.2% |
| CALL_PY_EXACT_ARGS | 210,480 | 33.1% |
| BUILD_TUPLE | 3,100 | 0.5% |
| LOAD_FAST | 800 | 0.1% |
| BINARY_OP | 80 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 30.0% |
| LOAD_GLOBAL | 100 | 12.5% |
| LOAD_FAST | 80 | 10.0% |
| RESUME | 60 | 7.5% |
| LOAD_GLOBAL_MODULE | 60 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 240 | 30.0% |
| LOAD_FAST | 160 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 160 | 20.0% |
| LOAD_GLOBAL | 100 | 12.5% |
| LOAD_ATTR | 60 | 7.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 414,040 | 65.4% |
| LOAD_CONST | 209,920 | 33.2% |
| BINARY_OP_ADD_FLOAT | 3,480 | 0.5% |
| SWAP | 3,200 | 0.5% |
| RETURN_VALUE | 1,600 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 416,480 | 65.8% |
| LOAD_GLOBAL_BUILTIN | 209,880 | 33.2% |
| RETURN_VALUE | 3,200 | 0.5% |
| JUMP_BACKWARD | 1,360 | 0.2% |
| LOAD_GLOBAL_MODULE | 1,140 | 0.2% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 3,080 | 99.4% |
| FOR_ITER | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 3,100 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 420,780 | 100.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 210,560 | 50.0% |
| LOAD_CONST | 209,920 | 49.9% |
| LOAD_FAST_LOAD_FAST | 400 | 0.1% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 3,200 | 36.5% |
| BUILD_LIST | 2,780 | 31.7% |
| LOAD_FAST_AND_CLEAR | 2,780 | 31.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,200 | 36.5% |
| BUILD_LIST | 2,780 | 31.7% |
| FOR_ITER_RANGE | 2,760 | 31.5% |
| FOR_ITER | 20 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 120 | 60.0% |
| LOAD_FAST | 80 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 100 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 100 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 57.1% |
| CALL_FUNCTION_EX | 20 | 14.3% |
| COPY_FREE_VARS | 20 | 14.3% |
| CALL_PY_EXACT_ARGS | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 60 | 42.9% |
| LOAD_FAST | 40 | 28.6% |
| LOAD_CONST | 20 | 14.3% |
| LOAD_DEREF | 20 | 14.3% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 2,080 | 59.1% |
| ENTER_EXECUTOR | 740 | 21.0% |
| BINARY_OP | 700 | 19.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,480 | 98.9% |
| BINARY_OP | 40 | 1.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 421,040 | 40.0% |
| LOAD_FAST_LOAD_FAST | 421,040 | 40.0% |
| LOAD_FAST | 210,520 | 20.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 421,080 | 40.0% |
| BINARY_OP | 210,560 | 20.0% |
| LOAD_FAST_LOAD_FAST | 210,540 | 20.0% |
| BINARY_OP_MULTIPLY_INT | 210,520 | 20.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 210,080 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 208,080 | 99.0% |
| BINARY_OP_ADD_FLOAT | 2,080 | 1.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 210,520 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 210,540 | 100.0% |


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
| RETURN_VALUE | 60 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 212,620 | 98.7% |
| CALL_LEN | 2,740 | 1.3% |
| CALL | 120 | 0.1% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 212,700 | 98.7% |
| CALL_LEN | 2,740 | 1.3% |
| STORE_FAST | 60 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 2,740 | 99.3% |
| CALL | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 2,740 | 99.3% |
| CALL | 20 | 0.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 210,480 | 49.6% |
| ENTER_EXECUTOR | 206,820 | 48.7% |
| BUILD_TUPLE | 3,060 | 0.7% |
| LOAD_FAST | 2,240 | 0.5% |
| RETURN_VALUE | 1,560 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 424,280 | 100.0% |
| CALL_PY_EXACT_ARGS | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 3,260 | 47.5% |
| SWAP | 2,760 | 40.2% |
| JUMP_BACKWARD | 660 | 9.6% |
| GET_ITER | 120 | 1.7% |
| FOR_ITER | 60 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,200 | 46.6% |
| STORE_FAST_LOAD_FAST | 3,080 | 44.9% |
| STORE_FAST | 420 | 6.1% |
| LOAD_CONST | 80 | 1.2% |
| LOAD_GLOBAL | 40 | 0.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 66.7% |
| LOAD_ATTR | 60 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 180 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 209,880 | 96.1% |
| LOAD_GLOBAL_BUILTIN | 5,480 | 2.5% |
| RESUME_CHECK | 2,780 | 1.3% |
| LOAD_GLOBAL | 160 | 0.1% |
| STORE_FAST_STORE_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 212,760 | 97.4% |
| LOAD_GLOBAL_BUILTIN | 5,480 | 2.5% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 210,480 | 97.2% |
| LOAD_GLOBAL_MODULE | 3,420 | 1.6% |
| STORE_FAST | 1,140 | 0.5% |
| RESUME_CHECK | 1,140 | 0.5% |
| LOAD_GLOBAL | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 210,520 | 97.2% |
| LOAD_GLOBAL_MODULE | 3,420 | 1.6% |
| LOAD_FAST | 2,300 | 1.1% |
| LOAD_ATTR_MODULE | 120 | 0.1% |
| BINARY_OP | 60 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 424,280 | 100.0% |
| CALL | 60 | 0.0% |
| CALL_FUNCTION_EX | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 210,540 | 49.6% |
| LOAD_FAST | 209,880 | 49.4% |
| LOAD_GLOBAL_BUILTIN | 2,780 | 0.7% |
| LOAD_GLOBAL_MODULE | 1,140 | 0.3% |
| LOAD_DEREF | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 210,840 | 50.1% |
| LOAD_FAST | 209,840 | 49.9% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 420,780 | 100.0% |


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
|     deferred | 838,740 | 0.2% |
|          hit | 405,226,380 | 99.8% |
|         miss | 2,280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 21.4% |
| Failure | 1,100 | 78.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add different types | 520 | 47.3% |
| floor divide | 240 | 21.8% |
| true divide different types | 240 | 21.8% |
| multiply different types | 100 | 9.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,240 | 0.0% |
|          hit | 54,922,640 | 100.0% |
|         miss | 3,700 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 81.0% |
| Failure | 80 | 19.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 75.0% |
| class no vectorcall | 20 | 25.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 211,020 | 96.6% |
|          hit | 6,860 | 3.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 13.0% |
| Failure | 400 | 87.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 340 | 85.0% |
| zip | 60 | 15.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 20.0% |
|          hit | 180 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 400 | 0.1% |
|          hit | 434,880 | 99.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 400 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 54,506,300 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 6,335,500 | 58.7% |
| Not specialized | 1,051,420 | 9.7% |
| Specialized hits | 3,400,800 | 31.5% |
| Specialized misses | 5,980 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 838,740 | 79.5% |
| FOR_ITER | 211,020 | 20.0% |
| CALL | 4,240 | 0.4% |
| LOAD_GLOBAL | 400 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| BINARY_SUBSCR | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,700 | 61.9% |
| BINARY_OP_ADD_FLOAT | 2,240 | 37.5% |
| BINARY_OP_MULTIPLY_FLOAT | 40 | 0.7% |
| GET_ITER | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |
| RETURN_VALUE | 0 | 0.0% |
| BUILD_LIST | 0 | 0.0% |
| BUILD_TUPLE | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 0 | 0.0% |
| Calls to Python functions inlined | 54,500,960 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 54,500,960 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 82,132,240 | 27.7% |
| Frees to freelist | 82,135,500 |  |
| Allocations | 214,503,820 | 72.3% |
| Allocations to 512 bytes | 214,500,460 | 72.3% |
| Allocations to 4 kbytes | 3,360 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 214,503,580 |  |
| New values | 0 |  |
| Interpreter increfs | 3,168,220 | 0.7% |
| Interpreter decrefs | 113,893,700 | 15.6% |
| Increfs | 430,123,920 | 99.3% |
| Decrefs | 616,030,881 | 84.4% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 39 |  |
| Method cache misses | 21 |  |
| Method cache collisions | 21 |  |
| Method cache dunder hits | 0 |  |
| Method cache dunder misses | 0 |  |


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
| Optimization attempts | 100 |  |
| Traces created | 100 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 40 | 40.0% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 0 | 0.0% |
| <= 64 | 20 | 20.0% |
| <= 128 | 60 | 60.0% |
| <= 256 | 20 | 20.0% |


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
| <= 32 | 20 | 20.0% |
| <= 64 | 40 | 40.0% |
| <= 128 | 20 | 20.0% |
| <= 256 | 20 | 20.0% |


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
