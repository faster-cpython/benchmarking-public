
# Pystats results

- benchmark: concurrent_imap
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 98,877,525 | 17.6% | 17.6% |  |
| RESUME_CHECK | 36,591,277 | 6.5% | 24.1% | 0.0% |
| STORE_FAST | 29,113,951 | 5.2% | 29.3% |  |
| LOAD_ATTR_INSTANCE_VALUE | 24,091,388 | 4.3% | 33.6% | 0.9% |
| POP_TOP | 23,776,258 | 4.2% | 37.8% |  |
| RETURN_VALUE | 21,600,864 | 3.8% | 41.7% |  |
| POP_JUMP_IF_FALSE | 18,781,161 | 3.3% | 45.0% |  |
| JUMP_BACKWARD | 17,899,771 | 3.2% | 48.2% |  |
| LOAD_GLOBAL_MODULE | 16,569,602 | 2.9% | 51.1% | 0.0% |
| LOAD_FAST_LOAD_FAST | 15,305,209 | 2.7% | 53.9% |  |
| LOAD_CONST | 15,304,859 | 2.7% | 56.6% |  |
| CALL_PY_EXACT_ARGS | 12,141,328 | 2.2% | 58.7% | 0.0% |
| INTERPRETER_EXIT | 11,805,739 | 2.1% | 60.8% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 10,872,542 | 1.9% | 62.8% | 0.8% |
| CALL | 10,828,277 | 1.9% | 64.7% |  |
| LOAD_ATTR | 10,091,123 | 1.8% | 66.5% |  |
| FOR_ITER_LIST | 9,874,712 | 1.8% | 68.3% |  |
| NOP | 9,805,966 | 1.7% | 70.0% |  |
| RETURN_CONST | 9,097,711 | 1.6% | 71.6% |  |
| LOAD_GLOBAL_BUILTIN | 8,498,964 | 1.5% | 73.1% | 0.0% |
| PUSH_NULL | 7,325,095 | 1.3% | 74.4% |  |
| COPY | 7,144,776 | 1.3% | 75.7% |  |
| YIELD_VALUE | 6,913,660 | 1.2% | 76.9% |  |
| TO_BOOL_BOOL | 6,868,690 | 1.2% | 78.2% |  |
| BINARY_OP | 6,819,002 | 1.2% | 79.4% |  |
| STORE_FAST_LOAD_FAST | 6,464,820 | 1.2% | 80.5% |  |
| FOR_ITER_GEN | 6,347,440 | 1.1% | 81.7% |  |
| LOAD_ATTR_METHOD_NO_DICT | 6,339,606 | 1.1% | 82.8% |  |
| TO_BOOL_INT | 5,032,174 | 0.9% | 83.7% |  |
| POP_JUMP_IF_NOT_NONE | 4,968,428 | 0.9% | 84.6% |  |
| STORE_FAST_STORE_FAST | 4,796,392 | 0.9% | 85.4% |  |
| STORE_ATTR_INSTANCE_VALUE | 4,343,584 | 0.8% | 86.2% | 5.6% |
| BUILD_TUPLE | 4,243,075 | 0.8% | 87.0% |  |
| COMPARE_OP_INT | 3,683,668 | 0.7% | 87.6% | 0.2% |
| LOAD_ATTR_MODULE | 3,534,524 | 0.6% | 88.2% | 0.0% |
| CALL_PY_WITH_DEFAULTS | 2,870,309 | 0.5% | 88.7% |  |
| POP_JUMP_IF_TRUE | 2,720,083 | 0.5% | 89.2% |  |
| SWAP | 2,552,361 | 0.5% | 89.7% |  |
| CALL_FUNCTION_EX | 2,413,976 | 0.4% | 90.1% |  |
| GET_ITER | 2,325,393 | 0.4% | 90.5% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 2,109,112 | 0.4% | 90.9% |  |
| CALL_BUILTIN_CLASS | 1,963,440 | 0.3% | 91.3% |  |
| BEFORE_WITH | 1,836,860 | 0.3% | 91.6% |  |
| CALL_BUILTIN_FAST | 1,789,845 | 0.3% | 91.9% |  |
| LOAD_DEREF | 1,777,591 | 0.3% | 92.2% |  |
| COPY_FREE_VARS | 1,727,531 | 0.3% | 92.5% |  |
| CONTAINS_OP | 1,712,082 | 0.3% | 92.8% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,667,948 | 0.3% | 93.1% |  |
| JUMP_FORWARD | 1,666,825 | 0.3% | 93.4% |  |
| BUILD_MAP | 1,656,929 | 0.3% | 93.7% |  |
| LOAD_SUPER_ATTR_METHOD | 1,631,211 | 0.3% | 94.0% |  |
| UNARY_INVERT | 1,627,288 | 0.3% | 94.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,617,417 | 0.3% | 94.6% | 0.0% |
| TO_BOOL | 1,580,592 | 0.3% | 94.9% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,482,309 | 0.3% | 95.1% |  |
| COMPARE_OP_STR | 1,475,414 | 0.3% | 95.4% |  |
| BUILD_LIST | 1,467,782 | 0.3% | 95.7% |  |
| FOR_ITER | 1,305,260 | 0.2% | 95.9% |  |
| STORE_SUBSCR_DICT | 1,224,928 | 0.2% | 96.1% |  |
| UNPACK_SEQUENCE_TUPLE | 1,169,542 | 0.2% | 96.3% |  |
| CALL_ISINSTANCE | 1,152,822 | 0.2% | 96.5% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,137,982 | 0.2% | 96.7% | 0.0% |
| BINARY_OP_ADD_INT | 1,112,441 | 0.2% | 96.9% |  |
| POP_JUMP_IF_NONE | 1,105,785 | 0.2% | 97.1% |  |
| EXIT_INIT_CHECK | 1,020,838 | 0.2% | 97.3% |  |
| CALL_ALLOC_AND_ENTER_INIT | 1,020,838 | 0.2% | 97.5% |  |
| LOAD_ATTR_PROPERTY | 999,330 | 0.2% | 97.7% | 1.2% |
| CALL_METHOD_DESCRIPTOR_O | 968,764 | 0.2% | 97.8% | 0.0% |
| LOAD_FAST_CHECK | 823,532 | 0.1% | 98.0% |  |
| LIST_APPEND | 799,895 | 0.1% | 98.1% |  |
| FOR_ITER_RANGE | 741,639 | 0.1% | 98.3% |  |
| LOAD_FAST_AND_CLEAR | 736,797 | 0.1% | 98.4% |  |
| BINARY_SUBSCR | 637,262 | 0.1% | 98.5% |  |
| CALL_LEN | 619,885 | 0.1% | 98.6% |  |
| CALL_TUPLE_1 | 583,120 | 0.1% | 98.7% |  |
| COMPARE_OP | 567,134 | 0.1% | 98.8% |  |
| DICT_MERGE | 564,260 | 0.1% | 98.9% |  |
| TO_BOOL_LIST | 530,849 | 0.1% | 99.0% |  |
| BINARY_SUBSCR_LIST_INT | 470,622 | 0.1% | 99.1% |  |
| LIST_EXTEND | 460,502 | 0.1% | 99.2% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 409,108 | 0.1% | 99.2% |  |
| CALL_KW | 346,318 | 0.1% | 99.3% |  |
| BINARY_OP_SUBTRACT_INT | 330,586 | 0.1% | 99.4% |  |
| CALL_LIST_APPEND | 258,053 | 0.0% | 99.4% |  |
| BINARY_OP_ADD_FLOAT | 246,798 | 0.0% | 99.5% |  |
| UNARY_NOT | 246,047 | 0.0% | 99.5% |  |
| TO_BOOL_NONE | 240,436 | 0.0% | 99.5% | 0.1% |
| BINARY_OP_SUBTRACT_FLOAT | 230,196 | 0.0% | 99.6% |  |
| CALL_BUILTIN_O | 154,400 | 0.0% | 99.6% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 142,386 | 0.0% | 99.6% | 4.5% |
| MAKE_CELL | 137,900 | 0.0% | 99.7% |  |
| STORE_DEREF | 137,660 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_DICT | 114,880 | 0.0% | 99.7% |  |
| BINARY_OP_MULTIPLY_FLOAT | 112,600 | 0.0% | 99.7% |  |
| BINARY_SUBSCR_STR_INT | 112,600 | 0.0% | 99.7% |  |
| STORE_ATTR | 100,859 | 0.0% | 99.8% |  |
| LOAD_ATTR_SLOT | 99,760 | 0.0% | 99.8% |  |
| STORE_ATTR_SLOT | 97,980 | 0.0% | 99.8% |  |
| LOAD_ATTR_CLASS | 91,522 | 0.0% | 99.8% |  |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 0.0% | 99.8% |  |
| DELETE_ATTR | 86,385 | 0.0% | 99.8% |  |
| DELETE_SUBSCR | 78,210 | 0.0% | 99.9% |  |
| MAKE_FUNCTION | 63,680 | 0.0% | 99.9% |  |
| FORMAT_SIMPLE | 55,680 | 0.0% | 99.9% |  |
| POP_EXCEPT | 49,402 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 49,402 | 0.0% | 99.9% |  |
| IS_OP | 46,986 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 43,642 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 43,340 | 0.0% | 99.9% |  |
| BUILD_STRING | 41,600 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 39,160 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 39,040 | 0.0% | 99.9% |  |
| IMPORT_NAME | 33,760 | 0.0% | 99.9% |  |
| IMPORT_FROM | 33,420 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 31,257 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 30,220 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 28,160 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 27,480 | 0.0% | 100.0% |  |
| BINARY_SLICE | 19,820 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 18,900 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 17,844 | 0.0% | 100.0% |  |
| RERAISE | 17,280 | 0.0% | 100.0% |  |
| CALL_STR_1 | 11,900 | 0.0% | 100.0% |  |
| END_FOR | 11,520 | 0.0% | 100.0% |  |
| STORE_NAME | 7,480 | 0.0% | 100.0% |  |
| RESUME | 5,980 | 0.0% | 100.0% | 0.0% |
| RAISE_VARARGS | 5,780 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 5,760 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 3,840 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 2,800 | 0.0% | 100.0% |  |
| LOAD_NAME | 2,200 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 1,440 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 946 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 920 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 560 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR | 520 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 280 | 0.0% | 100.0% |  |
| CALL_INTRINSIC_1 | 160 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 140 | 0.0% | 100.0% | 14.3% |


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 pairs </summary>

