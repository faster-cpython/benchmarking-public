
# Pystats results

- benchmark: async_tree_io
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 797,197,080 | 18.7% | 18.7% |  |
| RESUME_CHECK | 255,019,460 | 6.0% | 24.7% | 0.0% |
| POP_JUMP_IF_FALSE | 233,374,600 | 5.5% | 30.2% |  |
| LOAD_ATTR_SLOT | 207,688,220 | 4.9% | 35.1% | 0.0% |
| TO_BOOL_BOOL | 175,884,020 | 4.1% | 39.2% |  |
| LOAD_CONST | 156,782,380 | 3.7% | 42.9% |  |
| LOAD_FAST_LOAD_FAST | 156,022,040 | 3.7% | 46.6% |  |
| RETURN_VALUE | 147,516,480 | 3.5% | 50.0% |  |
| STORE_ATTR_SLOT | 142,582,940 | 3.4% | 53.4% | 0.0% |
| LOAD_GLOBAL_MODULE | 134,827,100 | 3.2% | 56.6% |  |
| POP_TOP | 134,378,620 | 3.2% | 59.7% |  |
| INTERPRETER_EXIT | 127,354,800 | 3.0% | 62.7% |  |
| LOAD_ATTR_INSTANCE_VALUE | 117,230,240 | 2.8% | 65.5% |  |
| STORE_FAST | 110,513,440 | 2.6% | 68.1% |  |
| RETURN_CONST | 105,263,100 | 2.5% | 70.5% |  |
| CALL_PY_EXACT_ARGS | 103,776,000 | 2.4% | 73.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 92,574,940 | 2.2% | 75.2% |  |
| LOAD_GLOBAL_BUILTIN | 75,109,220 | 1.8% | 76.9% | 0.0% |
| PUSH_NULL | 71,670,380 | 1.7% | 78.6% |  |
| CALL | 64,974,800 | 1.5% | 80.1% |  |
| LOAD_ATTR_MODULE | 62,709,680 | 1.5% | 81.6% |  |
| COMPARE_OP_FLOAT | 57,184,020 | 1.3% | 82.9% |  |
| CALL_ISINSTANCE | 57,183,940 | 1.3% | 84.3% |  |
| LOAD_DEREF | 47,776,100 | 1.1% | 85.4% |  |
| LOAD_ATTR | 44,070,760 | 1.0% | 86.5% |  |
| POP_JUMP_IF_NOT_NONE | 43,299,240 | 1.0% | 87.5% |  |
| TO_BOOL_NONE | 42,550,040 | 1.0% | 88.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 38,825,380 | 0.9% | 89.4% | 0.0% |
| ENTER_EXECUTOR | 26,126,340 | 0.6% | 90.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 22,483,820 | 0.5% | 90.5% | 20.3% |
| CALL_METHOD_DESCRIPTOR_O | 22,395,360 | 0.5% | 91.1% | 0.0% |
| SEND_GEN | 22,395,100 | 0.5% | 91.6% |  |
| CALL_FUNCTION_EX | 21,648,560 | 0.5% | 92.1% |  |
| POP_JUMP_IF_TRUE | 17,173,780 | 0.4% | 92.5% |  |
| END_SEND | 15,676,560 | 0.4% | 92.9% |  |
| RETURN_GENERATOR | 15,676,560 | 0.4% | 93.2% |  |
| GET_AWAITABLE | 15,676,560 | 0.4% | 93.6% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 15,676,560 | 0.4% | 94.0% |  |
| YIELD_VALUE | 15,676,560 | 0.4% | 94.3% |  |
| CALL_KW | 14,183,440 | 0.3% | 94.7% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.3% | 95.0% |  |
| NOP | 12,695,720 | 0.3% | 95.3% |  |
| COPY_FREE_VARS | 12,691,380 | 0.3% | 95.6% |  |
| STORE_DEREF | 12,690,160 | 0.3% | 95.9% |  |
| BUILD_LIST | 10,455,000 | 0.2% | 96.1% |  |
| COMPARE_OP_INT | 8,961,940 | 0.2% | 96.3% |  |
| SEND | 8,960,700 | 0.2% | 96.5% |  |
| BINARY_OP_ADD_INT | 8,957,780 | 0.2% | 96.8% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.2% | 97.0% |  |
| LOAD_SUPER_ATTR_METHOD | 8,212,000 | 0.2% | 97.2% |  |
| CALL_BUILTIN_FAST | 8,211,580 | 0.2% | 97.3% |  |
| CALL_INTRINSIC_1 | 7,467,000 | 0.2% | 97.5% |  |
| LIST_EXTEND | 7,467,000 | 0.2% | 97.7% |  |
| TO_BOOL | 5,231,740 | 0.1% | 97.8% |  |
| STORE_ATTR | 5,230,120 | 0.1% | 97.9% |  |
| FOR_ITER_RANGE | 5,229,280 | 0.1% | 98.1% |  |
| CONTAINS_OP | 5,225,800 | 0.1% | 98.2% |  |
| TO_BOOL_LIST | 4,483,200 | 0.1% | 98.3% |  |
| JUMP_FORWARD | 4,483,140 | 0.1% | 98.4% |  |
| JUMP_BACKWARD | 4,482,020 | 0.1% | 98.5% |  |
| COPY | 4,481,460 | 0.1% | 98.6% |  |
| BUILD_MAP | 4,479,360 | 0.1% | 98.7% |  |
| IS_OP | 4,479,280 | 0.1% | 98.8% |  |
| CALL_TYPE_1 | 4,478,940 | 0.1% | 98.9% |  |
| BINARY_OP_SUBTRACT_INT | 4,478,920 | 0.1% | 99.0% |  |
| STORE_SUBSCR_DICT | 4,478,920 | 0.1% | 99.1% |  |
| LIST_APPEND | 4,478,880 | 0.1% | 99.2% |  |
| COMPARE_OP | 3,734,440 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_FLOAT | 3,734,280 | 0.1% | 99.4% |  |
| CALL_BUILTIN_O | 3,733,040 | 0.1% | 99.5% |  |
| CALL_PY_WITH_DEFAULTS | 3,732,840 | 0.1% | 99.6% |  |
| MAKE_CELL | 3,732,480 | 0.1% | 99.7% |  |
| GET_ITER | 2,991,700 | 0.1% | 99.8% |  |
| FOR_ITER_LIST | 2,243,380 | 0.1% | 99.8% |  |
| SWAP | 2,239,780 | 0.1% | 99.9% |  |
| FOR_ITER_TUPLE | 1,493,260 | 0.0% | 99.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.9% |  |
| CALL_BUILTIN_CLASS | 749,000 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,540 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| RESUME | 1,920 | 0.0% | 100.0% | 4,639.2% |
| BINARY_OP | 1,160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 660 | 0.0% | 100.0% |  |
| FOR_ITER | 560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 500 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 200 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 160 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 120 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 100 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_SLOT | 203,954,680 | 4.8% | 4.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 159,460,620 | 3.7% | 8.5% |
| POP_JUMP_IF_FALSE LOAD_FAST | 139,306,100 | 3.3% | 11.8% |
| RESUME_CHECK LOAD_FAST | 131,389,260 | 3.1% | 14.9% |
| CACHE RESUME_CHECK | 113,917,520 | 2.7% | 17.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 112,002,920 | 2.6% | 20.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 88,099,060 | 2.1% | 22.3% |
| RETURN_VALUE INTERPRETER_EXIT | 83,310,940 | 2.0% | 24.2% |
| LOAD_CONST LOAD_FAST | 79,132,100 | 1.9% | 26.1% |
| STORE_FAST LOAD_FAST | 74,668,480 | 1.8% | 27.9% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 72,410,040 | 1.7% | 29.6% |
| LOAD_FAST STORE_ATTR_SLOT | 70,171,440 | 1.6% | 31.2% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 69,876,480 | 1.6% | 32.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 66,149,760 | 1.6% | 34.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 62,711,600 | 1.5% | 35.9% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 62,708,600 | 1.5% | 37.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 60,917,920 | 1.4% | 38.8% |
| LOAD_ATTR_MODULE PUSH_NULL | 58,976,540 | 1.4% | 40.2% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 57,484,520 | 1.4% | 41.5% |
| LOAD_ATTR_SLOT LOAD_FAST | 57,183,940 | 1.3% | 42.9% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 57,183,860 | 1.3% | 44.2% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 57,183,440 | 1.3% | 45.5% |
| COMPARE_OP_FLOAT RETURN_VALUE | 57,183,420 | 1.3% | 46.9% |
| LOAD_ATTR_SLOT COMPARE_OP_FLOAT | 57,183,400 | 1.3% | 48.2% |
| RETURN_CONST POP_TOP | 53,754,120 | 1.3% | 49.5% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 51,508,260 | 1.2% | 50.7% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 43,300,720 | 1.0% | 51.7% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 42,550,040 | 1.0% | 52.7% |
| STORE_ATTR_SLOT LOAD_CONST | 41,803,980 | 1.0% | 53.7% |
| LOAD_FAST LOAD_ATTR | 40,318,220 | 0.9% | 54.7% |
| RETURN_CONST INTERPRETER_EXIT | 39,564,900 | 0.9% | 55.6% |
| POP_TOP LOAD_FAST | 38,821,880 | 0.9% | 56.5% |
| LOAD_FAST RETURN_VALUE | 38,820,420 | 0.9% | 57.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 38,819,920 | 0.9% | 58.3% |
| CALL STORE_FAST | 38,818,300 | 0.9% | 59.2% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 38,071,000 | 0.9% | 60.1% |
| POP_JUMP_IF_FALSE RETURN_CONST | 33,592,700 | 0.8% | 60.9% |
| POP_JUMP_IF_FALSE LOAD_CONST | 29,863,760 | 0.7% | 61.6% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 29,860,260 | 0.7% | 62.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 29,115,580 | 0.7% | 63.0% |
| POP_TOP RETURN_CONST | 29,114,440 | 0.7% | 63.7% |
| PUSH_NULL LOAD_FAST | 28,369,880 | 0.7% | 64.4% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 26,878,240 | 0.6% | 65.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 26,874,160 | 0.6% | 65.6% |
| RETURN_VALUE STORE_FAST | 26,129,760 | 0.6% | 66.2% |
| RETURN_VALUE TO_BOOL_BOOL | 25,381,280 | 0.6% | 66.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 25,381,200 | 0.6% | 67.4% |
| STORE_ATTR_SLOT LOAD_FAST | 24,635,020 | 0.6% | 68.0% |
| STORE_ATTR_SLOT RETURN_CONST | 24,634,560 | 0.6% | 68.6% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 24,634,360 | 0.6% | 69.2% |
| LOAD_CONST STORE_FAST | 22,404,000 | 0.5% | 69.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 22,399,700 | 0.5% | 70.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 22,395,340 | 0.5% | 70.7% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 21,648,720 | 0.5% | 71.3% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 21,648,560 | 0.5% | 71.8% |
| POP_TOP LOAD_CONST | 20,904,420 | 0.5% | 72.3% |
| LOAD_FAST LOAD_CONST | 17,918,260 | 0.4% | 72.7% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 17,916,200 | 0.4% | 73.1% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,800 | 0.4% | 73.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 17,915,760 | 0.4% | 73.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 17,173,700 | 0.4% | 74.3% |
| PUSH_NULL CALL | 17,172,580 | 0.4% | 74.7% |
| LOAD_FAST CALL | 17,171,280 | 0.4% | 75.2% |
| STORE_FAST RETURN_CONST | 17,171,200 | 0.4% | 75.6% |
| LOAD_FAST_LOAD_FAST CALL | 17,169,560 | 0.4% | 76.0% |
| CALL_FUNCTION_EX POP_TOP | 17,169,520 | 0.4% | 76.4% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 17,169,280 | 0.4% | 76.8% |
| POP_TOP ENTER_EXECUTOR | 17,169,020 | 0.4% | 77.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 16,423,560 | 0.4% | 77.6% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 16,423,340 | 0.4% | 77.9% |
| GET_AWAITABLE LOAD_CONST | 15,676,560 | 0.4% | 78.3% |
| POP_TOP RESUME_CHECK | 15,676,440 | 0.4% | 78.7% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 15,676,420 | 0.4% | 79.0% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 14,932,000 | 0.4% | 79.4% |
| POP_JUMP_IF_TRUE LOAD_FAST | 13,437,220 | 0.3% | 79.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 13,436,860 | 0.3% | 80.0% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 13,434,840 | 0.3% | 80.3% |
| NOP LOAD_FAST | 12,695,160 | 0.3% | 80.6% |
| COPY_FREE_VARS RESUME_CHECK | 12,690,940 | 0.3% | 80.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 11,946,120 | 0.3% | 81.2% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 11,945,940 | 0.3% | 81.5% |
| END_SEND POP_TOP | 11,944,080 | 0.3% | 81.8% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 11,943,840 | 0.3% | 82.1% |
| RETURN_GENERATOR GET_AWAITABLE | 11,197,600 | 0.3% | 82.3% |
| YIELD_VALUE YIELD_VALUE | 11,197,600 | 0.3% | 82.6% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 11,197,560 | 0.3% | 82.9% |
| SEND_GEN RESUME_CHECK | 11,197,520 | 0.3% | 83.1% |
| SEND_GEN POP_TOP | 11,197,500 | 0.3% | 83.4% |
| LOAD_CONST SEND_GEN | 11,197,440 | 0.3% | 83.6% |
| LOAD_CONST CALL_KW | 10,451,320 | 0.2% | 83.9% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 9,704,680 | 0.2% | 84.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 8,961,940 | 0.2% | 84.3% |
| LOAD_DEREF LOAD_FAST | 8,958,740 | 0.2% | 84.5% |
| CALL POP_TOP | 8,958,640 | 0.2% | 84.7% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.2% | 85.0% |
| CACHE COPY_FREE_VARS | 8,958,020 | 0.2% | 85.2% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.2% | 85.4% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.2% | 85.6% |
| LOAD_CONST BINARY_OP_ADD_INT | 8,957,720 | 0.2% | 85.8% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.2% | 86.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 113,917,520 | 89.4% |
| COPY_FREE_VARS | 8,958,020 | 7.0% |
| POP_TOP | 4,478,960 | 3.5% |
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
| LOAD_CONST | 120 | 75.0% |
| LOAD_FAST | 40 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 60 | 37.5% |
| LOAD_ATTR | 40 | 25.0% |
| PUSH_EXC_INFO | 20 | 12.5% |
| STORE_FAST | 20 | 12.5% |
| BINARY_SUBSCR_DICT | 20 | 12.5% |


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
| RETURN_CONST | 7,465,120 | 47.6% |
| SEND | 4,478,960 | 28.6% |
| RETURN_VALUE | 3,732,480 | 23.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 11,944,080 | 76.2% |
| LOAD_FAST | 3,732,480 | 23.8% |


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
| RETURN_VALUE | 83,310,940 | 65.4% |
| RETURN_CONST | 39,564,900 | 31.1% |
| YIELD_VALUE | 4,478,960 | 3.5% |


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
| RESUME_CHECK | 4,481,620 | 35.3% |
| STORE_FAST | 4,480,960 | 35.3% |
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 29.4% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,695,160 | 100.0% |
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
| RETURN_CONST | 53,754,120 | 40.0% |
| CALL_METHOD_DESCRIPTOR_O | 22,395,340 | 16.7% |
| CALL_FUNCTION_EX | 17,169,520 | 12.8% |
| END_SEND | 11,944,080 | 8.9% |
| SEND_GEN | 11,197,500 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,821,880 | 28.9% |
| RETURN_CONST | 29,114,440 | 21.7% |
| LOAD_CONST | 20,904,420 | 15.6% |
| ENTER_EXECUTOR | 17,169,020 | 12.8% |
| RESUME_CHECK | 15,676,440 | 11.7% |


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
| LOAD_ATTR_MODULE | 58,976,540 | 82.3% |
| LOAD_ATTR | 7,467,900 | 10.4% |
| LOAD_FAST | 5,225,860 | 7.3% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,369,880 | 39.6% |
| LOAD_FAST_LOAD_FAST | 21,648,560 | 30.2% |
| CALL | 17,172,580 | 24.0% |
| LOAD_GLOBAL_MODULE | 3,732,440 | 5.2% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 1.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,943,840 | 76.2% |
| CALL_PY_WITH_DEFAULTS | 3,732,460 | 23.8% |
| CALL | 120 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 11,197,600 | 71.4% |
| LIST_APPEND | 4,478,880 | 28.6% |
| CALL | 40 | 0.0% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 57,183,420 | 38.8% |
| LOAD_FAST | 38,820,420 | 26.3% |
| LOAD_ATTR_INSTANCE_VALUE | 29,860,260 | 20.2% |
| CALL | 4,481,180 | 3.0% |
| RETURN_VALUE | 4,479,360 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 83,310,940 | 56.5% |
| STORE_FAST | 26,129,760 | 17.7% |
| TO_BOOL_BOOL | 25,381,280 | 17.2% |
| RETURN_VALUE | 4,479,360 | 3.0% |
| LOAD_FAST | 3,734,320 | 2.5% |


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
| LOAD_ATTR_INSTANCE_VALUE | 4,481,100 | 85.7% |
| LOAD_FAST | 746,640 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| LOAD_ATTR | 620 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,480,040 | 85.6% |
| POP_JUMP_IF_TRUE | 748,560 | 14.3% |
| TO_BOOL | 1,760 | 0.0% |
| TO_BOOL_BOOL | 960 | 0.0% |
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
| LOAD_CONST | 200 | 17.2% |
| LOAD_GLOBAL_MODULE | 180 | 15.5% |
| UNARY_INVERT | 160 | 13.8% |
| BINARY_OP | 160 | 13.8% |

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
| LOAD_ATTR_SLOT | 3,734,500 | 35.7% |
| LOAD_FAST | 3,732,480 | 35.7% |
| STORE_FAST | 748,320 | 7.2% |
| POP_JUMP_IF_FALSE | 746,480 | 7.1% |
| STORE_DEREF | 746,480 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,467,240 | 71.4% |
| STORE_FAST | 1,494,800 | 14.3% |
| STORE_DEREF | 746,480 | 7.1% |
| SWAP | 746,480 | 7.1% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,732,480 | 83.3% |
| STORE_FAST | 746,480 | 16.7% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 3,732,480 | 83.3% |
| STORE_FAST | 746,480 | 16.7% |
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
| PUSH_NULL | 17,172,580 | 26.4% |
| LOAD_FAST | 17,171,280 | 26.4% |
| LOAD_FAST_LOAD_FAST | 17,169,560 | 26.4% |
| LOAD_ATTR | 5,227,620 | 8.0% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,100 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 38,818,300 | 59.7% |
| POP_TOP | 8,958,640 | 13.8% |
| RESUME_CHECK | 8,212,060 | 12.6% |
| RETURN_VALUE | 4,481,180 | 6.9% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,060 | 6.9% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 13,434,840 | 62.1% |
| CALL_INTRINSIC_1 | 3,734,520 | 17.3% |
| BUILD_MAP | 3,732,480 | 17.2% |
| STORE_FAST | 746,480 | 3.4% |
| DICT_MERGE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 17,169,520 | 79.3% |
| STORE_FAST | 3,732,480 | 17.2% |
| MAKE_CELL | 746,480 | 3.4% |
| COPY_FREE_VARS | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 7,467,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 3,734,520 | 50.0% |
| LOAD_CONST | 3,732,480 | 50.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,451,320 | 73.7% |
| ENTER_EXECUTOR | 3,732,120 | 26.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 31.6% |
| RESUME_CHECK | 4,478,940 | 31.6% |
| RETURN_VALUE | 3,732,480 | 26.3% |
| POP_TOP | 746,560 | 5.3% |
| STORE_DEREF | 746,480 | 5.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,732,780 | 100.0% |
| COMPARE_OP | 1,180 | 0.0% |
| CALL_BUILTIN_CLASS | 140 | 0.0% |
| LOAD_GLOBAL_MODULE | 100 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,733,020 | 100.0% |
| COMPARE_OP | 1,180 | 0.0% |
| COMPARE_OP_INT | 140 | 0.0% |
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
| CACHE | 8,958,020 | 70.6% |
| CALL_PY_EXACT_ARGS | 3,733,100 | 29.4% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,690,940 | 100.0% |
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
| POP_TOP | 17,169,020 | 65.7% |
| CALL_LIST_APPEND | 8,957,080 | 34.3% |
| POP_JUMP_IF_FALSE | 160 | 0.0% |
| JUMP_BACKWARD | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 13,434,840 | 51.4% |
| LOAD_ATTR_SLOT | 3,732,400 | 14.3% |
| CALL | 3,732,120 | 14.3% |
| CALL_KW | 3,732,120 | 14.3% |
| FOR_ITER_TUPLE | 746,460 | 2.9% |


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
| RETURN_GENERATOR | 11,197,600 | 71.4% |
| LOAD_FAST | 3,732,480 | 23.8% |
| RETURN_VALUE | 746,480 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,676,560 | 100.0% |


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
| POP_JUMP_IF_FALSE | 2,120 | 0.0% |
| CALL_LIST_APPEND | 640 | 0.0% |
| POP_TOP | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 4,479,160 | 99.9% |
| LOAD_FAST | 2,100 | 0.0% |
| FOR_ITER_LIST | 300 | 0.0% |
| FOR_ITER_TUPLE | 300 | 0.0% |
| ENTER_EXECUTOR | 80 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 15,676,420 | 100.0% |
| RESUME | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 11,197,560 | 71.4% |
| SEND | 4,479,000 | 28.6% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,478,980 | 99.9% |
| STORE_FAST | 4,000 | 0.1% |
| ENTER_EXECUTOR | 80 | 0.0% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,478,880 | 99.9% |
| LOAD_FAST | 2,320 | 0.1% |
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
| LOAD_ATTR_SLOT | 3,734,500 | 50.0% |
| LOAD_FAST | 3,732,480 | 50.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 7,467,000 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,318,220 | 91.5% |
| LOAD_ATTR_SLOT | 3,734,620 | 8.5% |
| LOAD_ATTR | 14,440 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |
| LOAD_GLOBAL | 940 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,800 | 40.7% |
| LOAD_FAST | 8,212,560 | 18.6% |
| PUSH_NULL | 7,467,900 | 16.9% |
| CALL | 5,227,620 | 11.9% |
| TO_BOOL_NONE | 4,478,920 | 10.2% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 41,803,980 | 26.7% |
| POP_JUMP_IF_FALSE | 29,863,760 | 19.0% |
| POP_TOP | 20,904,420 | 13.3% |
| LOAD_FAST | 17,918,260 | 11.4% |
| GET_AWAITABLE | 15,676,560 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 79,132,100 | 50.5% |
| STORE_FAST | 22,404,000 | 14.3% |
| SEND_GEN | 11,197,440 | 7.1% |
| CALL_KW | 10,451,320 | 6.7% |
| BINARY_OP_ADD_INT | 8,957,720 | 5.7% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 8,957,760 | 18.7% |
| LOAD_GLOBAL_BUILTIN | 8,212,000 | 17.2% |
| POP_JUMP_IF_FALSE | 5,225,360 | 10.9% |
| RESUME_CHECK | 4,478,920 | 9.4% |
| JUMP_FORWARD | 4,478,880 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,958,740 | 18.8% |
| LOAD_CONST | 8,957,920 | 18.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,225,280 | 10.9% |
| LOAD_DEREF | 4,478,880 | 9.4% |
| POP_JUMP_IF_NONE | 4,478,880 | 9.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 139,306,100 | 17.5% |
| RESUME_CHECK | 131,389,260 | 16.5% |
| LOAD_CONST | 79,132,100 | 9.9% |
| STORE_FAST | 74,668,480 | 9.4% |
| LOAD_GLOBAL_BUILTIN | 66,149,760 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 203,954,680 | 25.6% |
| LOAD_ATTR_INSTANCE_VALUE | 112,002,920 | 14.0% |
| STORE_ATTR_SLOT | 70,171,440 | 8.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 62,711,600 | 7.9% |
| LOAD_GLOBAL_MODULE | 60,917,920 | 7.6% |


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
| STORE_ATTR_SLOT | 51,508,260 | 33.0% |
| LOAD_FAST_LOAD_FAST | 25,381,200 | 16.3% |
| PUSH_NULL | 21,648,560 | 13.9% |
| POP_JUMP_IF_NOT_NONE | 17,169,280 | 11.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,436,860 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 72,410,040 | 46.4% |
| LOAD_FAST_LOAD_FAST | 25,381,200 | 16.3% |
| LOAD_FAST | 21,648,720 | 13.9% |
| CALL | 17,169,560 | 11.0% |
| LOAD_CONST | 5,225,800 | 3.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 560 | 12.3% |
| RESUME_CHECK | 540 | 11.9% |
| POP_TOP | 500 | 11.0% |
| LOAD_FAST | 500 | 11.0% |
| POP_JUMP_IF_FALSE | 500 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,540 | 33.9% |
| LOAD_ATTR | 940 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 660 | 14.5% |
| LOAD_FAST | 340 | 7.5% |
| CALL | 280 | 6.2% |


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
| TO_BOOL_BOOL | 159,460,620 | 68.3% |
| TO_BOOL_NONE | 42,550,040 | 18.2% |
| COMPARE_OP_INT | 8,961,940 | 3.8% |
| CONTAINS_OP | 5,225,800 | 2.2% |
| TO_BOOL_LIST | 4,483,200 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,306,100 | 59.7% |
| RETURN_CONST | 33,592,700 | 14.4% |
| LOAD_CONST | 29,863,760 | 12.8% |
| LOAD_GLOBAL_MODULE | 16,423,560 | 7.0% |
| LOAD_DEREF | 5,225,360 | 2.2% |


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
| LOAD_FAST | 38,819,920 | 89.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,478,960 | 10.3% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 17,169,280 | 39.7% |
| LOAD_FAST | 11,945,940 | 27.6% |
| LOAD_GLOBAL_MODULE | 9,704,680 | 22.4% |
| NOP | 3,732,560 | 8.6% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 1.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 16,423,340 | 95.6% |
| TO_BOOL | 748,560 | 4.4% |
| TO_BOOL_INT | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,437,220 | 78.2% |
| LOAD_CONST | 3,734,320 | 21.7% |
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
| POP_JUMP_IF_FALSE | 33,592,700 | 31.9% |
| POP_TOP | 29,114,440 | 27.7% |
| STORE_ATTR_SLOT | 24,634,560 | 23.4% |
| STORE_FAST | 17,171,200 | 16.3% |
| STORE_ATTR_INSTANCE_VALUE | 747,120 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 53,754,120 | 51.1% |
| INTERPRETER_EXIT | 39,564,900 | 37.6% |
| END_SEND | 7,465,120 | 7.1% |
| TO_BOOL_BOOL | 4,478,920 | 4.3% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,479,120 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 4,479,000 | 50.0% |
| SEND | 2,580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 4,478,960 | 50.0% |
| YIELD_VALUE | 4,478,960 | 50.0% |
| SEND | 2,580 | 0.0% |
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
| CALL | 38,818,300 | 35.1% |
| RETURN_VALUE | 26,129,760 | 23.6% |
| LOAD_CONST | 22,404,000 | 20.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,480,960 | 4.1% |
| FOR_ITER_RANGE | 4,480,960 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,668,480 | 67.6% |
| RETURN_CONST | 17,171,200 | 15.5% |
| LOAD_FAST_LOAD_FAST | 5,226,040 | 4.7% |
| NOP | 4,480,960 | 4.1% |
| LOAD_GLOBAL_MODULE | 4,479,080 | 4.1% |


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
| YIELD_VALUE | 11,197,600 | 71.4% |
| SEND | 4,478,960 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 11,197,600 | 71.4% |
| INTERPRETER_EXIT | 4,478,960 | 28.6% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,080 | 56.2% |
| CACHE | 300 | 15.6% |
| COPY_FREE_VARS | 280 | 14.6% |
| POP_TOP | 120 | 6.2% |
| SEND_GEN | 80 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 920 | 47.9% |
| LOAD_GLOBAL | 560 | 29.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 140 | 7.3% |
| NOP | 100 | 5.2% |
| LOAD_CONST | 100 | 5.2% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,732,440 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,800 | 0.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,732,460 | 100.0% |
| STORE_FAST | 1,820 | 0.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,957,720 | 100.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 8,957,720 | 100.0% |
| SWAP | 60 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 33.3% |
| BINARY_OP | 40 | 33.3% |
| LOAD_FAST | 40 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,478,880 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,478,840 | 100.0% |
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
| LOAD_CONST | 600 | 90.9% |
| BINARY_SUBSCR | 60 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 460 | 69.7% |
| LOAD_ATTR_SLOT | 160 | 24.2% |
| LOAD_ATTR | 40 | 6.1% |


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
| PUSH_NULL | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 60 | 100.0% |


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
| LOAD_CONST | 4,479,060 | 54.5% |
| LOAD_FAST | 3,732,440 | 45.5% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,479,020 | 54.5% |
| POP_TOP | 3,732,460 | 45.5% |
| TO_BOOL_BOOL | 80 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,732,480 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.0% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,732,440 | 100.0% |
| STORE_FAST | 460 | 0.0% |
| POP_TOP | 120 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 57,183,440 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 380 | 0.0% |
| CALL | 80 | 0.0% |
| BUILD_TUPLE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 57,183,860 | 100.0% |
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
| LOAD_FAST_LOAD_FAST | 120 | 60.0% |
| RETURN_VALUE | 40 | 20.0% |
| CALL | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 70.0% |
| STORE_FAST | 60 | 30.0% |


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
| LOAD_ATTR | 17,915,800 | 79.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 19.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| LOAD_ATTR_METHOD_NO_DICT | 2,520 | 0.0% |
| CALL | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 17,915,760 | 79.7% |
| STORE_FAST | 4,480,960 | 19.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,916,200 | 80.0% |
| CALL | 4,479,060 | 20.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 22,395,340 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 57,484,520 | 55.4% |
| LOAD_FAST | 26,878,240 | 25.9% |
| LOAD_ATTR_METHOD_NO_DICT | 7,467,040 | 7.2% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 4.3% |
| LOAD_SUPER_ATTR_METHOD | 3,732,640 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 88,099,060 | 84.9% |
| RETURN_GENERATOR | 11,943,840 | 11.5% |
| COPY_FREE_VARS | 3,733,100 | 3.6% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,732,440 | 100.0% |
| CALL | 120 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| PUSH_NULL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 3,732,460 | 100.0% |
| RESUME_CHECK | 380 | 0.0% |


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
| LOAD_ATTR_SLOT | 57,183,400 | 100.0% |
| LOAD_FAST | 440 | 0.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 57,183,420 | 100.0% |
| POP_JUMP_IF_FALSE | 600 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,481,160 | 50.0% |
| LOAD_DEREF | 4,478,840 | 50.0% |
| LOAD_GLOBAL_MODULE | 1,800 | 0.0% |
| COMPARE_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,961,940 | 100.0% |


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
| LOAD_FAST | 112,002,920 | 95.5% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 3.8% |
| LOAD_DEREF | 746,440 | 0.6% |
| LOAD_ATTR | 1,560 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 43,300,720 | 36.9% |
| RETURN_VALUE | 29,860,260 | 25.5% |
| LOAD_ATTR_METHOD_NO_DICT | 22,399,700 | 19.1% |
| TO_BOOL_LIST | 4,483,100 | 3.8% |
| TO_BOOL | 4,481,100 | 3.8% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 22,399,700 | 57.7% |
| LOAD_FAST | 11,946,120 | 30.8% |
| LOAD_DEREF | 4,478,840 | 11.5% |
| LOAD_ATTR | 580 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,874,160 | 69.2% |
| CALL_PY_EXACT_ARGS | 7,467,040 | 19.2% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 11.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,520 | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,960 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,711,600 | 67.7% |
| LOAD_ATTR_SLOT | 24,634,360 | 26.6% |
| LOAD_DEREF | 5,225,280 | 5.6% |
| LOAD_ATTR_INSTANCE_VALUE | 2,120 | 0.0% |
| LOAD_ATTR | 1,220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 57,484,520 | 62.1% |
| LOAD_FAST | 17,173,700 | 18.6% |
| LOAD_FAST_LOAD_FAST | 13,436,860 | 14.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,478,840 | 4.8% |
| CALL | 720 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 62,708,600 | 100.0% |
| LOAD_ATTR | 960 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 58,976,540 | 94.0% |
| LOAD_FAST_LOAD_FAST | 3,732,460 | 6.0% |
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
| LOAD_FAST | 203,954,680 | 98.2% |
| ENTER_EXECUTOR | 3,732,400 | 1.8% |
| LOAD_ATTR | 500 | 0.0% |
| LOAD_ATTR_SLOT | 400 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,183,940 | 27.5% |
| COMPARE_OP_FLOAT | 57,183,400 | 27.5% |
| TO_BOOL_NONE | 38,071,000 | 18.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 24,634,360 | 11.9% |
| TO_BOOL_BOOL | 14,932,000 | 7.2% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 69,876,480 | 93.0% |
| POP_TOP | 3,732,640 | 5.0% |
| PUSH_NULL | 746,440 | 1.0% |
| POP_JUMP_IF_NOT_NONE | 746,440 | 1.0% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 66,149,760 | 88.1% |
| LOAD_DEREF | 8,212,000 | 10.9% |
| LOAD_GLOBAL_MODULE | 746,480 | 1.0% |
| CALL_ISINSTANCE | 380 | 0.0% |
| CALL_BUILTIN_CLASS | 220 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,917,920 | 45.2% |
| RESUME_CHECK | 29,115,580 | 21.6% |
| POP_JUMP_IF_FALSE | 16,423,560 | 12.2% |
| POP_JUMP_IF_NOT_NONE | 9,704,680 | 7.2% |
| STORE_FAST | 4,479,080 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 62,708,600 | 46.5% |
| CALL_ISINSTANCE | 57,183,440 | 42.4% |
| LOAD_FAST_LOAD_FAST | 5,225,940 | 3.9% |
| CONTAINS_OP | 4,478,940 | 3.3% |
| CALL_PY_WITH_DEFAULTS | 3,732,440 | 2.8% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,211,760 | 100.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,732,640 | 45.5% |
| LOAD_FAST_LOAD_FAST | 3,732,520 | 45.5% |
| LOAD_FAST | 746,720 | 9.1% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 113,917,520 | 44.7% |
| CALL_PY_EXACT_ARGS | 88,099,060 | 34.5% |
| POP_TOP | 15,676,440 | 6.1% |
| COPY_FREE_VARS | 12,690,940 | 5.0% |
| SEND_GEN | 11,197,520 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 131,389,260 | 51.5% |
| LOAD_GLOBAL_BUILTIN | 69,876,480 | 27.4% |
| LOAD_GLOBAL_MODULE | 29,115,580 | 11.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 15,676,420 | 6.1% |
| NOP | 4,481,620 | 1.8% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 11,197,560 | 50.0% |
| LOAD_CONST | 11,197,440 | 50.0% |
| SEND | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,197,520 | 50.0% |
| POP_TOP | 11,197,500 | 50.0% |
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
| LOAD_FAST_LOAD_FAST | 72,410,040 | 50.8% |
| LOAD_FAST | 70,171,440 | 49.2% |
| STORE_ATTR_SLOT | 1,120 | 0.0% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 51,508,260 | 36.1% |
| LOAD_CONST | 41,803,980 | 29.3% |
| LOAD_FAST | 24,635,020 | 17.3% |
| RETURN_CONST | 24,634,560 | 17.3% |
| STORE_ATTR_SLOT | 1,120 | 0.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,478,840 | 100.0% |
| STORE_SUBSCR | 40 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,478,920 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 57,183,860 | 32.5% |
| LOAD_ATTR_INSTANCE_VALUE | 43,300,720 | 24.6% |
| RETURN_VALUE | 25,381,280 | 14.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,915,760 | 10.2% |
| LOAD_ATTR_SLOT | 14,932,000 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 159,460,620 | 90.7% |
| POP_JUMP_IF_TRUE | 16,423,340 | 9.3% |
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
| LOAD_ATTR_INSTANCE_VALUE | 4,483,100 | 100.0% |
| TO_BOOL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,483,200 | 100.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 38,071,000 | 89.5% |
| LOAD_ATTR | 4,478,920 | 10.5% |
| TO_BOOL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 42,550,040 | 100.0% |


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
|          hit | 17,171,100 | 100.0% |

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
|     deferred | 80 | 0.0% |
|          hit | 3,732,980 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 69,431,620 | 20.3% |
|          hit | 272,942,880 | 79.7% |
|         miss | 4,565,360 | 1.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 89,020 | 82.0% |
| Failure | 19,520 | 18.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 5,380 | 27.6% |
| no dict | 4,600 | 23.6% |
| cfunc noargs | 3,840 | 19.7% |
| code complex parameters | 2,420 | 12.4% |
| class no vectorcall | 1,340 | 6.9% |
| other | 1,280 | 6.6% |
| cmethod | 380 | 1.9% |
| class mutable | 80 | 0.4% |
| metaclass | 60 | 0.3% |
| wrong number arguments | 40 | 0.2% |
| cfunc varargs | 40 | 0.2% |
| operator wrapper | 40 | 0.2% |
| cfunc varargs keywords | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,733,060 | 5.1% |
|          hit | 69,878,060 | 94.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 14.5% |
| Failure | 1,180 | 85.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 1,140 | 96.6% |
| bool | 40 | 3.4% |


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
|     deferred | 44,077,780 | 6.3% |
|          hit | 660,070,300 | 93.7% |
|         miss | 26,040 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,320 | 28.0% |
| Failure | 13,700 | 72.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 9,480 | 69.2% |
| method | 2,700 | 19.7% |
| class attr descriptor | 1,280 | 9.3% |
| not managed dict | 140 | 1.0% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,420 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 209,936,240 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,200 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 8,212,000 | 100.0% |

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
|     deferred | 8,958,020 | 28.6% |
|          hit | 22,395,100 | 71.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 3.7% |
| Failure | 2,580 | 96.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 2,580 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,285,520 | 3.5% |
|          hit | 147,005,080 | 96.5% |
|         miss | 59,600 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,440 | 58.1% |
| Failure | 1,760 | 41.9% |

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
|     deferred | 60 | 0.0% |
|          hit | 4,478,920 | 100.0% |

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
|     deferred | 5,228,640 | 2.0% |
|          hit | 257,253,260 | 98.0% |

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
| Basic | 2,102,346,160 | 49.4% |
| Not specialized | 439,495,000 | 10.3% |
| Specialized hits | 1,708,576,508 | 40.2% |
| Specialized misses | 4,740,152 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 69,431,620 | 50.8% |
| LOAD_ATTR | 44,077,780 | 32.2% |
| SEND | 8,958,020 | 6.6% |
| STORE_ATTR | 5,285,520 | 3.9% |
| TO_BOOL | 5,228,640 | 3.8% |
| COMPARE_OP | 3,733,060 | 2.7% |
| LOAD_GLOBAL | 2,420 | 0.0% |
| BINARY_OP | 820 | 0.0% |
| FOR_ITER | 320 | 0.0% |
| LOAD_SUPER_ATTR | 260 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 94.5% |
| RESUME | 89,072 | 1.8% |
| RESUME_CHECK | 89,072 | 1.8% |
| STORE_ATTR_SLOT | 59,600 | 1.2% |
| LOAD_ATTR_SLOT | 22,560 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 3,480 | 0.1% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 127,354,800 | 44.8% |
| Calls to Python functions inlined | 156,777,980 | 55.2% |
| Calls via PyEval_EvalFrame (total) | 127,354,800 | 44.8% |
| Calls via PyEval_EvalFrame (vector) | 118,396,880 | 41.7% |
| Calls via PyEval_EvalFrame (generator) | 8,957,920 | 3.2% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 118,396,880 | 41.7% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 57,183,440 | 20.1% |
| Calls via PyEval_EvalFrame (function ex) | 746,560 | 0.3% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 1.6% |
| Calls via PyEval_EvalFrame (method) | 26,873,760 | 9.5% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 252,779,660 | 89.0% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 114,342,494 | 39.1% |
| Frees to freelist | 114,850,524 |  |
| Allocations | 177,888,179 | 60.9% |
| Allocations to 512 bytes | 177,772,554 | 60.8% |
| Allocations to 4 kbytes | 115,520 | 0.0% |
| Allocations over 4 kbytes | 105 | 0.0% |
| Frees | 179,992,086 |  |
| New values | 420 |  |
| Interpreter increfs | 2,393,127,860 | 70.1% |
| Interpreter decrefs | 2,528,321,580 | 69.1% |
| Increfs | 1,022,765,717 | 29.9% |
| Decrefs | 1,133,108,690 | 30.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 108,988,160 |  |
| Method cache misses | 860,640 |  |
| Method cache collisions | 856,565 |  |
| Method cache dunder hits | 75,100,647 |  |
| Method cache dunder misses | 493 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 92,956 | 2,040 | 649,201,046 |
| 1 | 8,440 | 0 | 709,968,990 |
| 2 | 660 | 0 | 2,271,076,710 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 2,420 |  |
| Traces created | 2,420 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 2,300 | 95.0% |
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
| <= 32 | 2,380 | 98.3% |
| <= 64 | 0 | 0.0% |
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
| <= 32 | 20 | 0.8% |
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
