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
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">58,236,394</td>
<td align="right">419,937,414</td>
<td align="right">621.1%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">171,729,919</td>
<td align="right">646,519,292</td>
<td align="right">276.5%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,839,537</td>
<td align="right">57,814,804</td>
<td align="right">224.1%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,875,422</td>
<td align="right">163,935,773</td>
<td align="right">216.0%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,706,045</td>
<td align="right">35,911,002</td>
<td align="right">206.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,054</td>
<td align="right">593,303,404</td>
<td align="right">187.4%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,060</td>
<td align="right">6,152,500</td>
<td align="right">139.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">49,176,329</td>
<td align="right">116,937,500</td>
<td align="right">137.8%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">67,954,617</td>
<td align="right">140,848,499</td>
<td align="right">107.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,918,843</td>
<td align="right">226,752,173</td>
<td align="right">97.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">250,328,302</td>
<td align="right">479,126,883</td>
<td align="right">91.4%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,613,354</td>
<td align="right">103,276,648</td>
<td align="right">76.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,855,922</td>
<td align="right">172,691,080</td>
<td align="right">74.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">131,662,812</td>
<td align="right">228,929,243</td>
<td align="right">73.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,637,720</td>
<td align="right">204,158,350</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,365,943</td>
<td align="right">45,114,237</td>
<td align="right">71.1%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,866,911</td>
<td align="right">8,117,431</td>
<td align="right">66.8%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">18,278,762</td>
<td align="right">30,283,417</td>
<td align="right">65.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">292,384,892</td>
<td align="right">474,829,660</td>
<td align="right">62.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">485,573,232</td>
<td align="right">784,181,209</td>
<td align="right">61.5%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">33,292,776</td>
<td align="right">53,629,016</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,314,940</td>
<td align="right">54,635,117</td>
<td align="right">59.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">659,760,007</td>
<td align="right">1,041,055,765</td>
<td align="right">57.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">236,624,899</td>
<td align="right">367,111,933</td>
<td align="right">55.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,490,327,013</td>
<td align="right">3,794,243,567</td>
<td align="right">52.4%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">173,135,688</td>
<td align="right">262,425,742</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">331,490,771</td>
<td align="right">496,839,040</td>
<td align="right">49.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,514,179</td>
<td align="right">324,101,026</td>
<td align="right">45.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,975,070</td>
<td align="right">115,770,547</td>
<td align="right">44.8%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">61,655,295</td>
<td align="right">88,885,810</td>
<td align="right">44.2%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,201,583</td>
<td align="right">95,322,491</td>
<td align="right">39.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">300,978,820</td>
<td align="right">420,285,800</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">67,248,577</td>
<td align="right">93,737,307</td>
<td align="right">39.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,616,965,219</td>
<td align="right">2,253,173,473</td>
<td align="right">39.3%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,857,063,664</td>
<td align="right">5,369,451,246</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">644,784,750</td>
<td align="right">894,791,095</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">277,086,181</td>
<td align="right">384,139,436</td>
<td align="right">38.6%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,037,815,815</td>
<td align="right">1,259,805,406</td>
<td align="right">-38.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,281,409,095</td>
<td align="right">1,767,098,224</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,623,281</td>
<td align="right">453,414,223</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">209,998,657</td>
<td align="right">281,547,893</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,399,659</td>
<td align="right">86,930,695</td>
<td align="right">32.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,396,085</td>
<td align="right">156,403,090</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">225,758,560</td>
<td align="right">294,734,861</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">70,428,642</td>
<td align="right">91,801,715</td>
<td align="right">30.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,957,136</td>
<td align="right">124,846,039</td>
<td align="right">30.1%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,787,068,530</td>
<td align="right">2,321,048,509</td>
<td align="right">29.9%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,900,042,414</td>
<td align="right">18,007,076,117</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">251,870,320</td>
<td align="right">325,391,960</td>
<td align="right">29.2%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,492,839,321</td>
<td align="right">1,922,068,450</td>
<td align="right">28.8%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">406,864,138</td>
<td align="right">523,383,424</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,219,484,908</td>
<td align="right">4,140,480,354</td>
<td align="right">28.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">137,620,387</td>
<td align="right">176,731,825</td>
<td align="right">28.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,637,073</td>
<td align="right">241,039,638</td>
<td align="right">27.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">143,907,591</td>
<td align="right">181,786,469</td>
<td align="right">26.3%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">57,578,089</td>
<td align="right">72,245,448</td>
<td align="right">25.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,519,766</td>
<td align="right">118,400,103</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">121,954,119</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,932,439,714</td>
<td align="right">2,404,232,012</td>
<td align="right">24.4%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">710,019,358</td>
<td align="right">881,945,405</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,623,464</td>
<td align="right">194,388,012</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,126,358,381</td>
<td align="right">3,854,029,562</td>
<td align="right">23.3%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,767</td>
<td align="right">29,023,508</td>
<td align="right">23.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">88,428,906</td>
<td align="right">108,706,547</td>
<td align="right">22.9%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">539,623,241</td>
<td align="right">661,328,993</td>
<td align="right">22.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">266,180,149</td>
<td align="right">325,993,823</td>
<td align="right">22.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,942,423</td>
<td align="right">4,812,829</td>
<td align="right">22.1%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">309,508,795</td>
<td align="right">377,515,835</td>
<td align="right">22.0%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,872,998</td>
<td align="right">217,924,422</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">352,615,647</td>
<td align="right">429,359,911</td>
<td align="right">21.8%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">716,586,005</td>
<td align="right">866,673,313</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,170,212,384</td>
<td align="right">2,617,892,987</td>
<td align="right">20.6%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,850,351,068</td>
<td align="right">4,629,244,788</td>
<td align="right">20.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,753,893</td>
<td align="right">86,190,717</td>
<td align="right">20.1%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">182,853,931</td>
<td align="right">218,650,291</td>
<td align="right">19.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">271,110,400</td>
<td align="right">321,839,218</td>
<td align="right">18.7%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,362,171</td>
<td align="right">32,452,504</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">429,246,501</td>
<td align="right">508,921,685</td>
<td align="right">18.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105,047,934</td>
<td align="right">123,675,144</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,355,000</td>
<td align="right">121,337,894</td>
<td align="right">17.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,825,535</td>
<td align="right">526,501,114</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,801,646,240</td>
<td align="right">3,230,590,501</td>
<td align="right">15.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">153,460,109</td>
<td align="right">174,869,953</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">214,704,236</td>
<td align="right">244,475,010</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">173,416,046</td>
<td align="right">196,954,233</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">81,668,644</td>
<td align="right">92,553,371</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,173</td>
<td align="right">2,357,149</td>
<td align="right">12.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,245,163</td>
<td align="right">4,778,624</td>
<td align="right">12.6%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">853,354,224</td>
<td align="right">957,556,081</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">609,737,015</td>
<td align="right">683,649,487</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,614,494</td>
<td align="right">149,545,141</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,132,001</td>
<td align="right">28,061,616</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,806,275</td>
<td align="right">40,860,784</td>
<td align="right">11.0%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">113,206,776</td>
<td align="right">125,481,464</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">443,811,314</td>
<td align="right">488,822,285</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,781,911</td>
<td align="right">73,313,666</td>
<td align="right">9.8%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,318,538,692</td>
<td align="right">2,529,116,685</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">328,341,453</td>
<td align="right">356,161,024</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">534,473,288</td>
<td align="right">578,887,467</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">701,413,824</td>
<td align="right">756,852,165</td>
<td align="right">7.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,780,804</td>
<td align="right">156,816,056</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">328,953,526</td>
<td align="right">352,617,007</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,340,902</td>
<td align="right">38,654,532</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">307,983,208</td>
<td align="right">327,322,466</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,880,523</td>
<td align="right">33,754,250</td>
<td align="right">5.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">902,749,617</td>
<td align="right">954,153,681</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">126,713,082</td>
<td align="right">133,209,803</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">61,556,334</td>
<td align="right">58,617,780</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,154,667</td>
<td align="right">239,931,992</td>
<td align="right">4.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,730,820</td>
<td align="right">35,107,664</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,852,808</td>
<td align="right">19,680,499</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,362,280</td>
<td align="right">99,260,656</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">628,725,042</td>
<td align="right">653,894,225</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,924,953</td>
<td align="right">61,264,685</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,906,638</td>
<td align="right">807,445,306</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,954,636</td>
<td align="right">3,800,296</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">321,142,729</td>
<td align="right">332,830,713</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">155,964,783</td>
<td align="right">161,314,103</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,764,694</td>
<td align="right">14,217,278</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,773,878</td>
<td align="right">22,454,856</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,054,098</td>
<td align="right">273,993,915</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,311,881</td>
<td align="right">173,907,184</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">159,730,031</td>
<td align="right">163,985,793</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,136,089</td>
<td align="right">71,940,179</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,708</td>
<td align="right">2,648</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">186,967,301</td>
<td align="right">190,701,477</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,962,529</td>
<td align="right">1,093,216,485</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,660,466</td>
<td align="right">43,506,122</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,294,673</td>
<td align="right">10,094,655</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,643,198</td>
<td align="right">81,174,328</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,841,683</td>
<td align="right">71,074,641</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,054,539</td>
<td align="right">4,117,918</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">172,683,388</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,828,646,805</td>
<td align="right">4,901,587,558</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,953,506</td>
<td align="right">10,790,592</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,873,138</td>
<td align="right">26,560,536</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,906,067</td>
<td align="right">138,359,007</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,221,107</td>
<td align="right">9,129,572</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">8,983,194</td>
<td align="right">9,068,883</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,741,906</td>
<td align="right">9,650,644</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,614,787</td>
<td align="right">36,954,943</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,928,977</td>
<td align="right">396,253,050</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,635,022</td>
<td align="right">48,232,911</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,042,901</td>
<td align="right">112,806,952</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,606</td>
<td align="right">403,336</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,539,258</td>
<td align="right">57,839,843</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,480,882</td>
<td align="right">67,746,944</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,620,628,272</td>
<td align="right">1,625,689,551</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,144</td>
<td align="right">5,131</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">33,737</td>
<td align="right">33,691</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,816,132</td>
<td align="right">100,946,617</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,975,533</td>
<td align="right">60,901,469</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,516,819</td>
<td align="right">180,620,174</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,131</td>
<td align="right">133,069</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,321,534</td>
<td align="right">242,418,381</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,856</td>
<td align="right">120,819</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,193</td>
<td align="right">14,758,707</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,829,679</td>
<td align="right">4,829,278</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,700</td>
<td align="right">773,644</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,911</td>
<td align="right">1,439,859</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,547,461</td>
<td align="right">20,546,739</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,877,945</td>
<td align="right">20,877,223</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,965</td>
<td align="right">20,877,243</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,150</td>
<td align="right">3,115,231</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,913</td>
<td align="right">6,169,897</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">1,194,074</td>
<td align="right">1,194,076</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,607,899</td>
<td align="right">302,607,899</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,677</td>
<td align="right">128,851,677</td>
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
<td align="left">DELETE_ATTR</td>
<td align="right">1,645,923</td>
<td align="right">1,645,923</td>
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
<td align="right">236,754</td>
<td align="right">236,754</td>
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
<td align="right">330,461,515</td>
<td align="right">4.1%</td>
<td align="right">453,222,302</td>
<td align="right">5.6%</td>
<td align="right">37.1%</td>
</tr>
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
<td align="right">51,020,146</td>
<td align="right">0.6%</td>
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
<td align="right">7,641,211,651</td>
<td align="right">95.2%</td>
<td align="right">7,643,519,764</td>
<td align="right">93.8%</td>
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
<td align="right">153,174</td>
<td align="right">13.6%</td>
<td align="right">183,384</td>
<td align="right">15.9%</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">970,775</td>
<td align="right">86.4%</td>
<td align="right">971,151</td>
<td align="right">84.1%</td>
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
<td align="left">lshift</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">15,432</td>
<td align="right">8.4%</td>
<td align="right">134.8%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">5,458</td>
<td align="right">3.6%</td>
<td align="right">11,300</td>
<td align="right">6.2%</td>
<td align="right">107.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">7,753</td>
<td align="right">4.2%</td>
<td align="right">84.0%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,830</td>
<td align="right">12.9%</td>
<td align="right">29,920</td>
<td align="right">16.3%</td>
<td align="right">50.9%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">189</td>
<td align="right">0.1%</td>
<td align="right">209</td>
<td align="right">0.1%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,059</td>
<td align="right">13.1%</td>
<td align="right">21,865</td>
<td align="right">11.9%</td>
<td align="right">9.0%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">2,767</td>
<td align="right">1.5%</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.4%</td>
<td align="right">635</td>
<td align="right">0.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">3,174</td>
<td align="right">2.1%</td>
<td align="right">3,154</td>
<td align="right">1.7%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,718</td>
<td align="right">3.7%</td>
<td align="right">5,754</td>
<td align="right">3.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,767</td>
<td align="right">11.6%</td>
<td align="right">17,858</td>
<td align="right">9.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,469</td>
<td align="right">12.1%</td>
<td align="right">18,491</td>
<td align="right">10.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,474</td>
<td align="right">15.3%</td>
<td align="right">23,469</td>
<td align="right">12.8%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">17,023</td>
<td align="right">9.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">2,343</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">1.3%</td>
<td align="right">1,996</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">1,384</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">836</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">or different types</td>
<td align="right">597</td>
<td align="right">0.4%</td>
<td align="right">597</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">495</td>
<td align="right">0.3%</td>
<td align="right">495</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.1%</td>
<td align="right">83</td>
<td align="right">0.0%</td>
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
<td align="right">121,954,119</td>
<td align="right">100.0%</td>
<td align="right">25.3%</td>
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
<td align="right">526,332,943</td>
<td align="right">8.7%</td>
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
<td align="right">5,470,814,679</td>
<td align="right">92.3%</td>
<td align="right">5,496,015,979</td>
<td align="right">91.2%</td>
<td align="right">0.5%</td>
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
<td align="right">5,827,953</td>
<td align="right">0.1%</td>
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
<td align="right">141,932</td>
<td align="right">54.4%</td>
<td align="right">159,893</td>
<td align="right">57.5%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,913</td>
<td align="right">45.6%</td>
<td align="right">118,013</td>
<td align="right">42.5%</td>
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
<td align="left">array int</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">30,333</td>
<td align="right">19.0%</td>
<td align="right">83.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,096</td>
<td align="right">5.0%</td>
<td align="right">7,584</td>
<td align="right">4.7%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,677</td>
<td align="right">2.6%</td>
<td align="right">3,925</td>
<td align="right">2.5%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,676</td>
<td align="right">42.0%</td>
<td align="right">62,898</td>
<td align="right">39.3%</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">792</td>
<td align="right">0.5%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,055</td>
<td align="right">24.7%</td>
<td align="right">35,272</td>
<td align="right">22.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,443</td>
<td align="right">8.8%</td>
<td align="right">12,446</td>
<td align="right">7.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.5%</td>
<td align="right">3,609</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.1%</td>
<td align="right">2,941</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">code complex parameters</td>
<td align="right">72</td>
<td align="right">0.1%</td>
<td align="right">72</td>
<td align="right">0.0%</td>
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
<td align="right">139,797,263</td>
<td align="right">1.2%</td>
<td align="right">10.0%</td>
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
<td align="right">137,390,614</td>
<td align="right">1.2%</td>
<td align="right">10.0%</td>
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
<td align="right">11,119,334,990</td>
<td align="right">98.8%</td>
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
<td align="right">2,809,539</td>
<td align="right">100.0%</td>
<td align="right">9.2%</td>
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
<td align="right">82.9%</td>
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
<td align="right">20,160</td>
<td align="right">99.4%</td>
<td align="right">20,123</td>
<td align="right">99.4%</td>
<td align="right">-0.2%</td>
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
<td align="right">108,577,947</td>
<td align="right">2.3%</td>
<td align="right">23.0%</td>
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
<td align="right">1,292,015</td>
<td align="right">0.0%</td>
<td align="right">1.2%</td>
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
<td align="right">4,529,973,955</td>
<td align="right">97.6%</td>
<td align="right">0.3%</td>
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
<td align="right">110,671</td>
<td align="right">72.5%</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42,019</td>
<td align="right">28.5%</td>
<td align="right">41,991</td>
<td align="right">27.5%</td>
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
<td align="left">set</td>
<td align="right">359</td>
<td align="right">0.3%</td>
<td align="right">799</td>
<td align="right">0.7%</td>
<td align="right">122.6%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">941</td>
<td align="right">0.9%</td>
<td align="right">1,994</td>
<td align="right">1.8%</td>
<td align="right">111.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,405</td>
<td align="right">8.0%</td>
<td align="right">11,686</td>
<td align="right">10.6%</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">1,367</td>
<td align="right">1.2%</td>
<td align="right">12.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.3%</td>
<td align="right">356</td>
<td align="right">0.3%</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
<td align="right">6,552</td>
<td align="right">5.9%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,547</td>
<td align="right">4.3%</td>
<td align="right">4,602</td>
<td align="right">4.2%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,657</td>
<td align="right">41.4%</td>
<td align="right">43,834</td>
<td align="right">39.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,715</td>
<td align="right">7.3%</td>
<td align="right">7,706</td>
<td align="right">7.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,162</td>
<td align="right">22.0%</td>
<td align="right">23,152</td>
<td align="right">20.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">7,639</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">984</td>
<td align="right">0.9%</td>
<td align="right">984</td>
<td align="right">0.9%</td>
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
<td align="right">72,204,453</td>
<td align="right">3.2%</td>
<td align="right">25.5%</td>
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
<td align="right">2,194,248,870</td>
<td align="right">96.7%</td>
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
<td align="right">38,934</td>
<td align="right">50.5%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">52.0%</td>
<td align="right">38,235</td>
<td align="right">49.5%</td>
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
<td align="left">other</td>
<td align="right">7,856</td>
<td align="right">22.2%</td>
<td align="right">10,042</td>
<td align="right">25.8%</td>
<td align="right">27.8%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">7,197</td>
<td align="right">20.3%</td>
<td align="right">7,882</td>
<td align="right">20.2%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,166</td>
<td align="right">25.9%</td>
<td align="right">9,843</td>
<td align="right">25.3%</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,199</td>
<td align="right">31.6%</td>
<td align="right">11,167</td>
<td align="right">28.7%</td>
<td align="right">-0.3%</td>
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
<td align="right">56,565,494</td>
<td align="right">5.0%</td>
<td align="right">74.9%</td>
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
<td align="right">204,040,502</td>
<td align="right">17.9%</td>
<td align="right">72.1%</td>
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
<td align="right">877,966,210</td>
<td align="right">77.1%</td>
<td align="right">45.6%</td>
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
<td align="right">1,072,177</td>
<td align="right">90.5%</td>
<td align="right">74.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,376</td>
<td align="right">12.9%</td>
<td align="right">112,792</td>
<td align="right">9.5%</td>
<td align="right">23.4%</td>
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
<td align="left">map</td>
<td align="right">174</td>
<td align="right">0.2%</td>
<td align="right">734</td>
<td align="right">0.7%</td>
<td align="right">321.8%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,895</td>
<td align="right">6.5%</td>
<td align="right">16,567</td>
<td align="right">14.7%</td>
<td align="right">181.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.3%</td>
<td align="right">7,068</td>
<td align="right">6.3%</td>
<td align="right">134.4%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">1,529</td>
<td align="right">1.4%</td>
<td align="right">61.8%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,164</td>
<td align="right">6.7%</td>
<td align="right">6,923</td>
<td align="right">6.1%</td>
<td align="right">12.3%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.5%</td>
<td align="right">2,513</td>
<td align="right">2.2%</td>
<td align="right">11.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,734</td>
<td align="right">11.7%</td>
<td align="right">11,887</td>
<td align="right">10.5%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,547</td>
<td align="right">1.7%</td>
<td align="right">1,420</td>
<td align="right">1.3%</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">48,286</td>
<td align="right">52.8%</td>
<td align="right">51,650</td>
<td align="right">45.8%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">5.0%</td>
<td align="right">4,676</td>
<td align="right">4.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.1%</td>
<td align="right">2,825</td>
<td align="right">2.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,495</td>
<td align="right">4.9%</td>
<td align="right">4,539</td>
<td align="right">4.0%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">327</td>
<td align="right">0.4%</td>
<td align="right">327</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">134</td>
<td align="right">0.1%</td>
<td align="right">134</td>
<td align="right">0.1%</td>
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
<td align="right">804,147,092</td>
<td align="right">6.0%</td>
<td align="right">25.1%</td>
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
<td align="right">577,127,488</td>
<td align="right">4.3%</td>
<td align="right">8.3%</td>
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
<td align="right">12,130,314,365</td>
<td align="right">89.8%</td>
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
<td align="right">355,119</td>
<td align="right">2.8%</td>
<td align="right">492,983</td>
<td align="right">3.1%</td>
<td align="right">38.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,215,258</td>
<td align="right">97.2%</td>
<td align="right">15,254,635</td>
<td align="right">96.9%</td>
<td align="right">24.9%</td>
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
<td align="right">1,608</td>
<td align="right">0.5%</td>
<td align="right">1,802</td>
<td align="right">0.4%</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,455</td>
<td align="right">10.8%</td>
<td align="right">42,585</td>
<td align="right">8.6%</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,702</td>
<td align="right">11.5%</td>
<td align="right">44,852</td>
<td align="right">9.1%</td>
<td align="right">10.2%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">14,536</td>
<td align="right">4.1%</td>
<td align="right">15,562</td>
<td align="right">3.2%</td>
<td align="right">7.1%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">855</td>
<td align="right">0.2%</td>
<td align="right">820</td>
<td align="right">0.2%</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,912</td>
<td align="right">1.4%</td>
<td align="right">5,050</td>
<td align="right">1.0%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,828</td>
<td align="right">6.7%</td>
<td align="right">24,483</td>
<td align="right">5.0%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,404</td>
<td align="right">0.7%</td>
<td align="right">2,369</td>
<td align="right">0.5%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,050</td>
<td align="right">16.9%</td>
<td align="right">60,508</td>
<td align="right">12.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">1,583</td>
<td align="right">0.3%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,945</td>
<td align="right">2.2%</td>
<td align="right">7,942</td>
<td align="right">1.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">5,087</td>
<td align="right">1.4%</td>
<td align="right">5,088</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">6,405</td>
<td align="right">1.8%</td>
<td align="right">6,405</td>
<td align="right">1.3%</td>
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
<td align="right">0.0%</td>
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
<td align="right">4,613,477,222</td>
<td align="right">99.7%</td>
<td align="right">22.3%</td>
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
<td align="right">53,124</td>
<td align="right">0.0%</td>
<td align="right">1.1%</td>
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
<td align="right">14,622,667</td>
<td align="right">0.3%</td>
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
<td align="right">138,257</td>
<td align="right">100.0%</td>
<td align="right">136,807</td>
<td align="right">100.0%</td>
<td align="right">-1.0%</td>
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
<td align="right">65,094,554</td>
<td align="right">100.0%</td>
<td align="right">64,595,865</td>
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
<td align="right">2,395</td>
<td align="right">100.0%</td>
<td align="right">-2.4%</td>
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
<td align="right">593,288,693</td>
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
<td align="right">128,816,906</td>
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
<td align="right">69,748,569</td>
<td align="right">3.4%</td>
<td align="right">70,982,579</td>
<td align="right">3.5%</td>
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
<td align="right">1,845,640,262</td>
<td align="right">90.9%</td>
<td align="right">1,851,473,237</td>
<td align="right">90.8%</td>
<td align="right">0.3%</td>
</tr>
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
<td align="right">115,906,692</td>
<td align="right">5.7%</td>
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
<td align="right">50,961</td>
<td align="right">2.2%</td>
<td align="right">51,307</td>
<td align="right">2.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,228,397</td>
<td align="right">97.8%</td>
<td align="right">2,226,943</td>
<td align="right">97.7%</td>
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
<td align="right">135,470</td>
<td align="right">265.8%</td>
<td align="right">261,972</td>
<td align="right">510.6%</td>
<td align="right">93.4%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.4%</td>
<td align="right">741</td>
<td align="right">1.4%</td>
<td align="right">6.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">5,322</td>
<td align="right">10.4%</td>
<td align="right">4.4%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">3.2%</td>
<td align="right">1,665</td>
<td align="right">3.2%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.2%</td>
<td align="right">111</td>
<td align="right">0.2%</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">4,978</td>
<td align="right">9.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,344</td>
<td align="right">6.6%</td>
<td align="right">3,350</td>
<td align="right">6.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">24,076</td>
<td align="right">46.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,666</td>
<td align="right">14.9%</td>
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
<td align="right">1,194,074</td>
<td align="right">100.0%</td>
<td align="right">1,194,076</td>
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
<td align="right">149,495,414</td>
<td align="right">13.9%</td>
<td align="right">11.9%</td>
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
<td align="right">923,016,397</td>
<td align="right">86.1%</td>
<td align="right">0.3%</td>
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
<td align="right">47,690</td>
<td align="right">95.8%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,195</td>
<td align="right">4.8%</td>
<td align="right">2,077</td>
<td align="right">4.2%</td>
<td align="right">-5.4%</td>
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
<td align="right">11,232</td>
<td align="right">23.6%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">156</td>
<td align="right">0.3%</td>
<td align="right">-33.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">2,906</td>
<td align="right">6.1%</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">17,323</td>
<td align="right">36.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">14,752</td>
<td align="right">33.7%</td>
<td align="right">15,163</td>
<td align="right">31.8%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">501</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">341</td>
<td align="right">0.8%</td>
<td align="right">341</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">array slice</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">68</td>
<td align="right">0.1%</td>
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
<td align="right">40,958,294</td>
<td align="right">0.9%</td>
<td align="right">62,664,066</td>
<td align="right">1.3%</td>
<td align="right">53.0%</td>
</tr>
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
<td align="right">120,874,031</td>
<td align="right">2.5%</td>
<td align="right">17.5%</td>
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
<td align="right">4,575,269,802</td>
<td align="right">96.1%</td>
<td align="right">1.0%</td>
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
<td align="right">1,230,466</td>
<td align="right">74.8%</td>
<td align="right">49.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">413,283</td>
<td align="right">33.5%</td>
<td align="right">414,270</td>
<td align="right">25.2%</td>
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
<td align="right">16,408</td>
<td align="right">4.0%</td>
<td align="right">11,713</td>
<td align="right">2.8%</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,475</td>
<td align="right">3.3%</td>
<td align="right">15,674</td>
<td align="right">3.8%</td>
<td align="right">16.3%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">5,278</td>
<td align="right">1.3%</td>
<td align="right">14.8%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,689</td>
<td align="right">1.4%</td>
<td align="right">6,352</td>
<td align="right">1.5%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,611</td>
<td align="right">2.1%</td>
<td align="right">8,968</td>
<td align="right">2.2%</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,063</td>
<td align="right">22.8%</td>
<td align="right">95,867</td>
<td align="right">23.1%</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,361</td>
<td align="right">3.0%</td>
<td align="right">12,549</td>
<td align="right">3.0%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">256,193</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,233,606,829</td>
<td align="right">99.9%</td>
<td align="right">1,238,096,090</td>
<td align="right">99.9%</td>
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
<td align="right">1,427,528</td>
<td align="right">0.1%</td>
<td align="right">1,427,496</td>
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
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
<td align="right">11,581</td>
<td align="right">93.1%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">862</td>
<td align="right">6.9%</td>
<td align="right">862</td>
<td align="right">6.9%</td>
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
<td align="right">635</td>
<td align="right">73.7%</td>
<td align="right">635</td>
<td align="right">73.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.8%</td>
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
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">30,418,392,874</td>
<td align="right">37.8%</td>
<td align="right">40,112,475,606</td>
<td align="right">40.3%</td>
<td align="right">31.9%</td>
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
<td align="right">1,239,925,787</td>
<td align="right">1.2%</td>
<td align="right">21.6%</td>
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
<td align="right">2,554,596,066</td>
<td align="right">2.6%</td>
<td align="right">19.8%</td>
</tr>
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
<td align="right">55,674,715,785</td>
<td align="right">55.9%</td>
<td align="right">18.5%</td>
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
<td align="right">118,541,268</td>
<td align="right">5.3%</td>
<td align="right">204,040,502</td>
<td align="right">7.6%</td>
<td align="right">72.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,461,515</td>
<td align="right">14.7%</td>
<td align="right">453,222,302</td>
<td align="right">16.9%</td>
<td align="right">37.1%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">4.3%</td>
<td align="right">121,954,119</td>
<td align="right">4.5%</td>
<td align="right">25.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">88,305,264</td>
<td align="right">3.9%</td>
<td align="right">108,577,947</td>
<td align="right">4.0%</td>
<td align="right">23.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,891,601</td>
<td align="right">4.6%</td>
<td align="right">120,874,031</td>
<td align="right">4.5%</td>
<td align="right">17.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,674,365</td>
<td align="right">20.0%</td>
<td align="right">526,332,943</td>
<td align="right">19.6%</td>
<td align="right">16.5%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,568,563</td>
<td align="right">5.9%</td>
<td align="right">149,495,414</td>
<td align="right">5.6%</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">124,915,318</td>
<td align="right">5.5%</td>
<td align="right">137,390,614</td>
<td align="right">5.1%</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">532,847,492</td>
<td align="right">23.6%</td>
<td align="right">577,127,488</td>
<td align="right">21.5%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,906</td>
<td align="right">5.7%</td>
<td align="right">128,816,906</td>
<td align="right">4.8%</td>
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
<td align="right">184,014,368</td>
<td align="right">18.0%</td>
<td align="right">246,848,252</td>
<td align="right">19.9%</td>
<td align="right">34.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">255,322,860</td>
<td align="right">25.0%</td>
<td align="right">330,543,775</td>
<td align="right">26.7%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,458,461</td>
<td align="right">7.3%</td>
<td align="right">85,092,089</td>
<td align="right">6.9%</td>
<td align="right">14.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,730,649</td>
<td align="right">7.4%</td>
<td align="right">86,362,495</td>
<td align="right">7.0%</td>
<td align="right">14.0%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,073,265</td>
<td align="right">6.8%</td>
<td align="right">69,650,223</td>
<td align="right">5.6%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,274,265</td>
<td align="right">9.2%</td>
<td align="right">94,267,244</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,415,263</td>
<td align="right">2.4%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">21,239,806</td>
<td align="right">2.1%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,947</td>
<td align="right">2.0%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">29,414,544</td>
<td align="right">2.4%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">28,245,787</td>
<td align="right">2.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">28,241,837</td>
<td align="right">2.3%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">26,602,518</td>
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
<td align="right">2,128,247</td>
<td align="right">0.0%</td>
<td align="right">3,558,377</td>
<td align="right">0.1%</td>
<td align="right">67.2%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,068,170,298</td>
<td align="right">75.7%</td>
<td align="right">5,103,619,486</td>
<td align="right">75.8%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,580,347</td>
<td align="right">10.0%</td>
<td align="right">674,364,518</td>
<td align="right">10.0%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,634,001</td>
<td align="right">1.1%</td>
<td align="right">71,327,096</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,462,609,859</td>
<td align="right">81.6%</td>
<td align="right">5,481,833,928</td>
<td align="right">81.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,630,182,956</td>
<td align="right">24.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,630,182,956</td>
<td align="right">24.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">954,695,668</td>
<td align="right">14.3%</td>
<td align="right">955,818,438</td>
<td align="right">14.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,386,706</td>
<td align="right">4.2%</td>
<td align="right">279,528,023</td>
<td align="right">4.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">952,563,525</td>
<td align="right">14.2%</td>
<td align="right">952,256,165</td>
<td align="right">14.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,948</td>
<td align="right">3.9%</td>
<td align="right">261,414,735</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,432</td>
<td align="right">0.4%</td>
<td align="right">24,922,600</td>
<td align="right">0.4%</td>
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
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,925,103,433</td>
<td align="right">5.6%</td>
<td align="right">12,027,770,690</td>
<td align="right">7.6%</td>
<td align="right">34.8%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,516,176,225</td>
<td align="right">8.2%</td>
<td align="right">19,994,298,952</td>
<td align="right">10.1%</td>
<td align="right">21.1%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">35,930,617,616</td>
<td align="right">22.4%</td>
<td align="right">42,151,446,312</td>
<td align="right">26.6%</td>
<td align="right">17.3%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">77,400,036,232</td>
<td align="right">48.2%</td>
<td align="right">68,586,241,241</td>
<td align="right">43.3%</td>
<td align="right">-11.4%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">47,497,701,691</td>
<td align="right">23.6%</td>
<td align="right">51,441,746,415</td>
<td align="right">25.9%</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">82,872,995,483</td>
<td align="right">41.1%</td>
<td align="right">76,362,386,175</td>
<td align="right">38.5%</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,666,871,820</td>
<td align="right">27.1%</td>
<td align="right">50,612,199,003</td>
<td align="right">25.5%</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">38,388,708,385</td>
<td align="right">23.9%</td>
<td align="right">35,706,420,754</td>
<td align="right">22.5%</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">8,684,176</td>
<td align="right"></td>
<td align="right">8,160,255</td>
<td align="right"></td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,179,985,728</td>
<td align="right"></td>
<td align="right">2,272,942,067</td>
<td align="right"></td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,109,261</td>
<td align="right"></td>
<td align="right">59,342,017</td>
<td align="right"></td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,984,653</td>
<td align="right"></td>
<td align="right">66,694,323</td>
<td align="right"></td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,009,403,952</td>
<td align="right">32.5%</td>
<td align="right">6,020,666,529</td>
<td align="right">32.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,087,339,143</td>
<td align="right">32.9%</td>
<td align="right">6,098,700,820</td>
<td align="right">32.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,399,378,238</td>
<td align="right">67.1%</td>
<td align="right">12,422,465,316</td>
<td align="right">67.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,399,472,251</td>
<td align="right"></td>
<td align="right">12,422,548,288</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,900,013,598</td>
<td align="right"></td>
<td align="right">2,905,027,873</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,678,833,154</td>
<td align="right"></td>
<td align="right">6,689,453,764</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,515,418</td>
<td align="right">0.4%</td>
<td align="right">71,611,197</td>
<td align="right">0.4%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,996,654</td>
<td align="right"></td>
<td align="right">179,816,832</td>
<td align="right"></td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,773</td>
<td align="right">0.0%</td>
<td align="right">6,423,094</td>
<td align="right">0.0%</td>
<td align="right">0.1%</td>
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
<td align="right">364,692</td>
<td align="right">103,237,922</td>
<td align="right">9,561,523,944</td>
<td align="right">756,762,804</td>
<td align="right">765,329,029</td>
<td align="right">365,237</td>
<td align="right">103,535,307</td>
<td align="right">9,572,041,217</td>
<td align="right">756,820,823</td>
<td align="right">765,863,171</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,771,834</td>
<td align="right">0</td>
<td align="right">0</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,607,767,864</td>
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
<td align="right">398,075</td>
<td align="right">78.4%</td>
<td align="right">212,441</td>
<td align="right">47.7%</td>
<td align="right">-46.6%</td>
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
<td align="right">280</td>
<td align="right">0.7%</td>
<td align="right">-44.1%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it it too short.
</details>
</td>
<td align="right">440,533</td>
<td align="right">86.8%</td>
<td align="right">253,455</td>
<td align="right">57.0%</td>
<td align="right">-42.5%</td>
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
<td align="right">40,391</td>
<td align="right">9.1%</td>
<td align="right">-39.5%</td>
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
<td align="right">4,728,866,217</td>
<td align="right"></td>
<td align="right">-32.8%</td>
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
<td align="right">220</td>
<td align="right">0.0%</td>
<td align="right">-28.6%</td>
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
<td align="right">673</td>
<td align="right">0.2%</td>
<td align="right">-19.7%</td>
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
<td align="right">226,358,328,127</td>
<td align="right">4,786.7%</td>
<td align="right">-16.9%</td>
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
<td align="right">2,761</td>
<td align="right">0.6%</td>
<td align="right">-14.9%</td>
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
<td align="right">445,016</td>
<td align="right"></td>
<td align="right">-12.3%</td>
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
<td align="right">902</td>
<td align="right">0.2%</td>
<td align="right">-8.1%</td>
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
<td align="right">60,336</td>
<td align="right">90.4%</td>
<td align="right">33,835</td>
<td align="right">83.8%</td>
<td align="right">-43.9%</td>
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
<td align="right">40,391</td>
<td align="right"></td>
<td align="right">-39.5%</td>
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
Padding size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the padding of the JIT traces
</details>
</td>
<td align="right">129,029,609</td>
<td align="right">19.7%</td>
<td align="right">73,908,253</td>
<td align="right">18.4%</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">
Freed memory size
<details>
<summary>ⓘ</summary>

