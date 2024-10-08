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
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">3,600</td>
<td align="right">2,160</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">76,340</td>
<td align="right">47,900</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">189,424</td>
<td align="right">134,585</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">41,393</td>
<td align="right">51,536</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">51,945,467</td>
<td align="right">42,251,066</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">9,430,479</td>
<td align="right">7,774,325</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,040</td>
<td align="right">1,700</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">11,480</td>
<td align="right">10,080</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,506,198</td>
<td align="right">3,091,078</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">7,414,530</td>
<td align="right">6,803,678</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">117,080</td>
<td align="right">107,600</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">117,210,149</td>
<td align="right">125,503,674</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">101,060</td>
<td align="right">94,020</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">180,122,793</td>
<td align="right">169,076,163</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,668,152</td>
<td align="right">21,483,085</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">232,459</td>
<td align="right">221,409</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">16,321,531</td>
<td align="right">15,576,266</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">244,881</td>
<td align="right">233,763</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,919,097</td>
<td align="right">1,838,506</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">14,521,946</td>
<td align="right">13,924,318</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">122,242,773</td>
<td align="right">118,515,993</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">33,833,218</td>
<td align="right">34,692,514</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">22,355,193</td>
<td align="right">21,797,276</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">769,294</td>
<td align="right">750,434</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">591,742,367</td>
<td align="right">577,382,450</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">92,651,842</td>
<td align="right">90,492,326</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">26,826,091</td>
<td align="right">26,242,087</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">3,615,267</td>
<td align="right">3,537,092</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,311,706</td>
<td align="right">28,717,105</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,030,186</td>
<td align="right">1,990,404</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">18,576,503</td>
<td align="right">18,213,616</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">54,931,583</td>
<td align="right">53,884,122</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">840,826</td>
<td align="right">825,340</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">434,192</td>
<td align="right">426,264</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">5,333,882</td>
<td align="right">5,238,160</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">165,203</td>
<td align="right">162,466</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">140,707,881</td>
<td align="right">138,471,702</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,515,229</td>
<td align="right">1,492,097</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">442,840</td>
<td align="right">436,120</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">43,045,582</td>
<td align="right">43,691,705</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">20,030,614</td>
<td align="right">19,732,680</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">24,831,045</td>
<td align="right">24,464,107</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">49,997</td>
<td align="right">49,312</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">41,094,425</td>
<td align="right">40,566,913</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,450,564</td>
<td align="right">2,420,207</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">3,638,829</td>
<td align="right">3,594,659</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">42,260,652</td>
<td align="right">41,767,401</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">168,592,845</td>
<td align="right">166,633,036</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">197,146,116</td>
<td align="right">194,871,448</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">170,560,678</td>
<td align="right">168,632,845</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">51,050,971</td>
<td align="right">50,567,856</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">121,615,029</td>
<td align="right">120,538,833</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,352,364</td>
<td align="right">2,331,745</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,765</td>
<td align="right">528,280</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,760</td>
<td align="right">4,720</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">3,850,216</td>
<td align="right">3,818,921</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">142,511</td>
<td align="right">141,356</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,518,450</td>
<td align="right">1,506,247</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">4,081,669</td>
<td align="right">4,049,002</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">39,676</td>
<td align="right">39,970</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,388,295</td>
<td align="right">1,398,572</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">55,892,422</td>
<td align="right">55,498,465</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">49,711,115</td>
<td align="right">49,361,668</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,450,186</td>
<td align="right">1,440,299</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">867,370</td>
<td align="right">861,489</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">1,028,520</td>
<td align="right">1,035,464</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">2,841,351</td>
<td align="right">2,823,486</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,607,991</td>
<td align="right">8,553,957</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">3,445,072</td>
<td align="right">3,424,775</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">13,978,371</td>
<td align="right">13,897,814</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,491,122</td>
<td align="right">7,449,392</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,244</td>
<td align="right">118,580</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">54,922,680</td>
<td align="right">55,201,862</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">532,240</td>
<td align="right">529,584</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">5,027,429</td>
<td align="right">5,002,437</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">10,624,375</td>
<td align="right">10,672,550</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">3,095,562</td>
<td align="right">3,081,698</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">30,656,797</td>
<td align="right">30,520,969</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">39,215,106</td>
<td align="right">39,042,543</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">1,340,231</td>
<td align="right">1,334,509</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,184,486</td>
<td align="right">27,072,765</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">23,930,337</td>
<td align="right">23,834,721</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">13,209,634</td>
<td align="right">13,158,313</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">16,054,772</td>
<td align="right">15,992,518</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">4,842,138</td>
<td align="right">4,860,524</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,870,070</td>
<td align="right">1,863,330</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">5,045,967</td>
<td align="right">5,028,046</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">1,679,030</td>
<td align="right">1,673,240</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">8,958,396</td>
<td align="right">8,928,834</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">10,542,298</td>
<td align="right">10,508,923</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">16,564,066</td>
<td align="right">16,514,714</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">7,231,045</td>
<td align="right">7,209,704</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">12,328,564</td>
<td align="right">12,292,396</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">23,538,717</td>
<td align="right">23,469,707</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">21,656,000</td>
<td align="right">21,592,691</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">8,206,807</td>
<td align="right">8,185,656</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">1,204</td>
<td align="right">1,207</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">22,983,493</td>
<td align="right">22,929,707</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">10,023,333</td>
<td align="right">10,043,279</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">22,510</td>
<td align="right">22,552</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">25,266,570</td>
<td align="right">25,225,651</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">530,706</td>
<td align="right">529,877</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">1,118,638</td>
<td align="right">1,116,959</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">4,008</td>
<td align="right">4,014</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">181,848</td>
<td align="right">182,118</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,784,196</td>
<td align="right">1,781,627</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">14,540,828</td>
<td align="right">14,521,109</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,098,305</td>
<td align="right">2,095,475</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,656,052</td>
<td align="right">12,639,218</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">8,135,739</td>
<td align="right">8,125,004</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">41,797,017</td>
<td align="right">41,744,270</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">44,715,980</td>
<td align="right">44,661,482</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">32,967,521</td>
<td align="right">32,930,083</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">19,733,641</td>
<td align="right">19,711,893</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">5,719,510</td>
<td align="right">5,713,712</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">47,548</td>
<td align="right">47,596</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">2,582,390</td>
<td align="right">2,579,807</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">4,847,012</td>
<td align="right">4,842,427</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">227,611</td>
<td align="right">227,809</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">210,380</td>
<td align="right">210,202</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">262,586</td>
<td align="right">262,807</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">93,880</td>
<td align="right">93,957</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">21,352,869</td>
<td align="right">21,336,110</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,757,706</td>
<td align="right">64,706,920</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">19,021,273</td>
<td align="right">19,011,762</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">12,768</td>
<td align="right">12,774</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,592,093</td>
<td align="right">1,591,419</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">17,002,255</td>
<td align="right">16,996,177</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,980,074</td>
<td align="right">22,972,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">126,130,288</td>
<td align="right">126,163,715</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">13,187,815</td>
<td align="right">13,184,907</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">2,628,009</td>
<td align="right">2,627,431</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">411,790</td>
<td align="right">411,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">119,058</td>
<td align="right">119,072</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,349,022</td>
<td align="right">1,349,156</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,181,915</td>
<td align="right">1,182,026</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">543,653</td>
<td align="right">543,701</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">906,533</td>
<td align="right">906,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">906,533</td>
<td align="right">906,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">906,533</td>
<td align="right">906,487</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">3,312,372</td>
<td align="right">3,312,295</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">28,012,216</td>
<td align="right">28,012,833</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">178,043,952</td>
<td align="right">178,040,236</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">4,746,266</td>
<td align="right">4,746,221</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,572,567</td>
<td align="right">1,572,576</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">887,770</td>
<td align="right">887,768</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">519,360</td>
<td align="right">519,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">282,600</td>
<td align="right">282,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">282,560</td>
<td align="right">282,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">233,080</td>
<td align="right">233,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">140,940</td>
<td align="right">140,940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">139,180</td>
<td align="right">139,180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">72,160</td>
<td align="right">72,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">63,800</td>
<td align="right">63,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">19,260</td>
<td align="right">19,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">3,100</td>
<td align="right">3,100</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">2,660</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">1,840</td>
<td align="right">1,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">940</td>
<td align="right">940</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">480</td>
<td align="right">480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">300</td>
<td align="right">300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">60</td>
<td align="right">60</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">29,256,771</td>
<td align="right">60.8%</td>
<td align="right">28,657,972</td>
<td align="right">60.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">18,838,107</td>
<td align="right">39.1%</td>
<td align="right">18,842,260</td>
<td align="right">39.6%</td>
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
<td align="right">120</td>
<td align="right">0.0%</td>
<td align="right">120</td>
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
<td align="right">48,231</td>
<td align="right">87.8%</td>
<td align="right">52,327</td>
<td align="right">88.5%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,704</td>
<td align="right">12.2%</td>
<td align="right">6,806</td>
<td align="right">11.5%</td>
<td align="right">1.5%</td>
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
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">5,840</td>
<td align="right">12.1%</td>
<td align="right">7,520</td>
<td align="right">14.4%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">1,108</td>
<td align="right">2.3%</td>
<td align="right">1,400</td>
<td align="right">2.7%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">6,742</td>
<td align="right">14.0%</td>
<td align="right">7,836</td>
<td align="right">15.0%</td>
<td align="right">16.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">1,817</td>
<td align="right">3.8%</td>
<td align="right">2,020</td>
<td align="right">3.9%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,120</td>
<td align="right">4.4%</td>
<td align="right">2,329</td>
<td align="right">4.5%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">3,824</td>
<td align="right">7.9%</td>
<td align="right">4,159</td>
<td align="right">7.9%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,854</td>
<td align="right">5.9%</td>
<td align="right">3,075</td>
<td align="right">5.9%</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">2,051</td>
<td align="right">4.3%</td>
<td align="right">2,135</td>
<td align="right">4.1%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">3,841</td>
<td align="right">8.0%</td>
<td align="right">3,899</td>
<td align="right">7.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">226</td>
<td align="right">0.5%</td>
<td align="right">229</td>
<td align="right">0.4%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">9,144</td>
<td align="right">19.0%</td>
<td align="right">9,051</td>
<td align="right">17.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">582</td>
<td align="right">1.2%</td>
<td align="right">585</td>
<td align="right">1.1%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,521</td>
<td align="right">5.2%</td>
<td align="right">2,524</td>
<td align="right">4.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">1,183</td>
<td align="right">2.5%</td>
<td align="right">1,184</td>
<td align="right">2.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,700</td>
<td align="right">7.7%</td>
<td align="right">3,700</td>
<td align="right">7.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">376</td>
<td align="right">0.8%</td>
<td align="right">376</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">300</td>
<td align="right">0.6%</td>
<td align="right">300</td>
<td align="right">0.6%</td>
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
<td align="right">532,765</td>
<td align="right">100.0%</td>
<td align="right">528,280</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">3,488,392</td>
<td align="right">7.5%</td>
<td align="right">3,064,129</td>
<td align="right">6.7%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">42,687,035</td>
<td align="right">92.4%</td>
<td align="right">42,722,891</td>
<td align="right">93.2%</td>
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
<td align="right">14,927</td>
<td align="right">0.0%</td>
<td align="right">14,919</td>
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
<td align="left">Failure</td>
<td align="right">10,334</td>
<td align="right">57.3%</td>
<td align="right">19,462</td>
<td align="right">71.6%</td>
<td align="right">88.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,712</td>
<td align="right">42.7%</td>
<td align="right">7,727</td>
<td align="right">28.4%</td>
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
<td align="left">tuple slice</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">5</td>
<td align="right">0.0%</td>
<td align="right">150.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">1,200</td>
<td align="right">11.6%</td>
<td align="right">2,820</td>
<td align="right">14.5%</td>
<td align="right">135.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,152</td>
<td align="right">69.2%</td>
<td align="right">14,337</td>
<td align="right">73.7%</td>
<td align="right">100.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,960</td>
<td align="right">19.0%</td>
<td align="right">2,280</td>
<td align="right">11.7%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">20</td>
<td align="right">0.2%</td>
<td align="right">20</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,800</td>
<td align="right">0.0%</td>
<td align="right">19,962</td>
<td align="right">0.0%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">29,752,479</td>
<td align="right">7.2%</td>
<td align="right">30,005,669</td>
<td align="right">7.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">167,508</td>
<td align="right">0.0%</td>
<td align="right">167,655</td>
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
<td align="right">385,078,464</td>
<td align="right">92.8%</td>
<td align="right">384,850,949</td>
<td align="right">92.7%</td>
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
<td align="right">659,957</td>
<td align="right">100.0%</td>
<td align="right">666,857</td>
<td align="right">100.0%</td>
<td align="right">1.0%</td>
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
<td align="left">init not inline values</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
<td align="right">260</td>
<td align="right">260 / 0 !!</td>
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
<td align="right">7,984</td>
<td align="right">48.8%</td>
<td align="right">7,990</td>
<td align="right">48.9%</td>
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
<td align="right">3,580</td>
<td align="right">21.9%</td>
<td align="right">3,580</td>
<td align="right">21.9%</td>
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
<td align="right">22,595,428</td>
<td align="right">25.3%</td>
<td align="right">21,403,480</td>
<td align="right">24.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">465,611</td>
<td align="right">0.5%</td>
<td align="right">464,159</td>
<td align="right">0.5%</td>
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
<td align="right">66,066,997</td>
<td align="right">74.1%</td>
<td align="right">66,078,425</td>
<td align="right">75.1%</td>
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
<td align="right">63,096</td>
<td align="right">77.6%</td>
<td align="right">69,964</td>
<td align="right">79.4%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18,208</td>
<td align="right">22.4%</td>
<td align="right">18,193</td>
<td align="right">20.6%</td>
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
<td align="left">bool</td>
<td align="right">417</td>
<td align="right">0.7%</td>
<td align="right">1,404</td>
<td align="right">2.0%</td>
<td align="right">236.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">12,862</td>
<td align="right">20.4%</td>
<td align="right">16,734</td>
<td align="right">23.9%</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">12,152</td>
<td align="right">19.3%</td>
<td align="right">14,227</td>
<td align="right">20.3%</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">16,225</td>
<td align="right">25.7%</td>
<td align="right">16,162</td>
<td align="right">23.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">279</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,920</td>
<td align="right">15.7%</td>
<td align="right">9,918</td>
<td align="right">14.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,320</td>
<td align="right">16.4%</td>
<td align="right">10,320</td>
<td align="right">14.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">340</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">280</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">220</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
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
<td align="right">1,907,965</td>
<td align="right">6.0%</td>
<td align="right">1,824,763</td>
<td align="right">5.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">29,686,108</td>
<td align="right">93.9%</td>
<td align="right">29,687,767</td>
<td align="right">94.2%</td>
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
<td align="right">1,200</td>
<td align="right">0.0%</td>
<td align="right">1,200</td>
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
<td align="right">9,892</td>
<td align="right">88.9%</td>
<td align="right">12,503</td>
<td align="right">91.0%</td>
<td align="right">26.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,240</td>
<td align="right">11.1%</td>
<td align="right">1,240</td>
<td align="right">9.0%</td>
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
<td align="left">str</td>
<td align="right">280</td>
<td align="right">2.8%</td>
<td align="right">580</td>
<td align="right">4.6%</td>
<td align="right">107.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">940</td>
<td align="right">9.5%</td>
<td align="right">1,900</td>
<td align="right">15.2%</td>
<td align="right">102.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">3,556</td>
<td align="right">35.9%</td>
<td align="right">4,421</td>
<td align="right">35.4%</td>
<td align="right">24.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">5,116</td>
<td align="right">51.7%</td>
<td align="right">5,602</td>
<td align="right">44.8%</td>
<td align="right">9.5%</td>
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
<td align="right">113,433</td>
<td align="right">0.2%</td>
<td align="right">126,117</td>
<td align="right">0.3%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">27,137,773</td>
<td align="right">55.1%</td>
<td align="right">27,006,200</td>
<td align="right">54.9%</td>
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
<td align="right">21,983,757</td>
<td align="right">44.6%</td>
<td align="right">21,952,116</td>
<td align="right">44.7%</td>
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
<td align="left">Failure</td>
<td align="right">34,705</td>
<td align="right">71.2%</td>
<td align="right">54,532</td>
<td align="right">79.3%</td>
<td align="right">57.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">14,019</td>
<td align="right">28.8%</td>
<td align="right">14,269</td>
<td align="right">20.7%</td>
<td align="right">1.8%</td>
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
<td align="left">itertools</td>
<td align="right">1,840</td>
<td align="right">5.3%</td>
<td align="right">3,867</td>
<td align="right">7.1%</td>
<td align="right">110.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,960</td>
<td align="right">5.6%</td>
<td align="right">3,481</td>
<td align="right">6.4%</td>
<td align="right">77.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">140</td>
<td align="right">0.3%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,462</td>
<td align="right">10.0%</td>
<td align="right">5,509</td>
<td align="right">10.1%</td>
<td align="right">59.1%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,400</td>
<td align="right">4.0%</td>
<td align="right">2,220</td>
<td align="right">4.1%</td>
<td align="right">58.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,720</td>
<td align="right">13.6%</td>
<td align="right">7,380</td>
<td align="right">13.5%</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">16,378</td>
<td align="right">47.2%</td>
<td align="right">25,152</td>
<td align="right">46.1%</td>
<td align="right">53.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">80</td>
<td align="right">0.2%</td>
<td align="right">120</td>
<td align="right">0.2%</td>
<td align="right">50.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">780</td>
<td align="right">2.2%</td>
<td align="right">1,120</td>
<td align="right">2.1%</td>
<td align="right">43.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">4,005</td>
<td align="right">11.5%</td>
<td align="right">5,543</td>
<td align="right">10.2%</td>
<td align="right">38.4%</td>
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
<td align="right">33,216,584</td>
<td align="right">8.6%</td>
<td align="right">30,007,432</td>
<td align="right">8.0%</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">286,581,839</td>
<td align="right">74.5%</td>
<td align="right">280,669,505</td>
<td align="right">74.8%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">22,500</td>
<td align="right">0.0%</td>
<td align="right">22,380</td>
<td align="right">0.0%</td>
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
<td align="right">64,542,646</td>
<td align="right">16.8%</td>
<td align="right">64,469,512</td>
<td align="right">17.2%</td>
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
<td align="left">Failure</td>
<td align="right">121,886</td>
<td align="right">14.6%</td>
<td align="right">144,152</td>
<td align="right">18.1%</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">710,878</td>
<td align="right">85.4%</td>
<td align="right">650,287</td>
<td align="right">81.9%</td>
<td align="right">-8.5%</td>
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
<td align="left">builtin class method</td>
<td align="right">880</td>
<td align="right">0.7%</td>
<td align="right">1,200</td>
<td align="right">0.8%</td>
<td align="right">36.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">80</td>
<td align="right">0.1%</td>
<td align="right">33.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">59,460</td>
<td align="right">48.8%</td>
<td align="right">77,950</td>
<td align="right">54.1%</td>
<td align="right">31.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">360</td>
<td align="right">0.3%</td>
<td align="right">320</td>
<td align="right">0.2%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">14,880</td>
<td align="right">12.2%</td>
<td align="right">16,345</td>
<td align="right">11.3%</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">11,714</td>
<td align="right">9.6%</td>
<td align="right">12,660</td>
<td align="right">8.8%</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">4,800</td>
<td align="right">3.9%</td>
<td align="right">5,120</td>
<td align="right">3.6%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">7,743</td>
<td align="right">6.4%</td>
<td align="right">8,216</td>
<td align="right">5.7%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">9,262</td>
<td align="right">7.6%</td>
<td align="right">9,708</td>
<td align="right">6.7%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,907</td>
<td align="right">7.3%</td>
<td align="right">8,894</td>
<td align="right">6.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">120</td>
<td align="right">0.1%</td>
<td align="right">120</td>
<td align="right">0.1%</td>
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
<td align="right">265,086,714</td>
<td align="right">99.9%</td>
<td align="right">261,007,500</td>
<td align="right">99.9%</td>
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
<td align="right">90,019</td>
<td align="right">0.0%</td>
<td align="right">90,190</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">20,380</td>
<td align="right">0.0%</td>
<td align="right">20,380</td>
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
<td align="right">91,989</td>
<td align="right">100.0%</td>
<td align="right">92,088</td>
<td align="right">100.0%</td>
<td align="right">0.1%</td>
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
<td align="right">604</td>
<td align="right">0.0%</td>
<td align="right">607</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,996,031</td>
<td align="right">100.0%</td>
<td align="right">2,996,213</td>
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
<td align="right">600</td>
<td align="right">100.0%</td>
<td align="right">600</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">30,640</td>
<td align="right">2.1%</td>
<td align="right">32,740</td>
<td align="right">2.2%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">439,720</td>
<td align="right">29.9%</td>
<td align="right">431,960</td>
<td align="right">29.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">999,160</td>
<td align="right">67.8%</td>
<td align="right">1,004,864</td>
<td align="right">68.2%</td>
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
<td align="left">Failure</td>
<td align="right">3,060</td>
<td align="right">83.2%</td>
<td align="right">4,120</td>
<td align="right">86.2%</td>
<td align="right">34.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">620</td>
<td align="right">16.8%</td>
<td align="right">660</td>
<td align="right">13.8%</td>
<td align="right">6.5%</td>
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
<td align="right">3,060</td>
<td align="right">100.0%</td>
<td align="right">4,120</td>
<td align="right">100.0%</td>
<td align="right">34.6%</td>
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
<td align="right">11,175,418</td>
<td align="right">93.0%</td>
<td align="right">9,315,498</td>
<td align="right">92.1%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">426,066</td>
<td align="right">3.5%</td>
<td align="right">391,219</td>
<td align="right">3.9%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">402,986</td>
<td align="right">3.4%</td>
<td align="right">403,050</td>
<td align="right">4.0%</td>
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
<td align="right">12,972</td>
<td align="right">77.8%</td>
<td align="right">12,355</td>
<td align="right">76.9%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">3,704</td>
<td align="right">22.2%</td>
<td align="right">3,710</td>
<td align="right">23.1%</td>
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
<td align="left">not managed dict</td>
<td align="right">1,444</td>
<td align="right">39.0%</td>
<td align="right">1,450</td>
<td align="right">39.1%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,960</td>
<td align="right">52.9%</td>
<td align="right">1,960</td>
<td align="right">52.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">240</td>
<td align="right">6.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">60</td>
<td align="right">1.6%</td>
<td align="right">60</td>
<td align="right">1.6%</td>
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
<td align="right">940</td>
<td align="right">100.0%</td>
<td align="right">940</td>
<td align="right">100.0%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">183,867</td>
<td align="right">0.8%</td>
<td align="right">127,112</td>
<td align="right">0.6%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">22,622,056</td>
<td align="right">99.2%</td>
<td align="right">22,632,576</td>
<td align="right">99.4%</td>
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
<td align="right">2,833</td>
<td align="right">51.0%</td>
<td align="right">4,749</td>
<td align="right">63.5%</td>
<td align="right">67.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,724</td>
<td align="right">49.0%</td>
<td align="right">2,724</td>
<td align="right">36.5%</td>
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
<td align="left">dict subclass no override</td>
<td align="right">2,833</td>
<td align="right">100.0%</td>
<td align="right">4,749</td>
<td align="right">100.0%</td>
<td align="right">67.6%</td>
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
<td align="right">196,679,803</td>
<td align="right">93.8%</td>
<td align="right">197,047,187</td>
<td align="right">93.8%</td>
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
<td align="right">12,580,670</td>
<td align="right">6.0%</td>
<td align="right">12,562,793</td>
<td align="right">6.0%</td>
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
<td align="right">440,011</td>
<td align="right">0.2%</td>
<td align="right">440,300</td>
<td align="right">0.2%</td>
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
<td align="right">22,756</td>
<td align="right">27.6%</td>
<td align="right">23,729</td>
<td align="right">28.4%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">59,738</td>
<td align="right">72.4%</td>
<td align="right">59,804</td>
<td align="right">71.6%</td>
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
<td align="left">tuple</td>
<td align="right">10,793</td>
<td align="right">47.4%</td>
<td align="right">11,490</td>
<td align="right">48.4%</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">3,260</td>
<td align="right">14.3%</td>
<td align="right">3,420</td>
<td align="right">14.4%</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">3,509</td>
<td align="right">15.4%</td>
<td align="right">3,625</td>
<td align="right">15.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">1,440</td>
<td align="right">6.3%</td>
<td align="right">1,429</td>
<td align="right">6.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,634</td>
<td align="right">7.2%</td>
<td align="right">1,645</td>
<td align="right">6.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">2,080</td>
<td align="right">9.1%</td>
<td align="right">2,080</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">40</td>
<td align="right">0.2%</td>
<td align="right">40</td>
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
<td align="right">27,516</td>
<td align="right">0.0%</td>
<td align="right">27,551</td>
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
<td align="right">105,735,096</td>
<td align="right">100.0%</td>
<td align="right">105,693,158</td>
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
<td align="right">776</td>
<td align="right">6.4%</td>
<td align="right">1,011</td>
<td align="right">8.1%</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,384</td>
<td align="right">93.6%</td>
<td align="right">11,408</td>
<td align="right">91.9%</td>
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
<td align="left">sequence</td>
<td align="right">716</td>
<td align="right">92.3%</td>
<td align="right">951</td>
<td align="right">94.1%</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">60</td>
<td align="right">7.7%</td>
<td align="right">60</td>
<td align="right">5.9%</td>
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
<td align="right">64,485,031</td>
<td align="right">1.7%</td>
<td align="right">61,507,835</td>
<td align="right">1.7%</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">1,194,492,695</td>
<td align="right">32.0%</td>
<td align="right">1,165,603,327</td>
<td align="right">31.7%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">164,079,238</td>
<td align="right">4.4%</td>
<td align="right">161,559,338</td>
<td align="right">4.4%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">2,311,199,631</td>
<td align="right">61.9%</td>
<td align="right">2,291,721,591</td>
<td align="right">62.3%</td>
<td align="right">-0.8%</td>
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
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,488,392</td>
<td align="right">2.1%</td>
<td align="right">3,064,129</td>
<td align="right">1.9%</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">22,595,428</td>
<td align="right">13.8%</td>
<td align="right">21,403,480</td>
<td align="right">13.3%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">1,907,965</td>
<td align="right">1.2%</td>
<td align="right">1,824,763</td>
<td align="right">1.1%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">29,256,771</td>
<td align="right">17.9%</td>
<td align="right">28,657,972</td>
<td align="right">17.8%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">439,720</td>
<td align="right">0.3%</td>
<td align="right">431,960</td>
<td align="right">0.3%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">532,765</td>
<td align="right">0.3%</td>
<td align="right">528,280</td>
<td align="right">0.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">27,137,773</td>
<td align="right">16.6%</td>
<td align="right">27,006,200</td>
<td align="right">16.8%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,580,670</td>
<td align="right">7.7%</td>
<td align="right">12,562,793</td>
<td align="right">7.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">64,542,646</td>
<td align="right">39.5%</td>
<td align="right">64,469,512</td>
<td align="right">40.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">402,986</td>
<td align="right">0.2%</td>
<td align="right">403,050</td>
<td align="right">0.3%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">14,012,773</td>
<td align="right">21.7%</td>
<td align="right">11,384,056</td>
<td align="right">18.5%</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">425,086</td>
<td align="right">0.7%</td>
<td align="right">390,239</td>
<td align="right">0.6%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">5,407,697</td>
<td align="right">8.4%</td>
<td align="right">5,106,312</td>
<td align="right">8.3%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">6,162,961</td>
<td align="right">9.6%</td>
<td align="right">6,425,660</td>
<td align="right">10.4%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,548,850</td>
<td align="right">14.8%</td>
<td align="right">9,246,114</td>
<td align="right">15.0%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,669,067</td>
<td align="right">5.7%</td>
<td align="right">3,690,742</td>
<td align="right">6.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">464,011</td>
<td align="right">0.7%</td>
<td align="right">462,559</td>
<td align="right">0.8%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">14,347,924</td>
<td align="right">22.3%</td>
<td align="right">14,341,602</td>
<td align="right">23.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">2,661,158</td>
<td align="right">4.1%</td>
<td align="right">2,661,595</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">6,512,226</td>
<td align="right">10.1%</td>
<td align="right">6,512,549</td>
<td align="right">10.6%</td>
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
<td align="left">Frame objects created</td>
<td align="right">1,365,894</td>
<td align="right">0.5%</td>
<td align="right">1,386,120</td>
<td align="right">0.5%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">52,805,850</td>
<td align="right">19.4%</td>
<td align="right">52,845,726</td>
<td align="right">19.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">97,250,340</td>
<td align="right">35.7%</td>
<td align="right">97,290,927</td>
<td align="right">35.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">97,257,640</td>
<td align="right">35.7%</td>
<td align="right">97,298,227</td>
<td align="right">35.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">146,406,320</td>
<td align="right">53.7%</td>
<td align="right">146,352,111</td>
<td align="right">53.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">126,416,765</td>
<td align="right">46.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">126,373,185</td>
<td align="right">46.3%</td>
<td align="right">126,416,765</td>
<td align="right">46.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">29,115,545</td>
<td align="right">10.7%</td>
<td align="right">29,118,538</td>
<td align="right">10.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">243,347,602</td>
<td align="right">89.2%</td>
<td align="right">243,333,800</td>
<td align="right">89.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">23,782,907</td>
<td align="right">8.7%</td>
<td align="right">23,783,271</td>
<td align="right">8.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">11,824,676</td>
<td align="right">4.3%</td>
<td align="right">11,824,839</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">4,640</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">2,660</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">6,960</td>
<td align="right">0.0%</td>
<td align="right">6,960</td>
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
<td align="right">1,105,296</td>
<td align="right"></td>
<td align="right">1,446,864</td>
<td align="right"></td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">4,916,194</td>
<td align="right"></td>
<td align="right">5,302,022</td>
<td align="right"></td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">2,666,038,816</td>
<td align="right">59.8%</td>
<td align="right">2,764,196,353</td>
<td align="right">61.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">193,514,842</td>
<td align="right"></td>
<td align="right">199,948,730</td>
<td align="right"></td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">2,755,887,217</td>
<td align="right">54.8%</td>
<td align="right">2,839,121,430</td>
<td align="right">55.6%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">Interpreter increfs</td>
<td align="right">1,790,531,295</td>
<td align="right">40.2%</td>
<td align="right">1,765,103,742</td>
<td align="right">39.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">3,814,872</td>
<td align="right"></td>
<td align="right">3,859,252</td>
<td align="right"></td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,065,497</td>
<td align="right">0.2%</td>
<td align="right">1,071,185</td>
<td align="right">0.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">2,275,196,533</td>
<td align="right">45.2%</td>
<td align="right">2,264,844,399</td>
<td align="right">44.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">337,716,714</td>
<td align="right"></td>
<td align="right">338,471,500</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">292,972,230</td>
<td align="right">44.6%</td>
<td align="right">293,108,043</td>
<td align="right">44.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">291,882,273</td>
<td align="right">44.4%</td>
<td align="right">292,012,398</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">306,897,550</td>
<td align="right"></td>
<td align="right">307,027,920</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">364,539,796</td>
<td align="right">55.4%</td>
<td align="right">364,567,041</td>
<td align="right">55.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">364,778,873</td>
<td align="right"></td>
<td align="right">364,806,121</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">1,392,810</td>
<td align="right"></td>
<td align="right">1,392,867</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
<td align="right">24,460</td>
<td align="right">0.0%</td>
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
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">0</td>
</tr>
<tr>
<td align="right">2</td>
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
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">2,166</td>
<td align="right">2.4%</td>
<td align="right">2,676</td>
<td align="right">2.5%</td>
<td align="right">23.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">56,739</td>
<td align="right">63.9%</td>
<td align="right">69,812</td>
<td align="right">64.4%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">52,688</td>
<td align="right">59.3%</td>
<td align="right">64,807</td>
<td align="right">59.8%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">88,852</td>
<td align="right"></td>
<td align="right">108,433</td>
<td align="right"></td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">32,113</td>
<td align="right">36.1%</td>
<td align="right">38,621</td>
<td align="right">35.6%</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">370,299,253</td>
<td align="right"></td>
<td align="right">421,608,709</td>
<td align="right"></td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">313</td>
<td align="right">1.0%</td>
<td align="right">346</td>
<td align="right">0.9%</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">242</td>
<td align="right">0.3%</td>
<td align="right">263</td>
<td align="right">0.2%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">280</td>
<td align="right">0.3%</td>
<td align="right">300</td>
<td align="right">0.3%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">5,313,086,408</td>
<td align="right">1,434.8%</td>
<td align="right">5,570,377,882</td>
<td align="right">1,321.2%</td>
<td align="right">4.8%</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">32,113</td>
<td align="right"></td>
<td align="right">38,621</td>
<td align="right"></td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">30,494</td>
<td align="right">95.0%</td>
<td align="right">36,345</td>
<td align="right">94.1%</td>
<td align="right">19.2%</td>
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
<td align="right">160</td>
<td align="right">0.5%</td>
<td align="right">160</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
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
<td align="right">541</td>
<td align="right">1.7%</td>
<td align="right">473</td>
<td align="right">1.2%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">4,086</td>
<td align="right">12.7%</td>
<td align="right">5,664</td>
<td align="right">14.7%</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">4,342</td>
<td align="right">13.5%</td>
<td align="right">5,683</td>
<td align="right">14.7%</td>
<td align="right">30.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">12,371</td>
<td align="right">38.5%</td>
<td align="right">14,092</td>
<td align="right">36.5%</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">7,850</td>
<td align="right">24.4%</td>
<td align="right">9,242</td>
<td align="right">23.9%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,783</td>
<td align="right">8.7%</td>
<td align="right">3,287</td>
<td align="right">8.5%</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">140</td>
<td align="right">0.4%</td>
<td align="right">180</td>
<td align="right">0.5%</td>
<td align="right">28.6%</td>
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
<td align="right">4,106</td>
<td align="right">12.8%</td>
<td align="right">5,289</td>
<td align="right">13.7%</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">2,390</td>
<td align="right">7.4%</td>
<td align="right">3,296</td>
<td align="right">8.5%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,202</td>
<td align="right">25.5%</td>
<td align="right">9,853</td>
<td align="right">25.5%</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">10,020</td>
<td align="right">31.2%</td>
<td align="right">11,106</td>
<td align="right">28.8%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">5,216</td>
<td align="right">16.2%</td>
<td align="right">6,141</td>
<td align="right">15.9%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">520</td>
<td align="right">1.6%</td>
<td align="right">620</td>
<td align="right">1.6%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">40</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
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
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">338,436</td>
<td align="right">1,994,617</td>
<td align="right">489.4%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">341,516</td>
<td align="right">1,999,137</td>
<td align="right">485.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">320</td>
<td align="right">1,060</td>
<td align="right">231.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">969,070</td>
<td align="right">2,863,154</td>
<td align="right">195.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">3,765</td>
<td align="right">9,180</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">3,765</td>
<td align="right">9,180</td>
<td align="right">143.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">3,560</td>
<td align="right">8,520</td>
<td align="right">139.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">280</td>
<td align="right">660</td>
<td align="right">135.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">1,201,220</td>
<td align="right">468,540</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">6,420</td>
<td align="right">10,120</td>
<td align="right">57.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">3,900</td>
<td align="right">6,000</td>
<td align="right">53.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">3,080</td>
<td align="right">4,520</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">3,080</td>
<td align="right">4,520</td>
<td align="right">46.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">4,449,005</td>
<td align="right">2,632,301</td>
<td align="right">-40.8%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">8,160</td>
<td align="right">10,800</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">20,560</td>
<td align="right">26,441</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">20,560</td>
<td align="right">26,441</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">6,934,691</td>
<td align="right">8,817,700</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">14,860</td>
<td align="right">17,620</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">7,800</td>
<td align="right">9,200</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">17,702,941</td>
<td align="right">20,735,611</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">63,191,792</td>
<td align="right">73,900,362</td>
<td align="right">16.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">54,643,961</td>
<td align="right">63,722,588</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">219,328,059</td>
<td align="right">255,506,835</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">271,145</td>
<td align="right">315,626</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">346,698</td>
<td align="right">400,266</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">268,362</td>
<td align="right">309,771</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">343,159,545</td>
<td align="right">391,513,666</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">370,299,253</td>
<td align="right">421,608,709</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">711,330</td>
<td align="right">807,214</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">36,260</td>
<td align="right">40,840</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">5,287,217</td>
<td align="right">5,882,470</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">47,680</td>
<td align="right">52,960</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">26,754,177</td>
<td align="right">29,665,780</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">2,900,454</td>
<td align="right">2,585,874</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">980</td>
<td align="right">1,080</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">6,188,640</td>
<td align="right">6,786,412</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">5,748,572</td>
<td align="right">6,291,210</td>
<td align="right">9.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">29,920</td>
<td align="right">32,560</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">144,817,957</td>
<td align="right">156,170,531</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">3,985,172</td>
<td align="right">4,283,242</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">30,763,079</td>
<td align="right">33,025,859</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">413,620</td>
<td align="right">443,448</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">413,620</td>
<td align="right">443,448</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">16,211,390</td>
<td align="right">17,349,558</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">268,440</td>
<td align="right">286,020</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">45,139,045</td>
<td align="right">47,966,336</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">45,298,333</td>
<td align="right">48,133,142</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">31,960</td>
<td align="right">33,680</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">14,861,045</td>
<td align="right">15,552,640</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">54,718,942</td>
<td align="right">57,204,371</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,767,100</td>
<td align="right">16,461,922</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">15,767,100</td>
<td align="right">16,461,922</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">52,819,883</td>
<td align="right">55,006,541</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">25,113,948</td>
<td align="right">26,100,328</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">536,849,140</td>
<td align="right">557,467,872</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">57,325,528</td>
<td align="right">59,480,618</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">18,438,651</td>
<td align="right">19,123,416</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">23,181,783</td>
<td align="right">22,347,099</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">52,324,352</td>
<td align="right">54,151,838</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">61,720</td>
<td align="right">63,840</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">12,543,943</td>
<td align="right">12,967,623</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">432,240,271</td>
<td align="right">446,834,357</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">1,220</td>
<td align="right">1,260</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">83,917,278</td>
<td align="right">86,623,222</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">441,650</td>
<td align="right">455,626</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">441,650</td>
<td align="right">455,626</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">13,483,635</td>
<td align="right">13,073,697</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">13,206,702</td>
<td align="right">13,596,765</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">854,560</td>
<td align="right">879,500</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">50,101,240</td>
<td align="right">51,546,763</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">20,966,892</td>
<td align="right">21,543,747</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">24,308,844</td>
<td align="right">24,947,984</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">67,474,044</td>
<td align="right">69,216,216</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">617,260</td>
<td align="right">632,740</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">32,196,470</td>
<td align="right">31,412,211</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,254,320</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">943,873</td>
<td align="right">965,399</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">60,121,678</td>
<td align="right">61,412,838</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">446,180</td>
<td align="right">455,660</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">42,413,389</td>
<td align="right">43,267,742</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">17,974,464</td>
<td align="right">18,323,980</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">15,040,597</td>
<td align="right">15,332,352</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">35,847,324</td>
<td align="right">36,541,764</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">41,125,654</td>
<td align="right">41,867,135</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">3,238,333</td>
<td align="right">3,295,802</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">67,180</td>
<td align="right">68,340</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">658,678</td>
<td align="right">669,780</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">658,678</td>
<td align="right">669,780</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">418,540</td>
<td align="right">425,580</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">51,383,575</td>
<td align="right">52,242,760</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">26,443,210</td>
<td align="right">26,882,787</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">107,732,835</td>
<td align="right">109,522,268</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">110,600,015</td>
<td align="right">112,426,980</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">40,000</td>
<td align="right">40,660</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">40,000</td>
<td align="right">40,660</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">36,831,318</td>
<td align="right">37,426,443</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">13,680</td>
<td align="right">13,900</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">20,606,252</td>
<td align="right">20,935,215</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">185,058</td>
<td align="right">187,959</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">1,317,420</td>
<td align="right">1,337,380</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,466,546</td>
<td align="right">1,487,956</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">2,222,888</td>
<td align="right">2,254,447</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">189,120</td>
<td align="right">191,760</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">3,015,486</td>
<td align="right">3,057,189</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,909,025</td>
<td align="right">2,948,793</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">860,243</td>
<td align="right">871,438</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">115,192,090</td>
<td align="right">116,688,352</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">1,833,778</td>
<td align="right">1,856,932</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">968,377</td>
<td align="right">980,010</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">852,199</td>
<td align="right">862,411</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">44,902,662</td>
<td align="right">45,429,012</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">5,570,519</td>
<td align="right">5,633,622</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">82,627</td>
<td align="right">83,536</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">63,958,959</td>
<td align="right">64,629,431</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">460,541</td>
<td align="right">465,231</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">78,339,363</td>
<td align="right">77,563,672</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">42,601,601</td>
<td align="right">43,021,293</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,824,926</td>
<td align="right">4,871,359</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">20,899,299</td>
<td align="right">21,098,706</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">14,856,973</td>
<td align="right">14,998,578</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,675,809</td>
<td align="right">9,764,185</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">9,675,809</td>
<td align="right">9,764,185</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,295,280</td>
<td align="right">2,315,920</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">5,929,572</td>
<td align="right">5,979,053</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">6,117,621</td>
<td align="right">6,167,902</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">4,520,323</td>
<td align="right">4,556,680</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">7,758,743</td>
<td align="right">7,820,139</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">14,376,634</td>
<td align="right">14,490,302</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">6,087,981</td>
<td align="right">6,040,093</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">114,386</td>
<td align="right">113,637</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">27,952,016</td>
<td align="right">28,122,793</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">1,837,105</td>
<td align="right">1,848,202</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,932,855</td>
<td align="right">1,943,939</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">10,204,708</td>
<td align="right">10,262,898</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">7,570,823</td>
<td align="right">7,613,950</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">5,185,160</td>
<td align="right">5,214,576</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">9,898,793</td>
<td align="right">9,954,444</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">18,236,850</td>
<td align="right">18,136,579</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">10,463,948</td>
<td align="right">10,521,066</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">10,972,495</td>
<td align="right">11,026,350</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">134,622,839</td>
<td align="right">133,981,244</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">57,915,092</td>
<td align="right">58,164,666</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">1,894,574</td>
<td align="right">1,902,709</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">57,005,171</td>
<td align="right">57,249,781</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">24,567,338</td>
<td align="right">24,462,725</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">906,055</td>
<td align="right">909,282</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">19,952,764</td>
<td align="right">20,021,337</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">26,479,184</td>
<td align="right">26,568,846</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">10,563,186</td>
<td align="right">10,598,209</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">36,769,917</td>
<td align="right">36,877,502</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">18,429,541</td>
<td align="right">18,473,990</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">74,917,664</td>
<td align="right">75,090,610</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">8,731,078</td>
<td align="right">8,750,944</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">20,594,081</td>
<td align="right">20,633,804</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">18,113,484</td>
<td align="right">18,147,286</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">30,256,866</td>
<td align="right">30,311,689</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,488,115</td>
<td align="right">1,490,699</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">15,275,915</td>
<td align="right">15,301,438</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">4,317,978</td>
<td align="right">4,325,083</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">21,599,642</td>
<td align="right">21,634,401</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">25,419,354</td>
<td align="right">25,456,283</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">1,890,809</td>
<td align="right">1,893,529</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">15,530,849</td>
<td align="right">15,552,991</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">231,245,916</td>
<td align="right">231,562,144</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">97,568</td>
<td align="right">97,685</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">24,155,428</td>
<td align="right">24,182,734</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">9,962,649</td>
<td align="right">9,973,559</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">12,585,721</td>
<td align="right">12,599,355</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">10,789,970</td>
<td align="right">10,801,245</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">10,789,970</td>
<td align="right">10,801,245</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">26,033,025</td>
<td align="right">26,054,976</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">9,495,324</td>
<td align="right">9,502,423</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">18,702,203</td>
<td align="right">18,713,989</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">58,774,676</td>
<td align="right">58,788,271</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">62,126,643</td>
<td align="right">62,138,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">3,150,816</td>
<td align="right">3,150,570</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">16,858,338</td>
<td align="right">16,858,954</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">106,660</td>
<td align="right">106,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">49,740</td>
<td align="right">49,740</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">39,280</td>
<td align="right">39,280</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">36,660</td>
<td align="right">36,660</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">11,920</td>
<td align="right">11,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">11,040</td>
<td align="right">11,040</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">5,760</td>
<td align="right">5,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">2,540</td>
<td align="right">2,540</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">1,920</td>
<td align="right">1,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">1,220</td>
<td align="right">1,220</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">960</td>
<td align="right">960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">180</td>
<td align="right">180</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right"></td>
<td align="right">363</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">340</td>
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
<td align="left">SEND</td>
<td align="right">60</td>
<td align="right">160</td>
<td align="right">166.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">480</td>
<td align="right">671</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">3,864</td>
<td align="right">4,936</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">7,080</td>
<td align="right">8,559</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">20</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">80</td>
<td align="right">80</td>
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
<td align="right">80</td>
<td align="right">80</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-09-13
