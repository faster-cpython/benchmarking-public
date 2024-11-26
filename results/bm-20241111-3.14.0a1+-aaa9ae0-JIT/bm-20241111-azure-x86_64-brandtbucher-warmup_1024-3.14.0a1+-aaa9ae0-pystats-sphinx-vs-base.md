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
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">143</td>
<td align="right">2,560</td>
<td align="right">1,690.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">503,509</td>
<td align="right">2,124,332</td>
<td align="right">321.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">3,232</td>
<td align="right">10,427</td>
<td align="right">222.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">2,908</td>
<td align="right">8,138</td>
<td align="right">179.8%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">12,211</td>
<td align="right">23,619</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">133,326</td>
<td align="right">256,325</td>
<td align="right">92.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">4,135,397</td>
<td align="right">7,192,222</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">23,883</td>
<td align="right">39,531</td>
<td align="right">65.5%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">15,203</td>
<td align="right">23,499</td>
<td align="right">54.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">767,278</td>
<td align="right">1,064,420</td>
<td align="right">38.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">243,771</td>
<td align="right">303,494</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">13,575,264</td>
<td align="right">10,783,491</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">191,999</td>
<td align="right">229,008</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">10,151,166</td>
<td align="right">8,397,843</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">162,514</td>
<td align="right">189,522</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">66,815,972</td>
<td align="right">76,321,736</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">15,844,228</td>
<td align="right">13,673,063</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">6,961,834</td>
<td align="right">7,877,860</td>
<td align="right">13.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">105,390,167</td>
<td align="right">117,933,288</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">751,015</td>
<td align="right">833,666</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">41,830,547</td>
<td align="right">37,363,551</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">3,354,120</td>
<td align="right">3,709,868</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">16,691,924</td>
<td align="right">14,946,699</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">21,145</td>
<td align="right">23,298</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">1,214,513</td>
<td align="right">1,335,109</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">15,286,017</td>
<td align="right">13,783,687</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">965,538</td>
<td align="right">1,057,677</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">1,223,093</td>
<td align="right">1,335,990</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">543,755</td>
<td align="right">593,122</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">37,699,333</td>
<td align="right">34,478,958</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">61,173,934</td>
<td align="right">66,330,005</td>
<td align="right">8.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">9,015,194</td>
<td align="right">8,269,818</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">111,404,967</td>
<td align="right">120,321,563</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">129,448,403</td>
<td align="right">139,675,846</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">3,157,580</td>
<td align="right">3,370,845</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">136,487</td>
<td align="right">145,359</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">20,237</td>
<td align="right">21,530</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">472,548</td>
<td align="right">501,891</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">14,687,697</td>
<td align="right">13,794,779</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">4,447,682</td>
<td align="right">4,716,908</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">14,979,449</td>
<td align="right">14,090,782</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">5,673,546</td>
<td align="right">6,000,439</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">674,766</td>
<td align="right">711,967</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">5,551,535</td>
<td align="right">5,799,724</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">2,903,605</td>
<td align="right">3,018,714</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">1,176,488</td>
<td align="right">1,222,508</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">1,487,005</td>
<td align="right">1,544,573</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">12,434,265</td>
<td align="right">11,960,102</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">813,673</td>
<td align="right">841,901</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,813,876</td>
<td align="right">8,523,254</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">1,501,188</td>
<td align="right">1,549,586</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">2,020,630</td>
<td align="right">2,082,142</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">72,027</td>
<td align="right">69,882</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,322,690</td>
<td align="right">11,981,402</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">83,284,275</td>
<td align="right">85,552,561</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">452,259,330</td>
<td align="right">464,489,699</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">115,170,020</td>
<td align="right">112,089,619</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">116,642</td>
<td align="right">113,692</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,386,316</td>
<td align="right">1,420,930</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">4,145,810</td>
<td align="right">4,244,359</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">9,702,525</td>
<td align="right">9,924,984</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">482,688</td>
<td align="right">493,697</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,615,714</td>
<td align="right">29,939,483</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">2,526,184</td>
<td align="right">2,472,863</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,881,252</td>
<td align="right">1,919,532</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">118,124,311</td>
<td align="right">116,078,788</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">97,455,816</td>
<td align="right">95,769,817</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">8,559</td>
<td align="right">8,706</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">322,845</td>
<td align="right">317,474</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">630,505</td>
<td align="right">640,821</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">549,638</td>
<td align="right">558,449</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">10,663</td>
<td align="right">10,810</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,496,639</td>
<td align="right">1,515,911</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">3,300,695</td>
<td align="right">3,341,303</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">1,197,282</td>
<td align="right">1,210,941</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">1,055,983</td>
<td align="right">1,067,550</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">92,560,003</td>
<td align="right">91,562,669</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">2,908,524</td>
<td align="right">2,939,159</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,372,273</td>
<td align="right">6,438,048</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">5,883,740</td>
<td align="right">5,942,801</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">28,099,290</td>
<td align="right">28,380,210</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,484,123</td>
<td align="right">3,518,933</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">4,623,259</td>
<td align="right">4,582,017</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">151,760</td>
<td align="right">153,054</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">7,679,847</td>
<td align="right">7,743,437</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">1,720,488</td>
<td align="right">1,734,723</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">5,935,033</td>
<td align="right">5,983,843</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">14,313,468</td>
<td align="right">14,427,653</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">130,681,162</td>
<td align="right">131,692,139</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">140,094</td>
<td align="right">141,132</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">5,975,946</td>
<td align="right">6,020,146</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">8,330,168</td>
<td align="right">8,390,534</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">55,586,845</td>
<td align="right">55,962,621</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,073,538</td>
<td align="right">2,059,728</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">450,525</td>
<td align="right">453,495</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">38,129,908</td>
<td align="right">38,369,269</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">31,175,796</td>
<td align="right">31,364,294</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">341,596</td>
<td align="right">343,616</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">5,646,577</td>
<td align="right">5,679,340</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">4,913,795</td>
<td align="right">4,941,580</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">39,250,305</td>
<td align="right">39,460,187</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">254,403</td>
<td align="right">255,749</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">9,880,106</td>
<td align="right">9,930,131</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">2,087</td>
<td align="right">2,097</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">24,556,304</td>
<td align="right">24,672,823</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">4,459,335</td>
<td align="right">4,479,474</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,354,604</td>
<td align="right">3,369,186</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">24,350,516</td>
<td align="right">24,453,639</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">10,942,335</td>
<td align="right">10,986,234</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">604,930</td>
<td align="right">607,336</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">4,227,412</td>
<td align="right">4,241,362</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">2,328,267</td>
<td align="right">2,335,948</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">4,517,330</td>
<td align="right">4,531,937</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">2,978,522</td>
<td align="right">2,988,020</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">81,173,052</td>
<td align="right">80,947,434</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">7,288,786</td>
<td align="right">7,308,773</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">5,328,034</td>
<td align="right">5,341,749</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">20,790,625</td>
<td align="right">20,840,307</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">42,749,748</td>
<td align="right">42,850,447</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">741,982</td>
<td align="right">743,590</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">1,536,826</td>
<td align="right">1,540,015</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">3,710,137</td>
<td align="right">3,703,867</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">543,148</td>
<td align="right">544,060</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">1,131,361</td>
<td align="right">1,133,247</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">18,663,133</td>
<td align="right">18,693,559</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">2,911,420</td>
<td align="right">2,914,762</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">21,991</td>
<td align="right">22,016</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,481,476</td>
<td align="right">1,483,037</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">3,131</td>
<td align="right">3,134</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">9,210</td>
<td align="right">9,217</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">1,284,166</td>
<td align="right">1,283,392</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">266,486</td>
<td align="right">266,366</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">1,089,069</td>
<td align="right">1,089,439</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">76,798</td>
<td align="right">76,822</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">38,482</td>
<td align="right">38,493</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">32,159</td>
<td align="right">32,168</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">26,024</td>
<td align="right">26,031</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">219,438</td>
<td align="right">219,496</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">155,067,826</td>
<td align="right">155,096,781</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">1,265,664</td>
<td align="right">1,265,883</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">39,526,700</td>
<td align="right">39,528,183</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">129,137</td>
<td align="right">129,141</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">2,973,780</td>
<td align="right">2,973,783</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">2,687,015</td>
<td align="right">2,687,017</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">1,477,291</td>
<td align="right">1,477,292</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">1,522,494</td>
<td align="right">1,522,495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">1,522,494</td>
<td align="right">1,522,495</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">38,864,488</td>
<td align="right">38,864,488</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">22,677,619</td>
<td align="right">22,677,619</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">296,772</td>
<td align="right">296,772</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">158,435</td>
<td align="right">158,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">146,477</td>
<td align="right">146,477</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">117,056</td>
<td align="right">117,056</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">84,414</td>
<td align="right">84,414</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">35,881</td>
<td align="right">35,881</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">28,815</td>
<td align="right">28,815</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">16,387</td>
<td align="right">16,387</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">8,706</td>
<td align="right">8,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">4,541</td>
<td align="right">4,541</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">2,240</td>
<td align="right">2,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">1,357</td>
<td align="right">1,357</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">348</td>
<td align="right">348</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">315</td>
<td align="right">315</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">259</td>
<td align="right">259</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">129</td>
<td align="right">129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">117</td>
<td align="right">117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">117</td>
<td align="right">117</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">63</td>
<td align="right">63</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16</td>
<td align="right">16</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">14</td>
<td align="right">14</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">9</td>
<td align="right">9</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">7</td>
<td align="right">7</td>
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
<td align="right">6,362,992</td>
<td align="right">37.0%</td>
<td align="right">6,428,738</td>
<td align="right">37.2%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,824,891</td>
<td align="right">62.9%</td>
<td align="right">10,824,891</td>
<td align="right">62.7%</td>
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
<td align="right">8,692</td>
<td align="right">100.0%</td>
<td align="right">8,721</td>
<td align="right">100.0%</td>
<td align="right">0.3%</td>
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
<td align="left">true divide other</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">46</td>
<td align="right">0.5%</td>
<td align="right">1,433.3%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">16</td>
<td align="right">0.2%</td>
<td align="right">100.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">184</td>
<td align="right">2.1%</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">863</td>
<td align="right">9.9%</td>
<td align="right">824</td>
<td align="right">9.4%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">3,006</td>
<td align="right">34.6%</td>
<td align="right">2,976</td>
<td align="right">34.1%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">2,376</td>
<td align="right">27.3%</td>
<td align="right">2,378</td>
<td align="right">27.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">1,510</td>
<td align="right">17.4%</td>
<td align="right">1,510</td>
<td align="right">17.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">251</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">229</td>
<td align="right">2.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">127</td>
<td align="right">1.5%</td>
<td align="right">127</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">66</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
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
<td align="right">2,073,538</td>
<td align="right">100.0%</td>
<td align="right">2,059,728</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">3,347,459</td>
<td align="right">8.8%</td>
<td align="right">3,362,115</td>
<td align="right">8.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">32,467,998</td>
<td align="right">85.0%</td>
<td align="right">32,467,998</td>
<td align="right">85.0%</td>
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
<td align="right">2,363,146</td>
<td align="right">6.2%</td>
<td align="right">2,363,146</td>
<td align="right">6.2%</td>
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
<td align="right">5,906</td>
<td align="right">11.4%</td>
<td align="right">5,832</td>
<td align="right">11.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">45,681</td>
<td align="right">88.6%</td>
<td align="right">45,681</td>
<td align="right">88.7%</td>
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
<td align="left">out of range</td>
<td align="right">2,972</td>
<td align="right">50.3%</td>
<td align="right">2,914</td>
<td align="right">50.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">1,271</td>
<td align="right">21.5%</td>
<td align="right">1,252</td>
<td align="right">21.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">780</td>
<td align="right">13.2%</td>
<td align="right">783</td>
<td align="right">13.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">307</td>
<td align="right">5.2%</td>
<td align="right">307</td>
<td align="right">5.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">246</td>
<td align="right">4.2%</td>
<td align="right">246</td>
<td align="right">4.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">238</td>
<td align="right">4.0%</td>
<td align="right">238</td>
<td align="right">4.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">92</td>
<td align="right">1.6%</td>
<td align="right">92</td>
<td align="right">1.6%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,258</td>
<td align="right">0.0%</td>
<td align="right">14,265</td>
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
<td align="right">1,807,280</td>
<td align="right">0.7%</td>
<td align="right">1,807,320</td>
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
<td align="right">239,408,563</td>
<td align="right">99.2%</td>
<td align="right">239,405,772</td>
<td align="right">99.2%</td>
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
<td align="right">59,873</td>
<td align="right">100.0%</td>
<td align="right">59,897</td>
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
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">424</td>
<td align="right">424 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">24</td>
<td align="right">24 / 0 !!</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
<td align="right">3</td>
<td align="right">3 / 0 !!</td>
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
<td align="right">334</td>
<td align="right">15.5%</td>
<td align="right">339</td>
<td align="right">15.7%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">64</td>
<td align="right">3.0%</td>
<td align="right">64</td>
<td align="right">3.0%</td>
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
<td align="right">626,616</td>
<td align="right">5.4%</td>
<td align="right">636,925</td>
<td align="right">5.5%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">7,975</td>
<td align="right">0.1%</td>
<td align="right">8,055</td>
<td align="right">0.1%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">10,926,007</td>
<td align="right">94.5%</td>
<td align="right">10,926,004</td>
<td align="right">94.4%</td>
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
<td align="right">2,669</td>
<td align="right">66.4%</td>
<td align="right">2,676</td>
<td align="right">66.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,349</td>
<td align="right">33.6%</td>
<td align="right">1,351</td>
<td align="right">33.5%</td>
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
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">43</td>
<td align="right">1.6%</td>
<td align="right">104.8%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">27</td>
<td align="right">1.0%</td>
<td align="right">28</td>
<td align="right">1.0%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">1,821</td>
<td align="right">68.2%</td>
<td align="right">1,803</td>
<td align="right">67.4%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">255</td>
<td align="right">9.6%</td>
<td align="right">257</td>
<td align="right">9.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">259</td>
<td align="right">9.7%</td>
<td align="right">259</td>
<td align="right">9.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">157</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">106</td>
<td align="right">4.0%</td>
<td align="right">106</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">21</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">3,478,905</td>
<td align="right">22.9%</td>
<td align="right">3,513,573</td>
<td align="right">23.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,731,547</td>
<td align="right">77.1%</td>
<td align="right">11,731,563</td>
<td align="right">76.9%</td>
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
<td align="right">4,691</td>
<td align="right">100.0%</td>
<td align="right">4,830</td>
<td align="right">100.0%</td>
<td align="right">3.0%</td>
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
<td align="left">list</td>
<td align="right">561</td>
<td align="right">12.0%</td>
<td align="right">627</td>
<td align="right">13.0%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">1,973</td>
<td align="right">42.1%</td>
<td align="right">2,085</td>
<td align="right">43.2%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">1,423</td>
<td align="right">30.3%</td>
<td align="right">1,384</td>
<td align="right">28.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">734</td>
<td align="right">15.6%</td>
<td align="right">734</td>
<td align="right">15.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,350,279</td>
<td align="right">4.3%</td>
<td align="right">3,705,179</td>
<td align="right">4.7%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">2,226,944</td>
<td align="right">2.9%</td>
<td align="right">2,360,881</td>
<td align="right">3.0%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">71,438,775</td>
<td align="right">92.8%</td>
<td align="right">72,592,052</td>
<td align="right">92.3%</td>
<td align="right">1.6%</td>
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
<td align="right">3,196</td>
<td align="right">7.0%</td>
<td align="right">4,043</td>
<td align="right">8.2%</td>
<td align="right">26.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42,653</td>
<td align="right">93.0%</td>
<td align="right">45,169</td>
<td align="right">91.8%</td>
<td align="right">5.9%</td>
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
<td align="right">15</td>
<td align="right">0.5%</td>
<td align="right">61</td>
<td align="right">1.5%</td>
<td align="right">306.7%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">142</td>
<td align="right">4.4%</td>
<td align="right">272</td>
<td align="right">6.7%</td>
<td align="right">91.5%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">25</td>
<td align="right">0.8%</td>
<td align="right">47</td>
<td align="right">1.2%</td>
<td align="right">88.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">275</td>
<td align="right">8.6%</td>
<td align="right">474</td>
<td align="right">11.7%</td>
<td align="right">72.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">183</td>
<td align="right">5.7%</td>
<td align="right">296</td>
<td align="right">7.3%</td>
<td align="right">61.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">315</td>
<td align="right">9.9%</td>
<td align="right">449</td>
<td align="right">11.1%</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">76</td>
<td align="right">2.4%</td>
<td align="right">97</td>
<td align="right">2.4%</td>
<td align="right">27.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">54</td>
<td align="right">1.7%</td>
<td align="right">40</td>
<td align="right">1.0%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">1,053</td>
<td align="right">32.9%</td>
<td align="right">1,210</td>
<td align="right">29.9%</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">838</td>
<td align="right">26.2%</td>
<td align="right">872</td>
<td align="right">21.6%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">220</td>
<td align="right">6.9%</td>
<td align="right">225</td>
<td align="right">5.6%</td>
<td align="right">2.3%</td>
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
<td align="right">68,567,373</td>
<td align="right">22.4%</td>
<td align="right">66,188,484</td>
<td align="right">21.8%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">30,299,507</td>
<td align="right">9.9%</td>
<td align="right">29,623,245</td>
<td align="right">9.8%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">207,542,471</td>
<td align="right">67.7%</td>
<td align="right">207,498,564</td>
<td align="right">68.3%</td>
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
<td align="right">64,390</td>
<td align="right">0.0%</td>
<td align="right">64,390</td>
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
<td align="right">9,658</td>
<td align="right">0.6%</td>
<td align="right">9,387</td>
<td align="right">0.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,598,496</td>
<td align="right">99.4%</td>
<td align="right">1,553,894</td>
<td align="right">99.4%</td>
<td align="right">-2.8%</td>
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
<td align="left">not in dict</td>
<td align="right">300</td>
<td align="right">3.1%</td>
<td align="right">259</td>
<td align="right">2.8%</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">2,205</td>
<td align="right">22.8%</td>
<td align="right">1,933</td>
<td align="right">20.6%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">1,089</td>
<td align="right">11.3%</td>
<td align="right">1,017</td>
<td align="right">10.8%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">2,985</td>
<td align="right">30.9%</td>
<td align="right">3,075</td>
<td align="right">32.8%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">73</td>
<td align="right">0.8%</td>
<td align="right">71</td>
<td align="right">0.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">115</td>
<td align="right">1.2%</td>
<td align="right">118</td>
<td align="right">1.3%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">69</td>
<td align="right">0.7%</td>
<td align="right">68</td>
<td align="right">0.7%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">994</td>
<td align="right">10.3%</td>
<td align="right">996</td>
<td align="right">10.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">645</td>
<td align="right">6.7%</td>
<td align="right">645</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">530</td>
<td align="right">5.5%</td>
<td align="right">530</td>
<td align="right">5.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">7</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">2</td>
<td align="right">0.0%</td>
<td align="right">2</td>
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
<td align="right">166,551,737</td>
<td align="right">100.0%</td>
<td align="right">184,250,909</td>
<td align="right">100.0%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">3,023</td>
<td align="right">0.0%</td>
<td align="right">3,036</td>
<td align="right">0.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">12,364</td>
<td align="right">0.0%</td>
<td align="right">12,384</td>
<td align="right">0.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">61</td>
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
<td align="right">19,401</td>
<td align="right">100.0%</td>
<td align="right">19,413</td>
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
<td align="right">50</td>
<td align="right">0.0%</td>
<td align="right">50</td>
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
<td align="right">424,921</td>
<td align="right">99.9%</td>
<td align="right">424,921</td>
<td align="right">99.9%</td>
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
<td align="right">209</td>
<td align="right">100.0%</td>
<td align="right">209</td>
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
<td align="right">4,490</td>
<td align="right">29.2%</td>
<td align="right">4,490</td>
<td align="right">29.2%</td>
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
<td align="right">10,810</td>
<td align="right">70.4%</td>
<td align="right">10,810</td>
<td align="right">70.4%</td>
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
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">4</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">47</td>
<td align="right">92.2%</td>
<td align="right">47</td>
<td align="right">92.2%</td>
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
<td align="left">list</td>
<td align="right">47</td>
<td align="right">100.0%</td>
<td align="right">47</td>
<td align="right">100.0%</td>
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
<td align="right">8,799,199</td>
<td align="right">27.1%</td>
<td align="right">8,508,715</td>
<td align="right">26.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">9,551,844</td>
<td align="right">29.4%</td>
<td align="right">9,520,740</td>
<td align="right">29.6%</td>
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
<td align="right">14,099,784</td>
<td align="right">43.4%</td>
<td align="right">14,112,098</td>
<td align="right">43.9%</td>
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
<td align="right">9,528</td>
<td align="right">4.9%</td>
<td align="right">9,390</td>
<td align="right">4.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">184,888</td>
<td align="right">95.1%</td>
<td align="right">184,297</td>
<td align="right">95.2%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">8</td>
<td align="right">0.1%</td>
<td align="right">9</td>
<td align="right">0.1%</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">4,795</td>
<td align="right">50.3%</td>
<td align="right">4,656</td>
<td align="right">49.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">2,626</td>
<td align="right">27.6%</td>
<td align="right">2,626</td>
<td align="right">28.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">992</td>
<td align="right">10.4%</td>
<td align="right">992</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">643</td>
<td align="right">6.7%</td>
<td align="right">643</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">308</td>
<td align="right">3.2%</td>
<td align="right">308</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">94</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">53</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">5</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">1</td>
<td align="right">0.0%</td>
<td align="right">1</td>
<td align="right">0.0%</td>
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
<td align="right">116,642</td>
<td align="right">100.0%</td>
<td align="right">113,692</td>
<td align="right">100.0%</td>
<td align="right">-2.5%</td>
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
<td align="right">1,477,527</td>
<td align="right">13.9%</td>
<td align="right">1,479,091</td>
<td align="right">13.9%</td>
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
<td align="right">9,156,392</td>
<td align="right">86.1%</td>
<td align="right">9,156,397</td>
<td align="right">86.1%</td>
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
<td align="right">3,472</td>
<td align="right">87.9%</td>
<td align="right">3,469</td>
<td align="right">87.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">477</td>
<td align="right">12.1%</td>
<td align="right">477</td>
<td align="right">12.1%</td>
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
<td align="right">10</td>
<td align="right">0.3%</td>
<td align="right">7</td>
<td align="right">0.2%</td>
<td align="right">-30.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">2,961</td>
<td align="right">85.3%</td>
<td align="right">2,961</td>
<td align="right">85.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">341</td>
<td align="right">9.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">113</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">47</td>
<td align="right">1.4%</td>
<td align="right">47</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,295,516</td>
<td align="right">2.3%</td>
<td align="right">3,478,568</td>
<td align="right">1.9%</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">12,194,103</td>
<td align="right">6.6%</td>
<td align="right">11,883,894</td>
<td align="right">6.5%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">168,010,673</td>
<td align="right">91.0%</td>
<td align="right">168,391,312</td>
<td align="right">91.6%</td>
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
<td align="right">124,567</td>
<td align="right">59.4%</td>
<td align="right">93,501</td>
<td align="right">57.3%</td>
<td align="right">-24.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">85,006</td>
<td align="right">40.6%</td>
<td align="right">69,566</td>
<td align="right">42.7%</td>
<td align="right">-18.2%</td>
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
<td align="right">110,970</td>
<td align="right">89.1%</td>
<td align="right">80,127</td>
<td align="right">85.7%</td>
<td align="right">-27.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">94</td>
<td align="right">0.1%</td>
<td align="right">117</td>
<td align="right">0.1%</td>
<td align="right">24.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">1,074</td>
<td align="right">0.9%</td>
<td align="right">906</td>
<td align="right">1.0%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">2,160</td>
<td align="right">1.7%</td>
<td align="right">2,081</td>
<td align="right">2.2%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">213</td>
<td align="right">0.2%</td>
<td align="right">214</td>
<td align="right">0.2%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">9,949</td>
<td align="right">8.0%</td>
<td align="right">9,949</td>
<td align="right">10.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">107</td>
<td align="right">0.1%</td>
<td align="right">107</td>
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
<td align="right">14,605,616</td>
<td align="right">98.0%</td>
<td align="right">14,605,623</td>
<td align="right">98.0%</td>
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
<td align="right">296,271</td>
<td align="right">2.0%</td>
<td align="right">296,271</td>
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
<td align="left">Success</td>
<td align="right">404</td>
<td align="right">80.6%</td>
<td align="right">404</td>
<td align="right">80.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">97</td>
<td align="right">19.4%</td>
<td align="right">97</td>
<td align="right">19.4%</td>
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
<td align="left">sequence</td>
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">74</td>
<td align="right">76.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">23</td>
<td align="right">23.7%</td>
<td align="right">23</td>
<td align="right">23.7%</td>
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
<td align="right">956,383,270</td>
<td align="right">35.1%</td>
<td align="right">997,530,739</td>
<td align="right">36.1%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">88,836,877</td>
<td align="right">3.3%</td>
<td align="right">85,743,536</td>
<td align="right">3.1%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">72,983,693</td>
<td align="right">2.7%</td>
<td align="right">72,141,630</td>
<td align="right">2.6%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">1,605,042,208</td>
<td align="right">58.9%</td>
<td align="right">1,611,125,244</td>
<td align="right">58.2%</td>
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
<td align="left">FOR_ITER</td>
<td align="right">3,350,279</td>
<td align="right">4.6%</td>
<td align="right">3,705,179</td>
<td align="right">5.2%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">8,799,199</td>
<td align="right">12.1%</td>
<td align="right">8,508,715</td>
<td align="right">11.9%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">12,194,103</td>
<td align="right">16.8%</td>
<td align="right">11,883,894</td>
<td align="right">16.6%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">30,299,507</td>
<td align="right">41.8%</td>
<td align="right">29,623,245</td>
<td align="right">41.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">626,616</td>
<td align="right">0.9%</td>
<td align="right">636,925</td>
<td align="right">0.9%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">6,362,992</td>
<td align="right">8.8%</td>
<td align="right">6,428,738</td>
<td align="right">9.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">3,478,905</td>
<td align="right">4.8%</td>
<td align="right">3,513,573</td>
<td align="right">4.9%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">2,073,538</td>
<td align="right">2.9%</td>
<td align="right">2,059,728</td>
<td align="right">2.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">3,347,459</td>
<td align="right">4.6%</td>
<td align="right">3,362,115</td>
<td align="right">4.7%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">1,477,527</td>
<td align="right">2.0%</td>
<td align="right">1,479,091</td>
<td align="right">2.1%</td>
<td align="right">0.1%</td>
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
<td align="left">TO_BOOL_NONE</td>
<td align="right">3,588,802</td>
<td align="right">4.0%</td>
<td align="right">2,764,343</td>
<td align="right">3.2%</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">11,547,768</td>
<td align="right">13.0%</td>
<td align="right">9,986,990</td>
<td align="right">11.6%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">5,366,223</td>
<td align="right">6.0%</td>
<td align="right">4,688,806</td>
<td align="right">5.5%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">9,116,593</td>
<td align="right">10.3%</td>
<td align="right">8,045,674</td>
<td align="right">9.4%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">1,112,912</td>
<td align="right">1.3%</td>
<td align="right">1,180,610</td>
<td align="right">1.4%</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">1,114,032</td>
<td align="right">1.3%</td>
<td align="right">1,180,271</td>
<td align="right">1.4%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">32,564,975</td>
<td align="right">36.7%</td>
<td align="right">33,540,850</td>
<td align="right">39.1%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">9,440,228</td>
<td align="right">10.6%</td>
<td align="right">9,373,975</td>
<td align="right">10.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">9,511,738</td>
<td align="right">10.7%</td>
<td align="right">9,483,522</td>
<td align="right">11.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,338,580</td>
<td align="right">2.6%</td>
<td align="right">2,338,580</td>
<td align="right">2.7%</td>
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
<td align="right">18,591,204</td>
<td align="right">8.5%</td>
<td align="right">18,831,477</td>
<td align="right">8.6%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">39,664,227</td>
<td align="right">18.1%</td>
<td align="right">39,903,592</td>
<td align="right">18.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">39,665,971</td>
<td align="right">18.1%</td>
<td align="right">39,905,336</td>
<td align="right">18.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">40,534,333</td>
<td align="right">18.5%</td>
<td align="right">40,776,668</td>
<td align="right">18.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">40,534,333</td>
<td align="right">18.5%</td>
<td align="right">40,776,668</td>
<td align="right">18.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">868,362</td>
<td align="right">0.4%</td>
<td align="right">871,332</td>
<td align="right">0.4%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">178,870,789</td>
<td align="right">81.5%</td>
<td align="right">178,631,486</td>
<td align="right">81.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">7,048,786</td>
<td align="right">3.2%</td>
<td align="right">7,051,218</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">158,050,102</td>
<td align="right">72.0%</td>
<td align="right">158,051,076</td>
<td align="right">72.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">387</td>
<td align="right">0.0%</td>
<td align="right">387</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">1,357</td>
<td align="right">0.0%</td>
<td align="right">1,357</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">10,484,608</td>
<td align="right">4.8%</td>
<td align="right">10,484,608</td>
<td align="right">4.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">502,515</td>
<td align="right">0.2%</td>
<td align="right">502,515</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">88</td>
<td align="right">0.0%</td>
<td align="right">88</td>
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
<td align="right">1,111,061</td>
<td align="right"></td>
<td align="right">1,190,375</td>
<td align="right"></td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">290,099,017</td>
<td align="right">7.4%</td>
<td align="right">310,427,291</td>
<td align="right">7.9%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">8,011,915</td>
<td align="right"></td>
<td align="right">7,540,400</td>
<td align="right"></td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">440,948,149</td>
<td align="right">10.1%</td>
<td align="right">460,144,101</td>
<td align="right">10.6%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">9,120,791</td>
<td align="right"></td>
<td align="right">8,728,655</td>
<td align="right"></td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">1,554,046</td>
<td align="right">0.5%</td>
<td align="right">1,494,055</td>
<td align="right">0.5%</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">836,231,920</td>
<td align="right">19.2%</td>
<td align="right">815,429,547</td>
<td align="right">18.8%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">812,847,424</td>
<td align="right">20.7%</td>
<td align="right">801,772,617</td>
<td align="right">20.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">1,197,326,000</td>
<td align="right">30.5%</td>
<td align="right">1,204,524,664</td>
<td align="right">30.7%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">1,476,812,060</td>
<td align="right">34.0%</td>
<td align="right">1,468,588,964</td>
<td align="right">33.8%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">1,621,744,372</td>
<td align="right">41.3%</td>
<td align="right">1,612,799,932</td>
<td align="right">41.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">1,593,291,072</td>
<td align="right">36.7%</td>
<td align="right">1,599,742,800</td>
<td align="right">36.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">201,687,696</td>
<td align="right"></td>
<td align="right">202,453,545</td>
<td align="right"></td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">155,995,558</td>
<td align="right"></td>
<td align="right">155,696,914</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">83,874,316</td>
<td align="right"></td>
<td align="right">83,838,327</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">251,837,217</td>
<td align="right"></td>
<td align="right">251,933,920</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">83,887,976</td>
<td align="right">25.7%</td>
<td align="right">83,856,291</td>
<td align="right">25.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">240,793,993</td>
<td align="right">73.8%</td>
<td align="right">240,833,739</td>
<td align="right">73.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">61,855</td>
<td align="right">0.0%</td>
<td align="right">61,861</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">242,409,894</td>
<td align="right">74.3%</td>
<td align="right">242,389,655</td>
<td align="right">74.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">3,079,773</td>
<td align="right"></td>
<td align="right">3,079,774</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">997,148</td>
<td align="right">32.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">98,881</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (too big)</td>
<td align="right">1,344</td>
<td align="right">0.0%</td>
<td align="right">1,344</td>
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
<td align="right">6,239</td>
<td align="right">12,356,611</td>
<td align="right">369,527,243</td>
<td align="right">6,218</td>
<td align="right">12,431,214</td>
<td align="right">370,338,664</td>
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
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">149</td>
<td align="right">0.0%</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">-85.9%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">32</td>
<td align="right">0.0%</td>
<td align="right">12</td>
<td align="right">0.0%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">1,417</td>
<td align="right">0.4%</td>
<td align="right">578</td>
<td align="right">0.2%</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">226,831</td>
<td align="right">70.3%</td>
<td align="right">141,168</td>
<td align="right">59.6%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">3,140</td>
<td align="right">1.0%</td>
<td align="right">2,043</td>
<td align="right">0.9%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">322,882</td>
<td align="right"></td>
<td align="right">236,852</td>
<td align="right"></td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">130,547</td>
<td align="right">40.4%</td>
<td align="right">123,316</td>
<td align="right">52.1%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">3,782,238,832</td>
<td align="right">990.6%</td>
<td align="right">3,716,298,368</td>
<td align="right">968.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">381,807,013</td>
<td align="right"></td>
<td align="right">383,555,820</td>
<td align="right"></td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">96,051</td>
<td align="right">29.7%</td>
<td align="right">95,684</td>
<td align="right">40.4%</td>
<td align="right">-0.4%</td>
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
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">57</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">216,969</td>
<td align="right">95.7%</td>
<td align="right">134,879</td>
<td align="right">95.5%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">226,831</td>
<td align="right"></td>
<td align="right">141,168</td>
<td align="right"></td>
<td align="right">-37.8%</td>
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
<td align="right">15,764</td>
<td align="right">6.9%</td>
<td align="right">14,397</td>
<td align="right">10.2%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">58,650</td>
<td align="right">25.9%</td>
<td align="right">38,496</td>
<td align="right">27.3%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">85,462</td>
<td align="right">37.7%</td>
<td align="right">53,542</td>
<td align="right">37.9%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">49,670</td>
<td align="right">21.9%</td>
<td align="right">27,320</td>
<td align="right">19.4%</td>
<td align="right">-45.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">16,923</td>
<td align="right">7.5%</td>
<td align="right">7,389</td>
<td align="right">5.2%</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">362</td>
<td align="right">0.2%</td>
<td align="right">24</td>
<td align="right">0.0%</td>
<td align="right">-93.4%</td>
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
<td align="right">1,669</td>
<td align="right">0.7%</td>
<td align="right">1,400</td>
<td align="right">1.0%</td>
<td align="right">-16.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">47,840</td>
<td align="right">21.1%</td>
<td align="right">29,844</td>
<td align="right">21.1%</td>
<td align="right">-37.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">47,965</td>
<td align="right">21.1%</td>
<td align="right">38,753</td>
<td align="right">27.5%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">90,031</td>
<td align="right">39.7%</td>
<td align="right">49,664</td>
<td align="right">35.2%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">27,130</td>
<td align="right">12.0%</td>
<td align="right">14,156</td>
<td align="right">10.0%</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">2,272</td>
<td align="right">1.0%</td>
<td align="right">1,039</td>
<td align="right">0.7%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">62</td>
<td align="right">0.0%</td>
<td align="right">23</td>
<td align="right">0.0%</td>
<td align="right">-62.9%</td>
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
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">23</td>
<td align="right">63</td>
<td align="right">173.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">19,349</td>
<td align="right">120</td>
<td align="right">-99.4%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">28,553</td>
<td align="right">567</td>
<td align="right">-98.0%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">82,931</td>
<td align="right">2,430</td>
<td align="right">-97.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">10,409</td>
<td align="right">347</td>
<td align="right">-96.7%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">38,144</td>
<td align="right">1,743</td>
<td align="right">-95.4%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">2,294</td>
<td align="right">145</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">8,874</td>
<td align="right">580</td>
<td align="right">-93.5%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">1,725</td>
<td align="right">120</td>
<td align="right">-93.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">33,107</td>
<td align="right">2,476</td>
<td align="right">-92.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">2,499</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">29,507</td>
<td align="right">2,499</td>
<td align="right">-91.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">65,078</td>
<td align="right">6,025</td>
<td align="right">-90.7%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">36,304</td>
<td align="right">3,549</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">11,589</td>
<td align="right">1,181</td>
<td align="right">-89.8%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">3,364,035</td>
<td align="right">6,155,811</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">13,156</td>
<td align="right">4,284</td>
<td align="right">-67.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">4,378,135</td>
<td align="right">7,261,352</td>
<td align="right">65.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">42,870</td>
<td align="right">15,100</td>
<td align="right">-64.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">18,223</td>
<td align="right">6,656</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">2,798,849</td>
<td align="right">4,552,203</td>
<td align="right">62.6%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">48,150</td>
<td align="right">19,931</td>
<td align="right">-58.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">8,034,102</td>
<td align="right">3,497,129</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">3,892</td>
<td align="right">1,872</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">399,491</td>
<td align="right">590,649</td>
<td align="right">47.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">20,218,840</td>
<td align="right">10,713,126</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">338,690</td>
<td align="right">468,655</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">3,790,590</td>
<td align="right">2,425,504</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">27,834,373</td>
<td align="right">19,133,780</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">26,299,656</td>
<td align="right">18,337,453</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">29,438,819</td>
<td align="right">20,529,823</td>
<td align="right">-30.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">243,478</td>
<td align="right">171,178</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">3,083,555</td>
<td align="right">3,976,501</td>
<td align="right">29.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">110,734</td>
<td align="right">141,990</td>
<td align="right">28.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">7,846</td>
<td align="right">9,994</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">25,548,654</td>
<td align="right">18,676,625</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">11,017</td>
<td align="right">8,091</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">61,524</td>
<td align="right">45,876</td>
<td align="right">-25.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">183,673</td>
<td align="right">137,653</td>
<td align="right">-25.1%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">81,073</td>
<td align="right">60,944</td>
<td align="right">-24.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">1,248,408</td>
<td align="right">1,557,134</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">199,690</td>
<td align="right">150,947</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">59,901</td>
<td align="right">45,294</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">367,950</td>
<td align="right">279,490</td>
<td align="right">-24.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">227,114</td>
<td align="right">177,834</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">70,256</td>
<td align="right">56,600</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">74,724</td>
<td align="right">60,489</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">2,596,603</td>
<td align="right">3,040,629</td>
<td align="right">17.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">4,415,228</td>
<td align="right">5,157,741</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">80,768,450</td>
<td align="right">68,132,638</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">806,378</td>
<td align="right">685,533</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">805,809</td>
<td align="right">685,213</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">2,861,607</td>
<td align="right">3,268,725</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">109,167</td>
<td align="right">94,061</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">2,706</td>
<td align="right">2,338</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">184</td>
<td align="right">160</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">76,827,599</td>
<td align="right">67,583,825</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">1,931,863</td>
<td align="right">1,718,598</td>
<td align="right">-11.0%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">685,877</td>
<td align="right">617,425</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">685,877</td>
<td align="right">617,425</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">1,985,010</td>
<td align="right">1,788,653</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">350,644</td>
<td align="right">316,030</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">5,135,488</td>
<td align="right">5,609,651</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">1,418,512</td>
<td align="right">1,287,972</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">1,360,237</td>
<td align="right">1,245,128</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">136,731</td>
<td align="right">125,411</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">136,731</td>
<td align="right">125,411</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">577,797</td>
<td align="right">533,597</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">25,240,742</td>
<td align="right">23,396,157</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">508,256</td>
<td align="right">471,259</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">1,697,833</td>
<td align="right">1,574,834</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">1,697,833</td>
<td align="right">1,574,834</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">301,494</td>
<td align="right">279,793</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">1,570,861</td>
<td align="right">1,461,247</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">20,465,527</td>
<td align="right">21,878,691</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">42,373,306</td>
<td align="right">45,187,851</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,552,252</td>
<td align="right">1,453,780</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">812,208</td>
<td align="right">763,398</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">2,647,066</td>
<td align="right">2,491,148</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">8,974,679</td>
<td align="right">8,448,348</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">8,496,142</td>
<td align="right">8,007,539</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">2,055,972</td>
<td align="right">1,939,439</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">1,482,938</td>
<td align="right">1,398,894</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">331,565</td>
<td align="right">313,130</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">3,075,531</td>
<td align="right">2,911,565</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,881,893</td>
<td align="right">2,731,004</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">927,934</td>
<td align="right">975,803</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">12,352,080</td>
<td align="right">12,970,807</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">179,086</td>
<td align="right">170,275</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">1,256,157</td>
<td align="right">1,194,645</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">2,306,693</td>
<td align="right">2,193,796</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">25,290,082</td>
<td align="right">24,077,503</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">25,317,460</td>
<td align="right">24,141,429</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">69,471,861</td>
<td align="right">72,663,579</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">5,569,576</td>
<td align="right">5,810,772</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">13,247,026</td>
<td align="right">13,812,039</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">7,426,075</td>
<td align="right">7,118,161</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">6,543,734</td>
<td align="right">6,274,515</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">3,656,154</td>
<td align="right">3,508,317</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,606,201</td>
<td align="right">1,543,202</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">1,080,484</td>
<td align="right">1,120,601</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">79,598</td>
<td align="right">82,548</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">1,070,977</td>
<td align="right">1,032,703</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">996,520</td>
<td align="right">961,861</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">78,468,608</td>
<td align="right">75,773,249</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">92,482,800</td>
<td align="right">95,639,354</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">158,407</td>
<td align="right">163,778</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">158,407</td>
<td align="right">163,778</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">4,890,977</td>
<td align="right">4,725,807</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">1,970,957</td>
<td align="right">1,907,370</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">3,696,776</td>
<td align="right">3,582,599</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">3,696,776</td>
<td align="right">3,582,599</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">11,730,303</td>
<td align="right">11,372,357</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">17,568,117</td>
<td align="right">18,087,298</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">221,999,338</td>
<td align="right">215,598,377</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">65,479,644</td>
<td align="right">67,315,765</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">11,199,471</td>
<td align="right">10,888,195</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">552,782</td>
<td align="right">538,126</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">2,287,410</td>
<td align="right">2,227,519</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">1,488,939</td>
<td align="right">1,453,299</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">11,849,314</td>
<td align="right">11,568,385</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">2,877,899</td>
<td align="right">2,812,241</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">2,744,093</td>
<td align="right">2,683,727</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">44,347,395</td>
<td align="right">43,394,659</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">53,933,723</td>
<td align="right">55,065,178</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">970,407</td>
<td align="right">990,013</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">13,803,207</td>
<td align="right">13,527,359</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">713,903</td>
<td align="right">727,713</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">48,828,975</td>
<td align="right">47,898,585</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">66,853,408</td>
<td align="right">65,641,537</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">304,762,763</td>
<td align="right">299,762,611</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">3,142,392</td>
<td align="right">3,094,012</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">3,142,392</td>
<td align="right">3,094,012</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">15,499,798</td>
<td align="right">15,261,886</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">14,961</td>
<td align="right">14,742</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">14,961</td>
<td align="right">14,742</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">2,685,901</td>
<td align="right">2,648,700</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">177,328,176</td>
<td align="right">179,614,399</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">57,330</td>
<td align="right">58,048</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">5,149,080</td>
<td align="right">5,087,637</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">10,385,638</td>
<td align="right">10,265,371</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">1,440,188</td>
<td align="right">1,423,585</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">34,329,140</td>
<td align="right">33,953,372</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">304,648,108</td>
<td align="right">307,945,236</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">21,768,719</td>
<td align="right">21,558,837</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">38,819,012</td>
<td align="right">39,149,719</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">188,426</td>
<td align="right">186,862</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">759,294</td>
<td align="right">765,567</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">5,547,110</td>
<td align="right">5,503,212</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">12,875,895</td>
<td align="right">12,959,723</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">8,505,108</td>
<td align="right">8,558,433</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">30,013,494</td>
<td align="right">29,829,052</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">5,115,637</td>
<td align="right">5,085,222</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">73,088,878</td>
<td align="right">72,718,735</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">10,701,502</td>
<td align="right">10,652,441</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">381,807,013</td>
<td align="right">383,555,820</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">3,099,634</td>
<td align="right">3,085,924</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">73,029,625</td>
<td align="right">72,716,425</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">47,146,425</td>
<td align="right">46,962,335</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">3,058,750</td>
<td align="right">3,047,183</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">393,537,316</td>
<td align="right">394,928,177</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">16,930</td>
<td align="right">16,872</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">78,196,146</td>
<td align="right">77,937,287</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">815,013</td>
<td align="right">812,610</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">119,707,061</td>
<td align="right">119,368,400</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">41,380,994</td>
<td align="right">41,267,319</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">2,521,442</td>
<td align="right">2,514,711</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">14,938,044</td>
<td align="right">14,901,705</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">458,887</td>
<td align="right">457,852</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">5,505,775</td>
<td align="right">5,493,716</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">38,400,290</td>
<td align="right">38,343,862</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">41,324,126</td>
<td align="right">41,265,009</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">4,770,715</td>
<td align="right">4,767,321</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">50,466,053</td>
<td align="right">50,454,754</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">82,615</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">29,298</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">19,984</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,403</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">10,295</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">7,195</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">5,230</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">3,071</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_FORMAT_WITH_SPEC</td>
<td align="right">2,417</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">1,886</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">1,483</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">1,336</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">1,284</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">1,284</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">904</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">608</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">147</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">7</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right"></td>
<td align="right">120</td>
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
<td align="left">RAISE_VARARGS</td>
<td align="right">127</td>
<td align="right">42</td>
<td align="right">-66.9%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">4,402</td>
<td align="right">3,801</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">1,301</td>
<td align="right">1,172</td>
<td align="right">-9.9%</td>
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
<td align="right">8</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">8</td>
<td align="right">0</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">
set class
<details>
<summary>ⓘ</summary>

Setting an object's class, `obj.__class__ = ...`
</details>
</td>
<td align="right">22,592</td>
<td align="right">22,592</td>
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
<td align="right">23</td>
<td align="right">23</td>
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
<td align="right">24</td>
<td align="right">24</td>
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
<td align="right">21</td>
<td align="right">21</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-12
