
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
| LOAD_FAST | 482,591,040 | 18.4% | 18.4% |  |
| POP_JUMP_IF_FALSE | 155,529,740 | 5.9% | 24.3% |  |
| RESUME_CHECK | 125,346,600 | 4.8% | 29.1% | 0.0% |
| STORE_FAST | 118,555,540 | 4.5% | 33.6% |  |
| LOAD_FAST_LOAD_FAST | 111,249,140 | 4.2% | 37.8% |  |
| LOAD_CONST | 104,782,100 | 4.0% | 41.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 100,664,540 | 3.8% | 45.7% |  |
| TO_BOOL_BOOL | 96,370,040 | 3.7% | 49.3% | 0.0% |
| LOAD_ATTR_SLOT | 80,554,080 | 3.1% | 52.4% | 0.5% |
| POP_TOP | 76,200,620 | 2.9% | 55.3% |  |
| STORE_ATTR_SLOT | 71,953,100 | 2.7% | 58.1% | 3.5% |
| CALL_PY_EXACT_ARGS | 67,798,780 | 2.6% | 60.6% |  |
| LOAD_GLOBAL_MODULE | 67,072,640 | 2.6% | 63.2% |  |
| RETURN_VALUE | 64,643,960 | 2.5% | 65.7% |  |
| RETURN_CONST | 59,011,740 | 2.2% | 67.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 57,335,840 | 2.2% | 70.1% |  |
| PUSH_NULL | 52,632,960 | 2.0% | 72.1% |  |
| LOAD_ATTR_METHOD_NO_DICT | 51,906,200 | 2.0% | 74.1% | 0.0% |
| LOAD_ATTR | 49,123,580 | 1.9% | 75.9% |  |
| INTERPRETER_EXIT | 47,449,560 | 1.8% | 77.8% |  |
| CALL | 43,900,020 | 1.7% | 79.4% |  |
| LOAD_DEREF | 40,689,620 | 1.6% | 81.0% |  |
| LOAD_ATTR_MODULE | 34,930,860 | 1.3% | 82.3% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 34,621,760 | 1.3% | 83.6% | 13.2% |
| POP_JUMP_IF_NOT_NONE | 30,994,600 | 1.2% | 84.8% |  |
| TO_BOOL_NONE | 24,836,040 | 0.9% | 85.8% | 0.0% |
| JUMP_BACKWARD | 23,825,520 | 0.9% | 86.7% |  |
| CALL_METHOD_DESCRIPTOR_O | 19,040,880 | 0.7% | 87.4% | 0.0% |
| COMPARE_OP_INT | 16,959,780 | 0.6% | 88.0% |  |
| NOP | 15,500,840 | 0.6% | 88.6% |  |
| FOR_ITER_RANGE | 15,310,040 | 0.6% | 89.2% |  |
| POP_JUMP_IF_NONE | 13,437,680 | 0.5% | 89.7% |  |
| BUILD_LIST | 13,260,120 | 0.5% | 90.2% |  |
| LOAD_GLOBAL_BUILTIN | 12,920,180 | 0.5% | 90.7% | 0.0% |
| BINARY_OP_ADD_INT | 12,694,380 | 0.5% | 91.2% |  |
| STORE_DEREF | 12,690,160 | 0.5% | 91.7% |  |
| CALL_FUNCTION_EX | 11,018,840 | 0.4% | 92.1% |  |
| CALL_KW | 10,640,200 | 0.4% | 92.5% |  |
| RETURN_GENERATOR | 10,458,400 | 0.4% | 92.9% |  |
| CALL_INTRINSIC_1 | 10,272,120 | 0.4% | 93.3% |  |
| LIST_EXTEND | 10,272,120 | 0.4% | 93.7% |  |
| CALL_BUILTIN_O | 10,240,540 | 0.4% | 94.1% |  |
| POP_JUMP_IF_TRUE | 10,087,300 | 0.4% | 94.5% |  |
| CONTAINS_OP | 8,957,920 | 0.3% | 94.8% |  |
| CALL_LIST_APPEND | 8,957,720 | 0.3% | 95.1% |  |
| END_SEND | 6,915,160 | 0.3% | 95.4% |  |
| GET_AWAITABLE | 6,915,160 | 0.3% | 95.7% |  |
| SEND_GEN | 6,736,440 | 0.3% | 95.9% |  |
| BINARY_OP_SUBTRACT_INT | 6,347,220 | 0.2% | 96.2% |  |
| COMPARE_OP_FLOAT | 6,002,760 | 0.2% | 96.4% |  |
| FOR_ITER_LIST | 5,975,500 | 0.2% | 96.6% |  |
| COPY_FREE_VARS | 5,604,900 | 0.2% | 96.8% |  |
| TO_BOOL | 5,231,700 | 0.2% | 97.0% |  |
| STORE_ATTR | 5,230,120 | 0.2% | 97.2% |  |
| FOR_ITER_TUPLE | 5,225,380 | 0.2% | 97.4% |  |
| TO_BOOL_LIST | 4,671,900 | 0.2% | 97.6% |  |
| CALL_BUILTIN_FAST | 4,668,340 | 0.2% | 97.8% |  |
| JUMP_FORWARD | 4,483,220 | 0.2% | 98.0% |  |
| COPY | 4,481,460 | 0.2% | 98.1% |  |
| STORE_SUBSCR_DICT | 4,480,700 | 0.2% | 98.3% |  |
| IS_OP | 4,479,280 | 0.2% | 98.5% |  |
| CALL_TYPE_1 | 4,478,940 | 0.2% | 98.7% |  |
| LIST_APPEND | 4,478,880 | 0.2% | 98.8% |  |
| MAKE_CELL | 3,732,480 | 0.1% | 99.0% |  |
| GET_ITER | 2,991,700 | 0.1% | 99.1% |  |
| SWAP | 2,239,780 | 0.1% | 99.2% |  |
| CALL_ISINSTANCE | 2,081,380 | 0.1% | 99.2% |  |
| CALL_PY_WITH_DEFAULTS | 2,057,900 | 0.1% | 99.3% |  |
| SEND | 1,872,520 | 0.1% | 99.4% |  |
| LOAD_ATTR_CLASS | 1,868,440 | 0.1% | 99.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,868,360 | 0.1% | 99.5% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,692,840 | 0.1% | 99.6% |  |
| YIELD_VALUE | 1,692,840 | 0.1% | 99.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,681,060 | 0.1% | 99.7% |  |
| LOAD_SUPER_ATTR_METHOD | 1,125,520 | 0.0% | 99.8% |  |
| BUILD_MAP | 936,120 | 0.0% | 99.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 749,740 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 749,000 | 0.0% | 99.9% |  |
| BUILD_TUPLE | 747,120 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 746,720 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 746,720 | 0.0% | 99.9% |  |
| LOAD_FAST_AND_CLEAR | 746,480 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 191,040 | 0.0% | 100.0% |  |
| COMPARE_OP | 190,380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 189,440 | 0.0% | 100.0% |  |
| CALL_LEN | 5,460 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,900 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 2,200 | 0.0% | 100.0% |  |
| RESUME | 2,020 | 0.0% | 100.0% | 2,216.8% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 2,020 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 95,437,240 | 3.6% | 3.6% |
| POP_JUMP_IF_FALSE LOAD_FAST | 90,609,600 | 3.5% | 7.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 87,033,120 | 3.3% | 10.4% |
| STORE_FAST LOAD_FAST | 86,832,960 | 3.3% | 13.7% |
| LOAD_FAST LOAD_ATTR_SLOT | 80,545,360 | 3.1% | 16.8% |
| RESUME_CHECK LOAD_FAST | 74,701,560 | 2.8% | 19.6% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 57,340,020 | 2.2% | 21.8% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 40,520,880 | 1.5% | 23.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 39,777,160 | 1.5% | 24.9% |
| LOAD_FAST LOAD_ATTR | 39,021,060 | 1.5% | 26.4% |
| CACHE RESUME_CHECK | 37,555,520 | 1.4% | 27.8% |
| LOAD_CONST LOAD_FAST | 36,803,780 | 1.4% | 29.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 35,476,080 | 1.4% | 30.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 34,929,720 | 1.3% | 31.9% |
| LOAD_ATTR_MODULE PUSH_NULL | 34,740,960 | 1.3% | 33.2% |
| LOAD_FAST STORE_ATTR_SLOT | 31,384,560 | 1.2% | 34.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 30,806,820 | 1.2% | 35.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 30,248,820 | 1.2% | 36.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 29,138,560 | 1.1% | 37.8% |
| RETURN_CONST INTERPRETER_EXIT | 28,935,180 | 1.1% | 38.9% |
| LOAD_FAST RETURN_VALUE | 28,384,100 | 1.1% | 40.0% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 26,515,280 | 1.0% | 41.0% |
| RETURN_CONST POP_TOP | 25,408,200 | 1.0% | 42.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 25,200,540 | 1.0% | 43.0% |
| POP_TOP LOAD_FAST | 25,026,920 | 1.0% | 43.9% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 24,836,020 | 0.9% | 44.9% |
| CALL STORE_FAST | 24,645,460 | 0.9% | 45.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 23,528,320 | 0.9% | 46.7% |
| PUSH_NULL LOAD_FAST | 23,127,020 | 0.9% | 47.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 22,962,980 | 0.9% | 48.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 22,411,540 | 0.9% | 49.3% |
| STORE_ATTR_SLOT LOAD_CONST | 20,544,540 | 0.8% | 50.1% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 20,354,800 | 0.8% | 50.9% |
| POP_JUMP_IF_FALSE LOAD_CONST | 19,235,760 | 0.7% | 51.6% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 19,040,860 | 0.7% | 52.3% |
| LOAD_ATTR CALL_METHOD_DESCRIPTOR_NOARGS | 18,104,680 | 0.7% | 53.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS TO_BOOL_BOOL | 18,104,640 | 0.7% | 53.7% |
| RETURN_VALUE INTERPRETER_EXIT | 17,578,660 | 0.7% | 54.4% |
| RETURN_VALUE STORE_FAST | 17,368,360 | 0.7% | 55.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 16,959,780 | 0.6% | 55.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 16,619,520 | 0.6% | 56.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 16,430,020 | 0.6% | 56.9% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 15,687,300 | 0.6% | 57.5% |
| NOP LOAD_FAST | 15,500,280 | 0.6% | 58.1% |
| LOAD_CONST STORE_FAST | 15,317,520 | 0.6% | 58.7% |
| POP_TOP RETURN_CONST | 14,752,240 | 0.6% | 59.3% |
| RETURN_VALUE TO_BOOL_BOOL | 14,751,560 | 0.6% | 59.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 14,751,480 | 0.6% | 60.4% |
| LOAD_FAST LOAD_CONST | 14,568,340 | 0.6% | 60.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 14,562,240 | 0.6% | 61.5% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 14,562,080 | 0.6% | 62.1% |
| JUMP_BACKWARD FOR_ITER_RANGE | 14,561,720 | 0.6% | 62.6% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 14,561,720 | 0.6% | 63.2% |
| FOR_ITER_RANGE STORE_FAST | 14,561,720 | 0.6% | 63.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST_LOAD_FAST | 13,626,040 | 0.5% | 64.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 11,955,520 | 0.5% | 64.7% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 11,951,560 | 0.5% | 65.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 11,761,920 | 0.4% | 65.6% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 11,230,680 | 0.4% | 66.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 11,047,200 | 0.4% | 66.4% |
| RESUME_CHECK NOP | 10,829,980 | 0.4% | 66.9% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 10,826,240 | 0.4% | 67.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 10,826,000 | 0.4% | 67.7% |
| STORE_ATTR_SLOT LOAD_FAST | 10,650,820 | 0.4% | 68.1% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 10,650,640 | 0.4% | 68.5% |
| LOAD_CONST CALL_KW | 10,640,200 | 0.4% | 68.9% |
| STORE_ATTR_SLOT RETURN_CONST | 10,461,600 | 0.4% | 69.3% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 0.4% | 69.7% |
| POP_TOP RESUME_CHECK | 10,458,260 | 0.4% | 70.1% |
| PUSH_NULL CALL | 10,275,260 | 0.4% | 70.5% |
| POP_TOP LOAD_CONST | 10,274,700 | 0.4% | 70.9% |
| LOAD_ATTR PUSH_NULL | 10,273,080 | 0.4% | 71.3% |
| BUILD_LIST LOAD_FAST | 10,272,360 | 0.4% | 71.7% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 10,272,160 | 0.4% | 72.1% |
| LIST_EXTEND CALL_INTRINSIC_1 | 10,272,120 | 0.4% | 72.4% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 10,268,900 | 0.4% | 72.8% |
| LOAD_FAST CALL | 10,085,120 | 0.4% | 73.2% |
| STORE_FAST RETURN_CONST | 10,084,720 | 0.4% | 73.6% |
| LOAD_FAST_LOAD_FAST CALL | 10,083,080 | 0.4% | 74.0% |
| CALL_FUNCTION_EX POP_TOP | 10,083,040 | 0.4% | 74.4% |
| LOAD_ATTR_SLOT LOAD_ATTR | 10,082,980 | 0.4% | 74.8% |
| POP_TOP JUMP_BACKWARD | 10,082,920 | 0.4% | 75.1% |
| CALL_INTRINSIC_1 CALL_FUNCTION_EX | 10,082,880 | 0.4% | 75.5% |
| LOAD_ATTR_SLOT BUILD_LIST | 10,082,860 | 0.4% | 75.9% |
| LOAD_ATTR_SLOT LIST_EXTEND | 10,082,860 | 0.4% | 76.3% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 9,903,880 | 0.4% | 76.7% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,893,900 | 0.4% | 77.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 9,676,220 | 0.4% | 77.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 9,336,860 | 0.4% | 77.8% |
| LOAD_ATTR CALL | 8,959,740 | 0.3% | 78.1% |
| LOAD_FAST POP_JUMP_IF_NONE | 8,958,320 | 0.3% | 78.5% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 8,958,060 | 0.3% | 78.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 8,957,920 | 0.3% | 79.1% |
| LOAD_DEREF LOAD_CONST | 8,957,920 | 0.3% | 79.5% |
| POP_JUMP_IF_NONE LOAD_DEREF | 8,957,760 | 0.3% | 79.8% |
| BINARY_OP_ADD_INT STORE_DEREF | 8,957,720 | 0.3% | 80.2% |
| CALL_LIST_APPEND JUMP_BACKWARD | 8,957,720 | 0.3% | 80.5% |
| LOAD_FAST CALL_LIST_APPEND | 8,957,680 | 0.3% | 80.8% |
| LOAD_CONST COMPARE_OP_INT | 8,217,720 | 0.3% | 81.2% |
| CALL_BUILTIN_O STORE_FAST | 8,187,060 | 0.3% | 81.5% |


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
| RESUME_CHECK | 10,829,980 | 69.9% |
| POP_JUMP_IF_NOT_NONE | 3,732,560 | 24.1% |
| STORE_FAST | 937,720 | 6.0% |
| POP_TOP | 400 | 0.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,500,280 | 100.0% |
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
| RETURN_CONST | 25,408,200 | 33.3% |
| CALL_METHOD_DESCRIPTOR_O | 19,040,860 | 25.0% |
| CALL_FUNCTION_EX | 10,083,040 | 13.2% |
| SEND_GEN | 5,979,320 | 7.8% |
| CALL | 5,415,400 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,026,920 | 32.8% |
| RETURN_CONST | 14,752,240 | 19.4% |
| RESUME_CHECK | 10,458,260 | 13.7% |
| LOAD_CONST | 10,274,700 | 13.5% |
| JUMP_BACKWARD | 10,082,920 | 13.2% |


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
| LOAD_ATTR_MODULE | 34,740,960 | 66.0% |
| LOAD_ATTR | 10,273,080 | 19.5% |
| LOAD_FAST | 7,618,840 | 14.5% |
| LOAD_DEREF | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,127,020 | 43.9% |
| LOAD_FAST_LOAD_FAST | 14,562,080 | 27.7% |
| CALL | 10,275,260 | 19.5% |
| LOAD_GLOBAL_MODULE | 2,053,320 | 3.9% |
| LOAD_CONST | 1,868,560 | 3.6% |


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
| LOAD_FAST | 28,384,100 | 43.9% |
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
| LOAD_ATTR_SLOT | 10,082,860 | 76.0% |
| STORE_FAST | 748,320 | 5.6% |
| POP_JUMP_IF_FALSE | 746,480 | 5.6% |
| STORE_DEREF | 746,480 | 5.6% |
| SWAP | 746,480 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,272,360 | 77.5% |
| STORE_FAST | 1,494,800 | 11.3% |
| STORE_DEREF | 746,480 | 5.6% |
| SWAP | 746,480 | 5.6% |


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
| LOAD_ATTR | 8,959,740 | 20.4% |
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
| CALL_INTRINSIC_1 | 10,082,880 | 91.5% |
| STORE_FAST | 746,480 | 6.8% |
| BUILD_MAP | 189,240 | 1.7% |
| DICT_MERGE | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

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
| LIST_EXTEND | 10,272,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 10,082,880 | 98.2% |
| LOAD_CONST | 189,240 | 1.8% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,640,200 | 100.0% |

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
| POP_TOP | 10,082,920 | 42.3% |
| CALL_LIST_APPEND | 8,957,720 | 37.6% |
| LIST_APPEND | 4,478,880 | 18.8% |
| POP_JUMP_IF_FALSE | 306,000 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 14,561,720 | 61.1% |
| FOR_ITER_TUPLE | 4,478,880 | 18.8% |
| FOR_ITER_LIST | 4,478,860 | 18.8% |
| LOAD_FAST | 305,980 | 1.3% |
| FOR_ITER | 80 | 0.0% |


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
| LOAD_ATTR_SLOT | 10,082,860 | 98.2% |
| LOAD_FAST | 189,240 | 1.8% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 10,272,120 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 39,021,060 | 79.4% |
| LOAD_ATTR_SLOT | 10,082,980 | 20.5% |
| LOAD_ATTR | 15,880 | 0.0% |
| LOAD_GLOBAL_MODULE | 1,040 | 0.0% |
| LOAD_GLOBAL | 1,020 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,104,680 | 36.9% |
| PUSH_NULL | 10,273,080 | 20.9% |
| CALL | 8,959,740 | 18.2% |
| LOAD_FAST | 4,669,380 | 9.5% |
| TO_BOOL_NONE | 4,478,920 | 9.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 20,544,540 | 19.6% |
| POP_JUMP_IF_FALSE | 19,235,760 | 18.4% |
| LOAD_FAST | 14,568,340 | 13.9% |
| LOAD_FAST_LOAD_FAST | 10,826,240 | 10.3% |
| POP_TOP | 10,274,700 | 9.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,803,780 | 35.1% |
| STORE_FAST | 15,317,520 | 14.6% |
| BINARY_OP_ADD_INT | 10,826,000 | 10.3% |
| CALL_KW | 10,640,200 | 10.2% |
| COMPARE_OP_INT | 8,217,720 | 7.8% |


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
| POP_JUMP_IF_FALSE | 90,609,600 | 18.8% |
| STORE_FAST | 86,832,960 | 18.0% |
| RESUME_CHECK | 74,701,560 | 15.5% |
| LOAD_CONST | 36,803,780 | 7.6% |
| LOAD_ATTR_METHOD_NO_DICT | 25,200,540 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 95,437,240 | 19.8% |
| LOAD_ATTR_SLOT | 80,545,360 | 16.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 39,777,160 | 8.2% |
| LOAD_ATTR | 39,021,060 | 8.1% |
| STORE_ATTR_SLOT | 31,384,560 | 6.5% |


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
| STORE_ATTR_SLOT | 30,248,820 | 27.2% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 13.3% |
| PUSH_NULL | 14,562,080 | 13.1% |
| POP_JUMP_IF_NOT_NONE | 13,626,040 | 12.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,761,920 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 40,520,880 | 36.4% |
| LOAD_FAST_LOAD_FAST | 14,751,480 | 13.3% |
| LOAD_FAST | 14,562,240 | 13.1% |
| LOAD_CONST | 10,826,240 | 9.7% |
| CALL | 10,083,080 | 9.1% |


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
| TO_BOOL_BOOL | 87,033,120 | 56.0% |
| TO_BOOL_NONE | 24,836,020 | 16.0% |
| COMPARE_OP_INT | 16,959,780 | 10.9% |
| CONTAINS_OP | 8,957,920 | 5.8% |
| TO_BOOL_LIST | 4,671,900 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 90,609,600 | 58.3% |
| RETURN_CONST | 22,962,980 | 14.8% |
| LOAD_CONST | 19,235,760 | 12.4% |
| LOAD_GLOBAL_MODULE | 9,903,880 | 6.4% |
| LOAD_DEREF | 5,225,360 | 3.4% |


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
| CALL | 24,645,460 | 20.8% |
| RETURN_VALUE | 17,368,360 | 14.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 16,430,020 | 13.9% |
| LOAD_CONST | 15,317,520 | 12.9% |
| FOR_ITER_RANGE | 14,561,720 | 12.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,832,960 | 73.2% |
| RETURN_CONST | 10,084,720 | 8.5% |
| LOAD_FAST_LOAD_FAST | 9,676,220 | 8.2% |
| LOAD_GLOBAL_MODULE | 6,347,360 | 5.4% |
| LOAD_CONST | 1,682,280 | 1.4% |


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
| LOAD_CONST | 189,400 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 189,300 | 99.9% |
| LOAD_ATTR_SLOT | 120 | 0.1% |
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
| LOAD_FAST | 8,186,980 | 79.9% |
| LOAD_GLOBAL_MODULE | 1,864,120 | 18.2% |
| LOAD_ATTR_INSTANCE_VALUE | 189,200 | 1.8% |
| CALL | 200 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,187,060 | 79.9% |
| RETURN_VALUE | 1,864,140 | 18.2% |
| TO_BOOL_BOOL | 189,200 | 1.8% |
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
| JUMP_BACKWARD | 8,957,720 | 100.0% |


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
| LOAD_ATTR | 18,104,680 | 52.3% |
| LOAD_ATTR_METHOD_NO_DICT | 11,951,560 | 34.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,478,840 | 12.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.2% |
| CALL | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 18,104,640 | 52.3% |
| STORE_FAST | 16,430,020 | 47.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 86,120 | 0.2% |
| POP_TOP | 380 | 0.0% |
| GET_ITER | 160 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,561,720 | 76.5% |
| CALL | 4,479,060 | 23.5% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 19,040,860 | 100.0% |
| LOAD_CONST | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 29,138,560 | 43.0% |
| LOAD_FAST | 23,528,320 | 34.7% |
| LOAD_ATTR_METHOD_NO_DICT | 10,272,160 | 15.2% |
| BINARY_OP_SUBTRACT_INT | 4,478,840 | 6.6% |
| LOAD_SUPER_ATTR_METHOD | 189,400 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 57,340,020 | 84.6% |
| RETURN_GENERATOR | 10,268,900 | 15.1% |
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
| LOAD_GLOBAL_MODULE | 3,732,560 | 62.2% |
| LOAD_ATTR_SLOT | 2,080,840 | 34.7% |
| LOAD_FAST | 189,280 | 3.2% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,921,900 | 65.3% |
| RETURN_VALUE | 2,080,860 | 34.7% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,217,720 | 48.5% |
| LOAD_DEREF | 4,478,840 | 26.4% |
| LOAD_FAST_LOAD_FAST | 2,392,900 | 14.1% |
| LOAD_GLOBAL_MODULE | 1,870,080 | 11.0% |
| COMPARE_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,959,780 | 100.0% |


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
| JUMP_BACKWARD | 14,561,720 | 95.1% |
| SWAP | 746,460 | 4.9% |
| GET_ITER | 1,820 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,561,720 | 95.1% |
| SWAP | 746,480 | 4.9% |
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
| LOAD_FAST | 95,437,240 | 94.8% |
| LOAD_FAST_LOAD_FAST | 4,479,120 | 4.4% |
| LOAD_DEREF | 746,440 | 0.7% |
| LOAD_ATTR | 1,540 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 35,476,080 | 35.2% |
| LOAD_ATTR_METHOD_NO_DICT | 30,806,820 | 30.6% |
| RETURN_VALUE | 15,687,300 | 15.6% |
| TO_BOOL_LIST | 4,671,820 | 4.6% |
| TO_BOOL | 4,481,060 | 4.5% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 30,806,820 | 59.4% |
| LOAD_FAST | 16,619,520 | 32.0% |
| LOAD_DEREF | 4,478,840 | 8.6% |
| LOAD_ATTR | 620 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,200,540 | 48.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,951,560 | 23.0% |
| CALL_PY_EXACT_ARGS | 10,272,160 | 19.8% |
| LOAD_GLOBAL_MODULE | 4,478,960 | 8.6% |
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
| LOAD_GLOBAL_MODULE | 34,929,720 | 100.0% |
| LOAD_ATTR | 1,020 | 0.0% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 34,740,960 | 99.5% |
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
| LOAD_FAST | 80,545,360 | 100.0% |
| LOAD_ATTR_SLOT | 8,040 | 0.0% |
| LOAD_ATTR | 480 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR_MODULE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 20,354,800 | 25.3% |
| TO_BOOL_BOOL | 10,650,640 | 13.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,461,400 | 13.0% |
| LOAD_ATTR | 10,082,980 | 12.5% |
| BUILD_LIST | 10,082,860 | 12.5% |


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
| RESUME_CHECK | 22,411,540 | 33.4% |
| POP_JUMP_IF_FALSE | 9,903,880 | 14.8% |
| POP_JUMP_IF_NOT_NONE | 8,029,720 | 12.0% |
| STORE_FAST | 6,347,360 | 9.5% |
| LOAD_ATTR_METHOD_NO_DICT | 4,478,960 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 34,929,720 | 52.1% |
| LOAD_FAST_LOAD_FAST | 8,958,060 | 13.4% |
| LOAD_FAST | 5,605,420 | 8.4% |
| CONTAINS_OP | 4,478,940 | 6.7% |
| COMPARE_OP_FLOAT | 3,732,560 | 5.6% |


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
| CALL_PY_EXACT_ARGS | 57,340,020 | 45.7% |
| CACHE | 37,555,520 | 30.0% |
| POP_TOP | 10,458,260 | 8.3% |
| COPY_FREE_VARS | 5,604,460 | 4.5% |
| CALL | 4,668,800 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,701,560 | 59.6% |
| LOAD_GLOBAL_MODULE | 22,411,540 | 17.9% |
| LOAD_GLOBAL_BUILTIN | 11,230,680 | 9.0% |
| NOP | 10,829,980 | 8.6% |
| LOAD_DEREF | 4,478,920 | 3.6% |


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
| LOAD_FAST_LOAD_FAST | 40,520,880 | 56.3% |
| LOAD_FAST | 31,384,560 | 43.6% |
| STORE_ATTR_SLOT | 47,320 | 0.1% |
| STORE_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 30,248,820 | 42.0% |
| LOAD_CONST | 20,544,540 | 28.6% |
| LOAD_FAST | 10,650,820 | 14.8% |
| RETURN_CONST | 10,461,600 | 14.5% |
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
| LOAD_ATTR_INSTANCE_VALUE | 35,476,080 | 36.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,104,640 | 18.8% |
| RETURN_VALUE | 14,751,560 | 15.3% |
| LOAD_ATTR_SLOT | 10,650,640 | 11.1% |
| COPY | 4,479,080 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 87,033,120 | 90.3% |
| POP_JUMP_IF_TRUE | 9,336,860 | 9.7% |
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
| LOAD_ATTR_INSTANCE_VALUE | 4,671,820 | 100.0% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,671,900 | 100.0% |


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
|          hit | 26,510,920 | 100.0% |

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
|     deferred | 49,538,560 | 13.2% |
|          hit | 326,816,600 | 86.8% |
|         miss | 443,420 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 13,320 | 46.8% |
| Failure | 15,120 | 53.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 9,560 | 63.2% |
| method | 4,040 | 26.7% |
| class attr descriptor | 1,280 | 8.5% |
| not managed dict | 140 | 0.9% |
| metaclass attribute | 60 | 0.4% |
| class attr simple | 40 | 0.3% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,600 | 0.0% |
|        deopt | 80 | 0.0% |
|          hit | 79,992,740 | 100.0% |
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
| Basic | 1,338,336,880 | 51.0% |
| Not specialized | 315,605,220 | 12.0% |
| Specialized hits | 963,108,500 | 36.7% |
| Specialized misses | 7,564,800 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 49,538,560 | 43.9% |
| CALL | 48,361,560 | 42.8% |
| STORE_ATTR | 7,689,180 | 6.8% |
| TO_BOOL | 5,230,300 | 4.6% |
| SEND | 1,871,560 | 1.7% |
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
| CALL_METHOD_DESCRIPTOR_NOARGS | 4,565,240 | 60.0% |
| STORE_ATTR_SLOT | 2,509,460 | 33.0% |
| LOAD_ATTR_SLOT | 426,460 | 5.6% |
| RESUME | 44,780 | 0.6% |
| RESUME_CHECK | 44,780 | 0.6% |
| LOAD_ATTR_METHOD_NO_DICT | 16,960 | 0.2% |
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
| Frames pushed | 71,725,120 | 52.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 65,056,212 | 18.4% |
| Frees to freelist | 65,505,812 |  |
| Allocations | 288,919,559 | 81.6% |
| Allocations to 512 bytes | 286,995,416 | 81.1% |
| Allocations to 4 kbytes | 1,924,020 | 0.5% |
| Allocations over 4 kbytes | 123 | 0.0% |
| Frees | 291,026,319 |  |
| New values | 420 |  |
| Interpreter increfs | 1,285,364,740 | 78.9% |
| Interpreter decrefs | 1,350,255,888 | 68.8% |
| Increfs | 343,944,206 | 21.1% |
| Decrefs | 611,904,802 | 31.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 87,173,566 |  |
| Method cache misses | 2,609,714 |  |
| Method cache collisions | 2,636,808 |  |
| Method cache dunder hits | 12,882,987 |  |
| Method cache dunder misses | 29,113 |  |


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
