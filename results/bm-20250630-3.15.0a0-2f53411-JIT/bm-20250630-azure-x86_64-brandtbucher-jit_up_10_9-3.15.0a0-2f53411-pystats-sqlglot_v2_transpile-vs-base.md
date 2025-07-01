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
<td align="left">BINARY_OP</td>
<td align="right">89,306</td>
<td align="right">25,214</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">2,119,304</td>
<td align="right">1,121,085</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">118,902</td>
<td align="right">64,957</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">75,718</td>
<td align="right">46,026</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">69,598</td>
<td align="right">43,485</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,963,794</td>
<td align="right">1,245,994</td>
<td align="right">-36.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,432,620</td>
<td align="right">1,561,509</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">311,144</td>
<td align="right">205,518</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">564,615</td>
<td align="right">379,116</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,102,784</td>
<td align="right">2,175,582</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">624,256</td>
<td align="right">447,562</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">538,403</td>
<td align="right">387,875</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,855,203</td>
<td align="right">1,339,857</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">1,409,876</td>
<td align="right">1,031,596</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">1,453,031</td>
<td align="right">1,074,751</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,774,469</td>
<td align="right">2,056,669</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,839,805</td>
<td align="right">2,122,005</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,439,319</td>
<td align="right">1,830,985</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">458,596</td>
<td align="right">345,623</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">661,317</td>
<td align="right">499,653</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">2,397,966</td>
<td align="right">1,827,126</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,430,957</td>
<td align="right">1,764,076</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">1,592,734</td>
<td align="right">1,227,166</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">9,115,198</td>
<td align="right">7,113,182</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,215,822</td>
<td align="right">949,167</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,666,503</td>
<td align="right">1,307,603</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,557,014</td>
<td align="right">2,026,827</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">763,599</td>
<td align="right">621,019</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">308,097</td>
<td align="right">252,006</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,687,505</td>
<td align="right">3,020,977</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">33,033,958</td>
<td align="right">27,698,985</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">4,509,111</td>
<td align="right">3,787,498</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">418,921</td>
<td align="right">354,871</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,572,206</td>
<td align="right">1,342,498</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">2,531,613</td>
<td align="right">2,167,931</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,040,876</td>
<td align="right">7,769,203</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">3,175,587</td>
<td align="right">2,739,371</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">75,142,359</td>
<td align="right">64,981,193</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">19,279,252</td>
<td align="right">17,302,729</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">6,203,253</td>
<td align="right">5,573,815</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">12,991,828</td>
<td align="right">11,812,254</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,404,263</td>
<td align="right">3,103,063</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">10,215,505</td>
<td align="right">9,379,837</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">6,752,412</td>
<td align="right">6,292,220</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">2,376,445</td>
<td align="right">2,232,601</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,336,094</td>
<td align="right">1,260,091</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,460,672</td>
<td align="right">2,324,301</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">6,760,024</td>
<td align="right">6,389,307</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,039,746</td>
<td align="right">3,844,194</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,429,941</td>
<td align="right">1,361,285</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">11,724,878</td>
<td align="right">11,245,837</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">15,798,970</td>
<td align="right">15,199,349</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">16,019,711</td>
<td align="right">15,439,280</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">409,468</td>
<td align="right">394,816</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">7,035,665</td>
<td align="right">6,819,783</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">4,763,056</td>
<td align="right">4,632,523</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">91,989</td>
<td align="right">89,598</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">9,170,897</td>
<td align="right">8,934,958</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">5,212,350</td>
<td align="right">5,082,941</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,189,792</td>
<td align="right">1,171,087</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">317,222</td>
<td align="right">312,440</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">398,351</td>
<td align="right">394,151</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">118,626</td>
<td align="right">117,620</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">639,817</td>
<td align="right">635,035</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,234,817</td>
<td align="right">1,230,035</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,215,274</td>
<td align="right">2,215,274</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,778,696</td>
<td align="right">1,778,696</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,655,294</td>
<td align="right">1,655,294</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,400,591</td>
<td align="right">1,400,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,113,704</td>
<td align="right">1,113,704</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">918,788</td>
<td align="right">918,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">869,956</td>
<td align="right">869,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">754,555</td>
<td align="right">754,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">714,403</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">693,933</td>
<td align="right">693,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">640,585</td>
<td align="right">640,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">468,763</td>
<td align="right">468,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">459,788</td>
<td align="right">459,788</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">350,105</td>
<td align="right">350,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">315,049</td>
<td align="right">315,049</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">282,465</td>
<td align="right">282,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">274,298</td>
<td align="right">274,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">255,119</td>
<td align="right">255,119</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">231,447</td>
<td align="right">231,447</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">225,170</td>
<td align="right">225,170</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">200,606</td>
<td align="right">200,606</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">167,922</td>
<td align="right">167,922</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">130,861</td>
<td align="right">130,861</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">100,303</td>
<td align="right">100,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">96,277</td>
<td align="right">96,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">59,363</td>
<td align="right">59,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">57,253</td>
<td align="right">57,253</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">46,471</td>
<td align="right">46,471</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">40,877</td>
<td align="right">40,877</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">34,867</td>
<td align="right">34,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">32,820</td>
<td align="right">32,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">26,506</td>
<td align="right">26,506</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,762</td>
<td align="right">24,762</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">24,522</td>
<td align="right">24,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">22,517</td>
<td align="right">22,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">19,328</td>
<td align="right">19,328</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">18,816</td>
<td align="right">18,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">16,444</td>
<td align="right">16,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">16,376</td>
<td align="right">16,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">16,355</td>
<td align="right">16,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">14,329</td>
<td align="right">14,329</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">14,287</td>
<td align="right">14,287</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">12,318</td>
<td align="right">12,318</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">12,282</td>
<td align="right">12,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">12,282</td>
<td align="right">12,282</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">12,266</td>
<td align="right">12,266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">10,303</td>
<td align="right">10,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">9,576</td>
<td align="right">9,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">6,209</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,186</td>
<td align="right">6,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">6,141</td>
<td align="right">6,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">4,094</td>
<td align="right">4,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">4,073</td>
<td align="right">4,073</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,801</td>
<td align="right">3,801</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">2,247</td>
<td align="right">2,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,115</td>
<td align="right">2,115</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">2,094</td>
<td align="right">2,094</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,047</td>
<td align="right">2,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">2,026</td>
<td align="right">2,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">2,026</td>
<td align="right">2,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">2,023</td>
<td align="right">2,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">1,806</td>
<td align="right">1,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,008</td>
<td align="right">1,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">462</td>
<td align="right">462</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">252</td>
<td align="right">252</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">47</td>
<td align="right">47</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">88,255</td>
<td align="right">0.5%</td>
<td align="right">24,205</td>
<td align="right">0.1%</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,182,576</td>
<td align="right">99.5%</td>
<td align="right">18,182,576</td>
<td align="right">99.8%</td>
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
<td align="right">6,293</td>
<td align="right">0.0%</td>
<td align="right">6,293</td>
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
<td align="right">232</td>
<td align="right">20.0%</td>
<td align="right">190</td>
<td align="right">17.0%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">926</td>
<td align="right">80.0%</td>
<td align="right">926</td>
<td align="right">83.0%</td>
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
<td align="right">231</td>
<td align="right">99.6%</td>
<td align="right">189</td>
<td align="right">99.5%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1</td>
<td align="right">0.4%</td>
<td align="right">1</td>
<td align="right">0.5%</td>
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
<td align="right">714,403</td>
<td align="right">100.0%</td>
<td align="right">714,403</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">648,506</td>
<td align="right">2.8%</td>
<td align="right">648,506</td>
<td align="right">2.8%</td>
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
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
<td align="right">22,910,196</td>
<td align="right">97.2%</td>
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
<td align="right">651,317</td>
<td align="right">2.8%</td>
<td align="right">651,317</td>
<td align="right">2.8%</td>
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
<td align="right">21,627</td>
<td align="right">100.0%</td>
<td align="right">21,627</td>
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
<td align="right">903</td>
<td align="right">50.0%</td>
<td align="right">903</td>
<td align="right">50.0%</td>
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
<td align="right">903</td>
<td align="right">100.0%</td>
<td align="right">903</td>
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
<td align="right">3,401,059</td>
<td align="right">31.3%</td>
<td align="right">3,099,944</td>
<td align="right">29.8%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,448,508</td>
<td align="right">68.6%</td>
<td align="right">7,295,197</td>
<td align="right">70.2%</td>
<td align="right">-2.1%</td>
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
<td align="right">2,679</td>
<td align="right">83.6%</td>
<td align="right">2,594</td>
<td align="right">83.2%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">525</td>
<td align="right">16.4%</td>
<td align="right">525</td>
<td align="right">16.8%</td>
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
<td align="right">253</td>
<td align="right">9.4%</td>
<td align="right">231</td>
<td align="right">8.9%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">2,426</td>
<td align="right">90.6%</td>
<td align="right">2,363</td>
<td align="right">91.1%</td>
<td align="right">-2.6%</td>
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
<td align="right">18,738</td>
<td align="right">0.5%</td>
<td align="right">18,738</td>
<td align="right">0.5%</td>
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
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
<td align="right">3,545,313</td>
<td align="right">91.1%</td>
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
<td align="right">325,229</td>
<td align="right">8.4%</td>
<td align="right">325,229</td>
<td align="right">8.4%</td>
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
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">6,436</td>
<td align="right">95.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">275</td>
<td align="right">4.1%</td>
<td align="right">275</td>
<td align="right">4.1%</td>
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
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">169</td>
<td align="right">61.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">106</td>
<td align="right">38.5%</td>
<td align="right">106</td>
<td align="right">38.5%</td>
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
<td align="right">683,304</td>
<td align="right">26.9%</td>
<td align="right">468,113</td>
<td align="right">25.9%</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,852,634</td>
<td align="right">73.0%</td>
<td align="right">1,337,457</td>
<td align="right">74.0%</td>
<td align="right">-27.8%</td>
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
<td align="right">2,107</td>
<td align="right">82.0%</td>
<td align="right">1,938</td>
<td align="right">80.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">462</td>
<td align="right">18.0%</td>
<td align="right">462</td>
<td align="right">19.2%</td>
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
<td align="right">379</td>
<td align="right">18.0%</td>
<td align="right">337</td>
<td align="right">17.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">990</td>
<td align="right">47.0%</td>
<td align="right">904</td>
<td align="right">46.6%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">316</td>
<td align="right">15.0%</td>
<td align="right">295</td>
<td align="right">15.2%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">400</td>
<td align="right">19.0%</td>
<td align="right">380</td>
<td align="right">19.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">22</td>
<td align="right">1.0%</td>
<td align="right">22</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### GET_ITER

