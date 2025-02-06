## Execution counts

<details>
<summary> Execution counts for Tier 1 instructions. </summary>


The "miss ratio" column shows the percentage of times the instruction
executed that it deoptimized. When this happens, the base unspecialized
instruction is not counted.

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">105,492</td>
<td align="right">674,179</td>
<td align="right">539.1%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">167,305</td>
<td align="right">568,342</td>
<td align="right">239.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">318,718</td>
<td align="right">733,016</td>
<td align="right">130.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">412,127</td>
<td align="right">945,282</td>
<td align="right">129.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">363,258</td>
<td align="right">764,400</td>
<td align="right">110.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">826,450</td>
<td align="right">1,227,487</td>
<td align="right">48.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">5,061</td>
<td align="right">2,611</td>
<td align="right">-48.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,167,929</td>
<td align="right">1,640,319</td>
<td align="right">40.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,757,542</td>
<td align="right">3,850,077</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">917,265</td>
<td align="right">1,206,146</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">2,528,686</td>
<td align="right">3,137,129</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">362,688</td>
<td align="right">448,704</td>
<td align="right">23.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">279,324</td>
<td align="right">341,792</td>
<td align="right">22.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,094,030</td>
<td align="right">1,334,190</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">792,215</td>
<td align="right">964,205</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">2,864,349</td>
<td align="right">3,397,504</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">374,703</td>
<td align="right">439,215</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">4,079,789</td>
<td align="right">4,761,189</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,208,417</td>
<td align="right">4,863,513</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,755,491</td>
<td align="right">2,004,536</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">4,153,133</td>
<td align="right">4,731,735</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,364,070</td>
<td align="right">2,690,250</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">8,323,180</td>
<td align="right">9,435,150</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">692,593</td>
<td align="right">760,794</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">5,424,391</td>
<td align="right">5,911,269</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">748,727</td>
<td align="right">811,195</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">8,767,765</td>
<td align="right">9,487,809</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">8,256,336</td>
<td align="right">8,918,071</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,872,188</td>
<td align="right">7,386,444</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">27,127,255</td>
<td align="right">29,131,910</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">21,035,411</td>
<td align="right">22,465,869</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">27,528,637</td>
<td align="right">29,376,927</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">15,776,393</td>
<td align="right">16,788,783</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">13,052,294</td>
<td align="right">13,881,777</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">91,552,090</td>
<td align="right">97,283,429</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">31,846,292</td>
<td align="right">33,668,957</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,272,184</td>
<td align="right">6,620,662</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">17,669,913</td>
<td align="right">18,645,079</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,783,412</td>
<td align="right">11,141,268</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">42,678,271</td>
<td align="right">44,963,904</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">6,581,916</td>
<td align="right">6,930,394</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">16,512,003</td>
<td align="right">17,379,427</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">18,678,366</td>
<td align="right">19,573,356</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">12,836,779</td>
<td align="right">13,336,559</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,825,052</td>
<td align="right">1,887,520</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">3,116,695</td>
<td align="right">3,220,428</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,167,156</td>
<td align="right">8,426,776</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,000,784</td>
<td align="right">1,032,018</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">27,397,995</td>
<td align="right">28,199,652</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,458,400</td>
<td align="right">2,520,868</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">10,024,346</td>
<td align="right">10,269,168</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,152,964</td>
<td align="right">5,277,900</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,015,616</td>
<td align="right">3,078,084</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">14,714,692</td>
<td align="right">14,992,082</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,897,649</td>
<td align="right">1,928,883</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">573,246</td>
<td align="right">582,131</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,187,315</td>
<td align="right">2,195,837</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,059,392</td>
<td align="right">13,059,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,329,046</td>
<td align="right">11,329,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">8,479,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,785,099</td>
<td align="right">5,785,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,798,261</td>
<td align="right">3,798,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,506,064</td>
<td align="right">3,506,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,457,099</td>
<td align="right">3,457,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,457,019</td>
<td align="right">3,457,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,847,283</td>
<td align="right">2,847,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,817,856</td>
<td align="right">2,817,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,646,270</td>
<td align="right">2,646,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,452,224</td>
<td align="right">2,452,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,452,224</td>
<td align="right">2,452,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,386,901</td>
<td align="right">2,386,901</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,377,152</td>
<td align="right">1,377,152</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,349,440</td>
<td align="right">1,349,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">918,398</td>
<td align="right">918,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">784,640</td>
<td align="right">784,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">542,077</td>
<td align="right">542,077</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">511,486</td>
<td align="right">511,486</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">503,222</td>
<td align="right">503,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">477,034</td>
<td align="right">477,034</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">459,456</td>
<td align="right">459,456</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">434,110</td>
<td align="right">434,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">283,898</td>
<td align="right">283,898</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">282,485</td>
<td align="right">282,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">265,022</td>
<td align="right">265,022</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">242,236</td>
<td align="right">242,236</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">230,783</td>
<td align="right">230,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">110,144</td>
<td align="right">110,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">108,370</td>
<td align="right">108,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">99,517</td>
<td align="right">99,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">97,992</td>
<td align="right">97,992</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">90,612</td>
<td align="right">90,612</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,607</td>
<td align="right">90,607</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">65,524</td>
<td align="right">65,524</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">56,310</td>
<td align="right">56,310</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">40,064</td>
<td align="right">40,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">27,136</td>
<td align="right">27,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">25,408</td>
<td align="right">25,408</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">24,640</td>
<td align="right">24,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">24,635</td>
<td align="right">24,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">21,501</td>
<td align="right">21,501</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,616</td>
<td align="right">18,616</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">15,420</td>
<td align="right">15,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">14,688</td>
<td align="right">14,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,864</td>
<td align="right">12,864</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">10,108</td>
<td align="right">10,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,788</td>
<td align="right">9,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">7,037</td>
<td align="right">7,037</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,909</td>
<td align="right">6,909</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,882</td>
<td align="right">2,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,431</td>
<td align="right">2,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,584</td>
<td align="right">1,584</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,471</td>
<td align="right">1,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,471</td>
<td align="right">1,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">1,026</td>
<td align="right">1,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">959</td>
<td align="right">959</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">368</td>
<td align="right">368</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">142</td>
<td align="right">142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133</td>
<td align="right">133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">127</td>
<td align="right">127</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">64</td>
<td align="right">64</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">50</td>
<td align="right">50</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

