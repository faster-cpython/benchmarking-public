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
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,449,942</td>
<td align="right">6,195,460</td>
<td align="right">327.3%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,872,620</td>
<td align="right">51,314,100</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,494,841</td>
<td align="right">28,423,282</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,651,822</td>
<td align="right">57,344,983</td>
<td align="right">-45.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,815,338</td>
<td align="right">36,025,219</td>
<td align="right">-45.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,829,505</td>
<td align="right">36,406,240</td>
<td align="right">-44.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,641</td>
<td align="right">131,737</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,159,281</td>
<td align="right">48,661,142</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">152,920</td>
<td align="right">98,360</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">209,213,710</td>
<td align="right">283,845,297</td>
<td align="right">35.7%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,207</td>
<td align="right">114,158,784</td>
<td align="right">-34.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">291,538,242</td>
<td align="right">380,293,371</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">168,940</td>
<td align="right">118,540</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,502,480</td>
<td align="right">418,390,920</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">128,925,007</td>
<td align="right">101,127,136</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">180,808,740</td>
<td align="right">212,384,393</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">946,947,337</td>
<td align="right">796,995,560</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,635,861</td>
<td align="right">11,485,821</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">104,160</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">193,636,406</td>
<td align="right">164,677,244</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">390,627,389</td>
<td align="right">448,886,167</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,914,870</td>
<td align="right">3,349,338</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,310,641</td>
<td align="right">25,507,101</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,544,952</td>
<td align="right">305,159,109</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">41,580</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,607,489</td>
<td align="right">8,593,872</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">87,424,968</td>
<td align="right">78,740,740</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">762,829,424</td>
<td align="right">688,028,828</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">362,843,600</td>
<td align="right">397,523,251</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">355,725,576</td>
<td align="right">389,624,977</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,150,146</td>
<td align="right">36,061,077</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">1,126,768,271</td>
<td align="right">1,212,931,005</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,286,761</td>
<td align="right">7,664,890</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,272,595</td>
<td align="right">208,790,637</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">983,411,012</td>
<td align="right">1,046,338,696</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,602,186</td>
<td align="right">10,208,153</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">128,736,276</td>
<td align="right">120,777,620</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">381,522,188</td>
<td align="right">404,466,919</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">5,352,624,848</td>
<td align="right">5,655,825,051</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,788,164</td>
<td align="right">263,312,485</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">936,811,611</td>
<td align="right">886,031,452</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,667,996,736</td>
<td align="right">2,530,060,609</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,813,491</td>
<td align="right">42,767,370</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">735,439,529</td>
<td align="right">701,926,227</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">37,817,160</td>
<td align="right">39,484,840</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">860,146,818</td>
<td align="right">895,974,650</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">785,197,401</td>
<td align="right">754,869,245</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">363,821,246</td>
<td align="right">377,487,916</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,260,293,286</td>
<td align="right">3,138,235,509</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,148,079,951</td>
<td align="right">1,107,332,316</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">586,748,391</td>
<td align="right">567,299,470</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">707,547,020</td>
<td align="right">684,547,243</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">2,272,726,069</td>
<td align="right">2,339,568,475</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,900,904</td>
<td align="right">40,907,366</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">147,918,675</td>
<td align="right">151,448,905</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,281,414</td>
<td align="right">32,004,323</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,545,136,591</td>
<td align="right">1,580,175,409</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">366,574,654</td>
<td align="right">374,768,584</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">4,091,902,981</td>
<td align="right">4,000,562,909</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,935,682,240</td>
<td align="right">4,016,212,937</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,800,222</td>
<td align="right">71,318,586</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">105,275,285</td>
<td align="right">107,369,020</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,057,991</td>
<td align="right">130,412,665</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,807,277</td>
<td align="right">72,029,865</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,071,760</td>
<td align="right">81,686,937</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,906,842</td>
<td align="right">47,114,462</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,948,483,644</td>
<td align="right">6,039,829,298</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">104,707,901</td>
<td align="right">106,296,564</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,922,112,974</td>
<td align="right">3,865,432,463</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,269,183,990</td>
<td align="right">1,251,553,172</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">658,852,484</td>
<td align="right">650,003,558</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,753,972</td>
<td align="right">1,776,957</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,287,552</td>
<td align="right">630,303,788</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,499,123</td>
<td align="right">32,909,367</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">198,372,042</td>
<td align="right">195,951,306</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,251,113,940</td>
<td align="right">1,266,260,994</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,482,146</td>
<td align="right">193,477,216</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,248,624,722</td>
<td align="right">2,227,113,710</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">257,970,094</td>
<td align="right">255,622,304</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">393,019,518</td>
<td align="right">396,528,668</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">321,597,855</td>
<td align="right">324,419,248</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,397,266</td>
<td align="right">4,358,756</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">207,293</td>
<td align="right">205,550</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,669,348</td>
<td align="right">47,311,299</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">187,855,440</td>
<td align="right">189,198,625</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,188,292,147</td>
<td align="right">4,217,188,077</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">83,036,279</td>
<td align="right">83,573,282</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">473,013,140</td>
<td align="right">476,060,598</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">171,111,812</td>
<td align="right">172,124,959</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">90,090,528</td>
<td align="right">89,566,748</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">576,539,291</td>
<td align="right">579,888,020</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,780,947,873</td>
<td align="right">5,751,333,206</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">357,420,065</td>
<td align="right">359,108,942</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">110,811,244</td>
<td align="right">111,301,016</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,691,798</td>
<td align="right">58,439,214</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,363,769</td>
<td align="right">103,918,032</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,117</td>
<td align="right">159,228,765</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">716,400</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,925,517</td>
<td align="right">48,721,692</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">659,480,901</td>
<td align="right">662,097,533</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,466,719,983</td>
<td align="right">5,487,153,680</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">185,167,545</td>
<td align="right">185,837,406</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,239,529,087</td>
<td align="right">3,251,165,887</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">111,055,616</td>
<td align="right">111,419,284</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,180,099</td>
<td align="right">19,128,282</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,591,782</td>
<td align="right">94,340,986</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,898,075</td>
<td align="right">53,760,290</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,637,280</td>
<td align="right">90,861,440</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,632,460</td>
<td align="right">90,856,380</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">414,207,464</td>
<td align="right">413,203,102</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,662,406,264</td>
<td align="right">2,656,121,839</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,996,257</td>
<td align="right">67,861,667</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">20,582,704,522</td>
<td align="right">20,542,279,974</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,097,549</td>
<td align="right">397,832,383</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,348,311</td>
<td align="right">2,352,491</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,222,466</td>
<td align="right">216,506,638</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,226,000</td>
<td align="right">40,175,127</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,383,182</td>
<td align="right">1,048,613,159</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,729,708,405</td>
<td align="right">1,727,740,832</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,553,872</td>
<td align="right">221,804,572</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,124,148</td>
<td align="right">22,100,186</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,538,634</td>
<td align="right">17,519,884</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,527,059</td>
<td align="right">49,476,766</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">283,162,994</td>
<td align="right">282,911,103</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">289,075,452</td>
<td align="right">288,820,100</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,254,160</td>
<td align="right">7,248,200</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,684,914</td>
<td align="right">1,364,726,321</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,546,937,865</td>
<td align="right">1,548,069,477</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,782,067</td>
<td align="right">258,597,029</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,073,630</td>
<td align="right">231,218,605</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,484</td>
<td align="right">15,491</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">520,429,793</td>
<td align="right">520,202,827</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,363</td>
<td align="right">190,099,547</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,429,322</td>
<td align="right">17,423,912</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,959,137</td>
<td align="right">12,962,791</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,121,868</td>
<td align="right">91,098,650</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,692</td>
<td align="right">46,599,216</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,472</td>
<td align="right">687,307</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,182</td>
<td align="right">1,872,780</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">900,738,569</td>
<td align="right">900,569,774</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,218,140</td>
<td align="right">33,212,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">727,832,794</td>
<td align="right">727,960,125</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,868,197</td>
<td align="right">10,866,355</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">353,418,229</td>
<td align="right">353,364,083</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,966,897</td>
<td align="right">12,968,851</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,975,837</td>
<td align="right">12,977,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,752,597</td>
<td align="right">81,761,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,318,196</td>
<td align="right">97,309,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,275,744</td>
<td align="right">148,262,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,644,367</td>
<td align="right">9,643,516</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">559,320</td>
<td align="right">559,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,634</td>
<td align="right">173,330,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,210,813</td>
<td align="right">9,210,205</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,283,098</td>
<td align="right">143,287,657</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,916</td>
<td align="right">1,808,952</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,280,677</td>
<td align="right">20,281,078</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,799,408</td>
<td align="right">474,792,347</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">430,685,101</td>
<td align="right">430,679,453</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,382,450</td>
<td align="right">4,382,396</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,641,554</td>
<td align="right">225,644,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,077</td>
<td align="right">786,204,576</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,704,383</td>
<td align="right">555,706,514</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,306,487</td>
<td align="right">233,306,534</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,111</td>
<td align="right">402,022,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,460</td>
<td align="right">38,846,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,760</td>
<td align="right">38,845,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,056,380</td>
<td align="right">12,056,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">8,000,960</td>
<td align="right">8,000,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">8,000,000</td>
<td align="right">8,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,760</td>
<td align="right">3,464,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">142,120</td>
<td align="right">142,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,600</td>
<td align="right">91,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">25,780</td>
<td align="right">25,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">22,580</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">17,080</td>
<td align="right">17,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,960</td>
<td align="right">1,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">720</td>
<td align="right">720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">700</td>
<td align="right">700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">29,500,860</td>
<td align="right">0.3%</td>
<td align="right">27,558,420</td>
<td align="right">0.3%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">420,839,160</td>
<td align="right">4.3%</td>
<td align="right">419,022,709</td>
<td align="right">4.3%</td>
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
<td align="right">9,368,776,590</td>
<td align="right">95.7%</td>
<td align="right">9,372,600,143</td>
<td align="right">95.7%</td>
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
<td align="right">590,776</td>
<td align="right">35.1%</td>
<td align="right">2,153,849</td>
<td align="right">42.5%</td>
<td align="right">264.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,090,442</td>
<td align="right">64.9%</td>
<td align="right">2,910,530</td>
<td align="right">57.5%</td>
<td align="right">166.9%</td>
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
<td align="left">subtract different types</td>
<td align="right">781,613</td>
<td align="right">71.7%</td>
<td align="right">2,377,183</td>
<td align="right">81.7%</td>
<td align="right">204.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,704</td>
<td align="right">7.5%</td>
<td align="right">240,288</td>
<td align="right">8.3%</td>
<td align="right">194.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,946</td>
<td align="right">3.5%</td>
<td align="right">107,823</td>
<td align="right">3.7%</td>
<td align="right">184.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,500</td>
<td align="right">0.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,642</td>
<td align="right">2.7%</td>
<td align="right">28,458</td>
<td align="right">1.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,024</td>
<td align="right">0.5%</td>
<td align="right">4,855</td>
<td align="right">0.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,600</td>
<td align="right">0.1%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,604</td>
<td align="right">0.8%</td>
<td align="right">8,351</td>
<td align="right">0.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">39,304</td>
<td align="right">3.6%</td>
<td align="right">38,168</td>
<td align="right">1.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,213</td>
<td align="right">1.3%</td>
<td align="right">13,874</td>
<td align="right">0.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,480</td>
<td align="right">0.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,747</td>
<td align="right">0.3%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,439</td>
<td align="right">1.1%</td>
<td align="right">12,319</td>
<td align="right">0.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,504</td>
<td align="right">1.0%</td>
<td align="right">10,407</td>
<td align="right">0.4%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,687</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">2.9%</td>
<td align="right">31,928</td>
<td align="right">1.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,549</td>
<td align="right">0.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,897</td>
<td align="right">0.2%</td>
<td align="right">1,893</td>
<td align="right">0.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### BINARY_SLICE