|Pair | Count | Self | Cumulative | 
|---|---:|---:|---:|
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 21,804,876 | 3.9% | 3.9% |
| RESUME_CHECK LOAD_FAST | 20,504,667 | 3.6% | 7.5% |
| STORE_FAST LOAD_FAST | 12,607,303 | 2.2% | 9.8% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 12,094,728 | 2.2% | 11.9% |
| CACHE RESUME_CHECK | 11,691,864 | 2.1% | 14.0% |
| LOAD_FAST RETURN_VALUE | 10,539,259 | 1.9% | 15.9% |
| RETURN_VALUE INTERPRETER_EXIT | 10,356,465 | 1.8% | 17.7% |
| POP_TOP JUMP_BACKWARD | 8,667,279 | 1.5% | 19.3% |
| JUMP_BACKWARD FOR_ITER_LIST | 7,861,630 | 1.4% | 20.7% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 7,791,294 | 1.4% | 22.1% |
| LOAD_FAST LOAD_ATTR | 7,765,558 | 1.4% | 23.4% |
| POP_JUMP_IF_FALSE LOAD_FAST | 7,724,639 | 1.4% | 24.8% |
| POP_TOP LOAD_FAST | 7,308,575 | 1.3% | 26.1% |
| RESUME_CHECK POP_TOP | 6,913,520 | 1.2% | 27.3% |
| RETURN_CONST POP_TOP | 6,417,298 | 1.1% | 28.5% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,335,920 | 1.1% | 29.6% |
| YIELD_VALUE STORE_FAST | 6,335,920 | 1.1% | 30.7% |
| FOR_ITER_GEN RESUME_CHECK | 6,335,920 | 1.1% | 31.9% |
| NOP LOAD_FAST | 6,244,400 | 1.1% | 33.0% |
| FOR_ITER_LIST STORE_FAST_LOAD_FAST | 5,760,060 | 1.0% | 34.0% |
| STORE_FAST JUMP_BACKWARD | 5,760,000 | 1.0% | 35.0% |
| STORE_FAST_LOAD_FAST YIELD_VALUE | 5,760,000 | 1.0% | 36.1% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 5,517,429 | 1.0% | 37.0% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 5,475,685 | 1.0% | 38.0% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 5,032,034 | 0.9% | 38.9% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 5,030,879 | 0.9% | 39.8% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 4,773,564 | 0.8% | 40.7% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 4,690,534 | 0.8% | 41.5% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,921,567 | 0.7% | 42.2% |
| LOAD_FAST LOAD_CONST | 3,872,304 | 0.7% | 42.9% |
| LOAD_CONST LOAD_CONST | 3,784,587 | 0.7% | 43.6% |
| STORE_FAST NOP | 3,754,715 | 0.7% | 44.2% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,679,866 | 0.7% | 44.9% |
| LOAD_FAST PUSH_NULL | 3,669,913 | 0.7% | 45.5% |
| LOAD_GLOBAL_MODULE BINARY_OP | 3,650,739 | 0.6% | 46.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 3,643,728 | 0.6% | 46.8% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,543,913 | 0.6% | 47.5% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 3,531,339 | 0.6% | 48.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 3,531,284 | 0.6% | 48.7% |
| PUSH_NULL LOAD_FAST | 3,453,613 | 0.6% | 49.3% |
| LOAD_ATTR LOAD_FAST | 3,368,875 | 0.6% | 49.9% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 3,280,285 | 0.6% | 50.5% |
| POP_JUMP_IF_FALSE RETURN_CONST | 3,084,412 | 0.5% | 51.1% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 3,021,886 | 0.5% | 51.6% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,989,754 | 0.5% | 52.1% |
| BINARY_OP COPY | 2,762,190 | 0.5% | 52.6% |
| COPY TO_BOOL_INT | 2,761,870 | 0.5% | 53.1% |
| COPY STORE_FAST | 2,630,400 | 0.5% | 53.6% |
| STORE_FAST COPY | 2,629,760 | 0.5% | 54.0% |
| CALL STORE_FAST | 2,596,272 | 0.5% | 54.5% |
| LOAD_CONST CALL | 2,587,494 | 0.5% | 55.0% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 2,564,755 | 0.5% | 55.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 2,457,137 | 0.4% | 55.9% |
| CALL RETURN_VALUE | 2,437,862 | 0.4% | 56.3% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,400,946 | 0.4% | 56.7% |
| LOAD_ATTR_MODULE PUSH_NULL | 2,244,084 | 0.4% | 57.1% |
| CALL POP_TOP | 2,234,085 | 0.4% | 57.5% |
| RETURN_VALUE STORE_FAST | 2,221,075 | 0.4% | 57.9% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 2,118,636 | 0.4% | 58.3% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 2,102,052 | 0.4% | 58.7% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,078,149 | 0.4% | 59.0% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,021,099 | 0.4% | 59.4% |
| PUSH_NULL CALL | 2,016,794 | 0.4% | 59.8% |
| LOAD_CONST COMPARE_OP_INT | 2,002,708 | 0.4% | 60.1% |
| LOAD_FAST_LOAD_FAST LOAD_FAST_LOAD_FAST | 1,998,633 | 0.4% | 60.5% |
| RETURN_VALUE RETURN_VALUE | 1,906,050 | 0.3% | 60.8% |
| POP_TOP RETURN_CONST | 1,903,309 | 0.3% | 61.1% |
| LOAD_FAST_LOAD_FAST CALL | 1,875,155 | 0.3% | 61.5% |
| LOAD_FAST CALL_FUNCTION_EX | 1,849,696 | 0.3% | 61.8% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,849,119 | 0.3% | 62.1% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 1,824,661 | 0.3% | 62.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,792,522 | 0.3% | 62.8% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 1,735,407 | 0.3% | 63.1% |
| NOP LOAD_GLOBAL_MODULE | 1,734,086 | 0.3% | 63.4% |
| POP_TOP LOAD_CONST | 1,733,271 | 0.3% | 63.7% |
| COPY_FREE_VARS RESUME_CHECK | 1,726,871 | 0.3% | 64.0% |
| LOAD_DEREF LOAD_FAST | 1,721,251 | 0.3% | 64.3% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 1,720,731 | 0.3% | 64.6% |
| CONTAINS_OP POP_JUMP_IF_FALSE | 1,711,462 | 0.3% | 64.9% |
| LOAD_ATTR_INSTANCE_VALUE CONTAINS_OP | 1,710,803 | 0.3% | 65.2% |
| LOAD_FAST BUILD_TUPLE | 1,701,782 | 0.3% | 65.5% |
| LOAD_CONST LOAD_FAST | 1,668,632 | 0.3% | 65.8% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 1,661,396 | 0.3% | 66.1% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 1,631,011 | 0.3% | 66.4% |
| UNARY_INVERT BINARY_OP | 1,627,288 | 0.3% | 66.7% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 1,611,191 | 0.3% | 67.0% |
| FOR_ITER_LIST STORE_FAST | 1,609,144 | 0.3% | 67.3% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,580,666 | 0.3% | 67.6% |
| GET_ITER FOR_ITER_LIST | 1,537,138 | 0.3% | 67.8% |
| POP_TOP NOP | 1,534,546 | 0.3% | 68.1% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,525,018 | 0.3% | 68.4% |
| LOAD_FAST TO_BOOL | 1,519,072 | 0.3% | 68.7% |
| LOAD_FAST GET_ITER | 1,459,962 | 0.3% | 68.9% |
| RETURN_VALUE POP_TOP | 1,447,037 | 0.3% | 69.2% |
| LOAD_ATTR_METHOD_NO_DICT CALL | 1,440,126 | 0.3% | 69.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,438,300 | 0.3% | 69.7% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,436,391 | 0.3% | 69.9% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,429,340 | 0.3% | 70.2% |
| POP_JUMP_IF_FALSE POP_TOP | 1,425,083 | 0.3% | 70.5% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,411,623 | 0.3% | 70.7% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 18,520 | 93.4% |
| LOAD_CONST | 980 | 4.9% |
| LOAD_FAST | 280 | 1.4% |
| BINARY_OP | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,900 | 95.4% |
| BUILD_TUPLE | 280 | 1.4% |
| LOAD_DEREF | 280 | 1.4% |
| STORE_FAST | 280 | 1.4% |
| CALL | 80 | 0.4% |


</details>

### CACHE

<details>
<summary> Successors and predecessors for CACHE </summary>

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,691,864 | 99.0% |
| COPY_FREE_VARS | 109,900 | 0.9% |
| POP_TOP | 7,460 | 0.1% |
| RESUME | 2,280 | 0.0% |
| MAKE_CELL | 20 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,253,736 | 68.3% |
| RETURN_VALUE | 476,549 | 25.9% |
| LOAD_GLOBAL_MODULE | 82,435 | 4.5% |
| LOAD_FAST | 17,280 | 0.9% |
| CALL | 6,360 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,354,651 | 73.7% |
| STORE_FAST | 482,209 | 26.3% |


</details>

### BINARY_OP_INPLACE_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_INPLACE_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_STRING | 27,440 | 99.9% |
| BINARY_OP | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 27,480 | 100.0% |


</details>

### BINARY_SUBSCR

