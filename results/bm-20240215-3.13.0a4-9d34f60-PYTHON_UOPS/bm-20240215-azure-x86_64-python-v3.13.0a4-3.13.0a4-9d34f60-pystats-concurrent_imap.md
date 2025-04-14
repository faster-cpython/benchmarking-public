
# Pystats results

- benchmark: concurrent_imap
- fork: python
- ref: v3.13.0a4
- commit hash: 9d34f60
- commit date: 2024-02-15T14:38:42+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 88,381,784 | 17.9% | 17.9% |  |
| RESUME_CHECK | 34,651,944 | 7.0% | 24.9% | 0.0% |
| STORE_FAST | 26,379,430 | 5.3% | 30.3% |  |
| POP_TOP | 22,456,930 | 4.6% | 34.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 20,811,208 | 4.2% | 39.1% | 1.0% |
| RETURN_VALUE | 20,453,637 | 4.1% | 43.2% |  |
| POP_JUMP_IF_FALSE | 16,592,421 | 3.4% | 46.6% |  |
| LOAD_GLOBAL_MODULE | 14,900,144 | 3.0% | 49.6% | 0.0% |
| LOAD_CONST | 13,739,833 | 2.8% | 52.4% |  |
| INTERPRETER_EXIT | 12,697,030 | 2.6% | 55.0% |  |
| LOAD_FAST_LOAD_FAST | 12,582,422 | 2.6% | 57.5% |  |
| ENTER_EXECUTOR | 11,449,383 | 2.3% | 59.8% |  |
| CALL | 11,178,103 | 2.3% | 62.1% |  |
| CALL_PY_EXACT_ARGS | 10,887,325 | 2.2% | 64.3% | 0.0% |
| LOAD_ATTR | 9,457,415 | 1.9% | 66.2% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 8,874,930 | 1.8% | 68.0% | 0.9% |
| NOP | 8,612,965 | 1.7% | 69.8% |  |
| RETURN_CONST | 7,860,875 | 1.6% | 71.4% |  |
| LOAD_GLOBAL_BUILTIN | 6,932,466 | 1.4% | 72.8% | 0.0% |
| YIELD_VALUE | 6,913,660 | 1.4% | 74.2% |  |
| BINARY_OP | 6,700,632 | 1.4% | 75.5% |  |
| COPY | 6,596,879 | 1.3% | 76.9% |  |
| JUMP_BACKWARD | 6,351,438 | 1.3% | 78.2% |  |
| FOR_ITER_GEN | 6,347,440 | 1.3% | 79.4% |  |
| TO_BOOL_BOOL | 5,495,076 | 1.1% | 80.6% |  |
| PUSH_NULL | 5,429,162 | 1.1% | 81.7% |  |
| LOAD_ATTR_METHOD_NO_DICT | 5,268,502 | 1.1% | 82.7% |  |
| TO_BOOL_INT | 4,942,344 | 1.0% | 83.7% |  |
| POP_JUMP_IF_NOT_NONE | 4,852,471 | 1.0% | 84.7% |  |
| STORE_FAST_STORE_FAST | 4,210,128 | 0.9% | 85.6% |  |
| STORE_ATTR_INSTANCE_VALUE | 3,803,653 | 0.8% | 86.3% | 6.4% |
| COMPARE_OP_INT | 3,649,826 | 0.7% | 87.1% | 0.2% |
| FOR_ITER_LIST | 3,182,027 | 0.6% | 87.7% |  |
| BUILD_TUPLE | 3,073,892 | 0.6% | 88.4% |  |
| CALL_FUNCTION_EX | 2,414,020 | 0.5% | 88.8% |  |
| POP_JUMP_IF_TRUE | 2,361,300 | 0.5% | 89.3% |  |
| CALL_PY_WITH_DEFAULTS | 2,334,881 | 0.5% | 89.8% |  |
| LOAD_ATTR_MODULE | 2,275,013 | 0.5% | 90.3% | 0.0% |
| SWAP | 2,020,658 | 0.4% | 90.7% |  |
| BEFORE_WITH | 1,823,401 | 0.4% | 91.0% |  |
| LOAD_DEREF | 1,748,940 | 0.4% | 91.4% |  |
| STORE_SUBSCR_DICT | 1,707,233 | 0.3% | 91.7% |  |
| COPY_FREE_VARS | 1,698,920 | 0.3% | 92.1% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 1,639,354 | 0.3% | 92.4% |  |
| LOAD_SUPER_ATTR_METHOD | 1,602,600 | 0.3% | 92.7% |  |
| UNARY_INVERT | 1,598,694 | 0.3% | 93.1% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 1,591,467 | 0.3% | 93.4% | 0.0% |
| CALL_BUILTIN_FAST | 1,544,533 | 0.3% | 93.7% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,522,848 | 0.3% | 94.0% |  |
| GET_ITER | 1,508,128 | 0.3% | 94.3% |  |
| CALL_BUILTIN_CLASS | 1,500,934 | 0.3% | 94.6% |  |
| COMPARE_OP_STR | 1,471,279 | 0.3% | 94.9% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,465,422 | 0.3% | 95.2% |  |
| BUILD_LIST | 1,443,188 | 0.3% | 95.5% |  |
| CONTAINS_OP | 1,192,754 | 0.2% | 95.7% |  |
| UNPACK_SEQUENCE_TUPLE | 1,169,556 | 0.2% | 96.0% |  |
| CALL_ISINSTANCE | 1,132,410 | 0.2% | 96.2% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 1,132,336 | 0.2% | 96.4% | 0.0% |
| JUMP_FORWARD | 1,112,440 | 0.2% | 96.7% |  |
| POP_JUMP_IF_NONE | 1,093,596 | 0.2% | 96.9% |  |
| BUILD_MAP | 1,079,130 | 0.2% | 97.1% |  |
| TO_BOOL | 1,070,702 | 0.2% | 97.3% |  |
| LOAD_ATTR_PROPERTY | 983,003 | 0.2% | 97.5% | 1.3% |
| LOAD_FAST_CHECK | 819,468 | 0.2% | 97.7% |  |
| LIST_APPEND | 786,522 | 0.2% | 97.9% |  |
| LOAD_FAST_AND_CLEAR | 724,510 | 0.1% | 98.0% |  |
| BINARY_SUBSCR | 634,332 | 0.1% | 98.1% |  |
| BINARY_OP_ADD_INT | 613,505 | 0.1% | 98.3% |  |
| CALL_TUPLE_1 | 583,120 | 0.1% | 98.4% |  |
| DICT_MERGE | 564,260 | 0.1% | 98.5% |  |
| COMPARE_OP | 558,597 | 0.1% | 98.6% |  |
| TO_BOOL_LIST | 522,650 | 0.1% | 98.7% |  |
| CALL_METHOD_DESCRIPTOR_O | 464,001 | 0.1% | 98.8% | 0.0% |
| LIST_EXTEND | 452,292 | 0.1% | 98.9% |  |
| LOAD_ATTR_METHOD_LAZY_DICT | 409,164 | 0.1% | 99.0% |  |
| CALL_LEN | 396,874 | 0.1% | 99.1% |  |
| CALL_KW | 342,126 | 0.1% | 99.1% |  |
| BINARY_OP_SUBTRACT_INT | 327,684 | 0.1% | 99.2% |  |
| FOR_ITER_RANGE | 269,882 | 0.1% | 99.2% |  |
| CALL_LIST_APPEND | 253,962 | 0.1% | 99.3% |  |
| BINARY_OP_ADD_FLOAT | 242,704 | 0.0% | 99.3% |  |
| UNARY_NOT | 241,986 | 0.0% | 99.4% |  |
| TO_BOOL_NONE | 240,471 | 0.0% | 99.4% | 0.1% |
| BINARY_OP_SUBTRACT_FLOAT | 226,088 | 0.0% | 99.5% |  |
| CALL_BUILTIN_O | 154,260 | 0.0% | 99.5% |  |
| MAKE_CELL | 137,900 | 0.0% | 99.5% |  |
| STORE_DEREF | 137,660 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_DICT | 114,880 | 0.0% | 99.6% |  |
| BINARY_OP_MULTIPLY_FLOAT | 112,600 | 0.0% | 99.6% |  |
| BINARY_SUBSCR_STR_INT | 112,600 | 0.0% | 99.6% |  |
| STORE_ATTR | 100,900 | 0.0% | 99.7% |  |
| LOAD_ATTR_SLOT | 99,760 | 0.0% | 99.7% |  |
| STORE_ATTR_SLOT | 97,980 | 0.0% | 99.7% |  |
| LOAD_ATTR_CLASS | 91,536 | 0.0% | 99.7% |  |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 0.0% | 99.7% |  |
| DELETE_ATTR | 86,400 | 0.0% | 99.8% |  |
| DELETE_SUBSCR | 78,220 | 0.0% | 99.8% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 78,196 | 0.0% | 99.8% | 8.2% |
| EXIT_INIT_CHECK | 68,300 | 0.0% | 99.8% |  |
| CALL_ALLOC_AND_ENTER_INIT | 68,300 | 0.0% | 99.8% |  |
| MAKE_FUNCTION | 63,680 | 0.0% | 99.8% |  |
| FORMAT_SIMPLE | 55,680 | 0.0% | 99.8% |  |
| IS_OP | 46,624 | 0.0% | 99.9% |  |
| POP_EXCEPT | 46,472 | 0.0% | 99.9% |  |
| PUSH_EXC_INFO | 46,472 | 0.0% | 99.9% |  |
| STORE_FAST_LOAD_FAST | 43,040 | 0.0% | 99.9% |  |
| BUILD_STRING | 41,600 | 0.0% | 99.9% |  |
| CHECK_EXC_MATCH | 40,712 | 0.0% | 99.9% |  |
| BINARY_SUBSCR_TUPLE_INT | 39,160 | 0.0% | 99.9% |  |
| SET_FUNCTION_ATTRIBUTE | 39,040 | 0.0% | 99.9% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 38,380 | 0.0% | 99.9% |  |
| FOR_ITER | 36,380 | 0.0% | 99.9% |  |
| IMPORT_NAME | 33,760 | 0.0% | 99.9% |  |
| IMPORT_FROM | 33,420 | 0.0% | 99.9% |  |
| STORE_SUBSCR | 31,298 | 0.0% | 99.9% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 29,732 | 0.0% | 100.0% |  |
| CONVERT_VALUE | 28,160 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 27,960 | 0.0% | 100.0% |  |
| BINARY_OP_INPLACE_ADD_UNICODE | 27,480 | 0.0% | 100.0% |  |
| BINARY_SLICE | 19,820 | 0.0% | 100.0% |  |
| RETURN_GENERATOR | 18,900 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 18,400 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 17,844 | 0.0% | 100.0% |  |
| RERAISE | 17,280 | 0.0% | 100.0% |  |
| CALL_STR_1 | 11,900 | 0.0% | 100.0% |  |
| END_FOR | 11,520 | 0.0% | 100.0% |  |
| STORE_NAME | 7,480 | 0.0% | 100.0% |  |
| RESUME | 5,980 | 0.0% | 100.0% | 0.1% |
| RAISE_VARARGS | 5,780 | 0.0% | 100.0% |  |
| WITH_EXCEPT_START | 5,760 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 3,420 | 0.0% | 100.0% |  |
| LOAD_NAME | 2,200 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 1,660 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 1,440 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 971 | 0.0% | 100.0% |  |
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
| RESUME_CHECK LOAD_FAST | 19,134,051 | 3.9% | 3.9% |
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 18,549,263 | 3.8% | 7.6% |
| CACHE RESUME_CHECK | 12,115,080 | 2.5% | 10.1% |
| STORE_FAST LOAD_FAST | 10,862,952 | 2.2% | 12.3% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 10,840,725 | 2.2% | 14.5% |
| LOAD_FAST RETURN_VALUE | 10,457,548 | 2.1% | 16.6% |
| RETURN_VALUE INTERPRETER_EXIT | 10,319,800 | 2.1% | 18.7% |
| POP_TOP ENTER_EXECUTOR | 8,053,131 | 1.6% | 20.3% |
| LOAD_FAST LOAD_ATTR | 7,364,042 | 1.5% | 21.8% |
| RESUME_CHECK POP_TOP | 6,913,520 | 1.4% | 23.2% |
| POP_TOP LOAD_FAST | 6,578,343 | 1.3% | 24.6% |
| JUMP_BACKWARD FOR_ITER_GEN | 6,335,920 | 1.3% | 25.9% |
| YIELD_VALUE STORE_FAST | 6,335,920 | 1.3% | 27.1% |
| FOR_ITER_GEN RESUME_CHECK | 6,335,920 | 1.3% | 28.4% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 6,333,188 | 1.3% | 29.7% |
| ENTER_EXECUTOR YIELD_VALUE | 6,322,640 | 1.3% | 31.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 6,199,563 | 1.3% | 32.3% |
| STORE_FAST JUMP_BACKWARD | 5,760,000 | 1.2% | 33.4% |
| RETURN_CONST POP_TOP | 5,713,777 | 1.2% | 34.6% |
| NOP LOAD_FAST | 5,092,308 | 1.0% | 35.6% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 4,942,204 | 1.0% | 36.6% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 4,763,462 | 1.0% | 37.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 4,720,289 | 1.0% | 38.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 4,468,384 | 0.9% | 39.4% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 3,956,904 | 0.8% | 40.2% |
| LOAD_CONST LOAD_CONST | 3,768,200 | 0.8% | 41.0% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 3,759,598 | 0.8% | 41.8% |
| STORE_FAST NOP | 3,713,220 | 0.8% | 42.5% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 3,646,003 | 0.7% | 43.3% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_FAST | 3,616,165 | 0.7% | 44.0% |
| LOAD_FAST LOAD_CONST | 3,601,767 | 0.7% | 44.7% |
| LOAD_GLOBAL_MODULE BINARY_OP | 3,585,412 | 0.7% | 45.5% |
| RESUME_CHECK LOAD_GLOBAL_BUILTIN | 3,494,890 | 0.7% | 46.2% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,428,524 | 0.7% | 46.9% |
| PUSH_NULL LOAD_FAST | 3,336,999 | 0.7% | 47.5% |
| LOAD_ATTR LOAD_FAST | 3,096,090 | 0.6% | 48.2% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 3,029,402 | 0.6% | 48.8% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 2,956,958 | 0.6% | 49.4% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 2,762,073 | 0.6% | 49.9% |
| BINARY_OP COPY | 2,713,184 | 0.6% | 50.5% |
| COPY TO_BOOL_INT | 2,712,864 | 0.6% | 51.0% |
| COPY STORE_FAST | 2,630,400 | 0.5% | 51.6% |
| STORE_FAST COPY | 2,629,760 | 0.5% | 52.1% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 2,575,236 | 0.5% | 52.6% |
| CALL STORE_FAST | 2,572,713 | 0.5% | 53.1% |
| LOAD_GLOBAL_MODULE LOAD_FAST_LOAD_FAST | 2,514,326 | 0.5% | 53.7% |
| CALL RETURN_VALUE | 2,417,450 | 0.5% | 54.1% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 2,389,863 | 0.5% | 54.6% |
| LOAD_FAST PUSH_NULL | 2,366,910 | 0.5% | 55.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,271,773 | 0.5% | 55.6% |
| CALL POP_TOP | 2,217,165 | 0.4% | 56.0% |
| RETURN_VALUE STORE_FAST | 2,188,467 | 0.4% | 56.5% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 2,135,618 | 0.4% | 56.9% |
| STORE_ATTR_INSTANCE_VALUE RETURN_CONST | 2,085,840 | 0.4% | 57.3% |
| LOAD_CONST CALL | 2,073,682 | 0.4% | 57.7% |
| POP_JUMP_IF_FALSE RETURN_CONST | 2,047,127 | 0.4% | 58.2% |
| LOAD_GLOBAL_MODULE LOAD_FAST | 2,045,084 | 0.4% | 58.6% |
| POP_JUMP_IF_NOT_NONE LOAD_FAST | 2,006,007 | 0.4% | 59.0% |
| LOAD_CONST COMPARE_OP_INT | 1,979,496 | 0.4% | 59.4% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 1,927,816 | 0.4% | 59.8% |
| POP_JUMP_IF_FALSE LOAD_FAST_LOAD_FAST | 1,907,574 | 0.4% | 60.2% |
| POP_TOP RETURN_CONST | 1,889,475 | 0.4% | 60.5% |
| RETURN_VALUE RETURN_VALUE | 1,873,441 | 0.4% | 60.9% |
| LOAD_FAST CALL_FUNCTION_EX | 1,849,740 | 0.4% | 61.3% |
| RETURN_CONST INTERPRETER_EXIT | 1,799,490 | 0.4% | 61.7% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,784,128 | 0.4% | 62.0% |
| ENTER_EXECUTOR FOR_ITER_LIST | 1,757,970 | 0.4% | 62.4% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 1,731,544 | 0.4% | 62.7% |
| POP_TOP LOAD_CONST | 1,722,142 | 0.3% | 63.1% |
| NOP LOAD_GLOBAL_MODULE | 1,705,447 | 0.3% | 63.4% |
| ENTER_EXECUTOR CALL | 1,703,427 | 0.3% | 63.8% |
| COPY_FREE_VARS RESUME_CHECK | 1,698,260 | 0.3% | 64.1% |
| LOAD_DEREF LOAD_FAST | 1,692,640 | 0.3% | 64.5% |
| LOAD_GLOBAL_BUILTIN LOAD_DEREF | 1,692,120 | 0.3% | 64.8% |
| LOAD_FAST BUILD_TUPLE | 1,675,930 | 0.3% | 65.1% |
| LOAD_CONST LOAD_FAST | 1,660,417 | 0.3% | 65.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,651,110 | 0.3% | 65.8% |
| STORE_SUBSCR_DICT LOAD_FAST | 1,619,313 | 0.3% | 66.1% |
| LOAD_FAST LOAD_SUPER_ATTR_METHOD | 1,602,400 | 0.3% | 66.5% |
| UNARY_INVERT BINARY_OP | 1,598,694 | 0.3% | 66.8% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_FAST | 1,582,580 | 0.3% | 67.1% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,572,484 | 0.3% | 67.4% |
| POP_TOP NOP | 1,521,092 | 0.3% | 67.7% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,515,788 | 0.3% | 68.0% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,500,574 | 0.3% | 68.3% |
| CALL LOAD_FAST | 1,500,024 | 0.3% | 68.7% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 1,493,532 | 0.3% | 69.0% |
| LOAD_FAST GET_ITER | 1,435,368 | 0.3% | 69.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_GLOBAL_MODULE | 1,433,803 | 0.3% | 69.5% |
| COMPARE_OP_STR POP_JUMP_IF_FALSE | 1,432,286 | 0.3% | 69.8% |
| LOAD_ATTR_METHOD_NO_DICT CALL | 1,431,336 | 0.3% | 70.1% |
| RETURN_VALUE POP_TOP | 1,419,604 | 0.3% | 70.4% |
| LOAD_GLOBAL_MODULE COMPARE_OP_STR | 1,405,159 | 0.3% | 70.7% |
| POP_JUMP_IF_FALSE POP_TOP | 1,397,675 | 0.3% | 71.0% |
| POP_JUMP_IF_FALSE LOAD_GLOBAL_MODULE | 1,391,246 | 0.3% | 71.3% |
| BINARY_OP STORE_FAST | 1,371,012 | 0.3% | 71.5% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 1,364,566 | 0.3% | 71.8% |
| BEFORE_WITH POP_TOP | 1,349,391 | 0.3% | 72.1% |
| RESUME_CHECK NOP | 1,316,190 | 0.3% | 72.4% |
| POP_JUMP_IF_FALSE NOP | 1,297,610 | 0.3% | 72.6% |


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
| RESUME_CHECK | 12,115,080 | 95.4% |
| COPY_FREE_VARS | 577,970 | 4.5% |
| POP_TOP | 7,460 | 0.1% |
| RESUME | 2,280 | 0.0% |
| MAKE_CELL | 20 | 0.0% |