## Pair counts

<details>
<summary> Pair counts for top 100 opcode pairs </summary>


Pairs of specialized operations that deoptimize and are then followed by
the corresponding unspecialized instruction are not counted as pairs.

Not included in comparative output.


</details>

## Predecessor/Successor Pairs

<details>
<summary> Top 5 predecessors and successors of each Tier 1 opcode. </summary>


This does not include the unspecialized instructions that occur after a
specialized instruction deoptimizes.

Not included in comparative output.


</details>

## Specialization stats

<details>
<summary> Specialization stats by family </summary>

### BINARY_OP

<details>
<summary> specialization stats for BINARY_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">18,511</td>
<td align="right">11.8%</td>
<td align="right">18,511</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">137,649</td>
<td align="right">88.1%</td>
<td align="right">137,649</td>
<td align="right">88.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">35</td>
<td align="right">33.3%</td>
<td align="right">35</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">70</td>
<td align="right">66.7%</td>
<td align="right">70</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">add other</td>
<td align="right">49</td>
<td align="right">70.0%</td>
<td align="right">49</td>
<td align="right">70.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">30.0%</td>
<td align="right">21</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,904</td>
<td align="right">100.0%</td>
<td align="right">3,904</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SUBSCR

<details>
<summary> specialization stats for BINARY_SUBSCR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">39,822</td>
<td align="right">10.0%</td>
<td align="right">39,822</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">358,706</td>
<td align="right">89.9%</td>
<td align="right">358,706</td>
<td align="right">89.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">54</td>
<td align="right">22.3%</td>
<td align="right">54</td>
<td align="right">22.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">188</td>
<td align="right">77.7%</td>
<td align="right">188</td>
<td align="right">77.7%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">list slice</td>
<td align="right">94</td>
<td align="right">50.0%</td>
<td align="right">94</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">49</td>
<td align="right">26.1%</td>
<td align="right">49</td>
<td align="right">26.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">45</td>
<td align="right">23.9%</td>
<td align="right">45</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CALL

<details>
<summary> specialization stats for CALL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">429,152</td>
<td align="right">0.6%</td>
<td align="right">429,152</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,094,338</td>
<td align="right">99.4%</td>
<td align="right">75,094,338</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">437,035</td>
<td align="right">0.6%</td>
<td align="right">437,035</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">9,467</td>
<td align="right">100.0%</td>
<td align="right">9,467</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### CALL_KW

