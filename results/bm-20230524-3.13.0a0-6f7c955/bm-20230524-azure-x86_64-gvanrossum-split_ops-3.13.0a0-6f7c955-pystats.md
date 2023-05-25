
# Pystats results

- fork: gvanrossum
- ref: split-ops
- commit hash: 6f7c955
- commit date: 2023-05-24T20:33:58-07:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 18,185,243,013 | 13.7% | 13.7% |  |
| POP_JUMP_IF_FALSE | 8,416,591,914 | 6.3% | 20.0% |  |
| LOAD_FAST__LOAD_FAST | 7,592,243,708 | 5.7% | 25.7% |  |
| STORE_FAST__LOAD_FAST | 5,902,343,816 | 4.4% | 30.1% |  |
| RESUME | 5,024,791,977 | 3.8% | 33.9% |  |
| LOAD_CONST | 4,749,714,298 | 3.6% | 37.5% |  |
| LOAD_GLOBAL_BUILTIN | 4,084,841,698 | 3.1% | 40.5% | 0.0% |
| LOAD_FAST__LOAD_CONST | 3,746,713,818 | 2.8% | 43.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 3,741,163,370 | 2.8% | 46.1% | 6.2% |
| JUMP_BACKWARD | 3,284,806,610 | 2.5% | 48.6% |  |
| STORE_FAST | 3,126,602,786 | 2.3% | 51.0% |  |
| RETURN_VALUE | 2,921,629,749 | 2.2% | 53.1% |  |
| LOAD_GLOBAL_MODULE | 2,916,199,638 | 2.2% | 55.3% | 0.0% |
| CALL_PY_EXACT_ARGS | 2,822,893,208 | 2.1% | 57.5% | 3.3% |
| POP_TOP | 2,394,076,034 | 1.8% | 59.3% |  |
| BINARY_SUBSCR | 2,353,387,301 | 1.8% | 61.0% |  |
| BINARY_OP_ADD_INT | 2,207,023,774 | 1.7% | 62.7% | 0.0% |
| STORE_FAST__STORE_FAST | 2,029,275,024 | 1.5% | 64.2% |  |
| CONTAINS_OP | 1,989,446,367 | 1.5% | 65.7% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,818,994,712 | 1.4% | 67.1% | 9.3% |
| COMPARE_OP_STR | 1,597,003,333 | 1.2% | 68.3% | 0.0% |
| POP_JUMP_IF_TRUE | 1,483,856,248 | 1.1% | 69.4% |  |
| NOP | 1,480,835,614 | 1.1% | 70.5% |  |
| COMPARE_OP_INT | 1,418,358,657 | 1.1% | 71.6% | 0.1% |
| LOAD_ATTR_SLOT | 1,331,325,241 | 1.0% | 72.6% | 4.2% |
| RETURN_CONST | 1,326,407,572 | 1.0% | 73.6% |  |
| LOAD_ATTR_METHOD_NO_DICT | 1,316,760,122 | 1.0% | 74.5% | 3.4% |
| INTERPRETER_EXIT | 1,280,013,757 | 1.0% | 75.5% |  |
| FOR_ITER_LIST | 1,253,141,637 | 0.9% | 76.4% | 5.3% |
| LOAD_ATTR | 1,125,378,650 | 0.8% | 77.3% |  |
| COPY | 1,055,552,097 | 0.8% | 78.1% |  |
| STORE_ATTR_SLOT | 1,049,642,811 | 0.8% | 78.9% | 10.7% |
| LOAD_CONST__LOAD_FAST | 1,019,999,409 | 0.8% | 79.6% |  |
| CALL | 950,259,323 | 0.7% | 80.3% |  |
| CALL_NO_KW_BUILTIN_FAST | 938,651,374 | 0.7% | 81.1% | 0.0% |
| SWAP | 915,524,069 | 0.7% | 81.7% |  |
| BINARY_SUBSCR_LIST_INT | 882,484,530 | 0.7% | 82.4% | 0.4% |
| BINARY_OP_MULTIPLY_FLOAT | 827,610,801 | 0.6% | 83.0% | 0.8% |
| STORE_ATTR_INSTANCE_VALUE | 826,569,038 | 0.6% | 83.6% | 9.1% |
| BINARY_OP | 813,771,620 | 0.6% | 84.3% |  |
| LOAD_DEREF | 811,408,352 | 0.6% | 84.9% |  |
| CALL_NO_KW_ISINSTANCE | 793,824,977 | 0.6% | 85.5% |  |
| CALL_NO_KW_BUILTIN_O | 784,412,716 | 0.6% | 86.1% | 0.1% |
| PUSH_NULL | 772,018,678 | 0.6% | 86.6% |  |
| YIELD_VALUE | 769,386,816 | 0.6% | 87.2% |  |
| BUILD_TUPLE | 694,063,343 | 0.5% | 87.7% |  |
| BINARY_SUBSCR_DICT | 632,694,402 | 0.5% | 88.2% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 601,013,614 | 0.5% | 88.7% |  |
| GET_ITER | 593,542,257 | 0.4% | 89.1% |  |
| IS_OP | 530,573,080 | 0.4% | 89.5% |  |
| FOR_ITER_RANGE | 475,532,538 | 0.4% | 89.9% | 0.0% |
| BINARY_OP_SUBTRACT_INT | 469,824,476 | 0.4% | 90.2% | 0.1% |
| UNPACK_SEQUENCE_TUPLE | 441,542,260 | 0.3% | 90.5% | 0.3% |
| POP_JUMP_IF_NOT_NONE | 426,337,740 | 0.3% | 90.9% |  |
| JUMP_FORWARD | 419,724,500 | 0.3% | 91.2% |  |
| FOR_ITER_TUPLE | 417,841,700 | 0.3% | 91.5% | 15.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 391,915,395 | 0.3% | 91.8% | 1.7% |
| BINARY_OP_ADD_FLOAT | 390,241,013 | 0.3% | 92.1% | 1.6% |
| LOAD_ATTR_MODULE | 336,306,374 | 0.3% | 92.3% | 0.0% |
| LOAD_ATTR_WITH_HINT | 335,917,995 | 0.3% | 92.6% | 2.0% |
| CALL_NO_KW_TYPE_1 | 333,029,404 | 0.3% | 92.8% |  |
| CALL_NO_KW_LEN | 326,990,676 | 0.2% | 93.1% |  |
| STORE_SUBSCR | 315,798,674 | 0.2% | 93.3% |  |
| EXTENDED_ARG | 307,129,720 | 0.2% | 93.5% |  |
| STORE_SUBSCR_LIST_INT | 302,796,780 | 0.2% | 93.8% | 0.0% |
| SEND_GEN | 301,847,495 | 0.2% | 94.0% |  |
| POP_JUMP_IF_NONE | 297,327,360 | 0.2% | 94.2% |  |
| FOR_ITER | 296,931,016 | 0.2% | 94.4% |  |
| BUILD_LIST | 294,667,522 | 0.2% | 94.7% |  |
| BINARY_OP_SUBTRACT_FLOAT | 269,746,114 | 0.2% | 94.9% | 5.6% |
| BINARY_OP_MULTIPLY_INT | 265,876,859 | 0.2% | 95.1% | 3.2% |
| COPY_FREE_VARS | 254,477,817 | 0.2% | 95.3% |  |
| BINARY_SLICE | 245,070,762 | 0.2% | 95.4% |  |
| CALL_NO_KW_LIST_APPEND | 239,884,872 | 0.2% | 95.6% | 0.0% |
| RETURN_GENERATOR | 238,729,898 | 0.2% | 95.8% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 226,986,636 | 0.2% | 96.0% | 7.0% |
| BINARY_SUBSCR_TUPLE_INT | 225,263,040 | 0.2% | 96.1% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 214,263,496 | 0.2% | 96.3% |  |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 214,257,843 | 0.2% | 96.5% | 0.1% |
| STORE_SUBSCR_DICT | 198,994,723 | 0.1% | 96.6% |  |
| END_SEND | 193,874,717 | 0.1% | 96.8% |  |
| KW_NAMES | 168,115,402 | 0.1% | 96.9% |  |
| BUILD_SLICE | 158,746,079 | 0.1% | 97.0% |  |
| CALL_PY_WITH_DEFAULTS | 158,018,659 | 0.1% | 97.1% | 3.3% |
| FOR_ITER_GEN | 151,920,940 | 0.1% | 97.2% | 0.0% |
| LOAD_ATTR_METHOD_LAZY_DICT | 149,576,220 | 0.1% | 97.4% | 0.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 148,443,335 | 0.1% | 97.5% | 19.6% |
| CALL_INTRINSIC_1 | 147,722,236 | 0.1% | 97.6% |  |
| BINARY_SUBSCR_GETITEM | 146,536,843 | 0.1% | 97.7% | 0.0% |
| LIST_APPEND | 146,431,846 | 0.1% | 97.8% |  |
| UNPACK_SEQUENCE_LIST | 140,242,720 | 0.1% | 97.9% | 0.9% |
| COMPARE_OP | 136,333,778 | 0.1% | 98.0% |  |
| DELETE_SUBSCR | 126,945,957 | 0.1% | 98.1% |  |
| UNARY_NEGATIVE | 121,209,060 | 0.1% | 98.2% |  |
| CALL_BUILTIN_CLASS | 120,952,805 | 0.1% | 98.3% |  |
| LOAD_ATTR_CLASS | 120,729,912 | 0.1% | 98.4% | 1.1% |
| LOAD_SUPER_ATTR_METHOD | 117,787,110 | 0.1% | 98.5% |  |
| STORE_SLICE | 117,634,740 | 0.1% | 98.5% |  |
| FORMAT_VALUE | 114,955,560 | 0.1% | 98.6% |  |
| SEND | 112,328,358 | 0.1% | 98.7% |  |
| LOAD_CLOSURE | 109,635,212 | 0.1% | 98.8% |  |
| COMPARE_OP_FLOAT | 109,604,824 | 0.1% | 98.9% | 0.0% |
| GET_ANEXT | 100,136,760 | 0.1% | 99.0% |  |
| MAKE_FUNCTION | 93,651,654 | 0.1% | 99.0% |  |
| GET_AWAITABLE | 84,577,937 | 0.1% | 99.1% |  |
| MAKE_CELL | 83,119,549 | 0.1% | 99.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 75,141,266 | 0.1% | 99.2% | 0.0% |
| CALL_FUNCTION_EX | 74,238,180 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_UNICODE | 70,464,340 | 0.1% | 99.3% |  |
| STORE_DEREF | 65,100,740 | 0.0% | 99.4% |  |
| UNARY_NOT | 58,450,170 | 0.0% | 99.4% |  |
| BUILD_STRING | 57,707,100 | 0.0% | 99.5% |  |
| END_FOR | 57,304,960 | 0.0% | 99.5% |  |
| BUILD_MAP | 56,688,675 | 0.0% | 99.5% |  |
| STORE_ATTR | 56,104,396 | 0.0% | 99.6% |  |
| STORE_ATTR_WITH_HINT | 50,708,345 | 0.0% | 99.6% | 1.7% |
| LOAD_FAST_AND_CLEAR | 50,665,082 | 0.0% | 99.7% |  |
| LOAD_ATTR_PROPERTY | 48,846,755 | 0.0% | 99.7% | 11.1% |
| LIST_EXTEND | 47,936,048 | 0.0% | 99.7% |  |
| CALL_NO_KW_STR_1 | 47,499,404 | 0.0% | 99.8% |  |
| MAP_ADD | 40,750,380 | 0.0% | 99.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 22,744,088 | 0.0% | 99.8% | 7.7% |
| CALL_NO_KW_TUPLE_1 | 21,712,852 | 0.0% | 99.8% |  |
| PUSH_EXC_INFO | 17,146,215 | 0.0% | 99.8% |  |
| POP_EXCEPT | 17,146,215 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 16,778,415 | 0.0% | 99.9% |  |
| GET_YIELD_FROM_ITER | 15,169,260 | 0.0% | 99.9% |  |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 14,599,620 | 0.0% | 99.9% |  |
| INSTRUMENTED_RESUME | 14,583,120 | 0.0% | 99.9% |  |
| INSTRUMENTED_RETURN_VALUE | 14,576,040 | 0.0% | 99.9% |  |
| UNARY_INVERT | 12,487,197 | 0.0% | 99.9% |  |
| DICT_MERGE | 9,710,684 | 0.0% | 99.9% |  |
| LOAD_NAME | 9,003,000 | 0.0% | 99.9% |  |
| BUILD_CONST_KEY_MAP | 8,840,820 | 0.0% | 99.9% |  |
| RERAISE | 8,743,620 | 0.0% | 100.0% |  |
| DELETE_ATTR | 8,516,091 | 0.0% | 100.0% |  |
| LOAD_FAST_CHECK | 8,146,601 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 7,362,146 | 0.0% | 100.0% |  |
| STORE_GLOBAL | 6,152,400 | 0.0% | 100.0% |  |
| GET_AITER | 6,000,000 | 0.0% | 100.0% |  |
| END_ASYNC_FOR | 6,000,000 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 5,925,880 | 0.0% | 100.0% |  |
| BEFORE_WITH | 3,571,704 | 0.0% | 100.0% |  |
| RAISE_VARARGS | 3,411,420 | 0.0% | 100.0% |  |
| SET_ADD | 3,100,800 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 2,296,620 | 0.0% | 100.0% |  |
| IMPORT_FROM | 1,852,680 | 0.0% | 100.0% |  |
| IMPORT_NAME | 1,535,460 | 0.0% | 100.0% |  |
| BUILD_SET | 1,466,520 | 0.0% | 100.0% |  |
| DELETE_FAST | 376,920 | 0.0% | 100.0% |  |
| UNPACK_EX | 220,200 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 207,500 | 0.0% | 100.0% |  |
| DICT_UPDATE | 13,140 | 0.0% | 100.0% |  |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 9,990 | 0.0% | 100.0% |  |
| INSTRUMENTED_FOR_ITER | 8,430 | 0.0% | 100.0% |  |
| INSTRUMENTED_JUMP_BACKWARD | 7,410 | 0.0% | 100.0% |  |
| INSTRUMENTED_RETURN_CONST | 5,400 | 0.0% | 100.0% |  |
| STORE_NAME | 4,800 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 4,320 | 0.0% | 100.0% |  |
| LOAD_LOCALS | 2,580 | 0.0% | 100.0% |  |
| LOAD_FROM_DICT_OR_DEREF | 2,580 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 1,320 | 0.0% | 100.0% |  |
| DELETE_DEREF | 1,200 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 1,140 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,947,321,624 | 2.2% | 2.2% |
| POP_JUMP_IF_FALSE LOAD_FAST | 2,557,487,680 | 1.9% | 4.1% |
| CALL_PY_EXACT_ARGS RESUME | 2,516,821,591 | 1.9% | 6.0% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 2,317,146,380 | 1.7% | 7.8% |
| RESUME LOAD_FAST | 1,944,742,322 | 1.5% | 9.2% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,871,629,227 | 1.4% | 10.6% |
| POP_JUMP_IF_FALSE LOAD_FAST__LOAD_CONST | 1,813,612,453 | 1.4% | 12.0% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,555,861,166 | 1.2% | 13.2% |
| LOAD_FAST__LOAD_CONST BINARY_OP_ADD_INT | 1,355,583,140 | 1.0% | 14.2% |
| STORE_FAST__LOAD_FAST LOAD_CONST | 1,291,283,808 | 1.0% | 15.1% |
| POP_JUMP_IF_FALSE LOAD_FAST__LOAD_FAST | 1,284,453,899 | 1.0% | 16.1% |
| STORE_FAST__LOAD_FAST LOAD_FAST | 1,203,684,919 | 0.9% | 17.0% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 1,186,678,429 | 0.9% | 17.9% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 1,145,059,483 | 0.9% | 18.8% |
| LOAD_FAST__LOAD_FAST BINARY_SUBSCR | 1,089,244,920 | 0.8% | 19.6% |
| LOAD_FAST LOAD_GLOBAL_BUILTIN | 1,076,401,460 | 0.8% | 20.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 1,044,073,369 | 0.8% | 21.2% |
| LOAD_FAST LOAD_ATTR_SLOT | 1,042,813,730 | 0.8% | 22.0% |
| NOP LOAD_FAST__LOAD_FAST | 1,017,930,263 | 0.8% | 22.7% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_BUILTIN | 979,749,070 | 0.7% | 23.5% |
| BINARY_SUBSCR STORE_FAST__LOAD_FAST | 952,340,440 | 0.7% | 24.2% |
| JUMP_BACKWARD FOR_ITER_LIST | 935,468,512 | 0.7% | 24.9% |
| STORE_FAST JUMP_BACKWARD | 922,443,276 | 0.7% | 25.6% |
| LOAD_CONST COMPARE_OP_STR | 850,057,920 | 0.6% | 26.2% |
| RESUME LOAD_GLOBAL_BUILTIN | 834,236,004 | 0.6% | 26.8% |
| STORE_FAST__STORE_FAST STORE_FAST__STORE_FAST | 821,885,600 | 0.6% | 27.5% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 817,598,115 | 0.6% | 28.1% |
| LOAD_FAST__LOAD_FAST CONTAINS_OP | 813,486,480 | 0.6% | 28.7% |
| POP_TOP LOAD_FAST | 799,886,022 | 0.6% | 29.3% |
| LOAD_FAST__LOAD_FAST CALL_PY_EXACT_ARGS | 798,342,537 | 0.6% | 29.9% |
| BINARY_OP_ADD_INT STORE_FAST | 784,748,519 | 0.6% | 30.5% |
| LOAD_FAST RETURN_VALUE | 758,968,516 | 0.6% | 31.0% |
| BINARY_SUBSCR LOAD_FAST | 756,847,380 | 0.6% | 31.6% |
| LOAD_FAST__LOAD_CONST COMPARE_OP_STR | 719,742,620 | 0.5% | 32.1% |
| JUMP_BACKWARD NOP | 717,888,253 | 0.5% | 32.7% |
| POP_TOP JUMP_BACKWARD | 715,042,642 | 0.5% | 33.2% |
| LOAD_FAST BINARY_SUBSCR | 709,971,700 | 0.5% | 33.8% |
| CALL_NO_KW_ISINSTANCE POP_JUMP_IF_FALSE | 657,049,163 | 0.5% | 34.2% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 633,692,273 | 0.5% | 34.7% |
| LOAD_FAST__LOAD_FAST LOAD_FAST__LOAD_FAST | 629,535,781 | 0.5% | 35.2% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST__LOAD_FAST | 626,579,865 | 0.5% | 35.7% |
| LOAD_FAST CONTAINS_OP | 626,107,260 | 0.5% | 36.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 602,916,652 | 0.5% | 36.6% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 586,557,964 | 0.4% | 37.0% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST__STORE_FAST | 578,245,714 | 0.4% | 37.5% |
| LOAD_FAST POP_JUMP_IF_TRUE | 568,882,758 | 0.4% | 37.9% |
| LOAD_ATTR_INSTANCE_VALUE POP_JUMP_IF_FALSE | 555,300,052 | 0.4% | 38.3% |
| RETURN_CONST POP_TOP | 554,824,873 | 0.4% | 38.7% |
| RESUME POP_TOP | 548,746,160 | 0.4% | 39.1% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 538,229,395 | 0.4% | 39.5% |
| LOAD_DEREF LOAD_FAST | 532,653,619 | 0.4% | 39.9% |
| POP_JUMP_IF_TRUE LOAD_FAST | 528,309,669 | 0.4% | 40.3% |
| FOR_ITER_LIST STORE_FAST__LOAD_FAST | 512,389,478 | 0.4% | 40.7% |
| LOAD_FAST__LOAD_FAST LOAD_FAST | 494,604,316 | 0.4% | 41.1% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 488,519,901 | 0.4% | 41.5% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_SLOT | 475,984,531 | 0.4% | 41.8% |
| RETURN_VALUE RETURN_VALUE | 475,417,389 | 0.4% | 42.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST__LOAD_FAST | 474,949,248 | 0.4% | 42.5% |
| IS_OP POP_JUMP_IF_FALSE | 474,191,376 | 0.4% | 42.9% |
| BINARY_OP_ADD_INT STORE_FAST__LOAD_FAST | 473,850,420 | 0.4% | 43.2% |
| RETURN_CONST INTERPRETER_EXIT | 473,478,495 | 0.4% | 43.6% |
| YIELD_VALUE INTERPRETER_EXIT | 466,509,679 | 0.4% | 44.0% |
| POP_JUMP_IF_TRUE JUMP_BACKWARD | 466,069,597 | 0.3% | 44.3% |
| LOAD_FAST LOAD_ATTR | 464,604,163 | 0.3% | 44.7% |
| LOAD_CONST LOAD_CONST | 457,219,731 | 0.3% | 45.0% |
| POP_JUMP_IF_FALSE JUMP_BACKWARD | 448,361,684 | 0.3% | 45.3% |
| PUSH_NULL LOAD_FAST__LOAD_FAST | 447,601,344 | 0.3% | 45.7% |
| STORE_FAST__STORE_FAST LOAD_FAST | 442,066,777 | 0.3% | 46.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 440,640,266 | 0.3% | 46.3% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_BUILTIN_FAST | 434,565,640 | 0.3% | 46.7% |
| STORE_FAST__LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 427,921,107 | 0.3% | 47.0% |
| JUMP_BACKWARD FOR_ITER_RANGE | 423,329,376 | 0.3% | 47.3% |
| LOAD_CONST BINARY_OP_ADD_INT | 416,657,430 | 0.3% | 47.6% |
| STORE_FAST LOAD_GLOBAL_MODULE | 413,625,696 | 0.3% | 47.9% |
| BUILD_TUPLE RETURN_VALUE | 405,105,780 | 0.3% | 48.2% |
| STORE_FAST__LOAD_FAST POP_JUMP_IF_FALSE | 397,872,436 | 0.3% | 48.5% |
| LOAD_FAST__LOAD_FAST LOAD_CONST | 394,864,662 | 0.3% | 48.8% |
| UNPACK_SEQUENCE_TUPLE STORE_FAST__STORE_FAST | 389,713,420 | 0.3% | 49.1% |
| LOAD_FAST CALL_NO_KW_BUILTIN_O | 381,563,556 | 0.3% | 49.4% |
| CALL_NO_KW_BUILTIN_FAST POP_JUMP_IF_FALSE | 372,092,104 | 0.3% | 49.7% |
| LOAD_CONST COMPARE_OP_INT | 364,236,980 | 0.3% | 49.9% |
| LOAD_FAST BINARY_OP_MULTIPLY_FLOAT | 357,623,400 | 0.3% | 50.2% |
| RETURN_VALUE STORE_FAST__LOAD_FAST | 347,654,847 | 0.3% | 50.5% |
| CALL_NO_KW_BUILTIN_O POP_TOP | 347,469,156 | 0.3% | 50.7% |
| LOAD_GLOBAL_MODULE CALL_NO_KW_ISINSTANCE | 341,465,256 | 0.3% | 51.0% |
| STORE_FAST__LOAD_FAST LOAD_GLOBAL_MODULE | 336,844,863 | 0.3% | 51.2% |
| RESUME NOP | 334,041,382 | 0.3% | 51.5% |
| LOAD_FAST CALL_NO_KW_TYPE_1 | 329,394,064 | 0.2% | 51.7% |
| RESUME LOAD_GLOBAL_MODULE | 327,521,958 | 0.2% | 52.0% |
| LOAD_GLOBAL_BUILTIN CALL_NO_KW_ISINSTANCE | 321,584,301 | 0.2% | 52.2% |
| RETURN_VALUE INTERPRETER_EXIT | 321,573,963 | 0.2% | 52.5% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 319,828,883 | 0.2% | 52.7% |
| STORE_FAST__LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 318,226,374 | 0.2% | 53.0% |
| LOAD_FAST__LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 316,804,571 | 0.2% | 53.2% |
| FOR_ITER_LIST UNPACK_SEQUENCE_TWO_TUPLE | 314,360,080 | 0.2% | 53.4% |
| LOAD_FAST BINARY_SUBSCR_LIST_INT | 312,794,592 | 0.2% | 53.7% |
| LOAD_ATTR_SLOT LOAD_FAST | 308,219,719 | 0.2% | 53.9% |
| LOAD_GLOBAL_MODULE CONTAINS_OP | 305,981,940 | 0.2% | 54.1% |
| LOAD_CONST STORE_FAST | 302,145,471 | 0.2% | 54.4% |
| LOAD_FAST POP_JUMP_IF_FALSE | 298,338,182 | 0.2% | 54.6% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BEFORE_ASYNC_WITH

