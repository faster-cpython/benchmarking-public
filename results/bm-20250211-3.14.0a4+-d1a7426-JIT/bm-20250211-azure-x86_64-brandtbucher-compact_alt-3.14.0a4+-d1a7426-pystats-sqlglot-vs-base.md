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
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,152,964</td>
<td align="right">46,592</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,452,224</td>
<td align="right">22,400</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,452,224</td>
<td align="right">22,402</td>
<td align="right">-99.1%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,847,283</td>
<td align="right">65,652</td>
<td align="right">-97.7%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">434,110</td>
<td align="right">11,829</td>
<td align="right">-97.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,026,582</td>
<td align="right">131,700</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">8,068,158</td>
<td align="right">417,937</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,615,936</td>
<td align="right">395,537</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,346,174</td>
<td align="right">304,896</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">3,671,228</td>
<td align="right">359,515</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,309,593</td>
<td align="right">910,756</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,897,649</td>
<td align="right">300,598</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">6,027,997</td>
<td align="right">961,539</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">10,182,363</td>
<td align="right">1,982,137</td>
<td align="right">-80.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">13,059,392</td>
<td align="right">2,660,923</td>
<td align="right">-79.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">3,630,463</td>
<td align="right">773,415</td>
<td align="right">-78.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,414,550</td>
<td align="right">5,537,538</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,998,402</td>
<td align="right">1,126,969</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,479,872</td>
<td align="right">2,485,308</td>
<td align="right">-70.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,817,856</td>
<td align="right">830,924</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,785,099</td>
<td align="right">1,760,058</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">283,898</td>
<td align="right">97,628</td>
<td align="right">-65.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">10,191,302</td>
<td align="right">4,069,087</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">12,498,311</td>
<td align="right">5,143,491</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">540,683</td>
<td align="right">230,053</td>
<td align="right">-57.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">15,472,686</td>
<td align="right">6,937,207</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,917,233</td>
<td align="right">3,615,442</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">8,067,075</td>
<td align="right">3,714,593</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">11,235,296</td>
<td align="right">5,182,223</td>
<td align="right">-53.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">10,742,262</td>
<td align="right">5,285,624</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">23,250,452</td>
<td align="right">11,474,993</td>
<td align="right">-50.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,300,150</td>
<td align="right">3,136,089</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">721,280</td>
<td align="right">362,688</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">19,643,047</td>
<td align="right">10,516,740</td>
<td align="right">-46.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">318,718</td>
<td align="right">454,924</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">743,162</td>
<td align="right">435,872</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,849,993</td>
<td align="right">4,040,586</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">121,557,130</td>
<td align="right">72,712,961</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">19,468,533</td>
<td align="right">12,187,247</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">35,783,946</td>
<td align="right">22,624,801</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">36,311,589</td>
<td align="right">23,158,247</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">8,766,410</td>
<td align="right">5,595,387</td>
<td align="right">-36.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,542,431</td>
<td align="right">10,695,669</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">44,551,207</td>
<td align="right">29,533,301</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,420,608</td>
<td align="right">4,277,720</td>
<td align="right">-33.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">27,374,975</td>
<td align="right">18,420,474</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,325,639</td>
<td align="right">4,987,046</td>
<td align="right">-31.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,908,784</td>
<td align="right">5,553,195</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">31,540,090</td>
<td align="right">22,561,364</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">56,310</td>
<td align="right">40,905</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,525,020</td>
<td align="right">3,146,816</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,312,552</td>
<td align="right">11,652,483</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">99,517</td>
<td align="right">75,913</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,607</td>
<td align="right">69,292</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">210,778</td>
<td align="right">161,575</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">427,998</td>
<td align="right">329,340</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">97,992</td>
<td align="right">76,656</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">11,728,296</td>
<td align="right">9,338,784</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">110,144</td>
<td align="right">88,808</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">54,743,196</td>
<td align="right">44,995,896</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">25,408</td>
<td align="right">20,956</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">58,680</td>
<td align="right">49,755</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">573,246</td>
<td align="right">493,761</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">279,324</td>
<td align="right">243,204</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">90,612</td>
<td align="right">79,041</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,129,648</td>
<td align="right">1,909,633</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">214,550</td>
<td align="right">195,251</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">65,524</td>
<td align="right">59,728</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">317,520</td>
<td align="right">343,182</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,013,885</td>
<td align="right">3,197,184</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">1,825,052</td>
<td align="right">1,932,551</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,386,901</td>
<td align="right">2,266,129</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,460,962</td>
<td align="right">2,577,197</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">3,018,178</td>
<td align="right">3,128,869</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">632,407</td>
<td align="right">610,504</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">3,589,162</td>
<td align="right">3,698,319</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,000,784</td>
<td align="right">973,127</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">21,501</td>
<td align="right">21,354</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">503,222</td>
<td align="right">502,130</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">514,048</td>
<td align="right">513,901</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,329,046</td>
<td align="right">11,329,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,798,261</td>
<td align="right">3,798,261</td>
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
<td align="left">COPY_FREE_VARS</td>
<td align="right">3,002,944</td>
<td align="right">3,002,944</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,848,064</td>
<td align="right">2,848,064</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,646,270</td>
<td align="right">2,646,270</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">477,034</td>
<td align="right">477,034</td>
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
<td align="left">LOAD_ATTR</td>
<td align="right">108,370</td>
<td align="right">108,370</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">27,136</td>
<td align="right">27,136</td>
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
<td align="left">NOT_TAKEN</td>
<td align="right">5,166</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">49,429</td>
<td align="right">9.0%</td>
<td align="right">-15.3%</td>
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
<td align="right">90.9%</td>
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
<td align="left">Failure</td>
<td align="right">258</td>
<td align="right">74.4%</td>
<td align="right">237</td>
<td align="right">72.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">89</td>
<td align="right">25.6%</td>
<td align="right">89</td>
<td align="right">27.3%</td>
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
<td align="right">19.0%</td>
<td align="right">28</td>
<td align="right">11.8%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">94</td>
<td align="right">36.4%</td>
<td align="right">94</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">49</td>
<td align="right">19.0%</td>
<td align="right">49</td>
<td align="right">20.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">45</td>
<td align="right">17.4%</td>
<td align="right">45</td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">8.1%</td>
<td align="right">21</td>
<td align="right">8.9%</td>
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
<td align="right">430,735</td>
<td align="right">0.6%</td>
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
<td align="right">427,346</td>
<td align="right">0.6%</td>
<td align="right">422,978</td>
<td align="right">0.6%</td>
<td align="right">-1.0%</td>
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
<td align="right">75,100,512</td>
<td align="right">99.4%</td>
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
<td align="right">9,425</td>
<td align="right">100.0%</td>
<td align="right">9,341</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">971,979</td>
<td align="right">74.6%</td>
<td align="right">-2.8%</td>
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
<td align="right">25.4%</td>
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
<td align="right">1,135</td>
<td align="right">97.1%</td>
<td align="right">1,114</td>
<td align="right">97.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">34</td>
<td align="right">2.9%</td>
<td align="right">34</td>
<td align="right">3.0%</td>
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
<td align="left">set</td>
<td align="right">52</td>
<td align="right">4.6%</td>
<td align="right">31</td>
<td align="right">2.8%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">408</td>
<td align="right">35.9%</td>
<td align="right">408</td>
<td align="right">36.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">400</td>
<td align="right">35.2%</td>
<td align="right">400</td>
<td align="right">35.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">181</td>
<td align="right">15.9%</td>
<td align="right">181</td>
<td align="right">16.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">50</td>
<td align="right">4.4%</td>
<td align="right">50</td>
<td align="right">4.5%</td>
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
<td align="right">317,284</td>
<td align="right">94.7%</td>
<td align="right">342,967</td>
<td align="right">95.1%</td>
<td align="right">8.1%</td>
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
<td align="right">4.6%</td>
<td align="right">15,284</td>
<td align="right">4.2%</td>
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
<td align="right">0.7%</td>
<td align="right">2,286</td>
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
<td align="left">Failure</td>
<td align="right">227</td>
<td align="right">81.4%</td>
<td align="right">206</td>
<td align="right">79.8%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">52</td>
<td align="right">18.6%</td>
<td align="right">52</td>
<td align="right">20.2%</td>
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
<td align="right">206</td>
<td align="right">100.0%</td>
<td align="right">-9.3%</td>
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
<td align="right">10,188,366</td>
<td align="right">49.7%</td>
<td align="right">4,067,725</td>
<td align="right">44.7%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,299,666</td>
<td align="right">50.3%</td>
<td align="right">5,037,035</td>
<td align="right">55.3%</td>
<td align="right">-51.1%</td>
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
<td align="right">2,897</td>
<td align="right">98.7%</td>
<td align="right">1,323</td>
<td align="right">97.1%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39</td>
<td align="right">1.3%</td>
<td align="right">39</td>
<td align="right">2.9%</td>
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
<td align="right">31</td>
<td align="right">1.1%</td>
<td align="right">52</td>
<td align="right">3.9%</td>
<td align="right">67.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">2,276</td>
<td align="right">78.6%</td>
<td align="right">851</td>
<td align="right">64.3%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">318</td>
<td align="right">11.0%</td>
<td align="right">148</td>
<td align="right">11.2%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">84</td>
<td align="right">2.9%</td>
<td align="right">105</td>
<td align="right">7.9%</td>
<td align="right">25.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">96</td>
<td align="right">3.3%</td>
<td align="right">75</td>
<td align="right">5.7%</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">46</td>
<td align="right">1.6%</td>
<td align="right">46</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">46</td>
<td align="right">1.6%</td>
<td align="right">46</td>
<td align="right">3.5%</td>
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
<td align="right">5,503,104</td>
<td align="right">11.5%</td>
<td align="right">2,830,930</td>
<td align="right">5.8%</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,417,940</td>
<td align="right">88.3%</td>
<td align="right">45,694,471</td>
<td align="right">94.0%</td>
<td align="right">7.7%</td>
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
<td align="right">104,979</td>
<td align="right">98.7%</td>
<td align="right">54,612</td>
<td align="right">97.6%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">1,367</td>
<td align="right">2.4%</td>
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
<td align="right">75,024,652</td>
<td align="right">100.0%</td>
<td align="right">82,626,785</td>
<td align="right">100.0%</td>
<td align="right">10.1%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">242,854</td>
<td align="right">41.4%</td>
<td align="right">321,268</td>
<td align="right">55.0%</td>
<td align="right">32.3%</td>
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
<td align="right">262,751</td>
<td align="right">45.0%</td>
<td align="right">-23.3%</td>
</tr>
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
<td align="right">5,251</td>
<td align="right">100.0%</td>
<td align="right">-22.4%</td>
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
<td align="right">3,025,356</td>
<td align="right">6.3%</td>
<td align="right">131,176</td>
<td align="right">0.3%</td>
<td align="right">-95.7%</td>
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
<td align="right">7.7%</td>
<td align="right">2,980,484</td>
<td align="right">6.6%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,142,089</td>
<td align="right">86.0%</td>
<td align="right">41,982,476</td>
<td align="right">93.1%</td>
<td align="right">2.0%</td>
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
<td align="right">815</td>
<td align="right">1.2%</td>
<td align="right">113</td>
<td align="right">0.2%</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">69,996</td>
<td align="right">98.8%</td>
<td align="right">56,640</td>
<td align="right">99.8%</td>
<td align="right">-19.1%</td>
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
<td align="right">87.5%</td>
<td align="right">11</td>
<td align="right">9.7%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">102</td>
<td align="right">12.5%</td>
<td align="right">102</td>
<td align="right">90.3%</td>
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
<td align="right">69,201</td>
<td align="right">0.5%</td>
<td align="right">-23.5%</td>
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
<td align="right">99.5%</td>
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
<td align="right">14,800,781</td>
<td align="right">1.9%</td>
<td align="right">5,751,449</td>
<td align="right">1.3%</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">408,406,775</td>
<td align="right">53.4%</td>
<td align="right">222,656,507</td>
<td align="right">49.7%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">332,134,663</td>
<td align="right">43.4%</td>
<td align="right">213,178,846</td>
<td align="right">47.6%</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,974,130</td>
<td align="right">1.3%</td>
<td align="right">6,509,869</td>
<td align="right">1.5%</td>
<td align="right">-34.7%</td>
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
<td align="right">3,025,356</td>
<td align="right">19.9%</td>
<td align="right">131,176</td>
<td align="right">2.1%</td>
<td align="right">-95.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">10,188,366</td>
<td align="right">67.0%</td>
<td align="right">4,067,725</td>
<td align="right">66.0%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,516</td>
<td align="right">0.6%</td>
<td align="right">69,201</td>
<td align="right">1.1%</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">58,333</td>
<td align="right">0.4%</td>
<td align="right">49,429</td>
<td align="right">0.8%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">317,284</td>
<td align="right">2.1%</td>
<td align="right">342,967</td>
<td align="right">5.6%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">999,615</td>
<td align="right">6.6%</td>
<td align="right">971,979</td>
<td align="right">15.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">427,346</td>
<td align="right">2.8%</td>
<td align="right">422,978</td>
<td align="right">6.9%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">105,734</td>
<td align="right">0.7%</td>
<td align="right">105,734</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,904</td>
<td align="right">0.0%</td>
<td align="right">3,904</td>
<td align="right">0.1%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,933,212</td>
<td align="right">19.4%</td>
<td align="right">792,687</td>
<td align="right">12.2%</td>
<td align="right">-59.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,148,273</td>
<td align="right">31.6%</td>
<td align="right">1,616,624</td>
<td align="right">24.8%</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">865,265</td>
<td align="right">8.7%</td>
<td align="right">632,522</td>
<td align="right">9.7%</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">342,677</td>
<td align="right">3.4%</td>
<td align="right">262,751</td>
<td align="right">4.0%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,537,897</td>
<td align="right">25.4%</td>
<td align="right">2,062,906</td>
<td align="right">31.7%</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">250,908</td>
<td align="right">2.5%</td>
<td align="right">246,456</td>
<td align="right">3.8%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">398,733</td>
<td align="right">4.0%</td>
<td align="right">398,733</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">284,172</td>
<td align="right">2.8%</td>
<td align="right">284,172</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">184,279</td>
<td align="right">1.8%</td>
<td align="right">184,279</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,886</td>
<td align="right">0.2%</td>
<td align="right">22,886</td>
<td align="right">0.4%</td>
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
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">665</td>
<td align="right">0.0%</td>
<td align="right">533.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">1,246</td>
<td align="right"></td>
<td align="right">4,175</td>
<td align="right"></td>
<td align="right">235.1%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">187,735,331</td>
<td align="right">27.0%</td>
<td align="right">317,310,251</td>
<td align="right">42.2%</td>
<td align="right">69.0%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">216,136,687</td>
<td align="right">28.2%</td>
<td align="right">321,871,398</td>
<td align="right">38.4%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,702,715</td>
<td align="right"></td>
<td align="right">3,193,259</td>
<td align="right"></td>
<td align="right">-44.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">121,287,378</td>
<td align="right">15.8%</td>
<td align="right">150,838,599</td>
<td align="right">18.0%</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">80,828,982</td>
<td align="right">11.6%</td>
<td align="right">61,239,912</td>
<td align="right">8.1%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">311,277,558</td>
<td align="right">44.8%</td>
<td align="right">238,909,583</td>
<td align="right">31.7%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">68,581,801</td>
<td align="right">9.0%</td>
<td align="right">53,690,568</td>
<td align="right">6.4%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">114,986,097</td>
<td align="right">16.5%</td>
<td align="right">135,139,010</td>
<td align="right">18.0%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">359,694,382</td>
<td align="right">47.0%</td>
<td align="right">311,167,235</td>
<td align="right">37.2%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">479,983</td>
<td align="right"></td>
<td align="right">473,825</td>
<td align="right"></td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">31,873</td>
<td align="right">0.0%</td>
<td align="right">32,222</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">480,578</td>
<td align="right"></td>
<td align="right">477,270</td>
<td align="right"></td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">47,141,282</td>
<td align="right"></td>
<td align="right">46,897,405</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">45,401,000</td>
<td align="right">54.3%</td>
<td align="right">45,402,195</td>
<td align="right">54.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">45,724,453</td>
<td align="right"></td>
<td align="right">45,725,533</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">38,160,277</td>
<td align="right"></td>
<td align="right">38,160,893</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">38,162,986</td>
<td align="right">45.7%</td>
<td align="right">38,163,602</td>
<td align="right">45.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">45,369,022</td>
<td align="right">54.3%</td>
<td align="right">45,369,308</td>
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
<td align="right">31,475</td>
<td align="right">273,900</td>
<td align="right">4,529</td>
<td align="right">36,771</td>
<td align="right">21</td>
<td align="right">31,555</td>
<td align="right">273,965</td>
<td align="right">4,170</td>
<td align="right">36,679</td>
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
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">185,120,577</td>
<td align="right">1,622.4%</td>
<td align="right">1,121,404,218</td>
<td align="right">2,118.0%</td>
<td align="right">505.8%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">11,410,121</td>
<td align="right"></td>
<td align="right">52,947,338</td>
<td align="right"></td>
<td align="right">364.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">530</td>
<td align="right">13.8%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,234</td>
<td align="right">32.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,126</td>
<td align="right">29.2%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">21</td>
<td align="right">0.5%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">42</td>
<td align="right">1.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">42</td>
<td align="right">1.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,194</td>
<td align="right">57.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,850</td>
<td align="right"></td>
<td align="right">408</td>
<td align="right"></td>
<td align="right">-89.4%</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right"></td>
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
<td align="right">530</td>
<td align="right"></td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">530</td>
<td align="right">100.0%</td>
<td align="right">0</td>
<td align="right"></td>
<td align="right">-100.0%</td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right"></td>
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
<td align="right">3,227,648</td>
<td align="right">35.2%</td>
<td align="right">7,323,648</td>
<td align="right">73.3%</td>
<td align="right">126.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">1,143,968</td>
<td align="right">12.5%</td>
<td align="right">1,777,480</td>
<td align="right">17.8%</td>
<td align="right">55.4%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">1,350,498</td>
<td align="right">14.7%</td>
<td align="right">768,070</td>
<td align="right">7.7%</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">6,664,190</td>
<td align="right">72.8%</td>
<td align="right">7,448,690</td>
<td align="right">74.5%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">9,158,656</td>
<td align="right"></td>
<td align="right">9,994,240</td>
<td align="right"></td>
<td align="right">9.1%</td>
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
<td align="left">169</td>
<td align="right">31.9%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">171</td>
<td align="right">32.3%</td>
<td align="left">22</td>
<td align="right">7.3%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">43</td>
<td align="right">8.1%</td>
<td align="left">66</td>
<td align="right">21.8%</td>
<td align="right">53.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">63</td>
<td align="right">11.9%</td>
<td align="left">67</td>
<td align="right">22.1%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">7.9%</td>
<td align="left">127</td>
<td align="right">41.9%</td>
<td align="right">202.4%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">42</td>
<td align="right">7.9%</td>
<td align="left">21</td>
<td align="right">6.9%</td>
<td align="right">-50.0%</td>
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
<td align="right">168</td>
<td align="right">31.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">149</td>
<td align="right">28.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">64</td>
<td align="right">12.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">43</td>
<td align="right">8.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">21</td>
<td align="right">4.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">84</td>
<td align="right">15.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">125</td>
<td align="right">23.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">43</td>
<td align="right">8.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">24</td>
<td align="right">4.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">148</td>
<td align="right">27.9%</td>
<td align="right">2</td>
<td align="right">2 / 0 !!</td>
<td align="right">-98.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">43</td>
<td align="right">8.1%</td>
<td align="right">193</td>
<td align="right">193 / 0 !!</td>
<td align="right">348.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">63</td>
<td align="right">11.9%</td>
<td align="right">108</td>
<td align="right">108 / 0 !!</td>
<td align="right">71.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">7.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">42</td>
<td align="right">7.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,394</td>
<td align="right">312,024</td>
<td align="right">22,283.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">232,764</td>
<td align="right">11,847,992</td>
<td align="right">4,990.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">232,764</td>
<td align="right">11,847,992</td>
<td align="right">4,990.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">62,391</td>
<td align="right">2,871,798</td>
<td align="right">4,502.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">136,269</td>
<td align="right">5,954,165</td>
<td align="right">4,269.4%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">407,337</td>
<td align="right">15,267,849</td>
<td align="right">3,648.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">407,337</td>
<td align="right">15,267,849</td>
<td align="right">3,648.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">407,337</td>
<td align="right">15,267,849</td>
<td align="right">3,648.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">571,423</td>
<td align="right">19,307,634</td>
<td align="right">3,278.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">550,230</td>
<td align="right">16,674,201</td>
<td align="right">2,930.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">62,391</td>
<td align="right">1,546,656</td>
<td align="right">2,379.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">372,477</td>
<td align="right">9,062,174</td>
<td align="right">2,332.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">128,667</td>
<td align="right">3,000,100</td>
<td align="right">2,231.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">232,764</td>
<td align="right">5,339,136</td>
<td align="right">2,193.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">389,330</td>
<td align="right">8,924,809</td>
<td align="right">2,192.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">536,907</td>
<td align="right">12,108,453</td>
<td align="right">2,155.2%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,244,662</td>
<td align="right">22,812,015</td>
<td align="right">1,732.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">316,103</td>
<td align="right">5,366,907</td>
<td align="right">1,597.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,848</td>
<td align="right">28,980</td>
<td align="right">1,468.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">232,764</td>
<td align="right">3,375,324</td>
<td align="right">1,350.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">232,764</td>
<td align="right">3,375,324</td>
<td align="right">1,350.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">232,764</td>
<td align="right">3,375,324</td>
<td align="right">1,350.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">1,848</td>
<td align="right">23,184</td>
<td align="right">1,154.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,848</td>
<td align="right">23,184</td>
<td align="right">1,154.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">264,776</td>
<td align="right">3,267,707</td>
<td align="right">1,134.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,909,639</td>
<td align="right">23,146,072</td>
<td align="right">1,112.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">271,142</td>
<td align="right">3,234,868</td>
<td align="right">1,093.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,591</td>
<td align="right">3,319,869</td>
<td align="right">1,091.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">292,959</td>
<td align="right">3,187,139</td>
<td align="right">987.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,676,875</td>
<td align="right">16,695,493</td>
<td align="right">895.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">424,591</td>
<td align="right">4,084,660</td>
<td align="right">862.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">398,627</td>
<td align="right">3,569,650</td>
<td align="right">795.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">1,060,898</td>
<td align="right">9,432,389</td>
<td align="right">789.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">327,485</td>
<td align="right">2,871,523</td>
<td align="right">776.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">13,422,436</td>
<td align="right">114,969,131</td>
<td align="right">756.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">2,244,682</td>
<td align="right">18,998,395</td>
<td align="right">746.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">389,876</td>
<td align="right">2,913,292</td>
<td align="right">647.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">12,285</td>
<td align="right">90,258</td>
<td align="right">634.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">422,777</td>
<td align="right">3,055,169</td>
<td align="right">622.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">232,764</td>
<td align="right">1,680,534</td>
<td align="right">622.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">950,236</td>
<td align="right">6,349,073</td>
<td align="right">568.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">950,236</td>
<td align="right">6,349,073</td>
<td align="right">568.2%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,630,213</td>
<td align="right">10,608,939</td>
<td align="right">550.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,909,639</td>
<td align="right">12,184,138</td>
<td align="right">538.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,695,624</td>
<td align="right">16,597,141</td>
<td align="right">515.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">487,016</td>
<td align="right">2,910,466</td>
<td align="right">497.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">488,656</td>
<td align="right">2,844,245</td>
<td align="right">482.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">540,167</td>
<td align="right">2,977,540</td>
<td align="right">451.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,111,655</td>
<td align="right">16,761,242</td>
<td align="right">438.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">2,563,853</td>
<td align="right">13,731,081</td>
<td align="right">435.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">10,920</td>
<td align="right">56,679</td>
<td align="right">419.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">575,256</td>
<td align="right">2,964,768</td>
<td align="right">415.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">367,992</td>
<td align="right">1,866,907</td>
<td align="right">407.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">1,111,023</td>
<td align="right">5,541,502</td>
<td align="right">398.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">13,057,655</td>
<td align="right">62,973,513</td>
<td align="right">382.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">757,645</td>
<td align="right">3,539,276</td>
<td align="right">367.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">11,410,121</td>
<td align="right">52,947,338</td>
<td align="right">364.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">4,890,165</td>
<td align="right">21,662,866</td>
<td align="right">343.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">576,665</td>
<td align="right">2,305,094</td>
<td align="right">299.7%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">3,080,197</td>
<td align="right">12,034,698</td>
<td align="right">290.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,498,942</td>
<td align="right">5,800,733</td>
<td align="right">287.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">20,900,465</td>
<td align="right">77,846,821</td>
<td align="right">272.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">127,302</td>
<td align="right">434,592</td>
<td align="right">241.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">424,789</td>
<td align="right">1,397,383</td>
<td align="right">229.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">31,458</td>
<td align="right">92,463</td>
<td align="right">193.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">3,909,296</td>
<td align="right">11,104,694</td>
<td align="right">184.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">31,458</td>
<td align="right">80,661</td>
<td align="right">156.4%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">2,760,821</td>
<td align="right">6,785,862</td>
<td align="right">145.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,468,819</td>
<td align="right">19,994,985</td>
<td align="right">136.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">16,233</td>
<td align="right">35,532</td>
<td align="right">118.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">3,960,082</td>
<td align="right">8,649,102</td>
<td align="right">118.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">116,382</td>
<td align="right">147</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,232,517</td>
<td align="right">12,353,158</td>
<td align="right">98.2%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">116,382</td>
<td align="right">8,883</td>
<td align="right">-92.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">3,443,732</td>
<td align="right">6,358,233</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">12,654,783</td>
<td align="right">21,156,773</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,912,559</td>
<td align="right">6,467,784</td>
<td align="right">65.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">58,191</td>
<td align="right">85,827</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,931,582</td>
<td align="right">2,914,777</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">116,382</td>
<td align="right">152,502</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">367,574</td>
<td align="right">258,417</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">116,382</td>
<td align="right">149,310</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">116,382</td>
<td align="right">149,310</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">498,623</td>
<td align="right">362,417</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">498,623</td>
<td align="right">362,417</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">374,794</td>
<td align="right">293,482</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">173,733</td>
<td align="right">148,050</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">348,074</td>
<td align="right">341,249</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">353,534</td>
<td align="right">357,965</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">11,410,121</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">5,452,736</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,953,902</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,965,670</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,408,495</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,332,349</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">183,299</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">62,391</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_NOP</td>
<td align="right"></td>
<td align="right">158,191,168</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right"></td>
<td align="right">33,219,316</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right"></td>
<td align="right">23,192,251</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">10,398,469</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right"></td>
<td align="right">9,062,174</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right"></td>
<td align="right">7,741,196</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right"></td>
<td align="right">7,650,221</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right"></td>
<td align="right">5,994,564</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">3,454,722</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right"></td>
<td align="right">3,311,713</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">2,429,824</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right"></td>
<td align="right">2,429,822</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">2,276,158</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right"></td>
<td align="right">1,986,932</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">422,281</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">337,911</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">186,270</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right"></td>
<td align="right">120,772</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right"></td>
<td align="right">30,807</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">23,604</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">21,315</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right"></td>
<td align="right">15,405</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right"></td>
<td align="right">15,405</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">11,571</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">8,904</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right"></td>
<td align="right">6,846</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">5,796</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right"></td>
<td align="right">5,691</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">4,452</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right"></td>
<td align="right">1,092</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right"></td>
<td align="right">1,092</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">147</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right"></td>
<td align="right">147</td>
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
Stats gathered on: 2025-02-12