</details>

### BEFORE_WITH

<details>
<summary> Successors and predecessors for BEFORE_WITH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,248,471 | 68.5% |
| CALL | 474,430 | 26.0% |
| LOAD_GLOBAL_MODULE | 82,440 | 4.5% |
| LOAD_FAST | 17,280 | 0.9% |
| RETURN_VALUE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,349,391 | 74.0% |
| STORE_FAST | 474,010 | 26.0% |


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
| LOAD_FAST_LOAD_FAST | 576,080 | 90.8% |
| LOAD_CONST | 57,292 | 9.0% |
| BINARY_SUBSCR | 880 | 0.1% |
| CALL | 40 | 0.0% |
| CALL_BUILTIN_O | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 575,920 | 90.8% |
| STORE_FAST | 57,012 | 9.0% |
| BINARY_SUBSCR | 880 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 120 | 0.0% |
| LOAD_ATTR | 80 | 0.0% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 35,552 | 87.3% |
| LOAD_ATTR_MODULE | 5,100 | 12.5% |
| LOAD_GLOBAL | 40 | 0.1% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 40,712 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 37,900 | 48.5% |
| CALL | 27,520 | 35.2% |
| LOAD_ATTR_INSTANCE_VALUE | 12,718 | 16.3% |
| LOAD_ATTR | 82 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 60,800 | 77.7% |
| RETURN_CONST | 10,240 | 13.1% |
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
| POP_TOP | 11,520 | 100.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 68,300 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 68,300 | 100.0% |


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
| LOAD_FAST | 1,435,368 | 95.2% |
| CALL_BUILTIN_CLASS | 38,820 | 2.6% |
| CALL | 14,340 | 1.0% |
| STORE_FAST_LOAD_FAST | 6,400 | 0.4% |
| RETURN_VALUE | 5,760 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 951,140 | 63.1% |
| LOAD_FAST_AND_CLEAR | 482,408 | 32.0% |
| FOR_ITER_RANGE | 31,906 | 2.1% |
| FOR_ITER | 12,114 | 0.8% |
| FOR_ITER_TUPLE | 11,740 | 0.8% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 10,319,800 | 81.3% |
| RETURN_CONST | 1,799,490 | 14.2% |
| YIELD_VALUE | 577,740 | 4.6% |


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
| STORE_FAST | 3,713,220 | 43.1% |
| POP_TOP | 1,521,092 | 17.7% |
| RESUME_CHECK | 1,316,190 | 15.3% |
| POP_JUMP_IF_FALSE | 1,297,610 | 15.1% |
| POP_JUMP_IF_NOT_NONE | 476,947 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 5,092,308 | 59.1% |
| LOAD_GLOBAL_MODULE | 1,705,447 | 19.8% |
| LOAD_GLOBAL_BUILTIN | 689,950 | 8.0% |
| LOAD_FAST_LOAD_FAST | 583,320 | 6.8% |
| LOAD_CONST | 530,020 | 6.2% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 29,732 | 64.0% |
| COPY | 11,520 | 24.8% |
| POP_TOP | 5,200 | 11.2% |
| STORE_SUBSCR_DICT | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 29,732 | 64.0% |
| RERAISE | 11,520 | 24.8% |
| JUMP_FORWARD | 5,120 | 11.0% |
| RETURN_CONST | 60 | 0.1% |
| JUMP_BACKWARD | 20 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 6,913,520 | 30.8% |
| RETURN_CONST | 5,713,777 | 25.4% |
| CALL | 2,217,165 | 9.9% |
| RETURN_VALUE | 1,419,604 | 6.3% |
| POP_JUMP_IF_FALSE | 1,397,675 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 8,053,131 | 35.9% |
| LOAD_FAST | 6,578,343 | 29.3% |
| RETURN_CONST | 1,889,475 | 8.4% |
| LOAD_CONST | 1,722,142 | 7.7% |
| NOP | 1,521,092 | 6.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_NOARGS | 35,172 | 75.7% |
| RERAISE | 5,760 | 12.4% |
| CALL_KW | 5,120 | 11.0% |
| BINARY_SUBSCR_DICT | 300 | 0.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 60 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 35,512 | 76.4% |
| WITH_EXCEPT_START | 5,760 | 12.4% |
| LOAD_GLOBAL_MODULE | 5,080 | 10.9% |
| LOAD_GLOBAL | 120 | 0.3% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,366,910 | 43.6% |
| LOAD_ATTR_MODULE | 1,651,110 | 30.4% |
| LOAD_ATTR | 1,284,422 | 23.7% |
| LOAD_SUPER_ATTR_ATTR | 89,520 | 1.6% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,336,999 | 61.5% |
| CALL | 881,908 | 16.2% |
| LOAD_FAST_LOAD_FAST | 821,012 | 15.1% |
| LOAD_CONST | 315,627 | 5.8% |
| CALL_PY_EXACT_ARGS | 49,320 | 0.9% |


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
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 280 | 1.5% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,457,548 | 51.1% |
| CALL | 2,417,450 | 11.8% |
| RETURN_VALUE | 1,873,441 | 9.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,500,574 | 7.3% |
| CALL_FUNCTION_EX | 1,265,560 | 6.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| INTERPRETER_EXIT | 10,319,800 | 50.5% |
| STORE_FAST | 2,188,467 | 10.7% |
| RETURN_VALUE | 1,873,441 | 9.2% |
| POP_TOP | 1,419,604 | 6.9% |
| LOAD_FAST_LOAD_FAST | 1,114,490 | 5.4% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 14,080 | 45.0% |
| LOAD_FAST | 10,478 | 33.5% |
| LOAD_ATTR_INSTANCE_VALUE | 5,800 | 18.5% |
| STORE_SUBSCR | 660 | 2.1% |
| LOAD_ATTR | 200 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 19,960 | 63.8% |
| LOAD_GLOBAL_MODULE | 10,200 | 32.6% |
| STORE_SUBSCR | 660 | 2.1% |
| STORE_SUBSCR_DICT | 279 | 0.9% |
| LOAD_GLOBAL | 80 | 0.3% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,009,314 | 94.3% |
| LOAD_ATTR_INSTANCE_VALUE | 53,500 | 5.0% |
| TO_BOOL | 3,524 | 0.3% |
| LOAD_ATTR | 882 | 0.1% |
| RETURN_VALUE | 762 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 830,844 | 77.6% |
| POP_JUMP_IF_FALSE | 233,294 | 21.8% |
| TO_BOOL | 3,524 | 0.3% |
| TO_BOOL_BOOL | 2,160 | 0.2% |
| TO_BOOL_NONE | 360 | 0.0% |


