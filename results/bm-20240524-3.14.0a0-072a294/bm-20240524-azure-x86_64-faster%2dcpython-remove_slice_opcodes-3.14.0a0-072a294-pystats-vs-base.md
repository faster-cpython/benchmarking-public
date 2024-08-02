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
<td align="left">BUILD_SLICE</td>
<td align="right">211,756,552</td>
<td align="right">591,639,333</td>
<td align="right">179.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">448,578,598</td>
<td align="right">611,046,968</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,623,101,865</td>
<td align="right">1,959,302,637</td>
<td align="right">20.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">15,013,287</td>
<td align="right">14,288,129</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">BEFORE_WITH</td>
<td align="right">6,968,951</td>
<td align="right">6,689,317</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">12,280,091</td>
<td align="right">11,859,935</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">699,755,305</td>
<td align="right">684,364,988</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,823,442</td>
<td align="right">1,789,035</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">10,856,385</td>
<td align="right">10,720,175</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">507,140</td>
<td align="right">502,340</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">81,847,028</td>
<td align="right">81,119,977</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">14,740,071,528</td>
<td align="right">14,614,561,897</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">195,351,484</td>
<td align="right">196,944,969</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">337,983,486</td>
<td align="right">335,703,690</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">65,823,723</td>
<td align="right">65,408,581</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">212,856,640</td>
<td align="right">212,126,377</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">189,463,216</td>
<td align="right">188,836,770</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">819,019,213</td>
<td align="right">816,954,952</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">399,346,610</td>
<td align="right">398,359,449</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">86,716,753</td>
<td align="right">86,514,706</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,388,001,726</td>
<td align="right">1,384,957,135</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">147,280</td>
<td align="right">146,960</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">389,802,016</td>
<td align="right">389,018,626</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">701,239,516</td>
<td align="right">699,851,020</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">626,404,295</td>
<td align="right">625,227,302</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">18,057,861</td>
<td align="right">18,024,921</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">288,529,507</td>
<td align="right">288,004,252</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">1,890,850,289</td>
<td align="right">1,887,476,652</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">119,358,428</td>
<td align="right">119,151,601</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">233,232,425</td>
<td align="right">232,863,475</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">232,768,521</td>
<td align="right">232,416,055</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,926,895,297</td>
<td align="right">1,924,020,542</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,285,134,003</td>
<td align="right">2,281,951,800</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">76,969,190</td>
<td align="right">76,864,673</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">155,840,274</td>
<td align="right">155,628,685</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,811,323,120</td>
<td align="right">2,807,516,581</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">212,945,278</td>
<td align="right">212,682,580</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">4,132,153,465</td>
<td align="right">4,127,183,272</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">427,228,128</td>
<td align="right">426,714,394</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,167,270,378</td>
<td align="right">2,164,706,136</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">196,390,383</td>
<td align="right">196,170,869</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">4,143,237,182</td>
<td align="right">4,138,773,070</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,783,253,110</td>
<td align="right">1,781,333,720</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">116,585,578</td>
<td align="right">116,709,885</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">515,582,243</td>
<td align="right">515,035,250</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,821,830,176</td>
<td align="right">4,816,762,010</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">4,794,789,500</td>
<td align="right">4,789,788,461</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">7,830,826,399</td>
<td align="right">7,822,726,648</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">577,090,341</td>
<td align="right">576,612,015</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">7,044,369,214</td>
<td align="right">7,038,691,311</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">434,309,433</td>
<td align="right">433,961,271</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">839,224,017</td>
<td align="right">838,567,185</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">1,779,442,722</td>
<td align="right">1,778,092,174</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">1,542,682,863</td>
<td align="right">1,541,540,624</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,022,283,607</td>
<td align="right">1,021,526,777</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">649,366,964</td>
<td align="right">649,844,298</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">664,678,563</td>
<td align="right">664,239,906</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,151,982,992</td>
<td align="right">2,150,571,950</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,242,374</td>
<td align="right">21,228,633</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,242,514</td>
<td align="right">21,228,773</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,771,443</td>
<td align="right">20,758,013</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">558,192,883</td>
<td align="right">557,834,320</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">43,639,869,198</td>
<td align="right">43,612,225,456</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">354,411,689</td>
<td align="right">354,211,126</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,975,262,815</td>
<td align="right">1,974,198,250</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,323,538,228</td>
<td align="right">1,322,838,328</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">998,267,665</td>
<td align="right">997,751,878</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">795,335,343</td>
<td align="right">795,742,477</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,188,296,180</td>
<td align="right">2,187,176,603</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">229,111,572</td>
<td align="right">228,995,698</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">478,653,795</td>
<td align="right">478,413,227</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,562,336,373</td>
<td align="right">5,559,565,984</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,181,493,258</td>
<td align="right">1,180,935,564</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">410,236,682</td>
<td align="right">410,050,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">13,149,187,053</td>
<td align="right">13,143,274,810</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,440,108,854</td>
<td align="right">11,435,193,275</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">14,679,005,817</td>
<td align="right">14,672,863,868</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">942,548,083</td>
<td align="right">942,176,601</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">5,228,701,695</td>
<td align="right">5,226,689,700</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">832,060,801</td>
<td align="right">831,753,480</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,241,670</td>
<td align="right">9,238,309</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,665,533</td>
<td align="right">9,662,134</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">1,590,902,558</td>
<td align="right">1,590,373,034</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">944,768,001</td>
<td align="right">944,461,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">692,583</td>
<td align="right">692,799</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">131,628,083</td>
<td align="right">131,588,284</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">4,917,183,824</td>
<td align="right">4,915,716,479</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,270,300</td>
<td align="right">3,269,340</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">369,169,095</td>
<td align="right">369,063,902</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">481,699,663</td>
<td align="right">481,563,106</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">346,404,575</td>
<td align="right">346,502,351</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">506,524,374</td>
<td align="right">506,665,807</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">16,189</td>
<td align="right">16,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">469,736,293</td>
<td align="right">469,847,241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,219,739,546</td>
<td align="right">2,219,219,243</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">253,883,602</td>
<td align="right">253,824,636</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">457,469,496</td>
<td align="right">457,365,984</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">283,991,006</td>
<td align="right">283,935,730</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">127,699,683</td>
<td align="right">127,674,847</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">152,403,244</td>
<td align="right">152,376,199</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">665,641,195</td>
<td align="right">665,536,924</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">1,497,431,975</td>
<td align="right">1,497,212,019</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">843,329,189</td>
<td align="right">843,211,948</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">1,182,020</td>
<td align="right">1,181,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">544,386,753</td>
<td align="right">544,320,828</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,123,940</td>
<td align="right">8,122,980</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,395,862,700</td>
<td align="right">1,395,702,821</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,797,396</td>
<td align="right">1,797,550</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">68,775,135</td>
<td align="right">68,769,724</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">2,466,900,798</td>
<td align="right">2,466,725,220</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">14,132,640</td>
<td align="right">14,131,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">499,550,048</td>
<td align="right">499,525,048</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">88,174,187</td>
<td align="right">88,169,907</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">177,009,389</td>
<td align="right">177,000,964</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">94,738,076</td>
<td align="right">94,733,590</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">1,874,264</td>
<td align="right">1,874,182</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,974,958</td>
<td align="right">5,974,710</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">74,755,081</td>
<td align="right">74,752,201</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">92,198,320</td>
<td align="right">92,195,120</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,480,840</td>
<td align="right">94,477,640</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">148,346,322</td>
<td align="right">148,341,522</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,285,461,718</td>
<td align="right">1,285,425,117</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">139,685,160</td>
<td align="right">139,681,320</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">43,289,892</td>
<td align="right">43,290,968</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">555,914,965</td>
<td align="right">555,901,945</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">1,258,812,794</td>
<td align="right">1,258,784,234</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">274,353,550</td>
<td align="right">274,359,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">660,657,254</td>
<td align="right">660,643,445</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">589,479,027</td>
<td align="right">589,490,421</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">119,292,989</td>
<td align="right">119,290,688</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">176,569,834</td>
<td align="right">176,566,638</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">93,947,660</td>
<td align="right">93,946,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">2,335,039,369</td>
<td align="right">2,335,008,036</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,382,308,229</td>
<td align="right">1,382,292,875</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">99,239,927</td>
<td align="right">99,240,984</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_CONST_KEY_MAP</td>
<td align="right">12,200,147</td>
<td align="right">12,200,031</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,368,124</td>
<td align="right">20,367,934</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,674,382,420</td>
<td align="right">1,674,367,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,193,233,462</td>
<td align="right">3,193,204,221</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">360,262,025</td>
<td align="right">360,258,770</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,217,151</td>
<td align="right">82,216,535</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">844,003,440</td>
<td align="right">843,997,797</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">189,307,263</td>
<td align="right">189,306,001</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">110,852,301</td>
<td align="right">110,851,661</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">279,425,571</td>
<td align="right">279,425,061</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">47,436,244</td>
<td align="right">47,436,164</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">243,756,258</td>
<td align="right">243,756,625</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">249,500,459</td>
<td align="right">249,500,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">208,280,690</td>
<td align="right">208,280,831</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">357,627,339</td>
<td align="right">357,627,181</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">80,934,735</td>
<td align="right">80,934,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">437,672,631</td>
<td align="right">437,672,677</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">233,344,707</td>
<td align="right">233,344,687</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">786,225,739</td>
<td align="right">786,225,674</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">229,269,605</td>
<td align="right">229,269,614</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,318,810</td>
<td align="right">173,318,816</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,933,563,089</td>
<td align="right">1,933,563,137</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,026,545</td>
<td align="right">402,026,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">337,750,191</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">162,427,160</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">133,515,680</td>
<td align="right">133,515,680</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">97,525,061</td>
<td align="right">97,525,061</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">64,954,160</td>
<td align="right">64,954,160</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">8,204,680</td>
<td align="right">8,204,680</td>
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
<td align="left">BEFORE_ASYNC_WITH</td>
<td align="right">2,995,200</td>
<td align="right">2,995,200</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">1,041,440</td>
<td align="right">1,041,440</td>
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
<td align="right">94,200</td>
<td align="right">94,200</td>
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
<td align="right">83,960</td>
<td align="right">83,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">28,760</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,180</td>
<td align="right">27,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,260</td>
<td align="right">2,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">1,040</td>
<td align="right">1,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">980</td>
<td align="right">980</td>
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
<td align="right">1,435,654,982</td>
<td align="right">17.1%</td>
<td align="right">1,432,611,279</td>
<td align="right">17.1%</td>
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
<td align="right">6,951,340,210</td>
<td align="right">82.9%</td>
<td align="right">6,950,968,193</td>
<td align="right">82.9%</td>
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
<td align="right">50,340,300</td>
<td align="right">0.6%</td>
<td align="right">50,340,300</td>
<td align="right">0.6%</td>
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
<td align="right">1,695,222</td>
<td align="right">63.1%</td>
<td align="right">1,694,394</td>
<td align="right">63.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">991,822</td>
<td align="right">36.9%</td>
<td align="right">991,762</td>
<td align="right">36.9%</td>
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
<td align="right">16,324</td>
<td align="right">1.0%</td>
<td align="right">16,047</td>
<td align="right">0.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">69,170</td>
<td align="right">4.1%</td>
<td align="right">68,728</td>
<td align="right">4.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,893</td>
<td align="right">0.1%</td>
<td align="right">1,899</td>
<td align="right">0.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">66,733</td>
<td align="right">3.9%</td>
<td align="right">66,677</td>
<td align="right">3.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">13,515</td>
<td align="right">0.8%</td>
<td align="right">13,508</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">66,615</td>
<td align="right">3.9%</td>
<td align="right">66,598</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">28,773</td>
<td align="right">1.7%</td>
<td align="right">28,766</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">216,763</td>
<td align="right">12.8%</td>
<td align="right">216,735</td>
<td align="right">12.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">36,950</td>
<td align="right">2.2%</td>
<td align="right">36,947</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">52,680</td>
<td align="right">3.1%</td>
<td align="right">52,676</td>
<td align="right">3.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">17,765</td>
<td align="right">1.0%</td>
<td align="right">17,764</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">29,445</td>
<td align="right">1.7%</td>
<td align="right">29,444</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">29,505</td>
<td align="right">1.7%</td>
<td align="right">29,504</td>
<td align="right">1.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">777,944</td>
<td align="right">45.9%</td>
<td align="right">777,954</td>
<td align="right">45.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">247,187</td>
<td align="right">14.6%</td>
<td align="right">247,187</td>
<td align="right">14.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">15,260</td>
<td align="right">0.9%</td>
<td align="right">15,260</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">5,500</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,760</td>
<td align="right">0.2%</td>
<td align="right">2,760</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">440</td>
<td align="right">0.0%</td>
<td align="right">440</td>
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
<td align="right">1,627,492,339</td>
<td align="right">26.3%</td>
<td align="right">1,963,560,355</td>
<td align="right">30.1%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,045,311</td>
<td align="right">0.1%</td>
<td align="right">5,050,771</td>
<td align="right">0.1%</td>
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
<td align="right">4,566,386,033</td>
<td align="right">73.7%</td>
<td align="right">4,567,729,844</td>
<td align="right">69.9%</td>
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
<td align="right">468,428</td>
<td align="right">71.5%</td>
<td align="right">605,652</td>
<td align="right">76.4%</td>
<td align="right">29.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">186,409</td>
<td align="right">28.5%</td>
<td align="right">187,401</td>
<td align="right">23.6%</td>
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
<td align="left">string slice</td>
<td align="right">100</td>
<td align="right">0.0%</td>
<td align="right">47,140</td>
<td align="right">7.8%</td>
<td align="right">47,040.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">125</td>
<td align="right">0.0%</td>
<td align="right">20,449</td>
<td align="right">3.4%</td>
<td align="right">16,259.2%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">980</td>
<td align="right">0.2%</td>
<td align="right">13,440</td>
<td align="right">2.2%</td>
<td align="right">1,271.4%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">35,080</td>
<td align="right">7.5%</td>
<td align="right">83,760</td>
<td align="right">13.8%</td>
<td align="right">138.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">117,703</td>
<td align="right">25.1%</td>
<td align="right">126,440</td>
<td align="right">20.9%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">57,380</td>
<td align="right">12.2%</td>
<td align="right">57,343</td>
<td align="right">9.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">157,600</td>
<td align="right">33.6%</td>
<td align="right">157,600</td>
<td align="right">26.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">74,080</td>
<td align="right">15.8%</td>
<td align="right">74,080</td>
<td align="right">12.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">19,760</td>
<td align="right">4.2%</td>
<td align="right">19,760</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">5,620</td>
<td align="right">1.2%</td>
<td align="right">5,620</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">11,542,987,295</td>
<td align="right">97.0%</td>
<td align="right">11,535,030,700</td>
<td align="right">97.0%</td>
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
<td align="right">240,534,371</td>
<td align="right">2.0%</td>
<td align="right">240,481,393</td>
<td align="right">2.0%</td>
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
<td align="right">351,965,450</td>
<td align="right">3.0%</td>
<td align="right">352,038,157</td>
<td align="right">3.0%</td>
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
<td align="right">41,300</td>
<td align="right">0.0%</td>
<td align="right">41,300</td>
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
<td align="right">78,634</td>
<td align="right">1.5%</td>
<td align="right">78,380</td>
<td align="right">1.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">5,075,865</td>
<td align="right">98.5%</td>
<td align="right">5,074,741</td>
<td align="right">98.5%</td>
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
<td align="right">9,580</td>
<td align="right">12.2%</td>
<td align="right">9,540</td>
<td align="right">12.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class no vectorcall</td>
<td align="right">68,574</td>
<td align="right">87.2%</td>
<td align="right">68,360</td>
<td align="right">87.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3,000</td>
<td align="right">3.8%</td>
<td align="right">3,000</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">1,960</td>
<td align="right">2.5%</td>
<td align="right">1,960</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">700</td>
<td align="right">0.9%</td>
<td align="right">700</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">480</td>
<td align="right">0.6%</td>
<td align="right">480</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,376,411</td>
<td align="right">0.0%</td>
<td align="right">1,374,593</td>
<td align="right">0.0%</td>
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
<td align="right">214,044,131</td>
<td align="right">4.2%</td>
<td align="right">213,779,839</td>
<td align="right">4.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,903,321,026</td>
<td align="right">95.8%</td>
<td align="right">4,902,027,905</td>
<td align="right">95.8%</td>
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
<td align="right">193,909</td>
<td align="right">69.9%</td>
<td align="right">193,740</td>
<td align="right">69.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">83,649</td>
<td align="right">30.1%</td>
<td align="right">83,594</td>
<td align="right">30.1%</td>
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
<td align="left">tuple</td>
<td align="right">12,746</td>
<td align="right">6.6%</td>
<td align="right">12,716</td>
<td align="right">6.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">19,101</td>
<td align="right">9.9%</td>
<td align="right">19,060</td>
<td align="right">9.8%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">52,011</td>
<td align="right">26.8%</td>
<td align="right">51,934</td>
<td align="right">26.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">3,451</td>
<td align="right">1.8%</td>
<td align="right">3,456</td>
<td align="right">1.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">34,571</td>
<td align="right">17.8%</td>
<td align="right">34,521</td>
<td align="right">17.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">19,729</td>
<td align="right">10.2%</td>
<td align="right">19,753</td>
<td align="right">10.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27,500</td>
<td align="right">14.2%</td>
<td align="right">27,500</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,880</td>
<td align="right">5.6%</td>
<td align="right">10,880</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">9,880</td>
<td align="right">5.1%</td>
<td align="right">9,880</td>
<td align="right">5.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,260</td>
<td align="right">1.2%</td>
<td align="right">2,260</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">1,200</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">580</td>
<td align="right">0.3%</td>
<td align="right">580</td>
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
<td align="right">348,733,876</td>
<td align="right">12.5%</td>
<td align="right">348,831,635</td>
<td align="right">12.5%</td>
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
<td align="right">2,446,599,092</td>
<td align="right">87.5%</td>
<td align="right">2,446,052,147</td>
<td align="right">87.5%</td>
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
<td align="right">2,546,240</td>
<td align="right">0.1%</td>
<td align="right">2,546,240</td>
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
<td align="right">155,599</td>
<td align="right">71.7%</td>
<td align="right">155,618</td>
<td align="right">71.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,340</td>
<td align="right">28.3%</td>
<td align="right">61,338</td>
<td align="right">28.3%</td>
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
<td align="right">21,966</td>
<td align="right">14.1%</td>
<td align="right">21,983</td>
<td align="right">14.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">31,293</td>
<td align="right">20.1%</td>
<td align="right">31,295</td>
<td align="right">20.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">74,460</td>
<td align="right">47.9%</td>
<td align="right">74,460</td>
<td align="right">47.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">27,880</td>
<td align="right">17.9%</td>
<td align="right">27,880</td>
<td align="right">17.9%</td>
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
<td align="right">3,324,159,848</td>
<td align="right">83.0%</td>
<td align="right">3,322,074,684</td>
<td align="right">83.0%</td>
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
<td align="right">676,206,264</td>
<td align="right">16.9%</td>
<td align="right">676,333,652</td>
<td align="right">16.9%</td>
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
<td align="right">173,289,548</td>
<td align="right">4.3%</td>
<td align="right">173,272,869</td>
<td align="right">4.3%</td>
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
<td align="right">289,047</td>
<td align="right">8.0%</td>
<td align="right">286,737</td>
<td align="right">8.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,318,611</td>
<td align="right">92.0%</td>
<td align="right">3,318,287</td>
<td align="right">92.0%</td>
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
<td align="left">callable</td>
<td align="right">260</td>
<td align="right">0.1%</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">107,991</td>
<td align="right">37.4%</td>
<td align="right">105,702</td>
<td align="right">36.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">9,760</td>
<td align="right">3.4%</td>
<td align="right">9,740</td>
<td align="right">3.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">28,106</td>
<td align="right">9.7%</td>
<td align="right">28,162</td>
<td align="right">9.8%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">21,980</td>
<td align="right">7.6%</td>
<td align="right">21,960</td>
<td align="right">7.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">41,830</td>
<td align="right">14.5%</td>
<td align="right">41,813</td>
<td align="right">14.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">30,100</td>
<td align="right">10.4%</td>
<td align="right">30,100</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">14,020</td>
<td align="right">4.9%</td>
<td align="right">14,020</td>
<td align="right">4.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">12,240</td>
<td align="right">4.2%</td>
<td align="right">12,240</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">8,020</td>
<td align="right">2.8%</td>
<td align="right">8,020</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">5,980</td>
<td align="right">2.1%</td>
<td align="right">5,980</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">5,800</td>
<td align="right">2.0%</td>
<td align="right">5,800</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">2,280</td>
<td align="right">0.8%</td>
<td align="right">2,280</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">660</td>
<td align="right">0.2%</td>
<td align="right">660</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">2,829,229,761</td>
<td align="right">15.5%</td>
<td align="right">2,825,863,201</td>
<td align="right">15.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,356,650,546</td>
<td align="right">84.3%</td>
<td align="right">15,343,188,090</td>
<td align="right">84.3%</td>
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
<td align="right">959,572,443</td>
<td align="right">5.3%</td>
<td align="right">959,577,799</td>
<td align="right">5.3%</td>
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
<td align="right">324,280</td>
<td align="right">0.0%</td>
<td align="right">324,280</td>
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
<td align="right">2,462,744</td>
<td align="right">11.6%</td>
<td align="right">2,460,959</td>
<td align="right">11.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,730,227</td>
<td align="right">88.4%</td>
<td align="right">18,730,291</td>
<td align="right">88.4%</td>
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
<td align="right">6,156</td>
<td align="right">0.2%</td>
<td align="right">5,976</td>
<td align="right">0.2%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">20,420</td>
<td align="right">0.8%</td>
<td align="right">20,340</td>
<td align="right">0.8%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">28,720</td>
<td align="right">1.2%</td>
<td align="right">28,620</td>
<td align="right">1.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">12,460</td>
<td align="right">0.5%</td>
<td align="right">12,420</td>
<td align="right">0.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">114,972</td>
<td align="right">4.7%</td>
<td align="right">114,618</td>
<td align="right">4.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">144,877</td>
<td align="right">5.9%</td>
<td align="right">144,569</td>
<td align="right">5.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">22,260</td>
<td align="right">0.9%</td>
<td align="right">22,240</td>
<td align="right">0.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">19,668</td>
<td align="right">0.8%</td>
<td align="right">19,658</td>
<td align="right">0.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">997,030</td>
<td align="right">40.5%</td>
<td align="right">996,588</td>
<td align="right">40.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">716,051</td>
<td align="right">29.1%</td>
<td align="right">715,823</td>
<td align="right">29.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">81,369</td>
<td align="right">3.3%</td>
<td align="right">81,359</td>
<td align="right">3.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">264,581</td>
<td align="right">10.7%</td>
<td align="right">264,568</td>
<td align="right">10.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">16,620</td>
<td align="right">0.7%</td>
<td align="right">16,620</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">11,980</td>
<td align="right">0.5%</td>
<td align="right">11,980</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">3,420</td>
<td align="right">0.1%</td>
<td align="right">3,420</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
<td align="right">1,100</td>
<td align="right">0.0%</td>
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
<td align="right">472,703</td>
<td align="right">0.0%</td>
<td align="right">468,073</td>
<td align="right">0.0%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,356,653,170</td>
<td align="right">99.8%</td>
<td align="right">10,348,886,372</td>
<td align="right">99.8%</td>
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
<td align="right">20,364,252</td>
<td align="right">0.2%</td>
<td align="right">20,359,605</td>
<td align="right">0.2%</td>
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
<td align="right">12,360</td>
<td align="right">0.0%</td>
<td align="right">12,360</td>
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
<td align="right">476,575</td>
<td align="right">100.0%</td>
<td align="right">476,402</td>
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
<td align="right">83,670,470</td>
<td align="right">100.0%</td>
<td align="right">82,909,012</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">8,229</td>
<td align="right">0.0%</td>
<td align="right">8,225</td>
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
<td align="right">7,960</td>
<td align="right">100.0%</td>
<td align="right">7,960</td>
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
<td align="right">786,195,079</td>
<td align="right">81.9%</td>
<td align="right">786,195,014</td>
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
<td align="right">173,284,370</td>
<td align="right">18.1%</td>
<td align="right">173,284,376</td>
<td align="right">18.1%</td>
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
<td align="right">5,480</td>
<td align="right">8.4%</td>
<td align="right">5,480</td>
<td align="right">8.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
<td align="right">59,620</td>
<td align="right">91.6%</td>
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
<td align="right">9,980</td>
<td align="right">16.7%</td>
<td align="right">9,980</td>
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
<td align="right">2,742,367,012</td>
<td align="right">92.6%</td>
<td align="right">2,741,192,942</td>
<td align="right">92.6%</td>
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
<td align="right">216,456,476</td>
<td align="right">7.3%</td>
<td align="right">216,446,537</td>
<td align="right">7.3%</td>
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
<td align="right">150,731,729</td>
<td align="right">5.1%</td>
<td align="right">150,726,959</td>
<td align="right">5.1%</td>
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
<td align="right">106,390</td>
<td align="right">3.5%</td>
<td align="right">106,228</td>
<td align="right">3.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,943,998</td>
<td align="right">96.5%</td>
<td align="right">2,943,918</td>
<td align="right">96.5%</td>
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
<td align="right">3,680</td>
<td align="right">3.5%</td>
<td align="right">3,580</td>
<td align="right">3.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,060</td>
<td align="right">4.8%</td>
<td align="right">5,040</td>
<td align="right">4.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">34,800</td>
<td align="right">32.7%</td>
<td align="right">34,760</td>
<td align="right">32.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">16,730</td>
<td align="right">15.7%</td>
<td align="right">16,728</td>
<td align="right">15.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,720</td>
<td align="right">13.8%</td>
<td align="right">14,720</td>
<td align="right">13.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">10,700</td>
<td align="right">10.1%</td>
<td align="right">10,700</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,900</td>
<td align="right">7.4%</td>
<td align="right">7,900</td>
<td align="right">7.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,780</td>
<td align="right">6.4%</td>
<td align="right">6,780</td>
<td align="right">6.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,060</td>
<td align="right">4.8%</td>
<td align="right">5,060</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">840</td>
<td align="right">0.8%</td>
<td align="right">840</td>
<td align="right">0.8%</td>
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
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
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
<td align="right">448,409,490</td>
<td align="right">33.8%</td>
<td align="right">610,834,868</td>
<td align="right">41.0%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">878,005,634</td>
<td align="right">66.2%</td>
<td align="right">877,491,773</td>
<td align="right">58.9%</td>
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
<td align="right">158,740</td>
<td align="right">92.3%</td>
<td align="right">201,740</td>
<td align="right">93.8%</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,268</td>
<td align="right">7.7%</td>
<td align="right">13,260</td>
<td align="right">6.2%</td>
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
<td align="left">py simple</td>
<td align="right">43,960</td>
<td align="right">27.7%</td>
<td align="right">44,860</td>
<td align="right">22.2%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,360</td>
<td align="right">0.9%</td>
<td align="right">1,380</td>
<td align="right">0.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">66,240</td>
<td align="right">41.7%</td>
<td align="right">66,240</td>
<td align="right">32.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">34,300</td>
<td align="right">21.6%</td>
<td align="right">34,300</td>
<td align="right">17.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">9,640</td>
<td align="right">6.1%</td>
<td align="right">9,640</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">3,240</td>
<td align="right">2.0%</td>
<td align="right">3,240</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">41,920</td>
<td align="right">20.8%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">160</td>
<td align="right">0.1%</td>
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
<td align="right">6,405,572,758</td>
<td align="right">92.1%</td>
<td align="right">6,401,055,010</td>
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
<td align="right">548,582,885</td>
<td align="right">7.9%</td>
<td align="right">548,397,337</td>
<td align="right">7.9%</td>
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
<td align="right">141,882,519</td>
<td align="right">2.0%</td>
<td align="right">141,883,051</td>
<td align="right">2.0%</td>
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
<td align="right">659,875</td>
<td align="right">18.7%</td>
<td align="right">659,667</td>
<td align="right">18.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,876,441</td>
<td align="right">81.3%</td>
<td align="right">2,876,387</td>
<td align="right">81.3%</td>
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
<td align="right">16,560</td>
<td align="right">2.5%</td>
<td align="right">16,523</td>
<td align="right">2.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">97,762</td>
<td align="right">14.8%</td>
<td align="right">97,683</td>
<td align="right">14.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">46,288</td>
<td align="right">7.0%</td>
<td align="right">46,257</td>
<td align="right">7.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">100,454</td>
<td align="right">15.2%</td>
<td align="right">100,406</td>
<td align="right">15.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">174,023</td>
<td align="right">26.4%</td>
<td align="right">174,010</td>
<td align="right">26.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">165,148</td>
<td align="right">25.0%</td>
<td align="right">165,148</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">28,800</td>
<td align="right">4.4%</td>
<td align="right">28,800</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">27,640</td>
<td align="right">4.2%</td>
<td align="right">27,640</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,740</td>
<td align="right">0.3%</td>
<td align="right">1,740</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">1,040</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">420</td>
<td align="right">0.1%</td>
<td align="right">420</td>
<td align="right">0.1%</td>
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
<td align="right">1,570,085,249</td>
<td align="right">99.9%</td>
<td align="right">1,569,712,738</td>
<td align="right">99.9%</td>
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
<td align="right">1,767,927</td>
<td align="right">0.1%</td>
<td align="right">1,768,095</td>
<td align="right">0.1%</td>
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
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
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
<td align="right">2,873</td>
<td align="right">8.5%</td>
<td align="right">2,879</td>
<td align="right">8.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">30,836</td>
<td align="right">91.5%</td>
<td align="right">30,816</td>
<td align="right">91.5%</td>
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
<td align="right">2,233</td>
<td align="right">77.7%</td>
<td align="right">2,239</td>
<td align="right">77.8%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">13.2%</td>
<td align="right">380</td>
<td align="right">13.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">260</td>
<td align="right">9.0%</td>
<td align="right">260</td>
<td align="right">9.0%</td>
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
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">124,318,995,044</td>
<td align="right">53.7%</td>
<td align="right">124,489,792,863</td>
<td align="right">53.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">24,336,040,968</td>
<td align="right">10.5%</td>
<td align="right">24,319,843,957</td>
<td align="right">10.5%</td>
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
<td align="right">80,848,925,571</td>
<td align="right">35.0%</td>
<td align="right">80,798,215,392</td>
<td align="right">34.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,803,713,592</td>
<td align="right">0.8%</td>
<td align="right">1,803,643,537</td>
<td align="right">0.8%</td>
<td align="right">-0.0%</td>
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
<td align="left">STORE_SUBSCR</td>
<td align="right">448,409,490</td>
<td align="right">5.0%</td>
<td align="right">610,834,868</td>
<td align="right">6.5%</td>
<td align="right">36.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">1,627,492,339</td>
<td align="right">18.3%</td>
<td align="right">1,963,560,355</td>
<td align="right">20.9%</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">1,435,654,982</td>
<td align="right">16.1%</td>
<td align="right">1,432,611,279</td>
<td align="right">15.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">214,044,131</td>
<td align="right">2.4%</td>
<td align="right">213,779,839</td>
<td align="right">2.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">2,829,229,761</td>
<td align="right">31.8%</td>
<td align="right">2,825,863,201</td>
<td align="right">30.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">548,582,885</td>
<td align="right">6.2%</td>
<td align="right">548,397,337</td>
<td align="right">5.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">348,733,876</td>
<td align="right">3.9%</td>
<td align="right">348,831,635</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">351,965,450</td>
<td align="right">4.0%</td>
<td align="right">352,038,157</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">676,206,264</td>
<td align="right">7.6%</td>
<td align="right">676,333,652</td>
<td align="right">7.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">216,456,476</td>
<td align="right">2.4%</td>
<td align="right">216,446,537</td>
<td align="right">2.3%</td>
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
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">86,437,049</td>
<td align="right">4.6%</td>
<td align="right">86,425,317</td>
<td align="right">4.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">86,722,439</td>
<td align="right">4.6%</td>
<td align="right">86,717,492</td>
<td align="right">4.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">109,963,281</td>
<td align="right">5.8%</td>
<td align="right">109,968,906</td>
<td align="right">5.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">77,884,217</td>
<td align="right">4.1%</td>
<td align="right">77,883,689</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">77,884,217</td>
<td align="right">4.1%</td>
<td align="right">77,883,689</td>
<td align="right">4.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">66,956,358</td>
<td align="right">3.6%</td>
<td align="right">66,956,783</td>
<td align="right">3.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">377,640,184</td>
<td align="right">20.1%</td>
<td align="right">377,638,544</td>
<td align="right">20.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">115,672,935</td>
<td align="right">6.1%</td>
<td align="right">115,673,236</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">348,606,413</td>
<td align="right">18.5%</td>
<td align="right">348,606,437</td>
<td align="right">18.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">120,139,760</td>
<td align="right">6.4%</td>
<td align="right">120,139,760</td>
<td align="right">6.4%</td>
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
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">409,173,521</td>
<td align="right">4.8%</td>
<td align="right">407,549,933</td>
<td align="right">4.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,426,455,388</td>
<td align="right">16.6%</td>
<td align="right">1,423,081,992</td>
<td align="right">16.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,431,781,628</td>
<td align="right">16.6%</td>
<td align="right">1,428,408,232</td>
<td align="right">16.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,288,588,415</td>
<td align="right">26.6%</td>
<td align="right">2,285,405,896</td>
<td align="right">26.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,288,588,415</td>
<td align="right">26.6%</td>
<td align="right">2,285,405,896</td>
<td align="right">26.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,819,367,307</td>
<td align="right">79.3%</td>
<td align="right">6,811,400,990</td>
<td align="right">79.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">222,068,043</td>
<td align="right">2.6%</td>
<td align="right">221,852,310</td>
<td align="right">2.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,314,307,299</td>
<td align="right">73.4%</td>
<td align="right">6,309,365,047</td>
<td align="right">73.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">856,806,787</td>
<td align="right">10.0%</td>
<td align="right">856,997,664</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">83,828,530</td>
<td align="right">1.0%</td>
<td align="right">83,814,664</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,041,991</td>
<td align="right">0.4%</td>
<td align="right">31,041,141</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">211,381,035</td>
<td align="right">2.5%</td>
<td align="right">211,380,981</td>
<td align="right">2.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">5,297,480</td>
<td align="right">0.1%</td>
<td align="right">5,297,480</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">28,760</td>
<td align="right">0.0%</td>
<td align="right">28,760</td>
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
<td align="right">8,242,863</td>
<td align="right"></td>
<td align="right">10,112,961</td>
<td align="right"></td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">64,396,154</td>
<td align="right"></td>
<td align="right">60,295,226</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">71,650,028</td>
<td align="right"></td>
<td align="right">69,424,547</td>
<td align="right"></td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">25,499,621,620</td>
<td align="right">22.5%</td>
<td align="right">25,652,826,322</td>
<td align="right">22.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">20,211,036</td>
<td align="right">0.1%</td>
<td align="right">20,142,546</td>
<td align="right">0.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">162,219,556</td>
<td align="right"></td>
<td align="right">161,793,604</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,262,766,497</td>
<td align="right"></td>
<td align="right">3,256,562,987</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">102,227,877,030</td>
<td align="right">78.3%</td>
<td align="right">102,339,252,162</td>
<td align="right">78.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">28,306,116,622</td>
<td align="right">21.7%</td>
<td align="right">28,278,938,541</td>
<td align="right">21.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">87,781,309,065</td>
<td align="right">77.5%</td>
<td align="right">87,842,596,702</td>
<td align="right">77.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">6,821,378,314</td>
<td align="right">37.8%</td>
<td align="right">6,816,746,431</td>
<td align="right">37.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">6,823,235,269</td>
<td align="right"></td>
<td align="right">6,818,624,928</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">11,577,540,679</td>
<td align="right"></td>
<td align="right">11,570,647,363</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,200,853,828</td>
<td align="right">62.2%</td>
<td align="right">11,195,284,110</td>
<td align="right">62.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">11,077,454,179</td>
<td align="right">61.5%</td>
<td align="right">11,071,999,258</td>
<td align="right">61.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">103,188,613</td>
<td align="right">0.6%</td>
<td align="right">103,142,306</td>
<td align="right">0.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">3,282,867,338</td>
<td align="right"></td>
<td align="right">3,282,542,620</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,306,540</td>
<td align="right">2.0%</td>
<td align="right">3,306,540</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">114,100</td>
<td align="right">0.1%</td>
<td align="right">114,100</td>
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
<td align="right">115,377,500</td>
<td align="right">16,305,457,657</td>
<td align="right">0</td>
<td align="right">115,018,560</td>
<td align="right">16,360,558,257</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,756,040</td>
<td align="right">6,978,839,428</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">7,033,291,944</td>
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
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-05-24
