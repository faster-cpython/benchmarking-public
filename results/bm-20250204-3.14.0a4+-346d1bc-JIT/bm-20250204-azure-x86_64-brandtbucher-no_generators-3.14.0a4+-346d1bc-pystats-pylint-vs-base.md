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
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">2,214,289</td>
<td align="right">3,690,421</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">116,764</td>
<td align="right">161,607</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">132,011</td>
<td align="right">85,231</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">349,187</td>
<td align="right">235,361</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">85,137</td>
<td align="right">69,997</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">648,506</td>
<td align="right">534,680</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">11,738,343</td>
<td align="right">10,161,874</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">11,503,711</td>
<td align="right">12,715,242</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,063,812</td>
<td align="right">968,402</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">6,934,204</td>
<td align="right">6,317,091</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">2,467,121</td>
<td align="right">2,302,650</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">9,690,577</td>
<td align="right">9,086,482</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">52,901,490</td>
<td align="right">55,787,138</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">2,158,824</td>
<td align="right">2,042,870</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">33,679,330</td>
<td align="right">35,269,696</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,069,779</td>
<td align="right">2,000,822</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,153,021</td>
<td align="right">1,116,571</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">4,899,884</td>
<td align="right">4,751,543</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">2,924,051</td>
<td align="right">2,838,057</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,065,950</td>
<td align="right">1,035,670</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">5,842,538</td>
<td align="right">5,678,759</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,490,105</td>
<td align="right">2,420,750</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">2,466,308</td>
<td align="right">2,398,579</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">18,247,391</td>
<td align="right">18,722,025</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,053,052</td>
<td align="right">8,259,118</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,086,251</td>
<td align="right">3,991,393</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">16,604,305</td>
<td align="right">16,234,881</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,980,087</td>
<td align="right">1,939,287</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">26,136,149</td>
<td align="right">25,640,980</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">2,027,548</td>
<td align="right">1,993,228</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,780,534</td>
<td align="right">2,733,574</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">5,532,768</td>
<td align="right">5,446,776</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,578,998</td>
<td align="right">3,529,392</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">14,661,251</td>
<td align="right">14,480,676</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">46,047,154</td>
<td align="right">46,607,189</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,486,535</td>
<td align="right">10,363,212</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,529,381</td>
<td align="right">3,492,724</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">31,234,297</td>
<td align="right">30,910,618</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">29,564,352</td>
<td align="right">29,266,939</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">24,697,248</td>
<td align="right">24,936,352</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">29,188,293</td>
<td align="right">28,916,353</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,084,119</td>
<td align="right">1,074,220</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,958,342</td>
<td align="right">1,943,762</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">15,371,495</td>
<td align="right">15,272,175</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,862,113</td>
<td align="right">8,810,319</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">7,608,531</td>
<td align="right">7,567,737</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,996,110</td>
<td align="right">1,986,270</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">42,598,004</td>
<td align="right">42,392,217</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,932,624</td>
<td align="right">2,922,725</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">14,638,549</td>
<td align="right">14,596,654</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">8,915,454</td>
<td align="right">8,900,874</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">3,988,984</td>
<td align="right">3,982,768</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">3,527,583</td>
<td align="right">3,522,737</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">26,637,639</td>
<td align="right">26,667,521</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">4,531,465</td>
<td align="right">4,526,619</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,521,237</td>
<td align="right">4,516,582</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">10,131,226</td>
<td align="right">10,121,326</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">1,987,464</td>
<td align="right">1,985,775</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">42,580,338</td>
<td align="right">42,612,595</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">25,247,008</td>
<td align="right">25,230,840</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">13,927,476</td>
<td align="right">13,934,604</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">6,702,299</td>
<td align="right">6,699,124</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">6,790,309</td>
<td align="right">6,793,327</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">173,214,568</td>
<td align="right">173,150,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">9,311,975</td>
<td align="right">9,310,289</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">50,226</td>
<td align="right">50,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">46,461,665</td>
<td align="right">46,459,247</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,687,306</td>
<td align="right">3,687,266</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,562,416</td>
<td align="right">1,562,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">961,462</td>
<td align="right">961,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,613,785</td>
<td align="right">2,613,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">11,351,554</td>
<td align="right">11,351,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">11,710,999</td>
<td align="right">11,710,999</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">11,224,785</td>
<td align="right">11,224,785</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">10,022,771</td>
<td align="right">10,022,771</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,153,383</td>
<td align="right">8,153,383</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">8,099,048</td>
<td align="right">8,099,048</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">6,938,577</td>
<td align="right">6,938,577</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,494,808</td>
<td align="right">6,494,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,393,176</td>
<td align="right">6,393,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">5,643,820</td>
<td align="right">5,643,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">5,334,162</td>
<td align="right">5,334,162</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">4,699,693</td>
<td align="right">4,699,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">4,671,914</td>
<td align="right">4,671,914</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">4,327,418</td>
<td align="right">4,327,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">4,122,688</td>
<td align="right">4,122,688</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">3,780,176</td>
<td align="right">3,780,176</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,858,344</td>
<td align="right">2,858,344</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">2,664,635</td>
<td align="right">2,664,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">2,574,594</td>
<td align="right">2,574,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,946,594</td>
<td align="right">1,946,594</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,806,103</td>
<td align="right">1,806,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,800,326</td>
<td align="right">1,800,326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">1,746,788</td>
<td align="right">1,746,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,685,979</td>
<td align="right">1,685,979</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,640,833</td>
<td align="right">1,640,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,623,485</td>
<td align="right">1,623,485</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,548,305</td>
<td align="right">1,548,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,501,273</td>
<td align="right">1,501,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,424,474</td>
<td align="right">1,424,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,392,401</td>
<td align="right">1,392,401</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,149,161</td>
<td align="right">1,149,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,047,297</td>
<td align="right">1,047,297</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,000,580</td>
<td align="right">1,000,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">974,187</td>
<td align="right">974,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">918,636</td>
<td align="right">918,636</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">849,921</td>
<td align="right">849,921</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">823,880</td>
<td align="right">823,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">822,996</td>
<td align="right">822,996</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">820,983</td>
<td align="right">820,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">711,420</td>
<td align="right">711,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">703,476</td>
<td align="right">703,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">690,372</td>
<td align="right">690,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">667,288</td>
<td align="right">667,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">663,194</td>
<td align="right">663,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">657,605</td>
<td align="right">657,605</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">615,409</td>
<td align="right">615,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">615,409</td>
<td align="right">615,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">576,406</td>
<td align="right">576,406</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">555,770</td>
<td align="right">555,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">514,944</td>
<td align="right">514,944</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">446,278</td>
<td align="right">446,278</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">445,980</td>
<td align="right">445,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">438,760</td>
<td align="right">438,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">353,660</td>
<td align="right">353,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">307,447</td>
<td align="right">307,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">296,892</td>
<td align="right">296,892</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">281,347</td>
<td align="right">281,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">280,928</td>
<td align="right">280,928</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">258,715</td>
<td align="right">258,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">255,967</td>
<td align="right">255,967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">231,964</td>
<td align="right">231,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">165,658</td>
<td align="right">165,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">165,618</td>
<td align="right">165,618</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">163,573</td>
<td align="right">163,573</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">163,159</td>
<td align="right">163,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">137,188</td>
<td align="right">137,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">122,576</td>
<td align="right">122,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">108,790</td>
<td align="right">108,790</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,238</td>
<td align="right">98,238</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">84,775</td>
<td align="right">84,775</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">84,392</td>
<td align="right">84,392</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">82,705</td>
<td align="right">82,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,255</td>
<td align="right">76,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">64,045</td>
<td align="right">64,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">56,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">55,559</td>
<td align="right">55,559</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">43,011</td>
<td align="right">43,011</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">42,343</td>
<td align="right">42,343</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">31,532</td>
<td align="right">31,532</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">27,323</td>
<td align="right">27,323</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">23,459</td>
<td align="right">23,459</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">23,353</td>
<td align="right">23,353</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">19,679</td>
<td align="right">19,679</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">18,968</td>
<td align="right">18,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">17,957</td>
<td align="right">17,957</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">10,991</td>
<td align="right">10,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,664</td>
<td align="right">5,664</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">5,557</td>
<td align="right">5,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,036</td>
<td align="right">3,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,949</td>
<td align="right">2,949</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,426</td>
<td align="right">2,426</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1,305</td>
<td align="right">1,305</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,132</td>
<td align="right">1,132</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">1,081</td>
<td align="right">1,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">967</td>
<td align="right">967</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">953</td>
<td align="right">953</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">893</td>
<td align="right">893</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">777</td>
<td align="right">777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">723</td>
<td align="right">723</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">589</td>
<td align="right">589</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">226</td>
<td align="right">226</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">214</td>
<td align="right">214</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">192</td>
<td align="right">192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">126</td>
<td align="right">126</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">34</td>
<td align="right">34</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">25</td>
<td align="right">25</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">18</td>
<td align="right">18</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">15</td>
<td align="right">15</td>
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
<td align="right">708,836</td>
<td align="right">10.4%</td>
<td align="right">708,836</td>
<td align="right">10.4%</td>
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
<td align="right">6,089,717</td>
<td align="right">89.5%</td>
<td align="right">6,089,717</td>
<td align="right">89.5%</td>
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
<td align="right">25</td>
<td align="right">0.0%</td>
<td align="right">25</td>
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
<td align="right">532</td>
<td align="right">20.6%</td>
<td align="right">532</td>
<td align="right">20.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,052</td>
<td align="right">79.4%</td>
<td align="right">2,052</td>
<td align="right">79.4%</td>
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
<td align="right">998</td>
<td align="right">48.6%</td>
<td align="right">998</td>
<td align="right">48.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">211</td>
<td align="right">10.3%</td>
<td align="right">211</td>
<td align="right">10.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">210</td>
<td align="right">10.2%</td>
<td align="right">210</td>
<td align="right">10.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">160</td>
<td align="right">7.8%</td>
<td align="right">160</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">152</td>
<td align="right">7.4%</td>
<td align="right">152</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">117</td>
<td align="right">5.7%</td>
<td align="right">117</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">3.2%</td>
<td align="right">66</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">51</td>
<td align="right">2.5%</td>
<td align="right">51</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">36</td>
<td align="right">1.8%</td>
<td align="right">36</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">21</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">10</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">8</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">446,278</td>
<td align="right">100.0%</td>
<td align="right">446,278</td>
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
<td align="right">1,951,062</td>
<td align="right">14.3%</td>
<td align="right">1,936,482</td>
<td align="right">14.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,659,940</td>
<td align="right">85.2%</td>
<td align="right">11,659,946</td>
<td align="right">85.3%</td>
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
<td align="right">62,806</td>
<td align="right">0.5%</td>
<td align="right">62,806</td>
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
<td align="right">2,599</td>
<td align="right">30.7%</td>
<td align="right">2,599</td>
<td align="right">30.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">5,854</td>
<td align="right">69.3%</td>
<td align="right">5,854</td>
<td align="right">69.3%</td>
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
<td align="left">out of range</td>
<td align="right">2,690</td>
<td align="right">46.0%</td>
<td align="right">2,690</td>
<td align="right">46.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">845</td>
<td align="right">14.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">782</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">780</td>
<td align="right">13.3%</td>
<td align="right">780</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">690</td>
<td align="right">11.8%</td>
<td align="right">690</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">32</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">21</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">13</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">7,761,189</td>
<td align="right">11.3%</td>
<td align="right">7,728,644</td>
<td align="right">11.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,622,354</td>
<td align="right">11.1%</td>
<td align="right">7,590,424</td>
<td align="right">11.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">60,619,916</td>
<td align="right">88.6%</td>
<td align="right">60,705,166</td>
<td align="right">88.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">8,513</td>
<td align="right">0.0%</td>
<td align="right">8,513</td>
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
<td align="right">166,158</td>
<td align="right">100.0%</td>
<td align="right">165,543</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="left">init not simple</td>
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">62</td>
<td align="right">62 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">21</td>
<td align="right">21 / 0 !!</td>
<td align="right">0.0%</td>
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
<td align="right">562,890</td>
<td align="right">97.8%</td>
<td align="right">562,890</td>
<td align="right">97.8%</td>
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
<td align="right">573,137</td>
<td align="right">99.6%</td>
<td align="right">573,137</td>
<td align="right">99.6%</td>
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
<td align="right">12,673</td>
<td align="right">100.0%</td>
<td align="right">12,673</td>
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
<td align="right">1,061,900</td>
<td align="right">5.8%</td>
<td align="right">1,031,620</td>
<td align="right">5.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">17,224,073</td>
<td align="right">94.2%</td>
<td align="right">17,224,076</td>
<td align="right">94.3%</td>
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
<td align="right">3,372</td>
<td align="right">0.0%</td>
<td align="right">3,372</td>
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
<td align="right">1,535</td>
<td align="right">37.3%</td>
<td align="right">1,535</td>
<td align="right">37.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,582</td>
<td align="right">62.7%</td>
<td align="right">2,582</td>
<td align="right">62.7%</td>
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
<td align="right">1,108</td>
<td align="right">42.9%</td>
<td align="right">1,108</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">679</td>
<td align="right">26.3%</td>
<td align="right">679</td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">243</td>
<td align="right">9.4%</td>
<td align="right">243</td>
<td align="right">9.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">193</td>
<td align="right">7.5%</td>
<td align="right">193</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">153</td>
<td align="right">5.9%</td>
<td align="right">153</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">90</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">51</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">16</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">2,483,158</td>
<td align="right">37.4%</td>
<td align="right">2,413,822</td>
<td align="right">36.8%</td>
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
<td align="right">4,117,918</td>
<td align="right">62.1%</td>
<td align="right">4,117,918</td>
<td align="right">62.7%</td>
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
<td align="right">26,561</td>
<td align="right">0.4%</td>
<td align="right">26,561</td>
<td align="right">0.4%</td>
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
<td align="right">6,231</td>
<td align="right">83.5%</td>
<td align="right">6,212</td>
<td align="right">83.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,227</td>
<td align="right">16.5%</td>
<td align="right">1,227</td>
<td align="right">16.5%</td>
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
<td align="left">list</td>
<td align="right">1,213</td>
<td align="right">19.5%</td>
<td align="right">1,193</td>
<td align="right">19.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,248</td>
<td align="right">52.1%</td>
<td align="right">3,249</td>
<td align="right">52.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,241</td>
<td align="right">19.9%</td>
<td align="right">1,241</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">529</td>
<td align="right">8.5%</td>
<td align="right">529</td>
<td align="right">8.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">23,242,915</td>
<td align="right">84.3%</td>
<td align="right">22,522,866</td>
<td align="right">84.2%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,076,495</td>
<td align="right">14.8%</td>
<td align="right">3,981,657</td>
<td align="right">14.9%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">226,484</td>
<td align="right">0.8%</td>
<td align="right">225,784</td>
<td align="right">0.8%</td>
<td align="right">-0.3%</td>
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
<td align="right">8,624</td>
<td align="right">61.6%</td>
<td align="right">8,604</td>
<td align="right">61.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,382</td>
<td align="right">38.4%</td>
<td align="right">5,382</td>
<td align="right">38.5%</td>
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
<td align="left">enumerate</td>
<td align="right">1,189</td>
<td align="right">13.8%</td>
<td align="right">1,169</td>
<td align="right">13.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,243</td>
<td align="right">49.2%</td>
<td align="right">4,243</td>
<td align="right">49.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,409</td>
<td align="right">16.3%</td>
<td align="right">1,409</td>
<td align="right">16.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">604</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">306</td>
<td align="right">3.5%</td>
<td align="right">306</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">276</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">253</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">140</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">97</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">44</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">42</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">11</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
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
<td align="right">31,636,541</td>
<td align="right">25.3%</td>
<td align="right">32,166,573</td>
<td align="right">25.6%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,546,730</td>
<td align="right">63.6%</td>
<td align="right">79,357,142</td>
<td align="right">63.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13,795,415</td>
<td align="right">11.0%</td>
<td align="right">13,799,526</td>
<td align="right">11.0%</td>
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
<td align="right">207,251</td>
<td align="right">0.2%</td>
<td align="right">207,251</td>
<td align="right">0.2%</td>
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
<td align="right">70,087</td>
<td align="right">10.2%</td>
<td align="right">73,104</td>
<td align="right">10.5%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">614,876</td>
<td align="right">89.8%</td>
<td align="right">624,783</td>
<td align="right">89.5%</td>
<td align="right">1.6%</td>
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
<td align="right">3,888</td>
<td align="right">5.5%</td>
<td align="right">3,888</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">3,652</td>
<td align="right">5.2%</td>
<td align="right">3,652</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,533</td>
<td align="right">2.2%</td>
<td align="right">1,533</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,279</td>
<td align="right">1.8%</td>
<td align="right">1,279</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">989</td>
<td align="right">1.4%</td>
<td align="right">989</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">836</td>
<td align="right">1.2%</td>
<td align="right">836</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">392</td>
<td align="right">0.6%</td>
<td align="right">392</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.3%</td>
<td align="right">235</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">204</td>
<td align="right">0.3%</td>
<td align="right">204</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">127</td>
<td align="right">0.2%</td>
<td align="right">127</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">102</td>
<td align="right">0.1%</td>
<td align="right">102</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">55,690,763</td>
<td align="right">99.9%</td>
<td align="right">54,898,181</td>
<td align="right">99.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,292</td>
<td align="right">0.0%</td>
<td align="right">5,292</td>
<td align="right">0.0%</td>
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
<td align="right">508</td>
<td align="right">0.0%</td>
<td align="right">508</td>
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
<td align="right">9,738</td>
<td align="right">0.0%</td>
<td align="right">9,738</td>
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
<td align="right">18,196</td>
<td align="right">100.0%</td>
<td align="right">18,196</td>
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

