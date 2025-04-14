
# Pystats results

- benchmark: asyncio_tcp_ssl
- fork: python
- ref: v3.13.0a2
- commit hash: 9c4347e
- commit date: 2023-11-22T12:20:24+01:00

## Execution counts

<details>
<summary> execution counts for all instructions </summary>

|Name | Count | Self | Cumulative | Miss ratio | 
|---|---:|---:|---:|---:|
| LOAD_FAST | 121,080,159 | 23.1% | 23.1% |  |
| POP_JUMP_IF_FALSE | 28,468,421 | 5.4% | 28.6% |  |
| STORE_FAST | 27,728,728 | 5.3% | 33.9% |  |
| LOAD_ATTR_INSTANCE_VALUE | 24,593,489 | 4.7% | 38.6% |  |
| RESUME_CHECK | 22,261,704 | 4.3% | 42.8% | 0.0% |
| TO_BOOL_BOOL | 20,686,580 | 4.0% | 46.8% |  |
| LOAD_ATTR | 16,870,443 | 3.2% | 50.0% |  |
| LOAD_ATTR_METHOD_NO_DICT | 15,853,511 | 3.0% | 53.0% |  |
| LOAD_ATTR_WITH_HINT | 15,611,547 | 3.0% | 56.0% |  |
| LOAD_CONST | 14,262,338 | 2.7% | 58.7% |  |
| POP_TOP | 13,807,009 | 2.6% | 61.4% |  |
| LOAD_ATTR_METHOD_WITH_VALUES | 12,646,069 | 2.4% | 63.8% | 0.0% |
| CALL_PY_EXACT_ARGS | 12,492,392 | 2.4% | 66.2% | 0.0% |
| POP_JUMP_IF_TRUE | 11,568,161 | 2.2% | 68.4% |  |
| RETURN_VALUE | 10,579,384 | 2.0% | 70.4% |  |
| RETURN_CONST | 10,058,495 | 1.9% | 72.3% |  |
| CALL | 8,850,497 | 1.7% | 74.0% |  |
| JUMP_BACKWARD | 7,873,302 | 1.5% | 75.5% |  |
| TO_BOOL | 7,574,737 | 1.4% | 77.0% |  |
| LOAD_FAST_LOAD_FAST | 7,451,876 | 1.4% | 78.4% |  |
| POP_JUMP_IF_NONE | 7,405,088 | 1.4% | 79.8% |  |
| LOAD_ATTR_SLOT | 6,916,679 | 1.3% | 81.1% | 0.0% |
| LOAD_GLOBAL_MODULE | 6,869,536 | 1.3% | 82.4% | 0.0% |
| CALL_PY_WITH_DEFAULTS | 5,451,314 | 1.0% | 83.5% |  |
| LOAD_FAST_CHECK | 5,120,320 | 1.0% | 84.4% |  |
| CALL_LIST_APPEND | 4,846,130 | 0.9% | 85.4% |  |
| NOP | 4,693,875 | 0.9% | 86.3% |  |
| STORE_ATTR_SLOT | 4,664,733 | 0.9% | 87.2% | 0.1% |
| COMPARE_OP_INT | 4,662,190 | 0.9% | 88.0% | 0.0% |
| LOAD_GLOBAL_BUILTIN | 4,208,711 | 0.8% | 88.9% | 0.0% |
| TO_BOOL_INT | 3,190,189 | 0.6% | 89.5% |  |
| CALL_LEN | 2,968,940 | 0.6% | 90.0% |  |
| PUSH_NULL | 2,742,086 | 0.5% | 90.6% |  |
| LOAD_ATTR_MODULE | 2,443,064 | 0.5% | 91.0% | 0.0% |
| INTERPRETER_EXIT | 2,345,238 | 0.4% | 91.5% |  |
| BINARY_OP | 2,225,987 | 0.4% | 91.9% |  |
| CALL_METHOD_DESCRIPTOR_O | 2,059,425 | 0.4% | 92.3% | 0.0% |
| BUILD_LIST | 1,663,773 | 0.3% | 92.6% |  |
| LOAD_DEREF | 1,652,125 | 0.3% | 92.9% |  |
| STORE_ATTR_INSTANCE_VALUE | 1,639,027 | 0.3% | 93.2% |  |
| SEND_GEN | 1,637,765 | 0.3% | 93.5% |  |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,396,058 | 0.3% | 93.8% | 0.1% |
| FOR_ITER_LIST | 1,379,692 | 0.3% | 94.1% |  |
| BUILD_TUPLE | 1,372,751 | 0.3% | 94.3% |  |
| POP_JUMP_IF_NOT_NONE | 1,367,625 | 0.3% | 94.6% |  |
| FOR_ITER_RANGE | 1,359,435 | 0.3% | 94.9% |  |
| JUMP_FORWARD | 1,322,015 | 0.3% | 95.1% |  |
| YIELD_VALUE | 1,308,596 | 0.2% | 95.4% |  |
| JUMP_BACKWARD_NO_INTERRUPT | 1,308,356 | 0.2% | 95.6% |  |
| TO_BOOL_NONE | 1,305,558 | 0.2% | 95.9% | 0.0% |
| STORE_FAST_STORE_FAST | 1,110,496 | 0.2% | 96.1% |  |
| UNPACK_SEQUENCE_TWO_TUPLE | 1,109,936 | 0.2% | 96.3% |  |
| COPY | 1,075,383 | 0.2% | 96.5% |  |
| CALL_FUNCTION_EX | 1,019,086 | 0.2% | 96.7% |  |
| LIST_EXTEND | 1,018,486 | 0.2% | 96.9% |  |
| CALL_INTRINSIC_1 | 1,018,426 | 0.2% | 97.1% |  |
| COMPARE_OP | 989,083 | 0.2% | 97.3% |  |
| END_SEND | 987,847 | 0.2% | 97.4% |  |
| GET_AWAITABLE | 987,847 | 0.2% | 97.6% |  |
| GET_ITER | 984,267 | 0.2% | 97.8% |  |
| CALL_METHOD_DESCRIPTOR_FAST | 707,211 | 0.1% | 98.0% |  |
| BINARY_SLICE | 699,946 | 0.1% | 98.1% |  |
| STORE_ATTR_WITH_HINT | 691,080 | 0.1% | 98.2% |  |
| BINARY_OP_ADD_INT | 677,478 | 0.1% | 98.4% |  |
| CONTAINS_OP | 662,249 | 0.1% | 98.5% |  |
| SEND | 659,618 | 0.1% | 98.6% |  |
| RETURN_GENERATOR | 659,338 | 0.1% | 98.7% |  |
| TO_BOOL_LIST | 645,498 | 0.1% | 98.9% |  |
| SWAP | 395,602 | 0.1% | 98.9% |  |
| CALL_BUILTIN_CLASS | 385,982 | 0.1% | 99.0% |  |
| COPY_FREE_VARS | 349,995 | 0.1% | 99.1% |  |
| CALL_KW | 341,134 | 0.1% | 99.1% |  |
| CALL_BOUND_METHOD_EXACT_ARGS | 329,614 | 0.1% | 99.2% | 0.1% |
| DELETE_SUBSCR | 328,729 | 0.1% | 99.3% |  |
| CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS | 323,289 | 0.1% | 99.3% | 0.0% |
| BINARY_OP_ADD_FLOAT | 322,149 | 0.1% | 99.4% |  |
| CHECK_EXC_MATCH | 321,949 | 0.1% | 99.4% |  |
| POP_EXCEPT | 321,949 | 0.1% | 99.5% |  |
| PUSH_EXC_INFO | 321,949 | 0.1% | 99.6% |  |
| MAKE_CELL | 321,920 | 0.1% | 99.6% |  |
| LOAD_ATTR_PROPERTY | 321,829 | 0.1% | 99.7% |  |
| MAKE_FUNCTION | 321,780 | 0.1% | 99.8% |  |
| SET_FUNCTION_ATTRIBUTE | 321,140 | 0.1% | 99.8% |  |
| BINARY_OP_MULTIPLY_INT | 320,969 | 0.1% | 99.9% |  |
| BUILD_SLICE | 320,729 | 0.1% | 99.9% |  |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 53,968 | 0.0% | 100.0% | 0.2% |
| CALL_ISINSTANCE | 36,590 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_DICT | 19,825 | 0.0% | 100.0% |  |
| FOR_ITER_TUPLE | 17,920 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_INT | 17,780 | 0.0% | 100.0% |  |
| FOR_ITER | 17,480 | 0.0% | 100.0% |  |
| EXTENDED_ARG | 16,920 | 0.0% | 100.0% |  |
| LOAD_GLOBAL | 13,980 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_LIST_INT | 13,178 | 0.0% | 100.0% |  |
| MAP_ADD | 12,920 | 0.0% | 100.0% |  |
| STORE_ATTR | 12,580 | 0.0% | 100.0% |  |
| STORE_SUBSCR | 10,980 | 0.0% | 100.0% |  |
| STORE_SUBSCR_DICT | 9,385 | 0.0% | 100.0% |  |
| BINARY_SUBSCR | 8,700 | 0.0% | 100.0% |  |
| COMPARE_OP_FLOAT | 6,529 | 0.0% | 100.0% |  |
| RESUME | 5,620 | 0.0% | 100.0% | 0.4% |
| LOAD_SUPER_ATTR_METHOD | 3,520 | 0.0% | 100.0% |  |
| LIST_APPEND | 2,560 | 0.0% | 100.0% |  |
| IS_OP | 2,400 | 0.0% | 100.0% |  |
| BUILD_MAP | 2,180 | 0.0% | 100.0% |  |
| TO_BOOL_STR | 1,840 | 0.0% | 100.0% | 3.3% |
| CALL_BUILTIN_FAST | 1,780 | 0.0% | 100.0% | 1.1% |
| STORE_FAST_LOAD_FAST | 1,260 | 0.0% | 100.0% |  |
| CALL_BUILTIN_O | 1,180 | 0.0% | 100.0% | 5.1% |
| STORE_NAME | 1,160 | 0.0% | 100.0% |  |
| BINARY_OP_ADD_UNICODE | 1,060 | 0.0% | 100.0% |  |
| CALL_TYPE_1 | 1,040 | 0.0% | 100.0% |  |
| COMPARE_OP_STR | 1,020 | 0.0% | 100.0% | 2.0% |
| LOAD_SUPER_ATTR | 1,020 | 0.0% | 100.0% |  |
| LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES | 880 | 0.0% | 100.0% | 13.6% |
| UNARY_INVERT | 880 | 0.0% | 100.0% |  |
| STORE_DEREF | 880 | 0.0% | 100.0% |  |
| LOAD_SUPER_ATTR_ATTR | 820 | 0.0% | 100.0% |  |
| DICT_UPDATE | 760 | 0.0% | 100.0% |  |
| LOAD_NAME | 760 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE | 760 | 0.0% | 100.0% |  |
| CALL_ALLOC_AND_ENTER_INIT | 720 | 0.0% | 100.0% | 2.8% |
| EXIT_INIT_CHECK | 700 | 0.0% | 100.0% |  |
| LOAD_FAST_AND_CLEAR | 680 | 0.0% | 100.0% |  |
| BEFORE_WITH | 560 | 0.0% | 100.0% |  |
| UNARY_NOT | 520 | 0.0% | 100.0% |  |
| DICT_MERGE | 460 | 0.0% | 100.0% |  |
| TO_BOOL_ALWAYS_TRUE | 400 | 0.0% | 100.0% | 10.0% |
| BUILD_SET | 400 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_GETITEM | 400 | 0.0% | 100.0% |  |
| LOAD_ATTR_CLASS | 380 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_TUPLE_INT | 360 | 0.0% | 100.0% |  |
| UNPACK_SEQUENCE_TUPLE | 280 | 0.0% | 100.0% |  |
| BINARY_SUBSCR_STR_INT | 240 | 0.0% | 100.0% | 58.3% |
| IMPORT_NAME | 200 | 0.0% | 100.0% |  |
| BINARY_OP_SUBTRACT_FLOAT | 200 | 0.0% | 100.0% |  |
| BINARY_OP_MULTIPLY_FLOAT | 140 | 0.0% | 100.0% |  |
| CALL_STR_1 | 120 | 0.0% | 100.0% |  |
| LOAD_BUILD_CLASS | 100 | 0.0% | 100.0% |  |
| BUILD_CONST_KEY_MAP | 100 | 0.0% | 100.0% |  |
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
| LOAD_FAST LOAD_ATTR_INSTANCE_VALUE | 24,568,699 | 4.7% | 4.7% |
| STORE_FAST LOAD_FAST | 19,031,665 | 3.6% | 8.3% |
| TO_BOOL_BOOL POP_JUMP_IF_FALSE | 17,989,235 | 3.4% | 11.8% |
| RESUME_CHECK LOAD_FAST | 16,835,551 | 3.2% | 15.0% |
| POP_JUMP_IF_FALSE LOAD_FAST | 15,327,360 | 2.9% | 17.9% |
| LOAD_FAST LOAD_ATTR_WITH_HINT | 12,683,072 | 2.4% | 20.3% |
| LOAD_ATTR_METHOD_NO_DICT LOAD_FAST | 12,363,525 | 2.4% | 22.7% |
| CALL_PY_EXACT_ARGS RESUME_CHECK | 11,503,789 | 2.2% | 24.9% |
| LOAD_FAST LOAD_ATTR | 10,914,376 | 2.1% | 27.0% |
| LOAD_FAST TO_BOOL_BOOL | 10,570,743 | 2.0% | 29.0% |
| POP_JUMP_IF_TRUE LOAD_FAST | 9,221,420 | 1.8% | 30.8% |
| RETURN_CONST POP_TOP | 8,365,975 | 1.6% | 32.4% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_NO_DICT | 8,162,944 | 1.6% | 33.9% |
| RETURN_VALUE STORE_FAST | 7,784,214 | 1.5% | 35.4% |
| TO_BOOL POP_JUMP_IF_TRUE | 7,216,843 | 1.4% | 36.8% |
| LOAD_ATTR_METHOD_WITH_VALUES LOAD_FAST | 7,209,181 | 1.4% | 38.2% |
| LOAD_FAST RETURN_VALUE | 7,120,306 | 1.4% | 39.5% |
| POP_JUMP_IF_NONE LOAD_FAST | 7,080,699 | 1.4% | 40.9% |
| LOAD_FAST LOAD_ATTR_SLOT | 6,900,130 | 1.3% | 42.2% |
| CALL STORE_FAST | 6,817,095 | 1.3% | 43.5% |
| LOAD_FAST TO_BOOL | 6,483,114 | 1.2% | 44.7% |
| LOAD_FAST POP_JUMP_IF_NONE | 6,423,941 | 1.2% | 46.0% |
| LOAD_ATTR_WITH_HINT LOAD_ATTR_METHOD_WITH_VALUES | 6,115,659 | 1.2% | 47.1% |
| LOAD_FAST CALL | 6,107,568 | 1.2% | 48.3% |
| JUMP_BACKWARD LOAD_FAST | 6,083,662 | 1.2% | 49.4% |
| CALL_PY_WITH_DEFAULTS RESUME_CHECK | 5,451,194 | 1.0% | 50.5% |
| LOAD_ATTR CALL_PY_WITH_DEFAULTS | 5,441,029 | 1.0% | 51.5% |
| LOAD_CONST LOAD_FAST | 4,972,971 | 0.9% | 52.5% |
| CALL_LIST_APPEND JUMP_BACKWARD | 4,845,630 | 0.9% | 53.4% |
| POP_TOP RETURN_CONST | 4,694,063 | 0.9% | 54.3% |
| LOAD_ATTR_INSTANCE_VALUE TO_BOOL_BOOL | 4,616,752 | 0.9% | 55.2% |
| LOAD_CONST STORE_FAST | 4,570,984 | 0.9% | 56.1% |
| LOAD_FAST CALL_LIST_APPEND | 4,479,053 | 0.9% | 56.9% |
| POP_JUMP_IF_FALSE LOAD_FAST_CHECK | 4,478,873 | 0.9% | 57.8% |
| LOAD_FAST_CHECK LOAD_ATTR_METHOD_NO_DICT | 4,478,833 | 0.9% | 58.6% |
| LOAD_FAST LOAD_ATTR_METHOD_WITH_VALUES | 4,473,709 | 0.9% | 59.5% |
| POP_TOP LOAD_FAST | 4,357,479 | 0.8% | 60.3% |
| COMPARE_OP_INT POP_JUMP_IF_FALSE | 4,340,381 | 0.8% | 61.1% |
| NOP LOAD_FAST | 4,031,287 | 0.8% | 61.9% |
| LOAD_ATTR CALL_PY_EXACT_ARGS | 3,922,883 | 0.7% | 62.7% |
| LOAD_ATTR_METHOD_WITH_VALUES CALL_PY_EXACT_ARGS | 3,812,287 | 0.7% | 63.4% |
| LOAD_GLOBAL_BUILTIN LOAD_FAST | 3,705,416 | 0.7% | 64.1% |
| TO_BOOL_BOOL POP_JUMP_IF_TRUE | 2,696,905 | 0.5% | 64.6% |
| LOAD_FAST_LOAD_FAST STORE_ATTR_SLOT | 2,640,596 | 0.5% | 65.1% |
| POP_JUMP_IF_FALSE LOAD_CONST | 2,637,269 | 0.5% | 65.6% |
| LOAD_ATTR_WITH_HINT TO_BOOL_BOOL | 2,614,585 | 0.5% | 66.1% |
| LOAD_GLOBAL_MODULE LOAD_ATTR_MODULE | 2,440,584 | 0.5% | 66.6% |
| LOAD_FAST CALL_PY_EXACT_ARGS | 2,421,070 | 0.5% | 67.0% |
| LOAD_GLOBAL_MODULE LOAD_ATTR | 2,284,856 | 0.4% | 67.5% |
| LOAD_FAST STORE_ATTR_SLOT | 2,023,517 | 0.4% | 67.9% |
| CACHE RESUME_CHECK | 2,020,838 | 0.4% | 68.3% |
| POP_TOP LOAD_CONST | 1,984,264 | 0.4% | 68.6% |
| STORE_ATTR_SLOT LOAD_FAST_LOAD_FAST | 1,979,902 | 0.4% | 69.0% |
| LOAD_FAST_LOAD_FAST LOAD_ATTR_WITH_HINT | 1,949,276 | 0.4% | 69.4% |
| LOAD_ATTR_WITH_HINT COMPARE_OP_INT | 1,949,156 | 0.4% | 69.8% |
| TO_BOOL_INT POP_JUMP_IF_FALSE | 1,859,345 | 0.4% | 70.1% |
| LOAD_FAST LOAD_ATTR_METHOD_NO_DICT | 1,854,476 | 0.4% | 70.5% |
| LOAD_ATTR_SLOT TO_BOOL_BOOL | 1,819,862 | 0.3% | 70.8% |
| LOAD_FAST LOAD_GLOBAL_MODULE | 1,794,657 | 0.3% | 71.2% |
| CALL_METHOD_DESCRIPTOR_O POP_TOP | 1,729,847 | 0.3% | 71.5% |
| LOAD_ATTR_MODULE PUSH_NULL | 1,692,425 | 0.3% | 71.8% |
| POP_JUMP_IF_FALSE RETURN_CONST | 1,679,783 | 0.3% | 72.1% |
| LOAD_FAST LOAD_CONST | 1,677,105 | 0.3% | 72.5% |
| LOAD_FAST STORE_ATTR_INSTANCE_VALUE | 1,629,787 | 0.3% | 72.8% |
| LOAD_ATTR_WITH_HINT LOAD_GLOBAL_MODULE | 1,621,727 | 0.3% | 73.1% |
| LOAD_ATTR_INSTANCE_VALUE CALL_LEN | 1,606,636 | 0.3% | 73.4% |
| PUSH_NULL LOAD_FAST | 1,413,233 | 0.3% | 73.6% |
| STORE_FAST LOAD_FAST_LOAD_FAST | 1,398,036 | 0.3% | 73.9% |
| LOAD_FAST CALL_METHOD_DESCRIPTOR_O | 1,378,455 | 0.3% | 74.2% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR_METHOD_WITH_VALUES | 1,366,093 | 0.3% | 74.4% |
| STORE_FAST LOAD_GLOBAL_BUILTIN | 1,356,064 | 0.3% | 74.7% |
| RETURN_CONST INTERPRETER_EXIT | 1,353,371 | 0.3% | 75.0% |
| RESUME_CHECK LOAD_GLOBAL_MODULE | 1,353,255 | 0.3% | 75.2% |
| STORE_FAST RETURN_CONST | 1,339,695 | 0.3% | 75.5% |
| TO_BOOL_INT POP_JUMP_IF_TRUE | 1,330,764 | 0.3% | 75.7% |
| POP_JUMP_IF_FALSE NOP | 1,329,566 | 0.3% | 76.0% |
| STORE_ATTR_SLOT LOAD_CONST | 1,329,213 | 0.3% | 76.2% |
| STORE_FAST JUMP_FORWARD | 1,312,975 | 0.3% | 76.5% |
| LOAD_ATTR_INSTANCE_VALUE LOAD_ATTR | 1,308,998 | 0.3% | 76.7% |
| RESUME_CHECK JUMP_BACKWARD_NO_INTERRUPT | 1,307,876 | 0.2% | 77.0% |
| TO_BOOL_NONE POP_JUMP_IF_FALSE | 1,305,498 | 0.2% | 77.2% |
| LOAD_CONST COMPARE_OP_INT | 1,304,226 | 0.2% | 77.5% |
| LOAD_ATTR_SLOT TO_BOOL_NONE | 1,303,218 | 0.2% | 77.7% |
| UNPACK_SEQUENCE_TWO_TUPLE STORE_FAST_STORE_FAST | 1,109,776 | 0.2% | 77.9% |
| STORE_FAST_STORE_FAST LOAD_FAST | 1,108,616 | 0.2% | 78.2% |
| POP_TOP JUMP_BACKWARD | 1,079,794 | 0.2% | 78.4% |
| LOAD_ATTR_METHOD_NO_DICT CALL_METHOD_DESCRIPTOR_NOARGS | 1,065,589 | 0.2% | 78.6% |
| CALL_METHOD_DESCRIPTOR_NOARGS STORE_FAST | 1,063,329 | 0.2% | 78.8% |
| COPY TO_BOOL_INT | 1,055,903 | 0.2% | 79.0% |
| LOAD_GLOBAL_MODULE BINARY_OP | 1,055,863 | 0.2% | 79.2% |
| RESUME_CHECK NOP | 1,054,421 | 0.2% | 79.4% |
| LOAD_ATTR LOAD_FAST | 1,049,120 | 0.2% | 79.6% |
| LOAD_FAST POP_JUMP_IF_NOT_NONE | 1,043,676 | 0.2% | 79.8% |
| LOAD_FAST_LOAD_FAST LOAD_FAST | 1,042,571 | 0.2% | 80.0% |
| LOAD_FAST CALL_LEN | 1,040,995 | 0.2% | 80.2% |
| LOAD_ATTR_INSTANCE_VALUE RETURN_VALUE | 1,040,773 | 0.2% | 80.4% |
| FOR_ITER_RANGE STORE_FAST | 1,037,386 | 0.2% | 80.6% |
| JUMP_BACKWARD FOR_ITER_RANGE | 1,037,306 | 0.2% | 80.8% |
| LOAD_ATTR_METHOD_NO_DICT CALL_PY_EXACT_ARGS | 1,026,491 | 0.2% | 81.0% |
| LOAD_ATTR PUSH_NULL | 1,020,186 | 0.2% | 81.2% |


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each opcode </summary>

