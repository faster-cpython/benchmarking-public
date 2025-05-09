
# Pystats results

- benchmark: sqlglot_transpile
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 275,250,820 | 24.6% | 24.6% |  |
| LOAD_ATTR_SLOT | 138,101,580 | 12.3% | 37.0% | 2.3% |
| POP_JUMP_IF_FALSE | 59,570,740 | 5.3% | 42.3% |  |
| STORE_ATTR_SLOT | 44,611,060 | 4.0% | 46.3% | 7.4% |
| RESUME_CHECK | 43,788,760 | 3.9% | 50.2% | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 33,399,780 | 3.0% | 53.2% |  |
| STORE_FAST | 27,708,260 | 2.5% | 55.7% |  |
| POP_JUMP_IF_TRUE | 27,672,080 | 2.5% | 58.1% |  |
| LOAD_CONST | 25,734,640 | 2.3% | 60.4% |  |
| CALL_PY_EXACT_ARGS | 22,610,540 | 2.0% | 62.4% | 3.8% |
| RETURN_CONST | 22,466,560 | 2.0% | 64.5% |  |
| RETURN_VALUE | 20,982,540 | 1.9% | 66.3% |  |
| LOAD_GLOBAL_MODULE | 18,662,800 | 1.7% | 68.0% | 0.0% |
| TO_BOOL_BOOL | 17,561,280 | 1.6% | 69.6% | 1.8% |
| LOAD_GLOBAL_BUILTIN | 16,786,940 | 1.5% | 71.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 16,463,320 | 1.5% | 72.5% |  |
| COMPARE_OP_INT | 16,384,280 | 1.5% | 74.0% |  |
| BINARY_OP_ADD_INT | 16,337,760 | 1.5% | 75.5% |  |
| COPY | 16,174,080 | 1.4% | 76.9% |  |
| SWAP | 14,894,360 | 1.3% | 78.2% |  |
| TO_BOOL_ALWAYS_TRUE | 14,636,600 | 1.3% | 79.6% | 15.8% |
| BINARY_SUBSCR_STR_INT | 14,146,500 | 1.3% | 80.8% |  |
| TO_BOOL_NONE | 13,039,100 | 1.2% | 82.0% | 15.8% |
| ENTER_EXECUTOR | 12,890,740 | 1.2% | 83.1% |  |
| POP_TOP | 12,708,440 | 1.1% | 84.3% |  |
| LOAD_ATTR | 12,613,840 | 1.1% | 85.4% |  |
| COMPARE_OP | 11,018,900 | 1.0% | 86.4% |  |
| CALL_PY_WITH_DEFAULTS | 10,940,420 | 1.0% | 87.4% | 0.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 10,884,660 | 1.0% | 88.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 9,446,380 | 0.8% | 89.2% |  |
| JUMP_FORWARD | 8,806,400 | 0.8% | 90.0% |  |
| BINARY_OP_SUBTRACT_INT | 8,785,780 | 0.8% | 90.8% |  |
| TO_BOOL_STR | 8,511,160 | 0.8% | 91.5% | 6.2% |
| CONTAINS_OP | 7,137,940 | 0.6% | 92.2% |  |
| INTERPRETER_EXIT | 6,246,780 | 0.6% | 92.7% |  |
| CALL_ISINSTANCE | 5,312,400 | 0.5% | 93.2% |  |
| CALL_BUILTIN_O | 4,561,780 | 0.4% | 93.6% |  |
| TO_BOOL_INT | 4,474,840 | 0.4% | 94.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 4,066,880 | 0.4% | 94.4% | 17.4% |
| LOAD_ATTR_INSTANCE_VALUE | 3,502,680 | 0.3% | 94.7% | 0.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,302,760 | 0.3% | 95.0% |  |
| PUSH_NULL | 3,144,900 | 0.3% | 95.3% |  |
| GET_ITER | 3,098,060 | 0.3% | 95.5% |  |
| NOP | 3,092,560 | 0.3% | 95.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,040,020 | 0.3% | 96.1% | 61.0% |
| LOAD_DEREF | 2,709,200 | 0.2% | 96.3% |  |
| FOR_ITER | 2,636,620 | 0.2% | 96.6% |  |
| STORE_FAST_STORE_FAST | 2,327,900 | 0.2% | 96.8% |  |
| LOAD_ATTR_PROPERTY | 2,298,580 | 0.2% | 97.0% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,281,360 | 0.2% | 97.2% |  |
| BINARY_SUBSCR_LIST_INT | 2,176,160 | 0.2% | 97.4% | 0.7% |
| LOAD_ATTR_MODULE | 1,868,740 | 0.2% | 97.5% |  |
| BINARY_SLICE | 1,792,000 | 0.2% | 97.7% |  |
| FORMAT_SIMPLE | 1,735,680 | 0.2% | 97.8% |  |
| CALL_BUILTIN_FAST | 1,602,440 | 0.1% | 98.0% |  |
| CALL_LIST_APPEND | 1,530,760 | 0.1% | 98.1% |  |
| BUILD_TUPLE | 1,301,260 | 0.1% | 98.2% |  |
| BUILD_STRING | 1,172,480 | 0.1% | 98.4% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,147,520 | 0.1% | 98.5% | 69.7% |
| BINARY_SUBSCR_DICT | 1,075,040 | 0.1% | 98.5% |  |
| POP_JUMP_IF_NOT_NONE | 998,580 | 0.1% | 98.6% |  |
| COMPARE_OP_STR | 973,460 | 0.1% | 98.7% |  |
| CALL_KW | 967,680 | 0.1% | 98.8% |  |
| POP_JUMP_IF_NONE | 967,680 | 0.1% | 98.9% |  |
| BUILD_LIST | 931,980 | 0.1% | 99.0% |  |
| MAKE_CELL | 875,520 | 0.1% | 99.1% |  |
| CALL | 803,060 | 0.1% | 99.1% |  |
| CALL_TYPE_1 | 793,540 | 0.1% | 99.2% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 788,440 | 0.1% | 99.3% |  |
| CALL_LEN | 788,300 | 0.1% | 99.3% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 706,540 | 0.1% | 99.4% |  |
| BUILD_MAP | 655,360 | 0.1% | 99.5% |  |
| IS_OP | 645,120 | 0.1% | 99.5% |  |
| CALL_FUNCTION_EX | 578,720 | 0.1% | 99.6% |  |
| DICT_MERGE | 563,200 | 0.1% | 99.6% |  |
| YIELD_VALUE | 501,760 | 0.0% | 99.7% |  |
| FOR_ITER_LIST | 451,380 | 0.0% | 99.7% |  |
| FOR_ITER_TUPLE | 400,580 | 0.0% | 99.7% |  |
| EXTENDED_ARG | 302,760 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_O | 276,460 | 0.0% | 99.8% |  |
| RETURN_GENERATOR | 250,880 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 240,640 | 0.0% | 99.8% |  |
| STORE_SUBSCR_DICT | 230,280 | 0.0% | 99.9% |  |
| JUMP_BACKWARD | 178,340 | 0.0% | 99.9% |  |
| LIST_APPEND | 148,480 | 0.0% | 99.9% |  |
| FOR_ITER_GEN | 102,340 | 0.0% | 99.9% |  |
| TO_BOOL | 101,740 | 0.0% | 99.9% |  |
| STORE_DEREF | 87,040 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_TUPLE | 82,180 | 0.0% | 99.9% |  |
| COPY_FREE_VARS | 82,000 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 61,400 | 0.0% | 99.9% |  |
| TO_BOOL_LIST | 61,060 | 0.0% | 99.9% | 36.7% |
| CHECK_EXC_MATCH | 56,320 | 0.0% | 99.9% |  |
| POP_EXCEPT | 56,320 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 56,320 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 40,960 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 40,960 | 0.0% | 100.0% |  |
| SEND_GEN | 40,940 | 0.0% | 100.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 35,840 | 0.0% | 100.0% |  |
| CALL_STR_1 | 35,800 | 0.0% | 100.0% |  |
| UNARY_NOT | 30,720 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 30,720 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 30,720 | 0.0% | 100.0% |  |
| CALL_BUILTIN_CLASS | 30,720 | 0.0% | 100.0% |  |
| LIST_EXTEND | 25,680 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 15,960 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 15,440 | 0.0% | 100.0% |  |
| END_FOR | 15,360 | 0.0% | 100.0% |  |
| DICT_UPDATE | 10,240 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 10,220 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 9,120 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 6,300 | 0.0% | 100.0% |  |
| END_SEND | 5,120 | 0.0% | 100.0% |  |
| GET_YIELD_FROM_ITER | 5,120 | 0.0% | 100.0% |  |
| IMPORT_NAME | 5,120 | 0.0% | 100.0% |  |
| MAP_ADD | 5,120 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 5,100 | 0.0% | 100.0% | 1.2% |
| BINARY_OP_SUBTRACT_FLOAT | 5,100 | 0.0% | 100.0% |  |
| RESUME | 3,540 | 0.0% | 100.0% | 3.4% |
| STORE_ATTR | 2,140 | 0.0% | 100.0% |  |
| BINARY_OP | 760 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 460 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 400 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 240 | 0.0% | 100.0% |  |
| SEND | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_SLOT | 113,058,340 | 10.1% | 10.1% |
| LOAD_ATTR_SLOT LOAD_FAST | 57,861,340 | 5.2% | 15.3% |
| POP_JUMP_IF_FALSE LOAD_FAST | 36,277,020 | 3.2% | 18.5% |
| RESUME_CHECK LOAD_FAST | 31,127,840 | 2.8% | 21.3% |
| STORE_ATTR_SLOT LOAD_FAST | 30,438,420 | 2.7% | 24.0% |
| LOAD_FAST STORE_ATTR_SLOT | 25,343,100 | 2.3% | 26.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 22,066,980 | 2.0% | 28.3% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 18,354,240 | 1.6% | 29.9% |
| STORE_FAST LOAD_FAST | 17,245,980 | 1.5% | 31.5% |
| POP_JUMP_IF_TRUE LOAD_FAST | 16,779,320 | 1.5% | 33.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 16,091,400 | 1.4% | 34.4% |
| LOAD_FAST BINARY_OP_ADD_INT | 14,863,200 | 1.3% | 35.7% |
| LOAD_FAST COPY | 14,632,960 | 1.3% | 37.0% |
| BINARY_OP_ADD_INT SWAP | 14,515,120 | 1.3% | 38.3% |
| COPY LOAD_ATTR_SLOT | 14,515,040 | 1.3% | 39.6% |
| SWAP STORE_ATTR_SLOT | 14,515,040 | 1.3% | 40.9% |
| LOAD_ATTR_SLOT COMPARE_OP_INT | 14,151,560 | 1.3% | 42.2% |
| BINARY_SUBSCR_STR_INT LOAD_FAST | 13,593,560 | 1.2% | 43.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 12,039,620 | 1.1% | 44.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 11,442,560 | 1.0% | 45.5% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 10,893,820 | 1.0% | 46.5% |
| RETURN_CONST POP_TOP | 10,731,520 | 1.0% | 47.4% |
| COMPARE_OP POP_JUMP_IF_FALSE | 10,425,120 | 0.9% | 48.4% |
| LOAD_ATTR_SLOT LOAD_CONST | 10,122,480 | 0.9% | 49.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 10,120,740 | 0.9% | 50.2% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 10,120,480 | 0.9% | 51.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 9,731,940 | 0.9% | 52.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 9,584,940 | 0.9% | 52.8% |
| POP_JUMP_IF_FALSE RETURN_CONST | 9,390,080 | 0.8% | 53.6% |
| STORE_ATTR_SLOT RETURN_CONST | 9,077,640 | 0.8% | 54.5% |
| LOAD_ATTR_SLOT LOAD_ATTR_SLOT | 8,969,080 | 0.8% | 55.3% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 8,830,880 | 0.8% | 56.1% |
| LOAD_ATTR_SLOT TO_BOOL_ALWAYS_TRUE | 8,773,340 | 0.8% | 56.8% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 8,074,040 | 0.7% | 57.6% |
| CALL_METHOD_DESCRIPTOR_FAST STORE_FAST | 7,460,040 | 0.7% | 58.2% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 7,343,220 | 0.7% | 58.9% |
| RETURN_CONST TO_BOOL_NONE | 6,994,740 | 0.6% | 59.5% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 6,981,000 | 0.6% | 60.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_GLOBAL_MODULE | 6,887,760 | 0.6% | 60.7% |
| COMPARE_OP_INT LOAD_FAST | 6,799,340 | 0.6% | 61.4% |
| BINARY_OP_SUBTRACT_INT BINARY_SUBSCR_STR_INT | 6,799,320 | 0.6% | 62.0% |
| LOAD_ATTR_SLOT BINARY_SUBSCR_STR_INT | 6,794,200 | 0.6% | 62.6% |
| POP_TOP LOAD_FAST | 6,446,120 | 0.6% | 63.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 6,334,880 | 0.6% | 63.7% |
| ENTER_EXECUTOR CALL_PY_WITH_DEFAULTS | 6,224,480 | 0.6% | 64.3% |
| CACHE RESUME_CHECK | 6,015,820 | 0.5% | 64.8% |
| LOAD_FAST TO_BOOL_ALWAYS_TRUE | 5,751,660 | 0.5% | 65.3% |
| RETURN_VALUE RETURN_VALUE | 5,744,700 | 0.5% | 65.8% |
| LOAD_FAST COMPARE_OP | 5,683,280 | 0.5% | 66.3% |
| JUMP_FORWARD LOAD_FAST | 5,667,840 | 0.5% | 66.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 5,647,980 | 0.5% | 67.4% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 5,556,760 | 0.5% | 67.9% |
| LOAD_ATTR CALL_PY_EXACT_ARGS | 5,383,180 | 0.5% | 68.3% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 5,340,040 | 0.5% | 68.8% |
| LOAD_ATTR_SLOT CALL_METHOD_DESCRIPTOR_FAST | 5,268,360 | 0.5% | 69.3% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,219,560 | 0.5% | 69.7% |
| LOAD_FAST TO_BOOL_NONE | 5,127,160 | 0.5% | 70.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 5,050,840 | 0.5% | 70.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT LOAD_ATTR_METHOD_NO_DICT | 4,930,360 | 0.4% | 71.1% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 4,884,180 | 0.4% | 71.5% |
| LOAD_ATTR COMPARE_OP | 4,751,800 | 0.4% | 72.0% |
| RETURN_VALUE STORE_FAST | 4,648,940 | 0.4% | 72.4% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 4,602,520 | 0.4% | 72.8% |
| LOAD_ATTR_SLOT TO_BOOL_INT | 4,474,800 | 0.4% | 73.2% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 4,472,520 | 0.4% | 73.6% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 4,469,740 | 0.4% | 74.0% |
| LOAD_ATTR_SLOT TO_BOOL_STR | 4,469,720 | 0.4% | 74.4% |
| POP_JUMP_IF_FALSE JUMP_FORWARD | 4,290,600 | 0.4% | 74.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 4,254,320 | 0.4% | 75.2% |
| LOAD_FAST RETURN_VALUE | 4,096,080 | 0.4% | 75.5% |
| RETURN_VALUE INTERPRETER_EXIT | 4,060,480 | 0.4% | 75.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 3,928,480 | 0.4% | 76.2% |
| LOAD_FAST TO_BOOL_STR | 3,861,840 | 0.3% | 76.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 3,843,120 | 0.3% | 76.9% |
| LOAD_CONST LOAD_FAST | 3,743,000 | 0.3% | 77.3% |
| LOAD_FAST LOAD_CONST | 3,697,200 | 0.3% | 77.6% |
| LOAD_CONST STORE_FAST | 3,691,600 | 0.3% | 77.9% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 3,579,760 | 0.3% | 78.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 3,516,400 | 0.3% | 78.5% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,502,080 | 0.3% | 78.9% |
| CALL_BUILTIN_O RETURN_VALUE | 3,440,640 | 0.3% | 79.2% |
| LOAD_ATTR_INSTANCE_VALUE CALL_BUILTIN_O | 3,440,640 | 0.3% | 79.5% |
| LOAD_FAST TO_BOOL_BOOL | 3,307,380 | 0.3% | 79.8% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 3,302,480 | 0.3% | 80.1% |
| TO_BOOL_NONE POP_JUMP_IF_TRUE | 3,047,560 | 0.3% | 80.3% |
| TO_BOOL_STR POP_JUMP_IF_FALSE | 2,944,520 | 0.3% | 80.6% |
| STORE_FAST LOAD_CONST | 2,826,240 | 0.3% | 80.9% |
| LOAD_FAST CONTAINS_OP | 2,754,560 | 0.2% | 81.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT CONTAINS_OP | 2,749,520 | 0.2% | 81.3% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 2,652,100 | 0.2% | 81.6% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 2,642,940 | 0.2% | 81.8% |
| RESUME_CHECK NOP | 2,636,740 | 0.2% | 82.1% |
| GET_ITER FOR_ITER | 2,622,080 | 0.2% | 82.3% |
| RETURN_VALUE LOAD_FAST | 2,601,200 | 0.2% | 82.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 2,586,340 | 0.2% | 82.8% |
| LOAD_FAST STORE_FAST | 2,386,240 | 0.2% | 83.0% |
| LOAD_DEREF LOAD_ATTR_METHOD_NO_DICT | 2,368,640 | 0.2% | 83.2% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 2,360,180 | 0.2% | 83.4% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 2,325,220 | 0.2% | 83.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 2,298,760 | 0.2% | 83.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,786,860 | 99.7% |
| LOAD_CONST | 5,120 | 0.3% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,786,880 | 99.7% |
| GET_ITER | 5,120 | 0.3% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,015,820 | 96.3% |
| POP_TOP | 230,460 | 3.7% |
| RESUME | 500 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 552,920 | 70.1% |
| ENTER_EXECUTOR | 204,520 | 25.9% |
| LOAD_ATTR_SLOT | 30,960 | 3.9% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 788,440 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,600 | 88.9% |
| LOAD_FAST_LOAD_FAST | 160 | 2.5% |
| BINARY_SUBSCR | 140 | 2.2% |
| LOAD_ATTR | 80 | 1.3% |
| LOAD_FAST | 80 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,400 | 85.7% |
| BINARY_SUBSCR_DICT | 160 | 2.5% |
| BINARY_SUBSCR | 140 | 2.2% |
| BINARY_SUBSCR_LIST_INT | 120 | 1.9% |
| RETURN_VALUE | 80 | 1.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 56,280 | 99.9% |
| LOAD_GLOBAL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 56,320 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 15,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 15,360 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,120 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 752,620 | 43.4% |
| LOAD_FAST | 496,640 | 28.6% |
| RETURN_VALUE | 414,720 | 23.9% |
| LOAD_ATTR_SLOT | 61,400 | 3.5% |
| JUMP_FORWARD | 10,240 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,024,000 | 59.0% |
| BUILD_STRING | 394,240 | 22.7% |
| LOAD_FAST | 317,440 | 18.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,428,420 | 46.1% |
| LOAD_FAST | 921,980 | 29.8% |
| LOAD_ATTR_SLOT | 496,560 | 16.0% |
| BUILD_TUPLE | 184,320 | 5.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 25,540 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 2,622,080 | 84.6% |
| CALL_PY_EXACT_ARGS | 230,200 | 7.4% |
| FOR_ITER_LIST | 194,380 | 6.3% |
| LOAD_FAST_AND_CLEAR | 35,840 | 1.2% |
| FOR_ITER_GEN | 15,300 | 0.5% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,120 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,060,480 | 65.0% |
| RETURN_CONST | 1,807,360 | 28.9% |
| YIELD_VALUE | 378,940 | 6.1% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 240,640 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 199,680 | 83.0% |
| SET_FUNCTION_ATTRIBUTE | 40,960 | 17.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,636,740 | 85.3% |
| POP_JUMP_IF_FALSE | 240,640 | 7.8% |
| STORE_FAST | 215,040 | 7.0% |
| POP_TOP | 80 | 0.0% |
| RESUME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,150,400 | 69.5% |
| LOAD_FAST | 942,080 | 30.5% |
| LOAD_DEREF | 80 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 40,940 | 72.7% |
| POP_TOP | 15,360 | 27.3% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 56,320 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 10,731,520 | 84.4% |
| POP_JUMP_IF_TRUE | 578,560 | 4.6% |
| RESUME_CHECK | 465,780 | 3.7% |
| POP_JUMP_IF_FALSE | 281,600 | 2.2% |
| SWAP | 276,760 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,446,120 | 50.7% |
| JUMP_FORWARD | 2,063,360 | 16.2% |
| RETURN_CONST | 1,745,940 | 13.7% |
| LOAD_CONST | 880,640 | 6.9% |
| ENTER_EXECUTOR | 672,900 | 5.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 40,940 | 72.7% |
| BINARY_SUBSCR_LIST_INT | 15,360 | 27.3% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 56,240 | 99.9% |
| LOAD_GLOBAL | 80 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,787,460 | 56.8% |
| CALL_BUILTIN_FAST | 752,600 | 23.9% |
| LOAD_ATTR_MODULE | 292,180 | 9.3% |
| LOAD_FAST_LOAD_FAST | 168,960 | 5.4% |
| LOAD_ATTR | 41,160 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,101,180 | 35.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 613,180 | 19.5% |
| LOAD_CONST | 537,600 | 17.1% |
| CALL_PY_EXACT_ARGS | 512,700 | 16.3% |
| LOAD_FAST_LOAD_FAST | 307,560 | 9.8% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 199,620 | 79.6% |
| COPY_FREE_VARS | 30,720 | 12.2% |
| CALL_PY_WITH_DEFAULTS | 10,200 | 4.1% |
| CALL | 5,220 | 2.1% |
| CALL_KW | 5,120 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 230,200 | 91.8% |
| GET_ITER | 15,360 | 6.1% |
| GET_YIELD_FROM_ITER | 5,120 | 2.0% |
| CALL | 200 | 0.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,744,700 | 27.4% |
| LOAD_FAST | 4,096,080 | 19.5% |
| CALL_BUILTIN_O | 3,440,640 | 16.4% |
| BINARY_SUBSCR_LIST_INT | 2,140,120 | 10.2% |
| BINARY_SLICE | 1,786,880 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,744,700 | 27.4% |
| STORE_FAST | 4,648,940 | 22.2% |
| INTERPRETER_EXIT | 4,060,480 | 19.4% |
| LOAD_FAST | 2,601,200 | 12.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 839,880 | 4.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 60 | 25.0% |
| CALL_BUILTIN_O | 60 | 25.0% |
| RETURN_VALUE | 40 | 16.7% |
| LOAD_FAST | 40 | 16.7% |
| LOAD_FAST_LOAD_FAST | 40 | 16.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 120 | 50.0% |
| LOAD_FAST | 60 | 25.0% |
| POP_EXCEPT | 20 | 8.3% |
| JUMP_BACKWARD | 20 | 8.3% |
| LOAD_GLOBAL | 20 | 8.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,600 | 88.1% |
| COPY | 6,260 | 6.2% |
| RETURN_CONST | 2,880 | 2.8% |
| CALL | 660 | 0.6% |
| TO_BOOL | 640 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 89,900 | 88.4% |
| POP_JUMP_IF_TRUE | 6,560 | 6.4% |
| TO_BOOL_NONE | 2,080 | 2.0% |
| TO_BOOL_BOOL | 1,440 | 1.4% |
| TO_BOOL | 640 | 0.6% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 30,700 | 99.9% |
| TO_BOOL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 30,720 | 100.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 47.4% |
| LOAD_FAST | 200 | 26.3% |
| LOAD_ATTR | 40 | 5.3% |
| LOAD_FAST_LOAD_FAST | 40 | 5.3% |
| LOAD_ATTR_SLOT | 40 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 160 | 21.1% |
| BINARY_OP_SUBTRACT_INT | 140 | 18.4% |
| STORE_FAST | 120 | 15.8% |
| CALL | 80 | 10.5% |
| SWAP | 80 | 10.5% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 10,240 | 33.3% |
| LOAD_DEREF | 10,240 | 33.3% |
| LOAD_FAST | 10,240 | 33.3% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 742,540 | 79.7% |
| STORE_ATTR_SLOT | 40,900 | 4.4% |
| ENTER_EXECUTOR | 35,400 | 3.8% |
| SWAP | 30,720 | 3.3% |
| LOAD_CONST | 25,600 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 578,560 | 62.1% |
| LOAD_FAST | 102,400 | 11.0% |
| RETURN_VALUE | 97,340 | 10.4% |
| JUMP_FORWARD | 56,320 | 6.0% |
| SWAP | 30,720 | 3.3% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 552,960 | 84.4% |
| POP_JUMP_IF_NOT_NONE | 40,960 | 6.2% |
| RESUME_CHECK | 35,820 | 5.5% |
| BUILD_TUPLE | 10,240 | 1.6% |
| LOAD_FAST | 5,120 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 517,120 | 78.9% |
| STORE_FAST | 81,920 | 12.5% |
| LOAD_GLOBAL_MODULE | 35,800 | 5.5% |
| CALL_FUNCTION_EX | 15,360 | 2.3% |
| SWAP | 5,120 | 0.8% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 778,240 | 66.4% |
| FORMAT_SIMPLE | 394,240 | 33.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 752,640 | 64.2% |
| RETURN_VALUE | 363,520 | 31.0% |
| JUMP_FORWARD | 40,960 | 3.5% |
| LOAD_FAST | 10,240 | 0.9% |
| LOAD_FAST_LOAD_FAST | 5,120 | 0.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 932,560 | 71.7% |
| RETURN_VALUE | 184,320 | 14.2% |
| LOAD_GLOBAL_BUILTIN | 76,840 | 5.9% |
| LOAD_GLOBAL_MODULE | 76,780 | 5.9% |
| LOAD_CONST | 10,240 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 563,200 | 43.3% |
| SWAP | 276,760 | 21.3% |
| GET_ITER | 184,320 | 14.2% |
| CALL_ISINSTANCE | 153,580 | 11.8% |
| CALL_METHOD_DESCRIPTOR_O | 41,040 | 3.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 706,760 | 88.0% |
| LOAD_CONST | 33,520 | 4.2% |
| PUSH_NULL | 16,360 | 2.0% |
| BUILD_LIST | 10,360 | 1.3% |
| LOAD_FAST | 8,000 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 706,640 | 88.0% |
| TO_BOOL_BOOL | 30,680 | 3.8% |
| STORE_FAST | 20,960 | 2.6% |
| RESUME_CHECK | 9,600 | 1.2% |
| CALL_PY_EXACT_ARGS | 5,500 | 0.7% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 563,200 | 97.3% |
| BUILD_MAP | 15,360 | 2.7% |
| CALL_INTRINSIC_1 | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 486,400 | 84.0% |
| RETURN_VALUE | 61,440 | 10.6% |
| RESUME_CHECK | 15,400 | 2.7% |
| LIST_APPEND | 5,120 | 0.9% |
| LOAD_ATTR_METHOD_NO_DICT | 5,080 | 0.9% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 15,360 | 99.5% |
| LIST_EXTEND | 80 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,360 | 99.5% |
| CALL_FUNCTION_EX | 80 | 0.5% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 967,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 542,600 | 56.1% |
| RETURN_VALUE | 322,560 | 33.3% |
| MAKE_CELL | 92,160 | 9.5% |
| GET_ITER | 5,120 | 0.5% |
| RETURN_GENERATOR | 5,120 | 0.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,683,280 | 51.6% |
| LOAD_ATTR | 4,751,800 | 43.1% |
| BUILD_LIST | 578,560 | 5.3% |
| COMPARE_OP | 4,460 | 0.0% |
| LOAD_CONST | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,425,120 | 94.6% |
| POP_JUMP_IF_TRUE | 578,560 | 5.3% |
| STORE_FAST | 10,240 | 0.1% |
| COMPARE_OP | 4,460 | 0.0% |
| COMPARE_OP_INT | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,754,560 | 38.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,749,520 | 38.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 926,740 | 13.0% |
| LOAD_FAST_LOAD_FAST | 701,760 | 9.8% |
| LOAD_CONST | 5,120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,647,980 | 79.1% |
| POP_JUMP_IF_TRUE | 926,760 | 13.0% |
| STORE_FAST | 563,200 | 7.9% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,632,960 | 90.5% |
| RETURN_CONST | 803,840 | 5.0% |
| IS_OP | 302,080 | 1.9% |
| CALL_ISINSTANCE | 261,080 | 1.6% |
| RETURN_VALUE | 127,980 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 14,515,040 | 89.7% |
| TO_BOOL_BOOL | 787,660 | 4.9% |
| TO_BOOL_NONE | 674,720 | 4.2% |
| TO_BOOL_STR | 96,960 | 0.6% |
| TO_BOOL_ALWAYS_TRUE | 67,760 | 0.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 61,180 | 74.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 15,520 | 18.9% |
| CALL | 5,220 | 6.4% |
| CALL_FUNCTION_EX | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 51,200 | 62.4% |
| RETURN_GENERATOR | 30,720 | 37.5% |
| RESUME | 80 | 0.1% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 506,880 | 90.0% |
| RETURN_VALUE | 35,840 | 6.4% |
| BUILD_CONST_KEY_MAP | 10,240 | 1.8% |
| DICT_UPDATE | 10,240 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 563,200 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 10,240 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 6,981,000 | 54.2% |
| JUMP_FORWARD | 2,052,780 | 15.9% |
| STORE_ATTR_SLOT | 807,680 | 6.3% |
| CALL_LIST_APPEND | 705,880 | 5.5% |
| POP_TOP | 672,900 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 6,224,480 | 48.3% |
| LOAD_FAST | 1,370,420 | 10.6% |
| RETURN_CONST | 838,040 | 6.5% |
| CALL_LIST_APPEND | 696,000 | 5.4% |
| LOAD_CONST | 552,640 | 4.3% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 220,860 | 72.9% |
| TO_BOOL_BOOL | 60,640 | 20.0% |
| STORE_FAST | 15,360 | 5.1% |
| TO_BOOL_INT | 5,100 | 1.7% |
| POP_TOP | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 281,600 | 93.0% |
| JUMP_FORWARD | 15,360 | 5.1% |
| POP_JUMP_IF_TRUE | 5,120 | 1.7% |
| JUMP_BACKWARD | 680 | 0.2% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,622,080 | 99.4% |
| JUMP_BACKWARD | 7,040 | 0.3% |
| SWAP | 5,260 | 0.2% |
| FOR_ITER | 2,120 | 0.1% |
| LOAD_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,441,340 | 54.7% |
| STORE_FAST | 1,188,840 | 45.1% |
| FOR_ITER | 2,120 | 0.1% |
| RETURN_CONST | 1,660 | 0.1% |
| LOAD_FAST | 1,240 | 0.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,120 | 100.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 337,920 | 52.4% |
| CALL_TYPE_1 | 302,060 | 46.8% |
| LOAD_GLOBAL_MODULE | 5,120 | 0.8% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 343,040 | 53.2% |
| COPY | 302,080 | 46.8% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 77,820 | 43.6% |
| POP_JUMP_IF_TRUE | 45,580 | 25.6% |
| STORE_ATTR_SLOT | 32,000 | 17.9% |
| POP_TOP | 18,120 | 10.2% |
| STORE_FAST | 1,020 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 86,980 | 48.8% |
| LOAD_FAST | 78,400 | 44.0% |
| FOR_ITER | 7,040 | 3.9% |
| FOR_ITER_LIST | 3,040 | 1.7% |
| FOR_ITER_TUPLE | 1,860 | 1.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 35,820 | 99.9% |
| RESUME | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 35,820 | 99.9% |
| SEND | 20 | 0.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,290,600 | 48.7% |
| POP_TOP | 2,063,360 | 23.4% |
| STORE_FAST | 983,040 | 11.2% |
| RETURN_VALUE | 696,300 | 7.9% |
| ENTER_EXECUTOR | 409,560 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,667,840 | 64.4% |
| ENTER_EXECUTOR | 2,052,780 | 23.3% |
| STORE_FAST | 814,080 | 9.2% |
| LOAD_FAST_LOAD_FAST | 189,440 | 2.2% |
| LOAD_GLOBAL_BUILTIN | 40,920 | 0.5% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 143,360 | 96.6% |
| CALL_FUNCTION_EX | 5,120 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 128,000 | 86.2% |
| CALL_INTRINSIC_1 | 15,360 | 10.3% |
| ENTER_EXECUTOR | 4,780 | 3.2% |
| JUMP_BACKWARD | 340 | 0.2% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 25,600 | 99.7% |
| LOAD_DEREF | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,600 | 99.7% |
| CALL_INTRINSIC_1 | 80 | 0.3% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 11,442,560 | 90.7% |
| LOAD_FAST | 1,062,520 | 8.4% |
| LOAD_ATTR_MODULE | 46,020 | 0.4% |
| LOAD_ATTR | 29,900 | 0.2% |
| LOAD_DEREF | 12,440 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 5,383,180 | 42.7% |
| COMPARE_OP | 4,751,800 | 37.7% |
| LOAD_FAST | 1,017,620 | 8.1% |
| LOAD_GLOBAL_MODULE | 450,360 | 3.6% |
| CALL_PY_WITH_DEFAULTS | 424,840 | 3.4% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 10,122,480 | 39.3% |
| LOAD_FAST | 3,697,200 | 14.4% |
| STORE_FAST | 2,826,240 | 11.0% |
| POP_JUMP_IF_FALSE | 1,295,640 | 5.0% |
| FORMAT_SIMPLE | 1,024,000 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 8,074,040 | 31.4% |
| LOAD_FAST | 3,743,000 | 14.5% |
| STORE_FAST | 3,691,600 | 14.3% |
| COMPARE_OP_INT | 2,207,040 | 8.6% |
| CALL_PY_EXACT_ARGS | 1,641,200 | 6.4% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,228,800 | 45.4% |
| STORE_FAST | 553,440 | 20.4% |
| RESUME_CHECK | 481,180 | 17.8% |
| LOAD_ATTR_METHOD_NO_DICT | 127,940 | 4.7% |
| STORE_DEREF | 87,040 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 2,368,640 | 87.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 118,040 | 4.4% |
| LOAD_ATTR_SLOT | 102,320 | 3.8% |
| CALL_PY_EXACT_ARGS | 86,960 | 3.2% |
| LOAD_ATTR | 12,440 | 0.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 57,861,340 | 21.0% |
| POP_JUMP_IF_FALSE | 36,277,020 | 13.2% |
| RESUME_CHECK | 31,127,840 | 11.3% |
| STORE_ATTR_SLOT | 30,438,420 | 11.1% |
| STORE_FAST | 17,245,980 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 113,058,340 | 41.1% |
| STORE_ATTR_SLOT | 25,343,100 | 9.2% |
| LOAD_ATTR_METHOD_NO_DICT | 18,354,240 | 6.7% |
| BINARY_OP_ADD_INT | 14,863,200 | 5.4% |
| COPY | 14,632,960 | 5.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 35,840 | 87.5% |
| LOAD_FAST_AND_CLEAR | 5,120 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 35,840 | 87.5% |
| LOAD_FAST_AND_CLEAR | 5,120 | 12.5% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 30,680 | 99.9% |
| TO_BOOL | 40 | 0.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,586,340 | 15.7% |
| STORE_ATTR_SLOT | 2,298,760 | 14.0% |
| POP_JUMP_IF_FALSE | 2,176,980 | 13.2% |
| NOP | 2,150,400 | 13.1% |
| LOAD_GLOBAL_BUILTIN | 1,761,200 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 4,602,520 | 28.0% |
| BINARY_SUBSCR_LIST_INT | 2,160,520 | 13.1% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,053,020 | 12.5% |
| CALL_BUILTIN_FAST | 1,500,080 | 9.1% |
| LOAD_ATTR_SLOT | 962,560 | 5.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 2,240 | 24.6% |
| LOAD_ATTR_METHOD_NO_DICT | 1,880 | 20.6% |
| LOAD_FAST | 1,160 | 12.7% |
| STORE_FAST | 1,000 | 11.0% |
| POP_JUMP_IF_FALSE | 680 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,240 | 35.5% |
| LOAD_ATTR | 2,720 | 29.8% |
| LOAD_GLOBAL_BUILTIN | 1,320 | 14.5% |
| LOAD_FAST | 1,200 | 13.2% |
| CALL | 220 | 2.4% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 368,640 | 42.1% |
| CALL_PY_EXACT_ARGS | 266,580 | 30.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 112,160 | 12.8% |
| CALL_KW | 92,160 | 10.5% |
| CALL_PY_WITH_DEFAULTS | 35,780 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 506,740 | 57.9% |
| MAKE_CELL | 368,640 | 42.1% |
| RESUME | 140 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,780 | 93.4% |
| JUMP_BACKWARD | 340 | 6.6% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 10,425,120 | 17.5% |
| TO_BOOL_BOOL | 10,120,740 | 17.0% |
| TO_BOOL_NONE | 9,731,940 | 16.3% |
| COMPARE_OP_INT | 9,584,940 | 16.1% |
| CONTAINS_OP | 5,647,980 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 36,277,020 | 60.9% |
| RETURN_CONST | 9,390,080 | 15.8% |
| JUMP_FORWARD | 4,290,600 | 7.2% |
| LOAD_GLOBAL_BUILTIN | 2,325,220 | 3.9% |
| LOAD_FAST_LOAD_FAST | 2,176,980 | 3.7% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 942,080 | 97.4% |
| LOAD_ATTR_INSTANCE_VALUE | 20,480 | 2.1% |
| BINARY_SUBSCR_LIST_INT | 5,100 | 0.5% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 926,720 | 95.8% |
| LOAD_GLOBAL_BUILTIN | 35,800 | 3.7% |
| LOAD_FAST_LOAD_FAST | 5,120 | 0.5% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 993,460 | 99.5% |
| LOAD_ATTR_SLOT | 5,100 | 0.5% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 880,640 | 88.2% |
| LOAD_GLOBAL_BUILTIN | 76,820 | 7.7% |
| BUILD_MAP | 40,960 | 4.1% |
| BUILD_LIST | 120 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 10,120,480 | 36.6% |
| TO_BOOL_BOOL | 7,343,220 | 26.5% |
| TO_BOOL_STR | 5,556,760 | 20.1% |
| TO_BOOL_NONE | 3,047,560 | 11.0% |
| CONTAINS_OP | 926,760 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,779,320 | 60.6% |
| ENTER_EXECUTOR | 6,981,000 | 25.2% |
| LOAD_GLOBAL_BUILTIN | 1,899,480 | 6.9% |
| RETURN_CONST | 1,085,440 | 3.9% |
| POP_TOP | 578,560 | 2.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,390,080 | 41.8% |
| STORE_ATTR_SLOT | 9,077,640 | 40.4% |
| POP_TOP | 1,745,940 | 7.8% |
| POP_JUMP_IF_TRUE | 1,085,440 | 4.8% |
| ENTER_EXECUTOR | 838,040 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,731,520 | 47.8% |
| TO_BOOL_NONE | 6,994,740 | 31.1% |
| INTERPRETER_EXIT | 1,807,360 | 8.0% |
| RETURN_VALUE | 890,880 | 4.0% |
| COPY | 803,840 | 3.6% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 20 | 50.0% |
| LOAD_CONST | 20 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 20 | 50.0% |
| SEND_GEN | 20 | 50.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 40,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,720 | 75.0% |
| CALL_PY_EXACT_ARGS | 10,200 | 24.9% |
| CALL | 40 | 0.1% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,220 | 57.0% |
| LOAD_FAST_LOAD_FAST | 760 | 35.5% |
| SWAP | 160 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,240 | 57.9% |
| LOAD_FAST | 300 | 14.0% |
| LOAD_FAST_LOAD_FAST | 180 | 8.4% |
| RETURN_CONST | 120 | 5.6% |
| LOAD_CONST | 100 | 4.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 87,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 87,040 | 100.0% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 7,460,040 | 26.9% |
| RETURN_VALUE | 4,648,940 | 16.8% |
| LOAD_CONST | 3,691,600 | 13.3% |
| LOAD_FAST | 2,386,240 | 8.6% |
| FOR_ITER | 1,188,840 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,245,980 | 62.2% |
| LOAD_CONST | 2,826,240 | 10.2% |
| LOAD_FAST_LOAD_FAST | 2,586,340 | 9.3% |
| LOAD_GLOBAL_BUILTIN | 2,360,180 | 8.5% |
| JUMP_FORWARD | 983,040 | 3.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 15,940 | 99.9% |
| FOR_ITER | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 15,920 | 99.7% |
| TO_BOOL | 40 | 0.3% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,281,360 | 98.0% |
| UNPACK_SEQUENCE_TUPLE | 46,360 | 2.0% |
| UNPACK_SEQUENCE | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,362,940 | 58.5% |
| LOAD_GLOBAL_BUILTIN | 846,660 | 36.4% |
| LOAD_GLOBAL_MODULE | 71,820 | 3.1% |
| STORE_FAST | 46,400 | 2.0% |
| LOAD_GLOBAL | 80 | 0.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 14,515,120 | 97.5% |
| BUILD_TUPLE | 276,760 | 1.9% |
| LOAD_FAST_AND_CLEAR | 35,840 | 0.2% |
| BUILD_LIST | 30,720 | 0.2% |
| FOR_ITER_LIST | 30,660 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 14,515,040 | 97.5% |
| POP_TOP | 276,760 | 1.9% |
| BUILD_LIST | 30,720 | 0.2% |
| STORE_FAST | 30,720 | 0.2% |
| FOR_ITER_LIST | 30,580 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 240 | 60.0% |
| RETURN_VALUE | 80 | 20.0% |
| YIELD_VALUE | 40 | 10.0% |
| CALL | 20 | 5.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 180 | 45.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 140 | 35.0% |
| UNPACK_SEQUENCE_TUPLE | 60 | 15.0% |
| STORE_FAST | 20 | 5.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 266,400 | 53.1% |
| RETURN_VALUE | 107,520 | 21.4% |
| ENTER_EXECUTOR | 81,440 | 16.2% |
| YIELD_VALUE | 35,840 | 7.1% |
| BUILD_TUPLE | 10,560 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 378,940 | 75.5% |
| UNPACK_SEQUENCE_TUPLE | 71,600 | 14.3% |
| YIELD_VALUE | 35,840 | 7.1% |
| STORE_FAST | 15,340 | 3.1% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,820 | 51.4% |
| CACHE | 500 | 14.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 500 | 14.1% |
| POP_TOP | 160 | 4.5% |
| MAKE_CELL | 140 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,540 | 71.8% |
| LOAD_GLOBAL | 320 | 9.0% |
| LOAD_DEREF | 180 | 5.1% |
| POP_TOP | 140 | 4.0% |
| LOAD_CONST | 140 | 4.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,100 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,863,200 | 91.0% |
| LOAD_CONST | 1,474,400 | 9.0% |
| BINARY_OP | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 14,515,120 | 88.8% |
| STORE_FAST | 1,110,980 | 6.8% |
| CALL_PY_EXACT_ARGS | 711,640 | 4.4% |
| CALL | 20 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 5,080 | 99.6% |
| BINARY_OP | 20 | 0.4% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,074,040 | 91.9% |
| CALL_LEN | 706,520 | 8.0% |
| LOAD_ATTR_SLOT | 5,080 | 0.1% |
| BINARY_OP | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 6,799,320 | 77.4% |
| CALL_PY_EXACT_ARGS | 721,800 | 8.2% |
| LOAD_CONST | 706,540 | 8.0% |
| LOAD_FAST | 552,940 | 6.3% |
| COMPARE_OP_INT | 5,080 | 0.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 552,920 | 51.4% |
| LOAD_ATTR_SLOT | 389,000 | 36.2% |
| CALL_BUILTIN_O | 76,760 | 7.1% |
| LOAD_CONST | 35,800 | 3.3% |
| LOAD_FAST | 10,200 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 803,800 | 74.8% |
| LOAD_FAST_LOAD_FAST | 102,380 | 9.5% |
| RETURN_VALUE | 46,040 | 4.3% |
| PUSH_EXC_INFO | 40,940 | 3.8% |
| PUSH_NULL | 35,820 | 3.3% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,200 | 99.8% |
| BINARY_SUBSCR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,220 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,160,520 | 99.3% |
| LOAD_CONST | 15,240 | 0.7% |
| BINARY_SUBSCR_LIST_INT | 280 | 0.0% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,140,120 | 98.3% |
| PUSH_EXC_INFO | 15,360 | 0.7% |
| PUSH_NULL | 5,100 | 0.2% |
| LOAD_FAST | 5,100 | 0.2% |
| LOAD_FAST_LOAD_FAST | 5,100 | 0.2% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 6,799,320 | 48.1% |
| LOAD_ATTR_SLOT | 6,794,200 | 48.0% |
| LOAD_FAST | 552,920 | 3.9% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,593,560 | 96.1% |
| STORE_FAST | 552,940 | 3.9% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 613,180 | 53.4% |
| LOAD_FAST | 473,100 | 41.2% |
| LOAD_ATTR_SLOT | 35,760 | 3.1% |
| CALL_PY_EXACT_ARGS | 15,060 | 1.3% |
| LOAD_ATTR | 10,160 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,004,260 | 87.5% |
| MAKE_CELL | 112,160 | 9.8% |
| COPY_FREE_VARS | 15,520 | 1.4% |
| CALL_PY_EXACT_ARGS | 15,080 | 1.3% |
| RESUME | 500 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_FAST | 20,440 | 66.5% |
| LOAD_FAST | 5,120 | 16.7% |
| LOAD_ATTR | 5,080 | 16.5% |
| CALL | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20,460 | 66.6% |
| GET_ITER | 5,160 | 16.8% |
| STORE_FAST | 5,100 | 16.6% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,500,080 | 93.6% |
| LOAD_CONST | 61,360 | 3.8% |
| LOAD_GLOBAL_BUILTIN | 35,800 | 2.2% |
| LOAD_DEREF | 5,080 | 0.3% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 793,520 | 49.5% |
| PUSH_NULL | 752,600 | 47.0% |
| STORE_FAST | 35,820 | 2.2% |
| CALL_BUILTIN_CLASS | 20,440 | 1.3% |
| TO_BOOL | 40 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 706,520 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 706,540 | 100.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 3,440,640 | 75.4% |
| LOAD_FAST | 1,105,680 | 24.2% |
| RETURN_VALUE | 15,320 | 0.3% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,440,640 | 75.4% |
| TO_BOOL_BOOL | 757,720 | 16.6% |
| STORE_FAST | 189,420 | 4.2% |
| STORE_SUBSCR_DICT | 81,800 | 1.8% |
| BINARY_SUBSCR_DICT | 76,760 | 1.7% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,642,940 | 49.8% |
| LOAD_GLOBAL_MODULE | 1,138,320 | 21.4% |
| LOAD_ATTR_MODULE | 1,116,000 | 21.0% |
| LOAD_ATTR_SLOT | 225,240 | 4.2% |
| BUILD_TUPLE | 153,580 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,050,840 | 95.1% |
| COPY | 261,080 | 4.9% |
| TO_BOOL | 480 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 777,960 | 98.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 5,080 | 0.6% |
| LOAD_ATTR_SLOT | 5,080 | 0.6% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 706,520 | 89.6% |
| STORE_FAST | 40,900 | 5.2% |
| LOAD_CONST | 20,460 | 2.6% |
| COMPARE_OP_INT | 10,160 | 1.3% |
| LOAD_FAST | 5,100 | 0.6% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 706,640 | 46.2% |
| ENTER_EXECUTOR | 696,000 | 45.5% |
| LOAD_FAST | 117,960 | 7.7% |
| RETURN_VALUE | 10,160 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 706,540 | 46.2% |
| ENTER_EXECUTOR | 705,880 | 46.1% |
| LOAD_FAST | 81,880 | 5.3% |
| RETURN_CONST | 35,820 | 2.3% |
| JUMP_BACKWARD | 640 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 5,268,360 | 55.8% |
| LOAD_FAST | 2,652,100 | 28.1% |
| LOAD_CONST | 460,560 | 4.9% |
| LOAD_ATTR | 419,760 | 4.4% |
| LOAD_ATTR_METHOD_NO_DICT | 414,960 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,460,040 | 79.0% |
| CALL_PY_WITH_DEFAULTS | 1,546,160 | 16.4% |
| TO_BOOL_BOOL | 266,200 | 2.8% |
| RETURN_VALUE | 133,080 | 1.4% |
| GET_ITER | 25,540 | 0.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 30,680 | 50.0% |
| LOAD_ATTR_SLOT | 30,680 | 50.0% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 30,700 | 50.0% |
| STORE_FAST | 30,700 | 50.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,302,480 | 100.0% |
| CALL | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 1,428,420 | 43.2% |
| TO_BOOL_BOOL | 716,680 | 21.7% |
| CALL_PY_EXACT_ARGS | 701,720 | 21.2% |
| LOAD_GLOBAL_MODULE | 409,560 | 12.4% |
| UNPACK_SEQUENCE_TUPLE | 10,520 | 0.3% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 230,200 | 83.3% |
| BUILD_TUPLE | 41,040 | 14.8% |
| LOAD_FAST | 5,080 | 1.8% |
| CALL | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 209,840 | 75.9% |
| POP_TOP | 41,060 | 14.9% |
| STORE_FAST | 20,460 | 7.4% |
| LOAD_CONST | 5,100 | 1.8% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 5,383,180 | 23.8% |
| LOAD_FAST | 5,219,560 | 23.1% |
| LOAD_ATTR_METHOD_NO_DICT | 3,843,120 | 17.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,134,400 | 9.4% |
| LOAD_CONST | 1,641,200 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 22,066,980 | 97.6% |
| MAKE_CELL | 266,580 | 1.2% |
| RETURN_GENERATOR | 199,620 | 0.9% |
| COPY_FREE_VARS | 61,180 | 0.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 15,060 | 0.1% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 6,224,480 | 56.9% |
| LOAD_ATTR_METHOD_NO_DICT | 1,658,880 | 15.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,546,160 | 14.1% |
| LOAD_FAST | 809,000 | 7.4% |
| LOAD_ATTR | 424,840 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,893,820 | 99.6% |
| MAKE_CELL | 35,780 | 0.3% |
| RETURN_GENERATOR | 10,200 | 0.1% |
| CALL_PY_EXACT_ARGS | 580 | 0.0% |
| RESUME | 40 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,760 | 99.9% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 35,800 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 793,480 | 100.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 302,060 | 38.1% |
| LOAD_GLOBAL_BUILTIN | 302,040 | 38.1% |
| STORE_FAST | 189,420 | 23.9% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 14,151,560 | 86.4% |
| LOAD_CONST | 2,207,040 | 13.5% |
| LOAD_FAST_LOAD_FAST | 10,160 | 0.1% |
| CALL_LEN | 10,160 | 0.1% |
| BINARY_OP_SUBTRACT_INT | 5,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,584,940 | 58.5% |
| LOAD_FAST | 6,799,340 | 41.5% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 732,400 | 75.2% |
| LOAD_CONST | 107,560 | 11.0% |
| LOAD_FAST | 92,360 | 9.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 40,920 | 4.2% |
| COMPARE_OP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 973,460 | 100.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 86,980 | 85.0% |
| GET_ITER | 15,300 | 15.0% |
| FOR_ITER | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 86,980 | 85.0% |
| POP_TOP | 15,300 | 15.0% |
| RESUME | 60 | 0.1% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 194,380 | 43.1% |
| ENTER_EXECUTOR | 192,420 | 42.6% |
| LOAD_FAST | 30,660 | 6.8% |
| SWAP | 30,580 | 6.8% |
| JUMP_BACKWARD | 3,040 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 193,540 | 42.9% |
| STORE_FAST | 164,780 | 36.5% |
| RETURN_CONST | 35,820 | 7.9% |
| SWAP | 30,660 | 6.8% |
| LOAD_FAST | 15,340 | 3.4% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 300 | 65.2% |
| ENTER_EXECUTOR | 80 | 17.4% |
| GET_ITER | 60 | 13.0% |
| FOR_ITER | 20 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 380 | 82.6% |
| LOAD_FAST | 80 | 17.4% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 199,620 | 49.8% |
| ENTER_EXECUTOR | 199,040 | 49.7% |
| JUMP_BACKWARD | 1,860 | 0.5% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 199,680 | 49.8% |
| STORE_FAST | 184,960 | 46.2% |
| STORE_FAST_LOAD_FAST | 15,940 | 4.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,502,080 | 100.0% |
| LOAD_ATTR_INSTANCE_VALUE | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 3,440,640 | 98.2% |
| RETURN_VALUE | 20,480 | 0.6% |
| LOAD_FAST | 20,480 | 0.6% |
| POP_JUMP_IF_NONE | 20,480 | 0.6% |
| LOAD_ATTR_INSTANCE_VALUE | 600 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,354,240 | 55.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 4,930,360 | 14.8% |
| LOAD_ATTR_SLOT | 4,884,180 | 14.6% |
| LOAD_DEREF | 2,368,640 | 7.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,249,160 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,091,400 | 48.2% |
| LOAD_GLOBAL_MODULE | 6,887,760 | 20.6% |
| CALL_PY_EXACT_ARGS | 3,843,120 | 11.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 3,302,480 | 9.9% |
| CALL_PY_WITH_DEFAULTS | 1,658,880 | 5.0% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,928,480 | 96.6% |
| LOAD_DEREF | 118,040 | 2.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 13,320 | 0.3% |
| CALL_FUNCTION_EX | 5,080 | 0.1% |
| LOAD_ATTR | 1,960 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,516,400 | 86.5% |
| LOAD_CONST | 399,160 | 9.8% |
| LOAD_FAST_LOAD_FAST | 66,500 | 1.6% |
| CALL_PY_WITH_DEFAULTS | 35,640 | 0.9% |
| CALL_PY_EXACT_ARGS | 25,520 | 0.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,862,760 | 99.7% |
| LOAD_FAST | 5,100 | 0.3% |
| LOAD_ATTR | 880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,116,000 | 59.7% |
| PUSH_NULL | 292,180 | 15.6% |
| LOAD_FAST | 214,920 | 11.5% |
| LOAD_FAST_LOAD_FAST | 153,400 | 8.2% |
| LOAD_ATTR | 46,020 | 2.5% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,830,880 | 81.1% |
| LOAD_FAST_LOAD_FAST | 2,053,020 | 18.9% |
| LOAD_ATTR | 760 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,930,360 | 45.3% |
| CONTAINS_OP | 2,749,520 | 25.3% |
| CALL_PY_EXACT_ARGS | 2,134,400 | 19.6% |
| STORE_FAST | 701,420 | 6.4% |
| LOAD_FAST | 296,900 | 2.7% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,077,960 | 68.4% |
| LOAD_FAST_LOAD_FAST | 481,340 | 15.8% |
| ENTER_EXECUTOR | 445,380 | 14.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 34,940 | 1.1% |
| LOAD_ATTR | 400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,249,160 | 41.1% |
| CONTAINS_OP | 926,740 | 30.5% |
| FORMAT_SIMPLE | 752,620 | 24.8% |
| LOAD_FAST | 45,900 | 1.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 34,940 | 1.1% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,252,280 | 98.0% |
| LOAD_FAST_LOAD_FAST | 40,920 | 1.8% |
| LOAD_ATTR_SLOT | 5,080 | 0.2% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,298,580 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,058,340 | 81.9% |
| COPY | 14,515,040 | 10.5% |
| LOAD_ATTR_SLOT | 8,969,080 | 6.5% |
| LOAD_FAST_LOAD_FAST | 962,560 | 0.7% |
| ENTER_EXECUTOR | 491,420 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,861,340 | 41.9% |
| COMPARE_OP_INT | 14,151,560 | 10.2% |
| LOAD_CONST | 10,122,480 | 7.3% |
| LOAD_ATTR_SLOT | 8,969,080 | 6.5% |
| TO_BOOL_ALWAYS_TRUE | 8,773,340 | 6.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,254,320 | 25.3% |
| LOAD_FAST | 3,579,760 | 21.3% |
| STORE_FAST | 2,360,180 | 14.1% |
| POP_JUMP_IF_FALSE | 2,325,220 | 13.9% |
| POP_JUMP_IF_TRUE | 1,899,480 | 11.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,039,620 | 71.7% |
| CALL_ISINSTANCE | 2,642,940 | 15.7% |
| LOAD_FAST_LOAD_FAST | 1,761,200 | 10.5% |
| LOAD_GLOBAL_BUILTIN | 174,140 | 1.0% |
| BUILD_TUPLE | 76,840 | 0.5% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 6,887,760 | 36.9% |
| LOAD_FAST | 6,334,880 | 33.9% |
| RESUME_CHECK | 2,186,000 | 11.7% |
| POP_JUMP_IF_FALSE | 742,520 | 4.0% |
| LOAD_ATTR_SLOT | 732,280 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 11,442,560 | 61.3% |
| LOAD_FAST | 2,273,320 | 12.2% |
| LOAD_ATTR_MODULE | 1,862,760 | 10.0% |
| LOAD_FAST_LOAD_FAST | 1,500,380 | 8.0% |
| CALL_ISINSTANCE | 1,138,320 | 6.1% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 22,066,980 | 50.4% |
| CALL_PY_WITH_DEFAULTS | 10,893,820 | 24.9% |
| CACHE | 6,015,820 | 13.7% |
| LOAD_ATTR_PROPERTY | 2,298,580 | 5.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,004,260 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,127,840 | 71.1% |
| LOAD_GLOBAL_BUILTIN | 4,254,320 | 9.7% |
| NOP | 2,636,740 | 6.0% |
| LOAD_GLOBAL_MODULE | 2,186,000 | 5.0% |
| LOAD_FAST_LOAD_FAST | 1,628,100 | 3.7% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 35,820 | 87.5% |
| LOAD_CONST | 5,100 | 12.5% |
| SEND | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 35,840 | 87.5% |
| POP_TOP | 5,100 | 12.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,343,100 | 56.8% |
| SWAP | 14,515,040 | 32.5% |
| LOAD_FAST_LOAD_FAST | 4,602,520 | 10.3% |
| ENTER_EXECUTOR | 86,760 | 0.2% |
| STORE_ATTR_SLOT | 62,400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,438,420 | 68.2% |
| RETURN_CONST | 9,077,640 | 20.3% |
| LOAD_FAST_LOAD_FAST | 2,298,760 | 5.2% |
| LOAD_CONST | 931,740 | 2.1% |
| ENTER_EXECUTOR | 807,680 | 1.8% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 81,800 | 35.5% |
| LOAD_FAST | 76,760 | 33.3% |
| RETURN_VALUE | 66,520 | 28.9% |
| LOAD_FAST_LOAD_FAST | 5,080 | 2.2% |
| STORE_SUBSCR | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 76,760 | 33.3% |
| ENTER_EXECUTOR | 66,220 | 28.8% |
| LOAD_FAST | 46,020 | 20.0% |
| POP_EXCEPT | 40,940 | 17.8% |
| JUMP_BACKWARD | 320 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 8,773,340 | 59.9% |
| LOAD_FAST | 5,751,660 | 39.3% |
| COPY | 67,760 | 0.5% |
| TO_BOOL_NONE | 22,440 | 0.2% |
| TO_BOOL_ALWAYS_TRUE | 21,140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 10,120,480 | 69.1% |
| POP_JUMP_IF_FALSE | 4,472,520 | 30.6% |
| TO_BOOL_NONE | 22,460 | 0.2% |
| TO_BOOL_ALWAYS_TRUE | 21,140 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 5,340,040 | 30.4% |
| CALL_ISINSTANCE | 5,050,840 | 28.8% |
| LOAD_FAST | 3,307,380 | 18.8% |
| CALL_BUILTIN_FAST | 793,520 | 4.5% |
| COPY | 787,660 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 10,120,740 | 57.6% |
| POP_JUMP_IF_TRUE | 7,343,220 | 41.8% |
| EXTENDED_ARG | 60,640 | 0.3% |
| UNARY_NOT | 30,700 | 0.2% |
| TO_BOOL_NONE | 5,980 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 4,474,800 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,469,740 | 99.9% |
| EXTENDED_ARG | 5,100 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,060 | 57.4% |
| COPY | 25,520 | 41.8% |
| TO_BOOL_NONE | 420 | 0.7% |
| TO_BOOL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 56,400 | 92.4% |
| POP_JUMP_IF_FALSE | 4,240 | 6.9% |
| TO_BOOL_NONE | 420 | 0.7% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 6,994,740 | 53.6% |
| LOAD_FAST | 5,127,160 | 39.3% |
| COPY | 674,720 | 5.2% |
| LOAD_ATTR_SLOT | 140,300 | 1.1% |
| LOAD_FAST_CHECK | 30,680 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 9,731,940 | 74.6% |
| POP_JUMP_IF_TRUE | 3,047,560 | 23.4% |
| EXTENDED_ARG | 220,860 | 1.7% |
| TO_BOOL_ALWAYS_TRUE | 22,440 | 0.2% |
| TO_BOOL_STR | 9,860 | 0.1% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 4,469,720 | 52.5% |
| LOAD_FAST | 3,861,840 | 45.4% |
| COPY | 96,960 | 1.1% |
| RETURN_VALUE | 56,240 | 0.7% |
| STORE_FAST_LOAD_FAST | 15,920 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,556,760 | 65.3% |
| POP_JUMP_IF_FALSE | 2,944,520 | 34.6% |
| TO_BOOL_NONE | 9,880 | 0.1% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 71,600 | 87.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,520 | 12.8% |
| UNPACK_SEQUENCE | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 46,360 | 56.4% |
| STORE_FAST | 35,820 | 43.6% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,441,340 | 63.2% |
| RETURN_VALUE | 839,880 | 36.8% |
| UNPACK_SEQUENCE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,281,360 | 100.0% |


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
|     deferred | 440 | 0.0% |
|          hit | 25,922,120 | 100.0% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
| Failure | 0 | 0.0% |


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
|     deferred | 21,160 | 0.1% |
|          hit | 17,392,280 | 99.9% |
|         miss | 15,640 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 640 | 82.1% |
| Failure | 140 | 17.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 140 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,446,860 | 3.5% |
|          hit | 67,902,080 | 96.5% |
|         miss | 1,686,220 | 2.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40,400 | 95.2% |
| Failure | 2,020 | 4.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bound method | 460 | 22.8% |
| no dict | 360 | 17.8% |
| cfunc noargs | 300 | 14.9% |
| code complex parameters | 280 | 13.9% |
| metaclass | 280 | 13.9% |
| meth descr varargs | 180 | 8.9% |
| class no vectorcall | 160 | 7.9% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 11,013,940 | 37.1% |
|          hit | 18,631,180 | 62.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 500 | 10.1% |
| Failure | 4,460 | 89.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 4,120 | 92.4% |
| different types | 340 | 7.6% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,634,060 | 73.3% |
|          hit | 954,760 | 26.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 17.2% |
| Failure | 2,120 | 82.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 1,040 | 49.1% |
| dict keys | 440 | 20.8% |
| ascii string | 360 | 17.0% |
| enumerate | 280 | 13.2% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 18,287,080 | 7.9% |
|        deopt | 633,420 | 0.3% |
|          hit | 212,558,760 | 92.0% |
|         miss | 5,819,340 | 2.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 122,380 | 83.8% |
| Failure | 23,720 | 16.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 19,600 | 82.6% |
| method | 3,240 | 13.7% |
| mutable class | 600 | 2.5% |
| overridden | 140 | 0.6% |
| class method obj | 140 | 0.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,720 | 0.0% |
|          hit | 35,445,500 | 100.0% |
|         miss | 4,240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,640 | 100.0% |
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
|     deferred | 20 | 0.0% |
|          hit | 40,940 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,245,060 | 6.6% |
|          hit | 45,799,420 | 93.3% |
|         miss | 3,306,560 | 6.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 63,640 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 120 | 0.1% |
|          hit | 230,280 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 120 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,245,580 | 8.2% |
|          hit | 58,728,820 | 91.7% |
|         miss | 5,247,600 | 8.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 103,120 | 99.4% |
| Failure | 640 | 0.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 360 | 56.2% |
| other | 140 | 21.9% |
| dict | 140 | 21.9% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 200 | 0.0% |
|          hit | 5,186,360 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 493,541,980 | 44.1% |
| Not specialized | 118,194,240 | 10.6% |
| Specialized hits | 490,641,860 | 43.9% |
| Specialized misses | 16,079,780 | 1.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 18,287,080 | 42.6% |
| COMPARE_OP | 11,013,940 | 25.7% |
| TO_BOOL | 5,245,580 | 12.2% |
| STORE_ATTR | 3,245,060 | 7.6% |
| FOR_ITER | 2,634,060 | 6.1% |
| CALL | 2,446,860 | 5.7% |
| BINARY_SUBSCR | 21,160 | 0.0% |
| LOAD_GLOBAL | 8,720 | 0.0% |
| BINARY_OP | 440 | 0.0% |
| UNPACK_SEQUENCE | 200 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 3,306,560 | 20.6% |
| LOAD_ATTR_SLOT | 3,228,580 | 20.1% |
| TO_BOOL_ALWAYS_TRUE | 2,313,720 | 14.4% |
| TO_BOOL_NONE | 2,065,740 | 12.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,853,340 | 11.5% |
| CALL_PY_EXACT_ARGS | 855,140 | 5.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 800,340 | 5.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 706,480 | 4.4% |
| TO_BOOL_STR | 524,540 | 3.3% |
| TO_BOOL_BOOL | 321,200 | 2.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 6,246,780 | 13.9% |
| Calls to Python functions inlined | 38,614,820 | 86.1% |
| Calls via PyEval_EvalFrame (total) | 6,246,780 | 13.9% |
| Calls via PyEval_EvalFrame (vector) | 5,637,440 | 12.6% |
| Calls via PyEval_EvalFrame (generator) | 609,340 | 1.4% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 5,637,440 | 12.6% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 563,220 | 1.3% |
| Calls via PyEval_EvalFrame (function ex) | 15,520 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 3,440,940 | 7.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 56,320 | 0.1% |
| Frames pushed | 44,108,960 | 98.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 9,620,620 | 20.3% |
| Frees to freelist | 9,627,720 |  |
| Allocations | 37,812,520 | 79.7% |
| Allocations to 512 bytes | 37,776,400 | 79.6% |
| Allocations to 4 kbytes | 36,120 | 0.1% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 37,711,949 |  |
| New values | 855,040 |  |
| Interpreter increfs | 540,279,080 | 79.2% |
| Interpreter decrefs | 606,799,440 | 83.5% |
| Increfs | 141,768,735 | 20.8% |
| Decrefs | 119,714,518 | 16.5% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 34,199,384 |  |
| Method cache misses | 1,280,256 |  |
| Method cache collisions | 1,395,410 |  |
| Method cache dunder hits | 14,767,898 |  |
| Method cache dunder misses | 117,882 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 2,320 | 601,320 | 11,923,080 |
| 1 | 220 | 633,060 | 5,614,920 |
| 2 | 20 | 46,200 | 4,289,400 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 1,660 |  |
| Traces created | 1,080 | 65.1% |
| Trace stack overflow | 220 | 13.3% |
| Trace stack underflow | 20 | 1.2% |
| Trace too long | 0 | 0.0% |
| Trace too short | 580 | 34.9% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 40 | 2.4% |
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
| <= 16 | 200 | 18.5% |
| <= 32 | 280 | 25.9% |
| <= 64 | 300 | 27.8% |
| <= 128 | 160 | 14.8% |
| <= 256 | 80 | 7.4% |
| <= 512 | 60 | 5.6% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 100 | 9.3% |
| <= 16 | 180 | 16.7% |
| <= 32 | 360 | 33.3% |
| <= 64 | 60 | 5.6% |
| <= 128 | 20 | 1.9% |


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
| FOR_ITER_GEN | 580 |
| CALL_PY_WITH_DEFAULTS | 180 |
| CALL | 40 |
| YIELD_VALUE | 40 |
| CALL_LIST_APPEND | 40 |
| BINARY_OP_INPLACE_ADD_UNICODE | 20 |


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
