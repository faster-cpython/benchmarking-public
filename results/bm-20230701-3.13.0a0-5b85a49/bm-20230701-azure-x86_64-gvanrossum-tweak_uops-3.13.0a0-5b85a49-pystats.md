
# Pystats results

- fork: gvanrossum
- ref: tweak-uops
- commit hash: 5b85a49
- commit date: 2023-07-01T14:50:20-07:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 26,773,588,392 | 18.9% | 18.9% |  |
| STORE_FAST | 9,467,552,845 | 6.7% | 25.6% |  |
| LOAD_CONST | 8,846,774,167 | 6.2% | 31.8% |  |
| POP_JUMP_IF_FALSE | 8,188,882,497 | 5.8% | 37.6% |  |
| LOAD_FAST_LOAD_FAST | 7,065,688,542 | 5.0% | 42.6% |  |
| RESUME | 4,849,902,335 | 3.4% | 46.0% |  |
| LOAD_GLOBAL_BUILTIN | 4,039,594,963 | 2.9% | 48.9% | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 3,586,519,810 | 2.5% | 51.4% | 5.8% |
| TO_BOOL_BOOL | 3,116,101,453 | 2.2% | 53.6% | 0.0% |
| RETURN_VALUE | 2,911,874,017 | 2.1% | 55.6% |  |
| CALL_PY_EXACT_ARGS | 2,754,932,192 | 1.9% | 57.6% | 3.1% |
| LOAD_GLOBAL_MODULE | 2,749,626,405 | 1.9% | 59.5% | 0.0% |
| BINARY_SUBSCR | 2,343,158,742 | 1.7% | 61.2% |  |
| POP_TOP | 2,275,697,040 | 1.6% | 62.8% |  |
| JUMP_BACKWARD | 2,029,235,712 | 1.4% | 64.2% |  |
| BINARY_OP_ADD_INT | 2,018,966,554 | 1.4% | 65.6% | 0.0% |
| CONTAINS_OP | 1,939,859,687 | 1.4% | 67.0% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,772,622,097 | 1.3% | 68.3% | 8.7% |
| COMPARE_OP_STR | 1,585,966,904 | 1.1% | 69.4% | 0.0% |
| STORE_FAST_STORE_FAST | 1,528,120,226 | 1.1% | 70.5% |  |
| POP_JUMP_IF_TRUE | 1,441,310,515 | 1.0% | 71.5% |  |
| COMPARE_OP_INT | 1,348,817,373 | 1.0% | 72.4% | 0.1% |
| LOAD_ATTR_SLOT | 1,317,787,943 | 0.9% | 73.4% | 4.3% |
| RETURN_CONST | 1,305,161,276 | 0.9% | 74.3% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,304,110,690 | 0.9% | 75.2% | 3.5% |
| FOR_ITER_LIST | 1,234,352,052 | 0.9% | 76.1% | 5.3% |
| LOAD_ATTR | 1,199,318,604 | 0.8% | 76.9% |  |
| INTERPRETER_EXIT | 1,190,650,235 | 0.8% | 77.8% |  |
| ENTER_EXECUTOR | 1,160,430,355 | 0.8% | 78.6% |  |
| STORE_ATTR_SLOT | 1,050,920,608 | 0.7% | 79.3% | 10.6% |
| COPY | 1,029,730,990 | 0.7% | 80.0% |  |
| CALL_NO_KW_BUILTIN_FAST | 927,714,346 | 0.7% | 80.7% | 0.0% |
| SWAP | 904,041,014 | 0.6% | 81.3% |  |
| BINARY_SUBSCR_LIST_INT | 876,727,526 | 0.6% | 82.0% | 0.4% |
| CALL | 872,063,832 | 0.6% | 82.6% |  |
| BINARY_OP_MULTIPLY_FLOAT | 827,599,659 | 0.6% | 83.2% | 0.8% |
| BINARY_OP | 826,488,859 | 0.6% | 83.7% |  |
| LOAD_DEREF | 806,499,923 | 0.6% | 84.3% |  |
| STORE_ATTR_INSTANCE_VALUE | 786,446,744 | 0.6% | 84.9% | 8.8% |
| CALL_NO_KW_BUILTIN_O | 781,853,229 | 0.6% | 85.4% | 0.1% |
| CALL_NO_KW_ISINSTANCE | 777,536,660 | 0.5% | 86.0% |  |
| NOP | 750,752,366 | 0.5% | 86.5% |  |
| PUSH_NULL | 703,011,850 | 0.5% | 87.0% |  |
| YIELD_VALUE | 692,026,232 | 0.5% | 87.5% |  |
| BUILD_TUPLE | 666,260,710 | 0.5% | 88.0% |  |
| BINARY_SUBSCR_DICT | 613,454,932 | 0.4% | 88.4% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 598,590,546 | 0.4% | 88.8% |  |
| GET_ITER | 580,095,400 | 0.4% | 89.2% |  |
| FOR_ITER_RANGE | 476,859,265 | 0.3% | 89.6% | 0.0% |
| BINARY_OP_SUBTRACT_INT | 446,728,049 | 0.3% | 89.9% | 0.1% |
| IS_OP | 434,486,114 | 0.3% | 90.2% |  |
| UNPACK_SEQUENCE_TUPLE | 419,523,020 | 0.3% | 90.5% | 0.3% |
| FOR_ITER_TUPLE | 416,508,457 | 0.3% | 90.8% | 15.7% |
| JUMP_FORWARD | 408,339,619 | 0.3% | 91.1% |  |
| POP_JUMP_IF_NOT_NONE | 407,475,977 | 0.3% | 91.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 392,351,677 | 0.3% | 91.6% | 1.7% |
| BINARY_OP_ADD_FLOAT | 390,156,895 | 0.3% | 91.9% | 1.6% |
| TO_BOOL_NONE | 372,888,055 | 0.3% | 92.2% | 11.0% |
| LOAD_ATTR_WITH_HINT | 337,924,843 | 0.2% | 92.4% | 2.6% |
| CALL_NO_KW_TYPE_1 | 327,453,244 | 0.2% | 92.6% |  |
| LOAD_ATTR_MODULE | 325,472,634 | 0.2% | 92.9% | 0.0% |
| CALL_NO_KW_LEN | 318,592,081 | 0.2% | 93.1% |  |
| STORE_SUBSCR | 315,796,936 | 0.2% | 93.3% |  |
| SEND_GEN | 301,848,030 | 0.2% | 93.5% |  |
| STORE_SUBSCR_LIST_INT | 296,811,420 | 0.2% | 93.7% | 0.0% |
| BUILD_LIST | 291,319,352 | 0.2% | 93.9% |  |
| EXTENDED_ARG | 288,289,080 | 0.2% | 94.1% |  |
| POP_JUMP_IF_NONE | 282,217,363 | 0.2% | 94.3% |  |
| FOR_ITER | 281,643,230 | 0.2% | 94.5% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,668,759 | 0.2% | 94.7% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 265,822,858 | 0.2% | 94.9% | 3.2% |
| COPY_FREE_VARS | 245,617,478 | 0.2% | 95.1% |  |
| BINARY_SLICE | 243,544,320 | 0.2% | 95.3% |  |
| RETURN_GENERATOR | 238,120,116 | 0.2% | 95.4% |  |
| CALL_NO_KW_LIST_APPEND | 238,088,654 | 0.2% | 95.6% | 0.0% |
| TO_BOOL_INT | 226,250,701 | 0.2% | 95.8% | 0.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 225,113,836 | 0.2% | 95.9% | 7.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 214,264,032 | 0.2% | 96.1% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 211,147,608 | 0.1% | 96.2% | 0.0% |
| TO_BOOL | 198,269,392 | 0.1% | 96.4% |  |
| END_SEND | 193,874,714 | 0.1% | 96.5% |  |
| STORE_SUBSCR_DICT | 192,453,436 | 0.1% | 96.6% |  |
| BINARY_SUBSCR_TUPLE_INT | 184,222,740 | 0.1% | 96.8% |  |
| TO_BOOL_ALWAYS_TRUE | 178,257,328 | 0.1% | 96.9% | 21.4% |
| KW_NAMES | 168,475,196 | 0.1% | 97.0% |  |
| CALL_PY_WITH_DEFAULTS | 150,390,219 | 0.1% | 97.1% | 3.5% |
| CALL_INTRINSIC_1 | 147,718,669 | 0.1% | 97.2% |  |
| BINARY_SUBSCR_GETITEM | 146,525,156 | 0.1% | 97.3% | 0.0% |
| LIST_APPEND | 146,047,572 | 0.1% | 97.4% |  |
| UNPACK_SEQUENCE_LIST | 140,233,120 | 0.1% | 97.5% | 0.9% |
| CALL_BOUND_METHOD_EXACT_ARGS | 138,021,933 | 0.1% | 97.6% | 19.2% |
| COMPARE_OP | 134,903,357 | 0.1% | 97.7% |  |
| STORE_FAST_LOAD_FAST | 132,461,040 | 0.1% | 97.8% |  |
| DELETE_SUBSCR | 126,942,352 | 0.1% | 97.9% |  |
| UNARY_NEGATIVE | 121,209,060 | 0.1% | 98.0% |  |
| LOAD_ATTR_CLASS | 120,571,952 | 0.1% | 98.1% | 1.1% |
| CALL_BUILTIN_CLASS | 119,108,225 | 0.1% | 98.1% |  |
| STORE_SLICE | 117,634,500 | 0.1% | 98.2% |  |
| FORMAT_SIMPLE | 116,924,280 | 0.1% | 98.3% |  |
| LOAD_SUPER_ATTR_METHOD | 113,251,420 | 0.1% | 98.4% |  |
| SEND | 112,328,356 | 0.1% | 98.5% |  |
| TO_BOOL_LIST | 110,500,025 | 0.1% | 98.5% | 1.2% |
| COMPARE_OP_FLOAT | 109,606,602 | 0.1% | 98.6% | 0.0% |
| CONVERT_VALUE | 103,728,540 | 0.1% | 98.7% |  |
| MAKE_FUNCTION | 93,651,649 | 0.1% | 98.8% |  |
| FOR_ITER_GEN | 89,875,020 | 0.1% | 98.8% | 0.0% |
| GET_AWAITABLE | 84,577,934 | 0.1% | 98.9% |  |
| MAKE_CELL | 83,113,073 | 0.1% | 98.9% |  |
| SET_FUNCTION_ATTRIBUTE | 82,577,160 | 0.1% | 99.0% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 76,762,213 | 0.1% | 99.1% | 0.0% |
| CALL_FUNCTION_EX | 73,784,063 | 0.1% | 99.1% |  |
| BUILD_SLICE | 71,536,078 | 0.1% | 99.2% |  |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 68,236,510 | 0.0% | 99.2% | 2.5% |
| BINARY_OP_ADD_UNICODE | 67,841,080 | 0.0% | 99.3% |  |
| TO_BOOL_STR | 66,622,260 | 0.0% | 99.3% | 3.0% |
| EXIT_INIT_CHECK | 66,525,890 | 0.0% | 99.4% |  |
| STORE_DEREF | 65,096,460 | 0.0% | 99.4% |  |
| BUILD_STRING | 58,692,180 | 0.0% | 99.4% |  |
| END_FOR | 56,697,480 | 0.0% | 99.5% |  |
| STORE_ATTR_WITH_HINT | 52,984,267 | 0.0% | 99.5% | 5.9% |
| STORE_ATTR | 52,784,517 | 0.0% | 99.6% |  |
| BUILD_MAP | 51,799,317 | 0.0% | 99.6% |  |
| UNARY_NOT | 50,907,066 | 0.0% | 99.6% |  |
| LOAD_FAST_AND_CLEAR | 50,374,776 | 0.0% | 99.7% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 48,913,260 | 0.0% | 99.7% | 0.0% |
| LIST_EXTEND | 47,765,093 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 46,158,360 | 0.0% | 99.8% | 11.9% |
| MAP_ADD | 40,747,620 | 0.0% | 99.8% |  |
| CALL_NO_KW_STR_1 | 37,417,360 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 22,732,238 | 0.0% | 99.8% | 7.7% |
| CALL_NO_KW_TUPLE_1 | 21,686,400 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 17,134,956 | 0.0% | 99.9% |  |
| POP_EXCEPT | 17,134,956 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,767,288 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,169,260 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 11,900,667 | 0.0% | 99.9% |  |
| DICT_MERGE | 9,344,080 | 0.0% | 99.9% |  |
| RERAISE | 8,742,900 | 0.0% | 99.9% |  |
| DELETE_ATTR | 8,512,431 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,360,898 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 6,997,063 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_ANEXT | 6,000,000 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,921,860 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 3,745,380 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,411,180 | 0.0% | 100.0% |  |
| BEFORE_WITH | 3,343,556 | 0.0% | 100.0% |  |
| SET_ADD | 3,100,800 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,270,340 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,848,240 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,530,300 | 0.0% | 100.0% |  |
| BUILD_SET | 1,466,520 | 0.0% | 100.0% |  |
| DELETE_FAST | 370,744 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 207,020 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,993 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,433 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 4,353 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 4,080 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| FORMAT_WITH_SPEC | 2,160 | 0.0% | 100.0% |  |
| LOAD_NAME | 1,560 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,180 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NONE | 540 | 0.0% | 100.0% |  |
| SET_UPDATE | 360 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_FORWARD | 300 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_NOT_NONE | 240 | 0.0% | 100.0% |  |
| CLEANUP_THROW | 240 | 0.0% | 100.0% |  |
| BEFORE_ASYNC_WITH | 120 | 0.0% | 100.0% |  |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_CONST | 4,687,692,170 | 3.3% | 3.3% |
| STORE_FAST LOAD_FAST | 4,324,800,908 | 3.1% | 6.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 4,307,796,892 | 3.0% | 9.4% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 3,056,588,906 | 2.2% | 11.6% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,619,496,287 | 1.8% | 13.4% |
| CALL_PY_EXACT_ARGS RESUME | 2,453,160,352 | 1.7% | 15.1% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 2,270,348,892 | 1.6% | 16.7% |
| RESUME LOAD_FAST | 2,016,471,804 | 1.4% | 18.2% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,829,240,147 | 1.3% | 19.5% |
| LOAD_CONST BINARY_OP_ADD_INT | 1,584,754,444 | 1.1% | 20.6% |
| LOAD_CONST COMPARE_OP_STR | 1,560,608,652 | 1.1% | 21.7% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,546,009,912 | 1.1% | 22.8% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,524,391,712 | 1.1% | 23.8% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,203,704,771 | 0.8% | 24.7% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,179,864,179 | 0.8% | 25.5% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,141,318,453 | 0.8% | 26.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,127,873,807 | 0.8% | 27.1% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,089,588,005 | 0.8% | 27.9% |
| BINARY_OP_ADD_INT STORE_FAST | 1,079,413,438 | 0.8% | 28.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,037,017,334 | 0.7% | 29.4% |
| LOAD_CONST LOAD_FAST | 1,022,327,050 | 0.7% | 30.1% |
| LOAD_FAST_LOAD_FAST CONTAINS_OP | 989,041,200 | 0.7% | 30.8% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 971,097,482 | 0.7% | 31.5% |
| BINARY_SUBSCR STORE_FAST | 970,627,832 | 0.7% | 32.2% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 953,094,149 | 0.7% | 32.8% |
| ENTER_EXECUTOR BINARY_SUBSCR | 943,909,800 | 0.7% | 33.5% |
| JUMP_BACKWARD FOR_ITER_LIST | 921,159,950 | 0.7% | 34.2% |
| LOAD_FAST LOAD_FAST | 921,109,793 | 0.7% | 34.8% |
| BINARY_SUBSCR LOAD_FAST | 878,904,840 | 0.6% | 35.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 856,297,241 | 0.6% | 36.0% |
| RESUME LOAD_GLOBAL_BUILTIN | 824,656,304 | 0.6% | 36.6% |
| STORE_FAST_STORE_FAST STORE_FAST_STORE_FAST | 815,096,820 | 0.6% | 37.2% |
| POP_TOP LOAD_FAST | 800,184,094 | 0.6% | 37.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 778,134,348 | 0.5% | 38.3% |
| CALL_NO_KW_ISINSTANCE TO_BOOL_BOOL | 764,715,980 | 0.5% | 38.9% |
| LOAD_FAST RETURN_VALUE | 753,396,965 | 0.5% | 39.4% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 752,047,023 | 0.5% | 39.9% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 717,785,782 | 0.5% | 40.4% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 716,741,091 | 0.5% | 40.9% |
| LOAD_FAST TO_BOOL_BOOL | 713,319,982 | 0.5% | 41.4% |
| STORE_FAST STORE_FAST | 709,867,112 | 0.5% | 41.9% |
| LOAD_FAST LOAD_ATTR | 707,317,847 | 0.5% | 42.4% |
| STORE_FAST ENTER_EXECUTOR | 697,846,320 | 0.5% | 42.9% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 656,173,958 | 0.5% | 43.4% |
| LOAD_CONST LOAD_CONST | 646,942,679 | 0.5% | 43.8% |
| LOAD_FAST_LOAD_FAST CALL_PY_EXACT_ARGS | 637,338,206 | 0.4% | 44.3% |
| RETURN_VALUE STORE_FAST | 599,386,526 | 0.4% | 44.7% |
| FOR_ITER_LIST STORE_FAST | 584,783,292 | 0.4% | 45.1% |
| LOAD_FAST_LOAD_FAST BINARY_SUBSCR | 579,189,500 | 0.4% | 45.5% |
| LOAD_CONST COMPARE_OP_INT | 572,768,616 | 0.4% | 45.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 567,730,559 | 0.4% | 46.3% |
| POP_TOP JUMP_BACKWARD | 554,035,080 | 0.4% | 46.7% |
| RETURN_CONST POP_TOP | 542,382,076 | 0.4% | 47.1% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 539,003,320 | 0.4% | 47.5% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 536,880,567 | 0.4% | 47.9% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 532,562,509 | 0.4% | 48.2% |
| LOAD_DEREF LOAD_FAST | 528,737,408 | 0.4% | 48.6% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 516,898,216 | 0.4% | 49.0% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 510,409,828 | 0.4% | 49.3% |
| RETURN_VALUE RETURN_VALUE | 503,222,056 | 0.4% | 49.7% |
| LOAD_FAST STORE_ATTR_SLOT | 497,588,162 | 0.4% | 50.1% |
| CALL_NO_KW_BUILTIN_FAST TO_BOOL_BOOL | 477,106,524 | 0.3% | 50.4% |
| LOAD_FAST CONTAINS_OP | 473,792,400 | 0.3% | 50.7% |
| RESUME POP_TOP | 471,385,040 | 0.3% | 51.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST_LOAD_FAST | 463,313,665 | 0.3% | 51.4% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 458,282,166 | 0.3% | 51.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 456,170,446 | 0.3% | 52.0% |
| YIELD_VALUE INTERPRETER_EXIT | 450,585,378 | 0.3% | 52.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 447,135,068 | 0.3% | 52.7% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 0.3% | 53.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 432,057,045 | 0.3% | 53.3% |
| JUMP_BACKWARD FOR_ITER_RANGE | 424,856,883 | 0.3% | 53.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 414,985,668 | 0.3% | 53.9% |
| STORE_FAST LOAD_GLOBAL_MODULE | 412,392,754 | 0.3% | 54.2% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 406,147,210 | 0.3% | 54.4% |
| RETURN_CONST INTERPRETER_EXIT | 405,582,295 | 0.3% | 54.7% |
| BUILD_TUPLE RETURN_VALUE | 405,100,080 | 0.3% | 55.0% |
| PUSH_NULL LOAD_FAST | 402,018,182 | 0.3% | 55.3% |
| LOAD_CONST STORE_FAST | 399,041,409 | 0.3% | 55.6% |
| FOR_ITER_RANGE STORE_FAST | 393,440,651 | 0.3% | 55.9% |
| IS_OP POP_JUMP_IF_FALSE | 367,786,690 | 0.3% | 56.1% |
| LOAD_FAST_LOAD_FAST LOAD_CONST | 366,372,654 | 0.3% | 56.4% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 361,776,446 | 0.3% | 56.6% |
| LOAD_FAST BINARY_SUBSCR | 357,175,920 | 0.3% | 56.9% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 348,205,919 | 0.2% | 57.1% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 341,708,547 | 0.2% | 57.4% |
| LOAD_CONST BINARY_OP_SUBTRACT_INT | 339,770,629 | 0.2% | 57.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 336,329,061 | 0.2% | 57.9% |
| RESUME NOP | 334,028,603 | 0.2% | 58.1% |
| STORE_FAST LOAD_DEREF | 333,048,090 | 0.2% | 58.3% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 330,235,073 | 0.2% | 58.6% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 323,818,064 | 0.2% | 58.8% |
| RESUME LOAD_GLOBAL_MODULE | 322,916,532 | 0.2% | 59.0% |
| LOAD_CONST CALL_NO_KW_BUILTIN_FAST | 322,397,344 | 0.2% | 59.2% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 320,473,487 | 0.2% | 59.5% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 319,800,833 | 0.2% | 59.7% |
| RETURN_VALUE INTERPRETER_EXIT | 316,392,982 | 0.2% | 59.9% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 314,191,784 | 0.2% | 60.1% |
| CALL_NO_KW_BUILTIN_FAST STORE_FAST | 310,241,980 | 0.2% | 60.4% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 310,072,188 | 0.2% | 60.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 120 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 2,233,505 | 66.8% |
| LOAD_ATTR_INSTANCE_VALUE | 972,954 | 29.1% |
| LOAD_GLOBAL_MODULE | 68,757 | 2.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,600 | 1.1% |
| CALL | 31,740 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,911,771 | 87.1% |
| STORE_FAST | 430,345 | 12.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 220,297,376 | 26.7% |
| LOAD_FAST | 185,088,339 | 22.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.7% |
| LOAD_FAST_LOAD_FAST | 47,289,340 | 5.7% |
| LOAD_ATTR_INSTANCE_VALUE | 44,171,820 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 163,406,217 | 19.8% |
| LOAD_FAST | 136,763,020 | 16.5% |
| LOAD_FAST_LOAD_FAST | 106,675,148 | 12.9% |
| RETURN_VALUE | 69,475,980 | 8.4% |
| LOAD_CONST | 68,118,840 | 8.2% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,043,300 | 72.8% |
| LOAD_FAST | 65,046,933 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 115,760,495 | 29.7% |
| LOAD_FAST | 59,481,900 | 15.2% |
| RETURN_VALUE | 31,350,960 | 8.0% |
| LOAD_FAST_LOAD_FAST | 29,369,460 | 7.5% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,584,754,444 | 78.5% |
| LOAD_FAST | 234,196,084 | 11.6% |
| LOAD_FAST_LOAD_FAST | 94,377,180 | 4.7% |
| END_SEND | 29,134,080 | 1.4% |
| BINARY_OP_MULTIPLY_INT | 23,999,760 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,079,413,438 | 53.5% |
| LOAD_CONST | 131,530,200 | 6.5% |
| STORE_SLICE | 103,909,260 | 5.1% |
| BINARY_OP_MULTIPLY_INT | 96,055,140 | 4.8% |
| BINARY_SUBSCR | 89,539,800 | 4.4% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,034,040 | 47.2% |
| BINARY_SLICE | 15,579,000 | 23.0% |
| LOAD_CONST | 13,011,440 | 19.2% |
| LOAD_ATTR | 2,105,320 | 3.1% |
| BUILD_STRING | 2,011,200 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,139,040 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 23.5% |
| BUILD_TUPLE | 15,457,800 | 22.8% |
| LOAD_CONST | 8,422,860 | 12.4% |
| RETURN_VALUE | 3,047,100 | 4.5% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,590,560 | 43.7% |
| BINARY_SLICE | 1,580,580 | 26.7% |
| RETURN_VALUE | 680,220 | 11.5% |
| BINARY_OP_ADD_UNICODE | 364,960 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,731,820 | 63.0% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,420 | 8.6% |
| LOAD_CONST | 60,360 | 1.0% |
| LOAD_FAST_LOAD_FAST | 23,580 | 0.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 539,003,320 | 65.1% |
| LOAD_ATTR_INSTANCE_VALUE | 118,763,280 | 14.4% |
| BINARY_SUBSCR | 67,701,000 | 8.2% |
| LOAD_FAST_LOAD_FAST | 59,227,020 | 7.2% |
| CALL_BUILTIN_CLASS | 12,782,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 284,043,300 | 34.3% |
| YIELD_VALUE | 210,931,680 | 25.5% |
| LOAD_FAST | 111,266,580 | 13.4% |
| BINARY_OP_SUBTRACT_FLOAT | 109,285,680 | 13.2% |
| STORE_FAST | 36,069,060 | 4.4% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 96,055,140 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,998 | 19.3% |
| LOAD_FAST_LOAD_FAST | 44,782,000 | 16.8% |
| LOAD_FAST | 38,770,580 | 14.6% |
| BINARY_OP | 27,332,740 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 62,109,720 | 23.4% |
| LOAD_CONST | 61,631,700 | 23.2% |
| LOAD_FAST | 47,053,140 | 17.7% |
| LOAD_FAST_LOAD_FAST | 28,244,880 | 10.6% |
| BINARY_OP_ADD_INT | 23,999,760 | 9.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.5% |
| LOAD_FAST | 69,478,900 | 25.8% |
| LOAD_FAST_LOAD_FAST | 36,089,040 | 13.4% |
| LOAD_ATTR_INSTANCE_VALUE | 28,661,940 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 96,305,560 | 35.7% |
| LOAD_FAST_LOAD_FAST | 73,322,880 | 27.2% |
| SWAP | 55,701,000 | 20.7% |
| LOAD_FAST | 28,349,160 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 339,770,629 | 76.1% |
| LOAD_FAST | 66,874,540 | 15.0% |
| LOAD_FAST_LOAD_FAST | 26,967,200 | 6.0% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.2% |
| CALL_NO_KW_LEN | 2,724,360 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,675,400 | 21.0% |
| SWAP | 67,852,757 | 15.2% |
| STORE_FAST | 67,388,592 | 15.1% |
| RETURN_VALUE | 39,931,800 | 8.9% |
| BINARY_OP | 37,165,200 | 8.3% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 136,821,662 | 56.2% |
| LOAD_FAST_LOAD_FAST | 39,988,020 | 16.4% |
| BINARY_OP_ADD_INT | 35,908,560 | 14.7% |
| LOAD_FAST | 24,776,038 | 10.2% |
| LOAD_ATTR_SLOT | 2,747,460 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 53,132,688 | 21.8% |
| GET_ITER | 33,131,320 | 13.6% |
| CALL_PY_EXACT_ARGS | 25,417,320 | 10.4% |
| BUILD_TUPLE | 24,332,520 | 10.0% |
| LOAD_DEREF | 18,985,680 | 7.8% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 943,909,800 | 40.3% |
| LOAD_FAST_LOAD_FAST | 579,189,500 | 24.7% |
| LOAD_FAST | 357,175,920 | 15.2% |
| LOAD_CONST | 139,414,481 | 5.9% |
| COPY | 109,564,100 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 970,627,832 | 41.4% |
| LOAD_FAST | 878,904,840 | 37.5% |
| LOAD_FAST_LOAD_FAST | 110,147,520 | 4.7% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |
| BINARY_SUBSCR | 48,584,621 | 2.1% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 205,775,320 | 33.5% |
| LOAD_FAST | 202,286,396 | 33.0% |
| LOAD_FAST_LOAD_FAST | 131,706,060 | 21.5% |
| BINARY_SUBSCR | 41,253,420 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,361,760 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 231,744,576 | 37.8% |
| RETURN_VALUE | 104,365,328 | 17.0% |
| CONTAINS_OP | 77,768,700 | 12.7% |
| LOAD_FAST | 59,365,320 | 9.7% |
| LOAD_ATTR_METHOD_NO_DICT | 41,379,720 | 6.7% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 67,814,736 | 46.3% |
| LOAD_CONST | 41,616,840 | 28.4% |
| BUILD_TUPLE | 28,812,000 | 19.7% |
| LOAD_ATTR_INSTANCE_VALUE | 3,355,020 | 2.3% |
| LOAD_FAST | 3,077,040 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,815,016 | 99.5% |
| MAKE_CELL | 705,600 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,420 | 0.0% |
| CONTAINS_OP | 1,020 | 0.0% |
| LOAD_FAST | 300 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 272,981,600 | 31.1% |
| LOAD_CONST | 180,390,725 | 20.6% |
| COPY | 157,632,300 | 18.0% |
| LOAD_FAST_LOAD_FAST | 151,506,584 | 17.3% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 235,319,803 | 26.9% |
| LOAD_CONST | 189,851,160 | 21.7% |
| LOAD_FAST | 140,231,160 | 16.0% |
| RETURN_VALUE | 90,397,860 | 10.3% |
| BINARY_OP | 38,804,700 | 4.4% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 144,415,980 | 78.4% |
| LOAD_FAST | 39,803,100 | 21.6% |
| LOAD_FAST_LOAD_FAST | 3,360 | 0.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,660 | 39.1% |
| LOAD_CONST | 24,655,900 | 13.4% |
| LOAD_FAST | 24,038,880 | 13.0% |
| YIELD_VALUE | 19,353,600 | 10.5% |
| STORE_FAST | 8,162,440 | 4.4% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,745,380 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,930,620 | 51.5% |
| LOAD_FAST_LOAD_FAST | 1,704,180 | 45.5% |
| STORE_FAST | 55,200 | 1.5% |
| DICT_MERGE | 16,320 | 0.4% |
| LOAD_DEREF | 15,600 | 0.4% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 115,895,422 | 39.8% |
| LOAD_ATTR_SLOT | 37,318,629 | 12.8% |
| SWAP | 31,867,024 | 10.9% |
| LOAD_FAST | 24,960,653 | 8.6% |
| RESUME | 17,316,700 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 127,870,934 | 43.9% |
| LOAD_FAST | 83,092,854 | 28.5% |
| SWAP | 31,867,084 | 10.9% |
| CALL | 9,652,180 | 3.3% |
| RETURN_VALUE | 8,829,960 | 3.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,350,200 | 16.1% |
| RESUME | 6,500,717 | 12.5% |
| SWAP | 5,488,800 | 10.6% |
| LOAD_FAST | 5,419,920 | 10.5% |
| POP_JUMP_IF_FALSE | 3,888,600 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 20,270,652 | 39.1% |
| LOAD_FAST | 16,350,665 | 31.6% |
| SWAP | 5,488,800 | 10.6% |
| CALL_FUNCTION_EX | 3,354,540 | 6.5% |
| LOAD_CONST | 2,915,940 | 5.6% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| LOAD_CONST | 82,320 | 5.6% |
| LOAD_FAST | 52,920 | 3.6% |
| LOAD_GLOBAL_MODULE | 9,960 | 0.7% |
| LOAD_ATTR_MODULE | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| STORE_FAST | 48,240 | 3.3% |
| LOAD_GLOBAL_BUILTIN | 36,600 | 2.5% |
| CALL_PY_EXACT_ARGS | 34,080 | 2.3% |
| CONTAINS_OP | 9,600 | 0.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 70,736,520 | 98.9% |
| LOAD_FAST | 744,118 | 1.0% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.1% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 53,340,058 | 74.6% |
| BINARY_SUBSCR | 18,196,020 | 25.4% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 51,989,640 | 88.6% |
| LOAD_CONST | 6,702,540 | 11.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 62.5% |
| CALL | 12,295,080 | 20.9% |
| STORE_FAST | 4,596,420 | 7.8% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.4% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 198,246,257 | 29.8% |
| LOAD_CONST | 167,388,779 | 25.1% |
| LOAD_FAST_LOAD_FAST | 124,964,648 | 18.8% |
| CALL | 37,728,900 | 5.7% |
| LOAD_GLOBAL_BUILTIN | 28,322,860 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 405,100,080 | 60.8% |
| LOAD_CONST | 81,837,769 | 12.3% |
| CALL_NO_KW_ISINSTANCE | 33,206,480 | 5.0% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.3% |
| LIST_APPEND | 26,458,320 | 4.0% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 253,422,483 | 29.1% |
| KW_NAMES | 142,854,556 | 16.4% |
| LOAD_FAST_LOAD_FAST | 96,265,691 | 11.0% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,660 | 8.3% |
| LOAD_GLOBAL_MODULE | 46,254,951 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 307,404,351 | 35.3% |
| RESUME | 202,723,336 | 23.2% |
| RETURN_VALUE | 46,366,854 | 5.3% |
| POP_TOP | 43,021,289 | 4.9% |
| LOAD_GLOBAL_MODULE | 38,964,842 | 4.5% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,615,701 | 30.9% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 16.3% |
| LOAD_FAST_LOAD_FAST | 21,183,670 | 15.3% |
| LOAD_CONST | 13,518,460 | 9.8% |
| ENTER_EXECUTOR | 10,109,400 | 7.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 108,443,781 | 78.6% |
| COPY_FREE_VARS | 26,846,013 | 19.5% |
| POP_TOP | 2,060,300 | 1.5% |
| CALL_PY_EXACT_ARGS | 460,259 | 0.3% |
| MAKE_CELL | 171,620 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 32,818,951 | 27.6% |
| CALL_NO_KW_LEN | 23,152,652 | 19.4% |
| LOAD_GLOBAL_BUILTIN | 9,121,860 | 7.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,231,400 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 61,416,602 | 51.6% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.7% |
| STORE_FAST | 11,949,720 | 10.0% |
| LOAD_FAST | 9,360,240 | 7.9% |
| CALL_BUILTIN_CLASS | 4,075,192 | 3.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,040 | 43.0% |
| KW_NAMES | 24,569,440 | 32.0% |
| LOAD_FAST | 13,263,560 | 17.3% |
| LOAD_FAST_LOAD_FAST | 2,692,180 | 3.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,011,320 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 40.8% |
| STORE_FAST | 27,834,440 | 36.3% |
| POP_TOP | 11,159,671 | 14.5% |
| RETURN_VALUE | 5,460,282 | 7.1% |
| LOAD_CONST | 322,140 | 0.4% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 41,800,749 | 56.7% |
| LOAD_FAST | 9,715,374 | 13.2% |
| DICT_MERGE | 9,344,080 | 12.7% |
| LOAD_FAST_LOAD_FAST | 5,843,080 | 7.9% |
| BUILD_MAP | 3,354,540 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 44,952,349 | 60.9% |
| STORE_FAST | 8,094,120 | 11.0% |
| RETURN_VALUE | 6,016,034 | 8.2% |
| MAKE_CELL | 4,707,040 | 6.4% |
| LOAD_FAST_LOAD_FAST | 3,815,580 | 5.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 88,136,760 | 62.3% |
| LIST_EXTEND | 47,193,229 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 63.7% |
| CALL_FUNCTION_EX | 41,800,749 | 28.3% |
| RERAISE | 6,377,160 | 4.3% |
| LOAD_CONST | 3,370,680 | 2.3% |
| BUILD_MAP | 2,008,660 | 1.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,916,896 | 39.2% |
| LOAD_CONST | 8,583,920 | 37.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,063,100 | 17.9% |
| LOAD_FAST_LOAD_FAST | 740,622 | 3.3% |
| LOAD_ATTR | 258,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,051,582 | 31.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 30.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,435,680 | 10.7% |
| BINARY_OP | 2,010,960 | 8.8% |
| RETURN_VALUE | 1,418,500 | 6.2% |


