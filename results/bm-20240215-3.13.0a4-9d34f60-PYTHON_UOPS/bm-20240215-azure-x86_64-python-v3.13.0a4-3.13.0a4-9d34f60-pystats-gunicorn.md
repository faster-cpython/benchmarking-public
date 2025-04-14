
# Pystats results

- benchmark: gunicorn
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 38,505,051 | 19.1% | 19.1% |  |
| LOAD_CONST | 11,297,060 | 5.6% | 24.7% |  |
| RESUME_CHECK | 10,197,446 | 5.1% | 29.8% |  |
| STORE_FAST | 8,562,380 | 4.3% | 34.0% |  |
| POP_JUMP_IF_FALSE | 7,265,746 | 3.6% | 37.6% |  |
| LOAD_ATTR_INSTANCE_VALUE | 6,971,820 | 3.5% | 41.1% | 0.0% |
| LOAD_GLOBAL_MODULE | 6,349,660 | 3.2% | 44.3% | 0.0% |
| LOAD_FAST_LOAD_FAST | 6,139,920 | 3.0% | 47.3% |  |
| RETURN_VALUE | 5,952,566 | 3.0% | 50.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,781,393 | 2.9% | 53.1% | 0.3% |
| LOAD_GLOBAL_BUILTIN | 5,774,620 | 2.9% | 56.0% | 0.0% |
| POP_TOP | 5,237,026 | 2.6% | 58.6% |  |
| TO_BOOL_BOOL | 4,472,606 | 2.2% | 60.8% |  |
| CALL_PY_EXACT_ARGS | 4,123,340 | 2.0% | 62.9% | 0.4% |
| POP_JUMP_IF_TRUE | 4,069,240 | 2.0% | 64.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 3,949,720 | 2.0% | 66.8% | 0.3% |
| RETURN_CONST | 3,574,800 | 1.8% | 68.6% |  |
| CALL | 3,530,893 | 1.8% | 70.4% |  |
| INTERPRETER_EXIT | 2,946,006 | 1.5% | 71.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,782,980 | 1.4% | 73.2% | 0.6% |
| LOAD_ATTR | 2,743,398 | 1.4% | 74.6% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,959,986 | 1.0% | 75.6% | 5.6% |
| CALL_ISINSTANCE | 1,709,240 | 0.8% | 76.4% |  |
| GET_ITER | 1,618,620 | 0.8% | 77.2% |  |
| STORE_FAST_STORE_FAST | 1,604,560 | 0.8% | 78.0% |  |
| ENTER_EXECUTOR | 1,586,680 | 0.8% | 78.8% |  |
| BUILD_TUPLE | 1,321,540 | 0.7% | 79.4% |  |
| NOP | 1,291,413 | 0.6% | 80.1% |  |
| TO_BOOL_STR | 1,172,920 | 0.6% | 80.7% | 6.6% |
| POP_JUMP_IF_NOT_NONE | 1,157,940 | 0.6% | 81.2% |  |
| COMPARE_OP_INT | 1,137,200 | 0.6% | 81.8% |  |
| PUSH_NULL | 1,128,020 | 0.6% | 82.4% |  |
| FOR_ITER_LIST | 1,063,500 | 0.5% | 82.9% | 4.6% |
| TO_BOOL_NONE | 1,061,780 | 0.5% | 83.4% | 9.0% |
| SWAP | 1,045,600 | 0.5% | 83.9% |  |
| COPY | 1,024,480 | 0.5% | 84.5% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 983,140 | 0.5% | 84.9% |  |
| CALL_PY_WITH_DEFAULTS | 961,660 | 0.5% | 85.4% |  |
| JUMP_FORWARD | 870,540 | 0.4% | 85.9% |  |
| CALL_BUILTIN_FAST | 809,340 | 0.4% | 86.3% |  |
| CALL_METHOD_DESCRIPTOR_O | 779,200 | 0.4% | 86.6% | 4.0% |
| BUILD_LIST | 768,620 | 0.4% | 87.0% |  |
| CONTAINS_OP | 749,840 | 0.4% | 87.4% |  |
| TO_BOOL | 745,320 | 0.4% | 87.8% |  |
| LOAD_ATTR_MODULE | 728,220 | 0.4% | 88.1% | 0.0% |
| FOR_ITER_GEN | 725,580 | 0.4% | 88.5% | 13.2% |
| STORE_ATTR | 716,400 | 0.4% | 88.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 708,000 | 0.4% | 89.2% | 2.9% |
| CALL_LEN | 707,020 | 0.4% | 89.5% |  |
| POP_JUMP_IF_NONE | 701,480 | 0.3% | 89.9% |  |
| YIELD_VALUE | 696,360 | 0.3% | 90.2% |  |
| CALL_KW | 686,360 | 0.3% | 90.6% |  |
| CALL_FUNCTION_EX | 686,320 | 0.3% | 90.9% |  |
| LOAD_DEREF | 655,800 | 0.3% | 91.2% |  |
| BUILD_MAP | 655,440 | 0.3% | 91.6% |  |
| JUMP_BACKWARD | 624,500 | 0.3% | 91.9% |  |
| UNPACK_SEQUENCE_TUPLE | 614,160 | 0.3% | 92.2% |  |
| COPY_FREE_VARS | 594,120 | 0.3% | 92.5% |  |
| CALL_BUILTIN_CLASS | 593,680 | 0.3% | 92.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 589,980 | 0.3% | 93.1% |  |
| COMPARE_OP_STR | 574,060 | 0.3% | 93.4% | 1.8% |
| BINARY_SUBSCR_TUPLE_INT | 552,940 | 0.3% | 93.6% |  |
| FOR_ITER_TUPLE | 494,020 | 0.2% | 93.9% |  |
| FOR_ITER | 468,320 | 0.2% | 94.1% |  |
| CALL_LIST_APPEND | 440,300 | 0.2% | 94.3% |  |
| STORE_SUBSCR | 421,840 | 0.2% | 94.5% |  |
| EXTENDED_ARG | 410,280 | 0.2% | 94.7% |  |
| BINARY_SUBSCR_DICT | 409,920 | 0.2% | 94.9% | 4.9% |
| IS_OP | 400,460 | 0.2% | 95.1% |  |
| BINARY_SLICE | 400,340 | 0.2% | 95.3% |  |
| BINARY_SUBSCR_GETITEM | 389,420 | 0.2% | 95.5% | 5.7% |
| TO_BOOL_ALWAYS_TRUE | 388,960 | 0.2% | 95.7% | 5.6% |
| RETURN_GENERATOR | 378,920 | 0.2% | 95.9% |  |
| BINARY_OP_ADD_UNICODE | 348,720 | 0.2% | 96.1% |  |
| BEFORE_WITH | 317,800 | 0.2% | 96.2% |  |
| POP_EXCEPT | 317,520 | 0.2% | 96.4% |  |
| PUSH_EXC_INFO | 317,520 | 0.2% | 96.6% |  |
| LOAD_ATTR_PROPERTY | 317,100 | 0.2% | 96.7% |  |
| DICT_MERGE | 307,280 | 0.2% | 96.9% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 306,340 | 0.2% | 97.0% | 9.5% |
| BINARY_OP | 299,780 | 0.1% | 97.2% |  |
| LOAD_ATTR_SLOT | 297,160 | 0.1% | 97.3% |  |
| CHECK_EXC_MATCH | 297,040 | 0.1% | 97.5% |  |
| BINARY_SUBSCR | 258,340 | 0.1% | 97.6% |  |
| BINARY_OP_ADD_INT | 256,760 | 0.1% | 97.7% |  |
| COMPARE_OP | 252,000 | 0.1% | 97.8% |  |
| MAKE_FUNCTION | 235,880 | 0.1% | 98.0% |  |
| LOAD_FAST_AND_CLEAR | 235,740 | 0.1% | 98.1% |  |
| TO_BOOL_INT | 235,420 | 0.1% | 98.2% |  |
| LOAD_SUPER_ATTR_METHOD | 204,620 | 0.1% | 98.3% |  |
| TO_BOOL_LIST | 204,580 | 0.1% | 98.4% |  |
| END_FOR | 185,860 | 0.1% | 98.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 164,480 | 0.1% | 98.6% | 19.1% |
| STORE_ATTR_SLOT | 153,440 | 0.1% | 98.7% |  |
| BINARY_SUBSCR_LIST_INT | 143,760 | 0.1% | 98.7% |  |
| EXIT_INIT_CHECK | 143,200 | 0.1% | 98.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 143,200 | 0.1% | 98.9% |  |
| STORE_SUBSCR_DICT | 133,540 | 0.1% | 98.9% |  |
| CALL_BUILTIN_O | 123,100 | 0.1% | 99.0% |  |
| UNPACK_SEQUENCE | 114,580 | 0.1% | 99.0% |  |
| FOR_ITER_RANGE | 113,620 | 0.1% | 99.1% |  |
| RERAISE | 112,640 | 0.1% | 99.2% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 112,420 | 0.1% | 99.2% |  |
| FORMAT_SIMPLE | 92,320 | 0.0% | 99.3% |  |
| DELETE_ATTR | 92,160 | 0.0% | 99.3% |  |
| RAISE_VARARGS | 92,160 | 0.0% | 99.4% |  |
| LIST_APPEND | 82,140 | 0.0% | 99.4% |  |
| BUILD_CONST_KEY_MAP | 81,960 | 0.0% | 99.4% |  |
| STORE_FAST_LOAD_FAST | 61,680 | 0.0% | 99.5% |  |
| LOAD_FAST_CHECK | 61,560 | 0.0% | 99.5% |  |
| CALL_STR_1 | 61,440 | 0.0% | 99.5% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 52,000 | 0.0% | 99.6% | 98.1% |
| BINARY_OP_SUBTRACT_INT | 51,740 | 0.0% | 99.6% |  |
| BUILD_STRING | 51,360 | 0.0% | 99.6% |  |
| CALL_INTRINSIC_1 | 51,300 | 0.0% | 99.6% |  |
| LIST_EXTEND | 51,300 | 0.0% | 99.7% |  |
| MAKE_CELL | 51,240 | 0.0% | 99.7% |  |
| CONVERT_VALUE | 51,200 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_ATTR | 51,180 | 0.0% | 99.7% |  |
| STORE_SUBSCR_LIST_INT | 51,180 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 41,260 | 0.0% | 99.8% | 0.1% |
| CALL_TYPE_1 | 40,960 | 0.0% | 99.8% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 40,880 | 0.0% | 99.8% |  |
| IMPORT_FROM | 30,720 | 0.0% | 99.8% |  |
| MAP_ADD | 30,720 | 0.0% | 99.8% |  |
| LOAD_GLOBAL | 21,580 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_LIST | 20,680 | 0.0% | 99.9% |  |
| IMPORT_NAME | 20,540 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 20,520 | 0.0% | 99.9% |  |
| UNARY_NOT | 20,480 | 0.0% | 99.9% |  |
| WITH_EXCEPT_START | 20,480 | 0.0% | 99.9% |  |
| BUILD_SET | 20,480 | 0.0% | 99.9% |  |
| LOAD_ATTR_CLASS | 20,460 | 0.0% | 99.9% |  |
| SEND_GEN | 20,460 | 0.0% | 99.9% |  |
| BINARY_OP_SUBTRACT_FLOAT | 20,440 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 10,500 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 10,340 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 10,260 | 0.0% | 100.0% |  |
| END_SEND | 10,240 | 0.0% | 100.0% |  |
| GET_YIELD_FROM_ITER | 10,240 | 0.0% | 100.0% |  |
| BUILD_SLICE | 10,240 | 0.0% | 100.0% |  |
| SET_ADD | 10,240 | 0.0% | 100.0% |  |
| SET_UPDATE | 10,240 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 10,220 | 0.0% | 100.0% | 0.6% |
| RESUME | 6,440 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| STORE_NAME | 500 | 0.0% | 100.0% |  |
| LOAD_NAME | 100 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| SEND | 40 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,424,340 | 3.2% | 3.2% |
| RESUME_CHECK LOAD_FAST | 5,241,766 | 2.6% | 5.8% |
| STORE_FAST LOAD_FAST | 5,228,260 | 2.6% | 8.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,593,760 | 1.8% | 10.2% |
| POP_JUMP_IF_FALSE LOAD_FAST | 3,566,433 | 1.8% | 11.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 3,535,480 | 1.8% | 13.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 3,514,840 | 1.7% | 15.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 3,009,006 | 1.5% | 16.9% |
| CACHE RESUME_CHECK | 2,555,686 | 1.3% | 18.2% |
| LOAD_FAST LOAD_CONST | 2,492,960 | 1.2% | 19.4% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,267,800 | 1.1% | 20.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,114,760 | 1.0% | 21.6% |
| LOAD_FAST LOAD_ATTR | 2,069,498 | 1.0% | 22.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 1,854,220 | 0.9% | 23.6% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 1,715,820 | 0.9% | 24.4% |
| LOAD_CONST LOAD_FAST | 1,701,060 | 0.8% | 25.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,657,900 | 0.8% | 26.1% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 1,627,740 | 0.8% | 26.9% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,626,740 | 0.8% | 27.7% |
| RETURN_CONST POP_TOP | 1,587,560 | 0.8% | 28.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 1,584,780 | 0.8% | 29.3% |
| POP_TOP LOAD_FAST | 1,475,026 | 0.7% | 30.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,472,000 | 0.7% | 30.7% |
| RETURN_VALUE INTERPRETER_EXIT | 1,465,706 | 0.7% | 31.5% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,432,920 | 0.7% | 32.2% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,411,340 | 0.7% | 32.9% |
| RETURN_VALUE STORE_FAST | 1,382,940 | 0.7% | 33.6% |
| LOAD_FAST RETURN_VALUE | 1,352,140 | 0.7% | 34.2% |
| LOAD_CONST LOAD_CONST | 1,292,400 | 0.6% | 34.9% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,279,480 | 0.6% | 35.5% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,251,193 | 0.6% | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,248,920 | 0.6% | 36.8% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,238,800 | 0.6% | 37.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 1,176,860 | 0.6% | 38.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,157,260 | 0.6% | 38.5% |
| RETURN_CONST INTERPRETER_EXIT | 1,156,260 | 0.6% | 39.1% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 1,042,580 | 0.5% | 39.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 982,820 | 0.5% | 40.1% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 972,140 | 0.5% | 40.6% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 972,140 | 0.5% | 41.1% |
| LOAD_FAST LOAD_FAST | 962,700 | 0.5% | 41.6% |
| LOAD_FAST TO_BOOL_STR | 957,740 | 0.5% | 42.0% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 951,440 | 0.5% | 42.5% |
| LOAD_CONST CALL | 936,040 | 0.5% | 43.0% |
| LOAD_FAST TO_BOOL_BOOL | 900,100 | 0.4% | 43.4% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 870,860 | 0.4% | 43.8% |
| POP_TOP RETURN_CONST | 870,780 | 0.4% | 44.3% |
| STORE_FAST LOAD_GLOBAL_MODULE | 869,580 | 0.4% | 44.7% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 859,380 | 0.4% | 45.1% |
| LOAD_FAST CALL | 856,953 | 0.4% | 45.6% |
| POP_JUMP_IF_FALSE RETURN_CONST | 788,840 | 0.4% | 46.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 788,620 | 0.4% | 46.3% |
| PUSH_NULL LOAD_FAST | 768,660 | 0.4% | 46.7% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 768,460 | 0.4% | 47.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 757,000 | 0.4% | 47.5% |
| LOAD_CONST COMPARE_OP_INT | 736,460 | 0.4% | 47.8% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 717,720 | 0.4% | 48.2% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 695,840 | 0.3% | 48.5% |
| CALL STORE_FAST | 687,880 | 0.3% | 48.9% |
| RESUME_CHECK POP_TOP | 685,880 | 0.3% | 49.2% |
| NOP LOAD_FAST | 676,433 | 0.3% | 49.6% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 675,980 | 0.3% | 49.9% |
| POP_JUMP_IF_FALSE LOAD_CONST | 665,860 | 0.3% | 50.2% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 665,780 | 0.3% | 50.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 657,500 | 0.3% | 50.9% |
| RETURN_VALUE RETURN_VALUE | 645,200 | 0.3% | 51.2% |
| STORE_FAST_STORE_FAST STORE_FAST | 634,960 | 0.3% | 51.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 623,940 | 0.3% | 51.8% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 613,440 | 0.3% | 52.1% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 612,380 | 0.3% | 52.4% |
| LOAD_CONST STORE_FAST | 604,620 | 0.3% | 52.7% |
| LOAD_CONST CALL_KW | 584,280 | 0.3% | 53.0% |
| COPY_FREE_VARS RESUME_CHECK | 583,520 | 0.3% | 53.3% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 583,180 | 0.3% | 53.6% |
| LOAD_FAST COPY | 573,760 | 0.3% | 53.9% |
| POP_TOP ENTER_EXECUTOR | 559,340 | 0.3% | 54.2% |
| LOAD_FAST POP_JUMP_IF_NONE | 557,980 | 0.3% | 54.5% |
| RETURN_VALUE LOAD_FAST | 552,940 | 0.3% | 54.7% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 543,520 | 0.3% | 55.0% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 543,440 | 0.3% | 55.3% |
| CALL RETURN_VALUE | 543,233 | 0.3% | 55.5% |
| RESUME_CHECK NOP | 542,580 | 0.3% | 55.8% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 538,820 | 0.3% | 56.1% |
| LOAD_ATTR LOAD_FAST | 536,000 | 0.3% | 56.3% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 532,260 | 0.3% | 56.6% |
| LOAD_FAST TO_BOOL_NONE | 526,320 | 0.3% | 56.9% |
| JUMP_FORWARD LOAD_FAST | 522,260 | 0.3% | 57.1% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 521,880 | 0.3% | 57.4% |
| CALL TO_BOOL_BOOL | 501,160 | 0.2% | 57.6% |
| LOAD_FAST GET_ITER | 491,900 | 0.2% | 57.9% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 491,300 | 0.2% | 58.1% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 490,860 | 0.2% | 58.4% |
| LOAD_FAST TO_BOOL | 486,440 | 0.2% | 58.6% |
| GET_ITER FOR_ITER_LIST | 479,860 | 0.2% | 58.8% |
| JUMP_BACKWARD FOR_ITER_GEN | 477,160 | 0.2% | 59.1% |
| BUILD_MAP LOAD_FAST | 471,100 | 0.2% | 59.3% |
| LOAD_CONST BINARY_SUBSCR_TUPLE_INT | 470,920 | 0.2% | 59.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 460,980 | 0.2% | 59.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 459,980 | 0.2% | 60.0% |
| CALL POP_TOP | 451,980 | 0.2% | 60.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 307,740 | 76.9% |
| LOAD_FAST | 51,360 | 12.8% |
| BINARY_OP_ADD_INT | 41,220 | 10.3% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 163,920 | 40.9% |
| STORE_FAST | 82,240 | 20.5% |
| CALL_METHOD_DESCRIPTOR_O | 61,600 | 15.4% |
| LOAD_ATTR_METHOD_NO_DICT | 40,840 | 10.2% |
| LOAD_CONST | 20,520 | 5.1% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,555,686 | 86.4% |
| POP_TOP | 165,060 | 5.6% |
| COPY_FREE_VARS | 153,660 | 5.2% |
| RETURN_GENERATOR | 81,920 | 2.8% |
| RESUME | 1,800 | 0.1% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 276,560 | 87.0% |
| RETURN_VALUE | 40,980 | 12.9% |
| LOAD_ATTR | 120 | 0.0% |
| CALL | 100 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 307,540 | 96.8% |
| STORE_FAST | 10,260 | 3.2% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,400 | 49.9% |
| BUILD_STRING | 10,200 | 25.0% |
| LOAD_FAST_LOAD_FAST | 10,200 | 25.0% |
| BINARY_OP | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,660 | 75.0% |
| LOAD_FAST_LOAD_FAST | 10,220 | 25.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 184,320 | 71.3% |
| LOAD_CONST | 52,080 | 20.2% |
| BINARY_SUBSCR | 11,320 | 4.4% |
| BUILD_TUPLE | 10,240 | 4.0% |
| LOAD_FAST | 260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 194,580 | 75.3% |
| CALL_LEN | 20,440 | 7.9% |
| BINARY_SUBSCR | 11,320 | 4.4% |
| PUSH_EXC_INFO | 10,280 | 4.0% |
| LOAD_FAST | 10,240 | 4.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 255,980 | 86.2% |
| BUILD_TUPLE | 30,720 | 10.3% |
| LOAD_ATTR_MODULE | 10,220 | 3.4% |
| LOAD_GLOBAL | 100 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 297,040 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 10,240 | 99.8% |
| LOAD_FAST | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 99.8% |
| LOAD_GLOBAL_MODULE | 20 | 0.2% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 185,860 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 185,860 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,240 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 143,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 143,200 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 51,200 | 55.5% |
| LOAD_FAST | 30,880 | 33.4% |
| LOAD_GLOBAL_MODULE | 10,220 | 11.1% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 51,360 | 55.6% |
| LOAD_CONST | 40,960 | 44.4% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 491,900 | 30.4% |
| CALL_BUILTIN_CLASS | 255,880 | 15.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 229,100 | 14.2% |
| LOAD_ATTR_INSTANCE_VALUE | 184,220 | 11.4% |
| BINARY_SLICE | 163,920 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 479,860 | 29.6% |
| FOR_ITER | 335,660 | 20.7% |
| LOAD_FAST_AND_CLEAR | 194,780 | 12.0% |
| FOR_ITER_TUPLE | 184,340 | 11.4% |
| FOR_ITER_GEN | 167,960 | 10.4% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,465,706 | 49.8% |
| RETURN_CONST | 1,156,260 | 39.2% |
| YIELD_VALUE | 242,120 | 8.2% |
| RETURN_GENERATOR | 81,920 | 2.8% |


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
| LOAD_CONST | 235,880 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 194,560 | 82.5% |
| SET_FUNCTION_ATTRIBUTE | 10,340 | 4.4% |
| LOAD_CONST | 10,300 | 4.4% |
| STORE_FAST | 10,240 | 4.3% |
| LOAD_GLOBAL_MODULE | 10,200 | 4.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 542,580 | 42.0% |
| STORE_FAST | 164,060 | 12.7% |
| POP_JUMP_IF_FALSE | 143,453 | 11.1% |
| POP_JUMP_IF_TRUE | 123,200 | 9.5% |
| POP_TOP | 92,380 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 676,433 | 52.4% |
| LOAD_FAST_LOAD_FAST | 184,360 | 14.3% |
| LOAD_GLOBAL_MODULE | 174,000 | 13.5% |
| LOAD_GLOBAL_BUILTIN | 153,200 | 11.9% |
| NOP | 51,220 | 4.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 112,660 | 35.5% |
| SWAP | 92,180 | 29.0% |
| COPY | 92,160 | 29.0% |
| STORE_FAST | 10,280 | 3.2% |
| POP_JUMP_IF_FALSE | 10,240 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 112,640 | 35.5% |
| RETURN_VALUE | 92,180 | 29.0% |
| RERAISE | 92,160 | 29.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 10,280 | 3.2% |
| LOAD_FAST | 10,260 | 3.2% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,587,560 | 30.3% |
| RESUME_CHECK | 685,880 | 13.1% |
| CALL | 451,980 | 8.6% |
| POP_JUMP_IF_FALSE | 348,240 | 6.6% |
| BEFORE_WITH | 307,540 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,475,026 | 28.2% |
| RETURN_CONST | 870,780 | 16.6% |
| ENTER_EXECUTOR | 559,340 | 10.7% |
| LOAD_CONST | 440,580 | 8.4% |
| RESUME_CHECK | 368,360 | 7.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 112,040 | 35.3% |
| RERAISE | 90,900 | 28.6% |
| CALL_BUILTIN_FAST | 30,700 | 9.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20,480 | 6.4% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 20,440 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 286,540 | 90.2% |
| WITH_EXCEPT_START | 20,480 | 6.4% |
| LOAD_GLOBAL_MODULE | 10,200 | 3.2% |
| LOAD_GLOBAL | 300 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 420,680 | 37.3% |
| LOAD_ATTR_MODULE | 307,520 | 27.3% |
| LOAD_FAST | 307,400 | 27.3% |
| LOAD_SUPER_ATTR_ATTR | 51,180 | 4.5% |
| BINARY_SUBSCR_DICT | 20,480 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 768,660 | 68.1% |
| CALL | 133,880 | 11.9% |
| LOAD_FAST_LOAD_FAST | 71,820 | 6.4% |
| LOAD_CONST | 71,780 | 6.4% |
| LOAD_GLOBAL_MODULE | 61,320 | 5.4% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 235,360 | 62.1% |
| CACHE | 81,920 | 21.6% |
| CALL_FUNCTION_EX | 30,720 | 8.1% |
| COPY_FREE_VARS | 10,280 | 2.7% |
| CALL_KW | 10,240 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 112,640 | 29.7% |
| INTERPRETER_EXIT | 81,920 | 21.6% |
| CALL_BUILTIN_O | 51,160 | 13.5% |
| STORE_FAST | 40,960 | 10.8% |
| LOAD_FAST | 30,720 | 8.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,352,140 | 22.7% |
| RETURN_VALUE | 645,200 | 10.8% |
| CALL | 543,233 | 9.1% |
| CALL_FUNCTION_EX | 337,960 | 5.7% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 337,840 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,465,706 | 24.6% |
| STORE_FAST | 1,382,940 | 23.2% |
| RETURN_VALUE | 645,200 | 10.8% |
| LOAD_FAST | 552,940 | 9.3% |
| BUILD_TUPLE | 204,780 | 3.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 204,800 | 48.5% |
| LOAD_FAST | 92,360 | 21.9% |
| LOAD_FAST_LOAD_FAST | 82,000 | 19.4% |
| RETURN_VALUE | 40,960 | 9.7% |
| STORE_SUBSCR | 1,360 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 204,800 | 48.5% |
| JUMP_BACKWARD | 123,280 | 29.2% |
| ENTER_EXECUTOR | 50,980 | 12.1% |
| LOAD_FAST | 20,560 | 4.9% |
| LOAD_CONST | 10,320 | 2.4% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 486,440 | 65.3% |
| LOAD_ATTR_INSTANCE_VALUE | 123,620 | 16.6% |
| COPY | 62,560 | 8.4% |
| LOAD_ATTR | 22,140 | 3.0% |
| LOAD_FAST_CHECK | 20,520 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 423,960 | 56.9% |
| POP_JUMP_IF_TRUE | 309,740 | 41.6% |
| TO_BOOL | 4,880 | 0.7% |
| TO_BOOL_BOOL | 3,660 | 0.5% |
| TO_BOOL_NONE | 1,160 | 0.2% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 20,440 | 99.8% |
| TO_BOOL | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 10,240 | 50.0% |
| STORE_FAST | 10,240 | 50.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 20,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 20,400 | 99.6% |
| TO_BOOL | 80 | 0.4% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 143,400 | 47.8% |
| LOAD_FAST | 61,780 | 20.6% |
| LOAD_CONST | 51,860 | 17.3% |
| LOAD_FAST_LOAD_FAST | 41,360 | 13.8% |
| BINARY_OP | 1,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 143,420 | 47.8% |
| STORE_FAST | 92,660 | 30.9% |
| LOAD_FAST | 51,320 | 17.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 10,200 | 3.4% |
| BINARY_OP | 1,000 | 0.3% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 81,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,200 | 62.5% |
| RETURN_VALUE | 10,260 | 12.5% |
| STORE_FAST | 10,260 | 12.5% |
| CALL | 10,240 | 12.5% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 153,820 | 20.0% |
| RESUME_CHECK | 102,280 | 13.3% |
| LOAD_FAST | 92,260 | 12.0% |
| LOAD_CONST | 92,180 | 12.0% |
| STORE_ATTR_INSTANCE_VALUE | 81,860 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 307,340 | 40.0% |
| SWAP | 153,820 | 20.0% |
| LOAD_FAST | 143,440 | 18.7% |
| CALL_PY_EXACT_ARGS | 51,080 | 6.6% |
| MAP_ADD | 30,720 | 4.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 122,920 | 18.8% |
| POP_TOP | 122,880 | 18.7% |
| STORE_ATTR_INSTANCE_VALUE | 122,760 | 18.7% |
| BUILD_TUPLE | 112,640 | 17.2% |
| POP_JUMP_IF_NOT_NONE | 40,960 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 471,100 | 71.9% |
| STORE_FAST | 92,160 | 14.1% |
| SWAP | 30,720 | 4.7% |
| JUMP_FORWARD | 20,480 | 3.1% |
| CALL_PY_WITH_DEFAULTS | 20,400 | 3.1% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,240 | 50.0% |
| CALL_BUILTIN_CLASS | 10,220 | 49.9% |
| CALL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 50.0% |
| SWAP | 10,240 | 50.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 10,240 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 51,360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 10,400 | 20.2% |
| RETURN_VALUE | 10,240 | 19.9% |
| CALL | 10,240 | 19.9% |
| STORE_FAST | 10,240 | 19.9% |
| BINARY_OP_INPLACE_ADD_UNICODE | 10,200 | 19.9% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 430,200 | 32.6% |
| LOAD_FAST | 266,320 | 20.2% |
| RETURN_VALUE | 204,780 | 15.5% |
| LOAD_GLOBAL_BUILTIN | 163,680 | 12.4% |
| LOAD_GLOBAL_MODULE | 153,620 | 11.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,280 | 17.0% |
| RETURN_VALUE | 194,960 | 14.8% |
| CALL | 164,300 | 12.4% |
| YIELD_VALUE | 163,840 | 12.4% |
| BINARY_OP | 143,400 | 10.9% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 936,040 | 26.5% |
| LOAD_FAST | 856,953 | 24.3% |
| LOAD_GLOBAL_MODULE | 307,760 | 8.7% |
| LOAD_FAST_LOAD_FAST | 288,260 | 8.2% |
| LOAD_ATTR_METHOD_NO_DICT | 278,000 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 687,880 | 19.5% |
| RETURN_VALUE | 543,233 | 15.4% |
| TO_BOOL_BOOL | 501,160 | 14.2% |
| POP_TOP | 451,980 | 12.8% |
| RESUME_CHECK | 319,480 | 9.0% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 307,280 | 44.8% |
| LOAD_FAST | 286,800 | 41.8% |
| CALL_INTRINSIC_1 | 51,280 | 7.5% |
| ENTER_EXECUTOR | 30,480 | 4.4% |
| RETURN_VALUE | 10,480 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,960 | 49.2% |
| POP_TOP | 163,840 | 23.9% |
| RESUME_CHECK | 71,680 | 10.4% |
| STORE_FAST | 51,220 | 7.5% |
| RETURN_GENERATOR | 30,720 | 4.5% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 51,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 51,280 | 100.0% |
| BUILD_MAP | 20 | 0.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 584,280 | 85.1% |
| ENTER_EXECUTOR | 102,080 | 14.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 388,860 | 56.7% |
| RETURN_VALUE | 112,660 | 16.4% |
| STORE_FAST | 71,720 | 10.4% |
| LOAD_FAST | 51,200 | 7.5% |
| POP_TOP | 20,480 | 3.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,400 | 36.7% |
| LOAD_CONST | 74,320 | 29.5% |
| LOAD_GLOBAL_MODULE | 41,080 | 16.3% |
| LOAD_FAST_LOAD_FAST | 20,600 | 8.2% |
| BUILD_LIST | 10,280 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 184,900 | 73.4% |
| POP_JUMP_IF_FALSE | 62,940 | 25.0% |
| COMPARE_OP | 2,200 | 0.9% |
| COMPARE_OP_INT | 1,160 | 0.5% |
| COMPARE_OP_STR | 660 | 0.3% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 348,840 | 46.5% |
| LOAD_GLOBAL_MODULE | 174,140 | 23.2% |
| LOAD_CONST | 102,640 | 13.7% |
| LOAD_FAST_LOAD_FAST | 42,100 | 5.6% |
| LOAD_ATTR_MODULE | 40,980 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 543,520 | 72.5% |
| STORE_FAST | 61,460 | 8.2% |
| POP_JUMP_IF_TRUE | 52,700 | 7.0% |
| EXTENDED_ARG | 40,960 | 5.5% |
| COPY | 20,480 | 2.7% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,960 | 80.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 10,220 | 20.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 51,200 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 573,760 | 56.0% |
| RAISE_VARARGS | 71,680 | 7.0% |
| CALL_ISINSTANCE | 51,180 | 5.0% |
| LOAD_CONST | 41,000 | 4.0% |
| RETURN_VALUE | 40,960 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 234,940 | 22.9% |
| LOAD_ATTR_INSTANCE_VALUE | 163,960 | 16.0% |
| TO_BOOL_STR | 122,720 | 12.0% |
| TO_BOOL_BOOL | 122,640 | 12.0% |
| POP_EXCEPT | 92,160 | 9.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 348,020 | 58.6% |
| CACHE | 153,660 | 25.9% |
| CALL | 82,120 | 13.8% |
| CALL_KW | 10,240 | 1.7% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 583,520 | 98.2% |
| RETURN_GENERATOR | 10,280 | 1.7% |
| RESUME | 320 | 0.1% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,440 | 66.7% |
| NOP | 30,720 | 33.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 286,780 | 93.3% |
| BUILD_MAP | 10,240 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 10,220 | 3.3% |
| CALL | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 307,280 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 559,340 | 35.3% |
| POP_JUMP_IF_TRUE | 448,460 | 28.3% |
| POP_JUMP_IF_FALSE | 142,380 | 9.0% |
| CALL_LIST_APPEND | 142,340 | 9.0% |
| STORE_FAST | 81,520 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 311,800 | 19.7% |
| FOR_ITER_TUPLE | 245,140 | 15.4% |
| YIELD_VALUE | 193,920 | 12.2% |
| CALL_KW | 102,080 | 6.4% |
| CALL_LIST_APPEND | 101,860 | 6.4% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 122,840 | 29.9% |
| POP_JUMP_IF_TRUE | 112,640 | 27.5% |
| TO_BOOL_STR | 41,940 | 10.2% |
| CONTAINS_OP | 40,960 | 10.0% |
| GET_ITER | 30,720 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 245,760 | 59.9% |
| JUMP_FORWARD | 122,880 | 30.0% |
| FOR_ITER_LIST | 20,400 | 5.0% |
| FOR_ITER | 10,640 | 2.6% |
| POP_JUMP_IF_TRUE | 10,260 | 2.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 335,660 | 71.7% |
| LOAD_FAST | 71,840 | 15.3% |
| SWAP | 24,080 | 5.1% |
| JUMP_BACKWARD | 14,340 | 3.1% |
| EXTENDED_ARG | 10,640 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 127,260 | 27.2% |
| RETURN_CONST | 123,580 | 26.4% |
| LOAD_FAST | 103,820 | 22.2% |
| STORE_FAST | 76,320 | 16.3% |
| STORE_FAST_LOAD_FAST | 20,520 | 4.4% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 20,480 | 66.7% |
| STORE_FAST | 10,240 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 30,720 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 20,480 | 99.7% |
| STORE_NAME | 40 | 0.2% |
| STORE_FAST | 20 | 0.1% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 194,560 | 48.6% |
| LOAD_GLOBAL_MODULE | 103,320 | 25.8% |
| LOAD_FAST_LOAD_FAST | 81,920 | 20.5% |
| LOAD_FAST | 20,500 | 5.1% |
| LOAD_GLOBAL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 257,080 | 64.2% |
| RETURN_VALUE | 61,440 | 15.3% |
| COPY | 40,960 | 10.2% |
| POP_JUMP_IF_TRUE | 30,740 | 7.7% |
| STORE_FAST | 10,240 | 2.6% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 342,420 | 54.8% |
| STORE_SUBSCR | 123,280 | 19.7% |
| POP_JUMP_IF_TRUE | 106,340 | 17.0% |
| LIST_APPEND | 41,300 | 6.6% |
| POP_JUMP_IF_NONE | 6,500 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 477,160 | 76.4% |
| FOR_ITER_LIST | 127,200 | 20.4% |
| FOR_ITER | 14,340 | 2.3% |
| FOR_ITER_TUPLE | 2,780 | 0.4% |
| FOR_ITER_RANGE | 900 | 0.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 10,280 | 50.1% |
| RESUME_CHECK | 10,220 | 49.8% |
| RESUME | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 49.9% |
| SEND_GEN | 10,220 | 49.8% |
| LOAD_FAST | 40 | 0.2% |
| SEND | 20 | 0.1% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 163,900 | 18.8% |
| POP_JUMP_IF_FALSE | 153,600 | 17.6% |
| EXTENDED_ARG | 122,880 | 14.1% |
| LOAD_CONST | 81,920 | 9.4% |
| STORE_SUBSCR_LIST_INT | 51,180 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 522,260 | 60.0% |
| STORE_FAST | 163,840 | 18.8% |
| LOAD_GLOBAL_MODULE | 112,400 | 12.9% |
| LOAD_CONST | 30,720 | 3.5% |
| BUILD_MAP | 20,480 | 2.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40,960 | 49.9% |
| BUILD_TUPLE | 40,960 | 49.9% |
| CALL_METHOD_DESCRIPTOR_FAST | 220 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 41,300 | 50.3% |
| ENTER_EXECUTOR | 40,840 | 49.7% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,220 | 99.8% |
| LOAD_DEREF | 80 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 51,300 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,069,498 | 75.4% |
| LOAD_ATTR_INSTANCE_VALUE | 267,840 | 9.8% |
| LOAD_ATTR | 133,460 | 4.9% |
| LOAD_GLOBAL_MODULE | 113,880 | 4.2% |
| RETURN_VALUE | 51,400 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 536,000 | 19.5% |
| PUSH_NULL | 420,680 | 15.3% |
| LOAD_CONST | 207,320 | 7.6% |
| STORE_FAST | 195,100 | 7.1% |
| CALL_PY_EXACT_ARGS | 183,720 | 6.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,492,960 | 22.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,627,740 | 14.4% |
| LOAD_CONST | 1,292,400 | 11.4% |
| POP_JUMP_IF_FALSE | 665,860 | 5.9% |
| STORE_ATTR_INSTANCE_VALUE | 613,440 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,701,060 | 15.1% |
| LOAD_CONST | 1,292,400 | 11.4% |
| CALL | 936,040 | 8.3% |
| COMPARE_OP_INT | 736,460 | 6.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 695,840 | 6.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 276,240 | 42.1% |
| LOAD_ATTR_METHOD_NO_DICT | 235,520 | 35.9% |
| LOAD_GLOBAL_MODULE | 61,400 | 9.4% |
| STORE_FAST | 20,520 | 3.1% |
| NOP | 10,320 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 256,080 | 39.0% |
| LOAD_CONST | 245,800 | 37.5% |
| LOAD_ATTR_INSTANCE_VALUE | 51,000 | 7.8% |
| LOAD_FAST_LOAD_FAST | 30,720 | 4.7% |
| BINARY_SUBSCR_DICT | 20,480 | 3.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,241,766 | 13.6% |
| STORE_FAST | 5,228,260 | 13.6% |
| LOAD_GLOBAL_BUILTIN | 3,593,760 | 9.3% |
| POP_JUMP_IF_FALSE | 3,566,433 | 9.3% |
| POP_JUMP_IF_TRUE | 1,854,220 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 6,424,340 | 16.7% |
| LOAD_ATTR_METHOD_NO_DICT | 3,535,480 | 9.2% |
| LOAD_CONST | 2,492,960 | 6.5% |
| STORE_ATTR_INSTANCE_VALUE | 2,267,800 | 5.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,114,760 | 5.5% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 194,780 | 82.6% |
| LOAD_FAST_AND_CLEAR | 40,960 | 17.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 194,780 | 82.6% |
| LOAD_FAST_AND_CLEAR | 40,960 | 17.4% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 30,800 | 50.0% |
| LOAD_GLOBAL_BUILTIN | 20,440 | 33.2% |
| LOAD_FAST_LOAD_FAST | 10,240 | 16.6% |
| LOAD_GLOBAL | 40 | 0.1% |
| JUMP_FORWARD | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 20,520 | 33.3% |
| BUILD_TUPLE | 10,240 | 16.6% |
| LOAD_ATTR | 10,240 | 16.6% |
| CALL_BUILTIN_CLASS | 10,200 | 16.6% |
| TO_BOOL_BOOL | 10,200 | 16.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,157,260 | 18.8% |
| STORE_ATTR_INSTANCE_VALUE | 982,820 | 16.0% |
| LOAD_FAST_LOAD_FAST | 788,620 | 12.8% |
| STORE_FAST | 657,500 | 10.7% |
| RESUME_CHECK | 491,300 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,472,000 | 24.0% |
| LOAD_FAST_LOAD_FAST | 788,620 | 12.8% |
| LOAD_FAST | 543,440 | 8.9% |
| CALL_PY_EXACT_ARGS | 459,980 | 7.5% |
| BUILD_TUPLE | 430,200 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980 | 13.8% |
| STORE_FAST | 2,880 | 13.3% |
| POP_JUMP_IF_FALSE | 2,420 | 11.2% |
| RESUME_CHECK | 2,000 | 9.3% |
| RESUME | 1,920 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,740 | 31.2% |
| LOAD_FAST | 4,380 | 20.3% |
| LOAD_GLOBAL_BUILTIN | 4,200 | 19.5% |
| LOAD_ATTR | 1,580 | 7.3% |
| CALL | 1,460 | 6.8% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 60 | 60.0% |
| LOAD_CONST | 20 | 20.0% |
| STORE_NAME | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 60 | 60.0% |
| CALL | 20 | 20.0% |
| LOAD_CONST | 20 | 20.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 260 | 50.0% |
| CALL | 140 | 26.9% |
| LOAD_FAST | 40 | 7.7% |
| LOAD_FAST_LOAD_FAST | 40 | 7.7% |
| PUSH_NULL | 20 | 3.8% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 20,480 | 40.0% |
| CALL_PY_EXACT_ARGS | 10,260 | 20.0% |
| CALL_KW | 10,240 | 20.0% |
| CALL_PY_WITH_DEFAULTS | 10,220 | 19.9% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 20,480 | 40.0% |
| RESUME_CHECK | 20,480 | 40.0% |
| RETURN_GENERATOR | 10,240 | 20.0% |
| RESUME | 40 | 0.1% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 30,380 | 98.9% |
| JUMP_BACKWARD | 340 | 1.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 3,009,006 | 41.4% |
| COMPARE_OP_INT | 768,460 | 10.6% |
| TO_BOOL_NONE | 612,380 | 8.4% |
| CONTAINS_OP | 543,520 | 7.5% |
| TO_BOOL | 423,960 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,566,433 | 49.1% |
| RETURN_CONST | 788,840 | 10.9% |
| LOAD_CONST | 665,860 | 9.2% |
| LOAD_GLOBAL_MODULE | 623,940 | 8.6% |
| LOAD_GLOBAL_BUILTIN | 521,880 | 7.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 557,980 | 79.5% |
| LOAD_ATTR_INSTANCE_VALUE | 71,620 | 10.2% |
| LOAD_ATTR | 51,340 | 7.3% |
| LOAD_DEREF | 10,240 | 1.5% |
| CALL_BUILTIN_FAST | 10,220 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 379,000 | 54.0% |
| LOAD_GLOBAL_BUILTIN | 81,700 | 11.6% |
| LOAD_CONST | 71,700 | 10.2% |
| LOAD_FAST_LOAD_FAST | 61,440 | 8.8% |
| RETURN_CONST | 30,720 | 4.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 870,860 | 75.2% |
| LOAD_ATTR_INSTANCE_VALUE | 92,140 | 8.0% |
| LOAD_ATTR | 71,840 | 6.2% |
| LOAD_GLOBAL_MODULE | 61,480 | 5.3% |
| RETURN_VALUE | 30,680 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 450,940 | 38.9% |
| LOAD_GLOBAL_MODULE | 235,340 | 20.3% |
| LOAD_GLOBAL_BUILTIN | 173,840 | 15.0% |
| LOAD_FAST_LOAD_FAST | 102,400 | 8.8% |
| NOP | 51,260 | 4.4% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,432,920 | 35.2% |
| TO_BOOL_STR | 717,720 | 17.6% |
| TO_BOOL_NONE | 428,200 | 10.5% |
| TO_BOOL | 309,740 | 7.6% |
| TO_BOOL_ALWAYS_TRUE | 297,480 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,854,220 | 45.6% |
| ENTER_EXECUTOR | 448,460 | 11.0% |
| POP_TOP | 307,220 | 7.5% |
| LOAD_GLOBAL_BUILTIN | 307,140 | 7.5% |
| LOAD_GLOBAL_MODULE | 306,700 | 7.5% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,680 | 77.8% |
| LOAD_GLOBAL_BUILTIN | 10,220 | 11.1% |
| LOAD_GLOBAL_MODULE | 10,220 | 11.1% |
| LOAD_GLOBAL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 71,680 | 87.5% |
| PUSH_EXC_INFO | 10,240 | 12.5% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 92,160 | 81.8% |
| POP_JUMP_IF_TRUE | 20,480 | 18.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 90,900 | 81.6% |
| COPY | 20,480 | 18.4% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 870,780 | 24.4% |
| POP_JUMP_IF_FALSE | 788,840 | 22.1% |
| STORE_ATTR_INSTANCE_VALUE | 583,180 | 16.3% |
| CALL_LIST_APPEND | 215,000 | 6.0% |
| STORE_SUBSCR | 204,800 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,587,560 | 44.4% |
| INTERPRETER_EXIT | 1,156,260 | 32.3% |
| TO_BOOL_BOOL | 378,660 | 10.6% |
| END_FOR | 185,860 | 5.2% |
| EXIT_INIT_CHECK | 143,200 | 4.0% |


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

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 10,220 | 99.8% |
| CALL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 9,900 | 96.7% |
| JUMP_BACKWARD | 340 | 3.3% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 10,340 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,260 | 99.2% |
| STORE_NAME | 40 | 0.4% |
| LOAD_GLOBAL_MODULE | 40 | 0.4% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 10,240 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 436,180 | 60.9% |
| LOAD_FAST_LOAD_FAST | 228,380 | 31.9% |
| SWAP | 31,000 | 4.3% |
| STORE_ATTR | 10,460 | 1.5% |
| LOAD_GLOBAL_MODULE | 10,220 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 216,040 | 30.2% |
| LOAD_CONST | 144,420 | 20.2% |
| RETURN_CONST | 113,260 | 15.8% |
| LOAD_FAST_LOAD_FAST | 103,240 | 14.4% |
| LOAD_GLOBAL_MODULE | 91,800 | 12.8% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,382,940 | 16.2% |
| CALL | 687,880 | 8.0% |
| STORE_FAST_STORE_FAST | 634,960 | 7.4% |
| LOAD_CONST | 604,620 | 7.1% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 432,020 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,228,260 | 61.1% |
| LOAD_GLOBAL_MODULE | 869,580 | 10.2% |
| LOAD_GLOBAL_BUILTIN | 665,780 | 7.8% |
| LOAD_FAST_LOAD_FAST | 657,500 | 7.7% |
| LOAD_CONST | 297,460 | 3.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 40,920 | 66.3% |
| FOR_ITER | 20,520 | 33.3% |
| FOR_ITER_TUPLE | 220 | 0.4% |
| COPY | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 30,720 | 49.8% |
| LOAD_ATTR_METHOD_NO_DICT | 30,660 | 49.7% |
| TO_BOOL_STR | 220 | 0.4% |
| LOAD_ATTR | 80 | 0.1% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 538,820 | 33.6% |
| UNPACK_SEQUENCE_TUPLE | 532,260 | 33.2% |
| STORE_FAST_STORE_FAST | 256,000 | 16.0% |
| UNPACK_SEQUENCE | 113,360 | 7.1% |
| POP_TOP | 81,920 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 634,960 | 39.6% |
| LOAD_FAST | 447,160 | 27.9% |
| STORE_FAST_STORE_FAST | 256,000 | 16.0% |
| LOAD_FAST_LOAD_FAST | 143,480 | 8.9% |
| LOAD_GLOBAL_BUILTIN | 51,160 | 3.2% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 180 | 36.0% |
| LOAD_CONST | 100 | 20.0% |
| CALL | 60 | 12.0% |
| LOAD_NAME | 60 | 12.0% |
| IMPORT_NAME | 40 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 72.0% |
| LOAD_BUILD_CLASS | 60 | 12.0% |
| RETURN_CONST | 60 | 12.0% |
| LOAD_NAME | 20 | 4.0% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 297,000 | 28.4% |
| LOAD_FAST_AND_CLEAR | 194,780 | 18.6% |
| BINARY_OP_ADD_INT | 173,960 | 16.6% |
| BUILD_LIST | 153,820 | 14.7% |
| FOR_ITER_LIST | 81,920 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 163,960 | 15.7% |
| BUILD_LIST | 153,820 | 14.7% |
| LOAD_CONST | 122,920 | 11.8% |
| FOR_ITER_LIST | 102,280 | 9.8% |
| POP_EXCEPT | 92,180 | 8.8% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 102,600 | 89.5% |
| RETURN_VALUE | 10,600 | 9.3% |
| UNPACK_SEQUENCE | 380 | 0.3% |
| FOR_ITER | 300 | 0.3% |
| CALL | 280 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 113,360 | 98.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 420 | 0.4% |
| UNPACK_SEQUENCE | 380 | 0.3% |
| UNPACK_SEQUENCE_TUPLE | 320 | 0.3% |
| UNPACK_SEQUENCE_LIST | 40 | 0.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 193,920 | 27.8% |
| BUILD_TUPLE | 163,840 | 23.5% |
| RETURN_VALUE | 122,880 | 17.6% |
| LOAD_FAST | 61,680 | 8.9% |
| COMPARE_OP_STR | 51,180 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 388,960 | 55.9% |
| INTERPRETER_EXIT | 242,120 | 34.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 55,000 | 7.9% |
| YIELD_VALUE | 10,240 | 1.5% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,280 | 50.9% |
| CACHE | 1,800 | 28.0% |
| CALL_KW | 480 | 7.5% |
| POP_TOP | 320 | 5.0% |
| COPY_FREE_VARS | 320 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,180 | 49.4% |
| LOAD_GLOBAL | 1,920 | 29.8% |
| LOAD_CONST | 300 | 4.7% |
| LOAD_FAST_LOAD_FAST | 300 | 4.7% |
| POP_TOP | 240 | 3.7% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_SUBTRACT_FLOAT | 10,200 | 99.8% |
| BINARY_OP | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,220 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 215,360 | 83.9% |
| CALL_LEN | 30,640 | 11.9% |
| LOAD_FAST_LOAD_FAST | 10,520 | 4.1% |
| BINARY_OP | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 173,960 | 67.8% |
| BINARY_SLICE | 41,220 | 16.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 20,720 | 8.1% |
| STORE_FAST | 10,540 | 4.1% |
| LOAD_CONST | 10,280 | 4.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 215,100 | 61.7% |
| RETURN_VALUE | 40,880 | 11.7% |
| LOAD_CONST | 40,880 | 11.7% |
| BINARY_SLICE | 20,480 | 5.9% |
| POP_JUMP_IF_TRUE | 20,440 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 163,920 | 47.0% |
| RETURN_VALUE | 81,900 | 23.5% |
| STORE_FAST | 51,420 | 14.7% |
| COPY | 20,480 | 5.9% |
| LOAD_CONST | 20,460 | 5.9% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,400 | 99.8% |
| BINARY_OP | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 10,220 | 50.0% |
| BINARY_OP_ADD_FLOAT | 10,200 | 49.9% |
| BINARY_OP | 20 | 0.1% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 20,400 | 39.4% |
| LOAD_FAST | 10,520 | 20.3% |
| LOAD_FAST_LOAD_FAST | 10,520 | 20.3% |
| LOAD_CONST | 10,200 | 19.7% |
| BINARY_OP | 100 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 41,200 | 79.6% |
| STORE_FAST | 10,540 | 20.4% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 112,640 | 27.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 81,880 | 20.0% |
| LOAD_CONST | 81,640 | 19.9% |
| LOAD_FAST | 71,620 | 17.5% |
| LOAD_FAST_LOAD_FAST | 41,020 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 133,100 | 32.5% |
| PUSH_EXC_INFO | 112,040 | 27.4% |
| LOAD_ATTR_METHOD_NO_DICT | 51,000 | 12.5% |
| LOAD_FAST_LOAD_FAST | 41,020 | 10.0% |
| RETURN_VALUE | 40,940 | 10.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 204,700 | 52.6% |
| LOAD_FAST | 163,800 | 42.1% |
| LOAD_CONST | 20,480 | 5.3% |
| BINARY_SUBSCR_DICT | 380 | 0.1% |
| BINARY_SUBSCR_GETITEM | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 367,260 | 94.3% |
| LOAD_FAST_LOAD_FAST | 19,680 | 5.1% |
| PUSH_EXC_INFO | 1,880 | 0.5% |
| BINARY_SUBSCR_DICT | 360 | 0.1% |
| RETURN_VALUE | 200 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 92,480 | 64.3% |
| LOAD_FAST_LOAD_FAST | 51,160 | 35.6% |
| BINARY_SUBSCR | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 51,180 | 35.6% |
| RETURN_VALUE | 30,700 | 21.4% |
| TO_BOOL_STR | 30,680 | 21.3% |
| LOAD_ATTR_METHOD_NO_DICT | 20,640 | 14.4% |
| YIELD_VALUE | 10,460 | 7.3% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,440 | 99.4% |
| BINARY_SUBSCR | 60 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 10,460 | 99.6% |
| LOAD_ATTR | 40 | 0.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 470,920 | 85.2% |
| LOAD_FAST | 81,880 | 14.8% |
| BINARY_SUBSCR | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 194,540 | 35.2% |
| STORE_FAST | 163,860 | 29.6% |
| LOAD_GLOBAL_BUILTIN | 143,360 | 25.9% |
| LOAD_ATTR_METHOD_NO_DICT | 40,920 | 7.4% |
| JUMP_FORWARD | 10,220 | 1.8% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,880 | 28.5% |
| LOAD_GLOBAL_MODULE | 40,800 | 28.5% |
| LOAD_ATTR_INSTANCE_VALUE | 30,600 | 21.4% |
| LOAD_ATTR | 20,440 | 14.3% |
| PUSH_NULL | 10,200 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 143,200 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 153,480 | 93.3% |
| LOAD_FAST | 10,320 | 6.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 560 | 0.3% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 133,140 | 80.9% |
| POP_TOP | 30,760 | 18.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 560 | 0.3% |
| CALL_PY_EXACT_ARGS | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 245,440 | 41.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 92,160 | 15.5% |
| LOAD_ATTR_INSTANCE_VALUE | 81,800 | 13.8% |
| CALL_LEN | 51,120 | 8.6% |
| CALL | 31,220 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 255,880 | 43.1% |
| STORE_FAST | 143,400 | 24.2% |
| RETURN_VALUE | 81,880 | 13.8% |
| LOAD_FAST | 61,400 | 10.3% |
| COPY | 30,680 | 5.2% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 419,220 | 51.8% |
| LOAD_FAST_LOAD_FAST | 287,320 | 35.5% |
| LOAD_ATTR_INSTANCE_VALUE | 81,800 | 10.1% |
| BUILD_MAP | 10,200 | 1.3% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 10,200 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 337,380 | 41.7% |
| RETURN_VALUE | 328,280 | 40.6% |
| STORE_FAST | 51,180 | 6.3% |
| PUSH_EXC_INFO | 30,700 | 3.8% |
| LOAD_FAST | 20,440 | 2.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,120 | 99.7% |
| LOAD_CONST | 60 | 0.1% |
| RETURN_GENERATOR | 40 | 0.1% |
| CALL | 20 | 0.0% |
| CALL_STR_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,620 | 50.0% |
| PUSH_EXC_INFO | 20,480 | 49.6% |
| RETURN_VALUE | 140 | 0.3% |
| BEFORE_WITH | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,420 | 41.8% |
| RETURN_GENERATOR | 51,160 | 41.6% |
| BUILD_TUPLE | 10,240 | 8.3% |
| BUILD_LIST | 10,200 | 8.3% |
| CALL | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 61,360 | 49.8% |
| STORE_FAST | 51,440 | 41.8% |
| RETURN_VALUE | 10,240 | 8.3% |
| TO_BOOL | 40 | 0.0% |
| TO_BOOL_INT | 20 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 972,140 | 56.9% |
| LOAD_GLOBAL_MODULE | 490,860 | 28.7% |
| BUILD_TUPLE | 132,860 | 7.8% |
| LOAD_ATTR_MODULE | 91,920 | 5.4% |
| LOAD_ATTR | 20,400 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,411,340 | 82.6% |
| STORE_FAST | 143,380 | 8.4% |
| LOAD_FAST | 81,900 | 4.8% |
| COPY | 51,180 | 3.0% |
| RETURN_VALUE | 20,460 | 1.2% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 368,840 | 52.2% |
| LOAD_ATTR_INSTANCE_VALUE | 266,180 | 37.6% |
| LOAD_ATTR | 40,800 | 5.8% |
| BINARY_SUBSCR | 20,440 | 2.9% |
| LOAD_ATTR_SLOT | 10,200 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 266,180 | 37.6% |
| LOAD_CONST | 143,360 | 20.3% |
| LOAD_GLOBAL_MODULE | 71,880 | 10.2% |
| CALL_BUILTIN_CLASS | 51,120 | 7.2% |
| LOAD_FAST | 40,880 | 5.8% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 287,020 | 65.2% |
| ENTER_EXECUTOR | 101,860 | 23.1% |
| BUILD_TUPLE | 51,120 | 11.6% |
| CALL | 260 | 0.1% |
| LOAD_CONST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 215,000 | 48.8% |
| ENTER_EXECUTOR | 142,340 | 32.3% |
| LOAD_GLOBAL_BUILTIN | 51,160 | 11.6% |
| LOAD_FAST | 20,500 | 4.7% |
| LOAD_FAST_LOAD_FAST | 10,220 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 255,660 | 36.1% |
| LOAD_CONST | 225,440 | 31.8% |
| LOAD_FAST | 81,960 | 11.6% |
| LOAD_FAST_LOAD_FAST | 40,920 | 5.8% |
| LOAD_ATTR_METHOD_LAZY_DICT | 40,800 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 204,960 | 28.9% |
| RETURN_VALUE | 153,520 | 21.7% |
| POP_TOP | 112,960 | 16.0% |
| LOAD_FAST | 71,880 | 10.2% |
| BUILD_TUPLE | 51,400 | 7.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 695,840 | 70.8% |
| LOAD_ATTR_METHOD_NO_DICT | 256,000 | 26.0% |
| LOAD_FAST | 20,400 | 2.1% |
| LOAD_FAST_LOAD_FAST | 10,200 | 1.0% |
| CALL | 700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,840 | 34.4% |
| STORE_FAST | 235,480 | 24.0% |
| POP_TOP | 122,820 | 12.5% |
| GET_ITER | 61,380 | 6.2% |
| LOAD_FAST_LOAD_FAST | 51,180 | 5.2% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,715,820 | 87.5% |
| LOAD_ATTR_METHOD_LAZY_DICT | 138,520 | 7.1% |
| LOAD_ATTR | 51,026 | 2.6% |
| LOAD_SUPER_ATTR_METHOD | 30,640 | 1.6% |
| LOAD_FAST | 20,420 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 432,020 | 22.0% |
| LOAD_FAST | 287,040 | 14.6% |
| GET_ITER | 229,100 | 11.7% |
| STORE_SUBSCR | 204,800 | 10.4% |
| BINARY_SUBSCR | 184,320 | 9.4% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 337,760 | 43.3% |
| LOAD_FAST | 296,720 | 38.1% |
| BINARY_SLICE | 61,600 | 7.9% |
| STORE_FAST | 41,140 | 5.3% |
| LOAD_ATTR_INSTANCE_VALUE | 20,420 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 399,120 | 51.2% |
| POP_TOP | 112,800 | 14.5% |
| RETURN_VALUE | 112,780 | 14.5% |
| STORE_FAST | 61,440 | 7.9% |
| LOAD_CONST | 51,260 | 6.6% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,584,780 | 38.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,042,580 | 25.3% |
| LOAD_FAST_LOAD_FAST | 459,980 | 11.2% |
| LOAD_ATTR | 183,720 | 4.5% |
| GET_ITER | 163,620 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,514,840 | 85.2% |
| COPY_FREE_VARS | 348,020 | 8.4% |
| RETURN_GENERATOR | 235,360 | 5.7% |
| MAKE_CELL | 10,260 | 0.2% |
| STORE_FAST | 8,320 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 235,400 | 24.5% |
| LOAD_FAST | 183,920 | 19.1% |
| LOAD_CONST | 143,220 | 14.9% |
| LOAD_ATTR_INSTANCE_VALUE | 132,680 | 13.8% |
| ENTER_EXECUTOR | 91,860 | 9.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 951,440 | 98.9% |
| MAKE_CELL | 10,220 | 1.1% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,180 | 83.3% |
| RETURN_VALUE | 10,200 | 16.6% |
| CALL | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 51,120 | 83.2% |
| STORE_FAST | 10,260 | 16.7% |
| LOAD_ATTR | 40 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 0.0% |


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
| LOAD_FAST | 40,920 | 99.9% |
| CALL | 20 | 0.0% |
| LOAD_GLOBAL_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,480 | 50.0% |
| CALL_PY_EXACT_ARGS | 20,440 | 49.9% |
| PUSH_NULL | 20 | 0.0% |
| CALL | 20 | 0.0% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 736,460 | 64.8% |
| LOAD_ATTR_INSTANCE_VALUE | 122,760 | 10.8% |
| LOAD_GLOBAL_MODULE | 92,320 | 8.1% |
| CALL | 40,920 | 3.6% |
| COPY | 40,840 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 768,460 | 67.6% |
| POP_JUMP_IF_TRUE | 204,920 | 18.0% |
| EXTENDED_ARG | 122,840 | 10.8% |
| STORE_FAST | 40,960 | 3.6% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 317,160 | 55.2% |
| LOAD_GLOBAL_MODULE | 132,920 | 23.2% |
| LOAD_FAST | 123,320 | 21.5% |
| COMPARE_OP | 660 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 327,780 | 57.1% |
| POP_JUMP_IF_TRUE | 174,480 | 30.4% |
| YIELD_VALUE | 51,180 | 8.9% |
| EXTENDED_ARG | 20,440 | 3.6% |
| COMPARE_OP | 180 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 477,160 | 65.8% |
| GET_ITER | 167,960 | 23.1% |
| SWAP | 68,200 | 9.4% |
| LOAD_FAST | 10,220 | 1.4% |
| FOR_ITER | 2,040 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 436,420 | 60.1% |
| POP_TOP | 193,380 | 26.7% |
| STORE_FAST | 58,880 | 8.1% |
| JUMP_FORWARD | 35,040 | 4.8% |
| FOR_ITER | 1,800 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 479,860 | 45.1% |
| ENTER_EXECUTOR | 311,800 | 29.3% |
| JUMP_BACKWARD | 127,200 | 12.0% |
| SWAP | 102,280 | 9.6% |
| LOAD_FAST | 20,420 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 256,700 | 24.1% |
| LOAD_FAST | 234,560 | 22.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 223,220 | 21.0% |
| RETURN_CONST | 133,060 | 12.5% |
| SWAP | 81,920 | 7.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 61,420 | 54.1% |
| ENTER_EXECUTOR | 51,220 | 45.1% |
| JUMP_BACKWARD | 900 | 0.8% |
| FOR_ITER | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 52,120 | 45.9% |
| LOAD_FAST | 41,040 | 36.1% |
| LOAD_CONST | 20,460 | 18.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 245,140 | 49.6% |
| GET_ITER | 184,340 | 37.3% |
| LOAD_FAST | 61,400 | 12.4% |
| JUMP_BACKWARD | 2,780 | 0.6% |
| SWAP | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 247,740 | 50.1% |
| LOAD_FAST | 184,360 | 37.3% |
| RETURN_CONST | 61,460 | 12.4% |
| STORE_FAST_LOAD_FAST | 220 | 0.0% |
| SWAP | 220 | 0.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,420 | 99.8% |
| LOAD_ATTR | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 50.0% |
| GET_ITER | 10,220 | 50.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,424,340 | 92.1% |
| LOAD_FAST_LOAD_FAST | 234,960 | 3.4% |
| COPY | 163,960 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 91,960 | 1.3% |
| LOAD_DEREF | 51,000 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,248,920 | 17.9% |
| LOAD_ATTR_METHOD_NO_DICT | 1,176,860 | 16.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 460,980 | 6.6% |
| LOAD_CONST | 439,960 | 6.3% |
| STORE_FAST | 358,260 | 5.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 214,680 | 70.1% |
| LOAD_FAST | 90,680 | 29.6% |
| LOAD_ATTR | 460 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 138,520 | 45.2% |
| LOAD_CONST | 61,320 | 20.0% |
| LOAD_FAST | 41,200 | 13.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 40,800 | 13.3% |
| LOAD_GLOBAL_MODULE | 21,200 | 6.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,535,480 | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,176,860 | 20.4% |
| LOAD_GLOBAL_MODULE | 307,180 | 5.3% |
| LOAD_CONST | 245,600 | 4.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 71,840 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,715,820 | 29.7% |
| LOAD_CONST | 1,627,740 | 28.2% |
| LOAD_FAST | 1,251,193 | 21.6% |
| CALL | 278,000 | 4.8% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 256,000 | 4.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,114,760 | 76.0% |
| LOAD_ATTR_INSTANCE_VALUE | 460,980 | 16.6% |
| LOAD_ATTR | 125,320 | 4.5% |
| LOAD_ATTR_MODULE | 51,000 | 1.8% |
| LOAD_GLOBAL_MODULE | 20,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,042,580 | 37.5% |
| LOAD_FAST | 757,000 | 27.2% |
| LOAD_FAST_LOAD_FAST | 378,800 | 13.6% |
| LOAD_CONST | 276,660 | 9.9% |
| CALL_PY_WITH_DEFAULTS | 235,400 | 8.5% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 675,980 | 92.8% |
| LOAD_ATTR_MODULE | 51,080 | 7.0% |
| LOAD_ATTR | 1,140 | 0.2% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 307,520 | 42.2% |
| CALL_ISINSTANCE | 91,920 | 12.6% |
| LOAD_FAST | 61,540 | 8.5% |
| LOAD_ATTR_MODULE | 51,080 | 7.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 51,000 | 7.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,800 | 78.5% |
| LOAD_FAST_LOAD_FAST | 10,200 | 19.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 900 | 1.7% |
| LOAD_ATTR | 100 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 20,400 | 39.2% |
| LOAD_FAST | 10,220 | 19.7% |
| CALL_BUILTIN_FAST | 10,200 | 19.6% |
| LOAD_ATTR_METHOD_NO_DICT | 10,200 | 19.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 900 | 1.7% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 81,600 | 72.6% |
| LOAD_FAST_LOAD_FAST | 30,600 | 27.2% |
| LOAD_ATTR | 220 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 51,100 | 45.5% |
| LOAD_FAST | 20,440 | 18.2% |
| PUSH_NULL | 10,220 | 9.1% |
| CONVERT_VALUE | 10,220 | 9.1% |
| COMPARE_OP_INT | 10,200 | 9.1% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 296,280 | 93.4% |
| RETURN_VALUE | 10,200 | 3.2% |
| LOAD_ATTR_INSTANCE_VALUE | 10,200 | 3.2% |
| LOAD_ATTR | 420 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 317,100 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 163,800 | 55.1% |
| LOAD_FAST | 112,420 | 37.8% |
| COPY | 20,400 | 6.9% |
| LOAD_ATTR_MODULE | 280 | 0.1% |
| LOAD_ATTR | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 164,080 | 55.2% |
| LOAD_CONST | 40,980 | 13.8% |
| GET_ITER | 40,940 | 13.8% |
| PUSH_NULL | 10,220 | 3.4% |
| BUILD_MAP | 10,220 | 3.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,626,740 | 28.2% |
| LOAD_FAST | 859,380 | 14.9% |
| STORE_FAST | 665,780 | 11.5% |
| POP_JUMP_IF_FALSE | 521,880 | 9.0% |
| POP_JUMP_IF_TRUE | 307,140 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,593,760 | 62.2% |
| CALL_ISINSTANCE | 972,140 | 16.8% |
| LOAD_DEREF | 276,240 | 4.8% |
| CHECK_EXC_MATCH | 255,980 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 183,940 | 3.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,279,480 | 20.2% |
| RESUME_CHECK | 1,238,800 | 19.5% |
| STORE_FAST | 869,580 | 13.7% |
| POP_JUMP_IF_FALSE | 623,940 | 9.8% |
| STORE_ATTR_INSTANCE_VALUE | 367,700 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,657,900 | 26.1% |
| LOAD_FAST_LOAD_FAST | 1,157,260 | 18.2% |
| LOAD_ATTR_MODULE | 675,980 | 10.6% |
| CALL_ISINSTANCE | 490,860 | 7.7% |
| CALL | 307,760 | 4.8% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 51,160 | 100.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 51,180 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 204,360 | 99.9% |
| LOAD_SUPER_ATTR | 260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 51,260 | 25.1% |
| LOAD_FAST_LOAD_FAST | 40,960 | 20.0% |
| LOAD_FAST | 40,920 | 20.0% |
| CALL_PY_EXACT_ARGS | 40,840 | 20.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 30,640 | 15.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,514,840 | 34.5% |
| CACHE | 2,555,686 | 25.1% |
| CALL_PY_WITH_DEFAULTS | 951,440 | 9.3% |
| COPY_FREE_VARS | 583,520 | 5.7% |
| FOR_ITER_GEN | 436,420 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,241,766 | 51.4% |
| LOAD_GLOBAL_BUILTIN | 1,626,740 | 16.0% |
| LOAD_GLOBAL_MODULE | 1,238,800 | 12.1% |
| POP_TOP | 685,880 | 6.7% |
| NOP | 542,580 | 5.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 10,220 | 50.0% |
| LOAD_CONST | 10,220 | 50.0% |
| SEND | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 10,220 | 50.0% |
| RESUME_CHECK | 10,220 | 50.0% |
| RESUME | 20 | 0.1% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,267,800 | 57.4% |
| LOAD_FAST_LOAD_FAST | 1,472,000 | 37.3% |
| SWAP | 163,960 | 4.2% |
| LOAD_ATTR_INSTANCE_VALUE | 30,640 | 0.8% |
| LOAD_DEREF | 10,200 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 982,820 | 24.9% |
| LOAD_FAST | 972,140 | 24.6% |
| LOAD_CONST | 613,440 | 15.5% |
| RETURN_CONST | 583,180 | 14.8% |
| LOAD_GLOBAL_MODULE | 367,700 | 9.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,460 | 46.6% |
| LOAD_FAST_LOAD_FAST | 61,340 | 40.0% |
| SWAP | 20,400 | 13.3% |
| STORE_ATTR | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 51,180 | 33.4% |
| LOAD_FAST | 40,920 | 26.7% |
| LOAD_FAST_LOAD_FAST | 30,660 | 20.0% |
| LOAD_CONST | 20,460 | 13.3% |
| LOAD_GLOBAL_BUILTIN | 10,200 | 6.6% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 71,400 | 53.5% |
| LOAD_FAST_LOAD_FAST | 30,960 | 23.2% |
| BINARY_OP_ADD_UNICODE | 10,460 | 7.8% |
| LOAD_FAST | 10,240 | 7.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,200 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 50,720 | 38.0% |
| LOAD_FAST | 40,900 | 30.6% |
| LOAD_CONST | 30,660 | 23.0% |
| LOAD_FAST_LOAD_FAST | 10,220 | 7.7% |
| JUMP_BACKWARD | 960 | 0.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 51,160 | 100.0% |
| STORE_SUBSCR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 51,180 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 215,840 | 55.5% |
| LOAD_ATTR | 91,700 | 23.6% |
| LOAD_FAST | 80,680 | 20.7% |
| TO_BOOL_NONE | 400 | 0.1% |
| TO_BOOL | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 297,480 | 76.5% |
| POP_JUMP_IF_FALSE | 91,100 | 23.4% |
| TO_BOOL_NONE | 380 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,411,340 | 31.6% |
| LOAD_FAST | 900,100 | 20.1% |
| CALL | 501,160 | 11.2% |
| RETURN_CONST | 378,660 | 8.5% |
| LOAD_ATTR_INSTANCE_VALUE | 357,940 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,009,006 | 67.3% |
| POP_JUMP_IF_TRUE | 1,432,920 | 32.0% |
| UNARY_NOT | 20,440 | 0.5% |
| EXTENDED_ARG | 10,240 | 0.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 122,840 | 52.2% |
| LOAD_FAST | 40,840 | 17.3% |
| LOAD_ATTR | 30,640 | 13.0% |
| COPY | 20,400 | 8.7% |
| CALL_LEN | 10,220 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 153,540 | 65.2% |
| POP_JUMP_IF_FALSE | 81,880 | 34.8% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 163,500 | 79.9% |
| LOAD_ATTR_INSTANCE_VALUE | 40,820 | 20.0% |
| TO_BOOL | 260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 132,940 | 65.0% |
| POP_JUMP_IF_TRUE | 71,640 | 35.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 526,320 | 49.6% |
| COPY | 234,940 | 22.1% |
| LOAD_ATTR_INSTANCE_VALUE | 102,040 | 9.6% |
| CALL | 101,320 | 9.5% |
| LOAD_ATTR | 61,580 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 612,380 | 57.7% |
| POP_JUMP_IF_TRUE | 428,200 | 40.3% |
| EXTENDED_ARG | 19,460 | 1.8% |
| TO_BOOL_STR | 1,340 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 400 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 957,740 | 81.7% |
| COPY | 122,720 | 10.5% |
| ENTER_EXECUTOR | 38,820 | 3.3% |
| BINARY_SUBSCR_LIST_INT | 30,680 | 2.6% |
| STORE_FAST | 20,400 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 717,720 | 61.2% |
| POP_JUMP_IF_FALSE | 411,860 | 35.1% |
| EXTENDED_ARG | 41,940 | 3.6% |
| TO_BOOL_NONE | 1,400 | 0.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 20,640 | 99.8% |
| UNPACK_SEQUENCE | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 20,680 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 399,120 | 65.0% |
| RETURN_VALUE | 153,440 | 25.0% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 30,680 | 5.0% |
| LOAD_FAST | 20,400 | 3.3% |
| LOAD_CONST | 10,200 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 532,260 | 86.7% |
| POP_TOP | 81,900 | 13.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 223,220 | 37.8% |
| FOR_ITER | 127,260 | 21.6% |
| LOAD_FAST | 92,040 | 15.6% |
| YIELD_VALUE | 55,000 | 9.3% |
| CALL | 40,920 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 538,820 | 91.3% |
| STORE_FAST | 40,940 | 6.9% |
| LOAD_FAST | 10,220 | 1.7% |


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
|     deferred | 298,140 | 21.7% |
|          hit | 1,074,940 | 78.2% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 720 | 42.4% |
| Failure | 980 | 57.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 780 | 79.6% |
| add different types | 200 | 20.4% |


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
|     deferred | 298,160 | 16.1% |
|          hit | 1,555,680 | 83.8% |
|         miss | 42,300 | 2.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,400 | 56.5% |
| Failure | 1,080 | 43.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 520 | 48.1% |
| code complex parameters | 320 | 29.6% |
| other | 240 | 22.2% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 3,699,919 | 19.3% |
|          hit | 15,445,580 | 80.5% |
|         miss | 208,046 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,260 | 41.7% |
| Failure | 22,760 | 58.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 3,820 | 16.8% |
| code complex parameters | 3,620 | 15.9% |
| class no vectorcall | 2,640 | 11.6% |
| meth descr method fastcall keywords | 2,520 | 11.1% |
| metaclass | 2,240 | 9.8% |
| cfunc noargs | 1,520 | 6.7% |
| meth descr varargs keywords | 1,460 | 6.4% |
| cfunc varargs keywords | 1,080 | 4.7% |
| operator wrapper | 840 | 3.7% |
| other | 540 | 2.4% |
| wrong number arguments | 520 | 2.3% |
| cfunc varargs | 500 | 2.2% |
| cmethod | 400 | 1.8% |
| class mutable | 400 | 1.8% |
| no dict | 320 | 1.4% |
| method wrapper | 180 | 0.8% |
| str | 160 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 258,040 | 10.0% |
|          hit | 2,313,500 | 89.8% |
|         miss | 10,240 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,820 | 43.3% |
| Failure | 2,380 | 56.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 1,300 | 54.6% |
| big int | 340 | 14.3% |
| bool | 220 | 9.2% |
| bytes | 200 | 8.4% |
| list | 160 | 6.7% |
| set | 160 | 6.7% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 600,600 | 21.0% |
|          hit | 2,251,640 | 78.6% |
|         miss | 145,080 | 5.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,800 | 29.7% |
| Failure | 9,000 | 70.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 3,840 | 42.7% |
| dict keys | 3,480 | 38.7% |
| dict items | 540 | 6.0% |
| enumerate | 360 | 4.0% |
| dict values | 340 | 3.8% |
| reversed list | 200 | 2.2% |
| set | 160 | 1.8% |
| ascii string | 80 | 0.9% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,808,798 | 13.0% |
|          hit | 18,723,033 | 86.8% |
|         miss | 111,680 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,500 | 37.8% |
| Failure | 28,780 | 62.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 21,980 | 76.4% |
| method | 2,140 | 7.4% |
| metaclass attribute | 1,000 | 3.5% |
| class attr descriptor | 960 | 3.3% |
| module attr not found | 820 | 2.8% |
| class method obj | 760 | 2.6% |
| class attr simple | 480 | 1.7% |
| non overriding descriptor | 320 | 1.1% |
| mutable class | 320 | 1.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,700 | 0.1% |
|        deopt | 800 | 0.0% |
|          hit | 12,122,200 | 99.8% |
|         miss | 2,080 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,960 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.1% |
|          hit | 255,800 | 99.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 280 | 100.0% |
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
|     deferred | 20 | 0.1% |
|          hit | 20,460 | 99.8% |

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
|     deferred | 714,060 | 14.8% |
|          hit | 4,099,600 | 84.9% |
|         miss | 13,480 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,360 | 33.9% |
| Failure | 10,460 | 66.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 9,300 | 88.9% |
| class attr simple | 500 | 4.8% |
| property | 480 | 4.6% |
| overridden | 160 | 1.5% |
| no dict | 20 | 0.2% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 420,220 | 49.3% |
|          hit | 429,940 | 50.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 16.0% |
| Failure | 1,360 | 84.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 780 | 57.4% |
| other | 580 | 42.6% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 925,220 | 10.7% |
|          hit | 7,668,446 | 89.1% |
|         miss | 194,940 | 2.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,160 | 67.6% |
| Failure | 4,880 | 32.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 1,960 | 40.2% |
| dict | 1,180 | 24.2% |
| sequence | 760 | 15.6% |
| set | 320 | 6.6% |
| tuple | 320 | 6.6% |
| other | 180 | 3.7% |
| mapping | 160 | 3.3% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 113,420 | 6.0% |
|          hit | 1,760,920 | 93.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 67.2% |
| Failure | 380 | 32.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 380 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 104,546,982 | 51.9% |
| Not specialized | 23,167,757 | 11.5% |
| Specialized hits | 72,981,625 | 36.2% |
| Specialized misses | 727,906 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 3,699,919 | 36.5% |
| LOAD_ATTR | 2,808,798 | 27.7% |
| TO_BOOL | 925,220 | 9.1% |
| STORE_ATTR | 714,060 | 7.0% |
| FOR_ITER | 600,600 | 5.9% |
| STORE_SUBSCR | 420,220 | 4.1% |
| BINARY_SUBSCR | 298,160 | 2.9% |
| BINARY_OP | 298,140 | 2.9% |
| COMPARE_OP | 258,040 | 2.5% |
| UNPACK_SEQUENCE | 113,420 | 1.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 109,726 | 15.1% |
| FOR_ITER_GEN | 95,720 | 13.2% |
| TO_BOOL_NONE | 95,500 | 13.1% |
| TO_BOOL_STR | 77,520 | 10.6% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 51,000 | 7.0% |
| FOR_ITER_LIST | 49,360 | 6.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 31,360 | 4.3% |
| CALL_METHOD_DESCRIPTOR_O | 31,220 | 4.3% |
| LOAD_ATTR_METHOD_LAZY_DICT | 29,040 | 4.0% |
| BINARY_SUBSCR_GETITEM | 22,160 | 3.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 2,958,126 | 27.8% |
| Calls to Python functions inlined | 7,685,400 | 72.2% |
| Calls via PyEval_EvalFrame (total) | 2,958,126 | 27.8% |
| Calls via PyEval_EvalFrame (vector) | 2,543,426 | 23.9% |
| Calls via PyEval_EvalFrame (generator) | 414,700 | 3.9% |
| Calls via PyEval_EvalFrame (legacy) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,543,346 | 23.9% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 451,940 | 4.2% |
| Calls via PyEval_EvalFrame (function ex) | 102,580 | 1.0% |
| Calls via PyEval_EvalFrame (api) | 266,800 | 2.5% |
| Calls via PyEval_EvalFrame (method) | 71,626 | 0.7% |
| Frame objects created | 389,200 | 3.7% |
| Frames pushed | 9,721,686 | 91.3% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 8,848,233 | 37.3% |
| Frees to freelist | 8,850,553 |  |
| Allocations | 14,898,706 | 62.7% |
| Allocations to 512 bytes | 14,806,066 | 62.3% |
| Allocations to 4 kbytes | 82,360 | 0.3% |
| Allocations over 4 kbytes | 10,280 | 0.0% |
| Frees | 15,680,440 |  |
| New values | 379,260 |  |
| Interpreter increfs | 91,832,415 | 69.0% |
| Interpreter decrefs | 106,651,634 | 69.2% |
| Increfs | 41,292,984 | 31.0% |
| Decrefs | 47,435,631 | 30.8% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 20 | 0.0% |
| Method cache hits | 5,007,266 |  |
| Method cache misses | 173,357 |  |
| Method cache collisions | 254,911 |  |
| Method cache dunder hits | 3,988,854 |  |
| Method cache dunder misses | 87,526 |  |


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
| Optimization attempts | 2,460 |  |
| Traces created | 1,200 | 48.8% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 20 | 0.8% |
| Trace too long | 0 | 0.0% |
| Trace too short | 1,260 | 51.2% |
| Inner loop found | 0 | 0.0% |
| Recursive call | 0 | 0.0% |
| Low confidence | 0 | 0.0% |
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
| <= 16 | 180 | 15.0% |
| <= 32 | 580 | 48.3% |
| <= 64 | 260 | 21.7% |
| <= 128 | 180 | 15.0% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 80 | 6.7% |
| <= 16 | 360 | 30.0% |
| <= 32 | 240 | 20.0% |
| <= 64 | 60 | 5.0% |
| <= 128 | 60 | 5.0% |


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
| FOR_ITER_GEN | 1,260 |
| CALL | 160 |
| YIELD_VALUE | 140 |
| CALL_FUNCTION_EX | 40 |
| CALL_LIST_APPEND | 40 |
| CALL_KW | 20 |
| CALL_PY_WITH_DEFAULTS | 20 |


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
