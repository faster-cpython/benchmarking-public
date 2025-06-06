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
<td align="right">419,937,421</td>
<td align="right">621.1%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">11,706,045</td>
<td align="right">35,910,995</td>
<td align="right">206.8%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">206,464,054</td>
<td align="right">593,303,397</td>
<td align="right">187.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,975,070</td>
<td align="right">106,797,256</td>
<td align="right">33.5%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">23,563,767</td>
<td align="right">18,155,730</td>
<td align="right">-23.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">182,853,931</td>
<td align="right">143,765,021</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">781,020</td>
<td align="right">646,100</td>
<td align="right">-17.3%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">17,839,537</td>
<td align="right">20,768,256</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">143,907,591</td>
<td align="right">162,121,554</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">157,623,464</td>
<td align="right">137,946,312</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,857,063,664</td>
<td align="right">4,314,828,514</td>
<td align="right">11.9%</td>
</tr>
<tr>
<td align="left">NOT_TAKEN</td>
<td align="right">18,278,762</td>
<td align="right">20,349,023</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">137,620,387</td>
<td align="right">151,370,086</td>
<td align="right">10.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">4,245,163</td>
<td align="right">3,861,280</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">169,311,881</td>
<td align="right">154,120,441</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">61,655,295</td>
<td align="right">56,658,995</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,816,132</td>
<td align="right">93,108,007</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">36,806,275</td>
<td align="right">34,026,162</td>
<td align="right">-7.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">236,624,899</td>
<td align="right">254,123,708</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">68,201,583</td>
<td align="right">63,207,940</td>
<td align="right">-7.3%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">70,136,089</td>
<td align="right">65,308,316</td>
<td align="right">-6.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">328,953,526</td>
<td align="right">349,651,523</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,620,628,272</td>
<td align="right">1,713,779,835</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">95,957,136</td>
<td align="right">90,442,953</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">69,841,683</td>
<td align="right">66,025,572</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">609,737,015</td>
<td align="right">637,910,999</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,318,538,692</td>
<td align="right">2,425,515,364</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">2,090,173</td>
<td align="right">2,183,632</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">300,978,820</td>
<td align="right">288,989,688</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,954,636</td>
<td align="right">3,800,296</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">27,362,171</td>
<td align="right">28,348,291</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">113,206,776</td>
<td align="right">109,131,471</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">POP_ITER</td>
<td align="right">266,180,149</td>
<td align="right">275,548,146</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,490,327,013</td>
<td align="right">2,572,505,695</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">443,811,314</td>
<td align="right">431,181,079</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">81,668,644</td>
<td align="right">79,351,992</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">178,872,998</td>
<td align="right">173,860,770</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">88,428,906</td>
<td align="right">86,058,118</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,170,212,384</td>
<td align="right">2,112,309,955</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">13,764,694</td>
<td align="right">13,433,992</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_JIT</td>
<td align="right">171,729,919</td>
<td align="right">167,685,222</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">66,781,911</td>
<td align="right">65,259,296</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,850,351,068</td>
<td align="right">3,766,757,867</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">225,758,560</td>
<td align="right">230,589,448</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">331,490,771</td>
<td align="right">324,816,974</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">94,519,766</td>
<td align="right">92,656,941</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,770</td>
<td align="right">57,841</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">309,508,795</td>
<td align="right">303,990,297</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">79,643,198</td>
<td align="right">81,008,359</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">10,953,506</td>
<td align="right">10,785,595</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,801,646,240</td>
<td align="right">2,842,779,137</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">429,246,501</td>
<td align="right">423,261,668</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,616,965,219</td>
<td align="right">1,595,206,202</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">209,998,657</td>
<td align="right">207,210,210</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_MORTAL</td>
<td align="right">406,864,138</td>
<td align="right">401,485,741</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">539,623,241</td>
<td align="right">532,728,959</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">67,954,617</td>
<td align="right">67,207,861</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">392,928,977</td>
<td align="right">388,756,463</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,942,423</td>
<td align="right">3,901,072</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">534,473,288</td>
<td align="right">529,052,957</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">352,615,647</td>
<td align="right">355,897,859</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">36,730,820</td>
<td align="right">36,394,562</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">9,221,107</td>
<td align="right">9,137,368</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,492,839,321</td>
<td align="right">1,479,416,736</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">131,662,812</td>
<td align="right">130,481,046</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">328,341,453</td>
<td align="right">325,442,999</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">173,135,688</td>
<td align="right">171,609,343</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">659,760,007</td>
<td align="right">653,943,839</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">18,852,808</td>
<td align="right">18,687,993</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">9,741,906</td>
<td align="right">9,658,400</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,787,068,530</td>
<td align="right">1,771,806,516</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">853,354,224</td>
<td align="right">846,342,370</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">186,967,301</td>
<td align="right">188,452,871</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">145,780,804</td>
<td align="right">146,882,465</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">105,047,934</td>
<td align="right">105,753,658</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">716,586,005</td>
<td align="right">711,847,974</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">321,142,729</td>
<td align="right">319,339,330</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">65,399,659</td>
<td align="right">65,040,502</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">8,983,194</td>
<td align="right">9,032,333</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,932,439,714</td>
<td align="right">1,921,923,453</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">60,975,533</td>
<td align="right">60,645,755</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">170,068,018</td>
<td align="right">170,889,101</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,037,815,815</td>
<td align="right">2,047,619,991</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">26,873,138</td>
<td align="right">26,746,499</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">13,900,042,414</td>
<td align="right">13,835,572,843</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">67,248,577</td>
<td align="right">66,952,427</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">96,959,866</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">114,918,843</td>
<td align="right">114,449,081</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,281,409,095</td>
<td align="right">1,276,214,277</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">61,556,334</td>
<td align="right">61,316,119</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">155,964,783</td>
<td align="right">156,549,059</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">25,132,001</td>
<td align="right">25,224,745</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">173,416,046</td>
<td align="right">172,776,359</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">126,713,082</td>
<td align="right">126,248,179</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">229,154,667</td>
<td align="right">228,340,910</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">71,753,893</td>
<td align="right">71,514,078</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,126,358,381</td>
<td align="right">3,115,938,810</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">103,355,000</td>
<td align="right">103,697,120</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,825,535</td>
<td align="right">450,466,871</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">51,875,422</td>
<td align="right">51,724,986</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">3,219,484,908</td>
<td align="right">3,210,180,205</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,637,720</td>
<td align="right">118,901,687</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">250,328,302</td>
<td align="right">249,774,145</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">307,983,208</td>
<td align="right">308,637,034</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">112,042,901</td>
<td align="right">111,806,450</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">277,086,181</td>
<td align="right">277,661,130</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">710,019,358</td>
<td align="right">708,625,633</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">36,340,902</td>
<td align="right">36,410,151</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">48,635,022</td>
<td align="right">48,549,923</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">67,480,882</td>
<td align="right">67,596,428</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">701,413,824</td>
<td align="right">700,260,943</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">902,749,617</td>
<td align="right">901,369,473</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">57,539,258</td>
<td align="right">57,457,274</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">223,514,179</td>
<td align="right">223,210,962</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">57,578,089</td>
<td align="right">57,505,732</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,828,646,805</td>
<td align="right">4,823,175,785</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">98,855,922</td>
<td align="right">98,749,297</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">119,396,085</td>
<td align="right">119,283,828</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">485,573,232</td>
<td align="right">485,137,243</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">292,384,892</td>
<td align="right">292,145,666</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">271,110,400</td>
<td align="right">270,904,471</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">26,365,943</td>
<td align="right">26,385,488</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">139,906,067</td>
<td align="right">139,981,957</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">644,784,750</td>
<td align="right">644,457,072</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">189,637,073</td>
<td align="right">189,543,952</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">628,725,042</td>
<td align="right">628,463,189</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,294,673</td>
<td align="right">10,298,175</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,614,494</td>
<td align="right">133,571,111</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">159,730,031</td>
<td align="right">159,684,840</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">153,460,109</td>
<td align="right">153,418,795</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">133,131</td>
<td align="right">133,160</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,623,281</td>
<td align="right">330,551,848</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">251,870,320</td>
<td align="right">251,818,544</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">5,144</td>
<td align="right">5,145</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,962,529</td>
<td align="right">1,071,757,393</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">266,054,098</td>
<td align="right">266,009,953</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">58,613,354</td>
<td align="right">58,622,435</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">34,314,940</td>
<td align="right">34,309,800</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">180,516,819</td>
<td align="right">180,543,746</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">773,700</td>
<td align="right">773,597</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">95,362,280</td>
<td align="right">95,374,418</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">58,924,953</td>
<td align="right">58,932,224</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">36,614,787</td>
<td align="right">36,610,887</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">776,906,638</td>
<td align="right">776,981,942</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">42,660,466</td>
<td align="right">42,656,566</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">49,176,329</td>
<td align="right">49,171,926</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">405,606</td>
<td align="right">405,634</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">1,439,911</td>
<td align="right">1,439,812</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_JIT</td>
<td align="right">4,829,679</td>
<td align="right">4,829,366</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">20,547,461</td>
<td align="right">20,546,534</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">20,877,945</td>
<td align="right">20,877,018</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">20,877,965</td>
<td align="right">20,877,038</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">120,856</td>
<td align="right">120,858</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,115,150</td>
<td align="right">3,115,108</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">6,169,913</td>
<td align="right">6,169,875</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,760,193</td>
<td align="right">14,760,244</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">242,321,534</td>
<td align="right">242,320,920</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">21,773,878</td>
<td align="right">21,773,838</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">214,704,236</td>
<td align="right">214,704,522</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">31,880,523</td>
<td align="right">31,880,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">70,428,642</td>
<td align="right">70,428,641</td>
<td align="right">-0.0%</td>
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
<td align="left">BUILD_SLICE</td>
<td align="right">33,292,776</td>
<td align="right">33,292,776</td>
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
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,054,539</td>
<td align="right">4,054,539</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_GLOBAL</td>
<td align="right">2,573,060</td>
<td align="right">2,573,060</td>
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
<td align="left">RESUME</td>
<td align="right">33,737</td>
<td align="right">33,737</td>
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
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,641,211,651</td>
<td align="right">95.2%</td>
<td align="right">7,639,345,691</td>
<td align="right">95.2%</td>
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
<td align="right">330,461,515</td>
<td align="right">4.1%</td>
<td align="right">330,390,098</td>
<td align="right">4.1%</td>
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
<td align="right">50,997,629</td>
<td align="right">0.6%</td>
<td align="right">51,002,437</td>
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
<td align="right">153,174</td>
<td align="right">13.6%</td>
<td align="right">153,157</td>
<td align="right">13.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">970,775</td>
<td align="right">86.4%</td>
<td align="right">970,867</td>
<td align="right">86.4%</td>
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
<td align="left">true divide other</td>
<td align="right">1,384</td>
<td align="right">0.9%</td>
<td align="right">1,364</td>
<td align="right">0.9%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">627</td>
<td align="right">0.4%</td>
<td align="right">630</td>
<td align="right">0.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">495</td>
<td align="right">0.3%</td>
<td align="right">493</td>
<td align="right">0.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">17,767</td>
<td align="right">11.6%</td>
<td align="right">17,747</td>
<td align="right">11.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">18,469</td>
<td align="right">12.1%</td>
<td align="right">18,486</td>
<td align="right">12.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">20,059</td>
<td align="right">13.1%</td>
<td align="right">20,076</td>
<td align="right">13.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,830</td>
<td align="right">12.9%</td>
<td align="right">19,824</td>
<td align="right">12.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">23,474</td>
<td align="right">15.3%</td>
<td align="right">23,469</td>
<td align="right">15.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">5,458</td>
<td align="right">3.6%</td>
<td align="right">5,457</td>
<td align="right">3.6%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">xor int</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">17,023</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">6,572</td>
<td align="right">4.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">5,718</td>
<td align="right">3.7%</td>
<td align="right">5,718</td>
<td align="right">3.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
<td align="right">4,213</td>
<td align="right">2.8%</td>
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
<td align="left">true divide float</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">2,847</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">2,343</td>
<td align="right">1.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">1,996</td>
<td align="right">1.3%</td>
<td align="right">1,996</td>
<td align="right">1.3%</td>
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
<td align="right">97,359,536</td>
<td align="right">100.0%</td>
<td align="right">96,959,866</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">450,316,002</td>
<td align="right">7.6%</td>
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
<td align="right">5,824,996</td>
<td align="right">0.1%</td>
<td align="right">5,824,610</td>
<td align="right">0.1%</td>
<td align="right">-0.0%</td>
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
<td align="right">5,470,747,051</td>
<td align="right">92.3%</td>
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
<td align="right">141,932</td>
<td align="right">54.4%</td>
<td align="right">141,631</td>
<td align="right">54.4%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">118,913</td>
<td align="right">45.6%</td>
<td align="right">118,913</td>
<td align="right">45.6%</td>
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
<td align="left">buffer slice</td>
<td align="right">768</td>
<td align="right">0.5%</td>
<td align="right">688</td>
<td align="right">0.5%</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">3,677</td>
<td align="right">2.6%</td>
<td align="right">3,630</td>
<td align="right">2.6%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">7,096</td>
<td align="right">5.0%</td>
<td align="right">7,058</td>
<td align="right">5.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">35,055</td>
<td align="right">24.7%</td>
<td align="right">34,950</td>
<td align="right">24.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">16,574</td>
<td align="right">11.7%</td>
<td align="right">16,532</td>
<td align="right">11.7%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,443</td>
<td align="right">8.8%</td>
<td align="right">12,447</td>
<td align="right">8.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">59,676</td>
<td align="right">42.0%</td>
<td align="right">59,683</td>
<td align="right">42.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,609</td>
<td align="right">2.5%</td>
<td align="right">3,609</td>
<td align="right">2.5%</td>
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
<td align="right">126,485,229</td>
<td align="right">1.1%</td>
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
<td align="right">124,915,318</td>
<td align="right">1.1%</td>
<td align="right">124,329,852</td>
<td align="right">1.1%</td>
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
<td align="right">11,099,044,527</td>
<td align="right">98.9%</td>
<td align="right">11,095,774,398</td>
<td align="right">98.9%</td>
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
<td align="right">2,560,565</td>
<td align="right">100.0%</td>
<td align="right">-0.4%</td>
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
<td align="right">85,934,908</td>
<td align="right">1.9%</td>
<td align="right">-2.7%</td>
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
<td align="right">1,280,631</td>
<td align="right">0.0%</td>
<td align="right">0.3%</td>
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
<td align="right">4,516,977,412</td>
<td align="right">98.1%</td>
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
<td align="right">104,953</td>
<td align="right">71.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">42,019</td>
<td align="right">28.5%</td>
<td align="right">42,096</td>
<td align="right">28.6%</td>
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
<td align="left">bytes</td>
<td align="right">1,221</td>
<td align="right">1.2%</td>
<td align="right">861</td>
<td align="right">0.8%</td>
<td align="right">-29.5%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">359</td>
<td align="right">0.3%</td>
<td align="right">363</td>
<td align="right">0.3%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">941</td>
<td align="right">0.9%</td>
<td align="right">934</td>
<td align="right">0.9%</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">4,547</td>
<td align="right">4.3%</td>
<td align="right">4,569</td>
<td align="right">4.4%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,715</td>
<td align="right">7.3%</td>
<td align="right">7,691</td>
<td align="right">7.3%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,405</td>
<td align="right">8.0%</td>
<td align="right">8,426</td>
<td align="right">8.0%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">43,657</td>
<td align="right">41.4%</td>
<td align="right">43,562</td>
<td align="right">41.5%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,430</td>
<td align="right">6.1%</td>
<td align="right">6,431</td>
<td align="right">6.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">23,162</td>
<td align="right">22.0%</td>
<td align="right">23,159</td>
<td align="right">22.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,639</td>
<td align="right">7.2%</td>
<td align="right">7,639</td>
<td align="right">7.3%</td>
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
<td align="right">57,540,410</td>
<td align="right">2.6%</td>
<td align="right">57,468,072</td>
<td align="right">2.6%</td>
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
<td align="right">2,189,526,257</td>
<td align="right">97.4%</td>
<td align="right">2,189,236,460</td>
<td align="right">97.4%</td>
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
<td align="right">35,399</td>
<td align="right">47.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">38,435</td>
<td align="right">52.0%</td>
<td align="right">38,435</td>
<td align="right">52.1%</td>
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
<td align="right">7,856</td>
<td align="right">22.2%</td>
<td align="right">7,818</td>
<td align="right">22.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">str</td>
<td align="right">9,166</td>
<td align="right">25.9%</td>
<td align="right">9,205</td>
<td align="right">26.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">11,199</td>
<td align="right">31.6%</td>
<td align="right">11,180</td>
<td align="right">31.6%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">7,197</td>
<td align="right">20.3%</td>
<td align="right">7,196</td>
<td align="right">20.3%</td>
<td align="right">-0.0%</td>
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
<td align="right">47,792,736</td>
<td align="right">6.9%</td>
<td align="right">47.8%</td>
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
<td align="right">523,875,125</td>
<td align="right">75.9%</td>
<td align="right">-13.1%</td>
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
<td align="right">118,800,287</td>
<td align="right">17.2%</td>
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
<td align="left">Success</td>
<td align="right">615,107</td>
<td align="right">87.1%</td>
<td align="right">906,664</td>
<td align="right">90.4%</td>
<td align="right">47.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">91,376</td>
<td align="right">12.9%</td>
<td align="right">96,332</td>
<td align="right">9.6%</td>
<td align="right">5.4%</td>
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
<td align="right">48,286</td>
<td align="right">52.8%</td>
<td align="right">53,404</td>
<td align="right">55.4%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">seq iter</td>
<td align="right">6,164</td>
<td align="right">6.7%</td>
<td align="right">6,020</td>
<td align="right">6.2%</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">1,547</td>
<td align="right">1.7%</td>
<td align="right">1,566</td>
<td align="right">1.6%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">2,247</td>
<td align="right">2.5%</td>
<td align="right">2,227</td>
<td align="right">2.3%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">4,495</td>
<td align="right">4.9%</td>
<td align="right">4,476</td>
<td align="right">4.6%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">5,895</td>
<td align="right">6.5%</td>
<td align="right">5,874</td>
<td align="right">6.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,734</td>
<td align="right">11.7%</td>
<td align="right">10,757</td>
<td align="right">11.2%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,546</td>
<td align="right">5.0%</td>
<td align="right">4,546</td>
<td align="right">4.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">3,015</td>
<td align="right">3.3%</td>
<td align="right">3,015</td>
<td align="right">3.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,867</td>
<td align="right">3.1%</td>
<td align="right">2,867</td>
<td align="right">3.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">945</td>
<td align="right">1.0%</td>
<td align="right">0.0%</td>
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
<td align="right">658,319,476</td>
<td align="right">5.0%</td>
<td align="right">2.4%</td>
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
<td align="right">527,309,174</td>
<td align="right">4.0%</td>
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
<td align="right">12,094,784,929</td>
<td align="right">91.1%</td>
<td align="right">12,090,735,721</td>
<td align="right">91.1%</td>
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
<td align="right">481,359</td>
<td align="right">3.7%</td>
<td align="right">35.5%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">12,215,258</td>
<td align="right">97.2%</td>
<td align="right">12,507,229</td>
<td align="right">96.3%</td>
<td align="right">2.4%</td>
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
<td align="left">class method obj</td>
<td align="right">14,536</td>
<td align="right">4.1%</td>
<td align="right">13,182</td>
<td align="right">2.7%</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">23,828</td>
<td align="right">6.7%</td>
<td align="right">24,314</td>
<td align="right">5.1%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,608</td>
<td align="right">0.5%</td>
<td align="right">1,587</td>
<td align="right">0.3%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">38,455</td>
<td align="right">10.8%</td>
<td align="right">37,969</td>
<td align="right">7.9%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,912</td>
<td align="right">1.4%</td>
<td align="right">4,928</td>
<td align="right">1.0%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">40,702</td>
<td align="right">11.5%</td>
<td align="right">40,788</td>
<td align="right">8.5%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">855</td>
<td align="right">0.2%</td>
<td align="right">856</td>
<td align="right">0.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,404</td>
<td align="right">0.7%</td>
<td align="right">2,405</td>
<td align="right">0.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">60,050</td>
<td align="right">16.9%</td>
<td align="right">60,051</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">7,945</td>
<td align="right">2.2%</td>
<td align="right">7,945</td>
<td align="right">1.7%</td>
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
<td align="left">module attr not found</td>
<td align="right">5,087</td>
<td align="right">1.4%</td>
<td align="right">5,087</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,582</td>
<td align="right">0.4%</td>
<td align="right">1,582</td>
<td align="right">0.3%</td>
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
<td align="right">3,699,886,969</td>
<td align="right">99.6%</td>
<td align="right">-1.9%</td>
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
<td align="right">52,559</td>
<td align="right">0.0%</td>
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
<td align="right">14,622,703</td>
<td align="right">0.4%</td>
<td align="right">14,622,712</td>
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
<td align="right">138,301</td>
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
<td align="right">65,094,554</td>
<td align="right">100.0%</td>
<td align="right">64,639,716</td>
<td align="right">100.0%</td>
<td align="right">-0.7%</td>
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
<td align="right">65,933,377</td>
<td align="right">3.3%</td>
<td align="right">-5.5%</td>
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
<td align="right">1,844,816,572</td>
<td align="right">91.0%</td>
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
<td align="right">115,910,174</td>
<td align="right">5.7%</td>
<td align="right">115,906,210</td>
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
<td align="right">50,042</td>
<td align="right">2.2%</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,228,397</td>
<td align="right">97.8%</td>
<td align="right">2,228,327</td>
<td align="right">97.8%</td>
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
<td align="right">135,470</td>
<td align="right">265.8%</td>
<td align="right">263,011</td>
<td align="right">525.6%</td>
<td align="right">94.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">24,076</td>
<td align="right">47.2%</td>
<td align="right">23,256</td>
<td align="right">46.5%</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">4,954</td>
<td align="right">9.7%</td>
<td align="right">4,847</td>
<td align="right">9.7%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">3,344</td>
<td align="right">6.6%</td>
<td align="right">3,350</td>
<td align="right">6.7%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,666</td>
<td align="right">15.0%</td>
<td align="right">7,666</td>
<td align="right">15.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">5,098</td>
<td align="right">10.0%</td>
<td align="right">5,098</td>
<td align="right">10.2%</td>
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
<td align="right">1.5%</td>
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
<td align="right">133,525,199</td>
<td align="right">12.7%</td>
<td align="right">-0.0%</td>
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
<td align="right">920,133,054</td>
<td align="right">87.3%</td>
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
<td align="right">43,757</td>
<td align="right">95.2%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">2,195</td>
<td align="right">4.8%</td>
<td align="right">2,195</td>
<td align="right">4.8%</td>
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
<td align="right">8,143</td>
<td align="right">18.6%</td>
<td align="right">8,122</td>
<td align="right">18.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">14,752</td>
<td align="right">33.7%</td>
<td align="right">14,754</td>
<td align="right">33.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">16,703</td>
<td align="right">38.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">3,032</td>
<td align="right">6.9%</td>
<td align="right">0.0%</td>
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
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">236</td>
<td align="right">0.5%</td>
<td align="right">236</td>
<td align="right">0.5%</td>
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
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">40,958,294</td>
<td align="right">0.9%</td>
<td align="right">62,277,946</td>
<td align="right">1.3%</td>
<td align="right">52.1%</td>
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
<td align="right">103,299,731</td>
<td align="right">2.2%</td>
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
<td align="right">4,531,475,523</td>
<td align="right">96.9%</td>
<td align="right">4,519,075,264</td>
<td align="right">96.5%</td>
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
<td align="right">821,423</td>
<td align="right">66.5%</td>
<td align="right">1,223,730</td>
<td align="right">77.9%</td>
<td align="right">49.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">413,283</td>
<td align="right">33.5%</td>
<td align="right">347,266</td>
<td align="right">22.1%</td>
<td align="right">-16.0%</td>
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
<td align="right">256,193</td>
<td align="right">62.0%</td>
<td align="right">189,878</td>
<td align="right">54.7%</td>
<td align="right">-25.9%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">13,475</td>
<td align="right">3.3%</td>
<td align="right">12,581</td>
<td align="right">3.6%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">16,408</td>
<td align="right">4.0%</td>
<td align="right">17,267</td>
<td align="right">5.0%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">12,361</td>
<td align="right">3.0%</td>
<td align="right">12,636</td>
<td align="right">3.6%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,611</td>
<td align="right">2.1%</td>
<td align="right">8,640</td>
<td align="right">2.5%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">5,689</td>
<td align="right">1.4%</td>
<td align="right">5,691</td>
<td align="right">1.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">94,063</td>
<td align="right">22.8%</td>
<td align="right">94,090</td>
<td align="right">27.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">4,597</td>
<td align="right">1.1%</td>
<td align="right">4,597</td>
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">bytearray</td>
<td align="right">1,420</td>
<td align="right">0.3%</td>
<td align="right">1,420</td>
<td align="right">0.4%</td>
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
<td align="right">1,233,392,537</td>
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
<td align="right">1,427,528</td>
<td align="right">0.1%</td>
<td align="right">1,427,422</td>
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
<td align="right">869</td>
<td align="right">7.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">11,601</td>
<td align="right">93.1%</td>
<td align="right">11,601</td>
<td align="right">93.0%</td>
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
<td align="right">642</td>
<td align="right">73.9%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">15.8%</td>
<td align="right">136</td>
<td align="right">15.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">10.6%</td>
<td align="right">91</td>
<td align="right">10.5%</td>
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
<td align="right">1,019,951,052</td>
<td align="right">1.3%</td>
<td align="right">1,071,606,918</td>
<td align="right">1.3%</td>
<td align="right">5.1%</td>
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
<td align="right">31,240,811,489</td>
<td align="right">38.2%</td>
<td align="right">2.7%</td>
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
<td align="right">47,297,324,373</td>
<td align="right">57.9%</td>
<td align="right">0.7%</td>
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
<td align="right">2,119,565,889</td>
<td align="right">2.6%</td>
<td align="right">-0.6%</td>
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
<td align="right">88,305,264</td>
<td align="right">3.9%</td>
<td align="right">85,934,908</td>
<td align="right">3.8%</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">532,847,492</td>
<td align="right">23.6%</td>
<td align="right">527,309,174</td>
<td align="right">23.5%</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">124,915,318</td>
<td align="right">5.5%</td>
<td align="right">124,329,852</td>
<td align="right">5.5%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">97,359,536</td>
<td align="right">4.3%</td>
<td align="right">96,959,866</td>
<td align="right">4.3%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">102,891,601</td>
<td align="right">4.6%</td>
<td align="right">103,299,731</td>
<td align="right">4.6%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">451,674,365</td>
<td align="right">20.0%</td>
<td align="right">450,316,002</td>
<td align="right">20.1%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">118,541,268</td>
<td align="right">5.3%</td>
<td align="right">118,800,287</td>
<td align="right">5.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">133,568,563</td>
<td align="right">5.9%</td>
<td align="right">133,525,199</td>
<td align="right">6.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">330,461,515</td>
<td align="right">14.7%</td>
<td align="right">330,390,098</td>
<td align="right">14.7%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,816,906</td>
<td align="right">5.7%</td>
<td align="right">128,816,906</td>
<td align="right">5.7%</td>
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
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">74,458,461</td>
<td align="right">7.3%</td>
<td align="right">84,575,909</td>
<td align="right">7.9%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">75,730,649</td>
<td align="right">7.4%</td>
<td align="right">78,227,272</td>
<td align="right">7.3%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">255,322,860</td>
<td align="right">25.0%</td>
<td align="right">260,542,295</td>
<td align="right">24.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">184,014,368</td>
<td align="right">18.0%</td>
<td align="right">181,336,592</td>
<td align="right">16.9%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">69,073,265</td>
<td align="right">6.8%</td>
<td align="right">68,733,626</td>
<td align="right">6.4%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_EXTEND</td>
<td align="right">24,415,263</td>
<td align="right">2.4%</td>
<td align="right">24,417,623</td>
<td align="right">2.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">94,274,265</td>
<td align="right">9.2%</td>
<td align="right">94,272,785</td>
<td align="right">8.8%</td>
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
<td align="right">28,733,531</td>
<td align="right">2.7%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">27,063,550</td>
<td align="right">2.5%</td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">24,001,337</td>
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
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,580,347</td>
<td align="right">10.0%</td>
<td align="right">765,077,235</td>
<td align="right">11.4%</td>
<td align="right">14.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,718,273,238</td>
<td align="right">25.7%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,625,276,015</td>
<td align="right">24.3%</td>
<td align="right">1,718,273,238</td>
<td align="right">25.7%</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">5,068,170,298</td>
<td align="right">75.7%</td>
<td align="right">4,970,961,158</td>
<td align="right">74.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">71,634,001</td>
<td align="right">1.1%</td>
<td align="right">71,326,917</td>
<td align="right">1.1%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">279,386,706</td>
<td align="right">4.2%</td>
<td align="right">278,507,835</td>
<td align="right">4.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">952,563,525</td>
<td align="right">14.2%</td>
<td align="right">951,063,860</td>
<td align="right">14.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">954,695,668</td>
<td align="right">14.3%</td>
<td align="right">953,196,003</td>
<td align="right">14.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,462,609,859</td>
<td align="right">81.6%</td>
<td align="right">5,458,757,564</td>
<td align="right">81.6%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,922,432</td>
<td align="right">0.4%</td>
<td align="right">24,922,222</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,948</td>
<td align="right">3.9%</td>
<td align="right">261,407,334</td>
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
<td align="right">8,684,176</td>
<td align="right"></td>
<td align="right">8,967,611</td>
<td align="right"></td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">65,984,653</td>
<td align="right"></td>
<td align="right">67,452,312</td>
<td align="right"></td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">58,109,261</td>
<td align="right"></td>
<td align="right">59,293,172</td>
<td align="right"></td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">Interpreter immortal increfs</td>
<td align="right">8,925,103,433</td>
<td align="right">5.6%</td>
<td align="right">9,012,855,575</td>
<td align="right">5.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,179,985,728</td>
<td align="right"></td>
<td align="right">2,168,087,213</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">77,400,036,232</td>
<td align="right">48.2%</td>
<td align="right">76,979,588,305</td>
<td align="right">48.1%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">82,872,995,483</td>
<td align="right">41.1%</td>
<td align="right">82,428,445,558</td>
<td align="right">41.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">35,930,617,616</td>
<td align="right">22.4%</td>
<td align="right">35,760,810,377</td>
<td align="right">22.3%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">16,516,176,225</td>
<td align="right">8.2%</td>
<td align="right">16,573,501,533</td>
<td align="right">8.2%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">47,497,701,691</td>
<td align="right">23.6%</td>
<td align="right">47,347,003,183</td>
<td align="right">23.6%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">179,996,654</td>
<td align="right"></td>
<td align="right">179,665,709</td>
<td align="right"></td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">54,666,871,820</td>
<td align="right">27.1%</td>
<td align="right">54,577,936,193</td>
<td align="right">27.2%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">38,388,708,385</td>
<td align="right">23.9%</td>
<td align="right">38,364,721,050</td>
<td align="right">24.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">6,678,833,154</td>
<td align="right"></td>
<td align="right">6,676,201,526</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">6,009,403,952</td>
<td align="right">32.5%</td>
<td align="right">6,007,232,081</td>
<td align="right">32.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">6,087,339,143</td>
<td align="right">32.9%</td>
<td align="right">6,085,171,993</td>
<td align="right">32.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">12,399,378,238</td>
<td align="right">67.1%</td>
<td align="right">12,396,289,560</td>
<td align="right">67.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">12,399,472,251</td>
<td align="right"></td>
<td align="right">12,396,395,048</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,515,418</td>
<td align="right">0.4%</td>
<td align="right">71,520,023</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,419,773</td>
<td align="right">0.0%</td>
<td align="right">6,419,889</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">2,900,013,598</td>
<td align="right"></td>
<td align="right">2,899,998,096</td>
<td align="right"></td>
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
<td align="right">364,709</td>
<td align="right">103,148,733</td>
<td align="right">9,564,859,545</td>
<td align="right">756,671,760</td>
<td align="right">765,491,129</td>
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
<td align="right">5,607,770,814</td>
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
<td align="right">838</td>
<td align="right">0.2%</td>
<td align="right">1,022</td>
<td align="right">0.2%</td>
<td align="right">22.0%</td>
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
<td align="right">1,101</td>
<td align="right">0.2%</td>
<td align="right">12.1%</td>
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
<td align="right">6,473,383,844</td>
<td align="right"></td>
<td align="right">-8.0%</td>
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
<td align="right">288</td>
<td align="right">0.1%</td>
<td align="right">-6.5%</td>
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
<td align="right">269,099,114,425</td>
<td align="right">4,157.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">65,995</td>
<td align="right">13.0%</td>
<td align="right">-1.2%</td>
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
<td align="right">3,281</td>
<td align="right">0.6%</td>
<td align="right">1.1%</td>
</tr>
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
<td align="right">400,873</td>
<td align="right">78.7%</td>
<td align="right">0.7%</td>
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
<td align="right">442,987</td>
<td align="right">87.0%</td>
<td align="right">0.6%</td>
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
<td align="right">509,270</td>
<td align="right"></td>
<td align="right">0.3%</td>
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
<td align="right">502</td>
<td align="right">0.8%</td>
<td align="right">0.2%</td>
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
<td align="right">58,914</td>
<td align="right">89.3%</td>
<td align="right">-2.4%</td>
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
<td align="right">65,995</td>
<td align="right"></td>
<td align="right">-1.2%</td>
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
<td align="right">122,677,611</td>
<td align="right">18.6%</td>
<td align="right">-4.9%</td>
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
<td align="right">459,628,973</td>
<td align="right">69.7%</td>
<td align="right">2.2%</td>
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
<td align="right">77,579,496</td>
<td align="right">11.8%</td>
<td align="right">2.0%</td>
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
<td align="right">540,651,520</td>
<td align="right">81.9%</td>
<td align="right">-1.4%</td>
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
<td align="right">659,886,080</td>
<td align="right"></td>
<td align="right">0.8%</td>
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
<td align="left">12,443</td>
<td align="right">21.1%</td>
<td align="right">-17.7%</td>
</tr>
<tr>
<td align="left"><= 8,192</td>
<td align="left">24,334</td>
<td align="right">40.3%</td>
<td align="left">25,018</td>
<td align="right">42.5%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 16,384</td>
<td align="left">14,868</td>
<td align="right">24.6%</td>
<td align="left">15,340</td>
<td align="right">26.0%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left"><= 32,768</td>
<td align="left">4,139</td>
<td align="right">6.9%</td>
<td align="left">4,197</td>
<td align="right">7.1%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left"><= 65,536</td>
<td align="left">1,547</td>
<td align="right">2.6%</td>
<td align="left">1,568</td>
<td align="right">2.7%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left"><= 131,072</td>
<td align="left">328</td>
<td align="right">0.5%</td>
<td align="left">348</td>
<td align="right">0.6%</td>
<td align="right">6.1%</td>
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
<td align="right">5,162</td>
<td align="right">7.8%</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,253</td>
<td align="right">12.4%</td>
<td align="right">6,102</td>
<td align="right">9.2%</td>
<td align="right">-26.1%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">21,525</td>
<td align="right">32.2%</td>
<td align="right">22,140</td>
<td align="right">33.5%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">16,468</td>
<td align="right">24.7%</td>
<td align="right">17,012</td>
<td align="right">25.8%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">9,191</td>
<td align="right">13.8%</td>
<td align="right">10,010</td>
<td align="right">15.2%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">4,689</td>
<td align="right">7.0%</td>
<td align="right">4,649</td>
<td align="right">7.0%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">815</td>
<td align="right">1.2%</td>
<td align="right">838</td>
<td align="right">1.3%</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">82</td>
<td align="right">0.1%</td>
<td align="right">82</td>
<td align="right">0.1%</td>
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
<td align="right">1,917</td>
<td align="right">2.9%</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">8,191</td>
<td align="right">12.3%</td>
<td align="right">4,456</td>
<td align="right">6.8%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">8,455</td>
<td align="right">12.7%</td>
<td align="right">9,530</td>
<td align="right">14.4%</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">24,192</td>
<td align="right">36.2%</td>
<td align="right">24,965</td>
<td align="right">37.8%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">12,561</td>
<td align="right">18.8%</td>
<td align="right">12,969</td>
<td align="right">19.7%</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">3,462</td>
<td align="right">5.2%</td>
<td align="right">3,484</td>
<td align="right">5.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">1,246</td>
<td align="right">1.9%</td>
<td align="right">1,285</td>
<td align="right">1.9%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">288</td>
<td align="right">0.4%</td>
<td align="right">308</td>
<td align="right">0.5%</td>
<td align="right">6.9%</td>
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
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">123,165</td>
<td align="right">383,019</td>
<td align="right">211.0%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,202,667</td>
<td align="right">8,030,095</td>
<td align="right">150.7%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">6,818,123</td>
<td align="right">10,633,245</td>
<td align="right">56.0%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">1,049,568,999</td>
<td align="right">576,321,616</td>
<td align="right">-45.1%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,303,938,210</td>
<td align="right">867,707,391</td>
<td align="right">-33.5%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">2,615,370</td>
<td align="right">1,794,287</td>
<td align="right">-31.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">4,795,559</td>
<td align="right">6,137,343</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,168,619,009</td>
<td align="right">1,698,544,087</td>
<td align="right">-21.7%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">544,397</td>
<td align="right">428,113</td>
<td align="right">-21.4%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">20,513,079</td>
<td align="right">24,428,666</td>
<td align="right">19.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">23,680,384</td>
<td align="right">27,867,459</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">1,169,805</td>
<td align="right">965,622</td>
<td align="right">-17.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">114,399,380</td>
<td align="right">134,076,266</td>
<td align="right">17.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">209,658,948</td>
<td align="right">174,548,782</td>
<td align="right">-16.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">15,574,318</td>
<td align="right">17,890,820</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">284,807,439</td>
<td align="right">323,736,739</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">37,340,237</td>
<td align="right">42,351,331</td>
<td align="right">13.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">1,003,871</td>
<td align="right">878,853</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">1,617,596</td>
<td align="right">1,425,747</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,062,820</td>
<td align="right">52,470,857</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">1,560,112</td>
<td align="right">1,394,515</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">47,632,364</td>
<td align="right">52,640,522</td>
<td align="right">10.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,810,387,322</td>
<td align="right">1,643,243,336</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,033,994,861</td>
<td align="right">6,473,383,844</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">40,020,812</td>
<td align="right">37,050,660</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,662,322</td>
<td align="right">24,324,993</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">72,345,827</td>
<td align="right">77,610,262</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">221,169,471</td>
<td align="right">236,360,839</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,389,850,240</td>
<td align="right">1,484,752,186</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">96,398,763</td>
<td align="right">90,993,343</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">9,440,140,280</td>
<td align="right">8,914,881,608</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">48,241,948</td>
<td align="right">50,773,821</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">26,214,596</td>
<td align="right">27,577,291</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">95,268,190</td>
<td align="right">90,393,725</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">648,969,553</td>
<td align="right">620,355,497</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">436,746,875</td>
<td align="right">418,219,906</td>
<td align="right">-4.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">378,058,519</td>
<td align="right">364,397,656</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,266,469,850</td>
<td align="right">2,190,869,864</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,266,382,219</td>
<td align="right">2,190,846,062</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">29,954,571</td>
<td align="right">28,968,447</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">29,954,571</td>
<td align="right">28,968,447</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">536,303,591</td>
<td align="right">553,497,817</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">65,196,263</td>
<td align="right">63,340,125</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,194,550,597</td>
<td align="right">1,225,792,315</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">181,915</td>
<td align="right">186,255</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,086,367,727</td>
<td align="right">1,060,756,875</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">4,396,229,617</td>
<td align="right">4,295,874,819</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">296,945,206</td>
<td align="right">303,547,764</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">56,724,772</td>
<td align="right">57,968,282</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">167,979,708</td>
<td align="right">171,564,198</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">407,763,274</td>
<td align="right">399,506,923</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">309,438,152</td>
<td align="right">315,497,804</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">91,331,433</td>
<td align="right">93,119,214</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">88,367,803</td>
<td align="right">89,903,070</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">752,952,118</td>
<td align="right">765,282,106</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,010,152,054</td>
<td align="right">1,025,291,672</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">5,960,512,704</td>
<td align="right">5,871,486,827</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,406,145,419</td>
<td align="right">2,441,497,764</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">4,723,681,548</td>
<td align="right">4,790,042,136</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">6,154,665</td>
<td align="right">6,236,308</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">4,905,070,128</td>
<td align="right">4,965,788,664</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">113,182,193</td>
<td align="right">114,579,061</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,074,842,458</td>
<td align="right">2,049,616,544</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">2,865,196,522</td>
<td align="right">2,899,909,492</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">32,771,606,483</td>
<td align="right">32,375,699,862</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">502,921,084</td>
<td align="right">508,980,123</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">5,633,368,493</td>
<td align="right">5,566,297,288</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">571,941,216</td>
<td align="right">578,155,598</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">29,447,871</td>
<td align="right">29,765,153</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">30,211,904</td>
<td align="right">30,529,186</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,218,210,241</td>
<td align="right">4,261,956,766</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,692,422,957</td>
<td align="right">1,675,052,623</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,346,632,953</td>
<td align="right">1,360,424,390</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">504,580,749</td>
<td align="right">509,574,148</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">1,932,300,698</td>
<td align="right">1,913,833,458</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">700,393,130</td>
<td align="right">693,731,604</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">647,624,916</td>
<td align="right">653,069,215</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,198,462,390</td>
<td align="right">9,270,420,053</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">6,714,436</td>
<td align="right">6,665,116</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">6,696,290</td>
<td align="right">6,647,167</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">174,061,053</td>
<td align="right">172,793,522</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">5,376,935,668</td>
<td align="right">5,339,523,078</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,018,842,929</td>
<td align="right">1,025,796,188</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,620,799,310</td>
<td align="right">1,631,839,829</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">152,466,174</td>
<td align="right">153,504,249</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,467,637,445</td>
<td align="right">1,477,241,370</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">897,324,148</td>
<td align="right">902,937,625</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">1,710,401,063</td>
<td align="right">1,720,242,923</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">484,275,247</td>
<td align="right">486,988,329</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">9,232,795,950</td>
<td align="right">9,283,260,824</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">429,117,763</td>
<td align="right">431,382,630</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">4,463,680,569</td>
<td align="right">4,486,419,867</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">192,797,662</td>
<td align="right">191,850,351</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">83,999,188</td>
<td align="right">84,398,858</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,554,870,229</td>
<td align="right">1,562,046,453</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">208,585,462</td>
<td align="right">207,691,829</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">5,771,271,745</td>
<td align="right">5,795,193,595</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,223,586,685</td>
<td align="right">1,228,557,362</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">249,604,547</td>
<td align="right">248,609,006</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,165,639,474</td>
<td align="right">3,177,049,816</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">484,794,659</td>
<td align="right">486,489,489</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BINARY_OP_EXTEND</td>
<td align="right">168,890,217</td>
<td align="right">168,331,477</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_EXTEND</td>
<td align="right">159,116,666</td>
<td align="right">158,602,967</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,858,925,231</td>
<td align="right">1,864,772,068</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">40,425,380</td>
<td align="right">40,551,447</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">37,001,917</td>
<td align="right">37,114,337</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">37,000,957</td>
<td align="right">37,113,197</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">485,727,903</td>
<td align="right">487,143,773</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">117,726,002</td>
<td align="right">118,062,260</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">158,515,496</td>
<td align="right">158,965,767</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">576,845,478</td>
<td align="right">578,448,958</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,759,108,048</td>
<td align="right">2,766,610,844</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,089,073,391</td>
<td align="right">2,094,436,582</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">13,165,084</td>
<td align="right">13,198,768</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,834,865,347</td>
<td align="right">1,839,555,855</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">138,054,453</td>
<td align="right">138,398,594</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT</td>
<td align="right">725,039,253</td>
<td align="right">726,840,635</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">242,427,074</td>
<td align="right">243,016,477</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,098,865,752</td>
<td align="right">4,108,824,735</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">512,506,385</td>
<td align="right">511,535,544</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">49,726,160</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">49,818,820</td>
<td align="right">49,726,160</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,297,286,807</td>
<td align="right">8,312,588,841</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">97,684,124</td>
<td align="right">97,846,900</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">48,629,120</td>
<td align="right">48,553,220</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">43,283,323</td>
<td align="right">43,215,936</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,278,080</td>
<td align="right">60,184,600</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">335,155,842</td>
<td align="right">334,656,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">335,155,842</td>
<td align="right">334,656,442</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION_AND_LOCK</td>
<td align="right">335,270,882</td>
<td align="right">334,775,222</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,088,427,510</td>
<td align="right">1,086,900,101</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,221,383,421</td>
<td align="right">1,219,710,550</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,292,279,355</td>
<td align="right">4,297,760,499</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,222,263,000</td>
<td align="right">1,220,841,633</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">71,268,732</td>
<td align="right">71,350,646</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">71,268,732</td>
<td align="right">71,350,646</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">164,566,124</td>
<td align="right">164,748,560</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">724,932,369</td>
<td align="right">725,689,616</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">804,363,473</td>
<td align="right">803,583,753</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">194,365,047</td>
<td align="right">194,533,867</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,902,086,247</td>
<td align="right">1,903,589,404</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,151,797,624</td>
<td align="right">1,152,704,163</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,598,997,007</td>
<td align="right">4,602,397,587</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">792,417,586</td>
<td align="right">791,842,443</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">166,663,013</td>
<td align="right">166,769,633</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">172,166,252</td>
<td align="right">172,272,872</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">27,415,482,793</td>
<td align="right">27,431,234,626</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,352,229,679</td>
<td align="right">1,353,001,535</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">312,840,153</td>
<td align="right">313,015,522</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">21,348,589</td>
<td align="right">21,336,831</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">752,153,295</td>
<td align="right">751,818,819</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">269,263,237</td>
<td align="right">269,379,013</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">195,726,365</td>
<td align="right">195,650,485</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,910,468,424</td>
<td align="right">2,909,417,556</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">1,250,836</td>
<td align="right">1,250,408</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">647,439,727</td>
<td align="right">647,642,209</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,851,456,279</td>
<td align="right">1,851,950,994</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">171,099,272</td>
<td align="right">171,144,052</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,471,796,247</td>
<td align="right">2,472,409,627</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,299,340,421</td>
<td align="right">3,299,933,933</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,370,381,952</td>
<td align="right">1,370,620,926</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">537,551,034</td>
<td align="right">537,642,686</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">557,246,745</td>
<td align="right">557,335,763</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">500,430,593</td>
<td align="right">500,509,000</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">484,410,970</td>
<td align="right">484,482,043</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,005,724,073</td>
<td align="right">3,006,159,985</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,815,682,031</td>
<td align="right">3,816,022,342</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">545,548,388</td>
<td align="right">545,592,046</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">567,311,660</td>
<td align="right">567,355,090</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,043,601,673</td>
<td align="right">1,043,678,766</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">801,565,648</td>
<td align="right">801,617,424</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,562,396,336</td>
<td align="right">1,562,489,194</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">309,250,832</td>
<td align="right">309,268,581</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">78,392,486</td>
<td align="right">78,396,826</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">97,102,577</td>
<td align="right">97,107,717</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">78,196,594</td>
<td align="right">78,200,494</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">79,469,878</td>
<td align="right">79,473,778</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">578,981,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">578,954,664</td>
<td align="right">578,981,161</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">992,359,441</td>
<td align="right">992,403,586</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">97,751,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">97,754,771</td>
<td align="right">97,751,835</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">29,591,441</td>
<td align="right">29,591,061</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS</td>
<td align="right">297,033,245</td>
<td align="right">297,029,510</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">297,251,195</td>
<td align="right">297,247,460</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,304,301</td>
<td align="right">40,304,341</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">38,310,006</td>
<td align="right">38,309,975</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">495,343,741</td>
<td align="right">495,343,969</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">18,019,989</td>
<td align="right">18,019,991</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">444,211,436</td>
<td align="right">444,211,436</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">386,839,379</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">351,243,134</td>
<td align="right">351,243,134</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">287,427,225</td>
<td align="right">287,427,225</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL_CONDITIONAL</td>
<td align="right">129,244,604</td>
<td align="right">129,244,604</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">123,515,060</td>
<td align="right">123,515,060</td>
<td align="right">0.0%</td>
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
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">62,545,882</td>
<td align="right">62,545,882</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">52,084,880</td>
<td align="right">52,084,880</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">42,557,190</td>
<td align="right">42,557,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">41,512,720</td>
<td align="right">41,512,720</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">31,134,640</td>
<td align="right">31,134,640</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,705,621</td>
<td align="right">30,705,621</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE_PUSH_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">25,691,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE_FROM_KEYS</td>
<td align="right">25,691,171</td>
<td align="right">25,691,171</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">24,204,986</td>
<td align="right"></td>
<td align="right"></td>
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
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,579,440</td>
<td align="right">3,579,440</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,942,070</td>
<td align="right">2,942,070</td>
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
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">388,800</td>
<td align="right">388,800</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">98,482</td>
<td align="right">98,482</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right"></td>
<td align="right">134,920</td>
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
<td align="right">7,154</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">24,550</td>
<td align="right">24,600</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">23,530</td>
<td align="right">23,489</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">84</td>
<td align="right">84</td>
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
Stats gathered on: 2025-02-05