<details>
<summary> specialization stats for BINARY_SLICE family </summary>


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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,741,464</td>
<td align="right">0.0%</td>
<td align="right">1,838,556</td>
<td align="right">0.0%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">736,842,017</td>
<td align="right">10.9%</td>
<td align="right">703,323,088</td>
<td align="right">10.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,014,554,668</td>
<td align="right">89.1%</td>
<td align="right">6,027,686,597</td>
<td align="right">89.5%</td>
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
<td align="left">Success</td>
<td align="right">112,480</td>
<td align="right">33.2%</td>
<td align="right">220,908</td>
<td align="right">50.0%</td>
<td align="right">96.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">226,496</td>
<td align="right">66.8%</td>
<td align="right">220,787</td>
<td align="right">50.0%</td>
<td align="right">-2.5%</td>
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
<td align="left">buffer int</td>
<td align="right">30,257</td>
<td align="right">13.4%</td>
<td align="right">23,500</td>
<td align="right">10.6%</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">43,880</td>
<td align="right">19.4%</td>
<td align="right">45,700</td>
<td align="right">20.7%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.3%</td>
<td align="right">780</td>
<td align="right">0.4%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">127</td>
<td align="right">0.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">7.2%</td>
<td align="right">15,860</td>
<td align="right">7.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.4%</td>
<td align="right">5,280</td>
<td align="right">2.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">109,275</td>
<td align="right">48.2%</td>
<td align="right">108,880</td>
<td align="right">49.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,500</td>
<td align="right">8.6%</td>
<td align="right">19,500</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">1,060</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">100</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">27,384</td>
<td align="right">0.0%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">674,727,282</td>
<td align="right">4.9%</td>
<td align="right">664,289,622</td>
<td align="right">4.8%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">157,916,592</td>
<td align="right">1.2%</td>
<td align="right">156,782,056</td>
<td align="right">1.1%</td>
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
<td align="right">13,007,468,154</td>
<td align="right">95.0%</td>
<td align="right">13,053,972,093</td>
<td align="right">95.1%</td>
<td align="right">0.4%</td>
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
<td align="right">3,445,101</td>
<td align="right">95.2%</td>
<td align="right">12,521,189</td>
<td align="right">98.6%</td>
<td align="right">263.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">174,002</td>
<td align="right">4.8%</td>
<td align="right">174,072</td>
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
<td align="left">class no vectorcall</td>
<td align="right">165,622</td>
<td align="right">95.2%</td>
<td align="right">165,692</td>
<td align="right">95.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">8,040</td>
<td align="right">4.6%</td>
<td align="right">8,040</td>
<td align="right">4.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">2,920</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">340</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="right">735,701</td>
<td align="right">0.0%</td>
<td align="right">576,160</td>
<td align="right">0.0%</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,067,491,163</td>
<td align="right">98.4%</td>
<td align="right">6,083,693,343</td>
<td align="right">98.4%</td>
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
<td align="right">97,860,692</td>
<td align="right">1.6%</td>
<td align="right">97,608,019</td>
<td align="right">1.6%</td>
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
<td align="left">Success</td>
<td align="right">64,123</td>
<td align="right">33.2%</td>
<td align="right">94,100</td>
<td align="right">33.9%</td>
<td align="right">46.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">129,082</td>
<td align="right">66.8%</td>
<td align="right">183,341</td>
<td align="right">66.1%</td>
<td align="right">42.0%</td>
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
<td align="left">big int</td>
<td align="right">26,288</td>
<td align="right">20.4%</td>
<td align="right">64,901</td>
<td align="right">35.4%</td>
<td align="right">146.9%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">25,800</td>
<td align="right">14.1%</td>
<td align="right">141.6%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">920</td>
<td align="right">0.5%</td>
<td align="right">15.0%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">25,054</td>
<td align="right">19.4%</td>
<td align="right">26,327</td>
<td align="right">14.4%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">1,580</td>
<td align="right">0.9%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,379</td>
<td align="right">12.7%</td>
<td align="right">16,035</td>
<td align="right">8.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,680</td>
<td align="right">14.5%</td>
<td align="right">18,420</td>
<td align="right">10.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,365</td>
<td align="right">11.1%</td>
<td align="right">14,181</td>
<td align="right">7.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,710</td>
<td align="right">9.1%</td>
<td align="right">11,594</td>
<td align="right">6.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,426</td>
<td align="right">1.1%</td>
<td align="right">1,423</td>
<td align="right">0.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,580</td>
<td align="right">1.2%</td>
<td align="right">1,580</td>
<td align="right">0.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,458,300</td>
<td align="right">0.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">197,844,258</td>
<td align="right">7.6%</td>
<td align="right">195,638,333</td>
<td align="right">7.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,412,551,901</td>
<td align="right">92.4%</td>
<td align="right">2,416,972,577</td>
<td align="right">92.5%</td>
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
<td align="left">Success</td>
<td align="right">58,800</td>
<td align="right">37.9%</td>
<td align="right">200,399</td>
<td align="right">67.4%</td>
<td align="right">240.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">96,348</td>
<td align="right">62.1%</td>
<td align="right">96,784</td>
<td align="right">32.6%</td>
<td align="right">0.5%</td>
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
<td align="right">12,807</td>
<td align="right">13.3%</td>
<td align="right">14,643</td>
<td align="right">15.1%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">8,340</td>
<td align="right">8.7%</td>
<td align="right">8,120</td>
<td align="right">8.4%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">53,360</td>
<td align="right">55.4%</td>
<td align="right">52,460</td>
<td align="right">54.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">21,841</td>
<td align="right">22.7%</td>
<td align="right">21,561</td>
<td align="right">22.3%</td>
<td align="right">-1.3%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">134,774</td>
<td align="right">0.0%</td>
<td align="right">95,557</td>
<td align="right">0.0%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">461,333,868</td>
<td align="right">49.3%</td>
<td align="right">471,435,830</td>
<td align="right">49.8%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">474,699,939</td>
<td align="right">50.7%</td>
<td align="right">474,646,264</td>
<td align="right">50.2%</td>
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
<td align="right">45,948</td>
<td align="right">19.6%</td>
<td align="right">50,634</td>
<td align="right">21.0%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">188,295</td>
<td align="right">80.4%</td>
<td align="right">191,006</td>
<td align="right">79.0%</td>
<td align="right">1.4%</td>
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
<td align="left">seq iter</td>
<td align="right">2,020</td>
<td align="right">1.1%</td>
<td align="right">1,680</td>
<td align="right">0.9%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,992</td>
<td align="right">5.3%</td>
<td align="right">10,961</td>
<td align="right">5.7%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">520</td>
<td align="right">0.3%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,876</td>
<td align="right">18.5%</td>
<td align="right">37,262</td>
<td align="right">19.5%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,220</td>
<td align="right">0.6%</td>
<td align="right">1,140</td>
<td align="right">0.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,760</td>
<td align="right">2.0%</td>
<td align="right">3,860</td>
<td align="right">2.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,580</td>
<td align="right">1.9%</td>
<td align="right">3,500</td>
<td align="right">1.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,767</td>
<td align="right">5.2%</td>
<td align="right">9,563</td>
<td align="right">5.0%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,840</td>
<td align="right">55.7%</td>
<td align="right">104,840</td>
<td align="right">54.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,500</td>
<td align="right">3.5%</td>
<td align="right">6,500</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">6,240</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">2.3%</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">480</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.1%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">319,560</td>
<td align="right">0.0%</td>
<td align="right">271,060</td>
<td align="right">0.0%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,242,996,826</td>
<td align="right">7.4%</td>
<td align="right">1,285,387,667</td>
<td align="right">7.6%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">265,893,296</td>
<td align="right">1.6%</td>
<td align="right">260,411,263</td>
<td align="right">1.5%</td>
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
<td align="right">15,463,149,126</td>
<td align="right">92.5%</td>
<td align="right">15,553,243,171</td>
<td align="right">92.2%</td>
<td align="right">0.6%</td>
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
<td align="right">5,542,324</td>
<td align="right">87.9%</td>
<td align="right">20,538,994</td>
<td align="right">96.1%</td>
<td align="right">270.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">765,158</td>
<td align="right">12.1%</td>
<td align="right">823,298</td>
<td align="right">3.9%</td>
<td align="right">7.6%</td>
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
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">22,340</td>
<td align="right">2.7%</td>
<td align="right">41.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">45,249</td>
<td align="right">5.9%</td>
<td align="right">59,602</td>
<td align="right">7.2%</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">55,241</td>
<td align="right">7.2%</td>
<td align="right">71,102</td>
<td align="right">8.6%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,720</td>
<td align="right">1.8%</td>
<td align="right">16,940</td>
<td align="right">2.1%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,436</td>
<td align="right">1.8%</td>
<td align="right">14,427</td>
<td align="right">1.8%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">148,925</td>
<td align="right">19.5%</td>
<td align="right">159,134</td>
<td align="right">19.3%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">73,252</td>
<td align="right">9.6%</td>
<td align="right">75,086</td>
<td align="right">9.1%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">75,500</td>
<td align="right">9.9%</td>
<td align="right">76,936</td>
<td align="right">9.3%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,960</td>
<td align="right">3.4%</td>
<td align="right">25,480</td>
<td align="right">3.1%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">250,811</td>
<td align="right">32.8%</td>
<td align="right">255,209</td>
<td align="right">31.0%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,780</td>
<td align="right">0.4%</td>
<td align="right">2,820</td>
<td align="right">0.3%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,120</td>
<td align="right">0.7%</td>
<td align="right">5,060</td>
<td align="right">0.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">12,140</td>
<td align="right">1.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,760</td>
<td align="right">2.6%</td>
<td align="right">19,620</td>
<td align="right">2.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,564</td>
<td align="right">0.7%</td>
<td align="right">5,582</td>
<td align="right">0.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">1,100</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">10,620</td>
<td align="right">0.0%</td>
<td align="right">1,880</td>
<td align="right">0.0%</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">404,269</td>
<td align="right">0.0%</td>
<td align="right">148,165</td>
<td align="right">0.0%</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,613,617,612</td>
<td align="right">99.6%</td>
<td align="right">5,723,517,103</td>
<td align="right">99.6%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,254,639</td>
<td align="right">0.4%</td>
<td align="right">19,995,664</td>
<td align="right">0.3%</td>
<td align="right">-1.3%</td>
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
<td align="right">430,307</td>
<td align="right">100.0%</td>
<td align="right">433,579</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">7,884</td>
<td align="right">0.0%</td>
<td align="right">7,891</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">83,591,433</td>
<td align="right">100.0%</td>
<td align="right">83,603,775</td>
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
<td align="right">7,600</td>
<td align="right">100.0%</td>
<td align="right">7,600</td>
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
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">25,740</td>
<td align="right">0.0%</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,284,294</td>
<td align="right">18.1%</td>
<td align="right">173,285,800</td>
<td align="right">18.1%</td>
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
<td align="right">786,180,417</td>
<td align="right">81.9%</td>
<td align="right">786,178,836</td>
<td align="right">81.9%</td>
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
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">6,840</td>
<td align="right">9.8%</td>
<td align="right">26.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">63,200</td>
<td align="right">90.2%</td>
<td align="right">6.0%</td>
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
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">13,560</td>
<td align="right">21.5%</td>
<td align="right">36.1%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">52.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">22.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.5%</td>
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
<td align="right">98,706,746</td>
<td align="right">3.6%</td>
<td align="right">94,876,189</td>
<td align="right">3.4%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">68,872,467</td>
<td align="right">2.5%</td>
<td align="right">68,271,308</td>
<td align="right">2.5%</td>
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
<td align="right">2,662,786,234</td>
<td align="right">96.4%</td>
<td align="right">2,677,474,570</td>
<td align="right">96.4%</td>
<td align="right">0.6%</td>
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
<td align="right">1,385,267</td>
<td align="right">95.7%</td>
<td align="right">5,335,168</td>
<td align="right">98.8%</td>
<td align="right">285.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,868</td>
<td align="right">4.3%</td>
<td align="right">64,274</td>
<td align="right">1.2%</td>
<td align="right">3.9%</td>
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
<td align="left">not in keys</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">5,440</td>
<td align="right">8.5%</td>
<td align="right">43.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">4,920</td>
<td align="right">7.7%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">2,580</td>
<td align="right">4.2%</td>
<td align="right">2,680</td>
<td align="right">4.2%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">8,720</td>
<td align="right">13.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">13,000</td>
<td align="right">20.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,840</td>
<td align="right">15.9%</td>
<td align="right">9,780</td>
<td align="right">15.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,768</td>
<td align="right">15.8%</td>
<td align="right">9,714</td>
<td align="right">15.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,380</td>
<td align="right">7.1%</td>
<td align="right">4,360</td>
<td align="right">6.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,720</td>
<td align="right">7.6%</td>
<td align="right">4,740</td>
<td align="right">7.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">800</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

