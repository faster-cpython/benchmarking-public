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
<td align="right">63</td>
<td align="right">33,075</td>
<td align="right">52,400.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">238,371</td>
<td align="right">107,856</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">124,635</td>
<td align="right">69,069</td>
<td align="right">-44.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">97,902</td>
<td align="right">54,726</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">227,157</td>
<td align="right">128,835</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">452,277</td>
<td align="right">300,174</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">25,011</td>
<td align="right">18,018</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">3,437,217</td>
<td align="right">2,764,335</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">2,868,642</td>
<td align="right">2,409,519</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">533,547</td>
<td align="right">448,602</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">46,200</td>
<td align="right">39,186</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">279,342</td>
<td align="right">237,300</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">773,556</td>
<td align="right">658,161</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">49,812</td>
<td align="right">42,819</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">453,285</td>
<td align="right">391,587</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">10,410,330</td>
<td align="right">9,235,632</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">10,253,628</td>
<td align="right">9,530,199</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">575,484</td>
<td align="right">535,542</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">985,467</td>
<td align="right">920,955</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">17,903,466</td>
<td align="right">16,858,338</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,702,651</td>
<td align="right">9,154,572</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,139,123</td>
<td align="right">2,033,682</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">1,842,561</td>
<td align="right">1,773,114</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">7,017,045</td>
<td align="right">6,760,299</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">4,509,708</td>
<td align="right">4,346,223</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">850,017</td>
<td align="right">820,638</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">9,814,161</td>
<td align="right">9,476,985</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">11,941,188</td>
<td align="right">11,531,961</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">7,439,124</td>
<td align="right">7,203,966</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">33,998,412</td>
<td align="right">32,943,204</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">17,510,871</td>
<td align="right">16,999,626</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">25,438,098</td>
<td align="right">24,699,192</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">90,453,111</td>
<td align="right">87,974,586</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">37,743,867</td>
<td align="right">36,763,545</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">49,358,967</td>
<td align="right">48,302,961</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">6,306,090</td>
<td align="right">6,440,805</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">10,605,252</td>
<td align="right">10,385,907</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,045,254</td>
<td align="right">1,023,645</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">28,575,393</td>
<td align="right">28,020,300</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">9,899,043</td>
<td align="right">9,713,256</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">389,403</td>
<td align="right">382,410</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">15,486,324</td>
<td align="right">15,252,027</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">5,336,520</td>
<td align="right">5,255,901</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">9,319,065</td>
<td align="right">9,189,894</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">6,772,962</td>
<td align="right">6,680,268</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">30,348,255</td>
<td align="right">29,997,177</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">43,185,366</td>
<td align="right">42,715,659</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">4,061,883</td>
<td align="right">4,024,041</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,274,887</td>
<td align="right">3,247,020</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">22,802,745</td>
<td align="right">22,624,875</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">506,016</td>
<td align="right">502,719</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">16,414,041</td>
<td align="right">16,310,784</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">2,956,023</td>
<td align="right">2,937,858</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,823,030</td>
<td align="right">2,806,104</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">5,454,351</td>
<td align="right">5,421,864</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">15,775,788</td>
<td align="right">15,699,747</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">9,019,269</td>
<td align="right">8,987,643</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">24,753,645</td>
<td align="right">24,668,700</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">7,203,210</td>
<td align="right">7,224,021</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">2,537,073</td>
<td align="right">2,533,776</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">8,412,390</td>
<td align="right">8,405,397</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">12,855,339</td>
<td align="right">12,855,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">8,347,374</td>
<td align="right">8,347,374</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">7,942,053</td>
<td align="right">7,942,053</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">7,740,558</td>
<td align="right">7,740,558</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">7,025,298</td>
<td align="right">7,025,298</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">5,528,187</td>
<td align="right">5,528,187</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">5,301,576</td>
<td align="right">5,301,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">3,738,693</td>
<td align="right">3,738,693</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">3,568,068</td>
<td align="right">3,568,068</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,402,903</td>
<td align="right">3,402,903</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">3,402,882</td>
<td align="right">3,402,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">3,189,564</td>
<td align="right">3,189,564</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">2,803,563</td>
<td align="right">2,803,563</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">2,773,827</td>
<td align="right">2,773,827</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">2,604,882</td>
<td align="right">2,604,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">2,413,908</td>
<td align="right">2,413,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">2,413,908</td>
<td align="right">2,413,908</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">2,363,886</td>
<td align="right">2,363,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">2,349,186</td>
<td align="right">2,349,186</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">2,288,496</td>
<td align="right">2,288,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">1,925,280</td>
<td align="right">1,925,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,861,272</td>
<td align="right">1,861,272</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">1,861,209</td>
<td align="right">1,861,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">1,355,634</td>
<td align="right">1,355,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">904,008</td>
<td align="right">904,008</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">772,380</td>
<td align="right">772,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">710,010</td>
<td align="right">710,010</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">495,159</td>
<td align="right">495,159</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">469,140</td>
<td align="right">469,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">279,153</td>
<td align="right">279,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">260,841</td>
<td align="right">260,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">123,417</td>
<td align="right">123,417</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">110,082</td>
<td align="right">110,082</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">90,153</td>
<td align="right">90,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">89,145</td>
<td align="right">89,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">88,956</td>
<td align="right">88,956</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">64,260</td>
<td align="right">64,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">55,230</td>
<td align="right">55,230</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">26,712</td>
<td align="right">26,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">24,255</td>
<td align="right">24,255</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">24,150</td>
<td align="right">24,150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">21,105</td>
<td align="right">21,105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">15,099</td>
<td align="right">15,099</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">14,700</td>
<td align="right">14,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">14,259</td>
<td align="right">14,259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">12,936</td>
<td align="right">12,936</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">12,726</td>
<td align="right">12,726</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">12,663</td>
<td align="right">12,663</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">9,870</td>
<td align="right">9,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">9,555</td>
<td align="right">9,555</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">6,867</td>
<td align="right">6,867</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,741</td>
<td align="right">6,741</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,843</td>
<td align="right">3,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">2,982</td>
<td align="right">2,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">2,835</td>
<td align="right">2,835</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">2,373</td>
<td align="right">2,373</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">1,890</td>
<td align="right">1,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,848</td>
<td align="right">1,848</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">1,428</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,428</td>
<td align="right">1,428</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,092</td>
<td align="right">1,092</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">924</td>
<td align="right">924</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">588</td>
<td align="right">588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">189</td>
<td align="right">189</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">105</td>
<td align="right">105</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
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
<td align="right">45,066</td>
<td align="right">5.7%</td>
<td align="right">38,073</td>
<td align="right">4.9%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">739,137</td>
<td align="right">94.1%</td>
<td align="right">739,137</td>
<td align="right">94.9%</td>
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
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">189</td>
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
<td align="right">483</td>
<td align="right">42.6%</td>
<td align="right">462</td>
<td align="right">41.5%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">651</td>
<td align="right">57.4%</td>
<td align="right">651</td>
<td align="right">58.5%</td>
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
<td align="left">subscr tuple slice</td>
<td align="right">189</td>
<td align="right">39.1%</td>
<td align="right">168</td>
<td align="right">36.4%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">168</td>
<td align="right">34.8%</td>
<td align="right">168</td>
<td align="right">36.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">105</td>
<td align="right">21.7%</td>
<td align="right">105</td>
<td align="right">22.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">21</td>
<td align="right">4.3%</td>
<td align="right">21</td>
<td align="right">4.5%</td>
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
<td align="right">3,843</td>
<td align="right">100.0%</td>
<td align="right">3,843</td>
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
<td align="right">429,933</td>
<td align="right">0.6%</td>
<td align="right">423,213</td>
<td align="right">0.6%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">429,219</td>
<td align="right">0.6%</td>
<td align="right">422,625</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">72,054,990</td>
<td align="right">99.4%</td>
<td align="right">72,038,736</td>
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
<td align="right">15,414</td>
<td align="right">100.0%</td>
<td align="right">15,288</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">294</td>
<td align="right">50.0%</td>
<td align="right">294</td>
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
<td align="right">294</td>
<td align="right">100.0%</td>
<td align="right">294</td>
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
<td align="right">1,041,558</td>
<td align="right">76.0%</td>
<td align="right">1,019,970</td>
<td align="right">75.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">325,101</td>
<td align="right">23.7%</td>
<td align="right">325,101</td>
<td align="right">24.1%</td>
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
<td align="right">3,402</td>
<td align="right">92.0%</td>
<td align="right">3,381</td>
<td align="right">92.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">294</td>
<td align="right">8.0%</td>
<td align="right">294</td>
<td align="right">8.0%</td>
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
<td align="left">string</td>
<td align="right">210</td>
<td align="right">6.2%</td>
<td align="right">189</td>
<td align="right">5.6%</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,302</td>
<td align="right">38.3%</td>
<td align="right">1,302</td>
<td align="right">38.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">1,176</td>
<td align="right">34.6%</td>
<td align="right">1,176</td>
<td align="right">34.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">399</td>
<td align="right">11.7%</td>
<td align="right">399</td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">252</td>
<td align="right">7.4%</td>
<td align="right">252</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">63</td>
<td align="right">1.9%</td>
<td align="right">63</td>
<td align="right">1.9%</td>
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
<td align="right">452,109</td>
<td align="right">96.1%</td>
<td align="right">390,453</td>
<td align="right">95.5%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,952</td>
<td align="right">3.2%</td>
<td align="right">14,952</td>
<td align="right">3.7%</td>
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
<td align="right">2,142</td>
<td align="right">0.5%</td>
<td align="right">2,142</td>
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
<td align="right">987</td>
<td align="right">82.5%</td>
<td align="right">945</td>
<td align="right">81.8%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">210</td>
<td align="right">17.5%</td>
<td align="right">210</td>
<td align="right">18.2%</td>
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
<td align="right">987</td>
<td align="right">100.0%</td>
<td align="right">945</td>
<td align="right">100.0%</td>
<td align="right">-4.3%</td>
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
<td align="right">11,302,515</td>
<td align="right">53.8%</td>
<td align="right">10,574,067</td>
<td align="right">53.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">9,697,023</td>
<td align="right">46.2%</td>
<td align="right">9,149,112</td>
<td align="right">46.4%</td>
<td align="right">-5.7%</td>
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
<td align="right">5,187</td>
<td align="right">92.2%</td>
<td align="right">5,019</td>
<td align="right">91.9%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">441</td>
<td align="right">7.8%</td>
<td align="right">441</td>
<td align="right">8.1%</td>
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
<td align="right">231</td>
<td align="right">4.5%</td>
<td align="right">210</td>
<td align="right">4.2%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">483</td>
<td align="right">9.3%</td>
<td align="right">441</td>
<td align="right">8.8%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">315</td>
<td align="right">6.1%</td>
<td align="right">294</td>
<td align="right">5.9%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">3,213</td>
<td align="right">61.9%</td>
<td align="right">3,129</td>
<td align="right">62.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">693</td>
<td align="right">13.4%</td>
<td align="right">693</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">126</td>
<td align="right">2.4%</td>
<td align="right">126</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">126</td>
<td align="right">2.4%</td>
<td align="right">126</td>
<td align="right">2.5%</td>
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
<td align="right">6,398,406</td>
<td align="right">6,398,406 / 0 !!</td>
<td align="right">6,398,406</td>
<td align="right">6,398,406 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,771,684</td>
<td align="right">3,771,684 / 0 !!</td>
<td align="right">3,771,684</td>
<td align="right">3,771,684 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">427,329</td>
<td align="right">427,329 / 0 !!</td>
<td align="right">427,329</td>
<td align="right">427,329 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,248</td>
<td align="right">31,248 / 0 !!</td>
<td align="right">31,248</td>
<td align="right">31,248 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">24,822</td>
<td align="right">24,822 / 0 !!</td>
<td align="right">24,822</td>
<td align="right">24,822 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">24,696</td>
<td align="right">24,696 / 0 !!</td>
<td align="right">24,696</td>
<td align="right">24,696 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,394</td>
<td align="right">2,394 / 0 !!</td>
<td align="right">2,394</td>
<td align="right">2,394 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,197</td>
<td align="right">1,197 / 0 !!</td>
<td align="right">1,197</td>
<td align="right">1,197 / 0 !!</td>
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
<td align="right">4,955,160</td>
<td align="right">10.7%</td>
<td align="right">4,803,183</td>
<td align="right">10.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">41,385,540</td>
<td align="right">89.1%</td>
<td align="right">40,758,480</td>
<td align="right">89.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">111,888</td>
<td align="right">0.2%</td>
<td align="right">111,888</td>
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
<td align="right">302,967</td>
<td align="right">0.7%</td>
<td align="right">302,967</td>
<td align="right">0.7%</td>
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
<td align="right">101,199</td>
<td align="right">96.8%</td>
<td align="right">98,343</td>
<td align="right">96.7%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,360</td>
<td align="right">3.2%</td>
<td align="right">3,360</td>
<td align="right">3.3%</td>
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
<td align="right">2,793</td>
<td align="right">83.1%</td>
<td align="right">2,793</td>
<td align="right">83.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">525</td>
<td align="right">15.6%</td>
<td align="right">525</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">21</td>
<td align="right">0.6%</td>
<td align="right">21</td>
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
<td align="right">67,258,191</td>
<td align="right">100.0%</td>
<td align="right">65,206,365</td>
<td align="right">100.0%</td>
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
<td align="right">6,363</td>
<td align="right">0.0%</td>
<td align="right">6,363</td>
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
<td align="right">4,242</td>
<td align="right">0.0%</td>
<td align="right">4,242</td>
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
<td align="right">6,405</td>
<td align="right">100.0%</td>
<td align="right">6,405</td>
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
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">42</td>
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
<td align="right">7,942,053</td>
<td align="right">100.0%</td>
<td align="right">7,942,053</td>
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
<td align="right">42</td>
<td align="right">100.0%</td>
<td align="right">42</td>
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
<td align="right">235,137</td>
<td align="right">40.7%</td>
<td align="right">236,817</td>
<td align="right">41.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">340,347</td>
<td align="right">59.0%</td>
<td align="right">338,625</td>
<td align="right">58.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">924</td>
<td align="right">0.2%</td>
<td align="right">924</td>
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
<td align="right">7,245</td>
<td align="right">100.0%</td>
<td align="right">7,203</td>
<td align="right">100.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">227,157</td>
<td align="right">100.0%</td>
<td align="right">227,157</td>
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
<td align="right">36,241,443</td>
<td align="right">84.0%</td>
<td align="right">35,245,623</td>
<td align="right">83.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,269,889</td>
<td align="right">7.6%</td>
<td align="right">3,242,043</td>
<td align="right">7.7%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,632,727</td>
<td align="right">8.4%</td>
<td align="right">3,625,125</td>
<td align="right">8.6%</td>
<td align="right">-0.2%</td>
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
<td align="right">1,407</td>
<td align="right">1.9%</td>
<td align="right">1,386</td>
<td align="right">1.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">72,009</td>
<td align="right">98.1%</td>
<td align="right">71,883</td>
<td align="right">98.1%</td>
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
<td align="right">525</td>
<td align="right">37.3%</td>
<td align="right">504</td>
<td align="right">36.4%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">882</td>
<td align="right">62.7%</td>
<td align="right">882</td>
<td align="right">63.6%</td>
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
<td align="right">89,502</td>
<td align="right">0.7%</td>
<td align="right">89,502</td>
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
<td align="right">12,836,775</td>
<td align="right">99.3%</td>
<td align="right">12,836,775</td>
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
<td align="right">420</td>
<td align="right">64.5%</td>
<td align="right">420</td>
<td align="right">64.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">231</td>
<td align="right">35.5%</td>
<td align="right">231</td>
<td align="right">35.5%</td>
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
<td align="right">231</td>
<td align="right">100.0%</td>
<td align="right">231</td>
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
<td align="right">24,088,743</td>
<td align="right">3.2%</td>
<td align="right">23,293,305</td>
<td align="right">3.1%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">302,529,549</td>
<td align="right">40.0%</td>
<td align="right">294,112,623</td>
<td align="right">39.8%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">9,364,740</td>
<td align="right">1.2%</td>
<td align="right">9,196,740</td>
<td align="right">1.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">420,577,899</td>
<td align="right">55.6%</td>
<td align="right">413,220,969</td>
<td align="right">55.9%</td>
<td align="right">-1.7%</td>
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
<td align="right">45,066</td>
<td align="right">0.3%</td>
<td align="right">38,073</td>
<td align="right">0.3%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">452,109</td>
<td align="right">3.0%</td>
<td align="right">390,453</td>
<td align="right">2.7%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">9,697,023</td>
<td align="right">64.0%</td>
<td align="right">9,149,112</td>
<td align="right">63.2%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,041,558</td>
<td align="right">6.9%</td>
<td align="right">1,019,970</td>
<td align="right">7.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">429,219</td>
<td align="right">2.8%</td>
<td align="right">422,625</td>
<td align="right">2.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">3,269,889</td>
<td align="right">21.6%</td>
<td align="right">3,242,043</td>
<td align="right">22.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">111,888</td>
<td align="right">0.7%</td>
<td align="right">111,888</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">89,502</td>
<td align="right">0.6%</td>
<td align="right">89,502</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">6,363</td>
<td align="right">0.0%</td>
<td align="right">6,363</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">3,843</td>
<td align="right">0.0%</td>
<td align="right">3,843</td>
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
<td align="right">1,425,753</td>
<td align="right">15.2%</td>
<td align="right">1,352,358</td>
<td align="right">14.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">863,142</td>
<td align="right">9.2%</td>
<td align="right">828,828</td>
<td align="right">9.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">248,241</td>
<td align="right">2.7%</td>
<td align="right">241,521</td>
<td align="right">2.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">3,115,056</td>
<td align="right">33.3%</td>
<td align="right">3,036,474</td>
<td align="right">33.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,488,101</td>
<td align="right">26.6%</td>
<td align="right">2,514,813</td>
<td align="right">27.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">340,347</td>
<td align="right">3.6%</td>
<td align="right">338,625</td>
<td align="right">3.7%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">392,301</td>
<td align="right">4.2%</td>
<td align="right">392,301</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">279,972</td>
<td align="right">3.0%</td>
<td align="right">279,972</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">181,692</td>
<td align="right">1.9%</td>
<td align="right">181,692</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,050</td>
<td align="right">0.2%</td>
<td align="right">22,050</td>
<td align="right">0.2%</td>
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
<td align="right">7,025,361</td>
<td align="right">13.8%</td>
<td align="right">7,025,361</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">43,782,123</td>
<td align="right">86.2%</td>
<td align="right">43,782,123</td>
<td align="right">86.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">7,025,361</td>
<td align="right">13.8%</td>
<td align="right">7,025,361</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">4,551,099</td>
<td align="right">9.0%</td>
<td align="right">4,551,099</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">2,474,262</td>
<td align="right">4.9%</td>
<td align="right">2,474,262</td>
<td align="right">4.9%</td>
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
<td align="right">4,551,099</td>
<td align="right">9.0%</td>
<td align="right">4,551,099</td>
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
<td align="right">1,562,400</td>
<td align="right">3.1%</td>
<td align="right">1,562,400</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">25,263</td>
<td align="right">0.0%</td>
<td align="right">25,263</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">2,972,046</td>
<td align="right">5.8%</td>
<td align="right">2,972,046</td>
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
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">189</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">32,651,997</td>
<td align="right">64.3%</td>
<td align="right">32,651,997</td>
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
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">252</td>
<td align="right">0.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">15,761</td>
<td align="right"></td>
<td align="right">2,610</td>
<td align="right"></td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">493,877</td>
<td align="right"></td>
<td align="right">466,495</td>
<td align="right"></td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">478,947</td>
<td align="right"></td>
<td align="right">464,670</td>
<td align="right"></td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">191,581,677</td>
<td align="right">38.0%</td>
<td align="right">187,902,498</td>
<td align="right">37.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">181,555,718</td>
<td align="right">36.0%</td>
<td align="right">184,936,634</td>
<td align="right">36.7%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">202,343,391</td>
<td align="right">35.9%</td>
<td align="right">205,832,984</td>
<td align="right">36.6%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">244,422,885</td>
<td align="right">43.4%</td>
<td align="right">240,635,262</td>
<td align="right">42.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">31,353</td>
<td align="right">0.0%</td>
<td align="right">31,794</td>
<td align="right">0.0%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">5,167,386</td>
<td align="right"></td>
<td align="right">5,094,975</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">16,237,263</td>
<td align="right">3.2%</td>
<td align="right">16,047,339</td>
<td align="right">3.2%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">11,681,523</td>
<td align="right">2.1%</td>
<td align="right">11,660,460</td>
<td align="right">2.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">114,802,180</td>
<td align="right">22.8%</td>
<td align="right">114,929,944</td>
<td align="right">22.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">104,489,495</td>
<td align="right">18.6%</td>
<td align="right">104,447,522</td>
<td align="right">18.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">46,390,039</td>
<td align="right"></td>
<td align="right">46,380,321</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">32,023,007</td>
<td align="right">39.8%</td>
<td align="right">32,023,784</td>
<td align="right">39.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">31,991,570</td>
<td align="right">39.7%</td>
<td align="right">31,991,738</td>
<td align="right">39.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">34,158,257</td>
<td align="right"></td>
<td align="right">34,158,340</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">48,463,840</td>
<td align="right">60.2%</td>
<td align="right">48,463,882</td>
<td align="right">60.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">48,464,682</td>
<td align="right"></td>
<td align="right">48,464,724</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">16,443</td>
<td align="right"></td>
<td align="right">16,443</td>
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
<td align="right">9,807</td>
<td align="right">331,569</td>
<td align="right">7,770</td>
<td align="right">29,547</td>
<td align="right">21</td>
<td align="right">9,807</td>
<td align="right">337,953</td>
<td align="right">4,851</td>
<td align="right">32,256</td>
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
<td align="right">42</td>
<td align="right">1.2%</td>
<td align="right">210</td>
<td align="right">4.0%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">357</td>
<td align="right">10.1%</td>
<td align="right">1,197</td>
<td align="right">23.0%</td>
<td align="right">235.3%</td>
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
<td align="right">1.2%</td>
<td align="right">84</td>
<td align="right">1.6%</td>
<td align="right">100.0%</td>
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
<td align="right">1.2%</td>
<td align="right">63</td>
<td align="right">1.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">3,549</td>
<td align="right"></td>
<td align="right">5,208</td>
<td align="right"></td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">10,729,950</td>
<td align="right"></td>
<td align="right">14,821,086</td>
<td align="right"></td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">1,869</td>
<td align="right">52.7%</td>
<td align="right">2,478</td>
<td align="right">47.6%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">242,662,245</td>
<td align="right">2,261.5%</td>
<td align="right">293,359,500</td>
<td align="right">1,979.3%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">1,323</td>
<td align="right">37.3%</td>
<td align="right">1,512</td>
<td align="right">29.0%</td>
<td align="right">14.3%</td>
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
<td align="right">0.4%</td>
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
<td align="right">357</td>
<td align="right"></td>
<td align="right">1,197</td>
<td align="right"></td>
<td align="right">235.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">357</td>
<td align="right">100.0%</td>
<td align="right">1,134</td>
<td align="right">94.7%</td>
<td align="right">217.6%</td>
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
<td align="right">86,016</td>
<td align="right">1.7%</td>
<td align="right">258,048</td>
<td align="right">2.0%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">851,697</td>
<td align="right">16.5%</td>
<td align="right">2,424,660</td>
<td align="right">19.2%</td>
<td align="right">184.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">98,280</td>
<td align="right">1.9%</td>
<td align="right">252,168</td>
<td align="right">2.0%</td>
<td align="right">156.6%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">5,160,960</td>
<td align="right"></td>
<td align="right">12,644,352</td>
<td align="right"></td>
<td align="right">145.0%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">4,210,983</td>
<td align="right">81.6%</td>
<td align="right">9,967,524</td>
<td align="right">78.8%</td>
<td align="right">136.7%</td>
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
<td align="left">42</td>
<td align="right">11.8%</td>
<td align="left">420</td>
<td align="right">37.0%</td>
<td align="right">900.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">168</td>
<td align="right">47.1%</td>
<td align="left">378</td>
<td align="right">33.3%</td>
<td align="right">125.0%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">63</td>
<td align="right">17.6%</td>
<td align="left">84</td>
<td align="right">7.4%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">42</td>
<td align="right">11.8%</td>
<td align="left">210</td>
<td align="right">18.5%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">42</td>
<td align="right">11.8%</td>
<td align="left">42</td>
<td align="right">3.7%</td>
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
<td align="right">42</td>
<td align="right">11.8%</td>
<td align="right">210</td>
<td align="right">17.5%</td>
<td align="right">400.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">63</td>
<td align="right">5.3%</td>
<td align="right">63 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">42</td>
<td align="right">11.8%</td>
<td align="right">189</td>
<td align="right">15.8%</td>
<td align="right">350.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">105</td>
<td align="right">29.4%</td>
<td align="right">357</td>
<td align="right">29.8%</td>
<td align="right">240.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">42</td>
<td align="right">11.8%</td>
<td align="right">105</td>
<td align="right">8.8%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">63</td>
<td align="right">17.6%</td>
<td align="right">126</td>
<td align="right">10.5%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">63</td>
<td align="right">17.6%</td>
<td align="right">147</td>
<td align="right">12.3%</td>
<td align="right">133.3%</td>
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
<td align="left"><= 8</td>
<td align="right">42</td>
<td align="right">11.8%</td>
<td align="right">147</td>
<td align="right">12.3%</td>
<td align="right">250.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">105</td>
<td align="right">8.8%</td>
<td align="right">105 / 0 !!</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">63</td>
<td align="right">17.6%</td>
<td align="right">273</td>
<td align="right">22.8%</td>
<td align="right">333.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">126</td>
<td align="right">35.3%</td>
<td align="right">273</td>
<td align="right">22.8%</td>
<td align="right">116.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">84</td>
<td align="right">23.5%</td>
<td align="right">147</td>
<td align="right">12.3%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">42</td>
<td align="right">11.8%</td>
<td align="right">126</td>
<td align="right">10.5%</td>
<td align="right">200.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">63</td>
<td align="right">5.3%</td>
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
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,184</td>
<td align="right">54,663</td>
<td align="right">2,402.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">2,184</td>
<td align="right">37,275</td>
<td align="right">1,606.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">2,184</td>
<td align="right">33,810</td>
<td align="right">1,448.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">6,909</td>
<td align="right">51,093</td>
<td align="right">639.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,846</td>
<td align="right">36,225</td>
<td align="right">429.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">31,416</td>
<td align="right">124,110</td>
<td align="right">295.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">30,576</td>
<td align="right">104,958</td>
<td align="right">243.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,163,967</td>
<td align="right">3,860,472</td>
<td align="right">231.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">31,416</td>
<td align="right">93,072</td>
<td align="right">196.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">228,396</td>
<td align="right">521,976</td>
<td align="right">128.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">607,173</td>
<td align="right">1,197,042</td>
<td align="right">97.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">221,424</td>
<td align="right">415,044</td>
<td align="right">87.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">149,730</td>
<td align="right">271,866</td>
<td align="right">81.6%</td>
</tr>
<tr>
<td align="left">_COPY_1</td>
<td align="right">228,396</td>
<td align="right">414,183</td>
<td align="right">81.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">6,846</td>
<td align="right">12,180</td>
<td align="right">77.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">55,860</td>
<td align="right">83,958</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">172,410</td>
<td align="right">247,611</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">10,729,950</td>
<td align="right">14,821,086</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">10,729,950</td>
<td align="right">14,821,086</td>
<td align="right">38.1%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">11,779,467</td>
<td align="right">16,085,244</td>
<td align="right">36.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right">253,953</td>
<td align="right">341,313</td>
<td align="right">34.4%</td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right">2,285,640</td>
<td align="right">3,009,069</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">1,171,821</td>
<td align="right">1,519,077</td>
<td align="right">29.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">1,648,122</td>
<td align="right">2,086,434</td>
<td align="right">26.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">253,953</td>
<td align="right">318,465</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">299,460</td>
<td align="right">373,842</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">149,730</td>
<td align="right">186,921</td>
<td align="right">24.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">1,361,829</td>
<td align="right">1,690,815</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right">1,084,545</td>
<td align="right">1,345,617</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">1,208,613</td>
<td align="right">1,487,892</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,614,583</td>
<td align="right">4,359,663</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">1,049,517</td>
<td align="right">1,264,158</td>
<td align="right">20.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">2,317,560</td>
<td align="right">2,787,267</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">8,647,905</td>
<td align="right">10,370,535</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">32,535,027</td>
<td align="right">38,008,005</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">6,911,877</td>
<td align="right">8,066,037</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">46,017,321</td>
<td align="right">53,669,574</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,336,083</td>
<td align="right">1,555,428</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">946,995</td>
<td align="right">1,101,807</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right">3,402,105</td>
<td align="right">3,951,066</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">3,402,105</td>
<td align="right">3,951,066</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">3,402,105</td>
<td align="right">3,951,066</td>
<td align="right">16.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">4,540,011</td>
<td align="right">5,256,069</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">4,388,832</td>
<td align="right">5,061,714</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">4,388,832</td>
<td align="right">5,061,714</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,303,742</td>
<td align="right">2,654,820</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">4,593,792</td>
<td align="right">5,285,784</td>
<td align="right">15.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">3,395,196</td>
<td align="right">3,899,973</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">5,897,829</td>
<td align="right">6,735,855</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,577,680</td>
<td align="right">10,886,547</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">1,115,961</td>
<td align="right">1,266,846</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">2,113,734</td>
<td align="right">2,398,767</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">1,391,943</td>
<td align="right">1,572,732</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">2,234,127</td>
<td align="right">2,501,898</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,242,213</td>
<td align="right">1,385,811</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">1,416,387</td>
<td align="right">1,579,872</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">2,251,662</td>
<td align="right">2,508,408</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,251,662</td>
<td align="right">2,508,408</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right">1,614,480</td>
<td align="right">1,776,537</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">1,186,353</td>
<td align="right">1,301,853</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">1,362,711</td>
<td align="right">1,491,882</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,452,419</td>
<td align="right">5,964,063</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">979,524</td>
<td align="right">1,066,317</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">6,467,706</td>
<td align="right">7,015,617</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,210,797</td>
<td align="right">1,299,333</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">1,084,545</td>
<td align="right">1,163,799</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,084,545</td>
<td align="right">1,163,799</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,084,545</td>
<td align="right">1,163,799</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,360,527</td>
<td align="right">1,458,072</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right">2,546,040</td>
<td align="right">2,718,492</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">1,304,667</td>
<td align="right">1,374,114</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">725,571</td>
<td align="right">746,592</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,154,937</td>
<td align="right">1,187,193</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">725,571</td>
<td align="right">742,497</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">725,571</td>
<td align="right">742,497</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right"></td>
<td align="right">259,938</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right"></td>
<td align="right">172,557</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right"></td>
<td align="right">130,515</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">130,515</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right"></td>
<td align="right">98,322</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">98,322</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right"></td>
<td align="right">84,945</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">66,675</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">55,566</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">55,566</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">43,176</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">42,378</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">42,042</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">42,042</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">42,042</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">39,900</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">37,842</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right"></td>
<td align="right">37,842</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">36,183</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right"></td>
<td align="right">29,610</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right"></td>
<td align="right">27,846</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right"></td>
<td align="right">21,588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">21,588</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right"></td>
<td align="right">19,698</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right"></td>
<td align="right">19,698</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right"></td>
<td align="right">18,165</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right"></td>
<td align="right">10,689</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_ISINSTANCE</td>
<td align="right"></td>
<td align="right">8,946</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right"></td>
<td align="right">6,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right"></td>
<td align="right">6,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">6,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right"></td>
<td align="right">6,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP_2</td>
<td align="right"></td>
<td align="right">6,993</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right"></td>
<td align="right">3,297</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right"></td>
<td align="right">3,297</td>
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