</details>

### UNARY_INVERT

<details>
<summary> Successors and predecessors for UNARY_INVERT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,114,490 | 69.7% |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 484,124 | 30.3% |
| LOAD_ATTR | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 1,598,694 | 100.0% |


</details>

### UNARY_NOT

<details>
<summary> Successors and predecessors for UNARY_NOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 241,946 | 100.0% |
| TO_BOOL | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 241,986 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 3,585,412 | 53.5% |
| UNARY_INVERT | 1,598,694 | 23.9% |
| POP_JUMP_IF_FALSE | 1,114,490 | 16.6% |
| LOAD_ATTR | 256,202 | 3.8% |
| LOAD_FAST_LOAD_FAST | 84,160 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,713,184 | 40.5% |
| STORE_FAST | 1,371,012 | 20.5% |
| TO_BOOL_INT | 1,114,550 | 16.6% |
| UNARY_INVERT | 1,114,490 | 16.6% |
| BUILD_TUPLE | 242,102 | 3.6% |


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
| SWAP | 482,408 | 33.4% |
| JUMP_FORWARD | 468,110 | 32.4% |
| LOAD_FAST | 242,764 | 16.8% |
| POP_TOP | 225,366 | 15.6% |
| STORE_ATTR_INSTANCE_VALUE | 10,660 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 485,350 | 33.6% |
| SWAP | 482,408 | 33.4% |
| STORE_FAST | 469,570 | 32.5% |
| RETURN_VALUE | 5,120 | 0.4% |
| COMPARE_OP | 280 | 0.0% |


</details>

