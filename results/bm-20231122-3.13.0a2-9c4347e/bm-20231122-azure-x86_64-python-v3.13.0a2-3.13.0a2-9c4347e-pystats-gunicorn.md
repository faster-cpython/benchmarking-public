
# Pystats results

- benchmark: gunicorn
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 42,129,683 | 19.0% | 19.0% |  |
| LOAD_CONST | 13,123,140 | 5.9% | 24.9% |  |
| STORE_FAST | 10,429,020 | 4.7% | 29.6% |  |
| RESUME_CHECK | 10,401,418 | 4.7% | 34.3% |  |
| POP_JUMP_IF_FALSE | 7,929,058 | 3.6% | 37.9% |  |
| LOAD_FAST_LOAD_FAST | 7,252,720 | 3.3% | 41.2% |  |
| LOAD_ATTR_INSTANCE_VALUE | 6,969,460 | 3.1% | 44.3% | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 6,678,049 | 3.0% | 47.3% | 0.2% |
| LOAD_GLOBAL_MODULE | 6,542,980 | 3.0% | 50.3% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 6,060,060 | 2.7% | 53.0% | 0.0% |
| RETURN_VALUE | 6,034,178 | 2.7% | 55.8% |  |
| POP_TOP | 5,244,518 | 2.4% | 58.1% |  |
| POP_JUMP_IF_TRUE | 4,967,540 | 2.2% | 60.4% |  |
| TO_BOOL_BOOL | 4,451,818 | 2.0% | 62.4% |  |
| CALL_PY_EXACT_ARGS | 4,204,520 | 1.9% | 64.3% | 0.4% |
| STORE_ATTR_INSTANCE_VALUE | 3,949,420 | 1.8% | 66.1% | 0.3% |
| RETURN_CONST | 3,615,760 | 1.6% | 67.7% |  |
| CALL | 3,520,768 | 1.6% | 69.3% |  |
| JUMP_BACKWARD | 3,227,040 | 1.5% | 70.7% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,088,580 | 1.4% | 72.1% | 0.5% |
| INTERPRETER_EXIT | 2,921,478 | 1.3% | 73.4% |  |
| LOAD_ATTR | 2,814,630 | 1.3% | 74.7% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,244,558 | 1.0% | 75.7% | 4.9% |
| STORE_FAST_STORE_FAST | 2,140,660 | 1.0% | 76.7% |  |
| CALL_ISINSTANCE | 1,709,240 | 0.8% | 77.5% |  |
| GET_ITER | 1,618,620 | 0.7% | 78.2% |  |
| FOR_ITER_LIST | 1,512,680 | 0.7% | 78.9% | 3.3% |
| COMPARE_OP_INT | 1,402,420 | 0.6% | 79.5% |  |
| BUILD_TUPLE | 1,352,020 | 0.6% | 80.1% |  |
| CONTAINS_OP | 1,342,140 | 0.6% | 80.7% |  |
| NOP | 1,311,669 | 0.6% | 81.3% |  |
| TO_BOOL_STR | 1,295,280 | 0.6% | 81.9% | 6.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 1,218,140 | 0.5% | 82.5% |  |
| PUSH_NULL | 1,168,340 | 0.5% | 83.0% |  |
| POP_JUMP_IF_NOT_NONE | 1,157,940 | 0.5% | 83.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,095,600 | 0.5% | 84.0% |  |
| FOR_ITER_TUPLE | 1,065,740 | 0.5% | 84.5% |  |
| TO_BOOL_NONE | 1,062,140 | 0.5% | 85.0% | 9.3% |
| SWAP | 1,055,520 | 0.5% | 85.4% |  |
| COPY | 1,034,400 | 0.5% | 85.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 972,920 | 0.4% | 86.3% | 2.1% |
| CALL_PY_WITH_DEFAULTS | 961,660 | 0.4% | 86.8% |  |
| FOR_ITER | 934,240 | 0.4% | 87.2% |  |
| COMPARE_OP_STR | 921,280 | 0.4% | 87.6% | 1.1% |
| CALL_METHOD_DESCRIPTOR_O | 819,600 | 0.4% | 88.0% | 3.8% |
| CALL_BUILTIN_FAST | 809,340 | 0.4% | 88.3% |  |
| YIELD_VALUE | 778,280 | 0.4% | 88.7% |  |
| CALL_LEN | 777,860 | 0.4% | 89.0% |  |
| BUILD_LIST | 768,620 | 0.3% | 89.4% |  |
| FOR_ITER_GEN | 762,100 | 0.3% | 89.7% | 12.8% |
| TO_BOOL | 755,240 | 0.3% | 90.1% |  |
| LOAD_ATTR_MODULE | 738,060 | 0.3% | 90.4% | 0.0% |
| POP_JUMP_IF_NONE | 727,340 | 0.3% | 90.7% |  |
| STORE_ATTR | 716,360 | 0.3% | 91.1% |  |
| CALL_KW | 686,360 | 0.3% | 91.4% |  |
| CALL_FUNCTION_EX | 686,320 | 0.3% | 91.7% |  |
| LOAD_DEREF | 655,800 | 0.3% | 92.0% |  |
| BUILD_MAP | 655,440 | 0.3% | 92.3% |  |
| BINARY_SLICE | 635,340 | 0.3% | 92.6% |  |
| UNPACK_SEQUENCE_TUPLE | 614,160 | 0.3% | 92.8% |  |
| CALL_BUILTIN_CLASS | 603,760 | 0.3% | 93.1% |  |
| COPY_FREE_VARS | 594,120 | 0.3% | 93.4% |  |
| JUMP_FORWARD | 563,340 | 0.3% | 93.6% |  |
| BINARY_SUBSCR_TUPLE_INT | 552,940 | 0.2% | 93.9% |  |
| BINARY_OP_ADD_INT | 511,840 | 0.2% | 94.1% |  |
| BINARY_OP | 504,360 | 0.2% | 94.3% |  |
| COMPARE_OP | 456,580 | 0.2% | 94.5% |  |
| STORE_SUBSCR | 452,460 | 0.2% | 94.8% |  |
| IS_OP | 441,100 | 0.2% | 95.0% |  |
| CALL_LIST_APPEND | 440,300 | 0.2% | 95.2% |  |
| BINARY_OP_ADD_UNICODE | 420,040 | 0.2% | 95.3% |  |
| FOR_ITER_RANGE | 419,840 | 0.2% | 95.5% |  |
| BINARY_SUBSCR_DICT | 409,920 | 0.2% | 95.7% | 4.9% |
| RETURN_GENERATOR | 399,400 | 0.2% | 95.9% |  |
| BINARY_SUBSCR_GETITEM | 389,420 | 0.2% | 96.1% | 5.7% |
| TO_BOOL_ALWAYS_TRUE | 388,980 | 0.2% | 96.2% | 5.6% |
| STORE_SUBSCR_DICT | 378,760 | 0.2% | 96.4% |  |
| EXTENDED_ARG | 368,660 | 0.2% | 96.6% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 346,340 | 0.2% | 96.7% | 8.4% |
| BEFORE_WITH | 327,880 | 0.1% | 96.9% |  |
| CALL_BUILTIN_O | 327,640 | 0.1% | 97.0% |  |
| LOAD_ATTR_SLOT | 317,620 | 0.1% | 97.2% |  |
| POP_EXCEPT | 317,520 | 0.1% | 97.3% |  |
| PUSH_EXC_INFO | 317,520 | 0.1% | 97.5% |  |
| LOAD_ATTR_PROPERTY | 317,100 | 0.1% | 97.6% |  |
| DICT_MERGE | 307,280 | 0.1% | 97.7% |  |
| CHECK_EXC_MATCH | 297,040 | 0.1% | 97.9% |  |
| BINARY_SUBSCR | 258,340 | 0.1% | 98.0% |  |
| MAKE_FUNCTION | 235,880 | 0.1% | 98.1% |  |
| LOAD_FAST_AND_CLEAR | 235,740 | 0.1% | 98.2% |  |
| TO_BOOL_INT | 235,420 | 0.1% | 98.3% |  |
| BINARY_SUBSCR_LIST_INT | 204,720 | 0.1% | 98.4% |  |
| LOAD_SUPER_ATTR_METHOD | 204,620 | 0.1% | 98.5% |  |
| TO_BOOL_LIST | 204,580 | 0.1% | 98.6% |  |
| END_FOR | 194,480 | 0.1% | 98.7% |  |
| STORE_ATTR_SLOT | 174,420 | 0.1% | 98.8% | 15.4% |
| EXIT_INIT_CHECK | 173,900 | 0.1% | 98.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 173,900 | 0.1% | 98.9% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 164,480 | 0.1% | 99.0% | 19.1% |
| SEND_GEN | 122,840 | 0.1% | 99.0% |  |
| UNPACK_SEQUENCE | 114,580 | 0.1% | 99.1% |  |
| RERAISE | 112,640 | 0.1% | 99.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 112,420 | 0.1% | 99.2% |  |
| FORMAT_SIMPLE | 102,400 | 0.0% | 99.2% |  |
| DELETE_ATTR | 92,160 | 0.0% | 99.3% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 92,160 | 0.0% | 99.3% |  |
| RAISE_VARARGS | 92,160 | 0.0% | 99.4% |  |
| LIST_APPEND | 82,400 | 0.0% | 99.4% |  |
| BUILD_CONST_KEY_MAP | 81,960 | 0.0% | 99.4% |  |
| BINARY_OP_SUBTRACT_INT | 71,580 | 0.0% | 99.5% |  |
| STORE_FAST_LOAD_FAST | 61,940 | 0.0% | 99.5% |  |
| LOAD_FAST_CHECK | 61,560 | 0.0% | 99.5% |  |
| BUILD_STRING | 61,440 | 0.0% | 99.6% |  |
| CALL_STR_1 | 61,440 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 52,000 | 0.0% | 99.6% | 98.1% |
| CALL_INTRINSIC_1 | 51,300 | 0.0% | 99.6% |  |
| LIST_EXTEND | 51,300 | 0.0% | 99.7% |  |
| MAKE_CELL | 51,240 | 0.0% | 99.7% |  |
| CONVERT_VALUE | 51,200 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_ATTR | 51,180 | 0.0% | 99.7% |  |
| STORE_SUBSCR_LIST_INT | 51,180 | 0.0% | 99.8% |  |
| UNPACK_SEQUENCE_LIST | 51,160 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 41,180 | 0.0% | 99.8% | 0.1% |
| BINARY_SUBSCR_STR_INT | 40,980 | 0.0% | 99.8% |  |
| CALL_TYPE_1 | 40,960 | 0.0% | 99.8% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 40,880 | 0.0% | 99.8% |  |
| END_SEND | 30,720 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 30,720 | 0.0% | 99.9% |  |
| IMPORT_FROM | 30,720 | 0.0% | 99.9% |  |
| MAP_ADD | 30,720 | 0.0% | 99.9% |  |
| LOAD_GLOBAL | 21,620 | 0.0% | 99.9% |  |
| IMPORT_NAME | 20,540 | 0.0% | 99.9% |  |
| UNARY_NOT | 20,480 | 0.0% | 99.9% |  |
| WITH_EXCEPT_START | 20,480 | 0.0% | 99.9% |  |
| BUILD_SET | 20,480 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 20,460 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 20,440 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 10,340 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 10,260 | 0.0% | 100.0% |  |
| BUILD_SLICE | 10,240 | 0.0% | 100.0% |  |
| SET_ADD | 10,240 | 0.0% | 100.0% |  |
| SET_UPDATE | 10,240 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 10,220 | 0.0% | 100.0% | 0.6% |
| RESUME | 6,500 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| STORE_NAME | 500 | 0.0% | 100.0% |  |
| LOAD_NAME | 100 | 0.0% | 100.0% |  |
| SEND | 80 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 60 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 40 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 6,412,100 | 2.9% | 2.9% |
| STORE_FAST LOAD_FAST | 5,992,720 | 2.7% | 5.6% |
| RESUME_CHECK LOAD_FAST | 5,322,898 | 2.4% | 8.0% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 4,280,280 | 1.9% | 9.9% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,127,969 | 1.9% | 11.8% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,879,200 | 1.8% | 13.5% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 3,596,020 | 1.6% | 15.2% |
| LOAD_FAST LOAD_CONST | 3,513,940 | 1.6% | 16.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,988,218 | 1.3% | 18.1% |
| CACHE RESUME_CHECK | 2,511,258 | 1.1% | 19.2% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,257,600 | 1.0% | 20.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 2,257,400 | 1.0% | 21.3% |
| POP_JUMP_IF_TRUE LOAD_FAST | 2,191,620 | 1.0% | 22.3% |
| LOAD_FAST LOAD_ATTR | 2,109,954 | 1.0% | 23.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 1,970,360 | 0.9% | 24.1% |
| LOAD_CONST LOAD_FAST | 1,741,600 | 0.8% | 24.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 1,719,180 | 0.8% | 25.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 1,678,500 | 0.8% | 26.4% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 1,626,740 | 0.7% | 27.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 1,615,260 | 0.7% | 27.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,597,089 | 0.7% | 28.6% |
| RETURN_CONST POP_TOP | 1,587,560 | 0.7% | 29.3% |
| LOAD_CONST LOAD_CONST | 1,475,600 | 0.7% | 30.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,472,000 | 0.7% | 30.7% |
| RETURN_VALUE INTERPRETER_EXIT | 1,465,658 | 0.7% | 31.3% |
| POP_TOP LOAD_FAST | 1,464,418 | 0.7% | 32.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,432,920 | 0.6% | 32.6% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 1,411,340 | 0.6% | 33.3% |
| RETURN_VALUE STORE_FAST | 1,382,940 | 0.6% | 33.9% |
| LOAD_FAST RETURN_VALUE | 1,352,140 | 0.6% | 34.5% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,320,120 | 0.6% | 35.1% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,259,720 | 0.6% | 35.7% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,259,240 | 0.6% | 36.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,258,840 | 0.6% | 36.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 1,186,740 | 0.5% | 37.3% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 1,157,260 | 0.5% | 37.9% |
| RETURN_CONST INTERPRETER_EXIT | 1,137,420 | 0.5% | 38.4% |
| LOAD_FAST TO_BOOL_STR | 1,118,600 | 0.5% | 38.9% |
| LOAD_FAST TO_BOOL_BOOL | 1,114,820 | 0.5% | 39.4% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 1,093,260 | 0.5% | 39.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,044,440 | 0.5% | 40.3% |
| POP_TOP JUMP_BACKWARD | 1,024,120 | 0.5% | 40.8% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,023,540 | 0.5% | 41.3% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 992,740 | 0.4% | 41.7% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 972,140 | 0.4% | 42.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 972,140 | 0.4% | 42.6% |
| LOAD_FAST LOAD_FAST | 962,700 | 0.4% | 43.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 952,800 | 0.4% | 43.5% |
| STORE_FAST_STORE_FAST LOAD_FAST | 952,520 | 0.4% | 43.9% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 951,440 | 0.4% | 44.3% |
| LOAD_CONST CALL | 946,120 | 0.4% | 44.7% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 941,200 | 0.4% | 45.2% |
| LOAD_CONST COMPARE_OP_INT | 940,980 | 0.4% | 45.6% |
| LOAD_FAST CALL | 918,049 | 0.4% | 46.0% |
| JUMP_BACKWARD FOR_ITER_LIST | 888,180 | 0.4% | 46.4% |
| STORE_FAST LOAD_GLOBAL_MODULE | 879,480 | 0.4% | 46.8% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 870,860 | 0.4% | 47.2% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 859,380 | 0.4% | 47.6% |
| JUMP_BACKWARD FOR_ITER_TUPLE | 819,640 | 0.4% | 48.0% |
| FOR_ITER_TUPLE STORE_FAST | 819,200 | 0.4% | 48.3% |
| POP_TOP RETURN_CONST | 809,360 | 0.4% | 48.7% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 809,060 | 0.4% | 49.1% |
| PUSH_NULL LOAD_FAST | 799,140 | 0.4% | 49.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 788,840 | 0.4% | 49.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 788,620 | 0.4% | 50.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 787,480 | 0.4% | 50.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 778,560 | 0.4% | 50.8% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 778,520 | 0.4% | 51.2% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 726,320 | 0.3% | 51.5% |
| CALL STORE_FAST | 687,940 | 0.3% | 51.8% |
| LOAD_CONST CALL_KW | 686,360 | 0.3% | 52.1% |
| NOP LOAD_FAST | 686,329 | 0.3% | 52.4% |
| RESUME_CHECK POP_TOP | 685,880 | 0.3% | 52.7% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 685,820 | 0.3% | 53.1% |
| RETURN_VALUE RETURN_VALUE | 675,900 | 0.3% | 53.4% |
| POP_JUMP_IF_FALSE LOAD_CONST | 665,860 | 0.3% | 53.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 664,580 | 0.3% | 54.0% |
| STORE_FAST_STORE_FAST STORE_FAST | 634,960 | 0.3% | 54.3% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 612,380 | 0.3% | 54.5% |
| LOAD_CONST STORE_FAST | 604,620 | 0.3% | 54.8% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 603,480 | 0.3% | 55.1% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 603,220 | 0.3% | 55.3% |
| LOAD_FAST POP_JUMP_IF_NONE | 583,840 | 0.3% | 55.6% |
| LOAD_FAST COPY | 583,680 | 0.3% | 55.9% |
| COPY_FREE_VARS RESUME_CHECK | 583,520 | 0.3% | 56.1% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 583,180 | 0.3% | 56.4% |
| LOAD_FAST CONTAINS_OP | 553,360 | 0.2% | 56.6% |
| RETURN_VALUE LOAD_FAST | 552,940 | 0.2% | 56.9% |
| RESUME_CHECK NOP | 542,580 | 0.2% | 57.1% |
| LOAD_FAST TO_BOOL_NONE | 538,840 | 0.2% | 57.4% |
| LOAD_ATTR LOAD_FAST | 536,040 | 0.2% | 57.6% |
| CALL RETURN_VALUE | 532,989 | 0.2% | 57.9% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 532,260 | 0.2% | 58.1% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 521,880 | 0.2% | 58.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS LOAD_FAST | 511,820 | 0.2% | 58.6% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 511,780 | 0.2% | 58.8% |
| JUMP_BACKWARD FOR_ITER_GEN | 511,000 | 0.2% | 59.0% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 509,220 | 0.2% | 59.3% |
| CALL TO_BOOL_BOOL | 501,160 | 0.2% | 59.5% |
| LOAD_FAST GET_ITER | 491,900 | 0.2% | 59.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 338,220 | 53.2% |
| BINARY_OP_ADD_INT | 245,740 | 38.7% |
| LOAD_FAST | 51,360 | 8.1% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 286,760 | 45.1% |
| GET_ITER | 163,920 | 25.8% |
| CALL_METHOD_DESCRIPTOR_O | 92,080 | 14.5% |
| LOAD_ATTR_METHOD_NO_DICT | 40,840 | 6.4% |
| LOAD_CONST | 20,520 | 3.2% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,511,258 | 85.6% |
| POP_TOP | 164,480 | 5.6% |
| COPY_FREE_VARS | 153,660 | 5.2% |
| RETURN_GENERATOR | 102,400 | 3.5% |
| RESUME | 1,800 | 0.1% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 286,640 | 87.4% |
| RETURN_VALUE | 40,980 | 12.5% |
| LOAD_ATTR | 120 | 0.0% |
| CALL | 100 | 0.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 317,620 | 96.9% |
| STORE_FAST | 10,260 | 3.1% |


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
| RETURN_CONST | 194,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 81,900 | 42.1% |
| STORE_FAST | 51,160 | 26.3% |
| LOAD_CONST | 20,480 | 10.5% |
| LOAD_FAST | 20,480 | 10.5% |
| JUMP_FORWARD | 10,240 | 5.3% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 30,720 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 30,720 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 173,900 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 173,900 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 51,200 | 50.0% |
| LOAD_FAST | 40,960 | 40.0% |
| LOAD_GLOBAL_MODULE | 10,220 | 10.0% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 61,440 | 60.0% |
| LOAD_CONST | 40,960 | 40.0% |


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
| LOAD_ATTR_SLOT | 20,460 | 66.6% |
| RETURN_GENERATOR | 10,240 | 33.3% |
| LOAD_ATTR | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 30,720 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,465,658 | 50.2% |
| RETURN_CONST | 1,137,420 | 38.9% |
| YIELD_VALUE | 216,000 | 7.4% |
| RETURN_GENERATOR | 102,400 | 3.5% |


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
| RESUME_CHECK | 542,580 | 41.4% |
| STORE_FAST | 164,060 | 12.5% |
| POP_JUMP_IF_FALSE | 153,669 | 11.7% |
| POP_JUMP_IF_TRUE | 133,120 | 10.1% |
| POP_TOP | 82,140 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 686,329 | 52.3% |
| LOAD_FAST_LOAD_FAST | 184,360 | 14.1% |
| LOAD_GLOBAL_MODULE | 174,120 | 13.3% |
| LOAD_GLOBAL_BUILTIN | 153,200 | 11.7% |
| NOP | 61,460 | 4.7% |


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
| JUMP_BACKWARD | 10,280 | 3.2% |
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
| BEFORE_WITH | 317,620 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,464,418 | 27.9% |
| JUMP_BACKWARD | 1,024,120 | 19.5% |
| RETURN_CONST | 809,360 | 15.4% |
| LOAD_CONST | 440,420 | 8.4% |
| RESUME_CHECK | 388,820 | 7.4% |


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
| LOAD_ATTR | 451,160 | 38.6% |
| LOAD_ATTR_MODULE | 317,360 | 27.2% |
| LOAD_FAST | 307,400 | 26.3% |
| LOAD_SUPER_ATTR_ATTR | 51,180 | 4.4% |
| BINARY_SUBSCR_DICT | 20,480 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 799,140 | 68.4% |
| CALL | 143,720 | 12.3% |
| LOAD_FAST_LOAD_FAST | 71,820 | 6.1% |
| LOAD_CONST | 71,780 | 6.1% |
| LOAD_GLOBAL_MODULE | 61,320 | 5.2% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 235,360 | 58.9% |
| CACHE | 102,400 | 25.6% |
| CALL_FUNCTION_EX | 30,720 | 7.7% |
| COPY_FREE_VARS | 10,280 | 2.6% |
| CALL_KW | 10,240 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 112,640 | 28.2% |
| INTERPRETER_EXIT | 102,400 | 25.6% |
| CALL_BUILTIN_O | 51,160 | 12.8% |
| STORE_FAST | 40,960 | 10.3% |
| LOAD_FAST | 30,720 | 7.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,352,140 | 22.4% |
| RETURN_VALUE | 675,900 | 11.2% |
| CALL | 532,989 | 8.8% |
| CALL_FUNCTION_EX | 337,960 | 5.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 337,840 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 1,465,658 | 24.3% |
| STORE_FAST | 1,382,940 | 22.9% |
| RETURN_VALUE | 675,900 | 11.2% |
| LOAD_FAST | 552,940 | 9.2% |
| BUILD_TUPLE | 204,780 | 3.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 204,800 | 45.3% |
| LOAD_FAST | 122,960 | 27.2% |
| LOAD_FAST_LOAD_FAST | 82,000 | 18.1% |
| RETURN_VALUE | 40,960 | 9.1% |
| STORE_SUBSCR | 1,380 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 204,860 | 45.3% |
| RETURN_CONST | 204,800 | 45.3% |
| LOAD_FAST | 20,560 | 4.5% |
| LOAD_CONST | 10,320 | 2.3% |
| LOAD_GLOBAL_BUILTIN | 10,200 | 2.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 486,480 | 64.4% |
| LOAD_ATTR_INSTANCE_VALUE | 133,500 | 17.7% |
| COPY | 62,560 | 8.3% |
| LOAD_ATTR | 22,100 | 2.9% |
| LOAD_FAST_CHECK | 20,520 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 423,940 | 56.1% |
| POP_JUMP_IF_TRUE | 319,660 | 42.3% |
| TO_BOOL | 4,920 | 0.7% |
| TO_BOOL_BOOL | 3,640 | 0.5% |
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
| LOAD_FAST_LOAD_FAST | 245,880 | 48.8% |
| BUILD_TUPLE | 143,400 | 28.4% |
| LOAD_FAST | 61,780 | 12.2% |
| LOAD_CONST | 51,860 | 10.3% |
| BINARY_OP | 1,060 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 297,180 | 58.9% |
| RETURN_VALUE | 143,420 | 28.4% |
| LOAD_FAST | 51,320 | 10.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 10,200 | 2.0% |
| BINARY_OP | 1,060 | 0.2% |


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
| FORMAT_SIMPLE | 61,440 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 20,480 | 33.3% |
| RETURN_VALUE | 10,240 | 16.7% |
| CALL | 10,240 | 16.7% |
| STORE_FAST | 10,240 | 16.7% |
| BINARY_OP_INPLACE_ADD_UNICODE | 10,200 | 16.6% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 430,200 | 31.8% |
| LOAD_FAST | 266,320 | 19.7% |
| RETURN_VALUE | 204,780 | 15.1% |
| LOAD_GLOBAL_BUILTIN | 163,680 | 12.1% |
| LOAD_GLOBAL_MODULE | 153,620 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 225,440 | 16.7% |
| LOAD_FAST | 225,280 | 16.7% |
| CALL | 164,300 | 12.2% |
| YIELD_VALUE | 163,840 | 12.1% |
| BINARY_OP | 143,400 | 10.6% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 946,120 | 26.9% |
| LOAD_FAST | 918,049 | 26.1% |
| LOAD_GLOBAL_MODULE | 307,820 | 8.7% |
| LOAD_FAST_LOAD_FAST | 288,060 | 8.2% |
| LOAD_ATTR_METHOD_NO_DICT | 278,000 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 687,940 | 19.5% |
| RETURN_VALUE | 532,989 | 15.1% |
| TO_BOOL_BOOL | 501,160 | 14.2% |
| POP_TOP | 451,980 | 12.8% |
| RESUME_CHECK | 319,480 | 9.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 307,280 | 44.8% |
| LOAD_FAST | 286,800 | 41.8% |
| CALL_INTRINSIC_1 | 51,280 | 7.5% |
| RETURN_VALUE | 40,960 | 6.0% |

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
| LOAD_CONST | 686,360 | 100.0% |

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
| LOAD_CONST | 278,840 | 61.1% |
| LOAD_FAST | 92,400 | 20.2% |
| LOAD_GLOBAL_MODULE | 41,080 | 9.0% |
| LOAD_FAST_LOAD_FAST | 20,600 | 4.5% |
| BUILD_LIST | 10,280 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 389,420 | 85.3% |
| POP_JUMP_IF_FALSE | 62,940 | 13.8% |
| COMPARE_OP | 2,260 | 0.5% |
| COMPARE_OP_INT | 1,160 | 0.3% |
| COMPARE_OP_STR | 660 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 553,360 | 41.2% |
| LOAD_FAST_LOAD_FAST | 399,400 | 29.8% |
| LOAD_GLOBAL_MODULE | 174,140 | 13.0% |
| LOAD_CONST | 133,120 | 9.9% |
| LOAD_ATTR_MODULE | 40,980 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 778,520 | 58.0% |
| POP_JUMP_IF_TRUE | 410,000 | 30.5% |
| STORE_FAST | 61,460 | 4.6% |
| EXTENDED_ARG | 40,960 | 3.1% |
| COPY | 20,480 | 1.5% |


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
| LOAD_FAST | 583,680 | 56.4% |
| RAISE_VARARGS | 71,680 | 6.9% |
| CALL_ISINSTANCE | 51,180 | 4.9% |
| LOAD_CONST | 41,000 | 4.0% |
| RETURN_VALUE | 40,960 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 234,940 | 22.7% |
| LOAD_ATTR_INSTANCE_VALUE | 173,880 | 16.8% |
| TO_BOOL_STR | 122,720 | 11.9% |
| TO_BOOL_BOOL | 122,640 | 11.9% |
| POP_EXCEPT | 92,160 | 8.9% |


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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 122,840 | 33.3% |
| TO_BOOL_STR | 41,940 | 11.4% |
| CONTAINS_OP | 40,960 | 11.1% |
| JUMP_BACKWARD | 40,960 | 11.1% |
| STORE_FAST | 40,960 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 245,760 | 66.7% |
| FOR_ITER | 51,280 | 13.9% |
| JUMP_BACKWARD | 40,960 | 11.1% |
| FOR_ITER_LIST | 20,400 | 5.5% |
| POP_JUMP_IF_TRUE | 10,260 | 2.8% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 445,000 | 47.6% |
| GET_ITER | 335,660 | 35.9% |
| LOAD_FAST | 71,840 | 7.7% |
| EXTENDED_ARG | 51,280 | 5.5% |
| SWAP | 21,420 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 320,760 | 34.3% |
| RETURN_CONST | 215,160 | 23.0% |
| STORE_FAST | 186,160 | 19.9% |
| LOAD_FAST | 123,900 | 13.3% |
| LOAD_CONST | 51,260 | 5.5% |


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
| LOAD_CONST | 194,560 | 44.1% |
| LOAD_GLOBAL_MODULE | 143,960 | 32.6% |
| LOAD_FAST_LOAD_FAST | 81,920 | 18.6% |
| LOAD_FAST | 20,500 | 4.6% |
| LOAD_GLOBAL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 297,720 | 67.5% |
| RETURN_VALUE | 61,440 | 13.9% |
| COPY | 40,960 | 9.3% |
| POP_JUMP_IF_TRUE | 30,740 | 7.0% |
| STORE_FAST | 10,240 | 2.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,024,120 | 31.7% |
| POP_JUMP_IF_TRUE | 952,800 | 29.5% |
| STORE_SUBSCR_DICT | 296,900 | 9.2% |
| STORE_FAST | 246,000 | 7.6% |
| STORE_SUBSCR | 204,860 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 888,180 | 27.5% |
| FOR_ITER_TUPLE | 819,640 | 25.4% |
| FOR_ITER_GEN | 511,000 | 15.8% |
| FOR_ITER | 445,000 | 13.8% |
| FOR_ITER_RANGE | 358,340 | 11.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 92,120 | 100.0% |
| RESUME | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 92,120 | 100.0% |
| SEND | 40 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 163,900 | 29.1% |
| LOAD_CONST | 81,920 | 14.5% |
| STORE_SUBSCR_LIST_INT | 51,180 | 9.1% |
| STORE_ATTR_INSTANCE_VALUE | 51,120 | 9.1% |
| FOR_ITER_GEN | 35,040 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 266,260 | 47.3% |
| STORE_FAST | 163,840 | 29.1% |
| LOAD_GLOBAL_MODULE | 91,960 | 16.3% |
| BUILD_MAP | 20,480 | 3.6% |
| LOAD_FAST_LOAD_FAST | 10,280 | 1.8% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40,960 | 49.7% |
| BUILD_TUPLE | 40,960 | 49.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 480 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 82,400 | 100.0% |


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
| LOAD_FAST | 2,109,954 | 75.0% |
| LOAD_ATTR_INSTANCE_VALUE | 298,360 | 10.6% |
| LOAD_ATTR | 133,696 | 4.8% |
| LOAD_GLOBAL_MODULE | 113,880 | 4.0% |
| RETURN_VALUE | 51,400 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 536,040 | 19.0% |
| PUSH_NULL | 451,160 | 16.0% |
| LOAD_CONST | 207,320 | 7.4% |
| STORE_FAST | 195,100 | 6.9% |
| CALL_PY_EXACT_ARGS | 183,720 | 6.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,513,940 | 26.8% |
| LOAD_ATTR_METHOD_NO_DICT | 1,719,180 | 13.1% |
| LOAD_CONST | 1,475,600 | 11.2% |
| POP_JUMP_IF_FALSE | 665,860 | 5.1% |
| STORE_ATTR_INSTANCE_VALUE | 603,220 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,741,600 | 13.3% |
| LOAD_CONST | 1,475,600 | 11.2% |
| CALL | 946,120 | 7.2% |
| COMPARE_OP_INT | 940,980 | 7.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 726,320 | 5.5% |


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
| STORE_FAST | 5,992,720 | 14.2% |
| RESUME_CHECK | 5,322,898 | 12.6% |
| POP_JUMP_IF_FALSE | 4,127,969 | 9.8% |
| LOAD_GLOBAL_BUILTIN | 3,879,200 | 9.2% |
| POP_JUMP_IF_TRUE | 2,191,620 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 6,412,100 | 15.2% |
| LOAD_ATTR_METHOD_NO_DICT | 4,280,280 | 10.2% |
| LOAD_CONST | 3,513,940 | 8.3% |
| STORE_ATTR_INSTANCE_VALUE | 2,257,600 | 5.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 2,257,400 | 5.4% |


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
| STORE_FAST | 1,259,720 | 17.4% |
| LOAD_GLOBAL_MODULE | 1,157,260 | 16.0% |
| STORE_ATTR_INSTANCE_VALUE | 992,740 | 13.7% |
| LOAD_FAST_LOAD_FAST | 788,620 | 10.9% |
| RESUME_CHECK | 511,780 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 1,472,000 | 20.3% |
| LOAD_FAST_LOAD_FAST | 788,620 | 10.9% |
| LOAD_FAST | 778,560 | 10.7% |
| CALL_PY_EXACT_ARGS | 459,980 | 6.3% |
| BUILD_TUPLE | 430,200 | 5.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,980 | 13.8% |
| STORE_FAST | 2,920 | 13.5% |
| POP_JUMP_IF_FALSE | 2,420 | 11.2% |
| RESUME_CHECK | 2,020 | 9.3% |
| RESUME | 1,940 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,760 | 31.3% |
| LOAD_FAST | 4,400 | 20.4% |
| LOAD_GLOBAL_BUILTIN | 4,200 | 19.4% |
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
| JUMP_BACKWARD | 30,720 | 100.0% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,988,218 | 37.7% |
| COMPARE_OP_INT | 1,023,540 | 12.9% |
| CONTAINS_OP | 778,520 | 9.8% |
| TO_BOOL_NONE | 612,380 | 7.7% |
| COMPARE_OP_STR | 450,220 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,127,969 | 52.1% |
| RETURN_CONST | 788,840 | 9.9% |
| LOAD_CONST | 665,860 | 8.4% |
| LOAD_GLOBAL_MODULE | 664,580 | 8.4% |
| LOAD_GLOBAL_BUILTIN | 521,880 | 6.6% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 583,840 | 80.3% |
| LOAD_ATTR_INSTANCE_VALUE | 71,620 | 9.8% |
| LOAD_ATTR | 51,340 | 7.1% |
| LOAD_DEREF | 10,240 | 1.4% |
| CALL_BUILTIN_FAST | 10,220 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 379,000 | 52.1% |
| LOAD_CONST | 81,940 | 11.3% |
| LOAD_GLOBAL_BUILTIN | 81,700 | 11.2% |
| LOAD_FAST_LOAD_FAST | 61,440 | 8.4% |
| JUMP_BACKWARD | 40,960 | 5.6% |


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
| TO_BOOL_BOOL | 1,432,920 | 28.8% |
| TO_BOOL_STR | 809,060 | 16.3% |
| TO_BOOL_NONE | 428,500 | 8.6% |
| CONTAINS_OP | 410,000 | 8.3% |
| COMPARE_OP_STR | 399,260 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,191,620 | 44.1% |
| JUMP_BACKWARD | 952,800 | 19.2% |
| LOAD_GLOBAL_BUILTIN | 337,740 | 6.8% |
| LOAD_CONST | 327,720 | 6.6% |
| LOAD_GLOBAL_MODULE | 327,140 | 6.6% |


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
| POP_TOP | 809,360 | 22.4% |
| POP_JUMP_IF_FALSE | 788,840 | 21.8% |
| STORE_ATTR_INSTANCE_VALUE | 583,180 | 16.1% |
| FOR_ITER | 215,160 | 6.0% |
| CALL_LIST_APPEND | 215,000 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,587,560 | 43.9% |
| INTERPRETER_EXIT | 1,137,420 | 31.5% |
| TO_BOOL_BOOL | 378,660 | 10.5% |
| END_FOR | 194,480 | 5.4% |
| EXIT_INIT_CHECK | 173,900 | 4.8% |


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

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 10,220 | 99.8% |
| CALL | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,240 | 100.0% |


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
| LOAD_FAST | 436,140 | 60.9% |
| LOAD_FAST_LOAD_FAST | 228,380 | 31.9% |
| SWAP | 31,000 | 4.3% |
| STORE_ATTR | 10,460 | 1.5% |
| LOAD_GLOBAL_MODULE | 10,220 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 216,040 | 30.2% |
| LOAD_CONST | 144,400 | 20.2% |
| RETURN_CONST | 113,260 | 15.8% |
| LOAD_FAST_LOAD_FAST | 103,240 | 14.4% |
| LOAD_GLOBAL_MODULE | 91,800 | 12.8% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,382,940 | 13.3% |
| FOR_ITER_TUPLE | 819,200 | 7.9% |
| CALL | 687,940 | 6.6% |
| STORE_FAST_STORE_FAST | 634,960 | 6.1% |
| LOAD_CONST | 604,620 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,992,720 | 57.5% |
| LOAD_FAST_LOAD_FAST | 1,259,720 | 12.1% |
| LOAD_GLOBAL_BUILTIN | 941,200 | 9.0% |
| LOAD_GLOBAL_MODULE | 879,480 | 8.4% |
| LOAD_CONST | 307,540 | 2.9% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 40,920 | 66.1% |
| FOR_ITER | 20,520 | 33.1% |
| FOR_ITER_TUPLE | 480 | 0.8% |
| COPY | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 30,720 | 49.6% |
| LOAD_ATTR_METHOD_NO_DICT | 30,660 | 49.5% |
| TO_BOOL_STR | 480 | 0.8% |
| LOAD_ATTR | 80 | 0.1% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,044,440 | 48.8% |
| UNPACK_SEQUENCE_TUPLE | 532,260 | 24.9% |
| STORE_FAST_STORE_FAST | 256,000 | 12.0% |
| UNPACK_SEQUENCE | 113,360 | 5.3% |
| POP_TOP | 81,920 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 952,520 | 44.5% |
| STORE_FAST | 634,960 | 29.7% |
| STORE_FAST_STORE_FAST | 256,000 | 12.0% |
| LOAD_FAST_LOAD_FAST | 174,080 | 8.1% |
| LOAD_GLOBAL_BUILTIN | 51,160 | 2.4% |


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
| LOAD_FAST | 297,000 | 28.1% |
| LOAD_FAST_AND_CLEAR | 194,780 | 18.5% |
| BINARY_OP_ADD_INT | 173,960 | 16.5% |
| BUILD_LIST | 153,820 | 14.6% |
| FOR_ITER_LIST | 81,920 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 173,880 | 16.5% |
| BUILD_LIST | 153,820 | 14.6% |
| LOAD_CONST | 122,920 | 11.6% |
| FOR_ITER_LIST | 102,280 | 9.7% |
| POP_EXCEPT | 92,180 | 8.7% |


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
| LOAD_FAST | 215,040 | 27.6% |
| BUILD_TUPLE | 163,840 | 21.1% |
| RETURN_VALUE | 122,880 | 15.8% |
| YIELD_VALUE | 92,160 | 11.8% |
| COMPARE_OP_STR | 51,180 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 388,960 | 50.0% |
| INTERPRETER_EXIT | 216,000 | 27.8% |
| YIELD_VALUE | 92,160 | 11.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 81,120 | 10.4% |
| UNPACK_SEQUENCE | 40 | 0.0% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 3,300 | 50.8% |
| CACHE | 1,800 | 27.7% |
| CALL_KW | 480 | 7.4% |
| POP_TOP | 340 | 5.2% |
| COPY_FREE_VARS | 320 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,200 | 49.2% |
| LOAD_GLOBAL | 1,940 | 29.8% |
| LOAD_CONST | 300 | 4.6% |
| LOAD_FAST_LOAD_FAST | 300 | 4.6% |
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
| LOAD_CONST | 460,520 | 90.0% |
| CALL_LEN | 30,640 | 6.0% |
| LOAD_FAST_LOAD_FAST | 20,440 | 4.0% |
| BINARY_OP | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SLICE | 245,740 | 48.0% |
| SWAP | 173,960 | 34.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 61,360 | 12.0% |
| STORE_FAST | 20,460 | 4.0% |
| LOAD_CONST | 10,280 | 2.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 255,800 | 60.9% |
| CALL_METHOD_DESCRIPTOR_O | 40,920 | 9.7% |
| RETURN_VALUE | 40,880 | 9.7% |
| LOAD_CONST | 40,880 | 9.7% |
| BINARY_SLICE | 20,480 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 163,920 | 39.0% |
| RETURN_VALUE | 81,900 | 19.5% |
| STORE_FAST | 81,900 | 19.5% |
| STORE_SUBSCR_DICT | 51,160 | 12.2% |
| COPY | 20,480 | 4.9% |


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
| LOAD_FAST | 20,440 | 28.6% |
| LOAD_FAST_LOAD_FAST | 20,440 | 28.6% |
| CALL_LEN | 20,400 | 28.5% |
| LOAD_CONST | 10,200 | 14.2% |
| BINARY_OP | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 51,120 | 71.4% |
| STORE_FAST | 20,460 | 28.6% |


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
| LOAD_CONST | 153,440 | 75.0% |
| LOAD_FAST_LOAD_FAST | 51,160 | 25.0% |
| BINARY_SUBSCR | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 51,180 | 25.0% |
| LOAD_ATTR_METHOD_NO_DICT | 51,120 | 25.0% |
| YIELD_VALUE | 40,940 | 20.0% |
| RETURN_VALUE | 30,700 | 15.0% |
| TO_BOOL_STR | 30,680 | 15.0% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,920 | 99.9% |
| BINARY_SUBSCR | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40,940 | 99.9% |
| LOAD_ATTR | 40 | 0.1% |


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
| LOAD_FAST | 40,880 | 23.5% |
| LOAD_GLOBAL_MODULE | 40,800 | 23.5% |
| LOAD_FAST_LOAD_FAST | 30,720 | 17.7% |
| LOAD_ATTR_INSTANCE_VALUE | 30,600 | 17.6% |
| LOAD_ATTR | 20,440 | 11.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 173,900 | 100.0% |


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
| LOAD_FAST | 245,440 | 40.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 102,240 | 16.9% |
| LOAD_ATTR_INSTANCE_VALUE | 81,800 | 13.5% |
| CALL_LEN | 51,120 | 8.5% |
| CALL | 31,220 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 255,880 | 42.4% |
| STORE_FAST | 153,480 | 25.4% |
| RETURN_VALUE | 81,880 | 13.6% |
| LOAD_FAST | 61,400 | 10.2% |
| COPY | 30,680 | 5.1% |


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
| LOAD_FAST | 41,100 | 99.8% |
| LOAD_CONST | 60 | 0.1% |
| CALL_STR_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,540 | 49.9% |
| PUSH_EXC_INFO | 20,480 | 49.7% |
| RETURN_VALUE | 140 | 0.3% |
| BEFORE_WITH | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 255,960 | 78.1% |
| RETURN_GENERATOR | 51,160 | 15.6% |
| BUILD_TUPLE | 10,240 | 3.1% |
| BUILD_LIST | 10,200 | 3.1% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 255,980 | 78.1% |
| TO_BOOL_BOOL | 61,360 | 18.7% |
| RETURN_VALUE | 10,240 | 3.1% |
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
| LOAD_FAST | 439,680 | 56.5% |
| LOAD_ATTR_INSTANCE_VALUE | 266,180 | 34.2% |
| LOAD_ATTR | 40,800 | 5.2% |
| BINARY_SUBSCR | 20,440 | 2.6% |
| LOAD_ATTR_SLOT | 10,200 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 266,180 | 34.2% |
| LOAD_CONST | 143,360 | 18.4% |
| LOAD_GLOBAL_MODULE | 112,520 | 14.5% |
| CALL_BUILTIN_CLASS | 51,120 | 6.6% |
| LOAD_FAST | 40,880 | 5.3% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 388,880 | 88.3% |
| BUILD_TUPLE | 51,120 | 11.6% |
| CALL | 260 | 0.1% |
| LOAD_CONST | 20 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 215,000 | 48.8% |
| JUMP_BACKWARD | 143,300 | 32.5% |
| LOAD_GLOBAL_BUILTIN | 51,160 | 11.6% |
| LOAD_FAST | 20,500 | 4.7% |
| LOAD_FAST_LOAD_FAST | 10,220 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 408,760 | 42.0% |
| LOAD_ATTR_METHOD_NO_DICT | 255,660 | 26.3% |
| LOAD_FAST | 122,660 | 12.6% |
| BINARY_OP_ADD_INT | 61,360 | 6.3% |
| LOAD_FAST_LOAD_FAST | 40,920 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 245,600 | 25.2% |
| POP_TOP | 235,320 | 24.2% |
| RETURN_VALUE | 153,520 | 15.8% |
| LOAD_FAST | 112,580 | 11.6% |
| BUILD_TUPLE | 81,880 | 8.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 726,320 | 59.6% |
| LOAD_ATTR_METHOD_NO_DICT | 460,520 | 37.8% |
| LOAD_FAST | 20,400 | 1.7% |
| LOAD_FAST_LOAD_FAST | 10,200 | 0.8% |
| CALL | 700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,840 | 27.7% |
| LOAD_FAST | 245,740 | 20.2% |
| STORE_FAST | 235,480 | 19.3% |
| POP_TOP | 122,820 | 10.1% |
| GET_ITER | 61,380 | 5.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,970,360 | 87.8% |
| LOAD_ATTR_METHOD_LAZY_DICT | 168,600 | 7.5% |
| LOAD_ATTR | 50,978 | 2.3% |
| LOAD_SUPER_ATTR_METHOD | 30,640 | 1.4% |
| LOAD_FAST | 20,420 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 511,820 | 22.8% |
| STORE_FAST | 441,940 | 19.7% |
| GET_ITER | 229,100 | 10.2% |
| STORE_SUBSCR | 204,800 | 9.1% |
| BINARY_SUBSCR | 184,320 | 8.2% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 337,760 | 41.2% |
| LOAD_FAST | 306,640 | 37.4% |
| BINARY_SLICE | 92,080 | 11.2% |
| STORE_FAST | 41,140 | 5.0% |
| LOAD_ATTR_INSTANCE_VALUE | 20,420 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 399,120 | 48.7% |
| POP_TOP | 122,720 | 15.0% |
| RETURN_VALUE | 112,780 | 13.8% |
| STORE_FAST | 61,440 | 7.5% |
| LOAD_CONST | 51,260 | 6.3% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,615,260 | 38.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,093,260 | 26.0% |
| LOAD_FAST_LOAD_FAST | 459,980 | 10.9% |
| LOAD_ATTR | 183,720 | 4.4% |
| GET_ITER | 163,620 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,596,020 | 85.5% |
| COPY_FREE_VARS | 348,020 | 8.3% |
| RETURN_GENERATOR | 235,360 | 5.6% |
| MAKE_CELL | 10,260 | 0.2% |
| STORE_FAST | 8,320 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 235,400 | 24.5% |
| LOAD_CONST | 235,080 | 24.4% |
| LOAD_FAST | 183,920 | 19.1% |
| LOAD_ATTR_INSTANCE_VALUE | 132,680 | 13.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 61,320 | 6.4% |

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
| LOAD_CONST | 940,980 | 67.1% |
| LOAD_GLOBAL_MODULE | 132,960 | 9.5% |
| LOAD_ATTR_INSTANCE_VALUE | 122,760 | 8.8% |
| CALL | 40,920 | 2.9% |
| COPY | 40,840 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,023,540 | 73.0% |
| POP_JUMP_IF_TRUE | 215,060 | 15.3% |
| EXTENDED_ARG | 122,840 | 8.8% |
| STORE_FAST | 40,960 | 2.9% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 439,600 | 47.7% |
| LOAD_FAST | 348,100 | 37.8% |
| LOAD_GLOBAL_MODULE | 132,920 | 14.4% |
| COMPARE_OP | 660 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 450,220 | 48.9% |
| POP_JUMP_IF_TRUE | 399,260 | 43.3% |
| YIELD_VALUE | 51,180 | 5.6% |
| EXTENDED_ARG | 20,440 | 2.2% |
| COMPARE_OP | 180 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 511,000 | 67.1% |
| GET_ITER | 167,960 | 22.0% |
| SWAP | 70,860 | 9.3% |
| LOAD_FAST | 10,220 | 1.3% |
| FOR_ITER | 2,060 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 470,580 | 61.7% |
| POP_TOP | 193,960 | 25.5% |
| STORE_FAST | 60,640 | 8.0% |
| JUMP_FORWARD | 35,040 | 4.6% |
| FOR_ITER | 1,820 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 888,180 | 58.7% |
| GET_ITER | 479,860 | 31.7% |
| SWAP | 102,280 | 6.8% |
| LOAD_FAST | 20,420 | 1.3% |
| EXTENDED_ARG | 20,400 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 509,220 | 33.7% |
| STORE_FAST | 419,880 | 27.8% |
| LOAD_FAST | 234,560 | 15.5% |
| RETURN_CONST | 133,060 | 8.8% |
| SWAP | 81,920 | 5.4% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 358,340 | 85.4% |
| GET_ITER | 61,420 | 14.6% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 358,340 | 85.4% |
| LOAD_FAST | 41,040 | 9.8% |
| LOAD_CONST | 20,460 | 4.9% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 819,640 | 76.9% |
| GET_ITER | 184,340 | 17.3% |
| LOAD_FAST | 61,400 | 5.8% |
| SWAP | 220 | 0.0% |
| FOR_ITER | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 819,200 | 76.9% |
| LOAD_FAST | 184,360 | 17.3% |
| RETURN_CONST | 61,460 | 5.8% |
| STORE_FAST_LOAD_FAST | 480 | 0.0% |
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
| LOAD_FAST | 6,412,100 | 92.0% |
| LOAD_FAST_LOAD_FAST | 234,960 | 3.4% |
| COPY | 173,880 | 2.5% |
| LOAD_ATTR_INSTANCE_VALUE | 91,960 | 1.3% |
| LOAD_DEREF | 51,000 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,258,840 | 18.1% |
| LOAD_ATTR_METHOD_NO_DICT | 1,186,740 | 17.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 603,480 | 8.7% |
| LOAD_CONST | 439,960 | 6.3% |
| STORE_FAST | 358,260 | 5.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 234,840 | 67.8% |
| LOAD_FAST | 110,520 | 31.9% |
| LOAD_ATTR | 460 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 168,600 | 48.7% |
| LOAD_CONST | 61,320 | 17.7% |
| LOAD_FAST | 51,120 | 14.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 40,800 | 11.8% |
| LOAD_GLOBAL_MODULE | 21,200 | 6.1% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,280,280 | 64.1% |
| LOAD_ATTR_INSTANCE_VALUE | 1,186,740 | 17.8% |
| LOAD_GLOBAL_MODULE | 347,820 | 5.2% |
| LOAD_CONST | 276,080 | 4.1% |
| LOAD_FAST_LOAD_FAST | 81,840 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,970,360 | 29.5% |
| LOAD_CONST | 1,719,180 | 25.7% |
| LOAD_FAST | 1,597,089 | 23.9% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 460,520 | 6.9% |
| CALL | 278,000 | 4.2% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,257,400 | 73.1% |
| LOAD_ATTR_INSTANCE_VALUE | 603,480 | 19.5% |
| LOAD_ATTR | 125,340 | 4.1% |
| LOAD_ATTR_MODULE | 71,440 | 2.3% |
| LOAD_GLOBAL_MODULE | 20,420 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,093,260 | 35.4% |
| LOAD_FAST | 787,480 | 25.5% |
| LOAD_CONST | 470,600 | 15.2% |
| LOAD_FAST_LOAD_FAST | 409,280 | 13.3% |
| CALL_PY_WITH_DEFAULTS | 235,400 | 7.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 685,820 | 92.9% |
| LOAD_ATTR_MODULE | 51,080 | 6.9% |
| LOAD_ATTR | 1,140 | 0.2% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 317,360 | 43.0% |
| CALL_ISINSTANCE | 91,920 | 12.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 71,440 | 9.7% |
| LOAD_FAST | 61,540 | 8.3% |
| LOAD_ATTR_MODULE | 51,080 | 6.9% |


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
| LOAD_FAST_LOAD_FAST | 163,800 | 51.6% |
| LOAD_FAST | 132,860 | 41.8% |
| COPY | 20,400 | 6.4% |
| LOAD_ATTR_MODULE | 280 | 0.1% |
| LOAD_ATTR | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 164,080 | 51.7% |
| LOAD_CONST | 40,980 | 12.9% |
| GET_ITER | 40,940 | 12.9% |
| GET_YIELD_FROM_ITER | 20,460 | 6.4% |
| PUSH_NULL | 10,220 | 3.2% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,626,740 | 26.8% |
| STORE_FAST | 941,200 | 15.5% |
| LOAD_FAST | 859,380 | 14.2% |
| POP_JUMP_IF_FALSE | 521,880 | 8.6% |
| POP_JUMP_IF_TRUE | 337,740 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,879,200 | 64.0% |
| CALL_ISINSTANCE | 972,140 | 16.0% |
| LOAD_DEREF | 276,240 | 4.6% |
| CHECK_EXC_MATCH | 255,980 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 183,940 | 3.0% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,320,120 | 20.2% |
| RESUME_CHECK | 1,259,240 | 19.2% |
| STORE_FAST | 879,480 | 13.4% |
| POP_JUMP_IF_FALSE | 664,580 | 10.2% |
| STORE_ATTR_INSTANCE_VALUE | 367,700 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,678,500 | 25.7% |
| LOAD_FAST_LOAD_FAST | 1,157,260 | 17.7% |
| LOAD_ATTR_MODULE | 685,820 | 10.5% |
| CALL_ISINSTANCE | 490,860 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 347,820 | 5.3% |


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
| CALL_PY_EXACT_ARGS | 3,596,020 | 34.6% |
| CACHE | 2,511,258 | 24.1% |
| CALL_PY_WITH_DEFAULTS | 951,440 | 9.1% |
| COPY_FREE_VARS | 583,520 | 5.6% |
| FOR_ITER_GEN | 470,580 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,322,898 | 51.2% |
| LOAD_GLOBAL_BUILTIN | 1,626,740 | 15.6% |
| LOAD_GLOBAL_MODULE | 1,259,240 | 12.1% |
| POP_TOP | 685,880 | 6.6% |
| NOP | 542,580 | 5.2% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 92,120 | 75.0% |
| LOAD_CONST | 30,680 | 25.0% |
| SEND | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 92,120 | 75.0% |
| POP_TOP | 30,680 | 25.0% |
| RESUME | 40 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,257,600 | 57.2% |
| LOAD_FAST_LOAD_FAST | 1,472,000 | 37.3% |
| SWAP | 173,880 | 4.4% |
| LOAD_ATTR_INSTANCE_VALUE | 30,640 | 0.8% |
| LOAD_DEREF | 10,200 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 992,740 | 25.1% |
| LOAD_FAST | 972,140 | 24.6% |
| LOAD_CONST | 603,220 | 15.3% |
| RETURN_CONST | 583,180 | 14.8% |
| LOAD_GLOBAL_MODULE | 367,700 | 9.3% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 81,820 | 46.9% |
| LOAD_FAST | 71,460 | 41.0% |
| SWAP | 20,400 | 11.7% |
| STORE_ATTR_SLOT | 500 | 0.3% |
| STORE_ATTR | 240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 71,660 | 41.1% |
| LOAD_FAST | 40,920 | 23.5% |
| LOAD_FAST_LOAD_FAST | 30,660 | 17.6% |
| LOAD_CONST | 20,460 | 11.7% |
| LOAD_GLOBAL_BUILTIN | 10,200 | 5.8% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 235,480 | 62.2% |
| LOAD_CONST | 71,400 | 18.9% |
| BINARY_OP_ADD_UNICODE | 51,160 | 13.5% |
| LOAD_FAST | 10,240 | 2.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 10,200 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 296,900 | 78.4% |
| LOAD_FAST | 40,900 | 10.8% |
| LOAD_CONST | 30,660 | 8.1% |
| LOAD_FAST_LOAD_FAST | 10,220 | 2.7% |
| NOP | 40 | 0.0% |


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
| LOAD_FAST | 80,700 | 20.7% |
| TO_BOOL_NONE | 400 | 0.1% |
| TO_BOOL | 340 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 297,480 | 76.5% |
| POP_JUMP_IF_FALSE | 91,100 | 23.4% |
| TO_BOOL_NONE | 400 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 1,411,340 | 31.7% |
| LOAD_FAST | 1,114,820 | 25.0% |
| CALL | 501,160 | 11.3% |
| RETURN_CONST | 378,660 | 8.5% |
| CALL_BUILTIN_FAST | 337,380 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,988,218 | 67.1% |
| POP_JUMP_IF_TRUE | 1,432,920 | 32.2% |
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
| LOAD_FAST | 538,840 | 50.7% |
| COPY | 234,940 | 22.1% |
| LOAD_ATTR_INSTANCE_VALUE | 102,040 | 9.6% |
| CALL | 101,320 | 9.5% |
| LOAD_ATTR | 61,580 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 612,380 | 57.7% |
| POP_JUMP_IF_TRUE | 428,500 | 40.3% |
| EXTENDED_ARG | 19,460 | 1.8% |
| TO_BOOL_STR | 1,400 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 400 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,118,600 | 86.4% |
| COPY | 122,720 | 9.5% |
| BINARY_SUBSCR_LIST_INT | 30,680 | 2.4% |
| STORE_FAST | 20,400 | 1.6% |
| TO_BOOL_NONE | 1,400 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 809,060 | 62.5% |
| POP_JUMP_IF_FALSE | 442,820 | 34.2% |
| EXTENDED_ARG | 41,940 | 3.2% |
| TO_BOOL_NONE | 1,460 | 0.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 51,120 | 99.9% |
| UNPACK_SEQUENCE | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 51,160 | 100.0% |


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
| FOR_ITER_LIST | 509,220 | 46.5% |
| FOR_ITER | 320,760 | 29.3% |
| LOAD_FAST | 92,040 | 8.4% |
| YIELD_VALUE | 81,120 | 7.4% |
| CALL | 40,920 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,044,440 | 95.3% |
| STORE_FAST | 40,940 | 3.7% |
| LOAD_FAST | 10,220 | 0.9% |


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
|     deferred | 502,600 | 31.8% |
|          hit | 1,074,940 | 68.1% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 720 | 40.9% |
| Failure | 1,040 | 59.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 780 | 75.0% |
| add different types | 260 | 25.0% |


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
|     deferred | 255,860 | 13.8% |
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
|     deferred | 3,481,709 | 18.1% |
|          hit | 15,496,680 | 80.6% |
|         miss | 207,998 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,280 | 41.7% |
| Failure | 22,779 | 58.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 3,820 | 16.8% |
| code complex parameters | 3,620 | 15.9% |
| meth descr method fastcall keywords | 2,520 | 11.1% |
| class no vectorcall | 2,480 | 10.9% |
| cfunc noargs | 1,680 | 7.4% |
| meth descr varargs keywords | 1,459 | 6.4% |
| cfunc varargs keywords | 1,100 | 4.8% |
| wrong number arguments | 1,040 | 4.6% |
| init not simple | 1,000 | 4.4% |
| no dict | 860 | 3.8% |
| operator wrapper | 840 | 3.7% |
| class mutable | 580 | 2.5% |
| other | 540 | 2.4% |
| cfunc varargs | 500 | 2.2% |
| cmethod | 400 | 1.8% |
| method wrapper | 180 | 0.8% |
| str | 160 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 452,320 | 16.3% |
|          hit | 2,313,500 | 83.2% |
|         miss | 10,240 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,820 | 42.7% |
| Failure | 2,440 | 57.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 1,300 | 53.3% |
| big int | 340 | 13.9% |
| bytes | 260 | 10.7% |
| bool | 220 | 9.0% |
| list | 160 | 6.6% |
| set | 160 | 6.6% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 921,380 | 19.6% |
|          hit | 3,613,500 | 77.0% |
|         miss | 146,860 | 3.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,820 | 29.7% |
| Failure | 9,040 | 70.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 3,760 | 41.6% |
| dict keys | 3,480 | 38.5% |
| dict items | 540 | 6.0% |
| enumerate | 420 | 4.6% |
| dict values | 380 | 4.2% |
| reversed list | 200 | 2.2% |
| set | 180 | 2.0% |
| ascii string | 80 | 0.9% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 2,768,134 | 12.9% |
|          hit | 18,528,409 | 86.4% |
|         miss | 111,680 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 17,500 | 37.6% |
| Failure | 28,996 | 62.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 22,016 | 75.9% |
| method | 2,260 | 7.8% |
| metaclass attribute | 1,060 | 3.7% |
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
|     deferred | 11,440 | 0.1% |
|        deopt | 800 | 0.0% |
|          hit | 12,600,960 | 99.8% |
|         miss | 2,080 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,980 | 100.0% |
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
|     deferred | 40 | 0.0% |
|          hit | 122,840 | 99.9% |

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
|     deferred | 700,060 | 14.5% |
|          hit | 4,083,440 | 84.4% |
|         miss | 40,400 | 0.8% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,840 | 35.8% |
| Failure | 10,460 | 64.2% |

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
|     deferred | 450,820 | 51.1% |
|          hit | 429,940 | 48.7% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 15.9% |
| Failure | 1,380 | 84.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 800 | 58.0% |
| other | 580 | 42.0% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 740,040 | 8.8% |
|          hit | 7,437,198 | 88.6% |
|         miss | 201,020 | 2.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 10,280 | 67.6% |
| Failure | 4,920 | 32.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 1,960 | 39.8% |
| dict | 1,200 | 24.4% |
| sequence | 780 | 15.9% |
| set | 320 | 6.5% |
| tuple | 320 | 6.5% |
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
| Basic | 115,314,786 | 52.0% |
| Not specialized | 26,007,876 | 11.7% |
| Specialized hits | 79,501,185 | 35.9% |
| Specialized misses | 762,638 | 0.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 3,481,709 | 33.5% |
| LOAD_ATTR | 2,768,134 | 26.6% |
| FOR_ITER | 921,380 | 8.9% |
| TO_BOOL | 740,040 | 7.1% |
| STORE_ATTR | 700,060 | 6.7% |
| BINARY_OP | 502,600 | 4.8% |
| COMPARE_OP | 452,320 | 4.4% |
| STORE_SUBSCR | 450,820 | 4.3% |
| BINARY_SUBSCR | 255,860 | 2.5% |
| UNPACK_SEQUENCE | 113,420 | 1.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 109,678 | 14.4% |
| TO_BOOL_NONE | 98,680 | 12.9% |
| FOR_ITER_GEN | 97,500 | 12.8% |
| TO_BOOL_STR | 80,400 | 10.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 51,000 | 6.7% |
| FOR_ITER_LIST | 49,360 | 6.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 31,360 | 4.1% |
| CALL_METHOD_DESCRIPTOR_O | 31,220 | 4.1% |
| LOAD_ATTR_METHOD_LAZY_DICT | 29,040 | 3.8% |
| STORE_ATTR_SLOT | 26,920 | 3.5% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 2,933,598 | 27.1% |
| Calls to Python functions inlined | 7,873,720 | 72.9% |
| Calls via PyEval_EvalFrame (total) | 2,933,598 | 27.1% |
| Calls via PyEval_EvalFrame (vector) | 2,553,638 | 23.6% |
| Calls via PyEval_EvalFrame (generator) | 379,960 | 3.5% |
| Calls via PyEval_EvalFrame (legacy) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,553,558 | 23.6% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 451,940 | 4.2% |
| Calls via PyEval_EvalFrame (function ex) | 102,580 | 0.9% |
| Calls via PyEval_EvalFrame (api) | 287,280 | 2.7% |
| Calls via PyEval_EvalFrame (method) | 71,578 | 0.7% |
| Frame objects created | 389,200 | 3.6% |
| Frames pushed | 6,316,580 | 58.4% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 8,838,069 | 37.2% |
| Frees to freelist | 8,840,389 |  |
| Allocations | 14,938,818 | 62.8% |
| Allocations to 512 bytes | 14,846,358 | 62.4% |
| Allocations to 4 kbytes | 82,180 | 0.3% |
| Allocations over 4 kbytes | 10,280 | 0.0% |
| Frees | 15,721,470 |  |
| New values | 348,560 |  |
| Interpreter increfs | 97,286,195 | 73.9% |
| Interpreter decrefs | 112,349,802 | 73.6% |
| Increfs | 34,313,215 | 26.1% |
| Decrefs | 40,242,390 | 26.4% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 20 | 0.0% |
| Method cache hits | 5,033,823 |  |
| Method cache misses | 173,612 |  |
| Method cache collisions | 310,634 |  |
| Method cache dunder hits | 3,944,572 |  |
| Method cache dunder misses | 143,628 |  |


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