<details>
<summary> Successors and predecessors for BINARY_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 576,080 | 90.4% |
| LOAD_CONST | 60,222 | 9.5% |
| BINARY_SUBSCR | 880 | 0.1% |
| CALL | 40 | 0.0% |
| CALL_BUILTIN_O | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 575,920 | 90.4% |
| STORE_FAST | 59,942 | 9.4% |
| BINARY_SUBSCR | 880 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 38,482 | 88.2% |
| LOAD_ATTR_MODULE | 5,100 | 11.7% |
| LOAD_GLOBAL | 40 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 43,642 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,895 | 48.5% |
| CALL | 27,515 | 35.2% |
| LOAD_ATTR_INSTANCE_VALUE | 12,718 | 16.3% |
| LOAD_ATTR | 82 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,795 | 77.7% |
| RETURN_CONST | 10,235 | 13.1% |
| LOAD_FAST | 7,040 | 9.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.2% |


</details>

### END_FOR

<details>
<summary> Successors and predecessors for END_FOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 11,520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| NOP | 5,760 | 50.0% |
| LOAD_FAST | 5,760 | 50.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,020,838 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,020,838 | 100.0% |


</details>

### FORMAT_SIMPLE

<details>
<summary> Successors and predecessors for FORMAT_SIMPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CONVERT_VALUE | 28,160 | 50.6% |
| LOAD_FAST | 27,520 | 49.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 41,600 | 74.7% |
| BUILD_STRING | 14,080 | 25.3% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,459,962 | 62.8% |
| STORE_FAST_LOAD_FAST | 576,000 | 24.8% |
| CALL_BUILTIN_CLASS | 261,891 | 11.3% |
| CALL | 14,340 | 0.6% |
| RETURN_VALUE | 5,760 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 1,537,138 | 66.1% |
| LOAD_FAST_AND_CLEAR | 490,604 | 21.1% |
| FOR_ITER_RANGE | 254,975 | 11.0% |
| FOR_ITER | 12,116 | 0.5% |
| FOR_ITER_TUPLE | 11,740 | 0.5% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,356,465 | 87.7% |
| RETURN_CONST | 871,534 | 7.4% |
| YIELD_VALUE | 577,740 | 4.9% |


</details>

### LOAD_BUILD_CLASS

<details>
<summary> Successors and predecessors for LOAD_BUILD_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 500 | 89.3% |
| POP_TOP | 60 | 10.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 560 | 100.0% |


</details>

### MAKE_FUNCTION

<details>
<summary> Successors and predecessors for MAKE_FUNCTION </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 63,680 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SET_FUNCTION_ATTRIBUTE | 39,040 | 61.3% |
| STORE_FAST | 14,080 | 22.1% |
| LOAD_FAST | 7,040 | 11.1% |
| STORE_NAME | 2,480 | 3.9% |
| LOAD_CONST | 560 | 0.9% |


</details>

### NOP

<details>
<summary> Successors and predecessors for NOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 3,754,715 | 38.3% |
| POP_TOP | 1,534,546 | 15.6% |
| RESUME_CHECK | 1,336,602 | 13.6% |
| POP_JUMP_IF_FALSE | 1,309,875 | 13.4% |
| JUMP_BACKWARD | 1,088,000 | 11.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,244,400 | 63.7% |
| LOAD_GLOBAL_MODULE | 1,734,086 | 17.7% |
| LOAD_GLOBAL_BUILTIN | 702,220 | 7.2% |
| LOAD_FAST_LOAD_FAST | 583,320 | 5.9% |
| LOAD_CONST | 530,020 | 5.4% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_FORWARD | 32,382 | 65.5% |
| COPY | 11,520 | 23.3% |
| POP_TOP | 5,200 | 10.5% |
| STORE_FAST | 280 | 0.6% |
| STORE_SUBSCR_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 32,682 | 66.2% |
| RERAISE | 11,520 | 23.3% |
| JUMP_FORWARD | 5,120 | 10.4% |
| RETURN_CONST | 60 | 0.1% |
| LOAD_FAST | 20 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,913,520 | 29.1% |
| RETURN_CONST | 6,417,298 | 27.0% |
| CALL | 2,234,085 | 9.4% |
| RETURN_VALUE | 1,447,037 | 6.1% |
| POP_JUMP_IF_FALSE | 1,425,083 | 6.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 8,667,279 | 36.5% |
| LOAD_FAST | 7,308,575 | 30.7% |
| RETURN_CONST | 1,903,309 | 8.0% |
| LOAD_CONST | 1,733,271 | 7.3% |
| NOP | 1,534,546 | 6.5% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 38,102 | 77.1% |
| RERAISE | 5,760 | 11.7% |
| CALL_KW | 5,120 | 10.4% |
| BINARY_SUBSCR_DICT | 300 | 0.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 38,442 | 77.8% |
| WITH_EXCEPT_START | 5,760 | 11.7% |
| LOAD_GLOBAL_MODULE | 5,080 | 10.3% |
| LOAD_GLOBAL | 120 | 0.2% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,669,913 | 50.1% |
| LOAD_ATTR_MODULE | 2,244,084 | 30.6% |
| LOAD_ATTR | 1,284,378 | 17.5% |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 1.2% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,453,613 | 47.1% |
| CALL | 2,016,794 | 27.5% |
| LOAD_FAST_LOAD_FAST | 1,396,344 | 19.1% |
| LOAD_CONST | 321,018 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 64,706 | 0.9% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 18,420 | 97.5% |
| COPY_FREE_VARS | 340 | 1.8% |
| CALL | 140 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 5,760 | 30.5% |
| LOAD_FAST | 5,760 | 30.5% |
| STORE_FAST | 5,760 | 30.5% |
| CALL_METHOD_DESCRIPTOR_O | 1,300 | 6.9% |
| CALL | 320 | 1.7% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,539,259 | 48.8% |
| CALL | 2,437,862 | 11.3% |
| RETURN_VALUE | 1,906,050 | 8.8% |
| LOAD_ATTR_INSTANCE_VALUE | 1,525,018 | 7.1% |
| CALL_FUNCTION_EX | 1,265,516 | 5.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 10,356,465 | 47.9% |
| STORE_FAST | 2,221,075 | 10.3% |
| RETURN_VALUE | 1,906,050 | 8.8% |
| POP_TOP | 1,447,037 | 6.7% |
| LOAD_FAST_LOAD_FAST | 1,134,902 | 5.3% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 14,080 | 45.0% |
| LOAD_FAST | 10,437 | 33.4% |
| LOAD_ATTR_INSTANCE_VALUE | 5,800 | 18.6% |
| STORE_SUBSCR | 660 | 2.1% |
| LOAD_ATTR | 200 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 19,960 | 63.9% |
| LOAD_GLOBAL_MODULE | 10,200 | 32.6% |
| STORE_SUBSCR | 660 | 2.1% |
| STORE_SUBSCR_DICT | 258 | 0.8% |
| LOAD_GLOBAL | 80 | 0.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,519,072 | 96.1% |
| LOAD_ATTR_INSTANCE_VALUE | 53,490 | 3.4% |
| TO_BOOL | 3,663 | 0.2% |
| LOAD_ATTR | 882 | 0.1% |
| RETURN_VALUE | 765 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 834,895 | 52.8% |
| POP_JUMP_IF_FALSE | 738,993 | 46.8% |
| TO_BOOL | 3,663 | 0.2% |
| TO_BOOL_BOOL | 2,161 | 0.1% |
| TO_BOOL_NONE | 360 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,134,902 | 69.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 492,306 | 30.3% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,627,288 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 246,007 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 246,047 | 100.0% |


</details>

### WITH_EXCEPT_START

<details>
<summary> Successors and predecessors for WITH_EXCEPT_START </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_NONE | 5,680 | 98.6% |
| TO_BOOL | 80 | 1.4% |


</details>

### BINARY_OP

<details>
<summary> Successors and predecessors for BINARY_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,650,739 | 53.5% |
| UNARY_INVERT | 1,627,288 | 23.9% |
| POP_JUMP_IF_FALSE | 1,134,902 | 16.6% |
| LOAD_ATTR | 260,293 | 3.8% |
| LOAD_FAST_LOAD_FAST | 84,160 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,762,190 | 40.5% |
| STORE_FAST | 1,395,515 | 20.5% |
| TO_BOOL_INT | 1,134,962 | 16.6% |
| UNARY_INVERT | 1,134,902 | 16.6% |
| BUILD_TUPLE | 246,193 | 3.6% |


</details>

### BUILD_CONST_KEY_MAP

<details>
<summary> Successors and predecessors for BUILD_CONST_KEY_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 280 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 140 | 50.0% |
| STORE_FAST | 140 | 50.0% |


</details>

### BUILD_LIST

<details>
<summary> Successors and predecessors for BUILD_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 490,604 | 33.4% |
| JUMP_FORWARD | 476,309 | 32.5% |
| LOAD_FAST | 246,858 | 16.8% |
| POP_TOP | 229,471 | 15.6% |
| STORE_ATTR_INSTANCE_VALUE | 10,660 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 493,549 | 33.6% |
| SWAP | 490,604 | 33.4% |
| STORE_FAST | 477,769 | 32.6% |
| RETURN_VALUE | 5,120 | 0.3% |
| COMPARE_OP | 280 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 576,000 | 34.8% |
| LOAD_FAST | 529,560 | 32.0% |
| RESUME_CHECK | 486,509 | 29.4% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 2.1% |
| POP_JUMP_IF_NOT_NONE | 17,280 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,063,629 | 64.2% |
| BUILD_TUPLE | 576,020 | 34.8% |
| STORE_FAST | 17,280 | 1.0% |


</details>

### BUILD_STRING