### BUILD_MAP

<details>
<summary> Successors and predecessors for BUILD_MAP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 529,560 | 49.1% |
| RESUME_CHECK | 478,310 | 44.3% |
| LOAD_ATTR_INSTANCE_VALUE | 34,480 | 3.2% |
| POP_JUMP_IF_NOT_NONE | 17,280 | 1.6% |
| POP_TOP | 7,040 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,055,430 | 97.8% |
| STORE_FAST | 17,280 | 1.6% |
| BUILD_TUPLE | 6,420 | 0.6% |


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
| LOAD_FAST | 1,675,930 | 54.5% |
| LOAD_FAST_LOAD_FAST | 590,720 | 19.2% |
| RETURN_VALUE | 512,000 | 16.7% |
| BINARY_OP | 242,102 | 7.9% |
| LOAD_ATTR_INSTANCE_VALUE | 22,880 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 1,116,050 | 36.3% |
| YIELD_VALUE | 582,460 | 18.9% |
| STORE_FAST | 512,000 | 16.7% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 511,960 | 16.7% |
| CALL_LIST_APPEND | 242,022 | 7.9% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 2,073,682 | 18.6% |
| ENTER_EXECUTOR | 1,703,427 | 15.2% |
| LOAD_ATTR_METHOD_NO_DICT | 1,431,336 | 12.8% |
| LOAD_FAST_LOAD_FAST | 1,279,220 | 11.4% |
| BUILD_TUPLE | 1,116,050 | 10.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 2,572,713 | 23.0% |
| RETURN_VALUE | 2,417,450 | 21.6% |
| POP_TOP | 2,217,165 | 19.8% |
| LOAD_FAST | 1,500,024 | 13.4% |
| CALL_TUPLE_1 | 581,740 | 5.2% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,849,740 | 76.6% |
| DICT_MERGE | 564,260 | 23.4% |
| CALL_INTRINSIC_1 | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 1,265,560 | 52.4% |
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
| LOAD_CONST | 336,686 | 98.4% |
| ENTER_EXECUTOR | 5,440 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 272,646 | 79.7% |
| LOAD_FAST | 28,800 | 8.4% |
| RETURN_VALUE | 21,120 | 6.2% |
| STORE_FAST | 14,220 | 4.2% |
| PUSH_EXC_INFO | 5,120 | 1.5% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 554,645 | 99.3% |
| COMPARE_OP | 1,271 | 0.2% |
| LOAD_ATTR_INSTANCE_VALUE | 749 | 0.1% |
| LOAD_GLOBAL_MODULE | 380 | 0.1% |
| LOAD_FAST | 300 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 555,354 | 99.4% |
| COMPARE_OP | 1,271 | 0.2% |
| COMPARE_OP_INT | 1,172 | 0.2% |
| COMPARE_OP_STR | 440 | 0.1% |
| POP_JUMP_IF_TRUE | 280 | 0.1% |


</details>

### CONTAINS_OP

<details>
<summary> Successors and predecessors for CONTAINS_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,191,455 | 99.9% |
| LOAD_ATTR_MODULE | 560 | 0.0% |
| LOAD_FAST | 480 | 0.0% |
| LOAD_FAST_LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR | 119 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,192,134 | 99.9% |
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
| BINARY_OP | 2,713,184 | 41.1% |
| STORE_FAST | 2,629,760 | 39.9% |
| LOAD_CONST | 1,100,800 | 16.7% |
| LOAD_FAST | 91,184 | 1.4% |
| STORE_ATTR_INSTANCE_VALUE | 21,000 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 2,712,864 | 41.1% |
| STORE_FAST | 2,630,400 | 39.9% |
| STORE_FAST_STORE_FAST | 1,093,760 | 16.6% |
| LOAD_ATTR_INSTANCE_VALUE | 76,926 | 1.2% |
| LOAD_FAST | 28,160 | 0.4% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 1,114,490 | 65.6% |
| CACHE | 577,970 | 34.0% |
| CALL | 5,940 | 0.3% |
| CALL_PY_EXACT_ARGS | 360 | 0.0% |
| CALL_FUNCTION_EX | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,698,260 | 100.0% |
| RETURN_GENERATOR | 340 | 0.0% |
| RESUME | 320 | 0.0% |


</details>

### DELETE_ATTR

<details>
<summary> Successors and predecessors for DELETE_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 86,400 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 57,600 | 66.7% |
| RETURN_CONST | 27,520 | 31.9% |
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

### ENTER_EXECUTOR

<details>
<summary> Successors and predecessors for ENTER_EXECUTOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,053,131 | 70.3% |
| POP_JUMP_IF_NOT_NONE | 962,432 | 8.4% |
| LIST_APPEND | 784,822 | 6.9% |
| STORE_FAST_STORE_FAST | 580,400 | 5.1% |
| FOR_ITER_LIST | 575,320 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 6,322,640 | 55.2% |
| FOR_ITER_LIST | 1,757,970 | 15.4% |
| CALL | 1,703,427 | 14.9% |
| CALL_PY_WITH_DEFAULTS | 715,169 | 6.2% |
| LOAD_ATTR_PROPERTY | 659,666 | 5.8% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| SWAP | 14,160 | 38.9% |
| GET_ITER | 12,114 | 33.3% |
| LOAD_FAST | 6,060 | 16.7% |
| JUMP_BACKWARD | 3,106 | 8.5% |
| FOR_ITER | 940 | 2.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 21,080 | 57.9% |
| UNPACK_SEQUENCE_TWO_TUPLE | 12,000 | 33.0% |
| FOR_ITER | 940 | 2.6% |
| STORE_FAST | 760 | 2.1% |
| LOAD_GLOBAL_MODULE | 560 | 1.5% |


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
| RETURN_VALUE | 27,520 | 59.0% |
| LOAD_FAST | 17,420 | 37.4% |
| LOAD_GLOBAL_MODULE | 1,644 | 3.5% |
| LOAD_GLOBAL | 40 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 46,484 | 99.7% |
| POP_JUMP_IF_TRUE | 140 | 0.3% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 5,760,000 | 90.7% |
| POP_TOP | 582,659 | 9.2% |
| LIST_APPEND | 1,700 | 0.0% |
| POP_JUMP_IF_NOT_NONE | 1,360 | 0.0% |
| POP_JUMP_IF_TRUE | 1,360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_GEN | 6,335,920 | 99.8% |
| FOR_ITER_LIST | 5,169 | 0.1% |
| FOR_ITER | 3,106 | 0.0% |
| FOR_ITER_RANGE | 2,210 | 0.0% |
| LOAD_FAST | 1,882 | 0.0% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_EXCEPT | 29,732 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 29,452 | 99.1% |
| LOAD_FAST | 280 | 0.9% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 974,982 | 87.6% |
| POP_TOP | 119,238 | 10.7% |
| STORE_ATTR_INSTANCE_VALUE | 7,020 | 0.6% |
| BINARY_SUBSCR_TUPLE_INT | 5,720 | 0.5% |
| POP_EXCEPT | 5,120 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 600,870 | 54.0% |
| BUILD_LIST | 468,110 | 42.1% |
| LOAD_GLOBAL_MODULE | 24,820 | 2.2% |
| LOAD_FAST_LOAD_FAST | 7,320 | 0.7% |
| STORE_FAST | 5,760 | 0.5% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 430,900 | 54.8% |
| LOAD_ATTR | 242,122 | 30.8% |
| BINARY_SUBSCR_STR_INT | 112,600 | 14.3% |
| CALL_METHOD_DESCRIPTOR_FAST | 860 | 0.1% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 784,822 | 99.8% |
| JUMP_BACKWARD | 1,700 | 0.2% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 226,786 | 50.1% |
| RETURN_VALUE | 225,366 | 49.8% |
| LOAD_CONST | 120 | 0.0% |
| LOAD_DEREF | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 226,006 | 50.0% |
| STORE_FAST | 225,366 | 49.8% |
| RETURN_VALUE | 640 | 0.1% |
| CALL_INTRINSIC_1 | 160 | 0.0% |
| STORE_NAME | 120 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,364,042 | 77.9% |
| LOAD_ATTR_INSTANCE_VALUE | 1,784,128 | 18.9% |
| LOAD_GLOBAL_MODULE | 162,840 | 1.7% |
| CALL | 83,860 | 0.9% |
| LOAD_ATTR | 22,407 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,096,090 | 32.7% |
| PUSH_NULL | 1,284,422 | 13.6% |
| STORE_SUBSCR_DICT | 1,114,410 | 11.8% |
| POP_JUMP_IF_NOT_NONE | 1,027,610 | 10.9% |
| STORE_FAST | 712,582 | 7.5% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,768,200 | 27.4% |
| LOAD_FAST | 3,601,767 | 26.2% |
| POP_TOP | 1,722,142 | 12.5% |
| POP_JUMP_IF_FALSE | 904,795 | 6.6% |
| STORE_FAST | 628,300 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 3,768,200 | 27.4% |
| CALL | 2,073,682 | 15.1% |
| COMPARE_OP_INT | 1,979,496 | 14.4% |
| LOAD_FAST | 1,660,417 | 12.1% |
| COPY | 1,100,800 | 8.0% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,692,120 | 96.8% |
| POP_JUMP_IF_NOT_NONE | 27,520 | 1.6% |
| STORE_DEREF | 27,520 | 1.6% |
| STORE_FAST | 440 | 0.0% |
| POP_JUMP_IF_FALSE | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,692,640 | 96.8% |
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
| RESUME_CHECK | 19,134,051 | 21.6% |
| STORE_FAST | 10,862,952 | 12.3% |
| POP_TOP | 6,578,343 | 7.4% |
| POP_JUMP_IF_FALSE | 6,199,563 | 7.0% |
| NOP | 5,092,308 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 18,549,263 | 21.0% |
| RETURN_VALUE | 10,457,548 | 11.8% |
| LOAD_ATTR | 7,364,042 | 8.3% |
| LOAD_ATTR_METHOD_WITH_VALUES | 6,333,188 | 7.2% |
| CALL_PY_EXACT_ARGS | 4,720,289 | 5.3% |


