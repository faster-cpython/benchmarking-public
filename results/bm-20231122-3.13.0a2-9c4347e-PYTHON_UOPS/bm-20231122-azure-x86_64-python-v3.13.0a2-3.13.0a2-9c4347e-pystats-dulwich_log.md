
# Pystats results

- benchmark: dulwich_log
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 106,284,620 | 20.3% | 20.3% |  |
| LOAD_CONST | 44,640,340 | 8.5% | 28.8% |  |
| STORE_FAST | 30,466,620 | 5.8% | 34.6% |  |
| POP_JUMP_IF_FALSE | 25,087,880 | 4.8% | 39.4% |  |
| RESUME_CHECK | 21,559,660 | 4.1% | 43.5% |  |
| LOAD_ATTR_METHOD_NO_DICT | 16,965,980 | 3.2% | 46.7% |  |
| RETURN_VALUE | 16,810,400 | 3.2% | 50.0% |  |
| LOAD_FAST_LOAD_FAST | 16,055,420 | 3.1% | 53.0% |  |
| LOAD_ATTR_INSTANCE_VALUE | 15,152,940 | 2.9% | 55.9% |  |
| LOAD_GLOBAL_MODULE | 14,503,240 | 2.8% | 58.7% |  |
| CALL_PY_EXACT_ARGS | 12,225,740 | 2.3% | 61.0% |  |
| LOAD_GLOBAL_BUILTIN | 10,740,880 | 2.0% | 63.1% | 0.0% |
| STORE_ATTR_SLOT | 10,506,780 | 2.0% | 65.1% |  |
| LOAD_ATTR_SLOT | 9,459,500 | 1.8% | 66.9% |  |
| TO_BOOL_BOOL | 8,931,080 | 1.7% | 68.6% | 0.7% |
| COMPARE_OP | 8,206,180 | 1.6% | 70.1% |  |
| POP_TOP | 6,688,300 | 1.3% | 71.4% |  |
| BINARY_OP_ADD_INT | 6,519,240 | 1.2% | 72.7% |  |
| COMPARE_OP_INT | 6,100,720 | 1.2% | 73.8% |  |
| POP_JUMP_IF_NONE | 5,735,900 | 1.1% | 74.9% |  |
| BINARY_SLICE | 5,111,100 | 1.0% | 75.9% |  |
| STORE_FAST_STORE_FAST | 5,006,880 | 1.0% | 76.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 4,983,920 | 1.0% | 77.8% |  |
| PUSH_NULL | 4,854,600 | 0.9% | 78.7% |  |
| CALL | 4,764,700 | 0.9% | 79.6% |  |
| BUILD_TUPLE | 4,504,360 | 0.9% | 80.5% |  |
| JUMP_BACKWARD | 4,360,760 | 0.8% | 81.3% |  |
| BINARY_OP | 4,111,060 | 0.8% | 82.1% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 4,003,220 | 0.8% | 82.9% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,990,680 | 0.8% | 83.6% |  |
| POP_JUMP_IF_TRUE | 3,750,280 | 0.7% | 84.4% |  |
| NOP | 3,746,740 | 0.7% | 85.1% |  |
| LOAD_DEREF | 3,728,600 | 0.7% | 85.8% |  |
| RETURN_CONST | 3,496,340 | 0.7% | 86.4% |  |
| BINARY_OP_MULTIPLY_INT | 3,110,900 | 0.6% | 87.0% |  |
| BUILD_LIST | 3,002,900 | 0.6% | 87.6% |  |
| FOR_ITER | 3,001,640 | 0.6% | 88.2% |  |
| CALL_LEN | 2,999,100 | 0.6% | 88.8% |  |
| LOAD_ATTR_PROPERTY | 2,987,360 | 0.6% | 89.3% |  |
| CALL_BUILTIN_CLASS | 2,747,520 | 0.5% | 89.8% |  |
| POP_JUMP_IF_NOT_NONE | 2,746,760 | 0.5% | 90.4% |  |
| LOAD_ATTR_MODULE | 2,743,680 | 0.5% | 90.9% | 0.0% |
| CONTAINS_OP | 2,743,080 | 0.5% | 91.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 2,736,660 | 0.5% | 91.9% |  |
| JUMP_FORWARD | 2,347,720 | 0.4% | 92.4% |  |
| TO_BOOL | 2,003,160 | 0.4% | 92.8% |  |
| CALL_BUILTIN_O | 2,000,380 | 0.4% | 93.2% |  |
| CALL_BUILTIN_FAST | 1,751,460 | 0.3% | 93.5% |  |
| COPY | 1,750,320 | 0.3% | 93.8% |  |
| GET_ITER | 1,748,700 | 0.3% | 94.2% |  |
| CALL_METHOD_DESCRIPTOR_O | 1,742,320 | 0.3% | 94.5% | 0.0% |
| FOR_ITER_GEN | 1,503,660 | 0.3% | 94.8% |  |
| UNPACK_SEQUENCE_LIST | 1,503,640 | 0.3% | 95.1% |  |
| INTERPRETER_EXIT | 1,498,140 | 0.3% | 95.3% |  |
| CALL_LIST_APPEND | 1,257,660 | 0.2% | 95.6% |  |
| YIELD_VALUE | 1,253,480 | 0.2% | 95.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,099,060 | 0.2% | 96.0% | 0.0% |
| TO_BOOL_INT | 1,060,740 | 0.2% | 96.2% | 5.6% |
| LOAD_ATTR | 1,010,460 | 0.2% | 96.4% |  |
| BINARY_SUBSCR | 1,001,720 | 0.2% | 96.6% |  |
| CALL_ISINSTANCE | 999,580 | 0.2% | 96.8% |  |
| BINARY_SUBSCR_LIST_INT | 999,120 | 0.2% | 97.0% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 999,080 | 0.2% | 97.2% |  |
| CALL_KW | 998,740 | 0.2% | 97.4% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 997,120 | 0.2% | 97.6% | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 750,740 | 0.1% | 97.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 748,740 | 0.1% | 97.9% |  |
| CALL_PY_WITH_DEFAULTS | 748,400 | 0.1% | 98.0% |  |
| COPY_FREE_VARS | 747,140 | 0.1% | 98.1% |  |
| CHECK_EXC_MATCH | 746,580 | 0.1% | 98.3% |  |
| POP_EXCEPT | 746,580 | 0.1% | 98.4% |  |
| PUSH_EXC_INFO | 746,580 | 0.1% | 98.6% |  |
| BINARY_OP_SUBTRACT_INT | 643,840 | 0.1% | 98.7% |  |
| UNARY_NEGATIVE | 555,380 | 0.1% | 98.8% |  |
| BINARY_SUBSCR_GETITEM | 500,500 | 0.1% | 98.9% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 500,440 | 0.1% | 99.0% |  |
| SWAP | 499,120 | 0.1% | 99.1% |  |
| FOR_ITER_LIST | 498,760 | 0.1% | 99.2% |  |
| BINARY_SUBSCR_DICT | 498,720 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_UNICODE | 496,880 | 0.1% | 99.4% |  |
| BINARY_SUBSCR_TUPLE_INT | 255,400 | 0.0% | 99.4% |  |
| MAKE_FUNCTION | 250,960 | 0.0% | 99.5% |  |
| RETURN_GENERATOR | 250,280 | 0.0% | 99.5% |  |
| LOAD_SUPER_ATTR_METHOD | 250,260 | 0.0% | 99.6% |  |
| END_FOR | 250,240 | 0.0% | 99.6% |  |
| MAKE_CELL | 249,500 | 0.0% | 99.7% |  |
| EXTENDED_ARG | 248,880 | 0.0% | 99.7% |  |
| TO_BOOL_STR | 248,760 | 0.0% | 99.8% |  |
| BUILD_MAP | 248,560 | 0.0% | 99.8% |  |
| EXIT_INIT_CHECK | 248,520 | 0.0% | 99.9% |  |
| CALL_ALLOC_AND_ENTER_INIT | 248,520 | 0.0% | 99.9% |  |
| TO_BOOL_LIST | 248,500 | 0.0% | 99.9% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 248,380 | 0.0% | 100.0% |  |
| FOR_ITER_RANGE | 7,100 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 5,920 | 0.0% | 100.0% |  |
| STORE_ATTR | 4,920 | 0.0% | 100.0% |  |
| RESUME | 1,960 | 0.0% | 100.0% |  |
| IS_OP | 1,100 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 1,020 | 0.0% | 100.0% |  |
| STORE_NAME | 840 | 0.0% | 100.0% |  |
| TO_BOOL_NONE | 480 | 0.0% | 100.0% | 8.3% |
| FOR_ITER_TUPLE | 400 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 320 | 0.0% | 100.0% |  |
| CALL_FUNCTION_EX | 300 | 0.0% | 100.0% |  |
| IMPORT_FROM | 300 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 300 | 0.0% | 100.0% |  |
| IMPORT_NAME | 280 | 0.0% | 100.0% |  |
| LIST_APPEND | 280 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 260 | 0.0% | 100.0% |  |
| DICT_MERGE | 220 | 0.0% | 100.0% |  |
| LOAD_NAME | 220 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 220 | 0.0% | 100.0% |  |
| BEFORE_WITH | 200 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 180 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 180 | 0.0% | 100.0% |  |
| LIST_EXTEND | 180 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 180 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 120 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 60 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 60 | 0.0% | 100.0% |  |
| CALL_STR_1 | 60 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 40 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 20 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 20 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 20 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| POP_JUMP_IF_FALSE LOAD_FAST | 15,851,700 | 3.0% | 3.0% |
| LOAD_FAST LOAD_CONST | 14,658,580 | 2.8% | 5.8% |
| STORE_FAST LOAD_FAST | 14,512,820 | 2.8% | 8.6% |
| RESUME_CHECK LOAD_FAST | 12,814,320 | 2.4% | 11.0% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 11,920,900 | 2.3% | 13.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,727,140 | 2.2% | 15.5% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 9,253,960 | 1.8% | 17.3% |
| LOAD_FAST LOAD_ATTR_SLOT | 9,209,000 | 1.8% | 19.1% |
| LOAD_FAST STORE_ATTR_SLOT | 8,255,600 | 1.6% | 20.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 8,247,720 | 1.6% | 22.2% |
| COMPARE_OP POP_JUMP_IF_FALSE | 8,007,280 | 1.5% | 23.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 7,741,180 | 1.5% | 25.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 7,737,560 | 1.5% | 26.7% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 6,500,360 | 1.2% | 27.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 5,759,300 | 1.1% | 29.0% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 4,983,840 | 1.0% | 30.0% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 4,835,000 | 0.9% | 30.9% |
| LOAD_CONST LOAD_CONST | 4,760,160 | 0.9% | 31.8% |
| LOAD_GLOBAL_MODULE COMPARE_OP | 4,508,760 | 0.9% | 32.7% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 3,991,800 | 0.8% | 33.4% |
| LOAD_CONST BINARY_OP | 3,852,200 | 0.7% | 34.2% |
| STORE_ATTR_SLOT LOAD_FAST | 3,753,020 | 0.7% | 34.9% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 3,749,860 | 0.7% | 35.6% |
| POP_JUMP_IF_NONE LOAD_FAST | 3,735,620 | 0.7% | 36.3% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 3,730,080 | 0.7% | 37.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,598,560 | 0.7% | 37.7% |
| LOAD_CONST LOAD_FAST | 3,511,000 | 0.7% | 38.4% |
| LOAD_CONST BINARY_SLICE | 3,505,060 | 0.7% | 39.1% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 3,502,780 | 0.7% | 39.7% |
| LOAD_CONST COMPARE_OP_INT | 3,502,340 | 0.7% | 40.4% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS RETURN_VALUE | 3,480,280 | 0.7% | 41.1% |
| RETURN_VALUE LOAD_ATTR_METHOD_NO_DICT | 3,480,240 | 0.7% | 41.7% |
| LOAD_CONST STORE_FAST | 3,445,620 | 0.7% | 42.4% |
| PUSH_NULL LOAD_FAST | 3,349,640 | 0.6% | 43.0% |
| RETURN_VALUE STORE_FAST | 3,347,480 | 0.6% | 43.7% |
| LOAD_CONST BINARY_OP_ADD_INT | 3,058,920 | 0.6% | 44.2% |
| LOAD_FAST POP_JUMP_IF_NONE | 3,000,340 | 0.6% | 44.8% |
| NOP LOAD_FAST | 2,997,220 | 0.6% | 45.4% |
| LOAD_FAST LOAD_ATTR_PROPERTY | 2,987,120 | 0.6% | 46.0% |
| POP_TOP LOAD_FAST | 2,941,120 | 0.6% | 46.5% |
| LOAD_CONST CALL | 2,758,100 | 0.5% | 47.0% |
| CALL TO_BOOL_BOOL | 2,753,360 | 0.5% | 47.6% |
| STORE_FAST LOAD_CONST | 2,752,700 | 0.5% | 48.1% |
| LOAD_FAST LOAD_FAST | 2,751,700 | 0.5% | 48.6% |
| LOAD_FAST CALL_LEN | 2,750,500 | 0.5% | 49.1% |
| LOAD_ATTR_PROPERTY RESUME_CHECK | 2,739,060 | 0.5% | 49.7% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 2,610,400 | 0.5% | 50.2% |
| LOAD_CONST BINARY_OP_MULTIPLY_INT | 2,610,260 | 0.5% | 50.7% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 2,601,700 | 0.5% | 51.2% |
| STORE_FAST_STORE_FAST LOAD_FAST | 2,502,300 | 0.5% | 51.6% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 2,501,920 | 0.5% | 52.1% |
| BUILD_TUPLE RETURN_VALUE | 2,501,660 | 0.5% | 52.6% |
| LOAD_FAST STORE_FAST | 2,500,300 | 0.5% | 53.1% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 2,494,620 | 0.5% | 53.5% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,492,940 | 0.5% | 54.0% |
| LOAD_DEREF LOAD_ATTR_INSTANCE_VALUE | 2,484,040 | 0.5% | 54.5% |
| BINARY_OP_ADD_INT STORE_FAST | 2,304,320 | 0.4% | 54.9% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 2,250,020 | 0.4% | 55.4% |
| STORE_FAST LOAD_GLOBAL_MODULE | 2,249,280 | 0.4% | 55.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 2,248,480 | 0.4% | 56.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,248,320 | 0.4% | 56.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,246,820 | 0.4% | 57.1% |
| LOAD_ATTR_SLOT RETURN_VALUE | 2,238,640 | 0.4% | 57.5% |
| BINARY_SLICE RETURN_VALUE | 2,102,080 | 0.4% | 57.9% |
| BINARY_OP STORE_FAST | 2,100,340 | 0.4% | 58.3% |
| STORE_ATTR_SLOT LOAD_CONST | 2,001,120 | 0.4% | 58.7% |
| CALL_LEN LOAD_CONST | 2,001,080 | 0.4% | 59.1% |
| FOR_ITER STORE_FAST | 2,000,740 | 0.4% | 59.5% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 1,998,320 | 0.4% | 59.8% |
| LOAD_CONST COMPARE_OP | 1,947,980 | 0.4% | 60.2% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,894,300 | 0.4% | 60.6% |
| BINARY_OP_MULTIPLY_INT BINARY_OP_ADD_INT | 1,859,640 | 0.4% | 60.9% |
| LOAD_FAST PUSH_NULL | 1,849,620 | 0.4% | 61.3% |
| LOAD_FAST TO_BOOL | 1,751,920 | 0.3% | 61.6% |
| RETURN_VALUE UNPACK_SEQUENCE_TWO_TUPLE | 1,750,840 | 0.3% | 61.9% |
| JUMP_BACKWARD FOR_ITER | 1,750,220 | 0.3% | 62.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 1,747,240 | 0.3% | 62.6% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,745,600 | 0.3% | 62.9% |
| LOAD_FAST TO_BOOL_BOOL | 1,744,840 | 0.3% | 63.3% |
| RETURN_VALUE RETURN_VALUE | 1,744,660 | 0.3% | 63.6% |
| LOAD_FAST_LOAD_FAST COMPARE_OP | 1,744,180 | 0.3% | 63.9% |
| LOAD_ATTR_SLOT POP_JUMP_IF_NONE | 1,740,160 | 0.3% | 64.3% |
| LOAD_ATTR_SLOT LOAD_ATTR_METHOD_NO_DICT | 1,740,120 | 0.3% | 64.6% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 1,740,120 | 0.3% | 64.9% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 1,740,000 | 0.3% | 65.3% |
| BINARY_OP_ADD_INT BINARY_SLICE | 1,605,760 | 0.3% | 65.6% |
| BINARY_OP_ADD_INT LOAD_CONST | 1,604,460 | 0.3% | 65.9% |
| BINARY_SLICE STORE_FAST | 1,506,660 | 0.3% | 66.2% |
| UNPACK_SEQUENCE_LIST STORE_FAST_STORE_FAST | 1,503,640 | 0.3% | 66.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS UNPACK_SEQUENCE_LIST | 1,503,600 | 0.3% | 66.7% |
| CALL STORE_FAST | 1,501,520 | 0.3% | 67.0% |
| BUILD_LIST LOAD_FAST | 1,501,480 | 0.3% | 67.3% |
| CALL_BUILTIN_CLASS STORE_FAST | 1,501,460 | 0.3% | 67.6% |
| COMPARE_OP_INT POP_JUMP_IF_TRUE | 1,501,160 | 0.3% | 67.9% |
| BUILD_LIST STORE_FAST | 1,501,060 | 0.3% | 68.2% |
| STORE_ATTR_SLOT RETURN_CONST | 1,501,000 | 0.3% | 68.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,500,820 | 0.3% | 68.8% |
| STORE_FAST JUMP_BACKWARD | 1,499,700 | 0.3% | 69.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,498,280 | 0.3% | 69.3% |
| LOAD_FAST RETURN_VALUE | 1,497,880 | 0.3% | 69.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,505,060 | 68.6% |
| BINARY_OP_ADD_INT | 1,605,760 | 31.4% |
| BINARY_OP | 200 | 0.0% |
| LOAD_FAST | 60 | 0.0% |
| UNARY_NEGATIVE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,102,080 | 41.1% |
| STORE_FAST | 1,506,660 | 29.5% |
| CALL_BUILTIN_O | 751,000 | 14.7% |
| CALL_BUILTIN_CLASS | 750,280 | 14.7% |
| CALL | 440 | 0.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 997,960 | 66.6% |
| COPY_FREE_VARS | 250,340 | 16.7% |
| MAKE_CELL | 249,300 | 16.6% |
| RESUME | 500 | 0.0% |
| POP_TOP | 60 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 40.0% |
| RETURN_VALUE | 60 | 30.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 20.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 160 | 80.0% |
| STORE_FAST | 40 | 20.0% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 248,380 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 248,380 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,000,800 | 99.9% |
| BINARY_SUBSCR | 680 | 0.1% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,000,560 | 99.9% |
| BINARY_SUBSCR | 680 | 0.1% |
| STORE_FAST | 100 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 100 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 746,520 | 100.0% |
| LOAD_GLOBAL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 746,580 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20 | 100.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 250,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 250,240 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 248,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 248,520 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 748,800 | 42.8% |
| RETURN_VALUE | 498,740 | 28.5% |
| LOAD_FAST | 250,520 | 14.3% |
| RETURN_GENERATOR | 250,240 | 14.3% |
| CALL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,249,500 | 71.5% |
| FOR_ITER_GEN | 250,220 | 14.3% |
| FOR_ITER_LIST | 248,400 | 14.2% |
| FOR_ITER_RANGE | 420 | 0.0% |
| LOAD_FAST_AND_CLEAR | 120 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,000,800 | 66.8% |
| RETURN_VALUE | 497,280 | 33.2% |
| YIELD_VALUE | 60 | 0.0% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 60 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 250,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 250,300 | 99.7% |
| SET_FUNCTION_ATTRIBUTE | 320 | 0.1% |
| STORE_NAME | 240 | 0.1% |
| LOAD_CONST | 60 | 0.0% |
| BUILD_TUPLE | 20 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,497,540 | 40.0% |
| RESUME_CHECK | 1,249,300 | 33.3% |
| POP_JUMP_IF_TRUE | 500,600 | 13.4% |
| POP_JUMP_IF_FALSE | 250,300 | 6.7% |
| FOR_ITER | 248,360 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,997,220 | 80.0% |
| LOAD_GLOBAL_MODULE | 500,720 | 13.4% |
| LOAD_GLOBAL_BUILTIN | 248,340 | 6.6% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| LOAD_CONST | 100 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 746,540 | 100.0% |
| STORE_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 498,200 | 66.7% |
| RETURN_CONST | 248,340 | 33.3% |
| JUMP_BACKWARD | 40 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,497,300 | 22.4% |
| RESUME_CHECK | 1,253,440 | 18.7% |
| RETURN_CONST | 1,251,660 | 18.7% |
| CALL_METHOD_DESCRIPTOR_O | 1,241,520 | 18.6% |
| SWAP | 250,300 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,941,120 | 44.0% |
| RETURN_CONST | 749,260 | 11.2% |
| POP_EXCEPT | 746,540 | 11.2% |
| LOAD_CONST | 500,800 | 7.5% |
| JUMP_BACKWARD | 250,500 | 3.7% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 498,200 | 66.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 248,340 | 33.3% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 746,480 | 100.0% |
| LOAD_GLOBAL | 100 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,849,620 | 38.1% |
| LOAD_ATTR_MODULE | 1,500,820 | 30.9% |
| LOAD_FAST_LOAD_FAST | 1,003,200 | 20.7% |
| LOAD_ATTR | 250,520 | 5.2% |
| RETURN_VALUE | 250,240 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,349,640 | 69.0% |
| LOAD_CONST | 505,160 | 10.4% |
| CALL | 250,860 | 5.2% |
| LOAD_FAST_LOAD_FAST | 250,600 | 5.2% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 249,840 | 5.1% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 250,220 | 100.0% |
| COPY_FREE_VARS | 40 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 250,240 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 3,480,280 | 20.7% |
| BUILD_TUPLE | 2,501,660 | 14.9% |
| LOAD_ATTR_SLOT | 2,238,640 | 13.3% |
| BINARY_SLICE | 2,102,080 | 12.5% |
| RETURN_VALUE | 1,744,660 | 10.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,480,240 | 20.7% |
| STORE_FAST | 3,347,480 | 19.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,750,840 | 10.4% |
| RETURN_VALUE | 1,744,660 | 10.4% |
| BUILD_TUPLE | 1,253,080 | 7.5% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 66.7% |
| LOAD_CONST | 40 | 22.2% |
| STORE_SUBSCR | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 80 | 44.4% |
| STORE_SUBSCR_DICT | 40 | 22.2% |
| STORE_SUBSCR | 20 | 11.1% |
| JUMP_FORWARD | 20 | 11.1% |
| LOAD_FAST | 20 | 11.1% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,751,920 | 87.5% |
| LOAD_ATTR_INSTANCE_VALUE | 248,540 | 12.4% |
| TO_BOOL | 1,460 | 0.1% |
| CALL | 360 | 0.0% |
| BINARY_OP | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,253,860 | 62.6% |
| POP_JUMP_IF_TRUE | 747,040 | 37.3% |
| TO_BOOL | 1,460 | 0.1% |
| TO_BOOL_BOOL | 540 | 0.0% |
| TO_BOOL_INT | 160 | 0.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 307,040 | 55.3% |
| RETURN_VALUE | 248,300 | 44.7% |
| CALL | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 307,040 | 55.3% |
| LOAD_FAST | 248,320 | 44.7% |
| BINARY_SLICE | 20 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,852,200 | 93.7% |
| BINARY_OP_ADD_INT | 250,460 | 6.1% |
| BINARY_OP | 6,280 | 0.2% |
| LOAD_FAST | 1,180 | 0.0% |
| BINARY_OP_MULTIPLY_INT | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,100,340 | 51.1% |
| TO_BOOL_INT | 752,020 | 18.3% |
| CALL_BUILTIN_CLASS | 500,440 | 12.2% |
| BINARY_OP_ADD_INT | 250,600 | 6.1% |
| LOAD_FAST | 250,320 | 6.1% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 20 | 50.0% |
| STORE_FAST | 20 | 50.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,000,660 | 33.3% |
| STORE_ATTR_SLOT | 1,000,520 | 33.3% |
| RESUME_CHECK | 500,160 | 16.7% |
| LOAD_FAST | 250,560 | 8.3% |
| POP_TOP | 250,400 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,501,480 | 50.0% |
| STORE_FAST | 1,501,060 | 50.0% |
| SWAP | 120 | 0.0% |
| CALL_BUILTIN_CLASS | 120 | 0.0% |
| CALL | 40 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 248,300 | 99.9% |
| CALL_INTRINSIC_1 | 180 | 0.1% |
| LOAD_FAST | 40 | 0.0% |
| STORE_ATTR | 20 | 0.0% |
| RESUME | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 248,560 | 100.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,253,080 | 27.8% |
| LOAD_FAST_LOAD_FAST | 1,250,760 | 27.8% |
| LOAD_FAST | 999,300 | 22.2% |
| BUILD_TUPLE | 500,480 | 11.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 250,220 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,501,660 | 55.5% |
| YIELD_VALUE | 1,253,440 | 27.8% |
| BUILD_TUPLE | 500,480 | 11.1% |
| CALL_BUILTIN_FAST | 248,280 | 5.5% |
| LOAD_CONST | 300 | 0.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,758,100 | 57.9% |
| LOAD_FAST | 1,000,060 | 21.0% |
| LOAD_FAST_LOAD_FAST | 498,520 | 10.5% |
| PUSH_NULL | 250,860 | 5.3% |
| CALL_METHOD_DESCRIPTOR_O | 250,220 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,753,360 | 57.8% |
| STORE_FAST | 1,501,520 | 31.5% |
| LOAD_FAST | 250,680 | 5.3% |
| RESUME_CHECK | 248,860 | 5.2% |
| CALL | 3,460 | 0.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 220 | 73.3% |
| LOAD_FAST | 80 | 26.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 200 | 66.7% |
| COPY_FREE_VARS | 80 | 26.7% |
| RESUME_CHECK | 20 | 6.7% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 180 | 100.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 998,740 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 750,160 | 75.1% |
| RETURN_VALUE | 248,340 | 24.9% |
| RESUME | 120 | 0.0% |
| STORE_FAST | 100 | 0.0% |
| LOAD_FAST | 20 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,508,760 | 54.9% |
| LOAD_CONST | 1,947,980 | 23.7% |
| LOAD_FAST_LOAD_FAST | 1,744,180 | 21.3% |
| COMPARE_OP | 4,540 | 0.1% |
| LOAD_GLOBAL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 8,007,280 | 97.6% |
| STORE_FAST | 193,440 | 2.4% |
| COMPARE_OP | 4,540 | 0.1% |
| COMPARE_OP_INT | 640 | 0.0% |
| POP_JUMP_IF_TRUE | 200 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,491,720 | 54.4% |
| LOAD_GLOBAL_MODULE | 750,160 | 27.3% |
| LOAD_CONST | 500,500 | 18.2% |
| LOAD_FAST | 320 | 0.0% |
| LOAD_ATTR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,494,620 | 90.9% |
| STORE_FAST | 248,340 | 9.1% |
| POP_JUMP_IF_TRUE | 120 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,000,920 | 57.2% |
| LOAD_CONST | 307,040 | 17.5% |
| LOAD_FAST | 248,700 | 14.2% |
| POP_JUMP_IF_FALSE | 193,600 | 11.1% |
| COMPARE_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,193,920 | 68.2% |
| TO_BOOL_INT | 307,400 | 17.6% |
| LOAD_ATTR_INSTANCE_VALUE | 248,300 | 14.2% |
| TO_BOOL_NONE | 360 | 0.0% |
| TO_BOOL | 240 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 250,340 | 33.5% |
| CALL_PY_EXACT_ARGS | 248,340 | 33.2% |
| LOAD_ATTR_PROPERTY | 248,300 | 33.2% |
| CALL | 80 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 746,960 | 100.0% |
| RESUME | 140 | 0.0% |
| RETURN_GENERATOR | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 220 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_LIST | 248,460 | 99.8% |
| POP_JUMP_IF_FALSE | 340 | 0.1% |
| COMPARE_OP_INT | 40 | 0.0% |
| TO_BOOL | 20 | 0.0% |
| COMPARE_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 248,540 | 99.9% |
| JUMP_BACKWARD | 340 | 0.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,750,220 | 58.3% |
| GET_ITER | 1,249,500 | 41.6% |
| FOR_ITER | 1,880 | 0.1% |
| LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,000,740 | 66.7% |
| LOAD_FAST_LOAD_FAST | 250,240 | 8.3% |
| LOAD_GLOBAL_BUILTIN | 249,840 | 8.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 249,840 | 8.3% |
| NOP | 248,360 | 8.3% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 240 | 80.0% |
| STORE_NAME | 60 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 160 | 53.3% |
| STORE_NAME | 140 | 46.7% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 240 | 85.7% |
| STORE_NAME | 40 | 14.3% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 520 | 47.3% |
| LOAD_FAST_LOAD_FAST | 420 | 38.2% |
| LOAD_GLOBAL | 60 | 5.5% |
| LOAD_ATTR | 40 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,080 | 98.2% |
| POP_JUMP_IF_TRUE | 20 | 1.8% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,499,700 | 34.4% |
| POP_JUMP_IF_FALSE | 1,098,760 | 25.2% |
| STORE_FAST_STORE_FAST | 1,003,200 | 23.0% |
| CALL_LIST_APPEND | 257,560 | 5.9% |
| POP_TOP | 250,500 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 1,750,220 | 40.1% |
| FOR_ITER_GEN | 1,253,420 | 28.7% |
| LOAD_FAST_LOAD_FAST | 848,640 | 19.5% |
| FOR_ITER_LIST | 250,300 | 5.7% |
| LOAD_FAST | 250,040 | 5.7% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,100,320 | 46.9% |
| POP_EXCEPT | 498,200 | 21.2% |
| POP_TOP | 250,260 | 10.7% |
| POP_JUMP_IF_FALSE | 249,880 | 10.6% |
| STORE_ATTR_INSTANCE_VALUE | 248,700 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,347,760 | 57.4% |
| LOAD_FAST | 999,840 | 42.6% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 280 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 180 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 499,940 | 49.5% |
| LOAD_FAST_LOAD_FAST | 250,660 | 24.8% |
| LOAD_GLOBAL_MODULE | 250,400 | 24.8% |
| LOAD_FAST | 6,300 | 0.6% |
| LOAD_ATTR | 1,560 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 251,580 | 24.9% |
| PUSH_NULL | 250,520 | 24.8% |
| CALL_PY_EXACT_ARGS | 250,200 | 24.8% |
| CALL_PY_WITH_DEFAULTS | 249,840 | 24.7% |
| LOAD_ATTR | 1,560 | 0.2% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,658,580 | 32.8% |
| LOAD_ATTR_METHOD_NO_DICT | 7,741,180 | 17.3% |
| LOAD_CONST | 4,760,160 | 10.7% |
| STORE_FAST | 2,752,700 | 6.2% |
| LOAD_FAST_LOAD_FAST | 2,610,400 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 4,983,840 | 11.2% |
| LOAD_CONST | 4,760,160 | 10.7% |
| BINARY_OP | 3,852,200 | 8.6% |
| LOAD_FAST | 3,511,000 | 7.9% |
| BINARY_SLICE | 3,505,060 | 7.9% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 745,180 | 20.0% |
| LOAD_FAST | 745,000 | 20.0% |
| STORE_FAST | 498,520 | 13.4% |
| RESUME_CHECK | 497,580 | 13.3% |
| LOAD_GLOBAL_MODULE | 496,600 | 13.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,484,040 | 66.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 498,320 | 13.4% |
| STORE_ATTR_INSTANCE_VALUE | 496,680 | 13.3% |
| BINARY_OP_ADD_UNICODE | 248,280 | 6.7% |
| LOAD_ATTR | 600 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 15,851,700 | 14.9% |
| STORE_FAST | 14,512,820 | 13.7% |
| RESUME_CHECK | 12,814,320 | 12.1% |
| LOAD_GLOBAL_BUILTIN | 8,247,720 | 7.8% |
| LOAD_ATTR_INSTANCE_VALUE | 4,835,000 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 14,658,580 | 13.8% |
| LOAD_ATTR_INSTANCE_VALUE | 11,920,900 | 11.2% |
| LOAD_ATTR_METHOD_NO_DICT | 9,253,960 | 8.7% |
| LOAD_ATTR_SLOT | 9,209,000 | 8.7% |
| STORE_ATTR_SLOT | 8,255,600 | 7.8% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 120 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 80 | 44.4% |
| LOAD_FAST_LOAD_FAST | 60 | 33.3% |
| LOAD_FAST | 20 | 11.1% |
| LOAD_ATTR_METHOD_NO_DICT | 20 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_NOT_NONE | 80 | 44.4% |
| BUILD_TUPLE | 60 | 33.3% |
| LOAD_FAST | 20 | 11.1% |
| CALL_LIST_APPEND | 20 | 11.1% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,601,700 | 16.2% |
| POP_JUMP_IF_FALSE | 1,894,300 | 11.8% |
| JUMP_FORWARD | 1,347,760 | 8.4% |
| POP_JUMP_IF_NONE | 1,253,080 | 7.8% |
| STORE_ATTR_SLOT | 1,250,200 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,610,400 | 16.3% |
| STORE_ATTR_SLOT | 2,250,020 | 14.0% |
| COMPARE_OP | 1,744,180 | 10.9% |
| COMPARE_OP_INT | 1,349,560 | 8.4% |
| BUILD_TUPLE | 1,250,760 | 7.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,280 | 21.6% |
| STORE_FAST | 900 | 15.2% |
| POP_JUMP_IF_FALSE | 660 | 11.1% |
| RESUME | 540 | 9.1% |
| RESUME_CHECK | 320 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,480 | 25.0% |
| LOAD_GLOBAL_BUILTIN | 1,240 | 20.9% |
| LOAD_GLOBAL_MODULE | 1,240 | 20.9% |
| LOAD_ATTR | 440 | 7.4% |
| CALL | 340 | 5.7% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 36.4% |
| RESUME | 60 | 27.3% |
| STORE_NAME | 40 | 18.2% |
| MAKE_FUNCTION | 20 | 9.1% |
| LOAD_NAME | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 80 | 36.4% |
| CALL | 60 | 27.3% |
| BUILD_TUPLE | 40 | 18.2% |
| LOAD_CONST | 20 | 9.1% |
| LOAD_NAME | 20 | 9.1% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 33.3% |
| LOAD_FAST_LOAD_FAST | 20 | 33.3% |
| LOAD_SUPER_ATTR_METHOD | 20 | 33.3% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 249,300 | 99.9% |
| CALL | 160 | 0.1% |
| CALL_PY_EXACT_ARGS | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 249,440 | 100.0% |
| RESUME | 60 | 0.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 8,007,280 | 31.9% |
| TO_BOOL_BOOL | 7,737,560 | 30.8% |
| COMPARE_OP_INT | 3,598,560 | 14.3% |
| CONTAINS_OP | 2,494,620 | 9.9% |
| TO_BOOL | 1,253,860 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,851,700 | 63.2% |
| LOAD_FAST_LOAD_FAST | 1,894,300 | 7.6% |
| LOAD_GLOBAL_MODULE | 1,745,600 | 7.0% |
| POP_TOP | 1,497,300 | 6.0% |
| JUMP_BACKWARD | 1,098,760 | 4.4% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,000,340 | 52.3% |
| LOAD_ATTR_SLOT | 1,740,160 | 30.3% |
| LOAD_ATTR_INSTANCE_VALUE | 744,980 | 13.0% |
| CALL_BUILTIN_FAST | 250,220 | 4.4% |
| LOAD_ATTR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,735,620 | 65.1% |
| LOAD_FAST_LOAD_FAST | 1,253,080 | 21.8% |
| LOAD_GLOBAL_BUILTIN | 746,960 | 13.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,747,240 | 63.6% |
| LOAD_ATTR_INSTANCE_VALUE | 999,200 | 36.4% |
| CALL_BUILTIN_FAST | 120 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |
| LOAD_FAST_CHECK | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,998,320 | 72.8% |
| LOAD_GLOBAL_MODULE | 250,380 | 9.1% |
| LOAD_GLOBAL_BUILTIN | 248,400 | 9.0% |
| RETURN_CONST | 248,340 | 9.0% |
| JUMP_BACKWARD | 860 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 1,501,160 | 40.0% |
| TO_BOOL_BOOL | 1,192,400 | 31.8% |
| TO_BOOL | 747,040 | 19.9% |
| TO_BOOL_INT | 309,020 | 8.2% |
| TO_BOOL_NONE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,496,980 | 39.9% |
| LOAD_FAST_LOAD_FAST | 500,960 | 13.4% |
| NOP | 500,600 | 13.3% |
| LOAD_GLOBAL_BUILTIN | 499,080 | 13.3% |
| STORE_FAST | 307,040 | 8.2% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,501,000 | 42.9% |
| POP_TOP | 749,260 | 21.4% |
| STORE_ATTR_INSTANCE_VALUE | 496,980 | 14.2% |
| POP_JUMP_IF_FALSE | 251,360 | 7.2% |
| POP_EXCEPT | 248,340 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,251,660 | 35.8% |
| INTERPRETER_EXIT | 1,000,800 | 28.6% |
| STORE_FAST | 496,780 | 14.2% |
| END_FOR | 250,240 | 7.2% |
| EXIT_INIT_CHECK | 248,520 | 7.1% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 50.0% |
| STORE_NAME | 60 | 18.8% |
| LOAD_DEREF | 40 | 12.5% |
| LOAD_GLOBAL_MODULE | 40 | 12.5% |
| STORE_FAST | 20 | 6.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980 | 60.6% |
| LOAD_FAST_LOAD_FAST | 1,500 | 30.5% |
| LOAD_DEREF | 280 | 5.7% |
| SWAP | 80 | 1.6% |
| LOAD_ATTR | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,160 | 23.6% |
| LOAD_FAST | 1,020 | 20.7% |
| STORE_ATTR_INSTANCE_VALUE | 860 | 17.5% |
| LOAD_FAST_LOAD_FAST | 480 | 9.8% |
| LOAD_CONST | 440 | 8.9% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,445,620 | 11.3% |
| RETURN_VALUE | 3,347,480 | 11.0% |
| LOAD_FAST | 2,500,300 | 8.2% |
| BINARY_OP_ADD_INT | 2,304,320 | 7.6% |
| BINARY_OP | 2,100,340 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,512,820 | 47.6% |
| LOAD_CONST | 2,752,700 | 9.0% |
| LOAD_FAST_LOAD_FAST | 2,601,700 | 8.5% |
| LOAD_GLOBAL_BUILTIN | 2,501,920 | 8.2% |
| LOAD_GLOBAL_MODULE | 2,249,280 | 7.4% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 280 | 93.3% |
| UNPACK_SEQUENCE | 20 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 280 | 93.3% |
| STORE_ATTR | 20 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 3,502,780 | 70.0% |
| UNPACK_SEQUENCE_LIST | 1,503,640 | 30.0% |
| UNPACK_SEQUENCE | 380 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,502,300 | 50.0% |
| JUMP_BACKWARD | 1,003,200 | 20.0% |
| LOAD_FAST_LOAD_FAST | 750,420 | 15.0% |
| LOAD_GLOBAL_BUILTIN | 500,460 | 10.0% |
| LOAD_GLOBAL_MODULE | 250,200 | 5.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 240 | 28.6% |
| LOAD_CONST | 200 | 23.8% |
| IMPORT_FROM | 140 | 16.7% |
| LOAD_NAME | 80 | 9.5% |
| CALL | 60 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 520 | 61.9% |
| POP_TOP | 80 | 9.5% |
| RETURN_CONST | 80 | 9.5% |
| LOAD_BUILD_CLASS | 60 | 7.1% |
| IMPORT_FROM | 60 | 7.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 250,300 | 50.1% |
| BINARY_OP_ADD_INT | 248,340 | 49.8% |
| BUILD_LIST | 120 | 0.0% |
| LOAD_FAST_AND_CLEAR | 120 | 0.0% |
| FOR_ITER_TUPLE | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 250,300 | 50.1% |
| STORE_ATTR_INSTANCE_VALUE | 248,300 | 49.7% |
| BUILD_LIST | 120 | 0.0% |
| STORE_FAST | 120 | 0.0% |
| FOR_ITER_TUPLE | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 480 | 47.1% |
| LOAD_FAST | 160 | 15.7% |
| CALL | 120 | 11.8% |
| FOR_ITER | 100 | 9.8% |
| STORE_ATTR | 40 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 380 | 37.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 33.3% |
| LOAD_FAST | 120 | 11.8% |
| UNPACK_SEQUENCE_TUPLE | 80 | 7.8% |
| STORE_FAST | 40 | 3.9% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 1,253,440 | 100.0% |
| CALL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,253,400 | 100.0% |
| INTERPRETER_EXIT | 60 | 0.0% |
| UNPACK_SEQUENCE | 20 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,080 | 55.1% |
| CACHE | 500 | 25.5% |
| COPY_FREE_VARS | 140 | 7.1% |
| CALL_KW | 120 | 6.1% |
| MAKE_CELL | 60 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 760 | 38.8% |
| LOAD_GLOBAL | 540 | 27.6% |
| LOAD_FAST_LOAD_FAST | 180 | 9.2% |
| LOAD_CONST | 140 | 7.1% |
| NOP | 120 | 6.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,058,920 | 46.9% |
| BINARY_OP_MULTIPLY_INT | 1,859,640 | 28.5% |
| LOAD_FAST_LOAD_FAST | 1,099,640 | 16.9% |
| BINARY_OP | 250,600 | 3.8% |
| CALL_LEN | 249,860 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,304,320 | 35.3% |
| BINARY_SLICE | 1,605,760 | 24.6% |
| LOAD_CONST | 1,604,460 | 24.6% |
| BINARY_OP_MULTIPLY_INT | 500,440 | 7.7% |
| BINARY_OP | 250,460 | 3.8% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 248,380 | 50.0% |
| LOAD_DEREF | 248,280 | 50.0% |
| LOAD_FAST_LOAD_FAST | 160 | 0.0% |
| BINARY_SUBSCR_LIST_INT | 40 | 0.0% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 248,380 | 50.0% |
| CALL_BUILTIN_FAST | 248,280 | 50.0% |
| CALL | 100 | 0.0% |
| LOAD_FAST | 80 | 0.0% |
| STORE_FAST | 40 | 0.0% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,610,260 | 83.9% |
| BINARY_OP_ADD_INT | 500,440 | 16.1% |
| BINARY_OP | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,859,640 | 59.8% |
| LOAD_FAST | 1,000,920 | 32.2% |
| LOAD_CONST | 249,860 | 8.0% |
| BINARY_OP | 480 | 0.0% |


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
| LOAD_CONST | 643,760 | 100.0% |
| BINARY_OP | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 394,740 | 61.3% |
| BINARY_SUBSCR_LIST_INT | 249,080 | 38.7% |
| BINARY_SUBSCR | 20 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 250,260 | 50.2% |
| LOAD_FAST | 248,380 | 49.8% |
| BINARY_SUBSCR | 40 | 0.0% |
| LOAD_CONST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 498,200 | 99.9% |
| STORE_FAST | 480 | 0.1% |
| LOAD_FAST | 20 | 0.0% |
| CALL_BUILTIN_CLASS | 20 | 0.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500,460 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 500,500 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 499,740 | 50.0% |
| LOAD_FAST | 250,200 | 25.0% |
| BINARY_OP_SUBTRACT_INT | 249,080 | 24.9% |
| BINARY_SUBSCR | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 499,760 | 50.0% |
| STORE_FAST | 499,320 | 50.0% |
| BINARY_OP_ADD_UNICODE | 40 | 0.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 255,360 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 250,280 | 98.0% |
| CALL_LIST_APPEND | 5,080 | 2.0% |
| RETURN_VALUE | 20 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 248,440 | 100.0% |
| CALL | 40 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 248,520 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,098,960 | 100.0% |
| LOAD_CONST | 80 | 0.0% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,098,980 | 100.0% |
| POP_TOP | 80 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,247,400 | 45.4% |
| BINARY_SLICE | 750,280 | 27.3% |
| BINARY_OP | 500,440 | 18.2% |
| LOAD_GLOBAL_BUILTIN | 248,640 | 9.0% |
| LOAD_CONST | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,501,460 | 54.6% |
| GET_ITER | 748,800 | 27.3% |
| LOAD_FAST | 248,860 | 9.1% |
| RETURN_VALUE | 248,300 | 9.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 80 | 0.0% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 750,380 | 42.8% |
| LOAD_FAST | 254,940 | 14.6% |
| LOAD_ATTR_INSTANCE_VALUE | 249,240 | 14.2% |
| BUILD_TUPLE | 248,280 | 14.2% |
| BINARY_OP_ADD_UNICODE | 248,280 | 14.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 999,040 | 57.0% |
| POP_JUMP_IF_NONE | 250,220 | 14.3% |
| RETURN_VALUE | 248,440 | 14.2% |
| POP_TOP | 248,360 | 14.2% |
| LOAD_CONST | 5,100 | 0.3% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 498,740 | 50.0% |
| PUSH_NULL | 249,840 | 25.1% |
| LOAD_CONST | 248,380 | 24.9% |
| CALL_BUILTIN_CLASS | 80 | 0.0% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 498,280 | 50.0% |
| LOAD_CONST | 250,220 | 25.1% |
| PUSH_EXC_INFO | 248,340 | 24.9% |
| RETURN_VALUE | 260 | 0.0% |
| BEFORE_WITH | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,000,920 | 50.0% |
| BINARY_SLICE | 751,000 | 37.5% |
| LOAD_ATTR_INSTANCE_VALUE | 248,280 | 12.4% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 751,680 | 37.6% |
| RETURN_VALUE | 500,460 | 25.0% |
| CALL_LIST_APPEND | 499,900 | 25.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 248,280 | 12.4% |
| CALL | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 749,160 | 74.9% |
| LOAD_GLOBAL_MODULE | 250,220 | 25.0% |
| CALL | 180 | 0.0% |
| BUILD_TUPLE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 999,400 | 100.0% |
| TO_BOOL | 180 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,750,500 | 91.7% |
| LOAD_ATTR_INSTANCE_VALUE | 248,340 | 8.3% |
| CALL | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,001,080 | 66.7% |
| STORE_FAST | 499,760 | 16.7% |
| BINARY_OP_ADD_INT | 249,860 | 8.3% |
| LOAD_GLOBAL_MODULE | 248,280 | 8.3% |
| BINARY_OP | 40 | 0.0% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 752,120 | 59.8% |
| CALL_BUILTIN_O | 499,900 | 39.7% |
| BINARY_SUBSCR_TUPLE_INT | 5,080 | 0.4% |
| BINARY_SLICE | 320 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 499,900 | 39.7% |
| LOAD_FAST | 499,760 | 39.7% |
| JUMP_BACKWARD | 257,560 | 20.5% |
| JUMP_FORWARD | 180 | 0.0% |
| LOAD_FAST_LOAD_FAST | 180 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 250,220 | 25.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 250,200 | 25.0% |
| LOAD_FAST | 249,860 | 25.0% |
| LOAD_ATTR_MODULE | 248,320 | 24.9% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 250,220 | 25.0% |
| BUILD_TUPLE | 250,220 | 25.0% |
| POP_TOP | 249,900 | 25.0% |
| STORE_FAST | 248,420 | 24.9% |
| LIST_APPEND | 280 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,983,840 | 100.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,480,280 | 69.8% |
| UNPACK_SEQUENCE_LIST | 1,503,600 | 30.2% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 498,480 | 66.6% |
| LOAD_ATTR_METHOD_LAZY_DICT | 250,200 | 33.4% |
| CALL | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 250,220 | 33.4% |
| RETURN_VALUE | 250,220 | 33.4% |
| STORE_FAST | 248,300 | 33.2% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,245,280 | 71.5% |
| RETURN_VALUE | 496,560 | 28.5% |
| CALL | 180 | 0.0% |
| LOAD_CONST | 120 | 0.0% |
| STORE_FAST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,241,520 | 71.3% |
| BUILD_TUPLE | 250,220 | 14.4% |
| CALL | 250,220 | 14.4% |
| RETURN_VALUE | 120 | 0.0% |
| STORE_FAST | 120 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,500,360 | 53.2% |
| LOAD_ATTR_METHOD_NO_DICT | 3,730,080 | 30.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 995,100 | 8.1% |
| LOAD_FAST_LOAD_FAST | 498,580 | 4.1% |
| LOAD_ATTR | 250,200 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,727,140 | 95.9% |
| RETURN_GENERATOR | 250,220 | 2.0% |
| COPY_FREE_VARS | 248,340 | 2.0% |
| MAKE_CELL | 40 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 250,200 | 33.4% |
| LOAD_ATTR | 249,840 | 33.4% |
| LOAD_CONST | 248,280 | 33.2% |
| CALL | 60 | 0.0% |
| LOAD_FAST_LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 748,400 | 100.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 40 | 66.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 33.3% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 20 | 100.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 20 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,502,340 | 57.4% |
| LOAD_FAST_LOAD_FAST | 1,349,560 | 22.1% |
| LOAD_GLOBAL_MODULE | 747,920 | 12.3% |
| LOAD_ATTR_INSTANCE_VALUE | 249,880 | 4.1% |
| LOAD_ATTR_SLOT | 249,840 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,598,560 | 59.0% |
| POP_JUMP_IF_TRUE | 1,501,160 | 24.6% |
| COPY | 1,000,920 | 16.4% |
| EXTENDED_ARG | 40 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 120 | 54.5% |
| LOAD_CONST | 60 | 27.3% |
| COMPARE_OP | 20 | 9.1% |
| LOAD_FAST | 20 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220 | 100.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,253,420 | 83.4% |
| GET_ITER | 250,220 | 16.6% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,253,400 | 83.4% |
| POP_TOP | 250,220 | 16.6% |
| RESUME | 40 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 250,300 | 50.2% |
| GET_ITER | 248,400 | 49.8% |
| FOR_ITER | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 250,280 | 50.2% |
| LOAD_CONST | 248,320 | 49.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 80 | 0.0% |
| LOAD_FAST | 60 | 0.0% |
| BUILD_LIST | 20 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,600 | 93.0% |
| GET_ITER | 420 | 5.9% |
| FOR_ITER | 80 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,600 | 93.0% |
| LOAD_FAST | 300 | 4.2% |
| LOAD_CONST | 200 | 2.8% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 280 | 70.0% |
| SWAP | 120 | 30.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 280 | 70.0% |
| SWAP | 120 | 30.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,920,900 | 78.7% |
| LOAD_DEREF | 2,484,040 | 16.4% |
| LOAD_FAST_LOAD_FAST | 498,180 | 3.3% |
| COPY | 248,300 | 1.6% |
| LOAD_ATTR | 1,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,835,000 | 31.9% |
| LOAD_ATTR_METHOD_NO_DICT | 1,740,000 | 11.5% |
| CONTAINS_OP | 1,491,720 | 9.8% |
| LOAD_FAST_LOAD_FAST | 1,104,060 | 7.3% |
| POP_JUMP_IF_NOT_NONE | 999,200 | 6.6% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500,400 | 100.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 250,200 | 50.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 250,200 | 50.0% |
| CALL | 40 | 0.0% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,253,960 | 54.5% |
| RETURN_VALUE | 3,480,240 | 20.5% |
| LOAD_ATTR_SLOT | 1,740,120 | 10.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,740,000 | 10.3% |
| LOAD_CONST | 500,480 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 7,741,180 | 45.6% |
| LOAD_FAST | 3,991,800 | 23.5% |
| CALL_PY_EXACT_ARGS | 3,730,080 | 22.0% |
| LOAD_GLOBAL_BUILTIN | 499,920 | 2.9% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 498,480 | 2.9% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,492,940 | 62.5% |
| RETURN_VALUE | 998,880 | 25.0% |
| LOAD_DEREF | 498,320 | 12.5% |
| LOAD_ATTR | 440 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,248,320 | 56.3% |
| CALL_PY_EXACT_ARGS | 995,100 | 24.9% |
| LOAD_FAST_LOAD_FAST | 498,600 | 12.5% |
| LOAD_CONST | 248,300 | 6.2% |
| LOAD_GLOBAL_BUILTIN | 120 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,246,820 | 81.9% |
| LOAD_ATTR_MODULE | 496,640 | 18.1% |
| LOAD_ATTR | 160 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,500,820 | 54.7% |
| LOAD_ATTR_MODULE | 496,640 | 18.1% |
| LOAD_FAST | 248,540 | 9.1% |
| LOAD_FAST_LOAD_FAST | 248,360 | 9.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 248,320 | 9.1% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,987,120 | 100.0% |
| LOAD_ATTR | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,739,060 | 91.7% |
| COPY_FREE_VARS | 248,300 | 8.3% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,209,000 | 97.4% |
| LOAD_FAST_LOAD_FAST | 249,840 | 2.6% |
| LOAD_ATTR | 460 | 0.0% |
| LOAD_ATTR_MODULE | 180 | 0.0% |
| RETURN_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,238,640 | 23.7% |
| POP_JUMP_IF_NONE | 1,740,160 | 18.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,740,120 | 18.4% |
| TO_BOOL_BOOL | 1,740,120 | 18.4% |
| STORE_FAST | 750,400 | 7.9% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,501,920 | 23.3% |
| RESUME_CHECK | 2,248,480 | 20.9% |
| LOAD_FAST | 999,040 | 9.3% |
| POP_JUMP_IF_NONE | 746,960 | 7.0% |
| PUSH_EXC_INFO | 746,480 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,247,720 | 76.8% |
| CALL_ISINSTANCE | 749,160 | 7.0% |
| LOAD_GLOBAL_MODULE | 746,920 | 7.0% |
| CHECK_EXC_MATCH | 746,520 | 7.0% |
| CALL_BUILTIN_CLASS | 248,640 | 2.3% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,759,300 | 39.7% |
| STORE_FAST | 2,249,280 | 15.5% |
| POP_JUMP_IF_FALSE | 1,745,600 | 12.0% |
| RESUME_CHECK | 1,498,280 | 10.3% |
| LOAD_GLOBAL_BUILTIN | 746,920 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 4,508,760 | 31.1% |
| LOAD_FAST | 3,749,860 | 25.9% |
| LOAD_ATTR_MODULE | 2,246,820 | 15.5% |
| LOAD_FAST_LOAD_FAST | 750,200 | 5.2% |
| CONTAINS_OP | 750,160 | 5.2% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 250,240 | 100.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 250,200 | 100.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 11,727,140 | 54.4% |
| LOAD_ATTR_PROPERTY | 2,739,060 | 12.7% |
| FOR_ITER_GEN | 1,253,400 | 5.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 1,098,980 | 5.1% |
| CACHE | 997,960 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,814,320 | 59.4% |
| LOAD_GLOBAL_BUILTIN | 2,248,480 | 10.4% |
| LOAD_GLOBAL_MODULE | 1,498,280 | 6.9% |
| POP_TOP | 1,253,440 | 5.8% |
| NOP | 1,249,300 | 5.8% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,243,660 | 45.4% |
| LOAD_FAST_LOAD_FAST | 747,160 | 27.3% |
| LOAD_DEREF | 496,680 | 18.1% |
| SWAP | 248,300 | 9.1% |
| STORE_ATTR | 860 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 994,380 | 36.3% |
| RETURN_CONST | 496,980 | 18.2% |
| LOAD_FAST_LOAD_FAST | 249,400 | 9.1% |
| LOAD_GLOBAL_BUILTIN | 248,900 | 9.1% |
| JUMP_FORWARD | 248,700 | 9.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,255,600 | 78.6% |
| LOAD_FAST_LOAD_FAST | 2,250,020 | 21.4% |
| STORE_ATTR | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,753,020 | 35.7% |
| LOAD_CONST | 2,001,120 | 19.0% |
| RETURN_CONST | 1,501,000 | 14.3% |
| LOAD_FAST_LOAD_FAST | 1,250,200 | 11.9% |
| BUILD_LIST | 1,000,520 | 9.5% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 46.2% |
| LOAD_FAST | 60 | 23.1% |
| STORE_SUBSCR | 40 | 15.4% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 15.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160 | 61.5% |
| JUMP_FORWARD | 40 | 15.4% |
| LOAD_GLOBAL_MODULE | 40 | 15.4% |
| NOP | 20 | 7.7% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,753,360 | 30.8% |
| LOAD_FAST | 1,744,840 | 19.5% |
| LOAD_ATTR_SLOT | 1,740,120 | 19.5% |
| COPY | 1,193,920 | 13.4% |
| CALL_ISINSTANCE | 999,400 | 11.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 7,737,560 | 86.6% |
| POP_JUMP_IF_TRUE | 1,192,400 | 13.4% |
| TO_BOOL_INT | 1,120 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 752,020 | 70.9% |
| COPY | 307,400 | 29.0% |
| TO_BOOL_BOOL | 1,120 | 0.1% |
| TO_BOOL | 160 | 0.0% |
| CALL_BUILTIN_O | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 750,600 | 70.8% |
| POP_JUMP_IF_TRUE | 309,020 | 29.1% |
| TO_BOOL_BOOL | 1,120 | 0.1% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 248,460 | 100.0% |
| TO_BOOL | 20 | 0.0% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 248,460 | 100.0% |
| POP_JUMP_IF_FALSE | 20 | 0.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 360 | 75.0% |
| TO_BOOL | 60 | 12.5% |
| LOAD_FAST | 60 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 280 | 58.3% |
| POP_JUMP_IF_FALSE | 200 | 41.7% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 248,460 | 99.9% |
| STORE_FAST_LOAD_FAST | 280 | 0.1% |
| COPY | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 248,740 | 100.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,503,600 | 100.0% |
| UNPACK_SEQUENCE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,503,640 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 500,400 | 66.7% |
| RETURN_VALUE | 250,200 | 33.3% |
| UNPACK_SEQUENCE | 80 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 40 | 0.0% |
| FOR_ITER | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 750,660 | 100.0% |
| STORE_FAST_STORE_FAST | 80 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,750,840 | 43.7% |
| YIELD_VALUE | 1,253,400 | 31.3% |
| STORE_ATTR_SLOT | 500,400 | 12.5% |
| FOR_ITER | 249,840 | 6.2% |
| CALL_BUILTIN_O | 248,280 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 3,502,780 | 87.5% |
| LOAD_FAST | 500,440 | 12.5% |


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
|     deferred | 4,106,200 | 27.1% |
|          hit | 11,019,300 | 72.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 980 | 20.2% |
| Failure | 3,880 | 79.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 1,780 | 45.9% |
| lshift | 600 | 15.5% |
| floor divide | 460 | 11.9% |
| remainder | 320 | 8.2% |
| true divide other | 320 | 8.2% |
| rshift | 260 | 6.7% |
| or | 140 | 3.6% |


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
|     deferred | 1,000,820 | 30.7% |
|          hit | 2,253,740 | 69.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 220 | 24.4% |
| Failure | 680 | 75.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 360 | 52.9% |
| buffer int | 320 | 47.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 4,758,640 | 11.5% |
|          hit | 36,647,460 | 88.5% |
|         miss | 220 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,680 | 44.2% |
| Failure | 3,380 | 55.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 1,620 | 47.9% |
| no dict | 780 | 23.1% |
| class no vectorcall | 340 | 10.1% |
| code complex parameters | 280 | 8.3% |
| meth descr method fastcall keywords | 260 | 7.7% |
| cfunc noargs | 60 | 1.8% |
| other | 40 | 1.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,200,980 | 57.3% |
|          hit | 6,100,960 | 42.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 660 | 12.7% |
| Failure | 4,540 | 87.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 3,320 | 73.1% |
| different types | 1,220 | 26.9% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,999,600 | 59.9% |
|          hit | 2,009,920 | 40.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 7.8% |
| Failure | 1,880 | 92.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 500 | 26.6% |
| enumerate | 320 | 17.0% |
| dict values | 260 | 13.8% |
| reversed list | 260 | 13.8% |
| callable | 260 | 13.8% |
| map | 200 | 10.6% |
| itertools | 60 | 3.2% |
| set | 20 | 1.1% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,005,760 | 1.9% |
|          hit | 51,800,440 | 98.1% |
|         miss | 140 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,600 | 76.6% |
| Failure | 1,100 | 23.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 580 | 52.7% |
| non overriding descriptor | 260 | 23.6% |
| not managed dict | 260 | 23.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,440 | 0.0% |
|          hit | 25,244,100 | 100.0% |
|         miss | 20 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,480 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 40 | 0.0% |
|          hit | 250,260 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 20 | 100.0% |
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
|     deferred | 2,900 | 0.0% |
|          hit | 13,243,440 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,020 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 120 | 27.3% |
|          hit | 260 | 59.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 40 | 66.7% |
| Failure | 20 | 33.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 20 | 100.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,998,680 | 16.0% |
|          hit | 10,370,400 | 83.0% |
|         miss | 119,160 | 1.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,020 | 67.4% |
| Failure | 1,460 | 32.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 1,040 | 71.2% |
| sequence | 260 | 17.8% |
| tuple | 160 | 11.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 560 | 0.0% |
|          hit | 6,257,600 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 271,782,480 | 51.9% |
| Not specialized | 66,791,320 | 12.7% |
| Specialized hits | 185,410,180 | 35.4% |
| Specialized misses | 119,540 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| COMPARE_OP | 8,200,980 | 34.1% |
| CALL | 4,758,640 | 19.8% |
| BINARY_OP | 4,106,200 | 17.1% |
| FOR_ITER | 2,999,600 | 12.5% |
| TO_BOOL | 1,998,680 | 8.3% |
| LOAD_ATTR | 1,005,760 | 4.2% |
| BINARY_SUBSCR | 1,000,820 | 4.2% |
| LOAD_GLOBAL | 3,440 | 0.0% |
| STORE_ATTR | 2,900 | 0.0% |
| UNPACK_SEQUENCE | 560 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| TO_BOOL_INT | 59,760 | 50.0% |
| TO_BOOL_BOOL | 59,360 | 49.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 140 | 0.1% |
| LOAD_ATTR_MODULE | 140 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.1% |
| TO_BOOL_NONE | 40 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 20 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.0% |
| CACHE | 0 | 0.0% |
| BEFORE_WITH | 0 | 0.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,498,160 | 6.9% |
| Calls to Python functions inlined | 20,313,740 | 93.1% |
| Calls via PyEval_EvalFrame (total) | 1,498,160 | 6.9% |
| Calls via PyEval_EvalFrame (vector) | 1,498,060 | 6.9% |
| Calls via PyEval_EvalFrame (generator) | 100 | 0.0% |
| Calls via PyEval_EvalFrame (legacy) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 1,497,980 | 6.9% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 249,480 | 1.1% |
| Calls via PyEval_EvalFrame (function ex) | 100 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 540 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 996,500 | 4.6% |
| Frames pushed | 18,057,960 | 82.8% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 17,753,840 | 30.3% |
| Frees to freelist | 17,753,660 |  |
| Allocations | 40,841,024 | 69.7% |
| Allocations to 512 bytes | 40,076,744 | 68.4% |
| Allocations to 4 kbytes | 263,480 | 0.4% |
| Allocations over 4 kbytes | 500,800 | 0.9% |
| Frees | 41,526,651 |  |
| New values | 248,700 |  |
| Interpreter increfs | 238,595,560 | 85.0% |
| Interpreter decrefs | 267,787,440 | 78.6% |
| Increfs | 42,238,146 | 15.0% |
| Decrefs | 72,968,987 | 21.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 2,759,759 |  |
| Method cache misses | 254,261 |  |
| Method cache collisions | 430,988 |  |
| Method cache dunder hits | 2,820,732 |  |
| Method cache dunder misses | 180,588 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
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
