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
<td align="right">335</td>
<td align="right">2,752</td>
<td align="right">721.5%</td>
</tr>
<tr>
<td align="left">UNPACK_EX</td>
<td align="right">219,440</td>
<td align="right">735,220</td>
<td align="right">235.0%</td>
</tr>
<tr>
<td align="left">CONVERT_VALUE</td>
<td align="right">35,294,004</td>
<td align="right">72,950,530</td>
<td align="right">106.7%</td>
</tr>
<tr>
<td align="left">BUILD_STRING</td>
<td align="right">20,056,701</td>
<td align="right">40,098,619</td>
<td align="right">99.9%</td>
</tr>
<tr>
<td align="left">FORMAT_SIMPLE</td>
<td align="right">40,163,578</td>
<td align="right">78,968,191</td>
<td align="right">96.6%</td>
</tr>
<tr>
<td align="left">UNARY_NOT</td>
<td align="right">5,747,703</td>
<td align="right">11,071,976</td>
<td align="right">92.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD</td>
<td align="right">37,474,386</td>
<td align="right">69,394,766</td>
<td align="right">85.2%</td>
</tr>
<tr>
<td align="left">CALL_TYPE_1</td>
<td align="right">50,942,095</td>
<td align="right">90,906,375</td>
<td align="right">78.5%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TUPLE</td>
<td align="right">129,827,756</td>
<td align="right">200,950,099</td>
<td align="right">54.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS</td>
<td align="right">91,290,950</td>
<td align="right">131,405,665</td>
<td align="right">43.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">38,328,283</td>
<td align="right">21,704,177</td>
<td align="right">-43.4%</td>
</tr>
<tr>
<td align="left">DELETE_FAST</td>
<td align="right">338,524</td>
<td align="right">474,632</td>
<td align="right">40.2%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST</td>
<td align="right">219,957,179</td>
<td align="right">306,181,534</td>
<td align="right">39.2%</td>
</tr>
<tr>
<td align="left">SET_ADD</td>
<td align="right">42,351</td>
<td align="right">58,883</td>
<td align="right">39.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_O</td>
<td align="right">239,058,209</td>
<td align="right">322,721,069</td>
<td align="right">35.0%</td>
</tr>
<tr>
<td align="left">IS_OP</td>
<td align="right">162,117,261</td>
<td align="right">207,689,787</td>
<td align="right">28.1%</td>
</tr>
<tr>
<td align="left">TO_BOOL</td>
<td align="right">123,689,658</td>
<td align="right">89,641,716</td>
<td align="right">-27.5%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_SET</td>
<td align="right">179,071,800</td>
<td align="right">221,365,974</td>
<td align="right">23.6%</td>
</tr>
<tr>
<td align="left">COPY</td>
<td align="right">215,821,316</td>
<td align="right">264,829,654</td>
<td align="right">22.7%</td>
</tr>
<tr>
<td align="left">STORE_SLICE</td>
<td align="right">214,906</td>
<td align="right">261,205</td>
<td align="right">21.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">111,026,979</td>
<td align="right">88,281,112</td>
<td align="right">-20.5%</td>
</tr>
<tr>
<td align="left">UNARY_INVERT</td>
<td align="right">1,535,784</td>
<td align="right">1,838,049</td>
<td align="right">19.7%</td>
</tr>
<tr>
<td align="left">TO_BOOL_STR</td>
<td align="right">24,205,869</td>
<td align="right">28,811,703</td>
<td align="right">19.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_BUILTIN</td>
<td align="right">1,287,843,928</td>
<td align="right">1,524,746,694</td>
<td align="right">18.4%</td>
</tr>
<tr>
<td align="left">TO_BOOL_BOOL</td>
<td align="right">1,546,061,240</td>
<td align="right">1,801,967,657</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">45,366,704</td>
<td align="right">52,470,272</td>
<td align="right">15.7%</td>
</tr>
<tr>
<td align="left">EXTENDED_ARG</td>
<td align="right">37,932,184</td>
<td align="right">43,569,833</td>
<td align="right">14.9%</td>
</tr>
<tr>
<td align="left">FOR_ITER_RANGE</td>
<td align="right">35,237,141</td>
<td align="right">40,145,819</td>
<td align="right">13.9%</td>
</tr>
<tr>
<td align="left">TO_BOOL_ALWAYS_TRUE</td>
<td align="right">79,891,348</td>
<td align="right">69,030,306</td>
<td align="right">-13.6%</td>
</tr>
<tr>
<td align="left">BUILD_TUPLE</td>
<td align="right">347,020,248</td>
<td align="right">393,990,976</td>
<td align="right">13.5%</td>
</tr>
<tr>
<td align="left">LOAD_BUILD_CLASS</td>
<td align="right">3,468</td>
<td align="right">3,930</td>
<td align="right">13.3%</td>
</tr>
<tr>
<td align="left">CALL_LEN</td>
<td align="right">181,453,754</td>
<td align="right">159,923,758</td>
<td align="right">-11.9%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE</td>
<td align="right">583,070</td>
<td align="right">651,321</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,391,051</td>
<td align="right">81,859,927</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">STORE_FAST_LOAD_FAST</td>
<td align="right">14,001,212</td>
<td align="right">15,604,032</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_CHECK</td>
<td align="right">3,320,614</td>
<td align="right">3,697,161</td>
<td align="right">11.3%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_TRUE</td>
<td align="right">642,004,710</td>
<td align="right">710,476,215</td>
<td align="right">10.7%</td>
</tr>
<tr>
<td align="left">IMPORT_NAME</td>
<td align="right">7,094,808</td>
<td align="right">7,848,358</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">CALL_TUPLE_1</td>
<td align="right">7,545,083</td>
<td align="right">8,332,312</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">STORE_FAST</td>
<td align="right">3,387,543,441</td>
<td align="right">3,699,711,637</td>
<td align="right">9.2%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_FALSE</td>
<td align="right">2,767,379,162</td>
<td align="right">3,018,959,817</td>
<td align="right">9.1%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP</td>
<td align="right">34,026,768</td>
<td align="right">37,044,100</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,575,023</td>
<td align="right">393,660,074</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">STORE_NAME</td>
<td align="right">53,390</td>
<td align="right">57,657</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,046,646,771</td>
<td align="right">1,127,386,728</td>
<td align="right">7.7%</td>
</tr>
<tr>
<td align="left">PUSH_NULL</td>
<td align="right">575,531,112</td>
<td align="right">618,074,468</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">DICT_MERGE</td>
<td align="right">26,282,786</td>
<td align="right">28,065,659</td>
<td align="right">6.8%</td>
</tr>
<tr>
<td align="left">TO_BOOL_INT</td>
<td align="right">44,197,909</td>
<td align="right">47,155,452</td>
<td align="right">6.7%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_DICT</td>
<td align="right">103,915,574</td>
<td align="right">96,978,648</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">496,185,044</td>
<td align="right">463,541,522</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">1,487,142,463</td>
<td align="right">1,581,409,753</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">LOAD_CONST</td>
<td align="right">362,636,216</td>
<td align="right">384,902,427</td>
<td align="right">6.1%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_DICT</td>
<td align="right">260,176,554</td>
<td align="right">244,526,244</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">LOAD_CONST_IMMORTAL</td>
<td align="right">2,485,505,017</td>
<td align="right">2,630,399,795</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_LIST_INT</td>
<td align="right">154,139,158</td>
<td align="right">162,985,639</td>
<td align="right">5.7%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NONE</td>
<td align="right">120,052,390</td>
<td align="right">126,703,041</td>
<td align="right">5.5%</td>
</tr>
<tr>
<td align="left">FOR_ITER_LIST</td>
<td align="right">173,117,564</td>
<td align="right">182,507,948</td>
<td align="right">5.4%</td>
</tr>
<tr>
<td align="left">LIST_APPEND</td>
<td align="right">43,413,965</td>
<td align="right">45,726,578</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">TO_BOOL_LIST</td>
<td align="right">24,216,584</td>
<td align="right">25,503,735</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_LIST</td>
<td align="right">1,177,330</td>
<td align="right">1,238,498</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">BUILD_SET</td>
<td align="right">734,418</td>
<td align="right">772,384</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">2,270,343</td>
<td align="right">2,384,739</td>
<td align="right">5.0%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_CLASS</td>
<td align="right">97,066,455</td>
<td align="right">92,230,986</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">LOAD_FAST</td>
<td align="right">11,884,242,794</td>
<td align="right">12,462,406,741</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_WITH_HINT</td>
<td align="right">59,826,727</td>
<td align="right">62,587,402</td>
<td align="right">4.6%</td>
</tr>
<tr>
<td align="left">CONTAINS_OP_DICT</td>
<td align="right">93,862,238</td>
<td align="right">98,107,129</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_GENERAL</td>
<td align="right">3,623,183</td>
<td align="right">3,778,165</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">592,531,080</td>
<td align="right">617,808,201</td>
<td align="right">4.3%</td>
</tr>
<tr>
<td align="left">BUILD_MAP</td>
<td align="right">76,047,310</td>
<td align="right">79,166,494</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">796,285,899</td>
<td align="right">828,766,993</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_LOAD_FAST</td>
<td align="right">2,810,433,098</td>
<td align="right">2,920,000,571</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">IMPORT_FROM</td>
<td align="right">7,859,812</td>
<td align="right">8,164,627</td>
<td align="right">3.9%</td>
</tr>
<tr>
<td align="left">CALL_KW_BOUND_METHOD</td>
<td align="right">170,760</td>
<td align="right">177,232</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">155,849,218</td>
<td align="right">150,062,809</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">JUMP_FORWARD</td>
<td align="right">149,928,129</td>
<td align="right">144,376,292</td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">187,123,094</td>
<td align="right">194,004,024</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_METHOD</td>
<td align="right">50,755,586</td>
<td align="right">52,583,618</td>
<td align="right">3.6%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">107,786,394</td>
<td align="right">111,532,311</td>
<td align="right">3.5%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL_MODULE</td>
<td align="right">1,945,979,536</td>
<td align="right">2,011,353,771</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">RERAISE</td>
<td align="right">2,691,848</td>
<td align="right">2,601,556</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">POP_TOP</td>
<td align="right">2,222,000,445</td>
<td align="right">2,294,353,715</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">CALL_PY_GENERAL</td>
<td align="right">195,965,426</td>
<td align="right">202,330,354</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">54,960,466</td>
<td align="right">56,735,677</td>
<td align="right">3.2%</td>
</tr>
<tr>
<td align="left">LOAD_SPECIAL</td>
<td align="right">12,602,934</td>
<td align="right">12,983,290</td>
<td align="right">3.0%</td>
</tr>
<tr>
<td align="left">MAKE_FUNCTION</td>
<td align="right">40,203,062</td>
<td align="right">41,376,690</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">292,449,570</td>
<td align="right">300,951,048</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">RESUME_CHECK</td>
<td align="right">3,548,705,901</td>
<td align="right">3,649,386,840</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">26,521,219</td>
<td align="right">27,267,930</td>
<td align="right">2.8%</td>
</tr>
<tr>
<td align="left">STORE_FAST_STORE_FAST</td>
<td align="right">260,028,117</td>
<td align="right">266,849,466</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_STR_INT</td>
<td align="right">253,778,444</td>
<td align="right">260,400,457</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">CALL_KW_PY</td>
<td align="right">58,223,874</td>
<td align="right">59,666,387</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,955,472</td>
<td align="right">79,872,570</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">145,890,274</td>
<td align="right">149,426,900</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">FOR_ITER_TUPLE</td>
<td align="right">106,880,779</td>
<td align="right">109,356,343</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">RETURN_VALUE</td>
<td align="right">4,316,230,630</td>
<td align="right">4,414,613,327</td>
<td align="right">2.3%</td>
</tr>
<tr>
<td align="left">CALL_KW_NON_PY</td>
<td align="right">45,764,952</td>
<td align="right">46,750,715</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">LOAD_FAST_AND_CLEAR</td>
<td align="right">42,817,746</td>
<td align="right">43,727,910</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">UNARY_NEGATIVE</td>
<td align="right">45,717,061</td>
<td align="right">46,686,964</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR_LIST_INT</td>
<td align="right">43,384,562</td>
<td align="right">44,284,136</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">CALL_NON_PY_GENERAL</td>
<td align="right">448,764,751</td>
<td align="right">457,965,174</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">414,572,470</td>
<td align="right">423,025,119</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">TO_BOOL_NONE</td>
<td align="right">273,394,956</td>
<td align="right">278,910,274</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_INT</td>
<td align="right">270,478,713</td>
<td align="right">275,838,304</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_STR</td>
<td align="right">218,041,307</td>
<td align="right">222,271,707</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">POP_JUMP_IF_NOT_NONE</td>
<td align="right">318,654,447</td>
<td align="right">312,765,909</td>
<td align="right">-1.8%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_MODULE</td>
<td align="right">350,659,952</td>
<td align="right">357,005,837</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">SWAP</td>
<td align="right">219,587,416</td>
<td align="right">223,225,108</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">CALL_LIST_APPEND</td>
<td align="right">168,709,531</td>
<td align="right">171,398,304</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">GET_YIELD_FROM_ITER</td>
<td align="right">10,045,834</td>
<td align="right">9,885,965</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">MAKE_CELL</td>
<td align="right">63,501,771</td>
<td align="right">64,509,571</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">JUMP_BACKWARD_NO_INTERRUPT</td>
<td align="right">54,080,176</td>
<td align="right">54,875,513</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">LOAD_DEREF</td>
<td align="right">483,891,278</td>
<td align="right">490,228,248</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">791,985,835</td>
<td align="right">802,200,515</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_FLOAT</td>
<td align="right">109,671,501</td>
<td align="right">111,070,974</td>
<td align="right">1.3%</td>
</tr>
<tr>
<td align="left">ENTER_EXECUTOR</td>
<td align="right">2,022,385,143</td>
<td align="right">1,997,537,679</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">NOP</td>
<td align="right">602,906,669</td>
<td align="right">610,207,404</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">28,555,125</td>
<td align="right">28,897,841</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">COPY_FREE_VARS</td>
<td align="right">253,726,186</td>
<td align="right">256,706,604</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">CALL_ISINSTANCE</td>
<td align="right">470,129,735</td>
<td align="right">475,425,531</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">STORE_DEREF</td>
<td align="right">66,494,450</td>
<td align="right">67,111,992</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">GET_ITER</td>
<td align="right">511,910,129</td>
<td align="right">516,449,437</td>
<td align="right">0.9%</td>
</tr>
<tr>
<td align="left">LIST_EXTEND</td>
<td align="right">17,178,343</td>
<td align="right">17,321,942</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">144,611,871</td>
<td align="right">145,795,306</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">85,700,685</td>
<td align="right">86,345,566</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">MAP_ADD</td>
<td align="right">25,444,938</td>
<td align="right">25,634,890</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_INT</td>
<td align="right">413,286,164</td>
<td align="right">416,312,870</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_CLASS_WITH_METACLASS_CHECK</td>
<td align="right">10,024,552</td>
<td align="right">10,092,713</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">FOR_ITER_GEN</td>
<td align="right">106,580,372</td>
<td align="right">105,857,794</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">CALL_STR_1</td>
<td align="right">22,952,787</td>
<td align="right">23,106,338</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">CALL_ALLOC_AND_ENTER_INIT</td>
<td align="right">47,910,264</td>
<td align="right">48,172,163</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_WITH_HINT</td>
<td align="right">8,920,184</td>
<td align="right">8,966,968</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_INT</td>
<td align="right">94,193,012</td>
<td align="right">94,658,990</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">SET_FUNCTION_ATTRIBUTE</td>
<td align="right">32,978,515</td>
<td align="right">33,141,173</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">RETURN_GENERATOR</td>
<td align="right">341,234,023</td>
<td align="right">342,746,274</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">LOAD_SMALL_INT</td>
<td align="right">1,499,531,330</td>
<td align="right">1,493,030,108</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">DELETE_SUBSCR</td>
<td align="right">32,646,359</td>
<td align="right">32,781,760</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">SEND_GEN</td>
<td align="right">203,059,373</td>
<td align="right">203,856,392</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">BUILD_LIST</td>
<td align="right">129,936,079</td>
<td align="right">129,521,090</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">LOAD_NAME</td>
<td align="right">4,851,079</td>
<td align="right">4,865,831</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">183,665,753</td>
<td align="right">184,187,360</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR_GETITEM</td>
<td align="right">112,222,311</td>
<td align="right">111,905,768</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">82,406,467</td>
<td align="right">82,626,443</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">BINARY_OP_ADD_UNICODE</td>
<td align="right">26,645,165</td>
<td align="right">26,712,244</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_INT</td>
<td align="right">584,660,230</td>
<td align="right">586,048,360</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,207,077</td>
<td align="right">86,379,025</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">RESUME</td>
<td align="right">17,648</td>
<td align="right">17,621</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">149,637,429</td>
<td align="right">149,819,450</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">DELETE_ATTR</td>
<td align="right">1,623,213</td>
<td align="right">1,625,118</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">COMPARE_OP_FLOAT</td>
<td align="right">113,796,888</td>
<td align="right">113,914,009</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">152,251,333</td>
<td align="right">152,388,692</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">BUILD_SLICE</td>
<td align="right">31,861,376</td>
<td align="right">31,887,076</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,851,004</td>
<td align="right">53,884,023</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">INTERPRETER_EXIT</td>
<td align="right">1,782,131,039</td>
<td align="right">1,783,199,073</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">1,999,511,263</td>
<td align="right">1,998,347,317</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">CALL_INTRINSIC_1</td>
<td align="right">111,092,599</td>
<td align="right">111,042,704</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR</td>
<td align="right">2,635</td>
<td align="right">2,634</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">334,437</td>
<td align="right">334,335</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">EXIT_INIT_CHECK</td>
<td align="right">74,546,801</td>
<td align="right">74,552,866</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">YIELD_VALUE</td>
<td align="right">1,071,984,106</td>
<td align="right">1,072,054,153</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_KW</td>
<td align="right">116,597</td>
<td align="right">116,602</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">GET_AWAITABLE</td>
<td align="right">168,156,024</td>
<td align="right">168,161,842</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_SUPER_ATTR_ATTR</td>
<td align="right">2,981,290</td>
<td align="right">2,981,232</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">POP_EXCEPT</td>
<td align="right">16,651,680</td>
<td align="right">16,651,511</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">4,395,673</td>
<td align="right">4,395,631</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">END_FOR</td>
<td align="right">100,818,555</td>
<td align="right">100,817,604</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">LOAD_GLOBAL</td>
<td align="right">14,684,754</td>
<td align="right">14,684,659</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">CHECK_EXC_MATCH</td>
<td align="right">16,322,115</td>
<td align="right">16,322,188</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">PUSH_EXC_INFO</td>
<td align="right">16,652,470</td>
<td align="right">16,652,543</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">END_SEND</td>
<td align="right">302,606,993</td>
<td align="right">302,606,993</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,851,971</td>
<td align="right">128,851,971</td>
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
<td align="left">STORE_GLOBAL</td>
<td align="right">2,597,144</td>
<td align="right">2,597,144</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CLEANUP_THROW</td>
<td align="right">98,780</td>
<td align="right">98,780</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">SET_UPDATE</td>
<td align="right">84,554</td>
<td align="right">84,554</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN</td>
<td align="right">56,138</td>
<td align="right">56,138</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">DICT_UPDATE</td>
<td align="right">17,551</td>
<td align="right">17,551</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">WITH_EXCEPT_START</td>
<td align="right">5,320</td>
<td align="right">5,320</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">LOAD_LOCALS</td>
<td align="right">3,624</td>
<td align="right">3,624</td>
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
<td align="right">169</td>
<td align="right">169</td>
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
<td align="right">30</td>
<td align="right">30</td>
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
<td align="right">291,701,670</td>
<td align="right">3.8%</td>
<td align="right">300,187,441</td>
<td align="right">3.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">21,326,700</td>
<td align="right">0.3%</td>
<td align="right">21,772,775</td>
<td align="right">0.3%</td>
<td align="right">2.1%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">7,371,506,478</td>
<td align="right">95.9%</td>
<td align="right">7,370,631,763</td>
<td align="right">95.8%</td>
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
<td align="right">741,836</td>
<td align="right">100.0%</td>
<td align="right">757,612</td>
<td align="right">100.0%</td>
<td align="right">2.1%</td>
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
<td align="right">1,049</td>
<td align="right">0.1%</td>
<td align="right">1,364</td>
<td align="right">0.2%</td>
<td align="right">30.0%</td>
</tr>
<tr>
<td align="left">add different types</td>
<td align="right">34,580</td>
<td align="right">4.7%</td>
<td align="right">42,933</td>
<td align="right">5.7%</td>
<td align="right">24.2%</td>
</tr>
<tr>
<td align="left">and int</td>
<td align="right">7,366</td>
<td align="right">1.0%</td>
<td align="right">8,603</td>
<td align="right">1.1%</td>
<td align="right">16.8%</td>
</tr>
<tr>
<td align="left">multiply different types</td>
<td align="right">34,143</td>
<td align="right">4.6%</td>
<td align="right">38,540</td>
<td align="right">5.1%</td>
<td align="right">12.9%</td>
</tr>
<tr>
<td align="left">true divide float</td>
<td align="right">1,122</td>
<td align="right">0.2%</td>
<td align="right">1,023</td>
<td align="right">0.1%</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">xor</td>
<td align="right">2,749</td>
<td align="right">0.4%</td>
<td align="right">2,517</td>
<td align="right">0.3%</td>
<td align="right">-8.4%</td>
</tr>
<tr>
<td align="left">multiply other</td>
<td align="right">737</td>
<td align="right">0.1%</td>
<td align="right">775</td>
<td align="right">0.1%</td>
<td align="right">5.2%</td>
</tr>
<tr>
<td align="left">rshift</td>
<td align="right">2,828</td>
<td align="right">0.4%</td>
<td align="right">2,973</td>
<td align="right">0.4%</td>
<td align="right">5.1%</td>
</tr>
<tr>
<td align="left">or</td>
<td align="right">5,697</td>
<td align="right">0.8%</td>
<td align="right">5,906</td>
<td align="right">0.8%</td>
<td align="right">3.7%</td>
</tr>
<tr>
<td align="left">remainder</td>
<td align="right">9,664</td>
<td align="right">1.3%</td>
<td align="right">9,994</td>
<td align="right">1.3%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">floor divide</td>
<td align="right">19,037</td>
<td align="right">2.6%</td>
<td align="right">19,633</td>
<td align="right">2.6%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">true divide different types</td>
<td align="right">5,787</td>
<td align="right">0.8%</td>
<td align="right">5,967</td>
<td align="right">0.8%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">lshift</td>
<td align="right">4,183</td>
<td align="right">0.6%</td>
<td align="right">4,252</td>
<td align="right">0.6%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">subtract other</td>
<td align="right">4,576</td>
<td align="right">0.6%</td>
<td align="right">4,623</td>
<td align="right">0.6%</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">and other</td>
<td align="right">497</td>
<td align="right">0.1%</td>
<td align="right">494</td>
<td align="right">0.1%</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">power</td>
<td align="right">2,330</td>
<td align="right">0.3%</td>
<td align="right">2,343</td>
<td align="right">0.3%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">add other</td>
<td align="right">22,105</td>
<td align="right">3.0%</td>
<td align="right">22,019</td>
<td align="right">2.9%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">subtract different types</td>
<td align="right">583,303</td>
<td align="right">78.6%</td>
<td align="right">583,570</td>
<td align="right">77.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">and different types</td>
<td align="right">83</td>
<td align="right">0.0%</td>
<td align="right">83</td>
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
<td align="right">85,700,685</td>
<td align="right">100.0%</td>
<td align="right">86,345,566</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
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
<td align="right">428,432,597</td>
<td align="right">7.3%</td>
<td align="right">393,526,576</td>
<td align="right">6.7%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">5,755,517</td>
<td align="right">0.1%</td>
<td align="right">5,760,442</td>
<td align="right">0.1%</td>
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
<td align="right">5,457,034,611</td>
<td align="right">92.6%</td>
<td align="right">5,457,127,873</td>
<td align="right">93.2%</td>
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
<td align="right">134,497</td>
<td align="right">53.6%</td>
<td align="right">125,570</td>
<td align="right">51.9%</td>
<td align="right">-6.6%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">116,313</td>
<td align="right">46.4%</td>
<td align="right">116,416</td>
<td align="right">48.1%</td>
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
<td align="left">buffer int</td>
<td align="right">9,799</td>
<td align="right">7.3%</td>
<td align="right">2,546</td>
<td align="right">2.0%</td>
<td align="right">-74.0%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">36,512</td>
<td align="right">27.1%</td>
<td align="right">34,473</td>
<td align="right">27.5%</td>
<td align="right">-5.6%</td>
</tr>
<tr>
<td align="left">buffer slice</td>
<td align="right">767</td>
<td align="right">0.6%</td>
<td align="right">729</td>
<td align="right">0.6%</td>
<td align="right">-5.0%</td>
</tr>
<tr>
<td align="left">tuple slice</td>
<td align="right">12,355</td>
<td align="right">9.2%</td>
<td align="right">12,439</td>
<td align="right">9.9%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">45,797</td>
<td align="right">34.1%</td>
<td align="right">46,029</td>
<td align="right">36.7%</td>
<td align="right">0.5%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">4,759</td>
<td align="right">3.5%</td>
<td align="right">4,779</td>
<td align="right">3.8%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">18,032</td>
<td align="right">13.4%</td>
<td align="right">18,104</td>
<td align="right">14.4%</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">string slice</td>
<td align="right">3,442</td>
<td align="right">2.6%</td>
<td align="right">3,437</td>
<td align="right">2.7%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">sequence int</td>
<td align="right">2,941</td>
<td align="right">2.2%</td>
<td align="right">2,941</td>
<td align="right">2.3%</td>
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
deopt
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">18,828</td>
<td align="right">0.0%</td>
<td align="right">22,186</td>
<td align="right">0.0%</td>
<td align="right">17.8%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">119,104,912</td>
<td align="right">1.1%</td>
<td align="right">118,732,183</td>
<td align="right">1.1%</td>
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
<td align="right">10,827,420,461</td>
<td align="right">98.9%</td>
<td align="right">10,839,352,915</td>
<td align="right">98.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">193,026</td>
<td align="right">0.0%</td>
<td align="right">192,968</td>
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
<td align="right">2,404,026</td>
<td align="right">100.0%</td>
<td align="right">2,398,217</td>
<td align="right">100.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">569</td>
<td align="right">0.0%</td>
<td align="right">569</td>
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
<td align="right">750</td>
<td align="right">131.8%</td>
<td align="right">750</td>
<td align="right">131.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">out of versions</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">569</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not inline values</td>
<td align="right">385</td>
<td align="right">67.7%</td>
<td align="right">385</td>
<td align="right">67.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">init not python</td>
<td align="right">287</td>
<td align="right">50.4%</td>
<td align="right">287</td>
<td align="right">50.4%</td>
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
<td align="right">533,904</td>
<td align="right">82.1%</td>
<td align="right">591,605</td>
<td align="right">83.5%</td>
<td align="right">10.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">109,472</td>
<td align="right">16.8%</td>
<td align="right">109,470</td>
<td align="right">15.5%</td>
<td align="right">-0.0%</td>
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
<td align="right">860,673</td>
<td align="right">0.0%</td>
<td align="right">942,645</td>
<td align="right">0.0%</td>
<td align="right">9.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">77,868,425</td>
<td align="right">1.7%</td>
<td align="right">79,780,648</td>
<td align="right">1.7%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,507,661,380</td>
<td align="right">98.3%</td>
<td align="right">4,508,175,311</td>
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
<td align="left">Success</td>
<td align="right">23,845</td>
<td align="right">23.1%</td>
<td align="right">25,347</td>
<td align="right">23.1%</td>
<td align="right">6.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">79,310</td>
<td align="right">76.9%</td>
<td align="right">84,282</td>
<td align="right">76.9%</td>
<td align="right">6.3%</td>
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
<td align="left">different types</td>
<td align="right">22,552</td>
<td align="right">28.4%</td>
<td align="right">25,136</td>
<td align="right">29.8%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">974</td>
<td align="right">1.2%</td>
<td align="right">1,077</td>
<td align="right">1.3%</td>
<td align="right">10.6%</td>
</tr>
<tr>
<td align="left">big int</td>
<td align="right">21,008</td>
<td align="right">26.5%</td>
<td align="right">22,697</td>
<td align="right">26.9%</td>
<td align="right">8.0%</td>
</tr>
<tr>
<td align="left">baseobject</td>
<td align="right">6,196</td>
<td align="right">7.8%</td>
<td align="right">6,409</td>
<td align="right">7.6%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">bool</td>
<td align="right">692</td>
<td align="right">0.9%</td>
<td align="right">672</td>
<td align="right">0.8%</td>
<td align="right">-2.9%</td>
</tr>
<tr>
<td align="left">float long</td>
<td align="right">8,303</td>
<td align="right">10.5%</td>
<td align="right">8,499</td>
<td align="right">10.1%</td>
<td align="right">2.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">3,931</td>
<td align="right">5.0%</td>
<td align="right">4,001</td>
<td align="right">4.7%</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">334</td>
<td align="right">0.4%</td>
<td align="right">339</td>
<td align="right">0.4%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">string</td>
<td align="right">7,554</td>
<td align="right">9.5%</td>
<td align="right">7,639</td>
<td align="right">9.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">6,474</td>
<td align="right">8.2%</td>
<td align="right">6,521</td>
<td align="right">7.7%</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">958</td>
<td align="right">1.2%</td>
<td align="right">958</td>
<td align="right">1.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">long float</td>
<td align="right">334</td>
<td align="right">0.4%</td>
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
<td align="right">33,995,948</td>
<td align="right">1.5%</td>
<td align="right">37,012,571</td>
<td align="right">1.7%</td>
<td align="right">8.9%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">1,916,370</td>
<td align="right">0.1%</td>
<td align="right">1,916,987</td>
<td align="right">0.1%</td>
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
<td align="right">2,178,612,557</td>
<td align="right">98.4%</td>
<td align="right">2,178,925,927</td>
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
<td align="right">28,574</td>
<td align="right">100.0%</td>
<td align="right">29,283</td>
<td align="right">100.0%</td>
<td align="right">2.5%</td>
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
<td align="left">str</td>
<td align="right">6,378</td>
<td align="right">22.3%</td>
<td align="right">6,820</td>
<td align="right">23.3%</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">list</td>
<td align="right">4,838</td>
<td align="right">16.9%</td>
<td align="right">5,004</td>
<td align="right">17.1%</td>
<td align="right">3.4%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">10,208</td>
<td align="right">35.7%</td>
<td align="right">10,292</td>
<td align="right">35.1%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">7,150</td>
<td align="right">25.0%</td>
<td align="right">7,167</td>
<td align="right">24.5%</td>
<td align="right">0.2%</td>
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
<td align="right">73,346,954</td>
<td align="right">12.3%</td>
<td align="right">81,806,036</td>
<td align="right">13.1%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">25,167,537</td>
<td align="right">4.2%</td>
<td align="right">23,978,152</td>
<td align="right">3.8%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">499,374,818</td>
<td align="right">83.5%</td>
<td align="right">517,341,056</td>
<td align="right">83.0%</td>
<td align="right">3.6%</td>
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
<td align="right">40,556</td>
<td align="right">7.8%</td>
<td align="right">50,347</td>
<td align="right">9.9%</td>
<td align="right">24.1%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">478,278</td>
<td align="right">92.2%</td>
<td align="right">455,752</td>
<td align="right">90.1%</td>
<td align="right">-4.7%</td>
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
<td align="right">1,338</td>
<td align="right">3.3%</td>
<td align="right">2,513</td>
<td align="right">5.0%</td>
<td align="right">87.8%</td>
</tr>
<tr>
<td align="left">map</td>
<td align="right">130</td>
<td align="right">0.3%</td>
<td align="right">176</td>
<td align="right">0.3%</td>
<td align="right">35.4%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">6,590</td>
<td align="right">16.2%</td>
<td align="right">8,891</td>
<td align="right">17.7%</td>
<td align="right">34.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">55</td>
<td align="right">0.1%</td>
<td align="right">74</td>
<td align="right">0.1%</td>
<td align="right">34.5%</td>
</tr>
<tr>
<td align="left">dict items</td>
<td align="right">13,588</td>
<td align="right">33.5%</td>
<td align="right">17,805</td>
<td align="right">35.4%</td>
<td align="right">31.0%</td>
</tr>
<tr>
<td align="left">callable</td>
<td align="right">69</td>
<td align="right">0.2%</td>
<td align="right">90</td>
<td align="right">0.2%</td>
<td align="right">30.4%</td>
</tr>
<tr>
<td align="left">dict keys</td>
<td align="right">1,860</td>
<td align="right">4.6%</td>
<td align="right">2,218</td>
<td align="right">4.4%</td>
<td align="right">19.2%</td>
</tr>
<tr>
<td align="left">enumerate</td>
<td align="right">3,571</td>
<td align="right">8.8%</td>
<td align="right">4,142</td>
<td align="right">8.2%</td>
<td align="right">16.0%</td>
</tr>
<tr>
<td align="left">reversed list</td>
<td align="right">1,221</td>
<td align="right">3.0%</td>
<td align="right">1,411</td>
<td align="right">2.8%</td>
<td align="right">15.6%</td>
</tr>
<tr>
<td align="left">itertools</td>
<td align="right">2,493</td>
<td align="right">6.1%</td>
<td align="right">2,798</td>
<td align="right">5.6%</td>
<td align="right">12.2%</td>
</tr>
<tr>
<td align="left">ascii string</td>
<td align="right">871</td>
<td align="right">2.1%</td>
<td align="right">778</td>
<td align="right">1.5%</td>
<td align="right">-10.7%</td>
</tr>
<tr>
<td align="left">dict values</td>
<td align="right">3,593</td>
<td align="right">8.9%</td>
<td align="right">3,950</td>
<td align="right">7.8%</td>
<td align="right">9.9%</td>
</tr>
<tr>
<td align="left">zip</td>
<td align="right">3,408</td>
<td align="right">8.4%</td>
<td align="right">3,645</td>
<td align="right">7.2%</td>
<td align="right">7.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">1,769</td>
<td align="right">4.4%</td>
<td align="right">1,856</td>
<td align="right">3.7%</td>
<td align="right">4.9%</td>
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
<td align="right">598,199</td>
<td align="right">0.0%</td>
<td align="right">1,401,103</td>
<td align="right">0.0%</td>
<td align="right">134.2%</td>
</tr>
<tr>
<td align="left">
miss
<details>
<summary>ⓘ</summary>