</details>

### LOAD_FAST_AND_CLEAR

<details>
<summary> Successors and predecessors for LOAD_FAST_AND_CLEAR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 482,408 | 66.6% |
| LOAD_FAST_AND_CLEAR | 242,102 | 33.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 482,408 | 66.6% |
| LOAD_FAST_AND_CLEAR | 242,102 | 33.4% |


</details>

### LOAD_FAST_CHECK

<details>
<summary> Successors and predecessors for LOAD_FAST_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 576,560 | 70.4% |
| POP_JUMP_IF_NONE | 226,008 | 27.6% |
| LOAD_ATTR_CLASS | 16,580 | 2.0% |
| LOAD_FAST | 140 | 0.0% |
| LOAD_ATTR_METHOD_NO_DICT | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 575,920 | 70.3% |
| LOAD_GLOBAL_MODULE | 225,928 | 27.6% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 16,540 | 2.0% |
| POP_JUMP_IF_NOT_NONE | 560 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,514,326 | 20.0% |
| POP_JUMP_IF_FALSE | 1,907,574 | 15.2% |
| LOAD_FAST_LOAD_FAST | 1,185,550 | 9.4% |
| LOAD_SUPER_ATTR_METHOD | 1,128,770 | 9.0% |
| RETURN_VALUE | 1,114,490 | 8.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,029,402 | 24.1% |
| LOAD_ATTR_INSTANCE_VALUE | 2,135,618 | 17.0% |
| CALL | 1,279,220 | 10.2% |
| LOAD_FAST_LOAD_FAST | 1,185,550 | 9.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,114,410 | 8.9% |


</details>

### LOAD_GLOBAL

<details>
<summary> Successors and predecessors for LOAD_GLOBAL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 2,000 | 11.2% |
| RESUME_CHECK | 1,720 | 9.6% |
| POP_JUMP_IF_FALSE | 1,708 | 9.6% |
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
| TO_BOOL_INT | 4,942,204 | 29.8% |
| TO_BOOL_BOOL | 3,759,598 | 22.7% |
| COMPARE_OP_INT | 3,646,003 | 22.0% |
| COMPARE_OP_STR | 1,432,286 | 8.6% |
| CONTAINS_OP | 1,192,134 | 7.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,199,563 | 37.4% |
| RETURN_CONST | 2,047,127 | 12.3% |
| LOAD_FAST_LOAD_FAST | 1,907,574 | 11.5% |
| POP_TOP | 1,397,675 | 8.4% |
| LOAD_GLOBAL_MODULE | 1,391,246 | 8.4% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,015,796 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 47,800 | 4.4% |
| LOAD_ATTR | 28,300 | 2.6% |
| RETURN_VALUE | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 279,495 | 25.6% |
| LOAD_FAST | 274,900 | 25.1% |
| NOP | 263,286 | 24.1% |
| LOAD_FAST_CHECK | 226,008 | 20.7% |
| RETURN_CONST | 24,340 | 2.2% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,389,863 | 49.3% |
| LOAD_ATTR | 1,027,610 | 21.2% |
| LOAD_ATTR_INSTANCE_VALUE | 926,946 | 19.1% |
| RETURN_VALUE | 431,540 | 8.9% |
| LOAD_DEREF | 55,040 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,006,007 | 41.3% |
| RETURN_CONST | 1,029,043 | 21.2% |
| ENTER_EXECUTOR | 962,432 | 19.8% |
| NOP | 476,947 | 9.8% |
| LOAD_CONST | 225,646 | 4.7% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,493,532 | 63.3% |
| TO_BOOL | 830,844 | 35.2% |
| TO_BOOL_NONE | 19,700 | 0.8% |
| COMPARE_OP_STR | 10,913 | 0.5% |
| COMPARE_OP_INT | 3,431 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 833,602 | 35.3% |
| LOAD_FAST | 670,976 | 28.4% |
| RETURN_CONST | 665,890 | 28.2% |
| LOAD_GLOBAL_MODULE | 69,260 | 2.9% |
| RETURN_VALUE | 56,972 | 2.4% |


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
| STORE_ATTR_INSTANCE_VALUE | 2,085,840 | 26.5% |
| POP_JUMP_IF_FALSE | 2,047,127 | 26.0% |
| POP_TOP | 1,889,475 | 24.0% |
| POP_JUMP_IF_NOT_NONE | 1,029,043 | 13.1% |
| POP_JUMP_IF_TRUE | 665,890 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 5,713,777 | 72.7% |
| INTERPRETER_EXIT | 1,799,490 | 22.9% |
| TO_BOOL_BOOL | 183,044 | 2.3% |
| EXIT_INIT_CHECK | 68,300 | 0.9% |
| STORE_FAST | 58,812 | 0.7% |


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
| LOAD_FAST | 58,562 | 58.0% |
| LOAD_FAST_LOAD_FAST | 22,040 | 21.8% |
| LOAD_ATTR_INSTANCE_VALUE | 17,280 | 17.1% |
| STORE_ATTR | 2,520 | 2.5% |
| LOAD_ATTR | 240 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 44,840 | 44.4% |
| LOAD_FAST_LOAD_FAST | 14,760 | 14.6% |
| LOAD_FAST | 13,639 | 13.5% |
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
| YIELD_VALUE | 6,335,920 | 24.0% |
| COPY | 2,630,400 | 10.0% |
| CALL | 2,572,713 | 9.8% |
| RETURN_VALUE | 2,188,467 | 8.3% |
| BINARY_OP | 1,371,012 | 5.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,862,952 | 41.2% |
| JUMP_BACKWARD | 5,760,000 | 21.8% |
| NOP | 3,713,220 | 14.1% |
| COPY | 2,629,760 | 10.0% |
| JUMP_FORWARD | 974,982 | 3.7% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER | 21,080 | 49.0% |
| COPY | 14,080 | 32.7% |
| FOR_ITER_LIST | 7,020 | 16.3% |
| FOR_ITER_TUPLE | 860 | 2.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 14,640 | 34.0% |
| STORE_ATTR_INSTANCE_VALUE | 14,000 | 32.5% |
| YIELD_VALUE | 7,000 | 16.3% |
| GET_ITER | 6,400 | 14.9% |
| TO_BOOL_STR | 860 | 2.0% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,515,788 | 36.0% |
| COPY | 1,093,760 | 26.0% |
| UNPACK_SEQUENCE_TUPLE | 1,088,220 | 25.8% |
| STORE_FAST_STORE_FAST | 512,000 | 12.2% |
| UNPACK_SEQUENCE | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,572,484 | 37.4% |
| STORE_FAST | 1,088,280 | 25.8% |
| ENTER_EXECUTOR | 580,400 | 13.8% |
| STORE_FAST_STORE_FAST | 512,000 | 12.2% |
| LOAD_FAST_LOAD_FAST | 440,104 | 10.5% |


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
| BUILD_LIST | 482,408 | 23.9% |
| LOAD_FAST_AND_CLEAR | 482,408 | 23.9% |
| FOR_ITER_LIST | 467,468 | 23.1% |
| LOAD_FAST | 253,808 | 12.6% |
| STORE_FAST | 242,102 | 12.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 495,910 | 24.5% |
| BUILD_LIST | 482,408 | 23.9% |
| STORE_FAST | 482,408 | 23.9% |
| FOR_ITER_LIST | 467,388 | 23.1% |
| STORE_ATTR_INSTANCE_VALUE | 76,926 | 3.8% |


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
| ENTER_EXECUTOR | 6,322,640 | 91.5% |
| BUILD_TUPLE | 582,460 | 8.4% |
| STORE_FAST_LOAD_FAST | 7,000 | 0.1% |
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
| LOAD_FAST | 242,664 | 100.0% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 242,704 | 100.0% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 594,846 | 97.0% |
| LOAD_FAST_LOAD_FAST | 18,480 | 3.0% |
| BINARY_OP | 179 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 511,980 | 83.5% |
| SWAP | 77,005 | 12.6% |
| BINARY_SLICE | 18,520 | 3.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 5,680 | 0.9% |
| LOAD_CONST | 280 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 1,240 | 36.3% |
| CALL_METHOD_DESCRIPTOR_O | 1,240 | 36.3% |
| LOAD_FAST_LOAD_FAST | 600 | 17.5% |
| BINARY_SUBSCR_LIST_INT | 280 | 8.2% |
| BINARY_OP | 40 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,740 | 50.9% |
| LOAD_CONST | 1,260 | 36.8% |
| STORE_FAST | 300 | 8.8% |
| CALL | 120 | 3.5% |


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
| CALL | 225,928 | 99.9% |
| BINARY_OP | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 226,088 | 100.0% |


</details>

### BINARY_OP_SUBTRACT_INT

