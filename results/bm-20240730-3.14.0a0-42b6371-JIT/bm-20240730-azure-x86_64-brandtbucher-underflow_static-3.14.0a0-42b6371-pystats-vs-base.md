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
<td align="left">JUMP_BACKWARD</td>
<td align="right">3,734,881</td>
<td align="right">8,061,903</td>
<td align="right">115.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,461,860</td>
<td align="right">113,560</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,293,537</td>
<td align="right">6,132,343</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,210,720</td>
<td align="right">18,301,860</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,357,142</td>
<td align="right">24,782,262</td>
<td align="right">-82.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,719,201</td>
<td align="right">12,510,781</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,438,094</td>
<td align="right">1,019,925</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">661,880</td>
<td align="right">191,448</td>
<td align="right">-71.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">120,356,993</td>
<td align="right">35,081,499</td>
<td align="right">-70.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,997,933</td>
<td align="right">21,862,008</td>
<td align="right">-67.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">49,706,458</td>
<td align="right">17,329,846</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,601,473</td>
<td align="right">3,549,025</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">48,507,626</td>
<td align="right">18,551,811</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">174,441,410</td>
<td align="right">66,889,014</td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">101,717,094</td>
<td align="right">42,257,097</td>
<td align="right">-58.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">146,868,260</td>
<td align="right">66,333,693</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">324,141,705</td>
<td align="right">151,927,024</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,373</td>
<td align="right">91,907,508</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">49,052,472</td>
<td align="right">24,137,261</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,019</td>
<td align="right">116,992</td>
<td align="right">-47.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">1,051,503,944</td>
<td align="right">554,820,481</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">396,573,388</td>
<td align="right">211,134,192</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,508,207</td>
<td align="right">33,278,469</td>
<td align="right">-43.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">123,812,509</td>
<td align="right">70,602,164</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,801,652</td>
<td align="right">42,311,553</td>
<td align="right">-41.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">365,767,069</td>
<td align="right">212,760,319</td>
<td align="right">-41.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">420,359,967</td>
<td align="right">256,770,187</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">70,581,732</td>
<td align="right">46,794,099</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">76,016,384</td>
<td align="right">50,689,782</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,956,915</td>
<td align="right">7,513,062</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">111,926,589</td>
<td align="right">77,205,258</td>
<td align="right">-31.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">39,943,092</td>
<td align="right">28,026,881</td>
<td align="right">-29.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,054,313</td>
<td align="right">64,162,921</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">199,470,985</td>
<td align="right">141,922,163</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,420</td>
<td align="right">123,992</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">404,888,806</td>
<td align="right">290,145,537</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">28,713,173</td>
<td align="right">20,597,742</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,094,021</td>
<td align="right">15,852,271</td>
<td align="right">-28.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">5,107,026,484</td>
<td align="right">3,740,855,059</td>
<td align="right">-26.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,202,651,981</td>
<td align="right">3,099,570,021</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">98,598,586</td>
<td align="right">73,404,923</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,976,492</td>
<td align="right">40,512,981</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,888,690,033</td>
<td align="right">2,170,675,821</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">248,861,323</td>
<td align="right">187,399,393</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">82,643,022</td>
<td align="right">62,321,194</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">263,493,067</td>
<td align="right">198,734,384</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">958,967,414</td>
<td align="right">729,738,759</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">299,539,237</td>
<td align="right">227,998,456</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">48,050,489</td>
<td align="right">36,913,601</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">223,617,816</td>
<td align="right">172,030,608</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">358,086,597</td>
<td align="right">275,877,826</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">203,961,671</td>
<td align="right">159,477,019</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">296,872,218</td>
<td align="right">232,709,777</td>
<td align="right">-21.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">765,820</td>
<td align="right">603,340</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">31,059,001</td>
<td align="right">25,120,774</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,014,648,264</td>
<td align="right">2,442,234,982</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">768,752,895</td>
<td align="right">623,108,973</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">12,305,060</td>
<td align="right">10,020,880</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">821,780,666</td>
<td align="right">669,763,059</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">327,945,679</td>
<td align="right">267,665,038</td>
<td align="right">-18.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,857,205,265</td>
<td align="right">2,332,953,670</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">151,693,043</td>
<td align="right">123,908,848</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">690,751,197</td>
<td align="right">564,429,079</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">19,315,604,786</td>
<td align="right">15,826,686,800</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">758,442,685</td>
<td align="right">623,283,024</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,001,274,814</td>
<td align="right">3,288,965,500</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">59,690,400</td>
<td align="right">49,160,700</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,391,378,792</td>
<td align="right">1,146,681,413</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">325,885,639</td>
<td align="right">268,890,149</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">350,582,884</td>
<td align="right">292,297,252</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">327,368,540</td>
<td align="right">274,856,040</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">193,954,299</td>
<td align="right">163,246,138</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,863,737,734</td>
<td align="right">1,582,160,806</td>
<td align="right">-15.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">4,099,807,151</td>
<td align="right">3,483,390,363</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">36,738,346</td>
<td align="right">31,276,712</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,066,378,137</td>
<td align="right">909,068,558</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">870,591,719</td>
<td align="right">743,299,858</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,401,309,956</td>
<td align="right">2,050,374,737</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">442,393,425</td>
<td align="right">378,226,356</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">41,785,910</td>
<td align="right">35,852,417</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,908,608,920</td>
<td align="right">4,221,269,291</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">5,041,467,671</td>
<td align="right">4,339,673,626</td>
<td align="right">-13.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,985,456,723</td>
<td align="right">1,724,354,177</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">335,375,175</td>
<td align="right">291,999,754</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">139,289,710</td>
<td align="right">156,933,840</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">133,605,286</td>
<td align="right">117,001,435</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,132,753,800</td>
<td align="right">992,761,877</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">319,396,214</td>
<td align="right">280,255,405</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">183,739,102</td>
<td align="right">162,287,687</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,331,757,574</td>
<td align="right">2,945,916,219</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">728,573,153</td>
<td align="right">645,115,262</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">197,803,949</td>
<td align="right">175,915,152</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">92,342,267</td>
<td align="right">82,153,943</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">49,630,208</td>
<td align="right">44,378,922</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">897,058,864</td>
<td align="right">806,944,139</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">210,177,283</td>
<td align="right">190,046,898</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,085,302,233</td>
<td align="right">987,420,112</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">82,391,124</td>
<td align="right">75,147,946</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">649,334,277</td>
<td align="right">597,282,950</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,389,362,993</td>
<td align="right">4,973,960,674</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,337,803</td>
<td align="right">371,507,003</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,683,541</td>
<td align="right">9,003,291</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,395,407,719</td>
<td align="right">1,297,726,102</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">426,462,009</td>
<td align="right">397,104,134</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">47,903,872</td>
<td align="right">44,633,858</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">660,995,403</td>
<td align="right">616,261,035</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,007,121</td>
<td align="right">32,666,261</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">180,122,438</td>
<td align="right">168,512,894</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">149,913,876</td>
<td align="right">140,687,751</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,103,752</td>
<td align="right">382,562,911</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,237,033,011</td>
<td align="right">1,177,365,181</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">321,175,162</td>
<td align="right">336,313,052</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">484,264,184</td>
<td align="right">462,158,831</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">159,452,222</td>
<td align="right">152,889,865</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">371,659,999</td>
<td align="right">357,747,757</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,354,340</td>
<td align="right">2,441,363</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,867,738</td>
<td align="right">19,157,287</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">85,825,513</td>
<td align="right">82,945,749</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,007,877</td>
<td align="right">142,123,587</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">37,400,352</td>
<td align="right">36,222,747</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">37,870,450</td>
<td align="right">36,702,998</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">533,470,400</td>
<td align="right">517,417,743</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">215,527,066</td>
<td align="right">209,652,869</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">653,311</td>
<td align="right">639,148</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">51,147,249</td>
<td align="right">50,092,559</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">263,492,705</td>
<td align="right">258,333,223</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,037,328</td>
<td align="right">8,861,059</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">53,463,097</td>
<td align="right">52,445,785</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">265,395,778</td>
<td align="right">260,870,659</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,175,823</td>
<td align="right">81,904,343</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,385,658</td>
<td align="right">1,031,687,328</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">8,433,391</td>
<td align="right">8,314,594</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">638,889,856</td>
<td align="right">631,857,204</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,020,360</td>
<td align="right">91,060,220</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,003,904</td>
<td align="right">222,980,377</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">3,465,240</td>
<td align="right">3,435,760</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,976,353</td>
<td align="right">471,943,780</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">201,328,727</td>
<td align="right">199,661,748</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,153,572</td>
<td align="right">266,074,699</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,252,449</td>
<td align="right">21,094,622</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,908,470</td>
<td align="right">230,257,956</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">695,246</td>
<td align="right">692,329</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,588,019</td>
<td align="right">8,552,361</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">230,390,759</td>
<td align="right">229,439,603</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">15,027,140</td>
<td align="right">14,974,548</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,633,797,605</td>
<td align="right">2,628,276,851</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">17,508,534</td>
<td align="right">17,475,900</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">108,611,836</td>
<td align="right">108,807,526</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,619,195</td>
<td align="right">274,464,922</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">485,141,815</td>
<td align="right">484,960,969</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,840,586</td>
<td align="right">3,840,056</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,064</td>
<td align="right">15,065</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">71,203,587</td>
<td align="right">71,200,391</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,260,789</td>
<td align="right">21,260,531</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,818,552</td>
<td align="right">20,818,313</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,823,847</td>
<td align="right">1,823,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,348,719</td>
<td align="right">20,348,897</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,958,436</td>
<td align="right">5,958,452</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,403,188</td>
<td align="right">173,403,174</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,338,887</td>
<td align="right">233,338,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,302,300</td>
<td align="right">94,302,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,694,000</td>
<td align="right">77,694,000</td>
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
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">622,440</td>
<td align="right">622,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,700</td>
<td align="right">157,700</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">144,080</td>
<td align="right">144,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">91,840</td>
<td align="right">91,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">91,640</td>
<td align="right">91,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">47,200</td>
<td align="right">47,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,800</td>
<td align="right">28,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,460</td>
<td align="right">27,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,040</td>
<td align="right">21,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,200</td>
<td align="right">2,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,120</td>
<td align="right">1,120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">420</td>
<td align="right">420</td>
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
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">29,500,920</td>
<td align="right">0.3%</td>
<td align="right">20,415,620</td>
<td align="right">0.2%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">385,881,588</td>
<td align="right">3.9%</td>
<td align="right">294,873,685</td>
<td align="right">3.0%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,430,172,258</td>
<td align="right">96.1%</td>
<td align="right">9,406,943,199</td>
<td align="right">96.9%</td>
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
<td align="left">Success</td>
<td align="right">597,550</td>
<td align="right">35.0%</td>
<td align="right">426,170</td>
<td align="right">30.0%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,108,379</td>
<td align="right">65.0%</td>
<td align="right">993,591</td>
<td align="right">70.0%</td>
<td align="right">-10.4%</td>
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
<td align="left">lshift</td>
<td align="right">5,665</td>
<td align="right">0.5%</td>
<td align="right">2,605</td>
<td align="right">0.3%</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,646</td>
<td align="right">7.4%</td>
<td align="right">53,044</td>
<td align="right">5.3%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">47,098</td>
<td align="right">4.2%</td>
<td align="right">30,736</td>
<td align="right">3.1%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,541</td>
<td align="right">0.5%</td>
<td align="right">3,753</td>
<td align="right">0.4%</td>
<td align="right">-32.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">46,937</td>
<td align="right">4.2%</td>
<td align="right">35,166</td>
<td align="right">3.5%</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,723</td>
<td align="right">0.4%</td>
<td align="right">3,605</td>
<td align="right">0.4%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">7,443</td>
<td align="right">0.7%</td>
<td align="right">6,021</td>
<td align="right">0.6%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,273</td>
<td align="right">1.3%</td>
<td align="right">12,855</td>
<td align="right">1.3%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,540</td>
<td align="right">0.9%</td>
<td align="right">10,440</td>
<td align="right">1.1%</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,660</td>
<td align="right">0.2%</td>
<td align="right">2,460</td>
<td align="right">0.2%</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,606</td>
<td align="right">70.5%</td>
<td align="right">734,061</td>
<td align="right">73.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">6,466</td>
<td align="right">0.6%</td>
<td align="right">6,079</td>
<td align="right">0.6%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">28,076</td>
<td align="right">2.5%</td>
<td align="right">26,630</td>
<td align="right">2.7%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">400</td>
<td align="right">0.0%</td>
<td align="right">380</td>
<td align="right">0.0%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">832</td>
<td align="right">0.1%</td>
<td align="right">814</td>
<td align="right">0.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,439</td>
<td align="right">2.9%</td>
<td align="right">31,890</td>
<td align="right">3.2%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,503</td>
<td align="right">0.9%</td>
<td align="right">10,583</td>
<td align="right">1.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">19,911</td>
<td align="right">1.8%</td>
<td align="right">19,849</td>
<td align="right">2.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.3%</td>
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
<td align="right">732,966,108</td>
<td align="right">10.7%</td>
<td align="right">649,475,907</td>
<td align="right">9.6%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,811,547</td>
<td align="right">0.1%</td>
<td align="right">4,755,049</td>
<td align="right">0.1%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,147,519,788</td>
<td align="right">89.3%</td>
<td align="right">6,135,495,111</td>
<td align="right">90.4%</td>
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
<td align="right">236,616</td>
<td align="right">56.5%</td>
<td align="right">213,479</td>
<td align="right">54.1%</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,976</td>
<td align="right">43.5%</td>
<td align="right">180,925</td>
<td align="right">45.9%</td>
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
<td align="left">out of range</td>
<td align="right">54,660</td>
<td align="right">23.1%</td>
<td align="right">40,580</td>
<td align="right">19.0%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,179</td>
<td align="right">12.8%</td>
<td align="right">22,900</td>
<td align="right">10.7%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,220</td>
<td align="right">6.9%</td>
<td align="right">14,700</td>
<td align="right">6.9%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">125</td>
<td align="right">0.1%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">108,574</td>
<td align="right">45.9%</td>
<td align="right">108,314</td>
<td align="right">50.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,480</td>
<td align="right">8.2%</td>
<td align="right">19,480</td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,340</td>
<td align="right">2.3%</td>
<td align="right">5,340</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1,120</td>
<td align="right">0.5%</td>
<td align="right">1,120</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">820</td>
<td align="right">0.3%</td>
<td align="right">820</td>
<td align="right">0.4%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">179,202,480</td>
<td align="right">1.2%</td>
<td align="right">150,800,561</td>
<td align="right">1.1%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">660,272,522</td>
<td align="right">4.6%</td>
<td align="right">632,225,857</td>
<td align="right">4.4%</td>
<td align="right">-4.2%</td>
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
<td align="right">28,800</td>
<td align="right">0.0%</td>
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
<td align="right">13,692,671,525</td>
<td align="right">95.4%</td>
<td align="right">13,700,871,968</td>
<td align="right">95.6%</td>
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
<td align="left">Success</td>
<td align="right">3,906,147</td>
<td align="right">95.9%</td>
<td align="right">3,370,151</td>
<td align="right">95.3%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">165,626</td>
<td align="right">4.1%</td>
<td align="right">165,522</td>
<td align="right">4.7%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">9,220</td>
<td align="right">5.6%</td>
<td align="right">9,200</td>
<td align="right">5.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">156,046</td>
<td align="right">94.2%</td>
<td align="right">155,962</td>
<td align="right">94.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">2,920</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,000</td>
<td align="right">1.2%</td>
<td align="right">2,000</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">940</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">360</td>
<td align="right">0.2%</td>
<td align="right">360</td>
<td align="right">0.2%</td>
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
<td align="right">99,436,195</td>
<td align="right">1.6%</td>
<td align="right">74,183,831</td>
<td align="right">1.2%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,062,857</td>
<td align="right">0.0%</td>
<td align="right">991,852</td>
<td align="right">0.0%</td>
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
<td align="right">6,115,171,512</td>
<td align="right">98.4%</td>
<td align="right">6,114,892,097</td>
<td align="right">98.8%</td>
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
<td align="right">149,140</td>
<td align="right">66.2%</td>
<td align="right">138,390</td>
<td align="right">65.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">76,108</td>
<td align="right">33.8%</td>
<td align="right">74,554</td>
<td align="right">35.0%</td>
<td align="right">-2.0%</td>
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
<td align="right">14,369</td>
<td align="right">9.6%</td>
<td align="right">9,811</td>
<td align="right">7.1%</td>
<td align="right">-31.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.8%</td>
<td align="right">2,260</td>
<td align="right">1.6%</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">42,444</td>
<td align="right">28.5%</td>
<td align="right">39,208</td>
<td align="right">28.3%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,120</td>
<td align="right">12.8%</td>
<td align="right">18,420</td>
<td align="right">13.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">27,125</td>
<td align="right">18.2%</td>
<td align="right">26,140</td>
<td align="right">18.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">12,088</td>
<td align="right">8.1%</td>
<td align="right">11,745</td>
<td align="right">8.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,869</td>
<td align="right">11.3%</td>
<td align="right">16,403</td>
<td align="right">11.9%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,425</td>
<td align="right">1.0%</td>
<td align="right">1,423</td>
<td align="right">1.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">7.2%</td>
<td align="right">10,680</td>
<td align="right">7.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">920</td>
<td align="right">0.6%</td>
<td align="right">920</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">840</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">540</td>
<td align="right">0.4%</td>
<td align="right">540</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">1,913,980</td>
<td align="right">0.1%</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">203,701,443</td>
<td align="right">7.6%</td>
<td align="right">201,416,793</td>
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
<td align="right">2,489,228,781</td>
<td align="right">92.4%</td>
<td align="right">2,487,071,221</td>
<td align="right">92.5%</td>
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
<td align="right">61,180</td>
<td align="right">35.3%</td>
<td align="right">49,260</td>
<td align="right">31.0%</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">112,344</td>
<td align="right">64.7%</td>
<td align="right">109,675</td>
<td align="right">69.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">27,358</td>
<td align="right">24.4%</td>
<td align="right">25,467</td>
<td align="right">23.2%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">13,660</td>
<td align="right">12.2%</td>
<td align="right">13,120</td>
<td align="right">12.0%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,686</td>
<td align="right">14.0%</td>
<td align="right">15,328</td>
<td align="right">14.0%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">55,640</td>
<td align="right">49.5%</td>
<td align="right">55,760</td>
<td align="right">50.8%</td>
<td align="right">0.2%</td>
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
<td align="right">2,598,542</td>
<td align="right">0.2%</td>
<td align="right">193,721</td>
<td align="right">0.0%</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">573,825,675</td>
<td align="right">54.5%</td>
<td align="right">436,903,642</td>
<td align="right">48.1%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">478,282,956</td>
<td align="right">45.4%</td>
<td align="right">471,891,601</td>
<td align="right">51.9%</td>
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
<td align="right">97,051</td>
<td align="right">33.2%</td>
<td align="right">51,690</td>
<td align="right">21.0%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">194,888</td>
<td align="right">66.8%</td>
<td align="right">194,210</td>
<td align="right">79.0%</td>
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
<td align="left">dict values</td>
<td align="right">4,240</td>
<td align="right">2.2%</td>
<td align="right">7,160</td>
<td align="right">3.7%</td>
<td align="right">68.9%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,440</td>
<td align="right">1.3%</td>
<td align="right">1,720</td>
<td align="right">0.9%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">34,905</td>
<td align="right">17.9%</td>
<td align="right">32,834</td>
<td align="right">16.9%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,540</td>
<td align="right">3.4%</td>
<td align="right">6,280</td>
<td align="right">3.2%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,100</td>
<td align="right">2.6%</td>
<td align="right">4,920</td>
<td align="right">2.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,164</td>
<td align="right">5.7%</td>
<td align="right">10,883</td>
<td align="right">5.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,959</td>
<td align="right">5.1%</td>
<td align="right">9,873</td>
<td align="right">5.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,960</td>
<td align="right">53.9%</td>
<td align="right">104,960</td>
<td align="right">54.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,500</td>
<td align="right">3.3%</td>
<td align="right">6,500</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,180</td>
<td align="right">2.1%</td>
<td align="right">4,180</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,300</td>
<td align="right">1.7%</td>
<td align="right">3,300</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">620</td>
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
<tr>
<td align="left">string</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
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
<td align="right">395,253,756</td>
<td align="right">2.3%</td>
<td align="right">291,668,675</td>
<td align="right">1.7%</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,471,526,170</td>
<td align="right">8.4%</td>
<td align="right">1,272,102,277</td>
<td align="right">7.3%</td>
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
<td align="right">16,046,528,775</td>
<td align="right">91.6%</td>
<td align="right">16,044,805,161</td>
<td align="right">92.6%</td>
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
<td align="right">304,720</td>
<td align="right">0.0%</td>
<td align="right">304,720</td>
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
<td align="right">8,071,344</td>
<td align="right">89.4%</td>
<td align="right">6,117,619</td>
<td align="right">87.6%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">958,475</td>
<td align="right">10.6%</td>
<td align="right">868,891</td>
<td align="right">12.4%</td>
<td align="right">-9.3%</td>
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
<td align="right">157,029</td>
<td align="right">16.4%</td>
<td align="right">99,175</td>
<td align="right">11.4%</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,623</td>
<td align="right">1.8%</td>
<td align="right">14,950</td>
<td align="right">1.7%</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">258,570</td>
<td align="right">27.0%</td>
<td align="right">240,854</td>
<td align="right">27.7%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">320</td>
<td align="right">0.0%</td>
<td align="right">300</td>
<td align="right">0.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">27,080</td>
<td align="right">2.8%</td>
<td align="right">25,460</td>
<td align="right">2.9%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,544</td>
<td align="right">0.6%</td>
<td align="right">5,240</td>
<td align="right">0.6%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">86,720</td>
<td align="right">9.0%</td>
<td align="right">82,392</td>
<td align="right">9.5%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">18,380</td>
<td align="right">1.9%</td>
<td align="right">17,779</td>
<td align="right">2.0%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">163,663</td>
<td align="right">17.1%</td>
<td align="right">158,978</td>
<td align="right">18.3%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">88,944</td>
<td align="right">9.3%</td>
<td align="right">90,327</td>
<td align="right">10.4%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">76,642</td>
<td align="right">8.0%</td>
<td align="right">75,764</td>
<td align="right">8.7%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,120</td>
<td align="right">2.1%</td>
<td align="right">19,932</td>
<td align="right">2.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,480</td>
<td align="right">1.6%</td>
<td align="right">15,380</td>
<td align="right">1.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,200</td>
<td align="right">1.3%</td>
<td align="right">12,200</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,380</td>
<td align="right">0.6%</td>
<td align="right">5,380</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,900</td>
<td align="right">0.3%</td>
<td align="right">2,900</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">1,140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,441,405,538</td>
<td align="right">99.6%</td>
<td align="right">5,732,686,643</td>
<td align="right">99.6%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">441,297</td>
<td align="right">0.0%</td>
<td align="right">441,548</td>
<td align="right">0.0%</td>
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
<td align="right">20,324,966</td>
<td align="right">0.4%</td>
<td align="right">20,325,341</td>
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
<td align="right">11,380</td>
<td align="right">0.0%</td>
<td align="right">11,380</td>
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
<td align="right">465,050</td>
<td align="right">100.0%</td>
<td align="right">465,104</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">84,244,891</td>
<td align="right">100.0%</td>
<td align="right">84,311,151</td>
<td align="right">100.0%</td>
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
<td align="right">7,544</td>
<td align="right">0.0%</td>
<td align="right">7,545</td>
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
<td align="right">7,520</td>
<td align="right">100.0%</td>
<td align="right">7,520</td>
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
<td align="right">786,230,840</td>
<td align="right">81.9%</td>
<td align="right">786,230,773</td>
<td align="right">81.9%</td>
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
<td align="right">173,365,468</td>
<td align="right">18.1%</td>
<td align="right">173,365,454</td>
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
<td align="right">27,480</td>
<td align="right">0.0%</td>
<td align="right">27,480</td>
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
<td align="right">5,440</td>
<td align="right">8.3%</td>
<td align="right">5,440</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,760</td>
<td align="right">91.7%</td>
<td align="right">59,760</td>
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
<td align="right">55.5%</td>
<td align="right">33,180</td>
<td align="right">55.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">14,240</td>
<td align="right">23.8%</td>
<td align="right">14,240</td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">10,080</td>
<td align="right">16.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
<td align="right">2,260</td>
<td align="right">3.8%</td>
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
<td align="right">139,310,592</td>
<td align="right">4.8%</td>
<td align="right">105,514,243</td>
<td align="right">3.6%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">187,641,906</td>
<td align="right">6.4%</td>
<td align="right">153,429,250</td>
<td align="right">5.3%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,719,089,839</td>
<td align="right">93.5%</td>
<td align="right">2,742,064,551</td>
<td align="right">94.6%</td>
<td align="right">0.8%</td>
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
<td align="right">2,724,469</td>
<td align="right">96.8%</td>
<td align="right">2,086,977</td>
<td align="right">95.8%</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,466</td>
<td align="right">3.2%</td>
<td align="right">90,575</td>
<td align="right">4.2%</td>
<td align="right">-1.0%</td>
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
<td align="right">840</td>
<td align="right">0.9%</td>
<td align="right">800</td>
<td align="right">0.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,060</td>
<td align="right">3.3%</td>
<td align="right">2,920</td>
<td align="right">3.2%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,600</td>
<td align="right">9.4%</td>
<td align="right">8,220</td>
<td align="right">9.1%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,560</td>
<td align="right">34.5%</td>
<td align="right">31,240</td>
<td align="right">34.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,940</td>
<td align="right">5.4%</td>
<td align="right">4,936</td>
<td align="right">5.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">13,960</td>
<td align="right">15.3%</td>
<td align="right">13,949</td>
<td align="right">15.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,726</td>
<td align="right">10.6%</td>
<td align="right">9,730</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,480</td>
<td align="right">8.2%</td>
<td align="right">7,480</td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,400</td>
<td align="right">7.0%</td>
<td align="right">6,400</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">4,760</td>
<td align="right">5.2%</td>
<td align="right">4,760</td>
<td align="right">5.3%</td>
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
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">60</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">231,798,379</td>
<td align="right">20.9%</td>
<td align="right">230,148,567</td>
<td align="right">20.8%</td>
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
<td align="right">876,380,587</td>
<td align="right">79.1%</td>
<td align="right">875,547,975</td>
<td align="right">79.2%</td>
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
<td align="right">2,900</td>
<td align="right">0.0%</td>
<td align="right">2,900</td>
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
<td align="right">99,869</td>
<td align="right">88.4%</td>
<td align="right">99,169</td>
<td align="right">88.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,122</td>
<td align="right">11.6%</td>
<td align="right">13,120</td>
<td align="right">11.7%</td>
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
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">6.5%</td>
<td align="right">6,200</td>
<td align="right">6.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,469</td>
<td align="right">7.5%</td>
<td align="right">7,309</td>
<td align="right">7.4%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">39,640</td>
<td align="right">39.7%</td>
<td align="right">39,380</td>
<td align="right">39.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">43,420</td>
<td align="right">43.5%</td>
<td align="right">43,420</td>
<td align="right">43.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
<td align="right">1,360</td>
<td align="right">1.4%</td>
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
<td align="right">223,436,825</td>
<td align="right">3.5%</td>
<td align="right">160,786,520</td>
<td align="right">2.6%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">24,901,632</td>
<td align="right">0.4%</td>
<td align="right">19,645,559</td>
<td align="right">0.3%</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,093,917,823</td>
<td align="right">96.4%</td>
<td align="right">6,122,652,331</td>
<td align="right">97.4%</td>
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
<td align="right">272,257</td>
<td align="right">29.1%</td>
<td align="right">216,785</td>
<td align="right">27.8%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">663,535</td>
<td align="right">70.9%</td>
<td align="right">564,417</td>
<td align="right">72.2%</td>
<td align="right">-14.9%</td>
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
<td align="right">13,205</td>
<td align="right">4.9%</td>
<td align="right">6,730</td>
<td align="right">3.1%</td>
<td align="right">-49.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">95,881</td>
<td align="right">35.2%</td>
<td align="right">54,782</td>
<td align="right">25.3%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.5%</td>
<td align="right">1,640</td>
<td align="right">0.8%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">81,425</td>
<td align="right">29.9%</td>
<td align="right">74,367</td>
<td align="right">34.3%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,320</td>
<td align="right">6.4%</td>
<td align="right">16,997</td>
<td align="right">7.8%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,027</td>
<td align="right">1.8%</td>
<td align="right">4,957</td>
<td align="right">2.3%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">36,730</td>
<td align="right">13.5%</td>
<td align="right">36,269</td>
<td align="right">16.7%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">12,259</td>
<td align="right">4.5%</td>
<td align="right">12,136</td>
<td align="right">5.6%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">7,810</td>
<td align="right">2.9%</td>
<td align="right">7,767</td>
<td align="right">3.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">720</td>
<td align="right">0.3%</td>
<td align="right">720</td>
<td align="right">0.3%</td>
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
<td align="right">194,079</td>
<td align="right">0.0%</td>
<td align="right">88,118</td>
<td align="right">0.0%</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,577,205,029</td>
<td align="right">100.0%</td>
<td align="right">1,565,331,982</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">3,080</td>
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
<td align="right">1,852</td>
<td align="right">5.8%</td>
<td align="right">1,774</td>
<td align="right">5.6%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,168</td>
<td align="right">94.2%</td>
<td align="right">30,180</td>
<td align="right">94.4%</td>
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
<td align="right">380</td>
<td align="right">20.5%</td>
<td align="right">320</td>
<td align="right">18.0%</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.0%</td>
<td align="right">240</td>
<td align="right">13.5%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">1,212</td>
<td align="right">65.4%</td>
<td align="right">1,214</td>
<td align="right">68.4%</td>
<td align="right">0.2%</td>
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
<td align="right">857,562,470</td>
<td align="right">0.8%</td>
<td align="right">674,273,455</td>
<td align="right">0.7%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">60,455,172,206</td>
<td align="right">55.1%</td>
<td align="right">49,870,033,905</td>
<td align="right">54.4%</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">11,021,879,396</td>
<td align="right">10.1%</td>
<td align="right">9,243,525,166</td>
<td align="right">10.1%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,300,425,791</td>
<td align="right">34.0%</td>
<td align="right">31,855,118,572</td>
<td align="right">34.8%</td>
<td align="right">-14.6%</td>
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
<td align="right">223,436,825</td>
<td align="right">4.6%</td>
<td align="right">160,786,520</td>
<td align="right">3.7%</td>
<td align="right">-28.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">385,881,588</td>
<td align="right">7.9%</td>
<td align="right">294,873,685</td>
<td align="right">6.8%</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">187,641,906</td>
<td align="right">3.9%</td>
<td align="right">153,429,250</td>
<td align="right">3.5%</td>
<td align="right">-18.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,471,526,170</td>
<td align="right">30.2%</td>
<td align="right">1,272,102,277</td>
<td align="right">29.3%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">732,966,108</td>
<td align="right">15.1%</td>
<td align="right">649,475,907</td>
<td align="right">15.0%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">660,272,522</td>
<td align="right">13.6%</td>
<td align="right">632,225,857</td>
<td align="right">14.6%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">478,282,956</td>
<td align="right">9.8%</td>
<td align="right">471,891,601</td>
<td align="right">10.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">203,701,443</td>
<td align="right">4.2%</td>
<td align="right">201,416,793</td>
<td align="right">4.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">231,798,379</td>
<td align="right">4.8%</td>
<td align="right">230,148,567</td>
<td align="right">5.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,365,468</td>
<td align="right">3.6%</td>
<td align="right">173,365,454</td>
<td align="right">4.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">127,520,160</td>
<td align="right">13.6%</td>
<td align="right">82,917,940</td>
<td align="right">11.0%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,361,970</td>
<td align="right">3.8%</td>
<td align="right">23,250,136</td>
<td align="right">3.1%</td>
<td align="right">-34.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">35,195,387</td>
<td align="right">3.8%</td>
<td align="right">24,923,530</td>
<td align="right">3.3%</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">103,743,186</td>
<td align="right">11.1%</td>
<td align="right">77,361,429</td>
<td align="right">10.3%</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">24,161,732</td>
<td align="right">2.6%</td>
<td align="right">18,210,523</td>
<td align="right">2.4%</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">115,125,200</td>
<td align="right">12.3%</td>
<td align="right">87,280,060</td>
<td align="right">11.6%</td>
<td align="right">-24.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">169,144,653</td>
<td align="right">18.1%</td>
<td align="right">137,250,926</td>
<td align="right">18.2%</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,496,864</td>
<td align="right">2.9%</td>
<td align="right">27,496,834</td>
<td align="right">3.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,899,147</td>
<td align="right">8.3%</td>
<td align="right">77,899,187</td>
<td align="right">10.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,899,147</td>
<td align="right">8.3%</td>
<td align="right">77,899,187</td>
<td align="right">10.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,297,780</td>
<td align="right">0.1%</td>
<td align="right">4,417,700</td>
<td align="right">0.1%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">857,436,774</td>
<td align="right">9.8%</td>
<td align="right">851,838,409</td>
<td align="right">9.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,111,675,241</td>
<td align="right">69.8%</td>
<td align="right">6,083,659,254</td>
<td align="right">69.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,638,220,513</td>
<td align="right">30.2%</td>
<td align="right">2,632,776,742</td>
<td align="right">30.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,638,220,513</td>
<td align="right">30.2%</td>
<td align="right">2,632,776,742</td>
<td align="right">30.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">550,865,194</td>
<td align="right">6.3%</td>
<td align="right">551,881,297</td>
<td align="right">6.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,966,008,202</td>
<td align="right">79.6%</td>
<td align="right">6,957,349,297</td>
<td align="right">79.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,775,457,159</td>
<td align="right">20.3%</td>
<td align="right">1,776,491,833</td>
<td align="right">20.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,780,783,739</td>
<td align="right">20.4%</td>
<td align="right">1,780,938,333</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">333,237,341</td>
<td align="right">3.8%</td>
<td align="right">333,251,698</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,595,127</td>
<td align="right">1.0%</td>
<td align="right">84,594,069</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,096,062</td>
<td align="right">0.4%</td>
<td align="right">31,096,055</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,206</td>
<td align="right">2.0%</td>
<td align="right">175,480,213</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,800</td>
<td align="right">0.0%</td>
<td align="right">28,800</td>
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
<td align="left">Interpreter increfs</td>
<td align="right">49,984,103,580</td>
<td align="right">49,984,103,580 / 0 !!</td>
<td align="right">43,074,146,557</td>
<td align="right">43,074,146,557 / 0 !!</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">65,658,004,455</td>
<td align="right">65,658,004,455 / 0 !!</td>
<td align="right">59,629,559,424</td>
<td align="right">59,629,559,424 / 0 !!</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,778,329</td>
<td align="right"></td>
<td align="right">7,279,118</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">92,161,874,921</td>
<td align="right">92,161,874,921 / 0 !!</td>
<td align="right">97,945,019,357</td>
<td align="right">97,945,019,357 / 0 !!</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">99,328,133,378</td>
<td align="right">99,328,133,378 / 0 !!</td>
<td align="right">104,218,189,557</td>
<td align="right">104,218,189,557 / 0 !!</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">65,476,055</td>
<td align="right"></td>
<td align="right">66,537,456</td>
<td align="right"></td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,246,813,712</td>
<td align="right"></td>
<td align="right">3,200,367,027</td>
<td align="right"></td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">72,275,563</td>
<td align="right"></td>
<td align="right">72,835,980</td>
<td align="right"></td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,546,203,386</td>
<td align="right"></td>
<td align="right">13,526,486,736</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,732,586,062</td>
<td align="right">51.5%</td>
<td align="right">12,716,832,856</td>
<td align="right">51.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,840,100,841</td>
<td align="right">51.9%</td>
<td align="right">12,824,382,181</td>
<td align="right">51.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,657,096</td>
<td align="right">0.4%</td>
<td align="right">92,688,402</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,581,374,848</td>
<td align="right"></td>
<td align="right">4,582,541,378</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,601,576</td>
<td align="right"></td>
<td align="right">162,639,180</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">14,857,683</td>
<td align="right">0.1%</td>
<td align="right">14,860,923</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,878,967,798</td>
<td align="right"></td>
<td align="right">11,876,650,833</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,877,035,719</td>
<td align="right">48.1%</td>
<td align="right">11,874,743,535</td>
<td align="right">48.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,140</td>
<td align="right">2.1%</td>
<td align="right">3,382,140</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,920</td>
<td align="right">0.1%</td>
<td align="right">127,920</td>
<td align="right">0.1%</td>
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
<td align="right">114,895,880</td>
<td align="right">19,567,160,139</td>
<td align="right">0</td>
<td align="right">114,847,860</td>
<td align="right">19,559,095,115</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,356,960</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,357,508</td>
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
<td align="right">180</td>
<td align="right">0.0%</td>
<td align="right">360</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,176</td>
<td align="right">0.1%</td>
<td align="right">2,176</td>
<td align="right">0.3%</td>
<td align="right">85.0%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">18,649</td>
<td align="right">2.0%</td>
<td align="right">33,599</td>
<td align="right">4.1%</td>
<td align="right">80.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">565,386</td>
<td align="right">59.9%</td>
<td align="right">380,994</td>
<td align="right">46.5%</td>
<td align="right">-32.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">16,523</td>
<td align="right">1.7%</td>
<td align="right">21,381</td>
<td align="right">2.6%</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,840</td>
<td align="right">0.2%</td>
<td align="right">2,280</td>
<td align="right">0.3%</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">796,281</td>
<td align="right">84.3%</td>
<td align="right">649,002</td>
<td align="right">79.2%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">146,764</td>
<td align="right">15.5%</td>
<td align="right">168,239</td>
<td align="right">20.5%</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">944,221</td>
<td align="right"></td>
<td align="right">819,417</td>
<td align="right"></td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">264,629,325,694</td>
<td align="right">3,665.8%</td>
<td align="right">295,039,633,614</td>
<td align="right">4,237.5%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,218,813,423</td>
<td align="right"></td>
<td align="right">6,962,642,372</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">7,435</td>
<td align="right">5.1%</td>
<td align="right">7,634</td>
<td align="right">4.5%</td>
<td align="right">2.7%</td>
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
<td align="right">2,488</td>
<td align="right">1.7%</td>
<td align="right">9,711</td>
<td align="right">5.8%</td>
<td align="right">290.3%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">146,764</td>
<td align="right"></td>
<td align="right">168,239</td>
<td align="right"></td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">126,885</td>
<td align="right">86.5%</td>
<td align="right">137,494</td>
<td align="right">81.7%</td>
<td align="right">8.4%</td>
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
<td align="right">11,244</td>
<td align="right">7.7%</td>
<td align="right">4,409</td>
<td align="right">2.6%</td>
<td align="right">-60.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">16,785</td>
<td align="right">11.4%</td>
<td align="right">13,121</td>
<td align="right">7.8%</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">39,583</td>
<td align="right">27.0%</td>
<td align="right">38,568</td>
<td align="right">22.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">34,391</td>
<td align="right">23.4%</td>
<td align="right">40,831</td>
<td align="right">24.3%</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">27,436</td>
<td align="right">18.7%</td>
<td align="right">37,520</td>
<td align="right">22.3%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">14,245</td>
<td align="right">9.7%</td>
<td align="right">27,816</td>
<td align="right">16.5%</td>
<td align="right">95.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,880</td>
<td align="right">2.0%</td>
<td align="right">5,414</td>
<td align="right">3.2%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">200</td>
<td align="right">0.1%</td>
<td align="right">560</td>
<td align="right">0.3%</td>
<td align="right">180.0%</td>
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
<td align="right">9,983</td>
<td align="right">6.8%</td>
<td align="right">3,756</td>
<td align="right">2.2%</td>
<td align="right">-62.4%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">11,077</td>
<td align="right">7.5%</td>
<td align="right">7,457</td>
<td align="right">4.4%</td>
<td align="right">-32.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">26,216</td>
<td align="right">17.9%</td>
<td align="right">23,895</td>
<td align="right">14.2%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">38,946</td>
<td align="right">26.5%</td>
<td align="right">40,964</td>
<td align="right">24.3%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,141</td>
<td align="right">16.4%</td>
<td align="right">32,135</td>
<td align="right">19.1%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">11,869</td>
<td align="right">8.1%</td>
<td align="right">19,684</td>
<td align="right">11.7%</td>
<td align="right">65.8%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,993</td>
<td align="right">2.7%</td>
<td align="right">8,003</td>
<td align="right">4.8%</td>
<td align="right">100.4%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">660</td>
<td align="right">0.4%</td>
<td align="right">1,600</td>
<td align="right">1.0%</td>
<td align="right">142.4%</td>
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
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">7,339,340</td>
<td align="right">24,429.9%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,016,240</td>
<td align="right">120,925,100</td>
<td align="right">3,909.1%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,836,780</td>
<td align="right">123,411,660</td>
<td align="right">2,451.5%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,956,780</td>
<td align="right">62,165,200</td>
<td align="right">2,002.5%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">165,769</td>
<td align="right">1,921.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">47,983,225</td>
<td align="right">576,752,243</td>
<td align="right">1,102.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">55,485,505</td>
<td align="right">579,295,683</td>
<td align="right">944.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">9,780,560</td>
<td align="right">90,296,720</td>
<td align="right">823.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">120,094,558</td>
<td align="right">1,080,854,790</td>
<td align="right">800.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">124,632,538</td>
<td align="right">1,062,857,835</td>
<td align="right">752.8%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,789,146</td>
<td align="right">30,680,096</td>
<td align="right">709.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">11,468,900</td>
<td align="right">92,028,280</td>
<td align="right">702.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">69,147,033</td>
<td align="right">483,562,112</td>
<td align="right">599.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">94,477,030</td>
<td align="right">579,300,740</td>
<td align="right">513.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,701,920</td>
<td align="right">13,231,620</td>
<td align="right">389.7%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">828,915,102</td>
<td align="right">2,204,889,698</td>
<td align="right">166.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">236,585,411</td>
<td align="right">594,220,594</td>
<td align="right">151.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">498,902</td>
<td align="right">1,188,661</td>
<td align="right">138.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,731,689</td>
<td align="right">28,424,840</td>
<td align="right">107.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,731,689</td>
<td align="right">27,732,220</td>
<td align="right">102.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">63,986,120</td>
<td align="right">118,137,383</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">128,586,254</td>
<td align="right">228,008,537</td>
<td align="right">77.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">214,849,760</td>
<td align="right">376,102,398</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,513,460</td>
<td align="right">14,565,870</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,635,980</td>
<td align="right">9,063,521</td>
<td align="right">60.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,650,660</td>
<td align="right">9,078,201</td>
<td align="right">60.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">736,200</td>
<td align="right">338,820</td>
<td align="right">-54.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,265,728</td>
<td align="right">6,289,234</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">11,927,840</td>
<td align="right">6,367,880</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">46,376,815</td>
<td align="right">67,222,179</td>
<td align="right">44.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">78,467,886</td>
<td align="right">113,165,877</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">793,442,975</td>
<td align="right">1,122,768,738</td>
<td align="right">41.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">402,911,332</td>
<td align="right">567,513,645</td>
<td align="right">40.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">14,643,934</td>
<td align="right">20,594,925</td>
<td align="right">40.6%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">312,739,308</td>
<td align="right">435,588,319</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">97,078,400</td>
<td align="right">134,750,300</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">97,650,540</td>
<td align="right">135,241,800</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,479,116</td>
<td align="right">48,897,235</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">7,426,048</td>
<td align="right">10,170,840</td>
<td align="right">37.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">163,653,028</td>
<td align="right">223,457,760</td>
<td align="right">36.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,104,347,871</td>
<td align="right">2,856,850,440</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">419,008,167</td>
<td align="right">568,074,187</td>
<td align="right">35.6%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">73,424,040</td>
<td align="right">99,271,080</td>
<td align="right">35.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">386,719,574</td>
<td align="right">521,055,803</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">703,878,359</td>
<td align="right">948,148,661</td>
<td align="right">34.7%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">387,946,834</td>
<td align="right">522,283,063</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">28,040,985</td>
<td align="right">37,731,747</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,991,356,110</td>
<td align="right">2,645,576,607</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">470,028,416</td>
<td align="right">622,154,826</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,532,640</td>
<td align="right">215,910,287</td>
<td align="right">32.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,714,797</td>
<td align="right">103,654,469</td>
<td align="right">31.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,446,941</td>
<td align="right">128,221,953</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">37,035,252</td>
<td align="right">48,366,673</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">96,225,472</td>
<td align="right">124,793,770</td>
<td align="right">29.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">205,336,681</td>
<td align="right">265,781,813</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">182,238,115</td>
<td align="right">235,571,003</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,536,346,867</td>
<td align="right">1,970,818,670</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">252,336,541</td>
<td align="right">183,022,040</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,184,991</td>
<td align="right">119,439,041</td>
<td align="right">26.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,556,868,220</td>
<td align="right">3,231,500,665</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,608,776,860</td>
<td align="right">3,294,747,785</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">669,958</td>
<td align="right">845,638</td>
<td align="right">26.2%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">836,380,887</td>
<td align="right">1,054,993,428</td>
<td align="right">26.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">45,794,668</td>
<td align="right">57,710,879</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">768,117,386</td>
<td align="right">951,658,504</td>
<td align="right">23.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,718,265,616</td>
<td align="right">2,095,916,914</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">395,504,470</td>
<td align="right">480,329,375</td>
<td align="right">21.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,224,235</td>
<td align="right">12,393,930</td>
<td align="right">21.2%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,996,083,446</td>
<td align="right">2,417,110,741</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">51,193,980</td>
<td align="right">61,966,940</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,179,811</td>
<td align="right">7,450,445</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,071,502,473</td>
<td align="right">2,493,188,561</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,799,382,552</td>
<td align="right">2,161,139,656</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,397,433,169</td>
<td align="right">7,643,188,683</td>
<td align="right">19.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,209,767,977</td>
<td align="right">1,424,859,711</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,349,107,117</td>
<td align="right">1,584,084,447</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,327,949,677</td>
<td align="right">1,559,130,627</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,038,391,425</td>
<td align="right">8,233,682,393</td>
<td align="right">17.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,663,790,370</td>
<td align="right">3,088,015,418</td>
<td align="right">15.9%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,799,640</td>
<td align="right">2,083,500</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">380,086,947</td>
<td align="right">440,012,787</td>
<td align="right">15.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,765,608</td>
<td align="right">130,176,570</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">1,041,857,976</td>
<td align="right">1,193,782,491</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,625,905,316</td>
<td align="right">4,151,923,613</td>
<td align="right">14.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">659,910,843</td>
<td align="right">754,302,091</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">852,232</td>
<td align="right">970,515</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,558,153,375</td>
<td align="right">5,187,531,649</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,309,442,905</td>
<td align="right">4,887,275,218</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,384,414,551</td>
<td align="right">1,567,931,204</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right">425,208</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">901,140,630</td>
<td align="right">1,019,653,886</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,522,988</td>
<td align="right">126,888,130</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">60,454,248</td>
<td align="right">68,040,319</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">517,742,389</td>
<td align="right">457,654,632</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">10,330,482,479</td>
<td align="right">11,517,797,825</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">964,009,480</td>
<td align="right">1,071,481,600</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,447,019,464</td>
<td align="right">3,823,599,863</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,466,004</td>
<td align="right">260,887,371</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">657,757,727</td>
<td align="right">728,387,496</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,405,450</td>
<td align="right">35,849,448</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">19,457,144,970</td>
<td align="right">21,488,242,660</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">866,865,065</td>
<td align="right">956,954,923</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,102,786,232</td>
<td align="right">1,217,312,907</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">110,342,500</td>
<td align="right">121,686,596</td>
<td align="right">10.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,686,046</td>
<td align="right">99,907,332</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">533,584,640</td>
<td align="right">480,591,252</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">438,756,773</td>
<td align="right">395,743,899</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,594,296,063</td>
<td align="right">1,742,851,659</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,401,603,367</td>
<td align="right">8,087,204,320</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,250,691,333</td>
<td align="right">6,827,857,211</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">196,586,469</td>
<td align="right">213,797,758</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">374,292,574</td>
<td align="right">406,524,992</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">894,259,721</td>
<td align="right">970,762,442</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,128,032,413</td>
<td align="right">1,223,825,387</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">35,020</td>
<td align="right">37,990</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">16,099,649,750</td>
<td align="right">17,452,073,252</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">899,666,426</td>
<td align="right">825,633,155</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">40,625,681</td>
<td align="right">43,871,304</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,233,461,320</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,074,946,726</td>
<td align="right">1,158,031,655</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,893,578,435</td>
<td align="right">2,039,354,075</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">573,901,369</td>
<td align="right">616,695,479</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,930</td>
<td align="right">413,095,879</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">315,292,945</td>
<td align="right">337,172,608</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">2,021,612,448</td>
<td align="right">2,161,253,711</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,840</td>
<td align="right">1,649,860</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,342,759,886</td>
<td align="right">2,499,271,038</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">275,720,722</td>
<td align="right">257,584,640</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,278,882</td>
<td align="right">103,539,675</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,349,773,202</td>
<td align="right">2,497,827,991</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">163,366,098</td>
<td align="right">173,415,338</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,420,010,145</td>
<td align="right">1,506,863,906</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">322,277,438</td>
<td align="right">302,719,389</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">539,331,880</td>
<td align="right">571,708,578</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">851,544,848</td>
<td align="right">897,355,454</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">86,266,369</td>
<td align="right">90,847,322</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,620,824,570</td>
<td align="right">1,705,492,559</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,313,465,712</td>
<td align="right">5,987,893,899</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,365,162,316</td>
<td align="right">2,486,371,365</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">199,367,867</td>
<td align="right">209,404,939</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,230,782</td>
<td align="right">102,114,557</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">275,803,340</td>
<td align="right">289,093,976</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,965,260</td>
<td align="right">162,313,560</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">588,457,120</td>
<td align="right">616,348,807</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,067,186</td>
<td align="right">675,255,412</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,149,079</td>
<td align="right">239,681,466</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,353,684,555</td>
<td align="right">1,415,154,938</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">250,551,752</td>
<td align="right">261,888,198</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">993,075,340</td>
<td align="right">1,036,890,257</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">254,094,748</td>
<td align="right">265,165,101</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">556,523,127</td>
<td align="right">580,369,074</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">136,066,346</td>
<td align="right">141,751,705</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">136,066,346</td>
<td align="right">141,751,705</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,251,069,869</td>
<td align="right">1,302,599,880</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">674,885,639</td>
<td align="right">702,651,933</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,791,360</td>
<td align="right">60,152,720</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,263,785,791</td>
<td align="right">5,477,494,850</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,343,900,480</td>
<td align="right">1,396,415,020</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">777,695,381</td>
<td align="right">807,679,706</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">778,150,261</td>
<td align="right">808,135,586</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,679,073,680</td>
<td align="right">1,743,131,230</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,605,592,816</td>
<td align="right">5,815,669,798</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,218,813,423</td>
<td align="right">6,962,642,372</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,704,952</td>
<td align="right">166,162,694</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">143,126,582</td>
<td align="right">147,655,055</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">285,822,218</td>
<td align="right">294,502,552</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">2,333,458</td>
<td align="right">2,403,992</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,639,611,895</td>
<td align="right">9,920,457,290</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,502,087,940</td>
<td align="right">1,545,621,933</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,840,917,676</td>
<td align="right">2,921,380,058</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,835,392,729</td>
<td align="right">1,886,475,928</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,820,564</td>
<td align="right">10,544,284</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">122,455,118</td>
<td align="right">125,334,925</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,633,494,919</td>
<td align="right">3,716,137,323</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,751,745,232</td>
<td align="right">1,790,884,968</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,351,620</td>
<td align="right">7,514,100</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,993,774,410</td>
<td align="right">2,927,812,542</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">991,686,656</td>
<td align="right">1,011,781,831</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">994,609,802</td>
<td align="right">974,557,356</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">186,667,720</td>
<td align="right">190,427,561</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,893,256,933</td>
<td align="right">2,950,219,365</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,297,810,954</td>
<td align="right">2,342,270,569</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,571,125,182</td>
<td align="right">1,540,919,680</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,034,432,686</td>
<td align="right">2,068,987,021</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,214,098,838</td>
<td align="right">3,163,434,374</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">919,964,830</td>
<td align="right">933,823,887</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">150,540</td>
<td align="right">152,540</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,839,063,879</td>
<td align="right">3,883,797,710</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">144,616,990</td>
<td align="right">146,295,676</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,240,000</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">131,694,874</td>
<td align="right">132,862,079</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">149,626,956</td>
<td align="right">150,745,503</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,380,991,335</td>
<td align="right">14,282,644,289</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">173,973,160</td>
<td align="right">175,150,520</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">731,141,237</td>
<td align="right">735,767,695</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,769,000</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">247,598,040</td>
<td align="right">249,108,721</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">80,260,400</td>
<td align="right">80,730,840</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">869,477,168</td>
<td align="right">873,825,425</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">66,679,352</td>
<td align="right">66,357,808</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,827,691,488</td>
<td align="right">1,835,298,892</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,261,208</td>
<td align="right">520,340,014</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">644,023,111</td>
<td align="right">645,673,074</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">12,688,620</td>
<td align="right">12,667,772</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,493,780</td>
<td align="right">32,546,340</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,691,148,603</td>
<td align="right">4,685,038,557</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,474,553</td>
<td align="right">68,519,905</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">62,940,240</td>
<td align="right">62,970,400</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">581,940</td>
<td align="right">581,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">36,020</td>
<td align="right">36,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALLER_IP</td>
<td align="right"></td>
<td align="right">1,819,718,973</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">72,962,411</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">19,540,820</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_EXIT_INIT_CHECK</td>
<td align="right"></td>
<td align="right">960,140</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">1,460</td>
<td align="right">2,300</td>
<td align="right">57.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">4,560</td>
<td align="right">5,901</td>
<td align="right">29.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">35,920</td>
<td align="right">43,164</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">157,641</td>
<td align="right">169,541</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">45,038</td>
<td align="right">48,352</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">820</td>
<td align="right">840</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,420</td>
<td align="right">34,320</td>
<td align="right">-0.3%</td>
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
<td align="right">1,106</td>
<td align="right">1,107</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,106</td>
<td align="right">1,107</td>
<td align="right">0.1%</td>
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
<td align="right">300</td>
<td align="right">300</td>
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
<td align="right">420</td>
<td align="right">420</td>
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
<td align="right">1,780</td>
<td align="right">1,780</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
