
# Pystats results

- benchmark: flaskblogging
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 9,730,709 | 19.1% | 19.1% |  |
| LOAD_CONST | 2,859,300 | 5.6% | 24.7% |  |
| RESUME_CHECK | 2,563,554 | 5.0% | 29.8% |  |
| STORE_FAST | 2,162,380 | 4.2% | 34.0% |  |
| POP_JUMP_IF_FALSE | 1,833,454 | 3.6% | 37.6% |  |
| LOAD_ATTR_INSTANCE_VALUE | 1,751,980 | 3.4% | 41.1% | 0.0% |
| LOAD_GLOBAL_MODULE | 1,590,620 | 3.1% | 44.2% | 0.0% |
| LOAD_FAST_LOAD_FAST | 1,537,040 | 3.0% | 47.2% |  |
| RETURN_VALUE | 1,500,754 | 2.9% | 50.2% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,460,507 | 2.9% | 53.0% | 0.3% |
| LOAD_GLOBAL_BUILTIN | 1,443,100 | 2.8% | 55.9% | 0.1% |
| POP_TOP | 1,320,254 | 2.6% | 58.5% |  |
| TO_BOOL_BOOL | 1,116,514 | 2.2% | 60.6% |  |
| CALL_PY_EXACT_ARGS | 1,033,320 | 2.0% | 62.7% | 0.3% |
| POP_JUMP_IF_TRUE | 1,022,820 | 2.0% | 64.7% |  |
| STORE_ATTR_INSTANCE_VALUE | 997,880 | 2.0% | 66.6% | 0.3% |
| CALL | 914,507 | 1.8% | 68.4% |  |
| RETURN_CONST | 899,600 | 1.8% | 70.2% |  |
| INTERPRETER_EXIT | 739,334 | 1.5% | 71.7% |  |
| LOAD_ATTR | 734,582 | 1.4% | 73.1% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 701,000 | 1.4% | 74.5% | 0.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 504,314 | 1.0% | 75.5% | 6.0% |
| CALL_ISINSTANCE | 426,680 | 0.8% | 76.3% |  |
| STORE_FAST_STORE_FAST | 411,580 | 0.8% | 77.1% |  |
| GET_ITER | 410,300 | 0.8% | 77.9% |  |
| ENTER_EXECUTOR | 393,720 | 0.8% | 78.7% |  |
| BUILD_TUPLE | 330,820 | 0.6% | 79.4% |  |
| NOP | 328,867 | 0.6% | 80.0% |  |
| TO_BOOL_STR | 296,020 | 0.6% | 80.6% | 6.9% |
| POP_JUMP_IF_NOT_NONE | 287,540 | 0.6% | 81.1% |  |
| COMPARE_OP_INT | 287,280 | 0.6% | 81.7% |  |
| PUSH_NULL | 283,220 | 0.6% | 82.3% |  |
| FOR_ITER_LIST | 277,100 | 0.5% | 82.8% | 4.5% |
| TO_BOOL_NONE | 272,780 | 0.5% | 83.3% | 8.7% |
| SWAP | 262,240 | 0.5% | 83.9% |  |
| COPY | 256,480 | 0.5% | 84.4% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 245,860 | 0.5% | 84.8% |  |
| CALL_PY_WITH_DEFAULTS | 244,820 | 0.5% | 85.3% |  |
| JUMP_FORWARD | 217,740 | 0.4% | 85.8% |  |
| CALL_BUILTIN_FAST | 202,620 | 0.4% | 86.2% |  |
| TO_BOOL | 198,840 | 0.4% | 86.5% |  |
| STORE_ATTR | 196,640 | 0.4% | 86.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 195,100 | 0.4% | 87.3% | 4.0% |
| BUILD_LIST | 192,620 | 0.4% | 87.7% |  |
| CONTAINS_OP | 189,200 | 0.4% | 88.1% |  |
| FOR_ITER_GEN | 186,200 | 0.4% | 88.4% | 12.9% |
| LOAD_ATTR_MODULE | 182,940 | 0.4% | 88.8% | 0.0% |
| POP_JUMP_IF_NONE | 179,240 | 0.4% | 89.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 177,800 | 0.3% | 89.5% | 2.9% |
| CALL_LEN | 177,100 | 0.3% | 89.8% |  |
| YIELD_VALUE | 174,120 | 0.3% | 90.2% |  |
| CALL_KW | 171,800 | 0.3% | 90.5% |  |
| CALL_FUNCTION_EX | 171,760 | 0.3% | 90.9% |  |
| JUMP_BACKWARD | 171,380 | 0.3% | 91.2% |  |
| LOAD_DEREF | 164,280 | 0.3% | 91.5% |  |
| BUILD_MAP | 163,920 | 0.3% | 91.8% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 157,320 | 0.3% | 92.1% |  |
| UNPACK_SEQUENCE_TUPLE | 153,360 | 0.3% | 92.5% |  |
| COMPARE_OP_STR | 149,080 | 0.3% | 92.7% | 1.7% |
| COPY_FREE_VARS | 148,680 | 0.3% | 93.0% |  |
| CALL_BUILTIN_CLASS | 148,240 | 0.3% | 93.3% |  |
| BINARY_SUBSCR_TUPLE_INT | 138,220 | 0.3% | 93.6% |  |
| FOR_ITER_TUPLE | 125,380 | 0.2% | 93.8% |  |
| FOR_ITER | 122,920 | 0.2% | 94.1% |  |
| CALL_LIST_APPEND | 110,060 | 0.2% | 94.3% |  |
| STORE_SUBSCR | 106,680 | 0.2% | 94.5% |  |
| EXTENDED_ARG | 103,080 | 0.2% | 94.7% |  |
| BINARY_SUBSCR_DICT | 102,920 | 0.2% | 94.9% | 5.1% |
| IS_OP | 100,940 | 0.2% | 95.1% |  |
| BINARY_SLICE | 100,820 | 0.2% | 95.3% |  |
| BINARY_SUBSCR_GETITEM | 96,820 | 0.2% | 95.5% | 7.1% |
| RETURN_GENERATOR | 94,760 | 0.2% | 95.7% |  |
| TO_BOOL_ALWAYS_TRUE | 93,740 | 0.2% | 95.9% | 6.8% |
| BINARY_OP_ADD_UNICODE | 87,600 | 0.2% | 96.0% |  |
| BEFORE_WITH | 79,720 | 0.2% | 96.2% |  |
| POP_EXCEPT | 79,440 | 0.2% | 96.4% |  |
| PUSH_EXC_INFO | 79,440 | 0.2% | 96.5% |  |
| LOAD_ATTR_PROPERTY | 79,020 | 0.2% | 96.7% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 77,900 | 0.2% | 96.8% | 9.3% |
| LOAD_ATTR_SLOT | 77,000 | 0.2% | 97.0% |  |
| DICT_MERGE | 76,880 | 0.2% | 97.1% |  |
| BINARY_OP | 76,860 | 0.2% | 97.3% |  |
| CHECK_EXC_MATCH | 74,320 | 0.1% | 97.4% |  |
| COMPARE_OP | 66,880 | 0.1% | 97.6% |  |
| BINARY_SUBSCR | 66,100 | 0.1% | 97.7% |  |
| BINARY_OP_ADD_INT | 64,760 | 0.1% | 97.8% |  |
| MAKE_FUNCTION | 59,240 | 0.1% | 97.9% |  |
| LOAD_FAST_AND_CLEAR | 59,100 | 0.1% | 98.0% |  |
| TO_BOOL_INT | 58,780 | 0.1% | 98.2% |  |
| LOAD_SUPER_ATTR_METHOD | 51,020 | 0.1% | 98.3% |  |
| TO_BOOL_LIST | 50,980 | 0.1% | 98.4% |  |
| END_FOR | 47,620 | 0.1% | 98.5% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 41,160 | 0.1% | 98.5% | 19.1% |
| STORE_ATTR_SLOT | 40,800 | 0.1% | 98.6% |  |
| BINARY_SUBSCR_LIST_INT | 36,240 | 0.1% | 98.7% |  |
| EXIT_INIT_CHECK | 35,680 | 0.1% | 98.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 35,680 | 0.1% | 98.8% |  |
| STORE_SUBSCR_DICT | 33,700 | 0.1% | 98.9% |  |
| CALL_BUILTIN_O | 30,940 | 0.1% | 99.0% |  |
| UNPACK_SEQUENCE | 30,020 | 0.1% | 99.0% |  |
| FOR_ITER_RANGE | 29,140 | 0.1% | 99.1% |  |
| RERAISE | 28,160 | 0.1% | 99.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 27,940 | 0.1% | 99.2% |  |
| FORMAT_SIMPLE | 23,200 | 0.0% | 99.2% |  |
| DELETE_ATTR | 23,040 | 0.0% | 99.3% |  |
| RAISE_VARARGS | 23,040 | 0.0% | 99.3% |  |
| LOAD_GLOBAL | 21,580 | 0.0% | 99.4% |  |
| LIST_APPEND | 20,700 | 0.0% | 99.4% |  |
| BUILD_CONST_KEY_MAP | 20,520 | 0.0% | 99.4% |  |
| STORE_FAST_LOAD_FAST | 15,600 | 0.0% | 99.5% |  |
| LOAD_FAST_CHECK | 15,480 | 0.0% | 99.5% |  |
| CALL_STR_1 | 15,360 | 0.0% | 99.5% |  |
| BINARY_OP_SUBTRACT_INT | 13,340 | 0.0% | 99.6% |  |
| BUILD_STRING | 12,960 | 0.0% | 99.6% |  |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 12,900 | 0.0% | 99.6% | 97.7% |
| CALL_INTRINSIC_1 | 12,900 | 0.0% | 99.6% |  |
| LIST_EXTEND | 12,900 | 0.0% | 99.7% |  |
| MAKE_CELL | 12,840 | 0.0% | 99.7% |  |
| CONVERT_VALUE | 12,800 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_ATTR | 12,780 | 0.0% | 99.7% |  |
| STORE_SUBSCR_LIST_INT | 12,780 | 0.0% | 99.8% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 10,540 | 0.0% | 99.8% | 0.6% |
| CALL_TYPE_1 | 10,240 | 0.0% | 99.8% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 10,160 | 0.0% | 99.8% |  |
| IMPORT_FROM | 7,680 | 0.0% | 99.8% |  |
| MAP_ADD | 7,680 | 0.0% | 99.8% |  |
| RESUME | 6,440 | 0.0% | 99.9% |  |
| UNPACK_SEQUENCE_LIST | 5,320 | 0.0% | 99.9% |  |
| IMPORT_NAME | 5,180 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 5,160 | 0.0% | 99.9% |  |
| UNARY_NOT | 5,120 | 0.0% | 99.9% |  |
| WITH_EXCEPT_START | 5,120 | 0.0% | 99.9% |  |
| BUILD_SET | 5,120 | 0.0% | 99.9% |  |
| LOAD_ATTR_CLASS | 5,100 | 0.0% | 99.9% |  |
| SEND_GEN | 5,100 | 0.0% | 99.9% |  |
| BINARY_OP_SUBTRACT_FLOAT | 5,080 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 2,820 | 0.0% | 100.0% |  |
| SET_FUNCTION_ATTRIBUTE | 2,660 | 0.0% | 100.0% |  |
| DELETE_SUBSCR | 2,580 | 0.0% | 100.0% |  |
| END_SEND | 2,560 | 0.0% | 100.0% |  |
| GET_YIELD_FROM_ITER | 2,560 | 0.0% | 100.0% |  |
| BUILD_SLICE | 2,560 | 0.0% | 100.0% |  |
| SET_ADD | 2,560 | 0.0% | 100.0% |  |
| SET_UPDATE | 2,560 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_FLOAT | 2,540 | 0.0% | 100.0% | 2.4% |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,611,540 | 3.2% | 3.2% |
| STORE_FAST LOAD_FAST | 1,324,260 | 2.6% | 5.8% |
| RESUME_CHECK LOAD_FAST | 1,319,874 | 2.6% | 8.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 906,607 | 1.8% | 10.1% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 898,080 | 1.8% | 11.9% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 894,160 | 1.8% | 13.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 881,920 | 1.7% | 15.4% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 753,694 | 1.5% | 16.9% |
| CACHE RESUME_CHECK | 641,634 | 1.3% | 18.1% |
| LOAD_FAST LOAD_CONST | 626,720 | 1.2% | 19.4% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 578,240 | 1.1% | 20.5% |
| LOAD_FAST LOAD_ATTR | 543,862 | 1.1% | 21.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 527,080 | 1.0% | 22.6% |
| POP_JUMP_IF_TRUE LOAD_FAST | 459,000 | 0.9% | 23.5% |
| LOAD_CONST LOAD_FAST | 446,660 | 0.9% | 24.4% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 438,820 | 0.9% | 25.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 416,300 | 0.8% | 26.1% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 405,620 | 0.8% | 26.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_CONST | 404,080 | 0.8% | 27.7% |
| RETURN_CONST POP_TOP | 402,280 | 0.8% | 28.4% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 394,380 | 0.8% | 29.2% |
| POP_TOP LOAD_FAST | 374,254 | 0.7% | 30.0% |
| RETURN_VALUE INTERPRETER_EXIT | 373,414 | 0.7% | 30.7% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 363,560 | 0.7% | 31.4% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 355,180 | 0.7% | 32.1% |
| CALL_ISINSTANCE TO_BOOL_BOOL | 351,500 | 0.7% | 32.8% |
| RETURN_VALUE STORE_FAST | 348,700 | 0.7% | 33.5% |
| LOAD_FAST RETURN_VALUE | 343,500 | 0.7% | 34.2% |
| LOAD_CONST LOAD_CONST | 324,720 | 0.6% | 34.8% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 319,480 | 0.6% | 35.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 316,807 | 0.6% | 36.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 312,080 | 0.6% | 36.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 311,960 | 0.6% | 37.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 293,660 | 0.6% | 37.8% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 289,420 | 0.6% | 38.4% |
| RETURN_CONST INTERPRETER_EXIT | 288,420 | 0.6% | 39.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 261,620 | 0.5% | 39.5% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST_LOAD_FAST | 245,540 | 0.5% | 40.0% |
| LOAD_GLOBAL_BUILTIN CALL_ISINSTANCE | 242,540 | 0.5% | 40.5% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 242,280 | 0.5% | 40.9% |
| LOAD_FAST TO_BOOL_STR | 241,660 | 0.5% | 41.4% |
| LOAD_FAST LOAD_FAST | 240,780 | 0.5% | 41.9% |
| STORE_ATTR_INSTANCE_VALUE LOAD_FAST | 237,460 | 0.5% | 42.3% |
| LOAD_CONST CALL | 234,680 | 0.5% | 42.8% |
| LOAD_FAST TO_BOOL_BOOL | 224,260 | 0.4% | 43.2% |
| LOAD_FAST CALL | 222,087 | 0.4% | 43.7% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 218,060 | 0.4% | 44.1% |
| POP_TOP RETURN_CONST | 217,980 | 0.4% | 44.5% |
| STORE_FAST LOAD_GLOBAL_MODULE | 216,780 | 0.4% | 45.0% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 214,260 | 0.4% | 45.4% |
| POP_JUMP_IF_FALSE RETURN_CONST | 200,040 | 0.4% | 45.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 197,260 | 0.4% | 46.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 195,020 | 0.4% | 46.5% |
| PUSH_NULL LOAD_FAST | 192,660 | 0.4% | 46.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 188,680 | 0.4% | 47.3% |
| LOAD_CONST COMPARE_OP_INT | 186,060 | 0.4% | 47.7% |
| TO_BOOL_STR POP_JUMP_IF_TRUE | 179,520 | 0.4% | 48.0% |
| NOP LOAD_FAST | 174,687 | 0.3% | 48.4% |
| LOAD_CONST CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 173,600 | 0.3% | 48.7% |
| CALL STORE_FAST | 173,320 | 0.3% | 49.0% |
| RESUME_CHECK POP_TOP | 171,320 | 0.3% | 49.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 169,100 | 0.3% | 49.7% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 166,580 | 0.3% | 50.0% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 165,980 | 0.3% | 50.4% |
| STORE_ATTR_INSTANCE_VALUE LOAD_CONST | 165,440 | 0.3% | 50.7% |
| POP_JUMP_IF_FALSE LOAD_CONST | 164,100 | 0.3% | 51.0% |
| RETURN_VALUE RETURN_VALUE | 161,360 | 0.3% | 51.3% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 160,500 | 0.3% | 51.6% |
| STORE_FAST_STORE_FAST STORE_FAST | 158,800 | 0.3% | 52.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 155,460 | 0.3% | 52.3% |
| LOAD_CONST STORE_FAST | 151,500 | 0.3% | 52.6% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 147,980 | 0.3% | 52.8% |
| LOAD_CONST CALL_KW | 146,520 | 0.3% | 53.1% |
| COPY_FREE_VARS RESUME_CHECK | 145,760 | 0.3% | 53.4% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 144,560 | 0.3% | 53.7% |
| LOAD_FAST COPY | 143,680 | 0.3% | 54.0% |
| LOAD_FAST POP_JUMP_IF_NONE | 143,260 | 0.3% | 54.3% |
| CALL RETURN_VALUE | 138,767 | 0.3% | 54.5% |
| LOAD_FAST TO_BOOL_NONE | 138,660 | 0.3% | 54.8% |
| RETURN_VALUE LOAD_FAST | 138,220 | 0.3% | 55.1% |
| POP_TOP ENTER_EXECUTOR | 136,940 | 0.3% | 55.4% |
| LOAD_ATTR LOAD_FAST | 136,640 | 0.3% | 55.6% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 136,480 | 0.3% | 55.9% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 136,400 | 0.3% | 56.2% |
| RESUME_CHECK NOP | 135,540 | 0.3% | 56.4% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST_STORE_FAST | 132,900 | 0.3% | 56.7% |
| JUMP_FORWARD LOAD_FAST | 130,580 | 0.3% | 56.9% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 130,200 | 0.3% | 57.2% |
| LOAD_FAST TO_BOOL | 125,520 | 0.2% | 57.4% |
| GET_ITER FOR_ITER_LIST | 124,720 | 0.2% | 57.7% |
| JUMP_BACKWARD FOR_ITER_GEN | 123,880 | 0.2% | 57.9% |
| LOAD_FAST GET_ITER | 123,260 | 0.2% | 58.2% |
| RESUME_CHECK LOAD_FAST_LOAD_FAST | 122,660 | 0.2% | 58.4% |
| CALL TO_BOOL_BOOL | 122,320 | 0.2% | 58.7% |
| LOAD_GLOBAL_MODULE CALL_ISINSTANCE | 122,220 | 0.2% | 58.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 122,020 | 0.2% | 59.1% |
| LOAD_FAST STORE_ATTR | 118,700 | 0.2% | 59.4% |
| BUILD_MAP LOAD_FAST | 117,820 | 0.2% | 59.6% |
| LOAD_CONST BINARY_SUBSCR_TUPLE_INT | 117,640 | 0.2% | 59.8% |
| POP_JUMP_IF_TRUE ENTER_EXECUTOR | 115,660 | 0.2% | 60.1% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 77,340 | 76.7% |
| LOAD_FAST | 12,960 | 12.9% |
| BINARY_OP_ADD_INT | 10,500 | 10.4% |
| BINARY_OP | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 41,040 | 40.7% |
| STORE_FAST | 20,800 | 20.6% |
| CALL_METHOD_DESCRIPTOR_O | 15,520 | 15.4% |
| LOAD_ATTR_METHOD_NO_DICT | 10,120 | 10.0% |
| LOAD_CONST | 5,160 | 5.1% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 641,634 | 86.3% |
| POP_TOP | 41,400 | 5.6% |
| COPY_FREE_VARS | 38,460 | 5.2% |
| RETURN_GENERATOR | 20,480 | 2.8% |
| RESUME | 1,800 | 0.2% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 69,200 | 86.8% |
| RETURN_VALUE | 10,260 | 12.9% |
| LOAD_ATTR | 120 | 0.2% |
| CALL | 100 | 0.1% |
| LOAD_GLOBAL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 77,140 | 96.8% |
| STORE_FAST | 2,580 | 3.2% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,040 | 49.6% |
| BUILD_STRING | 2,520 | 24.8% |
| LOAD_FAST_LOAD_FAST | 2,520 | 24.8% |
| BINARY_OP | 80 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,620 | 75.0% |
| LOAD_FAST_LOAD_FAST | 2,540 | 25.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 46,080 | 69.7% |
| LOAD_CONST | 13,680 | 20.7% |
| BINARY_SUBSCR | 3,400 | 5.1% |
| BUILD_TUPLE | 2,560 | 3.9% |
| LOAD_FAST | 260 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,660 | 73.6% |
| CALL_LEN | 5,080 | 7.7% |
| BINARY_SUBSCR | 3,400 | 5.1% |
| PUSH_EXC_INFO | 2,600 | 3.9% |
| LOAD_FAST | 2,560 | 3.9% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 63,980 | 86.1% |
| BUILD_TUPLE | 7,680 | 10.3% |
| LOAD_ATTR_MODULE | 2,540 | 3.4% |
| LOAD_GLOBAL | 100 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 74,320 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 2,560 | 99.2% |
| LOAD_FAST | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 99.2% |
| LOAD_GLOBAL_MODULE | 20 | 0.8% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 47,620 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 47,620 | 100.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,560 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 35,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 35,680 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 12,800 | 55.2% |
| LOAD_FAST | 7,840 | 33.8% |
| LOAD_GLOBAL_MODULE | 2,540 | 10.9% |
| LOAD_GLOBAL | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 12,960 | 55.9% |
| LOAD_CONST | 10,240 | 44.1% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 123,260 | 30.0% |
| CALL_BUILTIN_CLASS | 63,880 | 15.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 57,660 | 14.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,100 | 12.5% |
| BINARY_SLICE | 41,040 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 124,720 | 30.4% |
| FOR_ITER | 84,800 | 20.7% |
| LOAD_FAST_AND_CLEAR | 48,860 | 11.9% |
| FOR_ITER_TUPLE | 46,100 | 11.2% |
| FOR_ITER_GEN | 41,800 | 10.2% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 373,414 | 50.5% |
| RETURN_CONST | 288,420 | 39.0% |
| YIELD_VALUE | 57,020 | 7.7% |
| RETURN_GENERATOR | 20,480 | 2.8% |


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
| LOAD_CONST | 59,240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 48,640 | 82.1% |
| SET_FUNCTION_ATTRIBUTE | 2,660 | 4.5% |
| LOAD_CONST | 2,620 | 4.4% |
| STORE_FAST | 2,560 | 4.3% |
| LOAD_GLOBAL_MODULE | 2,520 | 4.3% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 135,540 | 41.2% |
| STORE_FAST | 41,180 | 12.5% |
| POP_JUMP_IF_FALSE | 38,507 | 11.7% |
| POP_JUMP_IF_TRUE | 31,040 | 9.4% |
| POP_TOP | 23,260 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,687 | 53.1% |
| LOAD_FAST_LOAD_FAST | 46,120 | 14.0% |
| LOAD_GLOBAL_MODULE | 43,440 | 13.2% |
| LOAD_GLOBAL_BUILTIN | 38,000 | 11.6% |
| NOP | 12,820 | 3.9% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 28,180 | 35.5% |
| SWAP | 23,060 | 29.0% |
| COPY | 23,040 | 29.0% |
| STORE_FAST | 2,600 | 3.3% |
| POP_JUMP_IF_FALSE | 2,560 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 28,160 | 35.4% |
| RETURN_VALUE | 23,060 | 29.0% |
| RERAISE | 23,040 | 29.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 2,600 | 3.3% |
| LOAD_FAST | 2,580 | 3.2% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 402,280 | 30.5% |
| RESUME_CHECK | 171,320 | 13.0% |
| CALL | 114,060 | 8.6% |
| POP_JUMP_IF_FALSE | 87,120 | 6.6% |
| BEFORE_WITH | 77,140 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 374,254 | 28.3% |
| RETURN_CONST | 217,980 | 16.5% |
| ENTER_EXECUTOR | 136,940 | 10.4% |
| LOAD_CONST | 112,900 | 8.6% |
| RESUME_CHECK | 91,880 | 7.0% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 27,560 | 34.7% |
| RERAISE | 21,780 | 27.4% |
| CALL_BUILTIN_FAST | 7,660 | 9.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 5,120 | 6.4% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 5,080 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 71,500 | 90.0% |
| WITH_EXCEPT_START | 5,120 | 6.4% |
| LOAD_GLOBAL_MODULE | 2,520 | 3.2% |
| LOAD_GLOBAL | 300 | 0.4% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 105,800 | 37.4% |
| LOAD_ATTR_MODULE | 77,120 | 27.2% |
| LOAD_FAST | 77,000 | 27.2% |
| LOAD_SUPER_ATTR_ATTR | 12,780 | 4.5% |
| BINARY_SUBSCR_DICT | 5,120 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 192,660 | 68.0% |
| CALL | 34,040 | 12.0% |
| LOAD_FAST_LOAD_FAST | 18,060 | 6.4% |
| LOAD_CONST | 18,020 | 6.4% |
| LOAD_GLOBAL_MODULE | 15,240 | 5.4% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 58,720 | 62.0% |
| CACHE | 20,480 | 21.6% |
| CALL_FUNCTION_EX | 7,680 | 8.1% |
| COPY_FREE_VARS | 2,600 | 2.7% |
| CALL_KW | 2,560 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 28,160 | 29.7% |
| INTERPRETER_EXIT | 20,480 | 21.6% |
| CALL_BUILTIN_O | 12,760 | 13.5% |
| STORE_FAST | 10,240 | 10.8% |
| LOAD_FAST | 7,680 | 8.1% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 343,500 | 22.9% |
| RETURN_VALUE | 161,360 | 10.8% |
| CALL | 138,767 | 9.2% |
| CALL_FUNCTION_EX | 84,520 | 5.6% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 84,400 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 373,414 | 24.9% |
| STORE_FAST | 348,700 | 23.2% |
| RETURN_VALUE | 161,360 | 10.8% |
| LOAD_FAST | 138,220 | 9.2% |
| BUILD_TUPLE | 51,180 | 3.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 51,200 | 48.0% |
| LOAD_FAST | 23,240 | 21.8% |
| LOAD_FAST_LOAD_FAST | 20,560 | 19.3% |
| RETURN_VALUE | 10,240 | 9.6% |
| STORE_SUBSCR | 1,080 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 51,200 | 48.0% |
| JUMP_BACKWARD | 31,120 | 29.2% |
| ENTER_EXECUTOR | 12,580 | 11.8% |
| LOAD_FAST | 5,200 | 4.9% |
| LOAD_CONST | 2,640 | 2.5% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,520 | 63.1% |
| LOAD_ATTR_INSTANCE_VALUE | 31,460 | 15.8% |
| COPY | 16,480 | 8.3% |
| LOAD_ATTR | 6,740 | 3.4% |
| LOAD_FAST_CHECK | 5,160 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 109,100 | 54.9% |
| POP_JUMP_IF_TRUE | 79,320 | 39.9% |
| TO_BOOL | 3,680 | 1.9% |
| TO_BOOL_BOOL | 3,620 | 1.8% |
| TO_BOOL_NONE | 1,240 | 0.6% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,080 | 99.2% |
| TO_BOOL | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 2,560 | 50.0% |
| STORE_FAST | 2,560 | 50.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 5,040 | 98.4% |
| TO_BOOL | 80 | 1.6% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 35,880 | 46.7% |
| LOAD_FAST | 15,700 | 20.4% |
| LOAD_CONST | 13,460 | 17.5% |
| LOAD_FAST_LOAD_FAST | 10,640 | 13.8% |
| BINARY_OP | 800 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 35,900 | 46.7% |
| STORE_FAST | 23,540 | 30.6% |
| LOAD_FAST | 12,920 | 16.8% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,520 | 3.3% |
| BINARY_OP | 800 | 1.0% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,800 | 62.4% |
| RETURN_VALUE | 2,580 | 12.6% |
| STORE_FAST | 2,580 | 12.6% |
| CALL | 2,560 | 12.5% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,620 | 20.0% |
| RESUME_CHECK | 25,480 | 13.2% |
| LOAD_FAST | 23,140 | 12.0% |
| LOAD_CONST | 23,060 | 12.0% |
| STORE_ATTR_INSTANCE_VALUE | 20,420 | 10.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 76,940 | 39.9% |
| SWAP | 38,620 | 20.0% |
| LOAD_FAST | 35,920 | 18.6% |
| CALL_PY_EXACT_ARGS | 12,680 | 6.6% |
| MAP_ADD | 7,680 | 4.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,760 | 18.8% |
| POP_TOP | 30,720 | 18.7% |
| STORE_ATTR_INSTANCE_VALUE | 30,600 | 18.7% |
| BUILD_TUPLE | 28,160 | 17.2% |
| POP_JUMP_IF_NOT_NONE | 10,240 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,820 | 71.9% |
| STORE_FAST | 23,040 | 14.1% |
| SWAP | 7,680 | 4.7% |
| JUMP_FORWARD | 5,120 | 3.1% |
| CALL_PY_WITH_DEFAULTS | 5,040 | 3.1% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 2,560 | 50.0% |
| CALL_BUILTIN_CLASS | 2,540 | 49.6% |
| CALL | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 50.0% |
| SWAP | 2,560 | 50.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 2,560 | 100.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 12,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 2,720 | 21.0% |
| RETURN_VALUE | 2,560 | 19.8% |
| CALL | 2,560 | 19.8% |
| STORE_FAST | 2,560 | 19.8% |
| BINARY_OP_INPLACE_ADD_UNICODE | 2,520 | 19.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 107,640 | 32.5% |
| LOAD_FAST | 66,640 | 20.1% |
| RETURN_VALUE | 51,180 | 15.5% |
| LOAD_GLOBAL_BUILTIN | 40,800 | 12.3% |
| LOAD_GLOBAL_MODULE | 38,420 | 11.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 56,320 | 17.0% |
| RETURN_VALUE | 49,040 | 14.8% |
| CALL | 41,420 | 12.5% |
| YIELD_VALUE | 40,960 | 12.4% |
| BINARY_OP | 35,880 | 10.8% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 234,680 | 25.7% |
| LOAD_FAST | 222,087 | 24.3% |
| LOAD_GLOBAL_MODULE | 77,360 | 8.5% |
| LOAD_FAST_LOAD_FAST | 73,220 | 8.0% |
| LOAD_ATTR_METHOD_NO_DICT | 70,660 | 7.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 173,320 | 19.0% |
| RETURN_VALUE | 138,767 | 15.2% |
| TO_BOOL_BOOL | 122,320 | 13.4% |
| POP_TOP | 114,060 | 12.5% |
| RESUME_CHECK | 81,460 | 8.9% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 76,880 | 44.8% |
| LOAD_FAST | 71,760 | 41.8% |
| CALL_INTRINSIC_1 | 12,880 | 7.5% |
| ENTER_EXECUTOR | 7,440 | 4.3% |
| RETURN_VALUE | 2,800 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 84,520 | 49.2% |
| POP_TOP | 40,960 | 23.8% |
| RESUME_CHECK | 17,920 | 10.4% |
| STORE_FAST | 12,820 | 7.5% |
| RETURN_GENERATOR | 7,680 | 4.5% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 12,900 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 12,880 | 99.8% |
| BUILD_MAP | 20 | 0.2% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 146,520 | 85.3% |
| ENTER_EXECUTOR | 25,280 | 14.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 97,020 | 56.5% |
| RETURN_VALUE | 28,180 | 16.4% |
| STORE_FAST | 17,960 | 10.5% |
| LOAD_FAST | 12,800 | 7.5% |
| POP_TOP | 5,120 | 3.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,280 | 34.8% |
| LOAD_CONST | 20,420 | 30.5% |
| LOAD_GLOBAL_MODULE | 10,360 | 15.5% |
| LOAD_FAST_LOAD_FAST | 5,240 | 7.8% |
| BUILD_LIST | 2,600 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 46,660 | 69.8% |
| POP_JUMP_IF_FALSE | 16,720 | 25.0% |
| COMPARE_OP | 1,680 | 2.5% |
| COMPARE_OP_INT | 1,160 | 1.7% |
| COMPARE_OP_STR | 520 | 0.8% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,720 | 46.4% |
| LOAD_GLOBAL_MODULE | 43,580 | 23.0% |
| LOAD_CONST | 25,840 | 13.7% |
| LOAD_FAST_LOAD_FAST | 11,380 | 6.0% |
| LOAD_ATTR_MODULE | 10,260 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 136,480 | 72.1% |
| STORE_FAST | 15,380 | 8.1% |
| POP_JUMP_IF_TRUE | 14,300 | 7.6% |
| EXTENDED_ARG | 10,240 | 5.4% |
| COPY | 5,120 | 2.7% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,240 | 80.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 2,540 | 19.8% |
| LOAD_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 12,800 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 143,680 | 56.0% |
| RAISE_VARARGS | 17,920 | 7.0% |
| CALL_ISINSTANCE | 12,780 | 5.0% |
| LOAD_CONST | 10,280 | 4.0% |
| RETURN_VALUE | 10,240 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 58,300 | 22.7% |
| LOAD_ATTR_INSTANCE_VALUE | 41,080 | 16.0% |
| TO_BOOL_STR | 30,560 | 11.9% |
| TO_BOOL_BOOL | 30,480 | 11.9% |
| POP_EXCEPT | 23,040 | 9.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 86,900 | 58.4% |
| CACHE | 38,460 | 25.9% |
| CALL | 20,680 | 13.9% |
| CALL_KW | 2,560 | 1.7% |
| CALL_FUNCTION_EX | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 145,760 | 98.0% |
| RETURN_GENERATOR | 2,600 | 1.7% |
| RESUME | 320 | 0.2% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,360 | 66.7% |
| NOP | 7,680 | 33.3% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,740 | 93.3% |
| BUILD_MAP | 2,560 | 3.3% |
| LOAD_ATTR_INSTANCE_VALUE | 2,540 | 3.3% |
| CALL | 20 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 76,880 | 100.0% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 136,940 | 34.8% |
| POP_JUMP_IF_TRUE | 115,660 | 29.4% |
| POP_JUMP_IF_FALSE | 34,860 | 8.9% |
| CALL_LIST_APPEND | 34,820 | 8.8% |
| STORE_FAST | 20,080 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,920 | 20.6% |
| FOR_ITER_TUPLE | 60,820 | 15.4% |
| YIELD_VALUE | 48,000 | 12.2% |
| CALL_KW | 25,280 | 6.4% |
| CALL_LIST_APPEND | 25,060 | 6.4% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 30,680 | 29.8% |
| POP_JUMP_IF_TRUE | 28,160 | 27.3% |
| TO_BOOL_STR | 10,540 | 10.2% |
| CONTAINS_OP | 10,240 | 9.9% |
| GET_ITER | 7,680 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 61,440 | 59.6% |
| JUMP_FORWARD | 30,720 | 29.8% |
| FOR_ITER_LIST | 5,040 | 4.9% |
| FOR_ITER | 2,960 | 2.9% |
| POP_JUMP_IF_TRUE | 2,580 | 2.5% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 84,800 | 69.0% |
| LOAD_FAST | 18,080 | 14.7% |
| JUMP_BACKWARD | 6,660 | 5.4% |
| SWAP | 5,860 | 4.8% |
| FOR_ITER | 3,240 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 32,220 | 26.2% |
| RETURN_CONST | 31,420 | 25.6% |
| LOAD_FAST | 26,320 | 21.4% |
| STORE_FAST | 20,480 | 16.7% |
| STORE_FAST_LOAD_FAST | 5,160 | 4.2% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 5,120 | 66.7% |
| STORE_FAST | 2,560 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,680 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 5,120 | 98.8% |
| STORE_NAME | 40 | 0.8% |
| STORE_FAST | 20 | 0.4% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 48,640 | 48.2% |
| LOAD_GLOBAL_MODULE | 26,520 | 26.3% |
| LOAD_FAST_LOAD_FAST | 20,480 | 20.3% |
| LOAD_FAST | 5,140 | 5.1% |
| LOAD_GLOBAL | 160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 65,080 | 64.5% |
| RETURN_VALUE | 15,360 | 15.2% |
| COPY | 10,240 | 10.1% |
| POP_JUMP_IF_TRUE | 7,700 | 7.6% |
| STORE_FAST | 2,560 | 2.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 88,980 | 51.9% |
| STORE_SUBSCR | 31,120 | 18.2% |
| POP_JUMP_IF_TRUE | 29,540 | 17.2% |
| LIST_APPEND | 10,580 | 6.2% |
| POP_JUMP_IF_NONE | 6,500 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 123,880 | 72.3% |
| FOR_ITER_LIST | 35,040 | 20.4% |
| FOR_ITER | 6,660 | 3.9% |
| FOR_ITER_TUPLE | 2,780 | 1.6% |
| FOR_ITER_RANGE | 900 | 0.5% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 2,600 | 50.4% |
| RESUME_CHECK | 2,540 | 49.2% |
| RESUME | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 49.6% |
| SEND_GEN | 2,540 | 49.2% |
| LOAD_FAST | 40 | 0.8% |
| SEND | 20 | 0.4% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 41,020 | 18.8% |
| POP_JUMP_IF_FALSE | 38,400 | 17.6% |
| EXTENDED_ARG | 30,720 | 14.1% |
| LOAD_CONST | 20,480 | 9.4% |
| STORE_SUBSCR_LIST_INT | 12,780 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 130,580 | 60.0% |
| STORE_FAST | 40,960 | 18.8% |
| LOAD_GLOBAL_MODULE | 27,920 | 12.8% |
| LOAD_CONST | 7,680 | 3.5% |
| BUILD_MAP | 5,120 | 2.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,240 | 49.5% |
| BUILD_TUPLE | 10,240 | 49.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 220 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,580 | 51.1% |
| ENTER_EXECUTOR | 10,120 | 48.9% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,820 | 99.4% |
| LOAD_DEREF | 80 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 12,900 | 100.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 543,862 | 74.0% |
| LOAD_ATTR_INSTANCE_VALUE | 68,160 | 9.3% |
| LOAD_ATTR | 49,640 | 6.8% |
| LOAD_GLOBAL_MODULE | 29,400 | 4.0% |
| RETURN_VALUE | 13,000 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 136,640 | 18.6% |
| PUSH_NULL | 105,800 | 14.4% |
| LOAD_CONST | 53,740 | 7.3% |
| LOAD_ATTR | 49,640 | 6.8% |
| STORE_FAST | 49,180 | 6.7% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 626,720 | 21.9% |
| LOAD_ATTR_METHOD_NO_DICT | 404,080 | 14.1% |
| LOAD_CONST | 324,720 | 11.4% |
| STORE_ATTR_INSTANCE_VALUE | 165,440 | 5.8% |
| POP_JUMP_IF_FALSE | 164,100 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 446,660 | 15.6% |
| LOAD_CONST | 324,720 | 11.4% |
| CALL | 234,680 | 8.2% |
| COMPARE_OP_INT | 186,060 | 6.5% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 173,600 | 6.1% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 68,880 | 41.9% |
| LOAD_ATTR_METHOD_NO_DICT | 58,880 | 35.8% |
| LOAD_GLOBAL_MODULE | 15,320 | 9.3% |
| STORE_FAST | 5,160 | 3.1% |
| NOP | 2,640 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,080 | 39.0% |
| LOAD_CONST | 61,480 | 37.4% |
| LOAD_ATTR_INSTANCE_VALUE | 12,600 | 7.7% |
| LOAD_FAST_LOAD_FAST | 7,680 | 4.7% |
| BINARY_SUBSCR_DICT | 5,120 | 3.1% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,324,260 | 13.6% |
| RESUME_CHECK | 1,319,874 | 13.6% |
| POP_JUMP_IF_FALSE | 906,607 | 9.3% |
| LOAD_GLOBAL_BUILTIN | 898,080 | 9.2% |
| POP_JUMP_IF_TRUE | 459,000 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,611,540 | 16.6% |
| LOAD_ATTR_METHOD_NO_DICT | 894,160 | 9.2% |
| LOAD_CONST | 626,720 | 6.4% |
| STORE_ATTR_INSTANCE_VALUE | 578,240 | 5.9% |
| LOAD_ATTR | 543,862 | 5.6% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 48,860 | 82.7% |
| LOAD_FAST_AND_CLEAR | 10,240 | 17.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 48,860 | 82.7% |
| LOAD_FAST_AND_CLEAR | 10,240 | 17.3% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 7,760 | 50.1% |
| LOAD_GLOBAL_BUILTIN | 5,080 | 32.8% |
| LOAD_FAST_LOAD_FAST | 2,560 | 16.5% |
| LOAD_GLOBAL | 40 | 0.3% |
| JUMP_FORWARD | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 5,160 | 33.3% |
| BUILD_TUPLE | 2,560 | 16.5% |
| LOAD_ATTR | 2,560 | 16.5% |
| CALL_BUILTIN_CLASS | 2,520 | 16.3% |
| TO_BOOL_BOOL | 2,520 | 16.3% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 289,420 | 18.8% |
| STORE_ATTR_INSTANCE_VALUE | 245,540 | 16.0% |
| LOAD_FAST_LOAD_FAST | 197,260 | 12.8% |
| STORE_FAST | 165,980 | 10.8% |
| RESUME_CHECK | 122,660 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 363,560 | 23.7% |
| LOAD_FAST_LOAD_FAST | 197,260 | 12.8% |
| LOAD_FAST | 136,400 | 8.9% |
| CALL_PY_EXACT_ARGS | 114,380 | 7.4% |
| BUILD_TUPLE | 107,640 | 7.0% |


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
| MAKE_CELL | 5,120 | 39.9% |
| CALL_PY_EXACT_ARGS | 2,580 | 20.1% |
| CALL_KW | 2,560 | 19.9% |
| CALL_PY_WITH_DEFAULTS | 2,540 | 19.8% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 5,120 | 39.9% |
| RESUME_CHECK | 5,120 | 39.9% |
| RETURN_GENERATOR | 2,560 | 19.9% |
| RESUME | 40 | 0.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 7,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 7,340 | 95.6% |
| JUMP_BACKWARD | 340 | 4.4% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 753,694 | 41.1% |
| COMPARE_OP_INT | 195,020 | 10.6% |
| TO_BOOL_NONE | 160,500 | 8.8% |
| CONTAINS_OP | 136,480 | 7.4% |
| TO_BOOL | 109,100 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 906,607 | 49.4% |
| RETURN_CONST | 200,040 | 10.9% |
| LOAD_CONST | 164,100 | 9.0% |
| LOAD_GLOBAL_MODULE | 155,460 | 8.5% |
| LOAD_GLOBAL_BUILTIN | 130,200 | 7.1% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 143,260 | 79.9% |
| LOAD_ATTR_INSTANCE_VALUE | 17,860 | 10.0% |
| LOAD_ATTR | 12,940 | 7.2% |
| LOAD_DEREF | 2,560 | 1.4% |
| CALL_BUILTIN_FAST | 2,540 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 94,840 | 52.9% |
| LOAD_GLOBAL_BUILTIN | 20,260 | 11.3% |
| LOAD_CONST | 17,940 | 10.0% |
| LOAD_FAST_LOAD_FAST | 15,360 | 8.6% |
| RETURN_CONST | 7,680 | 4.3% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 218,060 | 75.8% |
| LOAD_ATTR_INSTANCE_VALUE | 23,020 | 8.0% |
| LOAD_ATTR | 15,520 | 5.4% |
| LOAD_GLOBAL_MODULE | 15,400 | 5.4% |
| RETURN_VALUE | 7,640 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,020 | 39.3% |
| LOAD_GLOBAL_MODULE | 58,700 | 20.4% |
| LOAD_GLOBAL_BUILTIN | 43,280 | 15.1% |
| LOAD_FAST_LOAD_FAST | 25,600 | 8.9% |
| NOP | 12,860 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 355,180 | 34.7% |
| TO_BOOL_STR | 179,520 | 17.6% |
| TO_BOOL_NONE | 107,100 | 10.5% |
| TO_BOOL | 79,320 | 7.8% |
| TO_BOOL_ALWAYS_TRUE | 73,900 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 459,000 | 44.9% |
| ENTER_EXECUTOR | 115,660 | 11.3% |
| POP_TOP | 76,820 | 7.5% |
| LOAD_GLOBAL_BUILTIN | 76,740 | 7.5% |
| LOAD_GLOBAL_MODULE | 76,300 | 7.5% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,920 | 77.8% |
| LOAD_GLOBAL_BUILTIN | 2,540 | 11.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 11.0% |
| LOAD_GLOBAL | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 17,920 | 87.5% |
| PUSH_EXC_INFO | 2,560 | 12.5% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 23,040 | 81.8% |
| POP_JUMP_IF_TRUE | 5,120 | 18.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 21,780 | 81.0% |
| COPY | 5,120 | 19.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 217,980 | 24.2% |
| POP_JUMP_IF_FALSE | 200,040 | 22.2% |
| STORE_ATTR_INSTANCE_VALUE | 147,980 | 16.4% |
| CALL_LIST_APPEND | 53,720 | 6.0% |
| STORE_SUBSCR | 51,200 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 402,280 | 44.7% |
| INTERPRETER_EXIT | 288,420 | 32.1% |
| TO_BOOL_BOOL | 94,500 | 10.5% |
| END_FOR | 47,620 | 5.3% |
| EXIT_INIT_CHECK | 35,680 | 4.0% |


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
| CALL_BUILTIN_CLASS | 2,540 | 99.2% |
| CALL | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 2,220 | 86.7% |
| JUMP_BACKWARD | 340 | 13.3% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,660 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,580 | 97.0% |
| STORE_NAME | 40 | 1.5% |
| LOAD_GLOBAL_MODULE | 40 | 1.5% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,560 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP | 2,560 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 118,700 | 60.4% |
| LOAD_FAST_LOAD_FAST | 59,380 | 30.2% |
| SWAP | 7,960 | 4.0% |
| STORE_ATTR | 7,900 | 4.0% |
| LOAD_GLOBAL_MODULE | 2,540 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,720 | 27.8% |
| LOAD_CONST | 42,020 | 21.4% |
| RETURN_CONST | 28,780 | 14.6% |
| LOAD_FAST_LOAD_FAST | 26,440 | 13.4% |
| LOAD_GLOBAL_MODULE | 22,680 | 11.5% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 348,700 | 16.1% |
| CALL | 173,320 | 8.0% |
| STORE_FAST_STORE_FAST | 158,800 | 7.3% |
| LOAD_CONST | 151,500 | 7.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 113,140 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,324,260 | 61.2% |
| LOAD_GLOBAL_MODULE | 216,780 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 166,580 | 7.7% |
| LOAD_FAST_LOAD_FAST | 165,980 | 7.7% |
| LOAD_CONST | 74,740 | 3.5% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 10,200 | 65.4% |
| FOR_ITER | 5,160 | 33.1% |
| FOR_ITER_TUPLE | 220 | 1.4% |
| COPY | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_LIST | 7,680 | 49.2% |
| LOAD_ATTR_METHOD_NO_DICT | 7,620 | 48.8% |
| TO_BOOL_STR | 220 | 1.4% |
| LOAD_ATTR | 80 | 0.5% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 144,560 | 35.1% |
| UNPACK_SEQUENCE_TUPLE | 132,900 | 32.3% |
| STORE_FAST_STORE_FAST | 64,000 | 15.5% |
| UNPACK_SEQUENCE | 28,880 | 7.0% |
| POP_TOP | 20,480 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 158,800 | 38.6% |
| LOAD_FAST | 122,020 | 29.6% |
| STORE_FAST_STORE_FAST | 64,000 | 15.5% |
| LOAD_FAST_LOAD_FAST | 35,960 | 8.7% |
| LOAD_GLOBAL_BUILTIN | 12,760 | 3.1% |


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
| LOAD_FAST | 74,280 | 28.3% |
| LOAD_FAST_AND_CLEAR | 48,860 | 18.6% |
| BINARY_OP_ADD_INT | 43,400 | 16.5% |
| BUILD_LIST | 38,620 | 14.7% |
| FOR_ITER_LIST | 20,480 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 41,080 | 15.7% |
| BUILD_LIST | 38,620 | 14.7% |
| LOAD_CONST | 30,760 | 11.7% |
| FOR_ITER_LIST | 25,480 | 9.7% |
| POP_EXCEPT | 23,060 | 8.8% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 25,800 | 85.9% |
| RETURN_VALUE | 2,920 | 9.7% |
| FOR_ITER | 300 | 1.0% |
| UNPACK_SEQUENCE | 300 | 1.0% |
| CALL | 280 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 28,880 | 96.2% |
| UNPACK_SEQUENCE_TWO_TUPLE | 420 | 1.4% |
| UNPACK_SEQUENCE_TUPLE | 320 | 1.1% |
| UNPACK_SEQUENCE | 300 | 1.0% |
| UNPACK_SEQUENCE_LIST | 40 | 0.1% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 48,000 | 27.6% |
| BUILD_TUPLE | 40,960 | 23.5% |
| RETURN_VALUE | 30,720 | 17.6% |
| LOAD_FAST | 15,600 | 9.0% |
| COMPARE_OP_STR | 12,780 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 97,120 | 55.8% |
| INTERPRETER_EXIT | 57,020 | 32.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 17,380 | 10.0% |
| YIELD_VALUE | 2,560 | 1.5% |
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
| BINARY_OP_SUBTRACT_FLOAT | 2,520 | 99.2% |
| BINARY_OP | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 54,080 | 83.5% |
| CALL_LEN | 7,600 | 11.7% |
| LOAD_FAST_LOAD_FAST | 2,840 | 4.4% |
| BINARY_OP | 240 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 43,400 | 67.0% |
| BINARY_SLICE | 10,500 | 16.2% |
| CALL_METHOD_DESCRIPTOR_FAST | 5,360 | 8.3% |
| STORE_FAST | 2,860 | 4.4% |
| LOAD_CONST | 2,600 | 4.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 53,820 | 61.4% |
| RETURN_VALUE | 10,160 | 11.6% |
| LOAD_CONST | 10,160 | 11.6% |
| BINARY_SLICE | 5,120 | 5.8% |
| POP_JUMP_IF_TRUE | 5,080 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,040 | 46.8% |
| RETURN_VALUE | 20,460 | 23.4% |
| STORE_FAST | 13,020 | 14.9% |
| COPY | 5,120 | 5.8% |
| LOAD_CONST | 5,100 | 5.8% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,040 | 99.2% |
| BINARY_OP | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,540 | 50.0% |
| BINARY_OP_ADD_FLOAT | 2,520 | 49.6% |
| BINARY_OP | 20 | 0.4% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LEN | 5,040 | 37.8% |
| LOAD_FAST | 2,840 | 21.3% |
| LOAD_FAST_LOAD_FAST | 2,840 | 21.3% |
| LOAD_CONST | 2,520 | 18.9% |
| BINARY_OP | 100 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 10,480 | 78.6% |
| STORE_FAST | 2,860 | 21.4% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 28,160 | 27.4% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 20,440 | 19.9% |
| LOAD_CONST | 20,200 | 19.6% |
| LOAD_FAST | 17,860 | 17.4% |
| LOAD_FAST_LOAD_FAST | 10,780 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 33,260 | 32.5% |
| PUSH_EXC_INFO | 27,560 | 26.9% |
| LOAD_ATTR_METHOD_NO_DICT | 12,600 | 12.3% |
| LOAD_FAST_LOAD_FAST | 10,780 | 10.5% |
| RETURN_VALUE | 10,220 | 10.0% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 50,620 | 52.3% |
| LOAD_FAST | 40,920 | 42.3% |
| LOAD_CONST | 5,120 | 5.3% |
| BINARY_SUBSCR_DICT | 100 | 0.1% |
| BINARY_SUBSCR_GETITEM | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 89,980 | 92.9% |
| LOAD_FAST_LOAD_FAST | 4,640 | 4.8% |
| PUSH_EXC_INFO | 1,880 | 1.9% |
| RETURN_VALUE | 200 | 0.2% |
| BINARY_SUBSCR_DICT | 80 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 23,360 | 64.5% |
| LOAD_FAST_LOAD_FAST | 12,760 | 35.2% |
| BINARY_SUBSCR | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 12,780 | 35.3% |
| RETURN_VALUE | 7,660 | 21.1% |
| TO_BOOL_STR | 7,640 | 21.1% |
| LOAD_ATTR_METHOD_NO_DICT | 5,280 | 14.6% |
| YIELD_VALUE | 2,780 | 7.7% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,760 | 97.9% |
| BINARY_SUBSCR | 60 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,780 | 98.6% |
| LOAD_ATTR | 40 | 1.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 117,640 | 85.1% |
| LOAD_FAST | 20,440 | 14.8% |
| BINARY_SUBSCR | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 48,620 | 35.2% |
| STORE_FAST | 40,980 | 29.6% |
| LOAD_GLOBAL_BUILTIN | 35,840 | 25.9% |
| LOAD_ATTR_METHOD_NO_DICT | 10,200 | 7.4% |
| JUMP_FORWARD | 2,540 | 1.8% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,160 | 28.5% |
| LOAD_GLOBAL_MODULE | 10,080 | 28.3% |
| LOAD_ATTR_INSTANCE_VALUE | 7,560 | 21.2% |
| LOAD_ATTR | 5,080 | 14.2% |
| PUSH_NULL | 2,520 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 35,680 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 38,280 | 93.0% |
| LOAD_FAST | 2,640 | 6.4% |
| CALL | 120 | 0.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 33,300 | 80.9% |
| POP_TOP | 7,720 | 18.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.3% |
| CALL_PY_EXACT_ARGS | 20 | 0.0% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 61,120 | 41.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 23,040 | 15.5% |
| LOAD_ATTR_INSTANCE_VALUE | 20,360 | 13.7% |
| CALL_LEN | 12,720 | 8.6% |
| CALL | 8,180 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 63,880 | 43.1% |
| STORE_FAST | 35,880 | 24.2% |
| RETURN_VALUE | 20,440 | 13.8% |
| LOAD_FAST | 15,320 | 10.3% |
| COPY | 7,640 | 5.2% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 104,340 | 51.5% |
| LOAD_FAST_LOAD_FAST | 72,280 | 35.7% |
| LOAD_ATTR_INSTANCE_VALUE | 20,360 | 10.0% |
| BUILD_MAP | 2,520 | 1.2% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 2,520 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 83,940 | 41.4% |
| RETURN_VALUE | 82,520 | 40.7% |
| STORE_FAST | 12,780 | 6.3% |
| PUSH_EXC_INFO | 7,660 | 3.8% |
| LOAD_FAST | 5,080 | 2.5% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,400 | 98.7% |
| LOAD_CONST | 60 | 0.6% |
| RETURN_GENERATOR | 40 | 0.4% |
| CALL | 20 | 0.2% |
| CALL_STR_1 | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,260 | 49.9% |
| PUSH_EXC_INFO | 5,120 | 48.6% |
| RETURN_VALUE | 140 | 1.3% |
| BEFORE_WITH | 20 | 0.2% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,020 | 42.1% |
| RETURN_GENERATOR | 12,760 | 41.2% |
| BUILD_TUPLE | 2,560 | 8.3% |
| BUILD_LIST | 2,520 | 8.1% |
| CALL | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 15,280 | 49.4% |
| STORE_FAST | 13,040 | 42.1% |
| RETURN_VALUE | 2,560 | 8.3% |
| TO_BOOL | 40 | 0.1% |
| TO_BOOL_INT | 20 | 0.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 242,540 | 56.8% |
| LOAD_GLOBAL_MODULE | 122,220 | 28.6% |
| BUILD_TUPLE | 33,020 | 7.7% |
| LOAD_ATTR_MODULE | 22,800 | 5.3% |
| LOAD_ATTR | 5,040 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 351,500 | 82.4% |
| STORE_FAST | 35,860 | 8.4% |
| LOAD_FAST | 20,460 | 4.8% |
| COPY | 12,780 | 3.0% |
| RETURN_VALUE | 5,100 | 1.2% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 92,360 | 52.2% |
| LOAD_ATTR_INSTANCE_VALUE | 66,500 | 37.5% |
| LOAD_ATTR | 10,080 | 5.7% |
| BINARY_SUBSCR | 5,080 | 2.9% |
| LOAD_ATTR_SLOT | 2,520 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,500 | 37.5% |
| LOAD_CONST | 35,840 | 20.2% |
| LOAD_GLOBAL_MODULE | 18,120 | 10.2% |
| CALL_BUILTIN_CLASS | 12,720 | 7.2% |
| LOAD_FAST | 10,160 | 5.7% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 71,980 | 65.4% |
| ENTER_EXECUTOR | 25,060 | 22.8% |
| BUILD_TUPLE | 12,720 | 11.6% |
| CALL | 260 | 0.2% |
| LOAD_CONST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 53,720 | 48.8% |
| ENTER_EXECUTOR | 34,820 | 31.6% |
| LOAD_GLOBAL_BUILTIN | 12,760 | 11.6% |
| LOAD_FAST | 5,140 | 4.7% |
| LOAD_FAST_LOAD_FAST | 2,540 | 2.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 63,660 | 35.8% |
| LOAD_CONST | 56,480 | 31.8% |
| LOAD_FAST | 20,520 | 11.5% |
| LOAD_FAST_LOAD_FAST | 10,200 | 5.7% |
| LOAD_ATTR_METHOD_LAZY_DICT | 10,080 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 51,360 | 28.9% |
| RETURN_VALUE | 38,320 | 21.6% |
| POP_TOP | 28,480 | 16.0% |
| LOAD_FAST | 18,120 | 10.2% |
| BUILD_TUPLE | 13,000 | 7.3% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 173,600 | 70.6% |
| LOAD_ATTR_METHOD_NO_DICT | 64,000 | 26.0% |
| LOAD_FAST | 5,040 | 2.0% |
| LOAD_FAST_LOAD_FAST | 2,520 | 1.0% |
| CALL | 700 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 84,400 | 34.3% |
| STORE_FAST | 58,840 | 23.9% |
| POP_TOP | 30,660 | 12.5% |
| GET_ITER | 15,300 | 6.2% |
| LOAD_FAST_LOAD_FAST | 12,780 | 5.2% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 438,820 | 87.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 35,620 | 7.1% |
| LOAD_ATTR | 17,774 | 3.5% |
| LOAD_FAST | 5,060 | 1.0% |
| LOAD_SUPER_ATTR_METHOD | 5,040 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 113,140 | 22.4% |
| LOAD_FAST | 77,100 | 15.3% |
| GET_ITER | 57,660 | 11.4% |
| STORE_SUBSCR | 51,200 | 10.2% |
| BINARY_SUBSCR | 46,080 | 9.1% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,320 | 43.2% |
| LOAD_FAST | 74,000 | 37.9% |
| BINARY_SLICE | 15,520 | 8.0% |
| STORE_FAST | 10,420 | 5.3% |
| LOAD_ATTR_INSTANCE_VALUE | 5,060 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TUPLE | 99,600 | 51.1% |
| POP_TOP | 28,320 | 14.5% |
| RETURN_VALUE | 28,300 | 14.5% |
| STORE_FAST | 15,360 | 7.9% |
| LOAD_CONST | 12,860 | 6.6% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 394,380 | 38.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 261,620 | 25.3% |
| LOAD_FAST_LOAD_FAST | 114,380 | 11.1% |
| LOAD_ATTR | 42,960 | 4.2% |
| GET_ITER | 40,740 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 881,920 | 85.3% |
| COPY_FREE_VARS | 86,900 | 8.4% |
| RETURN_GENERATOR | 58,720 | 5.7% |
| MAKE_CELL | 2,580 | 0.2% |
| STORE_FAST | 2,080 | 0.2% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 58,760 | 24.0% |
| LOAD_FAST | 45,680 | 18.7% |
| LOAD_CONST | 40,740 | 16.6% |
| LOAD_ATTR_INSTANCE_VALUE | 32,840 | 13.4% |
| ENTER_EXECUTOR | 22,740 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 242,280 | 99.0% |
| MAKE_CELL | 2,540 | 1.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,780 | 83.2% |
| RETURN_VALUE | 2,520 | 16.4% |
| CALL | 60 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 12,720 | 82.8% |
| STORE_FAST | 2,580 | 16.8% |
| LOAD_ATTR | 40 | 0.3% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 0.1% |


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
| LOAD_FAST | 10,200 | 99.6% |
| CALL | 20 | 0.2% |
| LOAD_GLOBAL_MODULE | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,120 | 50.0% |
| CALL_PY_EXACT_ARGS | 5,080 | 49.6% |
| PUSH_NULL | 20 | 0.2% |
| CALL | 20 | 0.2% |


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
| LOAD_CONST | 186,060 | 64.8% |
| LOAD_ATTR_INSTANCE_VALUE | 30,600 | 10.7% |
| LOAD_GLOBAL_MODULE | 23,200 | 8.1% |
| CALL | 10,200 | 3.6% |
| COPY | 10,120 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 195,020 | 67.9% |
| POP_JUMP_IF_TRUE | 51,320 | 17.9% |
| EXTENDED_ARG | 30,680 | 10.7% |
| STORE_FAST | 10,240 | 3.6% |
| RETURN_VALUE | 20 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 79,220 | 53.1% |
| LOAD_FAST | 36,260 | 24.3% |
| LOAD_GLOBAL_MODULE | 33,080 | 22.2% |
| COMPARE_OP | 520 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 82,160 | 55.1% |
| POP_JUMP_IF_TRUE | 49,020 | 32.9% |
| YIELD_VALUE | 12,780 | 8.6% |
| EXTENDED_ARG | 5,080 | 3.4% |
| COMPARE_OP | 40 | 0.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 123,880 | 66.5% |
| GET_ITER | 41,800 | 22.4% |
| SWAP | 17,300 | 9.3% |
| LOAD_FAST | 2,540 | 1.4% |
| FOR_ITER | 680 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 113,860 | 61.1% |
| POP_TOP | 48,240 | 25.9% |
| STORE_FAST | 14,880 | 8.0% |
| JUMP_FORWARD | 8,720 | 4.7% |
| FOR_ITER | 440 | 0.2% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 124,720 | 45.0% |
| ENTER_EXECUTOR | 80,920 | 29.2% |
| JUMP_BACKWARD | 35,040 | 12.6% |
| SWAP | 25,480 | 9.2% |
| LOAD_FAST | 5,060 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 64,700 | 23.3% |
| LOAD_FAST | 63,740 | 23.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 61,460 | 22.2% |
| RETURN_CONST | 33,220 | 12.0% |
| SWAP | 20,480 | 7.4% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 15,340 | 52.6% |
| ENTER_EXECUTOR | 12,820 | 44.0% |
| JUMP_BACKWARD | 900 | 3.1% |
| FOR_ITER | 80 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,720 | 47.1% |
| LOAD_FAST | 10,320 | 35.4% |
| LOAD_CONST | 5,100 | 17.5% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 60,820 | 48.5% |
| GET_ITER | 46,100 | 36.8% |
| LOAD_FAST | 15,320 | 12.2% |
| JUMP_BACKWARD | 2,780 | 2.2% |
| SWAP | 220 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 63,420 | 50.6% |
| LOAD_FAST | 46,120 | 36.8% |
| RETURN_CONST | 15,380 | 12.3% |
| STORE_FAST_LOAD_FAST | 220 | 0.2% |
| SWAP | 220 | 0.2% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,060 | 99.2% |
| LOAD_ATTR | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,560 | 50.2% |
| GET_ITER | 2,540 | 49.8% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,611,540 | 92.0% |
| LOAD_FAST_LOAD_FAST | 58,320 | 3.3% |
| COPY | 41,080 | 2.3% |
| LOAD_ATTR_INSTANCE_VALUE | 22,840 | 1.3% |
| LOAD_DEREF | 12,600 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 311,960 | 17.8% |
| LOAD_ATTR_METHOD_NO_DICT | 293,660 | 16.8% |
| LOAD_ATTR_METHOD_WITH_VALUES | 115,380 | 6.6% |
| LOAD_CONST | 109,720 | 6.3% |
| STORE_FAST | 94,580 | 5.4% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 53,400 | 68.5% |
| LOAD_FAST | 23,940 | 30.7% |
| LOAD_ATTR | 460 | 0.6% |
| LOAD_ATTR_METHOD_NO_DICT | 60 | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 35,620 | 45.7% |
| LOAD_CONST | 15,240 | 19.6% |
| LOAD_FAST | 10,480 | 13.5% |
| CALL_METHOD_DESCRIPTOR_FAST | 10,080 | 12.9% |
| LOAD_GLOBAL_MODULE | 6,060 | 7.8% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 894,160 | 61.2% |
| LOAD_ATTR_INSTANCE_VALUE | 293,660 | 20.1% |
| LOAD_GLOBAL_MODULE | 76,780 | 5.3% |
| LOAD_CONST | 61,280 | 4.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 18,080 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 438,820 | 30.0% |
| LOAD_CONST | 404,080 | 27.7% |
| LOAD_FAST | 316,807 | 21.7% |
| CALL | 70,660 | 4.8% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 64,000 | 4.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 527,080 | 75.2% |
| LOAD_ATTR_INSTANCE_VALUE | 115,380 | 16.5% |
| LOAD_ATTR | 38,260 | 5.5% |
| LOAD_ATTR_MODULE | 12,600 | 1.8% |
| LOAD_GLOBAL_MODULE | 5,060 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 261,620 | 37.3% |
| LOAD_FAST | 188,680 | 26.9% |
| LOAD_FAST_LOAD_FAST | 94,640 | 13.5% |
| LOAD_CONST | 74,380 | 10.6% |
| CALL_PY_WITH_DEFAULTS | 58,760 | 8.4% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 169,100 | 92.4% |
| LOAD_ATTR_MODULE | 12,680 | 6.9% |
| LOAD_ATTR | 1,140 | 0.6% |
| LOAD_FAST | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 77,120 | 42.2% |
| CALL_ISINSTANCE | 22,800 | 12.5% |
| LOAD_FAST | 15,460 | 8.5% |
| LOAD_ATTR_MODULE | 12,680 | 6.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,600 | 6.9% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,080 | 78.1% |
| LOAD_FAST_LOAD_FAST | 2,520 | 19.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 200 | 1.6% |
| LOAD_ATTR | 100 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,040 | 39.1% |
| LOAD_FAST | 2,540 | 19.7% |
| CALL_BUILTIN_FAST | 2,520 | 19.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,520 | 19.5% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 200 | 1.6% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,160 | 72.2% |
| LOAD_FAST_LOAD_FAST | 7,560 | 27.1% |
| LOAD_ATTR | 220 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,700 | 45.5% |
| LOAD_FAST | 5,080 | 18.2% |
| PUSH_NULL | 2,540 | 9.1% |
| CONVERT_VALUE | 2,540 | 9.1% |
| COMPARE_OP_INT | 2,520 | 9.0% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 73,560 | 93.1% |
| RETURN_VALUE | 2,520 | 3.2% |
| LOAD_ATTR_INSTANCE_VALUE | 2,520 | 3.2% |
| LOAD_ATTR | 420 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 79,020 | 100.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40,920 | 53.1% |
| LOAD_FAST | 30,500 | 39.6% |
| COPY | 5,040 | 6.5% |
| LOAD_ATTR_MODULE | 280 | 0.4% |
| LOAD_ATTR | 220 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 41,200 | 53.5% |
| LOAD_CONST | 12,820 | 16.6% |
| GET_ITER | 10,220 | 13.3% |
| PUSH_NULL | 2,540 | 3.3% |
| BUILD_MAP | 2,540 | 3.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 405,620 | 28.1% |
| LOAD_FAST | 214,260 | 14.8% |
| STORE_FAST | 166,580 | 11.5% |
| POP_JUMP_IF_FALSE | 130,200 | 9.0% |
| POP_JUMP_IF_TRUE | 76,740 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 898,080 | 62.2% |
| CALL_ISINSTANCE | 242,540 | 16.8% |
| LOAD_DEREF | 68,880 | 4.8% |
| CHECK_EXC_MATCH | 63,980 | 4.4% |
| LOAD_GLOBAL_BUILTIN | 45,700 | 3.2% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 319,480 | 20.1% |
| RESUME_CHECK | 312,080 | 19.6% |
| STORE_FAST | 216,780 | 13.6% |
| POP_JUMP_IF_FALSE | 155,460 | 9.8% |
| STORE_ATTR_INSTANCE_VALUE | 91,220 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 416,300 | 26.2% |
| LOAD_FAST_LOAD_FAST | 289,420 | 18.2% |
| LOAD_ATTR_MODULE | 169,100 | 10.6% |
| CALL_ISINSTANCE | 122,220 | 7.7% |
| CALL | 77,360 | 4.9% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,760 | 99.8% |
| LOAD_SUPER_ATTR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 12,780 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,760 | 99.5% |
| LOAD_SUPER_ATTR | 260 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 12,860 | 25.2% |
| CALL_PY_EXACT_ARGS | 12,680 | 24.9% |
| LOAD_FAST_LOAD_FAST | 10,240 | 20.1% |
| LOAD_FAST | 10,200 | 20.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 5,040 | 9.9% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 881,920 | 34.4% |
| CACHE | 641,634 | 25.0% |
| CALL_PY_WITH_DEFAULTS | 242,280 | 9.5% |
| COPY_FREE_VARS | 145,760 | 5.7% |
| FOR_ITER_GEN | 113,860 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,319,874 | 51.5% |
| LOAD_GLOBAL_BUILTIN | 405,620 | 15.8% |
| LOAD_GLOBAL_MODULE | 312,080 | 12.2% |
| POP_TOP | 171,320 | 6.7% |
| NOP | 135,540 | 5.3% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 2,540 | 49.8% |
| LOAD_CONST | 2,540 | 49.8% |
| SEND | 20 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,540 | 49.8% |
| RESUME_CHECK | 2,540 | 49.8% |
| RESUME | 20 | 0.4% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 578,240 | 57.9% |
| LOAD_FAST_LOAD_FAST | 363,560 | 36.4% |
| SWAP | 41,080 | 4.1% |
| LOAD_ATTR_INSTANCE_VALUE | 7,600 | 0.8% |
| STORE_ATTR | 4,840 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 245,540 | 24.6% |
| LOAD_FAST | 237,460 | 23.8% |
| LOAD_CONST | 165,440 | 16.6% |
| RETURN_CONST | 147,980 | 14.8% |
| LOAD_GLOBAL_MODULE | 91,220 | 9.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,260 | 49.7% |
| LOAD_FAST_LOAD_FAST | 15,260 | 37.4% |
| SWAP | 5,040 | 12.4% |
| STORE_ATTR | 240 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 12,780 | 31.3% |
| LOAD_FAST | 12,760 | 31.3% |
| LOAD_FAST_LOAD_FAST | 7,620 | 18.7% |
| LOAD_CONST | 5,100 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 2,520 | 6.2% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 17,640 | 52.3% |
| LOAD_FAST_LOAD_FAST | 7,920 | 23.5% |
| BINARY_OP_ADD_UNICODE | 2,780 | 8.2% |
| LOAD_FAST | 2,560 | 7.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 2,520 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 12,320 | 36.6% |
| LOAD_FAST | 10,180 | 30.2% |
| LOAD_CONST | 7,620 | 22.6% |
| LOAD_FAST_LOAD_FAST | 2,540 | 7.5% |
| JUMP_BACKWARD | 960 | 2.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 12,760 | 99.8% |
| STORE_SUBSCR | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 12,780 | 100.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 53,900 | 57.5% |
| LOAD_ATTR | 22,420 | 23.9% |
| LOAD_FAST | 17,020 | 18.2% |
| TO_BOOL | 300 | 0.3% |
| TO_BOOL_NONE | 100 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 73,900 | 78.8% |
| POP_JUMP_IF_FALSE | 19,720 | 21.0% |
| TO_BOOL_NONE | 120 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_ISINSTANCE | 351,500 | 31.5% |
| LOAD_FAST | 224,260 | 20.1% |
| CALL | 122,320 | 11.0% |
| RETURN_CONST | 94,500 | 8.5% |
| LOAD_ATTR_INSTANCE_VALUE | 89,140 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 753,694 | 67.5% |
| POP_JUMP_IF_TRUE | 355,180 | 31.8% |
| UNARY_NOT | 5,080 | 0.5% |
| EXTENDED_ARG | 2,560 | 0.2% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 30,680 | 52.2% |
| LOAD_FAST | 10,120 | 17.2% |
| LOAD_ATTR | 7,600 | 12.9% |
| COPY | 5,040 | 8.6% |
| CALL_LEN | 2,540 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 38,340 | 65.2% |
| POP_JUMP_IF_FALSE | 20,440 | 34.8% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40,620 | 79.7% |
| LOAD_ATTR_INSTANCE_VALUE | 10,100 | 19.8% |
| TO_BOOL | 260 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 33,100 | 64.9% |
| POP_JUMP_IF_TRUE | 17,880 | 35.1% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,660 | 50.8% |
| COPY | 58,300 | 21.4% |
| LOAD_ATTR_INSTANCE_VALUE | 25,240 | 9.3% |
| CALL | 25,180 | 9.2% |
| LOAD_ATTR | 13,100 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 160,500 | 58.8% |
| POP_JUMP_IF_TRUE | 107,100 | 39.3% |
| EXTENDED_ARG | 4,780 | 1.8% |
| TO_BOOL_STR | 300 | 0.1% |
| TO_BOOL_ALWAYS_TRUE | 100 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 241,660 | 81.6% |
| COPY | 30,560 | 10.3% |
| ENTER_EXECUTOR | 9,600 | 3.2% |
| BINARY_SUBSCR_LIST_INT | 7,640 | 2.6% |
| STORE_FAST | 5,040 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 179,520 | 60.6% |
| POP_JUMP_IF_FALSE | 105,640 | 35.7% |
| EXTENDED_ARG | 10,540 | 3.6% |
| TO_BOOL_NONE | 320 | 0.1% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 5,280 | 99.2% |
| UNPACK_SEQUENCE | 40 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 5,320 | 100.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 99,600 | 64.9% |
| RETURN_VALUE | 38,240 | 24.9% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 7,640 | 5.0% |
| LOAD_FAST | 5,040 | 3.3% |
| LOAD_CONST | 2,520 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 132,900 | 86.7% |
| POP_TOP | 20,460 | 13.3% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 61,460 | 39.1% |
| FOR_ITER | 32,220 | 20.5% |
| LOAD_FAST | 22,920 | 14.6% |
| YIELD_VALUE | 17,380 | 11.0% |
| CALL | 10,200 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 144,560 | 91.9% |
| STORE_FAST | 10,220 | 6.5% |
| LOAD_FAST | 2,540 | 1.6% |


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
|     deferred | 75,420 | 21.8% |
|          hit | 268,540 | 77.7% |
|         miss | 60 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 720 | 48.0% |
| Failure | 780 | 52.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| add other | 620 | 79.5% |
| add different types | 160 | 20.5% |


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
|     deferred | 76,560 | 16.4% |
|          hit | 387,200 | 83.2% |
|         miss | 12,140 | 2.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 840 | 50.0% |
| Failure | 840 | 50.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| out of range | 400 | 47.6% |
| code complex parameters | 240 | 28.6% |
| other | 200 | 23.8% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 937,801 | 19.3% |
|          hit | 3,892,220 | 80.1% |
|         miss | 54,234 | 1.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 13,500 | 43.6% |
| Failure | 17,440 | 56.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 2,820 | 16.2% |
| meth descr varargs | 2,820 | 16.2% |
| class no vectorcall | 2,000 | 11.5% |
| meth descr method fastcall keywords | 1,960 | 11.2% |
| metaclass | 1,720 | 9.9% |
| cfunc noargs | 1,160 | 6.7% |
| meth descr varargs keywords | 1,140 | 6.5% |
| cfunc varargs keywords | 840 | 4.8% |
| operator wrapper | 640 | 3.7% |
| other | 420 | 2.4% |
| wrong number arguments | 400 | 2.3% |
| cfunc varargs | 380 | 2.2% |
| cmethod | 320 | 1.8% |
| class mutable | 320 | 1.8% |
| no dict | 240 | 1.4% |
| method wrapper | 140 | 0.8% |
| str | 120 | 0.7% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 66,040 | 9.9% |
|          hit | 600,860 | 89.6% |
|         miss | 2,560 | 0.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,680 | 49.4% |
| Failure | 1,720 | 50.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| different types | 880 | 51.2% |
| big int | 260 | 15.1% |
| bool | 180 | 10.5% |
| bytes | 160 | 9.3% |
| list | 120 | 7.0% |
| set | 120 | 7.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 153,680 | 20.7% |
|          hit | 581,420 | 78.5% |
|         miss | 36,400 | 4.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,740 | 30.9% |
| Failure | 3,900 | 69.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 1,420 | 36.4% |
| dict keys | 1,160 | 29.7% |
| dict items | 420 | 10.8% |
| enumerate | 280 | 7.2% |
| dict values | 260 | 6.7% |
| reversed list | 160 | 4.1% |
| set | 120 | 3.1% |
| ascii string | 80 | 2.1% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 726,122 | 13.2% |
|          hit | 4,721,327 | 86.1% |
|         miss | 29,240 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 16,020 | 42.5% |
| Failure | 21,680 | 57.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 16,560 | 76.4% |
| method | 1,660 | 7.7% |
| class attr descriptor | 720 | 3.3% |
| metaclass attribute | 680 | 3.1% |
| module attr not found | 620 | 2.9% |
| class method obj | 600 | 2.8% |
| class attr simple | 360 | 1.7% |
| non overriding descriptor | 240 | 1.1% |
| mutable class | 240 | 1.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 12,700 | 0.4% |
|        deopt | 800 | 0.0% |
|          hit | 3,031,640 | 99.2% |
|         miss | 2,080 | 0.1% |

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
|     deferred | 240 | 0.4% |
|          hit | 63,800 | 99.2% |

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
|     deferred | 20 | 0.4% |
|          hit | 5,100 | 99.2% |

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
|     deferred | 186,720 | 15.1% |
|          hit | 1,037,820 | 83.9% |
|         miss | 3,100 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 5,120 | 39.3% |
| Failure | 7,900 | 60.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| not managed dict | 6,980 | 88.4% |
| class attr simple | 420 | 5.3% |
| property | 360 | 4.6% |
| overridden | 120 | 1.5% |
| no dict | 20 | 0.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 105,340 | 49.2% |
|          hit | 107,380 | 50.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 19.4% |
| Failure | 1,080 | 80.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 620 | 57.4% |
| other | 460 | 42.6% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 238,220 | 11.0% |
|          hit | 1,919,634 | 88.5% |
|         miss | 50,540 | 2.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,480 | 67.0% |
| Failure | 3,680 | 33.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 1,480 | 40.2% |
| dict | 860 | 23.4% |
| sequence | 600 | 16.3% |
| set | 240 | 6.5% |
| tuple | 240 | 6.5% |
| other | 140 | 3.8% |
| mapping | 120 | 3.3% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 28,940 | 5.9% |
|          hit | 460,440 | 93.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 780 | 72.2% |
| Failure | 300 | 27.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 300 | 100.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 26,382,658 | 51.8% |
| Not specialized | 5,960,043 | 11.7% |
| Specialized hits | 18,366,655 | 36.1% |
| Specialized misses | 190,354 | 0.4% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 937,801 | 36.0% |
| LOAD_ATTR | 726,122 | 27.8% |
| TO_BOOL | 238,220 | 9.1% |
| STORE_ATTR | 186,720 | 7.2% |
| FOR_ITER | 153,680 | 5.9% |
| STORE_SUBSCR | 105,340 | 4.0% |
| BINARY_SUBSCR | 76,560 | 2.9% |
| BINARY_OP | 75,420 | 2.9% |
| COMPARE_OP | 66,040 | 2.5% |
| UNPACK_SEQUENCE | 28,940 | 1.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 30,154 | 15.8% |
| FOR_ITER_GEN | 24,040 | 12.6% |
| TO_BOOL_NONE | 23,740 | 12.5% |
| TO_BOOL_STR | 20,440 | 10.7% |
| LOAD_ATTR_NONDESCRIPTOR_NO_DICT | 12,600 | 6.6% |
| FOR_ITER_LIST | 12,360 | 6.5% |
| CALL_BOUND_METHOD_EXACT_ARGS | 7,880 | 4.1% |
| CALL_METHOD_DESCRIPTOR_O | 7,760 | 4.1% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,220 | 3.8% |
| BINARY_SUBSCR_GETITEM | 6,840 | 3.6% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 743,774 | 27.8% |
| Calls to Python functions inlined | 1,935,620 | 72.2% |
| Calls via PyEval_EvalFrame (total) | 743,774 | 27.8% |
| Calls via PyEval_EvalFrame (vector) | 644,734 | 24.1% |
| Calls via PyEval_EvalFrame (generator) | 99,040 | 3.7% |
| Calls via PyEval_EvalFrame (legacy) | 20 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 644,654 | 24.1% |
| Calls via PyEval_EvalFrame (build class) | 60 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 114,820 | 4.3% |
| Calls via PyEval_EvalFrame (function ex) | 25,780 | 1.0% |
| Calls via PyEval_EvalFrame (api) | 67,120 | 2.5% |
| Calls via PyEval_EvalFrame (method) | 23,014 | 0.9% |
| Frame objects created | 97,360 | 3.6% |
| Frames pushed | 2,448,754 | 91.4% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 2,219,207 | 36.8% |
| Frees to freelist | 2,220,247 |  |
| Allocations | 3,808,494 | 63.2% |
| Allocations to 512 bytes | 3,777,294 | 62.7% |
| Allocations to 4 kbytes | 28,600 | 0.5% |
| Allocations over 4 kbytes | 2,600 | 0.0% |
| Frees | 4,001,576 |  |
| New values | 95,100 |  |
| Interpreter increfs | 23,119,165 | 68.7% |
| Interpreter decrefs | 26,926,026 | 69.1% |
| Increfs | 10,527,366 | 31.3% |
| Decrefs | 12,044,545 | 30.9% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 20 | 0.0% |
| Method cache hits | 1,323,457 |  |
| Method cache misses | 48,520 |  |
| Method cache collisions | 67,394 |  |
| Method cache dunder hits | 1,004,567 |  |
| Method cache dunder misses | 22,613 |  |


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
| Optimization attempts | 2,000 |  |
| Traces created | 1,080 | 54.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 20 | 1.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 920 | 46.0% |
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
| <= 16 | 180 | 16.7% |
| <= 32 | 540 | 50.0% |
| <= 64 | 220 | 20.4% |
| <= 128 | 140 | 13.0% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 0 | 0.0% |
| <= 8 | 80 | 7.4% |
| <= 16 | 360 | 33.3% |
| <= 32 | 240 | 22.2% |
| <= 64 | 60 | 5.6% |
| <= 128 | 60 | 5.6% |


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
| FOR_ITER_GEN | 920 |
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