</details>

### CALL_NO_KW_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_NO_KW_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 20,210,840 | 29.6% |
| LOAD_GLOBAL_MODULE | 9,317,725 | 13.7% |
| BINARY_OP_MULTIPLY_FLOAT | 8,978,540 | 13.2% |
| RETURN_CONST | 7,864,740 | 11.5% |
| BINARY_OP_ADD_FLOAT | 5,100,000 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 64,999,725 | 95.3% |
| LOAD_FAST | 1,660,840 | 2.4% |
| COPY_FREE_VARS | 1,525,925 | 2.2% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 32,220 | 0.0% |
| STORE_FAST | 13,960 | 0.0% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,160 | 46.8% |
| LOAD_CONST | 322,397,344 | 34.8% |
| LOAD_FAST_LOAD_FAST | 71,766,500 | 7.7% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| LOAD_FAST | 26,383,040 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 477,106,524 | 51.4% |
| STORE_FAST | 310,241,980 | 33.4% |
| POP_TOP | 47,605,244 | 5.1% |
| CALL_NO_KW_BUILTIN_FAST | 37,468,660 | 4.0% |
| RETURN_VALUE | 21,993,660 | 2.4% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 536,880,567 | 68.7% |
| LOAD_CONST | 55,890,060 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |
| LOAD_FAST_LOAD_FAST | 20,257,100 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 341,708,547 | 43.7% |
| LOAD_CONST | 171,752,679 | 22.0% |
| STORE_FAST | 163,891,484 | 21.0% |
| RETURN_VALUE | 29,118,972 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 330,235,073 | 42.5% |
| LOAD_GLOBAL_BUILTIN | 320,473,487 | 41.2% |
| LOAD_FAST_LOAD_FAST | 61,327,020 | 7.9% |
| BUILD_TUPLE | 33,206,480 | 4.3% |
| LOAD_ATTR_MODULE | 21,884,900 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 764,715,980 | 98.4% |
| COPY | 5,946,000 | 0.8% |
| RETURN_VALUE | 2,214,240 | 0.3% |
| POP_TOP | 1,996,800 | 0.3% |
| STORE_FAST | 1,489,620 | 0.2% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 200,273,268 | 62.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,414,571 | 13.3% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.3% |
| LOAD_DEREF | 20,446,300 | 6.4% |
| LOAD_ATTR_SLOT | 8,331,340 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 122,162,370 | 38.3% |
| LOAD_FAST | 43,783,920 | 13.7% |
| STORE_FAST | 37,901,425 | 11.9% |
| COMPARE_OP_INT | 32,501,580 | 10.2% |
| CALL_BUILTIN_CLASS | 23,152,652 | 7.3% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,096,282 | 73.1% |
| BINARY_SUBSCR | 20,171,040 | 8.5% |
| BINARY_SLICE | 18,506,220 | 7.8% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 4,894,440 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,679,034 | 37.7% |
| LOAD_FAST | 72,260,300 | 30.4% |
| EXTENDED_ARG | 27,821,580 | 11.7% |
| RETURN_CONST | 20,553,780 | 8.6% |
| LOAD_CONST | 11,303,760 | 4.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 176,202,980 | 44.9% |
| LOAD_CONST | 83,041,340 | 21.2% |
| LOAD_FAST_LOAD_FAST | 56,250,240 | 14.3% |
| LOAD_ATTR_METHOD_NO_DICT | 50,238,380 | 12.8% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 302,258,870 | 77.0% |
| LIST_APPEND | 28,850,040 | 7.4% |
| RETURN_VALUE | 11,993,412 | 3.1% |
| LOAD_FAST | 11,020,920 | 2.8% |
| POP_TOP | 8,572,415 | 2.2% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 143,899,269 | 63.9% |
| LOAD_ATTR | 71,923,118 | 31.9% |
| LOAD_ATTR_METHOD_LAZY_DICT | 7,410,790 | 3.3% |
| LOAD_FAST_LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 301,159 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 71,920,283 | 31.9% |
| TO_BOOL_BOOL | 59,436,018 | 26.4% |
| GET_ITER | 31,836,120 | 14.1% |
| LOAD_GLOBAL_MODULE | 18,632,220 | 8.3% |
| LOAD_FAST | 12,444,540 | 5.5% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 166,582,682 | 78.9% |
| CALL | 19,486,452 | 9.2% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.3% |
| LOAD_GLOBAL_MODULE | 5,276,340 | 2.5% |
| LOAD_ATTR | 3,038,880 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 101,254,308 | 48.0% |
| BINARY_OP | 72,002,140 | 34.1% |
| RETURN_VALUE | 17,284,260 | 8.2% |
| STORE_FAST | 6,937,860 | 3.3% |
| LOAD_FAST | 5,872,740 | 2.8% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 34,381,020 | 91.9% |
| RETURN_VALUE | 1,727,580 | 4.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,800 | 3.3% |
| BINARY_SUBSCR_TUPLE_INT | 30,420 | 0.1% |
| CALL | 25,600 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,520 | 33.9% |
| CALL_PY_EXACT_ARGS | 10,848,480 | 29.0% |
| STORE_FAST | 5,602,140 | 15.0% |
| RETURN_VALUE | 3,244,980 | 8.7% |
| BUILD_LIST | 1,966,480 | 5.3% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,490,280 | 66.8% |
| RETURN_GENERATOR | 5,394,160 | 24.9% |
| LOAD_ATTR_SLOT | 1,098,620 | 5.1% |
| CALL | 412,200 | 1.9% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,160 | 65.9% |
| BUILD_TUPLE | 2,891,780 | 13.3% |
| YIELD_VALUE | 2,419,200 | 11.2% |
| STORE_FAST | 617,040 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 571,920 | 2.6% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 323,818,064 | 98.9% |
| LOAD_CONST | 3,615,800 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,854,592 | 87.3% |
| LOAD_GLOBAL_MODULE | 13,598,440 | 4.2% |
| LOAD_GLOBAL_BUILTIN | 9,387,180 | 2.9% |
| LOAD_FAST | 7,472,280 | 2.3% |
| CALL_PY_EXACT_ARGS | 4,541,952 | 1.4% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 953,094,149 | 34.6% |
| LOAD_FAST_LOAD_FAST | 637,338,206 | 23.1% |
| LOAD_ATTR_METHOD_WITH_VALUES | 414,985,668 | 15.1% |
| LOAD_GLOBAL_MODULE | 159,065,658 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 109,897,529 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,453,160,352 | 89.0% |
| RETURN_GENERATOR | 140,280,976 | 5.1% |
| COPY_FREE_VARS | 120,097,647 | 4.4% |
| MAKE_CELL | 24,891,451 | 0.9% |
| INSTRUMENTED_RESUME | 14,577,900 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 87,614,504 | 58.3% |
| LOAD_ATTR_METHOD_NO_DICT | 12,061,720 | 8.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,617,811 | 7.7% |
| LOAD_ATTR | 11,184,040 | 7.4% |
| LOAD_SUPER_ATTR_METHOD | 5,951,040 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,345,564 | 96.6% |
| RETURN_GENERATOR | 3,297,720 | 2.2% |
| MAKE_CELL | 1,008,240 | 0.7% |
| COPY_FREE_VARS | 631,955 | 0.4% |
| CALL_PY_EXACT_ARGS | 87,580 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,683,624 | 93.5% |
| LOAD_GLOBAL_MODULE | 689,760 | 4.1% |
| BUILD_TUPLE | 356,280 | 2.1% |
| LOAD_ATTR_MODULE | 37,624 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,767,288 | 100.0% |


