
# Pystats results

- benchmark: asyncio_tcp_ssl
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 105,286,245 | 22.2% | 22.2% |  |
| POP_JUMP_IF_FALSE | 27,012,635 | 5.7% | 27.9% |  |
| STORE_FAST | 26,254,935 | 5.5% | 33.5% |  |
| LOAD_ATTR_INSTANCE_VALUE | 23,186,091 | 4.9% | 38.4% |  |
| RESUME_CHECK | 21,542,885 | 4.5% | 42.9% | 0.0% |
| TO_BOOL_BOOL | 19,287,527 | 4.1% | 47.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 14,408,421 | 3.0% | 50.0% |  |
| LOAD_CONST | 14,240,648 | 3.0% | 53.0% |  |
| POP_TOP | 13,799,119 | 2.9% | 56.0% |  |
| POP_JUMP_IF_TRUE | 11,508,021 | 2.4% | 58.4% |  |
| CALL_PY_EXACT_ARGS | 11,453,450 | 2.4% | 60.8% | 0.0% |
| LOAD_ATTR | 11,022,642 | 2.3% | 63.1% |  |
| RETURN_VALUE | 10,579,476 | 2.2% | 65.4% |  |
| LOAD_ATTR_WITH_HINT | 10,468,975 | 2.2% | 67.6% |  |
| RETURN_CONST | 10,058,349 | 2.1% | 69.7% |  |
| CALL | 8,850,337 | 1.9% | 71.6% |  |
| TO_BOOL | 7,521,641 | 1.6% | 73.2% |  |
| LOAD_FAST_LOAD_FAST | 7,440,038 | 1.6% | 74.7% |  |
| POP_JUMP_IF_NONE | 7,405,058 | 1.6% | 76.3% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 7,191,022 | 1.5% | 77.8% | 0.0% |
| ENTER_EXECUTOR | 6,848,200 | 1.4% | 79.3% |  |
| LOAD_GLOBAL_MODULE | 6,479,585 | 1.4% | 80.6% | 0.0% |
| CALL_PY_WITH_DEFAULTS | 5,451,608 | 1.2% | 81.8% |  |
| LOAD_FAST_CHECK | 5,120,320 | 1.1% | 82.9% |  |
| CALL_LIST_APPEND | 4,846,130 | 1.0% | 83.9% |  |
| STORE_ATTR_SLOT | 4,664,685 | 1.0% | 84.9% | 0.1% |
| COMPARE_OP_INT | 4,662,124 | 1.0% | 85.9% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 4,170,627 | 0.9% | 86.7% | 0.0% |
| LOAD_ATTR_SLOT | 4,134,009 | 0.9% | 87.6% | 0.1% |
| NOP | 4,005,325 | 0.8% | 88.4% |  |
| TO_BOOL_INT | 3,144,645 | 0.7% | 89.1% |  |
| CALL_LEN | 2,961,300 | 0.6% | 89.7% |  |
| LOAD_ATTR_MODULE | 2,443,014 | 0.5% | 90.3% | 0.0% |
| INTERPRETER_EXIT | 2,345,328 | 0.5% | 90.8% |  |
| BINARY_OP | 2,170,473 | 0.5% | 91.2% |  |
| CALL_METHOD_DESCRIPTOR_O | 2,051,727 | 0.4% | 91.6% | 0.0% |
| PUSH_NULL | 2,045,095 | 0.4% | 92.1% |  |
| LOAD_DEREF | 1,652,115 | 0.3% | 92.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 1,638,975 | 0.3% | 92.8% |  |
| SEND_GEN | 1,637,745 | 0.3% | 93.1% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,629,285 | 0.3% | 93.5% |  |
| POP_JUMP_IF_NOT_NONE | 1,367,561 | 0.3% | 93.7% |  |
| BUILD_TUPLE | 1,349,933 | 0.3% | 94.0% |  |
| FOR_ITER_LIST | 1,333,500 | 0.3% | 94.3% |  |
| JUMP_FORWARD | 1,322,002 | 0.3% | 94.6% |  |
| YIELD_VALUE | 1,308,580 | 0.3% | 94.9% |  |
| TO_BOOL_NONE | 1,305,790 | 0.3% | 95.1% | 0.0% |
| STORE_FAST_STORE_FAST | 1,064,518 | 0.2% | 95.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,063,958 | 0.2% | 95.6% |  |
| COPY | 1,022,295 | 0.2% | 95.8% |  |
| CALL_FUNCTION_EX | 1,019,070 | 0.2% | 96.0% |  |
| COMPARE_OP | 989,073 | 0.2% | 96.2% |  |
| END_SEND | 987,835 | 0.2% | 96.4% |  |
| GET_AWAITABLE | 987,835 | 0.2% | 96.7% |  |
| GET_ITER | 976,655 | 0.2% | 96.9% |  |
| BUILD_LIST | 968,120 | 0.2% | 97.1% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 700,347 | 0.1% | 97.2% | 0.2% |
| JUMP_BACKWARD | 692,367 | 0.1% | 97.4% |  |
| STORE_ATTR_WITH_HINT | 691,080 | 0.1% | 97.5% |  |
| BINARY_SLICE | 688,610 | 0.1% | 97.6% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 661,093 | 0.1% | 97.8% |  |
| BINARY_OP_ADD_INT | 659,770 | 0.1% | 97.9% |  |
| SEND | 659,610 | 0.1% | 98.1% |  |
| RETURN_GENERATOR | 659,330 | 0.1% | 98.2% |  |
| TO_BOOL_LIST | 645,550 | 0.1% | 98.3% |  |
| FOR_ITER_RANGE | 644,810 | 0.1% | 98.5% |  |
| CONTAINS_OP | 644,565 | 0.1% | 98.6% |  |
| SWAP | 388,308 | 0.1% | 98.7% |  |
| CALL_BUILTIN_CLASS | 384,728 | 0.1% | 98.8% |  |
| COPY_FREE_VARS | 349,989 | 0.1% | 98.9% |  |
| CALL_KW | 341,208 | 0.1% | 98.9% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 329,528 | 0.1% | 99.0% | 0.1% |
| DELETE_SUBSCR | 328,725 | 0.1% | 99.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 323,285 | 0.1% | 99.1% | 0.0% |
| LIST_EXTEND | 322,845 | 0.1% | 99.2% |  |
| CALL_INTRINSIC_1 | 322,785 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_FLOAT | 322,145 | 0.1% | 99.3% |  |
| CHECK_EXC_MATCH | 321,945 | 0.1% | 99.4% |  |
| POP_EXCEPT | 321,945 | 0.1% | 99.5% |  |
| PUSH_EXC_INFO | 321,945 | 0.1% | 99.5% |  |
| MAKE_CELL | 321,920 | 0.1% | 99.6% |  |
| LOAD_ATTR_PROPERTY | 321,825 | 0.1% | 99.7% |  |
| MAKE_FUNCTION | 321,780 | 0.1% | 99.7% |  |
| SET_FUNCTION_ATTRIBUTE | 321,140 | 0.1% | 99.8% |  |
| BINARY_OP_MULTIPLY_INT | 320,965 | 0.1% | 99.9% |  |
| BUILD_SLICE | 320,725 | 0.1% | 99.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 54,120 | 0.0% | 100.0% | 0.2% |
| CALL_ISINSTANCE | 28,986 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 16,740 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 16,540 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 13,980 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 13,192 | 0.0% | 100.0% |  |
| MAP_ADD | 12,920 | 0.0% | 100.0% |  |
| STORE_ATTR | 12,580 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 9,823 | 0.0% | 100.0% |  |
| FOR_ITER | 9,820 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 9,680 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 9,383 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 8,680 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 6,536 | 0.0% | 100.0% |  |
| RESUME | 5,620 | 0.0% | 100.0% | 0.4% |
| LOAD_SUPER_ATTR_METHOD | 3,520 | 0.0% | 100.0% |  |
| IS_OP | 2,280 | 0.0% | 100.0% |  |
| BUILD_MAP | 2,180 | 0.0% | 100.0% |  |
| CALL_BUILTIN_FAST | 1,780 | 0.0% | 100.0% | 1.1% |
| TO_BOOL_STR | 1,200 | 0.0% | 100.0% | 5.0% |
| STORE_NAME | 1,160 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 1,140 | 0.0% | 100.0% | 5.3% |
| CALL_TYPE_1 | 1,040 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,020 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 980 | 0.0% | 100.0% | 2.0% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 880 | 0.0% | 100.0% | 13.6% |
| UNARY_INVERT | 880 | 0.0% | 100.0% |  |
| STORE_DEREF | 880 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 860 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 820 | 0.0% | 100.0% |  |
| DICT_UPDATE | 760 | 0.0% | 100.0% |  |
| LOAD_NAME | 760 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 760 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 700 | 0.0% | 100.0% |  |
| LIST_APPEND | 680 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 680 | 0.0% | 100.0% |  |
| STORE_FAST_LOAD_FAST | 620 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 600 | 0.0% | 100.0% | 3.3% |
| EXIT_INIT_CHECK | 580 | 0.0% | 100.0% |  |
| BEFORE_WITH | 560 | 0.0% | 100.0% |  |
| UNARY_NOT | 520 | 0.0% | 100.0% |  |
| DICT_MERGE | 460 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 400 | 0.0% | 100.0% | 10.0% |
| BUILD_SET | 400 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 360 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 280 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 220 | 0.0% | 100.0% | 63.6% |
| IMPORT_NAME | 200 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 200 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 140 | 0.0% | 100.0% |  |
| CALL_STR_1 | 120 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 100 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 100 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 100 | 0.0% | 100.0% |  |
| CALL_TUPLE_1 | 100 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 80 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 80 | 0.0% | 100.0% |  |
| RERAISE | 80 | 0.0% | 100.0% |  |
| IMPORT_FROM | 60 | 0.0% | 100.0% |  |
| STORE_SLICE | 40 | 0.0% | 100.0% |  |
| UNARY_NEGATIVE | 40 | 0.0% | 100.0% |  |
| STORE_SUBSCR_LIST_INT | 40 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 20 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 23,161,305 | 4.9% | 4.9% |
| STORE_FAST LOAD_FAST | 17,568,594 | 3.7% | 8.6% |
| RESUME_CHECK LOAD_FAST | 16,820,037 | 3.6% | 12.2% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 16,597,824 | 3.5% | 15.7% |
| POP_JUMP_IF_FALSE LOAD_FAST | 13,916,680 | 2.9% | 18.6% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 12,310,543 | 2.6% | 21.2% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 10,785,122 | 2.3% | 23.5% |
| LOAD_FAST TO_BOOL_BOOL | 10,570,733 | 2.2% | 25.7% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,153,377 | 1.9% | 27.6% |
| RETURN_CONST POP_TOP | 8,365,851 | 1.8% | 29.4% |
| RETURN_VALUE STORE_FAST | 7,784,422 | 1.6% | 31.0% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 7,548,116 | 1.6% | 32.6% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 7,467,333 | 1.6% | 34.2% |
| TO_BOOL POP_JUMP_IF_TRUE | 7,163,753 | 1.5% | 35.7% |
| LOAD_FAST RETURN_VALUE | 7,120,258 | 1.5% | 37.2% |
| POP_JUMP_IF_NONE LOAD_FAST | 7,080,673 | 1.5% | 38.7% |
| CALL STORE_FAST | 6,817,047 | 1.4% | 40.2% |
| LOAD_FAST TO_BOOL | 6,430,146 | 1.4% | 41.5% |
| LOAD_FAST POP_JUMP_IF_NONE | 6,423,923 | 1.4% | 42.9% |
| LOAD_FAST CALL | 6,107,436 | 1.3% | 44.2% |
| LOAD_FAST LOAD_ATTR | 5,794,512 | 1.2% | 45.4% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 5,451,488 | 1.2% | 46.5% |
| ENTER_EXECUTOR CALL_PY_WITH_DEFAULTS | 5,119,680 | 1.1% | 47.6% |
| LOAD_CONST LOAD_FAST | 4,972,843 | 1.1% | 48.7% |
| CALL_LIST_APPEND ENTER_EXECUTOR | 4,845,030 | 1.0% | 49.7% |
| POP_TOP RETURN_CONST | 4,694,017 | 1.0% | 50.7% |
| LOAD_CONST STORE_FAST | 4,570,916 | 1.0% | 51.7% |
| LOAD_FAST CALL_LIST_APPEND | 4,479,065 | 0.9% | 52.6% |
| POP_JUMP_IF_FALSE LOAD_FAST_CHECK | 4,478,885 | 0.9% | 53.5% |
| LOAD_FAST_CHECK LOAD_ATTR_METHOD_NO_DICT | 4,478,845 | 0.9% | 54.5% |
| POP_TOP LOAD_FAST | 4,350,049 | 0.9% | 55.4% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 4,340,319 | 0.9% | 56.3% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 4,145,676 | 0.9% | 57.2% |
| LOAD_FAST LOAD_ATTR_SLOT | 4,117,453 | 0.9% | 58.1% |
| LOAD_ATTR CALL_PY_EXACT_ARGS | 3,922,855 | 0.8% | 58.9% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 3,921,073 | 0.8% | 59.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 3,812,147 | 0.8% | 60.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,690,156 | 0.8% | 61.3% |
| NOP LOAD_FAST | 3,343,169 | 0.7% | 62.0% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,689,263 | 0.6% | 62.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 2,640,572 | 0.6% | 63.1% |
| POP_JUMP_IF_FALSE LOAD_CONST | 2,637,119 | 0.6% | 63.7% |
| LOAD_ATTR_WITH_HINT TO_BOOL_BOOL | 2,614,565 | 0.6% | 64.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,440,534 | 0.5% | 64.8% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 2,405,822 | 0.5% | 65.3% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 2,262,040 | 0.5% | 65.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,074,497 | 0.4% | 66.2% |
| LOAD_FAST STORE_ATTR_SLOT | 2,023,493 | 0.4% | 66.6% |
| CACHE RESUME_CHECK | 2,020,868 | 0.4% | 67.0% |
| POP_TOP LOAD_CONST | 1,984,240 | 0.4% | 67.5% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 1,979,884 | 0.4% | 67.9% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_WITH_HINT | 1,949,260 | 0.4% | 68.3% |
| LOAD_ATTR_WITH_HINT COMPARE_OP_INT | 1,949,140 | 0.4% | 68.7% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 1,813,825 | 0.4% | 69.1% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,749,025 | 0.4% | 69.5% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 1,722,157 | 0.4% | 69.8% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,692,401 | 0.4% | 70.2% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,680,071 | 0.4% | 70.5% |
| LOAD_FAST LOAD_CONST | 1,656,917 | 0.3% | 70.9% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,629,755 | 0.3% | 71.2% |
| LOAD_ATTR_WITH_HINT LOAD_GLOBAL_MODULE | 1,614,115 | 0.3% | 71.6% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 1,606,620 | 0.3% | 71.9% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,387,936 | 0.3% | 72.2% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 1,370,795 | 0.3% | 72.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 1,358,759 | 0.3% | 72.8% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 1,356,040 | 0.3% | 73.1% |
| RETURN_CONST INTERPRETER_EXIT | 1,353,473 | 0.3% | 73.3% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,353,235 | 0.3% | 73.6% |
| STORE_FAST RETURN_CONST | 1,339,675 | 0.3% | 73.9% |
| TO_BOOL_INT POP_JUMP_IF_TRUE | 1,330,740 | 0.3% | 74.2% |
| POP_JUMP_IF_FALSE NOP | 1,329,870 | 0.3% | 74.5% |
| STORE_ATTR_SLOT LOAD_CONST | 1,329,199 | 0.3% | 74.8% |
| STORE_FAST JUMP_FORWARD | 1,312,871 | 0.3% | 75.0% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 1,307,860 | 0.3% | 75.3% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 1,305,730 | 0.3% | 75.6% |
| LOAD_CONST COMPARE_OP_INT | 1,304,206 | 0.3% | 75.9% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 1,303,210 | 0.3% | 76.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,301,290 | 0.3% | 76.4% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 1,124,134 | 0.2% | 76.7% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,112,615 | 0.2% | 76.9% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,063,798 | 0.2% | 77.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,063,118 | 0.2% | 77.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 1,043,616 | 0.2% | 77.6% |
| LOAD_ATTR LOAD_FAST | 1,041,278 | 0.2% | 77.8% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,040,759 | 0.2% | 78.0% |
| LOAD_FAST CALL_LEN | 1,033,375 | 0.2% | 78.2% |
| POP_TOP ENTER_EXECUTOR | 1,032,710 | 0.2% | 78.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 1,031,233 | 0.2% | 78.7% |
| CALL_FUNCTION_EX POP_TOP | 1,017,970 | 0.2% | 78.9% |
| COPY TO_BOOL_INT | 1,010,415 | 0.2% | 79.1% |
| LOAD_GLOBAL_MODULE BINARY_OP | 1,010,375 | 0.2% | 79.3% |
| LOAD_ATTR_WITH_HINT LOAD_ATTR_METHOD_WITH_VALUES | 995,971 | 0.2% | 79.5% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 988,713 | 0.2% | 79.7% |
| GET_AWAITABLE LOAD_CONST | 987,835 | 0.2% | 79.9% |
| COMPARE_OP POP_JUMP_IF_FALSE | 985,313 | 0.2% | 80.1% |
| LOAD_ATTR COMPARE_OP | 983,053 | 0.2% | 80.3% |
| LOAD_ATTR_WITH_HINT LOAD_ATTR | 979,769 | 0.2% | 80.5% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_NONE | 979,435 | 0.2% | 80.7% |
| YIELD_VALUE YIELD_VALUE | 979,355 | 0.2% | 81.0% |
| JUMP_BACKWARD_NO_INTERRUPT SEND_GEN | 979,055 | 0.2% | 81.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 641,690 | 93.2% |
| LOAD_CONST | 46,760 | 6.8% |
| BINARY_OP_ADD_INT | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 358,322 | 52.0% |
| CALL | 320,745 | 46.6% |
| STORE_FAST | 8,663 | 1.3% |
| LIST_EXTEND | 240 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 200 | 0.0% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 2,020,868 | 86.2% |
| COPY_FREE_VARS | 322,660 | 13.8% |
| RESUME | 920 | 0.0% |
| POP_TOP | 480 | 0.0% |
| RETURN_GENERATOR | 320 | 0.0% |


