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
<td align="left">CLEANUP_THROW</td>
<td align="right">98,514</td>
<td align="right">496</td>
<td align="right">-99.5%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,559</td>
<td align="right">12,071</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">76,557</td>
<td align="right">21,574</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,826,265</td>
<td align="right">575,538</td>
<td align="right">-68.5%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,279,457</td>
<td align="right">3,076,491</td>
<td align="right">-57.7%</td>
</tr>
<tr>
<td align="left">DELETE_NAME</td>
<td align="right">36</td>
<td align="right">16</td>
<td align="right">-55.6%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">232,167</td>
<td align="right">117,444</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">774,776</td>
<td align="right">395,907</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,346,746</td>
<td align="right">3,882,311</td>
<td align="right">-47.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">1,450,828</td>
<td align="right">937,092</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,516</td>
<td align="right">3,794</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,231</td>
<td align="right">41,485</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">LOAD_COMMON_CONSTANT</td>
<td align="right">28,586,948</td>
<td align="right">20,892,364</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,889</td>
<td align="right">2,930</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,954,978</td>
<td align="right">27,151,248</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,583,807</td>
<td align="right">63,272,417</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">68,873,327</td>
<td align="right">52,305,765</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,644</td>
<td align="right">2,021</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">SETUP_ANNOTATIONS</td>
<td align="right">153</td>
<td align="right">117</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,482,325</td>
<td align="right">18,030,147</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,766,710</td>
<td align="right">6,026,761</td>
<td align="right">-22.4%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,299</td>
<td align="right">4,240</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">135,701</td>
<td align="right">110,088</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">71,948,307</td>
<td align="right">60,106,861</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">34,189</td>
<td align="right">28,989</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,796,330</td>
<td align="right">3,265,232</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,481,593</td>
<td align="right">3,971,529</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">61,902,021</td>
<td align="right">54,968,217</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">69,813,049</td>
<td align="right">62,272,297</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">404,847</td>
<td align="right">361,919</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,832,701</td>
<td align="right">60,690,631</td>
<td align="right">-10.5%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,643,365</td>
<td align="right">1,482,762</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">156,196,640</td>
<td align="right">141,242,538</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">135,708,261</td>
<td align="right">123,562,648</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">340,415,564</td>
<td align="right">310,940,423</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,031,312</td>
<td align="right">725,005,289</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">116,003,786</td>
<td align="right">106,376,558</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">779,278,422</td>
<td align="right">715,418,821</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,613</td>
<td align="right">3,326</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,784,054</td>
<td align="right">1,643,320</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">99,060,670</td>
<td align="right">91,284,902</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,155,761,569</td>
<td align="right">1,066,530,407</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,475,857</td>
<td align="right">62,273,745</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">493,987,374</td>
<td align="right">456,183,387</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">14,754</td>
<td align="right">13,720</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">FORMAT_WITH_SPEC</td>
<td align="right">2,752</td>
<td align="right">2,560</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">115,608,580</td>
<td align="right">107,911,903</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">95,168,224</td>
<td align="right">89,327,420</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">839,327,429</td>
<td align="right">792,389,419</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,024,108</td>
<td align="right">19,872,334</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">325,824,502</td>
<td align="right">308,361,311</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">548,485,167</td>
<td align="right">519,200,650</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">355,642,659</td>
<td align="right">336,694,384</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,850,295</td>
<td align="right">122,113,015</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,355,359</td>
<td align="right">20,277,780</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,355,378</td>
<td align="right">20,277,801</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">174,954,419</td>
<td align="right">166,199,123</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">417,005,390</td>
<td align="right">397,415,173</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">178,725,614</td>
<td align="right">170,383,291</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,617,826</td>
<td align="right">332,403,605</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">824,669,787</td>
<td align="right">787,288,569</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">317,551,335</td>
<td align="right">304,026,884</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,284,834</td>
<td align="right">70,368,767</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">559,088,929</td>
<td align="right">538,164,836</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,201,649,519</td>
<td align="right">2,123,589,363</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,223,966</td>
<td align="right">162,325,291</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,063,786,398</td>
<td align="right">1,027,041,930</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">92,943,695</td>
<td align="right">89,833,283</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,744,056</td>
<td align="right">55,877,354</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">203,364,134</td>
<td align="right">197,005,933</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">100,792,417</td>
<td align="right">97,691,319</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,530</td>
<td align="right">5,981,971</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">533,904,382</td>
<td align="right">518,349,146</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,899,098,005</td>
<td align="right">3,786,397,483</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,652,085</td>
<td align="right">293,954,463</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">436,418,407</td>
<td align="right">423,881,972</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,381,535,612</td>
<td align="right">1,341,862,001</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,103,971,935</td>
<td align="right">2,044,168,572</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,843,139</td>
<td align="right">497,383,505</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,312,924,081</td>
<td align="right">3,220,233,144</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">121,012</td>
<td align="right">117,653</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">72,986,887</td>
<td align="right">71,004,841</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">222,452,051</td>
<td align="right">216,593,543</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,691,337</td>
<td align="right">7,490,366</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">62,492,346</td>
<td align="right">60,903,772</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,551,040,283</td>
<td align="right">1,511,927,753</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,261,673,198</td>
<td align="right">6,106,899,718</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">305,789,613</td>
<td align="right">298,232,617</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">402,467,719</td>
<td align="right">392,536,338</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,522,424,656</td>
<td align="right">1,485,009,264</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,212,158,356</td>
<td align="right">1,182,438,902</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,117,873,509</td>
<td align="right">1,090,979,076</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,369,788,842</td>
<td align="right">5,240,907,202</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">356,248,800</td>
<td align="right">348,687,584</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,899,228</td>
<td align="right">56,679,414</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,381,455</td>
<td align="right">61,069,770</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,776,595,788</td>
<td align="right">5,656,233,400</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">254,814,952</td>
<td align="right">249,530,685</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,677,245</td>
<td align="right">120,134,276</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,220,562</td>
<td align="right">75,695,455</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,495,712,606</td>
<td align="right">2,446,433,366</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,193,539,178</td>
<td align="right">3,130,987,513</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,819,221,815</td>
<td align="right">5,707,793,870</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">638,568,677</td>
<td align="right">626,386,609</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,329,280,037</td>
<td align="right">1,304,971,556</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">674,316,252</td>
<td align="right">662,320,323</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_TUPLE_INT</td>
<td align="right">292,954,639</td>
<td align="right">287,957,363</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,563,627</td>
<td align="right">260,230,748</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,535,420,424</td>
<td align="right">2,494,463,006</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,577,882</td>
<td align="right">71,411,231</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">267,379,559</td>
<td align="right">263,100,958</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,468,867,783</td>
<td align="right">1,446,016,216</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW</td>
<td align="right">34,238,676,630</td>
<td align="right">33,710,051,738</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,726,658,988</td>
<td align="right">10,561,166,623</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,110,221</td>
<td align="right">11,273,467</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">7,220,016,589</td>
<td align="right">7,114,278,410</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,499,614</td>
<td align="right">365,077,882</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">808,531,196</td>
<td align="right">796,737,959</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,114,691,851</td>
<td align="right">1,098,977,176</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,125,258</td>
<td align="right">558,452,373</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,109,154</td>
<td align="right">192,554,610</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">420,104,320</td>
<td align="right">414,728,089</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">2,945,273,611</td>
<td align="right">2,907,674,576</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_BORROW_LOAD_FAST_BORROW</td>
<td align="right">10,080,891,753</td>
<td align="right">9,952,572,913</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,515,816</td>
<td align="right">586,236,167</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,430,682,908</td>
<td align="right">13,267,174,735</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">948,414,106</td>
<td align="right">937,696,358</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">491,983,013</td>
<td align="right">487,450,016</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">375,932,970</td>
<td align="right">372,480,974</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">948,935,884</td>
<td align="right">940,333,493</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,135,953,134</td>
<td align="right">2,117,265,992</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,806,829,224</td>
<td align="right">2,782,478,805</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">41,964,608</td>
<td align="right">41,603,679</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,192,416,630</td>
<td align="right">3,166,780,035</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,736,524,713</td>
<td align="right">2,714,913,057</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,529,745,745</td>
<td align="right">2,509,945,829</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,263,512,487</td>
<td align="right">2,246,028,845</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,584,466,589</td>
<td align="right">1,572,348,115</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">357,045,467</td>
<td align="right">354,474,421</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">7,863,452</td>
<td align="right">7,808,756</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">191,146,333</td>
<td align="right">189,827,944</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_LIST_INT</td>
<td align="right">2,719,612,343</td>
<td align="right">2,701,492,191</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">863,191,165</td>
<td align="right">857,750,939</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">629,795,760</td>
<td align="right">625,979,439</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,834,281,235</td>
<td align="right">4,805,013,584</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">238,200,264</td>
<td align="right">236,771,995</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">240,257,550</td>
<td align="right">238,825,702</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_DICT</td>
<td align="right">1,078,938,828</td>
<td align="right">1,072,528,578</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,275,841,483</td>
<td align="right">1,268,499,200</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,850,656</td>
<td align="right">89,347,455</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">405,746,033</td>
<td align="right">403,605,964</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,073,715</td>
<td align="right">1,396,808,564</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,287,840,999</td>
<td align="right">7,254,723,097</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,689</td>
<td align="right">127,135,123</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,881,559</td>
<td align="right">154,382,053</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,502,420,733</td>
<td align="right">1,497,618,698</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,026,239</td>
<td align="right">698,960,119</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,022,090</td>
<td align="right">270,226,169</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">78,105,545</td>
<td align="right">77,897,074</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">939,077,334</td>
<td align="right">936,738,392</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,058</td>
<td align="right">14,724,196</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,657,489,979</td>
<td align="right">1,653,885,821</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,484,332,519</td>
<td align="right">3,476,832,601</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,957,873</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,370,313</td>
<td align="right">62,263,550</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,477,634</td>
<td align="right">13,455,780</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,162,376</td>
<td align="right">114,980,805</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,755,452,717</td>
<td align="right">1,753,092,273</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,743,587</td>
<td align="right">545,099,870</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,743,072</td>
<td align="right">9,735,022</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,190</td>
<td align="right">188,393,416</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,416,957</td>
<td align="right">131,331,239</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_STR_INT</td>
<td align="right">1,252,143,687</td>
<td align="right">1,251,652,050</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBSCR_GETITEM</td>
<td align="right">156,271,824</td>
<td align="right">156,217,684</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,592,174</td>
<td align="right">340,646,706</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">158,387,204</td>
<td align="right">158,373,127</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">287,605,175</td>
<td align="right">287,628,623</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,555,140</td>
<td align="right">504,573,585</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">73,291,751</td>
<td align="right">73,290,546</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">6,152,485</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,724,898</td>
<td align="right">112,724,681</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">1,053,436,105</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">172,683,388</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">100,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
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
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">53,984</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_FROM_DICT_OR_DEREF</td>
<td align="right">1,476</td>
<td align="right">1,476</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INSTRUMENTED_JUMP_BACKWARD</td>
<td align="right">120</td>
<td align="right">120</td>
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
<td align="right">2,805,883,724</td>
<td align="right">15.0%</td>
<td align="right">2,781,562,401</td>
<td align="right">14.9%</td>
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
<td align="right">15,834,374,998</td>
<td align="right">84.7%</td>
<td align="right">15,773,515,194</td>
<td align="right">84.7%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">58,940,895</td>
<td align="right">0.3%</td>
<td align="right">58,749,083</td>
<td align="right">0.3%</td>
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
<td align="right">925,425</td>
<td align="right">45.1%</td>
<td align="right">899,918</td>
<td align="right">44.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,128,760</td>
<td align="right">54.9%</td>
<td align="right">1,121,542</td>
<td align="right">55.5%</td>
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
<td align="left">subtract different types</td>
<td align="right">628</td>
<td align="right">0.1%</td>
<td align="right">287</td>
<td align="right">0.0%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left">subscr</td>
<td align="right">8,062</td>
<td align="right">0.9%</td>
<td align="right">4,123</td>
<td align="right">0.5%</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.2%</td>
<td align="right">1,233</td>
<td align="right">0.1%</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">subscr string slice</td>
<td align="right">2,344</td>
<td align="right">0.3%</td>
<td align="right">1,623</td>
<td align="right">0.2%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.0%</td>
<td align="right">282</td>
<td align="right">0.0%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.3%</td>
<td align="right">2,503</td>
<td align="right">0.3%</td>
<td align="right">-20.6%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.3%</td>
<td align="right">2,137</td>
<td align="right">0.2%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">subscr tuple slice</td>
<td align="right">1,968</td>
<td align="right">0.2%</td>
<td align="right">1,572</td>
<td align="right">0.2%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,225</td>
<td align="right">0.8%</td>
<td align="right">5,989</td>
<td align="right">0.7%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,247</td>
<td align="right">0.1%</td>
<td align="right">1,052</td>
<td align="right">0.1%</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,515</td>
<td align="right">0.9%</td>
<td align="right">7,654</td>
<td align="right">0.9%</td>
<td align="right">-10.1%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.1%</td>
<td align="right">1,254</td>
<td align="right">0.1%</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">46,973</td>
<td align="right">5.1%</td>
<td align="right">43,078</td>
<td align="right">4.8%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">subscr other slice</td>
<td align="right">327</td>
<td align="right">0.0%</td>
<td align="right">305</td>
<td align="right">0.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,664</td>
<td align="right">4.0%</td>
<td align="right">34,274</td>
<td align="right">3.8%</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,203</td>
<td align="right">0.9%</td>
<td align="right">7,710</td>
<td align="right">0.9%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,205</td>
<td align="right">8.0%</td>
<td align="right">70,312</td>
<td align="right">7.8%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">subscr deque</td>
<td align="right">141</td>
<td align="right">0.0%</td>
<td align="right">146</td>
<td align="right">0.0%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,512</td>
<td align="right">2.5%</td>
<td align="right">22,923</td>
<td align="right">2.5%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">85</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">subscr defaultdict</td>
<td align="right">79,308</td>
<td align="right">8.6%</td>
<td align="right">77,491</td>
<td align="right">8.6%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,828</td>
<td align="right">4.7%</td>
<td align="right">43,087</td>
<td align="right">4.8%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,421</td>
<td align="right">4.7%</td>
<td align="right">42,816</td>
<td align="right">4.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subscr list slice</td>
<td align="right">115,301</td>
<td align="right">12.5%</td>
<td align="right">114,472</td>
<td align="right">12.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,969</td>
<td align="right">3.7%</td>
<td align="right">33,735</td>
<td align="right">3.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,448</td>
<td align="right">2.1%</td>
<td align="right">19,433</td>
<td align="right">2.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">9.2%</td>
<td align="right">85,540</td>
<td align="right">9.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr array</td>
<td align="right">121,439</td>
<td align="right">13.1%</td>
<td align="right">121,438</td>
<td align="right">13.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subscr counter</td>
<td align="right">114,964</td>
<td align="right">12.4%</td>
<td align="right">114,964</td>
<td align="right">12.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr bytes</td>
<td align="right">22,296</td>
<td align="right">2.4%</td>
<td align="right">22,296</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">11,587</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">596</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr mappingproxy</td>
<td align="right">561</td>
<td align="right">0.1%</td>
<td align="right">561</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr structtime</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr ordereddict</td>
<td align="right">26</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">or int</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subscr stacksummary</td>
<td align="right">3</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">subscr enumdict</td>
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
<td align="right">545,743,587</td>
<td align="right">100.0%</td>
<td align="right">545,099,870</td>
<td align="right">100.0%</td>
<td align="right">-0.1%</td>
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
<td align="right">179,130,509</td>
<td align="right">1.6%</td>
<td align="right">152,281,615</td>
<td align="right">1.4%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">175,982,846</td>
<td align="right">1.6%</td>
<td align="right">149,627,801</td>
<td align="right">1.4%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,015,043,121</td>
<td align="right">98.4%</td>
<td align="right">10,820,839,469</td>
<td align="right">98.6%</td>
<td align="right">-1.8%</td>
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
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right">3,552,064</td>
<td align="right">100.0%</td>
<td align="right">3,015,287</td>
<td align="right">100.0%</td>
<td align="right">-15.1%</td>
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
<td align="right">690</td>
<td align="right">154.7%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">246</td>
<td align="right">55.2%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">566</td>
<td align="right">126.9%</td>
<td align="right">566</td>
<td align="right">126.9%</td>
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
<td align="right">584,644</td>
<td align="right">82.9%</td>
<td align="right">8,857</td>
<td align="right">7.0%</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">685,346</td>
<td align="right">97.1%</td>
<td align="right">119,492</td>
<td align="right">94.5%</td>
<td align="right">-82.6%</td>
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
<td align="right">20,190</td>
<td align="right">99.4%</td>
<td align="right">6,898</td>
<td align="right">98.3%</td>
<td align="right">-65.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">120</td>
<td align="right">0.6%</td>
<td align="right">120</td>
<td align="right">1.7%</td>
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
<td align="right">1,380,071</td>
<td align="right">0.0%</td>
<td align="right">1,299,123</td>
<td align="right">0.0%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">511,614,467</td>
<td align="right">10.2%</td>
<td align="right">497,173,609</td>
<td align="right">10.0%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,508,146,421</td>
<td align="right">89.8%</td>
<td align="right">4,474,355,465</td>
<td align="right">90.0%</td>
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
<td align="left">Success</td>
<td align="right">43,755</td>
<td align="right">17.2%</td>
<td align="right">39,969</td>
<td align="right">17.1%</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">210,629</td>
<td align="right">82.8%</td>
<td align="right">194,159</td>
<td align="right">82.9%</td>
<td align="right">-7.8%</td>
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
<td align="right">2,053</td>
<td align="right">1.0%</td>
<td align="right">768</td>
<td align="right">0.4%</td>
<td align="right">-62.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,838</td>
<td align="right">3.7%</td>
<td align="right">5,414</td>
<td align="right">2.8%</td>
<td align="right">-30.9%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,370</td>
<td align="right">11.1%</td>
<td align="right">17,447</td>
<td align="right">9.0%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">941</td>
<td align="right">0.4%</td>
<td align="right">728</td>
<td align="right">0.4%</td>
<td align="right">-22.6%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">312</td>
<td align="right">0.2%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">10,525</td>
<td align="right">5.0%</td>
<td align="right">9,666</td>
<td align="right">5.0%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,750</td>
<td align="right">21.7%</td>
<td align="right">42,043</td>
<td align="right">21.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">90,467</td>
<td align="right">43.0%</td>
<td align="right">88,490</td>
<td align="right">45.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,648</td>
<td align="right">3.6%</td>
<td align="right">7,486</td>
<td align="right">3.9%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,832</td>
<td align="right">3.2%</td>
<td align="right">6,695</td>
<td align="right">3.4%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">13,480</td>
<td align="right">6.4%</td>
<td align="right">13,741</td>
<td align="right">7.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,369</td>
<td align="right">0.6%</td>
<td align="right">1,369</td>
<td align="right">0.7%</td>
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
<td align="right">156,135,029</td>
<td align="right">6.6%</td>
<td align="right">141,192,656</td>
<td align="right">6.1%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,409,375</td>
<td align="right">0.1%</td>
<td align="right">1,368,378</td>
<td align="right">0.1%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,190,461,749</td>
<td align="right">93.3%</td>
<td align="right">2,175,605,867</td>
<td align="right">93.8%</td>
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
<td align="right">59,494</td>
<td align="right">67.4%</td>
<td align="right">48,582</td>
<td align="right">64.2%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">28,712</td>
<td align="right">32.6%</td>
<td align="right">27,132</td>
<td align="right">35.8%</td>
<td align="right">-5.5%</td>
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
<td align="right">11,675</td>
<td align="right">19.6%</td>
<td align="right">7,416</td>
<td align="right">15.3%</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,722</td>
<td align="right">19.7%</td>
<td align="right">7,964</td>
<td align="right">16.4%</td>
<td align="right">-32.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,645</td>
<td align="right">24.6%</td>
<td align="right">13,236</td>
<td align="right">27.2%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">21,452</td>
<td align="right">36.1%</td>
<td align="right">19,966</td>
<td align="right">41.1%</td>
<td align="right">-6.9%</td>
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
<td align="right">3,541,725,540</td>
<td align="right">68.4%</td>
<td align="right">3,416,125,531</td>
<td align="right">68.0%</td>
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
<td align="right">1,468,431,096</td>
<td align="right">28.4%</td>
<td align="right">1,445,624,019</td>
<td align="right">28.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">164,039,685</td>
<td align="right">3.2%</td>
<td align="right">162,732,840</td>
<td align="right">3.2%</td>
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
<td align="right">431,108</td>
<td align="right">12.2%</td>
<td align="right">388,490</td>
<td align="right">11.2%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">3,100,491</td>
<td align="right">87.8%</td>
<td align="right">3,074,025</td>
<td align="right">88.8%</td>
<td align="right">-0.9%</td>
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
<td align="right">71,947</td>
<td align="right">16.7%</td>
<td align="right">35,687</td>
<td align="right">9.2%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,607</td>
<td align="right">4.5%</td>
<td align="right">10,216</td>
<td align="right">2.6%</td>
<td align="right">-47.9%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">130</td>
<td align="right">0.0%</td>
<td align="right">-25.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,604</td>
<td align="right">1.1%</td>
<td align="right">3,646</td>
<td align="right">0.9%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,936</td>
<td align="right">1.6%</td>
<td align="right">5,786</td>
<td align="right">1.5%</td>
<td align="right">-16.6%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">3,149</td>
<td align="right">0.7%</td>
<td align="right">2,865</td>
<td align="right">0.7%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">35,042</td>
<td align="right">8.1%</td>
<td align="right">32,449</td>
<td align="right">8.4%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">10,835</td>
<td align="right">2.5%</td>
<td align="right">10,437</td>
<td align="right">2.7%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">258</td>
<td align="right">0.1%</td>
<td align="right">251</td>
<td align="right">0.1%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,154</td>
<td align="right">0.7%</td>
<td align="right">3,111</td>
<td align="right">0.8%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">172,124</td>
<td align="right">39.9%</td>
<td align="right">170,254</td>
<td align="right">43.8%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,223</td>
<td align="right">0.3%</td>
<td align="right">1,212</td>
<td align="right">0.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,796</td>
<td align="right">19.4%</td>
<td align="right">83,223</td>
<td align="right">21.4%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,259</td>
<td align="right">4.2%</td>
<td align="right">18,243</td>
<td align="right">4.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">10,479</td>
<td align="right">2.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">501</td>
<td align="right">0.1%</td>
<td align="right"></td>
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
<td align="left">set</td>
<td align="right">12,959,181</td>
<td align="right">12,959,181 / 0 !!</td>
<td align="right">6,516,411</td>
<td align="right">6,516,411 / 0 !!</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">6,121,195</td>
<td align="right">6,121,195 / 0 !!</td>
<td align="right">4,985,197</td>
<td align="right">4,985,197 / 0 !!</td>
<td align="right">-18.6%</td>
</tr>
<tr>
<td align="left">self</td>
<td align="right">394,627,535</td>
<td align="right">394,627,535 / 0 !!</td>
<td align="right">339,998,211</td>
<td align="right">339,998,211 / 0 !!</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">120,047,526</td>
<td align="right">120,047,526 / 0 !!</td>
<td align="right">113,341,210</td>
<td align="right">113,341,210 / 0 !!</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">generator</td>
<td align="right">102,451,624</td>
<td align="right">102,451,624 / 0 !!</td>
<td align="right">96,990,308</td>
<td align="right">96,990,308 / 0 !!</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">310,526,015</td>
<td align="right">310,526,015 / 0 !!</td>
<td align="right">300,778,862</td>
<td align="right">300,778,862 / 0 !!</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">170,522,029</td>
<td align="right">170,522,029 / 0 !!</td>
<td align="right">165,451,593</td>
<td align="right">165,451,593 / 0 !!</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">2,710,432</td>
<td align="right">2,710,432 / 0 !!</td>
<td align="right">2,693,406</td>
<td align="right">2,693,406 / 0 !!</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">34,968,901</td>
<td align="right">34,968,901 / 0 !!</td>
<td align="right">34,948,081</td>
<td align="right">34,948,081 / 0 !!</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">827,131</td>
<td align="right">827,131 / 0 !!</td>
<td align="right">827,128</td>
<td align="right">827,128 / 0 !!</td>
<td align="right">-0.0%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,436,112</td>
<td align="right">0.0%</td>
<td align="right">1,063,703</td>
<td align="right">0.0%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">869,763,343</td>
<td align="right">6.3%</td>
<td align="right">816,137,211</td>
<td align="right">6.1%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">822,826,896</td>
<td align="right">6.0%</td>
<td align="right">785,617,716</td>
<td align="right">5.8%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,025,398,656</td>
<td align="right">87.6%</td>
<td align="right">11,835,945,587</td>
<td align="right">88.1%</td>
<td align="right">-1.6%</td>
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
<td align="right">560,589</td>
<td align="right">3.3%</td>
<td align="right">459,811</td>
<td align="right">2.9%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,494,334</td>
<td align="right">96.7%</td>
<td align="right">15,456,654</td>
<td align="right">97.1%</td>
<td align="right">-6.3%</td>
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
<td align="right">1,778</td>
<td align="right">0.3%</td>
<td align="right">303</td>
<td align="right">0.1%</td>
<td align="right">-83.0%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,116</td>
<td align="right">1.1%</td>
<td align="right">3,609</td>
<td align="right">0.8%</td>
<td align="right">-41.0%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,182</td>
<td align="right">0.2%</td>
<td align="right">791</td>
<td align="right">0.2%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,738</td>
<td align="right">0.5%</td>
<td align="right">2,085</td>
<td align="right">0.5%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,627</td>
<td align="right">11.9%</td>
<td align="right">50,784</td>
<td align="right">11.0%</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,129</td>
<td align="right">1.6%</td>
<td align="right">7,556</td>
<td align="right">1.6%</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,677</td>
<td align="right">3.0%</td>
<td align="right">14,102</td>
<td align="right">3.1%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,284</td>
<td align="right">4.5%</td>
<td align="right">21,669</td>
<td align="right">4.7%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">163</td>
<td align="right">0.0%</td>
<td align="right">140</td>
<td align="right">0.0%</td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,093</td>
<td align="right">0.2%</td>
<td align="right">944</td>
<td align="right">0.2%</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,675</td>
<td align="right">10.3%</td>
<td align="right">54,080</td>
<td align="right">11.8%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,810</td>
<td align="right">0.3%</td>
<td align="right">1,701</td>
<td align="right">0.4%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">77,620</td>
<td align="right">13.8%</td>
<td align="right">74,436</td>
<td align="right">16.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">4,452</td>
<td align="right">0.8%</td>
<td align="right">4,336</td>
<td align="right">0.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,363</td>
<td align="right">1.4%</td>
<td align="right">-0.7%</td>
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
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,473</td>
<td align="right">0.0%</td>
<td align="right">990</td>
<td align="right">0.0%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,887</td>
<td align="right">0.0%</td>
<td align="right">43,943</td>
<td align="right">0.0%</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,089,465,982</td>
<td align="right">99.8%</td>
<td align="right">8,876,422,601</td>
<td align="right">99.8%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,623,556</td>
<td align="right">0.2%</td>
<td align="right">14,615,237</td>
<td align="right">0.2%</td>
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
<td align="right">137,272</td>
<td align="right">100.0%</td>
<td align="right">109,595</td>
<td align="right">100.0%</td>
<td align="right">-20.2%</td>
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
<td align="right">251</td>
<td align="right">0.0%</td>
<td align="right">96</td>
<td align="right">0.0%</td>
<td align="right">-61.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">63,943,174</td>
<td align="right">100.0%</td>
<td align="right">61,840,864</td>
<td align="right">100.0%</td>
<td align="right">-3.3%</td>
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
<td align="right">2,393</td>
<td align="right">100.0%</td>
<td align="right">1,925</td>
<td align="right">100.0%</td>
<td align="right">-19.6%</td>
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
<td align="right">14,711</td>
<td align="right">0.0%</td>
<td align="right">9,124</td>
<td align="right">0.0%</td>
<td align="right">-38.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">128,815,497</td>
<td align="right">17.8%</td>
<td align="right">122,081,423</td>
<td align="right">17.2%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,501,105</td>
<td align="right">82.2%</td>
<td align="right">586,227,043</td>
<td align="right">82.8%</td>
<td align="right">-1.2%</td>
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
<td align="right">463</td>
<td align="right">1.5%</td>
<td align="right">-29.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,411</td>
<td align="right">98.1%</td>
<td align="right">31,288</td>
<td align="right">98.5%</td>
<td align="right">-9.1%</td>
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
<td align="right">3,260</td>
<td align="right">9.5%</td>
<td align="right">940</td>
<td align="right">3.0%</td>
<td align="right">-71.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">5,959</td>
<td align="right">17.3%</td>
<td align="right">5,908</td>
<td align="right">18.9%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">async generator send</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">78.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right"></td>
<td align="right"></td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,498,276</td>
<td align="right">5.8%</td>
<td align="right">110,756,172</td>
<td align="right">5.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,127,109</td>
<td align="right">3.9%</td>
<td align="right">75,610,607</td>
<td align="right">3.9%</td>
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
<td align="right">1,791,828,555</td>
<td align="right">90.3%</td>
<td align="right">1,776,231,552</td>
<td align="right">90.5%</td>
<td align="right">-0.9%</td>
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
<td align="right">52,763</td>
<td align="right">2.3%</td>
<td align="right">48,701</td>
<td align="right">2.2%</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,200,162</td>
<td align="right">97.7%</td>
<td align="right">2,125,083</td>
<td align="right">97.8%</td>
<td align="right">-3.4%</td>
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
<td align="right">3,356</td>
<td align="right">6.4%</td>
<td align="right">1,764</td>
<td align="right">3.6%</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">271,475</td>
<td align="right">514.5%</td>
<td align="right">208,453</td>
<td align="right">428.0%</td>
<td align="right">-23.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,435</td>
<td align="right">2.9%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">362</td>
<td align="right">0.7%</td>
<td align="right">313</td>
<td align="right">0.6%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">817</td>
<td align="right">1.5%</td>
<td align="right">707</td>
<td align="right">1.5%</td>
<td align="right">-13.5%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,331</td>
<td align="right">10.1%</td>
<td align="right">4,713</td>
<td align="right">9.7%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">103</td>
<td align="right">0.2%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">100</td>
<td align="right">0.2%</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,226</td>
<td align="right">14.8%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">23,707</td>
<td align="right">48.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,007</td>
<td align="right">11.4%</td>
<td align="right">5,989</td>
<td align="right">12.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">741</td>
<td align="right">1.5%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">729</td>
<td align="right">1.5%</td>
<td align="right">-0.1%</td>
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
<td align="right">112,724,681</td>
<td align="right">100.0%</td>
<td align="right">-0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">923,168,505</td>
<td align="right">56.8%</td>
<td align="right">912,924,574</td>
<td align="right">56.6%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">700,841,913</td>
<td align="right">43.2%</td>
<td align="right">698,778,064</td>
<td align="right">43.4%</td>
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
<td align="left">Success</td>
<td align="right">2,102</td>
<td align="right">1.1%</td>
<td align="right">1,360</td>
<td align="right">0.7%</td>
<td align="right">-35.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">182,264</td>
<td align="right">98.9%</td>
<td align="right">180,735</td>
<td align="right">99.3%</td>
<td align="right">-0.8%</td>
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
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">18,005</td>
<td align="right">10.0%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,011</td>
<td align="right">1.7%</td>
<td align="right">2,919</td>
<td align="right">1.6%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,662</td>
<td align="right">0.9%</td>
<td align="right">1,614</td>
<td align="right">0.9%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,313</td>
<td align="right">2.9%</td>
<td align="right">5,294</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">17,316</td>
<td align="right">9.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">86,613</td>
<td align="right">47.5%</td>
<td align="right">86,588</td>
<td align="right">47.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">48,931</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.0%</td>
<td align="right">68</td>
<td align="right">0.0%</td>
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
<td align="right">111,307,560</td>
<td align="right">2.2%</td>
<td align="right">105,609,816</td>
<td align="right">2.1%</td>
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
<td align="right">4,749,940,832</td>
<td align="right">92.7%</td>
<td align="right">4,623,757,017</td>
<td align="right">92.7%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">263,881,214</td>
<td align="right">5.1%</td>
<td align="right">259,579,631</td>
<td align="right">5.2%</td>
<td align="right">-1.6%</td>
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
<td align="right">2,149,067</td>
<td align="right">77.3%</td>
<td align="right">2,028,742</td>
<td align="right">76.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,822</td>
<td align="right">22.7%</td>
<td align="right">614,119</td>
<td align="right">23.2%</td>
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
<td align="left">set</td>
<td align="right">13,365</td>
<td align="right">2.1%</td>
<td align="right">7,140</td>
<td align="right">1.2%</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,638</td>
<td align="right">15.5%</td>
<td align="right">92,475</td>
<td align="right">15.1%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,584</td>
<td align="right">3.3%</td>
<td align="right">19,803</td>
<td align="right">3.2%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">77,672</td>
<td align="right">12.3%</td>
<td align="right">76,186</td>
<td align="right">12.4%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">133,084</td>
<td align="right">21.1%</td>
<td align="right">130,559</td>
<td align="right">21.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,070</td>
<td align="right">1.6%</td>
<td align="right">9,937</td>
<td align="right">1.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">380</td>
<td align="right">0.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,645</td>
<td align="right">40.9%</td>
<td align="right">257,307</td>
<td align="right">41.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">18,828</td>
<td align="right">3.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
<td align="right">1,420</td>
<td align="right">0.2%</td>
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
<td align="right">1,815,335</td>
<td align="right">0.1%</td>
<td align="right">568,116</td>
<td align="right">0.0%</td>
<td align="right">-68.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,247,391,068</td>
<td align="right">99.9%</td>
<td align="right">1,181,284,635</td>
<td align="right">100.0%</td>
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
<td align="right">1,001</td>
<td align="right">9.1%</td>
<td align="right">388</td>
<td align="right">5.2%</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">10,009</td>
<td align="right">90.9%</td>
<td align="right">7,114</td>
<td align="right">94.8%</td>
<td align="right">-28.9%</td>
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
<td align="right">766</td>
<td align="right">76.5%</td>
<td align="right">200</td>
<td align="right">51.5%</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.6%</td>
<td align="right">90</td>
<td align="right">23.2%</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">99</td>
<td align="right">9.9%</td>
<td align="right">98</td>
<td align="right">25.3%</td>
<td align="right">-1.0%</td>
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
<td align="right">1,501,278,082</td>
<td align="right">0.7%</td>
<td align="right">1,409,150,492</td>
<td align="right">0.7%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">8,771,412,176</td>
<td align="right">4.2%</td>
<td align="right">8,551,545,255</td>
<td align="right">4.1%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,742,149,153</td>
<td align="right">41.1%</td>
<td align="right">85,284,987,160</td>
<td align="right">41.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">113,889,659,862</td>
<td align="right">54.0%</td>
<td align="right">112,027,850,409</td>
<td align="right">54.0%</td>
<td align="right">-1.6%</td>
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
<td align="left">CALL</td>
<td align="right">175,982,846</td>
<td align="right">2.3%</td>
<td align="right">149,627,801</td>
<td align="right">2.0%</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">156,135,029</td>
<td align="right">2.0%</td>
<td align="right">141,192,656</td>
<td align="right">1.9%</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,815,497</td>
<td align="right">1.7%</td>
<td align="right">122,081,423</td>
<td align="right">1.6%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">822,826,896</td>
<td align="right">10.6%</td>
<td align="right">785,617,716</td>
<td align="right">10.3%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">511,614,467</td>
<td align="right">6.6%</td>
<td align="right">497,173,609</td>
<td align="right">6.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,881,214</td>
<td align="right">3.4%</td>
<td align="right">259,579,631</td>
<td align="right">3.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,468,431,096</td>
<td align="right">18.9%</td>
<td align="right">1,445,624,019</td>
<td align="right">18.9%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">2,805,883,724</td>
<td align="right">36.0%</td>
<td align="right">2,781,562,401</td>
<td align="right">36.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,841,913</td>
<td align="right">9.0%</td>
<td align="right">698,778,064</td>
<td align="right">9.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">545,743,587</td>
<td align="right">7.0%</td>
<td align="right">545,099,870</td>
<td align="right">7.1%</td>
<td align="right">-0.1%</td>
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
<td align="right">90,288,029</td>
<td align="right">6.0%</td>
<td align="right">77,636,086</td>
<td align="right">5.5%</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">82,033,846</td>
<td align="right">5.5%</td>
<td align="right">74,696,470</td>
<td align="right">5.3%</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,421,840</td>
<td align="right">3.3%</td>
<td align="right">45,150,525</td>
<td align="right">3.2%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,598,486</td>
<td align="right">17.8%</td>
<td align="right">249,995,427</td>
<td align="right">17.7%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,193,686</td>
<td align="right">5.7%</td>
<td align="right">82,365,905</td>
<td align="right">5.8%</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,228,613</td>
<td align="right">6.3%</td>
<td align="right">92,494,234</td>
<td align="right">6.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">54,679,482</td>
<td align="right">3.6%</td>
<td align="right">53,783,656</td>
<td align="right">3.8%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,062,622</td>
<td align="right">24.5%</td>
<td align="right">362,389,222</td>
<td align="right">25.7%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,935,984</td>
<td align="right">5.5%</td>
<td align="right">81,253,671</td>
<td align="right">5.8%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,026,306</td>
<td align="right">5.5%</td>
<td align="right">81,426,291</td>
<td align="right">5.8%</td>
<td align="right">-0.7%</td>
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
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,889</td>
<td align="right">0.0%</td>
<td align="right">2,930</td>
<td align="right">0.0%</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,924,658</td>
<td align="right">0.4%</td>
<td align="right">22,044,509</td>
<td align="right">0.3%</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">274,558,332</td>
<td align="right">4.1%</td>
<td align="right">257,501,561</td>
<td align="right">3.9%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">937,259,101</td>
<td align="right">14.0%</td>
<td align="right">903,618,563</td>
<td align="right">13.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">941,536,431</td>
<td align="right">14.0%</td>
<td align="right">907,894,110</td>
<td align="right">13.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,181,098,794</td>
<td align="right">77.2%</td>
<td align="right">5,044,300,846</td>
<td align="right">77.2%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,215,084</td>
<td align="right">3.9%</td>
<td align="right">254,449,898</td>
<td align="right">3.9%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,426,936,831</td>
<td align="right">80.9%</td>
<td align="right">5,291,793,079</td>
<td align="right">81.0%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,526,916,117</td>
<td align="right">22.8%</td>
<td align="right">1,489,171,254</td>
<td align="right">22.8%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,526,916,117</td>
<td align="right">22.8%</td>
<td align="right">1,489,171,254</td>
<td align="right">22.8%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,234,185</td>
<td align="right">1.1%</td>
<td align="right">69,680,143</td>
<td align="right">1.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">585,379,686</td>
<td align="right">8.7%</td>
<td align="right">581,277,144</td>
<td align="right">8.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,273,441</td>
<td align="right">0.1%</td>
<td align="right">4,272,617</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,402</td>
<td align="right">2.0%</td>
<td align="right">132,512,960</td>
<td align="right">2.0%</td>
<td align="right">-0.0%</td>
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
<td align="left">Method cache dunder hits</td>
<td align="right">2,393,361,432</td>
<td align="right"></td>
<td align="right">2,239,919,752</td>
<td align="right"></td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">51,985,795</td>
<td align="right"></td>
<td align="right">48,993,511</td>
<td align="right"></td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">25,121,025,451</td>
<td align="right">27.2%</td>
<td align="right">23,788,733,003</td>
<td align="right">26.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,242,733,816</td>
<td align="right"></td>
<td align="right">2,132,004,232</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">14,124,170,352</td>
<td align="right"></td>
<td align="right">13,445,977,077</td>
<td align="right"></td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">14,124,006,877</td>
<td align="right">71.8%</td>
<td align="right">13,445,920,315</td>
<td align="right">71.3%</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">67,543,992</td>
<td align="right"></td>
<td align="right">64,459,904</td>
<td align="right"></td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">1,874,650,449</td>
<td align="right">1.7%</td>
<td align="right">1,794,495,606</td>
<td align="right">1.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">51,830,715,684</td>
<td align="right">47.2%</td>
<td align="right">49,764,337,374</td>
<td align="right">46.9%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">22,855,910,510</td>
<td align="right">24.7%</td>
<td align="right">22,143,816,041</td>
<td align="right">24.8%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">31,401,908,728</td>
<td align="right">28.6%</td>
<td align="right">30,485,773,510</td>
<td align="right">28.7%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">24,660,681,157</td>
<td align="right">22.5%</td>
<td align="right">24,036,285,889</td>
<td align="right">22.7%</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">39,855,271,479</td>
<td align="right">43.1%</td>
<td align="right">38,964,447,396</td>
<td align="right">43.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,441,240</td>
<td align="right">2.6%</td>
<td align="right">4,344,903</td>
<td align="right">2.6%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">5,459,428,907</td>
<td align="right">27.8%</td>
<td align="right">5,343,373,371</td>
<td align="right">28.3%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">5,537,442,988</td>
<td align="right">28.2%</td>
<td align="right">5,420,332,878</td>
<td align="right">28.7%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,139,081,619</td>
<td align="right"></td>
<td align="right">6,018,344,704</td>
<td align="right"></td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">4,587,460,204</td>
<td align="right">5.0%</td>
<td align="right">4,506,463,634</td>
<td align="right">5.0%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,593,333</td>
<td align="right">0.4%</td>
<td align="right">70,582,946</td>
<td align="right">0.4%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">168,591,673</td>
<td align="right"></td>
<td align="right">166,821,411</td>
<td align="right"></td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,866</td>
<td align="right">0.3%</td>
<td align="right">471,009</td>
<td align="right">0.3%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,420,748</td>
<td align="right">0.0%</td>
<td align="right">6,376,561</td>
<td align="right">0.0%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">16,362,135</td>
<td align="right"></td>
<td align="right">16,264,437</td>
<td align="right"></td>
<td align="right">-0.6%</td>
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
<td align="right">365,026</td>
<td align="right">102,689,479</td>
<td align="right">9,472,354,525</td>
<td align="right">745,586,537</td>
<td align="right">764,508,749</td>
<td align="right">363,663</td>
<td align="right">102,027,445</td>
<td align="right">9,408,019,636</td>
<td align="right">735,543,745</td>
<td align="right">763,558,627</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,613,888,780</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,432</td>
<td align="right">5,613,869,568</td>
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
set bases
<details>
<summary>ⓘ</summary>

Setting the bases of a class, `cls.__bases__ = ...`
</details>
</td>
<td align="right">30</td>
<td align="right">22</td>
<td align="right">-26.7%</td>
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
<td align="right">29</td>
<td align="right">-21.6%</td>
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
<td align="right">22,592</td>
<td align="right">-0.2%</td>
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
<td align="right">2,458</td>
<td align="right">2,395</td>
<td align="right">-2.6%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-04-30