Specialized instructions that deopt.
</details>
</td>
<td align="right">403,700,126</td>
<td align="right">3.1%</td>
<td align="right">450,293,894</td>
<td align="right">3.5%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">413,280,073</td>
<td align="right">3.2%</td>
<td align="right">421,729,002</td>
<td align="right">3.3%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">12,083,890,530</td>
<td align="right">93.7%</td>
<td align="right">12,096,363,140</td>
<td align="right">93.3%</td>
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
<td align="left">Success</td>
<td align="right">8,698,547</td>
<td align="right">97.7%</td>
<td align="right">9,578,748</td>
<td align="right">97.9%</td>
<td align="right">10.1%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">201,654</td>
<td align="right">2.3%</td>
<td align="right">204,290</td>
<td align="right">2.1%</td>
<td align="right">1.3%</td>
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
<td align="right">361</td>
<td align="right">0.2%</td>
<td align="right">421</td>
<td align="right">0.2%</td>
<td align="right">16.6%</td>
</tr>
<tr>
<td align="left">module attr not found</td>
<td align="right">1,073</td>
<td align="right">0.5%</td>
<td align="right">997</td>
<td align="right">0.5%</td>
<td align="right">-7.1%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">1,480</td>
<td align="right">0.7%</td>
<td align="right">1,414</td>
<td align="right">0.7%</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">builtin class method</td>
<td align="right">858</td>
<td align="right">0.4%</td>
<td align="right">821</td>
<td align="right">0.4%</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">non overriding descriptor</td>
<td align="right">4,680</td>
<td align="right">2.3%</td>
<td align="right">4,859</td>
<td align="right">2.4%</td>
<td align="right">3.8%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">56,170</td>
<td align="right">27.9%</td>
<td align="right">57,575</td>
<td align="right">28.2%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">class method obj</td>
<td align="right">13,971</td>
<td align="right">6.9%</td>
<td align="right">14,208</td>
<td align="right">7.0%</td>
<td align="right">1.7%</td>
</tr>
<tr>
<td align="left">expected error</td>
<td align="right">2,406</td>
<td align="right">1.2%</td>
<td align="right">2,370</td>
<td align="right">1.2%</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">metaclass attribute</td>
<td align="right">19,340</td>
<td align="right">9.6%</td>
<td align="right">19,623</td>
<td align="right">9.6%</td>
<td align="right">1.5%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">1,106</td>
<td align="right">0.5%</td>
<td align="right">1,092</td>
<td align="right">0.5%</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">overriding descriptor</td>
<td align="right">35,706</td>
<td align="right">17.7%</td>
<td align="right">36,094</td>
<td align="right">17.7%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">39,810</td>
<td align="right">19.7%</td>
<td align="right">40,064</td>
<td align="right">19.6%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">8,297</td>
<td align="right">4.1%</td>
<td align="right">8,253</td>
<td align="right">4.0%</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,235</td>
<td align="right">0.6%</td>
<td align="right">1,239</td>
<td align="right">0.6%</td>
<td align="right">0.3%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,541</td>
<td align="right">3.7%</td>
<td align="right">7,522</td>
<td align="right">3.7%</td>
<td align="right">-0.3%</td>
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
<td align="right">140</td>
<td align="right">0.1%</td>
<td align="right">140</td>
<td align="right">0.1%</td>
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
<td align="right">3,376,866,955</td>
<td align="right">99.6%</td>
<td align="right">3,675,677,047</td>
<td align="right">99.6%</td>
<td align="right">8.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">14,584,181</td>
<td align="right">0.4%</td>
<td align="right">14,584,108</td>
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
<td align="right">1,453</td>
<td align="right">0.0%</td>
<td align="right">1,453</td>
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
<td align="right">31,835</td>
<td align="right">0.0%</td>
<td align="right">31,835</td>
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
<td align="right">101,283</td>
<td align="right">100.0%</td>
<td align="right">101,261</td>
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
<td align="right">62,551,650</td>
<td align="right">100.0%</td>
<td align="right">63,039,492</td>
<td align="right">100.0%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">216</td>
<td align="right">0.0%</td>
<td align="right">215</td>
<td align="right">0.0%</td>
<td align="right">-0.5%</td>
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
<td align="right">2,419</td>
<td align="right">100.0%</td>
<td align="right">2,419</td>
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
<td align="right">593,287,030</td>
<td align="right">82.2%</td>
<td align="right">593,287,049</td>
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
<td align="right">128,817,179</td>
<td align="right">17.8%</td>
<td align="right">128,817,179</td>
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
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">652</td>
<td align="right">1.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">34,412</td>
<td align="right">98.1%</td>
<td align="right">34,412</td>
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
<td align="right">71.0%</td>
<td align="right">24,440</td>
<td align="right">71.0%</td>
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
<td align="right">752</td>
<td align="right">2.2%</td>
<td align="right">752</td>
<td align="right">2.2%</td>
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
<td align="right">104,015,449</td>
<td align="right">5.2%</td>
<td align="right">95,742,244</td>
<td align="right">4.8%</td>
<td align="right">-8.0%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">1,840,612,043</td>
<td align="right">92.1%</td>
<td align="right">1,851,981,300</td>
<td align="right">92.5%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">53,780,450</td>
<td align="right">2.7%</td>
<td align="right">53,813,246</td>
<td align="right">2.7%</td>
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
<td align="left">Success</td>
<td align="right">1,992,393</td>
<td align="right">98.0%</td>
<td align="right">1,836,329</td>
<td align="right">97.9%</td>
<td align="right">-7.8%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">40,070</td>
<td align="right">2.0%</td>
<td align="right">40,300</td>
<td align="right">2.1%</td>
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
<td align="left">overriding descriptor</td>
<td align="right">4,634</td>
<td align="right">11.6%</td>
<td align="right">4,756</td>
<td align="right">11.8%</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">not in dict</td>
<td align="right">7,467</td>
<td align="right">18.6%</td>
<td align="right">7,587</td>
<td align="right">18.8%</td>
<td align="right">1.6%</td>
</tr>
<tr>
<td align="left">overridden</td>
<td align="right">1,756</td>
<td align="right">4.4%</td>
<td align="right">1,766</td>
<td align="right">4.4%</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">class attr simple</td>
<td align="right">19,820</td>
<td align="right">49.5%</td>
<td align="right">19,796</td>
<td align="right">49.1%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">not managed dict</td>
<td align="right">1,915</td>
<td align="right">4.8%</td>
<td align="right">1,917</td>
<td align="right">4.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">property</td>
<td align="right">1,619</td>
<td align="right">4.0%</td>
<td align="right">1,619</td>
<td align="right">4.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">not in keys</td>
<td align="right">860</td>
<td align="right">2.1%</td>
<td align="right">860</td>
<td align="right">2.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">mutable class</td>
<td align="right">731</td>
<td align="right">1.8%</td>
<td align="right">731</td>
<td align="right">1.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">method</td>
<td align="right">699</td>
<td align="right">1.7%</td>
<td align="right">699</td>
<td align="right">1.7%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">split dict</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">365</td>
<td align="right">0.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">no dict</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">110</td>
<td align="right">0.3%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">non object slot</td>
<td align="right">94</td>
<td align="right">0.2%</td>
<td align="right">94</td>
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
<td align="right">214,906</td>
<td align="right">100.0%</td>
<td align="right">261,205</td>
<td align="right">100.0%</td>
<td align="right">21.5%</td>
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
<td align="right">86,172,709</td>
<td align="right">8.6%</td>
<td align="right">86,344,665</td>
<td align="right">8.6%</td>
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
<td align="right">916,873,311</td>
<td align="right">91.4%</td>
<td align="right">917,183,864</td>
<td align="right">91.4%</td>
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
<td align="left">Success</td>
<td align="right">2,143</td>
<td align="right">6.2%</td>
<td align="right">2,136</td>
<td align="right">6.2%</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">32,265</td>
<td align="right">93.8%</td>
<td align="right">32,264</td>
<td align="right">93.8%</td>
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
<td align="left">array slice</td>
<td align="right">24</td>
<td align="right">0.1%</td>
<td align="right">68</td>
<td align="right">0.2%</td>
<td align="right">183.3%</td>
</tr>
<tr>
<td align="left">bytearray int</td>
<td align="right">185</td>
<td align="right">0.6%</td>
<td align="right">156</td>
<td align="right">0.5%</td>
<td align="right">-15.7%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">209</td>
<td align="right">0.6%</td>
<td align="right">216</td>
<td align="right">0.7%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">dict subclass no override</td>
<td align="right">3,058</td>
<td align="right">9.5%</td>
<td align="right">2,999</td>
<td align="right">9.3%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">list slice</td>
<td align="right">2,934</td>
<td align="right">9.1%</td>
<td align="right">2,894</td>
<td align="right">9.0%</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">array int</td>
<td align="right">8,633</td>
<td align="right">26.8%</td>
<td align="right">8,729</td>
<td align="right">27.1%</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">py simple</td>
<td align="right">16,722</td>
<td align="right">51.8%</td>
<td align="right">16,702</td>
<td align="right">51.8%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">out of range</td>
<td align="right">500</td>
<td align="right">1.5%</td>
<td align="right">500</td>
<td align="right">1.5%</td>
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
<td align="right">21,382,250</td>
<td align="right">0.5%</td>
<td align="right">28,884,144</td>
<td align="right">0.6%</td>
<td align="right">35.1%</td>
</tr>
<tr>
<td align="left">
deferred
<details>
<summary>ⓘ</summary>