</details>

### CLEANUP_THROW

<details>
<summary> Successors and predecessors for CLEANUP_THROW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 240 | 100.0% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 43,089,876 | 31.9% |
| LOAD_FAST_LOAD_FAST | 32,019,060 | 23.7% |
| LOAD_ATTR | 15,173,616 | 11.2% |
| LOAD_ATTR_SLOT | 13,690,783 | 10.1% |
| LOAD_FAST | 10,752,440 | 8.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 69,229,906 | 51.3% |
| POP_JUMP_IF_TRUE | 38,838,510 | 28.8% |
| COPY | 18,630,266 | 13.8% |
| RETURN_VALUE | 7,089,365 | 5.3% |
| EXTENDED_ARG | 771,840 | 0.6% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 65,983,588 | 60.2% |
| BINARY_SUBSCR | 23,382,660 | 21.3% |
| LOAD_CONST | 6,004,560 | 5.5% |
| LOAD_FAST | 6,000,819 | 5.5% |
| LOAD_GLOBAL_MODULE | 3,631,855 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 47,983,768 | 43.8% |
| POP_JUMP_IF_TRUE | 32,445,300 | 29.6% |
| POP_JUMP_IF_FALSE | 29,177,174 | 26.6% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 572,768,616 | 42.5% |
| LOAD_ATTR_INSTANCE_VALUE | 171,609,721 | 12.7% |
| LOAD_FAST | 121,541,140 | 9.0% |
| LOAD_FAST_LOAD_FAST | 110,148,194 | 8.2% |
| COPY | 102,794,040 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,127,873,807 | 83.6% |
| POP_JUMP_IF_TRUE | 120,646,094 | 8.9% |
| RETURN_VALUE | 59,343,108 | 4.4% |
| LOAD_FAST | 15,024,000 | 1.1% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,567,100 | 1.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,560,608,652 | 98.4% |
| LOAD_FAST | 8,527,824 | 0.5% |
| LOAD_GLOBAL_MODULE | 4,654,352 | 0.3% |
| RETURN_VALUE | 4,023,840 | 0.3% |
| BINARY_SUBSCR_TUPLE_INT | 2,446,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,546,009,912 | 97.5% |
| POP_JUMP_IF_TRUE | 26,991,019 | 1.7% |
| COPY | 6,083,688 | 0.4% |
| RETURN_VALUE | 4,337,825 | 0.3% |
| EXTENDED_ARG | 1,172,820 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 989,041,200 | 51.0% |
| LOAD_FAST | 473,792,400 | 24.4% |
| LOAD_GLOBAL_MODULE | 301,342,680 | 15.5% |
| BINARY_SUBSCR_DICT | 77,768,700 | 4.0% |
| LOAD_ATTR_INSTANCE_VALUE | 41,839,527 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,829,240,147 | 94.3% |
| POP_JUMP_IF_TRUE | 59,676,000 | 3.1% |
| RETURN_VALUE | 25,006,260 | 1.3% |
| COPY | 20,881,380 | 1.1% |
| EXTENDED_ARG | 3,501,720 | 0.2% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 50,367,300 | 48.6% |
| LOAD_FAST_LOAD_FAST | 36,024,720 | 34.7% |
| LOAD_ATTR | 11,580,660 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 2,010,960 | 1.9% |
| RETURN_VALUE | 1,416,480 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 103,728,540 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,775,200 | 26.0% |
| LOAD_FAST | 226,442,154 | 22.0% |
| LOAD_FAST_LOAD_FAST | 120,895,740 | 11.7% |
| SWAP | 105,748,980 | 10.3% |
| LOAD_CONST | 95,063,460 | 9.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 267,775,200 | 26.0% |
| TO_BOOL_BOOL | 213,936,442 | 20.8% |
| BINARY_SUBSCR_LIST_INT | 157,632,300 | 15.3% |
| BINARY_SUBSCR | 109,564,100 | 10.6% |
| COMPARE_OP_INT | 102,794,040 | 10.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 120,097,647 | 76.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,846,013 | 17.0% |
| CALL | 8,744,576 | 5.5% |
| CALL_NO_KW_ALLOC_AND_ENTER_INIT | 1,525,925 | 1.0% |
| CALL_PY_WITH_DEFAULTS | 631,955 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 172,200,818 | 70.1% |
| RETURN_GENERATOR | 73,398,180 | 29.9% |
| MAKE_CELL | 18,480 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,512,431 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,648,634 | 78.1% |
| NOP | 1,713,800 | 20.1% |
| RETURN_CONST | 149,517 | 1.8% |
| LOAD_GLOBAL_MODULE | 480 | 0.0% |


