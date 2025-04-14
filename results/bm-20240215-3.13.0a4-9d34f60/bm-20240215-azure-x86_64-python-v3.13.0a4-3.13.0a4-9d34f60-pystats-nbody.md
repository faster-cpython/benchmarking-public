
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
| LOAD_FAST | 1,014,419,360 | 22.6% | 22.6% |  |
| COPY | 480,000,000 | 10.7% | 33.3% |  |
| SWAP | 480,000,000 | 10.7% | 43.9% |  |
| BINARY_OP_MULTIPLY_FLOAT | 432,019,880 | 9.6% | 53.6% |  |
| STORE_FAST | 339,230,800 | 7.6% | 61.1% |  |
| LOAD_CONST | 272,005,200 | 6.1% | 67.2% |  |
| STORE_SUBSCR_LIST_INT | 240,000,000 | 5.3% | 72.5% |  |
| BINARY_SUBSCR_LIST_INT | 239,999,820 | 5.3% | 77.8% |  |
| BINARY_OP_ADD_FLOAT | 208,010,940 | 4.6% | 82.5% |  |
| BINARY_OP_SUBTRACT_FLOAT | 192,013,800 | 4.3% | 86.8% |  |
| LOAD_FAST_LOAD_FAST | 128,023,840 | 2.8% | 89.6% |  |
| STORE_FAST_STORE_FAST | 128,013,680 | 2.8% | 92.4% |  |
| UNPACK_SEQUENCE_TUPLE | 80,008,320 | 1.8% | 94.2% |  |
| UNPACK_SEQUENCE_LIST | 80,008,260 | 1.8% | 96.0% |  |
| FOR_ITER_LIST | 54,405,820 | 1.2% | 97.2% |  |
| JUMP_BACKWARD | 51,205,360 | 1.1% | 98.4% |  |
| BINARY_OP | 32,018,760 | 0.7% | 99.1% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 32,003,160 | 0.7% | 99.8% |  |
| GET_ITER | 6,400,960 | 0.1% | 99.9% |  |
| FOR_ITER_RANGE | 3,200,360 | 0.1% | 100.0% |  |
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
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 400,008,360 | 8.9% | 8.9% |
| LOAD_FAST LOAD_FAST | 368,008,000 | 8.2% | 17.1% |
| LOAD_FAST LOAD_CONST | 240,000,240 | 5.3% | 22.4% |
| COPY COPY | 240,000,000 | 5.3% | 27.8% |
| LOAD_CONST COPY | 240,000,000 | 5.3% | 33.1% |
| SWAP SWAP | 240,000,000 | 5.3% | 38.5% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 239,999,820 | 5.3% | 43.8% |
| COPY BINARY_SUBSCR_LIST_INT | 239,999,640 | 5.3% | 49.1% |
| SWAP STORE_SUBSCR_LIST_INT | 239,999,640 | 5.3% | 54.5% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_ADD_FLOAT | 208,009,120 | 4.6% | 59.1% |
| STORE_SUBSCR_LIST_INT LOAD_FAST | 191,999,860 | 4.3% | 63.4% |
| BINARY_OP_ADD_FLOAT SWAP | 143,999,880 | 3.2% | 66.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 128,013,680 | 2.8% | 69.4% |
| STORE_FAST LOAD_FAST | 115,201,680 | 2.6% | 72.0% |
| BINARY_OP_SUBTRACT_FLOAT STORE_FAST | 96,013,800 | 2.1% | 74.1% |
| LOAD_FAST_LOAD_FAST BINARY_OP_SUBTRACT_FLOAT | 96,009,360 | 2.1% | 76.3% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP_SUBTRACT_FLOAT | 96,000,960 | 2.1% | 78.4% |
| BINARY_OP_MULTIPLY_FLOAT STORE_FAST | 95,999,940 | 2.1% | 80.6% |
| BINARY_OP_SUBTRACT_FLOAT SWAP | 95,999,940 | 2.1% | 82.7% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 64,006,800 | 1.4% | 84.1% |
| UNPACK_SEQUENCE_LIST STORE_FAST_STORE_FAST | 64,006,700 | 1.4% | 85.5% |
| STORE_FAST_STORE_FAST STORE_FAST | 64,006,480 | 1.4% | 87.0% |
| UNPACK_SEQUENCE_TUPLE UNPACK_SEQUENCE_LIST | 64,006,240 | 1.4% | 88.4% |
| JUMP_BACKWARD FOR_ITER_LIST | 48,005,100 | 1.1% | 89.5% |
| STORE_FAST STORE_FAST | 48,004,800 | 1.1% | 90.5% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 47,999,960 | 1.1% | 91.6% |
| LOAD_CONST BINARY_OP | 32,004,800 | 0.7% | 92.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 32,004,400 | 0.7% | 93.0% |
| BINARY_OP_ADD_FLOAT LOAD_CONST | 32,003,160 | 0.7% | 93.7% |
| STORE_FAST UNPACK_SEQUENCE_TUPLE | 32,003,120 | 0.7% | 94.4% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 32,003,120 | 0.7% | 95.2% |
| UNPACK_SEQUENCE_TWO_TUPLE UNPACK_SEQUENCE_TUPLE | 32,003,120 | 0.7% | 95.9% |
| BINARY_OP_ADD_FLOAT LOAD_FAST | 32,001,560 | 0.7% | 96.6% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST | 32,001,560 | 0.7% | 97.3% |
| BINARY_OP BINARY_OP_MULTIPLY_FLOAT | 32,000,480 | 0.7% | 98.0% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST | 16,001,940 | 0.4% | 98.4% |
| STORE_FAST UNPACK_SEQUENCE_LIST | 16,001,880 | 0.4% | 98.7% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TUPLE | 16,001,880 | 0.4% | 99.1% |
| UNPACK_SEQUENCE_LIST STORE_FAST | 16,001,560 | 0.4% | 99.4% |
| LOAD_FAST GET_ITER | 6,400,800 | 0.1% | 99.6% |
| GET_ITER FOR_ITER_LIST | 6,400,620 | 0.1% | 99.7% |
| FOR_ITER_LIST LOAD_FAST | 3,200,720 | 0.1% | 99.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 3,200,120 | 0.1% | 99.9% |
| FOR_ITER_RANGE STORE_FAST | 3,200,120 | 0.1% | 99.9% |
| FOR_ITER_LIST JUMP_BACKWARD | 3,200,000 | 0.1% | 100.0% |
| BINARY_OP BINARY_OP | 12,100 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 9,480 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_FAST_LOAD_FAST | 6,360 | 0.0% | 100.0% |
| STORE_FAST JUMP_BACKWARD | 5,200 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_SUBTRACT_FLOAT | 3,440 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT LOAD_FAST_LOAD_FAST | 3,180 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_FLOAT | 1,820 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT STORE_FAST | 1,580 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT LOAD_CONST | 1,580 | 0.0% | 100.0% |
| BINARY_OP_ADD_FLOAT BINARY_OP_MULTIPLY_FLOAT | 1,560 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 880 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 600 | 0.0% | 100.0% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 480 | 0.0% | 100.0% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 400 | 0.0% | 100.0% |
| COPY BINARY_SUBSCR | 360 | 0.0% | 100.0% |
| SWAP STORE_SUBSCR | 360 | 0.0% | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT BINARY_OP | 360 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_FAST | 360 | 0.0% | 100.0% |
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
| POP_TOP LOAD_GLOBAL | 120 | 0.0% | 100.0% |
| LOAD_CONST STORE_SUBSCR | 120 | 0.0% | 100.0% |
| LOAD_CONST STORE_SUBSCR_LIST_INT | 120 | 0.0% | 100.0% |
| LOAD_FAST CALL | 120 | 0.0% | 100.0% |
| LOAD_FAST CALL_PY_WITH_DEFAULTS | 120 | 0.0% | 100.0% |
| UNPACK_SEQUENCE STORE_FAST_STORE_FAST | 120 | 0.0% | 100.0% |


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
| LOAD_FAST | 6,400,800 | 100.0% |
| CALL_BUILTIN_CLASS | 140 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 6,400,620 | 100.0% |
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
| LOAD_CONST | 32,004,800 | 100.0% |
| BINARY_OP | 12,100 | 0.0% |
| LOAD_FAST | 880 | 0.0% |
| LOAD_FAST_LOAD_FAST | 600 | 0.0% |
| BINARY_OP_MULTIPLY_FLOAT | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 32,000,480 | 99.9% |
| BINARY_OP | 12,100 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 3,440 | 0.0% |
| BINARY_OP_ADD_FLOAT | 1,820 | 0.0% |
| LOAD_FAST | 320 | 0.0% |


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
| COPY | 240,000,000 | 50.0% |
| LOAD_CONST | 240,000,000 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 240,000,000 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 239,999,640 | 50.0% |
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
| STORE_SUBSCR_LIST_INT | 47,999,960 | 93.7% |
| FOR_ITER_LIST | 3,200,000 | 6.2% |
| STORE_FAST | 5,200 | 0.0% |
| POP_TOP | 160 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 48,005,100 | 93.8% |
| FOR_ITER_RANGE | 3,200,120 | 6.2% |
| FOR_ITER | 140 | 0.0% |


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
| LOAD_FAST | 240,000,240 | 88.2% |
| BINARY_OP_ADD_FLOAT | 32,003,160 | 11.8% |
| BINARY_OP_MULTIPLY_FLOAT | 1,580 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 240,000,000 | 88.2% |
| BINARY_OP | 32,004,800 | 11.8% |
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
| LOAD_FAST | 368,008,000 | 36.3% |
| BINARY_SUBSCR_LIST_INT | 239,999,820 | 23.7% |
| STORE_SUBSCR_LIST_INT | 191,999,860 | 18.9% |
| STORE_FAST | 115,201,680 | 11.4% |
| LOAD_FAST_LOAD_FAST | 32,004,400 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 400,008,360 | 39.4% |
| LOAD_FAST | 368,008,000 | 36.3% |
| LOAD_CONST | 240,000,240 | 23.7% |
| GET_ITER | 6,400,800 | 0.6% |
| BINARY_OP | 880 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 128,013,680 | 100.0% |
| BINARY_OP_MULTIPLY_FLOAT | 6,360 | 0.0% |
| BINARY_OP_ADD_FLOAT | 3,180 | 0.0% |
| STORE_FAST_STORE_FAST | 400 | 0.0% |
| STORE_SUBSCR_LIST_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 96,009,360 | 75.0% |
| LOAD_FAST | 32,004,400 | 25.0% |
| BINARY_OP_MULTIPLY_FLOAT | 9,480 | 0.0% |
| BINARY_OP | 600 | 0.0% |


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
| BINARY_OP_SUBTRACT_FLOAT | 96,013,800 | 28.3% |
| BINARY_OP_MULTIPLY_FLOAT | 95,999,940 | 28.3% |
| STORE_FAST_STORE_FAST | 64,006,480 | 18.9% |
| STORE_FAST | 48,004,800 | 14.2% |
| UNPACK_SEQUENCE_TUPLE | 16,001,940 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 128,013,680 | 37.7% |
| LOAD_FAST | 115,201,680 | 34.0% |
| STORE_FAST | 48,004,800 | 14.2% |
| UNPACK_SEQUENCE_TUPLE | 32,003,120 | 9.4% |
| UNPACK_SEQUENCE_LIST | 16,001,880 | 4.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 64,006,800 | 50.0% |
| UNPACK_SEQUENCE_LIST | 64,006,700 | 50.0% |
| UNPACK_SEQUENCE | 120 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 64,006,800 | 50.0% |
| STORE_FAST | 64,006,480 | 50.0% |
| LOAD_FAST_LOAD_FAST | 400 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 240,000,000 | 50.0% |
| BINARY_OP_ADD_FLOAT | 143,999,880 | 30.0% |
| BINARY_OP_SUBTRACT_FLOAT | 95,999,940 | 20.0% |
| BINARY_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 240,000,000 | 50.0% |
| STORE_SUBSCR_LIST_INT | 239,999,640 | 50.0% |
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
| BINARY_OP_MULTIPLY_FLOAT | 208,009,120 | 100.0% |
| BINARY_OP | 1,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 143,999,880 | 69.2% |
| LOAD_CONST | 32,003,160 | 15.4% |
| LOAD_FAST | 32,001,560 | 15.4% |
| LOAD_FAST_LOAD_FAST | 3,180 | 0.0% |
| STORE_FAST | 1,580 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400,008,360 | 92.6% |
| BINARY_OP | 32,000,480 | 7.4% |
| LOAD_FAST_LOAD_FAST | 9,480 | 0.0% |
| BINARY_OP_ADD_FLOAT | 1,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 208,009,120 | 48.1% |
| BINARY_OP_SUBTRACT_FLOAT | 96,000,960 | 22.2% |
| STORE_FAST | 95,999,940 | 22.2% |
| LOAD_FAST | 32,001,560 | 7.4% |
| LOAD_FAST_LOAD_FAST | 6,360 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 96,009,360 | 50.0% |
| BINARY_OP_MULTIPLY_FLOAT | 96,000,960 | 50.0% |
| BINARY_OP | 3,440 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,013,800 | 50.0% |
| SWAP | 95,999,940 | 50.0% |
| RETURN_VALUE | 60 | 0.0% |


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
| COPY | 239,999,640 | 100.0% |
| BINARY_SUBSCR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 239,999,820 | 100.0% |


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
| JUMP_BACKWARD | 48,005,100 | 88.2% |
| GET_ITER | 6,400,620 | 11.8% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 32,003,120 | 58.8% |
| UNPACK_SEQUENCE_TUPLE | 16,001,880 | 29.4% |
| LOAD_FAST | 3,200,720 | 5.9% |
| JUMP_BACKWARD | 3,200,000 | 5.9% |
| UNPACK_SEQUENCE | 100 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,200,120 | 100.0% |
| GET_ITER | 200 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,200,120 | 100.0% |
| RETURN_CONST | 160 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


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
| SWAP | 239,999,640 | 100.0% |
| STORE_SUBSCR | 240 | 0.0% |
| LOAD_CONST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 191,999,860 | 80.0% |
| JUMP_BACKWARD | 47,999,960 | 20.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |
| RETURN_CONST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 64,006,240 | 80.0% |
| STORE_FAST | 16,001,880 | 20.0% |
| UNPACK_SEQUENCE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 64,006,700 | 80.0% |
| STORE_FAST | 16,001,560 | 20.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 32,003,120 | 40.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 32,003,120 | 40.0% |
| FOR_ITER_LIST | 16,001,880 | 20.0% |
| UNPACK_SEQUENCE | 160 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_LIST | 64,006,240 | 80.0% |
| STORE_FAST | 16,001,940 | 20.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |
| STORE_FAST_STORE_FAST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 32,003,120 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 32,003,120 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |


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
|     deferred | 32,009,300 | 3.7% |
|          hit | 832,044,620 | 96.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,060 | 11.2% |
| Failure | 8,400 | 88.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| power | 8,120 | 96.7% |
| true divide float | 280 | 3.3% |


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
|          hit | 57,606,180 | 100.0% |

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
| Basic | 2,899,301,860 | 64.5% |
| Not specialized | 32,021,660 | 0.7% |
| Specialized hits | 1,561,672,820 | 34.8% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 32,009,300 | 100.0% |
| CALL | 360 | 0.0% |
| UNPACK_SEQUENCE | 340 | 0.0% |
| STORE_SUBSCR | 240 | 0.0% |
| BINARY_SUBSCR | 200 | 0.0% |
| LOAD_GLOBAL | 200 | 0.0% |
| FOR_ITER | 140 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |
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
| Frames pushed | 480 | 66.7% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 528,036,820 | 98.2% |
| Frees to freelist | 528,036,980 |  |
| Allocations | 9,561,260 | 1.8% |
| Allocations to 512 bytes | 9,561,260 | 1.8% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 9,560,660 |  |
| New values | 0 |  |
| Interpreter increfs | 2,374,536,680 | 99.7% |
| Interpreter decrefs | 2,918,536,560 | 100.0% |
| Increfs | 6,403,160 | 0.3% |
| Decrefs | 1,203 | 0.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 41 |  |
| Method cache misses | 19 |  |
| Method cache collisions | 19 |  |
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
