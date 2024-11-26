
# Pystats results

- benchmark: fannkuch
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_CONST | 1,243,073,760 | 22.0% | 22.0% |  |
| LOAD_FAST | 978,603,520 | 17.3% | 39.3% |  |
| LOAD_FAST_LOAD_FAST | 407,668,160 | 7.2% | 46.5% |  |
| POP_JUMP_IF_FALSE | 388,946,800 | 6.9% | 53.3% |  |
| STORE_FAST | 387,652,560 | 6.8% | 60.2% |  |
| BINARY_SUBSCR_LIST_INT | 316,081,720 | 5.6% | 65.8% |  |
| BINARY_OP_ADD_INT | 297,851,200 | 5.3% | 71.0% |  |
| COMPARE_OP_INT | 227,464,620 | 4.0% | 75.0% |  |
| JUMP_BACKWARD | 171,736,240 | 3.0% | 78.1% |  |
| TO_BOOL_INT | 161,481,960 | 2.9% | 80.9% |  |
| BINARY_SUBSCR | 138,533,860 | 2.4% | 83.4% |  |
| STORE_SLICE | 138,499,600 | 2.4% | 85.8% |  |
| BUILD_SLICE | 138,499,600 | 2.4% | 88.3% |  |
| PUSH_NULL | 99,765,040 | 1.8% | 90.0% |  |
| COPY | 99,764,640 | 1.8% | 91.8% |  |
| SWAP | 99,764,640 | 1.8% | 93.6% |  |
| CALL_BUILTIN_FAST | 99,764,600 | 1.8% | 95.3% |  |
| BINARY_OP_SUBTRACT_INT | 91,586,320 | 1.6% | 96.9% |  |
| STORE_SUBSCR_LIST_INT | 70,734,280 | 1.2% | 98.2% |  |
| POP_TOP | 49,882,480 | 0.9% | 99.1% |  |
| JUMP_FORWARD | 29,030,320 | 0.5% | 99.6% |  |
| BINARY_SLICE | 22,982,400 | 0.4% | 100.0% |  |
| CALL | 720 | 0.0% | 100.0% |  |
| BINARY_OP | 360 | 0.0% | 100.0% |  |
| COMPARE_OP | 360 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 360 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_BUILTIN | 360 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 320 | 0.0% | 100.0% |  |
| LOAD_ATTR | 280 | 0.0% | 100.0% |  |
| NOP | 160 | 0.0% | 100.0% |  |
| RETURN_VALUE | 160 | 0.0% | 100.0% |  |
| LOAD_DEREF | 160 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |  |
| RESUME_CHECK | 120 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 80 | 0.0% | 100.0% |  |
| TO_BOOL | 80 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| RESUME | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 741,432,240 | 13.1% | 13.1% |
| STORE_FAST LOAD_FAST | 343,816,560 | 6.1% | 19.2% |
| LOAD_CONST BINARY_OP_ADD_INT | 297,851,120 | 5.3% | 24.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 227,464,620 | 4.0% | 28.5% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 190,512,280 | 3.4% | 31.8% |
| LOAD_CONST LOAD_CONST | 161,482,000 | 2.9% | 34.7% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 161,481,960 | 2.9% | 37.5% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 161,481,960 | 2.9% | 40.4% |
| LOAD_FAST TO_BOOL_INT | 161,481,920 | 2.9% | 43.2% |
| BINARY_OP_ADD_INT STORE_FAST | 159,351,560 | 2.8% | 46.1% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 142,705,920 | 2.5% | 48.6% |
| LOAD_CONST LOAD_FAST | 138,499,680 | 2.4% | 51.0% |
| BINARY_SUBSCR LOAD_FAST | 138,499,620 | 2.4% | 53.5% |
| STORE_SLICE LOAD_FAST | 138,499,600 | 2.4% | 55.9% |
| BUILD_SLICE BINARY_SUBSCR | 138,499,600 | 2.4% | 58.4% |
| LOAD_CONST BUILD_SLICE | 138,499,600 | 2.4% | 60.8% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 138,499,600 | 2.4% | 63.3% |
| BINARY_OP_ADD_INT STORE_SLICE | 138,499,580 | 2.4% | 65.7% |
| LOAD_CONST COMPARE_OP_INT | 128,795,000 | 2.3% | 68.0% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 128,794,980 | 2.3% | 70.3% |
| JUMP_BACKWARD LOAD_FAST_LOAD_FAST | 121,854,000 | 2.2% | 72.4% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 115,314,000 | 2.0% | 74.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 101,896,560 | 1.8% | 76.2% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 91,586,240 | 1.6% | 77.9% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 75,687,040 | 1.3% | 79.2% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 72,864,680 | 1.3% | 80.5% |
| LOAD_FAST PUSH_NULL | 49,882,560 | 0.9% | 81.4% |
| POP_TOP LOAD_FAST_LOAD_FAST | 49,882,320 | 0.9% | 82.3% |
| PUSH_NULL LOAD_CONST | 49,882,320 | 0.9% | 83.1% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 49,882,320 | 0.9% | 84.0% |
| COPY COPY | 49,882,320 | 0.9% | 84.9% |
| LOAD_FAST_LOAD_FAST PUSH_NULL | 49,882,320 | 0.9% | 85.8% |
| LOAD_FAST_LOAD_FAST COPY | 49,882,320 | 0.9% | 86.7% |
| SWAP SWAP | 49,882,320 | 0.9% | 87.5% |
| BINARY_OP_SUBTRACT_INT SWAP | 49,882,300 | 0.9% | 88.4% |
| CALL_BUILTIN_FAST POP_TOP | 49,882,300 | 0.9% | 89.3% |
| STORE_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST | 49,882,300 | 0.9% | 90.2% |
| COPY BINARY_SUBSCR_LIST_INT | 49,882,280 | 0.9% | 91.1% |
| LOAD_CONST CALL_BUILTIN_FAST | 49,882,280 | 0.9% | 92.0% |
| SWAP STORE_SUBSCR_LIST_INT | 49,882,280 | 0.9% | 92.8% |
| CALL_BUILTIN_FAST CALL_BUILTIN_FAST | 49,882,280 | 0.9% | 93.7% |
| JUMP_BACKWARD LOAD_FAST | 49,882,240 | 0.9% | 94.6% |
| JUMP_FORWARD JUMP_BACKWARD | 29,030,320 | 0.5% | 95.1% |
| POP_JUMP_IF_FALSE JUMP_FORWARD | 29,030,320 | 0.5% | 95.6% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 25,804,780 | 0.5% | 96.1% |
| LOAD_FAST COMPARE_OP_INT | 25,804,760 | 0.5% | 96.5% |
| LOAD_CONST STORE_FAST | 22,982,480 | 0.4% | 96.9% |
| STORE_FAST LOAD_CONST | 22,982,480 | 0.4% | 97.3% |
| BINARY_SLICE STORE_FAST | 22,982,400 | 0.4% | 97.8% |
| LOAD_CONST BINARY_SLICE | 22,982,400 | 0.4% | 98.2% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 20,853,200 | 0.4% | 98.5% |
| BINARY_OP_SUBTRACT_INT STORE_FAST | 20,852,040 | 0.4% | 98.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 20,852,000 | 0.4% | 99.3% |
| STORE_SUBSCR_LIST_INT LOAD_FAST | 20,851,980 | 0.4% | 99.6% |
| BINARY_OP_SUBTRACT_INT STORE_SUBSCR_LIST_INT | 20,851,960 | 0.4% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR | 34,020 | 0.0% | 100.0% |
| LOAD_FAST STORE_FAST | 1,280 | 0.0% | 100.0% |
| PUSH_NULL CALL | 320 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP | 320 | 0.0% | 100.0% |
| LOAD_CONST COMPARE_OP | 200 | 0.0% | 100.0% |
| CALL POP_TOP | 180 | 0.0% | 100.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 180 | 0.0% | 100.0% |
| COMPARE_OP COMPARE_OP_INT | 180 | 0.0% | 100.0% |
| LOAD_ATTR STORE_FAST | 180 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS STORE_FAST | 180 | 0.0% | 100.0% |
| CALL CALL | 160 | 0.0% | 100.0% |
| LOAD_FAST RETURN_VALUE | 160 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 160 | 0.0% | 100.0% |
| CALL STORE_FAST | 140 | 0.0% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR_LIST_INT | 120 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| LOAD_CONST BINARY_SUBSCR | 120 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 120 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 120 | 0.0% | 100.0% |
| BINARY_OP STORE_FAST | 100 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| NOP LOAD_FAST | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| POP_TOP LOAD_FAST | 80 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 80 | 0.0% | 100.0% |
| RETURN_VALUE INTERPRETER_EXIT | 80 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_ADD_INT | 80 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP_SUBTRACT_INT | 80 | 0.0% | 100.0% |
| CALL LOAD_FAST | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 80 | 0.0% | 100.0% |
| LOAD_DEREF STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_FAST TO_BOOL | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 80 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 80 | 0.0% | 100.0% |
| STORE_FAST NOP | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_DEREF | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 80 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 22,982,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 22,982,400 | 100.0% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 138,499,580 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,499,600 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 138,499,600 | 100.0% |
| BINARY_SUBSCR | 34,020 | 0.0% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| COPY | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,499,620 | 100.0% |
| BINARY_SUBSCR | 34,020 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| STORE_FAST | 40 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 100.0% |


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
| LOAD_FAST | 80 | 50.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 49,882,300 | 100.0% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 49,882,320 | 100.0% |
| NOP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 49,882,560 | 50.0% |
| LOAD_FAST_LOAD_FAST | 49,882,320 | 50.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_ATTR_MODULE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,882,320 | 50.0% |
| LOAD_FAST_LOAD_FAST | 49,882,320 | 50.0% |
| CALL | 320 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 40 | 50.0% |
| BINARY_OP | 20 | 25.0% |
| BINARY_OP_SUBTRACT_INT | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 40 | 50.0% |
| LOAD_FAST | 20 | 25.0% |
| LOAD_FAST_LOAD_FAST | 20 | 25.0% |


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

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 320 | 88.9% |
| LOAD_FAST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 27.8% |
| BINARY_OP_ADD_INT | 80 | 22.2% |
| BINARY_OP_SUBTRACT_INT | 80 | 22.2% |
| STORE_SLICE | 20 | 5.6% |
| STORE_SUBSCR | 20 | 5.6% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 138,499,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 138,499,600 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 320 | 44.4% |
| CALL | 160 | 22.2% |
| LOAD_FAST | 80 | 11.1% |
| CALL_BUILTIN_CLASS | 60 | 8.3% |
| LOAD_CONST | 40 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 180 | 25.0% |
| CALL | 160 | 22.2% |
| STORE_FAST | 140 | 19.4% |
| CALL_BUILTIN_CLASS | 120 | 16.7% |
| LOAD_FAST | 80 | 11.1% |


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
| LOAD_CONST | 200 | 55.6% |
| LOAD_FAST_LOAD_FAST | 120 | 33.3% |
| LOAD_FAST | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 180 | 50.0% |
| COMPARE_OP_INT | 180 | 50.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 49,882,320 | 50.0% |
| LOAD_FAST_LOAD_FAST | 49,882,320 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 49,882,320 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 49,882,280 | 50.0% |
| BINARY_SUBSCR | 40 | 0.0% |


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
| POP_JUMP_IF_FALSE | 142,705,920 | 83.1% |
| JUMP_FORWARD | 29,030,320 | 16.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 121,854,000 | 71.0% |
| LOAD_FAST | 49,882,240 | 29.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 29,030,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 29,030,320 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 57.1% |
| LOAD_ATTR | 40 | 14.3% |
| LOAD_GLOBAL | 40 | 14.3% |
| LOAD_GLOBAL_MODULE | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 180 | 64.3% |
| LOAD_ATTR | 40 | 14.3% |
| LOAD_ATTR_MODULE | 40 | 14.3% |
| PUSH_NULL | 20 | 7.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 741,432,240 | 59.6% |
| LOAD_CONST | 161,482,000 | 13.0% |
| LOAD_FAST_LOAD_FAST | 138,499,600 | 11.1% |
| BINARY_SUBSCR_LIST_INT | 128,794,980 | 10.4% |
| PUSH_NULL | 49,882,320 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 297,851,120 | 24.0% |
| BINARY_SUBSCR_LIST_INT | 190,512,280 | 15.3% |
| LOAD_CONST | 161,482,000 | 13.0% |
| LOAD_FAST | 138,499,680 | 11.1% |
| BUILD_SLICE | 138,499,600 | 11.1% |


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
| STORE_FAST | 343,816,560 | 35.1% |
| LOAD_CONST | 138,499,680 | 14.2% |
| BINARY_SUBSCR | 138,499,620 | 14.2% |
| STORE_SLICE | 138,499,600 | 14.2% |
| POP_JUMP_IF_FALSE | 101,896,560 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 741,432,240 | 75.8% |
| TO_BOOL_INT | 161,481,920 | 16.5% |
| PUSH_NULL | 49,882,560 | 5.1% |
| COMPARE_OP_INT | 25,804,760 | 2.6% |
| STORE_FAST | 1,280 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 121,854,000 | 29.9% |
| POP_JUMP_IF_FALSE | 115,314,000 | 28.3% |
| POP_TOP | 49,882,320 | 12.2% |
| PUSH_NULL | 49,882,320 | 12.2% |
| STORE_SUBSCR_LIST_INT | 49,882,300 | 12.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 138,499,600 | 34.0% |
| BINARY_SUBSCR_LIST_INT | 75,687,040 | 18.6% |
| COMPARE_OP_INT | 72,864,680 | 17.9% |
| PUSH_NULL | 49,882,320 | 12.2% |
| COPY | 49,882,320 | 12.2% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 25.0% |
| LOAD_GLOBAL | 60 | 18.8% |
| LOAD_GLOBAL_BUILTIN | 60 | 18.8% |
| RETURN_VALUE | 40 | 12.5% |
| RESUME | 40 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 120 | 37.5% |
| LOAD_GLOBAL | 60 | 18.8% |
| LOAD_ATTR | 40 | 12.5% |
| LOAD_FAST | 40 | 12.5% |
| LOAD_GLOBAL_MODULE | 40 | 12.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 227,464,620 | 58.5% |
| TO_BOOL_INT | 161,481,960 | 41.5% |
| COMPARE_OP | 180 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 142,705,920 | 36.7% |
| LOAD_FAST_LOAD_FAST | 115,314,000 | 29.6% |
| LOAD_FAST | 101,896,560 | 26.2% |
| JUMP_FORWARD | 29,030,320 | 7.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 161,481,960 | 41.7% |
| BINARY_OP_ADD_INT | 159,351,560 | 41.1% |
| LOAD_CONST | 22,982,480 | 5.9% |
| BINARY_SLICE | 22,982,400 | 5.9% |
| BINARY_OP_SUBTRACT_INT | 20,852,040 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 343,816,560 | 88.7% |
| LOAD_CONST | 22,982,480 | 5.9% |
| LOAD_FAST_LOAD_FAST | 20,853,200 | 5.4% |
| NOP | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 49,882,320 | 50.0% |
| BINARY_OP_SUBTRACT_INT | 49,882,300 | 50.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 49,882,320 | 50.0% |
| STORE_SUBSCR_LIST_INT | 49,882,280 | 50.0% |
| STORE_SUBSCR | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 20 | 50.0% |
| COPY_FREE_VARS | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 297,851,120 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 159,351,560 | 53.5% |
| STORE_SLICE | 138,499,580 | 46.5% |
| CALL_BUILTIN_CLASS | 40 | 0.0% |
| CALL | 20 | 0.0% |


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
| LOAD_CONST | 91,586,240 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 49,882,300 | 54.5% |
| STORE_FAST | 20,852,040 | 22.8% |
| STORE_SUBSCR_LIST_INT | 20,851,960 | 22.8% |
| STORE_SUBSCR | 20 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 190,512,280 | 60.3% |
| LOAD_FAST_LOAD_FAST | 75,687,040 | 23.9% |
| COPY | 49,882,280 | 15.8% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 161,481,960 | 51.1% |
| LOAD_CONST | 128,794,980 | 40.7% |
| LOAD_FAST | 25,804,780 | 8.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 120 | 33.3% |
| CALL_BUILTIN_CLASS | 120 | 33.3% |
| LOAD_FAST | 80 | 22.2% |
| BINARY_OP_ADD_INT | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 180 | 50.0% |
| CALL_BUILTIN_CLASS | 120 | 33.3% |
| CALL | 60 | 16.7% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 49,882,280 | 50.0% |
| CALL_BUILTIN_FAST | 49,882,280 | 50.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 49,882,300 | 50.0% |
| CALL_BUILTIN_FAST | 49,882,280 | 50.0% |
| CALL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 128,795,000 | 56.6% |
| LOAD_FAST_LOAD_FAST | 72,864,680 | 32.0% |
| LOAD_FAST | 25,804,760 | 11.3% |
| COMPARE_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 227,464,620 | 100.0% |


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
| LOAD_GLOBAL | 120 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 120 | 33.3% |
| STORE_FAST | 80 | 22.2% |
| RESUME_CHECK | 40 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 120 | 33.3% |
| LOAD_CONST | 60 | 16.7% |
| LOAD_GLOBAL | 60 | 16.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 33.3% |
| LOAD_GLOBAL | 40 | 33.3% |
| RESUME_CHECK | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 80 | 66.7% |
| LOAD_ATTR | 40 | 33.3% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 60 | 50.0% |
| COPY_FREE_VARS | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 33.3% |
| LOAD_GLOBAL_BUILTIN | 40 | 33.3% |
| LOAD_GLOBAL_MODULE | 40 | 33.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 49,882,280 | 70.5% |
| BINARY_OP_SUBTRACT_INT | 20,851,960 | 29.5% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 49,882,300 | 70.5% |
| LOAD_FAST | 20,851,980 | 29.5% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 161,481,920 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 161,481,960 | 100.0% |


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
|     deferred | 180 | 0.0% |
|          hit | 389,437,580 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


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
|     deferred | 138,499,720 | 30.5% |
|          hit | 316,081,720 | 69.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 0.4% |
| Failure | 34,020 | 99.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| list slice | 34,020 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 99,764,960 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 66.7% |
| Failure | 80 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 75.0% |
| other | 20 | 25.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 180 | 0.0% |
|          hit | 227,464,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 50.0% |
|          hit | 120 | 30.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 50.0% |
| Failure | 40 | 50.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 40 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 160 | 20.0% |
|          hit | 480 | 60.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


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
|     deferred | 40 | 0.0% |
|          hit | 70,734,280 | 100.0% |

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
|     deferred | 40 | 0.0% |
|          hit | 161,481,960 | 100.0% |

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
| Basic | 3,705,441,720 | 65.5% |
| Not specialized | 688,964,860 | 12.2% |
| Specialized hits | 1,264,965,840 | 22.4% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 138,499,720 | 100.0% |
| CALL | 480 | 0.0% |
| LOAD_ATTR | 200 | 0.0% |
| BINARY_OP | 180 | 0.0% |
| COMPARE_OP | 180 | 0.0% |
| LOAD_GLOBAL | 160 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |
| TO_BOOL | 40 | 0.0% |
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
| Calls to PyEval_EvalDefault | 80 | 50.0% |
| Calls to Python functions inlined | 80 | 50.0% |
| Calls via PyEval_EvalFrame (total) | 80 | 50.0% |
| Calls via PyEval_EvalFrame (vector) | 80 | 50.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 80 | 50.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 50.0% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 0 | 0.0% |
| Frames pushed | 0 | 0.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 161,482,160 | 47.8% |
| Frees to freelist | 161,482,340 |  |
| Allocations | 175,998,340 | 52.2% |
| Allocations to 512 bytes | 175,998,340 | 52.2% |
| Allocations to 4 kbytes | 0 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 175,998,080 |  |
| New values | 0 |  |
| Interpreter increfs | 786,563,880 | 85.0% |
| Interpreter decrefs | 1,248,028,260 | 90.0% |
| Increfs | 138,500,000 | 15.0% |
| Decrefs | 138,500,201 | 10.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 199 |  |
| Method cache misses | 41 |  |
| Method cache collisions | 41 |  |
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