### BINARY_SLICE

<details>
<summary> Successors and predecessors for BINARY_SLICE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 642,938 | 91.9% |
| LOAD_CONST | 46,768 | 6.7% |
| BINARY_OP_ADD_INT | 10,240 | 1.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_METHOD_DESCRIPTOR_O | 358,332 | 51.2% |
| CALL | 320,749 | 45.8% |
| STORE_FAST | 18,745 | 2.7% |
| LOAD_CONST | 1,280 | 0.2% |
| LIST_EXTEND | 240 | 0.0% |


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
| RESUME_CHECK | 2,020,838 | 86.2% |
| COPY_FREE_VARS | 322,600 | 13.8% |
| RESUME | 940 | 0.0% |
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
| LOAD_CONST | 8,280 | 95.2% |
| BINARY_SUBSCR | 160 | 1.8% |
| LOAD_FAST | 160 | 1.8% |
| BUILD_SLICE | 60 | 0.7% |
| RETURN_VALUE | 40 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,080 | 93.1% |
| BINARY_SUBSCR | 160 | 1.8% |
| BINARY_SUBSCR_LIST_INT | 100 | 1.2% |
| BINARY_SUBSCR_DICT | 80 | 0.9% |
| LOAD_ATTR | 60 | 0.7% |


</details>