<details>
<summary> Successors and predecessors for BUILD_STRING </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 27,520 | 66.2% |
| FORMAT_SIMPLE | 14,080 | 33.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_INPLACE_ADD_UNICODE | 27,440 | 66.0% |
| RETURN_VALUE | 14,080 | 33.8% |
| BINARY_OP | 80 | 0.2% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,701,782 | 40.1% |
| LOAD_FAST_LOAD_FAST | 1,160,320 | 27.3% |
| BUILD_MAP | 576,020 | 13.6% |
| RETURN_VALUE | 512,000 | 12.1% |
| BINARY_OP | 246,193 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 1,152,100 | 27.2% |
| CALL | 1,136,462 | 26.8% |
| BUILD_MAP | 576,000 | 13.6% |
| STORE_FAST | 512,000 | 12.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 511,960 | 12.1% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,587,494 | 23.9% |
| PUSH_NULL | 2,016,794 | 18.6% |
| LOAD_FAST_LOAD_FAST | 1,875,155 | 17.3% |
| LOAD_ATTR_METHOD_NO_DICT | 1,440,126 | 13.3% |
| BUILD_TUPLE | 1,136,462 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,596,272 | 24.0% |
| RETURN_VALUE | 2,437,862 | 22.5% |
| POP_TOP | 2,234,085 | 20.6% |
| LOAD_FAST | 1,044,247 | 9.6% |
| TO_BOOL_BOOL | 731,472 | 6.8% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,849,696 | 76.6% |
| DICT_MERGE | 564,260 | 23.4% |
| CALL_INTRINSIC_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,265,516 | 52.4% |
| RESUME_CHECK | 535,040 | 22.2% |
| CALL_BUILTIN_CLASS | 511,960 | 21.2% |
| POP_TOP | 95,360 | 4.0% |
| STORE_FAST | 5,760 | 0.2% |


</details>

### CALL_INTRINSIC_1

<details>
<summary> Successors and predecessors for CALL_INTRINSIC_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LIST_EXTEND | 160 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BUILD_MAP | 140 | 87.5% |
| CALL_FUNCTION_EX | 20 | 12.5% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 346,318 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 276,751 | 79.9% |
| LOAD_FAST | 28,800 | 8.3% |
| RETURN_VALUE | 21,120 | 6.1% |
| STORE_FAST | 14,220 | 4.1% |
| PUSH_EXC_INFO | 5,120 | 1.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 562,822 | 99.2% |
| COMPARE_OP | 1,286 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,090 | 0.2% |
| LOAD_GLOBAL_MODULE | 380 | 0.1% |
| LOAD_FAST | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 563,872 | 99.4% |
| COMPARE_OP | 1,286 | 0.2% |
| COMPARE_OP_INT | 1,176 | 0.2% |
| COMPARE_OP_STR | 440 | 0.1% |
| POP_JUMP_IF_TRUE | 280 | 0.0% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,710,803 | 99.9% |
| LOAD_ATTR_MODULE | 560 | 0.0% |
| LOAD_FAST | 480 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR | 99 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,711,462 | 100.0% |
| POP_JUMP_IF_TRUE | 480 | 0.0% |
| STORE_FAST | 140 | 0.0% |


</details>

### CONVERT_VALUE

<details>
<summary> Successors and predecessors for CONVERT_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_DICT | 14,040 | 49.9% |
| CALL_BUILTIN_FAST | 14,040 | 49.9% |
| BINARY_SUBSCR | 40 | 0.1% |
| CALL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FORMAT_SIMPLE | 28,160 | 100.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 2,762,190 | 38.7% |
| STORE_FAST | 2,629,760 | 36.8% |
| LOAD_CONST | 1,100,800 | 15.4% |
| LOAD_FAST | 590,100 | 8.3% |
| STORE_ATTR_INSTANCE_VALUE | 21,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 2,761,870 | 38.7% |
| STORE_FAST | 2,630,400 | 36.8% |
| STORE_FAST_STORE_FAST | 1,093,760 | 15.3% |
| LOAD_ATTR_INSTANCE_VALUE | 575,883 | 8.1% |
| LOAD_FAST | 28,160 | 0.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 1,134,902 | 65.7% |
| CALL_ALLOC_AND_ENTER_INIT | 476,269 | 27.6% |
| CACHE | 109,900 | 6.4% |
| CALL | 5,940 | 0.3% |
| CALL_PY_EXACT_ARGS | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,726,871 | 100.0% |
| RETURN_GENERATOR | 340 | 0.0% |
| RESUME | 320 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,385 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,590 | 66.7% |
| RETURN_CONST | 27,515 | 31.9% |
| LOAD_GLOBAL_MODULE | 1,240 | 1.4% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### DICT_MERGE

<details>
<summary> Successors and predecessors for DICT_MERGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,700 | 93.9% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 6.1% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 564,260 | 100.0% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,271,224 | 97.4% |
| SWAP | 14,160 | 1.1% |
| GET_ITER | 12,116 | 0.9% |
| LOAD_FAST | 6,060 | 0.5% |
| FOR_ITER | 1,700 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 688,680 | 52.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 581,600 | 44.6% |
| SWAP | 14,080 | 1.1% |
| RETURN_CONST | 11,820 | 0.9% |
| LOAD_GLOBAL_MODULE | 5,680 | 0.4% |


</details>

### IMPORT_FROM

<details>
<summary> Successors and predecessors for IMPORT_FROM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| IMPORT_NAME | 33,080 | 99.0% |
| STORE_NAME | 340 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 32,640 | 97.7% |
| STORE_NAME | 780 | 2.3% |


</details>

### IMPORT_NAME

<details>
<summary> Successors and predecessors for IMPORT_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 33,760 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| IMPORT_FROM | 33,080 | 98.0% |
| STORE_NAME | 680 | 2.0% |


</details>

### IS_OP

<details>
<summary> Successors and predecessors for IS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 27,520 | 58.6% |
| LOAD_FAST | 17,420 | 37.1% |
| LOAD_GLOBAL_MODULE | 2,006 | 4.3% |
| LOAD_GLOBAL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 46,846 | 99.7% |
| POP_JUMP_IF_TRUE | 140 | 0.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,667,279 | 48.4% |
| STORE_FAST | 5,760,000 | 32.2% |
| POP_JUMP_IF_NOT_NONE | 972,002 | 5.4% |
| LIST_APPEND | 799,895 | 4.5% |
| STORE_FAST_STORE_FAST | 581,760 | 3.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 7,861,630 | 43.9% |
| FOR_ITER_GEN | 6,335,920 | 35.4% |
| FOR_ITER | 1,271,224 | 7.1% |
| NOP | 1,088,000 | 6.1% |
| LOAD_GLOBAL_BUILTIN | 575,960 | 3.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,026,635 | 61.6% |
| POP_TOP | 621,970 | 37.3% |
| STORE_ATTR_INSTANCE_VALUE | 7,020 | 0.4% |
| BINARY_SUBSCR_TUPLE_INT | 5,720 | 0.3% |
| POP_EXCEPT | 5,120 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,114,679 | 66.9% |
| BUILD_LIST | 476,309 | 28.6% |
| POP_EXCEPT | 32,382 | 1.9% |
| LOAD_GLOBAL_MODULE | 24,815 | 1.5% |
| LOAD_FAST_LOAD_FAST | 7,320 | 0.4% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 439,042 | 54.9% |
| LOAD_ATTR | 246,213 | 30.8% |
| BINARY_SUBSCR_STR_INT | 112,600 | 14.1% |
| CALL_METHOD_DESCRIPTOR_FAST | 2,000 | 0.3% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 799,895 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 230,891 | 50.1% |
| RETURN_VALUE | 229,471 | 49.8% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_DEREF | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 230,111 | 50.0% |
| STORE_FAST | 229,471 | 49.8% |
| RETURN_VALUE | 640 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |
| STORE_NAME | 120 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,765,558 | 77.0% |
| LOAD_ATTR_INSTANCE_VALUE | 1,792,522 | 17.8% |
| LOAD_GLOBAL_MODULE | 386,391 | 3.8% |
| CALL | 83,860 | 0.8% |
| LOAD_ATTR | 22,736 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,368,875 | 33.4% |
| PUSH_NULL | 1,284,378 | 12.7% |
| STORE_SUBSCR_DICT | 1,134,822 | 11.2% |
| POP_JUMP_IF_NOT_NONE | 1,108,120 | 11.0% |
| STORE_FAST | 720,753 | 7.1% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,872,304 | 25.3% |
| LOAD_CONST | 3,784,587 | 24.7% |
| POP_TOP | 1,733,271 | 11.3% |
| POP_JUMP_IF_FALSE | 908,864 | 5.9% |
| LOAD_ATTR_METHOD_NO_DICT | 740,746 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,784,587 | 24.7% |
| CALL | 2,587,494 | 16.9% |
| COMPARE_OP_INT | 2,002,708 | 13.1% |
| LOAD_FAST | 1,668,632 | 10.9% |
| COPY | 1,100,800 | 7.2% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,720,731 | 96.8% |
| POP_JUMP_IF_NOT_NONE | 27,520 | 1.5% |
| STORE_DEREF | 27,520 | 1.5% |
| STORE_FAST | 440 | 0.0% |
| POP_JUMP_IF_FALSE | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,721,251 | 96.8% |
| POP_JUMP_IF_NOT_NONE | 55,040 | 3.1% |
| PUSH_NULL | 460 | 0.0% |
| LOAD_CONST | 280 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 20,504,667 | 20.7% |
| STORE_FAST | 12,607,303 | 12.8% |
| POP_JUMP_IF_FALSE | 7,724,639 | 7.8% |
| POP_TOP | 7,308,575 | 7.4% |
| NOP | 6,244,400 | 6.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 21,804,876 | 22.1% |
| RETURN_VALUE | 10,539,259 | 10.7% |
| LOAD_ATTR_METHOD_WITH_VALUES | 7,791,294 | 7.9% |
| LOAD_ATTR | 7,765,558 | 7.9% |
| CALL_PY_EXACT_ARGS | 5,030,879 | 5.1% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 490,604 | 66.6% |
| LOAD_FAST_AND_CLEAR | 246,193 | 33.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 490,604 | 66.6% |
| LOAD_FAST_AND_CLEAR | 246,193 | 33.4% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 576,560 | 70.0% |
| POP_JUMP_IF_NONE | 230,116 | 27.9% |
| LOAD_ATTR_CLASS | 16,536 | 2.0% |
| LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 575,920 | 69.9% |
| LOAD_GLOBAL_MODULE | 230,036 | 27.9% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 16,496 | 2.0% |
| POP_JUMP_IF_NOT_NONE | 560 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,564,755 | 16.8% |
| LOAD_FAST_LOAD_FAST | 1,998,633 | 13.1% |
| POP_JUMP_IF_FALSE | 1,429,340 | 9.3% |
| PUSH_NULL | 1,396,344 | 9.1% |
| LOAD_SUPER_ATTR_METHOD | 1,149,182 | 7.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,531,339 | 23.1% |
| LOAD_FAST_LOAD_FAST | 1,998,633 | 13.1% |
| CALL | 1,875,155 | 12.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,661,396 | 10.9% |
| BUILD_TUPLE | 1,160,320 | 7.6% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,000 | 11.2% |
| RESUME_CHECK | 1,720 | 9.6% |
| POP_JUMP_IF_FALSE | 1,711 | 9.6% |
| LOAD_FAST | 1,600 | 9.0% |
| RESUME | 1,520 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 6,820 | 38.2% |
| LOAD_ATTR | 3,322 | 18.6% |
| LOAD_GLOBAL_BUILTIN | 2,740 | 15.4% |
| LOAD_FAST | 2,162 | 12.1% |
| CALL | 740 | 4.1% |


