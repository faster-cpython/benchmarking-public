
# Pystats results

- benchmark: regex_v8
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_CONST | 24,667,300 | 14.8% | 14.8% |  |
| LOAD_GLOBAL_MODULE | 17,919,240 | 10.8% | 25.6% | 0.1% |
| POP_TOP | 16,763,500 | 10.1% | 35.7% |  |
| CALL | 16,588,200 | 10.0% | 45.7% |  |
| LOAD_FAST | 12,297,140 | 7.4% | 53.0% |  |
| BINARY_SUBSCR_LIST_INT | 10,082,280 | 6.1% | 59.1% | 0.1% |
| ENTER_EXECUTOR | 8,934,280 | 5.4% | 64.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 7,546,940 | 4.5% | 69.0% |  |
| LOAD_GLOBAL_BUILTIN | 4,546,840 | 2.7% | 71.7% | 0.0% |
| POP_JUMP_IF_FALSE | 4,516,940 | 2.7% | 74.5% |  |
| LOAD_FAST_LOAD_FAST | 4,412,400 | 2.7% | 77.1% |  |
| RESUME_CHECK | 4,233,100 | 2.5% | 79.7% |  |
| RETURN_VALUE | 4,163,120 | 2.5% | 82.2% |  |
| CALL_PY_EXACT_ARGS | 2,309,640 | 1.4% | 83.6% | 0.0% |
| LOAD_ATTR_MODULE | 2,245,600 | 1.4% | 84.9% | 0.0% |
| TO_BOOL_BOOL | 1,841,900 | 1.1% | 86.0% |  |
| CALL_ISINSTANCE | 1,797,200 | 1.1% | 87.1% |  |
| BUILD_TUPLE | 1,787,640 | 1.1% | 88.2% |  |
| NOP | 1,780,700 | 1.1% | 89.2% |  |
| BINARY_SUBSCR_DICT | 1,734,200 | 1.0% | 90.3% |  |
| CALL_TYPE_1 | 1,727,220 | 1.0% | 91.3% |  |
| STORE_FAST | 1,625,180 | 1.0% | 92.3% |  |
| PUSH_NULL | 1,480,540 | 0.9% | 93.2% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,086,520 | 0.7% | 93.8% |  |
| IS_OP | 868,140 | 0.5% | 94.4% |  |
| STORE_FAST_STORE_FAST | 810,960 | 0.5% | 94.8% |  |
| TO_BOOL | 769,020 | 0.5% | 95.3% |  |
| TO_BOOL_LIST | 763,760 | 0.5% | 95.8% | 0.0% |
| IMPORT_NAME | 750,200 | 0.5% | 96.2% |  |
| CALL_KW | 749,600 | 0.5% | 96.7% |  |
| UNPACK_EX | 748,800 | 0.5% | 97.1% |  |
| CALL_PY_WITH_DEFAULTS | 743,180 | 0.4% | 97.6% |  |
| LOAD_ATTR | 349,360 | 0.2% | 97.8% |  |
| INTERPRETER_EXIT | 310,380 | 0.2% | 98.0% |  |
| POP_JUMP_IF_NOT_NONE | 290,640 | 0.2% | 98.1% |  |
| POP_JUMP_IF_NONE | 278,740 | 0.2% | 98.3% |  |
| EXTENDED_ARG | 155,460 | 0.1% | 98.4% |  |
| CALL_BUILTIN_O | 149,600 | 0.1% | 98.5% | 0.1% |
| FOR_ITER_RANGE | 140,600 | 0.1% | 98.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 125,520 | 0.1% | 98.7% |  |
| RETURN_CONST | 119,280 | 0.1% | 98.7% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 118,740 | 0.1% | 98.8% |  |
| POP_JUMP_IF_TRUE | 113,200 | 0.1% | 98.9% |  |
| CONTAINS_OP | 111,520 | 0.1% | 98.9% |  |
| BINARY_OP | 104,760 | 0.1% | 99.0% |  |
| COMPARE_OP_STR | 98,100 | 0.1% | 99.1% | 2.9% |
| TO_BOOL_INT | 97,840 | 0.1% | 99.1% |  |
| CALL_LEN | 95,380 | 0.1% | 99.2% |  |
| LOAD_GLOBAL | 94,240 | 0.1% | 99.2% |  |
| BINARY_SUBSCR | 93,100 | 0.1% | 99.3% |  |
| GET_ITER | 89,960 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_INT | 81,320 | 0.0% | 99.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 79,720 | 0.0% | 99.4% |  |
| JUMP_FORWARD | 78,940 | 0.0% | 99.5% |  |
| JUMP_BACKWARD | 58,360 | 0.0% | 99.5% |  |
| BINARY_SUBSCR_STR_INT | 56,240 | 0.0% | 99.5% | 5.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 53,160 | 0.0% | 99.6% | 0.9% |
| CALL_BUILTIN_CLASS | 48,480 | 0.0% | 99.6% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 44,800 | 0.0% | 99.6% | 0.1% |
| FOR_ITER_LIST | 44,660 | 0.0% | 99.7% |  |
| BUILD_LIST | 41,920 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_GETITEM | 40,080 | 0.0% | 99.7% |  |
| CALL_LIST_APPEND | 37,320 | 0.0% | 99.7% |  |
| COMPARE_OP_INT | 34,780 | 0.0% | 99.8% |  |
| FOR_ITER | 34,040 | 0.0% | 99.8% |  |
| BINARY_OP_SUBTRACT_INT | 32,380 | 0.0% | 99.8% |  |
| COPY | 29,560 | 0.0% | 99.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 28,720 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 28,540 | 0.0% | 99.8% | 0.6% |
| STORE_SUBSCR_LIST_INT | 13,520 | 0.0% | 99.9% |  |
| TO_BOOL_NONE | 12,520 | 0.0% | 99.9% | 18.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 12,240 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 11,800 | 0.0% | 99.9% | 0.5% |
| LOAD_NAME | 11,680 | 0.0% | 99.9% |  |
| STORE_FAST_LOAD_FAST | 10,700 | 0.0% | 99.9% |  |
| COMPARE_OP | 10,220 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 9,760 | 0.0% | 99.9% | 0.8% |
| LOAD_ATTR_PROPERTY | 9,120 | 0.0% | 99.9% |  |
| UNARY_NOT | 8,720 | 0.0% | 99.9% |  |
| EXIT_INIT_CHECK | 7,820 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 7,820 | 0.0% | 99.9% |  |
| STORE_SUBSCR_DICT | 7,380 | 0.0% | 99.9% |  |
| BUILD_SLICE | 7,220 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 7,180 | 0.0% | 99.9% |  |
| STORE_SUBSCR | 6,500 | 0.0% | 99.9% |  |
| BUILD_MAP | 6,140 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 5,840 | 0.0% | 99.9% |  |
| POP_EXCEPT | 5,840 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 5,840 | 0.0% | 100.0% |  |
| SWAP | 5,680 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 5,380 | 0.0% | 100.0% |  |
| STORE_NAME | 5,180 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 5,180 | 0.0% | 100.0% |  |
| BINARY_SLICE | 4,920 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 4,860 | 0.0% | 100.0% |  |
| FORMAT_SIMPLE | 4,660 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 4,660 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 4,380 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,440 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,420 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 2,900 | 0.0% | 100.0% |  |
| MAP_ADD | 2,040 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 2,000 | 0.0% | 100.0% | 35.0% |
| UNARY_INVERT | 1,960 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 1,620 | 0.0% | 100.0% |  |
| LIST_APPEND | 1,400 | 0.0% | 100.0% |  |
| LOAD_DEREF | 1,380 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 1,360 | 0.0% | 100.0% |  |
| BUILD_STRING | 1,280 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 1,140 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 1,040 | 0.0% | 100.0% |  |
| STORE_ATTR | 840 | 0.0% | 100.0% |  |
| RESUME | 800 | 0.0% | 100.0% |  |
| BEFORE_WITH | 680 | 0.0% | 100.0% |  |
| COPY_FREE_VARS | 600 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 460 | 0.0% | 100.0% |  |
| STORE_SLICE | 440 | 0.0% | 100.0% |  |
| MAKE_CELL | 400 | 0.0% | 100.0% |  |
| DICT_MERGE | 300 | 0.0% | 100.0% |  |
| STORE_DEREF | 280 | 0.0% | 100.0% |  |
| LIST_EXTEND | 260 | 0.0% | 100.0% |  |
| YIELD_VALUE | 220 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 200 | 0.0% | 100.0% |  |
| CALL_STR_1 | 200 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 180 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 180 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 160 | 0.0% | 100.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 160 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_METHOD | 160 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 140 | 0.0% | 100.0% |  |
| STORE_ATTR_SLOT | 140 | 0.0% | 100.0% |  |
| IMPORT_FROM | 100 | 0.0% | 100.0% |  |
| DELETE_NAME | 80 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| BUILD_SET | 60 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 60 | 0.0% | 100.0% |  |
| DICT_UPDATE | 40 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| CALL POP_TOP | 13,929,940 | 8.4% | 8.4% |
| LOAD_GLOBAL_MODULE LOAD_CONST | 10,009,380 | 6.0% | 14.4% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 9,972,300 | 6.0% | 20.4% |
| POP_TOP ENTER_EXECUTOR | 8,828,080 | 5.3% | 25.7% |
| ENTER_EXECUTOR CALL | 8,467,180 | 5.1% | 30.8% |
| POP_TOP LOAD_GLOBAL_MODULE | 7,666,420 | 4.6% | 35.4% |
| BINARY_SUBSCR_LIST_INT LOAD_ATTR_METHOD_NO_DICT | 5,737,980 | 3.4% | 38.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 5,301,640 | 3.2% | 42.0% |
| LOAD_CONST LOAD_CONST | 5,008,500 | 3.0% | 45.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,617,120 | 2.2% | 47.2% |
| LOAD_CONST LOAD_GLOBAL_MODULE | 3,452,360 | 2.1% | 49.3% |
| LOAD_CONST CALL | 3,228,940 | 1.9% | 51.2% |
| BINARY_SUBSCR_LIST_INT CALL | 2,996,320 | 1.8% | 53.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,756,600 | 1.7% | 54.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 2,309,360 | 1.4% | 56.1% |
| POP_JUMP_IF_FALSE LOAD_FAST | 2,169,320 | 1.3% | 57.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,830,020 | 1.1% | 58.5% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 1,812,240 | 1.1% | 59.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,788,700 | 1.1% | 60.6% |
| RETURN_VALUE POP_TOP | 1,752,760 | 1.1% | 61.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,750,620 | 1.1% | 62.8% |
| CALL RETURN_VALUE | 1,743,960 | 1.0% | 63.8% |
| LOAD_FAST CALL | 1,734,000 | 1.0% | 64.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 1,729,120 | 1.0% | 65.9% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 1,729,040 | 1.0% | 66.9% |
| NOP LOAD_GLOBAL_MODULE | 1,727,820 | 1.0% | 68.0% |
| LOAD_FAST CALL_TYPE_1 | 1,727,160 | 1.0% | 69.0% |
| CALL_TYPE_1 LOAD_FAST_LOAD_FAST | 1,725,420 | 1.0% | 70.0% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_BUILTIN | 1,724,540 | 1.0% | 71.1% |
| BUILD_TUPLE BINARY_SUBSCR_DICT | 1,722,600 | 1.0% | 72.1% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 1,722,500 | 1.0% | 73.1% |
| BINARY_SUBSCR_DICT RETURN_VALUE | 1,721,500 | 1.0% | 74.2% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 1,715,560 | 1.0% | 75.2% |
| POP_JUMP_IF_FALSE NOP | 1,494,640 | 0.9% | 76.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 1,491,960 | 0.9% | 77.0% |
| RESUME_CHECK LOAD_FAST | 1,367,820 | 0.8% | 77.8% |
| PUSH_NULL LOAD_CONST | 1,277,100 | 0.8% | 78.6% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,259,180 | 0.8% | 79.4% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,042,940 | 0.6% | 80.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,017,680 | 0.6% | 80.6% |
| STORE_FAST LOAD_FAST | 1,002,000 | 0.6% | 81.2% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 983,620 | 0.6% | 81.8% |
| LOAD_GLOBAL_MODULE IS_OP | 864,440 | 0.5% | 82.3% |
| IS_OP POP_JUMP_IF_FALSE | 836,460 | 0.5% | 82.8% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 790,220 | 0.5% | 83.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 780,400 | 0.5% | 83.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 769,540 | 0.5% | 84.2% |
| LOAD_FAST TO_BOOL_LIST | 762,320 | 0.5% | 84.7% |
| TO_BOOL POP_JUMP_IF_FALSE | 762,240 | 0.5% | 85.1% |
| LOAD_FAST TO_BOOL | 762,220 | 0.5% | 85.6% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 755,700 | 0.5% | 86.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 754,280 | 0.5% | 86.5% |
| CALL RESUME_CHECK | 752,300 | 0.5% | 87.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST | 751,220 | 0.5% | 87.4% |
| LOAD_CONST LOAD_GLOBAL_BUILTIN | 750,260 | 0.5% | 87.9% |
| LOAD_CONST IMPORT_NAME | 750,200 | 0.5% | 88.3% |
| IMPORT_NAME STORE_FAST | 749,920 | 0.5% | 88.8% |
| LOAD_FAST LOAD_ATTR_MODULE | 749,880 | 0.5% | 89.2% |
| LOAD_CONST CALL_KW | 749,600 | 0.5% | 89.7% |
| LOAD_ATTR_MODULE LOAD_CONST | 749,440 | 0.5% | 90.1% |
| CALL_KW POP_TOP | 748,800 | 0.5% | 90.6% |
| LOAD_FAST UNPACK_EX | 748,800 | 0.5% | 91.0% |
| UNPACK_EX STORE_FAST_STORE_FAST | 748,800 | 0.5% | 91.5% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 743,180 | 0.4% | 91.9% |
| BINARY_SUBSCR_LIST_INT LOAD_GLOBAL_MODULE | 540,740 | 0.3% | 92.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 468,160 | 0.3% | 92.5% |
| BINARY_SUBSCR_LIST_INT CALL_PY_WITH_DEFAULTS | 363,200 | 0.2% | 92.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 355,640 | 0.2% | 92.9% |
| CACHE RESUME_CHECK | 316,780 | 0.2% | 93.1% |
| RETURN_VALUE INTERPRETER_EXIT | 296,140 | 0.2% | 93.3% |
| LOAD_FAST LOAD_ATTR | 295,400 | 0.2% | 93.5% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 294,260 | 0.2% | 93.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 289,240 | 0.2% | 93.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 288,340 | 0.2% | 94.0% |
| LOAD_ATTR STORE_FAST | 287,580 | 0.2% | 94.2% |
| ENTER_EXECUTOR CALL_PY_WITH_DEFAULTS | 285,760 | 0.2% | 94.4% |
| STORE_FAST NOP | 273,900 | 0.2% | 94.5% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 270,560 | 0.2% | 94.7% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 267,680 | 0.2% | 94.9% |
| POP_JUMP_IF_NONE LOAD_FAST | 266,780 | 0.2% | 95.0% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 266,640 | 0.2% | 95.2% |
| RETURN_VALUE RETURN_VALUE | 260,720 | 0.2% | 95.3% |
| LOAD_ATTR_MODULE CALL_PY_EXACT_ARGS | 224,460 | 0.1% | 95.5% |
| LOAD_FAST LOAD_CONST | 214,560 | 0.1% | 95.6% |
| LOAD_FAST PUSH_NULL | 207,260 | 0.1% | 95.7% |
| STORE_FAST LOAD_GLOBAL_MODULE | 142,620 | 0.1% | 95.8% |
| CALL CALL | 137,900 | 0.1% | 95.9% |
| PUSH_NULL LOAD_FAST | 128,520 | 0.1% | 96.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS POP_TOP | 118,460 | 0.1% | 96.0% |
| CALL_BUILTIN_O POP_TOP | 112,840 | 0.1% | 96.1% |
| POP_TOP LOAD_FAST | 105,960 | 0.1% | 96.2% |
| FOR_ITER_RANGE STORE_FAST | 91,860 | 0.1% | 96.2% |
| LOAD_FAST CALL_BUILTIN_O | 91,580 | 0.1% | 96.3% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 87,600 | 0.1% | 96.3% |
| LOAD_CONST CALL_PY_WITH_DEFAULTS | 87,000 | 0.1% | 96.4% |
| LOAD_CONST BINARY_SUBSCR | 83,800 | 0.1% | 96.4% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 83,700 | 0.1% | 96.5% |
| LOAD_CONST COMPARE_OP_STR | 81,120 | 0.0% | 96.5% |
| LOAD_GLOBAL_MODULE BINARY_OP | 80,660 | 0.0% | 96.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 80,420 | 0.0% | 96.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,580 | 93.1% |
| LOAD_FAST | 300 | 6.1% |
| BINARY_OP_ADD_INT | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,980 | 80.9% |
| LOAD_FAST | 340 | 6.9% |
| LOAD_CONST | 180 | 3.7% |
| CALL_PY_EXACT_ARGS | 180 | 3.7% |
| BUILD_TUPLE | 120 | 2.4% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 400 | 90.9% |
| LOAD_CONST | 40 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 280 | 63.6% |
| JUMP_BACKWARD | 120 | 27.3% |
| LOAD_FAST | 40 | 9.1% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 316,780 | 99.8% |
| COPY_FREE_VARS | 240 | 0.1% |
| RESUME | 200 | 0.1% |
| POP_TOP | 140 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 280 | 41.2% |
| RETURN_VALUE | 180 | 26.5% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 23.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 600 | 88.2% |
| STORE_FAST | 80 | 11.8% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 3,780 | 77.8% |
| BINARY_OP | 1,080 | 22.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,860 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 83,800 | 90.0% |
| BUILD_SLICE | 7,220 | 7.8% |
| LOAD_FAST | 2,000 | 2.1% |
| BINARY_SUBSCR | 40 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 41,080 | 44.1% |
| LOAD_ATTR | 21,480 | 23.1% |
| CALL | 16,180 | 17.4% |
| GET_ITER | 7,040 | 7.6% |
| LOAD_GLOBAL | 2,880 | 3.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 5,840 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,840 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 70.0% |
| LOAD_CONST | 60 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 40.0% |
| JUMP_BACKWARD | 60 | 30.0% |
| RETURN_CONST | 60 | 30.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 7,820 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,820 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,240 | 69.5% |
| LOAD_FAST | 1,320 | 28.3% |
| LOAD_ATTR | 80 | 1.7% |
| STORE_FAST_LOAD_FAST | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,600 | 98.7% |
| BUILD_STRING | 60 | 1.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 40,060 | 44.5% |
| LOAD_FAST | 18,820 | 20.9% |
| LOAD_ATTR_INSTANCE_VALUE | 15,300 | 17.0% |
| BINARY_SUBSCR | 7,040 | 7.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,820 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 35,860 | 39.9% |
| EXTENDED_ARG | 32,000 | 35.6% |
| FOR_ITER_LIST | 11,900 | 13.2% |
| FOR_ITER | 7,600 | 8.4% |
| LOAD_FAST_AND_CLEAR | 1,340 | 1.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 296,140 | 95.4% |
| RETURN_CONST | 14,020 | 4.5% |
| YIELD_VALUE | 220 | 0.1% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 40 | 66.7% |
| DELETE_NAME | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 460 | 40.4% |
| STORE_NAME | 460 | 40.4% |
| CALL_BUILTIN_FAST | 80 | 7.0% |
| LOAD_CONST | 60 | 5.3% |
| CALL | 40 | 3.5% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,494,640 | 83.9% |
| STORE_FAST | 273,900 | 15.4% |
| RESUME_CHECK | 3,600 | 0.2% |
| NOP | 1,820 | 0.1% |
| STORE_FAST_STORE_FAST | 1,760 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,727,820 | 97.0% |
| LOAD_FAST | 42,060 | 2.4% |
| LOAD_FAST_LOAD_FAST | 3,940 | 0.2% |
| LOAD_CONST | 2,440 | 0.1% |
| NOP | 1,820 | 0.1% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,820 | 48.3% |
| STORE_ATTR_INSTANCE_VALUE | 2,820 | 48.3% |
| STORE_FAST | 200 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 2,820 | 48.3% |
| RETURN_CONST | 2,820 | 48.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 160 | 2.7% |
| EXTENDED_ARG | 40 | 0.7% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 13,929,940 | 83.1% |
| RETURN_VALUE | 1,752,760 | 10.5% |
| CALL_KW | 748,800 | 4.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 118,460 | 0.7% |
| CALL_BUILTIN_O | 112,840 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,828,080 | 52.7% |
| LOAD_GLOBAL_MODULE | 7,666,420 | 45.7% |
| LOAD_FAST | 105,960 | 0.6% |
| LOAD_GLOBAL | 46,620 | 0.3% |
| JUMP_BACKWARD | 42,420 | 0.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 2,980 | 51.0% |
| BINARY_SUBSCR_STR_INT | 2,820 | 48.3% |
| STORE_SUBSCR | 40 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 5,840 | 100.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,259,180 | 85.0% |
| LOAD_FAST | 207,260 | 14.0% |
| STORE_FAST_LOAD_FAST | 9,460 | 0.6% |
| LOAD_ATTR | 3,100 | 0.2% |
| LOAD_NAME | 1,060 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,277,100 | 86.3% |
| LOAD_FAST | 128,520 | 8.7% |
| LOAD_GLOBAL_MODULE | 51,580 | 3.5% |
| LOAD_FAST_LOAD_FAST | 11,860 | 0.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 8,940 | 0.6% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 120 | 85.7% |
| CALL_PY_EXACT_ARGS | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 120 | 85.7% |
| CALL_METHOD_DESCRIPTOR_O | 20 | 14.3% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,743,960 | 41.9% |
| BINARY_SUBSCR_DICT | 1,721,500 | 41.4% |
| LOAD_ATTR_INSTANCE_VALUE | 266,640 | 6.4% |
| RETURN_VALUE | 260,720 | 6.3% |
| BINARY_SUBSCR_LIST_INT | 61,460 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,752,760 | 42.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,722,500 | 41.4% |
| INTERPRETER_EXIT | 296,140 | 7.1% |
| RETURN_VALUE | 260,720 | 6.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 43,520 | 1.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,300 | 35.4% |
| LOAD_FAST_LOAD_FAST | 1,960 | 30.2% |
| LOAD_CONST | 1,880 | 28.9% |
| BINARY_OP | 160 | 2.5% |
| STORE_SUBSCR | 120 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,280 | 35.1% |
| EXTENDED_ARG | 1,880 | 28.9% |
| JUMP_FORWARD | 1,440 | 22.2% |
| ENTER_EXECUTOR | 260 | 4.0% |
| LOAD_FAST_LOAD_FAST | 180 | 2.8% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 762,220 | 99.1% |
| BINARY_OP | 2,920 | 0.4% |
| LOAD_ATTR | 1,740 | 0.2% |
| ENTER_EXECUTOR | 880 | 0.1% |
| TO_BOOL | 800 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 762,240 | 99.1% |
| POP_JUMP_IF_TRUE | 5,700 | 0.7% |
| TO_BOOL | 800 | 0.1% |
| TO_BOOL_BOOL | 140 | 0.0% |
| TO_BOOL_INT | 60 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,960 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 180 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 4,880 | 56.0% |
| TO_BOOL_LIST | 3,840 | 44.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 4,880 | 56.0% |
| CALL_PY_EXACT_ARGS | 3,840 | 44.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80,660 | 77.0% |
| LOAD_FAST_LOAD_FAST | 7,540 | 7.2% |
| LOAD_FAST | 4,540 | 4.3% |
| RETURN_VALUE | 3,000 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 2,820 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 70,280 | 67.1% |
| STORE_FAST | 14,180 | 13.5% |
| LOAD_FAST | 4,880 | 4.7% |
| TO_BOOL | 2,920 | 2.8% |
| LOAD_CONST | 2,900 | 2.8% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 100 | 55.6% |
| RETURN_VALUE | 60 | 33.3% |
| DICT_UPDATE | 20 | 11.1% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,720 | 23.2% |
| POP_JUMP_IF_NOT_NONE | 8,000 | 19.1% |
| STORE_FAST | 7,940 | 18.9% |
| LOAD_CONST | 7,140 | 17.0% |
| POP_JUMP_IF_FALSE | 3,340 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 32,560 | 77.7% |
| LOAD_FAST | 5,940 | 14.2% |
| LOAD_GLOBAL_BUILTIN | 1,500 | 3.6% |
| SWAP | 1,320 | 3.1% |
| CALL_METHOD_DESCRIPTOR_O | 180 | 0.4% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 5,640 | 91.9% |
| LOAD_FAST | 160 | 2.6% |
| LOAD_CONST | 80 | 1.3% |
| CALL_INTRINSIC_1 | 60 | 1.0% |
| STORE_FAST | 40 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,860 | 95.4% |
| LOAD_GLOBAL_BUILTIN | 80 | 1.3% |
| LOAD_CONST | 60 | 1.0% |
| STORE_FAST | 60 | 1.0% |
| STORE_NAME | 40 | 0.7% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 60 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 7,220 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,220 | 95.3% |
| FORMAT_SIMPLE | 60 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,120 | 87.5% |
| LOAD_FAST | 80 | 6.2% |
| LOAD_CONST | 40 | 3.1% |
| YIELD_VALUE | 20 | 1.6% |
| CALL_BUILTIN_O | 20 | 1.6% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,729,040 | 96.7% |
| CALL_BUILTIN_O | 23,880 | 1.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 9,380 | 0.5% |
| LOAD_FAST | 7,620 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 5,680 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 1,722,600 | 96.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 25,260 | 1.4% |
| LOAD_FAST | 11,280 | 0.6% |
| RETURN_VALUE | 6,820 | 0.4% |
| CALL_ISINSTANCE | 5,700 | 0.3% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,467,180 | 51.0% |
| LOAD_CONST | 3,228,940 | 19.5% |
| BINARY_SUBSCR_LIST_INT | 2,996,320 | 18.1% |
| LOAD_FAST | 1,734,000 | 10.5% |
| CALL | 137,900 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 13,929,940 | 84.0% |
| RETURN_VALUE | 1,743,960 | 10.5% |
| RESUME_CHECK | 752,300 | 4.5% |
| CALL | 137,900 | 0.8% |
| STORE_FAST | 14,200 | 0.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 480 | 46.2% |
| DICT_MERGE | 300 | 28.8% |
| LOAD_FAST | 140 | 13.5% |
| CALL_INTRINSIC_1 | 80 | 7.7% |
| RETURN_VALUE | 20 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 480 | 46.2% |
| RESUME_CHECK | 200 | 19.2% |
| RETURN_VALUE | 160 | 15.4% |
| COPY_FREE_VARS | 80 | 7.7% |
| STORE_FAST | 80 | 7.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 140 | 87.5% |
| IMPORT_NAME | 20 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 80 | 50.0% |
| BUILD_MAP | 60 | 37.5% |
| POP_TOP | 20 | 12.5% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 749,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 748,800 | 99.9% |
| RESUME_CHECK | 680 | 0.1% |
| STORE_FAST | 80 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,960 | 77.9% |
| LOAD_FAST | 1,140 | 11.2% |
| LOAD_CONST | 300 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 260 | 2.5% |
| COMPARE_OP | 180 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,440 | 82.6% |
| POP_JUMP_IF_TRUE | 1,340 | 13.1% |
| COMPARE_OP | 180 | 1.8% |
| COMPARE_OP_STR | 160 | 1.6% |
| COMPARE_OP_INT | 60 | 0.6% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 72,000 | 64.6% |
| LOAD_FAST_LOAD_FAST | 30,980 | 27.8% |
| LOAD_CONST | 7,660 | 6.9% |
| LOAD_FAST | 580 | 0.5% |
| LOAD_ATTR_MODULE | 200 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 83,700 | 75.1% |
| EXTENDED_ARG | 25,080 | 22.5% |
| RETURN_VALUE | 1,740 | 1.6% |
| POP_JUMP_IF_TRUE | 920 | 0.8% |
| STORE_FAST | 80 | 0.1% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 9,740 | 32.9% |
| LOAD_CONST | 9,400 | 31.8% |
| UNARY_NOT | 4,880 | 16.5% |
| LOAD_FAST | 2,280 | 7.7% |
| BINARY_OP | 2,040 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 9,760 | 33.0% |
| STORE_FAST_STORE_FAST | 9,380 | 31.7% |
| TO_BOOL_BOOL | 4,980 | 16.8% |
| TO_BOOL_INT | 4,080 | 13.8% |
| COMPARE_OP_INT | 1,060 | 3.6% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 240 | 40.0% |
| CALL | 140 | 23.3% |
| CALL_PY_EXACT_ARGS | 120 | 20.0% |
| CALL_FUNCTION_EX | 80 | 13.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 20 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 420 | 70.0% |
| RETURN_GENERATOR | 120 | 20.0% |
| RESUME | 60 | 10.0% |