</details>

### DELETE_DEREF

<details>
<summary> Successors and predecessors for DELETE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR | 1,200 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_FAST | 1,200 | 100.0% |


</details>

### DELETE_FAST

<details>
<summary> Successors and predecessors for DELETE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 222,720 | 60.1% |
| CALL | 81,000 | 21.8% |
| POP_EXCEPT | 18,000 | 4.9% |
| STORE_ATTR_INSTANCE_VALUE | 18,000 | 4.9% |
| NOP | 18,000 | 4.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 151,020 | 40.7% |
| RETURN_VALUE | 138,600 | 37.4% |
| RETURN_CONST | 36,000 | 9.7% |
| LOAD_FAST | 20,824 | 5.6% |
| LOAD_CONST | 9,060 | 2.4% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 72,994,140 | 57.5% |
| BUILD_SLICE | 53,340,058 | 42.0% |
| LOAD_FAST | 292,857 | 0.2% |
| LOAD_CONST | 286,740 | 0.2% |
| CALL | 19,917 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,231,458 | 84.5% |
| LOAD_CONST | 18,101,097 | 14.3% |
| JUMP_BACKWARD | 1,038,960 | 0.8% |
| RETURN_CONST | 347,037 | 0.3% |
| LOAD_FAST_LOAD_FAST | 208,140 | 0.2% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,025,020 | 96.6% |
| LOAD_ATTR_INSTANCE_VALUE | 150,600 | 1.6% |
| LOAD_DEREF | 75,760 | 0.8% |
| RETURN_VALUE | 50,880 | 0.5% |
| BUILD_CONST_KEY_MAP | 16,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,344,080 | 100.0% |


</details>

### DICT_UPDATE

<details>
<summary> Successors and predecessors for DICT_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 13,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DICT_MERGE | 13,140 | 100.0% |


</details>

### END_ASYNC_FOR

<details>
<summary> Successors and predecessors for END_ASYNC_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 6,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 5,999,940 | 100.0% |
| RETURN_CONST | 60 | 0.0% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 56,697,480 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 36,792,300 | 64.9% |
| LOAD_FAST | 19,100,640 | 33.7% |
| RETURN_CONST | 789,480 | 1.4% |
| LOAD_CONST | 5,280 | 0.0% |
| NOP | 4,740 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,299,238 | 51.7% |
| RETURN_VALUE | 68,993,658 | 35.6% |
| RETURN_CONST | 24,581,818 | 12.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 94,834,198 | 48.9% |
| POP_TOP | 36,145,256 | 18.6% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| LOAD_FAST | 3,215,880 | 1.7% |


</details>

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 697,846,320 | 60.1% |
| POP_JUMP_IF_FALSE | 301,735,034 | 26.0% |
| POP_TOP | 98,142,309 | 8.5% |
| EXTENDED_ARG | 28,322,380 | 2.4% |
| JUMP_FORWARD | 21,772,740 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 943,909,800 | 81.3% |
| SEND | 94,136,760 | 8.1% |
| POP_JUMP_IF_FALSE | 71,265,340 | 6.1% |
| CALL_NO_KW_BUILTIN_FAST | 15,732,600 | 1.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 10,109,400 | 0.9% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 66,525,890 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 66,525,890 | 100.0% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 81,547,640 | 28.3% |
| LOAD_FAST | 42,587,000 | 14.8% |
| JUMP_BACKWARD | 40,664,220 | 14.1% |
| CALL_NO_KW_LIST_APPEND | 27,821,580 | 9.7% |
| IS_OP | 18,001,680 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 123,737,320 | 42.9% |
| FOR_ITER_LIST | 38,689,360 | 13.4% |
| POP_JUMP_IF_NONE | 36,518,860 | 12.7% |
| ENTER_EXECUTOR | 28,322,380 | 9.8% |
| JUMP_BACKWARD | 25,663,640 | 8.9% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 103,728,540 | 88.7% |
| LOAD_FAST | 9,630,300 | 8.2% |
| LOAD_ATTR | 1,428,300 | 1.2% |
| RETURN_VALUE | 1,042,680 | 0.9% |
| LOAD_ATTR_SLOT | 860,640 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 59,084,040 | 50.5% |
| BUILD_STRING | 51,989,640 | 44.5% |
| LOAD_FAST | 5,841,780 | 5.0% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FORMAT_WITH_SPEC

<details>
<summary> Successors and predecessors for FORMAT_WITH_SPEC </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,920 | 88.9% |
| LOAD_CONST | 240 | 11.1% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 206,628,256 | 73.4% |
| GET_ITER | 49,587,317 | 17.6% |
| EXTENDED_ARG | 16,516,640 | 5.9% |
| SWAP | 5,812,020 | 2.1% |
| LOAD_FAST | 3,009,020 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 147,896,520 | 52.5% |
| STORE_FAST | 74,841,105 | 26.6% |
| LOAD_FAST | 17,495,918 | 6.2% |
| RETURN_CONST | 14,191,369 | 5.0% |
| PUSH_NULL | 7,954,800 | 2.8% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 56,710,020 | 63.1% |
| JUMP_BACKWARD | 32,801,160 | 36.5% |
| EXTENDED_ARG | 321,360 | 0.4% |
| LOAD_FAST | 42,120 | 0.0% |
| SWAP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 56,760,720 | 63.2% |
| RESUME | 33,114,060 | 36.8% |
| STORE_FAST | 120 | 0.0% |
| RETURN_CONST | 120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 921,159,950 | 74.6% |
| GET_ITER | 188,416,262 | 15.3% |
| LOAD_FAST | 59,095,840 | 4.8% |
| EXTENDED_ARG | 38,689,360 | 3.1% |
| SWAP | 25,705,944 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 584,783,292 | 47.4% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,191,784 | 25.5% |
| RETURN_CONST | 103,261,114 | 8.4% |
| STORE_FAST_LOAD_FAST | 80,255,100 | 6.5% |
| LOAD_FAST | 57,793,515 | 4.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 424,856,883 | 89.1% |
| GET_ITER | 25,379,102 | 5.3% |
| LOAD_FAST | 21,531,120 | 4.5% |
| SWAP | 4,261,260 | 0.9% |
| EXTENDED_ARG | 829,860 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 393,440,651 | 82.5% |
| STORE_FAST_LOAD_FAST | 35,405,280 | 7.4% |
| RETURN_CONST | 23,855,520 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 5,210,012 | 1.1% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 290,423,043 | 69.7% |
| GET_ITER | 120,729,855 | 29.0% |
| SWAP | 2,896,540 | 0.7% |
| FOR_ITER_LIST | 1,236,446 | 0.3% |
| LOAD_FAST | 1,120,800 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 285,544,508 | 68.6% |
| LOAD_FAST | 61,319,819 | 14.7% |
| LOAD_FAST_LOAD_FAST | 43,820,520 | 10.5% |
| RETURN_CONST | 12,222,000 | 2.9% |
| STORE_FAST_LOAD_FAST | 5,055,840 | 1.2% |


</details>

### GET_AITER

<details>
<summary> Successors and predecessors for GET_AITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,999,940 | 100.0% |
| RETURN_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ANEXT | 6,000,000 | 100.0% |


</details>

### GET_ANEXT

<details>
<summary> Successors and predecessors for GET_ANEXT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_AITER | 6,000,000 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 6,000,000 | 100.0% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 78,331,696 | 92.6% |
| LOAD_FAST | 3,309,180 | 3.9% |
| RETURN_VALUE | 2,446,800 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 489,658 | 0.6% |
| CALL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,577,934 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 209,691,087 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 77,367,747 | 13.3% |
| CALL_BUILTIN_CLASS | 61,416,602 | 10.6% |
| RETURN_VALUE | 49,965,060 | 8.6% |
| RETURN_GENERATOR | 37,669,200 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 188,416,262 | 32.5% |
| FOR_ITER_TUPLE | 120,729,855 | 20.8% |
| CALL_PY_EXACT_ARGS | 84,798,720 | 14.6% |
| FOR_ITER_GEN | 56,710,020 | 9.8% |
| FOR_ITER | 49,587,317 | 8.5% |


</details>

### GET_YIELD_FROM_ITER

