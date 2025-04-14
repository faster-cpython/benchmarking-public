
# Pystats results

- benchmark: deepcopy
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 503,443,480 | 20.7% | 20.7% |  |
| STORE_FAST | 251,129,980 | 10.3% | 31.0% |  |
| LOAD_FAST_LOAD_FAST | 221,023,140 | 9.1% | 40.1% |  |
| LOAD_GLOBAL_BUILTIN | 122,674,900 | 5.0% | 45.1% |  |
| POP_JUMP_IF_FALSE | 99,737,600 | 4.1% | 49.2% |  |
| RESUME_CHECK | 98,508,880 | 4.0% | 53.3% | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 94,658,280 | 3.9% | 57.2% |  |
| RETURN_VALUE | 88,351,300 | 3.6% | 60.8% |  |
| IS_OP | 87,081,180 | 3.6% | 64.4% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 84,541,320 | 3.5% | 67.8% |  |
| CALL_BUILTIN_O | 82,697,800 | 3.4% | 71.2% |  |
| PUSH_NULL | 73,487,300 | 3.0% | 74.3% |  |
| LOAD_GLOBAL_MODULE | 57,263,980 | 2.4% | 76.6% |  |
| CALL_PY_WITH_DEFAULTS | 53,873,260 | 2.2% | 78.8% | 13.8% |
| POP_JUMP_IF_NONE | 50,257,940 | 2.1% | 80.9% |  |
| POP_JUMP_IF_NOT_NONE | 45,629,440 | 1.9% | 82.8% |  |
| JUMP_FORWARD | 45,301,780 | 1.9% | 84.6% |  |
| CALL_TYPE_1 | 41,451,460 | 1.7% | 86.3% |  |
| CALL_PY_EXACT_ARGS | 41,078,600 | 1.7% | 88.0% | 14.6% |
| ENTER_EXECUTOR | 36,367,580 | 1.5% | 89.5% |  |
| POP_TOP | 32,031,020 | 1.3% | 90.8% |  |
| STORE_SUBSCR_DICT | 27,729,600 | 1.1% | 92.0% |  |
| LOAD_CONST | 11,881,120 | 0.5% | 92.4% |  |
| GET_ITER | 10,363,780 | 0.4% | 92.9% |  |
| RETURN_CONST | 8,929,520 | 0.4% | 93.2% |  |
| NOP | 8,888,580 | 0.4% | 93.6% |  |
| BINARY_SUBSCR_DICT | 8,888,220 | 0.4% | 94.0% |  |
| BUILD_LIST | 8,847,940 | 0.4% | 94.3% |  |
| TO_BOOL_BOOL | 8,847,100 | 0.4% | 94.7% |  |
| LOAD_DEREF | 7,578,400 | 0.3% | 95.0% |  |
| CALL | 7,462,220 | 0.3% | 95.3% |  |
| LOAD_ATTR | 6,353,200 | 0.3% | 95.6% |  |
| CALL_BUILTIN_FAST | 6,348,600 | 0.3% | 95.8% |  |
| BUILD_MAP | 6,307,920 | 0.3% | 96.1% |  |
| FOR_ITER_TUPLE | 5,817,300 | 0.2% | 96.3% |  |
| LOAD_ATTR_MODULE | 5,654,520 | 0.2% | 96.6% |  |
| FOR_ITER_LIST | 5,079,560 | 0.2% | 96.8% |  |
| CALL_LIST_APPEND | 5,078,980 | 0.2% | 97.0% |  |
| FOR_ITER | 5,042,040 | 0.2% | 97.2% |  |
| STORE_FAST_STORE_FAST | 5,038,820 | 0.2% | 97.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 5,038,720 | 0.2% | 97.6% |  |
| CHECK_EXC_MATCH | 3,809,280 | 0.2% | 97.8% |  |
| POP_EXCEPT | 3,809,280 | 0.2% | 97.9% |  |
| PUSH_EXC_INFO | 3,809,280 | 0.2% | 98.1% |  |
| LIST_APPEND | 3,809,280 | 0.2% | 98.2% |  |
| CALL_FUNCTION_EX | 3,768,800 | 0.2% | 98.4% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,768,260 | 0.2% | 98.5% |  |
| INTERPRETER_EXIT | 2,539,700 | 0.1% | 98.6% |  |
| MAKE_CELL | 2,539,600 | 0.1% | 98.7% |  |
| SWAP | 2,539,520 | 0.1% | 98.9% |  |
| LIST_EXTEND | 2,498,960 | 0.1% | 99.0% |  |
| CALL_INTRINSIC_1 | 2,498,800 | 0.1% | 99.1% |  |
| CALL_ISINSTANCE | 2,498,500 | 0.1% | 99.2% |  |
| BINARY_OP_SUBTRACT_FLOAT | 2,457,680 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_FLOAT | 2,457,560 | 0.1% | 99.4% | 0.0% |
| TO_BOOL | 1,271,080 | 0.1% | 99.4% |  |
| STORE_FAST_LOAD_FAST | 1,270,200 | 0.1% | 99.5% |  |
| COPY_FREE_VARS | 1,270,080 | 0.1% | 99.5% |  |
| BUILD_TUPLE | 1,270,000 | 0.1% | 99.6% |  |
| POP_JUMP_IF_TRUE | 1,270,000 | 0.1% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 1,269,760 | 0.1% | 99.7% |  |
| TO_BOOL_NONE | 1,269,720 | 0.1% | 99.7% |  |
| MAKE_FUNCTION | 1,229,120 | 0.1% | 99.8% |  |
| SET_FUNCTION_ATTRIBUTE | 1,228,960 | 0.1% | 99.8% |  |
| RETURN_GENERATOR | 1,228,800 | 0.1% | 99.9% |  |
| YIELD_VALUE | 1,228,800 | 0.1% | 99.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 956,600 | 0.0% | 100.0% | 77.7% |
| FOR_ITER_RANGE | 289,040 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 123,420 | 0.0% | 100.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 123,120 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 123,120 | 0.0% | 100.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 41,000 | 0.0% | 100.0% | 7.8% |
| CALL_TUPLE_1 | 40,940 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 5,440 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 3,100 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 680 | 0.0% | 100.0% |  |
| RESUME | 660 | 0.0% | 100.0% | 3.0% |
| BINARY_OP | 440 | 0.0% | 100.0% |  |
| STORE_NAME | 400 | 0.0% | 100.0% |  |
| STORE_ATTR | 300 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 200 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 160 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 120 | 0.0% | 100.0% | 33.3% |
| EXIT_INIT_CHECK | 80 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 80 | 0.0% | 100.0% |  |
| LOAD_NAME | 80 | 0.0% | 100.0% |  |
| STORE_DEREF | 80 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 113,704,480 | 4.7% | 4.7% |
| STORE_FAST LOAD_FAST | 104,653,540 | 4.3% | 9.0% |
| LOAD_FAST RETURN_VALUE | 87,081,220 | 3.6% | 12.5% |
| LOAD_FAST_LOAD_FAST IS_OP | 85,811,420 | 3.5% | 16.1% |
| IS_OP POP_JUMP_IF_FALSE | 84,541,440 | 3.5% | 19.5% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 84,541,320 | 3.5% | 23.0% |
| LOAD_FAST CALL_BUILTIN_O | 64,634,160 | 2.7% | 25.7% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 57,755,120 | 2.4% | 28.0% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 53,733,060 | 2.2% | 30.3% |
| LOAD_FAST PUSH_NULL | 51,570,280 | 2.1% | 32.4% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 50,955,220 | 2.1% | 34.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 50,257,940 | 2.1% | 36.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 47,800,160 | 2.0% | 38.5% |
| POP_JUMP_IF_NONE LOAD_FAST | 47,718,400 | 2.0% | 40.5% |
| CALL_BUILTIN_O STORE_FAST | 46,899,100 | 1.9% | 42.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 46,858,000 | 1.9% | 44.3% |
| RETURN_VALUE STORE_FAST | 46,489,680 | 1.9% | 46.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 45,629,440 | 1.9% | 48.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 45,629,320 | 1.9% | 50.0% |
| STORE_FAST JUMP_FORWARD | 43,991,040 | 1.8% | 51.8% |
| STORE_FAST LOAD_GLOBAL_MODULE | 43,910,440 | 1.8% | 53.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 43,089,920 | 1.8% | 55.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST | 43,089,860 | 1.8% | 57.1% |
| LOAD_FAST_LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 43,089,800 | 1.8% | 58.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 42,680,060 | 1.8% | 60.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 41,861,120 | 1.7% | 62.4% |
| CALL_TYPE_1 STORE_FAST | 41,451,460 | 1.7% | 64.1% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 41,451,400 | 1.7% | 65.8% |
| LOAD_FAST CALL_TYPE_1 | 41,451,400 | 1.7% | 67.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_METHOD_NO_DICT | 41,451,400 | 1.7% | 69.2% |
| JUMP_FORWARD LOAD_FAST_LOAD_FAST | 40,181,760 | 1.7% | 70.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 39,737,040 | 1.6% | 72.5% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 39,696,000 | 1.6% | 74.1% |
| RESUME_CHECK LOAD_FAST | 36,372,320 | 1.5% | 75.6% |
| LOAD_FAST_LOAD_FAST CALL_PY_WITH_DEFAULTS | 25,677,040 | 1.1% | 76.6% |
| ENTER_EXECUTOR CALL_PY_WITH_DEFAULTS | 23,099,120 | 0.9% | 77.6% |
| POP_TOP ENTER_EXECUTOR | 18,021,380 | 0.7% | 78.3% |
| CALL_BUILTIN_O POP_TOP | 16,793,560 | 0.7% | 79.0% |
| RETURN_VALUE CALL_BUILTIN_O | 16,793,520 | 0.7% | 79.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 15,195,640 | 0.6% | 80.3% |
| POP_TOP LOAD_FAST | 11,427,840 | 0.5% | 80.8% |
| PUSH_NULL LOAD_FAST | 11,265,920 | 0.5% | 81.3% |
| CALL_BUILTIN_O STORE_SUBSCR_DICT | 10,116,720 | 0.4% | 81.7% |
| RETURN_VALUE LOAD_FAST_LOAD_FAST | 9,994,240 | 0.4% | 82.1% |
| LOAD_FAST_LOAD_FAST PUSH_NULL | 9,994,240 | 0.4% | 82.5% |
| RETURN_VALUE STORE_SUBSCR_DICT | 9,994,120 | 0.4% | 82.9% |
| STORE_SUBSCR_DICT ENTER_EXECUTOR | 9,993,220 | 0.4% | 83.3% |
| NOP LOAD_FAST | 8,888,320 | 0.4% | 83.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 8,888,220 | 0.4% | 84.1% |
| CALL_BUILTIN_O BINARY_SUBSCR_DICT | 8,888,120 | 0.4% | 84.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 8,847,100 | 0.4% | 84.8% |
| RETURN_CONST POP_TOP | 7,659,520 | 0.3% | 85.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 7,618,640 | 0.3% | 85.4% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 7,618,560 | 0.3% | 85.7% |
| RESUME_CHECK NOP | 7,618,500 | 0.3% | 86.0% |
| LOAD_FAST STORE_SUBSCR_DICT | 7,618,440 | 0.3% | 86.3% |
| STORE_SUBSCR_DICT LOAD_GLOBAL_MODULE | 7,618,440 | 0.3% | 86.7% |
| STORE_SUBSCR_DICT LOAD_FAST | 7,577,460 | 0.3% | 87.0% |
| BUILD_MAP STORE_FAST | 6,307,840 | 0.3% | 87.2% |
| LOAD_FAST_LOAD_FAST LOAD_GLOBAL_BUILTIN | 6,307,640 | 0.3% | 87.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 5,654,520 | 0.2% | 87.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 5,654,220 | 0.2% | 88.0% |
| LOAD_FAST LOAD_ATTR | 5,079,340 | 0.2% | 88.2% |
| CALL_LIST_APPEND RETURN_CONST | 5,078,980 | 0.2% | 88.4% |
| LOAD_FAST CALL_LIST_APPEND | 5,078,920 | 0.2% | 88.6% |
| BINARY_SUBSCR_DICT LOAD_ATTR_METHOD_NO_DICT | 5,078,920 | 0.2% | 88.8% |
| JUMP_FORWARD LOAD_GLOBAL_BUILTIN | 5,078,820 | 0.2% | 89.0% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 5,038,720 | 0.2% | 89.2% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 5,038,620 | 0.2% | 89.4% |
| GET_ITER FOR_ITER | 5,038,260 | 0.2% | 89.6% |
| BUILD_LIST LOAD_FAST | 5,038,080 | 0.2% | 89.8% |
| LOAD_FAST GET_ITER | 5,038,080 | 0.2% | 90.0% |
| ENTER_EXECUTOR LOAD_FAST | 4,996,580 | 0.2% | 90.2% |
| LOAD_FAST LOAD_CONST | 3,809,300 | 0.2% | 90.4% |
| CHECK_EXC_MATCH POP_JUMP_IF_FALSE | 3,809,280 | 0.2% | 90.6% |
| RETURN_VALUE LIST_APPEND | 3,809,280 | 0.2% | 90.7% |
| POP_JUMP_IF_FALSE POP_TOP | 3,809,280 | 0.2% | 90.9% |
| BINARY_SUBSCR_DICT PUSH_EXC_INFO | 3,809,180 | 0.2% | 91.0% |
| LOAD_GLOBAL_BUILTIN CHECK_EXC_MATCH | 3,809,180 | 0.2% | 91.2% |
| CALL_BUILTIN_FAST STORE_FAST | 3,809,160 | 0.2% | 91.3% |
| PUSH_EXC_INFO LOAD_GLOBAL_BUILTIN | 3,809,080 | 0.2% | 91.5% |
| LOAD_CONST CALL_BUILTIN_FAST | 3,809,040 | 0.2% | 91.6% |
| LOAD_FAST TO_BOOL_BOOL | 3,809,040 | 0.2% | 91.8% |
| LIST_APPEND ENTER_EXECUTOR | 3,808,600 | 0.2% | 92.0% |
| STORE_FAST_STORE_FAST LOAD_FAST | 3,768,840 | 0.2% | 92.1% |
| LOAD_FAST BUILD_LIST | 3,768,640 | 0.2% | 92.3% |
| LOAD_FAST LOAD_DEREF | 3,768,320 | 0.2% | 92.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS GET_ITER | 3,768,260 | 0.2% | 92.6% |
| RESUME_CHECK BUILD_MAP | 3,768,260 | 0.2% | 92.7% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 3,768,200 | 0.2% | 92.9% |
| PUSH_NULL CALL | 3,196,460 | 0.1% | 93.0% |
| ENTER_EXECUTOR FOR_ITER_TUPLE | 3,153,140 | 0.1% | 93.1% |
| FOR_ITER_TUPLE STORE_FAST | 2,662,980 | 0.1% | 93.3% |
| FOR_ITER_LIST STORE_FAST | 2,540,040 | 0.1% | 93.4% |
| LOAD_CONST LOAD_CONST | 2,539,760 | 0.1% | 93.5% |
| BUILD_LIST STORE_FAST | 2,539,540 | 0.1% | 93.6% |
| RESUME_CHECK BUILD_LIST | 2,539,540 | 0.1% | 93.7% |
| POP_EXCEPT RETURN_CONST | 2,539,520 | 0.1% | 93.8% |
| LOAD_ATTR STORE_FAST | 2,539,520 | 0.1% | 93.9% |
| POP_JUMP_IF_NOT_NONE BUILD_MAP | 2,539,520 | 0.1% | 94.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 100 | 50.0% |
| CALL_BUILTIN_O | 100 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 100 | 50.0% |
| BINARY_SUBSCR_DICT | 100 | 50.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,809,180 | 100.0% |
| LOAD_GLOBAL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,809,280 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,038,080 | 48.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,768,260 | 36.4% |
| CALL | 1,269,920 | 12.3% |
| LOAD_CONST | 164,100 | 1.6% |
| CALL_BUILTIN_CLASS | 123,420 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 5,038,260 | 48.6% |
| FOR_ITER_LIST | 2,539,480 | 24.5% |
| LOAD_FAST_AND_CLEAR | 1,269,760 | 12.3% |
| CALL_PY_EXACT_ARGS | 1,228,760 | 11.9% |
| FOR_ITER_TUPLE | 164,060 | 1.6% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,618,500 | 85.7% |
| STORE_FAST | 1,269,760 | 14.3% |
| POP_TOP | 240 | 0.0% |
| RESUME | 60 | 0.0% |
| JUMP_FORWARD | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,888,320 | 100.0% |
| LOAD_DEREF | 240 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 2,539,460 | 66.7% |
| POP_TOP | 1,269,760 | 33.3% |
| STORE_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,539,520 | 66.7% |
| JUMP_FORWARD | 1,269,760 | 33.3% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 16,793,560 | 52.4% |
| RETURN_CONST | 7,659,520 | 23.9% |
| POP_JUMP_IF_FALSE | 3,809,280 | 11.9% |
| CALL | 1,270,100 | 4.0% |
| CACHE | 1,228,800 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 18,021,380 | 56.3% |
| LOAD_FAST | 11,427,840 | 35.7% |
| POP_EXCEPT | 1,269,760 | 4.0% |
| RESUME_CHECK | 1,228,780 | 3.8% |
| RETURN_CONST | 41,020 | 0.1% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 3,809,180 | 100.0% |
| BINARY_SUBSCR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,809,080 | 100.0% |
| LOAD_GLOBAL | 200 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,570,280 | 70.2% |
| LOAD_FAST_LOAD_FAST | 9,994,240 | 13.6% |
| LOAD_ATTR_MODULE | 5,654,520 | 7.7% |
| LOAD_DEREF | 2,499,120 | 3.4% |
| LOAD_ATTR | 2,498,860 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 57,755,120 | 78.6% |
| LOAD_FAST | 11,265,920 | 15.3% |
| CALL | 3,196,460 | 4.3% |
| LOAD_CONST | 1,269,760 | 1.7% |
| CALL_ALLOC_AND_ENTER_INIT | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,081,220 | 98.6% |
| CALL_FUNCTION_EX | 1,228,800 | 1.4% |
| BUILD_TUPLE | 40,960 | 0.0% |
| RETURN_VALUE | 240 | 0.0% |
| EXIT_INIT_CHECK | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 46,489,680 | 52.6% |
| CALL_BUILTIN_O | 16,793,520 | 19.0% |
| LOAD_FAST_LOAD_FAST | 9,994,240 | 11.3% |
| STORE_SUBSCR_DICT | 9,994,120 | 11.3% |
| LIST_APPEND | 3,809,280 | 4.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 200 | 29.4% |
| CALL_BUILTIN_O | 200 | 29.4% |
| RETURN_VALUE | 120 | 17.6% |
| LOAD_FAST | 120 | 17.6% |
| LOAD_CONST | 40 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 320 | 47.1% |
| LOAD_FAST | 140 | 20.6% |
| POP_EXCEPT | 60 | 8.8% |
| JUMP_BACKWARD | 60 | 8.8% |
| LOAD_GLOBAL | 60 | 8.8% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,270,080 | 99.9% |
| TO_BOOL | 700 | 0.1% |
| CALL | 160 | 0.0% |
| CALL_BUILTIN_FAST | 80 | 0.0% |
| CALL_ISINSTANCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,270,060 | 99.9% |
| TO_BOOL | 700 | 0.1% |
| TO_BOOL_BOOL | 260 | 0.0% |
| TO_BOOL_NONE | 40 | 0.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 36.4% |
| LOAD_FAST | 160 | 36.4% |
| BINARY_OP | 80 | 18.2% |
| BINARY_OP_SUBTRACT_FLOAT | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 36.4% |
| BINARY_OP | 80 | 18.2% |
| LOAD_CONST | 80 | 18.2% |
| BINARY_OP_SUBTRACT_FLOAT | 80 | 18.2% |
| BINARY_OP_ADD_FLOAT | 40 | 9.1% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 100.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,768,640 | 42.6% |
| RESUME_CHECK | 2,539,540 | 28.7% |
| LOAD_FAST_LOAD_FAST | 1,269,760 | 14.4% |
| SWAP | 1,269,760 | 14.4% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,038,080 | 56.9% |
| STORE_FAST | 2,539,540 | 28.7% |
| SWAP | 1,269,760 | 14.4% |
| LOAD_CONST | 320 | 0.0% |
| LOAD_DEREF | 240 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,768,260 | 59.7% |
| POP_JUMP_IF_NOT_NONE | 2,539,520 | 40.3% |
| LOAD_CONST | 80 | 0.0% |
| RESUME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,307,840 | 100.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,229,040 | 96.8% |
| LOAD_ATTR | 40,960 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,228,960 | 96.8% |
| RETURN_VALUE | 40,960 | 3.2% |
| LOAD_FAST | 80 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 3,196,460 | 42.8% |
| ENTER_EXECUTOR | 1,719,340 | 23.0% |
| LOAD_FAST | 1,271,280 | 17.0% |
| LOAD_FAST_LOAD_FAST | 1,270,520 | 17.0% |
| CALL | 3,540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,458,240 | 32.9% |
| LOAD_FAST | 2,457,760 | 32.9% |
| POP_TOP | 1,270,100 | 17.0% |
| GET_ITER | 1,269,920 | 17.0% |
| CALL | 3,540 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 2,498,800 | 66.3% |
| LOAD_FAST | 1,270,000 | 33.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 1,269,840 | 33.7% |
| RESUME_CHECK | 1,228,900 | 32.6% |
| RETURN_VALUE | 1,228,800 | 32.6% |
| STORE_FAST | 40,960 | 1.1% |
| COPY_FREE_VARS | 240 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 2,498,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 2,498,800 | 100.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,228,780 | 96.7% |
| CACHE | 41,040 | 3.2% |
| CALL_FUNCTION_EX | 240 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 1,228,800 | 96.7% |
| RESUME_CHECK | 41,180 | 3.2% |
| RESUME | 100 | 0.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 18,021,380 | 49.6% |
| STORE_SUBSCR_DICT | 9,993,220 | 27.5% |
| LIST_APPEND | 3,808,600 | 10.5% |
| STORE_FAST | 2,538,160 | 7.0% |
| POP_JUMP_IF_TRUE | 1,228,680 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 23,099,120 | 63.5% |
| LOAD_FAST | 4,996,580 | 13.7% |
| FOR_ITER_TUPLE | 3,153,140 | 8.7% |
| FOR_ITER_LIST | 2,539,440 | 7.0% |
| CALL | 1,719,340 | 4.7% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 5,038,260 | 99.9% |
| FOR_ITER | 2,200 | 0.0% |
| JUMP_BACKWARD | 1,520 | 0.0% |
| SWAP | 40 | 0.0% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 5,038,620 | 99.9% |
| FOR_ITER | 2,200 | 0.0% |
| LOAD_FAST | 540 | 0.0% |
| STORE_FAST | 200 | 0.0% |
| UNPACK_SEQUENCE | 200 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 85,811,420 | 98.5% |
| LOAD_CONST | 1,269,760 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 84,541,440 | 97.1% |
| POP_JUMP_IF_TRUE | 1,269,980 | 1.5% |
| STORE_FAST | 1,269,760 | 1.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,360 | 25.0% |
| POP_TOP | 1,020 | 18.8% |
| STORE_SUBSCR_DICT | 960 | 17.6% |
| LIST_APPEND | 680 | 12.5% |
| FOR_ITER_TUPLE | 680 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,520 | 27.9% |
| FOR_ITER_RANGE | 1,500 | 27.6% |
| FOR_ITER_TUPLE | 1,500 | 27.6% |
| FOR_ITER_LIST | 600 | 11.0% |
| ENTER_EXECUTOR | 320 | 5.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,991,040 | 97.1% |
| POP_EXCEPT | 1,269,760 | 2.8% |
| POP_TOP | 40,960 | 0.1% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40,181,760 | 88.7% |
| LOAD_GLOBAL_BUILTIN | 5,078,820 | 11.2% |
| LOAD_FAST | 40,960 | 0.1% |
| LOAD_GLOBAL | 220 | 0.0% |
| NOP | 20 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,809,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 3,808,600 | 100.0% |
| JUMP_BACKWARD | 680 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,498,560 | 100.0% |
| LOAD_DEREF | 240 | 0.0% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 2,498,800 | 100.0% |
| LOAD_CONST | 160 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,079,340 | 79.9% |
| LOAD_GLOBAL_MODULE | 1,270,080 | 20.0% |
| LOAD_ATTR | 3,220 | 0.1% |
| LOAD_GLOBAL | 400 | 0.0% |
| BINARY_SUBSCR_DICT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,539,520 | 40.0% |
| PUSH_NULL | 2,498,860 | 39.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,269,960 | 20.0% |
| BUILD_TUPLE | 40,960 | 0.6% |
| LOAD_ATTR | 3,220 | 0.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,809,300 | 32.1% |
| LOAD_CONST | 2,539,760 | 21.4% |
| LOAD_DEREF | 1,310,720 | 11.0% |
| PUSH_NULL | 1,269,760 | 10.7% |
| BUILD_TUPLE | 1,228,960 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 3,809,040 | 32.1% |
| LOAD_CONST | 2,539,760 | 21.4% |
| IS_OP | 1,269,760 | 10.7% |
| CALL_BUILTIN_O | 1,269,680 | 10.7% |
| MAKE_FUNCTION | 1,229,120 | 10.3% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,768,320 | 49.7% |
| RESUME_CHECK | 1,310,840 | 17.3% |
| POP_JUMP_IF_FALSE | 1,269,760 | 16.8% |
| STORE_FAST | 1,228,800 | 16.2% |
| NOP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,499,120 | 33.0% |
| CALL_PY_WITH_DEFAULTS | 2,498,440 | 33.0% |
| LOAD_CONST | 1,310,720 | 17.3% |
| LOAD_GLOBAL_BUILTIN | 1,269,680 | 16.8% |
| LIST_EXTEND | 240 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 113,704,480 | 22.6% |
| STORE_FAST | 104,653,540 | 20.8% |
| LOAD_ATTR_METHOD_NO_DICT | 47,800,160 | 9.5% |
| POP_JUMP_IF_NONE | 47,718,400 | 9.5% |
| POP_JUMP_IF_NOT_NONE | 43,089,920 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 87,081,220 | 17.3% |
| CALL_BUILTIN_O | 64,634,160 | 12.8% |
| PUSH_NULL | 51,570,280 | 10.2% |
| POP_JUMP_IF_NONE | 50,257,940 | 10.0% |
| LOAD_ATTR_METHOD_NO_DICT | 46,858,000 | 9.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,269,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,269,760 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 57,755,120 | 26.1% |
| STORE_FAST | 50,955,220 | 23.1% |
| LOAD_ATTR_METHOD_NO_DICT | 43,089,860 | 19.5% |
| JUMP_FORWARD | 40,181,760 | 18.2% |
| RETURN_VALUE | 9,994,240 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 85,811,420 | 38.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 43,089,800 | 19.5% |
| CALL_PY_EXACT_ARGS | 39,696,000 | 18.0% |
| CALL_PY_WITH_DEFAULTS | 25,677,040 | 11.6% |
| PUSH_NULL | 9,994,240 | 4.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 700 | 22.6% |
| LOAD_FAST | 600 | 19.4% |
| POP_JUMP_IF_FALSE | 340 | 11.0% |
| JUMP_FORWARD | 220 | 7.1% |
| PUSH_EXC_INFO | 200 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,020 | 32.9% |
| LOAD_FAST | 740 | 23.9% |
| LOAD_GLOBAL_MODULE | 520 | 16.8% |
| LOAD_ATTR | 400 | 12.9% |
| LOAD_FAST_LOAD_FAST | 140 | 4.5% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 84,541,440 | 84.8% |
| TO_BOOL_BOOL | 8,847,100 | 8.9% |
| CHECK_EXC_MATCH | 3,809,280 | 3.8% |
| TO_BOOL | 1,270,060 | 1.3% |
| TO_BOOL_NONE | 1,269,720 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 42,680,060 | 42.8% |
| LOAD_FAST | 41,861,120 | 42.0% |
| LOAD_FAST_LOAD_FAST | 7,618,560 | 7.6% |
| POP_TOP | 3,809,280 | 3.8% |
| LOAD_DEREF | 1,269,760 | 1.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,257,940 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,718,400 | 94.9% |
| LOAD_GLOBAL_BUILTIN | 1,269,680 | 2.5% |
| LOAD_GLOBAL_MODULE | 1,269,680 | 2.5% |
| LOAD_GLOBAL | 160 | 0.0% |
| BUILD_LIST | 20 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,629,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 43,089,920 | 94.4% |
| BUILD_MAP | 2,539,520 | 5.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 1,269,980 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,228,680 | 96.7% |
| LOAD_GLOBAL_BUILTIN | 40,920 | 3.2% |
| JUMP_BACKWARD | 340 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| JUMP_FORWARD | 20 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 5,078,980 | 56.9% |
| POP_EXCEPT | 2,539,520 | 28.4% |
| FOR_ITER_TUPLE | 1,228,800 | 13.8% |
| STORE_ATTR_INSTANCE_VALUE | 41,080 | 0.5% |
| POP_TOP | 41,020 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,659,520 | 85.8% |
| INTERPRETER_EXIT | 1,269,920 | 14.2% |
| EXIT_INIT_CHECK | 80 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 220 | 73.3% |
| LOAD_FAST | 80 | 26.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 140 | 46.7% |
| RETURN_CONST | 40 | 13.3% |
| LOAD_FAST_LOAD_FAST | 40 | 13.3% |
| LOAD_GLOBAL | 40 | 13.3% |
| LOAD_CONST | 20 | 6.7% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 84,541,320 | 33.7% |
| CALL_BUILTIN_O | 46,899,100 | 18.7% |
| RETURN_VALUE | 46,489,680 | 18.5% |
| CALL_TYPE_1 | 41,451,460 | 16.5% |
| BUILD_MAP | 6,307,840 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 104,653,540 | 41.7% |
| LOAD_FAST_LOAD_FAST | 50,955,220 | 20.3% |
| JUMP_FORWARD | 43,991,040 | 17.5% |
| LOAD_GLOBAL_MODULE | 43,910,440 | 17.5% |
| ENTER_EXECUTOR | 2,538,160 | 1.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 1,270,160 | 100.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,270,200 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 5,038,720 | 100.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,768,840 | 74.8% |
| LOAD_FAST_LOAD_FAST | 1,269,980 | 25.2% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 1,269,760 | 50.0% |
| LOAD_FAST_AND_CLEAR | 1,269,760 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 1,269,760 | 50.0% |
| FOR_ITER_TUPLE | 1,269,720 | 50.0% |
| FOR_ITER | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 100 | 50.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 100 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 200 | 30.3% |
| CALL_PY_WITH_DEFAULTS | 120 | 18.2% |
| COPY_FREE_VARS | 100 | 15.2% |
| CACHE | 80 | 12.1% |
| CALL_FUNCTION_EX | 60 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 27.3% |
| LOAD_DEREF | 120 | 18.2% |
| NOP | 60 | 9.1% |
| BUILD_LIST | 60 | 9.1% |
| BUILD_MAP | 60 | 9.1% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,457,600 | 100.0% |
| BINARY_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 2,457,520 | 100.0% |
| STORE_FAST | 120 | 0.0% |
| BINARY_OP | 40 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 8,888,120 | 100.0% |
| BINARY_SUBSCR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,078,920 | 57.1% |
| PUSH_EXC_INFO | 3,809,180 | 42.9% |
| LOAD_ATTR | 120 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,200 | 99.8% |
| LOAD_FAST | 120 | 0.1% |
| CALL | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 123,420 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,634,160 | 78.2% |
| RETURN_VALUE | 16,793,520 | 20.3% |
| LOAD_CONST | 1,269,680 | 1.5% |
| CALL | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 46,899,100 | 56.7% |
| POP_TOP | 16,793,560 | 20.3% |
| STORE_SUBSCR_DICT | 10,116,720 | 12.2% |
| BINARY_SUBSCR_DICT | 8,888,120 | 10.7% |
| STORE_SUBSCR | 200 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,078,920 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,078,980 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 43,089,800 | 51.0% |
| LOAD_FAST | 41,451,400 | 49.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 84,541,320 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,768,200 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,768,260 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 39,696,000 | 96.6% |
| GET_ITER | 1,228,760 | 3.0% |
| CALL_PY_WITH_DEFAULTS | 112,800 | 0.3% |
| LOAD_FAST | 40,920 | 0.1% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 39,737,040 | 96.7% |
| COPY_FREE_VARS | 1,228,780 | 3.0% |
| CALL_PY_WITH_DEFAULTS | 112,760 | 0.3% |
| RESUME | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 25,677,040 | 47.7% |
| ENTER_EXECUTOR | 23,099,120 | 42.9% |
| LOAD_DEREF | 2,498,440 | 4.6% |
| LOAD_FAST | 2,458,240 | 4.6% |
| CALL_PY_EXACT_ARGS | 112,760 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 53,733,060 | 99.7% |
| CALL_PY_EXACT_ARGS | 112,800 | 0.2% |
| CALL_PY_WITH_DEFAULTS | 27,280 | 0.1% |
| RESUME | 120 | 0.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,920 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40,940 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,451,400 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 41,451,460 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,539,480 | 50.0% |
| ENTER_EXECUTOR | 2,539,440 | 50.0% |
| JUMP_BACKWARD | 600 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540,040 | 50.0% |
| LOAD_FAST | 2,539,520 | 50.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 164,020 | 56.7% |
| GET_ITER | 123,420 | 42.7% |
| JUMP_BACKWARD | 1,500 | 0.5% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 124,960 | 43.2% |
| ENTER_EXECUTOR | 122,540 | 42.4% |
| LOAD_CONST | 40,960 | 14.2% |
| JUMP_BACKWARD | 340 | 0.1% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 3,153,140 | 54.2% |
| SWAP | 1,269,720 | 21.8% |
| LOAD_FAST | 1,228,780 | 21.1% |
| GET_ITER | 164,060 | 2.8% |
| JUMP_BACKWARD | 1,500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,662,980 | 45.8% |
| STORE_FAST_LOAD_FAST | 1,270,160 | 21.8% |
| RETURN_CONST | 1,228,800 | 21.1% |
| ENTER_EXECUTOR | 654,680 | 11.3% |
| JUMP_BACKWARD | 680 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 46,858,000 | 49.5% |
| LOAD_GLOBAL_MODULE | 41,451,400 | 43.8% |
| BINARY_SUBSCR_DICT | 5,078,920 | 5.4% |
| LOAD_ATTR | 1,269,960 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,800,160 | 50.5% |
| LOAD_FAST_LOAD_FAST | 43,089,860 | 45.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,768,200 | 4.0% |
| CALL | 60 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 5,654,220 | 100.0% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 5,654,520 | 100.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 45,629,320 | 37.2% |
| POP_JUMP_IF_FALSE | 42,680,060 | 34.8% |
| LOAD_FAST | 15,195,640 | 12.4% |
| LOAD_FAST_LOAD_FAST | 6,307,640 | 5.1% |
| JUMP_FORWARD | 5,078,820 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,704,480 | 92.7% |
| CHECK_EXC_MATCH | 3,809,180 | 3.1% |
| CALL_ISINSTANCE | 2,498,440 | 2.0% |
| LOAD_FAST_LOAD_FAST | 1,269,720 | 1.0% |
| CALL_BUILTIN_FAST | 1,269,680 | 1.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 43,910,440 | 76.7% |
| STORE_SUBSCR_DICT | 7,618,440 | 13.3% |
| LOAD_FAST | 2,457,520 | 4.3% |
| POP_JUMP_IF_FALSE | 1,269,680 | 2.2% |
| POP_JUMP_IF_NONE | 1,269,680 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 41,451,400 | 72.4% |
| LOAD_FAST_LOAD_FAST | 8,888,220 | 15.5% |
| LOAD_ATTR_MODULE | 5,654,220 | 9.9% |
| LOAD_ATTR | 1,270,080 | 2.2% |
| LOAD_CONST | 60 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 53,733,060 | 54.5% |
| CALL_PY_EXACT_ARGS | 39,737,040 | 40.3% |
| CACHE | 1,269,780 | 1.3% |
| MAKE_CELL | 1,269,780 | 1.3% |
| CALL_FUNCTION_EX | 1,228,900 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 45,629,320 | 46.3% |
| LOAD_FAST | 36,372,320 | 36.9% |
| NOP | 7,618,500 | 7.7% |
| BUILD_MAP | 3,768,260 | 3.8% |
| BUILD_LIST | 2,539,540 | 2.6% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 10,116,720 | 36.5% |
| RETURN_VALUE | 9,994,120 | 36.0% |
| LOAD_FAST | 7,618,440 | 27.5% |
| STORE_SUBSCR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 9,993,220 | 36.0% |
| LOAD_GLOBAL_MODULE | 7,618,440 | 27.5% |
| LOAD_FAST | 7,577,460 | 27.3% |
| POP_EXCEPT | 2,539,460 | 9.2% |
| JUMP_BACKWARD | 960 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 5,038,620 | 100.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 5,038,720 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,269,780 | 50.0% |
| POP_TOP | 1,228,800 | 48.4% |
| COPY_FREE_VARS | 41,040 | 1.6% |
| RESUME | 80 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,269,920 | 50.0% |
| YIELD_VALUE | 1,228,800 | 48.4% |
| RETURN_VALUE | 40,980 | 1.6% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 80 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,229,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 1,228,960 | 100.0% |
| STORE_NAME | 160 | 0.0% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 80 | 100.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,269,840 | 50.0% |
| MAKE_CELL | 1,269,760 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,269,780 | 50.0% |
| MAKE_CELL | 1,269,760 | 50.0% |
| RESUME | 60 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 1,228,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,800 | 100.0% |
| LOAD_CONST | 80 | 0.0% |
| STORE_NAME | 80 | 0.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 80 | 100.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 160 | 40.0% |
| LOAD_CONST | 80 | 20.0% |
| LOAD_NAME | 80 | 20.0% |
| SET_FUNCTION_ATTRIBUTE | 80 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 60.0% |
| LOAD_FAST | 80 | 20.0% |
| RETURN_CONST | 80 | 20.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 40 | 33.3% |
| CALL | 40 | 33.3% |
| LOAD_CONST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 66.7% |
| STORE_FAST | 40 | 33.3% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,809,040 | 60.0% |
| LOAD_FAST | 1,269,680 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 1,269,680 | 20.0% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,809,160 | 60.0% |
| TO_BOOL_BOOL | 2,539,360 | 40.0% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 60 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,498,440 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,498,440 | 100.0% |
| TO_BOOL | 60 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,920 | 99.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 60 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,940 | 99.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 60 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 695,940 | 72.8% |
| LOAD_FAST_LOAD_FAST | 164,520 | 17.2% |
| LOAD_FAST | 82,000 | 8.6% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 1.5% |
| STORE_ATTR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 737,500 | 77.1% |
| LOAD_GLOBAL_BUILTIN | 122,840 | 12.8% |
| RETURN_CONST | 41,080 | 4.3% |
| LOAD_CONST | 41,020 | 4.3% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 1.5% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,809,040 | 43.1% |
| CALL_BUILTIN_FAST | 2,539,360 | 28.7% |
| CALL_ISINSTANCE | 2,498,440 | 28.2% |
| TO_BOOL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,847,100 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,269,680 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,269,720 | 100.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,228,800 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,228,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,228,800 | 100.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 2,457,520 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,457,560 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 123,100 | 100.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,120 | 100.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,100 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 123,120 | 100.0% |


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
|     deferred | 340 | 0.0% |
|          hit | 4,915,180 | 100.0% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 75.0% |
| Failure | 40 | 25.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| multiply different types | 40 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 8,888,220 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20,605,440 | 6.3% |
|          hit | 308,140,600 | 93.7% |
|         miss | 13,401,280 | 4.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 254,520 | 98.6% |
| Failure | 3,540 | 1.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc noargs | 2,140 | 60.5% |
| meth descr varargs keywords | 700 | 19.8% |
| class no vectorcall | 700 | 19.8% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,039,600 | 31.1% |
|          hit | 11,185,900 | 68.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 9.8% |
| Failure | 2,200 | 90.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 1,500 | 68.2% |
| zip | 700 | 31.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,352,580 | 5.8% |
|          hit | 102,765,460 | 94.2% |
|         miss | 3,180 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 680 | 17.9% |
| Failure | 3,120 | 82.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 1,720 | 55.1% |
| class attr descriptor | 900 | 28.8% |
| metaclass attribute | 500 | 16.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,560 | 0.0% |
|          hit | 179,938,880 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,540 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