<details>
<summary> specialization stats for GET_ITER family </summary>

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
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">571,181</td>
<td align="right">571,181 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">501,515</td>
<td align="right">501,515 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">194,465</td>
<td align="right">194,465 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">188,324</td>
<td align="right">188,324 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">6,141</td>
<td align="right">6,141 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
<td align="right">4,094</td>
<td align="right">4,094 / 0 !!</td>
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
<td align="right">2,323,171</td>
<td align="right">2.7%</td>
<td align="right">1,933,828</td>
<td align="right">2.3%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,007,693</td>
<td align="right">4.6%</td>
<td align="right">3,812,204</td>
<td align="right">4.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">79,901,969</td>
<td align="right">92.6%</td>
<td align="right">78,790,490</td>
<td align="right">93.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">253,498</td>
<td align="right">0.3%</td>
<td align="right">253,498</td>
<td align="right">0.3%</td>
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
<td align="right">57,215</td>
<td align="right">75.5%</td>
<td align="right">49,859</td>
<td align="right">72.9%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">18,571</td>
<td align="right">24.5%</td>
<td align="right">18,508</td>
<td align="right">27.1%</td>
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
<td align="left">mutable class</td>
<td align="right">14,996</td>
<td align="right">80.7%</td>
<td align="right">14,933</td>
<td align="right">80.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,643</td>
<td align="right">14.2%</td>
<td align="right">2,643</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">592</td>
<td align="right">3.2%</td>
<td align="right">592</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">106</td>
<td align="right">0.6%</td>
<td align="right">106</td>
<td align="right">0.6%</td>
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
<td align="right">13,791,237</td>
<td align="right">99.9%</td>
<td align="right">13,204,638</td>
<td align="right">99.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
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
<td align="right">4,452</td>
<td align="right">0.0%</td>
<td align="right">4,452</td>
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
<td align="right">4,872</td>
<td align="right">100.0%</td>
<td align="right">4,872</td>
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
<td align="right">21</td>
<td align="right">0.1%</td>
<td align="right">21</td>
<td align="right">0.1%</td>
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
<td align="right">16,355</td>
<td align="right">99.7%</td>
<td align="right">16,355</td>
<td align="right">99.7%</td>
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
<td align="right">21</td>
<td align="right">100.0%</td>
<td align="right">21</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,348,111</td>
<td align="right">6.9%</td>
<td align="right">1,257,405</td>
<td align="right">6.4%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,284,591</td>
<td align="right">93.1%</td>
<td align="right">18,363,700</td>
<td align="right">93.6%</td>
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
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
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
<td align="right">26,736</td>
<td align="right">100.0%</td>
<td align="right">25,047</td>
<td align="right">100.0%</td>
<td align="right">-6.3%</td>
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
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.1%</td>
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
<td align="right">91,989</td>
<td align="right">99.7%</td>
<td align="right">91,989</td>
<td align="right">99.7%</td>
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
<td align="right">126</td>
<td align="right">100.0%</td>
<td align="right">126</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,963,074</td>
<td align="right">9.7%</td>
<td align="right">1,945,067</td>
<td align="right">9.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,224,095</td>
<td align="right">90.1%</td>
<td align="right">18,089,694</td>
<td align="right">90.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">41,450</td>
<td align="right">0.2%</td>
<td align="right">41,450</td>
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
<td align="left">Success</td>
<td align="right">41,201</td>
<td align="right">99.0%</td>
<td align="right">40,884</td>
<td align="right">99.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">422</td>
<td align="right">1.0%</td>
<td align="right">422</td>
<td align="right">1.0%</td>
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
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">210</td>
<td align="right">49.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">106</td>
<td align="right">25.1%</td>
<td align="right">106</td>
<td align="right">25.1%</td>
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
<td align="right">231</td>
<td align="right">0.0%</td>
<td align="right">231</td>
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
<td align="right">2,073,448</td>
<td align="right">100.0%</td>
<td align="right">2,073,448</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">231</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">148,777,150</td>
<td align="right">42.6%</td>
<td align="right">130,680,669</td>
<td align="right">42.3%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">182,033,971</td>
<td align="right">52.2%</td>
<td align="right">161,874,377</td>
<td align="right">52.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,538,015</td>
<td align="right">3.3%</td>
<td align="right">10,385,822</td>
<td align="right">3.4%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">6,621,670</td>
<td align="right">1.9%</td>
<td align="right">6,123,719</td>
<td align="right">2.0%</td>
<td align="right">-7.5%</td>
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
<td align="left">BINARY_OP</td>
<td align="right">88,255</td>
<td align="right">0.8%</td>
<td align="right">24,205</td>
<td align="right">0.2%</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,852,634</td>
<td align="right">17.2%</td>
<td align="right">1,337,457</td>
<td align="right">13.8%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">3,401,059</td>
<td align="right">31.6%</td>
<td align="right">3,099,944</td>
<td align="right">31.9%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">4,007,693</td>
<td align="right">37.2%</td>
<td align="right">3,812,204</td>
<td align="right">39.3%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">714,403</td>
<td align="right">6.6%</td>
<td align="right">714,403</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">648,506</td>
<td align="right">6.0%</td>
<td align="right">648,506</td>
<td align="right">6.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">41,450</td>
<td align="right">0.4%</td>
<td align="right">41,450</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">18,738</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">4,788</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">945</td>
<td align="right">0.0%</td>
<td align="right">945</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">739,363</td>
<td align="right">11.2%</td>
<td align="right">507,660</td>
<td align="right">8.3%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,288,155</td>
<td align="right">19.5%</td>
<td align="right">1,130,515</td>
<td align="right">18.5%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,348,111</td>
<td align="right">20.4%</td>
<td align="right">1,257,405</td>
<td align="right">20.5%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">758,695</td>
<td align="right">11.5%</td>
<td align="right">749,444</td>
<td align="right">12.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">856,804</td>
<td align="right">12.9%</td>
<td align="right">849,001</td>
<td align="right">13.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">208,806</td>
<td align="right">3.2%</td>
<td align="right">207,853</td>
<td align="right">3.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">324,298</td>
<td align="right">4.9%</td>
<td align="right">324,298</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">319,627</td>
<td align="right">4.8%</td>
<td align="right">319,627</td>
<td align="right">5.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">282,563</td>
<td align="right">4.3%</td>
<td align="right">282,563</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">162,763</td>
<td align="right">2.5%</td>
<td align="right">162,763</td>
<td align="right">2.7%</td>
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
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">15,675,914</td>
<td align="right">87.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">2,215,342</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
<td align="right">243,656</td>
<td align="right">1.4%</td>
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
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
<td align="right">1,971,686</td>
<td align="right">11.0%</td>
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
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">225,191</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">6,209</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
<td align="right">1,375,899</td>
<td align="right">7.7%</td>
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
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">22,517</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
<td align="right">17,872,812</td>
<td align="right">99.9%</td>
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
<td align="right">105</td>
<td align="right">0.0%</td>
<td align="right">66.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">7,011,330</td>
<td align="right">3.4%</td>
<td align="right">5,432,266</td>
<td align="right">2.6%</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">8,369,063</td>
<td align="right">3.8%</td>
<td align="right">6,517,079</td>
<td align="right">3.0%</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">37,204</td>
<td align="right"></td>
<td align="right">43,224</td>
<td align="right"></td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">62,370,980</td>
<td align="right">28.6%</td>
<td align="right">69,724,892</td>
<td align="right">32.0%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">509,894</td>
<td align="right"></td>
<td align="right">567,892</td>
<td align="right"></td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">475,680</td>
<td align="right"></td>
<td align="right">527,707</td>
<td align="right"></td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">63,315,617</td>
<td align="right">30.5%</td>
<td align="right">69,397,714</td>
<td align="right">33.4%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">105,479,693</td>
<td align="right">48.4%</td>
<td align="right">98,422,841</td>
<td align="right">45.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">87,530,019</td>
<td align="right">42.1%</td>
<td align="right">81,744,597</td>
<td align="right">39.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">41,653,619</td>
<td align="right">19.1%</td>
<td align="right">43,388,379</td>
<td align="right">19.9%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">14,541</td>
<td align="right">0.1%</td>
<td align="right">15,108</td>
<td align="right">0.1%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">49,932,869</td>
<td align="right">24.0%</td>
<td align="right">51,393,553</td>
<td align="right">24.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">13,730,007</td>
<td align="right"></td>
<td align="right">13,567,432</td>
<td align="right"></td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">5,631,280</td>
<td align="right"></td>
<td align="right">5,625,218</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">7,554,226</td>
<td align="right">40.0%</td>
<td align="right">7,554,733</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">7,330,919</td>
<td align="right"></td>
<td align="right">7,331,127</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,335,312</td>
<td align="right"></td>
<td align="right">11,335,503</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,337,495</td>
<td align="right">60.0%</td>
<td align="right">11,337,686</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">7,539,622</td>
<td align="right">39.9%</td>
<td align="right">7,539,520</td>
<td align="right">39.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">341,849</td>
<td align="right"></td>
<td align="right">341,849</td>
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
<td align="right">320</td>
<td align="right">529,920</td>
<td align="right">4,206,903</td>
<td align="right">103,072</td>
<td align="right">596,496</td>
<td align="right">320</td>
<td align="right">530,550</td>
<td align="right">4,209,893</td>
<td align="right">101,487</td>
<td align="right">598,320</td>
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
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">109</td>
<td align="right">20.4%</td>
<td align="right">489</td>
<td align="right">25.9%</td>
<td align="right">348.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">534</td>
<td align="right"></td>
<td align="right">1,885</td>
<td align="right"></td>
<td align="right">253.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">339</td>
<td align="right">63.5%</td>
<td align="right">1,120</td>
<td align="right">59.4%</td>
<td align="right">230.4%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">86</td>
<td align="right">16.1%</td>
<td align="right">255</td>
<td align="right">13.5%</td>
<td align="right">196.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,492,713</td>
<td align="right"></td>
<td align="right">4,034,541</td>
<td align="right"></td>
<td align="right">170.3%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">331,810,567</td>
<td align="right">22,228.7%</td>
<td align="right">425,336,432</td>
<td align="right">10,542.4%</td>
<td align="right">28.2%</td>
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
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21 / 0 !!</td>
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