<details>
<summary> Successors and predecessors for BEFORE_ASYNC_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 120 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 120 | 100.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,952,480 | 54.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,030,740 | 28.9% |
| CALL | 479,935 | 13.4% |
| LOAD_GLOBAL_MODULE | 70,929 | 2.0% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 36,900 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,972,449 | 83.2% |
| STORE_FAST__LOAD_FAST | 521,515 | 14.6% |
| STORE_FAST | 76,300 | 2.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.0% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,857,206 | 25.4% |
| LOAD_FAST | 114,298,869 | 14.0% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 72,002,140 | 8.8% |
| LOAD_FAST__LOAD_FAST | 61,323,760 | 7.5% |
| LOAD_ATTR_INSTANCE_VALUE | 44,172,300 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 125,640,860 | 15.4% |
| LOAD_FAST__LOAD_FAST | 106,844,401 | 13.1% |
| STORE_FAST__LOAD_FAST | 100,417,241 | 12.3% |
| RETURN_VALUE | 69,476,700 | 8.5% |
| LOAD_CONST | 68,594,340 | 8.4% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 284,043,300 | 72.8% |
| LOAD_FAST | 65,131,169 | 16.7% |
| RETURN_VALUE | 17,287,200 | 4.4% |
| BINARY_OP_MULTIPLY_INT | 8,437,640 | 2.2% |
| BINARY_OP | 6,097,100 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 116,255,040 | 29.8% |
| STORE_FAST | 90,508,449 | 23.2% |
| LOAD_FAST | 45,573,500 | 11.7% |
| LOAD_FAST__LOAD_FAST | 41,370,060 | 10.6% |
| RETURN_VALUE | 31,350,960 | 8.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 1,355,583,140 | 61.4% |
| LOAD_CONST | 416,657,430 | 18.9% |
| LOAD_FAST | 281,189,040 | 12.7% |
| LOAD_FAST__LOAD_FAST | 47,335,560 | 2.1% |
| END_SEND | 29,134,080 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 784,748,519 | 35.6% |
| STORE_FAST__LOAD_FAST | 473,850,420 | 21.5% |
| LOAD_CONST | 132,089,160 | 6.0% |
| STORE_SLICE | 103,909,260 | 4.7% |
| BINARY_OP_MULTIPLY_INT | 96,055,140 | 4.4% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,181,240 | 47.1% |
| BINARY_SLICE | 15,579,000 | 22.1% |
| LOAD_CONST | 12,144,620 | 17.2% |
| LOAD_ATTR | 2,105,320 | 3.0% |
| BUILD_STRING | 2,011,200 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 15,909,600 | 22.6% |
| BUILD_TUPLE | 15,457,800 | 21.9% |
| LOAD_FAST | 15,453,180 | 21.9% |
| LOAD_CONST | 8,803,740 | 12.5% |
| RETURN_VALUE | 3,047,100 | 4.3% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 2,305,260 | 38.9% |
| BINARY_SLICE | 1,580,580 | 26.7% |
| RETURN_VALUE | 680,220 | 11.5% |
| BINARY_OP_ADD_UNICODE | 365,140 | 6.2% |
| LOAD_ATTR_SLOT | 358,800 | 6.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,515,160 | 59.3% |
| PUSH_NULL | 1,580,580 | 26.7% |
| JUMP_BACKWARD | 511,600 | 8.6% |
| LOAD_FAST__LOAD_CONST | 216,660 | 3.7% |
| LOAD_CONST__LOAD_FAST | 60,360 | 1.0% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 357,623,400 | 43.2% |
| LOAD_FAST__LOAD_FAST | 240,558,420 | 29.1% |
| LOAD_ATTR_INSTANCE_VALUE | 118,763,280 | 14.4% |
| BINARY_SUBSCR | 67,701,000 | 8.2% |
| CALL_BUILTIN_CLASS | 12,782,880 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_FLOAT | 284,043,300 | 34.3% |
| YIELD_VALUE | 210,931,680 | 25.5% |
| BINARY_OP_SUBTRACT_FLOAT | 109,285,680 | 13.2% |
| LOAD_FAST__LOAD_FAST | 96,886,480 | 11.7% |
| LOAD_FAST | 50,101,980 | 6.1% |


</details>

### BINARY_OP_MULTIPLY_INT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 96,055,140 | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE | 51,230,999 | 19.3% |
| LOAD_FAST__LOAD_FAST | 41,778,900 | 15.7% |
| BINARY_OP | 27,332,740 | 10.3% |
| LOAD_FAST | 27,011,320 | 10.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,941,460 | 22.9% |
| LOAD_FAST | 46,425,420 | 17.5% |
| STORE_FAST | 31,320,480 | 11.8% |
| STORE_FAST__LOAD_FAST | 30,843,240 | 11.6% |
| LOAD_FAST__LOAD_FAST | 28,244,880 | 10.6% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 109,285,680 | 40.5% |
| LOAD_FAST | 99,719,460 | 37.0% |
| LOAD_ATTR_INSTANCE_VALUE | 28,661,940 | 10.6% |
| BINARY_SUBSCR | 12,729,580 | 4.7% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 96,381,133 | 35.7% |
| LOAD_FAST__LOAD_FAST | 73,322,880 | 27.2% |
| SWAP | 55,701,000 | 20.6% |
| LOAD_FAST | 28,349,160 | 10.5% |
| BINARY_OP_SUBTRACT_FLOAT | 10,737,420 | 4.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 206,147,229 | 43.9% |
| LOAD_FAST__LOAD_CONST | 153,629,287 | 32.7% |
| LOAD_FAST | 76,556,360 | 16.3% |
| LOAD_FAST__LOAD_FAST | 20,373,740 | 4.3% |
| LOAD_ATTR_INSTANCE_VALUE | 10,026,960 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 93,675,400 | 19.9% |
| STORE_FAST__LOAD_FAST | 72,774,880 | 15.5% |
| SWAP | 68,461,849 | 14.6% |
| RETURN_VALUE | 39,931,800 | 8.5% |
| BINARY_OP | 37,165,200 | 7.9% |