</details>

### DELETE_NAME

<details>
<summary> Successors and predecessors for DELETE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 40 | 50.0% |
| DELETE_NAME | 20 | 25.0% |
| STORE_NAME | 20 | 25.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_BUILD_CLASS | 20 | 25.0% |
| DELETE_NAME | 20 | 25.0% |
| LOAD_CONST | 20 | 25.0% |
| LOAD_NAME | 20 | 25.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220 | 73.3% |
| CALL | 80 | 26.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 300 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_CONST_KEY_MAP | 20 | 50.0% |
| MAP_ADD | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 20 | 50.0% |
| STORE_NAME | 20 | 50.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,828,080 | 98.8% |
| JUMP_FORWARD | 32,460 | 0.4% |
| POP_JUMP_IF_TRUE | 29,980 | 0.3% |
| STORE_FAST | 27,580 | 0.3% |
| STORE_SUBSCR_LIST_INT | 5,700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 8,467,180 | 94.8% |
| CALL_PY_WITH_DEFAULTS | 285,760 | 3.2% |
| LOAD_FAST | 47,440 | 0.5% |
| EXTENDED_ARG | 41,380 | 0.5% |
| FOR_ITER_RANGE | 36,740 | 0.4% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 41,380 | 26.6% |
| GET_ITER | 32,000 | 20.6% |
| POP_TOP | 31,860 | 20.5% |
| CONTAINS_OP | 25,080 | 16.1% |
| COMPARE_OP_STR | 10,440 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 39,020 | 25.1% |
| JUMP_FORWARD | 37,560 | 24.2% |
| FOR_ITER_RANGE | 27,420 | 17.6% |
| FOR_ITER | 22,820 | 14.7% |
| FOR_ITER_LIST | 22,100 | 14.2% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 22,820 | 67.0% |
| GET_ITER | 7,600 | 22.3% |
| JUMP_BACKWARD | 3,000 | 8.8% |
| FOR_ITER | 460 | 1.4% |
| LOAD_FAST | 120 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 17,960 | 52.8% |
| RETURN_CONST | 4,640 | 13.6% |
| LOAD_FAST | 2,820 | 8.3% |
| LOAD_GLOBAL_MODULE | 2,820 | 8.3% |
| STORE_FAST | 2,740 | 8.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 80 | 80.0% |
| STORE_NAME | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 100 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 750,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 749,920 | 100.0% |
| STORE_NAME | 180 | 0.0% |
| IMPORT_FROM | 80 | 0.0% |
| CALL_INTRINSIC_1 | 20 | 0.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 864,440 | 99.6% |
| LOAD_FAST | 1,800 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 1,740 | 0.2% |
| LOAD_CONST | 100 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 836,460 | 96.4% |
| POP_JUMP_IF_TRUE | 31,580 | 3.6% |
| COPY | 100 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 42,420 | 72.7% |
| EXTENDED_ARG | 6,540 | 11.2% |
| STORE_SUBSCR_LIST_INT | 3,160 | 5.4% |
| STORE_FAST | 3,080 | 5.3% |
| FOR_ITER | 480 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 39,140 | 67.1% |
| FOR_ITER_LIST | 6,880 | 11.8% |
| EXTENDED_ARG | 5,920 | 10.1% |
| FOR_ITER | 3,000 | 5.1% |
| ENTER_EXECUTOR | 1,780 | 3.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 37,560 | 47.6% |
| POP_TOP | 13,360 | 16.9% |
| STORE_FAST | 13,180 | 16.7% |
| POP_JUMP_IF_FALSE | 5,060 | 6.4% |
| POP_JUMP_IF_TRUE | 4,900 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 32,460 | 41.1% |
| LOAD_FAST | 20,460 | 25.9% |
| LOAD_GLOBAL_BUILTIN | 16,360 | 20.7% |
| LOAD_GLOBAL_MODULE | 4,780 | 6.1% |
| LOAD_FAST_LOAD_FAST | 3,900 | 4.9% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 660 | 47.1% |
| BUILD_TUPLE | 560 | 40.0% |
| CALL_BUILTIN_CLASS | 180 | 12.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,060 | 75.7% |
| JUMP_BACKWARD | 340 | 24.3% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 46.2% |
| LOAD_DEREF | 80 | 30.8% |
| LOAD_FAST | 60 | 23.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 140 | 53.8% |
| STORE_FAST | 60 | 23.1% |
| STORE_NAME | 40 | 15.4% |
| BINARY_OP | 20 | 7.7% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 295,400 | 84.6% |
| BINARY_SUBSCR | 21,480 | 6.1% |
| BINARY_SUBSCR_LIST_INT | 21,460 | 6.1% |
| LOAD_GLOBAL | 3,780 | 1.1% |
| LOAD_GLOBAL_MODULE | 3,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 287,580 | 82.3% |
| LOAD_ATTR_METHOD_NO_DICT | 21,720 | 6.2% |
| LOAD_CONST | 19,240 | 5.5% |
| LOAD_FAST | 5,040 | 1.4% |
| LOAD_ATTR_MODULE | 3,760 | 1.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,009,380 | 40.6% |
| LOAD_ATTR_METHOD_NO_DICT | 5,301,640 | 21.5% |
| LOAD_CONST | 5,008,500 | 20.3% |
| PUSH_NULL | 1,277,100 | 5.2% |
| LOAD_GLOBAL_BUILTIN | 790,220 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 9,972,300 | 40.4% |
| LOAD_CONST | 5,008,500 | 20.3% |
| LOAD_GLOBAL_MODULE | 3,452,360 | 14.0% |
| CALL | 3,228,940 | 13.1% |
| LOAD_GLOBAL_BUILTIN | 750,260 | 3.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 260 | 18.8% |
| POP_JUMP_IF_FALSE | 240 | 17.4% |
| STORE_FAST | 160 | 11.6% |
| NOP | 140 | 10.1% |
| RESUME_CHECK | 140 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 360 | 26.1% |
| LOAD_FAST | 300 | 21.7% |
| LOAD_CONST | 180 | 13.0% |
| LOAD_ATTR_METHOD_NO_DICT | 140 | 10.1% |
| LIST_EXTEND | 80 | 5.8% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,617,120 | 29.4% |
| POP_JUMP_IF_FALSE | 2,169,320 | 17.6% |
| RESUME_CHECK | 1,367,820 | 11.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,017,680 | 8.3% |
| STORE_FAST | 1,002,000 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,756,600 | 22.4% |
| CALL | 1,734,000 | 14.1% |
| CALL_TYPE_1 | 1,727,160 | 14.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,042,940 | 8.5% |
| TO_BOOL_LIST | 762,320 | 6.2% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,340 | 98.5% |
| LOAD_FAST_AND_CLEAR | 20 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,340 | 98.5% |
| LOAD_FAST_AND_CLEAR | 20 | 1.5% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 1,320 | 81.5% |
| POP_TOP | 300 | 18.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,320 | 81.5% |
| POP_JUMP_IF_NOT_NONE | 280 | 17.3% |
| TO_BOOL | 20 | 1.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,750,620 | 39.7% |
| CALL_TYPE_1 | 1,725,420 | 39.1% |
| LOAD_ATTR_METHOD_NO_DICT | 751,220 | 17.0% |
| RESUME_CHECK | 32,500 | 0.7% |
| STORE_ATTR_INSTANCE_VALUE | 30,380 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,729,120 | 39.2% |
| BUILD_TUPLE | 1,729,040 | 39.2% |
| LOAD_FAST | 769,540 | 17.4% |
| STORE_ATTR_INSTANCE_VALUE | 57,180 | 1.3% |
| CONTAINS_OP | 30,980 | 0.7% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 46,620 | 49.5% |
| LOAD_CONST | 30,220 | 32.1% |
| BINARY_SUBSCR | 2,880 | 3.1% |
| BINARY_SUBSCR_LIST_INT | 2,880 | 3.1% |
| STORE_FAST | 2,720 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 45,520 | 48.3% |
| LOAD_CONST | 42,320 | 44.9% |
| LOAD_ATTR | 3,780 | 4.0% |
| LOAD_GLOBAL_BUILTIN | 1,400 | 1.5% |
| LOAD_FAST | 380 | 0.4% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 3,320 | 28.4% |
| STORE_NAME | 2,380 | 20.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,120 | 9.6% |
| STORE_SUBSCR_DICT | 960 | 8.2% |
| LOAD_CONST | 860 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 3,320 | 28.4% |
| LOAD_CONST | 3,260 | 27.9% |
| CALL_METHOD_DESCRIPTOR_O | 1,080 | 9.2% |
| LOAD_ATTR_METHOD_NO_DICT | 1,080 | 9.2% |
| PUSH_NULL | 1,060 | 9.1% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 220 | 55.0% |
| CALL_PY_EXACT_ARGS | 120 | 30.0% |
| CALL | 60 | 15.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 220 | 55.0% |
| RESUME_CHECK | 160 | 40.0% |
| RESUME | 20 | 5.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,360 | 66.7% |
| LOAD_NAME | 680 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,020 | 50.0% |
| LOAD_CONST | 640 | 31.4% |
| JUMP_BACKWARD | 340 | 16.7% |
| BUILD_MAP | 20 | 1.0% |
| DICT_UPDATE | 20 | 1.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,812,240 | 40.1% |
| IS_OP | 836,460 | 18.5% |
| TO_BOOL | 762,240 | 16.9% |
| TO_BOOL_LIST | 755,700 | 16.7% |
| COMPARE_OP_STR | 87,600 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,169,320 | 48.0% |
| NOP | 1,494,640 | 33.1% |
| LOAD_CONST | 754,280 | 16.7% |
| LOAD_GLOBAL_MODULE | 34,160 | 0.8% |
| LOAD_FAST_LOAD_FAST | 14,680 | 0.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 270,560 | 97.1% |
| LOAD_FAST | 7,980 | 2.9% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| RETURN_VALUE | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 266,780 | 95.7% |
| LOAD_CONST | 9,460 | 3.4% |
| ENTER_EXECUTOR | 1,500 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 580 | 0.2% |
| LOAD_GLOBAL_MODULE | 360 | 0.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 288,340 | 99.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,420 | 0.5% |
| CALL_BUILTIN_FAST | 440 | 0.2% |
| LOAD_FAST_CHECK | 280 | 0.1% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 267,680 | 92.1% |
| BUILD_LIST | 8,000 | 2.8% |
| LOAD_GLOBAL_MODULE | 5,540 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 4,160 | 1.4% |
| LOAD_FAST_LOAD_FAST | 1,880 | 0.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 32,480 | 28.7% |
| IS_OP | 31,580 | 27.9% |
| TO_BOOL_BOOL | 26,200 | 23.1% |
| TO_BOOL_STR | 10,440 | 9.2% |
| TO_BOOL | 5,700 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 47,380 | 41.9% |
| ENTER_EXECUTOR | 29,980 | 26.5% |
| CALL_LEN | 9,620 | 8.5% |
| LOAD_FAST_LOAD_FAST | 6,700 | 5.9% |
| LOAD_GLOBAL_MODULE | 5,400 | 4.8% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 32,180 | 27.0% |
| CALL_LIST_APPEND | 29,680 | 24.9% |
| POP_TOP | 13,920 | 11.7% |
| POP_JUMP_IF_FALSE | 13,220 | 11.1% |
| FOR_ITER_RANGE | 7,680 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 75,580 | 63.4% |
| TO_BOOL_BOOL | 16,380 | 13.7% |
| INTERPRETER_EXIT | 14,020 | 11.8% |
| EXIT_INIT_CHECK | 7,820 | 6.6% |
| STORE_FAST | 5,340 | 4.5% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 460 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 43.5% |
| LOAD_GLOBAL_MODULE | 120 | 26.1% |
| STORE_NAME | 100 | 21.7% |
| CALL | 20 | 4.3% |
| LOAD_FAST | 20 | 4.3% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 460 | 54.8% |
| LOAD_FAST | 340 | 40.5% |
| SWAP | 40 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 42.9% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 21.4% |
| LOAD_FAST_LOAD_FAST | 120 | 14.3% |
| NOP | 80 | 9.5% |
| RETURN_CONST | 40 | 4.8% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 80 | 28.6% |
| LOAD_ATTR | 40 | 14.3% |
| LOAD_CONST | 20 | 7.1% |
| STORE_FAST | 20 | 7.1% |
| BINARY_OP_ADD_UNICODE | 20 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_DEREF | 80 | 28.6% |
| LOAD_GLOBAL_BUILTIN | 80 | 28.6% |
| LOAD_CONST | 60 | 21.4% |
| LOAD_DEREF | 20 | 7.1% |
| LOAD_GLOBAL | 20 | 7.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 749,920 | 46.1% |
| LOAD_ATTR | 287,580 | 17.7% |
| FOR_ITER_RANGE | 91,860 | 5.7% |
| LOAD_CONST | 55,820 | 3.4% |
| BINARY_OP_ADD_INT | 53,360 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,002,000 | 61.7% |
| NOP | 273,900 | 16.9% |
| LOAD_GLOBAL_MODULE | 142,620 | 8.8% |
| LOAD_CONST | 55,260 | 3.4% |
| STORE_FAST | 43,480 | 2.7% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 9,460 | 88.4% |
| FOR_ITER_TUPLE | 1,220 | 11.4% |
| FOR_ITER | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 9,460 | 88.4% |
| TO_BOOL_STR | 660 | 6.2% |
| LOAD_FAST | 560 | 5.2% |
| FORMAT_SIMPLE | 20 | 0.2% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_EX | 748,800 | 92.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 48,840 | 6.0% |
| COPY | 9,380 | 1.2% |
| UNPACK_SEQUENCE_TUPLE | 3,520 | 0.4% |
| STORE_FAST_STORE_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 780,400 | 96.2% |
| LOAD_FAST_LOAD_FAST | 21,300 | 2.6% |
| STORE_FAST | 3,160 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 3,080 | 0.4% |
| NOP | 1,760 | 0.2% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,780 | 34.4% |
| FOR_ITER_TUPLE | 1,120 | 21.6% |
| FOR_ITER | 720 | 13.9% |
| MAKE_FUNCTION | 460 | 8.9% |
| RETURN_VALUE | 300 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,460 | 47.5% |
| LOAD_NAME | 2,380 | 45.9% |
| RETURN_CONST | 100 | 1.9% |
| POP_TOP | 80 | 1.5% |
| LOAD_BUILD_CLASS | 40 | 0.8% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 1,340 | 23.6% |
| BUILD_LIST | 1,320 | 23.2% |
| LOAD_FAST | 1,240 | 21.8% |
| FOR_ITER_TUPLE | 1,140 | 20.1% |
| BINARY_OP | 200 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,360 | 23.9% |
| BUILD_LIST | 1,320 | 23.2% |
| FOR_ITER_TUPLE | 1,120 | 19.7% |
| COPY | 1,100 | 19.4% |
| POP_TOP | 200 | 3.5% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 748,800 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 748,800 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 40 | 66.7% |
| RETURN_VALUE | 20 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 40 | 66.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 20 | 33.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 120 | 54.5% |
| ENTER_EXECUTOR | 80 | 36.4% |
| BUILD_STRING | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 220 | 100.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 480 | 60.0% |
| CACHE | 200 | 25.0% |
| COPY_FREE_VARS | 60 | 7.5% |
| CALL_FUNCTION_EX | 40 | 5.0% |
| MAKE_CELL | 20 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL | 360 | 45.0% |
| LOAD_CONST | 120 | 15.0% |
| NOP | 100 | 12.5% |
| LOAD_FAST | 100 | 12.5% |
| LOAD_NAME | 60 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 74,100 | 91.1% |
| LOAD_FAST_LOAD_FAST | 5,080 | 6.2% |
| BINARY_OP_MULTIPLY_INT | 2,140 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,360 | 65.6% |
| LOAD_FAST | 22,680 | 27.9% |
| CALL_PY_EXACT_ARGS | 2,060 | 2.5% |
| CALL_BUILTIN_O | 1,600 | 2.0% |
| LOAD_FAST_LOAD_FAST | 740 | 0.9% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,080 | 70.3% |
| LOAD_FAST_LOAD_FAST | 600 | 13.7% |
| CALL_METHOD_DESCRIPTOR_O | 360 | 8.2% |
| BINARY_OP | 220 | 5.0% |
| BINARY_SUBSCR_LIST_INT | 120 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 1,200 | 27.4% |
| BUILD_TUPLE | 800 | 18.3% |
| LOAD_NAME | 800 | 18.3% |
| LOAD_FAST | 540 | 12.3% |
| RETURN_VALUE | 380 | 8.7% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,200 | 59.5% |
| BINARY_SUBSCR_TUPLE_INT | 2,140 | 39.8% |
| LOAD_ATTR | 40 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 2,140 | 39.8% |
| LOAD_CONST | 1,600 | 29.7% |
| CALL_BUILTIN_O | 1,600 | 29.7% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.7% |


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
| LOAD_CONST | 11,660 | 36.0% |
| LOAD_FAST | 11,020 | 34.0% |
| CALL_LEN | 9,680 | 29.9% |
| BINARY_OP | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 9,680 | 29.9% |
| LOAD_FAST_LOAD_FAST | 9,460 | 29.2% |
| LOAD_FAST | 3,940 | 12.2% |
| LOAD_CONST | 3,640 | 11.2% |
| STORE_FAST | 2,920 | 9.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,722,600 | 99.3% |
| LOAD_FAST | 9,140 | 0.5% |
| LOAD_FAST_LOAD_FAST | 2,280 | 0.1% |
| LOAD_CONST | 120 | 0.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,721,500 | 99.3% |
| CALL_BUILTIN_O | 4,920 | 0.3% |
| LOAD_CONST | 3,080 | 0.2% |
| PUSH_EXC_INFO | 2,980 | 0.2% |
| STORE_FAST | 1,300 | 0.1% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 22,360 | 55.8% |
| LOAD_CONST | 10,720 | 26.7% |
| LOAD_FAST | 7,000 | 17.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 40,080 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 9,972,300 | 98.9% |
| LOAD_FAST | 63,440 | 0.6% |
| BINARY_SUBSCR | 41,080 | 0.4% |
| LOAD_FAST_LOAD_FAST | 2,840 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 2,480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,737,980 | 57.0% |
| CALL | 2,996,320 | 29.7% |
| LOAD_GLOBAL_MODULE | 540,740 | 5.4% |
| CALL_PY_WITH_DEFAULTS | 363,200 | 3.6% |
| LOAD_CONST | 294,260 | 2.9% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,580 | 59.7% |
| LOAD_FAST | 20,960 | 37.3% |
| ENTER_EXECUTOR | 1,640 | 2.9% |
| BINARY_SUBSCR_STR_INT | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 31,640 | 56.3% |
| STORE_FAST | 16,000 | 28.4% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,780 | 6.7% |
| PUSH_EXC_INFO | 2,820 | 5.0% |
| CALL_BUILTIN_O | 1,940 | 3.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 28,700 | 99.9% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,460 | 32.9% |
| CALL_BUILTIN_O | 6,260 | 21.8% |
| GET_ITER | 2,460 | 8.6% |
| LOAD_FAST | 2,220 | 7.7% |
| BINARY_OP_MULTIPLY_INT | 2,140 | 7.5% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980 | 38.1% |
| LOAD_GLOBAL_MODULE | 2,820 | 36.1% |
| BINARY_SUBSCR | 1,880 | 24.0% |
| LOAD_FAST_LOAD_FAST | 140 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,820 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 25,260 | 47.5% |
| LOAD_CONST | 15,180 | 28.6% |
| PUSH_NULL | 8,940 | 16.8% |
| LOAD_FAST | 3,740 | 7.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 52,860 | 99.4% |
| POP_TOP | 280 | 0.5% |
| COPY_FREE_VARS | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 37,140 | 76.6% |
| CALL_LEN | 8,540 | 17.6% |
| CALL | 1,280 | 2.6% |
| CALL_BUILTIN_FAST | 680 | 1.4% |
| BINARY_OP_ADD_INT | 320 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40,060 | 82.6% |
| LOAD_CONST | 7,040 | 14.5% |
| RETURN_VALUE | 680 | 1.4% |
| STORE_FAST | 420 | 0.9% |
| LIST_APPEND | 180 | 0.4% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,040 | 52.0% |
| LOAD_CONST | 620 | 31.0% |
| LOAD_FAST_LOAD_FAST | 120 | 6.0% |
| MAKE_FUNCTION | 80 | 4.0% |
| LOAD_ATTR_SLOT | 80 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 680 | 34.0% |
| POP_JUMP_IF_NOT_NONE | 440 | 22.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 17.0% |
| TO_BOOL_BOOL | 180 | 9.0% |
| POP_TOP | 160 | 8.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 18,760 | 65.7% |
| LOAD_FAST_LOAD_FAST | 6,160 | 21.6% |
| CALL_TUPLE_1 | 2,820 | 9.9% |
| LOAD_FAST | 420 | 1.5% |
| LOAD_CONST | 200 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 9,380 | 32.9% |
| LOAD_GLOBAL_BUILTIN | 9,380 | 32.9% |
| STORE_FAST | 6,520 | 22.8% |
| RETURN_VALUE | 3,180 | 11.1% |
| BEFORE_WITH | 60 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 91,580 | 61.2% |
| LOAD_GLOBAL_MODULE | 16,240 | 10.9% |
| LOAD_CONST | 12,620 | 8.4% |
| RETURN_VALUE | 7,040 | 4.7% |
| BINARY_SUBSCR_TUPLE_INT | 6,260 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 112,840 | 75.4% |
| BUILD_TUPLE | 23,880 | 16.0% |
| TO_BOOL_BOOL | 8,880 | 5.9% |
| STORE_FAST | 3,900 | 2.6% |
| TO_BOOL_INT | 80 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,715,560 | 95.5% |
| LOAD_GLOBAL_BUILTIN | 71,980 | 4.0% |
| BUILD_TUPLE | 5,700 | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,720 | 0.1% |
| LOAD_ATTR_SLOT | 1,720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,788,700 | 99.5% |
| RETURN_VALUE | 5,640 | 0.3% |
| LOAD_FAST | 2,820 | 0.2% |
| TO_BOOL | 40 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,360 | 55.9% |
| LOAD_ATTR_INSTANCE_VALUE | 26,640 | 27.9% |
| POP_JUMP_IF_TRUE | 9,620 | 10.1% |
| LOAD_GLOBAL_MODULE | 5,640 | 5.9% |
| LOAD_CONST | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 26,400 | 27.7% |
| LOAD_CONST | 13,280 | 13.9% |
| LOAD_FAST | 10,440 | 10.9% |
| BINARY_OP_SUBTRACT_INT | 9,680 | 10.1% |
| STORE_FAST_LOAD_FAST | 9,460 | 9.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,600 | 79.3% |
| BUILD_TUPLE | 2,880 | 7.7% |
| LOAD_GLOBAL_MODULE | 2,820 | 7.6% |
| LOAD_CONST | 1,680 | 4.5% |
| ENTER_EXECUTOR | 260 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 29,680 | 79.5% |
| LOAD_FAST | 4,420 | 11.8% |
| ENTER_EXECUTOR | 1,640 | 4.4% |
| NOP | 1,320 | 3.5% |
| LOAD_FAST_LOAD_FAST | 180 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,000 | 49.0% |
| LOAD_CONST | 2,820 | 23.0% |
| LOAD_FAST_LOAD_FAST | 1,260 | 10.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,140 | 9.3% |
| LOAD_GLOBAL_MODULE | 820 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,320 | 92.5% |
| LIST_APPEND | 660 | 5.4% |
| POP_TOP | 120 | 1.0% |
| LOAD_FAST | 80 | 0.7% |
| SWAP | 60 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 66,880 | 56.3% |
| BINARY_SUBSCR_LIST_INT | 50,960 | 42.9% |
| CALL | 700 | 0.6% |
| LOAD_GLOBAL_MODULE | 180 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 118,460 | 99.8% |
| LOAD_CONST | 180 | 0.2% |
| STORE_FAST | 60 | 0.1% |
| STORE_DEREF | 20 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,400 | 99.4% |
| CALL | 20 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,820 | 82.5% |
| BUILD_TUPLE | 540 | 15.8% |
| RETURN_VALUE | 40 | 1.2% |
| TO_BOOL_BOOL | 20 | 0.6% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,180 | 42.8% |
| RETURN_VALUE | 1,500 | 15.4% |
| LOAD_NAME | 1,080 | 11.1% |
| LOAD_GLOBAL_MODULE | 920 | 9.4% |
| STORE_FAST | 660 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,640 | 68.0% |
| RETURN_VALUE | 1,600 | 16.4% |
| CALL_METHOD_DESCRIPTOR_O | 640 | 6.6% |
| BINARY_OP_ADD_UNICODE | 360 | 3.7% |
| LOAD_CONST | 220 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,729,120 | 74.9% |
| LOAD_FAST | 289,240 | 12.5% |
| LOAD_ATTR_MODULE | 224,460 | 9.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 38,000 | 1.6% |
| LOAD_GLOBAL_MODULE | 6,980 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,309,360 | 100.0% |
| COPY_FREE_VARS | 120 | 0.0% |
| MAKE_CELL | 120 | 0.0% |
| RETURN_GENERATOR | 20 | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 363,200 | 48.9% |
| ENTER_EXECUTOR | 285,760 | 38.5% |
| LOAD_CONST | 87,000 | 11.7% |
| LOAD_FAST_LOAD_FAST | 2,900 | 0.4% |
| LOAD_FAST | 2,260 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 743,180 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 60.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 30.0% |
| CALL_BUILTIN_O | 20 | 10.0% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,820 | 97.2% |
| LOAD_GLOBAL_MODULE | 60 | 2.1% |
| CALL_BUILTIN_CLASS | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 2,820 | 97.2% |
| CALL | 60 | 2.1% |
| STORE_DEREF | 20 | 0.7% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,727,160 | 100.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,725,420 | 99.9% |
| LOAD_FAST | 1,720 | 0.1% |
| PUSH_NULL | 60 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 21,260 | 61.1% |
| LOAD_GLOBAL_MODULE | 7,240 | 20.8% |
| CALL_LEN | 2,620 | 7.5% |
| BINARY_SUBSCR_LIST_INT | 1,420 | 4.1% |
| COPY | 1,060 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 34,320 | 98.7% |
| POP_JUMP_IF_TRUE | 340 | 1.0% |
| RETURN_VALUE | 60 | 0.2% |
| STORE_FAST | 60 | 0.2% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 81,120 | 82.7% |
| LOAD_ATTR_INSTANCE_VALUE | 16,720 | 17.0% |
| COMPARE_OP | 160 | 0.2% |
| LOAD_FAST | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 87,600 | 89.3% |
| EXTENDED_ARG | 10,440 | 10.6% |
| COMPARE_OP | 60 | 0.1% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 22,100 | 49.5% |
| GET_ITER | 11,900 | 26.6% |
| JUMP_BACKWARD | 6,880 | 15.4% |
| ENTER_EXECUTOR | 3,760 | 8.4% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 16,300 | 36.5% |
| STORE_FAST | 10,380 | 23.2% |
| LOAD_GLOBAL_BUILTIN | 9,400 | 21.0% |
| LOAD_FAST_LOAD_FAST | 3,020 | 6.8% |
| LOAD_FAST | 2,900 | 6.5% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 39,140 | 27.8% |
| ENTER_EXECUTOR | 36,740 | 26.1% |
| GET_ITER | 35,860 | 25.5% |
| EXTENDED_ARG | 27,420 | 19.5% |
| FOR_ITER | 1,260 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 91,860 | 65.3% |
| LOAD_GLOBAL_BUILTIN | 30,000 | 21.3% |
| LOAD_FAST | 8,540 | 6.1% |
| RETURN_CONST | 7,680 | 5.5% |
| LOAD_GLOBAL | 2,040 | 1.5% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,720 | 33.2% |
| JUMP_BACKWARD | 1,140 | 22.0% |
| GET_ITER | 1,120 | 21.6% |
| SWAP | 1,120 | 21.6% |
| FOR_ITER | 60 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 1,220 | 23.6% |
| SWAP | 1,140 | 22.0% |
| STORE_NAME | 1,120 | 21.6% |
| LOAD_NAME | 500 | 9.7% |
| JUMP_BACKWARD | 420 | 8.1% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,042,940 | 96.0% |
| LOAD_FAST_LOAD_FAST | 29,080 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 14,100 | 1.3% |
| LOAD_ATTR | 240 | 0.0% |
| COPY | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 355,640 | 32.7% |
| POP_JUMP_IF_NONE | 270,560 | 24.9% |
| RETURN_VALUE | 266,640 | 24.5% |
| STORE_FAST | 39,200 | 3.6% |
| LOAD_ATTR_METHOD_NO_DICT | 31,600 | 2.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 5,737,980 | 76.0% |
| RETURN_VALUE | 1,722,500 | 22.8% |
| LOAD_ATTR_INSTANCE_VALUE | 31,600 | 0.4% |
| LOAD_ATTR | 21,720 | 0.3% |
| LOAD_FAST | 19,720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,301,640 | 70.2% |
| LOAD_FAST | 1,017,680 | 13.5% |
| LOAD_FAST_LOAD_FAST | 751,220 | 10.0% |
| LOAD_GLOBAL_MODULE | 468,160 | 6.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,400 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,920 | 91.3% |
| BINARY_SUBSCR_TUPLE_INT | 1,880 | 4.2% |
| BINARY_SUBSCR | 1,600 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 320 | 0.7% |
| LOAD_GLOBAL_MODULE | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 38,000 | 84.8% |
| LOAD_FAST | 3,700 | 8.3% |
| LOAD_CONST | 2,040 | 4.6% |
| LOAD_GLOBAL_MODULE | 940 | 2.1% |
| LOAD_FAST_LOAD_FAST | 120 | 0.3% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,491,960 | 66.4% |
| LOAD_FAST | 749,880 | 33.4% |
| LOAD_ATTR | 3,760 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,259,180 | 56.1% |
| LOAD_CONST | 749,440 | 33.4% |
| CALL_PY_EXACT_ARGS | 224,460 | 10.0% |
| STORE_FAST | 5,900 | 0.3% |
| CALL | 1,960 | 0.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,720 | 50.0% |
| LOAD_FAST_LOAD_FAST | 1,720 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,720 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 1,720 | 50.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,640 | 61.8% |
| LOAD_FAST | 3,480 | 38.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,120 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,020 | 43.3% |
| LOAD_FAST_LOAD_FAST | 1,720 | 36.9% |
| LOAD_ATTR_MODULE | 860 | 18.5% |
| RETURN_VALUE | 60 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,720 | 36.9% |
| CALL_ISINSTANCE | 1,720 | 36.9% |
| LOAD_FAST | 820 | 17.6% |
| LOAD_CONST | 240 | 5.2% |
| CALL_BUILTIN_FAST | 80 | 1.7% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,830,020 | 40.2% |
| LOAD_GLOBAL_MODULE | 1,724,540 | 37.9% |
| LOAD_CONST | 750,260 | 16.5% |
| LOAD_FAST | 80,420 | 1.8% |
| STORE_FAST | 32,660 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,617,120 | 79.6% |
| LOAD_CONST | 790,220 | 17.4% |
| CALL_ISINSTANCE | 71,980 | 1.6% |
| STORE_FAST | 23,480 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 13,700 | 0.3% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,666,420 | 42.8% |
| LOAD_CONST | 3,452,360 | 19.3% |
| LOAD_FAST | 2,756,600 | 15.4% |
| NOP | 1,727,820 | 9.6% |
| RESUME_CHECK | 983,620 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,009,380 | 55.9% |
| LOAD_FAST_LOAD_FAST | 1,750,620 | 9.8% |
| LOAD_GLOBAL_BUILTIN | 1,724,540 | 9.6% |
| CALL_ISINSTANCE | 1,715,560 | 9.6% |
| LOAD_ATTR_MODULE | 1,491,960 | 8.3% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 160 | 100.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,309,360 | 54.6% |
| CALL | 752,300 | 17.8% |
| CALL_PY_WITH_DEFAULTS | 743,180 | 17.6% |
| CACHE | 316,780 | 7.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 52,860 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,830,020 | 43.2% |
| LOAD_FAST | 1,367,820 | 32.3% |
| LOAD_GLOBAL_MODULE | 983,620 | 23.2% |
| LOAD_FAST_LOAD_FAST | 32,500 | 0.8% |
| BUILD_LIST | 9,720 | 0.2% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,180 | 51.9% |
| LOAD_FAST_LOAD_FAST | 57,180 | 45.6% |
| LOAD_ATTR_INSTANCE_VALUE | 2,820 | 2.2% |
| STORE_ATTR | 180 | 0.1% |
| SWAP | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 32,180 | 25.6% |
| LOAD_FAST_LOAD_FAST | 30,380 | 24.2% |
| LOAD_FAST | 29,720 | 23.7% |
| LOAD_CONST | 21,480 | 17.1% |
| BUILD_MAP | 5,640 | 4.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 57.1% |
| LOAD_FAST | 40 | 28.6% |
| LOAD_ATTR_SLOT | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,940 | 80.5% |
| BINARY_OP_ADD_UNICODE | 1,200 | 16.3% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 2.2% |
| STORE_SUBSCR | 80 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,940 | 39.8% |
| LOAD_GLOBAL_BUILTIN | 2,820 | 38.2% |
| LOAD_NAME | 960 | 13.0% |
| JUMP_BACKWARD | 320 | 4.3% |
| LOAD_GLOBAL_MODULE | 160 | 2.2% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 10,980 | 81.2% |
| LOAD_FAST | 2,540 | 18.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,700 | 42.2% |
| RETURN_CONST | 4,360 | 32.2% |
| JUMP_BACKWARD | 3,160 | 23.4% |
| EXTENDED_ARG | 160 | 1.2% |
| LOAD_FAST | 140 | 1.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,788,700 | 97.1% |
| RETURN_CONST | 16,380 | 0.9% |
| LOAD_FAST | 9,100 | 0.5% |
| CALL_BUILTIN_O | 8,880 | 0.5% |
| RETURN_VALUE | 7,680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,812,240 | 98.4% |
| POP_JUMP_IF_TRUE | 26,200 | 1.4% |
| EXTENDED_ARG | 3,460 | 0.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 70,280 | 71.8% |
| LOAD_FAST | 23,260 | 23.8% |
| COPY | 4,080 | 4.2% |
| CALL_BUILTIN_O | 80 | 0.1% |
| CALL_LEN | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 60,480 | 61.8% |
| POP_JUMP_IF_TRUE | 32,480 | 33.2% |
| UNARY_NOT | 4,880 | 5.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 762,320 | 99.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,420 | 0.2% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 755,700 | 98.9% |
| POP_JUMP_IF_TRUE | 4,180 | 0.5% |
| UNARY_NOT | 3,840 | 0.5% |
| TO_BOOL_NONE | 40 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,020 | 96.0% |
| ENTER_EXECUTOR | 420 | 3.4% |
| TO_BOOL | 40 | 0.3% |
| TO_BOOL_LIST | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 12,480 | 99.7% |
| TO_BOOL | 20 | 0.2% |
| POP_JUMP_IF_TRUE | 20 | 0.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 9,760 | 82.7% |
| LOAD_FAST | 1,360 | 11.5% |
| STORE_FAST_LOAD_FAST | 660 | 5.6% |
| TO_BOOL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 10,440 | 88.5% |
| POP_JUMP_IF_FALSE | 1,360 | 11.5% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,860 | 53.8% |
| RETURN_VALUE | 3,040 | 42.3% |
| BINARY_SUBSCR_TUPLE_INT | 140 | 1.9% |
| CALL_METHOD_DESCRIPTOR_O | 120 | 1.7% |
| BUILD_TUPLE | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,640 | 50.7% |
| STORE_FAST_STORE_FAST | 3,520 | 49.0% |
| STORE_DEREF | 20 | 0.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 43,520 | 54.6% |
| FOR_ITER | 17,960 | 22.5% |
| FOR_ITER_LIST | 16,300 | 20.4% |
| BINARY_SUBSCR_LIST_INT | 1,340 | 1.7% |
| CALL_BUILTIN_FAST | 340 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 48,840 | 61.3% |
| STORE_FAST | 30,880 | 38.7% |


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
|     deferred | 103,180 | 36.5% |
|          hit | 178,260 | 63.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 17.7% |
| Failure | 1,300 | 82.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 720 | 55.4% |
| or | 240 | 18.5% |
| and different types | 100 | 7.7% |
| multiply different types | 80 | 6.2% |
| remainder | 80 | 6.2% |
| add other | 60 | 4.6% |
| floor divide | 20 | 1.5% |


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
|     deferred | 61,700 | 0.3% |
|          hit | 21,931,000 | 99.5% |
|         miss | 10,000 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 41,360 | 99.9% |
| Failure | 40 | 0.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 20 | 50.0% |
| list slice | 20 | 50.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,447,440 | 68.4% |
|          hit | 7,446,660 | 31.0% |
|         miss | 1,620 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,520 | 3.2% |
| Failure | 137,860 | 96.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 129,600 | 94.0% |
| code complex parameters | 7,980 | 5.8% |
| meth descr varargs | 100 | 0.1% |
| cfunc noargs | 60 | 0.0% |
| class no vectorcall | 60 | 0.0% |
| wrong number arguments | 40 | 0.0% |
| metaclass | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,600 | 7.3% |
|          hit | 160,100 | 92.5% |
|         miss | 2,840 | 1.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 47.8% |
| Failure | 240 | 52.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 100 | 41.7% |
| other | 60 | 25.0% |
| big int | 60 | 25.0% |
| tuple | 20 | 8.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 32,240 | 14.4% |
|          hit | 190,440 | 84.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,340 | 74.4% |
| Failure | 460 | 25.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| itertools | 160 | 34.8% |
| set | 120 | 26.1% |
| dict items | 80 | 17.4% |
| dict keys | 40 | 8.7% |
| seq iter | 40 | 8.7% |
| map | 20 | 4.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 323,140 | 1.6% |
|          hit | 19,930,160 | 98.3% |
|         miss | 140 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 25,720 | 97.6% |
| Failure | 640 | 2.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 260 | 40.6% |
| metaclass attribute | 160 | 25.0% |
| mutable class | 120 | 18.8% |
| not managed dict | 80 | 12.5% |
| class attr simple | 20 | 3.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 72,300 | 0.3% |
|          hit | 22,440,640 | 99.5% |
|         miss | 25,440 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 47,380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|          hit | 160 | 100.0% |


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
|     deferred | 660 | 0.4% |
|          hit | 168,100 | 99.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,300 | 19.4% |
|          hit | 26,040 | 80.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 40.0% |
| Failure | 120 | 60.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 80 | 66.7% |
| out of range | 20 | 16.7% |
| py simple | 20 | 16.7% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 770,460 | 21.6% |
|          hit | 2,793,220 | 78.4% |
|         miss | 2,580 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 320 | 28.1% |
| Failure | 820 | 71.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 380 | 46.3% |
| other | 220 | 26.8% |
| mapping | 100 | 12.2% |
| dict | 80 | 9.8% |
| number | 40 | 4.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 130,200 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 82,938,780 | 49.9% |
| Not specialized | 23,255,220 | 14.0% |
| Specialized hits | 60,099,180 | 36.1% |
| Specialized misses | 42,620 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 16,447,440 | 92.2% |
| TO_BOOL | 770,460 | 4.3% |
| LOAD_ATTR | 323,140 | 1.8% |
| BINARY_OP | 103,180 | 0.6% |
| LOAD_GLOBAL | 72,300 | 0.4% |
| BINARY_SUBSCR | 61,700 | 0.3% |
| FOR_ITER | 32,240 | 0.2% |
| COMPARE_OP | 12,600 | 0.1% |
| STORE_SUBSCR | 6,300 | 0.0% |
| STORE_ATTR | 660 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 25,000 | 58.7% |
| BINARY_SUBSCR_LIST_INT | 7,120 | 16.7% |
| BINARY_SUBSCR_STR_INT | 2,880 | 6.8% |
| COMPARE_OP_STR | 2,840 | 6.7% |
| TO_BOOL_NONE | 2,280 | 5.3% |
| CALL_BUILTIN_FAST | 700 | 1.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 480 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 440 | 1.0% |
| TO_BOOL_LIST | 240 | 0.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 180 | 0.4% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 317,360 | 7.3% |
| Calls to Python functions inlined | 4,026,760 | 92.7% |
| Calls via PyEval_EvalFrame (total) | 317,360 | 7.3% |
| Calls via PyEval_EvalFrame (vector) | 317,000 | 7.3% |
| Calls via PyEval_EvalFrame (generator) | 360 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 80 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 316,860 | 7.3% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 46,860 | 1.1% |
| Calls via PyEval_EvalFrame (function ex) | 320 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 1,680 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 775,640 | 17.9% |
| Frames pushed | 4,351,580 | 100.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 9,841,620 | 16.4% |
| Frees to freelist | 9,844,580 |  |
| Allocations | 50,292,100 | 83.6% |
| Allocations to 512 bytes | 49,931,260 | 83.0% |
| Allocations to 4 kbytes | 315,000 | 0.5% |
| Allocations over 4 kbytes | 45,840 | 0.1% |
| Frees | 70,360,320 |  |
| New values | 9,480 |  |
| Interpreter increfs | 72,671,580 | 42.3% |
| Interpreter decrefs | 109,005,428 | 52.6% |
| Increfs | 99,284,380 | 57.7% |
| Decrefs | 98,173,355 | 47.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 1,129,355 |  |
| Method cache misses | 2,505 |  |
| Method cache collisions | 2,594 |  |
| Method cache dunder hits | 6,367,984 |  |
| Method cache dunder misses | 416 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,920 | 168,960 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 2,380 |  |
| Traces created | 2,380 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
| Inner loop found | 40 | 1.7% |
| Recursive call | 40 | 1.7% |
| Low confidence | 20 | 0.8% |
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
| <= 16 | 20 | 0.8% |
| <= 32 | 2,080 | 87.4% |
| <= 64 | 140 | 5.9% |
| <= 128 | 140 | 5.9% |


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
| <= 16 | 720 | 30.3% |
| <= 32 | 840 | 35.3% |
| <= 64 | 160 | 6.7% |
| <= 128 | 60 | 2.5% |


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
| CALL | 1,960 |
| CALL_PY_WITH_DEFAULTS | 120 |
| BINARY_SUBSCR_GETITEM | 20 |
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
| watched dict modification | 20 |
| watched globals modification | 20 |


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