<details>
<summary> Successors and predecessors for GET_YIELD_FROM_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 12,000,420 | 79.1% |
| RETURN_GENERATOR | 3,161,760 | 20.8% |
| LOAD_FAST | 7,080 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 15,169,260 | 100.0% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 1,397,760 | 75.6% |
| STORE_FAST | 450,480 | 24.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,848,240 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,530,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,397,760 | 91.3% |
| STORE_FAST | 131,940 | 8.6% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,353 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,413 | 52.3% |
| NOP | 3,060 | 36.3% |
| INSTRUMENTED_RETURN_CONST | 240 | 2.8% |
| LOAD_CONST | 240 | 2.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 240 | 2.8% |


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 3,060 | 70.3% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 873 | 20.1% |
| LIST_APPEND | 300 | 6.9% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 1.4% |
| POP_TOP | 60 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,353 | 100.0% |


</details>

### INSTRUMENTED_JUMP_FORWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 240 | 80.0% |
| STORE_FAST | 60 | 20.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 80.0% |
| LOAD_GLOBAL | 60 | 20.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 14,567,100 | 99.8% |
| TO_BOOL_BOOL | 13,920 | 0.1% |
| COMPARE_OP_STR | 7,020 | 0.0% |
| TO_BOOL_STR | 6,600 | 0.0% |
| EXTENDED_ARG | 3,300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,297,080 | 50.0% |
| LOAD_GLOBAL | 7,287,600 | 49.9% |
| LOAD_FAST_LOAD_FAST | 9,420 | 0.1% |
| INSTRUMENTED_RETURN_CONST | 4,740 | 0.0% |
| LOAD_CONST | 240 | 0.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 540 | 100.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 240 | 100.0% |


</details>

### INSTRUMENTED_POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for INSTRUMENTED_POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 5,313 | 53.2% |
| TO_BOOL | 3,060 | 30.6% |
| TO_BOOL_STR | 960 | 9.6% |
| TO_BOOL_NONE | 300 | 3.0% |
| COMPARE_OP_STR | 240 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,260 | 42.6% |
| LOAD_GLOBAL | 4,020 | 40.2% |
| INSTRUMENTED_JUMP_BACKWARD | 873 | 8.7% |
| INSTRUMENTED_RETURN_VALUE | 480 | 4.8% |
| LOAD_FAST_LOAD_FAST | 180 | 1.8% |


</details>

### INSTRUMENTED_RESUME

<details>
<summary> Successors and predecessors for INSTRUMENTED_RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,577,900 | 100.0% |
| CALL | 3,300 | 0.0% |
| RESUME | 1,020 | 0.0% |
| INSTRUMENTED_RESUME | 660 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,569,080 | 99.9% |
| LOAD_GLOBAL | 12,000 | 0.1% |
| RESUME | 960 | 0.0% |
| INSTRUMENTED_RESUME | 660 | 0.0% |
| PUSH_NULL | 240 | 0.0% |


</details>

### INSTRUMENTED_RETURN_CONST

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 4,740 | 87.8% |
| POP_TOP | 300 | 5.6% |
| INSTRUMENTED_FOR_ITER | 240 | 4.4% |
| CALL_NO_KW_LIST_APPEND | 60 | 1.1% |
| STORE_GLOBAL | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,800 | 88.9% |
| TO_BOOL_BOOL | 400 | 7.4% |
| POP_TOP | 180 | 3.3% |
| TO_BOOL | 20 | 0.4% |


</details>

### INSTRUMENTED_RETURN_VALUE

<details>
<summary> Successors and predecessors for INSTRUMENTED_RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,288,320 | 50.0% |
| BINARY_OP_ADD_INT | 7,283,520 | 50.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |
| CALL | 960 | 0.0% |
| BINARY_SLICE | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 7,283,520 | 50.0% |
| BINARY_OP_ADD_INT | 7,283,520 | 50.0% |
| STORE_FAST | 5,340 | 0.0% |
| TO_BOOL_BOOL | 1,200 | 0.0% |
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 450,585,378 | 37.8% |
| RETURN_CONST | 405,582,295 | 34.1% |
| RETURN_VALUE | 316,392,982 | 26.6% |
| RETURN_GENERATOR | 18,089,340 | 1.5% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,104,040 | 49.7% |
| LOAD_FAST_LOAD_FAST | 108,118,500 | 24.9% |
| LOAD_GLOBAL_MODULE | 80,709,974 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 11,341,740 | 2.6% |
| LOAD_CONST | 8,333,680 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 367,786,690 | 84.6% |
| POP_JUMP_IF_TRUE | 38,152,584 | 8.8% |
| EXTENDED_ARG | 18,001,680 | 4.1% |
| RETURN_VALUE | 3,140,700 | 0.7% |
| COPY | 2,904,060 | 0.7% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 554,035,080 | 27.3% |
| POP_JUMP_IF_TRUE | 458,282,166 | 22.6% |
| STORE_FAST | 220,275,827 | 10.9% |
| LIST_APPEND | 145,939,752 | 7.2% |
| POP_JUMP_IF_FALSE | 141,072,881 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 921,159,950 | 45.4% |
| FOR_ITER_RANGE | 424,856,883 | 20.9% |
| FOR_ITER_TUPLE | 290,423,043 | 14.3% |
| FOR_ITER | 206,628,256 | 10.2% |
| LOAD_FAST | 66,192,544 | 3.3% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,264,032 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,263,554 | 97.2% |
| SEND | 6,000,478 | 2.8% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 169,589,162 | 41.5% |
| POP_JUMP_IF_FALSE | 98,745,426 | 24.2% |
| POP_TOP | 55,297,384 | 13.5% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.4% |
| POP_JUMP_IF_NONE | 10,513,680 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 160,955,129 | 39.4% |
| LOAD_FAST_LOAD_FAST | 77,214,780 | 18.9% |
| LOAD_CONST | 37,226,114 | 9.1% |
| LOAD_GLOBAL_MODULE | 26,452,729 | 6.5% |
| LOAD_GLOBAL_BUILTIN | 25,564,550 | 6.3% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,411,118 | 25.2% |
| LOAD_CONST | 37,705,610 | 22.4% |
| LOAD_FAST_LOAD_FAST | 30,672,908 | 18.2% |
| LOAD_GLOBAL_MODULE | 18,000,780 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,341,020 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 142,854,556 | 84.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 24,569,440 | 14.6% |
| CALL_BUILTIN_CLASS | 1,051,200 | 0.6% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,850,040 | 19.8% |
| BUILD_TUPLE | 26,458,320 | 18.1% |
| BINARY_OP | 20,606,280 | 14.1% |
| LOAD_FAST | 18,169,800 | 12.4% |
| RETURN_VALUE | 14,861,680 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 145,939,752 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 37,120,149 | 77.7% |
| LOAD_FAST | 10,040,472 | 21.0% |
| LOAD_CONST | 366,720 | 0.8% |
| RETURN_VALUE | 119,072 | 0.2% |
| LOAD_DEREF | 77,460 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 47,193,229 | 98.8% |
| STORE_FAST | 265,472 | 0.6% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.4% |
| LOAD_FAST | 130,172 | 0.3% |
| BUILD_TUPLE | 2,940 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 707,317,847 | 59.0% |
| LOAD_GLOBAL_BUILTIN | 221,925,612 | 18.5% |
| LOAD_GLOBAL_MODULE | 94,753,982 | 7.9% |
| LOAD_ATTR_SLOT | 80,021,869 | 6.7% |
| LOAD_FAST_LOAD_FAST | 43,267,792 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 245,098,572 | 20.4% |
| IS_OP | 216,104,040 | 18.0% |
| STORE_FAST | 171,683,292 | 14.3% |
| LOAD_FAST_LOAD_FAST | 85,807,472 | 7.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 71,923,118 | 6.0% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,324,000 | 96.5% |
| LOAD_GLOBAL_BUILTIN | 1,786,752 | 1.5% |
| LOAD_FAST | 1,405,940 | 1.2% |
| LOAD_FAST_LOAD_FAST | 591,660 | 0.5% |
| LOAD_ATTR_MODULE | 358,500 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,700,000 | 49.5% |
| LOAD_FAST | 21,922,450 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,784,900 | 18.1% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.4% |
| LOAD_FAST_LOAD_FAST | 2,452,692 | 2.0% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,056,588,906 | 85.2% |
| LOAD_FAST_LOAD_FAST | 319,800,833 | 8.9% |
| COPY | 68,433,758 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 50,312,486 | 1.4% |
| BINARY_SUBSCR_LIST_INT | 38,546,760 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,037,017,334 | 28.9% |
| TO_BOOL_BOOL | 406,147,210 | 11.3% |
| STORE_FAST | 268,352,956 | 7.5% |
| LOAD_ATTR_METHOD_NO_DICT | 181,699,079 | 5.1% |
| RETURN_VALUE | 173,111,819 | 4.8% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 30,424,860 | 62.2% |
| LOAD_FAST | 18,487,960 | 37.8% |
| LOAD_ATTR | 400 | 0.0% |
| LOAD_ATTR_WITH_HINT | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 35,235,240 | 72.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 7,410,790 | 15.2% |
| LOAD_CONST | 4,823,940 | 9.9% |
| LOAD_FAST_LOAD_FAST | 1,228,800 | 2.5% |
| CALL | 119,450 | 0.2% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 752,047,023 | 57.7% |
| LOAD_ATTR_INSTANCE_VALUE | 181,699,079 | 13.9% |
| LOAD_CONST | 90,765,640 | 7.0% |
| LOAD_GLOBAL_MODULE | 52,834,996 | 4.1% |
| LOAD_ATTR_SLOT | 47,456,992 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 656,173,958 | 50.3% |
| LOAD_CONST | 145,903,401 | 11.2% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 143,899,269 | 11.0% |
| CALL_PY_EXACT_ARGS | 109,897,529 | 8.4% |
| LOAD_FAST_LOAD_FAST | 109,891,395 | 8.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,524,391,712 | 86.0% |
| LOAD_ATTR_INSTANCE_VALUE | 61,258,220 | 3.5% |
| LOAD_ATTR | 45,745,566 | 2.6% |
| LOAD_ATTR_SLOT | 44,399,621 | 2.5% |
| LOAD_ATTR_WITH_HINT | 36,664,789 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 778,134,348 | 43.9% |
| LOAD_FAST_LOAD_FAST | 463,313,665 | 26.1% |
| CALL_PY_EXACT_ARGS | 414,985,668 | 23.4% |
| LOAD_GLOBAL_MODULE | 48,869,271 | 2.8% |
| LOAD_CONST | 46,507,662 | 2.6% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 310,072,188 | 95.3% |
| LOAD_ATTR_MODULE | 11,590,180 | 3.6% |
| LOAD_ATTR | 1,339,026 | 0.4% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.4% |
| LOAD_FAST_LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 109,823,492 | 33.7% |
| LOAD_FAST_LOAD_FAST | 99,624,717 | 30.6% |
| CALL | 25,890,643 | 8.0% |
| CALL_NO_KW_ISINSTANCE | 21,884,900 | 6.7% |
| LOAD_GLOBAL_BUILTIN | 15,320,040 | 4.7% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 38,381,114 | 83.2% |
| LOAD_ATTR_SLOT | 5,106,822 | 11.1% |
| RETURN_VALUE | 1,251,000 | 2.7% |
| LOAD_ATTR_INSTANCE_VALUE | 931,920 | 2.0% |
| LOAD_FAST_LOAD_FAST | 125,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 40,520,086 | 87.8% |
| TO_BOOL_NONE | 3,107,760 | 6.7% |
| RETURN_VALUE | 830,731 | 1.8% |
| LOAD_FAST | 560,620 | 1.2% |
| LOAD_ATTR_WITH_HINT | 402,480 | 0.9% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,203,704,771 | 91.3% |
| LOAD_ATTR_SLOT | 40,633,234 | 3.1% |
| COPY | 40,131,480 | 3.0% |
| LOAD_DEREF | 12,824,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 9,558,240 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 305,105,907 | 23.2% |
| TO_BOOL_NONE | 85,430,518 | 6.5% |
| LOAD_ATTR | 80,021,869 | 6.1% |
| TO_BOOL_BOOL | 66,913,873 | 5.1% |
| COMPARE_OP_FLOAT | 65,983,588 | 5.0% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 268,039,091 | 79.3% |
| LOAD_ATTR_WITH_HINT | 22,487,880 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 22,336,752 | 6.6% |
| COPY | 12,982,380 | 3.8% |
| LOAD_FAST_LOAD_FAST | 7,809,620 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 82,481,200 | 24.4% |
| STORE_FAST | 42,837,840 | 12.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,664,789 | 10.8% |
| COMPARE_OP_INT | 35,140,620 | 10.4% |
| LOAD_CONST | 28,138,140 | 8.3% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,320 | 100.0% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,687,692,170 | 53.0% |
| LOAD_CONST | 646,942,679 | 7.3% |
| LOAD_FAST_LOAD_FAST | 366,372,654 | 4.1% |
| STORE_FAST | 279,085,865 | 3.2% |
| POP_JUMP_IF_FALSE | 256,653,526 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,584,754,444 | 17.9% |
| COMPARE_OP_STR | 1,560,608,652 | 17.6% |
| LOAD_FAST | 1,022,327,050 | 11.6% |
| LOAD_CONST | 646,942,679 | 7.3% |
| COMPARE_OP_INT | 572,768,616 | 6.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 333,048,090 | 41.3% |
| LOAD_GLOBAL_BUILTIN | 106,001,031 | 13.1% |
| PUSH_NULL | 37,562,108 | 4.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,640 | 3.9% |
| POP_JUMP_IF_NONE | 27,393,360 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 528,737,408 | 65.6% |
| LOAD_CONST | 69,699,308 | 8.6% |
| LOAD_FAST_LOAD_FAST | 29,692,296 | 3.7% |
| LOAD_DEREF | 23,803,531 | 3.0% |
| CALL_NO_KW_LEN | 20,446,300 | 2.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,324,800,908 | 16.2% |
| POP_JUMP_IF_FALSE | 4,307,796,892 | 16.1% |
| LOAD_GLOBAL_BUILTIN | 2,619,496,287 | 9.8% |
| RESUME | 2,016,471,804 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,037,017,334 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,687,692,170 | 17.5% |
| LOAD_ATTR_INSTANCE_VALUE | 3,056,588,906 | 11.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,524,391,712 | 5.7% |
| LOAD_ATTR_SLOT | 1,203,704,771 | 4.5% |
| LOAD_GLOBAL_BUILTIN | 1,089,588,005 | 4.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 38,676,184 | 76.8% |
| LOAD_FAST_AND_CLEAR | 11,698,592 | 23.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,668,024 | 76.8% |
| LOAD_FAST_AND_CLEAR | 11,698,592 | 23.2% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,616,680 | 51.7% |
| POP_TOP | 2,028,780 | 29.0% |
| LOAD_GLOBAL_BUILTIN | 421,740 | 6.0% |
| STORE_FAST | 308,040 | 4.4% |
| LOAD_ATTR_METHOD_NO_DICT | 298,440 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 51.1% |
| POP_JUMP_IF_NOT_NONE | 1,506,240 | 21.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 408,000 | 5.8% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 294,360 | 4.2% |
| LOAD_FAST | 250,680 | 3.6% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,179,864,179 | 16.7% |
| STORE_FAST | 1,141,318,453 | 16.2% |
| LOAD_FAST_LOAD_FAST | 516,898,216 | 7.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 463,313,665 | 6.6% |
| LOAD_GLOBAL_MODULE | 456,170,446 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 989,041,200 | 14.0% |
| LOAD_FAST | 716,741,091 | 10.1% |
| CALL_PY_EXACT_ARGS | 637,338,206 | 9.0% |
| BINARY_SUBSCR | 579,189,500 | 8.2% |
| LOAD_FAST_LOAD_FAST | 516,898,216 | 7.3% |


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 2,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 1,200 | 46.5% |
| LOAD_LOCALS | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 99.0% |
| STORE_FAST | 18,369 | 0.2% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 6,720 | 0.1% |
| NOP | 4,142 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,298,584 | 99.2% |
| LOAD_GLOBAL_MODULE | 30,426 | 0.4% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 11,836 | 0.2% |
| LOAD_FAST_LOAD_FAST | 3,600 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,089,588,005 | 27.0% |
| POP_JUMP_IF_FALSE | 971,097,482 | 24.0% |
| RESUME | 824,656,304 | 20.4% |
| STORE_FAST | 532,562,509 | 13.2% |
| POP_JUMP_IF_NOT_NONE | 96,121,300 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,619,496,287 | 64.8% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,160 | 10.8% |
| CALL_NO_KW_ISINSTANCE | 320,473,487 | 7.9% |
| LOAD_ATTR | 221,925,612 | 5.5% |
| LOAD_FAST_LOAD_FAST | 113,013,580 | 2.8% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 856,297,241 | 31.1% |
| STORE_FAST | 412,392,754 | 15.0% |
| RESUME | 322,916,532 | 11.7% |
| POP_JUMP_IF_FALSE | 264,641,151 | 9.6% |
| LOAD_FAST_LOAD_FAST | 113,351,040 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 456,170,446 | 16.6% |
| LOAD_FAST | 432,057,045 | 15.7% |
| CALL_NO_KW_ISINSTANCE | 330,235,073 | 12.0% |
| LOAD_ATTR_MODULE | 310,072,188 | 11.3% |
| CONTAINS_OP | 301,342,680 | 11.0% |


