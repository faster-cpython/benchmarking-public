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
<td align="right">33,292,776</td>
<td align="right">2,088,456</td>
<td align="right">-93.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,054,098</td>
<td align="right">16,985,682</td>
<td align="right">-93.6%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,314,940</td>
<td align="right">3,110,900</td>
<td align="right">-90.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,637,073</td>
<td align="right">18,513,222</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">49,176,329</td>
<td align="right">5,934,301</td>
<td align="right">-87.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,311,881</td>
<td align="right">20,637,826</td>
<td align="right">-87.8%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,816,132</td>
<td align="right">16,092,248</td>
<td align="right">-84.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,962,529</td>
<td align="right">250,885,217</td>
<td align="right">-76.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,154,667</td>
<td align="right">54,812,490</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">251,870,320</td>
<td align="right">60,322,311</td>
<td align="right">-76.1%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,953,506</td>
<td align="right">2,672,367</td>
<td align="right">-75.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,614,494</td>
<td align="right">34,981,590</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,942,423</td>
<td align="right">1,098,962</td>
<td align="right">-72.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,753,893</td>
<td align="right">21,486,083</td>
<td align="right">-70.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">153,460,109</td>
<td align="right">46,629,314</td>
<td align="right">-69.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">81,668,644</td>
<td align="right">28,331,545</td>
<td align="right">-65.3%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">331,490,771</td>
<td align="right">127,760,573</td>
<td align="right">-61.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">277,086,181</td>
<td align="right">107,435,729</td>
<td align="right">-61.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,918,843</td>
<td align="right">44,648,011</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,396,085</td>
<td align="right">46,447,430</td>
<td align="right">-61.1%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">8,983,194</td>
<td align="right">3,640,543</td>
<td align="right">-59.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,480,882</td>
<td align="right">29,358,060</td>
<td align="right">-56.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,839,537</td>
<td align="right">7,793,189</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">173,135,688</td>
<td align="right">82,394,876</td>
<td align="right">-52.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,132,001</td>
<td align="right">12,157,298</td>
<td align="right">-51.6%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">710,019,358</td>
<td align="right">348,664,984</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">309,508,795</td>
<td align="right">152,095,196</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">271,110,400</td>
<td align="right">134,845,802</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">126,713,082</td>
<td align="right">63,987,318</td>
<td align="right">-49.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,825,535</td>
<td align="right">228,616,179</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,850,351,068</td>
<td align="right">2,009,993,624</td>
<td align="right">-47.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,932,439,714</td>
<td align="right">1,022,444,348</td>
<td align="right">-47.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">853,354,224</td>
<td align="right">455,841,689</td>
<td align="right">-46.6%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,126,358,381</td>
<td align="right">1,690,130,505</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">443,811,314</td>
<td align="right">240,356,594</td>
<td align="right">-45.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">61,556,334</td>
<td align="right">33,890,894</td>
<td align="right">-44.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">485,573,232</td>
<td align="right">270,340,148</td>
<td align="right">-44.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">55,581,769</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,875,422</td>
<td align="right">29,810,266</td>
<td align="right">-42.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,828,646,805</td>
<td align="right">2,788,874,229</td>
<td align="right">-42.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">131,662,812</td>
<td align="right">76,698,766</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">266,180,149</td>
<td align="right">156,098,080</td>
<td align="right">-41.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">300,978,820</td>
<td align="right">176,610,240</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">609,737,015</td>
<td align="right">359,376,334</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,219,484,908</td>
<td align="right">1,903,324,338</td>
<td align="right">-40.9%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">182,853,931</td>
<td align="right">109,444,815</td>
<td align="right">-40.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">67,248,577</td>
<td align="right">40,485,703</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,928,977</td>
<td align="right">240,719,751</td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,490,327,013</td>
<td align="right">1,531,783,500</td>
<td align="right">-38.5%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">186,967,301</td>
<td align="right">115,570,151</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">70,428,642</td>
<td align="right">44,066,979</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,514,179</td>
<td align="right">140,270,468</td>
<td align="right">-37.2%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">18,278,762</td>
<td align="right">25,061,800</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,037,815,815</td>
<td align="right">1,286,286,790</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,787,068,530</td>
<td align="right">1,141,920,707</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,900,042,414</td>
<td align="right">8,979,303,475</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,170,212,384</td>
<td align="right">1,419,081,116</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,399,659</td>
<td align="right">43,278,763</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">644,784,750</td>
<td align="right">426,820,669</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,906,638</td>
<td align="right">514,541,168</td>
<td align="right">-33.8%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,136,089</td>
<td align="right">46,467,403</td>
<td align="right">-33.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105,047,934</td>
<td align="right">69,798,116</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">225,758,560</td>
<td align="right">150,836,288</td>
<td align="right">-33.2%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">137,620,387</td>
<td align="right">92,065,442</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,355,000</td>
<td align="right">70,791,780</td>
<td align="right">-31.5%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,872,998</td>
<td align="right">122,871,566</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">406,864,138</td>
<td align="right">279,635,786</td>
<td align="right">-31.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,054,539</td>
<td align="right">2,791,199</td>
<td align="right">-31.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">539,623,241</td>
<td align="right">372,034,020</td>
<td align="right">-31.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,975,070</td>
<td align="right">55,374,984</td>
<td align="right">-30.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,801,646,240</td>
<td align="right">1,946,888,622</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">628,725,042</td>
<td align="right">437,287,509</td>
<td align="right">-30.4%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">716,586,005</td>
<td align="right">506,285,635</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,957,136</td>
<td align="right">67,800,396</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,281,409,095</td>
<td align="right">907,208,441</td>
<td align="right">-29.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">659,760,007</td>
<td align="right">471,953,477</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,492,839,321</td>
<td align="right">1,069,299,272</td>
<td align="right">-28.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,616,965,219</td>
<td align="right">1,175,343,042</td>
<td align="right">-27.3%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,201,583</td>
<td align="right">49,648,747</td>
<td align="right">-27.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">292,384,892</td>
<td align="right">213,487,393</td>
<td align="right">-27.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">61,655,295</td>
<td align="right">45,244,877</td>
<td align="right">-26.6%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">67,954,617</td>
<td align="right">49,964,797</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,362,280</td>
<td align="right">70,143,029</td>
<td align="right">-26.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">88,428,906</td>
<td align="right">65,225,506</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,539,258</td>
<td align="right">42,505,101</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">352,615,647</td>
<td align="right">262,062,722</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">321,142,729</td>
<td align="right">240,764,938</td>
<td align="right">-25.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">209,998,657</td>
<td align="right">158,094,329</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,318,538,692</td>
<td align="right">1,750,750,608</td>
<td align="right">-24.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,623,281</td>
<td align="right">251,463,458</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">250,328,302</td>
<td align="right">191,850,679</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,767</td>
<td align="right">18,165,426</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">173,416,046</td>
<td align="right">135,562,761</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">214,704,236</td>
<td align="right">169,305,836</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,706,045</td>
<td align="right">9,235,237</td>
<td align="right">-21.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,906,067</td>
<td align="right">110,677,932</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">113,206,776</td>
<td align="right">91,643,416</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,857,063,664</td>
<td align="right">3,122,518,260</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">701,413,824</td>
<td align="right">568,777,916</td>
<td align="right">-18.9%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">57,578,089</td>
<td align="right">47,629,914</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">534,473,288</td>
<td align="right">453,176,472</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,975,533</td>
<td align="right">51,729,879</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,852,808</td>
<td align="right">16,068,193</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,623,464</td>
<td align="right">134,346,292</td>
<td align="right">-14.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">429,246,501</td>
<td align="right">366,975,736</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,806,275</td>
<td align="right">31,547,107</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,173</td>
<td align="right">1,794,144</td>
<td align="right">-14.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,340,902</td>
<td align="right">31,642,151</td>
<td align="right">-12.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,245,163</td>
<td align="right">3,707,108</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">307,983,208</td>
<td align="right">272,143,777</td>
<td align="right">-11.6%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">328,341,453</td>
<td align="right">290,795,512</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,899</td>
<td align="right">268,172,859</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,841,683</td>
<td align="right">61,962,563</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">171,729,919</td>
<td align="right">190,301,661</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,519,766</td>
<td align="right">85,337,108</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,780,804</td>
<td align="right">131,710,186</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">143,907,591</td>
<td align="right">130,713,964</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,613,354</td>
<td align="right">53,255,091</td>
<td align="right">-9.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,924,953</td>
<td align="right">53,808,886</td>
<td align="right">-8.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,855,922</td>
<td align="right">90,705,148</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,362,171</td>
<td align="right">25,327,080</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">155,964,783</td>
<td align="right">145,923,957</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,764,694</td>
<td align="right">12,881,152</td>
<td align="right">-6.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">236,624,899</td>
<td align="right">222,340,565</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">159,730,031</td>
<td align="right">150,883,472</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">902,749,617</td>
<td align="right">854,915,114</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,635,022</td>
<td align="right">46,244,173</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,781,911</td>
<td align="right">64,156,396</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,294,673</td>
<td align="right">9,941,846</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">328,953,526</td>
<td align="right">318,776,687</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,042,901</td>
<td align="right">109,268,656</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,637,720</td>
<td align="right">116,239,209</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,873,138</td>
<td align="right">26,371,246</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,730,820</td>
<td align="right">36,116,910</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,054</td>
<td align="right">203,231,347</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,880,523</td>
<td align="right">31,438,673</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,365,943</td>
<td align="right">26,680,954</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">168,317,044</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,236,394</td>
<td align="right">58,809,113</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,643,198</td>
<td align="right">79,074,544</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,954,636</td>
<td align="right">3,926,506</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,221,107</td>
<td align="right">9,182,015</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,741,906</td>
<td align="right">9,702,942</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,144</td>
<td align="right">5,150</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,516,819</td>
<td align="right">180,433,231</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,709</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,620,628,272</td>
<td align="right">1,620,037,288</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,131</td>
<td align="right">133,167</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,737</td>
<td align="right">33,745</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,606</td>
<td align="right">405,671</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,877,945</td>
<td align="right">20,874,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,614,787</td>
<td align="right">36,610,463</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,700</td>
<td align="right">773,613</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,660,466</td>
<td align="right">42,656,139</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,773,878</td>
<td align="right">21,775,983</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">57,147</td>
<td align="right">57,144</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,911</td>
<td align="right">1,439,847</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,547,461</td>
<td align="right">20,546,608</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,965</td>
<td align="right">20,877,112</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,856</td>
<td align="right">120,860</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,321,534</td>
<td align="right">242,327,658</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,829,679</td>
<td align="right">4,829,562</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,150</td>
<td align="right">3,115,107</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,193</td>
<td align="right">14,760,309</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,060</td>
<td align="right">2,573,080</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,913</td>
<td align="right">6,169,883</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">236,754</td>
<td align="right">236,753</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,911</td>
<td align="right">4,866,899</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,677</td>
<td align="right">128,851,673</td>
<td align="right">-0.0%</td>
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
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,923</td>
<td align="right">1,645,923</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,194,074</td>
<td align="right">1,194,074</td>
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
<td align="right">50,997,629</td>
<td align="right">0.6%</td>
<td align="right">30,233,200</td>
<td align="right">0.4%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">330,461,515</td>
<td align="right">4.1%</td>
<td align="right">251,323,773</td>
<td align="right">3.2%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,641,211,651</td>
<td align="right">95.2%</td>
<td align="right">7,607,059,422</td>
<td align="right">96.4%</td>
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
<td align="right">970,775</td>
<td align="right">86.4%</td>
<td align="right">579,058</td>
<td align="right">81.5%</td>
<td align="right">-40.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">153,174</td>
<td align="right">13.6%</td>
<td align="right">131,054</td>
<td align="right">18.5%</td>
<td align="right">-14.4%</td>
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
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">2,633</td>
<td align="right">2.0%</td>
<td align="right">-59.9%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,474</td>
<td align="right">15.3%</td>
<td align="right">13,914</td>
<td align="right">10.6%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">3,151</td>
<td align="right">2.4%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">2,470</td>
<td align="right">1.9%</td>
<td align="right">-22.2%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">1,930</td>
<td align="right">1.5%</td>
<td align="right">-17.6%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">5,458</td>
<td align="right">3.6%</td>
<td align="right">4,662</td>
<td align="right">3.6%</td>
<td align="right">-14.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,059</td>
<td align="right">13.1%</td>
<td align="right">17,300</td>
<td align="right">13.2%</td>
<td align="right">-13.8%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">3,188</td>
<td align="right">2.4%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">15,023</td>
<td align="right">11.5%</td>
<td align="right">-11.7%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">1,284</td>
<td align="right">1.0%</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,718</td>
<td align="right">3.7%</td>
<td align="right">5,475</td>
<td align="right">4.2%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,830</td>
<td align="right">12.9%</td>
<td align="right">19,031</td>
<td align="right">14.5%</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">821</td>
<td align="right">0.6%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">495</td>
<td align="right">0.3%</td>
<td align="right">489</td>
<td align="right">0.4%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,767</td>
<td align="right">11.6%</td>
<td align="right">17,725</td>
<td align="right">13.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.4%</td>
<td align="right">628</td>
<td align="right">0.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,469</td>
<td align="right">12.1%</td>
<td align="right">18,445</td>
<td align="right">14.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">1.3%</td>
<td align="right">1,996</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">597</td>
<td align="right">0.5%</td>
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
<td align="right">97,359,536</td>
<td align="right">100.0%</td>
<td align="right">55,581,769</td>
<td align="right">100.0%</td>
<td align="right">-42.9%</td>
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
<td align="right">451,674,365</td>
<td align="right">7.6%</td>
<td align="right">228,519,546</td>
<td align="right">4.0%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,470,814,679</td>
<td align="right">92.3%</td>
<td align="right">5,449,224,129</td>
<td align="right">95.9%</td>
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
<td align="right">5,824,996</td>
<td align="right">0.1%</td>
<td align="right">5,825,365</td>
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
<td align="right">141,932</td>
<td align="right">54.4%</td>
<td align="right">87,390</td>
<td align="right">42.4%</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,913</td>
<td align="right">45.6%</td>
<td align="right">118,938</td>
<td align="right">57.6%</td>
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
<td align="left">array int</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">1,095</td>
<td align="right">1.3%</td>
<td align="right">-93.4%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,443</td>
<td align="right">8.8%</td>
<td align="right">2,105</td>
<td align="right">2.4%</td>
<td align="right">-83.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,055</td>
<td align="right">24.7%</td>
<td align="right">17,952</td>
<td align="right">20.5%</td>
<td align="right">-48.8%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">608</td>
<td align="right">0.7%</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,676</td>
<td align="right">42.0%</td>
<td align="right">48,275</td>
<td align="right">55.2%</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,677</td>
<td align="right">2.6%</td>
<td align="right">3,591</td>
<td align="right">4.1%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,096</td>
<td align="right">5.0%</td>
<td align="right">7,141</td>
<td align="right">8.2%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.5%</td>
<td align="right">3,589</td>
<td align="right">4.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">2,941</td>
<td align="right">3.4%</td>
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
<td align="right">127,081,937</td>
<td align="right">1.1%</td>
<td align="right">111,749,351</td>
<td align="right">1.0%</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">124,915,318</td>
<td align="right">1.1%</td>
<td align="right">109,872,043</td>
<td align="right">1.0%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">11,099,044,527</td>
<td align="right">98.9%</td>
<td align="right">11,093,546,761</td>
<td align="right">99.0%</td>
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
<td align="right">2,571,779</td>
<td align="right">100.0%</td>
<td align="right">2,282,533</td>
<td align="right">100.0%</td>
<td align="right">-11.2%</td>
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
<td align="right">684,424</td>
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
<td align="right">20,160</td>
<td align="right">99.4%</td>
<td align="right">20,162</td>
<td align="right">99.4%</td>
<td align="right">0.0%</td>
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
<td align="right">88,305,264</td>
<td align="right">1.9%</td>
<td align="right">65,120,677</td>
<td align="right">1.4%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,276,958</td>
<td align="right">0.0%</td>
<td align="right">966,257</td>
<td align="right">0.0%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,517,475,973</td>
<td align="right">98.1%</td>
<td align="right">4,516,551,283</td>
<td align="right">98.6%</td>
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
<td align="right">105,394</td>
<td align="right">71.5%</td>
<td align="right">86,598</td>
<td align="right">70.5%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42,019</td>
<td align="right">28.5%</td>
<td align="right">36,168</td>
<td align="right">29.5%</td>
<td align="right">-13.9%</td>
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
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">1,347</td>
<td align="right">1.6%</td>
<td align="right">-82.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">601</td>
<td align="right">0.7%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,405</td>
<td align="right">8.0%</td>
<td align="right">4,722</td>
<td align="right">5.5%</td>
<td align="right">-43.8%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,162</td>
<td align="right">22.0%</td>
<td align="right">16,347</td>
<td align="right">18.9%</td>
<td align="right">-29.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,547</td>
<td align="right">4.3%</td>
<td align="right">4,095</td>
<td align="right">4.7%</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">984</td>
<td align="right">0.9%</td>
<td align="right">930</td>
<td align="right">1.1%</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
<td align="right">6,162</td>
<td align="right">7.1%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,715</td>
<td align="right">7.3%</td>
<td align="right">7,458</td>
<td align="right">8.6%</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">359</td>
<td align="right">0.3%</td>
<td align="right">362</td>
<td align="right">0.4%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,657</td>
<td align="right">41.4%</td>
<td align="right">43,306</td>
<td align="right">50.0%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">941</td>
<td align="right">0.9%</td>
<td align="right">934</td>
<td align="right">1.1%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">334</td>
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
<td align="right">57,540,410</td>
<td align="right">2.6%</td>
<td align="right">47,594,731</td>
<td align="right">2.1%</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,189,526,257</td>
<td align="right">97.4%</td>
<td align="right">2,189,391,404</td>
<td align="right">97.8%</td>
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
<td align="right">35,418</td>
<td align="right">48.0%</td>
<td align="right">32,922</td>
<td align="right">46.1%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">52.0%</td>
<td align="right">38,435</td>
<td align="right">53.9%</td>
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
<td align="right">7,197</td>
<td align="right">20.3%</td>
<td align="right">5,556</td>
<td align="right">16.9%</td>
<td align="right">-22.8%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,166</td>
<td align="right">25.9%</td>
<td align="right">8,526</td>
<td align="right">25.9%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,856</td>
<td align="right">22.2%</td>
<td align="right">7,739</td>
<td align="right">23.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,199</td>
<td align="right">31.6%</td>
<td align="right">11,101</td>
<td align="right">33.7%</td>
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
<td align="right">32,339,644</td>
<td align="right">4.3%</td>
<td align="right">24,804,696</td>
<td align="right">3.7%</td>
<td align="right">-23.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">603,087,829</td>
<td align="right">80.0%</td>
<td align="right">528,717,359</td>
<td align="right">78.9%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">118,541,268</td>
<td align="right">15.7%</td>
<td align="right">116,145,121</td>
<td align="right">17.3%</td>
<td align="right">-2.0%</td>
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
<td align="right">615,107</td>
<td align="right">87.1%</td>
<td align="right">472,958</td>
<td align="right">84.2%</td>
<td align="right">-23.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,376</td>
<td align="right">12.9%</td>
<td align="right">89,002</td>
<td align="right">15.8%</td>
<td align="right">-2.6%</td>
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
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">1,325</td>
<td align="right">1.5%</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,164</td>
<td align="right">6.7%</td>
<td align="right">4,275</td>
<td align="right">4.8%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,495</td>
<td align="right">4.9%</td>
<td align="right">3,303</td>
<td align="right">3.7%</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,547</td>
<td align="right">1.7%</td>
<td align="right">1,247</td>
<td align="right">1.4%</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.4%</td>
<td align="right">369</td>
<td align="right">0.4%</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.5%</td>
<td align="right">2,351</td>
<td align="right">2.6%</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,734</td>
<td align="right">11.7%</td>
<td align="right">10,368</td>
<td align="right">11.6%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,895</td>
<td align="right">6.5%</td>
<td align="right">6,049</td>
<td align="right">6.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">5.0%</td>
<td align="right">4,628</td>
<td align="right">5.2%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">48,286</td>
<td align="right">52.8%</td>
<td align="right">48,917</td>
<td align="right">55.0%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.1%</td>
<td align="right">2,847</td>
<td align="right">3.2%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.3%</td>
<td align="right">3,015</td>
<td align="right">3.4%</td>
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
<td align="right">642,829,921</td>
<td align="right">4.8%</td>
<td align="right">518,551,086</td>
<td align="right">4.0%</td>
<td align="right">-19.3%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">532,847,492</td>
<td align="right">4.0%</td>
<td align="right">451,569,846</td>
<td align="right">3.5%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,094,784,929</td>
<td align="right">91.1%</td>
<td align="right">12,068,050,875</td>
<td align="right">92.5%</td>
<td align="right">-0.2%</td>
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
<td align="left">Success</td>
<td align="right">12,215,258</td>
<td align="right">97.2%</td>
<td align="right">9,870,988</td>
<td align="right">96.7%</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">355,119</td>
<td align="right">2.8%</td>
<td align="right">333,937</td>
<td align="right">3.3%</td>
<td align="right">-6.0%</td>
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
<td align="right">38,455</td>
<td align="right">10.8%</td>
<td align="right">26,398</td>
<td align="right">7.9%</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,536</td>
<td align="right">4.1%</td>
<td align="right">12,984</td>
<td align="right">3.9%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,050</td>
<td align="right">16.9%</td>
<td align="right">55,967</td>
<td align="right">16.8%</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,702</td>
<td align="right">11.5%</td>
<td align="right">39,137</td>
<td align="right">11.7%</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,828</td>
<td align="right">6.7%</td>
<td align="right">24,710</td>
<td align="right">7.4%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">855</td>
<td align="right">0.2%</td>
<td align="right">883</td>
<td align="right">0.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,912</td>
<td align="right">1.4%</td>
<td align="right">4,978</td>
<td align="right">1.5%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,608</td>
<td align="right">0.5%</td>
<td align="right">1,589</td>
<td align="right">0.5%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,404</td>
<td align="right">0.7%</td>
<td align="right">2,432</td>
<td align="right">0.7%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,945</td>
<td align="right">2.2%</td>
<td align="right">7,939</td>
<td align="right">2.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">6,405</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,087</td>
<td align="right">1.4%</td>
<td align="right">5,087</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">1,582</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,092</td>
<td align="right">0.3%</td>
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
<td align="right">3,771,214,923</td>
<td align="right">99.6%</td>
<td align="right">2,619,845,025</td>
<td align="right">99.4%</td>
<td align="right">-30.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,622,703</td>
<td align="right">0.4%</td>
<td align="right">14,622,775</td>
<td align="right">0.6%</td>
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
<td align="right">138,257</td>
<td align="right">100.0%</td>
<td align="right">138,297</td>
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
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">253</td>
<td align="right">0.0%</td>
<td align="right">254</td>
<td align="right">0.0%</td>
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
<td align="right">65,094,554</td>
<td align="right">100.0%</td>
<td align="right">64,882,818</td>
<td align="right">100.0%</td>
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
<td align="right">593,288,722</td>
<td align="right">82.2%</td>
<td align="right">593,288,686</td>
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
<td align="right">128,816,906</td>
<td align="right">17.8%</td>
<td align="right">128,816,902</td>
<td align="right">17.8%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">115,910,174</td>
<td align="right">5.7%</td>
<td align="right">86,097,203</td>
<td align="right">4.3%</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">69,748,569</td>
<td align="right">3.4%</td>
<td align="right">61,871,425</td>
<td align="right">3.1%</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,845,640,262</td>
<td align="right">90.9%</td>
<td align="right">1,873,949,681</td>
<td align="right">92.7%</td>
<td align="right">1.5%</td>
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
<td align="right">2,228,397</td>
<td align="right">97.8%</td>
<td align="right">1,665,899</td>
<td align="right">97.1%</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">50,961</td>
<td align="right">2.2%</td>
<td align="right">48,986</td>
<td align="right">2.9%</td>
<td align="right">-3.9%</td>
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
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">3,198</td>
<td align="right">6.5%</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">619</td>
<td align="right">1.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">135,470</td>
<td align="right">265.8%</td>
<td align="right">132,564</td>
<td align="right">270.6%</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,566</td>
<td align="right">15.4%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">361</td>
<td align="right">0.7%</td>
<td align="right">365</td>
<td align="right">0.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">24,176</td>
<td align="right">49.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">4,953</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,344</td>
<td align="right">6.6%</td>
<td align="right">3,344</td>
<td align="right">6.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">1,619</td>
<td align="right">3.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">810</td>
<td align="right">1.6%</td>
<td align="right">810</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">730</td>
<td align="right">1.4%</td>
<td align="right">730</td>
<td align="right">1.5%</td>
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
<td align="right">1,194,074</td>
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
<td align="right">133,568,563</td>
<td align="right">12.7%</td>
<td align="right">34,959,637</td>
<td align="right">3.7%</td>
<td align="right">-73.8%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">920,422,644</td>
<td align="right">87.3%</td>
<td align="right">912,860,215</td>
<td align="right">96.3%</td>
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
<td align="right">43,776</td>
<td align="right">95.2%</td>
<td align="right">19,799</td>
<td align="right">90.0%</td>
<td align="right">-54.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,195</td>
<td align="right">4.8%</td>
<td align="right">2,194</td>
<td align="right">10.0%</td>
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
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">1,473</td>
<td align="right">7.4%</td>
<td align="right">-81.9%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">14,752</td>
<td align="right">33.7%</td>
<td align="right">3,255</td>
<td align="right">16.4%</td>
<td align="right">-77.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">2,012</td>
<td align="right">10.2%</td>
<td align="right">-33.6%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">11,913</td>
<td align="right">60.2%</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">501</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">341</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">236</td>
<td align="right">1.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.3%</td>
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
<td align="right">102,891,601</td>
<td align="right">2.2%</td>
<td align="right">70,330,720</td>
<td align="right">1.6%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">40,958,294</td>
<td align="right">0.9%</td>
<td align="right">37,258,584</td>
<td align="right">0.8%</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,531,475,523</td>
<td align="right">96.9%</td>
<td align="right">4,276,773,146</td>
<td align="right">97.5%</td>
<td align="right">-5.6%</td>
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
<td align="right">821,423</td>
<td align="right">66.5%</td>
<td align="right">751,649</td>
<td align="right">64.7%</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">413,283</td>
<td align="right">33.5%</td>
<td align="right">410,912</td>
<td align="right">35.3%</td>
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
<td align="left">float</td>
<td align="right">382</td>
<td align="right">0.1%</td>
<td align="right">22</td>
<td align="right">0.0%</td>
<td align="right">-94.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,408</td>
<td align="right">4.0%</td>
<td align="right">21,755</td>
<td align="right">5.3%</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,689</td>
<td align="right">1.4%</td>
<td align="right">5,147</td>
<td align="right">1.3%</td>
<td align="right">-9.5%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,475</td>
<td align="right">3.3%</td>
<td align="right">12,519</td>
<td align="right">3.0%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,063</td>
<td align="right">22.8%</td>
<td align="right">88,304</td>
<td align="right">21.5%</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,611</td>
<td align="right">2.1%</td>
<td align="right">8,258</td>
<td align="right">2.0%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,361</td>
<td align="right">3.0%</td>
<td align="right">12,339</td>
<td align="right">3.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">256,193</td>
<td align="right">62.0%</td>
<td align="right">256,467</td>
<td align="right">62.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,233,606,829</td>
<td align="right">99.9%</td>
<td align="right">950,589,326</td>
<td align="right">99.8%</td>
<td align="right">-22.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">1,427,528</td>
<td align="right">0.1%</td>
<td align="right">1,427,462</td>
<td align="right">0.1%</td>
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
<td align="right">862</td>
<td align="right">6.9%</td>
<td align="right">856</td>
<td align="right">6.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
<td align="right">11,609</td>
<td align="right">93.1%</td>
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
<td align="left">sequence</td>
<td align="right">635</td>
<td align="right">73.7%</td>
<td align="right">629</td>
<td align="right">73.5%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.6%</td>
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
<td align="right">46,978,557,389</td>
<td align="right">58.3%</td>
<td align="right">29,654,679,052</td>
<td align="right">56.1%</td>
<td align="right">-36.9%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,418,392,874</td>
<td align="right">37.8%</td>
<td align="right">20,820,117,112</td>
<td align="right">39.4%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">2,132,512,557</td>
<td align="right">2.6%</td>
<td align="right">1,532,443,583</td>
<td align="right">2.9%</td>
<td align="right">-28.1%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">1,019,951,052</td>
<td align="right">1.3%</td>
<td align="right">818,246,356</td>
<td align="right">1.5%</td>
<td align="right">-19.8%</td>
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
<td align="right">451,674,365</td>
<td align="right">20.0%</td>
<td align="right">228,519,546</td>
<td align="right">13.9%</td>
<td align="right">-49.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">4.3%</td>
<td align="right">55,581,769</td>
<td align="right">3.4%</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,891,601</td>
<td align="right">4.6%</td>
<td align="right">70,330,720</td>
<td align="right">4.3%</td>
<td align="right">-31.6%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">88,305,264</td>
<td align="right">3.9%</td>
<td align="right">65,120,677</td>
<td align="right">4.0%</td>
<td align="right">-26.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,461,515</td>
<td align="right">14.7%</td>
<td align="right">251,323,773</td>
<td align="right">15.3%</td>
<td align="right">-23.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">532,847,492</td>
<td align="right">23.6%</td>
<td align="right">451,569,846</td>
<td align="right">27.5%</td>
<td align="right">-15.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">124,915,318</td>
<td align="right">5.5%</td>
<td align="right">109,872,043</td>
<td align="right">6.7%</td>
<td align="right">-12.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,541,268</td>
<td align="right">5.3%</td>
<td align="right">116,145,121</td>
<td align="right">7.1%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,906</td>
<td align="right">5.7%</td>
<td align="right">128,816,902</td>
<td align="right">7.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,568,563</td>
<td align="right">5.9%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">61,871,425</td>
<td align="right">3.8%</td>
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
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,415,263</td>
<td align="right">2.4%</td>
<td align="right">15,834,079</td>
<td align="right">1.9%</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">184,014,368</td>
<td align="right">18.0%</td>
<td align="right">130,024,507</td>
<td align="right">15.9%</td>
<td align="right">-29.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">255,322,860</td>
<td align="right">25.0%</td>
<td align="right">181,749,486</td>
<td align="right">22.2%</td>
<td align="right">-28.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,274,265</td>
<td align="right">9.2%</td>
<td align="right">71,397,725</td>
<td align="right">8.7%</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,073,265</td>
<td align="right">6.8%</td>
<td align="right">56,621,609</td>
<td align="right">6.9%</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,730,649</td>
<td align="right">7.4%</td>
<td align="right">83,900,929</td>
<td align="right">10.3%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,458,461</td>
<td align="right">7.3%</td>
<td align="right">71,284,431</td>
<td align="right">8.7%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,239,806</td>
<td align="right">2.1%</td>
<td align="right">21,043,444</td>
<td align="right">2.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,947</td>
<td align="right">2.0%</td>
<td align="right">20,872,856</td>
<td align="right">2.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">21,600,374</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,177,303</td>
<td align="right">2.2%</td>
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
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,068,170,298</td>
<td align="right">75.7%</td>
<td align="right">5,024,262,234</td>
<td align="right">75.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,462,609,859</td>
<td align="right">81.6%</td>
<td align="right">5,418,173,538</td>
<td align="right">81.5%</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,386,706</td>
<td align="right">4.2%</td>
<td align="right">279,149,269</td>
<td align="right">4.2%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,634,001</td>
<td align="right">1.1%</td>
<td align="right">71,576,951</td>
<td align="right">1.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">952,563,525</td>
<td align="right">14.2%</td>
<td align="right">952,030,165</td>
<td align="right">14.3%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">954,695,668</td>
<td align="right">14.3%</td>
<td align="right">954,162,308</td>
<td align="right">14.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,624,656,902</td>
<td align="right">24.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,624,656,902</td>
<td align="right">24.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,580,347</td>
<td align="right">10.0%</td>
<td align="right">670,494,594</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,432</td>
<td align="right">0.4%</td>
<td align="right">24,922,275</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,948</td>
<td align="right">3.9%</td>
<td align="right">261,407,401</td>
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
<td align="left">Interpreter mortal increfs</td>
<td align="right">35,930,617,616</td>
<td align="right">22.4%</td>
<td align="right">24,930,339,847</td>
<td align="right">15.3%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,925,103,433</td>
<td align="right">5.6%</td>
<td align="right">6,333,673,551</td>
<td align="right">3.9%</td>
<td align="right">-29.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,516,176,225</td>
<td align="right">8.2%</td>
<td align="right">13,153,939,412</td>
<td align="right">6.5%</td>
<td align="right">-20.4%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">77,400,036,232</td>
<td align="right">48.2%</td>
<td align="right">91,029,488,095</td>
<td align="right">55.9%</td>
<td align="right">17.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">47,497,701,691</td>
<td align="right">23.6%</td>
<td align="right">39,358,067,372</td>
<td align="right">19.3%</td>
<td align="right">-17.1%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">82,872,995,483</td>
<td align="right">41.1%</td>
<td align="right">93,920,558,032</td>
<td align="right">46.1%</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,179,985,728</td>
<td align="right"></td>
<td align="right">2,023,818,474</td>
<td align="right"></td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">8,684,176</td>
<td align="right"></td>
<td align="right">8,096,187</td>
<td align="right"></td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">38,388,708,385</td>
<td align="right">23.9%</td>
<td align="right">40,639,533,695</td>
<td align="right">24.9%</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,666,871,820</td>
<td align="right">27.1%</td>
<td align="right">57,293,548,698</td>
<td align="right">28.1%</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,984,653</td>
<td align="right"></td>
<td align="right">64,181,187</td>
<td align="right"></td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,399,378,238</td>
<td align="right">67.1%</td>
<td align="right">12,679,009,173</td>
<td align="right">67.6%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,399,472,251</td>
<td align="right"></td>
<td align="right">12,679,100,182</td>
<td align="right"></td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,109,261</td>
<td align="right"></td>
<td align="right">56,893,658</td>
<td align="right"></td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,996,654</td>
<td align="right"></td>
<td align="right">179,842,470</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,900,013,598</td>
<td align="right"></td>
<td align="right">2,902,003,091</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,515,418</td>
<td align="right">0.4%</td>
<td align="right">71,543,969</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,773</td>
<td align="right">0.0%</td>
<td align="right">6,421,360</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,678,833,154</td>
<td align="right"></td>
<td align="right">6,677,572,316</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,009,403,952</td>
<td align="right">32.5%</td>
<td align="right">6,008,462,769</td>
<td align="right">32.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,087,339,143</td>
<td align="right">32.9%</td>
<td align="right">6,086,428,098</td>
<td align="right">32.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,444,171</td>
<td align="right">2.5%</td>
<td align="right">4,444,171</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
<td align="right">476,016</td>
<td align="right">0.3%</td>
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
<td align="right">364,692</td>
<td align="right">103,237,922</td>
<td align="right">9,561,523,944</td>
<td align="right">364,677</td>
<td align="right">103,222,774</td>
<td align="right">9,556,319,775</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,771,834</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,604,227,272</td>
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
<td align="right">398,075</td>
<td align="right">78.4%</td>
<td align="right">19,891</td>
<td align="right">11.7%</td>
<td align="right">-95.0%</td>
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
<td align="right">961</td>
<td align="right">1.0%</td>
<td align="right">91.8%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">440,533</td>
<td align="right">86.8%</td>
<td align="right">73,293</td>
<td align="right">43.2%</td>
<td align="right">-83.4%</td>
</tr>
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
<td align="right">824</td>
<td align="right">0.5%</td>
<td align="right">-74.6%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">507,615</td>
<td align="right"></td>
<td align="right">169,557</td>
<td align="right"></td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,033,994,861</td>
<td align="right"></td>
<td align="right">10,456,979,845</td>
<td align="right"></td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">838</td>
<td align="right">0.2%</td>
<td align="right">1,236</td>
<td align="right">0.7%</td>
<td align="right">47.5%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">66,774</td>
<td align="right">13.2%</td>
<td align="right">95,905</td>
<td align="right">56.6%</td>
<td align="right">43.6%</td>
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
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">-33.3%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">982</td>
<td align="right">0.2%</td>
<td align="right">1,276</td>
<td align="right">0.8%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">272,384,993,924</td>
<td align="right">3,872.4%</td>
<td align="right">335,528,517,351</td>
<td align="right">3,208.7%</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">308</td>
<td align="right">0.1%</td>
<td align="right">359</td>
<td align="right">0.2%</td>
<td align="right">16.6%</td>
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
<td align="right">60,336</td>
<td align="right">90.4%</td>
<td align="right">88,365</td>
<td align="right">92.1%</td>
<td align="right">46.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">66,774</td>
<td align="right"></td>
<td align="right">95,905</td>
<td align="right"></td>
<td align="right">43.6%</td>
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
<td align="right">5,751</td>
<td align="right">8.6%</td>
<td align="right">6,205</td>
<td align="right">6.5%</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,253</td>
<td align="right">12.4%</td>
<td align="right">18,558</td>
<td align="right">19.4%</td>
<td align="right">124.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">21,525</td>
<td align="right">32.2%</td>
<td align="right">29,455</td>
<td align="right">30.7%</td>
<td align="right">36.8%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,468</td>
<td align="right">24.7%</td>
<td align="right">22,765</td>
<td align="right">23.7%</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,191</td>
<td align="right">13.8%</td>
<td align="right">11,942</td>
<td align="right">12.5%</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,689</td>
<td align="right">7.0%</td>
<td align="right">6,014</td>
<td align="right">6.3%</td>
<td align="right">28.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">815</td>
<td align="right">1.2%</td>
<td align="right">906</td>
<td align="right">0.9%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">60</td>
<td align="right">0.1%</td>
<td align="right">-26.8%</td>
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
<td align="right">1,941</td>
<td align="right">2.9%</td>
<td align="right">2,576</td>
<td align="right">2.7%</td>
<td align="right">32.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,191</td>
<td align="right">12.3%</td>
<td align="right">13,016</td>
<td align="right">13.6%</td>
<td align="right">58.9%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,455</td>
<td align="right">12.7%</td>
<td align="right">15,173</td>
<td align="right">15.8%</td>
<td align="right">79.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,192</td>
<td align="right">36.2%</td>
<td align="right">34,030</td>
<td align="right">35.5%</td>
<td align="right">40.7%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,561</td>
<td align="right">18.8%</td>
<td align="right">16,851</td>
<td align="right">17.6%</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,462</td>
<td align="right">5.2%</td>
<td align="right">4,582</td>
<td align="right">4.8%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,246</td>
<td align="right">1.9%</td>
<td align="right">1,951</td>
<td align="right">2.0%</td>
<td align="right">56.6%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">288</td>
<td align="right">0.4%</td>
<td align="right">186</td>
<td align="right">0.2%</td>
<td align="right">-35.4%</td>
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
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">283,457,935</td>
<td align="right">72,805.8%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">544,397</td>
<td align="right">38,666,627</td>
<td align="right">7,002.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,003,871</td>
<td align="right">10,037,832</td>
<td align="right">899.9%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,667</td>
<td align="right">26,871,089</td>
<td align="right">739.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,169,805</td>
<td align="right">9,277,700</td>
<td align="right">693.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,680,384</td>
<td align="right">175,891,496</td>
<td align="right">642.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right">603,477</td>
<td align="right">390.0%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">576,845,478</td>
<td align="right">2,572,179,478</td>
<td align="right">345.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,574,318</td>
<td align="right">68,911,374</td>
<td align="right">342.5%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,049,568,999</td>
<td align="right">4,613,722,424</td>
<td align="right">339.6%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">26,214,596</td>
<td align="right">106,382,190</td>
<td align="right">305.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,696,290</td>
<td align="right">26,878,589</td>
<td align="right">301.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,724,772</td>
<td align="right">218,523,981</td>
<td align="right">285.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,662,322</td>
<td align="right">80,317,354</td>
<td align="right">254.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,154,665</td>
<td align="right">21,188,538</td>
<td align="right">244.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">181,915</td>
<td align="right">556,495</td>
<td align="right">205.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">37,000,957</td>
<td align="right">109,949,600</td>
<td align="right">197.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">37,001,917</td>
<td align="right">109,950,440</td>
<td align="right">197.1%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,250,836</td>
<td align="right">3,324,789</td>
<td align="right">165.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">152,466,174</td>
<td align="right">403,396,379</td>
<td align="right">164.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">158,515,496</td>
<td align="right">405,862,355</td>
<td align="right">156.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,134,640</td>
<td align="right">79,112,100</td>
<td align="right">154.1%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">29,591,441</td>
<td align="right">74,989,585</td>
<td align="right">153.4%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,705,621</td>
<td align="right">75,979,385</td>
<td align="right">147.4%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">113,182,193</td>
<td align="right">279,579,998</td>
<td align="right">147.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,726,365</td>
<td align="right">457,513,383</td>
<td align="right">133.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,818,123</td>
<td align="right">15,250,716</td>
<td align="right">123.7%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,513,079</td>
<td align="right">41,980,634</td>
<td align="right">104.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right">1,544,928</td>
<td align="right">89.5%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,714,436</td>
<td align="right">12,056,868</td>
<td align="right">79.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">536,303,591</td>
<td align="right">959,440,603</td>
<td align="right">78.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,447,871</td>
<td align="right">51,549,147</td>
<td align="right">75.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,389,039</td>
<td align="right">164,669,308</td>
<td align="right">74.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">504,580,749</td>
<td align="right">876,012,637</td>
<td align="right">73.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,211,904</td>
<td align="right">52,313,180</td>
<td align="right">73.2%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,891,960</td>
<td align="right">6,716,200</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,891,960</td>
<td align="right">6,716,200</td>
<td align="right">72.6%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">335,270,882</td>
<td align="right">568,127,149</td>
<td align="right">69.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">309,438,152</td>
<td align="right">516,745,446</td>
<td align="right">67.0%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">4,366,344</td>
<td align="right">66.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">95,268,190</td>
<td align="right">157,404,989</td>
<td align="right">65.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">335,155,842</td>
<td align="right">552,194,823</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">335,155,842</td>
<td align="right">552,194,823</td>
<td align="right">64.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,629,120</td>
<td align="right">77,838,337</td>
<td align="right">60.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,398,763</td>
<td align="right">152,553,039</td>
<td align="right">58.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">296,945,206</td>
<td align="right">464,397,424</td>
<td align="right">56.4%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,392,486</td>
<td align="right">121,634,526</td>
<td align="right">55.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,795,559</td>
<td align="right">7,343,920</td>
<td align="right">53.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">42,557,190</td>
<td align="right">64,886,636</td>
<td align="right">52.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">83,999,188</td>
<td align="right">125,776,955</td>
<td align="right">49.7%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,033,994,861</td>
<td align="right">10,456,979,845</td>
<td align="right">48.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">167,979,708</td>
<td align="right">244,539,304</td>
<td align="right">45.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,620,799,310</td>
<td align="right">2,333,240,700</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,340,237</td>
<td align="right">53,752,884</td>
<td align="right">44.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,942,070</td>
<td align="right">4,205,410</td>
<td align="right">42.9%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,168,619,009</td>
<td align="right">3,072,909,706</td>
<td align="right">41.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">65,196,263</td>
<td align="right">92,302,722</td>
<td align="right">41.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,266,382,219</td>
<td align="right">3,179,280,566</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,266,469,850</td>
<td align="right">3,179,372,348</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,810,387,322</td>
<td align="right">2,537,746,791</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">537,551,034</td>
<td align="right">750,437,067</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,632,364</td>
<td align="right">66,187,200</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">72,345,827</td>
<td align="right">100,385,510</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">648,969,553</td>
<td align="right">898,910,857</td>
<td align="right">38.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,840,960</td>
<td align="right">5,317,080</td>
<td align="right">38.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,710,401,063</td>
<td align="right">2,365,692,759</td>
<td align="right">38.3%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,440,140,280</td>
<td align="right">12,820,030,986</td>
<td align="right">35.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,633,368,493</td>
<td align="right">7,633,284,655</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,396,229,617</td>
<td align="right">5,836,581,825</td>
<td align="right">32.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">571,941,216</td>
<td align="right">758,467,141</td>
<td align="right">32.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,577</td>
<td align="right">128,306,617</td>
<td align="right">32.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">168,890,217</td>
<td align="right">221,298,059</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,759,108,048</td>
<td align="right">3,584,305,430</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,303,938,210</td>
<td align="right">1,684,364,100</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,554,870,229</td>
<td align="right">2,007,653,625</td>
<td align="right">29.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,222,263,000</td>
<td align="right">1,571,547,770</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,221,383,421</td>
<td align="right">1,570,410,049</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,086,367,727</td>
<td align="right">1,396,021,026</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,346,632,953</td>
<td align="right">1,729,922,050</td>
<td align="right">28.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,989</td>
<td align="right">23,140,627</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,771,271,745</td>
<td align="right">7,394,466,749</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">138,054,453</td>
<td align="right">176,839,338</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,151,797,624</td>
<td align="right">1,474,441,379</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">484,410,970</td>
<td align="right">617,206,465</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,771,606,483</td>
<td align="right">41,697,615,923</td>
<td align="right">27.2%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,232,795,950</td>
<td align="right">11,727,611,787</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">752,952,118</td>
<td align="right">956,279,616</td>
<td align="right">27.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,169,471</td>
<td align="right">163,136,640</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">62,793,484</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">62,793,484</td>
<td align="right">26.0%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">284,807,439</td>
<td align="right">358,022,782</td>
<td align="right">25.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">752,153,295</td>
<td align="right">943,472,585</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">700,393,130</td>
<td align="right">878,286,918</td>
<td align="right">25.4%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">154,719,380</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">351,243,134</td>
<td align="right">439,470,504</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">992,359,441</td>
<td align="right">1,241,328,817</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40,020,812</td>
<td align="right">50,047,830</td>
<td align="right">25.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,560,112</td>
<td align="right">1,945,002</td>
<td align="right">24.7%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">129,244,604</td>
<td align="right">161,052,884</td>
<td align="right">24.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,617,596</td>
<td align="right">2,009,283</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">121,056,190</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">121,056,190</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,865,196,522</td>
<td align="right">3,542,309,622</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,275,247</td>
<td align="right">598,644,886</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">801,565,648</td>
<td align="right">986,680,800</td>
<td align="right">23.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,165,639,474</td>
<td align="right">3,887,842,641</td>
<td align="right">22.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,723,681,548</td>
<td align="right">5,784,782,387</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">724,932,369</td>
<td align="right">886,216,657</td>
<td align="right">22.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,467,637,445</td>
<td align="right">1,786,251,164</td>
<td align="right">21.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,905,070,128</td>
<td align="right">5,932,304,139</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">647,439,727</td>
<td align="right">782,753,532</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,399,380</td>
<td align="right">137,676,269</td>
<td align="right">20.3%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">312,840,153</td>
<td align="right">375,430,539</td>
<td align="right">20.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,299,340,421</td>
<td align="right">3,937,406,205</td>
<td align="right">19.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,311,660</td>
<td align="right">673,346,431</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">792,417,586</td>
<td align="right">940,516,165</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,263,237</td>
<td align="right">319,447,763</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,018,842,929</td>
<td align="right">1,208,162,024</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,463,680,569</td>
<td align="right">5,291,435,090</td>
<td align="right">18.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,194,550,597</td>
<td align="right">1,413,738,651</td>
<td align="right">18.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">436,746,875</td>
<td align="right">516,089,350</td>
<td align="right">18.2%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">647,624,916</td>
<td align="right">763,870,090</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,585,462</td>
<td align="right">245,730,541</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,376,935,668</td>
<td align="right">6,318,595,400</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">287,427,225</td>
<td align="right">335,601,064</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">164,566,124</td>
<td align="right">191,969,805</td>
<td align="right">16.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,198,462,390</td>
<td align="right">10,638,802,403</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">159,116,666</td>
<td align="right">183,803,084</td>
<td align="right">15.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">242,427,074</td>
<td align="right">279,860,390</td>
<td align="right">15.4%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">27,415,482,793</td>
<td align="right">31,574,603,362</td>
<td align="right">15.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">444,211,436</td>
<td align="right">510,022,916</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">502,921,084</td>
<td align="right">576,506,245</td>
<td align="right">14.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,218,210,241</td>
<td align="right">4,816,500,987</td>
<td align="right">14.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">897,324,148</td>
<td align="right">1,022,481,630</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,010,152,054</td>
<td align="right">1,148,741,098</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,858,925,231</td>
<td align="right">2,100,643,754</td>
<td align="right">13.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,880</td>
<td align="right">58,817,340</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,229,679</td>
<td align="right">1,526,560,155</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">192,797,662</td>
<td align="right">217,115,383</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,902,086,247</td>
<td align="right">2,125,816,214</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">52,461,161</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">249,604,547</td>
<td align="right">277,294,133</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">378,058,519</td>
<td align="right">419,947,665</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,396,336</td>
<td align="right">1,733,717,752</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,283,323</td>
<td align="right">47,981,592</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">62,545,882</td>
<td align="right">69,278,342</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,367,803</td>
<td align="right">97,816,570</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,348,589</td>
<td align="right">23,598,288</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">174,061,053</td>
<td align="right">192,159,319</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">97,684,124</td>
<td align="right">107,694,734</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,204,986</td>
<td align="right">26,675,756</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,241,948</td>
<td align="right">53,099,851</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">407,763,274</td>
<td align="right">448,734,072</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,098,865,752</td>
<td align="right">4,480,943,134</td>
<td align="right">9.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,089,073,391</td>
<td align="right">2,275,764,071</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">166,663,013</td>
<td align="right">181,305,150</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,598,997,007</td>
<td align="right">4,996,194,519</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">297,033,245</td>
<td align="right">322,567,868</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">297,251,195</td>
<td align="right">322,785,818</td>
<td align="right">8.6%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,834,865,347</td>
<td align="right">1,991,604,255</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,794,659</td>
<td align="right">521,382,167</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,727,903</td>
<td align="right">521,805,054</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">209,658,948</td>
<td align="right">225,149,756</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,005,724,073</td>
<td align="right">3,219,319,571</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,331,433</td>
<td align="right">97,816,570</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,815,682,031</td>
<td align="right">4,082,109,482</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,851,456,279</td>
<td align="right">1,977,513,448</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,954,571</td>
<td align="right">31,989,667</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,954,571</td>
<td align="right">31,989,667</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">725,039,253</td>
<td align="right">774,063,800</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,043,601,673</td>
<td align="right">1,112,779,014</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,088,427,510</td>
<td align="right">1,159,805,159</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,292,279,355</td>
<td align="right">4,572,743,815</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,252</td>
<td align="right">182,435,299</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,370,381,952</td>
<td align="right">1,449,279,300</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">429,117,763</td>
<td align="right">453,374,770</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">495,343,741</td>
<td align="right">521,703,207</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">171,099,272</td>
<td align="right">179,945,150</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,223,586,685</td>
<td align="right">1,279,568,614</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,910,468,424</td>
<td align="right">3,040,419,185</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">804,363,473</td>
<td align="right">840,143,901</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,297,286,807</td>
<td align="right">8,642,719,290</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right">13,672,424</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,732</td>
<td align="right">74,014,692</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,732</td>
<td align="right">74,014,692</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">194,365,047</td>
<td align="right">201,397,207</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">598,830,333</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">598,830,333</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,960,512,704</td>
<td align="right">5,759,615,278</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,471,796,247</td>
<td align="right">2,530,023,997</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">512,506,385</td>
<td align="right">522,271,116</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,406,145,419</td>
<td align="right">2,363,051,141</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,074,842,458</td>
<td align="right">2,110,981,530</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,250,832</td>
<td align="right">314,525,478</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,246,745</td>
<td align="right">564,179,848</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,425,380</td>
<td align="right">40,926,741</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,310,006</td>
<td align="right">38,751,856</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right">390,072,050</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,389,850,240</td>
<td align="right">1,399,053,869</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,692,422,957</td>
<td align="right">1,701,780,292</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,932,300,698</td>
<td align="right">1,942,609,681</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,726,002</td>
<td align="right">118,339,912</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,574,100</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">502,796,302</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">25,744,504</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">25,744,504</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,548,388</td>
<td align="right">546,351,498</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">98,602</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,594</td>
<td align="right">78,200,918</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,469,878</td>
<td align="right">79,474,202</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">40,302,193</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right">3,579,420</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">41,512,720</td>
<td align="right">41,512,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">10,461,002</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">10,461,002</td>
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
<td align="left">_YIELD_VALUE</td>
<td align="right"></td>
<td align="right">821,021,137</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_FOR</td>
<td align="right"></td>
<td align="right">84,724,527</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_END_SEND</td>
<td align="right"></td>
<td align="right">34,435,038</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right"></td>
<td align="right">2,111,940</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right"></td>
<td align="right">978,130</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right"></td>
<td align="right">2,300</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
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
<td align="left">CALL</td>
<td align="right">7,223</td>
<td align="right">22,911</td>
<td align="right">217.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,550</td>
<td align="right">29,772</td>
<td align="right">21.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,530</td>
<td align="right">23,708</td>
<td align="right">0.8%</td>
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
<td align="right">681</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">RERAISE</td>
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
Stats gathered on: 2025-05-05
