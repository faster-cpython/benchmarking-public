
# Pystats results

- benchmark: meteor_contest
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| STORE_FAST | 86,137,280 | 13.8% | 13.8% |  |
| LOAD_FAST | 80,651,840 | 12.9% | 26.8% |  |
| LOAD_FAST_LOAD_FAST | 78,088,800 | 12.5% | 39.3% |  |
| JUMP_BACKWARD | 62,308,240 | 10.0% | 49.3% |  |
| FOR_ITER_LIST | 50,678,920 | 8.1% | 57.4% |  |
| POP_JUMP_IF_TRUE | 45,842,800 | 7.4% | 64.8% |  |
| COMPARE_OP | 35,293,140 | 5.7% | 70.4% |  |
| FOR_ITER | 24,710,020 | 4.0% | 74.4% |  |
| LOAD_CONST | 21,507,680 | 3.5% | 77.8% |  |
| STORE_SUBSCR_LIST_INT | 20,586,380 | 3.3% | 81.1% |  |
| LOAD_GLOBAL_BUILTIN | 18,796,020 | 3.0% | 84.2% |  |
| CALL_LEN | 14,676,100 | 2.4% | 86.5% |  |
| COMPARE_OP_INT | 14,675,920 | 2.4% | 88.9% |  |
| GET_ITER | 13,074,560 | 2.1% | 91.0% |  |
| BINARY_SUBSCR_LIST_INT | 13,072,020 | 2.1% | 93.1% |  |
| BINARY_OP | 8,232,300 | 1.3% | 94.4% |  |
| BINARY_SLICE | 6,632,880 | 1.1% | 95.4% |  |
| POP_TOP | 5,040,000 | 0.8% | 96.3% |  |
| POP_JUMP_IF_FALSE | 4,117,360 | 0.7% | 96.9% |  |
| CALL | 4,117,220 | 0.7% | 97.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 2,522,720 | 0.4% | 98.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 2,517,960 | 0.4% | 98.4% |  |
| LOAD_GLOBAL_MODULE | 2,515,880 | 0.4% | 98.8% |  |
| RESUME_CHECK | 2,515,780 | 0.4% | 99.2% |  |
| RETURN_CONST | 2,515,680 | 0.4% | 99.6% |  |
| CALL_PY_WITH_DEFAULTS | 2,515,640 | 0.4% | 100.0% |  |
| PUSH_NULL | 5,200 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,760 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,760 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 2,680 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 2,620 | 0.0% | 100.0% |  |
| BUILD_SLICE | 2,400 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 840 | 0.0% | 100.0% |  |
| LOAD_ATTR | 280 | 0.0% | 100.0% |  |
| BUILD_LIST | 240 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 180 | 0.0% | 100.0% |  |
| RETURN_VALUE | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 140 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| RESUME | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST_LOAD_FAST | 62,312,000 | 10.0% | 10.0% |
| FOR_ITER_LIST STORE_FAST | 41,725,560 | 6.7% | 16.7% |
| JUMP_BACKWARD FOR_ITER_LIST | 41,721,760 | 6.7% | 23.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 39,206,160 | 6.3% | 29.7% |
| COMPARE_OP POP_JUMP_IF_TRUE | 35,284,140 | 5.7% | 35.3% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 35,284,080 | 5.7% | 41.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 29,732,640 | 4.8% | 45.8% |
| FOR_ITER STORE_FAST | 20,586,460 | 3.3% | 49.1% |
| JUMP_BACKWARD FOR_ITER | 20,586,420 | 3.3% | 52.4% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 20,586,380 | 3.3% | 55.7% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 20,586,360 | 3.3% | 59.0% |
| STORE_FAST LOAD_FAST | 15,594,960 | 2.5% | 61.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 14,678,540 | 2.4% | 63.8% |
| LOAD_FAST GET_ITER | 13,074,560 | 2.1% | 65.9% |
| LOAD_FAST CALL_LEN | 10,561,120 | 1.7% | 67.6% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 10,558,660 | 1.7% | 69.3% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 8,957,160 | 1.4% | 70.8% |
| GET_ITER FOR_ITER_LIST | 8,957,120 | 1.4% | 72.2% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 8,957,120 | 1.4% | 73.6% |
| CALL_LEN LOAD_CONST | 8,232,120 | 1.3% | 74.9% |
| LOAD_CONST COMPARE_OP_INT | 8,232,080 | 1.3% | 76.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 8,229,760 | 1.3% | 77.6% |
| LOAD_CONST LOAD_CONST | 6,637,680 | 1.1% | 78.7% |
| LOAD_FAST LOAD_CONST | 6,635,360 | 1.1% | 79.7% |
| BINARY_SLICE STORE_FAST | 6,632,880 | 1.1% | 80.8% |
| LOAD_CONST BINARY_SLICE | 6,632,880 | 1.1% | 81.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 6,632,880 | 1.1% | 82.9% |
| CALL_LEN LOAD_FAST | 6,443,800 | 1.0% | 83.9% |
| LOAD_FAST COMPARE_OP_INT | 6,443,760 | 1.0% | 85.0% |
| FOR_ITER_LIST LOAD_GLOBAL_BUILTIN | 6,441,400 | 1.0% | 86.0% |
| LOAD_FAST LOAD_FAST_LOAD_FAST | 5,031,280 | 0.8% | 86.8% |
| GET_ITER FOR_ITER | 4,117,380 | 0.7% | 87.5% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 4,117,260 | 0.7% | 88.1% |
| FOR_ITER LOAD_GLOBAL_BUILTIN | 4,117,240 | 0.7% | 88.8% |
| LOAD_FAST CALL | 4,115,480 | 0.7% | 89.5% |
| CALL STORE_FAST | 4,115,040 | 0.7% | 90.1% |
| BINARY_OP STORE_FAST | 4,114,980 | 0.7% | 90.8% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 4,114,880 | 0.7% | 91.4% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 4,114,880 | 0.7% | 92.1% |
| BINARY_SUBSCR_LIST_INT BINARY_OP | 4,114,860 | 0.7% | 92.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 4,114,860 | 0.7% | 93.4% |
| BINARY_OP CALL_LEN | 4,114,840 | 0.7% | 94.1% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 4,114,840 | 0.7% | 94.7% |
| LOAD_FAST LOAD_FAST | 2,520,400 | 0.4% | 95.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,520,340 | 0.4% | 95.5% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 2,520,280 | 0.4% | 96.0% |
| POP_TOP JUMP_BACKWARD | 2,515,680 | 0.4% | 96.4% |
| RETURN_CONST POP_TOP | 2,515,680 | 0.4% | 96.8% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 2,515,660 | 0.4% | 97.2% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 2,515,640 | 0.4% | 97.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,515,640 | 0.4% | 98.0% |
| LOAD_FAST CALL_PY_WITH_DEFAULTS | 2,515,600 | 0.4% | 98.4% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 2,515,580 | 0.4% | 98.8% |
| POP_TOP LOAD_GLOBAL_MODULE | 2,515,560 | 0.4% | 99.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 2,515,560 | 0.4% | 99.6% |
| FOR_ITER_LIST RETURN_CONST | 2,511,920 | 0.4% | 100.0% |
| COMPARE_OP COMPARE_OP | 8,820 | 0.0% | 100.0% |
| FOR_ITER FOR_ITER | 6,220 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 4,960 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 4,800 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS LOAD_FAST | 4,760 | 0.0% | 100.0% |
| CALL_METHOD_DESCRIPTOR_FAST POP_TOP | 4,760 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,720 | 0.0% | 100.0% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 4,720 | 0.0% | 100.0% |
| POP_TOP RETURN_CONST | 3,760 | 0.0% | 100.0% |
| POP_JUMP_IF_TRUE POP_TOP | 3,760 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 2,520 | 0.0% | 100.0% |
| BINARY_SUBSCR STORE_FAST | 2,440 | 0.0% | 100.0% |
| BINARY_OP BINARY_OP | 2,420 | 0.0% | 100.0% |
| POP_TOP LOAD_FAST | 2,400 | 0.0% | 100.0% |
| BUILD_SLICE BINARY_SUBSCR | 2,400 | 0.0% | 100.0% |
| LOAD_CONST BUILD_SLICE | 2,400 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_CLASS | 2,400 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 2,400 | 0.0% | 100.0% |
| CALL_METHOD_DESCRIPTOR_O STORE_FAST | 2,380 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL_BUILTIN | 2,360 | 0.0% | 100.0% |
| LOAD_CONST LOAD_ATTR_METHOD_NO_DICT | 2,360 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS CALL_METHOD_DESCRIPTOR_O | 2,360 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_BUILTIN | 2,360 | 0.0% | 100.0% |
| CALL CALL | 1,360 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 300 | 0.0% | 100.0% |
| PUSH_NULL CALL | 240 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 220 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS STORE_FAST | 180 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 180 | 0.0% | 100.0% |
| CALL LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| CALL POP_TOP | 140 | 0.0% | 100.0% |
| CALL CALL_LEN | 140 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 120 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 120 | 0.0% | 100.0% |
| BINARY_SUBSCR BINARY_SUBSCR | 100 | 0.0% | 100.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL | 100 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,632,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,632,880 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 2,400 | 91.6% |
| BINARY_SUBSCR | 100 | 3.8% |
| LOAD_FAST_LOAD_FAST | 80 | 3.1% |
| LOAD_FAST | 40 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,440 | 93.1% |
| BINARY_SUBSCR | 100 | 3.8% |
| BINARY_SUBSCR_LIST_INT | 60 | 2.3% |
| BINARY_OP | 20 | 0.8% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,074,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 8,957,120 | 68.5% |
| FOR_ITER | 4,117,380 | 31.5% |
| FOR_ITER_RANGE | 60 | 0.0% |


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
| RETURN_CONST | 2,515,680 | 49.9% |
| CALL_METHOD_DESCRIPTOR_O | 2,515,580 | 49.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 4,760 | 0.1% |
| POP_JUMP_IF_TRUE | 3,760 | 0.1% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,515,680 | 49.9% |
| LOAD_GLOBAL_MODULE | 2,515,560 | 49.9% |
| RETURN_CONST | 3,760 | 0.1% |
| LOAD_FAST | 2,400 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 2,360 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,800 | 92.3% |
| LOAD_ATTR_MODULE | 180 | 3.5% |
| LOAD_DEREF | 160 | 3.1% |
| LOAD_ATTR | 60 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,960 | 95.4% |
| CALL | 240 | 4.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| LOAD_FAST | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20 | 50.0% |
| STORE_SUBSCR_LIST_INT | 20 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,114,880 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 4,114,860 | 50.0% |
| BINARY_OP | 2,420 | 0.0% |
| CALL_LEN | 60 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,114,980 | 50.0% |
| CALL_LEN | 4,114,840 | 50.0% |
| BINARY_OP | 2,420 | 0.0% |
| CALL | 40 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 33.3% |
| LOAD_FAST | 80 | 33.3% |
| STORE_FAST | 80 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 33.3% |
| STORE_FAST | 80 | 33.3% |
| LOAD_GLOBAL | 40 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 40 | 16.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 2,400 | 100.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,115,480 | 100.0% |
| CALL | 1,360 | 0.0% |
| PUSH_NULL | 240 | 0.0% |
| CALL_BUILTIN_CLASS | 60 | 0.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,115,040 | 99.9% |
| CALL | 1,360 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| POP_TOP | 140 | 0.0% |
| CALL_LEN | 140 | 0.0% |


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

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 35,284,080 | 100.0% |
| COMPARE_OP | 8,820 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 35,284,140 | 100.0% |
| COMPARE_OP | 8,820 | 0.0% |
| POP_JUMP_IF_FALSE | 100 | 0.0% |
| COMPARE_OP_INT | 80 | 0.0% |


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
| JUMP_BACKWARD | 20,586,420 | 83.3% |
| GET_ITER | 4,117,380 | 16.7% |
| FOR_ITER | 6,220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,586,460 | 83.3% |
| LOAD_GLOBAL_BUILTIN | 4,117,240 | 16.7% |
| FOR_ITER | 6,220 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| FOR_ITER_LIST | 40 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 39,206,160 | 62.9% |
| STORE_SUBSCR_LIST_INT | 20,586,380 | 33.0% |
| POP_TOP | 2,515,680 | 4.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 41,721,760 | 67.0% |
| FOR_ITER | 20,586,420 | 33.0% |
| FOR_ITER_RANGE | 60 | 0.0% |


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
| LOAD_FAST | 120 | 42.9% |
| LOAD_GLOBAL | 60 | 21.4% |
| LOAD_GLOBAL_MODULE | 60 | 21.4% |
| LOAD_CONST | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 80 | 28.6% |
| PUSH_NULL | 60 | 21.4% |
| LOAD_FAST | 60 | 21.4% |
| LOAD_ATTR_MODULE | 60 | 21.4% |
| LOAD_GLOBAL | 20 | 7.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 8,232,120 | 38.3% |
| LOAD_CONST | 6,637,680 | 30.9% |
| LOAD_FAST | 6,635,360 | 30.9% |
| POP_JUMP_IF_FALSE | 2,400 | 0.0% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 8,232,080 | 38.3% |
| LOAD_CONST | 6,637,680 | 30.9% |
| BINARY_SLICE | 6,632,880 | 30.8% |
| BUILD_SLICE | 2,400 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 2,360 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 29,732,640 | 36.9% |
| STORE_FAST | 15,594,960 | 19.3% |
| LOAD_GLOBAL_BUILTIN | 14,678,540 | 18.2% |
| POP_JUMP_IF_TRUE | 6,632,880 | 8.2% |
| CALL_LEN | 6,443,800 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_LIST_INT | 20,586,360 | 25.5% |
| GET_ITER | 13,074,560 | 16.2% |
| CALL_LEN | 10,561,120 | 13.1% |
| LOAD_CONST | 6,635,360 | 8.2% |
| COMPARE_OP_INT | 6,443,760 | 8.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 50.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,312,000 | 79.8% |
| LOAD_FAST | 5,031,280 | 6.4% |
| POP_JUMP_IF_FALSE | 4,114,880 | 5.3% |
| LOAD_GLOBAL_BUILTIN | 4,114,860 | 5.3% |
| RESUME_CHECK | 2,515,660 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 35,284,080 | 45.2% |
| LOAD_FAST | 29,732,640 | 38.1% |
| BINARY_SUBSCR_LIST_INT | 8,957,120 | 11.5% |
| BINARY_OP | 4,114,880 | 5.3% |
| BINARY_SUBSCR | 80 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 28.6% |
| LOAD_GLOBAL | 100 | 11.9% |
| LOAD_GLOBAL_BUILTIN | 100 | 11.9% |
| POP_TOP | 80 | 9.5% |
| RETURN_VALUE | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 300 | 35.7% |
| LOAD_FAST | 220 | 26.2% |
| LOAD_GLOBAL_MODULE | 120 | 14.3% |
| LOAD_GLOBAL | 100 | 11.9% |
| LOAD_ATTR | 60 | 7.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 4,117,260 | 100.0% |
| COMPARE_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,114,880 | 99.9% |
| LOAD_CONST | 2,400 | 0.1% |
| LOAD_FAST | 80 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 35,284,140 | 77.0% |
| COMPARE_OP_INT | 10,558,660 | 23.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 39,206,160 | 85.5% |
| LOAD_FAST | 6,632,880 | 14.5% |
| POP_TOP | 3,760 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 2,511,920 | 99.9% |
| POP_TOP | 3,760 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,515,680 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 41,725,560 | 48.4% |
| FOR_ITER | 20,586,460 | 23.9% |
| BINARY_SUBSCR_LIST_INT | 8,957,160 | 10.4% |
| BINARY_SLICE | 6,632,880 | 7.7% |
| CALL | 4,115,040 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,312,000 | 72.3% |
| LOAD_FAST | 15,594,960 | 18.1% |
| LOAD_GLOBAL_BUILTIN | 8,229,760 | 9.6% |
| LOAD_GLOBAL | 240 | 0.0% |
| BUILD_LIST | 80 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 33.3% |
| CALL_FUNCTION_EX | 20 | 33.3% |
| COPY_FREE_VARS | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 20 | 33.3% |
| LOAD_FAST_LOAD_FAST | 20 | 33.3% |
| LOAD_GLOBAL | 20 | 33.3% |


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

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,957,120 | 68.5% |
| LOAD_FAST | 4,114,840 | 31.5% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,957,160 | 68.5% |
| BINARY_OP | 4,114,860 | 31.5% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,400 | 89.6% |
| CALL | 120 | 4.5% |
| CALL_BUILTIN_CLASS | 80 | 3.0% |
| CALL_LEN | 80 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 2,360 | 88.1% |
| STORE_FAST | 180 | 6.7% |
| CALL_BUILTIN_CLASS | 80 | 3.0% |
| CALL | 60 | 2.2% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,720 | 99.2% |
| CALL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,760 | 100.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,561,120 | 72.0% |
| BINARY_OP | 4,114,840 | 28.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,232,120 | 56.1% |
| LOAD_FAST | 6,443,800 | 43.9% |
| CALL_BUILTIN_CLASS | 80 | 0.0% |
| BINARY_OP | 60 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,720 | 99.2% |
| CALL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,760 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,515,560 | 99.9% |
| CALL_BUILTIN_CLASS | 2,360 | 0.1% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,515,580 | 99.9% |
| STORE_FAST | 2,380 | 0.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,515,600 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,515,640 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,232,080 | 56.1% |
| LOAD_FAST | 6,443,760 | 43.9% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 10,558,660 | 71.9% |
| POP_JUMP_IF_FALSE | 4,117,260 | 28.1% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 41,721,760 | 82.3% |
| GET_ITER | 8,957,120 | 17.7% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 41,725,560 | 82.3% |
| LOAD_GLOBAL_BUILTIN | 6,441,400 | 12.7% |
| RETURN_CONST | 2,511,920 | 5.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 42.9% |
| JUMP_BACKWARD | 60 | 42.9% |
| FOR_ITER | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 42.9% |
| LOAD_GLOBAL | 40 | 28.6% |
| LOAD_GLOBAL_MODULE | 40 | 28.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,520,280 | 99.9% |
| LOAD_CONST | 2,360 | 0.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,520,340 | 99.9% |
| LOAD_GLOBAL_BUILTIN | 2,360 | 0.1% |
| LOAD_GLOBAL | 20 | 0.0% |


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
| STORE_FAST | 8,229,760 | 43.8% |
| FOR_ITER_LIST | 6,441,400 | 34.3% |
| FOR_ITER | 4,117,240 | 21.9% |
| LOAD_GLOBAL_BUILTIN | 2,520 | 0.0% |
| POP_TOP | 2,360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,678,540 | 78.1% |
| LOAD_FAST_LOAD_FAST | 4,114,860 | 21.9% |
| LOAD_GLOBAL_BUILTIN | 2,520 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,515,560 | 100.0% |
| LOAD_GLOBAL | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |
| LOAD_FAST_CHECK | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,515,640 | 100.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| COMPARE_OP | 60 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 2,515,640 | 100.0% |
| CALL_FUNCTION_EX | 60 | 0.0% |
| COPY_FREE_VARS | 60 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,515,660 | 100.0% |
| LOAD_DEREF | 60 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,586,360 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20,586,380 | 100.0% |


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
|     deferred | 8,229,860 | 100.0% |
|          hit | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 0.8% |
| Failure | 2,420 | 99.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and other | 1,200 | 49.6% |
| subtract other | 1,200 | 49.6% |
| multiply different types | 20 | 0.8% |


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
|     deferred | 2,460 | 0.0% |
|          hit | 13,072,020 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 37.5% |
| Failure | 100 | 62.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string slice | 100 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,115,540 | 17.3% |
|          hit | 19,721,900 | 82.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 25.0% |
| Failure | 1,260 | 75.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc varargs keywords | 1,200 | 95.2% |
| cfunc noargs | 60 | 4.8% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 35,284,240 | 70.6% |
|          hit | 14,675,920 | 29.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 0.9% |
| Failure | 8,820 | 99.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 8,800 | 99.8% |
| list | 20 | 0.2% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 24,703,740 | 32.8% |
|          hit | 50,679,060 | 67.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 1.0% |
| Failure | 6,220 | 99.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 6,220 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 140 | 0.0% |
|          hit | 2,522,900 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 420 | 0.0% |
|          hit | 21,311,900 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 420 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 20,586,380 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 349,332,940 | 56.0% |
| Not specialized | 128,949,500 | 20.7% |
| Specialized hits | 145,085,920 | 23.3% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| COMPARE_OP | 35,284,240 | 48.8% |
| FOR_ITER | 24,703,740 | 34.2% |
| BINARY_OP | 8,229,860 | 11.4% |
| CALL | 4,115,540 | 5.7% |
| BINARY_SUBSCR | 2,460 | 0.0% |
| LOAD_GLOBAL | 420 | 0.0% |
| LOAD_ATTR | 140 | 0.0% |
| STORE_SUBSCR | 20 | 0.0% |
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
| Calls to Python functions inlined | 2,515,840 | 100.0% |
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
| Frames pushed | 2,515,640 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 10,872,960 | 23.0% |
| Frees to freelist | 10,873,140 |  |
| Allocations | 36,420,180 | 77.0% |
| Allocations to 512 bytes | 32,305,140 | 68.3% |
| Allocations to 4 kbytes | 4,115,040 | 8.7% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 36,420,000 |  |
| New values | 0 |  |
| Interpreter increfs | 245,812,180 | 91.8% |
| Interpreter decrefs | 289,346,340 | 93.0% |
| Increfs | 22,017,160 | 8.2% |
| Decrefs | 21,660,704 | 7.0% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 189 |  |
| Method cache misses | 31 |  |
| Method cache collisions | 32 |  |
| Method cache dunder hits | 2,399 |  |
| Method cache dunder misses | 1 |  |


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