### CHECK_EXC_MATCH

<details>
<summary> Successors and predecessors for CHECK_EXC_MATCH </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 321,009 | 99.7% |
| LOAD_GLOBAL_BUILTIN | 680 | 0.2% |
| BUILD_TUPLE | 160 | 0.0% |
| LOAD_GLOBAL | 100 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 321,949 | 100.0% |


</details>

### DELETE_SUBSCR

<details>
<summary> Successors and predecessors for DELETE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BUILD_SLICE | 320,669 | 97.5% |
| LOAD_CONST | 8,000 | 2.4% |
| LOAD_FAST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 328,669 | 100.0% |
| LOAD_GLOBAL_MODULE | 60 | 0.0% |


</details>

### END_SEND

<details>
<summary> Successors and predecessors for END_SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 337,149 | 34.1% |
| SEND | 328,989 | 33.3% |
| RETURN_VALUE | 321,709 | 32.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 666,298 | 67.4% |
| STORE_FAST | 321,149 | 32.5% |
| UNPACK_SEQUENCE | 120 | 0.0% |
| UNPACK_SEQUENCE_TWO_TUPLE | 120 | 0.0% |
| RETURN_VALUE | 80 | 0.0% |


</details>

### EXIT_INIT_CHECK

<details>
<summary> Successors and predecessors for EXIT_INIT_CHECK </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 700 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 700 | 100.0% |


</details>

### GET_ITER

<details>
<summary> Successors and predecessors for GET_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 653,458 | 66.4% |
| CALL_BUILTIN_CLASS | 322,109 | 32.7% |
| LOAD_ATTR_INSTANCE_VALUE | 8,140 | 0.8% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 180 | 0.0% |
| BINARY_SLICE | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_LIST | 644,618 | 65.5% |
| FOR_ITER_RANGE | 322,029 | 32.7% |
| FOR_ITER | 8,720 | 0.9% |
| FOR_ITER_TUPLE | 8,060 | 0.8% |
| LOAD_FAST_AND_CLEAR | 680 | 0.1% |


</details>

### INTERPRETER_EXIT

<details>
<summary> Successors and predecessors for INTERPRETER_EXIT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 1,353,371 | 57.7% |
| RETURN_VALUE | 662,238 | 28.2% |
| YIELD_VALUE | 329,229 | 14.0% |
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
| POP_JUMP_IF_FALSE | 1,329,566 | 28.3% |
| RESUME_CHECK | 1,054,421 | 22.5% |
| POP_JUMP_IF_TRUE | 650,643 | 13.9% |
| STORE_FAST | 645,878 | 13.8% |
| NOP | 641,998 | 13.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,031,287 | 85.9% |
| NOP | 641,998 | 13.7% |
| LOAD_GLOBAL_MODULE | 19,290 | 0.4% |
| LOAD_GLOBAL_BUILTIN | 340 | 0.0% |
| LOAD_CONST | 300 | 0.0% |


</details>

### POP_EXCEPT

<details>
<summary> Successors and predecessors for POP_EXCEPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 321,589 | 99.9% |
| STORE_FAST | 160 | 0.0% |
| SWAP | 100 | 0.0% |
| COPY | 80 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 320,869 | 99.7% |
| RETURN_CONST | 660 | 0.2% |
| RETURN_VALUE | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |


</details>

### POP_TOP

<details>
<summary> Successors and predecessors for POP_TOP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 8,365,975 | 60.6% |
| CALL_METHOD_DESCRIPTOR_O | 1,729,847 | 12.5% |
| CALL_FUNCTION_EX | 1,017,986 | 7.4% |
| POP_JUMP_IF_FALSE | 689,546 | 5.0% |
| END_SEND | 666,298 | 4.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_CONST | 4,694,063 | 34.0% |
| LOAD_FAST | 4,357,479 | 31.6% |
| LOAD_CONST | 1,984,264 | 14.4% |
| JUMP_BACKWARD | 1,079,794 | 7.8% |
| RESUME_CHECK | 658,858 | 4.8% |


</details>

### PUSH_EXC_INFO

<details>
<summary> Successors and predecessors for PUSH_EXC_INFO </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 320,809 | 99.6% |
| BINARY_SUBSCR_DICT | 520 | 0.2% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 360 | 0.1% |
| RERAISE | 80 | 0.0% |
| CALL_METHOD_DESCRIPTOR_O | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 320,949 | 99.7% |
| LOAD_GLOBAL_BUILTIN | 720 | 0.2% |
| LOAD_GLOBAL | 280 | 0.1% |


</details>

### PUSH_NULL

<details>
<summary> Successors and predecessors for PUSH_NULL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 1,692,425 | 61.7% |
| LOAD_ATTR | 1,020,186 | 37.2% |
| LOAD_DEREF | 24,255 | 0.9% |
| LOAD_FAST | 4,540 | 0.2% |
| LOAD_NAME | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,413,233 | 51.5% |
| LOAD_FAST_LOAD_FAST | 671,239 | 24.5% |
| CALL | 655,514 | 23.9% |
| LOAD_CONST | 840 | 0.0% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |


</details>

### RETURN_GENERATOR

<details>
<summary> Successors and predecessors for RETURN_GENERATOR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_EXACT_ARGS | 657,798 | 99.8% |
| CALL_KW | 400 | 0.1% |
| CACHE | 320 | 0.0% |
| CALL | 300 | 0.0% |
| MAKE_CELL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_AWAITABLE | 658,458 | 99.9% |
| INTERPRETER_EXIT | 400 | 0.1% |
| CALL | 200 | 0.0% |
| STORE_FAST | 160 | 0.0% |
| LIST_APPEND | 80 | 0.0% |


</details>

### RETURN_VALUE

<details>
<summary> Successors and predecessors for RETURN_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,120,306 | 67.3% |
| LOAD_ATTR_INSTANCE_VALUE | 1,040,773 | 9.8% |
| CALL | 690,526 | 6.5% |
| LOAD_ATTR | 641,409 | 6.1% |
| BINARY_OP_ADD_INT | 337,449 | 3.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 7,784,214 | 73.6% |
| TO_BOOL_BOOL | 694,259 | 6.6% |
| LOAD_FAST | 690,146 | 6.5% |
| INTERPRETER_EXIT | 662,238 | 6.3% |
| POP_TOP | 339,310 | 3.2% |


</details>

### STORE_SUBSCR

<details>
<summary> Successors and predecessors for STORE_SUBSCR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 10,240 | 93.3% |
| LOAD_FAST_LOAD_FAST | 200 | 1.8% |
| LOAD_ATTR_INSTANCE_VALUE | 140 | 1.3% |
| LOAD_CONST | 120 | 1.1% |
| LOAD_FAST | 120 | 1.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 10,080 | 91.8% |
| LOAD_FAST | 220 | 2.0% |
| RETURN_CONST | 180 | 1.6% |
| JUMP_FORWARD | 160 | 1.5% |
| STORE_SUBSCR_DICT | 160 | 1.5% |


</details>

### TO_BOOL