Lists the number of "deferred" (i.e. not specialized) instructions executed.
</details>
</td>
<td align="right">123,423,415</td>
<td align="right">2.6%</td>
<td align="right">89,383,697</td>
<td align="right">1.9%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">
hit
<details>
<summary>ⓘ</summary>

Specialized instructions that complete.
</details>
</td>
<td align="right">4,534,567,956</td>
<td align="right">96.9%</td>
<td align="right">4,512,831,647</td>
<td align="right">97.4%</td>
<td align="right">-0.5%</td>
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
<td align="right">436,523</td>
<td align="right">65.3%</td>
<td align="right">578,119</td>
<td align="right">72.1%</td>
<td align="right">32.4%</td>
</tr>
<tr>
<td align="left">Failure</td>
<td align="right">231,954</td>
<td align="right">34.7%</td>
<td align="right">223,657</td>
<td align="right">27.9%</td>
<td align="right">-3.6%</td>
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
<td align="right">182</td>
<td align="right">0.1%</td>
<td align="right">382</td>
<td align="right">0.2%</td>
<td align="right">109.9%</td>
</tr>
<tr>
<td align="left">bytes</td>
<td align="right">9,958</td>
<td align="right">4.3%</td>
<td align="right">978</td>
<td align="right">0.4%</td>
<td align="right">-90.2%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">9,161</td>
<td align="right">3.9%</td>
<td align="right">10,407</td>
<td align="right">4.7%</td>
<td align="right">13.6%</td>
</tr>
<tr>
<td align="left">tuple</td>
<td align="right">72,360</td>
<td align="right">31.2%</td>
<td align="right">78,486</td>
<td align="right">35.1%</td>
<td align="right">8.5%</td>
</tr>
<tr>
<td align="left">sequence</td>
<td align="right">3,384</td>
<td align="right">1.5%</td>
<td align="right">3,648</td>
<td align="right">1.6%</td>
<td align="right">7.8%</td>
</tr>
<tr>
<td align="left">number</td>
<td align="right">105,802</td>
<td align="right">45.6%</td>
<td align="right">98,679</td>
<td align="right">44.1%</td>
<td align="right">-6.7%</td>
</tr>
<tr>
<td align="left">dict</td>
<td align="right">12,755</td>
<td align="right">5.5%</td>
<td align="right">13,174</td>
<td align="right">5.9%</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">set</td>
<td align="right">10,288</td>
<td align="right">4.4%</td>
<td align="right">9,978</td>
<td align="right">4.5%</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">mapping</td>
<td align="right">8,024</td>
<td align="right">3.5%</td>
<td align="right">7,885</td>
<td align="right">3.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">memory view</td>
<td align="right">40</td>
<td align="right">0.0%</td>
<td align="right">40</td>
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
<td align="right">575,175</td>
<td align="right">0.0%</td>
<td align="right">643,407</td>
<td align="right">0.1%</td>
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
<td align="right">1,230,249,210</td>
<td align="right">100.0%</td>
<td align="right">1,230,489,594</td>
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
<td align="right">647</td>
<td align="right">8.1%</td>
<td align="right">674</td>
<td align="right">8.4%</td>
<td align="right">4.2%</td>
</tr>
<tr>
<td align="left">Success</td>
<td align="right">7,328</td>
<td align="right">91.9%</td>
<td align="right">7,320</td>
<td align="right">91.6%</td>
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
<td align="right">420</td>
<td align="right">64.9%</td>
<td align="right">447</td>
<td align="right">66.3%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">iterator</td>
<td align="right">136</td>
<td align="right">21.0%</td>
<td align="right">136</td>
<td align="right">20.2%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">other</td>
<td align="right">91</td>
<td align="right">14.1%</td>
<td align="right">91</td>
<td align="right">13.5%</td>
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
<td align="right">703,983,631</td>
<td align="right">1.0%</td>
<td align="right">748,851,178</td>
<td align="right">1.0%</td>
<td align="right">6.4%</td>
</tr>
<tr>
<td align="left">
Specialized hits
<details>
<summary>ⓘ</summary>

