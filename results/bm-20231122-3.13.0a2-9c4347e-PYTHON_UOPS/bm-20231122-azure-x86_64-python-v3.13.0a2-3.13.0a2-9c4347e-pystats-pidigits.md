
# Pystats results

- benchmark: pidigits
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 10,733,440 | 16.9% | 16.9% |  |
| BINARY_OP_MULTIPLY_INT | 8,820,160 | 13.9% | 30.7% |  |
| LOAD_FAST_LOAD_FAST | 7,598,800 | 11.9% | 42.6% |  |
| BINARY_OP_ADD_INT | 5,897,060 | 9.3% | 51.9% |  |
| STORE_FAST_STORE_FAST | 5,526,400 | 8.7% | 60.6% |  |
| LOAD_CONST | 4,675,920 | 7.3% | 67.9% |  |
| RESUME_CHECK | 2,763,280 | 4.3% | 72.3% |  |
| UNPACK_SEQUENCE_TUPLE | 2,763,140 | 4.3% | 76.6% |  |
| RETURN_VALUE | 2,603,440 | 4.1% | 80.7% |  |
| LOAD_GLOBAL_MODULE | 2,072,640 | 3.3% | 83.9% |  |
| CALL_PY_EXACT_ARGS | 2,072,400 | 3.3% | 87.2% |  |
| BINARY_OP | 1,382,920 | 2.2% | 89.4% |  |
| STORE_FAST | 1,382,080 | 2.2% | 91.5% |  |
| BUILD_TUPLE | 1,381,600 | 2.2% | 93.7% |  |
| INTERPRETER_EXIT | 690,880 | 1.1% | 94.8% |  |
| POP_JUMP_IF_FALSE | 690,880 | 1.1% | 95.9% |  |
| COMPARE_OP_INT | 690,820 | 1.1% | 97.0% |  |
| JUMP_BACKWARD | 545,520 | 0.9% | 97.8% |  |
| LOAD_GLOBAL_BUILTIN | 530,900 | 0.8% | 98.7% |  |
| CALL_BUILTIN_FAST | 530,780 | 0.8% | 99.5% |  |
| POP_TOP | 160,160 | 0.3% | 99.7% |  |
| YIELD_VALUE | 160,000 | 0.3% | 100.0% |  |
| CALL | 1,040 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 600 | 0.0% | 100.0% |  |
| PUSH_NULL | 400 | 0.0% | 100.0% |  |
| NOP | 160 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| RESUME | 160 | 0.0% | 100.0% |  |
| COMPARE_OP | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 80 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LOAD_ATTR | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_INT | 7,598,440 | 11.9% | 11.9% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 2,763,200 | 4.3% | 16.3% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST | 2,763,160 | 4.3% | 20.6% |
| BINARY_OP_ADD_INT LOAD_FAST_LOAD_FAST | 2,763,140 | 4.3% | 25.0% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 2,763,140 | 4.3% | 29.3% |
| LOAD_FAST BINARY_OP_ADD_INT | 2,763,120 | 4.3% | 33.6% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST_LOAD_FAST | 2,763,120 | 4.3% | 38.0% |
| LOAD_FAST UNPACK_SEQUENCE_TUPLE | 2,763,080 | 4.3% | 42.3% |
| RESUME_CHECK LOAD_FAST | 2,603,140 | 4.1% | 46.4% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 2,072,400 | 3.3% | 49.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 2,072,340 | 3.3% | 52.9% |
| BINARY_OP_MULTIPLY_INT BINARY_OP_ADD_INT | 2,072,280 | 3.3% | 56.2% |
| LOAD_FAST LOAD_CONST | 1,912,480 | 3.0% | 59.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,912,300 | 3.0% | 62.2% |
| RETURN_VALUE STORE_FAST | 1,381,680 | 2.2% | 64.3% |
| BINARY_OP RETURN_VALUE | 1,381,600 | 2.2% | 66.5% |
| BINARY_OP_ADD_INT BINARY_OP | 1,381,580 | 2.2% | 68.7% |
| LOAD_CONST CALL_PY_EXACT_ARGS | 1,381,440 | 2.2% | 70.8% |
| BUILD_TUPLE RETURN_VALUE | 1,221,600 | 1.9% | 72.8% |
| LOAD_CONST LOAD_FAST | 1,221,600 | 1.9% | 74.7% |
| BINARY_OP_ADD_INT BUILD_TUPLE | 1,221,560 | 1.9% | 76.6% |
| BINARY_OP_MULTIPLY_INT LOAD_CONST | 1,221,540 | 1.9% | 78.5% |
| LOAD_FAST BINARY_OP_MULTIPLY_INT | 1,221,480 | 1.9% | 80.4% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,061,520 | 1.7% | 82.1% |
| STORE_FAST LOAD_FAST | 851,040 | 1.3% | 83.4% |
| LOAD_CONST LOAD_CONST | 850,800 | 1.3% | 84.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 690,820 | 1.1% | 85.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 690,800 | 1.1% | 86.9% |
| CACHE RESUME_CHECK | 690,740 | 1.1% | 88.0% |
| RETURN_VALUE COMPARE_OP_INT | 690,720 | 1.1% | 89.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 690,720 | 1.1% | 90.2% |
| JUMP_BACKWARD LOAD_GLOBAL_MODULE | 545,500 | 0.9% | 91.1% |
| RETURN_VALUE INTERPRETER_EXIT | 530,880 | 0.8% | 91.9% |
| STORE_FAST LOAD_GLOBAL_MODULE | 530,800 | 0.8% | 92.7% |
| BINARY_OP_ADD_INT LOAD_CONST | 530,780 | 0.8% | 93.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 530,780 | 0.8% | 94.4% |
| LOAD_FAST CALL_BUILTIN_FAST | 530,760 | 0.8% | 95.2% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 530,760 | 0.8% | 96.1% |
| CALL_BUILTIN_FAST CALL_PY_EXACT_ARGS | 530,760 | 0.8% | 96.9% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 385,600 | 0.6% | 97.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 305,120 | 0.5% | 98.0% |
| LOAD_GLOBAL_MODULE LOAD_CONST | 160,040 | 0.3% | 98.2% |
| BUILD_TUPLE LOAD_FAST | 160,000 | 0.3% | 98.5% |
| LOAD_CONST BUILD_TUPLE | 160,000 | 0.3% | 98.7% |
| LOAD_FAST YIELD_VALUE | 160,000 | 0.3% | 99.0% |
| YIELD_VALUE INTERPRETER_EXIT | 160,000 | 0.3% | 99.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 159,960 | 0.3% | 99.5% |
| POP_TOP JUMP_BACKWARD | 159,920 | 0.3% | 99.7% |
| RESUME_CHECK POP_TOP | 159,900 | 0.3% | 100.0% |
| BINARY_OP BINARY_OP | 600 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 360 | 0.0% | 100.0% |
| PUSH_NULL CALL | 320 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_MULTIPLY_INT | 240 | 0.0% | 100.0% |
| LOAD_CONST CALL | 240 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 240 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 240 | 0.0% | 100.0% |
| CALL CALL | 220 | 0.0% | 100.0% |
| CALL POP_TOP | 160 | 0.0% | 100.0% |
| CALL CALL_PY_EXACT_ARGS | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL | 160 | 0.0% | 100.0% |
| BINARY_OP LOAD_FAST_LOAD_FAST | 140 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_INT | 140 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| LOAD_FAST LOAD_GLOBAL | 120 | 0.0% | 100.0% |
| LOAD_FAST UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 120 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS RETURN_VALUE | 120 | 0.0% | 100.0% |
| CACHE POP_TOP | 80 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| POP_TOP LOAD_FAST | 80 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 80 | 0.0% | 100.0% |
| RETURN_GENERATOR LOAD_FAST | 80 | 0.0% | 100.0% |
| RETURN_VALUE COMPARE_OP | 80 | 0.0% | 100.0% |
| BINARY_OP LOAD_CONST | 80 | 0.0% | 100.0% |
| CALL LOAD_FAST | 80 | 0.0% | 100.0% |
| CALL STORE_FAST | 80 | 0.0% | 100.0% |
| CALL RESUME_CHECK | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| LOAD_CONST MAKE_FUNCTION | 80 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP | 80 | 0.0% | 100.0% |
| LOAD_CONST STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 80 | 0.0% | 100.0% |
| LOAD_DEREF STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 80 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| STORE_FAST NOP | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_DEREF | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 80 | 0.0% | 100.0% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 80 | 0.0% | 100.0% |
| CACHE RESUME | 60 | 0.0% | 100.0% |
| NOP LOAD_GLOBAL_MODULE | 60 | 0.0% | 100.0% |
| POP_TOP RESUME_CHECK | 60 | 0.0% | 100.0% |
| CALL RESUME | 60 | 0.0% | 100.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 60 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 690,740 | 100.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 530,880 | 76.8% |
| YIELD_VALUE | 160,000 | 23.2% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 50.0% |
| LOAD_GLOBAL_MODULE | 60 | 37.5% |
| LOAD_GLOBAL | 20 | 12.5% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 159,900 | 99.8% |
| CALL | 160 | 0.1% |
| CACHE | 80 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 159,920 | 99.9% |
| NOP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 60.0% |
| LOAD_DEREF | 80 | 20.0% |
| LOAD_ATTR_MODULE | 60 | 15.0% |
| LOAD_ATTR | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 320 | 80.0% |
| LOAD_FAST | 80 | 20.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,381,600 | 53.1% |
| BUILD_TUPLE | 1,221,600 | 46.9% |
| CALL_BUILTIN_CLASS | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,381,680 | 53.1% |
| COMPARE_OP_INT | 690,720 | 26.5% |
| INTERPRETER_EXIT | 530,880 | 20.4% |
| COMPARE_OP | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,381,580 | 99.9% |
| BINARY_OP | 600 | 0.0% |
| LOAD_FAST_LOAD_FAST | 360 | 0.0% |
| LOAD_FAST | 240 | 0.0% |
| LOAD_CONST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,381,600 | 99.9% |
| BINARY_OP | 600 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 240 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| BINARY_OP_ADD_INT | 140 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,221,560 | 88.4% |
| LOAD_CONST | 160,000 | 11.6% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,221,600 | 88.4% |
| LOAD_FAST | 160,000 | 11.6% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 320 | 30.8% |
| LOAD_CONST | 240 | 23.1% |
| CALL | 220 | 21.2% |
| LOAD_FAST | 160 | 15.4% |
| LOAD_GLOBAL | 40 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 220 | 21.2% |
| POP_TOP | 160 | 15.4% |
| CALL_PY_EXACT_ARGS | 160 | 15.4% |
| CALL_BUILTIN_CLASS | 120 | 11.5% |
| LOAD_FAST | 80 | 7.7% |


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
| RETURN_VALUE | 80 | 66.7% |
| LOAD_CONST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 50.0% |
| COMPARE_OP_INT | 60 | 50.0% |


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

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 385,600 | 70.7% |
| POP_TOP | 159,920 | 29.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 545,500 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |


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
| LOAD_FAST | 1,912,480 | 40.9% |
| BINARY_OP_MULTIPLY_INT | 1,221,540 | 26.1% |
| LOAD_CONST | 850,800 | 18.2% |
| BINARY_OP_ADD_INT | 530,780 | 11.4% |
| LOAD_GLOBAL_MODULE | 160,040 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,381,440 | 29.5% |
| LOAD_FAST | 1,221,600 | 26.1% |
| BINARY_OP_ADD_INT | 1,061,520 | 22.7% |
| LOAD_CONST | 850,800 | 18.2% |
| BUILD_TUPLE | 160,000 | 3.4% |


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
| BINARY_OP_MULTIPLY_INT | 2,763,160 | 25.7% |
| RESUME_CHECK | 2,603,140 | 24.3% |
| LOAD_GLOBAL_MODULE | 1,912,300 | 17.8% |
| LOAD_CONST | 1,221,600 | 11.4% |
| STORE_FAST | 851,040 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,763,120 | 25.7% |
| UNPACK_SEQUENCE_TUPLE | 2,763,080 | 25.7% |
| LOAD_CONST | 1,912,480 | 17.8% |
| BINARY_OP_MULTIPLY_INT | 1,221,480 | 11.4% |
| LOAD_GLOBAL_MODULE | 690,720 | 6.4% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,763,140 | 36.4% |
| BINARY_OP_MULTIPLY_INT | 2,763,120 | 36.4% |
| STORE_FAST_STORE_FAST | 2,072,400 | 27.3% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 7,598,440 | 100.0% |
| BINARY_OP | 360 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 20.0% |
| POP_JUMP_IF_FALSE | 80 | 13.3% |
| STORE_FAST | 80 | 13.3% |
| RESUME | 60 | 10.0% |
| RESUME_CHECK | 60 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 240 | 40.0% |
| LOAD_FAST | 120 | 20.0% |
| LOAD_CONST | 60 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 60 | 10.0% |
| CALL | 40 | 6.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 690,820 | 100.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 385,600 | 55.8% |
| LOAD_GLOBAL_MODULE | 305,120 | 44.2% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,381,680 | 100.0% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 851,040 | 61.6% |
| LOAD_GLOBAL_MODULE | 530,800 | 38.4% |
| NOP | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,763,200 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 2,763,140 | 50.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,763,200 | 50.0% |
| LOAD_FAST_LOAD_FAST | 2,072,400 | 37.5% |
| LOAD_FAST | 690,800 | 12.5% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 60 | 50.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 160,000 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 60 | 37.5% |
| CALL | 60 | 37.5% |
| POP_TOP | 20 | 12.5% |
| COPY_FREE_VARS | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 37.5% |
| LOAD_GLOBAL | 60 | 37.5% |
| POP_TOP | 20 | 12.5% |
| LOAD_CONST | 20 | 12.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,763,120 | 46.9% |
| BINARY_OP_MULTIPLY_INT | 2,072,280 | 35.1% |
| LOAD_CONST | 1,061,520 | 18.0% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,763,140 | 46.9% |
| BINARY_OP | 1,381,580 | 23.4% |
| BUILD_TUPLE | 1,221,560 | 20.7% |
| LOAD_CONST | 530,780 | 9.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 7,598,440 | 86.1% |
| LOAD_FAST | 1,221,480 | 13.8% |
| BINARY_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,763,160 | 31.3% |
| LOAD_FAST_LOAD_FAST | 2,763,120 | 31.3% |
| BINARY_OP_ADD_INT | 2,072,280 | 23.5% |
| LOAD_CONST | 1,221,540 | 13.8% |
| BINARY_OP | 60 | 0.0% |


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

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 120 | 100.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 530,760 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 530,760 | 100.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,381,440 | 66.7% |
| CALL_BUILTIN_FAST | 530,760 | 25.6% |
| LOAD_FAST | 159,960 | 7.7% |
| CALL | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,072,340 | 100.0% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 690,720 | 100.0% |
| COMPARE_OP | 60 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 690,820 | 100.0% |


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
| LOAD_FAST | 530,760 | 100.0% |
| RESUME_CHECK | 80 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 530,780 | 100.0% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 690,720 | 33.3% |
| JUMP_BACKWARD | 545,500 | 26.3% |
| STORE_FAST | 530,800 | 25.6% |
| POP_JUMP_IF_FALSE | 305,120 | 14.7% |
| LOAD_GLOBAL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,912,300 | 92.3% |
| LOAD_CONST | 160,040 | 7.7% |
| CALL_PY_EXACT_ARGS | 80 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,072,340 | 75.0% |
| CACHE | 690,740 | 25.0% |
| CALL | 80 | 0.0% |
| POP_TOP | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,603,140 | 94.2% |
| POP_TOP | 159,900 | 5.8% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,763,080 | 100.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,763,140 | 100.0% |


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
|     deferred | 1,382,000 | 8.6% |
|          hit | 14,717,280 | 91.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 400 | 43.5% |
| Failure | 520 | 56.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 520 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 700 | 0.0% |
|          hit | 2,603,300 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 64.7% |
| Failure | 120 | 35.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 50.0% |
| class no vectorcall | 40 | 33.3% |
| other | 20 | 16.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 690,820 | 100.0% |

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
|     deferred | 300 | 0.0% |
|          hit | 2,603,540 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 2,763,140 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 35,459,440 | 55.7% |
| Not specialized | 2,075,760 | 3.3% |
| Specialized hits | 26,141,480 | 41.1% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 1,382,000 | 99.9% |
| CALL | 700 | 0.1% |
| LOAD_GLOBAL | 300 | 0.0% |
| COMPARE_OP | 60 | 0.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| CACHE | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |


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
| Calls to PyEval_EvalDefault | 690,880 | 25.0% |
| Calls to Python functions inlined | 2,072,640 | 75.0% |
| Calls via PyEval_EvalFrame (total) | 690,880 | 25.0% |
| Calls via PyEval_EvalFrame (vector) | 530,880 | 19.2% |
| Calls via PyEval_EvalFrame (generator) | 160,000 | 5.8% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 530,880 | 19.2% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 2,072,400 | 75.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 1,382,000 | 8.5% |
| Frees to freelist | 1,382,020 |  |
| Allocations | 14,856,640 | 91.5% |
| Allocations to 512 bytes | 4,729,040 | 29.1% |
| Allocations to 4 kbytes | 3,817,120 | 23.5% |
| Allocations over 4 kbytes | 6,310,480 | 38.9% |
| Frees | 14,856,540 |  |
| New values | 0 |  |
| Interpreter increfs | 32,236,840 | 99.7% |
| Interpreter decrefs | 40,354,320 | 83.1% |
| Increfs | 101,840 | 0.3% |
| Decrefs | 8,222,847 | 16.9% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 20 |  |
| Method cache misses | 20 |  |
| Method cache collisions | 27 |  |
| Method cache dunder hits | 60 |  |
| Method cache dunder misses | 20 |  |


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