<details>
<summary> Successors and predecessors for TO_BOOL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,483,114 | 85.6% |
| LOAD_ATTR_INSTANCE_VALUE | 743,474 | 9.8% |
| LOAD_ATTR_WITH_HINT | 336,989 | 4.4% |
| TO_BOOL | 4,860 | 0.1% |
| LOAD_ATTR | 2,560 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_TRUE | 7,216,843 | 95.3% |
| POP_JUMP_IF_FALSE | 349,054 | 4.6% |
| TO_BOOL | 4,860 | 0.1% |
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
| LOAD_GLOBAL_MODULE | 1,055,863 | 47.4% |
| LOAD_ATTR_MODULE | 741,079 | 33.3% |
| LOAD_ATTR | 366,757 | 16.5% |
| POP_JUMP_IF_FALSE | 46,008 | 2.1% |
| LOAD_CONST | 11,660 | 0.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COPY | 734,314 | 33.0% |
| TO_BOOL_INT | 733,694 | 33.0% |
| STORE_FAST | 368,797 | 16.6% |
| BUILD_TUPLE | 366,597 | 16.5% |
| STORE_SUBSCR | 10,240 | 0.5% |


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
| LOAD_ATTR_SLOT | 1,017,646 | 61.2% |
| STORE_FAST | 322,129 | 19.4% |
| LOAD_FAST | 321,558 | 19.3% |
| SWAP | 680 | 0.0% |
| STORE_ATTR_INSTANCE_VALUE | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,018,966 | 61.2% |
| STORE_FAST | 643,407 | 38.7% |
| SWAP | 680 | 0.0% |
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
| LOAD_FAST | 320,669 | 100.0% |
| LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| DELETE_SUBSCR | 320,669 | 100.0% |
| BINARY_SUBSCR | 60 | 0.0% |


</details>

### BUILD_TUPLE

<details>
<summary> Successors and predecessors for BUILD_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 649,309 | 47.3% |
| BINARY_OP | 366,597 | 26.7% |
| LOAD_FAST | 329,820 | 24.0% |
| LOAD_GLOBAL_BUILTIN | 16,660 | 1.2% |
| LOAD_FAST_LOAD_FAST | 9,145 | 0.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CONTAINS_OP | 649,309 | 47.3% |
| CALL_LIST_APPEND | 366,677 | 26.7% |
| LOAD_CONST | 321,100 | 23.4% |
| CALL_ISINSTANCE | 16,520 | 1.2% |
| CALL_PY_EXACT_ARGS | 16,225 | 1.2% |


</details>

### CALL

<details>
<summary> Successors and predecessors for CALL </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,107,568 | 69.0% |
| LOAD_FAST_LOAD_FAST | 660,954 | 7.5% |
| PUSH_NULL | 655,514 | 7.4% |
| LOAD_ATTR_INSTANCE_VALUE | 650,663 | 7.4% |
| LOAD_CONST | 339,654 | 3.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 6,817,095 | 77.0% |
| RETURN_VALUE | 690,526 | 7.8% |
| RESUME_CHECK | 333,045 | 3.8% |
| POP_TOP | 333,009 | 3.8% |
| LOAD_CONST | 320,869 | 3.6% |


</details>

### CALL_FUNCTION_EX

<details>
<summary> Successors and predecessors for CALL_FUNCTION_EX </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,018,066 | 99.9% |
| DICT_MERGE | 460 | 0.0% |
| BUILD_MAP | 320 | 0.0% |
| LOAD_FAST | 160 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,017,986 | 99.9% |
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
| LIST_EXTEND | 1,018,426 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_FUNCTION_EX | 1,018,066 | 100.0% |
| LOAD_CONST | 320 | 0.0% |
| BUILD_MAP | 40 | 0.0% |


</details>

### CALL_KW

<details>
<summary> Successors and predecessors for CALL_KW </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 341,134 | 100.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 329,089 | 96.5% |
| COPY_FREE_VARS | 8,025 | 2.4% |
| RESUME_CHECK | 1,280 | 0.4% |
| STORE_FAST | 1,200 | 0.4% |
| POP_TOP | 480 | 0.1% |


</details>

### COMPARE_OP

<details>
<summary> Successors and predecessors for COMPARE_OP </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 983,063 | 99.4% |
| COMPARE_OP | 2,380 | 0.2% |
| LOAD_CONST | 1,400 | 0.1% |
| LOAD_ATTR_MODULE | 940 | 0.1% |
| LOAD_GLOBAL_MODULE | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 985,323 | 99.6% |
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
| BUILD_TUPLE | 649,309 | 98.0% |
| LOAD_FAST | 10,980 | 1.7% |
| LOAD_ATTR_INSTANCE_VALUE | 440 | 0.1% |
| BUILD_SET | 400 | 0.1% |
| LOAD_GLOBAL_MODULE | 280 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 661,449 | 99.9% |
| POP_JUMP_IF_TRUE | 720 | 0.1% |
| STORE_FAST | 60 | 0.0% |
| EXTENDED_ARG | 20 | 0.0% |


</details>

### COPY

<details>
<summary> Successors and predecessors for COPY </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| BINARY_OP | 734,314 | 68.3% |
| CALL_LEN | 321,849 | 29.9% |
| LOAD_FAST | 17,440 | 1.6% |
| SWAP | 720 | 0.1% |
| UNARY_NOT | 260 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_INT | 1,055,903 | 98.2% |
| LOAD_ATTR_WITH_HINT | 16,040 | 1.5% |
| LOAD_ATTR_INSTANCE_VALUE | 840 | 0.1% |
| COMPARE_OP_INT | 600 | 0.1% |
| TO_BOOL | 500 | 0.0% |


</details>

### COPY_FREE_VARS

<details>
<summary> Successors and predecessors for COPY_FREE_VARS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CACHE | 322,600 | 92.2% |
| CALL_PY_EXACT_ARGS | 10,185 | 2.9% |
| CALL_KW | 8,025 | 2.3% |
| CALL_BOUND_METHOD_EXACT_ARGS | 8,005 | 2.3% |
| LOAD_ATTR_PROPERTY | 580 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 349,095 | 99.7% |
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

### EXTENDED_ARG

<details>
<summary> Successors and predecessors for EXTENDED_ARG </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| MAP_ADD | 9,480 | 56.0% |
| LOAD_CONST | 5,420 | 32.0% |
| BUILD_MAP | 580 | 3.4% |
| STORE_NAME | 360 | 2.1% |
| PUSH_NULL | 200 | 1.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 16,080 | 95.0% |
| JUMP_BACKWARD | 340 | 2.0% |
| FOR_ITER_LIST | 280 | 1.7% |
| POP_JUMP_IF_FALSE | 120 | 0.7% |
| JUMP_FORWARD | 60 | 0.4% |


</details>

### FOR_ITER

<details>
<summary> Successors and predecessors for FOR_ITER </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 8,720 | 49.9% |
| JUMP_BACKWARD | 8,380 | 47.9% |
| FOR_ITER | 280 | 1.6% |
| LOAD_FAST | 80 | 0.5% |
| SWAP | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,420 | 48.2% |
| RETURN_CONST | 8,140 | 46.6% |
| FOR_ITER | 280 | 1.6% |
| FOR_ITER_LIST | 280 | 1.6% |
| LOAD_FAST | 120 | 0.7% |


</details>

### GET_AWAITABLE

<details>
<summary> Successors and predecessors for GET_AWAITABLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RETURN_GENERATOR | 658,458 | 66.7% |
| LOAD_ATTR_INSTANCE_VALUE | 320,569 | 32.5% |
| LOAD_FAST | 8,160 | 0.8% |
| RETURN_VALUE | 240 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 987,847 | 100.0% |


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
| LOAD_GLOBAL_MODULE | 940 | 39.2% |
| LOAD_FAST | 800 | 33.3% |
| LOAD_CONST | 560 | 23.3% |
| LOAD_FAST_LOAD_FAST | 80 | 3.3% |
| LOAD_GLOBAL_BUILTIN | 20 | 0.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,720 | 71.7% |
| RETURN_VALUE | 400 | 16.7% |
| LOAD_DEREF | 160 | 6.7% |
| POP_JUMP_IF_TRUE | 120 | 5.0% |


</details>

### JUMP_BACKWARD

<details>
<summary> Successors and predecessors for JUMP_BACKWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_LIST_APPEND | 4,845,630 | 61.5% |
| POP_TOP | 1,079,794 | 13.7% |
| JUMP_FORWARD | 641,127 | 8.1% |
| POP_JUMP_IF_FALSE | 322,364 | 4.1% |
| POP_JUMP_IF_TRUE | 321,429 | 4.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,083,662 | 77.3% |
| FOR_ITER_RANGE | 1,037,306 | 13.2% |
| FOR_ITER_LIST | 734,454 | 9.3% |
| FOR_ITER_TUPLE | 9,260 | 0.1% |
| FOR_ITER | 8,380 | 0.1% |


</details>

### JUMP_BACKWARD_NO_INTERRUPT

<details>
<summary> Successors and predecessors for JUMP_BACKWARD_NO_INTERRUPT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 1,307,876 | 100.0% |
| RESUME | 480 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SEND_GEN | 979,067 | 74.8% |
| SEND | 329,289 | 25.2% |


</details>

### JUMP_FORWARD

<details>
<summary> Successors and predecessors for JUMP_FORWARD </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,312,975 | 99.3% |
| POP_JUMP_IF_FALSE | 6,389 | 0.5% |
| POP_TOP | 1,211 | 0.1% |
| STORE_ATTR_INSTANCE_VALUE | 480 | 0.0% |
| STORE_ATTR | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 641,127 | 48.5% |
| LOAD_FAST | 350,850 | 26.5% |
| LOAD_GLOBAL_BUILTIN | 328,458 | 24.8% |
| LOAD_FAST_LOAD_FAST | 500 | 0.0% |
| NOP | 340 | 0.0% |


</details>

### LIST_APPEND

<details>
<summary> Successors and predecessors for LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL_BUILTIN_CLASS | 1,280 | 50.0% |
| CALL_METHOD_DESCRIPTOR_FAST | 1,200 | 46.9% |
| RETURN_GENERATOR | 80 | 3.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 2,560 | 100.0% |


</details>

### LIST_EXTEND

<details>
<summary> Successors and predecessors for LIST_EXTEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,017,646 | 99.9% |
| LOAD_FAST | 520 | 0.1% |
| BINARY_SLICE | 240 | 0.0% |
| LOAD_CONST | 60 | 0.0% |
| LOAD_ATTR | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_INTRINSIC_1 | 1,018,426 | 100.0% |
| LOAD_NAME | 60 | 0.0% |


</details>

### LOAD_ATTR

<details>
<summary> Successors and predecessors for LOAD_ATTR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,914,376 | 64.7% |
| LOAD_GLOBAL_MODULE | 2,284,856 | 13.5% |
| LOAD_ATTR_INSTANCE_VALUE | 1,308,998 | 7.8% |
| LOAD_ATTR_SLOT | 1,018,046 | 6.0% |
| LOAD_ATTR_WITH_HINT | 979,777 | 5.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL_PY_WITH_DEFAULTS | 5,441,029 | 32.3% |
| CALL_PY_EXACT_ARGS | 3,922,883 | 23.3% |
| LOAD_FAST | 1,049,120 | 6.2% |
| PUSH_NULL | 1,020,186 | 6.0% |
| COMPARE_OP | 983,063 | 5.8% |