<details>
<summary> specialization stats for CALL_KW family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14</td>
<td align="right">29.2%</td>
<td align="right">14</td>
<td align="right">29.2%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">34</td>
<td align="right">100.0%</td>
<td align="right">34</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### COMPARE_OP

<details>
<summary> specialization stats for COMPARE_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">999,615</td>
<td align="right">75.1%</td>
<td align="right">1,030,849</td>
<td align="right">75.7%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">330,546</td>
<td align="right">24.8%</td>
<td align="right">330,546</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">34</td>
<td align="right">2.9%</td>
<td align="right">34</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,135</td>
<td align="right">97.1%</td>
<td align="right">1,135</td>
<td align="right">97.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">different types</td>
<td align="right">408</td>
<td align="right">35.9%</td>
<td align="right">408</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">400</td>
<td align="right">35.2%</td>
<td align="right">400</td>
<td align="right">35.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">181</td>
<td align="right">15.9%</td>
<td align="right">181</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">52</td>
<td align="right">4.6%</td>
<td align="right">52</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">50</td>
<td align="right">4.4%</td>
<td align="right">50</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">44</td>
<td align="right">3.9%</td>
<td align="right">44</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### CONTAINS_OP

<details>
<summary> specialization stats for CONTAINS_OP family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">374,467</td>
<td align="right">95.5%</td>
<td align="right">438,958</td>
<td align="right">96.1%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,284</td>
<td align="right">3.9%</td>
<td align="right">15,284</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,286</td>
<td align="right">0.6%</td>
<td align="right">2,286</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">227</td>
<td align="right">81.4%</td>
<td align="right">248</td>
<td align="right">82.7%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">18.6%</td>
<td align="right">52</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">tuple</td>
<td align="right">227</td>
<td align="right">100.0%</td>
<td align="right">248</td>
<td align="right">100.0%</td>
<td align="right">9.3%</td>
</tr>
</tbody>
</table>


</details>

### FOR_ITER

<details>
<summary> specialization stats for FOR_ITER family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,354,143</td>
<td align="right">48.0%</td>
<td align="right">7,094,621</td>
<td align="right">49.0%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,870,039</td>
<td align="right">51.9%</td>
<td align="right">7,384,189</td>
<td align="right">51.0%</td>
<td align="right">7.5%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">2,110</td>
<td align="right">98.2%</td>
<td align="right">2,216</td>
<td align="right">98.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39</td>
<td align="right">1.8%</td>
<td align="right">39</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">dict values</td>
<td align="right">148</td>
<td align="right">7.0%</td>
<td align="right">190</td>
<td align="right">8.6%</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,575</td>
<td align="right">74.6%</td>
<td align="right">1,639</td>
<td align="right">74.0%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">147</td>
<td align="right">7.0%</td>
<td align="right">147</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">96</td>
<td align="right">4.5%</td>
<td align="right">96</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">52</td>
<td align="right">2.5%</td>
<td align="right">52</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">46</td>
<td align="right">2.2%</td>
<td align="right">46</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">2.2%</td>
<td align="right">46</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_ATTR

<details>
<summary> specialization stats for LOAD_ATTR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,940,055</td>
<td align="right">8.1%</td>
<td align="right">4,446,593</td>
<td align="right">9.1%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">44,550,917</td>
<td align="right">91.7%</td>
<td align="right">44,095,189</td>
<td align="right">90.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">105,734</td>
<td align="right">0.2%</td>
<td align="right">105,734</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">308,630</td>
<td align="right">0.6%</td>
<td align="right">308,630</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">75,525</td>
<td align="right">98.2%</td>
<td align="right">85,070</td>
<td align="right">98.4%</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,367</td>
<td align="right">1.8%</td>
<td align="right">1,367</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">mutable class</td>
<td align="right">1,100</td>
<td align="right">80.5%</td>
<td align="right">1,100</td>
<td align="right">80.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">225</td>
<td align="right">16.5%</td>
<td align="right">225</td>
<td align="right">16.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">21</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### LOAD_GLOBAL

<details>
<summary> specialization stats for LOAD_GLOBAL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">59,846,680</td>
<td align="right">100.0%</td>
<td align="right">62,656,163</td>
<td align="right">100.0%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">303</td>
<td align="right">0.0%</td>
<td align="right">303</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,692</td>
<td align="right">0.0%</td>
<td align="right">1,692</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">767</td>
<td align="right">100.0%</td>
<td align="right">767</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### SEND