</details>

### LOAD_NAME

<details>
<summary> Successors and predecessors for LOAD_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 820 | 37.3% |
| LOAD_CONST | 600 | 27.3% |
| RESUME | 560 | 25.5% |
| PUSH_NULL | 120 | 5.5% |
| POP_TOP | 80 | 3.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_NAME | 640 | 29.1% |
| CALL | 500 | 22.7% |
| LOAD_ATTR | 420 | 19.1% |
| LOAD_CONST | 380 | 17.3% |
| PUSH_NULL | 220 | 10.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 520 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_SUPER_ATTR_METHOD | 200 | 38.5% |
| PUSH_NULL | 80 | 15.4% |
| LOAD_FAST_LOAD_FAST | 80 | 15.4% |
| LOAD_SUPER_ATTR_ATTR | 80 | 15.4% |
| CALL | 40 | 7.7% |


</details>

### MAKE_CELL

<details>
<summary> Successors and predecessors for MAKE_CELL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| CALL_PY_EXACT_ARGS | 27,800 | 20.2% |
| CACHE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| MAKE_CELL | 110,080 | 79.8% |
| RESUME_CHECK | 27,820 | 20.2% |


</details>

### POP_JUMP_IF_FALSE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_FALSE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 5,032,034 | 26.8% |
| TO_BOOL_BOOL | 4,773,564 | 25.4% |
| COMPARE_OP_INT | 3,679,866 | 19.6% |
| CONTAINS_OP | 1,711,462 | 9.1% |
| COMPARE_OP_STR | 1,436,391 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,724,639 | 41.1% |
| RETURN_CONST | 3,084,412 | 16.4% |
| LOAD_FAST_LOAD_FAST | 1,429,340 | 7.6% |
| POP_TOP | 1,425,083 | 7.6% |
| LOAD_GLOBAL_MODULE | 1,411,623 | 7.5% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,027,985 | 93.0% |
| LOAD_ATTR_INSTANCE_VALUE | 47,800 | 4.3% |
| LOAD_ATTR | 28,300 | 2.6% |
| RETURN_VALUE | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 283,564 | 25.6% |
| LOAD_FAST | 274,752 | 24.8% |
| NOP | 267,391 | 24.2% |
| LOAD_FAST_CHECK | 230,116 | 20.8% |
| RETURN_CONST | 24,340 | 2.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,400,946 | 48.3% |
| LOAD_ATTR | 1,108,120 | 22.3% |
| LOAD_ATTR_INSTANCE_VALUE | 943,100 | 19.0% |
| RETURN_VALUE | 439,682 | 8.8% |
| LOAD_DEREF | 55,040 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,021,099 | 40.7% |
| RETURN_CONST | 1,109,493 | 22.3% |
| JUMP_BACKWARD | 972,002 | 19.6% |
| NOP | 485,057 | 9.8% |
| LOAD_CONST | 229,751 | 4.6% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,849,119 | 68.0% |
| TO_BOOL | 834,895 | 30.7% |
| TO_BOOL_NONE | 19,700 | 0.7% |
| COMPARE_OP_STR | 10,943 | 0.4% |
| COMPARE_OP_INT | 3,406 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 957,440 | 35.2% |
| LOAD_FAST_LOAD_FAST | 837,693 | 30.8% |
| RETURN_CONST | 738,371 | 27.1% |
| LOAD_GLOBAL_MODULE | 72,230 | 2.7% |
| RETURN_VALUE | 59,902 | 2.2% |


</details>

### RAISE_VARARGS

<details>
<summary> Successors and predecessors for RAISE_VARARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 5,760 | 99.7% |
| CALL_KW | 20 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 5,760 | 100.0% |


</details>

### RERAISE

<details>
<summary> Successors and predecessors for RERAISE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 11,520 | 66.7% |
| POP_JUMP_IF_TRUE | 5,760 | 33.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_EXC_INFO | 5,760 | 50.0% |
| COPY | 5,760 | 50.0% |


</details>

### RETURN_CONST

<details>
<summary> Successors and predecessors for RETURN_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,084,412 | 33.9% |
| STORE_ATTR_INSTANCE_VALUE | 2,118,636 | 23.3% |
| POP_TOP | 1,903,309 | 20.9% |
| POP_JUMP_IF_NOT_NONE | 1,109,493 | 12.2% |
| POP_JUMP_IF_TRUE | 738,371 | 8.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 6,417,298 | 70.5% |
| EXIT_INIT_CHECK | 1,020,838 | 11.2% |
| INTERPRETER_EXIT | 871,534 | 9.6% |
| TO_BOOL_BOOL | 688,779 | 7.6% |
| STORE_FAST | 61,742 | 0.7% |


</details>

### SET_FUNCTION_ATTRIBUTE

<details>
<summary> Successors and predecessors for SET_FUNCTION_ATTRIBUTE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 39,040 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 37,920 | 97.1% |
| STORE_NAME | 780 | 2.0% |
| LOAD_GLOBAL_MODULE | 280 | 0.7% |
| LOAD_FAST | 60 | 0.2% |


</details>

### STORE_ATTR

<details>
<summary> Successors and predecessors for STORE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 58,562 | 58.1% |
| LOAD_FAST_LOAD_FAST | 22,040 | 21.9% |
| LOAD_ATTR_INSTANCE_VALUE | 17,280 | 17.1% |
| STORE_ATTR | 2,520 | 2.5% |
| LOAD_ATTR | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 44,840 | 44.5% |
| LOAD_FAST_LOAD_FAST | 14,760 | 14.6% |
| LOAD_FAST | 13,619 | 13.5% |
| LOAD_CONST | 12,642 | 12.5% |
| LOAD_GLOBAL_BUILTIN | 5,680 | 5.6% |


</details>

### STORE_DEREF

<details>
<summary> Successors and predecessors for STORE_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_MODULE | 55,040 | 40.0% |
| LOAD_GLOBAL_BUILTIN | 27,520 | 20.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 54,960 | 39.9% |
| LOAD_DEREF | 27,520 | 20.0% |
| LOAD_FAST | 27,520 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 27,480 | 20.0% |
| LOAD_GLOBAL | 120 | 0.1% |


</details>

### STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,335,920 | 21.8% |
| COPY | 2,630,400 | 9.0% |
| CALL | 2,596,272 | 8.9% |
| RETURN_VALUE | 2,221,075 | 7.6% |
| FOR_ITER_LIST | 1,609,144 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,607,303 | 43.3% |
| JUMP_BACKWARD | 5,760,000 | 19.8% |
| NOP | 3,754,715 | 12.9% |
| COPY | 2,629,760 | 9.0% |
| LOAD_GLOBAL_BUILTIN | 1,159,615 | 4.0% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 5,760,060 | 89.1% |
| FOR_ITER | 688,680 | 10.7% |
| COPY | 14,080 | 0.2% |
| FOR_ITER_TUPLE | 2,000 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 5,760,000 | 89.1% |
| GET_ITER | 576,000 | 8.9% |
| LOAD_FAST | 112,640 | 1.7% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 0.2% |
| TO_BOOL_STR | 2,000 | 0.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 2,102,052 | 43.8% |
| COPY | 1,093,760 | 22.8% |
| UNPACK_SEQUENCE_TUPLE | 1,088,220 | 22.7% |
| STORE_FAST_STORE_FAST | 512,000 | 10.7% |
| UNPACK_SEQUENCE | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,580,666 | 33.0% |
| STORE_FAST | 1,088,280 | 22.7% |
| LOAD_FAST_LOAD_FAST | 1,017,766 | 21.2% |
| JUMP_BACKWARD | 581,760 | 12.1% |
| STORE_FAST_STORE_FAST | 512,000 | 10.7% |


</details>

### STORE_NAME

<details>
<summary> Successors and predecessors for STORE_NAME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAKE_FUNCTION | 2,480 | 33.2% |
| CALL | 1,200 | 16.0% |
| IMPORT_FROM | 780 | 10.4% |
| SET_FUNCTION_ATTRIBUTE | 780 | 10.4% |
| IMPORT_NAME | 680 | 9.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 4,640 | 62.0% |
| LOAD_NAME | 820 | 11.0% |
| RETURN_CONST | 700 | 9.4% |
| LOAD_BUILD_CLASS | 500 | 6.7% |
| POP_TOP | 440 | 5.9% |


</details>

### SWAP

<details>
<summary> Successors and predecessors for SWAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_ADD_INT | 575,941 | 22.6% |
| BUILD_LIST | 490,604 | 19.2% |
| LOAD_FAST_AND_CLEAR | 490,604 | 19.2% |
| FOR_ITER_LIST | 475,664 | 18.6% |
| LOAD_FAST | 257,916 | 10.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 575,883 | 22.6% |
| LOAD_CONST | 504,109 | 19.8% |
| BUILD_LIST | 490,604 | 19.2% |
| STORE_FAST | 490,604 | 19.2% |
| FOR_ITER_LIST | 475,584 | 18.6% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 260 | 28.3% |
| FOR_ITER | 240 | 26.1% |
| LOAD_FAST | 120 | 13.0% |
| RETURN_VALUE | 80 | 8.7% |
| LOAD_FAST_CHECK | 80 | 8.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 360 | 39.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 340 | 37.0% |
| UNPACK_SEQUENCE_TUPLE | 100 | 10.9% |
| LOAD_FAST | 40 | 4.3% |
| STORE_FAST | 40 | 4.3% |