Specialized instructions, e.g. `LOAD_ATTR_MODULE` that complete.
</details>
</td>
<td align="right">25,850,263,984</td>
<td align="right">37.0%</td>
<td align="right">27,209,112,745</td>
<td align="right">37.3%</td>
<td align="right">5.3%</td>
</tr>
<tr>
<td align="left">
Basic
<details>
<summary>ⓘ</summary>

Instructions that are not and cannot be specialized, e.g. `LOAD_FAST`.
</details>
</td>
<td align="right">41,404,062,671</td>
<td align="right">59.3%</td>
<td align="right">43,255,855,376</td>
<td align="right">59.3%</td>
<td align="right">4.5%</td>
</tr>
<tr>
<td align="left">
Not specialized
<details>
<summary>ⓘ</summary>

Instructions that could be specialized but aren't, e.g. `LOAD_ATTR`, `BINARY_SLICE`.
</details>
</td>
<td align="right">1,815,207,148</td>
<td align="right">2.6%</td>
<td align="right">1,777,565,895</td>
<td align="right">2.4%</td>
<td align="right">-2.1%</td>
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
<td align="left">TO_BOOL</td>
<td align="right">123,423,415</td>
<td align="right">6.8%</td>
<td align="right">89,383,697</td>
<td align="right">5.0%</td>
<td align="right">-27.6%</td>
</tr>
<tr>
<td align="left">FOR_ITER</td>
<td align="right">73,346,954</td>
<td align="right">4.0%</td>
<td align="right">81,806,036</td>
<td align="right">4.6%</td>
<td align="right">11.5%</td>
</tr>
<tr>
<td align="left">BINARY_SUBSCR</td>
<td align="right">428,432,597</td>
<td align="right">23.6%</td>
<td align="right">393,526,576</td>
<td align="right">22.2%</td>
<td align="right">-8.1%</td>
</tr>
<tr>
<td align="left">BINARY_OP</td>
<td align="right">291,701,670</td>
<td align="right">16.1%</td>
<td align="right">300,187,441</td>
<td align="right">16.9%</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">COMPARE_OP</td>
<td align="right">77,868,425</td>
<td align="right">4.3%</td>
<td align="right">79,780,648</td>
<td align="right">4.5%</td>
<td align="right">2.5%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR</td>
<td align="right">413,280,073</td>
<td align="right">22.8%</td>
<td align="right">421,729,002</td>
<td align="right">23.8%</td>
<td align="right">2.0%</td>
</tr>
<tr>
<td align="left">BINARY_SLICE</td>
<td align="right">85,700,685</td>
<td align="right">4.7%</td>
<td align="right">86,345,566</td>
<td align="right">4.9%</td>
<td align="right">0.8%</td>
</tr>
<tr>
<td align="left">STORE_SUBSCR</td>
<td align="right">86,172,709</td>
<td align="right">4.8%</td>
<td align="right">86,344,665</td>
<td align="right">4.9%</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">STORE_ATTR</td>
<td align="right">53,780,450</td>
<td align="right">3.0%</td>
<td align="right">53,813,246</td>
<td align="right">3.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">128,817,179</td>
<td align="right">7.1%</td>
<td align="right">128,817,179</td>
<td align="right">7.3%</td>
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
<td align="right">102,186,231</td>
<td align="right">14.5%</td>
<td align="right">123,651,239</td>
<td align="right">16.5%</td>
<td align="right">21.0%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">86,943,407</td>
<td align="right">12.3%</td>
<td align="right">76,657,584</td>
<td align="right">10.2%</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">STORE_ATTR_SLOT</td>
<td align="right">17,050,354</td>
<td align="right">2.4%</td>
<td align="right">19,050,342</td>
<td align="right">2.5%</td>
<td align="right">11.7%</td>
</tr>
<tr>
<td align="left">CALL_PY_EXACT_ARGS</td>
<td align="right">56,063,883</td>
<td align="right">8.0%</td>
<td align="right">62,288,047</td>
<td align="right">8.3%</td>
<td align="right">11.1%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_SLOT</td>
<td align="right">47,403,858</td>
<td align="right">6.7%</td>
<td align="right">52,582,095</td>
<td align="right">7.0%</td>
<td align="right">10.9%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_INSTANCE_VALUE</td>
<td align="right">156,085,664</td>
<td align="right">22.2%</td>
<td align="right">172,255,980</td>
<td align="right">23.0%</td>
<td align="right">10.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_PROPERTY</td>
<td align="right">16,505,974</td>
<td align="right">2.3%</td>
<td align="right">15,618,593</td>
<td align="right">2.1%</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">59,401,560</td>
<td align="right">8.4%</td>
<td align="right">60,982,926</td>
<td align="right">8.1%</td>
<td align="right">2.7%</td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">20,872,673</td>
<td align="right">3.0%</td>
<td align="right">20,872,701</td>
<td align="right">2.8%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">18,379,948</td>
<td align="right">2.6%</td>
<td align="right"></td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right"></td>
<td align="right"></td>
<td align="right">15,568,045</td>
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
<td align="right">69,246,086</td>
<td align="right">1.0%</td>
<td align="right">69,125,977</td>
<td align="right">1.0%</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (api)</td>
<td align="right">278,750,657</td>
<td align="right">4.2%</td>
<td align="right">279,090,795</td>
<td align="right">4.2%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function vectorcall)</td>
<td align="right">1,114,052,817</td>
<td align="right">16.7%</td>
<td align="right">1,115,051,109</td>
<td align="right">16.7%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (vector)</td>
<td align="right">1,116,185,023</td>
<td align="right">16.8%</td>
<td align="right">1,117,183,315</td>
<td align="right">16.8%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Frames pushed</td>
<td align="right">5,255,248,891</td>
<td align="right">79.0%</td>
<td align="right">5,259,801,305</td>
<td align="right">79.0%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to Python functions inlined</td>
<td align="right">4,867,096,368</td>
<td align="right">73.1%</td>
<td align="right">4,870,644,325</td>
<td align="right">73.1%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls to PyEval_EvalDefault</td>
<td align="right">1,787,179,752</td>
<td align="right">26.9%</td>
<td align="right">1,788,157,432</td>
<td align="right">26.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (total)</td>
<td align="right">1,787,179,752</td>
<td align="right">26.9%</td>
<td align="right">1,788,157,432</td>
<td align="right">26.9%</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (generator)</td>
<td align="right">670,994,729</td>
<td align="right">10.1%</td>
<td align="right">670,974,117</td>
<td align="right">10.1%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (function ex)</td>
<td align="right">24,900,030</td>
<td align="right">0.4%</td>
<td align="right">24,899,817</td>
<td align="right">0.4%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (slot)</td>
<td align="right">261,407,535</td>
<td align="right">3.9%</td>
<td align="right">261,407,001</td>
<td align="right">3.9%</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (legacy)</td>
<td align="right">2,128,276</td>
<td align="right">0.0%</td>
<td align="right">2,128,276</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (build class)</td>
<td align="right">3,930</td>
<td align="right">0.0%</td>
<td align="right">3,930</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Calls via PyEval_EvalFrame (method)</td>
<td align="right">132,513,137</td>
<td align="right">2.0%</td>
<td align="right">132,513,137</td>
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
<td align="right">7,782,925,298</td>
<td align="right">4.7%</td>
<td align="right">8,667,677,788</td>
<td align="right">5.3%</td>
<td align="right">11.4%</td>
</tr>
<tr>
<td align="left">Method cache dunder misses</td>
<td align="right">7,455,986</td>
<td align="right"></td>
<td align="right">6,610,225</td>
<td align="right"></td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">Method cache collisions</td>
<td align="right">62,399,000</td>
<td align="right"></td>
<td align="right">60,101,799</td>
<td align="right"></td>
<td align="right">-3.7%</td>
</tr>
<tr>
<td align="left">Interpreter immortal decrefs</td>
<td align="right">15,092,096,620</td>
<td align="right">7.5%</td>
<td align="right">15,556,632,528</td>
<td align="right">7.7%</td>
<td align="right">3.1%</td>
</tr>
<tr>
<td align="left">Method cache misses</td>
<td align="right">55,736,158</td>
<td align="right"></td>
<td align="right">54,284,480</td>
<td align="right"></td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">Interpreter mortal increfs</td>
<td align="right">32,277,370,393</td>
<td align="right">19.6%</td>
<td align="right">32,988,935,279</td>
<td align="right">20.1%</td>
<td align="right">2.2%</td>
</tr>
<tr>
<td align="left">Mortal increfs</td>
<td align="right">81,610,728,241</td>
<td align="right">49.4%</td>
<td align="right">80,036,975,234</td>
<td align="right">48.7%</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">Immortal increfs</td>
<td align="right">43,383,363,805</td>
<td align="right">26.3%</td>
<td align="right">42,639,078,450</td>
<td align="right">25.9%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Mortal decrefs</td>
<td align="right">86,906,289,726</td>
<td align="right">43.0%</td>
<td align="right">85,432,736,670</td>
<td align="right">42.5%</td>
<td align="right">-1.7%</td>
</tr>
<tr>
<td align="left">Interpreter mortal decrefs</td>
<td align="right">44,107,548,607</td>
<td align="right">21.8%</td>
<td align="right">44,723,446,221</td>
<td align="right">22.2%</td>
<td align="right">1.4%</td>
</tr>
<tr>
<td align="left">Immortal decrefs</td>
<td align="right">55,994,249,326</td>
<td align="right">27.7%</td>
<td align="right">55,513,544,592</td>
<td align="right">27.6%</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">Method cache hits</td>
<td align="right">1,977,662,929</td>
<td align="right"></td>
<td align="right">1,968,797,543</td>
<td align="right"></td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Allocations to 4 kbytes</td>
<td align="right">71,618,641</td>
<td align="right">0.4%</td>
<td align="right">71,312,660</td>
<td align="right">0.4%</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">Inline values</td>
<td align="right">176,957,682</td>
<td align="right"></td>
<td align="right">177,312,398</td>
<td align="right"></td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">Method cache dunder hits</td>
<td align="right">3,063,816,072</td>
<td align="right"></td>
<td align="right">3,067,884,107</td>
<td align="right"></td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">Allocations over 4 kbytes</td>
<td align="right">6,415,450</td>
<td align="right">0.0%</td>
<td align="right">6,409,618</td>
<td align="right">0.0%</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">Frees to freelist</td>
<td align="right">8,403,879,123</td>
<td align="right"></td>
<td align="right">8,407,761,174</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations from freelist</td>
<td align="right">8,403,708,493</td>
<td align="right">44.9%</td>
<td align="right">8,407,583,710</td>
<td align="right">44.9%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations to 512 bytes</td>
<td align="right">10,223,102,181</td>
<td align="right">54.7%</td>
<td align="right">10,225,099,529</td>
<td align="right">54.6%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Allocations</td>
<td align="right">10,301,136,272</td>
<td align="right">55.1%</td>
<td align="right">10,302,821,807</td>
<td align="right">55.1%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Frees</td>
<td align="right">10,887,115,391</td>
<td align="right"></td>
<td align="right">10,888,776,472</td>
<td align="right"></td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (on request)</td>
<td align="right">4,443,533</td>
<td align="right">2.5%</td>
<td align="right">4,443,533</td>
<td align="right">2.5%</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">Materialize dict (new key)</td>
<td align="right">392,277</td>
<td align="right">0.2%</td>
<td align="right">392,277</td>
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
<td align="right">361,975</td>
<td align="right">101,131,989</td>
<td align="right">18,931,277,722</td>
<td align="right">361,973</td>
<td align="right">100,827,590</td>
<td align="right">18,945,169,533</td>
</tr>
<tr>
<td align="right">2</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,246,203,240</td>
<td align="right">7,998</td>
<td align="right">4,366,437</td>
<td align="right">5,246,185,450</td>
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
Executors invalidated
<details>
<summary>ⓘ</summary>