<details>
<summary> Successors and predecessors for BINARY_OP_SUBTRACT_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 264,912 | 80.8% |
| LOAD_CONST | 56,892 | 17.4% |
| CALL_LEN | 5,680 | 1.7% |
| BINARY_OP | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 321,964 | 98.3% |
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
| LOAD_CONST | 11,640 | 63.3% |
| LOAD_FAST_LOAD_FAST | 6,640 | 36.1% |
| BINARY_SUBSCR | 120 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 11,440 | 62.2% |
| STORE_FAST | 6,680 | 36.3% |
| BINARY_OP_ADD_UNICODE | 280 | 1.5% |


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
| CALL | 33,340 | 48.8% |
| LOAD_GLOBAL_MODULE | 27,480 | 40.2% |
| LOAD_FAST | 7,200 | 10.5% |
| LOAD_FAST_LOAD_FAST | 280 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 68,300 | 100.0% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 64,240 | 82.2% |
| LOAD_CONST | 7,000 | 9.0% |
| BINARY_OP_ADD_INT | 5,680 | 7.3% |
| PUSH_NULL | 996 | 1.3% |
| CALL | 160 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 71,796 | 91.8% |
| POP_TOP | 6,280 | 8.0% |
| CALL_BOUND_METHOD_EXACT_ARGS | 120 | 0.2% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 683,490 | 45.5% |
| CALL_FUNCTION_EX | 511,960 | 34.1% |
| LOAD_FAST | 260,444 | 17.4% |
| LOAD_CONST | 14,600 | 1.0% |
| LOAD_GLOBAL_BUILTIN | 10,260 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 754,684 | 50.3% |
| STORE_FAST | 683,790 | 45.6% |
| GET_ITER | 38,820 | 2.6% |
| LOAD_FAST | 17,280 | 1.2% |
| CALL_BUILTIN_CLASS | 6,320 | 0.4% |


</details>

### CALL_BUILTIN_FAST

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 849,479 | 55.0% |
| LOAD_CONST | 383,566 | 24.8% |
| LOAD_FAST_LOAD_FAST | 173,272 | 11.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 81,296 | 5.3% |
| LOAD_GLOBAL_MODULE | 27,880 | 1.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 579,354 | 37.5% |
| UNPACK_SEQUENCE_TWO_TUPLE | 433,664 | 28.1% |
| TO_BOOL_BOOL | 373,506 | 24.2% |
| UNPACK_SEQUENCE_TUPLE | 81,296 | 5.3% |
| POP_TOP | 14,933 | 1.0% |


</details>

### CALL_BUILTIN_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 518,160 | 45.8% |
| BUILD_TUPLE | 511,960 | 45.2% |
| CALL | 64,976 | 5.7% |
| LOAD_FAST_CHECK | 16,540 | 1.5% |
| LOAD_ATTR | 14,000 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,047,820 | 92.5% |
| RETURN_VALUE | 82,196 | 7.3% |
| LOAD_FAST | 1,260 | 0.1% |
| STORE_FAST | 860 | 0.1% |
| BEFORE_WITH | 140 | 0.0% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP_MULTIPLY_FLOAT | 112,560 | 73.0% |
| LOAD_ATTR | 27,440 | 17.8% |
| LOAD_FAST | 14,140 | 9.2% |
| CALL | 120 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_SUBSCR_STR_INT | 112,560 | 73.0% |
| LOAD_FAST | 41,520 | 26.9% |
| TO_BOOL_INT | 140 | 0.1% |
| BINARY_SUBSCR | 40 | 0.0% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 1,131,950 | 100.0% |
| CALL | 180 | 0.0% |
| BUILD_TUPLE | 140 | 0.0% |
| LOAD_GLOBAL_MODULE | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,132,230 | 100.0% |
| TO_BOOL | 180 | 0.0% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 368,594 | 92.9% |
| LOAD_ATTR_INSTANCE_VALUE | 27,900 | 7.0% |
| CALL | 380 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 344,352 | 86.8% |
| CALL_PY_EXACT_ARGS | 33,160 | 8.4% |
| CALL_BUILTIN_CLASS | 6,320 | 1.6% |
| LOAD_FAST | 5,720 | 1.4% |
| BINARY_OP_SUBTRACT_INT | 5,680 | 1.4% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_TUPLE | 242,022 | 95.3% |
| LOAD_FAST | 11,440 | 4.5% |
| LOAD_CONST | 140 | 0.1% |
| LOAD_FAST_CHECK | 140 | 0.1% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 241,422 | 95.1% |
| LOAD_GLOBAL_MODULE | 11,440 | 4.5% |
| JUMP_BACKWARD | 640 | 0.3% |
| NOP | 280 | 0.1% |
| RETURN_CONST | 140 | 0.1% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,582,580 | 99.4% |
| LOAD_ATTR_INSTANCE_VALUE | 5,908 | 0.4% |
| LOAD_CONST | 1,240 | 0.1% |
| LOAD_GLOBAL_MODULE | 1,140 | 0.1% |
| LOAD_ATTR_METHOD_NO_DICT | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,114,770 | 70.0% |
| STORE_FAST | 474,297 | 29.8% |
| TO_BOOL_NONE | 1,240 | 0.1% |
| LIST_APPEND | 860 | 0.1% |
| LOAD_FAST | 140 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 32,520 | 84.7% |
| BUILD_TUPLE | 5,680 | 14.8% |
| CALL | 180 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 26,900 | 70.1% |
| LOAD_FAST | 11,480 | 29.9% |


</details>

### CALL_METHOD_DESCRIPTOR_NOARGS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_NOARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 1,364,566 | 93.1% |
| LOAD_ATTR_METHOD_LAZY_DICT | 97,836 | 6.7% |
| LOAD_ATTR | 2,480 | 0.2% |
| CALL | 540 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 618,934 | 42.2% |
| STORE_FAST | 575,960 | 39.3% |
| LOAD_FAST | 85,060 | 5.8% |
| CALL_BUILTIN_FAST | 81,296 | 5.5% |
| RETURN_VALUE | 51,720 | 3.5% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 384,542 | 82.9% |
| LOAD_CONST | 33,720 | 7.3% |
| CALL | 29,159 | 6.3% |
| RETURN_VALUE | 14,000 | 3.0% |
| RETURN_GENERATOR | 1,300 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 413,841 | 89.2% |
| LOAD_CONST | 33,440 | 7.2% |
| RETURN_VALUE | 14,900 | 3.2% |
| BINARY_OP_ADD_UNICODE | 1,240 | 0.3% |
| STORE_FAST | 280 | 0.1% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 4,763,462 | 43.8% |
| LOAD_FAST | 4,720,289 | 43.4% |
| LOAD_FAST_LOAD_FAST | 596,520 | 5.5% |
| LOAD_SUPER_ATTR_METHOD | 468,030 | 4.3% |
| LOAD_GLOBAL_MODULE | 93,900 | 0.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 10,840,725 | 99.6% |
| MAKE_CELL | 27,800 | 0.3% |
| RETURN_GENERATOR | 18,420 | 0.2% |
| COPY_FREE_VARS | 360 | 0.0% |
| PUSH_EXC_INFO | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 715,169 | 30.6% |
| LOAD_ATTR_METHOD_WITH_VALUES | 629,112 | 26.9% |
| LOAD_ATTR_MODULE | 468,230 | 20.1% |
| LOAD_FAST | 325,062 | 13.9% |
| LOAD_CONST | 107,428 | 4.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,220,391 | 52.3% |
| COPY_FREE_VARS | 1,114,490 | 47.7% |


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
| LOAD_CONST | 1,979,496 | 54.2% |
| LOAD_ATTR_INSTANCE_VALUE | 1,049,787 | 28.8% |
| LOAD_FAST | 576,980 | 15.8% |
| LOAD_FAST_LOAD_FAST | 18,480 | 0.5% |
| CALL_BUILTIN_FAST | 14,000 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,646,003 | 99.9% |
| POP_JUMP_IF_TRUE | 3,431 | 0.1% |
| RETURN_VALUE | 160 | 0.0% |
| STORE_FAST | 140 | 0.0% |
| COMPARE_OP | 92 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 1,405,159 | 95.5% |
| LOAD_CONST | 59,860 | 4.1% |
| LOAD_FAST | 5,820 | 0.4% |
| COMPARE_OP | 440 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,432,286 | 97.3% |
| COPY | 14,040 | 1.0% |
| LOAD_FAST | 14,040 | 1.0% |
| POP_JUMP_IF_TRUE | 10,913 | 0.7% |


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
| ENTER_EXECUTOR | 1,757,970 | 55.2% |
| GET_ITER | 951,140 | 29.9% |
| SWAP | 467,388 | 14.7% |
| JUMP_BACKWARD | 5,169 | 0.2% |
| FOR_ITER | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 936,220 | 29.4% |
| STORE_FAST | 702,695 | 22.1% |
| ENTER_EXECUTOR | 575,320 | 18.1% |
| UNPACK_SEQUENCE_TWO_TUPLE | 484,184 | 15.2% |
| SWAP | 467,468 | 14.7% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 235,566 | 87.3% |
| GET_ITER | 31,906 | 11.8% |
| JUMP_BACKWARD | 2,210 | 0.8% |
| FOR_ITER | 200 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 225,526 | 83.6% |
| STORE_FAST | 33,476 | 12.4% |
| RETURN_CONST | 10,880 | 4.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 13,400 | 47.9% |
| GET_ITER | 11,740 | 42.0% |
| LOAD_FAST | 1,260 | 4.5% |
| SWAP | 860 | 3.1% |
| JUMP_BACKWARD | 660 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 13,140 | 47.0% |
| LOAD_FAST | 10,460 | 37.4% |
| RETURN_CONST | 2,560 | 9.2% |
| STORE_FAST_LOAD_FAST | 860 | 3.1% |
| SWAP | 860 | 3.1% |