</details>

### LOAD_CONST

<details>
<summary> Successors and predecessors for LOAD_CONST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 2,637,269 | 18.5% |
| POP_TOP | 1,984,264 | 13.9% |
| LOAD_FAST | 1,677,105 | 11.8% |
| STORE_ATTR_SLOT | 1,329,213 | 9.3% |
| GET_AWAITABLE | 987,847 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,972,971 | 34.9% |
| STORE_FAST | 4,570,984 | 32.0% |
| COMPARE_OP_INT | 1,304,226 | 9.1% |
| SEND_GEN | 658,238 | 4.6% |
| CALL_PY_EXACT_ARGS | 641,978 | 4.5% |


</details>

### LOAD_DEREF

<details>
<summary> Successors and predecessors for LOAD_DEREF </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 649,145 | 39.3% |
| STORE_FAST | 328,985 | 19.9% |
| POP_JUMP_IF_FALSE | 321,160 | 19.4% |
| LOAD_CONST | 320,480 | 19.4% |
| LOAD_ATTR | 16,090 | 1.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 961,320 | 58.2% |
| LOAD_ATTR | 321,360 | 19.5% |
| STORE_ATTR_WITH_HINT | 320,360 | 19.4% |
| PUSH_NULL | 24,255 | 1.5% |
| LOAD_FAST | 13,045 | 0.8% |


</details>

### LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 19,031,665 | 15.7% |
| RESUME_CHECK | 16,835,551 | 13.9% |
| POP_JUMP_IF_FALSE | 15,327,360 | 12.7% |
| LOAD_ATTR_METHOD_NO_DICT | 12,363,525 | 10.2% |
| POP_JUMP_IF_TRUE | 9,221,420 | 7.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 24,568,699 | 20.3% |
| LOAD_ATTR_WITH_HINT | 12,683,072 | 10.5% |
| LOAD_ATTR | 10,914,376 | 9.0% |
| TO_BOOL_BOOL | 10,570,743 | 8.7% |
| RETURN_VALUE | 7,120,306 | 5.9% |


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
| POP_JUMP_IF_FALSE | 4,478,873 | 87.5% |
| STORE_FAST | 320,538 | 6.3% |
| LOAD_ATTR_METHOD_NO_DICT | 320,538 | 6.3% |
| POP_TOP | 240 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 4,478,833 | 87.5% |
| LOAD_FAST | 320,558 | 6.3% |
| CALL_METHOD_DESCRIPTOR_O | 320,498 | 6.3% |
| POP_JUMP_IF_NOT_NONE | 240 | 0.0% |
| CALL | 79 | 0.0% |


</details>

### LOAD_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for LOAD_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 1,979,902 | 26.6% |
| STORE_FAST | 1,398,036 | 18.8% |
| POP_JUMP_IF_FALSE | 988,723 | 13.3% |
| LOAD_ATTR_METHOD_NO_DICT | 743,019 | 10.0% |
| PUSH_NULL | 671,239 | 9.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_ATTR_SLOT | 2,640,596 | 35.4% |
| LOAD_ATTR_WITH_HINT | 1,949,276 | 26.2% |
| LOAD_FAST | 1,042,571 | 14.0% |
| CALL | 660,954 | 8.9% |
| LOAD_FAST_LOAD_FAST | 654,489 | 8.8% |


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
| TO_BOOL_BOOL | 17,989,235 | 63.2% |
| COMPARE_OP_INT | 4,340,381 | 15.2% |
| TO_BOOL_INT | 1,859,345 | 6.5% |
| TO_BOOL_NONE | 1,305,498 | 4.6% |
| COMPARE_OP | 985,323 | 3.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 15,327,360 | 53.8% |
| LOAD_FAST_CHECK | 4,478,873 | 15.7% |
| LOAD_CONST | 2,637,269 | 9.3% |
| RETURN_CONST | 1,679,783 | 5.9% |
| NOP | 1,329,566 | 4.7% |


</details>

### POP_JUMP_IF_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,423,941 | 86.8% |
| LOAD_ATTR_INSTANCE_VALUE | 979,447 | 13.2% |
| LOAD_ATTR | 960 | 0.0% |
| LOAD_ATTR_WITH_HINT | 280 | 0.0% |
| CALL | 160 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,080,699 | 95.6% |
| LOAD_CONST | 321,129 | 4.3% |
| RETURN_CONST | 1,520 | 0.0% |
| LOAD_GLOBAL_MODULE | 440 | 0.0% |
| LOAD_FAST_LOAD_FAST | 400 | 0.0% |


</details>

### POP_JUMP_IF_NOT_NONE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_NOT_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,043,676 | 76.3% |
| LOAD_ATTR_INSTANCE_VALUE | 321,909 | 23.5% |
| LOAD_ATTR_WITH_HINT | 600 | 0.0% |
| LOAD_GLOBAL_MODULE | 480 | 0.0% |
| CALL_BUILTIN_FAST | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 702,631 | 51.4% |
| LOAD_GLOBAL_MODULE | 331,745 | 24.3% |
| LOAD_FAST_LOAD_FAST | 330,429 | 24.2% |
| RETURN_CONST | 620 | 0.0% |
| LOAD_GLOBAL | 600 | 0.0% |


</details>

### POP_JUMP_IF_TRUE

<details>
<summary> Successors and predecessors for POP_JUMP_IF_TRUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL | 7,216,843 | 62.4% |
| TO_BOOL_BOOL | 2,696,905 | 23.3% |
| TO_BOOL_INT | 1,330,764 | 11.5% |
| COMPARE_OP_INT | 321,709 | 2.8% |
| CONTAINS_OP | 720 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 9,221,420 | 79.7% |
| NOP | 650,643 | 5.6% |
| RETURN_CONST | 367,297 | 3.2% |
| LOAD_CONST | 362,454 | 3.1% |
| STORE_FAST | 321,869 | 2.8% |


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
| POP_TOP | 4,694,063 | 46.7% |
| POP_JUMP_IF_FALSE | 1,679,783 | 16.7% |
| STORE_FAST | 1,339,695 | 13.3% |
| STORE_ATTR_SLOT | 669,619 | 6.7% |
| STORE_ATTR_INSTANCE_VALUE | 643,849 | 6.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 8,365,975 | 83.2% |
| INTERPRETER_EXIT | 1,353,371 | 13.5% |
| END_SEND | 337,149 | 3.4% |
| EXIT_INIT_CHECK | 700 | 0.0% |
| STORE_FAST | 460 | 0.0% |


</details>

### SEND

<details>
<summary> Successors and predecessors for SEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 329,609 | 50.0% |
| JUMP_BACKWARD_NO_INTERRUPT | 329,289 | 49.9% |
| SEND | 720 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| END_SEND | 328,989 | 49.9% |
| YIELD_VALUE | 328,989 | 49.9% |
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
| RETURN_VALUE | 7,784,214 | 28.1% |
| CALL | 6,817,095 | 24.6% |
| LOAD_CONST | 4,570,984 | 16.5% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,063,329 | 3.8% |
| FOR_ITER_RANGE | 1,037,386 | 3.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 19,031,665 | 68.6% |
| LOAD_FAST_LOAD_FAST | 1,398,036 | 5.0% |
| LOAD_GLOBAL_BUILTIN | 1,356,064 | 4.9% |
| RETURN_CONST | 1,339,695 | 4.8% |
| JUMP_FORWARD | 1,312,975 | 4.7% |


</details>

### STORE_FAST_LOAD_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_LOAD_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| FOR_ITER_TUPLE | 1,200 | 95.2% |
| CALL_LEN | 40 | 3.2% |
| COPY | 20 | 1.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_STR | 1,200 | 95.2% |
| PUSH_NULL | 40 | 3.2% |
| LOAD_ATTR | 20 | 1.6% |


</details>

### STORE_FAST_STORE_FAST

<details>
<summary> Successors and predecessors for STORE_FAST_STORE_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 1,109,776 | 99.9% |
| UNPACK_SEQUENCE | 300 | 0.0% |
| UNPACK_SEQUENCE_TUPLE | 160 | 0.0% |
| COPY | 100 | 0.0% |
| POP_TOP | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,108,616 | 99.8% |
| NOP | 640 | 0.1% |
| LOAD_FAST_LOAD_FAST | 340 | 0.0% |
| LOAD_GLOBAL_MODULE | 320 | 0.0% |
| STORE_FAST | 180 | 0.0% |


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
| LOAD_ATTR | 375,022 | 94.8% |
| BINARY_OP_ADD_INT | 8,680 | 2.2% |
| BINARY_OP_SUBTRACT_INT | 8,400 | 2.1% |
| BUILD_LIST | 680 | 0.2% |
| LOAD_FAST_AND_CLEAR | 680 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 375,622 | 94.9% |
| STORE_ATTR_WITH_HINT | 16,040 | 4.1% |
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
| YIELD_VALUE | 979,367 | 74.8% |
| SEND | 328,989 | 25.1% |
| LOAD_CONST | 160 | 0.0% |
| CALL | 80 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| YIELD_VALUE | 979,367 | 74.8% |
| INTERPRETER_EXIT | 329,229 | 25.2% |


</details>

### RESUME

<details>
<summary> Successors and predecessors for RESUME </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| CALL | 2,920 | 52.0% |
| CACHE | 940 | 16.7% |
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
| LOAD_ATTR_INSTANCE_VALUE | 321,829 | 99.9% |
| LOAD_FAST | 280 | 0.1% |
| BINARY_OP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 321,849 | 99.9% |
| LOAD_FAST | 300 | 0.1% |


</details>

### BINARY_OP_ADD_INT

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 337,429 | 49.8% |
| CALL_LEN | 328,509 | 48.5% |
| LOAD_CONST | 11,340 | 1.7% |
| BINARY_OP | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 337,449 | 49.8% |
| STORE_FAST | 320,769 | 47.3% |
| BINARY_SLICE | 10,240 | 1.5% |
| SWAP | 8,680 | 1.3% |
| LOAD_FAST | 140 | 0.0% |


</details>

### BINARY_OP_ADD_UNICODE

