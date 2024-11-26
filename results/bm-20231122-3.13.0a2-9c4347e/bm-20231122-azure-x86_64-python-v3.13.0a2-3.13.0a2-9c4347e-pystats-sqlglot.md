
# Pystats results

- benchmark: sqlglot
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 162,591,760 | 15.9% | 15.9% |  |
| LOAD_GLOBAL_BUILTIN | 75,327,680 | 7.4% | 23.3% | 0.0% |
| RESUME_CHECK | 57,782,140 | 5.7% | 29.0% | 0.0% |
| POP_JUMP_IF_FALSE | 50,923,200 | 5.0% | 34.0% |  |
| TO_BOOL_BOOL | 49,228,580 | 4.8% | 38.8% | 0.0% |
| STORE_FAST | 40,293,620 | 3.9% | 42.8% |  |
| CALL_ISINSTANCE | 38,067,820 | 3.7% | 46.5% |  |
| RETURN_VALUE | 33,863,440 | 3.3% | 49.8% |  |
| POP_TOP | 29,064,600 | 2.8% | 52.7% |  |
| LOAD_GLOBAL_MODULE | 27,952,080 | 2.7% | 55.4% | 0.0% |
| CALL_PY_EXACT_ARGS | 26,557,520 | 2.6% | 58.0% | 1.2% |
| JUMP_BACKWARD | 22,161,680 | 2.2% | 60.2% |  |
| LOAD_ATTR_SLOT | 20,846,600 | 2.0% | 62.2% | 19.0% |
| FOR_ITER | 20,534,480 | 2.0% | 64.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 19,668,720 | 1.9% | 66.2% |  |
| LOAD_FAST_LOAD_FAST | 16,943,440 | 1.7% | 67.8% |  |
| YIELD_VALUE | 16,324,240 | 1.6% | 69.4% |  |
| BUILD_TUPLE | 15,379,280 | 1.5% | 70.9% |  |
| INTERPRETER_EXIT | 14,163,140 | 1.4% | 72.3% |  |
| GET_ITER | 13,564,160 | 1.3% | 73.6% |  |
| POP_JUMP_IF_TRUE | 13,558,960 | 1.3% | 75.0% |  |
| LOAD_CONST | 13,096,480 | 1.3% | 76.3% |  |
| STORE_FAST_STORE_FAST | 12,305,680 | 1.2% | 77.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 11,769,840 | 1.2% | 78.6% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,455,880 | 1.1% | 79.7% |  |
| SWAP | 10,682,400 | 1.0% | 80.8% |  |
| LOAD_FAST_AND_CLEAR | 10,599,840 | 1.0% | 81.8% |  |
| COPY | 10,496,800 | 1.0% | 82.9% |  |
| SEND_GEN | 10,085,160 | 1.0% | 83.8% |  |
| TO_BOOL_ALWAYS_TRUE | 9,147,000 | 0.9% | 84.7% | 34.5% |
| FOR_ITER_LIST | 9,074,580 | 0.9% | 85.6% |  |
| LOAD_DEREF | 8,640,560 | 0.8% | 86.5% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,165,360 | 0.8% | 87.3% | 29.6% |
| RETURN_CONST | 7,597,200 | 0.7% | 88.0% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 7,019,920 | 0.7% | 88.7% |  |
| RETURN_GENERATOR | 6,732,160 | 0.7% | 89.4% |  |
| BUILD_LIST | 4,945,920 | 0.5% | 89.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 4,747,620 | 0.5% | 90.3% |  |
| PUSH_NULL | 4,606,960 | 0.5% | 90.8% |  |
| FOR_ITER_GEN | 4,588,960 | 0.4% | 91.2% |  |
| UNPACK_SEQUENCE_TUPLE | 4,530,900 | 0.4% | 91.7% |  |
| MAP_ADD | 4,506,160 | 0.4% | 92.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 4,321,180 | 0.4% | 92.5% | 11.5% |
| CALL_BUILTIN_O | 4,321,180 | 0.4% | 93.0% |  |
| TO_BOOL | 4,156,500 | 0.4% | 93.4% |  |
| LOAD_ATTR_MODULE | 4,118,860 | 0.4% | 93.8% |  |
| POP_JUMP_IF_NOT_NONE | 3,996,400 | 0.4% | 94.2% |  |
| COPY_FREE_VARS | 3,753,680 | 0.4% | 94.5% |  |
| CALL | 3,679,800 | 0.4% | 94.9% |  |
| UNARY_NOT | 3,560,080 | 0.3% | 95.2% |  |
| BUILD_MAP | 3,522,240 | 0.3% | 95.6% |  |
| CALL_TYPE_1 | 3,307,800 | 0.3% | 95.9% |  |
| MAKE_FUNCTION | 3,221,600 | 0.3% | 96.2% |  |
| END_SEND | 3,065,280 | 0.3% | 96.5% |  |
| GET_YIELD_FROM_ITER | 3,065,280 | 0.3% | 96.8% |  |
| LOAD_ATTR_PROPERTY | 2,983,220 | 0.3% | 97.1% | 0.9% |
| TO_BOOL_NONE | 2,756,740 | 0.3% | 97.4% | 39.8% |
| JUMP_FORWARD | 2,447,760 | 0.2% | 97.6% |  |
| CALL_TUPLE_1 | 2,426,680 | 0.2% | 97.9% |  |
| FORMAT_SIMPLE | 1,721,440 | 0.2% | 98.0% |  |
| IS_OP | 1,686,720 | 0.2% | 98.2% |  |
| TO_BOOL_STR | 1,573,460 | 0.2% | 98.4% | 22.6% |
| CALL_PY_WITH_DEFAULTS | 1,568,300 | 0.2% | 98.5% |  |
| COMPARE_OP | 1,326,300 | 0.1% | 98.6% |  |
| CALL_BUILTIN_FAST | 1,147,960 | 0.1% | 98.7% |  |
| MAKE_CELL | 1,088,000 | 0.1% | 98.9% |  |
| EXTENDED_ARG | 1,026,000 | 0.1% | 99.0% |  |
| FOR_ITER_TUPLE | 1,021,620 | 0.1% | 99.1% |  |
| BUILD_STRING | 980,800 | 0.1% | 99.2% |  |
| STORE_FAST_LOAD_FAST | 901,600 | 0.1% | 99.2% |  |
| STORE_ATTR_SLOT | 731,020 | 0.1% | 99.3% | 58.9% |
| CALL_METHOD_DESCRIPTOR_O | 677,480 | 0.1% | 99.4% |  |
| CALL_KW | 648,320 | 0.1% | 99.4% |  |
| SET_FUNCTION_ATTRIBUTE | 642,480 | 0.1% | 99.5% |  |
| CONTAINS_OP | 635,680 | 0.1% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 595,880 | 0.1% | 99.6% |  |
| END_FOR | 542,600 | 0.1% | 99.7% |  |
| CALL_BUILTIN_CLASS | 494,520 | 0.0% | 99.7% |  |
| CALL_LIST_APPEND | 354,760 | 0.0% | 99.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 354,100 | 0.0% | 99.8% | 65.2% |
| COMPARE_OP_STR | 331,240 | 0.0% | 99.8% |  |
| BINARY_SUBSCR_LIST_INT | 302,720 | 0.0% | 99.9% | 0.1% |
| STORE_SUBSCR_DICT | 288,460 | 0.0% | 99.9% |  |
| LOAD_ATTR | 150,340 | 0.0% | 99.9% |  |
| BINARY_OP_ADD_INT | 139,840 | 0.0% | 99.9% |  |
| LIST_APPEND | 124,800 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 124,280 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE | 114,100 | 0.0% | 100.0% |  |
| CALL_LEN | 113,040 | 0.0% | 100.0% |  |
| COMPARE_OP_INT | 81,680 | 0.0% | 100.0% |  |
| BINARY_SLICE | 52,800 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 33,920 | 0.0% | 100.0% |  |
| STORE_DEREF | 31,680 | 0.0% | 100.0% |  |
| DICT_MERGE | 30,800 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 30,700 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 25,000 | 0.0% | 100.0% |  |
| BINARY_OP | 23,920 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 12,560 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 12,160 | 0.0% | 100.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 11,920 | 0.0% | 100.0% |  |
| NOP | 9,680 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 8,740 | 0.0% | 100.0% |  |
| TO_BOOL_LIST | 8,580 | 0.0% | 100.0% |  |
| TO_BOOL_INT | 3,000 | 0.0% | 100.0% |  |
| RESUME | 2,740 | 0.0% | 100.0% | 13.1% |
| BINARY_SUBSCR | 2,460 | 0.0% | 100.0% |  |
| POP_JUMP_IF_NONE | 2,400 | 0.0% | 100.0% |  |
| STORE_ATTR | 1,760 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 1,180 | 0.0% | 100.0% |  |
| CHECK_EXC_MATCH | 240 | 0.0% | 100.0% |  |
| POP_EXCEPT | 240 | 0.0% | 100.0% |  |
| PUSH_EXC_INFO | 240 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 140 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 80 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 80 | 0.0% | 100.0% |  |
| DICT_UPDATE | 80 | 0.0% | 100.0% |  |
| LIST_EXTEND | 80 | 0.0% | 100.0% |  |
| SEND | 80 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 40 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 44,423,580 | 4.4% | 4.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 38,512,620 | 3.8% | 8.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 36,071,560 | 3.5% | 11.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 30,210,320 | 3.0% | 14.6% |
| RESUME_CHECK LOAD_FAST | 26,776,460 | 2.6% | 17.3% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 23,818,520 | 2.3% | 19.6% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 20,386,480 | 2.0% | 21.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 16,197,900 | 1.6% | 23.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 13,570,460 | 1.3% | 24.5% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 13,438,080 | 1.3% | 25.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 13,434,800 | 1.3% | 27.1% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 13,364,280 | 1.3% | 28.4% |
| LOAD_FAST LOAD_ATTR_SLOT | 13,016,880 | 1.3% | 29.7% |
| JUMP_BACKWARD FOR_ITER | 12,034,100 | 1.2% | 30.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 11,782,080 | 1.2% | 32.1% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 11,707,700 | 1.1% | 33.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 11,455,520 | 1.1% | 34.3% |
| FOR_ITER UNPACK_SEQUENCE_TWO_TUPLE | 11,203,520 | 1.1% | 35.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 11,176,320 | 1.1% | 36.5% |
| CACHE RESUME_CHECK | 11,038,420 | 1.1% | 37.6% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 10,315,280 | 1.0% | 38.6% |
| RESUME_CHECK POP_TOP | 9,304,160 | 0.9% | 39.5% |
| LOAD_FAST RETURN_VALUE | 8,880,480 | 0.9% | 40.4% |
| POP_TOP JUMP_BACKWARD | 8,778,280 | 0.9% | 41.3% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 8,092,440 | 0.8% | 42.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS GET_ITER | 8,062,080 | 0.8% | 42.8% |
| LOAD_GLOBAL_BUILTIN LOAD_GLOBAL_BUILTIN | 8,011,380 | 0.8% | 43.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 7,584,360 | 0.7% | 44.4% |
| LOAD_ATTR_SLOT CALL_ISINSTANCE | 7,514,720 | 0.7% | 45.1% |
| LOAD_DEREF LOAD_ATTR_SLOT | 7,296,880 | 0.7% | 45.8% |
| LOAD_FAST LOAD_DEREF | 7,230,720 | 0.7% | 46.5% |
| LOAD_FAST BUILD_TUPLE | 7,157,920 | 0.7% | 47.2% |
| LOAD_FAST COPY | 7,133,440 | 0.7% | 47.9% |
| STORE_FAST STORE_FAST | 7,108,400 | 0.7% | 48.6% |
| YIELD_VALUE YIELD_VALUE | 7,019,920 | 0.7% | 49.3% |
| SEND_GEN RESUME_CHECK | 7,019,900 | 0.7% | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 7,019,880 | 0.7% | 50.7% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 7,019,880 | 0.7% | 51.4% |
| LOAD_FAST_AND_CLEAR LOAD_FAST_AND_CLEAR | 7,010,080 | 0.7% | 52.1% |
| STORE_FAST LOAD_FAST | 6,824,900 | 0.7% | 52.7% |
| POP_TOP RESUME_CHECK | 6,731,980 | 0.7% | 53.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 6,670,000 | 0.7% | 54.1% |
| COPY TO_BOOL_ALWAYS_TRUE | 6,664,520 | 0.7% | 54.7% |
| STORE_FAST_STORE_FAST LOAD_FAST | 6,401,120 | 0.6% | 55.3% |
| BUILD_TUPLE YIELD_VALUE | 6,021,760 | 0.6% | 55.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 5,953,360 | 0.6% | 56.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 5,767,160 | 0.6% | 57.1% |
| RETURN_VALUE INTERPRETER_EXIT | 5,758,180 | 0.6% | 57.6% |
| CALL_PY_EXACT_ARGS RETURN_GENERATOR | 5,621,600 | 0.6% | 58.2% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_TRUE | 5,522,820 | 0.5% | 58.7% |
| RETURN_VALUE STORE_FAST | 5,493,060 | 0.5% | 59.3% |
| YIELD_VALUE INTERPRETER_EXIT | 5,257,960 | 0.5% | 59.8% |
| RETURN_VALUE TO_BOOL_BOOL | 4,936,880 | 0.5% | 60.3% |
| POP_JUMP_IF_FALSE POP_TOP | 4,664,080 | 0.5% | 60.7% |
| POP_TOP LOAD_FAST | 4,637,080 | 0.5% | 61.2% |
| FOR_ITER_LIST STORE_FAST | 4,591,100 | 0.5% | 61.6% |
| MAP_ADD JUMP_BACKWARD | 4,506,160 | 0.4% | 62.1% |
| JUMP_BACKWARD FOR_ITER_LIST | 4,501,060 | 0.4% | 62.5% |
| GET_ITER FOR_ITER_LIST | 4,480,300 | 0.4% | 63.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 4,462,920 | 0.4% | 63.4% |
| RETURN_VALUE MAP_ADD | 4,408,320 | 0.4% | 63.8% |
| STORE_FAST_STORE_FAST LOAD_GLOBAL_MODULE | 4,401,160 | 0.4% | 64.3% |
| LOAD_FAST GET_ITER | 4,388,320 | 0.4% | 64.7% |
| LOAD_FAST LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 4,309,600 | 0.4% | 65.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 4,309,240 | 0.4% | 65.5% |
| LOAD_FAST BUILD_LIST | 4,285,440 | 0.4% | 65.9% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 4,174,080 | 0.4% | 66.4% |
| TO_BOOL POP_JUMP_IF_FALSE | 4,149,960 | 0.4% | 66.8% |
| LOAD_FAST TO_BOOL | 4,148,920 | 0.4% | 67.2% |
| BUILD_LIST RETURN_VALUE | 4,130,960 | 0.4% | 67.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 4,117,560 | 0.4% | 68.0% |
| FOR_ITER_LIST JUMP_BACKWARD | 4,085,840 | 0.4% | 68.4% |
| FOR_ITER RETURN_CONST | 4,084,760 | 0.4% | 68.8% |
| STORE_FAST POP_TOP | 4,049,360 | 0.4% | 69.2% |
| POP_TOP STORE_FAST | 4,046,400 | 0.4% | 69.6% |
| JUMP_BACKWARD FOR_ITER_GEN | 4,046,360 | 0.4% | 70.0% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST | 4,046,360 | 0.4% | 70.4% |
| FOR_ITER_GEN RESUME_CHECK | 4,046,340 | 0.4% | 70.8% |
| YIELD_VALUE UNPACK_SEQUENCE_TUPLE | 4,046,320 | 0.4% | 71.2% |
| BUILD_TUPLE CALL_ISINSTANCE | 4,025,360 | 0.4% | 71.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 3,996,320 | 0.4% | 71.9% |
| LOAD_GLOBAL_BUILTIN BUILD_TUPLE | 3,994,460 | 0.4% | 72.3% |
| POP_JUMP_IF_NOT_NONE LOAD_GLOBAL_BUILTIN | 3,994,440 | 0.4% | 72.7% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 3,832,960 | 0.4% | 73.1% |
| LOAD_FAST PUSH_NULL | 3,777,920 | 0.4% | 73.5% |
| COPY_FREE_VARS RESUME_CHECK | 3,750,560 | 0.4% | 73.8% |
| CALL_BUILTIN_O RETURN_VALUE | 3,745,960 | 0.4% | 74.2% |
| BUILD_TUPLE CALL_BUILTIN_O | 3,734,000 | 0.4% | 74.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 3,717,080 | 0.4% | 74.9% |
| LOAD_ATTR_MODULE CALL_ISINSTANCE | 3,691,480 | 0.4% | 75.3% |
| POP_TOP LOAD_GLOBAL_BUILTIN | 3,645,480 | 0.4% | 75.7% |
| GET_ITER LOAD_FAST_AND_CLEAR | 3,589,760 | 0.4% | 76.0% |
| LOAD_FAST_AND_CLEAR SWAP | 3,589,760 | 0.4% | 76.4% |
| LOAD_FAST CALL | 3,564,680 | 0.3% | 76.7% |
| TO_BOOL_ALWAYS_TRUE POP_JUMP_IF_FALSE | 3,564,600 | 0.3% | 77.1% |
| CALL COPY_FREE_VARS | 3,561,920 | 0.3% | 77.4% |
| PUSH_NULL LOAD_FAST_LOAD_FAST | 3,561,840 | 0.3% | 77.8% |
| UNARY_NOT RETURN_VALUE | 3,560,080 | 0.3% | 78.1% |
| TO_BOOL_BOOL UNARY_NOT | 3,560,060 | 0.3% | 78.5% |
| BUILD_MAP SWAP | 3,491,440 | 0.3% | 78.8% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 47,920 | 90.8% |
| LOAD_ATTR_SLOT | 4,860 | 9.2% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 31,400 | 59.5% |
| GET_ITER | 8,240 | 15.6% |
| TO_BOOL_LIST | 8,200 | 15.5% |
| RETURN_VALUE | 4,880 | 9.2% |
| TO_BOOL | 40 | 0.1% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,038,420 | 77.9% |
| POP_TOP | 3,124,320 | 22.1% |
| RESUME | 400 | 0.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,160 | 98.3% |
| BINARY_OP | 20 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,180 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,000 | 81.3% |
| LOAD_FAST | 120 | 4.9% |
| BINARY_SUBSCR | 100 | 4.1% |
| LOAD_FAST_LOAD_FAST | 80 | 3.3% |
| LOAD_ATTR | 60 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,800 | 73.2% |
| BINARY_SUBSCR | 100 | 4.1% |
| STORE_FAST | 80 | 3.3% |
| BINARY_SUBSCR_DICT | 80 | 3.3% |
| BINARY_SUBSCR_LIST_INT | 80 | 3.3% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 220 | 91.7% |
| LOAD_GLOBAL | 20 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 240 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 542,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 542,460 | 100.0% |
| LOAD_FAST | 140 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 3,065,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 3,065,280 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 573,980 | 33.3% |
| LOAD_ATTR_SLOT | 431,640 | 25.1% |
| LOAD_FAST | 406,800 | 23.6% |
| RETURN_VALUE | 308,960 | 17.9% |
| LOAD_ATTR | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 810,000 | 47.1% |
| LOAD_FAST | 504,640 | 29.3% |
| BUILD_STRING | 406,800 | 23.6% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 8,062,080 | 59.4% |
| LOAD_FAST | 4,388,320 | 32.4% |
| RETURN_GENERATOR | 542,640 | 4.0% |
| BUILD_TUPLE | 215,840 | 1.6% |
| RETURN_VALUE | 181,440 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 4,480,300 | 33.0% |
| LOAD_FAST_AND_CLEAR | 3,589,760 | 26.5% |
| CALL_PY_EXACT_ARGS | 2,582,080 | 19.0% |
| FOR_ITER | 2,353,600 | 17.4% |
| FOR_ITER_GEN | 542,520 | 4.0% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 3,065,280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,065,280 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,758,180 | 40.7% |
| YIELD_VALUE | 5,257,960 | 37.1% |
| RETURN_CONST | 3,147,000 | 22.2% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,221,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,912,600 | 59.4% |
| LOAD_FAST | 666,640 | 20.7% |
| SET_FUNCTION_ATTRIBUTE | 642,320 | 19.9% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,380 | 76.2% |
| POP_JUMP_IF_FALSE | 1,200 | 12.4% |
| STORE_FAST | 960 | 9.9% |
| POP_TOP | 80 | 0.8% |
| RESUME | 60 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 6,000 | 62.0% |
| LOAD_FAST | 3,360 | 34.7% |
| LOAD_GLOBAL_BUILTIN | 200 | 2.1% |
| LOAD_DEREF | 80 | 0.8% |
| LOAD_GLOBAL | 40 | 0.4% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 240 | 100.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 9,304,160 | 32.0% |
| POP_JUMP_IF_FALSE | 4,664,080 | 16.0% |
| STORE_FAST | 4,049,360 | 13.9% |
| CACHE | 3,124,320 | 10.7% |
| END_SEND | 3,065,280 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,778,280 | 30.2% |
| RESUME_CHECK | 6,731,980 | 23.2% |
| LOAD_FAST | 4,637,080 | 16.0% |
| STORE_FAST | 4,046,400 | 13.9% |
| LOAD_GLOBAL_BUILTIN | 3,645,480 | 12.5% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_LIST_INT | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 200 | 83.3% |
| LOAD_GLOBAL | 40 | 16.7% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,777,920 | 82.0% |
| CALL_BUILTIN_FAST | 573,980 | 12.5% |
| LOAD_ATTR_MODULE | 195,900 | 4.3% |
| LOAD_DEREF | 57,920 | 1.3% |
| LOAD_FAST_LOAD_FAST | 560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 3,561,840 | 77.3% |
| LOAD_FAST | 1,035,200 | 22.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 3,560 | 0.1% |
| LOAD_DEREF | 2,240 | 0.0% |
| LOAD_CONST | 1,680 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 5,621,600 | 83.5% |
| CALL_KW | 542,320 | 8.1% |
| MAKE_CELL | 519,440 | 7.7% |
| CALL | 22,980 | 0.3% |
| CALL_PY_WITH_DEFAULTS | 22,860 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_YIELD_FROM_ITER | 3,065,280 | 45.5% |
| CALL_TUPLE_1 | 2,395,160 | 35.6% |
| GET_ITER | 542,640 | 8.1% |
| CALL_BUILTIN_CLASS | 462,920 | 6.9% |
| CALL_METHOD_DESCRIPTOR_O | 215,800 | 3.2% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,880,480 | 26.2% |
| BUILD_LIST | 4,130,960 | 12.2% |
| CALL_BUILTIN_O | 3,745,960 | 11.1% |
| UNARY_NOT | 3,560,080 | 10.5% |
| STORE_FAST | 3,460,000 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 5,758,180 | 17.0% |
| STORE_FAST | 5,493,060 | 16.2% |
| TO_BOOL_BOOL | 4,936,880 | 14.6% |
| MAP_ADD | 4,408,320 | 13.0% |
| LOAD_ATTR_METHOD_NO_DICT | 3,832,960 | 11.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 20 | 50.0% |
| STORE_SUBSCR_DICT | 20 | 50.0% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,148,920 | 99.8% |
| TO_BOOL | 1,900 | 0.0% |
| RETURN_CONST | 1,280 | 0.0% |
| CALL | 1,180 | 0.0% |
| CALL_ISINSTANCE | 1,100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,149,960 | 99.8% |
| TO_BOOL_BOOL | 2,040 | 0.0% |
| TO_BOOL | 1,900 | 0.0% |
| POP_JUMP_IF_TRUE | 940 | 0.0% |
| TO_BOOL_NONE | 940 | 0.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,560,060 | 100.0% |
| TO_BOOL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,560,080 | 100.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 23,040 | 96.3% |
| BINARY_OP | 240 | 1.0% |
| LOAD_CONST | 240 | 1.0% |
| LOAD_FAST | 200 | 0.8% |
| LOAD_FAST_LOAD_FAST | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 23,060 | 96.4% |
| BINARY_OP | 240 | 1.0% |
| BINARY_OP_ADD_INT | 160 | 0.7% |
| STORE_FAST | 140 | 0.6% |
| BINARY_OP_SUBTRACT_INT | 100 | 0.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,285,440 | 86.6% |
| STORE_FAST | 288,480 | 5.8% |
| LOAD_CONST | 136,480 | 2.8% |
| SWAP | 98,320 | 2.0% |
| RESUME_CHECK | 97,820 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,130,960 | 83.5% |
| STORE_FAST | 592,720 | 12.0% |
| LOAD_FAST | 98,400 | 2.0% |
| SWAP | 98,320 | 2.0% |
| CALL | 22,880 | 0.5% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,491,440 | 99.1% |
| LOAD_FAST | 20,800 | 0.6% |
| BUILD_TUPLE | 8,320 | 0.2% |
| LOAD_CONST | 1,680 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 3,491,440 | 99.1% |
| LOAD_FAST | 30,800 | 0.9% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 574,000 | 58.5% |
| FORMAT_SIMPLE | 406,800 | 41.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 574,000 | 58.5% |
| RETURN_VALUE | 406,800 | 41.5% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,157,920 | 46.5% |
| LOAD_GLOBAL_BUILTIN | 3,994,460 | 26.0% |
| CALL_TUPLE_1 | 1,912,620 | 12.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,821,420 | 11.8% |
| RETURN_VALUE | 215,840 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,021,760 | 39.2% |
| CALL_ISINSTANCE | 4,025,360 | 26.2% |
| CALL_BUILTIN_O | 3,734,000 | 24.3% |
| LOAD_CONST | 663,120 | 4.3% |
| CALL_METHOD_DESCRIPTOR_O | 461,640 | 3.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,564,680 | 96.9% |
| LOAD_CONST | 33,840 | 0.9% |
| LOAD_ATTR_MODULE | 23,400 | 0.6% |
| BUILD_LIST | 22,880 | 0.6% |
| RETURN_GENERATOR | 16,040 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY_FREE_VARS | 3,561,920 | 96.8% |
| STORE_FAST | 38,980 | 1.1% |
| GET_ITER | 31,600 | 0.9% |
| RETURN_GENERATOR | 22,980 | 0.6% |
| RESUME_CHECK | 7,120 | 0.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 30,800 | 90.8% |
| RETURN_GENERATOR | 2,960 | 8.7% |
| CALL_INTRINSIC_1 | 80 | 0.2% |
| LOAD_FAST | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 32,020 | 94.4% |
| STORE_FAST | 1,600 | 4.7% |
| RETURN_VALUE | 80 | 0.2% |
| COPY_FREE_VARS | 80 | 0.2% |
| RESUME | 60 | 0.2% |


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
| LOAD_CONST | 648,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 542,320 | 83.7% |
| RESUME_CHECK | 70,960 | 10.9% |
| STORE_FAST | 17,680 | 2.7% |
| MAKE_CELL | 15,680 | 2.4% |
| RETURN_VALUE | 1,600 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 773,720 | 58.3% |
| CALL_BUILTIN_CLASS | 220,460 | 16.6% |
| LOAD_GLOBAL_MODULE | 105,700 | 8.0% |
| LOAD_ATTR | 103,720 | 7.8% |
| BINARY_SUBSCR_TUPLE_INT | 62,140 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 773,700 | 58.3% |
| POP_JUMP_IF_FALSE | 449,280 | 33.9% |
| POP_JUMP_IF_TRUE | 64,240 | 4.8% |
| COPY | 35,280 | 2.7% |
| COMPARE_OP | 3,500 | 0.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 444,000 | 69.8% |
| BUILD_TUPLE | 172,800 | 27.2% |
| LOAD_FAST | 10,080 | 1.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 6,620 | 1.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,060 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 411,920 | 64.8% |
| POP_JUMP_IF_TRUE | 222,560 | 35.0% |
| STORE_FAST | 1,200 | 0.2% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,133,440 | 68.0% |
| CALL_ISINSTANCE | 1,671,440 | 15.9% |
| IS_OP | 1,653,920 | 15.8% |
| COMPARE_OP | 35,280 | 0.3% |
| RETURN_CONST | 2,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 6,664,520 | 63.5% |
| TO_BOOL_BOOL | 3,361,160 | 32.0% |
| TO_BOOL_NONE | 460,640 | 4.4% |
| LOAD_ATTR_SLOT | 9,480 | 0.1% |
| TO_BOOL | 560 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,561,920 | 94.9% |
| CALL_PY_EXACT_ARGS | 191,680 | 5.1% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,750,560 | 99.9% |
| RETURN_GENERATOR | 2,960 | 0.1% |
| RESUME | 160 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,720 | 99.7% |
| DICT_UPDATE | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 30,800 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 80 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 485,880 | 47.4% |
| JUMP_BACKWARD | 299,840 | 29.2% |
| POP_JUMP_IF_TRUE | 223,360 | 21.8% |
| GET_ITER | 15,680 | 1.5% |
| TO_BOOL_NONE | 1,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 487,040 | 47.5% |
| FOR_ITER | 315,520 | 30.8% |
| JUMP_BACKWARD | 223,360 | 21.8% |
| POP_JUMP_IF_TRUE | 80 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 12,034,100 | 58.6% |
| SWAP | 3,460,060 | 16.9% |
| LOAD_FAST | 2,363,480 | 11.5% |
| GET_ITER | 2,353,600 | 11.5% |
| EXTENDED_ARG | 315,520 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 11,203,520 | 54.6% |
| RETURN_CONST | 4,084,760 | 19.9% |
| SWAP | 3,460,000 | 16.8% |
| STORE_FAST_LOAD_FAST | 901,600 | 4.4% |
| LOAD_FAST | 613,080 | 3.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_TYPE_1 | 1,653,900 | 98.1% |
| LOAD_DEREF | 32,800 | 1.9% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,653,920 | 98.1% |
| POP_JUMP_IF_FALSE | 32,800 | 1.9% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,778,280 | 39.6% |
| MAP_ADD | 4,506,160 | 20.3% |
| FOR_ITER_LIST | 4,085,840 | 18.4% |
| POP_JUMP_IF_FALSE | 2,463,280 | 11.1% |
| POP_JUMP_IF_TRUE | 1,353,200 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 12,034,100 | 54.3% |
| FOR_ITER_LIST | 4,501,060 | 20.3% |
| FOR_ITER_GEN | 4,046,360 | 18.3% |
| FOR_ITER_TUPLE | 766,100 | 3.5% |
| LOAD_FAST | 513,760 | 2.3% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,019,880 | 100.0% |
| RESUME | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 7,019,880 | 100.0% |
| SEND | 40 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,979,820 | 80.9% |
| CALL_BUILTIN_CLASS | 220,460 | 9.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 215,820 | 8.8% |
| LOAD_ATTR_MODULE | 21,540 | 0.9% |
| LOAD_GLOBAL_MODULE | 3,900 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,978,000 | 80.8% |
| STORE_FAST | 243,520 | 9.9% |
| LOAD_GLOBAL_BUILTIN | 220,440 | 9.0% |
| LOAD_FAST | 4,880 | 0.2% |
| JUMP_BACKWARD | 880 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,980 | 83.3% |
| RETURN_VALUE | 20,800 | 16.7% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 124,800 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 127,380 | 84.7% |
| LOAD_FAST | 14,600 | 9.7% |
| LOAD_ATTR | 3,960 | 2.6% |
| LOAD_GLOBAL | 2,060 | 1.4% |
| LOAD_DEREF | 1,000 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 103,720 | 69.0% |
| CALL_PY_EXACT_ARGS | 17,320 | 11.5% |
| LOAD_FAST | 6,000 | 4.0% |
| LOAD_ATTR | 3,960 | 2.6% |
| CALL | 3,560 | 2.4% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,183,420 | 24.3% |
| GET_YIELD_FROM_ITER | 3,065,280 | 23.4% |
| LOAD_GLOBAL_BUILTIN | 2,363,400 | 18.0% |
| LOAD_FAST | 1,479,520 | 11.3% |
| FORMAT_SIMPLE | 810,000 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 3,221,600 | 24.6% |
| SEND_GEN | 3,065,240 | 23.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,943,240 | 22.5% |
| CALL_PY_EXACT_ARGS | 1,294,040 | 9.9% |
| CALL_KW | 648,320 | 5.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,230,720 | 83.7% |
| RESUME_CHECK | 732,140 | 8.5% |
| LOAD_GLOBAL_MODULE | 180,600 | 2.1% |
| POP_JUMP_IF_TRUE | 134,480 | 1.6% |
| POP_JUMP_IF_FALSE | 125,600 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 7,296,880 | 84.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 535,040 | 6.2% |
| LOAD_FAST_LOAD_FAST | 164,960 | 1.9% |
| LOAD_ATTR_METHOD_NO_DICT | 156,840 | 1.8% |
| RETURN_VALUE | 85,680 | 1.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 44,423,580 | 27.3% |
| POP_JUMP_IF_FALSE | 30,210,320 | 18.6% |
| RESUME_CHECK | 26,776,460 | 16.5% |
| LOAD_GLOBAL_MODULE | 13,570,460 | 8.3% |
| LOAD_FAST_LOAD_FAST | 11,176,320 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 23,818,520 | 14.6% |
| CALL_PY_EXACT_ARGS | 16,197,900 | 10.0% |
| LOAD_ATTR_SLOT | 13,016,880 | 8.0% |
| LOAD_GLOBAL_MODULE | 11,782,080 | 7.2% |
| RETURN_VALUE | 8,880,480 | 5.5% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 7,010,080 | 66.1% |
| GET_ITER | 3,589,760 | 33.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 7,010,080 | 66.1% |
| SWAP | 3,589,760 | 33.9% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,174,080 | 24.6% |
| PUSH_NULL | 3,561,840 | 21.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,042,380 | 18.0% |
| LOAD_GLOBAL_BUILTIN | 2,958,680 | 17.5% |
| LOAD_GLOBAL_MODULE | 1,462,780 | 8.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,176,320 | 66.0% |
| CALL_PY_EXACT_ARGS | 1,544,920 | 9.1% |
| CALL_ISINSTANCE | 1,304,520 | 7.7% |
| CALL_BUILTIN_FAST | 1,147,920 | 6.8% |
| STORE_ATTR_SLOT | 480,360 | 2.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,440 | 20.1% |
| POP_JUMP_IF_FALSE | 2,240 | 18.4% |
| STORE_FAST | 1,680 | 13.8% |
| LOAD_ATTR | 1,020 | 8.4% |
| RESUME | 700 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,940 | 32.4% |
| LOAD_FAST | 2,440 | 20.1% |
| LOAD_GLOBAL_BUILTIN | 2,140 | 17.6% |
| LOAD_ATTR | 2,060 | 16.9% |
| LOAD_FAST_LOAD_FAST | 700 | 5.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 528,020 | 48.5% |
| CALL_PY_EXACT_ARGS | 351,720 | 32.3% |
| MAKE_CELL | 191,520 | 17.6% |
| CALL_KW | 15,680 | 1.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 519,440 | 47.7% |
| RESUME_CHECK | 376,820 | 34.6% |
| MAKE_CELL | 191,520 | 17.6% |
| RESUME | 220 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 4,408,320 | 97.8% |
| LOAD_FAST | 97,840 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,506,160 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 38,512,620 | 75.6% |
| TO_BOOL | 4,149,960 | 8.1% |
| TO_BOOL_ALWAYS_TRUE | 3,564,600 | 7.0% |
| TO_BOOL_NONE | 1,663,100 | 3.3% |
| TO_BOOL_STR | 1,560,740 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,210,320 | 59.3% |
| LOAD_GLOBAL_MODULE | 5,767,160 | 11.3% |
| POP_TOP | 4,664,080 | 9.2% |
| LOAD_GLOBAL_BUILTIN | 2,925,720 | 5.7% |
| JUMP_BACKWARD | 2,463,280 | 4.8% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,400 | 100.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,996,320 | 100.0% |
| LOAD_ATTR_SLOT | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 3,994,440 | 100.0% |
| LOAD_FAST | 1,920 | 0.0% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 6,670,000 | 49.2% |
| TO_BOOL_ALWAYS_TRUE | 5,522,820 | 40.7% |
| TO_BOOL_NONE | 1,072,000 | 7.9% |
| CONTAINS_OP | 222,560 | 1.6% |
| COMPARE_OP | 64,240 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,953,360 | 43.9% |
| STORE_FAST | 3,042,720 | 22.4% |
| LOAD_GLOBAL_BUILTIN | 1,491,960 | 11.0% |
| JUMP_BACKWARD | 1,353,200 | 10.0% |
| POP_TOP | 556,080 | 4.1% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 4,084,760 | 53.8% |
| POP_JUMP_IF_FALSE | 2,259,440 | 29.7% |
| END_FOR | 542,460 | 7.1% |
| POP_JUMP_IF_TRUE | 434,960 | 5.7% |
| FOR_ITER_TUPLE | 215,840 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 3,147,000 | 41.4% |
| END_SEND | 3,065,280 | 40.3% |
| END_FOR | 542,600 | 7.1% |
| RETURN_VALUE | 432,640 | 5.7% |
| POP_TOP | 213,040 | 2.8% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 40 | 50.0% |
| LOAD_CONST | 40 | 50.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 40 | 50.0% |
| SEND_GEN | 40 | 50.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 642,320 | 100.0% |
| SET_FUNCTION_ATTRIBUTE | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 519,440 | 80.8% |
| CALL_PY_EXACT_ARGS | 119,560 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 2,920 | 0.5% |
| CALL | 200 | 0.0% |
| SET_FUNCTION_ATTRIBUTE | 160 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,080 | 61.4% |
| LOAD_FAST_LOAD_FAST | 520 | 29.5% |
| SWAP | 120 | 6.8% |
| LOAD_DEREF | 40 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 880 | 50.0% |
| LOAD_FAST | 280 | 15.9% |
| LOAD_FAST_LOAD_FAST | 180 | 10.2% |
| RETURN_CONST | 120 | 6.8% |
| LOAD_CONST | 100 | 5.7% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 31,440 | 99.2% |
| SET_FUNCTION_ATTRIBUTE | 160 | 0.5% |
| RETURN_CONST | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 31,400 | 99.1% |
| LOAD_GLOBAL_MODULE | 120 | 0.4% |
| LOAD_DEREF | 80 | 0.3% |
| LOAD_GLOBAL | 80 | 0.3% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,108,400 | 17.6% |
| RETURN_VALUE | 5,493,060 | 13.6% |
| FOR_ITER_LIST | 4,591,100 | 11.4% |
| POP_TOP | 4,046,400 | 10.0% |
| UNPACK_SEQUENCE_TUPLE | 4,046,360 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 13,364,280 | 33.2% |
| STORE_FAST | 7,108,400 | 17.6% |
| LOAD_FAST | 6,824,900 | 16.9% |
| LOAD_FAST_LOAD_FAST | 4,174,080 | 10.4% |
| POP_TOP | 4,049,360 | 10.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 901,600 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_ALWAYS_TRUE | 901,560 | 100.0% |
| TO_BOOL | 40 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 11,707,700 | 95.1% |
| UNPACK_SEQUENCE_TUPLE | 484,540 | 3.9% |
| UNPACK_SEQUENCE | 113,440 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,401,120 | 52.0% |
| LOAD_GLOBAL_MODULE | 4,401,160 | 35.8% |
| LOAD_GLOBAL_BUILTIN | 735,880 | 6.0% |
| STORE_FAST | 484,560 | 3.9% |
| LOAD_FAST_LOAD_FAST | 282,640 | 2.3% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_AND_CLEAR | 3,589,760 | 33.6% |
| BUILD_MAP | 3,491,440 | 32.7% |
| FOR_ITER | 3,460,000 | 32.4% |
| BUILD_LIST | 98,320 | 0.9% |
| FOR_ITER_TUPLE | 31,440 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 3,491,440 | 32.7% |
| STORE_FAST | 3,491,440 | 32.7% |
| FOR_ITER | 3,460,060 | 32.4% |
| BUILD_LIST | 98,320 | 0.9% |
| FOR_ITER_LIST | 90,060 | 0.8% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 113,120 | 99.1% |
| FOR_ITER | 440 | 0.4% |
| UNPACK_SEQUENCE | 220 | 0.2% |
| RETURN_VALUE | 120 | 0.1% |
| BUILD_TUPLE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 113,440 | 99.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 320 | 0.3% |
| UNPACK_SEQUENCE | 220 | 0.2% |
| STORE_FAST | 60 | 0.1% |
| UNPACK_SEQUENCE_TUPLE | 60 | 0.1% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 7,019,920 | 43.0% |
| BUILD_TUPLE | 6,021,760 | 36.9% |
| JUMP_FORWARD | 1,978,000 | 12.1% |
| RETURN_VALUE | 901,600 | 5.5% |
| LOAD_FAST | 392,720 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 7,019,920 | 43.0% |
| INTERPRETER_EXIT | 5,257,960 | 32.2% |
| UNPACK_SEQUENCE_TUPLE | 4,046,320 | 24.8% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,420 | 51.8% |
| CACHE | 400 | 14.6% |
| MAKE_CELL | 220 | 8.0% |
| POP_TOP | 180 | 6.6% |
| COPY_FREE_VARS | 160 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,460 | 53.3% |
| LOAD_GLOBAL | 700 | 25.5% |
| LOAD_DEREF | 180 | 6.6% |
| POP_TOP | 160 | 5.8% |
| LOAD_CONST | 100 | 3.6% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 103,960 | 74.3% |
| LOAD_CONST | 25,080 | 17.9% |
| LOAD_FAST | 10,640 | 7.6% |
| BINARY_OP | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 103,980 | 74.4% |
| BINARY_OP_SUBTRACT_INT | 22,040 | 15.8% |
| SWAP | 9,540 | 6.8% |
| STORE_FAST | 2,360 | 1.7% |
| CALL_PY_EXACT_ARGS | 1,880 | 1.3% |


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
| BINARY_OP | 60 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 22,040 | 71.8% |
| LOAD_CONST | 6,760 | 22.0% |
| CALL_LEN | 1,800 | 5.9% |
| BINARY_OP | 100 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 22,060 | 71.9% |
| BINARY_SUBSCR_STR_INT | 3,800 | 12.4% |
| LOAD_CONST | 1,820 | 5.9% |
| CALL_PY_EXACT_ARGS | 1,800 | 5.9% |
| LOAD_FAST | 1,180 | 3.8% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,200 | 81.2% |
| LOAD_FAST_LOAD_FAST | 1,160 | 9.2% |
| LOAD_ATTR_SLOT | 1,120 | 8.9% |
| BINARY_SUBSCR | 80 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 10,220 | 81.4% |
| STORE_FAST | 1,800 | 14.3% |
| LOAD_FAST_LOAD_FAST | 540 | 4.3% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 296,680 | 98.0% |
| LOAD_FAST_LOAD_FAST | 5,960 | 2.0% |
| BINARY_SUBSCR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 288,460 | 95.3% |
| STORE_FAST | 8,220 | 2.7% |
| RETURN_VALUE | 5,800 | 1.9% |
| PUSH_EXC_INFO | 240 | 0.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_INT | 3,800 | 43.5% |
| LOAD_ATTR_SLOT | 3,720 | 42.6% |
| LOAD_FAST | 1,160 | 13.3% |
| BINARY_SUBSCR | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,560 | 86.5% |
| STORE_FAST | 1,180 | 13.5% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 62,120 | 50.0% |
| LOAD_FAST | 62,120 | 50.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 62,140 | 50.0% |
| LOAD_CONST | 62,140 | 50.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 346,100 | 97.7% |
| CALL_PY_EXACT_ARGS | 4,320 | 1.2% |
| PUSH_NULL | 3,560 | 1.0% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 349,020 | 98.6% |
| CALL_PY_EXACT_ARGS | 4,340 | 1.2% |
| MAKE_CELL | 620 | 0.2% |
| RESUME | 120 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 462,920 | 93.6% |
| BINARY_SLICE | 31,400 | 6.3% |
| CALL | 120 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 220,460 | 44.6% |
| JUMP_FORWARD | 220,460 | 44.6% |
| GET_ITER | 31,540 | 6.4% |
| CALL_LEN | 22,040 | 4.5% |
| CALL | 20 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,147,920 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 573,980 | 50.0% |
| TO_BOOL_BOOL | 573,960 | 50.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 22,040 | 88.2% |
| LOAD_DEREF | 2,920 | 11.7% |
| CALL | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 22,040 | 88.2% |
| GET_ITER | 2,940 | 11.8% |
| LOAD_GLOBAL | 20 | 0.1% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 3,734,000 | 86.4% |
| LOAD_FAST | 575,160 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 11,920 | 0.3% |
| CALL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,745,960 | 86.7% |
| TO_BOOL_BOOL | 573,960 | 13.3% |
| COMPARE_OP | 620 | 0.0% |
| STORE_FAST | 620 | 0.0% |
| TO_BOOL | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 13,438,080 | 35.3% |
| LOAD_GLOBAL_MODULE | 8,092,440 | 21.3% |
| LOAD_ATTR_SLOT | 7,514,720 | 19.7% |
| BUILD_TUPLE | 4,025,360 | 10.6% |
| LOAD_ATTR_MODULE | 3,691,480 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 36,071,560 | 94.8% |
| COPY | 1,671,440 | 4.4% |
| STORE_FAST | 288,460 | 0.8% |
| RETURN_VALUE | 35,260 | 0.1% |
| TO_BOOL | 1,100 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,880 | 54.7% |
| LOAD_DEREF | 28,440 | 25.2% |
| CALL_BUILTIN_CLASS | 22,040 | 19.5% |
| CALL_TUPLE_1 | 400 | 0.4% |
| CALL | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 28,680 | 25.4% |
| LOAD_GLOBAL_BUILTIN | 28,640 | 25.3% |
| LOAD_CONST | 22,360 | 19.8% |
| LOAD_FAST | 15,720 | 13.9% |
| STORE_FAST | 15,720 | 13.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 352,800 | 99.4% |
| CALL | 1,920 | 0.5% |
| RETURN_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 195,560 | 55.1% |
| JUMP_BACKWARD | 96,520 | 27.2% |
| LOAD_FAST | 62,680 | 17.7% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,943,240 | 62.0% |
| LOAD_FAST | 1,126,280 | 23.7% |
| LOAD_ATTR_SLOT | 576,880 | 12.2% |
| LOAD_ATTR_METHOD_NO_DICT | 99,840 | 2.1% |
| LOAD_ATTR | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,727,480 | 57.4% |
| CALL_PY_WITH_DEFAULTS | 908,960 | 19.1% |
| STORE_FAST | 895,320 | 18.9% |
| TO_BOOL_BOOL | 215,800 | 4.5% |
| CALL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 11,455,520 | 100.0% |
| CALL | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 8,062,080 | 70.4% |
| BUILD_TUPLE | 1,821,420 | 15.9% |
| RETURN_VALUE | 658,860 | 5.8% |
| UNPACK_SEQUENCE_TUPLE | 484,520 | 4.2% |
| JUMP_FORWARD | 215,820 | 1.9% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 461,640 | 68.1% |
| RETURN_GENERATOR | 215,800 | 31.9% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 461,660 | 68.1% |
| RETURN_VALUE | 215,820 | 31.9% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,197,900 | 61.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,717,080 | 14.0% |
| GET_ITER | 2,582,080 | 9.7% |
| LOAD_FAST_LOAD_FAST | 1,544,920 | 5.8% |
| LOAD_CONST | 1,294,040 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,386,480 | 76.8% |
| RETURN_GENERATOR | 5,621,600 | 21.2% |
| MAKE_CELL | 351,720 | 1.3% |
| COPY_FREE_VARS | 191,680 | 0.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 4,320 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 908,960 | 58.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 526,400 | 33.6% |
| LOAD_FAST | 99,920 | 6.4% |
| RETURN_VALUE | 24,280 | 1.5% |
| LOAD_ATTR_METHOD_NO_DICT | 6,480 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,017,420 | 64.9% |
| MAKE_CELL | 528,020 | 33.7% |
| RETURN_GENERATOR | 22,860 | 1.5% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 2,395,160 | 98.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 31,400 | 1.3% |
| CALL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,912,620 | 78.8% |
| RETURN_VALUE | 450,780 | 18.6% |
| STORE_FAST | 62,840 | 2.6% |
| CALL_LEN | 400 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,307,760 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IS_OP | 1,653,900 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 1,653,880 | 50.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 28,680 | 35.1% |
| LOAD_DEREF | 22,040 | 27.0% |
| LOAD_FAST | 15,640 | 19.1% |
| LOAD_ATTR_SLOT | 8,760 | 10.7% |
| LOAD_CONST | 6,320 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 77,860 | 95.3% |
| LOAD_FAST | 3,820 | 4.7% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 329,400 | 99.4% |
| LOAD_ATTR_SLOT | 1,800 | 0.5% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 329,420 | 99.5% |
| POP_JUMP_IF_FALSE | 1,820 | 0.5% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,046,360 | 88.2% |
| GET_ITER | 542,520 | 11.8% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 4,046,340 | 88.2% |
| POP_TOP | 542,560 | 11.8% |
| RESUME | 60 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,501,060 | 49.6% |
| GET_ITER | 4,480,300 | 49.4% |
| SWAP | 90,060 | 1.0% |
| LOAD_FAST | 2,940 | 0.0% |
| FOR_ITER | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,591,100 | 50.6% |
| JUMP_BACKWARD | 4,085,840 | 45.0% |
| LOAD_FAST | 394,620 | 4.3% |
| RETURN_CONST | 3,020 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 60 | 42.9% |
| JUMP_BACKWARD | 60 | 42.9% |
| FOR_ITER | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 57.1% |
| STORE_FAST | 60 | 42.9% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 766,100 | 75.0% |
| LOAD_FAST | 215,820 | 21.1% |
| SWAP | 39,640 | 3.9% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 774,340 | 75.8% |
| RETURN_CONST | 215,840 | 21.1% |
| SWAP | 31,440 | 3.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 11,920 | 100.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 10,315,280 | 52.4% |
| LOAD_FAST | 4,462,920 | 22.7% |
| RETURN_VALUE | 3,832,960 | 19.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 578,040 | 2.9% |
| LOAD_CONST | 215,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 11,455,520 | 58.2% |
| LOAD_FAST | 4,309,240 | 21.9% |
| LOAD_CONST | 3,183,420 | 16.2% |
| LOAD_FAST_LOAD_FAST | 580,180 | 2.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 99,840 | 0.5% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,584,360 | 92.9% |
| LOAD_DEREF | 535,040 | 6.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 45,420 | 0.6% |
| LOAD_ATTR | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,717,080 | 45.5% |
| LOAD_FAST_LOAD_FAST | 3,042,380 | 37.3% |
| LOAD_FAST | 579,520 | 7.1% |
| CALL_PY_WITH_DEFAULTS | 526,400 | 6.4% |
| LOAD_CONST | 231,480 | 2.8% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,117,560 | 100.0% |
| LOAD_ATTR | 1,300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 3,691,480 | 89.6% |
| PUSH_NULL | 195,900 | 4.8% |
| BUILD_TUPLE | 60,420 | 1.5% |
| LOAD_GLOBAL_MODULE | 60,360 | 1.5% |
| STORE_FAST | 45,140 | 1.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 590,720 | 99.1% |
| LOAD_FAST_LOAD_FAST | 4,720 | 0.8% |
| LOAD_ATTR | 440 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 578,040 | 97.0% |
| CALL_PY_EXACT_ARGS | 8,480 | 1.4% |
| CONTAINS_OP | 6,620 | 1.1% |
| STORE_FAST | 1,820 | 0.3% |
| LOAD_FAST | 620 | 0.1% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,309,600 | 99.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 9,360 | 0.2% |
| LOAD_FAST_LOAD_FAST | 2,040 | 0.0% |
| LOAD_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,912,600 | 44.3% |
| LOAD_FAST | 1,821,540 | 42.2% |
| FORMAT_SIMPLE | 573,980 | 13.3% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 9,360 | 0.2% |
| CONTAINS_OP | 2,060 | 0.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,979,000 | 99.9% |
| LOAD_DEREF | 3,360 | 0.1% |
| LOAD_ATTR_PROPERTY | 480 | 0.0% |
| LOAD_ATTR | 380 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,955,100 | 99.1% |
| RETURN_VALUE | 15,760 | 0.5% |
| STORE_FAST | 11,880 | 0.4% |
| LOAD_ATTR_PROPERTY | 480 | 0.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,016,880 | 62.4% |
| LOAD_DEREF | 7,296,880 | 35.0% |
| LOAD_FAST_LOAD_FAST | 417,400 | 2.0% |
| LOAD_ATTR_SLOT | 103,860 | 0.5% |
| COPY | 9,480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 10,315,280 | 49.5% |
| CALL_ISINSTANCE | 7,514,720 | 36.0% |
| TO_BOOL_BOOL | 625,640 | 3.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 576,880 | 2.8% |
| STORE_FAST | 538,300 | 2.6% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,818,520 | 31.6% |
| RESUME_CHECK | 13,434,800 | 17.8% |
| STORE_FAST | 13,364,280 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 8,011,380 | 10.6% |
| POP_JUMP_IF_NOT_NONE | 3,994,440 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 44,423,580 | 59.0% |
| CALL_ISINSTANCE | 13,438,080 | 17.8% |
| LOAD_GLOBAL_BUILTIN | 8,011,380 | 10.6% |
| BUILD_TUPLE | 3,994,460 | 5.3% |
| LOAD_FAST_LOAD_FAST | 2,958,680 | 3.9% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,782,080 | 42.2% |
| POP_JUMP_IF_FALSE | 5,767,160 | 20.6% |
| STORE_FAST_STORE_FAST | 4,401,160 | 15.7% |
| MAKE_FUNCTION | 1,912,600 | 6.8% |
| RETURN_VALUE | 1,216,240 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,570,460 | 48.5% |
| CALL_ISINSTANCE | 8,092,440 | 29.0% |
| LOAD_ATTR_MODULE | 4,117,560 | 14.7% |
| LOAD_FAST_LOAD_FAST | 1,462,780 | 5.2% |
| LOAD_DEREF | 180,600 | 0.6% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 20,386,480 | 35.3% |
| CACHE | 11,038,420 | 19.1% |
| SEND_GEN | 7,019,900 | 12.1% |
| POP_TOP | 6,731,980 | 11.7% |
| FOR_ITER_GEN | 4,046,340 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 26,776,460 | 46.3% |
| LOAD_GLOBAL_BUILTIN | 13,434,800 | 23.3% |
| POP_TOP | 9,304,160 | 16.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 7,019,880 | 12.1% |
| LOAD_DEREF | 732,140 | 1.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 7,019,880 | 69.6% |
| LOAD_CONST | 3,065,240 | 30.4% |
| SEND | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 7,019,900 | 69.6% |
| POP_TOP | 3,065,240 | 30.4% |
| RESUME | 20 | 0.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 480,360 | 65.7% |
| LOAD_FAST | 215,960 | 29.5% |
| LOAD_DEREF | 16,360 | 2.2% |
| SWAP | 9,480 | 1.3% |
| STORE_ATTR_SLOT | 7,980 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 230,940 | 31.6% |
| JUMP_BACKWARD | 227,000 | 31.1% |
| LOAD_FAST | 142,840 | 19.5% |
| LOAD_GLOBAL_MODULE | 69,120 | 9.5% |
| RETURN_CONST | 28,520 | 3.9% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 288,440 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 288,460 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 6,664,520 | 72.9% |
| LOAD_FAST | 1,472,480 | 16.1% |
| STORE_FAST_LOAD_FAST | 901,560 | 9.9% |
| LOAD_ATTR_SLOT | 48,620 | 0.5% |
| TO_BOOL_ALWAYS_TRUE | 45,640 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 5,522,820 | 60.4% |
| POP_JUMP_IF_FALSE | 3,564,600 | 39.0% |
| TO_BOOL_ALWAYS_TRUE | 45,640 | 0.5% |
| TO_BOOL_NONE | 13,940 | 0.2% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 36,071,560 | 73.3% |
| RETURN_VALUE | 4,936,880 | 10.0% |
| COPY | 3,361,160 | 6.8% |
| LOAD_FAST | 2,702,200 | 5.5% |
| LOAD_ATTR_SLOT | 625,640 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 38,512,620 | 78.2% |
| POP_JUMP_IF_TRUE | 6,670,000 | 13.5% |
| UNARY_NOT | 3,560,060 | 7.2% |
| EXTENDED_ARG | 485,880 | 1.0% |
| TO_BOOL_NONE | 20 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 2,960 | 98.7% |
| TO_BOOL | 40 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,940 | 98.0% |
| EXTENDED_ARG | 60 | 2.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 8,200 | 95.6% |
| COPY | 280 | 3.3% |
| TO_BOOL | 60 | 0.7% |
| LOAD_FAST | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,280 | 96.5% |
| POP_JUMP_IF_TRUE | 300 | 3.5% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,247,200 | 81.5% |
| COPY | 460,640 | 16.7% |
| RETURN_CONST | 26,120 | 0.9% |
| TO_BOOL_ALWAYS_TRUE | 13,940 | 0.5% |
| TO_BOOL_STR | 6,700 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,663,100 | 60.3% |
| POP_JUMP_IF_TRUE | 1,072,000 | 38.9% |
| TO_BOOL_ALWAYS_TRUE | 13,920 | 0.5% |
| TO_BOOL_STR | 6,700 | 0.2% |
| EXTENDED_ARG | 1,000 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,563,640 | 99.4% |
| TO_BOOL_NONE | 6,700 | 0.4% |
| LOAD_ATTR_SLOT | 2,920 | 0.2% |
| TO_BOOL | 160 | 0.0% |
| COPY | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,560,740 | 99.2% |
| TO_BOOL_NONE | 6,700 | 0.4% |
| POP_JUMP_IF_TRUE | 6,020 | 0.4% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 4,046,320 | 89.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 484,520 | 10.7% |
| UNPACK_SEQUENCE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,046,360 | 89.3% |
| STORE_FAST_STORE_FAST | 484,540 | 10.7% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 11,203,520 | 95.2% |
| RETURN_VALUE | 233,240 | 2.0% |
| LOAD_FAST | 220,440 | 1.9% |
| STORE_FAST | 62,120 | 0.5% |
| BUILD_TUPLE | 50,200 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 11,707,700 | 99.5% |
| STORE_FAST | 62,140 | 0.5% |


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
|     deferred | 23,420 | 12.0% |
|          hit | 171,780 | 87.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 300 | 60.0% |
| Failure | 200 | 40.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 180 | 90.0% |
| add different types | 20 | 10.0% |


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
|     deferred | 2,100 | 0.5% |
|          hit | 448,060 | 99.4% |
|         miss | 240 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 72.2% |
| Failure | 100 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 100 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,660,100 | 3.7% |
|          hit | 95,422,800 | 95.8% |
|         miss | 550,960 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,820 | 85.4% |
| Failure | 2,880 | 14.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 1,940 | 67.4% |
| class no vectorcall | 660 | 22.9% |
| no dict | 100 | 3.5% |
| cfunc varargs keywords | 100 | 3.5% |
| cfunc noargs | 60 | 2.1% |
| init not python | 20 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,322,520 | 76.0% |
|          hit | 412,920 | 23.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 7.4% |
| Failure | 3,500 | 92.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 1,360 | 38.9% |
| baseobject | 1,200 | 34.3% |
| other | 420 | 12.0% |
| set | 240 | 6.9% |
| string | 200 | 5.7% |
| big int | 80 | 2.3% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20,526,380 | 58.3% |
|          hit | 14,685,300 | 41.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 4.7% |
| Failure | 7,720 | 95.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| dict items | 5,640 | 73.1% |
| dict values | 740 | 9.6% |
| itertools | 540 | 7.0% |
| enumerate | 320 | 4.1% |
| other | 240 | 3.1% |
| dict keys | 120 | 1.6% |
| ascii string | 120 | 1.6% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 394,700 | 0.6% |
|        deopt | 385,000 | 0.6% |
|          hit | 53,814,680 | 88.4% |
|         miss | 6,897,060 | 11.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 137,300 | 97.6% |
| Failure | 3,340 | 2.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| metaclass attribute | 2,820 | 84.4% |
| method | 500 | 15.0% |
| mutable class | 20 | 0.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 6,000 | 0.0% |
|          hit | 103,275,520 | 100.0% |
|         miss | 4,240 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 6,160 | 100.0% |
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
|     deferred | 40 | 0.0% |
|          hit | 10,085,160 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 368,934,881,474,191,025,220 | 50,347,291,339,036,416.0% |
|          hit | 300,280 | 41.0% |
|         miss | 430,740 | 58.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,860 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 20 | 0.0% |
|          hit | 288,460 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,064,160 | 6.1% |
|          hit | 58,104,580 | 86.9% |
|         miss | 4,612,780 | 6.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 90,440 | 97.9% |
| Failure | 1,900 | 2.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,060 | 55.8% |
| sequence | 840 | 44.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 113,500 | 0.7% |
|          hit | 16,300,740 | 99.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 63.3% |
| Failure | 220 | 36.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 220 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 498,323,660 | 48.9% |
| Not specialized | 98,536,880 | 9.7% |
| Specialized hits | 410,736,780 | 40.3% |
| Specialized misses | 12,496,380 | 1.2% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR | 368,934,881,474,191,025,220 | 100.0% |
| FOR_ITER | 20,526,380 | 0.0% |
| TO_BOOL | 4,064,160 | 0.0% |
| CALL | 3,660,100 | 0.0% |
| COMPARE_OP | 1,322,520 | 0.0% |
| LOAD_ATTR | 394,700 | 0.0% |
| UNPACK_SEQUENCE | 113,500 | 0.0% |
| BINARY_OP | 23,420 | 0.0% |
| LOAD_GLOBAL | 6,000 | 0.0% |
| BINARY_SUBSCR | 2,100 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 3,952,840 | 31.6% |
| TO_BOOL_ALWAYS_TRUE | 3,159,420 | 25.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,417,840 | 19.3% |
| TO_BOOL_NONE | 1,096,040 | 8.8% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 498,260 | 4.0% |
| STORE_ATTR_SLOT | 430,740 | 3.4% |
| TO_BOOL_STR | 355,440 | 2.8% |
| CALL_PY_EXACT_ARGS | 320,180 | 2.6% |
| CALL_BOUND_METHOD_EXACT_ARGS | 230,780 | 1.8% |
| LOAD_ATTR_PROPERTY | 28,120 | 0.2% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 14,163,140 | 22.0% |
| Calls to Python functions inlined | 50,353,900 | 78.0% |
| Calls via PyEval_EvalFrame (total) | 14,163,140 | 22.0% |
| Calls via PyEval_EvalFrame (vector) | 5,780,900 | 9.0% |
| Calls via PyEval_EvalFrame (generator) | 8,382,240 | 13.0% |
| Calls via PyEval_EvalFrame (legacy) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 5,780,900 | 9.0% |
| Calls via PyEval_EvalFrame (build class) | 0 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 1,984,000 | 3.1% |
| Calls via PyEval_EvalFrame (function ex) | 32,160 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 3,774,020 | 5.8% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 240 | 0.0% |
| Frames pushed | 30,884,060 | 47.9% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 39,227,680 | 37.5% |
| Frees to freelist | 39,343,160 |  |
| Allocations | 65,241,720 | 62.5% |
| Allocations to 512 bytes | 65,202,200 | 62.4% |
| Allocations to 4 kbytes | 39,520 | 0.0% |
| Allocations over 4 kbytes | 0 | 0.0% |
| Frees | 65,466,219 |  |
| New values | 20,880 |  |
| Interpreter increfs | 408,009,760 | 68.9% |
| Interpreter decrefs | 466,752,940 | 67.8% |
| Increfs | 184,073,561 | 31.1% |
| Decrefs | 221,338,573 | 32.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 7,173,392 |  |
| Method cache misses | 586,928 |  |
| Method cache collisions | 584,894 |  |
| Method cache dunder hits | 61,356,558 |  |
| Method cache dunder misses | 2,542 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 200 | 10,700 | 405,280 |
| 1 | 20 | 3,380 | 681,920 |
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
