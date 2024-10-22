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
<td align="right">2,909,462</td>
<td align="right">1,507,280,132</td>
<td align="right">51,706.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">190,044,005</td>
<td align="right">1,483,128,972</td>
<td align="right">680.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">183,125,612</td>
<td align="right">956,840,163</td>
<td align="right">422.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,974,554</td>
<td align="right">1,148,547,019</td>
<td align="right">419.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">234,813,526</td>
<td align="right">1,164,529,036</td>
<td align="right">395.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">200,095,054</td>
<td align="right">963,506,479</td>
<td align="right">381.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,990,635</td>
<td align="right">435,828,077</td>
<td align="right">319.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,938,141</td>
<td align="right">1,283,340,294</td>
<td align="right">260.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,470</td>
<td align="right">549,250</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,459,180</td>
<td align="right">469,698,711</td>
<td align="right">198.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">701,218,455</td>
<td align="right">1,614,600,588</td>
<td align="right">130.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">759,398,097</td>
<td align="right">1,714,759,567</td>
<td align="right">125.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">815,474,522</td>
<td align="right">1,746,514,404</td>
<td align="right">114.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">475,655,280</td>
<td align="right">917,385,585</td>
<td align="right">92.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">272,019,897</td>
<td align="right">520,331,088</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">615,786,142</td>
<td align="right">1,116,951,166</td>
<td align="right">81.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,733,827,432</td>
<td align="right">8,505,560,300</td>
<td align="right">79.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,849,720,986</td>
<td align="right">3,194,718,767</td>
<td align="right">72.7%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">473,374,602</td>
<td align="right">803,618,200</td>
<td align="right">69.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">722,472,588</td>
<td align="right">1,222,107,086</td>
<td align="right">69.2%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,537,983</td>
<td align="right">12,206,143</td>
<td align="right">61.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,095,714</td>
<td align="right">50,119,157</td>
<td align="right">51.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">49,557,480</td>
<td align="right">74,958,981</td>
<td align="right">51.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">43,000,542</td>
<td align="right">60,287,356</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">10,355,103</td>
<td align="right">6,354,483</td>
<td align="right">-38.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">653,029,424</td>
<td align="right">902,268,849</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,999,788,838</td>
<td align="right">6,901,357,594</td>
<td align="right">38.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,977,389,991</td>
<td align="right">5,298,392,228</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,070,303,787</td>
<td align="right">5,391,920,203</td>
<td align="right">32.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">815,652,763</td>
<td align="right">1,064,913,477</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,668,303,672</td>
<td align="right">21,693,678,152</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,633,791</td>
<td align="right">135,045,330</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,813,638,313</td>
<td align="right">2,269,900,173</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,019,797</td>
<td align="right">28,327,407</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">298,017,155</td>
<td align="right">268,367,298</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">352,854,405</td>
<td align="right">381,452,953</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,299,732</td>
<td align="right">87,745,626</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">200,997,085</td>
<td align="right">185,388,581</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">824,988,488</td>
<td align="right">882,741,633</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,211,795,242</td>
<td align="right">1,288,722,964</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">337,331,987</td>
<td align="right">358,723,533</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,934,664</td>
<td align="right">259,506,561</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">188,157,355</td>
<td align="right">199,941,515</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,626,205</td>
<td align="right">36,475,001</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">217,872,327</td>
<td align="right">229,329,144</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,104,889</td>
<td align="right">108,400,654</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,163,061</td>
<td align="right">50,448,126</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">673,020,400</td>
<td align="right">706,853,501</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,322,291</td>
<td align="right">49,530,678</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,583,465,046</td>
<td align="right">2,698,532,772</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">226,513,310</td>
<td align="right">235,122,306</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,114,160,401</td>
<td align="right">2,187,960,428</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,798,587</td>
<td align="right">20,435,494</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,562,273</td>
<td align="right">36,376,396</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,011,843</td>
<td align="right">126,618,078</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">104,701,577</td>
<td align="right">101,721,899</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">536,292,465</td>
<td align="right">551,355,296</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,611,430</td>
<td align="right">55,099,964</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">384,699,700</td>
<td align="right">394,692,123</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,683,284</td>
<td align="right">3,595,625</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,152,214</td>
<td align="right">200,691,796</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">89,541,404</td>
<td align="right">91,578,954</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">318,781,106</td>
<td align="right">326,006,067</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,110,476</td>
<td align="right">330,548,564</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">762,767,785</td>
<td align="right">777,297,312</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,372,225,017</td>
<td align="right">1,346,317,508</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">459,640,765</td>
<td align="right">468,253,253</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">57,073,569</td>
<td align="right">58,093,742</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,087,538</td>
<td align="right">138,353,058</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,018,411</td>
<td align="right">44,733,752</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,115,409</td>
<td align="right">145,390,489</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">537,575,277</td>
<td align="right">545,671,834</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">164,405,782</td>
<td align="right">162,097,197</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">53,672,758</td>
<td align="right">52,926,886</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,194,644</td>
<td align="right">118,809,039</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">124,175,638</td>
<td align="right">125,878,252</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">166,159,989</td>
<td align="right">168,433,583</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,916,962,624</td>
<td align="right">4,982,935,112</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">200,763,239</td>
<td align="right">203,427,844</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,730,793</td>
<td align="right">72,623,413</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">271,432,063</td>
<td align="right">274,783,981</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,421,572</td>
<td align="right">301,862,132</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,050,474,973</td>
<td align="right">1,062,508,669</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,900,627,023</td>
<td align="right">2,931,984,561</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,817,128</td>
<td align="right">135,237,982</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">395,237,789</td>
<td align="right">399,040,914</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,828,927</td>
<td align="right">53,315,877</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,785,019</td>
<td align="right">9,874,090</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">714,366,374</td>
<td align="right">720,499,269</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,728</td>
<td align="right">3,557,439</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,848,771</td>
<td align="right">8,911,345</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,456,004</td>
<td align="right">142,386,934</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">988,954,246</td>
<td align="right">982,472,397</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">93,244,615</td>
<td align="right">93,789,602</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">492,950,412</td>
<td align="right">490,122,970</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,755,659,301</td>
<td align="right">2,739,999,242</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,542,233</td>
<td align="right">8,590,449</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,745,930</td>
<td align="right">49,002,480</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,226,283</td>
<td align="right">58,496,898</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,948,114</td>
<td align="right">71,270,070</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,035,022</td>
<td align="right">83,406,985</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,251</td>
<td align="right">2,904,385</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,266,477</td>
<td align="right">33,390,642</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,767,379,646</td>
<td align="right">3,753,447,805</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">14,953,154</td>
<td align="right">14,899,050</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,269,937,486</td>
<td align="right">2,261,964,783</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,842,259,940</td>
<td align="right">1,848,146,866</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,745</td>
<td align="right">92,156,956</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">894,827,921</td>
<td align="right">897,638,334</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,499,373</td>
<td align="right">4,513,076</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,198,924</td>
<td align="right">56,365,415</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,291,616</td>
<td align="right">16,249,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,676</td>
<td align="right">43,558,890</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,530,857</td>
<td align="right">47,649,405</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,418,362</td>
<td align="right">1,421,856</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,594,235</td>
<td align="right">10,618,830</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,582,949</td>
<td align="right">138,881,533</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,461,736</td>
<td align="right">82,303,403</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,264,386</td>
<td align="right">11,283,963</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,112,130</td>
<td align="right">22,143,173</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">314,076,328</td>
<td align="right">314,506,585</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">525,258</td>
<td align="right">524,601</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">72,107,719</td>
<td align="right">72,019,350</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,444,253</td>
<td align="right">198,245,365</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,311,178</td>
<td align="right">60,368,958</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">67,170,929</td>
<td align="right">67,227,642</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,057</td>
<td align="right">268,371,510</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,059,119</td>
<td align="right">91,117,885</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,399,826,873</td>
<td align="right">2,398,382,492</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">224,002</td>
<td align="right">224,112</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,772,041</td>
<td align="right">57,799,407</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,193,755</td>
<td align="right">150,259,380</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">339,327,738</td>
<td align="right">339,440,362</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,056,351,932</td>
<td align="right">1,056,615,466</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">246,817,263</td>
<td align="right">246,875,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,084,646</td>
<td align="right">21,080,359</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,398,958</td>
<td align="right">21,394,903</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">493,224,734</td>
<td align="right">493,134,380</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,390,617</td>
<td align="right">21,394,422</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">340,423,809</td>
<td align="right">340,484,210</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,584,887</td>
<td align="right">402,526,365</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,165</td>
<td align="right">15,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,994,963</td>
<td align="right">10,996,346</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,229,934</td>
<td align="right">107,217,981</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">365,476,410</td>
<td align="right">365,505,199</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">719,224</td>
<td align="right">719,268</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231,625,481</td>
<td align="right">231,612,337</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,001,650</td>
<td align="right">147,009,974</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,660</td>
<td align="right">268,675</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,781</td>
<td align="right">225,022,300</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">98,856,320</td>
<td align="right">98,851,371</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">658,292</td>
<td align="right">658,312</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,116</td>
<td align="right">3,744,192</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,259</td>
<td align="right">5,830,301</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,751,430</td>
<td align="right">120,752,256</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,353,394</td>
<td align="right">20,353,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,169,346</td>
<td align="right">94,169,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">236,562,124</td>
<td align="right">236,562,140</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,062</td>
<td align="right">173,399,060</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,074</td>
<td align="right">402,104,071</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,887,371</td>
<td align="right">91,887,371</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_LINE</td>
<td align="right">77,693,920</td>
<td align="right">77,693,920</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RESUME</td>
<td align="right">38,846,240</td>
<td align="right">38,846,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_VALUE</td>
<td align="right">38,845,680</td>
<td align="right">38,845,680</td>
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
<td align="right">3,465,288</td>
<td align="right">3,465,288</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">719,420</td>
<td align="right">719,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">157,711</td>
<td align="right">157,711</td>
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
<td align="right">91,641</td>
<td align="right">91,641</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">58,580</td>
<td align="right">58,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">30,129</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">27,806</td>
<td align="right">27,806</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">21,856</td>
<td align="right">21,856</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">16,120</td>
<td align="right">16,120</td>
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
<td align="right">1,560</td>
<td align="right">1,560</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">1,062</td>
<td align="right">1,062</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_GLOBALS</td>
<td align="right">423</td>
<td align="right">423</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">241</td>
<td align="right">241</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_RETURN_CONST</td>
<td align="right">240</td>
<td align="right">240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">160</td>
<td align="right">160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">140</td>
<td align="right">140</td>
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
<td align="right">412,553,451</td>
<td align="right">4.2%</td>
<td align="right">422,542,422</td>
<td align="right">4.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,395,553,379</td>
<td align="right">95.8%</td>
<td align="right">9,395,522,262</td>
<td align="right">95.7%</td>
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
<td align="right">29,575,090</td>
<td align="right">0.3%</td>
<td align="right">29,575,090</td>
<td align="right">0.3%</td>
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
<td align="right">1,121,563</td>
<td align="right">65.2%</td>
<td align="right">1,124,974</td>
<td align="right">65.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">599,776</td>
<td align="right">34.8%</td>
<td align="right">599,817</td>
<td align="right">34.8%</td>
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
<td align="left">remainder</td>
<td align="right">20,360</td>
<td align="right">1.8%</td>
<td align="right">23,179</td>
<td align="right">2.1%</td>
<td align="right">13.8%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,875</td>
<td align="right">4.4%</td>
<td align="right">49,095</td>
<td align="right">4.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,803</td>
<td align="right">1.0%</td>
<td align="right">10,844</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,580</td>
<td align="right">1.3%</td>
<td align="right">14,631</td>
<td align="right">1.3%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,919</td>
<td align="right">7.4%</td>
<td align="right">83,105</td>
<td align="right">7.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,605</td>
<td align="right">0.5%</td>
<td align="right">5,613</td>
<td align="right">0.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,342</td>
<td align="right">2.8%</td>
<td align="right">31,386</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">836</td>
<td align="right">0.1%</td>
<td align="right">835</td>
<td align="right">0.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,350</td>
<td align="right">4.4%</td>
<td align="right">49,378</td>
<td align="right">4.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,247</td>
<td align="right">0.7%</td>
<td align="right">8,250</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,962</td>
<td align="right">0.3%</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,311</td>
<td align="right">2.8%</td>
<td align="right">31,320</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,468</td>
<td align="right">0.8%</td>
<td align="right">8,470</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">4,728</td>
<td align="right">0.4%</td>
<td align="right">4,729</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">6,803</td>
<td align="right">0.6%</td>
<td align="right">6,804</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,611</td>
<td align="right">69.7%</td>
<td align="right">781,609</td>
<td align="right">69.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">9,742</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">2,620</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">401</td>
<td align="right">0.0%</td>
<td align="right">401</td>
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
<td align="right">657,418,254</td>
<td align="right">9.6%</td>
<td align="right">906,609,040</td>
<td align="right">12.8%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,202,014,676</td>
<td align="right">90.4%</td>
<td align="right">6,182,872,975</td>
<td align="right">87.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,347</td>
<td align="right">0.1%</td>
<td align="right">4,803,594</td>
<td align="right">0.1%</td>
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
<td align="right">221,965</td>
<td align="right">55.0%</td>
<td align="right">281,625</td>
<td align="right">60.8%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,552</td>
<td align="right">45.0%</td>
<td align="right">181,778</td>
<td align="right">39.2%</td>
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
<td align="left">other</td>
<td align="right">109,084</td>
<td align="right">49.1%</td>
<td align="right">169,787</td>
<td align="right">60.3%</td>
<td align="right">55.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">940</td>
<td align="right">0.4%</td>
<td align="right">980</td>
<td align="right">0.3%</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">58,326</td>
<td align="right">26.3%</td>
<td align="right">57,206</td>
<td align="right">20.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">123</td>
<td align="right">0.1%</td>
<td align="right">124</td>
<td align="right">0.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,332</td>
<td align="right">9.6%</td>
<td align="right">21,368</td>
<td align="right">7.6%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">26,640</td>
<td align="right">12.0%</td>
<td align="right">26,640</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">4,300</td>
<td align="right">1.9%</td>
<td align="right">4,300</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">800</td>
<td align="right">0.4%</td>
<td align="right">800</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">320</td>
<td align="right">0.1%</td>
<td align="right">320</td>
<td align="right">0.1%</td>
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
<td align="right">151,023,689</td>
<td align="right">1.1%</td>
<td align="right">157,096,436</td>
<td align="right">1.1%</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">640,705,632</td>
<td align="right">4.5%</td>
<td align="right">646,573,477</td>
<td align="right">4.6%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">13,489,690,188</td>
<td align="right">95.4%</td>
<td align="right">13,448,497,030</td>
<td align="right">95.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,002</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
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
<td align="right">3,375,183</td>
<td align="right">95.3%</td>
<td align="right">3,489,773</td>
<td align="right">95.4%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,608</td>
<td align="right">4.7%</td>
<td align="right">167,566</td>
<td align="right">4.6%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">156,755</td>
<td align="right">93.5%</td>
<td align="right">156,713</td>
<td align="right">93.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">wrong number arguments</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">10,490</td>
<td align="right">6.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">2,989</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not simple</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">2,003</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">921</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">363</td>
<td align="right">0.2%</td>
<td align="right">363</td>
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
<td align="right">105,073,658</td>
<td align="right">1.8%</td>
<td align="right">436,806,947</td>
<td align="right">7.1%</td>
<td align="right">315.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,327,228</td>
<td align="right">0.0%</td>
<td align="right">1,303,002</td>
<td align="right">0.0%</td>
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
<td align="right">5,722,183,275</td>
<td align="right">98.2%</td>
<td align="right">5,722,054,569</td>
<td align="right">92.9%</td>
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
<td align="right">164,488</td>
<td align="right">67.4%</td>
<td align="right">244,838</td>
<td align="right">75.5%</td>
<td align="right">48.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">79,717</td>
<td align="right">32.6%</td>
<td align="right">79,294</td>
<td align="right">24.5%</td>
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
<td align="left">tuple</td>
<td align="right">12,200</td>
<td align="right">7.4%</td>
<td align="right">93,034</td>
<td align="right">38.0%</td>
<td align="right">662.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,550</td>
<td align="right">0.9%</td>
<td align="right">1,452</td>
<td align="right">0.6%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,452</td>
<td align="right">29.5%</td>
<td align="right">47,811</td>
<td align="right">19.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,429</td>
<td align="right">11.8%</td>
<td align="right">19,589</td>
<td align="right">8.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,434</td>
<td align="right">10.6%</td>
<td align="right">17,481</td>
<td align="right">7.1%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">32,982</td>
<td align="right">20.1%</td>
<td align="right">33,022</td>
<td align="right">13.5%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,531</td>
<td align="right">8.8%</td>
<td align="right">14,539</td>
<td align="right">5.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">10,680</td>
<td align="right">6.5%</td>
<td align="right">10,680</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">3,060</td>
<td align="right">1.9%</td>
<td align="right">3,060</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,720</td>
<td align="right">1.7%</td>
<td align="right">2,720</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">960</td>
<td align="right">0.6%</td>
<td align="right">960</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">490</td>
<td align="right">0.3%</td>
<td align="right">490</td>
<td align="right">0.2%</td>
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
<td align="right">51,965,780</td>
<td align="right">2.0%</td>
<td align="right">77,360,334</td>
<td align="right">3.0%</td>
<td align="right">48.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,776,001</td>
<td align="right">97.9%</td>
<td align="right">2,484,631,858</td>
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
<td align="right">2,546,180</td>
<td align="right">0.1%</td>
<td align="right">2,546,180</td>
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
<td align="right">76,741</td>
<td align="right">55.7%</td>
<td align="right">83,688</td>
<td align="right">57.8%</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">61,139</td>
<td align="right">44.3%</td>
<td align="right">61,139</td>
<td align="right">42.2%</td>
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
<td align="right">19,502</td>
<td align="right">25.4%</td>
<td align="right">25,102</td>
<td align="right">30.0%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,470</td>
<td align="right">18.9%</td>
<td align="right">15,230</td>
<td align="right">18.2%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,572</td>
<td align="right">35.9%</td>
<td align="right">28,295</td>
<td align="right">33.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,197</td>
<td align="right">19.8%</td>
<td align="right">15,061</td>
<td align="right">18.0%</td>
<td align="right">-0.9%</td>
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
<td align="right">6,745,311</td>
<td align="right">0.6%</td>
<td align="right">37,434,528</td>
<td align="right">1.7%</td>
<td align="right">455.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">565,065,112</td>
<td align="right">53.9%</td>
<td align="right">1,302,530,554</td>
<td align="right">57.7%</td>
<td align="right">130.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">482,026,002</td>
<td align="right">46.0%</td>
<td align="right">953,757,559</td>
<td align="right">42.3%</td>
<td align="right">97.9%</td>
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
<td align="right">175,673</td>
<td align="right">46.9%</td>
<td align="right">754,746</td>
<td align="right">71.0%</td>
<td align="right">329.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,916</td>
<td align="right">53.1%</td>
<td align="right">307,808</td>
<td align="right">29.0%</td>
<td align="right">54.7%</td>
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
<td align="right">620</td>
<td align="right">0.3%</td>
<td align="right">1,274</td>
<td align="right">0.4%</td>
<td align="right">105.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,982</td>
<td align="right">52.8%</td>
<td align="right">206,322</td>
<td align="right">67.0%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">2.5%</td>
<td align="right">7,976</td>
<td align="right">2.6%</td>
<td align="right">60.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">4,661</td>
<td align="right">2.3%</td>
<td align="right">6,260</td>
<td align="right">2.0%</td>
<td align="right">34.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,078</td>
<td align="right">5.6%</td>
<td align="right">12,262</td>
<td align="right">4.0%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">3.3%</td>
<td align="right">6,105</td>
<td align="right">2.0%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,354</td>
<td align="right">5.7%</td>
<td align="right">12,138</td>
<td align="right">3.9%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,510</td>
<td align="right">18.4%</td>
<td align="right">37,261</td>
<td align="right">12.1%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">2,744</td>
<td align="right">1.4%</td>
<td align="right">2,764</td>
<td align="right">0.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">6,737</td>
<td align="right">3.4%</td>
<td align="right">6,737</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">5,202</td>
<td align="right">2.6%</td>
<td align="right">5,202</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">2,467</td>
<td align="right">1.2%</td>
<td align="right">2,467</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">740</td>
<td align="right">0.4%</td>
<td align="right">740</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">280</td>
<td align="right">0.1%</td>
<td align="right">280</td>
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
<td align="right">304,212,637</td>
<td align="right">1.9%</td>
<td align="right">434,121,879</td>
<td align="right">2.7%</td>
<td align="right">42.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">970,016,224</td>
<td align="right">6.0%</td>
<td align="right">1,130,268,737</td>
<td align="right">7.0%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,088,529,966</td>
<td align="right">93.9%</td>
<td align="right">15,084,040,678</td>
<td align="right">93.0%</td>
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
<td align="right">303,840</td>
<td align="right">0.0%</td>
<td align="right">303,840</td>
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
<td align="right">863,447</td>
<td align="right">12.0%</td>
<td align="right">1,902,560</td>
<td align="right">17.8%</td>
<td align="right">120.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,353,366</td>
<td align="right">88.0%</td>
<td align="right">8,804,083</td>
<td align="right">82.2%</td>
<td align="right">38.6%</td>
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
<td align="left">out of versions</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">2,000.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">159,366</td>
<td align="right">18.5%</td>
<td align="right">682,299</td>
<td align="right">35.9%</td>
<td align="right">328.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">155,979</td>
<td align="right">18.1%</td>
<td align="right">663,486</td>
<td align="right">34.9%</td>
<td align="right">325.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">17,509</td>
<td align="right">2.0%</td>
<td align="right">16,449</td>
<td align="right">0.9%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,638</td>
<td align="right">10.4%</td>
<td align="right">93,553</td>
<td align="right">4.9%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,425</td>
<td align="right">0.6%</td>
<td align="right">5,545</td>
<td align="right">0.3%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">176,740</td>
<td align="right">20.5%</td>
<td align="right">180,140</td>
<td align="right">9.5%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,293</td>
<td align="right">2.4%</td>
<td align="right">20,634</td>
<td align="right">1.1%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">2,543</td>
<td align="right">0.3%</td>
<td align="right">2,582</td>
<td align="right">0.1%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">2,964</td>
<td align="right">0.3%</td>
<td align="right">3,004</td>
<td align="right">0.2%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">17,651</td>
<td align="right">2.0%</td>
<td align="right">17,873</td>
<td align="right">0.9%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">class attr descriptor</td>
<td align="right">26,300</td>
<td align="right">3.0%</td>
<td align="right">26,600</td>
<td align="right">1.4%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">15,622</td>
<td align="right">1.8%</td>
<td align="right">15,742</td>
<td align="right">0.8%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">78,398</td>
<td align="right">9.1%</td>
<td align="right">78,888</td>
<td align="right">4.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,458</td>
<td align="right">10.1%</td>
<td align="right">87,814</td>
<td align="right">4.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,759</td>
<td align="right">0.7%</td>
<td align="right">5,749</td>
<td align="right">0.3%</td>
<td align="right">-0.2%</td>
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
<tr>
<td align="left">property</td>
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
<td align="right">4,844,647,894</td>
<td align="right">99.6%</td>
<td align="right">6,172,362,208</td>
<td align="right">99.7%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">391,983</td>
<td align="right">0.0%</td>
<td align="right">393,029</td>
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
<td align="right">20,279,854</td>
<td align="right">0.4%</td>
<td align="right">20,280,946</td>
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
<td align="right">9,236</td>
<td align="right">0.0%</td>
<td align="right">9,236</td>
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
<td align="right">465,523</td>
<td align="right">100.0%</td>
<td align="right">465,577</td>
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
<td align="right">86,248,195</td>
<td align="right">100.0%</td>
<td align="right">86,159,902</td>
<td align="right">100.0%</td>
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
<td align="right">7,624</td>
<td align="right">0.0%</td>
<td align="right">7,626</td>
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
<td align="right">7,541</td>
<td align="right">100.0%</td>
<td align="right">7,541</td>
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
<td align="right">786,232,534</td>
<td align="right">81.9%</td>
<td align="right">786,232,625</td>
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
<td align="right">173,364,414</td>
<td align="right">18.1%</td>
<td align="right">173,364,412</td>
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
<td align="right">30,643</td>
<td align="right">0.0%</td>
<td align="right">30,643</td>
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
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">5,557</td>
<td align="right">8.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
<td align="right">59,734</td>
<td align="right">91.5%</td>
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
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">14,268</td>
<td align="right">23.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
<td align="right">10,020</td>
<td align="right">16.8%</td>
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
<tr>
<td align="left">dict keys</td>
<td align="right">6</td>
<td align="right">0.0%</td>
<td align="right">6</td>
<td align="right">0.0%</td>
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
<td align="right">110,195,653</td>
<td align="right">4.2%</td>
<td align="right">113,561,397</td>
<td align="right">4.3%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">160,755,132</td>
<td align="right">6.1%</td>
<td align="right">164,543,959</td>
<td align="right">6.3%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,455,709,347</td>
<td align="right">93.8%</td>
<td align="right">2,454,613,354</td>
<td align="right">93.6%</td>
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
<td align="right">2,176,921</td>
<td align="right">95.9%</td>
<td align="right">2,240,446</td>
<td align="right">96.0%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,527</td>
<td align="right">4.1%</td>
<td align="right">92,869</td>
<td align="right">4.0%</td>
<td align="right">0.4%</td>
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
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">764</td>
<td align="right">0.8%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">31,964</td>
<td align="right">34.5%</td>
<td align="right">32,284</td>
<td align="right">34.8%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">5,075</td>
<td align="right">5.5%</td>
<td align="right">5,115</td>
<td align="right">5.5%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">6,419</td>
<td align="right">6.9%</td>
<td align="right">6,439</td>
<td align="right">6.9%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,772</td>
<td align="right">10.6%</td>
<td align="right">9,774</td>
<td align="right">10.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">8,663</td>
<td align="right">9.4%</td>
<td align="right">8,663</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,505</td>
<td align="right">8.1%</td>
<td align="right">7,505</td>
<td align="right">8.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">5,003</td>
<td align="right">5.4%</td>
<td align="right">5,003</td>
<td align="right">5.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">3,185</td>
<td align="right">3.4%</td>
<td align="right">3,185</td>
<td align="right">3.4%</td>
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
<td align="right">271,898,824</td>
<td align="right">23.7%</td>
<td align="right">520,149,175</td>
<td align="right">37.3%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">875,328,194</td>
<td align="right">76.3%</td>
<td align="right">873,501,654</td>
<td align="right">62.7%</td>
<td align="right">-0.2%</td>
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
<td align="right">110,604</td>
<td align="right">89.2%</td>
<td align="right">171,442</td>
<td align="right">92.8%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,369</td>
<td align="right">10.8%</td>
<td align="right">13,371</td>
<td align="right">7.2%</td>
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
<td align="right">43,420</td>
<td align="right">39.3%</td>
<td align="right">104,040</td>
<td align="right">60.7%</td>
<td align="right">139.6%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,580</td>
<td align="right">0.9%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">1,520</td>
<td align="right">1.4%</td>
<td align="right">1,580</td>
<td align="right">0.9%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">7,661</td>
<td align="right">6.9%</td>
<td align="right">7,739</td>
<td align="right">4.5%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">42,203</td>
<td align="right">38.2%</td>
<td align="right">42,223</td>
<td align="right">24.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">14,280</td>
<td align="right">12.9%</td>
<td align="right">14,280</td>
<td align="right">8.3%</td>
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
<td align="right">24,998,357</td>
<td align="right">0.4%</td>
<td align="right">30,856,494</td>
<td align="right">0.5%</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">188,487,212</td>
<td align="right">3.2%</td>
<td align="right">191,915,497</td>
<td align="right">3.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,754,886,157</td>
<td align="right">96.8%</td>
<td align="right">5,757,044,039</td>
<td align="right">96.8%</td>
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
<td align="right">664,538</td>
<td align="right">72.5%</td>
<td align="right">775,094</td>
<td align="right">74.7%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">252,389</td>
<td align="right">27.5%</td>
<td align="right">263,100</td>
<td align="right">25.3%</td>
<td align="right">4.2%</td>
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
<td align="right">37,241</td>
<td align="right">14.8%</td>
<td align="right">46,611</td>
<td align="right">17.7%</td>
<td align="right">25.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,994</td>
<td align="right">2.4%</td>
<td align="right">6,082</td>
<td align="right">2.3%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,188</td>
<td align="right">9.6%</td>
<td align="right">24,510</td>
<td align="right">9.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,125</td>
<td align="right">6.8%</td>
<td align="right">16,905</td>
<td align="right">6.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,214</td>
<td align="right">33.0%</td>
<td align="right">84,170</td>
<td align="right">32.0%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,973</td>
<td align="right">2.8%</td>
<td align="right">7,044</td>
<td align="right">2.7%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">54,874</td>
<td align="right">21.7%</td>
<td align="right">54,994</td>
<td align="right">20.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,888</td>
<td align="right">7.9%</td>
<td align="right">19,892</td>
<td align="right">7.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">1,749</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">723</td>
<td align="right">0.3%</td>
<td align="right">723</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">3,080</td>
<td align="right">0.0%</td>
<td align="right">4,240</td>
<td align="right">0.0%</td>
<td align="right">37.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">194,700</td>
<td align="right">0.0%</td>
<td align="right">195,919</td>
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
<td align="right">1,529,703,445</td>
<td align="right">100.0%</td>
<td align="right">1,524,212,424</td>
<td align="right">100.0%</td>
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
<td align="right">30,519</td>
<td align="right">94.2%</td>
<td align="right">30,571</td>
<td align="right">94.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,863</td>
<td align="right">5.8%</td>
<td align="right">1,862</td>
<td align="right">5.7%</td>
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
<td align="right">1,216</td>
<td align="right">65.3%</td>
<td align="right">1,215</td>
<td align="right">65.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">380</td>
<td align="right">20.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">267</td>
<td align="right">14.3%</td>
<td align="right">267</td>
<td align="right">14.3%</td>
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
<td align="right">9,327,743,288</td>
<td align="right">9.5%</td>
<td align="right">12,765,770,894</td>
<td align="right">10.2%</td>
<td align="right">36.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,592,516,162</td>
<td align="right">33.3%</td>
<td align="right">41,913,566,437</td>
<td align="right">33.4%</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">636,052,247</td>
<td align="right">0.7%</td>
<td align="right">811,936,093</td>
<td align="right">0.6%</td>
<td align="right">27.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,219,796,621</td>
<td align="right">56.5%</td>
<td align="right">70,136,854,940</td>
<td align="right">55.8%</td>
<td align="right">27.0%</td>
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
<td align="left">COMPARE_OP</td>
<td align="right">105,073,658</td>
<td align="right">2.5%</td>
<td align="right">436,806,947</td>
<td align="right">7.7%</td>
<td align="right">315.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">482,026,002</td>
<td align="right">11.7%</td>
<td align="right">953,757,559</td>
<td align="right">16.9%</td>
<td align="right">97.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">271,898,824</td>
<td align="right">6.6%</td>
<td align="right">520,149,175</td>
<td align="right">9.2%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">657,418,254</td>
<td align="right">15.9%</td>
<td align="right">906,609,040</td>
<td align="right">16.1%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">970,016,224</td>
<td align="right">23.5%</td>
<td align="right">1,130,268,737</td>
<td align="right">20.0%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">412,553,451</td>
<td align="right">10.0%</td>
<td align="right">422,542,422</td>
<td align="right">7.5%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">160,755,132</td>
<td align="right">3.9%</td>
<td align="right">164,543,959</td>
<td align="right">2.9%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">188,487,212</td>
<td align="right">4.6%</td>
<td align="right">191,915,497</td>
<td align="right">3.4%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">640,705,632</td>
<td align="right">15.5%</td>
<td align="right">646,573,477</td>
<td align="right">11.5%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,364,414</td>
<td align="right">4.2%</td>
<td align="right">173,364,412</td>
<td align="right">3.1%</td>
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
<td align="right">67,368,390</td>
<td align="right">10.6%</td>
<td align="right">130,797,350</td>
<td align="right">16.1%</td>
<td align="right">94.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">129,872,490</td>
<td align="right">20.4%</td>
<td align="right">180,392,248</td>
<td align="right">22.2%</td>
<td align="right">38.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">37,898,202</td>
<td align="right">6.0%</td>
<td align="right">46,842,553</td>
<td align="right">5.8%</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,507,967</td>
<td align="right">5.6%</td>
<td align="right">39,587,511</td>
<td align="right">4.9%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,319,016</td>
<td align="right">13.6%</td>
<td align="right">89,680,676</td>
<td align="right">11.0%</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,516,299</td>
<td align="right">12.7%</td>
<td align="right">83,473,091</td>
<td align="right">10.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,852,971</td>
<td align="right">3.7%</td>
<td align="right">23,857,056</td>
<td align="right">2.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,352</td>
<td align="right">4.3%</td>
<td align="right">27,497,312</td>
<td align="right">3.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">20,177,240</td>
<td align="right">3.2%</td>
<td align="right">20,177,240</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">18,237,369</td>
<td align="right">2.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,806,831</td>
<td align="right">2.3%</td>
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
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,272</td>
<td align="right">0.1%</td>
<td align="right">2,658,112</td>
<td align="right">0.0%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">852,113,378</td>
<td align="right">10.1%</td>
<td align="right">846,815,777</td>
<td align="right">10.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,158,388,402</td>
<td align="right">73.0%</td>
<td align="right">6,124,435,020</td>
<td align="right">73.0%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,273,754,537</td>
<td align="right">27.0%</td>
<td align="right">2,265,752,871</td>
<td align="right">27.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,273,754,537</td>
<td align="right">27.0%</td>
<td align="right">2,265,752,871</td>
<td align="right">27.0%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,671,132,731</td>
<td align="right">79.1%</td>
<td align="right">6,655,274,986</td>
<td align="right">79.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,251,407</td>
<td align="right">4.0%</td>
<td align="right">333,585,800</td>
<td align="right">4.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,421,641,159</td>
<td align="right">16.9%</td>
<td align="right">1,418,937,094</td>
<td align="right">16.9%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,417,192,758</td>
<td align="right">16.8%</td>
<td align="right">1,416,248,853</td>
<td align="right">16.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,759,162</td>
<td align="right">1.0%</td>
<td align="right">84,719,211</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,645,102</td>
<td align="right">3.9%</td>
<td align="right">331,643,381</td>
<td align="right">4.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,756</td>
<td align="right">0.4%</td>
<td align="right">31,097,820</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,463</td>
<td align="right">2.1%</td>
<td align="right">175,480,168</td>
<td align="right">2.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,129</td>
<td align="right">0.0%</td>
<td align="right">30,129</td>
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
<td align="right">44,345,341,663</td>
<td align="right">44,345,341,663 / 0 !!</td>
<td align="right">53,188,476,888</td>
<td align="right">53,188,476,888 / 0 !!</td>
<td align="right">19.9%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">60,708,942,459</td>
<td align="right">60,708,942,459 / 0 !!</td>
<td align="right">70,174,823,317</td>
<td align="right">70,174,823,317 / 0 !!</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">94,032,332,119</td>
<td align="right">94,032,332,119 / 0 !!</td>
<td align="right">82,403,052,639</td>
<td align="right">82,403,052,639 / 0 !!</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">100,182,880,628</td>
<td align="right">100,182,880,628 / 0 !!</td>
<td align="right">87,909,070,839</td>
<td align="right">87,909,070,839 / 0 !!</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,656,654</td>
<td align="right"></td>
<td align="right">9,168,688</td>
<td align="right"></td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">63,176,590</td>
<td align="right"></td>
<td align="right">63,865,278</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,540,147,645</td>
<td align="right"></td>
<td align="right">2,518,041,882</td>
<td align="right"></td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,967,530</td>
<td align="right">0.4%</td>
<td align="right">93,637,018</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">71,836,963</td>
<td align="right"></td>
<td align="right">72,038,179</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,784,799,743</td>
<td align="right">52.1%</td>
<td align="right">12,767,555,286</td>
<td align="right">52.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,893,127,271</td>
<td align="right">52.6%</td>
<td align="right">12,876,552,838</td>
<td align="right">52.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,638,265,680</td>
<td align="right">47.4%</td>
<td align="right">11,624,449,856</td>
<td align="right">47.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,640,151,396</td>
<td align="right"></td>
<td align="right">11,626,378,057</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,592,608,642</td>
<td align="right"></td>
<td align="right">13,577,901,599</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,359,747,133</td>
<td align="right"></td>
<td align="right">4,357,883,216</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,519,615</td>
<td align="right"></td>
<td align="right">173,468,904</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,359,998</td>
<td align="right">0.1%</td>
<td align="right">15,360,534</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,160</td>
<td align="right">1.9%</td>
<td align="right">3,382,160</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">127,883</td>
<td align="right">0.1%</td>
<td align="right">127,883</td>
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
<td align="right">113,748,508</td>
<td align="right">19,546,324,589</td>
<td align="right">0</td>
<td align="right">114,756,577</td>
<td align="right">19,545,252,595</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,972,197,132</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,763,256</td>
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
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">943</td>
<td align="right">0.1%</td>
<td align="right">17,803</td>
<td align="right">0.9%</td>
<td align="right">1,787.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">172,780</td>
<td align="right">17.4%</td>
<td align="right">1,014,306</td>
<td align="right">53.8%</td>
<td align="right">487.1%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">10,776</td>
<td align="right">1.1%</td>
<td align="right">23,112</td>
<td align="right">1.2%</td>
<td align="right">114.5%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">993,527</td>
<td align="right"></td>
<td align="right">1,884,314</td>
<td align="right"></td>
<td align="right">89.7%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">3,100</td>
<td align="right">0.3%</td>
<td align="right">5,820</td>
<td align="right">0.3%</td>
<td align="right">87.7%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,951</td>
<td align="right">0.2%</td>
<td align="right">2,756</td>
<td align="right">0.1%</td>
<td align="right">41.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">602,273</td>
<td align="right">60.6%</td>
<td align="right">798,873</td>
<td align="right">42.4%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">9,014,904,987</td>
<td align="right"></td>
<td align="right">7,102,005,583</td>
<td align="right"></td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">285,169,549,791</td>
<td align="right">3,163.3%</td>
<td align="right">243,550,098,351</td>
<td align="right">3,429.3%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,690</td>
<td align="right">5.0%</td>
<td align="right">7,854</td>
<td align="right">0.8%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">818,796</td>
<td align="right">82.4%</td>
<td align="right">867,252</td>
<td align="right">46.0%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">200</td>
<td align="right">0.0%</td>
<td align="right">200</td>
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
<td align="right">162,488</td>
<td align="right">94.0%</td>
<td align="right">990,886</td>
<td align="right">97.7%</td>
<td align="right">509.8%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">172,780</td>
<td align="right"></td>
<td align="right">1,014,306</td>
<td align="right"></td>
<td align="right">487.1%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,574</td>
<td align="right">1.5%</td>
<td align="right">2,494</td>
<td align="right">0.2%</td>
<td align="right">-3.1%</td>
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
<td align="right">3,637</td>
<td align="right">2.1%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,678</td>
<td align="right">13.1%</td>
<td align="right">61,209</td>
<td align="right">6.0%</td>
<td align="right">169.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,799</td>
<td align="right">12.0%</td>
<td align="right">128,813</td>
<td align="right">12.7%</td>
<td align="right">519.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,690</td>
<td align="right">27.6%</td>
<td align="right">372,101</td>
<td align="right">36.7%</td>
<td align="right">680.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">39,735</td>
<td align="right">23.0%</td>
<td align="right">303,110</td>
<td align="right">29.9%</td>
<td align="right">662.8%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22,839</td>
<td align="right">13.2%</td>
<td align="right">116,954</td>
<td align="right">11.5%</td>
<td align="right">412.1%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">13,002</td>
<td align="right">7.5%</td>
<td align="right">28,479</td>
<td align="right">2.8%</td>
<td align="right">119.0%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">2,160</td>
<td align="right">1.3%</td>
<td align="right">3,400</td>
<td align="right">0.3%</td>
<td align="right">57.4%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">240</td>
<td align="right">0.1%</td>
<td align="right">240</td>
<td align="right">0.0%</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0</td>
<td align="right">0.0%</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">19,891</td>
<td align="right">11.5%</td>
<td align="right">39,352</td>
<td align="right">3.9%</td>
<td align="right">97.8%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">17,035</td>
<td align="right">9.9%</td>
<td align="right">103,418</td>
<td align="right">10.2%</td>
<td align="right">507.1%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">30,096</td>
<td align="right">17.4%</td>
<td align="right">146,298</td>
<td align="right">14.4%</td>
<td align="right">386.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">49,875</td>
<td align="right">28.9%</td>
<td align="right">452,105</td>
<td align="right">44.6%</td>
<td align="right">806.5%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">28,247</td>
<td align="right">16.3%</td>
<td align="right">193,086</td>
<td align="right">19.0%</td>
<td align="right">583.6%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">13,044</td>
<td align="right">7.5%</td>
<td align="right">50,247</td>
<td align="right">5.0%</td>
<td align="right">285.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,820</td>
<td align="right">2.2%</td>
<td align="right">5,900</td>
<td align="right">0.6%</td>
<td align="right">54.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">460</td>
<td align="right">0.3%</td>
<td align="right">480</td>
<td align="right">0.0%</td>
<td align="right">4.3%</td>
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
<td align="left">_POP_EXCEPT</td>
<td align="right">8,200</td>
<td align="right">340</td>
<td align="right">-95.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">143,040</td>
<td align="right">15,100</td>
<td align="right">-89.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">960,362,113</td>
<td align="right">186,487,301</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">25,246,820</td>
<td align="right">45,253,320</td>
<td align="right">79.2%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,018,060</td>
<td align="right">752,540</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,343,624,645</td>
<td align="right">416,038,619</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,470,425,248</td>
<td align="right">540,697,417</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">555,698,049</td>
<td align="right">223,965,749</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,343,531</td>
<td align="right">785,937,635</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">915,179,464</td>
<td align="right">443,694,426</td>
<td align="right">-51.5%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,580,380</td>
<td align="right">2,305,300</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,828,599</td>
<td align="right">361,475,587</td>
<td align="right">-46.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,603,484,226</td>
<td align="right">3,045,653,690</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">902,242,483</td>
<td align="right">508,278,193</td>
<td align="right">-43.7%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">40,727,305</td>
<td align="right">22,960,788</td>
<td align="right">-43.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,176,890,175</td>
<td align="right">2,951,622,275</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,033,160,840</td>
<td align="right">1,738,041,340</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">41,965,925</td>
<td align="right">24,679,111</td>
<td align="right">-41.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,338,214,565</td>
<td align="right">1,376,497,523</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">603,925,083</td>
<td align="right">355,674,679</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,604,135,313</td>
<td align="right">968,630,462</td>
<td align="right">-39.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,708,712,708</td>
<td align="right">2,899,145,667</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,683,935,230</td>
<td align="right">2,310,395,752</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,548,145,846</td>
<td align="right">1,617,015,368</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">941,936,966</td>
<td align="right">606,319,879</td>
<td align="right">-35.6%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,055,672,344</td>
<td align="right">1,328,747,804</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,700,920</td>
<td align="right">1,808,300</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,348,289,257</td>
<td align="right">1,592,054,882</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,448,118,022</td>
<td align="right">2,460,052,487</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">874,294,691</td>
<td align="right">624,800,502</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,124,970,591</td>
<td align="right">819,549,772</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,362,256,610</td>
<td align="right">1,723,854,322</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,864,377,913</td>
<td align="right">1,361,161,586</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,342,442,171</td>
<td align="right">10,547,950,688</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,940,369,397</td>
<td align="right">1,440,554,859</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,984,564,336</td>
<td align="right">7,434,019,756</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,763,275,898</td>
<td align="right">2,849,890,931</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,097,725,524</td>
<td align="right">6,283,070,978</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">230,748,645</td>
<td align="right">180,055,257</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">2,515,109,779</td>
<td align="right">1,962,854,800</td>
<td align="right">-22.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,301,328,596</td>
<td align="right">3,362,473,751</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">9,014,904,987</td>
<td align="right">7,102,005,583</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,459,867,504</td>
<td align="right">3,548,383,099</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">20,705,324,747</td>
<td align="right">16,533,967,519</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,941,520</td>
<td align="right">5,553,900</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">24,356,144,407</td>
<td align="right">19,636,195,988</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">96,213,280</td>
<td align="right">78,623,380</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">95,373,940</td>
<td align="right">78,329,300</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">142,356,961</td>
<td align="right">116,923,909</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,832,222,795</td>
<td align="right">2,337,863,191</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,431,982</td>
<td align="right">132,039,078</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,438,850,937</td>
<td align="right">1,191,160,135</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,156</td>
<td align="right">101,643,192</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,781,582,692</td>
<td align="right">6,480,509,086</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,680,276,279</td>
<td align="right">8,096,421,569</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">55,419,048</td>
<td align="right">46,377,336</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,141,255,938</td>
<td align="right">962,209,681</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,007,167,593</td>
<td align="right">1,697,194,989</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">1,686,700</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">415,379,443</td>
<td align="right">353,317,170</td>
<td align="right">-14.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,870,920</td>
<td align="right">1,599,400</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">657,378,743</td>
<td align="right">569,042,347</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">28,138,302</td>
<td align="right">25,314,729</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">653,979,553</td>
<td align="right">591,127,868</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">869,665,564</td>
<td align="right">789,526,899</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">206,372,250</td>
<td align="right">190,035,225</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,394,409</td>
<td align="right">58,380,091</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">71,146,582</td>
<td align="right">65,718,782</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">186,107,658</td>
<td align="right">172,741,993</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,222,222</td>
<td align="right">99,814,298</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">376,062,883</td>
<td align="right">350,969,857</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,153,047,242</td>
<td align="right">5,745,920,906</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">937,941</td>
<td align="right">877,114</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">887,427,315</td>
<td align="right">829,937,573</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,035,153,257</td>
<td align="right">968,392,503</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,377,842</td>
<td align="right">222,527,742</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,574,615</td>
<td align="right">6,202,093</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">208,859,920</td>
<td align="right">197,221,804</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">365,512</td>
<td align="right">346,218</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,957,475</td>
<td align="right">13,641,262</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">211,672,846</td>
<td align="right">200,738,543</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">6,786,594</td>
<td align="right">6,446,918</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">247,376,738</td>
<td align="right">235,239,285</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,306,328,939</td>
<td align="right">2,197,530,954</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,200,135,869</td>
<td align="right">2,101,644,784</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,200,886</td>
<td align="right">33,638,271</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,001,233,513</td>
<td align="right">1,915,379,082</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">240,956,075</td>
<td align="right">230,619,742</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">301,461,125</td>
<td align="right">288,700,556</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,895,216,550</td>
<td align="right">2,774,512,099</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,219,792</td>
<td align="right">58,734,252</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">614,441</td>
<td align="right">589,857</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">467,666,039</td>
<td align="right">449,339,080</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">164,185,696</td>
<td align="right">157,817,926</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,361,182</td>
<td align="right">129,800,112</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">26,796,331</td>
<td align="right">25,901,048</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,889,180</td>
<td align="right">150,221,020</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,061,289</td>
<td align="right">9,776,210</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,081,160</td>
<td align="right">2,023,380</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,485,946,444</td>
<td align="right">3,389,583,859</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">528,707,243</td>
<td align="right">514,823,687</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,081,530,132</td>
<td align="right">1,053,395,005</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">65,250,400</td>
<td align="right">63,572,760</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,580,809,710</td>
<td align="right">1,540,211,896</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,577,021</td>
<td align="right">73,722,291</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,548,425,850</td>
<td align="right">7,375,298,706</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">99,691,136</td>
<td align="right">97,469,359</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,563,944,687</td>
<td align="right">1,529,588,790</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">162,104,246</td>
<td align="right">158,579,241</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,640,957,188</td>
<td align="right">7,477,445,142</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,940,107,068</td>
<td align="right">1,899,143,302</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,544,129,907</td>
<td align="right">1,511,752,090</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">438,495,179</td>
<td align="right">429,509,515</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">106,094,463</td>
<td align="right">104,172,437</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">340,483,301</td>
<td align="right">346,435,926</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">825,705,028</td>
<td align="right">811,456,563</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,184,551,275</td>
<td align="right">3,129,709,986</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,145,554,855</td>
<td align="right">3,091,387,946</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,303,825</td>
<td align="right">53,372,225</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,299,585</td>
<td align="right">53,368,645</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">878,182,156</td>
<td align="right">864,594,574</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,787,736</td>
<td align="right">3,729,364</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,946,365,440</td>
<td align="right">1,916,481,236</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">710,624,683</td>
<td align="right">700,070,689</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">391,425,102</td>
<td align="right">385,674,702</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">159,953,595</td>
<td align="right">157,654,715</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">111,840,420</td>
<td align="right">110,283,934</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">534,936,352</td>
<td align="right">528,034,143</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">978,405,654</td>
<td align="right">965,856,214</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,420,956,327</td>
<td align="right">1,402,953,810</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,326,996,411</td>
<td align="right">1,310,745,576</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">234,817,246</td>
<td align="right">232,104,452</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">257,276,665</td>
<td align="right">260,183,413</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,980,819</td>
<td align="right">113,723,792</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,330,484</td>
<td align="right">8,241,644</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">325,869,499</td>
<td align="right">322,652,588</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,076,776,136</td>
<td align="right">1,066,418,102</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,624</td>
<td align="right">11,724</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">569,357,290</td>
<td align="right">564,497,180</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,296,688</td>
<td align="right">13,191,651</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,296,688</td>
<td align="right">13,191,651</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">990,866,582</td>
<td align="right">983,066,916</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,045,929,768</td>
<td align="right">1,037,740,497</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">307,134,561</td>
<td align="right">304,733,440</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">497,898,064</td>
<td align="right">494,041,691</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">502,702,224</td>
<td align="right">498,845,411</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">986,762,974</td>
<td align="right">979,616,717</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,490</td>
<td align="right">1,294,064</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,600,625,198</td>
<td align="right">3,576,112,818</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">239,659,590</td>
<td align="right">238,037,228</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,707,868</td>
<td align="right">85,133,251</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,702,031,262</td>
<td align="right">3,677,488,458</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,419,220</td>
<td align="right">124,703,880</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,244,048</td>
<td align="right">279,740,129</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">688,538,614</td>
<td align="right">684,977,419</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">788,268,381</td>
<td align="right">784,513,433</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,577,440</td>
<td align="right">5,550,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,632,540</td>
<td align="right">530,716,920</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,926,402</td>
<td align="right">78,656,208</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">197,058,566</td>
<td align="right">196,385,891</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,634,039</td>
<td align="right">94,349,959</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">107,884,360</td>
<td align="right">108,184,540</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,200</td>
<td align="right">4,247,678</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,246,790,636</td>
<td align="right">1,243,943,948</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,235,799,942</td>
<td align="right">2,231,146,555</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,894</td>
<td align="right">5,461,760</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,974,995</td>
<td align="right">1,817,474,643</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,567,700</td>
<td align="right">32,621,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,442,680</td>
<td align="right">9,427,638</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,639,920</td>
<td align="right">204,318,580</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,398,228</td>
<td align="right">97,283,228</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">234,896,292</td>
<td align="right">234,625,987</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">37,843,900</td>
<td align="right">37,801,860</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,226,981</td>
<td align="right">68,151,819</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,828</td>
<td align="right">90,241,657</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,929</td>
<td align="right">167,814,720</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">393,967,002</td>
<td align="right">393,722,142</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,289,081</td>
<td align="right">97,232,141</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,089,903</td>
<td align="right">39,068,166</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">102,819,372</td>
<td align="right">102,762,752</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,620</td>
<td align="right">103,760,798</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,620</td>
<td align="right">103,760,798</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">127,819,170</td>
<td align="right">127,753,294</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,780,100</td>
<td align="right">57,752,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">162,266,588</td>
<td align="right">162,194,004</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,625,940</td>
<td align="right">46,605,174</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,240,981</td>
<td align="right">97,202,721</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,260</td>
<td align="right">517,900,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,852,286</td>
<td align="right">532,681,646</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,660,964,448</td>
<td align="right">1,660,534,213</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,436,734</td>
<td align="right">779,276,889</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,794,494</td>
<td align="right">780,634,649</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">732,984,238</td>
<td align="right">732,869,726</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">856,223,278</td>
<td align="right">856,147,443</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,331,855,094</td>
<td align="right">1,331,762,663</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">11,445,900</td>
<td align="right">11,445,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">81,007,580</td>
<td align="right">81,003,185</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,437,280</td>
<td align="right">32,436,298</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">559,022,360</td>
<td align="right">559,014,680</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,488,404</td>
<td align="right">228,487,604</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,950</td>
<td align="right">603,439,934</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,096,877,240</td>
<td align="right">1,096,877,240</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">350,232,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">125,514,720</td>
<td align="right">125,514,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">51,907,580</td>
<td align="right">51,907,580</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">10,396,360</td>
<td align="right">10,396,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">4,739,520</td>
<td align="right">4,739,520</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">1,825,480</td>
<td align="right">1,825,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,543,885</td>
<td align="right">1,543,885</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">1,225,880</td>
<td align="right">1,225,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">590,260</td>
<td align="right">590,260</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_ATTR</td>
<td align="right">375,780</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">322,020</td>
<td align="right">322,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">24,662</td>
<td align="right">24,662</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INCREMENT_RUN_COUNT</td>
<td align="right"></td>
<td align="right">9,439,868,774</td>
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
<td align="left">CALL_KW</td>
<td align="right">36,344</td>
<td align="right">86,106</td>
<td align="right">136.9%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,181</td>
<td align="right">24,762</td>
<td align="right">121.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">131,353</td>
<td align="right">59,803</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">920</td>
<td align="right">1,320</td>
<td align="right">43.5%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,563</td>
<td align="right">62,074</td>
<td align="right">42.5%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,440</td>
<td align="right">42,880</td>
<td align="right">24.5%</td>
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
<td align="right">1,146</td>
<td align="right">1,147</td>
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
<td align="right">1,146</td>
<td align="right">1,147</td>
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
<td align="right">460</td>
<td align="right">460</td>
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
<td align="right">1,801</td>
<td align="right">1,801</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-10-21