### LOAD_SUPER_ATTR

<details>
<summary> specialization stats for LOAD_SUPER_ATTR family </summary>

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
<td align="right">138</td>
<td align="right">0.0%</td>
<td align="right">138</td>
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
<td align="right">721,388</td>
<td align="right">99.9%</td>
<td align="right">721,388</td>
<td align="right">99.9%</td>
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
<td align="right">451</td>
<td align="right">100.0%</td>
<td align="right">451</td>
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
<td align="right">6,491,864</td>
<td align="right">54.9%</td>
<td align="right">6,491,864</td>
<td align="right">54.9%</td>
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
<td align="right">5,334,162</td>
<td align="right">45.1%</td>
<td align="right">5,334,162</td>
<td align="right">45.1%</td>
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
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">103</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,841</td>
<td align="right">96.5%</td>
<td align="right">2,841</td>
<td align="right">96.5%</td>
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
<td align="left">list</td>
<td align="right">2,058</td>
<td align="right">72.4%</td>
<td align="right">2,058</td>
<td align="right">72.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">25.8%</td>
<td align="right">732</td>
<td align="right">25.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">51</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
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
<td align="right">1,384,783</td>
<td align="right">9.9%</td>
<td align="right">1,384,783</td>
<td align="right">9.9%</td>
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
<td align="right">10,795,586</td>
<td align="right">77.1%</td>
<td align="right">10,795,586</td>
<td align="right">77.1%</td>
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
<td align="right">1,805,779</td>
<td align="right">12.9%</td>
<td align="right">1,805,779</td>
<td align="right">12.9%</td>
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
<td align="right">38,378</td>
<td align="right">92.2%</td>
<td align="right">38,378</td>
<td align="right">92.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,246</td>
<td align="right">7.8%</td>
<td align="right">3,246</td>
<td align="right">7.8%</td>
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
<td align="right">55,450</td>
<td align="right">1,708.3%</td>
<td align="right">58,467</td>
<td align="right">1,801.2%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">1,397</td>
<td align="right">43.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">606</td>
<td align="right">18.7%</td>
<td align="right">606</td>
<td align="right">18.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">440</td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">283</td>
<td align="right">8.7%</td>
<td align="right">283</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">230</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">105</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">50</td>
<td align="right">1.5%</td>
<td align="right">50</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">39</td>
<td align="right">1.2%</td>
<td align="right">39</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">8</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>

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
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">25</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
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
<td align="right">84,002</td>
<td align="right">3.1%</td>
<td align="right">84,002</td>
<td align="right">3.1%</td>
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
<td align="right">2,588,341</td>
<td align="right">96.8%</td>
<td align="right">2,588,341</td>
<td align="right">96.8%</td>
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
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">343</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430</td>
<td align="right">55.6%</td>
<td align="right">430</td>
<td align="right">55.6%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">240</td>
<td align="right">55.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">92</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">47</td>
<td align="right">10.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">25</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">18</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">8</td>
<td align="right">1.9%</td>
<td align="right">8</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
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
<td align="right">38,822,744</td>
<td align="right">91.5%</td>
<td align="right">38,810,513</td>
<td align="right">91.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">560,620</td>
<td align="right">1.3%</td>
<td align="right">560,620</td>
<td align="right">1.3%</td>
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
<td align="right">3,033,503</td>
<td align="right">7.1%</td>
<td align="right">3,033,503</td>
<td align="right">7.2%</td>
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
<td align="right">64,253</td>
<td align="right">88.5%</td>
<td align="right">64,253</td>
<td align="right">88.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">8,389</td>
<td align="right">11.5%</td>
<td align="right">8,389</td>
<td align="right">11.5%</td>
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
<td align="right">5,854</td>
<td align="right">69.8%</td>
<td align="right">5,854</td>
<td align="right">69.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">764</td>
<td align="right">9.1%</td>
<td align="right">764</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">665</td>
<td align="right">7.9%</td>
<td align="right">665</td>
<td align="right">7.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">564</td>
<td align="right">6.7%</td>
<td align="right">564</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">325</td>
<td align="right">3.9%</td>
<td align="right">325</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">146</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">50</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">21</td>
<td align="right">0.3%</td>
<td align="right">21</td>
<td align="right">0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,976,712</td>
<td align="right">90.4%</td>
<td align="right">7,975,026</td>
<td align="right">90.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">848,870</td>
<td align="right">9.6%</td>
<td align="right">848,870</td>
<td align="right">9.6%</td>
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
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">805</td>
<td align="right">76.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">246</td>
<td align="right">23.4%</td>
<td align="right">246</td>
<td align="right">23.4%</td>
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
<td align="left">sequence</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">222</td>
<td align="right">90.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">24</td>
<td align="right">9.8%</td>
<td align="right">24</td>
<td align="right">9.8%</td>
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
<td align="right">45,139,949</td>
<td align="right">4.1%</td>
<td align="right">45,636,553</td>
<td align="right">4.2%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">34,137,849</td>
<td align="right">3.1%</td>
<td align="right">33,935,904</td>
<td align="right">3.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">586,544,609</td>
<td align="right">53.7%</td>
<td align="right">588,858,464</td>
<td align="right">53.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">425,759,186</td>
<td align="right">39.0%</td>
<td align="right">424,708,975</td>
<td align="right">38.9%</td>
<td align="right">-0.2%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">1,061,900</td>
<td align="right">2.5%</td>
<td align="right">1,031,620</td>
<td align="right">2.5%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">2,483,158</td>
<td align="right">5.9%</td>
<td align="right">2,413,822</td>
<td align="right">5.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">4,076,495</td>
<td align="right">9.7%</td>
<td align="right">3,981,657</td>
<td align="right">9.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,951,062</td>
<td align="right">4.6%</td>
<td align="right">1,936,482</td>
<td align="right">4.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">7,622,354</td>
<td align="right">18.1%</td>
<td align="right">7,590,424</td>
<td align="right">18.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">13,795,415</td>
<td align="right">32.8%</td>
<td align="right">13,799,526</td>
<td align="right">33.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">6,491,864</td>
<td align="right">15.4%</td>
<td align="right">6,491,864</td>
<td align="right">15.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,384,783</td>
<td align="right">3.3%</td>
<td align="right">1,384,783</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">848,870</td>
<td align="right">2.0%</td>
<td align="right">848,870</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">708,836</td>
<td align="right">1.7%</td>
<td align="right">708,836</td>
<td align="right">1.7%</td>
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
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">6,127,904</td>
<td align="right">13.6%</td>
<td align="right">6,545,162</td>
<td align="right">14.3%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,217,684</td>
<td align="right">2.7%</td>
<td align="right">1,153,554</td>
<td align="right">2.5%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">5,260,412</td>
<td align="right">11.7%</td>
<td align="right">5,379,872</td>
<td align="right">11.8%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">5,741,771</td>
<td align="right">12.7%</td>
<td align="right">5,776,536</td>
<td align="right">12.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,117,333</td>
<td align="right">35.7%</td>
<td align="right">16,110,383</td>
<td align="right">35.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,140,557</td>
<td align="right">7.0%</td>
<td align="right">3,140,557</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,621,065</td>
<td align="right">5.8%</td>
<td align="right">2,621,065</td>
<td align="right">5.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,805,696</td>
<td align="right">4.0%</td>
<td align="right">1,805,696</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">924,727</td>
<td align="right">2.0%</td>
<td align="right">924,727</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">532,453</td>
<td align="right">1.2%</td>
<td align="right">532,453</td>
<td align="right">1.2%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,100,279</td>
<td align="right">1.6%</td>
<td align="right">873,611</td>
<td align="right">1.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">5,364,499</td>
<td align="right">7.7%</td>
<td align="right">5,250,673</td>
<td align="right">7.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">11,687,480</td>
<td align="right">16.9%</td>
<td align="right">11,573,657</td>
<td align="right">16.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">11,687,480</td>
<td align="right">16.9%</td>
<td align="right">11,573,657</td>
<td align="right">16.7%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">388,597</td>
<td align="right">0.6%</td>
<td align="right">388,600</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">6,321,876</td>
<td align="right">9.1%</td>
<td align="right">6,321,879</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">6,322,981</td>
<td align="right">9.1%</td>
<td align="right">6,322,984</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">48,094,067</td>
<td align="right">69.4%</td>
<td align="right">48,094,073</td>
<td align="right">69.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">57,620,639</td>
<td align="right">83.1%</td>
<td align="right">57,620,642</td>
<td align="right">83.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">212</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">893</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">453,539</td>
<td align="right">0.7%</td>
<td align="right">453,539</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,162,143</td>
<td align="right">1.7%</td>
<td align="right">1,162,143</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">24</td>
<td align="right">0.0%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">260,925</td>
<td align="right"></td>
<td align="right">280,606</td>
<td align="right"></td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">47,259,719</td>
<td align="right"></td>
<td align="right">46,801,139</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">48,307,951</td>
<td align="right">50.6%</td>
<td align="right">47,851,491</td>
<td align="right">50.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">48,660,683</td>
<td align="right">50.9%</td>
<td align="right">48,204,057</td>
<td align="right">50.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">325,156,444</td>
<td align="right">26.7%</td>
<td align="right">322,154,099</td>
<td align="right">26.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">1,849,487</td>
<td align="right"></td>
<td align="right">1,860,572</td>
<td align="right"></td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">120,496,178</td>
<td align="right">11.1%</td>
<td align="right">119,828,476</td>
<td align="right">11.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">178,490,486</td>
<td align="right">14.7%</td>
<td align="right">179,477,000</td>
<td align="right">14.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">1,590,454</td>
<td align="right"></td>
<td align="right">1,582,101</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">352,298,604</td>
<td align="right">32.6%</td>
<td align="right">350,648,389</td>
<td align="right">32.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">423,313,682</td>
<td align="right">39.1%</td>
<td align="right">422,221,106</td>
<td align="right">39.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">54,493,923</td>
<td align="right"></td>
<td align="right">54,602,423</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">185,715,958</td>
<td align="right">17.2%</td>
<td align="right">185,563,261</td>
<td align="right">17.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">182,807,931</td>
<td align="right">15.0%</td>
<td align="right">182,683,390</td>
<td align="right">15.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">29,027,940</td>
<td align="right"></td>
<td align="right">29,008,599</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">313,941</td>
<td align="right">0.3%</td>
<td align="right">313,776</td>
<td align="right">0.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">531,671,554</td>
<td align="right">43.6%</td>
<td align="right">531,475,662</td>
<td align="right">43.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">38,791</td>
<td align="right">0.0%</td>
<td align="right">38,790</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">46,855,327</td>
<td align="right">49.1%</td>
<td align="right">46,855,135</td>
<td align="right">49.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">46,880,797</td>
<td align="right"></td>
<td align="right">46,880,605</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,112,082</td>
<td align="right"></td>
<td align="right">1,112,082</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">99,255</td>
<td align="right">8.9%</td>
<td align="right">99,255</td>
<td align="right">8.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">5,007</td>
<td align="right">0.5%</td>
<td align="right">5,007</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
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
<td align="right">1,327</td>
<td align="right">27,060</td>
<td align="right">70,858,810</td>
<td align="right">11,096,896</td>
<td align="right">1,953,979</td>
<td align="right">1,327</td>
<td align="right">27,060</td>
<td align="right">70,854,745</td>
<td align="right">11,096,305</td>
<td align="right">1,953,290</td>
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
<td align="right">85</td>
<td align="right">2.1%</td>
<td align="right">43</td>
<td align="right">1.4%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">2,845</td>
<td align="right">71.1%</td>
<td align="right">2,193</td>
<td align="right">69.0%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">4,001</td>
<td align="right"></td>
<td align="right">3,176</td>
<td align="right"></td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">1,156</td>
<td align="right">28.9%</td>
<td align="right">983</td>
<td align="right">31.0%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">28,825,396</td>
<td align="right"></td>
<td align="right">25,511,068</td>
<td align="right"></td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,035</td>
<td align="right">25.9%</td>
<td align="right">1,008</td>
<td align="right">31.7%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">409,208,731</td>
<td align="right">1,419.6%</td>
<td align="right">407,135,079</td>
<td align="right">1,595.9%</td>
<td align="right">-0.5%</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
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
<td align="right">2,762</td>
<td align="right">97.1%</td>
<td align="right">2,110</td>
<td align="right">96.2%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">2,845</td>
<td align="right"></td>
<td align="right">2,193</td>
<td align="right"></td>
<td align="right">-22.9%</td>
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
<td align="right">30,101,504</td>
<td align="right">116.9%</td>
<td align="right">22,900,736</td>
<td align="right">100.9%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">5,820,801</td>
<td align="right">22.6%</td>
<td align="right">4,460,709</td>
<td align="right">19.7%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">25,747,456</td>
<td align="right"></td>
<td align="right">22,695,936</td>
<td align="right"></td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">2,872,064</td>
<td align="right">11.2%</td>
<td align="right">2,602,400</td>
<td align="right">11.5%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">17,054,591</td>
<td align="right">66.2%</td>
<td align="right">15,632,827</td>
<td align="right">68.9%</td>
<td align="right">-8.3%</td>
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
<td align="left">962</td>
<td align="right">34.8%</td>
<td align="left">373</td>
<td align="right">17.7%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">845</td>
<td align="right">30.6%</td>
<td align="left">804</td>
<td align="right">38.1%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">806</td>
<td align="right">29.2%</td>
<td align="left">786</td>
<td align="right">37.3%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">148</td>
<td align="right">5.4%</td>
<td align="left">147</td>
<td align="right">7.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1</td>
<td align="right">0.0%</td>
<td align="left"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">282</td>
<td align="right">9.9%</td>
<td align="right">68</td>
<td align="right">3.1%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">615</td>
<td align="right">21.6%</td>
<td align="right">283</td>
<td align="right">12.9%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">756</td>
<td align="right">26.6%</td>
<td align="right">713</td>
<td align="right">32.5%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">873</td>
<td align="right">30.7%</td>
<td align="right">832</td>
<td align="right">37.9%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">192</td>
<td align="right">6.7%</td>
<td align="right">191</td>
<td align="right">8.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">107</td>
<td align="right">3.8%</td>
<td align="right">106</td>
<td align="right">4.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">20</td>
<td align="right">0.7%</td>
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
<td align="right">256</td>
<td align="right">9.0%</td>
<td align="right">63</td>
<td align="right">2.9%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">550</td>
<td align="right">19.3%</td>
<td align="right">257</td>
<td align="right">11.7%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">224</td>
<td align="right">7.9%</td>
<td align="right">122</td>
<td align="right">5.6%</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">928</td>
<td align="right">32.6%</td>
<td align="right">907</td>
<td align="right">41.4%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">675</td>
<td align="right">23.7%</td>
<td align="right">634</td>
<td align="right">28.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">129</td>
<td align="right">4.5%</td>
<td align="right">127</td>
<td align="right">5.8%</td>
<td align="right">-1.6%</td>
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
<td align="left">_DELETE_SUBSCR</td>
<td align="right">333</td>
<td align="right">15,473</td>
<td align="right">4,546.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">2,744</td>
<td align="right">33,024</td>
<td align="right">1,103.5%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">28,513</td>
<td align="right">64,963</td>
<td align="right">127.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">4,858</td>
<td align="right">10,678</td>
<td align="right">119.8%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,351,202</td>
<td align="right">1,449,074</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,599,775</td>
<td align="right">1,132,752</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">85,557</td>
<td align="right">132,337</td>
<td align="right">54.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">95,453</td>
<td align="right">142,413</td>
<td align="right">49.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">90,314</td>
<td align="right">124,634</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">26,007</td>
<td align="right">35,847</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">11,733</td>
<td align="right">15,288</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">570,724</td>
<td align="right">735,198</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,656,490</td>
<td align="right">1,210,111</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">1,032,112</td>
<td align="right">783,363</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">468,856</td>
<td align="right">567,250</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">410,256</td>
<td align="right">496,251</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">12,918,305</td>
<td align="right">10,331,715</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">949,172</td>
<td align="right">761,730</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">2,224,172</td>
<td align="right">1,786,895</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">3,091,379</td>
<td align="right">3,690,093</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">264,992</td>
<td align="right">214,618</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">217,798</td>
<td align="right">258,598</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">662,062</td>
<td align="right">778,016</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">492,916</td>
<td align="right">578,910</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">1,045,818</td>
<td align="right">1,226,396</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">23,412,366</td>
<td align="right">19,462,548</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">687,955</td>
<td align="right">803,909</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">698,996</td>
<td align="right">584,507</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">4,269,710</td>
<td align="right">4,949,009</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">319,725</td>
<td align="right">369,331</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,764,977</td>
<td align="right">4,343,545</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,474,134</td>
<td align="right">2,839,183</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,093,864</td>
<td align="right">3,529,293</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">4,427,600</td>
<td align="right">5,044,013</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">641,512</td>
<td align="right">553,095</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,221,450</td>
<td align="right">1,385,146</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">5,148,038</td>
<td align="right">5,833,902</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">5,405,704</td>
<td align="right">6,108,032</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">398,757</td>
<td align="right">450,557</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">1,198,100</td>
<td align="right">1,344,322</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">28,825,396</td>
<td align="right">25,511,068</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,440,731</td>
<td align="right">1,605,565</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">1,314,885</td>
<td align="right">1,166,593</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,374,037</td>
<td align="right">1,526,086</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">1,926,395</td>
<td align="right">2,135,824</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,010,093</td>
<td align="right">3,310,337</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">6,318,041</td>
<td align="right">6,923,750</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">6,312,642</td>
<td align="right">6,915,751</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">105,318</td>
<td align="right">115,217</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,277,279</td>
<td align="right">2,488,665</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">3,641,040</td>
<td align="right">3,309,614</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">20,143,105</td>
<td align="right">21,920,907</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">978,625</td>
<td align="right">1,064,540</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">480,801</td>
<td align="right">522,696</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">33,095,106</td>
<td align="right">30,460,077</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">125,982</td>
<td align="right">135,881</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">919,602</td>
<td align="right">987,249</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">5,479,136</td>
<td align="right">5,841,254</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">3,973,762</td>
<td align="right">4,235,160</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">257,646</td>
<td align="right">274,130</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">7,594,378</td>
<td align="right">8,065,890</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,423,384</td>
<td align="right">6,783,820</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,724,282</td>
<td align="right">1,819,120</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">577,216</td>
<td align="right">607,950</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">36,772,075</td>
<td align="right">38,690,795</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">343,937</td>
<td align="right">359,964</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">628,259</td>
<td align="right">657,444</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">359,391</td>
<td align="right">373,971</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">402,278</td>
<td align="right">418,346</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">1,033,645</td>
<td align="right">1,074,439</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">579,144</td>
<td align="right">601,809</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">51,022,810</td>
<td align="right">52,963,939</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">4,861,519</td>
<td align="right">5,025,298</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">614,080</td>
<td align="right">633,016</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">538,436</td>
<td align="right">554,900</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,640,481</td>
<td align="right">1,688,521</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">247,615</td>
<td align="right">254,530</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">11,745,354</td>
<td align="right">12,064,972</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">243,487</td>
<td align="right">249,702</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">283,420</td>
<td align="right">289,636</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">2,080,444</td>
<td align="right">2,125,864</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,264,550</td>
<td align="right">3,334,750</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,709,592</td>
<td align="right">1,746,252</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">4,197,794</td>
<td align="right">4,284,994</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,036,100</td>
<td align="right">1,055,340</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">4,006,639</td>
<td align="right">4,081,033</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">4,274,702</td>
<td align="right">4,349,760</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">1,831,693</td>
<td align="right">1,861,973</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">7,773,084</td>
<td align="right">7,887,322</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">13,849,733</td>
<td align="right">13,694,655</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">251,126</td>
<td align="right">253,550</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">354,230</td>
<td align="right">357,408</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,880,206</td>
<td align="right">2,900,846</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,449,722</td>
<td align="right">1,452,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,337,390</td>
<td align="right">4,340,550</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">57,864</td>
<td align="right">57,905</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">547,261</td>
<td align="right">547,281</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">885,789</td>
<td align="right">885,769</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">227,057</td>
<td align="right">227,055</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">229,766</td>
<td align="right">229,764</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,561,379</td>
<td align="right">2,561,379</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,247,663</td>
<td align="right">2,247,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,207,290</td>
<td align="right">1,207,290</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,184,463</td>
<td align="right">1,184,463</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,041,083</td>
<td align="right">1,041,083</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">975,423</td>
<td align="right">975,423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">651,252</td>
<td align="right">651,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">635,166</td>
<td align="right">635,166</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">592,788</td>
<td align="right">592,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">572,124</td>
<td align="right">572,124</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">374,208</td>
<td align="right">374,208</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">207,135</td>
<td align="right">207,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">206,066</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">191,583</td>
<td align="right">191,583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">168,966</td>
<td align="right">168,966</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">139,325</td>
<td align="right">139,325</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">139,200</td>
<td align="right">139,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">128,793</td>
<td align="right">128,793</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">63,133</td>
<td align="right">63,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">63,042</td>
<td align="right">63,042</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">39,816</td>
<td align="right">39,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">33,075</td>
<td align="right">33,075</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">27,237</td>
<td align="right">27,237</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">19,908</td>
<td align="right">19,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3,018</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">2,709</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">23</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">23</td>
<td align="right">23</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">22</td>
<td align="right">22</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">6</td>
<td align="right">6</td>
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

<table>
<thead>
<tr>
<th align="left">Opcode</th>
<th align="right">Base Count</th>
<th align="right">Head Count</th>
<th align="right">Change</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">CALL</td>
<td align="right">29</td>
<td align="right">113</td>
<td align="right">289.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">529</td>
<td align="right"></td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="right">37</td>
<td align="right">37</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
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
Stats gathered on: 2025-02-04