</details>

### YIELD_VALUE

<details>
<summary> Successors and predecessors for YIELD_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,000 | 83.3% |
| BUILD_TUPLE | 1,152,100 | 16.7% |
| CALL_STR_1 | 1,260 | 0.0% |
| CALL | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,335,920 | 91.6% |
| INTERPRETER_EXIT | 577,740 | 8.4% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,820 | 47.2% |
| CACHE | 2,280 | 38.1% |
| COPY_FREE_VARS | 320 | 5.4% |
| CALL_KW | 200 | 3.3% |
| POP_TOP | 140 | 2.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,880 | 48.2% |
| LOAD_GLOBAL | 1,520 | 25.4% |
| LOAD_NAME | 560 | 9.4% |
| NOP | 280 | 4.7% |
| LOAD_CONST | 240 | 4.0% |


</details>

### BINARY_OP_ADD_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 246,758 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 246,798 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,093,803 | 98.3% |
| LOAD_FAST_LOAD_FAST | 18,480 | 1.7% |
| BINARY_OP | 158 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 575,941 | 51.8% |
| STORE_FAST | 511,980 | 46.0% |
| BINARY_SLICE | 18,520 | 1.7% |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,680 | 0.5% |
| LOAD_CONST | 280 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 32.3% |
| CALL_METHOD_DESCRIPTOR_O | 1,240 | 32.3% |
| LOAD_FAST_LOAD_FAST | 960 | 25.0% |
| BINARY_SUBSCR_LIST_INT | 280 | 7.3% |
| LOAD_FAST | 80 | 2.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,740 | 45.3% |
| LOAD_CONST | 1,260 | 32.8% |
| CALL | 480 | 12.5% |
| STORE_FAST | 360 | 9.4% |


</details>

### BINARY_OP_MULTIPLY_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_MULTIPLY_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 112,560 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| CALL | 40 | 0.0% |


</details>

### BINARY_OP_SUBTRACT_FLOAT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 230,036 | 99.9% |
| BINARY_OP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 230,196 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 264,884 | 80.1% |
| LOAD_CONST | 59,822 | 18.1% |
| CALL_LEN | 5,680 | 1.7% |
| BINARY_OP | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 324,866 | 98.3% |
| CALL_BUILTIN_CLASS | 5,680 | 1.7% |
| CALL | 40 | 0.0% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 99,860 | 86.9% |
| LOAD_CONST | 14,280 | 12.4% |
| LOAD_FAST | 700 | 0.6% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 99,860 | 86.9% |
| CONVERT_VALUE | 14,040 | 12.2% |
| STORE_FAST | 400 | 0.3% |
| PUSH_EXC_INFO | 300 | 0.3% |
| LOAD_FAST | 140 | 0.1% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 458,862 | 97.5% |
| LOAD_CONST | 11,640 | 2.5% |
| BINARY_SUBSCR | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 458,902 | 97.5% |
| LOAD_CONST | 11,440 | 2.4% |
| BINARY_OP_ADD_UNICODE | 280 | 0.1% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_O | 112,560 | 100.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LIST_APPEND | 112,600 | 100.0% |


</details>

### BINARY_SUBSCR_TUPLE_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_TUPLE_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 39,120 | 99.9% |
| BINARY_SUBSCR | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 33,020 | 84.3% |
| JUMP_FORWARD | 5,720 | 14.6% |
| STORE_FAST | 420 | 1.1% |


</details>

### CALL_ALLOC_AND_ENTER_INIT

<details>
<summary> Successors and predecessors for CALL_ALLOC_AND_ENTER_INIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 503,709 | 49.3% |
| LOAD_FAST | 483,429 | 47.4% |
| CALL | 33,420 | 3.3% |
| LOAD_FAST_LOAD_FAST | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 544,569 | 53.3% |
| COPY_FREE_VARS | 476,269 | 46.7% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 64,706 | 45.4% |
| LOAD_FAST | 64,240 | 45.1% |
| LOAD_CONST | 7,480 | 5.3% |
| BINARY_OP_ADD_INT | 5,680 | 4.0% |
| CALL | 160 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 135,986 | 95.5% |
| POP_TOP | 6,280 | 4.4% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 695,760 | 35.4% |
| CALL_FUNCTION_EX | 511,960 | 26.1% |
| LOAD_FAST | 264,538 | 13.5% |
| CALL_BUILTIN_CLASS | 229,391 | 11.7% |
| CALL_LEN | 229,391 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 758,778 | 38.6% |
| STORE_FAST | 696,060 | 35.5% |
| GET_ITER | 261,891 | 13.3% |
| CALL_BUILTIN_CLASS | 229,391 | 11.7% |
| LOAD_FAST | 17,280 | 0.9% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 861,577 | 48.1% |
| LOAD_CONST | 616,822 | 34.5% |
| LOAD_FAST_LOAD_FAST | 173,244 | 9.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 81,282 | 4.5% |
| LOAD_GLOBAL_MODULE | 27,880 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 606,762 | 33.9% |
| STORE_FAST | 583,417 | 32.6% |
| UNPACK_SEQUENCE_TWO_TUPLE | 441,726 | 24.7% |
| UNPACK_SEQUENCE_TUPLE | 81,282 | 4.5% |
| POP_TOP | 14,878 | 0.8% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 519,140 | 45.6% |
| BUILD_TUPLE | 511,960 | 45.0% |
| CALL | 65,006 | 5.7% |
| LOAD_FAST_CHECK | 16,496 | 1.4% |
| LOAD_ATTR | 14,000 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,053,900 | 92.6% |
| RETURN_VALUE | 82,182 | 7.2% |
| LOAD_FAST | 1,260 | 0.1% |
| STORE_FAST | 440 | 0.0% |
| BEFORE_WITH | 140 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 112,560 | 72.9% |
| LOAD_ATTR | 27,440 | 17.8% |
| LOAD_FAST | 14,280 | 9.2% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 112,560 | 72.9% |
| LOAD_FAST | 41,520 | 26.9% |
| STORE_FAST | 140 | 0.1% |
| TO_BOOL_INT | 140 | 0.1% |
| BINARY_SUBSCR | 40 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,152,362 | 100.0% |
| CALL | 180 | 0.0% |
| BUILD_TUPLE | 140 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,152,642 | 100.0% |
| TO_BOOL | 180 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 591,605 | 95.4% |
| LOAD_ATTR_INSTANCE_VALUE | 27,900 | 4.5% |
| CALL | 380 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 344,324 | 55.5% |
| CALL_BUILTIN_CLASS | 229,391 | 37.0% |
| CALL_PY_EXACT_ARGS | 33,160 | 5.3% |
| LOAD_FAST | 5,720 | 0.9% |
| BINARY_OP_SUBTRACT_INT | 5,680 | 0.9% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 246,113 | 95.4% |
| LOAD_FAST | 11,440 | 4.4% |
| LOAD_CONST | 140 | 0.1% |
| LOAD_FAST_CHECK | 140 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 246,153 | 95.4% |
| LOAD_GLOBAL_MODULE | 11,440 | 4.4% |
| NOP | 280 | 0.1% |
| RETURN_CONST | 140 | 0.1% |
| LOAD_GLOBAL | 40 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,611,191 | 99.6% |
| LOAD_GLOBAL_MODULE | 2,280 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,128 | 0.1% |
| LOAD_CONST | 1,240 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,135,182 | 70.2% |
| STORE_FAST | 478,695 | 29.6% |
| LIST_APPEND | 2,000 | 0.1% |
| TO_BOOL_NONE | 1,240 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 37,480 | 86.5% |
| BUILD_TUPLE | 5,680 | 13.1% |
| CALL | 180 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 31,860 | 73.5% |
| LOAD_FAST | 11,480 | 26.5% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,381,511 | 93.2% |
| LOAD_ATTR_METHOD_LAZY_DICT | 97,778 | 6.6% |
| LOAD_ATTR | 2,480 | 0.2% |
| CALL | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 632,993 | 42.7% |
| STORE_FAST | 575,960 | 38.9% |
| LOAD_FAST | 85,060 | 5.7% |
| CALL_BUILTIN_FAST | 81,282 | 5.5% |
| RETURN_VALUE | 51,632 | 3.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 889,326 | 91.8% |
| LOAD_CONST | 33,720 | 3.5% |
| CALL | 29,138 | 3.0% |
| RETURN_VALUE | 14,000 | 1.4% |
| RETURN_GENERATOR | 1,300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 918,604 | 94.8% |
| LOAD_CONST | 33,440 | 3.5% |
| RETURN_VALUE | 14,900 | 1.5% |
| BINARY_OP_ADD_UNICODE | 1,240 | 0.1% |
| STORE_FAST | 280 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 5,475,685 | 45.1% |
| LOAD_FAST | 5,030,879 | 41.4% |
| LOAD_FAST_LOAD_FAST | 819,591 | 6.8% |
| LOAD_SUPER_ATTR_METHOD | 476,229 | 3.9% |
| LOAD_GLOBAL_MODULE | 93,900 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 12,094,728 | 99.6% |
| MAKE_CELL | 27,800 | 0.2% |
| RETURN_GENERATOR | 18,420 | 0.2% |
| COPY_FREE_VARS | 360 | 0.0% |
| PUSH_EXC_INFO | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 1,208,971 | 42.1% |
| LOAD_ATTR_MODULE | 1,134,822 | 39.5% |
| LOAD_FAST | 329,153 | 11.5% |
| LOAD_CONST | 107,482 | 3.7% |
| BINARY_OP | 83,760 | 2.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,735,407 | 60.5% |
| COPY_FREE_VARS | 1,134,902 | 39.5% |


</details>

### CALL_STR_1