<details>
<summary> specialization stats for SEND family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,068,158</td>
<td align="right">100.0%</td>
<td align="right">8,068,158</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">2</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### STORE_ATTR

<details>
<summary> specialization stats for STORE_ATTR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">44</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">242,854</td>
<td align="right">41.4%</td>
<td align="right">242,854</td>
<td align="right">41.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">342,677</td>
<td align="right">58.5%</td>
<td align="right">342,677</td>
<td align="right">58.5%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">6,763</td>
<td align="right">100.0%</td>
<td align="right">6,763</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### STORE_SUBSCR

<details>
<summary> specialization stats for STORE_SUBSCR family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">230,783</td>
<td align="right">100.0%</td>
<td align="right">230,783</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">1</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### TO_BOOL

<details>
<summary> specialization stats for TO_BOOL family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">362,688</td>
<td align="right">0.8%</td>
<td align="right">763,725</td>
<td align="right">1.7%</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,528,703</td>
<td align="right">5.7%</td>
<td align="right">2,749,449</td>
<td align="right">6.1%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,545,834</td>
<td align="right">93.5%</td>
<td align="right">41,636,775</td>
<td align="right">92.2%</td>
<td align="right">0.2%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Failure</td>
<td align="right">159</td>
<td align="right">0.3%</td>
<td align="right">264</td>
<td align="right">0.5%</td>
<td align="right">66.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">48,110</td>
<td align="right">99.7%</td>
<td align="right">52,275</td>
<td align="right">99.5%</td>
<td align="right">8.7%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">14</td>
<td align="right">8.8%</td>
<td align="right">119</td>
<td align="right">45.1%</td>
<td align="right">750.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">145</td>
<td align="right">91.2%</td>
<td align="right">145</td>
<td align="right">54.9%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### UNPACK_SEQUENCE

<details>
<summary> specialization stats for UNPACK_SEQUENCE family </summary>

<table>
<thead>
<tr>
<th align="left">Kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">90,516</td>
<td align="right">0.7%</td>
<td align="right">90,516</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,040,940</td>
<td align="right">99.3%</td>
<td align="right">13,040,940</td>
<td align="right">99.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Success</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Success</td>
<td align="right">40</td>
<td align="right">44.0%</td>
<td align="right">40</td>
<td align="right">44.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">51</td>
<td align="right">56.0%</td>
<td align="right">51</td>
<td align="right">56.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left">Failure kind</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">51</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>


</details>

## Specialization effectiveness

<details>
<summary> specialization effectiveness </summary>


All entries are execution counts. Should add up to the total number of
Tier 1 instructions executed.

<table>
<thead>
<tr>
<th align="left">Instructions</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,875,526</td>
<td align="right">1.5%</td>
<td align="right">9,886,670</td>
<td align="right">1.6%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">7,252,788</td>
<td align="right">1.2%</td>
<td align="right">7,981,843</td>
<td align="right">1.3%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">252,591,381</td>
<td align="right">42.7%</td>
<td align="right">268,450,361</td>
<td align="right">42.9%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">322,860,008</td>
<td align="right">54.6%</td>
<td align="right">340,050,682</td>
<td align="right">54.3%</td>
<td align="right">5.3%</td>
</tr>
</tbody>
</table>

### Deferred by instruction

<details>
<summary> Breakdown of deferred (not specialized) instruction counts by family </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">362,688</td>
<td align="right">3.9%</td>
<td align="right">763,725</td>
<td align="right">7.4%</td>
<td align="right">110.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">374,467</td>
<td align="right">4.0%</td>
<td align="right">438,958</td>
<td align="right">4.3%</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">6,870,039</td>
<td align="right">73.9%</td>
<td align="right">7,384,189</td>
<td align="right">71.7%</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">999,615</td>
<td align="right">10.8%</td>
<td align="right">1,030,849</td>
<td align="right">10.0%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">429,152</td>
<td align="right">4.6%</td>
<td align="right">429,152</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">105,734</td>
<td align="right">1.1%</td>
<td align="right">105,734</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,516</td>
<td align="right">1.0%</td>
<td align="right">90,516</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">39,822</td>
<td align="right">0.4%</td>
<td align="right">39,822</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">18,511</td>
<td align="right">0.2%</td>
<td align="right">18,511</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Misses by instruction