</details>

### POP_JUMP_IF_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NONE family </summary>


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> specialization stats for POP_JUMP_IF_NOT_NONE family </summary>


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> specialization stats for POP_JUMP_IF_TRUE family </summary>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 729,680 | 50.4% |
|          hit | 704,340 | 48.6% |
|         miss | 743,520 | 51.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 14,140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 28,343,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,270,080 | 11.2% |
|          hit | 10,116,820 | 88.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 30.0% |
| Failure | 700 | 70.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 700 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 13,721,500 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 1,447,678,040 | 59.5% |
| Not specialized | 217,028,440 | 8.9% |
| Specialized hits | 755,232,160 | 31.0% |
| Specialized misses | 14,148,060 | 0.6% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 20,605,440 | 60.6% |
| LOAD_ATTR | 6,352,580 | 18.7% |
| FOR_ITER | 5,039,600 | 14.8% |
| TO_BOOL | 1,270,080 | 3.7% |
| STORE_ATTR | 729,680 | 2.1% |
| LOAD_GLOBAL | 1,560 | 0.0% |
| STORE_SUBSCR | 340 | 0.0% |
| BINARY_OP | 340 | 0.0% |
| BINARY_SUBSCR | 100 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 7,424,240 | 52.5% |
| CALL_PY_EXACT_ARGS | 5,977,000 | 42.2% |
| STORE_ATTR_INSTANCE_VALUE | 743,520 | 5.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,180 | 0.0% |
| BINARY_OP_ADD_FLOAT | 60 | 0.0% |
| CALL_ALLOC_AND_ENTER_INIT | 40 | 0.0% |
| RESUME | 20 | 0.0% |
| RESUME_CHECK | 20 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| GET_ITER | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 2,539,700 | 2.5% |
| Calls to Python functions inlined | 97,198,640 | 97.5% |
| Calls via PyEval_EvalFrame (total) | 2,539,700 | 2.5% |
| Calls via PyEval_EvalFrame (vector) | 82,100 | 0.1% |
| Calls via PyEval_EvalFrame (generator) | 2,457,600 | 2.5% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 82,020 | 0.1% |
| Calls via PyEval_EvalFrame (build class) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 2,499,040 | 2.5% |
| Calls via PyEval_EvalFrame (api) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 20 | 0.0% |
| Frame objects created | 3,809,280 | 3.8% |
| Frames pushed | 97,280,820 | 97.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 44,660,680 | 27.3% |
| Frees to freelist | 44,700,380 |  |
| Allocations | 118,685,340 | 72.7% |
| Allocations to 512 bytes | 118,684,980 | 72.7% |
| Allocations to 4 kbytes | 360 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 122,453,762 |  |
| New values | 1,269,840 |  |
| Interpreter increfs | 1,098,924,720 | 77.1% |
| Interpreter decrefs | 1,336,576,080 | 84.9% |
| Increfs | 326,529,881 | 22.9% |
| Decrefs | 238,384,432 | 15.1% |
| Materialize dict (on request) | 1,895,840 | 149.3% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 625,920 | 49.3% |
| Method cache hits | 5,784,085 |  |
| Method cache misses | 495 |  |
| Method cache collisions | 1,098 |  |
| Method cache dunder hits | 21,303,786 |  |
| Method cache dunder misses | 974 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 360 | 15,240 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 320 |  |
| Traces created | 320 | 100.0% |
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
| <= 16 | 40 | 12.5% |
| <= 32 | 220 | 68.8% |
| <= 64 | 40 | 12.5% |
| <= 128 | 20 | 6.2% |


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
| <= 16 | 240 | 75.0% |
| <= 32 | 40 | 12.5% |
| <= 64 | 40 | 12.5% |


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
| CALL_PY_WITH_DEFAULTS | 200 |
| CALL | 100 |


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
| Number of data files | 60 |


</details>

---
Stats gathered on: 2024-09-10
