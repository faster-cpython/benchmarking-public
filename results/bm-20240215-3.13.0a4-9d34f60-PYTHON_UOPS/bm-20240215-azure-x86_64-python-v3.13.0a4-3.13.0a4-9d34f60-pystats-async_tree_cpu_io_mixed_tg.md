
# Pystats results

- benchmark: async_tree_cpu_io_mixed_tg
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 408,902,880 | 19.9% | 19.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 126,218,460 | 6.1% | 26.1% |  |
| POP_JUMP_IF_FALSE | 112,113,500 | 5.5% | 31.5% |  |
| RESUME_CHECK | 107,990,220 | 5.3% | 36.8% | 0.0% |
| LOAD_FAST_LOAD_FAST | 96,951,300 | 4.7% | 41.5% |  |
| POP_TOP | 90,941,420 | 4.4% | 45.9% |  |
| LOAD_CONST | 90,221,380 | 4.4% | 50.3% |  |
| STORE_ATTR_SLOT | 71,764,340 | 3.5% | 53.8% | 3.5% |
| STORE_FAST | 70,281,940 | 3.4% | 57.2% |  |
| TO_BOOL_BOOL | 64,643,280 | 3.1% | 60.4% | 0.0% |
| RETURN_VALUE | 60,911,540 | 3.0% | 63.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 57,335,820 | 2.8% | 66.1% |  |
| RETURN_CONST | 55,279,340 | 2.7% | 68.8% |  |
| LOAD_GLOBAL_MODULE | 48,968,400 | 2.4% | 71.2% |  |
| CALL_PY_EXACT_ARGS | 48,949,500 | 2.4% | 73.6% |  |
| INTERPRETER_EXIT | 48,196,060 | 2.3% | 76.0% |  |
| CALL | 38,673,120 | 1.9% | 77.8% |  |
| LOAD_ATTR_SLOT | 36,319,240 | 1.8% | 79.6% | 1.0% |
| PUSH_NULL | 33,480,200 | 1.6% | 81.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 31,744,900 | 1.5% | 82.8% | 0.0% |
| LOAD_ATTR | 31,017,120 | 1.5% | 84.3% |  |
| POP_JUMP_IF_NOT_NONE | 28,008,680 | 1.4% | 85.7% |  |
| CALL_METHOD_DESCRIPTOR_O | 27,809,840 | 1.4% | 87.0% | 0.0% |
| LOAD_ATTR_MODULE | 26,530,820 | 1.3% | 88.3% |  |
| TO_BOOL_NONE | 24,836,040 | 1.2% | 89.5% | 0.0% |
| POP_JUMP_IF_NONE | 13,437,680 | 0.7% | 90.2% |  |
| COMPARE_OP_INT | 12,366,200 | 0.6% | 90.8% |  |
| RETURN_GENERATOR | 11,951,360 | 0.6% | 91.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 11,946,640 | 0.6% | 91.9% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,764,760 | 0.6% | 92.5% | 0.0% |
| TO_BOOL | 11,205,700 | 0.5% | 93.0% |  |
| CALL_FUNCTION_EX | 10,272,360 | 0.5% | 93.6% |  |
| ENTER_EXECUTOR | 10,197,460 | 0.5% | 94.0% |  |
| POP_JUMP_IF_TRUE | 10,087,300 | 0.5% | 94.5% |  |
| CALL_BUILTIN_O | 9,937,060 | 0.5% | 95.0% |  |
| CALL_KW | 9,893,720 | 0.5% | 95.5% |  |
| SEND_GEN | 8,975,840 | 0.4% | 95.9% |  |
| END_SEND | 8,408,120 | 0.4% | 96.4% |  |
| GET_AWAITABLE | 8,408,120 | 0.4% | 96.8% |  |
| BINARY_OP_SUBTRACT_INT | 6,347,220 | 0.3% | 97.1% |  |
| COMPARE_OP_FLOAT | 5,813,920 | 0.3% | 97.4% |  |
| TO_BOOL_LIST | 5,229,600 | 0.3% | 97.6% |  |
| FOR_ITER_RANGE | 5,229,280 | 0.3% | 97.9% |  |
| JUMP_FORWARD | 4,483,220 | 0.2% | 98.1% |  |
| JUMP_BACKWARD | 4,481,680 | 0.2% | 98.3% |  |
| LOAD_GLOBAL_BUILTIN | 3,962,420 | 0.2% | 98.5% | 0.0% |
| BINARY_OP_ADD_INT | 3,736,660 | 0.2% | 98.7% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,629,160 | 0.1% | 98.8% | 28.9% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,439,320 | 0.1% | 98.9% |  |
| YIELD_VALUE | 2,439,320 | 0.1% | 99.0% |  |
| CALL_ISINSTANCE | 2,081,380 | 0.1% | 99.1% |  |
| CALL_PY_WITH_DEFAULTS | 2,057,900 | 0.1% | 99.2% |  |
| SEND | 1,872,600 | 0.1% | 99.3% |  |
| LOAD_ATTR_CLASS | 1,868,440 | 0.1% | 99.4% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,681,060 | 0.1% | 99.5% |  |
| CALL_BUILTIN_CLASS | 1,495,460 | 0.1% | 99.6% |  |
| NOP | 1,130,440 | 0.1% | 99.6% |  |
| BUILD_LIST | 1,129,160 | 0.1% | 99.7% |  |
| GET_ITER | 752,260 | 0.0% | 99.7% |  |
| BEFORE_ASYNC_WITH | 746,480 | 0.0% | 99.8% |  |
| EXIT_INIT_CHECK | 746,460 | 0.0% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 746,460 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 746,460 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 380,600 | 0.0% | 99.9% |  |
| LIST_EXTEND | 380,600 | 0.0% | 99.9% |  |
| LOAD_DEREF | 379,700 | 0.0% | 99.9% |  |
| COPY_FREE_VARS | 379,540 | 0.0% | 99.9% |  |
| LOAD_SUPER_ATTR_METHOD | 379,060 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 191,040 | 0.0% | 100.0% |  |
| COMPARE_OP | 190,340 | 0.0% | 100.0% |  |
| BUILD_MAP | 189,640 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 189,460 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,820 | 0.0% | 100.0% |  |
| STORE_ATTR | 3,700 | 0.0% | 100.0% |  |
| FOR_ITER_LIST | 3,700 | 0.0% | 100.0% |  |
| COPY | 2,580 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| RESUME | 2,080 | 0.0% | 100.0% | 1,351.0% |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 121,737,160 | 5.9% | 5.9% |
| RESUME_CHECK LOAD_FAST | 82,912,820 | 4.0% | 10.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 78,948,000 | 3.8% | 13.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 59,038,780 | 2.9% | 16.7% |
| STORE_FAST LOAD_FAST | 48,567,080 | 2.4% | 19.1% |
| CACHE RESUME_CHECK | 42,034,380 | 2.0% | 21.1% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 40,520,880 | 2.0% | 23.1% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 39,777,120 | 1.9% | 25.0% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 39,767,520 | 1.9% | 26.9% |
| LOAD_CONST LOAD_FAST | 39,600,940 | 1.9% | 28.9% |
| POP_TOP LOAD_FAST | 39,021,280 | 1.9% | 30.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 38,490,740 | 1.9% | 32.6% |
| LOAD_FAST LOAD_ATTR_SLOT | 36,122,320 | 1.8% | 34.4% |
| LOAD_FAST RETURN_VALUE | 33,519,620 | 1.6% | 36.0% |
| LOAD_FAST STORE_ATTR_SLOT | 31,195,800 | 1.5% | 37.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 30,248,820 | 1.5% | 39.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 29,885,000 | 1.5% | 40.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 29,494,980 | 1.4% | 41.9% |
| LOAD_FAST LOAD_ATTR | 29,317,740 | 1.4% | 43.4% |
| RETURN_CONST INTERPRETER_EXIT | 28,188,720 | 1.4% | 44.7% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 27,809,820 | 1.4% | 46.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 26,529,680 | 1.3% | 47.4% |
| LOAD_ATTR_MODULE PUSH_NULL | 26,340,920 | 1.3% | 48.7% |
| RETURN_CONST POP_TOP | 25,408,200 | 1.2% | 49.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 25,011,780 | 1.2% | 51.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 24,836,020 | 1.2% | 52.3% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 23,330,640 | 1.1% | 53.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 21,289,920 | 1.0% | 54.5% |
| STORE_ATTR_SLOT LOAD_CONST | 20,544,540 | 1.0% | 55.5% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 20,354,800 | 1.0% | 56.5% |
| CALL STORE_FAST | 19,420,080 | 0.9% | 57.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 18,679,140 | 0.9% | 58.3% |
| RETURN_VALUE INTERPRETER_EXIT | 17,578,660 | 0.9% | 59.2% |
| RETURN_VALUE STORE_FAST | 16,621,880 | 0.8% | 60.0% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 16,240,780 | 0.8% | 60.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 15,687,300 | 0.8% | 61.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 15,498,180 | 0.8% | 62.3% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,751,480 | 0.7% | 63.0% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,562,080 | 0.7% | 63.7% |
| POP_TOP RETURN_CONST | 14,005,760 | 0.7% | 64.4% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 13,824,120 | 0.7% | 65.1% |
| LOAD_FAST LOAD_CONST | 13,821,860 | 0.7% | 65.8% |
| POP_JUMP_IF_NONE LOAD_FAST | 12,690,400 | 0.6% | 66.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 12,366,200 | 0.6% | 67.0% |
| POP_TOP RESUME_CHECK | 11,951,180 | 0.6% | 67.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 11,945,020 | 0.6% | 68.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 11,209,040 | 0.5% | 68.7% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL | 11,199,400 | 0.5% | 69.2% |
| POP_TOP LOAD_CONST | 11,021,180 | 0.5% | 69.8% |
| LOAD_CONST STORE_FAST | 10,838,640 | 0.5% | 70.3% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 10,826,240 | 0.5% | 70.8% |
| STORE_ATTR_SLOT LOAD_FAST | 10,462,060 | 0.5% | 71.3% |
| STORE_ATTR_SLOT RETURN_CONST | 10,461,600 | 0.5% | 71.9% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 0.5% | 72.4% |
| POP_JUMP_IF_FALSE LOAD_CONST | 10,278,000 | 0.5% | 72.9% |
| RETURN_VALUE TO_BOOL_BOOL | 10,272,680 | 0.5% | 73.4% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 10,268,900 | 0.5% | 73.9% |
| STORE_FAST RETURN_CONST | 10,084,720 | 0.5% | 74.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 10,083,360 | 0.5% | 74.8% |
| LOAD_FAST_LOAD_FAST CALL | 10,083,080 | 0.5% | 75.3% |
| CALL_FUNCTION_EX POP_TOP | 10,083,040 | 0.5% | 75.8% |
| POP_TOP ENTER_EXECUTOR | 10,082,540 | 0.5% | 76.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,893,900 | 0.5% | 76.8% |
| LOAD_CONST CALL_KW | 9,893,720 | 0.5% | 77.3% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 9,893,640 | 0.5% | 77.8% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 9,893,440 | 0.5% | 78.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 9,893,400 | 0.5% | 78.7% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 9,891,520 | 0.5% | 79.2% |
| PUSH_NULL CALL | 9,528,820 | 0.5% | 79.7% |
| LOAD_ATTR CALL | 8,959,720 | 0.4% | 80.1% |
| GET_AWAITABLE LOAD_CONST | 8,408,120 | 0.4% | 80.5% |
| LOAD_CONST COMPARE_OP_INT | 8,217,720 | 0.4% | 80.9% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,211,840 | 0.4% | 81.3% |
| LOAD_FAST CALL_BUILTIN_O | 8,072,260 | 0.4% | 81.7% |
| CALL_BUILTIN_O STORE_FAST | 7,883,580 | 0.4% | 82.1% |
| SEND_GEN POP_TOP | 7,472,240 | 0.4% | 82.5% |
| LOAD_CONST SEND_GEN | 7,472,120 | 0.4% | 82.8% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 7,283,280 | 0.4% | 83.2% |
| LOAD_FAST PUSH_NULL | 6,757,640 | 0.3% | 83.5% |
| TO_BOOL POP_JUMP_IF_FALSE | 6,719,500 | 0.3% | 83.8% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NOT_NONE | 6,718,340 | 0.3% | 84.2% |
| RETURN_VALUE END_SEND | 6,536,520 | 0.3% | 84.5% |
| RETURN_GENERATOR GET_AWAITABLE | 5,979,440 | 0.3% | 84.8% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 5,605,940 | 0.3% | 85.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 5,605,420 | 0.3% | 85.3% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 5,604,440 | 0.3% | 85.6% |
| END_SEND POP_TOP | 5,604,080 | 0.3% | 85.9% |
| CALL POP_TOP | 5,415,400 | 0.3% | 86.1% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 5,236,280 | 0.3% | 86.4% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 5,229,600 | 0.3% | 86.6% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_LIST | 5,229,500 | 0.3% | 86.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 5,227,400 | 0.3% | 87.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 5,226,060 | 0.3% | 87.4% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 5,225,580 | 0.3% | 87.7% |
| PUSH_NULL LOAD_FAST | 4,720,740 | 0.2% | 87.9% |
| LOAD_ATTR LOAD_FAST | 4,669,380 | 0.2% | 88.1% |
| CALL RESUME_CHECK | 4,668,780 | 0.2% | 88.3% |
| STORE_FAST JUMP_FORWARD | 4,482,960 | 0.2% | 88.6% |
| JUMP_FORWARD LOAD_FAST | 4,481,280 | 0.2% | 88.8% |
| TO_BOOL POP_JUMP_IF_TRUE | 4,480,980 | 0.2% | 89.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 42,034,380 | 87.2% |
| POP_TOP | 4,478,960 | 9.3% |
| RETURN_GENERATOR | 1,492,960 | 3.1% |
| COPY_FREE_VARS | 189,420 | 0.4% |
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
| RETURN_VALUE | 6,536,520 | 77.7% |
| RETURN_CONST | 935,880 | 11.1% |
| SEND | 935,720 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,604,080 | 66.7% |
| RETURN_VALUE | 1,868,320 | 22.2% |
| STORE_FAST | 746,480 | 8.9% |
| LOAD_FAST | 189,240 | 2.3% |


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
| RETURN_CONST | 28,188,720 | 58.5% |
| RETURN_VALUE | 17,578,660 | 36.5% |
| RETURN_GENERATOR | 1,492,960 | 3.1% |
| YIELD_VALUE | 935,720 | 1.9% |


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
| STORE_ATTR_INSTANCE_VALUE | 746,460 | 66.0% |
| RESUME_CHECK | 191,980 | 17.0% |
| STORE_FAST | 191,240 | 16.9% |
| POP_TOP | 400 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,129,880 | 100.0% |
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
| CALL_METHOD_DESCRIPTOR_O | 27,809,820 | 30.6% |
| RETURN_CONST | 25,408,200 | 27.9% |
| CALL_FUNCTION_EX | 10,083,040 | 11.1% |
| SEND_GEN | 7,472,240 | 8.2% |
| END_SEND | 5,604,080 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,021,280 | 42.9% |
| RETURN_CONST | 14,005,760 | 15.4% |
| RESUME_CHECK | 11,951,180 | 13.1% |
| LOAD_CONST | 11,021,180 | 12.1% |
| ENTER_EXECUTOR | 10,082,540 | 11.1% |


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
| LOAD_ATTR_MODULE | 26,340,920 | 78.7% |
| LOAD_FAST | 6,757,640 | 20.2% |
| LOAD_ATTR | 381,560 | 1.1% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,562,080 | 43.5% |
| CALL | 9,528,820 | 28.5% |
| LOAD_FAST | 4,720,740 | 14.1% |
| LOAD_GLOBAL_MODULE | 2,053,320 | 6.1% |
| LOAD_CONST | 1,868,560 | 5.6% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,268,900 | 85.9% |
| CACHE | 1,492,960 | 12.5% |
| CALL_PY_WITH_DEFAULTS | 189,220 | 1.6% |
| CALL | 140 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 5,979,440 | 50.0% |
| CALL | 4,478,920 | 37.5% |
| INTERPRETER_EXIT | 1,492,960 | 12.5% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,519,620 | 55.0% |
| LOAD_ATTR_INSTANCE_VALUE | 15,687,300 | 25.8% |
| COMPARE_OP_FLOAT | 2,080,860 | 3.4% |
| RETURN_VALUE | 1,868,800 | 3.1% |
| END_SEND | 1,868,320 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 17,578,660 | 28.9% |
| STORE_FAST | 16,621,880 | 27.3% |
| TO_BOOL_BOOL | 10,272,680 | 16.9% |
| END_SEND | 6,536,520 | 10.7% |
| POP_TOP | 4,479,120 | 7.4% |


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
| STORE_ATTR_INSTANCE_VALUE | 746,680 | 66.1% |
| LOAD_ATTR_SLOT | 191,340 | 16.9% |
| LOAD_FAST | 189,240 | 16.8% |
| STORE_FAST | 1,840 | 0.2% |
| STORE_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,127,320 | 99.8% |
| STORE_FAST | 1,840 | 0.2% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 189,240 | 99.8% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.1% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 189,240 | 99.8% |
| LOAD_FAST | 400 | 0.2% |


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
| LOAD_FAST_LOAD_FAST | 10,083,080 | 26.1% |
| PUSH_NULL | 9,528,820 | 24.6% |
| LOAD_ATTR | 8,959,720 | 23.2% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,120 | 11.6% |
| RETURN_GENERATOR | 4,478,920 | 11.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 19,420,080 | 50.2% |
| POP_TOP | 5,415,400 | 14.0% |
| RESUME_CHECK | 4,668,780 | 12.1% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,100 | 11.6% |
| LOAD_GLOBAL_MODULE | 3,732,500 | 9.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 9,891,520 | 96.3% |
| CALL_INTRINSIC_1 | 191,360 | 1.9% |
| BUILD_MAP | 189,240 | 1.8% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,083,040 | 98.2% |
| STORE_FAST | 189,240 | 1.8% |
| COPY_FREE_VARS | 80 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 380,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 191,360 | 50.3% |
| LOAD_CONST | 189,240 | 49.7% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,893,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 45.3% |
| RESUME_CHECK | 4,478,940 | 45.3% |
| RETURN_VALUE | 935,720 | 9.5% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 189,540 | 99.6% |
| COMPARE_OP | 280 | 0.1% |
| CALL_BUILTIN_CLASS | 140 | 0.1% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 189,720 | 99.7% |
| COMPARE_OP | 280 | 0.1% |
| COMPARE_OP_INT | 220 | 0.1% |
| COMPARE_OP_FLOAT | 80 | 0.0% |
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
| CALL_PY_EXACT_ARGS | 189,860 | 50.0% |
| CACHE | 189,420 | 49.9% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 379,140 | 99.9% |
| RESUME | 240 | 0.1% |
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
| POP_TOP | 10,082,540 | 98.9% |
| POP_JUMP_IF_FALSE | 89,980 | 0.9% |
| ENTER_EXECUTOR | 24,880 | 0.2% |
| JUMP_BACKWARD | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,891,520 | 97.0% |
| LOAD_ATTR_SLOT | 189,240 | 1.9% |
| RETURN_VALUE | 89,840 | 0.9% |
| ENTER_EXECUTOR | 24,880 | 0.2% |
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
| RETURN_GENERATOR | 5,979,440 | 71.1% |
| BEFORE_ASYNC_WITH | 746,480 | 8.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 746,460 | 8.9% |
| LOAD_ATTR_INSTANCE_VALUE | 746,460 | 8.9% |
| LOAD_FAST | 189,240 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,408,120 | 100.0% |


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
| RESUME_CHECK | 2,439,140 | 100.0% |
| RESUME | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 1,503,560 | 61.6% |
| SEND | 935,760 | 38.4% |


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
| LOAD_ATTR_SLOT | 191,340 | 50.3% |
| LOAD_FAST | 189,240 | 49.7% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 380,600 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,317,740 | 94.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,493,560 | 4.8% |
| LOAD_ATTR_SLOT | 191,460 | 0.6% |
| LOAD_ATTR | 11,420 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,893,440 | 31.9% |
| CALL | 8,959,720 | 28.9% |
| LOAD_FAST | 4,669,380 | 15.1% |
| TO_BOOL_NONE | 4,478,920 | 14.4% |
| STORE_FAST | 1,868,480 | 6.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 20,544,540 | 22.8% |
| LOAD_FAST | 13,821,860 | 15.3% |
| POP_TOP | 11,021,180 | 12.2% |
| LOAD_FAST_LOAD_FAST | 10,826,240 | 12.0% |
| POP_JUMP_IF_FALSE | 10,278,000 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,600,940 | 43.9% |
| STORE_FAST | 10,838,640 | 12.0% |
| CALL_KW | 9,893,720 | 11.0% |
| COMPARE_OP_INT | 8,217,720 | 9.1% |
| SEND_GEN | 7,472,120 | 8.3% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 379,060 | 99.8% |
| LOAD_GLOBAL | 240 | 0.1% |
| STORE_FAST | 160 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 379,300 | 99.9% |
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
| RESUME_CHECK | 82,912,820 | 20.3% |
| POP_JUMP_IF_FALSE | 78,948,000 | 19.3% |
| STORE_FAST | 48,567,080 | 11.9% |
| LOAD_CONST | 39,600,940 | 9.7% |
| POP_TOP | 39,021,280 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 121,737,160 | 29.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 39,777,120 | 9.7% |
| LOAD_ATTR_SLOT | 36,122,320 | 8.8% |
| RETURN_VALUE | 33,519,620 | 8.2% |
| STORE_ATTR_SLOT | 31,195,800 | 7.6% |


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
| STORE_ATTR_SLOT | 30,248,820 | 31.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 16,240,780 | 16.8% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 15.2% |
| PUSH_NULL | 14,562,080 | 15.0% |
| POP_JUMP_IF_NOT_NONE | 9,893,640 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 40,520,880 | 41.8% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 15.2% |
| LOAD_CONST | 10,826,240 | 11.2% |
| LOAD_FAST | 10,083,360 | 10.4% |
| CALL | 10,083,080 | 10.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 620 | 12.9% |
| RESUME_CHECK | 600 | 12.4% |
| POP_JUMP_IF_FALSE | 540 | 11.2% |
| POP_TOP | 500 | 10.4% |
| LOAD_FAST | 500 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,680 | 34.9% |
| LOAD_ATTR | 1,020 | 21.2% |
| LOAD_GLOBAL_BUILTIN | 660 | 13.7% |
| LOAD_FAST | 400 | 8.3% |
| CALL | 320 | 6.6% |


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
| TO_BOOL_BOOL | 59,038,780 | 52.7% |
| TO_BOOL_NONE | 24,836,020 | 22.2% |
| COMPARE_OP_INT | 12,366,200 | 11.0% |
| TO_BOOL | 6,719,500 | 6.0% |
| TO_BOOL_LIST | 5,229,600 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,948,000 | 70.4% |
| RETURN_CONST | 15,498,180 | 13.8% |
| LOAD_CONST | 10,278,000 | 9.2% |
| LOAD_GLOBAL_MODULE | 5,236,280 | 4.7% |
| LOAD_FAST_LOAD_FAST | 2,057,660 | 1.8% |


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
| LOAD_FAST | 21,289,920 | 76.0% |
| LOAD_ATTR_INSTANCE_VALUE | 6,718,340 | 24.0% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 9,893,640 | 35.3% |
| LOAD_GLOBAL_MODULE | 7,283,280 | 26.0% |
| LOAD_FAST | 5,605,940 | 20.0% |
| RETURN_CONST | 4,478,880 | 16.0% |
| LOAD_CONST | 746,500 | 2.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,604,440 | 55.6% |
| TO_BOOL | 4,480,980 | 44.4% |
| TO_BOOL_INT | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,893,900 | 98.1% |
| LOAD_CONST | 191,160 | 1.9% |
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
| POP_JUMP_IF_FALSE | 15,498,180 | 28.0% |
| POP_TOP | 14,005,760 | 25.3% |
| STORE_ATTR_SLOT | 10,461,600 | 18.9% |
| STORE_FAST | 10,084,720 | 18.2% |
| POP_JUMP_IF_NOT_NONE | 4,478,880 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 28,188,720 | 51.0% |
| POP_TOP | 25,408,200 | 46.0% |
| END_SEND | 935,880 | 1.7% |
| EXIT_INIT_CHECK | 746,460 | 1.4% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 936,000 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 935,760 | 50.0% |
| SEND | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 935,720 | 50.0% |
| YIELD_VALUE | 935,720 | 50.0% |
| SEND | 840 | 0.0% |
| POP_TOP | 160 | 0.0% |
| SEND_GEN | 160 | 0.0% |


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
| CALL | 19,420,080 | 27.6% |
| RETURN_VALUE | 16,621,880 | 23.7% |
| LOAD_CONST | 10,838,640 | 15.4% |
| CALL_BUILTIN_O | 7,883,580 | 11.2% |
| FOR_ITER_RANGE | 4,480,960 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,567,080 | 69.1% |
| RETURN_CONST | 10,084,720 | 14.3% |
| JUMP_FORWARD | 4,482,960 | 6.4% |
| LOAD_FAST_LOAD_FAST | 4,336,140 | 6.2% |
| LOAD_GLOBAL_MODULE | 1,868,480 | 2.7% |


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
| YIELD_VALUE | 1,503,600 | 61.6% |
| SEND | 935,720 | 38.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,503,600 | 61.6% |
| INTERPRETER_EXIT | 935,720 | 38.4% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,160 | 55.8% |
| CACHE | 340 | 16.3% |
| COPY_FREE_VARS | 240 | 11.5% |
| POP_TOP | 180 | 8.7% |
| SEND_GEN | 120 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 960 | 46.2% |
| LOAD_GLOBAL | 620 | 29.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 180 | 8.7% |
| LOAD_CONST | 140 | 6.7% |
| NOP | 100 | 4.8% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 189,200 | 99.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,800 | 0.9% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 189,220 | 99.0% |
| STORE_FAST | 1,820 | 1.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,868,320 | 50.0% |
| RETURN_VALUE | 1,868,280 | 50.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,868,300 | 50.0% |
| CALL_PY_WITH_DEFAULTS | 1,868,280 | 50.0% |
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
| LOAD_CONST | 4,478,880 | 70.6% |
| LOAD_FAST_LOAD_FAST | 1,868,280 | 29.4% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,478,840 | 70.6% |
| STORE_FAST | 1,868,300 | 29.4% |
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
| LOAD_CONST | 2,614,720 | 99.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 0.5% |
| CALL | 60 | 0.0% |
| PUSH_NULL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,868,300 | 71.1% |
| GET_AWAITABLE | 746,460 | 28.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 14,340 | 0.5% |
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
| LOAD_FAST | 189,200 | 99.9% |
| LOAD_CONST | 180 | 0.1% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 189,220 | 99.9% |
| COPY | 140 | 0.1% |
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
| LOAD_FAST | 8,072,260 | 81.2% |
| LOAD_GLOBAL_MODULE | 1,864,120 | 18.8% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.0% |
| CALL | 200 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,883,580 | 79.3% |
| RETURN_VALUE | 1,864,140 | 18.8% |
| TO_BOOL_BOOL | 189,200 | 1.9% |
| POP_TOP | 120 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,080,880 | 100.0% |
| LOAD_GLOBAL_BUILTIN | 380 | 0.0% |
| CALL | 80 | 0.0% |
| BUILD_TUPLE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,081,300 | 100.0% |
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
| LOAD_FAST | 1,680,840 | 100.0% |
| LOAD_FAST_LOAD_FAST | 120 | 0.0% |
| CALL | 60 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,678,660 | 99.9% |
| TO_BOOL_NONE | 2,180 | 0.1% |
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
| LOAD_ATTR | 9,893,440 | 84.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,870,800 | 15.9% |
| CALL | 400 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 9,893,400 | 84.1% |
| STORE_FAST | 1,870,400 | 15.9% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |
| CALL | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,330,640 | 83.9% |
| CALL | 4,479,100 | 16.1% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 27,809,820 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 29,885,000 | 61.1% |
| LOAD_FAST | 13,824,120 | 28.2% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 9.1% |
| LOAD_ATTR_METHOD_NO_DICT | 380,640 | 0.8% |
| LOAD_SUPER_ATTR_METHOD | 189,400 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 38,490,740 | 78.6% |
| RETURN_GENERATOR | 10,268,900 | 21.0% |
| COPY_FREE_VARS | 189,860 | 0.4% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,868,280 | 90.8% |
| LOAD_GLOBAL_MODULE | 189,200 | 9.2% |
| CALL | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,868,680 | 90.8% |
| RETURN_GENERATOR | 189,220 | 9.2% |


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
| LOAD_GLOBAL_MODULE | 3,732,560 | 64.2% |
| LOAD_ATTR_SLOT | 2,080,840 | 35.8% |
| LOAD_FAST | 440 | 0.0% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,733,060 | 64.2% |
| RETURN_VALUE | 2,080,860 | 35.8% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,217,720 | 66.5% |
| LOAD_FAST_LOAD_FAST | 2,278,180 | 18.4% |
| LOAD_GLOBAL_MODULE | 1,870,080 | 15.1% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,366,200 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 1,868,280 | 100.0% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,868,440 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 121,737,160 | 96.4% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 3.5% |
| LOAD_ATTR | 1,980 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| COPY | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 39,767,520 | 31.5% |
| LOAD_ATTR_METHOD_NO_DICT | 29,494,980 | 23.4% |
| RETURN_VALUE | 15,687,300 | 12.4% |
| TO_BOOL | 11,199,400 | 8.9% |
| POP_JUMP_IF_NOT_NONE | 6,718,340 | 5.3% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 29,494,980 | 92.9% |
| LOAD_FAST | 2,249,160 | 7.1% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,011,780 | 78.8% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 14.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,870,800 | 5.9% |
| CALL_PY_EXACT_ARGS | 380,640 | 1.2% |
| LOAD_FAST_LOAD_FAST | 1,960 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,777,120 | 69.4% |
| LOAD_ATTR_SLOT | 10,461,400 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 5,227,400 | 9.1% |
| LOAD_FAST_LOAD_FAST | 1,868,320 | 3.3% |
| LOAD_ATTR | 1,260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 29,885,000 | 52.1% |
| LOAD_FAST_LOAD_FAST | 16,240,780 | 28.3% |
| LOAD_FAST | 11,209,040 | 19.5% |
| CALL | 700 | 0.0% |
| LOAD_CONST | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 26,529,680 | 100.0% |
| LOAD_ATTR | 1,020 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 26,340,920 | 99.3% |
| LOAD_FAST_LOAD_FAST | 189,220 | 0.7% |
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
| LOAD_FAST | 36,122,320 | 99.5% |
| ENTER_EXECUTOR | 189,240 | 0.5% |
| LOAD_ATTR_SLOT | 7,000 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 20,354,800 | 56.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 28.8% |
| LOAD_FAST | 2,081,320 | 5.7% |
| COMPARE_OP_FLOAT | 2,080,840 | 5.7% |
| TO_BOOL_BOOL | 759,120 | 2.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,272,920 | 57.4% |
| STORE_FAST | 748,300 | 18.9% |
| STORE_ATTR_INSTANCE_VALUE | 746,580 | 18.8% |
| POP_TOP | 189,400 | 4.8% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,089,440 | 52.7% |
| CALL_BUILTIN_CLASS | 746,660 | 18.8% |
| LOAD_GLOBAL_MODULE | 746,480 | 18.8% |
| LOAD_DEREF | 379,060 | 9.6% |
| CALL_ISINSTANCE | 380 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,679,140 | 38.1% |
| POP_JUMP_IF_NOT_NONE | 7,283,280 | 14.9% |
| POP_JUMP_IF_FALSE | 5,236,280 | 10.7% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 9.1% |
| LOAD_FAST | 4,140,360 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 26,529,680 | 54.2% |
| LOAD_FAST | 5,605,420 | 11.4% |
| LOAD_FAST_LOAD_FAST | 4,479,200 | 9.1% |
| COMPARE_OP_FLOAT | 3,732,560 | 7.6% |
| CALL_ISINSTANCE | 2,080,880 | 4.2% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 378,840 | 99.9% |
| LOAD_SUPER_ATTR | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 189,400 | 50.0% |
| LOAD_FAST_LOAD_FAST | 189,280 | 49.9% |
| LOAD_FAST | 260 | 0.1% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 42,034,380 | 38.9% |
| CALL_PY_EXACT_ARGS | 38,490,740 | 35.6% |
| POP_TOP | 11,951,180 | 11.1% |
| CALL | 4,668,780 | 4.3% |
| CALL_KW | 4,478,940 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 82,912,820 | 76.8% |
| LOAD_GLOBAL_MODULE | 18,679,140 | 17.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,439,140 | 2.3% |
| LOAD_GLOBAL_BUILTIN | 2,272,920 | 2.1% |
| LOAD_CONST | 1,493,380 | 1.4% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,472,120 | 83.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,503,560 | 16.8% |
| SEND | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,472,240 | 83.2% |
| RESUME_CHECK | 1,503,480 | 16.8% |
| RESUME | 120 | 0.0% |


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
| LOAD_FAST_LOAD_FAST | 40,520,880 | 56.5% |
| LOAD_FAST | 31,195,800 | 43.5% |
| STORE_ATTR_SLOT | 47,320 | 0.1% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 30,248,820 | 42.2% |
| LOAD_CONST | 20,544,540 | 28.6% |
| LOAD_FAST | 10,462,060 | 14.6% |
| RETURN_CONST | 10,461,600 | 14.6% |
| STORE_ATTR_SLOT | 47,320 | 0.1% |


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
| LOAD_ATTR_INSTANCE_VALUE | 39,767,520 | 61.5% |
| RETURN_VALUE | 10,272,680 | 15.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,893,400 | 15.3% |
| CALL_ISINSTANCE | 2,081,300 | 3.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,678,660 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 59,038,780 | 91.3% |
| POP_JUMP_IF_TRUE | 5,604,440 | 8.7% |
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
| LOAD_ATTR_SLOT | 20,354,800 | 82.0% |
| LOAD_ATTR | 4,478,920 | 18.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,180 | 0.0% |
| TO_BOOL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 24,836,020 | 100.0% |
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
|          hit | 10,274,980 | 100.0% |

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
|          hit | 189,680 | 99.9% |

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
|     deferred | 39,403,840 | 23.0% |
|          hit | 131,667,740 | 77.0% |
|         miss | 761,180 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,500 | 57.5% |
| Failure | 12,960 | 42.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 3,240 | 25.0% |
| no dict | 2,860 | 22.1% |
| cfunc noargs | 2,360 | 18.2% |
| code complex parameters | 1,580 | 12.2% |
| class no vectorcall | 1,340 | 10.3% |
| other | 1,280 | 9.9% |
| class mutable | 80 | 0.6% |
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
|     deferred | 189,760 | 1.0% |
|          hit | 18,483,700 | 99.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 51.7% |
| Failure | 280 | 48.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 240 | 85.7% |
| bool | 40 | 14.3% |


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
|     deferred | 31,370,120 | 8.0% |
|          hit | 360,473,840 | 92.0% |
|         miss | 376,020 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 12,480 | 54.2% |
| Failure | 10,540 | 45.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 6,480 | 61.5% |
| method | 2,540 | 24.1% |
| class attr descriptor | 1,280 | 12.1% |
| not managed dict | 140 | 1.3% |
| metaclass attribute | 60 | 0.6% |
| class attr simple | 40 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,560 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 52,930,740 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,340 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.1% |
|          hit | 379,060 | 99.9% |

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
|     deferred | 1,871,600 | 17.3% |
|          hit | 8,975,840 | 82.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 16.0% |
| Failure | 840 | 84.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 840 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,464,120 | 2.9% |
|          hit | 81,390,280 | 97.0% |
|         miss | 2,509,460 | 3.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 48,940 | 99.8% |
| Failure | 100 | 0.2% |

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
|     deferred | 11,202,200 | 8.9% |
|          hit | 114,681,220 | 91.1% |
|         miss | 1,700 | 0.0% |

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
| Basic | 1,034,363,860 | 50.4% |
| Not specialized | 246,616,960 | 12.0% |
| Specialized hits | 768,826,280 | 37.4% |
| Specialized misses | 3,676,540 | 0.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 39,403,840 | 45.6% |
| LOAD_ATTR | 31,370,120 | 36.3% |
| TO_BOOL | 11,202,200 | 12.9% |
| STORE_ATTR | 2,464,120 | 2.8% |
| SEND | 1,871,600 | 2.2% |
| COMPARE_OP | 189,760 | 0.2% |
| LOAD_GLOBAL | 2,560 | 0.0% |
| BINARY_OP | 820 | 0.0% |
| FOR_ITER | 260 | 0.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 2,509,460 | 67.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 760,800 | 20.5% |
| LOAD_ATTR_SLOT | 372,540 | 10.1% |
| RESUME | 28,100 | 0.8% |
| RESUME_CHECK | 28,100 | 0.8% |
| LOAD_ATTR_METHOD_NO_DICT | 3,480 | 0.1% |
| TO_BOOL_NONE | 1,060 | 0.0% |
| TO_BOOL_BOOL | 640 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 260 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 48,196,060 | 37.1% |
| Calls to Python functions inlined | 81,639,120 | 62.9% |
| Calls via PyEval_EvalFrame (total) | 48,196,060 | 37.1% |
| Calls via PyEval_EvalFrame (vector) | 42,781,380 | 33.0% |
| Calls via PyEval_EvalFrame (generator) | 5,414,680 | 4.2% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 42,781,380 | 33.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 2,080,880 | 1.6% |
| Calls via PyEval_EvalFrame (function ex) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.4% |
| Calls via PyEval_EvalFrame (method) | 19,787,280 | 15.2% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 116,190,960 | 89.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 57,521,100 | 16.8% |
| Frees to freelist | 57,856,680 |  |
| Allocations | 284,515,400 | 83.2% |
| Allocations to 512 bytes | 281,844,719 | 82.4% |
| Allocations to 4 kbytes | 2,670,561 | 0.8% |
| Allocations over 4 kbytes | 120 | 0.0% |
| Frees | 284,430,467 |  |
| New values | 440 |  |
| Interpreter increfs | 1,068,699,680 | 70.7% |
| Interpreter decrefs | 1,150,041,700 | 62.7% |
| Increfs | 443,458,098 | 29.3% |
| Decrefs | 685,275,515 | 37.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 63,580,010 |  |
| Method cache misses | 4,350 |  |
| Method cache collisions | 3,869 |  |
| Method cache dunder hits | 13,658,182 |  |
| Method cache dunder misses | 438 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 53,420 | 2,040 | 356,195,080 |
| 1 | 4,860 | 0 | 367,194,760 |
| 2 | 440 | 0 | 951,900,600 |


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
