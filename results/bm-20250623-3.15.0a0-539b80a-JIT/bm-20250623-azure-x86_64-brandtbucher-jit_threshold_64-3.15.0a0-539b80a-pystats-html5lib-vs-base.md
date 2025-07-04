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
<td align="left">STORE_SUBSCR</td>
<td align="right">2,225</td>
<td align="right">215</td>
<td align="right">-90.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,028</td>
<td align="right">181</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">4,687</td>
<td align="right">2,291</td>
<td align="right">-51.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">4,608</td>
<td align="right">3,500</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">4,190</td>
<td align="right">3,289</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">14,657</td>
<td align="right">16,008</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,076,296</td>
<td align="right">989,565</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,400</td>
<td align="right">4,985</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">1,531,768</td>
<td align="right">1,615,589</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">845,845</td>
<td align="right">821,418</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">3,636</td>
<td align="right">3,552</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">7,807,689</td>
<td align="right">7,640,466</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">9,390</td>
<td align="right">9,255</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">504,098</td>
<td align="right">498,001</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,621,059</td>
<td align="right">1,602,119</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">1,766,363</td>
<td align="right">1,746,317</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">741,527</td>
<td align="right">733,220</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">380,977</td>
<td align="right">376,851</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">739,220</td>
<td align="right">731,799</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">419,088</td>
<td align="right">414,946</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">702,437</td>
<td align="right">695,664</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">1,212,763</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">711,477</td>
<td align="right">704,898</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">735,096</td>
<td align="right">728,438</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">5,267,817</td>
<td align="right">5,220,121</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">1,174,015</td>
<td align="right">1,163,399</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,794,478</td>
<td align="right">1,778,267</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,343,945</td>
<td align="right">5,296,039</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">11,480,518</td>
<td align="right">11,377,768</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">1,689,564</td>
<td align="right">1,674,547</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">14,047,353</td>
<td align="right">13,923,891</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,722,805</td>
<td align="right">10,629,188</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">8,829,788</td>
<td align="right">8,754,170</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">6,704,782</td>
<td align="right">6,647,509</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6,456,330</td>
<td align="right">6,401,374</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">963,586</td>
<td align="right">955,429</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">910,607</td>
<td align="right">902,974</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">6,895,624</td>
<td align="right">6,838,049</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">6,736</td>
<td align="right">6,680</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">50,266,072</td>
<td align="right">49,850,398</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">2,943,635</td>
<td align="right">2,919,420</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">163,170,948</td>
<td align="right">161,830,237</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">5,618,575</td>
<td align="right">5,572,582</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,795,143</td>
<td align="right">1,780,476</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">14,215,086</td>
<td align="right">14,099,141</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">43,243,788</td>
<td align="right">42,891,396</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">1,573,321</td>
<td align="right">1,560,519</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">2,392,073</td>
<td align="right">2,372,612</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">10,466,186</td>
<td align="right">10,381,620</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">2,274,341</td>
<td align="right">2,256,003</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">85,106,506</td>
<td align="right">84,421,309</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">6,630,484</td>
<td align="right">6,577,186</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">1,684,378</td>
<td align="right">1,670,860</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">14,811,018</td>
<td align="right">14,692,217</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,733,290</td>
<td align="right">1,719,400</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">12,675,810</td>
<td align="right">12,574,248</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">11,508,859</td>
<td align="right">11,416,867</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">15,899,615</td>
<td align="right">15,772,668</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">55,986,726</td>
<td align="right">55,540,544</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">3,936,161</td>
<td align="right">3,904,796</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,718,981</td>
<td align="right">1,705,309</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">252</td>
<td align="right">250</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">5,470,562</td>
<td align="right">5,427,192</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">405,899</td>
<td align="right">402,686</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">13,571,825</td>
<td align="right">13,464,448</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">10,471,992</td>
<td align="right">10,389,214</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">8,210,200</td>
<td align="right">8,145,311</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">3,421,115</td>
<td align="right">3,394,079</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">23,872,047</td>
<td align="right">23,683,402</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">12,260,711</td>
<td align="right">12,163,862</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">2,763,640</td>
<td align="right">2,741,818</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">23,129,647</td>
<td align="right">22,947,123</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,510,539</td>
<td align="right">3,482,837</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,131,483</td>
<td align="right">5,091,031</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">2,949,490</td>
<td align="right">2,926,252</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">1,904</td>
<td align="right">1,889</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">6,887,951</td>
<td align="right">6,833,691</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">6,188,075</td>
<td align="right">6,139,338</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">711,495</td>
<td align="right">705,892</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">2,330,851</td>
<td align="right">2,312,497</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">3,186,109</td>
<td align="right">3,161,021</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">1,098,168</td>
<td align="right">1,089,521</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">707,644</td>
<td align="right">702,072</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">127</td>
<td align="right">126</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">3,898,273</td>
<td align="right">3,867,578</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,098,046</td>
<td align="right">1,089,400</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">707,648</td>
<td align="right">702,076</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">353,824</td>
<td align="right">351,038</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">396,370</td>
<td align="right">393,249</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">1,101,357</td>
<td align="right">1,092,685</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,686,755</td>
<td align="right">1,673,474</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">1,208,075</td>
<td align="right">1,198,563</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">604,166</td>
<td align="right">599,409</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">2,205,747</td>
<td align="right">2,188,380</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">1,618,852</td>
<td align="right">1,606,106</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_SLICE</td>
<td align="right">97,673</td>
<td align="right">96,904</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">141,125</td>
<td align="right">140,014</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">355,952</td>
<td align="right">353,150</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">355,444</td>
<td align="right">352,646</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">1,602,937</td>
<td align="right">1,590,319</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">358,257</td>
<td align="right">355,437</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">355,985</td>
<td align="right">353,183</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,142,870</td>
<td align="right">1,133,876</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">399,392</td>
<td align="right">396,249</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">357,245</td>
<td align="right">354,435</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">6,232</td>
<td align="right">6,183</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">2,938</td>
<td align="right">2,915</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">10,988</td>
<td align="right">10,902</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">12,269</td>
<td align="right">12,173</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">128</td>
<td align="right">127</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,026</td>
<td align="right">1,018</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">7,974</td>
<td align="right">7,912</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">12,308</td>
<td align="right">12,213</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">130</td>
<td align="right">129</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">393</td>
<td align="right">390</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">131</td>
<td align="right">130</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">1,091</td>
<td align="right">1,083</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">3,589</td>
<td align="right">3,563</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">140</td>
<td align="right">139</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">281</td>
<td align="right">279</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">141</td>
<td align="right">140</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,747</td>
<td align="right">33,541</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">167</td>
<td align="right">166</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,134</td>
<td align="right">1,131</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">574</td>
<td align="right">573</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">583</td>
<td align="right">583</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">419</td>
<td align="right">419</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">326</td>
<td align="right">326</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">219</td>
<td align="right">219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">120</td>
<td align="right">120</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">110</td>
<td align="right">110</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">109</td>
<td align="right">109</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">48</td>
<td align="right">48</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">46</td>
<td align="right">46</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">44</td>
<td align="right">44</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">42</td>
<td align="right">42</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">41</td>
<td align="right">41</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">39</td>
<td align="right">39</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">36</td>
<td align="right">36</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">33</td>
<td align="right">33</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">32</td>
<td align="right">32</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">31</td>
<td align="right">31</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">30</td>
<td align="right">30</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">20</td>
<td align="right">20</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">10</td>
<td align="right">10</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">8</td>
<td align="right">8</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">6</td>
<td align="right">6</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">2</td>
<td align="right">2</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">1</td>
<td align="right">1</td>
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
<td align="right">5,341,199</td>
<td align="right">14.4%</td>
<td align="right">5,293,331</td>
<td align="right">14.4%</td>
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
<td align="right">31,764,792</td>
<td align="right">85.6%</td>
<td align="right">31,514,753</td>
<td align="right">85.6%</td>
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
<td align="right">1,831</td>
<td align="right">0.0%</td>
<td align="right">1,829</td>
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
<td align="right">2,470</td>
<td align="right">89.0%</td>
<td align="right">2,433</td>
<td align="right">88.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">305</td>
<td align="right">11.0%</td>
<td align="right">304</td>
<td align="right">11.1%</td>
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
<td align="left">floor divide</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">2</td>
<td align="right">0.1%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">4</td>
<td align="right">0.2%</td>
<td align="right">3</td>
<td align="right">0.1%</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">52</td>
<td align="right">2.1%</td>
<td align="right">51</td>
<td align="right">2.1%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,727</td>
<td align="right">69.9%</td>
<td align="right">1,697</td>
<td align="right">69.7%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">334</td>
<td align="right">13.5%</td>
<td align="right">332</td>
<td align="right">13.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">175</td>
<td align="right">7.1%</td>
<td align="right">174</td>
<td align="right">7.2%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">52</td>
<td align="right">2.1%</td>
<td align="right">52</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48</td>
<td align="right">1.9%</td>
<td align="right">48</td>
<td align="right">2.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">44</td>
<td align="right">1.8%</td>
<td align="right">44</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">23</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">6</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">1,224,275</td>
<td align="right">100.0%</td>
<td align="right">1,212,763</td>
<td align="right">100.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">29,308,565</td>
<td align="right">83.5%</td>
<td align="right">29,077,809</td>
<td align="right">83.5%</td>
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
<td align="right">5,785,418</td>
<td align="right">16.5%</td>
<td align="right">5,739,910</td>
<td align="right">16.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">5,676,764</td>
<td align="right">16.2%</td>
<td align="right">5,632,115</td>
<td align="right">16.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">109,788</td>
<td align="right">100.0%</td>
<td align="right">108,926</td>
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
<td align="right">10</td>
<td align="right">50.0%</td>
<td align="right">10</td>
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
<td align="right">10</td>
<td align="right">100.0%</td>
<td align="right">10</td>
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
<td align="right">1,619,577</td>
<td align="right">5.8%</td>
<td align="right">1,600,664</td>
<td align="right">5.8%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">15,096</td>
<td align="right">0.1%</td>
<td align="right">14,977</td>
<td align="right">0.1%</td>
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
<td align="right">26,304,783</td>
<td align="right">94.1%</td>
<td align="right">26,097,698</td>
<td align="right">94.2%</td>
<td align="right">-0.8%</td>
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
<td align="right">1,335</td>
<td align="right">76.0%</td>
<td align="right">1,308</td>
<td align="right">75.7%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">422</td>
<td align="right">24.0%</td>
<td align="right">420</td>
<td align="right">24.3%</td>
<td align="right">-0.5%</td>
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
<td align="right">200</td>
<td align="right">15.0%</td>
<td align="right">179</td>
<td align="right">13.7%</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">186</td>
<td align="right">13.9%</td>
<td align="right">184</td>
<td align="right">14.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">675</td>
<td align="right">50.6%</td>
<td align="right">671</td>
<td align="right">51.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">175</td>
<td align="right">13.1%</td>
<td align="right">175</td>
<td align="right">13.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">92</td>
<td align="right">6.9%</td>
<td align="right">92</td>
<td align="right">7.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6</td>
<td align="right">0.4%</td>
<td align="right">6</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">1</td>
<td align="right">0.1%</td>
<td align="right">1</td>
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
<td align="right">909,743</td>
<td align="right">11.9%</td>
<td align="right">902,112</td>
<td align="right">11.9%</td>
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
<td align="right">6,754,800</td>
<td align="right">88.1%</td>
<td align="right">6,701,623</td>
<td align="right">88.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">818</td>
<td align="right">94.7%</td>
<td align="right">816</td>
<td align="right">94.7%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">46</td>
<td align="right">5.3%</td>
<td align="right">46</td>
<td align="right">5.3%</td>
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
<td align="right">3</td>
<td align="right">0.4%</td>
<td align="right">2</td>
<td align="right">0.2%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">268</td>
<td align="right">32.8%</td>
<td align="right">267</td>
<td align="right">32.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">479</td>
<td align="right">58.6%</td>
<td align="right">479</td>
<td align="right">58.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">68</td>
<td align="right">8.3%</td>
<td align="right">68</td>
<td align="right">8.3%</td>
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
<td align="right">46</td>
<td align="right">0.0%</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,184,505</td>
<td align="right">72.1%</td>
<td align="right">2,086,350</td>
<td align="right">71.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">845,444</td>
<td align="right">27.9%</td>
<td align="right">821,021</td>
<td align="right">28.2%</td>
<td align="right">-2.9%</td>
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
<td align="right">383</td>
<td align="right">95.5%</td>
<td align="right">379</td>
<td align="right">95.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">18</td>
<td align="right">4.5%</td>
<td align="right">18</td>
<td align="right">4.5%</td>
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
<td align="left">dict items</td>
<td align="right">163</td>
<td align="right">42.6%</td>
<td align="right">161</td>
<td align="right">42.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">188</td>
<td align="right">49.1%</td>
<td align="right">186</td>
<td align="right">49.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">23</td>
<td align="right">6.0%</td>
<td align="right">23</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">8</td>
<td align="right">2.1%</td>
<td align="right">8</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">1</td>
<td align="right">0.3%</td>
<td align="right">1</td>
<td align="right">0.3%</td>
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
<td align="left">self</td>
<td align="right">598,170</td>
<td align="right">598,170 / 0 !!</td>
<td align="right">593,460</td>
<td align="right">593,460 / 0 !!</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">966,864</td>
<td align="right">966,864 / 0 !!</td>
<td align="right">959,252</td>
<td align="right">959,252 / 0 !!</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">228,102</td>
<td align="right">228,102 / 0 !!</td>
<td align="right">226,311</td>
<td align="right">226,311 / 0 !!</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,989</td>
<td align="right">1,989 / 0 !!</td>
<td align="right">1,974</td>
<td align="right">1,974 / 0 !!</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">13</td>
<td align="right">13 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">4</td>
<td align="right">4 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
<td align="right">1</td>
<td align="right">1 / 0 !!</td>
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
<td align="right">5,126,681</td>
<td align="right">4.1%</td>
<td align="right">5,086,249</td>
<td align="right">4.1%</td>
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
<td align="right">119,281,375</td>
<td align="right">95.9%</td>
<td align="right">118,341,798</td>
<td align="right">95.9%</td>
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
<td align="right">18,976</td>
<td align="right">0.0%</td>
<td align="right">18,838</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">3,589</td>
<td align="right">75.1%</td>
<td align="right">3,570</td>
<td align="right">75.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,191</td>
<td align="right">24.9%</td>
<td align="right">1,191</td>
<td align="right">25.0%</td>
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
<td align="left">method</td>
<td align="right">2,392</td>
<td align="right">66.6%</td>
<td align="right">2,376</td>
<td align="right">66.6%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">184</td>
<td align="right">5.1%</td>
<td align="right">183</td>
<td align="right">5.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">267</td>
<td align="right">7.4%</td>
<td align="right">266</td>
<td align="right">7.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">387</td>
<td align="right">10.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">22</td>
<td align="right">0.6%</td>
<td align="right">22</td>
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
<td align="right">20,918,725</td>
<td align="right">100.0%</td>
<td align="right">20,745,516</td>
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
<td align="right">1,143</td>
<td align="right">0.0%</td>
<td align="right">1,134</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">245</td>
<td align="right">0.0%</td>
<td align="right">245</td>
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
<td align="right">329</td>
<td align="right">100.0%</td>
<td align="right">328</td>
<td align="right">100.0%</td>
<td align="right">-0.3%</td>
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
<td align="right">382</td>
<td align="right">98.5%</td>
<td align="right">379</td>
<td align="right">98.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3</td>
<td align="right">0.8%</td>
<td align="right">3</td>
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
<td align="left">Success</td>
<td align="right">3</td>
<td align="right">100.0%</td>
<td align="right">3</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,141,953</td>
<td align="right">7.8%</td>
<td align="right">1,132,963</td>
<td align="right">7.8%</td>
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
<td align="right">13,569,534</td>
<td align="right">92.1%</td>
<td align="right">13,462,710</td>
<td align="right">92.1%</td>
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
<td align="right">14,599</td>
<td align="right">0.1%</td>
<td align="right">14,487</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
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
<td align="right">742</td>
<td align="right">63.4%</td>
<td align="right">738</td>
<td align="right">63.2%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">429</td>
<td align="right">36.6%</td>
<td align="right">429</td>
<td align="right">36.8%</td>
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
<td align="left">split dict</td>
<td align="right">180</td>
<td align="right">24.3%</td>
<td align="right">178</td>
<td align="right">24.1%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">314</td>
<td align="right">42.3%</td>
<td align="right">312</td>
<td align="right">42.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">226</td>
<td align="right">30.5%</td>
<td align="right">226</td>
<td align="right">30.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">22</td>
<td align="right">3.0%</td>
<td align="right">22</td>
<td align="right">3.0%</td>
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
<td align="right">2,196</td>
<td align="right">0.1%</td>
<td align="right">188</td>
<td align="right">0.0%</td>
<td align="right">-91.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,988,729</td>
<td align="right">99.9%</td>
<td align="right">2,965,197</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
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
<td align="right">6</td>
<td align="right">20.7%</td>
<td align="right">4</td>
<td align="right">14.8%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">23</td>
<td align="right">79.3%</td>
<td align="right">23</td>
<td align="right">85.2%</td>
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
<td align="left">bytearray int</td>
<td align="right">5</td>
<td align="right">83.3%</td>
<td align="right">3</td>
<td align="right">75.0%</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">1</td>
<td align="right">16.7%</td>
<td align="right">1</td>
<td align="right">25.0%</td>
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
<td align="right">6,454,376</td>
<td align="right">23.7%</td>
<td align="right">6,399,434</td>
<td align="right">23.7%</td>
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
<td align="right">20,702,757</td>
<td align="right">76.1%</td>
<td align="right">20,535,306</td>
<td align="right">76.1%</td>
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
<td align="right">52,508</td>
<td align="right">0.2%</td>
<td align="right">52,125</td>
<td align="right">0.2%</td>
<td align="right">-0.7%</td>
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
<td align="right">1,848</td>
<td align="right">63.1%</td>
<td align="right">1,834</td>
<td align="right">63.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,080</td>
<td align="right">36.9%</td>
<td align="right">1,074</td>
<td align="right">36.9%</td>
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
<td align="left">sequence</td>
<td align="right">1,365</td>
<td align="right">73.9%</td>
<td align="right">1,353</td>
<td align="right">73.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">158</td>
<td align="right">8.5%</td>
<td align="right">157</td>
<td align="right">8.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">230</td>
<td align="right">12.4%</td>
<td align="right">229</td>
<td align="right">12.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">70</td>
<td align="right">3.8%</td>
<td align="right">70</td>
<td align="right">3.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">25</td>
<td align="right">1.4%</td>
<td align="right">25</td>
<td align="right">1.4%</td>
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
<td align="right">746,336</td>
<td align="right">100.0%</td>
<td align="right">740,472</td>
<td align="right">100.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">11</td>
<td align="right">0.0%</td>
<td align="right">11</td>
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
<td align="right">31</td>
<td align="right">100.0%</td>
<td align="right">31</td>
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
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">24,475,558</td>
<td align="right">3.2%</td>
<td align="right">24,244,057</td>
<td align="right">3.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">302,472,820</td>
<td align="right">39.3%</td>
<td align="right">299,835,359</td>
<td align="right">39.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">436,383,709</td>
<td align="right">56.7%</td>
<td align="right">432,902,823</td>
<td align="right">56.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">5,889,786</td>
<td align="right">0.8%</td>
<td align="right">5,843,525</td>
<td align="right">0.8%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">845,444</td>
<td align="right">3.0%</td>
<td align="right">821,021</td>
<td align="right">2.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">1,619,577</td>
<td align="right">5.7%</td>
<td align="right">1,600,664</td>
<td align="right">5.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">1,224,275</td>
<td align="right">4.3%</td>
<td align="right">1,212,763</td>
<td align="right">4.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">5,341,199</td>
<td align="right">18.8%</td>
<td align="right">5,293,331</td>
<td align="right">18.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">6,454,376</td>
<td align="right">22.8%</td>
<td align="right">6,399,434</td>
<td align="right">22.8%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">909,743</td>
<td align="right">3.2%</td>
<td align="right">902,112</td>
<td align="right">3.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">5,126,681</td>
<td align="right">18.1%</td>
<td align="right">5,086,249</td>
<td align="right">18.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">1,141,953</td>
<td align="right">4.0%</td>
<td align="right">1,132,963</td>
<td align="right">4.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">5,676,764</td>
<td align="right">20.0%</td>
<td align="right">5,632,115</td>
<td align="right">20.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">2,196</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">245</td>
<td align="right">0.0%</td>
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
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">10,830</td>
<td align="right">0.2%</td>
<td align="right">10,738</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">26,240</td>
<td align="right">0.4%</td>
<td align="right">26,020</td>
<td align="right">0.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">15,096</td>
<td align="right">0.3%</td>
<td align="right">14,977</td>
<td align="right">0.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">273,388</td>
<td align="right">4.6%</td>
<td align="right">271,234</td>
<td align="right">4.6%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,749,362</td>
<td align="right">46.7%</td>
<td align="right">2,727,732</td>
<td align="right">46.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,751,557</td>
<td align="right">46.7%</td>
<td align="right">2,729,920</td>
<td align="right">46.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">8,272</td>
<td align="right">0.1%</td>
<td align="right">8,207</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">11,252</td>
<td align="right">0.2%</td>
<td align="right">11,164</td>
<td align="right">0.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">25,764</td>
<td align="right">0.4%</td>
<td align="right">25,605</td>
<td align="right">0.4%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">6,333</td>
<td align="right">0.1%</td>
<td align="right">6,300</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
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
<td align="right">355,271</td>
<td align="right">1.5%</td>
<td align="right">352,474</td>
<td align="right">1.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">23,472,923</td>
<td align="right">98.3%</td>
<td align="right">23,288,131</td>
<td align="right">98.3%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">23,129,664</td>
<td align="right">96.9%</td>
<td align="right">22,947,578</td>
<td align="right">96.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">399,431</td>
<td align="right">1.7%</td>
<td align="right">396,288</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">399,465</td>
<td align="right">1.7%</td>
<td align="right">396,322</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">399,474</td>
<td align="right">1.7%</td>
<td align="right">396,331</td>
<td align="right">1.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">14,733</td>
<td align="right">0.1%</td>
<td align="right">14,618</td>
<td align="right">0.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">258</td>
<td align="right">0.0%</td>
<td align="right">256</td>
<td align="right">0.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">9</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">32</td>
<td align="right">0.0%</td>
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
<td align="right">76</td>
<td align="right">0.0%</td>
<td align="right">76</td>
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
<td align="right">68,255</td>
<td align="right"></td>
<td align="right">26,156</td>
<td align="right"></td>
<td align="right">-61.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">68,646</td>
<td align="right"></td>
<td align="right">26,798</td>
<td align="right"></td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">501</td>
<td align="right"></td>
<td align="right">728</td>
<td align="right"></td>
<td align="right">45.3%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">9,731,213</td>
<td align="right"></td>
<td align="right">9,017,365</td>
<td align="right"></td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">52,065,731</td>
<td align="right">14.8%</td>
<td align="right">50,655,425</td>
<td align="right">14.6%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">2,757,284</td>
<td align="right">0.8%</td>
<td align="right">2,729,160</td>
<td align="right">0.8%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">21,099,635</td>
<td align="right"></td>
<td align="right">20,891,543</td>
<td align="right"></td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">21,101,361</td>
<td align="right">65.4%</td>
<td align="right">20,893,744</td>
<td align="right">65.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">67,396,769</td>
<td align="right">19.2%</td>
<td align="right">66,744,672</td>
<td align="right">19.2%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">64,006,709</td>
<td align="right">19.1%</td>
<td align="right">63,416,116</td>
<td align="right">19.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,266,630</td>
<td align="right">1.3%</td>
<td align="right">4,230,317</td>
<td align="right">1.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">879,756</td>
<td align="right"></td>
<td align="right">872,598</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">368,537</td>
<td align="right"></td>
<td align="right">365,636</td>
<td align="right"></td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">73,493,761</td>
<td align="right">21.9%</td>
<td align="right">72,918,097</td>
<td align="right">21.9%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">220,003</td>
<td align="right">0.7%</td>
<td align="right">218,283</td>
<td align="right">0.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">228,426,832</td>
<td align="right">65.1%</td>
<td align="right">226,676,951</td>
<td align="right">65.4%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">193,340,245</td>
<td align="right">57.7%</td>
<td align="right">191,876,896</td>
<td align="right">57.7%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">8,915</td>
<td align="right">0.0%</td>
<td align="right">8,866</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">11,153,500</td>
<td align="right">34.6%</td>
<td align="right">11,108,344</td>
<td align="right">34.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,924,582</td>
<td align="right">33.9%</td>
<td align="right">10,881,195</td>
<td align="right">34.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">7,090,611</td>
<td align="right"></td>
<td align="right">7,076,410</td>
<td align="right"></td>
<td align="right">-0.2%</td>
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
<td align="right">1,039</td>
<td align="right">284,996</td>
<td align="right">21,960,079</td>
<td align="right">1,163,703</td>
<td align="right">2,064,273</td>
<td align="right">1,050</td>
<td align="right">5,836</td>
<td align="right">21,547,614</td>
<td align="right">1,263,289</td>
<td align="right">1,950,155</td>
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
<td align="right">83</td>
<td align="right">3.7%</td>
<td align="right">268</td>
<td align="right">10.3%</td>
<td align="right">222.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">44</td>
<td align="right">1.9%</td>
<td align="right">77</td>
<td align="right">2.9%</td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">2,259</td>
<td align="right"></td>
<td align="right">2,614</td>
<td align="right"></td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">
Unknown callee
<details>
<summary>ⓘ</summary>