</details>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 134,070,662 | 54.7% |
| LOAD_FAST | 47,193,120 | 19.3% |
| BINARY_OP_ADD_INT | 35,917,200 | 14.7% |
| LOAD_FAST__LOAD_FAST | 17,152,380 | 7.0% |
| LOAD_FAST__LOAD_CONST | 3,470,621 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 35,336,681 | 14.4% |
| GET_ITER | 33,474,160 | 13.7% |
| CALL_PY_EXACT_ARGS | 25,418,520 | 10.4% |
| BUILD_TUPLE | 24,334,800 | 9.9% |
| CALL_NO_KW_LIST_APPEND | 19,300,860 | 7.9% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 1,089,244,920 | 46.3% |
| LOAD_FAST | 709,971,700 | 30.2% |
| COPY | 109,564,100 | 4.7% |
| BUILD_SLICE | 105,404,820 | 4.5% |
| BINARY_OP_ADD_INT | 89,539,860 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 952,340,440 | 40.5% |
| LOAD_FAST | 756,847,380 | 32.2% |
| LOAD_FAST__LOAD_FAST | 128,268,480 | 5.5% |
| LOAD_FAST__LOAD_CONST | 103,941,420 | 4.4% |
| BINARY_OP_MULTIPLY_FLOAT | 67,701,000 | 2.9% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 203,511,975 | 32.2% |
| LOAD_FAST__LOAD_CONST | 167,857,560 | 26.5% |
| LOAD_FAST__LOAD_FAST | 135,815,580 | 21.5% |
| LOAD_CONST | 49,956,520 | 7.9% |
| BINARY_SUBSCR | 41,253,440 | 6.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 153,894,000 | 24.3% |
| RETURN_VALUE | 104,620,047 | 16.5% |
| STORE_FAST | 81,785,783 | 12.9% |
| CONTAINS_OP | 77,768,700 | 12.3% |
| LOAD_FAST | 51,610,080 | 8.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 48,461,723 | 33.1% |
| LOAD_FAST__LOAD_CONST | 37,507,300 | 25.6% |
| BUILD_TUPLE | 28,812,000 | 19.7% |
| LOAD_FAST | 23,107,380 | 15.8% |
| LOAD_CONST | 4,109,720 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 145,826,783 | 99.5% |
| MAKE_CELL | 705,600 | 0.5% |
| LOAD_ATTR_METHOD_NO_DICT | 2,280 | 0.0% |
| CONTAINS_OP | 1,020 | 0.0% |
| LOAD_FAST | 300 | 0.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 312,794,592 | 35.4% |
| COPY | 158,091,420 | 17.9% |
| LOAD_CONST | 146,295,002 | 16.6% |
| LOAD_FAST__LOAD_FAST | 114,424,500 | 13.0% |
| BINARY_OP | 48,349,920 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 228,009,446 | 25.9% |
| LOAD_CONST | 192,238,860 | 21.8% |
| LOAD_FAST__LOAD_FAST | 97,672,380 | 11.1% |
| RETURN_VALUE | 90,398,160 | 10.3% |
| LOAD_FAST | 48,968,460 | 5.6% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 132,906,820 | 59.0% |
| LOAD_CONST | 52,549,460 | 23.3% |
| LOAD_FAST | 39,803,100 | 17.7% |
| LOAD_FAST__LOAD_FAST | 3,360 | 0.0% |
| BINARY_SUBSCR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 72,116,700 | 32.0% |
| LOAD_GLOBAL_MODULE | 30,051,520 | 13.3% |
| LOAD_CONST | 24,656,740 | 10.9% |
| LOAD_FAST | 21,756,420 | 9.7% |
| YIELD_VALUE | 19,353,600 | 8.6% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 8,812,200 | 99.7% |
| LOAD_FAST__LOAD_CONST | 28,620 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 3,960,720 | 44.8% |
| LOAD_FAST | 2,494,260 | 28.2% |
| LOAD_FAST__LOAD_FAST | 1,704,180 | 19.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 383,280 | 4.3% |
| STORE_FAST__LOAD_FAST | 145,020 | 1.6% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 116,313,744 | 39.5% |
| LOAD_ATTR_SLOT | 37,318,956 | 12.7% |
| SWAP | 32,071,936 | 10.9% |
| LOAD_FAST | 22,856,949 | 7.8% |
| RESUME | 17,319,160 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 95,111,276 | 32.3% |
| LOAD_FAST | 81,558,211 | 27.7% |
| STORE_FAST | 33,890,959 | 11.5% |
| SWAP | 32,071,996 | 10.9% |
| CALL | 9,672,740 | 3.3% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,709,780 | 15.4% |
| RESUME | 6,668,967 | 11.8% |
| LOAD_FAST | 6,044,580 | 10.7% |
| SWAP | 5,489,820 | 9.7% |
| POP_JUMP_IF_FALSE | 3,888,600 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,891,639 | 29.8% |
| STORE_FAST__LOAD_FAST | 10,325,764 | 18.2% |
| STORE_FAST | 10,307,172 | 18.2% |
| SWAP | 5,489,820 | 9.7% |
| CALL_NO_KW_BUILTIN_FAST | 4,322,400 | 7.6% |


</details>

### BUILD_SET

<details>
<summary> Successors and predecessors for BUILD_SET </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| LOAD_CONST | 82,320 | 5.6% |
| LOAD_FAST | 45,000 | 3.1% |
| LOAD_GLOBAL_MODULE | 9,960 | 0.7% |
| STORE_FAST__LOAD_FAST | 7,920 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 1,320,360 | 90.0% |
| STORE_FAST__LOAD_FAST | 48,240 | 3.3% |
| LOAD_GLOBAL_BUILTIN | 36,600 | 2.5% |
| CALL_PY_EXACT_ARGS | 34,080 | 2.3% |
| CONTAINS_OP | 9,600 | 0.7% |


</details>

### BUILD_SLICE

<details>
<summary> Successors and predecessors for BUILD_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 157,946,460 | 99.5% |
| LOAD_CONST__LOAD_FAST | 674,279 | 0.4% |
| LOAD_FAST | 69,840 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 54,000 | 0.0% |
| BINARY_OP_ADD_INT | 1,440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 105,404,820 | 66.4% |
| DELETE_SUBSCR | 53,341,259 | 33.6% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FORMAT_VALUE | 51,003,840 | 88.4% |
| LOAD_CONST | 6,703,260 | 11.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 36,694,920 | 63.6% |
| CALL | 12,295,080 | 21.3% |
| STORE_FAST | 2,922,000 | 5.1% |
| BINARY_OP_ADD_UNICODE | 2,011,200 | 3.5% |
| CALL_NO_KW_LIST_APPEND | 1,398,120 | 2.4% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 166,753,343 | 24.0% |
| LOAD_FAST__LOAD_FAST | 142,571,041 | 20.5% |
| LOAD_FAST | 125,455,519 | 18.1% |
| LOAD_CLOSURE | 79,461,910 | 11.4% |
| CALL | 37,729,440 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 405,105,780 | 58.4% |
| LOAD_CONST | 81,806,814 | 11.8% |
| CALL_NO_KW_ISINSTANCE | 33,213,880 | 4.8% |
| YIELD_VALUE | 32,187,900 | 4.6% |
| BINARY_SUBSCR_GETITEM | 28,812,000 | 4.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 232,644,107 | 24.5% |
| KW_NAMES | 144,773,282 | 15.2% |
| LOAD_FAST__LOAD_FAST | 100,432,388 | 10.6% |
| BINARY_SUBSCR_TUPLE_INT | 72,116,700 | 7.6% |
| LOAD_GLOBAL_MODULE | 55,745,403 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 289,429,021 | 30.5% |
| RESUME | 204,746,743 | 21.5% |
| RETURN_VALUE | 88,868,648 | 9.4% |
| POP_TOP | 48,211,558 | 5.1% |
| LOAD_GLOBAL_MODULE | 38,965,225 | 4.1% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 45,032,304 | 30.3% |
| BINARY_OP_MULTIPLY_INT | 22,513,860 | 15.2% |
| LOAD_FAST__LOAD_FAST | 21,602,073 | 14.6% |
| LOAD_CONST | 16,681,480 | 11.2% |
| LOAD_FAST__LOAD_CONST | 11,520,180 | 7.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 118,814,255 | 80.0% |
| COPY_FREE_VARS | 26,846,320 | 18.1% |
| POP_TOP | 2,060,540 | 1.4% |
| CALL_PY_EXACT_ARGS | 509,200 | 0.3% |
| MAKE_CELL | 172,340 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,350,156 | 27.6% |
| CALL_NO_KW_LEN | 23,237,786 | 19.2% |
| LOAD_GLOBAL_BUILTIN | 9,122,220 | 7.5% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 8,231,400 | 6.8% |
| BINARY_OP_MULTIPLY_INT | 6,174,460 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 62,070,562 | 51.3% |
| BINARY_OP_MULTIPLY_FLOAT | 12,782,880 | 10.6% |
| STORE_FAST__LOAD_FAST | 9,531,140 | 7.9% |
| LOAD_FAST | 9,141,900 | 7.6% |
| CALL_BUILTIN_CLASS | 4,158,646 | 3.4% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 33,017,040 | 43.9% |
| KW_NAMES | 22,170,640 | 29.5% |
| LOAD_FAST | 14,014,220 | 18.7% |
| LOAD_FAST__LOAD_FAST | 2,692,180 | 3.6% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 2,011,320 | 2.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_DEREF | 31,295,640 | 41.6% |
| STORE_FAST | 23,989,100 | 31.9% |
| POP_TOP | 8,764,363 | 11.7% |
| RETURN_VALUE | 6,223,363 | 8.3% |
| STORE_FAST__LOAD_FAST | 3,855,720 | 5.1% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 41,804,196 | 56.3% |
| LOAD_FAST | 9,799,260 | 13.2% |
| DICT_MERGE | 9,710,684 | 13.1% |
| LOAD_FAST__LOAD_FAST | 5,883,880 | 7.9% |
| BUILD_MAP | 3,354,540 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 44,979,316 | 60.6% |
| STORE_FAST__LOAD_FAST | 8,009,940 | 10.8% |
| RETURN_VALUE | 6,075,860 | 8.2% |
| MAKE_CELL | 4,707,040 | 6.3% |
| LOAD_FAST__LOAD_FAST | 3,815,580 | 5.1% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 88,136,760 | 62.3% |
| LIST_EXTEND | 47,196,796 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 6,000,000 | 4.2% |
| RERAISE | 41,160 | 0.0% |
| LIST_APPEND | 11,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 94,136,760 | 63.7% |
| CALL_FUNCTION_EX | 41,804,196 | 28.3% |
| RERAISE | 6,377,160 | 4.3% |
| LOAD_CONST__LOAD_FAST | 3,322,320 | 2.2% |
| BUILD_MAP | 2,008,780 | 1.4% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,918,804 | 39.2% |
| LOAD_CONST | 8,592,000 | 37.8% |
| LOAD_ATTR_METHOD_NO_DICT | 4,064,780 | 17.9% |
| LOAD_FAST__LOAD_FAST | 740,544 | 3.3% |
| LOAD_ATTR | 258,800 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 6,935,320 | 30.5% |
| STORE_FAST | 4,123,720 | 18.1% |
| STORE_FAST__LOAD_FAST | 2,930,244 | 12.9% |
| LOAD_ATTR_METHOD_NO_DICT | 2,436,040 | 10.7% |
| BINARY_OP | 2,010,960 | 8.8% |


</details>

### CALL_NO_KW_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 434,565,640 | 46.3% |
| LOAD_CONST | 275,347,180 | 29.3% |
| LOAD_FAST__LOAD_FAST | 72,111,140 | 7.7% |
| LOAD_FAST__LOAD_CONST | 63,672,604 | 6.8% |
| CALL_NO_KW_BUILTIN_FAST | 37,470,460 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 372,092,104 | 39.6% |
| STORE_FAST | 216,765,260 | 23.1% |
| STORE_FAST__LOAD_FAST | 100,059,180 | 10.7% |
| EXTENDED_ARG | 72,007,560 | 7.7% |
| POP_TOP | 47,616,945 | 5.1% |


</details>

### CALL_NO_KW_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 381,563,556 | 48.6% |
| LOAD_FAST__LOAD_FAST | 178,489,700 | 22.8% |
| LOAD_FAST__LOAD_CONST | 55,886,880 | 7.1% |
| RETURN_VALUE | 54,114,240 | 6.9% |
| BUILD_STRING | 36,694,920 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 347,469,156 | 44.3% |
| LOAD_CONST | 171,752,301 | 21.9% |
| STORE_FAST__LOAD_FAST | 157,752,200 | 20.1% |
| RETURN_VALUE | 29,118,978 | 3.7% |
| STORE_SUBSCR_DICT | 13,999,740 | 1.8% |


</details>

### CALL_NO_KW_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_NO_KW_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 341,465,256 | 43.0% |
| LOAD_GLOBAL_BUILTIN | 321,584,301 | 40.5% |
| LOAD_FAST__LOAD_FAST | 61,327,020 | 7.7% |
| BUILD_TUPLE | 33,213,880 | 4.2% |
| LOAD_ATTR_MODULE | 25,487,500 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 657,049,163 | 82.8% |
| POP_JUMP_IF_TRUE | 108,850,176 | 13.7% |
| UNARY_NOT | 7,956,060 | 1.0% |
| EXTENDED_ARG | 7,144,560 | 0.9% |
| COPY | 5,946,000 | 0.7% |


</details>

### CALL_NO_KW_LEN

<details>
<summary> Successors and predecessors for CALL_NO_KW_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 206,829,137 | 63.3% |
| LOAD_ATTR_INSTANCE_VALUE | 44,234,359 | 13.5% |
| BINARY_SUBSCR_LIST_INT | 29,548,500 | 9.0% |
| LOAD_DEREF | 20,446,300 | 6.3% |
| LOAD_ATTR_SLOT | 8,337,460 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 128,781,531 | 39.4% |
| LOAD_FAST | 43,777,140 | 13.4% |
| STORE_FAST__LOAD_FAST | 35,180,550 | 10.8% |
| COMPARE_OP_INT | 32,851,380 | 10.0% |
| CALL_BUILTIN_CLASS | 23,237,786 | 7.1% |


