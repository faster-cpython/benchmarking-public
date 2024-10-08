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
<td align="right">2,891,497</td>
<td align="right">1,525,911,694</td>
<td align="right">52,672.4%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">190,469,124</td>
<td align="right">1,483,345,333</td>
<td align="right">678.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">183,109,331</td>
<td align="right">957,009,223</td>
<td align="right">422.6%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">220,970,445</td>
<td align="right">1,148,762,678</td>
<td align="right">419.9%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">235,316,145</td>
<td align="right">1,164,567,688</td>
<td align="right">394.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">200,030,660</td>
<td align="right">970,158,013</td>
<td align="right">385.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">103,979,546</td>
<td align="right">435,833,155</td>
<td align="right">319.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">355,937,630</td>
<td align="right">1,283,340,341</td>
<td align="right">260.6%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">173,473</td>
<td align="right">549,253</td>
<td align="right">216.6%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">157,539,797</td>
<td align="right">469,698,279</td>
<td align="right">198.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">701,736,568</td>
<td align="right">1,614,698,554</td>
<td align="right">130.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">756,308,647</td>
<td align="right">1,719,735,253</td>
<td align="right">127.4%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">815,960,370</td>
<td align="right">1,746,521,097</td>
<td align="right">114.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">474,524,475</td>
<td align="right">924,544,065</td>
<td align="right">94.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">272,017,498</td>
<td align="right">520,332,039</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">615,748,436</td>
<td align="right">1,136,656,322</td>
<td align="right">84.6%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">4,735,635,630</td>
<td align="right">8,538,158,471</td>
<td align="right">80.3%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,849,665,181</td>
<td align="right">3,198,681,996</td>
<td align="right">72.9%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">473,343,566</td>
<td align="right">815,200,385</td>
<td align="right">72.2%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">722,445,157</td>
<td align="right">1,240,000,378</td>
<td align="right">71.6%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">7,537,983</td>
<td align="right">12,141,563</td>
<td align="right">61.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">49,524,944</td>
<td align="right">75,151,573</td>
<td align="right">51.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">33,096,017</td>
<td align="right">50,157,516</td>
<td align="right">51.6%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">43,001,186</td>
<td align="right">60,341,596</td>
<td align="right">40.3%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">4,997,918,896</td>
<td align="right">6,975,286,402</td>
<td align="right">39.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">652,978,499</td>
<td align="right">902,278,875</td>
<td align="right">38.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">3,973,163,028</td>
<td align="right">5,333,579,276</td>
<td align="right">34.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">4,070,149,702</td>
<td align="right">5,428,120,388</td>
<td align="right">33.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">16,662,378,847</td>
<td align="right">21,857,627,920</td>
<td align="right">31.2%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">815,568,888</td>
<td align="right">1,064,804,412</td>
<td align="right">30.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">109,741,061</td>
<td align="right">135,368,728</td>
<td align="right">23.4%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,816,294,292</td>
<td align="right">2,281,813,692</td>
<td align="right">-19.0%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">47,645,662</td>
<td align="right">53,689,114</td>
<td align="right">12.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">98,852,106</td>
<td align="right">110,841,878</td>
<td align="right">12.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">56,311,433</td>
<td align="right">62,397,203</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">93,140,744</td>
<td align="right">100,840,740</td>
<td align="right">8.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">353,003,217</td>
<td align="right">382,113,579</td>
<td align="right">8.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">81,270,584</td>
<td align="right">87,619,287</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">236,562,130</td>
<td align="right">254,561,954</td>
<td align="right">7.6%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">824,050,764</td>
<td align="right">884,560,533</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">384,594,866</td>
<td align="right">412,427,067</td>
<td align="right">7.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">673,924,215</td>
<td align="right">718,526,603</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">185,910,007</td>
<td align="right">198,179,228</td>
<td align="right">6.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,212,411,414</td>
<td align="right">1,291,310,775</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">337,333,727</td>
<td align="right">359,095,800</td>
<td align="right">6.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">103,105,046</td>
<td align="right">108,774,014</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">34,626,360</td>
<td align="right">36,476,586</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">47,313,736</td>
<td align="right">49,839,021</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">216,867,306</td>
<td align="right">228,288,888</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">1,050,470,329</td>
<td align="right">1,101,786,596</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">2,583,891,281</td>
<td align="right">2,701,724,165</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">276,934,700</td>
<td align="right">264,886,043</td>
<td align="right">-4.4%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">123,755,773</td>
<td align="right">129,121,977</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">91,866,883</td>
<td align="right">95,679,830</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">2,114,811,790</td>
<td align="right">2,199,998,702</td>
<td align="right">4.0%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">226,788,679</td>
<td align="right">235,432,553</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">3,654,024</td>
<td align="right">3,515,133</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">270,315,358</td>
<td align="right">280,295,118</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">364,359,809</td>
<td align="right">376,395,468</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">536,853,888</td>
<td align="right">554,585,349</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">457,752,229</td>
<td align="right">472,537,925</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">19,798,635</td>
<td align="right">20,435,265</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">53,590,552</td>
<td align="right">55,135,676</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">318,781,977</td>
<td align="right">327,937,039</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">138,661,355</td>
<td align="right">142,510,297</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">538,790,966</td>
<td align="right">553,071,886</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">165,530,102</td>
<td align="right">169,453,181</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">196,151,310</td>
<td align="right">200,686,655</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">324,705,485</td>
<td align="right">331,676,351</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">90,699,084</td>
<td align="right">92,504,952</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">762,689,275</td>
<td align="right">777,364,698</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">15,202,862</td>
<td align="right">14,913,038</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">4,916,380,017</td>
<td align="right">5,004,156,311</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">1,056,352,097</td>
<td align="right">1,074,617,699</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">136,087,578</td>
<td align="right">138,353,098</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">44,018,436</td>
<td align="right">44,731,457</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">143,115,529</td>
<td align="right">145,390,529</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">53,669,190</td>
<td align="right">52,826,564</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,900,143,216</td>
<td align="right">2,945,478,958</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">123,058,400</td>
<td align="right">124,946,399</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">53,165,524</td>
<td align="right">53,973,834</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">2,758,100,586</td>
<td align="right">2,799,721,537</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">56,983,728</td>
<td align="right">57,841,938</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">895,363,502</td>
<td align="right">907,810,926</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">199,682,429</td>
<td align="right">202,385,449</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">117,287,517</td>
<td align="right">118,870,403</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">71,730,853</td>
<td align="right">72,623,433</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">298,420,352</td>
<td align="right">301,855,516</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">37,561,430</td>
<td align="right">37,971,264</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">133,929,252</td>
<td align="right">135,364,623</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">394,248,029</td>
<td align="right">398,040,939</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">715,709,043</td>
<td align="right">722,400,729</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">9,785,492</td>
<td align="right">9,874,484</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">33,266,627</td>
<td align="right">33,555,265</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">52,829,756</td>
<td align="right">53,286,239</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">3,586,507</td>
<td align="right">3,557,510</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">495,368,484</td>
<td align="right">499,256,927</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">RETURN_CONST</td>
<td align="right">1,841,925,102</td>
<td align="right">1,854,489,538</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">8,844,640</td>
<td align="right">8,903,242</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">141,456,131</td>
<td align="right">142,381,686</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">164,405,526</td>
<td align="right">165,254,158</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">8,539,808</td>
<td align="right">8,579,196</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">70,947,424</td>
<td align="right">71,271,563</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">48,773,896</td>
<td align="right">48,983,940</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">83,046,604</td>
<td align="right">83,399,937</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">103,771,873</td>
<td align="right">104,199,724</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">16,275,204</td>
<td align="right">16,208,292</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,893,253</td>
<td align="right">2,904,385</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">58,254,362</td>
<td align="right">58,478,345</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">296,661,193</td>
<td align="right">297,791,396</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">43,448,685</td>
<td align="right">43,560,541</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,418,346</td>
<td align="right">1,421,863</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">10,593,683</td>
<td align="right">10,619,499</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">2,401,394,400</td>
<td align="right">2,406,933,655</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">72,079,677</td>
<td align="right">71,940,017</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">11,263,831</td>
<td align="right">11,284,688</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">4,495,109</td>
<td align="right">4,501,669</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">314,182,322</td>
<td align="right">314,576,422</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">198,407,301</td>
<td align="right">198,628,478</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">493,135,294</td>
<td align="right">493,676,286</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">60,311,177</td>
<td align="right">60,368,959</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">67,170,841</td>
<td align="right">67,227,494</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">35,019,872</td>
<td align="right">35,047,756</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">3,767,314,537</td>
<td align="right">3,764,315,708</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">268,166,108</td>
<td align="right">268,371,490</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">91,059,160</td>
<td align="right">91,117,815</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">22,254,306</td>
<td align="right">22,266,652</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">150,192,313</td>
<td align="right">150,261,523</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">223,966</td>
<td align="right">224,057</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">57,776,086</td>
<td align="right">57,799,352</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">200,997,022</td>
<td align="right">201,070,927</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">990,901,368</td>
<td align="right">991,256,063</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">339,322,338</td>
<td align="right">339,441,566</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">2,269,660,731</td>
<td align="right">2,268,896,950</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">402,585,234</td>
<td align="right">402,687,247</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">21,389,995</td>
<td align="right">21,395,410</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">246,816,778</td>
<td align="right">246,876,730</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">525,296</td>
<td align="right">525,180</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">107,225,663</td>
<td align="right">107,208,011</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">15,188</td>
<td align="right">15,190</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">21,084,034</td>
<td align="right">21,081,526</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">21,398,335</td>
<td align="right">21,395,891</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">10,995,029</td>
<td align="right">10,996,273</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,371,993,336</td>
<td align="right">1,372,121,219</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">231,622,221</td>
<td align="right">231,602,476</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">340,397,008</td>
<td align="right">340,421,019</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">719,152</td>
<td align="right">719,103</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">147,153,307</td>
<td align="right">147,161,747</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">225,010,782</td>
<td align="right">225,022,304</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">82,461,868</td>
<td align="right">82,464,146</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">268,749</td>
<td align="right">268,747</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">3,744,145</td>
<td align="right">3,744,119</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">120,751,620</td>
<td align="right">120,752,451</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">5,830,529</td>
<td align="right">5,830,553</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">20,353,769</td>
<td align="right">20,353,840</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">94,169,586</td>
<td align="right">94,169,886</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,399,104</td>
<td align="right">173,399,108</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">402,104,097</td>
<td align="right">402,104,103</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">91,887,611</td>
<td align="right">91,887,611</td>
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
<td align="left">LOAD_NAME</td>
<td align="right">10,355,283</td>
<td align="right">10,355,283</td>
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
<td align="left">STORE_NAME</td>
<td align="right">659,372</td>
<td align="right">659,372</td>
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
<td align="right">30,149</td>
<td align="right">30,149</td>
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
<td align="right">21,916</td>
<td align="right">21,916</td>
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
<td align="right">982</td>
<td align="right">982</td>
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
<td align="right">412,448,495</td>
<td align="right">4.2%</td>
<td align="right">440,272,650</td>
<td align="right">4.5%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">9,395,544,635</td>
<td align="right">95.8%</td>
<td align="right">9,395,500,746</td>
<td align="right">95.5%</td>
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
<td align="right">1,121,562</td>
<td align="right">65.2%</td>
<td align="right">1,129,594</td>
<td align="right">65.3%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">599,899</td>
<td align="right">34.8%</td>
<td align="right">599,913</td>
<td align="right">34.7%</td>
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
<td align="left">true divide float</td>
<td align="right">4,731</td>
<td align="right">0.4%</td>
<td align="right">9,531</td>
<td align="right">0.8%</td>
<td align="right">101.5%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">20,401</td>
<td align="right">1.8%</td>
<td align="right">23,199</td>
<td align="right">2.1%</td>
<td align="right">13.7%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">48,851</td>
<td align="right">4.4%</td>
<td align="right">49,041</td>
<td align="right">4.3%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">10,806</td>
<td align="right">1.0%</td>
<td align="right">10,846</td>
<td align="right">1.0%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">833</td>
<td align="right">0.1%</td>
<td align="right">835</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">14,565</td>
<td align="right">1.3%</td>
<td align="right">14,592</td>
<td align="right">1.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">82,905</td>
<td align="right">7.4%</td>
<td align="right">83,045</td>
<td align="right">7.4%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">31,354</td>
<td align="right">2.8%</td>
<td align="right">31,388</td>
<td align="right">2.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">31,288</td>
<td align="right">2.8%</td>
<td align="right">31,265</td>
<td align="right">2.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">8,250</td>
<td align="right">0.7%</td>
<td align="right">8,254</td>
<td align="right">0.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">true divide other</td>
<td align="right">2,963</td>
<td align="right">0.3%</td>
<td align="right">2,962</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">49,346</td>
<td align="right">4.4%</td>
<td align="right">49,362</td>
<td align="right">4.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">8,471</td>
<td align="right">0.8%</td>
<td align="right">8,473</td>
<td align="right">0.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">5,627</td>
<td align="right">0.5%</td>
<td align="right">5,626</td>
<td align="right">0.5%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">781,602</td>
<td align="right">69.7%</td>
<td align="right">781,606</td>
<td align="right">69.2%</td>
<td align="right">0.0%</td>
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
<td align="left">xor</td>
<td align="right">6,806</td>
<td align="right">0.6%</td>
<td align="right">6,806</td>
<td align="right">0.6%</td>
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
<td align="right">657,367,337</td>
<td align="right">9.6%</td>
<td align="right">906,619,087</td>
<td align="right">12.8%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">4,792,339</td>
<td align="right">0.1%</td>
<td align="right">4,803,592</td>
<td align="right">0.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">6,201,989,128</td>
<td align="right">90.4%</td>
<td align="right">6,200,484,873</td>
<td align="right">87.2%</td>
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
<td align="right">221,934</td>
<td align="right">55.0%</td>
<td align="right">281,591</td>
<td align="right">60.8%</td>
<td align="right">26.9%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">181,567</td>
<td align="right">45.0%</td>
<td align="right">181,789</td>
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
<td align="right">109,051</td>
<td align="right">49.1%</td>
<td align="right">169,789</td>
<td align="right">60.3%</td>
<td align="right">55.7%</td>
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
<td align="right">58,325</td>
<td align="right">26.3%</td>
<td align="right">57,165</td>
<td align="right">20.3%</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">buffer int</td>
<td align="right">21,332</td>
<td align="right">9.6%</td>
<td align="right">21,371</td>
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
<td align="left">tuple slice</td>
<td align="right">126</td>
<td align="right">0.1%</td>
<td align="right">126</td>
<td align="right">0.0%</td>
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
<td align="right">150,766,381</td>
<td align="right">1.1%</td>
<td align="right">157,027,057</td>
<td align="right">1.1%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">640,363,505</td>
<td align="right">4.5%</td>
<td align="right">647,046,981</td>
<td align="right">4.6%</td>
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
<td align="right">13,489,115,776</td>
<td align="right">95.4%</td>
<td align="right">13,479,923,044</td>
<td align="right">95.4%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">33,000</td>
<td align="right">0.0%</td>
<td align="right">33,000</td>
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
<td align="right">3,370,584</td>
<td align="right">95.3%</td>
<td align="right">3,488,644</td>
<td align="right">95.4%</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">167,586</td>
<td align="right">4.7%</td>
<td align="right">167,718</td>
<td align="right">4.6%</td>
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
<td align="left">class no vectorcall</td>
<td align="right">156,733</td>
<td align="right">93.5%</td>
<td align="right">156,865</td>
<td align="right">93.5%</td>
<td align="right">0.1%</td>
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
<td align="right">105,062,912</td>
<td align="right">1.8%</td>
<td align="right">436,811,069</td>
<td align="right">7.1%</td>
<td align="right">315.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,327,599</td>
<td align="right">0.0%</td>
<td align="right">1,301,584</td>
<td align="right">0.0%</td>
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
<td align="right">5,722,151,289</td>
<td align="right">98.2%</td>
<td align="right">5,721,954,979</td>
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
<td align="right">164,501</td>
<td align="right">67.4%</td>
<td align="right">244,386</td>
<td align="right">75.5%</td>
<td align="right">48.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">79,732</td>
<td align="right">32.6%</td>
<td align="right">79,284</td>
<td align="right">24.5%</td>
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
<td align="left">tuple</td>
<td align="right">12,226</td>
<td align="right">7.4%</td>
<td align="right">93,062</td>
<td align="right">38.1%</td>
<td align="right">661.2%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">1,536</td>
<td align="right">0.9%</td>
<td align="right">1,454</td>
<td align="right">0.6%</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">different types</td>
<td align="right">48,489</td>
<td align="right">29.5%</td>
<td align="right">47,441</td>
<td align="right">19.4%</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">19,429</td>
<td align="right">11.8%</td>
<td align="right">19,590</td>
<td align="right">8.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">17,417</td>
<td align="right">10.6%</td>
<td align="right">17,455</td>
<td align="right">7.1%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">33,000</td>
<td align="right">20.1%</td>
<td align="right">32,977</td>
<td align="right">13.5%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">14,514</td>
<td align="right">8.8%</td>
<td align="right">14,517</td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
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
<td align="right">1.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">2,700</td>
<td align="right">1.6%</td>
<td align="right">2,700</td>
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
<td align="right">51,933,188</td>
<td align="right">2.0%</td>
<td align="right">77,552,827</td>
<td align="right">3.0%</td>
<td align="right">49.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,486,756,401</td>
<td align="right">97.9%</td>
<td align="right">2,486,655,745</td>
<td align="right">97.0%</td>
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
<td align="right">76,797</td>
<td align="right">55.7%</td>
<td align="right">83,787</td>
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
<td align="right">14,490</td>
<td align="right">18.9%</td>
<td align="right">15,250</td>
<td align="right">18.2%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">27,617</td>
<td align="right">36.0%</td>
<td align="right">28,335</td>
<td align="right">33.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">15,188</td>
<td align="right">19.8%</td>
<td align="right">15,100</td>
<td align="right">18.0%</td>
<td align="right">-0.6%</td>
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
<td align="right">6,747,252</td>
<td align="right">0.6%</td>
<td align="right">37,666,222</td>
<td align="right">1.6%</td>
<td align="right">458.2%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">565,221,154</td>
<td align="right">54.0%</td>
<td align="right">1,336,115,450</td>
<td align="right">58.1%</td>
<td align="right">136.4%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">480,897,388</td>
<td align="right">46.0%</td>
<td align="right">961,141,555</td>
<td align="right">41.8%</td>
<td align="right">99.9%</td>
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
<td align="right">175,747</td>
<td align="right">46.9%</td>
<td align="right">759,143</td>
<td align="right">71.0%</td>
<td align="right">332.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">198,592</td>
<td align="right">53.1%</td>
<td align="right">309,589</td>
<td align="right">29.0%</td>
<td align="right">55.9%</td>
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
<td align="right">1,279</td>
<td align="right">0.4%</td>
<td align="right">106.3%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">104,982</td>
<td align="right">52.9%</td>
<td align="right">206,322</td>
<td align="right">66.6%</td>
<td align="right">96.5%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">4,956</td>
<td align="right">2.5%</td>
<td align="right">7,896</td>
<td align="right">2.6%</td>
<td align="right">59.3%</td>
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
<td align="left">other</td>
<td align="right">6,565</td>
<td align="right">3.3%</td>
<td align="right">8,365</td>
<td align="right">2.7%</td>
<td align="right">27.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">11,055</td>
<td align="right">5.6%</td>
<td align="right">12,288</td>
<td align="right">4.0%</td>
<td align="right">11.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">11,315</td>
<td align="right">5.7%</td>
<td align="right">12,016</td>
<td align="right">3.9%</td>
<td align="right">6.2%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">36,248</td>
<td align="right">18.3%</td>
<td align="right">36,953</td>
<td align="right">11.9%</td>
<td align="right">1.9%</td>
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
<td align="right">305,141,136</td>
<td align="right">1.9%</td>
<td align="right">435,860,561</td>
<td align="right">2.7%</td>
<td align="right">42.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">971,830,539</td>
<td align="right">6.0%</td>
<td align="right">1,143,631,426</td>
<td align="right">7.0%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">15,090,582,629</td>
<td align="right">93.9%</td>
<td align="right">15,101,305,881</td>
<td align="right">92.9%</td>
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
<td align="right">303,860</td>
<td align="right">0.0%</td>
<td align="right">303,860</td>
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
<td align="right">863,817</td>
<td align="right">11.9%</td>
<td align="right">1,918,759</td>
<td align="right">17.8%</td>
<td align="right">122.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">6,370,995</td>
<td align="right">88.1%</td>
<td align="right">8,836,979</td>
<td align="right">82.2%</td>
<td align="right">38.7%</td>
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
<td align="right">155,916</td>
<td align="right">18.0%</td>
<td align="right">673,728</td>
<td align="right">35.1%</td>
<td align="right">332.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">159,341</td>
<td align="right">18.4%</td>
<td align="right">687,296</td>
<td align="right">35.8%</td>
<td align="right">331.3%</td>
</tr>
<tr>
<td align="left">shadowed</td>
<td align="right">89,644</td>
<td align="right">10.4%</td>
<td align="right">92,979</td>
<td align="right">4.8%</td>
<td align="right">3.7%</td>
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
<td align="right">176,743</td>
<td align="right">20.5%</td>
<td align="right">180,242</td>
<td align="right">9.4%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">non string or split</td>
<td align="right">20,293</td>
<td align="right">2.3%</td>
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
<td align="left">not in keys</td>
<td align="right">15,622</td>
<td align="right">1.8%</td>
<td align="right">15,842</td>
<td align="right">0.8%</td>
<td align="right">1.4%</td>
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
<td align="right">17,670</td>
<td align="right">2.0%</td>
<td align="right">17,873</td>
<td align="right">0.9%</td>
<td align="right">1.1%</td>
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
<td align="left">class method obj</td>
<td align="right">17,529</td>
<td align="right">2.0%</td>
<td align="right">17,669</td>
<td align="right">0.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">78,394</td>
<td align="right">9.1%</td>
<td align="right">78,885</td>
<td align="right">4.1%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">87,496</td>
<td align="right">10.1%</td>
<td align="right">87,945</td>
<td align="right">4.6%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">5,735</td>
<td align="right">0.7%</td>
<td align="right">5,733</td>
<td align="right">0.3%</td>
<td align="right">-0.0%</td>
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
<td align="left">out of versions</td>
<td align="right">420</td>
<td align="right">0.0%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<td align="right">4,846,990,629</td>
<td align="right">99.6%</td>
<td align="right">6,236,004,301</td>
<td align="right">99.7%</td>
<td align="right">28.7%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">434,723</td>
<td align="right">0.0%</td>
<td align="right">437,022</td>
<td align="right">0.0%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">20,322,061</td>
<td align="right">0.4%</td>
<td align="right">20,324,333</td>
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
<td align="right">9,556</td>
<td align="right">0.0%</td>
<td align="right">9,556</td>
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
<td align="right">466,431</td>
<td align="right">100.0%</td>
<td align="right">466,529</td>
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
<td align="right">86,220,182</td>
<td align="right">100.0%</td>
<td align="right">86,080,496</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">7,627</td>
<td align="right">0.0%</td>
<td align="right">7,629</td>
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
<td align="right">7,561</td>
<td align="right">100.0%</td>
<td align="right">7,561</td>
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
<td align="right">786,232,587</td>
<td align="right">81.9%</td>
<td align="right">786,232,613</td>
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
<td align="right">173,364,456</td>
<td align="right">18.1%</td>
<td align="right">173,364,460</td>
<td align="right">18.1%</td>
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
<td align="right">111,551,977</td>
<td align="right">4.3%</td>
<td align="right">114,920,033</td>
<td align="right">4.4%</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">162,086,699</td>
<td align="right">6.2%</td>
<td align="right">165,847,284</td>
<td align="right">6.3%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">2,455,737,315</td>
<td align="right">93.7%</td>
<td align="right">2,454,501,559</td>
<td align="right">93.6%</td>
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
<td align="right">2,202,502</td>
<td align="right">96.0%</td>
<td align="right">2,266,076</td>
<td align="right">96.1%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">92,532</td>
<td align="right">4.0%</td>
<td align="right">92,912</td>
<td align="right">3.9%</td>
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
<td align="left">class attr simple</td>
<td align="right">31,964</td>
<td align="right">34.5%</td>
<td align="right">32,284</td>
<td align="right">34.7%</td>
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
<td align="left">non string or split</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">14,077</td>
<td align="right">15.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">9,777</td>
<td align="right">10.6%</td>
<td align="right">9,777</td>
<td align="right">10.5%</td>
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
<td align="left">method</td>
<td align="right">804</td>
<td align="right">0.9%</td>
<td align="right">804</td>
<td align="right">0.9%</td>
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
<td align="right">271,896,428</td>
<td align="right">23.7%</td>
<td align="right">520,150,134</td>
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
<td align="right">875,306,039</td>
<td align="right">76.3%</td>
<td align="right">875,202,644</td>
<td align="right">62.7%</td>
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
<td align="right">110,600</td>
<td align="right">89.2%</td>
<td align="right">171,432</td>
<td align="right">92.8%</td>
<td align="right">55.0%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">13,370</td>
<td align="right">10.8%</td>
<td align="right">13,373</td>
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
<td align="right">7,657</td>
<td align="right">6.9%</td>
<td align="right">7,729</td>
<td align="right">4.5%</td>
<td align="right">0.9%</td>
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
<td align="right">24,999,217</td>
<td align="right">0.4%</td>
<td align="right">31,219,064</td>
<td align="right">0.5%</td>
<td align="right">24.9%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">188,487,628</td>
<td align="right">3.2%</td>
<td align="right">195,428,122</td>
<td align="right">3.3%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">5,754,485,302</td>
<td align="right">96.8%</td>
<td align="right">5,767,059,558</td>
<td align="right">96.7%</td>
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
<td align="right">664,583</td>
<td align="right">72.5%</td>
<td align="right">781,983</td>
<td align="right">74.8%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">252,532</td>
<td align="right">27.5%</td>
<td align="right">263,117</td>
<td align="right">25.2%</td>
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
<td align="right">37,262</td>
<td align="right">14.8%</td>
<td align="right">45,715</td>
<td align="right">17.4%</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">17,145</td>
<td align="right">6.8%</td>
<td align="right">17,725</td>
<td align="right">6.7%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">24,185</td>
<td align="right">9.6%</td>
<td align="right">24,507</td>
<td align="right">9.3%</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">83,202</td>
<td align="right">32.9%</td>
<td align="right">84,197</td>
<td align="right">32.0%</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">6,969</td>
<td align="right">2.8%</td>
<td align="right">7,043</td>
<td align="right">2.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,110</td>
<td align="right">2.4%</td>
<td align="right">6,160</td>
<td align="right">2.3%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">54,873</td>
<td align="right">21.7%</td>
<td align="right">54,990</td>
<td align="right">20.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">19,894</td>
<td align="right">7.9%</td>
<td align="right">19,888</td>
<td align="right">7.6%</td>
<td align="right">-0.0%</td>
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
<td align="right">194,643</td>
<td align="right">0.0%</td>
<td align="right">195,844</td>
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
<td align="right">1,529,347,788</td>
<td align="right">100.0%</td>
<td align="right">1,529,564,601</td>
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
<td align="right">30,543</td>
<td align="right">94.3%</td>
<td align="right">30,591</td>
<td align="right">94.3%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">1,860</td>
<td align="right">5.7%</td>
<td align="right">1,862</td>
<td align="right">5.7%</td>
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
<td align="right">1,213</td>
<td align="right">65.2%</td>
<td align="right">1,215</td>
<td align="right">65.3%</td>
<td align="right">0.2%</td>
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
<td align="right">14.4%</td>
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
<td align="right">9,327,383,161</td>
<td align="right">9.5%</td>
<td align="right">12,851,323,612</td>
<td align="right">10.2%</td>
<td align="right">37.8%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">32,594,553,465</td>
<td align="right">33.3%</td>
<td align="right">42,204,221,534</td>
<td align="right">33.4%</td>
<td align="right">29.5%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">55,207,490,499</td>
<td align="right">56.5%</td>
<td align="right">70,656,258,263</td>
<td align="right">55.8%</td>
<td align="right">28.0%</td>
</tr>
<tr>
<td align="left">
Specialized misses
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that deopt.
</details>
</td>
<td align="right">638,126,508</td>
<td align="right">0.7%</td>
<td align="right">815,601,621</td>
<td align="right">0.6%</td>
<td align="right">27.8%</td>
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
<td align="right">105,062,912</td>
<td align="right">2.5%</td>
<td align="right">436,811,069</td>
<td align="right">7.7%</td>
<td align="right">315.8%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">480,897,388</td>
<td align="right">11.6%</td>
<td align="right">961,141,555</td>
<td align="right">16.9%</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">271,896,428</td>
<td align="right">6.6%</td>
<td align="right">520,150,134</td>
<td align="right">9.1%</td>
<td align="right">91.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">657,367,337</td>
<td align="right">15.9%</td>
<td align="right">906,619,087</td>
<td align="right">15.9%</td>
<td align="right">37.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">971,830,539</td>
<td align="right">23.5%</td>
<td align="right">1,143,631,426</td>
<td align="right">20.1%</td>
<td align="right">17.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">412,448,495</td>
<td align="right">10.0%</td>
<td align="right">440,272,650</td>
<td align="right">7.7%</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">188,487,628</td>
<td align="right">4.6%</td>
<td align="right">195,428,122</td>
<td align="right">3.4%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">162,086,699</td>
<td align="right">3.9%</td>
<td align="right">165,847,284</td>
<td align="right">2.9%</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">640,363,505</td>
<td align="right">15.5%</td>
<td align="right">647,046,981</td>
<td align="right">11.4%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">173,364,456</td>
<td align="right">4.2%</td>
<td align="right">173,364,460</td>
<td align="right">3.0%</td>
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
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">67,368,533</td>
<td align="right">10.6%</td>
<td align="right">131,298,830</td>
<td align="right">16.1%</td>
<td align="right">94.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">129,866,536</td>
<td align="right">20.3%</td>
<td align="right">180,704,597</td>
<td align="right">22.2%</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">37,898,174</td>
<td align="right">5.9%</td>
<td align="right">46,933,380</td>
<td align="right">5.8%</td>
<td align="right">23.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">35,507,969</td>
<td align="right">5.6%</td>
<td align="right">39,515,173</td>
<td align="right">4.8%</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">87,670,397</td>
<td align="right">13.7%</td>
<td align="right">91,026,376</td>
<td align="right">11.2%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">80,573,306</td>
<td align="right">12.6%</td>
<td align="right">83,498,663</td>
<td align="right">10.2%</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">23,857,914</td>
<td align="right">3.7%</td>
<td align="right">23,869,991</td>
<td align="right">2.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">27,497,439</td>
<td align="right">4.3%</td>
<td align="right">27,497,433</td>
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
<td align="right">17,999,747</td>
<td align="right">2.8%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">18,845,557</td>
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
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">334,244,106</td>
<td align="right">4.0%</td>
<td align="right">333,531,767</td>
<td align="right">4.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,417,148,046</td>
<td align="right">16.8%</td>
<td align="right">1,416,257,780</td>
<td align="right">16.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,421,596,487</td>
<td align="right">16.9%</td>
<td align="right">1,420,706,221</td>
<td align="right">16.9%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frame objects created</td>
<td align="right">84,758,775</td>
<td align="right">1.0%</td>
<td align="right">84,720,651</td>
<td align="right">1.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">2,273,477,874</td>
<td align="right">27.0%</td>
<td align="right">2,272,685,414</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">2,273,477,874</td>
<td align="right">27.0%</td>
<td align="right">2,272,685,414</td>
<td align="right">27.0%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">6,670,677,949</td>
<td align="right">79.1%</td>
<td align="right">6,669,794,687</td>
<td align="right">79.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">851,881,387</td>
<td align="right">10.1%</td>
<td align="right">851,979,193</td>
<td align="right">10.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">331,645,150</td>
<td align="right">3.9%</td>
<td align="right">331,646,539</td>
<td align="right">3.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">6,157,978,407</td>
<td align="right">73.0%</td>
<td align="right">6,157,986,971</td>
<td align="right">73.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">31,097,683</td>
<td align="right">0.4%</td>
<td align="right">31,097,725</td>
<td align="right">0.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">175,480,468</td>
<td align="right">2.1%</td>
<td align="right">175,480,475</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">4,418,292</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">30,149</td>
<td align="right">0.0%</td>
<td align="right">30,149</td>
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
<td align="right">44,342,471,930</td>
<td align="right">32.1%</td>
<td align="right">53,619,613,683</td>
<td align="right">39.4%</td>
<td align="right">20.9%</td>
</tr>
<tr>
<td align="left">Interpreter decrefs</td>
<td align="right">60,706,920,319</td>
<td align="right">37.7%</td>
<td align="right">70,657,925,029</td>
<td align="right">44.6%</td>
<td align="right">16.4%</td>
</tr>
<tr>
<td align="left">Increfs</td>
<td align="right">93,986,223,580</td>
<td align="right">67.9%</td>
<td align="right">82,327,849,039</td>
<td align="right">60.6%</td>
<td align="right">-12.4%</td>
</tr>
<tr>
<td align="left">Decrefs</td>
<td align="right">100,136,339,799</td>
<td align="right">62.3%</td>
<td align="right">87,807,977,483</td>
<td align="right">55.4%</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">6,088,882</td>
<td align="right"></td>
<td align="right">6,650,195</td>
<td align="right"></td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">70,147,135</td>
<td align="right"></td>
<td align="right">74,903,106</td>
<td align="right"></td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">65,054,096</td>
<td align="right"></td>
<td align="right">69,247,595</td>
<td align="right"></td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">92,950,599</td>
<td align="right">0.4%</td>
<td align="right">93,574,502</td>
<td align="right">0.4%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">2,537,588,846</td>
<td align="right"></td>
<td align="right">2,525,784,516</td>
<td align="right"></td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">4,362,920,989</td>
<td align="right"></td>
<td align="right">4,365,406,803</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">173,503,115</td>
<td align="right"></td>
<td align="right">173,423,486</td>
<td align="right"></td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">13,592,880,577</td>
<td align="right"></td>
<td align="right">13,595,231,493</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">11,639,667,998</td>
<td align="right"></td>
<td align="right">11,640,805,805</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">11,637,755,894</td>
<td align="right">47.4%</td>
<td align="right">11,638,866,886</td>
<td align="right">47.4%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">15,359,300</td>
<td align="right">0.1%</td>
<td align="right">15,360,332</td>
<td align="right">0.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">12,892,890,624</td>
<td align="right">52.6%</td>
<td align="right">12,893,702,949</td>
<td align="right">52.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">12,784,580,725</td>
<td align="right">52.1%</td>
<td align="right">12,784,768,115</td>
<td align="right">52.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">3,382,240</td>
<td align="right">1.9%</td>
<td align="right">3,382,240</td>
<td align="right">2.0%</td>
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
<td align="right">114,158,288</td>
<td align="right">19,489,386,315</td>
<td align="right">0</td>
<td align="right">114,781,937</td>
<td align="right">19,542,475,750</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,972,166,388</td>
<td align="right">0</td>
<td align="right">10,755,840</td>
<td align="right">6,971,631,120</td>
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
<td align="right">946</td>
<td align="right">0.1%</td>
<td align="right">18,113</td>
<td align="right">0.9%</td>
<td align="right">1,814.7%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">170,596</td>
<td align="right">17.3%</td>
<td align="right">1,043,515</td>
<td align="right">54.1%</td>
<td align="right">511.7%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">10,572</td>
<td align="right">1.1%</td>
<td align="right">22,498</td>
<td align="right">1.2%</td>
<td align="right">112.8%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">985,936</td>
<td align="right"></td>
<td align="right">1,930,347</td>
<td align="right"></td>
<td align="right">95.8%</td>
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
<td align="right">6,000</td>
<td align="right">0.3%</td>
<td align="right">93.5%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,944</td>
<td align="right">0.2%</td>
<td align="right">2,738</td>
<td align="right">0.1%</td>
<td align="right">40.8%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">601,803</td>
<td align="right">61.0%</td>
<td align="right">801,111</td>
<td align="right">41.5%</td>
<td align="right">33.1%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">8,970,142,752</td>
<td align="right"></td>
<td align="right">7,111,088,579</td>
<td align="right"></td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">272,638,339,375</td>
<td align="right">3,039.4%</td>
<td align="right">223,974,770,857</td>
<td align="right">3,149.7%</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">8,271</td>
<td align="right">4.8%</td>
<td align="right">7,508</td>
<td align="right">0.7%</td>
<td align="right">-9.2%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">813,396</td>
<td align="right">82.5%</td>
<td align="right">884,094</td>
<td align="right">45.8%</td>
<td align="right">8.7%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
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
<td align="right">160,444</td>
<td align="right">94.0%</td>
<td align="right">1,020,541</td>
<td align="right">97.8%</td>
<td align="right">536.1%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">170,596</td>
<td align="right"></td>
<td align="right">1,043,515</td>
<td align="right"></td>
<td align="right">511.7%</td>
</tr>
<tr>
<td align="left">
Remove globals incorrect keys
<details>
<summary>ⓘ</summary>