The number of executors that were invalidated due to watched dictionary changes.
</details>
</td>
<td align="right">3,787</td>
<td align="right">0.5%</td>
<td align="right">1,215</td>
<td align="right">0.3%</td>
<td align="right">-67.9%</td>
</tr>
<tr>
<td align="left">
Traces created
<details>
<summary>ⓘ</summary>

The number of traces that were successfully created.
</details>
</td>
<td align="right">764,996</td>
<td align="right">50.5%</td>
<td align="right">366,695</td>
<td align="right">33.9%</td>
<td align="right">-52.1%</td>
</tr>
<tr>
<td align="left">
Trace stack overflow
<details>
<summary>ⓘ</summary>

A trace is truncated because it would require more than 5 stack frames.
</details>
</td>
<td align="right">1,761</td>
<td align="right">0.1%</td>
<td align="right">847</td>
<td align="right">0.1%</td>
<td align="right">-51.9%</td>
</tr>
<tr>
<td align="left">
Inner loop found
<details>
<summary>ⓘ</summary>

A trace is truncated because it has an inner loop
</details>
</td>
<td align="right">14,849</td>
<td align="right">1.0%</td>
<td align="right">7,303</td>
<td align="right">0.7%</td>
<td align="right">-50.8%</td>
</tr>
<tr>
<td align="left">
Trace too long
<details>
<summary>ⓘ</summary>

A trace is truncated because it is longer than the instruction buffer.
</details>
</td>
<td align="right">240</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">-49.2%</td>
</tr>
<tr>
<td align="left">
Low confidence
<details>
<summary>ⓘ</summary>

A trace is abandoned because the likelihood of the jump to top being taken is too low.
</details>
</td>
<td align="right">7,286</td>
<td align="right">0.5%</td>
<td align="right">4,737</td>
<td align="right">0.4%</td>
<td align="right">-35.0%</td>
</tr>
<tr>
<td align="left">
Optimization attempts
<details>
<summary>ⓘ</summary>

