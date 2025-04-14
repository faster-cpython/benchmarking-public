
# Pystats results

- benchmark: sqlglot_optimize
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 132,935,180 | 17.1% | 17.1% |  |
| LOAD_GLOBAL_BUILTIN | 57,272,100 | 7.4% | 24.5% | 0.0% |
| RESUME_CHECK | 40,651,720 | 5.2% | 29.7% | 0.0% |
| POP_JUMP_IF_FALSE | 38,105,980 | 4.9% | 34.6% |  |
| TO_BOOL_BOOL | 35,924,260 | 4.6% | 39.3% | 0.0% |
| STORE_FAST | 31,873,340 | 4.1% | 43.4% |  |
| CALL_ISINSTANCE | 28,680,900 | 3.7% | 47.1% |  |
| LOAD_GLOBAL_MODULE | 28,301,980 | 3.6% | 50.7% | 0.0% |
| RETURN_VALUE | 26,912,300 | 3.5% | 54.2% |  |
| LOAD_ATTR_SLOT | 19,776,400 | 2.5% | 56.7% | 37.2% |
| CALL_PY_EXACT_ARGS | 19,089,940 | 2.5% | 59.2% | 2.0% |
| LOAD_ATTR_METHOD_NO_DICT | 17,993,940 | 2.3% | 61.5% | 0.0% |
| ENTER_EXECUTOR | 17,432,420 | 2.2% | 63.7% |  |
| POP_TOP | 16,938,740 | 2.2% | 65.9% |  |
| LOAD_CONST | 13,135,560 | 1.7% | 67.6% |  |
| BUILD_TUPLE | 12,394,920 | 1.6% | 69.2% |  |
| LOAD_FAST_LOAD_FAST | 11,588,300 | 1.5% | 70.7% |  |
| GET_ITER | 11,302,100 | 1.5% | 72.1% |  |
| INTERPRETER_EXIT | 10,429,680 | 1.3% | 73.5% |  |
| YIELD_VALUE | 10,029,280 | 1.3% | 74.8% |  |
| FOR_ITER_LIST | 10,026,220 | 1.3% | 76.1% |  |
| POP_JUMP_IF_TRUE | 9,955,960 | 1.3% | 77.3% |  |
| LOAD_ATTR_MODULE | 8,788,880 | 1.1% | 78.5% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,180,000 | 1.1% | 79.5% |  |
| SWAP | 6,793,080 | 0.9% | 80.4% |  |
| STORE_FAST_STORE_FAST | 6,555,180 | 0.8% | 81.3% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 6,221,440 | 0.8% | 82.1% |  |
| FOR_ITER | 6,206,360 | 0.8% | 82.9% |  |
| LOAD_FAST_AND_CLEAR | 6,013,920 | 0.8% | 83.6% |  |
| BUILD_LIST | 5,445,580 | 0.7% | 84.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 5,291,500 | 0.7% | 85.0% | 0.0% |
| RETURN_CONST | 5,278,120 | 0.7% | 85.7% |  |
| SEND_GEN | 4,811,540 | 0.6% | 86.3% |  |
| COPY | 4,624,740 | 0.6% | 86.9% |  |
| LOAD_DEREF | 4,488,320 | 0.6% | 87.5% |  |
| CALL_BUILTIN_O | 4,029,320 | 0.5% | 88.0% |  |
| STORE_ATTR_SLOT | 4,004,060 | 0.5% | 88.5% | 48.8% |
| TO_BOOL_ALWAYS_TRUE | 3,992,780 | 0.5% | 89.0% | 56.3% |
| PUSH_NULL | 3,987,640 | 0.5% | 89.5% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 3,781,600 | 0.5% | 90.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,656,300 | 0.5% | 90.5% | 41.6% |
| LOAD_ATTR_PROPERTY | 3,447,700 | 0.4% | 90.9% | 1.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,298,840 | 0.4% | 91.4% | 37.2% |
| RETURN_GENERATOR | 3,215,520 | 0.4% | 91.8% |  |
| TO_BOOL_NONE | 3,026,280 | 0.4% | 92.2% | 21.1% |
| POP_JUMP_IF_NOT_NONE | 2,668,640 | 0.3% | 92.5% |  |
| EXTENDED_ARG | 2,610,160 | 0.3% | 92.9% |  |
| MAKE_FUNCTION | 2,528,660 | 0.3% | 93.2% |  |
| FOR_ITER_GEN | 2,520,520 | 0.3% | 93.5% |  |
| TO_BOOL | 2,431,960 | 0.3% | 93.8% |  |
| COPY_FREE_VARS | 2,317,640 | 0.3% | 94.1% |  |
| JUMP_BACKWARD | 2,316,980 | 0.3% | 94.4% |  |
| BUILD_MAP | 2,296,240 | 0.3% | 94.7% |  |
| MAP_ADD | 2,057,180 | 0.3% | 95.0% |  |
| UNPACK_SEQUENCE_TUPLE | 1,938,640 | 0.2% | 95.2% |  |
| FORMAT_SIMPLE | 1,910,240 | 0.2% | 95.5% |  |
| CALL_TYPE_1 | 1,734,960 | 0.2% | 95.7% |  |
| CALL_TUPLE_1 | 1,678,720 | 0.2% | 95.9% |  |
| MAKE_CELL | 1,622,560 | 0.2% | 96.1% |  |
| CALL_LIST_APPEND | 1,611,780 | 0.2% | 96.3% |  |
| JUMP_FORWARD | 1,593,440 | 0.2% | 96.5% |  |
| STORE_SUBSCR_DICT | 1,541,660 | 0.2% | 96.7% |  |
| CALL | 1,491,020 | 0.2% | 96.9% |  |
| CALL_PY_WITH_DEFAULTS | 1,463,720 | 0.2% | 97.1% | 1.8% |
| IS_OP | 1,422,680 | 0.2% | 97.3% |  |
| BINARY_SUBSCR_LIST_INT | 1,315,780 | 0.2% | 97.5% | 0.5% |
| CALL_BUILTIN_FAST | 1,215,920 | 0.2% | 97.6% | 0.5% |
| TO_BOOL_STR | 1,161,920 | 0.1% | 97.8% | 26.0% |
| CALL_METHOD_DESCRIPTOR_O | 1,051,160 | 0.1% | 97.9% |  |
| END_SEND | 1,030,080 | 0.1% | 98.0% |  |
| GET_YIELD_FROM_ITER | 1,030,080 | 0.1% | 98.2% |  |
| BUILD_STRING | 1,029,280 | 0.1% | 98.3% |  |
| COMPARE_OP | 966,760 | 0.1% | 98.4% |  |
| UNARY_NOT | 962,400 | 0.1% | 98.5% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 951,000 | 0.1% | 98.7% |  |
| SET_FUNCTION_ATTRIBUTE | 872,000 | 0.1% | 98.8% |  |
| LOAD_ATTR_INSTANCE_VALUE | 800,680 | 0.1% | 98.9% | 2.0% |
| LOAD_ATTR | 727,580 | 0.1% | 99.0% |  |
| COMPARE_OP_INT | 609,640 | 0.1% | 99.1% |  |
| BINARY_SUBSCR_DICT | 587,940 | 0.1% | 99.1% |  |
| BINARY_OP_ADD_INT | 543,800 | 0.1% | 99.2% |  |
| CALL_KW | 526,880 | 0.1% | 99.3% |  |
| CONTAINS_OP | 457,240 | 0.1% | 99.3% |  |
| BINARY_SUBSCR_STR_INT | 452,100 | 0.1% | 99.4% |  |
| COMPARE_OP_STR | 416,920 | 0.1% | 99.4% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 391,640 | 0.1% | 99.5% | 67.6% |
| FOR_ITER_TUPLE | 304,500 | 0.0% | 99.5% |  |
| UNPACK_EX | 291,360 | 0.0% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 290,400 | 0.0% | 99.6% |  |
| END_FOR | 279,980 | 0.0% | 99.6% |  |
| POP_JUMP_IF_NONE | 233,120 | 0.0% | 99.7% |  |
| NOP | 227,120 | 0.0% | 99.7% |  |
| CALL_FUNCTION_EX | 193,760 | 0.0% | 99.7% |  |
| TO_BOOL_INT | 180,560 | 0.0% | 99.8% |  |
| DICT_MERGE | 177,020 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 172,840 | 0.0% | 99.8% |  |
| CALL_LEN | 171,420 | 0.0% | 99.8% |  |
| STORE_ATTR_INSTANCE_VALUE | 166,000 | 0.0% | 99.8% |  |
| STORE_FAST_LOAD_FAST | 157,020 | 0.0% | 99.9% |  |
| LIST_APPEND | 138,480 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 99,920 | 0.0% | 99.9% |  |
| LIST_EXTEND | 99,920 | 0.0% | 99.9% |  |
| BINARY_SLICE | 94,880 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 76,480 | 0.0% | 99.9% |  |
| POP_EXCEPT | 76,480 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 76,480 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 73,580 | 0.0% | 100.0% |  |
| BUILD_SET | 55,640 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 42,600 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 37,880 | 0.0% | 100.0% | 5.3% |
| STORE_DEREF | 31,840 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,140 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 29,560 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 25,400 | 0.0% | 100.0% |  |
| BINARY_OP | 19,640 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 18,560 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 16,700 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 16,600 | 0.0% | 100.0% |  |
| SET_ADD | 11,020 | 0.0% | 100.0% |  |
| RESUME | 6,340 | 0.0% | 100.0% | 9.8% |
| STORE_ATTR | 3,120 | 0.0% | 100.0% |  |
| CALL_STR_1 | 2,980 | 0.0% | 100.0% |  |
| DICT_UPDATE | 2,080 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,920 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 960 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 760 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 300 | 0.0% | 100.0% |  |
| SEND | 280 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 220 | 0.0% | 100.0% |  |
| SET_UPDATE | 160 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 140 | 0.0% | 100.0% | 42.9% |
| BINARY_OP_SUBTRACT_FLOAT | 140 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 32,831,920 | 4.2% | 4.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 27,040,960 | 3.5% | 7.7% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 26,999,700 | 3.5% | 11.2% |
| POP_JUMP_IF_FALSE LOAD_FAST | 24,373,260 | 3.1% | 14.3% |
| RESUME_CHECK LOAD_FAST | 17,229,960 | 2.2% | 16.5% |
| LOAD_FAST LOAD_ATTR_SLOT | 16,507,460 | 2.1% | 18.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 15,474,660 | 2.0% | 20.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 14,233,040 | 1.8% | 22.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 12,738,860 | 1.6% | 24.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 11,675,780 | 1.5% | 25.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 11,570,220 | 1.5% | 27.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 10,929,640 | 1.4% | 28.5% |
| STORE_FAST LOAD_FAST | 9,146,560 | 1.2% | 29.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 8,783,580 | 1.1% | 30.8% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 8,528,440 | 1.1% | 31.9% |
| CACHE RESUME_CHECK | 8,473,720 | 1.1% | 33.0% |
| RETURN_VALUE STORE_FAST | 8,406,840 | 1.1% | 34.1% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 8,397,540 | 1.1% | 35.2% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 8,206,520 | 1.1% | 36.3% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 8,173,320 | 1.1% | 37.3% |
| LOAD_FAST RETURN_VALUE | 7,692,840 | 1.0% | 38.3% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 7,512,840 | 1.0% | 39.3% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 6,260,220 | 0.8% | 40.1% |
| RESUME_CHECK POP_TOP | 6,247,400 | 0.8% | 40.9% |
| LOAD_ATTR_MODULE CALL_ISINSTANCE | 6,228,100 | 0.8% | 41.7% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 6,195,680 | 0.8% | 42.5% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 6,011,460 | 0.8% | 43.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS GET_ITER | 6,000,280 | 0.8% | 44.0% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 5,933,660 | 0.8% | 44.8% |
| POP_TOP ENTER_EXECUTOR | 5,328,060 | 0.7% | 45.5% |
| ENTER_EXECUTOR FOR_ITER_LIST | 5,284,260 | 0.7% | 46.1% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 5,266,840 | 0.7% | 46.8% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 4,977,120 | 0.6% | 47.5% |
| LOAD_FAST GET_ITER | 4,667,700 | 0.6% | 48.1% |
| GET_ITER FOR_ITER_LIST | 4,567,940 | 0.6% | 48.7% |
| FOR_ITER_LIST STORE_FAST | 4,531,980 | 0.6% | 49.2% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 4,522,160 | 0.6% | 49.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 4,491,160 | 0.6% | 50.4% |
| BUILD_TUPLE CALL_ISINSTANCE | 4,485,540 | 0.6% | 51.0% |
| LOAD_FAST BUILD_TUPLE | 4,424,540 | 0.6% | 51.5% |
| LOAD_FAST BUILD_LIST | 4,394,900 | 0.6% | 52.1% |
| RETURN_VALUE INTERPRETER_EXIT | 4,340,580 | 0.6% | 52.7% |
| YIELD_VALUE INTERPRETER_EXIT | 4,007,140 | 0.5% | 53.2% |
| STORE_FAST STORE_FAST | 3,927,040 | 0.5% | 53.7% |
| FOR_ITER_LIST ENTER_EXECUTOR | 3,926,680 | 0.5% | 54.2% |
| LOAD_FAST_AND_CLEAR LOAD_FAST_AND_CLEAR | 3,900,160 | 0.5% | 54.7% |
| YIELD_VALUE YIELD_VALUE | 3,781,600 | 0.5% | 55.2% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 3,781,540 | 0.5% | 55.7% |
| SEND_GEN RESUME_CHECK | 3,781,520 | 0.5% | 56.2% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 3,781,500 | 0.5% | 56.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 3,767,260 | 0.5% | 57.1% |
| LOAD_GLOBAL_BUILTIN BUILD_TUPLE | 3,750,620 | 0.5% | 57.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 3,737,080 | 0.5% | 58.1% |
| BUILD_LIST RETURN_VALUE | 3,714,580 | 0.5% | 58.6% |
| LOAD_ATTR_SLOT LOAD_FAST | 3,659,180 | 0.5% | 59.0% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,598,120 | 0.5% | 59.5% |
| STORE_FAST_STORE_FAST LOAD_FAST | 3,443,660 | 0.4% | 60.0% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 3,398,340 | 0.4% | 60.4% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 3,283,820 | 0.4% | 60.8% |
| POP_TOP RESUME_CHECK | 3,215,160 | 0.4% | 61.2% |
| CALL_BUILTIN_O RETURN_VALUE | 3,153,220 | 0.4% | 61.6% |
| LOAD_FAST TO_BOOL_BOOL | 3,142,180 | 0.4% | 62.0% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 3,139,800 | 0.4% | 62.4% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST | 3,065,820 | 0.4% | 62.8% |
| BUILD_TUPLE CALL_BUILTIN_O | 2,992,680 | 0.4% | 63.2% |
| ENTER_EXECUTOR RETURN_CONST | 2,981,120 | 0.4% | 63.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,967,680 | 0.4% | 64.0% |
| POP_TOP LOAD_FAST | 2,963,740 | 0.4% | 64.4% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 2,843,720 | 0.4% | 64.7% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 2,805,380 | 0.4% | 65.1% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 2,790,060 | 0.4% | 65.5% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 2,781,080 | 0.4% | 65.8% |
| LOAD_FAST LOAD_CONST | 2,705,760 | 0.3% | 66.2% |
| BUILD_TUPLE YIELD_VALUE | 2,686,660 | 0.3% | 66.5% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 2,671,440 | 0.3% | 66.9% |
| CALL_METHOD_DESCRIPTOR_FAST RETURN_VALUE | 2,665,080 | 0.3% | 67.2% |
| GET_ITER FOR_ITER | 2,652,280 | 0.3% | 67.5% |
| LOAD_FAST COPY | 2,644,640 | 0.3% | 67.9% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,640,800 | 0.3% | 68.2% |
| RETURN_VALUE RETURN_VALUE | 2,577,840 | 0.3% | 68.5% |
| ENTER_EXECUTOR YIELD_VALUE | 2,542,000 | 0.3% | 68.9% |
| LOAD_CONST MAKE_FUNCTION | 2,528,660 | 0.3% | 69.2% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 2,475,660 | 0.3% | 69.5% |
| LOAD_FAST TO_BOOL_NONE | 2,448,360 | 0.3% | 69.8% |
| TO_BOOL POP_JUMP_IF_FALSE | 2,410,640 | 0.3% | 70.1% |
| LOAD_FAST TO_BOOL | 2,409,640 | 0.3% | 70.5% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_BUILTIN | 2,376,900 | 0.3% | 70.8% |
| PUSH_NULL LOAD_FAST | 2,353,820 | 0.3% | 71.1% |
| COPY_FREE_VARS RESUME_CHECK | 2,312,580 | 0.3% | 71.4% |
| FOR_ITER_GEN RESUME_CHECK | 2,240,700 | 0.3% | 71.7% |
| LOAD_ATTR_SLOT CALL_ISINSTANCE | 2,144,900 | 0.3% | 71.9% |
| GET_ITER LOAD_FAST_AND_CLEAR | 2,113,760 | 0.3% | 72.2% |
| LOAD_FAST_AND_CLEAR SWAP | 2,113,760 | 0.3% | 72.5% |
| SWAP STORE_FAST | 2,086,880 | 0.3% | 72.7% |
| RETURN_CONST INTERPRETER_EXIT | 2,081,960 | 0.3% | 73.0% |
| LOAD_FAST PUSH_NULL | 2,081,680 | 0.3% | 73.3% |
| MAP_ADD ENTER_EXECUTOR | 2,055,480 | 0.3% | 73.5% |
| EXTENDED_ARG POP_JUMP_IF_FALSE | 1,997,640 | 0.3% | 73.8% |
| LOAD_FAST LOAD_DEREF | 1,995,320 | 0.3% | 74.1% |
| TO_BOOL_BOOL EXTENDED_ARG | 1,987,400 | 0.3% | 74.3% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 60,620 | 63.9% |
| LOAD_CONST | 34,240 | 36.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 60,640 | 63.9% |
| CALL_BUILTIN_CLASS | 21,240 | 22.4% |
| GET_ITER | 6,880 | 7.3% |
| TO_BOOL_LIST | 6,040 | 6.4% |
| TO_BOOL | 40 | 0.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 8,473,720 | 81.2% |
| POP_TOP | 1,905,720 | 18.3% |
| MAKE_CELL | 49,120 | 0.5% |
| RESUME | 1,120 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 18,040 | 71.0% |
| ENTER_EXECUTOR | 6,120 | 24.1% |
| LOAD_ATTR_SLOT | 1,200 | 4.7% |
| BINARY_OP | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,400 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,880 | 77.1% |
| LOAD_CONST | 2,880 | 17.2% |
| BINARY_SUBSCR | 340 | 2.0% |
| LOAD_FAST | 240 | 1.4% |
| LOAD_ATTR | 100 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 14,920 | 89.3% |
| BINARY_SUBSCR_DICT | 380 | 2.3% |
| BINARY_SUBSCR | 340 | 2.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 1.0% |
| LOAD_ATTR | 140 | 0.8% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 76,420 | 99.9% |
| LOAD_GLOBAL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 76,480 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 279,980 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 279,980 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,030,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,030,080 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 615,600 | 32.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 571,980 | 29.9% |
| LOAD_FAST | 469,920 | 24.6% |
| RETURN_VALUE | 252,480 | 13.2% |
| CALL_BUILTIN_FAST | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 829,600 | 43.4% |
| LOAD_FAST | 636,160 | 33.3% |
| BUILD_STRING | 444,480 | 23.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,000,280 | 53.1% |
| LOAD_FAST | 4,667,700 | 41.3% |
| RETURN_GENERATOR | 280,000 | 2.5% |
| BUILD_TUPLE | 117,120 | 1.0% |
| LOAD_ATTR_SLOT | 90,480 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,567,940 | 40.4% |
| FOR_ITER | 2,652,280 | 23.5% |
| LOAD_FAST_AND_CLEAR | 2,113,760 | 18.7% |
| CALL_PY_EXACT_ARGS | 1,665,120 | 14.7% |
| FOR_ITER_GEN | 265,060 | 2.3% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 1,030,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,030,080 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,340,580 | 41.6% |
| YIELD_VALUE | 4,007,140 | 38.4% |
| RETURN_CONST | 2,081,960 | 20.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,528,660 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,411,960 | 55.8% |
| SET_FUNCTION_ATTRIBUTE | 869,760 | 34.4% |
| LOAD_FAST | 246,740 | 9.8% |
| STORE_FAST | 160 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 157,020 | 69.1% |
| POP_JUMP_IF_FALSE | 60,480 | 26.6% |
| STORE_FAST | 8,480 | 3.7% |
| POP_JUMP_IF_TRUE | 960 | 0.4% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 109,760 | 48.3% |
| LOAD_FAST_LOAD_FAST | 76,800 | 33.8% |
| LOAD_GLOBAL_MODULE | 37,560 | 16.5% |
| LOAD_GLOBAL_BUILTIN | 2,380 | 1.0% |
| LOAD_CONST | 480 | 0.2% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 43,200 | 56.5% |
| STORE_SUBSCR_DICT | 33,260 | 43.5% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 39,680 | 51.9% |
| JUMP_FORWARD | 36,800 | 48.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,247,400 | 36.9% |
| CACHE | 1,905,720 | 11.3% |
| STORE_FAST | 1,888,480 | 11.1% |
| POP_JUMP_IF_FALSE | 1,586,400 | 9.4% |
| RETURN_CONST | 1,343,200 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,328,060 | 31.5% |
| RESUME_CHECK | 3,215,160 | 19.0% |
| LOAD_FAST | 2,963,740 | 17.5% |
| STORE_FAST | 1,886,080 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 1,073,360 | 6.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 70,060 | 91.6% |
| BINARY_SUBSCR_LIST_INT | 6,240 | 8.2% |
| LOAD_ATTR_METHOD_NO_DICT | 160 | 0.2% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 76,360 | 99.8% |
| LOAD_GLOBAL | 120 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,081,680 | 52.2% |
| LOAD_ATTR_MODULE | 664,540 | 16.7% |
| CALL_BUILTIN_FAST | 571,980 | 14.3% |
| LOAD_DEREF | 508,800 | 12.8% |
| LOAD_FAST_LOAD_FAST | 66,080 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,353,820 | 59.0% |
| LOAD_FAST_LOAD_FAST | 1,446,920 | 36.3% |
| LOAD_CONST | 53,220 | 1.3% |
| LOAD_DEREF | 49,920 | 1.3% |
| LOAD_GLOBAL_MODULE | 37,600 | 0.9% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,671,440 | 83.1% |
| CALL_KW | 258,880 | 8.1% |
| MAKE_CELL | 239,840 | 7.5% |
| CALL_PY_WITH_DEFAULTS | 21,240 | 0.7% |
| CALL | 19,320 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_TUPLE_1 | 1,559,440 | 48.5% |
| GET_YIELD_FROM_ITER | 1,030,080 | 32.0% |
| GET_ITER | 280,000 | 8.7% |
| CALL_BUILTIN_CLASS | 131,600 | 4.1% |
| CALL_METHOD_DESCRIPTOR_O | 117,080 | 3.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,692,840 | 28.6% |
| BUILD_LIST | 3,714,580 | 13.8% |
| CALL_BUILTIN_O | 3,153,220 | 11.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,665,080 | 9.9% |
| RETURN_VALUE | 2,577,840 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,406,840 | 31.2% |
| INTERPRETER_EXIT | 4,340,580 | 16.1% |
| LOAD_ATTR_METHOD_NO_DICT | 2,790,060 | 10.4% |
| RETURN_VALUE | 2,577,840 | 9.6% |
| MAP_ADD | 1,883,140 | 7.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 36.8% |
| LOAD_FAST_LOAD_FAST | 240 | 31.6% |
| RETURN_VALUE | 80 | 10.5% |
| CALL | 60 | 7.9% |
| CALL_BUILTIN_O | 60 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_SUBSCR_DICT | 380 | 50.0% |
| JUMP_BACKWARD | 240 | 31.6% |
| LOAD_FAST | 80 | 10.5% |
| POP_EXCEPT | 20 | 2.6% |
| EXTENDED_ARG | 20 | 2.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,409,640 | 99.1% |
| COPY | 9,240 | 0.4% |
| RETURN_CONST | 3,000 | 0.1% |
| CALL | 2,580 | 0.1% |
| TO_BOOL | 2,360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,410,640 | 99.1% |
| POP_JUMP_IF_TRUE | 10,480 | 0.4% |
| TO_BOOL_BOOL | 4,180 | 0.2% |
| TO_BOOL_NONE | 2,660 | 0.1% |
| TO_BOOL | 2,360 | 0.1% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 925,500 | 96.2% |
| TO_BOOL_ALWAYS_TRUE | 28,900 | 3.0% |
| TO_BOOL_NONE | 7,880 | 0.8% |
| TO_BOOL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 924,640 | 96.1% |
| STORE_FAST | 36,800 | 3.8% |
| COPY | 960 | 0.1% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,880 | 55.4% |
| LOAD_FAST_LOAD_FAST | 4,560 | 23.2% |
| CALL_BUILTIN_CLASS | 1,400 | 7.1% |
| BUILD_LIST | 1,180 | 6.0% |
| BINARY_OP | 740 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,600 | 54.0% |
| GET_ITER | 4,160 | 21.2% |
| STORE_FAST | 2,040 | 10.4% |
| LOAD_FAST_LOAD_FAST | 1,200 | 6.1% |
| BINARY_OP | 740 | 3.8% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 18,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,720 | 57.8% |
| CALL_FUNCTION_EX | 5,440 | 29.3% |
| DICT_MERGE | 1,280 | 6.9% |
| STORE_FAST | 800 | 4.3% |
| LOAD_DEREF | 320 | 1.7% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,394,900 | 80.7% |
| STORE_FAST | 647,580 | 11.9% |
| SWAP | 138,880 | 2.6% |
| LOAD_DEREF | 49,120 | 0.9% |
| POP_JUMP_IF_FALSE | 46,880 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,714,580 | 68.2% |
| STORE_FAST | 1,314,200 | 24.1% |
| SWAP | 138,880 | 2.6% |
| LOAD_FAST | 118,680 | 2.2% |
| LOAD_DEREF | 98,960 | 1.8% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,968,640 | 85.7% |
| LOAD_CONST | 101,280 | 4.4% |
| RESUME_CHECK | 55,120 | 2.4% |
| CALL_INTRINSIC_1 | 49,760 | 2.2% |
| LOAD_FAST_LOAD_FAST | 45,920 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,968,640 | 85.7% |
| STORE_FAST | 99,560 | 4.3% |
| LOAD_DEREF | 98,880 | 4.3% |
| CALL_PY_EXACT_ARGS | 46,640 | 2.0% |
| LOAD_FAST | 45,180 | 2.0% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,800 | 87.7% |
| SWAP | 6,240 | 11.2% |
| LOAD_GLOBAL_MODULE | 420 | 0.8% |
| JUMP_FORWARD | 160 | 0.3% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 48,760 | 87.6% |
| SWAP | 6,240 | 11.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 400 | 0.7% |
| LOAD_CONST | 160 | 0.3% |
| CALL | 40 | 0.1% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 584,800 | 56.8% |
| FORMAT_SIMPLE | 444,480 | 43.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 572,160 | 55.6% |
| RETURN_VALUE | 457,120 | 44.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,424,540 | 35.7% |
| LOAD_GLOBAL_BUILTIN | 3,750,620 | 30.3% |
| CALL_TUPLE_1 | 1,411,980 | 11.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,249,900 | 10.1% |
| LOAD_ATTR_MODULE | 635,560 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 4,485,540 | 36.2% |
| CALL_BUILTIN_O | 2,992,680 | 24.1% |
| YIELD_VALUE | 2,686,660 | 21.7% |
| CALL_METHOD_DESCRIPTOR_O | 916,540 | 7.4% |
| LOAD_CONST | 876,860 | 7.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,285,600 | 86.2% |
| RETURN_GENERATOR | 47,480 | 3.2% |
| LOAD_CONST | 42,960 | 2.9% |
| LOAD_ATTR_MODULE | 26,360 | 1.8% |
| LOAD_ATTR_SLOT | 24,280 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,215,880 | 81.5% |
| STORE_FAST | 73,400 | 4.9% |
| GET_ITER | 39,960 | 2.7% |
| RETURN_VALUE | 37,300 | 2.5% |
| CALL_LIST_APPEND | 24,340 | 1.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 177,020 | 91.4% |
| ENTER_EXECUTOR | 7,620 | 3.9% |
| BUILD_CONST_KEY_MAP | 5,440 | 2.8% |
| RETURN_GENERATOR | 2,400 | 1.2% |
| CALL_INTRINSIC_1 | 1,040 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 90,240 | 46.6% |
| RESUME_CHECK | 80,220 | 41.4% |
| STORE_FAST | 17,440 | 9.0% |
| COPY_FREE_VARS | 3,600 | 1.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,000 | 1.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 99,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 49,760 | 49.8% |
| LOAD_CONST | 49,120 | 49.2% |
| CALL_FUNCTION_EX | 1,040 | 1.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 524,820 | 99.6% |
| ENTER_EXECUTOR | 2,060 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 258,880 | 49.1% |
| RESUME_CHECK | 113,480 | 21.5% |
| MAKE_CELL | 59,840 | 11.4% |
| STORE_FAST | 52,960 | 10.1% |
| RETURN_VALUE | 38,080 | 7.2% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 266,800 | 27.6% |
| LOAD_ATTR | 234,120 | 24.2% |
| LOAD_FAST | 182,040 | 18.8% |
| LOAD_GLOBAL_MODULE | 98,420 | 10.2% |
| CALL_BUILTIN_CLASS | 86,540 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 592,160 | 61.3% |
| RETURN_VALUE | 272,500 | 28.2% |
| COPY | 54,420 | 5.6% |
| POP_JUMP_IF_TRUE | 42,060 | 4.4% |
| COMPARE_OP | 4,480 | 0.5% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,840 | 23.6% |
| LOAD_FAST_LOAD_FAST | 107,120 | 23.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 91,600 | 20.0% |
| BUILD_TUPLE | 72,360 | 15.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 39,360 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 342,500 | 74.9% |
| POP_JUMP_IF_TRUE | 96,340 | 21.1% |
| STORE_FAST | 18,400 | 4.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,644,640 | 57.2% |
| CALL_ISINSTANCE | 950,460 | 20.6% |
| IS_OP | 746,560 | 16.1% |
| RETURN_VALUE | 122,100 | 2.6% |
| COMPARE_OP | 54,420 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 1,935,120 | 41.8% |
| TO_BOOL_BOOL | 1,800,240 | 38.9% |
| LOAD_ATTR_SLOT | 468,480 | 10.1% |
| TO_BOOL_NONE | 261,560 | 5.7% |
| TO_BOOL_STR | 127,360 | 2.8% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,215,880 | 52.5% |
| CALL_PY_EXACT_ARGS | 1,093,880 | 47.2% |
| CALL_PY_WITH_DEFAULTS | 3,820 | 0.2% |
| CALL_FUNCTION_EX | 3,600 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,312,580 | 99.8% |
| RETURN_GENERATOR | 4,800 | 0.2% |
| RESUME | 260 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 98,880 | 55.9% |
| LOAD_FAST | 39,260 | 22.2% |
| RETURN_VALUE | 31,040 | 17.5% |
| BUILD_MAP | 4,480 | 2.5% |
| DICT_UPDATE | 2,080 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 177,020 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 2,080 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,328,060 | 30.6% |
| FOR_ITER_LIST | 3,926,680 | 22.5% |
| MAP_ADD | 2,055,480 | 11.8% |
| POP_JUMP_IF_TRUE | 1,894,380 | 10.9% |
| STORE_SUBSCR_DICT | 1,350,900 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,284,260 | 30.3% |
| RETURN_CONST | 2,981,120 | 17.1% |
| YIELD_VALUE | 2,542,000 | 14.6% |
| SWAP | 1,946,540 | 11.2% |
| LOAD_GLOBAL_BUILTIN | 1,556,100 | 8.9% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,987,400 | 76.1% |
| JUMP_BACKWARD | 317,660 | 12.2% |
| POP_JUMP_IF_TRUE | 242,740 | 9.3% |
| GET_ITER | 35,520 | 1.4% |
| TO_BOOL_NONE | 10,020 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,997,640 | 76.5% |
| FOR_ITER_GEN | 299,760 | 11.5% |
| JUMP_BACKWARD | 252,780 | 9.7% |
| FOR_ITER | 42,620 | 1.6% |
| FOR_ITER_LIST | 14,800 | 0.6% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 2,652,280 | 42.7% |
| SWAP | 1,948,920 | 31.4% |
| LOAD_FAST | 1,537,540 | 24.8% |
| EXTENDED_ARG | 42,620 | 0.7% |
| JUMP_BACKWARD | 18,880 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 5,933,660 | 95.6% |
| STORE_FAST_LOAD_FAST | 127,960 | 2.1% |
| STORE_FAST | 118,240 | 1.9% |
| LOAD_FAST | 7,520 | 0.1% |
| FOR_ITER | 6,120 | 0.1% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,920 | 100.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_TYPE_1 | 746,540 | 52.5% |
| LOAD_FAST_LOAD_FAST | 341,280 | 24.0% |
| LOAD_ATTR_INSTANCE_VALUE | 291,340 | 20.5% |
| LOAD_DEREF | 43,480 | 3.1% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 746,560 | 52.5% |
| POP_JUMP_IF_FALSE | 663,160 | 46.6% |
| RETURN_VALUE | 12,960 | 0.9% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 939,180 | 40.5% |
| POP_TOP | 644,520 | 27.8% |
| POP_JUMP_IF_FALSE | 358,060 | 15.5% |
| EXTENDED_ARG | 252,780 | 10.9% |
| CALL_LIST_APPEND | 59,780 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 1,947,940 | 84.1% |
| EXTENDED_ARG | 317,660 | 13.7% |
| FOR_ITER_LIST | 22,400 | 1.0% |
| FOR_ITER | 18,880 | 0.8% |
| LOAD_FAST | 4,640 | 0.2% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,781,500 | 100.0% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 3,781,540 | 100.0% |
| SEND | 60 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 485,380 | 30.5% |
| STORE_FAST | 336,640 | 21.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 234,220 | 14.7% |
| POP_JUMP_IF_FALSE | 135,080 | 8.5% |
| CALL_TUPLE_1 | 97,900 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 456,960 | 28.7% |
| STORE_FAST | 344,000 | 21.6% |
| LOAD_FAST | 245,120 | 15.4% |
| LOAD_FAST_LOAD_FAST | 168,480 | 10.6% |
| LOAD_GLOBAL_BUILTIN | 107,800 | 6.8% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 105,500 | 76.2% |
| LOAD_FAST | 27,240 | 19.7% |
| BINARY_OP_ADD_INT | 4,900 | 3.5% |
| BINARY_SUBSCR_DICT | 780 | 0.6% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 135,080 | 97.5% |
| JUMP_BACKWARD | 3,400 | 2.5% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 98,960 | 99.0% |
| CALL | 960 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 99,920 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 560,540 | 77.0% |
| LOAD_FAST | 119,640 | 16.4% |
| LOAD_FAST_LOAD_FAST | 15,280 | 2.1% |
| LOAD_ATTR | 14,200 | 2.0% |
| LOAD_GLOBAL | 5,440 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 234,120 | 32.2% |
| CALL_PY_EXACT_ARGS | 199,980 | 27.5% |
| LOAD_FAST | 115,000 | 15.8% |
| PUSH_NULL | 57,300 | 7.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 26,480 | 3.6% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,139,800 | 23.9% |
| LOAD_FAST | 2,705,760 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 1,537,380 | 11.7% |
| GET_YIELD_FROM_ITER | 1,030,080 | 7.8% |
| BUILD_TUPLE | 876,860 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 3,065,820 | 23.3% |
| MAKE_FUNCTION | 2,528,660 | 19.3% |
| CALL_PY_EXACT_ARGS | 1,624,840 | 12.4% |
| BINARY_SUBSCR_LIST_INT | 1,238,520 | 9.4% |
| SEND_GEN | 1,029,860 | 7.8% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,995,320 | 44.5% |
| RESUME_CHECK | 754,680 | 16.8% |
| POP_JUMP_IF_FALSE | 613,960 | 13.7% |
| LOAD_GLOBAL_BUILTIN | 501,820 | 11.2% |
| BUILD_LIST | 98,960 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,907,120 | 42.5% |
| PUSH_NULL | 508,800 | 11.3% |
| RETURN_VALUE | 495,520 | 11.0% |
| LOAD_GLOBAL_MODULE | 458,360 | 10.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 288,600 | 6.4% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 32,831,920 | 24.7% |
| POP_JUMP_IF_FALSE | 24,373,260 | 18.3% |
| RESUME_CHECK | 17,229,960 | 13.0% |
| LOAD_GLOBAL_MODULE | 10,929,640 | 8.2% |
| STORE_FAST | 9,146,560 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 16,507,460 | 12.4% |
| LOAD_GLOBAL_BUILTIN | 15,474,660 | 11.6% |
| LOAD_GLOBAL_MODULE | 12,738,860 | 9.6% |
| CALL_PY_EXACT_ARGS | 11,570,220 | 8.7% |
| RETURN_VALUE | 7,692,840 | 5.8% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 3,900,160 | 64.9% |
| GET_ITER | 2,113,760 | 35.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 3,900,160 | 64.9% |
| SWAP | 2,113,760 | 35.1% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 920 | 95.8% |
| TO_BOOL | 40 | 4.2% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,805,380 | 24.2% |
| STORE_FAST | 1,525,680 | 13.2% |
| PUSH_NULL | 1,446,920 | 12.5% |
| LOAD_ATTR_METHOD_NO_DICT | 1,095,700 | 9.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,027,380 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,491,160 | 38.8% |
| STORE_ATTR_SLOT | 1,857,360 | 16.0% |
| CALL_ISINSTANCE | 1,351,720 | 11.7% |
| CALL_BUILTIN_FAST | 1,145,000 | 9.9% |
| CALL_PY_EXACT_ARGS | 567,180 | 4.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,840 | 16.4% |
| STORE_FAST | 4,500 | 15.2% |
| POP_JUMP_IF_FALSE | 3,940 | 13.3% |
| LOAD_ATTR | 3,540 | 12.0% |
| LOAD_ATTR_METHOD_NO_DICT | 1,960 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 10,240 | 34.6% |
| LOAD_FAST | 5,880 | 19.9% |
| LOAD_ATTR | 5,440 | 18.4% |
| LOAD_GLOBAL_BUILTIN | 4,540 | 15.4% |
| LOAD_FAST_LOAD_FAST | 1,460 | 4.9% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,084,240 | 66.8% |
| MAKE_CELL | 233,920 | 14.4% |
| CALL_PY_WITH_DEFAULTS | 189,880 | 11.7% |
| CALL_KW | 59,840 | 3.7% |
| CACHE | 49,120 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,148,400 | 70.8% |
| RETURN_GENERATOR | 239,840 | 14.8% |
| MAKE_CELL | 233,920 | 14.4% |
| RESUME | 400 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,883,140 | 91.5% |
| JUMP_FORWARD | 101,440 | 4.9% |
| LOAD_FAST | 72,600 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 2,055,480 | 99.9% |
| JUMP_BACKWARD | 1,700 | 0.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 26,999,700 | 70.9% |
| TO_BOOL_NONE | 2,475,660 | 6.5% |
| TO_BOOL | 2,410,640 | 6.3% |
| EXTENDED_ARG | 1,997,640 | 5.2% |
| TO_BOOL_ALWAYS_TRUE | 1,140,560 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 24,373,260 | 64.0% |
| LOAD_GLOBAL_BUILTIN | 4,522,160 | 11.9% |
| LOAD_GLOBAL_MODULE | 2,843,720 | 7.5% |
| POP_TOP | 1,586,400 | 4.2% |
| RETURN_VALUE | 1,163,240 | 3.1% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 219,840 | 94.3% |
| LOAD_ATTR_INSTANCE_VALUE | 13,120 | 5.6% |
| BINARY_SUBSCR_LIST_INT | 140 | 0.1% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 199,040 | 85.4% |
| LOAD_GLOBAL_BUILTIN | 31,640 | 13.6% |
| LOAD_GLOBAL_MODULE | 1,260 | 0.5% |
| ENTER_EXECUTOR | 620 | 0.3% |
| JUMP_BACKWARD | 340 | 0.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,640,800 | 99.0% |
| LOAD_ATTR_INSTANCE_VALUE | 24,100 | 0.9% |
| STORE_FAST_LOAD_FAST | 2,560 | 0.1% |
| LOAD_ATTR_SLOT | 1,100 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 2,376,900 | 89.1% |
| LOAD_FAST | 194,400 | 7.3% |
| LOAD_GLOBAL_MODULE | 36,760 | 1.4% |
| BUILD_MAP | 33,280 | 1.2% |
| BUILD_LIST | 16,420 | 0.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,011,460 | 60.4% |
| TO_BOOL_ALWAYS_TRUE | 2,781,080 | 27.9% |
| TO_BOOL_NONE | 520,920 | 5.2% |
| TO_BOOL_STR | 457,020 | 4.6% |
| CONTAINS_OP | 96,340 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,767,260 | 37.8% |
| ENTER_EXECUTOR | 1,894,380 | 19.0% |
| LOAD_GLOBAL_BUILTIN | 1,211,640 | 12.2% |
| STORE_FAST | 1,052,800 | 10.6% |
| JUMP_BACKWARD | 939,180 | 9.4% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 2,981,120 | 56.5% |
| POP_JUMP_IF_FALSE | 979,240 | 18.6% |
| POP_TOP | 449,140 | 8.5% |
| STORE_ATTR_SLOT | 416,840 | 7.9% |
| POP_JUMP_IF_TRUE | 213,920 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 2,081,960 | 39.4% |
| POP_TOP | 1,343,200 | 25.4% |
| END_SEND | 1,030,080 | 19.5% |
| END_FOR | 279,980 | 5.3% |
| TO_BOOL_NONE | 249,320 | 4.7% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220 | 78.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 60 | 21.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 140 | 50.0% |
| SEND_GEN | 140 | 50.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,420 | 49.2% |
| LOAD_ATTR_PROPERTY | 4,160 | 37.7% |
| LOAD_FAST | 1,420 | 12.9% |
| LOAD_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 10,340 | 93.8% |
| JUMP_BACKWARD | 680 | 6.2% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 869,760 | 99.7% |
| SET_FUNCTION_ATTRIBUTE | 2,240 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 620,840 | 71.2% |
| LOAD_CONST | 239,840 | 27.5% |
| STORE_DEREF | 3,520 | 0.4% |
| LOAD_FAST | 2,400 | 0.3% |
| LOAD_GLOBAL_BUILTIN | 2,360 | 0.3% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 120 | 75.0% |
| LOAD_GLOBAL | 40 | 25.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,080 | 66.7% |
| LOAD_FAST_LOAD_FAST | 840 | 26.9% |
| SWAP | 160 | 5.1% |
| LOAD_DEREF | 40 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,000 | 32.1% |
| STORE_ATTR_INSTANCE_VALUE | 560 | 17.9% |
| LOAD_FAST | 440 | 14.1% |
| LOAD_CONST | 280 | 9.0% |
| LOAD_FAST_LOAD_FAST | 240 | 7.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 21,280 | 66.8% |
| RETURN_CONST | 3,840 | 12.1% |
| SET_FUNCTION_ATTRIBUTE | 3,520 | 11.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,420 | 4.5% |
| BUILD_LIST | 1,280 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 21,240 | 66.7% |
| LOAD_DEREF | 5,120 | 16.1% |
| LOAD_GLOBAL_MODULE | 2,200 | 6.9% |
| LOAD_FAST | 1,760 | 5.5% |
| STORE_FAST | 1,440 | 4.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,406,840 | 26.4% |
| FOR_ITER_LIST | 4,531,980 | 14.2% |
| STORE_FAST | 3,927,040 | 12.3% |
| SWAP | 2,086,880 | 6.5% |
| POP_TOP | 1,886,080 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,146,560 | 28.7% |
| LOAD_GLOBAL_BUILTIN | 8,397,540 | 26.3% |
| STORE_FAST | 3,927,040 | 12.3% |
| LOAD_GLOBAL_MODULE | 3,737,080 | 11.7% |
| RETURN_VALUE | 1,956,480 | 6.1% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 127,960 | 81.5% |
| YIELD_VALUE | 15,160 | 9.7% |
| FOR_ITER_LIST | 11,360 | 7.2% |
| FOR_ITER_TUPLE | 2,540 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 125,240 | 79.8% |
| LOAD_ATTR_PROPERTY | 21,760 | 13.9% |
| LOAD_FAST | 3,560 | 2.3% |
| POP_JUMP_IF_NOT_NONE | 2,560 | 1.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,200 | 1.4% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 6,195,680 | 94.5% |
| UNPACK_EX | 291,360 | 4.4% |
| UNPACK_SEQUENCE_TUPLE | 52,600 | 0.8% |
| UNPACK_SEQUENCE | 15,540 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,443,660 | 52.5% |
| LOAD_GLOBAL_MODULE | 1,826,960 | 27.9% |
| LOAD_GLOBAL_BUILTIN | 875,920 | 13.4% |
| LOAD_FAST_LOAD_FAST | 355,400 | 5.4% |
| STORE_FAST | 52,640 | 0.8% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 2,113,760 | 31.1% |
| BUILD_MAP | 1,968,640 | 29.0% |
| ENTER_EXECUTOR | 1,946,540 | 28.7% |
| BINARY_OP_ADD_INT | 468,560 | 6.9% |
| BUILD_LIST | 138,880 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,086,880 | 30.7% |
| BUILD_MAP | 1,968,640 | 29.0% |
| FOR_ITER | 1,948,920 | 28.7% |
| STORE_ATTR_SLOT | 468,480 | 6.9% |
| BUILD_LIST | 138,880 | 2.0% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 291,340 | 100.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 291,360 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 14,880 | 89.6% |
| FOR_ITER | 840 | 5.1% |
| RETURN_VALUE | 200 | 1.2% |
| UNPACK_SEQUENCE | 160 | 1.0% |
| STORE_FAST | 120 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 15,540 | 93.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 700 | 4.2% |
| UNPACK_SEQUENCE | 160 | 1.0% |
| STORE_FAST | 100 | 0.6% |
| UNPACK_SEQUENCE_TUPLE | 80 | 0.5% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 3,781,600 | 37.7% |
| BUILD_TUPLE | 2,686,660 | 26.8% |
| ENTER_EXECUTOR | 2,542,000 | 25.3% |
| JUMP_FORWARD | 456,960 | 4.6% |
| LOAD_FAST | 292,160 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 4,007,140 | 40.0% |
| YIELD_VALUE | 3,781,600 | 37.7% |
| UNPACK_SEQUENCE_TUPLE | 1,917,000 | 19.1% |
| UNPACK_EX | 291,340 | 2.9% |
| STORE_FAST | 16,980 | 0.2% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,140 | 49.5% |
| CACHE | 1,120 | 17.7% |
| MAKE_CELL | 400 | 6.3% |
| POP_TOP | 360 | 5.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 340 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,300 | 52.1% |
| LOAD_GLOBAL | 1,640 | 25.9% |
| POP_TOP | 280 | 4.4% |
| LOAD_DEREF | 280 | 4.4% |
| LOAD_CONST | 200 | 3.2% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 120 | 85.7% |
| BINARY_OP | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 140 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 481,120 | 88.5% |
| LOAD_CONST | 57,280 | 10.5% |
| LOAD_FAST_LOAD_FAST | 4,880 | 0.9% |
| BINARY_OP | 240 | 0.0% |
| RETURN_VALUE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 468,560 | 86.2% |
| STORE_FAST | 38,180 | 7.0% |
| CALL_PY_EXACT_ARGS | 26,040 | 4.8% |
| LIST_APPEND | 4,900 | 0.9% |
| BINARY_OP_SUBTRACT_INT | 4,760 | 0.9% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| BINARY_OP | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 120 | 85.7% |
| BINARY_OP | 20 | 14.3% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 261,400 | 90.0% |
| CALL_LEN | 23,960 | 8.3% |
| BINARY_OP_ADD_INT | 4,760 | 1.6% |
| BINARY_OP | 160 | 0.1% |
| LOAD_ATTR_SLOT | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 218,040 | 75.1% |
| CALL_PY_EXACT_ARGS | 24,360 | 8.4% |
| LOAD_CONST | 23,980 | 8.3% |
| LOAD_FAST | 19,020 | 6.5% |
| RETURN_VALUE | 4,780 | 1.6% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 441,040 | 75.0% |
| CALL_BUILTIN_O | 63,640 | 10.8% |
| BUILD_TUPLE | 36,800 | 6.3% |
| LOAD_FAST_LOAD_FAST | 22,520 | 3.8% |
| LOAD_ATTR_SLOT | 13,960 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 335,800 | 57.1% |
| RETURN_VALUE | 77,220 | 13.1% |
| PUSH_EXC_INFO | 70,060 | 11.9% |
| LOAD_ATTR_PROPERTY | 32,600 | 5.5% |
| STORE_FAST | 30,880 | 5.3% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 280 | 93.3% |
| BINARY_SUBSCR | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 300 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,238,520 | 94.1% |
| LOAD_FAST_LOAD_FAST | 77,000 | 5.9% |
| BINARY_SUBSCR | 160 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,228,940 | 93.4% |
| RETURN_VALUE | 72,600 | 5.5% |
| STORE_FAST | 7,320 | 0.6% |
| PUSH_EXC_INFO | 6,240 | 0.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 280 | 0.0% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 218,040 | 48.2% |
| LOAD_ATTR_SLOT | 215,960 | 47.8% |
| LOAD_FAST | 18,040 | 4.0% |
| BINARY_SUBSCR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 434,040 | 96.0% |
| STORE_FAST | 18,060 | 4.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 21,280 | 50.0% |
| LOAD_FAST | 21,280 | 50.0% |
| BINARY_SUBSCR | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 21,300 | 50.0% |
| LOAD_CONST | 21,300 | 50.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360,900 | 92.2% |
| PUSH_NULL | 24,580 | 6.3% |
| CALL_PY_EXACT_ARGS | 4,920 | 1.3% |
| LOAD_ATTR_SLOT | 1,040 | 0.3% |
| CALL | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 381,700 | 97.5% |
| CALL_PY_EXACT_ARGS | 4,920 | 1.3% |
| MAKE_CELL | 4,220 | 1.1% |
| COPY_FREE_VARS | 460 | 0.1% |
| RESUME | 340 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 131,600 | 76.1% |
| BINARY_SLICE | 21,240 | 12.3% |
| CALL_BUILTIN_FAST | 6,640 | 3.8% |
| LOAD_FAST | 4,360 | 2.5% |
| LOAD_GLOBAL_BUILTIN | 3,260 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 86,540 | 50.1% |
| JUMP_FORWARD | 37,740 | 21.8% |
| GET_ITER | 24,920 | 14.4% |
| RETURN_VALUE | 8,720 | 5.0% |
| CALL_LEN | 4,760 | 2.8% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,145,000 | 94.2% |
| LOAD_CONST | 32,240 | 2.7% |
| LOAD_GLOBAL_BUILTIN | 31,640 | 2.6% |
| RETURN_GENERATOR | 6,040 | 0.5% |
| CALL_BUILTIN_FAST | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 603,600 | 49.6% |
| PUSH_NULL | 571,980 | 47.0% |
| STORE_FAST | 31,660 | 2.6% |
| CALL_BUILTIN_CLASS | 6,640 | 0.5% |
| LOAD_FAST_LOAD_FAST | 940 | 0.1% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 23,960 | 76.9% |
| RETURN_VALUE | 4,760 | 15.3% |
| LOAD_DEREF | 2,360 | 7.6% |
| CALL | 60 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,980 | 77.0% |
| LOAD_GLOBAL_BUILTIN | 4,760 | 15.3% |
| GET_ITER | 2,380 | 7.6% |
| LOAD_GLOBAL | 20 | 0.1% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 2,992,680 | 74.3% |
| LOAD_FAST | 871,160 | 21.6% |
| LOAD_ATTR_INSTANCE_VALUE | 160,480 | 4.0% |
| RETURN_VALUE | 3,320 | 0.1% |
| RETURN_GENERATOR | 1,400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,153,220 | 78.3% |
| TO_BOOL_BOOL | 573,360 | 14.2% |
| STORE_FAST | 166,020 | 4.1% |
| STORE_SUBSCR_DICT | 65,800 | 1.6% |
| BINARY_SUBSCR_DICT | 63,640 | 1.6% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 8,206,520 | 28.6% |
| LOAD_GLOBAL_MODULE | 6,260,220 | 21.8% |
| LOAD_ATTR_MODULE | 6,228,100 | 21.7% |
| BUILD_TUPLE | 4,485,540 | 15.6% |
| LOAD_ATTR_SLOT | 2,144,900 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 27,040,960 | 94.3% |
| COPY | 950,460 | 3.3% |
| STORE_FAST | 633,780 | 2.2% |
| RETURN_VALUE | 53,420 | 0.2% |
| TO_BOOL | 2,280 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 144,760 | 84.4% |
| LOAD_DEREF | 18,840 | 11.0% |
| CALL_BUILTIN_CLASS | 4,760 | 2.8% |
| LOAD_ATTR_SLOT | 2,040 | 1.2% |
| CALL | 380 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 50,000 | 29.2% |
| LOAD_FAST | 48,920 | 28.5% |
| BINARY_OP_SUBTRACT_INT | 23,960 | 14.0% |
| COMPARE_OP_INT | 21,120 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 19,080 | 11.1% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,179,440 | 73.2% |
| ENTER_EXECUTOR | 397,120 | 24.6% |
| CALL | 24,340 | 1.5% |
| BUILD_TUPLE | 8,840 | 0.5% |
| RETURN_VALUE | 2,040 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 717,440 | 44.5% |
| LOAD_FAST_LOAD_FAST | 670,200 | 41.6% |
| LOAD_FAST | 126,020 | 7.8% |
| JUMP_BACKWARD | 59,780 | 3.7% |
| RETURN_CONST | 32,440 | 2.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,065,820 | 57.9% |
| LOAD_FAST | 1,257,560 | 23.8% |
| LOAD_ATTR_SLOT | 714,760 | 13.5% |
| LOAD_FAST_LOAD_FAST | 130,300 | 2.5% |
| LOAD_ATTR_METHOD_NO_DICT | 85,200 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,665,080 | 50.4% |
| STORE_FAST | 1,635,640 | 30.9% |
| CALL_PY_WITH_DEFAULTS | 631,600 | 11.9% |
| TO_BOOL_BOOL | 234,200 | 4.4% |
| LOAD_GLOBAL_MODULE | 78,840 | 1.5% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 73,560 | 100.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 73,580 | 100.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,173,320 | 99.9% |
| LOAD_FAST | 5,880 | 0.1% |
| CALL | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 6,000,280 | 73.4% |
| BUILD_TUPLE | 1,249,900 | 15.3% |
| RETURN_VALUE | 526,960 | 6.4% |
| JUMP_FORWARD | 234,220 | 2.9% |
| STORE_FAST | 47,180 | 0.6% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 916,540 | 87.2% |
| RETURN_GENERATOR | 117,080 | 11.1% |
| LOAD_FAST | 16,320 | 1.6% |
| RETURN_VALUE | 920 | 0.1% |
| LOAD_ATTR_PROPERTY | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 934,060 | 88.9% |
| RETURN_VALUE | 117,100 | 11.1% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,570,220 | 60.6% |
| GET_ITER | 1,665,120 | 8.7% |
| LOAD_CONST | 1,624,840 | 8.5% |
| RETURN_VALUE | 1,187,720 | 6.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,063,820 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 14,233,040 | 74.6% |
| RETURN_GENERATOR | 2,671,440 | 14.0% |
| COPY_FREE_VARS | 1,093,880 | 5.7% |
| MAKE_CELL | 1,084,240 | 5.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,920 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 631,600 | 43.2% |
| ENTER_EXECUTOR | 291,740 | 19.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 206,840 | 14.1% |
| LOAD_FAST_LOAD_FAST | 127,700 | 8.7% |
| LOAD_FAST | 94,280 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,248,300 | 85.3% |
| MAKE_CELL | 189,880 | 13.0% |
| RETURN_GENERATOR | 21,240 | 1.5% |
| COPY_FREE_VARS | 3,820 | 0.3% |
| CALL_PY_EXACT_ARGS | 480 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,920 | 98.0% |
| CALL | 60 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,900 | 63.8% |
| LOAD_CONST | 1,080 | 36.2% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 1,559,440 | 92.9% |
| LOAD_FAST | 97,880 | 5.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 21,240 | 1.3% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,411,980 | 84.1% |
| RETURN_VALUE | 125,100 | 7.5% |
| JUMP_FORWARD | 97,900 | 5.8% |
| STORE_FAST | 43,460 | 2.6% |
| CALL_LEN | 240 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,734,880 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 746,540 | 43.0% |
| LOAD_GLOBAL_BUILTIN | 746,520 | 43.0% |
| STORE_FAST | 168,280 | 9.7% |
| LOAD_FAST_LOAD_FAST | 73,600 | 4.2% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 455,080 | 74.6% |
| LOAD_CONST | 81,020 | 13.3% |
| LOAD_FAST | 46,840 | 7.7% |
| CALL_LEN | 21,120 | 3.5% |
| LOAD_DEREF | 4,760 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 388,280 | 63.7% |
| LOAD_FAST | 218,060 | 35.8% |
| POP_JUMP_IF_TRUE | 3,300 | 0.5% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 298,120 | 71.5% |
| LOAD_CONST | 78,720 | 18.9% |
| LOAD_ATTR_SLOT | 25,040 | 6.0% |
| LOAD_FAST_LOAD_FAST | 9,420 | 2.3% |
| LOAD_FAST | 3,080 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 255,980 | 61.4% |
| POP_JUMP_IF_FALSE | 115,200 | 27.6% |
| COPY | 41,100 | 9.9% |
| POP_JUMP_IF_TRUE | 4,640 | 1.1% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,947,940 | 77.3% |
| EXTENDED_ARG | 299,760 | 11.9% |
| GET_ITER | 265,060 | 10.5% |
| LOAD_FAST | 7,480 | 0.3% |
| FOR_ITER | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,240,700 | 88.9% |
| POP_TOP | 279,720 | 11.1% |
| RESUME | 100 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,284,260 | 52.7% |
| GET_ITER | 4,567,940 | 45.6% |
| SWAP | 133,240 | 1.3% |
| JUMP_BACKWARD | 22,400 | 0.2% |
| EXTENDED_ARG | 14,800 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,531,980 | 45.2% |
| ENTER_EXECUTOR | 3,926,680 | 39.2% |
| LOAD_FAST | 1,394,760 | 13.9% |
| SWAP | 118,980 | 1.2% |
| RETURN_CONST | 16,720 | 0.2% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 140 | 63.6% |
| GET_ITER | 60 | 27.3% |
| FOR_ITER | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 140 | 63.6% |
| LOAD_FAST | 80 | 36.4% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 149,940 | 49.2% |
| LOAD_FAST | 118,040 | 38.8% |
| SWAP | 31,600 | 10.4% |
| JUMP_BACKWARD | 2,720 | 0.9% |
| GET_ITER | 2,040 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 159,580 | 52.4% |
| RETURN_CONST | 118,080 | 38.8% |
| SWAP | 21,280 | 7.0% |
| STORE_FAST_LOAD_FAST | 2,540 | 0.8% |
| LOAD_FAST | 2,080 | 0.7% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 479,880 | 59.9% |
| LOAD_FAST_LOAD_FAST | 319,360 | 39.9% |
| LOAD_ATTR | 1,120 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 291,340 | 36.4% |
| CALL_BUILTIN_O | 160,480 | 20.0% |
| LOAD_ATTR_METHOD_NO_DICT | 84,240 | 10.5% |
| RETURN_VALUE | 78,100 | 9.8% |
| TO_BOOL_BOOL | 44,760 | 5.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 8,528,440 | 47.4% |
| LOAD_FAST | 5,266,840 | 29.3% |
| RETURN_VALUE | 2,790,060 | 15.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 742,400 | 4.1% |
| LOAD_GLOBAL_MODULE | 226,560 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,173,320 | 45.4% |
| LOAD_FAST | 4,977,120 | 27.7% |
| LOAD_CONST | 3,139,800 | 17.4% |
| LOAD_FAST_LOAD_FAST | 1,095,700 | 6.1% |
| LOAD_GLOBAL_MODULE | 308,960 | 1.7% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,967,680 | 90.0% |
| LOAD_DEREF | 288,600 | 8.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 22,760 | 0.7% |
| ENTER_EXECUTOR | 8,660 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 4,960 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,063,820 | 32.2% |
| LOAD_FAST_LOAD_FAST | 1,027,380 | 31.1% |
| LOAD_CONST | 506,820 | 15.4% |
| LOAD_FAST | 422,200 | 12.8% |
| CALL_PY_WITH_DEFAULTS | 206,840 | 6.3% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 8,783,580 | 99.9% |
| LOAD_ATTR | 3,420 | 0.0% |
| LOAD_FAST | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 6,228,100 | 70.9% |
| LOAD_GLOBAL_MODULE | 1,172,440 | 13.3% |
| PUSH_NULL | 664,540 | 7.6% |
| BUILD_TUPLE | 635,560 | 7.2% |
| JUMP_FORWARD | 28,080 | 0.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 882,440 | 92.8% |
| LOAD_FAST_LOAD_FAST | 67,740 | 7.1% |
| LOAD_ATTR | 820 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 742,400 | 78.1% |
| CONTAINS_OP | 91,600 | 9.6% |
| CALL_PY_EXACT_ARGS | 79,360 | 8.3% |
| STORE_FAST | 23,820 | 2.5% |
| LOAD_FAST | 11,140 | 1.2% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,598,120 | 98.4% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 28,660 | 0.8% |
| LOAD_FAST_LOAD_FAST | 15,260 | 0.4% |
| ENTER_EXECUTOR | 14,020 | 0.4% |
| LOAD_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,584,880 | 43.3% |
| LOAD_GLOBAL_BUILTIN | 1,411,960 | 38.6% |
| FORMAT_SIMPLE | 571,980 | 15.6% |
| CONTAINS_OP | 39,360 | 1.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 28,660 | 0.8% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,283,820 | 95.2% |
| ENTER_EXECUTOR | 80,640 | 2.3% |
| BINARY_SUBSCR_DICT | 32,600 | 0.9% |
| STORE_FAST_LOAD_FAST | 21,760 | 0.6% |
| LOAD_ATTR_SLOT | 9,620 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,398,340 | 98.6% |
| RETURN_VALUE | 17,120 | 0.5% |
| STORE_FAST | 16,640 | 0.5% |
| COPY | 8,560 | 0.2% |
| SET_ADD | 4,160 | 0.1% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,507,460 | 83.5% |
| LOAD_DEREF | 1,907,120 | 9.6% |
| COPY | 468,480 | 2.4% |
| LOAD_ATTR_SLOT | 427,180 | 2.2% |
| LOAD_FAST_LOAD_FAST | 384,820 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,528,440 | 43.1% |
| LOAD_FAST | 3,659,180 | 18.5% |
| CALL_ISINSTANCE | 2,144,900 | 10.8% |
| LOAD_CONST | 869,120 | 4.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 714,760 | 3.6% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,474,660 | 27.0% |
| RESUME_CHECK | 11,675,780 | 20.4% |
| STORE_FAST | 8,397,540 | 14.7% |
| LOAD_GLOBAL_BUILTIN | 7,512,840 | 13.1% |
| POP_JUMP_IF_FALSE | 4,522,160 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,831,920 | 57.3% |
| CALL_ISINSTANCE | 8,206,520 | 14.3% |
| LOAD_GLOBAL_BUILTIN | 7,512,840 | 13.1% |
| BUILD_TUPLE | 3,750,620 | 6.5% |
| LOAD_FAST_LOAD_FAST | 2,805,380 | 4.9% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,738,860 | 45.0% |
| STORE_FAST | 3,737,080 | 13.2% |
| POP_JUMP_IF_FALSE | 2,843,720 | 10.0% |
| STORE_FAST_STORE_FAST | 1,826,960 | 6.5% |
| MAKE_FUNCTION | 1,411,960 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,929,640 | 38.6% |
| LOAD_ATTR_MODULE | 8,783,580 | 31.0% |
| CALL_ISINSTANCE | 6,260,220 | 22.1% |
| LOAD_FAST_LOAD_FAST | 641,980 | 2.3% |
| LOAD_ATTR | 560,540 | 2.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,233,040 | 35.0% |
| CACHE | 8,473,720 | 20.8% |
| SEND_GEN | 3,781,520 | 9.3% |
| LOAD_ATTR_PROPERTY | 3,398,340 | 8.4% |
| POP_TOP | 3,215,160 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,229,960 | 42.4% |
| LOAD_GLOBAL_BUILTIN | 11,675,780 | 28.7% |
| POP_TOP | 6,247,400 | 15.4% |
| JUMP_BACKWARD_NO_INTERRUPT | 3,781,500 | 9.3% |
| LOAD_DEREF | 754,680 | 1.9% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 3,781,540 | 78.6% |
| LOAD_CONST | 1,029,860 | 21.4% |
| SEND | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,781,520 | 78.6% |
| POP_TOP | 1,029,940 | 21.4% |
| RESUME | 80 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 139,560 | 84.1% |
| LOAD_FAST_LOAD_FAST | 25,880 | 15.6% |
| STORE_ATTR | 560 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,180 | 38.1% |
| BUILD_LIST | 35,100 | 21.1% |
| LOAD_FAST | 32,200 | 19.4% |
| RETURN_CONST | 14,180 | 8.5% |
| LOAD_FAST_LOAD_FAST | 14,040 | 8.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,857,360 | 46.4% |
| LOAD_FAST | 1,598,800 | 39.9% |
| SWAP | 468,480 | 11.7% |
| STORE_ATTR_SLOT | 36,820 | 0.9% |
| ENTER_EXECUTOR | 24,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,132,440 | 28.3% |
| LOAD_FAST_LOAD_FAST | 871,540 | 21.8% |
| ENTER_EXECUTOR | 811,660 | 20.3% |
| LOAD_GLOBAL_MODULE | 475,440 | 11.9% |
| RETURN_CONST | 416,840 | 10.4% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,392,660 | 90.3% |
| RETURN_VALUE | 74,920 | 4.9% |
| CALL_BUILTIN_O | 65,800 | 4.3% |
| LOAD_FAST_LOAD_FAST | 7,900 | 0.5% |
| STORE_SUBSCR | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 1,350,900 | 87.6% |
| LOAD_FAST | 78,640 | 5.1% |
| LOAD_GLOBAL_MODULE | 63,640 | 4.1% |
| POP_EXCEPT | 33,260 | 2.2% |
| JUMP_BACKWARD | 14,880 | 1.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,935,120 | 48.5% |
| LOAD_FAST | 1,430,360 | 35.8% |
| LOAD_ATTR_SLOT | 305,180 | 7.6% |
| STORE_FAST_LOAD_FAST | 125,240 | 3.1% |
| ENTER_EXECUTOR | 123,660 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,781,080 | 69.7% |
| POP_JUMP_IF_FALSE | 1,140,560 | 28.6% |
| TO_BOOL_ALWAYS_TRUE | 36,380 | 0.9% |
| UNARY_NOT | 28,900 | 0.7% |
| TO_BOOL_NONE | 5,860 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 27,040,960 | 75.3% |
| LOAD_FAST | 3,142,180 | 8.7% |
| COPY | 1,800,240 | 5.0% |
| RETURN_VALUE | 1,686,080 | 4.7% |
| LOAD_ATTR_SLOT | 645,000 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 26,999,700 | 75.2% |
| POP_JUMP_IF_TRUE | 6,011,460 | 16.7% |
| EXTENDED_ARG | 1,987,400 | 5.5% |
| UNARY_NOT | 925,500 | 2.6% |
| TO_BOOL_NONE | 200 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 143,600 | 79.5% |
| LOAD_FAST | 36,880 | 20.4% |
| TO_BOOL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 178,360 | 98.8% |
| EXTENDED_ARG | 2,060 | 1.1% |
| POP_JUMP_IF_TRUE | 140 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 22,580 | 59.6% |
| LOAD_FAST | 6,560 | 17.3% |
| BINARY_SLICE | 6,040 | 15.9% |
| RETURN_VALUE | 2,480 | 6.5% |
| TO_BOOL | 220 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 26,440 | 69.8% |
| POP_JUMP_IF_FALSE | 11,420 | 30.1% |
| TO_BOOL_NONE | 20 | 0.1% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,448,360 | 80.9% |
| COPY | 261,560 | 8.6% |
| RETURN_CONST | 249,320 | 8.2% |
| LOAD_ATTR_SLOT | 29,700 | 1.0% |
| RETURN_VALUE | 15,060 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,475,660 | 81.8% |
| POP_JUMP_IF_TRUE | 520,920 | 17.2% |
| EXTENDED_ARG | 10,020 | 0.3% |
| UNARY_NOT | 7,880 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 5,840 | 0.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 842,940 | 72.5% |
| LOAD_ATTR_SLOT | 141,560 | 12.2% |
| COPY | 127,360 | 11.0% |
| RETURN_VALUE | 42,080 | 3.6% |
| TO_BOOL_NONE | 5,660 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 699,240 | 60.2% |
| POP_JUMP_IF_TRUE | 457,020 | 39.3% |
| TO_BOOL_NONE | 5,660 | 0.5% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,917,000 | 98.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 21,560 | 1.1% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,886,040 | 97.3% |
| STORE_FAST_STORE_FAST | 52,600 | 2.7% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 5,933,660 | 95.4% |
| RETURN_VALUE | 116,400 | 1.9% |
| BUILD_TUPLE | 97,360 | 1.6% |
| LOAD_FAST | 37,720 | 0.6% |
| STORE_FAST | 24,280 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 6,195,680 | 99.6% |
| STORE_FAST | 24,340 | 0.4% |
| STORE_DEREF | 1,420 | 0.0% |


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
|     deferred | 18,520 | 2.1% |
|          hit | 867,940 | 97.8% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 40.7% |
| Failure | 700 | 59.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 660 | 94.3% |
| subtract other | 40 | 5.7% |


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
|     deferred | 21,940 | 0.9% |
|          hit | 2,451,660 | 99.1% |
|         miss | 6,340 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 69.1% |
| Failure | 340 | 30.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 240 | 70.6% |
| out of range | 100 | 29.4% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,141,820 | 2.4% |
|          hit | 88,524,280 | 97.6% |
|         miss | 684,600 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 29,140 | 86.2% |
| Failure | 4,660 | 13.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 2,420 | 51.9% |
| class no vectorcall | 1,140 | 24.5% |
| meth descr varargs keywords | 300 | 6.4% |
| metaclass | 220 | 4.7% |
| no dict | 180 | 3.9% |
| meth descr method fastcall keywords | 140 | 3.0% |
| cfunc noargs | 100 | 2.1% |
| wrong number arguments | 80 | 1.7% |
| meth descr varargs | 80 | 1.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 961,480 | 47.1% |
|          hit | 1,074,720 | 52.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 800 | 15.2% |
| Failure | 4,480 | 84.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 1,960 | 43.8% |
| different types | 1,500 | 33.5% |
| other | 420 | 9.4% |
| set | 220 | 4.9% |
| string | 180 | 4.0% |
| big int | 120 | 2.7% |
| bool | 80 | 1.8% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,198,580 | 32.5% |
|          hit | 12,851,460 | 67.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,660 | 21.3% |
| Failure | 6,120 | 78.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 3,340 | 54.6% |
| dict values | 740 | 12.1% |
| dict keys | 460 | 7.5% |
| enumerate | 400 | 6.5% |
| set | 340 | 5.6% |
| itertools | 340 | 5.6% |
| other | 200 | 3.3% |
| ascii string | 180 | 2.9% |
| reversed list | 120 | 2.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,664,580 | 17.0% |
|        deopt | 439,820 | 0.7% |
|          hit | 51,800,320 | 82.6% |
|         miss | 10,161,560 | 16.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 212,360 | 94.6% |
| Failure | 12,200 | 5.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 9,800 | 80.3% |
| method | 1,900 | 15.6% |
| mutable class | 380 | 3.1% |
| builtin class method | 120 | 1.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 18,940 | 0.0% |
|          hit | 85,569,840 | 100.0% |
|         miss | 4,240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 14,860 | 100.0% |
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
|     deferred | 140 | 0.0% |
|          hit | 4,811,540 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 140 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,918,340 | 44.0% |
|          hit | 2,407,100 | 55.2% |
|         miss | 1,953,600 | 44.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 38,380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 380 | 0.0% |
|          hit | 1,558,820 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 5,564,980 | 9.9% |
|          hit | 50,373,860 | 89.9% |
|         miss | 3,203,420 | 5.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 67,960 | 96.5% |
| Failure | 2,440 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 1,040 | 42.6% |
| other | 660 | 27.0% |
| dict | 540 | 22.1% |
| tuple | 120 | 4.9% |
| set | 80 | 3.3% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 15,660 | 0.1% |
|          hit | 15,645,940 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 83.0% |
| Failure | 160 | 17.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 160 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 373,761,800 | 48.1% |
| Not specialized | 62,968,920 | 8.1% |
| Specialized hits | 323,940,260 | 41.7% |
| Specialized misses | 16,014,440 | 2.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 10,664,580 | 38.7% |
| FOR_ITER | 6,198,580 | 22.5% |
| TO_BOOL | 5,564,980 | 20.2% |
| CALL | 2,141,820 | 7.8% |
| STORE_ATTR | 1,918,340 | 7.0% |
| COMPARE_OP | 961,480 | 3.5% |
| BINARY_SUBSCR | 21,940 | 0.1% |
| LOAD_GLOBAL | 18,940 | 0.1% |
| BINARY_OP | 18,520 | 0.1% |
| UNPACK_SEQUENCE | 15,660 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 7,348,960 | 45.9% |
| TO_BOOL_ALWAYS_TRUE | 2,248,700 | 14.0% |
| STORE_ATTR_SLOT | 1,953,600 | 12.2% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,521,320 | 9.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,226,040 | 7.7% |
| TO_BOOL_NONE | 638,500 | 4.0% |
| CALL_PY_EXACT_ARGS | 385,400 | 2.4% |
| TO_BOOL_STR | 301,780 | 1.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 264,880 | 1.7% |
| LOAD_ATTR_PROPERTY | 49,360 | 0.3% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 10,429,680 | 21.6% |
| Calls to Python functions inlined | 37,823,640 | 78.4% |
| Calls via PyEval_EvalFrame (total) | 10,429,680 | 21.6% |
| Calls via PyEval_EvalFrame (vector) | 4,517,080 | 9.4% |
| Calls via PyEval_EvalFrame (generator) | 5,912,600 | 12.3% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 4,517,080 | 9.4% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,068,500 | 2.2% |
| Calls via PyEval_EvalFrame (function ex) | 84,000 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 3,204,220 | 6.6% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 76,480 | 0.2% |
| Frames pushed | 35,008,520 | 72.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 35,210,080 | 36.7% |
| Frees to freelist | 35,363,580 |  |
| Allocations | 60,749,740 | 63.3% |
| Allocations to 512 bytes | 60,673,220 | 63.2% |
| Allocations to 4 kbytes | 76,360 | 0.1% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 61,796,372 |  |
| New values | 151,840 |  |
| Interpreter increfs | 333,852,080 | 58.0% |
| Interpreter decrefs | 396,057,240 | 59.8% |
| Increfs | 241,524,988 | 42.0% |
| Decrefs | 266,426,700 | 40.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 12,679,616 |  |
| Method cache misses | 645,844 |  |
| Method cache collisions | 657,627 |  |
| Method cache dunder hits | 63,385,147 |  |
| Method cache dunder misses | 15,433 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 640 | 134,200 | 2,274,120 |
| 1 | 60 | 82,580 | 1,692,320 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 5,620 |  |
| Traces created | 2,860 | 50.9% |
| Trace stack overflow | 20 | 0.4% |
| Trace stack underflow | 20 | 0.4% |
| Trace too long | 0 | 0.0% |
| Trace too short | 2,760 | 49.1% |
| Inner loop found | 60 | 1.1% |
| Recursive call | 200 | 3.6% |
| Low confidence | 100 | 1.8% |
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
| <= 16 | 480 | 16.8% |
| <= 32 | 900 | 31.5% |
| <= 64 | 720 | 25.2% |
| <= 128 | 700 | 24.5% |
| <= 256 | 60 | 2.1% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 340 | 11.9% |
| <= 16 | 500 | 17.5% |
| <= 32 | 820 | 28.7% |
| <= 64 | 520 | 18.2% |
| <= 128 | 60 | 2.1% |
| <= 256 | 40 | 1.4% |


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
| FOR_ITER_GEN | 2,760 |
| LOAD_ATTR_PROPERTY | 600 |
| CALL_PY_WITH_DEFAULTS | 180 |
| YIELD_VALUE | 140 |
| CALL_LIST_APPEND | 120 |
| CALL | 100 |
| CALL_KW | 80 |
| BINARY_OP_INPLACE_ADD_UNICODE | 20 |
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