The keys in the globals dictionary aren't what was expected
</details>
</td>
<td align="right">2,615</td>
<td align="right">1.5%</td>
<td align="right">2,583</td>
<td align="right">0.2%</td>
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
<td align="right">3,642</td>
<td align="right">2.1%</td>
<td align="right">8,561</td>
<td align="right">0.8%</td>
<td align="right">135.1%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">22,587</td>
<td align="right">13.2%</td>
<td align="right">107,409</td>
<td align="right">10.3%</td>
<td align="right">375.5%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">20,432</td>
<td align="right">12.0%</td>
<td align="right">87,421</td>
<td align="right">8.4%</td>
<td align="right">327.9%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">47,359</td>
<td align="right">27.8%</td>
<td align="right">410,266</td>
<td align="right">39.3%</td>
<td align="right">766.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">39,040</td>
<td align="right">22.9%</td>
<td align="right">289,495</td>
<td align="right">27.7%</td>
<td align="right">641.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">22,718</td>
<td align="right">13.3%</td>
<td align="right">109,037</td>
<td align="right">10.4%</td>
<td align="right">380.0%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">12,938</td>
<td align="right">7.6%</td>
<td align="right">28,566</td>
<td align="right">2.7%</td>
<td align="right">120.8%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">1,660</td>
<td align="right">1.0%</td>
<td align="right">2,540</td>
<td align="right">0.2%</td>
<td align="right">53.0%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">220</td>
<td align="right">0.1%</td>
<td align="right">220</td>
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
<td align="right">20</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left"><= 4</td>
<td align="right">19,966</td>
<td align="right">11.7%</td>
<td align="right">60,761</td>
<td align="right">5.8%</td>
<td align="right">204.3%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">16,986</td>
<td align="right">10.0%</td>
<td align="right">92,705</td>
<td align="right">8.9%</td>
<td align="right">445.8%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">34,074</td>
<td align="right">20.0%</td>
<td align="right">241,006</td>
<td align="right">23.1%</td>
<td align="right">607.3%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">46,613</td>
<td align="right">27.3%</td>
<td align="right">415,746</td>
<td align="right">39.8%</td>
<td align="right">791.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">26,135</td>
<td align="right">15.3%</td>
<td align="right">158,239</td>
<td align="right">15.2%</td>
<td align="right">505.5%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">12,890</td>
<td align="right">7.6%</td>
<td align="right">46,624</td>
<td align="right">4.5%</td>
<td align="right">261.7%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">3,340</td>
<td align="right">2.0%</td>
<td align="right">5,020</td>
<td align="right">0.5%</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">420</td>
<td align="right">0.2%</td>
<td align="right">420</td>
<td align="right">0.0%</td>
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
<td align="right">960,378,667</td>
<td align="right">186,478,707</td>
<td align="right">-80.6%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">3,018,060</td>
<td align="right">752,540</td>
<td align="right">-75.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL</td>
<td align="right">27,412,380</td>
<td align="right">47,418,880</td>
<td align="right">73.0%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,343,625,211</td>
<td align="right">415,813,161</td>
<td align="right">-69.1%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,469,918,688</td>
<td align="right">540,646,978</td>
<td align="right">-63.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">555,615,440</td>
<td align="right">223,975,054</td>
<td align="right">-59.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,713,343,013</td>
<td align="right">785,938,697</td>
<td align="right">-54.1%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">916,035,892</td>
<td align="right">440,916,912</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">4,580,340</td>
<td align="right">2,305,340</td>
<td align="right">-49.7%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">673,686,512</td>
<td align="right">361,629,577</td>
<td align="right">-46.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">5,604,534,152</td>
<td align="right">3,030,578,675</td>
<td align="right">-45.9%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">901,892,880</td>
<td align="right">510,653,456</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">5,179,026,804</td>
<td align="right">2,953,728,745</td>
<td align="right">-43.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">3,032,708,980</td>
<td align="right">1,738,001,147</td>
<td align="right">-42.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">2,341,239,987</td>
<td align="right">1,373,342,456</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">41,966,421</td>
<td align="right">24,626,011</td>
<td align="right">-41.3%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">603,927,319</td>
<td align="right">355,673,246</td>
<td align="right">-41.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,606,131,738</td>
<td align="right">964,620,542</td>
<td align="right">-39.9%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">4,708,194,646</td>
<td align="right">2,899,102,811</td>
<td align="right">-38.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,684,093,376</td>
<td align="right">2,304,508,148</td>
<td align="right">-37.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,547,633,991</td>
<td align="right">1,616,922,398</td>
<td align="right">-36.5%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">941,909,916</td>
<td align="right">600,004,916</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">55,944,314</td>
<td align="right">35,659,136</td>
<td align="right">-36.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">2,055,611,319</td>
<td align="right">1,327,387,788</td>
<td align="right">-35.4%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">2,700,900</td>
<td align="right">1,808,320</td>
<td align="right">-33.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,348,201,306</td>
<td align="right">1,592,337,450</td>
<td align="right">-32.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">3,446,154,132</td>
<td align="right">2,450,010,241</td>
<td align="right">-28.9%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">874,031,865</td>
<td align="right">624,903,284</td>
<td align="right">-28.5%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,864,247,756</td>
<td align="right">1,343,721,003</td>
<td align="right">-27.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">1,127,113,400</td>
<td align="right">821,742,894</td>
<td align="right">-27.1%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,362,110,684</td>
<td align="right">1,726,398,630</td>
<td align="right">-26.9%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">1,940,339,614</td>
<td align="right">1,422,504,714</td>
<td align="right">-26.7%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">14,340,557,986</td>
<td align="right">10,543,263,675</td>
<td align="right">-26.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,983,869,529</td>
<td align="right">7,440,404,797</td>
<td align="right">-25.5%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,762,757,259</td>
<td align="right">2,849,792,674</td>
<td align="right">-24.3%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">8,038,886,609</td>
<td align="right">6,264,484,805</td>
<td align="right">-22.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">229,602,424</td>
<td align="right">179,539,407</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">4,301,100,219</td>
<td align="right">3,364,765,460</td>
<td align="right">-21.8%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">8,970,142,752</td>
<td align="right">7,111,088,579</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">15,063,380,043</td>
<td align="right">11,942,807,157</td>
<td align="right">-20.7%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,459,348,662</td>
<td align="right">3,554,828,536</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">6,941,520</td>
<td align="right">5,553,900</td>
<td align="right">-20.0%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">18,675,624,926</td>
<td align="right">15,024,866,951</td>
<td align="right">-19.5%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">96,211,500</td>
<td align="right">78,440,080</td>
<td align="right">-18.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">95,372,160</td>
<td align="right">78,153,440</td>
<td align="right">-18.1%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,831,966,473</td>
<td align="right">2,321,116,070</td>
<td align="right">-18.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">112,417,347</td>
<td align="right">132,554,995</td>
<td align="right">17.9%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">142,256,722</td>
<td align="right">116,981,083</td>
<td align="right">-17.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,438,711,808</td>
<td align="right">1,191,224,796</td>
<td align="right">-17.2%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">7,778,947,282</td>
<td align="right">6,466,459,976</td>
<td align="right">-16.9%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">9,682,758,920</td>
<td align="right">8,101,740,274</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">55,420,408</td>
<td align="right">46,386,194</td>
<td align="right">-16.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">1,138,846,487</td>
<td align="right">957,963,127</td>
<td align="right">-15.9%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,884,860</td>
<td align="right">1,598,780</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">416,217,664</td>
<td align="right">355,893,371</td>
<td align="right">-14.5%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">2,006,858,509</td>
<td align="right">1,718,223,972</td>
<td align="right">-14.4%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">657,116,458</td>
<td align="right">569,803,585</td>
<td align="right">-13.3%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">26,737,387</td>
<td align="right">24,014,350</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">653,655,939</td>
<td align="right">590,672,093</td>
<td align="right">-9.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">206,367,985</td>
<td align="right">189,750,254</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">887,065,647</td>
<td align="right">817,901,903</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">234,963,224</td>
<td align="right">216,654,175</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">868,525,147</td>
<td align="right">804,479,346</td>
<td align="right">-7.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">1,994,660</td>
<td align="right">1,850,920</td>
<td align="right">-7.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">375,891,339</td>
<td align="right">350,343,870</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">246,012,115</td>
<td align="right">229,339,324</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">6,151,177,536</td>
<td align="right">5,747,096,496</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">1,439,036,398</td>
<td align="right">1,344,619,908</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">107,116,707</td>
<td align="right">100,170,995</td>
<td align="right">-6.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">936,178</td>
<td align="right">876,843</td>
<td align="right">-6.3%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">187,062,980</td>
<td align="right">175,443,741</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">239,591,585</td>
<td align="right">225,327,501</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">213,581,482</td>
<td align="right">200,992,964</td>
<td align="right">-5.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">12,945,005</td>
<td align="right">13,696,235</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">210,377,802</td>
<td align="right">222,429,502</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">208,784,453</td>
<td align="right">197,286,822</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">6,562,803</td>
<td align="right">6,209,885</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">365,566</td>
<td align="right">346,082</td>
<td align="right">-5.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">63,394,193</td>
<td align="right">60,128,917</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">2,304,961,446</td>
<td align="right">2,195,664,421</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">6,786,682</td>
<td align="right">6,465,292</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,034,046,059</td>
<td align="right">986,820,625</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">2,200,012,879</td>
<td align="right">2,099,834,039</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">2,000,167,820</td>
<td align="right">1,910,810,893</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">280,278,994</td>
<td align="right">268,155,465</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">1,045,916,555</td>
<td align="right">1,001,052,346</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">67,032,262</td>
<td align="right">64,323,762</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">614,476</td>
<td align="right">589,765</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">35,172,854</td>
<td align="right">33,789,322</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">467,084,544</td>
<td align="right">449,256,383</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">197,060,986</td>
<td align="right">189,841,826</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,895,093,568</td>
<td align="right">2,789,985,688</td>
<td align="right">-3.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">134,168,911</td>
<td align="right">129,626,452</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">3,485,844,571</td>
<td align="right">3,372,501,058</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">122,707,320</td>
<td align="right">118,922,427</td>
<td align="right">-3.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">1,081,826,507</td>
<td align="right">1,049,070,084</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">154,889,180</td>
<td align="right">150,285,600</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">10,061,272</td>
<td align="right">9,772,865</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">879,126,534</td>
<td align="right">854,043,891</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">60,617,212</td>
<td align="right">58,917,252</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">2,081,160</td>
<td align="right">2,023,380</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">7,551,923,610</td>
<td align="right">7,346,799,442</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">1,076,760,976</td>
<td align="right">1,048,358,677</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">1,577,985,509</td>
<td align="right">1,538,379,346</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">65,101,560</td>
<td align="right">63,472,220</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">528,445,078</td>
<td align="right">515,377,385</td>
<td align="right">-2.5%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">534,876,407</td>
<td align="right">521,928,273</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">7,643,549,513</td>
<td align="right">7,470,610,192</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">75,458,516</td>
<td align="right">73,752,503</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">559,022,360</td>
<td align="right">547,012,640</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,941,126,914</td>
<td align="right">1,899,782,281</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,563,194,130</td>
<td align="right">1,529,907,384</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">856,223,278</td>
<td align="right">838,145,465</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">438,495,328</td>
<td align="right">429,340,005</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">706,945,690</td>
<td align="right">692,191,053</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,543,394,670</td>
<td align="right">1,512,101,804</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">568,883,639</td>
<td align="right">557,551,447</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">340,266,057</td>
<td align="right">346,934,855</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">256,828,519</td>
<td align="right">261,592,247</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">160,798,295</td>
<td align="right">157,816,370</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,945,858,723</td>
<td align="right">1,911,252,451</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">3,183,929,422</td>
<td align="right">3,128,091,040</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">3,144,932,842</td>
<td align="right">3,089,842,460</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">54,303,667</td>
<td align="right">53,377,456</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">54,299,427</td>
<td align="right">53,373,896</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">1,096,877,240</td>
<td align="right">1,078,877,420</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,328,839,760</td>
<td align="right">1,307,678,384</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">3,787,734</td>
<td align="right">3,729,334</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">825,143,634</td>
<td align="right">812,635,330</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">27,709,509</td>
<td align="right">27,291,301</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">689,299,658</td>
<td align="right">679,537,195</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">390,660,418</td>
<td align="right">385,193,533</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">111,840,420</td>
<td align="right">110,279,920</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">159,953,635</td>
<td align="right">157,819,595</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">978,403,196</td>
<td align="right">965,793,004</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,420,220,990</td>
<td align="right">1,402,828,044</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">163,200,460</td>
<td align="right">161,215,376</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">235,278,437</td>
<td align="right">232,522,275</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">532,738,646</td>
<td align="right">526,646,566</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,330,584</td>
<td align="right">8,241,744</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">990,828,251</td>
<td align="right">980,340,892</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">1,303,794</td>
<td align="right">1,290,734</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,703,298,778</td>
<td align="right">3,666,855,428</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">497,872,591</td>
<td align="right">493,356,650</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">499,099,851</td>
<td align="right">494,583,470</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">13,287,962</td>
<td align="right">13,168,059</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">13,287,962</td>
<td align="right">13,168,059</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">32,318,060</td>
<td align="right">32,607,900</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">11,624</td>
<td align="right">11,724</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">732,860,396</td>
<td align="right">726,808,561</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">779,308,678</td>
<td align="right">773,201,817</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">780,666,438</td>
<td align="right">774,559,577</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">3,600,227,802</td>
<td align="right">3,572,536,391</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,246,483,598</td>
<td align="right">1,237,128,534</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">986,146,965</td>
<td align="right">979,073,719</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">239,659,585</td>
<td align="right">238,037,790</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">107,884,360</td>
<td align="right">108,551,320</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">125,419,220</td>
<td align="right">124,706,200</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">281,242,619</td>
<td align="right">279,744,447</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">85,708,668</td>
<td align="right">85,299,311</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">5,577,440</td>
<td align="right">5,550,980</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">787,754,793</td>
<td align="right">784,439,400</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">325,720,450</td>
<td align="right">324,506,557</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">100,762,746</td>
<td align="right">100,430,647</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,259,202</td>
<td align="right">4,247,686</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">9,438,442</td>
<td align="right">9,416,024</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">114,971,110</td>
<td align="right">115,240,055</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">78,882,368</td>
<td align="right">78,711,398</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">308,196,052</td>
<td align="right">307,562,769</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">5,472,892</td>
<td align="right">5,461,760</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">94,589,940</td>
<td align="right">94,405,090</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,820,972,043</td>
<td align="right">1,817,464,373</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">204,639,420</td>
<td align="right">204,318,080</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,233,954,890</td>
<td align="right">2,230,777,608</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">106,076,519</td>
<td align="right">105,951,109</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">68,226,680</td>
<td align="right">68,148,269</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">37,843,920</td>
<td align="right">37,801,920</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">39,091,147</td>
<td align="right">39,055,454</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">90,309,833</td>
<td align="right">90,241,677</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">393,967,002</td>
<td align="right">393,686,402</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">167,924,929</td>
<td align="right">167,813,080</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">97,381,324</td>
<td align="right">97,318,298</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">102,819,368</td>
<td align="right">102,762,729</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,824</td>
<td align="right">103,760,376</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">103,816,824</td>
<td align="right">103,760,376</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">97,138,332</td>
<td align="right">97,085,982</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">57,780,080</td>
<td align="right">57,752,140</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE</td>
<td align="right">127,819,165</td>
<td align="right">127,757,870</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">162,266,847</td>
<td align="right">162,192,841</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">518,102,262</td>
<td align="right">517,900,046</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">97,089,012</td>
<td align="right">97,051,442</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION</td>
<td align="right">46,625,940</td>
<td align="right">46,608,880</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">532,632,540</td>
<td align="right">532,474,740</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,660,859,608</td>
<td align="right">1,660,465,533</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,331,860,514</td>
<td align="right">1,331,761,486</td>
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
<td align="right">81,007,604</td>
<td align="right">81,003,200</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">32,436,601</td>
<td align="right">32,436,098</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">350,232,020</td>
<td align="right">350,229,860</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">603,439,955</td>
<td align="right">603,437,792</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">228,488,364</td>
<td align="right">228,487,604</td>
<td align="right">-0.0%</td>
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
<td align="right">1,824,880</td>
<td align="right">1,824,880</td>
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
<td align="right">590,140</td>
<td align="right">590,140</td>
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
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">11,121</td>
<td align="right">57,322</td>
<td align="right">415.4%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">36,304</td>
<td align="right">86,206</td>
<td align="right">137.5%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">126,404</td>
<td align="right">55,396</td>
<td align="right">-56.2%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">43,515</td>
<td align="right">61,728</td>
<td align="right">41.9%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">920</td>
<td align="right">1,280</td>
<td align="right">39.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">34,260</td>
<td align="right">42,680</td>
<td align="right">24.6%</td>
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
<td align="right">1,148</td>
<td align="right">1,174</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">1,148</td>
<td align="right">1,174</td>
<td align="right">2.3%</td>
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
Stats gathered on: 2024-08-14
