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
<td align="right">2,373,936</td>
<td align="right">1,573,186</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">2,268,178</td>
<td align="right">1,696,539</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">6,581,077</td>
<td align="right">6,128,785</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,884,452</td>
<td align="right">6,583,443</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">75,668,884</td>
<td align="right">78,394,532</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">83,122,194</td>
<td align="right">80,606,110</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">251,011,929</td>
<td align="right">256,763,640</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">40,249,798</td>
<td align="right">39,443,940</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">106,080,576</td>
<td align="right">108,175,479</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">129,956,570</td>
<td align="right">132,481,966</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,808,791</td>
<td align="right">1,774,317</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">9,605,555</td>
<td align="right">9,458,569</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">7,566,433</td>
<td align="right">7,451,129</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,561,889</td>
<td align="right">17,333,321</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">479,620</td>
<td align="right">474,820</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,723,881</td>
<td align="right">80,921,225</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">212,154,614</td>
<td align="right">214,053,364</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">386,152,122</td>
<td align="right">382,795,206</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">169,979,438</td>
<td align="right">168,719,939</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">327,887,507</td>
<td align="right">330,121,251</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">152,640</td>
<td align="right">151,680</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">83,788,560</td>
<td align="right">84,303,380</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,358,557</td>
<td align="right">53,071,379</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">111,121,425</td>
<td align="right">110,537,447</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">203,633,726</td>
<td align="right">202,599,114</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">102,388,623</td>
<td align="right">101,874,140</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">115,858,547</td>
<td align="right">116,343,700</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">699,696,262</td>
<td align="right">696,931,574</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">384,276,883</td>
<td align="right">382,797,985</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">574,098,307</td>
<td align="right">571,904,116</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,612,872</td>
<td align="right">9,580,062</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">70,815,823</td>
<td align="right">70,582,565</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,227,017,303</td>
<td align="right">1,223,001,197</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">422,349,724</td>
<td align="right">423,700,541</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">85,211,021</td>
<td align="right">84,950,142</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,120,721</td>
<td align="right">96,854,683</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">285,691,968</td>
<td align="right">284,954,173</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">474,051,407</td>
<td align="right">472,843,749</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">142,040</td>
<td align="right">141,720</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">289,120,658</td>
<td align="right">288,478,261</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,585,531,682</td>
<td align="right">1,582,154,179</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,942,693</td>
<td align="right">49,039,696</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">188,373,452</td>
<td align="right">188,003,941</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">94,553,998</td>
<td align="right">94,729,291</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">67,999,950</td>
<td align="right">67,884,837</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,224,779,653</td>
<td align="right">3,219,321,367</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">289,967,440</td>
<td align="right">289,479,507</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,091,735,946</td>
<td align="right">3,086,542,212</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,293,431</td>
<td align="right">58,387,843</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">72,803,991</td>
<td align="right">72,689,495</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">887,913,763</td>
<td align="right">889,296,148</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">414,935,897</td>
<td align="right">415,577,942</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">392,468,335</td>
<td align="right">391,889,379</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,812,441,799</td>
<td align="right">3,807,115,363</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">581,038,003</td>
<td align="right">580,306,531</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,928,897,538</td>
<td align="right">4,922,825,320</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">372,812,108</td>
<td align="right">372,363,423</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">150,730,652</td>
<td align="right">150,553,970</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">33,150,818</td>
<td align="right">33,112,879</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,384,581,431</td>
<td align="right">2,381,909,661</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">1,097,241,928</td>
<td align="right">1,096,043,293</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,144,505,216</td>
<td align="right">1,143,255,448</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">958,662,022</td>
<td align="right">957,628,185</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">283,960,183</td>
<td align="right">283,668,314</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">195,367,098</td>
<td align="right">195,567,539</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,991,741,855</td>
<td align="right">3,987,662,500</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">586,581,514</td>
<td align="right">586,012,203</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">367,370,047</td>
<td align="right">367,014,223</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">225,163,719</td>
<td align="right">224,955,193</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">378,817,522</td>
<td align="right">378,481,762</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">981,566,740</td>
<td align="right">980,707,325</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">12,957,988</td>
<td align="right">12,946,709</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">12,965,748</td>
<td align="right">12,954,469</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,176,673,579</td>
<td align="right">4,173,102,274</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">12,974,789</td>
<td align="right">12,963,825</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,299,219,430</td>
<td align="right">2,301,150,573</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">1,754,439</td>
<td align="right">1,752,970</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,211,993,212</td>
<td align="right">2,210,190,813</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">246,214,282</td>
<td align="right">246,405,207</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,663,782,490</td>
<td align="right">2,661,774,238</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">216,667,696</td>
<td align="right">216,524,153</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">217,312,636</td>
<td align="right">217,174,100</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">5,466,511,390</td>
<td align="right">5,463,065,228</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">258,577,071</td>
<td align="right">258,730,414</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">214,248</td>
<td align="right">214,373</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">221,493,025</td>
<td align="right">221,366,734</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,364,142,879</td>
<td align="right">1,363,521,746</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">134,495,444</td>
<td align="right">134,553,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">18,945,254,479</td>
<td align="right">18,937,145,790</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">321,090,876</td>
<td align="right">320,959,211</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">312,560,161</td>
<td align="right">312,444,686</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">343,699,176</td>
<td align="right">343,584,676</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,209,685</td>
<td align="right">9,206,674</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">622,206,450</td>
<td align="right">622,019,938</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">352,994,018</td>
<td align="right">353,099,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,643,692</td>
<td align="right">9,640,813</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">356,426,610</td>
<td align="right">356,523,223</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,887,111,904</td>
<td align="right">4,885,821,332</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">399,850,093</td>
<td align="right">399,944,469</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">278,788,393</td>
<td align="right">278,723,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">122,049,030</td>
<td align="right">122,073,393</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">18,667,518</td>
<td align="right">18,663,814</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,447</td>
<td align="right">15,444</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">687,239</td>
<td align="right">687,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">207,249</td>
<td align="right">207,285</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">31,400,841</td>
<td align="right">31,395,405</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">39,860,816</td>
<td align="right">39,855,802</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,911,912,651</td>
<td align="right">4,911,304,364</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">78,150,868</td>
<td align="right">78,159,808</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,873,008</td>
<td align="right">1,873,133</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">506,576,310</td>
<td align="right">506,543,618</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,384,268</td>
<td align="right">4,383,996</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">22,134,073</td>
<td align="right">22,132,754</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,414,409</td>
<td align="right">47,411,723</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,843,086,410</td>
<td align="right">1,843,190,637</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">52,489,441</td>
<td align="right">52,486,561</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">56,323,899</td>
<td align="right">56,321,064</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">65,815,510</td>
<td align="right">65,812,284</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,106,826</td>
<td align="right">91,102,387</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">945,728,903</td>
<td align="right">945,774,487</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,069,718</td>
<td align="right">83,065,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">105,646,262</td>
<td align="right">105,641,462</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">42,153,116</td>
<td align="right">42,154,961</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">98,872,680</td>
<td align="right">98,868,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">397,050,627</td>
<td align="right">397,035,685</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">90,631,700</td>
<td align="right">90,628,500</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">90,636,840</td>
<td align="right">90,633,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,047,368,035</td>
<td align="right">1,047,331,963</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">37,817,080</td>
<td align="right">37,815,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">1,449,900</td>
<td align="right">1,449,852</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,310,081</td>
<td align="right">22,309,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">104,601,884</td>
<td align="right">104,599,418</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,253,079,523</td>
<td align="right">1,253,050,887</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,703,948</td>
<td align="right">555,693,015</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">32,498,901</td>
<td align="right">32,498,290</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">33,217,868</td>
<td align="right">33,217,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">355,802,637</td>
<td align="right">355,797,089</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">184,064,710</td>
<td align="right">184,061,888</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">190,039,366</td>
<td align="right">190,037,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">148,274,372</td>
<td align="right">148,275,863</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">189,368,170</td>
<td align="right">189,366,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">326,501,328</td>
<td align="right">326,499,387</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,279,829</td>
<td align="right">20,279,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">104,897,818</td>
<td align="right">104,897,316</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,867,647</td>
<td align="right">10,867,689</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">47,905,774</td>
<td align="right">47,905,948</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">143,299,744</td>
<td align="right">143,299,465</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">13,641,641</td>
<td align="right">13,641,617</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">273,307,042</td>
<td align="right">273,307,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">172,973,056</td>
<td align="right">172,973,218</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">158,553,991</td>
<td align="right">158,553,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">65,829,457</td>
<td align="right">65,829,447</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">275,110,014</td>
<td align="right">275,110,047</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,546</td>
<td align="right">173,318,540</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">228,622,206</td>
<td align="right">228,622,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,022,049</td>
<td align="right">402,022,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,211,059</td>
<td align="right">786,211,044</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,305,733</td>
<td align="right">233,305,733</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">49,528,140</td>
<td align="right">49,528,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">46,610,564</td>
<td align="right">46,610,564</td>
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
<td align="right">543,680</td>
<td align="right">543,680</td>
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
<td align="left">CALL_INTRINSIC_2</td>
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
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
<td align="right">413,974,709</td>
<td align="right">5.7%</td>
<td align="right">410,618,724</td>
<td align="right">5.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,805,596,062</td>
<td align="right">94.2%</td>
<td align="right">6,805,204,736</td>
<td align="right">94.3%</td>
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
<td align="right">1,087,713</td>
<td align="right">64.8%</td>
<td align="right">1,086,807</td>
<td align="right">64.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">590,560</td>
<td align="right">35.2%</td>
<td align="right">590,535</td>
<td align="right">35.2%</td>
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
<td align="left">or</td>
<td align="right">12,475</td>
<td align="right">1.1%</td>
<td align="right">12,169</td>
<td align="right">1.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">29,692</td>
<td align="right">2.7%</td>
<td align="right">29,197</td>
<td align="right">2.7%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">14,214</td>
<td align="right">1.3%</td>
<td align="right">14,158</td>
<td align="right">1.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,890</td>
<td align="right">0.2%</td>
<td align="right">1,895</td>
<td align="right">0.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">5,030</td>
<td align="right">0.5%</td>
<td align="right">5,024</td>
<td align="right">0.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,749</td>
<td align="right">3.4%</td>
<td align="right">36,721</td>
<td align="right">3.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,611</td>
<td align="right">0.8%</td>
<td align="right">8,606</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">37,911</td>
<td align="right">3.5%</td>
<td align="right">37,890</td>
<td align="right">3.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,464</td>
<td align="right">1.0%</td>
<td align="right">10,463</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,600</td>
<td align="right">71.9%</td>
<td align="right">781,607</td>
<td align="right">71.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">81,605</td>
<td align="right">7.5%</td>
<td align="right">81,605</td>
<td align="right">7.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">32,056</td>
<td align="right">2.9%</td>
<td align="right">32,056</td>
<td align="right">2.9%</td>
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
<td align="left">xor</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">8,844</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">5,528</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
<td align="right">4,724</td>
<td align="right">0.4%</td>
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
<td align="right">2,600</td>
<td align="right">0.2%</td>
<td align="right">2,600</td>
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
<td align="right">416,416,841</td>
<td align="right">8.9%</td>
<td align="right">417,058,794</td>
<td align="right">8.9%</td>
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
<td align="right">4,278,738,383</td>
<td align="right">91.1%</td>
<td align="right">4,278,508,498</td>
<td align="right">91.1%</td>
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
<td align="right">1,740,957</td>
<td align="right">0.0%</td>
<td align="right">1,740,976</td>
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
<td align="right">147,910</td>
<td align="right">56.9%</td>
<td align="right">148,024</td>
<td align="right">56.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">112,103</td>
<td align="right">43.1%</td>
<td align="right">112,100</td>
<td align="right">43.1%</td>
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
<td align="left">out of range</td>
<td align="right">43,760</td>
<td align="right">29.6%</td>
<td align="right">43,880</td>
<td align="right">29.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">30,319</td>
<td align="right">20.5%</td>
<td align="right">30,277</td>
<td align="right">20.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">30,727</td>
<td align="right">20.8%</td>
<td align="right">30,763</td>
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
<td align="right">10.9%</td>
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
<td align="left">tuple slice</td>
<td align="right">124</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.1%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">175,080,238</td>
<td align="right">1.6%</td>
<td align="right">174,536,582</td>
<td align="right">1.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,637,055,346</td>
<td align="right">97.3%</td>
<td align="right">10,628,961,203</td>
<td align="right">97.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">287,099,603</td>
<td align="right">2.6%</td>
<td align="right">287,051,627</td>
<td align="right">2.6%</td>
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
<td align="left">Success</td>
<td align="right">3,764,888</td>
<td align="right">98.1%</td>
<td align="right">3,754,527</td>
<td align="right">98.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">74,294</td>
<td align="right">1.9%</td>
<td align="right">74,128</td>
<td align="right">1.9%</td>
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
<td align="left">wrong number arguments</td>
<td align="right">8,020</td>
<td align="right">10.8%</td>
<td align="right">7,980</td>
<td align="right">10.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">65,934</td>
<td align="right">88.7%</td>
<td align="right">65,808</td>
<td align="right">88.8%</td>
<td align="right">-0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">97,662,855</td>
<td align="right">2.0%</td>
<td align="right">97,396,718</td>
<td align="right">2.0%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,830,114,473</td>
<td align="right">98.0%</td>
<td align="right">4,828,740,181</td>
<td align="right">98.0%</td>
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
<td align="right">734,835</td>
<td align="right">0.0%</td>
<td align="right">734,645</td>
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
<td align="right">128,759</td>
<td align="right">66.8%</td>
<td align="right">128,683</td>
<td align="right">66.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">63,942</td>
<td align="right">33.2%</td>
<td align="right">63,927</td>
<td align="right">33.2%</td>
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
<td align="left">float long</td>
<td align="right">14,369</td>
<td align="right">11.2%</td>
<td align="right">14,325</td>
<td align="right">11.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">24,967</td>
<td align="right">19.4%</td>
<td align="right">24,908</td>
<td align="right">19.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,550</td>
<td align="right">9.0%</td>
<td align="right">11,532</td>
<td align="right">9.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,326</td>
<td align="right">12.7%</td>
<td align="right">16,351</td>
<td align="right">12.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,421</td>
<td align="right">1.1%</td>
<td align="right">1,423</td>
<td align="right">1.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">26,286</td>
<td align="right">20.4%</td>
<td align="right">26,304</td>
<td align="right">20.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">18,740</td>
<td align="right">14.6%</td>
<td align="right">18,740</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
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
<td align="left">set</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">1,620</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,500</td>
<td align="right">1.2%</td>
<td align="right">1,500</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">197,729,124</td>
<td align="right">7.7%</td>
<td align="right">197,929,517</td>
<td align="right">7.7%</td>
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
<td align="right">2,366,573,483</td>
<td align="right">92.3%</td>
<td align="right">2,365,971,749</td>
<td align="right">92.3%</td>
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
<td align="right">96,574</td>
<td align="right">62.2%</td>
<td align="right">96,623</td>
<td align="right">62.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">58,660</td>
<td align="right">37.8%</td>
<td align="right">58,659</td>
<td align="right">37.8%</td>
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
<td align="right">12,771</td>
<td align="right">13.2%</td>
<td align="right">12,822</td>
<td align="right">13.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">22,063</td>
<td align="right">22.8%</td>
<td align="right">22,061</td>
<td align="right">22.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">53,360</td>
<td align="right">55.3%</td>
<td align="right">53,360</td>
<td align="right">55.2%</td>
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
<td align="right">137,564</td>
<td align="right">0.0%</td>
<td align="right">156,981</td>
<td align="right">0.0%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">75,670,182</td>
<td align="right">14.1%</td>
<td align="right">78,413,725</td>
<td align="right">14.6%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">459,905,336</td>
<td align="right">85.8%</td>
<td align="right">458,446,518</td>
<td align="right">85.4%</td>
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
<td align="right">90,410</td>
<td align="right">66.3%</td>
<td align="right">91,560</td>
<td align="right">66.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,856</td>
<td align="right">33.7%</td>
<td align="right">46,228</td>
<td align="right">33.6%</td>
<td align="right">0.8%</td>
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
<td align="left">reversed list</td>
<td align="right">3,060</td>
<td align="right">3.4%</td>
<td align="right">3,760</td>
<td align="right">4.1%</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">35,768</td>
<td align="right">39.6%</td>
<td align="right">36,166</td>
<td align="right">39.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,998</td>
<td align="right">11.1%</td>
<td align="right">10,069</td>
<td align="right">11.0%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,480</td>
<td align="right">7.2%</td>
<td align="right">6,460</td>
<td align="right">7.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">9,044</td>
<td align="right">10.0%</td>
<td align="right">9,045</td>
<td align="right">9.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">7,720</td>
<td align="right">8.5%</td>
<td align="right">7,720</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,240</td>
<td align="right">6.9%</td>
<td align="right">6,240</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">4,240</td>
<td align="right">4.7%</td>
<td align="right">4,240</td>
<td align="right">4.6%</td>
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
<td align="left">seq iter</td>
<td align="right">1,960</td>
<td align="right">2.2%</td>
<td align="right">1,960</td>
<td align="right">2.1%</td>
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
<td align="right">0.3%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">14,273,459,233</td>
<td align="right">92.1%</td>
<td align="right">14,262,577,054</td>
<td align="right">92.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,222,332,715</td>
<td align="right">7.9%</td>
<td align="right">1,221,509,130</td>
<td align="right">7.9%</td>
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
<td align="right">246,709,123</td>
<td align="right">1.6%</td>
<td align="right">246,744,707</td>
<td align="right">1.6%</td>
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
<td align="right">323,880</td>
<td align="right">0.0%</td>
<td align="right">323,880</td>
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
<td align="right">763,786</td>
<td align="right">12.9%</td>
<td align="right">762,951</td>
<td align="right">12.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,179,362</td>
<td align="right">87.1%</td>
<td align="right">5,179,951</td>
<td align="right">87.2%</td>
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
<td align="left">non overriding descriptor</td>
<td align="right">5,542</td>
<td align="right">0.7%</td>
<td align="right">5,418</td>
<td align="right">0.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">54,497</td>
<td align="right">7.1%</td>
<td align="right">54,830</td>
<td align="right">7.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,780</td>
<td align="right">1.8%</td>
<td align="right">13,700</td>
<td align="right">1.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">75,524</td>
<td align="right">9.9%</td>
<td align="right">75,207</td>
<td align="right">9.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">25,980</td>
<td align="right">3.4%</td>
<td align="right">25,880</td>
<td align="right">3.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,240</td>
<td align="right">1.6%</td>
<td align="right">12,200</td>
<td align="right">1.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">250,793</td>
<td align="right">32.8%</td>
<td align="right">250,278</td>
<td align="right">32.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">44,870</td>
<td align="right">5.9%</td>
<td align="right">44,919</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">13,422</td>
<td align="right">1.8%</td>
<td align="right">13,408</td>
<td align="right">1.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">19,740</td>
<td align="right">2.6%</td>
<td align="right">19,720</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">72,780</td>
<td align="right">9.5%</td>
<td align="right">72,760</td>
<td align="right">9.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">148,698</td>
<td align="right">19.5%</td>
<td align="right">148,711</td>
<td align="right">19.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">15,840</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,520</td>
<td align="right">0.7%</td>
<td align="right">5,520</td>
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
<td align="right">438,750</td>
<td align="right">0.0%</td>
<td align="right">436,767</td>
<td align="right">0.0%</td>
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
<td align="right">5,176,374,148</td>
<td align="right">99.6%</td>
<td align="right">5,171,022,139</td>
<td align="right">99.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,287,477</td>
<td align="right">0.4%</td>
<td align="right">20,285,522</td>
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
<td align="right">431,102</td>
<td align="right">100.0%</td>
<td align="right">430,965</td>
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
<td align="right">83,562,592</td>
<td align="right">100.0%</td>
<td align="right">82,725,462</td>
<td align="right">100.0%</td>
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
<td align="right">7,867</td>
<td align="right">0.0%</td>
<td align="right">7,864</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">173,284,206</td>
<td align="right">18.1%</td>
<td align="right">173,284,200</td>
<td align="right">18.1%</td>
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
<td align="right">786,180,399</td>
<td align="right">81.9%</td>
<td align="right">786,180,384</td>
<td align="right">81.9%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,668,638,136</td>
<td align="right">96.4%</td>
<td align="right">2,667,369,734</td>
<td align="right">96.4%</td>
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
<td align="right">98,433,242</td>
<td align="right">3.6%</td>
<td align="right">98,428,100</td>
<td align="right">3.6%</td>
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
<td align="right">68,471,858</td>
<td align="right">2.5%</td>
<td align="right">68,471,986</td>
<td align="right">2.5%</td>
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
<td align="right">62,068</td>
<td align="right">4.3%</td>
<td align="right">61,908</td>
<td align="right">4.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,377,389</td>
<td align="right">95.7%</td>
<td align="right">1,377,383</td>
<td align="right">95.7%</td>
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
<td align="left">property</td>
<td align="right">2,580</td>
<td align="right">4.2%</td>
<td align="right">2,480</td>
<td align="right">4.0%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">4,720</td>
<td align="right">7.6%</td>
<td align="right">4,700</td>
<td align="right">7.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">9,840</td>
<td align="right">15.9%</td>
<td align="right">9,800</td>
<td align="right">15.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">12,920</td>
<td align="right">20.8%</td>
<td align="right">12,920</td>
<td align="right">20.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,748</td>
<td align="right">15.7%</td>
<td align="right">9,748</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,580</td>
<td align="right">13.8%</td>
<td align="right">8,580</td>
<td align="right">13.9%</td>
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
<td align="right">818,324,669</td>
<td align="right">93.6%</td>
<td align="right">817,755,650</td>
<td align="right">93.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">56,264,686</td>
<td align="right">6.4%</td>
<td align="right">56,261,909</td>
<td align="right">6.4%</td>
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
<td align="right">48,587</td>
<td align="right">82.1%</td>
<td align="right">48,536</td>
<td align="right">82.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,626</td>
<td align="right">17.9%</td>
<td align="right">10,619</td>
<td align="right">18.0%</td>
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
<td align="left">other</td>
<td align="right">340</td>
<td align="right">0.7%</td>
<td align="right">320</td>
<td align="right">0.7%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,527</td>
<td align="right">15.5%</td>
<td align="right">7,516</td>
<td align="right">15.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">32,540</td>
<td align="right">67.0%</td>
<td align="right">32,520</td>
<td align="right">67.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">6,480</td>
<td align="right">13.3%</td>
<td align="right">6,480</td>
<td align="right">13.4%</td>
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
<td align="right">5,769,662,519</td>
<td align="right">95.5%</td>
<td align="right">5,764,340,397</td>
<td align="right">95.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">272,880,821</td>
<td align="right">4.5%</td>
<td align="right">272,672,843</td>
<td align="right">4.5%</td>
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
<td align="right">48,989,869</td>
<td align="right">0.8%</td>
<td align="right">48,990,164</td>
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
<td align="right">171,926</td>
<td align="right">13.5%</td>
<td align="right">171,704</td>
<td align="right">13.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,100,841</td>
<td align="right">86.5%</td>
<td align="right">1,100,810</td>
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
<td align="left">other</td>
<td align="right">4,454</td>
<td align="right">2.6%</td>
<td align="right">4,425</td>
<td align="right">2.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">13,114</td>
<td align="right">7.6%</td>
<td align="right">13,062</td>
<td align="right">7.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">47,942</td>
<td align="right">27.9%</td>
<td align="right">47,860</td>
<td align="right">27.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">26,858</td>
<td align="right">15.6%</td>
<td align="right">26,826</td>
<td align="right">15.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,023</td>
<td align="right">26.8%</td>
<td align="right">45,992</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">13,204</td>
<td align="right">7.7%</td>
<td align="right">13,208</td>
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
<td align="left">number</td>
<td align="right">4,831</td>
<td align="right">2.8%</td>
<td align="right">4,831</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,460</td>
<td align="right">0.8%</td>
<td align="right">1,460</td>
<td align="right">0.9%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">186,214</td>
<td align="right">0.0%</td>
<td align="right">186,346</td>
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
<td align="right">1,492,187,207</td>
<td align="right">100.0%</td>
<td align="right">1,491,471,636</td>
<td align="right">100.0%</td>
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
<td align="right">1,770</td>
<td align="right">6.3%</td>
<td align="right">1,775</td>
<td align="right">6.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">26,264</td>
<td align="right">93.7%</td>
<td align="right">26,252</td>
<td align="right">93.7%</td>
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
<td align="left">sequence</td>
<td align="right">1,130</td>
<td align="right">63.8%</td>
<td align="right">1,135</td>
<td align="right">63.9%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">21.5%</td>
<td align="right">380</td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">14.7%</td>
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
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">652,226,063</td>
<td align="right">0.6%</td>
<td align="right">651,735,783</td>
<td align="right">0.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">56,626,327,060</td>
<td align="right">54.4%</td>
<td align="right">56,588,384,727</td>
<td align="right">54.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">37,099,501,252</td>
<td align="right">35.7%</td>
<td align="right">37,076,873,271</td>
<td align="right">35.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">9,645,802,555</td>
<td align="right">9.3%</td>
<td align="right">9,640,143,576</td>
<td align="right">9.3%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">75,670,182</td>
<td align="right">2.3%</td>
<td align="right">78,413,725</td>
<td align="right">2.4%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">413,974,709</td>
<td align="right">12.4%</td>
<td align="right">410,618,724</td>
<td align="right">12.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">97,662,855</td>
<td align="right">2.9%</td>
<td align="right">97,396,718</td>
<td align="right">2.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">416,416,841</td>
<td align="right">12.5%</td>
<td align="right">417,058,794</td>
<td align="right">12.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">197,729,124</td>
<td align="right">5.9%</td>
<td align="right">197,929,517</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">272,880,821</td>
<td align="right">8.2%</td>
<td align="right">272,672,843</td>
<td align="right">8.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,222,332,715</td>
<td align="right">36.7%</td>
<td align="right">1,221,509,130</td>
<td align="right">36.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">287,099,603</td>
<td align="right">8.6%</td>
<td align="right">287,051,627</td>
<td align="right">8.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">98,433,242</td>
<td align="right">3.0%</td>
<td align="right">98,428,100</td>
<td align="right">3.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,284,206</td>
<td align="right">5.2%</td>
<td align="right">173,284,200</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">40,949,493</td>
<td align="right">5.6%</td>
<td align="right">40,958,433</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">73,029,720</td>
<td align="right">10.0%</td>
<td align="right">73,028,068</td>
<td align="right">10.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">90,672,704</td>
<td align="right">12.4%</td>
<td align="right">90,673,872</td>
<td align="right">12.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">24,452,345</td>
<td align="right">3.3%</td>
<td align="right">24,452,499</td>
<td align="right">3.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">25,197,678</td>
<td align="right">3.5%</td>
<td align="right">25,197,806</td>
<td align="right">3.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,874,089</td>
<td align="right">10.7%</td>
<td align="right">77,874,195</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,874,089</td>
<td align="right">10.7%</td>
<td align="right">77,874,195</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,481,361</td>
<td align="right">3.8%</td>
<td align="right">27,481,393</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">100,612,593</td>
<td align="right">13.8%</td>
<td align="right">100,612,585</td>
<td align="right">13.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">43,253,700</td>
<td align="right">5.9%</td>
<td align="right">43,253,700</td>
<td align="right">5.9%</td>
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
<td align="right">225,027,956</td>
<td align="right">2.8%</td>
<td align="right">224,334,229</td>
<td align="right">2.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,522,054,555</td>
<td align="right">18.9%</td>
<td align="right">1,519,652,658</td>
<td align="right">18.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,526,488,695</td>
<td align="right">19.0%</td>
<td align="right">1,524,086,798</td>
<td align="right">19.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,339,175,937</td>
<td align="right">78.8%</td>
<td align="right">6,330,846,093</td>
<td align="right">78.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,387,027,782</td>
<td align="right">29.7%</td>
<td align="right">2,384,355,185</td>
<td align="right">29.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,387,027,782</td>
<td align="right">29.7%</td>
<td align="right">2,384,355,185</td>
<td align="right">29.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,656,327,716</td>
<td align="right">70.3%</td>
<td align="right">5,650,050,445</td>
<td align="right">70.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">860,539,087</td>
<td align="right">10.7%</td>
<td align="right">860,268,387</td>
<td align="right">10.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,565,814</td>
<td align="right">0.9%</td>
<td align="right">71,553,258</td>
<td align="right">0.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">526,928,723</td>
<td align="right">6.6%</td>
<td align="right">526,894,309</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">28,576,994</td>
<td align="right">0.4%</td>
<td align="right">28,576,023</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,357,925</td>
<td align="right">2.6%</td>
<td align="right">211,357,955</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
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
<td align="right">22,143,966</td>
<td align="right"></td>
<td align="right">20,176,300</td>
<td align="right"></td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">29,035,581</td>
<td align="right"></td>
<td align="right">27,188,223</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,059,317</td>
<td align="right"></td>
<td align="right">7,182,064</td>
<td align="right"></td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">19,810,166</td>
<td align="right">0.1%</td>
<td align="right">19,741,311</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">150,014,746</td>
<td align="right"></td>
<td align="right">149,545,678</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,635,258,301</td>
<td align="right"></td>
<td align="right">2,628,389,236</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">66,656,299,311</td>
<td align="right">59.2%</td>
<td align="right">66,584,505,917</td>
<td align="right">59.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">69,438,160,611</td>
<td align="right">53.9%</td>
<td align="right">69,377,781,586</td>
<td align="right">53.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,106,256,594</td>
<td align="right"></td>
<td align="right">3,103,643,944</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,453,499,289</td>
<td align="right">38.6%</td>
<td align="right">6,449,495,312</td>
<td align="right">38.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,455,265,652</td>
<td align="right"></td>
<td align="right">6,451,260,996</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">59,337,887,787</td>
<td align="right">46.1%</td>
<td align="right">59,303,683,387</td>
<td align="right">46.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,616,293,346</td>
<td align="right"></td>
<td align="right">10,610,404,433</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,286,837,651</td>
<td align="right">61.4%</td>
<td align="right">10,281,363,348</td>
<td align="right">61.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,163,326,058</td>
<td align="right">60.7%</td>
<td align="right">10,157,946,236</td>
<td align="right">60.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">45,861,637,040</td>
<td align="right">40.8%</td>
<td align="right">45,847,112,889</td>
<td align="right">40.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,701,427</td>
<td align="right">0.6%</td>
<td align="right">103,675,801</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,271,200</td>
<td align="right">2.2%</td>
<td align="right">3,271,200</td>
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
<td align="right">18,600,000</td>
<td align="right">14,514,424,090</td>
<td align="right">0</td>
<td align="right">18,600,000</td>
<td align="right">14,506,563,416</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,003,734,840</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,002,424,720</td>
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
<td align="right">822</td>
<td align="right">0.1%</td>
<td align="right">680</td>
<td align="right">0.1%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">6,207</td>
<td align="right">6.2%</td>
<td align="right">6,401</td>
<td align="right">6.4%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">199,527,195,856</td>
<td align="right">2,851.5%</td>
<td align="right">197,159,767,028</td>
<td align="right">2,820.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">6,525</td>
<td align="right">0.9%</td>
<td align="right">6,505</td>
<td align="right">0.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">44,411</td>
<td align="right">6.1%</td>
<td align="right">44,480</td>
<td align="right">6.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">436,409</td>
<td align="right">59.5%</td>
<td align="right">435,978</td>
<td align="right">59.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">6,997,388,790</td>
<td align="right"></td>
<td align="right">6,991,419,122</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">632,934</td>
<td align="right">86.4%</td>
<td align="right">632,591</td>
<td align="right">86.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">732,903</td>
<td align="right"></td>
<td align="right">732,545</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">99,969</td>
<td align="right">13.6%</td>
<td align="right">99,954</td>
<td align="right">13.6%</td>
<td align="right">-0.0%</td>
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
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
<td align="right">1,300</td>
<td align="right">0.2%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,362</td>
<td align="right">2.4%</td>
<td align="right">2,360</td>
<td align="right">2.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">99,969</td>
<td align="right"></td>
<td align="right">99,954</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">96,387</td>
<td align="right">96.4%</td>
<td align="right">96,374</td>
<td align="right">96.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">4,414</td>
<td align="right">4.4%</td>
<td align="right">4,420</td>
<td align="right">4.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">18,775</td>
<td align="right">18.8%</td>
<td align="right">18,775</td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,493</td>
<td align="right">31.5%</td>
<td align="right">31,506</td>
<td align="right">31.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">24,554</td>
<td align="right">24.6%</td>
<td align="right">24,546</td>
<td align="right">24.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,140</td>
<td align="right">13.1%</td>
<td align="right">13,131</td>
<td align="right">13.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">5,933</td>
<td align="right">5.9%</td>
<td align="right">5,916</td>
<td align="right">5.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">1,500</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
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
<td align="right">3,514</td>
<td align="right">3.5%</td>
<td align="right">3,520</td>
<td align="right">3.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">13,215</td>
<td align="right">13.2%</td>
<td align="right">13,212</td>
<td align="right">13.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">21,007</td>
<td align="right">21.0%</td>
<td align="right">21,288</td>
<td align="right">21.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">31,659</td>
<td align="right">31.7%</td>
<td align="right">31,610</td>
<td align="right">31.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">15,912</td>
<td align="right">15.9%</td>
<td align="right">15,864</td>
<td align="right">15.9%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">7,796</td>
<td align="right">7.8%</td>
<td align="right">7,840</td>
<td align="right">7.8%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">2,864</td>
<td align="right">2.9%</td>
<td align="right">2,640</td>
<td align="right">2.6%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.4%</td>
<td align="right">400</td>
<td align="right">0.4%</td>
<td align="right">-4.8%</td>
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
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,655,393,854</td>
<td align="right">4,455,931,761</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">61,348,800</td>
<td align="right">58,790,560</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">61,462,900</td>
<td align="right">58,904,660</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">73,939,832</td>
<td align="right">71,154,717</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,175,719</td>
<td align="right">88,589,376</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,419,579</td>
<td align="right">88,833,236</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">128,564,479</td>
<td align="right">125,796,352</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">5,887,814</td>
<td align="right">5,772,685</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">177,290,785</td>
<td align="right">179,661,923</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">10,227,702</td>
<td align="right">10,113,943</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">313,469,522</td>
<td align="right">310,341,346</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">571,319,669</td>
<td align="right">566,294,016</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">342,064,596</td>
<td align="right">339,328,615</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">30,001,817</td>
<td align="right">30,202,054</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,013,405,311</td>
<td align="right">1,006,671,716</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,345,606,072</td>
<td align="right">1,337,157,545</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">541,226,710</td>
<td align="right">538,531,595</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">485,260,685</td>
<td align="right">483,216,648</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">760,038,110</td>
<td align="right">756,847,726</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">714,557,955</td>
<td align="right">711,896,854</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,666,887,461</td>
<td align="right">1,661,684,113</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">231,824,033</td>
<td align="right">232,540,792</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,728,603,850</td>
<td align="right">1,723,274,157</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">114,900,367</td>
<td align="right">114,548,446</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">1,974,304,904</td>
<td align="right">1,968,615,910</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,859,427,717</td>
<td align="right">1,854,090,644</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">359,699,499</td>
<td align="right">360,731,023</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">11,387,023</td>
<td align="right">11,354,522</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">11,387,023</td>
<td align="right">11,354,522</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,918,988,098</td>
<td align="right">1,913,651,461</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,048,332,263</td>
<td align="right">1,045,457,523</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">948,373,217</td>
<td align="right">945,852,347</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">399,744,059</td>
<td align="right">400,775,583</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">179,381,897</td>
<td align="right">178,979,840</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">145,245,020</td>
<td align="right">144,927,940</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">2,941,080,216</td>
<td align="right">2,935,409,014</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">4,561,711,868</td>
<td align="right">4,554,214,855</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">173,128,969</td>
<td align="right">172,887,225</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,464,290,065</td>
<td align="right">6,456,018,781</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">24,819,618</td>
<td align="right">24,787,930</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">13,838,456,947</td>
<td align="right">13,821,742,247</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">1,875,356,288</td>
<td align="right">1,873,136,556</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,093,383,695</td>
<td align="right">7,085,168,147</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,234,590,317</td>
<td align="right">2,232,003,480</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,257,356,977</td>
<td align="right">2,254,770,160</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">4,922,821,839</td>
<td align="right">4,917,294,130</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,406,868</td>
<td align="right">78,323,187</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">133,642,686</td>
<td align="right">133,784,722</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">185,072,867</td>
<td align="right">185,259,803</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">16,538,760</td>
<td align="right">16,522,078</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">187,592,305</td>
<td align="right">187,779,344</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">1,370,961,742</td>
<td align="right">1,369,638,038</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">88,982,129</td>
<td align="right">88,898,327</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,202,454,485</td>
<td align="right">3,199,485,671</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">11,784,165,342</td>
<td align="right">11,773,459,189</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">93,430,534</td>
<td align="right">93,346,973</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">93,535,123</td>
<td align="right">93,451,564</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,455,074,511</td>
<td align="right">3,452,114,256</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,310,397,169</td>
<td align="right">1,309,359,907</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">111,820,973</td>
<td align="right">111,900,848</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,984,025</td>
<td align="right">315,183,908</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,311,844,392</td>
<td align="right">1,311,047,214</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">618,223,222</td>
<td align="right">617,864,831</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,099,781,662</td>
<td align="right">1,099,181,768</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">217,966,922</td>
<td align="right">217,853,238</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">410,581,294</td>
<td align="right">410,400,066</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">592,652,860</td>
<td align="right">592,391,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,531,425</td>
<td align="right">779,193,077</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,068,745</td>
<td align="right">779,730,397</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,618,789</td>
<td align="right">133,562,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">133,618,789</td>
<td align="right">133,562,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_POP_FRAME</td>
<td align="right">875,460,654</td>
<td align="right">875,820,345</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,338,922,475</td>
<td align="right">1,338,415,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,561,966</td>
<td align="right">45,577,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">243,907,204</td>
<td align="right">243,990,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">565,771,067</td>
<td align="right">565,591,300</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">551,164,867</td>
<td align="right">550,991,940</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">733,468,302</td>
<td align="right">733,244,183</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">112,325,182</td>
<td align="right">112,292,856</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,114,256,154</td>
<td align="right">1,113,944,729</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,092,997,216</td>
<td align="right">2,092,448,252</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,274,720,182</td>
<td align="right">1,275,034,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">109,958,792</td>
<td align="right">109,984,014</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COLD_EXIT</td>
<td align="right">2,074,566,951</td>
<td align="right">2,074,124,992</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">2,182,099,494</td>
<td align="right">2,182,547,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">687,093,097</td>
<td align="right">687,228,782</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">4,710,003,807</td>
<td align="right">4,709,099,014</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">1,870,767,919</td>
<td align="right">1,871,114,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">2,819,883,954</td>
<td align="right">2,819,418,503</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">161,372,830</td>
<td align="right">161,347,288</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,388,373,310</td>
<td align="right">1,388,155,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">9,554,996,180</td>
<td align="right">9,553,576,443</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,231,660,017</td>
<td align="right">1,231,490,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">930,269,724</td>
<td align="right">930,158,556</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,146,500,679</td>
<td align="right">1,146,370,304</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">782,668,763</td>
<td align="right">782,581,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,246,589,319</td>
<td align="right">1,246,458,944</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,265,394,739</td>
<td align="right">1,265,264,384</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">6,486,971,958</td>
<td align="right">6,486,317,018</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,511,397,113</td>
<td align="right">1,511,249,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,183,648,599</td>
<td align="right">2,183,437,459</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">2,226,501,535</td>
<td align="right">2,226,287,817</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">444,981</td>
<td align="right">444,945</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">199,859,536</td>
<td align="right">199,874,683</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">229,758,264</td>
<td align="right">229,775,412</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">822,923,189</td>
<td align="right">822,869,255</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">139,955,972</td>
<td align="right">139,946,845</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,603,588,120</td>
<td align="right">3,603,374,478</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,636,040</td>
<td align="right">5,635,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">130,846,000</td>
<td align="right">130,838,694</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,974,852,365</td>
<td align="right">1,974,960,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">330,384,671</td>
<td align="right">330,366,879</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">3,292,448,854</td>
<td align="right">3,292,281,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">2,536,065,745</td>
<td align="right">2,535,937,830</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">4,437,289</td>
<td align="right">4,437,512</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">723,870,260</td>
<td align="right">723,904,347</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">325,053,641</td>
<td align="right">325,066,229</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">686,425,949</td>
<td align="right">686,450,599</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,727,363,699</td>
<td align="right">5,727,541,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,318,454</td>
<td align="right">32,319,330</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">226,295,900</td>
<td align="right">226,301,369</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">224,037,231</td>
<td align="right">224,041,743</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">909,705,915</td>
<td align="right">909,692,441</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,144,563,300</td>
<td align="right">1,144,549,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,335,163,792</td>
<td align="right">1,335,150,373</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">126,327,183</td>
<td align="right">126,326,028</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,043,488,069</td>
<td align="right">1,043,496,865</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">93,665,920</td>
<td align="right">93,665,280</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">966,585,399</td>
<td align="right">966,579,758</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">4,866,988</td>
<td align="right">4,866,961</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">647,423</td>
<td align="right">647,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">203,320,351</td>
<td align="right">203,319,422</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">280,522,350</td>
<td align="right">280,523,390</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">154,174,580</td>
<td align="right">154,174,043</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">264,462,419</td>
<td align="right">264,463,277</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">375,826,920</td>
<td align="right">375,828,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">59,835,132</td>
<td align="right">59,835,302</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">227,833,642</td>
<td align="right">227,834,087</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">263,235,599</td>
<td align="right">263,236,017</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,908,140</td>
<td align="right">9,908,154</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">199,031,000</td>
<td align="right">199,030,720</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">423,187,728</td>
<td align="right">423,188,303</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">55,151,915</td>
<td align="right">55,151,982</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,197,988</td>
<td align="right">97,198,104</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">98,155,328</td>
<td align="right">98,155,444</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">2,645,331,548</td>
<td align="right">2,645,334,569</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">22,284,220</td>
<td align="right">22,284,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">108,946,835</td>
<td align="right">108,946,902</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,367,059,285</td>
<td align="right">1,367,058,505</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">54,261,020</td>
<td align="right">54,261,044</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">958,950,647</td>
<td align="right">958,951,003</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,041,464,948</td>
<td align="right">1,041,465,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">35,070,081</td>
<td align="right">35,070,093</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">484,893,975</td>
<td align="right">484,894,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">101,199,243</td>
<td align="right">101,199,266</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">101,193,573</td>
<td align="right">101,193,595</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,818,524,166</td>
<td align="right">1,818,524,521</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">22,021,960</td>
<td align="right">22,021,964</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,911,721</td>
<td align="right">68,911,733</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">409,917,647</td>
<td align="right">409,917,694</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">384,637,975</td>
<td align="right">384,637,941</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">147,640,961</td>
<td align="right">147,640,970</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">645,068,463</td>
<td align="right">645,068,486</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">118,547,645</td>
<td align="right">118,547,646</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,652,506,973</td>
<td align="right">1,652,506,976</td>
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
<td align="left">_GUARD_TOS_INT</td>
<td align="right">213,613,460</td>
<td align="right">213,613,460</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">187,548,560</td>
<td align="right">187,548,560</td>
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
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">99,814,560</td>
<td align="right">99,814,560</td>
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
<td align="right">63,424,040</td>
<td align="right">63,424,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">61,837,320</td>
<td align="right">61,837,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">53,794,920</td>
<td align="right">53,794,920</td>
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
<td align="right">12,693,140</td>
<td align="right">12,693,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,133,940</td>
<td align="right">8,133,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_CONST_KEY_MAP</td>
<td align="right">6,583,580</td>
<td align="right">6,583,580</td>
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
<td align="right">543,340</td>
<td align="right">543,340</td>
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
<td align="left">BEFORE_WITH</td>
<td align="right">1,465</td>
<td align="right">1,422</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,202</td>
<td align="right">5,225</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">6,575</td>
<td align="right">6,551</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">539</td>
<td align="right">540</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">40,462</td>
<td align="right">40,526</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">28,920</td>
<td align="right">28,960</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">82,212</td>
<td align="right">82,292</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">2,341</td>
<td align="right">2,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">2,417</td>
<td align="right">2,416</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">32,220</td>
<td align="right">32,220</td>
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
<td align="right">1,084</td>
<td align="right">1,080</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,084</td>
<td align="right">1,080</td>
<td align="right">-0.4%</td>
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
Stats gathered on: 2024-05-29