<details>
<summary> Successors and predecessors for CALL_STR_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,860 | 99.7% |
| CALL | 40 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,220 | 85.9% |
| YIELD_VALUE | 1,260 | 10.6% |
| STORE_FAST | 280 | 2.4% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 140 | 1.2% |


</details>

### CALL_TUPLE_1

<details>
<summary> Successors and predecessors for CALL_TUPLE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 581,740 | 99.8% |
| LOAD_FAST | 1,240 | 0.2% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 581,720 | 99.8% |
| LOAD_FAST | 1,260 | 0.2% |
| CALL | 140 | 0.0% |


</details>

### CALL_TYPE_1

<details>
<summary> Successors and predecessors for CALL_TYPE_1 </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,240 | 86.1% |
| LOAD_GLOBAL_MODULE | 140 | 9.7% |
| CALL | 60 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,260 | 87.5% |
| PUSH_NULL | 140 | 9.7% |
| LOAD_GLOBAL | 40 | 2.8% |


</details>

### COMPARE_OP_FLOAT

<details>
<summary> Successors and predecessors for COMPARE_OP_FLOAT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 140 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 140 | 100.0% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,002,708 | 54.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,060,438 | 28.8% |
| LOAD_FAST | 576,980 | 15.7% |
| LOAD_FAST_LOAD_FAST | 18,480 | 0.5% |
| CALL_BUILTIN_FAST | 14,000 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,679,866 | 99.9% |
| POP_JUMP_IF_TRUE | 3,406 | 0.1% |
| RETURN_VALUE | 160 | 0.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 96 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,409,294 | 95.5% |
| LOAD_CONST | 59,860 | 4.1% |
| LOAD_FAST | 5,820 | 0.4% |
| COMPARE_OP | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,436,391 | 97.4% |
| COPY | 14,040 | 1.0% |
| LOAD_FAST | 14,040 | 1.0% |
| POP_JUMP_IF_TRUE | 10,943 | 0.7% |


</details>

### FOR_ITER_GEN

<details>
<summary> Successors and predecessors for FOR_ITER_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 6,335,920 | 99.8% |
| GET_ITER | 11,440 | 0.2% |
| FOR_ITER | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,335,920 | 99.8% |
| POP_TOP | 11,440 | 0.2% |
| RESUME | 80 | 0.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 7,861,630 | 79.6% |
| GET_ITER | 1,537,138 | 15.6% |
| SWAP | 475,584 | 4.8% |
| FOR_ITER | 300 | 0.0% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 5,760,060 | 58.3% |
| STORE_FAST | 1,609,144 | 16.3% |
| LOAD_FAST | 952,618 | 9.6% |
| JUMP_BACKWARD | 576,000 | 5.8% |
| UNPACK_SEQUENCE_TWO_TUPLE | 492,786 | 5.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 486,464 | 65.6% |
| GET_ITER | 254,975 | 34.4% |
| FOR_ITER | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 501,128 | 67.6% |
| LOAD_FAST | 229,631 | 31.0% |
| RETURN_CONST | 10,880 | 1.5% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 16,320 | 54.0% |
| GET_ITER | 11,740 | 38.8% |
| LOAD_FAST | 1,260 | 4.2% |
| SWAP | 860 | 2.8% |
| FOR_ITER | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 14,260 | 47.2% |
| LOAD_FAST | 10,460 | 34.6% |
| RETURN_CONST | 2,560 | 8.5% |
| STORE_FAST_LOAD_FAST | 2,000 | 6.6% |
| SWAP | 860 | 2.8% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 81,242 | 88.8% |
| LOAD_ATTR_MODULE | 10,200 | 11.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,986 | 81.9% |
| LOAD_FAST_CHECK | 16,536 | 18.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 21,804,876 | 90.5% |
| LOAD_FAST_LOAD_FAST | 1,661,396 | 6.9% |
| COPY | 575,883 | 2.4% |
| LOAD_ATTR_INSTANCE_VALUE | 23,706 | 0.1% |
| RETURN_VALUE | 14,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 5,517,429 | 22.9% |
| LOAD_FAST | 3,643,728 | 15.1% |
| TO_BOOL_BOOL | 1,824,661 | 7.6% |
| LOAD_ATTR | 1,792,522 | 7.4% |
| CONTAINS_OP | 1,710,803 | 7.1% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 408,928 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,684 | 39.8% |
| CALL | 148,646 | 36.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 97,778 | 23.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 5,517,429 | 87.0% |
| LOAD_FAST | 622,001 | 9.8% |
| LOAD_ATTR | 85,276 | 1.3% |
| LOAD_ATTR_SLOT | 83,760 | 1.3% |
| LOAD_CONST | 15,520 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,457,137 | 38.8% |
| CALL | 1,440,126 | 22.7% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,381,511 | 21.8% |
| LOAD_CONST | 740,746 | 11.7% |
| LOAD_FAST_LOAD_FAST | 288,546 | 4.6% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,791,294 | 71.7% |
| LOAD_ATTR_INSTANCE_VALUE | 1,322,405 | 12.2% |
| LOAD_FAST_LOAD_FAST | 1,134,822 | 10.4% |
| BINARY_SUBSCR | 575,920 | 5.3% |
| LOAD_GLOBAL_MODULE | 28,860 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 5,475,685 | 50.4% |
| LOAD_FAST | 3,280,285 | 30.2% |
| CALL_PY_WITH_DEFAULTS | 1,208,971 | 11.1% |
| LOAD_FAST_LOAD_FAST | 678,560 | 6.2% |
| LOAD_CONST | 125,962 | 1.2% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 3,531,284 | 99.9% |
| LOAD_ATTR | 2,820 | 0.1% |
| LOAD_FAST | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 2,244,084 | 63.5% |
| CALL_PY_WITH_DEFAULTS | 1,134,822 | 32.1% |
| STORE_DEREF | 55,040 | 1.6% |
| LOAD_CONST | 35,840 | 1.0% |
| LOAD_FAST | 28,800 | 0.8% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,175,422 | 70.5% |
| LOAD_FAST_LOAD_FAST | 492,226 | 29.5% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,134,862 | 68.0% |
| UNARY_INVERT | 492,306 | 29.5% |
| RETURN_VALUE | 14,040 | 0.8% |
| LOAD_CONST | 14,040 | 0.8% |
| LOAD_FAST_LOAD_FAST | 5,720 | 0.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 970,110 | 97.1% |
| RETURN_VALUE | 27,440 | 2.7% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.1% |
| LOAD_ATTR | 320 | 0.0% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 986,950 | 98.8% |
| TO_BOOL_BOOL | 12,160 | 1.2% |
| LOAD_ATTR_PROPERTY | 220 | 0.0% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 98,360 | 98.6% |
| LOAD_ATTR_MODULE | 1,180 | 1.2% |
| RETURN_VALUE | 140 | 0.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 83,760 | 84.0% |
| CALL_BUILTIN_FAST | 14,140 | 14.2% |
| LOAD_FAST | 1,040 | 1.0% |
| LOAD_CONST | 600 | 0.6% |
| STORE_FAST | 140 | 0.1% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 3,543,913 | 41.7% |
| LOAD_FAST | 1,179,002 | 13.9% |
| STORE_FAST | 1,159,615 | 13.6% |
| LOAD_GLOBAL_BUILTIN | 970,742 | 11.4% |
| NOP | 702,220 | 8.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,921,567 | 46.1% |
| LOAD_DEREF | 1,720,731 | 20.2% |
| CALL_ISINSTANCE | 1,152,362 | 13.6% |
| LOAD_GLOBAL_BUILTIN | 970,742 | 11.4% |
| LOAD_GLOBAL_MODULE | 625,080 | 7.4% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,690,534 | 28.3% |
| RESUME_CHECK | 3,021,886 | 18.2% |
| NOP | 1,734,086 | 10.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,438,300 | 8.7% |
| POP_JUMP_IF_FALSE | 1,411,623 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 3,650,739 | 22.0% |
| LOAD_ATTR_MODULE | 3,531,284 | 21.3% |
| LOAD_FAST_LOAD_FAST | 2,564,755 | 15.5% |
| LOAD_FAST | 2,078,149 | 12.5% |
| COMPARE_OP_STR | 1,409,294 | 8.5% |


</details>

### LOAD_SUPER_ATTR_ATTR

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 89,440 | 99.9% |
| LOAD_SUPER_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 89,520 | 100.0% |


</details>

### LOAD_SUPER_ATTR_METHOD

