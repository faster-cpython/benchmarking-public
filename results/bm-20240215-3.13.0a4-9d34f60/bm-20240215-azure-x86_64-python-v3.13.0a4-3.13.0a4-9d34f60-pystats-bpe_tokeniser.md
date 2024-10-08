
# Pystats results

- benchmark: bpe_tokeniser
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 6,424,446,000 | 16.8% | 16.8% |  |
| LOAD_CONST | 4,578,643,080 | 11.9% | 28.7% |  |
| STORE_FAST | 2,497,913,320 | 6.5% | 35.2% |  |
| LOAD_FAST_LOAD_FAST | 1,725,739,940 | 4.5% | 39.7% |  |
| BINARY_SUBSCR_LIST_INT | 1,721,677,300 | 4.5% | 44.2% | 0.0% |
| POP_JUMP_IF_FALSE | 1,676,478,480 | 4.4% | 48.6% |  |
| LOAD_GLOBAL_BUILTIN | 1,641,621,380 | 4.3% | 52.9% |  |
| JUMP_BACKWARD | 1,517,894,600 | 4.0% | 56.8% |  |
| BINARY_OP_ADD_INT | 1,328,114,540 | 3.5% | 60.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,242,524,660 | 3.2% | 63.5% |  |
| COMPARE_OP_INT | 1,237,349,220 | 3.2% | 66.8% |  |
| CALL_LEN | 1,235,194,920 | 3.2% | 70.0% |  |
| BINARY_OP_SUBTRACT_INT | 1,235,069,160 | 3.2% | 73.2% |  |
| CALL_LIST_APPEND | 1,234,381,260 | 3.2% | 76.4% |  |
| SWAP | 888,109,280 | 2.3% | 78.7% |  |
| COPY | 884,491,180 | 2.3% | 81.1% |  |
| FOR_ITER | 854,246,440 | 2.2% | 83.3% |  |
| BINARY_SLICE | 801,520,160 | 2.1% | 85.4% |  |
| FOR_ITER_LIST | 796,311,960 | 2.1% | 87.5% |  |
| BINARY_SUBSCR | 587,617,360 | 1.5% | 89.0% |  |
| LOAD_DEREF | 587,596,320 | 1.5% | 90.5% |  |
| STORE_SUBSCR | 442,355,720 | 1.2% | 91.7% |  |
| BUILD_TUPLE | 441,388,880 | 1.2% | 92.8% |  |
| COMPARE_OP | 441,372,160 | 1.2% | 94.0% |  |
| BUILD_LIST | 405,200,740 | 1.1% | 95.0% |  |
| CALL | 404,331,200 | 1.1% | 96.1% |  |
| GET_ITER | 400,765,980 | 1.0% | 97.1% |  |
| RESUME_CHECK | 291,109,320 | 0.8% | 97.9% |  |
| INTERPRETER_EXIT | 290,582,360 | 0.8% | 98.6% |  |
| RETURN_VALUE | 145,753,960 | 0.4% | 99.0% |  |
| RETURN_CONST | 145,355,400 | 0.4% | 99.4% |  |
| COPY_FREE_VARS | 145,350,800 | 0.4% | 99.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 13,307,240 | 0.0% | 99.8% |  |
| BINARY_OP | 11,669,240 | 0.0% | 99.9% |  |
| POP_JUMP_IF_NOT_NONE | 10,450,020 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,676,280 | 0.0% | 99.9% |  |
| STORE_FAST_STORE_FAST | 6,676,120 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 6,591,120 | 0.0% | 99.9% |  |
| LIST_APPEND | 6,340,320 | 0.0% | 99.9% |  |
| POP_JUMP_IF_NONE | 3,950,720 | 0.0% | 100.0% |  |
| POP_JUMP_IF_TRUE | 2,227,720 | 0.0% | 100.0% |  |
| JUMP_FORWARD | 2,188,640 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 2,187,680 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 1,551,200 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 1,347,040 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,034,060 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 828,020 | 0.0% | 100.0% |  |
| POP_TOP | 649,280 | 0.0% | 100.0% |  |
| LOAD_GLOBAL_MODULE | 600,800 | 0.0% | 100.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 530,360 | 0.0% | 100.0% |  |
| CALL_PY_EXACT_ARGS | 521,360 | 0.0% | 100.0% |  |
| NOP | 520,980 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_O | 517,280 | 0.0% | 100.0% |  |
| PUSH_NULL | 135,800 | 0.0% | 100.0% |  |
| MAP_ADD | 81,920 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 81,920 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 68,380 | 0.0% | 100.0% |  |
| LOAD_ATTR | 67,080 | 0.0% | 100.0% |  |
| LOAD_ATTR_MODULE | 65,540 | 0.0% | 100.0% |  |
| TO_BOOL | 63,480 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 62,240 | 0.0% | 100.0% |  |
| CALL_KW | 61,760 | 0.0% | 100.0% |  |
| BUILD_MAP | 61,640 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 61,520 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 61,520 | 0.0% | 100.0% |  |
| DICT_MERGE | 61,440 | 0.0% | 100.0% |  |
| STORE_DEREF | 61,440 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 61,420 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 23,640 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 7,160 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 6,940 | 0.0% | 100.0% | 0.9% |
| IS_OP | 6,320 | 0.0% | 100.0% |  |
| TO_BOOL_BOOL | 5,820 | 0.0% | 100.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 5,140 | 0.0% | 100.0% |  |
| CONTAINS_OP | 4,340 | 0.0% | 100.0% |  |
| CALL_ISINSTANCE | 4,060 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 3,560 | 0.0% | 100.0% | 0.6% |
| TO_BOOL_INT | 2,620 | 0.0% | 100.0% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,520 | 0.0% | 100.0% |  |
| CALL_STR_1 | 2,520 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 2,360 | 0.0% | 100.0% | 0.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,280 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 2,220 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,920 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 1,500 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 1,020 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 1,000 | 0.0% | 100.0% | 20.0% |
| STORE_SUBSCR_LIST_INT | 800 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 780 | 0.0% | 100.0% |  |
| RESUME | 660 | 0.0% | 100.0% |  |
| LOAD_ATTR_PROPERTY | 600 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 560 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 540 | 0.0% | 100.0% | 7.4% |
| STORE_ATTR | 520 | 0.0% | 100.0% |  |
| UNARY_NOT | 500 | 0.0% | 100.0% |  |
| TO_BOOL_NONE | 440 | 0.0% | 100.0% | 18.2% |
| BINARY_OP_ADD_UNICODE | 440 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 420 | 0.0% | 100.0% |  |
| YIELD_VALUE | 400 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 300 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 300 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 280 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 280 | 0.0% | 100.0% |  |
| POP_EXCEPT | 280 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 280 | 0.0% | 100.0% |  |
| BUILD_SLICE | 260 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 220 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 200 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 200 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 180 | 0.0% | 100.0% |  |
| MAKE_CELL | 160 | 0.0% | 100.0% |  |
| CALL_PY_WITH_DEFAULTS | 140 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 120 | 0.0% | 100.0% | 33.3% |
| BEFORE_WITH | 80 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 80 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 80 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 1,639,305,040 | 4.3% | 4.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,328,114,160 | 3.5% | 7.7% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR_LIST_INT | 1,278,741,200 | 3.3% | 11.1% |
| LOAD_FAST LOAD_CONST | 1,254,430,780 | 3.3% | 14.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,242,006,380 | 3.2% | 17.6% |
| LOAD_FAST CALL_LEN | 1,235,193,320 | 3.2% | 20.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,235,130,620 | 3.2% | 24.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 1,235,086,960 | 3.2% | 27.3% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,235,071,160 | 3.2% | 30.5% |
| CALL_LEN LOAD_CONST | 1,235,068,480 | 3.2% | 33.7% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 1,235,067,960 | 3.2% | 36.9% |
| BINARY_OP_SUBTRACT_INT COMPARE_OP_INT | 1,235,067,800 | 3.2% | 40.1% |
| STORE_FAST LOAD_FAST | 847,110,660 | 2.2% | 42.4% |
| CALL_LIST_APPEND LOAD_FAST | 837,477,720 | 2.2% | 44.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST | 835,808,380 | 2.2% | 46.7% |
| BINARY_SUBSCR_LIST_INT CALL_LIST_APPEND | 835,808,000 | 2.2% | 48.9% |
| LOAD_CONST BINARY_SLICE | 799,850,000 | 2.1% | 51.0% |
| LOAD_CONST LOAD_CONST | 798,180,600 | 2.1% | 53.1% |
| JUMP_BACKWARD FOR_ITER_LIST | 795,669,800 | 2.1% | 55.1% |
| FOR_ITER_LIST STORE_FAST | 794,840,340 | 2.1% | 57.2% |
| LOAD_DEREF LOAD_FAST | 587,595,680 | 1.5% | 58.8% |
| JUMP_BACKWARD FOR_ITER | 453,912,040 | 1.2% | 59.9% |
| FOR_ITER STORE_FAST | 447,756,140 | 1.2% | 61.1% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 444,604,080 | 1.2% | 62.3% |
| BINARY_SUBSCR_LIST_INT LOAD_FAST_LOAD_FAST | 442,933,240 | 1.2% | 63.4% |
| BINARY_OP_ADD_INT BINARY_SUBSCR_LIST_INT | 442,933,200 | 1.2% | 64.6% |
| STORE_SUBSCR JUMP_BACKWARD | 442,247,140 | 1.2% | 65.7% |
| STORE_FAST LOAD_DEREF | 442,245,440 | 1.2% | 66.9% |
| LOAD_FAST COPY | 442,245,120 | 1.2% | 68.0% |
| BINARY_SUBSCR LOAD_CONST | 442,245,040 | 1.2% | 69.2% |
| COPY BINARY_SUBSCR | 442,245,040 | 1.2% | 70.3% |
| COPY COPY | 442,245,040 | 1.2% | 71.5% |
| SWAP STORE_SUBSCR | 442,245,040 | 1.2% | 72.7% |
| SWAP SWAP | 442,245,040 | 1.2% | 73.8% |
| BINARY_OP_ADD_INT SWAP | 442,245,020 | 1.2% | 75.0% |
| BINARY_OP_ADD_INT STORE_FAST | 441,264,460 | 1.2% | 76.1% |
| BUILD_TUPLE LOAD_FAST | 441,263,700 | 1.2% | 77.3% |
| COMPARE_OP POP_JUMP_IF_FALSE | 441,263,580 | 1.2% | 78.4% |
| LOAD_FAST COMPARE_OP | 441,263,420 | 1.2% | 79.6% |
| BINARY_SUBSCR_LIST_INT BUILD_TUPLE | 441,263,100 | 1.2% | 80.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 405,682,020 | 1.1% | 81.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 404,208,480 | 1.1% | 82.8% |
| LOAD_CONST STORE_FAST | 401,278,820 | 1.0% | 83.9% |
| STORE_FAST LOAD_CONST | 399,093,580 | 1.0% | 84.9% |
| BINARY_SLICE LOAD_FAST | 399,089,920 | 1.0% | 86.0% |
| GET_ITER FOR_ITER | 399,089,780 | 1.0% | 87.0% |
| BINARY_SLICE CALL | 399,089,560 | 1.0% | 88.0% |
| LOAD_FAST CALL_LIST_APPEND | 398,572,840 | 1.0% | 89.1% |
| BUILD_LIST STORE_FAST | 396,965,180 | 1.0% | 90.1% |
| CALL_LIST_APPEND JUMP_BACKWARD | 396,902,840 | 1.0% | 91.1% |
| STORE_FAST BUILD_LIST | 396,902,760 | 1.0% | 92.2% |
| CALL GET_ITER | 396,902,500 | 1.0% | 93.2% |
| FOR_ITER JUMP_BACKWARD | 396,902,400 | 1.0% | 94.3% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 266,554,900 | 0.7% | 95.0% |
| JUMP_BACKWARD LOAD_FAST_LOAD_FAST | 266,554,880 | 0.7% | 95.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 174,709,020 | 0.5% | 96.1% |
| RETURN_CONST INTERPRETER_EXIT | 145,351,640 | 0.4% | 96.5% |
| CACHE COPY_FREE_VARS | 145,350,640 | 0.4% | 96.9% |
| COPY_FREE_VARS RESUME_CHECK | 145,350,620 | 0.4% | 97.2% |
| CACHE RESUME_CHECK | 145,231,800 | 0.4% | 97.6% |
| RETURN_VALUE INTERPRETER_EXIT | 145,230,320 | 0.4% | 98.0% |
| LOAD_FAST BINARY_SUBSCR | 145,227,680 | 0.4% | 98.4% |
| RESUME_CHECK LOAD_DEREF | 145,227,480 | 0.4% | 98.8% |
| BINARY_SUBSCR RETURN_VALUE | 145,227,440 | 0.4% | 99.1% |
| RESUME_CHECK RETURN_CONST | 145,227,420 | 0.4% | 99.5% |
| LOAD_CONST BINARY_SUBSCR_TUPLE_INT | 13,307,100 | 0.0% | 99.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 10,450,020 | 0.0% | 99.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 7,230,400 | 0.0% | 99.6% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 6,675,480 | 0.0% | 99.6% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 6,673,440 | 0.0% | 99.6% |
| BINARY_SUBSCR_TUPLE_INT LOAD_FAST | 6,652,540 | 0.0% | 99.6% |
| BINARY_SUBSCR_TUPLE_INT BINARY_OP | 6,652,280 | 0.0% | 99.7% |
| STORE_FAST_STORE_FAST LOAD_FAST | 6,592,600 | 0.0% | 99.7% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 6,591,100 | 0.0% | 99.7% |
| BINARY_OP CALL_METHOD_DESCRIPTOR_FAST | 6,590,840 | 0.0% | 99.7% |
| LIST_APPEND JUMP_BACKWARD | 6,340,320 | 0.0% | 99.7% |
| LOAD_FAST BUILD_LIST | 5,014,400 | 0.0% | 99.7% |
| BUILD_LIST CALL | 5,014,320 | 0.0% | 99.8% |
| CALL LIST_APPEND | 4,993,860 | 0.0% | 99.8% |
| LOAD_FAST STORE_FAST | 4,737,240 | 0.0% | 99.8% |
| STORE_FAST JUMP_BACKWARD | 4,008,660 | 0.0% | 99.8% |
| LOAD_FAST POP_JUMP_IF_NONE | 3,950,280 | 0.0% | 99.8% |
| POP_JUMP_IF_NOT_NONE JUMP_BACKWARD | 2,702,160 | 0.0% | 99.8% |
| POP_JUMP_IF_NONE LOAD_FAST_LOAD_FAST | 2,218,560 | 0.0% | 99.8% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 2,218,540 | 0.0% | 99.8% |
| LOAD_FAST_LOAD_FAST COMPARE_OP_INT | 2,218,520 | 0.0% | 99.8% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 2,187,420 | 0.0% | 99.8% |
| JUMP_FORWARD LOAD_FAST | 2,187,300 | 0.0% | 99.8% |
| CALL_BUILTIN_CLASS GET_ITER | 2,187,240 | 0.0% | 99.8% |
| CALL CALL_BUILTIN_CLASS | 2,187,140 | 0.0% | 99.9% |
| FOR_ITER LOAD_FAST | 2,187,140 | 0.0% | 99.9% |
| BINARY_OP STORE_FAST | 1,732,200 | 0.0% | 99.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 1,731,740 | 0.0% | 99.9% |
| LOAD_CONST LOAD_FAST | 1,671,160 | 0.0% | 99.9% |
| BINARY_SLICE BINARY_OP | 1,670,160 | 0.0% | 99.9% |
| BINARY_SLICE LOAD_FAST_LOAD_FAST | 1,670,160 | 0.0% | 99.9% |
| BINARY_OP BUILD_LIST | 1,670,160 | 0.0% | 99.9% |
| BINARY_OP LOAD_FAST_LOAD_FAST | 1,670,160 | 0.0% | 99.9% |
| BUILD_LIST BINARY_OP | 1,670,160 | 0.0% | 99.9% |
| JUMP_BACKWARD LOAD_CONST | 1,670,160 | 0.0% | 99.9% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 799,850,000 | 99.8% |
| LOAD_FAST | 1,670,160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 399,089,920 | 49.8% |
| CALL | 399,089,560 | 49.8% |
| BINARY_OP | 1,670,160 | 0.2% |
| LOAD_FAST_LOAD_FAST | 1,670,160 | 0.2% |
| BUILD_TUPLE | 160 | 0.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 145,350,640 | 50.0% |
| RESUME_CHECK | 145,231,800 | 50.0% |
| RESUME | 260 | 0.0% |
| POP_TOP | 80 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 100.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 160 | 57.1% |
| BINARY_SUBSCR_STR_INT | 120 | 42.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 160 | 57.1% |
| LOAD_FAST | 120 | 42.9% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 442,245,040 | 75.3% |
| LOAD_FAST | 145,227,680 | 24.7% |
| BINARY_SUBSCR | 143,840 | 0.0% |
| LOAD_CONST | 300 | 0.0% |
| BUILD_SLICE | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 442,245,040 | 75.3% |
| RETURN_VALUE | 145,227,440 | 24.7% |
| BINARY_SUBSCR | 143,840 | 0.0% |
| GET_ITER | 260 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 240 | 85.7% |
| LOAD_GLOBAL | 40 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 280 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 200 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 396,902,500 | 99.0% |
| CALL_BUILTIN_CLASS | 2,187,240 | 0.5% |
| LOAD_FAST | 1,158,380 | 0.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 516,920 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 399,089,780 | 99.6% |
| LOAD_FAST_AND_CLEAR | 1,551,040 | 0.4% |
| FOR_ITER_LIST | 123,340 | 0.0% |
| EXTENDED_ARG | 980 | 0.0% |
| FOR_ITER_RANGE | 460 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 145,351,640 | 50.0% |
| RETURN_VALUE | 145,230,320 | 50.0% |
| YIELD_VALUE | 400 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 61,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 61,520 | 100.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 518,980 | 99.6% |
| RESUME_CHECK | 640 | 0.1% |
| POP_JUMP_IF_FALSE | 500 | 0.1% |
| NOP | 220 | 0.0% |
| STORE_FAST_STORE_FAST | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 516,980 | 99.2% |
| LOAD_FAST | 2,960 | 0.6% |
| LOAD_GLOBAL_MODULE | 440 | 0.1% |
| NOP | 220 | 0.0% |
| EXTENDED_ARG | 120 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 240 | 85.7% |
| POP_TOP | 20 | 7.1% |
| STORE_ATTR_INSTANCE_VALUE | 20 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 240 | 85.7% |
| JUMP_FORWARD | 20 | 7.1% |
| RETURN_CONST | 20 | 7.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 517,080 | 79.6% |
| CALL | 61,760 | 9.5% |
| CALL_FUNCTION_EX | 61,760 | 9.5% |
| CALL_BUILTIN_O | 4,140 | 0.6% |
| RETURN_CONST | 2,640 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 518,380 | 79.8% |
| LOAD_FAST | 66,680 | 10.3% |
| RETURN_CONST | 62,360 | 9.6% |
| EXTENDED_ARG | 560 | 0.1% |
| LOAD_GLOBAL_MODULE | 540 | 0.1% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 200 | 71.4% |
| LOAD_ATTR | 40 | 14.3% |
| BINARY_SUBSCR_DICT | 20 | 7.1% |
| BINARY_SUBSCR_STR_INT | 20 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 200 | 71.4% |
| LOAD_GLOBAL | 80 | 28.6% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 64,840 | 47.7% |
| LOAD_ATTR | 61,640 | 45.4% |
| LOAD_FAST | 8,040 | 5.9% |
| STORE_FAST_LOAD_FAST | 560 | 0.4% |
| LOAD_SUPER_ATTR_ATTR | 300 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 67,020 | 49.4% |
| CALL | 61,680 | 45.4% |
| LOAD_GLOBAL_BUILTIN | 2,440 | 1.8% |
| LOAD_CONST | 1,600 | 1.2% |
| LOAD_GLOBAL_MODULE | 1,600 | 1.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 50.0% |
| CALL_METHOD_DESCRIPTOR_O | 40 | 50.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 145,227,440 | 99.6% |
| LOAD_FAST | 519,040 | 0.4% |
| BINARY_SUBSCR_LIST_INT | 2,220 | 0.0% |
| CALL_LEN | 1,140 | 0.0% |
| RETURN_VALUE | 580 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 145,230,320 | 99.6% |
| STORE_FAST | 518,400 | 0.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,380 | 0.0% |
| POP_TOP | 780 | 0.0% |
| LOAD_CONST | 700 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 442,245,040 | 100.0% |
| STORE_SUBSCR | 108,200 | 0.0% |
| LOAD_FAST_LOAD_FAST | 2,080 | 0.0% |
| LOAD_FAST | 200 | 0.0% |
| LOAD_CONST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 442,247,140 | 100.0% |
| STORE_SUBSCR | 108,200 | 0.0% |
| EXTENDED_ARG | 160 | 0.0% |
| RETURN_CONST | 160 | 0.0% |
| STORE_SUBSCR_DICT | 40 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,860 | 99.0% |
| TO_BOOL | 340 | 0.5% |
| COPY | 80 | 0.1% |
| CALL | 60 | 0.1% |
| CALL_ISINSTANCE | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 62,320 | 98.2% |
| POP_JUMP_IF_TRUE | 560 | 0.9% |
| TO_BOOL | 340 | 0.5% |
| TO_BOOL_STR | 140 | 0.2% |
| TO_BOOL_BOOL | 60 | 0.1% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 260 | 52.0% |
| TO_BOOL_LIST | 240 | 48.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 260 | 52.0% |
| CALL_PY_EXACT_ARGS | 240 | 48.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 6,652,280 | 57.0% |
| BINARY_SLICE | 1,670,160 | 14.3% |
| BUILD_LIST | 1,670,160 | 14.3% |
| BINARY_SUBSCR_LIST_INT | 1,670,140 | 14.3% |
| BINARY_OP | 3,900 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 6,590,840 | 56.5% |
| STORE_FAST | 1,732,200 | 14.8% |
| BUILD_LIST | 1,670,160 | 14.3% |
| LOAD_FAST_LOAD_FAST | 1,670,160 | 14.3% |
| BINARY_OP | 3,900 | 0.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 396,902,760 | 98.0% |
| LOAD_FAST | 5,014,400 | 1.2% |
| BINARY_OP | 1,670,160 | 0.4% |
| SWAP | 1,550,960 | 0.4% |
| STORE_SUBSCR_DICT | 61,420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 396,965,180 | 98.0% |
| CALL | 5,014,320 | 1.2% |
| BINARY_OP | 1,670,160 | 0.4% |
| SWAP | 1,550,960 | 0.4% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 61,440 | 99.7% |
| POP_JUMP_IF_FALSE | 80 | 0.1% |
| SWAP | 80 | 0.1% |
| STORE_ATTR_INSTANCE_VALUE | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,480 | 99.7% |
| STORE_FAST | 80 | 0.1% |
| SWAP | 80 | 0.1% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 260 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 260 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 441,263,100 | 100.0% |
| LOAD_FAST | 123,520 | 0.0% |
| LOAD_FAST_LOAD_FAST | 580 | 0.0% |
| CALL_BUILTIN_O | 560 | 0.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 441,263,700 | 100.0% |
| LOAD_CONST | 61,520 | 0.0% |
| BUILD_MAP | 61,440 | 0.0% |
| RETURN_VALUE | 460 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 440 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 399,089,560 | 98.7% |
| BUILD_LIST | 5,014,320 | 1.2% |
| CALL | 100,340 | 0.0% |
| PUSH_NULL | 61,680 | 0.0% |
| LOAD_SUPER_ATTR_METHOD | 61,420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 396,902,500 | 98.2% |
| LIST_APPEND | 4,993,860 | 1.2% |
| CALL_BUILTIN_CLASS | 2,187,140 | 0.5% |
| CALL | 100,340 | 0.0% |
| POP_TOP | 61,760 | 0.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 61,440 | 98.7% |
| LOAD_FAST | 720 | 1.2% |
| CALL_INTRINSIC_1 | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 61,760 | 99.2% |
| RETURN_VALUE | 240 | 0.4% |
| RESUME_CHECK | 140 | 0.2% |
| COPY_FREE_VARS | 80 | 0.1% |
| RESUME | 20 | 0.0% |


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
| LOAD_CONST | 61,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 61,440 | 99.5% |
| RETURN_VALUE | 160 | 0.3% |
| MAKE_CELL | 80 | 0.1% |
| RESUME_CHECK | 60 | 0.1% |
| RESUME | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 441,263,420 | 100.0% |
| COMPARE_OP | 107,980 | 0.0% |
| LOAD_GLOBAL_MODULE | 360 | 0.0% |
| LOAD_CONST | 240 | 0.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 441,263,580 | 100.0% |
| COMPARE_OP | 107,980 | 0.0% |
| POP_JUMP_IF_TRUE | 300 | 0.0% |
| COMPARE_OP_INT | 180 | 0.0% |
| COMPARE_OP_STR | 100 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,320 | 53.5% |
| LOAD_CONST | 1,020 | 23.5% |
| LOAD_FAST_LOAD_FAST | 1,000 | 23.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,280 | 75.6% |
| EXTENDED_ARG | 900 | 20.7% |
| RETURN_VALUE | 160 | 3.7% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 442,245,120 | 50.0% |
| COPY | 442,245,040 | 50.0% |
| LOAD_CONST | 420 | 0.0% |
| UNARY_NOT | 260 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 442,245,040 | 50.0% |
| COPY | 442,245,040 | 50.0% |
| STORE_FAST_STORE_FAST | 420 | 0.0% |
| TO_BOOL_STR | 340 | 0.0% |
| TO_BOOL_BOOL | 260 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 145,350,640 | 100.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |
| CALL_PY_EXACT_ARGS | 60 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 145,350,620 | 100.0% |
| RESUME | 100 | 0.0% |
| RETURN_GENERATOR | 80 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 61,440 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 61,640 | 90.1% |
| JUMP_BACKWARD | 1,640 | 2.4% |
| GET_ITER | 980 | 1.4% |
| CONTAINS_OP | 900 | 1.3% |
| JUMP_FORWARD | 880 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 63,240 | 92.5% |
| FOR_ITER_LIST | 1,460 | 2.1% |
| POP_JUMP_IF_FALSE | 1,380 | 2.0% |
| FOR_ITER | 1,160 | 1.7% |
| JUMP_FORWARD | 1,140 | 1.7% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 453,912,040 | 53.1% |
| GET_ITER | 399,089,780 | 46.7% |
| SWAP | 1,033,900 | 0.1% |
| FOR_ITER | 209,540 | 0.0% |
| EXTENDED_ARG | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 447,756,140 | 52.4% |
| JUMP_BACKWARD | 396,902,400 | 46.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,673,440 | 0.8% |
| LOAD_FAST | 2,187,140 | 0.3% |
| SWAP | 516,880 | 0.1% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,240 | 98.7% |
| LOAD_GLOBAL | 40 | 0.6% |
| LOAD_FAST | 20 | 0.3% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,560 | 88.0% |
| POP_JUMP_IF_TRUE | 760 | 12.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR | 442,247,140 | 29.1% |
| CALL_LIST_APPEND | 396,902,840 | 26.1% |
| FOR_ITER | 396,902,400 | 26.1% |
| POP_JUMP_IF_FALSE | 266,554,900 | 17.6% |
| LIST_APPEND | 6,340,320 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 795,669,800 | 52.4% |
| FOR_ITER | 453,912,040 | 29.9% |
| LOAD_FAST_LOAD_FAST | 266,554,880 | 17.6% |
| LOAD_CONST | 1,670,160 | 0.1% |
| LOAD_GLOBAL_MODULE | 61,340 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,669,920 | 76.3% |
| POP_JUMP_IF_NOT_NONE | 516,960 | 23.6% |
| EXTENDED_ARG | 1,140 | 0.1% |
| POP_TOP | 320 | 0.0% |
| POP_JUMP_IF_FALSE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,187,300 | 99.9% |
| EXTENDED_ARG | 880 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 320 | 0.0% |
| LOAD_GLOBAL_MODULE | 100 | 0.0% |
| NOP | 20 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 4,993,860 | 78.8% |
| BINARY_SUBSCR_DICT | 827,180 | 13.0% |
| STORE_FAST | 516,800 | 8.2% |
| CALL_BUILTIN_O | 2,460 | 0.0% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,340,320 | 100.0% |


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
| LOAD_FAST | 65,180 | 97.2% |
| LOAD_ATTR | 580 | 0.9% |
| LOAD_GLOBAL_MODULE | 360 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 340 | 0.5% |
| LOAD_GLOBAL | 240 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 61,640 | 91.9% |
| STORE_FAST | 1,660 | 2.5% |
| LOAD_FAST | 1,100 | 1.6% |
| LOAD_ATTR | 580 | 0.9% |
| LOAD_ATTR_METHOD_NO_DICT | 440 | 0.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,254,430,780 | 27.4% |
| CALL_LEN | 1,235,068,480 | 27.0% |
| LOAD_CONST | 798,180,600 | 17.4% |
| LOAD_FAST_LOAD_FAST | 444,604,080 | 9.7% |
| BINARY_SUBSCR | 442,245,040 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,328,114,160 | 29.0% |
| BINARY_OP_SUBTRACT_INT | 1,235,067,960 | 27.0% |
| BINARY_SLICE | 799,850,000 | 17.5% |
| LOAD_CONST | 798,180,600 | 17.4% |
| STORE_FAST | 401,278,820 | 8.8% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 442,245,440 | 75.3% |
| RESUME_CHECK | 145,227,480 | 24.7% |
| LOAD_GLOBAL_BUILTIN | 123,140 | 0.0% |
| NOP | 80 | 0.0% |
| BUILD_LIST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 587,595,680 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 360 | 0.0% |
| PUSH_NULL | 160 | 0.0% |
| LIST_EXTEND | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,639,305,040 | 25.5% |
| POP_JUMP_IF_FALSE | 1,235,086,960 | 19.2% |
| STORE_FAST | 847,110,660 | 13.2% |
| CALL_LIST_APPEND | 837,477,720 | 13.0% |
| LOAD_DEREF | 587,595,680 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,254,430,780 | 19.5% |
| LOAD_ATTR_METHOD_NO_DICT | 1,242,006,380 | 19.3% |
| CALL_LEN | 1,235,193,320 | 19.2% |
| LOAD_GLOBAL_BUILTIN | 1,235,071,160 | 19.2% |
| COPY | 442,245,120 | 6.9% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,551,040 | 100.0% |
| LOAD_FAST_AND_CLEAR | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,551,040 | 100.0% |
| LOAD_FAST_AND_CLEAR | 160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 60 | 75.0% |
| LOAD_GLOBAL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 40 | 50.0% |
| CALL_PY_EXACT_ARGS | 40 | 50.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 835,808,380 | 48.4% |
| BINARY_SUBSCR_LIST_INT | 442,933,240 | 25.7% |
| JUMP_BACKWARD | 266,554,880 | 15.4% |
| POP_JUMP_IF_FALSE | 174,709,020 | 10.1% |
| POP_JUMP_IF_NONE | 2,218,560 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 1,278,741,200 | 74.1% |
| LOAD_CONST | 444,604,080 | 25.8% |
| COMPARE_OP_INT | 2,218,520 | 0.1% |
| MAP_ADD | 81,920 | 0.0% |
| LOAD_FAST | 62,760 | 0.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 740 | 33.3% |
| LOAD_FAST | 300 | 13.5% |
| POP_JUMP_IF_FALSE | 220 | 9.9% |
| RESUME | 140 | 6.3% |
| RESUME_CHECK | 140 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 620 | 27.9% |
| LOAD_GLOBAL_MODULE | 520 | 23.4% |
| LOAD_FAST | 460 | 20.7% |
| LOAD_ATTR | 240 | 10.8% |
| CALL | 80 | 3.6% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 20 | 25.0% |
| CALL | 20 | 25.0% |
| LOAD_SUPER_ATTR_ATTR | 20 | 25.0% |
| LOAD_SUPER_ATTR_METHOD | 20 | 25.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_KW | 80 | 50.0% |
| CALL_PY_EXACT_ARGS | 60 | 37.5% |
| CALL | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 120 | 75.0% |
| RESUME | 40 | 25.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 81,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 81,920 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,235,130,620 | 73.7% |
| COMPARE_OP | 441,263,580 | 26.3% |
| TO_BOOL | 62,320 | 0.0% |
| IS_OP | 5,560 | 0.0% |
| TO_BOOL_BOOL | 4,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,235,086,960 | 73.7% |
| JUMP_BACKWARD | 266,554,900 | 15.9% |
| LOAD_FAST_LOAD_FAST | 174,709,020 | 10.4% |
| RETURN_CONST | 61,940 | 0.0% |
| EXTENDED_ARG | 61,640 | 0.0% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,950,280 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,218,560 | 56.2% |
| LOAD_FAST | 1,731,740 | 43.8% |
| LOAD_CONST | 420 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,450,020 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,230,400 | 69.2% |
| JUMP_BACKWARD | 2,702,160 | 25.9% |
| JUMP_FORWARD | 516,960 | 4.9% |
| BUILD_LIST | 280 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 2,218,540 | 99.6% |
| TO_BOOL_STR | 3,260 | 0.1% |
| COMPARE_OP_STR | 2,660 | 0.1% |
| TO_BOOL_BOOL | 860 | 0.0% |
| IS_OP | 760 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,551,540 | 69.6% |
| LOAD_FAST | 672,900 | 30.2% |
| LOAD_GLOBAL_MODULE | 2,480 | 0.1% |
| CALL_LEN | 240 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 200 | 0.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 145,227,420 | 99.9% |
| POP_TOP | 62,360 | 0.0% |
| POP_JUMP_IF_FALSE | 61,940 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 2,000 | 0.0% |
| CALL_LIST_APPEND | 560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 145,351,640 | 100.0% |
| POP_TOP | 2,640 | 0.0% |
| TO_BOOL_BOOL | 740 | 0.0% |
| EXIT_INIT_CHECK | 200 | 0.0% |
| STORE_FAST | 180 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 61,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 61,440 | 99.9% |
| LOAD_FAST | 80 | 0.1% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 53.8% |
| LOAD_FAST_LOAD_FAST | 240 | 46.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 180 | 34.6% |
| LOAD_FAST | 120 | 23.1% |
| LOAD_FAST_LOAD_FAST | 80 | 15.4% |
| STORE_ATTR_INSTANCE_VALUE | 80 | 15.4% |
| RETURN_CONST | 40 | 7.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 61,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,440 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 794,840,340 | 31.8% |
| FOR_ITER | 447,756,140 | 17.9% |
| BINARY_OP_ADD_INT | 441,264,460 | 17.7% |
| LOAD_CONST | 401,278,820 | 16.1% |
| BUILD_LIST | 396,965,180 | 15.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 847,110,660 | 33.9% |
| LOAD_DEREF | 442,245,440 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 404,208,480 | 16.2% |
| LOAD_CONST | 399,093,580 | 16.0% |
| BUILD_LIST | 396,902,760 | 15.9% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,346,420 | 100.0% |
| CALL_LEN | 560 | 0.0% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 827,200 | 61.4% |
| LOAD_ATTR_METHOD_NO_DICT | 516,760 | 38.4% |
| TO_BOOL_STR | 2,440 | 0.2% |
| PUSH_NULL | 560 | 0.0% |
| TO_BOOL | 40 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 6,675,480 | 100.0% |
| COPY | 420 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 160 | 0.0% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,592,600 | 98.7% |
| LOAD_FAST_LOAD_FAST | 82,880 | 1.2% |
| LOAD_GLOBAL_BUILTIN | 240 | 0.0% |
| NOP | 220 | 0.0% |
| STORE_FAST | 180 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 442,245,040 | 49.8% |
| BINARY_OP_ADD_INT | 442,245,020 | 49.8% |
| LOAD_FAST_AND_CLEAR | 1,551,040 | 0.2% |
| BUILD_LIST | 1,550,960 | 0.2% |
| FOR_ITER | 516,880 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR | 442,245,040 | 49.8% |
| SWAP | 442,245,040 | 49.8% |
| BUILD_LIST | 1,550,960 | 0.2% |
| FOR_ITER | 1,033,900 | 0.1% |
| FOR_ITER_LIST | 517,140 | 0.1% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 100 | 55.6% |
| FOR_ITER | 80 | 44.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 60 | 33.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 33.3% |
| UNPACK_SEQUENCE_TUPLE | 40 | 22.2% |
| LOAD_FAST | 20 | 11.1% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 380 | 95.0% |
| BINARY_SUBSCR | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 400 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 260 | 39.4% |
| CALL | 200 | 30.3% |
| COPY_FREE_VARS | 100 | 15.2% |
| MAKE_CELL | 40 | 6.1% |
| POP_TOP | 20 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 260 | 39.4% |
| LOAD_GLOBAL | 140 | 21.2% |
| NOP | 100 | 15.2% |
| LOAD_CONST | 40 | 6.1% |
| LOAD_DEREF | 40 | 6.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,328,114,160 | 100.0% |
| BINARY_OP_MULTIPLY_INT | 220 | 0.0% |
| BINARY_OP | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 442,933,200 | 33.4% |
| SWAP | 442,245,020 | 33.3% |
| STORE_FAST | 441,264,460 | 33.2% |
| LOAD_CONST | 1,670,140 | 0.1% |
| LOAD_FAST | 1,580 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 36.4% |
| LOAD_FAST_LOAD_FAST | 120 | 27.3% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 27.3% |
| BINARY_OP | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 160 | 36.4% |
| RETURN_VALUE | 140 | 31.8% |
| LOAD_FAST | 140 | 31.8% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 220 | 100.0% |


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

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,235,067,960 | 100.0% |
| LOAD_FAST | 880 | 0.0% |
| CALL_LEN | 260 | 0.0% |
| BINARY_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,235,067,800 | 100.0% |
| LOAD_FAST_LOAD_FAST | 560 | 0.0% |
| RETURN_VALUE | 260 | 0.0% |
| LOAD_FAST | 260 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 827,660 | 100.0% |
| BUILD_TUPLE | 160 | 0.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 827,180 | 99.9% |
| YIELD_VALUE | 380 | 0.0% |
| RETURN_VALUE | 160 | 0.0% |
| LOAD_CONST | 160 | 0.0% |
| CALL_BUILTIN_O | 120 | 0.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 940 | 62.7% |
| LOAD_FAST | 540 | 36.0% |
| BINARY_SUBSCR | 20 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,500 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,278,741,200 | 74.3% |
| BINARY_OP_ADD_INT | 442,933,200 | 25.7% |
| LOAD_FAST | 2,620 | 0.0% |
| BINARY_SUBSCR | 160 | 0.0% |
| LOAD_CONST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 835,808,000 | 48.5% |
| LOAD_FAST_LOAD_FAST | 442,933,240 | 25.7% |
| BUILD_TUPLE | 441,263,100 | 25.6% |
| BINARY_OP | 1,670,140 | 0.1% |
| RETURN_VALUE | 2,220 | 0.0% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,460 | 61.9% |
| LOAD_CONST | 900 | 38.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,320 | 55.9% |
| LOAD_CONST | 900 | 38.1% |
| BINARY_OP_INPLACE_ADD_UNICODE | 120 | 5.1% |
| PUSH_EXC_INFO | 20 | 0.8% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,307,100 | 100.0% |
| BINARY_SUBSCR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,652,540 | 50.0% |
| BINARY_OP | 6,652,280 | 50.0% |
| LOAD_GLOBAL_MODULE | 860 | 0.0% |
| CALL_BUILTIN_O | 640 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 220 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 160 | 80.0% |
| LOAD_FAST | 20 | 10.0% |
| LOAD_GLOBAL_MODULE | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 200 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 960 | 38.1% |
| LOAD_CONST | 780 | 31.0% |
| BUILD_TUPLE | 440 | 17.5% |
| RETURN_VALUE | 160 | 6.3% |
| LOAD_FAST | 120 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,520 | 100.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,187,140 | 100.0% |
| CALL_LEN | 260 | 0.0% |
| LOAD_FAST | 120 | 0.0% |
| BINARY_OP_ADD_INT | 80 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,187,240 | 100.0% |
| LOAD_CONST | 260 | 0.0% |
| STORE_FAST | 140 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 66.7% |
| CALL_BUILTIN_CLASS | 40 | 33.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 840 | 43.8% |
| LOAD_FAST | 480 | 25.0% |
| LOAD_FAST_LOAD_FAST | 480 | 25.0% |
| CALL | 60 | 3.1% |
| LOAD_CONST | 40 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,000 | 52.1% |
| BUILD_TUPLE | 420 | 21.9% |
| LOAD_GLOBAL_BUILTIN | 420 | 21.9% |
| BEFORE_WITH | 60 | 3.1% |
| RETURN_VALUE | 20 | 1.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_STR_1 | 2,440 | 34.1% |
| LOAD_FAST | 1,720 | 24.0% |
| LOAD_CONST | 820 | 11.5% |
| LOAD_GLOBAL_MODULE | 700 | 9.8% |
| BINARY_SUBSCR_TUPLE_INT | 640 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,140 | 57.8% |
| LIST_APPEND | 2,460 | 34.4% |
| BUILD_TUPLE | 560 | 7.8% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,300 | 81.3% |
| LOAD_GLOBAL_MODULE | 620 | 15.3% |
| CALL | 60 | 1.5% |
| BUILD_TUPLE | 40 | 1.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,940 | 97.0% |
| TO_BOOL | 60 | 1.5% |
| RETURN_VALUE | 40 | 1.0% |
| LOAD_FAST | 20 | 0.5% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,235,193,320 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,140 | 0.0% |
| POP_JUMP_IF_TRUE | 240 | 0.0% |
| CALL | 160 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,235,068,480 | 100.0% |
| LOAD_FAST | 62,280 | 0.0% |
| STORE_FAST | 61,420 | 0.0% |
| RETURN_VALUE | 1,140 | 0.0% |
| STORE_FAST_LOAD_FAST | 560 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 835,808,000 | 67.7% |
| LOAD_FAST | 398,572,840 | 32.3% |
| BUILD_TUPLE | 300 | 0.0% |
| CALL | 100 | 0.0% |
| LOAD_GLOBAL_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 837,477,720 | 67.8% |
| JUMP_BACKWARD | 396,902,840 | 32.2% |
| RETURN_CONST | 560 | 0.0% |
| NOP | 120 | 0.0% |
| JUMP_FORWARD | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 6,590,840 | 100.0% |
| LOAD_FAST | 140 | 0.0% |
| CALL | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |
| LOAD_CONST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,591,100 | 100.0% |
| POP_TOP | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,033,680 | 100.0% |
| LOAD_FAST | 280 | 0.0% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 517,080 | 50.0% |
| GET_ITER | 516,920 | 50.0% |
| RETURN_VALUE | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 60 | 75.0% |
| CALL | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 80 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 517,040 | 100.0% |
| LOAD_ATTR_SLOT | 120 | 0.0% |
| CALL | 80 | 0.0% |
| RETURN_GENERATOR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 517,080 | 100.0% |
| BINARY_OP_ADD_UNICODE | 120 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |
| BINARY_OP | 20 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 517,900 | 99.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,020 | 0.4% |
| LOAD_FAST_LOAD_FAST | 580 | 0.1% |
| UNARY_NOT | 240 | 0.0% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 521,240 | 100.0% |
| COPY_FREE_VARS | 60 | 0.0% |
| MAKE_CELL | 60 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 60 | 42.9% |
| CALL | 40 | 28.6% |
| LOAD_FAST | 40 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 140 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,480 | 98.4% |
| CALL | 40 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 2,440 | 96.8% |
| RETURN_VALUE | 60 | 2.4% |
| CALL | 20 | 0.8% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 95.2% |
| CALL | 20 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 220 | 52.4% |
| LOAD_FAST_LOAD_FAST | 180 | 42.9% |
| LOAD_FAST | 20 | 4.8% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 1,235,067,800 | 99.8% |
| LOAD_FAST_LOAD_FAST | 2,218,520 | 0.2% |
| LOAD_FAST | 61,520 | 0.0% |
| LOAD_CONST | 1,040 | 0.0% |
| COMPARE_OP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,235,130,620 | 99.8% |
| POP_JUMP_IF_TRUE | 2,218,540 | 0.2% |
| EXTENDED_ARG | 60 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,820 | 83.9% |
| LOAD_ATTR_INSTANCE_VALUE | 780 | 11.2% |
| LOAD_FAST | 240 | 3.5% |
| COMPARE_OP | 100 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,020 | 57.9% |
| POP_JUMP_IF_TRUE | 2,660 | 38.3% |
| EXTENDED_ARG | 260 | 3.7% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 795,669,800 | 99.9% |
| SWAP | 517,140 | 0.1% |
| GET_ITER | 123,340 | 0.0% |
| EXTENDED_ARG | 1,460 | 0.0% |
| FOR_ITER | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 794,840,340 | 99.8% |
| STORE_FAST_LOAD_FAST | 1,346,420 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 61,820 | 0.0% |
| LOAD_FAST | 61,740 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,240 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 23,140 | 97.9% |
| GET_ITER | 460 | 1.9% |
| FOR_ITER | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 23,140 | 97.9% |
| LOAD_FAST | 260 | 1.1% |
| JUMP_FORWARD | 80 | 0.3% |
| LOAD_GLOBAL | 80 | 0.3% |
| LOAD_GLOBAL_MODULE | 80 | 0.3% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 460 | 59.0% |
| GET_ITER | 300 | 38.5% |
| FOR_ITER | 20 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 460 | 59.0% |
| LOAD_FAST_LOAD_FAST | 320 | 41.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 85.7% |
| LOAD_ATTR | 80 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 480 | 85.7% |
| LOAD_ATTR | 80 | 14.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 528,660 | 99.7% |
| LOAD_FAST_LOAD_FAST | 1,180 | 0.2% |
| LOAD_DEREF | 360 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 100 | 0.0% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 522,080 | 98.4% |
| STORE_FAST | 3,300 | 0.6% |
| CALL_LEN | 1,140 | 0.2% |
| COMPARE_OP_STR | 780 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 680 | 0.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,242,006,380 | 100.0% |
| STORE_FAST_LOAD_FAST | 516,760 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 680 | 0.0% |
| LOAD_ATTR | 440 | 0.0% |
| LOAD_GLOBAL_MODULE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 835,808,380 | 67.3% |
| LOAD_FAST | 405,682,020 | 32.6% |
| LOAD_CONST | 1,034,080 | 0.1% |
| LOAD_GLOBAL_MODULE | 100 | 0.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 60 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,040 | 89.5% |
| BINARY_SUBSCR_TUPLE_INT | 160 | 7.0% |
| LOAD_ATTR | 80 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,020 | 88.6% |
| LOAD_FAST | 180 | 7.9% |
| LOAD_CONST | 60 | 2.6% |
| LOAD_GLOBAL_MODULE | 20 | 0.9% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 64,720 | 98.7% |
| LOAD_ATTR_CLASS | 480 | 0.7% |
| LOAD_ATTR | 300 | 0.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 64,840 | 98.9% |
| STORE_FAST | 280 | 0.4% |
| LOAD_FAST | 220 | 0.3% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.2% |
| LOAD_CONST | 60 | 0.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 80.0% |
| LOAD_ATTR | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 60.0% |
| LOAD_ATTR_MODULE | 40 | 20.0% |
| LOAD_ATTR | 20 | 10.0% |
| LOAD_GLOBAL | 20 | 10.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 50.0% |
| LOAD_FAST_LOAD_FAST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 20 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 50.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 60.0% |
| LOAD_ATTR | 160 | 26.7% |
| CALL | 40 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 600 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 820 | 82.0% |
| LOAD_ATTR | 160 | 16.0% |
| LOAD_FAST_LOAD_FAST | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 280 | 28.0% |
| PUSH_EXC_INFO | 200 | 20.0% |
| SWAP | 200 | 20.0% |
| STORE_FAST | 140 | 14.0% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 12.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,235,071,160 | 75.2% |
| STORE_FAST | 404,208,480 | 24.6% |
| LOAD_GLOBAL_BUILTIN | 2,187,420 | 0.1% |
| RESUME_CHECK | 66,120 | 0.0% |
| FOR_ITER_LIST | 61,820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,639,305,040 | 99.9% |
| LOAD_GLOBAL_BUILTIN | 2,187,420 | 0.1% |
| LOAD_DEREF | 123,140 | 0.0% |
| CALL_ISINSTANCE | 3,300 | 0.0% |
| STORE_FAST | 960 | 0.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 519,020 | 86.4% |
| JUMP_BACKWARD | 61,340 | 10.2% |
| LOAD_FAST | 10,760 | 1.8% |
| POP_JUMP_IF_TRUE | 2,480 | 0.4% |
| PUSH_NULL | 1,600 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 518,940 | 86.4% |
| LOAD_ATTR_MODULE | 64,720 | 10.8% |
| IS_OP | 6,240 | 1.0% |
| CONTAINS_OP | 2,320 | 0.4% |
| STORE_FAST | 2,060 | 0.3% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 93.3% |
| LOAD_SUPER_ATTR | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 300 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,400 | 100.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 61,420 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 145,350,620 | 49.9% |
| CACHE | 145,231,800 | 49.9% |
| CALL_PY_EXACT_ARGS | 521,240 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 2,520 | 0.0% |
| BINARY_SUBSCR_GETITEM | 1,500 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 145,227,480 | 49.9% |
| RETURN_CONST | 145,227,420 | 49.9% |
| LOAD_FAST | 584,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 66,120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,520 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,600 | 50.6% |
| LOAD_FAST_LOAD_FAST | 2,440 | 47.5% |
| STORE_ATTR | 80 | 1.6% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,000 | 38.9% |
| LOAD_FAST_LOAD_FAST | 1,420 | 27.6% |
| LOAD_FAST | 1,060 | 20.6% |
| LOAD_CONST | 520 | 10.1% |
| LOAD_GLOBAL_MODULE | 60 | 1.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 43.1% |
| LOAD_FAST_LOAD_FAST | 400 | 39.2% |
| STORE_ATTR | 180 | 17.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 52.9% |
| RETURN_CONST | 300 | 29.4% |
| LOAD_FAST_LOAD_FAST | 180 | 17.6% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,440 | 75.0% |
| CALL | 20,440 | 25.0% |
| STORE_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 61,420 | 75.0% |
| JUMP_BACKWARD | 20,460 | 25.0% |
| LOAD_FAST | 20 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 560 | 70.0% |
| LOAD_FAST | 240 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 480 | 60.0% |
| EXTENDED_ARG | 300 | 37.5% |
| RETURN_CONST | 20 | 2.5% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 3,940 | 67.7% |
| RETURN_CONST | 740 | 12.7% |
| CALL | 320 | 5.5% |
| LOAD_FAST | 280 | 4.8% |
| COPY | 260 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,820 | 82.8% |
| POP_JUMP_IF_TRUE | 860 | 14.8% |
| EXTENDED_ARG | 140 | 2.4% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,340 | 51.1% |
| LOAD_FAST | 1,280 | 48.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,680 | 64.1% |
| POP_JUMP_IF_TRUE | 680 | 26.0% |
| UNARY_NOT | 260 | 9.9% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500 | 92.6% |
| TO_BOOL | 20 | 3.7% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNARY_NOT | 240 | 44.4% |
| POP_JUMP_IF_FALSE | 200 | 37.0% |
| POP_JUMP_IF_TRUE | 100 | 18.5% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 400 | 90.9% |
| TO_BOOL | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 440 | 100.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,440 | 68.5% |
| LOAD_FAST | 640 | 18.0% |
| COPY | 340 | 9.6% |
| TO_BOOL | 140 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 3,260 | 91.6% |
| POP_JUMP_IF_FALSE | 300 | 8.4% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 260 | 86.7% |
| UNPACK_SEQUENCE | 40 | 13.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 160 | 53.3% |
| LOAD_FAST | 140 | 46.7% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 6,673,440 | 100.0% |
| RETURN_VALUE | 1,380 | 0.0% |
| FOR_ITER_LIST | 1,240 | 0.0% |
| CALL_BUILTIN_FAST | 80 | 0.0% |
| LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 6,675,480 | 100.0% |
| STORE_FAST | 800 | 0.0% |


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
|     deferred | 11,665,100 | 0.5% |
|          hit | 2,563,184,700 | 99.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 5.8% |
| Failure | 3,900 | 94.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 3,840 | 98.5% |
| true divide different types | 40 | 1.0% |
| and int | 20 | 0.5% |


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
|     deferred | 587,473,600 | 25.3% |
|          hit | 1,735,815,960 | 74.7% |
|         miss | 460 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 0.3% |
| Failure | 143,840 | 99.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 143,840 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 404,229,840 | 14.0% |
|          hit | 2,480,449,320 | 86.0% |
|         miss | 40 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,120 | 1.1% |
| Failure | 100,280 | 98.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class no vectorcall | 99,620 | 99.3% |
| class mutable | 220 | 0.2% |
| operator wrapper | 200 | 0.2% |
| code complex parameters | 60 | 0.1% |
| cfunc varargs keywords | 60 | 0.1% |
| cfunc noargs | 60 | 0.1% |
| wrong number arguments | 20 | 0.0% |
| cfunc varargs | 20 | 0.0% |
| meth descr varargs | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 441,263,960 | 26.3% |
|          hit | 1,237,356,100 | 73.7% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 0.3% |
| Failure | 107,980 | 99.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 107,940 | 100.0% |
| other | 40 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 854,036,680 | 51.7% |
|          hit | 796,336,380 | 48.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 0.1% |
| Failure | 209,540 | 99.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| zip | 205,120 | 97.9% |
| enumerate | 2,340 | 1.1% |
| bytes | 1,840 | 0.9% |
| dict items | 220 | 0.1% |
| seq iter | 20 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 65,520 | 0.0% |
|          hit | 1,243,125,040 | 100.0% |
|         miss | 200 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,320 | 75.0% |
| Failure | 440 | 25.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 240 | 54.5% |
| class method obj | 80 | 18.2% |
| metaclass attribute | 60 | 13.6% |
| non overriding descriptor | 20 | 4.5% |
| not managed dict | 20 | 4.5% |
| class attr simple | 20 | 4.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,080 | 0.0% |
|          hit | 1,642,222,180 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.1% |
|          hit | 61,720 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 260 | 3.9% |
|          hit | 6,160 | 92.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 442,247,480 | 100.0% |
|          hit | 82,720 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 0.0% |
| Failure | 108,200 | 100.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 108,180 | 100.0% |
| bytearray int | 20 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 63,020 | 82.4% |
|          hit | 12,840 | 16.8% |
|         miss | 140 | 0.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 43.3% |
| Failure | 340 | 56.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 260 | 76.5% |
| mapping | 60 | 17.6% |
| tuple | 20 | 5.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 80 | 0.0% |
|          hit | 6,676,580 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 100 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 21,099,237,160 | 55.0% |
| Not specialized | 5,236,352,780 | 13.7% |
| Specialized hits | 11,996,436,500 | 31.3% |
| Specialized misses | 900 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| FOR_ITER | 854,036,680 | 31.2% |
| BINARY_SUBSCR | 587,473,600 | 21.4% |
| STORE_SUBSCR | 442,247,480 | 16.1% |
| COMPARE_OP | 441,263,960 | 16.1% |
| CALL | 404,229,840 | 14.7% |
| BINARY_OP | 11,665,100 | 0.4% |
| LOAD_ATTR | 65,520 | 0.0% |
| TO_BOOL | 63,020 | 0.0% |
| LOAD_GLOBAL | 1,080 | 0.0% |
| STORE_ATTR | 260 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 440 | 48.9% |
| LOAD_ATTR_SLOT | 200 | 22.2% |
| TO_BOOL_NONE | 80 | 8.9% |
| COMPARE_OP_STR | 60 | 6.7% |
| CALL_BUILTIN_FAST | 40 | 4.4% |
| TO_BOOL_LIST | 40 | 4.4% |
| BINARY_SUBSCR_STR_INT | 20 | 2.2% |
| TO_BOOL_STR | 20 | 2.2% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 290,582,780 | 99.8% |
| Calls to Python functions inlined | 527,280 | 0.2% |
| Calls via PyEval_EvalFrame (total) | 290,582,780 | 99.8% |
| Calls via PyEval_EvalFrame (vector) | 290,582,300 | 99.8% |
| Calls via PyEval_EvalFrame (generator) | 480 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 290,582,300 | 99.8% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 2,800 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 240 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 145,227,680 | 49.9% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 1,120 | 0.0% |
| Frames pushed | 526,520 | 0.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 3,652,084,980 | 63.0% |
| Frees to freelist | 3,652,244,900 |  |
| Allocations | 2,145,008,100 | 37.0% |
| Allocations to 512 bytes | 2,144,519,600 | 37.0% |
| Allocations to 4 kbytes | 184,820 | 0.0% |
| Allocations over 4 kbytes | 303,680 | 0.0% |
| Frees | 2,544,521,552 |  |
| New values | 440 |  |
| Interpreter increfs | 13,443,133,580 | 64.5% |
| Interpreter decrefs | 15,701,564,300 | 58.0% |
| Increfs | 7,397,859,082 | 35.5% |
| Decrefs | 11,372,569,101 | 42.0% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 70,597 |  |
| Method cache misses | 923 |  |
| Method cache collisions | 956 |  |
| Method cache dunder hits | 1,180,281,527 |  |
| Method cache dunder misses | 253 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 517,140 | 0 | 2,622,613,400 |
| 1 | 47,000 | 0 | 2,584,226,200 |
| 2 | 4,260 | 0 | 824,400,280 |


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