</details>

### CALL_NO_KW_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_NO_KW_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,776,152 | 72.9% |
| BINARY_SUBSCR | 20,171,040 | 8.4% |
| BINARY_SLICE | 19,300,860 | 8.0% |
| BINARY_OP | 5,898,280 | 2.5% |
| RETURN_VALUE | 4,584,000 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 89,867,136 | 37.5% |
| LOAD_FAST__LOAD_FAST | 30,762,780 | 12.8% |
| EXTENDED_ARG | 27,732,240 | 11.6% |
| LOAD_FAST | 26,792,300 | 11.2% |
| RETURN_CONST | 20,554,500 | 8.6% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 174,794,230 | 44.6% |
| LOAD_CONST | 79,114,520 | 20.2% |
| LOAD_FAST__LOAD_FAST | 56,611,080 | 14.4% |
| LOAD_ATTR_METHOD_NO_DICT | 51,377,740 | 13.1% |
| LOAD_ATTR_SLOT | 8,646,000 | 2.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 260,546,408 | 66.5% |
| STORE_FAST | 40,252,480 | 10.3% |
| LIST_APPEND | 28,850,040 | 7.4% |
| RETURN_VALUE | 11,999,652 | 3.1% |
| LOAD_FAST | 10,616,580 | 2.7% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 145,745,602 | 64.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 65,649,671 | 28.9% |
| LOAD_ATTR | 13,710,660 | 6.0% |
| LOAD_FAST__LOAD_FAST | 1,557,480 | 0.7% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 301,163 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 58,433,424 | 25.7% |
| STORE_FAST__LOAD_FAST | 51,918,516 | 22.9% |
| GET_ITER | 32,049,780 | 14.1% |
| STORE_FAST | 20,026,202 | 8.8% |
| LOAD_GLOBAL_MODULE | 18,632,220 | 8.2% |


</details>

### CALL_NO_KW_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_NO_KW_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 168,293,868 | 78.5% |
| CALL | 19,487,669 | 9.1% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 6,935,320 | 3.2% |
| LOAD_GLOBAL_MODULE | 6,146,340 | 2.9% |
| LOAD_ATTR | 3,038,920 | 1.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 102,637,603 | 47.9% |
| BINARY_OP | 72,002,140 | 33.6% |
| RETURN_VALUE | 17,286,060 | 8.1% |
| STORE_FAST | 6,522,780 | 3.0% |
| LOAD_FAST | 5,318,760 | 2.5% |


</details>

### CALL_NO_KW_STR_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 42,063,084 | 88.6% |
| LOAD_FAST__LOAD_FAST | 2,400,000 | 5.1% |
| RETURN_VALUE | 1,727,580 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,228,800 | 2.6% |
| BINARY_SUBSCR_TUPLE_INT | 30,420 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_O | 12,689,460 | 26.7% |
| CALL_PY_EXACT_ARGS | 11,586,240 | 24.4% |
| YIELD_VALUE | 7,682,400 | 16.2% |
| STORE_FAST__LOAD_FAST | 5,588,100 | 11.8% |
| RETURN_VALUE | 3,244,980 | 6.8% |


</details>

### CALL_NO_KW_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,492,040 | 66.7% |
| RETURN_GENERATOR | 5,394,160 | 24.8% |
| LOAD_ATTR_SLOT | 1,098,672 | 5.1% |
| CALL | 436,520 | 2.0% |
| RETURN_VALUE | 180,060 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,283,720 | 65.8% |
| BUILD_TUPLE | 2,892,012 | 13.3% |
| YIELD_VALUE | 2,419,200 | 11.1% |
| LOAD_GLOBAL_BUILTIN | 572,040 | 2.6% |
| STORE_FAST__LOAD_FAST | 476,580 | 2.2% |


</details>

### CALL_NO_KW_TYPE_1

<details>
<summary> Successors and predecessors for CALL_NO_KW_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 329,394,064 | 98.9% |
| LOAD_CONST | 3,615,920 | 1.1% |
| LOAD_GLOBAL_BUILTIN | 19,240 | 0.0% |
| CALL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 239,978,100 | 72.1% |
| STORE_FAST | 45,877,512 | 13.8% |
| LOAD_GLOBAL_MODULE | 13,598,440 | 4.1% |
| LOAD_GLOBAL_BUILTIN | 13,352,980 | 4.0% |
| LOAD_FAST | 9,080,880 | 2.7% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 817,598,115 | 29.0% |
| LOAD_FAST__LOAD_FAST | 798,342,537 | 28.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 440,640,266 | 15.6% |
| LOAD_GLOBAL_MODULE | 163,989,171 | 5.8% |
| LOAD_ATTR_METHOD_NO_DICT | 109,897,169 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 2,516,821,591 | 89.2% |
| RETURN_GENERATOR | 140,526,618 | 5.0% |
| COPY_FREE_VARS | 124,046,918 | 4.4% |
| MAKE_CELL | 24,892,307 | 0.9% |
| INSTRUMENTED_RESUME | 14,577,840 | 0.5% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 90,549,132 | 57.3% |
| LOAD_ATTR_METHOD_NO_DICT | 12,061,760 | 7.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 11,866,394 | 7.5% |
| LOAD_ATTR | 11,184,280 | 7.1% |
| LOAD_SUPER_ATTR_METHOD | 5,951,040 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 148,589,244 | 94.0% |
| COPY_FREE_VARS | 5,010,555 | 3.2% |
| RETURN_GENERATOR | 3,297,780 | 2.1% |
| MAKE_CELL | 1,008,240 | 0.6% |
| CALL_PY_EXACT_ARGS | 87,660 | 0.1% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,697,815 | 93.6% |
| LOAD_GLOBAL_MODULE | 689,760 | 4.1% |
| BUILD_TUPLE | 356,040 | 2.1% |
| LOAD_ATTR_MODULE | 34,800 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 16,778,415 | 100.0% |


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
| LOAD_FAST | 43,289,060 | 31.8% |
| LOAD_CONST | 36,763,057 | 27.0% |
| LOAD_ATTR | 15,173,603 | 11.1% |
| LOAD_ATTR_SLOT | 13,691,375 | 10.0% |
| LOAD_GLOBAL_MODULE | 9,379,215 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 70,255,405 | 51.5% |
| POP_JUMP_IF_TRUE | 39,256,702 | 28.8% |
| COPY | 18,630,150 | 13.7% |
| RETURN_VALUE | 7,090,277 | 5.2% |
| EXTENDED_ARG | 756,720 | 0.6% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 65,981,765 | 60.2% |
| BINARY_SUBSCR | 23,382,660 | 21.3% |
| LOAD_FAST | 6,297,754 | 5.7% |
| LOAD_CONST | 6,004,560 | 5.5% |
| LOAD_GLOBAL_MODULE | 3,631,965 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 47,981,945 | 43.8% |
| POP_JUMP_IF_TRUE | 32,445,300 | 29.6% |
| POP_JUMP_IF_FALSE | 29,177,219 | 26.6% |
| COMPARE_OP | 360 | 0.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 364,236,980 | 25.7% |
| LOAD_FAST__LOAD_CONST | 253,258,394 | 17.9% |
| LOAD_FAST | 180,401,102 | 12.7% |
| LOAD_ATTR_INSTANCE_VALUE | 179,281,601 | 12.6% |
| COPY | 102,795,720 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,186,678,429 | 83.7% |
| POP_JUMP_IF_TRUE | 122,880,400 | 8.7% |
| RETURN_VALUE | 59,342,660 | 4.2% |
| EXTENDED_ARG | 16,761,780 | 1.2% |
| LOAD_FAST | 15,024,000 | 1.1% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 850,057,920 | 53.2% |
| LOAD_FAST__LOAD_CONST | 719,742,620 | 45.1% |
| LOAD_FAST | 8,704,060 | 0.5% |
| LOAD_GLOBAL_MODULE | 4,786,793 | 0.3% |
| RETURN_VALUE | 4,052,040 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,555,861,166 | 97.4% |
| POP_JUMP_IF_TRUE | 28,164,322 | 1.8% |
| COPY | 6,113,640 | 0.4% |
| RETURN_VALUE | 4,337,365 | 0.3% |
| EXTENDED_ARG | 1,149,540 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 813,486,480 | 40.9% |
| LOAD_FAST | 626,107,260 | 31.5% |
| LOAD_GLOBAL_MODULE | 305,981,940 | 15.4% |
| BINARY_SUBSCR_DICT | 77,768,700 | 3.9% |
| LOAD_CONST__LOAD_FAST | 66,105,960 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,871,629,227 | 94.1% |
| POP_JUMP_IF_TRUE | 66,004,740 | 3.3% |
| RETURN_VALUE | 25,010,040 | 1.3% |
| COPY | 20,881,380 | 1.0% |
| EXTENDED_ARG | 3,501,480 | 0.2% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 269,175,600 | 25.5% |
| LOAD_FAST | 236,064,629 | 22.4% |
| SWAP | 105,750,660 | 10.0% |
| LOAD_FAST__LOAD_FAST | 88,896,900 | 8.4% |
| LOAD_FAST__LOAD_CONST | 78,333,300 | 7.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 269,175,600 | 25.5% |
| POP_JUMP_IF_FALSE | 177,515,764 | 16.8% |
| BINARY_SUBSCR_LIST_INT | 158,091,420 | 15.0% |
| BINARY_SUBSCR | 109,564,100 | 10.4% |
| COMPARE_OP_INT | 102,795,720 | 9.7% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 124,046,918 | 75.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 26,846,320 | 16.3% |
| CALL | 8,744,923 | 5.3% |
| CALL_PY_WITH_DEFAULTS | 5,010,555 | 3.0% |
| LOAD_ATTR_PROPERTY | 157,200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 181,061,097 | 71.2% |
| RETURN_GENERATOR | 73,398,240 | 28.8% |
| MAKE_CELL | 18,480 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,516,031 | 100.0% |
| LOAD_DEREF | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,651,034 | 78.1% |
| NOP | 1,713,800 | 20.1% |
| RETURN_CONST | 150,237 | 1.8% |
| LOAD_GLOBAL_MODULE | 960 | 0.0% |
| LOAD_CONST | 60 | 0.0% |


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
| STORE_FAST | 222,720 | 59.1% |
| CALL | 81,000 | 21.5% |
| STORE_ATTR_INSTANCE_VALUE | 18,000 | 4.8% |
| POP_EXCEPT | 18,000 | 4.8% |
| NOP | 18,000 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RERAISE | 151,020 | 40.1% |
| RETURN_VALUE | 138,600 | 36.8% |
| RETURN_CONST | 36,000 | 9.6% |
| LOAD_FAST | 18,000 | 4.8% |
| JUMP_BACKWARD | 9,540 | 2.5% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 72,991,500 | 57.5% |
| BUILD_SLICE | 53,341,259 | 42.0% |
| LOAD_FAST | 296,221 | 0.2% |
| LOAD_FAST__LOAD_CONST | 277,500 | 0.2% |
| CALL | 20,637 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 54,070,500 | 42.6% |
| LOAD_FAST | 26,987,159 | 21.3% |
| LOAD_FAST__LOAD_FAST | 26,382,660 | 20.8% |
| LOAD_CONST | 18,042,361 | 14.2% |
| JUMP_BACKWARD | 1,038,960 | 0.8% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,390,180 | 96.7% |
| LOAD_ATTR_INSTANCE_VALUE | 152,044 | 1.6% |
| LOAD_DEREF | 75,760 | 0.8% |
| RETURN_VALUE | 50,880 | 0.5% |
| BUILD_CONST_KEY_MAP | 16,320 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 9,710,684 | 100.0% |


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
| RETURN_CONST | 57,304,960 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 37,036,200 | 64.6% |
| LOAD_FAST | 19,367,740 | 33.8% |
| RETURN_CONST | 791,580 | 1.4% |
| LOAD_FAST__LOAD_FAST | 93,840 | 0.2% |
| LOAD_CONST__LOAD_FAST | 5,280 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SEND | 100,299,239 | 51.7% |
| RETURN_VALUE | 68,993,659 | 35.6% |
| RETURN_CONST | 24,581,819 | 12.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 88,752,959 | 45.8% |
| POP_TOP | 36,145,258 | 18.6% |
| LOAD_GLOBAL_MODULE | 29,134,080 | 15.0% |
| BINARY_OP_ADD_INT | 29,134,080 | 15.0% |
| STORE_FAST | 6,081,240 | 3.1% |


</details>

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_BUILTIN_FAST | 72,007,560 | 23.4% |
| JUMP_BACKWARD | 64,331,400 | 20.9% |
| LOAD_FAST | 34,855,540 | 11.3% |
| CALL_NO_KW_LIST_APPEND | 27,732,240 | 9.0% |
| POP_TOP | 21,902,700 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 105,432,600 | 34.3% |
| JUMP_BACKWARD | 65,757,060 | 21.4% |
| FOR_ITER_LIST | 37,528,100 | 12.2% |
| POP_JUMP_IF_NONE | 37,462,780 | 12.2% |
| FOR_ITER_GEN | 26,083,460 | 8.5% |


</details>

### FORMAT_VALUE

