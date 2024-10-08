
# Pystats results

- benchmark: meteor_contest
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 60,257,420 | 19.6% | 19.6% |  |
| STORE_FAST | 28,939,320 | 9.4% | 29.0% |  |
| LOAD_FAST_LOAD_FAST | 24,816,400 | 8.1% | 37.0% |  |
| LOAD_CONST | 21,507,680 | 7.0% | 44.0% |  |
| ENTER_EXECUTOR | 20,112,980 | 6.5% | 50.6% |  |
| LOAD_GLOBAL_BUILTIN | 18,796,020 | 6.1% | 56.7% |  |
| CALL_LEN | 14,676,100 | 4.8% | 61.4% |  |
| COMPARE_OP_INT | 14,675,920 | 4.8% | 66.2% |  |
| FOR_ITER_LIST | 13,875,380 | 4.5% | 70.7% |  |
| GET_ITER | 9,149,000 | 3.0% | 73.7% |  |
| BINARY_SUBSCR_LIST_INT | 9,146,460 | 3.0% | 76.6% |  |
| POP_JUMP_IF_TRUE | 8,849,940 | 2.9% | 79.5% |  |
| BINARY_OP | 8,232,300 | 2.7% | 82.2% |  |
| POP_JUMP_IF_FALSE | 8,232,240 | 2.7% | 84.9% |  |
| BINARY_SLICE | 6,632,880 | 2.2% | 87.0% |  |
| POP_TOP | 5,040,000 | 1.6% | 88.7% |  |
| EXTENDED_ARG | 5,028,220 | 1.6% | 90.3% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,119,620 | 1.3% | 91.6% |  |
| FOR_ITER | 4,118,920 | 1.3% | 93.0% |  |
| STORE_SUBSCR_LIST_INT | 4,117,520 | 1.3% | 94.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 2,522,720 | 0.8% | 95.1% |  |
| CALL_METHOD_DESCRIPTOR_O | 2,517,960 | 0.8% | 95.9% |  |
| LOAD_GLOBAL_MODULE | 2,515,880 | 0.8% | 96.8% |  |
| RESUME_CHECK | 2,515,780 | 0.8% | 97.6% |  |
| RETURN_CONST | 2,515,680 | 0.8% | 98.4% |  |
| CALL_PY_WITH_DEFAULTS | 2,515,640 | 0.8% | 99.2% |  |
| COMPARE_OP | 2,407,140 | 0.8% | 100.0% |  |
| PUSH_NULL | 5,200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,760 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 2,680 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 2,620 | 0.0% | 100.0% |  |
| BUILD_SLICE | 2,400 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 2,120 | 0.0% | 100.0% |  |
| CALL | 1,180 | 0.0% | 100.0% |  |
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
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 14,678,540 | 4.8% | 4.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 13,263,780 | 4.3% | 9.1% |
| STORE_FAST LOAD_FAST | 11,669,400 | 3.8% | 12.9% |
| LOAD_FAST CALL_LEN | 10,561,120 | 3.4% | 16.3% |
| LOAD_FAST GET_ITER | 9,149,000 | 3.0% | 19.3% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 9,039,600 | 2.9% | 22.2% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 8,581,280 | 2.8% | 25.0% |
| CALL_LEN LOAD_CONST | 8,232,120 | 2.7% | 27.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 8,232,120 | 2.7% | 30.3% |
| LOAD_CONST COMPARE_OP_INT | 8,232,080 | 2.7% | 33.0% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 8,229,760 | 2.7% | 35.7% |
| LOAD_CONST LOAD_CONST | 6,637,680 | 2.2% | 37.8% |
| LOAD_FAST LOAD_CONST | 6,635,360 | 2.2% | 40.0% |
| BINARY_SLICE STORE_FAST | 6,632,880 | 2.2% | 42.2% |
| LOAD_CONST BINARY_SLICE | 6,632,880 | 2.2% | 44.3% |
| CALL_LEN LOAD_FAST | 6,443,800 | 2.1% | 46.4% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 6,443,800 | 2.1% | 48.5% |
| LOAD_FAST COMPARE_OP_INT | 6,443,760 | 2.1% | 50.6% |
| FOR_ITER_LIST LOAD_GLOBAL_BUILTIN | 6,441,400 | 2.1% | 52.7% |
| ENTER_EXECUTOR FOR_ITER_LIST | 6,330,300 | 2.1% | 54.7% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 5,031,600 | 1.6% | 56.4% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 5,031,560 | 1.6% | 58.0% |
| LOAD_FAST LOAD_FAST_LOAD_FAST | 5,031,280 | 1.6% | 59.6% |
| EXTENDED_ARG FOR_ITER_LIST | 5,027,840 | 1.6% | 61.3% |
| FOR_ITER_LIST STORE_FAST | 4,922,020 | 1.6% | 62.9% |
| LOAD_FAST CALL_BUILTIN_FAST_WITH_KEYWORDS | 4,119,560 | 1.3% | 64.2% |
| FOR_ITER STORE_FAST | 4,117,600 | 1.3% | 65.5% |
| LOAD_FAST STORE_SUBSCR_LIST_INT | 4,117,500 | 1.3% | 66.9% |
| GET_ITER FOR_ITER | 4,117,340 | 1.3% | 68.2% |
| ENTER_EXECUTOR LOAD_GLOBAL_BUILTIN | 4,117,220 | 1.3% | 69.6% |
| STORE_SUBSCR_LIST_INT ENTER_EXECUTOR | 4,117,200 | 1.3% | 70.9% |
| BINARY_OP STORE_FAST | 4,114,980 | 1.3% | 72.2% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 4,114,880 | 1.3% | 73.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 4,114,880 | 1.3% | 74.9% |
| BINARY_SUBSCR_LIST_INT BINARY_OP | 4,114,860 | 1.3% | 76.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS STORE_FAST | 4,114,860 | 1.3% | 77.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 4,114,860 | 1.3% | 78.9% |
| BINARY_OP CALL_LEN | 4,114,840 | 1.3% | 80.3% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 4,114,840 | 1.3% | 81.6% |
| ENTER_EXECUTOR LOAD_FAST | 3,853,400 | 1.3% | 82.8% |
| ENTER_EXECUTOR ENTER_EXECUTOR | 3,300,180 | 1.1% | 83.9% |
| LOAD_FAST LOAD_FAST | 2,520,400 | 0.8% | 84.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,520,340 | 0.8% | 85.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 2,520,280 | 0.8% | 86.4% |
| GET_ITER FOR_ITER_LIST | 2,515,920 | 0.8% | 87.2% |
| GET_ITER EXTENDED_ARG | 2,515,680 | 0.8% | 88.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 2,515,680 | 0.8% | 88.8% |
| RETURN_CONST POP_TOP | 2,515,680 | 0.8% | 89.6% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 2,515,660 | 0.8% | 90.5% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 2,515,640 | 0.8% | 91.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,515,640 | 0.8% | 92.1% |
| LOAD_FAST CALL_PY_WITH_DEFAULTS | 2,515,600 | 0.8% | 92.9% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 2,515,580 | 0.8% | 93.7% |
| POP_TOP LOAD_GLOBAL_MODULE | 2,515,560 | 0.8% | 94.5% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 2,515,560 | 0.8% | 95.4% |
| POP_TOP ENTER_EXECUTOR | 2,515,260 | 0.8% | 96.2% |
| FOR_ITER_LIST RETURN_CONST | 2,511,920 | 0.8% | 97.0% |
| ENTER_EXECUTOR EXTENDED_ARG | 2,511,880 | 0.8% | 97.8% |
| COMPARE_OP POP_JUMP_IF_TRUE | 2,406,140 | 0.8% | 98.6% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 2,406,100 | 0.8% | 99.4% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 1,598,940 | 0.5% | 99.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 263,880 | 0.1% | 100.0% |
| PUSH_NULL LOAD_FAST | 4,960 | 0.0% | 100.0% |
| LOAD_FAST PUSH_NULL | 4,800 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS LOAD_FAST | 4,760 | 0.0% | 100.0% |
| CALL_METHOD_DESCRIPTOR_FAST POP_TOP | 4,760 | 0.0% | 100.0% |
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
| JUMP_BACKWARD FOR_ITER_LIST | 1,280 | 0.0% | 100.0% |
| FOR_ITER FOR_ITER | 1,200 | 0.0% | 100.0% |
| COMPARE_OP COMPARE_OP | 800 | 0.0% | 100.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 680 | 0.0% | 100.0% |
| LOAD_FAST CALL | 640 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 420 | 0.0% | 100.0% |
| EXTENDED_ARG JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER | 340 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| POP_JUMP_IF_TRUE EXTENDED_ARG | 340 | 0.0% | 100.0% |
| JUMP_BACKWARD EXTENDED_ARG | 320 | 0.0% | 100.0% |
| STORE_SUBSCR_LIST_INT JUMP_BACKWARD | 320 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 300 | 0.0% | 100.0% |
| PUSH_NULL CALL | 240 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 240 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_FAST | 220 | 0.0% | 100.0% |
| CALL STORE_FAST | 180 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS STORE_FAST | 180 | 0.0% | 100.0% |


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
| LOAD_FAST | 9,149,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 4,117,340 | 45.0% |
| FOR_ITER_LIST | 2,515,920 | 27.5% |
| EXTENDED_ARG | 2,515,680 | 27.5% |
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
| LOAD_GLOBAL_MODULE | 2,515,560 | 49.9% |
| ENTER_EXECUTOR | 2,515,260 | 49.9% |
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
| LOAD_FAST | 640 | 54.2% |
| PUSH_NULL | 240 | 20.3% |
| CALL | 160 | 13.6% |
| CALL_BUILTIN_CLASS | 60 | 5.1% |
| BINARY_OP | 40 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 180 | 15.3% |
| CALL | 160 | 13.6% |
| LOAD_FAST | 160 | 13.6% |
| POP_TOP | 140 | 11.9% |
| CALL_LEN | 140 | 11.9% |


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
| LOAD_FAST_LOAD_FAST | 2,406,100 | 100.0% |
| COMPARE_OP | 800 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,406,140 | 100.0% |
| COMPARE_OP | 800 | 0.0% |
| POP_JUMP_IF_FALSE | 120 | 0.0% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 8,581,280 | 42.7% |
| STORE_SUBSCR_LIST_INT | 4,117,200 | 20.5% |
| ENTER_EXECUTOR | 3,300,180 | 16.4% |
| POP_TOP | 2,515,260 | 12.5% |
| POP_JUMP_IF_FALSE | 1,598,940 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 6,330,300 | 31.5% |
| LOAD_GLOBAL_BUILTIN | 4,117,220 | 20.5% |
| LOAD_FAST | 3,853,400 | 19.2% |
| ENTER_EXECUTOR | 3,300,180 | 16.4% |
| EXTENDED_ARG | 2,511,880 | 12.5% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,515,680 | 50.0% |
| ENTER_EXECUTOR | 2,511,880 | 50.0% |
| POP_JUMP_IF_TRUE | 340 | 0.0% |
| JUMP_BACKWARD | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,027,840 | 100.0% |
| JUMP_BACKWARD | 340 | 0.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 4,117,340 | 100.0% |
| FOR_ITER | 1,200 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |
| EXTENDED_ARG | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,117,600 | 100.0% |
| FOR_ITER | 1,200 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| FOR_ITER_LIST | 40 | 0.0% |
| FOR_ITER_RANGE | 20 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 680 | 32.1% |
| POP_TOP | 420 | 19.8% |
| EXTENDED_ARG | 340 | 16.0% |
| POP_JUMP_IF_FALSE | 340 | 16.0% |
| STORE_SUBSCR_LIST_INT | 320 | 15.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,280 | 60.4% |
| FOR_ITER | 340 | 16.0% |
| EXTENDED_ARG | 320 | 15.1% |
| ENTER_EXECUTOR | 120 | 5.7% |
| FOR_ITER_RANGE | 60 | 2.8% |


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
| LOAD_GLOBAL_BUILTIN | 14,678,540 | 24.4% |
| LOAD_FAST_LOAD_FAST | 13,263,780 | 22.0% |
| STORE_FAST | 11,669,400 | 19.4% |
| CALL_LEN | 6,443,800 | 10.7% |
| ENTER_EXECUTOR | 3,853,400 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 10,561,120 | 17.5% |
| GET_ITER | 9,149,000 | 15.2% |
| LOAD_CONST | 6,635,360 | 11.0% |
| COMPARE_OP_INT | 6,443,760 | 10.7% |
| LOAD_FAST_LOAD_FAST | 5,031,280 | 8.3% |


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
| STORE_FAST | 9,039,600 | 36.4% |
| LOAD_FAST | 5,031,280 | 20.3% |
| POP_JUMP_IF_FALSE | 4,114,880 | 16.6% |
| LOAD_GLOBAL_BUILTIN | 4,114,860 | 16.6% |
| RESUME_CHECK | 2,515,660 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,263,780 | 53.4% |
| BINARY_SUBSCR_LIST_INT | 5,031,560 | 20.3% |
| BINARY_OP | 4,114,880 | 16.6% |
| COMPARE_OP | 2,406,100 | 9.7% |
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
| COMPARE_OP_INT | 8,232,120 | 100.0% |
| COMPARE_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 4,114,880 | 50.0% |
| LOAD_FAST | 2,515,680 | 30.6% |
| ENTER_EXECUTOR | 1,598,940 | 19.4% |
| LOAD_CONST | 2,400 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 6,443,800 | 72.8% |
| COMPARE_OP | 2,406,140 | 27.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,581,280 | 97.0% |
| LOAD_FAST | 263,880 | 3.0% |
| POP_TOP | 3,760 | 0.0% |
| JUMP_BACKWARD | 680 | 0.0% |
| EXTENDED_ARG | 340 | 0.0% |


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
| BINARY_SLICE | 6,632,880 | 22.9% |
| BINARY_SUBSCR_LIST_INT | 5,031,600 | 17.4% |
| FOR_ITER_LIST | 4,922,020 | 17.0% |
| FOR_ITER | 4,117,600 | 14.2% |
| BINARY_OP | 4,114,980 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,669,400 | 40.3% |
| LOAD_FAST_LOAD_FAST | 9,039,600 | 31.2% |
| LOAD_GLOBAL_BUILTIN | 8,229,760 | 28.4% |
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
| LOAD_FAST_LOAD_FAST | 5,031,560 | 55.0% |
| LOAD_FAST | 4,114,840 | 45.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,031,600 | 55.0% |
| BINARY_OP | 4,114,860 | 45.0% |


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
| LOAD_FAST | 4,119,560 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,114,860 | 99.9% |
| LOAD_FAST | 4,760 | 0.1% |


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
| POP_JUMP_IF_FALSE | 8,232,120 | 56.1% |
| POP_JUMP_IF_TRUE | 6,443,800 | 43.9% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,330,300 | 45.6% |
| EXTENDED_ARG | 5,027,840 | 36.2% |
| GET_ITER | 2,515,920 | 18.1% |
| JUMP_BACKWARD | 1,280 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 6,441,400 | 46.4% |
| STORE_FAST | 4,922,020 | 35.5% |
| RETURN_CONST | 2,511,920 | 18.1% |
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
| ENTER_EXECUTOR | 4,117,220 | 21.9% |
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
| LOAD_FAST | 4,117,500 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,117,200 | 100.0% |
| JUMP_BACKWARD | 320 | 0.0% |


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
|     deferred | 680 | 0.0% |
|          hit | 23,836,760 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 88.0% |
| Failure | 60 | 12.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 60 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,406,260 | 14.1% |
|          hit | 14,675,920 | 85.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 9.1% |
| Failure | 800 | 90.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 780 | 97.5% |
| list | 20 | 2.5% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,117,660 | 22.9% |
|          hit | 13,875,520 | 77.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 4.8% |
| Failure | 1,200 | 95.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 1,200 | 100.0% |


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
| Basic | 177,377,680 | 57.6% |
| Not specialized | 38,478,380 | 12.5% |
| Specialized hits | 92,002,820 | 29.9% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 8,229,860 | 55.8% |
| FOR_ITER | 4,117,660 | 27.9% |
| COMPARE_OP | 2,406,260 | 16.3% |
| BINARY_SUBSCR | 2,460 | 0.0% |
| CALL | 680 | 0.0% |
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
| Frames pushed | 2,515,840 | 100.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 6,758,080 | 15.7% |
| Frees to freelist | 6,758,260 |  |
| Allocations | 36,420,300 | 84.3% |
| Allocations to 512 bytes | 32,305,260 | 74.8% |
| Allocations to 4 kbytes | 4,115,040 | 9.5% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 36,420,000 |  |
| New values | 0 |  |
| Interpreter increfs | 139,045,680 | 49.0% |
| Interpreter decrefs | 178,475,420 | 55.3% |
| Increfs | 144,781,880 | 51.0% |
| Decrefs | 144,414,960 | 44.7% |
| Materialize dict (on request) | 0 |  |
| Materialize dict (new key) | 0 |  |
| Materialize dict (too big) | 0 |  |
| Materialize dict (str subclass) | 0 |  |
| Dematerialize dict | 0 |  |
| Method cache hits | 177 |  |
| Method cache misses | 43 |  |
| Method cache collisions | 44 |  |
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
| <= 16 | 20 | 16.7% |
| <= 32 | 80 | 66.7% |
| <= 64 | 20 | 16.7% |


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
| <= 16 | 100 | 83.3% |
| <= 32 | 20 | 16.7% |


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
