
# Pystats results

- benchmark: spectral_norm
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| BINARY_OP_ADD_INT | 270,399,900 | 17.1% | 17.1% |  |
| LOAD_CONST | 216,736,240 | 13.7% | 30.9% |  |
| LOAD_FAST | 163,515,680 | 10.4% | 41.2% |  |
| LOAD_FAST_LOAD_FAST | 162,676,800 | 10.3% | 51.6% |  |
| BINARY_OP | 109,841,380 | 7.0% | 58.5% |  |
| STORE_FAST | 54,522,720 | 3.5% | 62.0% |  |
| FOR_ITER | 54,520,440 | 3.5% | 65.4% |  |
| JUMP_BACKWARD | 54,507,280 | 3.5% | 68.9% |  |
| STORE_FAST_STORE_FAST | 54,506,480 | 3.5% | 72.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 54,506,300 | 3.5% | 75.8% |  |
| CALL_PY_EXACT_ARGS | 54,503,840 | 3.5% | 79.3% | 0.3% |
| RETURN_VALUE | 54,500,960 | 3.5% | 82.7% |  |
| RESUME_CHECK | 54,500,820 | 3.5% | 86.2% |  |
| BINARY_OP_ADD_FLOAT | 54,100,720 | 3.4% | 89.6% | 0.8% |
| LOAD_GLOBAL_MODULE | 54,088,080 | 3.4% | 93.0% |  |
| BINARY_OP_MULTIPLY_INT | 54,079,980 | 3.4% | 96.5% |  |
| BINARY_OP_MULTIPLY_FLOAT | 52,463,760 | 3.3% | 99.8% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 425,680 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 422,440 | 0.0% | 99.8% |  |
| FOR_ITER_RANGE | 420,180 | 0.0% | 99.9% |  |
| GET_ITER | 419,440 | 0.0% | 99.9% |  |
| PUSH_NULL | 416,400 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 416,000 | 0.0% | 99.9% |  |
| LIST_APPEND | 416,000 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 416,000 | 0.0% | 100.0% |  |
| SWAP | 9,600 | 0.0% | 100.0% |  |
| BUILD_LIST | 3,360 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 3,200 | 0.0% | 100.0% |  |
| CALL_LEN | 3,180 | 0.0% | 100.0% |  |
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
| BINARY_OP_ADD_INT LOAD_CONST | 108,159,960 | 6.9% | 6.9% |
| LOAD_CONST BINARY_OP_ADD_INT | 108,159,920 | 6.9% | 13.7% |
| LOAD_FAST_LOAD_FAST BINARY_OP_ADD_INT | 108,159,920 | 6.9% | 20.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 54,506,300 | 3.5% | 24.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 54,500,640 | 3.5% | 27.5% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 54,092,880 | 3.4% | 30.9% |
| STORE_FAST JUMP_BACKWARD | 54,091,200 | 3.4% | 34.3% |
| JUMP_BACKWARD FOR_ITER | 54,090,460 | 3.4% | 37.8% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 54,090,280 | 3.4% | 41.2% |
| LOAD_CONST BINARY_OP | 54,080,080 | 3.4% | 44.6% |
| BINARY_OP RETURN_VALUE | 54,080,020 | 3.4% | 48.1% |
| RETURN_VALUE LOAD_FAST | 54,080,000 | 3.4% | 51.5% |
| BINARY_OP LOAD_FAST | 54,080,000 | 3.4% | 54.9% |
| LOAD_CONST LOAD_FAST_LOAD_FAST | 54,080,000 | 3.4% | 58.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 54,080,000 | 3.4% | 61.8% |
| BINARY_OP_ADD_INT BINARY_OP | 54,080,000 | 3.4% | 65.2% |
| BINARY_OP_ADD_INT LOAD_FAST_LOAD_FAST | 54,079,980 | 3.4% | 68.6% |
| BINARY_OP_MULTIPLY_INT LOAD_CONST | 54,079,980 | 3.4% | 72.1% |
| RESUME_CHECK LOAD_CONST | 54,079,980 | 3.4% | 75.5% |
| LOAD_FAST BINARY_OP_ADD_INT | 54,079,960 | 3.4% | 78.9% |
| BINARY_OP_ADD_INT BINARY_OP_MULTIPLY_INT | 54,079,960 | 3.4% | 82.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 54,079,960 | 3.4% | 85.8% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 54,079,920 | 3.4% | 89.2% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 54,079,920 | 3.4% | 92.6% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 52,463,620 | 3.3% | 96.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 52,456,020 | 3.3% | 99.3% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 1,644,700 | 0.1% | 99.4% |
| LOAD_FAST BINARY_OP | 1,637,260 | 0.1% | 99.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 419,260 | 0.0% | 99.5% |
| CALL_BUILTIN_CLASS GET_ITER | 419,200 | 0.0% | 99.5% |
| LOAD_FAST CALL_BUILTIN_CLASS | 419,120 | 0.0% | 99.6% |
| JUMP_BACKWARD FOR_ITER_RANGE | 416,820 | 0.0% | 99.6% |
| GET_ITER FOR_ITER | 416,120 | 0.0% | 99.6% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 416,000 | 0.0% | 99.6% |
| RETURN_VALUE LIST_APPEND | 416,000 | 0.0% | 99.7% |
| FOR_ITER LOAD_FAST | 416,000 | 0.0% | 99.7% |
| LIST_APPEND JUMP_BACKWARD | 416,000 | 0.0% | 99.7% |
| LOAD_CONST STORE_FAST | 416,000 | 0.0% | 99.8% |
| LOAD_FAST RETURN_VALUE | 416,000 | 0.0% | 99.8% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 416,000 | 0.0% | 99.8% |
| STORE_FAST_LOAD_FAST PUSH_NULL | 416,000 | 0.0% | 99.8% |
| STORE_FAST_STORE_FAST LOAD_CONST | 416,000 | 0.0% | 99.9% |
| FOR_ITER_RANGE STORE_FAST_LOAD_FAST | 415,980 | 0.0% | 99.9% |
| BUILD_TUPLE CALL_PY_EXACT_ARGS | 415,960 | 0.0% | 99.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 415,960 | 0.0% | 99.9% |
| RESUME_CHECK LOAD_FAST | 415,960 | 0.0% | 100.0% |
| LOAD_FAST UNPACK_SEQUENCE_TWO_TUPLE | 415,920 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 28,300 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 20,800 | 0.0% | 100.0% |
| FOR_ITER FOR_ITER | 13,840 | 0.0% | 100.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 10,400 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 10,400 | 0.0% | 100.0% |
| BINARY_OP STORE_FAST | 8,000 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT BINARY_OP | 7,840 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP | 7,740 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 6,320 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 4,680 | 0.0% | 100.0% |
| GET_ITER LOAD_FAST_AND_CLEAR | 3,200 | 0.0% | 100.0% |
| BUILD_LIST SWAP | 3,200 | 0.0% | 100.0% |
| LOAD_FAST_AND_CLEAR SWAP | 3,200 | 0.0% | 100.0% |
| STORE_FAST RETURN_VALUE | 3,200 | 0.0% | 100.0% |
| SWAP BUILD_LIST | 3,200 | 0.0% | 100.0% |
| SWAP STORE_FAST | 3,200 | 0.0% | 100.0% |
| FOR_ITER_RANGE SWAP | 3,200 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,200 | 0.0% | 100.0% |
| SWAP FOR_ITER_RANGE | 3,180 | 0.0% | 100.0% |
| CALL_PY_EXACT_ARGS CALL_PY_EXACT_ARGS | 3,180 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS CALL_LEN | 3,160 | 0.0% | 100.0% |
| CALL_LEN CALL_BUILTIN_CLASS | 3,160 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 3,140 | 0.0% | 100.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 3,080 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 1,680 | 0.0% | 100.0% |
| RETURN_VALUE STORE_FAST | 1,600 | 0.0% | 100.0% |
| RETURN_VALUE CALL_PY_EXACT_ARGS | 1,560 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 1,560 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,560 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 840 | 0.0% | 100.0% |
| LOAD_FAST CALL | 280 | 0.0% | 100.0% |
| PUSH_NULL CALL | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 240 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 100.0% |
| CALL GET_ITER | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 160 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_MULTIPLY_FLOAT | 140 | 0.0% | 100.0% |
| CALL CALL_PY_EXACT_ARGS | 140 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_RANGE | 120 | 0.0% | 100.0% |
| CALL CALL | 120 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| FOR_ITER UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_INT | 100 | 0.0% | 100.0% |
| CALL STORE_FAST | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL | 100 | 0.0% | 100.0% |
| UNPACK_SEQUENCE STORE_FAST_STORE_FAST | 100 | 0.0% | 100.0% |
| UNPACK_SEQUENCE UNPACK_SEQUENCE_TWO_TUPLE | 100 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 419,200 | 99.9% |
| CALL | 160 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 416,120 | 99.2% |
| LOAD_FAST_AND_CLEAR | 3,200 | 0.8% |
| FOR_ITER_RANGE | 120 | 0.0% |


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
| STORE_FAST_LOAD_FAST | 416,000 | 99.9% |
| LOAD_ATTR_MODULE | 180 | 0.0% |
| LOAD_DEREF | 160 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 416,000 | 99.9% |
| CALL | 240 | 0.1% |
| LOAD_FAST | 160 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 54,080,020 | 99.2% |
| LOAD_FAST | 416,000 | 0.8% |
| STORE_FAST | 3,200 | 0.0% |
| RETURN_VALUE | 1,680 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,080,000 | 99.2% |
| LIST_APPEND | 416,000 | 0.8% |
| RETURN_VALUE | 1,680 | 0.0% |
| STORE_FAST | 1,600 | 0.0% |
| CALL_PY_EXACT_ARGS | 1,560 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 54,080,080 | 49.2% |
| BINARY_OP_ADD_INT | 54,080,000 | 49.2% |
| LOAD_FAST | 1,637,260 | 1.5% |
| BINARY_OP | 28,300 | 0.0% |
| BINARY_OP_ADD_FLOAT | 7,840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 54,080,020 | 49.2% |
| LOAD_FAST | 54,080,000 | 49.2% |
| BINARY_OP_ADD_FLOAT | 1,644,700 | 1.5% |
| BINARY_OP | 28,300 | 0.0% |
| STORE_FAST | 8,000 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,200 | 95.2% |
| LOAD_CONST | 80 | 2.4% |
| LOAD_FAST | 80 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,200 | 95.2% |
| LOAD_DEREF | 80 | 2.4% |
| LOAD_GLOBAL | 40 | 1.2% |
| LOAD_GLOBAL_MODULE | 40 | 1.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 416,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 415,960 | 100.0% |
| CALL | 40 | 0.0% |


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

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 54,090,460 | 99.2% |
| GET_ITER | 416,120 | 0.8% |
| FOR_ITER | 13,840 | 0.0% |
| SWAP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 54,090,280 | 99.2% |
| LOAD_FAST | 416,000 | 0.8% |
| FOR_ITER | 13,840 | 0.0% |
| UNPACK_SEQUENCE | 120 | 0.0% |
| JUMP_BACKWARD | 80 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 54,091,200 | 99.2% |
| LIST_APPEND | 416,000 | 0.8% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 54,090,460 | 99.2% |
| FOR_ITER_RANGE | 416,820 | 0.8% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 416,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 416,000 | 100.0% |


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
| BINARY_OP_ADD_INT | 108,159,960 | 49.9% |
| BINARY_OP_MULTIPLY_INT | 54,079,980 | 25.0% |
| RESUME_CHECK | 54,079,980 | 25.0% |
| STORE_FAST_STORE_FAST | 416,000 | 0.2% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 108,159,920 | 49.9% |
| BINARY_OP | 54,080,080 | 25.0% |
| LOAD_FAST_LOAD_FAST | 54,080,000 | 25.0% |
| STORE_FAST | 416,000 | 0.2% |
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
| RETURN_VALUE | 54,080,000 | 33.1% |
| BINARY_OP | 54,080,000 | 33.1% |
| STORE_FAST_STORE_FAST | 54,080,000 | 33.1% |
| LOAD_GLOBAL_BUILTIN | 419,260 | 0.3% |
| FOR_ITER | 416,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 54,079,960 | 33.1% |
| LOAD_GLOBAL_MODULE | 54,079,920 | 33.1% |
| BINARY_OP_MULTIPLY_FLOAT | 52,463,620 | 32.1% |
| BINARY_OP | 1,637,260 | 1.0% |
| CALL_BUILTIN_CLASS | 419,120 | 0.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,200 | 100.0% |


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
| LOAD_CONST | 54,080,000 | 33.2% |
| BINARY_OP_ADD_INT | 54,079,980 | 33.2% |
| LOAD_GLOBAL_MODULE | 54,079,960 | 33.2% |
| PUSH_NULL | 416,000 | 0.3% |
| STORE_FAST | 10,400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 108,159,920 | 66.5% |
| CALL_PY_EXACT_ARGS | 54,079,920 | 33.2% |
| BUILD_TUPLE | 416,000 | 0.3% |
| LOAD_FAST | 20,800 | 0.0% |
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
| BINARY_OP_ADD_FLOAT | 54,092,880 | 99.2% |
| LOAD_CONST | 416,000 | 0.8% |
| BINARY_OP | 8,000 | 0.0% |
| SWAP | 3,200 | 0.0% |
| RETURN_VALUE | 1,600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 54,091,200 | 99.2% |
| LOAD_GLOBAL_BUILTIN | 415,960 | 0.8% |
| LOAD_FAST_LOAD_FAST | 10,400 | 0.0% |
| RETURN_VALUE | 3,200 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,560 | 0.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 415,980 | 100.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 416,000 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 54,506,300 | 100.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,080,000 | 99.2% |
| LOAD_CONST | 416,000 | 0.8% |
| LOAD_FAST_LOAD_FAST | 10,400 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 3,200 | 33.3% |
| LOAD_FAST_AND_CLEAR | 3,200 | 33.3% |
| FOR_ITER_RANGE | 3,200 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 3,200 | 33.3% |
| STORE_FAST | 3,200 | 33.3% |
| FOR_ITER_RANGE | 3,180 | 33.1% |
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
| BINARY_OP_MULTIPLY_FLOAT | 52,456,020 | 97.0% |
| BINARY_OP | 1,644,700 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 54,092,880 | 100.0% |
| BINARY_OP | 7,840 | 0.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,159,920 | 40.0% |
| LOAD_FAST_LOAD_FAST | 108,159,920 | 40.0% |
| LOAD_FAST | 54,079,960 | 20.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,159,960 | 40.0% |
| BINARY_OP | 54,080,000 | 20.0% |
| LOAD_FAST_LOAD_FAST | 54,079,980 | 20.0% |
| BINARY_OP_MULTIPLY_INT | 54,079,960 | 20.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,463,620 | 100.0% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 52,456,020 | 100.0% |
| BINARY_OP | 7,740 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 54,079,960 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 54,079,980 | 100.0% |


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
| LOAD_FAST | 419,120 | 99.2% |
| CALL_LEN | 3,160 | 0.7% |
| CALL | 120 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 419,200 | 99.2% |
| CALL_LEN | 3,160 | 0.7% |
| STORE_FAST | 60 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 3,160 | 99.4% |
| CALL | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 3,160 | 99.4% |
| CALL | 20 | 0.6% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 54,079,920 | 99.2% |
| BUILD_TUPLE | 415,960 | 0.8% |
| CALL_PY_EXACT_ARGS | 3,180 | 0.0% |
| LOAD_FAST | 3,080 | 0.0% |
| RETURN_VALUE | 1,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 54,500,640 | 100.0% |
| CALL_PY_EXACT_ARGS | 3,180 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 416,820 | 99.2% |
| SWAP | 3,180 | 0.8% |
| GET_ITER | 120 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 415,980 | 99.0% |
| SWAP | 3,200 | 0.8% |
| STORE_FAST | 840 | 0.2% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


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
| STORE_FAST | 415,960 | 97.7% |
| LOAD_GLOBAL_BUILTIN | 6,320 | 1.5% |
| RESUME_CHECK | 3,200 | 0.8% |
| LOAD_GLOBAL | 160 | 0.0% |
| STORE_FAST_STORE_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 419,260 | 98.5% |
| LOAD_GLOBAL_BUILTIN | 6,320 | 1.5% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,079,920 | 100.0% |
| LOAD_GLOBAL_MODULE | 4,680 | 0.0% |
| STORE_FAST | 1,560 | 0.0% |
| RESUME_CHECK | 1,560 | 0.0% |
| LOAD_GLOBAL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 54,079,960 | 100.0% |
| LOAD_GLOBAL_MODULE | 4,680 | 0.0% |
| LOAD_FAST | 3,140 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| BINARY_OP | 60 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 54,500,640 | 100.0% |
| CALL | 60 | 0.0% |
| CALL_FUNCTION_EX | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 54,079,980 | 99.2% |
| LOAD_FAST | 415,960 | 0.8% |
| LOAD_GLOBAL_BUILTIN | 3,200 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,560 | 0.0% |
| LOAD_DEREF | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 54,090,280 | 99.2% |
| LOAD_FAST | 415,920 | 0.8% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 54,506,300 | 100.0% |


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
|     deferred | 109,797,340 | 20.3% |
|          hit | 430,625,160 | 79.6% |
|         miss | 419,260 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,200 | 18.6% |
| Failure | 35,840 | 81.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 13,400 | 37.4% |
| true divide different types | 13,400 | 37.4% |
| add different types | 7,840 | 21.9% |
| multiply different types | 1,200 | 3.3% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,191,029,740 | 671,640,379,728,010.5% |
|          hit | 54,760,920 | 99.7% |
|         miss | 168,540 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,460 | 97.7% |
| Failure | 80 | 2.3% |

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
|     deferred | 54,506,540 | 99.2% |
|          hit | 420,180 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 0.4% |
| Failure | 13,840 | 99.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 13,680 | 98.8% |
| zip | 160 | 1.2% |


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
|     deferred | 400 | 0.0% |
|          hit | 54,513,760 | 100.0% |

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
| Basic | 763,067,260 | 48.4% |
| Not specialized | 164,363,900 | 10.4% |
| Specialized hits | 649,327,320 | 41.2% |
| Specialized misses | 587,800 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 368,934,881,474,191,029,740 | 100.0% |
| BINARY_OP | 109,797,340 | 0.0% |
| FOR_ITER | 54,506,540 | 0.0% |
| LOAD_GLOBAL | 400 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |
| BINARY_SUBSCR | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 416,080 | 70.8% |
| CALL_PY_EXACT_ARGS | 168,540 | 28.7% |
| BINARY_OP_MULTIPLY_FLOAT | 3,180 | 0.5% |
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
| Frames pushed | 54,335,300 | 99.7% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 56,733,460 | 20.9% |
| Frees to freelist | 56,736,720 |  |
| Allocations | 214,503,720 | 79.1% |
| Allocations to 512 bytes | 214,500,440 | 79.1% |
| Allocations to 4 kbytes | 3,280 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 214,503,580 |  |
| New values | 0 |  |
| Interpreter increfs | 324,378,720 | 75.0% |
| Interpreter decrefs | 648,454,620 | 92.2% |
| Increfs | 108,080,800 | 25.0% |
| Decrefs | 55,238,560 | 7.8% |
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