</details>

### LOAD_LOCALS

<details>
<summary> Successors and predecessors for LOAD_LOCALS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FROM_DICT_OR_DEREF | 1,200 | 46.5% |
| PUSH_NULL | 1,200 | 46.5% |
| LOAD_NAME | 180 | 7.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 100.0% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 1,320 | 84.6% |
| PUSH_NULL | 180 | 11.5% |
| STORE_NAME | 60 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 1,320 | 84.6% |
| LOAD_LOCALS | 180 | 11.5% |
| UNPACK_SEQUENCE_TUPLE | 40 | 2.6% |
| UNPACK_SEQUENCE | 20 | 1.3% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,180 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,160 | 98.3% |
| LOAD_SUPER_ATTR_ATTR | 20 | 1.7% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,270,200 | 100.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,191,620 | 96.5% |
| LOAD_GLOBAL_MODULE | 64,080 | 2.8% |
| LOAD_FAST_LOAD_FAST | 10,200 | 0.4% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 113,241,260 | 100.0% |
| LOAD_DEREF | 9,000 | 0.0% |
| LOAD_SUPER_ATTR | 1,160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 62,103,875 | 54.8% |
| LOAD_FAST | 36,953,460 | 32.6% |
| CALL_PY_EXACT_ARGS | 6,192,665 | 5.5% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.3% |
| CALL | 1,199,700 | 1.1% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,662,902 | 57.4% |
| CALL_PY_EXACT_ARGS | 24,891,451 | 30.0% |
| CALL_FUNCTION_EX | 4,707,040 | 5.7% |
| CALL | 3,797,580 | 4.6% |
| CALL_PY_WITH_DEFAULTS | 1,008,240 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,662,902 | 57.3% |
| RESUME | 34,861,151 | 41.9% |
| RETURN_GENERATOR | 580,860 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 93,651,649 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 81,658,549 | 87.2% |
| LOAD_FAST | 8,709,180 | 9.3% |
| LOAD_GLOBAL_MODULE | 2,504,360 | 2.7% |
| PUSH_NULL | 289,380 | 0.3% |
| KW_NAMES | 255,120 | 0.3% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,836,160 | 38.9% |
| RETURN_VALUE | 6,314,400 | 15.5% |
| LOAD_FAST | 5,930,640 | 14.6% |
| JUMP_FORWARD | 4,782,720 | 11.7% |
| STORE_FAST | 4,423,680 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 20,590,740 | 50.5% |
| JUMP_BACKWARD | 18,945,480 | 46.5% |
| CALL_FUNCTION_EX | 1,211,400 | 3.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 334,028,603 | 44.5% |
| STORE_FAST | 140,061,823 | 18.7% |
| POP_JUMP_IF_FALSE | 80,208,402 | 10.7% |
| STORE_ATTR_INSTANCE_VALUE | 51,296,769 | 6.8% |
| NOP | 49,330,312 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 309,055,680 | 41.2% |
| LOAD_FAST_LOAD_FAST | 279,657,036 | 37.3% |
| NOP | 49,330,312 | 6.6% |
| PUSH_NULL | 40,525,912 | 5.4% |
| LOAD_GLOBAL_BUILTIN | 27,610,707 | 3.7% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,776,380 | 57.1% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.9% |
| SWAP | 1,968,840 | 11.5% |
| COPY | 1,668,840 | 9.7% |
| STORE_FAST | 442,324 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,154,052 | 53.4% |
| RETURN_VALUE | 1,911,240 | 11.2% |
| JUMP_FORWARD | 1,715,820 | 10.0% |
| RERAISE | 1,668,840 | 9.7% |
| POP_TOP | 1,384,028 | 8.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 2,270,348,892 | 27.7% |
| CONTAINS_OP | 1,829,240,147 | 22.3% |
| COMPARE_OP_STR | 1,546,009,912 | 18.9% |
| COMPARE_OP_INT | 1,127,873,807 | 13.8% |
| IS_OP | 367,786,690 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,307,796,892 | 52.6% |
| LOAD_FAST_LOAD_FAST | 1,179,864,179 | 14.4% |
| LOAD_GLOBAL_BUILTIN | 971,097,482 | 11.9% |
| ENTER_EXECUTOR | 301,735,034 | 3.7% |
| LOAD_GLOBAL_MODULE | 264,641,151 | 3.2% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 190,698,341 | 67.6% |
| EXTENDED_ARG | 36,518,860 | 12.9% |
| LOAD_ATTR_SLOT | 25,233,420 | 8.9% |
| LOAD_DEREF | 13,535,820 | 4.8% |
| LOAD_ATTR_INSTANCE_VALUE | 8,203,695 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 127,050,214 | 45.0% |
| PUSH_NULL | 53,439,960 | 18.9% |
| LOAD_DEREF | 27,393,360 | 9.7% |
| JUMP_BACKWARD | 20,269,388 | 7.2% |
| RETURN_CONST | 15,339,451 | 5.4% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 336,329,061 | 82.5% |
| LOAD_ATTR_INSTANCE_VALUE | 26,533,344 | 6.5% |
| LOAD_ATTR | 17,310,628 | 4.2% |
| STORE_FAST_LOAD_FAST | 8,887,140 | 2.2% |
| EXTENDED_ARG | 7,189,900 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 145,829,408 | 35.8% |
| LOAD_GLOBAL_BUILTIN | 96,121,300 | 23.6% |
| LOAD_FAST_LOAD_FAST | 57,937,789 | 14.2% |
| LOAD_GLOBAL_MODULE | 35,093,707 | 8.6% |
| NOP | 18,185,789 | 4.5% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 717,785,782 | 49.8% |
| TO_BOOL | 130,175,071 | 9.0% |
| COMPARE_OP_INT | 120,646,094 | 8.4% |
| TO_BOOL_ALWAYS_TRUE | 82,642,920 | 5.7% |
| TO_BOOL_NONE | 77,262,712 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 567,730,559 | 39.4% |
| JUMP_BACKWARD | 458,282,166 | 31.8% |
| LOAD_GLOBAL_BUILTIN | 95,113,270 | 6.6% |
| LOAD_CONST | 67,479,039 | 4.7% |
| POP_TOP | 65,853,344 | 4.6% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 542,382,076 | 24.8% |
| RESUME | 471,385,040 | 21.5% |
| CALL_NO_KW_BUILTIN_O | 341,708,547 | 15.6% |
| POP_JUMP_IF_FALSE | 159,354,924 | 7.3% |
| RETURN_VALUE | 112,730,610 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 800,184,094 | 35.2% |
| JUMP_BACKWARD | 554,035,080 | 24.3% |
| RESUME | 238,120,116 | 10.5% |
| RETURN_CONST | 175,252,727 | 7.7% |
| ENTER_EXECUTOR | 98,142,309 | 4.3% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,320,500 | 31.1% |
| LOAD_ATTR | 3,246,420 | 19.0% |
| RAISE_VARARGS | 2,296,860 | 13.4% |
| CALL_NO_KW_BUILTIN_FAST | 1,783,220 | 10.4% |
| RERAISE | 1,632,360 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,712,112 | 91.7% |
| LOAD_GLOBAL_MODULE | 1,031,104 | 6.0% |
| LOAD_FAST | 386,940 | 2.3% |
| WITH_EXCEPT_START | 4,080 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 269,595,236 | 38.3% |
| POP_JUMP_IF_FALSE | 91,154,812 | 13.0% |
| POP_TOP | 70,133,764 | 10.0% |
| POP_JUMP_IF_NONE | 53,439,960 | 7.6% |
| NOP | 40,525,912 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 402,018,182 | 57.2% |
| LOAD_FAST_LOAD_FAST | 259,811,460 | 37.0% |
| LOAD_DEREF | 37,562,108 | 5.3% |
| LOAD_GLOBAL_BUILTIN | 3,415,800 | 0.5% |
| LOAD_GLOBAL_MODULE | 107,680 | 0.0% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,491,540 | 43.7% |
| LOAD_ATTR_MODULE | 583,740 | 17.1% |
| LOAD_CONST | 543,960 | 15.9% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 15.9% |
| LOAD_FAST | 150,960 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,296,860 | 67.3% |
| COPY | 963,300 | 28.2% |
| LOAD_CONST | 151,020 | 4.4% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,377,160 | 72.9% |
| POP_EXCEPT | 1,668,840 | 19.1% |
| POP_TOP | 386,940 | 4.4% |
| POP_JUMP_IF_FALSE | 154,860 | 1.8% |
| DELETE_FAST | 151,020 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,632,360 | 68.9% |
| COPY | 696,900 | 29.4% |
| CALL_INTRINSIC_1 | 41,160 | 1.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,453,160,352 | 63.7% |
| POP_TOP | 238,120,116 | 6.2% |
| SEND_GEN | 208,263,554 | 5.4% |
| CALL | 202,723,336 | 5.3% |
| COPY_FREE_VARS | 172,200,818 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,016,471,804 | 41.6% |
| LOAD_GLOBAL_BUILTIN | 824,656,304 | 17.0% |
| POP_TOP | 471,385,040 | 9.7% |
| NOP | 334,028,603 | 6.9% |
| LOAD_GLOBAL_MODULE | 322,916,532 | 6.7% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 251,444,397 | 19.3% |
| STORE_ATTR_SLOT | 245,133,585 | 18.8% |
| POP_TOP | 175,252,727 | 13.4% |
| STORE_ATTR_INSTANCE_VALUE | 172,941,802 | 13.3% |
| RESUME | 122,694,660 | 9.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 542,382,076 | 41.6% |
| INTERPRETER_EXIT | 405,582,295 | 31.1% |
| EXIT_INIT_CHECK | 66,525,890 | 5.1% |
| END_FOR | 56,697,480 | 4.3% |
| TO_BOOL_BOOL | 56,314,251 | 4.3% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,280,976 | 63.8% |
| COPY_FREE_VARS | 73,398,180 | 33.4% |
| CALL_PY_WITH_DEFAULTS | 3,297,720 | 1.5% |
| CALL_FUNCTION_EX | 1,713,800 | 0.8% |
| CALL | 768,180 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,331,696 | 32.9% |
| GET_ITER | 37,669,200 | 15.8% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,040 | 13.9% |
| STORE_FAST | 19,529,340 | 8.2% |
| INTERPRETER_EXIT | 18,089,340 | 7.6% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 753,396,965 | 25.9% |
| RETURN_VALUE | 503,222,056 | 17.3% |
| BUILD_TUPLE | 405,100,080 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 173,111,819 | 5.9% |
| BINARY_SUBSCR_DICT | 104,365,328 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 599,386,526 | 20.6% |
| RETURN_VALUE | 503,222,056 | 17.3% |
| INTERPRETER_EXIT | 316,392,982 | 10.9% |
| UNPACK_SEQUENCE_TUPLE | 258,461,820 | 8.9% |
| TO_BOOL_BOOL | 247,046,667 | 8.5% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 94,136,760 | 83.8% |
| LOAD_CONST | 12,162,978 | 10.8% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,000,478 | 5.3% |
| SEND | 28,140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,299,238 | 89.3% |
| YIELD_VALUE | 6,000,718 | 5.3% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,140 | 0.0% |
| SEND_GEN | 260 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,263,554 | 69.0% |
| LOAD_CONST | 93,584,216 | 31.0% |
| SEND | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,263,554 | 69.0% |
| POP_TOP | 93,584,476 | 31.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 4.0% |
| STORE_FAST_LOAD_FAST | 48,000 | 1.5% |
| LOAD_FAST | 19,440 | 0.6% |
| BINARY_SUBSCR_LIST_INT | 17,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,100,800 | 100.0% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 81,658,549 | 98.9% |
| SET_FUNCTION_ATTRIBUTE | 918,611 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 54,014,460 | 65.4% |
| LOAD_GLOBAL_BUILTIN | 18,989,160 | 23.0% |
| STORE_FAST | 5,351,078 | 6.5% |
| CALL_PY_EXACT_ARGS | 2,026,800 | 2.5% |
| SET_FUNCTION_ATTRIBUTE | 918,611 | 1.1% |


