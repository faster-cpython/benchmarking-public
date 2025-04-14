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
<td align="left">STORE_SLICE</td>
<td align="right">1,194,074</td>
<td align="right">273,674</td>
<td align="right">-77.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">171,230,702</td>
<td align="right">69,822,642</td>
<td align="right">-59.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">18,277,839</td>
<td align="right">11,685,654</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,859</td>
<td align="right">923,705</td>
<td align="right">-35.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,497,055</td>
<td align="right">3,545,015</td>
<td align="right">-21.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,216,916</td>
<td align="right">21,546,816</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,405,924</td>
<td align="right">94,603,324</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,269,474</td>
<td align="right">21,086,235</td>
<td align="right">-19.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,131,993</td>
<td align="right">21,111,705</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">234,703,077</td>
<td align="right">203,148,786</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">56,843,777</td>
<td align="right">49,210,063</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,726,195</td>
<td align="right">44,783,402</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">35,480,261</td>
<td align="right">30,770,648</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">61,097,919</td>
<td align="right">53,001,576</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">125,933,821</td>
<td align="right">109,614,784</td>
<td align="right">-13.0%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">265,156,127</td>
<td align="right">230,955,629</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">32,156,035</td>
<td align="right">28,329,363</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,277,936</td>
<td align="right">31,987,553</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">67,805,869</td>
<td align="right">60,290,177</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,485,804</td>
<td align="right">32,529,403</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">65,579,074</td>
<td align="right">59,549,357</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">115,093,564</td>
<td align="right">105,281,994</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,238,470</td>
<td align="right">95,421,707</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,421,635</td>
<td align="right">165,096,076</td>
<td align="right">-7.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">103,695,906</td>
<td align="right">96,168,431</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">143,524,900</td>
<td align="right">153,917,703</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">186,376,600</td>
<td align="right">173,507,915</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,347,078</td>
<td align="right">208,038,927</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">698,064,106</td>
<td align="right">651,178,512</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">300,558,758</td>
<td align="right">280,647,429</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,644,616</td>
<td align="right">3,880,388</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">171,557,615</td>
<td align="right">160,499,159</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,224,038</td>
<td align="right">111,699,513</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,660,317</td>
<td align="right">17,553,085</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">307,060,851</td>
<td align="right">289,012,233</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">87,928,901</td>
<td align="right">82,832,471</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,581,508</td>
<td align="right">34,519,250</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">270,865,020</td>
<td align="right">256,012,587</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">153,985,605</td>
<td align="right">145,549,546</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">405,136,913</td>
<td align="right">382,943,044</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">276,083,853</td>
<td align="right">262,142,029</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,922,530</td>
<td align="right">55,999,488</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">224,589,134</td>
<td align="right">213,542,776</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">851,272,219</td>
<td align="right">809,755,699</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,627,187</td>
<td align="right">40,564,929</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,594,702</td>
<td align="right">75,770,783</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,451,436</td>
<td align="right">138,633,127</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,487,759,452</td>
<td align="right">1,419,000,014</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">715,417,032</td>
<td align="right">682,793,017</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">902,537,734</td>
<td align="right">861,388,083</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">250,238,965</td>
<td align="right">238,947,669</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">708,533,551</td>
<td align="right">677,738,592</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,042,392</td>
<td align="right">92,845,821</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">209,445,507</td>
<td align="right">200,403,240</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">539,258,087</td>
<td align="right">516,396,044</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,277,833,905</td>
<td align="right">1,223,860,083</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,465,897</td>
<td align="right">90,494,646</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">181,993,491</td>
<td align="right">174,611,694</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,975,163</td>
<td align="right">76,838,423</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">442,601,379</td>
<td align="right">425,525,651</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,757,239</td>
<td align="right">20,924,870</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">428,553,005</td>
<td align="right">412,352,879</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">159,359,565</td>
<td align="right">153,495,254</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">292,234,505</td>
<td align="right">281,520,673</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">325,719,490</td>
<td align="right">313,852,591</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">531,850,450</td>
<td align="right">512,586,983</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,305,338</td>
<td align="right">56,195,754</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,452,293</td>
<td align="right">318,751,829</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">658,346,311</td>
<td align="right">635,830,205</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">607,565,476</td>
<td align="right">628,315,445</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,859,071,575</td>
<td align="right">13,385,787,245</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,118,757,526</td>
<td align="right">3,013,514,241</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,580,583</td>
<td align="right">129,103,502</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,211,532,325</td>
<td align="right">3,106,201,513</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,613,339,211</td>
<td align="right">1,560,488,367</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,838,504,966</td>
<td align="right">3,712,846,622</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,774,426</td>
<td align="right">17,202,874</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,810,581</td>
<td align="right">64,666,714</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">307,545,764</td>
<td align="right">297,907,758</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,781,960,847</td>
<td align="right">1,727,695,924</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">329,956,509</td>
<td align="right">320,304,757</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">485,290,701</td>
<td align="right">471,504,955</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,481,753,227</td>
<td align="right">2,414,016,591</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,068,200</td>
<td align="right">63,317,879</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">350,886,343</td>
<td align="right">341,697,891</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,931,215,963</td>
<td align="right">1,881,097,249</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">129,774,665</td>
<td align="right">126,533,274</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">137,982,326</td>
<td align="right">134,654,751</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,049,010</td>
<td align="right">66,412,379</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,641,362</td>
<td align="right">440,878,859</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,187,431</td>
<td align="right">165,176,964</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">82,014,742</td>
<td align="right">80,114,315</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">228,685,215</td>
<td align="right">223,456,063</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,216,310</td>
<td align="right">47,132,663</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,848,954,059</td>
<td align="right">3,763,522,504</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,791,022,136</td>
<td align="right">2,733,386,421</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,301,766</td>
<td align="right">10,094,632</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,034,899,280</td>
<td align="right">2,075,621,972</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">69,696,984</td>
<td align="right">68,309,805</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">61,473,298</td>
<td align="right">60,267,196</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,294,087</td>
<td align="right">56,178,517</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,292,776</td>
<td align="right">32,655,395</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,398,720</td>
<td align="right">185,831,128</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,910,065</td>
<td align="right">137,309,301</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,047,399</td>
<td align="right">8,882,188</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">626,345,850</td>
<td align="right">615,532,298</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,581,731</td>
<td align="right">154,958,038</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">172,202,213</td>
<td align="right">169,357,485</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">328,703,376</td>
<td align="right">323,361,512</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,162,395,535</td>
<td align="right">2,127,631,964</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,050,220</td>
<td align="right">4,114,478</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">111,568,561</td>
<td align="right">109,808,293</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,312,505,868</td>
<td align="right">2,276,577,773</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,315,226</td>
<td align="right">33,788,550</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">70,429,028</td>
<td align="right">69,375,595</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,609,123</td>
<td align="right">57,786,097</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,036,348</td>
<td align="right">8,912,702</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,445,341</td>
<td align="right">9,321,818</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,244,862</td>
<td align="right">13,416,166</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,873,142</td>
<td align="right">26,556,134</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,841,666</td>
<td align="right">70,632,825</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">168,143,509</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">265,807,399</td>
<td align="right">262,843,080</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,085</td>
<td align="right">204,176,284</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">640,011,302</td>
<td align="right">633,071,496</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">251,870,318</td>
<td align="right">249,180,651</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">153,395,141</td>
<td align="right">151,758,218</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">214,616,869</td>
<td align="right">212,682,924</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,910,032</td>
<td align="right">770,231,257</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,651,457</td>
<td align="right">11,552,812</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,003,170</td>
<td align="right">111,088,876</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,604,426</td>
<td align="right">10,686,186</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">320,220,891</td>
<td align="right">317,983,610</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,944,597</td>
<td align="right">390,304,410</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">66,897,701</td>
<td align="right">66,486,143</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,114,229</td>
<td align="right">94,558,815</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,844,091</td>
<td align="right">3,865,432</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,781,012</td>
<td align="right">98,352,664</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,817,867,039</td>
<td align="right">4,803,720,456</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,228,778</td>
<td align="right">60,401,896</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">49,176,342</td>
<td align="right">49,297,217</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,288,221</td>
<td align="right">95,114,227</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,135</td>
<td align="right">5,141</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,558,958</td>
<td align="right">71,623,179</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,713</td>
<td align="right">33,739</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,234,167</td>
<td align="right">242,304,507</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,015,283</td>
<td align="right">2,014,759</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,123</td>
<td align="right">133,148</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,132,658</td>
<td align="right">180,159,989</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,591</td>
<td align="right">405,645</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,618,896,825</td>
<td align="right">1,619,068,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,631</td>
<td align="right">773,591</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,861</td>
<td align="right">120,855</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,841,525</td>
<td align="right">1,071,794,139</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">5,196,447</td>
<td align="right">5,196,258</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">19,916,051</td>
<td align="right">19,915,536</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,246,535</td>
<td align="right">20,246,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,246,555</td>
<td align="right">20,246,040</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,060</td>
<td align="right">2,573,020</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,816,846</td>
<td align="right">100,816,099</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,048,559</td>
<td align="right">3,048,542</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,929</td>
<td align="right">1,645,923</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,803,810</td>
<td align="right">5,803,796</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,769</td>
<td align="right">23,563,787</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,217</td>
<td align="right">14,760,215</td>
<td align="right">-0.0%</td>
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
<td align="left">GET_ANEXT</td>
<td align="right">6,000,000</td>
<td align="right">6,000,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,911</td>
<td align="right">4,866,911</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">781,020</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">207,638</td>
<td align="right">207,638</td>
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
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,708</td>
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
<td align="right">330,290,513</td>
<td align="right">4.1%</td>
<td align="right">318,592,269</td>
<td align="right">4.0%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">51,004,210</td>
<td align="right">0.6%</td>
<td align="right">50,449,776</td>
<td align="right">0.6%</td>
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
<td align="right">7,638,285,230</td>
<td align="right">95.2%</td>
<td align="right">7,639,802,976</td>
<td align="right">95.4%</td>
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
<td align="right">153,189</td>
<td align="right">13.6%</td>
<td align="right">150,968</td>
<td align="right">13.6%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">970,903</td>
<td align="right">86.4%</td>
<td align="right">960,489</td>
<td align="right">86.4%</td>
<td align="right">-1.1%</td>
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
<td align="left">subtract other</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">3,562</td>
<td align="right">2.4%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">2,487</td>
<td align="right">1.6%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">5,832</td>
<td align="right">3.9%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">5,459</td>
<td align="right">3.6%</td>
<td align="right">4,976</td>
<td align="right">3.3%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">488</td>
<td align="right">0.3%</td>
<td align="right">531</td>
<td align="right">0.4%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,716</td>
<td align="right">3.7%</td>
<td align="right">5,535</td>
<td align="right">3.7%</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,068</td>
<td align="right">13.1%</td>
<td align="right">20,651</td>
<td align="right">13.7%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,764</td>
<td align="right">11.6%</td>
<td align="right">17,355</td>
<td align="right">11.5%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">626</td>
<td align="right">0.4%</td>
<td align="right">629</td>
<td align="right">0.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,836</td>
<td align="right">12.9%</td>
<td align="right">19,813</td>
<td align="right">13.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,488</td>
<td align="right">12.1%</td>
<td align="right">18,472</td>
<td align="right">12.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,468</td>
<td align="right">15.3%</td>
<td align="right">23,481</td>
<td align="right">15.6%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">17,023</td>
<td align="right">11.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">2,343</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,995</td>
<td align="right">1.3%</td>
<td align="right">1,995</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">836</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.1%</td>
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
<td align="right">97,042,392</td>
<td align="right">100.0%</td>
<td align="right">92,845,821</td>
<td align="right">100.0%</td>
<td align="right">-4.3%</td>
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
<td align="right">451,490,199</td>
<td align="right">7.6%</td>
<td align="right">440,731,169</td>
<td align="right">7.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,824,977</td>
<td align="right">0.1%</td>
<td align="right">5,765,731</td>
<td align="right">0.1%</td>
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
<td align="right">5,468,662,049</td>
<td align="right">92.3%</td>
<td align="right">5,468,737,746</td>
<td align="right">92.4%</td>
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
<td align="right">141,924</td>
<td align="right">54.4%</td>
<td align="right">138,451</td>
<td align="right">54.0%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,914</td>
<td align="right">45.6%</td>
<td align="right">117,789</td>
<td align="right">46.0%</td>
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
<td align="left">buffer int</td>
<td align="right">3,675</td>
<td align="right">2.6%</td>
<td align="right">2,955</td>
<td align="right">2.1%</td>
<td align="right">-19.6%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,100</td>
<td align="right">5.0%</td>
<td align="right">6,607</td>
<td align="right">4.8%</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,055</td>
<td align="right">24.7%</td>
<td align="right">34,043</td>
<td align="right">24.6%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,665</td>
<td align="right">42.0%</td>
<td align="right">58,437</td>
<td align="right">42.2%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,607</td>
<td align="right">2.5%</td>
<td align="right">3,586</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,446</td>
<td align="right">8.8%</td>
<td align="right">12,447</td>
<td align="right">9.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">16,574</td>
<td align="right">12.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">768</td>
<td align="right">0.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
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
<td align="right">126,923,324</td>
<td align="right">1.1%</td>
<td align="right">119,051,471</td>
<td align="right">1.1%</td>
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
<td align="right">124,759,641</td>
<td align="right">1.1%</td>
<td align="right">117,036,428</td>
<td align="right">1.0%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,082,378,253</td>
<td align="right">98.9%</td>
<td align="right">11,092,596,313</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
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
<td align="right">2,568,828</td>
<td align="right">100.0%</td>
<td align="right">2,420,242</td>
<td align="right">100.0%</td>
<td align="right">-5.8%</td>
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
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">64.3%</td>
<td align="right">287</td>
<td align="right">64.3%</td>
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
<td align="right">684,422</td>
<td align="right">97.1%</td>
<td align="right">684,422</td>
<td align="right">97.1%</td>
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
<td align="right">583,846</td>
<td align="right">82.8%</td>
<td align="right">583,846</td>
<td align="right">82.9%</td>
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
<td align="right">20,165</td>
<td align="right">99.4%</td>
<td align="right">20,159</td>
<td align="right">99.4%</td>
<td align="right">-0.0%</td>
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
<td align="right">87,812,007</td>
<td align="right">1.9%</td>
<td align="right">82,716,801</td>
<td align="right">1.8%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,155,459</td>
<td align="right">0.0%</td>
<td align="right">1,155,889</td>
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
<td align="right">4,515,246,999</td>
<td align="right">98.1%</td>
<td align="right">4,515,508,220</td>
<td align="right">98.2%</td>
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
<td align="right">98,676</td>
<td align="right">71.2%</td>
<td align="right">97,458</td>
<td align="right">71.0%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">39,823</td>
<td align="right">28.8%</td>
<td align="right">39,823</td>
<td align="right">29.0%</td>
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
<td align="left">bool</td>
<td align="right">927</td>
<td align="right">0.9%</td>
<td align="right">740</td>
<td align="right">0.8%</td>
<td align="right">-20.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,708</td>
<td align="right">7.8%</td>
<td align="right">6,740</td>
<td align="right">6.9%</td>
<td align="right">-12.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,551</td>
<td align="right">4.6%</td>
<td align="right">4,423</td>
<td align="right">4.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">364</td>
<td align="right">0.4%</td>
<td align="right">360</td>
<td align="right">0.4%</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,173</td>
<td align="right">23.5%</td>
<td align="right">23,205</td>
<td align="right">23.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,478</td>
<td align="right">8.6%</td>
<td align="right">8,486</td>
<td align="right">8.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">36,864</td>
<td align="right">37.4%</td>
<td align="right">36,896</td>
<td align="right">37.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,433</td>
<td align="right">6.5%</td>
<td align="right">6,430</td>
<td align="right">6.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.7%</td>
<td align="right">7,639</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">1,221</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">984</td>
<td align="right">1.0%</td>
<td align="right">984</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
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
<td align="right">56,806,151</td>
<td align="right">2.5%</td>
<td align="right">49,174,291</td>
<td align="right">2.2%</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,188,418,794</td>
<td align="right">97.4%</td>
<td align="right">2,188,567,717</td>
<td align="right">97.7%</td>
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
<td align="right">35,365</td>
<td align="right">47.9%</td>
<td align="right">33,511</td>
<td align="right">46.6%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">52.1%</td>
<td align="right">38,435</td>
<td align="right">53.4%</td>
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
<td align="right">7,174</td>
<td align="right">20.3%</td>
<td align="right">6,692</td>
<td align="right">20.0%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,818</td>
<td align="right">22.1%</td>
<td align="right">7,329</td>
<td align="right">21.9%</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,173</td>
<td align="right">25.9%</td>
<td align="right">8,655</td>
<td align="right">25.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,200</td>
<td align="right">31.7%</td>
<td align="right">10,835</td>
<td align="right">32.3%</td>
<td align="right">-3.3%</td>
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
<td align="right">32,375,897</td>
<td align="right">4.3%</td>
<td align="right">41,670,097</td>
<td align="right">6.1%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">118,306,642</td>
<td align="right">15.7%</td>
<td align="right">94,526,710</td>
<td align="right">13.8%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">601,341,647</td>
<td align="right">80.0%</td>
<td align="right">550,222,898</td>
<td align="right">80.1%</td>
<td align="right">-8.5%</td>
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
<td align="right">615,793</td>
<td align="right">86.7%</td>
<td align="right">791,144</td>
<td align="right">91.7%</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">94,212</td>
<td align="right">13.3%</td>
<td align="right">71,542</td>
<td align="right">8.3%</td>
<td align="right">-24.1%</td>
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
<td align="left">seq iter</td>
<td align="right">6,164</td>
<td align="right">6.5%</td>
<td align="right">2,799</td>
<td align="right">3.9%</td>
<td align="right">-54.6%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,547</td>
<td align="right">1.6%</td>
<td align="right">1,039</td>
<td align="right">1.5%</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">51,073</td>
<td align="right">54.2%</td>
<td align="right">35,473</td>
<td align="right">49.6%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.4%</td>
<td align="right">1,847</td>
<td align="right">2.6%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,913</td>
<td align="right">6.3%</td>
<td align="right">4,971</td>
<td align="right">6.9%</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,493</td>
<td align="right">4.8%</td>
<td align="right">3,912</td>
<td align="right">5.5%</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">1,065</td>
<td align="right">1.5%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">4.8%</td>
<td align="right">4,172</td>
<td align="right">5.8%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,032</td>
<td align="right">3.2%</td>
<td align="right">2,783</td>
<td align="right">3.9%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,750</td>
<td align="right">11.4%</td>
<td align="right">10,042</td>
<td align="right">14.0%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">2,804</td>
<td align="right">3.9%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">327</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">639,538,140</td>
<td align="right">4.8%</td>
<td align="right">602,912,792</td>
<td align="right">4.6%</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">530,226,034</td>
<td align="right">4.0%</td>
<td align="right">510,952,320</td>
<td align="right">3.9%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,074,789,315</td>
<td align="right">91.2%</td>
<td align="right">12,113,797,640</td>
<td align="right">91.6%</td>
<td align="right">0.3%</td>
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
<td align="right">355,053</td>
<td align="right">2.8%</td>
<td align="right">469,943</td>
<td align="right">3.9%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,153,130</td>
<td align="right">97.2%</td>
<td align="right">11,461,343</td>
<td align="right">96.1%</td>
<td align="right">-5.7%</td>
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
<td align="right">1,607</td>
<td align="right">0.5%</td>
<td align="right">1,482</td>
<td align="right">0.3%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,798</td>
<td align="right">6.7%</td>
<td align="right">22,460</td>
<td align="right">4.8%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">1,502</td>
<td align="right">0.3%</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">857</td>
<td align="right">0.2%</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,703</td>
<td align="right">11.5%</td>
<td align="right">39,596</td>
<td align="right">8.4%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,195</td>
<td align="right">10.8%</td>
<td align="right">37,474</td>
<td align="right">8.0%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,406</td>
<td align="right">0.7%</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,938</td>
<td align="right">1.4%</td>
<td align="right">4,864</td>
<td align="right">1.0%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,071</td>
<td align="right">16.9%</td>
<td align="right">59,643</td>
<td align="right">12.7%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,512</td>
<td align="right">4.1%</td>
<td align="right">14,425</td>
<td align="right">3.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,940</td>
<td align="right">2.2%</td>
<td align="right">7,944</td>
<td align="right">1.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">6,405</td>
<td align="right">1.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,086</td>
<td align="right">1.4%</td>
<td align="right">5,086</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
<td align="right">1,092</td>
<td align="right">0.2%</td>
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
<td align="right">0.1%</td>
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
<td align="right">3,758,312,363</td>
<td align="right">99.6%</td>
<td align="right">3,654,684,430</td>
<td align="right">99.6%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,698</td>
<td align="right">0.4%</td>
<td align="right">14,622,713</td>
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
<td align="right">1,508</td>
<td align="right">0.0%</td>
<td align="right">1,508</td>
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
<td align="right">52,555</td>
<td align="right">0.0%</td>
<td align="right">52,555</td>
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
<td align="right">138,286</td>
<td align="right">100.0%</td>
<td align="right">138,269</td>
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
<td align="right">64,084,389</td>
<td align="right">100.0%</td>
<td align="right">64,319,982</td>
<td align="right">100.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">253</td>
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
<td align="right">2,455</td>
<td align="right">100.0%</td>
<td align="right">2,455</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">593,288,753</td>
<td align="right">82.2%</td>
<td align="right">593,288,741</td>
<td align="right">82.2%</td>
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
<td align="right">69,748,540</td>
<td align="right">3.4%</td>
<td align="right">70,539,502</td>
<td align="right">3.5%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">114,603,408</td>
<td align="right">5.7%</td>
<td align="right">114,257,586</td>
<td align="right">5.6%</td>
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
<td align="right">1,842,119,647</td>
<td align="right">90.9%</td>
<td align="right">1,842,886,693</td>
<td align="right">90.9%</td>
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
<td align="right">50,974</td>
<td align="right">2.3%</td>
<td align="right">51,170</td>
<td align="right">2.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,203,803</td>
<td align="right">97.7%</td>
<td align="right">2,197,285</td>
<td align="right">97.7%</td>
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
<td align="left">other</td>
<td align="right">135,728</td>
<td align="right">266.3%</td>
<td align="right">254,628</td>
<td align="right">497.6%</td>
<td align="right">87.6%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">4,764</td>
<td align="right">9.3%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">24,476</td>
<td align="right">47.8%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,352</td>
<td align="right">6.6%</td>
<td align="right">3,344</td>
<td align="right">6.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
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
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">699</td>
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
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">110</td>
<td align="right">0.2%</td>
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
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">273,674</td>
<td align="right">100.0%</td>
<td align="right">-77.1%</td>
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
<td align="right">133,534,647</td>
<td align="right">12.7%</td>
<td align="right">129,058,684</td>
<td align="right">12.3%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">918,978,195</td>
<td align="right">87.3%</td>
<td align="right">919,126,994</td>
<td align="right">87.7%</td>
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
<td align="right">43,782</td>
<td align="right">95.2%</td>
<td align="right">42,663</td>
<td align="right">95.1%</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,194</td>
<td align="right">4.8%</td>
<td align="right">2,195</td>
<td align="right">4.9%</td>
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
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">156</td>
<td align="right">0.4%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">236</td>
<td align="right">0.6%</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,031</td>
<td align="right">6.9%</td>
<td align="right">2,290</td>
<td align="right">5.4%</td>
<td align="right">-24.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">8,038</td>
<td align="right">18.8%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">14,757</td>
<td align="right">33.7%</td>
<td align="right">14,651</td>
<td align="right">34.3%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,705</td>
<td align="right">38.2%</td>
<td align="right">16,723</td>
<td align="right">39.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">501</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">102,775,010</td>
<td align="right">2.2%</td>
<td align="right">94,957,365</td>
<td align="right">2.0%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">40,867,482</td>
<td align="right">0.9%</td>
<td align="right">39,413,832</td>
<td align="right">0.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,525,163,897</td>
<td align="right">96.9%</td>
<td align="right">4,526,246,949</td>
<td align="right">97.1%</td>
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
<td align="right">819,743</td>
<td align="right">66.5%</td>
<td align="right">792,282</td>
<td align="right">65.7%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">413,294</td>
<td align="right">33.5%</td>
<td align="right">414,233</td>
<td align="right">34.3%</td>
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
<td align="left">other</td>
<td align="right">16,411</td>
<td align="right">4.0%</td>
<td align="right">20,101</td>
<td align="right">4.9%</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">3,617</td>
<td align="right">0.9%</td>
<td align="right">-21.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,366</td>
<td align="right">3.0%</td>
<td align="right">11,694</td>
<td align="right">2.8%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,694</td>
<td align="right">1.4%</td>
<td align="right">5,621</td>
<td align="right">1.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,622</td>
<td align="right">2.1%</td>
<td align="right">8,543</td>
<td align="right">2.1%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,066</td>
<td align="right">22.8%</td>
<td align="right">93,367</td>
<td align="right">22.5%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,473</td>
<td align="right">3.3%</td>
<td align="right">13,421</td>
<td align="right">3.2%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">256,179</td>
<td align="right">62.0%</td>
<td align="right">255,983</td>
<td align="right">61.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
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
<td align="right">1,427,465</td>
<td align="right">0.1%</td>
<td align="right">911,458</td>
<td align="right">0.1%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,232,771,815</td>
<td align="right">99.9%</td>
<td align="right">1,232,865,885</td>
<td align="right">99.9%</td>
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
<td align="right">873</td>
<td align="right">7.0%</td>
<td align="right">726</td>
<td align="right">5.9%</td>
<td align="right">-16.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.0%</td>
<td align="right">11,601</td>
<td align="right">94.1%</td>
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
<td align="right">646</td>
<td align="right">74.0%</td>
<td align="right">499</td>
<td align="right">68.7%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.6%</td>
<td align="right">136</td>
<td align="right">18.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.4%</td>
<td align="right">91</td>
<td align="right">12.5%</td>
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
<td align="right">2,127,600,806</td>
<td align="right">2.6%</td>
<td align="right">2,032,205,864</td>
<td align="right">2.6%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,015,024,038</td>
<td align="right">1.3%</td>
<td align="right">977,382,206</td>
<td align="right">1.3%</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,337,435,584</td>
<td align="right">37.8%</td>
<td align="right">29,276,486,563</td>
<td align="right">37.5%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">46,853,566,789</td>
<td align="right">58.3%</td>
<td align="right">45,707,381,212</td>
<td align="right">58.6%</td>
<td align="right">-2.4%</td>
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
<td align="right">118,306,642</td>
<td align="right">5.3%</td>
<td align="right">94,526,710</td>
<td align="right">4.4%</td>
<td align="right">-20.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,775,010</td>
<td align="right">4.6%</td>
<td align="right">94,957,365</td>
<td align="right">4.4%</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">124,759,641</td>
<td align="right">5.5%</td>
<td align="right">117,036,428</td>
<td align="right">5.5%</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">87,812,007</td>
<td align="right">3.9%</td>
<td align="right">82,716,801</td>
<td align="right">3.9%</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,042,392</td>
<td align="right">4.3%</td>
<td align="right">92,845,821</td>
<td align="right">4.3%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">530,226,034</td>
<td align="right">23.6%</td>
<td align="right">510,952,320</td>
<td align="right">23.8%</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,290,513</td>
<td align="right">14.7%</td>
<td align="right">318,592,269</td>
<td align="right">14.8%</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,534,647</td>
<td align="right">5.9%</td>
<td align="right">129,058,684</td>
<td align="right">6.0%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,490,199</td>
<td align="right">20.1%</td>
<td align="right">440,731,169</td>
<td align="right">20.5%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,907</td>
<td align="right">5.7%</td>
<td align="right">128,816,907</td>
<td align="right">6.0%</td>
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
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">183,330,686</td>
<td align="right">18.1%</td>
<td align="right">157,281,713</td>
<td align="right">16.1%</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,732,667</td>
<td align="right">7.5%</td>
<td align="right">67,319,587</td>
<td align="right">6.9%</td>
<td align="right">-11.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,007,007</td>
<td align="right">6.8%</td>
<td align="right">61,799,592</td>
<td align="right">6.3%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,459,967</td>
<td align="right">7.3%</td>
<td align="right">78,317,840</td>
<td align="right">8.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">252,813,499</td>
<td align="right">24.9%</td>
<td align="right">248,670,867</td>
<td align="right">25.4%</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,418,465</td>
<td align="right">2.4%</td>
<td align="right">24,132,776</td>
<td align="right">2.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">92,967,816</td>
<td align="right">9.2%</td>
<td align="right">92,619,201</td>
<td align="right">9.5%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">21,600,057</td>
<td align="right">2.1%</td>
<td align="right">21,602,850</td>
<td align="right">2.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,241,544</td>
<td align="right">2.1%</td>
<td align="right">21,240,333</td>
<td align="right">2.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,873,003</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">20,907,063</td>
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
<td align="left">Frame objects created</td>
<td align="right">71,102,174</td>
<td align="right">1.1%</td>
<td align="right">71,520,125</td>
<td align="right">1.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,450,545,078</td>
<td align="right">81.6%</td>
<td align="right">5,452,801,915</td>
<td align="right">81.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,057,802,447</td>
<td align="right">75.7%</td>
<td align="right">5,059,769,172</td>
<td align="right">75.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,459,190</td>
<td align="right">10.0%</td>
<td align="right">670,648,554</td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,623,546,547</td>
<td align="right">24.3%</td>
<td align="right">1,623,954,374</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,623,546,547</td>
<td align="right">24.3%</td>
<td align="right">1,623,954,374</td>
<td align="right">24.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">950,955,214</td>
<td align="right">14.2%</td>
<td align="right">951,173,677</td>
<td align="right">14.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">953,087,357</td>
<td align="right">14.3%</td>
<td align="right">953,305,820</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,256,991</td>
<td align="right">4.2%</td>
<td align="right">279,225,020</td>
<td align="right">4.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,305</td>
<td align="right">0.4%</td>
<td align="right">24,922,230</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,730</td>
<td align="right">3.9%</td>
<td align="right">261,407,469</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
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
<td align="left">Method cache dunder misses</td>
<td align="right">8,280,232</td>
<td align="right"></td>
<td align="right">8,725,130</td>
<td align="right"></td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,892,505,517</td>
<td align="right">5.5%</td>
<td align="right">8,597,888,100</td>
<td align="right">5.5%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">77,331,415,411</td>
<td align="right">48.2%</td>
<td align="right">74,933,162,269</td>
<td align="right">47.7%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">82,810,838,105</td>
<td align="right">41.1%</td>
<td align="right">80,258,001,921</td>
<td align="right">40.5%</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">35,846,816,607</td>
<td align="right">22.3%</td>
<td align="right">34,974,815,971</td>
<td align="right">22.3%</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,467,686,101</td>
<td align="right">8.2%</td>
<td align="right">16,105,974,322</td>
<td align="right">8.1%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,166,721,332</td>
<td align="right"></td>
<td align="right">2,124,630,733</td>
<td align="right"></td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">47,386,833,134</td>
<td align="right">23.5%</td>
<td align="right">46,672,578,038</td>
<td align="right">23.6%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">69,178,738</td>
<td align="right"></td>
<td align="right">69,832,672</td>
<td align="right"></td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,616,524,408</td>
<td align="right">27.1%</td>
<td align="right">54,998,779,877</td>
<td align="right">27.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">38,347,677,862</td>
<td align="right">23.9%</td>
<td align="right">38,598,161,164</td>
<td align="right">24.6%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">61,707,195</td>
<td align="right"></td>
<td align="right">61,916,064</td>
<td align="right"></td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,896,706,825</td>
<td align="right"></td>
<td align="right">2,888,177,992</td>
<td align="right"></td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,139,794</td>
<td align="right"></td>
<td align="right">179,311,057</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,771</td>
<td align="right">0.0%</td>
<td align="right">6,425,475</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,000,322,498</td>
<td align="right">32.5%</td>
<td align="right">6,001,951,879</td>
<td align="right">32.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,668,529,852</td>
<td align="right"></td>
<td align="right">6,670,338,617</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,078,190,788</td>
<td align="right">32.9%</td>
<td align="right">6,079,810,463</td>
<td align="right">32.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,448,519</td>
<td align="right">0.4%</td>
<td align="right">71,433,109</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,385,033,458</td>
<td align="right"></td>
<td align="right">12,386,774,522</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,384,939,793</td>
<td align="right">67.1%</td>
<td align="right">12,386,660,950</td>
<td align="right">67.1%</td>
<td align="right">0.0%</td>
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
<td align="left">Materialize dict (new key)</td>
<td align="right">434,416</td>
<td align="right">0.2%</td>
<td align="right">434,416</td>
<td align="right">0.2%</td>
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
<td align="right">364,347</td>
<td align="right">102,538,647</td>
<td align="right">9,553,370,666</td>
<td align="right">756,955,674</td>
<td align="right">764,649,740</td>
<td align="right">364,224</td>
<td align="right">102,633,896</td>
<td align="right">9,544,391,187</td>
<td align="right">756,285,792</td>
<td align="right">763,229,892</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,608,255,050</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,608,263,882</td>
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
<td align="right">3,244</td>
<td align="right">0.6%</td>
<td align="right">436</td>
<td align="right">0.1%</td>
<td align="right">-86.6%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">958</td>
<td align="right">0.2%</td>
<td align="right">410</td>
<td align="right">0.1%</td>
<td align="right">-57.2%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">66,503</td>
<td align="right">13.1%</td>
<td align="right">34,446</td>
<td align="right">7.0%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,025,358,815</td>
<td align="right"></td>
<td align="right">3,720,072,593</td>
<td align="right"></td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">274</td>
<td align="right">0.1%</td>
<td align="right">308</td>
<td align="right">0.1%</td>
<td align="right">12.4%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">501</td>
<td align="right">0.8%</td>
<td align="right">480</td>
<td align="right">1.4%</td>
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
<td align="right">811</td>
<td align="right">0.2%</td>
<td align="right">778</td>
<td align="right">0.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">506,834</td>
<td align="right"></td>
<td align="right">489,081</td>
<td align="right"></td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">440,057</td>
<td align="right">86.8%</td>
<td align="right">454,327</td>
<td align="right">92.9%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">397,687</td>
<td align="right">78.5%</td>
<td align="right">409,727</td>
<td align="right">83.8%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">272,206,958,503</td>
<td align="right">3,874.6%</td>
<td align="right">273,009,775,631</td>
<td align="right">7,338.8%</td>
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
<td align="right">60</td>
<td align="right">0.0%</td>
<td align="right">60</td>
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
<td align="right">60,207</td>
<td align="right">90.5%</td>
<td align="right">29,843</td>
<td align="right">86.6%</td>
<td align="right">-50.4%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">66,503</td>
<td align="right"></td>
<td align="right">34,446</td>
<td align="right"></td>
<td align="right">-48.2%</td>
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
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">75,849,952</td>
<td align="right">11.7%</td>
<td align="right">103,992,848</td>
<td align="right">13.0%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">445,658,005</td>
<td align="right">68.6%</td>
<td align="right">605,726,706</td>
<td align="right">75.8%</td>
<td align="right">35.9%</td>
</tr>
<tr>
<td align="left">
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">128,023,435</td>
<td align="right">19.7%</td>
<td align="right">88,943,102</td>
<td align="right">11.1%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">649,531,392</td>
<td align="right"></td>
<td align="right">798,662,656</td>
<td align="right"></td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">541,642,752</td>
<td align="right">83.4%</td>
<td align="right">620,679,168</td>
<td align="right">77.7%</td>
<td align="right">14.6%</td>
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
<td align="left">15,198</td>
<td align="right">25.2%</td>
<td align="left">9,085</td>
<td align="right">21.7%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">24,673</td>
<td align="right">41.0%</td>
<td align="left">11,698</td>
<td align="right">27.9%</td>
<td align="right">-52.6%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">14,393</td>
<td align="right">23.9%</td>
<td align="left">9,428</td>
<td align="right">22.5%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,062</td>
<td align="right">6.7%</td>
<td align="left">6,086</td>
<td align="right">14.5%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,553</td>
<td align="right">2.6%</td>
<td align="left">3,552</td>
<td align="right">8.5%</td>
<td align="right">128.7%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">328</td>
<td align="right">0.5%</td>
<td align="left">1,787</td>
<td align="right">4.3%</td>
<td align="right">444.8%</td>
</tr>
<tr>
<td align="left"><= 262,144</td>
<td align="left"></td>
<td align="right"></td>
<td align="left">285</td>
<td align="right">0.7%</td>
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
<td align="left"><= 8</td>
<td align="right">5,665</td>
<td align="right">8.5%</td>
<td align="right">3,151</td>
<td align="right">9.1%</td>
<td align="right">-44.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,347</td>
<td align="right">12.6%</td>
<td align="right">4,585</td>
<td align="right">13.3%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">21,453</td>
<td align="right">32.3%</td>
<td align="right">9,563</td>
<td align="right">27.8%</td>
<td align="right">-55.4%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,498</td>
<td align="right">24.8%</td>
<td align="right">7,234</td>
<td align="right">21.0%</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">8,975</td>
<td align="right">13.5%</td>
<td align="right">5,593</td>
<td align="right">16.2%</td>
<td align="right">-37.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,681</td>
<td align="right">7.0%</td>
<td align="right">3,474</td>
<td align="right">10.1%</td>
<td align="right">-25.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">802</td>
<td align="right">1.2%</td>
<td align="right">760</td>
<td align="right">2.2%</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">86</td>
<td align="right">0.2%</td>
<td align="right">4.9%</td>
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
<td align="left"><= 4</td>
<td align="right">1,885</td>
<td align="right">2.8%</td>
<td align="right">1,386</td>
<td align="right">4.0%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,214</td>
<td align="right">12.4%</td>
<td align="right">3,744</td>
<td align="right">10.9%</td>
<td align="right">-54.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,438</td>
<td align="right">12.7%</td>
<td align="right">5,047</td>
<td align="right">14.7%</td>
<td align="right">-40.2%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,197</td>
<td align="right">36.4%</td>
<td align="right">10,413</td>
<td align="right">30.2%</td>
<td align="right">-57.0%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,481</td>
<td align="right">18.8%</td>
<td align="right">5,609</td>
<td align="right">16.3%</td>
<td align="right">-55.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,478</td>
<td align="right">5.2%</td>
<td align="right">2,532</td>
<td align="right">7.4%</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,226</td>
<td align="right">1.8%</td>
<td align="right">800</td>
<td align="right">2.3%</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">288</td>
<td align="right">0.4%</td>
<td align="right">312</td>
<td align="right">0.9%</td>
<td align="right">8.3%</td>
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
<td align="left">_IMPORT_NAME</td>
<td align="right">27,762</td>
<td align="right">193,640</td>
<td align="right">597.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,509,091</td>
<td align="right">7,176,376</td>
<td align="right">375.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,565,374</td>
<td align="right">7,319,728</td>
<td align="right">367.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">169,428</td>
<td align="right">618,591</td>
<td align="right">265.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">904,770</td>
<td align="right">132.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">553,297</td>
<td align="right">964,596</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">4,539,879</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,406,420,985</td>
<td align="right">3,769,895,931</td>
<td align="right">56.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,953,136,279</td>
<td align="right">2,596,474,023</td>
<td align="right">-56.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,507,238</td>
<td align="right">6,809,079</td>
<td align="right">51.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,025,358,815</td>
<td align="right">3,720,072,593</td>
<td align="right">-47.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,196,565</td>
<td align="right">4,583,616</td>
<td align="right">43.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,936,387</td>
<td align="right">3,888,427</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,642,138</td>
<td align="right">28,970,790</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,717,322</td>
<td align="right">111,019,554</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">36,807,877</td>
<td align="right">44,333,022</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">36,806,917</td>
<td align="right">44,331,436</td>
<td align="right">20.4%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,954,234</td>
<td align="right">35,624,332</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,954,234</td>
<td align="right">35,624,332</td>
<td align="right">18.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,158,323</td>
<td align="right">7,273,765</td>
<td align="right">18.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,991</td>
<td align="right">20,856,286</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">95,168,834</td>
<td align="right">109,793,385</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">207,453,910</td>
<td align="right">234,161,136</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">891,075</td>
<td align="right">1,002,051</td>
<td align="right">12.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,656,701</td>
<td align="right">17,556,844</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,066,246</td>
<td align="right">107,418,976</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,818,123</td>
<td align="right">6,027,135</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">64,995,818</td>
<td align="right">72,499,269</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,671,682</td>
<td align="right">26,316,013</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,551,265,357</td>
<td align="right">1,718,038,709</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,223,919</td>
<td align="right">104,024,658</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,310,006</td>
<td align="right">42,136,678</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,076,245</td>
<td align="right">47,364,998</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,250,178</td>
<td align="right">53,053,971</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">25,521,439</td>
<td align="right">27,998,210</td>
<td align="right">9.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,390,698,772</td>
<td align="right">4,799,443,120</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,516,736</td>
<td align="right">22,368,601</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">501,445,079</td>
<td align="right">544,855,605</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,705,621</td>
<td align="right">33,266,193</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">53,839,040</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">53,839,040</td>
<td align="right">8.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">97,309,258</td>
<td align="right">105,060,603</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">41,512,720</td>
<td align="right">44,788,720</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,134,640</td>
<td align="right">33,591,540</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">503,857,254</td>
<td align="right">543,347,611</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">296,165,513</td>
<td align="right">319,176,520</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">807,052</td>
<td align="right">869,544</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right">14,158,024</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,431,779,800</td>
<td align="right">10,048,641,724</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">29,591,441</td>
<td align="right">31,524,024</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,620,451</td>
<td align="right">27,250,784</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,620,451</td>
<td align="right">27,250,784</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">535,539,513</td>
<td align="right">568,594,955</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,447,871</td>
<td align="right">31,219,350</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">725,025,308</td>
<td align="right">768,129,382</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,211,904</td>
<td align="right">31,983,383</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,250,970</td>
<td align="right">22,426,277</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,625,120</td>
<td align="right">51,225,880</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">312,715,084</td>
<td align="right">329,183,804</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">173,818,495</td>
<td align="right">182,664,535</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">129,244,604</td>
<td align="right">135,796,404</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">164,278,335</td>
<td align="right">172,505,880</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">83,932,636</td>
<td align="right">88,129,206</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">158,025,791</td>
<td align="right">165,558,634</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,617,642,466</td>
<td align="right">1,692,541,962</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,165,092,585</td>
<td align="right">2,261,548,652</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,808,847,783</td>
<td align="right">1,889,294,493</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,048,329,835</td>
<td align="right">1,093,371,276</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,344,382,188</td>
<td align="right">1,400,862,943</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,302,713,145</td>
<td align="right">1,357,187,136</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,297,297,374</td>
<td align="right">3,432,839,279</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,617,240</td>
<td align="right">6,889,150</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,220,208,392</td>
<td align="right">1,270,264,023</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,286,692</td>
<td align="right">91,897,596</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">377,189,474</td>
<td align="right">361,992,725</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,219,313,113</td>
<td align="right">1,268,178,798</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">113,049,800</td>
<td align="right">117,150,433</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,627,684,547</td>
<td align="right">5,826,930,498</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">308,816,002</td>
<td align="right">319,596,087</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">192,195,213</td>
<td align="right">198,897,178</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,263,894,068</td>
<td align="right">2,342,647,818</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,263,803,357</td>
<td align="right">2,342,547,608</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,621,222</td>
<td align="right">49,261,985</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">171,028,039</td>
<td align="right">176,892,303</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,722,365</td>
<td align="right">202,400,705</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">194,365,047</td>
<td align="right">200,926,359</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,247,565</td>
<td align="right">121,203,962</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,862,305,774</td>
<td align="right">2,957,308,204</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,149,927,761</td>
<td align="right">1,187,969,648</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,333,717</td>
<td align="right">38,544,064</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">648,491,408</td>
<td align="right">628,097,084</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">249,511,740</td>
<td align="right">257,189,957</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,083,596,223</td>
<td align="right">1,116,674,094</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,389,037,738</td>
<td align="right">1,431,317,415</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">647,422,540</td>
<td align="right">667,103,811</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">570,819,243</td>
<td align="right">588,055,408</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,061,243</td>
<td align="right">499,399,100</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,709,199,502</td>
<td align="right">1,759,092,392</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,757,443,482</td>
<td align="right">2,836,939,393</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">575,918,791</td>
<td align="right">592,317,766</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">138,136,836</td>
<td align="right">142,029,880</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">556,778,766</td>
<td align="right">572,181,284</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,594</td>
<td align="right">80,258,852</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,766,374,076</td>
<td align="right">5,917,398,206</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,110,999</td>
<td align="right">496,788,133</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,749,252,804</td>
<td align="right">33,604,235,515</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">158,173,785</td>
<td align="right">162,283,568</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,469,878</td>
<td align="right">81,532,136</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">284,796,177</td>
<td align="right">292,176,245</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,850,145,741</td>
<td align="right">1,897,356,432</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">167,877,351</td>
<td align="right">172,087,472</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,193,866,046</td>
<td align="right">1,223,648,008</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">241,773,697</td>
<td align="right">235,743,727</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">483,916,951</td>
<td align="right">495,945,859</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,650,236</td>
<td align="right">6,815,380</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">167,529,622</td>
<td align="right">171,686,460</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,460,344,071</td>
<td align="right">4,569,015,912</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">484,546,259</td>
<td align="right">496,232,345</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,721,536,518</td>
<td align="right">4,834,206,608</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">335,217,555</td>
<td align="right">343,142,123</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">752,791,859</td>
<td align="right">770,058,975</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,399,380</td>
<td align="right">117,023,026</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">804,116,537</td>
<td align="right">822,228,431</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">699,641,049</td>
<td align="right">715,351,580</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,164,361,704</td>
<td align="right">3,235,076,142</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,291,729,900</td>
<td align="right">8,475,252,679</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">335,102,515</td>
<td align="right">342,463,980</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">335,102,515</td>
<td align="right">342,463,980</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">647,621,293</td>
<td align="right">661,318,762</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">41,136,670</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,018,614,402</td>
<td align="right">1,039,376,687</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">152,316,325</td>
<td align="right">155,309,902</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">897,064,751</td>
<td align="right">913,462,205</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,168,877</td>
<td align="right">225,179,051</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,498,364</td>
<td align="right">57,509,068</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">792,388,041</td>
<td align="right">806,329,655</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">512,141,453</td>
<td align="right">520,819,075</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,931,056,668</td>
<td align="right">1,963,445,461</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">27,399,871,780</td>
<td align="right">27,859,360,080</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,228,655,055</td>
<td align="right">9,378,600,426</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,722</td>
<td align="right">72,418,718</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,722</td>
<td align="right">72,418,718</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40,020,812</td>
<td align="right">40,613,709</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">751,159,527</td>
<td align="right">762,248,237</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,372,574,706</td>
<td align="right">5,444,847,104</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,009,364,260</td>
<td align="right">1,022,765,609</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">407,149,057</td>
<td align="right">401,824,285</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,098,453,291</td>
<td align="right">4,150,288,697</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">429,163,260</td>
<td align="right">434,428,987</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,679,343</td>
<td align="right">585,685,342</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,679,343</td>
<td align="right">585,685,342</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">435,980,853</td>
<td align="right">441,230,741</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">10,336,097</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">10,336,097</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,466,054,139</td>
<td align="right">1,483,424,954</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,088,378,371</td>
<td align="right">1,101,268,219</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,451,322</td>
<td align="right">551,872,932</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">724,817,766</td>
<td align="right">733,289,517</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,598,056,215</td>
<td align="right">4,651,785,687</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">537,547,034</td>
<td align="right">543,605,812</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,223,507,083</td>
<td align="right">1,236,853,712</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,088,714,988</td>
<td align="right">2,111,471,610</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,692,130,868</td>
<td align="right">1,708,961,761</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,043,455,492</td>
<td align="right">1,053,450,275</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">72,044,046</td>
<td align="right">72,726,488</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">112,412,820</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,218,075,794</td>
<td align="right">4,252,647,403</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,291,475</td>
<td align="right">571,767,545</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,425,188</td>
<td align="right">40,741,863</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,370,381,952</td>
<td align="right">1,381,095,549</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,292,245,339</td>
<td align="right">4,324,322,650</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,137,470</td>
<td align="right">311,274,379</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,910,252,183</td>
<td align="right">2,927,991,995</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,197,360,159</td>
<td align="right">9,252,640,984</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right">389,127,168</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,902,173,649</td>
<td align="right">1,913,150,517</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,834,293,059</td>
<td align="right">1,844,483,259</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,815,295,402</td>
<td align="right">3,836,470,018</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,858,656,457</td>
<td align="right">1,868,777,117</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,297</td>
<td align="right">97,628,966</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">124,152,440</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,471,626,068</td>
<td align="right">2,483,799,023</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,250,563</td>
<td align="right">1,256,504</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">351,243,134</td>
<td align="right">352,900,574</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,005,690,649</td>
<td align="right">3,019,486,836</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">287,427,225</td>
<td align="right">288,642,791</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,259,606</td>
<td align="right">24,358,239</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,120,759</td>
<td align="right">1,357,371,050</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">801,565,648</td>
<td align="right">804,255,277</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,073,681,864</td>
<td align="right">2,080,067,373</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">992,152,700</td>
<td align="right">995,130,539</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,252</td>
<td align="right">172,594,565</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,431,556</td>
<td align="right">1,565,998,388</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">495,343,741</td>
<td align="right">496,395,231</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,392,486</td>
<td align="right">78,271,558</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">166,663,013</td>
<td align="right">166,906,213</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">297,243,980</td>
<td align="right">297,654,238</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">297,026,030</td>
<td align="right">297,419,278</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">62,545,882</td>
<td align="right">62,469,317</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,880</td>
<td align="right">52,133,220</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,903,678,697</td>
<td align="right">4,908,153,700</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,748,929</td>
<td align="right">97,768,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,748,929</td>
<td align="right">97,768,910</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">500,330,181</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">209,319,858</td>
<td align="right">209,356,409</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right">3,579,480</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,278,600</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">47,062,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">444,211,436</td>
<td align="right">444,211,256</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,263,237</td>
<td align="right">269,263,286</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">42,557,190</td>
<td align="right">42,557,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,891,960</td>
<td align="right">3,891,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,891,960</td>
<td align="right">3,891,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,840,960</td>
<td align="right">3,840,960</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">815,372</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">764,033</td>
<td align="right">764,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">764,033</td>
<td align="right">764,033</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right">123,165</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right"></td>
<td align="right">165,878</td>
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
<td align="right">7,176</td>
<td align="right">3,107</td>
<td align="right">-56.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,523</td>
<td align="right">24,196</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,430</td>
<td align="right">23,507</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
<td align="right">84</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right"></td>
<td align="right">20</td>
<td align="right"></td>
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
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">160</td>
<td align="right">160</td>
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
<td align="right">2,476</td>
<td align="right">2,476</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2025-02-06
