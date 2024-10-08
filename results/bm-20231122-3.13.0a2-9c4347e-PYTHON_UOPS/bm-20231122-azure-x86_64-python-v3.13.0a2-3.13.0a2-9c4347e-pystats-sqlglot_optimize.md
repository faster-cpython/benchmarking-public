
# Pystats results

- benchmark: sqlglot_optimize
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 160,612,000 | 17.5% | 17.5% |  |
| LOAD_GLOBAL_BUILTIN | 71,919,600 | 7.8% | 25.3% | 0.0% |
| POP_JUMP_IF_FALSE | 46,935,520 | 5.1% | 30.4% |  |
| RESUME_CHECK | 45,031,460 | 4.9% | 35.4% | 0.0% |
| TO_BOOL_BOOL | 44,745,060 | 4.9% | 40.2% | 0.0% |
| CALL_ISINSTANCE | 37,015,580 | 4.0% | 44.3% |  |
| STORE_FAST | 36,678,520 | 4.0% | 48.3% |  |
| LOAD_GLOBAL_MODULE | 34,717,580 | 3.8% | 52.0% | 0.0% |
| RETURN_VALUE | 29,621,620 | 3.2% | 55.3% |  |
| CALL_PY_EXACT_ARGS | 23,469,820 | 2.6% | 57.8% | 1.7% |
| JUMP_BACKWARD | 22,471,040 | 2.4% | 60.3% |  |
| LOAD_ATTR_SLOT | 20,081,520 | 2.2% | 62.5% | 36.6% |
| LOAD_ATTR_METHOD_NO_DICT | 19,918,260 | 2.2% | 64.6% | 0.0% |
| FOR_ITER | 19,176,320 | 2.1% | 66.7% |  |
| POP_TOP | 16,728,300 | 1.8% | 68.5% |  |
| BUILD_TUPLE | 15,009,600 | 1.6% | 70.2% |  |
| STORE_FAST_STORE_FAST | 14,008,320 | 1.5% | 71.7% |  |
| LOAD_FAST_LOAD_FAST | 13,543,560 | 1.5% | 73.2% |  |
| LOAD_CONST | 13,266,320 | 1.4% | 74.6% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,736,100 | 1.4% | 76.0% |  |
| GET_ITER | 12,174,640 | 1.3% | 77.3% |  |
| FOR_ITER_LIST | 11,034,480 | 1.2% | 78.5% |  |
| POP_JUMP_IF_TRUE | 10,674,080 | 1.2% | 79.7% |  |
| INTERPRETER_EXIT | 10,429,540 | 1.1% | 80.8% |  |
| YIELD_VALUE | 10,029,280 | 1.1% | 81.9% |  |
| LOAD_ATTR_MODULE | 9,715,380 | 1.1% | 83.0% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,243,360 | 1.0% | 84.0% |  |
| BUILD_LIST | 6,904,400 | 0.8% | 84.8% |  |
| SWAP | 6,806,880 | 0.7% | 85.5% |  |
| LOAD_FAST_AND_CLEAR | 6,013,920 | 0.7% | 86.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 5,393,460 | 0.6% | 86.7% | 0.0% |
| RETURN_CONST | 5,387,040 | 0.6% | 87.3% |  |
| COPY | 5,082,080 | 0.6% | 87.9% |  |
| SEND_GEN | 4,811,540 | 0.5% | 88.4% |  |
| LOAD_DEREF | 4,611,120 | 0.5% | 88.9% |  |
| POP_JUMP_IF_NOT_NONE | 4,318,080 | 0.5% | 89.4% |  |
| STORE_ATTR_SLOT | 4,194,580 | 0.5% | 89.8% | 46.4% |
| PUSH_NULL | 4,093,840 | 0.4% | 90.3% |  |
| CALL_BUILTIN_O | 4,030,440 | 0.4% | 90.7% |  |
| MAP_ADD | 4,025,760 | 0.4% | 91.2% |  |
| TO_BOOL_ALWAYS_TRUE | 3,998,560 | 0.4% | 91.6% | 56.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 3,781,600 | 0.4% | 92.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,657,540 | 0.4% | 92.4% | 41.6% |
| LOAD_ATTR_PROPERTY | 3,447,700 | 0.4% | 92.8% | 1.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,320,400 | 0.4% | 93.1% | 37.2% |
| RETURN_GENERATOR | 3,215,520 | 0.4% | 93.5% |  |
| EXTENDED_ARG | 3,172,640 | 0.3% | 93.8% |  |
| TO_BOOL_NONE | 3,135,300 | 0.3% | 94.2% | 20.4% |
| UNPACK_SEQUENCE_TUPLE | 2,909,840 | 0.3% | 94.5% |  |
| MAKE_FUNCTION | 2,530,560 | 0.3% | 94.8% |  |
| FOR_ITER_GEN | 2,520,520 | 0.3% | 95.0% |  |
| TO_BOOL | 2,432,800 | 0.3% | 95.3% |  |
| COPY_FREE_VARS | 2,325,360 | 0.3% | 95.6% |  |
| BUILD_MAP | 2,312,480 | 0.3% | 95.8% |  |
| FORMAT_SIMPLE | 1,910,240 | 0.2% | 96.0% |  |
| CALL_TYPE_1 | 1,734,960 | 0.2% | 96.2% |  |
| CALL_TUPLE_1 | 1,678,720 | 0.2% | 96.4% |  |
| MAKE_CELL | 1,622,560 | 0.2% | 96.6% |  |
| CALL_LIST_APPEND | 1,611,780 | 0.2% | 96.7% |  |
| STORE_SUBSCR_DICT | 1,558,820 | 0.2% | 96.9% |  |
| CALL | 1,518,680 | 0.2% | 97.1% |  |
| JUMP_FORWARD | 1,482,080 | 0.2% | 97.2% |  |
| TO_BOOL_STR | 1,480,960 | 0.2% | 97.4% | 20.4% |
| CALL_PY_WITH_DEFAULTS | 1,463,720 | 0.2% | 97.6% | 1.8% |
| IS_OP | 1,430,400 | 0.2% | 97.7% |  |
| BINARY_SUBSCR_LIST_INT | 1,315,780 | 0.1% | 97.9% | 0.5% |
| CALL_BUILTIN_FAST | 1,215,920 | 0.1% | 98.0% | 0.5% |
| CALL_METHOD_DESCRIPTOR_O | 1,106,100 | 0.1% | 98.1% |  |
| END_SEND | 1,030,080 | 0.1% | 98.2% |  |
| GET_YIELD_FROM_ITER | 1,030,080 | 0.1% | 98.3% |  |
| BUILD_STRING | 1,029,280 | 0.1% | 98.5% |  |
| COMPARE_OP | 1,013,220 | 0.1% | 98.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 1,009,420 | 0.1% | 98.7% |  |
| UNARY_NOT | 962,400 | 0.1% | 98.8% |  |
| SET_FUNCTION_ATTRIBUTE | 872,000 | 0.1% | 98.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 812,000 | 0.1% | 99.0% | 1.9% |
| LOAD_ATTR | 751,180 | 0.1% | 99.0% |  |
| CONTAINS_OP | 662,240 | 0.1% | 99.1% |  |
| COMPARE_OP_INT | 636,980 | 0.1% | 99.2% |  |
| BINARY_SUBSCR_DICT | 597,700 | 0.1% | 99.2% |  |
| FOR_ITER_TUPLE | 595,520 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_INT | 551,920 | 0.1% | 99.4% |  |
| CALL_KW | 526,880 | 0.1% | 99.4% |  |
| BINARY_SUBSCR_STR_INT | 452,100 | 0.0% | 99.5% |  |
| COMPARE_OP_STR | 437,740 | 0.0% | 99.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 391,640 | 0.0% | 99.6% | 67.6% |
| STORE_FAST_LOAD_FAST | 317,920 | 0.0% | 99.6% |  |
| UNPACK_EX | 291,360 | 0.0% | 99.6% |  |
| BINARY_OP_SUBTRACT_INT | 290,400 | 0.0% | 99.7% |  |
| END_FOR | 279,980 | 0.0% | 99.7% |  |
| LIST_APPEND | 234,560 | 0.0% | 99.7% |  |
| POP_JUMP_IF_NONE | 233,120 | 0.0% | 99.7% |  |
| NOP | 215,280 | 0.0% | 99.8% |  |
| CALL_FUNCTION_EX | 193,760 | 0.0% | 99.8% |  |
| DICT_MERGE | 184,640 | 0.0% | 99.8% |  |
| TO_BOOL_INT | 180,560 | 0.0% | 99.8% |  |
| CALL_BUILTIN_CLASS | 179,260 | 0.0% | 99.9% |  |
| CALL_LEN | 171,940 | 0.0% | 99.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 166,000 | 0.0% | 99.9% |  |
| CALL_INTRINSIC_1 | 99,920 | 0.0% | 99.9% |  |
| LIST_EXTEND | 99,920 | 0.0% | 99.9% |  |
| BINARY_SLICE | 94,880 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 92,120 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 76,480 | 0.0% | 99.9% |  |
| POP_EXCEPT | 76,480 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 76,480 | 0.0% | 100.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 73,580 | 0.0% | 100.0% |  |
| BUILD_SET | 56,480 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 38,220 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 37,880 | 0.0% | 100.0% | 5.3% |
| STORE_DEREF | 31,840 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 29,560 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 25,400 | 0.0% | 100.0% |  |
| BINARY_OP | 20,740 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 18,560 | 0.0% | 100.0% |  |
| SET_ADD | 17,920 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 16,600 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 7,160 | 0.0% | 100.0% |  |
| RESUME | 6,340 | 0.0% | 100.0% | 10.1% |
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
| EXIT_INIT_CHECK | 140 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 140 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 140 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 40,953,860 | 4.5% | 4.5% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 35,059,160 | 3.8% | 8.3% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 34,276,880 | 3.7% | 12.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 29,422,880 | 3.2% | 15.2% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 25,244,280 | 2.8% | 18.0% |
| RESUME_CHECK LOAD_FAST | 18,926,780 | 2.1% | 20.0% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 18,605,060 | 2.0% | 22.1% |
| LOAD_FAST LOAD_ATTR_SLOT | 16,863,600 | 1.8% | 23.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 15,603,660 | 1.7% | 25.6% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 14,924,020 | 1.6% | 27.2% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 14,582,080 | 1.6% | 28.8% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 14,480,040 | 1.6% | 30.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 14,305,920 | 1.6% | 31.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 12,677,620 | 1.4% | 33.3% |
| JUMP_BACKWARD FOR_ITER | 12,663,620 | 1.4% | 34.7% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 12,396,400 | 1.4% | 36.1% |
| STORE_FAST LOAD_FAST | 11,170,920 | 1.2% | 37.3% |
| LOAD_FAST RETURN_VALUE | 9,775,120 | 1.1% | 38.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 9,710,080 | 1.1% | 39.4% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 9,236,680 | 1.0% | 40.4% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 9,212,160 | 1.0% | 41.4% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 8,604,200 | 0.9% | 42.3% |
| RETURN_VALUE STORE_FAST | 8,571,680 | 0.9% | 43.3% |
| CACHE RESUME_CHECK | 8,473,580 | 0.9% | 44.2% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 7,527,700 | 0.8% | 45.0% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 7,190,320 | 0.8% | 45.8% |
| LOAD_ATTR_MODULE CALL_ISINSTANCE | 7,131,120 | 0.8% | 46.6% |
| STORE_FAST_STORE_FAST LOAD_FAST | 7,024,320 | 0.8% | 47.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 7,013,720 | 0.8% | 48.1% |
| LOAD_FAST BUILD_TUPLE | 6,913,120 | 0.8% | 48.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 6,663,880 | 0.7% | 49.6% |
| RESUME_CHECK POP_TOP | 6,247,400 | 0.7% | 50.3% |
| POP_TOP JUMP_BACKWARD | 6,012,540 | 0.7% | 50.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS GET_ITER | 6,000,280 | 0.7% | 51.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 5,547,040 | 0.6% | 52.2% |
| LOAD_FAST GET_ITER | 5,539,680 | 0.6% | 52.8% |
| JUMP_BACKWARD FOR_ITER_LIST | 5,529,100 | 0.6% | 53.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 5,513,160 | 0.6% | 54.0% |
| FOR_ITER_LIST STORE_FAST | 5,502,500 | 0.6% | 54.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 5,472,320 | 0.6% | 55.2% |
| GET_ITER FOR_ITER_LIST | 5,348,320 | 0.6% | 55.8% |
| BUILD_TUPLE YIELD_VALUE | 5,098,880 | 0.6% | 56.3% |
| LOAD_FAST BUILD_LIST | 5,031,120 | 0.5% | 56.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 4,974,920 | 0.5% | 57.4% |
| BUILD_TUPLE CALL_ISINSTANCE | 4,498,880 | 0.5% | 57.9% |
| RETURN_VALUE INTERPRETER_EXIT | 4,340,580 | 0.5% | 58.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 4,290,240 | 0.5% | 58.8% |
| MAP_ADD JUMP_BACKWARD | 4,025,760 | 0.4% | 59.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 4,018,780 | 0.4% | 59.7% |
| YIELD_VALUE INTERPRETER_EXIT | 4,007,140 | 0.4% | 60.2% |
| POP_JUMP_IF_TRUE LOAD_FAST | 3,956,960 | 0.4% | 60.6% |
| FOR_ITER_LIST JUMP_BACKWARD | 3,934,800 | 0.4% | 61.0% |
| STORE_FAST STORE_FAST | 3,927,040 | 0.4% | 61.4% |
| LOAD_FAST_AND_CLEAR LOAD_FAST_AND_CLEAR | 3,900,160 | 0.4% | 61.9% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_BUILTIN | 3,881,000 | 0.4% | 62.3% |
| BUILD_LIST RETURN_VALUE | 3,866,400 | 0.4% | 62.7% |
| RETURN_VALUE MAP_ADD | 3,850,560 | 0.4% | 63.1% |
| LOAD_FAST TO_BOOL_BOOL | 3,810,620 | 0.4% | 63.6% |
| LOAD_ATTR_SLOT LOAD_FAST | 3,805,420 | 0.4% | 64.0% |
| YIELD_VALUE YIELD_VALUE | 3,781,600 | 0.4% | 64.4% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 3,781,540 | 0.4% | 64.8% |
| SEND_GEN RESUME_CHECK | 3,781,520 | 0.4% | 65.2% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 3,781,500 | 0.4% | 65.6% |
| LOAD_GLOBAL_BUILTIN BUILD_TUPLE | 3,757,100 | 0.4% | 66.0% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_MODULE | 3,708,000 | 0.4% | 66.4% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 3,598,120 | 0.4% | 66.8% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 3,398,340 | 0.4% | 67.2% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 3,337,640 | 0.4% | 67.6% |
| POP_TOP RESUME_CHECK | 3,215,160 | 0.4% | 67.9% |
| CALL_BUILTIN_O RETURN_VALUE | 3,153,220 | 0.3% | 68.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 3,142,140 | 0.3% | 68.6% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 3,123,200 | 0.3% | 68.9% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST | 3,075,680 | 0.3% | 69.3% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST_LOAD_FAST | 3,027,760 | 0.3% | 69.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,996,960 | 0.3% | 69.9% |
| BUILD_TUPLE CALL_BUILTIN_O | 2,992,680 | 0.3% | 70.2% |
| FOR_ITER RETURN_CONST | 2,986,020 | 0.3% | 70.6% |
| POP_TOP LOAD_FAST | 2,958,780 | 0.3% | 70.9% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 2,790,060 | 0.3% | 71.2% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 2,783,680 | 0.3% | 71.5% |
| GET_ITER FOR_ITER | 2,744,440 | 0.3% | 71.8% |
| LOAD_FAST LOAD_CONST | 2,740,480 | 0.3% | 72.1% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 2,671,440 | 0.3% | 72.4% |
| CALL_METHOD_DESCRIPTOR_FAST RETURN_VALUE | 2,665,080 | 0.3% | 72.7% |
| LOAD_FAST COPY | 2,644,640 | 0.3% | 73.0% |
| RETURN_VALUE RETURN_VALUE | 2,577,980 | 0.3% | 73.3% |
| BUILD_LIST STORE_FAST | 2,569,440 | 0.3% | 73.5% |
| LOAD_FAST TO_BOOL_NONE | 2,556,420 | 0.3% | 73.8% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 2,543,680 | 0.3% | 74.1% |
| LOAD_CONST MAKE_FUNCTION | 2,530,560 | 0.3% | 74.4% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 2,474,780 | 0.3% | 74.6% |
| PUSH_NULL LOAD_FAST | 2,411,520 | 0.3% | 74.9% |
| TO_BOOL POP_JUMP_IF_FALSE | 2,410,660 | 0.3% | 75.2% |
| LOAD_FAST TO_BOOL | 2,409,640 | 0.3% | 75.4% |
| COPY_FREE_VARS RESUME_CHECK | 2,320,300 | 0.3% | 75.7% |
| COPY TO_BOOL_BOOL | 2,255,400 | 0.2% | 75.9% |
| FOR_ITER_GEN RESUME_CHECK | 2,240,700 | 0.2% | 76.2% |
| LOAD_FAST PUSH_NULL | 2,172,000 | 0.2% | 76.4% |
| LOAD_ATTR_SLOT CALL_ISINSTANCE | 2,150,240 | 0.2% | 76.6% |
| RETURN_VALUE TO_BOOL_BOOL | 2,141,240 | 0.2% | 76.9% |


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
| RESUME_CHECK | 8,473,580 | 81.2% |
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
| LOAD_ATTR_SLOT | 7,320 | 28.8% |
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
| LOAD_CONST | 24,320 | 63.6% |
| LOAD_FAST_LOAD_FAST | 12,880 | 33.7% |
| BINARY_SUBSCR | 420 | 1.1% |
| LOAD_FAST | 240 | 0.6% |
| LOAD_ATTR | 100 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 36,360 | 95.1% |
| BINARY_SUBSCR | 420 | 1.1% |
| BINARY_SUBSCR_DICT | 380 | 1.0% |
| BINARY_SUBSCR_LIST_INT | 160 | 0.4% |
| LOAD_ATTR | 140 | 0.4% |


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
| RETURN_CONST | 261,580 | 93.4% |
| LOAD_CONST | 7,040 | 2.5% |
| JUMP_BACKWARD | 6,240 | 2.2% |
| LOAD_FAST | 4,960 | 1.8% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |


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

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 100.0% |


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
| CALL_METHOD_DESCRIPTOR_NOARGS | 6,000,280 | 49.3% |
| LOAD_FAST | 5,539,680 | 45.5% |
| RETURN_GENERATOR | 280,000 | 2.3% |
| BUILD_TUPLE | 117,120 | 1.0% |
| LOAD_ATTR_SLOT | 90,480 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,348,320 | 43.9% |
| FOR_ITER | 2,744,440 | 22.5% |
| LOAD_FAST_AND_CLEAR | 2,113,760 | 17.4% |
| CALL_PY_EXACT_ARGS | 1,665,120 | 13.7% |
| FOR_ITER_GEN | 265,060 | 2.2% |


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
| RETURN_CONST | 2,081,820 | 20.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,530,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,411,960 | 55.8% |
| SET_FUNCTION_ATTRIBUTE | 869,760 | 34.4% |
| LOAD_FAST | 248,640 | 9.8% |
| STORE_FAST | 160 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 157,020 | 72.9% |
| POP_JUMP_IF_FALSE | 48,640 | 22.6% |
| STORE_FAST | 8,480 | 3.9% |
| POP_JUMP_IF_TRUE | 960 | 0.4% |
| RESUME | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,920 | 45.5% |
| LOAD_FAST_LOAD_FAST | 76,800 | 35.7% |
| LOAD_GLOBAL_MODULE | 37,560 | 17.4% |
| LOAD_GLOBAL_BUILTIN | 2,380 | 1.1% |
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
| RESUME_CHECK | 6,247,400 | 37.3% |
| CACHE | 1,905,720 | 11.4% |
| STORE_FAST | 1,888,480 | 11.3% |
| POP_JUMP_IF_FALSE | 1,586,400 | 9.5% |
| RETURN_CONST | 1,343,200 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,012,540 | 35.9% |
| RESUME_CHECK | 3,215,160 | 19.2% |
| LOAD_FAST | 2,958,780 | 17.7% |
| STORE_FAST | 1,886,080 | 11.3% |
| LOAD_GLOBAL_BUILTIN | 1,073,360 | 6.4% |


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
| LOAD_FAST | 2,172,000 | 53.1% |
| LOAD_ATTR_MODULE | 680,420 | 16.6% |
| CALL_BUILTIN_FAST | 571,980 | 14.0% |
| LOAD_DEREF | 508,800 | 12.4% |
| LOAD_FAST_LOAD_FAST | 66,080 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,411,520 | 58.9% |
| LOAD_FAST_LOAD_FAST | 1,488,160 | 36.4% |
| LOAD_CONST | 60,480 | 1.5% |
| LOAD_DEREF | 49,920 | 1.2% |
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
| LOAD_FAST | 9,775,120 | 33.0% |
| BUILD_LIST | 3,866,400 | 13.1% |
| CALL_BUILTIN_O | 3,153,220 | 10.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,665,080 | 9.0% |
| RETURN_VALUE | 2,577,980 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,571,680 | 28.9% |
| INTERPRETER_EXIT | 4,340,580 | 14.7% |
| MAP_ADD | 3,850,560 | 13.0% |
| LOAD_ATTR_METHOD_NO_DICT | 2,790,060 | 9.4% |
| RETURN_VALUE | 2,577,980 | 8.7% |


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
| LOAD_FAST | 2,409,640 | 99.0% |
| COPY | 10,080 | 0.4% |
| RETURN_CONST | 3,000 | 0.1% |
| CALL | 2,580 | 0.1% |
| TO_BOOL | 2,360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,410,660 | 99.1% |
| POP_JUMP_IF_TRUE | 11,280 | 0.5% |
| TO_BOOL_BOOL | 4,180 | 0.2% |
| TO_BOOL_NONE | 2,680 | 0.1% |
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
| RETURN_VALUE | 10,880 | 52.5% |
| LOAD_FAST_LOAD_FAST | 4,560 | 22.0% |
| BUILD_LIST | 2,240 | 10.8% |
| CALL_BUILTIN_CLASS | 1,400 | 6.8% |
| BINARY_OP | 780 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,600 | 51.1% |
| GET_ITER | 4,160 | 20.1% |
| LOAD_FAST_LOAD_FAST | 2,260 | 10.9% |
| STORE_FAST | 2,040 | 9.8% |
| BINARY_OP | 780 | 3.8% |


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
| LOAD_FAST | 5,031,120 | 72.9% |
| STORE_FAST | 1,275,200 | 18.5% |
| POP_JUMP_IF_NOT_NONE | 161,760 | 2.3% |
| SWAP | 138,880 | 2.0% |
| RESUME_CHECK | 84,820 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,866,400 | 56.0% |
| STORE_FAST | 2,569,440 | 37.2% |
| LOAD_FAST | 168,320 | 2.4% |
| SWAP | 138,880 | 2.0% |
| LOAD_DEREF | 98,960 | 1.4% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,968,640 | 85.1% |
| LOAD_CONST | 101,280 | 4.4% |
| RESUME_CHECK | 57,320 | 2.5% |
| CALL_INTRINSIC_1 | 49,760 | 2.2% |
| LOAD_FAST_LOAD_FAST | 45,920 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,968,640 | 85.1% |
| STORE_FAST | 101,760 | 4.4% |
| LOAD_DEREF | 98,880 | 4.3% |
| LOAD_FAST | 52,800 | 2.3% |
| CALL_PY_EXACT_ARGS | 46,640 | 2.0% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,800 | 86.4% |
| SWAP | 6,240 | 11.0% |
| LOAD_GLOBAL_MODULE | 1,260 | 2.2% |
| JUMP_FORWARD | 160 | 0.3% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 48,760 | 86.3% |
| SWAP | 6,240 | 11.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 2.2% |
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
| LOAD_FAST | 6,913,120 | 46.1% |
| LOAD_GLOBAL_BUILTIN | 3,757,100 | 25.0% |
| CALL_TUPLE_1 | 1,411,980 | 9.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,249,900 | 8.3% |
| LOAD_ATTR_MODULE | 639,360 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 5,098,880 | 34.0% |
| CALL_ISINSTANCE | 4,498,880 | 30.0% |
| CALL_BUILTIN_O | 2,992,680 | 19.9% |
| CALL_METHOD_DESCRIPTOR_O | 971,480 | 6.5% |
| LOAD_CONST | 884,480 | 5.9% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,288,840 | 84.9% |
| LOAD_CONST | 67,440 | 4.4% |
| RETURN_GENERATOR | 47,480 | 3.1% |
| LOAD_ATTR_MODULE | 26,360 | 1.7% |
| LOAD_ATTR_SLOT | 24,280 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 1,215,880 | 80.1% |
| STORE_FAST | 74,180 | 4.9% |
| GET_ITER | 40,740 | 2.7% |
| RETURN_VALUE | 37,160 | 2.4% |
| CALL_LIST_APPEND | 24,340 | 1.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 184,640 | 95.3% |
| BUILD_CONST_KEY_MAP | 5,440 | 2.8% |
| RETURN_GENERATOR | 2,400 | 1.2% |
| CALL_INTRINSIC_1 | 1,040 | 0.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 140 | 0.1% |

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
| LOAD_CONST | 526,880 | 100.0% |

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
| RETURN_VALUE | 266,800 | 26.3% |
| LOAD_ATTR | 255,720 | 25.2% |
| LOAD_FAST | 182,040 | 18.0% |
| LOAD_GLOBAL_MODULE | 98,420 | 9.7% |
| CALL_BUILTIN_CLASS | 86,540 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 613,760 | 60.6% |
| RETURN_VALUE | 272,500 | 26.9% |
| POP_JUMP_IF_TRUE | 66,820 | 6.6% |
| COPY | 54,420 | 5.4% |
| COMPARE_OP | 4,580 | 0.5% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 181,280 | 27.4% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 150,020 | 22.7% |
| LOAD_FAST_LOAD_FAST | 125,440 | 18.9% |
| LOAD_FAST | 115,680 | 17.5% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 40,600 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 525,280 | 79.3% |
| POP_JUMP_IF_TRUE | 118,560 | 17.9% |
| STORE_FAST | 18,400 | 2.8% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,644,640 | 52.0% |
| CALL_ISINSTANCE | 1,405,620 | 27.7% |
| IS_OP | 746,560 | 14.7% |
| RETURN_VALUE | 122,100 | 2.4% |
| COMPARE_OP | 54,420 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,255,400 | 44.4% |
| TO_BOOL_ALWAYS_TRUE | 1,935,500 | 38.1% |
| LOAD_ATTR_SLOT | 468,480 | 9.2% |
| TO_BOOL_NONE | 262,520 | 5.2% |
| TO_BOOL_STR | 127,360 | 2.5% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,215,880 | 52.3% |
| CALL_PY_EXACT_ARGS | 1,101,600 | 47.4% |
| CALL_PY_WITH_DEFAULTS | 3,820 | 0.2% |
| CALL_FUNCTION_EX | 3,600 | 0.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,320,300 | 99.8% |
| RETURN_GENERATOR | 4,800 | 0.2% |
| RESUME | 260 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 98,880 | 53.6% |
| LOAD_FAST | 46,880 | 25.4% |
| RETURN_VALUE | 31,040 | 16.8% |
| BUILD_MAP | 4,480 | 2.4% |
| DICT_UPDATE | 2,080 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 184,640 | 100.0% |


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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,096,320 | 66.1% |
| JUMP_BACKWARD | 556,320 | 17.5% |
| POP_JUMP_IF_TRUE | 450,400 | 14.2% |
| GET_ITER | 35,520 | 1.1% |
| POP_TOP | 10,580 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,106,560 | 66.4% |
| JUMP_BACKWARD | 471,680 | 14.9% |
| FOR_ITER_GEN | 299,760 | 9.4% |
| FOR_ITER | 271,840 | 8.6% |
| FOR_ITER_LIST | 20,240 | 0.6% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 12,663,620 | 66.0% |
| GET_ITER | 2,744,440 | 14.3% |
| SWAP | 1,948,920 | 10.2% |
| LOAD_FAST | 1,537,540 | 8.0% |
| EXTENDED_ARG | 271,840 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 12,396,400 | 64.6% |
| RETURN_CONST | 2,986,020 | 15.6% |
| SWAP | 1,946,620 | 10.2% |
| LOAD_FAST | 1,241,400 | 6.5% |
| STORE_FAST | 291,060 | 1.5% |


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
| CALL_TYPE_1 | 746,540 | 52.2% |
| LOAD_FAST_LOAD_FAST | 341,280 | 23.9% |
| LOAD_ATTR_INSTANCE_VALUE | 291,340 | 20.4% |
| LOAD_DEREF | 51,200 | 3.6% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 746,560 | 52.2% |
| POP_JUMP_IF_FALSE | 670,880 | 46.9% |
| RETURN_VALUE | 12,960 | 0.9% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,012,540 | 26.8% |
| MAP_ADD | 4,025,760 | 17.9% |
| FOR_ITER_LIST | 3,934,800 | 17.5% |
| POP_JUMP_IF_TRUE | 3,123,200 | 13.9% |
| POP_JUMP_IF_FALSE | 1,542,080 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 12,663,620 | 56.4% |
| FOR_ITER_LIST | 5,529,100 | 24.6% |
| FOR_ITER_GEN | 1,947,940 | 8.7% |
| LOAD_FAST | 1,328,800 | 5.9% |
| EXTENDED_ARG | 556,320 | 2.5% |


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
| RETURN_VALUE | 485,380 | 32.7% |
| STORE_FAST | 336,640 | 22.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 234,220 | 15.8% |
| CALL_TUPLE_1 | 97,900 | 6.6% |
| LOAD_FAST | 87,680 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 456,960 | 30.8% |
| STORE_FAST | 344,000 | 23.2% |
| LOAD_FAST_LOAD_FAST | 168,480 | 11.4% |
| LOAD_FAST | 133,920 | 9.0% |
| LOAD_GLOBAL_BUILTIN | 107,800 | 7.3% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 199,180 | 84.9% |
| LOAD_FAST | 28,800 | 12.3% |
| BINARY_OP_ADD_INT | 5,740 | 2.4% |
| BINARY_SUBSCR_DICT | 780 | 0.3% |
| BINARY_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 234,560 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 582,140 | 77.5% |
| LOAD_FAST | 119,640 | 15.9% |
| LOAD_FAST_LOAD_FAST | 15,280 | 2.0% |
| LOAD_ATTR | 14,300 | 1.9% |
| LOAD_GLOBAL_BUILTIN | 6,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 255,720 | 34.0% |
| CALL_PY_EXACT_ARGS | 199,980 | 26.6% |
| LOAD_FAST | 115,000 | 15.3% |
| PUSH_NULL | 57,300 | 7.6% |
| CALL_METHOD_DESCRIPTOR_FAST | 26,480 | 3.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,142,140 | 23.7% |
| LOAD_FAST | 2,740,480 | 20.7% |
| LOAD_GLOBAL_BUILTIN | 1,537,380 | 11.6% |
| GET_YIELD_FROM_ITER | 1,030,080 | 7.8% |
| LOAD_ATTR_SLOT | 896,680 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 3,075,680 | 23.2% |
| MAKE_FUNCTION | 2,530,560 | 19.1% |
| CALL_PY_EXACT_ARGS | 1,624,840 | 12.2% |
| BINARY_SUBSCR_LIST_INT | 1,238,520 | 9.3% |
| SEND_GEN | 1,029,860 | 7.8% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,003,040 | 43.4% |
| RESUME_CHECK | 754,680 | 16.4% |
| POP_JUMP_IF_FALSE | 615,200 | 13.3% |
| LOAD_GLOBAL_BUILTIN | 501,820 | 10.9% |
| LOAD_GLOBAL_MODULE | 202,840 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,907,120 | 41.4% |
| PUSH_NULL | 508,800 | 11.0% |
| RETURN_VALUE | 495,520 | 10.7% |
| LOAD_GLOBAL_MODULE | 458,360 | 9.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 289,400 | 6.3% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 40,953,860 | 25.5% |
| POP_JUMP_IF_FALSE | 29,422,880 | 18.3% |
| RESUME_CHECK | 18,926,780 | 11.8% |
| LOAD_GLOBAL_MODULE | 14,924,020 | 9.3% |
| STORE_FAST | 11,170,920 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 25,244,280 | 15.7% |
| LOAD_ATTR_SLOT | 16,863,600 | 10.5% |
| CALL_PY_EXACT_ARGS | 15,603,660 | 9.7% |
| LOAD_GLOBAL_MODULE | 14,582,080 | 9.1% |
| RETURN_VALUE | 9,775,120 | 6.1% |


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
| LOAD_GLOBAL_BUILTIN | 3,027,760 | 22.4% |
| STORE_FAST | 2,543,680 | 18.8% |
| PUSH_NULL | 1,488,160 | 11.0% |
| LOAD_ATTR_METHOD_NO_DICT | 1,157,060 | 8.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,027,380 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,547,040 | 41.0% |
| STORE_ATTR_SLOT | 1,883,680 | 13.9% |
| CALL_ISINSTANCE | 1,561,080 | 11.5% |
| CALL_BUILTIN_FAST | 1,145,000 | 8.5% |
| CALL_PY_EXACT_ARGS | 915,620 | 6.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,840 | 16.4% |
| STORE_FAST | 4,500 | 15.2% |
| POP_JUMP_IF_FALSE | 3,960 | 13.4% |
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
| RETURN_VALUE | 3,850,560 | 95.6% |
| JUMP_FORWARD | 101,440 | 2.5% |
| LOAD_FAST | 73,760 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,025,760 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 35,059,160 | 74.7% |
| TO_BOOL_NONE | 2,474,780 | 5.3% |
| TO_BOOL | 2,410,660 | 5.1% |
| EXTENDED_ARG | 2,106,560 | 4.5% |
| TO_BOOL_ALWAYS_TRUE | 1,143,680 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 29,422,880 | 62.7% |
| LOAD_GLOBAL_MODULE | 5,472,320 | 11.7% |
| LOAD_GLOBAL_BUILTIN | 4,974,920 | 10.6% |
| RETURN_VALUE | 1,618,400 | 3.4% |
| POP_TOP | 1,586,400 | 3.4% |


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
| JUMP_BACKWARD | 960 | 0.4% |
| LOAD_FAST_LOAD_FAST | 160 | 0.1% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,290,240 | 99.4% |
| LOAD_ATTR_INSTANCE_VALUE | 24,100 | 0.6% |
| STORE_FAST_LOAD_FAST | 2,560 | 0.1% |
| LOAD_ATTR_SLOT | 1,100 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,881,000 | 89.9% |
| LOAD_FAST | 194,400 | 4.5% |
| BUILD_LIST | 161,760 | 3.7% |
| LOAD_GLOBAL_MODULE | 36,760 | 0.9% |
| BUILD_MAP | 33,280 | 0.8% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,663,880 | 62.4% |
| TO_BOOL_ALWAYS_TRUE | 2,783,680 | 26.1% |
| TO_BOOL_NONE | 630,820 | 5.9% |
| TO_BOOL_STR | 357,200 | 3.3% |
| CONTAINS_OP | 118,560 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,956,960 | 37.1% |
| JUMP_BACKWARD | 3,123,200 | 29.3% |
| LOAD_GLOBAL_BUILTIN | 1,212,480 | 11.4% |
| STORE_FAST | 1,052,800 | 9.9% |
| EXTENDED_ARG | 450,400 | 4.2% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 2,986,020 | 55.4% |
| POP_JUMP_IF_FALSE | 1,088,160 | 20.2% |
| STORE_ATTR_SLOT | 416,840 | 7.7% |
| END_FOR | 261,580 | 4.9% |
| POP_JUMP_IF_TRUE | 213,920 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 2,081,820 | 38.6% |
| POP_TOP | 1,343,200 | 24.9% |
| END_SEND | 1,030,080 | 19.1% |
| END_FOR | 279,980 | 5.2% |
| TO_BOOL_NONE | 249,320 | 4.6% |


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
| LOAD_FAST | 8,320 | 46.4% |
| RETURN_VALUE | 5,420 | 30.2% |
| LOAD_ATTR_PROPERTY | 4,160 | 23.2% |
| LOAD_ATTR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 17,920 | 100.0% |


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
| RETURN_VALUE | 8,571,680 | 23.4% |
| FOR_ITER_LIST | 5,502,500 | 15.0% |
| STORE_FAST | 3,927,040 | 10.7% |
| BUILD_LIST | 2,569,440 | 7.0% |
| SWAP | 2,086,880 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,170,920 | 30.5% |
| LOAD_GLOBAL_BUILTIN | 9,212,160 | 25.1% |
| LOAD_GLOBAL_MODULE | 4,018,780 | 11.0% |
| STORE_FAST | 3,927,040 | 10.7% |
| LOAD_FAST_LOAD_FAST | 2,543,680 | 6.9% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 255,340 | 80.3% |
| FOR_ITER_LIST | 44,880 | 14.1% |
| YIELD_VALUE | 15,160 | 4.8% |
| FOR_ITER_TUPLE | 2,540 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 250,200 | 78.7% |
| LOAD_ATTR_PROPERTY | 47,320 | 14.9% |
| YIELD_VALUE | 8,320 | 2.6% |
| LOAD_FAST | 5,920 | 1.9% |
| POP_JUMP_IF_NOT_NONE | 2,560 | 0.8% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 12,677,620 | 90.5% |
| UNPACK_SEQUENCE_TUPLE | 1,023,800 | 7.3% |
| UNPACK_EX | 291,360 | 2.1% |
| UNPACK_SEQUENCE | 15,540 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,024,320 | 50.1% |
| LOAD_GLOBAL_MODULE | 3,708,000 | 26.5% |
| LOAD_GLOBAL_BUILTIN | 1,867,560 | 13.3% |
| STORE_FAST | 1,023,840 | 7.3% |
| LOAD_FAST_LOAD_FAST | 384,000 | 2.7% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 2,113,760 | 31.1% |
| BUILD_MAP | 1,968,640 | 28.9% |
| FOR_ITER | 1,946,620 | 28.6% |
| BINARY_OP_ADD_INT | 468,560 | 6.9% |
| BUILD_LIST | 138,880 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,086,880 | 30.7% |
| BUILD_MAP | 1,968,640 | 28.9% |
| FOR_ITER | 1,948,920 | 28.6% |
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
| BUILD_TUPLE | 5,098,880 | 50.8% |
| YIELD_VALUE | 3,781,600 | 37.7% |
| JUMP_FORWARD | 456,960 | 4.6% |
| LOAD_FAST | 409,120 | 4.1% |
| RETURN_VALUE | 266,380 | 2.7% |

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
| LOAD_FAST | 481,120 | 87.2% |
| LOAD_CONST | 64,560 | 11.7% |
| LOAD_FAST_LOAD_FAST | 5,720 | 1.0% |
| BINARY_OP | 240 | 0.0% |
| RETURN_VALUE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 468,560 | 84.9% |
| STORE_FAST | 38,180 | 6.9% |
| CALL_PY_EXACT_ARGS | 26,040 | 4.7% |
| LOAD_FAST_LOAD_FAST | 8,300 | 1.5% |
| LIST_APPEND | 5,740 | 1.0% |


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
| LOAD_CONST | 441,040 | 73.8% |
| CALL_BUILTIN_O | 63,640 | 10.6% |
| BUILD_TUPLE | 36,800 | 6.2% |
| LOAD_FAST_LOAD_FAST | 23,080 | 3.9% |
| LOAD_FAST | 17,760 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 339,640 | 56.8% |
| RETURN_VALUE | 77,220 | 12.9% |
| PUSH_EXC_INFO | 70,060 | 11.7% |
| LOAD_ATTR_PROPERTY | 32,600 | 5.5% |
| STORE_FAST | 31,440 | 5.3% |


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
| LOAD_CONST | 46,040 | 50.0% |
| LOAD_FAST | 46,040 | 50.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 46,060 | 50.0% |
| LOAD_CONST | 46,060 | 50.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 85.7% |
| CALL | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 140 | 100.0% |


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
| RETURN_GENERATOR | 131,600 | 73.4% |
| BINARY_SLICE | 21,240 | 11.8% |
| LOAD_GLOBAL_BUILTIN | 9,680 | 5.4% |
| CALL_BUILTIN_FAST | 6,640 | 3.7% |
| LOAD_FAST | 4,360 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 86,540 | 48.3% |
| JUMP_FORWARD | 37,740 | 21.1% |
| GET_ITER | 24,920 | 13.9% |
| RETURN_VALUE | 8,720 | 4.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 7,640 | 4.3% |


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
| RETURN_VALUE | 4,760 | 66.5% |
| LOAD_DEREF | 2,360 | 33.0% |
| CALL | 40 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 4,760 | 66.5% |
| GET_ITER | 2,380 | 33.2% |
| LOAD_GLOBAL | 20 | 0.3% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 2,992,680 | 74.3% |
| LOAD_FAST | 872,280 | 21.6% |
| LOAD_ATTR_INSTANCE_VALUE | 160,480 | 4.0% |
| RETURN_VALUE | 3,320 | 0.1% |
| RETURN_GENERATOR | 1,400 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,153,220 | 78.2% |
| TO_BOOL_BOOL | 573,360 | 14.2% |
| STORE_FAST | 167,140 | 4.1% |
| STORE_SUBSCR_DICT | 65,800 | 1.6% |
| BINARY_SUBSCR_DICT | 63,640 | 1.6% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 14,480,040 | 39.1% |
| LOAD_GLOBAL_MODULE | 7,190,320 | 19.4% |
| LOAD_ATTR_MODULE | 7,131,120 | 19.3% |
| BUILD_TUPLE | 4,498,880 | 12.2% |
| LOAD_ATTR_SLOT | 2,150,240 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 34,276,880 | 92.6% |
| COPY | 1,405,620 | 3.8% |
| STORE_FAST | 1,277,380 | 3.5% |
| RETURN_VALUE | 53,420 | 0.1% |
| TO_BOOL | 2,280 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 145,280 | 84.5% |
| LOAD_DEREF | 18,840 | 11.0% |
| CALL_BUILTIN_CLASS | 4,760 | 2.8% |
| LOAD_ATTR_SLOT | 2,040 | 1.2% |
| CALL | 380 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 50,000 | 29.1% |
| LOAD_FAST | 48,920 | 28.5% |
| BINARY_OP_SUBTRACT_INT | 23,960 | 13.9% |
| COMPARE_OP_INT | 21,120 | 12.3% |
| LOAD_GLOBAL_BUILTIN | 19,080 | 11.1% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,576,560 | 97.8% |
| CALL | 24,340 | 1.5% |
| BUILD_TUPLE | 8,840 | 0.5% |
| RETURN_VALUE | 2,040 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 777,220 | 48.2% |
| LOAD_FAST_LOAD_FAST | 670,200 | 41.6% |
| LOAD_FAST | 126,020 | 7.8% |
| RETURN_CONST | 32,440 | 2.0% |
| EXTENDED_ARG | 5,900 | 0.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,075,680 | 57.0% |
| LOAD_FAST | 1,262,480 | 23.4% |
| LOAD_ATTR_SLOT | 714,760 | 13.3% |
| LOAD_ATTR_METHOD_NO_DICT | 152,720 | 2.8% |
| LOAD_FAST_LOAD_FAST | 136,720 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,665,080 | 49.4% |
| STORE_FAST | 1,716,100 | 31.8% |
| CALL_PY_WITH_DEFAULTS | 631,600 | 11.7% |
| TO_BOOL_BOOL | 234,200 | 4.3% |
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
| LOAD_ATTR_METHOD_NO_DICT | 9,236,680 | 99.9% |
| LOAD_FAST | 5,880 | 0.1% |
| CALL | 800 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 6,000,280 | 64.9% |
| BUILD_TUPLE | 1,249,900 | 13.5% |
| UNPACK_SEQUENCE_TUPLE | 992,760 | 10.7% |
| RETURN_VALUE | 526,960 | 5.7% |
| JUMP_FORWARD | 234,220 | 2.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 971,480 | 87.8% |
| RETURN_GENERATOR | 117,080 | 10.6% |
| LOAD_FAST | 16,320 | 1.5% |
| RETURN_VALUE | 920 | 0.1% |
| LOAD_ATTR_PROPERTY | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 989,000 | 89.4% |
| RETURN_VALUE | 117,100 | 10.6% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,603,660 | 66.5% |
| GET_ITER | 1,665,120 | 7.1% |
| LOAD_CONST | 1,624,840 | 6.9% |
| RETURN_VALUE | 1,194,200 | 5.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,078,800 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 18,605,060 | 79.3% |
| RETURN_GENERATOR | 2,671,440 | 11.4% |
| COPY_FREE_VARS | 1,101,600 | 4.7% |
| MAKE_CELL | 1,084,240 | 4.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,920 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 631,600 | 43.2% |
| LOAD_ATTR_METHOD_NO_DICT | 252,520 | 17.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 206,840 | 14.1% |
| LOAD_FAST_LOAD_FAST | 168,940 | 11.5% |
| LOAD_FAST | 145,040 | 9.9% |

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
| LOAD_ATTR_SLOT | 455,080 | 71.4% |
| LOAD_CONST | 108,360 | 17.0% |
| LOAD_FAST | 46,840 | 7.4% |
| CALL_LEN | 21,120 | 3.3% |
| LOAD_DEREF | 4,760 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 408,580 | 64.1% |
| LOAD_FAST | 218,060 | 34.2% |
| POP_JUMP_IF_TRUE | 10,340 | 1.6% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 298,120 | 68.1% |
| LOAD_CONST | 84,840 | 19.4% |
| LOAD_ATTR_SLOT | 32,080 | 7.3% |
| LOAD_FAST_LOAD_FAST | 10,960 | 2.5% |
| LOAD_FAST | 9,200 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 255,980 | 58.5% |
| POP_JUMP_IF_FALSE | 137,820 | 31.5% |
| COPY | 41,100 | 9.4% |
| POP_JUMP_IF_TRUE | 2,840 | 0.6% |


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
| JUMP_BACKWARD | 5,529,100 | 50.1% |
| GET_ITER | 5,348,320 | 48.5% |
| SWAP | 133,240 | 1.2% |
| EXTENDED_ARG | 20,240 | 0.2% |
| LOAD_FAST | 2,380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,502,500 | 49.9% |
| JUMP_BACKWARD | 3,934,800 | 35.7% |
| LOAD_FAST | 1,394,760 | 12.6% |
| SWAP | 118,980 | 1.1% |
| STORE_FAST_LOAD_FAST | 44,880 | 0.4% |


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
| JUMP_BACKWARD | 443,680 | 74.5% |
| LOAD_FAST | 118,040 | 19.8% |
| SWAP | 31,600 | 5.3% |
| GET_ITER | 2,040 | 0.3% |
| FOR_ITER | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 450,600 | 75.7% |
| RETURN_CONST | 118,080 | 19.8% |
| SWAP | 21,280 | 3.6% |
| STORE_FAST_LOAD_FAST | 2,540 | 0.4% |
| LOAD_FAST | 2,080 | 0.3% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 482,960 | 59.5% |
| LOAD_FAST_LOAD_FAST | 327,600 | 40.3% |
| LOAD_ATTR | 1,120 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 291,340 | 35.9% |
| CALL_BUILTIN_O | 160,480 | 19.8% |
| LOAD_ATTR_METHOD_NO_DICT | 84,240 | 10.4% |
| RETURN_VALUE | 78,100 | 9.6% |
| TO_BOOL_BOOL | 44,760 | 5.5% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 8,604,200 | 43.2% |
| LOAD_FAST | 7,013,720 | 35.2% |
| RETURN_VALUE | 2,790,060 | 14.0% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 742,400 | 3.7% |
| LOAD_GLOBAL_MODULE | 276,200 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 9,236,680 | 46.4% |
| LOAD_FAST | 5,513,160 | 27.7% |
| LOAD_CONST | 3,142,140 | 15.8% |
| LOAD_FAST_LOAD_FAST | 1,157,060 | 5.8% |
| LOAD_GLOBAL_MODULE | 308,960 | 1.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,996,960 | 90.3% |
| LOAD_DEREF | 289,400 | 8.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 22,900 | 0.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,960 | 0.1% |
| STORE_FAST_LOAD_FAST | 2,200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,078,800 | 32.5% |
| LOAD_FAST_LOAD_FAST | 1,027,380 | 30.9% |
| LOAD_CONST | 506,820 | 15.3% |
| LOAD_FAST | 423,380 | 12.8% |
| CALL_PY_WITH_DEFAULTS | 206,840 | 6.2% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 9,710,080 | 99.9% |
| LOAD_ATTR | 3,420 | 0.0% |
| LOAD_FAST | 1,880 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 7,131,120 | 73.4% |
| LOAD_GLOBAL_MODULE | 1,176,240 | 12.1% |
| PUSH_NULL | 680,420 | 7.0% |
| BUILD_TUPLE | 639,360 | 6.6% |
| JUMP_FORWARD | 28,080 | 0.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 882,440 | 87.4% |
| LOAD_FAST_LOAD_FAST | 126,160 | 12.5% |
| LOAD_ATTR | 820 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 742,400 | 73.5% |
| CONTAINS_OP | 150,020 | 14.9% |
| CALL_PY_EXACT_ARGS | 79,360 | 7.9% |
| STORE_FAST | 23,820 | 2.4% |
| LOAD_FAST | 11,140 | 1.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,598,120 | 98.4% |
| LOAD_FAST_LOAD_FAST | 30,520 | 0.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 28,660 | 0.8% |
| LOAD_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,584,880 | 43.3% |
| LOAD_GLOBAL_BUILTIN | 1,411,960 | 38.6% |
| FORMAT_SIMPLE | 571,980 | 15.6% |
| CONTAINS_OP | 40,600 | 1.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 28,660 | 0.8% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,337,640 | 96.8% |
| STORE_FAST_LOAD_FAST | 47,320 | 1.4% |
| BINARY_SUBSCR_DICT | 32,600 | 0.9% |
| LOAD_ATTR_SLOT | 10,320 | 0.3% |
| LOAD_ATTR_INSTANCE_VALUE | 9,960 | 0.3% |

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
| LOAD_FAST | 16,863,600 | 84.0% |
| LOAD_DEREF | 1,907,120 | 9.5% |
| COPY | 468,480 | 2.3% |
| LOAD_ATTR_SLOT | 427,380 | 2.1% |
| LOAD_FAST_LOAD_FAST | 403,960 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,604,200 | 42.8% |
| LOAD_FAST | 3,805,420 | 18.9% |
| CALL_ISINSTANCE | 2,150,240 | 10.7% |
| LOAD_CONST | 896,680 | 4.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 714,760 | 3.6% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,244,280 | 35.1% |
| RESUME_CHECK | 14,305,920 | 19.9% |
| STORE_FAST | 9,212,160 | 12.8% |
| LOAD_GLOBAL_BUILTIN | 7,527,700 | 10.5% |
| POP_JUMP_IF_FALSE | 4,974,920 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,953,860 | 56.9% |
| CALL_ISINSTANCE | 14,480,040 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 7,527,700 | 10.5% |
| BUILD_TUPLE | 3,757,100 | 5.2% |
| LOAD_FAST_LOAD_FAST | 3,027,760 | 4.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,582,080 | 42.0% |
| POP_JUMP_IF_FALSE | 5,472,320 | 15.8% |
| STORE_FAST | 4,018,780 | 11.6% |
| STORE_FAST_STORE_FAST | 3,708,000 | 10.7% |
| MAKE_FUNCTION | 1,411,960 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,924,020 | 43.0% |
| LOAD_ATTR_MODULE | 9,710,080 | 28.0% |
| CALL_ISINSTANCE | 7,190,320 | 20.7% |
| LOAD_FAST_LOAD_FAST | 1,008,740 | 2.9% |
| LOAD_ATTR | 582,140 | 1.7% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,605,060 | 41.3% |
| CACHE | 8,473,580 | 18.8% |
| SEND_GEN | 3,781,520 | 8.4% |
| LOAD_ATTR_PROPERTY | 3,398,340 | 7.5% |
| POP_TOP | 3,215,160 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,926,780 | 42.0% |
| LOAD_GLOBAL_BUILTIN | 14,305,920 | 31.8% |
| POP_TOP | 6,247,400 | 13.9% |
| JUMP_BACKWARD_NO_INTERRUPT | 3,781,500 | 8.4% |
| LOAD_DEREF | 754,680 | 1.7% |


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
| LOAD_FAST_LOAD_FAST | 1,883,680 | 44.9% |
| LOAD_FAST | 1,787,640 | 42.6% |
| SWAP | 468,480 | 11.2% |
| STORE_ATTR_SLOT | 36,700 | 0.9% |
| LOAD_DEREF | 17,080 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,321,280 | 31.5% |
| LOAD_FAST_LOAD_FAST | 872,440 | 20.8% |
| JUMP_BACKWARD | 842,960 | 20.1% |
| LOAD_GLOBAL_MODULE | 475,440 | 11.3% |
| RETURN_CONST | 416,840 | 9.9% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,397,640 | 89.7% |
| RETURN_VALUE | 74,920 | 4.8% |
| CALL_BUILTIN_O | 65,800 | 4.2% |
| LOAD_FAST_LOAD_FAST | 20,080 | 1.3% |
| STORE_SUBSCR | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,382,800 | 88.7% |
| LOAD_FAST | 78,640 | 5.0% |
| LOAD_GLOBAL_MODULE | 63,640 | 4.1% |
| POP_EXCEPT | 33,260 | 2.1% |
| EXTENDED_ARG | 460 | 0.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,935,500 | 48.4% |
| LOAD_FAST | 1,434,380 | 35.9% |
| LOAD_ATTR_SLOT | 305,180 | 7.6% |
| STORE_FAST_LOAD_FAST | 250,200 | 6.3% |
| TO_BOOL_ALWAYS_TRUE | 36,460 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 2,783,680 | 69.6% |
| POP_JUMP_IF_FALSE | 1,143,680 | 28.6% |
| TO_BOOL_ALWAYS_TRUE | 36,460 | 0.9% |
| UNARY_NOT | 28,900 | 0.7% |
| TO_BOOL_NONE | 5,840 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 34,276,880 | 76.6% |
| LOAD_FAST | 3,810,620 | 8.5% |
| COPY | 2,255,400 | 5.0% |
| RETURN_VALUE | 2,141,240 | 4.8% |
| LOAD_ATTR_SLOT | 651,120 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,059,160 | 78.4% |
| POP_JUMP_IF_TRUE | 6,663,880 | 14.9% |
| EXTENDED_ARG | 2,096,320 | 4.7% |
| UNARY_NOT | 925,500 | 2.1% |
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
| LOAD_FAST | 2,556,420 | 81.5% |
| COPY | 262,520 | 8.4% |
| RETURN_CONST | 249,320 | 8.0% |
| LOAD_ATTR_SLOT | 29,700 | 0.9% |
| RETURN_VALUE | 15,060 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,474,780 | 78.9% |
| POP_JUMP_IF_TRUE | 630,820 | 20.1% |
| EXTENDED_ARG | 10,020 | 0.3% |
| UNARY_NOT | 7,880 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 5,840 | 0.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,161,980 | 78.5% |
| LOAD_ATTR_SLOT | 141,560 | 9.6% |
| COPY | 127,360 | 8.6% |
| RETURN_VALUE | 42,080 | 2.8% |
| TO_BOOL_NONE | 5,660 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,118,100 | 75.5% |
| POP_JUMP_IF_TRUE | 357,200 | 24.1% |
| TO_BOOL_NONE | 5,660 | 0.4% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,917,000 | 65.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 992,760 | 34.1% |
| UNPACK_SEQUENCE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,886,040 | 64.8% |
| STORE_FAST_STORE_FAST | 1,023,800 | 35.2% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 12,396,400 | 97.3% |
| RETURN_VALUE | 130,200 | 1.0% |
| BUILD_TUPLE | 97,360 | 0.8% |
| STORE_FAST | 57,000 | 0.4% |
| LOAD_FAST | 37,720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 12,677,620 | 99.5% |
| STORE_FAST | 57,060 | 0.4% |
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
|     deferred | 19,520 | 2.2% |
|          hit | 867,940 | 97.7% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 39.3% |
| Failure | 740 | 60.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 700 | 94.6% |
| subtract other | 40 | 5.4% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> specialization stats for BINARY_OP_INPLACE_ADD_UNICODE family </summary>


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
|     deferred | 37,040 | 1.5% |
|          hit | 2,451,660 | 98.2% |
|         miss | 6,340 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 760 | 64.4% |
| Failure | 420 | 35.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 240 | 57.1% |
| out of range | 180 | 42.9% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,484,360 | 1.6% |
|          hit | 88,489,720 | 97.6% |
|         miss | 692,020 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 29,200 | 85.1% |
| Failure | 5,120 | 14.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 2,420 | 47.3% |
| class no vectorcall | 1,140 | 22.3% |
| meth descr varargs | 400 | 7.8% |
| meth descr varargs keywords | 300 | 5.9% |
| no dict | 180 | 3.5% |
| cfunc varargs keywords | 180 | 3.5% |
| meth descr method fastcall keywords | 140 | 2.7% |
| cfunc noargs | 100 | 2.0% |
| init not python | 100 | 2.0% |
| wrong number arguments | 80 | 1.6% |
| init not simple | 80 | 1.6% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,007,840 | 48.3% |
|          hit | 1,074,720 | 51.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 800 | 14.9% |
| Failure | 4,580 | 85.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 2,040 | 44.5% |
| different types | 1,500 | 32.8% |
| other | 420 | 9.2% |
| set | 220 | 4.8% |
| string | 200 | 4.4% |
| big int | 120 | 2.6% |
| bool | 80 | 1.7% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 19,164,700 | 57.5% |
|          hit | 14,150,740 | 42.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,660 | 14.3% |
| Failure | 9,960 | 85.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 6,360 | 63.9% |
| dict values | 880 | 8.8% |
| dict keys | 540 | 5.4% |
| enumerate | 540 | 5.4% |
| itertools | 520 | 5.2% |
| set | 460 | 4.6% |
| other | 260 | 2.6% |
| reversed list | 200 | 2.0% |
| ascii string | 200 | 2.0% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 966,000 | 1.5% |
|        deopt | 439,820 | 0.7% |
|          hit | 51,781,900 | 82.6% |
|         miss | 10,180,320 | 16.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 212,700 | 94.5% |
| Failure | 12,300 | 5.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 9,880 | 80.3% |
| method | 1,900 | 15.4% |
| mutable class | 380 | 3.1% |
| builtin class method | 140 | 1.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 14,700 | 0.0% |
|          hit | 106,632,940 | 100.0% |
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
|     deferred | 368,934,881,474,190,997,180 | 8,454,634,403,698,489.0% |
|          hit | 2,412,220 | 55.3% |
|         miss | 1,948,360 | 44.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 38,260 | 100.0% |
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
|     deferred | 2,362,320 | 4.2% |
|          hit | 50,372,780 | 89.9% |
|         miss | 3,205,540 | 5.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 68,040 | 96.5% |
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
| Basic | 429,677,360 | 46.8% |
| Not specialized | 87,282,560 | 9.5% |
| Specialized hits | 384,865,160 | 41.9% |
| Specialized misses | 16,037,520 | 1.7% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR | 368,934,881,474,190,997,180 | 100.0% |
| FOR_ITER | 19,164,700 | 0.0% |
| TO_BOOL | 2,362,320 | 0.0% |
| CALL | 1,484,360 | 0.0% |
| COMPARE_OP | 1,007,840 | 0.0% |
| LOAD_ATTR | 966,000 | 0.0% |
| BINARY_SUBSCR | 37,040 | 0.0% |
| BINARY_OP | 19,520 | 0.0% |
| UNPACK_SEQUENCE | 15,660 | 0.0% |
| LOAD_GLOBAL | 14,700 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 7,359,540 | 45.9% |
| TO_BOOL_ALWAYS_TRUE | 2,251,060 | 14.0% |
| STORE_ATTR_SLOT | 1,948,360 | 12.1% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,521,360 | 9.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,234,180 | 7.7% |
| TO_BOOL_NONE | 638,260 | 4.0% |
| CALL_PY_EXACT_ARGS | 392,820 | 2.4% |
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
| Calls to PyEval_EvalDefault | 10,429,540 | 21.6% |
| Calls to Python functions inlined | 37,823,780 | 78.4% |
| Calls via PyEval_EvalFrame (total) | 10,429,540 | 21.6% |
| Calls via PyEval_EvalFrame (vector) | 4,516,940 | 9.4% |
| Calls via PyEval_EvalFrame (generator) | 5,912,600 | 12.3% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 4,516,940 | 9.4% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,068,500 | 2.2% |
| Calls via PyEval_EvalFrame (function ex) | 84,000 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 3,204,220 | 6.6% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 76,480 | 0.2% |
| Frames pushed | 28,040,640 | 58.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 35,228,240 | 36.7% |
| Frees to freelist | 35,378,960 |  |
| Allocations | 60,777,160 | 63.3% |
| Allocations to 512 bytes | 60,701,640 | 63.2% |
| Allocations to 4 kbytes | 75,360 | 0.1% |
| Allocations over 4 kbytes | 160 | 0.0% |
| Frees | 61,820,725 |  |
| New values | 151,700 |  |
| Interpreter increfs | 368,632,020 | 66.1% |
| Interpreter decrefs | 427,171,660 | 66.2% |
| Increfs | 189,357,094 | 33.9% |
| Decrefs | 217,962,469 | 33.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 12,683,847 |  |
| Method cache misses | 655,033 |  |
| Method cache collisions | 688,928 |  |
| Method cache dunder hits | 63,360,766 |  |
| Method cache dunder misses | 40,014 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 640 | 116,980 | 2,412,280 |
| 1 | 60 | 95,660 | 1,607,240 |
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

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 20 |


</details>

---
Stats gathered on: 2024-09-10
