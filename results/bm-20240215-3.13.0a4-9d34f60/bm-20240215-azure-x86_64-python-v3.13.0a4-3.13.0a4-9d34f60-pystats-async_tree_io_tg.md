
# Pystats results

- benchmark: async_tree_io_tg
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 933,786,800 | 20.2% | 20.2% |  |
| RESUME_CHECK | 260,989,440 | 5.6% | 25.8% | 0.0% |
| LOAD_ATTR_SLOT | 260,681,820 | 5.6% | 31.5% | 0.0% |
| POP_JUMP_IF_FALSE | 252,031,720 | 5.4% | 36.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 209,041,720 | 4.5% | 41.4% |  |
| TO_BOOL_BOOL | 194,542,100 | 4.2% | 45.6% |  |
| LOAD_CONST | 153,795,460 | 3.3% | 49.0% |  |
| POP_TOP | 153,040,180 | 3.3% | 52.3% |  |
| LOAD_FAST_LOAD_FAST | 149,303,160 | 3.2% | 55.5% |  |
| STORE_ATTR_SLOT | 146,314,940 | 3.2% | 58.7% | 0.0% |
| RETURN_VALUE | 143,784,060 | 3.1% | 61.8% |  |
| STORE_FAST | 132,156,480 | 2.9% | 64.6% |  |
| INTERPRETER_EXIT | 128,101,300 | 2.8% | 67.4% |  |
| LOAD_GLOBAL_MODULE | 124,375,740 | 2.7% | 70.1% |  |
| CALL_PY_EXACT_ARGS | 108,253,080 | 2.3% | 72.4% |  |
| RETURN_CONST | 101,530,700 | 2.2% | 74.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 92,574,920 | 2.0% | 76.6% |  |
| PUSH_NULL | 79,879,460 | 1.7% | 78.4% |  |
| LOAD_ATTR_METHOD_NO_DICT | 73,159,720 | 1.6% | 80.0% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 66,151,460 | 1.4% | 81.4% | 0.0% |
| COMPARE_OP_FLOAT | 60,916,100 | 1.3% | 82.7% |  |
| CALL | 59,747,900 | 1.3% | 84.0% |  |
| LOAD_ATTR_MODULE | 58,230,400 | 1.3% | 85.2% |  |
| CALL_ISINSTANCE | 57,183,940 | 1.2% | 86.5% |  |
| LOAD_ATTR | 56,762,400 | 1.2% | 87.7% |  |
| TO_BOOL_NONE | 42,550,040 | 0.9% | 88.6% |  |
| POP_JUMP_IF_NOT_NONE | 40,313,320 | 0.9% | 89.5% |  |
| CALL_METHOD_DESCRIPTOR_O | 35,085,080 | 0.8% | 90.3% | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 30,606,940 | 0.7% | 90.9% | 0.0% |
| JUMP_BACKWARD | 25,382,440 | 0.5% | 91.5% |  |
| SEND_GEN | 24,634,500 | 0.5% | 92.0% |  |
| FOR_ITER_RANGE | 22,396,520 | 0.5% | 92.5% |  |
| NOP | 21,651,680 | 0.5% | 93.0% |  |
| BUILD_LIST | 21,650,400 | 0.5% | 93.4% |  |
| CALL_FUNCTION_EX | 20,902,080 | 0.5% | 93.9% |  |
| CALL_INTRINSIC_1 | 20,901,840 | 0.5% | 94.3% |  |
| LIST_EXTEND | 20,901,840 | 0.5% | 94.8% |  |
| POP_JUMP_IF_TRUE | 17,173,780 | 0.4% | 95.2% |  |
| END_SEND | 17,169,520 | 0.4% | 95.5% |  |
| RETURN_GENERATOR | 17,169,520 | 0.4% | 95.9% |  |
| GET_AWAITABLE | 17,169,520 | 0.4% | 96.3% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 16,423,040 | 0.4% | 96.6% |  |
| YIELD_VALUE | 16,423,040 | 0.4% | 97.0% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.3% | 97.3% |  |
| CALL_KW | 13,436,960 | 0.3% | 97.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 11,946,640 | 0.3% | 97.8% |  |
| TO_BOOL | 11,205,740 | 0.2% | 98.1% |  |
| TO_BOOL_LIST | 8,961,660 | 0.2% | 98.3% |  |
| SEND | 8,960,780 | 0.2% | 98.4% |  |
| LOAD_DEREF | 7,466,180 | 0.2% | 98.6% |  |
| COPY_FREE_VARS | 7,466,020 | 0.2% | 98.8% |  |
| LOAD_SUPER_ATTR_METHOD | 7,465,540 | 0.2% | 98.9% |  |
| CALL_BUILTIN_O | 7,465,040 | 0.2% | 99.1% |  |
| JUMP_FORWARD | 4,483,140 | 0.1% | 99.2% |  |
| COMPARE_OP_INT | 4,483,080 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_INT | 4,478,920 | 0.1% | 99.4% |  |
| COMPARE_OP | 3,734,400 | 0.1% | 99.5% |  |
| BINARY_OP_ADD_FLOAT | 3,734,280 | 0.1% | 99.5% |  |
| BUILD_MAP | 3,732,880 | 0.1% | 99.6% |  |
| CALL_PY_WITH_DEFAULTS | 3,732,840 | 0.1% | 99.7% |  |
| BINARY_SUBSCR_LIST_INT | 3,732,740 | 0.1% | 99.8% |  |
| CALL_BUILTIN_FAST | 3,732,700 | 0.1% | 99.9% |  |
| CALL_BUILTIN_CLASS | 1,495,460 | 0.0% | 99.9% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 760,860 | 0.0% | 99.9% | 100.0% |
| GET_ITER | 752,260 | 0.0% | 99.9% |  |
| BEFORE_ASYNC_WITH | 746,480 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 746,460 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 746,460 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 746,460 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,460 | 0.0% | 100.0% |  |
| STORE_ATTR | 3,700 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 3,700 | 0.0% | 100.0% |  |
| COPY | 2,580 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
| RESUME | 1,980 | 0.0% | 100.0% | 3,752.7% |
| BINARY_OP | 1,080 | 0.0% | 100.0% |  |
| BUILD_TUPLE | 640 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 460 | 0.0% | 100.0% |  |
| FOR_ITER | 440 | 0.0% | 100.0% |  |
| IS_OP | 400 | 0.0% | 100.0% |  |
| SWAP | 340 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 240 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 240 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 200 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 180 | 0.0% | 100.0% |  |
| POP_EXCEPT | 180 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 180 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 180 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 160 | 0.0% | 100.0% |  |
| UNARY_INVERT | 160 | 0.0% | 100.0% |  |
| UNARY_NOT | 160 | 0.0% | 100.0% |  |
| CONTAINS_OP | 160 | 0.0% | 100.0% |  |
| STORE_FAST_STORE_FAST | 160 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 140 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 140 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 120 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 120 | 0.0% | 100.0% |  |
| IMPORT_NAME | 100 | 0.0% | 100.0% |  |
| DICT_MERGE | 80 | 0.0% | 100.0% |  |
| MAKE_CELL | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 80 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 60 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_INT | 60 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 60 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_SLOT | 260,679,640 | 5.6% | 5.6% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 204,560,400 | 4.4% | 10.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 181,851,120 | 3.9% | 14.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 178,119,180 | 3.9% | 17.8% |
| RESUME_CHECK LOAD_FAST | 139,600,520 | 3.0% | 20.9% |
| CACHE RESUME_CHECK | 118,396,380 | 2.6% | 23.4% |
| STORE_FAST LOAD_FAST | 98,551,640 | 2.1% | 25.6% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 92,576,140 | 2.0% | 27.6% |
| LOAD_CONST LOAD_FAST | 85,850,020 | 1.9% | 29.4% |
| RETURN_VALUE INTERPRETER_EXIT | 83,310,940 | 1.8% | 31.2% |
| LOAD_FAST STORE_ATTR_SLOT | 73,903,440 | 1.6% | 32.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 72,410,040 | 1.6% | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 70,918,520 | 1.5% | 35.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 62,711,560 | 1.4% | 37.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 60,918,720 | 1.3% | 38.6% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 60,917,920 | 1.3% | 39.9% |
| LOAD_ATTR_SLOT LOAD_FAST | 60,916,020 | 1.3% | 41.2% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 58,230,960 | 1.3% | 42.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 58,229,320 | 1.3% | 43.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 57,192,000 | 1.2% | 45.0% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 57,183,860 | 1.2% | 46.2% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 57,183,440 | 1.2% | 47.4% |
| COMPARE_OP_FLOAT RETURN_VALUE | 57,183,420 | 1.2% | 48.7% |
| LOAD_ATTR_SLOT COMPARE_OP_FLOAT | 57,183,400 | 1.2% | 49.9% |
| POP_TOP LOAD_FAST | 56,737,000 | 1.2% | 51.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 54,497,260 | 1.2% | 52.3% |
| RETURN_CONST POP_TOP | 53,754,120 | 1.2% | 53.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 52,256,620 | 1.1% | 54.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 51,508,260 | 1.1% | 55.7% |
| LOAD_FAST RETURN_VALUE | 44,045,780 | 1.0% | 56.7% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 42,550,040 | 0.9% | 57.6% |
| STORE_ATTR_SLOT LOAD_CONST | 41,803,980 | 0.9% | 58.5% |
| RETURN_CONST INTERPRETER_EXIT | 38,818,440 | 0.8% | 59.3% |
| LOAD_FAST LOAD_ATTR | 38,079,140 | 0.8% | 60.2% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 38,071,000 | 0.8% | 61.0% |
| PUSH_NULL LOAD_FAST | 37,325,440 | 0.8% | 61.8% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 35,085,060 | 0.8% | 62.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 33,594,560 | 0.7% | 63.3% |
| CALL STORE_FAST | 33,592,920 | 0.7% | 64.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 30,606,160 | 0.7% | 64.7% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 30,605,880 | 0.7% | 65.3% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 29,860,260 | 0.6% | 66.0% |
| POP_TOP RETURN_CONST | 28,367,960 | 0.6% | 66.6% |
| STORE_ATTR_SLOT LOAD_FAST | 28,367,020 | 0.6% | 67.2% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 28,366,840 | 0.6% | 67.8% |
| POP_JUMP_IF_FALSE RETURN_CONST | 26,127,900 | 0.6% | 68.4% |
| RETURN_VALUE STORE_FAST | 25,383,280 | 0.5% | 68.9% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 25,383,180 | 0.5% | 69.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 25,381,200 | 0.5% | 70.0% |
| STORE_ATTR_SLOT RETURN_CONST | 24,634,560 | 0.5% | 70.6% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 24,634,360 | 0.5% | 71.1% |
| NOP LOAD_FAST | 21,651,120 | 0.5% | 71.6% |
| POP_TOP LOAD_CONST | 21,650,900 | 0.5% | 72.0% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 21,648,560 | 0.5% | 72.5% |
| BUILD_LIST LOAD_FAST | 21,648,560 | 0.5% | 73.0% |
| POP_TOP JUMP_BACKWARD | 21,648,240 | 0.5% | 73.4% |
| JUMP_BACKWARD FOR_ITER_RANGE | 21,648,200 | 0.5% | 73.9% |
| FOR_ITER_RANGE STORE_FAST | 21,648,200 | 0.5% | 74.4% |
| POP_JUMP_IF_FALSE LOAD_CONST | 20,906,000 | 0.5% | 74.8% |
| LOAD_ATTR PUSH_NULL | 20,902,740 | 0.5% | 75.3% |
| RETURN_VALUE TO_BOOL_BOOL | 20,902,400 | 0.5% | 75.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 20,902,120 | 0.5% | 76.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 20,901,880 | 0.5% | 76.6% |
| LIST_EXTEND CALL_INTRINSIC_1 | 20,901,840 | 0.5% | 77.1% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 19,408,840 | 0.4% | 77.5% |
| LOAD_CONST STORE_FAST | 17,925,120 | 0.4% | 77.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 17,915,720 | 0.4% | 78.3% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 17,174,040 | 0.4% | 78.7% |
| LOAD_FAST LOAD_CONST | 17,171,780 | 0.4% | 79.0% |
| STORE_FAST RETURN_CONST | 17,171,200 | 0.4% | 79.4% |
| RESUME_CHECK NOP | 17,169,980 | 0.4% | 79.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 17,169,840 | 0.4% | 80.1% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 17,169,760 | 0.4% | 80.5% |
| LOAD_FAST_LOAD_FAST CALL | 17,169,560 | 0.4% | 80.9% |
| CALL_FUNCTION_EX POP_TOP | 17,169,520 | 0.4% | 81.3% |
| GET_AWAITABLE LOAD_CONST | 17,169,520 | 0.4% | 81.6% |
| LOAD_ATTR_SLOT LOAD_ATTR | 17,169,460 | 0.4% | 82.0% |
| POP_TOP RESUME_CHECK | 17,169,360 | 0.4% | 82.4% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 17,169,360 | 0.4% | 82.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 17,169,340 | 0.4% | 83.1% |
| LOAD_ATTR_SLOT BUILD_LIST | 17,169,340 | 0.4% | 83.5% |
| LOAD_ATTR_SLOT LIST_EXTEND | 17,169,340 | 0.4% | 83.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 16,427,220 | 0.4% | 84.2% |
| PUSH_NULL CALL | 16,426,140 | 0.4% | 84.6% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 16,422,880 | 0.4% | 84.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 13,437,220 | 0.3% | 85.2% |
| LOAD_CONST CALL_KW | 13,436,960 | 0.3% | 85.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,436,880 | 0.3% | 85.8% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 13,436,680 | 0.3% | 86.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 13,436,640 | 0.3% | 86.4% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 12,692,420 | 0.3% | 86.6% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 12,690,920 | 0.3% | 86.9% |
| END_SEND POP_TOP | 12,690,560 | 0.3% | 87.2% |
| SEND_GEN POP_TOP | 12,690,420 | 0.3% | 87.5% |
| POP_JUMP_IF_NONE LOAD_FAST | 12,690,400 | 0.3% | 87.7% |
| LOAD_CONST SEND_GEN | 12,690,320 | 0.3% | 88.0% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 11,945,020 | 0.3% | 88.3% |
| YIELD_VALUE YIELD_VALUE | 11,944,080 | 0.3% | 88.5% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 11,944,040 | 0.3% | 88.8% |
| SEND_GEN RESUME_CHECK | 11,943,980 | 0.3% | 89.1% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 118,396,380 | 92.4% |
| POP_TOP | 4,478,960 | 3.5% |
| COPY_FREE_VARS | 3,732,660 | 2.9% |
| RETURN_GENERATOR | 1,492,960 | 1.2% |
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
| RETURN_CONST | 8,211,600 | 47.8% |
| RETURN_VALUE | 4,478,960 | 26.1% |
| SEND | 4,478,960 | 26.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 12,690,560 | 73.9% |
| LOAD_FAST | 3,732,480 | 21.7% |
| STORE_FAST | 746,480 | 4.3% |


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
| RETURN_VALUE | 83,310,940 | 65.0% |
| RETURN_CONST | 38,818,440 | 30.3% |
| YIELD_VALUE | 4,478,960 | 3.5% |
| RETURN_GENERATOR | 1,492,960 | 1.2% |


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
| RESUME_CHECK | 17,169,980 | 79.3% |
| STORE_FAST | 3,734,480 | 17.2% |
| STORE_ATTR_INSTANCE_VALUE | 746,460 | 3.4% |
| POP_TOP | 400 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,651,120 | 100.0% |
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
| RETURN_CONST | 53,754,120 | 35.1% |
| CALL_METHOD_DESCRIPTOR_O | 35,085,060 | 22.9% |
| CALL_FUNCTION_EX | 17,169,520 | 11.2% |
| END_SEND | 12,690,560 | 8.3% |
| SEND_GEN | 12,690,420 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 56,737,000 | 37.1% |
| RETURN_CONST | 28,367,960 | 18.5% |
| LOAD_CONST | 21,650,900 | 14.1% |
| JUMP_BACKWARD | 21,648,240 | 14.1% |
| RESUME_CHECK | 17,169,360 | 11.2% |


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
| LOAD_ATTR_MODULE | 54,497,260 | 68.2% |
| LOAD_ATTR | 20,902,740 | 26.2% |
| LOAD_FAST | 4,479,380 | 5.6% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,325,440 | 46.7% |
| LOAD_FAST_LOAD_FAST | 21,648,560 | 27.1% |
| CALL | 16,426,140 | 20.6% |
| LOAD_GLOBAL_MODULE | 3,732,440 | 4.7% |
| CALL_ALLOC_AND_ENTER_INIT | 746,440 | 0.9% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,943,840 | 69.6% |
| CALL_PY_WITH_DEFAULTS | 3,732,460 | 21.7% |
| CACHE | 1,492,960 | 8.7% |
| CALL | 120 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 11,197,600 | 65.2% |
| CALL | 4,478,920 | 26.1% |
| INTERPRETER_EXIT | 1,492,960 | 8.7% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 57,183,420 | 39.8% |
| LOAD_FAST | 44,045,780 | 30.6% |
| LOAD_ATTR_INSTANCE_VALUE | 29,860,260 | 20.8% |
| CALL_KW | 4,478,960 | 3.1% |
| CALL | 3,734,700 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 83,310,940 | 57.9% |
| STORE_FAST | 25,383,280 | 17.7% |
| TO_BOOL_BOOL | 20,902,400 | 14.5% |
| LOAD_FAST | 4,480,800 | 3.1% |
| POP_TOP | 4,479,120 | 3.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 40 | 66.7% |
| LOAD_FAST | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 33.3% |
| LOAD_FAST | 20 | 33.3% |
| STORE_SUBSCR_DICT | 20 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 11,199,440 | 99.9% |
| TO_BOOL | 3,800 | 0.0% |
| LOAD_ATTR | 800 | 0.0% |
| RETURN_VALUE | 480 | 0.0% |
| CALL | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,719,520 | 60.0% |
| POP_JUMP_IF_TRUE | 4,480,980 | 40.0% |
| TO_BOOL | 3,800 | 0.0% |
| TO_BOOL_BOOL | 1,000 | 0.0% |
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
| LOAD_FAST | 240 | 22.2% |
| LOAD_GLOBAL_MODULE | 180 | 16.7% |
| UNARY_INVERT | 160 | 14.8% |
| BINARY_OP | 160 | 14.8% |
| LOAD_CONST | 120 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 220 | 20.4% |
| BINARY_OP | 160 | 14.8% |
| COPY | 160 | 14.8% |
| LOAD_GLOBAL_MODULE | 120 | 11.1% |
| UNARY_INVERT | 80 | 7.4% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 17,169,340 | 79.3% |
| LOAD_FAST | 3,732,480 | 17.2% |
| STORE_ATTR_INSTANCE_VALUE | 746,680 | 3.4% |
| STORE_FAST | 1,840 | 0.0% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,648,560 | 100.0% |
| STORE_FAST | 1,840 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,732,480 | 100.0% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 3,732,480 | 100.0% |
| LOAD_FAST | 400 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 17,169,560 | 28.7% |
| PUSH_NULL | 16,426,140 | 27.5% |
| LOAD_ATTR | 8,959,720 | 15.0% |
| LOAD_FAST | 7,467,000 | 12.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,120 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 33,592,920 | 56.2% |
| POP_TOP | 8,958,640 | 15.0% |
| RESUME_CHECK | 8,212,040 | 13.7% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,100 | 7.5% |
| RETURN_VALUE | 3,734,700 | 6.3% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 17,169,360 | 82.1% |
| BUILD_MAP | 3,732,480 | 17.9% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 17,169,520 | 82.1% |
| STORE_FAST | 3,732,480 | 17.9% |
| COPY_FREE_VARS | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 20,901,840 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 17,169,360 | 82.1% |
| LOAD_CONST | 3,732,480 | 17.9% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,436,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,478,960 | 33.3% |
| STORE_FAST | 4,478,960 | 33.3% |
| RESUME_CHECK | 4,478,940 | 33.3% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |


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
| POP_JUMP_IF_FALSE | 3,733,000 | 100.0% |
| COMPARE_OP | 1,180 | 0.0% |
| COMPARE_OP_INT | 120 | 0.0% |
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
| CALL_PY_EXACT_ARGS | 3,733,100 | 50.0% |
| CACHE | 3,732,660 | 50.0% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,465,620 | 100.0% |
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
| RETURN_GENERATOR | 11,197,600 | 65.2% |
| LOAD_FAST | 3,732,480 | 21.7% |
| BEFORE_ASYNC_WITH | 746,480 | 4.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 746,460 | 4.3% |
| LOAD_ATTR_INSTANCE_VALUE | 746,460 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,169,520 | 100.0% |


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
| POP_TOP | 21,648,240 | 85.3% |
| POP_JUMP_IF_FALSE | 3,734,200 | 14.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 21,648,200 | 85.3% |
| LOAD_FAST | 3,734,180 | 14.7% |
| FOR_ITER | 40 | 0.0% |
| FOR_ITER_TUPLE | 20 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 16,422,880 | 100.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 11,944,040 | 72.7% |
| SEND | 4,479,000 | 27.3% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,482,880 | 100.0% |
| POP_JUMP_IF_FALSE | 160 | 0.0% |
| POP_TOP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,481,200 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 1,880 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_FAST_CHECK | 20 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 17,169,340 | 82.1% |
| LOAD_FAST | 3,732,480 | 17.9% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 20,901,840 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,079,140 | 67.1% |
| LOAD_ATTR_SLOT | 17,169,460 | 30.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,493,540 | 2.6% |
| LOAD_ATTR | 17,480 | 0.0% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 20,902,740 | 36.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 13,436,680 | 23.7% |
| CALL | 8,959,720 | 15.8% |
| LOAD_FAST | 8,212,560 | 14.5% |
| TO_BOOL_NONE | 4,478,920 | 7.9% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 41,803,980 | 27.2% |
| POP_TOP | 21,650,900 | 14.1% |
| POP_JUMP_IF_FALSE | 20,906,000 | 13.6% |
| LOAD_FAST | 17,171,780 | 11.2% |
| GET_AWAITABLE | 17,169,520 | 11.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 85,850,020 | 55.8% |
| STORE_FAST | 17,925,120 | 11.7% |
| CALL_KW | 13,436,960 | 8.7% |
| SEND_GEN | 12,690,320 | 8.3% |
| COMPARE_OP_INT | 4,481,160 | 2.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 7,465,540 | 100.0% |
| LOAD_GLOBAL | 240 | 0.0% |
| STORE_FAST | 160 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,465,780 | 100.0% |
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
| POP_JUMP_IF_FALSE | 178,119,180 | 19.1% |
| RESUME_CHECK | 139,600,520 | 14.9% |
| STORE_FAST | 98,551,640 | 10.6% |
| LOAD_CONST | 85,850,020 | 9.2% |
| LOAD_ATTR_SLOT | 60,916,020 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 260,679,640 | 27.9% |
| LOAD_ATTR_INSTANCE_VALUE | 204,560,400 | 21.9% |
| STORE_ATTR_SLOT | 73,903,440 | 7.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 62,711,560 | 6.7% |
| LOAD_GLOBAL_MODULE | 60,917,920 | 6.5% |


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
| STORE_ATTR_SLOT | 51,508,260 | 34.5% |
| LOAD_FAST_LOAD_FAST | 25,381,200 | 17.0% |
| PUSH_NULL | 21,648,560 | 14.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 17,915,720 | 12.0% |
| POP_JUMP_IF_NOT_NONE | 13,436,880 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 72,410,040 | 48.5% |
| LOAD_FAST_LOAD_FAST | 25,381,200 | 17.0% |
| LOAD_FAST | 17,169,840 | 11.5% |
| CALL | 17,169,560 | 11.5% |
| LOAD_CONST | 8,957,920 | 6.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 560 | 12.6% |
| RESUME_CHECK | 540 | 12.1% |
| POP_TOP | 500 | 11.2% |
| LOAD_FAST | 500 | 11.2% |
| POP_JUMP_IF_FALSE | 460 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,500 | 33.6% |
| LOAD_ATTR | 940 | 21.1% |
| LOAD_GLOBAL_BUILTIN | 660 | 14.8% |
| LOAD_FAST | 340 | 7.6% |
| CALL | 300 | 6.7% |


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
| TO_BOOL_BOOL | 181,851,120 | 72.2% |
| TO_BOOL_NONE | 42,550,040 | 16.9% |
| TO_BOOL_LIST | 8,961,660 | 3.6% |
| TO_BOOL | 6,719,520 | 2.7% |
| COMPARE_OP_INT | 4,483,080 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 178,119,180 | 70.7% |
| RETURN_CONST | 26,127,900 | 10.4% |
| LOAD_CONST | 20,906,000 | 8.3% |
| LOAD_GLOBAL_MODULE | 19,408,840 | 7.7% |
| JUMP_BACKWARD | 3,734,200 | 1.5% |


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
| LOAD_FAST | 33,594,560 | 83.3% |
| LOAD_ATTR_INSTANCE_VALUE | 6,718,340 | 16.7% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,436,880 | 33.3% |
| LOAD_FAST | 12,692,420 | 31.5% |
| LOAD_GLOBAL_MODULE | 8,958,240 | 22.2% |
| RETURN_CONST | 4,478,880 | 11.1% |
| LOAD_CONST | 746,500 | 1.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 12,690,920 | 73.9% |
| TO_BOOL | 4,480,980 | 26.1% |
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
| POP_TOP | 28,367,960 | 27.9% |
| POP_JUMP_IF_FALSE | 26,127,900 | 25.7% |
| STORE_ATTR_SLOT | 24,634,560 | 24.3% |
| STORE_FAST | 17,171,200 | 16.9% |
| POP_JUMP_IF_NOT_NONE | 4,478,880 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 53,754,120 | 52.9% |
| INTERPRETER_EXIT | 38,818,440 | 38.2% |
| END_SEND | 8,211,600 | 8.1% |
| EXIT_INIT_CHECK | 746,460 | 0.7% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,479,200 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 4,479,000 | 50.0% |
| SEND | 2,580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 4,478,960 | 50.0% |
| YIELD_VALUE | 4,478,960 | 50.0% |
| SEND | 2,580 | 0.0% |
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
| CALL | 33,592,920 | 25.4% |
| RETURN_VALUE | 25,383,280 | 19.2% |
| FOR_ITER_RANGE | 21,648,200 | 16.4% |
| LOAD_CONST | 17,925,120 | 13.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,169,340 | 13.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,551,640 | 74.6% |
| RETURN_CONST | 17,171,200 | 13.0% |
| JUMP_FORWARD | 4,482,880 | 3.4% |
| NOP | 3,734,480 | 2.8% |
| LOAD_FAST_LOAD_FAST | 3,732,800 | 2.8% |


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
| YIELD_VALUE | 11,944,080 | 72.7% |
| SEND | 4,478,960 | 27.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 11,944,080 | 72.7% |
| INTERPRETER_EXIT | 4,478,960 | 27.3% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,100 | 55.6% |
| CACHE | 340 | 17.2% |
| COPY_FREE_VARS | 240 | 12.1% |
| POP_TOP | 160 | 8.1% |
| SEND_GEN | 100 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 940 | 47.5% |
| LOAD_GLOBAL | 560 | 28.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 160 | 8.1% |
| LOAD_CONST | 140 | 7.1% |
| NOP | 100 | 5.1% |


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
| LOAD_CONST | 40 | 66.7% |
| BINARY_OP | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 60 | 100.0% |


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
| LOAD_CONST | 3,732,680 | 100.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,732,540 | 100.0% |
| LOAD_ATTR_SLOT | 160 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


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
| LOAD_CONST | 746,440 | 98.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 1.9% |
| PUSH_NULL | 40 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 746,460 | 98.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 1.9% |
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
| LOAD_FAST | 3,732,440 | 100.0% |
| LOAD_CONST | 180 | 0.0% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,732,460 | 100.0% |
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
| LOAD_FAST | 3,732,480 | 50.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,732,440 | 50.0% |
| CALL | 80 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,732,460 | 50.0% |
| TO_BOOL_BOOL | 3,732,440 | 50.0% |
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
| LOAD_ATTR_METHOD_NO_DICT | 17,169,760 | 56.1% |
| LOAD_ATTR | 13,436,680 | 43.9% |
| CALL | 380 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 17,169,340 | 56.1% |
| TO_BOOL_BOOL | 13,436,640 | 43.9% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |
| CALL | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,605,880 | 87.2% |
| CALL | 4,479,100 | 12.8% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 35,085,060 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 58,230,960 | 53.8% |
| LOAD_ATTR_METHOD_NO_DICT | 20,901,880 | 19.3% |
| LOAD_FAST | 17,174,040 | 15.9% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 4.1% |
| LOAD_SUPER_ATTR_METHOD | 3,732,640 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 92,576,140 | 85.5% |
| RETURN_GENERATOR | 11,943,840 | 11.0% |
| COPY_FREE_VARS | 3,733,100 | 3.4% |


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
| LOAD_ATTR_SLOT | 57,183,400 | 93.9% |
| LOAD_FAST | 3,732,520 | 6.1% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 57,183,420 | 93.9% |
| POP_JUMP_IF_FALSE | 3,732,680 | 6.1% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,481,160 | 100.0% |
| LOAD_GLOBAL_MODULE | 1,800 | 0.0% |
| COMPARE_OP | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,483,080 | 100.0% |


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
| JUMP_BACKWARD | 21,648,200 | 96.7% |
| GET_ITER | 748,280 | 3.3% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 21,648,200 | 96.7% |
| LOAD_CONST | 748,320 | 3.3% |


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
| LOAD_FAST | 204,560,400 | 97.9% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 2.1% |
| LOAD_ATTR | 2,000 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 70,918,520 | 33.9% |
| LOAD_ATTR_METHOD_NO_DICT | 52,256,620 | 25.0% |
| RETURN_VALUE | 29,860,260 | 14.3% |
| TO_BOOL | 11,199,440 | 5.4% |
| TO_BOOL_LIST | 8,961,540 | 4.3% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 52,256,620 | 71.4% |
| LOAD_FAST | 20,902,120 | 28.6% |
| LOAD_ATTR | 580 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 320 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,606,160 | 41.8% |
| CALL_PY_EXACT_ARGS | 20,901,880 | 28.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 17,169,760 | 23.5% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 6.1% |
| LOAD_FAST_LOAD_FAST | 1,960 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,711,560 | 67.7% |
| LOAD_ATTR_SLOT | 24,634,360 | 26.6% |
| LOAD_ATTR_INSTANCE_VALUE | 5,227,400 | 5.6% |
| LOAD_ATTR | 1,240 | 0.0% |
| RETURN_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 58,230,960 | 62.9% |
| LOAD_FAST_LOAD_FAST | 17,915,720 | 19.4% |
| LOAD_FAST | 16,427,220 | 17.7% |
| CALL | 720 | 0.0% |
| LOAD_CONST | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 58,229,320 | 100.0% |
| LOAD_ATTR | 960 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 54,497,260 | 93.6% |
| LOAD_FAST_LOAD_FAST | 3,732,460 | 6.4% |
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
| LOAD_FAST | 260,679,640 | 100.0% |
| LOAD_ATTR_SLOT | 1,440 | 0.0% |
| LOAD_ATTR | 500 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,916,020 | 23.4% |
| COMPARE_OP_FLOAT | 57,183,400 | 21.9% |
| TO_BOOL_NONE | 38,071,000 | 14.6% |
| TO_BOOL_BOOL | 28,366,840 | 10.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 24,634,360 | 9.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60,918,720 | 92.1% |
| POP_TOP | 3,732,640 | 5.6% |
| STORE_FAST | 748,300 | 1.1% |
| STORE_ATTR_INSTANCE_VALUE | 746,580 | 1.1% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,192,000 | 86.5% |
| LOAD_DEREF | 7,465,540 | 11.3% |
| CALL_BUILTIN_CLASS | 746,660 | 1.1% |
| LOAD_GLOBAL_MODULE | 746,480 | 1.1% |
| CALL_ISINSTANCE | 380 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,917,920 | 49.0% |
| RESUME_CHECK | 25,383,180 | 20.4% |
| POP_JUMP_IF_FALSE | 19,408,840 | 15.6% |
| POP_JUMP_IF_NOT_NONE | 8,958,240 | 7.2% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 58,229,320 | 46.8% |
| CALL_ISINSTANCE | 57,183,440 | 46.0% |
| LOAD_FAST_LOAD_FAST | 4,479,200 | 3.6% |
| CALL_PY_WITH_DEFAULTS | 3,732,440 | 3.0% |
| CALL_BUILTIN_CLASS | 746,440 | 0.6% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,465,320 | 100.0% |
| LOAD_SUPER_ATTR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,732,640 | 50.0% |
| LOAD_FAST_LOAD_FAST | 3,732,520 | 50.0% |
| LOAD_FAST | 260 | 0.0% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 118,396,380 | 45.4% |
| CALL_PY_EXACT_ARGS | 92,576,140 | 35.5% |
| POP_TOP | 17,169,360 | 6.6% |
| SEND_GEN | 11,943,980 | 4.6% |
| CALL | 8,212,040 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,600,520 | 53.5% |
| LOAD_GLOBAL_BUILTIN | 60,918,720 | 23.3% |
| LOAD_GLOBAL_MODULE | 25,383,180 | 9.7% |
| NOP | 17,169,980 | 6.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 16,422,880 | 6.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,690,320 | 51.5% |
| JUMP_BACKWARD_NO_INTERRUPT | 11,944,040 | 48.5% |
| SEND | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 12,690,420 | 51.5% |
| RESUME_CHECK | 11,943,980 | 48.5% |
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
| LOAD_FAST | 73,903,440 | 50.5% |
| LOAD_FAST_LOAD_FAST | 72,410,040 | 49.5% |
| STORE_ATTR_SLOT | 1,120 | 0.0% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 51,508,260 | 35.2% |
| LOAD_CONST | 41,803,980 | 28.6% |
| LOAD_FAST | 28,367,020 | 19.4% |
| RETURN_CONST | 24,634,560 | 16.8% |
| STORE_ATTR_SLOT | 1,120 | 0.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 40 | 66.7% |
| STORE_SUBSCR | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 70,918,520 | 36.5% |
| CALL_ISINSTANCE | 57,183,860 | 29.4% |
| LOAD_ATTR_SLOT | 28,366,840 | 14.6% |
| RETURN_VALUE | 20,902,400 | 10.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 13,436,640 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 181,851,120 | 93.5% |
| POP_JUMP_IF_TRUE | 12,690,920 | 6.5% |
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
| LOAD_ATTR_INSTANCE_VALUE | 8,961,540 | 100.0% |
| TO_BOOL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,961,660 | 100.0% |


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
|     deferred | 780 | 0.0% |
|          hit | 8,213,380 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 46.7% |
| Failure | 160 | 53.3% |

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
|     deferred | 60,473,900 | 19.5% |
|          hit | 249,055,480 | 80.5% |
|         miss | 761,180 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,280 | 49.1% |
| Failure | 17,900 | 50.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| no dict | 4,600 | 25.7% |
| meth descr method fastcall keywords | 4,100 | 22.9% |
| cfunc noargs | 3,840 | 21.5% |
| code complex parameters | 2,440 | 13.6% |
| class no vectorcall | 1,340 | 7.5% |
| other | 1,280 | 7.2% |
| class mutable | 80 | 0.4% |
| metaclass | 60 | 0.3% |
| wrong number arguments | 40 | 0.2% |
| cfunc varargs | 40 | 0.2% |
| operator wrapper | 40 | 0.2% |
| cmethod | 20 | 0.1% |
| cfunc varargs keywords | 20 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,733,040 | 5.4% |
|          hit | 65,399,200 | 94.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 13.2% |
| Failure | 1,180 | 86.8% |

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
|     deferred | 260 | 0.0% |
|          hit | 22,400,260 | 100.0% |

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
|     deferred | 56,832,140 | 7.6% |
|          hit | 693,595,340 | 92.4% |
|         miss | 93,440 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,080 | 29.9% |
| Failure | 16,620 | 70.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 8,200 | 49.3% |
| method | 6,900 | 41.5% |
| class attr descriptor | 1,280 | 7.7% |
| not managed dict | 140 | 0.8% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.2% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,380 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 190,527,120 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,160 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 7,465,540 | 100.0% |

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
|     deferred | 8,958,060 | 26.7% |
|          hit | 24,634,500 | 73.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 5.1% |
| Failure | 2,580 | 94.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 2,580 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 60,460 | 0.0% |
|          hit | 158,201,980 | 100.0% |
|         miss | 59,600 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,740 | 96.5% |
| Failure | 100 | 3.5% |

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
|     deferred | 40 | 33.3% |
|          hit | 60 | 50.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,200,540 | 4.4% |
|          hit | 246,056,000 | 95.6% |

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
| Basic | 2,229,961,040 | 48.2% |
| Not specialized | 463,378,200 | 10.0% |
| Specialized hits | 1,930,197,097 | 41.7% |
| Specialized misses | 988,603 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 60,473,900 | 42.8% |
| LOAD_ATTR | 56,832,140 | 40.2% |
| TO_BOOL | 11,200,540 | 7.9% |
| SEND | 8,958,060 | 6.3% |
| COMPARE_OP | 3,733,040 | 2.6% |
| STORE_ATTR | 60,460 | 0.0% |
| LOAD_GLOBAL | 2,380 | 0.0% |
| BINARY_OP | 780 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 760,800 | 71.6% |
| LOAD_ATTR_SLOT | 76,480 | 7.2% |
| RESUME | 74,303 | 7.0% |
| RESUME_CHECK | 74,303 | 7.0% |
| STORE_ATTR_SLOT | 59,600 | 5.6% |
| LOAD_ATTR_METHOD_NO_DICT | 16,960 | 1.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 260 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |
| CACHE | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 128,101,300 | 46.1% |
| Calls to Python functions inlined | 150,059,640 | 53.9% |
| Calls via PyEval_EvalFrame (total) | 128,101,300 | 46.1% |
| Calls via PyEval_EvalFrame (vector) | 119,143,380 | 42.8% |
| Calls via PyEval_EvalFrame (generator) | 8,957,920 | 3.2% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 119,143,380 | 42.8% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 57,183,440 | 20.6% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 1.6% |
| Calls via PyEval_EvalFrame (method) | 26,873,760 | 9.7% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 113,478,980 | 40.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 106,777,276 | 38.1% |
| Frees to freelist | 107,301,360 |  |
| Allocations | 173,513,771 | 61.9% |
| Allocations to 512 bytes | 172,651,702 | 61.6% |
| Allocations to 4 kbytes | 861,960 | 0.3% |
| Allocations over 4 kbytes | 109 | 0.0% |
| Frees | 173,429,018 |  |
| New values | 440 |  |
| Interpreter increfs | 2,577,421,880 | 79.0% |
| Interpreter decrefs | 2,698,215,936 | 77.1% |
| Increfs | 686,950,373 | 21.0% |
| Decrefs | 802,003,485 | 22.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 83,787,929 |  |
| Method cache misses | 4,251 |  |
| Method cache collisions | 4,037 |  |
| Method cache dunder hits | 75,847,229 |  |
| Method cache dunder misses | 431 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 94,971 | 2,040 | 677,951,308 |
| 1 | 8,640 | 0 | 731,825,706 |
| 2 | 660 | 0 | 2,419,256,696 |


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