The number of times a potential trace is identified.  Specifically, this occurs in the JUMP BACKWARD instruction when the counter reaches a threshold.
</details>
</td>
<td align="right">1,515,778</td>
<td align="right"></td>
<td align="right">1,081,620</td>
<td align="right"></td>
<td align="right">-28.6%</td>
</tr>
<tr>
<td align="left">
Recursive call
<details>
<summary>ⓘ</summary>

A trace is truncated because it has a recursive call.
</details>
</td>
<td align="right">5,207</td>
<td align="right">0.3%</td>
<td align="right">4,402</td>
<td align="right">0.4%</td>
<td align="right">-15.5%</td>
</tr>
<tr>
<td align="left">
Traces executed
<details>
<summary>ⓘ</summary>

The number of traces that were executed
</details>
</td>
<td align="right">7,701,956,123</td>
<td align="right"></td>
<td align="right">6,831,421,039</td>
<td align="right"></td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">
Trace stack underflow
<details>
<summary>ⓘ</summary>

A potential trace is abandoned because it pops more frames than it pushes.
</details>
</td>
<td align="right">772,514</td>
<td align="right">51.0%</td>
<td align="right">708,406</td>
<td align="right">65.5%</td>
<td align="right">-8.3%</td>
</tr>
<tr>
<td align="left">
Trace too short
<details>
<summary>ⓘ</summary>

A potential trace is abandoced because it it too short.
</details>
</td>
<td align="right">749,021</td>
<td align="right">49.4%</td>
<td align="right">714,078</td>
<td align="right">66.0%</td>
<td align="right">-4.7%</td>
</tr>
<tr>
<td align="left">
Uops executed
<details>
<summary>ⓘ</summary>

The total number of uops (micro-operations) that were executed
</details>
</td>
<td align="right">257,069,721,306</td>
<td align="right">3,337.7%</td>
<td align="right">249,308,843,218</td>
<td align="right">3,649.4%</td>
<td align="right">-3.0%</td>
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
<td align="right">448</td>
<td align="right">0.1%</td>
<td align="right">61</td>
<td align="right">0.0%</td>
<td align="right">-86.4%</td>
</tr>
<tr>
<td align="left">
Optimizer successes
<details>
<summary>ⓘ</summary>

The number of traces that were successfully optimized.
</details>
</td>
<td align="right">732,457</td>
<td align="right">95.7%</td>
<td align="right">340,924</td>
<td align="right">93.0%</td>
<td align="right">-53.5%</td>
</tr>
<tr>
<td align="left">
Optimizer attempts
<details>
<summary>ⓘ</summary>

