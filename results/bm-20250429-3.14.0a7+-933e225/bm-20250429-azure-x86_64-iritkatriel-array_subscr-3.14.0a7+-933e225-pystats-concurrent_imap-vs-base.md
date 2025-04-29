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
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">372,846</td>
<td align="right">470,943</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">5,211,561</td>
<td align="right">6,552,507</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">3,823,308</td>
<td align="right">4,804,314</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">766,704</td>
<td align="right">962,908</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,407,496</td>
<td align="right">1,767,163</td>
<td align="right">25.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">901,759</td>
<td align="right">1,130,692</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,163,991</td>
<td align="right">1,458,198</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">259,309</td>
<td align="right">324,563</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">1,435,742</td>
<td align="right">1,795,409</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">1,320,174</td>
<td align="right">1,646,906</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,190,085</td>
<td align="right">1,484,292</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,336,540</td>
<td align="right">1,663,466</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,473,559</td>
<td align="right">1,833,226</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">267,622</td>
<td align="right">332,876</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">427,394</td>
<td align="right">526,747</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">562,856</td>
<td align="right">693,578</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">282,429</td>
<td align="right">347,899</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">282,749</td>
<td align="right">348,219</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">423,023</td>
<td align="right">520,924</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">143,605</td>
<td align="right">176,807</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">427,387</td>
<td align="right">525,278</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">151,310</td>
<td align="right">183,947</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">455,152</td>
<td align="right">553,255</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">6,293,009</td>
<td align="right">7,600,200</td>
<td align="right">20.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,834,201</td>
<td align="right">8,240,381</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">159,906</td>
<td align="right">192,533</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">162,689</td>
<td align="right">195,104</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,807,935</td>
<td align="right">2,167,921</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,772,625</td>
<td align="right">11,701,015</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">165,829</td>
<td align="right">198,456</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">12,887,677</td>
<td align="right">15,405,639</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,905,485</td>
<td align="right">2,264,844</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">9,477,554</td>
<td align="right">11,210,634</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">12,036,526</td>
<td align="right">14,227,198</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,132,418</td>
<td align="right">7,243,853</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">1,301,755</td>
<td align="right">1,530,688</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,578,091</td>
<td align="right">4,197,839</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,846,116</td>
<td align="right">3,336,771</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">3,806,912</td>
<td align="right">4,461,468</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">1,363,722</td>
<td align="right">1,592,974</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">3,322,420</td>
<td align="right">3,878,179</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">64,151,739</td>
<td align="right">74,712,475</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,973,241</td>
<td align="right">4,626,911</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">2,617,198</td>
<td align="right">3,041,821</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,236,509</td>
<td align="right">1,432,397</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,308,330</td>
<td align="right">2,667,183</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,968,518</td>
<td align="right">3,426,004</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">21,293,882</td>
<td align="right">24,431,587</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,684,735</td>
<td align="right">3,077,523</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">7,308,420</td>
<td align="right">8,354,934</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">710,905</td>
<td align="right">808,833</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">5,378,509</td>
<td align="right">6,097,237</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">13,601,272</td>
<td align="right">15,398,308</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">22,312,270</td>
<td align="right">25,026,127</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">807,706</td>
<td align="right">905,803</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">7,913,764</td>
<td align="right">8,862,454</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">26,310,045</td>
<td align="right">29,447,765</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,114,669</td>
<td align="right">1,245,519</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">851,407</td>
<td align="right">949,519</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">286,719</td>
<td align="right">319,353</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">4,772,304</td>
<td align="right">5,296,084</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,224,080</td>
<td align="right">1,354,826</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">16,975,311</td>
<td align="right">18,741,302</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">17,012,576</td>
<td align="right">18,745,308</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">7,383,827</td>
<td align="right">8,070,020</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">7,035,818</td>
<td align="right">7,689,481</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,438,308</td>
<td align="right">1,569,042</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">3,041,650</td>
<td align="right">3,303,118</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">3,218,304</td>
<td align="right">3,479,874</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">8,575,417</td>
<td align="right">9,262,417</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,512,345</td>
<td align="right">8,068,211</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,696,247</td>
<td align="right">1,794,158</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,143,045</td>
<td align="right">1,208,319</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">649,607</td>
<td align="right">682,023</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">6,798,805</td>
<td align="right">7,093,180</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">13,388,235</td>
<td align="right">13,846,032</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,038,955</td>
<td align="right">1,071,596</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">491</td>
<td align="right">476</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">4,943</td>
<td align="right">5,049</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">3,235,150</td>
<td align="right">3,300,424</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">100</td>
<td align="right">102</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">4,589</td>
<td align="right">4,530</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">1,619</td>
<td align="right">1,602</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">13,341</td>
<td align="right">13,446</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">3,232</td>
<td align="right">3,211</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">17,564</td>
<td align="right">17,669</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">17,564</td>
<td align="right">17,669</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">344</td>
<td align="right">346</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">102,264</td>
<td align="right">102,390</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">97,364</td>
<td align="right">97,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">604,262</td>
<td align="right">604,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">35,126</td>
<td align="right">35,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">516,533</td>
<td align="right">516,635</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">928,801</td>
<td align="right">928,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">34,044</td>
<td align="right">34,045</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">857,670</td>
<td align="right">857,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">191,017</td>
<td align="right">191,018</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,656</td>
<td align="right">940,653</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">5,068,280</td>
<td align="right">5,068,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">4,724,457</td>
<td align="right">4,724,457</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">4,653,742</td>
<td align="right">4,653,742</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,818,699</td>
<td align="right">1,818,699</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">856,262</td>
<td align="right">856,262</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">462,683</td>
<td align="right">462,683</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">426,671</td>
<td align="right">426,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">105,140</td>
<td align="right">105,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">105,110</td>
<td align="right">105,110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">87,313</td>
<td align="right">87,313</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">84,720</td>
<td align="right">84,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">81,670</td>
<td align="right">81,670</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">77,356</td>
<td align="right">77,356</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">72,425</td>
<td align="right">72,425</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">69,638</td>
<td align="right">69,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">67,588</td>
<td align="right">67,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">63,345</td>
<td align="right">63,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">55,863</td>
<td align="right">55,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">55,859</td>
<td align="right">55,859</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">44,010</td>
<td align="right">44,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">42,906</td>
<td align="right">42,906</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">38,452</td>
<td align="right">38,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">38,409</td>
<td align="right">38,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">31,252</td>
<td align="right">31,252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">29,697</td>
<td align="right">29,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">29,557</td>
<td align="right">29,557</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">23,800</td>
<td align="right">23,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">21,908</td>
<td align="right">21,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,465</td>
<td align="right">21,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">20,988</td>
<td align="right">20,988</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">17,809</td>
<td align="right">17,809</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">17,404</td>
<td align="right">17,404</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">14,139</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">12,837</td>
<td align="right">12,837</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">12,672</td>
<td align="right">12,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">10,380</td>
<td align="right">10,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">8,488</td>
<td align="right">8,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">8,446</td>
<td align="right">8,446</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,227</td>
<td align="right">4,227</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">4,223</td>
<td align="right">4,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">784</td>
<td align="right">784</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">491</td>
<td align="right">491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">391</td>
<td align="right">391</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">207</td>
<td align="right">207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">181</td>
<td align="right">181</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">153</td>
<td align="right">153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">149</td>
<td align="right">149</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">128</td>
<td align="right">128</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">68</td>
<td align="right">68</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">38</td>
<td align="right">38</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">27</td>
<td align="right">27</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">15</td>
<td align="right">15</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">12</td>
<td align="right">12</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">4</td>
<td align="right">4</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">3</td>
<td align="right">3</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">1</td>
<td align="right">1</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">1</td>
<td align="right">1</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,156</td>
<td align="right">2.0%</td>
<td align="right">207,126</td>
<td align="right">2.2%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,348,114</td>
<td align="right">91.5%</td>
<td align="right">8,907,023</td>
<td align="right">92.5%</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">515,472</td>
<td align="right">6.4%</td>
<td align="right">515,579</td>
<td align="right">5.4%</td>
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
<td align="right">3,337</td>
<td align="right">80.6%</td>
<td align="right">4,166</td>
<td align="right">83.9%</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">802</td>
<td align="right">19.4%</td>
<td align="right">797</td>
<td align="right">16.1%</td>
<td align="right">-0.6%</td>
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
<td align="left">subscr deque</td>
<td align="right">91</td>
<td align="right">11.3%</td>
<td align="right">88</td>
<td align="right">11.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">291</td>
<td align="right">36.3%</td>
<td align="right">289</td>
<td align="right">36.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">187</td>
<td align="right">23.3%</td>
<td align="right">187</td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">164</td>
<td align="right">20.4%</td>
<td align="right">164</td>
<td align="right">20.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66</td>
<td align="right">8.2%</td>
<td align="right">66</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
<td align="right">0.1%</td>
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
<td align="right">14,139</td>
<td align="right">100.0%</td>
<td align="right">14,139</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,235,872</td>
<td align="right">100.0%</td>
<td align="right">21,243,400</td>
<td align="right">100.0%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,016</td>
<td align="right">0.0%</td>
<td align="right">1,987</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">787</td>
<td align="right">0.0%</td>
<td align="right">787</td>
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
<td align="right">3,360</td>
<td align="right">100.0%</td>
<td align="right">3,330</td>
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
<td align="right">42</td>
<td align="right">23.2%</td>
<td align="right">42</td>
<td align="right">23.2%</td>
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
<td align="right">139</td>
<td align="right">100.0%</td>
<td align="right">139</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">125,873</td>
<td align="right">3.0%</td>
<td align="right">158,585</td>
<td align="right">3.4%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">424,342</td>
<td align="right">10.2%</td>
<td align="right">523,046</td>
<td align="right">11.2%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,597,844</td>
<td align="right">86.7%</td>
<td align="right">3,990,561</td>
<td align="right">85.3%</td>
<td align="right">10.9%</td>
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
<td align="right">2,632</td>
<td align="right">48.6%</td>
<td align="right">3,250</td>
<td align="right">48.7%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">2,780</td>
<td align="right">51.4%</td>
<td align="right">3,427</td>
<td align="right">51.3%</td>
<td align="right">23.3%</td>
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
<td align="left">float long</td>
<td align="right">2,491</td>
<td align="right">89.6%</td>
<td align="right">3,140</td>
<td align="right">91.6%</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">150</td>
<td align="right">5.4%</td>
<td align="right">148</td>
<td align="right">4.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">95</td>
<td align="right">3.4%</td>
<td align="right">95</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">44</td>
<td align="right">1.6%</td>
<td align="right">44</td>
<td align="right">1.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,302,146</td>
<td align="right">100.0%</td>
<td align="right">1,531,079</td>
<td align="right">100.0%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">264</td>
<td align="right">0.0%</td>
<td align="right">264</td>
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
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">8</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">43</td>
<td align="right">84.3%</td>
<td align="right">43</td>
<td align="right">84.3%</td>
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
<td align="right">43</td>
<td align="right">100.0%</td>
<td align="right">43</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,482,765</td>
<td align="right">93.0%</td>
<td align="right">13,266,849</td>
<td align="right">93.4%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">940,117</td>
<td align="right">7.0%</td>
<td align="right">940,117</td>
<td align="right">6.6%</td>
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
<td align="right">51</td>
<td align="right">9.5%</td>
<td align="right">48</td>
<td align="right">9.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">488</td>
<td align="right">90.5%</td>
<td align="right">488</td>
<td align="right">91.0%</td>
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
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">164</td>
<td align="right">33.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">77</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">70</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">7</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">3</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1</td>
<td align="right">0.2%</td>
<td align="right">1</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">6,823,168</td>
<td align="right">17.2%</td>
<td align="right">8,229,062</td>
<td align="right">18.1%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,446,684</td>
<td align="right">81.8%</td>
<td align="right">36,926,016</td>
<td align="right">81.0%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">397,342</td>
<td align="right">1.0%</td>
<td align="right">397,337</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
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
<td align="right">6,497</td>
<td align="right">35.7%</td>
<td align="right">6,827</td>
<td align="right">36.9%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,727</td>
<td align="right">64.3%</td>
<td align="right">11,692</td>
<td align="right">63.1%</td>
<td align="right">-0.3%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">1,423</td>
<td align="right">21.9%</td>
<td align="right">1,614</td>
<td align="right">23.6%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">743</td>
<td align="right">11.4%</td>
<td align="right">779</td>
<td align="right">11.4%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">1,646</td>
<td align="right">25.3%</td>
<td align="right">1,674</td>
<td align="right">24.5%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">683</td>
<td align="right">10.5%</td>
<td align="right">683</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">460</td>
<td align="right">7.1%</td>
<td align="right">460</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">71</td>
<td align="right">1.1%</td>
<td align="right">71</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">68</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">45</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23</td>
<td align="right">0.4%</td>
<td align="right">23</td>
<td align="right">0.3%</td>
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
<td align="right">19,019,857</td>
<td align="right">100.0%</td>
<td align="right">22,649,254</td>
<td align="right">100.0%</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">854</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
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
<td align="right">238</td>
<td align="right">0.0%</td>
<td align="right">238</td>
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
<td align="right">2,384</td>
<td align="right">100.0%</td>
<td align="right">2,377</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,431,296</td>
<td align="right">100.0%</td>
<td align="right">1,790,963</td>
<td align="right">100.0%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">13</td>
<td align="right">0.0%</td>
<td align="right">13</td>
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
<td align="right">55</td>
<td align="right">100.0%</td>
<td align="right">55</td>
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
<td align="right">3,823,244</td>
<td align="right">94.0%</td>
<td align="right">4,476,914</td>
<td align="right">94.9%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">79,939</td>
<td align="right">2.0%</td>
<td align="right">79,939</td>
<td align="right">1.7%</td>
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
<td align="right">160,377</td>
<td align="right">3.9%</td>
<td align="right">160,377</td>
<td align="right">3.4%</td>
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
<td align="right">3,991</td>
<td align="right">84.3%</td>
<td align="right">3,991</td>
<td align="right">84.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">744</td>
<td align="right">15.7%</td>
<td align="right">744</td>
<td align="right">15.7%</td>
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
<td align="right">694</td>
<td align="right">93.3%</td>
<td align="right">740</td>
<td align="right">99.5%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">344</td>
<td align="right">46.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">206</td>
<td align="right">27.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">44</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">11</td>
<td align="right">1.5%</td>
<td align="right">11</td>
<td align="right">1.5%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,363,722</td>
<td align="right">98.5%</td>
<td align="right">1,592,974</td>
<td align="right">98.7%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">21,261</td>
<td align="right">1.5%</td>
<td align="right">21,261</td>
<td align="right">1.3%</td>
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
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">17</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">187</td>
<td align="right">91.7%</td>
<td align="right">187</td>
<td align="right">91.7%</td>
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
<td align="left">py simple</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">119</td>
<td align="right">63.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">36.4%</td>
<td align="right">68</td>
<td align="right">36.4%</td>
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
<td align="right">8,381,000</td>
<td align="right">92.8%</td>
<td align="right">10,177,959</td>
<td align="right">93.7%</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">648,271</td>
<td align="right">7.2%</td>
<td align="right">680,694</td>
<td align="right">6.3%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28</td>
<td align="right">0.0%</td>
<td align="right">28</td>
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
<td align="right">458</td>
<td align="right">34.3%</td>
<td align="right">453</td>
<td align="right">34.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">878</td>
<td align="right">65.7%</td>
<td align="right">876</td>
<td align="right">65.9%</td>
<td align="right">-0.2%</td>
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
<td align="right">151</td>
<td align="right">17.2%</td>
<td align="right">142</td>
<td align="right">16.2%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">318</td>
<td align="right">36.2%</td>
<td align="right">325</td>
<td align="right">37.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">232</td>
<td align="right">26.4%</td>
<td align="right">232</td>
<td align="right">26.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">111</td>
<td align="right">12.6%</td>
<td align="right">111</td>
<td align="right">12.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">44</td>
<td align="right">5.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">22</td>
<td align="right">2.5%</td>
<td align="right">22</td>
<td align="right">2.5%</td>
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
<td align="right">2,000,715</td>
<td align="right">100.0%</td>
<td align="right">2,065,999</td>
<td align="right">100.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">38</td>
<td align="right">0.0%</td>
<td align="right">38</td>
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
<td align="right">111</td>
<td align="right">100.0%</td>
<td align="right">111</td>
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
<td align="right">9,494,199</td>
<td align="right">2.2%</td>
<td align="right">11,032,167</td>
<td align="right">2.3%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">175,961,842</td>
<td align="right">41.3%</td>
<td align="right">200,142,231</td>
<td align="right">41.4%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">239,441,641</td>
<td align="right">56.2%</td>
<td align="right">270,893,158</td>
<td align="right">56.1%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">847,802</td>
<td align="right">0.2%</td>
<td align="right">924,479</td>
<td align="right">0.2%</td>
<td align="right">9.0%</td>
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
<td align="right">424,342</td>
<td align="right">4.5%</td>
<td align="right">523,046</td>
<td align="right">4.8%</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">6,823,168</td>
<td align="right">72.1%</td>
<td align="right">8,229,062</td>
<td align="right">74.8%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">648,271</td>
<td align="right">6.8%</td>
<td align="right">680,694</td>
<td align="right">6.2%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">854</td>
<td align="right">0.0%</td>
<td align="right">840</td>
<td align="right">0.0%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">2,016</td>
<td align="right">0.0%</td>
<td align="right">1,987</td>
<td align="right">0.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">515,472</td>
<td align="right">5.4%</td>
<td align="right">515,579</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">940,117</td>
<td align="right">9.9%</td>
<td align="right">940,117</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">79,939</td>
<td align="right">0.8%</td>
<td align="right">79,939</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">21,261</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
<td align="right">14,139</td>
<td align="right">0.1%</td>
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
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">81,491</td>
<td align="right">9.6%</td>
<td align="right">103,552</td>
<td align="right">11.2%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">81,665</td>
<td align="right">9.6%</td>
<td align="right">103,574</td>
<td align="right">11.2%</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">125,872</td>
<td align="right">14.8%</td>
<td align="right">158,584</td>
<td align="right">17.2%</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">49,698</td>
<td align="right">5.9%</td>
<td align="right">49,700</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">337,600</td>
<td align="right">39.8%</td>
<td align="right">337,593</td>
<td align="right">36.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">160,377</td>
<td align="right">18.9%</td>
<td align="right">160,377</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,895</td>
<td align="right">1.2%</td>
<td align="right">9,895</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">397</td>
<td align="right">0.0%</td>
<td align="right">397</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">275</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">152</td>
<td align="right">0.0%</td>
<td align="right">152</td>
<td align="right">0.0%</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">385,751</td>
<td align="right">1.5%</td>
<td align="right">451,216</td>
<td align="right">1.5%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">21,298,115</td>
<td align="right">80.9%</td>
<td align="right">24,435,820</td>
<td align="right">82.9%</td>
<td align="right">14.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">18,806,670</td>
<td align="right">71.4%</td>
<td align="right">21,388,509</td>
<td align="right">72.6%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">7,089,270</td>
<td align="right">26.9%</td>
<td align="right">7,645,136</td>
<td align="right">25.9%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">7,089,328</td>
<td align="right">26.9%</td>
<td align="right">7,645,194</td>
<td align="right">26.0%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">7,516,703</td>
<td align="right">28.6%</td>
<td align="right">8,072,569</td>
<td align="right">27.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,516,703</td>
<td align="right">28.6%</td>
<td align="right">8,072,569</td>
<td align="right">27.4%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">17,578</td>
<td align="right">0.1%</td>
<td align="right">17,683</td>
<td align="right">0.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">427,375</td>
<td align="right">1.6%</td>
<td align="right">427,375</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">16</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">456,471</td>
<td align="right">1.7%</td>
<td align="right">456,471</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">441,508</td>
<td align="right">1.7%</td>
<td align="right">441,508</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
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
<td align="right">9,309</td>
<td align="right"></td>
<td align="right">53,359</td>
<td align="right"></td>
<td align="right">473.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">56,845</td>
<td align="right"></td>
<td align="right">126,091</td>
<td align="right"></td>
<td align="right">121.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">47,804</td>
<td align="right"></td>
<td align="right">72,969</td>
<td align="right"></td>
<td align="right">52.6%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,173,686</td>
<td align="right"></td>
<td align="right">1,435,154</td>
<td align="right"></td>
<td align="right">22.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">8,312,258</td>
<td align="right"></td>
<td align="right">10,020,035</td>
<td align="right"></td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">42,977,910</td>
<td align="right">19.0%</td>
<td align="right">49,827,614</td>
<td align="right">19.5%</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">40,666,484</td>
<td align="right">20.4%</td>
<td align="right">46,950,122</td>
<td align="right">20.8%</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">50,637,109</td>
<td align="right">25.5%</td>
<td align="right">57,987,591</td>
<td align="right">25.7%</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">20,693,138</td>
<td align="right">64.9%</td>
<td align="right">23,602,743</td>
<td align="right">65.8%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">20,694,792</td>
<td align="right"></td>
<td align="right">23,604,592</td>
<td align="right"></td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">5,538,004</td>
<td align="right">2.8%</td>
<td align="right">6,290,389</td>
<td align="right">2.8%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">8,945,339</td>
<td align="right"></td>
<td align="right">10,143,648</td>
<td align="right"></td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">58,231,231</td>
<td align="right">25.8%</td>
<td align="right">65,822,131</td>
<td align="right">25.7%</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">123,360,811</td>
<td align="right">54.7%</td>
<td align="right">139,205,300</td>
<td align="right">54.4%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">102,112,347</td>
<td align="right">51.3%</td>
<td align="right">114,666,384</td>
<td align="right">50.8%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,113,074</td>
<td align="right">0.5%</td>
<td align="right">1,243,874</td>
<td align="right">0.5%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">12,182,460</td>
<td align="right"></td>
<td align="right">13,457,160</td>
<td align="right"></td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,087,679</td>
<td align="right">34.8%</td>
<td align="right">12,133,795</td>
<td align="right">33.8%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,208,797</td>
<td align="right">35.1%</td>
<td align="right">12,254,919</td>
<td align="right">34.2%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">43,529</td>
<td align="right">0.1%</td>
<td align="right">43,534</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">77,589</td>
<td align="right">0.2%</td>
<td align="right">77,590</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">640</td>
<td align="right">0.1%</td>
<td align="right">640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">1</td>
<td align="right">212</td>
<td align="right">10,306</td>
<td align="right">758</td>
<td align="right">711</td>
<td align="right">1</td>
<td align="right">212</td>
<td align="right">10,306</td>
<td align="right">758</td>
<td align="right">711</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-29