<details>
<summary> Successors and predecessors for FORMAT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 50,938,800 | 44.3% |
| LOAD_FAST__LOAD_FAST | 36,024,720 | 31.3% |
| LOAD_ATTR | 13,009,680 | 11.3% |
| LOAD_FAST | 5,719,740 | 5.0% |
| RETURN_VALUE | 2,459,160 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 51,370,620 | 44.7% |
| BUILD_STRING | 51,003,840 | 44.4% |
| LOAD_CONST | 6,727,260 | 5.9% |
| LOAD_FAST | 5,845,020 | 5.1% |
| LOAD_GLOBAL_MODULE | 8,820 | 0.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 216,854,849 | 73.0% |
| GET_ITER | 55,096,789 | 18.6% |
| EXTENDED_ARG | 16,060,220 | 5.4% |
| SWAP | 5,814,604 | 2.0% |
| LOAD_FAST | 3,009,260 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 148,151,760 | 49.9% |
| STORE_FAST__LOAD_FAST | 62,705,284 | 21.1% |
| STORE_FAST | 24,033,812 | 8.1% |
| LOAD_FAST | 17,863,650 | 6.0% |
| RETURN_CONST | 14,766,113 | 5.0% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 68,838,540 | 45.3% |
| GET_ITER | 56,956,440 | 37.5% |
| EXTENDED_ARG | 26,083,460 | 17.2% |
| LOAD_FAST | 42,120 | 0.0% |
| SWAP | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 94,551,340 | 62.2% |
| POP_TOP | 57,367,740 | 37.8% |
| UNPACK_SEQUENCE_TUPLE | 1,260 | 0.0% |
| LOAD_FAST | 340 | 0.0% |
| STORE_FAST__LOAD_FAST | 120 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 935,468,512 | 74.6% |
| GET_ITER | 193,898,156 | 15.5% |
| LOAD_FAST | 59,095,840 | 4.7% |
| EXTENDED_ARG | 37,528,100 | 3.0% |
| SWAP | 25,908,152 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 512,389,478 | 40.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 314,360,080 | 25.1% |
| STORE_FAST | 160,209,189 | 12.8% |
| RETURN_CONST | 103,369,804 | 8.2% |
| LOAD_FAST | 62,404,938 | 5.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 423,329,376 | 89.0% |
| GET_ITER | 25,619,062 | 5.4% |
| LOAD_FAST | 21,531,120 | 4.5% |
| SWAP | 4,261,380 | 0.9% |
| EXTENDED_ARG | 790,560 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 293,836,416 | 61.8% |
| STORE_FAST | 132,315,472 | 27.8% |
| RETURN_CONST | 23,857,500 | 5.0% |
| JUMP_BACKWARD | 9,675,480 | 2.0% |
| LOAD_FAST | 3,376,406 | 0.7% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 290,430,153 | 69.5% |
| GET_ITER | 122,054,914 | 29.2% |
| SWAP | 2,897,560 | 0.7% |
| FOR_ITER_LIST | 1,236,537 | 0.3% |
| LOAD_FAST | 1,121,280 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 242,999,280 | 58.2% |
| STORE_FAST | 46,718,491 | 11.2% |
| LOAD_FAST__LOAD_FAST | 41,688,480 | 10.0% |
| LOAD_FAST | 41,247,286 | 9.9% |
| LOAD_FAST__LOAD_CONST | 21,393,480 | 5.1% |


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
| JUMP_BACKWARD | 94,136,760 | 94.0% |
| GET_AITER | 6,000,000 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 100,136,760 | 100.0% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 78,331,698 | 92.6% |
| LOAD_FAST | 3,309,180 | 3.9% |
| RETURN_VALUE | 2,446,800 | 2.9% |
| LOAD_ATTR_INSTANCE_VALUE | 489,659 | 0.6% |
| CALL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 84,577,937 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 139,023,354 | 23.4% |
| LOAD_ATTR_INSTANCE_VALUE | 81,665,976 | 13.8% |
| LOAD_FAST | 74,072,789 | 12.5% |
| CALL_BUILTIN_CLASS | 62,070,562 | 10.5% |
| RETURN_VALUE | 53,925,600 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 193,898,156 | 32.7% |
| FOR_ITER_TUPLE | 122,054,914 | 20.6% |
| CALL_PY_EXACT_ARGS | 84,799,440 | 14.3% |
| FOR_ITER_GEN | 56,956,440 | 9.6% |
| FOR_ITER | 55,096,789 | 9.3% |


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
| IMPORT_NAME | 1,402,200 | 75.7% |
| STORE_FAST | 450,480 | 24.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,852,680 | 100.0% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,535,460 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 1,402,200 | 91.3% |
| STORE_FAST__LOAD_FAST | 130,560 | 8.5% |
| STORE_FAST | 2,100 | 0.1% |
| STORE_NAME | 360 | 0.0% |
| STORE_DEREF | 240 | 0.0% |


</details>

### INSTRUMENTED_FOR_ITER

<details>
<summary> Successors and predecessors for INSTRUMENTED_FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_JUMP_BACKWARD | 4,350 | 51.6% |
| GET_ITER | 4,020 | 47.7% |
| SWAP | 60 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,410 | 52.3% |
| NOP | 3,060 | 36.3% |
| INSTRUMENTED_RETURN_CONST | 240 | 2.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 240 | 2.8% |
| LOAD_CONST | 240 | 2.8% |


</details>

### INSTRUMENTED_JUMP_BACKWARD

<details>
<summary> Successors and predecessors for INSTRUMENTED_JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,060 | 41.3% |
| BINARY_OP_INPLACE_ADD_UNICODE | 3,060 | 41.3% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 870 | 11.7% |
| LIST_APPEND | 300 | 4.0% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 60 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_FOR_ITER | 4,350 | 58.7% |
| LOAD_FAST | 3,060 | 41.3% |


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
| CALL | 7,320 | 0.1% |
| COMPARE_OP_STR | 7,020 | 0.0% |
| LOAD_FAST | 6,840 | 0.0% |
| CALL_NO_KW_ISINSTANCE | 5,520 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,306,500 | 50.0% |
| LOAD_GLOBAL | 7,287,600 | 49.9% |
| INSTRUMENTED_RETURN_CONST | 4,740 | 0.0% |
| LOAD_CONST | 240 | 0.0% |
| POP_TOP | 240 | 0.0% |


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
| LOAD_FAST | 6,420 | 64.3% |
| CALL | 1,230 | 12.3% |
| INSTRUMENTED_RETURN_VALUE | 720 | 7.2% |
| LOAD_ATTR | 540 | 5.4% |
| COPY | 480 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,440 | 44.4% |
| LOAD_GLOBAL | 4,020 | 40.2% |
| INSTRUMENTED_JUMP_BACKWARD | 870 | 8.7% |
| INSTRUMENTED_RETURN_VALUE | 480 | 4.8% |
| POP_TOP | 180 | 1.8% |


</details>

### INSTRUMENTED_RESUME

<details>
<summary> Successors and predecessors for INSTRUMENTED_RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 14,577,840 | 100.0% |
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
| STORE_GLOBAL | 60 | 1.1% |
| CALL_NO_KW_LIST_APPEND | 60 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 4,800 | 88.9% |
| INSTRUMENTED_POP_JUMP_IF_FALSE | 420 | 7.8% |
| POP_TOP | 180 | 3.3% |


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
| INSTRUMENTED_RETURN_VALUE | 960 | 0.0% |
| INSTRUMENTED_POP_JUMP_IF_TRUE | 720 | 0.0% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 473,478,495 | 37.0% |
| YIELD_VALUE | 466,509,679 | 36.4% |
| RETURN_VALUE | 321,573,963 | 25.1% |
| RETURN_GENERATOR | 18,451,380 | 1.4% |
| INSTRUMENTED_RETURN_VALUE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 216,104,040 | 40.7% |
| LOAD_GLOBAL_MODULE | 171,052,960 | 32.2% |
| LOAD_FAST | 64,669,500 | 12.2% |
| LOAD_FAST__LOAD_FAST | 50,633,760 | 9.5% |
| LOAD_GLOBAL_BUILTIN | 15,475,380 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 474,191,376 | 89.4% |
| POP_JUMP_IF_TRUE | 45,834,924 | 8.6% |
| RETURN_VALUE | 3,140,700 | 0.6% |
| COPY | 2,903,880 | 0.5% |
| STORE_FAST__LOAD_FAST | 2,549,940 | 0.5% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 922,443,276 | 28.1% |
| POP_TOP | 715,042,642 | 21.8% |
| POP_JUMP_IF_TRUE | 466,069,597 | 14.2% |
| POP_JUMP_IF_FALSE | 448,361,684 | 13.6% |
| LIST_APPEND | 146,324,026 | 4.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 935,468,512 | 28.5% |
| NOP | 717,888,253 | 21.9% |
| FOR_ITER_RANGE | 423,329,376 | 12.9% |
| FOR_ITER_TUPLE | 290,430,153 | 8.8% |
| FOR_ITER | 216,854,849 | 6.6% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME | 214,263,496 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 208,263,017 | 97.2% |
| SEND | 6,000,479 | 2.8% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 175,205,887 | 41.7% |
| POP_JUMP_IF_FALSE | 98,771,918 | 23.5% |
| POP_TOP | 57,317,299 | 13.7% |
| LOAD_ATTR_SLOT | 22,225,800 | 5.3% |
| POP_JUMP_IF_NONE | 10,513,680 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 159,494,854 | 38.0% |
| LOAD_FAST__LOAD_FAST | 78,414,251 | 18.7% |
| LOAD_CONST__LOAD_FAST | 36,254,520 | 8.6% |
| LOAD_GLOBAL_MODULE | 26,454,849 | 6.3% |
| JUMP_BACKWARD | 26,010,360 | 6.2% |


</details>

### KW_NAMES

<details>
<summary> Successors and predecessors for KW_NAMES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 40,582,289 | 24.1% |
| LOAD_CONST | 36,302,610 | 21.6% |
| LOAD_FAST | 29,893,219 | 17.8% |
| LOAD_GLOBAL_MODULE | 18,000,780 | 10.7% |
| LOAD_ATTR_INSTANCE_VALUE | 11,342,100 | 6.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 144,773,282 | 86.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 22,170,640 | 13.2% |
| CALL_BUILTIN_CLASS | 1,171,480 | 0.7% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 28,850,040 | 19.7% |
| BUILD_TUPLE | 26,458,620 | 18.1% |
| BINARY_OP | 20,606,280 | 14.1% |
| LOAD_FAST | 18,168,840 | 12.4% |
| RETURN_VALUE | 15,020,280 | 10.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 146,324,026 | 99.9% |
| LOAD_FAST | 96,000 | 0.1% |
| CALL_INTRINSIC_1 | 11,520 | 0.0% |
| INSTRUMENTED_JUMP_BACKWARD | 300 | 0.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 37,120,476 | 77.4% |
| LOAD_FAST | 10,127,226 | 21.1% |
| LOAD_CONST | 366,720 | 0.8% |
| RETURN_VALUE | 202,526 | 0.4% |
| LOAD_DEREF | 77,580 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 47,196,796 | 98.5% |
| LOAD_FAST | 195,866 | 0.4% |
| STORE_FAST__LOAD_FAST | 176,366 | 0.4% |
| UNPACK_SEQUENCE_LIST | 172,560 | 0.4% |
| STORE_FAST | 172,560 | 0.4% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 464,604,163 | 41.3% |
| LOAD_GLOBAL_BUILTIN | 221,926,032 | 19.7% |
| STORE_FAST__LOAD_FAST | 145,165,974 | 12.9% |
| LOAD_GLOBAL_MODULE | 94,875,677 | 8.4% |
| LOAD_ATTR_SLOT | 80,027,116 | 7.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 223,390,051 | 19.9% |
| IS_OP | 216,104,040 | 19.2% |
| STORE_FAST__LOAD_FAST | 118,873,360 | 10.6% |
| LOAD_FAST__LOAD_FAST | 92,366,312 | 8.2% |
| STORE_FAST | 53,012,235 | 4.7% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 116,348,980 | 96.4% |
| LOAD_GLOBAL_BUILTIN | 1,919,232 | 1.6% |
| LOAD_FAST | 1,812,980 | 1.5% |
| LOAD_ATTR_MODULE | 358,500 | 0.3% |
| STORE_FAST__LOAD_FAST | 170,740 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 59,700,000 | 49.4% |
| LOAD_FAST | 21,944,068 | 18.2% |
| CALL_PY_EXACT_ARGS | 21,784,900 | 18.0% |
| CALL_BUILTIN_CLASS | 2,841,880 | 2.4% |
| LOAD_FAST__LOAD_FAST | 2,588,052 | 2.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,947,321,624 | 78.8% |
| STORE_FAST__LOAD_FAST | 318,226,374 | 8.5% |
| LOAD_FAST__LOAD_FAST | 250,829,880 | 6.7% |
| COPY | 72,086,939 | 1.9% |
| LOAD_ATTR_INSTANCE_VALUE | 60,061,563 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,044,073,369 | 27.9% |
| POP_JUMP_IF_FALSE | 555,300,052 | 14.8% |
| STORE_FAST__LOAD_FAST | 228,140,266 | 6.1% |
| LOAD_ATTR_METHOD_NO_DICT | 186,174,779 | 5.0% |
| RETURN_VALUE | 182,152,392 | 4.9% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,703,958 | 64.0% |
| LOAD_ATTR_INSTANCE_VALUE | 30,545,100 | 20.4% |
| STORE_FAST__LOAD_FAST | 23,090,200 | 15.4% |
| LOAD_CONST__LOAD_FAST | 154,820 | 0.1% |
| LOAD_DEREF | 74,183 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 65,649,671 | 43.9% |
| LOAD_FAST | 52,350,700 | 35.0% |
| CALL | 27,197,268 | 18.2% |
| LOAD_CONST | 3,006,899 | 2.0% |
| LOAD_FAST__LOAD_FAST | 1,237,800 | 0.8% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 488,519,901 | 37.1% |
| STORE_FAST__LOAD_FAST | 297,678,915 | 22.6% |
| LOAD_ATTR_INSTANCE_VALUE | 186,174,779 | 14.1% |
| LOAD_FAST__LOAD_CONST | 54,098,160 | 4.1% |
| LOAD_GLOBAL_MODULE | 53,199,328 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 633,692,273 | 48.1% |
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 145,745,602 | 11.1% |
| LOAD_FAST__LOAD_FAST | 129,124,253 | 9.8% |
| LOAD_CONST | 119,623,886 | 9.1% |
| CALL_PY_EXACT_ARGS | 109,897,169 | 8.3% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,145,059,483 | 63.0% |
| STORE_FAST__LOAD_FAST | 427,921,107 | 23.5% |
| LOAD_ATTR_INSTANCE_VALUE | 67,710,115 | 3.7% |
| LOAD_ATTR_SLOT | 46,270,767 | 2.5% |
| LOAD_ATTR | 45,742,396 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 626,579,865 | 34.4% |
| LOAD_FAST | 602,916,652 | 33.1% |
| CALL_PY_EXACT_ARGS | 440,640,266 | 24.2% |
| LOAD_GLOBAL_MODULE | 49,848,747 | 2.7% |
| LOAD_CONST__LOAD_FAST | 30,941,880 | 1.7% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 319,828,883 | 95.1% |
| LOAD_ATTR_MODULE | 11,592,000 | 3.4% |
| LOAD_ATTR | 2,078,011 | 0.6% |
| LOAD_ATTR_CLASS | 1,160,080 | 0.3% |
| LOAD_FAST__LOAD_FAST | 927,960 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 106,991,629 | 31.8% |
| LOAD_FAST__LOAD_FAST | 99,706,087 | 29.6% |
| CALL | 26,151,899 | 7.8% |
| CALL_NO_KW_ISINSTANCE | 25,487,500 | 7.6% |
| LOAD_GLOBAL_BUILTIN | 16,057,780 | 4.8% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 30,566,079 | 62.6% |
| STORE_FAST__LOAD_FAST | 10,070,292 | 20.6% |
| LOAD_ATTR_SLOT | 5,106,860 | 10.5% |
| RETURN_VALUE | 1,251,724 | 2.6% |
| LOAD_ATTR_INSTANCE_VALUE | 932,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 43,246,575 | 88.5% |
| POP_JUMP_IF_FALSE | 3,169,920 | 6.5% |
| RETURN_VALUE | 830,660 | 1.7% |
| LOAD_FAST | 538,780 | 1.1% |
| LOAD_ATTR_WITH_HINT | 383,760 | 0.8% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,042,813,730 | 78.3% |
| STORE_FAST__LOAD_FAST | 165,638,797 | 12.4% |
| LOAD_ATTR_SLOT | 40,634,362 | 3.1% |
| COPY | 40,131,480 | 3.0% |
| LOAD_CONST__LOAD_FAST | 13,874,860 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 308,219,719 | 23.2% |
| POP_JUMP_IF_FALSE | 147,678,691 | 11.1% |
| LOAD_ATTR | 80,027,116 | 6.0% |
| COMPARE_OP_FLOAT | 65,981,765 | 5.0% |
| LOAD_ATTR_METHOD_NO_DICT | 47,483,080 | 3.6% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 197,375,386 | 58.8% |
| STORE_FAST__LOAD_FAST | 73,035,280 | 21.7% |
| LOAD_ATTR_WITH_HINT | 22,448,480 | 6.7% |
| LOAD_ATTR_INSTANCE_VALUE | 22,337,509 | 6.6% |
| COPY | 12,982,380 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 78,524,480 | 23.4% |
| STORE_FAST__LOAD_FAST | 42,208,320 | 12.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 36,665,625 | 10.9% |
| COMPARE_OP_INT | 35,140,620 | 10.5% |
| LOAD_CONST | 27,892,680 | 8.3% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CLOSURE | 1,320 | 100.0% |


