
# Pystats results

- benchmark: async_tree_cpu_io_mixed
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 403,678,080 | 18.0% | 18.0% |  |
| POP_JUMP_IF_FALSE | 127,790,140 | 5.7% | 23.7% |  |
| RESUME_CHECK | 115,455,080 | 5.1% | 28.8% | 0.0% |
| LOAD_FAST_LOAD_FAST | 103,670,180 | 4.6% | 33.4% |  |
| LOAD_CONST | 100,672,380 | 4.5% | 37.9% |  |
| STORE_FAST | 90,437,460 | 4.0% | 41.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 79,937,140 | 3.6% | 45.5% |  |
| POP_TOP | 76,011,860 | 3.4% | 48.9% |  |
| TO_BOOL_BOOL | 72,854,880 | 3.2% | 52.1% | 0.0% |
| STORE_ATTR_SLOT | 71,764,340 | 3.2% | 55.3% | 3.5% |
| RETURN_VALUE | 64,643,960 | 2.9% | 58.2% |  |
| LOAD_GLOBAL_MODULE | 63,151,760 | 2.8% | 61.0% |  |
| RETURN_CONST | 59,011,740 | 2.6% | 63.6% |  |
| CALL_PY_EXACT_ARGS | 57,907,260 | 2.6% | 66.2% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 57,335,840 | 2.6% | 68.8% |  |
| INTERPRETER_EXIT | 47,449,560 | 2.1% | 70.9% |  |
| CALL | 43,900,020 | 2.0% | 72.8% |  |
| PUSH_NULL | 42,437,960 | 1.9% | 74.7% |  |
| LOAD_ATTR_SLOT | 40,798,120 | 1.8% | 76.5% | 0.9% |
| LOAD_DEREF | 40,689,620 | 1.8% | 78.3% |  |
| LOAD_ATTR_MODULE | 34,742,100 | 1.5% | 79.9% |  |
| LOAD_ATTR | 31,763,600 | 1.4% | 81.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 31,744,900 | 1.4% | 82.7% | 0.0% |
| POP_JUMP_IF_NOT_NONE | 30,994,600 | 1.4% | 84.1% |  |
| TO_BOOL_NONE | 24,836,040 | 1.1% | 85.2% | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20,808,880 | 0.9% | 86.1% | 21.9% |
| ENTER_EXECUTOR | 19,154,580 | 0.9% | 87.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 18,852,120 | 0.8% | 87.8% | 0.0% |
| COMPARE_OP_INT | 16,845,060 | 0.7% | 88.6% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.6% | 89.2% |  |
| LOAD_GLOBAL_BUILTIN | 12,920,180 | 0.6% | 89.7% | 0.0% |
| BINARY_OP_ADD_INT | 12,694,380 | 0.6% | 90.3% |  |
| STORE_DEREF | 12,690,160 | 0.6% | 90.9% |  |
| CALL_FUNCTION_EX | 11,018,840 | 0.5% | 91.4% |  |
| CALL_KW | 10,640,200 | 0.5% | 91.8% |  |
| RETURN_GENERATOR | 10,458,400 | 0.5% | 92.3% |  |
| POP_JUMP_IF_TRUE | 10,087,300 | 0.4% | 92.7% |  |
| CALL_BUILTIN_O | 9,937,060 | 0.4% | 93.2% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.4% | 93.6% |  |
| END_SEND | 6,915,160 | 0.3% | 93.9% |  |
| GET_AWAITABLE | 6,915,160 | 0.3% | 94.2% |  |
| SEND_GEN | 6,736,440 | 0.3% | 94.5% |  |
| BINARY_OP_SUBTRACT_INT | 6,347,220 | 0.3% | 94.8% |  |
| COMPARE_OP_FLOAT | 5,813,920 | 0.3% | 95.0% |  |
| NOP | 5,609,320 | 0.2% | 95.3% |  |
| COPY_FREE_VARS | 5,604,900 | 0.2% | 95.5% |  |
| TO_BOOL | 5,231,700 | 0.2% | 95.8% |  |
| STORE_ATTR | 5,230,120 | 0.2% | 96.0% |  |
| FOR_ITER_RANGE | 5,229,280 | 0.2% | 96.2% |  |
| CONTAINS_OP | 5,225,800 | 0.2% | 96.5% |  |
| CALL_BUILTIN_FAST | 4,668,340 | 0.2% | 96.7% |  |
| JUMP_FORWARD | 4,483,220 | 0.2% | 96.9% |  |
| TO_BOOL_LIST | 4,483,140 | 0.2% | 97.1% |  |
| JUMP_BACKWARD | 4,482,360 | 0.2% | 97.3% |  |
| COPY | 4,481,460 | 0.2% | 97.5% |  |
| STORE_SUBSCR_DICT | 4,480,700 | 0.2% | 97.7% |  |
| IS_OP | 4,479,280 | 0.2% | 97.9% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 98.1% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 98.3% |  |
| MAKE_CELL | 3,732,480 | 0.2% | 98.4% |  |
| BUILD_LIST | 3,368,600 | 0.1% | 98.6% |  |
| GET_ITER | 2,991,700 | 0.1% | 98.7% |  |
| FOR_ITER_LIST | 2,243,380 | 0.1% | 98.8% |  |
| SWAP | 2,239,780 | 0.1% | 98.9% |  |
| CALL_ISINSTANCE | 2,081,380 | 0.1% | 99.0% |  |
| CALL_PY_WITH_DEFAULTS | 2,057,900 | 0.1% | 99.1% |  |
| SEND | 1,872,520 | 0.1% | 99.2% |  |
| LOAD_ATTR_CLASS | 1,868,440 | 0.1% | 99.3% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,868,360 | 0.1% | 99.4% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,692,840 | 0.1% | 99.4% |  |
| YIELD_VALUE | 1,692,840 | 0.1% | 99.5% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,681,060 | 0.1% | 99.6% |  |
| FOR_ITER_TUPLE | 1,493,260 | 0.1% | 99.7% |  |
| LOAD_SUPER_ATTR_METHOD | 1,125,520 | 0.1% | 99.7% |  |
| BUILD_MAP | 936,120 | 0.0% | 99.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 749,000 | 0.0% | 99.8% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 380,600 | 0.0% | 100.0% |  |
| LIST_EXTEND | 380,600 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 191,040 | 0.0% | 100.0% |  |
| COMPARE_OP | 190,380 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,900 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| RESUME | 2,020 | 0.0% | 100.0% | 2,216.8% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 74,709,840 | 3.3% | 3.3% |
| RESUME_CHECK LOAD_FAST | 74,701,560 | 3.3% | 6.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 67,004,600 | 3.0% | 9.6% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 63,517,960 | 2.8% | 12.5% |
| STORE_FAST LOAD_FAST | 62,750,480 | 2.8% | 15.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 47,448,500 | 2.1% | 17.4% |
| LOAD_FAST LOAD_ATTR_SLOT | 40,601,200 | 1.8% | 19.2% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 40,520,880 | 1.8% | 21.0% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 39,777,160 | 1.8% | 22.8% |
| CACHE RESUME_CHECK | 37,555,520 | 1.7% | 24.4% |
| LOAD_CONST LOAD_FAST | 36,615,020 | 1.6% | 26.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 34,740,960 | 1.5% | 27.6% |
| LOAD_ATTR_MODULE PUSH_NULL | 34,552,200 | 1.5% | 29.1% |
| LOAD_FAST LOAD_ATTR | 31,556,820 | 1.4% | 30.5% |
| LOAD_FAST STORE_ATTR_SLOT | 31,195,800 | 1.4% | 31.9% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 30,248,820 | 1.3% | 33.3% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 29,138,560 | 1.3% | 34.6% |
| RETURN_CONST INTERPRETER_EXIT | 28,935,180 | 1.3% | 35.9% |
| LOAD_FAST RETURN_VALUE | 28,294,260 | 1.3% | 37.1% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 26,515,280 | 1.2% | 38.3% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 25,584,560 | 1.1% | 39.4% |
| RETURN_CONST POP_TOP | 25,408,200 | 1.1% | 40.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 25,011,780 | 1.1% | 41.7% |
| POP_TOP LOAD_FAST | 24,838,160 | 1.1% | 42.8% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 24,836,020 | 1.1% | 43.9% |
| CALL STORE_FAST | 24,645,460 | 1.1% | 45.0% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 23,528,320 | 1.0% | 46.0% |
| POP_JUMP_IF_FALSE RETURN_CONST | 22,962,980 | 1.0% | 47.1% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 22,411,540 | 1.0% | 48.1% |
| STORE_ATTR_SLOT LOAD_CONST | 20,544,540 | 0.9% | 49.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 20,537,300 | 0.9% | 49.9% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 20,354,800 | 0.9% | 50.8% |
| POP_JUMP_IF_FALSE LOAD_CONST | 19,235,760 | 0.9% | 51.7% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 18,852,100 | 0.8% | 52.5% |
| RETURN_VALUE INTERPRETER_EXIT | 17,578,660 | 0.8% | 53.3% |
| RETURN_VALUE STORE_FAST | 17,368,360 | 0.8% | 54.1% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 16,845,060 | 0.7% | 54.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 15,687,300 | 0.7% | 55.5% |
| LOAD_CONST STORE_FAST | 15,317,520 | 0.7% | 56.2% |
| POP_TOP RETURN_CONST | 14,752,240 | 0.7% | 56.8% |
| RETURN_VALUE TO_BOOL_BOOL | 14,751,560 | 0.7% | 57.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,751,480 | 0.7% | 58.2% |
| LOAD_FAST LOAD_CONST | 14,568,340 | 0.6% | 58.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,562,240 | 0.6% | 59.4% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,562,080 | 0.6% | 60.1% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,372,960 | 0.6% | 60.7% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 14,372,560 | 0.6% | 61.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 14,372,520 | 0.6% | 62.0% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,626,040 | 0.6% | 62.6% |
| PUSH_NULL LOAD_FAST | 12,932,020 | 0.6% | 63.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 11,955,520 | 0.5% | 63.7% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 11,761,920 | 0.5% | 64.3% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 11,230,680 | 0.5% | 64.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 11,047,200 | 0.5% | 65.2% |
| LOAD_CONST BINARY_OP_ADD_INT | 10,826,000 | 0.5% | 65.7% |
| STORE_ATTR_SLOT LOAD_FAST | 10,462,060 | 0.5% | 66.2% |
| STORE_ATTR_SLOT RETURN_CONST | 10,461,600 | 0.5% | 66.7% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 0.5% | 67.1% |
| POP_TOP RESUME_CHECK | 10,458,260 | 0.5% | 67.6% |
| PUSH_NULL CALL | 10,275,260 | 0.5% | 68.0% |
| POP_TOP LOAD_CONST | 10,274,700 | 0.5% | 68.5% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 10,268,900 | 0.5% | 69.0% |
| LOAD_FAST CALL | 10,085,120 | 0.4% | 69.4% |
| STORE_FAST RETURN_CONST | 10,084,720 | 0.4% | 69.9% |
| LOAD_FAST_LOAD_FAST CALL | 10,083,080 | 0.4% | 70.3% |
| CALL_FUNCTION_EX POP_TOP | 10,083,040 | 0.4% | 70.8% |
| POP_TOP ENTER_EXECUTOR | 10,082,540 | 0.4% | 71.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,893,900 | 0.4% | 71.6% |
| ENTER_EXECUTOR CALL_FUNCTION_EX | 9,891,520 | 0.4% | 72.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 9,336,860 | 0.4% | 72.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.4% | 72.9% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.4% | 73.3% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.4% | 73.7% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.4% | 74.1% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.4% | 74.5% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 8,957,080 | 0.4% | 74.9% |
| LOAD_CONST COMPARE_OP_INT | 8,217,720 | 0.4% | 75.3% |
| LOAD_FAST CALL_BUILTIN_O | 8,072,260 | 0.4% | 75.6% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_MODULE | 8,029,720 | 0.4% | 76.0% |
| CALL_BUILTIN_O STORE_FAST | 7,883,580 | 0.4% | 76.3% |
| LOAD_FAST PUSH_NULL | 7,504,120 | 0.3% | 76.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 7,094,120 | 0.3% | 77.0% |
| GET_AWAITABLE LOAD_CONST | 6,915,160 | 0.3% | 77.3% |
| LOAD_CONST CALL_KW | 6,908,080 | 0.3% | 77.6% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 6,728,000 | 0.3% | 77.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 6,349,260 | 0.3% | 78.2% |
| RETURN_VALUE RETURN_VALUE | 6,347,680 | 0.3% | 78.5% |
| STORE_FAST LOAD_GLOBAL_MODULE | 6,347,360 | 0.3% | 78.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 5,983,000 | 0.3% | 79.0% |
| RETURN_GENERATOR GET_AWAITABLE | 5,979,440 | 0.3% | 79.3% |
| SEND_GEN POP_TOP | 5,979,320 | 0.3% | 79.5% |
| LOAD_CONST SEND_GEN | 5,979,240 | 0.3% | 79.8% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 5,829,380 | 0.3% | 80.1% |
| RETURN_VALUE END_SEND | 5,790,040 | 0.3% | 80.3% |
| NOP LOAD_FAST | 5,608,760 | 0.2% | 80.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 5,605,420 | 0.2% | 80.8% |
| COPY_FREE_VARS RESUME_CHECK | 5,604,460 | 0.2% | 81.1% |
| CALL POP_TOP | 5,415,400 | 0.2% | 81.3% |
| CACHE COPY_FREE_VARS | 5,414,780 | 0.2% | 81.6% |
| LOAD_ATTR CALL | 5,227,620 | 0.2% | 81.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 37,555,520 | 79.1% |
| COPY_FREE_VARS | 5,414,780 | 11.4% |
| POP_TOP | 4,478,960 | 9.4% |
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
| RETURN_VALUE | 5,790,040 | 83.7% |
| SEND | 935,720 | 13.5% |
| RETURN_CONST | 189,400 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,857,600 | 70.2% |
| RETURN_VALUE | 1,868,320 | 27.0% |
| LOAD_FAST | 189,240 | 2.7% |


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
| RETURN_CONST | 28,935,180 | 61.0% |
| RETURN_VALUE | 17,578,660 | 37.0% |
| YIELD_VALUE | 935,720 | 2.0% |


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
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 66.5% |
| RESUME_CHECK | 938,460 | 16.7% |
| STORE_FAST | 937,720 | 16.7% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,608,760 | 100.0% |
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
| RETURN_CONST | 25,408,200 | 33.4% |
| CALL_METHOD_DESCRIPTOR_O | 18,852,100 | 24.8% |
| CALL_FUNCTION_EX | 10,083,040 | 13.3% |
| SEND_GEN | 5,979,320 | 7.9% |
| CALL | 5,415,400 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,838,160 | 32.7% |
| RETURN_CONST | 14,752,240 | 19.4% |
| RESUME_CHECK | 10,458,260 | 13.8% |
| LOAD_CONST | 10,274,700 | 13.5% |
| ENTER_EXECUTOR | 10,082,540 | 13.3% |


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
| LOAD_ATTR_MODULE | 34,552,200 | 81.4% |
| LOAD_FAST | 7,504,120 | 17.7% |
| LOAD_ATTR | 381,560 | 0.9% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 14,562,080 | 34.3% |
| LOAD_FAST | 12,932,020 | 30.5% |
| CALL | 10,275,260 | 24.2% |
| LOAD_GLOBAL_MODULE | 2,053,320 | 4.8% |
| LOAD_CONST | 1,868,560 | 4.4% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,268,900 | 98.2% |
| CALL_PY_WITH_DEFAULTS | 189,220 | 1.8% |
| CALL | 140 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 5,979,440 | 57.2% |
| LIST_APPEND | 4,478,880 | 42.8% |
| CALL | 40 | 0.0% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,294,260 | 43.8% |
| LOAD_ATTR_INSTANCE_VALUE | 15,687,300 | 24.3% |
| RETURN_VALUE | 6,347,680 | 9.8% |
| POP_JUMP_IF_FALSE | 4,479,040 | 6.9% |
| COMPARE_OP_FLOAT | 2,080,860 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 17,578,660 | 27.2% |
| STORE_FAST | 17,368,360 | 26.9% |
| TO_BOOL_BOOL | 14,751,560 | 22.8% |
| RETURN_VALUE | 6,347,680 | 9.8% |
| END_SEND | 5,790,040 | 9.0% |


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
| STORE_FAST | 748,320 | 22.2% |
| POP_JUMP_IF_FALSE | 746,480 | 22.2% |
| STORE_DEREF | 746,480 | 22.2% |
| SWAP | 746,480 | 22.2% |
| LOAD_ATTR_SLOT | 191,340 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,494,800 | 44.4% |
| STORE_DEREF | 746,480 | 22.2% |
| SWAP | 746,480 | 22.2% |
| LOAD_FAST | 380,840 | 11.3% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 79.7% |
| LOAD_FAST | 189,240 | 20.2% |
| STORE_ATTR_INSTANCE_VALUE | 140 | 0.0% |
| POP_TOP | 80 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 746,480 | 79.7% |
| CALL_FUNCTION_EX | 189,240 | 20.2% |
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
| PUSH_NULL | 10,275,260 | 23.4% |
| LOAD_FAST | 10,085,120 | 23.0% |
| LOAD_FAST_LOAD_FAST | 10,083,080 | 23.0% |
| LOAD_ATTR | 5,227,620 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 4,479,100 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 24,645,460 | 56.1% |
| POP_TOP | 5,415,400 | 12.3% |
| RESUME_CHECK | 4,668,800 | 10.6% |
| CALL_METHOD_DESCRIPTOR_O | 4,479,060 | 10.2% |
| LOAD_GLOBAL_MODULE | 3,732,500 | 8.5% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 9,891,520 | 89.8% |
| STORE_FAST | 746,480 | 6.8% |
| CALL_INTRINSIC_1 | 191,360 | 1.7% |
| BUILD_MAP | 189,240 | 1.7% |
| DICT_MERGE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,083,040 | 91.5% |
| MAKE_CELL | 746,480 | 6.8% |
| STORE_FAST | 189,240 | 1.7% |
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
| LOAD_CONST | 6,908,080 | 64.9% |
| ENTER_EXECUTOR | 3,732,120 | 35.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,478,960 | 42.1% |
| RESUME_CHECK | 4,478,940 | 42.1% |
| POP_TOP | 746,560 | 7.0% |
| STORE_DEREF | 746,480 | 7.0% |
| RETURN_VALUE | 189,240 | 1.8% |


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
| POP_JUMP_IF_FALSE | 189,740 | 99.7% |
| COMPARE_OP | 280 | 0.1% |
| COMPARE_OP_INT | 240 | 0.1% |
| COMPARE_OP_FLOAT | 80 | 0.0% |
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
| CACHE | 5,414,780 | 96.6% |
| CALL_PY_EXACT_ARGS | 189,860 | 3.4% |
| CALL | 180 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,604,460 | 100.0% |
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
| POP_TOP | 10,082,540 | 52.6% |
| CALL_LIST_APPEND | 8,957,080 | 46.8% |
| POP_JUMP_IF_FALSE | 89,980 | 0.5% |
| ENTER_EXECUTOR | 24,880 | 0.1% |
| JUMP_BACKWARD | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,891,520 | 51.6% |
| CALL | 3,732,120 | 19.5% |
| CALL_KW | 3,732,120 | 19.5% |
| FOR_ITER_TUPLE | 746,460 | 3.9% |
| FOR_ITER_LIST | 746,440 | 3.9% |


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
| RETURN_GENERATOR | 5,979,440 | 86.5% |
| RETURN_VALUE | 746,480 | 10.8% |
| LOAD_FAST | 189,240 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,915,160 | 100.0% |


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
| RESUME_CHECK | 1,692,680 | 100.0% |
| RESUME | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND | 935,760 | 55.3% |
| SEND_GEN | 757,080 | 44.7% |


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
| LOAD_FAST | 31,556,820 | 99.3% |
| LOAD_ATTR_SLOT | 191,460 | 0.6% |
| LOAD_ATTR | 11,660 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,040 | 0.0% |
| LOAD_GLOBAL | 1,020 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,372,560 | 45.2% |
| CALL | 5,227,620 | 16.5% |
| LOAD_FAST | 4,669,380 | 14.7% |
| TO_BOOL_NONE | 4,478,920 | 14.1% |
| STORE_FAST | 2,614,960 | 8.2% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 20,544,540 | 20.4% |
| POP_JUMP_IF_FALSE | 19,235,760 | 19.1% |
| LOAD_FAST | 14,568,340 | 14.5% |
| POP_TOP | 10,274,700 | 10.2% |
| LOAD_DEREF | 8,957,920 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,615,020 | 36.4% |
| STORE_FAST | 15,317,520 | 15.2% |
| BINARY_OP_ADD_INT | 10,826,000 | 10.8% |
| COMPARE_OP_INT | 8,217,720 | 8.2% |
| CALL_KW | 6,908,080 | 6.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NONE | 8,957,760 | 22.0% |
| POP_JUMP_IF_FALSE | 5,225,360 | 12.8% |
| RESUME_CHECK | 4,478,920 | 11.0% |
| JUMP_FORWARD | 4,478,880 | 11.0% |
| LOAD_DEREF | 4,478,880 | 11.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,957,920 | 22.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 5,225,280 | 12.8% |
| LOAD_DEREF | 4,478,880 | 11.0% |
| POP_JUMP_IF_NONE | 4,478,880 | 11.0% |
| COMPARE_OP_INT | 4,478,840 | 11.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 74,701,560 | 18.5% |
| POP_JUMP_IF_FALSE | 67,004,600 | 16.6% |
| STORE_FAST | 62,750,480 | 15.5% |
| LOAD_CONST | 36,615,020 | 9.1% |
| LOAD_ATTR_METHOD_NO_DICT | 25,011,780 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 74,709,840 | 18.5% |
| LOAD_ATTR_SLOT | 40,601,200 | 10.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 39,777,160 | 9.9% |
| LOAD_ATTR | 31,556,820 | 7.8% |
| STORE_ATTR_SLOT | 31,195,800 | 7.7% |


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
| STORE_ATTR_SLOT | 30,248,820 | 29.2% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 14.2% |
| PUSH_NULL | 14,562,080 | 14.0% |
| POP_JUMP_IF_NOT_NONE | 13,626,040 | 13.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,761,920 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 40,520,880 | 39.1% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 14.2% |
| LOAD_FAST | 14,562,240 | 14.0% |
| CALL | 10,083,080 | 9.7% |
| LOAD_CONST | 7,094,120 | 6.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 620 | 12.7% |
| RESUME_CHECK | 600 | 12.2% |
| POP_JUMP_IF_FALSE | 580 | 11.8% |
| POP_TOP | 500 | 10.2% |
| LOAD_FAST | 500 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,720 | 35.1% |
| LOAD_ATTR | 1,020 | 20.8% |
| LOAD_GLOBAL_BUILTIN | 660 | 13.5% |
| LOAD_FAST | 400 | 8.2% |
| CALL | 300 | 6.1% |


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
| TO_BOOL_BOOL | 63,517,960 | 49.7% |
| TO_BOOL_NONE | 24,836,020 | 19.4% |
| COMPARE_OP_INT | 16,845,060 | 13.2% |
| CONTAINS_OP | 5,225,800 | 4.1% |
| TO_BOOL_LIST | 4,483,140 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,004,600 | 52.4% |
| RETURN_CONST | 22,962,980 | 18.0% |
| LOAD_CONST | 19,235,760 | 15.1% |
| LOAD_GLOBAL_MODULE | 5,983,000 | 4.7% |
| LOAD_DEREF | 5,225,360 | 4.1% |


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
| LOAD_FAST | 26,515,280 | 85.5% |
| LOAD_ATTR_INSTANCE_VALUE | 4,478,960 | 14.5% |
| LOAD_GLOBAL_MODULE | 220 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,626,040 | 44.0% |
| LOAD_GLOBAL_MODULE | 8,029,720 | 25.9% |
| LOAD_FAST | 4,859,460 | 15.7% |
| NOP | 3,732,560 | 12.0% |
| LOAD_GLOBAL_BUILTIN | 746,440 | 2.4% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 9,336,860 | 92.6% |
| TO_BOOL | 748,560 | 7.4% |
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
| POP_JUMP_IF_FALSE | 22,962,980 | 38.9% |
| POP_TOP | 14,752,240 | 25.0% |
| STORE_ATTR_SLOT | 10,461,600 | 17.7% |
| STORE_FAST | 10,084,720 | 17.1% |
| STORE_ATTR_INSTANCE_VALUE | 747,120 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 28,935,180 | 49.0% |
| POP_TOP | 25,408,200 | 43.1% |
| TO_BOOL_BOOL | 4,478,920 | 7.6% |
| END_SEND | 189,400 | 0.3% |
| TO_BOOL | 40 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 935,920 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 935,760 | 50.0% |
| SEND | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 935,720 | 50.0% |
| YIELD_VALUE | 935,720 | 50.0% |
| SEND | 840 | 0.0% |
| POP_TOP | 120 | 0.0% |
| SEND_GEN | 120 | 0.0% |


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
| CALL | 24,645,460 | 27.3% |
| RETURN_VALUE | 17,368,360 | 19.2% |
| LOAD_CONST | 15,317,520 | 16.9% |
| CALL_BUILTIN_O | 7,883,580 | 8.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,349,260 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,750,480 | 69.4% |
| RETURN_CONST | 10,084,720 | 11.2% |
| LOAD_GLOBAL_MODULE | 6,347,360 | 7.0% |
| LOAD_FAST_LOAD_FAST | 5,829,380 | 6.4% |
| LOAD_CONST | 1,493,520 | 1.7% |


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
| SEND | 935,720 | 55.3% |
| YIELD_VALUE | 757,120 | 44.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 935,720 | 55.3% |
| YIELD_VALUE | 757,120 | 44.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,140 | 56.4% |
| CACHE | 300 | 14.9% |
| COPY_FREE_VARS | 280 | 13.9% |
| POP_TOP | 140 | 6.9% |
| SEND_GEN | 100 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 940 | 46.5% |
| LOAD_GLOBAL | 620 | 30.7% |
| JUMP_BACKWARD_NO_INTERRUPT | 160 | 7.9% |
| NOP | 100 | 5.0% |
| LOAD_CONST | 100 | 5.0% |


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
| LOAD_CONST | 10,826,000 | 85.3% |
| RETURN_VALUE | 1,868,280 | 14.7% |
| BINARY_OP | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 8,957,720 | 70.6% |
| RETURN_VALUE | 1,868,300 | 14.7% |
| CALL_PY_WITH_DEFAULTS | 1,868,280 | 14.7% |
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

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,868,280 | 100.0% |
| PUSH_NULL | 40 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,868,300 | 100.0% |
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
| LOAD_CONST | 4,479,060 | 95.9% |
| LOAD_FAST | 189,200 | 4.1% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,479,020 | 95.9% |
| POP_TOP | 189,220 | 4.1% |
| TO_BOOL_BOOL | 80 | 0.0% |
| TO_BOOL | 20 | 0.0% |


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
| LOAD_ATTR | 14,372,560 | 69.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 21.5% |
| LOAD_ATTR_METHOD_NO_DICT | 1,870,800 | 9.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| CALL | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 14,372,520 | 69.1% |
| STORE_FAST | 6,349,260 | 30.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.4% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,372,960 | 76.2% |
| CALL | 4,479,060 | 23.8% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 18,852,100 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 29,138,560 | 50.3% |
| LOAD_FAST | 23,528,320 | 40.6% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 7.7% |
| LOAD_ATTR_METHOD_NO_DICT | 380,640 | 0.7% |
| LOAD_SUPER_ATTR_METHOD | 189,400 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 47,448,500 | 81.9% |
| RETURN_GENERATOR | 10,268,900 | 17.7% |
| COPY_FREE_VARS | 189,860 | 0.3% |


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
| LOAD_CONST | 8,217,720 | 48.8% |
| LOAD_DEREF | 4,478,840 | 26.6% |
| LOAD_FAST_LOAD_FAST | 2,278,180 | 13.5% |
| LOAD_GLOBAL_MODULE | 1,870,080 | 11.1% |
| COMPARE_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,845,060 | 100.0% |


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
| LOAD_FAST | 74,709,840 | 93.5% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 5.6% |
| LOAD_DEREF | 746,440 | 0.9% |
| LOAD_ATTR | 1,540 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 25,584,560 | 32.0% |
| LOAD_ATTR_METHOD_NO_DICT | 20,537,300 | 25.7% |
| RETURN_VALUE | 15,687,300 | 19.6% |
| TO_BOOL_LIST | 4,483,060 | 5.6% |
| TO_BOOL | 4,481,060 | 5.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 20,537,300 | 64.7% |
| LOAD_FAST | 6,728,000 | 21.2% |
| LOAD_DEREF | 4,478,840 | 14.1% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |

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
| LOAD_FAST | 39,777,160 | 69.4% |
| LOAD_ATTR_SLOT | 10,461,400 | 18.2% |
| LOAD_DEREF | 5,225,280 | 9.1% |
| LOAD_FAST_LOAD_FAST | 1,868,320 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 29,138,560 | 50.8% |
| LOAD_FAST | 11,955,520 | 20.9% |
| LOAD_FAST_LOAD_FAST | 11,761,920 | 20.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,478,840 | 7.8% |
| CALL | 700 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 34,740,960 | 100.0% |
| LOAD_ATTR | 1,020 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 34,552,200 | 99.5% |
| LOAD_FAST_LOAD_FAST | 189,220 | 0.5% |
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
| LOAD_FAST | 40,601,200 | 99.5% |
| ENTER_EXECUTOR | 189,240 | 0.5% |
| LOAD_ATTR_SLOT | 7,000 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 20,354,800 | 49.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 25.6% |
| LOAD_CONST | 4,479,160 | 11.0% |
| LOAD_FAST | 2,081,320 | 5.1% |
| COMPARE_OP_FLOAT | 2,080,840 | 5.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,230,680 | 86.9% |
| PUSH_NULL | 746,440 | 5.8% |
| POP_JUMP_IF_NOT_NONE | 746,440 | 5.8% |
| POP_TOP | 189,400 | 1.5% |
| JUMP_FORWARD | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,047,200 | 85.5% |
| LOAD_DEREF | 1,125,520 | 8.7% |
| LOAD_GLOBAL_MODULE | 746,480 | 5.8% |
| CALL_ISINSTANCE | 380 | 0.0% |
| CALL_BUILTIN_CLASS | 220 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 22,411,540 | 35.5% |
| POP_JUMP_IF_NOT_NONE | 8,029,720 | 12.7% |
| STORE_FAST | 6,347,360 | 10.1% |
| POP_JUMP_IF_FALSE | 5,983,000 | 9.5% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 34,740,960 | 55.0% |
| LOAD_FAST | 5,605,420 | 8.9% |
| LOAD_FAST_LOAD_FAST | 5,225,940 | 8.3% |
| CONTAINS_OP | 4,478,940 | 7.1% |
| COMPARE_OP_FLOAT | 3,732,560 | 5.9% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,125,280 | 100.0% |
| LOAD_SUPER_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 746,720 | 66.3% |
| CALL_PY_EXACT_ARGS | 189,400 | 16.8% |
| LOAD_FAST_LOAD_FAST | 189,280 | 16.8% |
| CALL | 120 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 47,448,500 | 41.1% |
| CACHE | 37,555,520 | 32.5% |
| POP_TOP | 10,458,260 | 9.1% |
| COPY_FREE_VARS | 5,604,460 | 4.9% |
| CALL | 4,668,800 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,701,560 | 64.7% |
| LOAD_GLOBAL_MODULE | 22,411,540 | 19.4% |
| LOAD_GLOBAL_BUILTIN | 11,230,680 | 9.7% |
| LOAD_DEREF | 4,478,920 | 3.9% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,692,680 | 1.5% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,979,240 | 88.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 757,080 | 11.2% |
| SEND | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,979,320 | 88.8% |
| RESUME_CHECK | 757,020 | 11.2% |
| RESUME | 100 | 0.0% |


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
| LOAD_ATTR_INSTANCE_VALUE | 25,584,560 | 35.1% |
| RETURN_VALUE | 14,751,560 | 20.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,372,520 | 19.7% |
| COPY | 4,479,080 | 6.1% |
| RETURN_CONST | 4,478,920 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 63,517,960 | 87.2% |
| POP_JUMP_IF_TRUE | 9,336,860 | 12.8% |
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
|     deferred | 860 | 0.0% |
|          hit | 19,232,700 | 100.0% |

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
|     deferred | 48,361,560 | 23.7% |
|          hit | 155,555,140 | 76.2% |
|         miss | 4,565,360 | 2.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 89,240 | 86.0% |
| Failure | 14,580 | 14.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 4,520 | 31.0% |
| no dict | 2,860 | 19.6% |
| cfunc noargs | 2,360 | 16.2% |
| code complex parameters | 1,560 | 10.7% |
| class no vectorcall | 1,340 | 9.2% |
| other | 1,280 | 8.8% |
| cmethod | 380 | 2.6% |
| class mutable | 80 | 0.5% |
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
|     deferred | 189,780 | 0.8% |
|          hit | 22,962,560 | 99.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 53.3% |
| Failure | 280 | 46.7% |

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
|     deferred | 32,116,700 | 8.9% |
|          hit | 326,882,700 | 91.0% |
|         miss | 376,020 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 12,020 | 52.4% |
| Failure | 10,900 | 47.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 7,760 | 71.2% |
| method | 1,620 | 14.9% |
| class attr descriptor | 1,280 | 11.7% |
| not managed dict | 140 | 1.3% |
| metaclass attribute | 60 | 0.6% |
| class attr simple | 40 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,600 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 76,071,860 | 100.0% |
|         miss | 80 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 0.0% |
|          hit | 1,125,520 | 100.0% |

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
|     deferred | 1,871,560 | 21.7% |
|          hit | 6,736,440 | 78.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 12.5% |
| Failure | 840 | 87.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 840 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,689,180 | 9.9% |
|          hit | 70,193,380 | 90.1% |
|         miss | 2,509,460 | 3.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 48,640 | 96.5% |
| Failure | 1,760 | 3.5% |

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
|     deferred | 5,230,300 | 4.0% |
|          hit | 125,878,480 | 96.0% |
|         miss | 1,700 | 0.0% |

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
| Basic | 1,165,746,620 | 51.9% |
| Not specialized | 270,505,640 | 12.0% |
| Specialized hits | 802,403,360 | 35.7% |
| Specialized misses | 7,497,400 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 48,361,560 | 50.7% |
| LOAD_ATTR | 32,116,700 | 33.6% |
| STORE_ATTR | 7,689,180 | 8.1% |
| TO_BOOL | 5,230,300 | 5.5% |
| SEND | 1,871,560 | 2.0% |
| COMPARE_OP | 189,780 | 0.2% |
| LOAD_GLOBAL | 2,600 | 0.0% |
| BINARY_OP | 860 | 0.0% |
| FOR_ITER | 320 | 0.0% |
| LOAD_SUPER_ATTR | 260 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 60.5% |
| STORE_ATTR_SLOT | 2,509,460 | 33.3% |
| LOAD_ATTR_SLOT | 372,540 | 4.9% |
| RESUME | 44,780 | 0.6% |
| RESUME_CHECK | 44,780 | 0.6% |
| LOAD_ATTR_METHOD_NO_DICT | 3,480 | 0.0% |
| TO_BOOL_NONE | 1,060 | 0.0% |
| TO_BOOL_BOOL | 640 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 80 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 47,449,560 | 34.9% |
| Calls to Python functions inlined | 88,357,460 | 65.1% |
| Calls via PyEval_EvalFrame (total) | 47,449,560 | 34.9% |
| Calls via PyEval_EvalFrame (vector) | 42,034,880 | 31.0% |
| Calls via PyEval_EvalFrame (generator) | 5,414,680 | 4.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 42,034,880 | 31.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 2,080,880 | 1.5% |
| Calls via PyEval_EvalFrame (function ex) | 746,560 | 0.5% |
| Calls via PyEval_EvalFrame (api) | 4,479,100 | 3.3% |
| Calls via PyEval_EvalFrame (method) | 19,787,280 | 14.6% |
| Frame objects created | 180 | 0.0% |
| Frames pushed | 123,655,780 | 91.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 65,056,175 | 18.4% |
| Frees to freelist | 65,505,775 |  |
| Allocations | 288,919,746 | 81.6% |
| Allocations to 512 bytes | 286,995,550 | 81.1% |
| Allocations to 4 kbytes | 1,924,066 | 0.5% |
| Allocations over 4 kbytes | 130 | 0.0% |
| Frees | 291,027,561 |  |
| New values | 420 |  |
| Interpreter increfs | 1,129,167,040 | 68.5% |
| Interpreter decrefs | 1,218,718,940 | 61.5% |
| Increfs | 518,715,051 | 31.5% |
| Decrefs | 762,016,061 | 38.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 87,602,049 |  |
| Method cache misses | 2,109,611 |  |
| Method cache collisions | 2,107,890 |  |
| Method cache dunder hits | 12,911,654 |  |
| Method cache dunder misses | 446 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 51,440 | 2,040 | 344,538,160 |
| 1 | 4,680 | 0 | 348,571,920 |
| 2 | 420 | 0 | 848,250,000 |


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
