
# Pystats results

- benchmark: telco
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 108,891,100 | 41.0% | 41.0% |  |
| STORE_FAST | 51,248,860 | 19.3% | 60.2% |  |
| BINARY_OP | 35,240,300 | 13.3% | 73.5% |  |
| CALL | 16,019,040 | 6.0% | 79.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 9,608,920 | 3.6% | 83.1% |  |
| LOAD_CONST | 6,413,000 | 2.4% | 85.5% |  |
| POP_TOP | 6,403,100 | 2.4% | 87.9% |  |
| POP_JUMP_IF_FALSE | 6,401,600 | 2.4% | 90.4% |  |
| LOAD_GLOBAL_BUILTIN | 6,401,480 | 2.4% | 92.8% |  |
| ENTER_EXECUTOR | 6,400,640 | 2.4% | 95.2% |  |
| CALL_KW | 6,400,080 | 2.4% | 97.6% |  |
| TO_BOOL_INT | 6,399,980 | 2.4% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 5,240 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,520 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 4,460 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 3,300 | 0.0% | 100.0% |  |
| LOAD_ATTR | 2,240 | 0.0% | 100.0% |  |
| COMPARE_OP | 1,700 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 1,580 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 1,580 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 1,580 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 1,440 | 0.0% | 100.0% |  |
| GET_ITER | 1,360 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 920 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 800 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 680 | 0.0% | 100.0% |  |
| PUSH_NULL | 560 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 300 | 0.0% | 100.0% |  |
| LOAD_DEREF | 240 | 0.0% | 100.0% |  |
| RETURN_VALUE | 160 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 160 | 0.0% | 100.0% |  |
| RESUME_CHECK | 120 | 0.0% | 100.0% |  |
| STORE_ATTR | 100 | 0.0% | 100.0% |  |
| BEFORE_WITH | 80 | 0.0% | 100.0% |  |
| NOP | 80 | 0.0% | 100.0% |  |
| BUILD_LIST | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 80 | 0.0% | 100.0% |  |
| FOR_ITER | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 40 | 0.0% | 100.0% |  |
| TO_BOOL | 40 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 40 | 0.0% | 100.0% |  |
| RESUME | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| STORE_FAST LOAD_FAST | 44,844,300 | 16.9% | 16.9% |
| LOAD_FAST LOAD_FAST | 41,630,080 | 15.7% | 32.5% |
| LOAD_FAST BINARY_OP | 35,228,520 | 13.3% | 45.8% |
| BINARY_OP STORE_FAST | 35,228,480 | 13.3% | 59.0% |
| CALL STORE_FAST | 16,013,340 | 6.0% | 65.1% |
| LOAD_FAST CALL | 9,610,640 | 3.6% | 68.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 9,608,920 | 3.6% | 72.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 9,608,880 | 3.6% | 75.9% |
| LOAD_FAST LOAD_CONST | 6,403,280 | 2.4% | 78.3% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 6,401,280 | 2.4% | 80.7% |
| POP_TOP ENTER_EXECUTOR | 6,400,600 | 2.4% | 83.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 6,400,100 | 2.4% | 85.5% |
| LOAD_CONST CALL_KW | 6,400,080 | 2.4% | 87.9% |
| CALL_KW POP_TOP | 6,400,000 | 2.4% | 90.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 6,400,000 | 2.4% | 92.7% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 6,399,980 | 2.4% | 95.2% |
| LOAD_FAST TO_BOOL_INT | 6,399,960 | 2.4% | 97.6% |
| ENTER_EXECUTOR CALL | 6,399,300 | 2.4% | 100.0% |
| BINARY_OP BINARY_OP | 10,180 | 0.0% | 100.0% |
| CALL CALL | 5,020 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_CONST | 4,760 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR_METHOD_LAZY_DICT | 4,380 | 0.0% | 100.0% |
| LOAD_CONST CALL | 3,500 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_LAZY_DICT LOAD_CONST | 3,200 | 0.0% | 100.0% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST | 3,140 | 0.0% | 100.0% |
| CALL_METHOD_DESCRIPTOR_FAST POP_TOP | 2,880 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,720 | 0.0% | 100.0% |
| FOR_ITER_RANGE STORE_FAST | 1,940 | 0.0% | 100.0% |
| LOAD_FAST LOAD_ATTR | 1,920 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_FAST | 1,640 | 0.0% | 100.0% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 1,640 | 0.0% | 100.0% |
| BINARY_OP LOAD_FAST | 1,600 | 0.0% | 100.0% |
| COMPARE_OP POP_JUMP_IF_FALSE | 1,600 | 0.0% | 100.0% |
| LOAD_CONST BINARY_OP | 1,600 | 0.0% | 100.0% |
| LOAD_CONST COMPARE_OP | 1,600 | 0.0% | 100.0% |
| LOAD_CONST LOAD_FAST | 1,600 | 0.0% | 100.0% |
| BINARY_SUBSCR_LIST_INT STORE_FAST | 1,580 | 0.0% | 100.0% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST | 1,580 | 0.0% | 100.0% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 1,560 | 0.0% | 100.0% |
| LOAD_FAST CALL_BUILTIN_FAST | 1,560 | 0.0% | 100.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,560 | 0.0% | 100.0% |
| CALL_BUILTIN_FAST UNPACK_SEQUENCE_TUPLE | 1,560 | 0.0% | 100.0% |
| CALL_BUILTIN_CLASS GET_ITER | 1,320 | 0.0% | 100.0% |
| POP_TOP LOAD_FAST | 1,280 | 0.0% | 100.0% |
| ENTER_EXECUTOR FOR_ITER_RANGE | 1,280 | 0.0% | 100.0% |
| LOAD_CONST CALL_BUILTIN_CLASS | 1,280 | 0.0% | 100.0% |
| FOR_ITER_RANGE LOAD_FAST | 1,280 | 0.0% | 100.0% |
| GET_ITER FOR_ITER_RANGE | 1,260 | 0.0% | 100.0% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 1,260 | 0.0% | 100.0% |
| LOAD_ATTR_METHOD_LAZY_DICT CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 0.0% | 100.0% |
| STORE_FAST LOAD_GLOBAL | 480 | 0.0% | 100.0% |
| EXTENDED_ARG FOR_ITER_RANGE | 420 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL_MODULE | 380 | 0.0% | 100.0% |
| POP_TOP EXTENDED_ARG | 340 | 0.0% | 100.0% |
| POP_TOP JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| EXTENDED_ARG JUMP_BACKWARD | 340 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_MODULE | 340 | 0.0% | 100.0% |
| PUSH_NULL CALL | 320 | 0.0% | 100.0% |
| JUMP_BACKWARD EXTENDED_ARG | 320 | 0.0% | 100.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 300 | 0.0% | 100.0% |
| LOAD_ATTR_MODULE PUSH_NULL | 300 | 0.0% | 100.0% |
| CALL POP_TOP | 220 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_CONST | 200 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 200 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST | 160 | 0.0% | 100.0% |
| LOAD_CONST LOAD_CONST | 160 | 0.0% | 100.0% |
| LOAD_DEREF PUSH_NULL | 160 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR | 120 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL_BUILTIN | 120 | 0.0% | 100.0% |
| CALL CALL_METHOD_DESCRIPTOR_FAST | 100 | 0.0% | 100.0% |
| COMPARE_OP COMPARE_OP | 100 | 0.0% | 100.0% |
| LOAD_ATTR PUSH_NULL | 100 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_MODULE | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_ATTR | 100 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 100 | 0.0% | 100.0% |
| BEFORE_WITH STORE_FAST | 80 | 0.0% | 100.0% |
| GET_ITER EXTENDED_ARG | 80 | 0.0% | 100.0% |
| NOP LOAD_DEREF | 80 | 0.0% | 100.0% |
| POP_TOP NOP | 80 | 0.0% | 100.0% |
| POP_TOP LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| PUSH_NULL LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |
| RETURN_VALUE RETURN_VALUE | 80 | 0.0% | 100.0% |
| BUILD_LIST LOAD_DEREF | 80 | 0.0% | 100.0% |
| CALL LOAD_FAST | 80 | 0.0% | 100.0% |
| CALL STORE_ATTR | 80 | 0.0% | 100.0% |
| CALL CALL_BUILTIN_CLASS | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX COPY_FREE_VARS | 80 | 0.0% | 100.0% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| CALL_KW STORE_FAST | 80 | 0.0% | 100.0% |
| LIST_EXTEND CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |
| LOAD_ATTR LOAD_ATTR_METHOD_LAZY_DICT | 80 | 0.0% | 100.0% |
| LOAD_DEREF LIST_EXTEND | 80 | 0.0% | 100.0% |
| LOAD_FAST BUILD_LIST | 80 | 0.0% | 100.0% |
| LOAD_FAST CALL_FUNCTION_EX | 80 | 0.0% | 100.0% |
| LOAD_FAST_CHECK CALL | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL LOAD_GLOBAL | 80 | 0.0% | 100.0% |
| STORE_FAST LOAD_CONST | 80 | 0.0% | 100.0% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_MODULE | 80 | 0.0% | 100.0% |
| CALL_FUNCTION_EX RESUME_CHECK | 60 | 0.0% | 100.0% |
| COPY_FREE_VARS RESUME_CHECK | 60 | 0.0% | 100.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 50.0% |
| BINARY_SUBSCR_LIST_INT | 20 | 50.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 1,320 | 97.1% |
| CALL | 40 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 1,260 | 92.6% |
| EXTENDED_ARG | 80 | 5.9% |
| FOR_ITER | 20 | 1.5% |


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
| CALL_KW | 6,400,000 | 100.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,880 | 0.0% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,400,600 | 100.0% |
| LOAD_FAST | 1,280 | 0.0% |
| LOAD_GLOBAL_MODULE | 380 | 0.0% |
| EXTENDED_ARG | 340 | 0.0% |
| JUMP_BACKWARD | 340 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 300 | 53.6% |
| LOAD_DEREF | 160 | 28.6% |
| LOAD_ATTR | 100 | 17.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 320 | 57.1% |
| LOAD_FAST | 160 | 28.6% |
| LOAD_FAST_CHECK | 80 | 14.3% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 37.5% |
| BINARY_OP | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 50.0% |
| TO_BOOL_INT | 20 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,228,520 | 100.0% |
| BINARY_OP | 10,180 | 0.0% |
| LOAD_CONST | 1,600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 35,228,480 | 100.0% |
| BINARY_OP | 10,180 | 0.0% |
| LOAD_FAST | 1,600 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |
| BINARY_OP_SUBTRACT_FLOAT | 20 | 0.0% |


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
| LOAD_FAST | 9,610,640 | 60.0% |
| ENTER_EXECUTOR | 6,399,300 | 39.9% |
| CALL | 5,020 | 0.0% |
| LOAD_CONST | 3,500 | 0.0% |
| PUSH_NULL | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,013,340 | 100.0% |
| CALL | 5,020 | 0.0% |
| POP_TOP | 220 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 100 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


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

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,400,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,400,000 | 100.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,600 | 94.1% |
| COMPARE_OP | 100 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,600 | 94.1% |
| COMPARE_OP | 100 | 5.9% |


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
| POP_TOP | 6,400,600 | 100.0% |
| JUMP_BACKWARD | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 6,399,300 | 100.0% |
| FOR_ITER_RANGE | 1,280 | 0.0% |
| EXTENDED_ARG | 60 | 0.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 42.5% |
| JUMP_BACKWARD | 320 | 40.0% |
| GET_ITER | 80 | 10.0% |
| ENTER_EXECUTOR | 60 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 420 | 52.5% |
| JUMP_BACKWARD | 340 | 42.5% |
| FOR_ITER | 40 | 5.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 40 | 50.0% |
| GET_ITER | 20 | 25.0% |
| JUMP_BACKWARD | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 50.0% |
| FOR_ITER_RANGE | 40 | 50.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 340 | 50.0% |
| EXTENDED_ARG | 340 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 320 | 47.1% |
| FOR_ITER_RANGE | 300 | 44.1% |
| ENTER_EXECUTOR | 40 | 5.9% |
| FOR_ITER | 20 | 2.9% |


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
| LOAD_FAST | 1,920 | 85.7% |
| LOAD_ATTR | 120 | 5.4% |
| LOAD_GLOBAL | 100 | 4.5% |
| LOAD_GLOBAL_MODULE | 100 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,640 | 73.2% |
| LOAD_ATTR | 120 | 5.4% |
| PUSH_NULL | 100 | 4.5% |
| LOAD_ATTR_MODULE | 100 | 4.5% |
| LOAD_ATTR_METHOD_LAZY_DICT | 80 | 3.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,403,280 | 99.8% |
| LOAD_GLOBAL_MODULE | 4,760 | 0.1% |
| LOAD_ATTR_METHOD_LAZY_DICT | 3,200 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 1,260 | 0.0% |
| LOAD_GLOBAL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_KW | 6,400,080 | 99.8% |
| CALL | 3,500 | 0.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,140 | 0.0% |
| BINARY_OP | 1,600 | 0.0% |
| COMPARE_OP | 1,600 | 0.0% |


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
| STORE_FAST | 44,844,300 | 41.2% |
| LOAD_FAST | 41,630,080 | 38.2% |
| LOAD_ATTR_METHOD_NO_DICT | 9,608,920 | 8.8% |
| LOAD_GLOBAL_BUILTIN | 6,400,100 | 5.9% |
| POP_JUMP_IF_FALSE | 6,400,000 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,630,080 | 38.2% |
| BINARY_OP | 35,228,520 | 32.4% |
| CALL | 9,610,640 | 8.8% |
| LOAD_ATTR_METHOD_NO_DICT | 9,608,880 | 8.8% |
| LOAD_CONST | 6,403,280 | 5.9% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 100.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 52.2% |
| POP_TOP | 80 | 8.7% |
| LOAD_GLOBAL | 80 | 8.7% |
| RETURN_VALUE | 40 | 4.3% |
| POP_JUMP_IF_FALSE | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 340 | 37.0% |
| LOAD_CONST | 200 | 21.7% |
| LOAD_GLOBAL_BUILTIN | 120 | 13.0% |
| LOAD_ATTR | 100 | 10.9% |
| LOAD_GLOBAL | 80 | 8.7% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 6,399,980 | 100.0% |
| COMPARE_OP | 1,600 | 0.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,400,000 | 100.0% |
| LOAD_GLOBAL_MODULE | 1,560 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 80.0% |
| STORE_ATTR | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 40.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 40.0% |
| STORE_ATTR | 20 | 20.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 35,228,480 | 68.7% |
| CALL | 16,013,340 | 31.2% |
| FOR_ITER_RANGE | 1,940 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,640 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 1,580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,844,300 | 87.5% |
| LOAD_GLOBAL_BUILTIN | 6,401,280 | 12.5% |
| LOAD_GLOBAL_MODULE | 2,720 | 0.0% |
| LOAD_GLOBAL | 480 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 50.0% |
| CALL_BUILTIN_FAST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 50.0% |
| UNPACK_SEQUENCE_TUPLE | 20 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 20 | 50.0% |
| COPY_FREE_VARS | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 20 | 50.0% |
| LOAD_GLOBAL | 20 | 50.0% |


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

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,560 | 98.7% |
| BINARY_SUBSCR | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,580 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,280 | 88.9% |
| CALL | 80 | 5.6% |
| LOAD_FAST | 40 | 2.8% |
| CALL_BUILTIN_CLASS | 40 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,320 | 91.7% |
| STORE_FAST | 60 | 4.2% |
| CALL_BUILTIN_CLASS | 40 | 2.8% |
| CALL | 20 | 1.4% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,560 | 98.7% |
| CALL | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 1,560 | 98.7% |
| UNPACK_SEQUENCE | 20 | 1.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BEFORE_WITH | 60 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,140 | 69.5% |
| LOAD_ATTR_METHOD_LAZY_DICT | 1,240 | 27.4% |
| CALL | 100 | 2.2% |
| LOAD_ATTR | 40 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,880 | 63.7% |
| STORE_FAST | 1,640 | 36.3% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,280 | 38.8% |
| GET_ITER | 1,260 | 38.2% |
| EXTENDED_ARG | 420 | 12.7% |
| JUMP_BACKWARD | 300 | 9.1% |
| FOR_ITER | 40 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,940 | 58.8% |
| LOAD_FAST | 1,280 | 38.8% |
| LOAD_GLOBAL | 40 | 1.2% |
| LOAD_GLOBAL_MODULE | 40 | 1.2% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,380 | 98.2% |
| LOAD_ATTR | 80 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,200 | 71.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 27.8% |
| CALL | 20 | 0.4% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,608,880 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,608,920 | 100.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 200 | 66.7% |
| LOAD_ATTR | 100 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 300 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,401,280 | 100.0% |
| LOAD_GLOBAL | 120 | 0.0% |
| STORE_ATTR | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,400,100 | 100.0% |
| LOAD_CONST | 1,260 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,720 | 51.9% |
| POP_JUMP_IF_FALSE | 1,560 | 29.8% |
| POP_TOP | 380 | 7.3% |
| LOAD_GLOBAL | 340 | 6.5% |
| LOAD_GLOBAL_MODULE | 80 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,760 | 90.8% |
| LOAD_ATTR_MODULE | 200 | 3.8% |
| LOAD_ATTR | 100 | 1.9% |
| LOAD_GLOBAL_MODULE | 80 | 1.5% |
| CALL | 60 | 1.1% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 60 | 50.0% |
| COPY_FREE_VARS | 60 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 60 | 50.0% |
| LOAD_GLOBAL_MODULE | 40 | 33.3% |
| LOAD_GLOBAL | 20 | 16.7% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,399,960 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,399,980 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 1,560 | 98.7% |
| UNPACK_SEQUENCE | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,580 | 100.0% |


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
|     deferred | 35,230,100 | 100.0% |
|          hit | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 0.2% |
| Failure | 10,180 | 99.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 7,240 | 71.1% |
| multiply other | 2,740 | 26.9% |
| and int | 100 | 1.0% |
| multiply different types | 100 | 1.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 6,399,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,013,820 | 55.6% |
|          hit | 12,805,300 | 44.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 4.2% |
| Failure | 5,000 | 95.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs keywords | 2,740 | 54.8% |
| cfunc varargs | 1,780 | 35.6% |
| class no vectorcall | 400 | 8.0% |
| cfunc noargs | 80 | 1.6% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,600 | 94.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 0 | 0.0% |
| Failure | 100 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 100 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 1.2% |
|          hit | 3,300 | 97.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,900 | 0.0% |
|          hit | 16,012,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 64.7% |
| Failure | 120 | 35.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 100 | 83.3% |
| not managed dict | 20 | 16.7% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 460 | 0.0% |
|          hit | 6,406,720 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 80.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 0 | 0.0% |
| Failure | 20 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 20 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 6,399,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 6,399,980 | 100.0% |

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
| Basic | 185,761,340 | 69.9% |
| Not specialized | 57,666,100 | 21.7% |
| Specialized hits | 22,434,620 | 8.4% |
| Specialized misses | 0 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_OP | 35,230,100 | 68.7% |
| CALL | 16,013,820 | 31.2% |
| LOAD_ATTR | 1,900 | 0.0% |
| COMPARE_OP | 1,600 | 0.0% |
| LOAD_GLOBAL | 460 | 0.0% |
| STORE_ATTR | 80 | 0.0% |
| FOR_ITER | 40 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |
| TO_BOOL | 20 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


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
| Calls to Python functions inlined | 160 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 100.0% |
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
| Allocations from freelist | 28,814,440 | 20.8% |
| Frees to freelist | 28,814,440 |  |
| Allocations | 110,035,040 | 79.2% |
| Allocations to 512 bytes | 110,034,860 | 79.2% |
| Allocations to 4 kbytes | 20 | 0.0% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 110,034,693 |  |
| New values | 200 |  |
| Interpreter increfs | 131,311,860 | 24.4% |
| Interpreter decrefs | 201,759,760 | 30.0% |
| Increfs | 407,902,226 | 75.6% |
| Decrefs | 469,898,459 | 70.0% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 19,202,140 |  |
| Method cache misses | 220 |  |
| Method cache collisions | 170 |  |
| Method cache dunder hits | 236 |  |
| Method cache dunder misses | 4 |  |


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
| Inner loop found | 0 | 0.0% |
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
| <= 32 | 20 | 50.0% |
| <= 64 | 0 | 0.0% |
| <= 128 | 20 | 50.0% |


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
| <= 32 | 20 | 50.0% |
| <= 64 | 20 | 50.0% |


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

|Opcode | Count | 
|---|---:|
| CALL | 40 |


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
