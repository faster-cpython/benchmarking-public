
# Pystats results

- benchmark: async_tree_memoization
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 454,549,560 | 18.6% | 18.6% |  |
| POP_JUMP_IF_FALSE | 139,280,340 | 5.7% | 24.3% |  |
| RESUME_CHECK | 126,127,440 | 5.2% | 29.5% | 0.0% |
| LOAD_FAST_LOAD_FAST | 114,650,860 | 4.7% | 34.2% |  |
| LOAD_CONST | 111,603,000 | 4.6% | 38.8% |  |
| STORE_FAST | 107,593,360 | 4.4% | 43.2% |  |
| LOAD_ATTR_INSTANCE_VALUE | 83,631,900 | 3.4% | 46.6% |  |
| TO_BOOL_BOOL | 79,476,440 | 3.3% | 49.9% | 0.0% |
| POP_TOP | 77,255,560 | 3.2% | 53.0% |  |
| STORE_ATTR_SLOT | 75,466,700 | 3.1% | 56.1% | 6.2% |
| RETURN_VALUE | 72,759,620 | 3.0% | 59.1% |  |
| LOAD_GLOBAL_MODULE | 63,802,560 | 2.6% | 61.7% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,077,820 | 2.6% | 64.3% |  |
| RETURN_CONST | 61,208,460 | 2.5% | 66.8% |  |
| CALL_PY_EXACT_ARGS | 60,465,960 | 2.5% | 69.3% |  |
| INTERPRETER_EXIT | 51,108,820 | 2.1% | 71.4% |  |
| LOAD_ATTR_SLOT | 48,488,640 | 2.0% | 73.4% | 1.4% |
| PUSH_NULL | 42,995,320 | 1.8% | 75.1% |  |
| CALL | 41,448,080 | 1.7% | 76.8% |  |
| LOAD_DEREF | 41,055,740 | 1.7% | 78.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 35,839,340 | 1.5% | 80.0% | 0.0% |
| LOAD_ATTR | 34,360,500 | 1.4% | 81.4% |  |
| POP_JUMP_IF_NOT_NONE | 33,591,000 | 1.4% | 82.7% |  |
| LOAD_ATTR_MODULE | 32,840,260 | 1.3% | 84.1% |  |
| TO_BOOL_NONE | 25,751,560 | 1.1% | 85.1% | 0.0% |
| COMPARE_OP_INT | 24,713,720 | 1.0% | 86.2% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 22,856,100 | 0.9% | 87.1% | 20.0% |
| ENTER_EXECUTOR | 19,634,740 | 0.8% | 87.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 19,035,180 | 0.8% | 88.7% | 0.0% |
| BINARY_OP_ADD_INT | 16,422,700 | 0.7% | 89.4% |  |
| CALL_BUILTIN_O | 16,124,640 | 0.7% | 90.0% |  |
| LOAD_GLOBAL_BUILTIN | 15,664,140 | 0.6% | 90.7% | 0.0% |
| POP_JUMP_IF_NONE | 13,437,680 | 0.6% | 91.2% |  |
| STORE_DEREF | 12,690,160 | 0.5% | 91.7% |  |
| CALL_FUNCTION_EX | 11,568,020 | 0.5% | 92.2% |  |
| CALL_KW | 10,823,260 | 0.4% | 92.6% |  |
| POP_JUMP_IF_TRUE | 10,453,420 | 0.4% | 93.1% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.4% | 93.4% |  |
| RETURN_GENERATOR | 8,956,200 | 0.4% | 93.8% |  |
| BINARY_OP_SUBTRACT_INT | 8,211,380 | 0.3% | 94.1% |  |
| NOP | 5,975,440 | 0.2% | 94.4% |  |
| COPY_FREE_VARS | 5,971,020 | 0.2% | 94.6% |  |
| END_SEND | 5,596,020 | 0.2% | 94.9% |  |
| GET_AWAITABLE | 5,596,020 | 0.2% | 95.1% |  |
| SEND_GEN | 5,594,200 | 0.2% | 95.3% |  |
| TO_BOOL | 5,231,700 | 0.2% | 95.5% |  |
| STORE_ATTR | 5,230,120 | 0.2% | 95.7% |  |
| FOR_ITER_RANGE | 5,229,280 | 0.2% | 96.0% |  |
| CONTAINS_OP | 5,225,800 | 0.2% | 96.2% |  |
| CALL_BUILTIN_FAST | 4,851,400 | 0.2% | 96.4% |  |
| JUMP_FORWARD | 4,483,220 | 0.2% | 96.6% |  |
| TO_BOOL_LIST | 4,483,140 | 0.2% | 96.7% |  |
| JUMP_BACKWARD | 4,482,360 | 0.2% | 96.9% |  |
| COPY | 4,481,460 | 0.2% | 97.1% |  |
| STORE_SUBSCR_DICT | 4,480,700 | 0.2% | 97.3% |  |
| IS_OP | 4,479,280 | 0.2% | 97.5% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 97.7% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 97.8% |  |
| COMPARE_OP_FLOAT | 4,459,300 | 0.2% | 98.0% |  |
| CALL_ISINSTANCE | 4,459,220 | 0.2% | 98.2% |  |
| CALL_PY_WITH_DEFAULTS | 4,105,120 | 0.2% | 98.4% |  |
| BUILD_LIST | 3,734,720 | 0.2% | 98.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 3,732,520 | 0.2% | 98.7% |  |
| MAKE_CELL | 3,732,480 | 0.2% | 98.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 3,362,160 | 0.1% | 99.0% |  |
| GET_ITER | 2,991,700 | 0.1% | 99.1% |  |
| FOR_ITER_LIST | 2,243,380 | 0.1% | 99.2% |  |
| SWAP | 2,239,780 | 0.1% | 99.3% |  |
| SEND | 2,238,700 | 0.1% | 99.4% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 2,235,840 | 0.1% | 99.5% |  |
| YIELD_VALUE | 2,235,840 | 0.1% | 99.6% |  |
| FOR_ITER_TUPLE | 1,493,260 | 0.1% | 99.6% |  |
| LOAD_SUPER_ATTR_METHOD | 1,491,640 | 0.1% | 99.7% |  |
| BUILD_MAP | 1,119,180 | 0.0% | 99.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 749,000 | 0.0% | 99.8% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.8% |  |
| CALL_INTRINSIC_1 | 746,720 | 0.0% | 99.9% |  |
| LIST_EXTEND | 746,720 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 374,100 | 0.0% | 100.0% |  |
| COMPARE_OP | 373,440 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,700 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| RESUME | 1,980 | 0.0% | 100.0% | 2,450.7% |
| BINARY_OP | 1,240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 600 | 0.0% | 100.0% |  |
| FOR_ITER | 560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 500 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 140 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 120 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |
| BEFORE_WITH | 40 | 0.0% | 100.0% |  |
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
| RESUME_CHECK LOAD_FAST | 81,358,840 | 3.3% | 3.3% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 78,404,600 | 3.2% | 6.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 78,260,660 | 3.2% | 9.8% |
| STORE_FAST LOAD_FAST | 73,169,640 | 3.0% | 12.7% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 69,773,400 | 2.9% | 15.6% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 51,509,380 | 2.1% | 17.7% |
| LOAD_FAST LOAD_ATTR_SLOT | 48,102,780 | 2.0% | 19.7% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 42,922,740 | 1.8% | 21.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 42,168,420 | 1.7% | 23.2% |
| CACHE RESUME_CHECK | 41,031,720 | 1.7% | 24.9% |
| LOAD_CONST LOAD_FAST | 38,811,740 | 1.6% | 26.4% |
| LOAD_FAST LOAD_ATTR | 33,970,160 | 1.4% | 27.8% |
| LOAD_FAST STORE_ATTR_SLOT | 33,209,460 | 1.4% | 29.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 32,839,160 | 1.3% | 30.5% |
| LOAD_FAST RETURN_VALUE | 32,666,020 | 1.3% | 31.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 32,467,300 | 1.3% | 33.2% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 31,347,180 | 1.3% | 34.5% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 30,603,040 | 1.3% | 35.7% |
| RETURN_CONST INTERPRETER_EXIT | 29,484,360 | 1.2% | 37.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 29,111,680 | 1.2% | 38.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 26,875,940 | 1.1% | 39.3% |
| RETURN_CONST POP_TOP | 26,872,680 | 1.1% | 40.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 26,499,860 | 1.1% | 41.4% |
| POP_TOP LOAD_FAST | 25,753,460 | 1.1% | 42.5% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 25,751,540 | 1.1% | 43.5% |
| CALL STORE_FAST | 25,377,700 | 1.0% | 44.6% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 24,713,720 | 1.0% | 45.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 23,890,320 | 1.0% | 46.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 23,512,160 | 1.0% | 47.5% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 23,139,660 | 0.9% | 48.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 22,401,460 | 0.9% | 49.4% |
| STORE_ATTR_SLOT LOAD_CONST | 21,642,900 | 0.9% | 50.3% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 21,270,100 | 0.9% | 51.2% |
| RETURN_VALUE INTERPRETER_EXIT | 20,505,680 | 0.8% | 52.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 19,784,940 | 0.8% | 52.8% |
| RETURN_VALUE STORE_FAST | 19,781,700 | 0.8% | 53.6% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 19,035,160 | 0.8% | 54.4% |
| LOAD_FAST LOAD_CONST | 18,662,780 | 0.8% | 55.2% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 16,419,540 | 0.7% | 55.8% |
| LOAD_FAST CALL_BUILTIN_O | 16,123,980 | 0.7% | 56.5% |
| PUSH_NULL LOAD_FAST | 16,123,500 | 0.7% | 57.2% |
| CALL_BUILTIN_O STORE_FAST | 15,752,240 | 0.6% | 57.8% |
| LOAD_CONST STORE_FAST | 15,683,640 | 0.6% | 58.5% |
| POP_TOP RETURN_CONST | 15,301,420 | 0.6% | 59.1% |
| RETURN_VALUE TO_BOOL_BOOL | 15,300,740 | 0.6% | 59.7% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 15,300,660 | 0.6% | 60.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,928,360 | 0.6% | 60.9% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,928,200 | 0.6% | 61.6% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,556,020 | 0.6% | 62.2% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 14,555,620 | 0.6% | 62.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 14,555,580 | 0.6% | 63.3% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 14,185,800 | 0.6% | 63.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 13,809,140 | 0.6% | 64.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,809,100 | 0.6% | 65.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 13,791,580 | 0.6% | 65.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 13,425,040 | 0.5% | 66.2% |
| LOAD_CONST BINARY_OP_ADD_INT | 12,690,160 | 0.5% | 66.7% |
| LOAD_CONST COMPARE_OP_INT | 11,946,040 | 0.5% | 67.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 11,197,900 | 0.5% | 67.6% |
| STORE_ATTR_SLOT LOAD_FAST | 11,194,300 | 0.5% | 68.1% |
| STORE_ATTR_SLOT RETURN_CONST | 11,193,840 | 0.5% | 68.6% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 0.5% | 69.0% |
| POP_TOP LOAD_CONST | 10,823,880 | 0.4% | 69.5% |
| LOAD_FAST CALL | 10,451,200 | 0.4% | 69.9% |
| STORE_FAST RETURN_CONST | 10,450,840 | 0.4% | 70.3% |
| LOAD_FAST_LOAD_FAST CALL | 10,449,200 | 0.4% | 70.7% |
| CALL_FUNCTION_EX POP_TOP | 10,449,160 | 0.4% | 71.2% |
| POP_TOP ENTER_EXECUTOR | 10,448,660 | 0.4% | 71.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 10,152,780 | 0.4% | 72.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 10,076,960 | 0.4% | 72.4% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 10,076,940 | 0.4% | 72.8% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 10,074,580 | 0.4% | 73.3% |
| LOAD_FAST PUSH_NULL | 9,780,300 | 0.4% | 73.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 9,702,980 | 0.4% | 74.1% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.4% | 74.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 8,958,280 | 0.4% | 74.8% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 8,958,280 | 0.4% | 75.2% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.4% | 75.5% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.4% | 75.9% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.4% | 76.3% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.4% | 76.6% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 8,957,080 | 0.4% | 77.0% |
| POP_TOP RESUME_CHECK | 8,956,080 | 0.4% | 77.4% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 8,583,660 | 0.4% | 77.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 8,565,420 | 0.4% | 78.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 8,213,420 | 0.3% | 78.4% |
| RETURN_VALUE RETURN_VALUE | 8,211,840 | 0.3% | 78.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 8,211,520 | 0.3% | 79.1% |
| PUSH_NULL CALL | 7,091,960 | 0.3% | 79.4% |
| LOAD_CONST CALL_KW | 7,091,140 | 0.3% | 79.6% |
| NOP LOAD_FAST | 5,974,880 | 0.2% | 79.9% |
| COPY_FREE_VARS RESUME_CHECK | 5,970,580 | 0.2% | 80.1% |
| CALL POP_TOP | 5,598,460 | 0.2% | 80.4% |
| CACHE COPY_FREE_VARS | 5,597,840 | 0.2% | 80.6% |
| GET_AWAITABLE LOAD_CONST | 5,596,020 | 0.2% | 80.8% |
| LOAD_ATTR CALL | 5,227,620 | 0.2% | 81.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 5,225,940 | 0.2% | 81.3% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 5,225,800 | 0.2% | 81.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 5,225,580 | 0.2% | 81.7% |
| POP_JUMP_IF_FALSE LOAD_DEREF | 5,225,360 | 0.2% | 81.9% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 41,031,720 | 80.3% |
| COPY_FREE_VARS | 5,597,840 | 11.0% |
| POP_TOP | 4,478,960 | 8.8% |
| RESUME | 300 | 0.0% |


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
| RETURN_VALUE | 4,104,780 | 73.4% |
| SEND | 1,118,780 | 20.0% |
| RETURN_CONST | 372,460 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,223,720 | 93.3% |
| LOAD_FAST | 372,300 | 6.7% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,496,660 | 50.0% |
| CALL_BUILTIN_CLASS | 748,340 | 25.0% |
| LOAD_DEREF | 746,480 | 25.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 160 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,496,540 | 50.0% |
| LOAD_FAST_AND_CLEAR | 746,480 | 25.0% |
| FOR_ITER_TUPLE | 746,480 | 25.0% |
| FOR_ITER_RANGE | 1,820 | 0.1% |
| FOR_ITER | 380 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 29,484,360 | 57.7% |
| RETURN_VALUE | 20,505,680 | 40.1% |
| YIELD_VALUE | 1,118,780 | 2.2% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 746,720 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 62.5% |
| RESUME_CHECK | 1,121,520 | 18.8% |
| STORE_FAST | 1,120,780 | 18.8% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,974,880 | 100.0% |
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
| RETURN_CONST | 26,872,680 | 34.8% |
| CALL_METHOD_DESCRIPTOR_O | 19,035,160 | 24.6% |
| CALL_FUNCTION_EX | 10,449,160 | 13.5% |
| CALL | 5,598,460 | 7.2% |
| END_SEND | 5,223,720 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,753,460 | 33.3% |
| RETURN_CONST | 15,301,420 | 19.8% |
| LOAD_CONST | 10,823,880 | 14.0% |
| ENTER_EXECUTOR | 10,448,660 | 13.5% |
| RESUME_CHECK | 8,956,080 | 11.6% |


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
| LOAD_ATTR_MODULE | 32,467,300 | 75.5% |
| LOAD_FAST | 9,780,300 | 22.7% |
| LOAD_ATTR | 747,640 | 1.7% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,123,500 | 37.5% |
| LOAD_FAST_LOAD_FAST | 14,928,200 | 34.7% |
| CALL | 7,091,960 | 16.5% |
| LOAD_CONST | 3,732,720 | 8.7% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 1.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 8,583,660 | 95.8% |
| CALL_PY_WITH_DEFAULTS | 372,280 | 4.2% |
| CALL | 120 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 4,478,880 | 50.0% |
| GET_AWAITABLE | 4,477,240 | 50.0% |
| CALL | 40 | 0.0% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,666,020 | 44.9% |
| LOAD_ATTR_INSTANCE_VALUE | 16,419,540 | 22.6% |
| RETURN_VALUE | 8,211,840 | 11.3% |
| POP_JUMP_IF_FALSE | 4,479,040 | 6.2% |
| COMPARE_OP_FLOAT | 4,458,700 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 20,505,680 | 28.2% |
| STORE_FAST | 19,781,700 | 27.2% |
| TO_BOOL_BOOL | 15,300,740 | 21.0% |
| RETURN_VALUE | 8,211,840 | 11.3% |
| END_SEND | 4,104,780 | 5.6% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100 | 71.4% |
| LOAD_ATTR | 40 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 42.9% |
| STORE_SUBSCR_DICT | 60 | 42.9% |
| LOAD_CONST | 20 | 14.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,481,060 | 85.7% |
| LOAD_FAST | 746,640 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| LOAD_ATTR | 580 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,480,020 | 85.6% |
| POP_JUMP_IF_TRUE | 748,560 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| TO_BOOL_BOOL | 940 | 0.0% |
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
| LOAD_CONST | 240 | 19.4% |
| LOAD_FAST | 240 | 19.4% |
| LOAD_GLOBAL_MODULE | 180 | 14.5% |
| UNARY_INVERT | 160 | 12.9% |
| BINARY_OP | 160 | 12.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 220 | 17.7% |
| BINARY_OP | 160 | 12.9% |
| COPY | 160 | 12.9% |
| LOAD_GLOBAL_MODULE | 120 | 9.7% |
| BINARY_OP_ADD_INT | 100 | 8.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 748,320 | 20.0% |
| POP_JUMP_IF_FALSE | 746,480 | 20.0% |
| STORE_DEREF | 746,480 | 20.0% |
| SWAP | 746,480 | 20.0% |
| LOAD_ATTR_SLOT | 374,400 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,494,800 | 40.0% |
| LOAD_FAST | 746,960 | 20.0% |
| STORE_DEREF | 746,480 | 20.0% |
| SWAP | 746,480 | 20.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 66.7% |
| LOAD_FAST | 372,300 | 33.3% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 66.7% |
| CALL_FUNCTION_EX | 372,300 | 33.3% |
| LOAD_FAST | 400 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,720 | 99.9% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 746,720 | 99.9% |
| CALL | 160 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |
| BUILD_MAP | 80 | 0.0% |
| CALL_ISINSTANCE | 40 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,451,200 | 25.2% |
| LOAD_FAST_LOAD_FAST | 10,449,200 | 25.2% |
| PUSH_NULL | 7,091,960 | 17.1% |
| LOAD_ATTR | 5,227,620 | 12.6% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,100 | 10.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,377,700 | 61.2% |
| POP_TOP | 5,598,460 | 13.5% |
| RESUME_CHECK | 4,851,860 | 11.7% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,060 | 10.8% |
| RETURN_VALUE | 1,120,920 | 2.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 10,074,580 | 87.1% |
| STORE_FAST | 746,480 | 6.5% |
| CALL_INTRINSIC_1 | 374,420 | 3.2% |
| BUILD_MAP | 372,300 | 3.2% |
| DICT_MERGE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,449,160 | 90.3% |
| MAKE_CELL | 746,480 | 6.5% |
| STORE_FAST | 372,300 | 3.2% |
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
| LOAD_CONST | 7,091,140 | 65.5% |
| ENTER_EXECUTOR | 3,732,120 | 34.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 41.4% |
| RESUME_CHECK | 4,478,940 | 41.4% |
| POP_TOP | 746,560 | 6.9% |
| STORE_DEREF | 746,480 | 6.9% |
| RETURN_VALUE | 372,300 | 3.4% |


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
| POP_JUMP_IF_FALSE | 372,780 | 99.8% |
| COMPARE_OP | 320 | 0.1% |
| COMPARE_OP_INT | 240 | 0.1% |
| COMPARE_OP_FLOAT | 60 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,478,940 | 85.7% |
| LOAD_FAST_LOAD_FAST | 746,760 | 14.3% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,225,800 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 4,479,020 | 99.9% |
| CALL_LEN | 1,820 | 0.0% |
| BINARY_OP | 160 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| UNARY_NOT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 4,479,080 | 99.9% |
| TO_BOOL_INT | 1,880 | 0.0% |
| TO_BOOL | 240 | 0.0% |
| POP_EXCEPT | 80 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 5,597,840 | 93.8% |
| CALL_PY_EXACT_ARGS | 372,920 | 6.2% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,970,580 | 100.0% |
| RESUME | 280 | 0.0% |
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
| POP_TOP | 10,448,660 | 53.2% |
| CALL_LIST_APPEND | 8,957,080 | 45.6% |
| POP_JUMP_IF_FALSE | 178,780 | 0.9% |
| ENTER_EXECUTOR | 50,120 | 0.3% |
| JUMP_BACKWARD | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 10,074,580 | 51.3% |
| CALL | 3,732,120 | 19.0% |
| CALL_KW | 3,732,120 | 19.0% |
| FOR_ITER_TUPLE | 746,460 | 3.8% |
| FOR_ITER_LIST | 746,440 | 3.8% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 380 | 67.9% |
| FOR_ITER | 80 | 14.3% |
| JUMP_BACKWARD | 80 | 14.3% |
| SWAP | 20 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 120 | 21.4% |
| LOAD_FAST | 100 | 17.9% |
| FOR_ITER_LIST | 100 | 17.9% |
| FOR_ITER | 80 | 14.3% |
| STORE_FAST | 80 | 14.3% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 4,477,240 | 80.0% |
| RETURN_VALUE | 746,480 | 13.3% |
| LOAD_FAST | 372,300 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,596,020 | 100.0% |


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
| LOAD_FAST_LOAD_FAST | 4,478,880 | 100.0% |
| LOAD_CONST | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,478,880 | 100.0% |
| RETURN_VALUE | 400 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 4,478,880 | 99.9% |
| POP_JUMP_IF_FALSE | 2,460 | 0.1% |
| CALL_LIST_APPEND | 640 | 0.0% |
| POP_TOP | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 4,479,160 | 99.9% |
| LOAD_FAST | 2,420 | 0.1% |
| FOR_ITER_LIST | 300 | 0.0% |
| FOR_ITER_TUPLE | 300 | 0.0% |
| ENTER_EXECUTOR | 100 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,235,700 | 100.0% |
| RESUME | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 1,118,820 | 50.0% |
| SEND_GEN | 1,117,020 | 50.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,478,980 | 99.9% |
| STORE_FAST | 4,080 | 0.1% |
| ENTER_EXECUTOR | 80 | 0.0% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 99.9% |
| LOAD_FAST | 2,400 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 1,880 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 4,478,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,478,880 | 100.0% |


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
| LOAD_FAST | 33,970,160 | 98.9% |
| LOAD_ATTR_SLOT | 374,520 | 1.1% |
| LOAD_ATTR | 12,280 | 0.0% |
| LOAD_GLOBAL_MODULE | 980 | 0.0% |
| LOAD_GLOBAL | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,555,620 | 42.4% |
| CALL | 5,227,620 | 15.2% |
| LOAD_FAST | 4,852,420 | 14.1% |
| STORE_FAST | 4,479,120 | 13.0% |
| TO_BOOL_NONE | 4,478,920 | 13.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 21,642,900 | 19.4% |
| POP_JUMP_IF_FALSE | 19,784,940 | 17.7% |
| LOAD_FAST | 18,662,780 | 16.7% |
| POP_TOP | 10,823,880 | 9.7% |
| LOAD_FAST_LOAD_FAST | 8,958,280 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,811,740 | 34.8% |
| STORE_FAST | 15,683,640 | 14.1% |
| BINARY_OP_ADD_INT | 12,690,160 | 11.4% |
| COMPARE_OP_INT | 11,946,040 | 10.7% |
| CALL_KW | 7,091,140 | 6.4% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 8,957,760 | 21.8% |
| POP_JUMP_IF_FALSE | 5,225,360 | 12.7% |
| RESUME_CHECK | 4,478,920 | 10.9% |
| JUMP_FORWARD | 4,478,880 | 10.9% |
| LOAD_DEREF | 4,478,880 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,957,920 | 21.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,225,280 | 12.7% |
| LOAD_DEREF | 4,478,880 | 10.9% |
| POP_JUMP_IF_NONE | 4,478,880 | 10.9% |
| COMPARE_OP_INT | 4,478,840 | 10.9% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 81,358,840 | 17.9% |
| POP_JUMP_IF_FALSE | 78,260,660 | 17.2% |
| STORE_FAST | 73,169,640 | 16.1% |
| LOAD_CONST | 38,811,740 | 8.5% |
| LOAD_ATTR_METHOD_NO_DICT | 26,875,940 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 78,404,600 | 17.2% |
| LOAD_ATTR_SLOT | 48,102,780 | 10.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 42,922,740 | 9.4% |
| LOAD_ATTR | 33,970,160 | 7.5% |
| STORE_ATTR_SLOT | 33,209,460 | 7.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 746,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 746,480 | 100.0% |


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
| STORE_ATTR_SLOT | 31,347,180 | 27.3% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 13.3% |
| PUSH_NULL | 14,928,200 | 13.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,809,140 | 12.0% |
| POP_JUMP_IF_NOT_NONE | 13,809,100 | 12.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 42,168,420 | 36.8% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 13.3% |
| LOAD_FAST | 14,928,360 | 13.0% |
| CALL | 10,449,200 | 9.1% |
| LOAD_CONST | 8,958,280 | 7.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 600 | 12.8% |
| RESUME_CHECK | 580 | 12.3% |
| POP_TOP | 500 | 10.6% |
| LOAD_FAST | 500 | 10.6% |
| POP_JUMP_IF_FALSE | 500 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,620 | 34.5% |
| LOAD_ATTR | 960 | 20.4% |
| LOAD_GLOBAL_BUILTIN | 660 | 14.0% |
| LOAD_FAST | 400 | 8.5% |
| CALL | 280 | 6.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 240 | 48.0% |
| CALL | 140 | 28.0% |
| LOAD_FAST | 80 | 16.0% |
| LOAD_FAST_LOAD_FAST | 40 | 8.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,985,920 | 80.0% |
| CALL_FUNCTION_EX | 746,480 | 20.0% |
| COPY_FREE_VARS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 2,985,920 | 80.0% |
| RESUME_CHECK | 746,520 | 20.0% |
| RESUME | 40 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 69,773,400 | 50.1% |
| TO_BOOL_NONE | 25,751,540 | 18.5% |
| COMPARE_OP_INT | 24,713,720 | 17.7% |
| CONTAINS_OP | 5,225,800 | 3.8% |
| TO_BOOL_LIST | 4,483,140 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,260,660 | 56.2% |
| RETURN_CONST | 23,512,160 | 16.9% |
| LOAD_CONST | 19,784,940 | 14.2% |
| LOAD_DEREF | 5,225,360 | 3.8% |
| RETURN_VALUE | 4,479,040 | 3.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,958,320 | 66.7% |
| LOAD_DEREF | 4,478,880 | 33.3% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 8,957,760 | 66.7% |
| LOAD_FAST | 4,479,120 | 33.3% |
| RETURN_CONST | 480 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,111,680 | 86.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,478,960 | 13.3% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,809,100 | 41.1% |
| LOAD_GLOBAL_MODULE | 10,076,940 | 30.0% |
| LOAD_FAST | 5,225,580 | 15.6% |
| NOP | 3,732,560 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 2.2% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 9,702,980 | 92.8% |
| TO_BOOL | 748,560 | 7.2% |
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
| POP_JUMP_IF_FALSE | 23,512,160 | 38.4% |
| POP_TOP | 15,301,420 | 25.0% |
| STORE_ATTR_SLOT | 11,193,840 | 18.3% |
| STORE_FAST | 10,450,840 | 17.1% |
| STORE_ATTR_INSTANCE_VALUE | 747,120 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 29,484,360 | 48.2% |
| POP_TOP | 26,872,680 | 43.9% |
| TO_BOOL_BOOL | 4,478,920 | 7.3% |
| END_SEND | 372,460 | 0.6% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,118,940 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,118,820 | 50.0% |
| SEND | 940 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 1,118,780 | 50.0% |
| YIELD_VALUE | 1,118,780 | 50.0% |
| SEND | 940 | 0.0% |
| POP_TOP | 100 | 0.0% |
| SEND_GEN | 100 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 746,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,720 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,140 | 85.7% |
| LOAD_FAST_LOAD_FAST | 746,820 | 14.3% |
| STORE_ATTR | 1,760 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 85.6% |
| LOAD_CONST | 746,860 | 14.3% |
| STORE_ATTR | 1,760 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 980 | 0.0% |
| LOAD_FAST | 540 | 0.0% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 8,957,720 | 70.6% |
| LOAD_CONST | 2,239,440 | 17.6% |
| BUILD_LIST | 746,480 | 5.9% |
| CALL_KW | 746,480 | 5.9% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 35.3% |
| LOAD_FAST_LOAD_FAST | 4,478,880 | 35.3% |
| LOAD_CONST | 1,492,960 | 11.8% |
| LOAD_FAST | 1,492,960 | 11.8% |
| BUILD_LIST | 746,480 | 5.9% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 25,377,700 | 23.6% |
| RETURN_VALUE | 19,781,700 | 18.4% |
| CALL_BUILTIN_O | 15,752,240 | 14.6% |
| LOAD_CONST | 15,683,640 | 14.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,213,420 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 73,169,640 | 68.0% |
| RETURN_CONST | 10,450,840 | 9.7% |
| LOAD_FAST_LOAD_FAST | 10,152,780 | 9.4% |
| LOAD_GLOBAL_MODULE | 8,211,520 | 7.6% |
| LOAD_CONST | 1,493,520 | 1.4% |


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
| BUILD_LIST | 746,480 | 33.3% |
| LOAD_FAST_AND_CLEAR | 746,480 | 33.3% |
| FOR_ITER_RANGE | 746,480 | 33.3% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,560 | 33.3% |
| BUILD_LIST | 746,480 | 33.3% |
| FOR_ITER_RANGE | 746,460 | 33.3% |
| POP_EXCEPT | 100 | 0.0% |
| STORE_ATTR | 80 | 0.0% |


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
| SEND | 1,118,780 | 50.0% |
| YIELD_VALUE | 1,117,060 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,118,780 | 50.0% |
| YIELD_VALUE | 1,117,060 | 50.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,140 | 57.6% |
| CACHE | 300 | 15.2% |
| COPY_FREE_VARS | 280 | 14.1% |
| POP_TOP | 120 | 6.1% |
| SEND_GEN | 80 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 940 | 47.5% |
| LOAD_GLOBAL | 600 | 30.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 140 | 7.1% |
| NOP | 100 | 5.1% |
| LOAD_CONST | 100 | 5.1% |


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
| LOAD_CONST | 12,690,160 | 77.3% |
| RETURN_VALUE | 3,732,440 | 22.7% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 8,957,720 | 54.5% |
| RETURN_VALUE | 3,732,460 | 22.7% |
| CALL_PY_WITH_DEFAULTS | 3,732,440 | 22.7% |
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

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,732,440 | 100.0% |
| PUSH_NULL | 40 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,732,460 | 100.0% |
| RETURN_GENERATOR | 60 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 746,440 | 99.7% |
| LOAD_FAST | 1,980 | 0.3% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 748,340 | 99.9% |
| LOAD_FAST | 240 | 0.0% |
| COMPARE_OP | 140 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,479,060 | 92.3% |
| LOAD_FAST | 372,260 | 7.7% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,479,020 | 92.3% |
| POP_TOP | 372,280 | 7.7% |
| TO_BOOL_BOOL | 80 | 0.0% |
| TO_BOOL | 20 | 0.0% |


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

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,957,680 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,957,080 | 100.0% |
| JUMP_BACKWARD | 640 | 0.0% |


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
| LOAD_ATTR | 14,555,620 | 63.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 19.6% |
| LOAD_ATTR_METHOD_NO_DICT | 3,734,960 | 16.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| CALL | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 14,555,580 | 63.7% |
| STORE_FAST | 8,213,420 | 35.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,556,020 | 76.5% |
| CALL | 4,479,060 | 23.5% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 19,035,160 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 30,603,040 | 50.6% |
| LOAD_FAST | 23,890,320 | 39.5% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 7.4% |
| LOAD_ATTR_METHOD_NO_DICT | 746,760 | 1.2% |
| LOAD_SUPER_ATTR_METHOD | 372,460 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 51,509,380 | 85.2% |
| RETURN_GENERATOR | 8,583,660 | 14.2% |
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
| LOAD_FAST | 4,478,920 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,478,920 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |


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
| LOAD_CONST | 11,946,040 | 48.3% |
| LOAD_FAST_LOAD_FAST | 4,554,360 | 18.4% |
| LOAD_DEREF | 4,478,840 | 18.1% |
| LOAD_GLOBAL_MODULE | 3,734,240 | 15.1% |
| COMPARE_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,713,720 | 100.0% |


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
| GET_ITER | 1,496,540 | 66.7% |
| ENTER_EXECUTOR | 746,440 | 33.3% |
| JUMP_BACKWARD | 300 | 0.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 1,492,940 | 66.5% |
| STORE_FAST | 746,740 | 33.3% |
| RETURN_CONST | 1,880 | 0.1% |
| LOAD_FAST | 1,820 | 0.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,479,160 | 85.7% |
| SWAP | 746,460 | 14.3% |
| GET_ITER | 1,820 | 0.0% |
| ENTER_EXECUTOR | 1,800 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,480,960 | 85.7% |
| SWAP | 746,480 | 14.3% |
| LOAD_CONST | 1,840 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 746,480 | 50.0% |
| ENTER_EXECUTOR | 746,460 | 50.0% |
| JUMP_BACKWARD | 300 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,760 | 50.0% |
| LOAD_GLOBAL_MODULE | 746,440 | 50.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


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
| LOAD_FAST | 78,404,600 | 93.7% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 5.4% |
| LOAD_DEREF | 746,440 | 0.9% |
| LOAD_ATTR | 1,540 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 26,499,860 | 31.7% |
| LOAD_ATTR_METHOD_NO_DICT | 22,401,460 | 26.8% |
| RETURN_VALUE | 16,419,540 | 19.6% |
| TO_BOOL_LIST | 4,483,060 | 5.4% |
| TO_BOOL | 4,481,060 | 5.4% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 22,401,460 | 62.5% |
| LOAD_FAST | 8,958,280 | 25.0% |
| LOAD_DEREF | 4,478,840 | 12.5% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

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
| LOAD_FAST | 42,922,740 | 68.0% |
| LOAD_ATTR_SLOT | 11,193,640 | 17.7% |
| LOAD_DEREF | 5,225,280 | 8.3% |
| LOAD_FAST_LOAD_FAST | 3,732,480 | 5.9% |
| LOAD_ATTR_INSTANCE_VALUE | 2,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 30,603,040 | 48.5% |
| LOAD_FAST | 14,185,800 | 22.5% |
| LOAD_FAST_LOAD_FAST | 13,809,140 | 21.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,478,840 | 7.1% |
| CALL | 700 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 32,839,160 | 100.0% |
| LOAD_ATTR | 980 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 32,467,300 | 98.9% |
| LOAD_FAST_LOAD_FAST | 372,280 | 1.1% |
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
| LOAD_FAST | 48,102,780 | 99.2% |
| ENTER_EXECUTOR | 372,300 | 0.8% |
| LOAD_ATTR_SLOT | 12,880 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 21,270,100 | 43.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 23.1% |
| LOAD_CONST | 4,479,160 | 9.2% |
| LOAD_FAST | 4,459,160 | 9.2% |
| COMPARE_OP_FLOAT | 4,458,680 | 9.2% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 13,791,580 | 88.0% |
| PUSH_NULL | 746,440 | 4.8% |
| POP_JUMP_IF_NOT_NONE | 746,440 | 4.8% |
| POP_TOP | 372,460 | 2.4% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,425,040 | 85.7% |
| LOAD_DEREF | 1,491,640 | 9.5% |
| LOAD_GLOBAL_MODULE | 746,480 | 4.8% |
| CALL_ISINSTANCE | 380 | 0.0% |
| CALL_BUILTIN_CLASS | 220 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 23,139,660 | 36.3% |
| POP_JUMP_IF_NOT_NONE | 10,076,940 | 15.8% |
| LOAD_FAST | 8,565,420 | 13.4% |
| STORE_FAST | 8,211,520 | 12.9% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 32,839,160 | 51.5% |
| LOAD_FAST | 11,197,900 | 17.6% |
| LOAD_FAST_LOAD_FAST | 5,225,940 | 8.2% |
| CONTAINS_OP | 4,478,940 | 7.0% |
| CALL_ISINSTANCE | 4,458,720 | 7.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,491,400 | 100.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,720 | 50.1% |
| CALL_PY_EXACT_ARGS | 372,460 | 25.0% |
| LOAD_FAST_LOAD_FAST | 372,340 | 25.0% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 51,509,380 | 40.8% |
| CACHE | 41,031,720 | 32.5% |
| POP_TOP | 8,956,080 | 7.1% |
| COPY_FREE_VARS | 5,970,580 | 4.7% |
| CALL | 4,851,860 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 81,358,840 | 64.5% |
| LOAD_GLOBAL_MODULE | 23,139,660 | 18.3% |
| LOAD_GLOBAL_BUILTIN | 13,791,580 | 10.9% |
| LOAD_DEREF | 4,478,920 | 3.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,235,700 | 1.8% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,477,080 | 80.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,117,020 | 20.0% |
| SEND | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,477,140 | 80.0% |
| RESUME_CHECK | 1,116,980 | 20.0% |
| RESUME | 80 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 748,420 | 99.8% |
| STORE_ATTR | 980 | 0.1% |
| LOAD_FAST_LOAD_FAST | 260 | 0.0% |
| SWAP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 747,120 | 99.7% |
| LOAD_CONST | 840 | 0.1% |
| LOAD_FAST | 760 | 0.1% |
| LOAD_GLOBAL_MODULE | 360 | 0.0% |
| BUILD_LIST | 220 | 0.0% |


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
| LOAD_FAST | 4,480,600 | 100.0% |
| STORE_SUBSCR | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,480,700 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 26,499,860 | 33.3% |
| RETURN_VALUE | 15,300,740 | 19.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,555,580 | 18.3% |
| COPY | 4,479,080 | 5.6% |
| RETURN_CONST | 4,478,920 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 69,773,400 | 87.8% |
| POP_JUMP_IF_TRUE | 9,702,980 | 12.2% |
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
| LOAD_ATTR_INSTANCE_VALUE | 4,483,060 | 100.0% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,483,140 | 100.0% |


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
|     deferred | 860 | 0.0% |
|          hit | 25,008,240 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 57.9% |
| Failure | 160 | 42.1% |

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
|     deferred | 45,910,460 | 20.5% |
|          hit | 177,578,580 | 79.4% |
|         miss | 4,565,360 | 2.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 89,200 | 86.6% |
| Failure | 13,780 | 13.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 4,560 | 33.1% |
| no dict | 2,960 | 21.5% |
| code complex parameters | 1,600 | 11.6% |
| cfunc noargs | 1,380 | 10.0% |
| class no vectorcall | 1,340 | 9.7% |
| other | 1,280 | 9.3% |
| cmethod | 380 | 2.8% |
| class mutable | 80 | 0.6% |
| metaclass | 60 | 0.4% |
| wrong number arguments | 40 | 0.3% |
| cfunc varargs | 40 | 0.3% |
| operator wrapper | 40 | 0.3% |
| cfunc varargs keywords | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 372,820 | 1.2% |
|          hit | 29,773,700 | 98.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 48.4% |
| Failure | 320 | 51.6% |

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
|     deferred | 320 | 0.0% |
|          hit | 8,965,920 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 66.7% |
| Failure | 80 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 80 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 35,019,220 | 9.2% |
|          hit | 347,134,220 | 90.8% |
|         miss | 688,080 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,840 | 60.8% |
| Failure | 11,520 | 39.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 7,840 | 68.1% |
| method | 2,160 | 18.8% |
| class attr descriptor | 1,280 | 11.1% |
| not managed dict | 140 | 1.2% |
| metaclass attribute | 60 | 0.5% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,500 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 79,466,620 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,280 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 1,491,640 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 100.0% |
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
|     deferred | 2,237,660 | 28.6% |
|          hit | 5,594,200 | 71.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 9.6% |
| Failure | 940 | 90.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 940 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 9,832,440 | 12.0% |
|          hit | 71,894,380 | 87.9% |
|         miss | 4,693,880 | 5.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 89,800 | 98.1% |
| Failure | 1,760 | 1.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| overriding descriptor | 1,300 | 73.9% |
| no dict | 380 | 21.6% |
| overridden | 80 | 4.5% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 4,480,700 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 60 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,230,080 | 3.8% |
|          hit | 133,964,960 | 96.2% |
|         miss | 1,480 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,340 | 43.2% |
| Failure | 1,760 | 56.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| set | 1,280 | 72.7% |
| tuple | 380 | 21.6% |
| sequence | 100 | 5.7% |


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
| Basic | 1,271,995,660 | 52.1% |
| Not specialized | 285,652,360 | 11.7% |
| Specialized hits | 873,304,876 | 35.8% |
| Specialized misses | 9,997,404 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 45,910,460 | 46.6% |
| LOAD_ATTR | 35,019,220 | 35.5% |
| STORE_ATTR | 9,832,440 | 10.0% |
| TO_BOOL | 5,230,080 | 5.3% |
| SEND | 2,237,660 | 2.3% |
| COMPARE_OP | 372,820 | 0.4% |
| LOAD_GLOBAL | 2,500 | 0.0% |
| BINARY_OP | 860 | 0.0% |
| FOR_ITER | 320 | 0.0% |
| LOAD_SUPER_ATTR | 260 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 4,693,880 | 46.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 45.4% |
| LOAD_ATTR_SLOT | 684,600 | 6.8% |
| RESUME | 48,524 | 0.5% |
| RESUME_CHECK | 48,524 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 3,480 | 0.0% |
| TO_BOOL_NONE | 1,060 | 0.0% |
| TO_BOOL_BOOL | 420 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 51,108,820 | 35.2% |
| Calls to Python functions inlined | 94,051,380 | 64.8% |
| Calls via PyEval_EvalFrame (total) | 51,108,820 | 35.2% |
| Calls via PyEval_EvalFrame (vector) | 45,511,080 | 31.4% |
| Calls via PyEval_EvalFrame (generator) | 5,597,740 | 3.9% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 45,511,080 | 31.4% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 4,458,720 | 3.1% |
| Calls via PyEval_EvalFrame (function ex) | 746,560 | 0.5% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.1% |
| Calls via PyEval_EvalFrame (method) | 20,153,400 | 13.9% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 133,968,160 | 92.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 64,061,554 | 36.8% |
| Frees to freelist | 64,521,486 |  |
| Allocations | 110,120,068 | 63.2% |
| Allocations to 512 bytes | 110,058,022 | 63.2% |
| Allocations to 4 kbytes | 61,917 | 0.0% |
| Allocations over 4 kbytes | 129 | 0.0% |
| Frees | 112,222,185 |  |
| New values | 420 |  |
| Interpreter increfs | 1,201,621,640 | 68.4% |
| Interpreter decrefs | 1,290,032,540 | 67.6% |
| Increfs | 554,496,737 | 31.6% |
| Decrefs | 617,818,579 | 32.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 92,581,040 |  |
| Method cache misses | 2,773,180 |  |
| Method cache collisions | 2,768,595 |  |
| Method cache dunder hits | 15,655,527 |  |
| Method cache dunder misses | 533 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 53,340 | 2,040 | 366,946,996 |
| 1 | 4,840 | 0 | 373,306,304 |
| 2 | 440 | 0 | 903,622,828 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 2,440 |  |
| Traces created | 2,440 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 20 | 0.8% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 2,300 | 94.3% |
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
| <= 32 | 2,400 | 98.4% |
| <= 64 | 0 | 0.0% |
| <= 128 | 40 | 1.6% |


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
| <= 16 | 40 | 1.6% |
| <= 32 | 20 | 0.8% |
| <= 64 | 40 | 1.6% |


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
| CALL | 20 |
| CALL_FUNCTION_EX | 20 |
| CALL_KW | 20 |


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