</details>

### SET_UPDATE

<details>
<summary> Successors and predecessors for SET_UPDATE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 360 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 240 | 66.7% |
| LOAD_GLOBAL_BUILTIN | 120 | 33.3% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 31,046,481 | 58.8% |
| LOAD_FAST_LOAD_FAST | 15,233,200 | 28.9% |
| CALL | 5,419,260 | 10.3% |
| SWAP | 946,536 | 1.8% |
| LOAD_ATTR_MODULE | 38,220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,575,488 | 29.5% |
| LOAD_DEREF | 13,446,120 | 25.5% |
| RETURN_CONST | 8,603,220 | 16.3% |
| JUMP_BACKWARD | 5,554,200 | 10.5% |
| LOAD_FAST_LOAD_FAST | 4,676,300 | 8.9% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 348,205,919 | 44.3% |
| LOAD_FAST_LOAD_FAST | 294,770,672 | 37.5% |
| SWAP | 68,625,225 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.4% |
| RETURN_VALUE | 20,943,360 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 282,615,834 | 35.9% |
| RETURN_CONST | 172,941,802 | 22.0% |
| LOAD_FAST_LOAD_FAST | 165,260,320 | 21.0% |
| LOAD_CONST | 65,269,079 | 8.3% |
| NOP | 51,296,769 | 6.5% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 510,409,828 | 48.6% |
| LOAD_FAST | 497,588,162 | 47.3% |
| SWAP | 40,131,480 | 3.8% |
| STORE_ATTR_SLOT | 2,110,698 | 0.2% |
| LOAD_ATTR_SLOT | 636,960 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 276,224,231 | 26.3% |
| LOAD_FAST | 251,876,696 | 24.0% |
| RETURN_CONST | 245,133,585 | 23.3% |
| LOAD_CONST | 216,372,042 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 24,862,340 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 27,035,683 | 51.0% |
| SWAP | 12,982,380 | 24.5% |
| LOAD_FAST_LOAD_FAST | 12,436,500 | 23.5% |
| LOAD_DEREF | 240,940 | 0.5% |
| RETURN_VALUE | 224,100 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,616,640 | 63.4% |
| RETURN_CONST | 6,693,707 | 12.6% |
| JUMP_BACKWARD | 5,313,540 | 10.0% |
| LOAD_CONST | 3,923,460 | 7.4% |
| LOAD_FAST_LOAD_FAST | 2,308,020 | 4.4% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,873,520 | 41.3% |
| STORE_FAST | 19,047,000 | 29.3% |
| LOAD_CONST | 6,734,880 | 10.3% |
| LOAD_FAST | 2,916,480 | 4.5% |
| YIELD_VALUE | 2,419,200 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,280 | 29.2% |
| LOAD_DEREF | 13,725,300 | 21.1% |
| LOAD_FAST_LOAD_FAST | 13,436,760 | 20.6% |
| LOAD_FAST | 9,470,440 | 14.5% |
| LOAD_CONST | 4,658,340 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,079,413,438 | 11.4% |
| BINARY_SUBSCR | 970,627,832 | 10.3% |
| STORE_FAST | 709,867,112 | 7.5% |
| RETURN_VALUE | 599,386,526 | 6.3% |
| FOR_ITER_LIST | 584,783,292 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,324,800,908 | 45.7% |
| LOAD_FAST_LOAD_FAST | 1,141,318,453 | 12.1% |
| STORE_FAST | 709,867,112 | 7.5% |
| ENTER_EXECUTOR | 697,846,320 | 7.4% |
| LOAD_GLOBAL_BUILTIN | 532,562,509 | 5.6% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 80,255,100 | 60.6% |
| FOR_ITER_RANGE | 35,405,280 | 26.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 9,187,080 | 6.9% |
| FOR_ITER_TUPLE | 5,055,840 | 3.8% |
| FOR_ITER | 2,370,600 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 29,577,540 | 22.3% |
| LOAD_FAST | 24,358,500 | 18.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 20,555,520 | 15.5% |
| STORE_ATTR_INSTANCE_VALUE | 9,259,200 | 7.0% |
| POP_JUMP_IF_NOT_NONE | 8,887,140 | 6.7% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| UNPACK_SEQUENCE_TWO_TUPLE | 361,776,446 | 23.7% |
| UNPACK_SEQUENCE_LIST | 134,204,100 | 8.8% |
| UNPACK_SEQUENCE_TUPLE | 132,476,520 | 8.7% |
| LOAD_ATTR_SLOT | 45,908,040 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 815,096,820 | 53.3% |
| LOAD_FAST | 447,135,068 | 29.3% |
| LOAD_FAST_LOAD_FAST | 86,224,218 | 5.6% |
| STORE_FAST | 67,380,000 | 4.4% |
| LOAD_GLOBAL_MODULE | 46,034,580 | 3.0% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,147,600 | 99.9% |
| RETURN_VALUE | 3,900 | 0.1% |
| LOAD_ATTR | 540 | 0.0% |
| LOAD_FAST | 300 | 0.0% |
| BUILD_MAP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,864,260 | 79.1% |
| LOAD_GLOBAL_MODULE | 1,285,980 | 20.9% |
| LOAD_CONST | 1,920 | 0.0% |
| RETURN_CONST | 120 | 0.0% |
| INSTRUMENTED_RETURN_CONST | 60 | 0.0% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 1,320 | 27.5% |
| LOAD_CONST | 1,320 | 27.5% |
| LOAD_ATTR | 1,200 | 25.0% |
| IMPORT_NAME | 360 | 7.5% |
| CALL_NO_KW_BUILTIN_FAST | 180 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,680 | 35.0% |
| LOAD_CONST | 1,440 | 30.0% |
| PUSH_NULL | 1,380 | 28.7% |
| LOAD_FAST | 120 | 2.5% |
| STORE_NAME | 120 | 2.5% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,909,260 | 88.3% |
| LOAD_CONST | 13,458,840 | 11.4% |
| LOAD_FAST_LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,578,320 | 91.5% |
| RETURN_CONST | 5,855,760 | 5.0% |
| LOAD_FAST_LOAD_FAST | 4,157,040 | 3.5% |
| JUMP_BACKWARD | 39,840 | 0.0% |
| LOAD_GLOBAL_BUILTIN | 2,700 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 109,571,980 | 34.7% |
| LOAD_FAST | 64,708,056 | 20.5% |
| LOAD_FAST_LOAD_FAST | 56,745,560 | 18.0% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.2% |
| LOAD_CONST | 27,782,080 | 8.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.5% |
| LOAD_FAST_LOAD_FAST | 104,111,580 | 33.0% |
| RETURN_CONST | 33,817,800 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,002,980 | 8.6% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 92,271,520 | 47.9% |
| LOAD_FAST | 62,228,077 | 32.3% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.3% |
| RETURN_VALUE | 7,992,040 | 4.2% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,919,800 | 37.9% |
| LOAD_FAST | 64,211,656 | 33.4% |
| JUMP_BACKWARD | 28,272,300 | 14.7% |
| RETURN_CONST | 12,747,120 | 6.6% |
| LOAD_GLOBAL_MODULE | 7,339,700 | 3.8% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 157,633,380 | 53.1% |
| LOAD_FAST | 56,880,860 | 19.2% |
| LOAD_CONST | 26,874,440 | 9.1% |
| LOAD_FAST_LOAD_FAST | 24,036,360 | 8.1% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 110,152,700 | 37.1% |
| JUMP_BACKWARD | 110,064,240 | 37.1% |
| LOAD_FAST_LOAD_FAST | 71,536,320 | 24.1% |
| RETURN_CONST | 4,469,160 | 1.5% |
| LOAD_CONST | 230,760 | 0.1% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.6% |
| BINARY_OP_ADD_FLOAT | 116,255,040 | 12.9% |
| LOAD_FAST | 94,640,153 | 10.5% |
| BINARY_OP_ADD_INT | 78,399,716 | 8.7% |
| BINARY_OP_SUBTRACT_INT | 67,852,757 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 267,776,280 | 29.6% |
| STORE_SUBSCR_LIST_INT | 157,633,380 | 17.4% |
| STORE_SUBSCR | 109,571,980 | 12.1% |
| COPY | 105,748,980 | 11.7% |
| STORE_ATTR_INSTANCE_VALUE | 68,625,225 | 7.6% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,547,617 | 82.0% |
| LOAD_ATTR_INSTANCE_VALUE | 23,131,253 | 11.7% |
| LOAD_ATTR | 7,536,128 | 3.8% |
| LOAD_ATTR_SLOT | 2,026,400 | 1.0% |
| COPY | 2,014,844 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 130,175,071 | 65.7% |
| POP_JUMP_IF_FALSE | 67,453,403 | 34.0% |
| TO_BOOL | 230,133 | 0.1% |
| UNARY_NOT | 220,620 | 0.1% |
| TO_BOOL_NONE | 124,925 | 0.1% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,287,621 | 46.7% |
| LOAD_ATTR_INSTANCE_VALUE | 59,720,780 | 33.5% |
| LOAD_ATTR_SLOT | 17,755,080 | 10.0% |
| STORE_FAST_LOAD_FAST | 7,990,920 | 4.5% |
| COPY | 6,842,050 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 93,973,961 | 52.7% |
| POP_JUMP_IF_TRUE | 82,642,920 | 46.4% |
| EXTENDED_ARG | 901,240 | 0.5% |
| TO_BOOL_NONE | 600,767 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 116,500 | 0.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_ISINSTANCE | 764,715,980 | 24.5% |
| LOAD_FAST | 713,319,982 | 22.9% |
| CALL_NO_KW_BUILTIN_FAST | 477,106,524 | 15.3% |
| LOAD_ATTR_INSTANCE_VALUE | 406,147,210 | 13.0% |
| RETURN_VALUE | 247,046,667 | 7.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,270,348,892 | 72.9% |
| POP_JUMP_IF_TRUE | 717,785,782 | 23.0% |
| EXTENDED_ARG | 81,547,640 | 2.6% |
| UNARY_NOT | 46,376,646 | 1.5% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 13,920 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 175,186,785 | 77.4% |
| CALL_NO_KW_BUILTIN_O | 12,835,620 | 5.7% |
| BINARY_OP | 11,035,081 | 4.9% |
| COPY | 7,502,235 | 3.3% |
| LOAD_ATTR_SLOT | 6,926,500 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 201,132,298 | 88.9% |
| POP_JUMP_IF_TRUE | 23,900,576 | 10.6% |
| UNARY_NOT | 1,035,540 | 0.5% |
| EXTENDED_ARG | 164,040 | 0.1% |
| TO_BOOL_BOOL | 13,620 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,349,065 | 67.3% |
| LOAD_ATTR_INSTANCE_VALUE | 26,968,703 | 24.4% |
| LOAD_ATTR_SLOT | 5,049,000 | 4.6% |
| LOAD_ATTR | 1,779,620 | 1.6% |
| COPY | 814,260 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 61,623,440 | 55.8% |
| POP_JUMP_IF_FALSE | 45,309,325 | 41.0% |
| UNARY_NOT | 2,640,720 | 2.4% |
| EXTENDED_ARG | 900,900 | 0.8% |
| TO_BOOL | 23,200 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 169,198,645 | 45.4% |
| LOAD_ATTR_SLOT | 85,430,518 | 22.9% |
| LOAD_ATTR_INSTANCE_VALUE | 53,217,780 | 14.3% |
| LOAD_ATTR | 21,930,700 | 5.9% |
| RETURN_CONST | 13,912,340 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 293,868,814 | 78.8% |
| POP_JUMP_IF_TRUE | 77,262,712 | 20.7% |
| EXTENDED_ARG | 967,020 | 0.3% |
| TO_BOOL_ALWAYS_TRUE | 600,853 | 0.2% |
| TO_BOOL | 123,676 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,557,180 | 63.9% |
| LOAD_ATTR_SLOT | 7,140,480 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 4,424,880 | 6.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 3,881,220 | 5.8% |
| COPY | 2,668,380 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 35,708,200 | 53.6% |
| POP_JUMP_IF_TRUE | 30,267,560 | 45.4% |
| UNARY_NOT | 600,240 | 0.9% |
| TO_BOOL_NONE | 36,180 | 0.1% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 6,600 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,115,015 | 85.0% |
| LOAD_ATTR_MODULE | 1,443,888 | 12.1% |
| LOAD_ATTR | 209,464 | 1.8% |
| LOAD_FAST | 122,040 | 1.0% |
| LOAD_FAST_LOAD_FAST | 10,260 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 11,900,667 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 107,898,960 | 89.0% |
| LOAD_FAST_LOAD_FAST | 7,964,640 | 6.6% |
| LOAD_GLOBAL_MODULE | 3,058,560 | 2.5% |
| BINARY_SUBSCR_TUPLE_INT | 1,205,640 | 1.0% |
| CALL_NO_KW_LEN | 668,220 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 79,368,120 | 65.5% |
| BINARY_SUBSCR_LIST_INT | 26,768,580 | 22.1% |
| CALL_PY_EXACT_ARGS | 3,191,160 | 2.6% |
| STORE_SUBSCR | 2,419,140 | 2.0% |
| BINARY_SUBSCR | 2,419,140 | 2.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 46,376,646 | 91.1% |
| TO_BOOL_LIST | 2,640,720 | 5.2% |
| TO_BOOL_INT | 1,035,540 | 2.0% |
| TO_BOOL_STR | 600,240 | 1.2% |
| TO_BOOL | 220,620 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 23,463,000 | 46.1% |
| RETURN_VALUE | 15,093,966 | 29.7% |
| KW_NAMES | 10,514,640 | 20.7% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.5% |
| LOAD_FAST | 555,240 | 1.1% |


