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
<td align="right">1,598,709</td>
<td align="right">2,354,455</td>
<td align="right">47.3%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">312,449,879</td>
<td align="right">191,673,400</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">1,715,084</td>
<td align="right">2,254,773</td>
<td align="right">31.5%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,449,952</td>
<td align="right">1,219,379</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">39,470,013</td>
<td align="right">34,713,563</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">217,176,869</td>
<td align="right">193,028,970</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">80,686,960</td>
<td align="right">72,556,378</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,140,321</td>
<td align="right">6,572,737</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">382,901,368</td>
<td align="right">356,634,527</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">506,544,576</td>
<td align="right">476,899,405</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,153,538</td>
<td align="right">40,005,269</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,591,029</td>
<td align="right">6,879,177</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,298,642,196</td>
<td align="right">2,214,605,093</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">352,849,776</td>
<td align="right">341,723,088</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,096,074,320</td>
<td align="right">1,072,526,403</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,774,346</td>
<td align="right">1,808,904</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">886,463,555</td>
<td align="right">870,240,513</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,462,315</td>
<td align="right">9,602,779</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,340,734</td>
<td align="right">17,556,730</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,884,366,602</td>
<td align="right">4,825,586,680</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,840,537,530</td>
<td align="right">1,818,859,645</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,312,233</td>
<td align="right">270,303,564</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">474,820</td>
<td align="right">479,620</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">80,950,780</td>
<td align="right">81,708,357</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">372,340,861</td>
<td align="right">368,869,450</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,905,856,095</td>
<td align="right">4,865,776,621</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,106,737</td>
<td align="right">272,989,555</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">101,760,578</td>
<td align="right">102,456,493</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,915,272,526</td>
<td align="right">18,791,874,734</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">168,763,209</td>
<td align="right">169,851,388</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">84,644,062</td>
<td align="right">85,188,259</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,922,593,965</td>
<td align="right">4,890,967,348</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">151,680</td>
<td align="right">152,640</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,042,433</td>
<td align="right">53,377,247</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,309,434</td>
<td align="right">57,946,847</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">37,815,788</td>
<td align="right">37,586,640</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">355,798,120</td>
<td align="right">353,667,196</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">110,523,087</td>
<td align="right">111,098,547</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">202,643,640</td>
<td align="right">203,622,852</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">105,633,325</td>
<td align="right">106,069,401</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">571,510,606</td>
<td align="right">573,836,902</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">977,951,931</td>
<td align="right">981,620,219</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">382,838,531</td>
<td align="right">384,201,901</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,580,037</td>
<td align="right">9,613,205</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">697,003,616</td>
<td align="right">699,276,263</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,582,358,040</td>
<td align="right">1,577,214,914</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,854,791</td>
<td align="right">39,731,721</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">421,090,856</td>
<td align="right">422,310,988</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">284,905,822</td>
<td align="right">285,717,021</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,223,134,255</td>
<td align="right">1,226,554,176</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">129,928,345</td>
<td align="right">129,576,521</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,592,365</td>
<td align="right">70,423,343</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,860,598</td>
<td align="right">84,061,346</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">141,800</td>
<td align="right">142,120</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">472,914,123</td>
<td align="right">473,976,519</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">211,237,682</td>
<td align="right">211,688,580</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">288,494,834</td>
<td align="right">289,107,982</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,061,324</td>
<td align="right">183,679,865</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">289,414,997</td>
<td align="right">290,009,781</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">115,893,231</td>
<td align="right">116,129,170</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">327,234,894</td>
<td align="right">327,899,548</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">187,634,420</td>
<td align="right">187,988,329</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,207,137,788</td>
<td align="right">2,211,287,826</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">283,480,646</td>
<td align="right">284,010,688</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,454,957</td>
<td align="right">7,468,605</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,218,931,613</td>
<td align="right">3,224,673,658</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">414,683,682</td>
<td align="right">413,965,423</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">366,827,357</td>
<td align="right">367,419,138</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,888,516</td>
<td align="right">67,997,181</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">96,871,455</td>
<td align="right">97,020,033</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,521,092</td>
<td align="right">150,751,244</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,693,059</td>
<td align="right">72,801,134</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,812,461</td>
<td align="right">65,717,788</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">391,726,765</td>
<td align="right">392,281,169</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,807,064,819</td>
<td align="right">3,812,360,406</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,457,798,987</td>
<td align="right">5,464,789,619</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,170,697,019</td>
<td align="right">4,175,955,668</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,086,330,891</td>
<td align="right">3,082,593,067</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,630,342</td>
<td align="right">75,715,890</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,113,187</td>
<td align="right">33,150,300</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">580,211,745</td>
<td align="right">580,862,007</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">320,969,445</td>
<td align="right">320,621,560</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">246,176,688</td>
<td align="right">245,924,676</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,987,256,251</td>
<td align="right">3,983,276,634</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,382,093,843</td>
<td align="right">2,384,230,271</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">586,043,825</td>
<td align="right">586,566,749</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,946,889</td>
<td align="right">12,957,869</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,954,649</td>
<td align="right">12,965,629</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,143,329,977</td>
<td align="right">1,144,282,810</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,037,084</td>
<td align="right">225,222,309</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,963,946</td>
<td align="right">12,974,541</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,661,263,669</td>
<td align="right">2,663,110,095</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">378,451,562</td>
<td align="right">378,706,444</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">944,995,480</td>
<td align="right">945,625,223</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">957,653,865</td>
<td align="right">958,270,201</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,332,979</td>
<td align="right">1,046,743,987</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,546,943</td>
<td align="right">258,689,543</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,378,965</td>
<td align="right">221,499,258</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,753,807</td>
<td align="right">1,754,629</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,961,400</td>
<td align="right">48,981,205</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,032,690</td>
<td align="right">122,073,890</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,810,645</td>
<td align="right">215,882,334</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">343,580,551</td>
<td align="right">343,692,895</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,207,345</td>
<td align="right">9,210,261</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,641,597</td>
<td align="right">9,644,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,057,373</td>
<td align="right">622,237,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,606,231</td>
<td align="right">94,633,024</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,445</td>
<td align="right">15,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,664,203</td>
<td align="right">18,668,749</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,723,539</td>
<td align="right">278,787,603</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,396,533</td>
<td align="right">31,402,097</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,412,191</td>
<td align="right">195,440,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,384,000</td>
<td align="right">4,384,336</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">250,940,163</td>
<td align="right">250,921,157</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,253,060,161</td>
<td align="right">1,252,969,227</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">134,513,804</td>
<td align="right">134,523,136</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,244</td>
<td align="right">1,873,115</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,133,974</td>
<td align="right">22,135,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,411,544</td>
<td align="right">47,414,483</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,445,004</td>
<td align="right">356,465,843</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">399,866,447</td>
<td align="right">399,889,431</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,102,419</td>
<td align="right">91,107,464</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,486,661</td>
<td align="right">52,489,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,064,851</td>
<td align="right">83,069,385</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,363,601,035</td>
<td align="right">1,363,674,134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,461</td>
<td align="right">687,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,420</td>
<td align="right">214,410</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,641,622</td>
<td align="right">105,646,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,868,760</td>
<td align="right">98,872,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,030,002</td>
<td align="right">397,044,695</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,628,560</td>
<td align="right">90,631,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,633,700</td>
<td align="right">90,636,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,309,441</td>
<td align="right">22,310,081</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,599,900</td>
<td align="right">104,602,876</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">207,275</td>
<td align="right">207,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,152,752</td>
<td align="right">78,154,350</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,217,343</td>
<td align="right">33,218,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,498,350</td>
<td align="right">32,498,981</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,693,348</td>
<td align="right">555,703,473</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">56,321,099</td>
<td align="right">56,321,925</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,867,626</td>
<td align="right">10,867,777</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,279,568</td>
<td align="right">20,279,291</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">104,828,905</td>
<td align="right">104,829,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,037,445</td>
<td align="right">190,039,363</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,498,130</td>
<td align="right">326,499,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">189,363,126</td>
<td align="right">189,363,713</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,642,429</td>
<td align="right">13,642,461</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,554,005</td>
<td align="right">158,553,753</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,276,385</td>
<td align="right">148,276,598</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,588</td>
<td align="right">46,610,652</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,905,878</td>
<td align="right">47,905,891</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,829,453</td>
<td align="right">65,829,437</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,300,167</td>
<td align="right">143,300,137</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,305,686</td>
<td align="right">233,305,639</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,043</td>
<td align="right">786,211,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,239</td>
<td align="right">172,973,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,586</td>
<td align="right">173,318,578</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,206</td>
<td align="right">228,622,198</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,089</td>
<td align="right">402,022,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,527,058</td>
<td align="right">49,527,059</td>
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
<td align="right">12,084,360</td>
<td align="right">12,084,360</td>
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
<td align="left">STORE_SLICE</td>
<td align="right">7,254,160</td>
<td align="right">7,254,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,464,720</td>
<td align="right">3,464,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">543,600</td>
<td align="right">543,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">150,560</td>
<td align="right">150,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,600</td>
<td align="right">91,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">90,000</td>
<td align="right">90,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">46,620</td>
<td align="right">46,620</td>
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
<td align="right">22,520</td>
<td align="right">22,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,020</td>
<td align="right">2,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,000</td>
<td align="right">2,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">900</td>
<td align="right">900</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">410,724,808</td>
<td align="right">5.7%</td>
<td align="right">384,465,877</td>
<td align="right">5.3%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,805,209,837</td>
<td align="right">94.3%</td>
<td align="right">6,805,589,827</td>
<td align="right">94.6%</td>
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
<td align="right">29,500,860</td>
<td align="right">0.4%</td>
<td align="right">29,500,860</td>
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
<td align="right">1,086,877</td>
<td align="right">64.8%</td>
<td align="right">1,079,076</td>
<td align="right">64.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">590,543</td>
<td align="right">35.2%</td>
<td align="right">590,434</td>
<td align="right">35.4%</td>
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
<td align="left">rshift</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">6,442</td>
<td align="right">0.6%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">7,221</td>
<td align="right">0.7%</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,154</td>
<td align="right">1.3%</td>
<td align="right">12,594</td>
<td align="right">1.2%</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,190</td>
<td align="right">2.7%</td>
<td align="right">26,422</td>
<td align="right">2.4%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">12,177</td>
<td align="right">1.1%</td>
<td align="right">12,471</td>
<td align="right">1.2%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,507</td>
<td align="right">0.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,887</td>
<td align="right">3.5%</td>
<td align="right">37,929</td>
<td align="right">3.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,026</td>
<td align="right">0.5%</td>
<td align="right">5,021</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,721</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,716</td>
<td align="right">3.4%</td>
<td align="right">36,736</td>
<td align="right">3.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,896</td>
<td align="right">0.2%</td>
<td align="right">1,897</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,096</td>
<td align="right">3.0%</td>
<td align="right">32,084</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,464</td>
<td align="right">1.0%</td>
<td align="right">10,461</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,604</td>
<td align="right">7.5%</td>
<td align="right">81,601</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,605</td>
<td align="right">71.9%</td>
<td align="right">781,609</td>
<td align="right">72.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">10,620</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">2,680</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">2,640</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">416,164,789</td>
<td align="right">8.9%</td>
<td align="right">415,446,792</td>
<td align="right">8.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,278,511,076</td>
<td align="right">91.1%</td>
<td align="right">4,278,753,481</td>
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
<td align="right">1,740,995</td>
<td align="right">0.0%</td>
<td align="right">1,740,987</td>
<td align="right">0.0%</td>
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
<td align="right">147,787</td>
<td align="right">56.9%</td>
<td align="right">147,533</td>
<td align="right">56.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">112,101</td>
<td align="right">43.1%</td>
<td align="right">112,085</td>
<td align="right">43.2%</td>
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
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">121</td>
<td align="right">0.1%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">43,760</td>
<td align="right">29.6%</td>
<td align="right">43,440</td>
<td align="right">29.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,215</td>
<td align="right">20.4%</td>
<td align="right">30,257</td>
<td align="right">20.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">30,708</td>
<td align="right">20.8%</td>
<td align="right">30,735</td>
<td align="right">20.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,520</td>
<td align="right">13.2%</td>
<td align="right">19,520</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,200</td>
<td align="right">11.0%</td>
<td align="right">16,200</td>
<td align="right">11.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">3.6%</td>
<td align="right">5,340</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">1,060</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">760</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.1%</td>
<td align="right">100</td>
<td align="right">0.1%</td>
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
<td align="right">10,628,596,946</td>
<td align="right">97.3%</td>
<td align="right">10,637,282,702</td>
<td align="right">97.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">286,775,649</td>
<td align="right">2.6%</td>
<td align="right">286,983,994</td>
<td align="right">2.6%</td>
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
<td align="right">174,714,280</td>
<td align="right">1.6%</td>
<td align="right">174,686,474</td>
<td align="right">1.6%</td>
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
<td align="right">28,860</td>
<td align="right">0.0%</td>
<td align="right">28,860</td>
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
<td align="right">73,998</td>
<td align="right">1.9%</td>
<td align="right">74,340</td>
<td align="right">1.9%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,757,864</td>
<td align="right">98.1%</td>
<td align="right">3,757,310</td>
<td align="right">98.1%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">7,980</td>
<td align="right">10.8%</td>
<td align="right">8,020</td>
<td align="right">10.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">65,678</td>
<td align="right">88.8%</td>
<td align="right">65,980</td>
<td align="right">88.8%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">3.9%</td>
<td align="right">2,920</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">580</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">200</td>
<td align="right">0.3%</td>
<td align="right">200</td>
<td align="right">0.3%</td>
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
<td align="right">734,129</td>
<td align="right">0.0%</td>
<td align="right">736,028</td>
<td align="right">0.0%</td>
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
<td align="right">97,413,051</td>
<td align="right">2.0%</td>
<td align="right">97,563,428</td>
<td align="right">2.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,828,798,621</td>
<td align="right">98.0%</td>
<td align="right">4,830,129,419</td>
<td align="right">98.0%</td>
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
<td align="right">63,888</td>
<td align="right">33.2%</td>
<td align="right">63,928</td>
<td align="right">33.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">128,645</td>
<td align="right">66.8%</td>
<td align="right">128,705</td>
<td align="right">66.8%</td>
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
<td align="left">baseobject</td>
<td align="right">18,640</td>
<td align="right">14.5%</td>
<td align="right">18,520</td>
<td align="right">14.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">24,920</td>
<td align="right">19.4%</td>
<td align="right">25,039</td>
<td align="right">19.5%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,321</td>
<td align="right">11.1%</td>
<td align="right">14,367</td>
<td align="right">11.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,266</td>
<td align="right">20.4%</td>
<td align="right">26,307</td>
<td align="right">20.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,423</td>
<td align="right">1.1%</td>
<td align="right">1,425</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,540</td>
<td align="right">9.0%</td>
<td align="right">11,526</td>
<td align="right">9.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,336</td>
<td align="right">12.7%</td>
<td align="right">16,321</td>
<td align="right">12.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,619</td>
<td align="right">1.3%</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">10,680</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">1,600</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">800</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">500</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.4%</td>
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
<td align="right">2,365,993,509</td>
<td align="right">92.3%</td>
<td align="right">2,366,564,777</td>
<td align="right">92.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">197,774,242</td>
<td align="right">7.7%</td>
<td align="right">197,802,600</td>
<td align="right">7.7%</td>
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
<td align="right">2,517,260</td>
<td align="right">0.1%</td>
<td align="right">2,517,260</td>
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
<td align="right">96,550</td>
<td align="right">62.2%</td>
<td align="right">96,560</td>
<td align="right">62.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,659</td>
<td align="right">37.8%</td>
<td align="right">58,660</td>
<td align="right">37.8%</td>
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
<td align="right">12,775</td>
<td align="right">13.2%</td>
<td align="right">12,781</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,035</td>
<td align="right">22.8%</td>
<td align="right">22,039</td>
<td align="right">22.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">53,360</td>
<td align="right">55.3%</td>
<td align="right">53,360</td>
<td align="right">55.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">8,380</td>
<td align="right">8.7%</td>
<td align="right">8,380</td>
<td align="right">8.7%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">143,279</td>
<td align="right">0.0%</td>
<td align="right">147,003</td>
<td align="right">0.0%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">458,380,355</td>
<td align="right">85.8%</td>
<td align="right">459,847,181</td>
<td align="right">85.8%</td>
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
<td align="right">75,637,184</td>
<td align="right">14.2%</td>
<td align="right">75,726,234</td>
<td align="right">14.1%</td>
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
<td align="right">90,473</td>
<td align="right">66.3%</td>
<td align="right">90,648</td>
<td align="right">66.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,964</td>
<td align="right">33.7%</td>
<td align="right">46,011</td>
<td align="right">33.7%</td>
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
<td align="left">set</td>
<td align="right">9,977</td>
<td align="right">11.0%</td>
<td align="right">10,019</td>
<td align="right">11.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">35,864</td>
<td align="right">39.6%</td>
<td align="right">35,981</td>
<td align="right">39.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,460</td>
<td align="right">7.1%</td>
<td align="right">6,480</td>
<td align="right">7.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,052</td>
<td align="right">10.0%</td>
<td align="right">9,048</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.5%</td>
<td align="right">7,720</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">6.9%</td>
<td align="right">6,240</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">4.7%</td>
<td align="right">4,240</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,580</td>
<td align="right">4.0%</td>
<td align="right">3,580</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,060</td>
<td align="right">3.4%</td>
<td align="right">3,060</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,220</td>
<td align="right">1.3%</td>
<td align="right">1,220</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">560</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">320</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">220</td>
<td align="right">0.2%</td>
<td align="right">220</td>
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
<td align="right">1,218,663,766</td>
<td align="right">7.9%</td>
<td align="right">1,222,316,198</td>
<td align="right">7.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,258,649,654</td>
<td align="right">92.1%</td>
<td align="right">14,271,844,079</td>
<td align="right">92.1%</td>
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
<td align="right">246,651,855</td>
<td align="right">1.6%</td>
<td align="right">246,637,521</td>
<td align="right">1.6%</td>
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
<td align="right">320,700</td>
<td align="right">0.0%</td>
<td align="right">320,700</td>
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
<td align="right">761,712</td>
<td align="right">12.8%</td>
<td align="right">763,518</td>
<td align="right">12.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,178,308</td>
<td align="right">87.2%</td>
<td align="right">5,178,024</td>
<td align="right">87.1%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">5,420</td>
<td align="right">0.7%</td>
<td align="right">5,544</td>
<td align="right">0.7%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,088</td>
<td align="right">7.1%</td>
<td align="right">54,469</td>
<td align="right">7.1%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,759</td>
<td align="right">1.8%</td>
<td align="right">13,840</td>
<td align="right">1.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">75,145</td>
<td align="right">9.9%</td>
<td align="right">75,460</td>
<td align="right">9.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,860</td>
<td align="right">3.4%</td>
<td align="right">25,960</td>
<td align="right">3.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.6%</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">44,876</td>
<td align="right">5.9%</td>
<td align="right">44,997</td>
<td align="right">5.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">250,298</td>
<td align="right">32.9%</td>
<td align="right">250,808</td>
<td align="right">32.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,413</td>
<td align="right">1.8%</td>
<td align="right">13,432</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,720</td>
<td align="right">2.6%</td>
<td align="right">19,740</td>
<td align="right">2.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">148,673</td>
<td align="right">19.5%</td>
<td align="right">148,743</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72,760</td>
<td align="right">9.6%</td>
<td align="right">72,785</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,760</td>
<td align="right">2.1%</td>
<td align="right">15,760</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,180</td>
<td align="right">0.7%</td>
<td align="right">5,180</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,800</td>
<td align="right">0.4%</td>
<td align="right">2,800</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">320</td>
<td align="right">0.0%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">438,975</td>
<td align="right">0.0%</td>
<td align="right">441,604</td>
<td align="right">0.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,167,977,039</td>
<td align="right">99.6%</td>
<td align="right">5,152,164,813</td>
<td align="right">99.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,287,624</td>
<td align="right">0.4%</td>
<td align="right">20,290,047</td>
<td align="right">0.4%</td>
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
<td align="right">10,680</td>
<td align="right">0.0%</td>
<td align="right">10,680</td>
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
<td align="right">430,919</td>
<td align="right">100.0%</td>
<td align="right">430,848</td>
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
<td align="right">82,755,046</td>
<td align="right">100.0%</td>
<td align="right">83,547,181</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,865</td>
<td align="right">0.0%</td>
<td align="right">7,861</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">7,580</td>
<td align="right">100.0%</td>
<td align="right">7,580</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">786,180,383</td>
<td align="right">81.9%</td>
<td align="right">786,180,427</td>
<td align="right">81.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,284,246</td>
<td align="right">18.1%</td>
<td align="right">173,284,238</td>
<td align="right">18.1%</td>
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
<td align="right">30,660</td>
<td align="right">0.0%</td>
<td align="right">30,660</td>
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
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">5,400</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,600</td>
<td align="right">91.7%</td>
<td align="right">59,600</td>
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
<td align="left">async generator send</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">33,180</td>
<td align="right">55.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">14,240</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">9,960</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
<td align="right">2,220</td>
<td align="right">3.7%</td>
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
<td align="right">68,503,901</td>
<td align="right">2.5%</td>
<td align="right">67,998,398</td>
<td align="right">2.5%</td>
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
<td align="right">98,460,531</td>
<td align="right">3.6%</td>
<td align="right">97,969,968</td>
<td align="right">3.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,667,400,321</td>
<td align="right">96.4%</td>
<td align="right">2,668,552,374</td>
<td align="right">96.4%</td>
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
<td align="right">1,377,995</td>
<td align="right">95.7%</td>
<td align="right">1,368,465</td>
<td align="right">95.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">61,908</td>
<td align="right">4.3%</td>
<td align="right">62,062</td>
<td align="right">4.3%</td>
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
<td align="left">property</td>
<td align="right">2,480</td>
<td align="right">4.0%</td>
<td align="right">2,580</td>
<td align="right">4.2%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,700</td>
<td align="right">7.6%</td>
<td align="right">4,720</td>
<td align="right">7.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,800</td>
<td align="right">15.8%</td>
<td align="right">9,840</td>
<td align="right">15.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,748</td>
<td align="right">15.7%</td>
<td align="right">9,742</td>
<td align="right">15.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">12,920</td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
<td align="right">8,580</td>
<td align="right">13.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,600</td>
<td align="right">7.4%</td>
<td align="right">4,600</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">4,360</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">3,800</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">800</td>
<td align="right">1.3%</td>
<td align="right">800</td>
<td align="right">1.3%</td>
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
<td align="right">817,766,974</td>
<td align="right">93.6%</td>
<td align="right">818,314,869</td>
<td align="right">93.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">56,261,937</td>
<td align="right">6.4%</td>
<td align="right">56,262,727</td>
<td align="right">6.4%</td>
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
<td align="right">48,541</td>
<td align="right">82.0%</td>
<td align="right">48,578</td>
<td align="right">82.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,621</td>
<td align="right">18.0%</td>
<td align="right">10,620</td>
<td align="right">17.9%</td>
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
<td align="left">other</td>
<td align="right">320</td>
<td align="right">0.7%</td>
<td align="right">340</td>
<td align="right">0.7%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,520</td>
<td align="right">67.0%</td>
<td align="right">32,540</td>
<td align="right">67.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,521</td>
<td align="right">15.5%</td>
<td align="right">7,518</td>
<td align="right">15.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">13.3%</td>
<td align="right">6,480</td>
<td align="right">13.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">900</td>
<td align="right">1.9%</td>
<td align="right">900</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">800</td>
<td align="right">1.6%</td>
<td align="right">800</td>
<td align="right">1.6%</td>
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
<td align="right">5,764,695,473</td>
<td align="right">95.5%</td>
<td align="right">5,769,419,276</td>
<td align="right">95.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">272,690,084</td>
<td align="right">4.5%</td>
<td align="right">272,875,624</td>
<td align="right">4.5%</td>
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
<td align="right">48,924,299</td>
<td align="right">0.8%</td>
<td align="right">48,924,834</td>
<td align="right">0.8%</td>
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
<td align="right">171,731</td>
<td align="right">13.5%</td>
<td align="right">171,991</td>
<td align="right">13.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,099,568</td>
<td align="right">86.5%</td>
<td align="right">1,099,528</td>
<td align="right">86.5%</td>
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
<td align="left">number</td>
<td align="right">4,809</td>
<td align="right">2.8%</td>
<td align="right">4,836</td>
<td align="right">2.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">4,428</td>
<td align="right">2.6%</td>
<td align="right">4,449</td>
<td align="right">2.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,115</td>
<td align="right">7.6%</td>
<td align="right">13,158</td>
<td align="right">7.7%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">47,860</td>
<td align="right">27.9%</td>
<td align="right">47,943</td>
<td align="right">27.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,823</td>
<td align="right">15.6%</td>
<td align="right">26,858</td>
<td align="right">15.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">45,989</td>
<td align="right">26.8%</td>
<td align="right">46,038</td>
<td align="right">26.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,207</td>
<td align="right">7.7%</td>
<td align="right">13,209</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,580</td>
<td align="right">7.3%</td>
<td align="right">12,580</td>
<td align="right">7.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.9%</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
<td align="right">1,040</td>
<td align="right">0.6%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,491,489,748</td>
<td align="right">100.0%</td>
<td align="right">1,491,835,557</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">186,388</td>
<td align="right">0.0%</td>
<td align="right">186,405</td>
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
<td align="right">26,256</td>
<td align="right">93.7%</td>
<td align="right">26,228</td>
<td align="right">93.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,776</td>
<td align="right">6.3%</td>
<td align="right">1,777</td>
<td align="right">6.3%</td>
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
<td align="left">sequence</td>
<td align="right">1,136</td>
<td align="right">64.0%</td>
<td align="right">1,137</td>
<td align="right">64.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.6%</td>
<td align="right">260</td>
<td align="right">14.6%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,044,059,505</td>
<td align="right">35.7%</td>
<td align="right">36,815,783,203</td>
<td align="right">35.6%</td>
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
<td align="right">56,552,394,746</td>
<td align="right">54.4%</td>
<td align="right">56,245,250,585</td>
<td align="right">54.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,629,676,084</td>
<td align="right">9.3%</td>
<td align="right">9,577,527,749</td>
<td align="right">9.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">651,775,011</td>
<td align="right">0.6%</td>
<td align="right">651,236,008</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
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
<td align="right">410,724,808</td>
<td align="right">12.4%</td>
<td align="right">384,465,877</td>
<td align="right">11.6%</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,460,531</td>
<td align="right">3.0%</td>
<td align="right">97,969,968</td>
<td align="right">3.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,218,663,766</td>
<td align="right">36.7%</td>
<td align="right">1,222,316,198</td>
<td align="right">37.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">416,164,789</td>
<td align="right">12.5%</td>
<td align="right">415,446,792</td>
<td align="right">12.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,413,051</td>
<td align="right">2.9%</td>
<td align="right">97,563,428</td>
<td align="right">3.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,637,184</td>
<td align="right">2.3%</td>
<td align="right">75,726,234</td>
<td align="right">2.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">286,775,649</td>
<td align="right">8.6%</td>
<td align="right">286,983,994</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">272,690,084</td>
<td align="right">8.2%</td>
<td align="right">272,875,624</td>
<td align="right">8.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,774,242</td>
<td align="right">5.9%</td>
<td align="right">197,802,600</td>
<td align="right">6.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,246</td>
<td align="right">5.2%</td>
<td align="right">173,284,238</td>
<td align="right">5.2%</td>
<td align="right">-0.0%</td>
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
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,204,278</td>
<td align="right">3.5%</td>
<td align="right">24,698,777</td>
<td align="right">3.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,958,299</td>
<td align="right">5.6%</td>
<td align="right">40,952,901</td>
<td align="right">5.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,023,649</td>
<td align="right">10.0%</td>
<td align="right">73,024,951</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">24,452,281</td>
<td align="right">3.4%</td>
<td align="right">24,452,582</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,481,349</td>
<td align="right">3.8%</td>
<td align="right">27,481,440</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,768,036</td>
<td align="right">12.4%</td>
<td align="right">90,767,831</td>
<td align="right">12.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,518</td>
<td align="right">10.7%</td>
<td align="right">77,874,379</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,518</td>
<td align="right">10.7%</td>
<td align="right">77,874,379</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,608,214</td>
<td align="right">13.8%</td>
<td align="right">100,608,195</td>
<td align="right">13.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,280,203</td>
<td align="right">5.9%</td>
<td align="right">43,280,201</td>
<td align="right">5.9%</td>
<td align="right">-0.0%</td>
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
<td align="right">224,360,838</td>
<td align="right">2.8%</td>
<td align="right">225,149,229</td>
<td align="right">2.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,519,756,668</td>
<td align="right">18.9%</td>
<td align="right">1,522,172,580</td>
<td align="right">18.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,524,190,808</td>
<td align="right">19.0%</td>
<td align="right">1,526,606,720</td>
<td align="right">19.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,330,798,472</td>
<td align="right">78.8%</td>
<td align="right">6,339,369,419</td>
<td align="right">78.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,649,898,857</td>
<td align="right">70.3%</td>
<td align="right">5,656,403,375</td>
<td align="right">70.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,384,539,940</td>
<td align="right">29.7%</td>
<td align="right">2,386,676,538</td>
<td align="right">29.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,384,539,940</td>
<td align="right">29.7%</td>
<td align="right">2,386,676,538</td>
<td align="right">29.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,349,132</td>
<td align="right">10.7%</td>
<td align="right">860,069,818</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,554,360</td>
<td align="right">0.9%</td>
<td align="right">71,565,082</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,894,179</td>
<td align="right">6.6%</td>
<td align="right">526,931,169</td>
<td align="right">6.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,576,112</td>
<td align="right">0.4%</td>
<td align="right">28,577,464</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,989</td>
<td align="right">2.6%</td>
<td align="right">211,357,839</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,411,620</td>
<td align="right">0.1%</td>
<td align="right">4,411,620</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">22,520</td>
<td align="right">0.0%</td>
<td align="right">22,520</td>
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
<td align="right">21,535,064</td>
<td align="right"></td>
<td align="right">22,759,712</td>
<td align="right"></td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">26,223,810</td>
<td align="right"></td>
<td align="right">27,441,457</td>
<td align="right"></td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,092,167</td>
<td align="right"></td>
<td align="right">7,196,293</td>
<td align="right"></td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">59,271,792,801</td>
<td align="right">46.1%</td>
<td align="right">58,793,575,987</td>
<td align="right">45.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">69,414,165,447</td>
<td align="right">53.9%</td>
<td align="right">69,846,806,040</td>
<td align="right">54.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">45,802,219,079</td>
<td align="right">40.7%</td>
<td align="right">45,578,005,052</td>
<td align="right">40.6%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,741,864</td>
<td align="right">0.1%</td>
<td align="right">19,810,455</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">149,564,562</td>
<td align="right"></td>
<td align="right">150,008,062</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">66,635,219,417</td>
<td align="right">59.3%</td>
<td align="right">66,803,361,722</td>
<td align="right">59.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,631,652,836</td>
<td align="right"></td>
<td align="right">2,635,678,389</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,103,136,460</td>
<td align="right"></td>
<td align="right">3,106,357,179</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,448,446,059</td>
<td align="right">38.5%</td>
<td align="right">6,454,184,805</td>
<td align="right">38.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,450,211,476</td>
<td align="right"></td>
<td align="right">6,455,950,804</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,610,033,033</td>
<td align="right"></td>
<td align="right">10,616,654,657</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,281,158,920</td>
<td align="right">61.5%</td>
<td align="right">10,287,098,514</td>
<td align="right">61.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,157,744,588</td>
<td align="right">60.7%</td>
<td align="right">10,163,577,095</td>
<td align="right">60.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,672,468</td>
<td align="right">0.6%</td>
<td align="right">103,710,964</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,240</td>
<td align="right">2.2%</td>
<td align="right">3,271,240</td>
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
<td align="right">18,557,940</td>
<td align="right">14,350,717,695</td>
<td align="right">0</td>
<td align="right">18,557,740</td>
<td align="right">14,340,930,275</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,982,877,628</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,982,939,116</td>
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
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">686</td>
<td align="right">0.1%</td>
<td align="right">821</td>
<td align="right">0.1%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">44,495</td>
<td align="right">6.1%</td>
<td align="right">46,833</td>
<td align="right">6.7%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">632,610</td>
<td align="right">86.4%</td>
<td align="right">601,422</td>
<td align="right">85.7%</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">732,475</td>
<td align="right"></td>
<td align="right">701,562</td>
<td align="right"></td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,506</td>
<td align="right">0.9%</td>
<td align="right">6,756</td>
<td align="right">1.0%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,340</td>
<td align="right">0.2%</td>
<td align="right">1,380</td>
<td align="right">0.2%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,995,874,487</td>
<td align="right"></td>
<td align="right">6,845,317,520</td>
<td align="right"></td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">436,264</td>
<td align="right">59.6%</td>
<td align="right">440,576</td>
<td align="right">62.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,201</td>
<td align="right">6.2%</td>
<td align="right">6,236</td>
<td align="right">6.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">199,518,084,361</td>
<td align="right">2,851.9%</td>
<td align="right">200,250,931,808</td>
<td align="right">2,925.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">99,865</td>
<td align="right">13.6%</td>
<td align="right">100,140</td>
<td align="right">14.3%</td>
<td align="right">0.3%</td>
</tr>
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
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="right">96,285</td>
<td align="right">96.4%</td>
<td align="right">96,554</td>
<td align="right">96.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">99,865</td>
<td align="right"></td>
<td align="right">100,140</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">2,366</td>
<td align="right">2.4%</td>
<td align="right">0.3%</td>
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
<td align="right">4,417</td>
<td align="right">4.4%</td>
<td align="right">4,414</td>
<td align="right">4.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,770</td>
<td align="right">18.8%</td>
<td align="right">18,606</td>
<td align="right">18.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,426</td>
<td align="right">31.5%</td>
<td align="right">31,530</td>
<td align="right">31.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,676</td>
<td align="right">24.7%</td>
<td align="right">24,774</td>
<td align="right">24.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,011</td>
<td align="right">13.0%</td>
<td align="right">13,068</td>
<td align="right">13.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,905</td>
<td align="right">5.9%</td>
<td align="right">5,888</td>
<td align="right">5.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,700</td>
<td align="right">1.7%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">160</td>
<td align="right">0.2%</td>
<td align="right">160</td>
<td align="right">0.2%</td>
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
<td align="right">3,517</td>
<td align="right">3.5%</td>
<td align="right">3,514</td>
<td align="right">3.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,190</td>
<td align="right">13.2%</td>
<td align="right">13,184</td>
<td align="right">13.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,044</td>
<td align="right">21.1%</td>
<td align="right">20,770</td>
<td align="right">20.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,645</td>
<td align="right">31.7%</td>
<td align="right">31,469</td>
<td align="right">31.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,828</td>
<td align="right">15.8%</td>
<td align="right">16,292</td>
<td align="right">16.3%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,777</td>
<td align="right">7.8%</td>
<td align="right">7,833</td>
<td align="right">7.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,864</td>
<td align="right">2.9%</td>
<td align="right">2,992</td>
<td align="right">3.0%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">500</td>
<td align="right">0.5%</td>
<td align="right">19.0%</td>
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
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,440</td>
<td align="right">243,289,720</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,854,426</td>
<td align="right">242,248,603</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,384</td>
<td align="right">4,822,900</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,960</td>
<td align="right">105,332,260</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">177,501,460</td>
<td align="right">187,073,824</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,547,427</td>
<td align="right">47,700,936</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,835,680</td>
<td align="right">238,335,682</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,073,773,270</td>
<td align="right">1,979,779,768</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,814,040</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,532,656</td>
<td align="right">17,095,919</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,183,671,810</td>
<td align="right">2,253,818,924</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,041,466,866</td>
<td align="right">1,070,891,543</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,043,487,026</td>
<td align="right">1,068,187,900</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,487,575,199</td>
<td align="right">6,614,088,329</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,047,405</td>
<td align="right">561,510,600</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,776,574</td>
<td align="right">5,885,098</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,048,318,904</td>
<td align="right">1,065,981,556</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,560,740,706</td>
<td align="right">4,493,781,011</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,870,745,840</td>
<td align="right">1,895,233,873</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,922,101,217</td>
<td align="right">4,865,537,752</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,645,330,819</td>
<td align="right">2,675,009,495</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,292,731,288</td>
<td align="right">3,328,581,691</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,117,617</td>
<td align="right">10,224,921</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,021,992</td>
<td align="right">22,252,420</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,192,745</td>
<td align="right">1,125,536,941</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">875,622,191</td>
<td align="right">884,038,645</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,820,170,770</td>
<td align="right">2,844,447,167</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,387,999,946</td>
<td align="right">1,399,199,442</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,554,804,253</td>
<td align="right">9,624,010,886</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,311,234,991</td>
<td align="right">1,320,575,649</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,833,566</td>
<td align="right">60,222,690</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,921,260</td>
<td align="right">412,057,495</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,784,973,417</td>
<td align="right">11,842,081,422</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,246,464,824</td>
<td align="right">1,252,497,639</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,265,133,784</td>
<td align="right">1,271,175,939</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,294,657</td>
<td align="right">112,819,255</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,146,853</td>
<td align="right">91,565,458</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,390,973</td>
<td align="right">91,809,578</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,838,445,458</td>
<td align="right">13,897,378,771</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,656,314,967</td>
<td align="right">6,683,793,655</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,527,876</td>
<td align="right">93,894,712</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,315,992</td>
<td align="right">126,794,787</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,345,275,032</td>
<td align="right">1,349,931,446</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,043,428</td>
<td align="right">2,189,571,178</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,548,487</td>
<td align="right">114,900,464</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,719,228</td>
<td align="right">73,934,028</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,354,565</td>
<td align="right">11,387,072</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,354,565</td>
<td align="right">11,387,072</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">128,979,703</td>
<td align="right">129,318,863</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,174,508</td>
<td align="right">154,560,172</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">179,421,667</td>
<td align="right">179,860,017</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,727,426,828</td>
<td align="right">5,741,331,575</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,921,160</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">111,806,699</td>
<td align="right">112,002,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">571,278,550</td>
<td align="right">572,187,251</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,464,344,158</td>
<td align="right">6,474,348,147</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,088,192</td>
<td align="right">3,608,652,713</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,911,747</td>
<td align="right">69,006,910</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">172,894,806</td>
<td align="right">173,123,860</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,510,816</td>
<td align="right">1,654,628,013</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,787,939</td>
<td align="right">24,819,625</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,226,348,272</td>
<td align="right">2,229,086,589</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,871</td>
<td align="right">109,073,114</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">161,727,964</td>
<td align="right">161,901,513</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,422</td>
<td align="right">101,291,287</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,275,734</td>
<td align="right">134,404,654</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">134,275,734</td>
<td align="right">134,404,654</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,061,559</td>
<td align="right">30,090,190</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,234,288</td>
<td align="right">263,466,907</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,461,108</td>
<td align="right">264,693,727</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,454,700,186</td>
<td align="right">3,457,600,100</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,974,016,180</td>
<td align="right">1,975,606,617</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,656,618</td>
<td align="right">133,764,273</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,875,183,871</td>
<td align="right">1,876,658,337</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,229,132</td>
<td align="right">485,587,562</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,339,107,271</td>
<td align="right">1,340,076,845</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,666,575,631</td>
<td align="right">1,667,744,899</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,728,710,570</td>
<td align="right">1,729,873,360</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,859,490,873</td>
<td align="right">1,860,729,333</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,510,984,929</td>
<td align="right">1,511,981,691</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,918,726,671</td>
<td align="right">1,919,965,009</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,093,491,602</td>
<td align="right">7,098,019,567</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">822,854,645</td>
<td align="right">823,374,114</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,309,613,499</td>
<td align="right">1,310,408,592</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,013,864,955</td>
<td align="right">1,014,473,989</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">130,802,401</td>
<td align="right">130,878,243</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">313,297,428</td>
<td align="right">313,118,491</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">759,387,446</td>
<td align="right">759,804,212</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,016,375</td>
<td align="right">342,201,683</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,370,134,108</td>
<td align="right">1,370,853,778</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,201,882,244</td>
<td align="right">3,203,556,996</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,272,547</td>
<td align="right">199,372,800</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">139,987,220</td>
<td align="right">140,055,276</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,708,606,074</td>
<td align="right">4,710,854,036</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,146,375,424</td>
<td align="right">1,146,890,939</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">232,033,452</td>
<td align="right">232,136,592</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">948,339,282</td>
<td align="right">948,734,479</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,200,646</td>
<td align="right">779,524,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">779,737,966</td>
<td align="right">780,061,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">360,002,536</td>
<td align="right">360,152,091</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,099,366,093</td>
<td align="right">1,099,822,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,070,128</td>
<td align="right">617,821,826</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,760,042</td>
<td align="right">565,973,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">400,047,096</td>
<td align="right">400,196,651</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,944,001</td>
<td align="right">109,983,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">714,411,449</td>
<td align="right">714,656,005</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,582,084</td>
<td align="right">1,275,002,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,917</td>
<td align="right">445,059</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,248,288</td>
<td align="right">733,464,222</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,941,470,707</td>
<td align="right">2,942,326,673</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,440,069</td>
<td align="right">185,492,519</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,963,243</td>
<td align="right">188,015,661</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,233,766,789</td>
<td align="right">2,234,362,773</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,257,031,289</td>
<td align="right">2,257,627,293</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">958,951,116</td>
<td align="right">959,180,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,399,462</td>
<td align="right">78,380,744</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">541,056,271</td>
<td align="right">540,934,246</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,765,180</td>
<td align="right">229,815,269</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">88,974,636</td>
<td align="right">88,956,170</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,423,288</td>
<td align="right">93,404,609</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">410,807,585</td>
<td align="right">410,886,142</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,536,056,102</td>
<td align="right">2,536,514,593</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,093,256,740</td>
<td align="right">2,093,527,884</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">687,095,548</td>
<td align="right">687,182,544</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,507,283</td>
<td align="right">592,433,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,166,016</td>
<td align="right">930,276,015</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">315,041,692</td>
<td align="right">315,070,427</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,570,333</td>
<td align="right">966,650,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,231,275,102</td>
<td align="right">1,231,366,618</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,538,331</td>
<td align="right">280,556,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,586,850</td>
<td align="right">1,974,707,870</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,406,779</td>
<td align="right">686,448,259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">723,894,216</td>
<td align="right">723,937,101</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,720</td>
<td align="right">5,636,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,875,160</td>
<td align="right">4,875,396</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,947,697</td>
<td align="right">243,939,624</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,092,815</td>
<td align="right">1,367,131,739</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,318,784</td>
<td align="right">32,319,270</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,692,440</td>
<td align="right">909,705,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,252,400</td>
<td align="right">145,254,500</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,402,469</td>
<td align="right">330,398,262</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,549,860</td>
<td align="right">1,144,563,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,151,630</td>
<td align="right">1,335,165,135</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,157,418</td>
<td align="right">203,159,465</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">226,303,551</td>
<td align="right">226,305,803</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,188,480</td>
<td align="right">423,192,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,551,306</td>
<td align="right">118,552,283</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">782,652,754</td>
<td align="right">782,646,779</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,665,280</td>
<td align="right">93,665,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,423</td>
<td align="right">647,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">325,040,038</td>
<td align="right">325,041,597</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,198,196</td>
<td align="right">97,197,862</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,155,536</td>
<td align="right">98,155,202</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">224,415,462</td>
<td align="right">224,416,148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">375,828,062</td>
<td align="right">375,829,122</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,030,720</td>
<td align="right">199,031,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,284,200</td>
<td align="right">22,284,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,908,150</td>
<td align="right">9,908,157</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,261,092</td>
<td align="right">54,261,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,639,762</td>
<td align="right">147,639,683</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,524,606</td>
<td align="right">1,818,523,885</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,197,960</td>
<td align="right">101,197,930</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,898,826</td>
<td align="right">484,898,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,951</td>
<td align="right">55,151,954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,180</td>
<td align="right">645,067,150</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,107</td>
<td align="right">35,070,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,940</td>
<td align="right">384,637,941</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,100</td>
<td align="right">588,457,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,073,040</td>
<td align="right">533,073,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">509,717,760</td>
<td align="right">509,717,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">230,436,740</td>
<td align="right">230,436,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,540</td>
<td align="right">187,548,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">149,868,340</td>
<td align="right">149,868,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">144,940,100</td>
<td align="right">144,940,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,571,420</td>
<td align="right">80,571,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">66,194,480</td>
<td align="right">66,194,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">64,886,820</td>
<td align="right">64,886,820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,424,460</td>
<td align="right">63,424,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,901,080</td>
<td align="right">61,901,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,155,800</td>
<td align="right">61,155,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,045,260</td>
<td align="right">61,045,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,348,980</td>
<td align="right">46,348,980</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">14,750,660</td>
<td align="right">14,750,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">14,733,440</td>
<td align="right">14,733,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,693,340</td>
<td align="right">12,693,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,134,100</td>
<td align="right">8,134,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">4,625,240</td>
<td align="right">4,625,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,610,440</td>
<td align="right">3,610,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,714,740</td>
<td align="right">2,714,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">2,126,620</td>
<td align="right">2,126,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,940,740</td>
<td align="right">1,940,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">1,887,020</td>
<td align="right">1,887,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,543,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">821,160</td>
<td align="right">821,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">543,380</td>
<td align="right">543,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">71,600</td>
<td align="right">71,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">34,780</td>
<td align="right">34,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">29,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">17,200</td>
<td align="right">17,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">7,620</td>
<td align="right">7,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">120,883,926</td>
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
<td align="right">82,008</td>
<td align="right">46,526</td>
<td align="right">-43.3%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">1,440</td>
<td align="right">1,465</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,571</td>
<td align="right">6,617</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">538</td>
<td align="right">540</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,417</td>
<td align="right">2,419</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,479</td>
<td align="right">40,490</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">28,920</td>
<td align="right">28,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,201</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,340</td>
<td align="right">2,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">1,620</td>
<td align="right">1,620</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,340</td>
<td align="right">1,340</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">820</td>
<td align="right">820</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">360</td>
<td align="right">360</td>
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
<td align="right">1,081</td>
<td align="right">1,087</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,081</td>
<td align="right">1,087</td>
<td align="right">0.6%</td>
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
<td align="right">1,860</td>
<td align="right">1,860</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-06-06
