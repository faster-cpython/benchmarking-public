
# Pystats results

- benchmark: async_tree_memoization_tg
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 459,774,360 | 20.5% | 20.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 129,913,220 | 5.8% | 26.2% |  |
| POP_JUMP_IF_FALSE | 123,603,700 | 5.5% | 31.7% |  |
| RESUME_CHECK | 118,662,580 | 5.3% | 37.0% | 0.0% |
| LOAD_FAST_LOAD_FAST | 107,931,980 | 4.8% | 41.8% |  |
| LOAD_CONST | 101,152,000 | 4.5% | 46.3% |  |
| POP_TOP | 92,185,120 | 4.1% | 50.4% |  |
| STORE_FAST | 87,437,840 | 3.9% | 54.3% |  |
| STORE_ATTR_SLOT | 75,466,700 | 3.4% | 57.6% | 6.2% |
| TO_BOOL_BOOL | 71,264,840 | 3.2% | 60.8% | 0.0% |
| RETURN_VALUE | 69,027,200 | 3.1% | 63.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,077,800 | 2.8% | 66.7% |  |
| RETURN_CONST | 57,476,060 | 2.6% | 69.3% |  |
| INTERPRETER_EXIT | 51,855,320 | 2.3% | 71.6% |  |
| CALL_PY_EXACT_ARGS | 51,508,200 | 2.3% | 73.8% |  |
| LOAD_GLOBAL_MODULE | 49,619,200 | 2.2% | 76.1% |  |
| LOAD_ATTR_SLOT | 44,009,760 | 2.0% | 78.0% | 1.6% |
| CALL | 36,221,180 | 1.6% | 79.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 35,839,340 | 1.6% | 81.2% | 0.0% |
| PUSH_NULL | 34,037,560 | 1.5% | 82.7% |  |
| LOAD_ATTR | 33,614,020 | 1.5% | 84.2% |  |
| POP_JUMP_IF_NOT_NONE | 30,605,080 | 1.4% | 85.6% |  |
| CALL_METHOD_DESCRIPTOR_O | 27,992,900 | 1.2% | 86.8% | 0.0% |
| TO_BOOL_NONE | 25,751,560 | 1.1% | 88.0% | 0.0% |
| LOAD_ATTR_MODULE | 24,628,980 | 1.1% | 89.1% |  |
| COMPARE_OP_INT | 20,234,860 | 0.9% | 90.0% |  |
| CALL_BUILTIN_O | 16,124,640 | 0.7% | 90.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 13,811,980 | 0.6% | 91.3% | 0.0% |
| POP_JUMP_IF_NONE | 13,437,680 | 0.6% | 91.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 11,946,640 | 0.5% | 92.4% |  |
| TO_BOOL | 11,205,700 | 0.5% | 92.9% |  |
| CALL_FUNCTION_EX | 10,821,540 | 0.5% | 93.4% |  |
| ENTER_EXECUTOR | 10,677,620 | 0.5% | 93.9% |  |
| POP_JUMP_IF_TRUE | 10,453,420 | 0.5% | 94.4% |  |
| RETURN_GENERATOR | 10,449,160 | 0.5% | 94.8% |  |
| CALL_KW | 10,076,780 | 0.4% | 95.3% |  |
| BINARY_OP_SUBTRACT_INT | 8,211,380 | 0.4% | 95.6% |  |
| SEND_GEN | 7,833,600 | 0.3% | 96.0% |  |
| BINARY_OP_ADD_INT | 7,464,980 | 0.3% | 96.3% |  |
| END_SEND | 7,088,980 | 0.3% | 96.6% |  |
| GET_AWAITABLE | 7,088,980 | 0.3% | 96.9% |  |
| LOAD_GLOBAL_BUILTIN | 6,706,380 | 0.3% | 97.2% | 0.0% |
| TO_BOOL_LIST | 5,229,600 | 0.2% | 97.5% |  |
| FOR_ITER_RANGE | 5,229,280 | 0.2% | 97.7% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,493,320 | 0.2% | 97.9% | 16.9% |
| JUMP_FORWARD | 4,483,220 | 0.2% | 98.1% |  |
| JUMP_BACKWARD | 4,481,680 | 0.2% | 98.3% |  |
| COMPARE_OP_FLOAT | 4,459,300 | 0.2% | 98.5% |  |
| CALL_ISINSTANCE | 4,459,220 | 0.2% | 98.7% |  |
| CALL_PY_WITH_DEFAULTS | 4,105,120 | 0.2% | 98.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 3,362,160 | 0.1% | 99.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 2,982,320 | 0.1% | 99.2% |  |
| YIELD_VALUE | 2,982,320 | 0.1% | 99.3% |  |
| SEND | 2,238,780 | 0.1% | 99.4% |  |
| NOP | 1,496,560 | 0.1% | 99.5% |  |
| CALL_BUILTIN_CLASS | 1,495,460 | 0.1% | 99.5% |  |
| BUILD_LIST | 1,495,280 | 0.1% | 99.6% |  |
| GET_ITER | 752,260 | 0.0% | 99.6% |  |
| CALL_INTRINSIC_1 | 746,720 | 0.0% | 99.7% |  |
| LIST_EXTEND | 746,720 | 0.0% | 99.7% |  |
| BEFORE_ASYNC_WITH | 746,480 | 0.0% | 99.7% |  |
| EXIT_INIT_CHECK | 746,460 | 0.0% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 746,460 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 746,460 | 0.0% | 99.8% |  |
| LOAD_DEREF | 745,820 | 0.0% | 99.9% |  |
| COPY_FREE_VARS | 745,660 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR_METHOD | 745,180 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_FLOAT | 374,100 | 0.0% | 99.9% |  |
| COMPARE_OP | 373,400 | 0.0% | 100.0% |  |
| BUILD_MAP | 372,700 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 372,520 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,620 | 0.0% | 100.0% |  |
| STORE_ATTR | 3,700 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 3,700 | 0.0% | 100.0% |  |
| COPY | 2,580 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| RESUME | 2,040 | 0.0% | 100.0% | 1,517.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 1,840 | 0.0% | 100.0% |  |
| BINARY_OP | 1,160 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 640 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 600 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 460 | 0.0% | 100.0% |  |
| FOR_ITER | 440 | 0.0% | 100.0% |  |
| IS_OP | 400 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 125,431,920 | 5.6% | 5.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 90,204,060 | 4.0% | 9.6% |
| RESUME_CHECK LOAD_FAST | 89,570,100 | 4.0% | 13.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 65,294,220 | 2.9% | 16.5% |
| STORE_FAST LOAD_FAST | 58,986,240 | 2.6% | 19.1% |
| CACHE RESUME_CHECK | 45,510,580 | 2.0% | 21.1% |
| LOAD_FAST LOAD_ATTR_SLOT | 43,623,900 | 1.9% | 23.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 42,922,700 | 1.9% | 25.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 42,551,620 | 1.9% | 26.9% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 42,168,420 | 1.9% | 28.7% |
| LOAD_CONST LOAD_FAST | 41,797,660 | 1.9% | 30.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 40,682,820 | 1.8% | 32.4% |
| POP_TOP LOAD_FAST | 39,936,580 | 1.8% | 34.2% |
| LOAD_FAST RETURN_VALUE | 37,891,380 | 1.7% | 35.9% |
| LOAD_FAST STORE_ATTR_SLOT | 33,209,460 | 1.5% | 37.4% |
| LOAD_FAST LOAD_ATTR | 31,731,080 | 1.4% | 38.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 31,359,140 | 1.4% | 40.2% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 31,349,480 | 1.4% | 41.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 31,347,180 | 1.4% | 42.9% |
| RETURN_CONST INTERPRETER_EXIT | 28,737,900 | 1.3% | 44.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 27,992,880 | 1.2% | 45.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 26,875,940 | 1.2% | 46.7% |
| RETURN_CONST POP_TOP | 26,872,680 | 1.2% | 47.9% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 25,751,540 | 1.1% | 49.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 24,627,880 | 1.1% | 50.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 24,256,020 | 1.1% | 51.2% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 23,886,320 | 1.1% | 52.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 23,513,700 | 1.0% | 53.3% |
| STORE_ATTR_SLOT LOAD_CONST | 21,642,900 | 1.0% | 54.3% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 21,270,100 | 0.9% | 55.2% |
| RETURN_VALUE INTERPRETER_EXIT | 20,505,680 | 0.9% | 56.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 20,234,860 | 0.9% | 57.0% |
| CALL STORE_FAST | 20,152,320 | 0.9% | 57.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 19,407,260 | 0.9% | 58.8% |
| RETURN_VALUE STORE_FAST | 19,035,220 | 0.8% | 59.6% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 18,288,000 | 0.8% | 60.4% |
| LOAD_FAST LOAD_CONST | 17,916,300 | 0.8% | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 16,419,540 | 0.7% | 62.0% |
| LOAD_FAST CALL_BUILTIN_O | 16,123,980 | 0.7% | 62.7% |
| POP_JUMP_IF_FALSE RETURN_CONST | 16,047,360 | 0.7% | 63.4% |
| CALL_BUILTIN_O STORE_FAST | 15,752,240 | 0.7% | 64.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 15,300,660 | 0.7% | 64.8% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,928,200 | 0.7% | 65.4% |
| POP_TOP RETURN_CONST | 14,554,940 | 0.6% | 66.1% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 14,186,120 | 0.6% | 66.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 13,439,320 | 0.6% | 67.3% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 12,690,400 | 0.6% | 67.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 12,690,400 | 0.6% | 68.4% |
| LOAD_CONST COMPARE_OP_INT | 11,946,040 | 0.5% | 69.0% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 11,945,020 | 0.5% | 69.5% |
| POP_TOP LOAD_CONST | 11,570,360 | 0.5% | 70.0% |
| LOAD_CONST STORE_FAST | 11,204,760 | 0.5% | 70.5% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 11,199,400 | 0.5% | 71.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 11,197,900 | 0.5% | 71.5% |
| STORE_ATTR_SLOT LOAD_FAST | 11,194,300 | 0.5% | 72.0% |
| STORE_ATTR_SLOT RETURN_CONST | 11,193,840 | 0.5% | 72.5% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 0.5% | 73.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 10,827,180 | 0.5% | 73.5% |
| RETURN_VALUE TO_BOOL_BOOL | 10,821,860 | 0.5% | 74.0% |
| STORE_FAST RETURN_CONST | 10,450,840 | 0.5% | 74.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 10,449,480 | 0.5% | 74.9% |
| LOAD_FAST_LOAD_FAST CALL | 10,449,200 | 0.5% | 75.4% |
| CALL_FUNCTION_EX POP_TOP | 10,449,160 | 0.5% | 75.8% |
| POP_TOP RESUME_CHECK | 10,449,000 | 0.5% | 76.3% |
| POP_TOP ENTER_EXECUTOR | 10,448,660 | 0.5% | 76.8% |
| POP_JUMP_IF_TRUE LOAD_FAST | 10,076,960 | 0.4% | 77.2% |
| LOAD_CONST CALL_KW | 10,076,780 | 0.4% | 77.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 10,076,700 | 0.4% | 78.1% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,500 | 0.4% | 78.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 10,076,460 | 0.4% | 79.0% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 10,074,580 | 0.4% | 79.4% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 9,330,500 | 0.4% | 79.9% |
| LOAD_FAST PUSH_NULL | 9,033,820 | 0.4% | 80.3% |
| LOAD_ATTR CALL | 8,959,720 | 0.4% | 80.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 8,659,540 | 0.4% | 81.0% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,583,660 | 0.4% | 81.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 8,565,420 | 0.4% | 81.8% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,211,840 | 0.4% | 82.2% |
| PUSH_NULL LOAD_FAST | 7,912,220 | 0.4% | 82.5% |
| GET_AWAITABLE LOAD_CONST | 7,088,980 | 0.3% | 82.8% |
| TO_BOOL POP_JUMP_IF_FALSE | 6,719,500 | 0.3% | 83.1% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 6,718,340 | 0.3% | 83.4% |
| PUSH_NULL CALL | 6,345,520 | 0.3% | 83.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 5,972,060 | 0.3% | 84.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 5,970,560 | 0.3% | 84.3% |
| END_SEND POP_TOP | 5,970,200 | 0.3% | 84.5% |
| SEND_GEN POP_TOP | 5,970,060 | 0.3% | 84.8% |
| LOAD_CONST SEND_GEN | 5,969,960 | 0.3% | 85.0% |
| CALL POP_TOP | 5,598,460 | 0.2% | 85.3% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 5,229,600 | 0.2% | 85.5% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 5,229,500 | 0.2% | 85.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 5,227,400 | 0.2% | 86.0% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 5,226,060 | 0.2% | 86.2% |
| LOAD_CONST LOAD_CONST | 5,225,620 | 0.2% | 86.5% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 5,225,580 | 0.2% | 86.7% |
| LOAD_ATTR LOAD_FAST | 4,852,420 | 0.2% | 86.9% |
| CALL RESUME_CHECK | 4,851,840 | 0.2% | 87.1% |
| RETURN_VALUE END_SEND | 4,851,260 | 0.2% | 87.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 4,833,820 | 0.2% | 87.6% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 4,554,360 | 0.2% | 87.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 45,510,580 | 87.8% |
| POP_TOP | 4,478,960 | 8.6% |
| RETURN_GENERATOR | 1,492,960 | 2.9% |
| COPY_FREE_VARS | 372,480 | 0.7% |
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
| RETURN_CONST | 746,460 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 746,460 | 100.0% |


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
| RETURN_CONST | 28,737,900 | 55.4% |
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
| STORE_ATTR_INSTANCE_VALUE | 746,460 | 49.9% |
| RESUME_CHECK | 375,040 | 25.1% |
| STORE_FAST | 374,300 | 25.0% |
| POP_TOP | 400 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,496,000 | 100.0% |
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
| CALL_METHOD_DESCRIPTOR_O | 27,992,880 | 30.4% |
| RETURN_CONST | 26,872,680 | 29.2% |
| CALL_FUNCTION_EX | 10,449,160 | 11.3% |
| END_SEND | 5,970,200 | 6.5% |
| SEND_GEN | 5,970,060 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,936,580 | 43.3% |
| RETURN_CONST | 14,554,940 | 15.8% |
| LOAD_CONST | 11,570,360 | 12.6% |
| RESUME_CHECK | 10,449,000 | 11.3% |
| ENTER_EXECUTOR | 10,448,660 | 11.3% |


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
| LOAD_ATTR_MODULE | 24,256,020 | 71.3% |
| LOAD_FAST | 9,033,820 | 26.5% |
| LOAD_ATTR | 747,640 | 2.2% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,928,200 | 43.9% |
| LOAD_FAST | 7,912,220 | 23.2% |
| CALL | 6,345,520 | 18.6% |
| LOAD_CONST | 3,732,720 | 11.0% |
| CALL_ALLOC_AND_ENTER_INIT | 746,440 | 2.2% |


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
| LOAD_FAST | 37,891,380 | 54.9% |
| LOAD_ATTR_INSTANCE_VALUE | 16,419,540 | 23.8% |
| COMPARE_OP_FLOAT | 4,458,700 | 6.5% |
| RETURN_VALUE | 3,732,960 | 5.4% |
| BINARY_OP_ADD_INT | 3,732,460 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 20,505,680 | 29.7% |
| STORE_FAST | 19,035,220 | 27.6% |
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
| POP_JUMP_IF_FALSE | 6,719,500 | 60.0% |
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
| STORE_ATTR_INSTANCE_VALUE | 746,680 | 49.9% |
| LOAD_ATTR_SLOT | 374,400 | 25.0% |
| LOAD_FAST | 372,300 | 24.9% |
| STORE_FAST | 1,840 | 0.1% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,493,440 | 99.9% |
| STORE_FAST | 1,840 | 0.1% |


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
| LOAD_FAST_LOAD_FAST | 10,449,200 | 28.8% |
| LOAD_ATTR | 8,959,720 | 24.7% |
| PUSH_NULL | 6,345,520 | 17.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,120 | 12.4% |
| RETURN_GENERATOR | 4,478,920 | 12.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,152,320 | 55.6% |
| POP_TOP | 5,598,460 | 15.5% |
| RESUME_CHECK | 4,851,840 | 13.4% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,100 | 12.4% |
| LOAD_FAST | 747,200 | 2.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 10,074,580 | 93.1% |
| CALL_INTRINSIC_1 | 374,420 | 3.5% |
| BUILD_MAP | 372,300 | 3.4% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

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
| LIST_EXTEND | 746,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 374,420 | 50.1% |
| LOAD_CONST | 372,300 | 49.9% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,076,780 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 44.4% |
| RESUME_CHECK | 4,478,940 | 44.4% |
| RETURN_VALUE | 1,118,780 | 11.1% |
| POP_TOP | 80 | 0.0% |
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
| CACHE | 372,480 | 50.0% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,448,660 | 97.9% |
| POP_JUMP_IF_FALSE | 178,780 | 1.7% |
| ENTER_EXECUTOR | 50,120 | 0.5% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 10,074,580 | 94.4% |
| LOAD_ATTR_SLOT | 372,300 | 3.5% |
| RETURN_VALUE | 178,640 | 1.7% |
| ENTER_EXECUTOR | 50,120 | 0.5% |
| FOR_ITER_RANGE | 1,800 | 0.0% |


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
| LOAD_CONST | 400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 400 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,479,220 | 99.9% |
| POP_JUMP_IF_FALSE | 2,460 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 4,479,160 | 99.9% |
| LOAD_FAST | 2,420 | 0.1% |
| ENTER_EXECUTOR | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |


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
| POP_TOP | 100 | 0.0% |
| ENTER_EXECUTOR | 80 | 0.0% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,280 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 1,880 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 374,400 | 50.1% |
| LOAD_FAST | 372,300 | 49.9% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 746,720 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,731,080 | 94.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,493,560 | 4.4% |
| LOAD_ATTR_SLOT | 374,520 | 1.1% |
| LOAD_ATTR | 12,040 | 0.0% |
| LOAD_GLOBAL_MODULE | 980 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,500 | 30.0% |
| CALL | 8,959,720 | 26.7% |
| LOAD_FAST | 4,852,420 | 14.4% |
| TO_BOOL_NONE | 4,478,920 | 13.3% |
| STORE_FAST | 3,732,640 | 11.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 21,642,900 | 21.4% |
| LOAD_FAST | 17,916,300 | 17.7% |
| LOAD_FAST_LOAD_FAST | 12,690,400 | 12.5% |
| POP_TOP | 11,570,360 | 11.4% |
| POP_JUMP_IF_FALSE | 10,827,180 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,797,660 | 41.3% |
| COMPARE_OP_INT | 11,946,040 | 11.8% |
| STORE_FAST | 11,204,760 | 11.1% |
| CALL_KW | 10,076,780 | 10.0% |
| SEND_GEN | 5,969,960 | 5.9% |


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
| POP_JUMP_IF_FALSE | 90,204,060 | 19.6% |
| RESUME_CHECK | 89,570,100 | 19.5% |
| STORE_FAST | 58,986,240 | 12.8% |
| LOAD_CONST | 41,797,660 | 9.1% |
| POP_TOP | 39,936,580 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 125,431,920 | 27.3% |
| LOAD_ATTR_SLOT | 43,623,900 | 9.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 42,922,700 | 9.3% |
| RETURN_VALUE | 37,891,380 | 8.2% |
| STORE_ATTR_SLOT | 33,209,460 | 7.2% |


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
| STORE_ATTR_SLOT | 31,347,180 | 29.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 18,288,000 | 16.9% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 14.2% |
| PUSH_NULL | 14,928,200 | 13.8% |
| POP_JUMP_IF_NOT_NONE | 10,076,700 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 42,168,420 | 39.1% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 14.2% |
| LOAD_CONST | 12,690,400 | 11.8% |
| LOAD_FAST | 10,449,480 | 9.7% |
| CALL | 10,449,200 | 9.7% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 600 | 13.0% |
| RESUME_CHECK | 580 | 12.6% |
| POP_TOP | 500 | 10.8% |
| LOAD_FAST | 500 | 10.8% |
| POP_JUMP_IF_FALSE | 460 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,580 | 34.2% |
| LOAD_ATTR | 960 | 20.8% |
| LOAD_GLOBAL_BUILTIN | 660 | 14.3% |
| LOAD_FAST | 400 | 8.7% |
| CALL | 300 | 6.5% |


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
| TO_BOOL_BOOL | 65,294,220 | 52.8% |
| TO_BOOL_NONE | 25,751,540 | 20.8% |
| COMPARE_OP_INT | 20,234,860 | 16.4% |
| TO_BOOL | 6,719,500 | 5.4% |
| TO_BOOL_LIST | 5,229,600 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 90,204,060 | 73.0% |
| RETURN_CONST | 16,047,360 | 13.0% |
| LOAD_CONST | 10,827,180 | 8.8% |
| LOAD_FAST_LOAD_FAST | 4,104,880 | 3.3% |
| LOAD_GLOBAL_MODULE | 2,236,120 | 1.8% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,211,840 | 61.1% |
| LOAD_ATTR_INSTANCE_VALUE | 5,225,580 | 38.9% |
| CALL | 160 | 0.0% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,690,400 | 94.4% |
| LOAD_CONST | 746,480 | 5.6% |
| RETURN_CONST | 480 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |


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
| INTERPRETER_EXIT | 28,737,900 | 50.0% |
| POP_TOP | 26,872,680 | 46.8% |
| END_SEND | 1,118,940 | 1.9% |
| EXIT_INIT_CHECK | 746,460 | 1.3% |
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
| CALL | 20,152,320 | 23.0% |
| RETURN_VALUE | 19,035,220 | 21.8% |
| CALL_BUILTIN_O | 15,752,240 | 18.0% |
| LOAD_CONST | 11,204,760 | 12.8% |
| FOR_ITER_RANGE | 4,480,960 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,986,240 | 67.5% |
| RETURN_CONST | 10,450,840 | 12.0% |
| LOAD_FAST_LOAD_FAST | 8,659,540 | 9.9% |
| JUMP_FORWARD | 4,482,960 | 5.1% |
| LOAD_GLOBAL_MODULE | 3,732,640 | 4.3% |


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
| LOAD_CONST | 560 | 93.3% |
| BINARY_SUBSCR | 40 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 460 | 76.7% |
| LOAD_ATTR_SLOT | 120 | 20.0% |
| LOAD_ATTR | 20 | 3.3% |


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
| PUSH_NULL | 746,440 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 746,460 | 100.0% |


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
| LOAD_FAST | 16,123,980 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.0% |
| CALL | 180 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 15,752,240 | 97.7% |
| TO_BOOL_BOOL | 372,260 | 2.3% |
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
| LOAD_ATTR | 10,076,500 | 73.0% |
| LOAD_ATTR_METHOD_NO_DICT | 3,734,960 | 27.0% |
| CALL | 400 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 10,076,460 | 73.0% |
| STORE_FAST | 3,734,560 | 27.0% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |
| CALL | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,513,700 | 84.0% |
| CALL | 4,479,100 | 16.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 27,992,880 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 31,349,480 | 60.9% |
| LOAD_FAST | 14,186,120 | 27.5% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 8.7% |
| LOAD_ATTR_METHOD_NO_DICT | 746,760 | 1.4% |
| LOAD_SUPER_ATTR_METHOD | 372,460 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 42,551,620 | 82.6% |
| RETURN_GENERATOR | 8,583,660 | 16.7% |
| COPY_FREE_VARS | 372,920 | 0.7% |


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
| LOAD_ATTR_SLOT | 4,458,680 | 100.0% |
| LOAD_FAST | 440 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,458,700 | 100.0% |
| POP_JUMP_IF_FALSE | 600 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,946,040 | 59.0% |
| LOAD_FAST_LOAD_FAST | 4,554,360 | 22.5% |
| LOAD_GLOBAL_MODULE | 3,734,240 | 18.5% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20,234,860 | 100.0% |


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
| JUMP_BACKWARD | 4,479,160 | 85.7% |
| GET_ITER | 748,280 | 14.3% |
| ENTER_EXECUTOR | 1,800 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,480,960 | 85.7% |
| LOAD_CONST | 748,320 | 14.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 20 | 50.0% |
| ENTER_EXECUTOR | 20 | 50.0% |

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
| LOAD_FAST | 125,431,920 | 96.6% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 3.4% |
| LOAD_ATTR | 1,980 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 40,682,820 | 31.3% |
| LOAD_ATTR_METHOD_NO_DICT | 31,359,140 | 24.1% |
| RETURN_VALUE | 16,419,540 | 12.6% |
| TO_BOOL | 11,199,400 | 8.6% |
| POP_JUMP_IF_NOT_NONE | 6,718,340 | 5.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 31,359,140 | 87.5% |
| LOAD_FAST | 4,479,440 | 12.5% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,875,940 | 75.0% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 12.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,734,960 | 10.4% |
| CALL_PY_EXACT_ARGS | 746,760 | 2.1% |
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
| LOAD_FAST_LOAD_FAST | 18,288,000 | 29.0% |
| LOAD_FAST | 13,439,320 | 21.3% |
| CALL | 700 | 0.0% |
| LOAD_CONST | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 24,627,880 | 100.0% |
| LOAD_ATTR | 980 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 24,256,020 | 98.5% |
| LOAD_FAST_LOAD_FAST | 372,280 | 1.5% |
| LOAD_ATTR | 200 | 0.0% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_ATTR_SLOT | 80 | 0.0% |


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
| LOAD_FAST | 43,623,900 | 99.1% |
| ENTER_EXECUTOR | 372,300 | 0.8% |
| LOAD_ATTR_SLOT | 12,880 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 21,270,100 | 48.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 25.4% |
| LOAD_FAST | 4,459,160 | 10.1% |
| COMPARE_OP_FLOAT | 4,458,680 | 10.1% |
| TO_BOOL_BOOL | 1,491,360 | 3.4% |


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
| RESUME_CHECK | 19,407,260 | 39.1% |
| POP_JUMP_IF_NOT_NONE | 9,330,500 | 18.8% |
| LOAD_FAST | 8,565,420 | 17.3% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 9.0% |
| STORE_FAST | 3,732,640 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 24,627,880 | 49.6% |
| LOAD_FAST | 11,197,900 | 22.6% |
| LOAD_FAST_LOAD_FAST | 4,479,200 | 9.0% |
| CALL_ISINSTANCE | 4,458,720 | 9.0% |
| COMPARE_OP_INT | 3,734,240 | 7.5% |


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
| CACHE | 45,510,580 | 38.4% |
| CALL_PY_EXACT_ARGS | 42,551,620 | 35.9% |
| POP_TOP | 10,449,000 | 8.8% |
| CALL | 4,851,840 | 4.1% |
| CALL_KW | 4,478,940 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,570,100 | 75.5% |
| LOAD_GLOBAL_MODULE | 19,407,260 | 16.4% |
| LOAD_GLOBAL_BUILTIN | 4,833,820 | 4.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,982,160 | 2.5% |
| LOAD_CONST | 1,493,380 | 1.3% |


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
| LOAD_FAST_LOAD_FAST | 42,168,420 | 55.9% |
| LOAD_FAST | 33,209,460 | 44.0% |
| STORE_ATTR_SLOT | 88,480 | 0.1% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 31,347,180 | 41.5% |
| LOAD_CONST | 21,642,900 | 28.7% |
| LOAD_FAST | 11,194,300 | 14.8% |
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
| LOAD_ATTR_INSTANCE_VALUE | 40,682,820 | 57.1% |
| RETURN_VALUE | 10,821,860 | 15.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,076,460 | 14.1% |
| CALL_ISINSTANCE | 4,459,140 | 6.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 3,359,540 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 65,294,220 | 91.6% |
| POP_JUMP_IF_TRUE | 5,970,560 | 8.4% |
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
| LOAD_ATTR_INSTANCE_VALUE | 5,229,500 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,229,600 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 21,270,100 | 82.6% |
| LOAD_ATTR | 4,478,920 | 17.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,400 | 0.0% |
| TO_BOOL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 25,751,540 | 100.0% |
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
|     deferred | 36,952,740 | 19.4% |
|          hit | 153,691,180 | 80.6% |
|         miss | 761,180 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,460 | 58.9% |
| Failure | 12,160 | 41.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 3,280 | 27.0% |
| no dict | 2,960 | 24.3% |
| code complex parameters | 1,620 | 13.3% |
| cfunc noargs | 1,380 | 11.3% |
| class no vectorcall | 1,340 | 11.0% |
| other | 1,280 | 10.5% |
| class mutable | 80 | 0.7% |
| metaclass | 60 | 0.5% |
| wrong number arguments | 40 | 0.3% |
| cfunc varargs | 40 | 0.3% |
| operator wrapper | 40 | 0.3% |
| cmethod | 20 | 0.2% |
| cfunc varargs keywords | 20 | 0.2% |


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
|          hit | 5,233,020 | 100.0% |

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
|     deferred | 34,272,640 | 8.3% |
|          hit | 380,725,360 | 91.7% |
|         miss | 688,080 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 18,300 | 62.1% |
| Failure | 11,160 | 37.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 6,560 | 58.8% |
| method | 3,080 | 27.6% |
| class attr descriptor | 1,280 | 11.5% |
| not managed dict | 140 | 1.3% |
| metaclass attribute | 60 | 0.5% |
| class attr simple | 40 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,460 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 56,325,500 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,240 | 100.0% |
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
|     deferred | 4,607,380 | 5.2% |
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
|     deferred | 11,201,980 | 8.4% |
|          hit | 122,767,700 | 91.6% |
|         miss | 1,480 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,400 | 26.9% |
| Failure | 3,800 | 73.1% |

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
| Basic | 1,140,612,900 | 50.7% |
| Not specialized | 261,763,680 | 11.6% |
| Specialized hits | 839,728,687 | 37.3% |
| Specialized misses | 6,175,653 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 36,952,740 | 41.2% |
| LOAD_ATTR | 34,272,640 | 38.2% |
| TO_BOOL | 11,201,980 | 12.5% |
| STORE_ATTR | 4,607,380 | 5.1% |
| SEND | 2,237,700 | 2.5% |
| COMPARE_OP | 372,800 | 0.4% |
| LOAD_GLOBAL | 2,460 | 0.0% |
| BINARY_OP | 820 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 4,693,880 | 75.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 760,800 | 12.3% |
| LOAD_ATTR_SLOT | 684,600 | 11.0% |
| RESUME | 30,953 | 0.5% |
| RESUME_CHECK | 30,953 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 3,480 | 0.1% |
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
| Calls to PyEval_EvalDefault | 51,855,320 | 37.3% |
| Calls to Python functions inlined | 87,333,040 | 62.7% |
| Calls via PyEval_EvalFrame (total) | 51,855,320 | 37.3% |
| Calls via PyEval_EvalFrame (vector) | 46,257,580 | 33.2% |
| Calls via PyEval_EvalFrame (generator) | 5,597,740 | 4.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 46,257,580 | 33.2% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 4,458,720 | 3.2% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.2% |
| Calls via PyEval_EvalFrame (method) | 20,153,400 | 14.5% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 126,503,340 | 90.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 56,534,707 | 34.8% |
| Frees to freelist | 56,895,604 |  |
| Allocations | 105,707,379 | 65.2% |
| Allocations to 512 bytes | 104,898,858 | 64.7% |
| Allocations to 4 kbytes | 808,389 | 0.5% |
| Allocations over 4 kbytes | 132 | 0.0% |
| Frees | 105,628,933 |  |
| New values | 440 |  |
| Interpreter increfs | 1,141,154,320 | 70.4% |
| Interpreter decrefs | 1,221,355,360 | 69.3% |
| Increfs | 478,814,439 | 29.6% |
| Decrefs | 540,658,393 | 30.7% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 69,088,542 |  |
| Method cache misses | 138,378 |  |
| Method cache collisions | 138,135 |  |
| Method cache dunder hits | 16,402,156 |  |
| Method cache dunder misses | 424 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 55,362 | 2,040 | 378,586,904 |
| 1 | 5,036 | 0 | 393,653,028 |
| 2 | 451 | 0 | 986,786,210 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 2,400 |  |
| Traces created | 2,400 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 20 | 0.8% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 2,300 | 95.8% |
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
| <= 32 | 60 | 2.5% |
| <= 64 | 2,300 | 95.8% |
| <= 128 | 40 | 1.7% |


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
| <= 16 | 20 | 0.8% |
| <= 32 | 0 | 0.0% |
| <= 64 | 40 | 1.7% |


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
| CALL_FUNCTION_EX | 20 |


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