<details>
<summary> Successors and predecessors for BINARY_OP_ADD_UNICODE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 960 | 90.6% |
| BINARY_SUBSCR_LIST_INT | 80 | 7.5% |
| BINARY_OP | 20 | 1.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| CALL | 480 | 45.3% |
| LOAD_FAST | 480 | 45.3% |
| STORE_FAST | 80 | 7.5% |
| LOAD_GLOBAL | 20 | 1.9% |


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
| LOAD_ATTR_INSTANCE_VALUE | 320,549 | 99.9% |
| LOAD_CONST | 320 | 0.1% |
| BINARY_OP | 60 | 0.0% |
| LOAD_ATTR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| COMPARE_OP_INT | 320,589 | 99.9% |
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
| LOAD_FAST | 9,280 | 52.2% |
| LOAD_FAST_LOAD_FAST | 7,960 | 44.8% |
| LOAD_CONST | 400 | 2.2% |
| BINARY_OP | 100 | 0.6% |
| CALL_LEN | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| SWAP | 8,400 | 47.2% |
| STORE_FAST | 8,000 | 45.0% |
| LOAD_FAST | 1,300 | 7.3% |
| RETURN_VALUE | 40 | 0.2% |
| LOAD_FAST_LOAD_FAST | 40 | 0.2% |


</details>

### BINARY_SUBSCR_DICT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 11,580 | 58.4% |
| RETURN_VALUE | 8,065 | 40.7% |
| BINARY_SUBSCR | 80 | 0.4% |
| LOAD_CONST | 80 | 0.4% |
| BUILD_TUPLE | 20 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 10,120 | 51.0% |
| STORE_FAST | 8,205 | 41.4% |
| RETURN_VALUE | 940 | 4.7% |
| PUSH_EXC_INFO | 520 | 2.6% |
| CALL_BUILTIN_CLASS | 40 | 0.2% |


</details>

### BINARY_SUBSCR_GETITEM

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_GETITEM </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 300 | 75.0% |
| LOAD_FAST_LOAD_FAST | 80 | 20.0% |
| BINARY_SUBSCR | 20 | 5.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 400 | 100.0% |


</details>

### BINARY_SUBSCR_LIST_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_LIST_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 13,058 | 99.1% |
| BINARY_SUBSCR | 100 | 0.8% |
| LOAD_FAST | 20 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 6,649 | 50.5% |
| STORE_FAST | 6,269 | 47.6% |
| BINARY_OP_ADD_UNICODE | 80 | 0.6% |
| LOAD_ATTR | 60 | 0.5% |
| RETURN_VALUE | 40 | 0.3% |


</details>

### BINARY_SUBSCR_STR_INT

<details>
<summary> Successors and predecessors for BINARY_SUBSCR_STR_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 140 | 58.3% |
| LOAD_CONST | 100 | 41.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 120 | 50.0% |
| LOAD_CONST | 100 | 41.7% |
| PUSH_EXC_INFO | 20 | 8.3% |


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
| LOAD_FAST | 340 | 47.2% |
| LOAD_FAST_LOAD_FAST | 160 | 22.2% |
| CALL | 120 | 16.7% |
| PUSH_NULL | 40 | 5.6% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 5.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 640 | 88.9% |
| COPY_FREE_VARS | 60 | 8.3% |
| STORE_FAST | 20 | 2.8% |


</details>

### CALL_BOUND_METHOD_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_BOUND_METHOD_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 320,869 | 97.3% |
| CALL_BUILTIN_CLASS | 7,985 | 2.4% |
| LOAD_CONST | 360 | 0.1% |
| LOAD_FAST | 220 | 0.1% |
| PUSH_NULL | 120 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 321,369 | 97.5% |
| COPY_FREE_VARS | 8,005 | 2.4% |
| POP_TOP | 240 | 0.1% |


</details>

### CALL_BUILTIN_CLASS

<details>
<summary> Successors and predecessors for CALL_BUILTIN_CLASS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 330,234 | 85.6% |
| LOAD_ATTR_INSTANCE_VALUE | 53,568 | 13.9% |
| LOAD_CONST | 1,360 | 0.4% |
| CALL | 280 | 0.1% |
| LOAD_GLOBAL_BUILTIN | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| GET_ITER | 322,109 | 83.5% |
| CALL_BUILTIN_FAST_WITH_KEYWORDS | 53,408 | 13.8% |
| CALL_BOUND_METHOD_EXACT_ARGS | 7,985 | 2.1% |
| LIST_APPEND | 1,280 | 0.3% |
| STORE_FAST | 540 | 0.1% |


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
| CALL_BUILTIN_CLASS | 53,408 | 99.0% |
| LOAD_FAST | 360 | 0.7% |
| LOAD_CONST | 120 | 0.2% |
| CALL_STR_1 | 40 | 0.1% |
| CALL | 20 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RETURN_VALUE | 53,788 | 99.7% |
| STORE_FAST | 140 | 0.3% |
| BEFORE_WITH | 40 | 0.1% |


</details>

### CALL_BUILTIN_O

<details>
<summary> Successors and predecessors for CALL_BUILTIN_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 480 | 40.7% |
| LOAD_ATTR_INSTANCE_VALUE | 280 | 23.7% |
| CALL | 120 | 10.2% |
| BINARY_OP_MULTIPLY_FLOAT | 120 | 10.2% |
| LOAD_CONST | 80 | 6.8% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 500 | 42.4% |
| STORE_FAST | 340 | 28.8% |
| LOAD_CONST | 140 | 11.9% |
| BUILD_TUPLE | 80 | 6.8% |
| TO_BOOL_INT | 60 | 5.1% |


</details>

### CALL_ISINSTANCE

<details>
<summary> Successors and predecessors for CALL_ISINSTANCE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_BUILTIN | 19,130 | 52.3% |
| BUILD_TUPLE | 16,520 | 45.1% |
| CALL | 380 | 1.0% |
| LOAD_GLOBAL_MODULE | 360 | 1.0% |
| LOAD_ATTR_MODULE | 160 | 0.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 36,150 | 98.8% |
| TO_BOOL | 380 | 1.0% |
| RETURN_VALUE | 40 | 0.1% |
| LOAD_FAST | 20 | 0.1% |


</details>

### CALL_LEN

<details>
<summary> Successors and predecessors for CALL_LEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 1,606,636 | 54.1% |
| LOAD_FAST | 1,040,995 | 35.1% |
| LOAD_ATTR_WITH_HINT | 320,869 | 10.8% |
| CALL | 320 | 0.0% |
| BINARY_SUBSCR | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 697,161 | 23.5% |
| TO_BOOL_INT | 650,278 | 21.9% |
| LOAD_FAST | 641,349 | 21.6% |
| BINARY_OP_ADD_INT | 328,509 | 11.1% |
| COPY | 321,849 | 10.8% |


</details>

### CALL_LIST_APPEND

<details>
<summary> Successors and predecessors for CALL_LIST_APPEND </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 4,479,053 | 92.4% |
| BUILD_TUPLE | 366,677 | 7.6% |
| CALL | 120 | 0.0% |
| LOAD_ATTR_MODULE | 120 | 0.0% |
| LOAD_CONST | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 4,845,630 | 100.0% |
| JUMP_FORWARD | 140 | 0.0% |
| NOP | 80 | 0.0% |
| LOAD_CONST | 80 | 0.0% |
| LOAD_FAST | 80 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 366,737 | 51.9% |
| LOAD_ATTR_METHOD_NO_DICT | 329,549 | 46.6% |
| LOAD_FAST_LOAD_FAST | 8,945 | 1.3% |
| LOAD_GLOBAL_MODULE | 1,320 | 0.2% |
| RETURN_VALUE | 360 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 696,566 | 98.5% |
| RETURN_VALUE | 9,105 | 1.3% |
| LIST_APPEND | 1,200 | 0.2% |
| POP_TOP | 220 | 0.0% |
| LOAD_FAST | 60 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 321,829 | 99.5% |
| LOAD_FAST | 480 | 0.1% |
| LOAD_ATTR | 360 | 0.1% |
| LOAD_CONST | 280 | 0.1% |
| CALL | 220 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 322,009 | 99.6% |
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
| LOAD_ATTR_METHOD_NO_DICT | 1,065,589 | 76.3% |
| LOAD_ATTR | 329,229 | 23.6% |
| CALL | 840 | 0.1% |
| LOAD_FAST | 360 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,063,329 | 76.2% |
| TO_BOOL_BOOL | 329,349 | 23.6% |
| POP_TOP | 920 | 0.1% |
| RETURN_VALUE | 700 | 0.1% |
| LOAD_FAST | 460 | 0.0% |


</details>

### CALL_METHOD_DESCRIPTOR_O

<details>
<summary> Successors and predecessors for CALL_METHOD_DESCRIPTOR_O </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,378,455 | 66.9% |
| BINARY_SLICE | 358,332 | 17.4% |
| LOAD_FAST_CHECK | 320,498 | 15.6% |
| CALL | 840 | 0.0% |
| LOAD_CONST | 600 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_TOP | 1,729,847 | 84.0% |
| CALL_PY_EXACT_ARGS | 320,498 | 15.6% |
| RETURN_VALUE | 8,560 | 0.4% |
| LOAD_CONST | 280 | 0.0% |
| STORE_FAST | 80 | 0.0% |


</details>

### CALL_PY_EXACT_ARGS

<details>
<summary> Successors and predecessors for CALL_PY_EXACT_ARGS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 3,922,883 | 31.4% |
| LOAD_ATTR_METHOD_WITH_VALUES | 3,812,287 | 30.5% |
| LOAD_FAST | 2,421,070 | 19.4% |
| LOAD_ATTR_METHOD_NO_DICT | 1,026,491 | 8.2% |
| LOAD_CONST | 641,978 | 5.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 11,503,789 | 92.1% |
| RETURN_GENERATOR | 657,798 | 5.3% |
| MAKE_CELL | 320,600 | 2.6% |
| COPY_FREE_VARS | 10,185 | 0.1% |
| RESUME | 20 | 0.0% |


</details>

### CALL_PY_WITH_DEFAULTS

<details>
<summary> Successors and predecessors for CALL_PY_WITH_DEFAULTS </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 5,441,029 | 99.8% |
| LOAD_FAST | 8,885 | 0.2% |
| LOAD_ATTR_METHOD_NO_DICT | 360 | 0.0% |
| LOAD_ATTR_METHOD_WITH_VALUES | 360 | 0.0% |
| CALL | 320 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 5,451,194 | 100.0% |
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
| LOAD_FAST | 6,249 | 95.7% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 1.8% |
| LOAD_ATTR_SLOT | 120 | 1.8% |
| COMPARE_OP | 40 | 0.6% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 6,389 | 97.9% |
| RETURN_VALUE | 140 | 2.1% |


</details>

### COMPARE_OP_INT

<details>
<summary> Successors and predecessors for COMPARE_OP_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 1,949,156 | 41.8% |
| LOAD_CONST | 1,304,226 | 28.0% |
| LOAD_GLOBAL_MODULE | 321,869 | 6.9% |
| LOAD_FAST | 321,589 | 6.9% |
| BINARY_OP_MULTIPLY_INT | 320,589 | 6.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 4,340,381 | 93.1% |
| POP_JUMP_IF_TRUE | 321,709 | 6.9% |
| RETURN_VALUE | 60 | 0.0% |
| STORE_FAST | 40 | 0.0% |


</details>

### COMPARE_OP_STR