<details>
<summary> Breakdown of misses (specialized deopts) instruction counts by family </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">617,816</td>
<td align="right">8.5%</td>
<td align="right">1,062,465</td>
<td align="right">13.3%</td>
<td align="right">72.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">1,377,834</td>
<td align="right">19.0%</td>
<td align="right">1,595,158</td>
<td align="right">20.0%</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,900,620</td>
<td align="right">40.0%</td>
<td align="right">2,962,509</td>
<td align="right">37.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">865,267</td>
<td align="right">11.9%</td>
<td align="right">868,689</td>
<td align="right">10.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">398,733</td>
<td align="right">5.5%</td>
<td align="right">398,733</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">342,677</td>
<td align="right">4.7%</td>
<td align="right">342,677</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">284,172</td>
<td align="right">3.9%</td>
<td align="right">284,172</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">252,756</td>
<td align="right">3.5%</td>
<td align="right">252,756</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">184,279</td>
<td align="right">2.5%</td>
<td align="right">184,279</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.3%</td>
<td align="right">22,886</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>


</details>

## Call stats

<details>
<summary> Inlined calls and frame stats </summary>


This shows what fraction of calls to Python functions are inlined (i.e.
not having a call at the C level) and for those that are not, where the
call comes from.  The various categories overlap.

Also includes the count of frame objects created.

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,284,842</td>
<td align="right">78.1%</td>
<td align="right">40,284,842</td>
<td align="right">78.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,623,378</td>
<td align="right">9.0%</td>
<td align="right">4,623,378</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">6,705,732</td>
<td align="right">13.0%</td>
<td align="right">6,705,732</td>
<td align="right">13.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">4,623,378</td>
<td align="right">9.0%</td>
<td align="right">4,623,378</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">1,587,200</td>
<td align="right">3.1%</td>
<td align="right">1,587,200</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,664</td>
<td align="right">0.0%</td>
<td align="right">25,664</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
<td align="right">3,019,281</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">192</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">33,170,303</td>
<td align="right">64.3%</td>
<td align="right">33,170,303</td>
<td align="right">64.3%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

## Object stats

<details>
<summary> Allocations, frees and dict materializatons </summary>


Below, "allocations" means "allocations that are not from a freelist".
Total allocations = "Allocations from freelist" + "Allocations".

"Inline values" is the number of values arrays inlined into objects.

The cache hit/miss numbers are for the MRO cache, split into dunder and
other names.

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">169</td>
<td align="right">0.0%</td>
<td align="right">317</td>
<td align="right">0.0%</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">3,170</td>
<td align="right"></td>
<td align="right">2,078</td>
<td align="right"></td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">4,374,481</td>
<td align="right"></td>
<td align="right">4,832,383</td>
<td align="right"></td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">279,087,515</td>
<td align="right">39.0%</td>
<td align="right">252,839,718</td>
<td align="right">35.9%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">290,382,028</td>
<td align="right">36.4%</td>
<td align="right">267,803,424</td>
<td align="right">34.1%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">246,956,675</td>
<td align="right">34.5%</td>
<td align="right">260,322,871</td>
<td align="right">37.0%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">69,660,732</td>
<td align="right">9.7%</td>
<td align="right">72,006,861</td>
<td align="right">10.2%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">312,480,593</td>
<td align="right">39.2%</td>
<td align="right">322,184,591</td>
<td align="right">41.1%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">476,309</td>
<td align="right"></td>
<td align="right">468,666</td>
<td align="right"></td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">473,767</td>
<td align="right"></td>
<td align="right">467,192</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">65,185,840</td>
<td align="right">8.2%</td>
<td align="right">66,020,820</td>
<td align="right">8.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">120,192,027</td>
<td align="right">16.8%</td>
<td align="right">118,655,150</td>
<td align="right">16.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">129,685,006</td>
<td align="right">16.3%</td>
<td align="right">128,249,928</td>
<td align="right">16.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">32,133</td>
<td align="right">0.0%</td>
<td align="right">32,410</td>
<td align="right">0.0%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">46,906,257</td>
<td align="right"></td>
<td align="right">46,963,610</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,160,489</td>
<td align="right"></td>
<td align="right">38,166,143</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,163,198</td>
<td align="right">45.7%</td>
<td align="right">38,168,852</td>
<td align="right">45.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">45,724,641</td>
<td align="right"></td>
<td align="right">45,726,138</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,401,331</td>
<td align="right">54.3%</td>
<td align="right">45,401,820</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,369,029</td>
<td align="right">54.3%</td>
<td align="right">45,369,093</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">16,704</td>
<td align="right"></td>
<td align="right">16,704</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">Materialize dict (str subclass)</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