The size of the memory freed from the JIT traces
</details>
</td>
<td align="right">548,462,592</td>
<td align="right">83.8%</td>
<td align="right">316,395,520</td>
<td align="right">78.8%</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">
Total memory size
<details>
<summary>ⓘ</summary>

The total size of the memory allocated for the JIT traces
</details>
</td>
<td align="right">654,614,528</td>
<td align="right"></td>
<td align="right">401,264,640</td>
<td align="right"></td>
<td align="right">-38.7%</td>
</tr>
<tr>
<td align="left">
Data size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the data of the JIT traces
</details>
</td>
<td align="right">76,045,984</td>
<td align="right">11.6%</td>
<td align="right">47,270,376</td>
<td align="right">11.8%</td>
<td align="right">-37.8%</td>
</tr>
<tr>
<td align="left">
Code size
<details>
<summary>ⓘ</summary>

The size of the memory allocated for the code of the JIT traces
</details>
</td>
<td align="right">449,538,935</td>
<td align="right">68.7%</td>
<td align="right">280,086,011</td>
<td align="right">69.8%</td>
<td align="right">-37.7%</td>
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
<td align="left">15,120</td>
<td align="right">25.1%</td>
<td align="left">6,642</td>
<td align="right">19.6%</td>
<td align="right">-56.1%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">24,334</td>
<td align="right">40.3%</td>
<td align="left">12,982</td>
<td align="right">38.4%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">14,868</td>
<td align="right">24.6%</td>
<td align="left">10,137</td>
<td align="right">30.0%</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,139</td>
<td align="right">6.9%</td>
<td align="left">2,874</td>
<td align="right">8.5%</td>
<td align="right">-30.6%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,547</td>
<td align="right">2.6%</td>
<td align="left">932</td>
<td align="right">2.8%</td>
<td align="right">-39.8%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">328</td>
<td align="right">0.5%</td>
<td align="left">268</td>
<td align="right">0.8%</td>
<td align="right">-18.3%</td>
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
<td align="right">5,751</td>
<td align="right">8.6%</td>
<td align="right">2,962</td>
<td align="right">7.3%</td>
<td align="right">-48.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,253</td>
<td align="right">12.4%</td>
<td align="right">3,400</td>
<td align="right">8.4%</td>
<td align="right">-58.8%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">21,525</td>
<td align="right">32.2%</td>
<td align="right">11,821</td>
<td align="right">29.3%</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,468</td>
<td align="right">24.7%</td>
<td align="right">10,518</td>
<td align="right">26.0%</td>
<td align="right">-36.1%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,191</td>
<td align="right">13.8%</td>
<td align="right">7,306</td>
<td align="right">18.1%</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,689</td>
<td align="right">7.0%</td>
<td align="right">3,680</td>
<td align="right">9.1%</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">815</td>
<td align="right">1.2%</td>
<td align="right">622</td>
<td align="right">1.5%</td>
<td align="right">-23.7%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">82</td>
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
<td align="left"><= 4</td>
<td align="right">1,941</td>
<td align="right">2.9%</td>
<td align="right">1,151</td>
<td align="right">2.8%</td>
<td align="right">-40.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,191</td>
<td align="right">12.3%</td>
<td align="right">2,824</td>
<td align="right">7.0%</td>
<td align="right">-65.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,455</td>
<td align="right">12.7%</td>
<td align="right">5,531</td>
<td align="right">13.7%</td>
<td align="right">-34.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,192</td>
<td align="right">36.2%</td>
<td align="right">12,746</td>
<td align="right">31.6%</td>
<td align="right">-47.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,561</td>
<td align="right">18.8%</td>
<td align="right">8,173</td>
<td align="right">20.2%</td>
<td align="right">-34.9%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,462</td>
<td align="right">5.2%</td>
<td align="right">2,536</td>
<td align="right">6.3%</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,246</td>
<td align="right">1.9%</td>
<td align="right">646</td>
<td align="right">1.6%</td>
<td align="right">-48.2%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">288</td>
<td align="right">0.4%</td>
<td align="right">228</td>
<td align="right">0.6%</td>
<td align="right">-20.8%</td>
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
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">181,915</td>
<td align="right">1,376,515</td>
<td align="right">656.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,250,836</td>
<td align="right">263</td>
<td align="right">-100.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">129,244,604</td>
<td align="right">127,444</td>
<td align="right">-99.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">637,669</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">637,669</td>
<td align="right">-97.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">113,182,193</td>
<td align="right">5,716,547</td>
<td align="right">-94.9%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,880</td>
<td align="right">2,703,280</td>
<td align="right">-94.8%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">504,580,749</td>
<td align="right">44,784,656</td>
<td align="right">-91.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,392,486</td>
<td align="right">10,631,286</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right">2,075,564</td>
<td align="right">-84.2%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">62,545,882</td>
<td align="right">12,454,274</td>
<td align="right">-80.1%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,340,237</td>
<td align="right">10,133,091</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">335,155,842</td>
<td align="right">90,973,902</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">335,155,842</td>
<td align="right">90,973,902</td>
<td align="right">-72.9%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">335,270,882</td>
<td align="right">91,106,014</td>
<td align="right">-72.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,447,871</td>
<td align="right">8,067,811</td>
<td align="right">-72.6%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,398,763</td>
<td align="right">28,142,833</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,211,904</td>
<td align="right">8,831,844</td>
<td align="right">-70.8%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">287,427,225</td>
<td align="right">101,559,430</td>
<td align="right">-64.7%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">167,979,708</td>
<td align="right">60,699,941</td>
<td align="right">-63.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">159,116,666</td>
<td align="right">59,992,708</td>
<td align="right">-62.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,574,318</td>
<td align="right">6,122,956</td>
<td align="right">-60.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">502,921,084</td>
<td align="right">198,251,090</td>
<td align="right">-60.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">168,890,217</td>
<td align="right">69,713,513</td>
<td align="right">-58.7%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,632,364</td>
<td align="right">20,534,702</td>
<td align="right">-56.9%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,667</td>
<td align="right">1,398,443</td>
<td align="right">-56.3%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,168,619,009</td>
<td align="right">983,202,207</td>
<td align="right">-54.7%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,266,469,850</td>
<td align="right">1,031,253,742</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,266,382,219</td>
<td align="right">1,031,237,336</td>
<td align="right">-54.5%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,662,322</td>
<td align="right">10,676,589</td>
<td align="right">-52.9%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">152,466,174</td>
<td align="right">72,482,378</td>
<td align="right">-52.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">544,397</td>
<td align="right">278,354</td>
<td align="right">-48.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,252</td>
<td align="right">98,330,997</td>
<td align="right">-42.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,513,079</td>
<td align="right">11,771,321</td>
<td align="right">-42.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,003,871</td>
<td align="right">579,165</td>
<td align="right">-42.3%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">26,214,596</td>
<td align="right">15,656,583</td>
<td align="right">-40.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">95,268,190</td>
<td align="right">57,140,049</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">296,945,206</td>
<td align="right">178,302,379</td>
<td align="right">-40.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,554,870,229</td>
<td align="right">941,479,432</td>
<td align="right">-39.4%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,620,799,310</td>
<td align="right">983,202,207</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">72,345,827</td>
<td align="right">43,893,673</td>
<td align="right">-39.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">309,438,152</td>
<td align="right">188,044,200</td>
<td align="right">-39.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,151,797,624</td>
<td align="right">703,203,020</td>
<td align="right">-38.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,222,263,000</td>
<td align="right">747,754,693</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,221,383,421</td>
<td align="right">747,545,493</td>
<td align="right">-38.8%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,331,433</td>
<td align="right">58,412,465</td>
<td align="right">-36.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,633,368,493</td>
<td align="right">3,633,687,853</td>
<td align="right">-35.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,346,632,953</td>
<td align="right">873,745,192</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,367,803</td>
<td align="right">57,595,985</td>
<td align="right">-34.8%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">63,817,915</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">63,817,915</td>
<td align="right">-34.7%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,396,229,617</td>
<td align="right">2,942,746,990</td>
<td align="right">-33.1%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,033,994,861</td>
<td align="right">4,728,866,217</td>
<td align="right">-32.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">65,196,263</td>
<td align="right">44,342,473</td>
<td align="right">-32.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">700,393,130</td>
<td align="right">477,741,313</td>
<td align="right">-31.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">536,303,591</td>
<td align="right">377,867,963</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">83,999,188</td>
<td align="right">59,896,023</td>
<td align="right">-28.7%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">194,365,047</td>
<td align="right">138,718,247</td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">436,746,875</td>
<td align="right">322,172,079</td>
<td align="right">-26.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,560,112</td>
<td align="right">1,159,668</td>
<td align="right">-25.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">484,410,970</td>
<td align="right">362,099,118</td>
<td align="right">-25.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,010,152,054</td>
<td align="right">760,863,065</td>
<td align="right">-24.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,710,401,063</td>
<td align="right">1,289,609,014</td>
<td align="right">-24.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,440,140,280</td>
<td align="right">7,150,879,403</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">3,891,960</td>
<td align="right">2,976,000</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">3,891,960</td>
<td align="right">2,976,000</td>
<td align="right">-23.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">647,624,916</td>
<td align="right">498,449,590</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,771,271,745</td>
<td align="right">4,531,032,936</td>
<td align="right">-21.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,399,380</td>
<td align="right">90,376,686</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,169,805</td>
<td align="right">924,557</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,577</td>
<td align="right">76,782,406</td>
<td align="right">-20.9%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,960,512,704</td>
<td align="right">4,718,189,365</td>
<td align="right">-20.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,759,108,048</td>
<td align="right">2,209,855,260</td>
<td align="right">-19.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">466,759,722</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">466,759,722</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,617,596</td>
<td align="right">1,304,223</td>
<td align="right">-19.4%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,548,388</td>
<td align="right">441,301,549</td>
<td align="right">-19.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,865,196,522</td>
<td align="right">2,328,883,542</td>
<td align="right">-18.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,724,772</td>
<td align="right">46,369,257</td>
<td align="right">-18.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,246,745</td>
<td align="right">456,857,484</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,089,073,391</td>
<td align="right">1,714,629,544</td>
<td align="right">-17.9%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,954,571</td>
<td align="right">24,865,300</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,954,571</td>
<td align="right">24,865,300</td>
<td align="right">-17.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">103,178,820</td>
<td align="right">-16.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,810,387,322</td>
<td align="right">1,513,618,686</td>
<td align="right">-16.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,726,365</td>
<td align="right">165,192,785</td>
<td align="right">-15.6%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,771,606,483</td>
<td align="right">27,677,403,350</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,086,367,727</td>
<td align="right">918,253,610</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">97,684,124</td>
<td align="right">83,569,539</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">192,797,662</td>
<td align="right">165,144,983</td>
<td align="right">-14.3%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,250,832</td>
<td align="right">265,989,753</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">27,415,482,793</td>
<td align="right">23,651,317,219</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,680,384</td>
<td align="right">20,509,876</td>
<td align="right">-13.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,370,381,952</td>
<td align="right">1,188,143,590</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,463,680,569</td>
<td align="right">3,878,778,608</td>
<td align="right">-13.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,989</td>
<td align="right">15,704,991</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,723,681,548</td>
<td align="right">4,132,653,784</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">571,941,216</td>
<td align="right">501,198,589</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">792,417,586</td>
<td align="right">694,680,914</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,585,462</td>
<td align="right">184,924,416</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,299,340,421</td>
<td align="right">2,926,807,090</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,376,935,668</td>
<td align="right">4,793,588,351</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">648,969,553</td>
<td align="right">578,736,824</td>
<td align="right">-10.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">378,058,519</td>
<td align="right">337,989,137</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,194,550,597</td>
<td align="right">1,070,196,870</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">407,763,274</td>
<td align="right">367,065,118</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,905,070,128</td>
<td align="right">4,416,728,777</td>
<td align="right">-10.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,165,639,474</td>
<td align="right">2,853,229,550</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,005,724,073</td>
<td align="right">2,709,906,450</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,818,123</td>
<td align="right">6,150,708</td>
<td align="right">-9.8%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,232,795,950</td>
<td align="right">8,334,243,215</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">897,324,148</td>
<td align="right">811,454,118</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">537,551,034</td>
<td align="right">486,827,631</td>
<td align="right">-9.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,275,247</td>
<td align="right">439,020,551</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">576,845,478</td>
<td align="right">523,104,552</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,471,796,247</td>
<td align="right">2,241,762,607</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">801,565,648</td>
<td align="right">728,044,148</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,858,925,231</td>
<td align="right">1,694,367,025</td>
<td align="right">-8.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,198,462,390</td>
<td align="right">8,431,107,868</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,696,290</td>
<td align="right">6,137,792</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,018,842,929</td>
<td align="right">934,132,964</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">158,515,496</td>
<td align="right">145,543,961</td>
<td align="right">-8.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">444,211,436</td>
<td align="right">409,331,650</td>
<td align="right">-7.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,297,286,807</td>
<td align="right">7,682,877,484</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">647,439,727</td>
<td align="right">600,046,865</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,292,279,355</td>
<td align="right">3,992,410,402</td>
<td align="right">-7.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">242,427,074</td>
<td align="right">225,803,934</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">9,750,994</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">10,461,002</td>
<td align="right">9,750,994</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">249,604,547</td>
<td align="right">233,219,512</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,074,842,458</td>
<td align="right">1,939,284,436</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,932,300,698</td>
<td align="right">1,807,367,451</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,218,210,241</td>
<td align="right">3,953,129,126</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">725,039,253</td>
<td align="right">680,131,096</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">351,243,134</td>
<td align="right">329,788,034</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,815,682,031</td>
<td align="right">3,586,102,006</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">174,061,053</td>
<td align="right">163,679,808</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">46,893,820</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">46,893,820</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,389,850,240</td>
<td align="right">1,309,661,308</td>
<td align="right">-5.8%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,794,659</td>
<td align="right">457,775,370</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,727,903</td>
<td align="right">459,077,011</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,692,422,957</td>
<td align="right">1,599,833,219</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,263,237</td>
<td align="right">254,690,388</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">752,952,118</td>
<td align="right">712,779,974</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,283,323</td>
<td align="right">40,986,572</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">429,117,763</td>
<td align="right">409,975,084</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,598,997,007</td>
<td align="right">4,393,911,302</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">495,343,741</td>
<td align="right">474,322,246</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">42,557,190</td>
<td align="right">40,775,190</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,902,086,247</td>
<td align="right">1,830,578,505</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,834,865,347</td>
<td align="right">1,768,947,543</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">752,153,295</td>
<td align="right">726,565,899</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,043,601,673</td>
<td align="right">1,008,909,217</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">284,807,439</td>
<td align="right">275,451,998</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,629,120</td>
<td align="right">50,176,180</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,396,336</td>
<td align="right">1,513,991,609</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,098,865,752</td>
<td align="right">3,972,426,182</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,223,586,685</td>
<td align="right">1,185,949,844</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,910,468,424</td>
<td align="right">2,826,379,227</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,311,660</td>
<td align="right">551,384,488</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,154,665</td>
<td align="right">5,985,315</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,851,456,279</td>
<td align="right">1,802,057,122</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,467,637,445</td>
<td align="right">1,430,876,406</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">166,663,013</td>
<td align="right">162,692,988</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">804,363,473</td>
<td align="right">785,657,974</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">209,658,948</td>
<td align="right">214,391,967</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,942,070</td>
<td align="right">2,880,330</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,241,948</td>
<td align="right">49,188,327</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">164,566,124</td>
<td align="right">167,300,891</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">171,099,272</td>
<td align="right">168,428,852</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">312,840,153</td>
<td align="right">308,068,207</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">138,054,453</td>
<td align="right">140,137,134</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,726,002</td>
<td align="right">119,352,270</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,310,006</td>
<td align="right">37,807,275</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,732</td>
<td align="right">70,350,322</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,732</td>
<td align="right">70,350,322</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,714,436</td>
<td align="right">6,628,879</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">39,798,841</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">297,033,245</td>
<td align="right">293,392,187</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">297,251,195</td>
<td align="right">293,608,247</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,348,589</td>
<td align="right">21,586,836</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">512,506,385</td>
<td align="right">508,138,859</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,425,380</td>
<td align="right">40,739,373</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">724,932,369</td>
<td align="right">719,496,503</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,406,145,419</td>
<td align="right">2,422,013,186</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,469,878</td>
<td align="right">78,975,258</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">992,359,441</td>
<td align="right">986,976,109</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,013,180</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,229,679</td>
<td align="right">1,347,113,482</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,088,427,510</td>
<td align="right">1,085,536,619</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">501,708,644</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,169,471</td>
<td align="right">220,863,767</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,594</td>
<td align="right">78,207,474</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">47,063,339</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,303,938,210</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,049,568,999</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">111,492,420</td>
<td align="right">111,492,420</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">94,389,039</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40,020,812</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">37,001,917</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">37,000,957</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,134,640</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,705,621</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">29,591,441</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,204,986</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,795,559</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_CONST_MORTAL</td>
<td align="right">3,840,960</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">815,372</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">98,482</td>
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
<td align="left">CALL</td>
<td align="right">7,223</td>
<td align="right">2,414</td>
<td align="right">-66.6%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,530</td>
<td align="right">23,001</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,550</td>
<td align="right">24,195</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
<td align="right"></td>
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
watched dict modification
<details>
<summary>ⓘ</summary>

A watched dict has been modified
</details>
</td>
<td align="right">160</td>
<td align="right">120</td>
<td align="right">-25.0%</td>
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
<td align="right">120</td>
<td align="right">-25.0%</td>
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
Stats gathered on: 2025-02-05