</details>

### LOAD_CLOSURE

<details>
<summary> Successors and predecessors for LOAD_CLOSURE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 53,797,740 | 49.1% |
| LOAD_CLOSURE | 30,173,302 | 27.5% |
| STORE_FAST | 19,018,440 | 17.3% |
| POP_JUMP_IF_TRUE | 2,239,560 | 2.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,697,940 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 79,461,910 | 72.5% |
| LOAD_CLOSURE | 30,173,302 | 27.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 1,291,283,808 | 27.2% |
| LOAD_CONST | 457,219,731 | 9.6% |
| LOAD_FAST__LOAD_FAST | 394,864,662 | 8.3% |
| LOAD_FAST__LOAD_CONST | 275,822,100 | 5.8% |
| BINARY_SUBSCR_LIST_INT | 192,238,860 | 4.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_STR | 850,057,920 | 17.9% |
| LOAD_CONST | 457,219,731 | 9.6% |
| BINARY_OP_ADD_INT | 416,657,430 | 8.8% |
| COMPARE_OP_INT | 364,236,980 | 7.7% |
| STORE_FAST | 302,145,471 | 6.4% |


</details>

### LOAD_CONST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_CONST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 216,250,607 | 21.2% |
| POP_JUMP_IF_FALSE | 174,128,719 | 17.1% |
| RESUME | 149,642,580 | 14.7% |
| STORE_FAST | 111,611,953 | 10.9% |
| STORE_ATTR_INSTANCE_VALUE | 70,821,516 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 283,151,392 | 27.8% |
| LOAD_FAST | 202,071,936 | 19.8% |
| STORE_ATTR_INSTANCE_VALUE | 121,444,715 | 11.9% |
| SWAP | 78,968,280 | 7.7% |
| CONTAINS_OP | 66,105,960 | 6.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 229,975,980 | 28.3% |
| STORE_FAST | 122,117,258 | 15.1% |
| LOAD_GLOBAL_BUILTIN | 110,563,013 | 13.6% |
| PUSH_NULL | 37,563,089 | 4.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 31,295,640 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 532,653,619 | 65.6% |
| LOAD_CONST | 67,722,352 | 8.3% |
| LOAD_FAST__LOAD_FAST | 29,857,643 | 3.7% |
| LOAD_DEREF | 23,803,663 | 2.9% |
| CALL_NO_KW_LEN | 20,446,300 | 2.5% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,557,487,680 | 14.1% |
| LOAD_GLOBAL_BUILTIN | 2,317,146,380 | 12.7% |
| RESUME | 1,944,742,322 | 10.7% |
| STORE_FAST__LOAD_FAST | 1,203,684,919 | 6.6% |
| LOAD_ATTR_INSTANCE_VALUE | 1,044,073,369 | 5.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 2,947,321,624 | 16.2% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,145,059,483 | 6.3% |
| LOAD_GLOBAL_BUILTIN | 1,076,401,460 | 5.9% |
| LOAD_ATTR_SLOT | 1,042,813,730 | 5.7% |
| CALL_PY_EXACT_ARGS | 817,598,115 | 4.5% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 38,882,116 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,782,966 | 23.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 38,873,956 | 76.7% |
| LOAD_FAST_AND_CLEAR | 11,782,966 | 23.3% |
| MAKE_CELL | 8,160 | 0.0% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,616,680 | 44.4% |
| POP_TOP | 2,052,060 | 25.2% |
| POP_JUMP_IF_NONE | 1,214,249 | 14.9% |
| LOAD_GLOBAL_BUILTIN | 421,740 | 5.2% |
| STORE_FAST | 308,040 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 3,578,840 | 43.9% |
| POP_JUMP_IF_NOT_NONE | 1,506,240 | 18.5% |
| LOAD_FAST | 1,281,480 | 15.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 432,000 | 5.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_O | 294,360 | 3.6% |


</details>

### LOAD_FAST__LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,813,612,453 | 48.4% |
| LOAD_GLOBAL_BUILTIN | 279,622,224 | 7.5% |
| JUMP_BACKWARD | 206,231,040 | 5.5% |
| LOAD_GLOBAL_MODULE | 159,100,860 | 4.2% |
| STORE_FAST__LOAD_FAST | 135,840,780 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 1,355,583,140 | 36.2% |
| COMPARE_OP_STR | 719,742,620 | 19.2% |
| LOAD_CONST | 275,822,100 | 7.4% |
| COMPARE_OP_INT | 253,258,394 | 6.8% |
| BINARY_SUBSCR_DICT | 167,857,560 | 4.5% |


</details>

### LOAD_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,284,453,899 | 16.9% |
| NOP | 1,017,930,263 | 13.4% |
| LOAD_FAST__LOAD_FAST | 629,535,781 | 8.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 626,579,865 | 8.3% |
| LOAD_GLOBAL_MODULE | 474,949,248 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 1,089,244,920 | 14.3% |
| CONTAINS_OP | 813,486,480 | 10.7% |
| CALL_PY_EXACT_ARGS | 798,342,537 | 10.5% |
| LOAD_FAST__LOAD_FAST | 629,535,781 | 8.3% |
| LOAD_FAST | 494,604,316 | 6.5% |


</details>

### LOAD_FROM_DICT_OR_DEREF

<details>
<summary> Successors and predecessors for LOAD_FROM_DICT_OR_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 2,580 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_LOCALS | 1,200 | 46.5% |
| CALL_PY_EXACT_ARGS | 1,200 | 46.5% |
| LOAD_CONST | 180 | 7.0% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| INSTRUMENTED_POP_JUMP_IF_FALSE | 7,287,600 | 99.0% |
| STORE_FAST | 18,731 | 0.3% |
| INSTRUMENTED_RESUME | 12,000 | 0.2% |
| RESUME | 6,960 | 0.1% |
| NOP | 4,180 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,302,184 | 99.2% |
| LOAD_GLOBAL_MODULE | 30,782 | 0.4% |
| LOAD_ATTR_MODULE | 14,100 | 0.2% |
| LOAD_GLOBAL_BUILTIN | 12,672 | 0.2% |
| LOAD_ATTR | 1,861 | 0.0% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,076,401,460 | 26.4% |
| POP_JUMP_IF_FALSE | 979,749,070 | 24.0% |
| RESUME | 834,236,004 | 20.4% |
| STORE_FAST | 538,229,395 | 13.2% |
| POP_JUMP_IF_TRUE | 101,489,402 | 2.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,317,146,380 | 56.7% |
| CALL_NO_KW_BUILTIN_FAST | 434,565,640 | 10.6% |
| CALL_NO_KW_ISINSTANCE | 321,584,301 | 7.9% |
| LOAD_FAST__LOAD_CONST | 279,622,224 | 6.8% |
| LOAD_ATTR | 221,926,032 | 5.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 586,557,964 | 20.1% |
| STORE_FAST | 413,625,696 | 14.2% |
| STORE_FAST__LOAD_FAST | 336,844,863 | 11.6% |
| RESUME | 327,521,958 | 11.2% |
| POP_JUMP_IF_FALSE | 282,085,663 | 9.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 474,949,248 | 16.3% |
| CALL_NO_KW_ISINSTANCE | 341,465,256 | 11.7% |
| LOAD_ATTR_MODULE | 319,828,883 | 11.0% |
| CONTAINS_OP | 305,981,940 | 10.5% |
| LOAD_FAST | 266,979,005 | 9.2% |


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
| PUSH_NULL | 4,680,900 | 52.0% |
| LOAD_NAME | 4,320,720 | 48.0% |
| RESUME | 1,320 | 0.0% |
| STORE_NAME | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_NAME | 4,320,720 | 48.0% |
| LOAD_CONST | 4,320,720 | 48.0% |
| PUSH_NULL | 360,000 | 4.0% |
| STORE_NAME | 1,320 | 0.0% |
| LOAD_LOCALS | 180 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 1,120 | 98.2% |
| LOAD_SUPER_ATTR_ATTR | 20 | 1.8% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,296,480 | 100.0% |
| LOAD_GLOBAL_MODULE | 120 | 0.0% |
| LOAD_SUPER_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,217,900 | 96.6% |
| LOAD_GLOBAL_MODULE | 64,080 | 2.8% |
| LOAD_FAST__LOAD_FAST | 10,200 | 0.4% |
| STORE_FAST | 4,320 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 120 | 0.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 117,776,990 | 100.0% |
| LOAD_DEREF | 9,000 | 0.0% |
| LOAD_SUPER_ATTR | 1,120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 66,528,135 | 56.5% |
| LOAD_FAST | 36,798,840 | 31.2% |
| CALL_PY_EXACT_ARGS | 6,360,315 | 5.4% |
| CALL_PY_WITH_DEFAULTS | 5,951,040 | 5.1% |
| CALL | 1,199,820 | 1.0% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,666,842 | 57.4% |
| CALL_PY_EXACT_ARGS | 24,892,307 | 30.0% |
| CALL_FUNCTION_EX | 4,707,040 | 5.7% |
| CALL | 3,797,940 | 4.6% |
| CALL_PY_WITH_DEFAULTS | 1,008,240 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 47,666,842 | 57.3% |
| RESUME | 34,863,447 | 41.9% |
| RETURN_GENERATOR | 581,100 | 0.7% |
| SWAP | 8,160 | 0.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 93,642,414 | 100.0% |
| LOAD_FAST__LOAD_CONST | 9,240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 60,303,540 | 64.4% |
| LOAD_GLOBAL_BUILTIN | 18,994,680 | 20.3% |
| STORE_FAST | 2,951,087 | 3.2% |
| LOAD_GLOBAL_MODULE | 2,838,440 | 3.0% |
| STORE_FAST__LOAD_FAST | 2,504,864 | 2.7% |


</details>

### MAP_ADD

