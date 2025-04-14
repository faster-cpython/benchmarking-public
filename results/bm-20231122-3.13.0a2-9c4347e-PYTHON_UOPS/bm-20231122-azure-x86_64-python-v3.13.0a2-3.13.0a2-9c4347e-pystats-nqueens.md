
# Pystats results

- benchmark: nqueens
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 236,851,360 | 10.9% | 10.9% |  |
| POP_TOP | 138,195,120 | 6.4% | 17.2% |  |
| STORE_FAST | 129,912,240 | 6.0% | 23.2% |  |
| JUMP_BACKWARD | 129,911,200 | 6.0% | 29.2% |  |
| RESUME_CHECK | 125,630,500 | 5.8% | 35.0% | 0.0% |
| LOAD_FAST_LOAD_FAST | 122,752,160 | 5.6% | 40.6% |  |
| INTERPRETER_EXIT | 119,179,380 | 5.5% | 46.1% |  |
| YIELD_VALUE | 112,389,760 | 5.2% | 51.2% |  |
| LOAD_DEREF | 105,938,880 | 4.9% | 56.1% |  |
| BINARY_SUBSCR_TUPLE_INT | 105,923,760 | 4.9% | 61.0% |  |
| LOAD_CONST | 99,104,400 | 4.6% | 65.5% |  |
| FOR_ITER_RANGE | 78,639,840 | 3.6% | 69.1% |  |
| BINARY_OP_ADD_INT | 73,779,740 | 3.4% | 72.5% |  |
| FOR_ITER_LIST | 58,060,760 | 2.7% | 75.2% |  |
| SWAP | 47,974,240 | 2.2% | 77.4% |  |
| BINARY_SUBSCR_LIST_INT | 47,974,000 | 2.2% | 79.6% |  |
| COPY | 41,523,200 | 1.9% | 81.5% |  |
| STORE_SUBSCR_LIST_INT | 35,071,940 | 1.6% | 83.1% |  |
| LOAD_GLOBAL_BUILTIN | 32,933,180 | 1.5% | 84.6% |  |
| BINARY_OP_SUBTRACT_INT | 31,325,680 | 1.4% | 86.1% |  |
| POP_JUMP_IF_FALSE | 30,438,480 | 1.4% | 87.5% |  |
| BINARY_SLICE | 28,621,120 | 1.3% | 88.8% |  |
| COMPARE_OP_INT | 24,325,280 | 1.1% | 89.9% |  |
| CALL_BUILTIN_CLASS | 19,692,500 | 0.9% | 90.8% |  |
| GET_ITER | 19,691,920 | 0.9% | 91.7% |  |
| RETURN_CONST | 13,240,960 | 0.6% | 92.3% |  |
| RETURN_GENERATOR | 13,240,800 | 0.6% | 92.9% |  |
| COPY_FREE_VARS | 13,240,560 | 0.6% | 93.5% |  |
| CALL_PY_EXACT_ARGS | 13,240,540 | 0.6% | 94.2% |  |
| MAKE_FUNCTION | 13,240,480 | 0.6% | 94.8% |  |
| BUILD_TUPLE | 13,240,480 | 0.6% | 95.4% |  |
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 0.6% | 96.0% |  |
| UNARY_NEGATIVE | 12,902,080 | 0.6% | 96.6% |  |
| BINARY_OP | 11,088,260 | 0.5% | 97.1% |  |
| STORE_SLICE | 11,084,960 | 0.5% | 97.6% |  |
| CALL_LEN | 6,789,380 | 0.3% | 97.9% |  |
| JUMP_FORWARD | 6,465,760 | 0.3% | 98.2% |  |
| BINARY_SUBSCR | 6,453,320 | 0.3% | 98.5% |  |
| STORE_SUBSCR | 6,452,920 | 0.3% | 98.8% |  |
| STORE_DEREF | 6,451,360 | 0.3% | 99.1% |  |
| FOR_ITER_GEN | 6,451,340 | 0.3% | 99.4% |  |
| CALL_TUPLE_1 | 6,451,300 | 0.3% | 99.7% |  |
| TO_BOOL_INT | 6,451,160 | 0.3% | 100.0% |  |
| POP_JUMP_IF_TRUE | 338,080 | 0.0% | 100.0% |  |
| CALL | 1,420 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 840 | 0.0% | 100.0% |  |
| PUSH_NULL | 480 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 400 | 0.0% | 100.0% |  |
| MAKE_CELL | 320 | 0.0% | 100.0% |  |
| RESUME | 300 | 0.0% | 100.0% | 20.0% |
| FOR_ITER | 280 | 0.0% | 100.0% |  |
| END_FOR | 160 | 0.0% | 100.0% |  |
| BUILD_SLICE | 160 | 0.0% | 100.0% |  |
| COMPARE_OP | 160 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| RETURN_VALUE | 80 | 0.0% | 100.0% |  |
| TO_BOOL | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| LOAD_ATTR | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| RESUME_CHECK POP_TOP | 112,389,620 | 5.2% | 5.2% |
| POP_TOP JUMP_BACKWARD | 112,051,840 | 5.1% | 10.3% |
| CACHE RESUME_CHECK | 105,938,600 | 4.9% | 15.2% |
| YIELD_VALUE INTERPRETER_EXIT | 105,938,580 | 4.9% | 20.1% |
| STORE_FAST LOAD_DEREF | 105,923,920 | 4.9% | 24.9% |
| LOAD_DEREF LOAD_FAST | 105,923,840 | 4.9% | 29.8% |
| LOAD_FAST BINARY_SUBSCR_TUPLE_INT | 105,923,680 | 4.9% | 34.7% |
| FOR_ITER_RANGE STORE_FAST | 71,850,320 | 3.3% | 38.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 65,399,280 | 3.0% | 41.0% |
| BINARY_SUBSCR_TUPLE_INT LOAD_FAST | 54,314,200 | 2.5% | 43.5% |
| BINARY_OP_ADD_INT YIELD_VALUE | 51,609,580 | 2.4% | 45.8% |
| JUMP_BACKWARD FOR_ITER_LIST | 51,609,560 | 2.4% | 48.2% |
| LOAD_FAST BINARY_OP_ADD_INT | 51,609,560 | 2.4% | 50.6% |
| BINARY_SUBSCR_TUPLE_INT YIELD_VALUE | 51,609,560 | 2.4% | 52.9% |
| FOR_ITER_LIST STORE_FAST | 51,609,560 | 2.4% | 55.3% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 35,071,960 | 1.6% | 56.9% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 30,437,960 | 1.4% | 58.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 23,987,220 | 1.1% | 59.4% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 23,987,040 | 1.1% | 60.5% |
| STORE_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST | 23,987,000 | 1.1% | 61.6% |
| LOAD_CONST BINARY_OP_ADD_INT | 22,170,080 | 1.0% | 62.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 22,169,920 | 1.0% | 63.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 19,692,060 | 0.9% | 64.6% |
| LOAD_FAST LOAD_CONST | 17,536,400 | 0.8% | 65.4% |
| COPY COPY | 17,536,000 | 0.8% | 66.2% |
| LOAD_CONST COMPARE_OP_INT | 17,536,000 | 0.8% | 67.0% |
| LOAD_FAST_LOAD_FAST COPY | 17,536,000 | 0.8% | 67.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 17,536,000 | 0.8% | 68.6% |
| SWAP SWAP | 17,536,000 | 0.8% | 69.4% |
| BINARY_OP_SUBTRACT_INT SWAP | 17,535,980 | 0.8% | 70.2% |
| COPY BINARY_SUBSCR_LIST_INT | 17,535,960 | 0.8% | 71.0% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 17,535,960 | 0.8% | 71.8% |
| SWAP STORE_SUBSCR_LIST_INT | 17,535,960 | 0.8% | 72.6% |
| LOAD_FAST_LOAD_FAST STORE_SUBSCR_LIST_INT | 17,535,920 | 0.8% | 73.4% |
| RETURN_CONST INTERPRETER_EXIT | 13,240,800 | 0.6% | 74.1% |
| POP_TOP RESUME_CHECK | 13,240,680 | 0.6% | 74.7% |
| CACHE POP_TOP | 13,240,660 | 0.6% | 75.3% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 13,240,600 | 0.6% | 75.9% |
| MAKE_FUNCTION SET_FUNCTION_ATTRIBUTE | 13,240,480 | 0.6% | 76.5% |
| BUILD_TUPLE LOAD_CONST | 13,240,480 | 0.6% | 77.1% |
| COPY_FREE_VARS RETURN_GENERATOR | 13,240,480 | 0.6% | 77.7% |
| LOAD_CONST MAKE_FUNCTION | 13,240,480 | 0.6% | 78.3% |
| LOAD_FAST BUILD_TUPLE | 13,240,480 | 0.6% | 78.9% |
| SET_FUNCTION_ATTRIBUTE LOAD_FAST | 13,240,480 | 0.6% | 79.5% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 13,240,400 | 0.6% | 80.1% |
| RESUME_CHECK LOAD_FAST | 13,240,400 | 0.6% | 80.7% |
| GET_ITER CALL_PY_EXACT_ARGS | 13,240,320 | 0.6% | 81.4% |
| LOAD_FAST_LOAD_FAST UNARY_NEGATIVE | 12,902,080 | 0.6% | 81.9% |
| LOAD_FAST_LOAD_FAST BINARY_OP_SUBTRACT_INT | 11,085,040 | 0.5% | 82.5% |
| BINARY_OP LOAD_FAST_LOAD_FAST | 11,084,980 | 0.5% | 83.0% |
| BINARY_SLICE BINARY_OP | 11,084,960 | 0.5% | 83.5% |
| BINARY_SLICE LOAD_FAST_LOAD_FAST | 11,084,960 | 0.5% | 84.0% |
| STORE_SLICE LOAD_FAST_LOAD_FAST | 11,084,960 | 0.5% | 84.5% |
| LOAD_CONST BINARY_SLICE | 11,084,960 | 0.5% | 85.0% |
| LOAD_CONST STORE_SLICE | 11,084,960 | 0.5% | 85.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 11,084,960 | 0.5% | 86.0% |
| BINARY_OP_ADD_INT BINARY_SLICE | 11,084,940 | 0.5% | 86.5% |
| BINARY_OP_ADD_INT LOAD_CONST | 11,084,940 | 0.5% | 87.0% |
| BINARY_OP_SUBTRACT_INT LOAD_FAST_LOAD_FAST | 11,084,940 | 0.5% | 87.6% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 11,084,940 | 0.5% | 88.1% |
| FOR_ITER_RANGE RETURN_CONST | 6,789,440 | 0.3% | 88.4% |
| LOAD_FAST GET_ITER | 6,789,360 | 0.3% | 88.7% |
| RETURN_GENERATOR CALL_BUILTIN_CLASS | 6,789,320 | 0.3% | 89.0% |
| LOAD_FAST FOR_ITER_RANGE | 6,789,240 | 0.3% | 89.3% |
| CALL_BUILTIN_CLASS CALL_LEN | 6,789,200 | 0.3% | 89.6% |
| LOAD_FAST CALL_BUILTIN_CLASS | 6,451,440 | 0.3% | 89.9% |
| CALL_BUILTIN_CLASS CALL_BUILTIN_CLASS | 6,451,400 | 0.3% | 90.2% |
| GET_ITER FOR_ITER_RANGE | 6,451,240 | 0.3% | 90.5% |
| BINARY_SLICE GET_ITER | 6,451,200 | 0.3% | 90.8% |
| LOAD_CONST LOAD_FAST | 6,451,200 | 0.3% | 91.1% |
| LOAD_FAST BINARY_SLICE | 6,451,200 | 0.3% | 91.4% |
| STORE_DEREF LOAD_FAST | 6,451,200 | 0.3% | 91.7% |
| SWAP COPY | 6,451,200 | 0.3% | 92.0% |
| FOR_ITER_LIST RETURN_CONST | 6,451,200 | 0.3% | 92.3% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,451,180 | 0.3% | 92.6% |
| YIELD_VALUE STORE_DEREF | 6,451,180 | 0.3% | 92.9% |
| CALL_BUILTIN_CLASS GET_ITER | 6,451,180 | 0.3% | 93.2% |
| CALL_LEN SWAP | 6,451,180 | 0.3% | 93.5% |
| COPY COMPARE_OP_INT | 6,451,160 | 0.3% | 93.8% |
| LOAD_FAST FOR_ITER_LIST | 6,451,160 | 0.3% | 94.1% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 6,451,160 | 0.3% | 94.4% |
| CALL_TUPLE_1 YIELD_VALUE | 6,451,160 | 0.3% | 94.7% |
| FOR_ITER_GEN RESUME_CHECK | 6,451,160 | 0.3% | 95.0% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 6,451,160 | 0.3% | 95.3% |
| RETURN_GENERATOR CALL_TUPLE_1 | 6,451,120 | 0.3% | 95.6% |
| LOAD_FAST TO_BOOL_INT | 6,451,120 | 0.3% | 95.8% |
| BINARY_SUBSCR LOAD_FAST_LOAD_FAST | 6,451,040 | 0.3% | 96.1% |
| POP_TOP POP_TOP | 6,451,040 | 0.3% | 96.4% |
| POP_TOP JUMP_FORWARD | 6,451,040 | 0.3% | 96.7% |
| UNARY_NEGATIVE BINARY_SUBSCR | 6,451,040 | 0.3% | 97.0% |
| UNARY_NEGATIVE STORE_SUBSCR | 6,451,040 | 0.3% | 97.3% |
| JUMP_FORWARD LOAD_FAST | 6,451,040 | 0.3% | 97.6% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 6,451,040 | 0.3% | 97.9% |
| SWAP LOAD_FAST_LOAD_FAST | 6,451,040 | 0.3% | 98.2% |
| JUMP_BACKWARD LOAD_GLOBAL_BUILTIN | 6,451,020 | 0.3% | 98.5% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 6,451,020 | 0.3% | 98.8% |
| BINARY_SUBSCR_LIST_INT SWAP | 6,451,020 | 0.3% | 99.1% |
| STORE_SUBSCR LOAD_GLOBAL_BUILTIN | 6,451,000 | 0.3% | 99.4% |
| POP_JUMP_IF_FALSE POP_TOP | 6,113,120 | 0.3% | 99.7% |
| BINARY_OP_SUBTRACT_INT YIELD_VALUE | 2,704,620 | 0.1% | 99.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,084,960 | 38.7% |
| BINARY_OP_ADD_INT | 11,084,940 | 38.7% |
| LOAD_FAST | 6,451,200 | 22.5% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,084,960 | 38.7% |
| LOAD_FAST_LOAD_FAST | 11,084,960 | 38.7% |
| GET_ITER | 6,451,200 | 22.5% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,084,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,084,960 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 105,938,600 | 88.9% |
| POP_TOP | 13,240,660 | 11.1% |
| RESUME | 120 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 6,451,040 | 100.0% |
| BINARY_SUBSCR | 1,800 | 0.0% |
| BUILD_SLICE | 160 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,451,040 | 100.0% |
| BINARY_SUBSCR | 1,800 | 0.0% |
| STORE_FAST | 180 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 80 | 0.0% |
| BINARY_SUBSCR_TUPLE_INT | 80 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 160 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,789,360 | 34.5% |
| BINARY_SLICE | 6,451,200 | 32.8% |
| CALL_BUILTIN_CLASS | 6,451,180 | 32.8% |
| RETURN_GENERATOR | 160 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 13,240,320 | 67.2% |
| FOR_ITER_RANGE | 6,451,240 | 32.8% |
| CALL | 160 | 0.0% |
| FOR_ITER_GEN | 140 | 0.0% |
| FOR_ITER | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 105,938,580 | 88.9% |
| RETURN_CONST | 13,240,800 | 11.1% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 100.0% |


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
| RESUME_CHECK | 112,389,620 | 81.3% |
| CACHE | 13,240,660 | 9.6% |
| POP_TOP | 6,451,040 | 4.7% |
| POP_JUMP_IF_FALSE | 6,113,120 | 4.4% |
| CALL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,051,840 | 81.1% |
| RESUME_CHECK | 13,240,680 | 9.6% |
| POP_TOP | 6,451,040 | 4.7% |
| JUMP_FORWARD | 6,451,040 | 4.7% |
| LOAD_FAST | 160 | 0.0% |


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

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 13,240,480 | 100.0% |
| MAKE_CELL | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 6,789,320 | 51.3% |
| CALL_TUPLE_1 | 6,451,120 | 48.7% |
| CALL | 200 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNARY_NEGATIVE | 6,451,040 | 100.0% |
| STORE_SUBSCR | 1,760 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| SWAP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,451,000 | 100.0% |
| STORE_SUBSCR | 1,760 | 0.0% |
| STORE_SUBSCR_LIST_INT | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 50.0% |
| TO_BOOL_INT | 40 | 50.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,902,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 6,451,040 | 50.0% |
| STORE_SUBSCR | 6,451,040 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 11,084,960 | 100.0% |
| BINARY_OP | 2,900 | 0.0% |
| LOAD_CONST | 200 | 0.0% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 11,084,980 | 100.0% |
| BINARY_OP | 2,900 | 0.0% |
| BINARY_OP_ADD_INT | 100 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 80 | 0.0% |
| LOAD_CONST | 40 | 0.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 160 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,240,480 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 400 | 28.2% |
| LOAD_FAST | 280 | 19.7% |
| RETURN_GENERATOR | 200 | 14.1% |
| CALL | 200 | 14.1% |
| GET_ITER | 160 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 260 | 18.3% |
| CALL_BUILTIN_CLASS | 220 | 15.5% |
| CALL | 200 | 14.1% |
| STORE_FAST | 160 | 11.3% |
| CALL_PY_EXACT_ARGS | 100 | 7.0% |


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
| LOAD_CONST | 80 | 50.0% |
| COPY | 40 | 25.0% |
| CALL | 20 | 12.5% |
| CALL_LEN | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 80 | 50.0% |
| POP_JUMP_IF_FALSE | 60 | 37.5% |
| POP_JUMP_IF_TRUE | 20 | 12.5% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 17,536,000 | 42.2% |
| LOAD_FAST_LOAD_FAST | 17,536,000 | 42.2% |
| SWAP | 6,451,200 | 15.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 17,536,000 | 42.2% |
| BINARY_SUBSCR_LIST_INT | 17,535,960 | 42.2% |
| COMPARE_OP_INT | 6,451,160 | 15.5% |
| BINARY_SUBSCR | 40 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 13,240,400 | 100.0% |
| CALL | 80 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 13,240,480 | 100.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 140 | 50.0% |
| LOAD_FAST | 80 | 28.6% |
| GET_ITER | 60 | 21.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 42.9% |
| FOR_ITER_RANGE | 80 | 28.6% |
| FOR_ITER_LIST | 40 | 14.3% |
| STORE_DEREF | 20 | 7.1% |
| FOR_ITER_GEN | 20 | 7.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 112,051,840 | 86.3% |
| STORE_SUBSCR_LIST_INT | 11,084,940 | 8.5% |
| POP_JUMP_IF_FALSE | 6,451,040 | 5.0% |
| POP_JUMP_IF_TRUE | 323,360 | 0.2% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 65,399,280 | 50.3% |
| FOR_ITER_LIST | 51,609,560 | 39.7% |
| FOR_ITER_GEN | 6,451,180 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 6,451,020 | 5.0% |
| FOR_ITER | 140 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,451,040 | 99.8% |
| POP_JUMP_IF_TRUE | 14,720 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,040 | 99.8% |
| LOAD_DEREF | 14,720 | 0.2% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 40 | 50.0% |
| PUSH_NULL | 20 | 25.0% |
| STORE_FAST | 20 | 25.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 35,071,960 | 35.4% |
| LOAD_FAST_LOAD_FAST | 22,169,920 | 22.4% |
| LOAD_FAST | 17,536,400 | 17.7% |
| BUILD_TUPLE | 13,240,480 | 13.4% |
| BINARY_OP_ADD_INT | 11,084,940 | 11.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 22,170,080 | 22.4% |
| COMPARE_OP_INT | 17,536,000 | 17.7% |
| BINARY_OP_SUBTRACT_INT | 17,535,960 | 17.7% |
| MAKE_FUNCTION | 13,240,480 | 13.4% |
| BINARY_SLICE | 11,084,960 | 11.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 105,923,920 | 100.0% |
| JUMP_FORWARD | 14,720 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 140 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 105,923,840 | 100.0% |
| YIELD_VALUE | 14,720 | 0.0% |
| CALL_LEN | 120 | 0.0% |
| PUSH_NULL | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 105,923,840 | 44.7% |
| BINARY_SUBSCR_TUPLE_INT | 54,314,200 | 22.9% |
| LOAD_GLOBAL_BUILTIN | 19,692,060 | 8.3% |
| SET_FUNCTION_ATTRIBUTE | 13,240,480 | 5.6% |
| RESUME_CHECK | 13,240,400 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 105,923,680 | 44.7% |
| BINARY_OP_ADD_INT | 51,609,560 | 21.8% |
| LOAD_CONST | 17,536,400 | 7.4% |
| BUILD_TUPLE | 13,240,480 | 5.6% |
| GET_ITER | 6,789,360 | 2.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,987,040 | 19.5% |
| STORE_SUBSCR_LIST_INT | 23,987,000 | 19.5% |
| POP_JUMP_IF_FALSE | 17,536,000 | 14.3% |
| BINARY_OP | 11,084,980 | 9.0% |
| BINARY_SLICE | 11,084,960 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 30,437,960 | 24.8% |
| LOAD_CONST | 22,169,920 | 18.1% |
| COPY | 17,536,000 | 14.3% |
| STORE_SUBSCR_LIST_INT | 17,535,920 | 14.3% |
| UNARY_NEGATIVE | 12,902,080 | 10.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 19.0% |
| LOAD_GLOBAL | 120 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 120 | 14.3% |
| POP_JUMP_IF_FALSE | 100 | 11.9% |
| RESUME | 80 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 340 | 40.5% |
| LOAD_FAST | 220 | 26.2% |
| LOAD_GLOBAL | 120 | 14.3% |
| LOAD_GLOBAL_MODULE | 80 | 9.5% |
| LOAD_ATTR | 40 | 4.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140 | 43.8% |
| CALL_PY_WITH_DEFAULTS | 140 | 43.8% |
| CALL | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 320 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 23,987,220 | 78.8% |
| TO_BOOL_INT | 6,451,160 | 21.2% |
| COMPARE_OP | 60 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 17,536,000 | 57.6% |
| JUMP_BACKWARD | 6,451,040 | 21.2% |
| POP_TOP | 6,113,120 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 338,220 | 1.1% |
| LOAD_GLOBAL | 100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 338,060 | 100.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 323,360 | 95.6% |
| JUMP_FORWARD | 14,720 | 4.4% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 6,789,440 | 51.3% |
| FOR_ITER_LIST | 6,451,200 | 48.7% |
| END_FOR | 160 | 0.0% |
| POP_TOP | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 13,240,800 | 100.0% |
| END_FOR | 160 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 13,240,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,240,480 | 100.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,451,180 | 100.0% |
| CALL_TUPLE_1 | 140 | 0.0% |
| CALL | 20 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,200 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 71,850,320 | 55.3% |
| FOR_ITER_LIST | 51,609,560 | 39.7% |
| BINARY_SUBSCR_LIST_INT | 6,451,020 | 5.0% |
| CALL_BUILTIN_CLASS | 340 | 0.0% |
| BINARY_SUBSCR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 105,923,920 | 81.5% |
| LOAD_FAST_LOAD_FAST | 23,987,040 | 18.5% |
| LOAD_FAST | 640 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 360 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 17,536,000 | 36.6% |
| BINARY_OP_SUBTRACT_INT | 17,535,980 | 36.6% |
| CALL_LEN | 6,451,180 | 13.4% |
| BINARY_SUBSCR_LIST_INT | 6,451,020 | 13.4% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 17,536,000 | 36.6% |
| STORE_SUBSCR_LIST_INT | 17,535,960 | 36.6% |
| COPY | 6,451,200 | 13.4% |
| LOAD_FAST_LOAD_FAST | 6,451,040 | 13.4% |
| STORE_SUBSCR | 40 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 51,609,580 | 45.9% |
| BINARY_SUBSCR_TUPLE_INT | 51,609,560 | 45.9% |
| CALL_TUPLE_1 | 6,451,160 | 5.7% |
| BINARY_OP_SUBTRACT_INT | 2,704,620 | 2.4% |
| LOAD_DEREF | 14,720 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 105,938,580 | 94.3% |
| STORE_DEREF | 6,451,180 | 5.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 120 | 40.0% |
| POP_TOP | 120 | 40.0% |
| FOR_ITER_GEN | 40 | 13.3% |
| COPY_FREE_VARS | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 140 | 46.7% |
| LOAD_FAST | 80 | 26.7% |
| LOAD_GLOBAL | 80 | 26.7% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,609,560 | 70.0% |
| LOAD_CONST | 22,170,080 | 30.0% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 51,609,580 | 70.0% |
| BINARY_SLICE | 11,084,940 | 15.0% |
| LOAD_CONST | 11,084,940 | 15.0% |
| LOAD_FAST | 140 | 0.0% |
| CALL_BUILTIN_CLASS | 120 | 0.0% |


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
| LOAD_CONST | 17,535,960 | 56.0% |
| LOAD_FAST_LOAD_FAST | 11,085,040 | 35.4% |
| LOAD_FAST | 2,704,600 | 8.6% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 17,535,980 | 56.0% |
| LOAD_FAST_LOAD_FAST | 11,084,940 | 35.4% |
| YIELD_VALUE | 2,704,620 | 8.6% |
| LOAD_CONST | 140 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 30,437,960 | 63.4% |
| COPY | 17,535,960 | 36.6% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 35,071,960 | 73.1% |
| STORE_FAST | 6,451,020 | 13.4% |
| SWAP | 6,451,020 | 13.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 105,923,680 | 100.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,314,200 | 51.3% |
| YIELD_VALUE | 51,609,560 | 48.7% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 6,789,320 | 34.5% |
| LOAD_FAST | 6,451,440 | 32.8% |
| CALL_BUILTIN_CLASS | 6,451,400 | 32.8% |
| CALL | 220 | 0.0% |
| BINARY_OP_ADD_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 6,789,200 | 34.5% |
| CALL_BUILTIN_CLASS | 6,451,400 | 32.8% |
| GET_ITER | 6,451,180 | 32.8% |
| STORE_FAST | 340 | 0.0% |
| POP_TOP | 140 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 6,789,200 | 100.0% |
| LOAD_DEREF | 120 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 6,451,180 | 95.0% |
| COMPARE_OP_INT | 338,040 | 5.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 13,240,320 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 13,240,400 | 100.0% |
| MAKE_CELL | 140 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| CALL | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 140 | 100.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 6,451,120 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,451,160 | 100.0% |
| STORE_DEREF | 140 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,536,000 | 72.1% |
| COPY | 6,451,160 | 26.5% |
| CALL_LEN | 338,040 | 1.4% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 23,987,220 | 98.6% |
| POP_JUMP_IF_TRUE | 338,060 | 1.4% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,451,180 | 100.0% |
| GET_ITER | 140 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,451,160 | 100.0% |
| POP_TOP | 140 | 0.0% |
| RESUME | 40 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 51,609,560 | 88.9% |
| LOAD_FAST | 6,451,160 | 11.1% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 51,609,560 | 88.9% |
| RETURN_CONST | 6,451,200 | 11.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 65,399,280 | 83.2% |
| LOAD_FAST | 6,789,240 | 8.6% |
| GET_ITER | 6,451,240 | 8.2% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 71,850,320 | 91.4% |
| RETURN_CONST | 6,789,440 | 8.6% |
| LOAD_FAST | 80 | 0.0% |


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
| LOAD_GLOBAL_BUILTIN | 13,240,600 | 40.2% |
| LOAD_FAST | 6,451,160 | 19.6% |
| JUMP_BACKWARD | 6,451,020 | 19.6% |
| STORE_SUBSCR | 6,451,000 | 19.6% |
| POP_JUMP_IF_FALSE | 338,220 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,692,060 | 59.8% |
| LOAD_GLOBAL_BUILTIN | 13,240,600 | 40.2% |
| LOAD_DEREF | 140 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_GLOBAL | 120 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 30.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 30.0% |
| LOAD_GLOBAL | 80 | 20.0% |
| RETURN_VALUE | 40 | 10.0% |
| RESUME_CHECK | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 70.0% |
| LOAD_ATTR_MODULE | 80 | 20.0% |
| LOAD_ATTR | 40 | 10.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 105,938,600 | 84.3% |
| POP_TOP | 13,240,680 | 10.5% |
| FOR_ITER_GEN | 6,451,160 | 5.1% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 112,389,620 | 89.5% |
| LOAD_FAST | 13,240,400 | 10.5% |
| LOAD_GLOBAL_BUILTIN | 360 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 17,535,960 | 50.0% |
| LOAD_FAST_LOAD_FAST | 17,535,920 | 50.0% |
| STORE_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 23,987,000 | 68.4% |
| JUMP_BACKWARD | 11,084,940 | 31.6% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,451,120 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,451,160 | 100.0% |


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
|     deferred | 11,085,160 | 9.5% |
|          hit | 105,105,480 | 90.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 6.5% |
| Failure | 2,900 | 93.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 2,900 | 100.0% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,451,360 | 4.0% |
|          hit | 153,897,760 | 96.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 8.2% |
| Failure | 1,800 | 91.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 1,760 | 97.8% |
| list slice | 40 | 2.2% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 860 | 0.0% |
|          hit | 46,173,860 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 82.1% |
| Failure | 100 | 17.9% |

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
|     deferred | 80 | 0.0% |
|          hit | 24,325,280 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 140 | 0.0% |
|          hit | 143,151,940 | 100.0% |

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
|     deferred | 40 | 20.0% |
|          hit | 120 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 420 | 0.0% |
|          hit | 32,933,580 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,451,100 | 15.5% |
|          hit | 35,071,940 | 84.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 3.3% |
| Failure | 1,760 | 96.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 1,760 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 6,451,160 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,408,688,480 | 64.7% |
| Not specialized | 94,480,160 | 4.3% |
| Specialized hits | 672,741,560 | 30.9% |
| Specialized misses | 60 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 11,085,160 | 46.2% |
| BINARY_SUBSCR | 6,451,360 | 26.9% |
| STORE_SUBSCR | 6,451,100 | 26.9% |
| CALL | 860 | 0.0% |
| LOAD_GLOBAL | 420 | 0.0% |
| FOR_ITER | 140 | 0.0% |
| COMPARE_OP | 80 | 0.0% |
| TO_BOOL | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| RESUME | 60 | 50.0% |
| RESUME_CHECK | 60 | 50.0% |
| CACHE | 0 | 0.0% |
| END_FOR | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |
| INTERPRETER_EXIT | 0 | 0.0% |
| MAKE_FUNCTION | 0 | 0.0% |
| NOP | 0 | 0.0% |
| POP_TOP | 0 | 0.0% |
| PUSH_NULL | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 119,179,380 | 85.8% |
| Calls to Python functions inlined | 19,692,220 | 14.2% |
| Calls via PyEval_EvalFrame (total) | 119,179,380 | 85.8% |
| Calls via PyEval_EvalFrame (vector) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 119,179,220 | 85.8% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 13,240,680 | 9.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 52,947,040 | 32.1% |
| Frees to freelist | 52,988,020 |  |
| Allocations | 111,961,100 | 67.9% |
| Allocations to 512 bytes | 105,640,620 | 64.1% |
| Allocations to 4 kbytes | 6,320,480 | 3.8% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 111,923,244 |  |
| New values | 0 |  |
| Interpreter increfs | 334,617,160 | 75.3% |
| Interpreter decrefs | 479,546,260 | 78.7% |
| Increfs | 109,950,320 | 24.7% |
| Decrefs | 130,065,284 | 21.3% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 21 |  |
| Method cache misses | 19 |  |
| Method cache collisions | 38 |  |
| Method cache dunder hits | 12,902,540 |  |
| Method cache dunder misses | 20 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 60 | 1,920 | 131,320 |
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
