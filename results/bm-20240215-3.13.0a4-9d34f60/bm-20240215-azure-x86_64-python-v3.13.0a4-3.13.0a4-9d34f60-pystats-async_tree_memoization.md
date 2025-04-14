
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
| LOAD_FAST | 536,891,420 | 18.9% | 18.9% |  |
| POP_JUMP_IF_FALSE | 167,866,220 | 5.9% | 24.9% |  |
| STORE_FAST | 136,923,840 | 4.8% | 29.7% |  |
| RESUME_CHECK | 136,202,020 | 4.8% | 34.5% | 0.0% |
| LOAD_FAST_LOAD_FAST | 122,343,860 | 4.3% | 38.8% |  |
| LOAD_CONST | 116,078,840 | 4.1% | 42.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 105,640,720 | 3.7% | 46.7% |  |
| TO_BOOL_BOOL | 103,357,720 | 3.6% | 50.3% | 0.0% |
| LOAD_ATTR_SLOT | 89,159,900 | 3.1% | 53.5% | 0.8% |
| POP_TOP | 77,627,380 | 2.7% | 56.2% |  |
| STORE_ATTR_SLOT | 75,838,520 | 2.7% | 58.9% | 6.2% |
| RETURN_VALUE | 72,759,620 | 2.6% | 61.4% |  |
| CALL_PY_EXACT_ARGS | 70,540,540 | 2.5% | 63.9% |  |
| LOAD_GLOBAL_MODULE | 67,906,500 | 2.4% | 66.3% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,077,820 | 2.2% | 68.6% |  |
| RETURN_CONST | 61,208,460 | 2.2% | 70.7% |  |
| LOAD_ATTR_METHOD_NO_DICT | 56,732,880 | 2.0% | 72.7% | 0.0% |
| PUSH_NULL | 53,670,480 | 1.9% | 74.6% |  |
| LOAD_ATTR | 51,903,580 | 1.8% | 76.4% |  |
| INTERPRETER_EXIT | 51,108,820 | 1.8% | 78.2% |  |
| CALL | 41,448,080 | 1.5% | 79.7% |  |
| LOAD_DEREF | 41,055,740 | 1.4% | 81.2% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 37,035,100 | 1.3% | 82.5% | 12.3% |
| POP_JUMP_IF_NOT_NONE | 33,591,000 | 1.2% | 83.6% |  |
| LOAD_ATTR_MODULE | 33,212,080 | 1.2% | 84.8% |  |
| TO_BOOL_NONE | 25,751,560 | 0.9% | 85.7% | 0.0% |
| COMPARE_OP_INT | 24,942,480 | 0.9% | 86.6% |  |
| JUMP_BACKWARD | 24,488,740 | 0.9% | 87.5% |  |
| CALL_METHOD_DESCRIPTOR_O | 19,407,000 | 0.7% | 88.2% | 0.0% |
| CALL_BUILTIN_O | 16,725,220 | 0.6% | 88.8% |  |
| BINARY_OP_ADD_INT | 16,422,700 | 0.6% | 89.3% |  |
| NOP | 16,050,020 | 0.6% | 89.9% |  |
| FOR_ITER_RANGE | 15,676,160 | 0.6% | 90.4% |  |
| LOAD_GLOBAL_BUILTIN | 15,664,140 | 0.6% | 91.0% | 0.0% |
| BUILD_LIST | 13,809,300 | 0.5% | 91.5% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.5% | 92.0% |  |
| STORE_DEREF | 12,690,160 | 0.4% | 92.4% |  |
| CALL_FUNCTION_EX | 11,568,020 | 0.4% | 92.8% |  |
| CALL_KW | 10,823,260 | 0.4% | 93.2% |  |
| CALL_INTRINSIC_1 | 10,821,300 | 0.4% | 93.6% |  |
| LIST_EXTEND | 10,821,300 | 0.4% | 94.0% |  |
| POP_JUMP_IF_TRUE | 10,453,420 | 0.4% | 94.3% |  |
| CONTAINS_OP | 8,957,920 | 0.3% | 94.7% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.3% | 95.0% |  |
| RETURN_GENERATOR | 8,956,200 | 0.3% | 95.3% |  |
| BINARY_OP_SUBTRACT_INT | 8,211,380 | 0.3% | 95.6% |  |
| FOR_ITER_LIST | 5,975,500 | 0.2% | 95.8% |  |
| COPY_FREE_VARS | 5,971,020 | 0.2% | 96.0% |  |
| END_SEND | 5,596,020 | 0.2% | 96.2% |  |
| GET_AWAITABLE | 5,596,020 | 0.2% | 96.4% |  |
| SEND_GEN | 5,594,200 | 0.2% | 96.6% |  |
| TO_BOOL | 5,231,700 | 0.2% | 96.8% |  |
| STORE_ATTR | 5,230,120 | 0.2% | 97.0% |  |
| FOR_ITER_TUPLE | 5,225,380 | 0.2% | 97.1% |  |
| TO_BOOL_LIST | 4,854,960 | 0.2% | 97.3% |  |
| CALL_BUILTIN_FAST | 4,851,400 | 0.2% | 97.5% |  |
| COMPARE_OP_FLOAT | 4,831,200 | 0.2% | 97.7% |  |
| JUMP_FORWARD | 4,483,220 | 0.2% | 97.8% |  |
| COPY | 4,481,460 | 0.2% | 98.0% |  |
| STORE_SUBSCR_DICT | 4,480,700 | 0.2% | 98.1% |  |
| IS_OP | 4,479,280 | 0.2% | 98.3% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 98.4% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 98.6% |  |
| CALL_ISINSTANCE | 4,459,220 | 0.2% | 98.8% |  |
| CALL_PY_WITH_DEFAULTS | 4,105,120 | 0.1% | 98.9% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 3,732,520 | 0.1% | 99.0% |  |
| MAKE_CELL | 3,732,480 | 0.1% | 99.2% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 3,362,160 | 0.1% | 99.3% |  |
| GET_ITER | 2,991,700 | 0.1% | 99.4% |  |
| SWAP | 2,239,780 | 0.1% | 99.5% |  |
| SEND | 2,238,700 | 0.1% | 99.6% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 2,235,840 | 0.1% | 99.6% |  |
| YIELD_VALUE | 2,235,840 | 0.1% | 99.7% |  |
| LOAD_SUPER_ATTR_METHOD | 1,491,640 | 0.1% | 99.8% |  |
| BUILD_MAP | 1,119,180 | 0.0% | 99.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 749,000 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 374,100 | 0.0% | 100.0% |  |
| COMPARE_OP | 373,440 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 372,500 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,700 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| RESUME | 1,980 | 0.0% | 100.0% | 2,452.2% |
| BINARY_OP | 1,240 | 0.0% | 100.0% |  |
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
| POP_JUMP_IF_FALSE LOAD_FAST | 102,320,580 | 3.6% | 3.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 100,413,420 | 3.5% | 7.2% |
| STORE_FAST LOAD_FAST | 98,167,420 | 3.5% | 10.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 93,654,680 | 3.3% | 13.9% |
| LOAD_FAST LOAD_ATTR_SLOT | 89,145,300 | 3.1% | 17.1% |
| RESUME_CHECK LOAD_FAST | 81,358,840 | 2.9% | 19.9% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 61,583,960 | 2.2% | 22.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 42,922,740 | 1.5% | 23.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 42,168,420 | 1.5% | 25.1% |
| LOAD_FAST LOAD_ATTR | 41,434,400 | 1.5% | 26.6% |
| CACHE RESUME_CHECK | 41,031,720 | 1.4% | 28.0% |
| LOAD_CONST LOAD_FAST | 39,183,560 | 1.4% | 29.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 36,574,440 | 1.3% | 30.7% |
| LOAD_FAST STORE_ATTR_SLOT | 33,581,280 | 1.2% | 31.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 33,220,160 | 1.2% | 33.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 33,210,980 | 1.2% | 34.2% |
| LOAD_FAST RETURN_VALUE | 32,844,660 | 1.2% | 35.4% |
| LOAD_ATTR_MODULE PUSH_NULL | 32,839,120 | 1.2% | 36.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 31,347,180 | 1.1% | 37.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 30,603,040 | 1.1% | 38.7% |
| RETURN_CONST INTERPRETER_EXIT | 29,484,360 | 1.0% | 39.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 29,111,680 | 1.0% | 40.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 27,247,760 | 1.0% | 41.8% |
| RETURN_CONST POP_TOP | 26,872,680 | 0.9% | 42.7% |
| PUSH_NULL LOAD_FAST | 26,798,660 | 0.9% | 43.7% |
| POP_TOP LOAD_FAST | 26,125,280 | 0.9% | 44.6% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 25,751,540 | 0.9% | 45.5% |
| CALL STORE_FAST | 25,377,700 | 0.9% | 46.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 24,942,480 | 0.9% | 47.3% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 23,890,320 | 0.8% | 48.1% |
| POP_JUMP_IF_FALSE RETURN_CONST | 23,512,160 | 0.8% | 48.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 23,139,660 | 0.8% | 49.8% |
| STORE_ATTR_SLOT LOAD_CONST | 21,642,900 | 0.8% | 50.5% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 21,270,100 | 0.8% | 51.3% |
| RETURN_VALUE INTERPRETER_EXIT | 20,505,680 | 0.7% | 52.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 19,784,940 | 0.7% | 52.7% |
| RETURN_VALUE STORE_FAST | 19,781,700 | 0.7% | 53.4% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 19,406,980 | 0.7% | 54.1% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 19,032,860 | 0.7% | 54.8% |
| LOAD_FAST LOAD_CONST | 18,662,780 | 0.7% | 55.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 18,660,300 | 0.7% | 56.1% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 18,287,740 | 0.6% | 56.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 18,287,700 | 0.6% | 57.4% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 16,419,540 | 0.6% | 57.9% |
| CALL_BUILTIN_O STORE_FAST | 16,352,820 | 0.6% | 58.5% |
| LOAD_FAST CALL_BUILTIN_O | 16,352,740 | 0.6% | 59.1% |
| NOP LOAD_FAST | 16,049,460 | 0.6% | 59.7% |
| LOAD_CONST STORE_FAST | 15,683,640 | 0.6% | 60.2% |
| POP_TOP RETURN_CONST | 15,301,420 | 0.5% | 60.8% |
| RETURN_VALUE TO_BOOL_BOOL | 15,300,740 | 0.5% | 61.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 15,300,660 | 0.5% | 61.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,928,360 | 0.5% | 62.4% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,928,200 | 0.5% | 62.9% |
| JUMP_BACKWARD FOR_ITER_RANGE | 14,927,840 | 0.5% | 63.4% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,927,840 | 0.5% | 63.9% |
| FOR_ITER_RANGE STORE_FAST | 14,927,840 | 0.5% | 64.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 14,185,800 | 0.5% | 65.0% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 14,181,840 | 0.5% | 65.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 14,113,660 | 0.5% | 66.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 13,809,140 | 0.5% | 66.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,809,100 | 0.5% | 66.9% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 13,791,580 | 0.5% | 67.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 13,425,040 | 0.5% | 67.9% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 12,690,400 | 0.4% | 68.4% |
| LOAD_CONST BINARY_OP_ADD_INT | 12,690,160 | 0.4% | 68.8% |
| LOAD_CONST COMPARE_OP_INT | 11,946,040 | 0.4% | 69.2% |
| STORE_ATTR_SLOT LOAD_FAST | 11,566,120 | 0.4% | 69.6% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 11,565,940 | 0.4% | 70.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 11,197,900 | 0.4% | 70.4% |
| RESUME_CHECK NOP | 11,196,100 | 0.4% | 70.8% |
| STORE_ATTR_SLOT RETURN_CONST | 11,193,840 | 0.4% | 71.2% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 0.4% | 71.6% |
| POP_TOP LOAD_CONST | 10,823,880 | 0.4% | 72.0% |
| LOAD_CONST CALL_KW | 10,823,260 | 0.4% | 72.4% |
| LOAD_ATTR PUSH_NULL | 10,822,220 | 0.4% | 72.8% |
| BUILD_LIST LOAD_FAST | 10,821,540 | 0.4% | 73.1% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 10,821,340 | 0.4% | 73.5% |
| LIST_EXTEND CALL_INTRINSIC_1 | 10,821,300 | 0.4% | 73.9% |
| LOAD_FAST CALL | 10,451,200 | 0.4% | 74.3% |
| STORE_FAST RETURN_CONST | 10,450,840 | 0.4% | 74.6% |
| LOAD_FAST_LOAD_FAST CALL | 10,449,200 | 0.4% | 75.0% |
| CALL_FUNCTION_EX POP_TOP | 10,449,160 | 0.4% | 75.4% |
| LOAD_ATTR_SLOT LOAD_ATTR | 10,449,100 | 0.4% | 75.8% |
| POP_TOP JUMP_BACKWARD | 10,449,040 | 0.4% | 76.1% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 10,449,000 | 0.4% | 76.5% |
| LOAD_ATTR_SLOT BUILD_LIST | 10,448,980 | 0.4% | 76.9% |
| LOAD_ATTR_SLOT LIST_EXTEND | 10,448,980 | 0.4% | 77.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 10,076,960 | 0.4% | 77.6% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 10,076,940 | 0.4% | 77.9% |
| LOAD_FAST PUSH_NULL | 10,009,060 | 0.4% | 78.3% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 9,702,980 | 0.3% | 78.6% |
| LOAD_ATTR CALL | 8,959,740 | 0.3% | 79.0% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.3% | 79.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 8,958,060 | 0.3% | 79.6% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 8,957,920 | 0.3% | 79.9% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.3% | 80.2% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.3% | 80.5% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.3% | 80.9% |
| CALL_LIST_APPEND JUMP_BACKWARD | 8,957,720 | 0.3% | 81.2% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.3% | 81.5% |


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
| RESUME_CHECK | 11,196,100 | 69.8% |
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 23.3% |
| STORE_FAST | 1,120,780 | 7.0% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,049,460 | 100.0% |
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
| RETURN_CONST | 26,872,680 | 34.6% |
| CALL_METHOD_DESCRIPTOR_O | 19,406,980 | 25.0% |
| CALL_FUNCTION_EX | 10,449,160 | 13.5% |
| CALL | 5,598,460 | 7.2% |
| END_SEND | 5,223,720 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,125,280 | 33.7% |
| RETURN_CONST | 15,301,420 | 19.7% |
| LOAD_CONST | 10,823,880 | 13.9% |
| JUMP_BACKWARD | 10,449,040 | 13.5% |
| RESUME_CHECK | 8,956,080 | 11.5% |


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
| LOAD_ATTR_MODULE | 32,839,120 | 61.2% |
| LOAD_ATTR | 10,822,220 | 20.2% |
| LOAD_FAST | 10,009,060 | 18.6% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,798,660 | 49.9% |
| LOAD_FAST_LOAD_FAST | 14,928,200 | 27.8% |
| CALL | 7,091,960 | 13.2% |
| LOAD_CONST | 3,732,720 | 7.0% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 1.4% |


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
| LOAD_FAST | 32,844,660 | 45.1% |
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
| LOAD_ATTR_SLOT | 10,448,980 | 75.7% |
| STORE_FAST | 748,320 | 5.4% |
| POP_JUMP_IF_FALSE | 746,480 | 5.4% |
| STORE_DEREF | 746,480 | 5.4% |
| SWAP | 746,480 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,821,540 | 78.4% |
| STORE_FAST | 1,494,800 | 10.8% |
| STORE_DEREF | 746,480 | 5.4% |
| SWAP | 746,480 | 5.4% |


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
| LOAD_ATTR | 8,959,740 | 21.6% |
| PUSH_NULL | 7,091,960 | 17.1% |
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
| CALL_INTRINSIC_1 | 10,449,000 | 90.3% |
| STORE_FAST | 746,480 | 6.5% |
| BUILD_MAP | 372,300 | 3.2% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

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
| LOAD_CONST | 10,823,260 | 100.0% |

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
| LOAD_GLOBAL_MODULE | 4,478,940 | 50.0% |
| LOAD_FAST_LOAD_FAST | 4,478,880 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,957,920 | 100.0% |


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
| POP_TOP | 10,449,040 | 42.7% |
| CALL_LIST_APPEND | 8,957,720 | 36.6% |
| LIST_APPEND | 4,478,880 | 18.3% |
| POP_JUMP_IF_FALSE | 603,100 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 14,927,840 | 61.0% |
| FOR_ITER_TUPLE | 4,478,880 | 18.3% |
| FOR_ITER_LIST | 4,478,860 | 18.3% |
| LOAD_FAST | 603,080 | 2.5% |
| FOR_ITER | 80 | 0.0% |


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
| POP_JUMP_IF_FALSE | 160 | 0.0% |

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
| LOAD_FAST | 41,434,400 | 79.8% |
| LOAD_ATTR_SLOT | 10,449,100 | 20.1% |
| LOAD_ATTR | 16,540 | 0.0% |
| LOAD_GLOBAL_MODULE | 980 | 0.0% |
| LOAD_GLOBAL | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,287,740 | 35.2% |
| PUSH_NULL | 10,822,220 | 20.9% |
| CALL | 8,959,740 | 17.3% |
| LOAD_FAST | 4,852,420 | 9.3% |
| STORE_FAST | 4,479,120 | 8.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 21,642,900 | 18.6% |
| POP_JUMP_IF_FALSE | 19,784,940 | 17.0% |
| LOAD_FAST | 18,662,780 | 16.1% |
| LOAD_FAST_LOAD_FAST | 12,690,400 | 10.9% |
| POP_TOP | 10,823,880 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,183,560 | 33.8% |
| STORE_FAST | 15,683,640 | 13.5% |
| BINARY_OP_ADD_INT | 12,690,160 | 10.9% |
| COMPARE_OP_INT | 11,946,040 | 10.3% |
| CALL_KW | 10,823,260 | 9.3% |


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
| POP_JUMP_IF_FALSE | 102,320,580 | 19.1% |
| STORE_FAST | 98,167,420 | 18.3% |
| RESUME_CHECK | 81,358,840 | 15.2% |
| LOAD_CONST | 39,183,560 | 7.3% |
| LOAD_ATTR_METHOD_NO_DICT | 27,247,760 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 100,413,420 | 18.7% |
| LOAD_ATTR_SLOT | 89,145,300 | 16.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 42,922,740 | 8.0% |
| LOAD_ATTR | 41,434,400 | 7.7% |
| STORE_ATTR_SLOT | 33,581,280 | 6.3% |


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
| STORE_ATTR_SLOT | 31,347,180 | 25.6% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 12.5% |
| PUSH_NULL | 14,928,200 | 12.2% |
| STORE_FAST | 14,113,660 | 11.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,809,140 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 42,168,420 | 34.5% |
| LOAD_FAST_LOAD_FAST | 15,300,660 | 12.5% |
| LOAD_FAST | 14,928,360 | 12.2% |
| LOAD_CONST | 12,690,400 | 10.4% |
| CALL | 10,449,200 | 8.5% |


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
| TO_BOOL_BOOL | 93,654,680 | 55.8% |
| TO_BOOL_NONE | 25,751,540 | 15.3% |
| COMPARE_OP_INT | 24,942,480 | 14.9% |
| CONTAINS_OP | 8,957,920 | 5.3% |
| TO_BOOL_LIST | 4,854,960 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 102,320,580 | 61.0% |
| RETURN_CONST | 23,512,160 | 14.0% |
| LOAD_CONST | 19,784,940 | 11.8% |
| LOAD_GLOBAL_MODULE | 7,086,780 | 4.2% |
| LOAD_DEREF | 5,225,360 | 3.1% |


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
| CALL | 25,377,700 | 18.5% |
| RETURN_VALUE | 19,781,700 | 14.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,660,300 | 13.6% |
| CALL_BUILTIN_O | 16,352,820 | 11.9% |
| LOAD_CONST | 15,683,640 | 11.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,167,420 | 71.7% |
| LOAD_FAST_LOAD_FAST | 14,113,660 | 10.3% |
| RETURN_CONST | 10,450,840 | 7.6% |
| LOAD_GLOBAL_MODULE | 8,211,520 | 6.0% |
| LOAD_CONST | 1,865,340 | 1.4% |


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

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,957,680 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,957,720 | 100.0% |


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
| LOAD_ATTR | 18,287,740 | 49.4% |
| LOAD_ATTR_METHOD_NO_DICT | 14,181,840 | 38.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 12.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.2% |
| CALL | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,660,300 | 50.4% |
| TO_BOOL_BOOL | 18,287,700 | 49.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.2% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,927,840 | 76.9% |
| CALL | 4,479,060 | 23.1% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 19,406,980 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 30,603,040 | 43.4% |
| LOAD_FAST | 23,890,320 | 33.9% |
| LOAD_ATTR_METHOD_NO_DICT | 10,821,340 | 15.3% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 6.3% |
| LOAD_SUPER_ATTR_METHOD | 372,460 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 61,583,960 | 87.3% |
| RETURN_GENERATOR | 8,583,660 | 12.2% |
| COPY_FREE_VARS | 372,920 | 0.5% |


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
| LOAD_CONST | 11,946,040 | 47.9% |
| LOAD_FAST_LOAD_FAST | 4,783,120 | 19.2% |
| LOAD_DEREF | 4,478,840 | 18.0% |
| LOAD_GLOBAL_MODULE | 3,734,240 | 15.0% |
| COMPARE_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,942,480 | 100.0% |


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
| JUMP_BACKWARD | 4,478,860 | 75.0% |
| GET_ITER | 1,496,540 | 25.0% |
| FOR_ITER | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,860 | 75.0% |
| LOAD_DEREF | 1,492,940 | 25.0% |
| RETURN_CONST | 1,880 | 0.0% |
| LOAD_FAST | 1,820 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 14,927,840 | 95.2% |
| SWAP | 746,460 | 4.8% |
| GET_ITER | 1,820 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,927,840 | 95.2% |
| SWAP | 746,480 | 4.8% |
| LOAD_CONST | 1,840 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,478,880 | 85.7% |
| GET_ITER | 746,480 | 14.3% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,880 | 85.7% |
| LOAD_GLOBAL_MODULE | 746,440 | 14.3% |
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
| LOAD_FAST | 100,413,420 | 95.1% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 4.2% |
| LOAD_DEREF | 746,440 | 0.7% |
| LOAD_ATTR | 1,540 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 36,574,440 | 34.6% |
| LOAD_ATTR_METHOD_NO_DICT | 33,220,160 | 31.4% |
| RETURN_VALUE | 16,419,540 | 15.5% |
| TO_BOOL_LIST | 4,854,880 | 4.6% |
| TO_BOOL | 4,481,060 | 4.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 33,220,160 | 58.6% |
| LOAD_FAST | 19,032,860 | 33.5% |
| LOAD_DEREF | 4,478,840 | 7.9% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 320 | 0.0% |

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
| LOAD_GLOBAL_MODULE | 33,210,980 | 100.0% |
| LOAD_ATTR | 980 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 32,839,120 | 98.9% |
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
| LOAD_FAST | 89,145,300 | 100.0% |
| LOAD_ATTR_SLOT | 13,920 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 21,270,100 | 23.9% |
| TO_BOOL_BOOL | 11,565,940 | 13.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,193,640 | 12.6% |
| LOAD_ATTR | 10,449,100 | 11.7% |
| BUILD_LIST | 10,448,980 | 11.7% |


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
| RESUME_CHECK | 23,139,660 | 34.1% |
| POP_JUMP_IF_NOT_NONE | 10,076,940 | 14.8% |
| LOAD_FAST | 8,565,420 | 12.6% |
| STORE_FAST | 8,211,520 | 12.1% |
| POP_JUMP_IF_FALSE | 7,086,780 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 33,210,980 | 48.9% |
| LOAD_FAST | 11,197,900 | 16.5% |
| LOAD_FAST_LOAD_FAST | 8,958,060 | 13.2% |
| CONTAINS_OP | 4,478,940 | 6.6% |
| CALL_ISINSTANCE | 4,458,720 | 6.6% |


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
| CALL_PY_EXACT_ARGS | 61,583,960 | 45.2% |
| CACHE | 41,031,720 | 30.1% |
| POP_TOP | 8,956,080 | 6.6% |
| COPY_FREE_VARS | 5,970,580 | 4.4% |
| CALL | 4,851,860 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 81,358,840 | 59.7% |
| LOAD_GLOBAL_MODULE | 23,139,660 | 17.0% |
| LOAD_GLOBAL_BUILTIN | 13,791,580 | 10.1% |
| NOP | 11,196,100 | 8.2% |
| LOAD_DEREF | 4,478,920 | 3.3% |


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
| LOAD_ATTR_INSTANCE_VALUE | 36,574,440 | 35.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,287,700 | 17.7% |
| RETURN_VALUE | 15,300,740 | 14.8% |
| LOAD_ATTR_SLOT | 11,565,940 | 11.2% |
| COPY | 4,479,080 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 93,654,680 | 90.6% |
| POP_JUMP_IF_TRUE | 9,702,980 | 9.4% |
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
| LOAD_ATTR_INSTANCE_VALUE | 4,854,880 | 100.0% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,854,960 | 100.0% |


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
|          hit | 26,877,040 | 100.0% |

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
|     deferred | 52,624,140 | 13.2% |
|          hit | 347,068,120 | 86.8% |
|         miss | 755,480 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 19,140 | 54.8% |
| Failure | 15,780 | 45.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 9,640 | 61.1% |
| method | 4,620 | 29.3% |
| class attr descriptor | 1,280 | 8.1% |
| not managed dict | 140 | 0.9% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,500 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 83,570,560 | 100.0% |
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
| Basic | 1,451,285,900 | 51.2% |
| Not specialized | 331,781,320 | 11.7% |
| Specialized hits | 1,040,095,986 | 36.7% |
| Specialized misses | 10,064,834 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 52,624,140 | 45.3% |
| CALL | 45,910,460 | 39.5% |
| STORE_ATTR | 9,832,440 | 8.5% |
| TO_BOOL | 5,230,080 | 4.5% |
| SEND | 2,237,660 | 1.9% |
| COMPARE_OP | 372,820 | 0.3% |
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
| STORE_ATTR_SLOT | 4,693,880 | 46.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 45.1% |
| LOAD_ATTR_SLOT | 738,520 | 7.3% |
| RESUME | 48,554 | 0.5% |
| RESUME_CHECK | 48,554 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 16,960 | 0.2% |
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
| Frames pushed | 78,378,260 | 54.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 64,061,348 | 36.8% |
| Frees to freelist | 64,521,549 |  |
| Allocations | 110,119,977 | 63.2% |
| Allocations to 512 bytes | 110,057,978 | 63.2% |
| Allocations to 4 kbytes | 61,870 | 0.0% |
| Allocations over 4 kbytes | 129 | 0.0% |
| Frees | 112,222,285 |  |
| New values | 420 |  |
| Interpreter increfs | 1,363,860,320 | 78.5% |
| Interpreter decrefs | 1,427,790,412 | 75.6% |
| Increfs | 373,022,087 | 21.5% |
| Decrefs | 460,824,635 | 24.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 92,315,091 |  |
| Method cache misses | 3,110,789 |  |
| Method cache collisions | 3,106,009 |  |
| Method cache dunder hits | 15,655,565 |  |
| Method cache dunder misses | 495 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 53,357 | 2,040 | 367,319,542 |
| 1 | 4,840 | 0 | 372,820,250 |
| 2 | 440 | 0 | 903,137,070 |


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
| Low confidence | 0 |  |
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