The number of times the trace optimizer (_Py_uop_analyze_and_optimize) was run.
</details>
</td>
<td align="right">764,996</td>
<td align="right"></td>
<td align="right">366,695</td>
<td align="right"></td>
<td align="right">-52.1%</td>
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
<td align="right">54,406</td>
<td align="right">7.1%</td>
<td align="right">36,781</td>
<td align="right">10.0%</td>
<td align="right">-32.4%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">139,487</td>
<td align="right">18.2%</td>
<td align="right">75,936</td>
<td align="right">20.7%</td>
<td align="right">-45.6%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">265,011</td>
<td align="right">34.6%</td>
<td align="right">121,098</td>
<td align="right">33.0%</td>
<td align="right">-54.3%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">198,304</td>
<td align="right">25.9%</td>
<td align="right">77,268</td>
<td align="right">21.1%</td>
<td align="right">-61.0%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">81,763</td>
<td align="right">10.7%</td>
<td align="right">40,152</td>
<td align="right">10.9%</td>
<td align="right">-50.9%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">22,420</td>
<td align="right">2.9%</td>
<td align="right">12,672</td>
<td align="right">3.5%</td>
<td align="right">-43.5%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">3,345</td>
<td align="right">0.4%</td>
<td align="right">2,666</td>
<td align="right">0.7%</td>
<td align="right">-20.3%</td>
</tr>
<tr>
<td align="left"><= 1,024</td>
<td align="right">260</td>
<td align="right">0.0%</td>
<td align="right">122</td>
<td align="right">0.0%</td>
<td align="right">-53.1%</td>
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
<td align="right">11,058</td>
<td align="right">1.4%</td>
<td align="right">5,899</td>
<td align="right">1.6%</td>
<td align="right">-46.7%</td>
</tr>
<tr>
<td align="left"><= 8</td>
<td align="right">124,485</td>
<td align="right">16.3%</td>
<td align="right">61,888</td>
<td align="right">16.9%</td>
<td align="right">-50.3%</td>
</tr>
<tr>
<td align="left"><= 16</td>
<td align="right">144,055</td>
<td align="right">18.8%</td>
<td align="right">94,298</td>
<td align="right">25.7%</td>
<td align="right">-34.5%</td>
</tr>
<tr>
<td align="left"><= 32</td>
<td align="right">292,566</td>
<td align="right">38.2%</td>
<td align="right">111,491</td>
<td align="right">30.4%</td>
<td align="right">-61.9%</td>
</tr>
<tr>
<td align="left"><= 64</td>
<td align="right">119,682</td>
<td align="right">15.6%</td>
<td align="right">47,361</td>
<td align="right">12.9%</td>
<td align="right">-60.4%</td>
</tr>
<tr>
<td align="left"><= 128</td>
<td align="right">32,575</td>
<td align="right">4.3%</td>
<td align="right">15,224</td>
<td align="right">4.2%</td>
<td align="right">-53.3%</td>
</tr>
<tr>
<td align="left"><= 256</td>
<td align="right">7,165</td>
<td align="right">0.9%</td>
<td align="right">4,179</td>
<td align="right">1.1%</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left"><= 512</td>
<td align="right">871</td>
<td align="right">0.1%</td>
<td align="right">584</td>
<td align="right">0.2%</td>
<td align="right">-33.0%</td>
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
<td align="left">_LOAD_GLOBAL</td>
<td align="right">195,485</td>
<td align="right">1,719,272</td>
<td align="right">779.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_1</td>
<td align="right">949,540</td>
<td align="right">14,019</td>
<td align="right">-98.5%</td>
</tr>
<tr>
<td align="left">_SET_ADD</td>
<td align="right">17,263</td>
<td align="right">731</td>
<td align="right">-95.8%</td>
</tr>
<tr>
<td align="left">_BUILD_SET</td>
<td align="right">40,539</td>
<td align="right">2,441</td>
<td align="right">-94.0%</td>
</tr>
<tr>
<td align="left">_UNPACK_EX</td>
<td align="right">561,580</td>
<td align="right">45,800</td>
<td align="right">-91.8%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_WITH_HINT</td>
<td align="right">56,353</td>
<td align="right">9,807</td>
<td align="right">-82.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_1</td>
<td align="right">36,826,274</td>
<td align="right">61,864,422</td>
<td align="right">68.0%</td>
</tr>
<tr>
<td align="left">_CHECK_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">66,617,022</td>
<td align="right">101,349,712</td>
<td align="right">52.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_BOUND_METHOD_EXACT_ARGS</td>
<td align="right">63,831,683</td>
<td align="right">95,922,945</td>
<td align="right">50.3%</td>
</tr>
<tr>
<td align="left">_BUILD_STRING</td>
<td align="right">40,693,075</td>
<td align="right">20,651,157</td>
<td align="right">-49.3%</td>
</tr>
<tr>
<td align="left">_FORMAT_SIMPLE</td>
<td align="right">80,604,924</td>
<td align="right">41,800,311</td>
<td align="right">-48.1%</td>
</tr>
<tr>
<td align="left">_CONVERT_VALUE</td>
<td align="right">79,450,894</td>
<td align="right">41,794,368</td>
<td align="right">-47.4%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,115</td>
<td align="right">53,244,200</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_LAZY_DICT</td>
<td align="right">36,620,115</td>
<td align="right">53,244,200</td>
<td align="right">45.4%</td>
</tr>
<tr>
<td align="left">_IMPORT_NAME</td>
<td align="right">1,487,110</td>
<td align="right">821,390</td>
<td align="right">-44.8%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_CHECK</td>
<td align="right">652,084</td>
<td align="right">408,596</td>
<td align="right">-37.3%</td>
</tr>
<tr>
<td align="left">_POP_TOP_LOAD_CONST_INLINE_BORROW</td>
<td align="right">1,279,254</td>
<td align="right">822,200</td>
<td align="right">-35.7%</td>
</tr>
<tr>
<td align="left">_TO_BOOL</td>
<td align="right">161,414,497</td>
<td align="right">215,084,025</td>
<td align="right">33.2%</td>
</tr>
<tr>
<td align="left">_MAKE_CELL</td>
<td align="right">3,066,125</td>
<td align="right">2,057,839</td>
<td align="right">-32.9%</td>
</tr>
<tr>
<td align="left">_POP_EXCEPT</td>
<td align="right">766</td>
<td align="right">1,008</td>
<td align="right">31.6%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TUPLE</td>
<td align="right">259,655,852</td>
<td align="right">188,496,176</td>
<td align="right">-27.4%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_NO_DICT</td>
<td align="right">29,976,335</td>
<td align="right">22,892,932</td>
<td align="right">-23.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_PROPERTY_FRAME</td>
<td align="right">11,724,860</td>
<td align="right">8,985,695</td>
<td align="right">-23.4%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_NONE</td>
<td align="right">295,654,416</td>
<td align="right">229,018,234</td>
<td align="right">-22.5%</td>
</tr>
<tr>
<td align="left">_ERROR_POP_N</td>
<td align="right">2,451,668</td>
<td align="right">1,914,223</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_IMPORT_FROM</td>
<td align="right">992,788</td>
<td align="right">775,590</td>
<td align="right">-21.9%</td>
</tr>
<tr>
<td align="left">_DICT_MERGE</td>
<td align="right">9,274,181</td>
<td align="right">7,490,886</td>
<td align="right">-19.2%</td>
</tr>
<tr>
<td align="left">_DEOPT</td>
<td align="right">22,261,341</td>
<td align="right">18,695,366</td>
<td align="right">-16.0%</td>
</tr>
<tr>
<td align="left">_DELETE_FAST</td>
<td align="right">861,028</td>
<td align="right">724,920</td>
<td align="right">-15.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SUPER_ATTR_METHOD</td>
<td align="right">8,814,774</td>
<td align="right">7,474,642</td>
<td align="right">-15.2%</td>
</tr>
<tr>
<td align="left">_IS_OP</td>
<td align="right">302,637,682</td>
<td align="right">257,365,110</td>
<td align="right">-15.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_3</td>
<td align="right">2,885,508</td>
<td align="right">2,481,314</td>
<td align="right">-14.0%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_CLASS</td>
<td align="right">300,497,957</td>
<td align="right">259,286,464</td>
<td align="right">-13.7%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_CLASS_0</td>
<td align="right">296,751,895</td>
<td align="right">257,593,179</td>
<td align="right">-13.2%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR</td>
<td align="right">18,741,203</td>
<td align="right">16,342,317</td>
<td align="right">-12.8%</td>
</tr>
<tr>
<td align="left">_CALL_TYPE_1</td>
<td align="right">314,816,395</td>
<td align="right">274,989,835</td>
<td align="right">-12.7%</td>
</tr>
<tr>
<td align="left">_EXIT_TRACE</td>
<td align="right">6,775,483,264</td>
<td align="right">5,929,652,450</td>
<td align="right">-12.5%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_O</td>
<td align="right">680,806,593</td>
<td align="right">596,830,449</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_BOOL</td>
<td align="right">2,117,760,758</td>
<td align="right">1,857,029,359</td>
<td align="right">-12.3%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS</td>
<td align="right">63,130,200</td>
<td align="right">55,519,800</td>
<td align="right">-12.1%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_2</td>
<td align="right">169,718,478</td>
<td align="right">149,656,382</td>
<td align="right">-11.8%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_4</td>
<td align="right">501,468,435</td>
<td align="right">443,660,347</td>
<td align="right">-11.5%</td>
</tr>
<tr>
<td align="left">_START_EXECUTOR</td>
<td align="right">7,701,956,123</td>
<td align="right">6,831,421,039</td>
<td align="right">-11.3%</td>
</tr>
<tr>
<td align="left">_STORE_DEREF</td>
<td align="right">5,664,988</td>
<td align="right">5,047,240</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_BUILD_MAP</td>
<td align="right">26,775,022</td>
<td align="right">23,863,510</td>
<td align="right">-10.9%</td>
</tr>
<tr>
<td align="left">_RETURN_VALUE</td>
<td align="right">883,653,355</td>
<td align="right">789,817,326</td>
<td align="right">-10.6%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION</td>
<td align="right">3,012,497,639</td>
<td align="right">2,698,256,791</td>
<td align="right">-10.4%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST</td>
<td align="right">833,289,165</td>
<td align="right">747,195,968</td>
<td align="right">-10.3%</td>
</tr>
<tr>
<td align="left">_UNARY_NOT</td>
<td align="right">51,982,513</td>
<td align="right">46,702,465</td>
<td align="right">-10.2%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_STR</td>
<td align="right">52,400,730</td>
<td align="right">47,227,024</td>
<td align="right">-9.9%</td>
</tr>
<tr>
<td align="left">_CALL_TUPLE_1</td>
<td align="right">8,144,570</td>
<td align="right">7,357,313</td>
<td align="right">-9.7%</td>
</tr>
<tr>
<td align="left">_MAKE_WARM</td>
<td align="right">10,094,800,314</td>
<td align="right">9,152,580,091</td>
<td align="right">-9.3%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_TUPLE</td>
<td align="right">508,916,890</td>
<td align="right">463,192,249</td>
<td align="right">-9.0%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR</td>
<td align="right">609,856,632</td>
<td align="right">556,111,877</td>
<td align="right">-8.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_6</td>
<td align="right">527,864,777</td>
<td align="right">483,024,075</td>
<td align="right">-8.5%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION</td>
<td align="right">98,571,405</td>
<td align="right">90,979,370</td>
<td align="right">-7.7%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_CLASS</td>
<td align="right">67,881,582</td>
<td align="right">72,981,145</td>
<td align="right">7.5%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_INSTANCE_VALUE</td>
<td align="right">470,077,592</td>
<td align="right">504,911,727</td>
<td align="right">7.4%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_NO_DICT</td>
<td align="right">473,811,552</td>
<td align="right">508,175,007</td>
<td align="right">7.3%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_INT</td>
<td align="right">311,269,602</td>
<td align="right">332,601,925</td>
<td align="right">6.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_1</td>
<td align="right">2,333,463</td>
<td align="right">2,174,813</td>
<td align="right">-6.8%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_INT</td>
<td align="right">723,233,829</td>
<td align="right">678,651,010</td>
<td align="right">-6.2%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_WITH_HINT</td>
<td align="right">18,250,253</td>
<td align="right">17,128,401</td>
<td align="right">-6.1%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_WITH_HINT</td>
<td align="right">17,853,431</td>
<td align="right">16,779,314</td>
<td align="right">-6.0%</td>
</tr>
<tr>
<td align="left">_REPLACE_WITH_TRUE</td>
<td align="right">118,522,462</td>
<td align="right">125,353,329</td>
<td align="right">5.8%</td>
</tr>
<tr>
<td align="left">_BUILD_TUPLE</td>
<td align="right">812,066,002</td>
<td align="right">765,464,338</td>
<td align="right">-5.7%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE</td>
<td align="right">1,236,543</td>
<td align="right">1,168,173</td>
<td align="right">-5.5%</td>
</tr>
<tr>
<td align="left">_PUSH_NULL</td>
<td align="right">776,172,925</td>
<td align="right">734,057,556</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST</td>
<td align="right">4,409,779,537</td>
<td align="right">4,172,200,247</td>
<td align="right">-5.4%</td>
</tr>
<tr>
<td align="left">_STORE_ATTR_SLOT</td>
<td align="right">177,402,484</td>
<td align="right">168,093,005</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE_OPERAND</td>
<td align="right">832,085,874</td>
<td align="right">788,812,424</td>
<td align="right">-5.2%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES</td>
<td align="right">84,039,679</td>
<td align="right">79,742,156</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TYPE_VERSION</td>
<td align="right">6,105,959,483</td>
<td align="right">5,794,543,844</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_POP_TOP</td>
<td align="right">1,977,976,244</td>
<td align="right">1,877,566,079</td>
<td align="right">-5.1%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW</td>
<td align="right">4,895,697,175</td>
<td align="right">4,654,800,335</td>
<td align="right">-4.9%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_LIST</td>
<td align="right">2,030,218,391</td>
<td align="right">2,129,110,399</td>
<td align="right">4.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_1</td>
<td align="right">570,253,831</td>
<td align="right">597,867,589</td>
<td align="right">4.8%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_GENERAL</td>
<td align="right">121,230,394</td>
<td align="right">115,413,809</td>
<td align="right">-4.8%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_5</td>
<td align="right">923,233,031</td>
<td align="right">880,901,841</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_0</td>
<td align="right">158,697,956</td>
<td align="right">151,443,278</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_BORROW_WITH_NULL</td>
<td align="right">795,042,570</td>
<td align="right">758,838,703</td>
<td align="right">-4.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_6</td>
<td align="right">1,105,782,295</td>
<td align="right">1,055,795,649</td>
<td align="right">-4.5%</td>
</tr>
<tr>
<td align="left">_RESUME_CHECK</td>
<td align="right">1,494,439,194</td>
<td align="right">1,429,891,154</td>
<td align="right">-4.3%</td>
</tr>
<tr>
<td align="left">_SAVE_RETURN_OFFSET</td>
<td align="right">1,917,011,277</td>
<td align="right">1,838,395,435</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_GUARD_TOS_FLOAT</td>
<td align="right">58,355,243</td>
<td align="right">60,742,870</td>
<td align="right">4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_KW</td>
<td align="right">35,451,739</td>
<td align="right">34,005,139</td>
<td align="right">-4.1%</td>
</tr>
<tr>
<td align="left">_CHECK_STACK_SPACE</td>
<td align="right">333,158,130</td>
<td align="right">319,791,514</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_EXACT_ARGS</td>
<td align="right">1,593,193,213</td>
<td align="right">1,529,399,972</td>
<td align="right">-4.0%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE_WITH_NULL</td>
<td align="right">2,870,829,762</td>
<td align="right">2,758,792,791</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_TRUE_POP</td>
<td align="right">3,651,929,933</td>
<td align="right">3,509,704,270</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_PY_FRAME_KW</td>
<td align="right">36,174,943</td>
<td align="right">34,770,969</td>
<td align="right">-3.9%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_0</td>
<td align="right">437,373,094</td>
<td align="right">420,737,631</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_ATTR_MODULE</td>
<td align="right">28,688,574</td>
<td align="right">27,611,530</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_MODULE</td>
<td align="right">28,688,574</td>
<td align="right">27,611,530</td>
<td align="right">-3.8%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION_INLINE</td>
<td align="right">165,823,540</td>
<td align="right">160,046,680</td>
<td align="right">-3.5%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_SLOT_0</td>
<td align="right">805,056,704</td>
<td align="right">777,950,475</td>
<td align="right">-3.4%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NONE_POP</td>
<td align="right">141,717,877</td>
<td align="right">146,429,669</td>
<td align="right">3.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST</td>
<td align="right">9,793,734,395</td>
<td align="right">9,471,489,823</td>
<td align="right">-3.3%</td>
</tr>
<tr>
<td align="left">_GUARD_GLOBALS_VERSION_PUSH_KEYS</td>
<td align="right">107,634,121</td>
<td align="right">104,148,847</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_MODULE_FROM_KEYS</td>
<td align="right">107,634,121</td>
<td align="right">104,148,847</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_INLINE</td>
<td align="right">2,093,139,283</td>
<td align="right">2,025,420,682</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_PUSH_FRAME</td>
<td align="right">2,480,941,401</td>
<td align="right">2,402,307,880</td>
<td align="right">-3.2%</td>
</tr>
<tr>
<td align="left">_LOAD_SPECIAL</td>
<td align="right">840,872</td>
<td align="right">815,372</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_JUMP_TO_TOP</td>
<td align="right">2,392,844,191</td>
<td align="right">2,321,159,052</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_5</td>
<td align="right">4,208,141,864</td>
<td align="right">4,082,181,228</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_FALSE_POP</td>
<td align="right">5,330,001,527</td>
<td align="right">5,172,191,982</td>
<td align="right">-3.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_DICT</td>
<td align="right">247,188,078</td>
<td align="right">254,435,190</td>
<td align="right">2.9%</td>
</tr>
<tr>
<td align="left">_COPY_FREE_VARS</td>
<td align="right">87,783,579</td>
<td align="right">85,295,612</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION</td>
<td align="right">4,016,906</td>
<td align="right">3,903,120</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_DORV_VALUES_INST_ATTR_FROM_DICT</td>
<td align="right">1,395,766,029</td>
<td align="right">1,356,302,730</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_TUPLE_INT</td>
<td align="right">125,777,998</td>
<td align="right">122,241,057</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD</td>
<td align="right">4,015,749</td>
<td align="right">3,903,120</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_GUARD_KEYS_VERSION</td>
<td align="right">1,393,082,193</td>
<td align="right">1,354,295,879</td>
<td align="right">-2.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_INPLACE_ADD_UNICODE</td>
<td align="right">4,181,075</td>
<td align="right">4,066,679</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS_3</td>
<td align="right">61,702,063</td>
<td align="right">60,026,243</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_TIER2_RESUME_CHECK</td>
<td align="right">1,164,649,845</td>
<td align="right">1,133,124,922</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_SET</td>
<td align="right">1,565,660,431</td>
<td align="right">1,523,512,352</td>
<td align="right">-2.7%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_NOARGS</td>
<td align="right">192,484,431</td>
<td align="right">187,394,696</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CALL_KW_NON_PY</td>
<td align="right">37,581,543</td>
<td align="right">36,595,766</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE_KW</td>
<td align="right">37,581,543</td>
<td align="right">36,595,766</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_WITH_VALUES</td>
<td align="right">1,308,518,736</td>
<td align="right">1,274,546,641</td>
<td align="right">-2.6%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST</td>
<td align="right">227,017,410</td>
<td align="right">232,876,075</td>
<td align="right">2.6%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_AND_CLEAR</td>
<td align="right">26,295,657</td>
<td align="right">25,656,524</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT</td>
<td align="right">226,563,425</td>
<td align="right">221,080,549</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP</td>
<td align="right">116,789,045</td>
<td align="right">113,969,380</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_CHECK_FUNCTION_VERSION</td>
<td align="right">1,797,779,888</td>
<td align="right">1,754,627,037</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_COPY</td>
<td align="right">2,007,178,754</td>
<td align="right">1,959,063,883</td>
<td align="right">-2.4%</td>
</tr>
<tr>
<td align="left">_DYNAMIC_EXIT</td>
<td align="right">901,759,854</td>
<td align="right">881,159,000</td>
<td align="right">-2.3%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_2</td>
<td align="right">193,752,921</td>
<td align="right">189,557,119</td>
<td align="right">-2.2%</td>
</tr>
<tr>
<td align="left">_GUARD_IS_NOT_NONE_POP</td>
<td align="right">203,979,994</td>
<td align="right">199,614,502</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">_CHECK_PERIODIC</td>
<td align="right">8,642,134,522</td>
<td align="right">8,467,808,299</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_RETURN_GENERATOR</td>
<td align="right">75,389,257</td>
<td align="right">73,882,373</td>
<td align="right">-2.0%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_DICT</td>
<td align="right">802,841,938</td>
<td align="right">818,491,977</td>
<td align="right">1.9%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_1</td>
<td align="right">6,172,283,513</td>
<td align="right">6,055,278,402</td>
<td align="right">-1.9%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR</td>
<td align="right">1,926,867,426</td>
<td align="right">1,961,894,999</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_0</td>
<td align="right">1,021,262,618</td>
<td align="right">1,039,572,304</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_CALL_LEN</td>
<td align="right">1,218,222,532</td>
<td align="right">1,239,796,735</td>
<td align="right">1.8%</td>
</tr>
<tr>
<td align="left">_MAKE_FUNCTION</td>
<td align="right">75,034,612</td>
<td align="right">73,866,248</td>
<td align="right">-1.6%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_LIST</td>
<td align="right">54,164,525</td>
<td align="right">53,351,964</td>
<td align="right">-1.5%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY</td>
<td align="right">17,627,268,875</td>
<td align="right">17,381,520,841</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CALL_ISINSTANCE</td>
<td align="right">361,005,242</td>
<td align="right">356,018,003</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_CALL_NON_PY_GENERAL</td>
<td align="right">525,215,050</td>
<td align="right">518,003,646</td>
<td align="right">-1.4%</td>
</tr>
<tr>
<td align="left">_SET_IP</td>
<td align="right">21,192,518,787</td>
<td align="right">20,907,683,262</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_CHECK_IS_NOT_PY_CALLABLE</td>
<td align="right">526,091,132</td>
<td align="right">519,251,100</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_METHOD_NO_DICT</td>
<td align="right">1,941,660,199</td>
<td align="right">1,916,564,426</td>
<td align="right">-1.3%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_4</td>
<td align="right">4,697,008,454</td>
<td align="right">4,640,285,054</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_INIT_CALL_PY_EXACT_ARGS</td>
<td align="right">7,365,568</td>
<td align="right">7,277,373</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_0</td>
<td align="right">6,323,603,112</td>
<td align="right">6,248,224,165</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_UNARY_NEGATIVE</td>
<td align="right">81,851,778</td>
<td align="right">80,881,772</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_2</td>
<td align="right">738,381,115</td>
<td align="right">747,013,852</td>
<td align="right">1.2%</td>
</tr>
<tr>
<td align="left">_CONTAINS_OP_DICT</td>
<td align="right">341,960,048</td>
<td align="right">338,001,027</td>
<td align="right">-1.2%</td>
</tr>
<tr>
<td align="left">_CALL_BUILTIN_FAST_WITH_KEYWORDS</td>
<td align="right">66,435,551</td>
<td align="right">65,688,596</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_TWO_TUPLE</td>
<td align="right">591,854,963</td>
<td align="right">585,214,721</td>
<td align="right">-1.1%</td>
</tr>
<tr>
<td align="left">_UNARY_INVERT</td>
<td align="right">9,091,136</td>
<td align="right">9,188,068</td>
<td align="right">1.1%</td>
</tr>
<tr>
<td align="left">_LIST_APPEND</td>
<td align="right">181,617,418</td>
<td align="right">179,775,414</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_ITER_CHECK_RANGE</td>
<td align="right">594,861,387</td>
<td align="right">589,049,427</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_3</td>
<td align="right">637,508,332</td>
<td align="right">643,687,168</td>
<td align="right">1.0%</td>
</tr>
<tr>
<td align="left">_CHECK_VALIDITY_AND_SET_IP</td>
<td align="right">3,410,772,306</td>
<td align="right">3,377,808,523</td>
<td align="right">-1.0%</td>
</tr>
<tr>
<td align="left">_CREATE_INIT_FRAME</td>
<td align="right">28,560,665</td>
<td align="right">28,298,648</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_CHECK_AND_ALLOCATE_OBJECT</td>
<td align="right">30,358,295</td>
<td align="right">30,091,899</td>
<td align="right">-0.9%</td>
</tr>
<tr>
<td align="left">_LOAD_ATTR_INSTANCE_VALUE_0</td>
<td align="right">2,704,970,099</td>
<td align="right">2,682,097,173</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_RANGE</td>
<td align="right">593,842,827</td>
<td align="right">589,030,227</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_CHECK_PEP_523</td>
<td align="right">22,864,683</td>
<td align="right">22,681,980</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_TO_BOOL_INT</td>
<td align="right">209,099,191</td>
<td align="right">207,481,080</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_TUPLE</td>
<td align="right">424,679,741</td>
<td align="right">421,418,755</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_RANGE</td>
<td align="right">559,302,070</td>
<td align="right">555,082,827</td>
<td align="right">-0.8%</td>
</tr>
<tr>
<td align="left">_BINARY_OP</td>
<td align="right">809,032,275</td>
<td align="right">802,977,766</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_INIT_CALL</td>
<td align="right">42,400,592</td>
<td align="right">42,717,125</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_CHECK_FUNC</td>
<td align="right">42,402,215</td>
<td align="right">42,718,295</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_GEN_FRAME</td>
<td align="right">102,734,896</td>
<td align="right">103,451,900</td>
<td align="right">0.7%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_TUPLE</td>
<td align="right">274,718,690</td>
<td align="right">272,815,377</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SLICE</td>
<td align="right">93,852,919</td>
<td align="right">93,208,038</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_STR_INT</td>
<td align="right">1,002,192,320</td>
<td align="right">995,569,543</td>
<td align="right">-0.7%</td>
</tr>
<tr>
<td align="left">_LOAD_DEREF</td>
<td align="right">882,144,142</td>
<td align="right">876,422,366</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_4</td>
<td align="right">1,237,081,815</td>
<td align="right">1,229,223,965</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GET_YIELD_FROM_ITER</td>
<td align="right">25,864,246</td>
<td align="right">26,024,134</td>
<td align="right">0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_FLOAT</td>
<td align="right">610,908,072</td>
<td align="right">607,416,132</td>
<td align="right">-0.6%</td>
</tr>
<tr>
<td align="left">_GUARD_BOTH_UNICODE</td>
<td align="right">737,389,143</td>
<td align="right">733,397,835</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GET_ITER</td>
<td align="right">739,683,073</td>
<td align="right">736,041,838</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_GUARD_NOT_EXHAUSTED_LIST</td>
<td align="right">2,002,865,241</td>
<td align="right">1,993,158,134</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST_IMMORTAL</td>
<td align="right">34,305,500</td>
<td align="right">34,141,720</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_MAP_ADD</td>
<td align="right">41,853,562</td>
<td align="right">41,663,398</td>
<td align="right">-0.5%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_3</td>
<td align="right">3,297,522,558</td>
<td align="right">3,283,257,743</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_SUBSCR_LIST_INT</td>
<td align="right">2,568,031,174</td>
<td align="right">2,557,584,130</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_FOR_ITER_TIER_TWO</td>
<td align="right">1,396,009,490</td>
<td align="right">1,390,396,264</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP</td>
<td align="right">438,612,730</td>
<td align="right">436,871,592</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS</td>
<td align="right">123,287,317</td>
<td align="right">122,799,264</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_INT</td>
<td align="right">1,388,790,278</td>
<td align="right">1,383,430,449</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_1</td>
<td align="right">1,485,022,225</td>
<td align="right">1,490,726,674</td>
<td align="right">0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_2</td>
<td align="right">2,949,563,956</td>
<td align="right">2,939,088,391</td>
<td align="right">-0.4%</td>
</tr>
<tr>
<td align="left">_LOAD_CONST</td>
<td align="right">3,873,411</td>
<td align="right">3,860,240</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CHECK_METHOD_VERSION_KW</td>
<td align="right">768,354</td>
<td align="right">765,830</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_CALL_STR_1</td>
<td align="right">47,283,731</td>
<td align="right">47,130,180</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_EXPAND_METHOD_KW</td>
<td align="right">768,270</td>
<td align="right">765,830</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_ITER_NEXT_LIST</td>
<td align="right">1,751,408,713</td>
<td align="right">1,745,973,647</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_STR</td>
<td align="right">1,360,918,809</td>
<td align="right">1,356,742,326</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_STORE_FAST_7</td>
<td align="right">1,060,661,160</td>
<td align="right">1,057,645,249</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_INT</td>
<td align="right">174,523,424</td>
<td align="right">174,057,812</td>
<td align="right">-0.3%</td>
</tr>
<tr>
<td align="left">_SET_FUNCTION_ATTRIBUTE</td>
<td align="right">63,130,354</td>
<td align="right">62,973,218</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_LIST_APPEND</td>
<td align="right">1,102,606,183</td>
<td align="right">1,099,961,506</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_CALL_METHOD_DESCRIPTOR_O</td>
<td align="right">179,373,500</td>
<td align="right">178,946,112</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_FLOAT</td>
<td align="right">395,437,181</td>
<td align="right">394,579,825</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_SEND_GEN_FRAME</td>
<td align="right">390,243,693</td>
<td align="right">389,445,368</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BUILD_LIST</td>
<td align="right">531,120,699</td>
<td align="right">532,116,734</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR_LIST_INT</td>
<td align="right">522,387,317</td>
<td align="right">521,488,110</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_MULTIPLY_FLOAT</td>
<td align="right">857,301,915</td>
<td align="right">855,923,148</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_INT</td>
<td align="right">3,859,541,414</td>
<td align="right">3,865,655,123</td>
<td align="right">0.2%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_FLOAT</td>
<td align="right">74,738,305</td>
<td align="right">74,621,160</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_UNICODE</td>
<td align="right">43,033,271</td>
<td align="right">42,966,192</td>
<td align="right">-0.2%</td>
</tr>
<tr>
<td align="left">_LOAD_FAST_7</td>
<td align="right">2,974,996,577</td>
<td align="right">2,970,630,659</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_DELETE_SUBSCR</td>
<td align="right">98,771,791</td>
<td align="right">98,636,390</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GET_AWAITABLE</td>
<td align="right">4,527,364</td>
<td align="right">4,521,546</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_SWAP</td>
<td align="right">1,920,096,011</td>
<td align="right">1,917,848,419</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_ADD_INT</td>
<td align="right">3,076,738,334</td>
<td align="right">3,073,466,550</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_UNPACK_SEQUENCE_LIST</td>
<td align="right">60,652,335</td>
<td align="right">60,590,056</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_LIST_EXTEND</td>
<td align="right">72,549,753</td>
<td align="right">72,494,677</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_CHECK_MANAGED_OBJECT_HAS_VALUES</td>
<td align="right">2,742,577,944</td>
<td align="right">2,744,380,041</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_CALL_INTRINSIC_1</td>
<td align="right">72,535,267</td>
<td align="right">72,494,677</td>
<td align="right">-0.1%</td>
</tr>
<tr>
<td align="left">_GUARD_BUILTINS_VERSION_PUSH_KEYS</td>
<td align="right">35,441,205</td>
<td align="right">35,459,570</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_LOAD_GLOBAL_BUILTINS_FROM_KEYS</td>
<td align="right">35,441,205</td>
<td align="right">35,459,570</td>
<td align="right">0.1%</td>
</tr>
<tr>
<td align="left">_STORE_SLICE</td>
<td align="right">112,471,592</td>
<td align="right">112,425,293</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_COMPARE_OP_INT</td>
<td align="right">2,156,393,286</td>
<td align="right">2,155,539,000</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BINARY_OP_SUBTRACT_FLOAT</td>
<td align="right">270,210,582</td>
<td align="right">270,121,959</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_STORE_SUBSCR</td>
<td align="right">614,599,866</td>
<td align="right">614,427,798</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_BUILD_SLICE</td>
<td align="right">124,946,460</td>
<td align="right">124,920,760</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_SMALL_INT_1</td>
<td align="right">4,329,099,487</td>
<td align="right">4,328,258,253</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GUARD_NOS_FLOAT</td>
<td align="right">468,875,893</td>
<td align="right">468,818,138</td>
<td align="right">-0.0%</td>
</tr>
<tr>
<td align="left">_GET_ANEXT</td>
<td align="right">94,136,760</td>
<td align="right">94,136,760</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_STORE_GLOBAL</td>
<td align="right">3,555,360</td>
<td align="right">3,555,360</td>
<td align="right">0.0%</td>
</tr>
<tr>
<td align="left">_LOAD_NAME</td>
<td align="right">14,752</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_STORE_NAME</td>
<td align="right">4,267</td>
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
<td align="left">_DELETE_ATTR</td>
<td align="right">1,905</td>
<td align="right"></td>
<td align="right"></td>
</tr>
<tr>
<td align="left">_LOAD_BUILD_CLASS</td>
<td align="right">462</td>
<td align="right"></td>
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
<td align="right">126</td>
<td align="right">42</td>
<td align="right">-66.7%</td>
</tr>
<tr>
<td align="left">RAISE_VARARGS</td>
<td align="right">2,059</td>
<td align="right">1,200</td>
<td align="right">-41.7%</td>
</tr>
<tr>
<td align="left">CALL_FUNCTION_EX</td>
<td align="right">52,728</td>
<td align="right">41,647</td>
<td align="right">-21.0%</td>
</tr>
<tr>
<td align="left">SEND</td>
<td align="right">30,654</td>
<td align="right">29,999</td>
<td align="right">-2.1%</td>
</tr>
<tr>
<td align="left">CALL</td>
<td align="right">24,231</td>
<td align="right">24,493</td>
<td align="right">1.1%</td>
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
<td align="right">248</td>
<td align="right">161</td>
<td align="right">-35.1%</td>
</tr>
<tr>
<td align="left">
watched globals modification
<details>
<summary>ⓘ</summary>

A watched `globals()` dict has been modified
</details>
</td>
<td align="right">248</td>
<td align="right">161</td>
<td align="right">-35.1%</td>
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
<td align="right">35</td>
<td align="right">35</td>
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
<td align="right">42</td>
<td align="right">42</td>
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
<td align="right">1,857</td>
<td align="right">1,857</td>
<td align="right">0.0%</td>
</tr>
</tbody>
</table>


</details>

---
Stats gathered on: 2024-11-14
