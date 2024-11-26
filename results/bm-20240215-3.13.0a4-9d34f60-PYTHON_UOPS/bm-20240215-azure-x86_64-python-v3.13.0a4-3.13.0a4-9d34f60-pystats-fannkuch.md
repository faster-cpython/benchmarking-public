
# Pystats results

- benchmark: fannkuch
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_CONST | 384,746,100 | 18.2% | 18.2% |  |
| LOAD_FAST | 278,974,040 | 13.2% | 31.4% |  |
| POP_JUMP_IF_FALSE | 207,132,420 | 9.8% | 41.2% |  |
| LOAD_FAST_LOAD_FAST | 202,563,340 | 9.6% | 50.8% |  |
| BINARY_SUBSCR_LIST_INT | 148,782,220 | 7.0% | 57.8% |  |
| COMPARE_OP_INT | 146,652,160 | 6.9% | 64.8% |  |
| STORE_FAST | 135,767,360 | 6.4% | 71.2% |  |
| ENTER_EXECUTOR | 76,378,040 | 3.6% | 74.8% |  |
| BINARY_OP_ADD_INT | 66,817,440 | 3.2% | 78.0% |  |
| PUSH_NULL | 57,121,320 | 2.7% | 80.7% |  |
| COPY | 57,120,920 | 2.7% | 83.4% |  |
| SWAP | 57,120,920 | 2.7% | 86.1% |  |
| CALL_BUILTIN_FAST | 57,120,880 | 2.7% | 88.8% |  |
| TO_BOOL_INT | 45,965,080 | 2.2% | 90.9% |  |
| BINARY_OP_SUBTRACT_INT | 28,561,580 | 1.4% | 92.3% |  |
| STORE_SUBSCR_LIST_INT | 28,560,980 | 1.4% | 93.6% |  |
| POP_TOP | 28,560,620 | 1.4% | 95.0% |  |
| BINARY_SUBSCR | 22,988,760 | 1.1% | 96.1% |  |
| STORE_SLICE | 22,982,720 | 1.1% | 97.2% |  |
| BUILD_SLICE | 22,982,720 | 1.1% | 98.2% |  |
| BINARY_SLICE | 22,982,400 | 1.1% | 99.3% |  |
| JUMP_FORWARD | 14,045,160 | 0.7% | 100.0% |  |
| JUMP_BACKWARD | 1,360 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_CONST | 182,942,160 | 8.7% | 8.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 146,652,160 | 6.9% | 15.6% |
| STORE_FAST LOAD_FAST | 91,931,360 | 4.3% | 19.9% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 81,313,020 | 3.8% | 23.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 75,330,580 | 3.6% | 27.4% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 72,394,420 | 3.4% | 30.8% |
| POP_JUMP_IF_FALSE LOAD_FAST | 71,905,920 | 3.4% | 34.2% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 70,157,160 | 3.3% | 37.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 66,817,360 | 3.2% | 40.7% |
| LOAD_CONST COMPARE_OP_INT | 52,753,460 | 2.5% | 43.2% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 50,064,520 | 2.4% | 45.5% |
| LOAD_CONST LOAD_CONST | 45,965,120 | 2.2% | 47.7% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 45,965,080 | 2.2% | 49.9% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 45,965,080 | 2.2% | 52.0% |
| LOAD_FAST TO_BOOL_INT | 45,965,040 | 2.2% | 54.2% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 45,849,740 | 2.2% | 56.4% |
| BINARY_OP_ADD_INT STORE_FAST | 43,834,680 | 2.1% | 58.5% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 28,561,500 | 1.4% | 59.8% |
| LOAD_FAST PUSH_NULL | 28,560,700 | 1.4% | 61.2% |
| POP_TOP LOAD_FAST_LOAD_FAST | 28,560,460 | 1.4% | 62.5% |
| PUSH_NULL LOAD_CONST | 28,560,460 | 1.4% | 63.9% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 28,560,460 | 1.4% | 65.2% |
| COPY COPY | 28,560,460 | 1.4% | 66.6% |
| LOAD_FAST_LOAD_FAST PUSH_NULL | 28,560,460 | 1.4% | 67.9% |
| LOAD_FAST_LOAD_FAST COPY | 28,560,460 | 1.4% | 69.3% |
| SWAP SWAP | 28,560,460 | 1.4% | 70.6% |
| BINARY_OP_SUBTRACT_INT SWAP | 28,560,440 | 1.4% | 72.0% |
| CALL_BUILTIN_FAST POP_TOP | 28,560,440 | 1.4% | 73.3% |
| STORE_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST | 28,560,440 | 1.4% | 74.7% |
| COPY BINARY_SUBSCR_LIST_INT | 28,560,420 | 1.4% | 76.0% |
| LOAD_CONST CALL_BUILTIN_FAST | 28,560,420 | 1.4% | 77.4% |
| SWAP STORE_SUBSCR_LIST_INT | 28,560,420 | 1.4% | 78.7% |
| CALL_BUILTIN_FAST CALL_BUILTIN_FAST | 28,560,420 | 1.4% | 80.1% |
| ENTER_EXECUTOR LOAD_FAST | 24,682,140 | 1.2% | 81.2% |
| LOAD_CONST LOAD_FAST | 22,982,800 | 1.1% | 82.3% |
| BINARY_SUBSCR LOAD_FAST | 22,982,740 | 1.1% | 83.4% |
| STORE_SLICE LOAD_FAST | 22,982,720 | 1.1% | 84.5% |
| BUILD_SLICE BINARY_SUBSCR | 22,982,720 | 1.1% | 85.6% |
| LOAD_CONST BUILD_SLICE | 22,982,720 | 1.1% | 86.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 22,982,720 | 1.1% | 87.8% |
| BINARY_OP_ADD_INT STORE_SLICE | 22,982,700 | 1.1% | 88.9% |
| LOAD_CONST STORE_FAST | 22,982,480 | 1.1% | 89.9% |
| STORE_FAST LOAD_CONST | 22,982,480 | 1.1% | 91.0% |
| BINARY_SLICE STORE_FAST | 22,982,400 | 1.1% | 92.1% |
| LOAD_CONST BINARY_SLICE | 22,982,400 | 1.1% | 93.2% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST | 21,504,120 | 1.0% | 94.2% |
| LOAD_FAST COMPARE_OP_INT | 21,504,100 | 1.0% | 95.2% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 20,853,200 | 1.0% | 96.2% |
| ENTER_EXECUTOR LOAD_FAST_LOAD_FAST | 20,697,540 | 1.0% | 97.2% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 16,483,400 | 0.8% | 98.0% |
| ENTER_EXECUTOR POP_JUMP_IF_FALSE | 14,514,960 | 0.7% | 98.7% |
| POP_JUMP_IF_FALSE JUMP_FORWARD | 14,045,160 | 0.7% | 99.3% |
| JUMP_FORWARD ENTER_EXECUTOR | 14,044,820 | 0.7% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR | 5,800 | 0.0% | 100.0% |
| LOAD_FAST STORE_FAST | 1,280 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 1,020 | 0.0% | 100.0% |
| JUMP_BACKWARD LOAD_FAST | 640 | 0.0% | 100.0% |
| JUMP_BACKWARD LOAD_FAST_LOAD_FAST | 640 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_INT STORE_FAST | 600 | 0.0% | 100.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 560 | 0.0% | 100.0% |
| STORE_SUBSCR_LIST_INT LOAD_FAST | 540 | 0.0% | 100.0% |
| BINARY_OP_SUBTRACT_INT STORE_SUBSCR_LIST_INT | 520 | 0.0% | 100.0% |
| JUMP_FORWARD JUMP_BACKWARD | 340 | 0.0% | 100.0% |
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
| JUMP_BACKWARD ENTER_EXECUTOR | 80 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 80 | 0.0% | 100.0% |
| LOAD_DEREF STORE_FAST | 80 | 0.0% | 100.0% |
| LOAD_FAST TO_BOOL | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |


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
| BINARY_OP_ADD_INT | 22,982,700 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,982,720 | 100.0% |


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
| BUILD_SLICE | 22,982,720 | 100.0% |
| BINARY_SUBSCR | 5,800 | 0.0% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| COPY | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 22,982,740 | 100.0% |
| BINARY_SUBSCR | 5,800 | 0.0% |
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
| CALL_BUILTIN_FAST | 28,560,440 | 100.0% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 28,560,460 | 100.0% |
| NOP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,560,700 | 50.0% |
| LOAD_FAST_LOAD_FAST | 28,560,460 | 50.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_ATTR_MODULE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 28,560,460 | 50.0% |
| LOAD_FAST_LOAD_FAST | 28,560,460 | 50.0% |
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
| LOAD_CONST | 22,982,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 22,982,720 | 100.0% |


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
| COPY | 28,560,460 | 50.0% |
| LOAD_FAST_LOAD_FAST | 28,560,460 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 28,560,460 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 28,560,420 | 50.0% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 45,849,740 | 60.0% |
| ENTER_EXECUTOR | 16,483,400 | 21.6% |
| JUMP_FORWARD | 14,044,820 | 18.4% |
| JUMP_BACKWARD | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,682,140 | 32.3% |
| LOAD_FAST_LOAD_FAST | 20,697,540 | 27.1% |
| ENTER_EXECUTOR | 16,483,400 | 21.6% |
| POP_JUMP_IF_FALSE | 14,514,960 | 19.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,020 | 75.0% |
| JUMP_FORWARD | 340 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 47.1% |
| LOAD_FAST_LOAD_FAST | 640 | 47.1% |
| ENTER_EXECUTOR | 80 | 5.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 14,045,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 14,044,820 | 100.0% |
| JUMP_BACKWARD | 340 | 0.0% |


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
| LOAD_FAST | 182,942,160 | 47.5% |
| BINARY_SUBSCR_LIST_INT | 81,313,020 | 21.1% |
| LOAD_CONST | 45,965,120 | 11.9% |
| PUSH_NULL | 28,560,460 | 7.4% |
| LOAD_FAST_LOAD_FAST | 22,982,720 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 70,157,160 | 18.2% |
| BINARY_OP_ADD_INT | 66,817,360 | 17.4% |
| COMPARE_OP_INT | 52,753,460 | 13.7% |
| LOAD_CONST | 45,965,120 | 11.9% |
| BINARY_OP_SUBTRACT_INT | 28,561,500 | 7.4% |


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
| STORE_FAST | 91,931,360 | 33.0% |
| POP_JUMP_IF_FALSE | 71,905,920 | 25.8% |
| ENTER_EXECUTOR | 24,682,140 | 8.8% |
| LOAD_CONST | 22,982,800 | 8.2% |
| BINARY_SUBSCR | 22,982,740 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 182,942,160 | 65.6% |
| TO_BOOL_INT | 45,965,040 | 16.5% |
| PUSH_NULL | 28,560,700 | 10.2% |
| COMPARE_OP_INT | 21,504,100 | 7.7% |
| STORE_FAST | 1,280 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 75,330,580 | 37.2% |
| POP_TOP | 28,560,460 | 14.1% |
| PUSH_NULL | 28,560,460 | 14.1% |
| STORE_SUBSCR_LIST_INT | 28,560,440 | 14.1% |
| STORE_FAST | 20,853,200 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 72,394,420 | 35.7% |
| BINARY_SUBSCR_LIST_INT | 50,064,520 | 24.7% |
| PUSH_NULL | 28,560,460 | 14.1% |
| COPY | 28,560,460 | 14.1% |
| LOAD_CONST | 22,982,720 | 11.3% |


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
| COMPARE_OP_INT | 146,652,160 | 70.8% |
| TO_BOOL_INT | 45,965,080 | 22.2% |
| ENTER_EXECUTOR | 14,514,960 | 7.0% |
| COMPARE_OP | 180 | 0.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 75,330,580 | 36.4% |
| LOAD_FAST | 71,905,920 | 34.7% |
| ENTER_EXECUTOR | 45,849,740 | 22.1% |
| JUMP_FORWARD | 14,045,160 | 6.8% |
| JUMP_BACKWARD | 1,020 | 0.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 45,965,080 | 33.9% |
| BINARY_OP_ADD_INT | 43,834,680 | 32.3% |
| LOAD_CONST | 22,982,480 | 16.9% |
| BINARY_SLICE | 22,982,400 | 16.9% |
| LOAD_FAST | 1,280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 91,931,360 | 67.7% |
| LOAD_CONST | 22,982,480 | 16.9% |
| LOAD_FAST_LOAD_FAST | 20,853,200 | 15.4% |
| NOP | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 28,560,460 | 50.0% |
| BINARY_OP_SUBTRACT_INT | 28,560,440 | 50.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 28,560,460 | 50.0% |
| STORE_SUBSCR_LIST_INT | 28,560,420 | 50.0% |
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
| LOAD_CONST | 66,817,360 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,834,680 | 65.6% |
| STORE_SLICE | 22,982,700 | 34.4% |
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
| LOAD_CONST | 28,561,500 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 28,560,440 | 100.0% |
| STORE_FAST | 600 | 0.0% |
| STORE_SUBSCR_LIST_INT | 520 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 70,157,160 | 47.2% |
| LOAD_FAST_LOAD_FAST | 50,064,520 | 33.6% |
| COPY | 28,560,420 | 19.2% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 81,313,020 | 54.7% |
| STORE_FAST | 45,965,080 | 30.9% |
| LOAD_FAST | 21,504,120 | 14.5% |


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
| LOAD_CONST | 28,560,420 | 50.0% |
| CALL_BUILTIN_FAST | 28,560,420 | 50.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 28,560,440 | 50.0% |
| CALL_BUILTIN_FAST | 28,560,420 | 50.0% |
| CALL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,394,420 | 49.4% |
| LOAD_CONST | 52,753,460 | 36.0% |
| LOAD_FAST | 21,504,100 | 14.7% |
| COMPARE_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 146,652,160 | 100.0% |


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
| SWAP | 28,560,420 | 100.0% |
| BINARY_OP_SUBTRACT_INT | 520 | 0.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 28,560,440 | 100.0% |
| LOAD_FAST | 540 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,965,040 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 45,965,080 | 100.0% |


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
|     deferred | 22,982,840 | 6.8% |
|          hit | 316,081,720 | 93.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 2.0% |
| Failure | 5,800 | 98.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| list slice | 5,800 | 100.0% |


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
| Basic | 1,315,382,660 | 62.2% |
| Not specialized | 276,088,500 | 13.1% |
| Specialized hits | 522,461,480 | 24.7% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 22,982,840 | 100.0% |
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
| Frames pushed | 160 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 161,482,160 | 47.8% |
| Frees to freelist | 161,482,340 |  |
| Allocations | 175,998,420 | 52.2% |
| Allocations to 512 bytes | 175,998,340 | 52.2% |
| Allocations to 4 kbytes | 80 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 175,998,080 |  |
| New values | 0 |  |
| Interpreter increfs | 379,791,640 | 37.9% |
| Interpreter decrefs | 494,705,380 | 33.8% |
| Increfs | 621,650,360 | 62.1% |
| Decrefs | 968,201,200 | 66.2% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 208 |  |
| Method cache misses | 32 |  |
| Method cache collisions | 32 |  |
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
| Optimization attempts | 80 |  |
| Traces created | 80 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 40 | 50.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 20 | 25.0% |
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
| <= 64 | 60 | 75.0% |
| <= 128 | 20 | 25.0% |


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
| <= 32 | 20 | 25.0% |
| <= 64 | 40 | 50.0% |
| <= 128 | 20 | 25.0% |


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
