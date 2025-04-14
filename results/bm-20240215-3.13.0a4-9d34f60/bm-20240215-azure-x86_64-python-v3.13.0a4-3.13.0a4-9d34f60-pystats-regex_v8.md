
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
| LOAD_CONST | 45,613,180 | 19.2% | 19.2% |  |
| LOAD_GLOBAL_MODULE | 28,571,120 | 12.0% | 31.2% | 0.1% |
| BINARY_SUBSCR_LIST_INT | 20,027,340 | 8.4% | 39.6% | 0.0% |
| POP_TOP | 16,859,220 | 7.1% | 46.7% |  |
| CALL | 16,588,200 | 7.0% | 53.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 15,883,560 | 6.7% | 60.3% |  |
| LOAD_FAST | 13,024,340 | 5.5% | 65.8% |  |
| STORE_FAST | 10,578,040 | 4.4% | 70.2% |  |
| JUMP_BACKWARD | 9,024,820 | 3.8% | 74.0% |  |
| FOR_ITER_RANGE | 8,940,380 | 3.8% | 77.8% |  |
| POP_JUMP_IF_FALSE | 4,740,380 | 2.0% | 79.8% |  |
| LOAD_GLOBAL_BUILTIN | 4,596,880 | 1.9% | 81.7% | 0.0% |
| LOAD_FAST_LOAD_FAST | 4,532,500 | 1.9% | 83.6% |  |
| RESUME_CHECK | 4,343,180 | 1.8% | 85.4% |  |
| RETURN_VALUE | 4,204,040 | 1.8% | 87.2% |  |
| LOAD_ATTR_MODULE | 2,768,220 | 1.2% | 88.4% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,394,940 | 1.0% | 89.4% | 0.0% |
| PUSH_NULL | 2,015,400 | 0.8% | 90.2% |  |
| TO_BOOL_BOOL | 1,876,440 | 0.8% | 91.0% |  |
| NOP | 1,828,240 | 0.8% | 91.8% |  |
| CALL_ISINSTANCE | 1,827,780 | 0.8% | 92.5% |  |
| BUILD_TUPLE | 1,807,740 | 0.8% | 93.3% |  |
| BINARY_SUBSCR_DICT | 1,764,900 | 0.7% | 94.0% |  |
| CALL_TYPE_1 | 1,746,840 | 0.7% | 94.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,191,700 | 0.5% | 95.3% |  |
| IS_OP | 943,120 | 0.4% | 95.7% |  |
| STORE_FAST_STORE_FAST | 854,040 | 0.4% | 96.0% |  |
| TO_BOOL | 770,160 | 0.3% | 96.4% |  |
| TO_BOOL_LIST | 764,040 | 0.3% | 96.7% | 0.0% |
| IMPORT_NAME | 750,200 | 0.3% | 97.0% |  |
| CALL_KW | 749,600 | 0.3% | 97.3% |  |
| UNPACK_EX | 748,800 | 0.3% | 97.6% |  |
| CALL_PY_WITH_DEFAULTS | 743,180 | 0.3% | 97.9% |  |
| EXTENDED_ARG | 581,640 | 0.2% | 98.2% |  |
| LOAD_ATTR | 369,120 | 0.2% | 98.3% |  |
| POP_JUMP_IF_NOT_NONE | 323,200 | 0.1% | 98.5% |  |
| INTERPRETER_EXIT | 310,380 | 0.1% | 98.6% |  |
| POP_JUMP_IF_NONE | 278,740 | 0.1% | 98.7% |  |
| CONTAINS_OP | 191,520 | 0.1% | 98.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 167,960 | 0.1% | 98.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 164,080 | 0.1% | 98.9% |  |
| CALL_BUILTIN_O | 159,600 | 0.1% | 99.0% | 0.1% |
| RETURN_CONST | 140,560 | 0.1% | 99.1% |  |
| TO_BOOL_INT | 127,040 | 0.1% | 99.1% |  |
| POP_JUMP_IF_TRUE | 126,140 | 0.1% | 99.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 123,020 | 0.1% | 99.2% |  |
| BINARY_OP_ADD_INT | 122,980 | 0.1% | 99.3% |  |
| COMPARE_OP_STR | 122,760 | 0.1% | 99.3% | 2.3% |
| BINARY_OP | 121,920 | 0.1% | 99.4% |  |
| CALL_LEN | 97,680 | 0.0% | 99.4% |  |
| LOAD_GLOBAL | 94,240 | 0.0% | 99.5% |  |
| BINARY_SUBSCR | 93,100 | 0.0% | 99.5% |  |
| FOR_ITER_LIST | 90,700 | 0.0% | 99.5% | 5.6% |
| GET_ITER | 90,460 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_STR_INT | 79,740 | 0.0% | 99.6% | 3.6% |
| JUMP_FORWARD | 78,940 | 0.0% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 77,940 | 0.0% | 99.7% | 0.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 69,520 | 0.0% | 99.7% | 0.1% |
| CALL_BUILTIN_CLASS | 50,660 | 0.0% | 99.7% |  |
| FOR_ITER | 44,160 | 0.0% | 99.7% |  |
| BUILD_LIST | 41,920 | 0.0% | 99.8% |  |
| BINARY_SUBSCR_GETITEM | 40,080 | 0.0% | 99.8% |  |
| COMPARE_OP_INT | 40,060 | 0.0% | 99.8% |  |
| BINARY_OP_SUBTRACT_INT | 39,160 | 0.0% | 99.8% |  |
| CALL_LIST_APPEND | 37,320 | 0.0% | 99.8% |  |
| COPY | 31,860 | 0.0% | 99.8% |  |
| BINARY_SUBSCR_TUPLE_INT | 28,940 | 0.0% | 99.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 28,600 | 0.0% | 99.9% | 0.6% |
| STORE_SUBSCR | 22,520 | 0.0% | 99.9% |  |
| STORE_SUBSCR_LIST_INT | 17,940 | 0.0% | 99.9% |  |
| LOAD_NAME | 17,640 | 0.0% | 99.9% |  |
| TO_BOOL_NONE | 17,140 | 0.0% | 99.9% | 20.1% |
| BINARY_SLICE | 17,020 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 13,020 | 0.0% | 99.9% |  |
| TO_BOOL_STR | 12,640 | 0.0% | 99.9% | 0.5% |
| CALL_METHOD_DESCRIPTOR_O | 12,180 | 0.0% | 99.9% | 0.7% |
| STORE_FAST_LOAD_FAST | 11,720 | 0.0% | 99.9% |  |
| UNARY_NOT | 10,880 | 0.0% | 99.9% |  |
| COMPARE_OP | 10,220 | 0.0% | 99.9% |  |
| LOAD_ATTR_PROPERTY | 9,120 | 0.0% | 99.9% |  |
| STORE_SUBSCR_DICT | 8,100 | 0.0% | 99.9% |  |
| EXIT_INIT_CHECK | 7,820 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 7,820 | 0.0% | 99.9% |  |
| FOR_ITER_TUPLE | 7,300 | 0.0% | 100.0% |  |
| BUILD_SLICE | 7,220 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 7,180 | 0.0% | 100.0% |  |
| STORE_NAME | 6,340 | 0.0% | 100.0% |  |
| BUILD_MAP | 6,140 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 5,840 | 0.0% | 100.0% |  |
| POP_EXCEPT | 5,840 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 5,840 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 5,820 | 0.0% | 100.0% |  |
| SWAP | 5,680 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_INT | 5,380 | 0.0% | 100.0% |  |
| FORMAT_SIMPLE | 5,020 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 4,860 | 0.0% | 100.0% |  |
| LOAD_ATTR_SLOT | 4,720 | 0.0% | 100.0% |  |
| LIST_APPEND | 4,240 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,680 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,440 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 2,900 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 2,200 | 0.0% | 100.0% | 31.8% |
| MAP_ADD | 2,040 | 0.0% | 100.0% |  |
| UNARY_INVERT | 1,960 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 1,620 | 0.0% | 100.0% |  |
| BUILD_STRING | 1,540 | 0.0% | 100.0% |  |
| LOAD_DEREF | 1,380 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 1,360 | 0.0% | 100.0% |  |
| MAKE_FUNCTION | 1,140 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 1,040 | 0.0% | 100.0% |  |
| STORE_ATTR | 940 | 0.0% | 100.0% |  |
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
| COMPARE_OP_FLOAT | 120 | 0.0% | 100.0% |  |
| IMPORT_FROM | 100 | 0.0% | 100.0% |  |
| DELETE_NAME | 80 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| BUILD_SET | 60 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| DICT_UPDATE | 40 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_MODULE LOAD_CONST | 19,946,880 | 8.4% | 8.4% |
| LOAD_CONST BINARY_SUBSCR_LIST_INT | 19,909,800 | 8.4% | 16.7% |
| BINARY_SUBSCR_LIST_INT LOAD_ATTR_METHOD_NO_DICT | 14,049,240 | 5.9% | 22.7% |
| CALL POP_TOP | 13,929,940 | 5.9% | 28.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 13,527,680 | 5.7% | 34.2% |
| LOAD_CONST CALL | 10,200,360 | 4.3% | 38.5% |
| STORE_FAST LOAD_GLOBAL_MODULE | 8,902,020 | 3.7% | 42.2% |
| FOR_ITER_RANGE STORE_FAST | 8,891,640 | 3.7% | 46.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 8,729,440 | 3.7% | 49.6% |
| POP_TOP JUMP_BACKWARD | 8,716,060 | 3.7% | 53.3% |
| POP_TOP LOAD_GLOBAL_MODULE | 7,711,760 | 3.2% | 56.5% |
| LOAD_CONST LOAD_CONST | 7,111,160 | 3.0% | 59.5% |
| LOAD_CONST LOAD_GLOBAL_MODULE | 4,977,580 | 2.1% | 61.6% |
| BINARY_SUBSCR_LIST_INT CALL | 4,469,640 | 1.9% | 63.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,666,460 | 1.5% | 65.0% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 2,892,700 | 1.2% | 66.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 2,394,660 | 1.0% | 67.2% |
| POP_JUMP_IF_FALSE LOAD_FAST | 2,382,060 | 1.0% | 68.2% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,014,580 | 0.8% | 69.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,859,900 | 0.8% | 69.9% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 1,843,900 | 0.8% | 70.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,819,280 | 0.8% | 71.4% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,782,220 | 0.7% | 72.2% |
| RETURN_VALUE POP_TOP | 1,772,940 | 0.7% | 72.9% |
| PUSH_NULL LOAD_CONST | 1,770,100 | 0.7% | 73.7% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 1,758,620 | 0.7% | 74.4% |
| LOAD_FAST CALL | 1,755,760 | 0.7% | 75.1% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,752,240 | 0.7% | 75.9% |
| LOAD_FAST_LOAD_FAST BUILD_TUPLE | 1,748,660 | 0.7% | 76.6% |
| NOP LOAD_GLOBAL_MODULE | 1,748,000 | 0.7% | 77.3% |
| LOAD_FAST CALL_TYPE_1 | 1,746,780 | 0.7% | 78.1% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 1,745,000 | 0.7% | 78.8% |
| CALL_TYPE_1 LOAD_FAST_LOAD_FAST | 1,744,940 | 0.7% | 79.5% |
| LOAD_GLOBAL_MODULE LOAD_GLOBAL_BUILTIN | 1,744,060 | 0.7% | 80.3% |
| CALL RETURN_VALUE | 1,743,960 | 0.7% | 81.0% |
| BUILD_TUPLE BINARY_SUBSCR_DICT | 1,742,120 | 0.7% | 81.7% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 1,742,020 | 0.7% | 82.5% |
| BINARY_SUBSCR_DICT RETURN_VALUE | 1,741,020 | 0.7% | 83.2% |
| POP_JUMP_IF_FALSE NOP | 1,494,760 | 0.6% | 83.8% |
| RESUME_CHECK LOAD_FAST | 1,417,260 | 0.6% | 84.4% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,148,060 | 0.5% | 84.9% |
| STORE_FAST LOAD_FAST | 1,125,300 | 0.5% | 85.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,037,960 | 0.4% | 85.8% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,014,260 | 0.4% | 86.2% |
| LOAD_GLOBAL_MODULE IS_OP | 939,320 | 0.4% | 86.6% |
| IS_OP POP_JUMP_IF_FALSE | 911,320 | 0.4% | 87.0% |
| STORE_FAST_STORE_FAST LOAD_FAST | 807,120 | 0.3% | 87.4% |
| LOAD_GLOBAL_BUILTIN LOAD_CONST | 790,500 | 0.3% | 87.7% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 781,740 | 0.3% | 88.0% |
| LOAD_FAST TO_BOOL | 764,220 | 0.3% | 88.3% |
| LOAD_FAST TO_BOOL_LIST | 762,600 | 0.3% | 88.7% |
| TO_BOOL POP_JUMP_IF_FALSE | 760,760 | 0.3% | 89.0% |
| POP_JUMP_IF_FALSE LOAD_CONST | 756,560 | 0.3% | 89.3% |
| TO_BOOL_LIST POP_JUMP_IF_FALSE | 755,980 | 0.3% | 89.6% |
| CALL RESUME_CHECK | 752,300 | 0.3% | 89.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST_LOAD_FAST | 751,320 | 0.3% | 90.2% |
| LOAD_CONST LOAD_GLOBAL_BUILTIN | 750,260 | 0.3% | 90.6% |
| LOAD_CONST IMPORT_NAME | 750,200 | 0.3% | 90.9% |
| IMPORT_NAME STORE_FAST | 749,920 | 0.3% | 91.2% |
| LOAD_FAST LOAD_ATTR_MODULE | 749,880 | 0.3% | 91.5% |
| LOAD_CONST CALL_KW | 749,600 | 0.3% | 91.8% |
| LOAD_ATTR_MODULE LOAD_CONST | 749,440 | 0.3% | 92.1% |
| CALL_KW POP_TOP | 748,800 | 0.3% | 92.4% |
| LOAD_FAST UNPACK_EX | 748,800 | 0.3% | 92.8% |
| UNPACK_EX STORE_FAST_STORE_FAST | 748,800 | 0.3% | 93.1% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 743,180 | 0.3% | 93.4% |
| BINARY_SUBSCR_LIST_INT LOAD_GLOBAL_MODULE | 583,040 | 0.2% | 93.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 557,260 | 0.2% | 93.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 380,300 | 0.2% | 94.0% |
| LOAD_CONST CALL_PY_WITH_DEFAULTS | 369,200 | 0.2% | 94.2% |
| BINARY_SUBSCR_LIST_INT CALL_PY_WITH_DEFAULTS | 366,760 | 0.2% | 94.3% |
| BINARY_SUBSCR_LIST_INT LOAD_CONST | 358,280 | 0.2% | 94.5% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 320,900 | 0.1% | 94.6% |
| LOAD_FAST LOAD_CONST | 320,120 | 0.1% | 94.8% |
| STORE_FAST NOP | 318,240 | 0.1% | 94.9% |
| CACHE RESUME_CHECK | 316,780 | 0.1% | 95.0% |
| LOAD_FAST LOAD_ATTR | 315,140 | 0.1% | 95.2% |
| LOAD_ATTR STORE_FAST | 307,100 | 0.1% | 95.3% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 297,380 | 0.1% | 95.4% |
| RETURN_VALUE INTERPRETER_EXIT | 296,140 | 0.1% | 95.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 289,240 | 0.1% | 95.7% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 270,560 | 0.1% | 95.8% |
| POP_JUMP_IF_NONE LOAD_FAST | 266,780 | 0.1% | 95.9% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 266,640 | 0.1% | 96.0% |
| RETURN_VALUE RETURN_VALUE | 260,720 | 0.1% | 96.1% |
| LOAD_ATTR_MODULE CALL_PY_EXACT_ARGS | 253,900 | 0.1% | 96.2% |
| LOAD_FAST PUSH_NULL | 248,040 | 0.1% | 96.3% |
| EXTENDED_ARG JUMP_BACKWARD | 232,160 | 0.1% | 96.4% |
| JUMP_BACKWARD EXTENDED_ARG | 227,420 | 0.1% | 96.5% |
| POP_TOP EXTENDED_ARG | 193,020 | 0.1% | 96.6% |
| EXTENDED_ARG FOR_ITER_RANGE | 173,360 | 0.1% | 96.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS POP_TOP | 163,800 | 0.1% | 96.7% |
| POP_TOP LOAD_FAST | 149,620 | 0.1% | 96.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 148,800 | 0.1% | 96.9% |
| PUSH_NULL LOAD_FAST | 140,620 | 0.1% | 96.9% |
| CALL CALL | 137,900 | 0.1% | 97.0% |
| CALL_BUILTIN_O POP_TOP | 120,120 | 0.1% | 97.0% |
| LOAD_ATTR_INSTANCE_VALUE STORE_FAST | 119,060 | 0.1% | 97.1% |
| LOAD_CONST BINARY_OP_ADD_INT | 115,760 | 0.0% | 97.1% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 112,260 | 0.0% | 97.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 10,240 | 60.2% |
| LOAD_CONST | 4,580 | 26.9% |
| LOAD_FAST | 2,200 | 12.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,180 | 83.3% |
| LOAD_CONST | 2,080 | 12.2% |
| LOAD_FAST | 340 | 2.0% |
| CALL_PY_EXACT_ARGS | 180 | 1.1% |
| BUILD_TUPLE | 120 | 0.7% |


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
| JUMP_BACKWARD | 400 | 90.9% |
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
| LOAD_ATTR_INSTANCE_VALUE | 3,240 | 64.5% |
| LOAD_FAST | 1,500 | 29.9% |
| LOAD_ATTR | 180 | 3.6% |
| STORE_FAST_LOAD_FAST | 100 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,780 | 95.2% |
| BUILD_STRING | 240 | 4.8% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 40,340 | 44.6% |
| LOAD_FAST | 18,820 | 20.8% |
| LOAD_ATTR_INSTANCE_VALUE | 15,360 | 17.0% |
| BINARY_SUBSCR | 7,040 | 7.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,820 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 36,140 | 40.0% |
| EXTENDED_ARG | 32,000 | 35.4% |
| FOR_ITER_LIST | 11,960 | 13.2% |
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
| POP_JUMP_IF_FALSE | 1,494,760 | 81.8% |
| STORE_FAST | 318,240 | 17.4% |
| RESUME_CHECK | 3,600 | 0.2% |
| STORE_FAST_STORE_FAST | 3,540 | 0.2% |
| NOP | 3,120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,748,000 | 95.6% |
| LOAD_FAST | 68,020 | 3.7% |
| LOAD_FAST_LOAD_FAST | 3,940 | 0.2% |
| NOP | 3,120 | 0.2% |
| LOAD_CONST | 2,440 | 0.1% |


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
| CALL | 13,929,940 | 82.6% |
| RETURN_VALUE | 1,772,940 | 10.5% |
| CALL_KW | 748,800 | 4.4% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 163,800 | 1.0% |
| CALL_BUILTIN_O | 120,120 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,716,060 | 51.7% |
| LOAD_GLOBAL_MODULE | 7,711,760 | 45.7% |
| EXTENDED_ARG | 193,020 | 1.1% |
| LOAD_FAST | 149,620 | 0.9% |
| LOAD_GLOBAL | 46,620 | 0.3% |


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
| LOAD_ATTR_MODULE | 1,752,240 | 86.9% |
| LOAD_FAST | 248,040 | 12.3% |
| STORE_FAST_LOAD_FAST | 9,460 | 0.5% |
| LOAD_ATTR | 3,100 | 0.2% |
| LOAD_NAME | 2,080 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,770,100 | 87.8% |
| LOAD_FAST | 140,620 | 7.0% |
| LOAD_GLOBAL_MODULE | 54,780 | 2.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 33,600 | 1.7% |
| LOAD_FAST_LOAD_FAST | 13,760 | 0.7% |


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
| CALL | 1,743,960 | 41.5% |
| BINARY_SUBSCR_DICT | 1,741,020 | 41.4% |
| LOAD_ATTR_INSTANCE_VALUE | 266,640 | 6.3% |
| RETURN_VALUE | 260,720 | 6.2% |
| BINARY_SUBSCR_LIST_INT | 61,460 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,772,940 | 42.2% |
| LOAD_ATTR_METHOD_NO_DICT | 1,742,020 | 41.4% |
| INTERPRETER_EXIT | 296,140 | 7.0% |
| RETURN_VALUE | 260,720 | 6.2% |
| STORE_FAST | 44,640 | 1.1% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,320 | 45.8% |
| LOAD_FAST_LOAD_FAST | 7,800 | 34.6% |
| LOAD_FAST | 2,300 | 10.2% |
| LOAD_CONST | 1,880 | 8.3% |
| STORE_SUBSCR | 140 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 14,860 | 66.0% |
| RETURN_CONST | 2,280 | 10.1% |
| EXTENDED_ARG | 1,880 | 8.3% |
| LOAD_FAST_LOAD_FAST | 1,600 | 7.1% |
| JUMP_FORWARD | 1,440 | 6.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 764,220 | 99.2% |
| BINARY_OP | 2,920 | 0.4% |
| LOAD_ATTR | 1,740 | 0.2% |
| TO_BOOL | 800 | 0.1% |
| CALL | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 760,760 | 98.8% |
| POP_JUMP_IF_TRUE | 8,280 | 1.1% |
| TO_BOOL | 800 | 0.1% |
| TO_BOOL_BOOL | 140 | 0.0% |
| TO_BOOL_NONE | 80 | 0.0% |


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
| TO_BOOL_INT | 7,040 | 64.7% |
| TO_BOOL_LIST | 3,840 | 35.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 7,040 | 64.7% |
| CALL_PY_EXACT_ARGS | 3,840 | 35.3% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 87,520 | 71.8% |
| LOAD_CONST | 11,180 | 9.2% |
| LOAD_FAST_LOAD_FAST | 7,540 | 6.2% |
| LOAD_FAST | 4,620 | 3.8% |
| RETURN_VALUE | 3,000 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 77,140 | 63.3% |
| STORE_FAST | 14,260 | 11.7% |
| STORE_SUBSCR | 10,320 | 8.5% |
| LOAD_FAST | 4,880 | 4.0% |
| TO_BOOL | 2,920 | 2.4% |


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
| LOAD_CONST | 1,300 | 84.4% |
| FORMAT_SIMPLE | 240 | 15.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,120 | 72.7% |
| LOAD_FAST | 180 | 11.7% |
| YIELD_VALUE | 100 | 6.5% |
| CALL_BUILTIN_O | 100 | 6.5% |
| LOAD_CONST | 40 | 2.6% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,748,660 | 96.7% |
| CALL_BUILTIN_O | 23,880 | 1.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 9,380 | 0.5% |
| LOAD_FAST | 7,780 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 5,680 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 1,742,120 | 96.4% |
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
| LOAD_CONST | 10,200,360 | 61.5% |
| BINARY_SUBSCR_LIST_INT | 4,469,640 | 26.9% |
| LOAD_FAST | 1,755,760 | 10.6% |
| CALL | 137,900 | 0.8% |
| BINARY_SUBSCR | 16,180 | 0.1% |

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
| LOAD_GLOBAL_MODULE | 96,920 | 50.6% |
| LOAD_FAST_LOAD_FAST | 47,900 | 25.0% |
| LOAD_CONST | 35,620 | 18.6% |
| LOAD_FAST | 10,780 | 5.6% |
| LOAD_ATTR_MODULE | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 148,800 | 77.7% |
| EXTENDED_ARG | 38,560 | 20.1% |
| POP_JUMP_IF_TRUE | 2,340 | 1.2% |
| RETURN_VALUE | 1,740 | 0.9% |
| STORE_FAST | 80 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 9,800 | 30.8% |
| LOAD_CONST | 9,400 | 29.5% |
| UNARY_NOT | 7,040 | 22.1% |
| LOAD_FAST | 2,360 | 7.4% |
| BINARY_OP | 2,040 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 9,820 | 30.8% |
| STORE_FAST_STORE_FAST | 9,380 | 29.4% |
| TO_BOOL_BOOL | 7,140 | 22.4% |
| TO_BOOL_INT | 4,080 | 12.8% |
| COMPARE_OP_INT | 1,060 | 3.3% |


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
| FOR_ITER | 40 | 50.0% |
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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 227,420 | 39.1% |
| POP_TOP | 193,020 | 33.2% |
| CONTAINS_OP | 38,560 | 6.6% |
| JUMP_FORWARD | 32,480 | 5.6% |
| GET_ITER | 32,000 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 232,160 | 39.9% |
| FOR_ITER_RANGE | 173,360 | 29.8% |
| FOR_ITER_LIST | 58,000 | 10.0% |
| POP_JUMP_IF_FALSE | 52,500 | 9.0% |
| JUMP_FORWARD | 37,560 | 6.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 28,060 | 63.5% |
| GET_ITER | 7,600 | 17.2% |
| JUMP_BACKWARD | 7,220 | 16.3% |
| FOR_ITER | 1,020 | 2.3% |
| LOAD_FAST | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 22,320 | 50.5% |
| RETURN_CONST | 6,740 | 15.3% |
| STORE_FAST | 4,920 | 11.1% |
| LOAD_FAST | 2,820 | 6.4% |
| LOAD_GLOBAL_MODULE | 2,820 | 6.4% |


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
| LOAD_GLOBAL_MODULE | 939,320 | 99.6% |
| LOAD_GLOBAL_BUILTIN | 1,840 | 0.2% |
| LOAD_FAST | 1,800 | 0.2% |
| LOAD_CONST | 100 | 0.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 911,320 | 96.6% |
| POP_JUMP_IF_TRUE | 31,700 | 3.4% |
| COPY | 100 | 0.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,716,060 | 96.6% |
| EXTENDED_ARG | 232,160 | 2.6% |
| POP_JUMP_IF_TRUE | 30,260 | 0.3% |
| STORE_SUBSCR | 14,860 | 0.2% |
| STORE_SUBSCR_LIST_INT | 9,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_RANGE | 8,729,440 | 96.7% |
| EXTENDED_ARG | 227,420 | 2.5% |
| LOAD_FAST | 35,020 | 0.4% |
| FOR_ITER_LIST | 20,620 | 0.2% |
| FOR_ITER | 7,220 | 0.1% |


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
| EXTENDED_ARG | 32,480 | 41.1% |
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
| CALL_BUILTIN_CLASS | 2,080 | 49.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,440 | 34.0% |
| BUILD_TUPLE | 720 | 17.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,240 | 100.0% |


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
| LOAD_FAST | 315,140 | 85.4% |
| BINARY_SUBSCR | 21,480 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 21,460 | 5.8% |
| LOAD_GLOBAL | 3,780 | 1.0% |
| LOAD_GLOBAL_MODULE | 3,760 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 307,100 | 83.2% |
| LOAD_ATTR_METHOD_NO_DICT | 21,720 | 5.9% |
| LOAD_CONST | 19,240 | 5.2% |
| LOAD_FAST | 5,160 | 1.4% |
| LOAD_ATTR_MODULE | 3,760 | 1.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 19,946,880 | 43.7% |
| LOAD_ATTR_METHOD_NO_DICT | 13,527,680 | 29.7% |
| LOAD_CONST | 7,111,160 | 15.6% |
| PUSH_NULL | 1,770,100 | 3.9% |
| LOAD_GLOBAL_BUILTIN | 790,500 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 19,909,800 | 43.6% |
| CALL | 10,200,360 | 22.4% |
| LOAD_CONST | 7,111,160 | 15.6% |
| LOAD_GLOBAL_MODULE | 4,977,580 | 10.9% |
| LOAD_GLOBAL_BUILTIN | 750,260 | 1.6% |


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
| LOAD_GLOBAL_BUILTIN | 3,666,460 | 28.2% |
| POP_JUMP_IF_FALSE | 2,382,060 | 18.3% |
| RESUME_CHECK | 1,417,260 | 10.9% |
| STORE_FAST | 1,125,300 | 8.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,037,960 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,892,700 | 22.2% |
| CALL | 1,755,760 | 13.5% |
| CALL_TYPE_1 | 1,746,780 | 13.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,148,060 | 8.8% |
| TO_BOOL | 764,220 | 5.9% |


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
| LOAD_GLOBAL_MODULE | 1,782,220 | 39.3% |
| CALL_TYPE_1 | 1,744,940 | 38.5% |
| LOAD_ATTR_METHOD_NO_DICT | 751,320 | 16.6% |
| STORE_ATTR_INSTANCE_VALUE | 51,600 | 1.1% |
| STORE_FAST_STORE_FAST | 34,780 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,758,620 | 38.8% |
| BUILD_TUPLE | 1,748,660 | 38.6% |
| LOAD_FAST | 781,740 | 17.2% |
| STORE_ATTR_INSTANCE_VALUE | 78,400 | 1.7% |
| CONTAINS_OP | 47,900 | 1.1% |


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
| LOAD_NAME | 4,600 | 26.1% |
| STORE_NAME | 3,540 | 20.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,960 | 11.1% |
| LOAD_FAST | 1,540 | 8.7% |
| STORE_FAST_STORE_FAST | 1,540 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,600 | 26.1% |
| LOAD_CONST | 4,220 | 23.9% |
| PUSH_NULL | 2,080 | 11.8% |
| CALL_METHOD_DESCRIPTOR_O | 1,920 | 10.9% |
| LOAD_ATTR_METHOD_NO_DICT | 1,920 | 10.9% |


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
| JUMP_BACKWARD | 1,360 | 66.7% |
| LOAD_CONST | 640 | 31.4% |
| BUILD_MAP | 20 | 1.0% |
| DICT_UPDATE | 20 | 1.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,843,900 | 38.9% |
| IS_OP | 911,320 | 19.2% |
| TO_BOOL | 760,760 | 16.0% |
| TO_BOOL_LIST | 755,980 | 15.9% |
| CONTAINS_OP | 148,800 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,382,060 | 50.3% |
| NOP | 1,494,760 | 31.5% |
| LOAD_CONST | 756,560 | 16.0% |
| LOAD_GLOBAL_MODULE | 34,980 | 0.7% |
| LOAD_FAST_LOAD_FAST | 15,740 | 0.3% |


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
| JUMP_BACKWARD | 1,500 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 580 | 0.2% |
| LOAD_GLOBAL_MODULE | 360 | 0.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,900 | 99.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,420 | 0.4% |
| CALL_BUILTIN_FAST | 440 | 0.1% |
| LOAD_FAST_CHECK | 280 | 0.1% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 297,380 | 92.0% |
| BUILD_LIST | 8,000 | 2.5% |
| LOAD_GLOBAL_MODULE | 5,540 | 1.7% |
| LOAD_GLOBAL_BUILTIN | 4,160 | 1.3% |
| EXTENDED_ARG | 2,820 | 0.9% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 37,580 | 29.8% |
| IS_OP | 31,700 | 25.1% |
| TO_BOOL_BOOL | 29,080 | 23.1% |
| TO_BOOL_STR | 11,280 | 8.9% |
| TO_BOOL | 8,280 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,720 | 45.8% |
| JUMP_BACKWARD | 30,260 | 24.0% |
| CALL_LEN | 9,620 | 7.6% |
| LOAD_FAST_LOAD_FAST | 7,820 | 6.2% |
| LOAD_GLOBAL_MODULE | 5,500 | 4.4% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 53,400 | 38.0% |
| CALL_LIST_APPEND | 29,680 | 21.1% |
| POP_TOP | 13,920 | 9.9% |
| POP_JUMP_IF_FALSE | 13,240 | 9.4% |
| FOR_ITER_RANGE | 7,680 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 96,800 | 68.9% |
| TO_BOOL_BOOL | 16,440 | 11.7% |
| INTERPRETER_EXIT | 14,020 | 10.0% |
| EXIT_INIT_CHECK | 7,820 | 5.6% |
| STORE_FAST | 5,340 | 3.8% |


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
| LOAD_FAST_LOAD_FAST | 460 | 48.9% |
| LOAD_FAST | 440 | 46.8% |
| SWAP | 40 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 38.3% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 19.1% |
| JUMP_BACKWARD | 120 | 12.8% |
| LOAD_FAST_LOAD_FAST | 120 | 12.8% |
| NOP | 80 | 8.5% |


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
| FOR_ITER_RANGE | 8,891,640 | 84.1% |
| IMPORT_NAME | 749,920 | 7.1% |
| LOAD_ATTR | 307,100 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 119,060 | 1.1% |
| BINARY_OP_ADD_INT | 61,440 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 8,902,020 | 84.2% |
| LOAD_FAST | 1,125,300 | 10.6% |
| NOP | 318,240 | 3.0% |
| LOAD_CONST | 61,100 | 0.6% |
| STORE_FAST | 43,700 | 0.4% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 9,460 | 80.7% |
| FOR_ITER_TUPLE | 2,240 | 19.1% |
| FOR_ITER | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 9,460 | 80.7% |
| TO_BOOL_STR | 1,440 | 12.3% |
| LOAD_FAST | 720 | 6.1% |
| FORMAT_SIMPLE | 100 | 0.9% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_EX | 748,800 | 87.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 91,920 | 10.8% |
| COPY | 9,380 | 1.1% |
| UNPACK_SEQUENCE_TUPLE | 3,520 | 0.4% |
| STORE_FAST_STORE_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 807,120 | 94.5% |
| LOAD_FAST_LOAD_FAST | 34,780 | 4.1% |
| NOP | 3,540 | 0.4% |
| STORE_FAST | 3,160 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 3,080 | 0.4% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 1,960 | 30.9% |
| LOAD_CONST | 1,780 | 28.1% |
| FOR_ITER | 1,040 | 16.4% |
| MAKE_FUNCTION | 460 | 7.3% |
| RETURN_VALUE | 300 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 3,540 | 55.8% |
| LOAD_CONST | 2,460 | 38.8% |
| RETURN_CONST | 100 | 1.6% |
| POP_TOP | 80 | 1.3% |
| LOAD_BUILD_CLASS | 40 | 0.6% |


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
| BUILD_STRING | 100 | 45.5% |

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
| LOAD_CONST | 115,760 | 94.1% |
| LOAD_FAST_LOAD_FAST | 5,080 | 4.1% |
| BINARY_OP_MULTIPLY_INT | 2,140 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 61,440 | 50.0% |
| LOAD_FAST | 46,060 | 37.5% |
| BINARY_SLICE | 10,240 | 8.3% |
| CALL_PY_EXACT_ARGS | 2,060 | 1.7% |
| CALL_BUILTIN_O | 1,600 | 1.3% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,040 | 69.4% |
| LOAD_FAST_LOAD_FAST | 1,080 | 18.6% |
| CALL_METHOD_DESCRIPTOR_O | 360 | 6.2% |
| BINARY_OP | 220 | 3.8% |
| BINARY_SUBSCR_LIST_INT | 120 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 1,840 | 31.6% |
| BUILD_TUPLE | 960 | 16.5% |
| LOAD_NAME | 960 | 16.5% |
| CALL | 540 | 9.3% |
| LOAD_FAST | 540 | 9.3% |


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
| LOAD_FAST | 15,280 | 39.0% |
| LOAD_CONST | 14,180 | 36.2% |
| CALL_LEN | 9,680 | 24.7% |
| BINARY_OP | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 9,680 | 24.7% |
| LOAD_FAST_LOAD_FAST | 9,460 | 24.2% |
| LOAD_FAST | 7,980 | 20.4% |
| BINARY_SUBSCR_LIST_INT | 5,000 | 12.8% |
| LOAD_CONST | 3,860 | 9.9% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,742,120 | 98.7% |
| LOAD_FAST | 20,320 | 1.2% |
| LOAD_FAST_LOAD_FAST | 2,280 | 0.1% |
| LOAD_CONST | 120 | 0.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,741,020 | 98.6% |
| LOAD_FAST | 10,180 | 0.6% |
| CALL_BUILTIN_O | 5,900 | 0.3% |
| LOAD_CONST | 3,080 | 0.2% |
| PUSH_EXC_INFO | 2,980 | 0.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 28,620 | 71.4% |
| LOAD_CONST | 11,460 | 28.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 40,080 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 19,909,800 | 99.4% |
| LOAD_FAST | 63,440 | 0.3% |
| BINARY_SUBSCR | 41,080 | 0.2% |
| LOAD_FAST_LOAD_FAST | 7,880 | 0.0% |
| BINARY_OP_SUBTRACT_INT | 5,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 14,049,240 | 70.2% |
| CALL | 4,469,640 | 22.3% |
| LOAD_GLOBAL_MODULE | 583,040 | 2.9% |
| CALL_PY_WITH_DEFAULTS | 366,760 | 1.8% |
| LOAD_CONST | 358,280 | 1.8% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,620 | 57.2% |
| LOAD_CONST | 34,060 | 42.7% |
| BINARY_SUBSCR_STR_INT | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 39,020 | 48.9% |
| LOAD_CONST | 32,120 | 40.3% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,780 | 4.7% |
| PUSH_EXC_INFO | 2,820 | 3.5% |
| CALL_BUILTIN_O | 1,940 | 2.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 28,920 | 99.9% |
| BINARY_SUBSCR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,460 | 32.7% |
| CALL_BUILTIN_O | 6,260 | 21.6% |
| GET_ITER | 2,460 | 8.5% |
| LOAD_FAST | 2,220 | 7.7% |
| BINARY_OP_MULTIPLY_INT | 2,140 | 7.4% |


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
| PUSH_NULL | 33,600 | 43.1% |
| BUILD_TUPLE | 25,260 | 32.4% |
| LOAD_CONST | 15,180 | 19.5% |
| LOAD_FAST | 3,860 | 5.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 77,640 | 99.6% |
| POP_TOP | 280 | 0.4% |
| COPY_FREE_VARS | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,320 | 77.6% |
| CALL_LEN | 8,540 | 16.9% |
| CALL | 1,280 | 2.5% |
| CALL_BUILTIN_FAST | 680 | 1.3% |
| BINARY_OP_ADD_INT | 320 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 40,340 | 79.6% |
| LOAD_CONST | 7,040 | 13.9% |
| LIST_APPEND | 2,080 | 4.1% |
| RETURN_VALUE | 680 | 1.3% |
| STORE_FAST | 420 | 0.8% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,140 | 51.8% |
| LOAD_CONST | 620 | 28.2% |
| LOAD_FAST_LOAD_FAST | 220 | 10.0% |
| MAKE_FUNCTION | 80 | 3.6% |
| LOAD_ATTR_SLOT | 80 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 680 | 30.9% |
| POP_JUMP_IF_NOT_NONE | 440 | 20.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 15.5% |
| POP_TOP | 260 | 11.8% |
| STORE_FAST | 220 | 10.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 18,760 | 65.6% |
| LOAD_FAST_LOAD_FAST | 6,160 | 21.5% |
| CALL_TUPLE_1 | 2,820 | 9.9% |
| LOAD_FAST | 480 | 1.7% |
| LOAD_CONST | 200 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 9,380 | 32.8% |
| LOAD_GLOBAL_BUILTIN | 9,380 | 32.8% |
| STORE_FAST | 6,520 | 22.8% |
| RETURN_VALUE | 3,240 | 11.3% |
| BEFORE_WITH | 60 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 100,560 | 63.0% |
| LOAD_GLOBAL_MODULE | 16,300 | 10.2% |
| LOAD_CONST | 12,620 | 7.9% |
| RETURN_VALUE | 7,040 | 4.4% |
| BINARY_SUBSCR_TUPLE_INT | 6,260 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 120,120 | 75.3% |
| BUILD_TUPLE | 23,880 | 15.0% |
| TO_BOOL_BOOL | 10,520 | 6.6% |
| STORE_FAST | 4,980 | 3.1% |
| TO_BOOL_INT | 80 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,745,000 | 95.5% |
| LOAD_GLOBAL_BUILTIN | 72,100 | 3.9% |
| BUILD_TUPLE | 5,700 | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,720 | 0.1% |
| LOAD_ATTR_SLOT | 1,720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,819,280 | 99.5% |
| RETURN_VALUE | 5,640 | 0.3% |
| LOAD_FAST | 2,820 | 0.2% |
| TO_BOOL | 40 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 55,660 | 57.0% |
| LOAD_ATTR_INSTANCE_VALUE | 26,640 | 27.3% |
| POP_JUMP_IF_TRUE | 9,620 | 9.8% |
| LOAD_GLOBAL_MODULE | 5,640 | 5.8% |
| LOAD_CONST | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 26,400 | 27.0% |
| LOAD_CONST | 13,440 | 13.8% |
| LOAD_FAST | 12,580 | 12.9% |
| BINARY_OP_SUBTRACT_INT | 9,680 | 9.9% |
| STORE_FAST_LOAD_FAST | 9,460 | 9.7% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,600 | 79.3% |
| BUILD_TUPLE | 3,140 | 8.4% |
| LOAD_GLOBAL_MODULE | 2,820 | 7.6% |
| LOAD_CONST | 1,680 | 4.5% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 29,680 | 79.5% |
| LOAD_FAST | 4,420 | 11.8% |
| JUMP_BACKWARD | 1,680 | 4.5% |
| NOP | 1,320 | 3.5% |
| LOAD_FAST_LOAD_FAST | 180 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,000 | 46.1% |
| LOAD_CONST | 2,820 | 21.7% |
| LOAD_GLOBAL_MODULE | 1,600 | 12.3% |
| LOAD_FAST_LOAD_FAST | 1,260 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 1,140 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 11,320 | 86.9% |
| LIST_APPEND | 1,440 | 11.1% |
| POP_TOP | 120 | 0.9% |
| LOAD_FAST | 80 | 0.6% |
| SWAP | 60 | 0.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 94,000 | 57.3% |
| LOAD_CONST | 69,180 | 42.2% |
| CALL | 700 | 0.4% |
| LOAD_GLOBAL_MODULE | 180 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 163,800 | 99.8% |
| LOAD_CONST | 180 | 0.1% |
| STORE_FAST | 60 | 0.0% |
| STORE_DEREF | 20 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,660 | 99.5% |
| CALL | 20 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,820 | 76.6% |
| BUILD_TUPLE | 700 | 19.0% |
| TO_BOOL_BOOL | 120 | 3.3% |
| RETURN_VALUE | 40 | 1.1% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,940 | 40.6% |
| LOAD_NAME | 1,920 | 15.8% |
| RETURN_VALUE | 1,500 | 12.3% |
| CALL_METHOD_DESCRIPTOR_O | 1,400 | 11.5% |
| LOAD_GLOBAL_MODULE | 920 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,240 | 67.7% |
| RETURN_VALUE | 1,600 | 13.1% |
| CALL_METHOD_DESCRIPTOR_O | 1,400 | 11.5% |
| BINARY_OP_ADD_UNICODE | 360 | 3.0% |
| LOAD_CONST | 280 | 2.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,758,620 | 73.4% |
| LOAD_FAST | 289,240 | 12.1% |
| LOAD_ATTR_MODULE | 253,900 | 10.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 62,660 | 2.6% |
| LOAD_GLOBAL_MODULE | 7,320 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,394,660 | 100.0% |
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
| LOAD_CONST | 369,200 | 49.7% |
| BINARY_SUBSCR_LIST_INT | 366,760 | 49.4% |
| LOAD_FAST_LOAD_FAST | 2,900 | 0.4% |
| LOAD_FAST | 2,260 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060 | 0.1% |

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
| LOAD_FAST | 1,746,780 | 100.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,744,940 | 99.9% |
| LOAD_FAST | 1,720 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |
| PUSH_NULL | 60 | 0.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 120 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 24,020 | 60.0% |
| LOAD_GLOBAL_MODULE | 7,240 | 18.1% |
| BINARY_SUBSCR_LIST_INT | 3,940 | 9.8% |
| CALL_LEN | 2,620 | 6.5% |
| COPY | 1,060 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 39,600 | 98.9% |
| POP_JUMP_IF_TRUE | 340 | 0.8% |
| RETURN_VALUE | 60 | 0.1% |
| STORE_FAST | 60 | 0.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 105,780 | 86.2% |
| LOAD_ATTR_INSTANCE_VALUE | 16,720 | 13.6% |
| COMPARE_OP | 160 | 0.1% |
| LOAD_FAST | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 112,260 | 91.4% |
| EXTENDED_ARG | 10,440 | 8.5% |
| COMPARE_OP | 60 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 58,000 | 63.9% |
| JUMP_BACKWARD | 20,620 | 22.7% |
| GET_ITER | 11,960 | 13.2% |
| FOR_ITER | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 55,240 | 60.9% |
| STORE_FAST | 14,600 | 16.1% |
| LOAD_GLOBAL_BUILTIN | 9,400 | 10.4% |
| LOAD_FAST_LOAD_FAST | 3,020 | 3.3% |
| LOAD_FAST | 2,900 | 3.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,729,440 | 97.6% |
| EXTENDED_ARG | 173,360 | 1.9% |
| GET_ITER | 36,140 | 0.4% |
| FOR_ITER | 1,260 | 0.0% |
| SWAP | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,891,640 | 99.5% |
| LOAD_GLOBAL_BUILTIN | 30,000 | 0.3% |
| LOAD_FAST | 8,540 | 0.1% |
| RETURN_CONST | 7,680 | 0.1% |
| LOAD_GLOBAL | 2,040 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,820 | 66.0% |
| GET_ITER | 1,280 | 17.5% |
| SWAP | 1,120 | 15.3% |
| FOR_ITER | 60 | 0.8% |
| LOAD_FAST | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,240 | 30.7% |
| STORE_NAME | 1,960 | 26.8% |
| SWAP | 1,140 | 15.6% |
| STORE_FAST | 660 | 9.0% |
| JUMP_BACKWARD | 580 | 7.9% |


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
| LOAD_FAST | 1,148,060 | 96.3% |
| LOAD_FAST_LOAD_FAST | 29,140 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 14,100 | 1.2% |
| LOAD_ATTR | 240 | 0.0% |
| COPY | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 380,300 | 31.9% |
| POP_JUMP_IF_NONE | 270,560 | 22.7% |
| RETURN_VALUE | 266,640 | 22.4% |
| STORE_FAST | 119,060 | 10.0% |
| LOAD_ATTR_METHOD_NO_DICT | 31,600 | 2.7% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 14,049,240 | 88.5% |
| RETURN_VALUE | 1,742,020 | 11.0% |
| LOAD_ATTR_INSTANCE_VALUE | 31,600 | 0.2% |
| LOAD_FAST | 23,960 | 0.2% |
| LOAD_ATTR | 21,720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,527,680 | 85.2% |
| LOAD_FAST | 1,037,960 | 6.5% |
| LOAD_FAST_LOAD_FAST | 751,320 | 4.7% |
| LOAD_GLOBAL_MODULE | 557,260 | 3.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,660 | 0.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 65,640 | 94.4% |
| BINARY_SUBSCR_TUPLE_INT | 1,880 | 2.7% |
| BINARY_SUBSCR | 1,600 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 320 | 0.5% |
| LOAD_GLOBAL_MODULE | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 62,660 | 90.1% |
| LOAD_FAST | 3,700 | 5.3% |
| LOAD_CONST | 2,040 | 2.9% |
| LOAD_GLOBAL_MODULE | 940 | 1.4% |
| LOAD_FAST_LOAD_FAST | 180 | 0.3% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,014,580 | 72.8% |
| LOAD_FAST | 749,880 | 27.1% |
| LOAD_ATTR | 3,760 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,752,240 | 63.3% |
| LOAD_CONST | 749,440 | 27.1% |
| CALL_PY_EXACT_ARGS | 253,900 | 9.2% |
| STORE_FAST | 5,900 | 0.2% |
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
| LOAD_FAST | 2,020 | 42.8% |
| LOAD_FAST_LOAD_FAST | 1,720 | 36.4% |
| LOAD_ATTR_MODULE | 860 | 18.2% |
| RETURN_VALUE | 120 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,720 | 36.4% |
| CALL_ISINSTANCE | 1,720 | 36.4% |
| LOAD_FAST | 820 | 17.4% |
| LOAD_CONST | 240 | 5.1% |
| STORE_FAST | 120 | 2.5% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,859,900 | 40.5% |
| LOAD_GLOBAL_MODULE | 1,744,060 | 37.9% |
| LOAD_CONST | 750,260 | 16.3% |
| LOAD_FAST | 80,540 | 1.8% |
| STORE_FAST | 32,980 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,666,460 | 79.8% |
| LOAD_CONST | 790,500 | 17.2% |
| CALL_ISINSTANCE | 72,100 | 1.6% |
| STORE_FAST | 23,480 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 13,700 | 0.3% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,902,020 | 31.2% |
| POP_TOP | 7,711,760 | 27.0% |
| LOAD_CONST | 4,977,580 | 17.4% |
| LOAD_FAST | 2,892,700 | 10.1% |
| NOP | 1,748,000 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 19,946,880 | 69.8% |
| LOAD_ATTR_MODULE | 2,014,580 | 7.1% |
| LOAD_FAST_LOAD_FAST | 1,782,220 | 6.2% |
| CALL_ISINSTANCE | 1,745,000 | 6.1% |
| LOAD_GLOBAL_BUILTIN | 1,744,060 | 6.1% |


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
| CALL_PY_EXACT_ARGS | 2,394,660 | 55.1% |
| CALL | 752,300 | 17.3% |
| CALL_PY_WITH_DEFAULTS | 743,180 | 17.1% |
| CACHE | 316,780 | 7.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 77,640 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,859,900 | 42.8% |
| LOAD_FAST | 1,417,260 | 32.6% |
| LOAD_GLOBAL_MODULE | 1,014,260 | 23.4% |
| LOAD_FAST_LOAD_FAST | 32,500 | 0.7% |
| BUILD_LIST | 9,720 | 0.2% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,400 | 51.4% |
| LOAD_FAST_LOAD_FAST | 78,400 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 2,820 | 1.7% |
| STORE_ATTR | 180 | 0.1% |
| SWAP | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 53,400 | 31.8% |
| LOAD_FAST_LOAD_FAST | 51,600 | 30.7% |
| LOAD_FAST | 29,720 | 17.7% |
| LOAD_CONST | 21,480 | 12.8% |
| BUILD_MAP | 5,640 | 3.4% |


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
| LOAD_FAST | 6,020 | 74.3% |
| BINARY_OP_ADD_UNICODE | 1,840 | 22.7% |
| LOAD_ATTR_INSTANCE_VALUE | 160 | 2.0% |
| STORE_SUBSCR | 80 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,020 | 37.3% |
| LOAD_GLOBAL_BUILTIN | 2,820 | 34.8% |
| LOAD_NAME | 1,440 | 17.8% |
| JUMP_BACKWARD | 580 | 7.2% |
| LOAD_GLOBAL_MODULE | 160 | 2.0% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 13,260 | 73.9% |
| LOAD_FAST | 4,680 | 26.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 9,960 | 55.5% |
| RETURN_CONST | 4,360 | 24.3% |
| EXTENDED_ARG | 3,480 | 19.4% |
| LOAD_FAST | 140 | 0.8% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,819,280 | 97.0% |
| RETURN_CONST | 16,440 | 0.9% |
| CALL_BUILTIN_O | 10,520 | 0.6% |
| LOAD_FAST | 9,100 | 0.5% |
| RETURN_VALUE | 7,680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,843,900 | 98.3% |
| POP_JUMP_IF_TRUE | 29,080 | 1.5% |
| EXTENDED_ARG | 3,460 | 0.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 77,140 | 60.7% |
| LOAD_FAST | 45,600 | 35.9% |
| COPY | 4,080 | 3.2% |
| CALL_BUILTIN_O | 80 | 0.1% |
| CALL_LEN | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 82,420 | 64.9% |
| POP_JUMP_IF_TRUE | 37,580 | 29.6% |
| UNARY_NOT | 7,040 | 5.5% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 762,600 | 99.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,420 | 0.2% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 755,980 | 98.9% |
| POP_JUMP_IF_TRUE | 4,180 | 0.5% |
| UNARY_NOT | 3,840 | 0.5% |
| TO_BOOL_NONE | 40 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,020 | 99.3% |
| TO_BOOL | 80 | 0.5% |
| TO_BOOL_LIST | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 17,080 | 99.6% |
| TO_BOOL | 40 | 0.2% |
| POP_JUMP_IF_TRUE | 20 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 9,820 | 77.7% |
| STORE_FAST_LOAD_FAST | 1,440 | 11.4% |
| LOAD_FAST | 1,360 | 10.8% |
| TO_BOOL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 11,280 | 89.2% |
| POP_JUMP_IF_FALSE | 1,360 | 10.8% |


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
| FOR_ITER_LIST | 55,240 | 44.9% |
| RETURN_VALUE | 43,520 | 35.4% |
| FOR_ITER | 22,320 | 18.1% |
| BINARY_SUBSCR_LIST_INT | 1,340 | 1.1% |
| CALL_BUILTIN_FAST | 340 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 91,920 | 74.7% |
| STORE_FAST | 31,100 | 25.3% |


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
|     deferred | 120,280 | 40.1% |
|          hit | 178,260 | 59.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 17.1% |
| Failure | 1,360 | 82.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 740 | 54.4% |
| or | 240 | 17.6% |
| and different types | 100 | 7.4% |
| multiply different types | 80 | 5.9% |
| remainder | 80 | 5.9% |
| add other | 60 | 4.4% |
| floor divide | 40 | 2.9% |
| add different types | 20 | 1.5% |


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
|     deferred | 46,680 | 0.5% |
|          hit | 9,033,300 | 99.5% |
|         miss | 5,080 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,440 | 56.2% |
| Failure | 1,120 | 43.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| seq iter | 620 | 55.4% |
| itertools | 180 | 16.1% |
| set | 120 | 10.7% |
| dict items | 120 | 10.7% |
| dict keys | 40 | 3.6% |
| enumerate | 20 | 1.8% |
| map | 20 | 1.8% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 342,880 | 1.7% |
|          hit | 19,930,160 | 98.2% |
|         miss | 140 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 25,720 | 97.5% |
| Failure | 660 | 2.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 260 | 39.4% |
| metaclass attribute | 160 | 24.2% |
| mutable class | 140 | 21.2% |
| not managed dict | 80 | 12.1% |
| class attr simple | 20 | 3.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 72,300 | 0.2% |
|          hit | 33,142,560 | 99.6% |
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
|     deferred | 760 | 0.4% |
|          hit | 168,100 | 99.4% |

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
|     deferred | 22,300 | 45.9% |
|          hit | 26,040 | 53.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 80 | 36.4% |
| Failure | 140 | 63.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytearray int | 100 | 71.4% |
| out of range | 20 | 14.3% |
| py simple | 20 | 14.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 772,700 | 21.7% |
|          hit | 2,793,560 | 78.3% |
|         miss | 3,740 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 360 | 30.0% |
| Failure | 840 | 70.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| tuple | 380 | 45.2% |
| other | 220 | 26.2% |
| mapping | 120 | 14.3% |
| dict | 80 | 9.5% |
| number | 40 | 4.8% |


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
| Basic | 115,118,220 | 48.4% |
| Not specialized | 23,600,560 | 9.9% |
| Specialized hits | 99,205,620 | 41.7% |
| Specialized misses | 48,860 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 16,447,440 | 91.9% |
| TO_BOOL | 772,700 | 4.3% |
| LOAD_ATTR | 342,880 | 1.9% |
| BINARY_OP | 120,280 | 0.7% |
| LOAD_GLOBAL | 72,300 | 0.4% |
| BINARY_SUBSCR | 61,700 | 0.3% |
| FOR_ITER | 46,680 | 0.3% |
| STORE_SUBSCR | 22,300 | 0.1% |
| COMPARE_OP | 12,600 | 0.1% |
| STORE_ATTR | 760 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 25,000 | 51.2% |
| BINARY_SUBSCR_LIST_INT | 7,120 | 14.6% |
| FOR_ITER_LIST | 5,080 | 10.4% |
| TO_BOOL_NONE | 3,440 | 7.0% |
| BINARY_SUBSCR_STR_INT | 2,880 | 5.9% |
| COMPARE_OP_STR | 2,840 | 5.8% |
| CALL_BUILTIN_FAST | 700 | 1.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 480 | 1.0% |
| LOAD_GLOBAL_BUILTIN | 440 | 0.9% |
| TO_BOOL_LIST | 240 | 0.5% |


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
| Frames pushed | 3,280,360 | 75.5% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 9,841,620 | 16.4% |
| Frees to freelist | 9,844,580 |  |
| Allocations | 50,290,320 | 83.6% |
| Allocations to 512 bytes | 49,929,720 | 83.0% |
| Allocations to 4 kbytes | 314,760 | 0.5% |
| Allocations over 4 kbytes | 45,840 | 0.1% |
| Frees | 70,359,908 |  |
| New values | 9,480 |  |
| Interpreter increfs | 96,434,000 | 59.2% |
| Interpreter decrefs | 117,403,560 | 59.2% |
| Increfs | 66,581,582 | 40.8% |
| Decrefs | 80,834,473 | 40.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 1,129,274 |  |
| Method cache misses | 2,606 |  |
| Method cache collisions | 2,749 |  |
| Method cache dunder hits | 6,367,974 |  |
| Method cache dunder misses | 426 |  |


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