<details>
<summary> Successors and predecessors for COMPARE_OP_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_CONST | 780 | 76.5% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 11.8% |
| COMPARE_OP | 80 | 7.8% |
| LOAD_FAST | 40 | 3.9% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 880 | 86.3% |
| COPY | 60 | 5.9% |
| STORE_FAST | 60 | 5.9% |
| EXTENDED_ARG | 20 | 2.0% |


</details>

### FOR_ITER_LIST

<details>
<summary> Successors and predecessors for FOR_ITER_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 734,454 | 53.2% |
| GET_ITER | 644,618 | 46.7% |
| EXTENDED_ARG | 280 | 0.0% |
| FOR_ITER | 280 | 0.0% |
| SWAP | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| UNPACK_SEQUENCE_TWO_TUPLE | 733,854 | 53.2% |
| RETURN_CONST | 322,069 | 23.3% |
| LOAD_FAST | 321,949 | 23.3% |
| STORE_FAST | 1,300 | 0.1% |
| LOAD_DEREF | 140 | 0.0% |


</details>

### FOR_ITER_RANGE

<details>
<summary> Successors and predecessors for FOR_ITER_RANGE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 1,037,306 | 76.3% |
| GET_ITER | 322,029 | 23.7% |
| FOR_ITER | 60 | 0.0% |
| SWAP | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,037,386 | 76.3% |
| LOAD_CONST | 321,869 | 23.7% |
| LOAD_FAST | 100 | 0.0% |
| SWAP | 40 | 0.0% |
| LOAD_GLOBAL_MODULE | 40 | 0.0% |


</details>

### FOR_ITER_TUPLE

<details>
<summary> Successors and predecessors for FOR_ITER_TUPLE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD | 9,260 | 51.7% |
| GET_ITER | 8,060 | 45.0% |
| SWAP | 560 | 3.1% |
| FOR_ITER | 40 | 0.2% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 8,060 | 45.0% |
| NOP | 8,000 | 44.6% |
| STORE_FAST_LOAD_FAST | 1,200 | 6.7% |
| SWAP | 560 | 3.1% |
| LOAD_GLOBAL | 40 | 0.2% |


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
| LOAD_FAST | 24,568,699 | 99.9% |
| LOAD_FAST_LOAD_FAST | 9,505 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 9,045 | 0.0% |
| LOAD_ATTR | 4,880 | 0.0% |
| COPY | 840 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_NO_DICT | 8,162,944 | 33.2% |
| TO_BOOL_BOOL | 4,616,752 | 18.8% |
| CALL_LEN | 1,606,636 | 6.5% |
| LOAD_ATTR_METHOD_WITH_VALUES | 1,366,093 | 5.6% |
| LOAD_ATTR | 1,308,998 | 5.3% |


</details>

### LOAD_ATTR_METHOD_NO_DICT

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_NO_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 8,162,944 | 51.5% |
| LOAD_FAST_CHECK | 4,478,833 | 28.3% |
| LOAD_FAST | 1,854,476 | 11.7% |
| LOAD_ATTR_WITH_HINT | 658,538 | 4.2% |
| LOAD_ATTR | 376,922 | 2.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,363,525 | 78.0% |
| CALL_METHOD_DESCRIPTOR_NOARGS | 1,065,589 | 6.7% |
| CALL_PY_EXACT_ARGS | 1,026,491 | 6.5% |
| LOAD_FAST_LOAD_FAST | 743,019 | 4.7% |
| CALL_METHOD_DESCRIPTOR_FAST | 329,549 | 2.1% |


</details>

### LOAD_ATTR_METHOD_WITH_VALUES

<details>
<summary> Successors and predecessors for LOAD_ATTR_METHOD_WITH_VALUES </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_WITH_HINT | 6,115,659 | 48.4% |
| LOAD_FAST | 4,473,709 | 35.4% |
| LOAD_ATTR_INSTANCE_VALUE | 1,366,093 | 10.8% |
| LOAD_ATTR_SLOT | 677,304 | 5.4% |
| RETURN_VALUE | 9,025 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 7,209,181 | 57.0% |
| CALL_PY_EXACT_ARGS | 3,812,287 | 30.1% |
| LOAD_FAST_LOAD_FAST | 660,034 | 5.2% |
| LOAD_CONST | 641,347 | 5.1% |
| LOAD_GLOBAL_MODULE | 320,709 | 2.5% |


</details>

### LOAD_ATTR_MODULE

<details>
<summary> Successors and predecessors for LOAD_ATTR_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_GLOBAL_MODULE | 2,440,584 | 99.9% |
| LOAD_ATTR | 2,280 | 0.1% |
| LOAD_FAST | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| PUSH_NULL | 1,692,425 | 69.3% |
| BINARY_OP | 741,079 | 30.3% |
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
| LOAD_FAST | 321,409 | 99.9% |
| LOAD_ATTR | 220 | 0.1% |
| LOAD_DEREF | 120 | 0.0% |
| LOAD_FAST_LOAD_FAST | 40 | 0.0% |
| LOAD_ATTR_INSTANCE_VALUE | 40 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 321,249 | 99.8% |
| COPY_FREE_VARS | 580 | 0.2% |


</details>

### LOAD_ATTR_SLOT

<details>
<summary> Successors and predecessors for LOAD_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 6,900,130 | 99.8% |
| LOAD_FAST_LOAD_FAST | 7,980 | 0.1% |
| BINARY_SUBSCR_LIST_INT | 6,649 | 0.1% |
| LOAD_ATTR | 940 | 0.0% |
| LOAD_ATTR_MODULE | 820 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| TO_BOOL_BOOL | 1,819,862 | 26.3% |
| TO_BOOL_NONE | 1,303,218 | 18.8% |
| LOAD_ATTR | 1,018,046 | 14.7% |
| BUILD_LIST | 1,017,646 | 14.7% |
| LIST_EXTEND | 1,017,646 | 14.7% |


</details>

### LOAD_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for LOAD_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 12,683,072 | 81.2% |
| LOAD_FAST_LOAD_FAST | 1,949,276 | 12.5% |
| LOAD_DEREF | 961,320 | 6.2% |
| COPY | 16,040 | 0.1% |
| LOAD_ATTR | 1,839 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_METHOD_WITH_VALUES | 6,115,659 | 39.2% |
| TO_BOOL_BOOL | 2,614,585 | 16.7% |
| COMPARE_OP_INT | 1,949,156 | 12.5% |
| LOAD_GLOBAL_MODULE | 1,621,727 | 10.4% |
| LOAD_ATTR | 979,777 | 6.3% |


</details>

### LOAD_GLOBAL_BUILTIN

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_BUILTIN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST | 1,356,064 | 32.2% |
| POP_JUMP_IF_FALSE | 636,500 | 15.1% |
| LOAD_GLOBAL_BUILTIN | 460,525 | 10.9% |
| RESUME_CHECK | 414,007 | 9.8% |
| LOAD_FAST | 356,219 | 8.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 3,705,416 | 88.0% |
| LOAD_GLOBAL_BUILTIN | 460,525 | 10.9% |
| CALL_ISINSTANCE | 19,130 | 0.5% |
| BUILD_TUPLE | 16,660 | 0.4% |
| LOAD_DEREF | 4,200 | 0.1% |


</details>

### LOAD_GLOBAL_MODULE

<details>
<summary> Successors and predecessors for LOAD_GLOBAL_MODULE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,794,657 | 26.1% |
| LOAD_ATTR_WITH_HINT | 1,621,727 | 23.6% |
| RESUME_CHECK | 1,353,255 | 19.7% |
| LOAD_ATTR | 658,229 | 9.6% |
| POP_TOP | 375,922 | 5.5% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_MODULE | 2,440,584 | 35.5% |
| LOAD_ATTR | 2,284,856 | 33.3% |
| BINARY_OP | 1,055,863 | 15.4% |
| COMPARE_OP_INT | 321,869 | 4.7% |
| CALL_PY_EXACT_ARGS | 321,709 | 4.7% |


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
| CALL_PY_EXACT_ARGS | 11,503,789 | 51.7% |
| CALL_PY_WITH_DEFAULTS | 5,451,194 | 24.5% |
| CACHE | 2,020,838 | 9.1% |
| SEND_GEN | 978,967 | 4.4% |
| POP_TOP | 658,858 | 3.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 16,835,551 | 75.6% |
| LOAD_GLOBAL_MODULE | 1,353,255 | 6.1% |
| JUMP_BACKWARD_NO_INTERRUPT | 1,307,876 | 5.9% |
| NOP | 1,054,421 | 4.7% |
| LOAD_DEREF | 649,145 | 2.9% |


</details>

### SEND_GEN

<details>
<summary> Successors and predecessors for SEND_GEN </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| JUMP_BACKWARD_NO_INTERRUPT | 979,067 | 59.8% |
| LOAD_CONST | 658,238 | 40.2% |
| SEND | 460 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| RESUME_CHECK | 978,967 | 59.8% |
| POP_TOP | 658,398 | 40.2% |
| RESUME | 400 | 0.0% |


</details>

### STORE_ATTR_INSTANCE_VALUE

<details>
<summary> Successors and predecessors for STORE_ATTR_INSTANCE_VALUE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 1,629,787 | 99.4% |
| LOAD_FAST_LOAD_FAST | 4,220 | 0.3% |
| STORE_ATTR | 3,560 | 0.2% |
| SWAP | 840 | 0.1% |
| LOAD_DEREF | 360 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 661,569 | 40.4% |
| RETURN_CONST | 643,849 | 39.3% |
| NOP | 320,629 | 19.6% |
| LOAD_CONST | 6,200 | 0.4% |
| LOAD_FAST_LOAD_FAST | 2,160 | 0.1% |


</details>

### STORE_ATTR_SLOT

<details>
<summary> Successors and predecessors for STORE_ATTR_SLOT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 2,640,596 | 56.6% |
| LOAD_FAST | 2,023,517 | 43.4% |
| STORE_ATTR | 560 | 0.0% |
| STORE_ATTR_SLOT | 60 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST_LOAD_FAST | 1,979,902 | 42.4% |
| LOAD_CONST | 1,329,213 | 28.5% |
| LOAD_FAST | 669,979 | 14.4% |
| RETURN_CONST | 669,619 | 14.4% |
| NOP | 15,960 | 0.3% |


</details>

### STORE_ATTR_WITH_HINT

<details>
<summary> Successors and predecessors for STORE_ATTR_WITH_HINT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 353,120 | 51.1% |
| LOAD_DEREF | 320,360 | 46.4% |
| SWAP | 16,040 | 2.3% |
| LOAD_FAST_LOAD_FAST | 1,120 | 0.2% |
| STORE_ATTR | 440 | 0.1% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 337,320 | 48.8% |
| RETURN_CONST | 329,420 | 47.7% |
| NOP | 15,800 | 2.3% |
| JUMP_BACKWARD | 7,980 | 1.2% |
| LOAD_CONST | 420 | 0.1% |