</details>

### LOAD_ATTR_CLASS

<details>
<summary> Successors and predecessors for LOAD_ATTR_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 81,256 | 88.8% |
| LOAD_ATTR_MODULE | 10,200 | 11.1% |
| LOAD_ATTR | 80 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 74,956 | 81.9% |
| LOAD_FAST_CHECK | 16,580 | 18.1% |


</details>

### LOAD_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for LOAD_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 18,549,263 | 89.1% |
| LOAD_FAST_LOAD_FAST | 2,135,618 | 10.3% |
| COPY | 76,926 | 0.4% |
| LOAD_ATTR_INSTANCE_VALUE | 23,728 | 0.1% |
| RETURN_VALUE | 14,000 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,468,384 | 21.5% |
| LOAD_FAST | 3,616,165 | 17.4% |
| LOAD_ATTR | 1,784,128 | 8.6% |
| TO_BOOL_BOOL | 1,731,544 | 8.3% |
| RETURN_VALUE | 1,500,574 | 7.2% |


</details>

### LOAD_ATTR_METHOD_LAZY_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_LAZY_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 408,984 | 100.0% |
| LOAD_ATTR | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 162,712 | 39.8% |
| CALL | 148,616 | 36.3% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 97,836 | 23.9% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 4,468,384 | 84.8% |
| LOAD_FAST | 599,900 | 11.4% |
| LOAD_ATTR | 85,318 | 1.6% |
| LOAD_ATTR_SLOT | 83,760 | 1.6% |
| LOAD_CONST | 15,520 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,927,816 | 36.6% |
| CALL | 1,431,336 | 27.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,364,566 | 25.9% |
| LOAD_FAST_LOAD_FAST | 284,352 | 5.4% |
| LOAD_CONST | 230,032 | 4.4% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,333,188 | 71.4% |
| LOAD_FAST_LOAD_FAST | 1,114,410 | 12.6% |
| LOAD_ATTR_INSTANCE_VALUE | 803,313 | 9.1% |
| BINARY_SUBSCR | 575,920 | 6.5% |
| LOAD_GLOBAL_MODULE | 28,860 | 0.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 4,763,462 | 53.7% |
| LOAD_FAST | 2,575,236 | 29.0% |
| LOAD_FAST_LOAD_FAST | 678,560 | 7.6% |
| CALL_PY_WITH_DEFAULTS | 629,112 | 7.1% |
| LOAD_CONST | 125,908 | 1.4% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,271,773 | 99.9% |
| LOAD_ATTR | 2,820 | 0.1% |
| LOAD_FAST | 420 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,651,110 | 72.6% |
| CALL_PY_WITH_DEFAULTS | 468,230 | 20.6% |
| STORE_DEREF | 55,040 | 2.4% |
| LOAD_CONST | 35,840 | 1.6% |
| LOAD_FAST | 28,800 | 1.3% |


</details>

### LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,155,010 | 70.5% |
| LOAD_FAST_LOAD_FAST | 484,044 | 29.5% |
| LOAD_ATTR | 300 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,114,450 | 68.0% |
| UNARY_INVERT | 484,124 | 29.5% |
| RETURN_VALUE | 14,040 | 0.9% |
| LOAD_CONST | 14,040 | 0.9% |
| LOAD_FAST_LOAD_FAST | 5,720 | 0.3% |


</details>

### LOAD_ATTR_PROPERTY

<details>
<summary> Successors and predecessors for LOAD_ATTR_PROPERTY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| ENTER_EXECUTOR | 659,666 | 67.1% |
| LOAD_FAST | 294,117 | 29.9% |
| RETURN_VALUE | 27,440 | 2.8% |
| LOAD_GLOBAL_MODULE | 1,240 | 0.1% |
| LOAD_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 970,623 | 98.7% |
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
| RESUME_CHECK | 3,494,890 | 50.4% |
| LOAD_FAST | 1,158,590 | 16.7% |
| STORE_FAST | 699,222 | 10.1% |
| NOP | 689,950 | 10.0% |
| LOAD_GLOBAL_BUILTIN | 524,600 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,428,524 | 49.5% |
| LOAD_DEREF | 1,692,120 | 24.4% |
| CALL_ISINSTANCE | 1,131,950 | 16.3% |
| LOAD_GLOBAL_BUILTIN | 524,600 | 7.6% |
| LOAD_GLOBAL_MODULE | 49,720 | 0.7% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,956,904 | 26.6% |
| RESUME_CHECK | 2,762,073 | 18.5% |
| NOP | 1,705,447 | 11.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,433,803 | 9.6% |
| POP_JUMP_IF_FALSE | 1,391,246 | 9.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 3,585,412 | 24.1% |
| LOAD_FAST_LOAD_FAST | 2,514,326 | 16.9% |
| LOAD_ATTR_MODULE | 2,271,773 | 15.2% |
| LOAD_FAST | 2,045,084 | 13.7% |
| COMPARE_OP_STR | 1,405,159 | 9.4% |


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
| LOAD_FAST | 1,602,400 | 100.0% |
| LOAD_SUPER_ATTR | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,128,770 | 70.4% |
| CALL_PY_EXACT_ARGS | 468,030 | 29.2% |
| LOAD_FAST | 5,760 | 0.4% |
| CALL | 40 | 0.0% |


</details>

### RESUME_CHECK

<details>
<summary> Successors and predecessors for RESUME_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 12,115,080 | 35.0% |
| CALL_PY_EXACT_ARGS | 10,840,725 | 31.3% |
| FOR_ITER_GEN | 6,335,920 | 18.3% |
| COPY_FREE_VARS | 1,698,260 | 4.9% |
| CALL_PY_WITH_DEFAULTS | 1,220,391 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,134,051 | 55.2% |
| POP_TOP | 6,913,520 | 20.0% |
| LOAD_GLOBAL_BUILTIN | 3,494,890 | 10.1% |
| LOAD_GLOBAL_MODULE | 2,762,073 | 8.0% |
| NOP | 1,316,190 | 3.8% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 2,956,958 | 77.7% |
| LOAD_FAST_LOAD_FAST | 729,810 | 19.2% |
| SWAP | 76,926 | 2.0% |
| LOAD_ATTR_INSTANCE_VALUE | 17,040 | 0.4% |
| STORE_FAST_LOAD_FAST | 14,000 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 2,085,840 | 54.8% |
| LOAD_GLOBAL_MODULE | 706,650 | 18.6% |
| LOAD_FAST | 441,665 | 11.6% |
| LOAD_CONST | 302,858 | 8.0% |
| LOAD_FAST_LOAD_FAST | 129,480 | 3.4% |


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
| LOAD_ATTR | 1,114,410 | 65.3% |
| LOAD_FAST | 546,424 | 32.0% |
| LOAD_ATTR_INSTANCE_VALUE | 34,680 | 2.0% |
| CALL | 10,200 | 0.6% |
| LOAD_CONST | 1,240 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,619,313 | 94.9% |
| RETURN_CONST | 32,520 | 1.9% |
| LOAD_GLOBAL_MODULE | 27,720 | 1.6% |
| LOAD_CONST | 27,480 | 1.6% |
| NOP | 140 | 0.0% |


</details>

### TO_BOOL_ALWAYS_TRUE

<details>
<summary> Successors and predecessors for TO_BOOL_ALWAYS_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 600 | 61.8% |
| COPY | 331 | 34.1% |
| TO_BOOL | 40 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 620 | 63.9% |
| POP_JUMP_IF_FALSE | 351 | 36.1% |


</details>

### TO_BOOL_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,731,544 | 31.5% |
| CALL_ISINSTANCE | 1,132,230 | 20.6% |
| RETURN_VALUE | 840,986 | 15.3% |
| LOAD_FAST | 716,732 | 13.0% |
| CALL_BUILTIN_FAST | 373,506 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 3,759,598 | 68.4% |
| POP_JUMP_IF_TRUE | 1,493,532 | 27.2% |
| UNARY_NOT | 241,946 | 4.4% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 2,712,864 | 54.9% |
| BINARY_OP | 1,114,550 | 22.6% |
| LOAD_FAST | 1,114,410 | 22.5% |
| TO_BOOL | 240 | 0.0% |
| CALL_BUILTIN_O | 140 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,942,204 | 100.0% |
| POP_JUMP_IF_TRUE | 140 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 479,530 | 91.7% |
| LOAD_ATTR_INSTANCE_VALUE | 42,900 | 8.2% |
| TO_BOOL | 200 | 0.0% |
| LOAD_ATTR_MODULE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 522,490 | 100.0% |
| POP_JUMP_IF_TRUE | 160 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 191,411 | 79.6% |
| LOAD_FAST | 27,900 | 11.6% |
| COPY | 13,880 | 5.8% |
| WITH_EXCEPT_START | 5,680 | 2.4% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,240 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 220,771 | 91.8% |
| POP_JUMP_IF_TRUE | 19,700 | 8.2% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 860 | 51.8% |
| LOAD_FAST | 620 | 37.3% |
| COPY | 160 | 9.6% |
| LOAD_GLOBAL_MODULE | 20 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 1,060 | 63.9% |
| POP_JUMP_IF_FALSE | 600 | 36.1% |