</details>

### UNPACK_EX

<details>
<summary> Successors and predecessors for UNPACK_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 218,520 | 99.2% |
| CALL_INTRINSIC_1 | 960 | 0.4% |
| FOR_ITER | 720 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 220,200 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 96,120 | 46.4% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,940 | 32.8% |
| COPY | 19,920 | 9.6% |
| FOR_ITER_LIST | 10,560 | 5.1% |
| LOAD_FAST | 9,120 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 126,600 | 61.2% |
| STORE_FAST | 78,240 | 37.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,420 | 0.7% |
| UNPACK_SEQUENCE | 380 | 0.2% |
| UNPACK_SEQUENCE_TUPLE | 360 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,417,940 | 70.2% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,000,900 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 799,560 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 134,204,100 | 95.7% |
| STORE_FAST | 6,004,980 | 4.3% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 258,461,820 | 61.6% |
| LOAD_FAST | 102,710,520 | 24.5% |
| BINARY_SUBSCR_DICT | 14,268,900 | 3.4% |
| STORE_FAST | 12,281,520 | 2.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,001,200 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 262,729,360 | 62.6% |
| STORE_FAST_STORE_FAST | 132,476,520 | 31.6% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.7% |
| LOAD_FAST | 290,520 | 0.1% |
| POP_TOP | 120 | 0.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,191,784 | 52.5% |
| FOR_ITER | 147,896,520 | 24.7% |
| RETURN_VALUE | 84,038,180 | 14.0% |
| LOAD_FAST | 35,322,780 | 5.9% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 361,776,446 | 60.4% |
| STORE_FAST | 214,698,100 | 35.9% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST_LOAD_FAST | 9,187,080 | 1.5% |
| LOAD_FAST | 904,080 | 0.2% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 4,080 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 4,080 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 30.5% |
| YIELD_VALUE | 208,263,554 | 30.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 13.6% |
| BINARY_SUBSCR | 30,970,080 | 4.5% |
| LOAD_CONST | 26,856,640 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 450,585,378 | 65.1% |
| YIELD_VALUE | 208,263,554 | 30.1% |
| STORE_FAST | 24,437,700 | 3.5% |
| UNPACK_SEQUENCE_TUPLE | 4,808,640 | 0.7% |
| STORE_DEREF | 2,419,200 | 0.3% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    197881234 | 4.6% |
| specialization.deopt |      1598863 | 0.0% |
|          hit |   3986982892 | 93.4% |
|         miss |     84770397 | 2.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,609,112 | 81.0% |
| Failure | 377,909 | 19.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| number | 135,740 | 35.9% |
| other | 125,880 | 33.3% |
| tuple | 74,420 | 19.7% |
| dict | 14,700 | 3.9% |
| bytes | 10,613 | 2.8% |
| set | 5,820 | 1.5% |
| sequence | 5,460 | 1.4% |
| mapping | 4,276 | 1.1% |
| float | 640 | 0.2% |
| bytearray | 280 | 0.1% |
| memory view | 80 | 0.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2342568804 | 56.2% |
| specialization.deopt |        60040 | 0.0% |
|          hit |   1822521194 | 43.7% |
|         miss |      3183300 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 61,557 | 9.5% |
| Failure | 588,421 | 90.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 304,920 | 51.8% |
| array int | 112,980 | 19.2% |
| other | 76,520 | 13.0% |
| out of range | 40,400 | 6.9% |
| list slice | 25,500 | 4.3% |
| buffer int | 23,741 | 4.0% |
| sequence int | 2,920 | 0.5% |
| code complex parameters | 1,340 | 0.2% |
| buffer slice | 40 | 0.0% |
| tuple slice | 40 | 0.0% |
| string slice | 20 | 0.0% |


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    315713088 | 39.0% |
| specialization.deopt |           40 | 0.0% |
|          hit |    494015236 | 61.0% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 588 | 0.7% |
| Failure | 83,300 | 99.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| array int | 45,640 | 54.8% |
| dict subclass no override | 17,700 | 21.2% |
| py simple | 13,580 | 16.3% |
| bytearray int | 5,200 | 6.2% |
| out of range | 1,020 | 1.2% |
| other | 120 | 0.1% |
| list slice | 40 | 0.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |       204840 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1155798986 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 49,880 | 99.2% |
| Failure | 380 | 0.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 180 | 47.4% |
| iterator | 120 | 31.6% |
| other | 80 | 21.1% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    281552652 | 11.3% |
| specialization.deopt |      2480434 | 0.1% |
|          hit |   2086131344 | 83.5% |
|         miss |    131463450 | 5.3% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,035 | 96.5% |
| Failure | 89,977 | 3.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 22,900 | 25.5% |
| dict items | 17,780 | 19.8% |
| seq iter | 15,120 | 16.8% |
| set | 10,797 | 12.0% |
| other | 7,500 | 8.3% |
| reversed list | 3,580 | 4.0% |
| dict values | 3,380 | 3.8% |
| zip | 3,100 | 3.4% |
| ascii string | 2,680 | 3.0% |
| dict keys | 1,780 | 2.0% |
| map | 600 | 0.7% |
| itertools | 600 | 0.7% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     52735089 | 2.7% |
| specialization.deopt |      3474742 | 0.2% |
|          hit |   1706184384 | 87.8% |
|         miss |    184167235 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,489,590 | 99.0% |
| Failure | 34,580 | 1.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,120 | 49.5% |
| not in dict | 8,020 | 23.2% |
| overriding descriptor | 4,940 | 14.3% |
| not in keys | 920 | 2.7% |
| non object slot | 920 | 2.7% |
| no dict | 800 | 2.3% |
| property | 760 | 2.2% |
| overridden | 640 | 1.9% |
| not managed dict | 340 | 1.0% |
| method | 120 | 0.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1197795400 | 11.9% |
| specialization.deopt |      9043144 | 0.1% |
|          hit |   8380672821 | 83.3% |
|         miss |    479408768 | 4.8% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,091,175 | 86.0% |
| Failure | 1,475,173 | 14.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 642,940 | 43.6% |
| class attr simple | 580,863 | 39.4% |
| metaclass attribute | 98,884 | 6.7% |
| not managed dict | 66,841 | 4.5% |
| method | 51,214 | 3.5% |
| class method obj | 7,000 | 0.5% |
| non object slot | 6,700 | 0.5% |
| class attr descriptor | 5,740 | 0.4% |
| overridden | 5,240 | 0.4% |
| non overriding descriptor | 4,032 | 0.3% |
| mutable class | 2,320 | 0.2% |
| not in keys | 1,680 | 0.1% |
| module attr not found | 1,160 | 0.1% |
| builtin class method | 360 | 0.0% |
| shadowed | 199 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    134793467 | 4.2% |
| specialization.deopt |        23668 | 0.0% |
|          hit |   3087127670 | 95.8% |
|         miss |      1254909 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 26,869 | 20.1% |
| Failure | 106,689 | 79.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 45,576 | 42.7% |
| different types | 24,144 | 22.6% |
| baseobject | 12,880 | 12.1% |
| float long | 8,842 | 8.3% |
| set | 6,620 | 6.2% |
| other | 2,800 | 2.6% |
| bool | 2,327 | 2.2% |
| tuple | 1,640 | 1.5% |
| list | 1,020 | 1.0% |
| bytes | 640 | 0.6% |
| string | 140 | 0.1% |
| long float | 60 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322096 | 0.1% |
| specialization.deopt |          250 | 0.0% |
|          hit |   6789204258 | 99.9% |
|         miss |        17110 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 39,052 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    825382811 | 15.5% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   4455515574 | 83.8% |
|         miss |     37779500 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 715,962 | 39.4% |
| Failure | 1,102,886 | 60.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 578,820 | 52.5% |
| multiply different types | 171,355 | 15.5% |
| add different types | 151,660 | 13.8% |
| floor divide | 32,520 | 2.9% |
| remainder | 31,546 | 2.9% |
| add other | 29,080 | 2.6% |
| and int | 25,008 | 2.3% |
| lshift | 18,620 | 1.7% |
| rshift | 16,540 | 1.5% |
| true divide different types | 14,340 | 1.3% |
| xor | 10,420 | 0.9% |
| true divide float | 6,640 | 0.6% |
| subtract other | 5,440 | 0.5% |
| power | 3,640 | 0.3% |
| or | 3,457 | 0.3% |
| multiply other | 1,940 | 0.2% |
| true divide other | 980 | 0.1% |
| and other | 820 | 0.1% |
| and different types | 60 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112299956 | 27.1% |
|          hit |    301848030 | 72.9% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 260 | 0.9% |
| Failure | 28,140 | 99.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| async generator send | 24,440 | 86.9% |
| other | 3,660 | 13.0% |
| list | 40 | 0.1% |


</details>

### JUMP_BACKWARD

<details>
<summary> specialization stats for JUMP_BACKWARD family </summary>

|Kind | Count | Ratio | 
|---|---|---|


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
|          hit |    115521760 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,180 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    871665341 | 10.1% |
| specialization.deopt |      2744727 | 0.0% |
|          hit |   7579456289 | 88.2% |
|         miss |    145575584 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,779,465 | 88.4% |
| Failure | 363,753 | 11.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr method fastcall keywords | 65,020 | 17.9% |
| kwnames | 51,097 | 14.0% |
| no dict | 50,420 | 13.9% |
| code complex parameters | 48,565 | 13.4% |
| class no vectorcall | 25,304 | 7.0% |
| cfunc varargs keywords | 23,336 | 6.4% |
| meth descr varargs | 20,910 | 5.7% |
| cfunc noargs | 17,299 | 4.8% |
| init not python | 10,360 | 2.8% |
| other | 10,304 | 2.8% |
| class mutable | 7,826 | 2.2% |
| init not simple | 7,780 | 2.1% |
| meth descr varargs keywords | 7,150 | 2.0% |
| cmethod | 3,540 | 1.0% |
| wrong number arguments | 3,480 | 1.0% |
| bound method | 3,365 | 0.9% |
| cfunc varargs | 2,520 | 0.7% |
| method wrapper | 2,466 | 0.7% |
| operator wrapper | 2,031 | 0.6% |
| str | 980 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 90,321,982,107 | 63.7% |
| Not specialized | 9,804,909,628 | 6.9% |
| Specialized | 41,569,845,923 | 29.3% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,342,568,804 | 36.9% |
| LOAD_ATTR | 1,197,795,400 | 18.9% |
| CALL | 871,665,341 | 13.7% |
| BINARY_OP | 825,382,811 | 13.0% |
| STORE_SUBSCR | 315,713,088 | 5.0% |
| FOR_ITER | 281,552,652 | 4.4% |
| TO_BOOL | 197,881,234 | 3.1% |
| COMPARE_OP | 134,793,467 | 2.1% |
| SEND | 112,299,956 | 1.8% |
| STORE_ATTR | 52,735,089 | 0.8% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 207,705,047 | 19.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 154,144,388 | 14.4% |
| STORE_ATTR_SLOT | 111,857,878 | 10.5% |
| CALL_PY_EXACT_ARGS | 86,726,304 | 8.1% |
| STORE_ATTR_INSTANCE_VALUE | 69,158,387 | 6.5% |
| FOR_ITER_LIST | 65,827,560 | 6.2% |
| FOR_ITER_TUPLE | 65,584,770 | 6.1% |
| LOAD_ATTR_SLOT | 56,470,397 | 5.3% |
| LOAD_ATTR_METHOD_NO_DICT | 45,366,632 | 4.2% |
| TO_BOOL_NONE | 41,150,278 | 3.8% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,199,017,598 | 23.5% |
| Calls to Python functions inlined | 3,909,946,773 | 76.5% |
| Calls via PyEval_EvalFrame (total) | 1,199,017,598 | 23.5% |
| Calls via PyEval_EvalFrame (vector) | 660,594,060 | 12.9% |
| Calls via PyEval_EvalFrame (generator) | 538,423,538 | 10.5% |
| Calls via PyEval_EvalFrame (legacy) | 3,780 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 660,588,960 | 12.9% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 188,879,342 | 3.7% |
| Calls via PyEval_EvalFrame (function ex) | 9,423,700 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 112,457,288 | 2.2% |
| Calls via PyEval_EvalFrame (method) | 93,801,247 | 1.8% |
| Frames pushed | 4,245,343,913 | 83.1% |
| Frame objects created | 58,903,528 | 1.2% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,082,413,812 | 35.3% |
| Frees to freelist | 4,086,290,898 |  |
| Allocations | 7,497,914,381 | 64.7% |
| Allocations to 512 bytes | 7,417,229,156 | 64.1% |
| Allocations to 4 kbytes | 65,715,579 | 0.6% |
| Allocations over 4 kbytes | 14,969,646 | 0.1% |
| Frees | 7,744,069,450 |  |
| New values | 57,243,880 |  |
| Interpreter increfs | 56,177,897,384 | 76.6% |
| Interpreter decrefs | 65,174,044,456 | 77.3% |
| Increfs | 17,197,718,313 | 23.4% |
| Decrefs | 19,174,574,387 | 22.7% |
| Materialize dict (on request) | 3,684,060 | 6.4% |
| Materialize dict (new key) | 57,960 | 0.1% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,956,465,782 |  |
| Method cache misses | 71,180,038 |  |
| Method cache collisions | 79,260,423 |  |
| Method cache dunder hits | 2,149,543,823 |  |
| Method cache dunder misses | 8,120,370 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,265 |


</details>

---
Stats gathered on: 2023-07-02