<details>
<summary> Successors and predecessors for MAP_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 15,836,160 | 38.9% |
| RETURN_VALUE | 6,246,240 | 15.3% |
| LOAD_FAST | 5,888,640 | 14.5% |
| JUMP_FORWARD | 4,782,720 | 11.7% |
| STORE_FAST | 4,423,680 | 10.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST__LOAD_FAST | 20,584,800 | 50.5% |
| JUMP_BACKWARD | 18,948,240 | 46.5% |
| CALL_FUNCTION_EX | 1,211,400 | 3.0% |
| LOAD_CONST | 5,940 | 0.0% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 717,888,253 | 48.5% |
| RESUME | 334,041,382 | 22.6% |
| STORE_FAST | 147,002,576 | 9.9% |
| POP_JUMP_IF_FALSE | 81,070,096 | 5.5% |
| NOP | 52,740,164 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 1,017,930,263 | 68.7% |
| LOAD_FAST | 277,054,832 | 18.7% |
| NOP | 52,740,164 | 3.6% |
| PUSH_NULL | 41,394,031 | 2.8% |
| LOAD_GLOBAL_BUILTIN | 34,226,087 | 2.3% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 9,776,292 | 57.0% |
| STORE_SUBSCR_DICT | 3,075,240 | 17.9% |
| SWAP | 1,968,240 | 11.5% |
| COPY | 1,669,320 | 9.7% |
| STORE_FAST | 442,620 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 9,153,920 | 53.4% |
| RETURN_VALUE | 1,910,640 | 11.1% |
| JUMP_FORWARD | 1,715,820 | 10.0% |
| RERAISE | 1,669,320 | 9.7% |
| POP_TOP | 1,384,132 | 8.1% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 1,871,629,227 | 22.2% |
| COMPARE_OP_STR | 1,555,861,166 | 18.5% |
| COMPARE_OP_INT | 1,186,678,429 | 14.1% |
| CALL_NO_KW_ISINSTANCE | 657,049,163 | 7.8% |
| LOAD_ATTR_INSTANCE_VALUE | 555,300,052 | 6.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,557,487,680 | 30.4% |
| LOAD_FAST__LOAD_CONST | 1,813,612,453 | 21.5% |
| LOAD_FAST__LOAD_FAST | 1,284,453,899 | 15.3% |
| LOAD_GLOBAL_BUILTIN | 979,749,070 | 11.6% |
| JUMP_BACKWARD | 448,361,684 | 5.3% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__LOAD_FAST | 156,660,747 | 52.7% |
| LOAD_FAST | 48,145,170 | 16.2% |
| EXTENDED_ARG | 37,462,780 | 12.6% |
| LOAD_ATTR_SLOT | 25,233,420 | 8.5% |
| LOAD_DEREF | 13,536,180 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 95,517,136 | 32.1% |
| PUSH_NULL | 52,475,464 | 17.6% |
| LOAD_FAST__LOAD_CONST | 36,587,439 | 12.3% |
| LOAD_DEREF | 27,393,360 | 9.2% |
| JUMP_BACKWARD | 26,685,847 | 9.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,532,828 | 52.9% |
| STORE_FAST__LOAD_FAST | 134,859,564 | 31.6% |
| LOAD_ATTR_INSTANCE_VALUE | 29,664,444 | 7.0% |
| LOAD_ATTR | 17,696,424 | 4.2% |
| EXTENDED_ARG | 7,189,500 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 147,970,528 | 34.7% |
| LOAD_GLOBAL_BUILTIN | 99,729,560 | 23.4% |
| LOAD_FAST__LOAD_FAST | 59,536,206 | 14.0% |
| LOAD_GLOBAL_MODULE | 35,090,658 | 8.2% |
| NOP | 18,354,837 | 4.3% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 568,882,758 | 38.3% |
| STORE_FAST__LOAD_FAST | 192,993,578 | 13.0% |
| COMPARE_OP_INT | 122,880,400 | 8.3% |
| CALL_NO_KW_ISINSTANCE | 108,850,176 | 7.3% |
| COPY | 85,698,024 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 528,309,669 | 35.6% |
| JUMP_BACKWARD | 466,069,597 | 31.4% |
| LOAD_GLOBAL_BUILTIN | 101,489,402 | 6.8% |
| POP_TOP | 72,132,560 | 4.9% |
| LOAD_CONST | 60,820,848 | 4.1% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 554,824,873 | 24.1% |
| RESUME | 548,746,160 | 23.8% |
| CALL_NO_KW_BUILTIN_O | 347,469,156 | 15.1% |
| POP_JUMP_IF_FALSE | 167,277,575 | 7.3% |
| RETURN_VALUE | 115,590,656 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 799,886,022 | 33.4% |
| JUMP_BACKWARD | 715,042,642 | 29.9% |
| RESUME | 238,729,778 | 10.0% |
| RETURN_CONST | 178,651,692 | 7.5% |
| LOAD_FAST__LOAD_FAST | 124,963,636 | 5.2% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 5,320,500 | 31.1% |
| LOAD_ATTR | 3,258,780 | 19.0% |
| RAISE_VARARGS | 2,296,860 | 13.4% |
| CALL_NO_KW_BUILTIN_FAST | 1,783,220 | 10.4% |
| RERAISE | 1,632,600 | 9.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 15,725,955 | 91.7% |
| LOAD_GLOBAL_MODULE | 1,028,280 | 6.0% |
| LOAD_FAST | 386,940 | 2.3% |
| WITH_EXCEPT_START | 4,320 | 0.0% |
| LOAD_GLOBAL | 720 | 0.0% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 273,561,763 | 35.4% |
| POP_JUMP_IF_FALSE | 98,894,552 | 12.8% |
| POP_TOP | 70,134,240 | 9.1% |
| POP_JUMP_IF_NONE | 52,475,464 | 6.8% |
| NOP | 41,394,031 | 5.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 447,601,344 | 58.0% |
| LOAD_FAST | 152,051,885 | 19.7% |
| LOAD_FAST__LOAD_CONST | 125,780,700 | 16.3% |
| LOAD_DEREF | 37,563,089 | 4.9% |
| LOAD_NAME | 4,680,900 | 0.6% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,491,540 | 43.7% |
| LOAD_ATTR_MODULE | 583,740 | 17.1% |
| LOAD_CONST | 544,200 | 16.0% |
| LOAD_GLOBAL_BUILTIN | 543,240 | 15.9% |
| LOAD_FAST | 150,960 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 2,296,860 | 67.3% |
| COPY | 963,540 | 28.2% |
| LOAD_CONST | 151,020 | 4.4% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 6,377,160 | 72.9% |
| POP_EXCEPT | 1,669,320 | 19.1% |
| POP_TOP | 386,940 | 4.4% |
| POP_JUMP_IF_FALSE | 154,860 | 1.8% |
| DELETE_FAST | 151,020 | 1.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 1,632,600 | 68.9% |
| COPY | 697,140 | 29.4% |
| CALL_INTRINSIC_1 | 41,160 | 1.7% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 2,516,821,591 | 63.9% |
| POP_TOP | 238,729,778 | 6.1% |
| SEND_GEN | 208,263,017 | 5.3% |
| CALL | 204,746,743 | 5.2% |
| COPY_FREE_VARS | 181,061,097 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,944,742,322 | 38.7% |
| LOAD_GLOBAL_BUILTIN | 834,236,004 | 16.6% |
| POP_TOP | 548,746,160 | 10.9% |
| NOP | 334,041,382 | 6.6% |
| LOAD_GLOBAL_MODULE | 327,521,958 | 6.5% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 253,763,579 | 19.1% |
| STORE_ATTR_SLOT | 245,137,364 | 18.5% |
| STORE_ATTR_INSTANCE_VALUE | 181,423,513 | 13.7% |
| POP_TOP | 178,651,692 | 13.5% |
| RESUME | 122,694,660 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 554,824,873 | 41.8% |
| INTERPRETER_EXIT | 473,478,495 | 35.7% |
| END_FOR | 57,304,960 | 4.3% |
| LOAD_FAST | 52,435,800 | 4.0% |
| RETURN_VALUE | 49,481,603 | 3.7% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 140,526,618 | 63.8% |
| COPY_FREE_VARS | 73,398,240 | 33.3% |
| CALL_PY_WITH_DEFAULTS | 3,297,780 | 1.5% |
| CALL_FUNCTION_EX | 1,713,800 | 0.8% |
| CALL | 769,440 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 78,331,698 | 32.8% |
| GET_ITER | 37,914,060 | 15.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 33,017,040 | 13.8% |
| STORE_FAST__LOAD_FAST | 19,048,740 | 8.0% |
| INTERPRETER_EXIT | 18,451,380 | 7.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 758,968,516 | 26.0% |
| RETURN_VALUE | 475,417,389 | 16.3% |
| BUILD_TUPLE | 405,105,780 | 13.9% |
| LOAD_ATTR_INSTANCE_VALUE | 182,152,392 | 6.2% |
| BINARY_SUBSCR_DICT | 104,620,047 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 475,417,389 | 16.3% |
| STORE_FAST__LOAD_FAST | 347,654,847 | 11.9% |
| INTERPRETER_EXIT | 321,573,963 | 11.0% |
| STORE_FAST | 266,358,316 | 9.1% |
| UNPACK_SEQUENCE_TUPLE | 258,461,900 | 8.8% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 106,299,739 | 94.6% |
| JUMP_BACKWARD_NO_INTERRUPT | 6,000,479 | 5.3% |
| SEND | 28,140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 100,299,239 | 89.3% |
| YIELD_VALUE | 6,000,719 | 5.3% |
| END_ASYNC_FOR | 6,000,000 | 5.3% |
| SEND | 28,140 | 0.0% |
| SEND_GEN | 260 | 0.0% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 208,263,017 | 69.0% |
| LOAD_CONST | 93,584,218 | 31.0% |
| SEND | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME | 208,263,017 | 69.0% |
| POP_TOP | 93,584,478 | 31.0% |


</details>

### SET_ADD

<details>
<summary> Successors and predecessors for SET_ADD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_UNICODE | 2,879,280 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 124,560 | 4.0% |
| STORE_FAST__LOAD_FAST | 48,000 | 1.5% |
| LOAD_FAST | 19,440 | 0.6% |
| BINARY_SUBSCR_LIST_INT | 17,520 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 3,100,800 | 100.0% |


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
| LOAD_FAST | 17,988,120 | 32.1% |
| LOAD_CONST__LOAD_FAST | 16,852,166 | 30.0% |
| LOAD_FAST__LOAD_FAST | 14,018,840 | 25.0% |
| CALL | 5,419,260 | 9.7% |
| SWAP | 1,330,190 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,168,505 | 28.8% |
| LOAD_DEREF | 13,446,480 | 24.0% |
| RETURN_CONST | 11,226,200 | 20.0% |
| JUMP_BACKWARD | 5,554,200 | 9.9% |
| LOAD_FAST__LOAD_FAST | 4,695,100 | 8.4% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 316,804,571 | 38.3% |
| LOAD_FAST | 240,753,108 | 29.1% |
| LOAD_CONST__LOAD_FAST | 121,444,715 | 14.7% |
| SWAP | 72,086,939 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 27,097,200 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 289,329,114 | 35.0% |
| RETURN_CONST | 181,423,513 | 21.9% |
| LOAD_FAST__LOAD_FAST | 165,885,272 | 20.1% |
| LOAD_CONST__LOAD_FAST | 70,821,516 | 8.6% |
| NOP | 51,297,262 | 6.2% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 475,984,531 | 45.3% |
| LOAD_CONST__LOAD_FAST | 283,151,392 | 27.0% |
| LOAD_FAST | 243,957,289 | 23.2% |
| SWAP | 40,131,480 | 3.8% |
| STORE_FAST__LOAD_FAST | 3,626,160 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 280,309,589 | 26.7% |
| RETURN_CONST | 245,137,364 | 23.4% |
| LOAD_FAST | 242,527,325 | 23.1% |
| LOAD_CONST__LOAD_FAST | 216,250,607 | 20.6% |
| LOAD_GLOBAL_BUILTIN | 24,862,340 | 2.4% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,238,560 | 41.9% |
| SWAP | 12,982,380 | 25.6% |
| LOAD_FAST__LOAD_FAST | 11,672,780 | 23.0% |
| LOAD_CONST__LOAD_FAST | 4,323,202 | 8.5% |
| LOAD_DEREF | 240,940 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 33,381,560 | 65.8% |
| JUMP_BACKWARD | 5,313,540 | 10.5% |
| RETURN_CONST | 4,455,105 | 8.8% |
| LOAD_CONST__LOAD_FAST | 3,665,700 | 7.2% |
| LOAD_FAST__LOAD_FAST | 2,308,020 | 4.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 26,873,520 | 41.3% |
| STORE_FAST | 19,045,080 | 29.3% |
| LOAD_CONST | 6,734,880 | 10.3% |
| YIELD_VALUE | 2,419,200 | 3.7% |
| CALL | 2,261,700 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 18,986,280 | 29.2% |
| LOAD_DEREF | 13,726,264 | 21.1% |
| LOAD_FAST__LOAD_FAST | 13,436,760 | 20.6% |
| LOAD_FAST | 9,422,460 | 14.5% |
| LOAD_CONST | 4,658,340 | 7.2% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 784,748,519 | 25.1% |
| LOAD_CONST | 302,145,471 | 9.7% |
| RETURN_VALUE | 266,358,316 | 8.5% |
| STORE_FAST__STORE_FAST | 218,053,080 | 7.0% |
| CALL_NO_KW_BUILTIN_FAST | 216,765,260 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 922,443,276 | 29.5% |
| LOAD_GLOBAL_BUILTIN | 538,229,395 | 17.2% |
| LOAD_GLOBAL_MODULE | 413,625,696 | 13.2% |
| PUSH_NULL | 273,561,763 | 8.7% |
| JUMP_FORWARD | 175,205,887 | 5.6% |


</details>

### STORE_FAST__LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR | 952,340,440 | 16.1% |
| FOR_ITER_LIST | 512,389,478 | 8.7% |
| BINARY_OP_ADD_INT | 473,850,420 | 8.0% |
| RETURN_VALUE | 347,654,847 | 5.9% |
| FOR_ITER_RANGE | 293,836,416 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,291,283,808 | 21.9% |
| LOAD_FAST | 1,203,684,919 | 20.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 427,921,107 | 7.3% |
| POP_JUMP_IF_FALSE | 397,872,436 | 6.7% |
| LOAD_GLOBAL_MODULE | 336,844,863 | 5.7% |


</details>

### STORE_FAST__STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST__STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 821,885,600 | 40.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 578,245,714 | 28.5% |
| UNPACK_SEQUENCE_TUPLE | 389,713,420 | 19.2% |
| UNPACK_SEQUENCE_LIST | 140,218,620 | 6.9% |
| LOAD_ATTR_SLOT | 45,908,040 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 821,885,600 | 40.5% |
| LOAD_FAST | 442,066,777 | 21.8% |
| LOAD_DEREF | 229,975,980 | 11.3% |
| STORE_FAST | 218,053,080 | 10.7% |
| STORE_FAST__LOAD_FAST | 111,654,600 | 5.5% |


</details>

### STORE_GLOBAL

<details>
<summary> Successors and predecessors for STORE_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 6,147,600 | 99.9% |
| CALL | 3,840 | 0.1% |
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
| MAKE_FUNCTION | 240 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,680 | 35.0% |
| LOAD_CONST | 1,440 | 30.0% |
| PUSH_NULL | 1,380 | 28.7% |
| LOAD_CLOSURE | 120 | 2.5% |
| STORE_NAME | 120 | 2.5% |


</details>

### STORE_SLICE

<details>
<summary> Successors and predecessors for STORE_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 103,909,260 | 88.3% |
| LOAD_CONST | 13,459,080 | 11.4% |
| LOAD_FAST__LOAD_FAST | 258,360 | 0.2% |
| LOAD_ATTR | 8,040 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_CONST | 103,875,000 | 88.3% |
| RETURN_CONST | 5,855,760 | 5.0% |
| LOAD_FAST__LOAD_FAST | 4,157,040 | 3.5% |
| LOAD_FAST | 3,703,320 | 3.1% |
| JUMP_BACKWARD | 39,840 | 0.0% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 109,571,980 | 34.7% |
| LOAD_FAST | 85,443,414 | 27.1% |
| BINARY_OP_ADD_INT | 41,532,300 | 13.2% |
| LOAD_FAST__LOAD_FAST | 36,010,260 | 11.4% |
| LOAD_FAST__LOAD_CONST | 25,985,560 | 8.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 112,068,360 | 35.5% |
| LOAD_FAST__LOAD_FAST | 104,114,220 | 33.0% |
| RETURN_CONST | 33,819,484 | 10.7% |
| LOAD_GLOBAL_BUILTIN | 27,002,980 | 8.6% |
| LOAD_DEREF | 15,741,300 | 5.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 138,142,752 | 69.4% |
| LOAD_FAST__LOAD_FAST | 20,546,400 | 10.3% |
| CALL_NO_KW_BUILTIN_O | 13,999,740 | 7.0% |
| RETURN_VALUE | 7,992,040 | 4.0% |
| BINARY_SUBSCR_TUPLE_INT | 3,815,040 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 72,025,804 | 36.2% |
| LOAD_FAST | 64,212,331 | 32.3% |
| JUMP_BACKWARD | 28,491,420 | 14.3% |
| RETURN_CONST | 17,650,564 | 8.9% |
| LOAD_GLOBAL_MODULE | 7,340,704 | 3.7% |


</details>

### STORE_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 158,091,420 | 52.2% |
| LOAD_FAST__LOAD_FAST | 69,943,740 | 23.1% |
| LOAD_FAST__LOAD_CONST | 26,244,000 | 8.7% |
| BINARY_SUBSCR_LIST_INT | 20,171,040 | 6.7% |
| BINARY_OP_SUBTRACT_INT | 15,939,000 | 5.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 110,624,160 | 36.5% |
| LOAD_FAST__LOAD_FAST | 97,710,840 | 32.3% |
| LOAD_FAST__LOAD_CONST | 87,681,960 | 29.0% |
| RETURN_CONST | 4,685,160 | 1.5% |
| LOAD_FAST | 1,265,180 | 0.4% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 269,175,600 | 29.4% |
| BINARY_OP_ADD_FLOAT | 116,255,040 | 12.7% |
| BINARY_OP_ADD_INT | 80,942,995 | 8.8% |
| LOAD_CONST__LOAD_FAST | 78,968,280 | 8.6% |
| BINARY_OP_SUBTRACT_INT | 68,461,849 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 269,175,600 | 29.4% |
| STORE_SUBSCR_LIST_INT | 158,091,420 | 17.3% |
| STORE_SUBSCR | 109,571,980 | 12.0% |
| COPY | 105,750,660 | 11.6% |
| STORE_ATTR_INSTANCE_VALUE | 72,086,939 | 7.9% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,533,255 | 84.4% |
| LOAD_ATTR_MODULE | 1,444,270 | 11.6% |
| LOAD_ATTR | 377,372 | 3.0% |
| LOAD_FAST | 132,300 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 12,487,197 | 100.0% |


</details>

### UNARY_NEGATIVE

