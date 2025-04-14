
# Pystats results

- benchmark: async_tree_memoization_tg
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 548,088,620 | 21.1% | 21.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 151,922,040 | 5.8% | 26.9% |  |
| POP_JUMP_IF_FALSE | 146,218,300 | 5.6% | 32.6% |  |
| RESUME_CHECK | 128,737,160 | 5.0% | 37.5% | 0.0% |
| STORE_FAST | 109,304,080 | 4.2% | 41.7% |  |
| LOAD_FAST_LOAD_FAST | 103,681,860 | 4.0% | 45.7% |  |
| LOAD_CONST | 97,416,840 | 3.7% | 49.5% |  |
| POP_TOP | 97,035,820 | 3.7% | 53.2% |  |
| TO_BOOL_BOOL | 91,414,000 | 3.5% | 56.7% | 0.0% |
| LOAD_ATTR_SLOT | 84,681,020 | 3.3% | 60.0% | 0.9% |
| STORE_ATTR_SLOT | 75,838,520 | 2.9% | 62.9% | 6.2% |
| RETURN_VALUE | 69,027,320 | 2.7% | 65.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,077,800 | 2.4% | 68.0% |  |
| CALL_PY_EXACT_ARGS | 61,582,780 | 2.4% | 70.4% |  |
| RETURN_CONST | 57,476,060 | 2.2% | 72.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 56,732,880 | 2.2% | 74.8% | 0.0% |
| INTERPRETER_EXIT | 51,855,200 | 2.0% | 76.8% |  |
| LOAD_GLOBAL_MODULE | 50,737,480 | 2.0% | 78.7% |  |
| LOAD_ATTR | 48,171,260 | 1.9% | 80.6% |  |
| PUSH_NULL | 44,712,720 | 1.7% | 82.3% |  |
| CALL | 40,701,260 | 1.6% | 83.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 32,843,580 | 1.3% | 85.1% | 0.0% |
| POP_JUMP_IF_NOT_NONE | 30,605,080 | 1.2% | 86.3% |  |
| TO_BOOL_NONE | 26,498,020 | 1.0% | 87.3% | 0.0% |
| LOAD_ATTR_MODULE | 25,747,260 | 1.0% | 88.3% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 24,258,860 | 0.9% | 89.2% | 0.0% |
| COMPARE_OP_INT | 20,463,620 | 0.8% | 90.0% |  |
| CALL_BUILTIN_O | 16,725,220 | 0.6% | 90.7% |  |
| FOR_ITER_RANGE | 15,676,160 | 0.6% | 91.3% |  |
| JUMP_BACKWARD | 15,530,980 | 0.6% | 91.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 11,946,640 | 0.5% | 92.3% |  |
| POP_JUMP_IF_NONE | 11,944,720 | 0.5% | 92.8% |  |
| NOP | 11,571,220 | 0.4% | 93.2% |  |
| BUILD_LIST | 11,569,860 | 0.4% | 93.7% |  |
| TO_BOOL | 11,205,740 | 0.4% | 94.1% |  |
| CALL_FUNCTION_EX | 10,821,540 | 0.4% | 94.5% |  |
| CALL_INTRINSIC_1 | 10,821,300 | 0.4% | 94.9% |  |
| LIST_EXTEND | 10,821,300 | 0.4% | 95.4% |  |
| POP_JUMP_IF_TRUE | 10,453,420 | 0.4% | 95.8% |  |
| RETURN_GENERATOR | 10,449,160 | 0.4% | 96.2% |  |
| BINARY_OP_SUBTRACT_INT | 8,211,380 | 0.3% | 96.5% |  |
| SEND_GEN | 7,833,600 | 0.3% | 96.8% |  |
| BINARY_OP_ADD_INT | 7,464,980 | 0.3% | 97.1% |  |
| END_SEND | 7,088,980 | 0.3% | 97.3% |  |
| GET_AWAITABLE | 7,088,980 | 0.3% | 97.6% |  |
| LOAD_GLOBAL_BUILTIN | 6,706,380 | 0.3% | 97.9% | 0.0% |
| TO_BOOL_LIST | 5,601,420 | 0.2% | 98.1% |  |
| CALL_KW | 5,597,900 | 0.2% | 98.3% |  |
| COMPARE_OP_FLOAT | 4,831,200 | 0.2% | 98.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,493,320 | 0.2% | 98.7% | 16.9% |
| JUMP_FORWARD | 4,483,220 | 0.2% | 98.8% |  |
| CALL_ISINSTANCE | 4,459,220 | 0.2% | 99.0% |  |
| CALL_PY_WITH_DEFAULTS | 4,105,120 | 0.2% | 99.2% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 3,362,160 | 0.1% | 99.3% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 2,982,320 | 0.1% | 99.4% |  |
| YIELD_VALUE | 2,982,320 | 0.1% | 99.5% |  |
| SEND | 2,238,780 | 0.1% | 99.6% |  |
| CALL_BUILTIN_CLASS | 1,495,460 | 0.1% | 99.7% |  |
| GET_ITER | 752,260 | 0.0% | 99.7% |  |
| IS_OP | 746,880 | 0.0% | 99.7% |  |
| EXIT_INIT_CHECK | 746,580 | 0.0% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 746,580 | 0.0% | 99.8% |  |
| BEFORE_ASYNC_WITH | 746,480 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 746,460 | 0.0% | 99.8% |  |
| LOAD_DEREF | 745,820 | 0.0% | 99.9% |  |
| COPY_FREE_VARS | 745,660 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR_METHOD | 745,180 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_FLOAT | 374,100 | 0.0% | 99.9% |  |
| COMPARE_OP | 373,400 | 0.0% | 100.0% |  |
| BUILD_MAP | 372,700 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 372,520 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 372,500 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,660 | 0.0% | 100.0% |  |
| STORE_ATTR | 3,700 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 3,700 | 0.0% | 100.0% |  |
| COPY | 2,580 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| RESUME | 2,040 | 0.0% | 100.0% | 1,516.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 1,840 | 0.0% | 100.0% |  |
| BINARY_OP | 1,160 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 640 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 460 | 0.0% | 100.0% |  |
| FOR_ITER | 440 | 0.0% | 100.0% |  |
| SWAP | 340 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 240 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 240 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| CONTAINS_OP | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 100 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| MAKE_CELL | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |
| BEFORE_WITH | 40 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 40 | 0.0% | 100.0% |  |
| IMPORT_FROM | 20 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 20 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 20 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 20 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 147,440,740 | 5.7% | 5.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 111,278,340 | 4.3% | 10.0% |
| RESUME_CHECK LOAD_FAST | 89,570,100 | 3.4% | 13.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 85,443,380 | 3.3% | 16.7% |
| LOAD_FAST LOAD_ATTR_SLOT | 84,666,420 | 3.3% | 20.0% |
| STORE_FAST LOAD_FAST | 80,251,900 | 3.1% | 23.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 52,626,200 | 2.0% | 25.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 50,757,400 | 2.0% | 27.0% |
| CACHE RESUME_CHECK | 45,510,520 | 1.8% | 28.8% |
| POP_TOP LOAD_FAST | 44,787,280 | 1.7% | 30.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 42,922,700 | 1.7% | 32.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 42,177,840 | 1.6% | 33.8% |
| LOAD_CONST LOAD_FAST | 42,169,480 | 1.6% | 35.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 42,168,420 | 1.6% | 37.0% |
| LOAD_FAST RETURN_VALUE | 38,070,020 | 1.5% | 38.5% |
| LOAD_FAST LOAD_ATTR | 36,209,960 | 1.4% | 39.9% |
| LOAD_FAST STORE_ATTR_SLOT | 33,581,280 | 1.3% | 41.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 32,843,560 | 1.3% | 42.4% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 31,349,480 | 1.2% | 43.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 31,347,180 | 1.2% | 44.8% |
| RETURN_CONST INTERPRETER_EXIT | 28,737,780 | 1.1% | 46.0% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 28,364,360 | 1.1% | 47.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 27,247,760 | 1.0% | 48.1% |
| RETURN_CONST POP_TOP | 26,872,680 | 1.0% | 49.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 26,498,000 | 1.0% | 50.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 25,746,140 | 1.0% | 51.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 24,627,840 | 0.9% | 52.1% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,886,320 | 0.9% | 53.0% |
| STORE_ATTR_SLOT LOAD_CONST | 21,642,900 | 0.8% | 53.8% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 21,270,100 | 0.8% | 54.7% |
| RETURN_VALUE INTERPRETER_EXIT | 20,505,680 | 0.8% | 55.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 20,463,620 | 0.8% | 56.2% |
| CALL STORE_FAST | 20,152,260 | 0.8% | 57.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 19,407,260 | 0.7% | 57.8% |
| RETURN_VALUE STORE_FAST | 19,035,280 | 0.7% | 58.5% |
| PUSH_NULL LOAD_FAST | 18,587,380 | 0.7% | 59.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 17,918,180 | 0.7% | 59.9% |
| LOAD_FAST LOAD_CONST | 17,916,300 | 0.7% | 60.6% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 16,419,540 | 0.6% | 61.2% |
| CALL_BUILTIN_O STORE_FAST | 16,352,820 | 0.6% | 61.8% |
| LOAD_FAST CALL_BUILTIN_O | 16,352,740 | 0.6% | 62.5% |
| POP_JUMP_IF_FALSE RETURN_CONST | 16,047,360 | 0.6% | 63.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 15,300,660 | 0.6% | 63.7% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,928,200 | 0.6% | 64.3% |
| POP_TOP JUMP_BACKWARD | 14,927,880 | 0.6% | 64.8% |
| JUMP_BACKWARD FOR_ITER_RANGE | 14,927,840 | 0.6% | 65.4% |
| FOR_ITER_RANGE STORE_FAST | 14,927,840 | 0.6% | 66.0% |
| POP_TOP RETURN_CONST | 14,554,940 | 0.6% | 66.5% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 14,554,020 | 0.6% | 67.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 14,186,120 | 0.5% | 67.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 14,181,840 | 0.5% | 68.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 14,181,440 | 0.5% | 68.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 13,809,140 | 0.5% | 69.3% |
| LOAD_CONST COMPARE_OP_INT | 11,946,040 | 0.5% | 69.7% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 11,945,020 | 0.5% | 70.2% |
| POP_JUMP_IF_NONE LOAD_FAST | 11,943,920 | 0.5% | 70.7% |
| POP_JUMP_IF_FALSE LOAD_CONST | 11,573,660 | 0.4% | 71.1% |
| NOP LOAD_FAST | 11,570,660 | 0.4% | 71.5% |
| POP_TOP LOAD_CONST | 11,570,360 | 0.4% | 72.0% |
| BUILD_LIST LOAD_FAST | 11,568,020 | 0.4% | 72.4% |
| STORE_ATTR_SLOT LOAD_FAST | 11,566,120 | 0.4% | 72.9% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 11,565,940 | 0.4% | 73.3% |
| LOAD_CONST STORE_FAST | 11,204,760 | 0.4% | 73.8% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 11,199,400 | 0.4% | 74.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 11,197,900 | 0.4% | 74.6% |
| STORE_ATTR_SLOT RETURN_CONST | 11,193,840 | 0.4% | 75.0% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 0.4% | 75.5% |
| LOAD_ATTR PUSH_NULL | 10,822,220 | 0.4% | 75.9% |
| RETURN_VALUE TO_BOOL_BOOL | 10,821,860 | 0.4% | 76.3% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 10,821,340 | 0.4% | 76.7% |
| LIST_EXTEND CALL_INTRINSIC_1 | 10,821,300 | 0.4% | 77.1% |
| STORE_FAST RETURN_CONST | 10,450,840 | 0.4% | 77.5% |
| RESUME_CHECK NOP | 10,449,620 | 0.4% | 77.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 10,449,480 | 0.4% | 78.4% |
| LOAD_FAST_LOAD_FAST CALL | 10,449,200 | 0.4% | 78.8% |
| CALL_FUNCTION_EX POP_TOP | 10,449,160 | 0.4% | 79.2% |
| LOAD_ATTR_SLOT LOAD_ATTR | 10,449,100 | 0.4% | 79.6% |
| POP_TOP RESUME_CHECK | 10,449,000 | 0.4% | 80.0% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 10,449,000 | 0.4% | 80.4% |
| LOAD_ATTR_SLOT BUILD_LIST | 10,448,980 | 0.4% | 80.8% |
| LOAD_ATTR_SLOT LIST_EXTEND | 10,448,980 | 0.4% | 81.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 10,076,960 | 0.4% | 81.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 10,076,700 | 0.4% | 81.9% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,500 | 0.4% | 82.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 10,076,460 | 0.4% | 82.7% |
| LOAD_ATTR LOAD_FAST | 9,331,320 | 0.4% | 83.1% |
| CALL RESUME_CHECK | 9,330,720 | 0.4% | 83.4% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 9,330,500 | 0.4% | 83.8% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 9,311,860 | 0.4% | 84.2% |
| LOAD_FAST PUSH_NULL | 9,262,580 | 0.4% | 84.5% |
| LOAD_ATTR CALL | 8,959,720 | 0.3% | 84.9% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 8,888,300 | 0.3% | 85.2% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,583,660 | 0.3% | 85.5% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,211,520 | 0.3% | 85.8% |
| GET_AWAITABLE LOAD_CONST | 7,088,980 | 0.3% | 86.1% |
| TO_BOOL POP_JUMP_IF_FALSE | 6,719,520 | 0.3% | 86.4% |
| LOAD_FAST POP_JUMP_IF_NONE | 6,718,880 | 0.3% | 86.6% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 6,718,340 | 0.3% | 86.9% |
| PUSH_NULL CALL | 6,345,480 | 0.2% | 87.1% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 5,972,060 | 0.2% | 87.4% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 45,510,520 | 87.8% |
| POP_TOP | 4,478,960 | 8.6% |
| RETURN_GENERATOR | 1,492,960 | 2.9% |
| COPY_FREE_VARS | 372,420 | 0.7% |
| RESUME | 340 | 0.0% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 746,460 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 746,480 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 40 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 66.7% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 40 | 33.3% |
| PUSH_EXC_INFO | 20 | 16.7% |
| LOAD_ATTR | 20 | 16.7% |
| STORE_FAST | 20 | 16.7% |
| BINARY_SUBSCR_DICT | 20 | 16.7% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 160 | 88.9% |
| LOAD_GLOBAL | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 180 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,851,260 | 68.4% |
| RETURN_CONST | 1,118,940 | 15.8% |
| SEND | 1,118,780 | 15.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,970,200 | 84.2% |
| STORE_FAST | 746,480 | 10.5% |
| LOAD_FAST | 372,300 | 5.3% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 746,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 746,580 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 748,340 | 99.5% |
| LOAD_FAST | 3,700 | 0.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 160 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 748,280 | 99.5% |
| FOR_ITER_LIST | 3,640 | 0.5% |
| FOR_ITER | 320 | 0.0% |
| FOR_ITER_TUPLE | 20 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 28,737,780 | 55.4% |
| RETURN_VALUE | 20,505,680 | 39.5% |
| RETURN_GENERATOR | 1,492,960 | 2.9% |
| YIELD_VALUE | 1,118,780 | 2.2% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 240 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,449,620 | 90.3% |
| STORE_ATTR_INSTANCE_VALUE | 746,460 | 6.5% |
| STORE_FAST | 374,300 | 3.2% |
| POP_TOP | 400 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,570,660 | 100.0% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 100 | 55.6% |
| COPY | 80 | 44.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 100 | 55.6% |
| RERAISE | 80 | 44.4% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 32,843,560 | 33.8% |
| RETURN_CONST | 26,872,680 | 27.7% |
| CALL_FUNCTION_EX | 10,449,160 | 10.8% |
| END_SEND | 5,970,200 | 6.2% |
| SEND_GEN | 5,970,060 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,787,280 | 46.2% |
| JUMP_BACKWARD | 14,927,880 | 15.4% |
| RETURN_CONST | 14,554,940 | 15.0% |
| LOAD_CONST | 11,570,360 | 11.9% |
| RESUME_CHECK | 10,449,000 | 10.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 80 | 44.4% |
| BINARY_SUBSCR_DICT | 80 | 44.4% |
| BINARY_SUBSCR | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 160 | 88.9% |
| LOAD_GLOBAL | 20 | 11.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 24,627,840 | 55.1% |
| LOAD_ATTR | 10,822,220 | 24.2% |
| LOAD_FAST | 9,262,580 | 20.7% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,587,380 | 41.6% |
| LOAD_FAST_LOAD_FAST | 14,928,200 | 33.4% |
| CALL | 6,345,480 | 14.2% |
| LOAD_CONST | 3,732,720 | 8.3% |
| CALL_ALLOC_AND_ENTER_INIT | 746,480 | 1.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 8,583,660 | 82.1% |
| CACHE | 1,492,960 | 14.3% |
| CALL_PY_WITH_DEFAULTS | 372,280 | 3.6% |
| CALL | 120 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 4,478,920 | 42.9% |
| GET_AWAITABLE | 4,477,240 | 42.8% |
| INTERPRETER_EXIT | 1,492,960 | 14.3% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,070,020 | 55.2% |
| LOAD_ATTR_INSTANCE_VALUE | 16,419,540 | 23.8% |
| COMPARE_OP_FLOAT | 4,458,700 | 6.5% |
| RETURN_VALUE | 3,732,960 | 5.4% |
| BINARY_OP_ADD_INT | 3,732,460 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 20,505,680 | 29.7% |
| STORE_FAST | 19,035,280 | 27.6% |
| TO_BOOL_BOOL | 10,821,860 | 15.7% |
| END_SEND | 4,851,260 | 7.0% |
| POP_TOP | 4,479,120 | 6.5% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 60.0% |
| LOAD_ATTR | 40 | 40.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 40.0% |
| STORE_SUBSCR_DICT | 40 | 40.0% |
| LOAD_CONST | 20 | 20.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 11,199,400 | 99.9% |
| TO_BOOL | 3,800 | 0.0% |
| LOAD_ATTR | 760 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,719,520 | 60.0% |
| POP_JUMP_IF_TRUE | 4,480,980 | 40.0% |
| TO_BOOL | 3,800 | 0.0% |
| TO_BOOL_BOOL | 980 | 0.0% |
| TO_BOOL_INT | 160 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 80 | 50.0% |
| LOAD_ATTR_MODULE | 60 | 37.5% |
| LOAD_ATTR | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 160 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 60 | 37.5% |
| TO_BOOL_INT | 60 | 37.5% |
| TO_BOOL | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 20.7% |
| LOAD_GLOBAL_MODULE | 180 | 15.5% |
| UNARY_INVERT | 160 | 13.8% |
| BINARY_OP | 160 | 13.8% |
| LOAD_CONST | 160 | 13.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 220 | 19.0% |
| BINARY_OP | 160 | 13.8% |
| COPY | 160 | 13.8% |
| LOAD_GLOBAL_MODULE | 120 | 10.3% |
| UNARY_INVERT | 80 | 6.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 10,448,980 | 90.3% |
| STORE_ATTR_INSTANCE_VALUE | 746,680 | 6.5% |
| LOAD_FAST | 372,300 | 3.2% |
| STORE_FAST | 1,840 | 0.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,568,020 | 100.0% |
| STORE_FAST | 1,840 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 372,300 | 99.9% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 372,300 | 99.9% |
| LOAD_FAST | 400 | 0.1% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 37.5% |
| CALL | 80 | 12.5% |
| LOAD_CONST | 80 | 12.5% |
| LOAD_FAST_LOAD_FAST | 80 | 12.5% |
| LOAD_GLOBAL_MODULE | 80 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240 | 37.5% |
| CALL | 160 | 25.0% |
| RETURN_VALUE | 80 | 12.5% |
| BUILD_MAP | 80 | 12.5% |
| CALL_ISINSTANCE | 40 | 6.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,449,200 | 25.7% |
| LOAD_ATTR | 8,959,720 | 22.0% |
| PUSH_NULL | 6,345,480 | 15.6% |
| LOAD_FAST | 5,225,800 | 12.8% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,120 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,152,260 | 49.5% |
| RESUME_CHECK | 9,330,720 | 22.9% |
| POP_TOP | 5,598,480 | 13.8% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,120 | 11.0% |
| LOAD_FAST | 747,140 | 1.8% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 10,449,000 | 96.6% |
| BUILD_MAP | 372,300 | 3.4% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,449,160 | 96.6% |
| STORE_FAST | 372,300 | 3.4% |
| COPY_FREE_VARS | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 10,821,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 10,449,000 | 96.6% |
| LOAD_CONST | 372,300 | 3.4% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,597,900 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 80.0% |
| RETURN_VALUE | 1,118,780 | 20.0% |
| POP_TOP | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 372,600 | 99.8% |
| COMPARE_OP | 320 | 0.1% |
| CALL_BUILTIN_CLASS | 140 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 372,760 | 99.8% |
| COMPARE_OP | 320 | 0.1% |
| COMPARE_OP_INT | 220 | 0.1% |
| COMPARE_OP_FLOAT | 60 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 60 | 37.5% |
| LOAD_GLOBAL_MODULE | 60 | 37.5% |
| LOAD_ATTR | 20 | 12.5% |
| LOAD_GLOBAL | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 160 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 1,820 | 70.5% |
| BINARY_OP | 160 | 6.2% |
| LOAD_FAST | 160 | 6.2% |
| CALL_BUILTIN_FAST | 140 | 5.4% |
| UNARY_NOT | 80 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 1,880 | 72.9% |
| TO_BOOL | 240 | 9.3% |
| TO_BOOL_BOOL | 200 | 7.8% |
| POP_EXCEPT | 80 | 3.1% |
| LOAD_ATTR | 80 | 3.1% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 372,920 | 50.0% |
| CACHE | 372,420 | 49.9% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL_ALLOC_AND_ENTER_INIT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 745,260 | 99.9% |
| RESUME | 240 | 0.0% |
| RETURN_GENERATOR | 80 | 0.0% |
| MAKE_CELL | 80 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 320 | 72.7% |
| FOR_ITER | 80 | 18.2% |
| JUMP_BACKWARD | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 27.3% |
| LOAD_FAST | 100 | 22.7% |
| FOR_ITER | 80 | 18.2% |
| FOR_ITER_LIST | 60 | 13.6% |
| STORE_FAST | 40 | 9.1% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 4,477,240 | 63.2% |
| BEFORE_ASYNC_WITH | 746,480 | 10.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 746,460 | 10.5% |
| LOAD_ATTR_INSTANCE_VALUE | 746,460 | 10.5% |
| LOAD_FAST | 372,300 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,088,980 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 80.0% |
| IMPORT_FROM | 20 | 20.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 746,460 | 99.9% |
| LOAD_CONST | 400 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 746,480 | 99.9% |
| RETURN_VALUE | 400 | 0.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 14,927,880 | 96.1% |
| POP_JUMP_IF_FALSE | 603,100 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 14,927,840 | 96.1% |
| LOAD_FAST | 603,080 | 3.9% |
| FOR_ITER | 40 | 0.0% |
| FOR_ITER_TUPLE | 20 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,982,160 | 100.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 1,863,500 | 62.5% |
| SEND | 1,118,820 | 37.5% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,482,960 | 100.0% |
| POP_JUMP_IF_FALSE | 160 | 0.0% |
| POP_TOP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,200 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 1,880 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 10,448,980 | 96.6% |
| LOAD_FAST | 372,300 | 3.4% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 10,821,300 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,209,960 | 75.2% |
| LOAD_ATTR_SLOT | 10,449,100 | 21.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,493,560 | 3.1% |
| LOAD_ATTR | 15,780 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 10,822,220 | 22.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,500 | 20.9% |
| LOAD_FAST | 9,331,320 | 19.4% |
| CALL | 8,959,720 | 18.6% |
| TO_BOOL_NONE | 4,478,920 | 9.3% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 21,642,900 | 22.2% |
| LOAD_FAST | 17,916,300 | 18.4% |
| POP_JUMP_IF_FALSE | 11,573,660 | 11.9% |
| POP_TOP | 11,570,360 | 11.9% |
| LOAD_FAST_LOAD_FAST | 8,211,520 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,169,480 | 43.3% |
| COMPARE_OP_INT | 11,946,040 | 12.3% |
| STORE_FAST | 11,204,760 | 11.5% |
| SEND_GEN | 5,969,960 | 6.1% |
| CALL_KW | 5,597,900 | 5.7% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 745,180 | 99.9% |
| LOAD_GLOBAL | 240 | 0.0% |
| STORE_FAST | 160 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 745,420 | 99.9% |
| LOAD_CONST | 160 | 0.0% |
| PUSH_NULL | 80 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 111,278,340 | 20.3% |
| RESUME_CHECK | 89,570,100 | 16.3% |
| STORE_FAST | 80,251,900 | 14.6% |
| POP_TOP | 44,787,280 | 8.2% |
| LOAD_CONST | 42,169,480 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 147,440,740 | 26.9% |
| LOAD_ATTR_SLOT | 84,666,420 | 15.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 42,922,700 | 7.8% |
| RETURN_VALUE | 38,070,020 | 6.9% |
| LOAD_ATTR | 36,209,960 | 6.6% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 20 | 100.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 31,347,180 | 30.2% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 14.8% |
| PUSH_NULL | 14,928,200 | 14.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,809,140 | 13.3% |
| POP_JUMP_IF_NOT_NONE | 10,076,700 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 42,168,420 | 40.7% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 14.8% |
| LOAD_FAST | 10,449,480 | 10.1% |
| CALL | 10,449,200 | 10.1% |
| LOAD_CONST | 8,211,520 | 7.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 600 | 12.9% |
| RESUME_CHECK | 580 | 12.4% |
| LOAD_FAST | 540 | 11.6% |
| POP_TOP | 500 | 10.7% |
| POP_JUMP_IF_FALSE | 460 | 9.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,600 | 34.3% |
| LOAD_ATTR | 980 | 21.0% |
| LOAD_GLOBAL_BUILTIN | 660 | 14.2% |
| LOAD_FAST | 400 | 8.6% |
| CALL | 300 | 6.4% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 460 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 220 | 47.8% |
| CALL | 140 | 30.4% |
| LOAD_FAST | 60 | 13.0% |
| LOAD_FAST_LOAD_FAST | 40 | 8.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 75.0% |
| RESUME | 20 | 25.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 85,443,380 | 58.4% |
| TO_BOOL_NONE | 26,498,000 | 18.1% |
| COMPARE_OP_INT | 20,463,620 | 14.0% |
| TO_BOOL | 6,719,520 | 4.6% |
| TO_BOOL_LIST | 5,601,420 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 111,278,340 | 76.1% |
| RETURN_CONST | 16,047,360 | 11.0% |
| LOAD_CONST | 11,573,660 | 7.9% |
| LOAD_FAST_LOAD_FAST | 4,104,880 | 2.8% |
| LOAD_GLOBAL_MODULE | 2,607,940 | 1.8% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,718,880 | 56.2% |
| LOAD_ATTR_INSTANCE_VALUE | 5,225,580 | 43.7% |
| CALL | 160 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,943,920 | 100.0% |
| RETURN_CONST | 480 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,886,320 | 78.0% |
| LOAD_ATTR_INSTANCE_VALUE | 6,718,340 | 22.0% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,076,700 | 32.9% |
| LOAD_GLOBAL_MODULE | 9,330,500 | 30.5% |
| LOAD_FAST | 5,972,060 | 19.5% |
| RETURN_CONST | 4,478,880 | 14.6% |
| LOAD_CONST | 746,500 | 2.4% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,970,560 | 57.1% |
| TO_BOOL | 4,480,980 | 42.9% |
| TO_BOOL_INT | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,076,960 | 96.4% |
| LOAD_CONST | 374,220 | 3.6% |
| STORE_FAST | 1,840 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,047,360 | 27.9% |
| POP_TOP | 14,554,940 | 25.3% |
| STORE_ATTR_SLOT | 11,193,840 | 19.5% |
| STORE_FAST | 10,450,840 | 18.2% |
| POP_JUMP_IF_NOT_NONE | 4,478,880 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 28,737,780 | 50.0% |
| POP_TOP | 26,872,680 | 46.8% |
| END_SEND | 1,118,940 | 1.9% |
| EXIT_INIT_CHECK | 746,580 | 1.3% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,119,020 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,118,820 | 50.0% |
| SEND | 940 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 1,118,780 | 50.0% |
| YIELD_VALUE | 1,118,780 | 50.0% |
| SEND | 940 | 0.0% |
| POP_TOP | 140 | 0.0% |
| SEND_GEN | 140 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,860 | 77.3% |
| LOAD_FAST_LOAD_FAST | 340 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 7.6% |
| STORE_ATTR | 100 | 2.7% |
| SWAP | 80 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,280 | 34.6% |
| LOAD_FAST | 620 | 16.8% |
| LOAD_CONST | 520 | 14.1% |
| RETURN_CONST | 520 | 14.1% |
| STORE_ATTR_SLOT | 340 | 9.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20,152,260 | 18.4% |
| RETURN_VALUE | 19,035,280 | 17.4% |
| CALL_BUILTIN_O | 16,352,820 | 15.0% |
| FOR_ITER_RANGE | 14,927,840 | 13.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,181,440 | 13.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80,251,900 | 73.4% |
| RETURN_CONST | 10,450,840 | 9.6% |
| LOAD_FAST_LOAD_FAST | 8,888,300 | 8.1% |
| JUMP_FORWARD | 4,482,960 | 4.1% |
| LOAD_GLOBAL_MODULE | 3,732,640 | 3.4% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 20 | 100.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 120 | 75.0% |
| UNPACK_SEQUENCE | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 50.0% |
| LOAD_GLOBAL | 40 | 25.0% |
| LOAD_GLOBAL_MODULE | 40 | 25.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 80 | 23.5% |
| LOAD_FAST | 80 | 23.5% |
| BINARY_OP_ADD_INT | 60 | 17.6% |
| BINARY_OP_SUBTRACT_INT | 60 | 17.6% |
| BINARY_OP | 40 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 100 | 29.4% |
| STORE_ATTR | 80 | 23.5% |
| STORE_FAST | 80 | 23.5% |
| STORE_ATTR_INSTANCE_VALUE | 80 | 23.5% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 33.3% |
| CALL | 40 | 33.3% |
| STORE_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 50.0% |
| STORE_FAST_STORE_FAST | 40 | 33.3% |
| LOAD_FAST | 20 | 16.7% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,863,540 | 62.5% |
| SEND | 1,118,780 | 37.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,863,540 | 62.5% |
| INTERPRETER_EXIT | 1,118,780 | 37.5% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,160 | 56.9% |
| CACHE | 340 | 16.7% |
| COPY_FREE_VARS | 240 | 11.8% |
| POP_TOP | 160 | 7.8% |
| SEND_GEN | 100 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 960 | 47.1% |
| LOAD_GLOBAL | 600 | 29.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 160 | 7.8% |
| LOAD_CONST | 140 | 6.9% |
| NOP | 100 | 4.9% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 372,260 | 99.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,800 | 0.5% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 372,280 | 99.5% |
| STORE_FAST | 1,820 | 0.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,732,480 | 50.0% |
| RETURN_VALUE | 3,732,440 | 50.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,732,460 | 50.0% |
| CALL_PY_WITH_DEFAULTS | 3,732,440 | 50.0% |
| SWAP | 60 | 0.0% |
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
| LOAD_CONST | 4,478,880 | 54.5% |
| LOAD_FAST_LOAD_FAST | 3,732,440 | 45.5% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,478,840 | 54.5% |
| STORE_FAST | 3,732,460 | 45.5% |
| SWAP | 60 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 80 | 57.1% |
| LOAD_FAST | 40 | 28.6% |
| BINARY_SUBSCR | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 57.1% |
| RETURN_VALUE | 60 | 42.9% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 80 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 372,460 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 372,360 | 100.0% |
| LOAD_ATTR_SLOT | 120 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20 | 100.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 746,480 | 100.0% |
| CALL | 60 | 0.0% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 746,520 | 100.0% |
| COPY_FREE_VARS | 60 | 0.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,478,880 | 99.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 0.3% |
| CALL | 60 | 0.0% |
| PUSH_NULL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,732,460 | 83.1% |
| GET_AWAITABLE | 746,460 | 16.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 0.3% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 746,660 | 49.9% |
| LOAD_GLOBAL_MODULE | 746,440 | 49.9% |
| LOAD_FAST | 1,980 | 0.1% |
| CALL | 180 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 748,340 | 50.0% |
| LOAD_FAST | 746,700 | 49.9% |
| COMPARE_OP | 140 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 372,260 | 99.9% |
| LOAD_CONST | 180 | 0.0% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 372,280 | 99.9% |
| COPY | 140 | 0.0% |
| TO_BOOL_BOOL | 80 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 746,440 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,460 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,352,740 | 97.8% |
| LOAD_ATTR_INSTANCE_VALUE | 372,260 | 2.2% |
| CALL | 180 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 16,352,820 | 97.8% |
| TO_BOOL_BOOL | 372,260 | 2.2% |
| POP_TOP | 120 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,458,720 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 380 | 0.0% |
| CALL | 80 | 0.0% |
| BUILD_TUPLE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 4,459,140 | 100.0% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,400 | 98.9% |
| CALL | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,640 | 66.7% |
| COPY | 1,820 | 33.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,361,940 | 100.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |
| CALL | 60 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,359,540 | 99.9% |
| TO_BOOL_NONE | 2,400 | 0.1% |
| RETURN_VALUE | 140 | 0.0% |
| STORE_FAST | 60 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,800 | 89.1% |
| LOAD_CONST | 80 | 4.0% |
| CALL | 60 | 3.0% |
| LOAD_ATTR | 40 | 2.0% |
| LOAD_FAST | 40 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,820 | 90.1% |
| POP_TOP | 120 | 5.9% |
| RETURN_VALUE | 80 | 4.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 14,181,840 | 58.5% |
| LOAD_ATTR | 10,076,500 | 41.5% |
| CALL | 400 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,181,440 | 58.5% |
| TO_BOOL_BOOL | 10,076,460 | 41.5% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |
| CALL | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,364,360 | 86.4% |
| CALL | 4,479,120 | 13.6% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 32,843,560 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 31,349,480 | 50.9% |
| LOAD_FAST | 14,186,120 | 23.0% |
| LOAD_ATTR_METHOD_NO_DICT | 10,821,340 | 17.6% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 7.3% |
| LOAD_SUPER_ATTR_METHOD | 372,460 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 52,626,200 | 85.5% |
| RETURN_GENERATOR | 8,583,660 | 13.9% |
| COPY_FREE_VARS | 372,920 | 0.6% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 3,732,440 | 90.9% |
| LOAD_GLOBAL_MODULE | 372,260 | 9.1% |
| CALL | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,732,840 | 90.9% |
| RETURN_GENERATOR | 372,280 | 9.1% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 66.7% |
| LOAD_GLOBAL | 20 | 33.3% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 4,458,680 | 92.3% |
| LOAD_FAST | 372,340 | 7.7% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,458,700 | 92.3% |
| POP_JUMP_IF_FALSE | 372,500 | 7.7% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,946,040 | 58.4% |
| LOAD_FAST_LOAD_FAST | 4,783,120 | 23.4% |
| LOAD_GLOBAL_MODULE | 3,734,240 | 18.2% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,463,620 | 100.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 100.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 3,640 | 98.4% |
| FOR_ITER | 60 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,880 | 50.8% |
| LOAD_FAST | 1,820 | 49.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 14,927,840 | 95.2% |
| GET_ITER | 748,280 | 4.8% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,927,840 | 95.2% |
| LOAD_CONST | 748,320 | 4.8% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 50.0% |
| JUMP_BACKWARD | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| STORE_FAST | 20 | 50.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| LOAD_ATTR | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 147,440,740 | 97.1% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 2.9% |
| LOAD_ATTR | 1,980 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 50,757,400 | 33.4% |
| LOAD_ATTR_METHOD_NO_DICT | 42,177,840 | 27.8% |
| RETURN_VALUE | 16,419,540 | 10.8% |
| TO_BOOL | 11,199,400 | 7.4% |
| POP_JUMP_IF_NOT_NONE | 6,718,340 | 4.4% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 42,177,840 | 74.3% |
| LOAD_FAST | 14,554,020 | 25.7% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 320 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,247,760 | 48.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,181,840 | 25.0% |
| CALL_PY_EXACT_ARGS | 10,821,340 | 19.1% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 7.9% |
| LOAD_FAST_LOAD_FAST | 1,960 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,922,700 | 68.0% |
| LOAD_ATTR_SLOT | 11,193,640 | 17.7% |
| LOAD_ATTR_INSTANCE_VALUE | 5,227,400 | 8.3% |
| LOAD_FAST_LOAD_FAST | 3,732,480 | 5.9% |
| LOAD_ATTR | 1,260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 31,349,480 | 49.7% |
| LOAD_FAST | 17,918,180 | 28.4% |
| LOAD_FAST_LOAD_FAST | 13,809,140 | 21.9% |
| CALL | 700 | 0.0% |
| LOAD_CONST | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 25,746,140 | 100.0% |
| LOAD_ATTR | 1,000 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 24,627,840 | 95.7% |
| IS_OP | 746,460 | 2.9% |
| LOAD_FAST_LOAD_FAST | 372,280 | 1.4% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_FAST | 120 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 66.7% |
| LOAD_ATTR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 84,666,420 | 100.0% |
| LOAD_ATTR_SLOT | 13,920 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 21,270,100 | 25.1% |
| TO_BOOL_BOOL | 11,565,940 | 13.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 13.2% |
| LOAD_ATTR | 10,449,100 | 12.3% |
| BUILD_LIST | 10,448,980 | 12.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,833,820 | 72.1% |
| STORE_FAST | 748,300 | 11.2% |
| STORE_ATTR_INSTANCE_VALUE | 746,580 | 11.1% |
| POP_TOP | 372,460 | 5.6% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,467,280 | 66.6% |
| CALL_BUILTIN_CLASS | 746,660 | 11.1% |
| LOAD_GLOBAL_MODULE | 746,480 | 11.1% |
| LOAD_DEREF | 745,180 | 11.1% |
| CALL_ISINSTANCE | 380 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 19,407,260 | 38.3% |
| POP_JUMP_IF_NOT_NONE | 9,330,500 | 18.4% |
| LOAD_FAST | 9,311,860 | 18.4% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 8.8% |
| STORE_FAST | 3,732,640 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 25,746,140 | 50.7% |
| LOAD_FAST | 11,197,900 | 22.1% |
| LOAD_FAST_LOAD_FAST | 4,479,200 | 8.8% |
| CALL_ISINSTANCE | 4,458,720 | 8.8% |
| COMPARE_OP_INT | 3,734,240 | 7.4% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 744,960 | 100.0% |
| LOAD_SUPER_ATTR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 372,460 | 50.0% |
| LOAD_FAST_LOAD_FAST | 372,340 | 50.0% |
| LOAD_FAST | 260 | 0.0% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 52,626,200 | 40.9% |
| CACHE | 45,510,520 | 35.4% |
| POP_TOP | 10,449,000 | 8.1% |
| CALL | 9,330,720 | 7.2% |
| CALL_PY_WITH_DEFAULTS | 3,732,840 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,570,100 | 69.6% |
| LOAD_GLOBAL_MODULE | 19,407,260 | 15.1% |
| NOP | 10,449,620 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 4,833,820 | 3.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,982,160 | 2.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,969,960 | 76.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,863,500 | 23.8% |
| SEND | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,970,060 | 76.2% |
| RESUME_CHECK | 1,863,440 | 23.8% |
| RESUME | 100 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,945,020 | 100.0% |
| STORE_ATTR | 1,280 | 0.0% |
| LOAD_FAST_LOAD_FAST | 260 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,226,060 | 43.7% |
| LOAD_FAST | 2,986,600 | 25.0% |
| RETURN_CONST | 747,120 | 6.3% |
| LOAD_GLOBAL_MODULE | 746,800 | 6.3% |
| BUILD_LIST | 746,680 | 6.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 42,168,420 | 55.6% |
| LOAD_FAST | 33,581,280 | 44.3% |
| STORE_ATTR_SLOT | 88,480 | 0.1% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 31,347,180 | 41.3% |
| LOAD_CONST | 21,642,900 | 28.5% |
| LOAD_FAST | 11,566,120 | 15.3% |
| RETURN_CONST | 11,193,840 | 14.8% |
| STORE_ATTR_SLOT | 88,480 | 0.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,760 | 95.7% |
| STORE_SUBSCR | 40 | 2.2% |
| LOAD_ATTR | 40 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,840 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 50,757,400 | 55.5% |
| LOAD_ATTR_SLOT | 11,565,940 | 12.7% |
| RETURN_VALUE | 10,821,860 | 11.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,460 | 11.0% |
| CALL_ISINSTANCE | 4,459,140 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 85,443,380 | 93.5% |
| POP_JUMP_IF_TRUE | 5,970,560 | 6.5% |
| UNARY_NOT | 60 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,880 | 85.5% |
| TO_BOOL | 160 | 7.3% |
| LOAD_FAST | 80 | 3.6% |
| BINARY_OP | 40 | 1.8% |
| LOAD_ATTR_SLOT | 40 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,880 | 85.5% |
| POP_JUMP_IF_FALSE | 260 | 11.8% |
| UNARY_NOT | 60 | 2.7% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,601,320 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,601,420 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 21,270,100 | 80.3% |
| LOAD_ATTR | 4,478,920 | 16.9% |
| LOAD_FAST | 746,440 | 2.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,400 | 0.0% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 26,498,000 | 100.0% |
| TO_BOOL_BOOL | 20 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE | 60 | 33.3% |
| RETURN_VALUE | 40 | 22.2% |
| CALL | 40 | 22.2% |
| STORE_FAST | 40 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 120 | 66.7% |
| LOAD_FAST | 60 | 33.3% |


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
|     deferred | 820 | 0.0% |
|          hit | 16,050,520 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 52.9% |
| Failure | 160 | 47.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 80 | 50.0% |
| or | 40 | 25.0% |
| true divide other | 40 | 25.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 0.0% |
|          hit | 372,740 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40,670,340 | 20.4% |
|          hit | 158,170,160 | 79.2% |
|         miss | 761,180 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,520 | 56.7% |
| Failure | 13,400 | 43.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 3,280 | 24.5% |
| no dict | 2,960 | 22.1% |
| code complex parameters | 2,900 | 21.6% |
| cfunc noargs | 1,380 | 10.3% |
| class no vectorcall | 1,340 | 10.0% |
| other | 1,280 | 9.6% |
| class mutable | 80 | 0.6% |
| wrong number arguments | 40 | 0.3% |
| cfunc varargs | 40 | 0.3% |
| operator wrapper | 40 | 0.3% |
| cmethod | 20 | 0.1% |
| cfunc varargs keywords | 20 | 0.1% |
| init not simple | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 372,800 | 1.5% |
|          hit | 25,294,840 | 98.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 46.7% |
| Failure | 320 | 53.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 280 | 87.5% |
| bool | 40 | 12.5% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 15,679,900 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 55.6% |
| Failure | 80 | 44.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 80 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 48,136,740 | 11.2% |
|          hit | 381,405,720 | 88.6% |
|         miss | 755,480 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 19,620 | 56.8% |
| Failure | 14,900 | 43.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 7,840 | 52.6% |
| method | 5,540 | 37.2% |
| class attr descriptor | 1,280 | 8.6% |
| not managed dict | 140 | 0.9% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,480 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 57,443,780 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,260 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 745,180 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 100.0% |
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

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,237,700 | 22.2% |
|          hit | 7,833,600 | 77.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 13.0% |
| Failure | 940 | 87.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 940 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,190,945,820 | 420,252,502,964,716.6% |
|          hit | 83,091,280 | 94.6% |
|         miss | 4,693,880 | 5.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 90,100 | 99.9% |
| Failure | 100 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overridden | 80 | 80.0% |
| overriding descriptor | 20 | 20.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 3.1% |
|          hit | 1,840 | 94.8% |

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
|     deferred | 11,200,520 | 8.3% |
|          hit | 123,514,160 | 91.7% |
|         miss | 1,480 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,420 | 27.2% |
| Failure | 3,800 | 72.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 3,700 | 97.4% |
| sequence | 100 | 2.6% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60 | 20.0% |
|          hit | 180 | 60.0% |

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
| Basic | 1,295,271,780 | 49.9% |
| Not specialized | 301,922,720 | 11.6% |
| Specialized hits | 994,577,603 | 38.3% |
| Specialized misses | 6,243,037 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR | 368,934,881,474,190,945,820 | 100.0% |
| LOAD_ATTR | 48,136,740 | 0.0% |
| CALL | 40,670,340 | 0.0% |
| TO_BOOL | 11,200,520 | 0.0% |
| SEND | 2,237,700 | 0.0% |
| COMPARE_OP | 372,800 | 0.0% |
| LOAD_GLOBAL | 2,480 | 0.0% |
| BINARY_OP | 820 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 4,693,880 | 74.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 760,800 | 12.1% |
| LOAD_ATTR_SLOT | 738,520 | 11.8% |
| RESUME | 30,937 | 0.5% |
| RESUME_CHECK | 30,937 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 16,960 | 0.3% |
| TO_BOOL_NONE | 1,060 | 0.0% |
| TO_BOOL_BOOL | 420 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 260 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 51,855,200 | 37.3% |
| Calls to Python functions inlined | 87,333,160 | 62.7% |
| Calls via PyEval_EvalFrame (total) | 51,855,200 | 37.3% |
| Calls via PyEval_EvalFrame (vector) | 46,257,460 | 33.2% |
| Calls via PyEval_EvalFrame (generator) | 5,597,740 | 4.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 46,257,460 | 33.2% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 4,458,720 | 3.2% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.2% |
| Calls via PyEval_EvalFrame (method) | 20,153,400 | 14.5% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 70,913,660 | 50.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 56,534,252 | 33.9% |
| Frees to freelist | 56,907,889 |  |
| Allocations | 110,186,520 | 66.1% |
| Allocations to 512 bytes | 109,378,026 | 65.6% |
| Allocations to 4 kbytes | 808,354 | 0.5% |
| Allocations over 4 kbytes | 140 | 0.0% |
| Frees | 110,109,137 |  |
| New values | 320 |  |
| Interpreter increfs | 1,276,521,800 | 79.0% |
| Interpreter decrefs | 1,351,649,344 | 76.7% |
| Increfs | 338,659,068 | 21.0% |
| Decrefs | 410,049,346 | 23.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 73,772,609 |  |
| Method cache misses | 4,351 |  |
| Method cache collisions | 4,031 |  |
| Method cache dunder hits | 16,402,081 |  |
| Method cache dunder misses | 439 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 55,349 | 0 | 377,954,800 |
| 1 | 5,040 | 60 | 393,898,616 |
| 2 | 458 | 0 | 997,129,380 |


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