## GC stats

<details>
<summary> GC collections and effectiveness </summary>


Collected/visits gives some measure of efficiency.

<table>
<thead>
<tr>
<th align="right">Generation</th>
<th align="right">Base Collections</th>
<th align="right">Base Objects collected</th>
<th align="right">Base Object visits</th>
<th align="right">Base Reachable from roots</th>
<th align="right">Base Not reachable from roots</th>
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
<th align="right">Head Reachable from roots</th>
<th align="right">Head Not reachable from roots</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">1</td>
<td align="right">21</td>
<td align="right">31,311</td>
<td align="right">273,286</td>
<td align="right">4,537</td>
<td align="right">36,750</td>
<td align="right">21</td>
<td align="right">31,555</td>
<td align="right">273,897</td>
<td align="right">4,042</td>
<td align="right">36,742</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
</tbody>
</table>


</details>

## Optimization (Tier 2) stats

<details>
<summary> statistics about the Tier 2 optimizer </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">43</td>
<td align="right">1.3%</td>
<td align="right">106</td>
<td align="right">3.5%</td>
<td align="right">146.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">87</td>
<td align="right">2.7%</td>
<td align="right">149</td>
<td align="right">4.9%</td>
<td align="right">71.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">32,759,200</td>
<td align="right"></td>
<td align="right">20,413,416</td>
<td align="right"></td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">861</td>
<td align="right">26.3%</td>
<td align="right">1,177</td>
<td align="right">38.4%</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">2,414</td>
<td align="right">73.7%</td>
<td align="right">1,890</td>
<td align="right">61.6%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,611</td>
<td align="right">79.7%</td>
<td align="right">2,131</td>
<td align="right">69.5%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">570,727,575</td>
<td align="right">1,742.2%</td>
<td align="right">475,104,643</td>
<td align="right">2,327.4%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,275</td>
<td align="right"></td>
<td align="right">3,067</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">105</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">861</td>
<td align="right"></td>
<td align="right">1,177</td>
<td align="right"></td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">861</td>
<td align="right">100.0%</td>
<td align="right">1,177</td>
<td align="right">100.0%</td>
<td align="right">36.7%</td>
</tr>
<tr>
<td align="left">
Optimizer no memory
<details>
<summary>ⓘ</summary>

The number of optimizations that failed due to no memory.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Remove globals builtins changed
<details>
<summary>ⓘ</summary>

The builtins changed during optimization
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>

### JIT memory stats

<details>
<summary> JIT memory stats </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Size (bytes)</th>
<th align="right">Base Ratio</th>
<th align="right">Head Size (bytes)</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">10,985,472</td>
<td align="right">71.2%</td>
<td align="right">23,334,912</td>
<td align="right">95.8%</td>
<td align="right">112.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">11,591,671</td>
<td align="right">75.1%</td>
<td align="right">18,441,047</td>
<td align="right">75.7%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">15,429,632</td>
<td align="right"></td>
<td align="right">24,363,008</td>
<td align="right"></td>
<td align="right">57.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,954,112</td>
<td align="right">12.7%</td>
<td align="right">3,060,264</td>
<td align="right">12.6%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,883,849</td>
<td align="right">12.2%</td>
<td align="right">2,861,697</td>
<td align="right">11.7%</td>
<td align="right">51.9%</td>
</tr>
<tr>
<td align="left">
Trampoline size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the trampolines of the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

### JIT trace total memory histogram

<details>
<summary> JIT trace total memory histogram </summary>

<table>
<thead>
<tr>
<th align="left">Size (bytes)</th>
<th align="left">Base Count</th>
<th align="right">Base Ratio</th>
<th align="left">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4,096</td>
<td align="left">176</td>
<td align="right">20.4%</td>
<td align="left">240</td>
<td align="right">17.8%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">277</td>
<td align="right">32.2%</td>
<td align="left">383</td>
<td align="right">28.4%</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">153</td>
<td align="right">17.8%</td>
<td align="left">302</td>
<td align="right">22.4%</td>
<td align="right">97.4%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">108</td>
<td align="right">12.5%</td>
<td align="left">194</td>
<td align="right">14.4%</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">105</td>
<td align="right">12.2%</td>
<td align="left">189</td>
<td align="right">14.0%</td>
<td align="right">80.0%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">42</td>
<td align="right">4.9%</td>
<td align="left">42</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace length histogram

