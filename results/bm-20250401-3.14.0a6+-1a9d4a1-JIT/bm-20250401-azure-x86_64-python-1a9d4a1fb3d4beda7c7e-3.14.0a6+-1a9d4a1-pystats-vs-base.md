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
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,804,235,096</td>
<td align="right">4,182,332</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,898</td>
<td align="right">1,232,478</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,368,247</td>
<td align="right">2,356,584</td>
<td align="right">-96.2%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,459,950,248</td>
<td align="right">198,661,056</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,026,147</td>
<td align="right">103,938,468</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,578,779,857</td>
<td align="right">238,010,566</td>
<td align="right">-84.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,402,588,491</td>
<td align="right">214,514,519</td>
<td align="right">-84.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,752,356,176</td>
<td align="right">273,688,959</td>
<td align="right">-84.4%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,274,359,485</td>
<td align="right">203,135,833</td>
<td align="right">-84.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,718,770,137</td>
<td align="right">438,602,184</td>
<td align="right">-83.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">565,771,696</td>
<td align="right">96,192,960</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,481,330,117</td>
<td align="right">609,819,229</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,260,114,105</td>
<td align="right">396,882,209</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,132,383,070</td>
<td align="right">377,213,599</td>
<td align="right">-82.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">510,152,259</td>
<td align="right">94,238,822</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,892,517</td>
<td align="right">19,480,018</td>
<td align="right">-78.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,249,253,068</td>
<td align="right">275,162,291</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,713,273</td>
<td align="right">76,714,995</td>
<td align="right">-77.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,825,276</td>
<td align="right">35,854,185</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,932,946,644</td>
<td align="right">697,859,646</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">669,513,270</td>
<td align="right">165,425,475</td>
<td align="right">-75.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,169,500</td>
<td align="right">432,244,296</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">938,256,274</td>
<td align="right">254,197,801</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,283,505,297</td>
<td align="right">2,011,737,459</td>
<td align="right">-72.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">629,915,325</td>
<td align="right">174,277,708</td>
<td align="right">-72.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">194,985,213</td>
<td align="right">54,311,048</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,596,047</td>
<td align="right">146,097,544</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">369,794,392</td>
<td align="right">107,711,218</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,405,877</td>
<td align="right">17,218,808</td>
<td align="right">-70.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">633,856,629</td>
<td align="right">192,375,151</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">375,849,924</td>
<td align="right">115,666,524</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">535,241,100</td>
<td align="right">169,056,465</td>
<td align="right">-68.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,196,064,011</td>
<td align="right">704,629,468</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">114,811,348</td>
<td align="right">36,971,994</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,729,411,968</td>
<td align="right">885,975,452</td>
<td align="right">-67.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">255,714,164</td>
<td align="right">83,468,301</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,114,109,344</td>
<td align="right">365,873,316</td>
<td align="right">-67.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,113,473</td>
<td align="right">185,270,437</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,523,069,103</td>
<td align="right">863,550,511</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,746,476,797</td>
<td align="right">1,987,248,541</td>
<td align="right">-65.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,087,511</td>
<td align="right">55,208,382</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">73,287,138</td>
<td align="right">25,631,232</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">121,581,155</td>
<td align="right">42,974,017</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">355,576,655</td>
<td align="right">125,758,150</td>
<td align="right">-64.6%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">61,804,199</td>
<td align="right">22,180,838</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,529,992,420</td>
<td align="right">910,361,652</td>
<td align="right">-64.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,071,225,148</td>
<td align="right">3,685,504,839</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,397,876,769</td>
<td align="right">4,922,102,708</td>
<td align="right">-63.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,684,696,053</td>
<td align="right">4,033,515,563</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">861,649,442</td>
<td align="right">326,350,781</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,327,533,901</td>
<td align="right">503,600,809</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">152,419,354</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,803,167,778</td>
<td align="right">1,095,373,412</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">436,236,241</td>
<td align="right">170,677,786</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">65,889,657</td>
<td align="right">25,839,473</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,070,828,004</td>
<td align="right">420,503,675</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,104,351</td>
<td align="right">31,033,272</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">266,118,266</td>
<td align="right">107,652,610</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,091,485,162</td>
<td align="right">878,342,623</td>
<td align="right">-58.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,597,140</td>
<td align="right">-57.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,453,011</td>
<td align="right">10,054,248</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">808,959,921</td>
<td align="right">355,448,161</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">404,600,351</td>
<td align="right">177,846,565</td>
<td align="right">-56.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,776,311</td>
<td align="right">44,754,147</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">468,522,117</td>
<td align="right">-55.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">785,913,672</td>
<td align="right">367,624,166</td>
<td align="right">-53.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,100</td>
<td align="right">129,350,852</td>
<td align="right">-52.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">34,112,580,143</td>
<td align="right">16,817,027,042</td>
<td align="right">-50.7%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,189,552,628</td>
<td align="right">3,581,889,158</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,254,367,936</td>
<td align="right">639,328,915</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,206,045,154</td>
<td align="right">635,844,830</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">98,680,749</td>
<td align="right">52,102,120</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">313,238,547</td>
<td align="right">165,457,649</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,388,935</td>
<td align="right">38,535,619</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">546,325,515</td>
<td align="right">296,206,261</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">259,932,419</td>
<td align="right">141,623,045</td>
<td align="right">-45.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,851,796</td>
<td align="right">4,305,764</td>
<td align="right">-45.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">89,759,969</td>
<td align="right">49,262,818</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,500,994,169</td>
<td align="right">843,219,593</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">353,001,811</td>
<td align="right">198,468,993</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">289,258,543</td>
<td align="right">163,450,539</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">200,676,774</td>
<td align="right">113,647,765</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,875,588,227</td>
<td align="right">2,202,234,019</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,359,633</td>
<td align="right">88,312,954</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,865,330</td>
<td align="right">33,380,706</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,058,311,190</td>
<td align="right">615,344,397</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">114,971,899</td>
<td align="right">66,935,506</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">773,662,153</td>
<td align="right">460,859,532</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,490,535,303</td>
<td align="right">1,493,005,464</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,194</td>
<td align="right">114,765,193</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,540,067,465</td>
<td align="right">938,515,816</td>
<td align="right">-39.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,379,617,151</td>
<td align="right">842,788,740</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,731,534</td>
<td align="right">4,724,448</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,180,462,003</td>
<td align="right">1,967,585,298</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">190,502,521</td>
<td align="right">120,152,168</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">823,782,439</td>
<td align="right">555,626,186</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,792,908,587</td>
<td align="right">3,257,518,612</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">67,555,073</td>
<td align="right">46,765,470</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">490,543,678</td>
<td align="right">344,530,611</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">172,842,226</td>
<td align="right">121,479,725</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">399,050,979</td>
<td align="right">282,327,933</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">167,817,394</td>
<td align="right">118,874,989</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">324,734,286</td>
<td align="right">243,275,870</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,295,133,701</td>
<td align="right">2,475,544,224</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">221,387,883</td>
<td align="right">167,956,933</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">824,373,636</td>
<td align="right">645,513,882</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,820,500</td>
<td align="right">1,431,579</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">491,805,544</td>
<td align="right">389,407,021</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,183,316,356</td>
<td align="right">2,534,307,375</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">354,225,440</td>
<td align="right">282,467,758</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,235,904,539</td>
<td align="right">4,990,795,081</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">347,943,740</td>
<td align="right">288,912,178</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,477,823</td>
<td align="right">57,482,514</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,921,517</td>
<td align="right">249,338,605</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">946,767,807</td>
<td align="right">815,733,789</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,864,874</td>
<td align="right">82,298,412</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,348,477,460</td>
<td align="right">4,647,258,365</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">304,485,775</td>
<td align="right">266,720,275</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">555,518,965</td>
<td align="right">491,110,057</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">415,705,644</td>
<td align="right">367,779,812</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,056,186</td>
<td align="right">4,509,433</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,473,756</td>
<td align="right">10,299,496</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">942,972,787</td>
<td align="right">847,228,412</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">71,207,046</td>
<td align="right">64,437,351</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,945,624</td>
<td align="right">57,007,804</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">61,830,030</td>
<td align="right">56,356,641</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">134,351,861</td>
<td align="right">127,160,758</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">76,658,303</td>
<td align="right">72,748,904</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,708</td>
<td align="right">123,859,692</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,615,239</td>
<td align="right">81,371,390</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">68,808,506</td>
<td align="right">70,634,158</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,704</td>
<td align="right">2,644</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,418,540</td>
<td align="right">7,258,206</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,272,780</td>
<td align="right">71,727,492</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,800,980</td>
<td align="right">13,552,642</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,360,967</td>
<td align="right">7,299,137</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">409,312</td>
<td align="right">407,138</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,710,959</td>
<td align="right">7,684,159</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,217,434</td>
<td align="right">67,074,431</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">336,884,651</td>
<td align="right">337,266,160</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">238,015,112</td>
<td align="right">238,191,393</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">240,070,988</td>
<td align="right">240,248,675</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,190</td>
<td align="right">34,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">27,943,956</td>
<td align="right">27,958,562</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,622,481</td>
<td align="right">178,706,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,336</td>
<td align="right">121,291</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,505</td>
<td align="right">5,507</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,230,965</td>
<td align="right">1,113,612,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,682</td>
<td align="right">135,712</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,520,827,625</td>
<td align="right">1,520,491,607</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,268</td>
<td align="right">131,401,017</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,450,884</td>
<td align="right">1,451,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,763,345</td>
<td align="right">14,761,908</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">752,847</td>
<td align="right">752,916</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,265,661</td>
<td align="right">156,271,705</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,630</td>
<td align="right">6,169,648</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,644,274</td>
<td align="right">1,644,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,995,525</td>
<td align="right">20,995,494</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,326,516</td>
<td align="right">21,326,485</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,326,495</td>
<td align="right">21,326,465</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">418,615,580</td>
<td align="right">418,615,276</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,549,611</td>
<td align="right">35,549,587</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">114,894,309</td>
<td align="right">114,894,331</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">591,621,536</td>
<td align="right">591,621,512</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,246,638</td>
<td align="right">302,246,638</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,071</td>
<td align="right">128,850,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">58,270,440</td>
<td align="right">58,270,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,669</td>
<td align="right">41,964,669</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">9,743,071</td>
<td align="right">9,743,071</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,798,023</td>
<td align="right">3,798,023</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,777,442</td>
<td align="right">1,777,442</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">117,444</td>
<td align="right">117,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,601</td>
<td align="right">98,601</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,496</td>
<td align="right">84,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">69,511</td>
<td align="right">69,511</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,207</td>
<td align="right">57,207</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,629</td>
<td align="right">56,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">13,935</td>
<td align="right">13,935</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,265</td>
<td align="right">5,265</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,613</td>
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
<td align="right">153</td>
<td align="right">153</td>
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
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">1,062,589,597</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">851,744,093</td>
<td align="right"></td>
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
<td align="right">2,802,224,748</td>
<td align="right">15.0%</td>
<td align="right">1,094,989,275</td>
<td align="right">6.4%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">58,992,505</td>
<td align="right">0.3%</td>
<td align="right">51,917,781</td>
<td align="right">0.3%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,818,710,754</td>
<td align="right">84.7%</td>
<td align="right">15,837,686,542</td>
<td align="right">93.2%</td>
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
<td align="right">924,976</td>
<td align="right">45.0%</td>
<td align="right">367,127</td>
<td align="right">26.9%</td>
<td align="right">-60.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,130,882</td>
<td align="right">55.0%</td>
<td align="right">996,369</td>
<td align="right">73.1%</td>
<td align="right">-11.9%</td>
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
<td align="right">115,273</td>
<td align="right">12.5%</td>
<td align="right">6,367</td>
<td align="right">1.7%</td>
<td align="right">-94.5%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.2%</td>
<td align="right">16,343</td>
<td align="right">4.5%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">2,767</td>
<td align="right">0.8%</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,193</td>
<td align="right">8.0%</td>
<td align="right">18,485</td>
<td align="right">5.0%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">2,342</td>
<td align="right">0.6%</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">836</td>
<td align="right">0.2%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,510</td>
<td align="right">2.5%</td>
<td align="right">8,298</td>
<td align="right">2.3%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">350,580</td>
<td align="right">37.9%</td>
<td align="right">132,063</td>
<td align="right">36.0%</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,252</td>
<td align="right">0.1%</td>
<td align="right">493</td>
<td align="right">0.1%</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,848</td>
<td align="right">4.7%</td>
<td align="right">22,151</td>
<td align="right">6.0%</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,981</td>
<td align="right">3.7%</td>
<td align="right">19,861</td>
<td align="right">5.4%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">11,552</td>
<td align="right">3.1%</td>
<td align="right">-40.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,620</td>
<td align="right">4.0%</td>
<td align="right">23,120</td>
<td align="right">6.3%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">294</td>
<td align="right">0.0%</td>
<td align="right">209</td>
<td align="right">0.1%</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,514</td>
<td align="right">0.9%</td>
<td align="right">6,194</td>
<td align="right">1.7%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">0.8%</td>
<td align="right">5,754</td>
<td align="right">1.6%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,416</td>
<td align="right">4.7%</td>
<td align="right">36,687</td>
<td align="right">10.0%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,516</td>
<td align="right">5.0%</td>
<td align="right">41,361</td>
<td align="right">11.3%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,996</td>
<td align="right">0.5%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">632</td>
<td align="right">0.1%</td>
<td align="right">638</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">0.3%</td>
<td align="right">3,154</td>
<td align="right">0.9%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,966</td>
<td align="right">0.2%</td>
<td align="right">1,969</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,384</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.2%</td>
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
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">545,113,473</td>
<td align="right">100.0%</td>
<td align="right">185,270,437</td>
<td align="right">100.0%</td>
<td align="right">-66.0%</td>
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
<td align="right">175,897,910</td>
<td align="right">1.6%</td>
<td align="right">150,502,631</td>
<td align="right">1.3%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">172,811,479</td>
<td align="right">1.6%</td>
<td align="right">147,895,383</td>
<td align="right">1.3%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,970,533,526</td>
<td align="right">98.4%</td>
<td align="right">11,011,045,544</td>
<td align="right">98.6%</td>
<td align="right">0.4%</td>
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
<td align="right">3,495,297</td>
<td align="right">100.0%</td>
<td align="right">3,013,940</td>
<td align="right">100.0%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">446</td>
<td align="right">0.0%</td>
<td align="right">446</td>
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
<td align="right">168.6%</td>
<td align="right">752</td>
<td align="right">168.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">267</td>
<td align="right">59.9%</td>
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
<td align="right">684,329</td>
<td align="right">97.1%</td>
<td align="right">684,329</td>
<td align="right">97.1%</td>
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
<td align="right">583,611</td>
<td align="right">82.8%</td>
<td align="right">583,611</td>
<td align="right">82.8%</td>
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
<td align="right">20,498</td>
<td align="right">99.4%</td>
<td align="right">20,453</td>
<td align="right">99.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">0.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">509,922,489</td>
<td align="right">10.2%</td>
<td align="right">94,113,093</td>
<td align="right">2.0%</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,412,838</td>
<td align="right">0.0%</td>
<td align="right">1,293,010</td>
<td align="right">0.0%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,495,314,181</td>
<td align="right">89.8%</td>
<td align="right">4,507,935,408</td>
<td align="right">97.9%</td>
<td align="right">0.3%</td>
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
<td align="right">211,260</td>
<td align="right">82.5%</td>
<td align="right">107,545</td>
<td align="right">71.8%</td>
<td align="right">-49.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">44,839</td>
<td align="right">17.5%</td>
<td align="right">42,262</td>
<td align="right">28.2%</td>
<td align="right">-5.7%</td>
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
<td align="right">90,680</td>
<td align="right">42.9%</td>
<td align="right">4,603</td>
<td align="right">4.3%</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,830</td>
<td align="right">3.2%</td>
<td align="right">369</td>
<td align="right">0.3%</td>
<td align="right">-94.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,451</td>
<td align="right">4.9%</td>
<td align="right">5,956</td>
<td align="right">5.5%</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,270</td>
<td align="right">6.8%</td>
<td align="right">9,325</td>
<td align="right">8.7%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.2%</td>
<td align="right">356</td>
<td align="right">0.3%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,321</td>
<td align="right">0.6%</td>
<td align="right">1,367</td>
<td align="right">1.3%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,564</td>
<td align="right">21.6%</td>
<td align="right">44,054</td>
<td align="right">41.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,995</td>
<td align="right">0.9%</td>
<td align="right">1,971</td>
<td align="right">1.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,840</td>
<td align="right">3.7%</td>
<td align="right">7,752</td>
<td align="right">7.2%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,383</td>
<td align="right">11.1%</td>
<td align="right">23,200</td>
<td align="right">21.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">7,648</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">944</td>
<td align="right">0.4%</td>
<td align="right">944</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">155,297,971</td>
<td align="right">6.6%</td>
<td align="right">88,267,940</td>
<td align="right">3.9%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,187,196,458</td>
<td align="right">93.3%</td>
<td align="right">2,190,329,111</td>
<td align="right">96.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,395,959</td>
<td align="right">0.1%</td>
<td align="right">1,395,959</td>
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
<td align="right">59,343</td>
<td align="right">67.4%</td>
<td align="right">42,895</td>
<td align="right">60.1%</td>
<td align="right">-27.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,662</td>
<td align="right">32.6%</td>
<td align="right">28,462</td>
<td align="right">39.9%</td>
<td align="right">-0.7%</td>
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
<td align="right">21,451</td>
<td align="right">36.1%</td>
<td align="right">9,619</td>
<td align="right">22.4%</td>
<td align="right">-55.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,601</td>
<td align="right">24.6%</td>
<td align="right">12,097</td>
<td align="right">28.2%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,676</td>
<td align="right">19.7%</td>
<td align="right">9,992</td>
<td align="right">23.3%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,615</td>
<td align="right">19.6%</td>
<td align="right">11,187</td>
<td align="right">26.1%</td>
<td align="right">-3.7%</td>
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
<td align="right">1,459,516,450</td>
<td align="right">28.3%</td>
<td align="right">198,541,256</td>
<td align="right">12.5%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,534,078,053</td>
<td align="right">68.5%</td>
<td align="right">1,323,220,610</td>
<td align="right">83.5%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,027,034</td>
<td align="right">3.2%</td>
<td align="right">62,009,191</td>
<td align="right">3.9%</td>
<td align="right">-62.2%</td>
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
<td align="right">428,216</td>
<td align="right">12.1%</td>
<td align="right">114,200</td>
<td align="right">8.9%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,100,256</td>
<td align="right">87.9%</td>
<td align="right">1,175,414</td>
<td align="right">91.1%</td>
<td align="right">-62.1%</td>
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
<td align="left">zip</td>
<td align="right">172,124</td>
<td align="right">40.2%</td>
<td align="right">4,469</td>
<td align="right">3.9%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,793</td>
<td align="right">19.6%</td>
<td align="right">11,069</td>
<td align="right">9.7%</td>
<td align="right">-86.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,997</td>
<td align="right">8.2%</td>
<td align="right">6,420</td>
<td align="right">5.6%</td>
<td align="right">-81.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">-73.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,153</td>
<td align="right">0.7%</td>
<td align="right">1,132</td>
<td align="right">1.0%</td>
<td align="right">-64.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,835</td>
<td align="right">2.5%</td>
<td align="right">4,320</td>
<td align="right">3.8%</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,246</td>
<td align="right">4.3%</td>
<td align="right">8,974</td>
<td align="right">7.9%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,978</td>
<td align="right">0.7%</td>
<td align="right">1,737</td>
<td align="right">1.5%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,501</td>
<td align="right">4.6%</td>
<td align="right">14,175</td>
<td align="right">12.4%</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">69,425</td>
<td align="right">16.2%</td>
<td align="right">50,866</td>
<td align="right">44.5%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,583</td>
<td align="right">1.1%</td>
<td align="right">3,813</td>
<td align="right">3.3%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,930</td>
<td align="right">1.6%</td>
<td align="right">6,510</td>
<td align="right">5.7%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">254</td>
<td align="right">0.1%</td>
<td align="right">254</td>
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
<td align="right">821,933,732</td>
<td align="right">6.0%</td>
<td align="right">553,866,532</td>
<td align="right">4.2%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">865,832,352</td>
<td align="right">6.3%</td>
<td align="right">613,021,313</td>
<td align="right">4.6%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,951,203,224</td>
<td align="right">87.6%</td>
<td align="right">12,116,419,403</td>
<td align="right">91.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,263,438</td>
<td align="right">0.0%</td>
<td align="right">1,263,438</td>
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
<td align="right">16,426,256</td>
<td align="right">96.7%</td>
<td align="right">11,652,258</td>
<td align="right">96.0%</td>
<td align="right">-29.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">559,708</td>
<td align="right">3.3%</td>
<td align="right">491,096</td>
<td align="right">4.0%</td>
<td align="right">-12.3%</td>
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
<td align="left">method</td>
<td align="right">76,806</td>
<td align="right">13.7%</td>
<td align="right">39,966</td>
<td align="right">8.1%</td>
<td align="right">-48.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,201</td>
<td align="right">0.2%</td>
<td align="right">841</td>
<td align="right">0.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,796</td>
<td align="right">10.3%</td>
<td align="right">42,794</td>
<td align="right">8.7%</td>
<td align="right">-26.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,126</td>
<td align="right">1.1%</td>
<td align="right">4,849</td>
<td align="right">1.0%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,737</td>
<td align="right">0.5%</td>
<td align="right">2,377</td>
<td align="right">0.5%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,187</td>
<td align="right">1.6%</td>
<td align="right">8,008</td>
<td align="right">1.6%</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,434</td>
<td align="right">11.9%</td>
<td align="right">61,765</td>
<td align="right">12.6%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,277</td>
<td align="right">4.5%</td>
<td align="right">24,238</td>
<td align="right">4.9%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,668</td>
<td align="right">3.0%</td>
<td align="right">16,315</td>
<td align="right">3.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,777</td>
<td align="right">0.3%</td>
<td align="right">1,803</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,019</td>
<td align="right">0.9%</td>
<td align="right">5,020</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,491</td>
<td align="right">0.3%</td>
<td align="right">1,491</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">400</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">235</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">163</td>
<td align="right">0.0%</td>
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
<td align="right">9,041,557,880</td>
<td align="right">99.8%</td>
<td align="right">4,574,381,074</td>
<td align="right">99.7%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">52,618</td>
<td align="right">0.0%</td>
<td align="right">53,185</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,566</td>
<td align="right">0.2%</td>
<td align="right">14,623,595</td>
<td align="right">0.3%</td>
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
<td align="right">1,502</td>
<td align="right">0.0%</td>
<td align="right">1,502</td>
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
<td align="right">140,554</td>
<td align="right">100.0%</td>
<td align="right">139,088</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">64,396,508</td>
<td align="right">100.0%</td>
<td align="right">64,055,354</td>
<td align="right">100.0%</td>
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
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">251</td>
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
<td align="right">2,453</td>
<td align="right">100.0%</td>
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">591,606,825</td>
<td align="right">82.1%</td>
<td align="right">591,606,801</td>
<td align="right">82.1%</td>
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
<td align="right">128,815,273</td>
<td align="right">17.9%</td>
<td align="right">128,815,273</td>
<td align="right">17.9%</td>
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
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">659</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">34,411</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">3,260</td>
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
<td align="right">113,765,060</td>
<td align="right">5.8%</td>
<td align="right">107,739,180</td>
<td align="right">5.4%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">76,563,546</td>
<td align="right">3.9%</td>
<td align="right">72,656,484</td>
<td align="right">3.7%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,784,952,375</td>
<td align="right">90.4%</td>
<td align="right">1,796,980,959</td>
<td align="right">90.9%</td>
<td align="right">0.7%</td>
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
<td align="right">2,187,593</td>
<td align="right">97.7%</td>
<td align="right">2,072,526</td>
<td align="right">97.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">52,627</td>
<td align="right">2.3%</td>
<td align="right">51,692</td>
<td align="right">2.4%</td>
<td align="right">-1.8%</td>
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
<td align="right">5,942</td>
<td align="right">11.3%</td>
<td align="right">4,963</td>
<td align="right">9.6%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.1%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">271,245</td>
<td align="right">515.4%</td>
<td align="right">264,289</td>
<td align="right">511.3%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,315</td>
<td align="right">10.1%</td>
<td align="right">5,319</td>
<td align="right">10.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,348</td>
<td align="right">6.4%</td>
<td align="right">3,346</td>
<td align="right">6.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.5%</td>
<td align="right">24,476</td>
<td align="right">47.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.6%</td>
<td align="right">7,666</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">814</td>
<td align="right">1.5%</td>
<td align="right">814</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">365</td>
<td align="right">0.7%</td>
<td align="right">365</td>
<td align="right">0.7%</td>
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
<td align="right">112,724,898</td>
<td align="right">100.0%</td>
<td align="right">1,232,478</td>
<td align="right">100.0%</td>
<td align="right">-98.9%</td>
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
<td align="right">700,841,683</td>
<td align="right">43.2%</td>
<td align="right">103,899,838</td>
<td align="right">10.1%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">921,346,131</td>
<td align="right">56.8%</td>
<td align="right">922,611,591</td>
<td align="right">89.9%</td>
<td align="right">0.1%</td>
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
<td align="right">182,262</td>
<td align="right">98.8%</td>
<td align="right">36,550</td>
<td align="right">94.5%</td>
<td align="right">-79.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,242</td>
<td align="right">1.2%</td>
<td align="right">2,120</td>
<td align="right">5.5%</td>
<td align="right">-5.4%</td>
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
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">341</td>
<td align="right">0.9%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,311</td>
<td align="right">2.9%</td>
<td align="right">178</td>
<td align="right">0.5%</td>
<td align="right">-96.6%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">3,483</td>
<td align="right">9.5%</td>
<td align="right">-82.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">10,484</td>
<td align="right">28.7%</td>
<td align="right">-78.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">17,323</td>
<td align="right">47.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,012</td>
<td align="right">1.7%</td>
<td align="right">3,012</td>
<td align="right">8.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,661</td>
<td align="right">0.9%</td>
<td align="right">1,661</td>
<td align="right">4.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">259,250,340</td>
<td align="right">5.1%</td>
<td align="right">141,064,573</td>
<td align="right">3.1%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">110,034,896</td>
<td align="right">2.2%</td>
<td align="right">63,716,859</td>
<td align="right">1.4%</td>
<td align="right">-42.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,722,528,710</td>
<td align="right">92.7%</td>
<td align="right">4,412,331,438</td>
<td align="right">95.6%</td>
<td align="right">-6.6%</td>
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
<td align="right">2,125,973</td>
<td align="right">77.1%</td>
<td align="right">1,251,481</td>
<td align="right">71.1%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">630,591</td>
<td align="right">22.9%</td>
<td align="right">507,505</td>
<td align="right">28.9%</td>
<td align="right">-19.5%</td>
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
<td align="left">bytes</td>
<td align="right">18,877</td>
<td align="right">3.0%</td>
<td align="right">4,678</td>
<td align="right">0.9%</td>
<td align="right">-75.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">133,004</td>
<td align="right">21.1%</td>
<td align="right">33,944</td>
<td align="right">6.7%</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,414</td>
<td align="right">3.2%</td>
<td align="right">15,291</td>
<td align="right">3.0%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">9,220</td>
<td align="right">1.5%</td>
<td align="right">9,733</td>
<td align="right">1.9%</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,590</td>
<td align="right">12.3%</td>
<td align="right">73,801</td>
<td align="right">14.5%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,664</td>
<td align="right">15.5%</td>
<td align="right">96,067</td>
<td align="right">18.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,643</td>
<td align="right">41.0%</td>
<td align="right">258,809</td>
<td align="right">51.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,293</td>
<td align="right">2.1%</td>
<td align="right">13,296</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
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
<td align="right">84</td>
<td align="right">0.0%</td>
<td align="right">84</td>
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
<td align="right">1,809,517</td>
<td align="right">0.1%</td>
<td align="right">1,420,747</td>
<td align="right">0.1%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,240,627,051</td>
<td align="right">99.9%</td>
<td align="right">1,240,816,468</td>
<td align="right">99.9%</td>
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
<td align="right">992</td>
<td align="right">9.0%</td>
<td align="right">861</td>
<td align="right">7.9%</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,071</td>
<td align="right">91.0%</td>
<td align="right">10,051</td>
<td align="right">92.1%</td>
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
<td align="right">758</td>
<td align="right">76.4%</td>
<td align="right">627</td>
<td align="right">72.8%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">98</td>
<td align="right">9.9%</td>
<td align="right">98</td>
<td align="right">11.4%</td>
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
<td align="right">7,593,834,865</td>
<td align="right">3.6%</td>
<td align="right">2,682,600,393</td>
<td align="right">2.7%</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,418,799,617</td>
<td align="right">41.1%</td>
<td align="right">39,667,259,356</td>
<td align="right">40.3%</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">114,803,044,511</td>
<td align="right">54.6%</td>
<td align="right">55,017,067,231</td>
<td align="right">55.9%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,492,141,361</td>
<td align="right">0.7%</td>
<td align="right">1,052,383,559</td>
<td align="right">1.1%</td>
<td align="right">-29.5%</td>
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
<td align="right">1,459,516,450</td>
<td align="right">18.8%</td>
<td align="right">198,541,256</td>
<td align="right">7.0%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,841,683</td>
<td align="right">9.0%</td>
<td align="right">103,899,838</td>
<td align="right">3.7%</td>
<td align="right">-85.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">509,922,489</td>
<td align="right">6.6%</td>
<td align="right">94,113,093</td>
<td align="right">3.3%</td>
<td align="right">-81.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,113,473</td>
<td align="right">7.0%</td>
<td align="right">185,270,437</td>
<td align="right">6.6%</td>
<td align="right">-66.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,802,224,748</td>
<td align="right">36.1%</td>
<td align="right">1,094,989,275</td>
<td align="right">38.7%</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">259,250,340</td>
<td align="right">3.3%</td>
<td align="right">141,064,573</td>
<td align="right">5.0%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,297,971</td>
<td align="right">2.0%</td>
<td align="right">88,267,940</td>
<td align="right">3.1%</td>
<td align="right">-43.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">821,933,732</td>
<td align="right">10.6%</td>
<td align="right">553,866,532</td>
<td align="right">19.6%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">172,811,479</td>
<td align="right">2.2%</td>
<td align="right">147,895,383</td>
<td align="right">5.2%</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,273</td>
<td align="right">1.7%</td>
<td align="right">128,815,273</td>
<td align="right">4.6%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,940,475</td>
<td align="right">5.5%</td>
<td align="right">30,942,046</td>
<td align="right">2.9%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,009,164</td>
<td align="right">5.5%</td>
<td align="right">30,989,750</td>
<td align="right">2.9%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">48,568,633</td>
<td align="right">3.3%</td>
<td align="right">26,705,174</td>
<td align="right">2.5%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,399,424</td>
<td align="right">3.6%</td>
<td align="right">30,006,367</td>
<td align="right">2.9%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,068,655</td>
<td align="right">24.7%</td>
<td align="right">216,878,378</td>
<td align="right">20.6%</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,136,236</td>
<td align="right">17.8%</td>
<td align="right">176,071,785</td>
<td align="right">16.7%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,560,635</td>
<td align="right">5.4%</td>
<td align="right">55,473,486</td>
<td align="right">5.3%</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,262,926</td>
<td align="right">6.3%</td>
<td align="right">88,685,778</td>
<td align="right">8.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">87,398,970</td>
<td align="right">5.9%</td>
<td align="right">82,722,301</td>
<td align="right">7.9%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">85,607,104</td>
<td align="right">5.7%</td>
<td align="right">82,154,508</td>
<td align="right">7.8%</td>
<td align="right">-4.0%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,155,627,432</td>
<td align="right">77.2%</td>
<td align="right">5,164,853,933</td>
<td align="right">77.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,405,587,924</td>
<td align="right">80.9%</td>
<td align="right">5,414,273,191</td>
<td align="right">80.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">273,272,883</td>
<td align="right">4.1%</td>
<td align="right">273,380,427</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">936,141,516</td>
<td align="right">14.0%</td>
<td align="right">935,805,486</td>
<td align="right">14.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">940,418,847</td>
<td align="right">14.1%</td>
<td align="right">940,082,817</td>
<td align="right">14.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,525,319,723</td>
<td align="right">22.8%</td>
<td align="right">1,524,983,705</td>
<td align="right">22.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,525,319,723</td>
<td align="right">22.8%</td>
<td align="right">1,524,983,705</td>
<td align="right">22.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">260,786,904</td>
<td align="right">3.9%</td>
<td align="right">260,794,291</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,892,483</td>
<td align="right">0.4%</td>
<td align="right">24,892,695</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,208,937</td>
<td align="right">1.1%</td>
<td align="right">71,208,861</td>
<td align="right">1.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">584,900,876</td>
<td align="right">8.8%</td>
<td align="right">584,900,888</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,513,402</td>
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
<td align="left">Mortal increfs</td>
<td align="right">25,580,080,309</td>
<td align="right">27.5%</td>
<td align="right">45,122,333,743</td>
<td align="right">46.1%</td>
<td align="right">76.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,756,741,159</td>
<td align="right">28.9%</td>
<td align="right">54,257,666,940</td>
<td align="right">46.9%</td>
<td align="right">70.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,660,292,048</td>
<td align="right">42.6%</td>
<td align="right">25,073,477,337</td>
<td align="right">25.6%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,579,859,469</td>
<td align="right">4.9%</td>
<td align="right">2,931,568,904</td>
<td align="right">3.0%</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,869,222,103</td>
<td align="right">1.7%</td>
<td align="right">1,213,771,981</td>
<td align="right">1.0%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">51,696,195,962</td>
<td align="right">47.0%</td>
<td align="right">34,159,247,895</td>
<td align="right">29.5%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,225,328,343</td>
<td align="right"></td>
<td align="right">2,052,791,334</td>
<td align="right"></td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">23,264,029,555</td>
<td align="right">25.0%</td>
<td align="right">24,716,607,086</td>
<td align="right">25.3%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,576,719,401</td>
<td align="right">22.4%</td>
<td align="right">25,975,471,273</td>
<td align="right">22.5%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,191,385</td>
<td align="right"></td>
<td align="right">59,596,297</td>
<td align="right"></td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">68,534,798</td>
<td align="right"></td>
<td align="right">65,101,309</td>
<td align="right"></td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,149,921</td>
<td align="right"></td>
<td align="right">6,309,420</td>
<td align="right"></td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,441,142</td>
<td align="right">0.4%</td>
<td align="right">71,574,814</td>
<td align="right">0.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,869,971,939</td>
<td align="right"></td>
<td align="right">2,865,914,565</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,416,588</td>
<td align="right">0.0%</td>
<td align="right">6,424,504</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,011,594,124</td>
<td align="right">30.7%</td>
<td align="right">6,016,224,458</td>
<td align="right">30.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,933,736,394</td>
<td align="right">30.3%</td>
<td align="right">5,938,225,140</td>
<td align="right">30.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">13,599,607,771</td>
<td align="right">69.3%</td>
<td align="right">13,608,539,153</td>
<td align="right">69.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">13,599,722,196</td>
<td align="right"></td>
<td align="right">13,608,643,575</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,612,477,365</td>
<td align="right"></td>
<td align="right">6,615,721,975</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,683,396</td>
<td align="right"></td>
<td align="right">168,617,835</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,421</td>
<td align="right">2.6%</td>
<td align="right">4,443,421</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,949</td>
<td align="right">0.3%</td>
<td align="right">475,949</td>
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
<td align="right">364,477</td>
<td align="right">101,996,011</td>
<td align="right">9,541,980,281</td>
<td align="right">765,114,407</td>
<td align="right">764,972,949</td>
<td align="right">364,998</td>
<td align="right">101,790,229</td>
<td align="right">9,581,341,417</td>
<td align="right">768,002,097</td>
<td align="right">767,149,146</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,625,638,544</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,625,889,860</td>
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
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">37</td>
<td align="right">37</td>
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
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">100</td>
<td align="right">100 / 0 !!</td>
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
<td align="right">2,458</td>
<td align="right">2,458</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-04