### STORE_SLICE

<details>
<summary> specialization stats for STORE_SLICE family </summary>


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
<td align="right">818,399,829</td>
<td align="right">78.0%</td>
<td align="right">820,274,220</td>
<td align="right">78.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">230,971,510</td>
<td align="right">22.0%</td>
<td align="right">231,117,484</td>
<td align="right">22.0%</td>
<td align="right">0.1%</td>
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
<td align="right">91,460</td>
<td align="right">89.6%</td>
<td align="right">90,454</td>
<td align="right">89.5%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,660</td>
<td align="right">10.4%</td>
<td align="right">10,667</td>
<td align="right">10.5%</td>
<td align="right">0.1%</td>
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
<td align="left">bytearray int</td>
<td align="right">920</td>
<td align="right">1.0%</td>
<td align="right">680</td>
<td align="right">0.8%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">760</td>
<td align="right">0.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">6,200</td>
<td align="right">6.9%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,520</td>
<td align="right">8.2%</td>
<td align="right">7,234</td>
<td align="right">8.0%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,540</td>
<td align="right">35.6%</td>
<td align="right">32,380</td>
<td align="right">35.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,200</td>
<td align="right">47.2%</td>
<td align="right">43,200</td>
<td align="right">47.8%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">273,307,962</td>
<td align="right">4.5%</td>
<td align="right">252,744,925</td>
<td align="right">4.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">49,314,233</td>
<td align="right">0.8%</td>
<td align="right">48,046,191</td>
<td align="right">0.8%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,769,794,598</td>
<td align="right">95.5%</td>
<td align="right">5,779,750,626</td>
<td align="right">95.7%</td>
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
<td align="left">Success</td>
<td align="right">1,107,100</td>
<td align="right">86.6%</td>
<td align="right">3,870,801</td>
<td align="right">94.6%</td>
<td align="right">249.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">171,766</td>
<td align="right">13.4%</td>
<td align="right">221,102</td>
<td align="right">5.4%</td>
<td align="right">28.7%</td>
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
<td align="left">dict</td>
<td align="right">12,780</td>
<td align="right">7.4%</td>
<td align="right">25,800</td>
<td align="right">11.7%</td>
<td align="right">101.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,451</td>
<td align="right">2.6%</td>
<td align="right">8,880</td>
<td align="right">4.0%</td>
<td align="right">99.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">47,963</td>
<td align="right">27.9%</td>
<td align="right">74,904</td>
<td align="right">33.9%</td>
<td align="right">56.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">4,801</td>
<td align="right">2.8%</td>
<td align="right">6,986</td>
<td align="right">3.2%</td>
<td align="right">45.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,197</td>
<td align="right">7.7%</td>
<td align="right">8,005</td>
<td align="right">3.6%</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,034</td>
<td align="right">26.8%</td>
<td align="right">51,503</td>
<td align="right">23.3%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,843</td>
<td align="right">15.6%</td>
<td align="right">29,421</td>
<td align="right">13.3%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,777</td>
<td align="right">7.4%</td>
<td align="right">12,683</td>
<td align="right">5.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.2%</td>
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
<td align="right">186,472</td>
<td align="right">0.0%</td>
<td align="right">103,572</td>
<td align="right">0.0%</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,498,372,953</td>
<td align="right">100.0%</td>
<td align="right">1,499,360,366</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">1,777</td>
<td align="right">6.3%</td>
<td align="right">1,733</td>
<td align="right">6.2%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">26,392</td>
<td align="right">93.7%</td>
<td align="right">26,432</td>
<td align="right">93.8%</td>
<td align="right">0.2%</td>
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
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">340</td>
<td align="right">19.6%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,137</td>
<td align="right">64.0%</td>
<td align="right">1,133</td>
<td align="right">65.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">15.0%</td>
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
<td align="right">654,939,109</td>
<td align="right">0.6%</td>
<td align="right">644,089,773</td>
<td align="right">0.6%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,358,870,492</td>
<td align="right">9.7%</td>
<td align="right">11,531,819,660</td>
<td align="right">9.9%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">63,868,427,923</td>
<td align="right">54.6%</td>
<td align="right">63,573,497,834</td>
<td align="right">54.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">41,101,312,053</td>
<td align="right">35.1%</td>
<td align="right">41,272,468,015</td>
<td align="right">35.3%</td>
<td align="right">0.4%</td>
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
<td align="right">273,307,962</td>
<td align="right">5.9%</td>
<td align="right">252,744,925</td>
<td align="right">5.5%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">736,842,017</td>
<td align="right">15.9%</td>
<td align="right">703,323,088</td>
<td align="right">15.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,242,996,826</td>
<td align="right">26.8%</td>
<td align="right">1,285,387,667</td>
<td align="right">27.9%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">674,727,282</td>
<td align="right">14.5%</td>
<td align="right">664,289,622</td>
<td align="right">14.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,844,258</td>
<td align="right">4.3%</td>
<td align="right">195,638,333</td>
<td align="right">4.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">420,839,160</td>
<td align="right">9.1%</td>
<td align="right">419,022,709</td>
<td align="right">9.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">230,971,510</td>
<td align="right">5.0%</td>
<td align="right">231,117,484</td>
<td align="right">5.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,699,939</td>
<td align="right">10.2%</td>
<td align="right">474,646,264</td>
<td align="right">10.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,294</td>
<td align="right">3.7%</td>
<td align="right">173,285,800</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,706,746</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">97,608,019</td>
<td align="right">2.1%</td>
<td align="right"></td>
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
<td align="right">85,151,162</td>
<td align="right">11.6%</td>
<td align="right">92,612,379</td>
<td align="right">12.8%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,491,256</td>
<td align="right">3.8%</td>
<td align="right">29,218,396</td>
<td align="right">4.0%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">70,358,359</td>
<td align="right">9.6%</td>
<td align="right">66,296,656</td>
<td align="right">9.2%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">23,948,394</td>
<td align="right">3.3%</td>
<td align="right">23,143,160</td>
<td align="right">3.2%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,209,466</td>
<td align="right">3.4%</td>
<td align="right">24,657,062</td>
<td align="right">3.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,979,227</td>
<td align="right">5.6%</td>
<td align="right">41,769,859</td>
<td align="right">5.8%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">121,603,786</td>
<td align="right">16.6%</td>
<td align="right">122,048,100</td>
<td align="right">16.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,643,581</td>
<td align="right">6.0%</td>
<td align="right">43,599,540</td>
<td align="right">6.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,877,533</td>
<td align="right">10.6%</td>
<td align="right">77,878,057</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,877,533</td>
<td align="right">10.6%</td>
<td align="right">77,878,057</td>
<td align="right">10.8%</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,077,904</td>
<td align="right">10.4%</td>
<td align="right">851,474,317</td>
<td align="right">10.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">370,214,465</td>
<td align="right">4.5%</td>
<td align="right">371,734,776</td>
<td align="right">4.5%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,636,331,129</td>
<td align="right">67.9%</td>
<td align="right">5,657,972,383</td>
<td align="right">68.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,664,850,370</td>
<td align="right">32.1%</td>
<td align="right">2,658,586,950</td>
<td align="right">32.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,664,850,370</td>
<td align="right">32.1%</td>
<td align="right">2,658,586,950</td>
<td align="right">32.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,597,463,218</td>
<td align="right">79.5%</td>
<td align="right">6,612,000,817</td>
<td align="right">79.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,907,575</td>
<td align="right">6.3%</td>
<td align="right">527,694,653</td>
<td align="right">6.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,800,338,246</td>
<td align="right">21.7%</td>
<td align="right">1,802,678,413</td>
<td align="right">21.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,804,772,466</td>
<td align="right">21.7%</td>
<td align="right">1,807,112,633</td>
<td align="right">21.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,562,129</td>
<td align="right">0.9%</td>
<td align="right">71,603,269</td>
<td align="right">0.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,577,731</td>
<td align="right">0.3%</td>
<td align="right">28,577,581</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,937</td>
<td align="right">2.5%</td>
<td align="right">211,357,856</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">4,411,640</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,580</td>
<td align="right">0.0%</td>
<td align="right">22,580</td>
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
<td align="left">Method cache misses</td>
<td align="right">23,335,836</td>
<td align="right"></td>
<td align="right">20,072,658</td>
<td align="right"></td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">28,465,326</td>
<td align="right"></td>
<td align="right">24,685,572</td>
<td align="right"></td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,639,280</td>
<td align="right"></td>
<td align="right">7,119,162</td>
<td align="right"></td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">68,126,886,856</td>
<td align="right">42.8%</td>
<td align="right">68,477,180,619</td>
<td align="right">43.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">50,676,523,147</td>
<td align="right">37.0%</td>
<td align="right">50,891,996,910</td>
<td align="right">37.2%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">91,132,688,274</td>
<td align="right">57.2%</td>
<td align="right">90,760,018,690</td>
<td align="right">57.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,627,061,534</td>
<td align="right"></td>
<td align="right">2,637,374,038</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">86,143,901,757</td>
<td align="right">63.0%</td>
<td align="right">85,885,270,006</td>
<td align="right">62.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">150,004,920</td>
<td align="right"></td>
<td align="right">150,243,646</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,882,731</td>
<td align="right">0.5%</td>
<td align="right">104,038,714</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,379,142,873</td>
<td align="right">55.1%</td>
<td align="right">12,395,064,210</td>
<td align="right">55.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,255,146,752</td>
<td align="right">54.5%</td>
<td align="right">12,270,906,228</td>
<td align="right">54.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,108,105,674</td>
<td align="right"></td>
<td align="right">13,124,558,997</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">10,108,261,579</td>
<td align="right"></td>
<td align="right">10,115,545,982</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">10,106,455,058</td>
<td align="right">44.9%</td>
<td align="right">10,113,712,136</td>
<td align="right">44.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,285,674,303</td>
<td align="right"></td>
<td align="right">4,288,530,280</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,113,390</td>
<td align="right">0.1%</td>
<td align="right">20,119,268</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">3,270,980</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
<td align="right">63,660</td>
<td align="right">0.0%</td>
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
<th align="right">Head Collections</th>
<th align="right">Head Objects collected</th>
<th align="right">Head Object visits</th>
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
</tr>
<tr>
<td align="right">1</td>
<td align="right">0</td>
<td align="right">18,574,860</td>
<td align="right">18,450,468,217</td>
<td align="right">0</td>
<td align="right">19,271,820</td>
<td align="right">18,477,588,046</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,985,714,352</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,991,677,896</td>
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
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">85.7%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,339</td>
<td align="right">5.9%</td>
<td align="right">8,688</td>
<td align="right">7.2%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">45,084</td>
<td align="right">4.0%</td>
<td align="right">55,288</td>
<td align="right">4.6%</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">107,257</td>
<td align="right">9.5%</td>
<td align="right">120,252</td>
<td align="right">10.1%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">774</td>
<td align="right">0.1%</td>
<td align="right">839</td>
<td align="right">0.1%</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,360</td>
<td align="right">0.1%</td>
<td align="right">1,260</td>
<td align="right">0.1%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,129,749</td>
<td align="right"></td>
<td align="right">1,196,381</td>
<td align="right"></td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">1,022,492</td>
<td align="right">90.5%</td>
<td align="right">1,076,129</td>
<td align="right">89.9%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">10,649,478,376</td>
<td align="right"></td>
<td align="right">10,301,663,849</td>
<td align="right"></td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">429,614</td>
<td align="right">38.0%</td>
<td align="right">441,750</td>
<td align="right">36.9%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">11,964</td>
<td align="right">1.1%</td>
<td align="right">12,247</td>
<td align="right">1.0%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">243,064,916,270</td>
<td align="right">2,282.4%</td>
<td align="right">243,472,438,057</td>
<td align="right">2,363.4%</td>
<td align="right">0.2%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,307</td>
<td align="right">2.2%</td>
<td align="right">1,443</td>
<td align="right">1.2%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">107,257</td>
<td align="right"></td>
<td align="right">120,252</td>
<td align="right"></td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">96,283</td>
<td align="right">89.8%</td>
<td align="right">107,461</td>
<td align="right">89.4%</td>
<td align="right">11.6%</td>
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
</tbody>
</table>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,497</td>
<td align="right">4.2%</td>
<td align="right">5,477</td>
<td align="right">4.6%</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,691</td>
<td align="right">17.4%</td>
<td align="right">22,241</td>
<td align="right">18.5%</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">30,699</td>
<td align="right">28.6%</td>
<td align="right">33,182</td>
<td align="right">27.6%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">26,255</td>
<td align="right">24.5%</td>
<td align="right">33,155</td>
<td align="right">27.6%</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">19,210</td>
<td align="right">17.9%</td>
<td align="right">17,313</td>
<td align="right">14.4%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">6,265</td>
<td align="right">5.8%</td>
<td align="right">7,084</td>
<td align="right">5.9%</td>
<td align="right">13.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,480</td>
<td align="right">1.4%</td>
<td align="right">1,520</td>
<td align="right">1.3%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.1%</td>
<td align="right">280</td>
<td align="right">0.2%</td>
<td align="right">75.0%</td>
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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 2</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">3,637</td>
<td align="right">3.4%</td>
<td align="right">4,242</td>
<td align="right">3.5%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,166</td>
<td align="right">12.3%</td>
<td align="right">15,063</td>
<td align="right">12.5%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,323</td>
<td align="right">19.9%</td>
<td align="right">24,790</td>
<td align="right">20.6%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,544</td>
<td align="right">29.4%</td>
<td align="right">33,681</td>
<td align="right">28.0%</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,988</td>
<td align="right">14.9%</td>
<td align="right">18,221</td>
<td align="right">15.2%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,765</td>
<td align="right">7.2%</td>
<td align="right">8,544</td>
<td align="right">7.1%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,500</td>
<td align="right">2.3%</td>
<td align="right">2,380</td>
<td align="right">2.0%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">50.0%</td>
</tr>
</tbody>
</table>