<details>
<summary> Successors and predecessors for UNARY_NEGATIVE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST__LOAD_FAST | 110,837,640 | 91.4% |
| LOAD_GLOBAL_MODULE | 3,058,560 | 2.5% |
| LOAD_FAST | 2,803,800 | 2.3% |
| LOAD_CONST__LOAD_FAST | 2,222,160 | 1.8% |
| BINARY_SUBSCR_TUPLE_INT | 1,205,640 | 1.0% |

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
| LOAD_ATTR_INSTANCE_VALUE | 32,284,612 | 55.2% |
| LOAD_FAST | 12,189,360 | 20.9% |
| CALL_NO_KW_ISINSTANCE | 7,956,060 | 13.6% |
| STORE_FAST__LOAD_FAST | 1,934,340 | 3.3% |
| BINARY_SUBSCR | 1,513,680 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 29,526,840 | 50.5% |
| RETURN_VALUE | 16,573,230 | 28.4% |
| KW_NAMES | 10,514,640 | 18.0% |
| CALL_PY_EXACT_ARGS | 746,880 | 1.3% |
| LOAD_FAST | 555,240 | 0.9% |


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
| STORE_FAST__STORE_FAST | 220,200 | 100.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS | 96,120 | 46.3% |
| CALL_NO_KW_METHOD_DESCRIPTOR_FAST | 67,940 | 32.7% |
| COPY | 19,920 | 9.6% |
| FOR_ITER_LIST | 10,560 | 5.1% |
| LOAD_FAST | 9,100 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 204,840 | 98.7% |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,440 | 0.7% |
| UNPACK_SEQUENCE_TUPLE | 420 | 0.2% |
| UNPACK_SEQUENCE | 420 | 0.2% |
| LOAD_FAST | 360 | 0.2% |


</details>

### UNPACK_SEQUENCE_LIST

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,172,180 | 70.0% |
| UNPACK_SEQUENCE_TUPLE | 24,026,440 | 17.1% |
| CALL | 10,636,560 | 7.6% |
| STORE_FAST | 6,000,900 | 4.3% |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 805,200 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 140,218,620 | 100.0% |
| UNPACK_SEQUENCE_TUPLE | 24,040 | 0.0% |
| STORE_FAST | 60 | 0.0% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 258,461,900 | 58.5% |
| LOAD_FAST | 102,479,620 | 23.2% |
| YIELD_VALUE | 25,091,440 | 5.7% |
| BINARY_SUBSCR_DICT | 14,268,900 | 3.2% |
| STORE_FAST | 12,281,520 | 2.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 389,713,420 | 88.3% |
| STORE_FAST | 24,993,240 | 5.7% |
| UNPACK_SEQUENCE_LIST | 24,026,440 | 5.4% |
| STORE_FAST__LOAD_FAST | 2,518,580 | 0.6% |
| LOAD_FAST | 290,520 | 0.1% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 314,360,080 | 52.3% |
| FOR_ITER | 148,151,760 | 24.7% |
| RETURN_VALUE | 84,041,120 | 14.0% |
| LOAD_FAST | 36,450,520 | 6.1% |
| BINARY_SUBSCR_LIST_INT | 9,483,960 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST__STORE_FAST | 578,245,714 | 96.2% |
| UNPACK_SEQUENCE_TUPLE | 12,001,200 | 2.0% |
| STORE_FAST__LOAD_FAST | 9,187,080 | 1.5% |
| LOAD_FAST | 906,600 | 0.2% |
| STORE_FAST | 649,380 | 0.1% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 4,320 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 4,320 | 100.0% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 210,931,680 | 27.4% |
| YIELD_VALUE | 208,263,017 | 27.1% |
| CALL_INTRINSIC_1 | 94,136,760 | 12.2% |
| LOAD_FAST | 39,519,640 | 5.1% |
| STORE_FAST__LOAD_FAST | 33,543,660 | 4.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 466,509,679 | 60.6% |
| YIELD_VALUE | 208,263,017 | 27.1% |
| STORE_FAST__LOAD_FAST | 47,629,620 | 6.2% |
| UNPACK_SEQUENCE_TUPLE | 25,091,440 | 3.3% |
| STORE_FAST | 18,055,380 | 2.3% |


</details>


</details>

## Specialization stats

<details>
<summary> specialization stats by family </summary>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   2352793602 | 55.5% |
| specialization.deopt |        60040 | 0.0% |
|          hit |   1883795575 | 44.4% |
|         miss |      3183240 | 0.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 61,616 | 9.4% |
| Failure | 592,123 | 90.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| string int | 306,340 | 51.7% |
| array int | 112,980 | 19.1% |
| other | 76,560 | 12.9% |
| out of range | 42,140 | 7.1% |
| list slice | 25,560 | 4.3% |
| buffer int | 24,023 | 4.1% |
| sequence int | 2,920 | 0.5% |
| code complex parameters | 1,340 | 0.2% |
| buffer slice | 180 | 0.0% |
| tuple slice | 60 | 0.0% |
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
| specialization.deferred |    315714769 | 38.6% |
| specialization.deopt |           40 | 0.0% |
|          hit |    501789283 | 61.4% |
|         miss |         2220 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 645 | 0.8% |
| Failure | 83,300 | 99.2% |

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
| specialization.deferred |       205200 | 0.0% |
| specialization.deopt |        48080 | 0.0% |
|          hit |   1180250894 | 99.8% |
|         miss |      2547700 | 0.2% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 49,960 | 99.2% |
| Failure | 420 | 0.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| sequence | 180 | 42.9% |
| iterator | 160 | 38.1% |
| other | 80 | 19.0% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    296835063 | 11.4% |
| specialization.deopt |      2480871 | 0.1% |
|          hit |   2166948676 | 83.5% |
|         miss |    131488139 | 5.1% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,481,530 | 96.3% |
| Failure | 95,294 | 3.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| enumerate | 23,000 | 24.1% |
| dict items | 18,120 | 19.0% |
| seq iter | 15,120 | 15.9% |
| set | 10,994 | 11.5% |
| other | 8,800 | 9.2% |
| dict values | 5,040 | 5.3% |
| reversed list | 3,960 | 4.2% |
| zip | 3,200 | 3.4% |
| ascii string | 2,660 | 2.8% |
| dict keys | 1,880 | 2.0% |
| itertools | 1,740 | 1.8% |
| map | 600 | 0.6% |
| callable | 120 | 0.1% |
| bytes | 40 | 0.0% |
| string | 20 | 0.0% |


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |     56052411 | 2.8% |
| specialization.deopt |      3543562 | 0.2% |
|          hit |   1739102049 | 87.7% |
|         miss |    187818145 | 9.5% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,559,247 | 99.0% |
| Failure | 36,300 | 1.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| class attr simple | 17,200 | 47.4% |
| not in dict | 8,020 | 22.1% |
| overriding descriptor | 5,500 | 15.2% |
| not managed dict | 1,540 | 4.2% |
| not in keys | 1,000 | 2.8% |
| property | 980 | 2.7% |
| non object slot | 920 | 2.5% |
| overridden | 640 | 1.8% |
| no dict | 260 | 0.7% |
| method | 240 | 0.7% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |   1123869213 | 10.9% |
| specialization.deopt |      9718918 | 0.1% |
|          hit |   8684393063 | 84.1% |
|         miss |    515227638 | 5.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,770,009 | 87.0% |
| Failure | 1,458,346 | 13.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 609,460 | 41.8% |
| class attr simple | 583,087 | 40.0% |
| metaclass attribute | 99,424 | 6.8% |
| not managed dict | 76,032 | 5.2% |
| method | 54,315 | 3.7% |
| class method obj | 10,020 | 0.7% |
| non object slot | 6,700 | 0.5% |
| overridden | 4,720 | 0.3% |
| non overriding descriptor | 4,036 | 0.3% |
| mutable class | 2,500 | 0.2% |
| class attr descriptor | 2,320 | 0.2% |
| shadowed | 2,012 | 0.1% |
| not in keys | 1,680 | 0.1% |
| module attr not found | 1,680 | 0.1% |
| builtin class method | 360 | 0.0% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    136222834 | 4.2% |
| specialization.deopt |        23554 | 0.0% |
|          hit |   3123717257 | 95.8% |
|         miss |      1249557 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 26,849 | 20.0% |
| Failure | 107,649 | 80.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| big int | 45,079 | 41.9% |
| different types | 24,679 | 22.9% |
| baseobject | 13,020 | 12.1% |
| float long | 8,796 | 8.2% |
| set | 6,620 | 6.1% |
| other | 2,840 | 2.6% |
| bool | 2,335 | 2.2% |
| tuple | 2,140 | 2.0% |
| list | 1,020 | 0.9% |
| bytes | 820 | 0.8% |
| long float | 160 | 0.1% |
| string | 140 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |      7322152 | 0.1% |
| specialization.deopt |          403 | 0.0% |
|          hit |   7001014154 | 99.9% |
|         miss |        27182 | 0.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 40,397 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    812667821 | 15.3% |
| specialization.deopt |       712800 | 0.0% |
|          hit |   4468933757 | 84.0% |
|         miss |     37779500 | 0.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 716,117 | 39.4% |
| Failure | 1,100,482 | 60.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| subtract different types | 578,820 | 52.6% |
| multiply different types | 170,984 | 15.5% |
| add different types | 151,620 | 13.8% |
| floor divide | 32,680 | 3.0% |
| remainder | 31,910 | 2.9% |
| add other | 26,940 | 2.4% |
| and int | 24,958 | 2.3% |
| lshift | 18,620 | 1.7% |
| rshift | 16,540 | 1.5% |
| true divide different types | 14,340 | 1.3% |
| xor | 10,720 | 1.0% |
| true divide float | 6,640 | 0.6% |
| subtract other | 5,440 | 0.5% |
| or | 3,670 | 0.3% |
| power | 3,640 | 0.3% |
| multiply other | 1,060 | 0.1% |
| true divide other | 980 | 0.1% |
| and other | 820 | 0.1% |
| and different types | 100 | 0.0% |


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    112299958 | 27.1% |
|          hit |    301847495 | 72.9% |

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

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---|---|
|          hit |    120083730 | 100.0% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,140 | 100.0% |
| Failure | 0 | 0.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---|---|
| specialization.deferred |    949825402 | 10.8% |
| specialization.deopt |      2865319 | 0.0% |
|          hit |   7661711155 | 87.4% |
|         miss |    151962681 | 1.7% |

#### Specialization attempts

| | Count | Ratio | 
|---|---:|---:|
| Success | 2,900,716 | 87.9% |
| Failure | 398,524 | 12.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| python class | 100,044 | 25.1% |
| meth descr method fastcall keywords | 65,620 | 16.5% |
| kwnames | 51,489 | 12.9% |
| code complex parameters | 49,300 | 12.4% |
| class no vectorcall | 26,003 | 6.5% |
| cfunc varargs keywords | 23,552 | 5.9% |
| meth descr varargs | 21,611 | 5.4% |
| cfunc noargs | 19,650 | 4.9% |
| other | 10,180 | 2.6% |
| class mutable | 9,424 | 2.4% |
| meth descr varargs keywords | 6,212 | 1.6% |
| cmethod | 4,320 | 1.1% |
| bound method | 3,422 | 0.9% |
| method wrapper | 2,486 | 0.6% |
| cfunc varargs | 2,100 | 0.5% |
| operator wrapper | 2,091 | 0.5% |
| str | 1,020 | 0.3% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 86,916,479,735 | 65.3% |
| Not specialized | 7,561,855,406 | 5.7% |
| Specialized | 38,687,272,762 | 29.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| BINARY_SUBSCR | 2,352,793,602 | 38.2% |
| LOAD_ATTR | 1,123,869,213 | 18.2% |
| CALL | 949,825,402 | 15.4% |
| BINARY_OP | 812,667,821 | 13.2% |
| STORE_SUBSCR | 315,714,769 | 5.1% |
| FOR_ITER | 296,835,063 | 4.8% |
| COMPARE_OP | 136,222,834 | 2.2% |
| SEND | 112,299,958 | 1.8% |
| STORE_ATTR | 56,052,411 | 0.9% |
| LOAD_GLOBAL | 7,322,152 | 0.1% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 231,281,276 | 22.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 168,367,380 | 16.3% |
| STORE_ATTR_SLOT | 111,896,707 | 10.9% |
| CALL_PY_EXACT_ARGS | 91,956,600 | 8.9% |
| STORE_ATTR_INSTANCE_VALUE | 75,046,518 | 7.3% |
| FOR_ITER_LIST | 65,844,639 | 6.4% |
| FOR_ITER_TUPLE | 65,590,760 | 6.4% |
| LOAD_ATTR_SLOT | 56,531,081 | 5.5% |
| LOAD_ATTR_METHOD_NO_DICT | 45,396,167 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 29,108,146 | 2.8% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 1,288,381,364 | 24.4% |
| Calls to Python functions inlined | 3,996,081,651 | 75.6% |
| Calls via PyEval_EvalFrame (total) | 1,288,381,364 | 24.4% |
| Calls via PyEval_EvalFrame (vector) | 734,031,345 | 13.9% |
| Calls via PyEval_EvalFrame (generator) | 554,350,019 | 10.5% |
| Calls via PyEval_EvalFrame (legacy) | 3,964,140 | 0.1% |
| Calls via PyEval_EvalFrame (function vectorcall) | 730,065,885 | 13.8% |
| Calls via PyEval_EvalFrame (build class) | 1,320 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 189,088,097 | 3.6% |
| Calls via PyEval_EvalFrame (function ex) | 9,425,564 | 0.2% |
| Calls via PyEval_EvalFrame (api) | 112,944,230 | 2.1% |
| Calls via PyEval_EvalFrame (method) | 93,801,381 | 1.8% |
| Frames pushed | 4,276,346,421 | 80.9% |
| Frame objects created | 58,919,869 | 1.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 4,193,112,473 | 35.7% |
| Frees to freelist | 4,197,057,390 |  |
| Allocations | 7,536,909,165 | 64.3% |
| Allocations to 512 bytes | 7,455,923,715 | 63.6% |
| Allocations to 4 kbytes | 65,952,074 | 0.6% |
| Allocations over 4 kbytes | 15,033,376 | 0.1% |
| Frees | 7,782,946,589 |  |
| New values | 124,465,442 |  |
| Interpreter increfs | 56,608,134,664 | 76.3% |
| Interpreter decrefs | 65,644,373,402 | 77.0% |
| Increfs | 17,571,457,241 | 23.7% |
| Decrefs | 19,625,588,939 | 23.0% |
| Materialize dict (on request) | 3,684,060 | 3.0% |
| Materialize dict (new key) | 58,440 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Method cache hits | 1,920,378,596 |  |
| Method cache misses | 85,240,497 |  |
| Method cache collisions | 90,171,831 |  |
| Method cache dunder hits | 2,232,805,559 |  |
| Method cache dunder misses | 4,972,974 |  |


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

| | Count | 
|---|---:|
| Number of data files | 8,523 |


</details>

---
Stats gathered on: 2023-05-25