<details>
<summary> Successors and predecessors for LOAD_SUPER_ATTR_METHOD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,631,011 | 100.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,149,182 | 70.4% |
| CALL_PY_EXACT_ARGS | 476,229 | 29.2% |
| LOAD_FAST | 5,760 | 0.4% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 12,094,728 | 33.1% |
| CACHE | 11,691,864 | 32.0% |
| FOR_ITER_GEN | 6,335,920 | 17.3% |
| CALL_PY_WITH_DEFAULTS | 1,735,407 | 4.7% |
| COPY_FREE_VARS | 1,726,871 | 4.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 20,504,667 | 56.0% |
| POP_TOP | 6,913,520 | 18.9% |
| LOAD_GLOBAL_BUILTIN | 3,543,913 | 9.7% |
| LOAD_GLOBAL_MODULE | 3,021,886 | 8.3% |
| NOP | 1,336,602 | 3.7% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,989,754 | 68.8% |
| LOAD_FAST_LOAD_FAST | 738,009 | 17.0% |
| SWAP | 575,883 | 13.3% |
| LOAD_ATTR_INSTANCE_VALUE | 17,040 | 0.4% |
| STORE_FAST_LOAD_FAST | 14,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,118,636 | 48.8% |
| LOAD_FAST | 940,601 | 21.7% |
| LOAD_GLOBAL_MODULE | 714,849 | 16.5% |
| LOAD_CONST | 302,858 | 7.0% |
| LOAD_FAST_LOAD_FAST | 129,480 | 3.0% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 83,760 | 85.5% |
| LOAD_FAST_LOAD_FAST | 14,140 | 14.4% |
| STORE_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 97,980 | 100.0% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 1,134,822 | 92.6% |
| LOAD_FAST | 43,728 | 3.6% |
| LOAD_ATTR_INSTANCE_VALUE | 34,680 | 2.8% |
| CALL | 10,200 | 0.8% |
| LOAD_CONST | 1,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,137,008 | 92.8% |
| RETURN_CONST | 32,520 | 2.7% |
| LOAD_GLOBAL_MODULE | 27,720 | 2.3% |
| LOAD_CONST | 27,480 | 2.2% |
| NOP | 140 | 0.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 63.4% |
| COPY | 306 | 32.3% |
| TO_BOOL | 40 | 4.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 620 | 65.5% |
| POP_JUMP_IF_FALSE | 326 | 34.5% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,824,661 | 26.6% |
| CALL_ISINSTANCE | 1,152,642 | 16.8% |
| RETURN_VALUE | 853,311 | 12.4% |
| CALL | 731,472 | 10.6% |
| LOAD_FAST | 719,662 | 10.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,773,564 | 69.5% |
| POP_JUMP_IF_TRUE | 1,849,119 | 26.9% |
| UNARY_NOT | 246,007 | 3.6% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,761,870 | 54.9% |
| BINARY_OP | 1,134,962 | 22.6% |
| LOAD_FAST | 1,134,822 | 22.6% |
| TO_BOOL | 240 | 0.0% |
| CALL_BUILTIN_O | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 5,032,034 | 100.0% |
| POP_JUMP_IF_TRUE | 140 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 487,729 | 91.9% |
| LOAD_ATTR_INSTANCE_VALUE | 42,900 | 8.1% |
| TO_BOOL | 200 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 530,689 | 100.0% |
| POP_JUMP_IF_TRUE | 160 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 191,376 | 79.6% |
| LOAD_FAST | 27,900 | 11.6% |
| COPY | 13,880 | 5.8% |
| WITH_EXCEPT_START | 5,680 | 2.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220,736 | 91.8% |
| POP_JUMP_IF_TRUE | 19,700 | 8.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 2,000 | 71.4% |
| LOAD_FAST | 620 | 22.1% |
| COPY | 160 | 5.7% |
| LOAD_GLOBAL_MODULE | 20 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,600 | 92.9% |
| POP_JUMP_IF_TRUE | 200 | 7.1% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,087,880 | 93.0% |
| CALL_BUILTIN_FAST | 81,282 | 6.9% |
| CALL_METHOD_DESCRIPTOR_O | 280 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,088,220 | 93.0% |
| STORE_FAST | 81,322 | 7.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 581,600 | 27.6% |
| LOAD_FAST_CHECK | 575,920 | 27.3% |
| FOR_ITER_LIST | 492,786 | 23.4% |
| CALL_BUILTIN_FAST | 441,726 | 20.9% |
| CALL | 9,440 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 2,102,052 | 99.7% |
| LOAD_FAST | 7,000 | 0.3% |
| STORE_DEREF | 60 | 0.0% |


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
|     deferred | 6,812,002 | 76.7% |
|          hit | 2,063,941 | 23.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 598 | 8.5% |
| Failure | 6,402 | 91.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,183 | 49.7% |
| or | 1,699 | 26.5% |
| remainder | 780 | 12.2% |
| add different types | 640 | 10.0% |
| add other | 100 | 1.6% |


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
|     deferred | 636,142 | 46.3% |
|          hit | 737,262 | 53.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 240 | 21.4% |
| Failure | 880 | 78.6% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 880 | 100.0% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,788,779 | 27.7% |
|          hit | 28,087,984 | 72.2% |
|         miss | 7,580 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,297 | 23.5% |
| Failure | 30,201 | 76.5% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 7,913 | 26.2% |
| cfunc noargs | 6,329 | 21.0% |
| class no vectorcall | 4,000 | 13.2% |
| meth descr varargs keywords | 3,220 | 10.7% |
| class mutable | 1,278 | 4.2% |
| other | 1,180 | 3.9% |
| bound method | 1,123 | 3.7% |
| cfunc varargs | 1,100 | 3.6% |
| meth descr method fastcall keywords | 920 | 3.0% |
| cfunc varargs keywords | 918 | 3.0% |
| operator wrapper | 780 | 2.6% |
| cmethod | 640 | 2.1% |
| wrong number arguments | 480 | 1.6% |
| method wrapper | 280 | 0.9% |
| meth descr varargs | 40 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 564,136 | 9.9% |
|          hit | 5,152,540 | 90.0% |
|         miss | 6,682 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,616 | 53.9% |
| Failure | 1,382 | 46.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 812 | 58.8% |
| big int | 360 | 26.0% |
| different types | 210 | 15.2% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,302,940 | 7.1% |
|          hit | 16,994,011 | 92.9% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 26.7% |
| Failure | 1,700 | 73.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 520 | 30.6% |
| enumerate | 520 | 30.6% |
| itertools | 400 | 23.5% |
| callable | 260 | 15.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 10,048,187 | 17.3% |
|          hit | 47,794,160 | 82.1% |
|         miss | 311,568 | 0.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,444 | 52.3% |
| Failure | 20,492 | 47.7% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 4,617 | 22.5% |
| shadowed | 4,270 | 20.8% |
| not managed dict | 3,720 | 18.2% |
| non overriding descriptor | 2,448 | 11.9% |
| has managed dict | 1,120 | 5.5% |
| class attr descriptor | 1,040 | 5.1% |
| metaclass attribute | 960 | 4.7% |
| class method obj | 920 | 4.5% |
| non object slot | 560 | 2.7% |
| class attr simple | 477 | 2.3% |
| mutable class | 280 | 1.4% |
| overridden | 80 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,296 | 0.0% |
|        deopt | 100 | 0.0% |
|          hit | 25,061,236 | 99.9% |
|         miss | 7,330 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,648 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 1,720,731 | 100.0% |

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

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 89,361 | 2.0% |
|          hit | 4,196,304 | 92.4% |
|         miss | 245,260 | 5.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,978 | 78.1% |
| Failure | 2,520 | 21.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| property | 1,180 | 46.8% |
| class attr simple | 560 | 22.2% |
| not in keys | 520 | 20.6% |
| no dict | 260 | 10.3% |


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 30,339 | 2.4% |
|          hit | 1,224,928 | 97.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 258 | 28.1% |
| Failure | 660 | 71.9% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| py simple | 440 | 66.7% |
| other | 220 | 33.3% |


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 1,573,928 | 11.0% |
|          hit | 12,675,615 | 88.9% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,001 | 45.0% |
| Failure | 3,663 | 55.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| mapping | 1,083 | 29.6% |
| sequence | 880 | 24.0% |
| set | 740 | 20.2% |
| tuple | 740 | 20.2% |
| other | 220 | 6.0% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 3,278,654 | 100.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 440 | 100.0% |
| Failure | 0 | 0.0% |


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>

|Instructions | Count | Ratio | 
|---|---:|---:|
| Basic | 316,239,305 | 56.3% |
| Not specialized | 59,602,807 | 10.6% |
| Specialized hits | 185,415,176 | 33.0% |
| Specialized misses | 578,701 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 10,788,779 | 33.9% |
| LOAD_ATTR | 10,048,187 | 31.5% |
| BINARY_OP | 6,812,002 | 21.4% |
| TO_BOOL | 1,573,928 | 4.9% |
| FOR_ITER | 1,302,940 | 4.1% |
| BINARY_SUBSCR | 636,142 | 2.0% |
| COMPARE_OP | 564,136 | 1.8% |
| STORE_ATTR | 89,361 | 0.3% |
| STORE_SUBSCR | 30,339 | 0.1% |
| LOAD_GLOBAL | 8,296 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 245,260 | 42.4% |
| LOAD_ATTR_INSTANCE_VALUE | 216,072 | 37.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,016 | 14.2% |
| LOAD_ATTR_PROPERTY | 12,380 | 2.1% |
| LOAD_GLOBAL_MODULE | 6,990 | 1.2% |
| COMPARE_OP_INT | 6,662 | 1.2% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,400 | 1.1% |
| LOAD_ATTR_MODULE | 1,100 | 0.2% |
| CALL_PY_EXACT_ARGS | 580 | 0.1% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 420 | 0.1% |


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>

| | Count | Ratio | 
|---|---:|---:|
| Calls to PyEval_EvalDefault | 11,811,524 | 32.3% |
| Calls to Python functions inlined | 24,804,633 | 67.7% |
| Calls via PyEval_EvalFrame (total) | 11,811,524 | 32.3% |
| Calls via PyEval_EvalFrame (vector) | 11,226,404 | 30.7% |
| Calls via PyEval_EvalFrame (generator) | 585,120 | 1.6% |
| Calls via PyEval_EvalFrame (legacy) | 140 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 11,225,704 | 30.7% |
| Calls via PyEval_EvalFrame (build class) | 560 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 625,920 | 1.7% |
| Calls via PyEval_EvalFrame (function ex) | 535,340 | 1.5% |
| Calls via PyEval_EvalFrame (api) | 614,332 | 1.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 49,538 | 0.1% |
| Frames pushed | 18,175,669 | 49.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 18,897,671 | 41.6% |
| Frees to freelist | 18,910,379 |  |
| Allocations | 26,541,300 | 58.4% |
| Allocations to 512 bytes | 26,256,015 | 57.8% |
| Allocations to 4 kbytes | 117,293 | 0.3% |
| Allocations over 4 kbytes | 167,992 | 0.4% |
| Frees | 27,977,220 |  |
| New values | 88,020 |  |
| Interpreter increfs | 220,059,807 | 76.8% |
| Interpreter decrefs | 241,239,559 | 73.7% |
| Increfs | 66,300,948 | 23.2% |
| Decrefs | 85,995,114 | 26.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 40 | 0.0% |
| Method cache hits | 11,857,683 |  |
| Method cache misses | 88,082 |  |
| Method cache collisions | 154,875 |  |
| Method cache dunder hits | 11,260,231 |  |
| Method cache dunder misses | 70,672 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 600 | 275,402 |
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
| Number of data files | 40 |


</details>

---
Stats gathered on: 2024-09-10
