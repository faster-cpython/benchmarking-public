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
<td align="left">UNARY_INVERT</td>
<td align="right">3,579,416</td>
<td align="right">9,647,232</td>
<td align="right">169.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,705,954</td>
<td align="right">6,274,269</td>
<td align="right">131.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">11,831,168</td>
<td align="right">25,533,546</td>
<td align="right">115.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">177,074,535</td>
<td align="right">282,507,856</td>
<td align="right">59.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,802,426</td>
<td align="right">2,873,956</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">492,073,347</td>
<td align="right">765,556,242</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">47,058,483</td>
<td align="right">73,186,628</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">29,408,639</td>
<td align="right">45,015,455</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">74,371,772</td>
<td align="right">38,174,532</td>
<td align="right">-48.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">23,393,569</td>
<td align="right">34,771,081</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">243,461,695</td>
<td align="right">360,401,896</td>
<td align="right">48.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">80,409,122</td>
<td align="right">44,217,825</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">40,648,517</td>
<td align="right">22,606,220</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">350,321</td>
<td align="right">498,194</td>
<td align="right">42.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">111,949,272</td>
<td align="right">157,291,446</td>
<td align="right">40.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">31,252,964</td>
<td align="right">42,802,597</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">114,948,263</td>
<td align="right">157,272,756</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,895,878</td>
<td align="right">46,201,874</td>
<td align="right">36.3%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">882,965</td>
<td align="right">1,199,717</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">327,803,859</td>
<td align="right">444,510,948</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">95,088,616</td>
<td align="right">63,636,087</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,128,030,244</td>
<td align="right">2,820,558,865</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">185,872,000</td>
<td align="right">244,300,516</td>
<td align="right">31.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">120,317,967</td>
<td align="right">155,218,647</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,617,360</td>
<td align="right">22,567,256</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">287,843,993</td>
<td align="right">365,658,428</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">70,851,504</td>
<td align="right">89,466,523</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">135,103,283</td>
<td align="right">170,190,353</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">328,360,862</td>
<td align="right">408,594,686</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,362,455</td>
<td align="right">14,082,893</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">618,884,669</td>
<td align="right">761,188,938</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">97,116,945</td>
<td align="right">119,301,019</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,417,591</td>
<td align="right">65,441,518</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">21,895,055</td>
<td align="right">26,813,535</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">204,303,468</td>
<td align="right">160,639,216</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">57,188,065</td>
<td align="right">69,286,241</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">48,508,339</td>
<td align="right">58,715,248</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">534,905,429</td>
<td align="right">647,277,827</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">288,418,666</td>
<td align="right">348,788,301</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">132,636,790</td>
<td align="right">105,190,697</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">47,246,209</td>
<td align="right">56,838,331</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">298,523,168</td>
<td align="right">358,942,468</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">95,541,086</td>
<td align="right">114,835,089</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">150,115,212</td>
<td align="right">180,303,597</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">183,027,886</td>
<td align="right">147,922,200</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">170,342,171</td>
<td align="right">202,389,412</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">164,991,128</td>
<td align="right">195,936,894</td>
<td align="right">18.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">8,723,623</td>
<td align="right">10,302,062</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">499,541,963</td>
<td align="right">589,557,158</td>
<td align="right">18.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">428,141,976</td>
<td align="right">504,891,595</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">180,792,533</td>
<td align="right">213,100,615</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">671,870,313</td>
<td align="right">791,574,600</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,171,090,276</td>
<td align="right">1,376,220,876</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">223,996,629</td>
<td align="right">263,145,847</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">144,319,183</td>
<td align="right">169,343,576</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">862,163,370</td>
<td align="right">1,008,481,174</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">69,730,696</td>
<td align="right">81,428,179</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">126,731,836</td>
<td align="right">147,729,328</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">34,704,523</td>
<td align="right">40,272,451</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">34,294,950</td>
<td align="right">39,745,573</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">91,578,713</td>
<td align="right">105,864,855</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">84,699,491</td>
<td align="right">97,223,595</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,056,460,272</td>
<td align="right">14,943,105,483</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">89,089,221</td>
<td align="right">101,959,184</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,548,484,869</td>
<td align="right">1,770,890,996</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">57,319,686</td>
<td align="right">65,146,735</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">46,648,146</td>
<td align="right">52,933,772</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">43,556,985</td>
<td align="right">49,420,546</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">453,363,127</td>
<td align="right">514,028,609</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,758,849,734</td>
<td align="right">4,248,424,094</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">90,124,900</td>
<td align="right">101,858,449</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">225,733,221</td>
<td align="right">197,171,690</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">83,788,667</td>
<td align="right">94,311,506</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">265,936,233</td>
<td align="right">299,260,178</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">104,068,882</td>
<td align="right">117,042,734</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,631,044,980</td>
<td align="right">1,829,769,551</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">117,299,297</td>
<td align="right">131,552,782</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,331,590,685</td>
<td align="right">2,609,424,698</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">96,403,201</td>
<td align="right">107,879,792</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">154,440,988</td>
<td align="right">172,731,875</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">771,607,080</td>
<td align="right">861,707,030</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">49,270,359</td>
<td align="right">54,984,838</td>
<td align="right">11.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">54,204,986</td>
<td align="right">60,448,149</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">62,775,004</td>
<td align="right">69,775,507</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">216,778,415</td>
<td align="right">240,507,381</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">56,051,114</td>
<td align="right">62,174,891</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,032,191,881</td>
<td align="right">3,358,150,295</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">49,553,287</td>
<td align="right">54,859,805</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,895,166</td>
<td align="right">290,736,648</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">216,415,899</td>
<td align="right">238,592,675</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,726,686,299</td>
<td align="right">3,004,963,498</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">48,281,371</td>
<td align="right">53,050,224</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,154,567,987</td>
<td align="right">3,457,045,932</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">510,180,415</td>
<td align="right">558,591,087</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">156,930,166</td>
<td align="right">171,769,225</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">264,413,794</td>
<td align="right">288,958,010</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">292,927,883</td>
<td align="right">319,639,257</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">647,912,854</td>
<td align="right">706,985,736</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">474,121,962</td>
<td align="right">512,389,130</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">406,505,171</td>
<td align="right">439,284,060</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">62,709,325</td>
<td align="right">67,662,861</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">401,488,687</td>
<td align="right">431,965,631</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">645,233,356</td>
<td align="right">691,515,031</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">4,068,864</td>
<td align="right">3,802,251</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,078,611,900</td>
<td align="right">2,212,337,715</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">735,220</td>
<td align="right">781,020</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">380,598,590</td>
<td align="right">403,947,406</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,867,959,730</td>
<td align="right">4,101,797,859</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">204,513,212</td>
<td align="right">216,758,291</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">29,494,917</td>
<td align="right">31,233,415</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">214,311,469</td>
<td align="right">201,902,103</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">35,534,223</td>
<td align="right">37,547,809</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">33,731,880</td>
<td align="right">35,630,979</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,675,852</td>
<td align="right">12,912,288</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,924,055,717</td>
<td align="right">2,031,444,288</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">335,209,535</td>
<td align="right">316,724,498</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">56,637,423</td>
<td align="right">59,633,217</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">153,371,650</td>
<td align="right">160,661,345</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,103,868</td>
<td align="right">9,535,120</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,567,146</td>
<td align="right">10,092,044</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,617,529,263</td>
<td align="right">1,690,213,332</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,631,261</td>
<td align="right">9,016,742</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">110,940,587</td>
<td align="right">115,814,440</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,864,626,019</td>
<td align="right">1,943,189,524</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">228,037,584</td>
<td align="right">237,318,467</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">806,029,086</td>
<td align="right">838,730,626</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">68,476,470</td>
<td align="right">71,224,247</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">32,339,376</td>
<td align="right">33,519,396</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">264,080,428</td>
<td align="right">273,339,236</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">115,803,793</td>
<td align="right">119,162,254</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">344,572,621</td>
<td align="right">353,964,127</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,350,427</td>
<td align="right">172,683,388</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,956,772</td>
<td align="right">4,055,751</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">116,627,482</td>
<td align="right">119,494,530</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,924,603</td>
<td align="right">3,840,616</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">115,445,874</td>
<td align="right">113,023,289</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,483,220</td>
<td align="right">67,761,998</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">231,805</td>
<td align="right">235,942</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,840,828</td>
<td align="right">27,241,262</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">57,762,899</td>
<td align="right">58,528,082</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,882</td>
<td align="right">59,548</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">416,952,552</td>
<td align="right">412,950,025</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,455,472,320</td>
<td align="right">4,441,025,822</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,950,554</td>
<td align="right">83,211,061</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">771,232</td>
<td align="right">773,601</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,496,414</td>
<td align="right">23,563,774</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,967,497</td>
<td align="right">8,976,944</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,787,435,701</td>
<td align="right">1,785,995,992</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">75,185,115</td>
<td align="right">75,219,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,709</td>
<td align="right">2,708</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,729</td>
<td align="right">33,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,785,278</td>
<td align="right">1,072,013,561</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,928</td>
<td align="right">405,872</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,875,802</td>
<td align="right">20,877,201</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,919</td>
<td align="right">1,439,855</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,878</td>
<td align="right">120,876</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,125</td>
<td align="right">3,115,090</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,814,144</td>
<td align="right">100,813,452</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,330</td>
<td align="right">14,760,237</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,883</td>
<td align="right">6,169,861</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,546,554</td>
<td align="right">20,546,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,175</td>
<td align="right">20,877,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">153,409,855</td>
<td align="right">153,409,530</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,938</td>
<td align="right">1,645,935</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,376</td>
<td align="right">302,607,376</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,588</td>
<td align="right">128,850,588</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">29,134,740</td>
<td align="right">29,134,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">29,134,440</td>
<td align="right">29,134,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,975</td>
<td align="right">4,866,975</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,140</td>
<td align="right">2,597,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,720</td>
<td align="right">98,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,553</td>
<td align="right">84,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,192</td>
<td align="right">57,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,672</td>
<td align="right">56,672</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,642</td>
<td align="right">3,642</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,752</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">150</td>
<td align="right">150</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">44</td>
<td align="right">44</td>
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
<td align="right">21,769,889</td>
<td align="right">0.3%</td>
<td align="right">35,801,223</td>
<td align="right">0.5%</td>
<td align="right">64.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">327,030,151</td>
<td align="right">4.2%</td>
<td align="right">443,502,515</td>
<td align="right">5.6%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,375,673,203</td>
<td align="right">95.5%</td>
<td align="right">7,387,601,902</td>
<td align="right">93.9%</td>
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
<td align="right">766,626</td>
<td align="right">100.0%</td>
<td align="right">1,001,392</td>
<td align="right">100.0%</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">true divide float</td>
<td align="right">1,324</td>
<td align="right">0.2%</td>
<td align="right">7,167</td>
<td align="right">0.7%</td>
<td align="right">441.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">38,926</td>
<td align="right">5.1%</td>
<td align="right">137,974</td>
<td align="right">13.8%</td>
<td align="right">254.5%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">44,580</td>
<td align="right">5.8%</td>
<td align="right">153,297</td>
<td align="right">15.3%</td>
<td align="right">243.9%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,373</td>
<td align="right">0.7%</td>
<td align="right">11,632</td>
<td align="right">1.2%</td>
<td align="right">116.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,473</td>
<td align="right">0.5%</td>
<td align="right">6,819</td>
<td align="right">0.7%</td>
<td align="right">96.3%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">10,149</td>
<td align="right">1.3%</td>
<td align="right">15,234</td>
<td align="right">1.5%</td>
<td align="right">50.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,572</td>
<td align="right">0.3%</td>
<td align="right">3,290</td>
<td align="right">0.3%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">11,804</td>
<td align="right">1.5%</td>
<td align="right">14,014</td>
<td align="right">1.4%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">495</td>
<td align="right">0.1%</td>
<td align="right">575</td>
<td align="right">0.1%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,987</td>
<td align="right">0.8%</td>
<td align="right">6,847</td>
<td align="right">0.7%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,016</td>
<td align="right">0.7%</td>
<td align="right">5,553</td>
<td align="right">0.6%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,557</td>
<td align="right">2.9%</td>
<td align="right">24,131</td>
<td align="right">2.4%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">807</td>
<td align="right">0.1%</td>
<td align="right">857</td>
<td align="right">0.1%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,364</td>
<td align="right">0.2%</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">6,411</td>
<td align="right">0.8%</td>
<td align="right">6,317</td>
<td align="right">0.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,787</td>
<td align="right">2.6%</td>
<td align="right">20,052</td>
<td align="right">2.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,350</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,568</td>
<td align="right">76.1%</td>
<td align="right">583,823</td>
<td align="right">58.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
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
<td align="right">91,578,713</td>
<td align="right">100.0%</td>
<td align="right">105,864,855</td>
<td align="right">100.0%</td>
<td align="right">15.6%</td>
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
<td align="right">401,350,043</td>
<td align="right">6.8%</td>
<td align="right">431,819,774</td>
<td align="right">7.3%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,826,433</td>
<td align="right">0.1%</td>
<td align="right">5,825,823</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,470,831,184</td>
<td align="right">93.1%</td>
<td align="right">5,470,596,919</td>
<td align="right">92.6%</td>
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
<td align="left">Failure</td>
<td align="right">129,361</td>
<td align="right">52.1%</td>
<td align="right">136,579</td>
<td align="right">53.4%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,022</td>
<td align="right">47.9%</td>
<td align="right">118,992</td>
<td align="right">46.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">6,523</td>
<td align="right">5.0%</td>
<td align="right">7,681</td>
<td align="right">5.6%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">2,924</td>
<td align="right">2.3%</td>
<td align="right">3,254</td>
<td align="right">2.4%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">728</td>
<td align="right">0.6%</td>
<td align="right">808</td>
<td align="right">0.6%</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47,175</td>
<td align="right">36.5%</td>
<td align="right">51,896</td>
<td align="right">38.0%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,479</td>
<td align="right">2.7%</td>
<td align="right">3,651</td>
<td align="right">2.7%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,167</td>
<td align="right">14.0%</td>
<td align="right">18,773</td>
<td align="right">13.7%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">34,884</td>
<td align="right">27.0%</td>
<td align="right">35,035</td>
<td align="right">25.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,447</td>
<td align="right">9.6%</td>
<td align="right">12,447</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.3%</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">120,278,673</td>
<td align="right">1.1%</td>
<td align="right">131,814,469</td>
<td align="right">1.2%</td>
<td align="right">9.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,902,165,557</td>
<td align="right">98.9%</td>
<td align="right">10,879,500,528</td>
<td align="right">98.8%</td>
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
<td align="right">230,197</td>
<td align="right">0.0%</td>
<td align="right">230,181</td>
<td align="right">0.0%</td>
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
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
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
<td align="right">2,461,088</td>
<td align="right">100.0%</td>
<td align="right">2,681,303</td>
<td align="right">100.0%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">569</td>
<td align="right">0.0%</td>
<td align="right">569</td>
<td align="right">0.0%</td>
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
<td align="left">init not simple</td>
<td align="right">752</td>
<td align="right">132.2%</td>
<td align="right">752</td>
<td align="right">132.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">386</td>
<td align="right">67.8%</td>
<td align="right">386</td>
<td align="right">67.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">50.4%</td>
<td align="right">287</td>
<td align="right">50.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">446,694</td>
<td align="right">78.7%</td>
<td align="right">584,207</td>
<td align="right">82.9%</td>
<td align="right">30.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">111,572</td>
<td align="right">19.7%</td>
<td align="right">111,570</td>
<td align="right">15.8%</td>
<td align="right">-0.0%</td>
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
<td align="right">1,125,637</td>
<td align="right">0.0%</td>
<td align="right">1,408,394</td>
<td align="right">0.0%</td>
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
<td align="right">84,583,941</td>
<td align="right">1.8%</td>
<td align="right">97,095,773</td>
<td align="right">2.1%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,517,256,226</td>
<td align="right">98.1%</td>
<td align="right">4,516,248,353</td>
<td align="right">97.9%</td>
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
<td align="right">39,185</td>
<td align="right">28.7%</td>
<td align="right">44,535</td>
<td align="right">28.9%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97,290</td>
<td align="right">71.3%</td>
<td align="right">109,536</td>
<td align="right">71.1%</td>
<td align="right">12.6%</td>
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
<td align="right">340</td>
<td align="right">0.3%</td>
<td align="right">801</td>
<td align="right">0.7%</td>
<td align="right">135.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">807</td>
<td align="right">0.8%</td>
<td align="right">1,809</td>
<td align="right">1.7%</td>
<td align="right">124.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,666</td>
<td align="right">8.9%</td>
<td align="right">11,058</td>
<td align="right">10.1%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">36,639</td>
<td align="right">37.7%</td>
<td align="right">43,697</td>
<td align="right">39.9%</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,121</td>
<td align="right">1.2%</td>
<td align="right">1,321</td>
<td align="right">1.2%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,101</td>
<td align="right">7.3%</td>
<td align="right">7,823</td>
<td align="right">7.1%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,444</td>
<td align="right">6.6%</td>
<td align="right">6,784</td>
<td align="right">6.2%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">959</td>
<td align="right">1.0%</td>
<td align="right">979</td>
<td align="right">0.9%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,078</td>
<td align="right">4.2%</td>
<td align="right">4,119</td>
<td align="right">3.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,162</td>
<td align="right">23.8%</td>
<td align="right">23,172</td>
<td align="right">21.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.9%</td>
<td align="right">7,639</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
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
<td align="right">47,023,907</td>
<td align="right">2.1%</td>
<td align="right">73,145,239</td>
<td align="right">3.2%</td>
<td align="right">55.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,183,245,098</td>
<td align="right">97.8%</td>
<td align="right">2,182,577,122</td>
<td align="right">96.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
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
<td align="right">32,316</td>
<td align="right">100.0%</td>
<td align="right">39,129</td>
<td align="right">100.0%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Success</td>
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
<td align="left">str</td>
<td align="right">8,272</td>
<td align="right">25.6%</td>
<td align="right">12,391</td>
<td align="right">31.7%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,572</td>
<td align="right">23.4%</td>
<td align="right">9,704</td>
<td align="right">24.8%</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,813</td>
<td align="right">33.5%</td>
<td align="right">11,195</td>
<td align="right">28.6%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">5,659</td>
<td align="right">17.5%</td>
<td align="right">5,839</td>
<td align="right">14.9%</td>
<td align="right">3.2%</td>
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
<td align="right">24,234,239</td>
<td align="right">3.3%</td>
<td align="right">48,149,205</td>
<td align="right">6.0%</td>
<td align="right">98.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">117,229,474</td>
<td align="right">16.1%</td>
<td align="right">131,444,128</td>
<td align="right">16.3%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">585,066,201</td>
<td align="right">80.5%</td>
<td align="right">627,012,690</td>
<td align="right">77.7%</td>
<td align="right">7.2%</td>
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
<td align="right">462,180</td>
<td align="right">87.7%</td>
<td align="right">913,364</td>
<td align="right">89.8%</td>
<td align="right">97.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">64,700</td>
<td align="right">12.3%</td>
<td align="right">103,562</td>
<td align="right">10.2%</td>
<td align="right">60.1%</td>
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
<td align="left">dict items</td>
<td align="right">21,433</td>
<td align="right">33.1%</td>
<td align="right">60,212</td>
<td align="right">58.1%</td>
<td align="right">180.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,405</td>
<td align="right">2.2%</td>
<td align="right">2,005</td>
<td align="right">1.9%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,856</td>
<td align="right">10.6%</td>
<td align="right">5,027</td>
<td align="right">4.9%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">263</td>
<td align="right">0.4%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,747</td>
<td align="right">2.7%</td>
<td align="right">1,427</td>
<td align="right">1.4%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,664</td>
<td align="right">14.9%</td>
<td align="right">11,186</td>
<td align="right">10.8%</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,282</td>
<td align="right">3.5%</td>
<td align="right">2,141</td>
<td align="right">2.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,706</td>
<td align="right">7.3%</td>
<td align="right">4,846</td>
<td align="right">4.7%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">2,929</td>
<td align="right">4.5%</td>
<td align="right">3,015</td>
<td align="right">2.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,883</td>
<td align="right">9.1%</td>
<td align="right">5,833</td>
<td align="right">5.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,358</td>
<td align="right">6.7%</td>
<td align="right">4,389</td>
<td align="right">4.2%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,866</td>
<td align="right">4.4%</td>
<td align="right">2,846</td>
<td align="right">2.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.3%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.2%</td>
<td align="right">134</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">496,368,495</td>
<td align="right">3.8%</td>
<td align="right">726,391,680</td>
<td align="right">5.4%</td>
<td align="right">46.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">451,929,707</td>
<td align="right">3.4%</td>
<td align="right">512,524,288</td>
<td align="right">3.8%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,180,417,108</td>
<td align="right">92.8%</td>
<td align="right">12,128,139,486</td>
<td align="right">90.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,401,145</td>
<td align="right">0.0%</td>
<td align="right">1,404,526</td>
<td align="right">0.0%</td>
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
<td align="right">10,575,735</td>
<td align="right">98.0%</td>
<td align="right">14,970,017</td>
<td align="right">98.5%</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">213,339</td>
<td align="right">2.0%</td>
<td align="right">229,827</td>
<td align="right">1.5%</td>
<td align="right">7.7%</td>
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
<td align="right">37,717</td>
<td align="right">17.7%</td>
<td align="right">44,140</td>
<td align="right">19.2%</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">918</td>
<td align="right">0.4%</td>
<td align="right">820</td>
<td align="right">0.4%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">22,172</td>
<td align="right">10.4%</td>
<td align="right">24,509</td>
<td align="right">10.7%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,720</td>
<td align="right">19.1%</td>
<td align="right">44,670</td>
<td align="right">19.4%</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,520</td>
<td align="right">0.7%</td>
<td align="right">1,640</td>
<td align="right">0.7%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">58,758</td>
<td align="right">27.5%</td>
<td align="right">61,734</td>
<td align="right">26.9%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,467</td>
<td align="right">1.2%</td>
<td align="right">2,369</td>
<td align="right">1.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,050</td>
<td align="right">2.4%</td>
<td align="right">4,902</td>
<td align="right">2.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,306</td>
<td align="right">6.7%</td>
<td align="right">14,586</td>
<td align="right">6.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,589</td>
<td align="right">0.7%</td>
<td align="right">1,566</td>
<td align="right">0.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,564</td>
<td align="right">3.5%</td>
<td align="right">7,585</td>
<td align="right">3.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,140</td>
<td align="right">3.8%</td>
<td align="right">8,136</td>
<td align="right">3.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,189</td>
<td align="right">0.6%</td>
<td align="right">1,189</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">400</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">235</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">151</td>
<td align="right">0.1%</td>
<td align="right">151</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property not py function</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">3,833,644,443</td>
<td align="right">99.6%</td>
<td align="right">4,021,111,651</td>
<td align="right">99.6%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,741</td>
<td align="right">0.4%</td>
<td align="right">14,622,683</td>
<td align="right">0.4%</td>
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
<td align="right">1,637</td>
<td align="right">0.0%</td>
<td align="right">1,637</td>
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
<td align="right">53,017</td>
<td align="right">0.0%</td>
<td align="right">53,017</td>
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
<td align="right">138,377</td>
<td align="right">100.0%</td>
<td align="right">138,342</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
<td align="right">65,025,246</td>
<td align="right">100.0%</td>
<td align="right">63,975,337</td>
<td align="right">100.0%</td>
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
<td align="right">254</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
<td align="right">593,288,787</td>
<td align="right">82.2%</td>
<td align="right">593,288,768</td>
<td align="right">82.2%</td>
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
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
<td align="right">128,815,796</td>
<td align="right">17.8%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">14,711</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
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
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">98,194,547</td>
<td align="right">4.9%</td>
<td align="right">126,227,517</td>
<td align="right">6.2%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">55,963,356</td>
<td align="right">2.8%</td>
<td align="right">62,085,657</td>
<td align="right">3.1%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,869,206,810</td>
<td align="right">92.4%</td>
<td align="right">1,843,400,781</td>
<td align="right">90.7%</td>
<td align="right">-1.4%</td>
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
<td align="right">1,894,427</td>
<td align="right">97.7%</td>
<td align="right">2,423,352</td>
<td align="right">98.1%</td>
<td align="right">27.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">45,205</td>
<td align="right">2.3%</td>
<td align="right">46,678</td>
<td align="right">1.9%</td>
<td align="right">3.3%</td>
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
<td align="left">class attr simple</td>
<td align="right">22,988</td>
<td align="right">50.9%</td>
<td align="right">24,477</td>
<td align="right">52.4%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,950</td>
<td align="right">11.0%</td>
<td align="right">4,890</td>
<td align="right">10.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,626</td>
<td align="right">16.9%</td>
<td align="right">7,666</td>
<td align="right">16.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,348</td>
<td align="right">7.4%</td>
<td align="right">3,352</td>
<td align="right">7.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,757</td>
<td align="right">3.9%</td>
<td align="right">1,757</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.6%</td>
<td align="right">1,619</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">913</td>
<td align="right">2.0%</td>
<td align="right">913</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">730</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">699</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">365</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">100</td>
<td align="right">0.2%</td>
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
<td align="right">350,321</td>
<td align="right">100.0%</td>
<td align="right">498,194</td>
<td align="right">100.0%</td>
<td align="right">42.2%</td>
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
<td align="right">89,054,111</td>
<td align="right">8.8%</td>
<td align="right">101,921,013</td>
<td align="right">10.0%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">920,376,672</td>
<td align="right">91.2%</td>
<td align="right">919,708,411</td>
<td align="right">90.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,220</td>
<td align="right">0.0%</td>
<td align="right">2,220</td>
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
<td align="right">32,954</td>
<td align="right">93.8%</td>
<td align="right">36,012</td>
<td align="right">94.2%</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,196</td>
<td align="right">6.2%</td>
<td align="right">2,199</td>
<td align="right">5.8%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">3,306</td>
<td align="right">10.0%</td>
<td align="right">4,707</td>
<td align="right">13.1%</td>
<td align="right">42.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,896</td>
<td align="right">27.0%</td>
<td align="right">10,468</td>
<td align="right">29.1%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">257</td>
<td align="right">0.8%</td>
<td align="right">299</td>
<td align="right">0.8%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">214</td>
<td align="right">0.6%</td>
<td align="right">216</td>
<td align="right">0.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,010</td>
<td align="right">9.1%</td>
<td align="right">3,031</td>
<td align="right">8.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">50.7%</td>
<td align="right">16,723</td>
<td align="right">46.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">32,382,775</td>
<td align="right">0.7%</td>
<td align="right">51,370,475</td>
<td align="right">1.1%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">95,189,980</td>
<td align="right">2.0%</td>
<td align="right">114,295,749</td>
<td align="right">2.4%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,549,426,983</td>
<td align="right">97.3%</td>
<td align="right">4,574,098,045</td>
<td align="right">96.5%</td>
<td align="right">0.5%</td>
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
<td align="right">300,802</td>
<td align="right">31.3%</td>
<td align="right">489,041</td>
<td align="right">32.4%</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">659,825</td>
<td align="right">68.7%</td>
<td align="right">1,018,067</td>
<td align="right">67.6%</td>
<td align="right">54.3%</td>
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
<td align="right">10,341</td>
<td align="right">3.4%</td>
<td align="right">102,517</td>
<td align="right">21.0%</td>
<td align="right">891.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">165,116</td>
<td align="right">54.9%</td>
<td align="right">256,109</td>
<td align="right">52.4%</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,880</td>
<td align="right">1.3%</td>
<td align="right">4,780</td>
<td align="right">1.0%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,256</td>
<td align="right">2.7%</td>
<td align="right">8,673</td>
<td align="right">1.8%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,999</td>
<td align="right">4.0%</td>
<td align="right">12,567</td>
<td align="right">2.6%</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,267</td>
<td align="right">4.4%</td>
<td align="right">13,743</td>
<td align="right">2.8%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">80,447</td>
<td align="right">26.7%</td>
<td align="right">83,124</td>
<td align="right">17.0%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,654</td>
<td align="right">1.9%</td>
<td align="right">5,686</td>
<td align="right">1.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.5%</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">1,427,489</td>
<td align="right">0.1%</td>
<td align="right">1,427,427</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,233,527,852</td>
<td align="right">99.9%</td>
<td align="right">1,233,500,844</td>
<td align="right">99.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,700</td>
<td align="right">0.0%</td>
<td align="right">3,700</td>
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
<td align="right">859</td>
<td align="right">6.9%</td>
<td align="right">865</td>
<td align="right">6.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,651</td>
<td align="right">93.1%</td>
<td align="right">11,643</td>
<td align="right">93.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">632</td>
<td align="right">73.6%</td>
<td align="right">638</td>
<td align="right">73.8%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.5%</td>
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
<td align="right">802,797,170</td>
<td align="right">1.1%</td>
<td align="right">1,129,736,331</td>
<td align="right">1.3%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,909,903,751</td>
<td align="right">2.5%</td>
<td align="right">2,223,380,542</td>
<td align="right">2.6%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">28,446,516,162</td>
<td align="right">37.4%</td>
<td align="right">31,955,449,827</td>
<td align="right">37.9%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">44,863,439,764</td>
<td align="right">59.0%</td>
<td align="right">48,988,514,465</td>
<td align="right">58.1%</td>
<td align="right">9.2%</td>
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
<td align="right">327,030,151</td>
<td align="right">17.2%</td>
<td align="right">443,502,515</td>
<td align="right">20.0%</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">95,189,980</td>
<td align="right">5.0%</td>
<td align="right">114,295,749</td>
<td align="right">5.1%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">91,578,713</td>
<td align="right">4.8%</td>
<td align="right">105,864,855</td>
<td align="right">4.8%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">84,583,941</td>
<td align="right">4.4%</td>
<td align="right">97,095,773</td>
<td align="right">4.4%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">89,054,111</td>
<td align="right">4.7%</td>
<td align="right">101,921,013</td>
<td align="right">4.6%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">451,929,707</td>
<td align="right">23.7%</td>
<td align="right">512,524,288</td>
<td align="right">23.1%</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">117,229,474</td>
<td align="right">6.1%</td>
<td align="right">131,444,128</td>
<td align="right">5.9%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">401,350,043</td>
<td align="right">21.1%</td>
<td align="right">431,819,774</td>
<td align="right">19.5%</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,796</td>
<td align="right">6.8%</td>
<td align="right">128,815,796</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">55,963,356</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">73,145,239</td>
<td align="right">3.3%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">191,585,108</td>
<td align="right">23.9%</td>
<td align="right">305,451,898</td>
<td align="right">27.0%</td>
<td align="right">59.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">127,926,748</td>
<td align="right">15.9%</td>
<td align="right">193,091,737</td>
<td align="right">17.1%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">62,489,684</td>
<td align="right">7.8%</td>
<td align="right">88,772,640</td>
<td align="right">7.9%</td>
<td align="right">42.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">79,110,101</td>
<td align="right">9.9%</td>
<td align="right">104,395,327</td>
<td align="right">9.2%</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">67,217,973</td>
<td align="right">8.4%</td>
<td align="right">84,116,005</td>
<td align="right">7.4%</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">19,050,002</td>
<td align="right">2.4%</td>
<td align="right">21,796,553</td>
<td align="right">1.9%</td>
<td align="right">14.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">63,811,453</td>
<td align="right">7.9%</td>
<td align="right">69,890,465</td>
<td align="right">6.2%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,902</td>
<td align="right">2.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">19,068,708</td>
<td align="right">2.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">15,297,025</td>
<td align="right">1.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,756,756</td>
<td align="right">2.2%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,132,987</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">23,938,511</td>
<td align="right">2.1%</td>
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
<td align="left">Frame objects created</td>
<td align="right">71,804,482</td>
<td align="right">1.1%</td>
<td align="right">71,327,645</td>
<td align="right">1.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,297,149,383</td>
<td align="right">79.1%</td>
<td align="right">5,287,949,224</td>
<td align="right">79.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,902,858,246</td>
<td align="right">73.2%</td>
<td align="right">4,895,291,863</td>
<td align="right">73.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,119,547,496</td>
<td align="right">16.7%</td>
<td align="right">1,117,877,777</td>
<td align="right">16.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,121,679,642</td>
<td align="right">16.8%</td>
<td align="right">1,120,009,923</td>
<td align="right">16.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,792,197,534</td>
<td align="right">26.8%</td>
<td align="right">1,790,491,209</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,792,197,534</td>
<td align="right">26.8%</td>
<td align="right">1,790,491,209</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,335,809</td>
<td align="right">4.2%</td>
<td align="right">279,132,920</td>
<td align="right">4.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,517,892</td>
<td align="right">10.0%</td>
<td align="right">670,481,286</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,313</td>
<td align="right">0.4%</td>
<td align="right">24,922,199</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,406,079</td>
<td align="right">3.9%</td>
<td align="right">261,405,823</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">2,128,250</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">34,060,662,265</td>
<td align="right">20.7%</td>
<td align="right">37,867,173,953</td>
<td align="right">23.1%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">45,803,393,654</td>
<td align="right">22.7%</td>
<td align="right">48,881,082,464</td>
<td align="right">24.3%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,082,008,318</td>
<td align="right">8.0%</td>
<td align="right">17,139,787,862</td>
<td align="right">8.5%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">9,091,871,212</td>
<td align="right">5.5%</td>
<td align="right">9,615,382,993</td>
<td align="right">5.9%</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">79,129,222,308</td>
<td align="right">48.0%</td>
<td align="right">74,620,761,269</td>
<td align="right">45.5%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,903,297</td>
<td align="right"></td>
<td align="right">6,552,212</td>
<td align="right"></td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">84,596,264,922</td>
<td align="right">41.9%</td>
<td align="right">80,805,044,743</td>
<td align="right">40.2%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,995,058,607</td>
<td align="right"></td>
<td align="right">2,079,744,570</td>
<td align="right"></td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,810,097</td>
<td align="right"></td>
<td align="right">64,538,249</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,207,934,664</td>
<td align="right">27.4%</td>
<td align="right">54,260,113,949</td>
<td align="right">27.0%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">59,710,636</td>
<td align="right"></td>
<td align="right">58,792,366</td>
<td align="right"></td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">42,512,007,339</td>
<td align="right">25.8%</td>
<td align="right">42,062,488,856</td>
<td align="right">25.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,944,174</td>
<td align="right"></td>
<td align="right">179,180,537</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,607,096</td>
<td align="right">0.4%</td>
<td align="right">71,499,551</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,445,540,001</td>
<td align="right"></td>
<td align="right">8,438,853,384</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,445,356,882</td>
<td align="right">45.7%</td>
<td align="right">8,438,679,651</td>
<td align="right">45.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,612,124,234</td>
<td align="right"></td>
<td align="right">10,605,530,889</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,022,376,614</td>
<td align="right">54.3%</td>
<td align="right">10,016,562,583</td>
<td align="right">54.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">9,944,348,074</td>
<td align="right">53.8%</td>
<td align="right">9,938,645,153</td>
<td align="right">53.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,421,444</td>
<td align="right">0.0%</td>
<td align="right">6,417,879</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,079,508,912</td>
<td align="right"></td>
<td align="right">3,079,079,459</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">4,444,139</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
<td align="right">476,014</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">4,404</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">363,657</td>
<td align="right">105,878,084</td>
<td align="right">16,485,611,969</td>
<td align="right">363,687</td>
<td align="right">105,816,753</td>
<td align="right">16,483,821,082</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,604,264,380</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,604,228,450</td>
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
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">610,709</td>
<td align="right">75.8%</td>
<td align="right">17,451</td>
<td align="right">31.2%</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">576,371</td>
<td align="right">71.6%</td>
<td align="right">18,350</td>
<td align="right">32.8%</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">805,329</td>
<td align="right"></td>
<td align="right">55,890</td>
<td align="right"></td>
<td align="right">-93.1%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">4,865</td>
<td align="right">0.6%</td>
<td align="right">804</td>
<td align="right">1.4%</td>
<td align="right">-83.5%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">4,782</td>
<td align="right">0.6%</td>
<td align="right">875</td>
<td align="right">1.6%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">193,851</td>
<td align="right">24.1%</td>
<td align="right">38,219</td>
<td align="right">68.4%</td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">1,205</td>
<td align="right">0.6%</td>
<td align="right">340</td>
<td align="right">0.9%</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">769</td>
<td align="right">0.1%</td>
<td align="right">220</td>
<td align="right">0.4%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,679</td>
<td align="right">0.3%</td>
<td align="right">822</td>
<td align="right">1.5%</td>
<td align="right">-69.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,498,492,884</td>
<td align="right"></td>
<td align="right">5,704,559,832</td>
<td align="right"></td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">244,807,763,549</td>
<td align="right">3,767.1%</td>
<td align="right">227,305,271,393</td>
<td align="right">3,984.6%</td>
<td align="right">-7.1%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">193,851</td>
<td align="right"></td>
<td align="right">38,219</td>
<td align="right"></td>
<td align="right">-80.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">173,446</td>
<td align="right">89.5%</td>
<td align="right">34,719</td>
<td align="right">90.8%</td>
<td align="right">-80.0%</td>
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
<td align="right">20,516</td>
<td align="right">10.6%</td>
<td align="right">1,532</td>
<td align="right">4.0%</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">35,660</td>
<td align="right">18.4%</td>
<td align="right">4,136</td>
<td align="right">10.8%</td>
<td align="right">-88.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">57,055</td>
<td align="right">29.4%</td>
<td align="right">13,320</td>
<td align="right">34.9%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">45,126</td>
<td align="right">23.3%</td>
<td align="right">9,972</td>
<td align="right">26.1%</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">24,254</td>
<td align="right">12.5%</td>
<td align="right">4,510</td>
<td align="right">11.8%</td>
<td align="right">-81.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">9,264</td>
<td align="right">4.8%</td>
<td align="right">4,243</td>
<td align="right">11.1%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,934</td>
<td align="right">1.0%</td>
<td align="right">466</td>
<td align="right">1.2%</td>
<td align="right">-75.9%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">42</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">-4.8%</td>
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
<td align="right">3,714</td>
<td align="right">1.9%</td>
<td align="right">346</td>
<td align="right">0.9%</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">29,057</td>
<td align="right">15.0%</td>
<td align="right">4,118</td>
<td align="right">10.8%</td>
<td align="right">-85.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">47,948</td>
<td align="right">24.7%</td>
<td align="right">4,296</td>
<td align="right">11.2%</td>
<td align="right">-91.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">53,514</td>
<td align="right">27.6%</td>
<td align="right">16,109</td>
<td align="right">42.1%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,851</td>
<td align="right">14.4%</td>
<td align="right">6,580</td>
<td align="right">17.2%</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,326</td>
<td align="right">4.3%</td>
<td align="right">2,294</td>
<td align="right">6.0%</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,792</td>
<td align="right">1.4%</td>
<td align="right">934</td>
<td align="right">2.4%</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">244</td>
<td align="right">0.1%</td>
<td align="right">42</td>
<td align="right">0.1%</td>
<td align="right">-82.8%</td>
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
<td align="left">_LOAD_GLOBAL</td>
<td align="right">1,471,814</td>
<td align="right">30,221,279</td>
<td align="right">1,953.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">386,343</td>
<td align="right">1,029</td>
<td align="right">-99.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,258,977</td>
<td align="right">30,963</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">7,705,135</td>
<td align="right">412,098</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">9,812,435</td>
<td align="right">928,997</td>
<td align="right">-90.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">9,866,498</td>
<td align="right">948,031</td>
<td align="right">-90.4%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">40,439,608</td>
<td align="right">76,636,848</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,427,000</td>
<td align="right">6,267,540</td>
<td align="right">-88.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">41,718,835</td>
<td align="right">77,910,132</td>
<td align="right">86.8%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">720,458</td>
<td align="right">98,482</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">21,428,471</td>
<td align="right">39,470,768</td>
<td align="right">84.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,290,652</td>
<td align="right">722,337</td>
<td align="right">-83.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">1,540,733</td>
<td align="right">261,717</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">8,487,377</td>
<td align="right">1,560,563</td>
<td align="right">-81.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">6,630,878</td>
<td align="right">1,401,878</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">14,279,535</td>
<td align="right">4,550,523</td>
<td align="right">-68.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">90,661,250</td>
<td align="right">36,896,802</td>
<td align="right">-59.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">4,861,864</td>
<td align="right">2,113,919</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">499,280,249</td>
<td align="right">223,315,481</td>
<td align="right">-55.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">496,066,229</td>
<td align="right">222,458,721</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">361,285</td>
<td align="right">182,532</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">22,798,907</td>
<td align="right">11,894,240</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">14,268,531</td>
<td align="right">7,793,317</td>
<td align="right">-45.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">503,849,655</td>
<td align="right">276,261,212</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">138,159,950</td>
<td align="right">78,211,706</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">40,781,911</td>
<td align="right">25,175,095</td>
<td align="right">-38.3%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,085,966,301</td>
<td align="right">726,165,090</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">313,404,347</td>
<td align="right">210,753,396</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">71,143,660</td>
<td align="right">48,388,770</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">82,891,636</td>
<td align="right">57,281,700</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">205,345,152</td>
<td align="right">143,659,212</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">46,022,701</td>
<td align="right">32,224,940</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">195,530,050</td>
<td align="right">137,706,787</td>
<td align="right">-29.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">35,910,461</td>
<td align="right">25,703,540</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">35,910,461</td>
<td align="right">25,703,540</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">23,316,013</td>
<td align="right">16,743,768</td>
<td align="right">-28.2%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,605,086</td>
<td align="right">77,936,368</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">336,971,581</td>
<td align="right">246,287,891</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">586,254,385</td>
<td align="right">432,515,282</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,142,574</td>
<td align="right">1,585,924</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">44,967,379</td>
<td align="right">33,428,456</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">7,092,046</td>
<td align="right">5,353,494</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,602,737,214</td>
<td align="right">1,970,994,136</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">108,303,584</td>
<td align="right">82,129,127</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,665,158,898</td>
<td align="right">2,026,380,982</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">105,285,634</td>
<td align="right">80,232,902</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">186,177,558</td>
<td align="right">229,842,297</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,971,905</td>
<td align="right">5,393,399</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">144,939,075</td>
<td align="right">112,314,779</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">222,949,986</td>
<td align="right">176,262,179</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">5,404,528,271</td>
<td align="right">4,363,195,160</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">27,612,207</td>
<td align="right">22,304,981</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,823,904,978</td>
<td align="right">1,482,005,759</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">781,775,044</td>
<td align="right">635,314,070</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">164,255,825</td>
<td align="right">133,905,765</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">63,728,097</td>
<td align="right">52,178,713</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">719,437,933</td>
<td align="right">590,931,508</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">754,760,124</td>
<td align="right">621,671,539</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">411,811,266</td>
<td align="right">339,424,268</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">28,504,171</td>
<td align="right">23,540,041</td>
<td align="right">-17.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,011,083</td>
<td align="right">77,916,334</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,092,582,808</td>
<td align="right">5,055,351,329</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">32,231,384</td>
<td align="right">27,081,837</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">89,779,756</td>
<td align="right">75,493,614</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">723,759,466</td>
<td align="right">610,107,952</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">449,197,160</td>
<td align="right">379,752,003</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">32,896,364</td>
<td align="right">27,845,870</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">210,316,839</td>
<td align="right">178,690,758</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,725,132,319</td>
<td align="right">1,468,002,384</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">102,322,047</td>
<td align="right">87,984,359</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">102,322,047</td>
<td align="right">87,984,359</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,796,441,527</td>
<td align="right">1,545,133,406</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,504,671,031</td>
<td align="right">1,303,162,923</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">60,742,810</td>
<td align="right">52,612,866</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">324,559,056</td>
<td align="right">281,566,579</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">780,728,562</td>
<td align="right">678,639,797</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,234,250</td>
<td align="right">30,629,262</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,234,250</td>
<td align="right">30,629,262</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">72,049,866</td>
<td align="right">62,642,646</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">844,624,624</td>
<td align="right">737,122,507</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,246,214,012</td>
<td align="right">1,093,672,845</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">59,321,463</td>
<td align="right">52,062,355</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">6,498,492,884</td>
<td align="right">5,704,559,832</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,323,881,002</td>
<td align="right">1,162,968,108</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,324,840,965</td>
<td align="right">1,163,949,961</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,638,340,752</td>
<td align="right">4,959,613,045</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">77,612,585</td>
<td align="right">68,295,064</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">605,917,573</td>
<td align="right">533,606,030</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">50,194,148</td>
<td align="right">44,274,190</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,873,064,093</td>
<td align="right">2,536,059,662</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">272,775,229</td>
<td align="right">304,227,362</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,347,292,965</td>
<td align="right">2,077,496,912</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">219,584,669</td>
<td align="right">194,613,528</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">442,620,768</td>
<td align="right">492,750,445</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">403,525,107</td>
<td align="right">357,838,168</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,548,017</td>
<td align="right">21,827,560</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,963,385,581</td>
<td align="right">5,304,422,161</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">256,145,882</td>
<td align="right">284,282,992</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">157,043,888</td>
<td align="right">139,832,082</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">62,091,487</td>
<td align="right">55,384,137</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">260,094,118</td>
<td align="right">232,005,652</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">179,669,437</td>
<td align="right">160,363,157</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">256,949,623</td>
<td align="right">284,500,942</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">603,101,478</td>
<td align="right">538,650,539</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">393,793,617</td>
<td align="right">353,312,205</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">329,501,091</td>
<td align="right">296,431,964</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,404,027,743</td>
<td align="right">1,265,258,999</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">19,159,491</td>
<td align="right">17,292,062</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">662,476,026</td>
<td align="right">597,935,564</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">53,055,820</td>
<td align="right">48,137,260</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">53,055,820</td>
<td align="right">48,137,260</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">62,068,947</td>
<td align="right">56,485,361</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">8,923,401,269</td>
<td align="right">8,149,263,614</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">173,900,874</td>
<td align="right">159,059,823</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,593,203</td>
<td align="right">37,234,744</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,593,823</td>
<td align="right">37,235,584</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">509,323,729</td>
<td align="right">467,255,837</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">72,294,670</td>
<td align="right">66,415,386</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">508,134,256</td>
<td align="right">466,821,592</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,028,405,236</td>
<td align="right">949,659,248</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">202,679,950</td>
<td align="right">187,706,068</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,491,518</td>
<td align="right">67,350,650</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,491,218</td>
<td align="right">67,350,650</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,129,830,622</td>
<td align="right">1,986,653,508</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">716,789,203</td>
<td align="right">669,647,883</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,329,572,619</td>
<td align="right">3,112,482,529</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,882,772,283</td>
<td align="right">1,762,783,128</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,585,250,214</td>
<td align="right">4,294,245,882</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,900,733,595</td>
<td align="right">1,781,693,270</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">118,648,513</td>
<td align="right">111,358,821</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">79,287,400</td>
<td align="right">74,518,486</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,224,083,905</td>
<td align="right">3,034,814,443</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">870,560,107</td>
<td align="right">821,271,254</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">20,577,814,445</td>
<td align="right">19,428,985,340</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">250,537,145</td>
<td align="right">236,895,271</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,037,002,251</td>
<td align="right">981,729,607</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,989,343,565</td>
<td align="right">1,883,591,209</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,089,829,013</td>
<td align="right">4,823,622,593</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">854,228,408</td>
<td align="right">809,718,192</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">26,056,829</td>
<td align="right">24,700,871</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">26,056,829</td>
<td align="right">24,700,871</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">253,175,214</td>
<td align="right">265,812,977</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">188,267,617</td>
<td align="right">178,885,618</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">524,086,366</td>
<td align="right">498,107,424</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,204,291,017</td>
<td align="right">1,146,337,500</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">733,222,181</td>
<td align="right">767,094,147</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,491,102,843</td>
<td align="right">1,423,698,604</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,086,838,702</td>
<td align="right">16,327,979,039</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,372,405,314</td>
<td align="right">1,312,035,864</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,545,203,638</td>
<td align="right">2,438,161,456</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">803,553,965</td>
<td align="right">770,230,292</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,940,794,867</td>
<td align="right">1,861,268,874</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">71,907,700</td>
<td align="right">69,040,660</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">564,266,383</td>
<td align="right">542,062,120</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,706,291,767</td>
<td align="right">2,601,042,299</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,814,475,046</td>
<td align="right">1,745,790,375</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,103,153,937</td>
<td align="right">2,025,338,013</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">124,298,378</td>
<td align="right">119,987,866</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,825,149,695</td>
<td align="right">3,703,323,512</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">388,790,286</td>
<td align="right">376,545,188</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,721,794,260</td>
<td align="right">1,668,329,002</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">31,562,500</td>
<td align="right">32,537,220</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">433,194,136</td>
<td align="right">419,828,497</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,844,140</td>
<td align="right">3,727,380</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,094,593,106</td>
<td align="right">1,062,190,174</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,962,092,797</td>
<td align="right">1,906,200,079</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,604,524,840</td>
<td align="right">4,474,692,051</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">147,828,763</td>
<td align="right">143,660,701</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">728,092,099</td>
<td align="right">707,743,788</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,046,348,625</td>
<td align="right">1,017,609,083</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,464,844,947</td>
<td align="right">3,370,090,904</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">584,158,112</td>
<td align="right">599,985,271</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,950,586,779</td>
<td align="right">2,871,469,012</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,232,112,510</td>
<td align="right">1,199,969,615</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,306,567,719</td>
<td align="right">4,195,909,979</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">93,869,532</td>
<td align="right">96,279,189</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,063,060,318</td>
<td align="right">2,986,445,975</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,996,685</td>
<td align="right">168,851,297</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,376,314,011</td>
<td align="right">8,187,582,456</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,489,880</td>
<td align="right">32,180,940</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">611,826,122</td>
<td align="right">598,959,301</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,685,650</td>
<td align="right">95,786,549</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,359,114,719</td>
<td align="right">1,384,899,440</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,520,065,113</td>
<td align="right">1,548,626,484</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">518,526,656</td>
<td align="right">508,934,295</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">471,604,655</td>
<td align="right">462,897,503</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,565,818</td>
<td align="right">59,494,280</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">118,922,655</td>
<td align="right">116,909,068</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">868,260,255</td>
<td align="right">882,855,613</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,952,612,363</td>
<td align="right">1,922,044,193</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">754,081,568</td>
<td align="right">765,873,826</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,682,714</td>
<td align="right">6,585,627</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,818,138</td>
<td align="right">463,169,484</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,133,931,997</td>
<td align="right">4,180,498,125</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">548,040,083</td>
<td align="right">542,032,588</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,398,524,663</td>
<td align="right">9,297,355,892</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">581,522,480</td>
<td align="right">575,540,259</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">581,503,280</td>
<td align="right">575,540,259</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,457,308</td>
<td align="right">40,056,736</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">994,348,398</td>
<td align="right">984,918,140</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,468,460</td>
<td align="right">123,288,440</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,424,908,385</td>
<td align="right">2,444,703,782</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,353,093,806</td>
<td align="right">1,343,960,644</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">784,542,745</td>
<td align="right">789,805,391</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">168,336,802</td>
<td align="right">167,286,018</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,728,624,668</td>
<td align="right">2,712,207,530</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">750,452,993</td>
<td align="right">753,662,627</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,903,120</td>
<td align="right">3,891,960</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,903,120</td>
<td align="right">3,891,960</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">765,830</td>
<td align="right">764,033</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">765,830</td>
<td align="right">764,033</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,035,925</td>
<td align="right">269,489,725</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,130,180</td>
<td align="right">47,062,820</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,045,563,150</td>
<td align="right">4,039,855,957</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,336,173</td>
<td align="right">112,188,300</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,332,961</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,225,456</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">576,176</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">316,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">45,800</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">19,378</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">9,373</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">2,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">1,353</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">666</td>
<td align="right"></td>
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
<td align="left">CALL</td>
<td align="right">21,258</td>
<td align="right">120</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">35,966</td>
<td align="right">1,944</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">25,869</td>
<td align="right">1,503</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">100</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">21</td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">140</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">140</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,629</td>
<td align="right">22,629</td>
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
<td align="right">31</td>
<td align="right">31</td>
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
<td align="right">38</td>
<td align="right">38</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-21
