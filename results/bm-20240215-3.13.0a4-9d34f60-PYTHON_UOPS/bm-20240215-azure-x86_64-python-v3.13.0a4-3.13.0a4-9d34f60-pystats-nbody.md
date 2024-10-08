
# Pystats results

- benchmark: nbody
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 32,032,320 | 19.6% | 19.6% |  |
| COPY | 19,210,920 | 11.8% | 31.4% |  |
| SWAP | 19,210,920 | 11.8% | 43.1% |  |
| STORE_FAST | 16,016,980 | 9.8% | 52.9% |  |
| BINARY_OP_MULTIPLY_FLOAT | 9,615,440 | 5.9% | 58.8% |  |
| LOAD_CONST | 9,607,840 | 5.9% | 64.7% |  |
| BINARY_OP_ADD_FLOAT | 9,607,400 | 5.9% | 70.6% |  |
| STORE_SUBSCR_LIST_INT | 9,605,460 | 5.9% | 76.5% |  |
| BINARY_SUBSCR_LIST_INT | 9,605,280 | 5.9% | 82.3% |  |
| FOR_ITER_LIST | 9,603,200 | 5.9% | 88.2% |  |
| ENTER_EXECUTOR | 9,600,180 | 5.9% | 94.1% |  |
| UNPACK_SEQUENCE_TUPLE | 3,203,900 | 2.0% | 96.1% |  |
| UNPACK_SEQUENCE_LIST | 3,203,840 | 2.0% | 98.0% |  |
| GET_ITER | 3,201,440 | 2.0% | 100.0% |  |
| LOAD_FAST_LOAD_FAST | 8,720 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 7,980 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 6,360 | 0.0% | 100.0% |  |
| BINARY_OP | 5,340 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 2,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,360 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 840 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 720 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 680 | 0.0% | 100.0% |  |
| POP_TOP | 640 | 0.0% | 100.0% |  |
| RESUME_CHECK | 620 | 0.0% | 100.0% |  |
| CALL | 540 | 0.0% | 100.0% |  |
| RETURN_VALUE | 480 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 480 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 480 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 400 | 0.0% | 100.0% |  |
| PUSH_NULL | 400 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 400 | 0.0% | 100.0% |  |
| FOR_ITER | 280 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| RETURN_CONST | 240 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 200 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_BUILTIN | 200 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 180 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| LOAD_ATTR | 120 | 0.0% | 100.0% |  |
| RESUME | 100 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| BUILD_LIST | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 9,611,900 | 5.9% | 5.9% |
| LOAD_FAST LOAD_FAST | 9,611,480 | 5.9% | 11.8% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 9,606,600 | 5.9% | 17.6% |
| LOAD_FAST LOAD_CONST | 9,605,700 | 5.9% | 23.5% |
| COPY COPY | 9,605,460 | 5.9% | 29.4% |
| LOAD_CONST COPY | 9,605,460 | 5.9% | 35.3% |
| SWAP SWAP | 9,605,460 | 5.9% | 41.2% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 9,605,280 | 5.9% | 47.0% |
| COPY BINARY_SUBSCR_LIST_INT | 9,605,100 | 5.9% | 52.9% |
| SWAP STORE_SUBSCR_LIST_INT | 9,605,100 | 5.9% | 58.8% |
| BINARY_OP_ADD_FLOAT SWAP | 9,603,000 | 5.9% | 64.7% |
| STORE_FAST STORE_FAST | 9,602,520 | 5.9% | 70.6% |
| STORE_SUBSCR_LIST_INT LOAD_FAST | 6,404,280 | 3.9% | 74.5% |
| ENTER_EXECUTOR FOR_ITER_LIST | 6,400,500 | 3.9% | 78.4% |
| STORE_FAST LOAD_FAST | 3,203,740 | 2.0% | 80.4% |
| LOAD_FAST GET_ITER | 3,201,280 | 2.0% | 82.3% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST | 3,201,120 | 2.0% | 84.3% |
| GET_ITER FOR_ITER_LIST | 3,201,100 | 2.0% | 86.2% |
| STORE_FAST UNPACK_SEQUENCE_LIST | 3,201,060 | 2.0% | 88.2% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TUPLE | 3,201,060 | 2.0% | 90.2% |
| UNPACK_SEQUENCE_LIST STORE_FAST | 3,200,800 | 2.0% | 92.1% |
| FOR_ITER_LIST LOAD_FAST | 3,200,720 | 2.0% | 94.1% |
| STORE_SUBSCR_LIST_INT ENTER_EXECUTOR | 3,200,360 | 2.0% | 96.0% |
| FOR_ITER_LIST ENTER_EXECUTOR | 3,199,660 | 2.0% | 98.0% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 3,199,520 | 2.0% | 100.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 6,360 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_FLOAT STORE_FAST | 5,640 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 3,960 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 3,140 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_SUBTRACT_FLOAT | 3,120 | 0.0% | 100.0% |
| UNPACK_SEQUENCE_LIST STORE_FAST_STORE_FAST | 3,040 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST STORE_FAST | 2,880 | 0.0% | 100.0% |
| UNPACK_SEQUENCE_TUPLE UNPACK_SEQUENCE_LIST | 2,640 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 2,420 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT STORE_FAST | 2,280 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_FLOAT SWAP | 2,280 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP | 1,980 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 1,740 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 1,500 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_LIST | 1,500 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT LOAD_CONST | 1,360 | 0.0% | 100.0% |
| STORE_FAST UNPACK_SEQUENCE_TUPLE | 1,320 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT LOAD_FAST | 1,320 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST | 1,320 | 0.0% | 100.0% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 1,320 | 0.0% | 100.0% |
| UNPACK_SEQUENCE_TWO_TUPLE UNPACK_SEQUENCE_TUPLE | 1,320 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_MULTIPLY_FLOAT | 1,260 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_LOAD_FAST | 1,200 | 0.0% | 100.0% |
| STORE_FAST JUMP_BACKWARD | 1,020 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 880 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 860 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 800 | 0.0% | 100.0% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 640 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 600 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT LOAD_FAST_LOAD_FAST | 600 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 600 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 560 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_CONST | 560 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT BINARY_OP_MULTIPLY_FLOAT | 540 | 0.0% | 100.0% |
| STORE_FAST ENTER_EXECUTOR | 520 | 0.0% | 100.0% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 480 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 440 | 0.0% | 100.0% |
| COPY BINARY_SUBSCR | 360 | 0.0% | 100.0% |
| SWAP STORE_SUBSCR | 360 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP | 360 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_FAST | 360 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 340 | 0.0% | 100.0% |
| FOR_ITER_LIST JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| RETURN_VALUE POP_TOP | 320 | 0.0% | 100.0% |
| BINARY_OP LOAD_FAST | 320 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 320 | 0.0% | 100.0% |
| BINARY_OP STORE_FAST | 280 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL_MODULE | 240 | 0.0% | 100.0% |
| PUSH_NULL CALL | 240 | 0.0% | 100.0% |
| STORE_SUBSCR STORE_SUBSCR_LIST_INT | 240 | 0.0% | 100.0% |
| RETURN_CONST POP_TOP | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE CALL_PY_WITH_DEFAULTS | 240 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_RANGE | 200 | 0.0% | 100.0% |
| STORE_FAST UNPACK_SEQUENCE | 200 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 200 | 0.0% | 100.0% |
| BINARY_SUBSCR LOAD_FAST | 180 | 0.0% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR_LIST_INT | 180 | 0.0% | 100.0% |
| BINARY_OP SWAP | 180 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 160 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 160 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 160 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 160 | 0.0% | 100.0% |
| UNPACK_SEQUENCE UNPACK_SEQUENCE_TUPLE | 160 | 0.0% | 100.0% |
| FOR_ITER_RANGE RETURN_CONST | 160 | 0.0% | 100.0% |
| GET_ITER FOR_ITER | 140 | 0.0% | 100.0% |
| STORE_SUBSCR LOAD_FAST | 140 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER | 140 | 0.0% | 100.0% |
| UNPACK_SEQUENCE UNPACK_SEQUENCE_LIST | 140 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS GET_ITER | 140 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_CONST | 140 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 360 | 90.0% |
| LOAD_FAST | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 45.0% |
| BINARY_SUBSCR_LIST_INT | 180 | 45.0% |
| CALL | 20 | 5.0% |
| BINARY_SUBSCR_DICT | 20 | 5.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,201,280 | 100.0% |
| CALL_BUILTIN_CLASS | 140 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 3,201,100 | 100.0% |
| FOR_ITER_RANGE | 200 | 0.0% |
| FOR_ITER | 140 | 0.0% |


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
| RETURN_VALUE | 320 | 50.0% |
| RETURN_CONST | 240 | 37.5% |
| CALL | 80 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 240 | 37.5% |
| JUMP_BACKWARD | 160 | 25.0% |
| LOAD_GLOBAL | 120 | 18.8% |
| NOP | 80 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 40 | 6.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 180 | 45.0% |
| LOAD_DEREF | 160 | 40.0% |
| LOAD_ATTR | 60 | 15.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 240 | 60.0% |
| LOAD_FAST | 160 | 40.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320 | 66.7% |
| RETURN_VALUE | 80 | 16.7% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 12.5% |
| BINARY_OP | 20 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 320 | 66.7% |
| RETURN_VALUE | 80 | 16.7% |
| LOAD_GLOBAL | 40 | 8.3% |
| LOAD_GLOBAL_MODULE | 40 | 8.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 360 | 75.0% |
| LOAD_CONST | 120 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 240 | 50.0% |
| LOAD_FAST | 140 | 29.2% |
| JUMP_BACKWARD | 40 | 8.3% |
| LOAD_FAST_LOAD_FAST | 40 | 8.3% |
| RETURN_CONST | 20 | 4.2% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,980 | 37.1% |
| BINARY_OP | 1,500 | 28.1% |
| LOAD_FAST | 880 | 16.5% |
| LOAD_FAST_LOAD_FAST | 600 | 11.2% |
| BINARY_OP_MULTIPLY_FLOAT | 360 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,500 | 28.1% |
| BINARY_OP_MULTIPLY_FLOAT | 1,260 | 23.6% |
| BINARY_OP_SUBTRACT_FLOAT | 860 | 16.1% |
| BINARY_OP_ADD_FLOAT | 800 | 15.0% |
| LOAD_FAST | 320 | 6.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 240 | 44.4% |
| LOAD_FAST | 120 | 22.2% |
| CALL | 60 | 11.1% |
| LOAD_GLOBAL | 40 | 7.4% |
| LOAD_GLOBAL_MODULE | 40 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 18.5% |
| POP_TOP | 80 | 14.8% |
| LOAD_FAST | 80 | 14.8% |
| CALL_PY_WITH_DEFAULTS | 80 | 14.8% |
| CALL | 60 | 11.1% |


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
| COPY | 9,605,460 | 50.0% |
| LOAD_CONST | 9,605,460 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 9,605,460 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 9,605,100 | 50.0% |
| BINARY_SUBSCR | 360 | 0.0% |


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
| STORE_SUBSCR_LIST_INT | 3,200,360 | 33.3% |
| FOR_ITER_LIST | 3,199,660 | 33.3% |
| ENTER_EXECUTOR | 3,199,520 | 33.3% |
| STORE_FAST | 520 | 0.0% |
| JUMP_BACKWARD | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 6,400,500 | 66.7% |
| ENTER_EXECUTOR | 3,199,520 | 33.3% |
| FOR_ITER_RANGE | 160 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 140 | 50.0% |
| JUMP_BACKWARD | 140 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE | 100 | 35.7% |
| FOR_ITER_LIST | 100 | 35.7% |
| STORE_FAST | 40 | 14.3% |
| FOR_ITER_RANGE | 40 | 14.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,020 | 46.4% |
| STORE_SUBSCR_LIST_INT | 640 | 29.1% |
| FOR_ITER_LIST | 340 | 15.5% |
| POP_TOP | 160 | 7.3% |
| STORE_SUBSCR | 40 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,500 | 68.2% |
| FOR_ITER_RANGE | 440 | 20.0% |
| FOR_ITER | 140 | 6.4% |
| ENTER_EXECUTOR | 120 | 5.5% |


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
| LOAD_FAST | 9,605,700 | 100.0% |
| BINARY_OP_ADD_FLOAT | 1,360 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 560 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 9,605,460 | 100.0% |
| BINARY_OP | 1,980 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| STORE_SUBSCR | 120 | 0.0% |
| STORE_SUBSCR_LIST_INT | 120 | 0.0% |


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
| LOAD_FAST | 9,611,480 | 30.0% |
| BINARY_SUBSCR_LIST_INT | 9,605,280 | 30.0% |
| STORE_SUBSCR_LIST_INT | 6,404,280 | 20.0% |
| STORE_FAST | 3,203,740 | 10.0% |
| FOR_ITER_LIST | 3,200,720 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 9,611,900 | 30.0% |
| LOAD_FAST | 9,611,480 | 30.0% |
| LOAD_CONST | 9,605,700 | 30.0% |
| GET_ITER | 3,201,280 | 10.0% |
| BINARY_OP | 880 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,360 | 72.9% |
| BINARY_OP_MULTIPLY_FLOAT | 1,200 | 13.8% |
| BINARY_OP_ADD_FLOAT | 600 | 6.9% |
| STORE_FAST_STORE_FAST | 340 | 3.9% |
| STORE_SUBSCR_LIST_INT | 120 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 3,960 | 45.4% |
| LOAD_FAST | 2,420 | 27.8% |
| BINARY_OP_MULTIPLY_FLOAT | 1,740 | 20.0% |
| BINARY_OP | 600 | 6.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 120 | 30.0% |
| STORE_FAST | 80 | 20.0% |
| RETURN_VALUE | 40 | 10.0% |
| RESUME | 40 | 10.0% |
| FOR_ITER_RANGE | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 160 | 40.0% |
| LOAD_ATTR | 60 | 15.0% |
| LOAD_FAST | 60 | 15.0% |
| CALL | 40 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 10.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 160 | 66.7% |
| STORE_SUBSCR_LIST_INT | 60 | 25.0% |
| STORE_SUBSCR | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 240 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,602,520 | 60.0% |
| UNPACK_SEQUENCE_TUPLE | 3,201,120 | 20.0% |
| UNPACK_SEQUENCE_LIST | 3,200,800 | 20.0% |
| BINARY_OP_SUBTRACT_FLOAT | 5,640 | 0.0% |
| STORE_FAST_STORE_FAST | 2,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 9,602,520 | 60.0% |
| LOAD_FAST | 3,203,740 | 20.0% |
| UNPACK_SEQUENCE_LIST | 3,201,060 | 20.0% |
| LOAD_FAST_LOAD_FAST | 6,360 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 1,320 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 3,140 | 49.4% |
| UNPACK_SEQUENCE_LIST | 3,040 | 47.8% |
| UNPACK_SEQUENCE | 120 | 1.9% |
| UNPACK_SEQUENCE_TUPLE | 60 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 3,140 | 49.4% |
| STORE_FAST | 2,880 | 45.3% |
| LOAD_FAST_LOAD_FAST | 340 | 5.3% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,605,460 | 50.0% |
| BINARY_OP_ADD_FLOAT | 9,603,000 | 50.0% |
| BINARY_OP_SUBTRACT_FLOAT | 2,280 | 0.0% |
| BINARY_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,605,460 | 50.0% |
| STORE_SUBSCR_LIST_INT | 9,605,100 | 50.0% |
| STORE_SUBSCR | 360 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 29.4% |
| UNPACK_SEQUENCE | 120 | 17.6% |
| FOR_ITER | 100 | 14.7% |
| FOR_ITER_LIST | 100 | 14.7% |
| UNPACK_SEQUENCE_TUPLE | 80 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 160 | 23.5% |
| UNPACK_SEQUENCE_LIST | 140 | 20.6% |
| STORE_FAST_STORE_FAST | 120 | 17.6% |
| UNPACK_SEQUENCE | 120 | 17.6% |
| STORE_FAST | 100 | 14.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 60 | 60.0% |
| CALL_FUNCTION_EX | 20 | 20.0% |
| COPY_FREE_VARS | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| LOAD_GLOBAL | 40 | 40.0% |
| LOAD_DEREF | 20 | 20.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 9,606,600 | 100.0% |
| BINARY_OP | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,603,000 | 100.0% |
| LOAD_CONST | 1,360 | 0.0% |
| LOAD_FAST | 1,320 | 0.0% |
| LOAD_FAST_LOAD_FAST | 600 | 0.0% |
| STORE_FAST | 560 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,611,900 | 100.0% |
| LOAD_FAST_LOAD_FAST | 1,740 | 0.0% |
| BINARY_OP | 1,260 | 0.0% |
| BINARY_OP_ADD_FLOAT | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 9,606,600 | 99.9% |
| BINARY_OP_SUBTRACT_FLOAT | 3,120 | 0.0% |
| STORE_FAST | 2,280 | 0.0% |
| LOAD_FAST | 1,320 | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,200 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,960 | 49.6% |
| BINARY_OP_MULTIPLY_FLOAT | 3,120 | 39.1% |
| BINARY_OP | 860 | 10.8% |
| LOAD_FAST | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,640 | 70.7% |
| SWAP | 2,280 | 28.6% |
| RETURN_VALUE | 60 | 0.8% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| BINARY_SUBSCR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 40 | 66.7% |
| CALL | 20 | 33.3% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 9,605,100 | 100.0% |
| BINARY_SUBSCR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,605,280 | 100.0% |


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

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 240 | 50.0% |
| LOAD_FAST | 120 | 25.0% |
| CALL | 80 | 16.7% |
| BINARY_SUBSCR_DICT | 40 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 480 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,400,500 | 66.6% |
| GET_ITER | 3,201,100 | 33.3% |
| JUMP_BACKWARD | 1,500 | 0.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 3,201,060 | 33.3% |
| LOAD_FAST | 3,200,720 | 33.3% |
| ENTER_EXECUTOR | 3,199,660 | 33.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,320 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 440 | 52.4% |
| GET_ITER | 200 | 23.8% |
| ENTER_EXECUTOR | 160 | 19.0% |
| FOR_ITER | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 71.4% |
| RETURN_CONST | 160 | 19.0% |
| LOAD_GLOBAL | 40 | 4.8% |
| LOAD_GLOBAL_MODULE | 40 | 4.8% |


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
| RESUME_CHECK | 120 | 60.0% |
| POP_TOP | 40 | 20.0% |
| LOAD_GLOBAL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 240 | 33.3% |
| LOAD_GLOBAL | 160 | 22.2% |
| STORE_FAST | 160 | 22.2% |
| RETURN_VALUE | 40 | 5.6% |
| FOR_ITER_RANGE | 40 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 240 | 33.3% |
| LOAD_CONST | 140 | 19.4% |
| LOAD_ATTR_MODULE | 120 | 16.7% |
| LOAD_ATTR | 60 | 8.3% |
| LOAD_FAST | 60 | 8.3% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 480 | 77.4% |
| CALL_FUNCTION_EX | 60 | 9.7% |
| COPY_FREE_VARS | 60 | 9.7% |
| CALL | 20 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 58.1% |
| LOAD_GLOBAL_BUILTIN | 120 | 19.4% |
| LOAD_DEREF | 60 | 9.7% |
| LOAD_GLOBAL | 40 | 6.5% |
| LOAD_GLOBAL_MODULE | 40 | 6.5% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 9,605,100 | 100.0% |
| STORE_SUBSCR | 240 | 0.0% |
| LOAD_CONST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,404,280 | 66.7% |
| ENTER_EXECUTOR | 3,200,360 | 33.3% |
| JUMP_BACKWARD | 640 | 0.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |
| RETURN_CONST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,201,060 | 99.9% |
| UNPACK_SEQUENCE_TUPLE | 2,640 | 0.1% |
| UNPACK_SEQUENCE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,200,800 | 99.9% |
| STORE_FAST_STORE_FAST | 3,040 | 0.1% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 3,201,060 | 99.9% |
| STORE_FAST | 1,320 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,320 | 0.0% |
| UNPACK_SEQUENCE | 160 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,201,120 | 99.9% |
| UNPACK_SEQUENCE_LIST | 2,640 | 0.1% |
| UNPACK_SEQUENCE | 80 | 0.0% |
| STORE_FAST_STORE_FAST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,320 | 97.1% |
| UNPACK_SEQUENCE | 40 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 1,320 | 97.1% |
| UNPACK_SEQUENCE | 40 | 2.9% |


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
|     deferred | 3,900 | 0.0% |
|          hit | 832,044,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,060 | 73.6% |
| Failure | 380 | 26.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| true divide float | 220 | 57.9% |
| power | 160 | 42.1% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 0.0% |
|          hit | 239,999,880 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 360 | 29.5% |
|          hit | 680 | 55.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 66.7% |
| Failure | 60 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 140 | 0.0% |
|          hit | 9,604,040 | 100.0% |

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
|     deferred | 200 | 15.2% |
|          hit | 920 | 69.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 240,000,000 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 192,019,740 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 108,900,540 | 66.7% |
| Not specialized | 8,240 | 0.0% |
| Specialized hits | 54,457,160 | 33.3% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 3,900 | 71.7% |
| CALL | 360 | 6.6% |
| UNPACK_SEQUENCE | 340 | 6.2% |
| STORE_SUBSCR | 240 | 4.4% |
| BINARY_SUBSCR | 200 | 3.7% |
| LOAD_GLOBAL | 200 | 3.7% |
| FOR_ITER | 140 | 2.6% |
| LOAD_ATTR | 60 | 1.1% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 0 | 0.0% |
| Calls to Python functions inlined | 720 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 22.2% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 720 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 528,036,820 | 98.2% |
| Frees to freelist | 528,036,980 |  |
| Allocations | 9,561,380 | 1.8% |
| Allocations to 512 bytes | 9,561,260 | 1.8% |
| Allocations to 4 kbytes | 120 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 9,560,660 |  |
| New values | 0 |  |
| Interpreter increfs | 83,294,940 | 3.5% |
| Interpreter decrefs | 105,721,100 | 3.6% |
| Increfs | 2,307,245,280 | 96.5% |
| Decrefs | 2,822,417,040 | 96.4% |
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
| Optimization attempts | 120 |  |
| Traces created | 120 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 20 | 16.7% |
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
| <= 64 | 20 | 16.7% |
| <= 128 | 60 | 50.0% |
| <= 256 | 0 | 0.0% |
| <= 512 | 40 | 33.3% |


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
| <= 64 | 80 | 66.7% |
| <= 128 | 0 | 0.0% |
| <= 256 | 40 | 33.3% |


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
