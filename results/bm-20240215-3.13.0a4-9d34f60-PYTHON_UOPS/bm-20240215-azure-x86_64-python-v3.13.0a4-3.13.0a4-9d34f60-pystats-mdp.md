
# Pystats results

- benchmark: mdp
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 1,108,490,260 | 14.7% | 14.7% |  |
| RESUME_CHECK | 576,474,260 | 7.7% | 22.4% | 0.0% |
| INTERPRETER_EXIT | 435,891,180 | 5.8% | 28.2% |  |
| POP_TOP | 388,578,040 | 5.2% | 33.4% |  |
| ENTER_EXECUTOR | 373,013,640 | 5.0% | 38.4% |  |
| YIELD_VALUE | 324,495,840 | 4.3% | 42.7% |  |
| LOAD_FAST_LOAD_FAST | 308,283,100 | 4.1% | 46.8% |  |
| STORE_FAST | 269,640,960 | 3.6% | 50.4% |  |
| LOAD_DEREF | 239,879,080 | 3.2% | 53.5% |  |
| RETURN_VALUE | 193,172,620 | 2.6% | 56.1% |  |
| LOAD_GLOBAL_MODULE | 168,004,500 | 2.2% | 58.4% |  |
| LOAD_CONST | 167,980,480 | 2.2% | 60.6% |  |
| LOAD_GLOBAL_BUILTIN | 163,514,540 | 2.2% | 62.8% |  |
| CALL_PY_EXACT_ARGS | 160,529,760 | 2.1% | 64.9% | 1.1% |
| POP_JUMP_IF_FALSE | 147,311,040 | 2.0% | 66.9% |  |
| COPY_FREE_VARS | 141,718,960 | 1.9% | 68.7% |  |
| BINARY_SUBSCR | 131,177,400 | 1.7% | 70.5% |  |
| LOAD_ATTR_SLOT | 130,016,240 | 1.7% | 72.2% |  |
| FOR_ITER_LIST | 126,232,500 | 1.7% | 73.9% | 0.1% |
| PUSH_NULL | 100,104,320 | 1.3% | 75.2% |  |
| BINARY_OP_MULTIPLY_INT | 97,943,940 | 1.3% | 76.5% |  |
| BINARY_OP | 86,126,860 | 1.1% | 77.7% |  |
| STORE_ATTR_SLOT | 80,104,680 | 1.1% | 78.7% |  |
| COMPARE_OP_INT | 71,896,020 | 1.0% | 79.7% |  |
| BUILD_TUPLE | 71,399,660 | 0.9% | 80.7% |  |
| STORE_SUBSCR | 67,616,680 | 0.9% | 81.6% |  |
| GET_ITER | 65,504,800 | 0.9% | 82.4% |  |
| STORE_FAST_STORE_FAST | 64,515,460 | 0.9% | 83.3% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 63,604,220 | 0.8% | 84.1% |  |
| LOAD_ATTR_INSTANCE_VALUE | 63,357,060 | 0.8% | 85.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,311,220 | 0.8% | 85.8% |  |
| RETURN_CONST | 63,239,120 | 0.8% | 86.7% |  |
| MAKE_FUNCTION | 63,032,400 | 0.8% | 87.5% |  |
| BINARY_SUBSCR_DICT | 63,032,120 | 0.8% | 88.3% |  |
| RETURN_GENERATOR | 62,832,560 | 0.8% | 89.2% |  |
| NOP | 62,739,520 | 0.8% | 90.0% |  |
| SET_FUNCTION_ATTRIBUTE | 62,353,760 | 0.8% | 90.8% |  |
| CALL_BUILTIN_FAST | 58,829,240 | 0.8% | 91.6% |  |
| LOAD_ATTR_MODULE | 58,243,860 | 0.8% | 92.4% |  |
| LOAD_ATTR | 50,823,320 | 0.7% | 93.1% |  |
| CALL | 47,619,600 | 0.6% | 93.7% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 43,596,920 | 0.6% | 94.3% |  |
| BINARY_OP_MULTIPLY_FLOAT | 41,716,800 | 0.6% | 94.8% |  |
| LOAD_SUPER_ATTR_METHOD | 40,052,360 | 0.5% | 95.4% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 35,344,000 | 0.5% | 95.8% |  |
| TO_BOOL_BOOL | 34,553,040 | 0.5% | 96.3% |  |
| CALL_ISINSTANCE | 33,089,520 | 0.4% | 96.7% |  |
| POP_JUMP_IF_TRUE | 31,855,900 | 0.4% | 97.2% |  |
| BINARY_OP_ADD_INT | 31,352,900 | 0.4% | 97.6% |  |
| COMPARE_OP_FLOAT | 31,185,840 | 0.4% | 98.0% |  |
| JUMP_FORWARD | 15,114,160 | 0.2% | 98.2% |  |
| BINARY_SUBSCR_TUPLE_INT | 14,898,020 | 0.2% | 98.4% |  |
| SWAP | 14,091,320 | 0.2% | 98.6% |  |
| COPY | 10,835,880 | 0.1% | 98.7% |  |
| IS_OP | 10,113,040 | 0.1% | 98.9% |  |
| CALL_TYPE_1 | 10,112,980 | 0.1% | 99.0% |  |
| EXTENDED_ARG | 9,457,360 | 0.1% | 99.1% |  |
| POP_JUMP_IF_NOT_NONE | 9,448,480 | 0.1% | 99.2% |  |
| CALL_BUILTIN_CLASS | 9,419,180 | 0.1% | 99.4% |  |
| LOAD_ATTR_METHOD_NO_DICT | 4,857,220 | 0.1% | 99.4% | 1.0% |
| CALL_LEN | 4,647,240 | 0.1% | 99.5% |  |
| CALL_KW | 4,647,120 | 0.1% | 99.6% |  |
| TO_BOOL | 4,356,140 | 0.1% | 99.6% |  |
| LOAD_ATTR_PROPERTY | 3,246,800 | 0.0% | 99.7% | 0.8% |
| TO_BOOL_LIST | 2,472,100 | 0.0% | 99.7% |  |
| FOR_ITER_TUPLE | 2,461,300 | 0.0% | 99.7% | 6.9% |
| STORE_FAST_LOAD_FAST | 2,286,340 | 0.0% | 99.8% |  |
| UNARY_NEGATIVE | 1,900,540 | 0.0% | 99.8% |  |
| LOAD_FAST_AND_CLEAR | 1,655,280 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,615,560 | 0.0% | 99.8% | 55.4% |
| FOR_ITER | 1,603,780 | 0.0% | 99.9% |  |
| BUILD_LIST | 1,171,520 | 0.0% | 99.9% |  |
| FOR_ITER_RANGE | 1,171,320 | 0.0% | 99.9% |  |
| CONTAINS_OP | 833,540 | 0.0% | 99.9% |  |
| CALL_LIST_APPEND | 771,640 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 734,960 | 0.0% | 99.9% |  |
| BUILD_MAP | 720,800 | 0.0% | 99.9% |  |
| COMPARE_OP_STR | 665,460 | 0.0% | 99.9% |  |
| LIST_APPEND | 586,160 | 0.0% | 99.9% |  |
| MAP_ADD | 535,560 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 491,860 | 0.0% | 100.0% |  |
| JUMP_BACKWARD | 453,960 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 385,680 | 0.0% | 100.0% |  |
| POP_EXCEPT | 385,680 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 385,680 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 385,660 | 0.0% | 100.0% |  |
| COMPARE_OP | 294,960 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 292,960 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 292,800 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 292,700 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 292,700 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 105,800 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 9,040 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 4,340 | 0.0% | 100.0% |  |
| RESUME | 1,000 | 0.0% | 100.0% | 92.0% |
| UNPACK_SEQUENCE | 680 | 0.0% | 100.0% |  |
| STORE_ATTR | 480 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 440 | 0.0% | 100.0% |  |
| STORE_ATTR_INSTANCE_VALUE | 360 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 300 | 0.0% | 100.0% |  |
| MAKE_CELL | 160 | 0.0% | 100.0% |  |
| STORE_DEREF | 160 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 80 | 0.0% | 100.0% |  |
| EXIT_INIT_CHECK | 60 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 60 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 60 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| CACHE RESUME_CHECK | 333,005,880 | 4.4% | 4.4% |
| POP_TOP ENTER_EXECUTOR | 324,864,960 | 4.3% | 8.8% |
| YIELD_VALUE INTERPRETER_EXIT | 324,495,840 | 4.3% | 13.1% |
| RESUME_CHECK POP_TOP | 324,495,720 | 4.3% | 17.4% |
| ENTER_EXECUTOR YIELD_VALUE | 260,347,940 | 3.5% | 20.9% |
| LOAD_DEREF LOAD_FAST | 191,857,320 | 2.6% | 23.4% |
| LOAD_FAST LOAD_ATTR_SLOT | 130,015,840 | 1.7% | 25.1% |
| LOAD_FAST BINARY_SUBSCR | 126,108,600 | 1.7% | 26.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 110,514,500 | 1.5% | 28.3% |
| RESUME_CHECK LOAD_FAST | 106,363,340 | 1.4% | 29.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 97,665,440 | 1.3% | 31.0% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 88,230,880 | 1.2% | 32.2% |
| COPY_FREE_VARS RESUME_CHECK | 79,365,060 | 1.1% | 33.2% |
| LOAD_FAST LOAD_CONST | 75,432,200 | 1.0% | 34.2% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 74,935,420 | 1.0% | 35.2% |
| STORE_FAST LOAD_FAST | 72,476,140 | 1.0% | 36.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 71,896,020 | 1.0% | 37.1% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 71,320,680 | 0.9% | 38.1% |
| RETURN_VALUE RETURN_VALUE | 67,699,120 | 0.9% | 39.0% |
| LOAD_CONST COMPARE_OP_INT | 67,261,860 | 0.9% | 39.9% |
| STORE_FAST LOAD_DEREF | 66,708,760 | 0.9% | 40.8% |
| LOAD_ATTR_SLOT LOAD_FAST | 65,008,120 | 0.9% | 41.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 64,338,560 | 0.9% | 42.5% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 63,311,160 | 0.8% | 43.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 63,310,960 | 0.8% | 44.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 63,125,380 | 0.8% | 45.0% |
| ENTER_EXECUTOR FOR_ITER_LIST | 63,096,780 | 0.8% | 45.9% |
| LOAD_CONST MAKE_FUNCTION | 63,032,400 | 0.8% | 46.7% |
| LOAD_FAST BINARY_SUBSCR_DICT | 63,032,080 | 0.8% | 47.5% |
| LOAD_FAST BUILD_TUPLE | 63,029,100 | 0.8% | 48.4% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 62,971,120 | 0.8% | 49.2% |
| RETURN_CONST INTERPRETER_EXIT | 62,867,220 | 0.8% | 50.1% |
| CACHE POP_TOP | 62,832,560 | 0.8% | 50.9% |
| POP_TOP RESUME_CHECK | 62,832,440 | 0.8% | 51.7% |
| RETURN_VALUE GET_ITER | 62,739,600 | 0.8% | 52.6% |
| NOP LOAD_FAST | 62,739,440 | 0.8% | 53.4% |
| RESUME_CHECK NOP | 62,739,420 | 0.8% | 54.2% |
| GET_ITER CALL_PY_EXACT_ARGS | 62,739,400 | 0.8% | 55.1% |
| LOAD_FAST STORE_SUBSCR | 62,565,320 | 0.8% | 55.9% |
| BUILD_TUPLE LOAD_CONST | 62,539,680 | 0.8% | 56.7% |
| FOR_ITER_LIST RETURN_CONST | 62,390,320 | 0.8% | 57.6% |
| LOAD_FAST FOR_ITER_LIST | 62,390,240 | 0.8% | 58.4% |
| MAKE_FUNCTION SET_FUNCTION_ATTRIBUTE | 62,353,760 | 0.8% | 59.2% |
| COPY_FREE_VARS RETURN_GENERATOR | 62,353,760 | 0.8% | 60.1% |
| SET_FUNCTION_ATTRIBUTE LOAD_FAST | 62,353,760 | 0.8% | 60.9% |
| BINARY_SUBSCR_DICT RETURN_VALUE | 62,353,760 | 0.8% | 61.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS LOAD_DEREF | 62,353,680 | 0.8% | 62.5% |
| CALL_PY_EXACT_ARGS COPY_FREE_VARS | 62,353,680 | 0.8% | 63.4% |
| RETURN_GENERATOR CALL_BUILTIN_FAST_WITH_KEYWORDS | 62,353,600 | 0.8% | 64.2% |
| LOAD_ATTR_SLOT STORE_FAST_STORE_FAST | 61,207,680 | 0.8% | 65.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 60,189,860 | 0.8% | 65.8% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 58,243,560 | 0.8% | 66.6% |
| LOAD_FAST_LOAD_FAST CALL_BUILTIN_FAST | 56,928,840 | 0.8% | 67.3% |
| LOAD_ATTR_MODULE PUSH_NULL | 54,150,740 | 0.7% | 68.1% |
| CALL_BUILTIN_FAST STORE_FAST | 54,150,560 | 0.7% | 68.8% |
| LOAD_FAST RETURN_VALUE | 50,118,160 | 0.7% | 69.5% |
| RETURN_VALUE INTERPRETER_EXIT | 48,528,120 | 0.6% | 70.1% |
| LOAD_FAST_LOAD_FAST BINARY_OP_MULTIPLY_INT | 48,105,760 | 0.6% | 70.7% |
| BINARY_SUBSCR LOAD_FAST | 47,486,060 | 0.6% | 71.4% |
| CALL STORE_FAST | 45,285,640 | 0.6% | 72.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 44,188,880 | 0.6% | 72.6% |
| LOAD_DEREF PUSH_NULL | 43,667,280 | 0.6% | 73.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 42,287,480 | 0.6% | 73.7% |
| STORE_FAST STORE_FAST | 42,251,800 | 0.6% | 74.3% |
| BINARY_OP_MULTIPLY_FLOAT YIELD_VALUE | 41,716,800 | 0.6% | 74.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST | 41,716,800 | 0.6% | 75.4% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 41,716,760 | 0.6% | 75.9% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 41,716,760 | 0.6% | 76.5% |
| LOAD_FAST CALL | 41,224,440 | 0.5% | 77.0% |
| LOAD_FAST BINARY_OP | 41,152,060 | 0.5% | 77.6% |
| CACHE COPY_FREE_VARS | 40,052,400 | 0.5% | 78.1% |
| LOAD_SUPER_ATTR_METHOD LOAD_FAST | 40,052,360 | 0.5% | 78.7% |
| STORE_ATTR_SLOT LOAD_FAST | 40,052,340 | 0.5% | 79.2% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 40,052,320 | 0.5% | 79.7% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_MODULE | 40,052,320 | 0.5% | 80.2% |
| LOAD_FAST_LOAD_FAST BINARY_OP | 39,893,680 | 0.5% | 80.8% |
| BINARY_OP BINARY_OP_MULTIPLY_INT | 36,261,020 | 0.5% | 81.3% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 35,282,320 | 0.5% | 81.7% |
| CALL_BOUND_METHOD_EXACT_ARGS COPY_FREE_VARS | 34,958,180 | 0.5% | 82.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 34,553,040 | 0.5% | 82.7% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 33,089,440 | 0.4% | 83.1% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 32,954,800 | 0.4% | 83.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 32,913,600 | 0.4% | 84.0% |
| STORE_FAST_STORE_FAST LOAD_FAST | 32,683,720 | 0.4% | 84.4% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 32,429,480 | 0.4% | 84.8% |
| BINARY_SUBSCR LOAD_DEREF | 31,291,680 | 0.4% | 85.3% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 31,268,440 | 0.4% | 85.7% |
| COMPARE_OP_FLOAT POP_JUMP_IF_TRUE | 31,176,860 | 0.4% | 86.1% |
| BINARY_SUBSCR COMPARE_OP_FLOAT | 31,176,840 | 0.4% | 86.5% |
| STORE_SUBSCR LOAD_GLOBAL_BUILTIN | 31,176,800 | 0.4% | 86.9% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_MODULE | 31,003,500 | 0.4% | 87.3% |
| BINARY_OP_MULTIPLY_INT LOAD_FAST_LOAD_FAST | 30,896,520 | 0.4% | 87.7% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 30,738,660 | 0.4% | 88.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 30,604,100 | 0.4% | 88.6% |
| POP_JUMP_IF_FALSE LOAD_DEREF | 30,604,000 | 0.4% | 89.0% |
| LOAD_ATTR LOAD_FAST_LOAD_FAST | 30,603,920 | 0.4% | 89.4% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 30,311,160 | 0.4% | 89.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 30,162,120 | 0.4% | 90.2% |
| BINARY_OP_MULTIPLY_INT CALL_BOUND_METHOD_EXACT_ARGS | 30,018,280 | 0.4% | 90.6% |
| BINARY_OP_MULTIPLY_INT BINARY_OP_ADD_INT | 28,837,600 | 0.4% | 91.0% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 333,005,880 | 76.4% |
| POP_TOP | 62,832,560 | 14.4% |
| COPY_FREE_VARS | 40,052,400 | 9.2% |
| RESUME | 340 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 126,108,600 | 96.1% |
| COPY | 5,032,780 | 3.8% |
| BINARY_SUBSCR | 35,380 | 0.0% |
| LOAD_CONST | 640 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,486,060 | 36.2% |
| LOAD_DEREF | 31,291,680 | 23.9% |
| COMPARE_OP_FLOAT | 31,176,840 | 23.8% |
| YIELD_VALUE | 20,637,440 | 15.7% |
| LOAD_FAST_LOAD_FAST | 434,480 | 0.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 385,660 | 100.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 385,680 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 62,739,600 | 95.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,306,040 | 2.0% |
| CALL_BUILTIN_CLASS | 585,420 | 0.9% |
| LOAD_FAST | 301,920 | 0.5% |
| CALL | 292,940 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 62,739,400 | 95.8% |
| LOAD_FAST_AND_CLEAR | 1,120,400 | 1.7% |
| FOR_ITER | 1,064,180 | 1.6% |
| FOR_ITER_LIST | 301,720 | 0.5% |
| FOR_ITER_TUPLE | 278,840 | 0.4% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 324,495,840 | 74.4% |
| RETURN_CONST | 62,867,220 | 14.4% |
| RETURN_VALUE | 48,528,120 | 11.1% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,032,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 62,353,760 | 98.9% |
| LOAD_FAST | 385,840 | 0.6% |
| LOAD_CONST | 292,720 | 0.5% |
| CALL | 80 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 62,739,420 | 100.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,739,440 | 100.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 385,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 385,680 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 324,495,720 | 83.5% |
| CACHE | 62,832,560 | 16.2% |
| CALL_METHOD_DESCRIPTOR_O | 491,860 | 0.1% |
| POP_JUMP_IF_FALSE | 385,680 | 0.1% |
| RETURN_CONST | 371,840 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 324,864,960 | 83.6% |
| RESUME_CHECK | 62,832,440 | 16.2% |
| LOAD_FAST | 386,040 | 0.1% |
| JUMP_FORWARD | 385,840 | 0.1% |
| JUMP_BACKWARD | 108,480 | 0.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 385,660 | 100.0% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 385,640 | 100.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 54,150,740 | 54.1% |
| LOAD_DEREF | 43,667,280 | 43.6% |
| LOAD_FAST | 2,286,080 | 2.3% |
| LOAD_ATTR | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 88,230,880 | 88.1% |
| LOAD_FAST | 11,580,480 | 11.6% |
| LOAD_GLOBAL_MODULE | 292,680 | 0.3% |
| CALL | 240 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 62,353,760 | 99.2% |
| CALL_PY_EXACT_ARGS | 478,760 | 0.8% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 62,353,600 | 99.2% |
| CALL_METHOD_DESCRIPTOR_O | 385,800 | 0.6% |
| CALL_BUILTIN_CLASS | 92,920 | 0.1% |
| CALL | 240 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,699,120 | 35.0% |
| BINARY_SUBSCR_DICT | 62,353,760 | 32.3% |
| LOAD_FAST | 50,118,160 | 25.9% |
| CALL_BUILTIN_FAST | 4,678,680 | 2.4% |
| LOAD_ATTR_SLOT | 3,800,440 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 67,699,120 | 35.0% |
| GET_ITER | 62,739,600 | 32.5% |
| INTERPRETER_EXIT | 48,528,120 | 25.1% |
| STORE_FAST | 10,507,600 | 5.4% |
| CALL_BUILTIN_CLASS | 3,214,960 | 1.7% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,565,320 | 92.5% |
| SWAP | 5,032,780 | 7.4% |
| STORE_SUBSCR | 18,420 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 31,176,800 | 46.1% |
| LOAD_DEREF | 20,964,080 | 31.0% |
| JUMP_FORWARD | 10,318,560 | 15.3% |
| ENTER_EXECUTOR | 5,031,420 | 7.4% |
| LOAD_FAST | 105,860 | 0.2% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,354,600 | 100.0% |
| TO_BOOL | 1,260 | 0.0% |
| LOAD_ATTR | 120 | 0.0% |
| CALL | 80 | 0.0% |
| CALL_ISINSTANCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,354,640 | 100.0% |
| TO_BOOL | 1,260 | 0.0% |
| TO_BOOL_BOOL | 160 | 0.0% |
| TO_BOOL_LIST | 60 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_TUPLE_INT | 1,607,500 | 84.6% |
| LOAD_FAST_LOAD_FAST | 293,020 | 15.4% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,607,520 | 84.6% |
| CALL_PY_EXACT_ARGS | 292,980 | 15.4% |
| CALL | 40 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,152,060 | 47.8% |
| LOAD_FAST_LOAD_FAST | 39,893,680 | 46.3% |
| LOAD_CONST | 1,761,480 | 2.0% |
| CALL_BUILTIN_CLASS | 1,607,500 | 1.9% |
| BINARY_OP_MULTIPLY_INT | 585,480 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 36,261,020 | 42.1% |
| STORE_FAST | 25,485,260 | 29.6% |
| LOAD_FAST_LOAD_FAST | 14,852,080 | 17.2% |
| SWAP | 5,032,780 | 5.8% |
| RETURN_VALUE | 1,607,620 | 1.9% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 585,600 | 50.0% |
| LOAD_FAST | 292,880 | 25.0% |
| LOAD_FAST_LOAD_FAST | 292,720 | 25.0% |
| POP_JUMP_IF_FALSE | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 585,600 | 50.0% |
| CALL | 292,760 | 25.0% |
| LOAD_FAST_LOAD_FAST | 292,720 | 25.0% |
| RETURN_VALUE | 160 | 0.0% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 534,800 | 74.2% |
| CALL | 185,920 | 25.8% |
| RESUME_CHECK | 60 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 534,800 | 74.2% |
| RETURN_VALUE | 185,920 | 25.8% |
| LOAD_FAST | 80 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,029,100 | 88.3% |
| LOAD_FAST_LOAD_FAST | 4,261,920 | 6.0% |
| BINARY_SUBSCR_TUPLE_INT | 1,849,860 | 2.6% |
| LOAD_CONST | 1,700,980 | 2.4% |
| CALL | 371,840 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 62,539,680 | 87.6% |
| COPY | 4,168,480 | 5.8% |
| YIELD_VALUE | 1,793,620 | 2.5% |
| RETURN_VALUE | 1,607,520 | 2.3% |
| LOAD_FAST | 391,660 | 0.5% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,224,440 | 86.6% |
| LOAD_FAST_LOAD_FAST | 4,355,000 | 9.1% |
| LOAD_GLOBAL_MODULE | 878,120 | 1.8% |
| LOAD_CONST | 851,080 | 1.8% |
| BUILD_LIST | 292,760 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 45,285,640 | 95.1% |
| CALL_PY_EXACT_ARGS | 586,100 | 1.2% |
| LOAD_FAST | 585,720 | 1.2% |
| BUILD_TUPLE | 371,840 | 0.8% |
| GET_ITER | 292,940 | 0.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 292,800 | 99.9% |
| CALL_INTRINSIC_1 | 80 | 0.0% |
| STORE_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 292,680 | 99.9% |
| RETURN_VALUE | 80 | 0.0% |
| COPY_FREE_VARS | 80 | 0.0% |
| RESUME_CHECK | 60 | 0.0% |
| CALL | 40 | 0.0% |


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
| ENTER_EXECUTOR | 3,875,460 | 83.4% |
| LOAD_CONST | 771,660 | 16.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 4,354,400 | 93.7% |
| STORE_FAST | 292,720 | 6.3% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 294,220 | 99.7% |
| COMPARE_OP | 460 | 0.2% |
| LOAD_FAST | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 293,200 | 99.4% |
| POP_JUMP_IF_FALSE | 580 | 0.2% |
| COMPARE_OP_INT | 520 | 0.2% |
| COMPARE_OP | 460 | 0.2% |
| COMPARE_OP_FLOAT | 80 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 833,540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 447,700 | 53.7% |
| POP_JUMP_IF_TRUE | 385,840 | 46.3% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,032,780 | 46.4% |
| BUILD_TUPLE | 4,168,480 | 38.5% |
| LOAD_FAST_LOAD_FAST | 864,300 | 8.0% |
| SWAP | 664,560 | 6.1% |
| BINARY_OP | 105,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 5,032,780 | 46.4% |
| COPY | 5,032,780 | 46.4% |
| IS_OP | 664,560 | 6.1% |
| LOAD_DEREF | 105,760 | 1.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 62,353,680 | 44.0% |
| CACHE | 40,052,400 | 28.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 34,958,180 | 24.7% |
| CALL_KW | 4,354,400 | 3.1% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 79,365,060 | 56.0% |
| RETURN_GENERATOR | 62,353,760 | 44.0% |
| RESUME | 140 | 0.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 324,864,960 | 87.1% |
| POP_JUMP_IF_TRUE | 30,738,660 | 8.2% |
| ENTER_EXECUTOR | 8,422,120 | 2.3% |
| STORE_SUBSCR | 5,031,420 | 1.3% |
| POP_JUMP_IF_FALSE | 2,251,020 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 260,347,940 | 69.8% |
| FOR_ITER_LIST | 63,096,780 | 16.9% |
| POP_JUMP_IF_FALSE | 22,785,920 | 6.1% |
| LOAD_FAST | 8,985,840 | 2.4% |
| ENTER_EXECUTOR | 8,422,120 | 2.3% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,448,480 | 99.9% |
| POP_JUMP_IF_FALSE | 8,800 | 0.1% |
| COMPARE_OP_FLOAT | 60 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 9,448,480 | 99.9% |
| JUMP_BACKWARD | 8,800 | 0.1% |
| POP_JUMP_IF_FALSE | 80 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,064,180 | 66.4% |
| SWAP | 534,920 | 33.4% |
| JUMP_BACKWARD | 2,800 | 0.2% |
| FOR_ITER | 1,780 | 0.1% |
| LOAD_FAST | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,600,420 | 99.8% |
| FOR_ITER | 1,780 | 0.1% |
| UNPACK_SEQUENCE | 380 | 0.0% |
| RETURN_CONST | 300 | 0.0% |
| SWAP | 280 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 8,783,900 | 86.9% |
| COPY | 664,560 | 6.6% |
| CALL_TYPE_1 | 664,540 | 6.6% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,113,040 | 100.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 332,460 | 73.2% |
| POP_TOP | 108,480 | 23.9% |
| EXTENDED_ARG | 8,800 | 1.9% |
| STORE_SUBSCR | 1,360 | 0.3% |
| MAP_ADD | 1,020 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 440,360 | 97.0% |
| LOAD_FAST | 9,120 | 2.0% |
| FOR_ITER | 2,800 | 0.6% |
| FOR_ITER_TUPLE | 920 | 0.2% |
| ENTER_EXECUTOR | 400 | 0.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR | 10,318,560 | 68.3% |
| ENTER_EXECUTOR | 1,407,620 | 9.3% |
| POP_JUMP_IF_FALSE | 664,620 | 4.4% |
| JUMP_FORWARD | 664,560 | 4.4% |
| STORE_FAST | 510,320 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 10,318,560 | 68.3% |
| LOAD_FAST | 2,843,760 | 18.8% |
| STORE_FAST | 776,880 | 5.1% |
| JUMP_FORWARD | 664,560 | 4.4% |
| LOAD_FAST_LOAD_FAST | 324,400 | 2.1% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 585,760 | 99.9% |
| LOAD_FAST | 240 | 0.0% |
| BUILD_TUPLE | 80 | 0.0% |
| JUMP_FORWARD | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 585,420 | 99.9% |
| JUMP_BACKWARD | 740 | 0.1% |


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
| LOAD_GLOBAL_MODULE | 30,604,100 | 60.2% |
| LOAD_FAST | 16,950,960 | 33.4% |
| LOAD_ATTR | 2,044,720 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 1,222,260 | 2.4% |
| LOAD_ATTR_PROPERTY | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 30,603,920 | 60.2% |
| LOAD_DEREF | 8,708,800 | 17.1% |
| BINARY_OP_MULTIPLY_INT | 3,769,120 | 7.4% |
| LOAD_FAST | 2,528,680 | 5.0% |
| LOAD_ATTR | 2,044,720 | 4.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 75,432,200 | 44.9% |
| BUILD_TUPLE | 62,539,680 | 37.2% |
| BINARY_SUBSCR_TUPLE_INT | 9,348,020 | 5.6% |
| STORE_ATTR_SLOT | 8,783,900 | 5.2% |
| STORE_FAST_LOAD_FAST | 1,700,580 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 67,261,860 | 40.0% |
| MAKE_FUNCTION | 63,032,400 | 37.5% |
| BINARY_SUBSCR_TUPLE_INT | 14,897,720 | 8.9% |
| LOAD_FAST | 10,776,040 | 6.4% |
| BINARY_OP | 1,761,480 | 1.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 66,708,760 | 27.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 62,353,680 | 26.0% |
| BINARY_SUBSCR | 31,291,680 | 13.0% |
| POP_JUMP_IF_FALSE | 30,604,000 | 12.8% |
| STORE_SUBSCR | 20,964,080 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 191,857,320 | 80.0% |
| PUSH_NULL | 43,667,280 | 18.2% |
| COMPARE_OP_INT | 4,354,360 | 1.8% |
| LIST_EXTEND | 80 | 0.0% |
| COMPARE_OP | 40 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 191,857,320 | 17.3% |
| LOAD_GLOBAL_BUILTIN | 110,514,500 | 10.0% |
| RESUME_CHECK | 106,363,340 | 9.6% |
| STORE_FAST | 72,476,140 | 6.5% |
| LOAD_ATTR_SLOT | 65,008,120 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 130,015,840 | 11.7% |
| BINARY_SUBSCR | 126,108,600 | 11.4% |
| LOAD_CONST | 75,432,200 | 6.8% |
| CALL_PY_EXACT_ARGS | 64,338,560 | 5.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 63,310,960 | 5.7% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,120,400 | 67.7% |
| LOAD_FAST_AND_CLEAR | 534,880 | 32.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,120,400 | 67.7% |
| LOAD_FAST_AND_CLEAR | 534,880 | 32.3% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 292,760 | 100.0% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 292,680 | 100.0% |
| LOAD_FAST | 80 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 88,230,880 | 28.6% |
| STORE_FAST | 60,189,860 | 19.5% |
| POP_JUMP_IF_FALSE | 32,954,800 | 10.7% |
| STORE_ATTR_SLOT | 31,268,440 | 10.1% |
| BINARY_OP_MULTIPLY_INT | 30,896,520 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 71,320,680 | 23.1% |
| CALL_BUILTIN_FAST | 56,928,840 | 18.5% |
| BINARY_OP_MULTIPLY_INT | 48,105,760 | 15.6% |
| LOAD_FAST | 44,188,880 | 14.3% |
| BINARY_OP | 39,893,680 | 12.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 900 | 20.7% |
| POP_JUMP_IF_FALSE | 760 | 17.5% |
| LOAD_FAST | 480 | 11.1% |
| LOAD_CONST | 280 | 6.5% |
| RESUME_CHECK | 280 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,420 | 32.7% |
| LOAD_GLOBAL_BUILTIN | 760 | 17.5% |
| LOAD_FAST | 700 | 16.1% |
| LOAD_ATTR | 420 | 9.7% |
| LOAD_CONST | 300 | 6.9% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 50.0% |
| LOAD_SUPER_ATTR_METHOD | 40 | 50.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 80 | 50.0% |
| CALL_PY_EXACT_ARGS | 60 | 37.5% |
| CALL | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 80 | 50.0% |
| RESUME_CHECK | 60 | 37.5% |
| RESUME | 20 | 12.5% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 293,140 | 54.7% |
| LOAD_FAST | 242,380 | 45.3% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 534,540 | 99.8% |
| JUMP_BACKWARD | 1,020 | 0.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 71,896,020 | 48.8% |
| TO_BOOL_BOOL | 34,553,040 | 23.5% |
| ENTER_EXECUTOR | 22,785,920 | 15.5% |
| IS_OP | 10,113,040 | 6.9% |
| TO_BOOL | 4,354,640 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 32,954,800 | 22.4% |
| LOAD_GLOBAL_BUILTIN | 32,913,600 | 22.3% |
| LOAD_GLOBAL_MODULE | 32,429,480 | 22.0% |
| LOAD_DEREF | 30,604,000 | 20.8% |
| LOAD_FAST | 13,879,620 | 9.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 9,448,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 9,448,400 | 100.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_FLOAT | 31,176,860 | 97.9% |
| CONTAINS_OP | 385,840 | 1.2% |
| COMPARE_OP | 293,200 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 30,738,660 | 96.5% |
| LOAD_FAST | 679,020 | 2.1% |
| JUMP_BACKWARD | 332,460 | 1.0% |
| LOAD_DEREF | 105,760 | 0.3% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 62,390,320 | 98.7% |
| FOR_ITER_TUPLE | 442,240 | 0.7% |
| ENTER_EXECUTOR | 371,540 | 0.6% |
| RESUME_CHECK | 34,620 | 0.1% |
| FOR_ITER | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 62,867,220 | 99.4% |
| POP_TOP | 371,840 | 0.6% |
| EXIT_INIT_CHECK | 60 | 0.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 62,353,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,353,760 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 58.3% |
| LOAD_FAST_LOAD_FAST | 200 | 41.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 120 | 25.0% |
| STORE_ATTR_SLOT | 120 | 25.0% |
| LOAD_CONST | 80 | 16.7% |
| LOAD_FAST | 60 | 12.5% |
| LOAD_GLOBAL | 60 | 12.5% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 80 | 50.0% |
| SWAP | 80 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 80 | 50.0% |
| STORE_FAST | 80 | 50.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 54,150,560 | 20.1% |
| CALL | 45,285,640 | 16.8% |
| STORE_FAST | 42,251,800 | 15.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 41,716,800 | 15.5% |
| BINARY_OP | 25,485,260 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 72,476,140 | 26.9% |
| LOAD_DEREF | 66,708,760 | 24.7% |
| LOAD_FAST_LOAD_FAST | 60,189,860 | 22.3% |
| STORE_FAST | 42,251,800 | 15.7% |
| LOAD_GLOBAL_MODULE | 24,248,720 | 9.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 1,550,640 | 67.8% |
| FOR_ITER_RANGE | 585,740 | 25.6% |
| FOR_ITER_LIST | 149,900 | 6.6% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,700,580 | 74.4% |
| LOAD_FAST | 585,760 | 25.6% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 61,207,680 | 94.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,880,120 | 2.9% |
| UNPACK_SEQUENCE_TUPLE | 734,960 | 1.1% |
| BINARY_OP_MULTIPLY_INT | 585,420 | 0.9% |
| STORE_FAST_STORE_FAST | 106,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,683,720 | 50.7% |
| LOAD_GLOBAL_MODULE | 31,003,500 | 48.1% |
| STORE_FAST | 628,240 | 1.0% |
| STORE_FAST_STORE_FAST | 106,800 | 0.2% |
| LOAD_CONST | 92,960 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 5,032,780 | 35.7% |
| SWAP | 5,032,780 | 35.7% |
| LOAD_FAST_AND_CLEAR | 1,120,400 | 8.0% |
| LOAD_GLOBAL_BUILTIN | 664,540 | 4.7% |
| BUILD_LIST | 585,600 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR | 5,032,780 | 35.7% |
| SWAP | 5,032,780 | 35.7% |
| STORE_FAST | 1,120,320 | 8.0% |
| COPY | 664,560 | 4.7% |
| BUILD_LIST | 585,600 | 4.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 380 | 55.9% |
| LOAD_FAST | 200 | 29.4% |
| FOR_ITER_LIST | 40 | 5.9% |
| CALL | 20 | 2.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 300 | 44.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 260 | 38.2% |
| UNPACK_SEQUENCE_TUPLE | 80 | 11.8% |
| STORE_FAST | 40 | 5.9% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 260,347,940 | 80.2% |
| BINARY_OP_MULTIPLY_FLOAT | 41,716,800 | 12.9% |
| BINARY_SUBSCR | 20,637,440 | 6.4% |
| BUILD_TUPLE | 1,793,620 | 0.6% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 324,495,840 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 340 | 34.0% |
| CALL | 340 | 34.0% |
| COPY_FREE_VARS | 140 | 14.0% |
| POP_TOP | 120 | 12.0% |
| CALL_FUNCTION_EX | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 420 | 42.0% |
| LOAD_GLOBAL | 260 | 26.0% |
| POP_TOP | 120 | 12.0% |
| LOAD_CONST | 60 | 6.0% |
| LOAD_DEREF | 40 | 4.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 105,760 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 105,800 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 28,837,600 | 92.0% |
| LOAD_CONST | 1,179,640 | 3.8% |
| BINARY_OP | 856,760 | 2.7% |
| LOAD_FAST | 478,900 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 22,859,560 | 72.9% |
| LOAD_FAST_LOAD_FAST | 7,428,940 | 23.7% |
| LOAD_FAST | 585,420 | 1.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 478,900 | 1.5% |
| RETURN_VALUE | 60 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,716,760 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 41,716,800 | 100.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 48,105,760 | 49.1% |
| BINARY_OP | 36,261,020 | 37.0% |
| LOAD_FAST | 8,898,680 | 9.1% |
| LOAD_ATTR | 3,769,120 | 3.8% |
| LOAD_CONST | 878,080 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 30,896,520 | 31.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 30,018,280 | 30.6% |
| BINARY_OP_ADD_INT | 28,837,600 | 29.4% |
| LOAD_FAST | 3,071,060 | 3.1% |
| CALL_BUILTIN_FAST | 1,900,200 | 1.9% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 8,880 | 98.2% |
| BINARY_OP | 80 | 0.9% |
| LOAD_FAST | 80 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,920 | 98.7% |
| STORE_FAST | 60 | 0.7% |
| CALL_BUILTIN_O | 40 | 0.4% |
| CALL | 20 | 0.2% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 292,680 | 100.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 292,700 | 100.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,032,080 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 62,353,760 | 98.9% |
| PUSH_EXC_INFO | 385,660 | 0.6% |
| STORE_FAST | 292,700 | 0.5% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 292,680 | 100.0% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 292,700 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 14,897,720 | 100.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,348,020 | 62.7% |
| BUILD_TUPLE | 1,849,860 | 12.4% |
| UNARY_NEGATIVE | 1,607,500 | 10.8% |
| LOAD_ATTR | 1,222,260 | 8.2% |
| LOAD_FAST | 484,720 | 3.3% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 60 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_INT | 30,018,280 | 84.9% |
| CALL_BUILTIN_CLASS | 4,354,360 | 12.3% |
| LOAD_FAST_LOAD_FAST | 585,400 | 1.7% |
| LOAD_FAST | 385,800 | 1.1% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 34,958,180 | 98.9% |
| RESUME_CHECK | 385,820 | 1.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,647,500 | 49.3% |
| RETURN_VALUE | 3,214,960 | 34.1% |
| LOAD_CONST | 585,400 | 6.2% |
| BINARY_OP_MULTIPLY_INT | 585,400 | 6.2% |
| CALL_FUNCTION_EX | 292,680 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BOUND_METHOD_EXACT_ARGS | 4,354,360 | 46.2% |
| BINARY_OP | 1,607,500 | 17.1% |
| LOAD_GLOBAL_BUILTIN | 1,607,480 | 17.1% |
| STORE_FAST | 678,480 | 7.2% |
| GET_ITER | 585,420 | 6.2% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 56,928,840 | 96.8% |
| BINARY_OP_MULTIPLY_INT | 1,900,200 | 3.2% |
| CALL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 54,150,560 | 92.0% |
| RETURN_VALUE | 4,678,680 | 8.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 62,353,600 | 98.0% |
| BINARY_OP_ADD_INT | 478,900 | 0.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 478,900 | 0.8% |
| CALL | 292,820 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 62,353,680 | 98.0% |
| STORE_FAST | 771,620 | 1.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 478,900 | 0.8% |
| CALL | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 40 | 66.7% |
| CALL | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 30,311,160 | 91.6% |
| LOAD_ATTR_MODULE | 2,192,880 | 6.6% |
| LOAD_GLOBAL_BUILTIN | 585,400 | 1.8% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 33,089,440 | 100.0% |
| TO_BOOL | 80 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,647,200 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 4,354,380 | 93.7% |
| BINARY_OP | 292,860 | 6.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 385,800 | 50.0% |
| ENTER_EXECUTOR | 385,520 | 50.0% |
| BUILD_TUPLE | 280 | 0.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 771,640 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 360 | 81.8% |
| BUILD_LIST | 40 | 9.1% |
| CALL | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 360 | 81.8% |
| POP_TOP | 60 | 13.6% |
| UNPACK_SEQUENCE | 20 | 4.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,598,600 | 99.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 16,820 | 1.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,306,040 | 80.8% |
| LOAD_CONST | 292,700 | 18.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 16,820 | 1.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 385,800 | 78.4% |
| LOAD_FAST | 106,000 | 21.6% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 491,860 | 100.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,338,560 | 40.1% |
| GET_ITER | 62,739,400 | 39.1% |
| LOAD_FAST_LOAD_FAST | 30,162,120 | 18.8% |
| LOAD_ATTR_MODULE | 1,900,160 | 1.2% |
| CALL | 586,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 97,665,440 | 60.8% |
| COPY_FREE_VARS | 62,353,680 | 38.8% |
| RETURN_GENERATOR | 478,760 | 0.3% |
| CALL_PY_EXACT_ARGS | 31,800 | 0.0% |
| MAKE_CELL | 60 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,112,920 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 9,448,400 | 93.4% |
| IS_OP | 664,540 | 6.6% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 31,176,840 | 100.0% |
| LOAD_FAST | 8,920 | 0.0% |
| COMPARE_OP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 31,176,860 | 100.0% |
| POP_JUMP_IF_FALSE | 8,920 | 0.0% |
| EXTENDED_ARG | 60 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 67,261,860 | 93.6% |
| LOAD_DEREF | 4,354,360 | 6.1% |
| LOAD_FAST_LOAD_FAST | 279,280 | 0.4% |
| COMPARE_OP | 520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 71,896,020 | 100.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 665,400 | 100.0% |
| COMPARE_OP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 372,440 | 56.0% |
| POP_JUMP_IF_FALSE | 293,020 | 44.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 63,096,780 | 50.0% |
| LOAD_FAST | 62,390,240 | 49.4% |
| JUMP_BACKWARD | 440,360 | 0.3% |
| GET_ITER | 301,720 | 0.2% |
| FOR_ITER_TUPLE | 3,180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 62,390,320 | 49.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 41,716,760 | 33.0% |
| STORE_FAST | 21,377,960 | 16.9% |
| ENTER_EXECUTOR | 585,100 | 0.5% |
| STORE_FAST_LOAD_FAST | 149,900 | 0.1% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 585,440 | 50.0% |
| SWAP | 585,420 | 50.0% |
| JUMP_BACKWARD | 360 | 0.0% |
| GET_ITER | 60 | 0.0% |
| FOR_ITER | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 585,740 | 50.0% |
| SWAP | 585,440 | 50.0% |
| STORE_FAST | 60 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,829,040 | 74.3% |
| LOAD_FAST | 349,260 | 14.2% |
| GET_ITER | 278,840 | 11.3% |
| FOR_ITER_LIST | 3,200 | 0.1% |
| JUMP_BACKWARD | 920 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 1,550,640 | 63.0% |
| RETURN_CONST | 442,240 | 18.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 186,200 | 7.6% |
| LOAD_FAST | 185,920 | 7.6% |
| STORE_FAST | 93,100 | 3.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 62,971,120 | 99.4% |
| LOAD_FAST_LOAD_FAST | 385,640 | 0.6% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,125,380 | 99.6% |
| STORE_FAST | 231,380 | 0.4% |
| STORE_SUBSCR | 120 | 0.0% |
| BUILD_LIST | 60 | 0.0% |
| SWAP | 60 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,084,660 | 84.1% |
| RETURN_VALUE | 478,560 | 9.9% |
| LOAD_FAST_CHECK | 292,680 | 6.0% |
| LOAD_ATTR_METHOD_NO_DICT | 940 | 0.0% |
| LOAD_ATTR | 340 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,871,340 | 59.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,598,600 | 32.9% |
| LOAD_CONST | 385,820 | 7.9% |
| LOAD_ATTR_METHOD_NO_DICT | 940 | 0.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 360 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,310,960 | 100.0% |
| LOAD_ATTR | 220 | 0.0% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 63,311,160 | 100.0% |
| LOAD_CONST | 60 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 58,243,560 | 100.0% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 54,150,740 | 93.0% |
| CALL_ISINSTANCE | 2,192,880 | 3.8% |
| CALL_PY_EXACT_ARGS | 1,900,160 | 3.3% |
| CALL | 80 | 0.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,246,240 | 100.0% |
| LOAD_ATTR | 560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,219,240 | 99.2% |
| BINARY_OP_MULTIPLY_INT | 27,040 | 0.8% |
| LOAD_ATTR | 520 | 0.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,015,840 | 100.0% |
| LOAD_ATTR | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,008,120 | 50.0% |
| STORE_FAST_STORE_FAST | 61,207,680 | 47.1% |
| RETURN_VALUE | 3,800,440 | 2.9% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 74,935,420 | 45.8% |
| POP_JUMP_IF_FALSE | 32,913,600 | 20.1% |
| STORE_SUBSCR | 31,176,800 | 19.1% |
| POP_JUMP_IF_NOT_NONE | 9,448,400 | 5.8% |
| CALL_TYPE_1 | 9,448,400 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 110,514,500 | 67.6% |
| LOAD_GLOBAL_MODULE | 40,052,320 | 24.5% |
| IS_OP | 8,783,900 | 5.4% |
| LOAD_CONST | 1,357,040 | 0.8% |
| SWAP | 664,540 | 0.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 40,052,320 | 23.8% |
| LOAD_FAST | 35,282,320 | 21.0% |
| POP_JUMP_IF_FALSE | 32,429,480 | 19.3% |
| STORE_FAST_STORE_FAST | 31,003,500 | 18.5% |
| STORE_FAST | 24,248,720 | 14.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 58,243,560 | 34.7% |
| LOAD_FAST | 42,287,480 | 25.2% |
| LOAD_ATTR | 30,604,100 | 18.2% |
| CALL_ISINSTANCE | 30,311,160 | 18.0% |
| LOAD_FAST_LOAD_FAST | 3,950,840 | 2.4% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,052,320 | 100.0% |
| LOAD_SUPER_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,052,360 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 333,005,880 | 57.8% |
| CALL_PY_EXACT_ARGS | 97,665,440 | 16.9% |
| COPY_FREE_VARS | 79,365,060 | 13.8% |
| POP_TOP | 62,832,440 | 10.9% |
| LOAD_ATTR_PROPERTY | 3,219,240 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 324,495,720 | 56.3% |
| LOAD_FAST | 106,363,340 | 18.5% |
| LOAD_GLOBAL_BUILTIN | 74,935,420 | 13.0% |
| NOP | 62,739,420 | 10.9% |
| LOAD_DEREF | 4,354,440 | 0.8% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 66.7% |
| STORE_ATTR | 120 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 180 | 50.0% |
| LOAD_GLOBAL_MODULE | 80 | 22.2% |
| LOAD_GLOBAL | 60 | 16.7% |
| LOAD_GLOBAL_BUILTIN | 40 | 11.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 71,320,680 | 89.0% |
| LOAD_FAST | 8,783,880 | 11.0% |
| STORE_ATTR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,052,340 | 50.0% |
| LOAD_FAST_LOAD_FAST | 31,268,440 | 39.0% |
| LOAD_CONST | 8,783,900 | 11.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 385,640 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 385,660 | 100.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 33,089,440 | 95.8% |
| LOAD_ATTR | 878,040 | 2.5% |
| LOAD_FAST | 585,400 | 1.7% |
| TO_BOOL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 34,553,040 | 100.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 93.3% |
| TO_BOOL | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 300 | 100.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,472,040 | 100.0% |
| TO_BOOL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,472,100 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 734,880 | 100.0% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 734,960 | 100.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 41,716,760 | 95.7% |
| FOR_ITER | 1,600,420 | 3.7% |
| FOR_ITER_TUPLE | 186,200 | 0.4% |
| LOAD_FAST | 92,920 | 0.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 41,716,800 | 95.7% |
| STORE_FAST_STORE_FAST | 1,880,120 | 4.3% |


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
|     deferred | 86,099,780 | 16.4% |
|          hit | 437,439,640 | 83.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 840 | 3.1% |
| Failure | 26,240 | 96.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| floor divide | 22,140 | 84.4% |
| add other | 1,980 | 7.5% |
| true divide other | 580 | 2.2% |
| true divide different types | 500 | 1.9% |
| multiply different types | 480 | 1.8% |
| multiply other | 300 | 1.1% |
| subtract different types | 260 | 1.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 131,141,660 | 54.9% |
|          hit | 107,560,040 | 45.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 360 | 1.0% |
| Failure | 35,380 | 99.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 34,080 | 96.3% |
| buffer int | 1,300 | 3.7% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 50,135,440 | 10.5% |
|          hit | 427,573,040 | 89.5% |
|         miss | 2,581,280 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 50,520 | 77.2% |
| Failure | 14,920 | 22.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| cfunc varargs keywords | 11,560 | 77.5% |
| metaclass | 1,840 | 12.3% |
| class no vectorcall | 1,300 | 8.7% |
| class mutable | 160 | 1.1% |
| cfunc noargs | 60 | 0.4% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 293,840 | 0.2% |
|          hit | 132,187,980 | 99.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 660 | 58.9% |
| Failure | 460 | 41.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 460 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,934,240 | 1.5% |
|          hit | 129,526,260 | 98.5% |
|         miss | 338,860 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,620 | 78.8% |
| Failure | 1,780 | 21.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 1,460 | 82.0% |
| zip | 320 | 18.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 50,875,620 | 13.4% |
|          hit | 329,965,180 | 86.6% |
|         miss | 78,280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,060 | 11.8% |
| Failure | 22,920 | 88.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 11,760 | 51.3% |
| metaclass attribute | 8,620 | 37.6% |
| method | 1,280 | 5.6% |
| class method obj | 1,260 | 5.5% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,160 | 0.0% |
|          hit | 331,519,040 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,180 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 40,052,360 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> specialization stats for POP_JUMP_IF_FALSE family </summary>


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
|     deferred | 240 | 0.0% |
|          hit | 80,105,040 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 67,598,240 | 99.4% |
|          hit | 385,660 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 0.1% |
| Failure | 18,420 | 99.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict subclass no override | 18,420 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,354,640 | 10.5% |
|          hit | 37,025,440 | 89.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 16.0% |
| Failure | 1,260 | 84.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict | 1,260 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 340 | 0.0% |
|          hit | 294,582,380 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 340 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 4,643,012,680 | 61.8% |
| Not specialized | 578,239,740 | 7.7% |
| Specialized hits | 2,291,638,960 | 30.5% |
| Specialized misses | 2,999,340 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 131,141,660 | 33.4% |
| BINARY_OP | 86,099,780 | 21.9% |
| STORE_SUBSCR | 67,598,240 | 17.2% |
| LOAD_ATTR | 50,875,620 | 13.0% |
| CALL | 50,135,440 | 12.8% |
| TO_BOOL | 4,354,640 | 1.1% |
| FOR_ITER | 1,934,240 | 0.5% |
| COMPARE_OP | 293,840 | 0.1% |
| LOAD_GLOBAL | 2,160 | 0.0% |
| UNPACK_SEQUENCE | 340 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,686,380 | 56.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 894,900 | 29.8% |
| FOR_ITER_LIST | 169,600 | 5.7% |
| FOR_ITER_TUPLE | 169,260 | 5.6% |
| LOAD_ATTR_METHOD_NO_DICT | 50,720 | 1.7% |
| LOAD_ATTR_PROPERTY | 27,560 | 0.9% |
| RESUME | 920 | 0.0% |
| RESUME_CHECK | 920 | 0.0% |
| CACHE | 0 | 0.0% |
| CHECK_EXC_MATCH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 435,891,180 | 67.7% |
| Calls to Python functions inlined | 207,848,900 | 32.3% |
| Calls via PyEval_EvalFrame (total) | 435,891,180 | 67.7% |
| Calls via PyEval_EvalFrame (vector) | 48,562,780 | 7.5% |
| Calls via PyEval_EvalFrame (generator) | 387,328,400 | 60.2% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 48,562,780 | 7.5% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 34,111,680 | 5.3% |
| Calls via PyEval_EvalFrame (function ex) | 160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 2,223,400 | 0.3% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 385,680 | 0.1% |
| Frames pushed | 256,411,740 | 39.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 508,804,980 | 51.5% |
| Frees to freelist | 509,131,700 |  |
| Allocations | 479,320,060 | 48.5% |
| Allocations to 512 bytes | 478,712,800 | 48.4% |
| Allocations to 4 kbytes | 605,340 | 0.1% |
| Allocations over 4 kbytes | 1,920 | 0.0% |
| Frees | 479,746,464 |  |
| New values | 20 |  |
| Interpreter increfs | 3,572,780,500 | 48.1% |
| Interpreter decrefs | 4,215,022,420 | 50.2% |
| Increfs | 3,849,939,960 | 51.9% |
| Decrefs | 4,188,118,569 | 49.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 102,223,644 |  |
| Method cache misses | 132,476 |  |
| Method cache collisions | 191,146 |  |
| Method cache dunder hits | 71,165,919 |  |
| Method cache dunder misses | 59,081 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 8,500 | 0 | 45,879,440 |
| 1 | 760 | 0 | 42,808,360 |
| 2 | 60 | 0 | 21,867,080 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 960 |  |
| Traces created | 960 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 20 | 2.1% |
| Recursive call | 0 | 0.0% |
| Low confidence | 60 | 6.2% |
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
| <= 16 | 80 | 8.3% |
| <= 32 | 160 | 16.7% |
| <= 64 | 60 | 6.2% |
| <= 128 | 620 | 64.6% |
| <= 256 | 40 | 4.2% |


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
| <= 16 | 100 | 10.4% |
| <= 32 | 160 | 16.7% |
| <= 64 | 100 | 10.4% |
| <= 128 | 20 | 2.1% |
| <= 256 | 20 | 2.1% |


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
| YIELD_VALUE | 120 |
| CALL_KW | 20 |
| CALL_LIST_APPEND | 20 |


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