</details>

### UNPACK_SEQUENCE_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,087,880 | 93.0% |
| CALL_BUILTIN_FAST | 81,296 | 7.0% |
| CALL_METHOD_DESCRIPTOR_O | 280 | 0.0% |
| UNPACK_SEQUENCE | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,088,220 | 93.0% |
| STORE_FAST | 81,336 | 7.0% |


</details>

### UNPACK_SEQUENCE_TWO_TUPLE

<details>
<summary> Successors and predecessors for UNPACK_SEQUENCE_TWO_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_CHECK | 575,920 | 37.8% |
| FOR_ITER_LIST | 484,184 | 31.8% |
| CALL_BUILTIN_FAST | 433,664 | 28.5% |
| FOR_ITER | 12,000 | 0.8% |
| CALL | 9,440 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,515,788 | 99.5% |
| LOAD_FAST | 7,000 | 0.5% |
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
|     deferred | 6,693,628 | 76.5% |
|          hit | 2,052,817 | 23.5% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 619 | 8.8% |
| Failure | 6,385 | 91.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 3,174 | 49.7% |
| or | 1,692 | 26.5% |
| remainder | 779 | 12.2% |
| add different types | 640 | 10.0% |
| add other | 100 | 1.6% |


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
|     deferred | 633,212 | 46.4% |
|          hit | 729,052 | 53.5% |

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
|     deferred | 11,145,404 | 29.7% |
|          hit | 26,296,568 | 70.2% |
|         miss | 7,580 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,258 | 23.0% |
| Failure | 31,021 | 77.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| code complex parameters | 7,916 | 25.5% |
| cfunc noargs | 5,826 | 18.8% |
| class no vectorcall | 4,500 | 14.5% |
| meth descr varargs keywords | 3,099 | 10.0% |
| class mutable | 1,274 | 4.1% |
| other | 1,180 | 3.8% |
| bound method | 1,124 | 3.6% |
| metaclass | 1,108 | 3.6% |
| cfunc varargs | 1,100 | 3.5% |
| meth descr method fastcall keywords | 920 | 3.0% |
| cfunc varargs keywords | 914 | 2.9% |
| operator wrapper | 780 | 2.5% |
| cmethod | 640 | 2.1% |
| wrong number arguments | 320 | 1.0% |
| method wrapper | 280 | 0.9% |
| meth descr varargs | 40 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 562,152 | 9.9% |
|          hit | 5,114,715 | 90.1% |
|         miss | 6,530 | 0.1% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 1,612 | 54.2% |
| Failure | 1,363 | 45.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| float long | 813 | 59.6% |
| big int | 360 | 26.4% |
| different types | 190 | 13.9% |


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 34,820 | 0.4% |
|          hit | 9,827,309 | 99.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 620 | 39.7% |
| Failure | 940 | 60.3% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| itertools | 280 | 29.8% |
| other | 220 | 23.4% |
| enumerate | 220 | 23.4% |
| callable | 220 | 23.4% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 9,726,184 | 17.4% |
|          hit | 46,287,388 | 82.6% |
|         miss | 311,521 | 0.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 22,627 | 52.9% |
| Failure | 20,125 | 47.1% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| method | 4,614 | 22.9% |
| shadowed | 4,249 | 21.1% |
| not managed dict | 3,710 | 18.4% |
| non overriding descriptor | 2,118 | 10.5% |
| has managed dict | 1,120 | 5.6% |
| class attr descriptor | 1,040 | 5.2% |
| metaclass attribute | 960 | 4.8% |
| class method obj | 920 | 4.6% |
| non object slot | 560 | 2.8% |
| class attr simple | 474 | 2.4% |
| mutable class | 280 | 1.4% |
| overridden | 80 | 0.4% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 13,304 | 0.1% |
|        deopt | 100 | 0.0% |
|          hit | 21,827,543 | 99.9% |
|         miss | 5,067 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 9,607 | 100.0% |
| Failure | 0 | 0.0% |


</details>

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 240 | 0.0% |
|          hit | 1,692,120 | 100.0% |

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
|     deferred | 334,641 | 7.4% |
|          hit | 4,155,289 | 92.3% |
|         miss | 245,260 | 5.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,999 | 78.1% |
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
|     deferred | 30,359 | 1.7% |
|          hit | 1,707,233 | 98.2% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 279 | 29.7% |
| Failure | 660 | 70.3% |

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
|     deferred | 1,064,458 | 8.5% |
|          hit | 11,493,625 | 91.5% |
|         miss | 280 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,000 | 46.0% |
| Failure | 3,524 | 54.0% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| mapping | 1,084 | 30.8% |
| sequence | 740 | 21.0% |
| set | 740 | 21.0% |
| tuple | 740 | 21.0% |
| other | 220 | 6.2% |


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 480 | 0.0% |
|          hit | 3,262,424 | 100.0% |

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
| Basic | 279,893,657 | 56.8% |
| Not specialized | 54,707,251 | 11.1% |
| Specialized hits | 157,984,161 | 32.0% |
| Specialized misses | 576,241 | 0.1% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| CALL | 11,145,404 | 36.9% |
| LOAD_ATTR | 9,726,184 | 32.2% |
| BINARY_OP | 6,693,628 | 22.1% |
| TO_BOOL | 1,064,458 | 3.5% |
| BINARY_SUBSCR | 633,212 | 2.1% |
| COMPARE_OP | 562,152 | 1.9% |
| STORE_ATTR | 334,641 | 1.1% |
| FOR_ITER | 34,820 | 0.1% |
| STORE_SUBSCR | 30,359 | 0.1% |
| LOAD_GLOBAL | 13,304 | 0.0% |


</details>

### Misses by instruction

<details>
<summary> misses by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| STORE_ATTR_INSTANCE_VALUE | 245,260 | 42.6% |
| LOAD_ATTR_INSTANCE_VALUE | 216,015 | 37.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 82,026 | 14.2% |
| LOAD_ATTR_PROPERTY | 12,380 | 2.1% |
| COMPARE_OP_INT | 6,510 | 1.1% |
| CALL_BOUND_METHOD_EXACT_ARGS | 6,400 | 1.1% |
| LOAD_GLOBAL_MODULE | 4,727 | 0.8% |
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
| Calls to PyEval_EvalDefault | 12,702,810 | 36.0% |
| Calls to Python functions inlined | 22,610,509 | 64.0% |
| Calls via PyEval_EvalFrame (total) | 12,702,810 | 36.0% |
| Calls via PyEval_EvalFrame (vector) | 12,117,690 | 34.3% |
| Calls via PyEval_EvalFrame (generator) | 585,120 | 1.7% |
| Calls via PyEval_EvalFrame (legacy) | 140 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 12,116,990 | 34.3% |
| Calls via PyEval_EvalFrame (build class) | 560 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 625,920 | 1.8% |
| Calls via PyEval_EvalFrame (function ex) | 535,340 | 1.5% |
| Calls via PyEval_EvalFrame (api) | 606,200 | 1.7% |
| Calls via PyEval_EvalFrame (method) | 0 | 0.0% |
| Frame objects created | 46,588 | 0.1% |
| Frames pushed | 28,449,059 | 80.6% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 18,593,086 | 41.3% |
| Frees to freelist | 18,605,708 |  |
| Allocations | 26,472,724 | 58.7% |
| Allocations to 512 bytes | 26,166,470 | 58.1% |
| Allocations to 4 kbytes | 133,116 | 0.3% |
| Allocations over 4 kbytes | 173,138 | 0.4% |
| Frees | 27,849,353 |  |
| New values | 1,024,160 |  |
| Interpreter increfs | 197,967,107 | 67.2% |
| Interpreter decrefs | 229,952,290 | 68.7% |
| Increfs | 96,501,315 | 32.8% |
| Decrefs | 104,963,344 | 31.3% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 0 | 0.0% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 40 | 0.0% |
| Method cache hits | 11,836,109 |  |
| Method cache misses | 34,861 |  |
| Method cache collisions | 37,146 |  |
| Method cache dunder hits | 12,187,118 |  |
| Method cache dunder misses | 6,190 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 40 | 720 | 289,618 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

| | Count | Ratio | 
|---|---:|---:|
| Optimization attempts | 4,471 |  |
| Traces created | 891 | 19.9% |
| Trace stack overflow | 0 | 0.0% |
| Trace stack underflow | 0 | 0.0% |
| Trace too long | 0 | 0.0% |
| Trace too short | 3,580 | 80.1% |
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
| <= 16 | 198 | 22.2% |
| <= 32 | 460 | 51.6% |
| <= 64 | 40 | 4.5% |
| <= 128 | 193 | 21.7% |


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

|Range | Count | Ratio | 
|---|---:|---:|
| <= 1 | 0 | 0.0% |
| <= 2 | 0 | 0.0% |
| <= 4 | 40 | 4.5% |
| <= 8 | 78 | 8.8% |
| <= 16 | 380 | 42.6% |
| <= 32 | 160 | 18.0% |
| <= 64 | 153 | 17.2% |
| <= 128 | 80 | 9.0% |


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
| FOR_ITER_GEN | 3,620 |
| CALL | 216 |
| YIELD_VALUE | 140 |
| LOAD_ATTR_PROPERTY | 138 |
| CALL_PY_WITH_DEFAULTS | 120 |
| CALL_KW | 40 |
| CALL_LIST_APPEND | 40 |


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
| Number of data files | 40 |


</details>

---
Stats gathered on: 2024-09-10