A trace is abandoned because the target of a call is unknown.
</details>
</td>
<td align="right">2,132</td>
<td align="right">94.4%</td>
<td align="right">2,269</td>
<td align="right">86.8%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">1,531,665</td>
<td align="right"></td>
<td align="right">1,617,600</td>
<td align="right"></td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">56,550,005</td>
<td align="right">3,692.1%</td>
<td align="right">57,493,236</td>
<td align="right">3,554.2%</td>
<td align="right">1.7%</td>
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
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
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
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
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
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
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
<td align="right">44</td>
<td align="right"></td>
<td align="right">77</td>
<td align="right"></td>
<td align="right">75.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">44</td>
<td align="right">100.0%</td>
<td align="right">77</td>
<td align="right">100.0%</td>
<td align="right">75.0%</td>
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
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">259,281</td>
<td align="right">71.9%</td>
<td align="right">1,054,233</td>
<td align="right">90.0%</td>
<td align="right">306.6%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">7,608</td>
<td align="right">2.1%</td>
<td align="right">26,360</td>
<td align="right">2.3%</td>
<td align="right">246.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">360,448</td>
<td align="right"></td>
<td align="right">1,171,456</td>
<td align="right"></td>
<td align="right">225.0%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">93,559</td>
<td align="right">26.0%</td>
<td align="right">90,863</td>
<td align="right">7.8%</td>
<td align="right">-2.9%</td>
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
<td align="right">4,096</td>
<td align="right">0.3%</td>
<td align="right">4,096 / 0 !!</td>
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
<td align="left">1</td>
<td align="right">2.3%</td>
<td align="left">2</td>
<td align="right">2.6%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">42</td>
<td align="right">95.5%</td>
<td align="left">26</td>
<td align="right">33.8%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">1</td>
<td align="right">2.3%</td>
<td align="left">28</td>
<td align="right">36.4%</td>
<td align="right">2,700.0%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">21</td>
<td align="right">27.3%</td>
<td align="right"></td>
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
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">1</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">42</td>
<td align="right">95.5%</td>
<td align="right">6</td>
<td align="right">7.8%</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">1</td>
<td align="right">2.3%</td>
<td align="right">48</td>
<td align="right">62.3%</td>
<td align="right">4,700.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">1.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">27.3%</td>
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
<td align="left"><= 32</td>
<td align="right">22</td>
<td align="right">50.0%</td>
<td align="right">5</td>
<td align="right">6.5%</td>
<td align="right">-77.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">22</td>
<td align="right">50.0%</td>
<td align="right">50</td>
<td align="right">64.9%</td>
<td align="right">127.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">1</td>
<td align="right">1.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21</td>
<td align="right">27.3%</td>
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
<td align="left">_LOAD_FAST_BORROW_2</td>
<td align="right">2,893</td>
<td align="right">14,502</td>
<td align="right">401.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,893</td>
<td align="right">10,455</td>
<td align="right">261.4%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">2,893</td>
<td align="right">8,213</td>
<td align="right">183.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,893</td>
<td align="right">8,117</td>
<td align="right">180.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">90,357</td>
<td align="right">167,840</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">90,357</td>
<td align="right">167,840</td>
<td align="right">85.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">2,893</td>
<td align="right">5,069</td>
<td align="right">75.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_TUPLE</td>
<td align="right">2,893</td>
<td align="right">4,483</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">2,893</td>
<td align="right">4,483</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">2,893</td>
<td align="right">4,383</td>
<td align="right">51.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_DICT</td>
<td align="right">2,893</td>
<td align="right">4,130</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">2,893</td>
<td align="right">3,302</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">2,893</td>
<td align="right">3,301</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">2,893</td>
<td align="right">3,287</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">2,893</td>
<td align="right">3,264</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW</td>
<td align="right">122,022</td>
<td align="right">134,823</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">124,915</td>
<td align="right">137,473</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">1,531,665</td>
<td align="right">1,617,600</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">1,531,665</td>
<td align="right">1,617,378</td>
<td align="right">5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">122,022</td>
<td align="right">127,745</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">2,311,183</td>
<td align="right">2,400,973</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">3,405,130</td>
<td align="right">3,492,816</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">122,592</td>
<td align="right">124,971</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">122,592</td>
<td align="right">124,971</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">122,022</td>
<td align="right">124,386</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">11,643,184</td>
<td align="right">11,841,273</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">122,022</td>
<td align="right">124,030</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">10,122,734</td>
<td align="right">10,233,655</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,004,287</td>
<td align="right">1,014,221</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">779,518</td>
<td align="right">783,373</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">1,093,947</td>
<td align="right">1,089,455</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_4</td>
<td align="right">778,399</td>
<td align="right">780,873</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,565,669</td>
<td align="right">1,561,267</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_ANY_SET</td>
<td align="right">775,506</td>
<td align="right">773,339</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">790,163</td>
<td align="right">788,009</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,659,616</td>
<td align="right">2,653,785</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,659,616</td>
<td align="right">2,653,785</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_1</td>
<td align="right">790,163</td>
<td align="right">791,571</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_6</td>
<td align="right">1,687,691</td>
<td align="right">1,685,439</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">1,884,110</td>
<td align="right">1,881,785</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_0</td>
<td align="right">1,093,947</td>
<td align="right">1,092,881</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">3,452,672</td>
<td align="right">3,449,458</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_3</td>
<td align="right">793,056</td>
<td align="right">792,558</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">775,506</td>
<td align="right">775,224</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_5</td>
<td align="right">778,399</td>
<td align="right">778,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">775,506</td>
<td align="right">775,619</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">790,163</td>
<td align="right">790,109</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right"></td>
<td align="right">3,770</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_LIST</td>
<td align="right"></td>
<td align="right">2,939</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right"></td>
<td align="right">2,284</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right"></td>
<td align="right">2,185</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right"></td>
<td align="right">2,147</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right"></td>
<td align="right">2,128</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right"></td>
<td align="right">2,085</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_CALLABLE_LIST_APPEND</td>
<td align="right"></td>
<td align="right">2,069</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_NOT_NULL</td>
<td align="right"></td>
<td align="right">2,065</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST_TIER_TWO</td>
<td align="right"></td>
<td align="right">2,014</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right"></td>
<td align="right">1,887</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right"></td>
<td align="right">1,778</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_DICT</td>
<td align="right"></td>
<td align="right">1,760</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right"></td>
<td align="right">1,735</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right"></td>
<td align="right">1,734</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_UNICODE</td>
<td align="right"></td>
<td align="right">1,469</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right"></td>
<td align="right">1,404</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right"></td>
<td align="right">1,384</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right"></td>
<td align="right">1,366</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right"></td>
<td align="right">1,185</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right"></td>
<td align="right">1,094</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right">1,080</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right"></td>
<td align="right">1,041</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right"></td>
<td align="right">985</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_DICT</td>
<td align="right"></td>
<td align="right">985</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_UNICODE</td>
<td align="right"></td>
<td align="right">955</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TOS_LIST</td>
<td align="right"></td>
<td align="right">897</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">871</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right"></td>
<td align="right">868</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right"></td>
<td align="right">850</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right"></td>
<td align="right">847</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right"></td>
<td align="right">711</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_RECURSION_REMAINING</td>
<td align="right"></td>
<td align="right">711</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right"></td>
<td align="right">711</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right"></td>
<td align="right">711</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right"></td>
<td align="right">676</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right"></td>
<td align="right">668</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right"></td>
<td align="right">635</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_ITER</td>
<td align="right"></td>
<td align="right">577</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right"></td>
<td align="right">539</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOS_TUPLE</td>
<td align="right"></td>
<td align="right">537</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right"></td>
<td align="right">537</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right"></td>
<td align="right">536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right"></td>
<td align="right">536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right"></td>
<td align="right">536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right"></td>
<td align="right">536</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBSCR_STR_INT</td>
<td align="right"></td>
<td align="right">533</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right"></td>
<td align="right">473</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right"></td>
<td align="right">438</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right"></td>
<td align="right">415</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_UNDER_INLINE</td>
<td align="right"></td>
<td align="right">411</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right"></td>
<td align="right">384</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">377</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right"></td>
<td align="right">377</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right"></td>
<td align="right">376</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right"></td>
<td align="right">373</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right">364</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_BORROW_7</td>
<td align="right"></td>
<td align="right">337</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right"></td>
<td align="right">334</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right"></td>
<td align="right">334</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right"></td>
<td align="right">334</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right"></td>
<td align="right">262</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right"></td>
<td align="right">219</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right"></td>
<td align="right">207</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right"></td>
<td align="right">200</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right">139</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right"></td>
<td align="right">100</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right"></td>
<td align="right">74</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right"></td>
<td align="right">70</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right"></td>
<td align="right">68</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right"></td>
<td align="right">61</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right"></td>
<td align="right">43</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right"></td>
<td align="right">29</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right"></td>
<td align="right">19</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right"></td>
<td align="right">16</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right"></td>
<td align="right">13</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">5</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right">5</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right"></td>
<td align="right">3</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right"></td>
<td align="right">1</td>
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
Stats gathered on: 2025-06-24