<details>
<summary> trace length histogram </summary>

<table>
<thead>
<tr>
<th align="left">Range</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 8</td>
<td align="right">87</td>
<td align="right">10.1%</td>
<td align="right">88</td>
<td align="right">7.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">89</td>
<td align="right">10.3%</td>
<td align="right">152</td>
<td align="right">12.9%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">212</td>
<td align="right">24.6%</td>
<td align="right">315</td>
<td align="right">26.8%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">216</td>
<td align="right">25.1%</td>
<td align="right">281</td>
<td align="right">23.9%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">88</td>
<td align="right">10.2%</td>
<td align="right">130</td>
<td align="right">11.0%</td>
<td align="right">47.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">43</td>
<td align="right">5.0%</td>
<td align="right">85</td>
<td align="right">7.2%</td>
<td align="right">97.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">126</td>
<td align="right">14.6%</td>
<td align="right">126</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Optimized trace length histogram

<details>
<summary> optimized trace length histogram </summary>

<table>
<thead>
<tr>
<th align="left">Range</th>
<th align="right">Base Count</th>
<th align="right">Base Ratio</th>
<th align="right">Head Count</th>
<th align="right">Head Ratio</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><= 4</td>
<td align="right">43</td>
<td align="right">5.0%</td>
<td align="right">22</td>
<td align="right">1.9%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">132</td>
<td align="right">15.3%</td>
<td align="right">217</td>
<td align="right">18.4%</td>
<td align="right">64.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">23</td>
<td align="right">2.7%</td>
<td align="right">65</td>
<td align="right">5.5%</td>
<td align="right">182.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">255</td>
<td align="right">29.6%</td>
<td align="right">317</td>
<td align="right">26.9%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">153</td>
<td align="right">17.8%</td>
<td align="right">238</td>
<td align="right">20.2%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">108</td>
<td align="right">12.5%</td>
<td align="right">171</td>
<td align="right">14.5%</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">105</td>
<td align="right">12.2%</td>
<td align="right">105</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">42</td>
<td align="right">4.9%</td>
<td align="right">42</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>


</details>

### Uop execution stats

<details>
<summary> uop execution stats </summary>

