
# Pystats results

- benchmark: pidigits
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_CONST | 3,296,560 | 20.7% | 20.7% |  |
| LOAD_FAST | 2,406,000 | 15.1% | 35.8% |  |
| BINARY_OP_MULTIPLY_INT | 2,350,880 | 14.8% | 50.6% |  |
| BINARY_OP_ADD_INT | 1,548,100 | 9.7% | 60.4% |  |
| LOAD_FAST_LOAD_FAST | 1,129,520 | 7.1% | 67.5% |  |
| RESUME_CHECK | 853,840 | 5.4% | 72.8% |  |
| BUILD_TUPLE | 851,520 | 5.4% | 78.2% |  |
| RETURN_VALUE | 694,000 | 4.4% | 82.5% |  |
| INTERPRETER_EXIT | 690,880 | 4.3% | 86.9% |  |
| STORE_FAST_STORE_FAST | 647,360 | 4.1% | 91.0% |  |
| UNPACK_SEQUENCE_TUPLE | 323,620 | 2.0% | 93.0% |  |
| ENTER_EXECUTOR | 294,840 | 1.9% | 94.8% |  |
| LOAD_GLOBAL_MODULE | 163,200 | 1.0% | 95.9% |  |
| CALL_PY_EXACT_ARGS | 162,960 | 1.0% | 96.9% |  |
| STORE_FAST | 162,320 | 1.0% | 97.9% |  |
| POP_TOP | 160,160 | 1.0% | 98.9% |  |
| YIELD_VALUE | 160,000 | 1.0% | 99.9% |  |
| BINARY_OP | 3,140 | 0.0% | 99.9% |  |
| POP_JUMP_IF_FALSE | 1,200 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 1,140 | 0.0% | 100.0% |  |
| CALL | 1,040 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_BUILTIN | 820 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 700 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 680 | 0.0% | 100.0% |  |
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
| LOAD_CONST LOAD_FAST | 1,221,600 | 7.7% | 7.7% |
| BINARY_OP_MULTIPLY_INT LOAD_CONST | 1,221,540 | 7.7% | 15.4% |
| LOAD_FAST BINARY_OP_MULTIPLY_INT | 1,221,480 | 7.7% | 23.0% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_INT | 1,129,160 | 7.1% | 30.1% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,061,520 | 6.7% | 36.8% |
| LOAD_CONST LOAD_CONST | 850,800 | 5.3% | 42.2% |
| RESUME_CHECK LOAD_FAST | 693,700 | 4.4% | 46.5% |
| BUILD_TUPLE RETURN_VALUE | 691,520 | 4.3% | 50.9% |
| BINARY_OP_ADD_INT BUILD_TUPLE | 691,480 | 4.3% | 55.2% |
| CACHE RESUME_CHECK | 690,740 | 4.3% | 59.6% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST_LOAD_FAST | 642,800 | 4.0% | 63.6% |
| LOAD_FAST LOAD_CONST | 533,120 | 3.4% | 66.9% |
| RETURN_VALUE INTERPRETER_EXIT | 530,880 | 3.3% | 70.3% |
| BINARY_OP_ADD_INT LOAD_CONST | 530,780 | 3.3% | 73.6% |
| BINARY_OP_MULTIPLY_INT BINARY_OP_ADD_INT | 482,040 | 3.0% | 76.7% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 323,680 | 2.0% | 78.7% |
| BINARY_OP_ADD_INT LOAD_FAST_LOAD_FAST | 323,620 | 2.0% | 80.7% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 323,620 | 2.0% | 82.8% |
| LOAD_FAST UNPACK_SEQUENCE_TUPLE | 323,560 | 2.0% | 84.8% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 162,960 | 1.0% | 85.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 162,900 | 1.0% | 86.8% |
| RETURN_VALUE STORE_FAST | 161,920 | 1.0% | 87.9% |
| STORE_FAST LOAD_FAST | 161,360 | 1.0% | 88.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 160,720 | 1.0% | 89.9% |
| LOAD_GLOBAL_MODULE LOAD_CONST | 160,040 | 1.0% | 90.9% |
| BUILD_TUPLE LOAD_FAST | 160,000 | 1.0% | 91.9% |
| LOAD_CONST BUILD_TUPLE | 160,000 | 1.0% | 92.9% |
| LOAD_FAST YIELD_VALUE | 160,000 | 1.0% | 93.9% |
| YIELD_VALUE INTERPRETER_EXIT | 160,000 | 1.0% | 94.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 159,960 | 1.0% | 95.9% |
| RESUME_CHECK POP_TOP | 159,900 | 1.0% | 96.9% |
| ENTER_EXECUTOR LOAD_GLOBAL_MODULE | 159,780 | 1.0% | 97.9% |
| POP_TOP ENTER_EXECUTOR | 159,580 | 1.0% | 98.9% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 135,060 | 0.8% | 99.8% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST | 4,440 | 0.0% | 99.8% |
| LOAD_FAST BINARY_OP_ADD_INT | 4,400 | 0.0% | 99.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,860 | 0.0% | 99.9% |
| BINARY_OP RETURN_VALUE | 2,240 | 0.0% | 99.9% |
| BINARY_OP_ADD_INT BINARY_OP | 2,220 | 0.0% | 99.9% |
| LOAD_CONST CALL_PY_EXACT_ARGS | 2,080 | 0.0% | 99.9% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,140 | 0.0% | 99.9% |
| RETURN_VALUE COMPARE_OP_INT | 1,040 | 0.0% | 99.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,040 | 0.0% | 99.9% |
| STORE_FAST LOAD_GLOBAL_MODULE | 720 | 0.0% | 99.9% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 700 | 0.0% | 99.9% |
| LOAD_FAST CALL_BUILTIN_FAST | 680 | 0.0% | 99.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 680 | 0.0% | 99.9% |
| CALL_BUILTIN_FAST CALL_PY_EXACT_ARGS | 680 | 0.0% | 99.9% |
| JUMP_BACKWARD LOAD_GLOBAL_MODULE | 620 | 0.0% | 99.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 540 | 0.0% | 99.9% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 360 | 0.0% | 99.9% |
| POP_TOP JUMP_BACKWARD | 340 | 0.0% | 99.9% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 340 | 0.0% | 99.9% |
| PUSH_NULL CALL | 320 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_MULTIPLY_INT | 240 | 0.0% | 100.0% |
| LOAD_CONST CALL | 240 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 240 | 0.0% | 100.0% |
| LOAD_FAST BINARY_OP | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 240 | 0.0% | 100.0% |
| CALL CALL | 220 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 180 | 0.0% | 100.0% |
| CALL POP_TOP | 160 | 0.0% | 100.0% |
| CALL CALL_PY_EXACT_ARGS | 160 | 0.0% | 100.0% |
| LOAD_FAST CALL | 160 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 160 | 0.0% | 100.0% |
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
| ENTER_EXECUTOR | 159,580 | 99.6% |
| JUMP_BACKWARD | 340 | 0.2% |
| NOP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |


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
| BUILD_TUPLE | 691,520 | 99.6% |
| BINARY_OP | 2,240 | 0.3% |
| CALL_BUILTIN_CLASS | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 530,880 | 76.5% |
| STORE_FAST | 161,920 | 23.3% |
| COMPARE_OP_INT | 1,040 | 0.1% |
| COMPARE_OP | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,220 | 70.7% |
| LOAD_FAST_LOAD_FAST | 360 | 11.5% |
| LOAD_FAST | 240 | 7.6% |
| BINARY_OP | 180 | 5.7% |
| LOAD_CONST | 80 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,240 | 71.3% |
| BINARY_OP_MULTIPLY_INT | 240 | 7.6% |
| BINARY_OP | 180 | 5.7% |
| LOAD_FAST_LOAD_FAST | 140 | 4.5% |
| BINARY_OP_ADD_INT | 140 | 4.5% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 691,480 | 81.2% |
| LOAD_CONST | 160,000 | 18.8% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 691,520 | 81.2% |
| LOAD_FAST | 160,000 | 18.8% |


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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 159,580 | 54.1% |
| ENTER_EXECUTOR | 135,060 | 45.8% |
| POP_JUMP_IF_FALSE | 160 | 0.1% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 159,780 | 54.2% |
| ENTER_EXECUTOR | 135,060 | 45.8% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 50.0% |
| POP_JUMP_IF_FALSE | 340 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 620 | 91.2% |
| ENTER_EXECUTOR | 40 | 5.9% |
| LOAD_GLOBAL | 20 | 2.9% |


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
| BINARY_OP_MULTIPLY_INT | 1,221,540 | 37.1% |
| LOAD_CONST | 850,800 | 25.8% |
| LOAD_FAST | 533,120 | 16.2% |
| BINARY_OP_ADD_INT | 530,780 | 16.1% |
| LOAD_GLOBAL_MODULE | 160,040 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,221,600 | 37.1% |
| BINARY_OP_ADD_INT | 1,061,520 | 32.2% |
| LOAD_CONST | 850,800 | 25.8% |
| BUILD_TUPLE | 160,000 | 4.9% |
| CALL_PY_EXACT_ARGS | 2,080 | 0.1% |


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
| LOAD_CONST | 1,221,600 | 50.8% |
| RESUME_CHECK | 693,700 | 28.8% |
| STORE_FAST | 161,360 | 6.7% |
| STORE_FAST_STORE_FAST | 160,720 | 6.7% |
| BUILD_TUPLE | 160,000 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 1,221,480 | 50.8% |
| LOAD_CONST | 533,120 | 22.2% |
| UNPACK_SEQUENCE_TUPLE | 323,560 | 13.4% |
| YIELD_VALUE | 160,000 | 6.7% |
| CALL_PY_EXACT_ARGS | 159,960 | 6.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 642,800 | 56.9% |
| BINARY_OP_ADD_INT | 323,620 | 28.7% |
| STORE_FAST_STORE_FAST | 162,960 | 14.4% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 1,129,160 | 100.0% |
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
| COMPARE_OP_INT | 1,140 | 95.0% |
| COMPARE_OP | 60 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 540 | 45.0% |
| JUMP_BACKWARD | 340 | 28.3% |
| ENTER_EXECUTOR | 160 | 13.3% |
| LOAD_FAST | 80 | 6.7% |
| LOAD_GLOBAL | 80 | 6.7% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 161,920 | 99.8% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 161,360 | 99.4% |
| LOAD_GLOBAL_MODULE | 720 | 0.4% |
| NOP | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 323,680 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 323,620 | 50.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 323,680 | 50.0% |
| LOAD_FAST_LOAD_FAST | 162,960 | 25.2% |
| LOAD_FAST | 160,720 | 24.8% |


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
| LOAD_CONST | 1,061,520 | 68.6% |
| BINARY_OP_MULTIPLY_INT | 482,040 | 31.1% |
| LOAD_FAST | 4,400 | 0.3% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 691,480 | 44.7% |
| LOAD_CONST | 530,780 | 34.3% |
| LOAD_FAST_LOAD_FAST | 323,620 | 20.9% |
| BINARY_OP | 2,220 | 0.1% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,221,480 | 52.0% |
| LOAD_FAST_LOAD_FAST | 1,129,160 | 48.0% |
| BINARY_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,221,540 | 52.0% |
| LOAD_FAST_LOAD_FAST | 642,800 | 27.3% |
| BINARY_OP_ADD_INT | 482,040 | 20.5% |
| LOAD_FAST | 4,440 | 0.2% |
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
| LOAD_FAST | 680 | 97.1% |
| CALL | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 680 | 97.1% |
| CALL | 20 | 2.9% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 159,960 | 98.2% |
| LOAD_CONST | 2,080 | 1.3% |
| CALL_BUILTIN_FAST | 680 | 0.4% |
| CALL | 160 | 0.1% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 162,900 | 100.0% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,040 | 91.2% |
| COMPARE_OP | 60 | 5.3% |
| LOAD_CONST | 40 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,140 | 100.0% |


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
| LOAD_FAST | 680 | 82.9% |
| RESUME_CHECK | 80 | 9.8% |
| LOAD_GLOBAL | 60 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 700 | 85.4% |
| LOAD_CONST | 60 | 7.3% |
| LOAD_GLOBAL_MODULE | 40 | 4.9% |
| LOAD_GLOBAL | 20 | 2.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 159,780 | 97.9% |
| LOAD_FAST | 1,040 | 0.6% |
| STORE_FAST | 720 | 0.4% |
| JUMP_BACKWARD | 620 | 0.4% |
| POP_JUMP_IF_FALSE | 540 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160,040 | 98.1% |
| LOAD_FAST | 2,860 | 1.8% |
| CALL_PY_EXACT_ARGS | 80 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 690,740 | 80.9% |
| CALL_PY_EXACT_ARGS | 162,900 | 19.1% |
| CALL | 80 | 0.0% |
| POP_TOP | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 693,700 | 81.2% |
| POP_TOP | 159,900 | 18.7% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 323,560 | 100.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 323,620 | 100.0% |


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
|     deferred | 2,640 | 0.0% |
|          hit | 14,717,280 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 400 | 80.0% |
| Failure | 100 | 20.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 100 | 100.0% |


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
|     deferred | 300 | 0.2% |
|          hit | 164,020 | 99.6% |

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
| Basic | 10,495,040 | 66.0% |
| Not specialized | 6,300 | 0.0% |
| Specialized hits | 5,405,560 | 34.0% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 2,640 | 69.5% |
| CALL | 700 | 18.4% |
| LOAD_GLOBAL | 300 | 7.9% |
| COMPARE_OP | 60 | 1.6% |
| UNPACK_SEQUENCE | 60 | 1.6% |
| LOAD_ATTR | 40 | 1.1% |
| BINARY_SLICE | 0 | 0.0% |
| STORE_SLICE | 0 | 0.0% |
| CACHE | 0 | 0.0% |
| BINARY_SUBSCR | 0 | 0.0% |


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
| Frames pushed | 2,603,520 | 94.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 1,382,000 | 8.5% |
| Frees to freelist | 1,382,020 |  |
| Allocations | 14,856,680 | 91.5% |
| Allocations to 512 bytes | 4,729,040 | 29.1% |
| Allocations to 4 kbytes | 3,817,160 | 23.5% |
| Allocations over 4 kbytes | 6,310,480 | 38.9% |
| Frees | 14,856,541 |  |
| New values | 0 |  |
| Interpreter increfs | 6,119,300 | 18.8% |
| Interpreter decrefs | 20,992,040 | 43.0% |
| Increfs | 26,514,460 | 81.2% |
| Decrefs | 27,880,204 | 57.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 18 |  |
| Method cache misses | 22 |  |
| Method cache collisions | 28 |  |
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
| Optimization attempts | 40 |  |
| Traces created | 40 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 20 | 50.0% |
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
| <= 64 | 0 | 0.0% |
| <= 128 | 0 | 0.0% |
| <= 256 | 20 | 50.0% |
| <= 512 | 20 | 50.0% |


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
| <= 64 | 0 | 0.0% |
| <= 128 | 0 | 0.0% |
| <= 256 | 40 | 100.0% |


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
