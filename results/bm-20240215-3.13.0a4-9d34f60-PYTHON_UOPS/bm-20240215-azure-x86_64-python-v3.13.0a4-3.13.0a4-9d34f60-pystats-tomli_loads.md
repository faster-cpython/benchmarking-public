
# Pystats results

- benchmark: tomli_loads
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 1,886,997,740 | 14.9% | 14.9% |  |
| LOAD_FAST_LOAD_FAST | 1,258,420,300 | 9.9% | 24.8% |  |
| STORE_FAST | 1,154,295,560 | 9.1% | 33.9% |  |
| LOAD_CONST | 894,146,820 | 7.0% | 40.9% |  |
| POP_JUMP_IF_FALSE | 884,618,960 | 7.0% | 47.9% |  |
| LOAD_GLOBAL_MODULE | 581,922,320 | 4.6% | 52.5% |  |
| CONTAINS_OP | 467,976,260 | 3.7% | 56.2% |  |
| RESUME_CHECK | 413,106,660 | 3.3% | 59.4% | 0.0% |
| BINARY_SUBSCR_STR_INT | 412,518,600 | 3.3% | 62.7% | 0.0% |
| NOP | 408,321,460 | 3.2% | 65.9% |  |
| RETURN_VALUE | 407,422,680 | 3.2% | 69.1% |  |
| CALL_PY_EXACT_ARGS | 361,485,840 | 2.8% | 72.0% |  |
| LOAD_GLOBAL_BUILTIN | 338,493,760 | 2.7% | 74.6% |  |
| TO_BOOL_BOOL | 280,308,020 | 2.2% | 76.8% |  |
| COMPARE_OP_STR | 227,223,940 | 1.8% | 78.6% |  |
| BINARY_OP_ADD_INT | 211,018,880 | 1.7% | 80.3% |  |
| BINARY_SUBSCR_DICT | 194,092,240 | 1.5% | 81.8% |  |
| BUILD_TUPLE | 191,588,800 | 1.5% | 83.3% |  |
| ENTER_EXECUTOR | 186,496,480 | 1.5% | 84.8% |  |
| CALL_ISINSTANCE | 127,886,200 | 1.0% | 85.8% |  |
| STORE_FAST_STORE_FAST | 114,407,140 | 0.9% | 86.7% |  |
| FOR_ITER_TUPLE | 114,076,420 | 0.9% | 87.6% |  |
| GET_ITER | 110,778,920 | 0.9% | 88.5% |  |
| BINARY_SLICE | 110,349,320 | 0.9% | 89.4% |  |
| LOAD_DEREF | 101,972,640 | 0.8% | 90.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 86,901,160 | 0.7% | 90.8% |  |
| POP_TOP | 86,750,300 | 0.7% | 91.5% |  |
| BINARY_SUBSCR | 85,817,040 | 0.7% | 92.2% |  |
| POP_JUMP_IF_TRUE | 77,894,920 | 0.6% | 92.8% |  |
| LOAD_ATTR | 66,873,440 | 0.5% | 93.3% |  |
| CALL | 65,357,620 | 0.5% | 93.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 61,984,980 | 0.5% | 94.3% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 60,446,620 | 0.5% | 94.8% |  |
| MAKE_CELL | 50,627,120 | 0.4% | 95.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 36,110,840 | 0.3% | 95.5% |  |
| RETURN_CONST | 33,126,420 | 0.3% | 95.8% |  |
| CALL_BUILTIN_CLASS | 32,092,080 | 0.3% | 96.0% |  |
| LOAD_ATTR_CLASS | 30,876,880 | 0.2% | 96.3% |  |
| STORE_SUBSCR_DICT | 29,324,620 | 0.2% | 96.5% |  |
| BINARY_OP | 29,034,680 | 0.2% | 96.7% |  |
| TO_BOOL | 28,693,160 | 0.2% | 97.0% |  |
| JUMP_FORWARD | 27,801,840 | 0.2% | 97.2% |  |
| COPY | 25,490,580 | 0.2% | 97.4% |  |
| CALL_LEN | 25,314,480 | 0.2% | 97.6% |  |
| FOR_ITER_RANGE | 25,313,640 | 0.2% | 97.8% |  |
| COPY_FREE_VARS | 25,313,600 | 0.2% | 98.0% |  |
| UNPACK_SEQUENCE_TUPLE | 25,313,540 | 0.2% | 98.2% |  |
| MAKE_FUNCTION | 25,313,520 | 0.2% | 98.4% |  |
| RETURN_GENERATOR | 25,313,520 | 0.2% | 98.6% |  |
| SET_FUNCTION_ATTRIBUTE | 25,313,520 | 0.2% | 98.8% |  |
| STORE_DEREF | 25,313,520 | 0.2% | 99.0% |  |
| END_FOR | 25,313,500 | 0.2% | 99.2% |  |
| FOR_ITER_GEN | 25,313,500 | 0.2% | 99.4% |  |
| CALL_KW | 22,365,600 | 0.2% | 99.5% |  |
| BINARY_OP_ADD_UNICODE | 20,173,340 | 0.2% | 99.7% |  |
| PUSH_NULL | 8,807,620 | 0.1% | 99.8% |  |
| TO_BOOL_NONE | 4,466,220 | 0.0% | 99.8% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 4,214,880 | 0.0% | 99.8% |  |
| BUILD_MAP | 4,185,520 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 2,528,260 | 0.0% | 99.9% |  |
| BUILD_CONST_KEY_MAP | 2,272,240 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 2,233,260 | 0.0% | 99.9% |  |
| TO_BOOL_ALWAYS_TRUE | 2,233,100 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 2,193,180 | 0.0% | 100.0% |  |
| FOR_ITER | 1,834,060 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,833,100 | 0.0% | 100.0% |  |
| BUILD_LIST | 480,180 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 364,360 | 0.0% | 100.0% |  |
| CALL_LIST_APPEND | 174,920 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,140 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 3,860 | 0.0% | 100.0% |  |
| SWAP | 1,120 | 0.0% | 100.0% |  |
| COMPARE_OP | 1,000 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 980 | 0.0% | 100.0% |  |
| RESUME | 720 | 0.0% | 100.0% | 200.0% |
| LOAD_ATTR_MODULE | 660 | 0.0% | 100.0% |  |
| INTERPRETER_EXIT | 520 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 480 | 0.0% | 100.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 420 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 200 | 0.0% | 100.0% |  |
| POP_EXCEPT | 200 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 200 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 200 | 0.0% | 100.0% |  |
| STORE_ATTR | 200 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 200 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 180 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 160 | 0.0% | 100.0% | 12.5% |
| EXIT_INIT_CHECK | 120 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 120 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 100 | 0.0% | 100.0% |  |
| CALL_STR_1 | 100 | 0.0% | 100.0% |  |
| BEFORE_WITH | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| IS_OP | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 60 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 60 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 60 | 0.0% | 100.0% |  |
| LIST_APPEND | 40 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 40 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 20 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 20 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 552,774,340 | 4.4% | 4.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 459,584,980 | 3.6% | 8.0% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 417,000,900 | 3.3% | 11.3% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_STR_INT | 410,680,320 | 3.2% | 14.5% |
| STORE_FAST LOAD_FAST | 381,757,060 | 3.0% | 17.5% |
| NOP LOAD_FAST_LOAD_FAST | 331,385,920 | 2.6% | 20.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 325,236,620 | 2.6% | 22.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 310,858,780 | 2.4% | 25.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 274,052,600 | 2.2% | 27.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 231,099,080 | 1.8% | 29.1% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 227,223,880 | 1.8% | 30.9% |
| LOAD_CONST COMPARE_OP_STR | 227,223,520 | 1.8% | 32.7% |
| LOAD_FAST RETURN_VALUE | 226,778,440 | 1.8% | 34.5% |
| RETURN_VALUE STORE_FAST | 225,240,500 | 1.8% | 36.3% |
| BINARY_SUBSCR_STR_INT STORE_FAST | 212,382,780 | 1.7% | 37.9% |
| LOAD_CONST BINARY_OP_ADD_INT | 211,016,560 | 1.7% | 39.6% |
| RESUME_CHECK NOP | 202,690,660 | 1.6% | 41.2% |
| LOAD_FAST CONTAINS_OP | 200,135,680 | 1.6% | 42.8% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 200,135,560 | 1.6% | 44.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 188,742,060 | 1.5% | 45.8% |
| BINARY_OP_ADD_INT STORE_FAST | 182,162,460 | 1.4% | 47.3% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 151,619,640 | 1.2% | 48.5% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 132,695,060 | 1.0% | 49.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 130,869,120 | 1.0% | 50.5% |
| RESUME_CHECK LOAD_FAST | 130,532,320 | 1.0% | 51.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 130,122,320 | 1.0% | 52.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 127,887,020 | 1.0% | 53.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 127,886,100 | 1.0% | 54.6% |
| LOAD_FAST_LOAD_FAST LOAD_GLOBAL_MODULE | 119,007,240 | 0.9% | 55.6% |
| LOAD_GLOBAL_MODULE CALL_PY_EXACT_ARGS | 119,007,240 | 0.9% | 56.5% |
| BUILD_TUPLE RETURN_VALUE | 110,461,920 | 0.9% | 57.4% |
| BINARY_SUBSCR_DICT STORE_FAST | 109,801,320 | 0.9% | 58.2% |
| LOAD_CONST BINARY_SUBSCR_DICT | 108,263,200 | 0.9% | 59.1% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 107,921,320 | 0.9% | 59.9% |
| POP_JUMP_IF_FALSE ENTER_EXECUTOR | 104,213,700 | 0.8% | 60.8% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 102,572,620 | 0.8% | 61.6% |
| STORE_FAST NOP | 101,908,500 | 0.8% | 62.4% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 99,506,560 | 0.8% | 63.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 90,270,280 | 0.7% | 63.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 86,901,160 | 0.7% | 64.5% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 86,900,880 | 0.7% | 65.2% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_DICT | 85,469,660 | 0.7% | 65.9% |
| LOAD_CONST BINARY_SUBSCR | 83,687,540 | 0.7% | 66.6% |
| STORE_FAST ENTER_EXECUTOR | 82,282,500 | 0.6% | 67.2% |
| LOAD_FAST BUILD_TUPLE | 79,966,020 | 0.6% | 67.8% |
| ENTER_EXECUTOR LOAD_FAST | 79,227,400 | 0.6% | 68.5% |
| LOAD_CONST LOAD_CONST | 79,146,460 | 0.6% | 69.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 78,724,460 | 0.6% | 69.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 77,773,780 | 0.6% | 70.3% |
| BINARY_SUBSCR_DICT CONTAINS_OP | 77,499,060 | 0.6% | 70.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 76,774,060 | 0.6% | 71.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 74,552,280 | 0.6% | 72.1% |
| LOAD_FAST TO_BOOL_BOOL | 73,330,680 | 0.6% | 72.7% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 61,984,720 | 0.5% | 73.2% |
| LOAD_FAST LOAD_ATTR | 60,153,280 | 0.5% | 73.7% |
| LOAD_ATTR LOAD_ATTR_METHOD_WITH_VALUES | 60,151,540 | 0.5% | 74.1% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 60,041,400 | 0.5% | 74.6% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 58,318,560 | 0.5% | 75.1% |
| GET_ITER FOR_ITER_TUPLE | 58,318,480 | 0.5% | 75.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 58,254,420 | 0.5% | 76.0% |
| LOAD_GLOBAL_MODULE CONTAINS_OP | 57,646,360 | 0.5% | 76.4% |
| LOAD_CONST BINARY_SLICE | 56,780,780 | 0.4% | 76.9% |
| FOR_ITER_TUPLE LOAD_FAST | 55,966,340 | 0.4% | 77.3% |
| FOR_ITER_TUPLE STORE_FAST | 55,917,860 | 0.4% | 77.8% |
| BINARY_SUBSCR STORE_FAST | 55,886,720 | 0.4% | 78.2% |
| ENTER_EXECUTOR FOR_ITER_TUPLE | 55,756,580 | 0.4% | 78.7% |
| LOAD_FAST GET_ITER | 54,652,480 | 0.4% | 79.1% |
| LOAD_FAST STORE_FAST | 53,141,540 | 0.4% | 79.5% |
| POP_JUMP_IF_TRUE LOAD_FAST | 52,404,280 | 0.4% | 79.9% |
| LOAD_FAST CALL | 51,767,700 | 0.4% | 80.3% |
| LOAD_FAST_LOAD_FAST BINARY_SLICE | 51,459,340 | 0.4% | 80.7% |
| LOAD_DEREF LOAD_CONST | 50,627,040 | 0.4% | 81.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 49,208,940 | 0.4% | 81.5% |
| NOP NOP | 47,320,240 | 0.4% | 81.9% |
| ENTER_EXECUTOR LOAD_GLOBAL_BUILTIN | 45,109,240 | 0.4% | 82.2% |
| RETURN_VALUE RETURN_VALUE | 40,706,800 | 0.3% | 82.6% |
| LOAD_GLOBAL_MODULE STORE_FAST | 40,346,520 | 0.3% | 82.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 32,084,180 | 0.3% | 83.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 31,172,800 | 0.2% | 83.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_CLASS | 30,876,600 | 0.2% | 83.6% |
| STORE_FAST_STORE_FAST LOAD_FAST_LOAD_FAST | 30,774,160 | 0.2% | 83.9% |
| BINARY_SLICE BUILD_TUPLE | 30,499,780 | 0.2% | 84.1% |
| NOP LOAD_FAST | 29,614,020 | 0.2% | 84.3% |
| POP_TOP LOAD_FAST | 29,274,900 | 0.2% | 84.6% |
| CALL RESUME_CHECK | 29,254,520 | 0.2% | 84.8% |
| POP_JUMP_IF_FALSE NOP | 29,253,920 | 0.2% | 85.0% |
| BINARY_SLICE GET_ITER | 28,979,760 | 0.2% | 85.3% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 28,746,840 | 0.2% | 85.5% |
| LOAD_FAST TO_BOOL | 28,685,080 | 0.2% | 85.7% |
| TO_BOOL POP_JUMP_IF_TRUE | 28,684,860 | 0.2% | 85.9% |
| LOAD_ATTR_CLASS CALL_PY_EXACT_ARGS | 28,684,480 | 0.2% | 86.2% |
| BINARY_OP STORE_FAST | 28,667,020 | 0.2% | 86.4% |
| BINARY_SUBSCR STORE_FAST_STORE_FAST | 27,505,760 | 0.2% | 86.6% |
| JUMP_FORWARD LOAD_GLOBAL_MODULE | 27,441,680 | 0.2% | 86.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 27,242,600 | 0.2% | 87.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 27,148,260 | 0.2% | 87.3% |
| BUILD_TUPLE STORE_FAST | 27,146,640 | 0.2% | 87.5% |
| STORE_FAST JUMP_FORWARD | 27,146,640 | 0.2% | 87.7% |
| POP_TOP LOAD_FAST_LOAD_FAST | 25,846,800 | 0.2% | 87.9% |
| COPY TO_BOOL_BOOL | 25,489,480 | 0.2% | 88.1% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 56,780,780 | 51.5% |
| LOAD_FAST_LOAD_FAST | 51,459,340 | 46.6% |
| BINARY_OP_ADD_INT | 2,109,140 | 1.9% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 30,499,780 | 27.6% |
| GET_ITER | 28,979,760 | 26.3% |
| LOAD_DEREF | 25,313,520 | 22.9% |
| BINARY_OP_ADD_UNICODE | 20,173,240 | 18.3% |
| LOAD_FAST | 2,192,360 | 2.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 400 | 76.9% |
| RESUME | 100 | 19.2% |
| POP_TOP | 20 | 3.8% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,107,400 | 50.0% |
| ENTER_EXECUTOR | 1,321,140 | 31.3% |
| BINARY_SLICE | 786,260 | 18.7% |
| BINARY_OP | 40 | 0.0% |
| BINARY_OP_ADD_UNICODE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,214,840 | 100.0% |
| ENTER_EXECUTOR | 40 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 83,687,540 | 97.5% |
| LOAD_FAST | 2,106,480 | 2.5% |
| BINARY_SUBSCR | 22,280 | 0.0% |
| LOAD_FAST_LOAD_FAST | 680 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 55,886,720 | 65.1% |
| STORE_FAST_STORE_FAST | 27,505,760 | 32.1% |
| BUILD_TUPLE | 2,106,480 | 2.5% |
| LOAD_CONST | 295,160 | 0.3% |
| BINARY_SUBSCR | 22,280 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 140 | 70.0% |
| LOAD_GLOBAL | 60 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 200 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 25,313,500 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 25,313,500 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 120 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,652,480 | 49.3% |
| BINARY_SLICE | 28,979,760 | 26.2% |
| CALL_BUILTIN_CLASS | 25,313,520 | 22.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,833,100 | 1.7% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 58,318,480 | 52.6% |
| CALL_PY_EXACT_ARGS | 25,313,480 | 22.9% |
| FOR_ITER_GEN | 25,313,480 | 22.9% |
| FOR_ITER | 1,833,360 | 1.7% |
| FOR_ITER_RANGE | 60 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 380 | 73.1% |
| RETURN_CONST | 140 | 26.9% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 25,313,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 25,313,520 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 202,690,660 | 49.6% |
| STORE_FAST | 101,908,500 | 25.0% |
| NOP | 47,320,240 | 11.6% |
| POP_JUMP_IF_FALSE | 29,253,920 | 7.2% |
| STORE_FAST_STORE_FAST | 25,313,520 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 331,385,920 | 81.2% |
| NOP | 47,320,240 | 11.6% |
| LOAD_FAST | 29,614,020 | 7.3% |
| LOAD_GLOBAL_MODULE | 1,140 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 160 | 80.0% |
| SWAP | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 80.0% |
| RETURN_VALUE | 40 | 20.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 25,487,680 | 29.4% |
| END_FOR | 25,313,500 | 29.2% |
| FOR_ITER_GEN | 25,313,500 | 29.2% |
| RETURN_CONST | 4,615,680 | 5.3% |
| CALL_METHOD_DESCRIPTOR_O | 2,192,220 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,274,900 | 33.7% |
| LOAD_FAST_LOAD_FAST | 25,846,800 | 29.8% |
| RESUME_CHECK | 25,313,500 | 29.2% |
| RETURN_CONST | 4,480,500 | 5.2% |
| NOP | 1,833,200 | 2.1% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 160 | 80.0% |
| LOAD_ATTR | 20 | 10.0% |
| LOAD_ATTR_SLOT | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 120 | 60.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 40.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 6,699,520 | 76.1% |
| LOAD_FAST | 2,107,440 | 23.9% |
| LOAD_ATTR_MODULE | 500 | 0.0% |
| LOAD_DEREF | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 8,806,880 | 100.0% |
| LOAD_FAST | 460 | 0.0% |
| CALL | 240 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 25,313,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,313,520 | 100.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 226,778,440 | 55.7% |
| BUILD_TUPLE | 110,461,920 | 27.1% |
| RETURN_VALUE | 40,706,800 | 10.0% |
| CONTAINS_OP | 25,487,680 | 6.3% |
| CALL_BUILTIN_CLASS | 2,233,100 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 225,240,500 | 55.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 86,900,880 | 21.3% |
| RETURN_VALUE | 40,706,800 | 10.0% |
| TO_BOOL_BOOL | 25,488,560 | 6.3% |
| UNPACK_SEQUENCE_TUPLE | 25,313,480 | 6.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 160 | 80.0% |
| LOAD_FAST | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 100 | 50.0% |
| LOAD_FAST_LOAD_FAST | 60 | 30.0% |
| LOAD_FAST | 20 | 10.0% |
| RETURN_CONST | 20 | 10.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,685,080 | 100.0% |
| TO_BOOL | 7,200 | 0.0% |
| CALL | 420 | 0.0% |
| COPY | 140 | 0.0% |
| RETURN_CONST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 28,684,860 | 100.0% |
| TO_BOOL | 7,200 | 0.0% |
| TO_BOOL_BOOL | 520 | 0.0% |
| POP_JUMP_IF_FALSE | 400 | 0.0% |
| TO_BOOL_STR | 100 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,313,640 | 87.2% |
| BUILD_TUPLE | 3,353,120 | 11.5% |
| LOAD_DEREF | 359,120 | 1.2% |
| BINARY_OP | 7,680 | 0.0% |
| LOAD_CONST | 880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 28,667,020 | 98.7% |
| LOAD_GLOBAL_MODULE | 359,080 | 1.2% |
| BINARY_OP | 7,680 | 0.0% |
| BINARY_OP_ADD_INT | 480 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,272,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,272,240 | 100.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 359,120 | 74.8% |
| BUILD_MAP | 120,960 | 25.2% |
| LOAD_FAST | 80 | 0.0% |
| SWAP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 359,120 | 74.8% |
| LOAD_FAST_LOAD_FAST | 120,960 | 25.2% |
| LOAD_DEREF | 80 | 0.0% |
| SWAP | 20 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 2,272,200 | 54.3% |
| ENTER_EXECUTOR | 1,618,000 | 38.7% |
| LOAD_ATTR_METHOD_NO_DICT | 174,140 | 4.2% |
| POP_JUMP_IF_FALSE | 120,960 | 2.9% |
| RESUME_CHECK | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,272,240 | 54.3% |
| LOAD_FAST_LOAD_FAST | 1,618,000 | 38.7% |
| CALL_LIST_APPEND | 174,120 | 4.2% |
| BUILD_LIST | 120,960 | 2.9% |
| LOAD_FAST | 160 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,966,020 | 41.7% |
| BINARY_SLICE | 30,499,780 | 15.9% |
| LOAD_FAST_LOAD_FAST | 28,746,840 | 15.0% |
| LOAD_GLOBAL_BUILTIN | 25,313,500 | 13.2% |
| BINARY_OP_ADD_UNICODE | 20,173,260 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 110,461,920 | 57.7% |
| STORE_FAST | 27,146,640 | 14.2% |
| LOAD_CONST | 25,313,520 | 13.2% |
| CALL_ISINSTANCE | 25,313,480 | 13.2% |
| BINARY_OP | 3,353,120 | 1.8% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,767,700 | 79.2% |
| LOAD_FAST_LOAD_FAST | 8,807,360 | 13.5% |
| LOAD_CONST | 2,233,440 | 3.4% |
| LOAD_ATTR_METHOD_NO_DICT | 2,233,140 | 3.4% |
| BINARY_SLICE | 295,120 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 29,254,520 | 44.8% |
| TO_BOOL_BOOL | 24,914,920 | 38.1% |
| STORE_FAST | 6,699,620 | 10.3% |
| LOAD_CONST | 2,233,120 | 3.4% |
| TO_BOOL_STR | 2,233,080 | 3.4% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100 | 55.6% |
| CALL_INTRINSIC_1 | 80 | 44.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 44.4% |
| RESUME_CHECK | 80 | 44.4% |
| RESUME | 20 | 11.1% |


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
| LOAD_CONST | 22,365,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 22,365,540 | 100.0% |
| RESUME | 60 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 840 | 84.0% |
| LOAD_FAST | 80 | 8.0% |
| COPY | 40 | 4.0% |
| LOAD_FAST_LOAD_FAST | 40 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 420 | 42.0% |
| POP_JUMP_IF_FALSE | 400 | 40.0% |
| COMPARE_OP_INT | 120 | 12.0% |
| COPY | 20 | 2.0% |
| JUMP_FORWARD | 20 | 2.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200,135,680 | 42.8% |
| LOAD_FAST_LOAD_FAST | 132,695,060 | 28.4% |
| BINARY_SUBSCR_DICT | 77,499,060 | 16.6% |
| LOAD_GLOBAL_MODULE | 57,646,360 | 12.3% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 417,000,900 | 89.1% |
| RETURN_VALUE | 25,487,680 | 5.4% |
| COPY | 25,487,680 | 5.4% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 25,487,680 | 100.0% |
| JUMP_FORWARD | 960 | 0.0% |
| SWAP | 960 | 0.0% |
| COMPARE_OP_INT | 940 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 25,489,480 | 100.0% |
| COMPARE_OP_INT | 920 | 0.0% |
| TO_BOOL | 140 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 25,313,500 | 100.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 25,313,520 | 100.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 104,213,700 | 55.9% |
| STORE_FAST | 82,282,500 | 44.1% |
| JUMP_BACKWARD | 240 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,227,400 | 42.5% |
| FOR_ITER_TUPLE | 55,756,580 | 29.9% |
| LOAD_GLOBAL_BUILTIN | 45,109,240 | 24.2% |
| RETURN_VALUE | 1,752,920 | 0.9% |
| BUILD_MAP | 1,618,000 | 0.9% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,833,360 | 100.0% |
| FOR_ITER | 640 | 0.0% |
| LOAD_FAST | 40 | 0.0% |
| JUMP_BACKWARD | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,833,200 | 100.0% |
| FOR_ITER | 640 | 0.0% |
| FOR_ITER_TUPLE | 80 | 0.0% |
| STORE_FAST | 40 | 0.0% |
| FOR_ITER_RANGE | 40 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 60 | 75.0% |
| LOAD_GLOBAL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 80 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,720 | 70.5% |
| POP_JUMP_IF_FALSE | 1,020 | 26.4% |
| POP_TOP | 80 | 2.1% |
| LIST_APPEND | 40 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 1,280 | 33.2% |
| FOR_ITER_TUPLE | 1,280 | 33.2% |
| LOAD_FAST | 640 | 16.6% |
| LOAD_GLOBAL_MODULE | 300 | 7.8% |
| ENTER_EXECUTOR | 240 | 6.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 27,146,640 | 97.6% |
| LOAD_CONST | 359,120 | 1.3% |
| STORE_FAST_STORE_FAST | 295,120 | 1.1% |
| COMPARE_OP_INT | 940 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 27,441,680 | 98.7% |
| BINARY_SUBSCR_DICT | 359,100 | 1.3% |
| COPY | 960 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 40 | 100.0% |


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
| LOAD_FAST | 60,153,280 | 90.0% |
| LOAD_GLOBAL_MODULE | 6,699,740 | 10.0% |
| LOAD_ATTR | 19,840 | 0.0% |
| LOAD_GLOBAL | 400 | 0.0% |
| LOAD_ATTR_CLASS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 60,151,540 | 89.9% |
| PUSH_NULL | 6,699,520 | 10.0% |
| LOAD_ATTR | 19,840 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 420 | 0.0% |
| LOAD_FAST | 380 | 0.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 552,774,340 | 61.8% |
| LOAD_FAST_LOAD_FAST | 99,506,560 | 11.1% |
| LOAD_CONST | 79,146,460 | 8.9% |
| LOAD_DEREF | 50,627,040 | 5.7% |
| LOAD_ATTR_METHOD_NO_DICT | 27,148,260 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 227,223,520 | 25.4% |
| BINARY_OP_ADD_INT | 211,016,560 | 23.6% |
| BINARY_SUBSCR_DICT | 108,263,200 | 12.1% |
| BINARY_SUBSCR | 83,687,540 | 9.4% |
| LOAD_CONST | 79,146,460 | 8.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 25,313,520 | 24.8% |
| STORE_FAST | 25,313,520 | 24.8% |
| STORE_FAST_STORE_FAST | 25,313,520 | 24.8% |
| LOAD_GLOBAL_BUILTIN | 25,313,500 | 24.8% |
| LOAD_DEREF | 359,120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 50,627,040 | 49.6% |
| LOAD_FAST | 25,313,520 | 24.8% |
| CALL_LEN | 25,313,480 | 24.8% |
| BINARY_OP | 359,120 | 0.4% |
| LOAD_DEREF | 359,120 | 0.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 459,584,980 | 24.4% |
| STORE_FAST | 381,757,060 | 20.2% |
| BINARY_SUBSCR_STR_INT | 200,135,560 | 10.6% |
| LOAD_FAST_LOAD_FAST | 130,869,120 | 6.9% |
| RESUME_CHECK | 130,532,320 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 552,774,340 | 29.3% |
| RETURN_VALUE | 226,778,440 | 12.0% |
| CONTAINS_OP | 200,135,680 | 10.6% |
| LOAD_GLOBAL_BUILTIN | 127,887,020 | 6.8% |
| LOAD_GLOBAL_MODULE | 90,270,280 | 4.8% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 20 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| NOP | 331,385,920 | 26.3% |
| LOAD_GLOBAL_MODULE | 325,236,620 | 25.8% |
| STORE_FAST | 274,052,600 | 21.8% |
| POP_JUMP_IF_FALSE | 151,619,640 | 12.0% |
| LOAD_FAST_LOAD_FAST | 76,774,060 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 410,680,320 | 32.6% |
| CONTAINS_OP | 132,695,060 | 10.5% |
| LOAD_FAST | 130,869,120 | 10.4% |
| LOAD_GLOBAL_MODULE | 119,007,240 | 9.5% |
| CALL_PY_EXACT_ARGS | 107,921,320 | 8.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,240 | 30.0% |
| POP_JUMP_IF_FALSE | 660 | 15.9% |
| LOAD_FAST | 580 | 14.0% |
| LOAD_FAST_LOAD_FAST | 440 | 10.6% |
| RESUME_CHECK | 160 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,500 | 36.2% |
| LOAD_FAST_LOAD_FAST | 660 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 620 | 15.0% |
| CALL | 420 | 10.1% |
| LOAD_ATTR | 400 | 9.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 25,313,560 | 50.0% |
| MAKE_CELL | 25,313,520 | 50.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 25,313,560 | 50.0% |
| MAKE_CELL | 25,313,520 | 50.0% |
| RESUME | 40 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 417,000,900 | 47.1% |
| TO_BOOL_BOOL | 231,099,080 | 26.1% |
| COMPARE_OP_STR | 227,223,880 | 25.7% |
| TO_BOOL_NONE | 4,466,220 | 0.5% |
| TO_BOOL_STR | 2,233,160 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 459,584,980 | 52.0% |
| LOAD_FAST_LOAD_FAST | 151,619,640 | 17.1% |
| ENTER_EXECUTOR | 104,213,700 | 11.8% |
| LOAD_GLOBAL_MODULE | 74,552,280 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 60,041,400 | 6.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 49,208,940 | 63.2% |
| TO_BOOL | 28,684,860 | 36.8% |
| COMPARE_OP_INT | 940 | 0.0% |
| TO_BOOL_STR | 100 | 0.0% |
| COMPARE_OP_STR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 52,404,280 | 67.3% |
| POP_TOP | 25,487,680 | 32.7% |
| LOAD_FAST_LOAD_FAST | 980 | 0.0% |
| RETURN_VALUE | 960 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 25,313,500 | 76.4% |
| POP_TOP | 4,480,500 | 13.5% |
| POP_JUMP_IF_FALSE | 3,036,980 | 9.2% |
| CALL_LIST_APPEND | 174,140 | 0.5% |
| STORE_SUBSCR_DICT | 120,940 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_FOR | 25,313,500 | 76.4% |
| POP_TOP | 4,615,680 | 13.9% |
| TO_BOOL_BOOL | 3,196,840 | 9.7% |
| INTERPRETER_EXIT | 140 | 0.0% |
| EXIT_INIT_CHECK | 120 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 25,313,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 25,313,480 | 100.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 60 | 30.0% |
| STORE_ATTR_SLOT | 60 | 30.0% |
| RETURN_CONST | 40 | 20.0% |
| LOAD_FAST | 20 | 10.0% |
| LOAD_GLOBAL | 20 | 10.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,313,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,313,520 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 225,240,500 | 19.5% |
| BINARY_SUBSCR_STR_INT | 212,382,780 | 18.4% |
| BINARY_OP_ADD_INT | 182,162,460 | 15.8% |
| BINARY_SUBSCR_DICT | 109,801,320 | 9.5% |
| LOAD_ATTR_INSTANCE_VALUE | 58,318,560 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 381,757,060 | 33.1% |
| LOAD_FAST_LOAD_FAST | 274,052,600 | 23.7% |
| LOAD_GLOBAL_MODULE | 188,742,060 | 16.4% |
| NOP | 101,908,500 | 8.8% |
| ENTER_EXECUTOR | 82,282,500 | 7.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 40 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 86,901,160 | 76.0% |
| BINARY_SUBSCR | 27,505,760 | 24.0% |
| UNPACK_SEQUENCE | 200 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,172,800 | 27.2% |
| LOAD_FAST_LOAD_FAST | 30,774,160 | 26.9% |
| NOP | 25,313,520 | 22.1% |
| LOAD_DEREF | 25,313,520 | 22.1% |
| LOAD_GLOBAL_MODULE | 1,538,000 | 1.3% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 960 | 85.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 60 | 5.4% |
| BUILD_LIST | 20 | 1.8% |
| CALL | 20 | 1.8% |
| LOAD_ATTR | 20 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 960 | 85.7% |
| LOAD_CONST | 80 | 7.1% |
| POP_EXCEPT | 40 | 3.6% |
| BUILD_LIST | 20 | 1.8% |
| FOR_ITER_LIST | 20 | 1.8% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 200 | 41.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 41.7% |
| UNPACK_SEQUENCE_TUPLE | 60 | 12.5% |
| STORE_FAST | 20 | 4.2% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 460 | 63.9% |
| CACHE | 100 | 13.9% |
| CALL_KW | 60 | 8.3% |
| MAKE_CELL | 40 | 5.6% |
| POP_TOP | 20 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 41.7% |
| LOAD_GLOBAL | 140 | 19.4% |
| NOP | 120 | 16.7% |
| BUILD_MAP | 40 | 5.6% |
| LOAD_CONST | 40 | 5.6% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 211,016,560 | 100.0% |
| LOAD_FAST_LOAD_FAST | 1,840 | 0.0% |
| BINARY_OP | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 182,162,460 | 86.3% |
| LOAD_FAST_LOAD_FAST | 20,173,260 | 9.6% |
| LOAD_CONST | 2,548,760 | 1.2% |
| LOAD_FAST | 2,192,160 | 1.0% |
| BINARY_SLICE | 2,109,140 | 1.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 20,173,240 | 100.0% |
| BINARY_OP | 60 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 20,173,260 | 100.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 40 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


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

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 108,263,200 | 55.8% |
| LOAD_FAST_LOAD_FAST | 85,469,660 | 44.0% |
| JUMP_FORWARD | 359,100 | 0.2% |
| BINARY_SUBSCR | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 109,801,320 | 56.6% |
| CONTAINS_OP | 77,499,060 | 39.9% |
| LOAD_CONST | 2,407,420 | 1.2% |
| LOAD_FAST | 2,192,220 | 1.1% |
| LOAD_ATTR_METHOD_NO_DICT | 2,192,200 | 1.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 410,680,320 | 99.6% |
| BINARY_OP_ADD_INT | 1,833,080 | 0.4% |
| ENTER_EXECUTOR | 4,880 | 0.0% |
| BINARY_SUBSCR | 220 | 0.0% |
| BINARY_SUBSCR_STR_INT | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 212,382,780 | 51.5% |
| LOAD_FAST | 200,135,560 | 48.5% |
| PUSH_EXC_INFO | 160 | 0.0% |
| BINARY_SUBSCR_STR_INT | 100 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 66.7% |
| CALL | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 120 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 25,313,480 | 78.9% |
| LOAD_GLOBAL_BUILTIN | 4,544,360 | 14.2% |
| LOAD_CONST | 2,234,000 | 7.0% |
| CALL | 180 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 25,313,520 | 78.9% |
| BUILD_MAP | 2,272,200 | 7.1% |
| LOAD_GLOBAL_BUILTIN | 2,272,160 | 7.1% |
| RETURN_VALUE | 2,233,100 | 7.0% |
| STORE_FAST | 1,000 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 80.0% |
| CALL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 60.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 40.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 40.0% |
| LOAD_FAST_LOAD_FAST | 40 | 40.0% |
| LOAD_FAST | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 60.0% |
| STORE_FAST | 40 | 40.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 920 | 93.9% |
| CALL_STR_1 | 40 | 4.1% |
| CALL | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 940 | 95.9% |
| LIST_APPEND | 40 | 4.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 102,572,620 | 80.2% |
| BUILD_TUPLE | 25,313,480 | 19.8% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 127,886,100 | 100.0% |
| TO_BOOL | 100 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 25,313,480 | 100.0% |
| LOAD_FAST | 920 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 25,313,480 | 100.0% |
| LOAD_FAST | 940 | 0.0% |
| LOAD_CONST | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 174,120 | 99.5% |
| LOAD_FAST | 760 | 0.4% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 174,140 | 99.6% |
| LOAD_GLOBAL_MODULE | 760 | 0.4% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,233,080 | 88.3% |
| LOAD_CONST | 295,080 | 11.7% |
| CALL | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,233,080 | 88.3% |
| POP_TOP | 295,100 | 11.7% |
| SWAP | 60 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 50.0% |
| LOAD_CONST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 75.0% |
| GET_ITER | 20 | 25.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,833,080 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,833,100 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,193,120 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,192,220 | 100.0% |
| TO_BOOL_BOOL | 920 | 0.0% |
| TO_BOOL | 20 | 0.0% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 119,007,240 | 32.9% |
| LOAD_FAST_LOAD_FAST | 107,921,320 | 29.9% |
| LOAD_FAST | 78,724,460 | 21.8% |
| LOAD_ATTR_CLASS | 28,684,480 | 7.9% |
| GET_ITER | 25,313,480 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 310,858,780 | 86.0% |
| MAKE_CELL | 25,313,560 | 7.0% |
| COPY_FREE_VARS | 25,313,500 | 7.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 80.0% |
| CALL | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 60.0% |
| CALL_BUILTIN_O | 40 | 40.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 361,480 | 99.2% |
| COPY | 920 | 0.3% |
| LOAD_CONST | 920 | 0.3% |
| LOAD_FAST | 920 | 0.3% |
| COMPARE_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 361,540 | 99.2% |
| COPY | 940 | 0.3% |
| JUMP_FORWARD | 940 | 0.3% |
| POP_JUMP_IF_TRUE | 940 | 0.3% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 227,223,520 | 100.0% |
| COMPARE_OP | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 227,223,880 | 100.0% |
| POP_JUMP_IF_TRUE | 60 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 25,313,480 | 100.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 25,313,500 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 20 | 33.3% |
| JUMP_BACKWARD | 20 | 33.3% |
| SWAP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 40 | 66.7% |
| STORE_FAST | 20 | 33.3% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,313,480 | 100.0% |
| GET_ITER | 60 | 0.0% |
| JUMP_BACKWARD | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 25,313,500 | 100.0% |
| STORE_FAST | 60 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 58,318,480 | 51.1% |
| ENTER_EXECUTOR | 55,756,580 | 48.9% |
| JUMP_BACKWARD | 1,280 | 0.0% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,966,340 | 49.1% |
| STORE_FAST | 55,917,860 | 49.0% |
| LOAD_FAST_LOAD_FAST | 2,192,220 | 1.9% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 30,876,600 | 100.0% |
| LOAD_ATTR | 240 | 0.0% |
| LOAD_ATTR_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 28,684,480 | 92.9% |
| LOAD_CONST | 2,192,180 | 7.1% |
| CALL | 80 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 60 | 0.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,984,720 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 58,318,560 | 94.1% |
| GET_ITER | 1,833,100 | 3.0% |
| LOAD_ATTR_METHOD_NO_DICT | 1,833,080 | 3.0% |
| LOAD_FAST | 160 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,084,180 | 88.8% |
| BINARY_SUBSCR_DICT | 2,192,200 | 6.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,833,080 | 5.1% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |
| LOAD_ATTR | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 27,148,260 | 75.2% |
| LOAD_FAST | 2,489,140 | 6.9% |
| CALL | 2,233,140 | 6.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,233,080 | 6.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,833,080 | 5.1% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 60,151,540 | 99.5% |
| LOAD_FAST | 295,080 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,254,420 | 96.4% |
| CALL_PY_EXACT_ARGS | 1,833,080 | 3.0% |
| LOAD_DEREF | 359,100 | 0.6% |
| CALL | 20 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 400 | 60.6% |
| LOAD_ATTR | 260 | 39.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 500 | 75.8% |
| LOAD_ATTR | 40 | 6.1% |
| LOAD_FAST | 40 | 6.1% |
| STORE_FAST | 40 | 6.1% |
| LOAD_ATTR_CLASS | 40 | 6.1% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 120 | 75.0% |
| LOAD_FAST | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 100 | 62.5% |
| PUSH_EXC_INFO | 20 | 12.5% |
| STORE_FAST | 20 | 12.5% |
| SWAP | 20 | 12.5% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 127,887,020 | 37.8% |
| POP_JUMP_IF_FALSE | 60,041,400 | 17.7% |
| ENTER_EXECUTOR | 45,109,240 | 13.3% |
| STORE_FAST | 27,242,600 | 8.0% |
| LOAD_CONST | 25,313,480 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,122,320 | 38.4% |
| CALL_ISINSTANCE | 102,572,620 | 30.3% |
| BUILD_TUPLE | 25,313,500 | 7.5% |
| LOAD_CONST | 25,313,500 | 7.5% |
| LOAD_DEREF | 25,313,500 | 7.5% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 188,742,060 | 32.4% |
| LOAD_FAST_LOAD_FAST | 119,007,240 | 20.5% |
| LOAD_FAST | 90,270,280 | 15.5% |
| RESUME_CHECK | 77,773,780 | 13.4% |
| POP_JUMP_IF_FALSE | 74,552,280 | 12.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 325,236,620 | 55.9% |
| CALL_PY_EXACT_ARGS | 119,007,240 | 20.5% |
| CONTAINS_OP | 57,646,360 | 9.9% |
| STORE_FAST | 40,346,520 | 6.9% |
| LOAD_ATTR_CLASS | 30,876,600 | 5.3% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 310,858,780 | 75.2% |
| CALL | 29,254,520 | 7.1% |
| MAKE_CELL | 25,313,560 | 6.1% |
| POP_TOP | 25,313,500 | 6.1% |
| CALL_KW | 22,365,540 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 202,690,660 | 49.1% |
| LOAD_FAST | 130,532,320 | 31.6% |
| LOAD_GLOBAL_MODULE | 77,773,780 | 18.8% |
| LOAD_FAST_LOAD_FAST | 2,108,440 | 0.5% |
| LOAD_CONST | 1,000 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 66.7% |
| LOAD_FAST_LOAD_FAST | 80 | 19.0% |
| STORE_ATTR | 60 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 280 | 66.7% |
| LOAD_FAST | 80 | 19.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 9.5% |
| LOAD_GLOBAL | 20 | 4.8% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,313,480 | 86.3% |
| LOAD_FAST_LOAD_FAST | 4,011,040 | 13.7% |
| STORE_SUBSCR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,313,500 | 86.3% |
| LOAD_FAST_LOAD_FAST | 3,890,180 | 13.3% |
| RETURN_CONST | 120,940 | 0.4% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,233,080 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,233,100 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 127,886,100 | 45.6% |
| LOAD_FAST | 73,330,680 | 26.2% |
| COPY | 25,489,480 | 9.1% |
| RETURN_VALUE | 25,488,560 | 9.1% |
| CALL | 24,914,920 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 231,099,080 | 82.4% |
| POP_JUMP_IF_TRUE | 49,208,940 | 17.6% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,466,160 | 100.0% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,466,220 | 100.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,233,080 | 100.0% |
| TO_BOOL | 100 | 0.0% |
| LOAD_FAST | 40 | 0.0% |
| STORE_FAST_LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,233,160 | 100.0% |
| POP_JUMP_IF_TRUE | 100 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 25,313,480 | 100.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,313,500 | 100.0% |
| LOAD_FAST | 20 | 0.0% |
| STORE_FAST_STORE_FAST | 20 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 86,900,880 | 100.0% |
| UNPACK_SEQUENCE | 200 | 0.0% |
| CALL_BUILTIN_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 86,901,160 | 100.0% |


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
|     deferred | 29,026,400 | 2.1% |
|          hit | 1,350,512,920 | 97.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 600 | 7.2% |
| Failure | 7,680 | 92.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 7,680 | 100.0% |


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
|     deferred | 85,799,860 | 4.3% |
|          hit | 1,902,181,900 | 95.7% |
|         miss | 5,700 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 600 | 2.6% |
| Failure | 22,280 | 97.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 21,580 | 96.9% |
| other | 700 | 3.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 65,336,940 | 9.4% |
|          hit | 630,213,180 | 90.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,640 | 7.9% |
| Failure | 19,040 | 92.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 8,780 | 46.1% |
| code complex parameters | 7,920 | 41.6% |
| cmethod | 2,220 | 11.7% |
| cfunc noargs | 60 | 0.3% |
| cfunc varargs | 20 | 0.1% |
| cfunc varargs keywords | 20 | 0.1% |
| class mutable | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 460 | 0.0% |
|          hit | 2,009,640,820 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 540 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,833,280 | 1.1% |
|          hit | 164,703,620 | 98.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 17.9% |
| Failure | 640 | 82.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 640 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 66,852,740 | 26.1% |
|          hit | 189,420,440 | 73.9% |
|         miss | 20 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,460 | 7.0% |
| Failure | 19,260 | 93.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 17,000 | 88.3% |
| method | 2,220 | 11.5% |
| class method obj | 20 | 0.1% |
| class attr simple | 20 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,020 | 0.0% |
|          hit | 920,416,080 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,120 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 11.8% |
|          hit | 480 | 70.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 100 | 0.0% |
|          hit | 29,324,620 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 28,685,260 | 6.9% |
|          hit | 385,647,440 | 93.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 700 | 8.9% |
| Failure | 7,200 | 91.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 7,200 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 220 | 0.0% |
|          hit | 112,214,700 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 7,596,620,940 | 59.9% |
| Not specialized | 1,350,479,220 | 10.6% |
| Specialized hits | 3,741,535,780 | 29.5% |
| Specialized misses | 7,160 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 85,799,860 | 30.9% |
| LOAD_ATTR | 66,852,740 | 24.1% |
| CALL | 65,336,940 | 23.5% |
| BINARY_OP | 29,026,400 | 10.5% |
| TO_BOOL | 28,685,260 | 10.3% |
| FOR_ITER | 1,833,280 | 0.7% |
| LOAD_GLOBAL | 2,020 | 0.0% |
| COMPARE_OP | 460 | 0.0% |
| UNPACK_SEQUENCE | 220 | 0.0% |
| STORE_SUBSCR | 100 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 5,700 | 66.3% |
| RESUME | 1,440 | 16.7% |
| RESUME_CHECK | 1,440 | 16.7% |
| LOAD_ATTR_SLOT | 20 | 0.2% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |
| BINARY_OP_INPLACE_ADD_UNICODE | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |
| END_FOR | 0 | 0.0% |
| EXIT_INIT_CHECK | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 520 | 0.0% |
| Calls to Python functions inlined | 465,861,980 | 100.0% |
| Calls via PyEval_EvalFrame (total) | 520 | 0.0% |
| Calls via PyEval_EvalFrame (vector) | 500 | 0.0% |
| Calls via PyEval_EvalFrame (generator) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 500 | 0.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 180 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 140 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 200 | 0.0% |
| Frames pushed | 440,549,100 | 94.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 261,546,880 | 13.8% |
| Frees to freelist | 261,549,160 |  |
| Allocations | 1,629,723,860 | 86.2% |
| Allocations to 512 bytes | 1,629,311,720 | 86.1% |
| Allocations to 4 kbytes | 410,940 | 0.0% |
| Allocations over 4 kbytes | 1,200 | 0.0% |
| Frees | 1,636,427,278 |  |
| New values | 120 |  |
| Interpreter increfs | 5,875,714,940 | 47.5% |
| Interpreter decrefs | 6,785,902,740 | 47.3% |
| Increfs | 6,494,466,161 | 52.5% |
| Decrefs | 7,567,071,829 | 52.7% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 66,876,796 |  |
| Method cache misses | 684 |  |
| Method cache collisions | 608 |  |
| Method cache dunder hits | 96,916,564 |  |
| Method cache dunder misses | 176 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 3,300 | 1,920 | 30,527,560 |
| 1 | 300 | 0 | 30,041,680 |
| 2 | 20 | 0 | 5,050,840 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 240 |  |
| Traces created | 240 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 40 | 16.7% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 40 | 16.7% |
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
| <= 32 | 80 | 33.3% |
| <= 64 | 80 | 33.3% |
| <= 128 | 40 | 16.7% |
| <= 256 | 40 | 16.7% |


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
| <= 16 | 40 | 16.7% |
| <= 32 | 120 | 50.0% |
| <= 64 | 20 | 8.3% |
| <= 128 | 20 | 8.3% |
| <= 256 | 40 | 16.7% |


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
| BINARY_OP_INPLACE_ADD_UNICODE | 20 |


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