<table>
<thead>
<tr>
<th align="left">Name</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">_DEOPT</td>
<td align="right">44</td>
<td align="right">800</td>
<td align="right">1,718.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,208</td>
<td align="right">735</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">353,534</td>
<td align="right">55,768</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">348,074</td>
<td align="right">55,065</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">498,623</td>
<td align="right">84,325</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">498,623</td>
<td align="right">84,325</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">12,285</td>
<td align="right">3,400</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">116,550</td>
<td align="right">52,059</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">140,077</td>
<td align="right">63,182</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">232,764</td>
<td align="right">107,828</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">116,382</td>
<td align="right">53,914</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">116,382</td>
<td align="right">53,914</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">58,191</td>
<td align="right">26,957</td>
<td align="right">-53.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">412,482</td>
<td align="right">193,844</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">412,482</td>
<td align="right">193,844</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">412,482</td>
<td align="right">193,844</td>
<td align="right">-53.0%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">118,944</td>
<td align="right">56,476</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">121,737</td>
<td align="right">59,269</td>
<td align="right">-51.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">245,616</td>
<td align="right">120,680</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">245,616</td>
<td align="right">120,680</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">124,089</td>
<td align="right">61,621</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">124,089</td>
<td align="right">61,621</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">24,676,334</td>
<td align="right">13,034,939</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">32,759,200</td>
<td align="right">20,413,416</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">576,303</td>
<td align="right">374,644</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,572,637</td>
<td align="right">1,828,253</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">2,428,325</td>
<td align="right">1,755,294</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">2,428,325</td>
<td align="right">1,755,294</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,428,325</td>
<td align="right">1,755,294</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,022,451</td>
<td align="right">745,061</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">997,881</td>
<td align="right">738,261</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">11,461,253</td>
<td align="right">8,488,592</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,857,230</td>
<td align="right">1,381,385</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,852,022</td>
<td align="right">1,380,650</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,137,064</td>
<td align="right">1,598,751</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">3,621,752</td>
<td align="right">2,793,445</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">5,549,774</td>
<td align="right">4,333,000</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">2,759,251</td>
<td align="right">2,180,649</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">8,839,788</td>
<td align="right">6,998,993</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">2,742,572</td>
<td align="right">2,173,885</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">8,097,246</td>
<td align="right">6,613,084</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">8,432,294</td>
<td align="right">6,947,514</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,020,113</td>
<td align="right">4,141,571</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">955,765</td>
<td align="right">788,865</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">3,025,237</td>
<td align="right">2,525,457</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,973,049</td>
<td align="right">2,486,171</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,959,140</td>
<td align="right">2,486,750</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">7,563,691</td>
<td align="right">6,376,987</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">2,151,737</td>
<td align="right">1,815,852</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">16,563,515</td>
<td align="right">14,024,491</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">9,419,761</td>
<td align="right">7,989,303</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">11,712,897</td>
<td align="right">9,950,448</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">15,565,779</td>
<td align="right">13,273,432</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">9,226,447</td>
<td align="right">7,869,883</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">14,916,797</td>
<td align="right">12,800,877</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">40,856,007</td>
<td align="right">35,071,648</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">2,835,639</td>
<td align="right">2,434,602</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">6,347,508</td>
<td align="right">5,459,036</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">5,772,308</td>
<td align="right">4,970,651</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">2,955,627</td>
<td align="right">2,554,590</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,256,998</td>
<td align="right">1,952,347</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">16,515,116</td>
<td align="right">14,325,191</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">17,007,831</td>
<td align="right">14,764,769</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,203,847</td>
<td align="right">1,927,980</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">2,209,456</td>
<td align="right">1,933,589</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">61,370,835</td>
<td align="right">53,746,823</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,196,791</td>
<td align="right">1,925,397</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">2,204,248</td>
<td align="right">1,932,854</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">8,034,326</td>
<td align="right">7,100,869</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">4,146,405</td>
<td align="right">3,666,085</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,103,154</td>
<td align="right">1,862,994</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">3,301,155</td>
<td align="right">2,925,253</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,201,245</td>
<td align="right">1,952,200</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">12,649,335</td>
<td align="right">11,231,569</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,147,905</td>
<td align="right">1,907,745</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">33,714,965</td>
<td align="right">29,946,421</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,143,991</td>
<td align="right">2,795,513</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">2,279,206</td>
<td align="right">2,034,384</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">4,899,585</td>
<td align="right">4,381,440</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">5,203,809</td>
<td align="right">4,670,654</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">310,507</td>
<td align="right">279,273</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">4,611,427</td>
<td align="right">4,159,617</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">2,900,517</td>
<td align="right">2,632,511</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">16,415,771</td>
<td align="right">14,954,487</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,899,544</td>
<td align="right">2,641,553</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">8,082,822</td>
<td align="right">7,377,677</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">20,117,711</td>
<td align="right">18,675,420</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">4,895,759</td>
<td align="right">4,569,579</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">4,895,759</td>
<td align="right">4,569,579</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">2,879,013</td>
<td align="right">2,707,023</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">9,550,844</td>
<td align="right">9,036,694</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,009,036</td>
<td align="right">2,954,490</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,692,983</td>
<td align="right">3,647,133</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,760,821</td>
<td align="right">2,760,821</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">757,645</td>
<td align="right">757,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">252,316</td>
<td align="right">252,316</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">118,701</td>
<td align="right">118,701</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">2,772</td>
<td align="right">2,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,562</td>
<td align="right">2,562</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### Pair counts

<details>
<summary> Pair counts for top 100 Non-JIT uop pairs </summary>


Pairs of specialized operations that deoptimize and are then followed by
the corresponding unspecialized instruction are not counted as pairs.

Not included in comparative output.


</details>

### Unsupported opcodes

<details>
<summary> unsupported opcodes </summary>


</details>

### Optimizer errored out with opcode

<details>
<summary> Optimization stopped after encountering this opcode </summary>


</details>


</details>

## Rare events

<details>
<summary> Counts of rare/unlikely events </summary>

<table>
<thead>
<tr>
<th align="left">Event</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
set eval frame func
<details>
<summary>ⓘ</summary>

Setting the PEP 523 frame eval function `_PyInterpreterState_SetFrameEvalFunc()`
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
builtin dict
<details>
<summary>ⓘ</summary>

Modifying the builtins, `__builtins__.__dict__[var] = ...`
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
func modification
<details>
<summary>ⓘ</summary>

Modifying a function, e.g. `func.__defaults__ = ...`, etc.
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right"></td>
</tr>
</tbody>
</table>


</details>

## Meta stats

<details>
<summary> Meta statistics </summary>

<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Number of data files</td>
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