</details>

### Trace run length histogram

<details>
<summary> trace run length histogram </summary>

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
<td align="left"><= 1</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
</tbody>
</table>


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
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,600</td>
<td align="right">48,075,880</td>
<td align="right">67,045.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,935,140</td>
<td align="right">50,687,739</td>
<td align="right">2,519.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,881,420</td>
<td align="right">26,175,859</td>
<td align="right">1,291.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">7,891,700</td>
<td align="right">35,717,840</td>
<td align="right">352.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">7,908,960</td>
<td align="right">35,755,760</td>
<td align="right">352.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,104</td>
<td align="right">93,884,425</td>
<td align="right">167.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,284,220</td>
<td align="right">55,492,980</td>
<td align="right">149.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,200</td>
<td align="right">36,960</td>
<td align="right">114.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">632,240</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">47,971,805</td>
<td align="right">77,503,663</td>
<td align="right">61.6%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">2,594,320</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">101,766,725</td>
<td align="right">132,930,906</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,759</td>
<td align="right">130,983,879</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,450,825</td>
<td align="right">114,337,718</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,693,445</td>
<td align="right">114,351,838</td>
<td align="right">28.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,890,167</td>
<td align="right">6,273,483</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">5,920</td>
<td align="right">-22.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">254,195,677</td>
<td align="right">309,054,960</td>
<td align="right">21.6%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">255,422,937</td>
<td align="right">310,283,420</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,320</td>
<td align="right">174,744,160</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,957</td>
<td align="right">534,484</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">394,350,361</td>
<td align="right">320,823,180</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">177,786,632</td>
<td align="right">148,581,424</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">310,680</td>
<td align="right">361,080</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">377,042,977</td>
<td align="right">431,989,322</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">39,820</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,714,202</td>
<td align="right">24,150,407</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">33,760</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,220</td>
<td align="right">9,147,732</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,837,130</td>
<td align="right">13,269,259</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,837,130</td>
<td align="right">13,269,199</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">356,981,585</td>
<td align="right">399,730,927</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">66,409,000</td>
<td align="right">59,316,800</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">284,761,601</td>
<td align="right">256,167,071</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,320,910,996</td>
<td align="right">1,444,291,945</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,900,740</td>
<td align="right">124,556,083</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">879,901,674</td>
<td align="right">953,075,996</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">48,452,136</td>
<td align="right">44,508,512</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">324,854,500</td>
<td align="right">350,751,129</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,356,801</td>
<td align="right">300,803,925</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,089,013,738</td>
<td align="right">2,237,865,624</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">22,125,122</td>
<td align="right">20,557,205</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">143,097,600</td>
<td align="right">153,222,978</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,358,178</td>
<td align="right">189,597,239</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,740</td>
<td align="right">245,912,580</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,165,160</td>
<td align="right">1,246,751,340</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">812,167,060</td>
<td align="right">863,335,856</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,816,320</td>
<td align="right">65,558,660</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,980</td>
<td align="right">539,649,360</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">181,440,994</td>
<td align="right">191,890,048</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,363,291,560</td>
<td align="right">1,285,868,919</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,008,916,926</td>
<td align="right">951,797,909</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,626,644</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,838,476</td>
<td align="right">62,959,587</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">118,201,830</td>
<td align="right">112,211,645</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,682,070,184</td>
<td align="right">1,597,153,360</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">979,271,000</td>
<td align="right">929,959,901</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,196,660</td>
<td align="right">63,003,280</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,202,175</td>
<td align="right">10,648,079</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,857,895,888</td>
<td align="right">1,936,117,524</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,419,443,505</td>
<td align="right">6,152,897,801</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,882,938,681</td>
<td align="right">1,959,918,505</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,011,997,181</td>
<td align="right">6,731,961,127</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,631,513,223</td>
<td align="right">10,003,947,266</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,473,323</td>
<td align="right">1,899,322,050</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,275,700</td>
<td align="right">56,286,440</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">3,689,699,957</td>
<td align="right">3,555,222,387</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">47,925,363</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,137,802,251</td>
<td align="right">1,175,500,401</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">915,799,664</td>
<td align="right">945,528,888</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,312,809,783</td>
<td align="right">1,354,540,985</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,639,420</td>
<td align="right">5,818,220</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">91,603,958</td>
<td align="right">94,478,699</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,668,569</td>
<td align="right">90,765,868</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,237,856,971</td>
<td align="right">1,275,937,401</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,959,778,419</td>
<td align="right">6,746,441,462</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,919,950,421</td>
<td align="right">1,978,583,538</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,256,514,871</td>
<td align="right">1,294,748,741</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,607,815,454</td>
<td align="right">1,656,700,553</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">55,427,243</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">768,189,561</td>
<td align="right">745,422,321</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,668,476,866</td>
<td align="right">1,713,854,726</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,805,072,861</td>
<td align="right">1,854,041,455</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">136,618,409</td>
<td align="right">140,209,976</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,353,257,866</td>
<td align="right">3,270,621,138</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">715,596,860</td>
<td align="right">732,799,461</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,605,808,328</td>
<td align="right">1,643,796,978</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,278,464,453</td>
<td align="right">1,308,558,469</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,171,814,384</td>
<td align="right">3,098,017,130</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,464,767,505</td>
<td align="right">3,537,970,482</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,901,801,789</td>
<td align="right">2,844,381,655</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,588,753</td>
<td align="right">136,174,299</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">189,156,291</td>
<td align="right">185,994,163</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,759,260</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,063,456,431</td>
<td align="right">3,013,568,607</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,919,540</td>
<td align="right">1,950,780</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,224,014</td>
<td align="right">10,064,832</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,636,040</td>
<td align="right">5,723,000</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">186,631,161</td>
<td align="right">183,849,543</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,458,440,852</td>
<td align="right">2,493,765,484</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,832,917,328</td>
<td align="right">1,807,030,670</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">832,540</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,359,690,921</td>
<td align="right">4,418,384,950</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,673,615,833</td>
<td align="right">3,626,462,905</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,252,530,015</td>
<td align="right">2,225,319,286</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,629,806,818</td>
<td align="right">2,598,243,174</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,259,580,589</td>
<td align="right">4,208,756,356</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">123,481,860</td>
<td align="right">122,039,416</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">757,720,615</td>
<td align="right">749,102,105</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,066,274</td>
<td align="right">135,565,512</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,066,274</td>
<td align="right">135,565,512</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,615,336,888</td>
<td align="right">5,674,808,298</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,011,617,415</td>
<td align="right">1,022,320,744</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">995,672,507</td>
<td align="right">985,802,964</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">911,410,895</td>
<td align="right">920,361,631</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">227,252,215</td>
<td align="right">229,458,714</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">325,040</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,108,670,322</td>
<td align="right">6,052,108,852</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,071,639,103</td>
<td align="right">12,951,734,212</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,257,044</td>
<td align="right">68,880,525</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">402,727,108</td>
<td align="right">399,074,745</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,692,029</td>
<td align="right">162,349,863</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,240,716,778</td>
<td align="right">2,258,799,998</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">58,046,140</td>
<td align="right">57,584,940</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">320,746,905</td>
<td align="right">323,206,619</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,217,836,318</td>
<td align="right">2,201,674,198</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">563,517,331</td>
<td align="right">567,582,080</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">17,077,204,306</td>
<td align="right">17,192,167,673</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">57,936,640</td>
<td align="right">57,567,960</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">236,350,590</td>
<td align="right">234,878,736</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,671,180</td>
<td align="right">3,693,860</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,758,092</td>
<td align="right">228,509,417</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,912,335</td>
<td align="right">1,922,686</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,316,460</td>
<td align="right">2,328,882</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,337,596</td>
<td align="right">125,666,780</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">151,028,334</td>
<td align="right">151,805,009</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">894,041,979</td>
<td align="right">898,501,958</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,166,306,037</td>
<td align="right">2,156,556,019</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">968,234,221</td>
<td align="right">964,068,374</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,651,520</td>
<td align="right">100,070,980</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">552,813,730</td>
<td align="right">555,122,936</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,046,151,575</td>
<td align="right">1,050,319,595</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,246,323</td>
<td align="right">233,168,986</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">71,374,736</td>
<td align="right">71,632,301</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,022,520</td>
<td align="right">22,095,720</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,560</td>
<td align="right">186,973,840</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,350,361</td>
<td align="right">401,565,183</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,305,801</td>
<td align="right">361,332,963</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,442,678</td>
<td align="right">93,706,149</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">89,301,471</td>
<td align="right">89,552,469</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,490,271</td>
<td align="right">78,705,481</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">343,046,207</td>
<td align="right">343,858,697</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">113,064,322</td>
<td align="right">113,329,731</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,738,660</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,460</td>
<td align="right">213,137,680</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">587,168,800</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">625,206,322</td>
<td align="right">626,442,848</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">14,915,925,571</td>
<td align="right">14,945,218,275</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">31,156,961</td>
<td align="right">31,114,790</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">682,868,769</td>
<td align="right">682,020,136</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,077,412,199</td>
<td align="right">1,076,165,998</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,392,920,025</td>
<td align="right">6,386,060,731</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,706,160</td>
<td align="right">908,730,421</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,031,029</td>
<td align="right">199,240,720</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">859,989,614</td>
<td align="right">860,894,141</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,839,512</td>
<td align="right">227,609,784</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">543,917,483</td>
<td align="right">544,371,020</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,236,239,510</td>
<td align="right">1,237,194,604</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">3,628,057</td>
<td align="right">3,625,380</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,059,300</td>
<td align="right">532,666,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">96,436,761</td>
<td align="right">96,502,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,524,967,947</td>
<td align="right">1,525,967,499</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,372,602</td>
<td align="right">930,960,074</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,140</td>
<td align="right">12,701,120</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,496,302</td>
<td align="right">1,817,373,079</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,101,632,564</td>
<td align="right">1,100,998,814</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,612,704,056</td>
<td align="right">3,614,698,402</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,814,089,741</td>
<td align="right">1,813,146,565</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,437,459</td>
<td align="right">330,597,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,235,777</td>
<td align="right">733,587,591</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,293,202</td>
<td align="right">779,648,955</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,523,412</td>
<td align="right">173,601,872</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,831,507,082</td>
<td align="right">2,830,277,100</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,830,522</td>
<td align="right">780,167,355</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">958,914,872</td>
<td align="right">958,518,919</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,105,665,634</td>
<td align="right">2,106,374,624</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,200,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,627,730,051</td>
<td align="right">4,628,830,769</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">643,367,742</td>
<td align="right">643,221,006</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,894,464,828</td>
<td align="right">1,894,889,749</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,171,800</td>
<td align="right">98,193,697</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">148,684,969</td>
<td align="right">148,712,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,214,460</td>
<td align="right">97,232,517</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">646,922,174</td>
<td align="right">647,015,973</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,198,267</td>
<td align="right">101,210,177</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,735,043,050</td>
<td align="right">4,735,499,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,207</td>
<td align="right">645,019,277</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,300</td>
<td align="right">543,260</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,401,138</td>
<td align="right">32,403,274</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,571,440</td>
<td align="right">80,575,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,874,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">384,647,781</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">6,229,902,657</td>
<td align="right">6,230,022,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right"></td>
<td align="right">420</td>
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
<td align="left">IMPORT_NAME</td>
<td align="right">2,399</td>
<td align="right">4,720</td>
<td align="right">96.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">640</td>
<td align="right">77.8%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,620</td>
<td align="right">2,840</td>
<td align="right">75.3%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">540</td>
<td align="right">920</td>
<td align="right">70.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">480</td>
<td align="right">640</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,495</td>
<td align="right">8,331</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">300</td>
<td align="right">220</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">29,100</td>
<td align="right">34,420</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,344</td>
<td align="right">6,100</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,979</td>
<td align="right">46,256</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">479,045</td>
<td align="right">501,817</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,360</td>
<td align="right">2,260</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">33,340</td>
<td align="right">34,060</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">1,089</td>
<td align="right">1,167</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,089</td>
<td align="right">1,167</td>
<td align="right">7.2%</td>
</tr>
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
<td align="right">240</td>
<td align="right">240</td>
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
<td align="right">360</td>
<td align="right">360</td>
<td align="right">0.0%</td>
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
<td align="right">1,880</td>
<td align="right">1,880</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-06-20
