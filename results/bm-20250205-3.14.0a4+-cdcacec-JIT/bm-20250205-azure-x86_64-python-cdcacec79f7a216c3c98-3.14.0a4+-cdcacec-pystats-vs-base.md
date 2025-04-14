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
<td align="right">5,760,532,271</td>
<td align="right">5,196,447</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">112,686,498</td>
<td align="right">1,194,074</td>
<td align="right">-98.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">62,369,174</td>
<td align="right">2,015,283</td>
<td align="right">-96.8%</td>
</tr>
<tr>
<td align="left">GET_ANEXT</td>
<td align="right">100,136,760</td>
<td align="right">6,000,000</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">1,476,458,780</td>
<td align="right">118,405,924</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">630,672,482</td>
<td align="right">51,726,195</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,720,907,554</td>
<td align="right">250,238,965</td>
<td align="right">-90.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">2,197,840,822</td>
<td align="right">234,703,077</td>
<td align="right">-89.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">1,756,315,414</td>
<td align="right">189,398,720</td>
<td align="right">-89.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">1,780,473</td>
<td align="right">207,638</td>
<td align="right">-88.3%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">566,124,654</td>
<td align="right">70,429,028</td>
<td align="right">-87.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">1,404,566,084</td>
<td align="right">178,421,635</td>
<td align="right">-87.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">195,030,358</td>
<td align="right">26,269,474</td>
<td align="right">-86.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">497,363,451</td>
<td align="right">67,805,869</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">3,494,522,157</td>
<td align="right">485,290,701</td>
<td align="right">-86.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">419,933,868</td>
<td align="right">58,609,123</td>
<td align="right">-86.0%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">2,145,206,070</td>
<td align="right">307,545,764</td>
<td align="right">-85.7%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">1,587,288,832</td>
<td align="right">228,685,215</td>
<td align="right">-85.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">1,276,705,031</td>
<td align="right">186,376,600</td>
<td align="right">-85.4%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">2,247,135,854</td>
<td align="right">329,956,509</td>
<td align="right">-85.3%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">370,701,792</td>
<td align="right">58,305,338</td>
<td align="right">-84.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">518,995,585</td>
<td align="right">87,928,901</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,662,971,099</td>
<td align="right">292,234,505</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">701,063,437</td>
<td align="right">133,580,583</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,357,293,220</td>
<td align="right">451,641,362</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">89,866,310</td>
<td align="right">18,660,317</td>
<td align="right">-79.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">340,636,372</td>
<td align="right">71,558,958</td>
<td align="right">-79.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">1,260,959,328</td>
<td align="right">265,807,399</td>
<td align="right">-78.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">156,807,836</td>
<td align="right">33,292,776</td>
<td align="right">-78.8%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">7,317,305,458</td>
<td align="right">1,613,339,211</td>
<td align="right">-78.0%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">668,558,857</td>
<td align="right">153,985,605</td>
<td align="right">-77.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">154,839,605</td>
<td align="right">36,485,804</td>
<td align="right">-76.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">1,700,144,611</td>
<td align="right">405,136,913</td>
<td align="right">-76.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">2,755,658,955</td>
<td align="right">658,346,311</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,053,436,108</td>
<td align="right">251,870,318</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">379,229,800</td>
<td align="right">95,288,221</td>
<td align="right">-74.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">259,536,518</td>
<td align="right">65,579,074</td>
<td align="right">-74.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">1,037,815,150</td>
<td align="right">265,156,127</td>
<td align="right">-74.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">1,079,519,523</td>
<td align="right">276,083,853</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">538,391,959</td>
<td align="right">137,982,326</td>
<td align="right">-74.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">5,783,467,664</td>
<td align="right">1,487,759,452</td>
<td align="right">-74.3%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">131,417,726</td>
<td align="right">34,315,226</td>
<td align="right">-73.9%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">225,536,086</td>
<td align="right">61,097,919</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,562,016,940</td>
<td align="right">698,064,106</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">1,116,751,099</td>
<td align="right">307,060,851</td>
<td align="right">-72.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">2,536,303,316</td>
<td align="right">708,533,551</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">11,048,102,964</td>
<td align="right">3,118,757,526</td>
<td align="right">-71.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">13,493,932,844</td>
<td align="right">3,838,504,966</td>
<td align="right">-71.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">441,545,521</td>
<td align="right">125,933,821</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">781,353,434</td>
<td align="right">223,347,078</td>
<td align="right">-71.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">357,020,427</td>
<td align="right">103,695,906</td>
<td align="right">-71.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">918,401,902</td>
<td align="right">270,865,020</td>
<td align="right">-70.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">10,735,179,660</td>
<td align="right">3,211,532,325</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">504,577,774</td>
<td align="right">153,395,141</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">57,732,580</td>
<td align="right">17,774,426</td>
<td align="right">-69.2%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">76,086,856</td>
<td align="right">23,563,769</td>
<td align="right">-69.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">115,161,906</td>
<td align="right">36,581,508</td>
<td align="right">-68.2%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">35,910,996</td>
<td align="right">11,651,457</td>
<td align="right">-67.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">74,955,594</td>
<td align="right">25,131,993</td>
<td align="right">-66.5%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">593,303,397</td>
<td align="right">206,464,085</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">122,480,869</td>
<td align="right">42,627,187</td>
<td align="right">-65.2%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">62,253,442</td>
<td align="right">21,757,239</td>
<td align="right">-65.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">520,153,589</td>
<td align="right">181,993,491</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">271,020,978</td>
<td align="right">98,781,012</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,911,378</td>
<td align="right">56,843,777</td>
<td align="right">-63.5%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">1,210,799,069</td>
<td align="right">442,601,379</td>
<td align="right">-63.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">37,483,133,654</td>
<td align="right">13,859,071,575</td>
<td align="right">-63.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">211,103,004</td>
<td align="right">79,975,163</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">93,580,928</td>
<td align="right">35,480,261</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">792,630,254</td>
<td align="right">300,558,758</td>
<td align="right">-62.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">127,568,827</td>
<td align="right">49,176,342</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">264,337,000</td>
<td align="right">103,238,470</td>
<td align="right">-60.9%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">67,299,595</td>
<td align="right">26,873,142</td>
<td align="right">-60.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">815,016,714</td>
<td align="right">325,719,490</td>
<td align="right">-60.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">2,099,815,524</td>
<td align="right">851,272,219</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">814,219,545</td>
<td align="right">330,452,293</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">6,152,500</td>
<td align="right">2,573,060</td>
<td align="right">-58.2%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">403,675,452</td>
<td align="right">169,187,431</td>
<td align="right">-58.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">6,509,594,727</td>
<td align="right">2,791,022,136</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">23,493,544</td>
<td align="right">10,301,766</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">388,807,804</td>
<td align="right">172,202,213</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">72,566,184</td>
<td align="right">32,156,035</td>
<td align="right">-55.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">80,690,725</td>
<td align="right">36,277,936</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">288,033,519</td>
<td align="right">129,774,665</td>
<td align="right">-54.9%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">1,379,399,142</td>
<td align="right">626,345,850</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">320,165,228</td>
<td align="right">145,451,436</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">1,536,868,792</td>
<td align="right">715,417,032</td>
<td align="right">-53.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">365,456,552</td>
<td align="right">171,557,615</td>
<td align="right">-53.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">57,316,657</td>
<td align="right">27,216,916</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">242,354,546</td>
<td align="right">115,093,564</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">332,402,857</td>
<td align="right">159,359,565</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">1,263,886,569</td>
<td align="right">607,565,476</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">3,874,650,871</td>
<td align="right">1,931,215,963</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">7,706,625</td>
<td align="right">3,844,091</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">9,742,691</td>
<td align="right">4,866,911</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">4,850,597,034</td>
<td align="right">2,481,753,227</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">2,485,239,198</td>
<td align="right">1,277,833,905</td>
<td align="right">-48.6%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,068,564</td>
<td align="right">97,042,392</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">292,955,030</td>
<td align="right">157,581,731</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">175,326,729</td>
<td align="right">94,465,897</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">8,340,298</td>
<td align="right">4,497,055</td>
<td align="right">-46.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,637,951,047</td>
<td align="right">902,537,734</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">3,210,783,159</td>
<td align="right">1,781,960,847</td>
<td align="right">-44.5%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">168,303,559</td>
<td align="right">95,114,229</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">15,697,691</td>
<td align="right">9,047,399</td>
<td align="right">-42.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">115,843,117</td>
<td align="right">68,049,010</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">6,308,074,603</td>
<td align="right">3,848,954,059</td>
<td align="right">-39.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">183,156,569</td>
<td align="right">112,003,170</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">99,004,341</td>
<td align="right">61,473,298</td>
<td align="right">-37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">850,842,769</td>
<td align="right">531,850,450</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">331,226,298</td>
<td align="right">209,445,507</td>
<td align="right">-36.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">226,568,587</td>
<td align="right">143,524,900</td>
<td align="right">-36.7%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">842,242,920</td>
<td align="right">539,258,087</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">3,347,783,225</td>
<td align="right">2,162,395,535</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">984,079,550</td>
<td align="right">640,011,302</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">498,506,094</td>
<td align="right">328,703,376</td>
<td align="right">-34.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">94,912,690</td>
<td align="right">65,068,200</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">69,516,520</td>
<td align="right">48,216,310</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">502,916,862</td>
<td align="right">350,886,343</td>
<td align="right">-30.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">320,514,683</td>
<td align="right">224,589,134</td>
<td align="right">-29.9%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">3,175,027,122</td>
<td align="right">2,312,505,868</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">188,535,188</td>
<td align="right">139,910,065</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">571,423,924</td>
<td align="right">428,553,005</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">156,397,455</td>
<td align="right">119,224,038</td>
<td align="right">-23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">76,989,262</td>
<td align="right">58,922,530</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,828,712</td>
<td align="right">1,439,859</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">972,651,078</td>
<td align="right">776,910,032</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">138,454,320</td>
<td align="right">111,568,561</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">101,065,364</td>
<td align="right">82,014,742</td>
<td align="right">-18.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">244,473,763</td>
<td align="right">214,616,869</td>
<td align="right">-12.2%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">5,425,161,299</td>
<td align="right">4,817,867,039</td>
<td align="right">-11.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,533,924</td>
<td align="right">4,050,220</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">63,886,805</td>
<td align="right">57,294,087</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">77,226,775</td>
<td align="right">69,841,666</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">72,978,979</td>
<td align="right">66,810,581</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">348,279,659</td>
<td align="right">320,220,891</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,164,252</td>
<td align="right">5,803,810</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">416,816,444</td>
<td align="right">392,944,597</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">11,204,107</td>
<td align="right">10,604,426</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">73,332,052</td>
<td align="right">69,696,984</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">83,649,249</td>
<td align="right">79,594,702</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,870,086</td>
<td align="right">19,916,051</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,200,570</td>
<td align="right">20,246,535</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,200,590</td>
<td align="right">20,246,555</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,795,496</td>
<td align="right">3,644,616</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,113,124,433</td>
<td align="right">1,071,841,525</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,564,476</td>
<td align="right">13,244,862</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,650</td>
<td align="right">2,708</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,114,209</td>
<td align="right">3,048,559</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">68,017,012</td>
<td align="right">66,897,701</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">172,683,388</td>
<td align="right">170,068,018</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,582,866</td>
<td align="right">9,445,341</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">8,965,669</td>
<td align="right">9,036,348</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,629,451,860</td>
<td align="right">1,618,896,825</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">403,202</td>
<td align="right">405,591</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,579,808</td>
<td align="right">60,228,778</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,626,432</td>
<td align="right">180,132,658</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">101,012,072</td>
<td align="right">100,816,846</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,141</td>
<td align="right">5,135</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,747</td>
<td align="right">33,713</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,763</td>
<td align="right">120,861</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,417,134</td>
<td align="right">242,234,167</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,149</td>
<td align="right">133,123</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,758,384</td>
<td align="right">14,760,217</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,613</td>
<td align="right">773,631</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,924</td>
<td align="right">1,645,929</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,900</td>
<td align="right">302,607,900</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,678</td>
<td align="right">128,851,678</td>
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
<td align="right">41,964,793</td>
<td align="right">41,964,793</td>
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
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,976,841</td>
<td align="right">8,976,841</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_ASYNC_FOR</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AITER</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">781,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,734</td>
<td align="right">98,734</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,552</td>
<td align="right">84,552</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">59,727</td>
<td align="right">59,727</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,147</td>
<td align="right">57,147</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">56,770</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,546</td>
<td align="right">17,546</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,321</td>
<td align="right">5,321</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,896</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,620</td>
<td align="right">3,620</td>
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
<td align="right">151</td>
<td align="right">151</td>
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
<td align="left">ENTER_EXECUTOR</td>
<td align="right"></td>
<td align="right">2,034,899,280</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right"></td>
<td align="right">171,230,702</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right"></td>
<td align="right">18,277,839</td>
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
<td align="right">813,802,647</td>
<td align="right">9.6%</td>
<td align="right">330,290,513</td>
<td align="right">4.1%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,038,636</td>
<td align="right">0.6%</td>
<td align="right">51,004,210</td>
<td align="right">0.6%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,643,065,853</td>
<td align="right">89.8%</td>
<td align="right">7,638,285,230</td>
<td align="right">95.2%</td>
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
<td align="right">408,297</td>
<td align="right">28.8%</td>
<td align="right">153,189</td>
<td align="right">13.6%</td>
<td align="right">-62.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">1,009,281</td>
<td align="right">71.2%</td>
<td align="right">970,903</td>
<td align="right">86.4%</td>
<td align="right">-3.8%</td>
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
<td align="left">xor int</td>
<td align="right">85,543</td>
<td align="right">21.0%</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">23,513</td>
<td align="right">5.8%</td>
<td align="right">5,459</td>
<td align="right">3.6%</td>
<td align="right">-76.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">11,588</td>
<td align="right">2.8%</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">-75.4%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">74,212</td>
<td align="right">18.2%</td>
<td align="right">18,488</td>
<td align="right">12.1%</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">8,210</td>
<td align="right">2.0%</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">-71.5%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">2,678</td>
<td align="right">0.7%</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">-68.8%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">19,451</td>
<td align="right">4.8%</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">1,252</td>
<td align="right">0.3%</td>
<td align="right">488</td>
<td align="right">0.3%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">43,418</td>
<td align="right">10.6%</td>
<td align="right">17,764</td>
<td align="right">11.6%</td>
<td align="right">-59.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">43,792</td>
<td align="right">10.7%</td>
<td align="right">20,068</td>
<td align="right">13.1%</td>
<td align="right">-54.2%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">399</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">8,513</td>
<td align="right">2.1%</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">-50.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">33,978</td>
<td align="right">8.3%</td>
<td align="right">19,836</td>
<td align="right">12.9%</td>
<td align="right">-41.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">36,624</td>
<td align="right">9.0%</td>
<td align="right">23,468</td>
<td align="right">15.3%</td>
<td align="right">-35.9%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">7,224</td>
<td align="right">1.8%</td>
<td align="right">5,716</td>
<td align="right">3.7%</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">2,036</td>
<td align="right">0.5%</td>
<td align="right">1,995</td>
<td align="right">1.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,154</td>
<td align="right">0.8%</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">628</td>
<td align="right">0.2%</td>
<td align="right">626</td>
<td align="right">0.4%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.3%</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.1%</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
<td align="right">0.1%</td>
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
<td align="right">182,068,564</td>
<td align="right">100.0%</td>
<td align="right">97,042,392</td>
<td align="right">100.0%</td>
<td align="right">-46.7%</td>
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
<td align="right">2,356,677,027</td>
<td align="right">30.0%</td>
<td align="right">451,490,199</td>
<td align="right">7.6%</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,928,443</td>
<td align="right">0.1%</td>
<td align="right">5,824,977</td>
<td align="right">0.1%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,504,810,447</td>
<td align="right">70.0%</td>
<td align="right">5,468,662,049</td>
<td align="right">92.3%</td>
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
<td align="right">607,926</td>
<td align="right">83.5%</td>
<td align="right">141,924</td>
<td align="right">54.4%</td>
<td align="right">-76.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">119,918</td>
<td align="right">16.5%</td>
<td align="right">118,914</td>
<td align="right">45.6%</td>
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
<td align="left">list slice</td>
<td align="right">193,733</td>
<td align="right">31.9%</td>
<td align="right">7,100</td>
<td align="right">5.0%</td>
<td align="right">-96.3%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">28,487</td>
<td align="right">4.7%</td>
<td align="right">3,675</td>
<td align="right">2.6%</td>
<td align="right">-87.1%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">121,418</td>
<td align="right">20.0%</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">-86.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">197,055</td>
<td align="right">32.4%</td>
<td align="right">59,665</td>
<td align="right">42.0%</td>
<td align="right">-69.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">47,128</td>
<td align="right">7.8%</td>
<td align="right">35,055</td>
<td align="right">24.7%</td>
<td align="right">-25.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">1,012</td>
<td align="right">0.2%</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">-24.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">0.6%</td>
<td align="right">3,607</td>
<td align="right">2.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,450</td>
<td align="right">2.0%</td>
<td align="right">12,446</td>
<td align="right">8.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">0.5%</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.0%</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">21</td>
<td align="right">0.0%</td>
<td align="right">21</td>
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
<td align="right">154,898,940</td>
<td align="right">1.4%</td>
<td align="right">126,923,324</td>
<td align="right">1.1%</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">152,207,450</td>
<td align="right">1.4%</td>
<td align="right">124,759,641</td>
<td align="right">1.1%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,118,048,921</td>
<td align="right">98.6%</td>
<td align="right">11,082,378,253</td>
<td align="right">98.9%</td>
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
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
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
<td align="right">3,094,246</td>
<td align="right">100.0%</td>
<td align="right">2,568,828</td>
<td align="right">100.0%</td>
<td align="right">-17.0%</td>
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
<td align="left">init not python</td>
<td align="right">267</td>
<td align="right">59.9%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">7.5%</td>
</tr>
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
<td align="right">684,424</td>
<td align="right">97.1%</td>
<td align="right">684,422</td>
<td align="right">97.1%</td>
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
<td align="right">583,846</td>
<td align="right">82.9%</td>
<td align="right">583,846</td>
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
<td align="right">20,065</td>
<td align="right">99.4%</td>
<td align="right">20,165</td>
<td align="right">99.4%</td>
<td align="right">0.5%</td>
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
<td align="right">518,765,169</td>
<td align="right">10.3%</td>
<td align="right">87,812,007</td>
<td align="right">1.9%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,388,970</td>
<td align="right">0.0%</td>
<td align="right">1,155,459</td>
<td align="right">0.0%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,530,094,005</td>
<td align="right">89.7%</td>
<td align="right">4,515,246,999</td>
<td align="right">98.1%</td>
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
<td align="right">212,465</td>
<td align="right">82.9%</td>
<td align="right">98,676</td>
<td align="right">71.2%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">43,834</td>
<td align="right">17.1%</td>
<td align="right">39,823</td>
<td align="right">28.8%</td>
<td align="right">-9.2%</td>
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
<td align="right">90,859</td>
<td align="right">42.8%</td>
<td align="right">4,551</td>
<td align="right">4.6%</td>
<td align="right">-95.0%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,822</td>
<td align="right">3.2%</td>
<td align="right">364</td>
<td align="right">0.4%</td>
<td align="right">-94.7%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,998</td>
<td align="right">0.9%</td>
<td align="right">927</td>
<td align="right">0.9%</td>
<td align="right">-53.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">11,954</td>
<td align="right">5.6%</td>
<td align="right">6,433</td>
<td align="right">6.5%</td>
<td align="right">-46.2%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">13,686</td>
<td align="right">6.4%</td>
<td align="right">8,478</td>
<td align="right">8.6%</td>
<td align="right">-38.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">45,651</td>
<td align="right">21.5%</td>
<td align="right">36,864</td>
<td align="right">37.4%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,367</td>
<td align="right">0.6%</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">356</td>
<td align="right">0.2%</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">1,004</td>
<td align="right">0.5%</td>
<td align="right">984</td>
<td align="right">1.0%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,367</td>
<td align="right">11.0%</td>
<td align="right">23,173</td>
<td align="right">23.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,762</td>
<td align="right">3.7%</td>
<td align="right">7,708</td>
<td align="right">7.8%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">3.6%</td>
<td align="right">7,639</td>
<td align="right">7.7%</td>
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
<td align="right">155,850,041</td>
<td align="right">6.6%</td>
<td align="right">56,806,151</td>
<td align="right">2.5%</td>
<td align="right">-63.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,195,943,948</td>
<td align="right">93.3%</td>
<td align="right">2,188,418,794</td>
<td align="right">97.4%</td>
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
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
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
<td align="right">59,276</td>
<td align="right">60.8%</td>
<td align="right">35,365</td>
<td align="right">47.9%</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,235</td>
<td align="right">39.2%</td>
<td align="right">38,435</td>
<td align="right">52.1%</td>
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
<td align="left">str</td>
<td align="right">21,374</td>
<td align="right">36.1%</td>
<td align="right">9,173</td>
<td align="right">25.9%</td>
<td align="right">-57.1%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">14,625</td>
<td align="right">24.7%</td>
<td align="right">7,174</td>
<td align="right">20.3%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,685</td>
<td align="right">19.7%</td>
<td align="right">7,818</td>
<td align="right">22.1%</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,592</td>
<td align="right">19.6%</td>
<td align="right">11,200</td>
<td align="right">31.7%</td>
<td align="right">-3.4%</td>
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
<td align="right">1,476,023,345</td>
<td align="right">29.0%</td>
<td align="right">118,306,642</td>
<td align="right">15.7%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">3,445,265,585</td>
<td align="right">67.7%</td>
<td align="right">601,341,647</td>
<td align="right">80.0%</td>
<td align="right">-82.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">163,994,224</td>
<td align="right">3.2%</td>
<td align="right">32,375,897</td>
<td align="right">4.3%</td>
<td align="right">-80.3%</td>
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
<td align="right">3,099,133</td>
<td align="right">87.8%</td>
<td align="right">615,793</td>
<td align="right">86.7%</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">430,355</td>
<td align="right">12.2%</td>
<td align="right">94,212</td>
<td align="right">13.3%</td>
<td align="right">-78.1%</td>
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
<td align="right">172,145</td>
<td align="right">40.0%</td>
<td align="right">4,493</td>
<td align="right">4.8%</td>
<td align="right">-97.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">83,979</td>
<td align="right">19.5%</td>
<td align="right">3,032</td>
<td align="right">3.2%</td>
<td align="right">-96.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">34,993</td>
<td align="right">8.1%</td>
<td align="right">5,913</td>
<td align="right">6.3%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">11,325</td>
<td align="right">2.6%</td>
<td align="right">2,247</td>
<td align="right">2.4%</td>
<td align="right">-80.2%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">734</td>
<td align="right">0.2%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">-76.3%</td>
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
<td align="left">reversed list</td>
<td align="right">3,139</td>
<td align="right">0.7%</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">-69.9%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">18,261</td>
<td align="right">4.2%</td>
<td align="right">6,164</td>
<td align="right">6.5%</td>
<td align="right">-66.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">3,390</td>
<td align="right">0.8%</td>
<td align="right">1,547</td>
<td align="right">1.6%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">19,467</td>
<td align="right">4.5%</td>
<td align="right">10,750</td>
<td align="right">11.4%</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">4,601</td>
<td align="right">1.1%</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">6,911</td>
<td align="right">1.6%</td>
<td align="right">4,546</td>
<td align="right">4.8%</td>
<td align="right">-34.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">70,013</td>
<td align="right">16.3%</td>
<td align="right">51,073</td>
<td align="right">54.2%</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">174</td>
<td align="right">0.0%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">-23.0%</td>
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
<td align="right">848,996,720</td>
<td align="right">6.1%</td>
<td align="right">530,226,034</td>
<td align="right">4.0%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">871,304,204</td>
<td align="right">6.3%</td>
<td align="right">639,538,140</td>
<td align="right">4.8%</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,173,845,724</td>
<td align="right">87.6%</td>
<td align="right">12,074,789,315</td>
<td align="right">91.2%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,404,473</td>
<td align="right">0.0%</td>
<td align="right">1,404,473</td>
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
<td align="right">565,103</td>
<td align="right">3.3%</td>
<td align="right">355,053</td>
<td align="right">2.8%</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">16,520,865</td>
<td align="right">96.7%</td>
<td align="right">12,153,130</td>
<td align="right">97.2%</td>
<td align="right">-26.4%</td>
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
<td align="right">81,350</td>
<td align="right">14.4%</td>
<td align="right">40,703</td>
<td align="right">11.5%</td>
<td align="right">-50.0%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">57,750</td>
<td align="right">10.2%</td>
<td align="right">38,195</td>
<td align="right">10.8%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">1,180</td>
<td align="right">0.2%</td>
<td align="right">857</td>
<td align="right">0.2%</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">6,046</td>
<td align="right">1.1%</td>
<td align="right">4,938</td>
<td align="right">1.4%</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">9,130</td>
<td align="right">1.6%</td>
<td align="right">7,940</td>
<td align="right">2.2%</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">16,619</td>
<td align="right">2.9%</td>
<td align="right">14,512</td>
<td align="right">4.1%</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,729</td>
<td align="right">0.5%</td>
<td align="right">2,406</td>
<td align="right">0.7%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,802</td>
<td align="right">0.3%</td>
<td align="right">1,607</td>
<td align="right">0.5%</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">66,190</td>
<td align="right">11.7%</td>
<td align="right">60,071</td>
<td align="right">16.9%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">25,271</td>
<td align="right">4.5%</td>
<td align="right">23,798</td>
<td align="right">6.7%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,584</td>
<td align="right">0.3%</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,088</td>
<td align="right">0.9%</td>
<td align="right">5,086</td>
<td align="right">1.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.1%</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
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
<td align="right">0.1%</td>
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
<td align="right">9,131,197,738</td>
<td align="right">99.8%</td>
<td align="right">3,758,312,363</td>
<td align="right">99.6%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">53,151</td>
<td align="right">0.0%</td>
<td align="right">52,555</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,768</td>
<td align="right">0.2%</td>
<td align="right">14,622,698</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">136,383</td>
<td align="right">100.0%</td>
<td align="right">138,286</td>
<td align="right">100.0%</td>
<td align="right">1.4%</td>
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
<td align="right">255</td>
<td align="right">0.0%</td>
<td align="right">253</td>
<td align="right">0.0%</td>
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
<td align="right">63,694,017</td>
<td align="right">100.0%</td>
<td align="right">64,084,389</td>
<td align="right">100.0%</td>
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
<td align="left">Success</td>
<td align="right">2,395</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="right">593,288,686</td>
<td align="right">82.2%</td>
<td align="right">593,288,753</td>
<td align="right">82.2%</td>
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
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
<td align="right">128,816,907</td>
<td align="right">17.8%</td>
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
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">651</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,392</td>
<td align="right">98.1%</td>
<td align="right">34,392</td>
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
<td align="right">71.1%</td>
<td align="right">24,440</td>
<td align="right">71.1%</td>
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
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">3,261</td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">732</td>
<td align="right">2.1%</td>
<td align="right">732</td>
<td align="right">2.1%</td>
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
<td align="right">77,133,431</td>
<td align="right">3.8%</td>
<td align="right">69,748,540</td>
<td align="right">3.4%</td>
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
<td align="right">116,579,238</td>
<td align="right">5.7%</td>
<td align="right">114,603,408</td>
<td align="right">5.7%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,849,128,231</td>
<td align="right">90.5%</td>
<td align="right">1,842,119,647</td>
<td align="right">90.9%</td>
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
<td align="left">Failure</td>
<td align="right">52,770</td>
<td align="right">2.3%</td>
<td align="right">50,974</td>
<td align="right">2.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,239,418</td>
<td align="right">97.7%</td>
<td align="right">2,203,803</td>
<td align="right">97.7%</td>
<td align="right">-1.6%</td>
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
<td align="right">271,985</td>
<td align="right">515.4%</td>
<td align="right">135,728</td>
<td align="right">266.3%</td>
<td align="right">-50.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">6,033</td>
<td align="right">11.4%</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">743</td>
<td align="right">1.4%</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,322</td>
<td align="right">10.1%</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,476</td>
<td align="right">46.4%</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,356</td>
<td align="right">6.4%</td>
<td align="right">3,352</td>
<td align="right">6.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">14.5%</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.5%</td>
<td align="right">810</td>
<td align="right">1.6%</td>
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
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">361</td>
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
<td align="right">112,686,498</td>
<td align="right">100.0%</td>
<td align="right">1,194,074</td>
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
<td align="right">700,879,100</td>
<td align="right">43.2%</td>
<td align="right">133,534,647</td>
<td align="right">12.7%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">923,142,861</td>
<td align="right">56.8%</td>
<td align="right">918,978,195</td>
<td align="right">87.3%</td>
<td align="right">-0.5%</td>
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
<td align="right">182,299</td>
<td align="right">98.9%</td>
<td align="right">43,782</td>
<td align="right">95.2%</td>
<td align="right">-76.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,078</td>
<td align="right">1.1%</td>
<td align="right">2,194</td>
<td align="right">4.8%</td>
<td align="right">5.6%</td>
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
<td align="right">0.8%</td>
<td align="right">-99.6%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">5,309</td>
<td align="right">2.9%</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">-95.6%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">48,931</td>
<td align="right">26.8%</td>
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">-83.4%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">1,681</td>
<td align="right">0.9%</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">-70.2%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">19,343</td>
<td align="right">10.6%</td>
<td align="right">14,757</td>
<td align="right">33.7%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">17,323</td>
<td align="right">9.5%</td>
<td align="right">16,705</td>
<td align="right">38.2%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,031</td>
<td align="right">1.7%</td>
<td align="right">3,031</td>
<td align="right">6.9%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">112,463,174</td>
<td align="right">2.2%</td>
<td align="right">40,867,482</td>
<td align="right">0.9%</td>
<td align="right">-63.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">263,655,807</td>
<td align="right">5.1%</td>
<td align="right">102,775,010</td>
<td align="right">2.2%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,744,282,813</td>
<td align="right">92.6%</td>
<td align="right">4,525,163,897</td>
<td align="right">96.9%</td>
<td align="right">-4.6%</td>
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
<td align="right">2,169,937</td>
<td align="right">77.5%</td>
<td align="right">819,743</td>
<td align="right">66.5%</td>
<td align="right">-62.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">631,651</td>
<td align="right">22.5%</td>
<td align="right">413,294</td>
<td align="right">33.5%</td>
<td align="right">-34.6%</td>
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
<td align="left">mapping</td>
<td align="right">77,641</td>
<td align="right">12.3%</td>
<td align="right">8,622</td>
<td align="right">2.1%</td>
<td align="right">-88.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">132,987</td>
<td align="right">21.1%</td>
<td align="right">16,411</td>
<td align="right">4.0%</td>
<td align="right">-87.7%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">18,878</td>
<td align="right">3.0%</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">10,055</td>
<td align="right">1.6%</td>
<td align="right">5,694</td>
<td align="right">1.4%</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">20,552</td>
<td align="right">3.3%</td>
<td align="right">13,473</td>
<td align="right">3.3%</td>
<td align="right">-34.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">13,326</td>
<td align="right">2.1%</td>
<td align="right">12,366</td>
<td align="right">3.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">97,674</td>
<td align="right">15.5%</td>
<td align="right">94,066</td>
<td align="right">22.8%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">258,652</td>
<td align="right">40.9%</td>
<td align="right">256,179</td>
<td align="right">62.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">1,816,268</td>
<td align="right">0.1%</td>
<td align="right">1,427,465</td>
<td align="right">0.1%</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,247,394,360</td>
<td align="right">99.9%</td>
<td align="right">1,232,771,815</td>
<td align="right">99.9%</td>
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
<td align="right">991</td>
<td align="right">7.9%</td>
<td align="right">873</td>
<td align="right">7.0%</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,533</td>
<td align="right">92.1%</td>
<td align="right">11,601</td>
<td align="right">93.0%</td>
<td align="right">0.6%</td>
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
<td align="right">764</td>
<td align="right">77.1%</td>
<td align="right">646</td>
<td align="right">74.0%</td>
<td align="right">-15.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">13.7%</td>
<td align="right">136</td>
<td align="right">15.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">9.2%</td>
<td align="right">91</td>
<td align="right">10.4%</td>
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
<td align="right">7,657,068,940</td>
<td align="right">3.6%</td>
<td align="right">2,127,600,806</td>
<td align="right">2.6%</td>
<td align="right">-72.2%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">86,720,431,867</td>
<td align="right">41.1%</td>
<td align="right">30,337,435,584</td>
<td align="right">37.8%</td>
<td align="right">-65.0%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">115,373,286,137</td>
<td align="right">54.6%</td>
<td align="right">46,853,566,789</td>
<td align="right">58.3%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,482,296,457</td>
<td align="right">0.7%</td>
<td align="right">1,015,024,038</td>
<td align="right">1.3%</td>
<td align="right">-31.5%</td>
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
<td align="right">1,476,023,345</td>
<td align="right">18.9%</td>
<td align="right">118,306,642</td>
<td align="right">5.3%</td>
<td align="right">-92.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">518,765,169</td>
<td align="right">6.6%</td>
<td align="right">87,812,007</td>
<td align="right">3.9%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">700,879,100</td>
<td align="right">9.0%</td>
<td align="right">133,534,647</td>
<td align="right">5.9%</td>
<td align="right">-80.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">2,356,677,027</td>
<td align="right">30.2%</td>
<td align="right">451,490,199</td>
<td align="right">20.1%</td>
<td align="right">-80.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">263,655,807</td>
<td align="right">3.4%</td>
<td align="right">102,775,010</td>
<td align="right">4.6%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">813,802,647</td>
<td align="right">10.4%</td>
<td align="right">330,290,513</td>
<td align="right">14.7%</td>
<td align="right">-59.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">182,068,564</td>
<td align="right">2.3%</td>
<td align="right">97,042,392</td>
<td align="right">4.3%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">848,996,720</td>
<td align="right">10.9%</td>
<td align="right">530,226,034</td>
<td align="right">23.6%</td>
<td align="right">-37.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">152,207,450</td>
<td align="right">2.0%</td>
<td align="right">124,759,641</td>
<td align="right">5.5%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">155,850,041</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">128,816,907</td>
<td align="right">5.7%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">266,986,901</td>
<td align="right">18.0%</td>
<td align="right">183,330,686</td>
<td align="right">18.1%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">368,041,142</td>
<td align="right">24.8%</td>
<td align="right">252,813,499</td>
<td align="right">24.9%</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">90,677,494</td>
<td align="right">6.1%</td>
<td align="right">75,732,667</td>
<td align="right">7.5%</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">82,380,128</td>
<td align="right">5.6%</td>
<td align="right">69,007,007</td>
<td align="right">6.8%</td>
<td align="right">-16.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">86,869,982</td>
<td align="right">5.9%</td>
<td align="right">74,459,967</td>
<td align="right">7.3%</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,260,202</td>
<td align="right">6.4%</td>
<td align="right">92,967,816</td>
<td align="right">9.2%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">82,008,512</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">81,907,452</td>
<td align="right">5.5%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">55,295,828</td>
<td align="right">3.7%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">49,780,851</td>
<td align="right">3.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,418,465</td>
<td align="right">2.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21,600,057</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">21,241,544</td>
<td align="right">2.1%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,873,003</td>
<td align="right">2.1%</td>
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
<td align="right">4,273,442</td>
<td align="right">0.1%</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">-50.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,120,283,419</td>
<td align="right">75.8%</td>
<td align="right">5,057,802,447</td>
<td align="right">75.7%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">678,736,010</td>
<td align="right">10.0%</td>
<td align="right">670,459,190</td>
<td align="right">10.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,651,988</td>
<td align="right">1.1%</td>
<td align="right">71,102,174</td>
<td align="right">1.1%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,633,945,270</td>
<td align="right">24.2%</td>
<td align="right">1,623,546,547</td>
<td align="right">24.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,633,945,270</td>
<td align="right">24.2%</td>
<td align="right">1,623,546,547</td>
<td align="right">24.3%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,482,285,460</td>
<td align="right">81.2%</td>
<td align="right">5,450,545,078</td>
<td align="right">81.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">955,209,260</td>
<td align="right">14.1%</td>
<td align="right">953,087,357</td>
<td align="right">14.3%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,368,064</td>
<td align="right">4.1%</td>
<td align="right">279,256,991</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,414,572</td>
<td align="right">3.9%</td>
<td align="right">261,407,730</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">950,931,922</td>
<td align="right">14.1%</td>
<td align="right">950,955,214</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,595</td>
<td align="right">0.4%</td>
<td align="right">24,922,305</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">3,896</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,139</td>
<td align="right">2.0%</td>
<td align="right">132,513,139</td>
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
<td align="right">25,405,855,378</td>
<td align="right">16.4%</td>
<td align="right">77,331,415,411</td>
<td align="right">48.2%</td>
<td align="right">204.4%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">33,083,880,831</td>
<td align="right">17.3%</td>
<td align="right">82,810,838,105</td>
<td align="right">41.1%</td>
<td align="right">150.3%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">23,847,217,375</td>
<td align="right">12.5%</td>
<td align="right">54,616,524,408</td>
<td align="right">27.1%</td>
<td align="right">129.0%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">21,988,971,390</td>
<td align="right">14.2%</td>
<td align="right">38,347,677,862</td>
<td align="right">23.9%</td>
<td align="right">74.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">27,488,830,437</td>
<td align="right">17.8%</td>
<td align="right">8,892,505,517</td>
<td align="right">5.5%</td>
<td align="right">-67.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">45,501,375,588</td>
<td align="right">23.8%</td>
<td align="right">16,467,686,101</td>
<td align="right">8.2%</td>
<td align="right">-63.8%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">79,635,497,702</td>
<td align="right">51.5%</td>
<td align="right">35,846,816,607</td>
<td align="right">22.3%</td>
<td align="right">-55.0%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">89,044,393,228</td>
<td align="right">46.5%</td>
<td align="right">47,386,833,134</td>
<td align="right">23.5%</td>
<td align="right">-46.8%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">9,852,981</td>
<td align="right"></td>
<td align="right">8,280,232</td>
<td align="right"></td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">80,580,676</td>
<td align="right"></td>
<td align="right">69,178,738</td>
<td align="right"></td>
<td align="right">-14.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">71,536,508</td>
<td align="right"></td>
<td align="right">61,707,195</td>
<td align="right"></td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">475,376</td>
<td align="right">0.3%</td>
<td align="right">434,416</td>
<td align="right">0.2%</td>
<td align="right">-8.6%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,279,361,246</td>
<td align="right"></td>
<td align="right">2,166,721,332</td>
<td align="right"></td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,702,634,484</td>
<td align="right"></td>
<td align="right">6,668,529,852</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,030,700,530</td>
<td align="right">32.5%</td>
<td align="right">6,000,322,498</td>
<td align="right">32.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,108,700,260</td>
<td align="right">32.9%</td>
<td align="right">6,078,190,788</td>
<td align="right">32.9%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,436,935,134</td>
<td align="right"></td>
<td align="right">12,385,033,458</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,436,805,407</td>
<td align="right">67.1%</td>
<td align="right">12,384,939,793</td>
<td align="right">67.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,902,654,226</td>
<td align="right"></td>
<td align="right">2,896,706,825</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,578,573</td>
<td align="right">0.4%</td>
<td align="right">71,448,519</td>
<td align="right">0.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,421,157</td>
<td align="right">0.0%</td>
<td align="right">6,419,771</td>
<td align="right">0.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,159,046</td>
<td align="right"></td>
<td align="right">179,139,794</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,172</td>
<td align="right">2.5%</td>
<td align="right">4,444,172</td>
<td align="right">2.5%</td>
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
<td align="right">365,627</td>
<td align="right">103,615,818</td>
<td align="right">9,521,207,709</td>
<td align="right">746,900,430</td>
<td align="right">766,389,936</td>
<td align="right">364,347</td>
<td align="right">102,538,647</td>
<td align="right">9,553,370,666</td>
<td align="right">756,955,674</td>
<td align="right">764,649,740</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,989,756</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,608,255,050</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
<td align="right">160</td>
<td align="right">160 / 0 !!</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
