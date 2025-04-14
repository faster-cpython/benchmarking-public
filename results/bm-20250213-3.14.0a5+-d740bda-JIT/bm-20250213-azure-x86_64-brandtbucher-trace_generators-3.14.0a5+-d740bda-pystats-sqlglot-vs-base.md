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
<td align="left">NOT_TAKEN</td>
<td align="right">126</td>
<td align="right">21</td>
<td align="right">-83.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">3,671,228</td>
<td align="right">1,220,369</td>
<td align="right">-66.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,615,936</td>
<td align="right">2,018,097</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,789,564</td>
<td align="right">9,235,796</td>
<td align="right">36.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">7,461,832</td>
<td align="right">5,149,738</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">8,068,158</td>
<td align="right">6,554,142</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">210,778</td>
<td align="right">242,236</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,784,946</td>
<td align="right">3,107,192</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">43,599,446</td>
<td align="right">40,155,060</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,641,402</td>
<td align="right">2,848,777</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">214,550</td>
<td align="right">230,783</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">427,998</td>
<td align="right">459,456</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,404,637</td>
<td align="right">2,510,267</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,329,046</td>
<td align="right">11,780,651</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,482,986</td>
<td align="right">9,796,618</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">428,862</td>
<td align="right">441,966</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,541,558</td>
<td align="right">18,048,204</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,957,219</td>
<td align="right">7,139,268</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,385,652</td>
<td align="right">7,567,701</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">751,393</td>
<td align="right">764,854</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">8,025,166</td>
<td align="right">8,167,231</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">8,288,717</td>
<td align="right">8,421,822</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,727,627</td>
<td align="right">9,883,342</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">33,906,968</td>
<td align="right">34,415,987</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,829,360</td>
<td align="right">1,856,114</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">25,381,615</td>
<td align="right">25,717,111</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,043,261</td>
<td align="right">12,185,326</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,495,465</td>
<td align="right">17,690,786</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">35,911,738</td>
<td align="right">36,288,310</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">49,478,606</td>
<td align="right">49,933,802</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,664,745</td>
<td align="right">28,898,685</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">514,048</td>
<td align="right">510,163</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">113,790,371</td>
<td align="right">114,549,248</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">30,588,329</td>
<td align="right">30,778,778</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,129,648</td>
<td align="right">2,142,752</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,630,463</td>
<td align="right">3,651,967</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">859,544</td>
<td align="right">863,786</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">14,404,543</td>
<td align="right">14,473,675</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">434,110</td>
<td align="right">432,655</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">10,873,337</td>
<td align="right">10,909,310</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,002,944</td>
<td align="right">2,995,132</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,577,344</td>
<td align="right">2,573,459</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,849,993</td>
<td align="right">6,859,191</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,134,560</td>
<td align="right">3,130,675</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,658,813</td>
<td align="right">16,678,280</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">12,861,028</td>
<td align="right">12,870,226</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,161,383</td>
<td align="right">9,164,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,708,919</td>
<td align="right">15,711,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,251,846</td>
<td align="right">23,251,846</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,059,392</td>
<td align="right">13,059,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,545,920</td>
<td align="right">8,545,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">8,479,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,325,639</td>
<td align="right">7,325,639</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,385,767</td>
<td align="right">5,385,767</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,385,728</td>
<td align="right">5,385,728</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,114,784</td>
<td align="right">4,114,784</td>
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
<td align="right">3,624,765</td>
<td align="right">3,624,765</td>
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
<td align="left">TO_BOOL</td>
<td align="right">3,319,626</td>
<td align="right">3,319,626</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,848,064</td>
<td align="right">2,848,064</td>
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
<td align="left">JUMP_FORWARD</td>
<td align="right">1,955,840</td>
<td align="right">1,955,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,941,434</td>
<td align="right">1,941,434</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,058,975</td>
<td align="right">1,058,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">918,398</td>
<td align="right">918,398</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">917,265</td>
<td align="right">917,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">784,640</td>
<td align="right">784,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">721,280</td>
<td align="right">721,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">573,246</td>
<td align="right">573,246</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">542,077</td>
<td align="right">542,077</td>
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
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">395,706</td>
<td align="right">395,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">318,718</td>
<td align="right">318,718</td>
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
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
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
<td align="left">BINARY_OP</td>
<td align="right">58,680</td>
<td align="right">58,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">56,310</td>
<td align="right">56,310</td>
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
<td align="left">BINARY_OP_SUBSCR_DICT</td>
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
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
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
<td align="right">58,333</td>
<td align="right">10.5%</td>
<td align="right">58,333</td>
<td align="right">10.5%</td>
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
<td align="right">496,355</td>
<td align="right">89.4%</td>
<td align="right">496,355</td>
<td align="right">89.4%</td>
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
<td align="right">89</td>
<td align="right">25.6%</td>
<td align="right">89</td>
<td align="right">25.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">258</td>
<td align="right">74.4%</td>
<td align="right">258</td>
<td align="right">74.4%</td>
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
<td align="left">subscr list slice</td>
<td align="right">94</td>
<td align="right">36.4%</td>
<td align="right">94</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">49</td>
<td align="right">19.0%</td>
<td align="right">49</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">49</td>
<td align="right">19.0%</td>
<td align="right">49</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">45</td>
<td align="right">17.4%</td>
<td align="right">45</td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">8.1%</td>
<td align="right">21</td>
<td align="right">8.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">435,187</td>
<td align="right">0.6%</td>
<td align="right">436,783</td>
<td align="right">0.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">427,346</td>
<td align="right">0.6%</td>
<td align="right">428,900</td>
<td align="right">0.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">75,096,144</td>
<td align="right">99.4%</td>
<td align="right">75,094,590</td>
<td align="right">99.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">9,425</td>
<td align="right">100.0%</td>
<td align="right">9,467</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
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
<td align="right">1,057,806</td>
<td align="right">76.1%</td>
<td align="right">1,057,806</td>
<td align="right">76.1%</td>
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
<td align="right">330,546</td>
<td align="right">23.8%</td>
<td align="right">330,546</td>
<td align="right">23.8%</td>
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
<td align="right">428,626</td>
<td align="right">96.0%</td>
<td align="right">441,730</td>
<td align="right">96.1%</td>
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
<td align="right">15,284</td>
<td align="right">3.4%</td>
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
<td align="right">0.5%</td>
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
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">18.6%</td>
<td align="right">52</td>
<td align="right">18.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">227</td>
<td align="right">81.4%</td>
<td align="right">227</td>
<td align="right">81.4%</td>
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
<td align="right">227</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,480,242</td>
<td align="right">58.3%</td>
<td align="right">9,793,810</td>
<td align="right">57.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,775,019</td>
<td align="right">41.7%</td>
<td align="right">6,645,660</td>
<td align="right">39.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">460,288</td>
<td align="right">2.7%</td>
<td align="right"></td>
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
<td align="right">39</td>
<td align="right">1.4%</td>
<td align="right">8,722</td>
<td align="right">75.9%</td>
<td align="right">22,264.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,705</td>
<td align="right">98.6%</td>
<td align="right">2,769</td>
<td align="right">24.1%</td>
<td align="right">2.4%</td>
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
<td align="left">itertools</td>
<td align="right">84</td>
<td align="right">3.1%</td>
<td align="right">105</td>
<td align="right">3.8%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,084</td>
<td align="right">77.0%</td>
<td align="right">2,127</td>
<td align="right">76.8%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">318</td>
<td align="right">11.8%</td>
<td align="right">318</td>
<td align="right">11.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">96</td>
<td align="right">3.5%</td>
<td align="right">96</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">46</td>
<td align="right">1.7%</td>
<td align="right">46</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">1.7%</td>
<td align="right">46</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">31</td>
<td align="right">1.1%</td>
<td align="right">31</td>
<td align="right">1.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,909,736</td>
<td align="right">89.4%</td>
<td align="right">43,114,549</td>
<td align="right">89.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,001,850</td>
<td align="right">10.4%</td>
<td align="right">5,016,382</td>
<td align="right">10.4%</td>
<td align="right">0.3%</td>
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
<td align="right">95,521</td>
<td align="right">98.6%</td>
<td align="right">95,815</td>
<td align="right">98.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,367</td>
<td align="right">1.4%</td>
<td align="right">1,367</td>
<td align="right">1.4%</td>
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
<td align="right">67,018,472</td>
<td align="right">100.0%</td>
<td align="right">68,007,572</td>
<td align="right">100.0%</td>
<td align="right">1.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">8,068,158</td>
<td align="right">100.0%</td>
<td align="right">4,337,171</td>
<td align="right">53.3%</td>
<td align="right">-46.2%</td>
</tr>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3,802,736</td>
<td align="right">46.7%</td>
<td align="right"></td>
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
<td align="right">71,751</td>
<td align="right">100.0%</td>
<td align="right">3,587,450.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,258,471</td>
<td align="right">85.5%</td>
<td align="right">41,413,640</td>
<td align="right">85.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,318,315</td>
<td align="right">6.9%</td>
<td align="right">3,318,315</td>
<td align="right">6.9%</td>
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
<td align="right">3,688,911</td>
<td align="right">7.6%</td>
<td align="right">3,688,911</td>
<td align="right">7.6%</td>
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
<td align="right">69,996</td>
<td align="right">98.7%</td>
<td align="right">69,996</td>
<td align="right">98.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">900</td>
<td align="right">1.3%</td>
<td align="right">900</td>
<td align="right">1.3%</td>
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
<td align="right">713</td>
<td align="right">79.2%</td>
<td align="right">713</td>
<td align="right">79.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">187</td>
<td align="right">20.8%</td>
<td align="right">187</td>
<td align="right">20.8%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,472,816</td>
<td align="right">1.3%</td>
<td align="right">13,752,056</td>
<td align="right">1.9%</td>
<td align="right">45.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">313,750,505</td>
<td align="right">42.2%</td>
<td align="right">302,554,713</td>
<td align="right">41.0%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">14,555,042</td>
<td align="right">2.0%</td>
<td align="right">14,881,778</td>
<td align="right">2.0%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">405,241,277</td>
<td align="right">54.5%</td>
<td align="right">407,156,322</td>
<td align="right">55.1%</td>
<td align="right">0.5%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">9,480,242</td>
<td align="right">63.3%</td>
<td align="right">9,793,810</td>
<td align="right">64.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">428,626</td>
<td align="right">2.9%</td>
<td align="right">441,730</td>
<td align="right">2.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">427,346</td>
<td align="right">2.9%</td>
<td align="right">428,900</td>
<td align="right">2.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,318,315</td>
<td align="right">22.2%</td>
<td align="right">3,318,315</td>
<td align="right">21.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,057,806</td>
<td align="right">7.1%</td>
<td align="right">1,057,806</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">105,734</td>
<td align="right">0.7%</td>
<td align="right">105,734</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,516</td>
<td align="right">0.6%</td>
<td align="right">90,516</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">58,333</td>
<td align="right">0.4%</td>
<td align="right">58,333</td>
<td align="right">0.4%</td>
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
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">303</td>
<td align="right">0.0%</td>
<td align="right">303</td>
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
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">250,908</td>
<td align="right">2.6%</td>
<td align="right">252,504</td>
<td align="right">1.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,148,273</td>
<td align="right">33.2%</td>
<td align="right">3,162,805</td>
<td align="right">23.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,537,897</td>
<td align="right">26.8%</td>
<td align="right">2,537,897</td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,431,958</td>
<td align="right">15.1%</td>
<td align="right">1,431,958</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">865,265</td>
<td align="right">9.1%</td>
<td align="right">865,265</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">398,733</td>
<td align="right">4.2%</td>
<td align="right">398,733</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">342,677</td>
<td align="right">3.6%</td>
<td align="right">342,677</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">284,172</td>
<td align="right">3.0%</td>
<td align="right">284,172</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">184,279</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">3,802,736</td>
<td align="right">27.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">460,288</td>
<td align="right">3.3%</td>
<td align="right"></td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">6,705,732</td>
<td align="right">13.0%</td>
<td align="right">7,157,337</td>
<td align="right">13.9%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">11,780,715</td>
<td align="right">22.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,329,110</td>
<td align="right">21.9%</td>
<td align="right">11,780,715</td>
<td align="right">22.8%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">40,284,842</td>
<td align="right">78.1%</td>
<td align="right">39,833,237</td>
<td align="right">77.2%</td>
<td align="right">-1.1%</td>
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
<td align="right">63</td>
<td align="right">0.0%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,470</td>
<td align="right"></td>
<td align="right">1,084</td>
<td align="right"></td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">296,885,986</td>
<td align="right">42.9%</td>
<td align="right">304,190,236</td>
<td align="right">43.3%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">353,654,345</td>
<td align="right">46.1%</td>
<td align="right">360,822,345</td>
<td align="right">46.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">119,443,699</td>
<td align="right">15.6%</td>
<td align="right">121,558,595</td>
<td align="right">15.6%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">202,852,114</td>
<td align="right">29.3%</td>
<td align="right">205,753,148</td>
<td align="right">29.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">76,122,407</td>
<td align="right">11.0%</td>
<td align="right">77,179,155</td>
<td align="right">11.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">222,901,641</td>
<td align="right">29.1%</td>
<td align="right">225,939,353</td>
<td align="right">29.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">31,893</td>
<td align="right">0.0%</td>
<td align="right">32,049</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">471,434</td>
<td align="right"></td>
<td align="right">469,218</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">470,729</td>
<td align="right"></td>
<td align="right">468,584</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">70,793,037</td>
<td align="right">9.2%</td>
<td align="right">71,109,761</td>
<td align="right">9.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">116,238,008</td>
<td align="right">16.8%</td>
<td align="right">115,764,487</td>
<td align="right">16.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,210,715</td>
<td align="right"></td>
<td align="right">5,227,392</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">45,724,106</td>
<td align="right"></td>
<td align="right">45,724,540</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">47,141,058</td>
<td align="right"></td>
<td align="right">47,141,444</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,400,854</td>
<td align="right">54.3%</td>
<td align="right">45,401,031</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,160,297</td>
<td align="right"></td>
<td align="right">38,160,361</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,163,006</td>
<td align="right">45.7%</td>
<td align="right">38,163,070</td>
<td align="right">45.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,368,898</td>
<td align="right">54.3%</td>
<td align="right">45,368,856</td>
<td align="right">54.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">31,555</td>
<td align="right">274,023</td>
<td align="right">4,028</td>
<td align="right">36,699</td>
<td align="right">21</td>
<td align="right">31,475</td>
<td align="right">273,933</td>
<td align="right">4,559</td>
<td align="right">36,684</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">65</td>
<td align="right">2.0%</td>
<td align="right">554</td>
<td align="right">16.7%</td>
<td align="right">752.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">42</td>
<td align="right">1.3%</td>
<td align="right">129</td>
<td align="right">3.9%</td>
<td align="right">207.1%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">830</td>
<td align="right">25.2%</td>
<td align="right">63</td>
<td align="right">1.9%</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">63</td>
<td align="right">1.9%</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">11,785,337</td>
<td align="right"></td>
<td align="right">19,311,436</td>
<td align="right"></td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">405</td>
<td align="right">12.3%</td>
<td align="right">561</td>
<td align="right">16.9%</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">241,910,685</td>
<td align="right">2,052.6%</td>
<td align="right">305,801,032</td>
<td align="right">1,583.5%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">2,063</td>
<td align="right">62.6%</td>
<td align="right">2,209</td>
<td align="right">66.6%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,298</td>
<td align="right"></td>
<td align="right">3,319</td>
<td align="right"></td>
<td align="right">0.6%</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">486</td>
<td align="right">14.6%</td>
<td align="right">486 / 0 !!</td>
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
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">384</td>
<td align="right">94.8%</td>
<td align="right">561</td>
<td align="right">100.0%</td>
<td align="right">46.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">405</td>
<td align="right"></td>
<td align="right">561</td>
<td align="right"></td>
<td align="right">38.5%</td>
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
<td align="right">3,313,664</td>
<td align="right">52.3%</td>
<td align="right">10,194,944</td>
<td align="right">95.8%</td>
<td align="right">207.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">777,960</td>
<td align="right">12.3%</td>
<td align="right">1,376,304</td>
<td align="right">12.9%</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">4,587,100</td>
<td align="right">72.3%</td>
<td align="right">8,016,600</td>
<td align="right">75.3%</td>
<td align="right">74.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">6,340,608</td>
<td align="right"></td>
<td align="right">10,641,408</td>
<td align="right"></td>
<td align="right">67.8%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">975,548</td>
<td align="right">15.4%</td>
<td align="right">1,248,504</td>
<td align="right">11.7%</td>
<td align="right">28.0%</td>
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
<td align="left">44</td>
<td align="right">11.5%</td>
<td align="left">90</td>
<td align="right">16.0%</td>
<td align="right">104.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">148</td>
<td align="right">38.5%</td>
<td align="left">148</td>
<td align="right">26.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">65</td>
<td align="right">16.9%</td>
<td align="left">111</td>
<td align="right">19.8%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">85</td>
<td align="right">22.1%</td>
<td align="left">107</td>
<td align="right">19.1%</td>
<td align="right">25.9%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">10.9%</td>
<td align="left">105</td>
<td align="right">18.7%</td>
<td align="right">150.0%</td>
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
<td align="right">44</td>
<td align="right">10.9%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">88</td>
<td align="right">15.7%</td>
<td align="right">88 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">148</td>
<td align="right">36.5%</td>
<td align="right">149</td>
<td align="right">26.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">64</td>
<td align="right">15.8%</td>
<td align="right">109</td>
<td align="right">19.4%</td>
<td align="right">70.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">65</td>
<td align="right">16.0%</td>
<td align="right">88</td>
<td align="right">15.7%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">5.2%</td>
<td align="right">42</td>
<td align="right">7.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">63</td>
<td align="right">15.6%</td>
<td align="right">84</td>
<td align="right">15.0%</td>
<td align="right">33.3%</td>
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
<td align="right">44</td>
<td align="right">10.9%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">88</td>
<td align="right">15.7%</td>
<td align="right">88 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">148</td>
<td align="right">36.5%</td>
<td align="right">149</td>
<td align="right">26.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">65</td>
<td align="right">16.0%</td>
<td align="right">111</td>
<td align="right">19.8%</td>
<td align="right">70.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">64</td>
<td align="right">15.8%</td>
<td align="right">86</td>
<td align="right">15.3%</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">15.6%</td>
<td align="right">126</td>
<td align="right">22.5%</td>
<td align="right">100.0%</td>
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
<td align="left">_RESUME_CHECK</td>
<td align="right">2,628,636</td>
<td align="right">6,073,044</td>
<td align="right">131.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,766,325</td>
<td align="right">7,616,353</td>
<td align="right">102.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">19,887</td>
<td align="right">714</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">3,654</td>
<td align="right">714</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">10,920</td>
<td align="right">2,772</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">11,785,337</td>
<td align="right">19,311,436</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">11,785,337</td>
<td align="right">19,311,414</td>
<td align="right">63.9%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">13,025,337</td>
<td align="right">20,422,475</td>
<td align="right">56.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">258,412</td>
<td align="right">142,198</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">345,772</td>
<td align="right">190,477</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">10,920</td>
<td align="right">6,678</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">372,274</td>
<td align="right">230,209</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">27,392,140</td>
<td align="right">34,631,055</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">10,522,331</td>
<td align="right">12,793,494</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">62,391</td>
<td align="right">49,287</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">62,391</td>
<td align="right">49,287</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">305,824</td>
<td align="right">252,316</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">305,824</td>
<td align="right">252,316</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">14,220,293</td>
<td align="right">16,325,565</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">62,391</td>
<td align="right">53,193</td>
<td align="right">-14.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,091,132</td>
<td align="right">947,513</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,569,456</td>
<td align="right">1,378,608</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">1,736,545</td>
<td align="right">1,534,021</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,580,022</td>
<td align="right">4,097,337</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,224</td>
<td align="right">25,284</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,240,000</td>
<td align="right">1,111,039</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">9,896,731</td>
<td align="right">9,031,216</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">2,593,020</td>
<td align="right">2,386,527</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">5,133,603</td>
<td align="right">4,731,831</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,458,956</td>
<td align="right">2,276,907</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,581,974</td>
<td align="right">2,391,525</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">7,760,321</td>
<td align="right">7,191,494</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">1,848,231</td>
<td align="right">1,714,713</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">4,474,883</td>
<td align="right">4,152,637</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">4,474,883</td>
<td align="right">4,152,637</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">5,105,015</td>
<td align="right">4,738,061</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">18,334,877</td>
<td align="right">17,068,429</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,552,099</td>
<td align="right">1,446,469</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">5,073,557</td>
<td align="right">4,738,061</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,458,683</td>
<td align="right">2,298,600</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">1,319,381</td>
<td align="right">1,235,381</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,628,051</td>
<td align="right">2,481,842</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,516,210</td>
<td align="right">1,436,914</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,766,325</td>
<td align="right">3,571,046</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,457,473</td>
<td align="right">1,388,341</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,453,819</td>
<td align="right">1,387,627</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,455,667</td>
<td align="right">1,389,475</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,940,641</td>
<td align="right">6,627,073</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,365,146</td>
<td align="right">1,312,604</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,365,146</td>
<td align="right">1,312,604</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,308,761</td>
<td align="right">1,264,199</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,715,540</td>
<td align="right">2,628,201</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,300,907</td>
<td align="right">1,261,469</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,283,057</td>
<td align="right">1,244,396</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,295,548</td>
<td align="right">2,229,587</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,297,253</td>
<td align="right">1,260,755</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,138,735</td>
<td align="right">6,944,569</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,430,215</td>
<td align="right">1,394,242</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,773,973</td>
<td align="right">5,645,075</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,367,824</td>
<td align="right">1,341,070</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,200,080</td>
<td align="right">1,186,976</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,161,020</td>
<td align="right">1,172,234</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,209,068</td>
<td align="right">1,203,503</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,137,689</td>
<td align="right">1,137,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,137,689</td>
<td align="right">1,137,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,137,689</td>
<td align="right">1,137,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,137,689</td>
<td align="right">1,137,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,098,894</td>
<td align="right">1,098,894</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">757,645</td>
<td align="right">757,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">498,623</td>
<td align="right">498,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">498,623</td>
<td align="right">498,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">353,534</td>
<td align="right">353,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">348,074</td>
<td align="right">348,074</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">31,458</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">31,458</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,233</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">12,285</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">12,285</td>
<td align="right">12,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">6,825</td>
<td align="right">6,825</td>
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
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_OFFSET</td>
<td align="right"></td>
<td align="right">5,292,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN</td>
<td align="right"></td>
<td align="right">5,292,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FOR_ITER_GEN_FUNCTION</td>
<td align="right"></td>
<td align="right">5,292,458</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_SEND_GEN_OFFSET</td>
<td align="right"></td>
<td align="right">3,597,839</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_SEND_GEN</td>
<td align="right"></td>
<td align="right">3,597,839</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_SEND_GEN_FUNCTION</td>
<td align="right"></td>
<td align="right">3,597,839</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">2,459,542</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">1,585,765</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">793,394</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">19,467</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">19,467</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">11,676</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right"></td>
<td align="right">11,676</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">7,812</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right"></td>
<td align="right">7,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">7,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right"></td>
<td align="right">7,791</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">3,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">3,885</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">22</td>
<td align="right"></td>
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
Stats gathered on: 2025-02-14