</details>

### STORE_SUBSCR_DICT

<details>
<summary> Successors and predecessors for STORE_SUBSCR_DICT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR | 8,345 | 88.9% |
| LOAD_FAST | 480 | 5.1% |
| LOAD_CONST | 280 | 3.0% |
| STORE_SUBSCR | 160 | 1.7% |
| LOAD_ATTR_INSTANCE_VALUE | 120 | 1.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| LOAD_FAST | 8,685 | 92.5% |
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
| EXTENDED_ARG | 20 | 50.0% |
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
| LOAD_FAST | 10,570,743 | 51.1% |
| LOAD_ATTR_INSTANCE_VALUE | 4,616,752 | 22.3% |
| LOAD_ATTR_WITH_HINT | 2,614,585 | 12.6% |
| LOAD_ATTR_SLOT | 1,819,862 | 8.8% |
| RETURN_VALUE | 694,259 | 3.4% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 17,989,235 | 87.0% |
| POP_JUMP_IF_TRUE | 2,696,905 | 13.0% |
| UNARY_NOT | 340 | 0.0% |
| EXTENDED_ARG | 100 | 0.0% |


</details>

### TO_BOOL_INT

<details>
<summary> Successors and predecessors for TO_BOOL_INT </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| COPY | 1,055,903 | 33.1% |
| BINARY_OP | 733,694 | 23.0% |
| CALL_LEN | 650,278 | 20.4% |
| LOAD_FAST | 375,037 | 11.8% |
| LOAD_ATTR_INSTANCE_VALUE | 374,717 | 11.7% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,859,345 | 58.3% |
| POP_JUMP_IF_TRUE | 1,330,764 | 41.7% |
| UNARY_NOT | 80 | 0.0% |


</details>

### TO_BOOL_LIST

<details>
<summary> Successors and predecessors for TO_BOOL_LIST </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_INSTANCE_VALUE | 644,998 | 99.9% |
| LOAD_FAST | 320 | 0.0% |
| TO_BOOL | 180 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 645,258 | 100.0% |
| POP_JUMP_IF_TRUE | 220 | 0.0% |
| UNARY_NOT | 20 | 0.0% |


</details>

### TO_BOOL_NONE

<details>
<summary> Successors and predecessors for TO_BOOL_NONE </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| LOAD_ATTR_SLOT | 1,303,218 | 99.8% |
| LOAD_FAST | 1,500 | 0.1% |
| LOAD_ATTR | 600 | 0.0% |
| TO_BOOL | 240 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,305,498 | 100.0% |
| TO_BOOL_ALWAYS_TRUE | 40 | 0.0% |
| POP_JUMP_IF_TRUE | 20 | 0.0% |


</details>

### TO_BOOL_STR

<details>
<summary> Successors and predecessors for TO_BOOL_STR </summary>

|Predecessors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_LOAD_FAST | 1,200 | 65.2% |
| LOAD_FAST | 400 | 21.7% |
| COPY | 160 | 8.7% |
| TO_BOOL | 80 | 4.3% |

|Successors | Count | Percentage | 
|---|---:|---:|
| POP_JUMP_IF_FALSE | 1,560 | 84.8% |
| POP_JUMP_IF_TRUE | 280 | 15.2% |


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
| FOR_ITER_LIST | 733,854 | 66.1% |
| STORE_FAST | 374,862 | 33.8% |
| RETURN_VALUE | 480 | 0.0% |
| UNPACK_SEQUENCE | 320 | 0.0% |
| BINARY_SLICE | 200 | 0.0% |

|Successors | Count | Percentage | 
|---|---:|---:|
| STORE_FAST_STORE_FAST | 1,109,776 | 100.0% |
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
|     deferred | 2,222,947 | 62.3% |
|          hit | 1,339,776 | 37.6% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 480 | 15.8% |
| Failure | 2,560 | 84.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| and int | 1,760 | 68.8% |
| or | 600 | 23.4% |
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
|     deferred | 8,340 | 19.5% |
|          hit | 33,863 | 79.3% |
|         miss | 140 | 0.3% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 200 | 55.6% |
| Failure | 160 | 44.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| buffer int | 140 | 87.5% |
| out of range | 20 | 12.5% |


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 8,834,038 | 22.0% |
|          hit | 31,382,407 | 78.0% |
|         miss | 2,820 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 8,419 | 51.2% |
| Failure | 8,040 | 48.8% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| meth descr varargs | 1,960 | 24.4% |
| class no vectorcall | 1,340 | 16.7% |
| code complex parameters | 920 | 11.4% |
| cfunc noargs | 800 | 10.0% |
| meth descr method fastcall keywords | 760 | 9.5% |
| no dict | 640 | 8.0% |
| other | 380 | 4.7% |
| cfunc varargs keywords | 340 | 4.2% |
| class mutable | 300 | 3.7% |
| meth descr varargs keywords | 260 | 3.2% |
| operator wrapper | 140 | 1.7% |
| cfunc varargs | 100 | 1.2% |
| wrong number arguments | 40 | 0.5% |
| cmethod | 40 | 0.5% |
| init not simple | 20 | 0.2% |


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 985,823 | 17.4% |
|          hit | 4,669,559 | 82.5% |
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
|     deferred | 16,820 | 0.6% |
|          hit | 2,757,047 | 99.4% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 380 | 57.6% |
| Failure | 280 | 42.4% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| other | 160 | 57.1% |
| dict items | 80 | 28.6% |
| set | 40 | 14.3% |


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 16,836,785 | 17.7% |
|          hit | 78,383,808 | 82.3% |
|         miss | 3,640 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 15,738 | 46.8% |
| Failure | 17,920 | 53.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| has managed dict | 9,080 | 50.7% |
| metaclass attribute | 3,680 | 20.5% |
| not managed dict | 2,660 | 14.8% |
| method | 1,380 | 7.7% |
| shadowed | 720 | 4.0% |
| class method obj | 180 | 1.0% |
| non object slot | 80 | 0.4% |
| class attr descriptor | 60 | 0.3% |
| class attr simple | 40 | 0.2% |
| module attr not found | 20 | 0.1% |
| builtin class method | 20 | 0.1% |


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

|Kind | Count | Ratio | 
|---|---:|---:|
|     deferred | 7,060 | 0.1% |
|        deopt | 80 | 0.0% |
|          hit | 11,078,067 | 99.9% |
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
|     deferred | 658,438 | 28.7% |
|          hit | 1,637,765 | 71.3% |

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
|     deferred | 7,280 | 0.1% |
|          hit | 6,988,580 | 99.7% |
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
|     deferred | 10,760 | 52.7% |
|          hit | 9,425 | 46.2% |

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
|     deferred | 7,565,937 | 22.6% |
|          hit | 25,829,885 | 77.3% |
|         miss | 180 | 0.0% |

| | Count | Ratio | 
|---|---:|---:|
| Success | 3,940 | 44.8% |
| Failure | 4,860 | 55.2% |

|Failure kind | Count | Ratio | 
|---|---:|---:|
| bytes | 2,500 | 51.4% |
| sequence | 1,380 | 28.4% |
| mapping | 280 | 5.8% |
| bytearray | 260 | 5.3% |
| dict | 160 | 3.3% |
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
|          hit | 1,110,216 | 99.9% |

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
| Basic | 249,613,107 | 47.7% |
| Not specialized | 86,745,146 | 16.6% |
| Specialized hits | 187,157,048 | 35.7% |
| Specialized misses | 13,420 | 0.0% |

### Deferred by instruction

<details>
<summary> deferred by instruction </summary>

|Name | Count | Ratio | 
|---|---:|---:|
| LOAD_ATTR | 16,836,785 | 45.3% |
| CALL | 8,834,038 | 23.8% |
| TO_BOOL | 7,565,937 | 20.4% |
| BINARY_OP | 2,222,947 | 6.0% |
| COMPARE_OP | 985,823 | 2.7% |
| SEND | 658,438 | 1.8% |
| FOR_ITER | 16,820 | 0.0% |
| STORE_SUBSCR | 10,760 | 0.0% |
| BINARY_SUBSCR | 8,340 | 0.0% |
| STORE_ATTR | 7,280 | 0.0% |


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
| Calls to PyEval_EvalDefault | 2,345,258 | 10.2% |
| Calls to Python functions inlined | 20,581,404 | 89.8% |
| Calls via PyEval_EvalFrame (total) | 2,345,258 | 10.2% |
| Calls via PyEval_EvalFrame (vector) | 2,015,549 | 8.8% |
| Calls via PyEval_EvalFrame (generator) | 329,709 | 1.4% |
| Calls via PyEval_EvalFrame (legacy) | 40 | 0.0% |
| Calls via PyEval_EvalFrame (function vectorcall) | 2,015,409 | 8.8% |
| Calls via PyEval_EvalFrame (build class) | 100 | 0.0% |
| Calls via PyEval_EvalFrame (slot) | 380 | 0.0% |
| Calls via PyEval_EvalFrame (function ex) | 440 | 0.0% |
| Calls via PyEval_EvalFrame (api) | 1,920 | 0.0% |
| Calls via PyEval_EvalFrame (method) | 659,818 | 2.9% |
| Frame objects created | 643,418 | 2.8% |
| Frames pushed | 18,596,429 | 81.1% |


</details>

## Object stats

<details>
<summary> allocations, frees and dict materializatons </summary>

| | Count | Ratio | 
|---|---:|---:|
| Allocations from freelist | 14,685,661 | 41.2% |
| Frees to freelist | 14,693,666 |  |
| Allocations | 20,965,651 | 58.8% |
| Allocations to 512 bytes | 14,551,989 | 40.8% |
| Allocations to 4 kbytes | 323,031 | 0.9% |
| Allocations over 4 kbytes | 6,090,631 | 17.1% |
| Frees | 21,347,623 |  |
| New values | 1,560 |  |
| Interpreter increfs | 223,472,853 | 76.0% |
| Interpreter decrefs | 248,182,680 | 75.8% |
| Increfs | 70,549,993 | 24.0% |
| Decrefs | 79,309,533 | 24.2% |
| Materialize dict (on request) | 0 | 0.0% |
| Materialize dict (new key) | 160 | 10.3% |
| Materialize dict (too big) | 0 | 0.0% |
| Materialize dict (str subclass) | 0 | 0.0% |
| Dematerialize dict | 0 | 0.0% |
| Method cache hits | 20,424,622 |  |
| Method cache misses | 50,993 |  |
| Method cache collisions | 50,448 |  |
| Method cache dunder hits | 1,046,435 |  |
| Method cache dunder misses | 1,401 |  |


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>

|Generation | Collections | Objects collected | Object visits | 
|---:|---:|---:|---:|
| 0 | 20 | 1,980 | 139,880 |
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