A potential trace is abandoned because it is too short.
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">42</td>
<td align="right">2.2%</td>
<td align="right">42 / 0 !!</td>
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
<td align="right">21</td>
<td align="right">1.1%</td>
<td align="right">21 / 0 !!</td>
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
<td align="right">63</td>
<td align="right">3.3%</td>
<td align="right">63 / 0 !!</td>
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
<td align="right">275</td>
<td align="right">81.1%</td>
<td align="right">931</td>
<td align="right">83.1%</td>
<td align="right">238.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">339</td>
<td align="right"></td>
<td align="right">1,120</td>
<td align="right"></td>
<td align="right">230.4%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">617,097</td>
<td align="right">13.7%</td>
<td align="right">2,024,387</td>
<td align="right">20.4%</td>
<td align="right">228.1%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">94,696</td>
<td align="right">2.1%</td>
<td align="right">212,176</td>
<td align="right">2.1%</td>
<td align="right">124.1%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">4,489,216</td>
<td align="right"></td>
<td align="right">9,928,704</td>
<td align="right"></td>
<td align="right">121.2%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">3,777,423</td>
<td align="right">84.1%</td>
<td align="right">7,692,141</td>
<td align="right">77.5%</td>
<td align="right">103.6%</td>
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
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">258,048</td>
<td align="right">2.6%</td>
<td align="right">258,048 / 0 !!</td>
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
<td align="left">22</td>
<td align="right">8.0%</td>
<td align="left">320</td>
<td align="right">34.4%</td>
<td align="right">1,354.5%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">84</td>
<td align="right">30.5%</td>
<td align="left">296</td>
<td align="right">31.8%</td>
<td align="right">252.4%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">106</td>
<td align="right">38.5%</td>
<td align="left">210</td>
<td align="right">22.6%</td>
<td align="right">98.1%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">21</td>
<td align="right">7.6%</td>
<td align="left">63</td>
<td align="right">6.8%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">15.3%</td>
<td align="left">42</td>
<td align="right">4.5%</td>
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
<td align="left"><= 32</td>
<td align="right">43</td>
<td align="right">12.7%</td>
<td align="right">232</td>
<td align="right">20.7%</td>
<td align="right">439.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">84</td>
<td align="right">24.8%</td>
<td align="right">358</td>
<td align="right">32.0%</td>
<td align="right">326.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">105</td>
<td align="right">9.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">5.6%</td>
<td align="right">63 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">168</td>
<td align="right">15.0%</td>
<td align="right">58.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">47</td>
<td align="right">4.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">147</td>
<td align="right">13.1%</td>
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
<td align="left"><= 16</td>
<td align="right">22</td>
<td align="right">6.5%</td>
<td align="right">252</td>
<td align="right">22.5%</td>
<td align="right">1,045.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">296</td>
<td align="right">26.4%</td>
<td align="right">369.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">106</td>
<td align="right">31.3%</td>
<td align="right">189</td>
<td align="right">16.9%</td>
<td align="right">78.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">21</td>
<td align="right">6.2%</td>
<td align="right">63</td>
<td align="right">5.6%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">18.6%</td>
<td align="right">84</td>
<td align="right">7.5%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">43</td>
<td align="right">3.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">4</td>
<td align="right">0.4%</td>
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
<td align="left">_POP_ITER</td>
<td align="right">1,698</td>
<td align="right">20,403</td>
<td align="right">1,101.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">7,099</td>
<td align="right">77,842</td>
<td align="right">996.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,099</td>
<td align="right">63,190</td>
<td align="right">790.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">22,365</td>
<td align="right">199,059</td>
<td align="right">790.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right">135,081</td>
<td align="right">433,555</td>
<td align="right">221.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,657</td>
<td align="right">43,154</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,657</td>
<td align="right">43,154</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE</td>
<td align="right">15,657</td>
<td align="right">43,154</td>
<td align="right">175.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">189,556</td>
<td align="right">515,830</td>
<td align="right">172.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,492,713</td>
<td align="right">4,034,541</td>
<td align="right">170.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,492,713</td>
<td align="right">4,034,541</td>
<td align="right">170.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">142,180</td>
<td align="right">378,119</td>
<td align="right">165.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">248,919</td>
<td align="right">530,285</td>
<td align="right">113.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">3,594,416</td>
<td align="right">6,370,417</td>
<td align="right">77.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">791,406</td>
<td align="right">1,399,740</td>
<td align="right">76.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">135,081</td>
<td align="right">225,706</td>
<td align="right">67.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">606,319</td>
<td align="right">984,599</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">981,633</td>
<td align="right">1,582,581</td>
<td align="right">61.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">173,869</td>
<td align="right">275,893</td>
<td align="right">58.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">135,081</td>
<td align="right">214,245</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">135,767</td>
<td align="right">211,770</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,088,558</td>
<td align="right">1,655,908</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">135,767</td>
<td align="right">204,423</td>
<td align="right">50.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">135,081</td>
<td align="right">199,593</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">135,081</td>
<td align="right">199,593</td>
<td align="right">47.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,117,414</td>
<td align="right">1,626,454</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">525,655</td>
<td align="right">758,227</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,283,002</td>
<td align="right">1,837,710</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">194,444</td>
<td align="right">273,608</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">734,852</td>
<td align="right">1,026,043</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,039,582</td>
<td align="right">9,725,078</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">522,531</td>
<td align="right">716,611</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">606,319</td>
<td align="right">831,288</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">390,574</td>
<td align="right">534,418</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">698,455</td>
<td align="right">943,482</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,656,089</td>
<td align="right">2,224,589</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,447,309</td>
<td align="right">1,932,903</td>
<td align="right">33.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,539,775</td>
<td align="right">2,054,952</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">193,006</td>
<td align="right">257,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">257,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right">193,006</td>
<td align="right">257,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right">193,006</td>
<td align="right">257,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right">193,006</td>
<td align="right">257,056</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">2,278,033</td>
<td align="right">3,025,470</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,201,538</td>
<td align="right">4,240,135</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">6,092,541</td>
<td align="right">8,042,418</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,051,776</td>
<td align="right">5,324,468</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">1,853,101</td>
<td align="right">2,433,532</td>
<td align="right">31.3%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,988,182</td>
<td align="right">2,587,803</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">1,988,182</td>
<td align="right">2,587,803</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,988,182</td>
<td align="right">2,587,803</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,988,182</td>
<td align="right">2,587,803</td>
<td align="right">30.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">1,988,182</td>
<td align="right">2,583,021</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,531,163</td>
<td align="right">3,269,419</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">5,708,510</td>
<td align="right">7,314,135</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">64,378,571</td>
<td align="right">81,742,173</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">5,544,555</td>
<td align="right">6,996,855</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">2,039,981</td>
<td align="right">2,570,168</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right">3,721,468</td>
<td align="right">4,672,053</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">2,255,668</td>
<td align="right">2,826,411</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">62,828,119</td>
<td align="right">78,712,505</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">3,938,671</td>
<td align="right">4,889,448</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">1,283,002</td>
<td align="right">1,584,117</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">3,104,441</td>
<td align="right">3,774,975</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">3,699,103</td>
<td align="right">4,472,994</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">25,934,797</td>
<td align="right">31,142,353</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">9,237,109</td>
<td align="right">11,087,700</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">34,385,692</td>
<td align="right">41,263,691</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">1,846,002</td>
<td align="right">2,209,684</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">7,384,008</td>
<td align="right">8,819,608</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,692,004</td>
<td align="right">4,409,804</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">3,692,004</td>
<td align="right">4,409,804</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">3,692,004</td>
<td align="right">4,409,804</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right">3,692,004</td>
<td align="right">4,409,804</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,846,002</td>
<td align="right">2,204,902</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_NOP</td>
<td align="right">1,846,002</td>
<td align="right">2,204,902</td>
<td align="right">19.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">10,517,504</td>
<td align="right">12,507,923</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">1,655,092</td>
<td align="right">1,937,687</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right">31,351</td>
<td align="right">35,551</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,250,654</td>
<td align="right">1,401,182</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,101,703</td>
<td align="right">2,335,876</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right"></td>
<td align="right">213,643</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right"></td>
<td align="right">185,499</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right"></td>
<td align="right">185,499</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right"></td>
<td align="right">169,011</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">167,963</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">161,664</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_3</td>
<td align="right"></td>
<td align="right">153,311</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">142,580</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right"></td>
<td align="right">127,809</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">120,278</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">112,973</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">100,684</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">37,942</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">29,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">29,692</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">26,113</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right"></td>
<td align="right">9,908</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right"></td>
<td align="right">9,359</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right"></td>
<td align="right">7,347</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right"></td>
<td align="right">4,782</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">4,782</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right"></td>
<td align="right">4,782</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">2,391</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">1,006</td>
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
Stats gathered on: 2025-07-01