</details>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 80 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 240 | 42.9% |
| RETURN_VALUE | 120 | 21.4% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 21.4% |
| LOAD_GLOBAL | 40 | 7.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 520 | 92.9% |
| STORE_FAST | 40 | 7.1% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,280 | 95.4% |
| BINARY_SUBSCR | 180 | 2.1% |
| LOAD_FAST | 120 | 1.4% |
| BUILD_SLICE | 60 | 0.7% |
| RETURN_VALUE | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,080 | 93.1% |
| BINARY_SUBSCR | 180 | 2.1% |
| BINARY_SUBSCR_LIST_INT | 100 | 1.2% |
| BINARY_SUBSCR_DICT | 80 | 0.9% |
| LOAD_ATTR | 60 | 0.7% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 321,005 | 99.7% |
| LOAD_GLOBAL_BUILTIN | 680 | 0.2% |
| BUILD_TUPLE | 160 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 321,945 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 320,665 | 97.5% |
| LOAD_CONST | 8,000 | 2.4% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 328,665 | 100.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 337,145 | 34.1% |
| SEND | 328,985 | 33.3% |
| RETURN_VALUE | 321,705 | 32.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 666,290 | 67.4% |
| STORE_FAST | 321,145 | 32.5% |
| UNPACK_SEQUENCE | 120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 120 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 580 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 645,850 | 66.1% |
| CALL_BUILTIN_CLASS | 322,105 | 33.0% |
| LOAD_ATTR_INSTANCE_VALUE | 8,140 | 0.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 180 | 0.0% |
| BINARY_SLICE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 644,610 | 66.0% |
| FOR_ITER_RANGE | 322,025 | 33.0% |
| FOR_ITER | 8,640 | 0.9% |
| LOAD_FAST_AND_CLEAR | 680 | 0.1% |
| FOR_ITER_TUPLE | 460 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,353,473 | 57.7% |
| RETURN_VALUE | 662,230 | 28.2% |
| YIELD_VALUE | 329,225 | 14.0% |
| RETURN_GENERATOR | 400 | 0.0% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 100 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 321,780 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 321,140 | 99.8% |
| STORE_NAME | 500 | 0.2% |
| LOAD_CONST | 100 | 0.0% |
| CALL_BUILTIN_FAST | 40 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,329,870 | 33.2% |
| POP_JUMP_IF_TRUE | 658,416 | 16.4% |
| STORE_FAST | 645,630 | 16.1% |
| NOP | 641,870 | 16.0% |
| RESUME_CHECK | 358,774 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,343,169 | 83.5% |
| NOP | 641,870 | 16.0% |
| LOAD_GLOBAL_MODULE | 18,986 | 0.5% |
| LOAD_GLOBAL_BUILTIN | 340 | 0.0% |
| LOAD_CONST | 300 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 321,265 | 99.8% |
| SWAP | 420 | 0.1% |
| STORE_FAST | 160 | 0.0% |
| COPY | 80 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 320,945 | 99.7% |
| RETURN_VALUE | 420 | 0.1% |
| RETURN_CONST | 340 | 0.1% |
| POP_TOP | 80 | 0.0% |
| RERAISE | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 8,365,851 | 60.6% |
| CALL_METHOD_DESCRIPTOR_O | 1,722,157 | 12.5% |
| CALL_FUNCTION_EX | 1,017,970 | 7.4% |
| END_SEND | 666,290 | 4.8% |
| SEND_GEN | 658,390 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 4,694,017 | 34.0% |
| LOAD_FAST | 4,350,049 | 31.5% |
| LOAD_CONST | 1,984,240 | 14.4% |
| ENTER_EXECUTOR | 1,032,710 | 7.5% |
| RESUME_CHECK | 658,850 | 4.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 320,805 | 99.6% |
| BINARY_SUBSCR_DICT | 520 | 0.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 360 | 0.1% |
| RERAISE | 80 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 320,945 | 99.7% |
| LOAD_GLOBAL_BUILTIN | 720 | 0.2% |
| LOAD_GLOBAL | 280 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,692,401 | 82.8% |
| LOAD_ATTR | 324,545 | 15.9% |
| LOAD_DEREF | 24,249 | 1.2% |
| LOAD_FAST | 3,220 | 0.2% |
| LOAD_NAME | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 717,576 | 35.1% |
| LOAD_FAST_LOAD_FAST | 669,991 | 32.8% |
| CALL | 655,548 | 32.1% |
| LOAD_CONST | 840 | 0.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 337,525 | 51.2% |
| ENTER_EXECUTOR | 320,265 | 48.6% |
| CALL_KW | 400 | 0.1% |
| CACHE | 320 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 658,450 | 99.9% |
| INTERPRETER_EXIT | 400 | 0.1% |
| STORE_FAST | 160 | 0.0% |
| CALL | 120 | 0.0% |
| LIST_APPEND | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,120,258 | 67.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,040,759 | 9.8% |
| CALL | 690,510 | 6.5% |
| LOAD_ATTR | 641,405 | 6.1% |
| BINARY_OP_ADD_INT | 337,445 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,784,422 | 73.6% |
| TO_BOOL_BOOL | 694,251 | 6.6% |
| LOAD_FAST | 690,070 | 6.5% |
| INTERPRETER_EXIT | 662,230 | 6.3% |
| POP_TOP | 339,306 | 3.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 240 | 27.9% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 16.3% |
| LOAD_CONST | 120 | 14.0% |
| LOAD_FAST | 120 | 14.0% |
| LOAD_ATTR | 100 | 11.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 220 | 25.6% |
| RETURN_CONST | 180 | 20.9% |
| STORE_SUBSCR_DICT | 160 | 18.6% |
| ENTER_EXECUTOR | 80 | 9.3% |
| JUMP_FORWARD | 80 | 9.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,430,146 | 85.5% |
| LOAD_ATTR_INSTANCE_VALUE | 743,450 | 9.9% |
| LOAD_ATTR_WITH_HINT | 336,985 | 4.5% |
| TO_BOOL | 4,760 | 0.1% |
| LOAD_ATTR | 2,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 7,163,753 | 95.2% |
| POP_JUMP_IF_FALSE | 349,088 | 4.6% |
| TO_BOOL | 4,760 | 0.1% |
| TO_BOOL_BOOL | 2,860 | 0.0% |
| TO_BOOL_INT | 460 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 440 | 50.0% |
| BINARY_OP | 400 | 45.5% |
| LOAD_ATTR | 40 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 880 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 40 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 340 | 65.4% |
| TO_BOOL | 80 | 15.4% |
| TO_BOOL_INT | 80 | 15.4% |
| TO_BOOL_LIST | 20 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 260 | 50.0% |
| RETURN_VALUE | 160 | 30.8% |
| STORE_FAST | 80 | 15.4% |
| CALL_PY_EXACT_ARGS | 20 | 3.8% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,010,375 | 46.6% |
| LOAD_ATTR_MODULE | 741,053 | 34.1% |
| LOAD_ATTR | 366,745 | 16.9% |
| POP_JUMP_IF_FALSE | 46,000 | 2.1% |
| BINARY_OP | 2,620 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 733,670 | 33.8% |
| COPY | 688,830 | 31.7% |
| STORE_FAST | 368,785 | 17.0% |
| BUILD_TUPLE | 366,585 | 16.9% |
| LOAD_FAST_LOAD_FAST | 7,943 | 0.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 40 | 40.0% |
| STORE_FAST | 40 | 40.0% |
| DICT_UPDATE | 20 | 20.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 322,125 | 33.3% |
| LOAD_ATTR_SLOT | 322,005 | 33.3% |
| LOAD_FAST | 321,550 | 33.2% |
| SWAP | 680 | 0.1% |
| STORE_ATTR_INSTANCE_VALUE | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 643,395 | 66.5% |
| LOAD_FAST | 323,325 | 33.4% |
| SWAP | 680 | 0.1% |
| RETURN_VALUE | 240 | 0.0% |
| STORE_DEREF | 160 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| DICT_UPDATE | 720 | 33.0% |
| LOAD_FAST | 540 | 24.8% |
| BUILD_TUPLE | 240 | 11.0% |
| STORE_ATTR_INSTANCE_VALUE | 180 | 8.3% |
| STORE_FAST | 120 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 780 | 35.8% |
| EXTENDED_ARG | 580 | 26.6% |
| CALL_FUNCTION_EX | 320 | 14.7% |
| STORE_FAST | 280 | 12.8% |
| LOAD_CONST | 180 | 8.3% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 360 | 90.0% |
| LOAD_ATTR | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 400 | 100.0% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 320,665 | 100.0% |
| LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 320,665 | 100.0% |
| BINARY_SUBSCR | 60 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 641,705 | 47.5% |
| BINARY_OP | 366,585 | 27.2% |
| LOAD_FAST | 322,220 | 23.9% |
| LOAD_FAST_LOAD_FAST | 9,143 | 0.7% |
| LOAD_GLOBAL_BUILTIN | 9,060 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 641,705 | 47.5% |
| CALL_LIST_APPEND | 366,665 | 27.2% |
| LOAD_CONST | 321,100 | 23.8% |
| CALL_ISINSTANCE | 8,920 | 0.7% |
| CALL_PY_EXACT_ARGS | 8,623 | 0.6% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,107,436 | 69.0% |
| LOAD_FAST_LOAD_FAST | 660,948 | 7.5% |
| PUSH_NULL | 655,548 | 7.4% |
| LOAD_ATTR_INSTANCE_VALUE | 650,653 | 7.4% |
| LOAD_CONST | 339,648 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,817,047 | 77.0% |
| RETURN_VALUE | 690,510 | 7.8% |
| POP_TOP | 332,985 | 3.8% |
| RESUME_CHECK | 332,963 | 3.8% |
| LOAD_CONST | 320,865 | 3.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 695,625 | 68.3% |
| CALL_INTRINSIC_1 | 322,425 | 31.6% |
| DICT_MERGE | 460 | 0.0% |
| BUILD_MAP | 320 | 0.0% |
| LOAD_FAST | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,017,970 | 99.9% |
| STORE_FAST | 360 | 0.0% |
| RESUME_CHECK | 260 | 0.0% |
| GET_AWAITABLE | 160 | 0.0% |
| RETURN_VALUE | 140 | 0.0% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 322,785 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 322,425 | 99.9% |
| LOAD_CONST | 320 | 0.1% |
| BUILD_MAP | 40 | 0.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 341,208 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 329,085 | 96.4% |
| COPY_FREE_VARS | 8,023 | 2.4% |
| RESUME_CHECK | 1,360 | 0.4% |
| STORE_FAST | 1,200 | 0.4% |
| POP_TOP | 480 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 983,053 | 99.4% |
| COMPARE_OP | 2,380 | 0.2% |
| LOAD_CONST | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 940 | 0.1% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 985,313 | 99.6% |
| COMPARE_OP | 2,380 | 0.2% |
| COMPARE_OP_INT | 760 | 0.1% |
| POP_JUMP_IF_TRUE | 420 | 0.0% |
| COMPARE_OP_STR | 80 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 641,705 | 99.6% |
| LOAD_FAST | 900 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.1% |
| BUILD_SET | 400 | 0.1% |
| LOAD_GLOBAL_MODULE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 643,765 | 99.9% |
| POP_JUMP_IF_TRUE | 720 | 0.1% |
| STORE_FAST | 60 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 688,830 | 67.4% |
| CALL_LEN | 321,845 | 31.5% |
| LOAD_FAST | 9,840 | 1.0% |
| SWAP | 720 | 0.1% |
| UNARY_NOT | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 1,010,415 | 98.8% |
| LOAD_ATTR_WITH_HINT | 8,440 | 0.8% |
| LOAD_ATTR_INSTANCE_VALUE | 840 | 0.1% |
| COMPARE_OP_INT | 600 | 0.1% |
| TO_BOOL | 500 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 322,660 | 92.2% |
| CALL_PY_EXACT_ARGS | 10,183 | 2.9% |
| CALL_KW | 8,023 | 2.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 8,003 | 2.3% |
| LOAD_ATTR_PROPERTY | 580 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 349,089 | 99.7% |
| RESUME | 660 | 0.2% |
| RETURN_GENERATOR | 160 | 0.0% |
| MAKE_CELL | 80 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 420 | 91.3% |
| CALL | 40 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 460 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 740 | 97.4% |
| BUILD_CONST_KEY_MAP | 20 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 720 | 94.7% |
| EXTENDED_ARG | 20 | 2.6% |
| STORE_NAME | 20 | 2.6% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 4,845,030 | 70.7% |
| POP_TOP | 1,032,710 | 15.1% |
| JUMP_FORWARD | 641,055 | 9.4% |
| STORE_FAST | 320,265 | 4.7% |
| STORE_ATTR_WITH_HINT | 7,660 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 5,119,680 | 74.8% |
| CALL_FUNCTION_EX | 695,625 | 10.2% |
| FOR_ITER_RANGE | 321,785 | 4.7% |
| FOR_ITER_LIST | 320,865 | 4.7% |
| RETURN_GENERATOR | 320,265 | 4.7% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 9,480 | 56.6% |
| LOAD_CONST | 5,420 | 32.4% |
| BUILD_MAP | 580 | 3.5% |
| STORE_NAME | 360 | 2.2% |
| PUSH_NULL | 200 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,080 | 96.1% |
| FOR_ITER | 200 | 1.2% |
| JUMP_BACKWARD | 120 | 0.7% |
| POP_JUMP_IF_FALSE | 120 | 0.7% |
| FOR_ITER_LIST | 120 | 0.7% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 8,640 | 88.0% |
| JUMP_BACKWARD | 620 | 6.3% |
| FOR_ITER | 260 | 2.6% |
| EXTENDED_ARG | 200 | 2.0% |
| LOAD_FAST | 80 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,420 | 85.7% |
| RETURN_CONST | 480 | 4.9% |
| FOR_ITER_LIST | 280 | 2.9% |
| FOR_ITER | 260 | 2.6% |
| LOAD_FAST | 200 | 2.0% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 658,450 | 66.7% |
| LOAD_ATTR_INSTANCE_VALUE | 320,565 | 32.5% |
| LOAD_FAST | 8,160 | 0.8% |
| RETURN_VALUE | 240 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 987,835 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 60 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 40 | 66.7% |
| STORE_FAST | 20 | 33.3% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 40.0% |
| IMPORT_FROM | 60 | 30.0% |
| STORE_NAME | 60 | 30.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 820 | 36.0% |
| LOAD_FAST | 800 | 35.1% |
| LOAD_CONST | 560 | 24.6% |
| LOAD_FAST_LOAD_FAST | 80 | 3.5% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,600 | 70.2% |
| RETURN_VALUE | 400 | 17.5% |
| LOAD_DEREF | 160 | 7.0% |
| POP_JUMP_IF_TRUE | 120 | 5.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 322,282 | 46.5% |
| POP_JUMP_IF_TRUE | 320,985 | 46.4% |
| POP_TOP | 47,060 | 6.8% |
| CALL_LIST_APPEND | 600 | 0.1% |
| STORE_FAST | 580 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 367,565 | 53.1% |
| LOAD_FAST | 322,662 | 46.6% |
| FOR_ITER_RANGE | 900 | 0.1% |
| FOR_ITER | 620 | 0.1% |
| FOR_ITER_TUPLE | 360 | 0.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,307,860 | 80.3% |
| POP_EXCEPT | 320,945 | 19.7% |
| RESUME | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 979,055 | 60.1% |
| SEND | 329,285 | 20.2% |
| LOAD_FAST | 320,865 | 19.7% |
| LOAD_CONST | 80 | 0.0% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,312,871 | 99.3% |
| POP_JUMP_IF_FALSE | 6,396 | 0.5% |
| POP_TOP | 1,215 | 0.1% |
| STORE_ATTR_INSTANCE_VALUE | 480 | 0.0% |
| STORE_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 641,055 | 48.5% |
| LOAD_FAST | 351,006 | 26.6% |
| LOAD_GLOBAL_BUILTIN | 328,461 | 24.8% |
| LOAD_FAST_LOAD_FAST | 500 | 0.0% |
| LOAD_GLOBAL | 240 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_FAST | 560 | 82.4% |
| RETURN_GENERATOR | 80 | 11.8% |
| CALL_BUILTIN_CLASS | 40 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 600 | 88.2% |
| JUMP_BACKWARD | 80 | 11.8% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 322,005 | 99.7% |
| LOAD_FAST | 520 | 0.2% |
| BINARY_SLICE | 240 | 0.1% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 322,785 | 100.0% |
| LOAD_NAME | 60 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,794,512 | 52.6% |
| LOAD_GLOBAL_MODULE | 2,262,040 | 20.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,301,290 | 11.8% |
| LOAD_ATTR_WITH_HINT | 979,769 | 8.9% |
| LOAD_ATTR_SLOT | 322,405 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,922,855 | 35.6% |
| LOAD_FAST | 1,041,278 | 9.4% |
| COMPARE_OP | 983,053 | 8.9% |
| LOAD_CONST | 651,650 | 5.9% |
| LOAD_GLOBAL_MODULE | 643,025 | 5.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,637,119 | 18.5% |
| POP_TOP | 1,984,240 | 13.9% |
| LOAD_FAST | 1,656,917 | 11.6% |
| STORE_ATTR_SLOT | 1,329,199 | 9.3% |
| GET_AWAITABLE | 987,835 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,972,843 | 34.9% |
| STORE_FAST | 4,570,916 | 32.1% |
| COMPARE_OP_INT | 1,304,206 | 9.2% |
| SEND_GEN | 658,230 | 4.6% |
| CALL_PY_EXACT_ARGS | 641,970 | 4.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 649,143 | 39.3% |
| STORE_FAST | 328,983 | 19.9% |
| POP_JUMP_IF_FALSE | 321,160 | 19.4% |
| LOAD_CONST | 320,480 | 19.4% |
| LOAD_ATTR | 16,086 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 961,320 | 58.2% |
| LOAD_ATTR | 321,360 | 19.5% |
| STORE_ATTR_WITH_HINT | 320,360 | 19.4% |
| PUSH_NULL | 24,249 | 1.5% |
| LOAD_FAST | 13,043 | 0.8% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 17,568,594 | 16.7% |
| RESUME_CHECK | 16,820,037 | 16.0% |
| POP_JUMP_IF_FALSE | 13,916,680 | 13.2% |
| LOAD_ATTR_METHOD_NO_DICT | 12,310,543 | 11.7% |
| POP_JUMP_IF_TRUE | 9,153,377 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 23,161,305 | 22.0% |
| TO_BOOL_BOOL | 10,570,733 | 10.0% |
| LOAD_ATTR_WITH_HINT | 7,548,116 | 7.2% |
| RETURN_VALUE | 7,120,258 | 6.8% |
| TO_BOOL | 6,430,146 | 6.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 680 | 100.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,478,885 | 87.5% |
| STORE_FAST | 320,530 | 6.3% |
| LOAD_ATTR_METHOD_NO_DICT | 320,530 | 6.3% |
| POP_TOP | 240 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,478,845 | 87.5% |
| LOAD_FAST | 320,550 | 6.3% |
| CALL_METHOD_DESCRIPTOR_O | 320,490 | 6.3% |
| POP_JUMP_IF_NOT_NONE | 240 | 0.0% |
| CALL | 79 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,979,884 | 26.6% |
| STORE_FAST | 1,387,936 | 18.7% |
| POP_JUMP_IF_FALSE | 988,713 | 13.3% |
| LOAD_ATTR_METHOD_NO_DICT | 742,993 | 10.0% |
| PUSH_NULL | 669,991 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 2,640,572 | 35.5% |
| LOAD_ATTR_WITH_HINT | 1,949,260 | 26.2% |
| LOAD_FAST | 1,031,233 | 13.9% |
| CALL | 660,948 | 8.9% |
| LOAD_FAST_LOAD_FAST | 654,485 | 8.8% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,960 | 14.0% |
| LOAD_ATTR | 1,460 | 10.4% |
| RESUME_CHECK | 1,100 | 7.9% |
| RESUME | 1,080 | 7.7% |
| STORE_FAST | 1,040 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 4,740 | 33.9% |
| LOAD_ATTR | 3,100 | 22.2% |
| LOAD_GLOBAL_BUILTIN | 2,260 | 16.2% |
| LOAD_FAST | 1,140 | 8.2% |
| CALL | 620 | 4.4% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 200 | 26.3% |
| STORE_NAME | 120 | 15.8% |
| LOAD_CONST | 100 | 13.2% |
| RESUME | 100 | 13.2% |
| BINARY_OP | 80 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 480 | 63.2% |
| LOAD_ATTR | 140 | 18.4% |
| STORE_NAME | 100 | 13.2% |
| LOAD_NAME | 40 | 5.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 980 | 96.1% |
| LOAD_GLOBAL | 20 | 2.0% |
| LOAD_GLOBAL_MODULE | 20 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 440 | 43.1% |
| LOAD_FAST | 200 | 19.6% |
| CALL | 160 | 15.7% |
| LOAD_FAST_LOAD_FAST | 100 | 9.8% |
| LOAD_SUPER_ATTR_ATTR | 60 | 5.9% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 320,600 | 99.6% |
| MAKE_CELL | 880 | 0.3% |
| CALL_KW | 160 | 0.0% |
| CACHE | 80 | 0.0% |
| CALL_FUNCTION_EX | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 320,720 | 99.6% |
| MAKE_CELL | 880 | 0.3% |
| RETURN_GENERATOR | 240 | 0.1% |
| RESUME | 80 | 0.0% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 12,920 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| EXTENDED_ARG | 9,480 | 73.4% |
| LOAD_CONST | 2,680 | 20.7% |
| DICT_UPDATE | 740 | 5.7% |
| BUILD_MAP | 20 | 0.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 16,597,824 | 61.4% |
| COMPARE_OP_INT | 4,340,319 | 16.1% |
| TO_BOOL_INT | 1,813,825 | 6.7% |
| TO_BOOL_NONE | 1,305,730 | 4.8% |
| COMPARE_OP | 985,313 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,916,680 | 51.5% |
| LOAD_FAST_CHECK | 4,478,885 | 16.6% |
| LOAD_CONST | 2,637,119 | 9.8% |
| RETURN_CONST | 1,680,071 | 6.2% |
| NOP | 1,329,870 | 4.9% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,423,923 | 86.8% |
| LOAD_ATTR_INSTANCE_VALUE | 979,435 | 13.2% |
| LOAD_ATTR | 960 | 0.0% |
| LOAD_ATTR_WITH_HINT | 280 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,080,673 | 95.6% |
| LOAD_CONST | 321,125 | 4.3% |
| RETURN_CONST | 1,520 | 0.0% |
| LOAD_GLOBAL_MODULE | 440 | 0.0% |
| LOAD_FAST_LOAD_FAST | 400 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,043,616 | 76.3% |
| LOAD_ATTR_INSTANCE_VALUE | 321,905 | 23.5% |
| LOAD_ATTR_WITH_HINT | 600 | 0.0% |
| LOAD_GLOBAL_MODULE | 480 | 0.0% |
| CALL_BUILTIN_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 702,593 | 51.4% |
| LOAD_GLOBAL_MODULE | 331,743 | 24.3% |
| LOAD_FAST_LOAD_FAST | 330,425 | 24.2% |
| RETURN_CONST | 620 | 0.0% |
| LOAD_GLOBAL | 600 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 7,163,753 | 62.3% |
| TO_BOOL_BOOL | 2,689,263 | 23.4% |
| TO_BOOL_INT | 1,330,740 | 11.6% |
| COMPARE_OP_INT | 321,705 | 2.8% |
| TO_BOOL_STR | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,153,377 | 79.5% |
| NOP | 658,416 | 5.7% |
| RETURN_CONST | 367,285 | 3.2% |
| LOAD_CONST | 362,528 | 3.2% |
| STORE_FAST | 321,865 | 2.8% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 80 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 80 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 80 | 100.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 4,694,017 | 46.7% |
| POP_JUMP_IF_FALSE | 1,680,071 | 16.7% |
| STORE_FAST | 1,339,675 | 13.3% |
| STORE_ATTR_SLOT | 669,611 | 6.7% |
| STORE_ATTR_INSTANCE_VALUE | 643,825 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,365,851 | 83.2% |
| INTERPRETER_EXIT | 1,353,473 | 13.5% |
| END_SEND | 337,145 | 3.4% |
| EXIT_INIT_CHECK | 580 | 0.0% |
| STORE_FAST | 460 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 329,605 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 329,285 | 49.9% |
| SEND | 720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 328,985 | 49.9% |
| YIELD_VALUE | 328,985 | 49.9% |
| SEND | 720 | 0.1% |
| POP_TOP | 460 | 0.1% |
| SEND_GEN | 460 | 0.1% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 321,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 320,940 | 99.9% |
| LOAD_FAST_LOAD_FAST | 80 | 0.0% |
| LOAD_GLOBAL_MODULE | 80 | 0.0% |
| STORE_NAME | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,340 | 66.3% |
| LOAD_FAST_LOAD_FAST | 2,520 | 20.0% |
| STORE_ATTR | 680 | 5.4% |
| SWAP | 400 | 3.2% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 3,560 | 28.3% |
| LOAD_FAST | 2,760 | 21.9% |
| LOAD_CONST | 1,760 | 14.0% |
| RETURN_CONST | 1,000 | 7.9% |
| STORE_ATTR | 680 | 5.4% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 320 | 36.4% |
| BUILD_LIST | 160 | 18.2% |
| CALL_KW | 160 | 18.2% |
| BINARY_OP_ADD_INT | 120 | 13.6% |
| CALL | 80 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 54.5% |
| LOAD_CONST | 160 | 18.2% |
| BUILD_LIST | 80 | 9.1% |
| LOAD_DEREF | 80 | 9.1% |
| LOAD_FAST_LOAD_FAST | 80 | 9.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 7,784,422 | 29.6% |
| CALL | 6,817,047 | 26.0% |
| LOAD_CONST | 4,570,916 | 17.4% |
| CALL_LEN | 697,147 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 689,030 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 17,568,594 | 66.9% |
| LOAD_FAST_LOAD_FAST | 1,387,936 | 5.3% |
| LOAD_GLOBAL_BUILTIN | 1,356,040 | 5.2% |
| RETURN_CONST | 1,339,675 | 5.1% |
| JUMP_FORWARD | 1,312,871 | 5.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 560 | 90.3% |
| CALL_LEN | 40 | 6.5% |
| COPY | 20 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 560 | 90.3% |
| PUSH_NULL | 40 | 6.5% |
| LOAD_ATTR | 20 | 3.2% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,063,798 | 99.9% |
| UNPACK_SEQUENCE | 300 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 160 | 0.0% |
| COPY | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,063,118 | 99.9% |
| LOAD_FAST_LOAD_FAST | 340 | 0.0% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |
| STORE_FAST | 180 | 0.0% |
| NOP | 160 | 0.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 20 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20 | 100.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 500 | 43.1% |
| CALL | 220 | 19.0% |
| LOAD_CONST | 160 | 13.8% |
| LOAD_NAME | 100 | 8.6% |
| IMPORT_NAME | 60 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 400 | 34.5% |
| EXTENDED_ARG | 360 | 31.0% |
| LOAD_NAME | 120 | 10.3% |
| RETURN_CONST | 120 | 10.3% |
| LOAD_BUILD_CLASS | 100 | 8.6% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 375,008 | 96.6% |
| BINARY_OP_SUBTRACT_INT | 8,400 | 2.2% |
| BINARY_OP_ADD_INT | 1,080 | 0.3% |
| BUILD_LIST | 680 | 0.2% |
| LOAD_FAST_AND_CLEAR | 680 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 375,608 | 96.7% |
| STORE_ATTR_WITH_HINT | 8,440 | 2.2% |
| STORE_ATTR_INSTANCE_VALUE | 840 | 0.2% |
| COPY | 720 | 0.2% |
| BUILD_LIST | 680 | 0.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 160 | 21.1% |
| STORE_FAST | 160 | 21.1% |
| END_SEND | 120 | 15.8% |
| LOAD_FAST | 80 | 10.5% |
| FOR_ITER_LIST | 80 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 320 | 42.1% |
| STORE_FAST_STORE_FAST | 300 | 39.5% |
| UNPACK_SEQUENCE_TUPLE | 60 | 7.9% |
| STORE_FAST | 40 | 5.3% |
| POP_TOP | 20 | 2.6% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 979,355 | 74.8% |
| SEND | 328,985 | 25.1% |
| LOAD_CONST | 160 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 979,355 | 74.8% |
| INTERPRETER_EXIT | 329,225 | 25.2% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,940 | 52.3% |
| CACHE | 920 | 16.4% |
| COPY_FREE_VARS | 660 | 11.7% |
| POP_TOP | 480 | 8.5% |
| SEND_GEN | 400 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,940 | 52.3% |
| LOAD_GLOBAL | 1,080 | 19.2% |
| JUMP_BACKWARD_NO_INTERRUPT | 480 | 8.5% |
| LOAD_CONST | 340 | 6.0% |
| NOP | 260 | 4.6% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 321,825 | 99.9% |
| LOAD_FAST | 280 | 0.1% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 321,845 | 99.9% |
| LOAD_FAST | 300 | 0.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 337,425 | 51.1% |
| CALL_LEN | 320,905 | 48.6% |
| LOAD_CONST | 1,240 | 0.2% |
| BINARY_OP | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,445 | 51.1% |
| STORE_FAST | 320,765 | 48.6% |
| SWAP | 1,080 | 0.2% |
| BINARY_SLICE | 160 | 0.0% |
| LOAD_FAST | 120 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 600 | 85.7% |
| BINARY_SUBSCR_LIST_INT | 80 | 11.4% |
| BINARY_OP | 20 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 68.6% |
| CALL | 120 | 17.1% |
| STORE_FAST | 80 | 11.4% |
| LOAD_GLOBAL | 20 | 2.9% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 120 | 85.7% |
| BINARY_OP | 20 | 14.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 120 | 85.7% |
| CALL | 20 | 14.3% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,545 | 99.9% |
| LOAD_CONST | 320 | 0.1% |
| BINARY_OP | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 320,585 | 99.9% |
| STORE_FAST | 300 | 0.1% |
| COMPARE_OP | 40 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 40 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 120 | 60.0% |
| BINARY_OP | 40 | 20.0% |
| LOAD_FAST | 40 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,040 | 48.6% |
| LOAD_FAST_LOAD_FAST | 7,960 | 48.1% |
| LOAD_CONST | 400 | 2.4% |
| BINARY_OP | 100 | 0.6% |
| CALL_LEN | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 8,400 | 50.8% |
| STORE_FAST | 8,000 | 48.4% |
| LOAD_FAST | 60 | 0.4% |
| RETURN_VALUE | 40 | 0.2% |
| LOAD_FAST_LOAD_FAST | 40 | 0.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 8,063 | 82.1% |
| LOAD_FAST | 1,580 | 16.1% |
| BINARY_SUBSCR | 80 | 0.8% |
| LOAD_CONST | 80 | 0.8% |
| BUILD_TUPLE | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,203 | 83.5% |
| RETURN_VALUE | 940 | 9.6% |
| PUSH_EXC_INFO | 520 | 5.3% |
| LOAD_FAST | 120 | 1.2% |
| CALL_BUILTIN_CLASS | 40 | 0.4% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 80 | 80.0% |
| LOAD_FAST | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 100 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,072 | 99.1% |
| BINARY_SUBSCR | 100 | 0.8% |
| LOAD_FAST | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 6,656 | 50.5% |
| STORE_FAST | 6,276 | 47.6% |
| BINARY_OP_ADD_UNICODE | 80 | 0.6% |
| LOAD_ATTR | 60 | 0.5% |
| RETURN_VALUE | 40 | 0.3% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 80 | 36.4% |
| LOAD_CONST | 80 | 36.4% |
| LOAD_FAST | 60 | 27.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100 | 45.5% |
| STORE_FAST | 100 | 45.5% |
| PUSH_EXC_INFO | 20 | 9.1% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 200 | 55.6% |
| RETURN_VALUE | 80 | 22.2% |
| LOAD_GLOBAL_MODULE | 80 | 22.2% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 50.0% |
| LOAD_FAST_LOAD_FAST | 160 | 26.7% |
| CALL | 80 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 6.7% |
| LOAD_GLOBAL_MODULE | 20 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 580 | 96.7% |
| STORE_FAST | 20 | 3.3% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,865 | 97.4% |
| CALL_BUILTIN_CLASS | 7,983 | 2.4% |
| LOAD_CONST | 360 | 0.1% |
| LOAD_FAST | 220 | 0.1% |
| PUSH_NULL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 321,285 | 97.5% |
| COPY_FREE_VARS | 8,003 | 2.4% |
| POP_TOP | 240 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 330,228 | 85.8% |
| LOAD_ATTR_INSTANCE_VALUE | 53,560 | 13.9% |
| CALL | 280 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.1% |
| LOAD_CONST | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 322,105 | 83.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 53,400 | 13.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 7,983 | 2.1% |
| STORE_FAST | 540 | 0.1% |
| LOAD_FAST | 240 | 0.1% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,060 | 59.6% |
| LOAD_FAST | 320 | 18.0% |
| LOAD_ATTR_SLOT | 180 | 10.1% |
| CALL | 120 | 6.7% |
| LOAD_FAST_LOAD_FAST | 60 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 560 | 31.5% |
| TO_BOOL_BOOL | 520 | 29.2% |
| POP_JUMP_IF_NOT_NONE | 360 | 20.2% |
| COPY | 220 | 12.4% |
| TO_BOOL | 60 | 3.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 53,400 | 98.7% |
| LOAD_FAST | 400 | 0.7% |
| LOAD_CONST | 120 | 0.2% |
| RETURN_GENERATOR | 80 | 0.1% |
| CALL_STR_1 | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 53,780 | 99.4% |
| STORE_FAST | 260 | 0.5% |
| BEFORE_WITH | 40 | 0.1% |
| BUILD_TUPLE | 20 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 440 | 38.6% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 24.6% |
| CALL | 120 | 10.5% |
| BINARY_OP_MULTIPLY_FLOAT | 120 | 10.5% |
| LOAD_CONST | 80 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 500 | 43.9% |
| STORE_FAST | 300 | 26.3% |
| LOAD_CONST | 140 | 12.3% |
| BUILD_TUPLE | 80 | 7.0% |
| TO_BOOL_INT | 60 | 5.3% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 19,126 | 66.0% |
| BUILD_TUPLE | 8,920 | 30.8% |
| CALL | 380 | 1.3% |
| LOAD_GLOBAL_MODULE | 360 | 1.2% |
| LOAD_ATTR_MODULE | 160 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 28,546 | 98.5% |
| TO_BOOL | 380 | 1.3% |
| RETURN_VALUE | 40 | 0.1% |
| LOAD_FAST | 20 | 0.1% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,606,620 | 54.3% |
| LOAD_FAST | 1,033,375 | 34.9% |
| LOAD_ATTR_WITH_HINT | 320,865 | 10.8% |
| CALL | 320 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 697,147 | 23.5% |
| TO_BOOL_INT | 650,270 | 22.0% |
| LOAD_FAST | 641,345 | 21.7% |
| COPY | 321,845 | 10.9% |
| LOAD_CONST | 321,185 | 10.8% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,479,065 | 92.4% |
| BUILD_TUPLE | 366,665 | 7.6% |
| CALL | 120 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 4,845,030 | 100.0% |
| JUMP_BACKWARD | 600 | 0.0% |
| JUMP_FORWARD | 140 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 329,545 | 49.8% |
| LOAD_FAST | 321,265 | 48.6% |
| LOAD_FAST_LOAD_FAST | 8,943 | 1.4% |
| LOAD_GLOBAL_MODULE | 680 | 0.1% |
| RETURN_VALUE | 360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 651,090 | 98.5% |
| RETURN_VALUE | 9,103 | 1.4% |
| LIST_APPEND | 560 | 0.1% |
| POP_TOP | 220 | 0.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 321,825 | 99.5% |
| LOAD_FAST | 480 | 0.1% |
| LOAD_ATTR | 360 | 0.1% |
| LOAD_CONST | 280 | 0.1% |
| CALL | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 322,005 | 99.6% |
| POP_TOP | 1,020 | 0.3% |
| RETURN_VALUE | 140 | 0.0% |
| LOAD_CONST | 40 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 369,882 | 52.8% |
| LOAD_ATTR | 329,225 | 47.0% |
| CALL | 840 | 0.1% |
| LOAD_FAST | 360 | 0.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 367,622 | 52.5% |
| TO_BOOL_BOOL | 329,345 | 47.0% |
| POP_TOP | 920 | 0.1% |
| RETURN_VALUE | 700 | 0.1% |
| LOAD_FAST | 460 | 0.1% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,370,795 | 66.8% |
| BINARY_SLICE | 358,322 | 17.5% |
| LOAD_FAST_CHECK | 320,490 | 15.6% |
| CALL | 820 | 0.0% |
| LOAD_CONST | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,722,157 | 83.9% |
| CALL_PY_EXACT_ARGS | 320,490 | 15.6% |
| RETURN_VALUE | 8,560 | 0.4% |
| LOAD_CONST | 280 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 3,922,855 | 34.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,812,147 | 33.3% |
| LOAD_FAST | 2,405,822 | 21.0% |
| LOAD_CONST | 641,970 | 5.6% |
| LOAD_ATTR_METHOD_NO_DICT | 330,848 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,785,122 | 94.2% |
| RETURN_GENERATOR | 337,525 | 2.9% |
| MAKE_CELL | 320,600 | 2.8% |
| COPY_FREE_VARS | 10,183 | 0.1% |
| RESUME | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 5,119,680 | 93.9% |
| LOAD_ATTR | 321,345 | 5.9% |
| LOAD_FAST | 9,163 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 360 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,451,488 | 100.0% |
| RETURN_GENERATOR | 120 | 0.0% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 80 | 66.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 40 | 33.3% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 80 | 80.0% |
| LOAD_FAST | 20 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 80 | 80.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 20 | 20.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 980 | 94.2% |
| LOAD_GLOBAL_MODULE | 40 | 3.8% |
| CALL | 20 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 740 | 71.2% |
| LOAD_GLOBAL_MODULE | 200 | 19.2% |
| PUSH_NULL | 40 | 3.8% |
| LOAD_FAST_LOAD_FAST | 40 | 3.8% |
| LOAD_GLOBAL | 20 | 1.9% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,256 | 95.7% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 1.8% |
| LOAD_ATTR_SLOT | 120 | 1.8% |
| COMPARE_OP | 40 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,396 | 97.9% |
| RETURN_VALUE | 140 | 2.1% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 1,949,140 | 41.8% |
| LOAD_CONST | 1,304,206 | 28.0% |
| LOAD_GLOBAL_MODULE | 321,865 | 6.9% |
| LOAD_FAST | 321,585 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 320,585 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,340,319 | 93.1% |
| POP_JUMP_IF_TRUE | 321,705 | 6.9% |
| RETURN_VALUE | 60 | 0.0% |
| STORE_FAST | 40 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 740 | 75.5% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 12.2% |
| COMPARE_OP | 80 | 8.2% |
| LOAD_FAST | 40 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 840 | 85.7% |
| COPY | 60 | 6.1% |
| STORE_FAST | 60 | 6.1% |
| EXTENDED_ARG | 20 | 2.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 644,610 | 48.3% |
| JUMP_BACKWARD | 367,565 | 27.6% |
| ENTER_EXECUTOR | 320,865 | 24.1% |
| FOR_ITER | 280 | 0.0% |
| EXTENDED_ARG | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 687,870 | 51.6% |
| RETURN_CONST | 322,045 | 24.2% |
| LOAD_FAST | 321,945 | 24.1% |
| STORE_FAST | 1,120 | 0.1% |
| LOAD_DEREF | 140 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 322,025 | 49.9% |
| ENTER_EXECUTOR | 321,785 | 49.9% |
| JUMP_BACKWARD | 900 | 0.1% |
| FOR_ITER | 60 | 0.0% |
| SWAP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 322,765 | 50.1% |
| LOAD_CONST | 321,865 | 49.9% |
| LOAD_FAST | 100 | 0.0% |
| SWAP | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,260 | 85.3% |
| SWAP | 560 | 5.8% |
| GET_ITER | 460 | 4.8% |
| JUMP_BACKWARD | 360 | 3.7% |
| FOR_ITER | 40 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 8,000 | 82.6% |
| STORE_FAST_LOAD_FAST | 560 | 5.8% |
| SWAP | 560 | 5.8% |
| STORE_FAST | 460 | 4.8% |
| LOAD_GLOBAL | 40 | 0.4% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 360 | 94.7% |
| LOAD_ATTR | 20 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 380 | 100.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 23,161,305 | 99.9% |
| LOAD_FAST_LOAD_FAST | 9,503 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 9,043 | 0.0% |
| LOAD_ATTR | 4,880 | 0.0% |
| COPY | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 7,467,333 | 32.2% |
| TO_BOOL_BOOL | 3,921,073 | 16.9% |
| CALL_LEN | 1,606,620 | 6.9% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,358,759 | 5.9% |
| LOAD_ATTR | 1,301,290 | 5.6% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 7,467,333 | 51.8% |
| LOAD_FAST_CHECK | 4,478,845 | 31.1% |
| LOAD_FAST | 1,112,615 | 7.7% |
| LOAD_ATTR_WITH_HINT | 650,930 | 4.5% |
| LOAD_ATTR | 376,908 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,310,543 | 85.4% |
| LOAD_FAST_LOAD_FAST | 742,993 | 5.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 369,882 | 2.6% |
| CALL_PY_EXACT_ARGS | 330,848 | 2.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 329,545 | 2.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,145,676 | 57.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,358,759 | 18.9% |
| LOAD_ATTR_WITH_HINT | 995,971 | 13.9% |
| LOAD_ATTR_SLOT | 677,294 | 9.4% |
| RETURN_VALUE | 9,023 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 3,812,147 | 53.0% |
| LOAD_FAST | 2,074,497 | 28.8% |
| LOAD_FAST_LOAD_FAST | 660,088 | 9.2% |
| LOAD_CONST | 641,335 | 8.9% |
| CALL | 1,820 | 0.0% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,440,534 | 99.9% |
| LOAD_ATTR | 2,280 | 0.1% |
| LOAD_FAST | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,692,401 | 69.3% |
| BINARY_OP | 741,053 | 30.3% |
| CALL | 1,280 | 0.1% |
| LOAD_FAST | 1,080 | 0.0% |
| LOAD_CONST | 1,040 | 0.0% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 740 | 84.1% |
| LOAD_ATTR | 120 | 13.6% |
| LOAD_FAST_LOAD_FAST | 20 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 580 | 65.9% |
| CALL | 140 | 15.9% |
| BINARY_OP | 120 | 13.6% |
| CALL_ISINSTANCE | 20 | 2.3% |
| LOAD_GLOBAL_BUILTIN | 20 | 2.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 321,405 | 99.9% |
| LOAD_ATTR | 220 | 0.1% |
| LOAD_DEREF | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 321,245 | 99.8% |
| COPY_FREE_VARS | 580 | 0.2% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,117,453 | 99.6% |
| LOAD_FAST_LOAD_FAST | 7,980 | 0.2% |
| BINARY_SUBSCR_LIST_INT | 6,656 | 0.2% |
| LOAD_ATTR | 940 | 0.0% |
| LOAD_ATTR_MODULE | 820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 1,303,210 | 31.5% |
| TO_BOOL_BOOL | 1,124,134 | 27.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 677,294 | 16.4% |
| LOAD_ATTR | 322,405 | 7.8% |
| BUILD_LIST | 322,005 | 7.8% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,548,116 | 72.1% |
| LOAD_FAST_LOAD_FAST | 1,949,260 | 18.6% |
| LOAD_DEREF | 961,320 | 9.2% |
| COPY | 8,440 | 0.1% |
| LOAD_ATTR | 1,839 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,614,565 | 25.0% |
| COMPARE_OP_INT | 1,949,140 | 18.6% |
| LOAD_GLOBAL_MODULE | 1,614,115 | 15.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 995,971 | 9.5% |
| LOAD_ATTR | 979,769 | 9.4% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,356,040 | 32.5% |
| POP_JUMP_IF_FALSE | 636,489 | 15.3% |
| LOAD_GLOBAL_BUILTIN | 445,305 | 10.7% |
| RESUME_CHECK | 406,391 | 9.7% |
| LOAD_FAST | 348,611 | 8.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,690,156 | 88.5% |
| LOAD_GLOBAL_BUILTIN | 445,305 | 10.7% |
| CALL_ISINSTANCE | 19,126 | 0.5% |
| BUILD_TUPLE | 9,060 | 0.2% |
| LOAD_DEREF | 4,200 | 0.1% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,749,025 | 27.0% |
| LOAD_ATTR_WITH_HINT | 1,614,115 | 24.9% |
| RESUME_CHECK | 1,353,235 | 20.9% |
| LOAD_ATTR | 643,025 | 9.9% |
| POP_TOP | 375,848 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,440,534 | 37.7% |
| LOAD_ATTR | 2,262,040 | 34.9% |
| BINARY_OP | 1,010,375 | 15.6% |
| COMPARE_OP_INT | 321,865 | 5.0% |
| CHECK_EXC_MATCH | 321,005 | 5.0% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 640 | 78.0% |
| LOAD_GLOBAL_MODULE | 120 | 14.6% |
| LOAD_SUPER_ATTR | 60 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 640 | 78.0% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 14.6% |
| LOAD_GLOBAL | 40 | 4.9% |
| LOAD_ATTR | 20 | 2.4% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,080 | 87.5% |
| LOAD_SUPER_ATTR | 440 | 12.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,400 | 39.8% |
| LOAD_FAST_LOAD_FAST | 1,220 | 34.7% |
| CALL_PY_EXACT_ARGS | 760 | 21.6% |
| CALL | 140 | 4.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 10,785,122 | 50.1% |
| CALL_PY_WITH_DEFAULTS | 5,451,488 | 25.3% |
| CACHE | 2,020,868 | 9.4% |
| SEND_GEN | 978,955 | 4.5% |
| POP_TOP | 658,850 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,820,037 | 78.1% |
| LOAD_GLOBAL_MODULE | 1,353,235 | 6.3% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,307,860 | 6.1% |
| LOAD_DEREF | 649,143 | 3.0% |
| LOAD_CONST | 644,065 | 3.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 979,055 | 59.8% |
| LOAD_CONST | 658,230 | 40.2% |
| SEND | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 978,955 | 59.8% |
| POP_TOP | 658,390 | 40.2% |
| RESUME | 400 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,629,755 | 99.4% |
| LOAD_FAST_LOAD_FAST | 4,200 | 0.3% |
| STORE_ATTR | 3,560 | 0.2% |
| SWAP | 840 | 0.1% |
| LOAD_DEREF | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 661,565 | 40.4% |
| RETURN_CONST | 643,825 | 39.3% |
| NOP | 320,625 | 19.6% |
| LOAD_CONST | 6,200 | 0.4% |
| LOAD_FAST_LOAD_FAST | 2,140 | 0.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,640,572 | 56.6% |
| LOAD_FAST | 2,023,493 | 43.4% |
| STORE_ATTR | 560 | 0.0% |
| STORE_ATTR_SLOT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,979,884 | 42.4% |
| LOAD_CONST | 1,329,199 | 28.5% |
| LOAD_FAST | 669,971 | 14.4% |
| RETURN_CONST | 669,611 | 14.4% |
| NOP | 15,960 | 0.3% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 353,120 | 51.1% |
| LOAD_DEREF | 320,360 | 46.4% |
| SWAP | 8,440 | 1.2% |
| ENTER_EXECUTOR | 7,600 | 1.1% |
| LOAD_FAST_LOAD_FAST | 1,120 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 337,320 | 48.8% |
| RETURN_CONST | 329,420 | 47.7% |
| NOP | 15,800 | 2.3% |
| ENTER_EXECUTOR | 7,660 | 1.1% |
| LOAD_CONST | 420 | 0.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 8,343 | 88.9% |
| LOAD_FAST | 480 | 5.1% |
| LOAD_CONST | 280 | 3.0% |
| STORE_SUBSCR | 160 | 1.7% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,683 | 92.5% |
| NOP | 220 | 2.3% |
| LOAD_CONST | 140 | 1.5% |
| RETURN_CONST | 140 | 1.5% |
| LOAD_GLOBAL_MODULE | 120 | 1.3% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 40 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 20 | 50.0% |
| RETURN_CONST | 20 | 50.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 280 | 70.0% |
| TO_BOOL | 80 | 20.0% |
| TO_BOOL_NONE | 40 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 260 | 65.0% |
| POP_JUMP_IF_TRUE | 140 | 35.0% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,570,733 | 54.8% |
| LOAD_ATTR_INSTANCE_VALUE | 3,921,073 | 20.3% |
| LOAD_ATTR_WITH_HINT | 2,614,565 | 13.6% |
| LOAD_ATTR_SLOT | 1,124,134 | 5.8% |
| RETURN_VALUE | 694,251 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,597,824 | 86.1% |
| POP_JUMP_IF_TRUE | 2,689,263 | 13.9% |
| UNARY_NOT | 340 | 0.0% |
| EXTENDED_ARG | 100 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,010,415 | 32.1% |
| BINARY_OP | 733,670 | 23.3% |
| CALL_LEN | 650,270 | 20.7% |
| LOAD_FAST | 375,025 | 11.9% |
| LOAD_ATTR_INSTANCE_VALUE | 374,705 | 11.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,813,825 | 57.7% |
| POP_JUMP_IF_TRUE | 1,330,740 | 42.3% |
| UNARY_NOT | 80 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 644,990 | 99.9% |
| LOAD_FAST | 360 | 0.1% |
| TO_BOOL | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 645,250 | 100.0% |
| POP_JUMP_IF_TRUE | 280 | 0.0% |
| UNARY_NOT | 20 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,303,210 | 99.8% |
| LOAD_FAST | 1,700 | 0.1% |
| LOAD_ATTR | 600 | 0.0% |
| TO_BOOL | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,305,730 | 100.0% |
| TO_BOOL_ALWAYS_TRUE | 40 | 0.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 560 | 46.7% |
| LOAD_FAST | 400 | 33.3% |
| COPY | 160 | 13.3% |
| TO_BOOL | 80 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 840 | 70.0% |
| POP_JUMP_IF_FALSE | 360 | 30.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 80 | 28.6% |
| CALL_METHOD_DESCRIPTOR_O | 80 | 28.6% |
| UNPACK_SEQUENCE | 60 | 21.4% |
| BINARY_SUBSCR_LIST_INT | 40 | 14.3% |
| RETURN_VALUE | 20 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 160 | 57.1% |
| POP_TOP | 60 | 21.4% |
| STORE_FAST | 60 | 21.4% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 687,870 | 64.7% |
| STORE_FAST | 374,848 | 35.2% |
| RETURN_VALUE | 480 | 0.0% |
| UNPACK_SEQUENCE | 320 | 0.0% |
| BINARY_SLICE | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,063,798 | 100.0% |
| STORE_FAST | 100 | 0.0% |
| LOAD_FAST | 60 | 0.0% |


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
|     deferred | 2,167,413 | 61.7% |
|          hit | 1,339,760 | 38.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 15.7% |
| Failure | 2,580 | 84.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 1,780 | 69.0% |
| or | 600 | 23.3% |
| floor divide | 120 | 4.7% |
| multiply different types | 60 | 2.3% |
| add different types | 20 | 0.8% |


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
|     deferred | 8,460 | 20.0% |
|          hit | 33,575 | 79.2% |
|         miss | 140 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 180 | 50.0% |
| Failure | 180 | 50.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 140 | 77.8% |
| out of range | 20 | 11.1% |
| buffer slice | 20 | 11.1% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,836,718 | 22.0% |
|          hit | 31,382,305 | 78.0% |
|         miss | 2,820 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,379 | 51.0% |
| Failure | 8,060 | 49.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 1,960 | 24.3% |
| class no vectorcall | 1,340 | 16.6% |
| code complex parameters | 900 | 11.2% |
| cfunc noargs | 800 | 9.9% |
| meth descr method fastcall keywords | 760 | 9.4% |
| no dict | 640 | 7.9% |
| other | 380 | 4.7% |
| cfunc varargs keywords | 340 | 4.2% |
| meth descr varargs keywords | 260 | 3.2% |
| class mutable | 220 | 2.7% |
| operator wrapper | 140 | 1.7% |
| metaclass | 140 | 1.7% |
| cfunc varargs | 100 | 1.2% |
| wrong number arguments | 40 | 0.5% |
| cmethod | 40 | 0.5% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 985,993 | 17.4% |
|          hit | 4,669,500 | 82.5% |
|         miss | 180 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 880 | 27.0% |
| Failure | 2,380 | 73.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| baseobject | 1,780 | 74.8% |
| other | 220 | 9.2% |
| tuple | 140 | 5.9% |
| different types | 120 | 5.0% |
| float long | 80 | 3.4% |
| bool | 40 | 1.7% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 9,180 | 0.5% |
|          hit | 1,987,990 | 99.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 59.4% |
| Failure | 260 | 40.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 140 | 53.8% |
| dict items | 80 | 30.8% |
| set | 40 | 15.4% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,994,384 | 12.3% |
|          hit | 78,383,462 | 87.7% |
|         miss | 3,640 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 15,758 | 49.4% |
| Failure | 16,140 | 50.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 7,720 | 47.8% |
| metaclass attribute | 3,440 | 21.3% |
| not managed dict | 2,660 | 16.5% |
| method | 1,200 | 7.4% |
| shadowed | 720 | 4.5% |
| class method obj | 180 | 1.1% |
| non object slot | 80 | 0.5% |
| class attr descriptor | 60 | 0.4% |
| class attr simple | 40 | 0.2% |
| module attr not found | 20 | 0.1% |
| builtin class method | 20 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,160 | 0.1% |
|        deopt | 80 | 0.0% |
|          hit | 10,650,032 | 99.9% |
|         miss | 180 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 7,000 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 520 | 9.7% |
|          hit | 4,340 | 81.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 500 | 100.0% |
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
|     deferred | 658,430 | 28.7% |
|          hit | 1,637,745 | 71.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 460 | 39.0% |
| Failure | 720 | 61.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 720 | 100.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,540 | 0.2% |
|          hit | 6,988,520 | 99.7% |
|         miss | 6,260 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,620 | 87.2% |
| Failure | 680 | 12.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 320 | 47.1% |
| overridden | 80 | 11.8% |
| overriding descriptor | 80 | 11.8% |
| not in dict | 80 | 11.8% |
| no dict | 40 | 5.9% |
| property | 40 | 5.9% |
| not in keys | 40 | 5.9% |


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
|     deferred | 640 | 6.2% |
|          hit | 9,423 | 91.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 160 | 72.7% |
| Failure | 60 | 27.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 40 | 66.7% |
| bytearray int | 20 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,513,061 | 22.5% |
|          hit | 25,830,062 | 77.4% |
|         miss | 180 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 4,000 | 45.7% |
| Failure | 4,760 | 54.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 2,420 | 50.8% |
| sequence | 1,380 | 29.0% |
| bytearray | 260 | 5.5% |
| mapping | 260 | 5.5% |
| dict | 160 | 3.4% |
| memory view | 140 | 2.9% |
| set | 100 | 2.1% |
| float | 20 | 0.4% |
| tuple | 20 | 0.4% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 380 | 0.0% |
|          hit | 1,110,178 | 99.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 228,662,283 | 48.3% |
| Not specialized | 79,243,401 | 16.7% |
| Specialized hits | 165,682,759 | 35.0% |
| Specialized misses | 13,420 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 10,994,384 | 35.2% |
| CALL | 8,836,718 | 28.3% |
| TO_BOOL | 7,513,061 | 24.1% |
| BINARY_OP | 2,167,413 | 6.9% |
| COMPARE_OP | 985,993 | 3.2% |
| SEND | 658,430 | 2.1% |
| STORE_ATTR | 13,540 | 0.0% |
| FOR_ITER | 9,180 | 0.0% |
| BINARY_SUBSCR | 8,460 | 0.0% |
| LOAD_GLOBAL | 7,160 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_SLOT | 6,260 | 46.6% |
| LOAD_ATTR_SLOT | 3,000 | 22.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,420 | 10.6% |
| CALL_METHOD_DESCRIPTOR_O | 540 | 4.0% |
| CALL_PY_EXACT_ARGS | 280 | 2.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 280 | 2.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 240 | 1.8% |
| LOAD_ATTR_MODULE | 240 | 1.8% |
| COMPARE_OP_INT | 160 | 1.2% |
| BINARY_SUBSCR_STR_INT | 140 | 1.0% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 2,345,328 | 10.2% |
| Calls to Python functions inlined | 20,581,092 | 89.8% |
| Calls via PyEval_EvalFrame (total) | 2,345,328 | 10.2% |
| Calls via PyEval_EvalFrame (vector) | 2,015,623 | 8.8% |
| Calls via PyEval_EvalFrame (generator) | 329,705 | 1.4% |
| Calls via PyEval_EvalFrame (legacy) | 40 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,015,483 | 8.8% |
| Calls via PyEval_EvalFrame (build class) | 100 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 360 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 440 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 1,920 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 659,810 | 2.9% |
| Frame objects created | 643,090 | 2.8% |
| Frames pushed | 20,959,090 | 91.4% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 14,685,445 | 41.2% |
| Frees to freelist | 14,693,428 |  |
| Allocations | 20,964,723 | 58.8% |
| Allocations to 512 bytes | 14,550,983 | 40.8% |
| Allocations to 4 kbytes | 323,115 | 0.9% |
| Allocations over 4 kbytes | 6,090,625 | 17.1% |
| Frees | 21,346,502 |  |
| New values | 1,680 |  |
| Interpreter increfs | 198,667,801 | 66.0% |
| Interpreter decrefs | 236,291,634 | 70.7% |
| Increfs | 102,163,211 | 34.0% |
| Decrefs | 98,007,469 | 29.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 160 | 9.5% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 20,460,741 |  |
| Method cache misses | 12,986 |  |
| Method cache collisions | 12,776 |  |
| Method cache dunder hits | 1,046,220 |  |
| Method cache dunder misses | 1,636 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,980 | 140,880 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 860 |  |
| Traces created | 860 | 100.0% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 0 | 0.0% |
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
| <= 16 | 0 | 0.0% |
| <= 32 | 340 | 39.5% |
| <= 64 | 20 | 2.3% |
| <= 128 | 480 | 55.8% |
| <= 256 | 20 | 2.3% |


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
| <= 16 | 20 | 2.3% |
| <= 32 | 40 | 4.7% |
| <= 64 | 60 | 7.0% |
| <= 128 | 0 | 0.0% |
| <= 256 | 20 | 2.3% |


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
| STORE_ATTR_WITH_HINT | 40 |
| RETURN_GENERATOR | 20 |
| CALL | 20 |
| CALL_FUNCTION_EX | 20 |
| CALL_LIST_APPEND | 20 |
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
